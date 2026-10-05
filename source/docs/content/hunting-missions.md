# Hunting Missions

**Location:** {{ npc_where("Hunting Missions") }} · Quest Room

Take a mission and you are told to hunt one random monster **{{ arrays("npc/miracle/Hunting_Mission.txt", "Hunting Missions")["Count"]|join("~") }} times**.
Report back when you are done.

| | |
|---|---|
| **Reward** | **7 Mission Points** plus Zeny (kills × monster level × 150) |
| **Cooldown** | None, take the next mission right away |
| **Party kills** | Count for party members who also have a mission, on the same screen |
| **Abandon** | Free, no penalty |
| **Limit** | One active mission per account (not one per character) |

Mission Points are shared by all characters on your account. The NPC also shows the **top 5 hunters**.

## Mission Shop

Choose **Mission Shop** in the NPC menu.

{{ shop("missionshop#1", collapsed=False) }}

The {{ item_name(30062) }} gives one random accessory, see [Gacha Machines](gacha.md#exclusive-accessory-box).
Coins can be changed back into Mission Points at the [Coin Exchanger](../shops/coin-exchanger.md).
