# Lake of Fire

## Guide

The Lake of Fire is the first prison of the **Garden of Time**. One of the four Divine Beasts, the former guards of
the prison, is held here. It starts out completely invulnerable: you have to lure it over seven barriers spread around
the lava lake to strip its defence, then kill it. Every player who finishes gets that season's Energy, a stack of
{{ item(1001414) }} and the {{ item(1001415) }} needed to enter the [Hall of Life](hall-of-life.md).

### Entering

**Unlocking the prisons (one time)**

1. Reach **Base Level 250** and enter the Garden of Time through the **Dimensional barrier** at
   `/navi xmas_fild01 158/246` (Lutie field).
2. Talk to **Oscar** at `/navi t_garden 119/46` to start the Garden of Time story.
3. Talk to **Rigel** at `/navi t_garden 166/217`, then register at the **Sealing Spirit Stone** at
   `/navi t_garden 166/235`.

**Every entry**

| Requirement | Details |
|---|---|
| Gate | **Dimensional Prison** (left gate) at `/navi t_garden 158/235` |
| Party | Needed. The **party leader** clicks the gate first and picks *Get permission to the Lake of Fire*; then everyone clicks it and picks *Enter*. |
| Cooldown | Once per day. Entering starts the cooldown, which ends at the next **04:00** server time. |
| Time limit | The instance closes after **60 minutes**. |
| Inventory | You need some free inventory space and weight, or the gate refuses you. |

!!! warning "Everyone in before the fight starts"
    The cooldown starts as soon as you enter, so you cannot come back in after leaving. Your reward depends on a
    hunting quest that is given when you arrive at the entrance, and only **until the leader wakes the beast**. A player
    who enters after that does not get the quest and receives **no reward**.

### The four Divine Beasts

Each instance picks one beast at random:

| Beast | Field skill in the final phase | Energy reward |
|---|---|---|
| Spring Divine Beast | Aimed Shower | {{ item(1001440) }} |
| Summer Divine Beast | Block Seal followed by Block Explosion | {{ item(1001441) }} |
| Autumn Divine Beast | Blazing Eruption | {{ item(1001442) }} |
| Winter Divine Beast | Frost Field | {{ item(1001443) }} |

### Walkthrough

**1. Wake the beast**

You arrive at the west end of the lake. The beast is sleeping next to the entrance. Once everyone has arrived, the
**party leader** talks to it and picks *I wish to receive the Hall of Life key*. After a short speech it spawns as a
monster.

**2. Lure it over the seven barriers**

At first the beast takes **no damage at all**. Seven **Mana Storm** barriers are placed around the lake:

| Barrier | Coordinates (x, y) |
|---|---|
| 1 | 24, 154 |
| 2 | 95, 182 |
| 3 | 51, 93 |
| 4 | 93, 58 |
| 5 | 129, 58 |
| 6 | 94, 35 |
| 7 | 43, 35 |

The barriers trigger when the **beast** walks onto them, so have it chase someone across each one. The order does not
matter. Each barrier disappears once used, briefly stuns the beast, and lowers its defence:

| Barriers triggered | Damage the beast takes |
|---|---|
| 0 | 0% |
| 1 | 5% |
| 2 | 10% |
| 3 | 20% |
| 4 | 30% |
| 5 | 40% |
| 6 | 50% |
| 7 | 100%, final phase starts |

While you kite it, invisible bombs keep spawning within 8 cells of the beast (five at a time, about every 3 seconds)
and **self-destruct**. Keep moving and do not let the party bunch up next to it.

**3. Final phase**

After the seventh barrier the beast teleports to the east side of the lake (176, 163) and every
living party member is pulled there with it. The bombs stop, it now takes full damage, and it starts its field skill
in a loop:

- Spring, Summer and Autumn: blue Mana Barrier markers appear at random spots within 10 cells of the beast, flash,
  and then the beast's skill (table above) goes off at four points 10 cells diagonally around it.
- Winter: a 5x5 grid of markers appears around a spot near the beast, then **Frost Field** goes off from its centre.

Step out of the marked area when the markers flash.

**4. Leave**

When the beast dies, a portal appears just north of that spot (176, 166). Talk to it to get your reward and return to the
Garden of Time.

### Rewards

Each player who completed the hunting quest for the beast (it counts the kill) receives, from the exit portal:

| Item | Amount |
|---|---|
| Energy of the beast's season ({{ item(1001440) }}, {{ item(1001441) }}, {{ item(1001442) }} or {{ item(1001443) }}) | 5 |
| {{ item(1001414) }} | 10 |
| {{ item(1001415) }} | 1 |
| Instance Points | 40-60 (random) |

The key is consumed when you enter the Hall of Life, so one Lake of Fire per day means one Hall of Life entry per day.

{{ instance_page("lake-of-fire") }}
