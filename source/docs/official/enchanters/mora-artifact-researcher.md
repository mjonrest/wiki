# Mora Artifact Researcher

<!-- npcs: Guardian of Power; Artifact Researcher -->

The Artifact Researcher adds random enchants to the Mora artifacts for Rune Knights, Guillotine Crosses and Rangers, and to the Empowered Arch Bishop and Warlock weapons. Unlike the other Mora enchanters, he works on the item you are **wearing** and keeps its refine and cards.

## Guardian of Power (getting the gear)

**Where:** `/navi mora 152/97`

Trades 10 {{ item(6380) }} for one artifact of your choice (no random roll, no job check):

| Class | Shoes | Garments |
|---|---|---|
| Rune Knight | {{ item(2475) }}, {{ item(2476) }} | {{ item(2574) }}, {{ item(2575) }} |
| Guillotine Cross | {{ item(2477) }}, {{ item(2478) }} | {{ item(2577) }}, {{ item(2578) }} |
| Ranger | {{ item(2479) }}, {{ item(2480) }} | {{ item(2580) }}, {{ item(2581) }} |

The Empowered weapons come from the [Artifact Collector](mora-arch-bishop-warlock-artifacts.md).

## Artifact Researcher

**Where:** `/navi mora 148/98`

**Cost:** 100,000 zeny and 1 {{ item(6380) }} per enchant attempt or reset. You must have both before he will even look at your item.

### Items it works on

Wear the item, then pick its equipment slot in the menu. Every item has an **enchant type** that decides the enchant table. If the item is refined to **+9 or higher**, you may pick its bonus type instead (you choose on each attempt).

| Slot | Item | Enchant type | Bonus type at +9 |
|---|---|---|---|
| Weapon (right hand) | {{ item(1660) }} | Healer Type | Spell Ability 1 |
| Weapon (right hand) | {{ item(2011) }} | Spell Ability 1 | Spell Ability 2 |
| Weapon (right hand) | {{ item(2012) }} | Spell Ability 1 | Spell Ability 2 |
| Weapon (right hand) | {{ item(2013) }} | Spell Ability 1 | Spell Ability 2 |
| Weapon (right hand) | {{ item(2014) }} | Spell Ability 1 | Spell Ability 2 |
| Weapon (right hand) | {{ item(16018) }} | ATK Type | Spell Ability 1 |
| Shoes | {{ item(2475) }} | Assist Ability 1 | Strength |
| Shoes | {{ item(2476) }} | Assist Ability 1 | Physical Type |
| Shoes | {{ item(2477) }} | Assist Ability 1 | Critical Type |
| Shoes | {{ item(2478) }} | Assist Ability 1 | ATK Type |
| Shoes | {{ item(2479) }} | Assist Ability 1 | Critical Type |
| Shoes | {{ item(2480) }} | Assist Ability 1 | ATK Type |
| Garment | {{ item(2574) }} | Evasion Type | Strength |
| Garment | {{ item(2575) }} | Evasion Type | Critical Type |
| Garment | {{ item(2577) }} | Evasion Type | Critical Type |
| Garment | {{ item(2578) }} | Evasion Type | Critical Type |
| Garment | {{ item(2580) }} | Evasion Type | ATK Type |
| Garment | {{ item(2581) }} | Evasion Type | ATK Type |
| Armor | {{ item(15036) }} | Strength | ATK Type |
| Armor | {{ item(15037) }} | Physical Type | Critical Type |
| Armor | {{ item(15038) }} | Critical Type | Physical Type |
| Armor | {{ item(15039) }} | ATK Type | Critical Type |
| Armor | {{ item(15042) }} | Critical Type | Range Type |
| Armor | {{ item(15043) }} | ATK Type | Range Type |
| Accessory (left accessory slot) | {{ item(2883) }} | Assist Ability 1 | - |
| Accessory (left accessory slot) | {{ item(2884) }} | Assist Ability 1 | - |
| Accessory (left accessory slot) | {{ item(2886) }} | Assist Ability 1 | - |
| Accessory (left accessory slot) | {{ item(2887) }} | Assist Ability 1 | - |
| Accessory (left accessory slot) | {{ item(2890) }} | Assist Ability 1 | - |
| Accessory (left accessory slot) | {{ item(2891) }} | Assist Ability 1 | - |

!!! tip "Accessories"
    The Researcher only checks the **left** accessory slot. If he says you are not wearing the item, swap the ring or brooch to the other accessory slot.

