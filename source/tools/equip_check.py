"""Who can wear an item, decided the way the map server decides it.

The server turns an item's Jobs list into three job masks (first jobs, 2-1 jobs, 2-2 jobs) and its Classes list
into a tier mask (itemdb.cpp: itemdb_jobid2mapid and the Classes loop). A character can wear the item when the
mask of its own row has its first-job bit (pc.cpp: pc_job_can_use_item) and the tier mask lets its tier through
(pc.cpp: pc_isItemClass, renewal branch). So `Swordman: true` alone does not let a Dragon Knight wear an item
(Dragon Knight sits on the 2-1 row, with Knight), while `Star_Emperor: true` does let a Sky Emperor wear it.

The job and tier numbers are read from the game source (src/map/map.hpp, script_constants.hpp, itemdb.hpp), so
this follows the server when they change.
"""
import os
import re

ALL64 = (1 << 64) - 1


def _read(root, path):
    with open(os.path.join(root, path), encoding="utf-8", errors="replace") as f:
        return f.read()


def _constants(root):
    src = _read(root, "src/map/map.hpp")
    defs = {"UINT64_MAX": ALL64}
    defs.update({k: int(v, 16) for k, v in re.findall(r"#define (JOBL_\w+|MAPID_\w+MASK) (0x[0-9a-fA-F]+)", src)})
    body = src[src.index("enum e_mapid"):]
    body = re.sub(r"//[^\n]*", "", body[body.index("{") + 1:body.index("};")])
    mapid, nxt = {}, 0
    for part in body.split(","):
        part = part.strip()
        if not part:
            continue
        if "=" in part:
            name, expr = (x.strip() for x in part.split("=", 1))
            v = 0
            for t in expr.split("|"):
                t = t.strip()
                v |= int(t, 16) if t.startswith("0x") else defs[t] if t in defs else mapid[t]
        else:
            name, v = part, nxt
        mapid[name] = v
        nxt = v + 1
    sc = _read(root, "src/map/script_constants.hpp")
    eaj = {k.upper(): mapid[v] if v in mapid else defs[v]
           for k, v in re.findall(r'export_constant2\("EAJ_(\w+)",\s*(\w+)\)', sc)}
    ih = _read(root, "src/map/itemdb.hpp")
    itemj = {k.upper(): int(v, 16) for k, v in re.findall(r"ITEMJ_(\w+)\s*=\s*(0x[0-9A-Fa-f]+)", ih)}
    itemj["ALL_UPPER"] = itemj["UPPER"] | itemj["THIRD_UPPER"] | itemj["FOURTH"]
    itemj["ALL_BABY"] = itemj["BABY"] | itemj["THIRD_BABY"]
    itemj["ALL_THIRD"] = itemj["THIRD"] | itemj["THIRD_UPPER"] | itemj["THIRD_BABY"]
    itemj["ALL"] = (itemj["NORMAL"] | itemj["UPPER"] | itemj["BABY"] | itemj["THIRD"] | itemj["THIRD_UPPER"]
                    | itemj["THIRD_BABY"] | itemj["FOURTH"])  # renewal
    return defs, mapid, eaj, itemj


def make(root, jobs):
    """Returns mask(item) -> bit i set when jobs[i] can wear it. jobs are the Combat Power tools' JOBS rows,
    whose second field names the job's MAPID (DRAGON_KNIGHT -> MAPID_DRAGON_KNIGHT)."""
    defs, mapid, eaj, itemj = _constants(root)
    J21, J22, J3, J4 = defs["JOBL_2_1"], defs["JOBL_2_2"], defs["JOBL_THIRD"], defs["JOBL_FOURTH"]
    UP, BABY = defs["JOBL_UPPER"], defs["JOBL_BABY"]
    F1, F2, F3, F4 = (defs[k] for k in ("MAPID_FIRSTMASK", "MAPID_SECONDMASK", "MAPID_THIRDMASK", "MAPID_FOURTHMASK"))

    def upper_expanded_second(c):  # pc.hpp: pc_is_upper_expanded_second
        return ((c & F4) in (mapid["MAPID_HYPER_NOVICE"], mapid["MAPID_SKY_EMPEROR"], mapid["MAPID_SOUL_ASCETIC"])
                or (c & F3) in (mapid["MAPID_NIGHT_WATCH"], mapid["MAPID_SHINKIROSHIRANUI"], mapid["MAPID_ALITEA"])
                or (c & F2) == mapid["MAPID_SPIRIT_HANDLER"])

    def class_base(it):
        jl = it.get("Jobs")
        if jl is None:
            return [ALL64] * 3
        base = [0, 0, 0]

        def put(m, on):
            t = [ALL64] * 3 if m == ALL64 else [0, 0, 0]
            if m != ALL64:
                t[1 if m & J21 else 2 if m & J22 else 0] = 1 << (m & F1)
            for i in range(3):
                if t[i]:
                    base[i] = base[i] | t[i] if on else base[i] & ~t[i]
        if "All" in jl:
            put(ALL64, bool(jl["All"]))
        for k, on in jl.items():
            if k == "All":
                continue
            if k.upper() not in eaj:  # the server warns and lets every job wear it
                put(ALL64, True)
                break
            put(eaj[k.upper()], bool(on))
        return base

    def class_upper(it):
        cl = it.get("Classes")
        if cl is None:
            return itemj["ALL"]
        u = 0
        if "All" in cl:
            u = u | itemj["ALL"] if cl["All"] else u & ~itemj["ALL"]
        for k, on in cl.items():
            if k == "All":
                continue
            if k.upper() not in itemj:
                u |= itemj["ALL"]
                break
            u = u | itemj[k.upper()] if on else u & ~itemj[k.upper()]
        return u

    def tier_ok(u, c):  # pc.cpp: pc_isItemClass (renewal)
        return bool(
            (u & itemj["NORMAL"] and not c & (UP | BABY | J3 | J4))
            or (u & itemj["UPPER"] and c & UP and not c & J3)
            or (u & itemj["BABY"] and c & BABY and not c & J3)
            or (u & itemj["THIRD"] and c & J3 and not c & (UP | BABY) and not c & J4)
            or (u & itemj["THIRD_UPPER"] and c & J3 and c & UP and not c & J4)
            or (u & itemj["THIRD_BABY"] and c & J3 and c & BABY and not c & J4)
            or (u & itemj["FOURTH"] and (c & J4 or upper_expanded_second(c))))

    classes = [mapid["MAPID_" + j[1]] for j in jobs]

    def mask(it):
        base, u, m = class_base(it), class_upper(it), 0
        for i, c in enumerate(classes):
            row = 1 if c & J21 else 2 if c & J22 else 0
            if base[row] & (1 << (c & F1)) and tier_ok(u, c):
                m |= 1 << i
        return m
    return mask
