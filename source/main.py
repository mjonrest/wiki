"""mkdocs-macros entry point.

Every table of items, prices, enchants and NPC locations on the wiki is read
from the server files at build time, so the wiki stays in sync with the
scripts: edit an NPC, rebuild, and the page updates.
"""
import os
import re
import sys
import functools
from collections import OrderedDict

import yaml

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "tools"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rodb  # noqa: E402
from rodb import ROOT, item_name, item_id, mob_name  # noqa: E402
import official  # noqa: E402

# Point variables players see as currencies.
CURRENCIES = {
    "#CASHPOINTS": "Cash Points",
    "#KAFRAPOINTS": "Kafra Points",
    "#instance_points": "Instance Points",
    "#Mission_Points": "Mission Points",
    "#EVENTVARIABLE": "Event Points",
    "#card_point": "Card Points",
    "AncientToken": "Ancient Tokens",
    "#Goldpc_Points": "Hourly Points",
    "#PvpPoints": "PvP Points",
    "#HourlyRewards": "Activity Points",
}

NPC_HEADER = re.compile(
    r"^(?P<map>[\w@-]+),(?P<x>\d+),(?P<y>\d+),\d+\t"
    r"(?P<type>script|shop|cashshop|itemshop|pointshop|marketshop|duplicate\([^)]*\)|warp)\t"
    r"(?P<name>[^\t]+)\t(?P<rest>.*)$"
)
FLOAT_SHOP = re.compile(r"^-\t(?P<type>shop|cashshop|itemshop|pointshop|marketshop)\t(?P<name>[^\t]+)\t(?P<rest>.*)$")


def _read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8", errors="replace") as f:
        return f.read().replace("\ufffd", "")


def _strip_comments(text):
    """Remove /* */ blocks and // line comments (good enough for rAthena scripts)."""
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    return "\n".join(re.sub(r"(^|\s)//.*$", "", line) for line in text.split("\n"))


@functools.lru_cache(None)
def enabled_scripts():
    """Script files loaded by npc/scripts_custom.conf (uncommented `npc:` lines)."""
    files = []
    for line in _read("npc/scripts_custom.conf").splitlines():
        m = re.match(r"^npc:\s*(\S.*?)\s*$", line)
        if m:
            files.append(m.group(1))
    return files


@functools.lru_cache(None)
def script_text(rel):
    return _strip_comments(_read(rel))


def display_name(raw):
    """'Quest Shop#1' -> 'Quest Shop', 'Kafra Employee::kaf' -> 'Kafra Employee'."""
    return raw.split("::")[0].split("#")[0].strip()


@functools.lru_cache(None)
def npcs():
    """All visible NPCs in enabled scripts: list of dicts (name, map, x, y, file)."""
    out = []
    for rel in enabled_scripts():
        if not os.path.exists(os.path.join(ROOT, rel)):
            continue
        for line in script_text(rel).splitlines():
            m = NPC_HEADER.match(line)
            if not m or m.group("type") == "warp":
                continue
            out.append(dict(name=display_name(m.group("name")), raw=m.group("name"), map=m.group("map"),
                            x=int(m.group("x")), y=int(m.group("y")), file=rel, type=m.group("type")))
    return out


@functools.lru_cache(None)
def shops():
    """Every shop definition in enabled scripts, keyed by its unique name."""
    out = {}
    for rel in enabled_scripts():
        if not os.path.exists(os.path.join(ROOT, rel)):
            continue
        for line in script_text(rel).splitlines():
            m = FLOAT_SHOP.match(line) or NPC_HEADER.match(line)
            if not m or m.group("type") not in ("shop", "cashshop", "itemshop", "pointshop", "marketshop"):
                continue
            parts = [p.strip() for p in m.group("rest").rstrip(";").split(",") if p.strip()]
            parts = parts[1:]  # sprite
            currency = None
            if m.group("type") == "itemshop":
                currency = ("item", int(parts.pop(0).split(":")[0]))
            elif m.group("type") == "pointshop":
                currency = ("var", parts.pop(0).split(":")[0])
            elif m.group("type") == "cashshop":
                currency = ("var", "#CASHPOINTS")
            else:
                currency = ("zeny", None)
            entries = []
            for p in parts:
                if ":" not in p:
                    continue  # discount flag like "no"
                iid, price = p.split(":")[:2]
                if not iid.strip().isdigit():
                    continue
                entries.append((int(iid), int(price)))
            out[m.group("name").strip()] = dict(type=m.group("type"), currency=currency, items=entries, file=rel)
    return out


