"""Builds the data behind the Combat Power simulator (docs/special/cp-simulator.md, assets/cp-sim.js).

Combat Power (CP) is the game's `@cp` number. Its scoring lives in the game repository, in tools/combat-power
(cp.py, weights.py, enchant.py), so the simulator, the owner's shop page and the in-game command agree. This file
runs those tools over every piece of equipment, card, enchant, random option and set bonus, and writes what the
browser needs to add them up for any job, refine and grade:

- every item script is run for each refine (0-20), grade and job it depends on; the stat totals are stored once
  and shared (most scripts give the same totals at many refines);
- skill bonuses stay per skill, so the browser can apply the per-skill curve and caps after adding everything up,
  just like `@cp` does on the server.

Running the scripts takes a while, so the result is cached in <site>/cp/data.json together with a checksum of
everything it was made from; when nothing changed the previous file (in the repository root) is reused.

    MIRACLE_SERVER=/path/to/Miracle-MMO python3 tools/gen_cp.py OUT_DIR   # same thing by hand
"""
import hashlib
import json
import math
import os
import re
import runpy
import shutil
import sys
import tempfile
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rodb import ROOT  # noqa: E402

VERSION = 1
TOOLS = os.path.join(ROOT, "tools", "combat-power")
HERE = os.path.dirname(os.path.abspath(__file__))
SITE_ROOT = os.path.dirname(os.path.dirname(HERE))  # the repository root holds the last published site
REFINES = range(21)
GRADES = range(5)

# Which part of the character a script reads decides what it has to be run for.
DEP_REFINE = re.compile(r"getrefine|getequiprefinerycnt")
DEP_GRADE = re.compile(r"getenchantgrade|getequipenchantgrade")
DEP_JOB = re.compile(r"\bClass\b|BaseJob|BaseClass|eaclass|getskilllv|readparam|autobonus3|bAutoSpellOnSkill|\bUpper\b")
EQI = re.compile(r"getequip(?:refinerycnt|enchantgrade)\s*\(\s*(EQI_\w+)")

# Equipment slots as the simulator shows them (bit, Locations names that use it).
SLOTS = [
    ("Head_Top", 1), ("Head_Mid", 2), ("Head_Low", 4), ("Armor", 8), ("Right_Hand", 16), ("Left_Hand", 32),
    ("Garment", 64), ("Shoes", 128), ("Right_Accessory", 256), ("Left_Accessory", 512),
    ("Costume_Head_Top", 1024), ("Costume_Head_Mid", 2048), ("Costume_Head_Low", 4096), ("Costume_Garment", 8192),
    ("Shadow_Armor", 16384), ("Shadow_Weapon", 32768), ("Shadow_Shield", 65536), ("Shadow_Shoes", 131072),
    ("Shadow_Right_Accessory", 262144), ("Shadow_Left_Accessory", 524288),
]
LOC = dict(SLOTS)
LOC.update({"Both_Hand": 16 | 32, "Both_Accessory": 256 | 512, "Costume_Head": 1024 | 2048 | 4096})
EQI_SLOT = {"EQI_HEAD_TOP": 1, "EQI_HEAD_MID": 2, "EQI_HEAD_LOW": 4, "EQI_ARMOR": 8, "EQI_HAND_R": 16,
            "EQI_HAND_L": 32, "EQI_GARMENT": 64, "EQI_SHOES": 128, "EQI_ACC_R": 256, "EQI_ACC_L": 512,
            "EQI_SHADOW_ARMOR": 16384, "EQI_SHADOW_WEAPON": 32768, "EQI_SHADOW_SHIELD": 65536,
            "EQI_SHADOW_SHOES": 131072, "EQI_SHADOW_ACC_R": 262144, "EQI_SHADOW_ACC_L": 524288}
