# Heart Hunter War Base 2

## Guide

After the Heart Hunter base falls in the **Terra Gloria** main quest, Julian turns its outer grounds into a training
course. In this repeatable version you play the attackers: fight through two defended sections and a robot maze, then
spar with Ebel. Each clear gives Instance Points.

### Entering

- **Quest:** clear [Heart Hunter War Base 1](heart-hunter-war-base-1.md) first.
- **Party:** needed. The **party leader** talks to **Julian** at `/navi ein_fild04 281/337` and agrees to examine the
  training ground, which creates the instance.
- **Enter:** everyone talks to the **Striker Unit Commander** at `/navi ein_fild04 275/342`.
- **Cooldown:** entering starts *Base maintenance*, which ends at the next **04:00** server time.
- **Time limit:** 1 hour.

!!! tip
    Julian opens Base 1 or Base 2 depending on the **party leader's** story progress, and the commander sends each
    player to the base matching **their own** progress. Everyone in the party needs to be past Base 1.

### Walkthrough

!!! warning "Robot turrets"
    The robots in the security lines and the maze hit anyone who walks next to them for **40% of their Max HP**.

**Start.** The party leader talks to **Julian** at the entrance. If you answer that it is your first visit he explains
the training at length; otherwise he keeps it short.

**Section 1.** 21 {{ mob(3627) }} defend the yard. Each kill has a **5%** chance to call an {{ mob(3626) }}. A counter
shows how many are left. When they are all dead, walk north to the first security line (around 31, 211): it shuts down
and the passage opens.

**Section 2.** Walk on to Julian (around 31, 233). After his speech, 24 Heart Hunter Guards defend the next yard, this
time with a **10%** chance per kill to call an Upgraded Heart Hunter. Clearing them shuts down the second security line.

**Section 3: the maze.**

1. Talk to Julian (around 56, 283), then push the red button on the **SWT_8309** robot next to him.
2. The robots turn the area into a maze with one of six random layouts, and **40 Heart Hunter Guards** defend it.
3. You only need to bring the defence down to **20 or fewer**: the rest are removed, Julian announces that the
   defence failed, and the door to the boss room opens.

**Boss: Ebel.** Go through the door, then the party leader talks to **Julian** and starts the test. After some
dialogue the room's automatic defence robots switch on and {{ mob(3628) }} attacks. Kill her; the robots shut down
again.

### Rewards

After the closing dialogue (about 40 seconds), a warp opens up the stairs behind Julian. Walking into it gives each
player **20-40 Instance Points** (up to the daily cap of 1,200) and returns you to `ein_fild04`.

{{ instance_page("heart-hunter-war-base-2") }}
