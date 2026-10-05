# iRO Enchanter

**Location:** {{ npc_where("iRO Enchanter") }} · Quest Room

Gives Follower equipment and OCP accessories **2 or 3 random options**, like the official Follower enchant.

| | |
|---|---|
| **Cost** | {{ scalar("npc/miracle/follower_enchant.txt", "Cost") }} Cash Points per enchant |
| **Options 1 and 2** | Always given, rolled separately (the same option can appear twice) |
| **Option 3** | {{ scalar("npc/miracle/follower_enchant.txt", "ThirdChance") }}% chance |
| **Re-rolling** | Enchanting again **replaces all** current options |
| **Kept** | Refine, enchant grade, cards and bound status |
| **Not allowed** | Equipped items and rental items |

Three-option results are announced to the server.

## Possible options

| Option 1 and 2 (always) | Option 3 ({{ scalar("npc/miracle/follower_enchant.txt", "ThirdChance") }}%) |
|---|---|
| STR / AGI / VIT / INT / DEX / LUK +5~15 | POW / SPL / STA / WIS / CON / CRT +1~6 |
| ATK / MATK +10~50 | Max HP / Max SP +5~20% |
| ATK / MATK +5~25% | Variable cast time -5~15% |
| Critical damage +5~25% | After-cast delay -5~15% |
| Long-range damage +5~25% | |

Each option in a column has the same chance, and the value is random within its range.

## Enchantable equipment

{% set items = arrays("npc/miracle/follower_enchant.txt", "iRO Enchanter")["Items"] %}
{{ items_table(items[:17], "Follower equipment") }}

<details class="abstract shop" markdown="1">
<summary>OCP accessories <span class="count">{{ items|length - 17 }} items</span></summary>

{{ items_table(items[17:], "Accessory") }}

</details>
