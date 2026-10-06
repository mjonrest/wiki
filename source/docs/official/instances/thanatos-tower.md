# Thanatos Tower

## Guide

Thanatos Tower is a custom multi-floor instance. A central hub connects to the tower's floors, and each floor has to be cleared to open the warp to the next one. Each floor ends with one of Thanatos's guardians, and the run finishes with Thanatos himself at the top.

### Requirements and entry

| | |
|---|---|
| Level | Base Level 180 or higher |
| Party | Required. Only the party leader can create the instance, and only the leader can trigger events inside. |
| Entrance | **Thanatos Tower Entry** at `/navi thana_step 154/367` |
| Cooldown | Once per day per character. Entering starts the cooldown, which resets at 04:00 server time. |

The leader picks **Generate Thanatos Tower** (and is sent in right away). The rest of the party picks **Enter Thanatos Tower**.

!!! note
    Teleport, Ice Wall and saving are disabled on every tower floor. The system announces how many monsters are left on the current floor after each kill.

### Walkthrough

The first map is a hub. Each time a floor is cleared, a new pair of warps opens in the hub: one leads to the next floor, the other brings you back.

| # | Floor | Trigger | Monsters to clear | Floor guardian |
|---|---|---|---|---|
| 1 | Observation floor (from the hub's first warp) | Leader walks up to the Guardian at around `2@thts 57/171` | 37 {{ mob(20800) }} | — |
| 2 | Next floor | Opens when floor 1 is cleared | 20 {{ mob(20789) }} | {{ mob(20797) }} |
| 3 | Next floor | Opens when the guardian dies | 25 {{ mob(20791) }} | {{ mob(20798) }} |
| 4 | Next floor | Opens when the guardian dies | 25 {{ mob(20790) }} | {{ mob(20799) }} |
| 5 | Next floor | Opens when the guardian dies | 45 {{ mob(20787) }} / {{ mob(20788) }} | {{ mob(20796) }} |
| 6 | Seal room | Opens when the guardian dies | 15 (3 each of the five floor monsters) | 4 guardians (see below) |
| 7 | Thanatos's chamber | Opens when the 4 guardians die | — | {{ mob(20784) }} or {{ mob(20785) }} |

Each guardian spawns as soon as the last monster on its floor dies.

**Seal room.** After the 15 monsters die, four ancient devices light up in the middle of the room. The leader activates each one. Every device summons a guardian: one {{ mob(20798) }} and three {{ mob(20799) }}. When all four are dead, the warp to Thanatos's chamber opens.

!!! note
    The devices mention keys, and some guardian-shaped NPCs let the leader collect fragments ({{ item(7439) }}, {{ item(7437) }}, {{ item(7436) }}, {{ item(7438) }}). The devices **do not check or take** these items, so you can activate them without any keys.

**Thanatos.** The leader walks up to the dormant guardian in the chamber (around `8@thts 135/139`). After a short awakening, either {{ mob(20784) }} or {{ mob(20785) }} spawns (random). While he is alive, two groups of adds spawn in the north-east part of the room 50 seconds after the fight starts, and again 50 seconds after any of those adds dies:

- 2 {{ mob(20792) }}
- 4 of one random type: {{ mob(20793) }}, {{ mob(20794) }} or {{ mob(20795) }}

Killing Thanatos stops the adds and makes the Reward NPC appear.

### Rewards

Each player talks to the **Reward** NPC (around `8@thts 140/131`) and picks one option. You are then warped to Prontera.

| Option | Guaranteed | Also |
|---|---|---|
| Reward Option 1 | {{ item(1000257) }} x10, {{ item(102572) }} x1 | — |
| Reward Option 2 | {{ item(1000263) }} x10, {{ item(102572) }} x1 | 20 to 40 Instance Points |

With either option there is also a **1% chance** of one random bonus item from this list:

- {{ item(400023) }}
- {{ item(436000) }}
- {{ item(436001) }}
- {{ item(436002) }}
- {{ item(480136) }}
- {{ item(490099) }}

!!! warning
    Only **Reward Option 2** gives Instance Points.

!!! tip "Instance Points"
    Instance Points can be earned once per device for each instance run, up to 1200 per account per day. A rented {{ item(30034) }} adds 50 points per claim. Use `@instancepoints` to see your total.

{{ instance_page("thanatos-tower") }}
