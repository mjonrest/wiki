"""Enchant part of the Database: the enchant UI systems (db/item_enchant.yml) and Laphine synthesis and upgrade.

Used by gen_db.build(); item pages link to the systems an item takes part in, NPC pages to the systems they open.
"""
import re
from collections import defaultdict

import ydb


def _mats(lst, by_aegis):
    return [[by_aegis[m["Material"]], m.get("Amount", 1)] for m in lst or [] if m.get("Material") in by_aegis]


def _label(option, script):
    """'VAR_ATTPOWER' with script 'bonus bBaseAtk,...' -> 'Base Atk'."""
    m = re.search(r"bonus\d?\s+b(\w+)", script or "")
    if not m:
        return option.replace("VAR_", "").replace("_", " ").title()
    name = re.sub(r"(?i)rate$", "%", m.group(1))
    name = re.sub(r"(?<=[a-z])(?=[A-Z%])|(?<=[A-Z])(?=[A-Z][a-z])|(?<=[A-Z])(?=%)", " ", name)
    return name.replace("Castrate", "Cast %").replace("Aspd", "ASPD")


def random_option_groups():
    """{group name: [[ [label, min, max, chance], ... ] per slot], with labels from item_randomopt_db."""
    names = {}
    for e in ydb.table("db/item_randomopt_db.yml", "Option").values():
        names[e["Option"]] = _label(e["Option"], e.get("Script"))
    out = {}
    for name, g in ydb.table("db/item_randomopt_group.yml", "Group").items():
        slots = []
        for s in g.get("Slots") or []:
            slots.append([[names.get(o.get("Option"), str(o.get("Option"))), o.get("MinValue", 0), o.get("MaxValue", 0),
                           o.get("Chance", 0)] for o in s.get("Options") or []])
        out[str(name)] = slots
    return out


def build(by_aegis, groups, npc_enchants, from_npc):
    """(list rows, {key: detail}, {item id: {role: [keys]}}), limited to what players can reach through an NPC:
    enchant systems an NPC opens, and Laphine recipes whose trigger item an NPC sells or gives.

    groups: {GROUP NAME: [[item id, chance, amount], ...]} from the item group db.
    npc_enchants: {enchant system id: [npc ids]}.
    from_npc: ids of items an NPC sells, trades or gives.
    """
    rows, detail = [], {}
    roles = defaultdict(lambda: defaultdict(list))

    def role(iid, kind, key):
        if key not in roles[iid][kind]:
            roles[iid][kind].append(key)

    for eid, e in sorted(ydb.table("db/item_enchant.yml").items()):
        if eid not in npc_enchants:
            continue
        key = f"E{eid}"
        targets = [by_aegis[a] for a, on in (e.get("TargetItems") or {}).items() if on and a in by_aegis]
        slots = []
        for s in e.get("Slots") or []:
            grades = [[g.get("Enchantgrade", 0), [[by_aegis[i["Item"]], i.get("Chance", 0)] for i in g.get("Items") or []
                                                 if i.get("Item") in by_aegis]] for g in s.get("Enchants") or []]
            perfect = [[by_aegis[p["Item"]], p.get("Price", 0), _mats(p.get("Materials"), by_aegis)]
                       for p in s.get("PerfectEnchants") or [] if p.get("Item") in by_aegis]
            ups = [[by_aegis[u["Enchant"]], by_aegis[u["Upgrade"]], u.get("Price", 0), _mats(u.get("Materials"), by_aegis)]
                   for u in s.get("Upgrades") or [] if u.get("Enchant") in by_aegis and u.get("Upgrade") in by_aegis]
            slots.append({"slot": s.get("Slot"), "price": s.get("Price", 0), "mats": _mats(s.get("Materials"), by_aegis),
                          "chance": s.get("Chance", 100000),
                          "bonus": [[b.get("Enchantgrade"), b.get("Chance")] for b in s.get("EnchantgradeBonus") or []],
                          "grades": grades, "perfect": perfect, "upgrades": ups})
            for _, lst in grades:
                for iid, _c in lst:
                    role(iid, "enchantResult", key)
            for p in perfect:
                role(p[0], "enchantResult", key)
            for u in ups:
                role(u[1], "enchantResult", key)
        reset = e.get("Reset") or {}
        d = {"targets": targets, "minRefine": e.get("MinimumRefine", 0), "minGrade": e.get("MinimumEnchantgrade", 0),
             "order": [o.get("Slot") for o in e.get("Order") or []], "slots": slots,
             "npcs": npc_enchants.get(eid, [])}
        if reset:
            d["reset"] = [reset.get("Chance", 0), reset.get("Price", 0), _mats(reset.get("Materials"), by_aegis)]
        detail[key] = d
        for t in targets:
            role(t, "enchantTarget", key)
        rows.append([key, "Enchant", targets[0] if targets else 0, len(targets), d["minRefine"], len(slots)])

    opt_groups = random_option_groups()
    for name, e in ydb.table("db/laphine_synthesis.yml", "Item").items():
        iid = by_aegis.get(name)
        if iid not in from_npc:
            continue
        key = f"S{iid}"
        reqs = [[by_aegis[r["Item"]], r.get("Amount", 1)] for r in e.get("Requirements") or [] if r.get("Item") in by_aegis]
        reward = groups.get(str(e.get("RewardGroup", "")).upper(), [])
        detail[key] = {"item": iid, "count": e.get("RequiredRequirementsCount", 1), "minRefine": e.get("MinimumRefine", 0),
                       "maxRefine": e.get("MaximumRefine"), "reqs": reqs, "group": e.get("RewardGroup"),
                       "rewards": reward[:400]}
        role(iid, "laphineItem", key)
        for r, _a in reqs:
            role(r, "laphineReq", key)
        for r in reward:
            role(r[0], "laphineReward", key)
        rows.append([key, "Laphine synthesis", iid, len(reqs), e.get("MinimumRefine", 0), len(reward)])

    for name, e in ydb.table("db/laphine_upgrade.yml", "Item").items():
        iid = by_aegis.get(name)
        if iid not in from_npc:
            continue
        key = f"U{iid}"
        targets = [by_aegis[t["Item"]] for t in e.get("TargetItems") or [] if t.get("Item") in by_aegis]
        d = {"item": iid, "targets": targets, "group": e.get("RandomOptionGroup"),
             "options": opt_groups.get(str(e.get("RandomOptionGroup"))) or [],
             "minRefine": e.get("MinimumRefine", 0), "maxRefine": e.get("MaximumRefine"),
             "resultRefine": e.get("ResultRefine"), "resultMin": e.get("ResultRefineMinimum"),
             "resultMax": e.get("ResultRefineMaximum"), "needOptions": e.get("RequiredRandomOptions", 0),
             "cards": bool(e.get("CardsAllowed"))}
        detail[key] = {k: v for k, v in d.items() if v not in (None, [], 0, False) or k in ("item", "targets")}
        role(iid, "laphineItem", key)
        for t in targets:
            role(t, "laphineTarget", key)
        rows.append([key, "Laphine upgrade", iid, len(targets), e.get("MinimumRefine", 0), 0])
    return rows, detail, {iid: {k: v[:60] for k, v in r.items()} for iid, r in roles.items()}
