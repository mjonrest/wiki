# Thanatos Tower Enchanters

<!-- npcs: Headgear Enchanter; Briliant Light Enchanter; Sinful Enchanter; Sinfull Accessory; Brilight Accessory; Tha-Tower Exchanger -->

The Thanatos Tower lobby has enchanters for the Good and Evil gear:

| NPC | Works on | Where |
|---|---|---|
| Headgear Enchanter | Crown of Good and Evil | `/navi tha_t01 142/82` |
| Briliant Light Enchanter | Brilliant Light weapons | `/navi tha_t01 154/82` |
| Sinful Enchanter | Sinful weapons | `/navi tha_t01 157/82` |
| Sinfull Accessory | Sinful rings and necklaces | `/navi tha_t01 136/83` |
| Brilight Accessory | Brilliant Light rings and necklaces | `/navi tha_t01 162/83` |
| Tha-Tower Exchanger | Turns fragments into enchant materials | `/navi tha_t01 139/83` |

The Boots Enchanter next to them has its own page: [Boots of Good and Evil](good-and-evil-boots.md).

Every step on the headgear and weapon enchanters always succeeds. Refine, the first two slots and the enchant
grade are kept.

!!! warning "Known issue: carry only one copy"
    All of these NPCs take the item out of your inventory by item ID, not the one you are wearing. If you also
    carry another copy of the **same** item, that copy can be used up instead while your worn item stays as it
    was. Keep only the item you are enchanting on you.

## Materials

| Material | Used by |
|---|---|
| {{ item(1000257) }} | Headgear, Sinful weapons, Sinful accessories |
| {{ item(1000263) }} | Headgear, Brilliant Light weapons, Brilliant Light accessories |
| {{ item(7925) }} | Headgear, weapons |
| {{ item(1000874) }} | Headgear, some Lv5 upgrades |

**Tha-Tower Exchanger** trades 5 fragments of one kind for 1 material (in batches of 1, 50 or 100):

| Menu | Fragments accepted | You get |
|---|---|---|
| Exchange to Fragment of Sin | {{ item(1000243) }}, {{ item(1000244) }}, {{ item(1000245) }}, {{ item(1000255) }}, {{ item(1000256) }} | {{ item(1000257) }} |
| Exchange to Fragment of Fate | {{ item(1000258) }}, {{ item(1000259) }}, {{ item(1000260) }}, {{ item(1000261) }}, {{ item(1000262) }} | {{ item(1000263) }} |

## Headgear Enchanter

Wear one of these as your upper headgear (22 items):

{{ item(400374) }}, {{ item(400375) }}, {{ item(400376) }}, {{ item(400377) }}, {{ item(400378) }},
{{ item(400379) }}, {{ item(400380) }}, {{ item(400381) }}, {{ item(400382) }}, {{ item(400383) }},
{{ item(400384) }}, {{ item(400385) }}, {{ item(400386) }}, {{ item(400387) }}, {{ item(400388) }},
{{ item(400389) }}, {{ item(400390) }}, {{ item(400391) }}, {{ item(400392) }}, {{ item(400393) }},
{{ item(400394) }}, {{ item(400395) }}

### Slot 3 (selectable)

Choose {{ item(312014) }} or {{ item(312021) }}. Slot 3 must be empty.

**Cost:** 250 {{ item(1000257) }}, 3 {{ item(1000263) }}, 1 {{ item(1000874) }}, 3,000,000z.

### Slot 4

If Slot 4 is empty you choose how to fill it:

| Method | Cost | Result |
|---|---|---|
| Random Enchant | 1 {{ item(7925) }}, 25 {{ item(1000257) }}, 25 {{ item(1000263) }}, 300,000z | One of the six Lv1 enchants below, 16.67% each |
| Specific Enchant | 2 {{ item(7925) }}, 100 {{ item(1000257) }}, 100 {{ item(1000263) }}, 1 {{ item(1000874) }}, 3,000,000z | The Lv1 enchant you pick |

If Slot 4 already has a Lv1 or Lv2 enchant, **Slot 4 Enchant** upgrades it instead:

| Upgrade | Cost |
|---|---|
| Lv1 → Lv2 | 50 {{ item(1000257) }}, 1 {{ item(1000263) }}, 1 {{ item(1000874) }} |
| Lv2 → Lv3 | 1 {{ item(7925) }}, 70 {{ item(1000257) }}, 70 {{ item(1000263) }}, 1 {{ item(1000874) }} |

