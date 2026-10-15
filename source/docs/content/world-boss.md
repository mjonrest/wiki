# World Boss

**Location:** {{ npc_where("World Boss") }}

Every monster killed on the server adds **1 soul** to a shared counter. When it reaches
**75,000 souls**, any player of **Base Level 275** can summon the World Boss at the World Boss NPC.

1. The boss appears on a **random field map**, guarded by **8 guardians**, one for each of its 8 skills.
   Each living guardian lets the boss use one skill. Kill guardians to strip them away.
2. The gate opens 5 minutes after the summon. Enter through the World Boss NPC (maximum 100 players,
   [one character per computer](../guide/fair-play.md)).
3. The boss leaves after **1 hour** if it is not defeated.

## The fight

- The boss takes **50% less damage**. It has high DEF and MDEF, so physical and magic builds are cut about the same.
- Two of its skills punish both kinds of damage: **Reflect Shield** sends back 25% of melee damage, and
  **Magic Mirror** has a 20% chance to bounce a spell back. Kill their guardians to turn them off.
- It uses a skill every 3 seconds and hits harder than its base stats. Half the time it goes after one of the
  **top 5 damage dealers** still on the map instead of the closest player, so the main damage dealers need support.
- At **50% HP** it becomes **Enraged**: more damage and skills come faster.
- At **25% HP** it goes **Berserk**: even more damage and skills twice as fast.

## Rewards

Rewards are sent **by mail** to **everyone who hit the boss** and is still on the boss map when it dies.
Only **one reward per computer**: if several of your characters hit the boss, only the one with the most damage
is rewarded.

{% set w = arrays("npc/miracle/wb_new(non-regen).txt", "World Boss") %}
| Reward | Amount | Chance |
|---|---|---|
{% for i in w.default_item %}| {{ item(i) }} | {{ w.default_min[loop.index0] }} ~ {{ w.default_max[loop.index0] }} | Always |
{% endfor %}{% for i in w.reward_item %}| {{ item(i) }} | {{ w.reward_min[loop.index0] }} ~ {{ w.reward_max[loop.index0] }} | {{ w.reward_rate[loop.index0] }}% |
{% endfor %}

The **top damage dealer** also gets {% for i in w.killer_item %}{{ w.killer_min[loop.index0] }}~{{ w.killer_max[loop.index0] }} {{ item(i) }}{% endfor %}.
Having {{ item(30034) }} active adds **50** extra {{ item_name(30007) }} to your reward.

Spend MVP Souls at the [World Boss Merchant](../shops/world-boss-merchant.md).

## Possible maps

{% set maps = arrays("npc/miracle/wb_new(non-regen).txt", "World Boss")["wb_maps$"] %}
{% for m in maps %}`{{ m }}`{% if not loop.last %}, {% endif %}{% endfor %}
