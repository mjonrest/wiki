# Friday Dungeon

## Guide

A farming instance that is only open on **Fridays**. You kill undead in a copy of Geffen's dungeon to collect
{{ item(25235) }}. You then spend the stones on Marry Jay's accessory enchants, or feed them to a sculpture to try
to wake the {{ mob(3658) }}. There is no story and no end: you farm until the 2-hour instance timer runs out.

### Entering

- **Day:** **Friday** only (00:00 to 23:59 server time). On other days, Marry Jay just tells you the opening hours.
- **Level:** 130 or higher.
- **Party:** you must be in a party. The **party leader** talks to **Marry Jay** at `/navi gef_tower 57/170` and
  picks *Prepare Friday Memorial*. Then everyone picks *Enter Friday Memorial*.
- **Cooldown:** entering gives you *Time to Rest*. It ends at the next **04:00** server time.

### Difficulty

Inside, the party leader talks to **Marry Jay** at the entrance and picks a difficulty. This decides which version
of every monster spawns:

| Difficulty | Requirement | Monsters |
| --- | --- | --- |
| Lv 130–199 | Leader level 130+ | {{ mob(3660) }}, {{ mob(3662) }}, {{ mob(3664) }}, {{ mob(3666) }}; boss {{ mob(3658) }} |
| Lv 200+ | Leader level 200+ | {{ mob(3661) }}, {{ mob(3663) }}, {{ mob(3665) }}, {{ mob(3667) }}; boss {{ mob(3659) }} |

The harder mode also gives more stones from each chest (see below).

About 7 seconds after the choice, the map fills with **20 Nightmare, 30 Jakk, 30 Ghoul and 20 Drainliar**. Every
monster you kill comes back **10 seconds** later, so the map never runs dry.

!!! warning
    Monsters only count when they are killed normally. Taming or otherwise "processing" them does not add to the
    kill count.

### Getting Crafted Stones

| Source | Lv 130–199 | Lv 200+ |
| --- | --- | --- |
| **The Stranger**'s body (`1@md_gef 183/222`), *Investigate the body* (once per run) | 5–7 stones | 7–9 stones |
| **Treasure chest**, appears every **100 kills** | 5–7 stones | 7–9 stones |

- An announcement tells you when a chest appears. Chests take turns between the four corners of the map
  (`212/212`, `190/56`, `49/57`, `44/211`).
- Each chest **disappears after 3 minutes** if nobody opens it.
- The stones drop on the ground, so loot them quickly.

### Summoning the Lich Lord

Once the party has killed **100 monsters**, the **Bizzare Sculpture** at `1@md_gef 199/73` can be used. Put
**10× {{ item(25235) }}** into it:

- **10% chance:** the Lord of the Dead wakes and {{ mob(3658) }} (or {{ mob(3659) }} on Lv 200+) spawns at
  `210/110`. This can happen only once per run.
- **90% chance:** nothing happens. The stones are used up and the sculpture is gone for **5 minutes**.

### Accessory enchants (Amateur Collector)

The **Amateur Collector** next to Marry Jay (`/navi gef_tower 57/167`) enchants or resets an **equipped** accessory.
Each try costs **10× {{ item(25235) }} and 100,000 Zeny**. You need at least 10,000 free weight.

- Enchanting **removes any random options** on the accessory.
- Only accessories on her list can be enchanted. If an accessory is not on it, she will not take it.

**Normal accessories:** one enchant in the 4th slot, and it always works. Possible results:

| Enchant | Chance each |
| --- | --- |
| STR, INT, DEX, AGI or VIT +2 / +3 / +4 | 3.26% |
| HP +200, HP +400, DEF +6, DEF +12, SP +50, SP +100, MDEF +2, MDEF +4 | 3.26% |
| Max HP +1%, Max HP +2%, Max SP +1%, ATK +1%, MATK +1% | 2.17% |
| Sharp 2, Sharp 3, Fatal, Fatal 1, Expert Archer 1, Spell 3, Spell 4, Archbishop 1, Archbishop 2, Fighting Spirit 3, Fighting Spirit 4 | 1.09% |
| Sharp 4, Fatal 2, Spell 5, Fighting Spirit 5 | 0.54% |

**{{ item(28483) }}:** two enchants. You pick **Physical**, **Magical** or **Ranged** each time. The first enchant
goes in the 4th slot (stats), the second in the 3rd slot. Both always work.

| Type | 4th slot (first enchant) | 3rd slot (second enchant) |
| --- | --- | --- |
| Physical | STR, AGI or VIT: +3 / +4 at 13.3% each, +5 / +6 at 2.7%, +7 at 1.3% | Fighting Spirit 3–7, Sharp 1–5, ATK (Atk 1, ATK +2%, ATK +3%), Attack Speed 1–2 |
| Magical | INT, DEX or VIT: +3 / +4 at 13.3% each, +5 / +6 at 2.7%, +7 at 1.3% | Spell 3–7, Max SP +1%, Archbishop 1–4, MATK +1/2/3%, MATK 1–2 |
| Ranged | AGI, DEX or LUK: +3 / +4 at 13.3% each, +5 / +6 at 2.7%, +7 at 1.3% | Fatal, Fatal 1–4, Sharp 1–5, Expert Archer 1–3, Attack Speed 1–2 |

For the 3rd slot, the lowest grades are the most common (about 13% each) and the top grades are the rarest (about 2%).

**Reset:** removes the enchants (both of them on the Royal Guardian Ring). It works about **80%** of the time on
the Royal Guardian Ring and about **20%** on other accessories.

!!! danger
    If a reset fails, the **accessory is destroyed**.

{{ instance_page("friday-dungeon") }}