# Costume enchant stones are cards without a location; their name says where they go.
STONE = [(re.compile(r"\((?:Upper|Top)\)|Upper\b"), 1024), (re.compile(r"\((?:Middle|Mid)\)|Middle\b"), 2048),
         (re.compile(r"\((?:Lower|Low)\)|Lower\b"), 4096), (re.compile(r"Garment|Robe"), 8192)]


def _inputs_checksum():
    """Checksum of every file the data is made from, so an unchanged game reuses the last result."""
    h = hashlib.sha1(str(VERSION).encode())
    paths = [os.path.join(HERE, "gen_cp.py")]
    for folder in ("db", "tools/combat-power"):
        for base, dirs, files in os.walk(os.path.join(ROOT, folder)):
            dirs.sort()
            paths += [os.path.join(base, f) for f in sorted(files) if f.endswith((".yml", ".py"))]
    paths += [os.path.join(ROOT, p) for p in ("src/map/map.hpp", "src/common/mmo.hpp", "npc/scripts_custom.conf",
                                              "npc/miracle/jro_enchant.txt", "npc/miracle/follower_enchant.txt")]
    for p in paths:
        if os.path.exists(p):
            h.update(p[len(ROOT):].encode())
            with open(p, "rb") as f:
                h.update(hashlib.sha1(f.read()).digest())
    return h.hexdigest()


class _AnySkill(dict):
    """Lets every skill bonus through; the browser keeps the ones the chosen job has."""
    def __contains__(self, k):
        return True


def _load_cp():
    if not os.path.isdir(TOOLS):
        raise SystemExit(f"gen_cp: {TOOLS} not found (the game repository's Combat Power tools)")
    work = tempfile.mkdtemp(prefix="cp-")
    cwd = os.getcwd()
    os.chdir(work)  # cp.py reads items.pkl, written by load.py, from the working folder
    sys.path.insert(0, TOOLS)
    try:
        import contextlib
        import io
        with contextlib.redirect_stdout(io.StringIO()):
            runpy.run_path(os.path.join(TOOLS, "load.py"), run_name="__main__")
        import cp
        import weights
    finally:
        os.chdir(cwd)
        shutil.rmtree(work, ignore_errors=True)
    return cp, weights


