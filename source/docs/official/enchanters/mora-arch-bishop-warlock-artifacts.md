# Mora Arch Bishop & Warlock Artifacts

<!-- npcs: Keeper of Secrets; Master of Relics; Guardian of Artifacts; Artifact Crafter; Artifact Collector -->

In Mora you can trade {{ item(6380) }} for Arch Bishop and Warlock artifacts, have them enchanted with random stats, and finally turn a well-enchanted +7 weapon into its **Empowered** version.

| NPC | What it does | Where |
|---|---|---|
| Keeper of Secrets | Sells Arch Bishop relics for Mora Coins | `/navi mora 88/89` |
| Master of Relics | Enchants Arch Bishop relics | `/navi mora 96/74` |
| Guardian of Artifacts | Sells Warlock artifacts for Mora Coins | `/navi mora 104/76` |
| Artifact Crafter | Enchants Warlock artifacts | `/navi mora 99/93` |
| Artifact Collector | Turns a +7 enchanted staff/wand/mace into its Empowered version | `/navi mora 124/82` |

## Getting the artifacts

### Keeper of Secrets (Arch Bishop relics)

**Where:** `/navi mora 88/89`

You need at least 10 {{ item(6380) }}. Pick a category; you get **one random item** from that category for 10 Mora Coins.

| Category | Possible items (equal chance) |
|---|---|
| Ring | {{ item(2864) }}, {{ item(2865) }}, {{ item(2866) }} |
| Shoes | {{ item(2471) }}, {{ item(2472) }} |
| Shawl | {{ item(2569) }}, {{ item(2570) }} |
| Robe | {{ item(15029) }}, {{ item(15030) }} |
| Shield | {{ item(2156) }} |
| Weapon | {{ item(1657) }}, {{ item(16013) }} |

!!! tip "Ring rules"
    Only Arch Bishops can get a ring, and only if they carry none of the three rings already. Characters who are **not** Arch Bishops can trade one of these rings back to the Keeper for 10 Mora Coins.

### Guardian of Artifacts (Warlock artifacts)

**Where:** `/navi mora 104/76`

Same deal: 10 {{ item(6380) }} for **one random item** from the category you pick. There is no job check.

| Category | Possible items (equal chance) |
|---|---|
| Shoes | {{ item(2467) }}, {{ item(2468) }}, {{ item(2469) }}, {{ item(2470) }} |
| Orbs | {{ item(2859) }}, {{ item(2860) }}, {{ item(2861) }}, {{ item(2862) }} |
| Robes | {{ item(15025) }}, {{ item(15026) }}, {{ item(15027) }}, {{ item(15028) }} |
| Staves | {{ item(2007) }}, {{ item(2008) }}, {{ item(2009) }}, {{ item(2010) }} |

## How these enchants work

Master of Relics and Artifact Crafter work the same way:

- The item must be in your **inventory**; you choose it from a list.
- One attempt costs **2 {{ item(6380) }}**. Coins and the item are taken before the roll.
- On success you get the item back as a **brand-new copy**: refine is reset to **+0**, any card is gone, and every old enchant is replaced by the new roll. The NPC does not care whether the item was enchanted before.
- On failure (about **30%**) the item is **destroyed**.
- Each attempt fills all slots at once (2 or 3 enchants). You cannot keep part of a roll.

!!! tip
    If you carry several copies of the same item, the NPC takes an unrefined, unenchanted copy first. Still, put any copy you want to keep in storage before you start.

## Master of Relics

**Where:** `/navi mora 96/74`

**Cost:** 2 {{ item(6380) }} per attempt.

### Rings

Works on {{ item(2864) }}, {{ item(2865) }} and {{ item(2866) }}. Enchants go into the 3rd and 4th slots. Each ring has its own special enchant:

| Ring | Special enchant |
|---|---|
| {{ item(2864) }} | {{ item(4803) }} |
| {{ item(2865) }} | {{ item(4804) }} |
| {{ item(2866) }} | {{ item(4805) }} |

| Result | Chance |
|---|---|
| Normal enchant (see below) | 68.86% |
| Special enchant in **both** 3rd and 4th slot | 1.08% |
| Ring destroyed | 30.06% |

On a normal enchant each slot rolls one of four options with equal chance (25% each):

