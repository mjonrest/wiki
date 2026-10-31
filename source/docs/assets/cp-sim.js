/* Combat Power simulator (special/cp-simulator.md). Data: cp/data.json, written at build time by tools/gen_cp.py
   from the game's own Combat Power tools, so the number here follows the same rules as @cp in game.

   How a build is scored: every item, card, enchant, random option and set bonus has a stat table (per job, refine
   and grade where its script reads them). The tables are added up, skill bonuses get the per-skill curve and caps,
   and each stat is multiplied by its weight. Total = max(physical, magic) + both + defense + utility. */
(function () {
  "use strict";
  var me = document.currentScript && document.currentScript.src;
  if (!me) return;
  var BASE = me.slice(0, me.indexOf("assets/cp-sim.js"));
  var D = null;          // cp/data.json
  var icons = null;
  var ITEM = {}, CARD = {}, ENCH = {}, KEYIX = {};
  var COMBO_BY = {};     // item id -> combos it is part of
  var HAVE = null;       // cp/obtain.json: ids the Database knows a way to get
  var onlyHave = true;

  var SLOTS = [
    // key, label, bit, group
    ["top", "Upper headgear", 1, "Equipment"], ["mid", "Middle headgear", 2, "Equipment"], ["low", "Lower headgear", 4, "Equipment"],
    ["armor", "Armor", 8, "Equipment"], ["weapon", "Weapon", 16, "Equipment"], ["shield", "Shield / left hand", 32, "Equipment"],
    ["garment", "Garment", 64, "Equipment"], ["shoes", "Shoes", 128, "Equipment"],
    ["accR", "Accessory (right)", 256, "Equipment"], ["accL", "Accessory (left)", 512, "Equipment"],
    ["sarmor", "Shadow armor", 16384, "Shadow gear"], ["sweapon", "Shadow weapon", 32768, "Shadow gear"],
    ["sshield", "Shadow shield", 65536, "Shadow gear"], ["sshoes", "Shadow shoes", 131072, "Shadow gear"],
    ["sacR", "Shadow earring", 262144, "Shadow gear"], ["sacL", "Shadow pendant", 524288, "Shadow gear"],
    ["ctop", "Costume upper", 1024, "Costumes"], ["cmid", "Costume middle", 2048, "Costumes"],
    ["clow", "Costume lower", 4096, "Costumes"], ["cgarment", "Costume garment", 8192, "Costumes"]
  ];
  var SLOT = {};
  SLOTS.forEach(function (s) { SLOT[s[0]] = s; });
  var ACC = 256 | 512;
  var COSTUME = 1024 | 2048 | 4096 | 8192;
  var DUAL_JOBS = { "Shadow Cross": 1, "Shinkiro": 1, "Shiranui": 1 };
  var DUAL_TYPES = { "Dagger": 1, "1hSword": 1, "1hAxe": 1 };
  var GRADES = ["None", "D", "C", "B", "A"];
  var GROUPS = { P: "Physical", M: "Magic", S: "Both", D: "Defense", U: "Utility" };
  var ANY_COSTUME = -1; // "any costume" holds a stone for costumes without bonuses

  // item row: [id, name, loc, slots, flags, level, atk, matk, def, subtype, jobmask, table, kind]
  function I(id) { return id === ANY_COSTUME ? [ANY_COSTUME, "Any costume", COSTUME, 0, 0, 1, 0, 0, 0, "", -1, -1, 0] : ITEM[id]; }

  // ------------------------------------------------------------------ build state
  function emptyBuild() { return { job: 0, slots: {} }; }
  var builds = { A: emptyBuild(), B: null };
  var cur = "A";
  function B() { return builds[cur]; }

  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function fmt(n) { return Math.round(n).toLocaleString("en-US"); }
  function fmt1(n) { var r = Math.round(n * 10) / 10; return (r > 0 ? "+" : "") + r.toLocaleString("en-US"); }
  function itemPage(id) { return BASE + "db/items" + (D.dirUrls === false ? ".html" : "/") + "#" + id; }
  function pic(id) {
    var slot = icons && icons.items && icons.items[id];
    if (slot == null) return '<span class="spr ico cp-noico"></span>';
    var per = icons.cols * icons.rows, col = slot % icons.cols, row = Math.floor(slot / icons.cols) % icons.rows;
    return '<span class="spr ico" style="background-image:url(' + BASE + "img/sheets/items-" + Math.floor(slot / per) +
      ".png);background-size:" + icons.cols * 100 + "% " + icons.rows * 100 + "%;background-position:" +
      (col * 100 / (icons.cols - 1)) + "% " + (row * 100 / (icons.rows - 1)) + '%"></span>';
  }
  function label(row) { return row[1] + (row[3] ? " [" + row[3] + "]" : ""); }

  // ------------------------------------------------------------------ adding up stats
  function addVec(acc, vi, mult) {
    if (vi < 0) return;
    var v = D.vecs[vi];
    for (var i = 0; i < v.length; i += 2) {
      var k = D.keys[v[i]];
      acc[k] = (acc[k] || 0) + v[i + 1] * mult;
    }
  }
  function merge(acc, part) {
    for (var k in part) {
      if (k === "fct") acc[k] = Math.max(acc[k] || 0, part[k]); // fixed cast % does not stack: the server keeps the best
      else acc[k] = (acc[k] || 0) + part[k];
    }
  }
  // One stat table at this job, refine and grade.
  function table(acc, ti, j, r, g) {
    if (ti == null || ti < 0) return;
    var t = D.tables[ti], part = {};
    if (typeof t === "number") { addVec(part, t, 1); merge(acc, part); return; }
    var dims = t[0], flat = t[1];
    var hasR = dims.indexOf("r") >= 0, hasG = dims.indexOf("g") >= 0;
    var nr = hasR ? D.nr : 1, ng = hasG ? D.ng : 1;
    var row = dims.indexOf("j") >= 0 ? t[2][j] * nr * ng : 0;
    var gi = hasG ? Math.min(g, D.ng - 1) : 0;
    if (hasR) {
      // the refine axis holds the change from the refine before, so add every step up to r
      var rr = Math.min(r, D.nr - 1);
      for (var x = 0; x <= rr; x++) addVec(part, flat[row + x * ng + gi], 1);
    } else addVec(part, flat[row + gi], 1);
    merge(acc, part);
  }
  // Weapon ATK/MATK and armor DEF with their refine and grade bonus, as the server adds them.
  function baseStats(acc, it, r, g) {
    if (it[12] === 1) {
      var wl = Math.min(it[5] || 1, 5), ref = 0, rnd = 0, t = D.refine["Weapon" + wl];
      if (r && t && t[r]) { ref = Math.floor(t[r][0] / 100); rnd = t[r][1]; }
      if (g) ref += Math.floor(ref * (D.grade["Weapon" + wl + "_" + g] || 0) / 100);
      acc.atk = (acc.atk || 0) + it[6] + ref + rnd / 100 / 2;
      acc.matk = (acc.matk || 0) + it[7] + (it[9] !== "Bow" ? ref : 0);
      if (wl === 5) { acc.patk = (acc.patk || 0) + 2 * r; acc.smatk = (acc.smatk || 0) + 2 * r; }
    } else if (it[12] === 0) {
      var al = it[5] || 1, ta = D.refine["Armor" + al];
      acc.def = (acc.def || 0) + it[8] + (r && ta && ta[r] ? ta[r][0] / 100 : 0);
      if (al === 2) { acc.res = (acc.res || 0) + 2 * r; acc.mres = (acc.mres || 0) + 2 * r; }
    }
  }
  function effRG(it, s) { return [it[4] & 1 ? s.r || 0 : 0, it[4] & 2 ? s.g || 0 : 0]; }

  // Everything one slot adds: the item, its cards, enchants and random options.
  function slotStats(acc, s, j) {
    var it = I(s.id);
    if (!it) return;
    var rg = effRG(it, s), r = rg[0], g = rg[1];
    baseStats(acc, it, r, g);
    table(acc, it[11], j, r, g);
    (s.cards || []).forEach(function (c) { if (c && CARD[c]) table(acc, CARD[c][3], j, r, g); });
    (s.ench || []).forEach(function (e) { if (e && ENCH[e]) table(acc, ENCH[e][2], j, r, g); });
    var src = s.opt != null ? D.sources[s.opt] : null;
    if (src && src.pools) {
      (s.opts || []).forEach(function (o, k) {
        if (!o) return;
        var pool = src.pools[k < src.n[0] ? 0 : 1], op = pool && pool[o[0]];
        if (op) table(acc, op[3][Math.min(o[1], op[3].length - 1)], j, r, g);
      });
    }
  }
  // Ids worn anywhere (items, cards, enchants, stones), for set bonuses.
  function worn(b) {
    var n = {};
    function add(id) { if (id && id > 0) n[id] = (n[id] || 0) + 1; }
    for (var k in b.slots) {
      var s = b.slots[k];
      if (!s || s.id == null) continue;
      add(s.id);
      (s.cards || []).forEach(add);
      (s.ench || []).forEach(add);
    }
    return n;
  }
  function where(b, id) {
    for (var k in b.slots) {
      var s = b.slots[k];
      if (!s || s.id == null) continue;
      if (s.id === id || (s.cards || []).indexOf(id) >= 0 || (s.ench || []).indexOf(id) >= 0) return s;
    }
    return null;
  }
  function slotAt(b, bit) {
    for (var k in b.slots) if (SLOT[k][2] === bit && b.slots[k] && b.slots[k].id != null) return b.slots[k];
    return null;
  }
  function activeCombos(b) {
    var n = worn(b), seen = {}, out = [];
    Object.keys(n).forEach(function (id) {
      (COMBO_BY[id] || []).forEach(function (ci) {
        if (seen[ci]) return;
        seen[ci] = 1;
        var need = {}, ok = true;
        D.combos[ci][0].forEach(function (x) { need[x] = (need[x] || 0) + 1; });
        for (var x in need) if ((n[x] || 0) < need[x]) { ok = false; break; }
        if (ok) out.push(ci);
      });
    });
    return out;
  }
  function stats(b, skipSlot) {
    var acc = {}, j = b.job;
    for (var k in b.slots) if (k !== skipSlot && b.slots[k] && b.slots[k].id != null) slotStats(acc, b.slots[k], j);
    var view = b;
    if (skipSlot && b.slots[skipSlot]) { view = { job: j, slots: Object.assign({}, b.slots) }; delete view.slots[skipSlot]; }
    activeCombos(view).forEach(function (ci) {
      var c = D.combos[ci], s = c[2] ? slotAt(view, c[2]) : where(view, c[3]);
      var it = s && I(s.id), rg = it ? effRG(it, s) : [0, 0];
      table(acc, c[1], j, rg[0], rg[1]);
    });
    return acc;
  }

  // Stats -> CP, the same way @cp does it.
  function score(acc, j) {
    var job = D.jobs[j], W = D.weights, caps = D.caps, flat = {}, perSkill = {};
    for (var k in acc) {
      var dot = k.indexOf(".");
      if (dot < 0) { flat[k] = (flat[k] || 0) + acc[k]; continue; }
      var kind = k.slice(0, dot), sk = k.slice(dot + 1), tier = job.sk[sk];
      if (!tier) continue; // a skill this job does not have
      var x = acc[k];
      if (kind === "sa") {
        var eff = x > 0 ? caps.curve * Math.log(1 + x / caps.curve) : x;
        flat["skillatk" + tier] = (flat["skillatk" + tier] || 0) + eff;
        perSkill[sk] = (perSkill[sk] || 0) + x;
      } else {
        var key = { cd: "skillcd", vc: "skillvctms", fc: "skillfctms" }[kind];
        flat[key] = (flat[key] || 0) + Math.min(x, caps.cd);
      }
    }
    var g = { P: 0, M: 0, S: 0, D: 0, U: 0 }, parts = [];
    for (var key2 in flat) {
      var w = W[key2];
      if (!w) continue;
      var val = flat[key2];
      if (caps.rate[key2] != null) val = Math.min(val, caps.rate[key2]);
      var cp = w[1] * val;
      g[w[0]] += cp;
      if (Math.abs(cp) >= 0.05) parts.push([key2, val, cp]);
    }
    parts.sort(function (a, b) { return Math.abs(b[2]) - Math.abs(a[2]); });
    return { total: Math.max(g.P, g.M) + g.S + g.D + g.U, g: g, flat: flat, parts: parts, perSkill: perSkill };
  }
  function cpOf(b) { return score(stats(b), b.job).total; }

  // ------------------------------------------------------------------ what fits where
  function canDual(j) { return !!DUAL_JOBS[D.jobs[j].n]; }
  function fits(it, key, j) {
    var bit = SLOT[key][2];
    if (!(it[10] & (1 << j)) && it[0] !== ANY_COSTUME) return false;
    if (it[2] & bit) return true;
    return key === "shield" && it[12] === 1 && it[2] === 16 && DUAL_TYPES[it[9]] && canDual(j);
  }
  // Slots an item fills when worn in `key`: all its locations, except one accessory slot only.
  function covers(it, key) {
    if (key === "shield" && it[12] === 1 && it[2] === 16) return 32;
    var bit = SLOT[key][2], m = it[2];
    if ((bit & ACC) && (m & ACC)) m = (m & ~ACC) | bit;
    if ((bit & (262144 | 524288)) && (m & (262144 | 524288))) m = (m & ~(262144 | 524288)) | bit;
    return m | bit;
  }
  function coveredBy(b, key) {
    var bit = SLOT[key][2];
    for (var k in b.slots) {
      var s = b.slots[k];
      if (k !== key && s && s.id != null && (covers(I(s.id), k) & bit)) return k;
    }
    return null;
  }
  function cardCount(it) { return it[0] === ANY_COSTUME || (it[2] & COSTUME) ? 1 : Math.min(it[3], 4); }
  function cardFits(c, it, key) {
    if (it[2] & COSTUME || it[0] === ANY_COSTUME) return !!(c[2] & SLOT[key][2]);
    var m = key === "shield" && it[12] === 1 ? 16 : it[2];
    return !!(c[2] & m);
  }
  function sourcesOf(id) { return (D.itemSources[id] || []).map(function (i) { return [i, D.sources[i]]; }); }

  function equip(b, key, id) {
    var old = b.slots[key] || {};
    if (id == null) { delete b.slots[key]; return; }
    var it = I(id);
    var s = { id: id, r: old.r || 0, g: old.g || 0, cards: [], ench: [], opts: [] };
    var srcs = sourcesOf(id);
    var slotSrc = srcs.filter(function (x) { return x[1].slots; })[0];
    var optSrc = srcs.filter(function (x) { return x[1].pools; })[0];
    s.src = slotSrc ? slotSrc[0] : null;
    s.opt = optSrc ? optSrc[0] : null;
    b.slots[key] = s;
    var cov = covers(it, key);
    SLOTS.forEach(function (x) { if (x[0] !== key && (cov & x[2])) delete b.slots[x[0]]; });
    // a two-handed weapon also clears whatever covered this slot
    var by = coveredBy(b, key);
    if (by) delete b.slots[by];
  }

  // ------------------------------------------------------------------ share links and saved builds
  function pack(b) {
    var o = { j: b.job, s: {} };
    for (var k in b.slots) {
      var s = b.slots[k];
      if (!s || s.id == null) continue;
      o.s[k] = [s.id, s.r || 0, s.g || 0, s.cards || [], s.src == null ? -1 : s.src, s.ench || [], s.opts || []];
    }
    return o;
  }
  function unpack(o) {
    var b = emptyBuild();
    if (!o) return b;
    b.job = o.j >= 0 && o.j < D.jobs.length ? o.j : 0;
    for (var k in o.s || {}) {
      var a = o.s[k];
      if (!SLOT[k] || !I(a[0])) continue;
      var srcs = sourcesOf(a[0]), optSrc = srcs.filter(function (x) { return x[1].pools; })[0];
      b.slots[k] = { id: a[0], r: a[1] | 0, g: a[2] | 0, cards: a[3] || [], src: a[4] >= 0 ? a[4] : null,
                     ench: a[5] || [], opts: a[6] || [], opt: optSrc ? optSrc[0] : null };
    }
    return b;
  }
  function b64(s) { return btoa(unescape(encodeURIComponent(s))).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, ""); }
  function unb64(s) { return decodeURIComponent(escape(atob(s.replace(/-/g, "+").replace(/_/g, "/")))); }
  function shareHash() {
    var o = { a: pack(builds.A) };
    if (builds.B) o.b = pack(builds.B);
    return "#b=" + b64(JSON.stringify(o));
  }
  function readHash() {
    var m = /^#b=(.+)$/.exec(location.hash);
    if (!m) return false;
    try {
      var o = JSON.parse(unb64(m[1]));
      builds.A = unpack(o.a);
      builds.B = o.b ? unpack(o.b) : null;
      return true;
    } catch (e) { return false; }
  }
  var STORE = "cp-sim-builds";
  function saved() { try { return JSON.parse(localStorage.getItem(STORE) || "{}"); } catch (e) { return {}; } }
  function save(all) { try { localStorage.setItem(STORE, JSON.stringify(all)); } catch (e) { /* private window */ } }

  // ------------------------------------------------------------------ picker (one shared pop-up list)
  var pop = null, popClose = null;
  function closePop() { if (pop) { pop.remove(); pop = null; } if (popClose) { document.removeEventListener("mousedown", popClose); popClose = null; } }
  /* rows: [[id, label, extra], ...]; gainOf(id) -> CP change; onPick(id or null) */
  function openPicker(anchor, title, rows, gainOf, onPick, allowNone, noFilter) {
    var filt = HAVE && !noFilter;
    closePop();
    pop = document.createElement("div");
    pop.className = "cp-pop";
    pop.innerHTML = '<div class="cp-pop-head"><input type="search" placeholder="Search ' + esc(title) + '…" aria-label="Search">' +
      '<label class="cp-sort"><input type="checkbox" checked> Biggest CP gain first</label>' +
      (filt ? '<label class="cp-sort"><input type="checkbox" class="cp-have"' + (onlyHave ? " checked" : "") + "> Only items players can get</label>" : "") + '</div><div class="cp-pop-list" role="listbox"></div>';
    document.body.appendChild(pop);
    var r = anchor.getBoundingClientRect();
    var w = Math.min(Math.max(r.width, 440), window.innerWidth - 32);
    pop.style.width = w + "px";
    pop.style.left = Math.max(16, Math.min(r.left, window.innerWidth - w - 16)) + window.scrollX + "px";
    pop.style.top = r.bottom + window.scrollY + 4 + "px";
    var input = pop.querySelector("input[type=search]"), byGain = pop.querySelector(".cp-sort input"), list = pop.querySelector(".cp-pop-list");
    var gains = null, have = pop.querySelector(".cp-have");
    if (have) have.addEventListener("change", function () { onlyHave = have.checked; draw(); });
    function draw() {
      var q = input.value.trim().toLowerCase().split(/\s+/).filter(Boolean);
      var hits = rows.filter(function (x) {
        if (filt && onlyHave && x[0] > 0 && !HAVE[x[0]]) return false;
        var t = (x[1] + " " + x[0]).toLowerCase();
        return q.every(function (w) { return t.indexOf(w) >= 0; });
      });
      if (byGain.checked) {
        if (!gains) { gains = {}; rows.forEach(function (x) { gains[x[0]] = gainOf(x[0]); }); }
        hits.sort(function (a, b) { return gains[b[0]] - gains[a[0]] || (a[1] < b[1] ? -1 : 1); });
      }
      var html = allowNone ? '<button type="button" class="cp-opt" data-id="">(empty)</button>' : "";
      hits.slice(0, 80).forEach(function (x) {
        var gn = gains ? gains[x[0]] : gainOf(x[0]);
        html += '<button type="button" class="cp-opt" data-id="' + x[0] + '">' + (x[0] > 0 ? pic(x[0]) : "") +
          '<span class="cp-opt-name">' + esc(x[1]) + (x[2] ? ' <small>' + esc(x[2]) + "</small>" : "") + (x[0] > 0 ? ' <small class="iid">' + x[0] + "</small>" : "") + "</span>" +
          '<span class="cp-gain ' + (gn > 0.5 ? "up" : gn < -0.5 ? "down" : "") + '">' + fmt1(gn) + "</span></button>";
      });
      if (hits.length > 80) html += '<p class="cp-more">' + (hits.length - 80) + " more: type to narrow down.</p>";
      if (!hits.length) html += '<p class="cp-more">Nothing matches.</p>';
      list.innerHTML = html;
    }
    input.addEventListener("input", draw);
    byGain.addEventListener("change", draw);
    list.addEventListener("click", function (e) {
      var o = e.target.closest(".cp-opt");
      if (!o) return;
      closePop();
      onPick(o.getAttribute("data-id") === "" ? null : +o.getAttribute("data-id"));
    });
    pop.addEventListener("keydown", function (e) { if (e.key === "Escape") closePop(); });
    popClose = function (e) { if (pop && !pop.contains(e.target) && e.target !== anchor) closePop(); };
    setTimeout(function () { document.addEventListener("mousedown", popClose); }, 0);
    draw();
    input.focus();
  }
  // CP change if `mutate` is applied to a copy of the current build
  function gainWith(mutate, base) {
    var b = B();
    var copy = { job: b.job, slots: {} };
    for (var k in b.slots) copy.slots[k] = JSON.parse(JSON.stringify(b.slots[k]));
    mutate(copy);
    return cpOf(copy) - (base == null ? cpOf(b) : base);
  }

  // ------------------------------------------------------------------ drawing
  var root;
  function selectHtml(cls, opts, val, attrs) {
    return '<select class="' + cls + '"' + (attrs || "") + ">" + opts.map(function (o) {
      return '<option value="' + o[0] + '"' + (String(o[0]) === String(val) ? " selected" : "") + ">" + esc(o[1]) + "</option>";
    }).join("") + "</select>";
  }
  function pickBtn(cls, id, row, text, data) {
    return '<button type="button" class="cp-pick ' + cls + '"' + data + ">" + (row ? (id > 0 ? pic(id) : "") + esc(text) : '<span class="cp-empty">' + esc(text) + "</span>") + "</button>";
  }
  // Random option name from what it gives at its best roll ("VAR_STRAMOUNT" -> "STR 5-15")
  function optName(p) {
    var t = D.tables[p[3][p[3].length - 1]], names = [];
    if (typeof t === "number") {
      var v = D.vecs[t];
      for (var i = 0; i < v.length; i += 2) {
        var k = D.keys[v[i]], w = D.weights[k];
        names.push(w ? w[2] : k.indexOf("sa.") === 0 ? "Skill damage %" : k);
      }
    }
    return (names.length && names.length < 4 ? names.join(", ") : p[0].replace(/^VAR_|^RDM_/, "").replace(/_/g, " ")) +
      (p[2] > p[1] ? " " + p[1] + "-" + p[2] : p[1] ? " " + p[1] : "");
  }
  function slotHtml(key) {
    var b = B(), s = b.slots[key], lab = SLOT[key][1], by = coveredBy(b, key);
    var marg = s && s.id != null ? cpOf(b) - score(stats(b, key), b.job).total : 0;
    var filled = s && s.id != null;
    var h = '<div class="cp-slot ' + (by ? "cp-is-covered" : filled ? "cp-is-filled" : "cp-is-empty") + '" data-slot="' + key + '">' +
      '<div class="cp-slot-head"><span class="cp-slot-name">' + esc(lab) + "</span>" +
      (filled ? '<span class="cp-slot-cp ' + (marg >= 0 ? "up" : "down") + '" title="CP this slot adds to the build">' + fmt1(marg) + " CP</span>" +
        '<button type="button" class="cp-x" data-pick="remove" title="Take it off" aria-label="Take off ' + esc(lab) + '">×</button>' : "") + "</div>";
    if (by) return h + '<p class="cp-covered">Used by the ' + esc(SLOT[by][1].toLowerCase()) + ".</p></div>";
    var it = s && I(s.id);
    h += pickBtn("cp-item", it && it[0], it, it ? label(it) : "+ Choose " + lab.toLowerCase(), ' data-pick="item"');
    if (!it) return h + "</div>";
    if (it[0] > 0) h += '<a class="cp-link" href="' + itemPage(it[0]) + '" target="_blank" rel="noopener" title="Open in the Database">ⓘ</a>';
    var row = "";
    if (it[4] & 1) {
      var ro = [];
      for (var r = 0; r < D.nr; r++) ro.push([r, "+" + r]);
      row += "<label>Refine " + selectHtml("cp-ref", ro, s.r || 0) + "</label>";
    }
    if (it[4] & 2) row += "<label>Grade " + selectHtml("cp-grade", GRADES.map(function (g, i) { return [i, g]; }), s.g || 0) + "</label>";
    if (row) h += '<div class="cp-row">' + row + "</div>";
    var n = cardCount(it);
    if (n) {
      h += '<div class="cp-sub">' + ((it[2] & COSTUME) || it[0] === ANY_COSTUME ? "Costume stone" : "Cards") + "</div>";
      for (var c = 0; c < n; c++) {
        var cid = s.cards[c], cr = cid && CARD[cid];
        h += pickBtn("cp-card", cid, cr, cr ? cr[1] : "Empty slot " + (c + 1), ' data-pick="card" data-i="' + c + '"');
      }
    }
    var srcs = sourcesOf(it[0]).filter(function (x) { return x[1].slots; });
    var free = Math.max(0, 4 - it[3]);
    if (srcs.length && free) {
      var src = s.src != null ? D.sources[s.src] : null;
      h += '<div class="cp-sub">Enchants ' + selectHtml("cp-src", [["", "none"]].concat(srcs.map(function (x) {
        return [x[0], x[1].s + (x[1].w ? " (" + x[1].w + ")" : "")];
      })), s.src == null ? "" : s.src) + "</div>";
      if (src) {
        if (src.m && (s.r || 0) < src.m) h += '<p class="cp-warn">This enchanter needs refine +' + src.m + " or more.</p>";
        for (var e = 0; e < Math.min(free, src.slots.length); e++) {
          var eid = s.ench[e], er = eid && ENCH[eid];
          h += pickBtn("cp-ench", eid, er, er ? er[1] : "Enchant " + (e + 1), ' data-pick="ench" data-i="' + e + '"');
        }
      }
    }
    var osrc = s.opt != null ? D.sources[s.opt] : null;
    if (osrc && osrc.pools) {
      h += '<div class="cp-sub">Random options (' + esc(osrc.w || osrc.s) + ")</div>";
      var total = osrc.n[0] + osrc.n[1];
      for (var o = 0; o < total; o++) {
        var pool = osrc.pools[o < osrc.n[0] ? 0 : 1], sel = s.opts[o], op = sel && pool[sel[0]];
        h += '<div class="cp-row">' + selectHtml("cp-opt-sel", [["", o < osrc.n[0] ? "Option " + (o + 1) : "Option 3 (rare)"]].concat(pool.map(function (p, i) {
          return [i, optName(p)];
        })), sel ? sel[0] : "", ' data-i="' + o + '"');
        if (op && op[2] > op[1]) {
          var vals = [];
          for (var v = op[1]; v <= op[2]; v++) vals.push([v - op[1], String(v)]);
          h += selectHtml("cp-opt-val", vals, sel[1], ' data-i="' + o + '"');
        }
        h += "</div>";
      }
    }
    return h + "</div>";
  }

  function summaryHtml() {
    var b = B(), res = score(stats(b), b.job), g = res.g, max = Math.max(g.P, g.M, g.S, g.D, g.U, 1);
    var h = '<div class="cp-total"><span>Combat Power</span><strong>' + fmt(res.total) + "</strong></div>";
    if (builds.B) {
      var other = builds[cur === "A" ? "B" : "A"], ot = cpOf(other), d = res.total - ot;
      h += '<p class="cp-vs">Build ' + (cur === "A" ? "B" : "A") + ": " + fmt(ot) + ' CP, this one is <b class="' + (d >= 0 ? "up" : "down") + '">' + fmt1(d) + "</b></p>";
    }
    h += '<div class="cp-groups">';
    ["P", "M", "S", "D", "U"].forEach(function (k) {
      var counted = (k === "P" && g.P < g.M) || (k === "M" && g.M <= g.P && g.P > 0) ? " cp-off" : "";
      h += '<div class="cp-group cp-g-' + k + counted + '"><span>' + GROUPS[k] + '</span><span class="cp-bar"><i style="width:' +
        Math.max(0, g[k] / max * 100) + '%"></i></span><b>' + fmt(g[k]) + "</b></div>";
    });
    h += '</div><p class="cp-note">Only the bigger of Physical and Magic counts.</p>';
    var combos = activeCombos(b);
    if (combos.length) {
      h += '<div class="cp-sub">Set bonuses on (' + combos.length + ")</div><ul class=\"cp-sets\">";
      combos.forEach(function (ci) {
        h += "<li>" + D.combos[ci][0].map(function (id) {
          var r = ITEM[id] || CARD[id] || ENCH[id];
          return esc(r ? r[1] : id);
        }).join(" + ") + "</li>";
      });
      h += "</ul>";
    }
    h += '<div class="cp-sub">Biggest parts</div><table class="cp-parts"><tbody>';
    res.parts.slice(0, 12).forEach(function (p) { h += partRow(p); });
    h += "</tbody></table>";
    if (res.parts.length > 12) {
      h += '<details class="cp-all"><summary>Every stat (' + res.parts.length + ')</summary><table class="cp-parts"><tbody>';
      res.parts.forEach(function (p) { h += partRow(p); });
      h += "</tbody></table></details>";
    }
    var sk = Object.keys(res.perSkill);
    if (sk.length) {
      sk.sort(function (a, b) { return res.perSkill[b] - res.perSkill[a]; });
      h += '<details class="cp-all"><summary>Skill damage bonuses (' + sk.length + ")</summary><table class=\"cp-parts\"><tbody>";
      sk.forEach(function (i) { h += "<tr><td>" + esc(D.skills[i][1]) + "</td><td>+" + Math.round(res.perSkill[i]) + "%</td><td></td></tr>"; });
      h += "</tbody></table></details>";
    }
    return h;
  }
  function partRow(p) {
    var w = D.weights[p[0]], name = w ? w[2] : p[0];
    var v = Math.round(p[1] * 100) / 100;
    return '<tr title="' + esc(w && w[3] || "") + '"><td>' + esc(name) + "</td><td>" + v.toLocaleString("en-US") + "</td><td>" + fmt1(p[2]) + "</td></tr>";
  }

  function draw() {
    var b = B();
    var jobs = D.jobs.map(function (j, i) { return [i, j.n]; });
    var res = score(stats(b), b.job), other = builds.B ? cpOf(builds[cur === "A" ? "B" : "A"]) : null;
    var h = '<div class="cp-toolbar"><div class="cp-bar-top"><label class="cp-joblab">Job ' + selectHtml("cp-job", jobs, b.job) + "</label>" +
      '<div class="cp-tabs"><button type="button" class="cp-tab' + (cur === "A" ? " on" : "") + '" data-b="A">Build A</button>' +
      (builds.B ? '<button type="button" class="cp-tab' + (cur === "B" ? " on" : "") + '" data-b="B">Build B</button>'
        : '<button type="button" class="cp-tab cp-addb" title="Copy this build to compare a change">+ Compare</button>') + "</div></div>" +
      '<div class="cp-bar-top cp-actions"><button type="button" class="cp-btn cp-share">Copy share link</button>' +
      '<button type="button" class="cp-btn cp-saveb">Save build</button>' +
      selectHtml("cp-load", [["", "Load a saved build…"]].concat(Object.keys(saved()).sort().map(function (n) { return [n, n]; })), "") +
      '<button type="button" class="cp-btn cp-clear">Clear all</button></div></div>';
    // small total that stays on screen on phones, where the full summary sits below the gear
    h += '<div class="cp-mini"><span>Combat Power</span><b>' + fmt(res.total) + "</b>" +
      (other != null ? '<small class="' + (res.total >= other ? "up" : "down") + '">' + fmt1(res.total - other) + " vs " + (cur === "A" ? "B" : "A") + "</small>" : "") + "</div>";
    h += '<div class="cp-main"><div class="cp-gear">';
    var group = "";
    SLOTS.forEach(function (s) {
      if (s[3] !== group) {
        if (group) h += "</div>";
        group = s[3];
        var inGroup = SLOTS.filter(function (x) { return x[3] === group; });
        var used = inGroup.filter(function (x) { return b.slots[x[0]] && b.slots[x[0]].id != null; }).length;
        h += '<h3 class="cp-h">' + group + ' <small>' + used + " / " + inGroup.length + '</small></h3><div class="cp-grid">';
      }
      h += slotHtml(s[0]);
    });
    h += '</div></div><aside class="cp-side">' + summaryHtml() + "</aside></div>";
    root.innerHTML = h;
  }

  function redraw() {
    draw();
    try { history.replaceState(null, "", location.pathname + shareHash()); } catch (e) { /* file:// */ }
  }

  function bind() {
    root.addEventListener("change", function (e) {
      var t = e.target, b = B(), el = t.closest(".cp-slot"), key = el && el.getAttribute("data-slot"), s = key && b.slots[key];
      if (t.classList.contains("cp-job")) {
        b.job = +t.value;
        // drop what the new job can't wear
        for (var k in b.slots) if (b.slots[k].id !== ANY_COSTUME && !fits(I(b.slots[k].id), k, b.job)) delete b.slots[k];
      } else if (t.classList.contains("cp-load")) {
        var all = saved();
        if (!t.value || !all[t.value]) return;
        builds[cur] = unpack(all[t.value]);
      } else if (!s) return;
      else if (t.classList.contains("cp-ref")) s.r = +t.value;
      else if (t.classList.contains("cp-grade")) s.g = +t.value;
      else if (t.classList.contains("cp-src")) { s.src = t.value === "" ? null : +t.value; s.ench = []; }
      else if (t.classList.contains("cp-opt-sel")) {
        var oi = +t.getAttribute("data-i"), os = D.sources[s.opt], pl = os.pools[oi < os.n[0] ? 0 : 1];
        s.opts[oi] = t.value === "" ? null : [+t.value, pl[+t.value][3].length - 1];
      }
      else if (t.classList.contains("cp-opt-val")) { var o = s.opts[+t.getAttribute("data-i")]; if (o) o[1] = +t.value; }
      redraw();
    });
    root.addEventListener("click", function (e) {
      var t = e.target.closest("button");
      if (!t || !root.contains(t)) return;
      var b = B();
      if (t.classList.contains("cp-tab")) {
        if (t.classList.contains("cp-addb")) { builds.B = unpack(pack(builds.A)); cur = "B"; } else cur = t.getAttribute("data-b");
        return redraw();
      }
      if (t.classList.contains("cp-share")) {
        var url = location.href.split("#")[0] + shareHash();
        var done = function () { t.textContent = "Link copied"; setTimeout(function () { t.textContent = "Copy share link"; }, 1500); };
        if (navigator.clipboard) navigator.clipboard.writeText(url).then(done, function () { prompt("Copy this link:", url); });
        else prompt("Copy this link:", url);
        return;
      }
      if (t.classList.contains("cp-saveb")) {
        var name = prompt("Name this build:", D.jobs[b.job].n);
        if (!name) return;
        var all = saved(); all[name] = pack(b); save(all);
        return redraw();
      }
      if (t.classList.contains("cp-clear")) { builds[cur] = { job: b.job, slots: {} }; return redraw(); }
      var el = t.closest(".cp-slot"), key = el && el.getAttribute("data-slot"), kind = t.getAttribute("data-pick");
      if (!key || !kind) return;
      var s = b.slots[key], i = +t.getAttribute("data-i"), base = cpOf(b);
      if (kind === "remove") { delete b.slots[key]; return redraw(); }
      if (kind === "item") {
        var rows = [];
        if (SLOT[key][2] & COSTUME) rows.push([ANY_COSTUME, "Any costume (no bonus, holds a stone)", ""]);
        D.items.forEach(function (it) { if (fits(it, key, b.job)) rows.push([it[0], label(it), it[12] === 1 ? it[9] : ""]); });
        openPicker(t, SLOT[key][1].toLowerCase(), rows, function (id) { return gainWith(function (c) { equip(c, key, id); }, base); },
          function (id) { equip(b, key, id); redraw(); }, true);
      } else if (kind === "card") {
        var it = I(s.id), cr = [];
        D.cards.forEach(function (c) { if (cardFits(c, it, key)) cr.push([c[0], c[1], ""]); });
        openPicker(t, (it[2] & COSTUME) || it[0] === ANY_COSTUME ? "stones" : "cards", cr,
          function (id) { return gainWith(function (c) { c.slots[key].cards[i] = id; }, base); },
          function (id) { s.cards[i] = id; redraw(); }, true);
      } else if (kind === "ench") {
        var src = D.sources[s.src], er = (src.slots[i] || []).map(function (id) { return [id, ENCH[id] ? ENCH[id][1] : String(id), ""]; });
        openPicker(t, "enchants", er, function (id) { return gainWith(function (c) { c.slots[key].ench[i] = id; }, base); },
          function (id) { s.ench[i] = id; redraw(); }, true, true);
      }
    });
  }

  function start() {
    root = document.querySelector(".cp-app");
    if (!root) return;
    Promise.all([
      fetch(BASE + "cp/data.json", { cache: "no-cache" }).then(function (r) { if (!r.ok) throw new Error("cp/data.json: " + r.status); return r.json(); }),
      fetch(BASE + "img/icons.json", { cache: "no-cache" }).then(function (r) { return r.ok ? r.json() : null; }).catch(function () { return null; }),
      fetch(BASE + "cp/obtain.json", { cache: "no-cache" }).then(function (r) { return r.ok ? r.json() : null; }).catch(function () { return null; })
    ]).then(function (res) {
      if (res[2] && res[2].length) { HAVE = {}; res[2].forEach(function (id) { HAVE[id] = 1; }); }
      D = res[0];
      var ic = res[1];
      if (ic) {
        icons = { cols: ic.cols, rows: ic.rows, items: {} };
        for (var i = 0; i < (ic.items || []).length; i += 2) icons.items[ic.items[i]] = ic.items[i + 1];
      }
      D.keys.forEach(function (k, i) { KEYIX[k] = i; });
      D.items.forEach(function (it) { ITEM[it[0]] = it; });
      D.cards.forEach(function (c) { CARD[c[0]] = c; });
      D.enchants.forEach(function (e) { ENCH[e[0]] = e; });
      D.combos.forEach(function (c, ci) {
        c[0].forEach(function (id) { (COMBO_BY[id] = COMBO_BY[id] || []).indexOf(ci) < 0 && COMBO_BY[id].push(ci); });
      });
      readHash();
      bind();
      draw();
    }).catch(function (e) {
      root.innerHTML = '<p class="cp-warn">Could not load the simulator data (' + esc(e.message) + ").</p>";
    });
  }
  // Material's instant navigation swaps pages without reloading scripts
  if (window.document$ && window.document$.subscribe) window.document$.subscribe(start);
  else if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start);
  else start();
})();
