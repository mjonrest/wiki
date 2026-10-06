"""Downloads item icons and monster pictures from Divine Pride into img/ at the wiki root.

The wiki shows img/items/<id>.png and img/mobs/<id>.png first and falls back to Divine Pride when a picture is
missing, so this only has to run when the database gains new ids. Ids Divine Pride has no picture for are kept
in img/missing.json and skipped next time (pass --retry to try them again).

    python3 source/tools/fetch_images.py            # from the wiki repo root
"""
import argparse
import concurrent.futures
import json
import os
import time
import urllib.error
import urllib.request

SOURCES = {
    "items": ("items.json", "https://static.divine-pride.net/images/items/item/{}.png"),
    "mobs": ("mobs.json", "https://static.divine-pride.net/images/mobs/png/{}.png"),
}


def fetch(url, path):
    """True when saved, False when Divine Pride has no picture, None on a temporary error."""
    req = urllib.request.Request(url, headers={"User-Agent": "MiracleWiki-ImageSync/1.0"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                data = r.read()
            if not data.startswith(b"\x89PNG"):
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

    jobs = []
    for kind, (index, url) in SOURCES.items():
        os.makedirs(os.path.join(img, kind), exist_ok=True)
        with open(os.path.join(args.root, "db", "data", index)) as f:
            ids = sorted({row[0] for row in json.load(f)})
        skip = missing.get(kind, set())
        for i in ids:
            path = os.path.join(img, kind, f"{i}.png")
            if i not in skip and not os.path.exists(path):
                jobs.append((kind, i, url.format(i), path))
    if args.limit:
        jobs = jobs[: args.limit]
    print(f"{len(jobs)} pictures to fetch")

    saved = 0
    with concurrent.futures.ThreadPoolExecutor(args.workers) as pool:
        futures = {pool.submit(fetch, u, p): (k, i) for k, i, u, p in jobs}
        for n, fut in enumerate(concurrent.futures.as_completed(futures), 1):
            kind, i = futures[fut]
            ok = fut.result()
            if ok:
                saved += 1
            elif ok is False:
                missing.setdefault(kind, set()).add(i)
            if n % 1000 == 0:
                print(f"{n}/{len(jobs)} checked, {saved} saved")

    with open(missing_path, "w") as f:
        json.dump({k: sorted(v) for k, v in sorted(missing.items())}, f, separators=(",", ":"))
    print(f"saved {saved}, no picture for {sum(len(v) for v in missing.values())} ids")


if __name__ == "__main__":
    main()