@functools.lru_cache(None)
def barters():
    out = {}
    for rel in ("npc/re/merchants/barters.yml", "npc/custom/barters.yml"):
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            continue
        data = yaml.safe_load(_read(rel)) or {}
        for shop in data.get("Body") or []:
            out[shop["Name"]] = shop
    return out


# ---------------------------------------------------------------- rendering

def fmt(n):
    return f"{int(n):,}"


# Pictures are hotlinked from Divine Pride; custom Miracle ids have none, so a failed image removes itself.
REMOTE_PIC = {"items": "https://static.divine-pride.net/images/items/item/{}.png",
              "mobs": "https://static.divine-pride.net/images/mobs/png/{}.png"}
_PIC_ERR = "var a=this.getAttribute('data-alt');if(a){this.removeAttribute('data-alt');this.src=a}else this.remove()"


def _site_root():
    """Relative path from the rendered page's URL to the site root (raw HTML is not rewritten by MkDocs)."""
    page = getattr(ENV, "page", None)
    url = getattr(page, "url", "") or ""
    return "../" * url.count("/")


def pic(kind, pid, cls):
    """<img> for a picture saved in img/ (tools/fetch_images.py), falling back to Divine Pride, then to nothing."""
    return (f'<img class="{cls}" src="{_site_root()}img/{kind}/{pid}.png" data-alt="{REMOTE_PIC[kind].format(pid)}" '
            f'alt="" loading="lazy" onerror="{_PIC_ERR}">')
ENV = None  # set by define_env; ENV.page is the page being rendered


def _root():
    """Relative path from the page being rendered to the docs root."""
    page = getattr(ENV, "page", None)
    src = getattr(getattr(page, "file", None), "src_uri", "") or ""
    return "../" * src.count("/")


def _md_text(s):
    return str(s).replace("[", "\\[").replace("]", "\\]").replace("|", "\\|")


def item(iid):
    """Item icon and name, linked to its Database entry, with its id."""
    iid = int(iid)
    icon = pic("items", iid, "ico")
    return f'{icon}[{_md_text(item_name(iid))}]({_root()}db/items.md#{iid}) <small class="iid">#{iid}</small>'


def mob(mid, size="sm"):
    """Monster picture and name, linked to its Database entry."""
    mid = int(mid)
    img = pic("mobs", mid, f"mob-{size}")
    return f'{img}[{_md_text(mob_name(mid))}]({_root()}db/monsters.md#{mid}) <small class="iid">#{mid}</small>'


def currency_label(currency):
    kind, value = currency
    if kind == "zeny":
        return "Zeny"
    if kind == "item":
        return item_name(value)
    return CURRENCIES.get(value, value)


def _details(title, body, open_=False):
    return (f'<details class="abstract shop" markdown="1"{" open" if open_ else ""}>\n'
            f"<summary>{title}</summary>\n\n{body}\n\n</details>\n")


def _table(header, rows):
    out = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def shop(name, title=None, collapsed=None):
    """Price list of a shop / pointshop / itemshop / barter, by its script name."""
    if name in barters():
        return barter(name, title, collapsed)
    s = shops().get(name)
    if not s:
        return f'!!! warning "Shop `{name}` not found"\n    It is not defined in any enabled script.\n'
    cur = currency_label(s["currency"])
    rows = []
    for iid, price in s["items"]:
        if price < 0:
            buy = rodb.items()[0].get(iid, {}).get("buy")
            price_txt = f"{fmt(buy)} (default)" if buy else "default"
        else:
            price_txt = fmt(price)
        rows.append((item(iid), price_txt))
    body = _table(["Item", f"Price ({cur})"], rows)
    title = title or name
    if collapsed is None:
        collapsed = len(rows) > 15
    if collapsed:
        return _details(f"{title} <span class=\"count\">{len(rows)} items · paid in {cur}</span>", body)
    return f"*Paid in **{cur}**.*\n\n{body}\n"


def _aegis_item(aegis):
    iid = item_id(aegis)
    return item(iid) if iid else f"{aegis}"


