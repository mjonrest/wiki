# Old Helmet Enchants (Nightmare Bio Lab)

<!-- npcs: Wandering Mind; Hot Machine; Sorrowful Soul's Mind; Victimized Soul's Mind -->

The Old helmets from the Nightmare Bio Laboratory (`lhz_dun_n`) are made and enchanted by the
"Mind" NPCs at the dungeon entrance. **Wandering Mind** gives random enchants and can level up the special enchant
with a chance; **Hot Machine** (a server addition) lets you pick the enchant and level it up without failure, for
much more material.

Each Mind NPC stands twice: once inside the dungeon and once on the safe map (no monsters) next to it.

| NPC | Dungeon | Safe map |
|---|---|---|
| Wandering Mind | `/navi lhz_dun_n 134/265` | `/navi lhz_d_n2 42/49` |
| Sorrowful Soul's Mind | `/navi lhz_dun_n 136/269` | `/navi lhz_d_n2 44/53` |
| Victimized Soul's Mind | `/navi lhz_dun_n 143/269` | `/navi lhz_d_n2 51/53` |
| Hot Machine | `/navi lhz_dun_n 128/263` | - |

## Items they work on

All 14 Old helmets, **equipped** in the upper headgear slot. No refine requirement.

{{ item(18971) }}, {{ item(18972) }}, {{ item(18973) }}, {{ item(18974) }}, {{ item(18975) }}, {{ item(18976) }}, {{ item(18977) }}, {{ item(18978) }}, {{ item(18979) }}, {{ item(18980) }}, {{ item(18981) }}, {{ item(18982) }}, {{ item(18983) }}, {{ item(18984) }}

## Wandering Mind: enchant

Pick **"Old Helmet enchant"**. The NPC fills the slots in a fixed order: **4th slot, then 3rd, then 2nd**. After
that, the same menu levels up the special enchant in the 2nd slot.

- **Cost:** 10 {{ item(23016) }} per slot. No zeny.
- Always succeeds. Refine and cards are kept and the helmet is never destroyed.

### 4th and 3rd slot

Every result has the same chance: **3.33%** (1 in 30).

{{ item(4700) }}, {{ item(4701) }}, {{ item(4702) }}, {{ item(4703) }}, {{ item(4704) }}, {{ item(4710) }}, {{ item(4711) }}, {{ item(4712) }}, {{ item(4713) }}, {{ item(4714) }}, {{ item(4720) }}, {{ item(4721) }}, {{ item(4722) }}, {{ item(4723) }}, {{ item(4724) }}, {{ item(4730) }}, {{ item(4731) }}, {{ item(4732) }}, {{ item(4733) }}, {{ item(4734) }}, {{ item(4740) }}, {{ item(4741) }}, {{ item(4742) }}, {{ item(4743) }}, {{ item(4744) }}, {{ item(4750) }}, {{ item(4751) }}, {{ item(4752) }}, {{ item(4753) }}, {{ item(4754) }}

### 2nd slot

Every result has the same chance: **5.56%** (1 in 18).

{{ item(4703) }}, {{ item(4704) }}, {{ item(4713) }}, {{ item(4714) }}, {{ item(4723) }}, {{ item(4724) }}, {{ item(4733) }}, {{ item(4734) }}, {{ item(4743) }}, {{ item(4744) }}, {{ item(4753) }}, {{ item(4754) }}, {{ item(29061) }}, {{ item(29071) }}, {{ item(29081) }}, {{ item(29091) }}, {{ item(29101) }}, {{ item(29111) }}

The last six ({{ item(29061) }}, {{ item(29071) }}, {{ item(29081) }}, {{ item(29091) }}, {{ item(29101) }}, {{ item(29111) }}) are the special enchants that can be levelled up.

### Levelling up the 2nd-slot special enchant

Once all three slots are filled and the 2nd slot holds Mettle, Magic Essence, Acute, Master Archer, Adamantine
or Affection, the enchant menu tries to raise it one level.

