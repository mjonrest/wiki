# Culvert

## Guide

Help Missing the cat clean Malangdo's culverts. Drains open one after another across the map, each one guarded by
deep-sea monsters; someone has to reach the drain and "clean" it before it overflows with seaweed. Survive all ten
drains and a Coelacanth boss rises from the abyss. There is a normal mode (level 90+) and a hard mode (level 140+).

### How to enter

| | |
|---|---|
| **NPC** | Missing, the Cleaner in Malangdo: `/navi mal_in01 160/34` |
| **Level** | 90+ (hard mode: 140+) |
| **Party** | Required. The party leader creates the instance by answering *"Aragam insulted me."* |
| **Required item** | Every player needs a {{ item(6436) }} in their inventory to talk to Missing |
| **Cooldown** | 1 hour per character, starting when you enter |
| **Time limit** | 1 hour |

The first time, talk Missing through his story to receive the password memo.

### Choosing the mode

Inside, the **party leader** talks to Missing at the start:

- *"I'm pretty good at delivering bread."* starts **normal mode** on the first map.
- *"I know how to fight."* starts **hard mode** (leader must be level 140+). Missing opens a gate to the east; players
  of level 140+ who step in go to the hard map, everyone else is sent to the normal map instead.

Then walk east and talk to Missing again to start cleaning.

!!! warning
    In hard mode, party members below level 140 cannot reach the hard map. Bring a party where everyone is 140+.

### How the cleaning works

| | Normal | Hard |
|---|---|---|
| Drains in total | 10 | 10 |
| Possible drain spots | 6 | 10 |
| New drain every | 50 seconds | 40 seconds |
| Time to clean a drain | 10-second cast | 15-second cast |
| Drain overflows after | about 50 seconds | about 40 seconds |
| Monsters per drain | 1~3 of each of six deep-sea monsters | 2~3 of each of six deep-sea monsters |

1. A new drain opens at a random spot (5 seconds of warning first). It is surrounded by fresh monsters.
2. Any player can click the drain to clean it. The cleaner casts for 10 seconds (15 in hard mode); once the cast
   finishes the drain is closed safely.
3. If nobody cleans it in time, the drain closes on its own, its monsters vanish, and a **Contaminated Seaweed**
   ({{ mob(2191) }}) grows at the starting area.
4. Seaweed is counted each time the fifth to tenth drains open, and once more at the end. If **6 or more seaweeds**
   are alive at any check, Missing calls the run a failure; talk to him to restart the cleaning.

!!! tip
    Seaweeds can be killed. If you miss drains, go back and kill seaweeds before the next check to stay under 6.

### The Coelacanth

About 20 seconds after the tenth drain, if fewer than 6 seaweeds remain, a Coelacanth appears somewhere on the map
(50/50 which one):

| Mode | Possible bosses |
|---|---|
| Normal | {{ mob(2188) }} or {{ mob(2187) }} |
| Hard | {{ mob(2189) }} or {{ mob(2190) }} |

Killing it opens the exit and drops **10 random items** on the floor near the start:

| Item | Normal | Hard |
|---|---|---|
| {{ item(12636) }} | 78.1% | - |
| {{ item(12615) }} | 7.8% | 40% |
| {{ item(12621) }} | 7.8% | 20% |
| {{ item(12620) }} | 3.1% | 20% |
| {{ item(12619) }} | - | 10% |
| {{ item(12623) }} | 3.1% | 10% |

### Daily and weekly services

**Albo** (`/navi mal_in01 172/28`, level 90+) gives cleaning jobs; **Madeca** next to him (`/navi mal_in01 172/26`)
pays for them. Each job asks you to hunt one random culvert monster (or one of the two Coelacanths for the weekly
jobs).

| Job | Level | Repeat | Reward |
|---|---|---|---|
| General Culvert Daily Service | 90+ | Daily (resets 04:00) | 2 {{ item(6419) }} |
| Hard Culvert Daily Service | 140+ | Daily (resets 04:00) | 1 {{ item(6418) }} |
| General Culvert Weekly Service | 90+ | Every 7 days (at 04:00) | 1 {{ item(6423) }} |
| Hard Culvert Weekly Service | 140+ | Every 7 days (at 04:00) | 5 {{ item(6423) }} |

{{ instance_page("culvert") }}
