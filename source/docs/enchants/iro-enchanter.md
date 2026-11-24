# iRO Enchanter

**Location:** {{ npc_where("iRO Enchanter") }} · Quest Room

Gives Follower equipment, OCP accessories, OCP Type A equipment, Kafra Point equipment and Royal Garments **2 or 3
random options**, like the official Follower, OCP and Royal Medal enchant runes and the iRO Kafra Point Enchant Stone.

It also gives **slot enchants** to Royal Garments, OCP Shoes and the Nebula Pendant in the official enchant window.
See [Slot enchants](#slot-enchants).

| | |
|---|---|
| **Cost** | {{ scalar("npc/miracle/follower_enchant.txt", "Cost") }} Cash Points per enchant |
| **Options 1 and 2** | Always given, rolled separately (the same option can appear twice) |
| **Option 3** | {{ scalar("npc/miracle/follower_enchant.txt", "ThirdChance") }}% chance |
| **Re-rolling** | Enchanting again **replaces all** current options |
| **Kept** | Refine, enchant grade and cards (including JRO enchants) |
| **Not allowed** | Equipped items, rental items and bound items |

Three-option results are announced to the server.

## Random options

Pick **Random Option Enchant (Cash Points)** in the NPC's menu.

### Possible options

#### Follower equipment and OCP accessories

| Option 1 and 2 (always) | Option 3 ({{ scalar("npc/miracle/follower_enchant.txt", "ThirdChance") }}%) |
|---|---|
| STR / AGI / VIT / INT / DEX / LUK +5~15 | POW / SPL / STA / WIS / CON / CRT +1~6 |
| ATK / MATK +10~50 | Max HP / Max SP +5~20% |
| ATK / MATK +5~25% | Variable cast time -5~15% |
| Critical damage +5~25% | After-cast delay -5~15% |
| Long-range damage +5~25% | |

#### OCP Type A equipment and Royal Garments

These items roll the stronger iRO Random Option Type A instead. The iRO **Royal Medal Enchant Rune** for Royal
Garments uses the same list.

| Option 1 | Option 2 | Option 3 ({{ scalar("npc/miracle/follower_enchant.txt", "ThirdChance") }}%) |
|---|---|---|
| POW / SPL / STA / WIS / CON / CRT +2~12 | ATK / MATK +30~100 | POW / SPL / STA / WIS / CON / CRT +5~15 |
| | ATK / MATK +15~30% | Max HP / Max SP +15~30% |
| | Critical damage +15~30% | Variable cast time -10~15% |
| | Long-range damage +15~30% | After-cast delay -10~15% |

#### Kafra Point equipment

These items roll the iRO **Kafra Point Enchant Stone** options.

| Option 1 | Option 2 | Option 3 ({{ scalar("npc/miracle/follower_enchant.txt", "ThirdChance") }}%) |
|---|---|---|
| POW / SPL / STA / WIS / CON / CRT +2~12 | Max HP / Max SP +10~25% | EXP +5~20% when killing monsters |
| | *Rare:* ATK / MATK +5~20% | |
| | *Rare:* Critical damage +5~20% | |
| | *Rare:* Long-range damage +5~20% | |

In option 2, Max HP and Max SP are each 10 times more likely than one rare option.

Each option in a column has the same chance unless noted, and the value is random within its range.

### Enchantable equipment

{% set cats = array_seq("npc/miracle/follower_enchant.txt", "iRO Enchanter", "Items") %}
{{ items_table(cats[0], "Follower equipment") }}

<details class="abstract shop" markdown="1">
<summary>OCP accessories <span class="count">{{ cats[1]|length }} items</span></summary>

{{ items_table(cats[1], "Accessory") }}

</details>

{{ items_table(cats[2], "OCP Type A equipment") }}

{{ items_table(cats[3], "Kafra Point equipment") }}

{% if cats|length > 4 %}{{ items_table(cats[4], "Royal Garment") }}{% endif %}

## Slot enchants

Pick **Slot Enchant (Royal Garment / OCP Shoes / Nebula Pendant)** in the NPC's menu, choose your item, and the
official enchant window opens. Take the item off first: the NPC only sees items in your inventory. Slot enchants
are separate from the random options above, so an item can have both.

| Item | Slot 4 | Slot 3 | Slot 2 |
|---|---|---|---|
| **Royal Garments** | Varmundt enchant, upgrade up to Lv 3 | Jewel enchant, upgrade up to Lv 10 | Meow Power enchant |
| **OCP Shoes** | Warrior / Shooter / Magician Orb, upgrade up to Lv 15 | Power / Spell Orb, upgrade up to Lv 20 | Special enchant |
| **Nebula Pendant** | Random Star Lv 1~5, or Spell / Expert Archer / Fighting Spirit / Sharp 3~4 | Same as slot 4 | Same as slot 4 |

- The slots fill in order: **slot 4 first, then slot 3, then slot 2** (the tables below use the database numbers 3,
  2 and 1 for the same slots).
- **Every enchant and every upgrade** costs 50 {{ item_name(1000874) }} and 100 {{ item_name(6417) }}, and always
  succeeds.
- **Reset** removes all slot enchants for 400 {{ item_name(6417) }} and always works. The item is never destroyed.
- {{ item_name(1000874) }} comes from the [Event Shop](../shops/event-shop.md) and the
  [Instance Point Merchant](../shops/instance-point-merchant.md).

<details class="abstract shop" markdown="1">
<summary>Royal Garments: enchant lists</summary>

{{ item_enchant(220) }}

</details>

<details class="abstract shop" markdown="1">
<summary>OCP Shoes: enchant lists</summary>

{{ item_enchant(221) }}

</details>

<details class="abstract shop" markdown="1">
<summary>Nebula Pendant: enchant lists</summary>

{{ item_enchant(222) }}

</details>
