# Wave Mode

## Guide

Wave Mode is Zonda's tower-defence style instance. Monsters walk along a fixed path toward an exit, and your party has to kill them before they get through. There are two versions, **Forest** and **Sky**, created from the same NPC. There is no final wave: the run lasts until 20 monsters escape or the instance time runs out.

### Requirements and entry

| | |
|---|---|
| **NPC** | Zonda Rep (Belka): `/navi prontera 146/75`, `/navi payon 166/98`, `/navi moc_para01 45/89`, `/navi morocc 168/271` |
| **Level** | No requirement |
| **Party** | Required. Only the party leader can request an instance |
| **Time limit** | 60 minutes (closes after 5 minutes with nobody inside) |
| **Cooldown** | None; you can request a new instance as soon as the old one is gone |

1. The party leader talks to the Zonda Rep, picks **Request entry.**, chooses Forest or Sky and signs.
2. Everyone picks **Enter Wave Mode - Forest** or **Enter Wave Mode - Sky**.

The Zonda Rep remembers where you entered from. When the run is over, the exit warp sends you back to that spot.

### Common rules

- A new wave starts every **24 seconds**, whether or not the previous one is dead.
- Monsters walk the path and do not stop to fight unless the wave is aggressive (see Sky below).
- Every monster that reaches the end of the path counts as **escaped**. At **20 escapes** the challenge fails, waves stop, an exit warp opens, and the instance is destroyed **30 seconds** later.

!!! tip
    Escapes never reset, so a leak in an early wave still counts at wave 40. Area skills along the path are the main tool; monsters ignore players and keep walking.

### Wave Mode - Forest

Map `1@def01`. The run starts as soon as the first player arrives at the entrance: there are about 20 seconds of announcements, then a 3-2-1 countdown. Monsters enter at the top of the bridge and walk straight down to its other end.

- **Normal waves** spawn 24 monsters, one every 0.3 seconds.
- **Every 5th wave** is a champion wave with 5 champion monsters side by side.
- The monster list repeats every 70 waves (wave 71 is Porings again).

| Waves | Normal waves (24 each) | Champion wave (5) |
|---|---|---|
| 1-5 | {{ mob(2401) }} / {{ mob(2582) }} / {{ mob(2573) }} / {{ mob(2590) }} | **{{ mob(2699) }}** |
| 6-10 | {{ mob(2577) }} / {{ mob(1747) }} / {{ mob(2595) }} / {{ mob(2576) }} | **{{ mob(2678) }}** |
| 11-15 | {{ mob(2572) }} / {{ mob(1603) }} / {{ mob(2589) }} / {{ mob(2578) }} | **{{ mob(2670) }}** |
| 16-20 | {{ mob(2601) }} / {{ mob(2575) }} / {{ mob(2583) }} / {{ mob(2600) }} | **{{ mob(2705) }}** |
| 21-25 | {{ mob(1430) }} / {{ mob(2597) }} / {{ mob(1431) }} / {{ mob(2591) }} | **{{ mob(2857) }}** |
| 26-30 | {{ mob(1457) }} / {{ mob(1424) }} / {{ mob(1429) }} / {{ mob(1441) }} | **{{ mob(2648) }}** |
| 31-35 | {{ mob(1422) }} / {{ mob(2585) }} / {{ mob(2592) }} / {{ mob(2571) }} | **{{ mob(2673) }}** |
| 36-40 | {{ mob(2574) }} / {{ mob(1459) }} / {{ mob(1565) }} / {{ mob(2602) }} | **{{ mob(2644) }}** |
| 41-45 | {{ mob(2588) }} / {{ mob(1624) }} / {{ mob(2570) }} / {{ mob(1573) }} | **{{ mob(2811) }}** |
| 46-50 | {{ mob(2598) }} / {{ mob(1606) }} / {{ mob(1794) }} / {{ mob(2596) }} | **{{ mob(2838) }}** |
| 51-55 | {{ mob(2569) }} / {{ mob(2584) }} / {{ mob(2599) }} / {{ mob(1531) }} | **{{ mob(2612) }}** |
| 56-60 | {{ mob(2587) }} / {{ mob(1564) }} / {{ mob(2586) }} / {{ mob(1483) }} | **{{ mob(2888) }}** |
| 61-65 | {{ mob(2593) }} / {{ mob(2580) }} / {{ mob(1600) }} / {{ mob(1791) }} | **{{ mob(2629) }}** |
| 66-70 | {{ mob(2581) }} / {{ mob(2579) }} / {{ mob(1549) }} / {{ mob(2594) }} | **{{ mob(2730) }}** |

### Wave Mode - Sky

Map `1@def02`. Step on the warp at the entrance to start; after a short delay the 3-2-1 countdown begins. Monsters run a winding path around the map and finish back next to the entrance.

- **Normal waves** spawn 15 monsters at half-second intervals. Every other monster is **aggressive** and will attack players; the others only walk.
- Each normal wave also sends out 2 friendly {{ mob(3086) }} that walk the path in the opposite direction and fight the invaders. They disappear after 45 seconds.
- **Every 5th wave** is a treasure wave: no monsters, just {{ mob(3075) }} boxes scattered over the map. The first treasure wave has 1 box, each one after adds another up to a maximum of 5. The boxes roll a dice countdown and self-destruct about 19 seconds after appearing, so break them fast.

| Wave (repeats every 10) | Monster |
|---|---|
| 1 | {{ mob(3076) }} |
| 2 | {{ mob(3077) }} |
| 3 | {{ mob(3078) }} |
| 4 | {{ mob(3079) }} |
| 5 | Treasure boxes |
| 6 | {{ mob(3081) }} |
| 7 | {{ mob(3082) }} |
| 8 | {{ mob(3083) }} |
| 9 | {{ mob(3084) }} |
| 10 | Treasure boxes |

### Rewards

The script gives no completion reward. What you get is what the monsters and treasure boxes drop, so the further you survive, the more you collect (see the monster list below).

{{ instance_page("wave-mode") }}
