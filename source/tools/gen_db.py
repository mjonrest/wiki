"""Builds the JSON behind the Database pages (items, monsters, skills, jobs).

Run by hooks.py after every build; the files land in <site>/db/data/. The browser loads a small index for the
search list and fetches one detail chunk when a row is opened, so the 30,000+ items cost little to browse.

    python3 tools/gen_db.py OUT_DIR   # same thing by hand
"""
import json
import os
import re
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import ydb  # noqa: E402
from rodb import ROOT  # noqa: E402

CHUNK = 1000  # detail files hold the ids id//CHUNK*CHUNK .. +CHUNK-1


# ---------------------------------------------------------------- server settings

def battle_conf():
    """conf/battle/*.conf values (conf/import is not committed; the live server may override these)."""
    out = {}
    d = os.path.join(ROOT, "conf", "battle")
    for name in sorted(os.listdir(d)) if os.path.isdir(d) else []:
        with open(os.path.join(d, name), encoding="utf-8", errors="replace") as f:
            for line in f:
                m = re.match(r"^\s*(\w+)\s*:\s*(\S+)", line)
                if m:
                    out[m.group(1)] = m.group(2)
    return out


def _int(conf, key, default):
    try:
        return int(conf.get(key, default))
    except ValueError:
        return {"yes": 1, "no": 0}.get(conf.get(key), default)


def drop_rate(conf, base, item_type, bosstype, treasure=False, mvp_reward=False):
    """Effective drop chance in 1/10000, following mob.cpp (linear mode)."""
    if mvp_reward:
        key, cap = "item_rate_mvp", "item_drop_mvp"
    elif treasure:
        key, cap = "item_rate_treasure", "item_drop_treasure"
    else:
        kind = {"Healing": "heal", "Usable": "use", "Cash": "use", "Weapon": "equip", "Armor": "equip",
                "PetArmor": "equip", "Card": "card"}.get(item_type, "common")
        key = f"item_rate_{kind}" + {"mvp": "_mvp", "boss": "_boss"}.get(bosstype, "")
        cap = f"item_drop_{kind}"
    adjust = _int(conf, key, 100)
    if not mvp_reward and _int(conf, "drop_rateincrease", 0) and base < 5000:
        base += 1
    if _int(conf, "item_logarithmic_drops", 0):
        import math
        if adjust > 0 and adjust != 100 and base > 0:
            rate = base * pow(5.0 - math.log10(base), math.log(adjust / 100.0) / math.log(5.0)) + 0.5
        else:
            rate = base * adjust / 100
    else:
        rate = base * adjust / 100
    return int(max(_int(conf, cap + "_min", 1), min(_int(conf, cap + "_max", 10000), rate)))


# ---------------------------------------------------------------- helpers

def _flags(d):
    """{'Knight': True, 'Mage': False} -> ['Knight']"""
    return [k for k, v in (d or {}).items() if v] if isinstance(d, dict) else []


def _nice(s):
    return str(s).replace("_", " ")


def _bosstype(mob):
    if (mob.get("Modes") or {}).get("Mvp") or mob.get("MvpExp"):
        return "mvp"
    return "boss" if mob.get("Class") == "Boss" else ""


def _mob_name(mob):
    return mob.get("JapaneseName") if not mob.get("Name") else mob["Name"]


def _spawns():
    """{mob id: [[map, count], ...]} from permanent spawns in every loaded script."""
    import official
    import main
    files = official.official_scripts() + [f for f in main.enabled_scripts() if os.path.exists(os.path.join(ROOT, f))]
    spawn = re.compile(r"^([\w@-]+),\d+,\d+(?:,\d+,\d+)?\t(?:boss_)?monster\t[^\t]+\t(\d+),(\d+)")
    out = defaultdict(lambda: defaultdict(int))
    for rel in dict.fromkeys(files):
        for line in official._read(rel).splitlines():
            m = spawn.match(line)
            if m:
                out[int(m.group(2))][m.group(1)] += int(m.group(3))
    return {k: sorted(([m, n] for m, n in v.items()), key=lambda x: -x[1]) for k, v in out.items()}


