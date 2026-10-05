"""Shared helpers: load item/mob names from the server's YAML databases."""
import os, re, functools

# The Miracle-MMO server checkout the tables are read from: $MIRACLE_SERVER, or the folder next to this repo.
ROOT = os.path.abspath(os.environ.get("MIRACLE_SERVER")
                       or os.path.join(os.path.dirname(__file__), "..", "..", "..", "Miracle-MMO"))

# Load order matters: later files override earlier ones (same as the server's import folder).
ITEM_DBS = [
    "db/re/item_db_usable.yml", "db/re/item_db_equip.yml", "db/re/item_db_etc.yml",
    "db/re/item_db_rune_cards.yml", "db/re/item_db_rune_tablet.yml",
    "db/import/item_db.yml", "db/import/item_db_other.yml", "db/import/item_db_costume_legacy.yml",
    "db/import/item_db_elite.yml", "db/import/item_db_newjob.yml", "db/import/item_db_ex.yml",
]
ENTRY = re.compile(r"^  - Id: (\d+)\s*\n((?:    .*\n|\s*\n)*)", re.M)
FIELD = re.compile(r"^    (AegisName|Name|Type|Slots|Locations|Buy): ?(.*)$", re.M)


@functools.lru_cache(None)
def items():
    """Returns ({id: {name, aegis, type, slots}}, {aegis: id})."""
    by_id, by_aegis = {}, {}
    for rel in ITEM_DBS:
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            continue
        text = open(path, encoding="utf-8", errors="replace").read().replace("\ufffd", "")
        for m in ENTRY.finditer(text):
            iid = int(m.group(1))
            info = by_id.get(iid, {}).copy()
            for k, v in FIELD.findall(m.group(2)):
                info[k.lower()] = v.strip().strip('"')
            by_id[iid] = info
            if "aegisname" in info:
                by_aegis[info["aegisname"]] = iid
    return by_id, by_aegis


def item_name(iid):
    info = items()[0].get(int(iid))
    if not info:
        return f"Unknown item #{iid}"
    name = info.get("name", info.get("aegisname", str(iid)))
    slots = info.get("slots")
    if slots and slots != "0" and info.get("type") in ("Weapon", "Armor", "Shadowgear"):
        name += f" [{slots}]"
    return name


def item_id(aegis):
    return items()[1].get(aegis)


def item_cell(iid):
    """Markdown cell: name plus a small id, linked to divine-pride for lookups."""
    iid = int(iid)
    return f"{item_name(iid)} <small>`{iid}`</small>"


MOB_DBS = ["db/re/mob_db.yml", "db/import/mob_db.yml", "db/import/new_mob.yml", "db/import/ep20_mob.yml"]
MOB_ENTRY = re.compile(r"^  - Id: (\d+)\s*\n((?:    .*\n|\s*\n)*)", re.M)
MOB_FIELD = re.compile(r"^    (AegisName|Name|Level): ?(.*)$", re.M)


@functools.lru_cache(None)
def mobs():
    by_id = {}
    for rel in MOB_DBS:
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            continue
        text = open(path, encoding="utf-8", errors="replace").read().replace("\ufffd", "")
        for m in MOB_ENTRY.finditer(text):
            info = by_id.get(int(m.group(1)), {}).copy()
            for k, v in MOB_FIELD.findall(m.group(2)):
                info[k.lower()] = v.strip().strip('"')
            by_id[int(m.group(1))] = info
    return by_id


def mob_name(mid):
    info = mobs().get(int(mid))
    return info.get("name", f"Monster #{mid}") if info else f"Monster #{mid}"
