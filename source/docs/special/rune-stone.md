# Rune Stone: Imprint Gear & Upgrades

**Location:** {{ npc_where("Rune Stone") }}

The **Rune Stone** in the Quest Room has three options:

- **Open Rune UI** opens the Rune Tablet window, where you register rune fragments and turn on rune sets.
- **Imprint Gear** turns a piece of old gear into its **Printed** version. Printed items are one of the materials
  the Rune Tablet asks for when you register some runes.
- **Upgrade Rune Set** raises the level of a rune set you have turned on, up to **+15**. See
  [Upgrading rune sets](#upgrading-rune-sets).

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


## Upgrading rune sets

Our game client's Rune Tablet window has no Upgrade page, so upgrades are done at the Rune Stone instead.

1. Turn the set on in the Rune UI first. Only active sets are listed.
2. Talk to the Rune Stone, pick **Upgrade Rune Set** and choose the set. The list shows each set's current level
   and which one you have equipped.
3. The NPC shows the **success chance** for the next level and the **materials** it costs, with how many you have.
   Pick **Upgrade** to try. You can keep upgrading from the same window.

- Every try uses the materials, whether it works or not.
- **A failure never lowers the level.** Instead, each failed try raises the chance of the next one, until it
  succeeds. The bonus resets after a success.
- Materials and chances are different for every set and level, and match the official Rune Tablet. Higher levels
  cost more and have lower base chances.
- Many set effects grow with the set level (some only every few levels), so a set at +0 can show only a small
  part of its effect.
