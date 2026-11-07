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
- **Reset** removes every enchant (cards stay) so you can start again. Refine, grade and random options are kept,
  so an item can have JRO enchants and iRO Enchanter options at the same time.
- Rental items, bound items, signed or forged items and equipped items can't be enchanted. Take the item off first.

## Pity: Guaranteed Pick

Not every enchant in a list is useful, so bad luck is softened:

- Every paid enchant adds **1** to your pity counter. The NPC shows it as **Pity: N/100**.
- At **100** the counter goes back to 0 and you get **1 Guaranteed Pick**.
- With a Guaranteed Pick you **choose** which enchant goes into the next slot, from that slot's list. Using a pick
  costs no ticket and no Zeny. It still follows the usual rules (slot order 4, 3, 2 and the refine needed).
- The counter and picks belong to your **account**, so tries on all your characters add up, and a pick can be used
  by any of them. You can save picks; they never expire.
- Resets and enchants made with a pick don't count toward the next pick.
- Slots with only one possible enchant don't offer a pick, since there is nothing to choose.

## Equipment and enchant lists

Click an item to see what each slot can roll.

{{ slot_enchanter("npc/miracle/jro_enchant.txt", "JRO Enchanter") }}
