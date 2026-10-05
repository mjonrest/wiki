"""Fast loader for the server's YAML databases (db/*.yml).

PyYAML without libyaml takes minutes on the item and monster databases, so this reads the subset of YAML that
rAthena writes: nested maps, `- ` lists, quoted and plain scalars, and `|` blocks for scripts. Entries are
merged the way the server does it: files are read in Footer import order, and a later entry with the same key
replaces the fields it sets.
"""
import functools
import os
import re

from rodb import ROOT

_INT = re.compile(r"^-?\d+$")


def _uncomment(v):
    """Drops a trailing `# comment`, keeping a quoted value whole."""
    m = re.match(r"^(\"(?:[^\"\\]|\\.)*\"|'[^']*')", v)
    return m.group(1) if m else re.sub(r"(^|\s+)#.*$", "", v)


def _scalar(v):
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        v = v[1:-1]
        return v.replace('\\"', '"') if v else v
    if v in ("true", "True"):
        return True
    if v in ("false", "False"):
        return False
    if _INT.match(v):
        return int(v)
    return v


class _Parser:
    def __init__(self, text):
        self.lines = []
        for raw in text.replace("\t", "    ").split("\n"):
            s = raw.rstrip()
            st = s.lstrip()
            self.lines.append([len(s) - len(st), st])
        self.i = 0

    def _skip(self):
        while self.i < len(self.lines) and (not self.lines[self.i][1] or self.lines[self.i][1][0] == "#"):
            self.i += 1

    def _peek(self):
        self._skip()
        return self.lines[self.i] if self.i < len(self.lines) else None

    def node(self):
        line = self._peek()
        if line is None:
            return None
        if line[1] == "-" or line[1].startswith("- "):
            return self._seq(line[0])
        return self._map(line[0])

    def _seq(self, ind):
        out = []
        while True:
            line = self._peek()
            if not line or line[0] != ind or not (line[1] == "-" or line[1].startswith("- ")):
                return out
            rest = line[1][2:].strip()
            if not rest:
                self.i += 1
                out.append(self.node())
            elif re.match(r"^[^\"'\s][^:]*:(\s|$)", rest):
                line[0], line[1] = ind + 2, rest  # "- Key: v" opens a map indented past the dash
                out.append(self._map(ind + 2))
            else:
                self.i += 1
                out.append(_scalar(_uncomment(rest)))

    def _block(self, ind):
        body = []
        while self.i < len(self.lines):
            li, st = self.lines[self.i]
            if st and li <= ind:
                break
            body.append((li, st))
            self.i += 1
        while body and not body[-1][1]:
            body.pop()
        base = min((li for li, st in body if st), default=0)
        return "\n".join(" " * (li - base) + st if st else "" for li, st in body)

    def _map(self, ind):
        out = {}
        while True:
            line = self._peek()
            if not line or line[0] != ind or line[1] == "-" or line[1].startswith("- "):
                return out
            key, _, val = line[1].partition(":")
            key, val = key.strip().strip("\"'"), _uncomment(val.strip())
            self.i += 1
            if val in ("|", "|-", "|+", ">", ">-"):
                out[key] = self._block(ind)
            elif val:
                out[key] = _scalar(val)
            else:
                nxt = self._peek()
                if nxt and (nxt[0] > ind or (nxt[0] == ind and (nxt[1] == "-" or nxt[1].startswith("- ")))):
                    out[key] = self.node()
                else:
                    out[key] = None


@functools.lru_cache(None)
def load(rel):
    """The whole file as a dict (Header, Body, Footer)."""
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8", errors="replace") as f:
        return _Parser(f.read().replace("\ufffd", "")).node() or {}


def files(rel):
    """`rel` and every file it imports, in the order the server reads them (renewal mode)."""
    out = []

    def walk(r):
        if r in out:
            return
        out.append(r)
        for imp in (load(r).get("Footer") or {}).get("Imports") or []:
            if imp.get("Mode") != "Prerenewal" and imp.get("Path"):
                walk(imp["Path"])

    walk(rel)
    return out


@functools.lru_cache(None)
def table(rel, key="Id"):
    """{key: entry} for a database and its imports, later files overriding earlier fields."""
    out = {}
    for r in files(rel):
        for e in load(r).get("Body") or []:
            if not isinstance(e, dict) or e.get(key) is None:
                continue
            k = e[key]
            out[k] = {**out[k], **e} if k in out else dict(e)
    return out


def items():
    return table("db/item_db.yml")


def mobs():
    return table("db/mob_db.yml")


def skills():
    return table("db/skill_db.yml")


def skill_tree():
    return table("db/skill_tree.yml", "Job")


def job_stats():
    out = []
    for r in files("db/job_stats.yml"):
        out += [e for e in load(r).get("Body") or [] if isinstance(e, dict)]
    return out
