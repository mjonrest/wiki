# Glastheim Challenge Mode

## Guide

Glastheim Challenge Mode sends the party into a corrupted Old Glast Heim to purify phantoms with Oscar. The party is
split in two to clear both wings, then fights a phantom of Amdarais or Himmelmez that has to be **kept inside a magic
circle**. The leader picks a **stage from 1 to 10**: higher stages give a tougher boss and a much bigger treasure
box of Temporal materials.

### Entering

- **NPC:** **Glastheim Challenge Mode Administrator** at `/navi glast_01 143/288`.
- **Party:** needed. The **party leader** picks *create*; then everyone picks *enter*.
- **Level:** the script has no level check.
- **Cooldown:** entering starts the *Glast Heim Challenge Mode* quest, which ends at the next **04:00** server time.
- **Time limit:** **30 minutes**, and the instance closes after 5 minutes with nobody inside.

### Stages

Inside, the party leader talks to **Oscar** at the entrance and picks a *Contaminated Magic Stage*. The stages you can
pick depend on how many times **you, the leader,** have cleared Challenge Mode:

| Leader's clears | Stages available |
|---|---|
| 0-9 | 1 |
| 10-19 | 1-2 |
| 20-29 | 1-3 |
| ... | one more stage per 10 clears |
| 90 or more | 1-10 |

| Stage | Boss Max HP |
|---|---|
| 1 | 600,000,000 |
| 2 | 750,000,000 |
| 3 | 900,000,000 |
| 4 | 1,050,000,000 |
| 5 | 1,200,000,000 |
| 6 | 1,350,000,000 |
| 7 | 1,500,000,000 |
| 8 | 1,650,000,000 |
| 9 | 1,800,000,000 |
| 10 | 2,000,000,000 |

Everyone inside the instance when the leader claims the reward from Oscar gets the clear counted.

### Walkthrough

**1. Purify both wings**

After the leader confirms the stage, the party is split as evenly as possible between the **left** and **right**
wings. Each wing spawns **50 phantoms**: 10 each of {{ mob(20574) }}, {{ mob(20576) }}, {{ mob(20577) }} and
{{ mob(20578) }}, and 20 {{ mob(20579) }}. A counter announces how many are left on each side.

When one wing is cleared, a warp opens there that leads toward the other wing, so that group can go help.

**2. Meet Oscar at the centre**

When both wings are cleared, the warp to the central area opens. Go north ("12 o'clock") and find **Oscar**. A
{{ mob(20575) }} also spawns next to him. The leader talks to Oscar and picks *Transform*: he walks north and opens the
passage to the boss room.

**3. Boss: the Phantom of Dark Dhalis**

In the boss room the leader talks to Oscar again and picks *We're ready*. The boss appears in the central magic circle
and, 6 seconds later, everyone on the map is pulled into the room. The boss is:

- {{ mob(20573) }} (about 90% of runs), or
- {{ mob(20572) }} (about 10%).

**Keep it in the circle.** Every 10 seconds the script checks whether the boss is inside the central magic circle.
If it is outside on **three checks in a row** (about 30 seconds), the purification fails: the boss vanishes without a
reward. Oscar reappears, and the leader can talk to him to summon it again.

Every 5 seconds the boss uses one of these:

| Attack | What happens |
|---|---|
| Wide-range Curse | Meteor Storms run outward along the four diagonals from the boss |
| Cross Earthquake ("!!") | Heaven's Drive spreads outward in a cross and diagonals around the boss |
| Rage Blast | A shorter burst of Heaven's Drive all around the boss |
| Cross Firewall ("!!") | Fire Walls run out along the four diagonals |
| Random warp | Sometimes nothing; otherwise each player has about a 35% chance to be teleported to a random spot on the map |
| Dark Judgment ("!!") | 16 **Contaminated Bone Thorns** appear in a 4x4 grid over the room and cast **Dark Grand Cross** six times between 15 and 24 seconds later, then vanish. The boss's other attacks pause meanwhile. |

### Rewards

When the boss dies, a **treasure box** and **Oscar** appear in the boss room.

**Treasure box.** The first player to click it opens it and the loot drops **on the ground** around it. Amounts are
random, roughly in these ranges:

| Stage | {{ item(25864) }} | {{ item(25865) }} | {{ item(25866) }} | {{ item(25867) }} |
|---|---|---|---|---|
| 1 | 3-5 | - | - | 6-15 |
| 2 | 3-6 | - | - | 7-20 |
| 3 | 3-7 | 1-3 | - | 10-25 |
| 4 | 4-8 | 1-4 | - | 12-30 |
| 5 | 5-9 | 1-4 | 1-3 | 15-30 |
| 6 | 6-10 | 1-5 | 3-7 | 17-30 |
| 7 | 6-10 | 2-5 | 5-11 | 18-30 |
| 8 | 6-10 | 2-6 | 8-16 | 19-30 |
| 9 | 8-10 | 2-6 | 11-22 | 20-30 |
| 10 | 8-10 | 2-7 | 14-28 | 22-30 |

**Oscar.** Only the **party leader** can talk to him. This counts the clear for the leader and opens the **Exit**.

**Exit.** Each player who uses it returns to `glast_01` and earns Instance Points: **20 per stage** of the Contaminated Magic Stage fought this run
(20 for stage 1, up to 200 for stage 10). Instance Points count toward the daily cap of 1,200.

{{ instance_page("glastheim-challenge-mode") }}
