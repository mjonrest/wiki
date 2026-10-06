# Sanctuary Purification

## Guide

Sanctuary Purification is the daily Episode 18 instance that takes place in the same temple district as Wolves Gathering Place. It has two raids, which you can take separately or together:

- **Raid on the defected temple guards**: clear the renegade guards from four zones of the temple square (first map).
- **Raid on the Heart Hunters**: clear the Heart Hunters from the temple vaults and reset the vault security codes (second map).

### Requirements and entry

| | |
|---|---|
| Level | Base Level 170 or higher |
| Prerequisite | Clear the Episode 18 story instance Wolves Gathering Place. |
| Party | Required. The party leader creates the instance and triggers every encounter. |
| NPC | **Priest** in Rachel, `/navi rachel 167/244` (she appears after you talk to the Ordinary Person next to her) |
| Cooldown | Once per day. Entering starts the cooldown, which resets at 04:00 server time. |

1. Talk to the Priest and choose which raid(s) to accept: **Since we're doing it, let's do both.**, **Raid on the defected temple guards.** or **Raid on the Heart Hunters.**
2. Talk to her again. The leader picks **Alright. I'll send the signal.** to create the instance, and everyone picks **I'll proceed.** to enter.

!!! note
    You can only get credit for a raid you accepted **before** finishing it. Both raids can be completed in the same run.

### Part 1: Temple square (defected temple guards)

1. The leader walks forward from the entrance to meet the temple guards. This starts the raid.
2. The square is split into **4 zones** by walls. In each zone, Temple Guard NPCs stand at set points. When the **leader walks up to one**, it turns hostile: a group of {{ mob(21311) }} spawns around it, along with more {{ mob(21310) }} / {{ mob(21311) }} (random) at nearby spots.
3. Kill everything from that group. The next guard is then revealed and a system message says whether enemies remain in the zone. Each zone has 2 or 3 groups. When a zone is cleared, the passage to the next zone opens.
4. After all 4 zones are cleared, gather at the temple entrance. The leader talks to the **Temple Guard** in front of the temple (around `1@nyr 119/175`), which opens the portal to the vaults.
5. **Each player who walks through that portal** is credited with the guard raid.

### Part 2: The vaults (Heart Hunters)

1. Walk forward from the arrival point. A Temple Guard tells everyone **today's 4-digit security code**. It is random each run. If you forget it, talk to the Temple Guard at around `2@nyr 35/187` again.
2. The leader walks up to each Heart Hunter NPC in turn to start a fight against {{ mob(21312) }}. The vaults have three storage rooms. For each one:
    - clear the corridor groups, then the storage room itself;
    - the leader steps out through the storage exit, then enters the security code at the **Security Device** to reset that storage.
3. After the third storage, clear the centre group. The path north to the storage room opens.
4. In the storage room the leader steps into the middle to trigger the final fight: 8 Resonators ({{ mob(21312) }}) and one {{ mob(21313) }}.
5. Afterwards, the leader enters the code at the last **Security Device** (around `2@nyr 124/138`), the guards gather near the exit, and the leader walks up to them to finish.
6. Leave through the exit in the north-east (around `2@nyr 203/220`). **Each player who uses this exit** after the final scene is credited with the Heart Hunter raid and returned to Rachel.

!!! warning "Known issue"
    After the Resonators die, the script closes the warps into the final storage room but never opens the warp out of it. Teleporting is disabled on these maps, so the party may get stuck in that room and be unable to finish the **Heart Hunter** raid. The temple guard raid (Part 1) is not affected, since it is credited as you enter the vaults.

### Rewards

Return to the **Priest** in Rachel and talk to her to turn in your completed raids:

| Completed raid | Reward |
|---|---|
| Raid on the defected temple guards | {{ item(1000405) }} x2 |
| Raid on the Heart Hunters | {{ item(1000405) }} x2 |
| Turning in (once, either or both) | 20 to 40 Instance Points (random) |

Rewards are given per player, so every party member should accept the raids and turn them in.

!!! tip "Instance Points"
    Instance Points can be earned once per device for each instance run, up to 1200 per account per day. A rented {{ item(30034) }} adds 50 points per claim. Use `@instancepoints` to see your total.

{{ instance_page("sanctuary-purification") }}