| Enchant | Lv1 | Lv2 | Lv3 |
|---|---|---|---|
| Tenacity | {{ item(29706) }} | {{ item(29707) }} | {{ item(29708) }} |
| Adamantine | {{ item(29101) }} | {{ item(29102) }} | {{ item(29103) }} |
| Magic Essence | {{ item(29071) }} | {{ item(29072) }} | {{ item(29073) }} |
| Master Archer | {{ item(29091) }} | {{ item(29092) }} | {{ item(29093) }} |
| Acute | {{ item(29081) }} | {{ item(29082) }} | {{ item(29083) }} |
| Affection | {{ item(29111) }} | {{ item(29112) }} | {{ item(29113) }} |

### Reset

50 {{ item(1000257) }}, 100 {{ item(1000263) }}, 1,000,000z. Removes the Slot 3 and Slot 4 enchants.

!!! warning "Known issue: headgear is not put back on"
    After an enchant, upgrade or reset, the conversation stops without the "successful" message and the crown
    is left in your inventory. The change has been made. Just equip the crown again.

## Brilliant Light and Sinful weapons

Wear the weapon in your right hand. Both NPCs work the same way. Only the material changes:
the **Briliant Light Enchanter** uses {{ item(1000263) }}, the **Sinful Enchanter** uses {{ item(1000257) }}.
In the tables below, "pieces" means that material.

**Brilliant Light weapons** (23): {{ item(500063) }}, {{ item(500066) }}, {{ item(510092) }},
{{ item(530045) }}, {{ item(540055) }}, {{ item(540060) }}, {{ item(550088) }}, {{ item(550094) }},
{{ item(550116) }}, {{ item(570037) }}, {{ item(580038) }}, {{ item(590045) }}, {{ item(610045) }},
{{ item(620022) }}, {{ item(630027) }}, {{ item(640037) }}, {{ item(650034) }}, {{ item(700065) }},
{{ item(800027) }}, {{ item(810027) }}, {{ item(820021) }}, {{ item(830026) }}, {{ item(840021) }}

**Sinful weapons** (23): {{ item(1341) }}, {{ item(500062) }}, {{ item(500065) }}, {{ item(500072) }},
{{ item(510091) }}, {{ item(540053) }}, {{ item(540054) }}, {{ item(540059) }}, {{ item(550093) }},
{{ item(550115) }}, {{ item(560036) }}, {{ item(570036) }}, {{ item(580037) }}, {{ item(600041) }},
{{ item(610044) }}, {{ item(640036) }}, {{ item(650033) }}, {{ item(700066) }}, {{ item(800026) }},
{{ item(810026) }}, {{ item(820020) }}, {{ item(830025) }}, {{ item(840020) }}

Pick **Slot 3 Enchant** or **Slot 4 Enchant**. If the slot is empty you choose a Lv1 enchant. If it already
has one, the same option upgrades it by one level. The weapon goes to your inventory afterwards.

### Slot 3

New enchant: 1 {{ item(7925) }}, 250 pieces, 3,000,000z. Choose one:

| Enchant | Lv1 | Lv2 | Lv3 | Lv4 | Lv5 |
|---|---|---|---|---|---|
| Expert Archer | {{ item(4832) }} | {{ item(4833) }} | {{ item(4834) }} | {{ item(4835) }} | {{ item(4836) }} |
| Expert Magician | {{ item(311389) }} | {{ item(311390) }} | {{ item(311391) }} | {{ item(311392) }} | {{ item(311393) }} |
| Expert Fighter | {{ item(311384) }} | {{ item(311385) }} | {{ item(311386) }} | {{ item(311387) }} | {{ item(311388) }} |

| Upgrade | Cost |
|---|---|
| → Lv2 | 50 pieces |
| → Lv3 | 55 pieces |
| → Lv4 | 1 {{ item(7925) }}, 60 pieces |
| → Lv5 | 1 {{ item(7925) }}, 65 pieces (Expert Magician also needs 1 {{ item(1000874) }}) |

### Slot 4

New enchant: 150 pieces, 1,500,000z. Choose one:

