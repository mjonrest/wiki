# World Boss

**Location:** {{ npc_where("World Boss") }}

Every monster killed on the server adds **1 soul** to a shared counter. When it reaches
**75,000 souls**, any player of **Base Level 275** can summon the World Boss at the World Boss NPC.

1. The boss appears on a **random field map**, guarded by 7 guardians. Each living guardian gives the boss one
   of its skills. Kill guardians to strip them away.
2. The gate opens 5 minutes after the summon. Enter through the World Boss NPC (maximum 100 players,
   [one character per computer](../guide/fair-play.md)).
3. The boss leaves after **1 hour** if it is not defeated.

## Rewards

Rewards are sent **by mail** to everyone who dealt more than **100,000 damage**.

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
