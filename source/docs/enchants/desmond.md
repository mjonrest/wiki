# Armor Enchanter (Desmond)

**Location:** {{ npc_where("Desmond") }} · Quest Room

{% set a = arrays("npc/miracle/sp_enchant.txt", "Desmond") %}
| | |
|---|---|
| **Enchant cost** | {{ a.CostEnchant[1] }}× {{ item(a.CostEnchant[0]) }} + {{ fmt(a.CostEnchant[2]) }} Zeny |
| **Reset cost** | {{ a.CostReset[1] }}× {{ item(a.CostReset[0]) }} + {{ fmt(a.CostReset[2]) }} Zeny |

Each enchant fills the **next empty slot** that has a pool, with one random enchant from it. Every enchant in a
pool has the same chance. Reset removes all enchants.

## Equipment and enchant pools

Click an item group to see what it can roll.

{{ slot_enchanter("npc/miracle/sp_enchant.txt", "Desmond") }}
