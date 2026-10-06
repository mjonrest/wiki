/* Database pages: a searchable list, and a detail view at #<id> (items, monsters, skills) or #<Job> (jobs).
   Data comes from db/data/*.json, written at build time by tools/gen_db.py. */
(function () {
  "use strict";
  var me = document.currentScript.src;
  var BASE = me.slice(0, me.indexOf("assets/db.js"));
  var DATA = BASE + "db/data/";
  var cache = {};
  var meta = null;

  function get(path) {
    if (!cache[path]) {
      cache[path] = fetch(DATA + path).then(function (r) {
        if (!r.ok) throw new Error(path + ": " + r.status);
        return r.json();
      });
    }
    return cache[path];
  }

  // Pictures: the copy saved in img/ (tools/fetch_images.py), then Divine Pride, then nothing.
  var REMOTE = { items: "https://static.divine-pride.net/images/items/item/", mobs: "https://static.divine-pride.net/images/mobs/png/" };
  var ONERR = "var a=this.getAttribute('data-alt');if(a){this.removeAttribute('data-alt');this.src=a}else this.remove()";
  function pic(kind, id, cls) {
    return '<img class="' + cls + '" src="' + BASE + "img/" + kind + "/" + id + '.png" data-alt="' + REMOTE[kind] + id +
      '.png" alt="" loading="lazy" onerror="' + ONERR + '">';
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
    return '<a href="' + page("skills") + "#" + esc(aegis) + '">' + esc(s ? s.name : nice(aegis)) + "</a>";
  }
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
        { h: "Skill", cell: function (s) { return nameCell("", s.aegis, s.name, " <small>" + esc(s.aegis) + "</small>"); }, sort: function (s) { return s.name; } },
        { h: "Max level", cell: function (s) { return s.max; }, sort: function (s) { return s.max; } },
        { h: "Type", cell: function (s) { return esc(s.type); }, sort: function (s) { return s.type; } },
        { h: "Element", cell: function (s) { return typeof s.Element === "string" ? elemChip(s.Element) : ""; }, sort: function (s) { return typeof s.Element === "string" ? s.Element : ""; } },
        { h: "Learned by", cell: function (s) { return s.jobs.slice(0, 4).map(function (j) { return esc(nice(j)); }).join(", ") + (s.jobs.length > 4 ? " +" + (s.jobs.length - 4) : ""); }, sort: function (s) { return s.jobs[0] || "~"; } },
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

  function back(kind) { return '<p><a href="#" class="db-back">← All ' + kind + "</a></p>"; }

  function itemView(root, id) {
    return Promise.all([get("items.json"), get("mobs.json"), get("items/" + Math.floor(id / meta.chunk) + ".json")]).then(function (a) {
      var items = byId(a[0]), mobs = byId(a[1]), d = a[2][id], r = items[id];
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
      [["Script", "Effect"], ["EquipScript", "On equip"], ["UnEquipScript", "On unequip"]].forEach(function (s) {
        if (d[s[0]]) h += "<h3>" + s[1] + '</h3><pre class="db-script"><code>' + esc(d[s[0]]) + "</code></pre>";
      });
      if (d.drops) h += "<h3>Dropped by</h3>" + table(["Monster", "Level", "Chance"], d.drops.map(function (x) {
        var m = mobs[x[0]];
        return [mobLink(x[0], mobs) + (x[2] === "mvp" ? ' <span class="db-chip db-mvp">MVP reward</span>' : ""), m ? m[2] : "", pct(x[1])];
      }));
      if (d.shops) h += "<h3>Sold by</h3>" + table(["NPC", "Where", "Price"], d.shops.map(function (s) {
        var where = s[1] ? "<code>" + esc(s[1]) + "</code> " + s[2] + ", " + s[3] : "<small>opened from another NPC</small>";
        var price;
        if (s[5] && s[5].barter) {
          price = s[5].barter.map(function (c) { return c[0] === "zeny" ? num(c[1]) + " z" : c[1] + " × " + itemLink(c[0], items); }).join("<br>");
        } else if (/^item:/.test(s[5])) {
          price = num(s[4]) + " × " + itemLink(+s[5].slice(5), items);
        } else {
          price = num(s[4]) + " " + esc(s[5] === "Zeny" ? "z" : s[5]);
        }
        return [esc(s[0]), where, price];
      }));
      if (d.boxes) h += "<h3>Found in</h3>" + table(["Box", "Chance"], d.boxes.map(function (b) { return [itemLink(b[0], items), b[1] == null ? "always" : b[1] + "%"]; }));
      if (d.contains) h += "<h3>Contents</h3>" + table(["Item", "Amount", "Chance"], d.contains.map(function (b) { return [itemLink(b[0], items), b[2], b[1] == null ? "always" : b[1] + "%"]; }));
      root.innerHTML = h;
    });
  }

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
      var h = back("skills") + "<h2>" + esc(s.name) + ' <small class="iid">' + esc(s.aegis) + " · " + s.id + "</small></h2>";
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

  var DETAIL = { items: itemView, monsters: mobView, skills: skillView, jobs: jobView };

  function route(root, kind) {
    var key = decodeURIComponent(location.hash.slice(1));
    var view = root.querySelector(".db-view") || root;
    var go = key ? DETAIL[kind](view, kind === "items" || kind === "monsters" ? +key : key) : listView(view, kind);
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
    get("meta.json").then(function (m) {
      meta = m;
      route(root, kind);
      window.addEventListener("hashchange", function () { route(root, kind); });
      window.addEventListener("popstate", function () { route(root, kind); });
    }).catch(function (e) {
      root.innerHTML = '<p class="db-loading">Could not load the database (' + esc(e.message) + "). Try reloading the page.</p>";
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start); else start();
})();
