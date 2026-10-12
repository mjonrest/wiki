# JRO Enchanter

**Location:** {{ npc_where("JRO Enchanter") }} · Quest Room

{% set a = arrays("npc/miracle/jro_enchant.txt", "JRO Enchanter") %}
| | |
|---|---|
| **Enchant cost** | {{ a.CostEnchant[1] }}× {{ item(a.CostEnchant[0]) }} + {{ fmt(a.CostEnchant[2]) }} Zeny |
| **Reset cost** | {{ a.CostReset[1] }}× {{ item(a.CostReset[0]) }} + {{ fmt(a.CostReset[2]) }} Zeny |

The JRO Enchanter adds the Japanese server's special enchants to headgear, armor, weapons, shields, garments,
shoes and accessories. It replaces the old Aulion and Desmond enchanters.

- Slots are filled in order: **slot 4 first, then slot 3, then slot 2**. Each try fills the next empty slot with one
  random enchant from that slot's list. Every enchant in a list has the same chance.
- Some slots need the item to be refined first. The **Refine** column shows the lowest refine for that slot.
- Slots that are card slots of the item (for example slot 2 of a weapon with 2 card slots) are never enchanted.
- **Reset** removes every enchant (cards stay) so you can start again. Refine, grade and random options are kept.
- Rental items, signed or forged items and equipped items can't be enchanted. Take the item off first.

## Equipment and enchant lists

Click an item to see what each slot can roll.

{{ slot_enchanter("npc/miracle/jro_enchant.txt", "JRO Enchanter") }}
