# Daily Quests

**Location:** {{ npc_where("Daily Quest Manager") }}

Register once a day and complete **5 quests**, one after another. Each finished quest gives a random reward and
a server announcement. Only **one account per computer** can register each day.

{% set d = arrays("npc/miracle/daily_new.txt", "Daily Quest Manager") %}
## Quest types

Each quest is a random type and a random difficulty:

| Difficulty | Hunting | Collecting | Instance |
|---|---|---|---|
{% for name in d["DiffName$"] %}| {{ name }} | Kill {{ d.HuntNeed[loop.index0] }} | Bring {{ d.CollectNeed[loop.index0] }} | Clear any 5 instances |
{% endfor %}

- **Hunting** asks for one monster from the hunting list below.
- **Collecting** asks for one item from the list for that difficulty. The items are taken when you submit.
- **Instance** counts any instance you clear (party instances count for the whole party).

## Rewards

One random reward per finished quest:

| Reward | Amount |
|---|---|
{% for i in d.RewardItem %}| {{ item(i) }} | {{ d.RewardMin[loop.index0] }}{% if d.RewardMax[loop.index0] != d.RewardMin[loop.index0] %} ~ {{ d.RewardMax[loop.index0] }}{% endif %} |
{% endfor %}

## Monsters and items

<details class="abstract shop" markdown="1">
<summary>Hunting monsters <span class="count">{{ d.HuntMob|length }}</span></summary>

{% for m in d.HuntMob %}{{ mob_name(m) }}{% if not loop.last %}, {% endif %}{% endfor %}

</details>

<details class="abstract shop" markdown="1">
<summary>Collecting items: Easy (200 each)</summary>

{{ items_list(d.CollectItem_Easy) }}

</details>

<details class="abstract shop" markdown="1">
<summary>Collecting items: Medium (5 each)</summary>

{{ items_list(d.CollectItem_Medium) }}

</details>

<details class="abstract shop" markdown="1">
<summary>Collecting items: Hard (1 each)</summary>

{{ items_list(d.CollectItem_Hard) }}

</details>
