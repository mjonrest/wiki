# Enchants

| Enchanter | Location | Works on | Cost |
|---|---|---|---|
| [iRO Enchanter](iro-enchanter.md) | {{ npc_where("iRO Enchanter") }} | Follower gear and OCP accessories | {{ scalar("npc/miracle/follower_enchant.txt", "Cost") }} Cash Points |
| [Aulion](aulion.md) | {{ npc_where("Aulion") }} | Accessories | {{ arrays("npc/miracle/sp_enchant.txt", "Aulion")["CostEnchant"][1] }}× {{ item_name(arrays("npc/miracle/sp_enchant.txt", "Aulion")["CostEnchant"][0]) }} + {{ fmt(arrays("npc/miracle/sp_enchant.txt", "Aulion")["CostEnchant"][2]) }} Zeny |
| [Desmond](desmond.md) | {{ npc_where("Desmond") }} | Armor, garments, shoes, headgear | {{ arrays("npc/miracle/sp_enchant.txt", "Desmond")["CostEnchant"][1] }}× {{ item_name(arrays("npc/miracle/sp_enchant.txt", "Desmond")["CostEnchant"][0]) }} + {{ fmt(arrays("npc/miracle/sp_enchant.txt", "Desmond")["CostEnchant"][2]) }} Zeny |
| [Wing Enchanters](wing-enchanters.md) | {{ npc_where("Fallen Angel Wing Enchanter") }} | Fallen Angel Wing, Archangel Wing | 2× {{ item_name(6417) }} |
| [Special Enchanter](special.md) | {{ npc_where("Special Enchanter") }} | Mad Bunny-LT | Enchant tickets |
| [Memory Enchanter](special.md#memory-enchanter) | {{ npc_where("Memory Enchanter") }} | Memory Records | Silvervine and bio materials |

!!! tip "Unequip first"
    All enchanters only see items in your inventory. Take the item off before talking to them.
