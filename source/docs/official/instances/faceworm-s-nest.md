# Faceworm's Nest

## Guide

Faceworm's Nest is a time attack instance with five stages. Your party follows Chaos and Iris through the forest and kills four Dark Faceworms and then the Faceworm Queen. Each boss leaves a treasure chest with a {{ item(20717) }} cape. The faster you open the chest after the stage starts, the better the refine and enchants on the cape.

### How to enter

- **Where:** the Dimensional Gap, `/navi dali 80/60`.
- **Level:** Base Level 140 or higher.
- **Party:** You need a party, even if you go alone. The party leader talks to the **Magic Scholar** (`dali 80/60`) and picks **"Reserve Faceworm's Nest"**. Then everyone enters through the **Interdimensional Device** next to him (`/navi dali 72/55`).
- **Cooldown:** Entering starts a **4 hour** cooldown ("Faceworm's Nest after-effects"). After it ends, talk to the Magic Scholar or the device once to clear it.
- The **Old Sign** at `/navi dali 83/67` shows the server's best clear time and the size of the party that set it.

### Stage 1: The forest path

The party leader talks to **Chaos**. After a short conversation the time attack starts and {{ mob(2528) }} spawn along the forest path. There are (number of players in the instance + 1) × 11 of them in total, and the announcer counts down how many are left.

When fewer than 3 Faceworms remain, the rest disappear and a {{ mob(2530) }} spawns in the east, near `145/74`.

### Dark Faceworm mechanics

All four Dark Faceworms share the same basics:

- **HP scales with the party:** 5,200,000 minus 200,000 for each player fewer than 13 who is in the instance, with a minimum of 1,500,000. A solo player faces 2,800,000 HP.
- **Stage 1: Eggs.** The boss lays 2 or 4 {{ mob(2540) }} around itself. It lays 4 when it is low on HP. After 12 seconds it absorbs every egg still standing and heals, and more eggs heal it for much more. Break eggs as soon as they appear.
- **Stage 2: Water Balls.** Invisible helpers spawn around the boss and cast Water Ball. They disappear after 20 seconds.
- **Stage 3: Venom Bugs.** The boss fills a square around itself with {{ mob(2531) }}, which self-destruct, and heals a random amount each time.
- **Stage 4: Venom Fog.** Invisible helpers cast Venom Fog around the boss for 30 seconds at a time. The whole stage 4 area also has extra venom fog spots until the boss dies.

When a Dark Faceworm dies, a **treasure chest** appears and a portal opens to the next area.

### Stages 2 to 4

| Stage | Start | Boss spawns near |
|---|---|---|
| 2 | Leader talks to **Chaos** after taking the portal at `149/92` | `161/272` (south of the hill) |
| 3 | Leader talks to **Chaos** after the portal at `139/100` | `278/308` (narrow canyon in the north-east) |
| 4 | Walk into the area just past the portal at `248/185` | `214/108` (west) |

Each stage first spawns a new wave of (players + 1) × 11 Faceworms, and the boss appears when fewer than 3 remain.

### Stage 5: Faceworm Queen

Take the portal at `204/122` and walk to the large puddle. After a cutscene with Chaos, the {{ mob(2529) }} crawls out of the nest at `213/153`.

