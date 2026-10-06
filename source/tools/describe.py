"""Turns rAthena item scripts into plain English for the Database item pages.

    describe(script) -> [line, ...]

A line is a string, [heading, [line, ...]] for a condition with its effects, or {"c": source} for a statement
the translator does not understand (shown as code). Strings may hold links written as ⟦i:ID|Name⟧ (item),
⟦m:ID|Name⟧ (monster) or ⟦k:AEGIS_NAME|Name⟧ (skill); db.js turns them into links.

Bonus meanings follow doc/item_bonus.txt from the server. Values that depend on refine, level or stats are
written out ("MATK +20 for every 2 refine levels"); anything the translator cannot read falls back to code.
"""
import functools
import re

import ydb

# ---------------------------------------------------------------- names


@functools.lru_cache(None)
def _db():
    items = ydb.items()
    by_aegis = {str(v.get("AegisName")): k for k, v in items.items() if v.get("AegisName")}
    mobs = ydb.mobs()
    skills = ydb.skills()
    sk_aegis = {str(v.get("Name")): k for k, v in skills.items()}
    return items, by_aegis, mobs, skills, sk_aegis


def _words(s):
    s = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", s.replace("_", " "))
    return re.sub(r"\s+", " ", s).strip()


RACE = {"RC_Angel": "Angel", "RC_Brute": "Brute", "RC_DemiHuman": "Demi-Human", "RC_Demon": "Demon",
        "RC_Dragon": "Dragon", "RC_Fish": "Fish", "RC_Formless": "Formless", "RC_Insect": "Insect",
        "RC_Plant": "Plant", "RC_Player_Human": "Human players", "RC_Player": "players",
        "RC_Player_Doram": "Doram players", "RC_Undead": "Undead", "RC_All": "every race",
        "RC_NonBoss": "normal monsters", "RC_Boss": "boss monsters", "RC_NonPlayer": "monsters"}
RACE_SUFFIX = {"RC_Player_Human", "RC_Player", "RC_Player_Doram", "RC_All", "RC_NonBoss", "RC_Boss", "RC_NonPlayer"}
ELE = {"Ele_Neutral": "Neutral", "Ele_Water": "Water", "Ele_Earth": "Earth", "Ele_Fire": "Fire", "Ele_Wind": "Wind",
       "Ele_Poison": "Poison", "Ele_Holy": "Holy", "Ele_Dark": "Shadow", "Ele_Ghost": "Ghost", "Ele_Undead": "Undead",
       "Ele_All": "all"}
SIZE = {"Size_Small": "small", "Size_Medium": "medium", "Size_Large": "large", "Size_All": "all"}
CLASS = {"Class_Normal": "normal monsters", "Class_Boss": "boss monsters", "Class_Guardian": "guardians",
         "Class_All": "all enemies"}
EFF = {"Eff_DPoison": "Deadly Poison", "Eff_Stone": "Stone Curse", "Eff_WhiteImprison": "White Imprison",
       "Eff_Deepsleep": "Deep Sleep", "Eff_Crystalize": "Crystallization", "Eff_Freezing": "Freezing",
       "Eff_Burning": "Burning", "Eff_Bleeding": "Bleeding", "Eff_Stun": "Stun"}
WEAPON = {"W_FIST": "bare hands", "W_DAGGER": "a Dagger", "W_1HSWORD": "a One-Handed Sword",
          "W_2HSWORD": "a Two-Handed Sword", "W_1HSPEAR": "a One-Handed Spear", "W_2HSPEAR": "a Two-Handed Spear",
          "W_1HAXE": "a One-Handed Axe", "W_2HAXE": "a Two-Handed Axe", "W_MACE": "a Mace",
          "W_2HMACE": "a Two-Handed Mace", "W_STAFF": "a Staff", "W_2HSTAFF": "a Two-Handed Staff",
          "W_BOW": "a Bow", "W_KNUCKLE": "a Knuckle", "W_MUSICAL": "an Instrument", "W_WHIP": "a Whip",
          "W_BOOK": "a Book", "W_KATAR": "a Katar", "W_REVOLVER": "a Revolver", "W_RIFLE": "a Rifle",
          "W_GATLING": "a Gatling Gun", "W_SHOTGUN": "a Shotgun", "W_GRENADE": "a Grenade Launcher",
          "W_HUUMA": "a Huuma Shuriken", "W_SHIELD": "a Shield"}
SLOT = {"EQI_HEAD_TOP": "upper headgear", "EQI_HEAD_MID": "middle headgear", "EQI_HEAD_LOW": "lower headgear",
        "EQI_ARMOR": "armor", "EQI_HAND_L": "left hand", "EQI_HAND_R": "weapon", "EQI_GARMENT": "garment",
        "EQI_SHOES": "shoes", "EQI_ACC_L": "left accessory", "EQI_ACC_R": "right accessory",
        "EQI_COSTUME_HEAD_TOP": "costume upper headgear", "EQI_COSTUME_HEAD_MID": "costume middle headgear",
        "EQI_COSTUME_HEAD_LOW": "costume lower headgear", "EQI_COSTUME_GARMENT": "costume garment",
        "EQI_AMMO": "ammunition", "EQI_SHADOW_ARMOR": "shadow armor", "EQI_SHADOW_WEAPON": "shadow weapon",
        "EQI_SHADOW_SHIELD": "shadow shield", "EQI_SHADOW_SHOES": "shadow shoes",
        "EQI_SHADOW_ACC_R": "right shadow earring", "EQI_SHADOW_ACC_L": "left shadow pendant"}
STAT = {"bStr": "STR", "bAgi": "AGI", "bVit": "VIT", "bInt": "INT", "bDex": "DEX", "bLuk": "LUK",
        "bPow": "POW", "bSta": "STA", "bWis": "WIS", "bSpl": "SPL", "bCon": "CON", "bCrt": "CRT"}
SC = {"SC_STRFOOD": "STR +{1}", "SC_AGIFOOD": "AGI +{1}", "SC_VITFOOD": "VIT +{1}", "SC_INTFOOD": "INT +{1}",
      "SC_DEXFOOD": "DEX +{1}", "SC_LUKFOOD": "LUK +{1}", "SC_FOOD_STR_CASH": "STR +{1}",
      "SC_FOOD_AGI_CASH": "AGI +{1}", "SC_FOOD_VIT_CASH": "VIT +{1}", "SC_FOOD_INT_CASH": "INT +{1}",
      "SC_FOOD_DEX_CASH": "DEX +{1}", "SC_FOOD_LUK_CASH": "LUK +{1}", "SC_HITFOOD": "HIT +{1}",
      "SC_FLEEFOOD": "FLEE +{1}", "SC_CRIFOOD": "CRIT +{1}", "SC_BATKFOOD": "ATK +{1}", "SC_MATKFOOD": "MATK +{1}",
      "SC_ATKPOTION": "ATK +{1}", "SC_MATKPOTION": "MATK +{1}", "SC_INCSTR": "STR +{1}", "SC_INCAGI": "AGI +{1}",
      "SC_INCDEX": "DEX +{1}", "SC_INCINT": "INT +{1}", "SC_INCLUK": "LUK +{1}", "SC_INCCRI": "CRIT +{1}",
      "SC_INCFLEE2": "Perfect Dodge +{1}", "SC_INCALLSTATUS": "All stats +{1}", "SC_INCHEALRATE": "Healing +{1}%",
      "SC_EXPBOOST": "Base EXP +{1}% from monsters", "SC_JEXPBOOST": "Job EXP +{1}% from monsters",
      "SC_ITEMBOOST": "Item drop rate +{1}%", "SC_SPEEDUP0": "Movement speed up", "SC_SPEEDUP1": "Movement speed up",
      "SC_ASPDPOTION0": "Attack speed up (Concentration Potion)",
      "SC_ASPDPOTION1": "Attack speed up (Awakening Potion)", "SC_ASPDPOTION2": "Attack speed up (Berserk Potion)",
      "SC_ASPDPOTION3": "Attack speed up", "SC_DEF_RATE": "DEF +{1}%", "SC_MDEF_RATE": "MDEF +{1}%",
      "SC_INCREASE_MAXSP": "Max SP +{1}%", "SC_INCREASEAGI": "Increase AGI", "SC_BLESSING": "Blessing",
      "SC_ASSUMPTIO": "Assumptio", "SC_ANGELUS": "Angelus", "SC_LIFEINSURANCE": "No EXP loss on death",
      "SC_S_LIFEPOTION": "Recover HP over time", "SC_M_LIFEPOTION": "Recover HP over time",
      "SC_L_LIFEPOTION": "Recover HP over time", "SC_S_MANAPOTION": "Recover SP over time",
      "SC_SPIRIT": "Soul Link", "SC_HIDING": "Hiding", "SC_CLOAKING": "Cloaking", "SC_SIGHT": "Sight",
      "SC_SPCOST_RATE": "SP cost -{1}%", "SC_ITEMSCRIPT": "Special effect",
      "SC_BOSSMAPINFO": "Shows where the boss of the map is", "SC_CHANGEUNDEAD": "Undead armor element",
      "SC_ELEMENTALCHANGE": "Changes your armor element"}
JOBNAME_FIX = {"Arch Bishop": "Archbishop"}
ATF_TRIGGER = [("ATF_SHORT", "melee"), ("ATF_LONG", "ranged"), ("ATF_WEAPON", "physical"), ("ATF_MAGIC", "magic"),
               ("ATF_MISC", "misc"), ("ATF_SKILL", "skill")]
BF = [("BF_SHORT", "melee"), ("BF_LONG", "ranged"), ("BF_WEAPON", "physical"), ("BF_MAGIC", "magic"),
      ("BF_MISC", "misc"), ("BF_NORMAL", "normal"), ("BF_SKILL", "skill")]
FUNCS = {"F_CashCity": "Teleports you to a town of your choice", "F_CashTele": "Teleports you to a place of your choice",
         "F_CashStore": "Opens a storage window", "F_CashReset": "Resets your stats and skills",
         "F_CashReduceStat": "Lets you lower a stat and get the points back",
         "F_CashReduceTraitStat": "Lets you lower a trait stat and get the points back",
         "F_CashPartyCall": "Calls your party members to you", "F_CashDungeon": "Teleports you to a dungeon of your choice",
         "F_CashSiegeTele": "Teleports you to a War of Emperium castle", "F_CashSiegeTele2": "Teleports you to a War of Emperium castle",
         "F_Rand": "Gives one random item", "bulba": "Summons this Pokémon as your companion"}
IGNORE = {"specialeffect", "specialeffect2", "hateffect", "showscript", "setfont", "skilleffect", "dispbottom",
          "playbgm", "end", "close", "misceffect", "emotion", "soundeffect", "soundeffectall", "message", "mes",
          "next", "close2", "announce", "sleep", "sleep2"}


def _race(c):
    return RACE.get(c, _words(c.replace("RC_", ""))) + ("" if c in RACE_SUFFIX else " monsters")


def _ele(c):
    return "every element" if c == "Ele_All" else ELE.get(c, _words(c.replace("Ele_", ""))) + " element"


def _size(c):
    return "every size" if c == "Size_All" else SIZE.get(c, _words(c.replace("Size_", ""))) + " size"


def _cls(c):
    return CLASS.get(c, _words(c.replace("Class_", "")))


def _race2(c):
    return _words(c.replace("RC2_", "")) + " monsters"


def _eff(c):
    return EFF.get(c, _words(c.replace("Eff_", "")))


def _job(c):
    w = _words(re.sub(r"^(Job|EAJ)_", "", c)).title()
    return JOBNAME_FIX.get(w, w)


def _flags(node, table, default):
    names = _names(node)
    out = [t for k, t in table if k in names]
    return out or [default]


def _names(node):
    if node is None:
        return set()
    if node[0] == "id":
        return {node[1]}
    if node[0] == "bin":
        return _names(node[2]) | _names(node[3])
    return set()


# ---------------------------------------------------------------- parsing