| 3rd slot | 4th slot |
|---|---|
| {{ item(4711) }} | The ring's special enchant |
| {{ item(4720) }} | {{ item(4799) }} |
| {{ item(4721) }} | {{ item(4766) }} |
| {{ item(4740) }} | {{ item(4788) }} |

### Shoes, shawls, robes and the Bible

Works on {{ item(2471) }}, {{ item(2472) }}, {{ item(2569) }}, {{ item(2570) }}, {{ item(15029) }}, {{ item(15030) }}, {{ item(2156) }}. Enchants go into the 2nd, 3rd and 4th slots.

| Result | Chance |
|---|---|
| Normal enchant (see below) | 68.86% |
| One of the 8 jackpot sets below | 0.13% each |
| Item destroyed | 30.06% |

Normal enchant, each slot 25% per option:

| 2nd slot | 3rd slot | 4th slot |
|---|---|---|
| {{ item(4710) }} | {{ item(4711) }} | {{ item(4764) }} |
| {{ item(4711) }} | {{ item(4720) }} | {{ item(4799) }} |
| {{ item(4720) }} | {{ item(4721) }} | {{ item(4766) }} |
| {{ item(4721) }} | {{ item(4740) }} | {{ item(4788) }} |

Jackpot sets (0.13% each):

| 2nd slot | 3rd slot | 4th slot |
|---|---|---|
| {{ item(4761) }} | {{ item(4761) }} | {{ item(4761) }} |
| {{ item(4712) }} | {{ item(4713) }} | {{ item(4713) }} |
| {{ item(4712) }} | {{ item(4761) }} | {{ item(4761) }} |
| {{ item(4712) }} | {{ item(4713) }} | {{ item(4761) }} |
| {{ item(4722) }} | {{ item(4723) }} | {{ item(4723) }} |
| {{ item(4722) }} | {{ item(4703) }} | {{ item(4703) }} |
| {{ item(4722) }} | {{ item(4767) }} | {{ item(4767) }} |
| {{ item(4767) }} | {{ item(4767) }} | {{ item(4767) }} |

### Weapons

Works on {{ item(1657) }} and {{ item(16013) }}. Enchants go into the 3rd and 4th slots, so the weapon's two card slots stay free for cards (but any card already in it is lost, because you get a fresh copy).

| Result | Chance |
|---|---|
| Normal enchant (see below) | 69.57% |
| One of the 6 jackpot sets below | 0.07% each |
| Weapon destroyed | 30.01% |

Normal enchant, each slot 25% per option:

| Weapon | 3rd slot options | 4th slot options |
|---|---|---|
| {{ item(1657) }} | {{ item(4720) }}, {{ item(4740) }}, {{ item(4741) }}, {{ item(4801) }} | {{ item(4710) }}, {{ item(4711) }}, {{ item(4721) }}, {{ item(4760) }} |
| {{ item(16013) }} | {{ item(4720) }}, {{ item(4740) }}, {{ item(4741) }}, {{ item(4701) }} | {{ item(4700) }}, {{ item(4701) }}, {{ item(4721) }}, {{ item(4767) }} |

Jackpot sets (0.07% each):

| {{ item(1657) }} (3rd + 4th) | {{ item(16013) }} (3rd + 4th) |
|---|---|
| {{ item(4761) }} + {{ item(4761) }} | {{ item(4767) }} + {{ item(4767) }} |
| {{ item(4761) }} + {{ item(4723) }} | {{ item(4767) }} + {{ item(4723) }} |
| {{ item(4761) }} + {{ item(4714) }} | {{ item(4767) }} + {{ item(4704) }} |
| {{ item(4714) }} + {{ item(4714) }} | {{ item(4704) }} + {{ item(4704) }} |
| {{ item(4714) }} + {{ item(4723) }} | {{ item(4704) }} + {{ item(4723) }} |
| {{ item(4723) }} + {{ item(4723) }} | {{ item(4723) }} + {{ item(4723) }} |

## Artifact Crafter

**Where:** `/navi mora 99/93`

**Cost:** 2 {{ item(6380) }} per attempt.

### Staves

Works on {{ item(2007) }}, {{ item(2008) }}, {{ item(2009) }}, {{ item(2010) }}. Enchants go into the 3rd and 4th slots.

| Result | Chance |
|---|---|
| Normal enchant (see below) | 69.69% |
| One of the 4 jackpot sets below | 0.07% each |
| Staff destroyed | 30.03% |

Normal enchant, each slot 25% per option:

