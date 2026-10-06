# Devil's Tower

## Guide

Climb the tower where the Magic Swordman Thanatos holds back Demon Morocc. You go through three maps: help the
wounded, fight waves of {{ mob(2939) }}, break the Magic Seals Morocc is pulling towards himself, and finally,
with Loki's help, defeat the demon-blessed Lord Knight {{ mob(2942) }}. A treasure box with an Evil Slayer weapon
waits at the end.

### Entering

All three NPCs stand together in `dali02`:

1. **Every member** talks to **Historian Shep** at `/navi dali02 134/119` and volunteers. This gives you
   *Explore the tower*, which lets you enter for the next **1 hour 30 minutes**.
2. The **party leader** talks to **Magic Scholar Artie** at `/navi dali02 137/121` to activate the device.
3. Everyone enters through the **Dimensional Device** at `/navi dali02 141/120`.

- **Level:** 130 or higher.
- **Party:** required. The leader makes all the key story choices.
- **Re-entry:** you can go back in through the device until you leave the first room with Assassin Dewey. After
  that you cannot get back in.

### Cooldown and EXP reward

You get your EXP when you talk to **Historian Shep** after the run, and that is also when the cooldown starts. It
ends at the next **04:00** server time. How much EXP you get depends on how far you got:

| How far you got | Reward from Historian Shep |
| --- | --- |
| Cleared the tower | 450,000 Base EXP and 450,000 Job EXP |
| Broke the Magic Seals and followed Lucile upstairs, but did not finish | 300,000 Base EXP and 300,000 Job EXP |
| Got past the first stairs (moved on with Assassin Louie), but did not break the seals | 200,000 Base EXP and 200,000 Job EXP |
| Did not get that far, gave up, or let the 1h30 entry window run out | No EXP, but the cooldown still starts |

If you volunteered but want to back out before entering, Shep has a *Cancel my reservation* option.

### Walkthrough

**1. The infirmary (`1@tnm1`)**

1. A short scene plays when you arrive. Then the leader talks to **Officer Heim**.
2. **Healer Fama** hands out a {{ item(7641) }}, one at a time. Take a box to an **Injured Soldier**, use it (a
   10-second progress bar), then go back to Fama for another one. Heal all **7** soldiers.
3. The leader talks to **Lucile** for the next scene. Then talk to **Assassin Dewey** and pick *Move now* to go to
   the stairs. (After this you can no longer re-enter.)

**2. The stairs**

27 {{ mob(2939) }} spawn in waves over about 40 seconds, 9 of each of the three kinds. The hunting task Dewey gave
you asks for **7 of each kind** (21 in total). When it is done, talk to **Assassin Louie** at the end of the stairs to move on.

**3. The second stairs**

1. The leader talks to **Lucile** and picks *Can I help?*. This costs the leader **30% HP** and starts a
   **40-second** progress bar. Do not cancel it.
2. 16 Evil Shadows appear around **Huey**. Kill them all, then talk to Huey and pick *Move immediately* to go up
   to the battlefield (`1@tnm2`).

**4. Thanatos against Demon Morocc: the Magic Seals**

The leader talks to **Lucile**. After a short exchange, Demon Morocc calls in five {{ mob(2938) }}, one from each
direction (north, north-west, south-west, south-east and north-east).

- Each seal has **3,000,000 HP** and moves **one step closer to the centre about every 35 seconds**. It keeps the
  damage you have done to it, and every time it moves, 4 Evil Shadows spawn next to it.
- Every 20 seconds, lines of {{ mob(2960) }} burst out along the five paths for a few seconds. Do not stand on the
  paths when that happens.
- **Destroy all five seals.** If they are not all dead after about 3 minutes, Thanatos blasts the field and every
  seal starts again from the edge with full HP. Seals you have already destroyed still count, so you only have to
  finish the rest.

When the fifth seal falls, Thanatos banishes Morocc. Talk to **Lucile** and pick *Follow* to go to the top floor
(`1@tnm3`).

**5. The Young Girl**

1. 12 Evil Shadows attack a **Young Girl**. Kill them, then the leader talks to her (*Where are they?*) and a warp
   opens.
2. 18 more Evil Shadows spawn on the next section. When they are dead she shows you the way underground.
3. Walking up to the Evil Shadow at the next corner spawns 5 more. Kill them to open the warp to the boss room.

**6. Boss: the Lord Knight**

- Walking near the Demonic Shade at the boss room entrance spawns about 33 Evil Shadows across the room. This step
  is optional, so you can go around it.
- Talk to **Loki** next to the Morocc Lord Knight. After the scene everyone is moved to `1@tnm3 136/62`.
- The leader talks to **Loki** again. The leader **must not have a mercenary**. Loki says the Lord Knight is
  protected by a demonic blessing that only Mind Blaster can break. He then joins the **leader** as the mercenary
  **Loki's Shadow** for 30 minutes, and you use his Mind Blaster to break the blessing.
- {{ mob(2942) }} (MVP, 8,256,000 HP) spawns. His fight repeats every 90 seconds:

| Time in each cycle | What happens around the boss |
| --- | --- |
| 0:01 | {{ mob(2943) }} in a **+** shape (up to 10 cells out) |
| 0:21 | {{ mob(2960) }} in an **X** shape (up to 13 cells out) |
| 0:51 | Ice Mines in an **X** shape |
| 1:21 | Flame Crosses in an **S** shape |

When he dies, the party is moved to the treasure room.

### Rewards

**Treasure box** (one per run, at `1@tnm3 69/70`). The items drop on the floor around it:

| Item | Chance |
| --- | --- |
| {{ item(7293) }} | 100% |
| {{ item(749) }} | 100% |
| {{ item(7511) }} | 100% |
| {{ item(616) }} | 75% |
| {{ item(748) }} | 50% |
| One Evil Slayer weapon (each equally likely): {{ item(1671) }}, {{ item(13094) }}, {{ item(16027) }}, {{ item(18120) }}, {{ item(21010) }}, {{ item(28001) }} | 100% |

The Evil Slayer weapon comes **refined to +1 to +6** at random, with three random bonus options (Fighting Spirit,
Spell, SP+50 or MDEF+2).

**Leaving:** talk to **Loki** next to the box. The first time, he only gives you the *Morocc castle seal* quest;
talk to him again and pick *Get out of here*. You get **20–40 Instance Points** (+50 with {{ item(30034) }}, within
the daily Instance Point limit) and go back to `dali02`. Then report to **Historian Shep** for your EXP.

!!! warning "Known issue"
    The weapon's second and third bonus options are always taken from the first option list. Spell 5 and DEF+3
    never appear, even though the script defines them.

{{ instance_page("devil-s-tower") }}
