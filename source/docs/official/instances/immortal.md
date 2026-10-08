# Immortal

## Guide

Immortal is the Episode 20 daily boss instance. The party removes the seal on {{ mob(21981) }} and fights him while his untouchable {{ mob(21979) }} (the "Vision of Lasgand") roams the arena. The whole fight is about **keeping Lasgand far away from his Vision** and **keeping everyone alive**.

### Requirements and entry

| | |
|---|---|
| Level | Base Level 215 or higher |
| Prerequisite | Episode 20 main quest completed |
| Party | Required. The party leader creates the instance and starts the fight. |
| NPC | **Branches of the World Tree** at `/navi jor_twig 114/147` |
| Modes | **Immortal** (normal) and **Immortal (Hard)** |
| Cooldown | One entry per day across both modes. Entering starts the cooldown, which resets at 04:00 server time. |
| Time limit | 30 minutes |

The leader talks to the Branches of the World Tree and picks **Create Immortal** or **Create Immortal (Hard)**. Everyone then talks to it again and picks **Enter**.

### The fight

1. The leader talks to the sealed Lasgand in the middle of the room and picks **Remove the seal and attack.**
2. {{ mob(21981) }} spawns in the centre. His Vision spawns at a random spot to the west, east or south.
3. **The Vision cannot be damaged or killed** and is immune to status effects. Ignore it and keep away from it.

**Distance is everything.** Every few seconds the script checks how far Lasgand is from his Vision:

- The closer they are, the **less damage Lasgand takes** (damage reduction ranges from very high when they are together to much lower when they are far apart).
- The Vision visibly **grows** as it gets closer to Lasgand and **shrinks** as it moves away, so you can judge the distance from its size.
- Pull Lasgand away from the Vision and keep the fight there.

**Lasgand's extra attacks** (every 4 seconds, picked at random):

| Attack | Normal | Hard |
|---|---|---|
| Meteor Storm in a 3x3 grid around him | 15% | 40% |
| Heaven's Drive in a 3x3 grid around him | 45% | 40% |
| Cloud Kill | 25% | 5% |
| Nothing | 15% | 15% |

When Lasgand and the Vision are more than 8 cells apart, his Meteor and Heaven's Drive attacks **also hit points along the line between him and the Vision**. Cloud Kill is cast along that line too. Don't stand between the two.

**The Vision's attacks** (every 2 seconds): Heaven's Drive in a 3x3 grid around itself (55%) or Storm Gust (25%, level 1 in Normal and level 10 in Hard).

!!! warning "Nobody may die"
    Every 2 seconds the script checks the party. If **any member is dead**, or the party no longer has the same number of members as when the seal was removed, Lasgand becomes **invincible** and the message "There is a death in the party" appears. He stays invincible until everyone is alive again. Resurrect fallen members right away, and **don't invite, kick or let anyone leave the party** during the fight.

### Rewards

When Lasgand dies, a {{ mob(22004) }} (Normal) or {{ mob(22005) }} (Hard) appears, along with **Nyar** at the north side of the room. **Each player credited with the Lasgand kill** talks to Nyar for:

| Reward | Normal | Hard |
|---|---|---|
| {{ item(1001249) }} | 1–2 | 1–2 |
| Antiquity box | {{ item(102567) }} | {{ item(102568) }} |
| Base / Job EXP | 34,152,989 / 5,567,916 | 34,152,989 / 5,567,916 |
| White Cat Alliance reputation | +20 | +20 |
| Instance Points | 40–60 | 60–80 |

Afterwards, pick **Go outside** to return to `jor_twig`.

!!! tip "Instance Points"
    Instance Points can be earned once per device for each instance run, up to 1200 per account per day. A rented {{ item(30034) }} adds 50 points per claim. Use `@instancepoints` to see your total.

{{ instance_page("immortal") }}