def barter(name, title=None, collapsed=None):
    b = barters().get(name)
    if not b:
        return f'!!! warning "Barter `{name}` not found"\n'
    rows = []
    for it in b.get("Items") or []:
        req = []
        if it.get("Zeny"):
            req.append(f"{fmt(it['Zeny'])} Zeny")
        for r in it.get("RequiredItems") or []:
            ref = f" +{r['Refine']}" if r.get("Refine") else ""
            req.append(f"{r.get('Amount', 1)}× {_aegis_item(r['Item'])}{ref}")
        rows.append((_aegis_item(it["Item"]), "<br>".join(req) or "free"))
    body = _table(["You get", "You give"], rows)
    title = title or name
    if collapsed is None:
        collapsed = len(rows) > 15
    if collapsed:
        return _details(f"{title} <span class=\"count\">{len(rows)} items</span>", body)
    return body + "\n"


def shops_in(rel, skip=()):
    """Every placed shop NPC in one script file, each as a collapsible price list."""
    out = []
    for n in npcs():
        if n["file"] == rel and n["type"] in ("shop", "cashshop", "itemshop", "pointshop", "marketshop") \
                and n["raw"] not in skip:
            out.append(shop(n["raw"], title=n["name"], collapsed=True))
    return "\n".join(out)


def items_table(ids, header="Item"):
    return _table([header], [(item(i),) for i in ids]) + "\n"


def items_list(ids):
    return ", ".join(item(i) for i in ids)


# ---------------------------------------------------------------- script data

def npc_block(rel, npc):
    """Text of one NPC definition (from its header to the next top-level header)."""
    text = script_text(rel)
    lines = text.split("\n")
    start = None
    for i, line in enumerate(lines):
        m = NPC_HEADER.match(line) or re.match(r"^(-|function)\t(script)\t(?P<name>[^\t]+)\t", line)
        if m and start is not None:
            return "\n".join(lines[start:i])
        if m and display_name(m.group("name")) == npc or (m and m.group("name").strip() == npc):
            start = i
    return "\n".join(lines[start:]) if start is not None else ""


def arrays(rel, npc=None):
    """All `setarray .Var[...], a, b, c;` in a script (or one NPC of it) -> {Var: [values]}."""
    text = npc_block(rel, npc) if npc else script_text(rel)
    out = OrderedDict()
    for m in re.finditer(r"setarray\s+(\.@?[\w$]+)(?:\[[^\]]*\])?\s*,(.*?);", text, re.S):
        name = m.group(1).lstrip(".@")
        vals = [v.strip().strip('"') for v in m.group(2).split(",") if v.strip()]
        vals = [int(v) if re.fullmatch(r"-?\d+", v) else v for v in vals]
        out.setdefault(name, [])
        out[name] += vals
    return out


def array_seq(rel, npc, var):
    """Each separate `setarray <var>` in one NPC/function, in order (for tiered pools)."""
    text = npc_block(rel, npc)
    out = []
    for m in re.finditer(r"setarray\s+\.@?" + re.escape(var) + r"(?:\[[^\]]*\])?\s*,(.*?);", text, re.S):
        out.append([int(v) for v in re.findall(r"-?\d+", m.group(1))])
    return out


def scalar(rel, var, npc=None):
    text = npc_block(rel, npc) if npc else script_text(rel)
    m = re.search(r"(?:set\s+)?\.@?" + re.escape(var) + r"\s*(?:=|,)\s*(-?\d+)\s*;", text)
    return int(m.group(1)) if m else None


def quest_shop(shop_id):
    """Rewards of one tab of the Quest Shop (npc/miracle/quest_shop.txt)."""
    text = script_text("npc/miracle/quest_shop.txt")
    rows = []
    for m in re.finditer(r"^\s*Add\(([^)]*)\);", text, re.M):
        a = [int(x) for x in m.group(1).split(",")]
        if a[0] != shop_id:
            continue
        req = []
        if a[3]:
            req.append(f"{fmt(a[3])} Zeny")
        if a[4]:
            req.append(f"{fmt(a[4])} Cash Points")
        for i in range(5, len(a), 2):
            req.append(f"{a[i + 1]}× {item(a[i])}")
        amt = f"{a[2]}× " if a[2] > 1 else ""
        rows.append((amt + item(a[1]), "<br>".join(req)))
    if not rows:
        return "*This tab is currently empty.*\n"
    return _table(["Reward", "Requirements"], rows) + "\n"


def quest_shop_tabs():
    return arrays("npc/miracle/quest_shop.txt").get("Shops$", [])