| 3rd slot | 4th slot |
|---|---|
| {{ item(4720) }} | {{ item(4786) }} |
| {{ item(4796) }} | {{ item(4760) }} |
| {{ item(4710) }} | {{ item(4711) }} |
| {{ item(4801) }} | {{ item(4721) }} |

Jackpot sets (0.07% each): 

| 3rd slot | 4th slot |
|---|---|
| {{ item(4713) }} | {{ item(4761) }} |
| {{ item(4713) }} | {{ item(4713) }} |
| {{ item(4761) }} | {{ item(4761) }} |
| {{ item(4761) }} | {{ item(4713) }} |

### Shoes, orbs and robes

Works on {{ item(2467) }}, {{ item(2468) }}, {{ item(2469) }}, {{ item(2470) }}, {{ item(2859) }}, {{ item(2860) }}, {{ item(2861) }}, {{ item(2862) }}, {{ item(15025) }}, {{ item(15026) }}, {{ item(15027) }}, {{ item(15028) }}. Enchants go into the 2nd, 3rd and 4th slots.

| Result | Chance |
|---|---|
| Normal enchant (see below) | 69.42% |
| One of the 8 jackpot sets below | 0.07% each |
| Item destroyed | 30.02% |

Normal enchant, each slot 25% per option:

| 2nd slot | 3rd slot | 4th slot |
|---|---|---|
| {{ item(4710) }} | {{ item(4720) }} | {{ item(4786) }} |
| {{ item(4711) }} | {{ item(4796) }} | {{ item(4760) }} |
| {{ item(4720) }} | {{ item(4710) }} | {{ item(4711) }} |
| {{ item(4721) }} | {{ item(4801) }} | {{ item(4721) }} |

Jackpot sets (0.07% each):

| 2nd slot | 3rd slot | 4th slot |
|---|---|---|
| {{ item(4712) }} | {{ item(4713) }} | {{ item(4761) }} |
| {{ item(4712) }} | {{ item(4713) }} | {{ item(4713) }} |
| {{ item(4712) }} | {{ item(4761) }} | {{ item(4761) }} |
| {{ item(4712) }} | {{ item(4761) }} | {{ item(4713) }} |
| {{ item(4722) }} | {{ item(4713) }} | {{ item(4761) }} |
| {{ item(4722) }} | {{ item(4713) }} | {{ item(4713) }} |
| {{ item(4722) }} | {{ item(4761) }} | {{ item(4761) }} |
| {{ item(4722) }} | {{ item(4761) }} | {{ item(4713) }} |

## Artifact Collector (Empowered weapons)

**Where:** `/navi mora 124/82`

The Artifact Collector exchanges an enchanted artifact weapon for its Empowered version. There is no fee and no failure chance.

**Requirements:**

- The weapon must be **equipped**.
- It must be refined to **+7 or higher**.
- Its 3rd or 4th slot must hold one of the enchants listed below.

| Weapon | Needs one of these enchants | Becomes |
|---|---|---|
| {{ item(1657) }} | {{ item(4761) }}, {{ item(4714) }}, {{ item(4723) }} | {{ item(1660) }} |
| {{ item(16013) }} | {{ item(4723) }}, {{ item(4704) }}, {{ item(4767) }} | {{ item(16018) }} |
| {{ item(2007) }} | {{ item(4761) }}, {{ item(4713) }} | {{ item(2011) }} |
| {{ item(2008) }} | {{ item(4761) }}, {{ item(4713) }} | {{ item(2012) }} |
| {{ item(2009) }} | {{ item(4761) }}, {{ item(4713) }} | {{ item(2013) }} |
| {{ item(2010) }} | {{ item(4761) }}, {{ item(4713) }} | {{ item(2014) }} |

!!! tip "You lose the refine, cards and enchants"
    You get a plain **+0** Empowered weapon with no cards and no enchants. The Collector says so himself. The Empowered weapons can then be enchanted at the [Artifact Researcher](mora-artifact-researcher.md).

!!! tip "Which rolls qualify"
    For the staves and the {{ item(1657) }}, none of the normal enchants qualify, so you need one of the rare jackpot sets (every jackpot set qualifies). That is about 0.28% per attempt for a staff and 0.42% for the wand. The {{ item(16013) }} is much easier: {{ item(4767) }} is one of its normal 4th-slot options, so about 17.81% of attempts qualify.
