"""Readers for the official (non-custom) rAthena content the server loads.

Used by the macros in main.py for the "Official content" pages.
"""
import functools
from collections import OrderedDict
import os
import re

import sys

import yaml

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "tools"))
from rodb import ROOT  # noqa: E402
import ydb  # noqa: E402

NPC_START = re.compile(
    r"^(?:(?P<map>[\w@-]+),(?P<x>\d+),(?P<y>\d+),\d+|-|function)\t"
    r"(?:script(?:\([^)]*\))?|duplicate\([^)]*\)|shop|cashshop|itemshop|pointshop|marketshop)\t(?P<name>[^\t]+)\t"
)
STR_ASSIGN = re.compile(r"""([.'$]?@?\w+\$)\s*(?:=|,)\s*"([^"]+)"\s*[;)]""")
INSTANCE_CALL = re.compile(r"instance_(create|enter)\s*\(\s*([^,)]+)\s*(?:,\s*([^,)]+))?")


def _read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8", errors="replace") as f:
        return f.read().replace("\ufffd", "")


def _strip_comments(text):
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    return "\n".join(re.sub(r"(^|\s)//.*$", "", line) for line in text.split("\n"))


@functools.lru_cache(None)
def official_scripts():
    """Script files loaded by npc/re/scripts_main.conf, minus scripts_custom.conf."""
    files, seen = [], set()

    def walk(conf):
        if conf in seen or not os.path.exists(os.path.join(ROOT, conf)):
            return
        seen.add(conf)
        for line in _read(conf).splitlines():
            m = re.match(r"^(npc|import):\s*(\S.*?)\s*$", line)
            if not m:
                continue
            if m.group(1) == "import":
                if not m.group(2).endswith("scripts_custom.conf"):
                    walk(m.group(2))
            elif m.group(2) not in files:
                files.append(m.group(2))

    walk("npc/re/scripts_main.conf")
    return [f for f in files if os.path.exists(os.path.join(ROOT, f))]


def instance_scripts():
    """Official scripts plus the official-style ones the server loads from scripts_custom.conf (npc/ep17,
    npc/custom); Miracle's own npc/miracle scripts are covered by the Content pages."""
    extra = []
    for line in _read("npc/scripts_custom.conf").splitlines():
        m = re.match(r"^npc:\s*(\S.*?)\s*$", line)
        if m and not m.group(1).startswith("npc/miracle/") and os.path.exists(os.path.join(ROOT, m.group(1))):
            extra.append(m.group(1))
    return list(dict.fromkeys(official_scripts() + extra))


@functools.lru_cache(None)
def blocks(rel):
    """[(header match, body text)] for every top-level definition in a script file."""
    lines = _strip_comments(_read(rel)).split("\n")
    out, cur, body = [], None, []
    for line in lines:
        m = NPC_START.match(line)
        if m:
            if cur:
                out.append((cur, "\n".join(body)))
            cur, body = m, [line]
        elif cur:
            body.append(line)
    if cur:
        out.append((cur, "\n".join(body)))
    return out


def _yaml_body(rels):
    out = []
    for rel in rels:
        path = os.path.join(ROOT, rel)
        if os.path.exists(path):
            with open(path, encoding="utf-8") as f:
                out.extend((yaml.safe_load(f) or {}).get("Body") or [])
    return out


@functools.lru_cache(None)
def instance_db():
    """{name: entry} from every file db/instance_db.yml imports (later files override)."""
    out = {}
    for e in _yaml_body(ydb.files("db/instance_db.yml")[1:]):
        if e.get("Name"):
            out[e["Name"]] = e
    return out


