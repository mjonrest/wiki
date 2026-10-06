# Consecrated Weapons (Ester)

<!-- npcs: Ester -->

**Ester** purifies the Adulter Fides weapons into Vivatus Fides weapons, and sells the
Pontifex items that give these weapons random options.

**Where:** `/navi grademk 48/169`

| Menu | What it does |
|---|---|
| Purification Ritual | Reform window: cheaper, refine drops by 5 |
| Advanced Purification Ritual | Reform window: more expensive, refine drops by 1 |
| Enchantment | Shop that sells the Pontifex items for 20,000,000z each |

## Purification (reform)

Put the weapon in the reform window from your **inventory** (unequip it first). It must be refined to
**+9 or higher**. The reform always succeeds. Cards, enchants, the enchant grade and random options are kept.

| Ritual | Refine afterwards | Cost |
|---|---|---|
| Purification Ritual | refine **-5** (a +9 weapon becomes +4) | 10 × the weapon's blueprint, 50 × {{ item(1000501) }}, 50 × {{ item(1000502) }}, 50 × {{ item(1000503) }}, 200 × {{ item(1000405) }} |
| Advanced Purification Ritual | refine **-1** (a +9 weapon becomes +8) | 30 × the weapon's blueprint, 200 × {{ item(1000501) }}, 200 × {{ item(1000502) }}, 200 × {{ item(1000503) }}, 400 × {{ item(1000405) }} |

39 weapons can be purified. Each one needs its own blueprint:

| Weapon (+9 or higher) | Becomes | Blueprint |
|---|---|---|
| {{ item(600017) }} | {{ item(600018) }} | {{ item(1000475) }} |
| {{ item(630012) }} | {{ item(630013) }} | {{ item(1000476) }} |
| {{ item(500025) }} | {{ item(500027) }} | {{ item(1000477) }} |
| {{ item(530013) }} | {{ item(530014) }} | {{ item(1000478) }} |
| {{ item(520008) }} | {{ item(520009) }} | {{ item(1000479) }} |
| {{ item(590021) }} | {{ item(590023) }} | {{ item(1000480) }} |
| {{ item(500026) }} | {{ item(500028) }} | {{ item(1000481) }} |
| {{ item(590022) }} | {{ item(590024) }} | {{ item(1000482) }} |
| {{ item(610020) }} | {{ item(610022) }} | {{ item(1000483) }} |
| {{ item(610021) }} | {{ item(610023) }} | {{ item(1000484) }} |
| {{ item(510032) }} | {{ item(510033) }} | {{ item(1000485) }} |
| {{ item(700030) }} | {{ item(700033) }} | {{ item(1000486) }} |
| {{ item(640019) }} | {{ item(640021) }} | {{ item(1000487) }} |
| {{ item(640020) }} | {{ item(640022) }} | {{ item(1000488) }} |
| {{ item(540019) }} | {{ item(540024) }} | {{ item(1000489) }} |
| {{ item(540020) }} | {{ item(540025) }} | {{ item(1000490) }} |
| {{ item(540021) }} | {{ item(540026) }} | {{ item(1000491) }} |
| {{ item(550024) }} | {{ item(550029) }} | {{ item(1000492) }} |
| {{ item(560018) }} | {{ item(560020) }} | {{ item(1000493) }} |
| {{ item(560019) }} | {{ item(560021) }} | {{ item(1000494) }} |
| {{ item(700031) }} | {{ item(700034) }} | {{ item(1000495) }} |
| {{ item(700032) }} | {{ item(700035) }} | {{ item(1000496) }} |
| {{ item(570017) }} | {{ item(570019) }} | {{ item(1000497) }} |
| {{ item(580017) }} | {{ item(580019) }} | {{ item(1000498) }} |
| {{ item(570018) }} | {{ item(570020) }} | {{ item(1000499) }} |
| {{ item(580018) }} | {{ item(580020) }} | {{ item(1000500) }} |
| {{ item(650008) }} | {{ item(650022) }} | {{ item(1000685) }} |
| {{ item(650009) }} | {{ item(650021) }} | {{ item(1000686) }} |
| {{ item(800003) }} | {{ item(800012) }} | {{ item(1000687) }} |
| {{ item(810002) }} | {{ item(810008) }} | {{ item(1000689) }} |
| {{ item(830003) }} | {{ item(830011) }} | {{ item(1000690) }} |
| {{ item(840002) }} | {{ item(840007) }} | {{ item(1000691) }} |
| {{ item(540022) }} | {{ item(540046) }} | {{ item(1000692) }} |
| {{ item(540023) }} | {{ item(540045) }} | {{ item(1000693) }} |
| {{ item(550025) }} | {{ item(550064) }} | {{ item(1000694) }} |
| {{ item(550026) }} | {{ item(550063) }} | {{ item(1000695) }} |
| {{ item(550027) }} | {{ item(550065) }} | {{ item(1000696) }} |
| {{ item(550028) }} | {{ item(550066) }} | {{ item(1000697) }} |
| {{ item(820002) }} | {{ item(820006) }} | {{ item(1000688) }} |

