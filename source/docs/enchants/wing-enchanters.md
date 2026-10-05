# Wing Enchanters

**Location:** Quest Room. Fallen Angel Wing Enchanter at {{ npc_where("Fallen Angel Wing Enchanter") }},
Archangel Wing Enchanter at {{ npc_where("Archangel Wing Enchanter") }}.

| Enchanter | Item |
|---|---|
| Fallen Angel Wing Enchanter | {{ item(scalar("npc/miracle/Enchant_FAW.txt", "faw_itemid", "Fallen Angel Wing Enchanter")) }} |
| Archangel Wing Enchanter | {{ item(scalar("npc/miracle/Enchant_FAW.txt", "faw_itemid", "Archangel Wing Enchanter")) }} |

You must be **wearing** the wing. Choose a slot and an enchant type; the NPC adds a random enchant of that type.

| | |
|---|---|
| **Cost per try** | {{ scalar("npc/miracle/Enchant_FAW.txt", "enchant_Zeny", "Fallen Angel Wing Enchanter") }}× {{ item(6417) }} |
| **Success rate** | {{ scalar("npc/miracle/Enchant_FAW.txt", "success_rate", "Fallen Angel Wing Enchanter") }}% (the Silvervine is used up either way) |
| **Reset** | {{ scalar("npc/miracle/Enchant_FAW.txt", "enchant_reset_Zeny", "Fallen Angel Wing Enchanter") }}× {{ item(6417) }}, removes all enchants |

## Slots

| Slot | Needs refine |
|---|---|
| Slot 1 | +6 |
| Slot 2 | +7 |
| Slot 3 | +9 |

At **+9 or higher**, every enchant type also has a chance to roll its special (stronger) enchant.

## Enchant types

{% set a = arrays("npc/miracle/Enchant_FAW.txt", "Fallen Angel Wing Enchanter") %}
| Type | Possible enchants | Extra at +9 |
|---|---|---|
{% for t in a["enchant_type$"] %}| {{ t }} | {{ items_list(a["enchant_list_" ~ loop.index]) }} | {{ item(a.special_enchant[loop.index0]) }} |
{% endfor %}
