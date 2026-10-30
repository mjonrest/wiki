---
hide:
  - navigation
  - toc
---

# Combat Power Simulator

Try out gear before you farm it. Pick your job, put items in every slot, and set refines, grades, cards,
enchants and random options: the simulator shows the **Combat Power (CP)** the build would have, the same number
the `@cp` command shows in game.

- Every item list is sorted by **how much CP it adds to your build right now**, so the best upgrade for a slot
  is at the top. Untick *Biggest CP gain first* to sort by name.
- Each slot shows how much CP it adds. Set bonuses switch on by themselves when all pieces are worn.
- **+ Compare** copies the build into a second one (Build B), so you can change one thing and see the difference.
- **Copy share link** gives a link to exactly this build (both builds when comparing). **Save** keeps builds in
  this browser.

<div class="cp-app"><p>Loading the simulator…</p></div>

## How CP is counted

CP adds up what your gear gives and weighs each stat by how much it helps in endgame: **1% more damage against
every target is 10 CP**. Physical and magic offense are counted apart and only the bigger one counts, so a
caster's MATK doesn't help a knight. Then the stats that help both, defense and utility are added.

- **Skill damage** counts only for skills your job has, more for 4th-job skills than for older ones. Large bonuses
  on one skill count a bit less each (+100% counts as 69, +500% as 179).
- **Cooldown and cast time** cuts count up to 3 seconds per skill. Variable cast, fixed cast and after-cast delay
  cuts count up to 100%. Fixed cast % from several items does not add up in game (the best one is used), so it
  doesn't here either.
- **Refine and grade** add weapon ATK/MATK and armor DEF just as the server does, plus the item's own refine bonuses.
- **Stat-based bonuses** (like "+1% per 10 STR") assume a level 275 character with 130 in the job's main stats,
  60 in the others and 100 in each trait.
- **Chance-based bonuses** (autobonus, "on attack, 5% chance…") count at their average uptime. In game, `@cp` counts
  them only while they are active, so the two numbers can differ for those items.
- **Left-hand weapons** (Shadow Cross, Shinkiro, Shiranui) count like right-hand ones here.

CP compares gear; it does not replace testing on a dummy. Use it to find upgrades and to see what an enchant or a
refine is worth.
