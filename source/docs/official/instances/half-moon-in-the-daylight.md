# Half Moon In The Daylight

## Guide

A story instance from the Edda series. You walk into the Pope's dream in Rachel and follow her and her brother
Luwmin through three dream areas, fighting temple guards and devotees along the way. The Pope fights at your side
as a mercenary. It is effectively **solo**: only a party leader can step through the dream portal.

### How to enter

| | |
|---|---|
| **NPC** | High Priestess Niren in Rachel: `/navi rachel 174/138` |
| **Portal** | Dream (next to Niren): `/navi rachel 176/145` |
| **Level** | 80+ |
| **Party** | You must be a party leader (a party of one is enough). Only party leaders can use the Dream portal |
| **Cooldown** | Once per day ("Time to Rest"): after entering you must wait until the next **04:00** server time |
| **Time limit** | 2 hours |

The first time, talk through Niren's introduction. Then talk to her again to create the dream and use the Dream
portal to go in.

### Difficulty

The difficulty is set by the level of the player who starts the dream (first talks to the Pope inside):

| Mode | Leader level | Monsters | Final fight | Hunting quest given on entry |
|---|---|---|---|---|
| Casual | below 130 | Lv 80 ~ 90 versions | {{ mob(3516) }} | Defeat {{ mob(3516) }} |
| Hard | 130+ | Lv 130 ~ 141 versions | {{ mob(3524) }}, then {{ mob(3526) }} | Defeat {{ mob(3526) }} |

The **Pope joins you as a mercenary** for 30 minutes at the start of each big fight. In hard mode she is the
"Casual Pope" mercenary ({{ mob(3569) }}), in casual mode the "Official Pope" ({{ mob(3570) }}). She leaves when the
fight ends.

### Walkthrough

**Dream 1: the temple**

1. Talk to the Pope at the start and follow her through the portal that opens.
2. Walk up to the Pope further along, then talk to her again in the hall (around 100/98). After a long scene she
   joins you and the fight starts in three waves: 11 {{ mob(3510) }}, then 15 Enraged Devotees, then a
   {{ mob(3514) }}. Each wave appears when the previous one is dead.
3. Follow the Pope south, watch the scene with Luwmin, and take the portal at the bottom of the map.

**Dream 2: the escape**

1. Follow the Pope and Luwmin. Stepping on certain spots along the route (the game points you to them) brings out
   the next group of guards: {{ mob(3510) }}, Enraged Devotees and {{ mob(3513) }}. Kill each group to move on.
2. The area ends with another {{ mob(3514) }} near 57/80.
3. Follow the strange copy of the Pope to the portal at 130/22.

**Dream 3: the cold**

1. Talk to the Pope at 45/66. {{ mob(3516) }} appears with six Frozen Hearts ({{ mob(3515) }}). Only Luwmin has
   to die; the Frozen Hearts are removed with him.
2. **Hard mode only:** after Luwmin, {{ mob(3526) }} appears with eleven Frozen Hearts. Again only the boss needs
   to die.
3. Talk to the Pope (57/68) to finish. An exit appears to the east (79/67) that returns you to Rachel.

### The Old Doll and rewards

- Each of the three dreams can drop an {{ item(25087) }} on the floor as a glowing light: after the High Priest in
  dreams 1 and 2 (1 in 3 chance each), and after Luwmin in dream 3 (always, if you have none yet). Step on the light
  to pick it up.
- At the end, talking to the Pope with the doll in your inventory exchanges it for **350,000 base EXP, 350,000 job
  EXP and 2** {{ item(25088) }}.
- Back in Rachel, talk to **Niren** with the hunting quest done for another **126,000 base EXP and 90,000 job
  EXP**.

!!! warning "Match the leader's mode"
    The hunting quest is given according to **your own** level (Luwmin below 130, Ktullanux at 130+), but the
    monsters follow the **leader's** level. A level 130+ player in a casual run never meets Ktullanux, and a
    lower-level player in a hard run fights the hard Luwmin, so neither can complete their quest that run.

!!! tip
    Only the first player who talks to the Pope at the end gets the doll reward, so make sure that player is the
    one carrying the {{ item(25087) }}.

### Fragments of Dreams

The **Temple Item Manager** next to Niren (`/navi rachel 177/139`) uses {{ item(25088) }} to add a Goddess enchant
(Justice, Mercy or Insight) to a worn {{ item(28387) }}: 100 fragments for an A-class enchant, 1,000 for S-class.

{{ instance_page("half-moon-in-the-daylight") }}
