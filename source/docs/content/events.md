# Automatic Events

Events start on their own every 30 minutes. When one opens, the server announces it and you have **1 minute**
to type **`@eventjoin`** and pick it. `@eventjoin` also shows your current Event Points.

Winners earn **Event Points**, spent at the [Event Shop](../shops/event-shop.md), the
[Mining Zone](mining.md) tool shop, [Hell Raid](hell-raid.md) and the [Antiquity Gacha](gacha.md).

## Daily schedule (server time)

{{ event_schedule() }}

## The events

| Event | How to win | Prize |
|---|---|---|
| **Bombring** | Survive 5 rounds of exploding Bombrings, 30 seconds each, in `quiz_02`. | 20 Event Points to every survivor |
| **Dice** | Stand in one of 4 boxes. A 4-sided die is thrown and the other boxes are kicked out. Last box standing wins. | 20 Event Points |
| **Poring Catcher** | Dozens of Porings with fake names spawn. Kill the one named exactly **Poring**. Kill a wrong one and you are out. | 20 Event Points |
| **Poring Hunter** | Score the most points before time runs out: Poring +1, Drops +5, Poporing -10. | 20 Event Points |
| **Disguise** | The **Disguise Event** NPC in the Quest Room ({{ npc_where("Disguise Event") }}) turns into a monster. Be the first to type its name in chat. | 4 Event Points per round |
| **Monster Battle** | Two monsters fight in `poring_w02`. Bet 20 Event Points on one at the **MVP Bet Girl**. | 100 Event Points if your monster wins |

## Weekend double rates

Every **Friday 00:00 to Monday 00:00**, Base EXP, Job EXP and drop rates (including cards) are **doubled**.

## Battle Rumble

A GM-run event at the **Novice Magic Tournament Gate** (`new_1-1`). Only **Base Level 99 Novices** with an
**empty inventory** may enter. You get random rental gear for 30 minutes, then fight to be the last one standing.

{% set br = arrays("npc/miracle/magic_pvp.txt", "Novice Magic Tournament Gate") %}
On entry you get one random costume from each of the three lists below, plus a fixed set of gear
({{ items_list([24693, 24694, 24695, 24696, 24697, 1639]) }}). All of it is rented for 30 minutes.

<details class="abstract shop" markdown="1">
<summary>Random costumes on entry</summary>

**List 1:** {{ items_list(br.item_list1|unique|list) }}

**List 2:** {{ items_list(br.item_list2) }}

**List 3:** {{ items_list(br.item_list3) }}

</details>

The **Touch Me!** spots around the arena give one random consumable, rented for 1 minute. Each spot comes back
2 minutes after someone touches it.

<details class="abstract shop" markdown="1">
<summary>Touch Me! items</summary>

{{ items_list(arrays("npc/miracle/magic_pvp.txt", "Touch Me!").item_list) }}

</details>
