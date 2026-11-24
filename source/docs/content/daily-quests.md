# Daily Quests

**Location:** {{ npc_where("Daily Quest Manager") }}

Register once a day and complete **5 quests**, one after another. Each finished quest gives a random reward and
a server announcement. Only **one account per computer** can register each day.

{% set d = arrays("npc/miracle/daily_new.txt", "Daily Quest Manager") %}
## Quest types

Each quest is a random type and a random difficulty:

| Difficulty | Hunting | Collecting | Instance |
|---|---|---|---|
{% for name in d["DiffName$"] %}| {{ name }} | Kill {{ d.HuntNeed[loop.index0] }} | {% if loop.index0 == 1 %}Bring {{ d.CollectNeed[1] }} each of 2 different Monster Souls{% else %}Bring {{ d.CollectNeed[loop.index0] }}{% endif %} | Clear any 5 instances |
{% endfor %}

- **Hunting** asks for one monster from the hunting list below.
- **Collecting** asks for one item from the list for that difficulty. The items are taken when you submit.
  **Medium** asks for **two different Monster Souls** instead. Each soul drops (10%) only from its own monster,
  on the maps where that monster spawns: open a soul below to see where it drops, or type [`@souls`](../guide/commands.md#souls)
  ({{ scalar("npc/miracle/soul_tracker.txt", "soul_cost", "SoulTracker") }} Event Points) to see which of its monsters
  are alive and when the dead ones respawn.
- **Instance** counts any instance you clear (party instances count for the whole party).

## Soul guarantee

{% set dn = "npc/miracle/daily_new.txt" %}
While your current quest is a **Medium** soul quest, your **{{ scalar(dn, "SoulPityKills", "Daily Quest Manager") }}rd kill**
of one of its soul monsters, on that soul's drop maps, always gives you the soul if you have none of it yet.
On the kills before that, a message over your head shows how many kills are left.

- It works **once per soul per quest**, so each Medium quest can guarantee both of its souls, even if you get the
  same soul again in a later quest.
- Guaranteed souls are **account bound**: they cannot be traded, vended or sold. Normal drops are not bound.
- If you already carry that soul, no extra one is given.

## Changing a quest

You can **change your current quest {{ scalar(dn, "FreeRerolls", "Daily Quest Manager") }} times a day for free**
(per account). Pick **Change Quest** at the Daily Quest Manager and you get a different random quest of a random type
and difficulty. Progress on the old quest is lost. The option is gone once you have used your free changes for the day.

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
<summary>Collecting items: Easy ({{ d.CollectNeed[0] }} each)</summary>

{{ items_list(d.CollectItem_Easy) }}

</details>

<details class="abstract shop" markdown="1">
<summary>Collecting items: Medium (Monster Souls, 1 each of 2)</summary>

{{ items_list(d.CollectItem_Medium) }}

</details>

<details class="abstract shop" markdown="1">
<summary>Collecting items: Hard ({{ d.CollectNeed[2] }} each)</summary>

{{ items_list(d.CollectItem_Hard) }}

</details>
