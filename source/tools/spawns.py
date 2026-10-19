"""Where monsters come from: permanent spawns with their respawn times, and the instances and scripts that summon them."""
import functools
import os
import re
from collections import defaultdict

from rodb import ROOT

# map{,x,y{,xs,ys}}<TAB>monster|boss_monster<TAB>name<TAB>mob,amount{,delay1{,delay2{,event...}}}
SPAWN = re.compile(r"^([\w@.-]+)(?:,\d+){0,4}\t(?:boss_)?monster\t[^\t]+\t\s*(\w+)\s*,\s*(\d+)(?:\s*,\s*(\d+))?(?:\s*,\s*(\d+))?")
SUMMON = re.compile(r"\b(monster|areamonster|bg_monster)\b\s*\(?\s*([^;]+);")
MOB_ARG = {"monster": 4, "areamonster": 6, "bg_monster": 5}
MAP_ARG = {"monster": 0, "areamonster": 0, "bg_monster": 1}

# Miracle scripts that have their own wiki page.
PAGES = {
    "npc/miracle/hell_raid.txt": ("Hell Raid", "content/hell-raid.md"),
    "npc/miracle/wb_new(non-regen).txt": ("World Boss", "content/world-boss.md"),
    "npc/miracle/abyssal_bb.txt": ("Abyssal Bloody Branch", "special/abyssal-bloody-branch.md"),
    "npc/miracle/mining.txt": ("Mining Zone", "content/mining.md"),
}
# Files whose monsters are covered by the Illusion & Summoned Bosses page.
BOSS_PAGE = ("Illusion & Summoned Bosses", "special/boss-spawns.md")


def _files():
    import official
    import main
    files = official.official_scripts() + [f for f in main.enabled_scripts() if os.path.exists(os.path.join(ROOT, f))]
    return list(dict.fromkeys(files))


def _mob(tok):
    import official
    return official._mob_ref(tok)


@functools.lru_cache(None)
def permanent():
    """{mob id: [[map, amount, delay1 ms, delay2 ms], ...]} from every permanent spawn line the server loads.
    The respawn time is delay1 plus a random 0 to delay2 (mob.cpp mob_setdelayspawn)."""
    import official
    out = defaultdict(lambda: defaultdict(int))
    for rel in _files():
        for line in official._read(rel).splitlines():
            m = SPAWN.match(line)
            if not m:
                continue
            mid = _mob(m.group(2))
            if not mid:
                continue
            d1, d2 = int(m.group(4) or 0), int(m.group(5) or 0)
            out[mid][(m.group(1), d1, d2)] += int(m.group(3))
    return {k: sorted(([mp, n, d1, d2] for (mp, d1, d2), n in v.items()), key=lambda x: (-x[1], x[0]))
            for k, v in out.items()}


@functools.lru_cache(None)
def summoned():
    """{mob id: [[label, page or None], ...]}: instances whose scripts spawn it, and other scripts that summon it
    (by page when one covers the script, else by the map the script names)."""
    import official
    out = defaultdict(list)

    def add(mid, row):
        if row not in out[mid]:
            out[mid].append(row)

    for key, title, recs in official.instance_groups():
        for rec in recs:
            for mid in official.instance_details(rec)["mobs"]:
                add(mid, [title, f"official/instances/{key}.md"])
    covered = {f for _, _, recs in official.instance_groups() for r in recs for f in official.instance_files(r)}
    for rel in _files():
        if rel in covered and rel not in PAGES:
            continue
        blks = official.blocks(rel)
        if not any(SUMMON.search(b) for _, b in blks):
            continue
        res = official._Resolver("\n".join(b for _, b in blks))
        page = PAGES.get(rel)
        for hdr, body in blks:
            for cmd, call in SUMMON.findall(body):
                args = official._split_args(call)
                pos = MOB_ARG[cmd]
                if len(args) <= pos:
                    continue
                mp = args[MAP_ARG[cmd]].strip().strip('"')
                if not re.fullmatch(r"[\w@.-]+", mp) or mp == "this":
                    mp = hdr.group("map") if hdr.group("map") else ""
                for v in res.values(args[pos], body):
                    mid = _mob(v)
                    if not mid:
                        continue
                    if page:
                        add(mid, list(page))
                    elif "@" in mp:
                        continue  # an instance map we could not tie to an instance page
                    elif mp:
                        add(mid, [mp, None])
    # Summon items: Dead Branch, Bloody Branch, Poring Box and the like (db/mob_summon.yml groups).
    import ydb
    groups = ydb.table("db/mob_summon.yml", "Group")
    for iid, it in sorted(ydb.items().items()):
        for g in dict.fromkeys(re.findall(r"\bMOBG_(\w+)", str(it.get("Script") or ""))):
            e = next((v for k, v in groups.items() if str(k).upper() == g.upper()), None)
            if not e:
                continue
            for aegis in [x.get("Mob") for x in e.get("Summon") or []] + [e.get("Default")]:
                mid = _mob(str(aegis or ""))
                if mid:
                    add(mid, ["@item", iid])
    page = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", BOSS_PAGE[1])
    if os.path.exists(page):
        with open(page, encoding="utf-8") as f:
            for mid in re.findall(r"\bmob\((\d+)\)", f.read()):
                add(int(mid), list(BOSS_PAGE))
    return dict(out)


def respawn_text(d1, d2):
    """'2 h ~ 2 h 10 min' style text for a spawn line's delays."""
    if d1 < 60000 and d2 < 60000:
        return "Instant"

    def t(ms):
        m = round(ms / 60000)
        h, m = divmod(m, 60)
        return " ".join(p for p in (f"{h} h" if h else "", f"{m} min" if m else "") if p) or "0 min"
    return t(d1) if not d2 else f"{t(d1)} ~ {t(d1 + d2)}"