@functools.lru_cache(None)
def quest_db():
    """{id: {Title, TimeLimit}}; read by regex since quest_db.yml has tabs PyYAML rejects."""
    out = {}
    for rel in ydb.files("db/quest_db.yml")[1:]:
        if not os.path.exists(os.path.join(ROOT, rel)):
            continue
        cur = None
        for line in _read(rel).splitlines():
            m = re.match(r"^\s*-\s*Id:\s*(\d+)", line)
            if m:
                cur = out.setdefault(int(m.group(1)), {})
                continue
            m = re.match(r"^\s{4}(Title|TimeLimit):\s*(.*?)\s*$", line)
            if m and cur is not None:
                cur[m.group(1)] = m.group(2).strip('"')
    return out


def duration(text_or_secs):
    """'4h' / '+3d' / '4:00' / 7200 -> readable string."""
    if text_or_secs is None:
        return ""
    if isinstance(text_or_secs, int):
        s = text_or_secs
        h, m = divmod(s // 60, 60)
        return (f"{h}h" if h else "") + (f" {m}m" if m else "") or f"{s}s"
    t = str(text_or_secs).strip()
    if re.fullmatch(r"\d+:\d+", t):
        return f"resets daily at {t}"
    t = t.lstrip("+")
    names = {"d": "day", "h": "hour", "mn": "min", "m": "min", "s": "sec"}
    parts = re.findall(r"(\d+)(d|h|mn|m|s)", t)
    if not parts:
        return t
    return " ".join(f"{n} {names[u]}{'s' if int(n) > 1 and names[u] in ('day', 'hour') else ''}" for n, u in parts)


@functools.lru_cache(None)
def instances():
    """Official instances the server loads, with entrance and limits read from their scripts."""
    db = instance_db()
    found = {}
    for rel in instance_scripts():
        blks = blocks(rel)
        whole = "\n".join(b for _, b in blks)
        literals = [n for n in db if f'"{n}"' in whole]
        vars_ = {}
        for v, val in STR_ASSIGN.findall(whole):
            if val in db:
                vars_.setdefault(v, []).append(val)
        for hdr, body in blks:
            # .@ variables are local to one NPC, so a value set in this block wins over the rest of the file.
            local = {}
            for v, val in STR_ASSIGN.findall(body):
                if val in db:
                    local.setdefault(v, []).append(val)
            for kind, arg, mode in INSTANCE_CALL.findall(body):
                arg = arg.strip()
                if arg.startswith('"'):
                    names = [arg.strip('"')]
                else:
                    names = local.get(arg) or vars_.get(arg) or literals
                for name in names:
                    if name in db:
                        _note(found, name, rel, hdr, body, kind, mode)
        # Level checks often sit in a talk NPC next to the one that opens the instance.
        mine = [r for r in found.values() if r["file"] == rel]
        if len(mine) == 1 and mine[0]["level"] is None:
            for hdr, body in blks:
                if hdr.group("map") and "@" not in hdr.group("map"):
                    lv = re.findall(r"BaseLevel\s*<\s*(\d+)", body)
                    if lv:
                        mine[0]["level"] = int(lv[0])
                        break
    for rec in found.values():
        e = db[rec["name"]]
        rec["time_limit"] = e.get("TimeLimit", 3600)
        rec["id"] = e.get("Id")
        cds = [quest_db().get(q, {}).get("TimeLimit") for q in rec["cooldowns"]]
        cds = [c for c in cds if c]
        rec["cooldown"] = duration(max(cds, key=_seconds)) if cds else ""
    return sorted(found.values(), key=lambda r: (r["level"] is None, r["level"] or 0, r["name"]))


def _seconds(t):
    t = str(t).lstrip("+")
    if re.fullmatch(r"\d+:\d+", t):
        return 86400
    mult = {"d": 86400, "h": 3600, "mn": 60, "m": 60, "s": 1}
    return sum(int(n) * mult[u] for n, u in re.findall(r"(\d+)(d|h|mn|m|s)", t))


def _note(found, name, rel, hdr, body, kind, mode):
    rec = found.setdefault(name, dict(name=name, file=rel, entrances=[], level=None,
                                      cooldowns=[], mode=None))
    if kind == "create" and mode:
        rec["mode"] = mode.strip()
    if hdr.group("map") and "@" not in hdr.group("map"):
        spot = (hdr.group("map"), int(hdr.group("x")), int(hdr.group("y")),
                hdr.group("name").split("#")[0].split("::")[0].strip())
        if spot not in rec["entrances"]:
            rec["entrances"].append(spot)
    lv = re.findall(r"BaseLevel\s*<\s*(\d+)", body) or re.findall(r"BaseLevel\s*>=\s*(\d+)", body)
    if lv and rec["level"] is None:
        rec["level"] = int(lv[0])
    for qid in re.findall(r"checkquest\s*\(\s*(\d+)\s*,\s*PLAYTIME", body):
        if int(qid) not in rec["cooldowns"]:
            rec["cooldowns"].append(int(qid))


def visible_npcs(rel):
    """[(name, map, x, y)] for NPCs players can click in an official script file."""
    out = []
    for hdr, _ in blocks(rel):
        if not hdr.group("map") or "@" in hdr.group("map"):
            continue
        raw = hdr.group("name")
        name = raw.split("::")[0].split("#")[0].strip()
        if not name or name.startswith(("#", ".")):
            continue
        out.append((name, hdr.group("map"), int(hdr.group("x")), int(hdr.group("y"))))
    return out


# ---------------------------------------------------------------------------
# Per-script details for the instance pages.

from rodb import item_id as _item_id, items as _items  # noqa: E402


@functools.lru_cache(None)
def mob_db():
    """{id: {name, aegis, level, hp, race, element, size, class, mvp, drops:[(aegis, rate)], mvp_drops:[...]}}

    Read with the full YAML loader (tools/ydb.py), so entries with commented-out drop lines are not lost."""
    import ydb
    out = {}
    for mid, e in ydb.mobs().items():
        out[int(mid)] = dict(
            name=e.get("Name") or e.get("AegisName") or f"Monster #{mid}", aegis=e.get("AegisName"),
            level=e.get("Level", 1), hp=e.get("Hp", 1), race=e.get("Race", "Formless"),
            element=f'{e.get("Element", "Neutral")} {e.get("ElementLevel", 1)}',
            size=e.get("Size", "Small"), cls=e.get("Class", "Normal"),
            mvp=bool(e.get("MvpExp")) or bool(e.get("MvpDrops")),
            drops=[(d["Item"], d["Rate"]) for d in e.get("Drops") or [] if d.get("Item") and d.get("Rate")],
            mvp_drops=[(d["Item"], d["Rate"]) for d in e.get("MvpDrops") or [] if d.get("Item") and d.get("Rate")],
        )
    return out


@functools.lru_cache(None)
def mob_by_aegis():
    return {v["aegis"]: k for k, v in mob_db().items() if v.get("aegis")}


def _mob_ref(tok):
    tok = tok.strip().strip('"')
    if tok.isdigit():
        mid = int(tok)
        return mid if mid in mob_db() else None
    return mob_by_aegis().get(tok)


def _item_ref(tok):
    tok = tok.strip().strip('"')
    if tok.isdigit():
        return int(tok) if int(tok) in _items()[0] else None
    return _item_id(tok)


def _split_args(s):
    """Split a script argument list on top-level commas."""
    out, depth, cur, q = [], 0, "", False
    for ch in s:
        if ch == '"':
            q = not q
        if not q and ch in "([":
            depth += 1
        elif not q and ch in ")]":
            depth -= 1
        if ch == "," and depth == 0 and not q:
            out.append(cur)
            cur = ""
        else:
            cur += ch
    out.append(cur)
    return [a.strip() for a in out]


def _setarrays(text):
    """{var: [values]} for every setarray in a script (later ones extend earlier ones)."""
    out = {}
    for var, vals in re.findall(r"setarray\s+([.'$@\w]+?)(?:\[\d+\])?\s*,\s*([^;]+);", text, re.I):
        out.setdefault(var, []).extend(_split_args(vals))
    return out


class _Resolver:
    """Possible values of a script expression, as tokens (ids or aegis names): numbers, names, arrays, variables
    (from their assignments and for loops), rand(a,b), F_Rand(...), base+variable and getarg(n) of a callsub."""

    def __init__(self, text):
        self.text = text
        self.arrays = _setarrays(text)

    def _assigned(self, var, scope):
        v = re.escape(var)
        out = re.findall(r"(?<![\w.'$@])" + v + r"\s*=(?!=)\s*([^;]+);", scope)
        out += re.findall(r"\bset\s+" + v + r"\s*,\s*([^;]+);", scope)
        for a, op, b in re.findall(r"for\s*\(\s*" + v + r"\s*=\s*(\d+)\s*;\s*" + v + r"\s*(<=?)\s*(\d+)", scope):
            hi = int(b) + (op == "<=")
            if 0 < hi - int(a) <= 40:
                out += [str(i) for i in range(int(a), hi)]
        return out

    def values(self, expr, scope, depth=0):
        expr = re.sub(r"\s+", " ", expr).strip()
        while expr.startswith("(") and expr.endswith(")") and expr.count("(") == 1:
            expr = expr[1:-1].strip()
        expr = re.sub(r"^atoi\((.*)\)$", r"\1", expr).strip().strip('"')
        if depth > 4 or not expr:
            return []
        if re.fullmatch(r"\d+|[A-Za-z][A-Za-z0-9_]*", expr) and not re.fullmatch(r"getarg|rand", expr):
            return [expr]
        m = re.fullmatch(r"rand\(\s*(\d+)\s*,\s*(\d+)\s*\)", expr)
        if m:
            a, b = int(m.group(1)), int(m.group(2))
            return [str(i) for i in range(a, b + 1)] if 0 <= b - a <= 40 else []
        m = re.fullmatch(r"(?:callfunc\s*\(?\s*\"F_Rand\"\s*,|F_Rand\s*\()(.*)\)", expr)
        if m:
            return [v for a in _split_args(m.group(1)) for v in self.values(a, scope, depth + 1)]
        m = re.fullmatch(r"([.'$@]*\w+\$?)\[.*\]", expr) or re.fullmatch(r"getelementofarray\(\s*([.'$@]*\w+)", expr)
        if m:
            return [v for a in self.arrays.get(m.group(1), []) for v in self.values(a, scope, depth + 1)]
        m = re.fullmatch(r"\(?\s*(\d+)\s*\+\s*\(\s*\(?[.'$@\w]+\s*-\s*1\)?\s*%\s*(\d+)\s*\)\s*\)?", expr)
        if m:  # base + ((n-1) % k)
            return [str(int(m.group(1)) + i) for i in range(int(m.group(2)))] if int(m.group(2)) <= 40 else []
        m = re.fullmatch(r"(\d+)\s*\+\s*(.+)|(.+?)\s*\+\s*(\d+)", expr)
        if m:
            base, var = (m.group(1), m.group(2)) if m.group(1) else (m.group(4), m.group(3))
            offs = [int(v) for v in self.values(var, scope, depth + 1) if v.isdigit() and int(v) < 100]
            return [str(int(base) + o) for o in sorted(set(offs))]
        m = re.fullmatch(r'get_instance_var\(\s*"([^"]*)"(.*)\)', expr)
        if m:  # set_instance_var("name", value), or a name built from the same first part
            key, rest = re.escape(m.group(1)), m.group(2)
            vals = re.findall(r'set_instance_var\(\s*"' + key + (r'"' if not rest.strip() else r'[^,]*') + r"\s*,\s*([^;]+?)\)\s*;", self.text)
            return [v for a in vals for v in self.values(a, scope, depth + 1)]
        m = re.fullmatch(r"getarg\(\s*(\d+)\s*(?:,[^)]*)?\)", expr)
        if m:
            return [v for a in self._args(int(m.group(1)), scope) for v in self.values(a, scope, depth + 1)]
        if re.fullmatch(r"[.'$@]+\w+\$?", expr):
            found = self._assigned(expr, scope)
            if not found and scope is not self.text:
                found = self._assigned(expr, self.text)
            return [v for a in found for v in self.values(a, scope, depth + 1)]
        return []

    def _args(self, n, scope):
        """Argument n of every callsub/callfunc into the label or function this getarg sits in."""
        names = re.findall(r"^\s*(\w+)\s*:", scope, re.M) + re.findall(r"^function\s+script\s+(\w+)", scope, re.M) + \
            re.findall(r"^function\t\w+\t(\w+)", scope, re.M)
        out = []
        for name in set(names):
            for call in re.findall(r"\bcall(?:sub|func)\s*\(?\s*\"?" + re.escape(name) + r"\"?\s*,([^;]*);", self.text):
                args = _split_args(call.rstrip().rstrip(")"))
                if len(args) > n:
                    out.append(args[n])
        return out


@functools.lru_cache(None)
def script_details(rel):
    """Monsters spawned, items given and shops of one official script file."""
    text = "\n".join(b for _, b in blocks(rel))
    arrays = _setarrays(text)
    mobs = []

    def add_mob(tok):
        mid = _mob_ref(tok)
        if mid and mid not in mobs:
            mobs.append(mid)

    res = _Resolver(text)
    for _, body in blocks(rel):
        for cmd, call in re.findall(r"\b(monster|areamonster|bg_monster)\b\s*\(?\s*([^;]+);", body):
            args = _split_args(call)
            pos = {"monster": 4, "areamonster": 6, "bg_monster": 5}[cmd]
            if len(args) <= pos:
                continue
            for v in res.values(args[pos], body):
                add_mob(v)
    # Spawn helpers (callfunc "F_Tower_Monster_Summon", ...): a monster label followed by its id.
    for label, tok in re.findall(r'"([^"]*)"\s*,\s*("?[A-Z0-9_]+"?)\s*,', text):
        mid = _mob_ref(tok)
        if not mid:
            continue
        name = (mob_db()[mid]["name"] or "").lower()
        label = label.lower()
        if label in ("--ja--", "--en--") or (name and (name in label or label.endswith(name[:8]))):
            add_mob(tok)
    for var, vals in arrays.items():
        if re.search(r"mob|monster|boss|mvp", var, re.I):
            for v in vals:
                add_mob(v)

    rewards = OrderedDict()
    for _, body in blocks(rel):
        for call in re.findall(r"\b(?:getitem2|getitembound2|getitembound|getitem|rentitem2|rentitem|makeitem2|makeitem)\b\s*\(?\s*([^;]+);", body):
            args = _split_args(call)
            if len(args) < 2:
                continue
            amt = args[1] if args[1].isdigit() else ""
            for v in res.values(args[0], body):
                iid = _item_ref(v)
                if iid and iid not in rewards:
                    rewards[iid] = amt
    for var, vals in arrays.items():
        if re.search(r"reward|prize|box|item", var, re.I) and not re.search(r"amount|count|cost|req", var, re.I):
            for v in vals:
                iid = _item_ref(v)
                if iid and iid not in rewards and iid > 500:
                    rewards[iid] = ""

    shops = []
    for hdr, body in blocks(rel):
        if re.match(r"^\S+\t(shop|cashshop|itemshop|pointshop|marketshop)\t", body):
            shops.append(hdr.group("name").split("#")[0].split("::")[0].strip())
    return dict(mobs=mobs, rewards=rewards, shops=shops)


def description(rel):
    """The script header's description lines, minus conversion tags."""
    m = re.search(r"//=+ ?Description:? ?=*\s*\n(.*?)\n//={5,}", _read(rel), re.S)
    if not m:
        return ""
    lines = []
    for line in m.group(1).splitlines():
        line = re.sub(r"^//[=\-]*\s*", "", line).strip()
        if not line or re.match(r"^\[.*Conversion\]$", line) or line.lower().startswith(("todo", "- ")):
            continue
        lines.append(line)
    return " ".join(lines)


@functools.lru_cache(None)
def _files_by_map():
    out = {}
    for rel in instance_scripts():
        for hdr, _ in blocks(rel):
            if hdr.group("map"):
                out.setdefault(hdr.group("map"), [])
                if rel not in out[hdr.group("map")]:
                    out[hdr.group("map")].append(rel)
    return out


def instance_maps(name):
    e = instance_db().get(name, {})
    maps = [(e.get("Enter") or {}).get("Map")] + list((e.get("AdditionalMaps") or {}).keys())
    return [m for m in maps if m]


def instance_files(rec):
    """The script that opens the instance plus every script with NPCs on its maps."""
    files = [rec["file"]]
    for m in instance_maps(rec["name"]):
        for rel in _files_by_map().get(m, []):
            if rel not in files:
                files.append(rel)
    return files


def instance_details(rec):
    mobs, rewards, shops = [], OrderedDict(), []
    for rel in instance_files(rec):
        d = script_details(rel)
        mobs += [m for m in d["mobs"] if m not in mobs]
        if rel == rec["file"] and "instances" not in rel:
            continue  # a quest script: its rewards and shops belong to the quests
        for k, v in d["rewards"].items():
            rewards.setdefault(k, v)
        shops += [s for s in d["shops"] if s not in shops]
    return dict(mobs=mobs, rewards=rewards, shops=shops)


# Instance names in instance_db.yml that read badly on a page.
TITLES = {
    "Fogh_Normal": "Fall of Glast Heim (Normal)",
    "Fogh_Hard": "Fall of Glast Heim (Hard)",
    "Fogh": "Fall of Glast Heim",
    "Werner Laboratory central room#1": "Werner Laboratory Central Room",
    "Werner Laboratory central room#2": "Werner Laboratory Central Room (Hard)",
    "Werner Laboratory central room": "Werner Laboratory Central Room",
    "Last room": "Last Room",
    "Wave Mode": "Wave Mode",
}


def title(name):
    return TITLES.get(name, name)


VARIANT = re.compile(r"\s*(?:\((?:Normal|Hard|Advanced|Beginner)\)|Advanced|Hard|#\d+| - (?:Forest|Sky)|_Normal|_Hard)$", re.I)


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


@functools.lru_cache(None)
def instance_groups():
    """[(key, [records])]: an instance and its harder variants share one page."""
    groups = OrderedDict()
    for rec in instances():
        base = VARIANT.sub("", rec["name"]).strip()
        groups.setdefault((rec["file"], base), []).append(rec)
    return [(slug(title(base)), title(base), recs) for (_, base), recs in groups.items()]


def group(key):
    for k, t, recs in instance_groups():
        if k == key:
            return t, recs
    raise KeyError(key)


def page_of(name):
    for k, _, recs in instance_groups():
        if any(r["name"] == name for r in recs):
            return k
    return None


# ---------------------------------------------------------------------------
# Where instance materials are traded or used.

@functools.lru_cache(None)
def barter_db():
    """{shop name: [(item id, [(required id, amount)])]} from the official barter files."""
    out = {}
    queue, seen = ["npc/barters.yml", "npc/re/merchants/barters.yml"], set()
    while queue:
        rel = queue.pop(0)
        if rel in seen or not os.path.exists(os.path.join(ROOT, rel)):
            continue
        seen.add(rel)
        try:
            data = yaml.safe_load(_read(rel).replace("\t", "  ")) or {}
        except yaml.YAMLError:
            continue
        for imp in (data.get("Footer") or {}).get("Imports") or []:
            queue.append(imp["Path"])
        for shop in data.get("Body") or []:
            rows = []
            for it in shop.get("Items") or []:
                gid = _item_ref(str(it.get("Item", "")))
                req = [(_item_ref(str(r.get("Item", ""))), r.get("Amount", 1)) for r in it.get("RequiredItems") or []]
                if gid:
                    rows.append((gid, [(i, a) for i, a in req if i]))
            out[shop["Name"]] = rows
    return out


@functools.lru_cache(None)
def callshop_spots():
    """[(shop name or prefix, npc name, map, x, y)] for NPCs that open a barter/market shop."""
    out = []
    for rel in official_scripts():
        for hdr, body in blocks(rel):
            if not hdr.group("map") or "@" in hdr.group("map"):
                continue
            npc = hdr.group("name").split("#")[0].split("::")[0].strip()
            for name in re.findall(r'callshop\s*\(?\s*"([^"]+)"', body):
                out.append((name, npc, hdr.group("map"), int(hdr.group("x")), int(hdr.group("y"))))
    return out


def _block_items(body, cmd_regex, arrays):
    ids = []
    scalars = {}
    for var, val in re.findall(r"([.'$@]+\w+)\s*=\s*(\d{3,7})\s*;", body):
        scalars.setdefault(var, []).append(val)
    for call in re.findall(cmd_regex + r"\s+([^;]+);", body):
        arg = _split_args(call)[0]
        m = re.match(r"([.'$@\w]+)\[", arg)
        vals = arrays.get(m.group(1), []) if m else scalars.get(arg, [arg])
        for v in vals:
            iid = _item_ref(v)
            if iid and iid not in ids:
                ids.append(iid)
    return ids


@functools.lru_cache(None)
def item_users():
    """{item id: [trade dicts]} for every visible official NPC that takes the item."""
    out = {}
    for rel in official_scripts():
        for hdr, body in blocks(rel):
            if not hdr.group("map") or "@" in hdr.group("map"):
                continue
            arrays = _setarrays(body)
            takes = _block_items(body, r"\bdelitem", arrays)
            if not takes:
                continue
            gives = [i for i in _block_items(body, r"\b(?:getitem|getitem2|rentitem|getitembound)", arrays)
                     if i not in takes]
            enchants = []
            for var, vals in arrays.items():
                if re.search(r"enchant", var, re.I) and not re.search(r"cost|rate|per|chance", var, re.I):
                    enchants += [i for i in (_item_ref(v) for v in vals) if i and i not in enchants]
            npc = hdr.group("name").split("#")[0].split("::")[0].strip()
            rec = dict(npc=npc, spot=(hdr.group("map"), int(hdr.group("x")), int(hdr.group("y"))),
                       takes=takes, gives=gives, enchants=enchants, kind="script")
            for t in takes:
                out.setdefault(t, []).append(rec)
    spots = callshop_spots()
    for shop, rows in barter_db().items():
        npc_spots = [(n, (m, x, y)) for s, n, m, x, y in spots if shop == s or (shop.startswith(s) and len(s) > 4)]
        if not npc_spots:
            continue
        npc, spot = npc_spots[0]
        takes = []
        for _, req in rows:
            takes += [i for i, _ in req if i not in takes]
        rec = dict(npc=npc, spot=spot, takes=takes, gives=[g for g, _ in rows], enchants=[], kind="barter",
                   recipes=rows)
        for t in takes:
            out.setdefault(t, []).append(rec)
    return out


@functools.lru_cache(None)
def item_droppers():
    """{item id: set of monster ids that drop it}."""
    out = {}
    for mid, m in mob_db().items():
        for aegis, _ in m["drops"] + m["mvp_drops"]:
            iid = _item_id(aegis)
            if iid:
                out.setdefault(iid, set()).add(mid)
    return out