| Enchant | Lv1 | Lv2 | Lv3 | Lv4 | Lv5 |
|---|---|---|---|---|---|
| Caster | {{ item(311400) }} | {{ item(311401) }} | {{ item(311402) }} | {{ item(311403) }} | {{ item(311404) }} |
| Hit Plus | {{ item(311395) }} | {{ item(311396) }} | {{ item(311397) }} | {{ item(311398) }} | {{ item(311399) }} |
| Delay After Attack | {{ item(4869) }} | {{ item(4872) }} | {{ item(4873) }} | {{ item(4881) }} | {{ item(311394) }} |
| Sharp | {{ item(4818) }} | {{ item(4817) }} | {{ item(4816) }} | {{ item(4843) }} | {{ item(4844) }} |

| Upgrade | Cost |
|---|---|
| → Lv2 | 40 pieces |
| → Lv3 | 45 pieces |
| → Lv4 | 1 {{ item(7925) }}, 50 pieces |
| → Lv5 | 1 {{ item(7925) }}, 55 pieces (Hit Plus also needs 1 {{ item(1000874) }}) |

### Reset

20 pieces + 1,000,000z. Removes the Slot 3 and Slot 4 enchants.

## Sinful and Brilliant Light accessories

Wear the accessory in either slot. If both slots qualify, the NPC asks which one (right first, then left).

| NPC | Accessories | Pieces used |
|---|---|---|
| Sinfull Accessory | {{ item(490044) }}, {{ item(490045) }}, {{ item(490046) }}, {{ item(490047) }}, {{ item(490048) }}, {{ item(490049) }}, {{ item(490050) }}, {{ item(490051) }}, {{ item(490052) }}, {{ item(490053) }}, {{ item(490054) }}, {{ item(490055) }} | {{ item(1000257) }} |
| Brilight Accessory | {{ item(490056) }}, {{ item(490057) }}, {{ item(490058) }}, {{ item(490059) }}, {{ item(490060) }}, {{ item(490061) }}, {{ item(490062) }}, {{ item(490063) }}, {{ item(490064) }}, {{ item(490065) }}, {{ item(490066) }}, {{ item(490067) }} | {{ item(1000263) }} |

One enchant run fills **both** Slot 3 and Slot 4 at once. Slots 3 and 4 must both be empty (reset first).
There is no zeny cost and it always succeeds. Refine and the first card are kept; the 2nd slot is cleared.

| Method | Cost | Type | Level |
|---|---|---|---|
| Method 1 (Choose Type) | 50 pieces | You pick the Slot 3 and Slot 4 type | Random Lv1–Lv5, 20% each, rolled separately per slot |
| Method 2 (Random) | 10 pieces | Random: 25% each Slot 3 type, 50% each Slot 4 type | Random Lv1–Lv5, 20% each |

**Sinful accessory enchants**

| Slot | Types (Lv1 shown, up to Lv5) |
|---|---|
| Slot 3 | {{ item(310197) }}, {{ item(310202) }}, {{ item(310207) }}, {{ item(310212) }} |
| Slot 4 | {{ item(310237) }}, {{ item(310242) }} |

**Brilliant Light accessory enchants**

| Slot | Types (Lv1 shown, up to Lv5) |
|---|---|
| Slot 3 | {{ item(310217) }}, {{ item(310222) }}, {{ item(310227) }}, {{ item(310232) }} |
| Slot 4 | {{ item(310247) }}, {{ item(310252) }} |

!!! warning "Known issue: Brilight Accessory shows the wrong names"
    The Brilight Accessory NPC shows the **Sinful** menu labels and says it needs "Piece of Sin". It really
    takes {{ item(1000263) }}, and the labels map like this:

    | Menu label | You get |
    |---|---|
    | Anger | Empathy |
    | Horror | Happiness |
    | Resentment | Shelter |
    | Regret | Solace |
    | Inverse Scale | Divine Evil |
    | Dragon Scale | Destructive Evil |

    The result screen shows the correct names.

### Reset

| Option | Success | On failure |
|---|---|---|
| 1,000,000z | 70% | **The accessory is destroyed** |
| 10 {{ item(6417) }} | 100% | - |

Reset removes the enchants in slots 2, 3 and 4 and keeps refine and the first card. It takes the cost even if
the accessory has no enchants.
