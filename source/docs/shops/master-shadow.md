# Master Shadow

**Location:** {{ npc_where("Master Shadow") }} · Quest Room

{% set f = "npc/miracle/master_shadow.txt" %}
{% set reward = scalar(f, "RewardItem", "Master Shadow") %}
Recycle old Shadow gear into {{ item(reward) }}, then exchange essences and +10 Shadows for Master Shadows.

## Recycling

| Shadow refine | You get |
|---|---|
| +0 ~ +9 | {{ scalar(f, "NormalMin", "Master Shadow") }}~{{ scalar(f, "NormalMax", "Master Shadow") }} {{ item_name(reward) }} |
| +10 | {{ scalar(f, "BonusMin", "Master Shadow") }}~{{ scalar(f, "BonusMax", "Master Shadow") }} {{ item_name(reward) }} |

**Recycle All** recycles every +0 to +9 Shadow in your inventory at once and skips +10 ones.

<details class="abstract shop" markdown="1">
<summary>Recyclable Shadows</summary>

{{ items_table(arrays(f, "Master Shadow").RecycleItem, "Shadow") }}

</details>

## Exchange

{{ shop("Master_01", "Master Shadows") }}
{{ shop("Master_02", "Master Shadow Boxes") }}

## 4th Skill Master

Skill shadows for each 4th job.

{% for job in ["Dragon_Knight", "Meister", "Shadow_Cross", "Arch_Mage", "Cardinal", "Windhawk", "Imperial_Guard", "Biolo", "Abyss_Chaser", "Elemental_Master", "Inquisitor", "Troubadour_Trouvere", "Sky_Emperor", "Soul_Ascetic", "Shinkiro_Shiranui", "Night_Watch", "Hyper_Novice", "Spirit_Handler", "Alitea"] %}
{{ shop("Master_" ~ job, job | replace("_", " ")) }}
{% endfor %}