## Pontifex items (random options)

Ester sells four Pontifex items for **20,000,000z** each. Using one opens a window where you put in the
weapon from your **inventory** (unequip it first). It always works and the item is used up.

| Item | Works on | Kind |
|---|---|---|
| {{ item(100650) }} | Adulter Fides weapons (before purification) | Physical |
| {{ item(100651) }} | Adulter Fides weapons (before purification) | Magical |
| {{ item(100652) }} | Vivatus Fides weapons (after purification) | Physical |
| {{ item(100653) }} | Vivatus Fides weapons (after purification) | Magical |

Each use **replaces all random options** on the weapon with two new ones: one from the Option 1 list and one
from the Option 2 list. Every option in a list has the same chance, and the value is random within the range
shown. Refine, cards and enchants are kept.

Random options are kept when you purify the weapon, so options from Courage or Wisdom carry over to the
Vivatus Fides weapon until you use Tenacity or Belief on it.

=== "Pontifex Courage"

    **Option 1** (21 possible options):

    | Option | Value | Chance |
    |---|---|---|
    | Max HP | +200 to +1000 | 4.76% |
    | Max SP | +50 to +250 | 4.76% |
    | ATK | +1% to +5% | 4.76% |
    | ATK | +10 to +50 | 4.76% |
    | DEF | +10 to +50 | 4.76% |
    | FLEE | +5 to +25 | 4.76% |
    | HIT | +5 to +25 | 4.76% |
    | Physical damage against Demi-Human/Brute/Demon/Dragon/Plant/Formless/Angel/Undead/Insect/Fish monsters (one of them) | +3% to +15% | 4.76% each |
    | Ranged physical damage | +2% to +10% | 4.76% |
    | Melee physical damage | +2% to +10% | 4.76% |
    | Critical damage | +2% to +10% | 4.76% |
    | After-cast delay | -1% to -3% | 4.76% |

    **Option 2** (14 possible options):

    | Option | Value | Chance |
    |---|---|---|
    | Physical damage against Fire/Holy/Shadow/Poison/Neutral/Ghost/Undead property monsters (one of them) | +2% to +10% | 7.14% each |
    | Ranged physical damage | +2% to +10% | 7.14% |
    | Melee physical damage | +2% to +10% | 7.14% |
    | Critical damage | +2% to +10% | 7.14% |
    | Physical damage against Small/Medium/Large size monsters (one of them) | +2% to +10% | 7.14% each |
    | After-cast delay | -1% to -3% | 7.14% |

