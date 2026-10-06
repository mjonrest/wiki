# Sticky Sea

## Guide

Sticky Sea is the Episode 20 snail pit reached through Cocopo. You first visit it during the *Copo's Secret Base* side story; afterwards it becomes the repeatable daily quest **Escargo!**, where you clear waves of {{ mob(22000) }} and kill the {{ mob(21982) }} at the bottom.

### Requirements and entry

| | |
|---|---|
| **Daily quest NPC** | Laraha, Ice Castle: `/navi icecastle 67/218` |
| **Instance NPC** | Cocopo: `/navi jor_back4 101/265` |
| **Prerequisite** | Finish the *Copo's Secret Base* side story and report back to Laraha |
| **Party** | Required. Only the party leader can create the instance |
| **Time limit** | 30 minutes (closes after 5 minutes with nobody inside) |
| **Cooldown** | 4 hours (*Escargot! - Wait*), starting when you claim the reward |

1. Talk to Laraha and pick **Escargo!** to receive the quest. She sends you to Cocopo.
2. The party leader talks to Cocopo and picks **Look at the entrance to the pit.** to create the instance.
3. Everyone picks **Enter the pit.** to go in. Cocopo only shows this menu while you have the *Escargo!* quest active.

### Walkthrough

The pit is a single long path. Each step starts when the **party leader** talks to the Cocopo NPC waiting at the end of the previous one; the next Cocopo only appears once every snail of the current wave is dead.

| Step | Talk to | Spawns | Next stop |
|---|---|---|---|
| 1 | Rorohu at the entrance (`1@slug 52/61`) | 8 {{ mob(22000) }} | Cocopo at `83/127` |
| 2 | Cocopo (`83/127`) | 8 {{ mob(22000) }} | Cocopo at `46/186` |
| 3 | Cocopo (`46/186`) | 12 {{ mob(22000) }} | Cocopo at `159/309` |
| 4 | Cocopo (`159/309`) | 6 {{ mob(22000) }}, and opens the shortcut warp at `148/309` | Cocopo at `66/336` |
| 5 | Cocopo (`66/336`) | Boss: {{ mob(21982) }} | Cocopo at `66/336` again |

!!! warning
    Every member should talk to Rorohu at the entrance, not just the leader. Talking to him updates your *Escargo!* quest to the boss-kill stage. Until the leader has started step 1 and your quest is at that stage, the invisible tiles past the entrance send you back to the start.

The map is also full of roaming {{ mob(21995) }}. They are not part of the run: every one you kill is immediately replaced by a new one, so ignore them unless you are working on Laraha's separate *Dangerous!* daily.

### Rewards

After {{ mob(21982) }} dies, each member talks to the Cocopo at `66/336` to claim the reward and get sent back to `jor_back4`. You can also skip that and hand the quest in to Laraha later; she gives the same items and EXP, but no Instance Points.

| Reward | Amount |
|---|---|
| {{ item(1001217) }} | 3 (4 if your White Cat Alliance reputation is at 3000) |
| Base EXP | 34,152,989 |
| Job EXP | 4,283,013 |
| White Cat Alliance reputation | +5 |
| Instance Points | 40-60 (only when claimed from Cocopo inside the instance) |

!!! tip
    Cocopo needs room for 3 whiskers in your inventory before giving the reward, and Laraha wants room for 10 before she will talk to you at all.

{{ instance_page("sticky-sea") }}