### Enchant order and failure

| Attempt | Slot | What can go wrong |
|---|---|---|
| 1st enchant | 4th slot | Always succeeds. |
| 2nd enchant | 3rd slot | It can **fail**: you lose the 1st enchant too and the item is left with no enchants. |
| 3rd enchant | 2nd slot | It can **fail** (all three enchants removed) or **destroy the item**. Not available on accessories. |

Refine and cards are kept on success and on a normal failure. Once all slots are full the Researcher refuses; reset the item to start over.

If the 2nd enchant fails, only the 2nd slot stays empty; the 1st enchant is kept.

### Reset

Choose "Reset Enhanced abilities." For 100,000 zeny and 1 {{ item(6380) }} all enchants are removed. Refine and cards are kept, and it always works. The fee is taken even if the item has no enchants.

### Enchant tables

Chances below are per attempt. "Fails" means the enchants on the item are removed as described above; "Item destroyed" means you lose the item.

#### ATK Type

| Enchant | 1st (4th slot) | 2nd (3rd slot) | 3rd (2nd slot) |
|---|---|---|---|
| {{ item(4700) }} | 19.05% | - | - |
| {{ item(4811) }} | 19.05% | - | - |
| {{ item(4819) }} | 19.05% | - | - |
| {{ item(4701) }} | 9.52% | 14.08% | - |
| {{ item(4810) }} | 9.52% | 14.08% | - |
| {{ item(4766) }} | 9.52% | 14.08% | - |
| {{ item(4702) }} | 4.76% | 7.04% | 8.33% |
| {{ item(4809) }} | 4.76% | 7.04% | 8.33% |
| {{ item(4767) }} | 4.76% | 7.04% | 8.33% |
| {{ item(4703) }} | - | 4.23% | 5% |
| {{ item(4808) }} | - | 4.23% | 5% |
| {{ item(4704) }} | - | - | 1.67% |
| {{ item(4820) }} | - | - | 1.67% |
| {{ item(4705) }} | - | - | 0.67% |
| {{ item(4821) }} | - | - | 0.67% |
| **Fails** | - | 28.17% | 33.33% |
| **Item destroyed** | - | - | 27% |

#### Critical Type

| Enchant | 1st (4th slot) | 2nd (3rd slot) | 3rd (2nd slot) |
|---|---|---|---|
| {{ item(4750) }} | 21.28% | - | - |
| {{ item(4700) }} | 21.28% | - | - |
| {{ item(4751) }} | 12.77% | 14.63% | - |
| {{ item(4701) }} | 12.77% | 14.63% | - |
| {{ item(4752) }} | 12.77% | 14.63% | 8.11% |
| {{ item(4702) }} | 6.38% | 7.32% | - |
| {{ item(4764) }} | 6.38% | 7.32% | 8.11% |
| {{ item(4818) }} | 6.38% | 7.32% | 8.11% |
| {{ item(4753) }} | - | 3.66% | 4.05% |
| {{ item(4754) }} | - | 3.66% | 4.05% |
| {{ item(4765) }} | - | 1.22% | 1.35% |
| {{ item(4817) }} | - | 1.22% | 1.35% |
| {{ item(4703) }} | - | - | 1.35% |
| {{ item(4816) }} | - | - | 0.54% |
| **Fails** | - | 24.39% | 27.03% |
| **Item destroyed** | - | - | 35.95% |

#### Evasion Type

| Enchant | 1st (4th slot) | 2nd (3rd slot) | 3rd (2nd slot) |
|---|---|---|---|
| {{ item(4859) }} | 19.05% | - | - |
| {{ item(4750) }} | 19.05% | - | - |
| {{ item(4730) }} | 19.05% | - | - |
| {{ item(4860) }} | 9.52% | 13.51% | - |
| {{ item(4751) }} | 9.52% | 13.51% | - |
| {{ item(4731) }} | 14.29% | 20.27% | 7.14% |
| {{ item(4752) }} | 4.76% | 6.76% | 7.14% |
| {{ item(4732) }} | 4.76% | 6.76% | 7.14% |
| {{ item(4762) }} | - | 4.05% | 4.29% |
| {{ item(4753) }} | - | 4.05% | 4.29% |
| {{ item(4733) }} | - | 4.05% | 4.29% |
| {{ item(4763) }} | - | - | 1.43% |
| {{ item(4754) }} | - | - | 1.43% |
| {{ item(4734) }} | - | - | 0.57% |
| **Fails** | - | 27.03% | 28.57% |
| **Item destroyed** | - | - | 33.71% |

