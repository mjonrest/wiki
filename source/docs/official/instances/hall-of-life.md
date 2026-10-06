# Hall of Life

## Guide

The Hall of Life is the second prison of the **Garden of Time**. Inside waits the Dimensional Criminal Rigel, a
doppelganger that stole the body of the Constellation of Life. You fight it twice, and the difficulty is set by a
**barrier level** from 1 to 20 that is stored on your {{ item(420231) }}. Each clear lets you either **raise your
barrier level** or **claim the weekly reward** for the level you just cleared. Higher levels give more
{{ item(1001456) }}, {{ item(1001457) }}, {{ item(1001458) }} and, from level 6 on, rarer materials.

The prison is entered with a {{ item(1001415) }}, which you get from the other prison, the
[Lake of Fire](lake-of-fire.md), once per day.

### Entering

**Unlocking the prisons (one time)**

1. Reach **Base Level 250**. The Garden of Time (`t_garden`) is reached through the **Dimensional barrier** at
   `/navi xmas_fild01 158/246` in the Lutie field; below level 250 the garden sends you back out.
2. Talk to **Oscar** at `/navi t_garden 119/46` and eavesdrop on his talk with Leticia and Rigel. This starts the
   Garden of Time story and the *Watching Rigel* quest.
3. Walk to `/navi t_garden 166/217` and talk to **Rigel**. He tells you to register on the prison access list.
4. Talk to the **Sealing Spirit Stone** at `/navi t_garden 166/235` and put your hand on it. You are registered and
   the two **Dimensional Prison** gates appear: Lake of Fire on the left (`/navi t_garden 158/235`) and Hall of Life
   on the right (`/navi t_garden 173/235`).

**Getting the Constellation's Protection**

Talk to the Sealing Spirit Stone again and pick **Reissue of the Constellation's protection**. If you have no
{{ item(420231) }} in your inventory or equipped, you get a new one at **barrier level 1**. It is a lower headgear.
The stone only hands one out when you have none, and a reissued one always starts at level 1, so do not throw your
old one away.

The Spirit Stone also has an in-game guide (prisoners, barriers, traps, sanctuary, the "other world") that matches
the mechanics below.

**Every entry**

| Requirement | Details |
|---|---|
| Party | Needed. The **party leader** clicks the Hall of Life gate first and picks *Get permission to the Hall of Life*; then everyone clicks it again and picks *Enter*. |
| Blessing | Every player must have the {{ item(420231) }} **equipped** to enter. |
| Key | Every player needs one {{ item(1001415) }}. It is used up when you enter. |
| Cooldown | **1 hour** from the moment you enter (*Take a break*). The gate refuses you until it has passed, even if your party's instance is still open. |
| Time limit | The instance closes after **60 minutes**. |
| Weekly reward | One claim per **account** per week. Entering after you claimed is still allowed, you just cannot claim again. |

!!! warning "You cannot re-enter a running Hall of Life"
    The 1-hour cooldown starts the moment you walk in. If you leave, die and get sent out, or disconnect, the gate
    will not let you back in until the hour has passed. Because of the party check described below, losing a member
    usually means the run is lost.

### The barrier level

Your barrier level is the number stored on your {{ item(420231) }} (levels **1 to 20**). When the fight starts the
**party leader** talks to the criminal and chooses *Release Level N Barrier*, where N can be anything from 1 up to the
**leader's** own barrier level. Everyone's reward and level-up afterwards is based on the level the leader picked,
not on their own blessing.

**How to raise your level**

After the second Rigel dies, a portal appears in the middle of the room. Each player talks to it on their own (with
the blessing equipped) and picks **one** of these:

| Choice | What happens |
|---|---|
| Increase challenge level | Your blessing is replaced with one at the new level (see table). You get no reward from this run. |
| Receive rewards | You get the reward for the level that was cleared. This uses your weekly claim. |
| I'll think about it | Nothing yet; you can talk to the portal again before leaving. |

| Cleared level compared with your blessing | Raise to |
|---|---|
| Cleared level is **higher** than yours | The cleared level (you can jump several levels at once) |
| Cleared level is **equal** to yours | Your level + 1 (up to 20) |
| Cleared level is **lower** than yours | Cannot raise; you can only claim the reward |

So a player at level 3 who clears level 10 with a level-10 leader can go straight to level 10.

**How you lose a level**

