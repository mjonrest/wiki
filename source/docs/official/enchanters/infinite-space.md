# Infinite Space Artifact Enhancer

<!-- npcs: Artifact Enhancer; Artifact Appraiser -->

The **Artifact Enhancer** enchants the Infinity and Rift gear from Infinite Space with
{{ item(6905) }}. The **Artifact Appraiser** next to her sells that gear.

**Where:** Artifact Enhancer `/navi cmd_fild07 60/275`, Artifact Appraiser `/navi cmd_fild07 57/275`

## Getting the gear

The Artifact Appraiser sells each item below for 50 {{ item(6905) }}.

| Type | Items |
|---|---|
| Weapons | {{ item(1994) }}, {{ item(1938) }}, {{ item(13323) }}, {{ item(13126) }}, {{ item(28703) }}, {{ item(2024) }}, {{ item(16038) }}, {{ item(21014) }}, {{ item(28105) }}, {{ item(18128) }} |
| Armor | {{ item(15141) }} |
| Shoes | {{ item(22075) }} |
| Garment | {{ item(20779) }} |
| Helm (upper headgear) | {{ item(19033) }} |

## Enchanting

Wear the item and pick its slot (Weapon, Armor, Shoes, Garment, Helm). The weapon must be in your right hand.
You need 1,000 free weight.

**Cost:** 20 {{ item(6905) }} per enchant. It **always succeeds**. Refine and cards are kept.

Two enchants per item: the 1st goes into slot 4, the 2nd into slot 3. Each time you pick a type
(Physical, Magical or Range) and get a random enchant from that list. Every entry in a list has the same
chance.

!!! warning "Known issue: Quit does not cancel"
    Choosing **Quit** on the Physical / Magical / Range menu does not end the conversation. To back out,
    choose **I'll return later.** on the next screen.

### 1st enchant (slot 4)

| Item | Physical | Magical | Range |
|---|---|---|---|
| Weapons | {{ item(4700) }}, {{ item(4701) }} (50% each) | {{ item(4710) }}, {{ item(4711) }} (50% each) | {{ item(4720) }}, {{ item(4721) }} (50% each) |
| Armor, shoes, garment, helm | {{ item(4700) }} … {{ item(4703) }} (25% each) | {{ item(4710) }} … {{ item(4713) }} (25% each) | {{ item(4720) }} … {{ item(4723) }} (25% each) |

### 2nd enchant (slot 3)

**Weapons** (12.5% each):

| Type | Possible enchants |
|---|---|
| Physical | {{ item(4811) }}, {{ item(4810) }}, {{ item(4809) }}, {{ item(4808) }}, {{ item(4820) }}, {{ item(4821) }}, {{ item(4822) }}, {{ item(4823) }} |
| Magical | {{ item(4815) }}, {{ item(4814) }}, {{ item(4813) }}, {{ item(4812) }}, {{ item(4826) }}, {{ item(4827) }}, {{ item(4828) }}, {{ item(4829) }} |
| Range | {{ item(4832) }}, {{ item(4833) }}, {{ item(4834) }}, {{ item(4835) }}, {{ item(4836) }}, {{ item(4837) }}, {{ item(4838) }}, {{ item(4839) }} |

**Armor and shoes** (33.33% each):

| Type | Possible enchants |
|---|---|
| Physical | {{ item(4795) }}, {{ item(4796) }}, {{ item(4797) }} |
| Magical | {{ item(4870) }}, {{ item(4871) }}, {{ item(4800) }} |
| Range | {{ item(4870) }}, {{ item(4871) }}, {{ item(4800) }} |

**Garment and helm** (20% each, all three types use the same list): {{ item(4861) }}, {{ item(4862) }},
{{ item(4867) }}, {{ item(4868) }}, {{ item(4900) }}

## Initialize (reset)

**Cost:** 30 {{ item(6905) }}. Removes both enchants. Refine and cards are kept. The item must have at least
one enchant.

!!! warning "Known issue: the break warning is wrong"
    The NPC warns that the item may be destroyed during the reset. In the current script the reset
    **always succeeds** and never destroys the item.
