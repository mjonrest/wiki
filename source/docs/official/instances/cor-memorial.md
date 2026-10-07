# Cor Memorial

## Guide

In Cor Memorial you help the Rebellion collect battle data on Elyumina's creations. Your party activates four
trap boxes around Cor, defeats the illusion monsters that come out of each, and then fights her prototype
{{ mob(20340) }} in the barracks.

### Entering

- **Story run:** the first time, Cor Memorial is part of the Episode 17.1 story. **Elena Volkova** at
  `/navi sp_cor 180/169` sends you in to capture Elyumina. Only the party leader can create and enter this
  version from her.
- **Repeatable run:** once you have finished the *Pure Facts* story quest, talk to the **Rebellion** soldier at
  `/navi sp_cor 113/130`. The first time, a short scene with Elyumina plays.
- **Party:** you must be in a party. The **party leader** picks *Ready* to create the instance, then everyone picks
  *Enter*.
- **Cooldown:** entering gives you *Pure Backstab (Standby)*, a daily cooldown that resets at **04:00** server time. Once it has passed, talk to the
  Rebellion soldier to clear it.
- **Time limit:** the instance lasts **2 hours**.

### Walkthrough (repeatable run)

!!! warning
    The **party leader** must be the first to walk up to Elena. The instance only switches to the repeatable
    version when the leader steps next to her. If someone else talks to her first, the story version starts
    instead and the repeatable boxes do not appear.

1. Inside, the **party leader** walks up to **Elena Volkova** at the start (`1@cor 180/169`) and talks to her.
   Elyumina gives the briefing and marks the four trap boxes on everyone's minimap.
2. Visit the four boxes in any order. Touch a box to set it off: a group of Elyumina's monsters spawns around it.
3. Kill the whole group. The box is then cleared and its mark on the minimap disappears.
4. When all four boxes are cleared, Elyumina appears in the barracks at `1@cor 172/223`. Talk to her and choose
   *Go in.* to open the portal next to her.
5. The first player through the portal starts the boss fight with {{ mob(20340) }} at `1@cor 137/221`.

| Box | Location | Monsters |
| --- | --- | --- |
| 1 | `1@cor 222/236` | 6 {{ mob(20341) }}, 3 {{ mob(20343) }}, 4 {{ mob(20355) }} |
| 2 | `1@cor 220/170` | 6 {{ mob(20342) }}, 3 {{ mob(20343) }}, 3 {{ mob(20356) }} |
| 3 | `1@cor 160/119` | 6 {{ mob(20341) }}, 3 {{ mob(20343) }}, 3 {{ mob(20355) }} |
| 4 | `1@cor 140/79` | 6 {{ mob(20342) }}, 3 {{ mob(20343) }}, 3 {{ mob(20356) }} |

### Traps

While a box's monsters are alive, a trap keeps reappearing on top of the box (every 10 seconds or so):

- **Biological Battery** (boxes 1 and 3): stepping on it summons a {{ mob(20345) }} that blows itself up. A few
  seconds later a **Reinforced Energy** orb appears next to the box. Click it for **+20 to all stats for 30
  seconds**.
- **Chemical Poison** (boxes 2 and 4): stepping on it summons a {{ mob(20344) }}, which turns into a poison cloud.

### EL1-A17T

- The arena is closed off by barricades.
- Every **30 seconds** Elyumina warns that the boss "is starting to spread something", and a new Biological
  Battery or Chemical Poison trap appears at one of 11 spots in the arena. The traps work the same way as at the
  boxes, and a battery you trigger here also spawns a Reinforced Energy orb for the stat boost.
- When the boss dies, every trap and leftover monster is removed and **Elena Volkova** appears at
  `1@cor 138/221`.

### Rewards

Talk to **Elena Volkova** after the fight. Each player gets this once per run, and is then sent back to `sp_cor`:

| Reward | Amount |
| --- | --- |
| {{ item(25723) }} | 1 |
| {{ item(25669) }} | 5 |

{{ instance_page("cor-memorial") }}
