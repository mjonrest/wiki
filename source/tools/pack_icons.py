"""Packs the small 24×24 icons (items and skills) into a few sprite sheets in img/sheets/.

Thirty thousand tiny PNG files take far more disk than their bytes (every file uses at least one disk block) and
make every git checkout slow. The sheets hold each distinct picture once, and img/icons.json says where each
id's picture is:

    {"cols": 32, "rows": 32, "cell": 24, "items": [id, slot, id, slot, ...], "skills": [...]}

Slot n is on sheet n // (cols*rows), at column n % cols and row n // cols % rows. Packing is append-only: pictures
already in a sheet keep their slot, and new pictures go after the last one, so a sync only changes the last sheet
and the index.

    python3 source/tools/pack_icons.py        # from the wiki repo root: moves img/items/*.png and img/skills/*.png
                                              # into the sheets and deletes the loose files
"""
import argparse
import hashlib
import json
import os

from PIL import Image

KINDS = ("items", "skills")
COLS = ROWS = 32
CELL = 24
PER_SHEET = COLS * ROWS


def _sheet_path(img, kind, n):
    return os.path.join(img, "sheets", f"{kind}-{n}.png")


def load_index(img):
    path = os.path.join(img, "icons.json")
    if not os.path.exists(path):
        return {}
    with open(path) as f:
        data = json.load(f)
    return {k: dict(zip(data[k][::2], data[k][1::2])) for k in KINDS if k in data}


def _cell(im):
    """The picture centred on a CELL×CELL transparent square (a few icons are 18×18 or 22×24)."""
    im = im.convert("RGBA")
    if im.size == (CELL, CELL):
        return im
    im.thumbnail((CELL, CELL))
    out = Image.new("RGBA", (CELL, CELL))
    out.paste(im, ((CELL - im.width) // 2, (CELL - im.height) // 2))
    return out


def _key(im):
    return hashlib.sha1(im.tobytes()).hexdigest()


def pack(img, new):
    """Adds {kind: {id: png path}} to the sheets and rewrites the index; returns {kind: pictures added}."""
    index = load_index(img)
    added = {}
    os.makedirs(os.path.join(img, "sheets"), exist_ok=True)
    for kind in KINDS:
        slots = index.get(kind, {})
        files = new.get(kind) or {}
        if not files and kind in index:
            continue
        sheets, seen = {}, {}

        def sheet(n):
            if n not in sheets:
                p = _sheet_path(img, kind, n)
                sheets[n] = Image.open(p).convert("RGBA") if os.path.exists(p) else \
                    Image.new("RGBA", (COLS * CELL, ROWS * CELL))
            return sheets[n]

        def box(slot):
            x, y = slot % COLS * CELL, slot // COLS % ROWS * CELL
            return x, y, x + CELL, y + CELL

        # Pictures already packed, so a new id with the same picture reuses its slot.
        for slot in sorted(set(slots.values())):
            seen.setdefault(_key(sheet(slot // PER_SHEET).crop(box(slot))), slot)
        nxt = max(slots.values(), default=-1) + 1
        changed = set()
        for pid in sorted(files):
            with Image.open(files[pid]) as im:
                cell = _cell(im)
            k = _key(cell)
            if k not in seen:
                seen[k] = nxt
                sheet(nxt // PER_SHEET).paste(cell, box(nxt)[:2])
                changed.add(nxt // PER_SHEET)
                nxt += 1
            slots[pid] = seen[k]
        for n in changed:
            sheets[n].save(_sheet_path(img, kind, n), optimize=True)
        index[kind] = slots
        added[kind] = len(files)
    out = {"cols": COLS, "rows": ROWS, "cell": CELL}
    for kind in KINDS:
        out[kind] = [v for pid in sorted(index.get(kind, {})) for v in (pid, index[kind][pid])]
    with open(os.path.join(img, "icons.json"), "w") as f:
        json.dump(out, f, separators=(",", ":"))
    return added


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".", help="wiki root (holds img)")
    args = ap.parse_args()
    img = os.path.join(args.root, "img")
    loose = {}
    for kind in KINDS:
        folder = os.path.join(img, kind)
        if os.path.isdir(folder):
            loose[kind] = {int(f[:-4]): os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".png")}
    added = pack(img, loose)
    for kind, files in loose.items():
        for p in files.values():
            os.remove(p)
        if not os.listdir(os.path.join(img, kind)):
            os.rmdir(os.path.join(img, kind))
    print("packed", added)


if __name__ == "__main__":
    main()
