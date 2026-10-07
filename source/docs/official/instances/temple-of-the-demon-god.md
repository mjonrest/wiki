# Temple of the Demon God

## Guide

The Temple of the Demon God is the Episode 14.3 finale: your party storms Morroc's temple, defeats his two apostles, kills the ice and fire guardians Brinaranea and Muspellskoll, then faces Morroc in three forms. It is long and mechanic-heavy; most of the bosses punish burst damage with heals.

### Requirements and entry

| | |
|---|---|
| **Quest NPC** | Commander Hibba Agip: `/navi moro_vol 108/88` |
| **Instance NPCs** | Guardian Nidhogg (create) `/navi moro_cav 41/73`, Yggdrasil Lookalike (enter) `/navi moro_cav 45/75` |
| **Level** | Base level 160 or higher |
| **Prerequisite** | Finish the Morse's Cave part of Episode 14.3 |
| **Party** | Required. The party leader creates the instance and must carry the *Demon God Subjugation* quest |
| **Time limit** | 60 minutes (closes after 5 minutes with nobody inside) |
| **Cooldown** | Once per day (*Caged God*), starting when you enter the temple. Resets at 04:00 server time. While it runs you can only re-enter the same temple, not a new one. |

1. Talk to Commander Hibba Agip to accept **Demon God Subjugation** (kill Despair God Morroc).
2. The party leader talks to Guardian Nidhogg and picks **Enter now.** to create the temple.
3. Everyone clicks the Yggdrasil Lookalike next to her and picks **Enter.**

### Walkthrough

Almost every step is started by the **party leader**, and the leader needs the *Demon God Subjugation* quest still unfinished for the NPCs to react.

The temple is also patrolled by {{ mob(3101) }} and its red and yellow counterparts. They respawn 5 seconds after dying anywhere on the map and are not needed for anything.

#### 1. The Apostles

1. The leader talks to **Demon God's Apostle Ahat** (`1@eom 101/43`). This gives the leader the *Qualifications of the Guests* quest and warps the party back to the entrance.
2. {{ mob(3105) }} and {{ mob(3106) }} (5,000,000 HP each) appear, each with four {{ mob(1918) }} / {{ mob(1921) }}.
3. Kill all ten. Ahat and Shnaim always drop {{ item(6713) }} and {{ item(6714) }} for players with *Qualifications of the Guests*.
4. Once all ten are dead the two **Empty Soul Globes** (`98/56` and `104/56`) activate. The leader must click each one while holding the matching soul. When both globes are filled, the gate to the central hall opens at `101/58`.

#### 2. Central hall

The leader talks to the **Strange Boy** (`100/122`). After the dialogue with Loki and Nidhogg, the gate to the ice area opens at `91/120`.

A **Nidhogg** NPC (`94/120`) stays in the hall. The party leader can talk to her to summon {{ mob(3087) }} as a mercenary for 30 minutes. This puts the *Guardian's Blessing* quest on you, and you cannot summon her again for 3 hours. You cannot use her if you already have a mercenary out.

#### 3. Ice area: Brinaranea

Entering the ice gate gives you *Temple of the Demon God Phase 1* (kill Brinaranea).

- Pick up the eight **Cold Mana Crystalline** spread around the ice area. Each gives one {{ item(22566) }}. You need them in the fire area, so collect them all.
- Groups of {{ mob(3088) }} spawn as you walk through.
- Walking near Brinaranea (`38/129`) starts the fight with {{ mob(3091) }}.

Boss mechanics (checked every 3 seconds):

| Trigger | What happens |
|---|---|
| She loses more than 2,000,000 HP between two checks | She casts a full heal on herself ("She's regenerated herself perfectly") |
| HP reaches about 70M, 60M or 50M | She calls 5 {{ mob(3088) }} around herself and casts Wide Freeze |
| HP below 22,200,000 | Rows of Ice Mines march across the room around her |
| Every ~10 seconds | One random combo: Wide Freeze + Thunderstorm corners, Wide Freeze + Jupiter Thunder on her target, Wide Freeze + Lord of Vermilion + expanding Thunderstorms, or three self Heals |

When she dies a warp back to the central hall appears at `67/149`. Talk to the **Nidhogg** at `59/147` or step on that warp to hand in Phase 1 for **1,000,000 Base / 500,000 Job EXP**.

