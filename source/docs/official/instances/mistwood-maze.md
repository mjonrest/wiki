# Mistwood Maze

## Guide

Mistwood Maze (the Hazy Forest) is the maze of warps between Bifrost and Mora. Most of the paths are blocked at the start. Each one opens when you chop down the garden tree that guards it, and you can only chop a tree after you kill the gardener who owns it. When every path is open, you clear the Gardeners' Tree at the end and walk out onto the second Bifrost field. The maze is also where the **Wandering Guardian** quest takes place, which pays out {{ item(2568) }} and {{ item(2858) }}.

### Requirements and entry

| | |
|---|---|
| Party | Required. Only the party leader can register the party. |
| Registration | **Laphine Soldier** at `/navi bif_fild01 158/340` |
| Entrance | **Log Tunnel** at `/navi bif_fild01 161/355` |
| Time limit | 2 hours from creation |
| Cooldown | 2 hours 30 minutes, starting when you enter |

The leader talks to the Laphine Soldier and picks **Venture into the Hazy Forest.** Then everyone uses the Log Tunnel next to him and picks **Enter the tunnel.**

!!! note "Cooldown"
    The 2h30m lockout starts the first time you enter the maze. While the leader's lockout is running, the soldier refuses to register a new maze. Members on cooldown can still join a maze someone else created.

### Walkthrough

**How the maze works**

- The forest is full of {{ mob(2137) }}, {{ mob(2132) }}, {{ mob(2133) }}, {{ mob(2134) }} and {{ mob(2136) }}. A replacement spawns somewhere on the map each time one dies. You will also run into 15 {{ mob(2138) }}, which do not respawn.
- Each garden has a **Garden Tree**. Clicking it and picking **Chop down the garden tree.** opens a warp path that was closed. If the tree's gardener is still alive, the tree will not fall, and a voice complains on the map instead.
- Gardeners are named monsters. They do **not** always stand next to their tree, so you may have to hunt for them first.

**Garden trees**

| Garden tree | Gardener to kill first | Gardener spawns near |
|---|---|---|
| Tom's Garden Tree (`247/123`) | Tom, a {{ mob(2136) }} | `249/120` |
| Tomba's Garden Tree (`225/98`) | Tomba, a {{ mob(2136) }} | `200/64` |
| Remi's Garden Tree (`159/184`) | Remi the Tired, a {{ mob(2137) }} | `154/184` |
| Tired Rem's Garden Tree (`61/39`) | Rem the Gardener, a {{ mob(2136) }} | `101/107` |
| Ron's Garden Tree (`230/179`) | Ron the Gardener, a {{ mob(2134) }} | `227/178` |
| Rover's Garden Tree (`285/225`) | Rover the Strutter, a {{ mob(2134) }} | `304/237` |
| Mona's Garden Tree (`161/316`) | Mona the Seedseeker, a {{ mob(2133) }} | `239/253` |
| Namon's Garden Tree (`204/299`) | Brave Namon, a {{ mob(2134) }} | `89/173` |
| Sad Neoron's Garden Tree (`221/236`) | Sad Neoron, a {{ mob(2137) }} | `143/265` |
| Spyder's Garden Tree (`206/200`) | Spyder the Eight-Legged, a {{ mob(2132) }} | `209/200` |
| Tito's Garden Tree (`95/287`) | Tito the Flipper, a {{ mob(2133) }} | `264/291` |
| Pumba's Garden Tree (`324/325`) | Diligent Pumba, a {{ mob(2134) }} | `309/165` |
| Tete's Garden Tree (`280/344`) | Carefree Tete, a {{ mob(2136) }} | `277/343` |

All coordinates are on the instance map. The Forest Whisper announces each tree as it falls, and after Rem's and Spyder's trees it hints at the next part of the forest.

**The Gardeners' Tree (exit)**

The last tree is at `345/186`. Thirteen "retired" copies of the gardeners (Baby Tom, Tomba the Baby, Exhausted Remi, Rem the Exhausted, Ron the Ex-Gardener, Rover the Strutter, Mona the Seedpicker, Timid Namon, Indifferent Neoron, Spyder the Seven-Legged, Tito the Flapper, Lazy Pumba and Careless Tete) stand around `317-327/129-137`. Kill all 13, then chop down the Gardeners' Tree. This opens the exit warp, which leads to `/navi bif_fild02 151/121`.

The warp at the maze entrance always takes you back to `/navi bif_fild01 160/352`.

### Mysterious Flowers and Seeds

About fifty **Mysterious Flowers** grow in clusters around the maze. Clicking one gives you a {{ item(12561) }} and makes that flower disappear.

Outside the maze there is a giant **Mysterious Flower** at `/navi bif_fild01 38/374`. If you have a Mysterious Seed, you can pick **Observe the reaction.** to spend one seed and be flung straight to `/navi bif_fild02 160/230`, without going through the maze.

### The Wandering Guardian quest

A **Wandering Purple Dragon** (a {{ mob(2131) }}) spawns at one of six random spots in the maze every run. The quest uses it:

1. **Before you go deep**, talk to the **Mysterious Young Man** standing near the entrance (`97/30` in the maze). He only speaks to characters of **Base Level 98 or higher**. Agree that you are crossing the forest. He introduces himself as Loki and asks about a purple-haired girl, which starts **Loki's Search**.
2. Find and kill the Wandering Purple Dragon. A voice asks for help, and a **Collapsed Girl** and **Loki** appear at `183/304`.
3. Talk to Loki there. The quest becomes **Wandering Protector**.
4. Leave the forest and go to Mora. Talk to the **Flower Smelling Lady** at `/navi mora 46/152`, then to the **Sharp Eyed Man** next to her at `/navi mora 48/152`.

| Reward (Sharp Eyed Man) | Amount |
|---|---|
| {{ item(2568) }} | 1 |
| {{ item(2858) }} | 1 |
| Base / Job EXP | 400,000 / 400,000 |

!!! tip
    The Sharp Eyed Man checks your weight before handing out the reward. Free up some space (at least 1,000 weight) before you talk to him.

!!! tip
    The dragon's spawn spot is random each run. If you are only here for the quest, split the party up to search for it while the others work on the gardeners.

{{ instance_page("mistwood-maze") }}
