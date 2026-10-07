"""NPC part of the Database: every visible NPC the server loads, with what it sells, gives, takes and offers.

Used by gen_db.build(); the item pages link back to the NPCs that sell or give an item.
"""
import os
import re
from collections import defaultdict

from rodb import ROOT

SHOP_TYPES = ("shop", "cashshop", "itemshop", "pointshop", "marketshop")
HIDDEN_SPRITES = {-1, 45, 111, 139, 32767}  # FAKE_NPC, WARPNPC, HIDDEN_NPC, HIDDEN_WARP_NPC, INVISIBLE
COLOR = re.compile(r"\^[0-9A-Fa-f]{6}")
STRING = re.compile(r'"((?:[^"\\]|\\.)*)"')
GIVE = re.compile(r"\b(?:getitem|getitem2|getitembound|getitembound2|rentitem|rentitem2|getnameditem)\s*\(?\s*(\d+|[A-Za-z_]\w*)\s*[,)]")
TAKE = re.compile(r"\b(?:delitem|delitem2)\s*\(?\s*(\d+|[A-Za-z_]\w*)\s*[,)]")
WARP = re.compile(r"\bwarp\s*\(?\s*\"([\w@-]+)\"")
INSTANCE = re.compile(r"\binstance_create\s*\(\s*\"([^\"]+)\"")
QUEST = re.compile(r"\bsetquest\s*\(?\s*(\d+)")
ENCHANT_UI = re.compile(r"\bitem_enchant\s*\(?\s*(\d+)")
CALLSHOP = re.compile(r"\bcallshop\s*\(?\s*\"([^\"]+)\"")
SELECT = re.compile(r"\b(?:select|prompt)\s*\(([^;]*)\)")
MENU = re.compile(r"\bmenu\s+(\"[^;]*);")


def sprite_ids():
    """{'4_M_MERCHANT': 86, ...} from the e_job_types enum in src/map/npc.hpp."""
    path = os.path.join(ROOT, "src/map/npc.hpp")
    out = {}
    if not os.path.exists(path):
        return out
    text = open(path, encoding="utf-8", errors="replace").read()
    m = re.search(r"enum e_job_types\s*\{(.*?)\};", text, re.S)
    if not m:
        return out
    val = -1
    for line in m.group(1).splitlines():
        line = re.sub(r"//.*", "", line).strip().rstrip(",")
        e = re.match(r"^(\w+)(?:\s*=\s*(-?\d+))?$", line)
        if not e:
            continue
        val = int(e.group(2)) if e.group(2) is not None else val + 1
        if e.group(1).startswith("JT_"):
            out[e.group(1)[3:]] = val
    return out


def _sprite(token, ids):
    token = token.strip()
    if re.fullmatch(r"-?\d+", token):
        return int(token)
    return ids.get(token.upper(), -1 if token in ("FAKE_NPC", "") else None)


def _text(s):
    return COLOR.sub("", s).replace('\\"', '"').strip()


def _options(body):
    out = []
    for m in SELECT.finditer(body):
        out += [o for s in STRING.findall(m.group(1)) for o in s.split(":")]
    for m in MENU.finditer(body):
        out += STRING.findall(m.group(1))
    seen = []
    for o in (_text(o) for o in out):
        if o and o not in seen and not o.startswith("-") and len(o) < 80:
            seen.append(o)
    return seen[:30]


def _says(body):
    lines = []
    for s in re.findall(r"\bmes\s*\(?\s*\"((?:[^\"\\]|\\.)*)\"", body):
        t = _text(s)
        if t and not re.fullmatch(r"\[.*\]", t):
            lines.append(t)
        if len(lines) == 4:
            break
    return lines


def _items(rx, body, by_aegis, items):
    out = []
    for tok in rx.findall(body):
        iid = int(tok) if tok.isdigit() else by_aegis.get(tok)
        if iid in items and iid not in out:
            out.append(iid)
    return out[:40]


