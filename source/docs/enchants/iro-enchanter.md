# iRO Enchanter

**Location:** {{ npc_where("iRO Enchanter") }} · Quest Room

Gives Follower equipment, OCP accessories and OCP Type A equipment **2 or 3 random options**, like the official
Follower and OCP enchant runes.

| | |
|---|---|
| **Cost** | {{ scalar("npc/miracle/follower_enchant.txt", "Cost") }} Cash Points per enchant |
| **Options 1 and 2** | Always given, rolled separately (the same option can appear twice) |
| **Option 3** | {{ scalar("npc/miracle/follower_enchant.txt", "ThirdChance") }}% chance |
| **Re-rolling** | Enchanting again **replaces all** current options |
| **Kept** | Refine, enchant grade and cards (including JRO enchants) |
| **Not allowed** | Equipped items, rental items and bound items |

Three-option results are announced to the server.

## Possible options

### Follower equipment and OCP accessories

| Option 1 and 2 (always) | Option 3 ({{ scalar("npc/miracle/follower_enchant.txt", "ThirdChance") }}%) |
|---|---|
| STR / AGI / VIT / INT / DEX / LUK +5~15 | POW / SPL / STA / WIS / CON / CRT +1~6 |
| ATK / MATK +10~50 | Max HP / Max SP +5~20% |
| ATK / MATK +5~25% | Variable cast time -5~15% |
| Critical damage +5~25% | After-cast delay -5~15% |
| Long-range damage +5~25% | |

### OCP Type A equipment

These items roll the stronger iRO Random Option Type A instead.

| Option 1 | Option 2 | Option 3 ({{ scalar("npc/miracle/follower_enchant.txt", "ThirdChance") }}%) |
|---|---|---|
| POW / SPL / STA / WIS / CON / CRT +2~12 | ATK / MATK +30~100 | POW / SPL / STA / WIS / CON / CRT +5~15 |
| | ATK / MATK +15~30% | Max HP / Max SP +15~30% |
| | Critical damage +15~30% | Variable cast time -10~15% |
| | Long-range damage +15~30% | After-cast delay -10~15% |

Each option in a column has the same chance, and the value is random within its range.

## Enchantable equipment

{% set cats = array_seq("npc/miracle/follower_enchant.txt", "iRO Enchanter", "Items") %}
{{ items_table(cats[0], "Follower equipment") }}

<details class="abstract shop" markdown="1">
<summary>OCP accessories <span class="count">{{ cats[1]|length }} items</span></summary>

{{ items_table(cats[1], "Accessory") }}

</details>

{{ items_table(cats[2], "OCP Type A equipment") }}
