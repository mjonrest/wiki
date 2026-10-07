# Infinite Space

## Guide

A 50-floor climb under the sunken Paros Lighthouse. Each floor is a small room: kill everything in it and a portal
opens to the next. Every tenth floor holds an "Infinite" MVP and a treasure chest full of
{{ item(6905) }}, the currency for the Infinity weapons sold outside. A harder mode adds random mini-bosses and
better chests.

### How to enter

| | |
|---|---|
| **NPC** | Reckless Explorer in the Comodo field: `/navi cmd_fild07 63/275` |
| **Portal** | Temporary Entrance: `/navi cmd_fild07 54/280` |
| **Level** | 100+ |
| **Party** | Required. A party member asks the Reckless Explorer to prepare Infinite Space, then everyone uses the Temporary Entrance |
| **Prerequisite** | Hear the Reckless Explorer's story once ("Fallen Paros Lighthouse") |
| **Cooldown** | 3 hours per character, starting when you enter |
| **Time limit** | 1 hour |

### Choosing the mode

Inside, the **party leader** talks to the Reckless Explorer at the start (42/8):

| | Normal | Hard |
|---|---|---|
| Choice | *"I want to proceed normally"* | *"I want to proceed with something difficult"* |
| Extra mini-boss on a normal floor | - | 10% chance per floor |
| Floor bosses call for help | - | Yes, every 5 seconds while alive |
| Shining Poring chance | 1% | 2% |
| Chest: {{ item(6905) }} | 3 ~ 10 | 6 ~ 22 |
| Chest: Infinity weapons | - | 1% for each of the 10 weapons |

The first floor's monsters appear as soon as the mode is chosen.

### Climbing the floors

1. Kill **every** monster on the floor. Five seconds after the last one dies, a portal opens.
2. Step through the portal: the next floor's monsters spawn when the first player arrives.
3. Floors 1 ~ 49 use upgraded versions of familiar field monsters ({{ mob(3384) }} on floor 1, getting stronger up
   to {{ mob(3420) }} near the top).
4. **Hard mode:** each normal floor has a 10% chance to add one of {{ mob(3421) }}, {{ mob(3422) }},
   {{ mob(3423) }}, {{ mob(3424) }} or {{ mob(3425) }} (never the same one twice in a row). It must die too.

!!! tip "Shining Poring"
    Every wave and every kill has a small chance (1%, or 2% in hard mode) to spawn a {{ mob(3494) }} somewhere on the
    current floor. It vanishes after **20 seconds**, so drop everything and hunt it.

### Boss floors

| Floor | Boss | Escort |
|---|---|---|
| 10 | {{ mob(3426) }} | 5 helpers |
| 20 | {{ mob(3427) }} | 7 helpers |
| 30 | {{ mob(3428) }} | 7 helpers |
| 40 | {{ mob(3429) }} | 6 helpers |
| 50 | {{ mob(3430) }} | 6 helpers |

In hard mode, starting 10 seconds after it appears, each boss calls in another group of 3 ~ 5 monsters every
5 seconds for as long as it lives, so kill it fast.

When a boss floor is cleared, a **treasure chest** appears. Only the **party leader** can open it; the contents drop
on the floor around it (see the mode table above). The hard-mode weapons are the Infinity weapons:
{{ item(1994) }}, {{ item(1938) }}, {{ item(13323) }}, {{ item(13126) }}, {{ item(28703) }}, {{ item(2024) }},
{{ item(16038) }}, {{ item(21014) }}, {{ item(28105) }} and {{ item(18128) }}.

### Finishing

After floor 50, talk to the Reckless Explorer who appears at the end (366/392). She sends you back to `cmd_fild07`
and gives **50 ~ 100 Instance Points** on Normal or **70 ~ 120** on Hard (see [Instance Points](../../content/instances.md)).

!!! warning
    The instance only lasts one hour. A party that cannot clear 50 floors in time gets the floor-10/20/30/40 chests
    but not the Instance Points at the end.

### Spending Broken Magic Stones

Back outside, the **Artifact Appraiser** (`/navi cmd_fild07 57/275`) sells each Infinity weapon or armor for 50
{{ item(6905) }}, and the **Artifact Enhancer** next to her (`/navi cmd_fild07 60/275`) uses them to enchant that
equipment.

{{ instance_page("infinite-space") }}
