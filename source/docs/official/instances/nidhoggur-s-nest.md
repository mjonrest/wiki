# Nidhoggur's Nest

## Guide

Nidhoggur's Nest is the classic two-floor memorial dungeon behind the Yggdrasil Gatekeeper in Nidhoggur's Dungeon. On the first floor you have 30 minutes to kill Nidhoggur's twelve guardians. On the second floor you fight {{ mob(2022) }}, who keeps dragging the whole party into trapped side rooms.

### Requirements and entry

| | |
|---|---|
| Level | Base Level 70 or higher |
| Party | At least 2 members. Only the party leader can create the dungeon. |
| Prerequisite | The **Nidhoggur's Nest** access quest (see below) |
| Entrance | **Yggdrasil Gatekeeper** at `/navi nyd_dun02 100/201` |
| Time limit | 4 hours |
| Cooldown | Until 04:00 server time, 3 days after you enter. A separate 4-hour play-time timer also runs. |

Once you have access, the leader talks to the Gatekeeper and picks **Please allow me to enter.**, then everyone talks to the Gatekeeper and picks **I want to go in.**

!!! note "Cooldown"
    Both timers start on your first entry. While the leader's timers are running, the Gatekeeper will not open a new nest. During the 3-day lockout you can only re-enter the nest you entered; you cannot join a different one.

### Access quest

Before you can enter, you have to research the Gatekeeper. This quest follows on from the Rune-Midgarts Expedition storyline, and the Laphine and Sapha NPCs only understand you while you wear the {{ item(2782) }}.

1. Walk up to the **Yggdrasil Gatekeeper** at `/navi nyd_dun02 100/201` and look at it closely. It pushes you back.
2. Report the strange gate to **Hibba Agip** at `/navi mid_campin 90/121`. He sends you to **Historian Magnifier** at `/navi mid_camp 271/299`.
3. Magnifier sends you to his assistant **Naomi** at `/navi prt_in 171/94`. Help her, then go back to Magnifier and say you have read all the stories.
4. With the ring equipped, ask about the cave to the north. Either ask a soldier in Splendide (`/navi splendide 198/178` or `/navi splendide 240/164`) and then **Commander Lebiordirr** at `/navi spl_in01 109/60`, or ask the **Laphine Prisoner** at `/navi man_in01 291/62` and then **Neat Etorr** at `/navi man_in01 311/57`.
5. Report to Magnifier again, then to Hibba Agip. He asks you to pick a tribe to ask for help: **Laphine** or **Sapha**.
6. Laphine: talk to Commander Lebiordirr, then twice to **Aide Arioss** at `/navi spl_in01 104/56`. Sapha: talk to Neat Etorr, then twice to the Laphine Prisoner.
7. Go back to the Gatekeeper and use the **Guardian's spell**. From now on it lets you in.

### Walkthrough

**1st floor: the guardians (30 minutes)**

The floor is full of {{ mob(2019) }}, {{ mob(2020) }}, {{ mob(2021) }}, {{ mob(2016) }} and {{ mob(2015) }}. A replacement spawns each time one dies.

1. The party leader talks to the **Murdered Yggdrasilid** at `213/277` and agrees to help (**Leave it to us.**). This starts a **30-minute timer**.
2. Twelve **Nidhoggur's Guardians** spawn around `200-255/200-280`: six {{ mob(2020) }} and six {{ mob(2021) }}. Kill all twelve.
3. When the last guardian dies, a warp to the second floor opens at `195/320`.

!!! warning "Time limit"
    The World Tree warns you at 15, 20 and 25 minutes. If the guardians are still alive after 30 minutes, everyone on the floor is sent out to `/navi mid_camp 310/150`.

**2nd floor: Nidhoggur's Shadow**

The second floor has {{ mob(2020) }}, {{ mob(2021) }}, {{ mob(2023) }} and {{ mob(2015) }}, which respawn.

1. Walk north. Stepping on the glowing spot around `199/178` teleports you to `199/255`.
2. When the party leader walks into the area around `199/268`, {{ mob(2022) }} spawns at `199/327`.
3. **Every 3 minutes** the Shadow pulls the whole party into one of four side rooms, chosen at random. Each room has a trap on its landing spot that is active for 10 seconds:

    | Room | Trap effect |
    |---|---|
    | Red | Loses 50% and then another 30% of max HP, plus Bleeding for 60 seconds |
    | White | Loses 50% HP, plus Freeze for 20 seconds |
    | Yellow | Loses 50% SP, plus Sleep for 20 seconds and Confusion for 60 seconds |
    | Green | Loses 50% HP and 50% SP, plus Poison for 60 seconds |

4. Each room holds five Nidhoggur's Guardians (three {{ mob(2020) }}, two {{ mob(2021) }}). While they are alive, the room's exits just loop you back to the landing spot. Kill all five to open the way back to the Shadow. The next pull comes 3 minutes later.
5. If you do not clear the room within 3 minutes, its guardians vanish and the party is pulled into another random room.
6. Kill Nidhoggur's Shadow. **World Tree Yggdrasil** appears at `202/324`.

!!! tip
    Bring Green Potions, Panacea or status recovery. Every room trap inflicts a status effect, and the pulls keep coming every 3 minutes until the Shadow is dead.

### Rewards

| Reward | Who | Notes |
|---|---|---|
| 10 Instance Points | Each player who talks to World Tree Yggdrasil and picks **Please let me out.** | Counts toward the daily 1,200 point cap. You are then warped to `/navi nyd_dun02 98/196`. |
| 1,500,000 Base / 350,000 Job EXP and 10 {{ item(6081) }} | Each player, after a clear | Report to Commander Lebiordirr, then talk to Aide Arioss. |
| 1,500,000 Base / 350,000 Job EXP and 10 {{ item(6080) }} | Each player, after a clear (instead of the row above) | Report to Neat Etorr. |

Leaving through World Tree Yggdrasil unlocks the report again, so you can collect it once after every clear. You can pick either NPC each time, whichever tribe you sided with during the access quest. Wear the {{ item(2782) }} when you report.

!!! tip "Instance Points"
    Instance Points can be earned once per device for each instance run, up to 1,200 per account per day. A rented {{ item(30034) }} adds 50 points per claim. Use `@instancepoints` to see your total.

{{ instance_page("nidhoggur-s-nest") }}
