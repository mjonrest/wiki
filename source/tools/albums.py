"""Bonus rolls that item scripts add through a script function, such as the jRO card roll of the card albums
(Old Card Album: callfunc "F_GetJROCard"; then getgroupitem(IG_CardAlbum)).

The function is read as tiers: `.@roll = rand(N)`, then `if (.@roll < A) { ... setarray .@Pool ... }
else if (.@roll < B) { ... }`, each tier giving one random item of its pool.
"""
import functools
import os
import re

from rodb import ROOT

FUNC = re.compile(r"^function\tscript\t(\w+)\t\{", re.M)
CALL = re.compile(r'callfunc\s*\(?\s*"(\w+)"')


@functools.lru_cache(None)
def functions():
    """{function name: (file, body)} for script functions in every loaded custom script."""
    import main
    out = {}
    for rel in main.enabled_scripts():
        if not os.path.exists(os.path.join(ROOT, rel)):
            continue
        text = main.script_text(rel)
        for m in FUNC.finditer(text):
            depth, i = 1, m.end()
            while i < len(text) and depth:
                depth += {"{": 1, "}": -1}.get(text[i], 0)
                i += 1
            out.setdefault(m.group(1), (rel, text[m.end():i - 1]))
    return out


def tiers(body):
    """[{"name", "chance" (percent), "items": [ids]}] or [] when the function is not a tiered roll."""
    m = re.search(r"(\.@\w+)\s*=\s*rand\(\s*(\d+)\s*\)\s*;", body)
    if not m:
        return []
    var, total = m.group(1), int(m.group(2))
    cuts = list(re.finditer(r"if\s*\(\s*" + re.escape(var) + r"\s*<\s*(\d+)\s*\)", body))
    out, prev = [], 0
    for k, c in enumerate(cuts):
        end = cuts[k + 1].start() if k + 1 < len(cuts) else len(body)
        part = body[c.end():end]
        pool = re.search(r"setarray\s+\.@\w+(?:\[\d+\])?\s*,([^;]+);", part)
        if not pool:
            continue
        ids = [int(x) for x in re.findall(r"\d+", pool.group(1))]
        name = re.search(r'\.@rarity\$\s*=\s*"([^"]*)"', part)
        hi = int(c.group(1))
        out.append({"name": name.group(1) if name else f"Tier {k + 1}", "chance": (hi - prev) * 100 / total,
                    "items": list(dict.fromkeys(ids))})
        prev = hi
    return out


@functools.lru_cache(None)
def bonus_rolls():
    """[{"function", "file", "boxes": [item ids whose script calls it], "tiers": [...]}]."""
    import ydb
    items = ydb.items()
    funcs = functions()
    found = {}
    for iid, it in sorted(items.items()):
        for name in CALL.findall(str(it.get("Script") or "")):
            if name in funcs:
                found.setdefault(name, []).append(iid)
    out = []
    for name, boxes in found.items():
        rel, body = funcs[name]
        t = tiers(body)
        if t:
            out.append({"function": name, "file": rel, "boxes": boxes, "tiers": t})
    return out


def box_rows():
    """{box id: [[item id, chance percent], ...]} for the item pages ("Found in" / "Contents")."""
    out = {}
    for r in bonus_rolls():
        for box in r["boxes"]:
            rows = out.setdefault(box, [])
            for t in r["tiers"]:
                each = round(t["chance"] / len(t["items"]), 4)
                rows += [[i, each] for i in t["items"]]
    return out
