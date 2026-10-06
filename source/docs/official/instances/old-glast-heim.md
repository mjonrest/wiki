# Old Glast Heim

## Guide

Travel back to the night Glast Heim fell. Himelmez has come for the piece of Ymir's Heart, and you fight through
the castle grounds, kill the {{ mob(2475) }}, hunt the two Commanders of Destruction on the second floor and finally
put down the cursed knight {{ mob(2476) }}. On Miracle there are two difficulties: **Normal** and **Hard** (shown as
*Old Glast Heim Advanced*). Hard uses much stronger monsters and pays {{ item(6755) }} instead of
{{ item(6608) }}.

### Entering

Talk to **Hugin** at `/navi glast_01 204/273`. The first time, agree to help him. Then pick a mode:

| Mode | Level | Extra requirement | Cooldown quest |
| --- | --- | --- | --- |
| Normal | 130+ | None | *Trace of Time Travel* (Normal) |
| Hard (*Old Glast Heim Advanced*) | 160+ | You must have cleared Normal once and left through Hugin at the end | *Trace of Time Travel* (Hard) |

- **Party:** you must be in a party. The **party leader** picks the mode and *Generate Time Gap*. Everyone then
  picks **the same mode** and *Enter*. Each member must meet that mode's requirements.
- **Cooldown:** each mode has its own cooldown, so you can run Normal and Hard on the same day. Each one ends at
  the next **04:00** server time. When it has ended, talk to Hugin once to clear it.
- Talking to Hugin also gives you the *Corrupted Soul Hunt* quest for the first boss. You need it for the first
  reward.

### Difficulty

| | Normal | Hard |
| --- | --- | --- |
| Monsters | {{ mob(2464) }}, {{ mob(2465) }}, {{ mob(2466) }}, {{ mob(2468) }}, {{ mob(2469) }}, {{ mob(2470) }}, {{ mob(2471) }}, {{ mob(2472) }} | {{ mob(3139) }}, {{ mob(3140) }}, {{ mob(3141) }}, {{ mob(3143) }}, {{ mob(3144) }}, {{ mob(3145) }}, {{ mob(3146) }}, {{ mob(3147) }} |
| First boss | {{ mob(2475) }}: Lv 150, 1,820,000 HP | {{ mob(3151) }}: Lv 180, 18,200,000 HP |
| Commanders | {{ mob(2473) }}, {{ mob(2474) }} | {{ mob(3148) }}, {{ mob(3149) }} |
| Final boss | {{ mob(2476) }}: Lv 150, 4,290,000 HP | {{ mob(3150) }}: Lv 180, 42,900,000 HP |
| Boss material | {{ item(6608) }} | {{ item(6755) }} |

### Fast mode

If the **party leader** has finished the **Normal** story at least once (they have *Time Conqueror*), **Varmundt**
at the entrance offers *Omit moderately*. This also works in Hard mode. This skips the three courtyard sectors: after a short scene, a blue gate
takes you straight to the first boss. The Commanders also show up more often in fast mode (see below).

### Walkthrough

**Castle grounds (`1@gl_k`)**

1. The leader talks to **Varmundt** at the entrance, then to **Heinrich** in the hall full of knights. A long scene
   follows (about 2.5 minutes). When it ends, the knights turn and are wiped out, and a portal opens to the west.
2. **Sector 1 (west):** 51 monsters. Once **36** are dead, the rest vanish. The leader then talks to
   **Altar boy Domun** (`1@gl_k 17/51`).
3. **Sector 2 (east):** 69 monsters. Once **57** are dead, the rest vanish. The leader talks to
   **Holgren the Destroyer** (`1@gl_k 291/145`). Dead bodies lying around this sector each release 3–7
   {{ mob(2467) }} when you walk past.
4. **Sector 3 (north-west):** 100 monsters. Once **86** are dead, the rest vanish and Himelmez waits for you north
   of the castle.
5. Walk up to **Himelmez** (`1@gl_k 150/257`). After the scene, the **Corrupted Soul** spawns. Kill it and the
   2nd floor entrance opens at the 12 o'clock end of the courtyard.

!!! tip "Talk to Varmundt after the first boss"
    Every player should talk to **Varmundt** next to the first boss after it dies. He gives the first reward and
    the *Amdarais Hunt* quest. **Without that quest, Hugin will not give you the final reward.**

**Second floor (`2@gl_k`)**

