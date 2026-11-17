# Abyss Lake / Violent Dragon Armor-LT Enchant

**NPC:** {{ npc("Gacha Enchanter", "moc_para01") }} · **Location:** {{ npc_where("Gacha Enchanter") }}

The Gacha Enchanter enchants {{ item(450358) }} and {{ item(450357) }} in the official enchant window, with the
iRO enchant list. Talk to the NPC, choose **Abyss Lake / Violent Dragon Armor-LT**, pick your armor, and the
enchant window opens. Both armors are sold by the {{ npc("Instance Point Merchant", "moc_para01") }}.

{% set e = enchant_db(219) %}
{% set s3 = e.Slots | selectattr("Slot", "equalto", 3) | first %}
{% set s2 = e.Slots | selectattr("Slot", "equalto", 2) | first %}
{% set s1 = e.Slots | selectattr("Slot", "equalto", 1) | first %}

## How it works

The slots fill in order: **slot 4 first, then slot 3, then slot 2** (the tables further down use the database
numbers 3, 2 and 1 for the same slots).

| Slot | What you get | Cost per try |
|---|---|---|
| **4** | STR / AGI / VIT / INT / DEX / LUK +2~5, or a Rune (Lv 1) stat enchant | {{ enchant_cost(s3) }} |
| **3** | A **Nebula** enchant Lv 1~3 (Lv 1 is the most common) | {{ enchant_cost(s2) }} |
| **2** | A **Star Cluster** enchant at Lv 1, which you can **upgrade up to Lv 3** | {{ enchant_cost(s1) }} |

- **Upgrades always succeed.** The cost of each step is in the table below.
- **Reset** removes all enchants: {{ enchant_cost(e.Reset) }}. It works 80% of the time, and the armor is never
  destroyed.
- Take the armor off first. The NPC only sees armors in your inventory.

{{ item_enchant(219) }}
