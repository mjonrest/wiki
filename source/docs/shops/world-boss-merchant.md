# World Boss Merchant

**Location:** {{ npc_where("World Boss Merchant") }} · Quest Room

Everything here, including the [MVP Soul Costume Gacha](#mvp-soul-costume-gacha), is paid with **{{ item_name(30007) }}**, which drops from the [World Boss](../content/world-boss.md).
You can also buy Souls with Cash Points through `@donate` and get them from Daily Quests and the Card Trader.

## Box Pack

{{ shop("Skill01", "1st Skill Pack") }}
{{ shop("Skill02", "2nd Skill Pack") }}
{{ shop("Skill03", "3rd Skill Pack") }}
{{ shop("Job01", "Job Pack") }}

## Enchant Stones

{{ shop("WB_barter_stone_top", "Top headgear stones") }}
{{ shop("WB_barter_stone_mid", "Middle headgear stones") }}
{{ shop("WB_barter_stone_low", "Lower headgear stones") }}
{{ shop("WB_barter_stone_garment", "Garment stones") }}
{{ shop("WB_barter_stone_dual", "Dual and effect stones") }}
{{ shop("wb7#1", "4th garment stones") }}
{{ shop("wb7#2", "New II stones") }}

## Shadows Exchange

{{ shop("wb6#1", "Shadows Exchange") }}

## Shadows Partial

=== "Collection 1"

    {{ shop("wb1#1", "Page 1", collapsed=True) | indent(4) }}
    {{ shop("wb1#2", "Page 2", collapsed=True) | indent(4) }}
    {{ shop("wb1#3", "Page 3", collapsed=True) | indent(4) }}
    {{ shop("wb1#4", "Page 4", collapsed=True) | indent(4) }}

=== "Collection 2"

{% for p in range(1, 10) %}
    {{ shop("wb2#" ~ p, "Page " ~ p, collapsed=True) | indent(4) }}
{% endfor %}

=== "Shadow Skills"

{% for p in range(1, 8) %}
    {{ shop("wb4#" ~ p, "Page " ~ p, collapsed=True) | indent(4) }}
{% endfor %}

=== "Shadow Job"

{% for p in range(1, 4) %}
    {{ shop("wb5#" ~ p, "Page " ~ p, collapsed=True) | indent(4) }}
{% endfor %}

## Fragment

{{ shop("MvpFrag", "MVP Fragments", collapsed=False) }}

## MVP Soul Costume Gacha

{% set g = "npc/miracle/gacha_mvpsoul.txt" %}
{% set cost = scalar(g, "cost", "MvpSoulGacha") %}
{% set p = arrays(g, "MvpSoulGacha") %}
Pick **MVP Soul Costume Gacha** in the merchant's menu. Every pull gives **one costume headgear**: the slot is fully
random (**Upper, Mid or Lower, 1/3 each**), then one costume from that slot's list, all with the same chance.

| | |
|---|---|
| **1 pull** | {{ "{:,}".format(cost) }} {{ item_name(30007) }} |
| **10 pulls** | {{ "{:,}".format(cost * 10) }} {{ item_name(30007) }} |
| **Prizes** | Not bound: you can trade, vend and sell them |
| **Inventory** | Keep one free slot per pull. If your inventory is full or too heavy, no Souls are used |

**View Rates** in the menu shows how many costumes each slot has.

<details class="abstract shop" markdown="1">
<summary>Costume prizes <span class="count">{{ p.pool_raw_top|length + p.pool_raw_mid|length + p.pool_raw_low|length }} items</span></summary>

**Upper:** {{ items_list(p.pool_raw_top) }}

**Mid:** {{ items_list(p.pool_raw_mid) }}

**Lower:** {{ items_list(p.pool_raw_low) }}

</details>
