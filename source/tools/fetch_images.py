"""Downloads item icons, monster pictures and skill icons from Divine Pride, and NPC pictures from ai4rei's NPC list
(nn.ai4rei.net/dev/npclist), into img/ at the wiki root.

The wiki only shows pictures saved in img/, so this runs whenever the database gains new ids. Monster and NPC
pictures stay as img/<kind>/<id>.png; item and skill icons are packed into sprite sheets by pack_icons.py.
Ids no site has a picture for are kept in img/missing.json and skipped next time (pass --retry to try them
again).

    python3 source/tools/fetch_images.py            # from the wiki repo root
"""
import argparse
import hashlib
import concurrent.futures
import json
import os
import shutil
import tempfile
import time
import urllib.error
import urllib.request
from collections import defaultdict

from PIL import Image

import pack_icons

# kind: (index file, how to read ids from it, URLs to try in order; {id} is the id and {name} the NPC sprite name)
SOURCES = {
    "items": ("items.json", lambda rows: [r[0] for r in rows], ["https://static.divine-pride.net/images/items/item/{}.png"]),
    "mobs": ("mobs.json", lambda rows: [r[0] for r in rows], ["https://static.divine-pride.net/images/mobs/png/{}.png"]),
    "skills": ("skills.json", lambda rows: [r["id"] for r in rows], ["https://static.divine-pride.net/images/skill/{}.png"]),
    # NPC sprite ids; ids in the monster range use the monster picture instead.
    "npcs": ("npcs.json", lambda rows: [r[5] for r in rows if 0 < r[5] and not 1001 <= r[5] < 4000],
             ["http://nn.ai4rei.net/dev/npclist/i/{name}.gif"]),
}
# Bump a kind's number when its URLs change, so the ids the old URLs had no picture for are tried again.
SOURCE_VERSION = {"npcs": 2}


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
            if data.startswith(b"GIF8"):
                return _save_gif(data, path)
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


def _save_gif(data, path):
    """The first frame of an animated GIF sprite as a PNG, cropped to the sprite."""
    import io
    with Image.open(io.BytesIO(data)) as im:
        im.seek(0)
        im = im.convert("RGBA")
    box = im.getchannel("A").getbbox()
    if not box:
        return False
    im.crop(box).save(path, optimize=True)
    return True


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
            saved_missing = json.load(f)
        versions = saved_missing.pop("_versions", {})
        missing = {k: set(v) for k, v in saved_missing.items()
                   if versions.get(k, 1) == SOURCE_VERSION.get(k, 1)}

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

    packed = pack_icons.load_index(img)
    tmp = tempfile.mkdtemp()
    jobs = []
    for kind, (index, read_ids, urls) in SOURCES.items():
        folder = os.path.join(tmp, kind) if kind in pack_icons.KINDS else os.path.join(img, kind)
        os.makedirs(folder, exist_ok=True)
        path = os.path.join(args.root, "db", "data", index)
        if not os.path.exists(path):
            continue
        with open(path) as f:
            ids = sorted(set(read_ids(json.load(f))))
        names = {}
        if kind == "npcs":
            names_path = os.path.join(args.root, "db", "data", "npc_sprites.json")
            if os.path.exists(names_path):
                with open(names_path) as f:
                    names = {int(k): v for k, v in json.load(f).items()}
            print(f"npcs: {len(ids)} sprite ids, {len(names)} sprite names")
        skip = missing.get(kind, set())
        have = packed.get(kind, {})
        for i in ids:
            out = os.path.join(folder, f"{i}.png")
            todo = [u.format(i, id=i, name=names.get(i, "")) for u in urls if "{name}" not in u or i in names]
            if todo and i not in skip and i not in have and not os.path.exists(out):
                jobs.append((kind, i, todo, out))
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

    new = {k: {int(f[:-4]): os.path.join(tmp, k, f) for f in os.listdir(os.path.join(tmp, k))}
           for k in pack_icons.KINDS if os.path.isdir(os.path.join(tmp, k))}
    if any(new.values()) or not os.path.exists(os.path.join(img, "icons.json")):
        pack_icons.pack(img, new)
    shutil.rmtree(tmp, ignore_errors=True)

    with open(missing_path, "w") as f:
        out = {k: sorted(v) for k, v in sorted(missing.items())}
        out["_versions"] = SOURCE_VERSION
        json.dump(out, f, separators=(",", ":"))
    for kind in SOURCES:
        print(f"{kind}: saved {saved[kind]}, no picture for {len(missing.get(kind, ()))}")


if __name__ == "__main__":
    main()
