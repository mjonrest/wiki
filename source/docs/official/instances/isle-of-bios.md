# Isle of Bios

## Guide

Isle of Bios is a short three-island memorial dungeon from the Morocc storyline. You clear two islands of corrupted monsters, then survive three waves and a boss fight against {{ mob(3029) }} on the final island.

### Requirements and entry

| | |
|---|---|
| Level | Base Level 160 or higher |
| Party | Required (a party of 1 is enough). Only the party leader can create the dungeon. |
| Prerequisite | Talk to **Wandering Old Man** at `/navi moro_cav 45/60` once to unlock access. |
| Entrance | **Yellow Seed** at `/navi moro_cav 50/64` |
| Cooldown | One run per day. The lockout resets daily at 04:00 server time. |

The leader talks to the Yellow Seed and picks **Create Memorial dungeon**, then everyone talks to it again and picks **Enter Isle of Bios**.

!!! note "Re-entering"
    For the first 5 minutes after your first entry you can still re-enter (for example after a disconnect). After those 5 minutes, or once you have claimed the reward, the Seed refuses entry until the daily reset. The NPC text says "23 hours", but the lockout actually ends at the next 04:00 reset.

### Walkthrough

**Island 1**

1. Walk up to Vrid and Zeith near the entrance. A short cutscene plays where Grim Reaper Ankou reveals himself.
2. Kill every monster on the island: {{ mob(3010) }}, {{ mob(3011) }} and {{ mob(3012) }}. The system announces when 10, 5 and 1 monsters are left.
3. When the island is clear, the exit portal on the east side (3 o'clock) opens. It takes you to Island 2.

**Island 2**

1. Same as Island 1, with stronger monsters: {{ mob(3013) }}, {{ mob(3014) }} and {{ mob(3015) }}.
2. Clear them all to open the east exit to Island 3.

**Island 3: the Grim Reaper**

1. Walk up to Vrid and Zeith. Ankou appears, freezes your friends and casts a Storm Gust. **Every party member within about 30 cells is frozen for 17.5 seconds.**
2. Three waves spawn one after another in the area north of the NPCs, 27 monsters each. The next wave only appears once the previous one is dead:
    1. {{ mob(3016) }}
    2. {{ mob(3017) }}
    3. {{ mob(3018) }}
3. After the third wave, {{ mob(3029) }} spawns in the middle of the arena. Kill him to free Vrid and Zeith.

### Rewards

When Ankou is dead, **each party member** talks to **Vrid** to claim their reward and is then warped back to Morocc Cave:

| Reward | Amount |
|---|---|
| {{ item(6684) }} | 1 |
| Instance Points | 20 to 40 (random) |

!!! tip "Instance Points"
    Instance Points can be earned once per device for each instance run, up to 1200 per account per day. A rented {{ item(30034) }} adds 50 points per claim. Use `@instancepoints` to see your total.

!!! tip
    Stay out of the arena until the whole party is ready. The freeze hits everyone close to the NPCs, and the first wave spawns right when it ends.

{{ instance_page("isle-of-bios") }}