#### Healer Type

| Enchant | 1st (4th slot) | 2nd (3rd slot) | 3rd (2nd slot) |
|---|---|---|---|
| {{ item(4710) }} | 26.67% | - | - |
| {{ item(4720) }} | 26.67% | - | - |
| {{ item(4711) }} | 13.33% | 14.93% | - |
| {{ item(4721) }} | 13.33% | 14.93% | - |
| {{ item(4805) }} | 6.67% | 7.46% | 7.14% |
| {{ item(4712) }} | 6.67% | 7.46% | 7.14% |
| {{ item(4722) }} | 6.67% | 7.46% | 7.14% |
| {{ item(4760) }} | - | 4.48% | 4.29% |
| {{ item(4850) }} | - | 4.48% | 4.29% |
| {{ item(4713) }} | - | 4.48% | 4.29% |
| {{ item(4723) }} | - | 4.48% | 4.29% |
| {{ item(4761) }} | - | - | 1.43% |
| {{ item(4851) }} | - | - | 1.43% |
| {{ item(4806) }} | - | - | 0.57% |
| {{ item(4852) }} | - | - | 0.57% |
| **Fails** | - | 29.85% | 28.57% |
| **Item destroyed** | - | - | 28.86% |

#### Spell Ability 1

| Enchant | 1st (4th slot) | 2nd (3rd slot) | 3rd (2nd slot) |
|---|---|---|---|
| {{ item(4710) }} | 16.67% | - | - |
| {{ item(4720) }} | 16.67% | - | - |
| {{ item(4795) }} | 16.67% | - | - |
| {{ item(4815) }} | 16.67% | - | - |
| {{ item(4711) }} | 8.33% | 13.89% | 13.66% |
| {{ item(4721) }} | 8.33% | 13.89% | 13.66% |
| {{ item(4796) }} | 8.33% | 13.89% | 13.66% |
| {{ item(4814) }} | 8.33% | 13.89% | 13.66% |
| {{ item(4712) }} | - | 4.17% | 4.1% |
| {{ item(4722) }} | - | 4.17% | 4.1% |
| {{ item(4797) }} | - | 4.17% | 4.1% |
| {{ item(4813) }} | - | 4.17% | 4.1% |
| {{ item(4713) }} | - | - | 0.55% |
| {{ item(4723) }} | - | - | 0.55% |
| {{ item(4812) }} | - | - | 0.55% |
| **Fails** | - | 27.78% | 27.32% |
| **Item destroyed** | - | - | - |

#### Assist Ability 1

| Enchant | 1st (4th slot) | 2nd (3rd slot) | 3rd (2nd slot) |
|---|---|---|---|
| {{ item(4792) }} | 15.38% | - | - |
| {{ item(4787) }} | 15.38% | - | - |
| {{ item(4801) }} | 15.38% | - | - |
| {{ item(4796) }} | 15.38% | - | - |
| {{ item(4700) }} | 9.62% | 12.5% | - |
| {{ item(4720) }} | 9.62% | 12.5% | - |
| {{ item(4730) }} | 9.62% | 12.5% | - |
| {{ item(4740) }} | 9.62% | 12.5% | - |
| {{ item(4793) }} | - | 6.25% | 7.58% |
| {{ item(4788) }} | - | 6.25% | 7.58% |
| {{ item(4802) }} | - | 6.25% | 7.58% |
| {{ item(4797) }} | - | 6.25% | 7.58% |
| {{ item(4701) }} | - | - | 3.03% |
| {{ item(4721) }} | - | - | 3.03% |
| {{ item(4731) }} | - | - | 3.03% |
| **Fails** | - | 25% | 30.3% |
| **Item destroyed** | - | - | 30.3% |

Accessories with this type only get the 1st and 2nd enchant.

#### Strength

| Enchant | 1st (4th slot) | 2nd (3rd slot) | 3rd (2nd slot) |
|---|---|---|---|
| {{ item(4740) }} | 19.05% | - | - |
| {{ item(4797) }} | 19.05% | - | - |
| {{ item(4791) }} | 19.05% | - | - |
| {{ item(4741) }} | 9.52% | 12.99% | - |
| {{ item(4798) }} | 9.52% | 12.99% | - |
| {{ item(4792) }} | 9.52% | 12.99% | - |
| {{ item(4742) }} | 4.76% | 10.39% | 11.43% |
| {{ item(4793) }} | 4.76% | 6.49% | 7.14% |
| {{ item(4799) }} | 4.76% | 6.49% | 7.14% |
| {{ item(4743) }} | - | 3.9% | 4.29% |
| {{ item(4794) }} | - | 3.9% | 4.29% |
| {{ item(4744) }} | - | 3.9% | 4.86% |
| **Fails** | - | 25.97% | 28.57% |
| **Item destroyed** | - | - | 32.29% |

