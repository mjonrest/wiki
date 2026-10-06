# Airship Destruction

## Guide

Airship Destruction is an Episode 19 instance. Your party climbs aboard the Isgard airship on a forged ticket,
fights through four areas of broken patrol robots and then shuts down the airship's core, {{ mob(21531) }}. You
pick the difficulty yourself by choosing a seat class at the start.

### Entering

- **Requirement:** you must be far enough in the **Episode 19 main story** to have been sent to destroy the
  airship. The first time you click the **Rope** at `/navi jor_nest 22/255`, you decode Reiji's note, which
  unlocks the instance.
- **Party:** you must be in a party. Any member clicks the Rope and picks *Rope to Airship* to create the instance,
  then everyone clicks it again and picks *Enter using rope*.
- **Cooldown:** entering gives you *Neutralization of Unfairness*, a **4-hour** cooldown. When it has passed,
  click the Rope once to clear it.
- **Time limit:** the instance lasts **1 hour** and closes after 5 minutes with nobody inside.

### Choosing the difficulty

When the **party leader** steps into the starting area, a **Management robot** walks up to the party. The leader
talks to it:

- *Change seat class* sets the difficulty. You can only change it before the run starts.
- *Send out any message* starts the run with the current class.

| Seat class | Difficulty | Patrol HP | Aquila HP | Aquila HP regen | Aquila RES / MRES |
| --- | --- | --- | --- | --- | --- |
| Economy (default) | Easy | 2,500,000 | 300,000,000 | 100,000 per second | 0 / 0 |
| Business | Medium | 4,000,000 | 500,000,000 | 1,000,000 per second | 100 / 100 |
| First Class | Hard | 5,000,000 | 600,000,000 | 1,000,000 per second | 200 / 200 |

Aquila also takes less damage the higher the class (a damage-reduction buff of level 1, 5 and 8).

### Walkthrough

The airship has four patrol areas. Each starts when the **party leader** walks through the portal into it, and
the portal onward stays closed ("movement is prohibited in case of battle") until every patrol in the area is dead.
An announcement counts down the last 10 patrols.

| Area | Portal in | Easy | Medium | Hard |
| --- | --- | --- | --- | --- |
| 2: corridor | `1@whl 53/74` | 10 | 16 | 31 |
| 3: cargo hold and rest area | `1@whl 53/97` | 40 | 47 | 59 |
| 4: engine room entrance | `1@whl 37/162` | 9 | 17 | 30 |
| 5: engine room | `1@whl 160/43` | 40 | 48 | 60 |

The patrols are {{ mob(20631) }}, {{ mob(20633) }}, {{ mob(20639) }} and {{ mob(20641) }}, plus a few
**District Inspectors** ({{ mob(20342) }}) that take much less damage than the rest. Every patrol spawns with a
random Holy or Shadow element, so check before you pick your element.

After area 5, the portal at `1@whl 160/117` leads to the core room. From then on the very first portal also
takes you straight there. The party leader talks to the core at `1@whl 160/166` to start the boss fight.

### Aquila

Aquila's attacks unlock as you deal damage to it:

| Damage dealt | Mechanic | What to do |
| --- | --- | --- |
| 5,000,000 | **Protection process:** "Activate automatic protection process" is followed 2 seconds later by Max Pain. Repeats every 150 seconds. | Ease off damage when you see the warning. |
| 5,000,000 | **Berserkaizer** (random): Aquila's attack range becomes 8 and it runs away from its target. | Click the device at `1@whl 159/173` (2-second cast) to cancel it. |
| 15,000,000 | **Cleaning robots:** 20 Broken cleaning robots spawn around the room. After about 13 seconds they cast Light of Sun, then they self-destruct 2 seconds later. This repeats for the whole fight. | They are immune to skills and status effects. Spread out or get clear of them before they blow up. |
| 50,000,000 | **Yellow ether** (random): Aquila uses Unlimit and Light of Sun, and a yellow spot appears at `1@whl 173/161` or `1@whl 146/161`. | Pull Aquila onto the spot. 2 seconds later the buffs end. |
| 100,000,000 | **Green ether** (random): Aquila gets a level 10 damage-reduction buff and Berserk, and a green spot appears in one of the four corners. | Pull Aquila onto the spot. It is teleported somewhere in the room and loses its defence for **5 seconds**. Burst it then. |

!!! warning
    On Medium and Hard, Aquila regenerates **1,000,000 HP every second**. Make sure your party can out-damage
    this before choosing Business or First Class.

### Rewards

When Aquila dies:

- **Medium:** a {{ mob(21853) }} spawns. **Hard:** a {{ mob(21854) }} spawns. Break it for extra loot.
- **10% chance** of a relic dropping where Aquila died: {{ item(102564) }} on Easy and Medium, or
  {{ item(102565) }} on Hard.

Then every player clicks the **portal** in the middle of the room (`1@whl 160/160`) to collect their personal
reward, once per run:

| Reward | Easy | Medium / Hard |
| --- | --- | --- |
| {{ item(1000608) }} | 4 | 9 |
| {{ item(1000811) }} | 1 | 2 |
| Isgard reputation | +10 | +15 |
| Base EXP | 10 × 1,605,000 | 10 × 1,605,000 |
| Job EXP | 3,000,000 | 3,000,000 |
| Bonus at 3,000 Isgard reputation | +2 {{ item(1000608) }} | +2 {{ item(1000608) }} |

Click the portal again and choose *Exit* to return to `jor_nest`. Leaving gives **40–60 Instance Points**
(+50 with {{ item(30034) }}), within the server's daily Instance Point limit.

!!! note
    Hard (First Class) currently gives the same personal reward as Medium. Its extra value is the
    {{ mob(21854) }} and the First Class relic.

{{ instance_page("airship-destruction") }}
