# Orc's Memory

## Guide

Relive the memory of the orc Kruger as he tries to stop the Orc Shaman Cargalache. The run has two floors: on the
first you hunt down Enchanted Orcs to unseal four zones, on the second the party leader lights braziers in order
while the party fights three mini-bosses and finally the Shaman herself.

### How to enter

| | |
|---|---|
| **NPC** | Dimensional Gorge Piece (a statue) in the Geffen field: `/navi gef_fild10 242/202` |
| **Level** | 30 ~ 80 |
| **Party** | At least 2 members. The party leader reserves the dungeon, then everyone selects "Enter" |
| **Cooldown** | 2 hours per character, starting when you enter |
| **Time limit** | 1 hour |

The Mad Scientist standing next to the statue only gives story dialogue; he is not needed to enter.

### Floor 1: the four sealed zones

1. Talk to **Kruger** at the starting point. He explains the plan over about a minute of messages.
2. When the mission starts, the floor fills with endlessly respawning {{ mob(1023) }}, {{ mob(1106) }} and
   {{ mob(1189) }} (plus {{ mob(1627) }} from the start). A minute after you talked to Kruger, the first
   **Enchanted Orc** (an Orc Warrior with a special name) appears around 140/86.
3. Each Enchanted Orc you kill opens a portal to the next zone and spawns the next Enchanted Orc:

    | Kill the Enchanted Orc near | Portal that opens | Next Enchanted Orc near |
    |---|---|---|
    | 140/86 | 168/125 | 106/108 |
    | 106/108 | 89/94 | 35/43 |
    | 35/43 | 38/105 | 22/180 |
    | 22/180 | 21/189, to floor 2 | (none) |

4. Killing the last Enchanted Orc removes all the respawning monsters on floor 1.

!!! tip "Be sneaky"
    Every normal orc you kill is replaced, and most replacements are **High Orcs** placed at the last path (around
    22/182), the same spot you need to reach for the floor 2 portal. Rarely, killing orcs also calls 20
    {{ mob(1278) }} into that area. Only kill what blocks your way.

### Floor 2: the braziers

1. Talk to **Kruger** again at the start. After about 24 seconds the mission begins and {{ mob(1152) }},
   {{ mob(1153) }}, {{ mob(1189) }} and {{ mob(1627) }} start respawning.
2. **Only the party leader** can light a brazier (a 5-second progress bar). There are three sets of four, and each
   set must be lit in order; the next brazier only becomes active after the previous one is lit.
3. Lighting the last brazier of a set spawns a mini-boss. Killing it opens the portal to the next area:

    | Brazier set | Mini-boss | Portal after the kill |
    |---|---|---|
    | 26/164, 55/155, 108/146, 98/171 | {{ mob(1981) }} at 109/156 | 48/100 |
    | 35/92, 32/70, 70/31, 84/51 | {{ mob(1982) }} at 67/64 | 101/55 |
    | 142/145, 162/134, 144/117, 136/98 | {{ mob(1983) }} at 152/147 | 167/104 |

4. After the third mini-boss, **Shaman Cargalache** ({{ mob(1984) }}) appears at the altar (185/8) together with an
   {{ mob(1087) }}. Killing the Shaman clears the floor's respawning monsters, reveals Kruger's body at 172/13 and
   opens a portal at 182/8 back to `gef_fild10`.

!!! tip
    As on floor 1, the respawning orcs on floor 2 gather at the Shaman's altar, and very rarely 30 {{ mob(1475) }}
    are summoned there. After each mini-boss dies, another copy of it respawns near the area's entrance about 10
    seconds later, so move on quickly.

### Rewards

The script gives no completion reward: the loot is what the monsters and bosses drop (see the tables below).

{{ instance_page("orc-s-memory") }}
