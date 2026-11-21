# Rune Stone: Imprint Gear

**Location:** {{ npc_where("Rune Stone") }}

The **Rune Stone** in the Quest Room has two options:

- **Open Rune UI** opens the Rune Tablet window, where you register rune fragments and turn on rune sets.
- **Imprint Gear** turns a piece of old gear into its **Printed** version. Printed items are one of the materials
  the Rune Tablet asks for when you register some runes.

## How imprinting works

1. Have the gear in your inventory and **10 {{ item(1001282) }}**.
2. Talk to the Rune Stone, pick **Imprint Gear**, then **Imprint Gear** again and choose the item from the list.
   Only gear from the table below shows up.
3. The gear is **destroyed** and you get its Printed item. Refine, cards, enchants and random options are lost,
   so use a spare copy.

Printed items cannot be traded, mailed, dropped or put in guild storage.

{% set r = arrays("npc/custom/rune_npc.txt", "Rune Stone") %}
<details class="abstract shop" markdown="1">
<summary>Gear that can be imprinted <span class="count">{{ r.BaseItem|length }}</span></summary>

| Gear | Becomes |
|---|---|
{% for b in r.BaseItem %}| {{ item(b) }} | {{ item(r.PrintItem[loop.index0]) }} |
{% endfor %}

</details>