1. Walk into the hall where Heinrich and Varmundt stand. A portal opens to the west.
2. **West wing:** walking into each of the 7 marked spots spawns 5 monsters (a Palace Guard, an Archer, an
   Abysmal Knight, a Khalitzburg and a Bloody Knight). The spots refill over time. Every kill has a **1 in 50**
   chance (**1 in 10** in fast mode) to call the **1st Commander of Destruction**. Kill the Commander to open the
   east wing.
3. **East wing:** the same, with 44 fixed monsters plus 7 spots. Kill the **2nd Commander of Destruction**
   to open the portal at the end of the central corridor.
4. Walk up the corridor. Decomposed bodies along the way release 3–7 Maggots when you get close.

**Final boss: Amdarais**

Walk up to **Himelmez**. Gerhalt turns into {{ mob(2476) }} ({{ mob(3150) }} on Hard).

Every 30 seconds the game announces Amdarais's HP. Then for 10 seconds one or two **Varmundt's Ghosts** appear in
the corners of the room. Stand within 2 cells of a ghost to get its buff for 30 seconds. Six adds also join the
fight, and they vanish when the next 30-second cycle starts.

| Amdarais HP | Ghost(s) that appear | Adds |
| --- | --- | --- |
| 90–99% | Attack chance (`2@gl_k 165/247`) | None |
| 80–89% | Protection against the zombie (`150/232`) | 6 Khalitzburg |
| 70–79% | Protection against the zombie | 6 Abysmal Knights |
| 60–69% | Protection against the zombie | 6 Bloody Knights |
| 50–59% | Attack chance | None |
| 40–49% | Protection against the zombie | 6 Wandering Archers |
| 30–39% | Magic shield (`150/247`) and protection against the zombie | 6 Bloody Knights |
| 20–29% | Magic shield and protection against the zombie | 6 Abysmal Knights |
| 0–19% | Magic shield and protection against Amdarais's power (`165/232`) | 6 Wandering Archers |

### Rewards

| From | First time | Every later run |
| --- | --- | --- |
| **Varmundt** after the Corrupted Soul (Normal) | 250,000 Base EXP, 250,000 Job EXP, 1× {{ item(6607) }}, 1× {{ item(6608) }} | 1× {{ item(6607) }}, 1× {{ item(6608) }} |
| **Varmundt** after the Corrupted Soul (Hard) | 250,000 Base EXP, 250,000 Job EXP, 2–5× {{ item(6607) }}, 1× {{ item(6755) }} | 2–5× {{ item(6607) }}, 1× {{ item(6755) }} |
| **Hugin** after Amdarais (Normal) | 350,000 Base EXP, 350,000 Job EXP, 5× {{ item(6607) }}, 5× {{ item(6608) }} | 1× {{ item(6607) }}, 1× {{ item(6608) }} |
| **Hugin** after Amdarais (Hard) | 350,000 Base EXP, 350,000 Job EXP, 5× {{ item(6607) }}, 5× {{ item(6755) }} | 1× {{ item(6607) }}, 1× {{ item(6755) }} |

Normal and Hard each have their own "first time".

When you talk to Hugin again and pick *Please let me out*, you get **20–40 Instance Points** (+50 with
{{ item(30034) }}, within the daily Instance Point limit) and go back to `glast_01`. Leaving this way after a
**Normal** clear is what unlocks Hard mode.

### Treasure room

Hugin's reward also gives you *Space Distortion*. Before you leave, go back down to the castle grounds and use the
**Strange crack** at `1@gl_k 269/267` to enter the treasure room. Seven more cracks inside each drop loot once per
run (on Hard, {{ item(6755) }} replaces {{ item(6608) }}):

| Crack | Loot |
| --- | --- |
| 1 | 1–4× {{ item(719) }}, 1× {{ item(6608) }} |
| 2 | 1–4× {{ item(720) }}, 1× {{ item(7229) }}, 1× {{ item(6608) }}, 25%: {{ item(15066) }} |
| 3 | 1–4× {{ item(721) }}, 1× {{ item(7230) }}, 1× {{ item(6608) }}, 25%: {{ item(13086) }} |
| 4 | 1–4× {{ item(722) }}, 1× {{ item(6612) }}, 1× {{ item(6613) }}, 1× {{ item(6608) }}, 25%: {{ item(2949) }} |
| 5 | 1–4× {{ item(725) }}, 1× {{ item(7228) }}, 1× {{ item(6608) }}, 25%: {{ item(13440) }} |
| 6 | 1–4× {{ item(726) }}, 1× {{ item(6608) }}, 25%: {{ item(2022) }} |
| 7 | 1–4× {{ item(727) }}, 1× {{ item(6608) }}, 25%: {{ item(21007) }} |

{{ instance_page("old-glast-heim") }}
