/* Database pages: a searchable list, and a detail view at #<id> (items, monsters, skills) or #<Job> (jobs).
   Data comes from db/data/*.json, written at build time by tools/gen_db.py. */
(function () {
  "use strict";
  var me = document.currentScript.src;
  var BASE = me.slice(0, me.indexOf("assets/db.js"));
  var DATA = BASE + "db/data/";
  var cache = {};
  var meta = null;
  var icons = null; // img/icons.json: where each item and skill icon sits in the sprite sheets
  var npcPics = {}; // img/npcs.json: the NPC sprites that have a picture

  function get(path) {
    if (!cache[path]) {
      cache[path] = fetch(DATA + path, { cache: "no-cache" }).then(function (r) {
        if (!r.ok) throw new Error(path + ": " + r.status);
        return r.json();
      });
    }
    return cache[path];
  }

  // Pictures saved in img/ by tools/fetch_images.py; a missing one removes itself. (No Divine Pride fallback:
  // it answers unknown ids with a "no image" picture.) Item and skill icons are cells of the sprite sheets
  // that tools/pack_icons.py writes, drawn as a background so one sheet serves a thousand icons.
  function pic(kind, id, cls) {
    if (kind === "items" || kind === "skills") {
      var slot = icons && icons[kind] && icons[kind][id];
      if (slot == null) return "";
      var per = icons.cols * icons.rows, col = slot % icons.cols, row = Math.floor(slot / icons.cols) % icons.rows;
      return '<span class="spr ' + cls + '" style="background-image:url(' + BASE + "img/sheets/" + kind + "-" + Math.floor(slot / per) +
        ".png);background-size:" + icons.cols * 100 + "% " + icons.rows * 100 + "%;background-position:" +
        (col * 100 / (icons.cols - 1)) + "% " + (row * 100 / (icons.rows - 1)) + '%"></span>';
    }
    return '<img class="' + cls + '" src="' + BASE + "img/" + kind + "/" + id + '.png" alt="" loading="lazy" onerror="this.remove()">';
  }
  function loadIcons() {
    return fetch(BASE + "img/icons.json", { cache: "no-cache" }).then(function (r) { return r.ok ? r.json() : null; }).then(function (d) {
      if (!d) return;
      icons = { cols: d.cols, rows: d.rows };
      ["items", "skills"].forEach(function (k) {
        var m = {}, a = d[k] || [];
        for (var i = 0; i < a.length; i += 2) m[a[i]] = a[i + 1];
        icons[k] = m;
      });
    }).catch(function () { icons = null; });
  }
  function loadNpcPics() {
    return fetch(BASE + "img/npcs.json", { cache: "no-cache" }).then(function (r) { return r.ok ? r.json() : []; }).then(function (a) {
      a.forEach(function (id) { npcPics[id] = 1; });
    }).catch(function () {});
  }

  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function nice(s) { return String(s == null ? "" : s).replace(/_/g, " "); }
  function num(n) { return n == null || n === "" ? "" : Number(n).toLocaleString("en-US"); }
  function pct(r) { var v = r / 100; return (v >= 1 ? +v.toFixed(2) : +v.toFixed(3)) + "%"; }
  function secs(ms) { return ms == null ? "" : +(ms / 1000).toFixed(2) + " s"; }

  function page(kind) { return BASE + "db/" + kind + (meta.dirUrls ? "/" : ".html"); }
  function itemLink(id, names) {
    var it = names && names[id];
    var label = it ? it[1] + (+it[4] ? " [" + it[4] + "]" : "") : "Item " + id;
    return pic("items", id, "ico") + '<a href="' + page("items") + "#" + id + '">' + esc(label) + '</a> <small class="iid">' + id + "</small>";
  }
  function mobLink(id, names) {
    var m = names && names[id];
    return pic("mobs", id, "mob-sm") + '<a href="' + page("monsters") + "#" + id + '">' + esc(m ? m[1] : "Monster " + id) + '</a> <small class="iid">' + id + "</small>";
  }
  function skillLink(aegis, skills) {
    var s = skills && skills.byAegis[aegis];
    return (s ? pic("skills", s.id, "ico") : "") + '<a href="' + page("skills") + "#" + esc(aegis) + '">' + esc(s ? s.name : nice(aegis)) + "</a>";
  }
  // NPC sprites: monster pictures for monster-shaped NPCs, otherwise the saved NPC picture.
  function npcPic(sprite, cls) { return sprite >= 1001 && sprite < 4000 ? pic("mobs", sprite, cls) : npcPics[sprite] ? pic("npcs", sprite, cls) : ""; }
  function npcLink(id, npcs) {
    var n = npcs && npcs[id];
    return (n ? npcPic(n[5], "ico") : "") + '<a href="' + page("npcs") + "#" + id + '">' + esc(n ? n[1] : "NPC " + id) + "</a>";
  }
  function where(m, x, y) { return "<code>/navi " + esc(m) + " " + x + "/" + y + "</code>"; }
  function jobLink(job) { return '<a href="' + page("jobs") + "#" + esc(job) + '">' + esc(nice(job)) + "</a>"; }

  function table(head, rows, cls) {
    if (!rows.length) return "";
    return '<div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table' + (cls ? ' class="' + cls + '"' : "") +
      "><thead><tr>" + head.map(function (h) { return "<th>" + h + "</th>"; }).join("") + "</tr></thead><tbody>" +
      rows.map(function (r) { return "<tr>" + r.map(function (c) { return "<td>" + c + "</td>"; }).join("") + "</tr>"; }).join("") +
      "</tbody></table></div></div>";
  }
  function facts(pairs) {
    var rows = pairs.filter(function (p) { return p[1] !== "" && p[1] != null; });
    return '<dl class="db-facts">' + rows.map(function (p) { return "<dt>" + p[0] + "</dt><dd>" + p[1] + "</dd>"; }).join("") + "</dl>";
  }
  function chips(list) {
    return list.map(function (x) { return '<span class="db-chip">' + esc(nice(x)) + "</span>"; }).join(" ");
  }
  function byId(list) { var o = {}; list.forEach(function (r) { o[r[0]] = r; }); return o; }

  function skillsData() {
    return get("skills.json").then(function (list) {
      if (!list.byAegis) {
        list.byAegis = {}; list.byId = {};
        list.forEach(function (s) { list.byAegis[s.aegis] = s; list.byId[s.id] = s; });
      }
      return list;
    });
  }

  /* ------------------------------------------------------------ list views */

  /* Each list: columns (header, cell, sort key) and filters (select, range or text) suited to its data. */
  function nameCell(img, href, label, extra) {
    return img + '<a href="#' + esc(href) + '">' + esc(label) + "</a>" + (extra || "");
  }
  function tagOf(bt) {
    return bt === "mvp" ? ' <span class="db-chip db-mvp">MVP</span>' : bt === "boss" ? ' <span class="db-chip db-boss">Boss</span>' : "";
  }
  var ELEM = /^(\w+)/;
  function elemChip(e) {
    var base = (ELEM.exec(e) || [, ""])[1];
    return '<span class="db-chip db-el db-el-' + esc(base.toLowerCase()) + '">' + esc(e) + "</span>";
  }
  function itemJobs(r) {
    if (r[7] === "*") return ["All jobs"];
    return r[7] ? r[7].split(".").map(function (i) { return meta.itemJobs[+i]; }) : [];
  }
  function isMain(j) { return !/^Baby|^Super_Baby/.test(j.job) && !/\d$/.test(j.job); }

  var KINDS = {
    items: {
      index: "items.json",
      searchHint: "Item name or id, e.g. Elunium or 985",
      text: function (r) { return (r[0] + " " + r[1]).toLowerCase(); },
      filters: [
        { label: "Type", type: "select", get: function (r) { return r[2]; } },
        { label: "Sub-type", type: "select", get: function (r) { return r[3]; } },
        { label: "Equips on", type: "select", get: function (r) { return r[6] ? r[6].split("|") : []; } },
        { label: "Job", type: "select", get: function (r) { return r[7] === "*" ? meta.itemJobs : itemJobs(r); } },
        { label: "Slots", type: "select", get: function (r) { return r[2] === "Weapon" || r[2] === "Armor" ? String(r[4] || 0) : ""; } },
        { label: "Required level", type: "range", get: function (r) { return r[5]; } },
      ],
      cols: [
        { h: "Id", cell: function (r) { return r[0]; }, sort: function (r) { return r[0]; } },
        { h: "Name", cell: function (r) { return nameCell(pic("items", r[0], "ico"), r[0], r[1] + (r[4] ? " [" + r[4] + "]" : "")); }, sort: function (r) { return r[1]; } },
        { h: "Type", cell: function (r) { return esc(nice(r[2])) + (r[3] ? " <small>" + esc(nice(r[3])) + "</small>" : ""); }, sort: function (r) { return r[2] + r[3]; } },
        { h: "Level", cell: function (r) { return r[5] || ""; }, sort: function (r) { return r[5]; } },
        { h: "ATK", cell: function (r) { return r[8] || ""; }, sort: function (r) { return r[8]; } },
        { h: "MATK", cell: function (r) { return r[9] || ""; }, sort: function (r) { return r[9]; } },
        { h: "DEF", cell: function (r) { return r[10] || ""; }, sort: function (r) { return r[10]; } },
        { h: "Weight", cell: function (r) { return r[11] || ""; }, sort: function (r) { return r[11]; } },
      ],
    },
    monsters: {
      index: "mobs.json",
      searchHint: "Monster name or id, e.g. Baphomet or 1039",
      text: function (r) { return (r[0] + " " + r[1]).toLowerCase(); },
      filters: [
        { label: "Class", type: "select", get: function (r) { return r[7] === "mvp" ? "MVP" : r[7] === "boss" ? "Boss" : "Normal"; } },
        { label: "Race", type: "select", get: function (r) { return r[4]; } },
        { label: "Element", type: "select", get: function (r) { return (ELEM.exec(r[5]) || [, ""])[1]; } },
        { label: "Size", type: "select", get: function (r) { return r[6]; } },
        { label: "Spawns on map", type: "text", get: function (r) { return r[11] || ""; }, placeholder: "e.g. prt_fild08" },
        { label: "Level", type: "range", get: function (r) { return r[2]; } },
      ],
      cols: [
        { h: "Id", cell: function (r) { return r[0]; }, sort: function (r) { return r[0]; } },
        { h: "Name", cell: function (r) { return nameCell(pic("mobs", r[0], "mob-sm"), r[0], r[1], tagOf(r[7])); }, sort: function (r) { return r[1]; } },
        { h: "Level", cell: function (r) { return r[2]; }, sort: function (r) { return r[2]; } },
        { h: "HP", cell: function (r) { return num(r[3]); }, sort: function (r) { return r[3]; } },
        { h: "Base exp", cell: function (r) { return num(r[9]); }, sort: function (r) { return r[9]; } },
        { h: "Race", cell: function (r) { return esc(r[4]); }, sort: function (r) { return r[4]; } },
        { h: "Element", cell: function (r) { return elemChip(r[5]); }, sort: function (r) { return r[5]; } },
        { h: "Size", cell: function (r) { return esc(r[6]); }, sort: function (r) { return r[6]; } },
      ],
    },
    skills: {
      index: "skills.json",
      searchHint: "Skill name or id, e.g. Storm Gust",
      text: function (s) { return (s.id + " " + s.name + " " + s.aegis).toLowerCase(); },
      filters: [
        { label: "Job", type: "select", get: function (s) { return s.jobs.map(nice); } },
        { label: "Type", type: "select", get: function (s) { return s.type; } },
        { label: "Target", type: "select", get: function (s) { return nice(s.target); } },
        { label: "Element", type: "select", get: function (s) { return typeof s.Element === "string" ? s.Element : ""; } },
        { label: "Max level", type: "range", get: function (s) { return s.max; } },
      ],
      cols: [
        { h: "Id", cell: function (s) { return s.id; }, sort: function (s) { return s.id; } },
        { h: "Skill", cell: function (s) { return nameCell(pic("skills", s.id, "ico"), s.aegis, s.name, " <small>" + esc(s.aegis) + "</small>"); }, sort: function (s) { return s.name; } },
        { h: "Max level", cell: function (s) { return s.max; }, sort: function (s) { return s.max; } },
        { h: "Type", cell: function (s) { return esc(s.type); }, sort: function (s) { return s.type; } },
        { h: "Element", cell: function (s) { return typeof s.Element === "string" ? elemChip(s.Element) : ""; }, sort: function (s) { return typeof s.Element === "string" ? s.Element : ""; } },
        { h: "Learned by", cell: function (s) { return s.jobs.slice(0, 4).map(function (j) { return esc(nice(j)); }).join(", ") + (s.jobs.length > 4 ? " +" + (s.jobs.length - 4) : ""); }, sort: function (s) { return s.jobs[0] || "~"; } },
      ],
    },
    npcs: {
      index: "npcs.json",
      searchHint: "NPC name or map, e.g. Kafra or prontera",
      text: function (r) { return (r[1] + " " + r[2]).toLowerCase(); },
      filters: [
        { label: "Does", type: "select", get: function (r) { return r[6] ? r[6].split("|") : []; } },
        { label: "Content", type: "select", get: function (r) { return r[7]; } },
        { label: "Map", type: "text", get: function (r) { return r[2]; }, placeholder: "e.g. prontera" },
      ],
      cols: [
        { h: "NPC", cell: function (r) { return nameCell(npcPic(r[5], "mob-sm"), r[0], r[1], r[8] > 1 ? " <small>+" + (r[8] - 1) + " more places</small>" : ""); }, sort: function (r) { return r[1]; } },
        { h: "Where", cell: function (r) { return where(r[2], r[3], r[4]); }, sort: function (r) { return r[2]; } },
        { h: "Does", cell: function (r) { return r[6] ? chips(r[6].split("|")) : ""; }, sort: function (r) { return r[6] || "~"; } },
        { h: "Content", cell: function (r) { return esc(r[7]); }, sort: function (r) { return r[7]; } },
      ],
    },
    enchants: {
      index: "enchants.json",
      searchHint: "Item name, e.g. Gray Wolf Suits or Shadow Mix Recipe",
      text: function (r) { return (r[2] + " " + r[3] + " " + r[1] + " " + (r[6] || "")).toLowerCase(); },
      filters: [
        { label: "Kind", type: "select", get: function (r) { return r[1]; } },
        { label: "Minimum refine", type: "range", get: function (r) { return r[5]; } },
      ],
      cols: [
        { h: "For", cell: function (r) { return nameCell(pic("items", r[2], "ico"), r[0], r[3], r[1] === "Enchant" && r[4] > 1 ? " <small>+" + (r[4] - 1) + " more items</small>" : r[0][0] === "G" && r[4] ? " <small>" + r[4] + " items</small>" : ""); }, sort: function (r) { return r[3]; } },
        { h: "Kind", cell: function (r) { return '<span class="db-chip">' + esc(r[1]) + "</span>"; }, sort: function (r) { return r[1]; } },
        { h: "Items", cell: function (r) { return r[4]; }, sort: function (r) { return r[4]; } },
        { h: "Min. refine", cell: function (r) { return r[5] ? "+" + r[5] : ""; }, sort: function (r) { return r[5]; } },
      ],
    },
    jobs: {
      index: "jobs.json",
      searchHint: "Job name, e.g. Arch Bishop",
      text: function (j) { return j.job.toLowerCase().replace(/_/g, " "); },
      filters: [
        { label: "Show", type: "select", def: "Main jobs", get: function (j) { return /^Baby|^Super_Baby/.test(j.job) ? "Baby jobs" : /\d$/.test(j.job) ? "Mounted / alternate" : "Main jobs"; } },
        { label: "Comes from", type: "select", get: function (j) { return j.inherit.map(nice); } },
        { label: "Max base level", type: "range", get: function (j) { return j.maxBase || 0; } },
      ],
      cols: [
        { h: "Job", cell: function (j) { return nameCell("", j.job, nice(j.job)); }, sort: function (j) { return j.job; } },
        { h: "Comes from", cell: function (j) { return j.inherit.map(function (x) { return esc(nice(x)); }).join(", "); }, sort: function (j) { return j.inherit.length; } },
        { h: "Max level", cell: function (j) { return (j.maxBase || "") + (j.maxJob ? " / " + j.maxJob : ""); }, sort: function (j) { return j.maxBase || 0; } },
        { h: "Skills", cell: function (j) { return j.tree.length; }, sort: function (j) { return j.tree.length; } },
      ],
    },
  };

  function asList(v) { return Array.isArray(v) ? v : v === "" || v == null ? [] : [v]; }

  function listView(root, kind) {
    var K = KINDS[kind];
    root.innerHTML = '<p class="db-loading">Loading…</p>';
    return get(K.index).then(function (rows) {
      var state = root._state;
      if (!state) {
        state = root._state = { q: "", f: {}, sort: 0, dir: 1, shown: 100 };
        K.filters.forEach(function (f, i) { if (f.def) state.f[i] = f.def; });
      }
      var h = '<form class="db-bar" role="search"><input type="search" class="db-q" placeholder="' + esc(K.searchHint || "Search by name or id") +
        '" aria-label="Search"><button type="submit" class="md-button md-button--primary db-go">Search</button></form>' +
        '<div class="db-filters">';
      K.filters.forEach(function (f, i) {
        h += '<label class="db-filter"><span>' + esc(f.label) + "</span>";
        if (f.type === "select") {
          var counts = {};
          rows.forEach(function (r) { asList(f.get(r)).forEach(function (v) { counts[v] = (counts[v] || 0) + 1; }); });
          h += '<select data-i="' + i + '"><option value="">Any</option>' + Object.keys(counts).sort(function (a, b) {
            return isNaN(a) || isNaN(b) ? a.localeCompare(b) : a - b;
          }).map(function (o) { return '<option value="' + esc(o) + '">' + esc(nice(o)) + " (" + num(counts[o]) + ")</option>"; }).join("") + "</select>";
        } else if (f.type === "range") {
          h += '<span class="db-range"><input type="number" inputmode="numeric" data-i="' + i + '" data-end="min" placeholder="min" aria-label="' + esc(f.label) + ' from">' +
            '<span>to</span><input type="number" inputmode="numeric" data-i="' + i + '" data-end="max" placeholder="max" aria-label="' + esc(f.label) + ' to"></span>';
        } else {
          h += '<input type="search" data-i="' + i + '" placeholder="' + esc(f.placeholder || "") + '">';
        }
        h += "</label>";
      });
      h += '<button type="button" class="db-reset">Clear filters</button></div>' +
        '<p class="db-count"></p><div class="db-list"></div><p><button class="md-button db-more">Show more</button></p>';
      root.innerHTML = h;

      var q = root.querySelector(".db-q");
      q.value = state.q;
      root.querySelectorAll("[data-i]").forEach(function (el) {
        var i = +el.getAttribute("data-i"), end = el.getAttribute("data-end"), v = state.f[i];
        el.value = end ? (v && v[end] != null ? v[end] : "") : (v || "");
      });

      function matches(r) {
        for (var i = 0; i < K.filters.length; i++) {
          var f = K.filters[i], want = state.f[i];
          if (want == null || want === "") continue;
          var v = f.get(r);
          if (f.type === "select") { if (asList(v).indexOf(want) < 0) return false; }
          else if (f.type === "range") {
            if (want.min != null && want.min !== "" && !(v >= +want.min)) return false;
            if (want.max != null && want.max !== "" && !(v <= +want.max)) return false;
          } else if (String(v).toLowerCase().indexOf(want.toLowerCase()) < 0) return false;
        }
        return true;
      }
      function draw() {
        var words = state.q.toLowerCase().split(/\s+/).filter(Boolean);
        var hits = rows.filter(function (r) {
          var t = K.text(r);
          return words.every(function (w) { return t.indexOf(w) >= 0; }) && matches(r);
        });
        var key = K.cols[state.sort].sort, dir = state.dir;
        hits.sort(function (a, b) {
          var x = key(a), y = key(b);
          return (typeof x === "string" ? x.localeCompare(y) : x - y) * dir;
        });
        root.querySelector(".db-count").textContent = num(hits.length) + " found";
        var head = K.cols.map(function (c, i) {
          return '<button type="button" class="db-sort' + (i === state.sort ? " on" : "") + '" data-col="' + i + '">' + c.h +
            (i === state.sort ? (dir > 0 ? " ▲" : " ▼") : "") + "</button>";
        });
        root.querySelector(".db-list").innerHTML = table(head, hits.slice(0, state.shown).map(function (r) {
          return K.cols.map(function (c) { return c.cell(r); });
        }));
        root.querySelector(".db-more").style.display = hits.length > state.shown ? "" : "none";
      }
      var t;
      q.addEventListener("input", function () { clearTimeout(t); t = setTimeout(function () { state.q = q.value; state.shown = 100; draw(); }, 120); });
      root.querySelector(".db-bar").addEventListener("submit", function (e) {
        e.preventDefault(); clearTimeout(t); state.q = q.value; state.shown = 100; draw();
        root.querySelector(".db-count").scrollIntoView({ block: "nearest", behavior: "smooth" });
      });
      root.querySelector(".db-filters").addEventListener("input", function (e) {
        var el = e.target, i = el.getAttribute("data-i");
        if (i == null) return;
        var end = el.getAttribute("data-end");
        if (end) { state.f[i] = state.f[i] || {}; state.f[i][end] = el.value; } else state.f[i] = el.value;
        clearTimeout(t); t = setTimeout(function () { state.shown = 100; draw(); }, 120);
      });
      root.querySelector(".db-reset").addEventListener("click", function () {
        root._state = null; listView(root, kind);
      });
      root.querySelector(".db-list").addEventListener("click", function (e) {
        var b = e.target.closest && e.target.closest(".db-sort");
        if (!b) return;
        var c = +b.getAttribute("data-col");
        if (c === state.sort) state.dir = -state.dir; else { state.sort = c; state.dir = c === 0 || c === 1 ? 1 : -1; }
        draw();
      });
      root.querySelector(".db-more").addEventListener("click", function () { state.shown += 200; draw(); });
      draw();
    });
  }

  /* ------------------------------------------------------------ detail views */

  // Item effects come as plain-English lines (tools/describe.py): a string, [heading, [lines]] for a condition,
  // or {c: script} for something written only as code. Strings carry links as ⟦i:ID|Name⟧, ⟦m:ID|Name⟧, ⟦k:AEGIS|Name⟧.
  function fxText(t) {
    return esc(t).replace(/⟦([imk]):([^|⟧]*)\|([^⟧]*)⟧/g, function (_, k, id, name) {
      var kind = k === "i" ? "items" : k === "m" ? "monsters" : "skills";
      return (k === "i" ? pic("items", id, "ico") : "") + '<a href="' + page(kind) + "#" + id + '">' + name + "</a>";
    });
  }
  function fxList(lines) {
    return '<ul class="db-fx">' + lines.map(function (x) {
      if (Array.isArray(x)) return "<li>" + fxText(x[0]) + ":" + fxList(x[1]) + "</li>";
      if (x && typeof x === "object") return '<li><code class="db-fx-code">' + esc(x.c) + "</code></li>";
      return "<li>" + fxText(x) + "</li>";
    }).join("") + "</ul>";
  }
  function scriptBox(script) {
    return '<details class="db-script-box"><summary>Show script</summary><pre class="db-script"><code>' + esc(script) + "</code></pre></details>";
  }

  function back(kind) { return '<p><a href="#" class="db-back">← All ' + (kind === "npcs" ? "NPCs" : kind === "enchants" ? "enchants" : kind) + "</a></p>"; }

  function itemView(root, id) {
    return Promise.all([get("items.json"), get("mobs.json"), get("items/" + Math.floor(id / meta.chunk) + ".json"), get("npcs.json")]).then(function (a) {
      var items = byId(a[0]), mobs = byId(a[1]), d = a[2][id], r = items[id], npcs = byId(a[3]);
      if (!r || !d) { root.innerHTML = back("items") + "<p>No item with id " + esc(id) + ".</p>"; return; }
      var h = back("items") + pic("items", id, "db-pic") + "<h2>" + esc(r[1]) + (r[4] ? " [" + r[4] + "]" : "") + ' <small class="iid">' + id + "</small></h2>";
      h += facts([
        ["Type", esc(nice(r[2])) + (d.SubType ? " / " + esc(nice(d.SubType)) : "")],
        ["Aegis name", "<code>" + esc(d.AegisName) + "</code>"],
        ["Weight", d.Weight != null ? +(d.Weight / 10).toFixed(1) : ""],
        ["Attack", d.Attack != null ? num(d.Attack) : ""], ["Magic attack", d.MagicAttack != null ? num(d.MagicAttack) : ""],
        ["Defense", d.Defense != null ? num(d.Defense) : ""], ["Range", d.Range || ""],
        ["Weapon level", d.WeaponLevel || ""], ["Armor level", d.ArmorLevel || ""],
        ["Required level", d.EquipLevelMin ? d.EquipLevelMin + (d.EquipLevelMax ? " to " + d.EquipLevelMax : "") : ""],
        ["Equips on", d.Locations ? chips(d.Locations) : ""],
        ["Refinable", d.Refineable ? "Yes" : r[2] === "Weapon" || r[2] === "Armor" ? "No" : ""],
        ["Gender", d.Gender && d.Gender !== "Both" ? esc(d.Gender) : ""],
        ["Buy / sell", d.Buy || d.Sell ? num(d.Buy || (d.Sell || 0) * 2) + " / " + num(d.Sell || Math.floor((d.Buy || 0) / 2)) + " z" : ""],
        ["Trade limits", d.Trade ? chips(d.Trade) : ""],
      ]);
      if (d.Jobs) h += "<h3>Jobs</h3><p>" + (d.Jobs.indexOf("All") >= 0 ? "All jobs" : chips(d.Jobs)) + (d.Classes ? "<br><small>Classes: " + esc(d.Classes.map(nice).join(", ")) + "</small>" : "") + "</p>";
      [["Script", "fx", "Effect"], ["EquipScript", "fxEquip", "When equipped"], ["UnEquipScript", "fxUnequip", "When taken off"]].forEach(function (s) {
        if (!d[s[0]]) return;
        h += "<h3>" + s[2] + "</h3>" + (d[s[1]] && d[s[1]].length ? fxList(d[s[1]]) : "<p><small>No effect on stats (looks only).</small></p>") + scriptBox(d[s[0]]);
      });
      if (d.combos) h += "<h3>Set bonuses</h3>" + d.combos.map(function (c) {
        var names = c[0].map(function (i) { return i == id ? "<strong>" + esc(items[i] ? items[i][1] : "Item " + i) + "</strong>" : itemLink(i, items); }).join(" + ");
        return "<p>Worn together: " + names + "</p>" + (c[1].length ? fxList(c[1]) : "") + (c[2] ? scriptBox(c[2]) : "");
      }).join("");
      if (d.drops) h += "<h3>Dropped by</h3>" + table(["Monster", "Level", "Chance"], d.drops.map(function (x) {
        var m = mobs[x[0]];
        return [mobLink(x[0], mobs) + (x[2] === "mvp" ? ' <span class="db-chip db-mvp">MVP reward</span>' : ""), m ? m[2] : "", pct(x[1])];
      }));
      if (d.shops) h += "<h3>Sold by</h3>" + table(["NPC", "Where", "Price"], d.shops.map(function (s) {
        var loc = s[1] ? where(s[1], s[2], s[3]) : "<small>opened from another NPC</small>";
        var price;
        if (s[5] && s[5].barter) {
          price = s[5].barter.map(function (c) { return c[0] === "zeny" ? num(c[1]) + " z" : c[1] + " × " + itemLink(c[0], items); }).join("<br>");
        } else if (/^item:/.test(s[5])) {
          price = num(s[4]) + " × " + itemLink(+s[5].slice(5), items);
        } else {
          price = num(s[4]) + " " + esc(s[5] === "Zeny" ? "z" : s[5]);
        }
        return [s[6] ? npcLink(s[6], npcs) : esc(s[0]), loc, price];
      }));
      if (d.givenBy) h += "<h3>Given by NPC</h3><p><small>These NPCs hand out this item, for example as a quest reward or exchange.</small></p>" +
        table(["NPC", "Where"], d.givenBy.map(function (n) { var x = npcs[n]; return [npcLink(n, npcs), x ? where(x[2], x[3], x[4]) : ""]; }));
      if (d.enchant) h += '<div class="db-enchanting"></div>';
      if (d.boxes) h += "<h3>Found in</h3>" + table(["Box", "Chance"], d.boxes.map(function (b) { return [itemLink(b[0], items), b[1] == null ? "always" : b[1] + "%"]; }));
      if (d.contains) h += "<h3>Contents</h3>" + table(["Item", "Amount", "Chance"], d.contains.map(function (b) { return [itemLink(b[0], items), b[2], b[1] == null ? "always" : b[1] + "%"]; }));
      root.innerHTML = h;
      if (d.enchant) return enchantLinks(d.enchant).then(function (names) {
        var e = d.enchant, link = function (k) { return '<a href="' + page("enchants") + "#" + k + '">' + esc(names[k] || k) + "</a>"; };
        var parts = [["enchantTarget", "Can be enchanted at"], ["enchantResult", "Is an enchant from"], ["enchantMaterial", "Used to enchant at"],
          ["laphineItem", "Opens Laphine"], ["laphineReq", "Used as material in"], ["laphineReward", "Comes out of Laphine"], ["laphineTarget", "Can be upgraded with"]];
        root.querySelector(".db-enchanting").innerHTML = "<h3>Enchanting</h3>" + facts(parts.map(function (p) { return [p[1], e[p[0]] ? e[p[0]].map(link).join("<br>") : ""]; }));
      });
    });
  }

  // {enchant key: name} for links: NPC enchanters by their guide's title, enchant systems by the NPC that opens them.
  function enchantLinks() {
    return Promise.all([get("enchants.json"), get("enchants_detail.json"), get("npcs.json")]).then(function (a) {
      var npcs = byId(a[2]), out = {};
      a[0].forEach(function (r) {
        var d = a[1][r[0]] || {}, n = d.npcs && d.npcs.length && npcs[d.npcs[0]];
        out[r[0]] = r[0][0] === "G" ? r[3] : r[0][0] === "E" ? (n ? n[1] + ": " : "") + "enchant system " + r[0].slice(1) + (r[4] > 1 ? " (" + r[3] + " and " + (r[4] - 1) + " more)" : " (" + r[3] + ")")
          : r[1] + ": " + r[3];
      });
      return out;
    });
  }
  function guideUrl(p) { return BASE + p.replace(/\.md$/, meta.dirUrls ? "/" : ".html").replace(/index\/$/, ""); }

  function mobView(root, id) {
    return Promise.all([get("items.json"), get("mobs.json"), get("mobs/" + Math.floor(id / meta.chunk) + ".json")]).then(function (a) {
      var items = byId(a[0]), mobs = byId(a[1]), d = a[2][id], r = mobs[id];
      if (!r || !d) { root.innerHTML = back("monsters") + "<p>No monster with id " + esc(id) + ".</p>"; return; }
      var s = d.stats;
      var tag = r[7] === "mvp" ? ' <span class="db-chip db-mvp">MVP</span>' : r[7] === "boss" ? ' <span class="db-chip">Boss</span>' : "";
      var h = back("monsters") + pic("mobs", id, "db-pic") + "<h2>" + esc(r[1]) + ' <small class="iid">' + id + "</small>" + tag + "</h2>";
      h += facts([
        ["Level", s.Level], ["HP", num(s.Hp)], ["Base / job exp", num(s.BaseExp) + " / " + num(s.JobExp)],
        ["MVP exp", s.MvpExp ? num(s.MvpExp) : ""],
        ["Attack", num(s.Attack) + (s.Attack2 ? " ~ " + num(s.Attack + s.Attack2) : "")],
        ["Def / MDef", num(s.Defense) + " / " + num(s.MagicDefense)],
        ["Res / MRes", s.Resistance || s.MagicResistance ? num(s.Resistance) + " / " + num(s.MagicResistance) : ""],
        ["Race", esc(r[4]) + (d.racegroups.length ? " <small>(" + esc(d.racegroups.map(nice).join(", ")) + ")</small>" : "")],
        ["Element", elemChip(r[5])], ["Size", esc(r[6])],
        ["Stats", ["Str", "Agi", "Vit", "Int", "Dex", "Luk"].map(function (k) { return k.toUpperCase() + " " + s[k]; }).join(" · ")],
        ["Attack range", s.AttackRange], ["Walk speed", s.WalkSpeed], ["Attack delay", s.AttackDelay ? s.AttackDelay + " ms" : ""],
        ["Behaviour", d.modes.filter(function (m) { return m !== "Mvp"; }).length ? chips(d.modes.filter(function (m) { return m !== "Mvp"; })) : ""], ["Aegis name", "<code>" + esc(d.aegis) + "</code>"],
      ]);
      if (d.drops.length) h += "<h3>Drops</h3>" + table(["Item", "Chance", ""], d.drops.map(function (x) {
        return [itemLink(x[0], items), pct(x[1]), (x[2] === "mvp" ? '<span class="db-chip db-mvp">MVP reward</span> ' : "") + (x[3] ? "<small>can't be stolen</small>" : "")];
      }));
      h += "<h3>Where to find</h3>" + (d.spawns.length ? table(["Map", "Amount"], d.spawns.map(function (sp) { return ["<code>" + esc(sp[0]) + "</code>", sp[1]]; }))
        : "<p>No permanent spawn. It appears in instances, events or by summon.</p>");
      root.innerHTML = h;
    });
  }

  function perLevel(v, unit) {
    if (!Array.isArray(v)) return typeof v === "object" ? esc(JSON.stringify(v)) : esc(unit === "ms" ? secs(v) : v);
    var keys = v.length && Object.keys(v[0]).filter(function (k) { return k !== "Level"; });
    if (!keys || keys.length !== 1) return esc(JSON.stringify(v));
    return v.map(function (e) { var x = e[keys[0]]; return "Lv " + e.Level + ": " + esc(unit === "ms" ? secs(x) : x); }).join("<br>");
  }

  function skillView(root, key) {
    return Promise.all([skillsData(), get("items.json")]).then(function (a) {
      var skills = a[0], items = byId(a[1]);
      var s = skills.byAegis[key] || skills.byId[key];
      if (!s) { root.innerHTML = back("skills") + "<p>No skill " + esc(key) + ".</p>"; return; }
      var h = back("skills") + pic("skills", s.id, "db-pic") + "<h2>" + esc(s.name) + ' <small class="iid">' + esc(s.aegis) + " · " + s.id + "</small></h2>";
      h += facts([
        ["Max level", s.max], ["Type", esc(s.type)], ["Target", esc(nice(s.target))], ["Element", s.Element ? perLevel(s.Element) : ""],
        ["Range", s.Range != null ? perLevel(s.Range) : ""], ["Hits", s.HitCount ? perLevel(s.HitCount) : ""],
        ["Area", s.SplashArea ? perLevel(s.SplashArea) : ""],
        ["SP cost", s.SpCost ? perLevel(s.SpCost) : ""], ["HP cost", s.HpCost ? perLevel(s.HpCost) : ""], ["AP cost", s.ApCost ? perLevel(s.ApCost) : ""],
        ["Zeny cost", s.ZenyCost ? perLevel(s.ZenyCost) : ""],
        ["Variable cast", s.CastTime ? perLevel(s.CastTime, "ms") : ""], ["Fixed cast", s.FixedCastTime ? perLevel(s.FixedCastTime, "ms") : ""],
        ["After-cast delay", s.AfterCastActDelay ? perLevel(s.AfterCastActDelay, "ms") : ""], ["Cooldown", s.Cooldown ? perLevel(s.Cooldown, "ms") : ""],
        ["Duration", s.Duration1 ? perLevel(s.Duration1, "ms") : ""], ["Second duration", s.Duration2 ? perLevel(s.Duration2, "ms") : ""],
        ["Needs weapon", s.Weapon ? chips(s.Weapon) : ""], ["Needs state", s.State ? esc(nice(s.State)) : ""],
        ["Items used", s.ItemCost ? s.ItemCost.map(function (c) { return c[1] + " × " + itemLink(c[0], items) + (c[2] ? " <small>(Lv " + c[2] + ")</small>" : ""); }).join("<br>") : ""],
      ]);
      if (s.jobs.length) h += "<h3>Learned by</h3><p>" + s.jobs.map(jobLink).join(", ") + "</p>";
      root.innerHTML = h;
    });
  }

  function npcView(root, id) {
    return Promise.all([get("npcs.json"), get("items.json"), get("npcs/" + Math.floor(id / meta.chunk) + ".json")]).then(function (a) {
      var npcs = byId(a[0]), items = byId(a[1]), d = a[2][id], r = npcs[id];
      if (!r || !d) { root.innerHTML = back("npcs") + "<p>No NPC with id " + esc(id) + ".</p>"; return; }
      var h = back("npcs") + npcPic(r[5], "db-pic") + "<h2>" + esc(r[1]) + "</h2>";
      h += facts([
        ["Where", d.locs.slice(0, 1).map(function (l) { return where(l[0], l[1], l[2]); }).join("")],
        ["Also at", d.locs.length > 1 ? d.locs.slice(1, 40).map(function (l) { return where(l[0], l[1], l[2]); }).join("<br>") + (d.locs.length > 41 ? "<br>…" : "") : ""],
        ["Does", r[6] ? chips(r[6].split("|")) : ""],
        ["Content", esc(r[7])],
        ["Script", "<code>" + esc(d.file) + "</code>"],
      ]);
      if (d.page) h += '<p><a class="md-button" href="' + guideUrl(d.page) + '">Full guide for this NPC</a></p>';
      if (d.says) h += "<h3>Says</h3><blockquote>" + d.says.map(esc).join("<br>") + "</blockquote>";
      if (d.menu) h += "<h3>Menu options</h3><p>" + chips(d.menu) + "</p>";
      if (d.sells) h += "<h3>Sells</h3>" + table(["Item", "Price"], d.sells.map(function (s) {
        var price = /^item:/.test(s[2]) ? num(s[1]) + " × " + itemLink(+s[2].slice(5), items) : num(s[1]) + " " + esc(s[2] === "Zeny" ? "z" : s[2]);
        return [itemLink(s[0], items), price];
      }));
      if (d.barter) h += "<h3>Trades</h3>" + table(["Item", "Costs"], d.barter.map(function (b) {
        return [itemLink(b[0], items), b[1].map(function (c) { return c[0] === "zeny" ? num(c[1]) + " z" : c[1] + " × " + itemLink(c[0], items); }).join("<br>")];
      }));
      if (d.gives) h += "<h3>Gives</h3><p><small>Items this NPC's script can hand out.</small></p>" + table(["Item"], d.gives.map(function (i) { return [itemLink(i, items)]; }));
      if (d.takes) h += "<h3>Takes</h3><p><small>Items this NPC's script can take from you.</small></p>" + table(["Item"], d.takes.map(function (i) { return [itemLink(i, items)]; }));
      if (d.quests) h += "<h3>Quests</h3>" + table(["Quest", "Id"], d.quests.map(function (q) { return [esc(q[1] || "Quest"), q[0]]; }));
      if (d.enchants || d.enchantGuide) h += "<h3>Enchanting</h3><p>" + (d.enchantGuide ? ['<a href="' + page("enchants") + "#" + d.enchantGuide + '">What this NPC enchants</a>'] : [])
        .concat((d.enchants || []).map(function (e) { return '<a href="' + page("enchants") + "#E" + e + '">Enchant system ' + e + "</a>"; })).join("<br>") + "</p>";
      if (d.instances) h += "<h3>Instances</h3><p>" + chips(d.instances) + "</p>";
      if (d.warps) h += "<h3>Can warp you to</h3><p>" + d.warps.map(function (m) { return "<code>" + esc(m) + "</code>"; }).join(" ") + "</p>";
      root.innerHTML = h;
    });
  }

  function costs(price, mats, items) {
    var out = (mats || []).map(function (m) { return m[1] + " × " + itemLink(m[0], items); });
    if (price) out.push(num(price) + " z");
    return out.join("<br>") || "free";
  }
  function enchantView(root, key) {
    return Promise.all([get("enchants_detail.json"), get("items.json"), get("npcs.json")]).then(function (a) {
      var d = a[0][key], items = byId(a[1]), npcs = byId(a[2]);
      if (!d) { root.innerHTML = back("enchants") + "<p>No enchant entry " + esc(key) + ".</p>"; return; }
      var h = back("enchants");
      var refine = function (lo, hi) { return lo || hi != null ? "+" + (lo || 0) + (hi != null ? " to +" + hi : " or higher") : ""; };
      var npcList = function (ids) { return ids.map(function (n) { var x = npcs[n]; return npcLink(n, npcs) + (x ? " " + where(x[2], x[3], x[4]) : ""); }).join("<br>"); };
      var guide = d.page ? '<p><a class="md-button" href="' + guideUrl(d.page) + '">Read the full guide</a>' +
        (d.guide ? ' <a class="md-button" href="#' + esc(d.guide) + '">Everything this NPC enchants</a>' : "") + "</p>" : "";
      if (key[0] === "G") {
        h += "<h2>" + esc(d.title) + "</h2>" + guide;
        h += "<p><small>This enchanter is an NPC script, so the chances and costs are on its guide page. " +
          "The lists below are the items the guide mentions.</small></p>";
        h += facts([["NPC", npcList(d.npcs)]]);
        h += "<h3>Items it enchants</h3>" + (table(["Item"], d.targets.map(function (t) { return [itemLink(t, items)]; })) || "<p>See the guide.</p>");
        if (d.results.length) h += "<h3>Enchants it can add</h3>" + table(["Enchant"], d.results.map(function (t) { return [itemLink(t, items)]; }));
        if (d.mats.length) h += "<h3>Materials and other items</h3>" + table(["Item"], d.mats.map(function (t) { return [itemLink(t, items)]; }));
      } else if (key[0] === "E") {
        h += "<h2>Enchant system " + esc(key.slice(1)) + "</h2>" + guide;
        h += facts([
          ["Opened by", npcList(d.npcs)],
          ["Needs refine", d.minRefine ? "+" + d.minRefine + " or higher" : ""], ["Needs enchant grade", d.minGrade || ""],
          ["Slot order", d.order.length ? d.order.map(function (o) { return "slot " + o; }).join(" → ") : ""],
          ["Reset", d.reset ? (d.reset[0] / 1000) + "% success, costs " + costs(d.reset[1], d.reset[2], items) : "not possible"],
        ]);
        h += "<h3>Items you can enchant</h3>" + table(["Item"], d.targets.map(function (t) { return [itemLink(t, items)]; }));
        d.slots.forEach(function (sl) {
          h += "<h3>Slot " + sl.slot + "</h3>" + facts([["Cost per try", costs(sl.price, sl.mats, items)], ["Success", sl.chance / 1000 + "%"],
            ["Grade bonus", sl.bonus.length ? sl.bonus.map(function (b) { return "grade " + b[0] + ": +" + b[1] / 1000 + "%"; }).join(", ") : ""]]);
          sl.grades.forEach(function (g) {
            var total = g[1].reduce(function (t, x) { return t + x[1]; }, 0);
            h += (sl.grades.length > 1 ? "<h4>Enchant grade " + g[0] + "</h4>" : "") + table(["Enchant", "Chance"], g[1].map(function (x) {
              return [itemLink(x[0], items), total ? +(x[1] * 100 / total).toFixed(2) + "%" : ""];
            }));
          });
          if (sl.perfect.length) h += "<h4>Perfect enchant (pick one, always succeeds)</h4>" + table(["Enchant", "Cost"], sl.perfect.map(function (p) { return [itemLink(p[0], items), costs(p[1], p[2], items)]; }));
          if (sl.upgrades.length) h += "<h4>Upgrades</h4>" + table(["From", "To", "Cost"], sl.upgrades.map(function (u) { return [itemLink(u[0], items), itemLink(u[1], items), costs(u[2], u[3], items)]; }));
        });
      } else if (key[0] === "S") {
        h += pic("items", d.item, "db-pic") + "<h2>Laphine synthesis: " + esc((items[d.item] || [, "Item " + d.item])[1]) + "</h2>";
        h += "<p>Use " + itemLink(d.item, items) + " and hand in <b>" + d.count + "</b> of the items below" +
          (d.minRefine || d.maxRefine != null ? ", refined " + refine(d.minRefine, d.maxRefine) : "") + ". You get one item from the reward list.</p>";
        h += "<h3>Accepted items</h3>" + table(["Item", "Amount"], d.reqs.map(function (r) { return [itemLink(r[0], items), r[1]]; }));
        if (d.rewards.length) h += "<h3>Rewards</h3>" + table(["Item", "Amount", "Chance"], d.rewards.map(function (r) { return [itemLink(r[0], items), r[2], r[1] == null ? "always" : r[1] + "%"]; }));
      } else {
        h += pic("items", d.item, "db-pic") + "<h2>Laphine upgrade: " + esc((items[d.item] || [, "Item " + d.item])[1]) + "</h2>";
        h += facts([
          ["Use", itemLink(d.item, items)],
          ["Item must be refined", refine(d.minRefine, d.maxRefine)],
          ["Refine afterwards", d.resultRefine != null ? "+" + d.resultRefine : d.resultMin != null ? "+" + d.resultMin + " to +" + d.resultMax : "unchanged"],
          ["Needs random options", d.needOptions || ""], ["Cards", d.cards ? "kept" : "not allowed"],
        ]);
        if (d.options && d.options.length) h += "<h3>Random options added</h3>" + d.options.map(function (slot, i) {
          var total = slot.reduce(function (t, o) { return t + o[3]; }, 0);
          return "<h4>Option " + (i + 1) + "</h4>" + table(["Option", "Value", "Chance"], slot.map(function (o) {
            return [esc(o[0]), o[1] === o[2] ? o[1] : o[1] + " ~ " + o[2], total ? +(o[3] * 100 / total).toFixed(2) + "%" : ""];
          }));
        }).join("");
        h += "<h3>Items you can upgrade</h3>" + table(["Item"], d.targets.map(function (t) { return [itemLink(t, items)]; }));
      }
      root.innerHTML = h;
    });
  }

  function jobView(root, key) {
    return Promise.all([get("jobs.json"), skillsData()]).then(function (a) {
      var job = a[0].filter(function (j) { return j.job === key; })[0], skills = a[1];
      if (!job) { root.innerHTML = back("jobs") + "<p>No job " + esc(key) + ".</p>"; return; }
      var h = back("jobs") + "<h2>" + esc(nice(job.job)) + "</h2>";
      var bonus = Object.keys(job.bonus).map(function (k) { return k.toUpperCase() + " +" + job.bonus[k]; }).join(" · ");
      h += facts([
        ["Inherits skills from", job.inherit.map(jobLink).join(", ")],
        ["Max base / job level", (job.maxBase || "?") + " / " + (job.maxJob || "?")],
        ["HP / SP at max level", job.hp ? num(job.hp) + " / " + num(job.sp) : ""],
        ["Job bonus at max job level", bonus], ["Base weight limit", job.weight ? num(job.weight / 10) : ""],
      ]);
      h += "<h3>Skills</h3>" + table(["Skill", "Max level", "Requires"], job.tree.map(function (t) {
        return [skillLink(t[1], skills), t[2], t[3].map(function (r) { return skillLink(r[0], skills) + " " + r[1]; }).join(", ")];
      }));
      if (job.aspd) h += "<h3>Base ASPD by weapon</h3>" + table(["Weapon", "Base ASPD"], Object.keys(job.aspd).map(function (w) { return [esc(nice(w)), job.aspd[w]]; }));
      root.innerHTML = h;
    });
  }

  var DETAIL = { items: itemView, monsters: mobView, skills: skillView, npcs: npcView, enchants: enchantView, jobs: jobView };

  function route(root, kind) {
    var key = decodeURIComponent(location.hash.slice(1));
    var view = root.querySelector(".db-view") || root;
    var go = key ? DETAIL[kind](view, kind === "items" || kind === "monsters" || kind === "npcs" ? +key : key) : listView(view, kind);
    go.catch(function (e) { view.innerHTML = '<p class="db-loading">Could not load the database (' + esc(e.message) + ").</p>"; });
    if (key) window.scrollTo(0, root.getBoundingClientRect().top + window.scrollY - 80);
  }

  function start() {
    var root = document.querySelector(".db-app");
    if (!root) return;
    var kind = root.getAttribute("data-kind");
    root.innerHTML = '<div class="db-view"></div>';
    root.addEventListener("click", function (e) {
      if (e.target.closest && e.target.closest(".db-back")) { e.preventDefault(); history.pushState(null, "", location.pathname); route(root, kind); }
    });
    Promise.all([get("meta.json"), loadIcons(), loadNpcPics()]).then(function (a) {
      meta = a[0];
      route(root, kind);
      window.addEventListener("hashchange", function () { route(root, kind); });
      window.addEventListener("popstate", function () { route(root, kind); });
    }).catch(function (e) {
      root.innerHTML = '<p class="db-loading">Could not load the database (' + esc(e.message) + "). Try reloading the page.</p>";
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start); else start();
})();