#### 4. Fire area: Muspellskoll

Back in the hall, the leader talks to **Morroc** (`100/122`) to open the fire gate at `104/120`. Entering it gives *Temple of the Demon God Phase 2*. Stepping inside spawns nine {{ mob(3089) }} and {{ mob(3092) }}.

- Two **Flowing Lava** pools sit at `154/119` and `182/129`. Standing in the lava zones near them drains 3% HP. Click a pool with a {{ item(22566) }} to harden it for 2 minutes; this removes its damage zones and stops Muspellskoll from healing at it.
- At the start of the fight, and again when its HP passes 45M, 40M, 36M and 30M, Muspellskoll runs to the lava pools and heals itself 9 times at each pool that is not frozen, casts Reflect Shield and calls more Frenzied Kasa.
- If it loses more than 1,000,000 HP within one 3-second check it casts Meteor Storm and heals itself 36 times.
- Every ~10 seconds it uses one combo: Fire Storm + Sightrasher, Fire Storm + four Fire Pillars, Fire Storm + Flame Cross + four Meteor Storms, or it summons two {{ mob(3090) }}.

When it dies a warp back appears at `147/156`. Talk to the **Nidhogg** at `151/155` or use that warp to hand in Phase 2 for **1,000,000 Base / 500,000 Job EXP**.

!!! tip
    Freeze both lava pools right before each heal threshold. Each freeze lasts 2 minutes and costs one Frost Crystal, so you only have eight for the whole fight.

#### 5. Final room: Morroc

In the hall, the **party leader** walks up to the **Strange Young Man** (`98/123`). After a short scene the gate to the final room opens at `98/127`. Walking up to Morroc there (`101/194`) starts the last fight.

**Phase 1, Demigod.** {{ mob(3096) }} appears with a Meteor Storm. Every 6 seconds the script compares its HP: if it lost more than 1,000,000 HP since the last check, it regenerates three times the amount above 200,000 (up to 80,000,000 HP) and casts Heal. Every ~10 seconds it uses a combo of Wide Web, Fire Storm, Lord of Vermilion, Thunderstorm rings or Meteor Storms, sometimes ending in Reflect Shield.

**Phase 2, the two Morrocs.** When Demigod drops below 40,000,000 HP it moves to `101/207` and {{ mob(3098) }} appears at `114/198`, constantly healing Demigod. When Morroc of the Genesis falls below 2,200,000 HP, {{ mob(3099) }} appears at `86/199`.

- If one of them dies while the other lives, the survivor's HP is set to 3,000,000 (Genesis) or 1,000,000 (Sabbath).
- Once both are dead, Demigod returns to the centre for phase 3.

!!! warning
    Do not hit Demigod during phase 2. When phase 3 starts, its HP is raised by ten times the damage it took during phase 2 (up to 80,000,000).

**Phase 3, Demigod again.** Same skills and regeneration rule as phase 1. Below 30,000,000 HP it keeps calling groups of four {{ mob(3089) }} around itself.

**Despair God.** When Demigod dies, {{ mob(3097) }} spawns at `101/194` about 12 seconds later and attacks with Wide Web, Fire Storm, Wide Freeze and Flame Cross combos. Killing it completes *Demon God Subjugation*.

### Rewards

| From | Reward | Who |
|---|---|---|
| Ice and fire Nidhogg | 1,000,000 Base / 500,000 Job EXP for each phase quest | Each player holding the phase quest |
| Nidhogg in the final room (`103/194`) | 20-40 Instance Points, then warp to `moro_vol 91/87` | Each player who talks to her |
| Commander Hibba Agip (first clear) | {{ item(22567) }}, {{ item(6715) }}, 1,000,000 Base / 500,000 Job EXP | Each player who completed the quest |
| Commander Hibba Agip (repeat clears) | {{ item(22567) }}, 1,000,000 Base / 500,000 Job EXP | Each player who completed the quest |

The *Caged God* cooldown already started when you entered; reporting to Hibba Agip does not restart it. When it runs out, talk to him again to clear it, then accept *Demon God Subjugation* again.

{{ instance_page("temple-of-the-demon-god") }}
