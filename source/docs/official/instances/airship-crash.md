# Airship Crash

## Guide

Airship Crash is a farming instance. You follow Lydia's group through the crash site, help the wounded, then go down into the cave below to hunt endlessly respawning monsters for {{ item(1000364) }}. With enough ore you can summon the {{ mob(20891) }}. The main rewards are {{ item(1000363) }}, which are traded at Rusbald.

### Requirements and entry

| | |
|---|---|
| Level | Base Level 215 or higher |
| Party | Required. Only the party leader can create the instance and trigger story events. |
| NPC | **Dr.Dulaisakstrom** at `/navi dali02 137/86` |
| Cooldown | Once per day. Entering starts the cooldown, which resets at 04:00 server time. |

The leader picks **Create Airship Crash**, then everyone (leader included) picks **Enter Airship Crash**.

!!! note
    Teleport, Ice Wall and saving are disabled on both instance maps. In the cave, use the **Ropes** to move around (see below).

### Walkthrough

**1. The crash site**

1. Head south from the entrance to Lydia, Seth, Alice and Roki (around `1@mjo1 233/293`). The leader talks to **Lydia** to play the first scene. The group then moves on.
2. The leader talks to **Lydia** again at around `1@mjo1 96/200`, then a third time at around `1@mjo1 196/132`.
3. After the third scene, Captain Pei Lu asks for help with the injured. Ten **Injured Travelers** are scattered around the crash site. Treat one by clicking it and standing still for 3 seconds. The system counts the treated travelers for the whole party.
4. Once **6** are treated, each player can report to **Captain Pei Lu** at around `1@mjo1 71/344` for 1 {{ item(1000363) }}. This reward has its own daily cooldown.

!!! warning "Treat exactly 6"
    Captain Pei Lu only gives the reward while the party's count is **exactly 6**. If anyone treats a 7th traveler, nobody can claim it for the rest of the run. Stop at 6 and report.

**2. The cave**

1. Take the warp at around `1@mjo1 274/252` down into the cave camp.
2. The leader talks to the **Doctor** at the camp and chooses **Join the exploration team**. This spawns the cave's monsters, which **respawn as soon as they die**:
    - 50 {{ mob(20886) }} on the crash site map
    - 50 {{ mob(20886) }}, 60 {{ mob(20887) }}, 45 {{ mob(20888) }}, 60 {{ mob(20889) }} and 60 {{ mob(20890) }} in the cave
3. Farm the cave for {{ item(1000364) }}, which drops from all of these monsters.
4. **Ropes** are placed all over the cave. Each one can send you back to the camp or to the "unknown creature area" in the north. The **Student** at the camp marks all 15 rope locations on your minimap.

**3. Unidentified Creature (optional boss)**

Bring **55** {{ item(1000364) }} to the **Mysterious Ghost** at the camp (around `1@mjo2 373/371`) and choose **Place Ymir Ore**. The ore is consumed and the {{ mob(20891) }} spawns in the northern area (around `1@mjo2 197/354`). You can summon it again each time someone has 55 ore.

### Cave hunting missions

The **Researcher** at the camp gives repeatable kill missions. Any monster killed in the cave counts:

| Mission | Kills | Reward | Unlocks |
|---|---|---|---|
| Capture 100 monsters | 100 | {{ item(1000363) }} x2 | the 200 mission (first time) |
| Capture 200 monsters | 200 | {{ item(1000363) }} x5 | the 350 mission (first time) |
| Capture 350 monsters | 350 | {{ item(1000363) }} x10 | — |

Only one mission can be active at a time. Talk to the Researcher once it is complete to get the reward automatically.

!!! warning "Known issue: Researcher menu is shifted by one"
    The Researcher's options don't match the missions you get:

    - **Cancel** starts the 100-kill mission.
    - **Capture 100 monsters** starts the 200-kill mission.
    - **Capture 200 monsters** starts the 350-kill mission.
    - **Capture 350 monsters** does nothing.

    The rewards still match the mission you actually have.

!!! warning "Known issue: entrance gate"
    The Warp Gate next to the arrival point on the crash site uses a destination that no script sets, so it may not take you out of the instance.

### Rewards and exchange

- {{ item(1000363) }} from Captain Pei Lu (1 per day) and the Researcher missions (2, 5 or 10).
- {{ item(1000364) }} from cave monster drops.
- **Rusbald** at `/navi dali02 134/86` trades 10 {{ item(1000364) }} for 1 {{ item(1000363) }}, and Ymir Fragments for his equipment and random boxes (see the exchange table below).

{{ instance_page("airship-crash") }}
