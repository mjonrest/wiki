# Accessory Enchanter (Aulion)

**Location:** {{ npc_where("Aulion") }} · Quest Room

{% set a = arrays("npc/miracle/sp_enchant.txt", "Aulion") %}
| | |
|---|---|
| **Enchant cost** | {{ a.CostEnchant[1] }}× {{ item(a.CostEnchant[0]) }} + {{ fmt(a.CostEnchant[2]) }} Zeny |
| **Reset cost** | {{ a.CostReset[1] }}× {{ item(a.CostReset[0]) }} + {{ fmt(a.CostReset[2]) }} Zeny |

Each enchant fills the **next empty slot** (slot 2, then 3, then 4) with one random enchant from that slot's pool.
Every enchant in a pool has the same chance. Reset clears slots 2 to 4 so you can start again.

## Equipment and enchant pools

{{ slot_enchanter("npc/miracle/sp_enchant.txt", "Aulion") }}
