# Central Laboratory

## Guide

You go back in time to the last day of the Central Laboratory's particle accelerator experiment. You get through
the lab doors with the day's access code, then watch the experiment go wrong. Over **three rounds** the Mother
Computer pulls a random boss out of another dimension, and you kill each one to move on. The bosses are random
picks from a list of classic MVPs and mini-bosses, so no two runs are the same.

### Entering

- **Level:** 135 or higher.
- **Quest:** the first time, talk to the **Civilization Explorer** at `/navi verus01 149/155` and agree to help.
- **Party:** you must be in a party. The **party leader** talks to the Civilization Explorer and picks
  *Produce a crack of time*. Everyone then enters through the **Temporary Dimension-mover** at
  `/navi verus01 153/155`.
- **Cooldown:** entering gives you *Trace of Laboratory Access*. It ends at the next **04:00** server time. When it
  has ended, talk to the Civilization Explorer or the device once to clear it.

!!! warning
    The Civilization Explorer warns that taming monsters in here will break the run's progress.

### Walkthrough

**1. Get through the door**

1. The leader talks to the **Probationary researcher** at the entrance (`1@lab 104/34`) and agrees to take part.
   The corridor warps heading west open.
2. Talk to the **Senior researcher** (`1@lab 45/32`). They tell you **today's access code**.
3. Enter the code in binary on the **8 switches** behind them (Switch 1 to Switch 8, left to right). Then press the
   **Main Switch** (`1@lab 34/37`). The doors north and into the lab open.

!!! tip "Working out the code"
    The code is **(month + day of the month) × 5**, using the server date. Write it as an 8-digit binary number.
    Switch 1 is the leftmost digit, and each 1 means **ON**. For example, on 5 October the code is
    (10 + 5) × 5 = 75 = `01001011`. That means switches 2, 5, 7 and 8 are ON and the rest are OFF.

**2. The experiment**

Walk up to the four doctors around the particle accelerator in the middle of the lab (around `1@lab 80/89`). Dr.
Lona Fresa starts the experiment over the announcements. After a short countdown, an **"Unidentified creature"**
appears in the middle of the accelerator (`1@lab 90/88`). Kill it and the next round begins on its own.

| Round | Possible bosses |
| --- | --- |
| 1 | {{ mob(1087) }}, {{ mob(1147) }}, {{ mob(1190) }}, {{ mob(1115) }}, {{ mob(1086) }}, {{ mob(1038) }}, {{ mob(1159) }}, {{ mob(1389) }}, {{ mob(1046) }}, {{ mob(1059) }}, {{ mob(1150) }}, {{ mob(1688) }}, {{ mob(1039) }} (6.7% each) |
| 2 | {{ mob(1980) }}, {{ mob(1157) }}, {{ mob(1112) }}, {{ mob(1251) }}, {{ mob(2068) }}, {{ mob(1373) }}, {{ mob(2156) }}, {{ mob(1272) }}, {{ mob(1630) }}, {{ mob(1252) }}, {{ mob(1779) }}, {{ mob(1708) }} (7.1% each) |
| 3 | {{ mob(1623) }}, {{ mob(1418) }}, {{ mob(1312) }}, {{ mob(1785) }}, {{ mob(1734) }}, {{ mob(1719) }}, {{ mob(1768) }}, {{ mob(2087) }}, {{ mob(1751) }}, {{ mob(2253) }}, {{ mob(2255) }}, {{ mob(1832) }}, {{ mob(1874) }} (6.7% each) |

In every round there is also a small chance that a mini-boss comes through instead: {{ mob(1089) }},
{{ mob(1092) }}, {{ mob(1088) }}, {{ mob(1096) }}, {{ mob(1093) }}, {{ mob(1120) }} or {{ mob(1090) }} (about 2%
each, so 13–14% in total).

**3. The way out**

When the third creature dies, the Mother Computer moves the whole lab into the other dimension and the scientists
vanish. A gateway opens at the 3 o'clock side of the lab. Talk to the researcher at the **Exit** (`1@lab 123/88`)
to leave.

### Rewards

- The bosses drop their normal loot.
- Leaving through the **Exit** gives **20–40 Instance Points** (+50 with {{ item(30034) }}, within the daily
  Instance Point limit) and takes you back to `verus01`.

{{ instance_page("central-laboratory") }}
