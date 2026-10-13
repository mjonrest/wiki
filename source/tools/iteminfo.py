"""Server tags (e.g. jRO) from the game client's itemInfo.lua, for the Database "Server" filter.

Item descriptions are not taken from the client: the wiki shows and searches the effects it translates from the
item scripts instead (tools/describe.py). The client file is too big to keep here (25 MB), so this saves the tags:

    python3 tools/iteminfo.py PATH/TO/itemInfo.lua    # writes data/item_text.json

Run it again whenever the client's itemInfo changes. Lua keeps the last entry of a duplicated id, and so does this.
"""
import json
import os
import re
import sys

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "item_text.json")
ENTRY = re.compile(r"\[\s*(\d+)\s*\]\s*=\s*\{")
STRING = re.compile(r'"((?:[^"\\]|\\.)*)"')
COLOR = re.compile(r"\^[0-9A-Fa-f]{6}")


def _field(body, key):
    m = re.search(r"\b" + key + r'\s*=\s*"((?:[^"\\]|\\.)*)"', body)
    return m.group(1) if m else ""


def parse(path):
    """{id: {"name": client name, "desc": [lines], "server": "jRO" or ""}} from an itemInfo.lua (CP949)."""
    with open(path, "rb") as f:
        text = f.read().decode("cp949", "replace")
    out, pos, n = {}, 0, len(text)
    while True:
        m = ENTRY.search(text, pos)
        if not m:
            break
        i, depth, quoted = m.end(), 1, False
        while i < n and depth:
            c = text[i]
            if quoted:
                if c == "\\":
                    i += 1
                elif c == '"':
                    quoted = False
            elif c == '"':
                quoted = True
            elif c == "-" and text.startswith("--", i):
                j = text.find("\n", i)
                i = j if j > 0 else n
                continue
            elif c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
            i += 1
        body, pos = text[m.end():i - 1], i
        desc = re.search(r"\bidentifiedDescriptionName\s*=\s*\{(.*?)\}\s*,?\s*\n", body, re.S)
        lines = [COLOR.sub("", s).replace('\\"', '"').strip() for s in STRING.findall(desc.group(1))] if desc else []
        out[int(m.group(1))] = {"name": _field(body, "identifiedDisplayName"), "desc": lines,
                                "server": _field(body, "Server")}
    return out


def main(path):
    data = parse(path)
    out = {}
    for iid, d in sorted(data.items()):
        if d["server"]:
            out[str(iid)] = {"s": d["server"]}
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, separators=(",", ":"))
    print(f"{len(out)} items -> {OUT}")


@__import__("functools").lru_cache(None)
def load():
    """{item id: {"s": server tag}}, or {} before the file exists."""
    if not os.path.exists(OUT):
        return {}
    with open(OUT, encoding="utf-8") as f:
        return {int(k): v for k, v in json.load(f).items()}


if __name__ == "__main__":
    main(sys.argv[1])