| From level | {{ item(23016) }} | Success | On failure |
|---|---|---|---|
| Lv. 1 | 20 | 80% | nothing changes (stays Lv. 1) |
| Lv. 2 | 40 | 70% | drops to Lv. 1 |
| Lv. 3 | 50 | 50% | drops to Lv. 2 |
| Lv. 4 | 70 | 20% | drops to Lv. 3 |
| Lv. 5 | 100 | 20% | drops to Lv. 4 |
| Lv. 6 | 150 | 20% | drops to Lv. 5 |
| Lv. 7 | 250 | 20% | drops to Lv. 6 |
| Lv. 8 | 500 | 20% | drops to Lv. 7 |
| Lv. 9 | 1000 | 20% | drops to Lv. 8 |

- The fragments are used up on success and on failure.
- Refine, cards and the helmet itself are never lost.
- Lv. 10 is the maximum. A stat enchant in the 2nd slot cannot be levelled; reset the helmet instead.

When a Lv. 1 to Lv. 2 attempt fails, your fragments are used and the enchant stays at Lv. 1 (the NPC says the power "didn't explode").

## Wandering Mind: reset

Pick **"Old Helmet reset"**. The helmet must have at least the 4th-slot enchant.

- **Cost:** 10 {{ item(22687) }}.
- Always succeeds. All enchants (2nd, 3rd and 4th slot) are removed. The card in the 1st slot and the refine stay.

## Hot Machine: choose your enchant

Pick **"Enchant Old Headgear"**, choose an **empty** slot, then the exact enchant you want. It always succeeds.
You can fill the slots in any order. Refine and cards are kept.

| Slot | Cost | Choices |
|---|---|---|
| 4th or 3rd slot | 100 {{ item(23016) }} | {{ item(4704) }}, {{ item(4714) }}, {{ item(4724) }}, {{ item(4734) }}, {{ item(4744) }}, {{ item(4754) }} |
| 2nd slot | 1,000 {{ item(23016) }} | {{ item(29061) }}, {{ item(29071) }}, {{ item(29081) }}, {{ item(29091) }}, {{ item(29101) }}, {{ item(29111) }} |

A slot that already has an enchant cannot be changed here; reset it at the Wandering Mind first.

## Hot Machine: guaranteed level up

Pick **"[Guaranteed] Upgrade Special Enchantment"**. It raises the special enchant in the **2nd slot** (the NPC
calls it "slot 1") by one level, always successfully.

| From level | {{ item(23016) }} | Zeny |
|---|---|---|
| Lv. 1 | 100 | 3,500,000 |
| Lv. 2 | 200 | 5,000,000 |
| Lv. 3 | 250 | 8,000,000 |
| Lv. 4 | 350 | 14,000,000 |

Lv. 5 is the highest it goes ("Your enchant cannot be upgraded further"). To go beyond Lv. 5, use the Wandering
Mind's chance-based level up.

## Sorrowful Soul's Mind: making Old helmets

Pick **"Hand over the soul."** and the helmet you want. Each helmet is made from its costume version, a job soul and
{{ item(6820) }}. You choose between a cheap 20% try and a 5x-cost guaranteed try. On failure **all materials are lost**,
including the costume item. Every attempt also takes away half of your HP and SP.