def slot_enchanter(rel, npc, title_prefix="Group"):
    """Aulion / Desmond style enchanters: GroupItemIDn + GroupSlot{2,3,4}_n pools."""
    arr = arrays(rel, npc)
    out = []
    n = 1
    while f"GroupItemID{n}" in arr:
        ids = arr[f"GroupItemID{n}"]
        rows = []
        for slot in (2, 3, 4):
            pool = [p for p in arr.get(f"GroupSlot{slot}_{n}", []) if p]
            if pool:
                rows.append((f"Slot {slot}", items_list(pool)))
        names = ", ".join(item_name(i) for i in ids[:3]) + (f" +{len(ids) - 3} more" if len(ids) > 3 else "")
        body = "**Equipment:** " + items_list(ids) + "\n\n" + _table(["Slot", "Possible enchants (equal chance)"], rows)
        out.append(_details(f"{names}", body))
        n += 1
    return "\n".join(out)


def item_enchant(eid):
    """Render one entry of db/re/item_enchant.yml (official-style enchant UI)."""
    for rel in ("db/import/item_enchant.yml", "db/re/item_enchant.yml"):
        data = _enchant_db(rel)
        if eid in data:
            e = data[eid]
            break
    else:
        return f'!!! warning "Enchant #{eid} not found"\n'
    md = ["**Items:** " + ", ".join(_aegis_item(a) for a in (e.get("TargetItems") or {}))]
    reset = e.get("Reset")
    if reset:
        cost = [f"{fmt(reset['Price'])} Zeny"] if reset.get("Price") else []
        cost += [f"{m.get('Amount', 1)}× {_aegis_item(m['Material'])}" for m in reset.get("Materials") or []]
        md.append(f"**Reset:** {reset.get('Chance', 100000) / 1000:g}% success, costs {', '.join(cost) or 'nothing'}")
    order = [o["Slot"] for o in e.get("Order") or []]
    if order:
        md.append("**Slot order:** " + " → ".join(f"slot {s}" for s in order))
    md.append("")
    for slot in e.get("Slots") or []:
        cost = [f"{fmt(slot['Price'])} Zeny"] if slot.get("Price") else []
        cost += [f"{m.get('Amount', 1)}× {_aegis_item(m['Material'])}" for m in slot.get("Materials") or []]
        grades = slot.get("Enchants") or []
        pool = grades[0].get("Items", []) if grades else []
        total = sum(p.get("Chance", 0) for p in pool) or 1
        rows = [(_aegis_item(p["Item"]), f"{p.get('Chance', 0) / total * 100:.1f}%") for p in pool]
        md.append(f"#### Slot {slot['Slot']}\n")
        md.append(f"Cost per try: {', '.join(cost) or 'free'}\n")
        md.append(_table(["Enchant", "Chance"], rows))
        md.append("")
    return "\n".join(md) + "\n"


@functools.lru_cache(None)
def _enchant_db(rel):
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        return {}
    data = yaml.safe_load(_read(rel)) or {}
    return {e["Id"]: e for e in data.get("Body") or []}


def event_schedule():
    """Daily automatic events from Event_Manager's OnClock labels."""
    names = {"Event_Bombring": "Bombring", "Event_Dice": "Dice", "Poring_Catcher": "Poring Catcher",
             "Disguise Event": "Disguise", "Poring_Hunter": "Poring Hunter", "Monster_battle": "Monster Battle"}
    text = npc_block("npc/miracle/event_manager.txt", "Event_Manager")
    sched = {}
    for hh, mm, npc in re.findall(r"OnClock(\d\d)(\d\d):\s*donpcevent\s+\"([^\"]+)::OnStart\"", text):
        sched[f"{hh}:{mm}"] = names.get(npc, npc)
    rows = sorted(sched.items())
    half = (len(rows) + 1) // 2
    left, right = rows[:half], rows[half:]
    table = []
    for i in range(half):
        r = right[i] if i < len(right) else ("", "")
        table.append((f"**{left[i][0]}**", left[i][1], f"**{r[0]}**" if r[0] else "", r[1]))
    return _table(["Time", "Event", "Time", "Event"], table) + "\n"


def costume_drops():
    a = arrays("npc/miracle/mob_drop.txt", "MobExtraDrops")
    rows = [(mob_name(m), item(d)) for m, d in zip(a.get("MobID", []), a.get("DropID", []))]
    rows.sort(key=lambda r: r[0])
    return _table(["Monster", "Costume"], rows) + "\n"