=== "Pontifex Wisdom"

    **Option 1** (27 possible options):

    | Option | Value | Chance |
    |---|---|---|
    | Max HP | +200 to +1000 | 3.7% |
    | Max SP | +50 to +250 | 3.7% |
    | MATK | +1% to +5% | 3.7% |
    | MATK | +10 to +50 | 3.7% |
    | DEF | +10 to +50 | 3.7% |
    | FLEE | +5 to +25 | 3.7% |
    | Variable cast time | -2% to -10% | 3.7% |
    | Magic damage against Demi-Human/Brute/Demon/Dragon/Plant/Formless/Angel/Undead/Insect/Fish monsters (one of them) | +3% to +15% | 3.7% each |
    | Water/Wind/Earth/Fire/Holy/Shadow/Poison/Neutral/Ghost magic damage (one of them) | +2% to +10% | 3.7% each |
    | After-cast delay | -1% to -3% | 3.7% |

    **Option 2** (14 possible options):

    | Option | Value | Chance |
    |---|---|---|
    | Magic damage against Undead property monsters | +2% to +10% | 7.14% |
    | Water/Wind/Earth/Fire/Holy/Shadow/Poison/Neutral/Ghost magic damage (one of them) | +2% to +10% | 7.14% each |
    | Magic damage against Small/Medium/Large size monsters (one of them) | +2% to +10% | 7.14% each |
    | After-cast delay | -1% to -3% | 7.14% |

=== "Pontifex Tenacity"

    **Option 1** (21 possible options):

    | Option | Value | Chance |
    |---|---|---|
    | Max HP | +250 to +1250 | 4.76% |
    | Max SP | +75 to +375 | 4.76% |
    | ATK | +2% to +10% | 4.76% |
    | ATK | +12 to +60 | 4.76% |
    | DEF | +12 to +60 | 4.76% |
    | FLEE | +6 to +30 | 4.76% |
    | HIT | +6 to +30 | 4.76% |
    | Physical damage against Demi-Human/Brute/Demon/Dragon/Plant/Formless/Angel/Undead/Insect/Fish monsters (one of them) | +4% to +20% | 4.76% each |
    | Ranged physical damage | +2% to +10% | 4.76% |
    | Melee physical damage | +2% to +10% | 4.76% |
    | Critical damage | +2% to +10% | 4.76% |
    | After-cast delay | -1% to -5% | 4.76% |

    **Option 2** (17 possible options):

    | Option | Value | Chance |
    |---|---|---|
    | Physical damage against Water/Wind/Earth/Fire/Holy/Shadow/Poison/Neutral/Ghost/Undead property monsters (one of them) | +3% to +15% | 5.88% each |
    | Ranged physical damage | +3% to +15% | 5.88% |
    | Melee physical damage | +3% to +15% | 5.88% |
    | Critical damage | +3% to +15% | 5.88% |
    | Physical damage against Small/Medium/Large size monsters (one of them) | +3% to +15% | 5.88% each |
    | After-cast delay | -1% to -5% | 5.88% |

=== "Pontifex Belief"

    **Option 1** (27 possible options):

    | Option | Value | Chance |
    |---|---|---|
    | Max HP | +250 to +1250 | 3.7% |
    | Max SP | +75 to +375 | 3.7% |
    | MATK | +2% to +10% | 3.7% |
    | MATK | +12 to +60 | 3.7% |
    | DEF | +12 to +60 | 3.7% |
    | FLEE | +6 to +30 | 3.7% |
    | Variable cast time | -3% to -15% | 3.7% |
    | Magic damage against Demi-Human/Brute/Demon/Dragon/Plant/Formless/Angel/Undead/Insect/Fish monsters (one of them) | +4% to +20% | 3.7% each |
    | Water/Wind/Earth/Fire/Holy/Shadow/Poison/Neutral/Ghost magic damage (one of them) | +3% to +15% | 3.7% each |
    | After-cast delay | -1% to -5% | 3.7% |

    **Option 2** (17 possible options):

    | Option | Value | Chance |
    |---|---|---|
    | Magic damage against Poison/Neutral/Ghost/Undead property monsters (one of them) | +3% to +15% | 5.88% each |
    | Water/Wind/Earth/Fire/Holy/Shadow/Poison/Neutral/Ghost magic damage (one of them) | +3% to +15% | 5.88% each |
    | Magic damage against Small/Medium/Large size monsters (one of them) | +3% to +15% | 5.88% each |
    | After-cast delay | -1% to -5% | 5.88% |