_TOK = re.compile(r"""
    (?P<ws>\s+|//[^\n]*|/\*.*?\*/)
  | (?P<str>"(?:\\.|[^"\\])*")
  | (?P<num>0x[0-9a-fA-F]+|\d+)
  | (?P<id>[.'$@]*[A-Za-z_]\w*\$?)
  | (?P<op>>>=|<<=|\+\+|--|&&|\|\||==|!=|>=|<=|<<|>>|\+=|-=|\*=|/=|%=|&=|\|=|[-+*/%<>=!~&|^?:;,(){}\[\]])
""", re.S | re.X)


class Bad(Exception):
    pass


def _lex(s):
    out, i = [], 0
    while i < len(s):
        m = _TOK.match(s, i)
        if not m:
            raise Bad("lex")
        if m.lastgroup != "ws":
            v = m.group()
            if m.lastgroup == "str":
                v = re.sub(r"\\(.)", r"\1", v[1:-1])
            elif m.lastgroup == "num":
                v = int(v, 0)
            out.append((m.lastgroup, v, m.start(), m.end()))
        i = m.end()
    out.append(("eof", None, len(s), len(s)))
    return out


_BIN = [["||"], ["&&"], ["|"], ["^"], ["&"], ["==", "!="], ["<", "<=", ">", ">="], ["<<", ">>"], ["+", "-"],
        ["*", "/", "%"]]
_ASSIGN = {"=", "+=", "-=", "*=", "/=", "%=", "&=", "|=", "<<=", ">>="}


class _P:
    def __init__(self, src):
        self.src = src
        self.t = _lex(src)
        self.i = 0

    def peek(self, k=0):
        return self.t[min(self.i + k, len(self.t) - 1)]

    def is_(self, v, k=0):
        tok = self.peek(k)
        return tok[0] in ("op", "id") and tok[1] == v

    def take(self, v=None):
        tok = self.peek()
        if v is not None and not self.is_(v):
            raise Bad("expected %s got %r" % (v, tok[1]))
        if tok[0] == "eof":
            raise Bad("eof")
        self.i += 1
        return tok

    # statements
    def block(self, end="eof"):
        out = []
        while not (self.peek()[0] == "eof" if end == "eof" else self.is_("}")):
            if self.peek()[0] == "eof":
                raise Bad("unclosed")
            out.append(self.stmt())
        return out

    def stmt(self):
        start = self.peek()[2]
        tok = self.peek()
        if self.is_(";"):
            self.take()
            return ("nop",)
        if self.is_("{"):
            self.take()
            b = self.block("}")
            self.take("}")
            return ("block", b)
        if tok[0] == "id" and tok[1] == "if" and self.is_("(", 1):
            self.take()
            self.take("(")
            c = self.expr()
            self.take(")")
            a = self.stmt()
            b = None
            if self.is_("else"):
                self.take()
                b = self.stmt()
            return ("if", c, a, b, start)
        if tok[0] == "id" and tok[1] in ("for", "while", "switch") and self.is_("(", 1):
            self.take()
            self._skip_parens()
            self.stmt()
            return ("code", self.src[start:self.t[self.i - 1][3]])
        if tok[0] == "id" and tok[1] in ("case", "default", "break", "return", "goto", "do", "function"):
            while not self.is_(";") and not self.is_("}") and self.peek()[0] != "eof":
                self.take()
            if self.is_(";"):
                self.take()
            return ("code", self.src[start:self.t[self.i - 1][3]])
        if tok[0] != "id":
            raise Bad("statement starts with %r" % (tok[1],))
        # assignment
        j = 1
        if self.is_("[", 1):
            depth, j = 0, 1
            while True:
                if self.is_("[", j):
                    depth += 1
                elif self.is_("]", j):
                    depth -= 1
                    if depth == 0:
                        j += 1
                        break
                elif self.peek(j)[0] == "eof":
                    raise Bad("eof")
                j += 1
        nxt = self.peek(j)
        if nxt[0] == "op" and (nxt[1] in _ASSIGN or nxt[1] in ("++", "--")):
            name = self.take()[1]
            if j > 1:
                while self.i < self.i + j - 1 and not self.is_(nxt[1]):
                    self.take()
                name += "[]"
            op = self.take()[1]
            if op in ("++", "--"):
                val = ("bin", op[0], ("id", name), ("num", 1))
            elif op == "=":
                val = self.expr()
            else:
                val = ("bin", op[:-1], ("id", name), self.expr())
            self._end()
            return ("set", name, val, self.src[start:self.t[self.i - 1][3]])
        name = self.take()[1]
        if name == "set" and not self.is_("("):
            var = self.take()[1]
            self.take(",")
            val = self.expr()
            self._end()
            return ("set", var, val, self.src[start:self.t[self.i - 1][3]])
        args = []
        if self.is_("("):
            save = self.i
            try:
                self.take("(")
                args = self._args(")")
                self.take(")")
                if not (self.is_(";") or self.is_("}") or self.peek()[0] == "eof"):
                    raise Bad("not a call")
            except Bad:
                self.i = save
                args = self._args(";")
        elif not self.is_(";"):
            args = self._args(";")
        self._end()
        return ("cmd", name, args, self.src[start:self.t[self.i - 1][3]])

    def _end(self):
        if self.is_(";"):
            self.take()
        elif not (self.is_("}") or self.peek()[0] == "eof"):
            raise Bad("missing ;")

    def _skip_parens(self):
        self.take("(")
        depth = 1
        while depth:
            tok = self.take()
            if tok[0] == "op" and tok[1] == "(":
                depth += 1
            elif tok[0] == "op" and tok[1] == ")":
                depth -= 1

    def _args(self, end):
        out = []
        if self.is_(end):
            return out
        out.append(self.expr())
        while self.is_(","):
            self.take()
            out.append(self.expr())
        return out

    # expressions
    def expr(self):
        c = self.binary(0)
        if self.is_("?"):
            self.take()
            a = self.expr()
            self.take(":")
            b = self.expr()
            return ("tern", c, a, b)
        return c

    def binary(self, level):
        if level == len(_BIN):
            return self.unary()
        a = self.binary(level + 1)
        while self.peek()[0] == "op" and self.peek()[1] in _BIN[level]:
            op = self.take()[1]
            a = ("bin", op, a, self.binary(level + 1))
        return a

    def unary(self):
        if self.peek()[0] == "op" and self.peek()[1] in ("-", "!", "~", "+"):
            op = self.take()[1]
            v = self.unary()
            if op == "+":
                return v
            if op == "-" and v[0] == "num":
                return ("num", -v[1])
            return ("un", op, v)
        return self.atom()

    def atom(self):
        tok = self.take()
        if tok[0] == "num":
            return ("num", tok[1])
        if tok[0] == "str":
            return ("str", tok[1])
        if tok[0] == "op" and tok[1] == "(":
            e = self.expr()
            self.take(")")
            return e
        if tok[0] == "id":
            if self.is_("("):
                self.take()
                args = self._args(")")
                self.take(")")
                return ("call", tok[1], args)
            if self.is_("["):
                self.take()
                idx = self.expr()
                self.take("]")
                return ("id", tok[1] + "[]")
            return ("id", tok[1])
        raise Bad("unexpected %r" % (tok[1],))


# ---------------------------------------------------------------- values

def _fnum(x):
    if isinstance(x, float):
        x = round(x, 3)
        if x == int(x):
            x = int(x)
    return "{:,}".format(x) if isinstance(x, int) and abs(x) >= 10000 else str(x)


class Ctx:
    def __init__(self):
        self.env = {}
        self.dynamic = set()  # loop variables: their value can't be followed
        self.guard = []  # [(condition, True/False), ...] of the if-branches being read

    def sub(self, n):
        """n with known variables replaced by what they hold."""
        k = n[0]
        if k == "id" and n[1] in self.env and n[1] not in self.dynamic:
            return self.env[n[1]]
        if k == "bin":
            return ("bin", n[1], self.sub(n[2]), self.sub(n[3]))
        if k == "un":
            return ("un", n[1], self.sub(n[2]))
        if k == "call":
            return ("call", n[1], [self.sub(a) for a in n[2]])
        if k == "tern":
            return ("tern", self.sub(n[1]), self.sub(n[2]), self.sub(n[3]))
        return n


def _factor(n):
    """(singular, plural) unit for a value that changes per player, or None."""
    k = n[0]
    if k == "call":
        f, a = n[1], n[2]
        if f == "getrefine":
            return ("refine level", "refine levels")
        if f == "getequiprefinerycnt" and a and a[0][0] == "id":
            s = SLOT.get(a[0][1], "item")
            return ("refine level of the " + s, "refine levels of the " + s)
        if f == "getenchantgrade":
            return ("grade", "grades")
        if f == "readparam" and a and a[0][0] == "id" and a[0][1] in STAT:
            s = "base " + STAT[a[0][1]]
            return (s, s)
        if f == "getskilllv" and a:
            s = _skill(a[0])
            return ("learned level of " + s, "learned levels of " + s)
        if f in ("getequipweaponlv",):
            return ("weapon level", "weapon levels")
        if f == "min" and len(a) == 2:
            for x, y in ((a[0], a[1]), (a[1], a[0])):
                fx, cy = _factor(x), _lin(y)
                if fx and cy and list(cy) == [None]:
                    cap = cy[None]
                    cap = ("+%d" if fx[0].startswith("refine") else "%s") % cap
                    return (fx[0] + " (up to %s)" % cap, fx[1] + " (up to %s)" % cap)
            return None
        return None
    if k == "id":
        if n[1] == "BaseLevel":
            return ("base level", "base levels")
        if n[1] == "JobLevel":
            return ("job level", "job levels")
        if n[1] in STAT:
            s = "base " + STAT[n[1]]
            return (s, s)
    return None


def _key(n):
    return repr(n)