Every time you enter, you are marked as "in a correction". Only **raising your level** removes that mark. If it is
still there the next time you click the gate (you failed, timed out, left without choosing, or **claimed the reward**),
Rigel lowers your barrier level by **1** instead of letting you in. Click the gate again to actually enter. At level 1
nothing is lowered.

!!! warning "Claiming the reward costs one level"
    The portal says claiming "locks" your level until the weekly reset. What really happens is that claiming does not
    clear the mark above, so the next time you enter your blessing drops by 1. The portal also says the weekly reset is
    on Friday; the reward actually resets on **Monday at 04:00** server time.

A simple weekly plan: raise your level with every clear up to the level you want, and claim on your last clear of the
week. Next week you will start one level lower, clear that level once to get back up, then claim again.

### What the level changes

Both Rigels get stronger with every level:

| Stat | Bonus per barrier level |
|---|---|
| Max HP, 1st Rigel | 450,000,000 + 50,000,000 per level (level 1: 500M, level 13: 1.1B, level 20: 1.45B) |
| Max HP, 2nd Rigel | 100,000,000 + 50,000,000 per level (level 1: 150M, level 13: 750M, level 20: 1.1B) |
| RES and MRES | +200 |
| STR, AGI, VIT | +10 |
| INT, DEX, LUK | +20 |
| ATK and MATK | +3,000 (capped at 65,000) |

The level also sets these mechanics:

| Barrier level | HP regen every 5 s | Damage reduction buff | Field skill level | Seed traps per volley | Sanctuary cycle |
|---|---|---|---|---|---|
| 1-5 | 4% | 20% | 2 | up to 2 | 15 s |
| 6-9 | 5% | 30% | 3 | up to 3 | 15 s |
| 10-14 | 5% | 40% | 4 | up to 5 | 10 s |
| 15-17 | 7% | 50% | 5 | up to 6 | 10 s |
| 18-20 | 10% | 60% | 5 | up to 7 | 7 s |

| Barrier level | 1-2 | 3-5 | 6-8 | 9-11 | 12-14 | 15-17 | 18-20 |
|---|---|---|---|---|---|---|---|
| Rigel's Illusions in the other world | 4 | 6 | 8 | 10 | 12 | 14 | 16 |

While Rigel is groggy (see the other world below) it takes **4,100% minus 200% per barrier level** of normal damage:
3,900% at level 1, 2,100% at level 10, 1,500% at level 13 and 100% (no bonus) at level 20.

Moving purple traps also hit for **20% of your Max HP per barrier level**, so from level 5 up a purple trap is
practically lethal.

### Walkthrough

You enter at the south of a square hall. The criminal stands in the middle.

**Before you start**

- Get **every** party member inside first. When the leader starts the fight, the script remembers how many players
  are on the map. Whenever that number changes (someone leaves, disconnects, or a late member walks in), Rigel becomes
  **immune to damage** until it matches again.
- The leader equips the {{ item(420231) }}, talks to the criminal in the middle and chooses the barrier level.

**Phase 1: Dimensional Criminal Rigel** ({{ mob(22175) }})

After a short speech the first Rigel appears. During the whole fight:

- **Regeneration:** every 5 seconds it heals the percentage of its Max HP shown in the table above. Your damage must
  out-pace this.
- **Self-cleanse:** every 6 seconds it removes the status effects on itself.
- **Seed traps:** every 5 seconds, if players are within 10 cells, it drops seed traps on random nearby players.
- **Field skills:** in a loop, blue Mana Barrier markers appear on the floor (either scattered across the hall, or
  in five rows), flash, and then one of these goes off: **Aimed Shower**, **Blazing Eruption**, or **Block Seal**
  followed by **Block Explosion** at the four points around the centre. Step out of marked areas.
- **Death check:** while any party member is dead, Rigel is immune ("an infinite amount of power is granted").
  Revive fallen members quickly.

**Moving traps.** Shortly after the fight begins, gates start patrolling back and forth across the hall:

| Time after start | Traps |
|---|---|
| 10 s | 4 **purple** traps along the outer edge (they move faster) |
| 18 s, 26 s, 34 s, 42 s, 50 s | 4 **green** traps each, closer to the centre each time |
| 58 s | 2 more green traps |

- Purple trap: knocks you back and deals 20% of your Max HP per barrier level.
- Green trap: knocks you back, heals Rigel by **10% of its Max HP** and adds **+3,000 ATK/MATK** to it (up to 65,000).
  These bonuses stack every time anyone touches one.

