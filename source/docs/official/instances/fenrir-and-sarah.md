# Fenrir and Sarah

## Guide

Professor Bernhard sends you back in time to Glast Heim, to the battle between Fenrith Fenrir and the Valkyrie Sarah Irene. The story follows Fenrir across the old castle grounds. Your real goal is to collect **Fragments of Gigantes** from the Ancient Gigantes on the map. The professor's assistant uses them to give you and enchant **Sarah's Earrings**.

### How to enter

- **NPC:** Professor Bernhard in the Dimensional Gap, `/navi dali02 97/142`. The **Dimensional Device** is right next to him at `/navi dali02 99/148`.
- **Level:** Base Level 145 or higher.
- **Party:** The party leader talks to Bernhard and answers **"Yes"** to create the instance. Then everyone enters through the Dimensional Device.
- **Reporting back:** After every run, talk to Bernhard again. Until you do, the device will not let you back in. Reporting back starts a daily cooldown ("Go back to Professor Bernhard") that resets at **04:00** server time. He says a week in his dialogue, but the cooldown is one day.

### Walkthrough

**1. The entrance.** Walk toward Fenrir near `360/295`. Nine {{ mob(3198) }} ambush you while Fenrir channels a spell for 10 seconds, then her lightning wipes them out. After the conversation, take the warp at `352/279` into Glast Heim.

**2. South courtyard.** Find Fenrir at `216/48`. This starts a **5 minute timer** and marks `47/270` on your minimap. It also wakes up the six **Ancient Gigantes** around the map (see below).

**3. Fenrir's chamber (west).** The **party leader** must reach `47/270` before the 5 minutes run out. The party is then moved into the chamber. Walk in to spawn two {{ mob(3191) }}. Waves of {{ mob(3198) }} and {{ mob(3199) }} keep pouring in while Fenrir uses the Sentinel Breeze. Kill both Gigantes, or hold out for 5 waves until Fenrir finishes them. Everyone in the room is then sent to `105/369`.

**4. North path.** Walk east to Fenrir at `133/365`. This starts another **5 minute timer** and marks `199/237`. The **party leader** steps on the warp at `199/237`. That moves everyone in the instance to the castle stairs. Then the leader takes the warp at `199/294` into the final room.

**5. Final room: Sarah Irene.** Walking in spawns {{ mob(3190) }} together with pairs of {{ mob(3194) }} and {{ mob(3195) }}. More Large Gigantes keep arriving during the fight, up to four at a time.

- Fenrir fights Sarah with a series of big spells. Each spell sets Sarah's HP to a fixed fraction of her maximum, so damage you deal to Sarah in between does not carry over. Spend that time killing the Large Gigantes.
- About **4 minutes 13 seconds** into the fight, Fenrir announces that Sarah is in critical condition and drops her to **100 HP**. Finish her quickly. About 30 seconds later the fight ends either way.

**6. Escape.** After the cutscene, everyone in the final room is moved outside to `197/221`, next to Fenrir. Sarah's wrath begins almost immediately:

- Groups of Large Gigantes spawn all over Glast Heim in five waves.
- Then **14 hidden blast zones** activate across the map. Walking into one **kills you instantly**.
- Run back to the entrance. The **party leader** steps on the warp at `351/269`, which brings everyone back to `349/282`.

Talk to **Fenrith Fenrir** at `359/294` for your reward. Then leave through the warp at `376/303`.

!!! note "Missing a timer"
    If the leader does not reach the chamber (step 3) within 5 minutes, Fenrir handles it alone and the story jumps to step 4. If the castle timer in step 4 also runs out, Fenrir takes the Sentinel Breeze herself and the escape (step 6) starts immediately. Either way you can still finish the run. You just skip those fights.

### Fragments of Gigantes

Six dormant **Ancient Gigantes** become active once you reach Fenrir in the south courtyard (step 2). Walk up to one to wake an {{ mob(3196) }} with two {{ mob(3193) }}. Each Ancient Gigantes drops a {{ item(6803) }}.

| Location | | |
|---|---|---|
| `290/147` (east) | `300/248` (east) | `292/344` (north-east) |
| `107/147` (west) | `98/248` (west) | `107/344` (north-west) |

Stone Gargoyle statues near them turn into {{ mob(3197) }} when you step next to them. {{ mob(3200) }} roam the east side of the map from the start.

!!! tip
    The 5 minute timer from step 2 is short. Decide before you start whether your party hunts the Ancient Gigantes first or follows Fenrir. Skipping the chamber still lets you finish the run.

### Rewards

| Reward | From |
|---|---|
| {{ item(607) }} ×1 and {{ item(608) }} ×1 | Fenrith Fenrir at the end of the escape, once per run |
| 20–40 [Instance Points](../../content/instances.md) | Same, counts toward the daily 1,200 cap |
| {{ item(6803) }} | Ancient Gigantes |
| {{ item(28310) }} **or** {{ item(28311) }} | Professor Bernhard, the first time you report back (one per character) |

The left earring lets you use Heal Lv1 and the right earring lets you use Teleport Lv1.

### Sarah's Earrings: Chief Assistant

The **Chief Assistant** stands at `/navi dali02 93/146`. He only talks to characters who already got their first earring from Bernhard.

- **Buy another earring:** 1 {{ item(6803) }} for either the left or the right earring.
- **Enchant:** 4 Fragments per attempt. The earring must be **equipped**, and it can have 2 enchants. First pick which accessory slot it is worn in, then pick a category:

| Category | Possible results, in order |
|---|---|
| CRI or Critical | Fatal 1, Fatal 2, CRI 2, CRI 3, CRI 4, Fatal 3 |
| Expert Archer or Bleed | Expert Archer 1, Expert Archer 2, Parrying 1, Parrying 2, Parrying 3, Expert Archer 3 |
| Conservation or MATK | Economy 1, Economy 2, MATK +3%, MATK +4%, Economy 3, MATK +5% |
| Delay Attack or Delay Skill | Attack Delay 1, Attack Delay 2, Skill Delay 1, Skill Delay 2, Skill Delay 3, Attack Delay 3 |

- **Earring in the left accessory slot:** only the first 4 results of the category can roll, about 20% each. About 19% of attempts **fail**.
- **Earring in the right accessory slot:** all 6 results can roll, about 10% each, including the best two. About 39% of attempts **fail**.
- **Reset enchants:** 1 Fragment returns a clean earring.

!!! warning
    A failed enchant **destroys the earring**, including any enchant it already had. Keep a spare Fragment to buy a new one.

{{ instance_page("fenrir-and-sarah") }}