def _shop_sells(t, rest, items, currencies):
    parts = [p.strip() for p in rest.rstrip(";").split(",") if p.strip()][1:]
    if t == "itemshop":
        cur = "item:" + parts.pop(0).split(":")[0] if parts else "Zeny"
    elif t == "pointshop":
        v = parts.pop(0).split(":")[0] if parts else ""
        cur = currencies.get(v, v)
    elif t == "cashshop":
        cur = "Cash Points"
    else:
        cur = "Zeny"
    out = []
    for p in parts:
        iid, _, price = p.partition(":")
        if not iid.strip().isdigit():
            continue
        iid = int(iid)
        price = price.split(":")[0].strip()
        price = int(price) if price.lstrip("-").isdigit() else -1
        if price == -1 and iid in items:
            price = items[iid].get("Buy") or (items[iid].get("Sell") or 0) * 2
        out.append([iid, price, cur])
    return out


def guide_pages(docs_dir):
    """({NPC name: page} for Miracle NPCs a page shows with npc_where("Name"),
    {NPC name: page} for official NPCs a page lists in a `<!-- npcs: A; B -->` comment)."""
    custom, official_npcs = {}, {}
    paths = [os.path.join(root, fn) for root, _, names in os.walk(docs_dir) for fn in names if fn.endswith(".md")]
    # An NPC's own page wins over an overview (index.md) that also mentions it.
    for path in sorted(paths, key=lambda p: (os.path.basename(p) == "index.md", p)):
        text = open(path, encoding="utf-8").read()
        rel = os.path.relpath(path, docs_dir).replace(os.sep, "/")
        for name in re.findall(r'npc_where\(\s*"([^"]+)"', text):
            custom.setdefault(name, rel)
        for group in re.findall(r"<!--\s*npcs:(.*?)-->", text, re.S):
            names = [n.strip() for n in group.split(";") if n.strip()]
            for name in names:
                official_npcs.setdefault(name, (rel, names))
    return custom, official_npcs