class Builder:
    def __init__(self, cp):
        self.cp = cp
        self.any = _AnySkill()
        self.vecs, self.vec_id = [], {}
        self.tables, self.table_id = [], {}
        self.skills, self.skill_id = [], {}
        self.script_cache = {}

    def skill(self, name):
        if name not in self.skill_id:
            self.skill_id[name] = len(self.skills)
            self.skills.append(name)
        return self.skill_id[name]

    def raw_vec(self, recs):
        """Stat totals of one script run. Skill bonuses keep their skill: 'sa.<n>' damage %, 'cd.<n>', 'vc.<n>',
        'fc.<n>' cooldown / cast ms cut, where n indexes the skill list."""
        cp = self.cp
        vec = defaultdict(float)
        for r in recs:
            k, val = cp.score_rec(r, self.any)
            if k in (None, "_skip") or not val:
                continue
            if k in ("skillatk", "skillcd", "skillvctms", "skillfctms"):
                vec[{"skillatk": "sa.", "skillcd": "cd.", "skillvctms": "vc.", "skillfctms": "fc."}[k]
                    + str(self.skill(cp.skname(r[1][0])))] += val
            elif k == "allstats":
                for s in cp.STATS6:
                    vec[s] += val
            elif k == "alltraits":
                for s in cp.TRAITS6:
                    vec[s] += val
            elif k == "agivit":
                vec["agi"] += val
                vec["vit"] += val
            elif k == "agidexstr":
                for s in ("agi", "dex", "str"):
                    vec[s] += val
            elif k in cp.NOSTACK:
                vec[k] = max(vec[k], val)
            else:
                vec[k] += val
        return self.intern(vec)

    def intern(self, vec):
        out = {k: round(v, 3) for k, v in sorted(vec.items()) if abs(v) > 1e-9}
        key = json.dumps(out, sort_keys=True)
        if key not in self.vec_id:
            self.vec_id[key] = len(self.vecs)
            self.vecs.append(out)
        return self.vec_id[key]

    def delta(self, a, b):
        """Vector index of vecs[b] - vecs[a]."""
        va, vb = self.vecs[a], self.vecs[b]
        return self.intern({k: vb.get(k, 0) - va.get(k, 0) for k in set(va) | set(vb)})

    def run(self, it, script, job, r, g):
        recs, _ = self.cp.run_item(it, job, r, g, script)
        return self.raw_vec(recs)

    def table(self, script, it=None):
        """Index of the stat table of a script: [dims, values] where dims is a subset of 'jrg' (job, refine,
        grade) and values is the flat list of vector indexes, job outermost; a plain int when nothing varies."""
        script = script or ""
        if not script.strip():
            return -1
        if script in self.script_cache:
            return self.script_cache[script]
        cp = self.cp
        it = it or {}
        jobs = cp.JOBS if DEP_JOB.search(script) else cp.JOBS[:1]
        refs = list(REFINES) if DEP_REFINE.search(script) else [0]
        grades = list(GRADES) if DEP_GRADE.search(script) else [0]
        grid = [[[self.run(it, script, j, r, g) for g in grades] for r in refs] for j in jobs]
        # drop the dimensions that turned out not to matter
        dims = ""
        if len(jobs) > 1 and any(grid[i] != grid[0] for i in range(len(jobs))):
            dims += "j"
        else:
            grid = grid[:1]
        if len(refs) > 1 and any(row[i] != row[0] for row in grid for i in range(len(refs))):
            dims += "r"
        else:
            grid = [row[:1] for row in grid]
        if len(grades) > 1 and any(cell[i] != cell[0] for row in grid for cell in row for i in range(len(grades))):
            dims += "g"
        else:
            grid = [[cell[:1] for cell in row] for row in grid]
        if "r" in dims:
            # along the refine axis store the change from the refine before, which repeats a lot (+5 ATK a refine)
            nr = len(grid[0])
            grid = [[[grid[j][r][g] if r == 0 else self.delta(grid[j][r - 1][g], grid[j][r][g])
                      for g in range(len(grid[j][r]))] for r in range(nr)] for j in range(len(grid))]
        if "j" in dims:
            # jobs mostly fall into a few groups (one class check): keep each distinct slice once
            rows, jmap = [], []
            for row in grid:
                if row not in rows:
                    rows.append(row)
                jmap.append(rows.index(row))
            grid = rows
        flat = [v for row in grid for cell in row for v in cell]
        val = flat[0] if not dims else [dims, flat] + ([jmap] if "j" in dims else [])
        key = json.dumps(val)
        if key not in self.table_id:
            self.table_id[key] = len(self.tables)
            self.tables.append(val)
        self.script_cache[script] = self.table_id[key]
        return self.table_id[key]


def _locmask(it):
    m = 0
    for k, on in (it.get("Locations") or {}).items():
        if on:
            m |= LOC.get(k, 0)
            m |= {"COSTUME_HEAD_TOP": 1024, "COSTUME_HEAD_MID": 2048, "COSTUME_HEAD_LOW": 4096}.get(k, 0)
    return m