def _shops(item_by_aegis):
    """{item id: [[shop, map, x, y, price, currency], ...]} for NPC shops and barters."""
    import official
    import main
    out = defaultdict(list)
    files = list(dict.fromkeys(official.official_scripts() + main.enabled_scripts()))
    for rel in files:
        if not os.path.exists(os.path.join(ROOT, rel)):
            continue
        for line in main.script_text(rel).splitlines():
            m = main.NPC_HEADER.match(line) or main.FLOAT_SHOP.match(line)
            if not m or m.group("type") not in ("shop", "cashshop", "itemshop", "pointshop", "marketshop"):
                continue
            parts = [p.strip() for p in m.group("rest").rstrip(";").split(",") if p.strip()][1:]
            t = m.group("type")
            if t == "itemshop":
                cur = "item:" + parts.pop(0).split(":")[0]
            elif t == "pointshop":
                v = parts.pop(0).split(":")[0]
                cur = main.CURRENCIES.get(v, v)
            elif t == "cashshop":
                cur = "Cash Points"
            else:
                cur = "Zeny"
            where = [m.group("map"), int(m.group("x")), int(m.group("y"))] if "map" in m.groupdict() else ["", 0, 0]
            for p in parts:
                iid, _, price = p.partition(":")
                if iid.strip().isdigit():
                    price = price.split(":")[0].strip()
                    out[int(iid)].append([main.display_name(m.group("name")), *where,
                                          int(price) if price.lstrip("-").isdigit() else -1, cur])
    for name, shop in main.barters().items():
        for entry in shop.get("Items") or []:
            iid = item_by_aegis.get(entry.get("Item"))
            if iid is None:
                continue
            cost = [[item_by_aegis.get(r.get("Item")), r.get("Amount", 1)] for r in entry.get("RequiredItems") or []]
            if entry.get("Zeny"):
                cost.append(["zeny", entry["Zeny"]])
            out[iid].append([_nice(name), shop.get("Map", ""), shop.get("X", 0), shop.get("Y", 0), 0,
                             {"barter": [c for c in cost if c[0] is not None]}])
    return out


def _boxes(items, item_by_aegis):
    """({item id: [[box id, chance %|null], ...]}, {box id: [[item id, chance|null, amount], ...]})."""
    groups = ydb.table("db/item_group_db.yml", "Group")
    contents = {}
    for gname, g in groups.items():
        rows = []
        for sub in g.get("SubGroups") or []:
            lst = [e for e in sub.get("List") or [] if item_by_aegis.get(e.get("Item")) is not None]
            total = sum(int(e.get("Rate") or 0) for e in lst)
            for e in lst:
                rate = int(e.get("Rate") or 0)
                chance = None if sub.get("SubGroup") == 0 or not total else round(rate * 100 / total, 2)
                rows.append([item_by_aegis[e["Item"]], chance, e.get("Amount", 1)])
        contents[str(gname).upper()] = rows
    in_box, box_has = defaultdict(list), {}
    for iid, it in items.items():
        names = re.findall(r"\bIG_(\w+)", str(it.get("Script") or ""))
        rows = [r for n in dict.fromkeys(names) for r in contents.get(n.upper(), [])]
        if not rows:
            continue
        box_has[iid] = rows[:400]
        for r in rows:
            in_box[r[0]].append([iid, r[1]])
    return in_box, box_has


# ---------------------------------------------------------------- build

