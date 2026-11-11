# Dim Glacier Ring Enchant

**NPC:** {{ npc("Gacha Enchanter", "moc_para01") }} · **Location:** {{ npc_where("Gacha Enchanter") }}

The Gacha Enchanter enchants the **Dim Glacier Ring of Resonance**, one ring for each 4th job, in the official
enchant window. Talk to the NPC, pick your ring, and the enchant window opens.

{% set f = "npc/miracle/dim_ring_enchant.txt" %}
{% set rings = indexed(f, "ring", "Gacha Enchanter") %}
{% set e = enchant_db(indexed(f, "table", "Gacha Enchanter")[0]) %}
{% set s3 = e.Slots | selectattr("Slot", "equalto", 3) | first %}
{% set s2 = e.Slots | selectattr("Slot", "equalto", 2) | first %}
{% set s1 = e.Slots | selectattr("Slot", "equalto", 1) | first %}

## How it works

The slots fill in order: **slot 4 first, then slot 3, then slot 2** (the enchant window counts them this way; the
tables further down use the database numbers 3, 2 and 1 for the same slots).

| Slot | What you get | Cost per try |
|---|---|---|
| **4** | One random enchant: Spell, ASPD or one of the Expert enchants | {{ enchant_cost(s3) }} |
| **3** | One random **Star of** enchant at Lv 1, which you can then **upgrade up to Lv 5** | {{ enchant_cost(s2) }} |
| **2** | The **Dim Crystal** of your job. You choose it, nothing is random | {{ enchant_cost(s1.PerfectEnchants[0]) }} |

- **Upgrades always succeed.** Each step from Lv 1 to Lv 5 costs more Zeny and more Meteorite Fragments, and the
  later steps also take {{ item(1000874) }}. The full cost of every step is in the table below.
- **Reset** removes all enchants from the ring: {{ enchant_cost(e.Reset) }}.
- Take the ring off first. The NPC only sees rings in your inventory.

## The rings

Every ring has its own enchant table. They all cost the same; only the Dim Crystal in slot 2 is different for each
job. Click a ring's enchant table to see its exact enchants in the Database.

| Ring | Enchant table |
|---|---|
{% for r in rings %}| {{ item(r) }} | [Enchant system {{ indexed(f, "table", "Gacha Enchanter")[loop.index0] }}](../db/enchants.md#E{{ indexed(f, "table", "Gacha Enchanter")[loop.index0] }}) |
{% endfor %}

## Example: {{ item_name(rings[0]) }}

{{ item_enchant(indexed(f, "table", "Gacha Enchanter")[0]) }}
