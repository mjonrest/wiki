# Poring Village

## Guide

A short, beginner-friendly party instance. You follow Emily into the Porings' hideout, push through three areas of
"Enriched" Porings, beat three bosses, and Emily hands out the loot at the end.

### How to enter

| | |
|---|---|
| **NPC** | Emily, Prontera field: `/navi prt_fild05 145/235` |
| **Level** | 30 ~ 70 (Emily turns away anyone outside that range) |
| **Party** | Required. The party leader creates the entrance, then everyone talks to Emily again to enter |
| **Prerequisite** | Talk through Emily's "Contract with Emily" dialogue once (it completes on the spot) |
| **Cooldown** | Once per day per character ("Recovering Fatigue"): after entering you must wait until the next **04:00** server time |
| **Time limit** | 1 hour |

!!! note
    Taming or otherwise "processing" monsters inside does not count as normal progress, and any transformation you
    already have is removed when you go in.

### Walkthrough

1. **Start.** Walk onto the spot next to Emily at the entrance. After a short conversation the first barrier of
   rope posts disappears.
2. **First area.** The map fills with {{ mob(3815) }}, {{ mob(3813) }}, {{ mob(3814) }} and {{ mob(3816) }}.
   Once only 3 of them are left the rest vanish and {{ mob(3811) }} appears at around 132/103.
   Killing it opens the next barrier (after about 6 seconds).
3. **Second area.** A new wave of the same Porings spawns along the eastern and northern paths. When 4 or fewer are
   left, the rest vanish and {{ mob(3812) }} appears near 42/173. Killing it opens the last barrier.
4. **Third area.** A long line of {{ mob(3816) }} blocks the north path. Thin them down to 4 or fewer and
   {{ mob(3810) }} shows up near 182/194 together with 10 fast, aggressive Porings.
5. **Finish.** Kill King Poring and Emily appears near 199/186. Talk to her to claim your reward; she warps you back to
   `prt_fild05`.

### Blue Light Columns

Three columns of blue light stand in the village (around 117/108, 37/165 and 175/199). Stepping on one turns you
into a {{ mob(1629) }} for 60 seconds and gives a short 30-second power-up. Emily points them out before the first
boss, so use them before the boss fights.

### Rewards

Every party member who talks to Emily at the end gets:

| Reward | Notes |
|---|---|
| {{ item(23302) }} | Every clear |
| 20 ~ 40 Instance Points | Random, see [Instance Points](../../content/instances.md) for the daily cap |
| {{ item(19238) }} or {{ item(19239) }} | 50/50, **first clear only** |

### Veggie Enchanter

Next to Emily (`/navi prt_fild05 174/238`) the Veggie Enchanter adds one random bonus to a Poring Village Leek or
Carrot worn in the lower headgear slot. Each attempt costs 50 {{ item(909) }} and 20,000 zeny, and **30% of attempts
destroy the vegetable**. She can also reset an enchanted vegetable for the same price and the same 30% risk.

| Possible enchant | Chance (when it succeeds) |
|---|---|
| VIT +1 | 21.1% |
| LUK +1 | 21.1% |
| SP +10 | 14.9% |
| STR +1, AGI +1, INT +1, DEX +1, SP +25 | 7.5% each |
| Max HP +100 | 3.0% |
| SP +50 | 1.5% |
| Max HP +200 | 0.75% |
| HP Absorb 1 / SP Absorb 1 | 0.15% each |

{{ instance_page("poring-village") }}
