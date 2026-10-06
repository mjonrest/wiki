# Temporal Boots (Old Glast Heim)

<!-- npcs: Hugin's Butler; Hugin's Magician; Hugin's Craftsman; Dark magic master -->

Four NPCs in Glast Heim turn the Old Glast Heim Temporal Boots into stat boots, add a socket and enchant them.

| NPC | Job | Where |
|---|---|---|
| Hugin's Butler | Sells and upgrades Temporal Boots | `/navi glast_01 210/273` |
| Hugin's Magician | Enchants stat boots (with or without a socket) | `/navi glast_01 212/273` |
| Hugin's Craftsman | Adds a socket | `/navi glast_01 210/270` |
| Dark magic master | Enchants socketed stat boots (riskier) | `/navi glast_01 184/283` |

All four need at least 1,000 free weight. Wear the boots you want to change.

## The boots

| Stat | Temporal (no socket) | Temporal (socket) | Modified (no socket) | Modified (socket) |
|---|---|---|---|---|
| STR | {{ item(22000) }} | {{ item(22006) }} | {{ item(22107) }} | {{ item(22113) }} |
| INT | {{ item(22001) }} | {{ item(22009) }} | {{ item(22108) }} | {{ item(22114) }} |
| AGI | {{ item(22002) }} | {{ item(22010) }} | {{ item(22109) }} | {{ item(22115) }} |
| VIT | {{ item(22003) }} | {{ item(22007) }} | {{ item(22110) }} | {{ item(22116) }} |
| DEX | {{ item(22004) }} | {{ item(22008) }} | {{ item(22111) }} | {{ item(22117) }} |
| LUK | {{ item(22005) }} | {{ item(22011) }} | {{ item(22112) }} | {{ item(22118) }} |

## Hugin's Butler

| Option | Cost | Result |
|---|---|---|
| Buy Temporal Boots | 1 {{ item(6607) }} | {{ item(2499) }} |
| Upgrade Temporal Boots | Wear {{ item(2499) }} + 5 {{ item(6607) }} | Temporal stat boots of your choice (no socket) |
| Upgrade Modified Boots | Wear {{ item(2499) }} + 5 {{ item(6607) }} | Modified stat boots of your choice (no socket) |

The upgrade gives brand-new boots: the old refine is **not** kept.

## Hugin's Craftsman (socket)

Wear Temporal or Modified stat boots **without** a socket and pay 5 {{ item(6607) }}.

- **Success (51%)**: you get the socketed version of the same boots.
- **Failure (49%)**: the boots are **destroyed**.

Either way the new boots start at +0 with no enchants.

## Enchanting

Both enchanters use the same enchant lines. You pick one line for the 4th slot, then raise it from level 1 to
level 4. After the 4th level, one more step adds a random bonus to the 3rd slot. Once the 3rd slot has a
bonus, the boots are finished and cannot be enchanted again. There is **no reset**.

| Menu | Level 1 | Level 2 | Level 3 | Level 4 |
|---|---|---|---|---|
| Fighting Spirit | {{ item(4808) }} | {{ item(4820) }} | {{ item(4821) }} | {{ item(4822) }} |
| Archery | {{ item(4832) }} | {{ item(4833) }} | {{ item(4834) }} | {{ item(4835) }} |
| Spell | {{ item(4814) }} | {{ item(4813) }} | {{ item(4812) }} | {{ item(4826) }} |
| Vitality | {{ item(4741) }} | {{ item(4742) }} | {{ item(4861) }} | {{ item(4862) }} |
| Attack Speed | {{ item(4869) }} | {{ item(4872) }} | {{ item(4873) }} | {{ item(4881) }} |
| Lucky | {{ item(4752) }} | {{ item(4753) }} | {{ item(4754) }} | {{ item(4755) }} |

**3rd slot bonus** (one of six, 16.67% each): {{ item(4875) }}, {{ item(4876) }}, {{ item(4877) }},
{{ item(4878) }}, {{ item(4879) }}, {{ item(4880) }}.

Refine is kept by every enchant step.

### Hugin's Magician

Choose **Enchant Unslotted** or **Enchant Slotted** to match your boots. Every step always succeeds.

| Step | Unslotted boots | Slotted boots |
|---|---|---|
| Level 1 | 1 {{ item(6608) }} | 3 {{ item(6608) }} + 1 {{ item(6755) }} |
| Level 2 | 4 {{ item(6608) }} | 10 {{ item(6608) }} + 2 {{ item(6755) }} |
| Level 3 | 15 {{ item(6608) }} | 20 {{ item(6608) }} + 4 {{ item(6755) }} |
| Level 4 | 30 {{ item(6608) }} | 40 {{ item(6608) }} + 7 {{ item(6755) }} |
| 3rd slot bonus | 10 {{ item(6608) }} | 50 {{ item(6608) }} + 10 {{ item(6755) }} |

### Dark magic master

Only works on **socketed** boots. Same materials as the Magician's slotted column, plus **100,000z** per try.

| Step | Success | On failure |
|---|---|---|
| Level 1 | 100% | - |
| Level 2, 3, 4 and the bonus | 70% | **The boots are destroyed** (refine, card and enchants lost) |

!!! tip
    Hugin's Magician does the same enchants on socketed boots for the same materials, with no zeny and no
    chance to fail. There is no reason to use the Dark magic master.

!!! warning "Known issue: the card in socketed boots is lost"
    When either NPC enchants **socketed** boots, the boots come back with an empty socket. A card you put
    in the socket is **deleted** on every enchant step. Enchant the boots fully first, then insert the card.
