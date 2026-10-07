# Wolfchev's Laboratory

## Guide

Wolfchev's Laboratory is the hidden experiment wing of the Lighthalzen Bio Lab. Your party fights through three security labs full of {{ mob(2242) }} and then faces one randomly chosen transcendent experiment, one of the thirteen Bio Lab heroes. Killing all thirteen over several runs earns a reward from Wolfchev himself.

### Requirements and entry

| | |
|---|---|
| **NPCs** | Researcher (create) `/navi lhz_dun04 151/276`, Laboratory Entrance (enter) `/navi lhz_dun04 147/279` |
| **Getting there** | Take the warp at `lhz_dun03 239/78` down to the 4th floor |
| **Party** | Required. Only the party leader can create the instance |
| **Time limit** | 4 hours (closes after 5 minutes with nobody inside) |
| **Cooldown** | Once per day (*Laboratory Restricted Access*), starting when you **enter**. Resets at 04:00 server time. |

1. Talk to the Researcher once to receive the thirteen *[Rest]* boss quests (one per experiment).
2. The party leader talks to the Researcher again, picks **Going into the laboratory** and creates the instance.
3. Everyone clicks the Laboratory Entrance and picks **Go inside**. This starts your personal daily cooldown.

!!! note
    When your cooldown has expired, click the Laboratory Entrance once to clear it, then click again to enter. The leader cannot create a new instance while still on cooldown. The Researcher, the Entrance and Wolfchev all want at least 1,000 free weight before they talk to you.

### Walkthrough

#### Lab No.1: emergency valves

A few seconds after you arrive the security system releases 10-15 {{ mob(2242) }}. Kill them all to stop the system. Then:

1. The **party leader** reads the **Manual Sheet** (`1@lhz 39/168`). It gives one random procedure for either the left or the right valve.
2. The leader turns that valve (left `41/172`, right `52/172`) exactly as written: four turns in total.

| Manual says | Valve | Turns |
|---|---|---|
| Clockwise twice, Counterclockwise once, Clockwise once | Left | CW, CW, CCW, CW |
| Clockwise once, Counterclockwise twice, Clockwise once | Left | CW, CCW, CCW, CW |
| Clockwise once, Counterclockwise once, Clockwise twice | Left | CW, CCW, CW, CW |
| Counterclockwise twice, Clockwise once, Counterclockwise once | Right | CCW, CCW, CW, CCW |
| Counterclockwise once, Clockwise twice, Counterclockwise once | Right | CCW, CW, CW, CCW |
| Counterclockwise once, Clockwise once, Counterclockwise twice | Right | CCW, CW, CCW, CCW |

A wrong sequence does nothing and you have to read the manual again (which may give a new procedure). The right sequence opens the door to Lab No.2 at `45/173`.

#### Lab No.2: pipe pressure

Stepping in starts the security system and the pipe alarms.

- **Monster waves**: Starving Lab animals ({{ mob(2242) }}) arrive in waves at about 0:08 (10), 5:08 (20), 10:08 (16), 15:08 (19) and 20:08 (20).
- **Pipe pressure**: roughly every 3 minutes one or more **Valves** light up around the room, each with 5 {{ mob(2243) }}. The **party leader** must click any lit valve and finish a 20 second progress bar within 63 seconds, or a pipe explodes.
- **Three pipe explosions** freeze the system: after a 10 second warning, everyone in Lab No.2 is thrown out to `lhz_dun04`.

The moment every spawned animal in Lab No.2 is dead, the security system stops, no more waves or pipe alarms come, and the door to Lab No.3 opens at `151/64`.

!!! tip
    You do not have to survive all five waves. Clear the first wave quickly and the lab is done before the second one arrives. Keep the leader free to run to the valves.

#### Lab No.3: animal pens

Five waves of mixed {{ mob(2242) }} and {{ mob(2243) }} spawn in the pens around `83/58`: the first at 0:12 (10 animals), then every 3 minutes with 1-5 animals per spawn point. As in Lab No.2, the door to Lab No.4 (`83/62`) opens as soon as every spawned animal is dead.

#### Lab No.4: the experiment

After about 17 seconds of whispers, one random experiment out of thirteen wakes up from its tube:

| | | |
|---|---|---|
| {{ mob(1646) }} | {{ mob(1650) }} | {{ mob(2239) }} |
| {{ mob(1647) }} | {{ mob(2241) }} | {{ mob(2238) }} |
| {{ mob(2240) }} | {{ mob(2236) }} | {{ mob(2235) }} |
| {{ mob(2237) }} | {{ mob(1651) }} | {{ mob(1649) }} |
| {{ mob(1648) }} | | |

Killing it completes that experiment's *[Rest]* quest and makes **Wolfchev** appear at `137/156`.

### Rewards

Talk to Wolfchev after the boss dies:

- **Not all thirteen [Rest] quests done yet:** leave with 20-40 Instance Points and a warp to `lhz_dun04 147/273`.
- **All thirteen done:** Wolfchev removes the quests and gives one random reward below. Accept the quests again from the Researcher (**Going into the laboratory**, then **Why not**) to start a new collection.

| Reward | Chance |
|---|---|
| {{ item(2582) }} | 8.3% |
| {{ item(18570) }} | 8.3% |
| {{ item(1490) }} | 8.3% |
| {{ item(16017) }} | 8.3% |
| {{ item(1291) }} | 8.3% |
| {{ item(1584) }} | 8.3% |
| {{ item(6471) }} x10 | 8.3% |
| {{ item(6470) }} x10 | 8.3% |
| {{ item(6469) }} x10 | 8.3% |
| {{ item(6471) }} x20 | 8.3% |
| {{ item(6470) }} x20 | 8.3% |
| {{ item(6469) }} x20 | 8.7% |

!!! tip
    The boss is random each run, so finishing all thirteen usually takes many more than thirteen runs. Each player's quests are tracked separately, so party members can be at different points in their collection.

{{ instance_page("wolfchev-s-laboratory") }}
