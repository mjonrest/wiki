"""Every way to get an item that the NPC and drop tables in gen_db/gen_npcs don't already cover:
Quest Shop rewards, instance rewards, the Cash Shop, map drops, quest drops, achievements, attendance, crafting
and Miracle's scripted kill bonuses.

Used by gen_db.build(); each row is [kind, ...] and db.js turns it into a line under "How to get" on the item page.
"""
import os
import re
from collections import defaultdict

import ydb
from rodb import ROOT


def _read(rel):
    import main
    return main.script_text(rel) if os.path.exists(os.path.join(ROOT, rel)) else ""


def quest_shop(out):
    """["quest", tab name, amount, [[cost item, amount]...], zeny, cash points] from Euphy's Quest Shop."""
    import main
    rel = "npc/miracle/quest_shop.txt"
    if rel not in main.enabled_scripts():
        return
    text = _read(rel)
    tabs = main.arrays(rel).get("Shops$", [])
    for m in re.finditer(r"^\s*Add\(([^)]*)\);", text, re.M):
        try:
            a = [int(x) for x in m.group(1).split(",")]
        except ValueError:
            continue
        tab = tabs[a[0] - 1] if 0 < a[0] <= len(tabs) else f"Tab {a[0]}"
        cost = [[a[i], a[i + 1]] for i in range(5, len(a) - 1, 2)]
        out[a[1]].append(["quest", str(tab).strip('"'), a[2], cost, a[3], a[4]])


def instances(out):
    """["instance", page slug, title] for items the instance NPCs hand out."""
    import official
    for key, title, recs in official.instance_groups():
        seen = set()
        for r in recs:
            for iid in official.instance_details(r)["rewards"]:
                if iid not in seen:
                    seen.add(iid)
                    out[iid].append(["instance", key, title])


def cash_shop(out, by_aegis):
    """["cash", tab, price]"""
    for rel in ydb.files("db/item_cash.yml"):
        for tab in ydb.load(rel).get("Body") or []:
            for it in tab.get("Items") or []:
                iid = by_aegis.get(str(it.get("Item")))
                if iid is not None:
                    row = ["cash", tab.get("Tab"), it.get("Price")]
                    out[iid] = [r for r in out[iid] if not (r[0] == "cash" and r[1] == row[1])] + [row]


def map_drops(out, by_aegis):
    """["mapdrop", map, chance in 1/10000, monster id or null]"""
    for rel in ydb.files("db/map_drops.yml"):
        for e in ydb.load(rel).get("Body") or []:
            for d in e.get("GlobalDrops") or []:
                iid = by_aegis.get(str(d.get("Item")))
                if iid is not None and d.get("Rate"):
                    out[iid].append(["mapdrop", e.get("Map"), d["Rate"], None])
            for sp in e.get("SpecificDrops") or []:
                mid = sp.get("Monster")
                for d in sp.get("Drops") or []:
                    iid = by_aegis.get(str(d.get("Item")))
                    if iid is not None and d.get("Rate"):
                        out[iid].append(["mapdrop", e.get("Map"), d["Rate"], mid])


def quest_drops(out, by_aegis, mob_by_aegis):
    """["questdrop", quest id, title, monster id (0 = any), chance in 1/10000]"""
    for qid, q in ydb.table("db/quest_db.yml").items():
        for d in q.get("Drops") or []:
            iid = by_aegis.get(str(d.get("Item")))
            if iid is None:
                continue
            mob = d.get("Mob", 0)
            mid = mob if isinstance(mob, int) else mob_by_aegis.get(str(mob), 0)
            out[iid].append(["questdrop", qid, q.get("Title", ""), mid, d.get("Rate", 0)])


def achievements(out, by_aegis):
    """["achievement", id, name]"""
    for aid, a in ydb.table("db/achievement_db.yml").items():
        r = a.get("Rewards") or {}
        iid = by_aegis.get(str(r.get("Item")))
        if iid is not None:
            out[iid].append(["achievement", aid, a.get("Name", "")])


def attendance(out, by_aegis):
    """["attendance", day]"""
    for rel in ydb.files("db/attendance.yml"):
        for period in ydb.load(rel).get("Body") or []:
            for r in period.get("Rewards") or []:
                iid = by_aegis.get(str(r.get("Item")))
                if iid is not None:
                    out[iid].append(["attendance", r.get("Day")])


def crafting(out, items):
    """["craft", skill, skill level, [[material, amount]...]] from produce_db.txt (db/re, then db/import)."""
    recipes = {}
    for rel in ("db/re/produce_db.txt", "db/import/produce_db.txt"):
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            continue
        for line in open(path, encoding="utf-8", errors="replace"):
            line = line.split("//")[0].strip()
            p = [x.strip() for x in line.split(",")]
            if len(p) < 5 or not p[0].isdigit() or not p[1].isdigit():
                continue
            recipes[int(p[0])] = p
    for p in recipes.values():
        iid = int(p[1])
        if iid not in items:
            continue
        mats = [[int(p[i]), int(p[i + 1])] for i in range(5, len(p) - 1, 2) if p[i].isdigit() and p[i + 1].isdigit()]
        out[iid].append(["craft", p[3], p[4], mats])


KILL_BONUS_NPCS = ("MobExtraDrops", "MobDropModifier")


def kill_bonus(mobs):
    """Miracle's OnNPCKillEvent extra drops (npc/miracle/mob_drop.txt): [(mob id, item id, chance in 1/10000)]."""
    out = []
    import main
    rel = "npc/miracle/mob_drop.txt"
    if rel not in main.enabled_scripts():
        return out
    for npc in KILL_BONUS_NPCS:
        body = main.npc_block(rel, npc)
        a = main.arrays(rel, npc)
        roll = re.search(r"rand\(\s*1\s*,\s*(\d+)\s*\)\s*;\s*if\s*\(\s*\.@\w+\s*<=\s*(\d+)", body)
        if not roll or not a.get("MobID") or not a.get("DropID"):
            continue
        chance = int(roll.group(2)) * 10000 / int(roll.group(1))
        mob_ids = [int(m) for m in a["MobID"] if str(m).isdigit()]
        drop_ids = [int(d) for d in a["DropID"] if str(d).isdigit()]
        if re.search(r"\.@DropID\[\s*rand\(", body):  # one random item of the list per kill
            each = chance / len(drop_ids)
            pairs = [(m, d, each) for m in mob_ids for d in drop_ids]
        else:  # the item at the same position as the monster
            pairs = [(m, d, chance) for m, d in zip(mob_ids, drop_ids)]
        for m, d, c in dict.fromkeys(pairs):
            if m in mobs:
                out.append((m, d, round(c, 2)))
    return out


def build(items, by_aegis, mobs):
    out = defaultdict(list)
    mob_by_aegis = {m.get("AegisName"): mid for mid, m in mobs.items()}
    for step in (lambda: quest_shop(out), lambda: instances(out), lambda: cash_shop(out, by_aegis),
                 lambda: map_drops(out, by_aegis), lambda: quest_drops(out, by_aegis, mob_by_aegis),
                 lambda: achievements(out, by_aegis), lambda: attendance(out, by_aegis), lambda: crafting(out, items)):
        step()
    return {k: v for k, v in out.items() if k in items}