def build(out, dir_urls=True):
    conf = battle_conf()
    items, mobs, skills = ydb.items(), ydb.mobs(), ydb.skills()
    by_aegis = {it.get("AegisName"): iid for iid, it in items.items() if it.get("AegisName")}
    skill_by_name = {s.get("Name"): sid for sid, s in skills.items()}
    spawns = _spawns()

    # Monsters, and the drop side of items.
    dropped_by = defaultdict(list)
    mob_index, mob_detail = [], defaultdict(dict)
    for mid, mob in sorted(mobs.items()):
        name = _mob_name(mob) or mob.get("AegisName")
        bt = _bosstype(mob)
        treasure = bool((mob.get("RaceGroups") or {}).get("Treasure"))
        drops = []
        for kind, key in (("mvp", "MvpDrops"), ("", "Drops")):
            for d in mob.get(key) or []:
                iid = by_aegis.get(d.get("Item"))
                if iid is None or not d.get("Rate"):
                    continue
                it = items[iid]
                rate = drop_rate(conf, int(d["Rate"]), it.get("Type", "Etc"), bt, treasure, kind == "mvp")
                drops.append([iid, rate, kind, bool(d.get("StealProtected"))])
                dropped_by[iid].append([mid, rate, kind])
        mob_index.append([mid, name, mob.get("Level", 1), mob.get("Hp", 1), mob.get("Race", "Formless"),
                          f"{mob.get('Element', 'Neutral')} {mob.get('ElementLevel', 1)}", mob.get("Size", "Small"),
                          bt, 1 if mid in spawns else 0])
        mob_detail[mid // CHUNK][mid] = {
            "aegis": mob.get("AegisName"),
            "stats": {k: mob.get(k, 0) for k in ("Level", "Hp", "Sp", "BaseExp", "JobExp", "MvpExp", "Attack",
                                                 "Attack2", "Defense", "MagicDefense", "Resistance",
                                                 "MagicResistance", "Str", "Agi", "Vit", "Int", "Dex", "Luk",
                                                 "AttackRange", "SkillRange", "ChaseRange", "WalkSpeed",
                                                 "AttackDelay", "AttackMotion", "DamageMotion")},
            "class": mob.get("Class", "Normal"),
            "racegroups": _flags(mob.get("RaceGroups")),
            "modes": _flags(mob.get("Modes")),
            "drops": drops,
            "spawns": spawns.get(mid, []),
        }

    # Items.
    shops = _shops(by_aegis)
    for iid, rows in shops.items():
        for r in rows:
            if r[4] == -1 and iid in items:  # -1 in a shop line means the item's Buy price
                r[4] = items[iid].get("Buy") or (items[iid].get("Sell") or 0) * 2
    in_box, box_has = _boxes(items, by_aegis)
    item_index, item_detail = [], defaultdict(dict)
    for iid, it in sorted(items.items()):
        t = it.get("Type", "Etc")
        item_index.append([iid, it.get("Name") or it.get("AegisName"), t, it.get("SubType", ""), it.get("Slots", 0)])
        d = {k: it[k] for k in ("AegisName", "SubType", "Buy", "Sell", "Weight", "Attack", "MagicAttack", "Defense",
                                "Range", "Slots", "Gender", "WeaponLevel", "ArmorLevel", "EquipLevelMin",
                                "EquipLevelMax", "Refineable", "Gradable", "View", "Script", "EquipScript",
                                "UnEquipScript") if it.get(k) not in (None, "", 0, False)}
        for k in ("Jobs", "Classes", "Locations", "Trade", "Flags"):
            if _flags(it.get(k)):
                d[k] = _flags(it.get(k))
        for k, v in (("drops", sorted(dropped_by.get(iid, []), key=lambda x: -x[1])[:80]),
                     ("shops", shops.get(iid, [])[:40]), ("boxes", in_box.get(iid, [])[:60]),
                     ("contains", box_has.get(iid))):
            if v:
                d[k] = v
        item_detail[iid // CHUNK][iid] = d

    # Skills and jobs.
    tree = ydb.skill_tree()
    learned_by = defaultdict(list)
    for job, entry in tree.items():
        for s in entry.get("Tree") or []:
            learned_by[s.get("Name")].append(job)
    skill_out = []
    for sid, s in sorted(skills.items()):
        req = s.get("Requires") or {}
        row = {"id": sid, "aegis": s.get("Name"), "name": s.get("Description") or s.get("Name"),
               "max": s.get("MaxLevel", 1), "type": s.get("Type", "None"), "target": s.get("TargetType", "Passive"),
               "jobs": learned_by.get(s.get("Name"), [])}
        for k in ("Range", "Hit", "HitCount", "Element", "CastTime", "AfterCastActDelay", "AfterCastWalkDelay",
                  "Cooldown", "FixedCastTime", "Duration1", "Duration2", "SplashArea"):
            if s.get(k) not in (None, 0, ""):
                row[k] = s[k]
        for k in ("SpCost", "HpCost", "ApCost", "ZenyCost"):
            if req.get(k) not in (None, 0, ""):
                row[k] = req[k]
        if req.get("ItemCost"):
            row["ItemCost"] = [[by_aegis.get(c.get("Item")), c.get("Amount", 1), c.get("Level")]
                               for c in req["ItemCost"] if by_aegis.get(c.get("Item"))]
        if _flags(req.get("Weapon")):
            row["Weapon"] = _flags(req.get("Weapon"))
        if req.get("State"):
            row["State"] = req["State"]
        skill_out.append(row)

    stats = defaultdict(dict)
    for e in ydb.job_stats():
        for job in _flags(e.get("Jobs")):
            stats[job].update({k: v for k, v in e.items() if k != "Jobs"})
    jobs = []
    for job, entry in tree.items():
        st = stats.get(job, {})
        bonus = defaultdict(int)
        for b in st.get("BonusStats") or []:
            for k, v in b.items():
                if k != "Level":
                    bonus[k] += v
        hp, sp = st.get("BaseHp") or [], st.get("BaseSp") or []
        jobs.append({
            "job": job, "inherit": _flags(entry.get("Inherit")),
            "maxBase": st.get("MaxBaseLevel"), "maxJob": st.get("MaxJobLevel"), "weight": st.get("MaxWeight"),
            "hp": hp[-1].get("Hp") if hp else None, "sp": sp[-1].get("Sp") if sp else None,
            "bonus": dict(bonus), "aspd": st.get("BaseASPD"),
            "tree": [[skill_by_name.get(s.get("Name")), s.get("Name"), s.get("MaxLevel", 1),
                      [[r.get("Name"), r.get("Level", 1)] for r in s.get("Requires") or []]]
                     for s in entry.get("Tree") or []],
        })

    # Write.
    os.makedirs(os.path.join(out, "items"), exist_ok=True)
    os.makedirs(os.path.join(out, "mobs"), exist_ok=True)

    def dump(rel, data):
        with open(os.path.join(out, rel), "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, separators=(",", ":"))

    dump("items.json", item_index)
    dump("mobs.json", mob_index)
    dump("skills.json", skill_out)
    dump("jobs.json", jobs)
    for k, v in item_detail.items():
        dump(f"items/{k}.json", v)
    for k, v in mob_detail.items():
        dump(f"mobs/{k}.json", v)
    dump("meta.json", {"chunk": CHUNK, "dirUrls": dir_urls, "rates": {k: conf.get(k) for k in conf if k.startswith("item_rate_")}})
    return len(item_index), len(mob_index), len(skill_out), len(jobs)


if __name__ == "__main__":
    print(build(sys.argv[1] if len(sys.argv) > 1 else "site/db/data"))