| You get | Costume item | Soul | 20% try | 100% try |
|---|---|---|---|---|
| {{ item(18971) }} | {{ item(19961) }} | {{ item(6814) }} | 1 soul, 20 {{ item(6820) }} | 5 souls, 100 {{ item(6820) }} |
| {{ item(18972) }} | {{ item(19962) }} | {{ item(6819) }} | 1 soul, 20 {{ item(6820) }} | 5 souls, 100 {{ item(6820) }} |
| {{ item(18973) }} | {{ item(19963) }} | {{ item(6815) }} | 1 soul, 20 {{ item(6820) }} | 5 souls, 100 {{ item(6820) }} |
| {{ item(18974) }} | {{ item(19964) }} | {{ item(6815) }} | 1 soul, 20 {{ item(6820) }} | 5 souls, 100 {{ item(6820) }} |
| {{ item(18975) }} | {{ item(19965) }} | {{ item(6816) }} | 1 soul, 20 {{ item(6820) }} | 5 souls, 100 {{ item(6820) }} |
| {{ item(18976) }} | {{ item(19966) }} | {{ item(6818) }} | 1 soul, 20 {{ item(6820) }} | 5 souls, 100 {{ item(6820) }} |
| {{ item(18977) }} | {{ item(19967) }} | {{ item(6815) }} | 1 soul, 20 {{ item(6820) }} | 5 souls, 100 {{ item(6820) }} |
| {{ item(18978) }} | {{ item(19968) }} | {{ item(6817) }} | 1 soul, 20 {{ item(6820) }} | 5 souls, 100 {{ item(6820) }} |
| {{ item(18979) }} | {{ item(19969) }} | {{ item(6819) }} | 1 soul, 20 {{ item(6820) }} | 5 souls, 100 {{ item(6820) }} |
| {{ item(18980) }} | {{ item(19970) }} | {{ item(6817) }} | 1 soul, 20 {{ item(6820) }} | 5 souls, 100 {{ item(6820) }} |
| {{ item(18981) }} | {{ item(19971) }} | {{ item(6818) }} | 1 soul, 20 {{ item(6820) }} | 5 souls, 100 {{ item(6820) }} |
| {{ item(18984) }} | {{ item(19974) }} | {{ item(6818) }} | 1 soul, 20 {{ item(6820) }} | 5 souls, 100 {{ item(6820) }} |
| {{ item(18982) }} | {{ item(19973) }} | {{ item(6816) }} | 1 soul, 20 {{ item(6820) }} | 5 souls, 100 {{ item(6820) }} |
| {{ item(18983) }} | {{ item(19972) }} | {{ item(6814) }} | 1 soul, 20 {{ item(6820) }} | 5 souls, 100 {{ item(6820) }} |
| {{ item(20749) }} | {{ item(20748) }} | {{ item(6471) }} | 20 {{ item(6471) }}, 100 {{ item(6820) }} | 100 {{ item(6471) }}, 500 {{ item(6820) }} |

## Victimized Soul's Mind: Energy Fragments

Pick **"Hand over the weapon."** and a weapon type to destroy one of these Bio Lab weapons for {{ item(6820) }}. Every
exchange also takes away half of your HP and SP.

| Fragments received | Chance |
|---|---|
| 1 | 70% |
| 2 | 20% |
| 3 | 10% |

Accepted: {{ item(1284) }}, {{ item(1290) }}, {{ item(1285) }}, {{ item(1291) }}, {{ item(18109) }}, {{ item(18110) }}, {{ item(1745) }}, {{ item(18103) }}, {{ item(18111) }}, {{ item(1311) }}, {{ item(1392) }}, {{ item(1393) }}, {{ item(16017) }}, {{ item(16010) }}, {{ item(2161) }}, {{ item(1584) }}, {{ item(16000) }}, {{ item(16001) }}, {{ item(2005) }}, {{ item(2004) }}, {{ item(1647) }}, {{ item(1659) }}, {{ item(1646) }}, {{ item(1654) }}, {{ item(13431) }}, {{ item(13421) }}, {{ item(13061) }}, {{ item(13062) }}, {{ item(13070) }}, {{ item(13069) }}, {{ item(13046) }}, {{ item(13047) }}, {{ item(1433) }}, {{ item(1435) }}, {{ item(1490) }}, {{ item(1196) }}, {{ item(1189) }}, {{ item(1930) }}, {{ item(1984) }}, {{ item(1985) }}, {{ item(1830) }}.

!!! tip
    {{ item(6820) }} can be turned into {{ item(22687) }} (50 each) and {{ item(23016) }} (666 each) at the **Bully** in
    Lighthalzen (`/navi lighthalzen 312/296`).