def npc_directory():
    """Custom NPCs (npc/miracle and npc/custom). Names placed in many towns get one row."""
    hidden = {"Box 1", "Box 2", "Box 3", "Box 4", "Back", "Touch Me!", "BR_Announcer"}
    by_name = OrderedDict()
    for n in npcs():
        if not n["file"].startswith(("npc/miracle/", "npc/custom/")):
            continue
        if not n["name"] or n["name"].startswith(".") or n["name"] in hidden:
            continue
        spots = by_name.setdefault(n["name"], [])
        if (n["map"], n["x"], n["y"]) not in [(m["map"], m["x"], m["y"]) for m in spots]:
            spots.append(n)
    rows = []
    for name, spots in by_name.items():
        f = f"<small>{os.path.basename(spots[0]['file'])}</small>"
        if len({m["map"] for m in spots}) > 3:
            rows.append((name, f"{len(spots)} maps", "most towns", f))
            continue
        for m in spots:
            rows.append((name, f"`{m['map']}`", f"`/navi {m['map']} {m['x']}/{m['y']}`", f))
    order = lambda r: (r[1] != "`prontera`", r[1] != "`moc_para01`", r[1], r[0])
    rows.sort(key=order)
    return _table(["NPC", "Map", "Find it", "Script"], rows) + "\n"


def npc_where(name):
    """'`moc_para01` 36,38' for the first NPC with that display name."""
    for n in npcs():
        if n["name"] == name or n["raw"] == name:
            return f"`{n['map']}` {n['x']}, {n['y']}"
    return "*not placed on a map*"


def official_instances():
    """Table of every official instance the server loads, from the instance scripts."""
    rows = []
    for r in official.instances():
        spots = []
        for m, x, y, npc in r["entrances"][:1]:
            spots.append(f"{npc + ', ' if npc else ''}`{m} {x}/{y}`")
        rows.append([
            f"**[{official.title(r['name'])}]({official.page_of(r['name'])}.md)**",
            str(r["level"]) if r["level"] else "—",
            "<br>".join(spots) or "—",
            official.duration(r["time_limit"]).strip(),
            r["cooldown"] or "—",
        ])
    return _table(["Instance", "Level", "Entrance", "Time limit", "Cooldown"], rows)


def _mob_cell(mid):
    return mob(mid)


def _rate(rate):
    pct = int(rate) / 100
    return f"{pct:g}%"


@functools.lru_cache(None)
def _battle_conf():
    import gen_db
    return gen_db.battle_conf()


def _server_rate(iid, rate, m, mvp_reward):
    import gen_db
    from ydb import items as ydb_items
    bt = "mvp" if m["mvp"] else "boss" if m["cls"] == "Boss" else ""
    t = ydb_items().get(iid, {}).get("Type", "Etc")
    return gen_db.drop_rate(_battle_conf(), int(rate), t, bt, mvp_reward=mvp_reward)


def _drops_table(mid):
    m = official.mob_db()[mid]
    rows, seen = [], set()
    for kind, drops in (("MVP reward", m["mvp_drops"]), ("", m["drops"])):
        for aegis, rate in drops:
            if (aegis, rate, kind) in seen:
                continue
            seen.add((aegis, rate, kind))
            iid = item_id(aegis)
            chance = _rate(_server_rate(iid, rate, m, bool(kind))) if iid else _rate(rate)
            rows.append([item(iid) if iid else aegis, chance, kind])
    return _table(["Item", "Chance", ""], rows) if rows else "_No drops._"