def generate():
    cp, weights = _load_cp()
    items = cp.items
    b = Builder(cp)
    njobs = len(cp.JOBS)

    def jobmask(it):
        return sum(1 << i for i, j in enumerate(cp.JOBS) if cp.can_equip(it, j))

    # ---------------------------------------------------------------- equipment
    eq = []
    for iid, it in sorted(items.items()):
        if it.get("Type") not in ("Weapon", "Armor", "Shadowgear", "ShadowGear"):
            continue
        loc = _locmask(it)
        jm = jobmask(it)
        if not loc or not jm:
            continue
        costume = loc & (1024 | 2048 | 4096 | 8192)
        if costume and not it.get("Script"):
            continue  # plain look-only costumes: the "Any costume" choice holds stones for them
        flags = (1 if it.get("Refineable") else 0) | (2 if it.get("Gradable") else 0)
        sub = it.get("SubType") or ""
        eq.append([iid, it.get("Name") or str(iid), loc, it.get("Slots") or 0, flags,
                   (it.get("WeaponLevel") if it.get("Type") == "Weapon" else it.get("ArmorLevel")) or 1,
                   it.get("Attack") or 0, it.get("MagicAttack") or 0, it.get("Defense") or 0, sub,
                   jm, b.table(it.get("Script"), it), {"Weapon": 1, "Armor": 0}.get(it.get("Type"), 2)])

    # ---------------------------------------------------------------- cards and stones
    cards = []
    for iid, it in sorted(items.items()):
        if it.get("Type") != "Card":
            continue
        loc = _locmask(it)
        if not loc:
            for rx, bit in STONE:
                if "Stone" in (it.get("Name") or "") and rx.search(it.get("Name") or ""):
                    loc = bit
                    break
        if not loc:
            continue
        cards.append([iid, it.get("Name") or str(iid), loc, b.table(it.get("Script"), it)])

    # ---------------------------------------------------------------- enchants
    enchant_items = {}
    sources, src_id, item_src = [], {}, defaultdict(list)
    for iid, lst in cp.ENCH.items():
        for s in lst:
            if s["kind"] == "slots":
                slots = []
                for sl in s["slots"]:
                    for c in sl:
                        if c not in enchant_items and c in items:
                            enchant_items[c] = [c, items[c].get("Name") or str(c), b.table(items[c].get("Script"), items[c])]
                    slots.append(sorted(c for c in sl if c in items))
                d = {"s": s["src"], "w": ", ".join(s.get("where") or []), "m": s.get("minref", 0), "slots": slots}
            else:
                pools = []
                for pool in (s["pool1"], s["pool2"]):
                    p = []
                    for name, lo, hi, script in pool:
                        lo, hi = lo or 0, hi or 0
                        vals = list(range(lo, hi + 1)) if hi > lo else [lo]
                        p.append([name, lo, hi, [b.table(script.replace("getrandomoptinfo(ROA_VALUE)", str(v)))
                                                for v in vals]])
                    pools.append(p)
                d = {"s": "iRO", "w": ", ".join(s.get("where") or []), "pools": pools, "n": [2, 1]}
            key = json.dumps(d, sort_keys=True)
            if key not in src_id:
                src_id[key] = len(sources)
                sources.append(d)
            item_src[iid].append(src_id[key])

    # ---------------------------------------------------------------- set bonuses
    combos, seen = [], set()
    for iid, lst in cp.COMBOS.items():
        for ids, script in lst:
            key = (tuple(sorted(ids)), script)
            if key in seen:
                continue
            seen.add(key)
            # refine/grade the set reads: the slot named in getequiprefinerycnt(EQI_..), else its first refinable piece
            m = EQI.search(script)
            ref = EQI_SLOT.get(m.group(1), 0) if m else 0
            first = next((x for x in ids if items.get(x, {}).get("Refineable")), ids[0])
            combos.append([sorted(ids), b.table(script, items.get(first)), ref, first])

    # ---------------------------------------------------------------- jobs, weights, refine tables
    jobs = []
    for label, *_ in cp.JOBS:
        sk = cp.JOBSK[label]
        tiers = cp.SKTIER[label]
        jobs.append({"n": label, "sk": {str(i): tiers.get(name, 4) for i, name in enumerate(b.skills) if name in sk}})
    refine = {}
    for (group, lvl, r), (bonus, rnd) in cp.REFINE_T.items():
        refine.setdefault(f"{group}{lvl}", [[0, 0] for _ in REFINES])
        if r < len(REFINES):
            refine[f"{group}{lvl}"][r] = [bonus, rnd]
    grade = {f"{t}{lvl}_{g}": v for (t, lvl, g), v in cp.GRADE_T.items()}
    w = {k: [v[0], v[1], v[2], v[3]] for k, v in weights.W.items()}

    skill_names = []
    sk_db = {}
    for path in ("db/re/skill_db.yml", "db/import/skill_db.yml"):
        import yaml
        with open(os.path.join(ROOT, path)) as f:
            for e in (yaml.load(f, Loader=yaml.CLoader).get("Body") or []):
                if "Name" in e:
                    sk_db[e["Name"]] = e.get("Description") or e["Name"]
    for name in b.skills:
        skill_names.append([name, sk_db.get(name, name.replace("_", " "))])

    # keep only the vectors the tables use (refine steps replaced the full vectors with changes)
    used = sorted({x for t in b.tables for x in (t[1] if isinstance(t, list) else [t])})
    remap = {old: new for new, old in enumerate(used)}
    b.tables = [remap[t] if not isinstance(t, list) else [t[0], [remap[x] for x in t[1]]] + t[2:] for t in b.tables]
    b.vecs = [b.vecs[i] for i in used]
    # vectors as flat [key index, value, ...] lists
    keys = sorted({k for v in b.vecs for k in v})
    kid = {k: i for i, k in enumerate(keys)}
    vecs = [[x for k, v in vec.items() for x in (kid[k], int(v) if v == int(v) else v)] for vec in b.vecs]
    return {
        "v": VERSION, "jobs": jobs, "skills": skill_names, "weights": w,
        "caps": {"curve": cp.SKILL_CURVE, "cd": cp.COOLDOWN_CAP, "rate": cp.CAPS},
        "refine": refine, "grade": grade, "nr": len(REFINES), "ng": len(GRADES), "nj": njobs,
        "keys": keys, "vecs": vecs, "tables": b.tables,
        "items": eq, "cards": cards, "enchants": sorted(enchant_items.values()),
        "sources": sources, "itemSources": {str(k): v for k, v in sorted(item_src.items())},
        "combos": combos,
    }


