# Werner Laboratory Central Room

## Guide

The Central Room of Werner's laboratory is part of the Terra Gloria (Episode 16.2) story. You visit it once during the main quest, then come back for the repeatable daily **Sweeping the remnants**, where you fight through the lab's guards and security devices to kill the {{ mob(3621) }}.

### Requirements and entry

| | |
|---|---|
| **Instance NPC** | Rookie: `/navi slabw01 236/91` (entrance gate next to him at `246/88`) |
| **Daily quest NPC** | Rookie: `/navi que_swat 150/58` |
| **Prerequisite** | Story run: Terra Gloria main quest at the Central Room step. Daily: Terra Gloria main quest finished |
| **Party** | Required. Only the party leader can create the instance |
| **Time limit** | 60 minutes (closes after 5 minutes with nobody inside) |
| **Cooldown** | Daily quest: 4 hours (*Sweeping the remnants (Standby)*), starting when you hand it in |

**Daily run:**

1. Talk to the Rookie in `que_swat`, choose **About the monster in the central room** and accept *Sweeping the remnants* (kill one Pet Child).
2. Go to the Rookie in `slabw01`. The party leader (with the quest active) picks **Enter now.** to create the instance.
3. Click the **Central Room** gate next to him and pick **Go in.**

Party members with the daily quest active talk to the Rookie after the leader has created the instance; the gate then appears for them. Click it and pick **Go in**.

### Walkthrough (daily)

The run is a chain of rooms. Doors open when the **party leader** solves the Security devices.

#### Security devices

Each device shows one of the sample names in **red** and in **blue** and you must pick the correct colour. The rule from the samples on display: *change red to blue, and blue to red*.

| Sample | Correct answer |
|---|---|
| Purity, Eternity, Dawn | the **blue** option |
| Rose, Contradiction, Joy, Sea, Way back home, Loneliness, Glow, Twilight | the **red** option |

A wrong answer resets both devices of that pair, so you have to solve them again. Only the party leader can use the devices.

#### Room 1

When the leader steps off the entrance, four **Guards** appear along the hallway. Walking within 4 cells of one triggers an ambush of {{ mob(3622) }}:

| Guard | Ambush |
|---|---|
| `188/58` | 3 near it, plus 3 more further up the hall |
| `189/117` | 3 near it, plus 6 more in two groups further up |
| `171/167` | 1; killing it activates Security device L-01 (`155/191`) |
| `206/167` | 3; killing them activates Security device R-01 (`220/191`) |

Solve both devices to open the warp at `187/170`.

#### Room 2

Three more Guards appear:

| Guard | Ambush |
|---|---|
| `70/38` | 3 |
| `33/52` | 3; killing them activates Security device L-02 (`22/61`) |
| `111/52` | 3; killing them activates Security device R-02 (`122/61`) |

Solving both opens the warp at `71/77` and the **Central Entrance** door.

#### Central Room

When the leader steps on the Central Entrance (`54/146`) they choose:

- **Proceed with the story.** Replays the scene with Eisen Werner and Seyren. Afterwards the room resets and the party is sent back outside the door, so you can then choose the battle.
- **Proceed with the battle.** The leader walks up to the Pet Child; after about 15 seconds the magic field activates and {{ mob(3621) }} spawns.

Other party members who step on the door just go inside. Killing the Pet Child completes *Sweeping the remnants* and opens the **Emergency exit** at `55/150`, which leads to `que_swat 155/58`.

### Story run

During the main quest the same rooms are used, but Eisen Werner talks to you at each stage instead of the guard ambushes, and the leader still has to solve the four Security devices. At the end, talking to Eisen Werner in the central room gives the party leader {{ item(25179) }} and {{ item(23087) }}, 20-40 Instance Points, and a warp to `que_swat 155/50`.

### Rewards (daily)

Hand in *Sweeping the remnants* to the Rookie in `que_swat`:

| Reward | Amount |
|---|---|
| {{ item(25155) }} | 3 |
| Base EXP | 200,000 |
| Job EXP | 200,000 |

{{ instance_page("werner-laboratory-central-room") }}
