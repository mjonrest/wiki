# Hell Raid

**Location:** {{ npc_where("Hell Raid Guardian") }}

A 10-round party raid in `ordeal_3-1`.

## Schedule

Registration opens **every 3 hours** (00:00, 03:00, 06:00, 09:00, 12:00, 15:00, 18:00, 21:00) for **5 minutes**.
Talk to the Hell Raid Guardian to enter. You cannot join once the raid has started.

## How a round works

1. **70 monsters** spawn around the arena.
2. When all are dead, a **round boss** appears 10 seconds later.
3. Killing the boss mails every player on the map the round reward.
4. Talk to the **Hell Raid Guide** within 5 minutes and donate **10 Event Points** together
   (each account can donate once per round) to start the next round. If nobody does, the raid ends.

The raid also ends after 1 hour or when everyone has left.

## Rules

- No {{ item_name(7621) }}, commands or cash shop
- No teleport, warp, branches or Ice Wall; nothing is lost on death
- Bosses have extra HP and damage and only take 1% of your damage
- [One character per computer](../guide/fair-play.md)

## Rounds and rewards

{% set h = arrays("npc/miracle/hell_raid.txt", "Hell Raid Guardian") %}
| Round | Boss | Reward |
|---|---|---|
{% for r in range(10) %}| {{ r + 1 }} | {{ mob_name(h.BossID[r]) }} | {{ h.RewardAmount[r] }}× {{ item(30056) }} |
{% endfor %}

## Hell Scroll

Opening a {{ item(30056) }} gives one of:

| Chance | Reward |
|---|---|
| 0.01% | {{ items_list(array_seq("npc/miracle/hell_raid.txt", "F_GachaReward", "rare1")[0]) }} |
| 0.09% | {{ items_list(array_seq("npc/miracle/hell_raid.txt", "F_GachaReward", "rare2")[0]) }} |
| 0.4% | {{ items_list(array_seq("npc/miracle/hell_raid.txt", "F_GachaReward", "rare3")[0]) }} |
| Otherwise | 5~30× {{ item(30047) }} |

Rare results are announced to the server.
