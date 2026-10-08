# Villa of Deception

## Guide

Villa of Deception is a repeatable Episode 18 instance in Grey Wolf Village. The party fights through the villa's corridor, central hall and garden, then defeats {{ mob(21316) }} and finally {{ mob(21317) }} in the basement. It has a **Normal** and an **Advanced** (hard) mode.

### Requirements and entry

| | Normal | Advanced |
|---|---|---|
| Level | 170+ | 200+ |
| Cost to create | Free | 1 {{ item(1000471) }} (taken from the party leader) |
| Party | Required, leader creates | Required, leader creates |

- **NPC:** **Aira** at `/navi wolfvill 79/260`. She appears once you have progressed far enough in the Episode 18 main quest.
- **Cooldown:** entering either mode starts a shared cooldown that resets at 04:00 server time. When it is over, talk to Aira once to clear it before entering again.

The leader picks **Create Villa of Deception** (or **Create Villa of Deception Advanced**, which only shows up while the leader has a Villa Basement Key). Then everyone picks **Entry** and the mode.

### Mode differences

| | Normal | Advanced |
|---|---|---|
| Monsters | {{ mob(21318) }}, {{ mob(21319) }} | {{ mob(21377) }}, {{ mob(21378) }} |
| Bosses | {{ mob(21316) }}, {{ mob(21317) }} | {{ mob(21360) }}, {{ mob(21361) }} |
| Monsters to kill in the hall (stage 2) | 35 | 70 |
| Monsters to kill in the garden (stage 3) | 35 | 80 |
| Plague zones in the garden (before food) | 16 | 48 |
| Wandering magic circles in the final room | 2 | 4 |

### Walkthrough

**Stage 1: Corridor of souls**

- The corridor is full of monsters, and Death-shaped traps patrol the row in front of the hall door. Touching a trap **pushes you back and deals 50% of your Max HP**.
- To open the hall, two players must free the souls (wisps) at the two ends of the hallway, at `1@advs 67/182` and `1@advs 180/182`, **within 3 seconds of each other**. If only one is freed in time, both reset.
- Once both are freed, the remaining corridor monsters vanish and the door to the hall opens.

**Stage 2: The hall**

- Monsters keep spawning until the stage total is reached. A counter announces how many are left.
- Four **food tables** are in the hall. Eating takes 4 seconds and gives you a random ailment (Confusion, Curse, Blind, Poison or Silence) for 30 seconds. **Every 2 dishes eaten removes one Plague zone from the next stage**, down to a minimum of 3.
- Kill every monster to open the warp to the garden. The warp drops you at a random spot in the garden.

!!! tip
    The food is worth it, especially in Advanced: the garden starts with 48 Plague zones.

**Stage 3: The garden**

- {{ mob(20846) }} zones appear at random spots in the garden and are reshuffled to new random spots every 10 seconds. Avoid standing in them.
- Kill the stage's monster total to open the way to the next room.

**Stage 4: Schulang**

- The leader talks to Schulang at the end of the room. {{ mob(21316) }} spawns (Normal) or {{ mob(21360) }} (Advanced), together with one {{ mob(21319) }}.
- Schulang repeatedly casts Thunder Storm in a grid of five columns, sweeping row by row. **One random column is left untouched each cycle.** Stand in that column to dodge the storm.
- Killing Schulang opens the warp to the final room.

**Stage 5: Twisted God Freyja**

- The leader clicks the spot under the chandelier at the top of the room. Twisted God Freyja then spawns.
- **Freyja takes less damage the farther she is from the chandelier** (around `1@advs 124/356`). Pull her as close to it as you can.
- Magic circles wander around the room. Stepping on one costs 10% HP and **warps you all the way back to the Stage 1 corridor**.
- Four yellow magic stones on the sides of the room can stop the circles. Using one drains 2 to 20% of your HP and SP (it can kill you). If you survive, all circles stop moving for 10 seconds. A stone can be used again 20 seconds later.

### Rewards

When Freyja dies, a glowing box appears under the chandelier. **Each player** opens it once for:

| Reward | Amount |
|---|---|
| {{ item(1000405) }} | 8 (10 with 5000 Grey Wolf Village reputation) |
| {{ item(1000471) }} | 1, 10% chance (needed to open Advanced mode) |
| Instance Points | 20 to 40 (random) on Normal, 40 to 60 on Advanced, given when you choose **Exit** |

Both modes give the same box rewards.

!!! tip "Instance Points"
    Instance Points can be earned once per device for each instance run, up to 1200 per account per day. A rented {{ item(30034) }} adds 50 points per claim. Use `@instancepoints` to see your total.

{{ instance_page("villa-of-deception") }}
