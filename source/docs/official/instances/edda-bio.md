# Edda Bio

## Guide

Edda Bio is Miracle's own take on the Biolab: a long run through the Rekenber laboratory in eight rooms, ending with
the Nameless Swordsman in the lower lab. Every player gets one random Edda weapon from the treasure box, a weapon box,
Somatology materials and Instance Points. The materials are spent at the Edda enchanter in Juno.

### Entering

- **NPC:** **Sierra** at `/navi yuno 216/345`.
- **Party:** the **party leader** picks *create*; then everyone picks *enter*.
- **Level:** the script has no level check.
- **Cooldown:** entering starts the *Road of Battle* quest, which ends at the next **04:00** server time.
- **Time limit:** 1 hour.

### Walkthrough

Each room spawns its monsters when you step into it, and the whole party is moved to the next room as soon as the
last one dies. If you get left behind, the **Sierra** standing in each cleared room sends you on to the next one.

| Room | Monsters to kill |
|---|---|
| 1 | None. The party leader talks to **Sierra** next to the entrance to start. |
| 2 | 14: {{ mob(20541) }}, {{ mob(20542) }}, Regenschirm Scientists |
| 3 | 25: the same three plus {{ mob(20538) }} |
| 4 | 21: Rekenber Guards, Senior Guards and Regenschirm Scientists |
| 5 | 25: Rekenber Guards, Senior Guards, Scientists and Nameless Acolytes |
| 6 | See below |
| 7 | 33: {{ mob(20537) }}, {{ mob(20539) }}, Acolytes, Guards and Scientists |
| 8 | 17: Guards, Senior Guards, Scientists and Nameless Swordsmen |

**Room 6, the four switches**

1. Entering the room spawns 6 Rekenber Guards and seals one passage. Kill them to reopen it.
2. There are four switch areas in the room. Walking into each one spawns **11 monsters** (5 Rekenber Guards,
   5 Nameless Swordsmen, 1 Rekenber Senior Guard) and seals its exits until they are all dead.
3. When all four switch groups are cleared, the party moves to room 7.

**Room 8 to the boss**

Room 8 does not move you on by itself. After clearing it, talk to **Sierra** in the room to go down to the lower lab.

**Boss: {{ mob(20536) }}**

Walk to **Sierra** in the middle of the lower lab and talk to her to start the fight. The whole party is pulled to her,
the door behind you closes and the Nameless Swordsman appears just south of her. Then, in a loop:

1. Over about 8 seconds, walls rise to form **four pens** around the middle of the room, and one extra monster
   appears in each pen.
2. 5 seconds later, if the boss is still alive, the pen monsters vanish and the whole party is pulled back to the
   middle.
3. The walls drop, and 5 seconds later the cycle starts again.

Fight in the open corridor between the pens so the walls do not lock you away from the boss.

### Rewards

When the boss dies, a **treasure box** appears south of Sierra and Sierra comes back.

| Source | Reward (each player) |
|---|---|
| Treasure box | 1 random Edda weapon (38 possible weapons), once per entry |
| Sierra | 9 {{ item(25786) }} and 15 {{ item(25787) }} |
| Sierra | 100-200 {{ item(25786) }} and the same amount of {{ item(25787) }} |
| Sierra | 1 {{ item(23806) }} |
| Sierra | 20-40 Instance Points (up to the daily cap of 1,200 points) |

!!! warning "Open the box first"
    Talking to Sierra gives her rewards and immediately sends you back to Juno. Open the treasure box before you talk
    to her, or you lose the weapon.

### Enchanting Edda weapons

The **enchant** NPC ("Edda bio enchants") at `/navi yuno 210/340` enchants the Edda weapon you have equipped, using
{{ item(25786) }} and {{ item(25787) }}. Refine level and cards are kept.

| Slot | Possible enchants |
|---|---|
| 4th slot (done first) | {{ item(4832) }}, {{ item(4833) }}, {{ item(4834) }}, {{ item(4808) }}, {{ item(4820) }}, {{ item(4821) }}, {{ item(4818) }}, {{ item(4817) }}, {{ item(4816) }}, {{ item(4863) }}, {{ item(4864) }}, {{ item(4865) }}, {{ item(4815) }}, {{ item(4814) }}, {{ item(4813) }} |
| 3rd slot (done second) | {{ item(29594) }}, {{ item(29595) }}, {{ item(29596) }}, {{ item(29598) }}, {{ item(29599) }}, {{ item(29600) }}, {{ item(29601) }}, {{ item(29602) }}, {{ item(29603) }}, {{ item(29604) }}, {{ item(29605) }}, {{ item(29606) }}, {{ item(29607) }} |

| Action | Normal mode | Safe mode |
|---|---|---|
| Add an enchant (empty slot) | 50 of each material, **40%** chance the weapon is destroyed | 500 of each material, no risk |
| Reroll the 3rd slot | 500 of each material, 20% chance the weapon is destroyed | 2,000 of each material, no risk |
| Reroll the 4th slot | 200 of each material, 20% chance the weapon is destroyed | 1,000 of each material, no risk |

!!! warning "Known issue"
    Rerolling in **normal mode** takes the materials (and can destroy the weapon) but never changes the enchant. Only
    **safe mode** actually rerolls. The NPC also understates the risks: it says 5% for normal rerolls and suggests
    first-time enchants are fairly safe.

{{ instance_page("edda-bio") }}
