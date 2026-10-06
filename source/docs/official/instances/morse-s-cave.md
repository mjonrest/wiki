# Morse's Cave

## Guide

Morse's Cave (the "Red Flower") is the follow-up to Isle of Bios. The party tracks the weakened Demon God Morocc into his lair, holds off his army in three timed survival rooms, and finally fights the {{ mob(3000) }}.

### Requirements and entry

| | |
|---|---|
| Level | Base Level 160 or higher |
| Prerequisite | Clear Isle of Bios and claim the reward from Vrid at least once. |
| Party | Required. Only the party leader can open the dungeon. |
| Open the dungeon | **Senior Tracker** at `/navi moro_cav 61/69` (party leader) |
| Entrance | **Red Flower** at `/navi moro_cav 57/69` |
| Cooldown | One run per day. Resets daily at 04:00 server time, counted from the moment you report back to the Senior Tracker. |

The leader talks to the Senior Tracker and answers **Yes** to open the Red Flower. Everyone then enters through the Red Flower next to him.

!!! warning "You only get one entry"
    Entering the Red Flower starts the "Pursuing Hiding Morocc" quest, and the Red Flower stays closed to you while that quest is active. If you die, disconnect or fail, you **cannot go back in**. Report to the Senior Tracker, then wait for the next daily reset.

### Walkthrough

**1. The entrance**

Walking in wakes Morocc up and 9 {{ mob(3001) }} spawn along the corridor. Kill them all. Grim Reaper Ankou then appears, and after his speech three portals open that lead to Morocc's chamber.

**2. Weakened Morocc**

Step into the chamber to trigger a cutscene, after which {{ mob(2998) }} spawns. Kill it. Morocc talks some more and then four portals open around the chamber.

!!! note
    Only the **party leader** can use these portals (and the ones later in the dungeon). When the leader steps in, the whole party is teleported and split between the next rooms.

**3. The split rooms (left and right)**

The party is split between two rooms. In each room Morocc freezes you for a few seconds, then waves keep spawning for **3 minutes**:

- 4 {{ mob(3001) }} at the start and then about every 20 seconds
- one {{ mob(3003) }} each at around 2:40 and 2:50

At the 3-minute mark the script counts the monsters still alive in each room. **If 20 or more are left in a room, the run fails:** Ankou appears and the portals send everyone to Prontera. Otherwise the remaining monsters vanish and new portals open. The leader steps in and the party regroups in the next room.

**4. The lower-left room**

This works the same way, also for **3 minutes**, but each wave adds more {{ mob(3003) }} and {{ mob(3005) }} to the 4 Ghouls. The same rule applies: **20 or more monsters alive at the end means failure.** If you survive, the leader takes the portal to the final room.

**5. Morocc Necromancer**

1. Morocc hands the fight over to his Necromancer. The first form, {{ mob(2999) }}, spawns. Kill it.
2. The second form, {{ mob(3000) }}, appears in the same spot and keeps summoning adds about every 7 seconds. The fewer adds are alive, the bigger the wave. It stops summoning while 40 or more are alive. Waves mix {{ mob(3001) }}, {{ mob(3003) }}, {{ mob(3004) }}, {{ mob(3005) }} and {{ mob(3006) }}.
3. Many waves also bring a {{ mob(3002) }} that drops poison clouds where it stands every few seconds. Kill Osiris quickly or move away from it.
4. When the Necromancer dies, all remaining adds vanish, Ankou has a last word and an exit portal opens in the middle of the room.

!!! warning "Healing mechanic"
    Every 30 seconds, if the second-form Necromancer is below 3,000,000 HP, it is healed back to exactly 3,000,000 HP. Bring it down to around 3M, then burst it down from there before the next heal.

### Rewards

| When | Reward | Who |
|---|---|---|
| Using the exit portal after the Necromancer dies | 20 to 40 Instance Points (random) | Each player who uses the portal |
| Reporting back to the **Senior Tracker** | {{ item(6684) }} x1 (only if you were credited with the second-form Necromancer kill) | Each player |

Reporting to the Senior Tracker after a run is required either way. It closes your current quest and starts the daily cooldown.

!!! tip "Instance Points"
    Instance Points can be earned once per device for each instance run, up to 1200 per account per day. A rented {{ item(30034) }} adds 50 points per claim. Use `@instancepoints` to see your total.

{{ instance_page("morse-s-cave") }}