def instance_page(key, overview_only=False):
    """Full page body for one instance (and its harder variants)."""
    ttl, recs = official.group(key)
    main = recs[0]
    out = []
    desc = official.description(main["file"])
    if desc and len(desc) > 30:
        out.append(f"_{desc}_\n")
    info = []
    for r in recs:
        label = f" ({official.title(r['name'])})" if len(recs) > 1 else ""
        bits = [f"Level **{r['level']}+**" if r["level"] else "Unlocked by its story quest",
                f"time limit **{official.duration(r['time_limit']).strip()}**",
                f"cooldown **{r['cooldown']}**" if r["cooldown"] else "no cooldown"]
        info.append(f"- **Requirements{label}:** " + ", ".join(bits))
    spots = []
    for m, x, y, npc in main["entrances"][:2]:
        spots.append(f"{('**' + npc + '** at ') if npc else ''}`{m} {x}/{y}` (`/navi {m} {x}/{y}`)")
    if spots:
        info.insert(0, "- **Entrance:** " + " or ".join(spots))
    party = {"IM_CHAR": "Solo", "IM_GUILD": "Guild", "IM_CLAN": "Clan"}.get(main["mode"] or "", "Party (create a party first)")
    info.append(f"- **Who can enter:** {party}")
    if len(recs) > 1:
        info.append("- **Modes:** " + ", ".join(official.title(r["name"]) for r in recs))
    out += ["## Overview", "", *info, ""]
    if overview_only:
        return "\n".join(out)

    d = {"mobs": [], "rewards": OrderedDict(), "shops": []}
    for r in recs:
        dd = official.instance_details(r)
        d["mobs"] += [m for m in dd["mobs"] if m not in d["mobs"]]
        for k, v in dd["rewards"].items():
            d["rewards"].setdefault(k, v)
        d["shops"] += [x for x in dd["shops"] if x not in d["shops"]]
    db = official.mob_db()
    # Script helpers (event dummies, invisible counters) are not monsters players fight.
    d["mobs"] = [m for m in d["mobs"] if not re.match(r"^(Monster \d+|[A-Z0-9_]+|--.*--)$", str(db[m]["name"]))
                 and db[m]["cls"] != "Battlefield" and int(db[m]["hp"] or 0) > 10]
    bosses = [m for m in d["mobs"] if db[m]["mvp"] or db[m]["cls"] == "Boss"]
    normal = [m for m in d["mobs"] if m not in bosses]
    if bosses:
        out += ["## Bosses", "",
                "Drop chances include Miracle's drop rates.", ""]
        bosses.sort(key=lambda m: (not db[m]["mvp"], -int(db[m]["hp"] or 0)))
        for mid in bosses:
            m = db[mid]
            kind = "MVP" if m["mvp"] else "Boss"
            stats = (f"{kind} · Level {m['level']} · {fmt(int(m['hp']))} HP · {m['race']} · "
                     f"{m['element']} · {m['size']}")
            pic_html = pic("mobs", mid, "mob-lg")
            link = f"[Full monster entry]({_root()}db/monsters.md#{mid})"
            out.append(_details(f"{m['name']} #{mid}", pic_html + "\n\n" + stats + " · " + link + "\n\n" + _drops_table(mid),
                                open_=m["mvp"]))
            out.append("")
    if normal:
        out += ["## Monsters", "", _table(["Monster", "Level", "HP", "Race", "Element"],
                                           [[_mob_cell(mid), db[mid]["level"], fmt(int(db[mid]["hp"] or 0)),
                                             db[mid]["race"], db[mid]["element"]] for mid in normal]), ""]
    if d["rewards"]:
        out += ["## Rewards and quest items", "",
                "Items the instance NPCs hand out, including quest items used along the way.", "",
                _table(["Item", "Amount"], [[item(i), a or "—"] for i, a in d["rewards"].items()]), ""]
    trades = _instance_trades(d)
    if trades:
        out += ["## Exchange and crafting", "",
                "NPCs outside the instance that take what you bring back from it.", "", trades, ""]
    if d["shops"]:
        out += ["## Shops", "", "\n".join(f"- {s}" for s in d["shops"]), ""]
    return "\n".join(out)


def _names(ids, limit=8):
    names = [item(i) for i in ids[:limit]]
    more = f" and {len(ids) - limit} more" if len(ids) > limit else ""
    return ", ".join(names) + more


def _instance_trades(d):
    """Table of NPCs that take this instance's materials (etc drops and rewards)."""
    db, items_by_id = official.mob_db(), rodb.items()[0]
    mats = []
    for mid in d["mobs"]:
        for aegis, _ in db[mid]["mvp_drops"] + db[mid]["drops"]:
            iid = item_id(aegis)
            if iid and iid not in mats:
                mats.append(iid)
    mats += [i for i in d["rewards"] if i not in mats]
    users, droppers = official.item_users(), official.item_droppers()
    here = set(d["mobs"])
    # Keep the instance's own materials: etc items that few monsters outside it drop.
    mats = [i for i in mats if items_by_id.get(i, {}).get("type") == "Etc" and 0 < len(users.get(i, [])) <= 6
            and ((i in d["rewards"] and len(droppers.get(i, set()) - here) <= 6) or (droppers.get(i) and not droppers[i] - here
                                       and any(db[m]["mvp"] or db[m]["cls"] == "Boss" for m in droppers[i])))]
    seen, rows = set(), []
    for mat in mats:
        for t in users[mat]:
            key = (t["npc"], t["spot"])
            if key in seen:
                continue
            seen.add(key)
            mine = [i for i in t["takes"] if i in mats]
            if t["kind"] == "barter":
                gives = [g for g, req in t["recipes"] if any(i in mats for i, _ in req)]
            else:
                gives = t["gives"]
            what = _names(gives) if gives else ""
            if t["enchants"]:
                what += ("<br>" if what else "") + "Enchants: " + _names(t["enchants"], 6)
            m, x, y = t["spot"]
            rows.append([f"**{t['npc'] or 'NPC'}**<br>`{m} {x}/{y}`", _names(mine, 4), what or "Upgrades or quest use"])
    return _table(["NPC", "Takes", "Gives"], rows) if rows else ""


