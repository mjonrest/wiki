# World Boss Merchant

**Location:** {{ npc_where("World Boss Merchant") }} · Quest Room

Everything here is paid with **{{ item_name(30007) }}**, which drops from the [World Boss](../content/world-boss.md).
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
