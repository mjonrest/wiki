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

{% set wb = "npc/miracle/wb_new(non-regen).txt" %}
{% set per = scalar(wb, "soul_per_dmg", "World Boss") %}
{% set w = arrays(wb, "World Boss") %}
Rewards are sent **by mail** when the boss dies, and they depend on **how much damage you dealt yourself**:

- You get **{{ scalar(wb, "soul_amount", "World Boss") }} {{ item(scalar(wb, "soul_item", "World Boss")) }}** for every
  **{{ "{:,}".format(per) }} damage**, up to **{{ "{:,}".format(scalar(wb, "soul_cap", "World Boss")) }} souls**.
  Less than {{ "{:,}".format(per) }} damage gives no reward.
- **Party bonus:** +{{ scalar(wb, "party_bonus_per", "World Boss") }}% of your own souls for every other party member who
  also earned a reward (up to +{{ scalar(wb, "party_bonus_max", "World Boss") }}%, a full party). The bonus is based on
  your own damage only, so party members who did not fight add nothing.
- Only damage counts: healing or buffing other players does not earn souls, and there is no extra prize for the top
  damage dealer.
- You must still be **on the boss map** when it dies, and not idle for more than
  **{{ scalar(wb, "idle_limit", "World Boss") }} seconds** (time spent waiting before the gate opens does not count).
- Only **one reward per computer**: if several of your characters hit the boss, only the one with the most damage
  is rewarded.

Every rewarded player also has a chance at these extra items:

| Reward | Amount | Chance |
|---|---|---|
{% for i in w.reward_item %}| {{ item(i) }} | {{ w.reward_min[loop.index0] }} ~ {{ w.reward_max[loop.index0] }} | {{ w.reward_rate[loop.index0] }}% |
{% endfor %}

Having {{ item(30034) }} active adds **{{ scalar(wb, "rental_bonus_extra", "World Boss") }}** extra {{ item_name(30007) }} to your reward.

Spend MVP Souls at the [World Boss Merchant](../shops/world-boss-merchant.md).

## Possible maps

{% set maps = arrays("npc/miracle/wb_new(non-regen).txt", "World Boss")["wb_maps$"] %}
{% for m in maps %}`{{ m }}`{% if not loop.last %}, {% endif %}{% endfor %}
