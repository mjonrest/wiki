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
    return '<a href="' + page("items") + "#" + id + '">' + esc(label) + '</a> <small class="iid">' + id + "</small>";
  }
  function mobLink(id, names) {
    var m = names && names[id];
    return '<a href="' + page("monsters") + "#" + id + '">' + esc(m ? m[1] : "Monster " + id) + '</a> <small class="iid">' + id + "</small>";
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

  var KINDS = {
    items: {
      index: "items.json",
      filter: function (r) { return r[2]; },
      head: ["Id", "Name", "Type", "Slots"],
      row: function (r) { return [r[0], '<a href="#' + r[0] + '">' + esc(r[1]) + "</a>", esc(nice(r[2])) + (r[3] ? " <small>" + esc(nice(r[3])) + "</small>" : ""), r[4] || ""]; },
      text: function (r) { return (r[0] + " " + r[1]).toLowerCase(); },
    },
    monsters: {
      index: "mobs.json",
      filter: function (r) { return r[7] === "mvp" ? "MVP" : r[7] === "boss" ? "Boss" : r[4]; },
      head: ["Id", "Name", "Level", "HP", "Race", "Element", "Size"],
      row: function (r) {
        var tag = r[7] === "mvp" ? ' <span class="db-chip db-mvp">MVP</span>' : r[7] === "boss" ? ' <span class="db-chip">Boss</span>' : "";
        return [r[0], '<a href="#' + r[0] + '">' + esc(r[1]) + "</a>" + tag, r[2], num(r[3]), esc(r[4]), esc(r[5]), esc(r[6])];
      },
      text: function (r) { return (r[0] + " " + r[1]).toLowerCase(); },
    },
    skills: {
      index: "skills.json",
      filter: function (s) { return s.type; },
      head: ["Id", "Skill", "Max level", "Type", "Learned by"],
      row: function (s) {
        return [s.id, '<a href="#' + esc(s.aegis) + '">' + esc(s.name) + "</a> <small>" + esc(s.aegis) + "</small>", s.max, esc(s.type),
          s.jobs.slice(0, 4).map(function (j) { return esc(nice(j)); }).join(", ") + (s.jobs.length > 4 ? " +" + (s.jobs.length - 4) : "")];
      },
      text: function (s) { return (s.id + " " + s.name + " " + s.aegis).toLowerCase(); },
    },
    jobs: {
      index: "jobs.json",
      filter: function (j) { return /^Baby|^Super_Baby/.test(j.job) ? "Baby" : /\d$/.test(j.job) ? "Mounted / alternate" : "Main"; },
      defaultFilter: "Main",
      head: ["Job", "Inherits from", "Max level", "Skills"],
      row: function (j) {
        return ['<a href="#' + esc(j.job) + '">' + esc(nice(j.job)) + "</a>", j.inherit.map(function (x) { return esc(nice(x)); }).join(", "),
          (j.maxBase || "") + (j.maxJob ? " / " + j.maxJob : ""), j.tree.length];
      },
      text: function (j) { return j.job.toLowerCase().replace(/_/g, " "); },
    },
  };

  function listView(root, kind) {
    var K = KINDS[kind];
    root.innerHTML = '<p class="db-loading">Loading…</p>';
    return get(K.index).then(function (rows) {
      var groups = {};
      rows.forEach(function (r) { var g = K.filter(r); if (g) groups[g] = (groups[g] || 0) + 1; });
      var opts = Object.keys(groups).sort();
      var state = root._state || (root._state = { q: "", f: K.defaultFilter || "", shown: 100 });
      root.innerHTML =
        '<div class="db-bar"><input type="search" class="db-q" placeholder="Search by name or id" aria-label="Search">' +
        '<select class="db-f" aria-label="Filter"><option value="">All (' + num(rows.length) + ")</option>" +
        opts.map(function (o) { return '<option value="' + esc(o) + '">' + esc(nice(o)) + " (" + num(groups[o]) + ")</option>"; }).join("") +
        '</select></div><p class="db-count"></p><div class="db-list"></div><p><button class="md-button db-more">Show more</button></p>';
      var q = root.querySelector(".db-q"), f = root.querySelector(".db-f");
      q.value = state.q; f.value = state.f;
      function draw() {
        var words = state.q.toLowerCase().split(/\s+/).filter(Boolean);
        var hits = rows.filter(function (r) {
          if (state.f && K.filter(r) !== state.f) return false;
          var t = K.text(r);
          return words.every(function (w) { return t.indexOf(w) >= 0; });
        });
        root.querySelector(".db-count").textContent = num(hits.length) + " found";
        root.querySelector(".db-list").innerHTML = table(K.head, hits.slice(0, state.shown).map(K.row));
        root.querySelector(".db-more").style.display = hits.length > state.shown ? "" : "none";
      }
      var t;
      q.addEventListener("input", function () { clearTimeout(t); t = setTimeout(function () { state.q = q.value; state.shown = 100; draw(); }, 120); });
      f.addEventListener("change", function () { state.f = f.value; state.shown = 100; draw(); });
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
      var h = back("items") + "<h2>" + esc(r[1]) + (r[4] ? " [" + r[4] + "]" : "") + ' <small class="iid">' + id + "</small></h2>";
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
      var h = back("monsters") + "<h2>" + esc(r[1]) + ' <small class="iid">' + id + "</small>" + tag + "</h2>";
      h += facts([
        ["Level", s.Level], ["HP", num(s.Hp)], ["Base / job exp", num(s.BaseExp) + " / " + num(s.JobExp)],
        ["MVP exp", s.MvpExp ? num(s.MvpExp) : ""],
        ["Attack", num(s.Attack) + (s.Attack2 ? " ~ " + num(s.Attack + s.Attack2) : "")],
        ["Def / MDef", num(s.Defense) + " / " + num(s.MagicDefense)],
        ["Res / MRes", s.Resistance || s.MagicResistance ? num(s.Resistance) + " / " + num(s.MagicResistance) : ""],
        ["Race", esc(r[4]) + (d.racegroups.length ? " <small>(" + esc(d.racegroups.map(nice).join(", ")) + ")</small>" : "")],
        ["Element", esc(r[5])], ["Size", esc(r[6])],
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
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start); else start();
})();