def _obtainable(out_dir):
    """obtain.json: items the Database knows a way to get (its "How to get" column), for the simulator's
    "only items you can get" filter. Rebuilt every time, since it follows the NPC scripts too."""
    index = os.path.join(os.path.dirname(out_dir), "db", "data", "items.json")
    ids = []
    if os.path.exists(index):
        with open(index, encoding="utf-8") as f:
            ids = [row[0] for row in json.load(f) if len(row) > 12 and row[12]]
    with open(os.path.join(out_dir, "obtain.json"), "w", encoding="utf-8") as f:
        json.dump(ids, f, separators=(",", ":"))


def build(out_dir, dir_urls=True):
    """Writes out_dir/data.json, reusing the published copy when nothing it is made from changed."""
    os.makedirs(out_dir, exist_ok=True)
    _obtainable(out_dir)
    target = os.path.join(out_dir, "data.json")
    stamp = _inputs_checksum()
    old = os.path.join(SITE_ROOT, "cp", "data.json")
    if os.path.exists(old):
        with open(old, encoding="utf-8") as f:
            head = f.read(200)
        m = re.search(r'"sum": "([0-9a-f]+)"', head)
        if m and m.group(1) == stamp:
            if os.path.abspath(old) != os.path.abspath(target):
                shutil.copyfile(old, target)
            return
    data = generate()
    data["dirUrls"] = dir_urls
    with open(target, "w", encoding="utf-8") as f:
        # the checksum goes first so the next build can read it without loading the whole file
        f.write('{"sum": "%s", ' % stamp)
        f.write(json.dumps(data, separators=(",", ":"))[1:])


if __name__ == "__main__":
    build(sys.argv[1] if len(sys.argv) > 1 else "cp-out")