def official_npcs(*rels, only=None, limit=3):
    """Where the NPCs of one or more official script files stand: 'Name: map x/y' list."""
    seen = OrderedDict()
    for rel in rels:
        for name, m, x, y in official.visible_npcs(rel):
            if only and name not in only:
                continue
            seen.setdefault(name, []).append(f"`{m} {x}/{y}`")
    lines = []
    for name, spots in seen.items():
        more = f" and {len(spots) - limit} more" if len(spots) > limit else ""
        lines.append(f"- **{name}**: {', '.join(spots[:limit])}{more}")
    return "\n".join(lines)


def official_instance_count():
    return len(official.instances())


# ---------------------------------------------------------------- Endless Tower

def _et_file():
    for r in official.instances():
        if r["name"] == "Endless Tower":
            return r["file"]
    return None


def _nums(text):
    return [int(n) for n in re.findall(r"-?\d+", re.sub(r"//[^\n]*", "", text))]


def endless_tower():
    """Difficulty modes, floors and rewards of the Endless Tower script the server loads."""
    rel = _et_file()
    if not rel:
        return "_Endless Tower is not loaded on this server._"
    t = _read(rel)
    out = []

    # Difficulty modes: the menu gives names and levels, F_Tower_Settings the numbers.
    menu = re.findall(r'"\[ Level (\d+)\+ \] (?:\^\w{6})?([A-Za-z]+)', t)
    cfg = {k: _nums(v) for k, v in re.findall(r"setarray \$@(\w+)_mode_variables\s*,([^;]+);", t)}
    exp = _nums((re.search(r"setarray \$@bonus_exp\[1\]\s*,([^;]+);", t) or [None, ""])[1])
    pts = _nums((re.search(r"setarray \$@instance_points\[1\]\s*,([^;]+);", t) or [None, ""])[1])
    summon = t[t.find("F_Tower_Monster_Summon\t{"):]
    summon = summon[:summon.find("\nfunction\t")]
    keys = ["easy", "veteran", "nightmare", "hell", "torment"]
    broken = set(re.findall(r"\.@(\w+)_mode_variables", summon))  # read from an empty local array
    if menu:
        rows = []
        for i, (lv, name) in enumerate(menu):
            k = keys[i] if i < len(keys) else ""
            v = cfg.get(k, [0] * 7) + [0] * 7
            mult = exp[i] if i < len(exp) else 0
            stats = (f"+{v[0]}%", f"+{v[1]}%", f"{v[2]}%", f"+{v[3]}% / +{v[4]}%", f"+{v[5]}% / +{v[6]}%")
            if k in broken:
                stats = ("not applied",) * 5
            rows.append([f"**{name}**", f"{lv}+", *stats,
                         f"+{mult}× monster exp" if mult else "normal", pts[i] if i < len(pts) else "—"])
        out += ["## Difficulty modes", "",
                "The party leader picks a mode when creating the tower. Every party member must meet its level. "
                "Monsters get the bonuses below on top of their normal stats.", "",
                _table(["Mode", "Level", "Monster HP", "Monster damage", "Damage they take", "DEF / MDEF",
                        "HIT / FLEE", "Bonus exp", "Instance Points"], rows), ""]
        if broken & set(keys):
            out += ['!!! warning "Known issue"',
                    "    " + ", ".join(k.title() for k in keys if k in broken) +
                    " mode currently spawns monsters without its bonuses, so it plays easier than intended.", ""]

    # Floors.
    s = t.find("F_Tower_Monster\t{")
    e = t.find("\nfunction\t", s + 1)
    body = t[s:e] if s >= 0 else ""
    parts = re.split(r"\n\s*case (\d+):", body)
    floors = {}
    for i in range(1, len(parts), 2):
        spawns = re.findall(r'"([^"]+)",\s*(\d+),\s*(\d+),\s*\.@label\$', parts[i + 1])
        if spawns:
            floors[int(parts[i])] = [(int(mid), int(n)) for _, mid, n in spawns]
    db = official.mob_db()

    def is_boss(mid):
        m = db.get(mid)
        return bool(m and (m["mvp"] or m["cls"] == "Boss"))

    def cell(lst, only=None):
        merged = OrderedDict()
        for mid, n in lst:
            if only is None or only(mid):
                merged[mid] = merged.get(mid, 0) + n
        return "<br>".join(f"{mob(mid)} ×{n}" for mid, n in merged.items())

    boss_floors = [(f, l) for f, l in sorted(floors.items()) if any(is_boss(m) for m, _ in l)]
    if boss_floors:
        out += ["## Boss floors", "",
                _table(["Floor", "Boss", "With"], [[f"**{f}F**", cell(l, is_boss), cell(l, lambda m: not is_boss(m)) or "—"]
                                                   for f, l in boss_floors]), ""]
    if floors:
        out += ["## Every floor", "",
                "Kill everything on a floor to open the gate to the next one. Floors 26, 51 and 76 start new maps.", ""]
        top = max(floors)
        for start in range(1, top + 1, 10):
            rows = [[f"{f}F", cell(floors[f])] for f in range(start, min(start + 9, top) + 1) if f in floors]
            if rows:
                out.append(_details(f"Floors {start} to {min(start + 9, top)}", _table(["Floor", "Monsters"], rows)))
                out.append("")

    # Rewards.
    rew = []
    shared = re.search(r'F_PartySharedDrop_Map",\s*[^,]+,\s*(\d+),\s*(\d+),\s*(\d+)', t)
    if shared:
        iid, n, ch = map(int, shared.groups())
        rew.append(f"- **Every monster you kill:** {ch}% chance for each party member to get {n}× {item(iid)} "
                   "(one per player, extra accounts of the same person don't count).")
    ash = re.search(r"getitem (\d+),\s*1;\s*//\s*Dark_Ashes", t)
    if ash:
        rew.append(f"- **Gates on floors 25, 50 and 75:** 1× {item(int(ash.group(1)))} each time you pass.")
    m = re.search(r"\.@roll = rand\(1,\s*(\d+)\);(.*?)getitem (\d+), \.@amount;", t, re.S)
    if m:
        top, block, iid = int(m.group(1)), m.group(2), int(m.group(3))
        limits = [int(x) for x in re.findall(r"\.@roll <= (\d+)", block)] + [top]
        amounts = re.findall(r"\.@amount = rand\((\d+),\s*(\d+)\)", block)
        rows, prev = [], 0
        for lim, (a, b) in zip(limits, amounts):
            rows.append([f"{int(a)} to {int(b)}", f"{(lim - prev) * 100 / top:g}%"])
            prev = lim
        rew += [f"- **Clearing the tower** (talk to the Lost Souls after Nacht Sieger): {item(iid)}, amount rolled like this:", "",
                _table(["Amount", "Chance"], rows), ""]
    if "F_EarnInstancePoints" in t:
        rew.append("- **Instance Points** for the mode you cleared (see the table above). Spend them at the "
                   f"[Instance Point Merchant]({_root()}shops/instance-point-merchant.md).")
    craft = re.search(r"delitem (\d+),1;[^\n]*\n\s*delitem (\d+),1;[^\n]*\n\s*getitem (\d+),1;", t)
    if craft:
        a, b, c = map(int, craft.groups())
        rew.append(f"- **The Lost Souls** combine {item(a)} and {item(b)} (both dropped by Nacht Sieger) into {item(c)}.")
    if rew:
        out += ["## Rewards", "", *rew, ""]
    return "\n".join(out)


def define_env(env):
    global ENV
    ENV = env
    for fn in (item, shops_in, items_table, items_list, shop, barter, quest_shop, quest_shop_tabs, slot_enchanter,
               item_enchant, array_seq, event_schedule, costume_drops, npc_directory, npc_where, arrays, scalar,
               fmt, item_name, mob_name, official_instances, official_instance_count,
               official_npcs, instance_page, mob, endless_tower):
        env.macro(fn)
