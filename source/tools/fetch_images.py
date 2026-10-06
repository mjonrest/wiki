"""Downloads item icons, monster pictures, skill icons and NPC pictures from Divine Pride into img/ at the wiki root.

The wiki only shows pictures saved in img/<kind>/<id>.png, so this runs whenever the database gains new ids.
Ids Divine Pride has no picture for are kept in img/missing.json and skipped next time (pass --retry to try them
again).

    python3 source/tools/fetch_images.py            # from the wiki repo root
"""
import argparse
import hashlib
import concurrent.futures
import json
import os
import time
import urllib.error
import urllib.request
from collections import defaultdict

# kind: (index file, how to read ids from it, URLs to try in order)
SOURCES = {
    "items": ("items.json", lambda rows: [r[0] for r in rows], ["https://static.divine-pride.net/images/items/item/{}.png"]),
    "mobs": ("mobs.json", lambda rows: [r[0] for r in rows], ["https://static.divine-pride.net/images/mobs/png/{}.png"]),
    "skills": ("skills.json", lambda rows: [r["id"] for r in rows], ["https://static.divine-pride.net/images/skill/{}.png"]),
    # NPC sprite ids; ids in the monster range use the monster picture instead.
    "npcs": ("npcs.json", lambda rows: [r[5] for r in rows if 0 < r[5] and not 1001 <= r[5] < 4000],
             ["https://static.divine-pride.net/images/npc/{}.png", "https://static.divine-pride.net/images/npcs/{}.png"]),
}


# Divine Pride answers ids it has no picture for with this "no image" picture instead of a 404.
PLACEHOLDERS = {"90fd5dfc46354798fa8fc4cbcec9dee97d8071b75abc58951ab1887b11cd916e"}


def _placeholder(data):
    return hashlib.sha256(data).hexdigest() in PLACEHOLDERS


def fetch(urls, path):
    """True when saved, False when no URL has a picture, None on a temporary error."""
    result = False
    for url in urls:
        r = _fetch_one(url, path)
        if r:
            return True
        if r is None:
            result = None
    return result


def _fetch_one(url, path):
    req = urllib.request.Request(url, headers={"User-Agent": "MiracleWiki-ImageSync/1.0"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                data = r.read()
            if not data.startswith(b"\x89PNG") or _placeholder(data):
                return False
            with open(path, "wb") as f:
                f.write(data)
            return True
        except urllib.error.HTTPError as e:
            if e.code in (403, 404):
                return False
        except (urllib.error.URLError, TimeoutError, ConnectionError):
            pass
        time.sleep(2 ** attempt)
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".", help="wiki root (holds db/data and img)")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--retry", action="store_true", help="try ids recorded as missing again")
    ap.add_argument("--limit", type=int, default=0, help="stop after this many downloads (0 = all)")
    args = ap.parse_args()

    img = os.path.join(args.root, "img")
    missing_path = os.path.join(img, "missing.json")
    missing = {}
    if os.path.exists(missing_path) and not args.retry:
        with open(missing_path) as f:
            missing = {k: set(v) for k, v in json.load(f).items()}

    # Drop placeholders saved before they were recognised.
    removed = 0
    for kind in SOURCES:
        folder = os.path.join(img, kind)
        for fn in os.listdir(folder) if os.path.isdir(folder) else []:
            path = os.path.join(folder, fn)
            with open(path, "rb") as f:
                if _placeholder(f.read()):
                    os.remove(path)
                    missing.setdefault(kind, set()).add(int(fn.split(".")[0]))
                    removed += 1
    if removed:
        print(f"removed {removed} placeholder pictures")

    jobs = []
    for kind, (index, read_ids, urls) in SOURCES.items():
        os.makedirs(os.path.join(img, kind), exist_ok=True)
        path = os.path.join(args.root, "db", "data", index)
        if not os.path.exists(path):
            continue
        with open(path) as f:
            ids = sorted(set(read_ids(json.load(f))))
        skip = missing.get(kind, set())
        for i in ids:
            out = os.path.join(img, kind, f"{i}.png")
            if i not in skip and not os.path.exists(out):
                jobs.append((kind, i, [u.format(i) for u in urls], out))
    if args.limit:
        jobs = jobs[: args.limit]
    print(f"{len(jobs)} pictures to fetch")

    saved = defaultdict(int)
    with concurrent.futures.ThreadPoolExecutor(args.workers) as pool:
        futures = {pool.submit(fetch, u, p): (k, i) for k, i, u, p in jobs}
        for n, fut in enumerate(concurrent.futures.as_completed(futures), 1):
            kind, i = futures[fut]
            ok = fut.result()
            if ok:
                saved[kind] += 1
            elif ok is False:
                missing.setdefault(kind, set()).add(i)
            if n % 1000 == 0:
                print(f"{n}/{len(jobs)} checked, {sum(saved.values())} saved")

    with open(missing_path, "w") as f:
        json.dump({k: sorted(v) for k, v in sorted(missing.items())}, f, separators=(",", ":"))
    for kind in SOURCES:
        print(f"{kind}: saved {saved[kind]}, no picture for {len(missing.get(kind, ()))}")


if __name__ == "__main__":
    main()