#### Range Type

| Enchant | 1st (4th slot) | 2nd (3rd slot) | 3rd (2nd slot) |
|---|---|---|---|
| {{ item(4750) }} | 21.28% | - | - |
| {{ item(4720) }} | 21.28% | - | - |
| {{ item(4751) }} | 12.77% | 14.63% | - |
| {{ item(4721) }} | 12.77% | 14.63% | - |
| {{ item(4752) }} | 6.38% | 7.32% | 6.98% |
| {{ item(4722) }} | 6.38% | 7.32% | 6.98% |
| {{ item(4764) }} | 6.38% | 7.32% | 6.98% |
| {{ item(4832) }} | 6.38% | 7.32% | 6.98% |
| {{ item(4753) }} | 6.38% | 7.32% | 6.98% |
| {{ item(4723) }} | - | 3.66% | 3.49% |
| {{ item(4833) }} | - | 3.66% | 3.49% |
| {{ item(4765) }} | - | 1.22% | 1.16% |
| {{ item(4834) }} | - | 1.22% | 1.16% |
| {{ item(4724) }} | - | - | 1.16% |
| {{ item(4835) }} | - | - | 0.47% |
| **Fails** | - | 24.39% | 23.26% |
| **Item destroyed** | - | - | 30.93% |

#### Physical Type

| Enchant | 1st (4th slot) | 2nd (3rd slot) | 3rd (2nd slot) |
|---|---|---|---|
| {{ item(4791) }} | 16.67% | - | - |
| {{ item(4730) }} | 16.67% | - | - |
| {{ item(4750) }} | 16.67% | - | - |
| {{ item(4795) }} | 16.67% | - | - |
| {{ item(4792) }} | 8.33% | 12.5% | - |
| {{ item(4731) }} | 8.33% | 12.5% | - |
| {{ item(4751) }} | 8.33% | 12.5% | - |
| {{ item(4796) }} | 8.33% | 12.5% | - |
| {{ item(4793) }} | - | 6.25% | 7.58% |
| {{ item(4732) }} | - | 6.25% | 7.58% |
| {{ item(4752) }} | - | 6.25% | 7.58% |
| {{ item(4797) }} | - | 6.25% | 7.58% |
| {{ item(4733) }} | - | - | 4.55% |
| {{ item(4753) }} | - | - | 4.55% |
| {{ item(4807) }} | - | - | 0.61% |
| **Fails** | - | 25% | 30.3% |
| **Item destroyed** | - | - | 29.7% |

#### Spell Ability 2

| Enchant | 1st (4th slot) | 2nd (3rd slot) | 3rd (2nd slot) |
|---|---|---|---|
| {{ item(4711) }} | 16.67% | - | - |
| {{ item(4721) }} | 16.67% | - | - |
| {{ item(4796) }} | 16.67% | - | - |
| {{ item(4814) }} | 16.67% | - | - |
| {{ item(4712) }} | 8.33% | 13.89% | 13.66% |
| {{ item(4722) }} | 8.33% | 13.89% | 13.66% |
| {{ item(4760) }} | 8.33% | 13.89% | 13.66% |
| {{ item(4813) }} | 8.33% | 13.89% | 13.66% |
| {{ item(4713) }} | - | 4.17% | 4.1% |
| {{ item(4723) }} | - | 4.17% | 4.1% |
| {{ item(4761) }} | - | 4.17% | 4.1% |
| {{ item(4812) }} | - | 4.17% | 4.1% |
| {{ item(4714) }} | - | - | 0.55% |
| {{ item(4724) }} | - | - | 0.55% |
| {{ item(4806) }} | - | - | 0.55% |
| **Fails** | - | 27.78% | 27.32% |
| **Item destroyed** | - | - | - |

!!! tip "Spell Ability types never break the item"
    The 3rd-enchant warning says the artifact may be destroyed, but for **Spell Ability 1** and **Spell Ability 2** (the Empowered staves, and the Empowered wand and mace at +9) the 3rd enchant can only fail, never destroy the item.