def _lin(n):
    """{None: constant, (factor key, divisor): coefficient} for constant or linear values, else None.
    Divisions round down like the server does."""
    k = n[0]
    if k == "num":
        return {None: n[1]}
    if k == "id" and n[1] in GRADES:
        return {None: GRADES[n[1]]}
    f = _factor(n)
    if f:
        return {(_key(n), 1, f, 0): 1}
    if k == "call" and n[1] == "max" and len(n[2]) == 2:  # max(0, x): "above" wording already means none below
        for x, y in ((n[2][0], n[2][1]), (n[2][1], n[2][0])):
            if x == ("num", 0):
                return _lin(y)
    if k == "un" and n[1] == "-":
        v = _lin(n[2])
        return {a: -b for a, b in v.items()} if v else None
    if k == "bin":
        a, b = _lin(n[2]), _lin(n[3])
        if a is None or b is None:
            return None
        op = n[1]
        if op in "+-":
            out = dict(a)
            for kk, vv in b.items():
                out[kk] = out.get(kk, 0) + (vv if op == "+" else -vv)
            return {kk: vv for kk, vv in out.items() if vv or kk is None}
        ca, cb = list(a) == [None], list(b) == [None]
        if op == "*":
            if ca:
                return {kk: vv * a[None] for kk, vv in b.items()}
            if cb:
                return {kk: vv * b[None] for kk, vv in a.items()}
            return None
        if op in "/%" and cb and b[None]:
            if ca:
                x, y = a[None], b[None]
                return {None: int(x / y) if op == "/" else x - int(x / y) * y}
            terms = [kk for kk in a if kk is not None]
            if op == "/" and len(terms) >= 2 and b[None] > 0 and all(
                    a[t] == 1 and t[1] == 1 and t[3] == 0 for t in terms):
                # (refine A + refine B) / 3: one combined value
                key, f = _combined(terms)
                return {(key, b[None], f, -a.get(None, 0)): 1}
            if op == "/" and len(terms) == 1 and a[terms[0]] == 1 and b[None] > 0:
                key, div, f, off = terms[0]
                c = a.get(None, 0)
                if div == 1:  # (X + c) / d
                    return {(key, b[None], f, -c): 1}
                if c == 0:
                    return {(key, div * b[None], f, off): 1}
            if op == "/" and all(kk is None or a[kk] % b[None] == 0 for kk in a) and a.get(None, 0) % b[None] == 0:
                return {kk: vv // b[None] for kk, vv in a.items()}
        return None
    return None


def _combined(terms):
    """(key, names) for a sum of per-player values, like the refine of two pieces of gear."""
    names = [t[2][0] for t in terms]
    if all(x.startswith("refine level of the ") for x in names):
        parts = _and([x[len("refine level of the "):] for x in names])
        f = ("total refine level of the " + parts, "total refine levels of the " + parts)
    elif all(x.startswith("base ") for x in names):
        f = ("base " + " + ".join(x[5:] for x in names),) * 2
    else:
        f = (" + ".join(names),) * 2
    return "+".join(t[0] for t in terms), f


def _text(n):
    """Readable form of any expression (fallback)."""
    k = n[0]
    if k == "num":
        return _fnum(n[1])
    if k == "str":
        return n[1]
    if k == "id":
        return {"BaseLevel": "base level", "JobLevel": "job level"}.get(n[1], n[1])
    if k == "un":
        return ("not " if n[1] == "!" else n[1]) + _text(n[2])
    if k == "bin":
        op = {"*": "×", "/": "÷", "&&": "and", "||": "or"}.get(n[1], n[1])
        return "(%s %s %s)" % (_text(n[2]), op, _text(n[3]))
    if k == "tern":
        return "(%s if %s, else %s)" % (_text(n[2]), _text(n[1]), _text(n[3]))
    if k == "call":
        f = _factor(n)
        if f:
            return f[0]
        if n[1] == "rand" and len(n[2]) == 2:
            return "%s to %s" % (_text(n[2][0]), _text(n[2][1]))
        if n[1] == "pow" and len(n[2]) == 2 and n[2][1] in (("num", 2), ("num", 3)):
            return "%s%s" % (_text(n[2][0]) if n[2][0][0] == "bin" else "(%s)" % _text(n[2][0]), "²" if n[2][1][1] == 2 else "³")
        if n[1] in ("min", "max") and len(n[2]) == 2 and n[2][1][0] == "num":
            return "%s (%s %s)" % (_text(n[2][0]), "at most" if n[1] == "min" else "at least", _text(n[2][1]))
        if n[1] in ("min", "max") and len(n[2]) == 2:
            return "%s(%s, %s)" % ("lowest of" if n[1] == "min" else "highest of", _text(n[2][0]), _text(n[2][1]))
        if n[1] == "rand" and len(n[2]) == 1:
            return "0 to %s" % _text(("bin", "-", n[2][0], ("num", 1)))
        return "%s(%s)" % (n[1], ", ".join(_text(a) for a in n[2]))
    return "?"


def _plain(n, ctx):
    """Unsigned amount with no unit, e.g. a skill level."""
    return _cased(ctx.sub(n), ctx, _plain1)


def _plain1(n):
    v = _lin(n)
    if v and list(v) == [None]:
        return _fnum(v[None])
    if n[0] == "call" and n[1] == "rand" and all(a[0] == "num" for a in n[2]) and len(n[2]) == 2:
        return "%s to %s" % (_fnum(n[2][0][1]), _fnum(n[2][1][1]))
    if v:
        return _amount1(n, sign=False)
    return _text(n)


def _amount(n, ctx, unit="", scale=1, sign=True, neg=False):
    """'+20%', '+20 for every 2 refine levels', '-1.5 sec' ..."""
    lo = 0
    st = _state(ctx.guard) if ctx.guard else None
    for names, a, b in (st[0].values() if st else []):
        if names[0].startswith("refine level") and a != -INF:
            lo = int(a)
    return _cased(ctx.sub(n), ctx, lambda x: _amount1(x, unit, scale, sign, neg, lo))


def _eval_refine(n, r):
    """Value of n at refine r, for expressions built only from getrefine() and numbers; None otherwise."""
    k = n[0]
    if k == "num":
        return n[1]
    if k == "call" and n[1] == "getrefine" and not n[2]:
        return r
    if k == "call" and n[1] in ("min", "max", "pow") and len(n[2]) == 2:
        a, b = _eval_refine(n[2][0], r), _eval_refine(n[2][1], r)
        if a is None or b is None:
            return None
        return min(a, b) if n[1] == "min" else max(a, b) if n[1] == "max" else a ** b
    if k == "un" and n[1] == "-":
        a = _eval_refine(n[2], r)
        return None if a is None else -a
    if k == "bin" and n[1] in "+-*/":
        a, b = _eval_refine(n[2], r), _eval_refine(n[3], r)
        if a is None or b is None or (n[1] == "/" and not b):
            return None
        return a + b if n[1] == "+" else a - b if n[1] == "-" else a * b if n[1] == "*" else int(a / b)
    return None


def _refine_table(n, one, lo):
    """'+9% at +6, +16% at +7, ... +121% at +14 or higher' for values that grow unevenly with refine."""
    vals = [(r, _eval_refine(n, r)) for r in range(lo, 21)]
    if any(v is None for _, v in vals):
        return None
    groups = []
    for r, v in vals:
        if groups and groups[-1][2] == v:
            groups[-1][1] = r
        else:
            groups.append([r, r, v])
    if len(groups) > 12:
        return None
    out = []
    for a, b, v in groups:
        if b == 20 and a != b:
            where = "+%d or higher" % a
        elif a == b:
            where = "+%d" % a
        else:
            where = "+%d to +%d" % (a, b)
        out.append("%s at %s" % (one(v), where))
    return ", ".join(out)


def _amount1(n, unit="", scale=1, sign=True, neg=False, lo=0):
    v = _lin(n)

    def one(x, sign=sign):
        x = x * scale
        if neg:
            x = -x
        s = _fnum(x)
        return ("+" + s if sign and x >= 0 else s) + unit

    if n[0] == "call" and n[1] == "rand" and len(n[2]) == 2 and all(a[0] == "num" for a in n[2]):
        return "%s to %s" % (one(n[2][0][1]), one(n[2][1][1], False))
    if v is None:
        t = _refine_table(n, one, lo)
        if t:
            return t
        t = _text(n)
        if not (t.startswith("(") and (t.endswith(")") or t.endswith("²"))):
            t = "(" + t + ")"
        return ("+" + t if sign else t) + unit if not neg else "-" + t + unit
    c = v.get(None, 0)
    terms = [(kk, vv) for kk, vv in v.items() if kk is not None]
    if len(terms) == 1 and c < 0 < terms[0][1] and terms[0][0][1] == 1 and -c % terms[0][1] == 0 \
            and terms[0][0][0] != "x":
        # 20*X - 100 reads better as "+20 per X above 5"
        (key, div, (sg, pl), off), coef = terms[0]
        k = -c // coef
        head, _, cap = sg.partition(" (")
        above = "+%d" % k if head.startswith("refine") else _fnum(k)
        return one(coef) + " per %s above %s" % (head, above) + (" (" + cap if cap else "")
    parts = []
    if c or not terms:
        parts.append(one(c))
    for (key, div, (sg, pl), off), coef in terms:
        each = " per " + sg if div == 1 else " for every %s %s" % (_fnum(div), pl)
        if off:
            head, _, cap = each.partition(" (")
            at = off if off > 0 else off + div
            num = ("+%d" if sg.startswith("refine") else "%s") % at
            each = head + (" above " if off > 0 else ", starting at ") + num + (" (" + cap if cap else "")
        if parts:
            parts.append(("minus " if coef * (-1 if neg else 1) < 0 else "plus ") + one(abs(coef) * (-1 if neg else 1), False) + each)
        else:
            parts.append(one(coef) + each)
    return ", ".join(parts)


# A value that changes inside if-branches is held as ("tern", condition, value if true, value if false). _cased
# splits such a value into its possible results and names the refine/level range each one applies to.

GRADES = {"ENCHANTGRADE_NONE": 0, "ENCHANTGRADE_D": 1, "ENCHANTGRADE_C": 2, "ENCHANTGRADE_B": 3,
          "ENCHANTGRADE_A": 4}
INF = float("inf")


def _all(guard):
    out = None
    for c, b in guard:
        x = c if b else ("un", "!", c)
        out = x if out is None else ("bin", "&&", out, x)
    return out


def _has_tern(n):
    if not isinstance(n, tuple):
        return False
    if n[0] == "tern":
        return True
    if n[0] == "call":
        return any(_has_tern(a) for a in n[2])
    return any(_has_tern(x) for x in n[1:] if isinstance(x, tuple))


def _split(c, b):
    """Constraints saying condition c is b."""
    if c[0] == "un" and c[1] == "!":
        return _split(c[2], not b)
    if b and c[0] == "bin" and c[1] == "&&":
        return _split(c[2], True) + _split(c[3], True)
    return [(c, b)]


def _numcmp(c):
    """(factor key, factor names, op, number) when c compares a per-player value with a number."""
    if c[0] != "bin" or c[1] not in _CMP:
        return None
    for op, x, y in ((c[1], c[2], c[3]), (_FLIP[c[1]], c[3], c[2])):
        lx, ly = _lin(x), _lin(y)
        if lx and ly and list(ly) == [None] and len(lx) >= 2 and None not in lx and op != "!=" and all(
                v == 1 and t[1] == 1 and t[3] == 0 for t, v in lx.items()):
            key, names = _combined(list(lx))
            return key, names, op, ly[None]
        if lx and ly and list(ly) == [None] and len(lx) == 1 and None not in lx:
            (key, div, names, off), coef = next(iter(lx.items()))
            if coef == 1 and div == 1 and op != "!=":
                return key, names, op, ly[None]
    return None


def _interval(op, k, b):
    lo, hi = {">=": (k, INF), ">": (k + 1, INF), "<=": (-INF, k), "<": (-INF, k - 1), "==": (k, k)}[op]
    if b:
        return [(lo, hi)]
    out = []
    if lo != -INF:
        out.append((-INF, lo - 1))
    if hi != INF:
        out.append((hi + 1, INF))
    return out


def _state(cons):
    """({factor key: (names, lo, hi)}, {other condition: truth}) or None when the constraints contradict."""
    rng, other = {}, {}
    for c, b in cons:
        m = _numcmp(c)
        if m:
            key, names, op, k = m
            opts = _interval(op, k, b)
            if len(opts) != 1:  # "not exactly k": too fine to track
                continue
            _, lo, hi = rng.get(key, (names, -INF, INF))
            lo, hi = max(lo, opts[0][0]), min(hi, opts[0][1])
            if lo > hi:
                return None
            rng[key] = (names, lo, hi)
        else:
            r = repr(c)
            if other.get(r, b) != b:
                return None
            other[r] = b
    return rng, other


def _cases(n, cons, limit):
    """[(constraints, value without ternaries), ...]"""
    if len(limit) > 24:
        raise Bad("too many cases")
    k = n[0]
    if k == "tern":
        out = []
        for b in (True, False):
            nc = _assume(cons, n[1], b)
            if nc is not None and _state(nc) is not None:
                out += _cases(n[2] if b else n[3], nc, limit)
        limit.extend(out)
        return out
    if k in ("bin", "un", "call"):
        kids = list(n[2:]) if k == "bin" else [n[2]] if k == "un" else list(n[2])
        acc = [(cons, [])]
        for kid in kids:
            acc = [(c2, vals + [v]) for c1, vals in acc for c2, v in _cases(kid, c1, limit)]
        if k == "bin":
            return [(c, ("bin", n[1], v[0], v[1])) for c, v in acc]
        if k == "un":
            return [(c, ("un", n[1], v[0])) for c, v in acc]
        return [(c, ("call", n[1], v)) for c, v in acc]
    return [(cons, n)]


def _conj(c):
    if c[0] == "bin" and c[1] == "&&":
        return _conj(c[2]) + _conj(c[3])
    return [c]


def _implied(c, st, want=True):
    """True when the state already makes condition c come out as `want`."""
    while c[0] == "un" and c[1] == "!":
        c, want = c[2], not want
    m = _numcmp(c)
    if m:
        key, names, op, k = m
        if key not in st[0]:
            return False
        opts = _interval(op, k, want)
        return any(st[0][key][1] >= lo and st[0][key][2] <= hi for lo, hi in opts)
    return st[1].get(repr(c)) is want


def _assume(cons, c, b):
    """cons plus 'c is b', or None when that can't happen."""
    while c[0] == "un" and c[1] == "!":
        c, b = c[2], not b
    if b or c[0] != "bin" or c[1] != "&&":
        return cons + _split(c, b)
    st = _state(cons)
    if st is None:
        return None
    if any(_implied(x, st, False) for x in _conj(c)):
        return cons
    left = [x for x in _conj(c) if not _implied(x, st)]
    if not left:
        return None
    if len(left) == 1:
        return _assume(cons, left[0], False)
    out = left[0]
    for x in left[1:]:
        out = ("bin", "&&", out, x)
    return cons + [(out, False)]


def _range_text(names, lo, hi):
    head, _, _ = names[0].partition(" (")
    if head.startswith("refine level"):
        label, f = "refine" + head[len("refine level"):], lambda x: "+%d" % x
    elif head.startswith("total refine level"):
        label, f = "total refine" + head[len("total refine level"):], lambda x: "+%d" % x
    elif head == "grade":
        label, f = "grade", lambda x: "ABCD-"[::-1][int(x)] if 0 <= x <= 4 else str(x)
    else:
        label, f = head, lambda x: _fnum(int(x))
    if lo == hi:
        return "%s %s" % (label, f(lo))
    if hi == INF:
        return "%s %s or higher" % (label, f(lo))
    if lo == -INF:
        return "%s %s or lower" % (label, f(hi))
    return "%s %s to %s" % (label, f(lo), f(hi))


def _case_text(cons, base):
    st = _state(cons)
    extra = cons[base:]
    keys, words = [], []
    for i, (c, b) in enumerate(extra):
        m = _numcmp(c)
        if m and m[0] not in keys:
            keys.append(m[0])
        elif not m:
            rest = _state(cons[:base + i] + cons[base + i + 1:])
            if rest and (_implied(c, rest, b) or not b and any(_implied(x, rest, False) for x in _conj(c))):
                continue
            t = _lower(_cond(c, Ctx()))
            words.append(t if b else "not " + t)
    rng = st[0] if st else {}
    out = [_range_text(*rng[k]) for k in keys if k in rng] + words
    return " and ".join(dict.fromkeys(out))


def _cased(n, ctx, fmt):
    if not _has_tern(n):
        return fmt(n)
    try:
        cases = _cases(n, list(ctx.guard), [])
    except Bad:
        return fmt(n)
    texts = [(c, fmt(v)) for c, v in cases]
    if len({t for _, t in texts}) == 1:
        return texts[0][1]
    g = len(ctx.guard)
    base = [t for c, t in texts if all(not b for _, b in c[g:])]
    rest = [(c, t) for c, t in texts if not all(not b for _, b in c[g:])]
    parts = ["at %s: %s" % (_case_text(c, g), t) for c, t in rest]
    if base:
        return base[0] + "; " + "; ".join(parts)
    return "; ".join(parts)


def _const(n, ctx):
    n = ctx.sub(n)
    v = _lin(n)
    return v[None] if v and list(v) == [None] else None


# ---------------------------------------------------------------- links

def _clean(s):
    return str(s).replace("⟦", "[").replace("⟧", "]").replace("|", "/")


def _item(n, ctx=None):
    items, by_aegis, *_ = _db()
    if ctx:
        n = ctx.sub(n)
    if n[0] == "call" and n[1] == "callfunc" and n[2] and n[2][0] == ("str", "F_Rand"):
        return "one of " + _or([_item(x) for x in n[2][1:]])
    iid = n[1] if n[0] == "num" else by_aegis.get(n[1]) if n[0] in ("str", "id") else None
    if iid in items:
        return "⟦i:%d|%s⟧" % (iid, _clean(items[iid].get("Name") or items[iid].get("AegisName")))
    return "item " + _text(n)


def _mob(n, ctx=None):
    mobs = _db()[2]
    if ctx:
        n = ctx.sub(n)
    if n[0] == "num" and n[1] in mobs:
        return "⟦m:%d|%s⟧" % (n[1], _clean(mobs[n[1]].get("Name") or mobs[n[1]].get("AegisName")))
    if n[0] in ("str", "id"):
        for k, m in mobs.items():
            if m.get("AegisName") == n[1]:
                return "⟦m:%d|%s⟧" % (k, _clean(m.get("Name")))
    return "monster " + _text(n)


def _skill(n, ctx=None):
    skills, sk_aegis = _db()[3], _db()[4]
    if ctx:
        n = ctx.sub(n)
    sid = n[1] if n[0] == "num" else sk_aegis.get(n[1]) if n[0] in ("str", "id") else None
    if sid in skills:
        return "⟦k:%s|%s⟧" % (_clean(skills[sid].get("Name")), _clean(skills[sid].get("Description") or skills[sid].get("Name")))
    return _words(str(n[1])) if n[0] in ("str", "id") else "skill " + _text(n)


def _group(n):
    name = n[1] if n[0] in ("id", "str") else str(n[1])
    return "the " + _words(re.sub(r"^IG_", "", str(name))) + " group"


def _ms(n, ctx):
    n = ctx.sub(n)
    v = _const(n, ctx)
    if v is None:
        return _amount(n, ctx, " ms", sign=False)
    return _duration(v)


def _duration(ms):
    s = ms / 1000
    for size, word in ((86400, "day"), (3600, "hour"), (60, "minute")):
        if s >= size and s % size == 0 or s >= size * 2:
            x = s / size
            return _fnum(round(x, 1)) + " " + word + ("" if x == 1 else "s")
    return _fnum(round(s, 2)) + " second" + ("" if s == 1 else "s")


def _p(n, ctx, div):
    """Chance written as n/div %."""
    return _amount(n, ctx, "%", 1 / div, sign=False)


# ---------------------------------------------------------------- bonuses

def _A(i):
    return lambda a, c: _amount(a[i], c)


def _AP(i):
    return lambda a, c: _amount(a[i], c, "%")


def _NEG(i, unit="%"):
    return lambda a, c: _amount(a[i], c, unit, neg=True)


def _SEC(i):
    return lambda a, c: _amount(a[i], c, " sec", 1 / 1000)


def _N(i):
    return lambda a, c: _plain(a[i], c)


def _LV(i):
    def f(a, c):
        v = _const(a[i], c)
        return "Lv %s" % _fnum(v) if v is not None else "at your " + _plain(a[i], c)
    return f


def _NP(i):
    return lambda a, c: _amount(a[i], c, "%", sign=False)


def _P100(i):
    return lambda a, c: _p(a[i], c, 100)


def _P10(i):
    return lambda a, c: _p(a[i], c, 10)


def _C(i, fn):
    return lambda a, c: fn(a[i][1]) if a[i][0] in ("id", "str") else _text(a[i])


def _SK(i):
    return lambda a, c: _skill(a[i], c)


def _I(i):
    return lambda a, c: _item(a[i], c)


def _M(i):
    return lambda a, c: _mob(a[i], c)


def _T(i):
    return lambda a, c: _ms(a[i], c)


def _ATF(i):
    def f(a, c):
        if len(a) <= i:
            return ""
        names = _names(a[i])
        who = " on yourself" if "ATF_SELF" in names else ""
        how = [t for k, t in ATF_TRIGGER if k in names]
        return who + (" with %s attacks" % " or ".join(how) if how else "")
    return f


def _BF(i):
    def f(a, c):
        if len(a) <= i:
            return ""
        how = [t for k, t in BF if k in _names(a[i])]
        return " (%s attacks)" % " or ".join(how) if how else ""
    return f


def _AUTO_TARGET(i):
    def f(a, c):
        v = _const(a[i], c) if len(a) > i else None
        if v is None:
            return ""
        return (" on yourself" if not v & 1 else "") + (" (random level)" if v & 2 else "")
    return f


_RACE, _ELE, _SIZE, _CLS, _EFF, _R2, _W = (lambda i: _C(i, _race)), (lambda i: _C(i, _ele)), \
    (lambda i: _C(i, _size)), (lambda i: _C(i, _cls)), (lambda i: _C(i, _eff)), (lambda i: _C(i, _race2)), \
    (lambda i: _C(i, lambda x: WEAPON.get(x, _words(x))))


def _ELEN(i, noun):
    def f(a, c):
        if a[i][0] != "id":
            return _text(a[i]) + " " + noun
        if a[i][1] == "Ele_All":
            return noun + " of every element"
        return _ele(a[i][1]) + " " + noun
    return f


def _SIZEN(i):
    def f(a, c):
        if a[i][0] != "id":
            return _text(a[i]) + " enemies"
        if a[i][1] == "Size_All":
            return "enemies of every size"
        return SIZE.get(a[i][1], _words(a[i][1])) + " enemies"
    return f


def _B(text, *args):
    return (text, args)


STAT1 = {"Str": "STR", "Agi": "AGI", "Vit": "VIT", "Int": "INT", "Dex": "DEX", "Luk": "LUK", "Pow": "POW",
         "Sta": "STA", "Wis": "WIS", "Spl": "SPL", "Con": "CON", "Crt": "CRT", "AllStats": "All stats",
         "Allstats": "All stats", "AgiVit": "AGI and VIT", "AgiDexStr": "STR, AGI and DEX", "IntVit": "INT and VIT",
         "AllTraitStats": "All trait stats", "MaxHP": "Max HP", "MaxSP": "Max SP", "MaxAP": "Max AP",
         "BaseAtk": "ATK", "Atk": "ATK", "Atk2": "ATK", "Matk": "MATK", "MAtk": "MATK", "Matk2": "MATK",
         "Def": "DEF", "Def2": "Soft DEF", "Mdef": "MDEF", "Mdef2": "Soft MDEF", "Hit": "HIT", "Critical": "CRIT",
         "Flee": "FLEE", "Flee2": "Perfect Dodge", "Aspd": "ASPD", "PAtk": "P.ATK", "Patk": "P.ATK",
         "SMatk": "S.MATK", "Res": "RES", "MRes": "MRES", "HPlus": "H.PLUS", "CRate": "C.RATE"}
RATE1 = {"MaxHPrate": "Max HP", "MaxSPrate": "Max SP", "MaxAPrate": "Max AP", "AtkRate": "ATK",
         "WeaponAtkRate": "Weapon ATK", "MatkRate": "MATK", "WeaponMatkRate": "Weapon MATK", "DefRate": "DEF",
         "Def2Rate": "Soft DEF", "MdefRate": "MDEF", "Mdef2Rate": "Soft MDEF", "HitRate": "HIT",
         "CriticalRate": "CRIT", "FleeRate": "FLEE", "Flee2Rate": "Perfect Dodge", "AspdRate": "ASPD",
         "PAtkRate": "P.ATK", "SMatkRate": "S.MATK", "ResRate": "RES", "MResRate": "MRES", "HPlusRate": "H.PLUS",
         "CRateRate": "C.RATE", "HPrecovRate": "Natural HP recovery", "HPRecovRate": "Natural HP recovery",
         "SPrecovRate": "Natural SP recovery", "UseSPrate": "SP cost", "ShortAtkRate": "Melee physical damage",
         "LongAtkRate": "Ranged physical damage", "CritAtkRate": "Critical damage",
         "HealPower": "Healing skill power", "HealPower2": "Healing received from skills",
         "Healpower2": "Healing received from skills", "AddItemHealRate": "HP recovered from healing items",
         "AddItemSPHealRate": "SP recovered from healing items", "Castrate": "Variable cast time",
         "VariableCastrate": "Variable cast time", "FixedCastrate": "Fixed cast time",
         "FixedCastRate": "Fixed cast time", "Delayrate": "After-cast delay", "DelayRate": "After-cast delay",
         "SpeedRate": "Movement speed", "SpeedAddRate": "Movement speed", "PerfectHitRate": "Perfect hit chance",
         "PerfectHitAddRate": "Perfect hit chance", "DoubleRate": "Double Attack chance",
         "DoubleAddRate": "Double Attack chance", "SkillRatio": "Skill damage",
         "NonCritAtkRate": "Non-critical damage"}
TAKEN1 = {"CritDefRate": "Critical damage taken", "CriticalDef": "Chance of being hit by a critical",
          "NearAtkDef": "Melee physical damage taken", "LongAtkDef": "Ranged physical damage taken",
          "MagicAtkDef": "Magic damage taken", "MiscAtkDef": "Trap and misc damage taken",
          "NoWeaponDamage": "Physical damage taken", "NoMiscDamage": "Misc damage taken",
          "ReduceDamageReturn": "Reflected damage taken", "Unbreakable": "Break chance of your equipment"}
FLAG1 = {"NoCastCancel": "Casting can't be interrupted (except in War of Emperium)",
         "NoCastCancel2": "Casting can't be interrupted", "NoSizeFix": "No size penalty on weapon damage",
         "NoKnockback": "Can't be knocked back", "NoGemStone": "Skills need no gemstones",
         "Intravision": "See hidden and cloaked enemies", "PerfectHide": "Stay hidden from monsters that detect",
         "RestartFullRecover": "Revive with full HP and SP", "NoMadoFuel": "Mado Gear skills need no fuel",
         "NoWalkDelay": "No flinching when hit (permanent Endure)",
         "UnbreakableWeapon": "Weapon can't be broken", "UnbreakableArmor": "Armor can't be broken",
         "UnbreakableHelm": "Headgear can't be broken", "UnbreakableShield": "Shield can't be broken",
         "UnbreakableShoes": "Shoes can't be broken", "UnbreakableGarment": "Garment can't be broken",
         "UnstripableWeapon": "Weapon can't be stripped", "UnstripableArmor": "Armor can't be stripped",
         "UnstripableHelm": "Headgear can't be stripped", "UnstripableShield": "Shield can't be stripped",
         "Unstripable": "Equipment can't be stripped"}

BONUS = {
    (1, "Unbreakable"): _B("Break chance of your equipment {0}", _NEG(0)),
    (1, "AtkRange"): _B("Attack range {0} cells", _A(0)),
    (1, "AddMaxWeight"): _B("Weight limit {0}", lambda a, c: _amount(a[0], c, "", 1 / 10)),
    (1, "CriticalLong"): _B("CRIT {0} on ranged normal attacks", _A(0)),
    (1, "FixedCast"): _B("Fixed cast time {0}", _SEC(0)),
    (1, "VariableCast"): _B("Variable cast time {0}", _SEC(0)),
    (1, "NoMagicDamage"): _B("Magic received {0} (healing and buffs too)", _NEG(0)),
    (1, "NoRegen"): _B("{0}", lambda a, c: {1: "No natural HP recovery", 2: "No natural SP recovery"}.get(
        _const(a[0], c), "No natural recovery")),
    (1, "AbsorbDmgMaxHP"): _B("Damage above {0} of Max HP in one hit is cut off", _N(0)),
    (1, "AbsorbDmgMaxHP2"): _B("A single hit can't deal more than {0} of your Max HP", _NP(0)),
    (1, "AtkEle"): _B("Attacks become {0}", _ELE(0)),
    (1, "DefEle"): _B("Armor becomes {0}", _ELE(0)),
    (1, "DefRatioAtkRace"): _B("More damage to {0} the higher their DEF", _RACE(0)),
    (1, "DefRatioAtkEle"): _B("More damage to {0} the higher their DEF", _ELEN(0, "enemies")),
    (1, "DefRatioAtkClass"): _B("More damage to {0} the higher their DEF", _CLS(0)),
    (1, "IgnoreDefEle"): _B("Ignore DEF of {0}", _ELEN(0, "enemies")),
    (1, "IgnoreDefRace"): _B("Ignore DEF of {0}", _RACE(0)),
    (1, "IgnoreDefClass"): _B("Ignore DEF of {0}", _CLS(0)),
    (1, "IgnoreMDefRace"): _B("Ignore MDEF of {0}", _RACE(0)),
    (1, "IgnoreMDefEle"): _B("Ignore MDEF of {0}", _ELEN(0, "enemies")),
    (1, "HPDrainValue"): _B("Recover {0} HP on each normal attack", _N(0)),
    (1, "SPDrainValue"): _B("Recover {0} SP on each normal attack", _N(0)),
    (1, "HPGainValue"): _B("Recover {0} HP when you kill with a melee physical attack", _N(0)),
    (1, "SPGainValue"): _B("Recover {0} SP when you kill with a melee physical attack", _N(0)),
    (1, "LongHPGainValue"): _B("Recover {0} HP when you kill with a ranged physical attack", _N(0)),
    (1, "LongSPGainValue"): _B("Recover {0} SP when you kill with a ranged physical attack", _N(0)),
    (1, "MagicHPGainValue"): _B("Recover {0} HP when you kill with magic", _N(0)),
    (1, "MagicSPGainValue"): _B("Recover {0} SP when you kill with magic", _N(0)),
    (1, "ShortWeaponDamageReturn"): _B("Reflect {0} of melee physical damage taken", _NP(0)),
    (1, "LongWeaponDamageReturn"): _B("Reflect {0} of ranged physical damage taken", _NP(0)),
    (1, "MagicDamageReturn"): _B("{0} chance to reflect targeted magic", _NP(0)),
    (1, "BreakWeaponRate"): _B("{0} chance to break the enemy's weapon when attacking", _P100(0)),
    (1, "BreakArmorRate"): _B("{0} chance to break the enemy's armor when attacking", _P100(0)),
    (1, "SplashRange"): _B("Normal attacks hit everything in a {0} area", lambda a, c: _splash(a[0], c)),
    (1, "SplashAddRange"): _B("Normal attacks hit everything in a {0} area", lambda a, c: _splash(a[0], c)),
    (1, "ClassChange"): _B("{0} chance to transform a monster with normal attacks", _P100(0)),
    (1, "AddStealRate"): _B("Steal success chance {0}", lambda a, c: _amount(a[0], c, "%", 1 / 100)),

    (2, "SkillAtk"): _B("{0} damage {1}", _SK(0), _AP(1)),
    (2, "CriticalAddRace"): _B("CRIT {1} against {0}", _RACE(0), _A(1)),
    (2, "HPRegenRate"): _B("Recover {0} HP every {1}", _N(0), _T(1)),
    (2, "SPRegenRate"): _B("Recover {0} SP every {1}", _N(0), _T(1)),
    (2, "HPLossRate"): _B("Lose {0} HP every {1}", _N(0), _T(1)),
    (2, "SPLossRate"): _B("Lose {0} SP every {1}", _N(0), _T(1)),
    (2, "RegenPercentHP"): _B("Recover {0} of Max HP every {1}", _NP(0), _T(1)),
    (2, "RegenPercentSP"): _B("Recover {0} of Max SP every {1}", _NP(0), _T(1)),
    (2, "SkillUseSP"): _B("{0} SP cost {1}", _SK(0), _NEG(1, "")),
    (2, "SkillUseSPrate"): _B("{0} SP cost {1}", _SK(0), _NEG(1)),
    (2, "WeaponAtk"): _B("ATK {1} with {0}", _W(0), _A(1)),
    (2, "WeaponDamageRate"): _B("Normal attack damage {1} with {0}", _W(0), _AP(1)),
    (2, "SkillHeal"): _B("{0} healing {1}", _SK(0), _AP(1)),
    (2, "SkillHeal2"): _B("Healing received from {0} {1}", _SK(0), _AP(1)),
    (2, "AddItemHealRate"): _B("HP recovered from {0} {1}", _I(0), _AP(1)),
    (2, "AddItemSPHealRate"): _B("SP recovered from {0} {1}", _I(0), _AP(1)),
    (2, "AddItemGroupHealRate"): _B("HP recovered from items in {0} {1}", lambda a, c: _group(a[0]), _AP(1)),
    (2, "AddItemGroupSPHealRate"): _B("SP recovered from items in {0} {1}", lambda a, c: _group(a[0]), _AP(1)),
    (2, "Castrate"): _B("{0} variable cast time {1}", _SK(0), _AP(1)),
    (2, "VariableCastrate"): _B("{0} variable cast time {1}", _SK(0), _AP(1)),
    (2, "FixedCastrate"): _B("{0} fixed cast time {1}", _SK(0), _AP(1)),
    (2, "SkillFixedCast"): _B("{0} fixed cast time {1}", _SK(0), _SEC(1)),
    (2, "SkillVariableCast"): _B("{0} variable cast time {1}", _SK(0), _SEC(1)),
    (2, "SkillDelay"): _B("{0} after-cast delay {1}", _SK(0), _SEC(1)),
    (2, "SkillCooldown"): _B("{0} cooldown {1}", _SK(0), _SEC(1)),
    (2, "AddEle"): _B("Physical damage against {0} {1}", _ELEN(0, "enemies"), _AP(1)),
    (2, "MagicAddEle"): _B("Magic damage against {0} {1}", _ELEN(0, "enemies"), _AP(1)),
    (2, "SubEle"): _B("Damage taken from {0} {1}", _ELEN(0, "attacks"), _NEG(1)),
    (2, "SubDefEle"): _B("Physical damage taken from {0} {1}", _ELEN(0, "enemies"), _NEG(1)),
    (2, "MagicSubDefEle"): _B("Magic damage taken from {0} {1}", _ELEN(0, "enemies"), _NEG(1)),
    (2, "MagicAtkEle"): _B("{0} magic damage {1}", lambda a, c: _magic_ele(a[0]), _AP(1)),
    (2, "AddRace"): _B("Physical damage against {0} {1}", _RACE(0), _AP(1)),
    (2, "MagicAddRace"): _B("Magic damage against {0} {1}", _RACE(0), _AP(1)),
    (2, "SubRace"): _B("Damage taken from {0} {1}", _RACE(0), _NEG(1)),
    (2, "AddClass"): _B("Physical damage against {0} {1}", _CLS(0), _AP(1)),
    (2, "MagicAddClass"): _B("Magic damage against {0} {1}", _CLS(0), _AP(1)),
    (2, "SubClass"): _B("Damage taken from {0} {1}", _CLS(0), _NEG(1)),
    (2, "AddSize"): _B("Physical damage against {0} {1}", _SIZEN(0), _AP(1)),
    (2, "MagicAddSize"): _B("Magic damage against {0} {1}", _SIZEN(0), _AP(1)),
    (2, "SubSize"): _B("Damage taken from {0} {1}", _SIZEN(0), _NEG(1)),
    (2, "WeaponSubSize"): _B("Physical damage taken from {0} {1}", _SIZEN(0), _NEG(1)),
    (2, "MagicSubSize"): _B("Magic damage taken from {0} {1}", _SIZEN(0), _NEG(1)),
    (2, "AddDamageClass"): _B("Physical damage against {0} {1}", _M(0), _AP(1)),
    (2, "AddMagicDamageClass"): _B("Magic damage against {0} {1}", _M(0), _AP(1)),
    (2, "AddDefMonster"): _B("Physical damage taken from {0} {1}", _M(0), _NEG(1)),
    (2, "AddMDefMonster"): _B("Magic damage taken from {0} {1}", _M(0), _NEG(1)),
    (2, "AddRace2"): _B("Damage against {0} {1}", _R2(0), _AP(1)),
    (2, "MagicAddRace2"): _B("Magic damage against {0} {1}", _R2(0), _AP(1)),
    (2, "SubRace2"): _B("Damage taken from {0} {1}", _R2(0), _NEG(1)),
    (2, "SubSkill"): _B("Damage taken from {0} {1}", _SK(0), _NEG(1)),
    (2, "IgnoreDefRaceRate"): _B("Ignore {1} DEF of {0}", _RACE(0), _NP(1)),
    (2, "IgnoreMdefRaceRate"): _B("Ignore {1} MDEF of {0}", _RACE(0), _NP(1)),
    (2, "IgnoreMDefRaceRate"): _B("Ignore {1} MDEF of {0}", _RACE(0), _NP(1)),
    (2, "IgnoreMdefRace2Rate"): _B("Ignore {1} MDEF of {0}", _R2(0), _NP(1)),
    (2, "IgnoreDefClassRate"): _B("Ignore {1} DEF of {0}", _CLS(0), _NP(1)),
    (2, "IgnoreMdefClassRate"): _B("Ignore {1} MDEF of {0}", _CLS(0), _NP(1)),
    (2, "IgnoreMDefClassRate"): _B("Ignore {1} MDEF of {0}", _CLS(0), _NP(1)),
    (2, "IgnoreResRaceRate"): _B("Ignore {1} RES of {0}", _RACE(0), _NP(1)),
    (2, "IgnoreMResRaceRate"): _B("Ignore {1} MRES of {0}", _RACE(0), _NP(1)),
    (2, "ExpAddRace"): _B("EXP from {0} {1}", _RACE(0), _AP(1)),
    (2, "ExpAddClass"): _B("EXP from {0} {1}", _CLS(0), _AP(1)),
    (2, "AddEff"): _B("{1} chance to inflict {0} when attacking", _EFF(0), _P100(1)),
    (2, "AddEff2"): _B("{1} chance to inflict {0} on yourself when attacking", _EFF(0), _P100(1)),
    (2, "AddEffWhenHit"): _B("{1} chance to inflict {0} on the attacker when hit", _EFF(0), _P100(1)),
    (2, "ResEff"): _B("Resistance to {0} {1}", _EFF(0), lambda a, c: _amount(a[1], c, "%", 1 / 100)),
    (2, "ComaClass"): _B("{1} chance to inflict Coma on {0}", _CLS(0), _P100(1)),
    (2, "ComaRace"): _B("{1} chance to inflict Coma on {0}", _RACE(0), _P100(1)),
    (2, "WeaponComaEle"): _B("{1} chance to inflict Coma on {0} with normal attacks", _ELEN(0, "enemies"), _P100(1)),
    (2, "WeaponComaClass"): _B("{1} chance to inflict Coma on {0} with normal attacks", _CLS(0), _P100(1)),
    (2, "WeaponComaRace"): _B("{1} chance to inflict Coma on {0} with normal attacks", _RACE(0), _P100(1)),
    (2, "HPDrainRate"): _B("{0} chance to absorb {1} of damage dealt as HP", _P10(0), _NP(1)),
    (2, "HpDrainRate"): _B("{0} chance to absorb {1} of damage dealt as HP", _P10(0), _NP(1)),
    (2, "SPDrainRate"): _B("{0} chance to absorb {1} of damage dealt as SP", _P10(0), _NP(1)),
    (2, "HPDrainValueRace"): _B("Recover {1} HP on each normal attack against {0}", _RACE(0), _N(1)),
    (2, "SPDrainValueRace"): _B("Recover {1} SP on each normal attack against {0}", _RACE(0), _N(1)),
    (2, "HpDrainValueClass"): _B("Recover {1} HP on each normal attack against {0}", _CLS(0), _N(1)),
    (2, "SpDrainValueClass"): _B("Recover {1} SP on each normal attack against {0}", _CLS(0), _N(1)),
    (2, "HPVanishRate"): _B("{0} chance to destroy {1} of the enemy's HP with normal attacks", _P10(0), _NP(1)),
    (2, "SPVanishRate"): _B("{0} chance to destroy {1} of the enemy's SP with normal attacks", _P10(0), _NP(1)),
    (2, "SPGainRace"): _B("Recover {1} SP when you kill {0} with a melee physical attack", _RACE(0), _N(1)),
    (2, "DropAddRace"): _B("Drop rate from {0} {1}", _RACE(0), _AP(1)),
    (2, "DropAddClass"): _B("Drop rate from {0} {1}", _CLS(0), _AP(1)),
    (2, "AddMonsterDropItem"): _B("{1} chance to get {0} when you kill a monster", _I(0), _P100(1)),
    (2, "AddMonsterDropItemGroup"): _B("{1} chance to get an item from {0} when you kill a monster",
                                       lambda a, c: _group(a[0]), _P100(1)),
    (2, "GetZenyNum"): _B("{1} chance to get 1 to {0} zeny when you kill a monster", _N(0), _NP(1)),
    (2, "AddGetZenyNum"): _B("{1} chance to get 1 to {0} zeny when you kill a monster", _N(0), _NP(1)),
    (2, "AddSkillBlow"): _B("{0} knocks the target back {1} cells", _SK(0), _N(1)),

    (3, "AddEle"): _B("Physical damage against {0} {1}{2}", _ELEN(0, "enemies"), _AP(1), _BF(2)),
    (3, "SubEle"): _B("Damage taken from {0} {1}{2}", _ELEN(0, "attacks"), _NEG(1), _BF(2)),
    (3, "SubRace"): _B("Damage taken from {0} {1}{2}", _RACE(0), _NEG(1), _BF(2)),
    (3, "AutoSpell"): _B("{2} chance to cast {0} {1} when attacking", _SK(0), _LV(1), _P10(2)),
    (3, "AutoSpellWhenHit"): _B("{2} chance to cast {0} {1} when hit", _SK(0), _LV(1), _P10(2)),
    (3, "AddMonsterDropItem"): _B("{2} chance to get {0} when you kill {1}", _I(0), _RACE(1), _P100(2)),
    (3, "AddMonsterIdDropItem"): _B("{2} chance to get {0} when you kill {1}", _I(0), _M(1), _P100(2)),
    (3, "AddClassDropItem"): _B("{2} chance to get {0} when you kill {1}", _I(0), _CLS(1), _P100(2)),
    (3, "AddMonsterDropItemGroup"): _B("{2} chance to get an item from {0} when you kill {1}",
                                       lambda a, c: _group(a[0]), _RACE(1), _P100(2)),
    (3, "AddClassDropItemGroup"): _B("{2} chance to get an item from {0} when you kill {1}",
                                     lambda a, c: _group(a[0]), _CLS(1), _P100(2)),
    (3, "AddEff"): _B("{1} chance to inflict {0}{2} when attacking", _EFF(0), _P100(1), _ATF(2)),
    (3, "AddEffWhenHit"): _B("{1} chance to inflict {0}{2} when hit", _EFF(0), _P100(1), _ATF(2)),
    (3, "AddEffOnSkill"): _B("{2} chance to inflict {1} when using {0}", _SK(0), _EFF(1), _P100(2)),
    (3, "HPVanishRaceRate"): _B("{1} chance to destroy {2} of the HP of {0} when attacking", _RACE(0), _P10(1), _NP(2)),
    (3, "SPVanishRaceRate"): _B("{1} chance to destroy {2} of the SP of {0} when attacking", _RACE(0), _P10(1), _NP(2)),
    (3, "HPVanishRate"): _B("{0} chance to destroy {1} of the enemy's HP when attacking{2}", _P10(0), _NP(1), _BF(2)),
    (3, "SPVanishRate"): _B("{0} chance to destroy {1} of the enemy's SP when attacking{2}", _P10(0), _NP(1), _BF(2)),
    (3, "StateNoRecoverRace"): _B("{1} chance to stop {0} from healing for {2} with normal attacks",
                                  _RACE(0), _P100(1), _T(2)),

    (4, "AutoSpell"): _B("{2} chance to cast {0} {1}{3} when attacking", _SK(0), _LV(1), _P10(2), _AUTO_TARGET(3)),
    (4, "AutoSpellWhenHit"): _B("{2} chance to cast {0} {1}{3} when hit", _SK(0), _LV(1), _P10(2), _AUTO_TARGET(3)),
    (4, "AutoSpellOnSkill"): _B("{3} chance to cast {1} {2} when using {0}", _SK(0), _SK(1), _LV(2), _P10(3)),
    (4, "AddEff"): _B("{1} chance to inflict {0} for {3}{2} when attacking", _EFF(0), _P100(1), _ATF(2), _T(3)),
    (4, "AddEffWhenHit"): _B("{1} chance to inflict {0} for {3}{2} when hit", _EFF(0), _P100(1), _ATF(2), _T(3)),
    (4, "AddEffOnSkill"): _B("{2} chance to inflict {1}{3} when using {0}", _SK(0), _EFF(1), _P100(2), _ATF(3)),
    (4, "SetDefRace"): _B("{1} chance to set the DEF of {0} to {3} for {2} with normal attacks",
                          _RACE(0), _P100(1), _T(2), _N(3)),
    (4, "SetMDefRace"): _B("{1} chance to set the MDEF of {0} to {3} for {2} with normal attacks",
                           _RACE(0), _P100(1), _T(2), _N(3)),

    (5, "AutoSpell"): _B("{2} chance to cast {0} {1}{4} when attacking{3}", _SK(0), _LV(1), _P10(2), _BF(3),
                         _AUTO_TARGET(4)),
    (5, "AutoSpellWhenHit"): _B("{2} chance to cast {0} {1}{4} when hit{3}", _SK(0), _LV(1), _P10(2), _BF(3),
                                _AUTO_TARGET(4)),
    (5, "AutoSpellOnSkill"): _B("{3} chance to cast {1} {2} when using {0}", _SK(0), _SK(1), _LV(2), _P10(3)),
    (5, "AddEffOnSkill"): _B("{2} chance to inflict {1} for {4}{3} when using {0}", _SK(0), _EFF(1), _P100(2),
                             _ATF(3), _T(4)),
}


def _splash(n, c):
    v = _const(n, c)
    if v is None:
        return _text(c.sub(n))
    side = 2 * v + 1
    return "%d×%d" % (side, side)


def _magic_ele(n):
    if n[0] != "id":
        return _text(n)
    return "All-element" if n[1] == "Ele_All" else ELE.get(n[1], _words(n[1]))


def _bonus(name, args, ctx):
    k = name[1:] if name.startswith("b") else name
    n = len(args)
    if n == 0 and k in FLAG1:
        return FLAG1[k]
    if n == 1 and (1, k) not in BONUS:
        if k in STAT1:
            return "%s %s" % (STAT1[k], _amount(args[0], ctx))
        if k in RATE1:
            return "%s %s" % (RATE1[k], _amount(args[0], ctx, "%"))
        if k in TAKEN1:
            return "%s %s" % (TAKEN1[k], _amount(args[0], ctx, "%", neg=True))
        if k in FLAG1:
            return FLAG1[k]
    spec = BONUS.get((n, k))
    if not spec:
        return None
    text, fns = spec
    vals = [f(args, ctx) for f in fns]
    for i, v in enumerate(vals):
        ph = "{%d}" % i
        tail = re.search(r"(\{\d\})*$", text).group()
        if (", " in v or re.search(r"\b(per|every)\b", v)) and ph not in tail:
            # a long value reads badly mid-sentence: "Ignore DEF of X: 10%, plus 2% per refine level"
            t = text.replace(ph + " ", "").replace(" " + ph, "").replace(ph, "")
            t = t.format(*vals)
            text = t[0].upper() + t[1:] + ": " + v
            break
    else:
        text = text.format(*vals)
    return text.replace("every 1 second", "every second")


# ---------------------------------------------------------------- conditions

_CMP = {">=": "{} or higher", ">": "above {}", "<=": "{} or lower", "<": "below {}", "==": "exactly {}",
        "!=": "not {}"}
_FLIP = {">=": "<=", ">": "<", "<=": ">=", "<": ">", "==": "==", "!=": "!="}


def _cond(n, ctx):
    n = ctx.sub(n)
    if _has_tern(n):
        try:
            texts = list(dict.fromkeys(_cond(v, Ctx()) for _, v in _cases(n, list(ctx.guard), [])))
        except Bad:
            texts = []
        if len(texts) == 1:
            return texts[0]
    k = n[0]
    if k == "bin" and n[1] == "||":
        parts = []

        def flat(x):
            if x[0] == "bin" and x[1] == "||":
                flat(x[2])
                flat(x[3])
            else:
                parts.append(_cond(x, ctx))
        flat(n)
        if all(p.startswith("With ") for p in parts):
            return "With " + _or([p[5:] for p in parts])
        if all(p.startswith("For ") for p in parts):
            return "For " + _or([p[4:] for p in parts])
        return _or([parts[0]] + [_lower(p) for p in parts[1:]])
    if k == "bin" and n[1] in ("&&", "||"):
        a, b = _cond(n[2], ctx), _cond(n[3], ctx)
        return "%s %s %s" % (a, "and" if n[1] == "&&" else "or", _lower(b))
    if k == "un" and n[1] == "!":
        inner = n[2]
        if inner[0] == "call" and inner[1] == "getskilllv":
            return "%s not learned" % _skill(inner[2][0])
        if inner[0] == "call" and inner[1] == "isequipped":
            return "Not worn together with " + _and([_item(a) for a in inner[2]])
        return "Not (%s)" % _lower(_cond(inner, ctx))
    if k == "bin" and n[1] in _CMP:
        m = _numcmp(n)
        if m and not (n[2][0] == "call" and n[2][1] in ("getskilllv", "getenchantgrade") or
                      n[3][0] == "call" and n[3][1] in ("getskilllv", "getenchantgrade")):
            key, names, op, num = m
            lo, hi = _interval(op, num, True)[0]
            t = _range_text(names, lo, hi)
            return t[0].upper() + t[1:]
        t = _compare(n[1], n[2], n[3])
        if t is None:
            t = _compare(_FLIP[n[1]], n[3], n[2])
        if t is not None:
            return t
    if k == "call":
        f, a = n[1], n[2]
        if f == "isequipped":
            return "Worn together with " + _and([_item(x) for x in a])
        if f == "getskilllv" and a:
            return "%s learned" % _skill(a[0])
        if f == "checkmadogear":
            return "While riding a Mado Gear"
        if f == "checkfalcon":
            return "With a falcon"
        if f == "checkriding" or f == "checkdragon" or f == "checkwug":
            return "While mounted"
        if f == "vip_status":
            return "For VIP players"
        if f == "getpetinfo":
            return "With a pet out"
    if k == "bin" and n[1] == "&":
        names = _names(n[3]) | _names(n[2])
        if any(x.startswith("EAJL_") for x in names):
            return "For " + _and([{"EAJL_THIRD": "3rd jobs", "EAJL_2": "2nd jobs", "EAJL_UPPER": "transcendent jobs",
                                    "EAJL_BABY": "baby jobs", "EAJL_2_1": "2-1 jobs", "EAJL_2_2": "2-2 jobs",
                                    "EAJL_FOURTH": "4th jobs"}.get(x, _words(x)) for x in sorted(names)
                                   if x.startswith("EAJL_")])
    return "If " + _text(n)


def _lower(s):
    return s[0].lower() + s[1:] if s and not s[:2].isupper() and not s.startswith("⟦") else s


def _or(xs):
    xs = list(dict.fromkeys(xs))
    return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " or " + xs[-1]


def _and(xs):
    xs = list(xs)
    return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " and " + xs[-1]


def _compare(op, left, right):
    """Text for `left op right` when left is something we can name; None otherwise."""
    rv = _lin(right)
    num = rv[None] if rv and list(rv) == [None] else None
    rname = right[1] if right[0] == "id" else None
    if left[0] == "call":
        f, a = left[1], left[2]
        if f in ("getrefine",) and num is not None:
            return "Refine " + _CMP[op].format("+%d" % num)
        if f == "getequiprefinerycnt" and num is not None and a and a[0][0] == "id":
            return "%s refined %s" % (SLOT.get(a[0][1], "Item").capitalize(), _CMP[op].format("+%d" % num))
        if f == "getenchantgrade" and (rname or num is not None):
            g = rname.replace("ENCHANTGRADE_", "") if rname else "ABCDE"[::-1][num - 1] if 1 <= (num or 0) <= 5 else str(num)
            g = {"NONE": "no grade"}.get(g, "grade " + g)
            return "Item " + _CMP[op].format(g).replace("exactly ", "")
        if f == "readparam" and a and a[0][0] == "id" and a[0][1] in STAT and num is not None:
            return "Base %s %s" % (STAT[a[0][1]], _CMP[op].format(num))
        if f == "getskilllv" and a and num is not None:
            if num == 0 and op == "==":
                return "%s not learned" % _skill(a[0])
            if num == 0 and op in (">", "!="):
                return "%s learned" % _skill(a[0])
            return "%s learned at level %s" % (_skill(a[0]), num if op == "==" else _CMP[op].format(num))
        if f == "getequipid" and a and a[0][0] == "id" and num is not None and op in ("==", "!="):
            return "%s %s in the %s" % ("With" if op == "==" else "Without", _item(("num", num)), SLOT.get(a[0][1], "slot"))
        if f == "getiteminfo" and len(a) == 2 and a[1] == ("id", "ITEMINFO_WEAPONLEVEL") and num is not None:
            return "Weapon level " + _CMP[op].format(num)
        if f == "getiteminfo" and len(a) == 2 and a[1] == ("id", "ITEMINFO_ARMORLEVEL") and num is not None:
            return "Armor level " + _CMP[op].format(num)
        if f == "getitempos" and rname and op == "==":
            return "When worn as the " + {"EQP_ACC_L": "left accessory", "EQP_ACC_R": "right accessory"}.get(
                rname, _words(rname.replace("EQP_", "")).lower())
        if f == "rand" and num is not None and len(a) in (1, 2) and all(x[0] == "num" for x in a):
            lo_, hi_ = (a[0][1], a[1][1]) if len(a) == 2 else (0, a[0][1] - 1)
            total = hi_ - lo_ + 1
            hits = {"==": 1, "<": num - lo_, "<=": num - lo_ + 1, ">": hi_ - num, ">=": hi_ - num + 1,
                    "!=": total - 1}[op]
            hits = max(0, min(total, hits))
            return "%d in %d chance" % (hits, total)
        if f == "getequipweaponlv" and num is not None:
            return "Weapon level " + _CMP[op].format(num)
        if f == "getiteminfo" and len(a) == 2 and a[1] in (("id", "ITEMINFO_VIEW"), ("id", "ITEMINFO_SUBTYPE"), ("num", 11)) \
                and rname in WEAPON and op in ("==", "!="):
            return ("With " if op == "==" else "Not with ") + WEAPON[rname]
        if f == "getpetinfo" and a and a[0][0] == "id":
            if a[0][1] == "PETINFO_EGGID" and num is not None:
                return "With the %s pet out" % _item(("num", num))
            if a[0][1] == "PETINFO_INTIMATE" and rname:
                return "Pet intimacy " + _CMP[op].format(_words(rname.replace("PET_INTIMATE_", "")).lower())
        if f == "strcharinfo" and right[0] == "str":
            return "On the map " + right[1] if op == "==" else "Not on the map " + right[1]
        if f == "getmapflag":
            return "On maps with " + _words(_text(a[1]) if len(a) > 1 else "a flag").lower()
        if f == "getequiparmorlv" and num is not None:
            return "Armor level " + _CMP[op].format(num)
    if left[0] == "id":
        v = left[1]
        if v in ("BaseLevel", "JobLevel") and num is not None:
            return "%s %s" % ("Base level" if v == "BaseLevel" else "Job level", _CMP[op].format(num))
        if v in STAT and num is not None:
            return "Base %s %s" % (STAT[v], _CMP[op].format(num))
        if v in ("BaseJob", "Class", "BaseClass") and rname and op in ("==", "!="):
            who = _job(rname) + (" classes" if v == "BaseClass" else "")
            return ("For " if op == "==" else "Not for ") + who
        if v == "Upper" and num is not None and op in ("==", "!="):
            return ("For " if op == "==" else "Not for ") + {0: "normal jobs", 1: "transcendent jobs",
                                                             2: "baby jobs"}.get(num, "upper type %d" % num)
    lv = _lin(left)
    if lv and num is not None and None not in lv and len(lv) >= 2 and all(
            c == 1 and t[1] == 1 and t[3] == 0 and t[2][0].startswith("refine level of the ") for t, c in lv.items()):
        parts = [t[2][0][len("refine level of the "):] for t in lv]
        return "Total refine of the %s %s" % (_and(parts), _CMP[op].format("+%d" % num))
    if left[0] == "bin" and left[1] == "&" and rname and op in ("==", "!="):
        if rname.startswith("EAJ_"):
            return ("For " if op == "==" else "Not for ") + _job(rname) + (
                " classes" if "BASEMASK" in repr(left) or "UPPERMASK" in repr(left) else "")
        if rname.startswith("EAJL_"):
            return _cond(("bin", "&", ("call", "eaclass", []), right), Ctx())
    if left[0] == "call" and left[1] == "eaclass" and rname and rname.startswith("EAJ_") and op in ("==", "!="):
        return ("For " if op == "==" else "Not for ") + _job(rname)
    return None


# ---------------------------------------------------------------- statements

def _cmd(name, args, ctx, src):
    """[line, ...] for one command, or None when it has no plain-English form."""
    if name in IGNORE:
        return []
    if name in ("bonus", "bonus2", "bonus3", "bonus4", "bonus5") and args and args[0][0] == "id":
        t = _bonus(args[0][1], args[1:], ctx)
        return [t] if t else None
    if name in ("autobonus", "autobonus2", "autobonus3") and len(args) >= 3 and _strcat(args[0], ctx) is not None:
        inner = describe(_strcat(args[0], ctx), Ctx())
        chance = _p(args[1], ctx, 10)
        dur = _ms(args[2], ctx)
        if name == "autobonus3":
            when = "When using %s" % (_skill(args[3], ctx) if len(args) > 3 else "a skill")
        else:
            names = _names(args[3]) if len(args) > 3 else set()
            kind = [t for kk, t in (("BF_WEAPON", "physical"), ("BF_MAGIC", "magic"), ("BF_MISC", "misc")) if kk in names]
            rng = [t for kk, t in (("BF_SHORT", "melee"), ("BF_LONG", "ranged")) if kk in names]
            what = " or ".join(kind or ["physical"])
            if rng and len(rng) == 1:
                what = rng[0] + " " + what
            when = ("When dealing %s damage" if name == "autobonus" else "When taking %s damage") % what
        if " " in chance:
            return [["%s, for %s (chance: %s)" % (when, dur, chance), inner]]
        return [["%s: %s chance for %s" % (when, chance, dur), inner]]
    if name == "bonus_script" and args and _strcat(args[0], ctx) is not None:
        dur = _ms(("num", _const(args[1], ctx) * 1000), ctx) if len(args) > 1 and _const(args[1], ctx) is not None else "a while"
        return [["For %s" % dur, describe(_strcat(args[0], ctx), Ctx())]]
    if name == "vip_time" and args and _const(args[0], ctx):
        return ["Gives %s of VIP status" % _duration(_const(args[0], ctx) * 60000)]
    if name == "skill" and args:
        lv = _plain(args[1], ctx) if len(args) > 1 else "1"
        return ["Lets you use %s Lv %s" % (_skill(args[0], ctx), lv)]
    if name == "itemskill" and args:
        lv = _plain(args[1], ctx) if len(args) > 1 else "1"
        return ["Casts %s Lv %s" % (_skill(args[0], ctx), lv)]
    if name == "unitskilluseid" and len(args) >= 3:
        return ["Casts %s Lv %s on yourself" % (_skill(args[1], ctx), _plain(args[2], ctx))]
    if name in ("itemheal", "heal", "percentheal") and args:
        unit = "%" if name == "percentheal" else ""
        out = []
        for a, what in zip(args[:2], ("HP", "SP")):
            c = _const(a, ctx)
            if c == 0:
                continue
            amt = _amount(a, ctx, unit, sign=False)
            out.append(("Lose %s %s" % (amt.lstrip("-"), what)) if c is not None and c < 0
                       else "Restores %s %s" % (amt, what))
        return out
    if name in ("sc_start", "sc_start2", "sc_start4") and len(args) >= 2 and args[0][0] == "id":
        sc = args[0][1]
        val = _plain(args[2], ctx) if len(args) > 2 else ""
        t = SC.get(sc)
        label = t.format(None, val) if t else _words(re.sub(r"^SC_", "", sc)).title()
        dur = _const(args[1], ctx)
        if dur is not None and dur <= 0:
            return [label + " (until removed)"]
        return ["%s for %s" % (label, _ms(args[1], ctx))]
    if name == "sc_end" and args and args[0][0] == "id":
        sc = args[0][1]
        if sc == "SC_ALL":
            return ["Removes all status effects"]
        return ["Cures " + _words(re.sub(r"^SC_", "", sc)).title()]
    if name in ("getitem", "getitembound", "getnameditem") and args:
        amt = _plain(args[1], ctx) if len(args) > 1 else "1"
        return ["Gives %s × %s" % (amt, _item(args[0], ctx))]
    if name == "rentitem" and len(args) >= 2:
        return ["Gives %s for %s" % (_item(args[0], ctx), _ms(("num", (_const(args[1], ctx) or 0) * 1000), ctx))]
    if name in ("getgroupitem", "getrandgroupitem"):
        return ["Gives items from its box (listed under Contains)"]
    if name == "pet" and args:
        return ["Used to tame %s" % _mob(args[0], ctx)]
    if name == "bpet":
        return ["Opens the pet egg list to hatch a pet"]
    if name == "monster" and len(args) >= 5:
        return ["Summons %s" % _mob(args[4], ctx)]
    if name in ("transform", "active_transform") and len(args) >= 2:
        return ["Changes your look into %s for %s" % (_mob(args[0], ctx), _ms(args[1], ctx))]
    if name == "mercenary_create" and len(args) >= 2:
        return ["Summons a mercenary for %s" % _ms(("num", (_const(args[1], ctx) or 0)), ctx)]
    if name == "warp" and args:
        m = args[0][1] if args[0][0] == "str" else "?"
        return ["Teleports you to a random spot on the map" if m == "Random" else
                "Teleports you to your save point" if m == "SavePoint" else "Teleports you to " + m]
    if name in ("getexp", "getexp2") and args:
        b = _plain(args[0], ctx)
        j = _plain(args[1], ctx) if len(args) > 1 else "0"
        return [x for x, v in (("Gives %s Base EXP" % b, b), ("Gives %s Job EXP" % j, j)) if v != "0"]
    if name == "guildgetexp" and args:
        return ["Gives %s guild EXP" % _plain(args[0], ctx)]
    if name == "callfunc" and args and args[0][0] == "str":
        f = args[0][1]
        return [FUNCS.get(f, "Special effect when used")]
    if name in ("laphine_synthesis",):
        return ["Opens Laphine's synthesis window"]
    if name in ("laphine_upgrade",):
        return ["Opens Laphine's upgrade window"]
    if name == "item_reform":
        return ["Opens the item reform window"]
    if name == "item_enchant":
        return ["Opens an enchant window"]
    if name in ("cooking", "makerune", "produce"):
        return [{"cooking": "Opens the cooking menu", "makerune": "Opens the rune crafting menu",
                 "produce": "Opens the crafting menu"}[name]]
    if name == "searchstores":
        return ["Searches the vending shops on this map"]
    if name == "setmounting":
        return ["Mounts or dismounts your ride"]
    if name == "homevolution":
        return ["Evolves your homunculus"]
    if name == "addhomintimacy" and args:
        return ["Homunculus intimacy %s" % _amount(args[0], ctx)]
    if name in ("mercenary_heal",):
        return ["Heals your mercenary"]
    if name == "mercenary_sc_start":
        return ["Buffs your mercenary"]
    if name == "buyingstore":
        return ["Opens a buying store"]
    if name == "pet" or name == "catchpet":
        return ["Used to tame a monster"]
    return None


def _src(n):
    """Script source for an expression (to rebuild the script inside an autobonus string)."""
    k = n[0]
    if k == "num":
        return str(n[1])
    if k == "str":
        return '"%s"' % n[1].replace('"', '\\"')
    if k == "id":
        return n[1]
    if k == "un":
        return "%s(%s)" % (n[1], _src(n[2]))
    if k == "bin":
        return "(%s %s %s)" % (_src(n[2]), n[1], _src(n[3]))
    if k == "tern":
        return "(%s ? %s : %s)" % (_src(n[1]), _src(n[2]), _src(n[3]))
    if k == "call":
        return "%s(%s)" % (n[1], ", ".join(_src(a) for a in n[2]))
    raise Bad("src")


def _strcat(n, ctx):
    """Text of a string built with +, numbers and variables written back as script; None if not a string."""
    n = ctx.sub(n)
    if n[0] == "str":
        return n[1]
    if n[0] == "bin" and n[1] == "+":
        a = _strcat(n[2], Ctx())
        if a is None:
            return None
        b = _strcat(n[3], Ctx())
        return a + (b if b is not None else _src(n[3]))
    return None


def _run(stmts, ctx, depth):
    out = []
    for s in stmts:
        k = s[0]
        if k == "nop":
            continue
        if k == "block":
            out += _run(s[1], ctx, depth)
        elif k == "set":
            name, val, src = s[1], s[2], s[3]
            new = ctx.sub(val)
            if ctx.guard:  # only set when the surrounding conditions hold
                old = ctx.env.get(name, ("str", "") if name.endswith("$") else ("num", 0))
                new = ("tern", _all(ctx.guard), new, old)
            ctx.env[name] = new
            if name.startswith(".@") or name.startswith("@"):
                continue
            if name in ("Zeny",):
                out.append("Gives %s zeny" % _amount(("bin", "-", val, ("id", "Zeny")), ctx, sign=False))
                continue
            out.append({"c": src})
        elif k == "code":
            out.append({"c": s[1]})
        elif k == "if":
            heads, node, outer = [], s, ctx.guard
            prior = []  # earlier branches of an else-if chain, all false here
            while True:
                c, a, b = node[1], node[2], node[3]
                cs = ctx.sub(c)
                head = _cond(c, ctx)
                ctx.guard = outer + prior + [(cs, True)]
                body = _run([a], ctx, depth + 1)
                ctx.guard = outer
                if body:
                    heads.append([head, body])
                prior = prior + [(cs, False)]
                if b is None:
                    break
                if b[0] == "if":
                    node = b
                    continue
                ctx.guard = outer + prior
                other = _run([b], ctx, depth + 1)
                ctx.guard = outer
                if other:
                    heads.append(["Otherwise", other])
                break
            if len(heads) > 1:
                for h in heads[1:]:
                    if h[0] != "Otherwise" and not h[0].endswith(" chance"):
                        h[0] = "Otherwise, " + _lower(h[0])
            out += heads
        elif k == "cmd":
            name, args, src = s[1], s[2], s[3]
            if any(_uses(a, ctx.dynamic) for a in args):
                out.append({"c": src})
                continue
            subs = [ctx.sub(a) for a in args]
            if any(_has_tern(a) for a in subs):
                merged = _cmd_cases(name, subs, ctx, src)
                if merged is not None:
                    out += merged
                    continue
            try:
                r = _cmd(name, args, ctx, src)
            except (Bad, IndexError, TypeError, KeyError, ValueError, ZeroDivisionError):
                r = None
            out += r if r is not None else [{"c": src}]
    return out


def _cmd_cases(name, args, ctx, src):
    """Lines for a command whose values change inside if-branches, one value per refine/level range."""
    try:
        cases = _cases(("call", name, args), list(ctx.guard), [])
        outs = []
        for cons, call in cases:
            r = _cmd(name, call[2], Ctx(), src)
            if r is None:
                return None
            outs.append((cons, r))
    except (Bad, IndexError, TypeError, KeyError, ValueError, ZeroDivisionError):
        return None
    g = len(ctx.guard)
    if not outs:
        return []
    if all(r == outs[0][1] for _, r in outs):
        return outs[0][1]
    base = [r for c, r in outs if all(not b for _, b in c[g:])]
    rest = [(c, r) for c, r in outs if not all(not b for _, b in c[g:])]

    def order(cr):
        st = _state(cr[0])
        los = [v[1] for v in st[0].values()] if st else []
        return min(los) if los else 0
    rest.sort(key=order)
    # same lines for several ranges: name them together
    grouped = []
    for c, r in rest:
        d = _case_text(c, g)
        for x in grouped:
            if x[1] == r:
                x[0] += " or " + d
                break
        else:
            grouped.append([d, r])
    single = all(len(r) == 1 and isinstance(r[0], str) for r in [x[1] for x in grouped] + base)
    if single and not any(": " in r[0] for r in [x[1] for x in grouped] + base):
        texts = [x[1][0] for x in grouped] + ([base[0][0]] if base else [])
        toks = [re.findall(r"⟦[^⟧]*⟧\S*|\S+", t) for t in texts]
        pre = 0
        while all(len(t) > pre for t in toks) and len({tuple(t[:pre + 1]) for t in toks}) == 1:
            pre += 1
        suf = 0
        while all(len(t) > pre + suf for t in toks) and len({tuple(t[len(t) - suf - 1:]) for t in toks}) == 1:
            suf += 1
        mids = [" ".join(t[pre:len(t) - suf]) for t in toks]
        head = " ".join(toks[0][:pre])
        tail = " ".join(toks[0][len(toks[0]) - suf:]) if suf else ""
        if all(m.endswith(",") for m in mids):
            mids = [m[:-1] for m in mids]
            tail = "," + (" " + tail if tail else "")
        if any(" per " in m or "every" in m for m in mids):
            opts = "; ".join("at %s: %s" % (x[0], m) for m, x in zip(mids, grouped))
        else:
            opts = ", ".join("%s at %s" % (m, x[0]) for m, x in zip(mids, grouped))
        if base and not re.fullmatch(r"[+-]?0(\.0)?(%| sec)?", mids[-1]):
            body = "%s (%s)" % (mids[-1], opts)
        else:
            body = opts
        line = " ".join(x for x in (head, body, tail) if x)
        return [line.replace(" ,", ",").replace(",,", ",")]
    out = [[(d[0].upper() + d[1:]) if d else "Sometimes", r] for d, r in grouped]
    if base:
        c0 = [c for c, r in outs if all(not b for _, b in c[g:])][0]
        d = _case_text(c0, g)
        out.insert(0, [(d[0].upper() + d[1:]) if d else "Otherwise", base[0]])
    return out


def _uses(n, names):
    if not names or not isinstance(n, tuple):
        return False
    if n[0] == "id":
        return n[1] in names
    return any(_uses(x, names) for x in n[1:] if isinstance(x, tuple)) or (
        n[0] == "call" and any(_uses(x, names) for x in n[2]))


def describe(script, ctx=None):
    """Plain-English lines for an item script (see the module docstring), [] when there is nothing to say."""
    if not script or not str(script).strip():
        return []
    try:
        stmts = _P(str(script)).block()
    except (Bad, RecursionError):
        return [{"c": str(script).strip()}]
    try:
        return _run(stmts, ctx or Ctx(), 0)
    except (Bad, RecursionError, IndexError, TypeError, KeyError, ValueError, ZeroDivisionError, AttributeError):
        return [{"c": str(script).strip()}]


def coverage(lines):
    """(plain lines, code lines) in a describe() result."""
    p = c = 0
    for x in lines:
        if isinstance(x, dict):
            c += 1
        elif isinstance(x, list):
            p += 1
            a, b = coverage(x[1])
            p, c = p + a, c + b
        else:
            p += 1
    return p, c
