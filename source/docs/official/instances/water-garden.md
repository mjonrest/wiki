# Water Garden

## Guide

Water Garden is the Episode 17.2 instance at the Ba Maison docks. The party clears five garden areas tended by broken gardener bots, each with its own trap, and ends with a fight against {{ mob(20667) }} (Normal) or {{ mob(20668) }} (Hard).

### Requirements and entry

| | Normal | Hard |
|---|---|---|
| Level | — | Base Level 180+ (party leader) |
| Story progress | Progress in the Episode 17.2 Water Garden story | Leader must also have completed "Completion of the Antidote" |
| Party | Required, leader creates | Required, leader creates |

- **NPC:** **Harad** at `/navi ba_maison 238/44`.
- **Cooldown:** entering starts a "Water Garden - Waiting" cooldown that resets at 04:00 server time. Talk to Harad after it expires to clear it.

The leader picks **Create Water Garden** or **Create Water Garden Hard**. Everyone then picks **Garden Entrance** and the matching mode.

!!! note
    The mode is locked in when the **party leader** steps onto the entrance area inside the instance. The leader must go in first, before anyone uses the warp into the gardens.

### Mode differences

Hard mode uses stronger "Senior" monsters and spawns more of them:

| Area | Normal | Hard |
|---|---|---|
| Area 1 | 12 ({{ mob(20677) }}, {{ mob(20669) }}) | 30 ({{ mob(20678) }}, {{ mob(20670) }}) |
| Area 2 | 12 ({{ mob(20677) }}, {{ mob(20622) }}) | 27 ({{ mob(20678) }}, {{ mob(20666) }}, {{ mob(20632) }}) |
| Area 3 ambushes | 3 {{ mob(20665) }} each | 6 ({{ mob(20666) }}, {{ mob(20632) }}) each |
| Area 4 targets | {{ mob(20671) }}, {{ mob(20674) }} | {{ mob(20672) }}, {{ mob(20675) }} |
| Boss | {{ mob(20667) }} | {{ mob(20668) }} |

### Walkthrough

**Area 1: Meteor garden**

- Take the warp east of the entrance and talk to the **Gardener** at around `1@ghg 216/58` to start.
- The area clears once **fewer than 2** of its monsters are left. The rest vanish automatically.
- **Trap:** every ~24 seconds the whole party is teleported to one of eight spots in the garden. 2 seconds later a warning appears, and 2 seconds after that Papilas cast **Meteor Storm on all eight spots**, including the one you were sent to. Move away from your landing spot right after the teleport.

**Area 2: Heaven's Drive board**

- Take the warp to the next garden and talk to the **Gardener** at around `1@ghg 316/69`.
- Again the area clears once fewer than 2 monsters are left.
- **Trap:** every ~27 seconds, three Papilas appear on the 6x6 board. About 5 seconds later each one fires Heaven's Drive in lines spreading 5, 10, 15 and 20 cells outward:
    - **red** {{ mob(20673) }}: in a **cross (+)**
    - **blue** {{ mob(20676) }}: in a **diagonal (X)**
- Stand off those lines, or kill a Papila before it casts to cancel its pattern.

**Area 3: Ambush corridor**

- Warp north and walk past the **Gardener** at around `1@ghg 341/143` to start the area.
- Follow the long corridor west and back east. Hidden spots along the way spawn ambush groups. You don't have to kill them.
- At the end, talk to the **Gardener** at around `1@ghg 344/173` (5-second progress bar). This opens the warp to the maze.

!!! note
    Characters in Hiding/Cloaking do not trigger the corridor spots.

**Area 4: Maze**

- The warp drops you at a random spot in the maze.
- Only two monsters are required: the red {{ mob(20671) }} (around `1@ghg 278/241`) and the blue {{ mob(20674) }} (around `1@ghg 278/301`). In Hard mode these are the Senior versions. All other monsters in the maze are optional.
- Killing both opens the warp to the final garden.
- One of four Gardeners in the maze (chosen at random) hands out a {{ item(1000099) }} if you are on the daily quest "Searching for Gardener" (see Rewards).

**Area 5: Silva Papilia**

- Talk to **Velkina** at around `1@ghg 186/287` to summon the boss.
- Every cycle, a red Papila Ruba and a blue Papila Cae spawn in the centre, and one red and one blue **pillar** light up for 15 seconds. Lead each Papila into the light of the pillar with **its own colour** and it dies instantly.
- When the pillars go out, **everyone is pulled to the centre and loses 50% of their current Max HP** (this cannot kill you; it leaves at least 1 HP). A second later everyone is thrown to a random edge of the arena (north, south, east or west). Heal up right after the pull.
- The cycle repeats every ~18 seconds until the boss dies.

### Rewards

- Talk to **Velkina** after the boss dies. She warps you out and gives **20 to 40 Instance Points**.
- **Daily quest "Searching for Gardener"** from **Seihyu** at `/navi ba_maison 239/47`: accept it before your run, get the {{ item(1000099) }} from the gardener in the maze, then hand it in for {{ item(1000103) }} x4 and 800,000 Base / 500,000 Job EXP.

!!! tip "Instance Points"
    Instance Points can be earned once per device for each instance run, up to 1200 per account per day. A rented {{ item(30034) }} adds 50 points per claim. Use `@instancepoints` to see your total.

{{ instance_page("water-garden") }}