- **HP:** 52,000,000 minus 2,000,000 for each player fewer than 13 in the instance, with a minimum of 15,000,000. A solo player faces 28,000,000 HP.
- **Element changes:** About every 25 seconds she may shed her skin and change form: {{ mob(2535) }} (wind), {{ mob(2533) }} (earth), {{ mob(2534) }} (water) or back to normal. Watch the announcement and switch to the right element.
- **Adds:** Depending on her remaining HP, she uses the same tricks as the Dark Faceworms: eggs that heal her (up to 1,000,000 per player for 4 eggs), Water Ball helpers, Venom Bug grids that also heal her, and Venom Fog. Below 10,000,000 HP she combines two of these at once.
- **Stay near the nest:** Keep her inside the nest area (roughly `190–230 / 135–175`). If she leaves it you get a warning, and then she turns into the {{ mob(2532) }} for 15 seconds.
- **Burst damage triggers rage:** If the party deals more than (players + 7) × 400,000 damage within one cycle (about 20 seconds), she recovers 80% of that damage and turns into the Red Faceworm Queen with higher attack.
- **Chaos helps:** While she has more than 7,000,000 HP, Chaos sometimes shouts "Lure it to the north/south/east/west!" and appears at that edge of the nest for 15 seconds. Pull the Queen next to him and step on his spot. He hits her for up to (players + 7) × 250,000 damage. His hit cannot take her below 5,000,000 HP.

When she dies, the final chest appears. Talk to Chaos (step near `212/156`) and then use the **Dimensional Device** to leave.

### Rewards

**Stage chests (Dark Faceworms):** Each chest drops one {{ item(20717) }}. It is either the unslotted cape or the slotted version {{ item(20718) }}. The slotted chance grows with each stage: 5%, 10%, 15% and 20%.

- The timer for each chest starts when that stage starts. Open it within **2 minutes** for the best result: refine **+2 to +6**. Each 15 seconds after that lowers the range, down to +0 to +4.
- It can also roll up to three random stat enchants (STR/AGI/VIT/INT/DEX/LUK +1 to +5, plus a rare Special stat enchant). Faster clears raise the chance of getting enchants.

**Final chest (Faceworm Queen):** Drops **two** capes, each with a 60% chance to be slotted.

- Open it within **4 minutes 30 seconds** of the Queen's stage starting for refine **+4 to +11**. Each 15 seconds later lowers the range, down to +1 to +8.
- Enchants can go up to +7 per stat.
- Opening it records your clear time on the Old Sign. If you beat the record, it is announced to the whole server.

**Merchant Prince's Boxes:** When the final chest is opened, each of 27 hidden boxes around the map has a 50% chance to appear. Each box drops:

- 1–7 jewels
- One quest item: {{ item(6650) }}, {{ item(6651) }}, {{ item(6652) }}, {{ item(6653) }} or {{ item(22507) }}
- 60% chance of {{ item(6648) }}
- 30% chance of {{ item(7228) }}
- 10% chance of {{ item(7229) }}

**[Instance Points](../../content/instances.md):** 20–40 when you leave through the Dimensional Device. This counts toward the daily 1,200 point cap.

### Payon side quests

Four NPCs in Payon take the quest items from the boxes. Each turn-in gives **70,000 Base EXP and 55,000 Job EXP**. Each NPC can be done once every **4 hours**, and you need Base Level 140.

| NPC | Location | Takes |
|---|---|---|
| An Old Woman (Jeum-sun) | `/navi payon 157/54` | {{ item(6650) }} |
| Exotic Merchant (Sergio) | `/navi payon 161/54` | {{ item(6652) }} |
| Strong Looking Man (Dol-Seoi) | `/navi payon 161/50` | {{ item(6653) }} |
| A dreary man (Keaton) | `/navi payon 139/68` | {{ item(6651) }} |

!!! tip
    - Stepping near a **Suspicious Mound** spawns 1–3 {{ mob(2541) }}.
    - Hidden toxic spots on the path to stages 2 and 3 release 25–50 Venom Bugs.
    - {{ mob(1277) }}, {{ mob(1494) }} and {{ mob(1166) }} roam the whole map.
    - Clear quickly but carefully. The chest timers keep running while you fight trash.

!!! warning "Known issue"
    The **Dimensional Device** warps you out to `dali` even if you pick **"Stop"**. If you pick "Stop", you also receive 0 Instance Points, and that still counts as your claim for this run. Only talk to it when you are ready to leave, and pick **"Return to Dimensional Gap"**.

{{ instance_page("faceworm-s-nest") }}