def build(items, by_aegis, docs_dir=None):
    """(index rows, {id: detail}, {item id: [shop rows]}, {item id: [npc ids that give it]},
    {enchant system id: [npc ids that open it]})."""
    import main
    import official

    ids = sprite_ids()
    quests = official.quest_db()
    files = [f for f in dict.fromkeys(official.instance_scripts() + main.enabled_scripts())
             if os.path.exists(os.path.join(ROOT, f))]

    # Pass 1: every definition, by unique name, so duplicates and callshop can find their source.
    defs, order = {}, []
    for rel in files:
        for m, body in official.blocks(rel):
            head = body.split("\n", 1)[0].split("\t")
            if len(head) < 4 or head[0] == "function":
                continue
            raw = head[2]
            exname = raw.split("::")[1] if "::" in raw else raw
            d = {"raw": raw, "name": main.display_name(raw), "type": head[1], "rest": head[3], "body": body,
                 "file": rel, "map": m.group("map"), "x": int(m.group("x") or 0), "y": int(m.group("y") or 0)}
            defs.setdefault(exname, d)
            if d["map"]:
                order.append(d)

    barters = main.barters()
    floating_sells = {}
    for ex, d in defs.items():
        if d["type"] in SHOP_TYPES:
            floating_sells[ex] = _shop_sells(d["type"], d["rest"], items, main.CURRENCIES)

    def barter_rows(shop):
        rows = []
        for e in shop.get("Items") or []:
            iid = by_aegis.get(e.get("Item"))
            if iid is None:
                continue
            cost = [[by_aegis.get(r.get("Item")), r.get("Amount", 1)] for r in e.get("RequiredItems") or []]
            if e.get("Zeny"):
                cost.append(["zeny", e["Zeny"]])
            rows.append([iid, [c for c in cost if c[0] is not None]])
        return rows

    # Pass 2: visible NPCs, merging duplicates of one source into one entry with several locations.
    npcs = {}
    for d in order:
        t = d["type"]
        src = d
        if t.startswith("duplicate("):
            src = defs.get(t[len("duplicate("):-1]) or d
        sprite = _sprite(d["rest"].split(",")[0], ids)
        if sprite in HIDDEN_SPRITES or not re.search(r"[^\W_]", d["name"]):
            continue
        # One entry per NPC: duplicates join their source, and the same NPC defined in two loaded files merges.
        key = (src["name"], src["map"], src["x"], src["y"]) if src["map"] else (src["raw"], src["file"])
        n = npcs.get(key)
        if n:
            loc = [d["map"], d["x"], d["y"]]
            if loc not in n["locs"]:
                n["locs"].append(loc)
            if src["raw"] not in n["raws"] and src["type"] in SHOP_TYPES:  # two shops stacked on one spot
                n["raws"].append(src["raw"])
                have = {r[0] for r in n.get("sells", [])}
                n.setdefault("sells", []).extend(r for r in _shop_sells(src["type"], src["rest"], items, main.CURRENCIES)
                                                 if r[0] not in have)
            continue
        body = src["body"] if src["type"] == "script" or src["type"].startswith("script") else ""
        n = npcs[key] = {"name": d["name"], "sprite": sprite if sprite is not None else -1, "file": src["file"],
                         "locs": [[d["map"], d["x"], d["y"]]], "raws": [src["raw"]]}
        if src["type"] in SHOP_TYPES:
            n["sells"] = floating_sells.get(src["raw"].split("::")[-1]) or _shop_sells(src["type"], src["rest"], items, main.CURRENCIES)
        if body:
            for k, v in (("says", _says(body)), ("menu", _options(body)),
                         ("gives", _items(GIVE, body, by_aegis, items)), ("takes", _items(TAKE, body, by_aegis, items)),
                         ("warps", list(dict.fromkeys(w for w in WARP.findall(body) if w not in ("SavePoint", "Random")))[:20]),
                         ("instances", list(dict.fromkeys(INSTANCE.findall(body)))),
                         ("enchants", [int(e) for e in dict.fromkeys(ENCHANT_UI.findall(body))]),
                         ("quests", [[int(q), quests.get(int(q), {}).get("Title", "")] for q in dict.fromkeys(QUEST.findall(body))][:30])):
                if v:
                    n[k] = v
            sells, trades = [], []
            for shop in dict.fromkeys(CALLSHOP.findall(body)):
                if shop in floating_sells:
                    sells += floating_sells[shop]
                elif shop in barters:
                    trades += barter_rows(barters[shop])
            if sells:
                n["sells"] = sells[:400]
            if trades:
                n["barter"] = trades[:400]
    for name, shop in barters.items():
        if shop.get("Map"):
            spr = _sprite(str(shop.get("Sprite", "4_M_MERCHANT")), ids)
            npcs[("barter", name)] = {"name": main.display_name(name.replace("_", " ")), "sprite": spr if spr is not None else -1,
                                       "file": "npc/custom/barters.yml",
                                       "locs": [[shop["Map"], shop.get("X", 0), shop.get("Y", 0)]],
                                       "barter": barter_rows(shop)}

    custom, official_npcs = guide_pages(docs_dir) if docs_dir else ({}, {})
    files_of = defaultdict(set)
    for n in npcs.values():
        files_of[n["name"]].add(n["file"])
    for n in npcs.values():
        if n["file"].startswith(("npc/miracle/", "npc/custom/")):
            if n["name"] in custom:
                n["page"] = custom[n["name"]]
        elif n["name"] in official_npcs:
            page, names = official_npcs[n["name"]]
            # A common name ("Lisa") links only the copy in the same script as the page's other NPCs.
            near = set().union(*(files_of[o] for o in names if o != n["name"])) if len(names) > 1 else set()
            if len(files_of[n["name"]]) == 1 or not near or n["file"] in near:
                n["page"] = page
    index, detail = [], {}
    sold_by, given_by, enchanters = defaultdict(list), defaultdict(list), defaultdict(list)
    for nid, n in enumerate(sorted(npcs.values(), key=lambda n: (n["name"].lower(), n["locs"][0])), 1):
        kinds = [k for k, f in (("Shop", "sells"), ("Barter", "barter"), ("Quest", "quests"), ("Instance", "instances"), ("Enchanter", "enchants"),
                                ("Warper", "warps"), ("Gives items", "gives")) if n.get(f)]
        group = "Miracle" if n["file"].startswith(("npc/miracle/", "npc/custom/")) else "Official"
        m, x, y = n["locs"][0]
        index.append([nid, n["name"], m, x, y, n["sprite"], "|".join(kinds), group, len(n["locs"])])
        detail[nid] = {k: v for k, v in n.items() if k not in ("name", "sprite", "raws")}
        for iid, price, cur in n.get("sells", []):
            sold_by[iid].append([n["name"], m, x, y, price, cur, nid])
        for iid, cost in n.get("barter", []):
            sold_by[iid].append([n["name"], m, x, y, 0, {"barter": cost}, nid])
        for iid in n.get("gives", []):
            given_by[iid].append(nid)
        for e in n.get("enchants", []):
            enchanters[e].append(nid)
    return index, detail, sold_by, given_by, enchanters