**Nets.** At 26 seconds four {{ mob(20582) }} (15,000,000 HP each) appear around the middle. Every 10 seconds they
use **Wide Leash** to pull players in, then are replaced by fresh ones.

**The other world.** Also at 26 seconds, a portal opens on the **north side** of the hall (around the middle of the
north wall). It leads to an alternate Hall of Life in a separate part of the map with **Rigel's Illusions** ({{ mob(22176) }}): one in
each corner plus extra ones depending on the level (table above). In there, Mana Barrier markers appear in a 5x5 grid
followed by **Frost Field** or **Lightning Judgement**.

- While the portal is open Rigel heals an **extra 3% of Max HP every 5 seconds, plus 3% more for every player who is
  inside the other world**. Send only a few strong, mobile players.
- When the **last illusion dies**: all moving traps vanish, Rigel's ATK/MATK goes back to normal (removing all trap
  bonuses), it becomes **groggy for 10 seconds**, takes the multiplied damage described above, and stops
  regenerating, dispelling and planting seeds during that time. A return portal appears in the other world.
- The trap cycle then starts over (purple traps after 10 s, portal again at 26 s, and so on).

The rhythm of phase 1 is: clear the illusions, burst Rigel during the 10-second groggy window, repeat.

**Phase 2: Criminal Rigel** ({{ mob(22174) }})

When the first Rigel dies, everyone alive is pulled to the centre and the second Rigel spawns with less HP (see
above). Regeneration, self-cleanse, seed traps, field skills, the death check and the player-count check all
continue, the nets come back straight away, and new moving traps no longer spawn.

- **Sanctuary:** every cycle (15, 10 or 7 seconds depending on level) Rigel marks a 13x13 sanctuary around itself.
  While Rigel stands within 6 cells of the centre of its latest sanctuary it takes **no damage**. Pull or lure it at
  least 7 cells away, then deal damage until the next sanctuary appears under it.

!!! tip
    Traps that were already walking when the first Rigel died are not removed when phase 2 starts, and green ones still
    heal and empower the new Rigel. Killing the remaining Rigel's Illusions clears them and makes Rigel groggy, but
    it also restarts the trap cycle.

**Finish.** When the second Rigel dies, the reward portal appears in the middle of the hall. Talk to it with the
blessing equipped to raise your level or claim your reward, as described above. The portal also offers *Return to
Garden*.

### Rewards

The reward is for the barrier level the leader picked, given once per account per week (resets **Monday 04:00**).

| Level | {{ item(1001456) }} | {{ item(1001457) }} | {{ item(1001458) }} | {{ item(1001459) }} | {{ item(1001460) }} | {{ item(1001601) }} | {{ item(1001593) }} |
|---|---|---|---|---|---|---|---|
| 1 | 15 | - | - | - | - | - | - |
| 2 | 23 | 8 | 8 | - | - | - | - |
| 3 | 32 | 15 | 15 | - | - | - | - |
| 4 | 41 | 20 | 20 | - | - | - | - |
| 5 | 52 | 25 | 25 | - | - | - | - |
| 6 | 58 | 27 | 27 | 5 | - | - | - |
| 7 | 61 | 30 | 30 | 12 | - | - | - |
| 8 | 68 | 34 | 34 | 20 | 5 | - | - |
| 9 | 78 | 38 | 38 | 22 | 6 | 1 | 3 |
| 10 | 87 | 43 | 43 | 24 | 8 | 3 | 5 |
| 11 | 98 | 48 | 48 | 26 | 9 | 5 | 6 |
| 12 | 111 | 54 | 54 | 29 | 10 | 7 | 9 |
| 13 | 125 | 60 | 60 | 32 | 11 | 8 | 10 |

All amounts are guaranteed; there is no random roll.

Rewards are only defined up to level 13; clears at level 14 to 20 give the level 13 rewards.

### Tips

- Your weekly loop needs one {{ item(1001415) }} per entry, and the Lake of Fire gives one per day. Do not waste keys
  on runs your party cannot finish.
- Bring everyone in before the leader starts, and keep everyone alive and inside: a dead or missing member makes Rigel
  immune.
- Avoid the green traps. Each touch heals Rigel 10% and stacks +3,000 ATK/MATK until the illusions are cleared.
- Keep the number of players going through the north portal small; each one adds 3% healing every 5 seconds.
- Save burst skills for the 10-second groggy window after the illusions die.

{{ instance_page("hall-of-life") }}
