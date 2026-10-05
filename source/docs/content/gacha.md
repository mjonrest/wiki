# Gacha Machines

## Gacha Machine (Activity Points)

**Location:** {{ npc_where("Gacha Machine") }} · Quest Room

Paid with **Activity Points**. You earn **1 Activity Point per minute** while you are actively playing.
You get nothing while idle, standing in the same spot, vending or using a buying store, and only one character
per computer earns points. Type `@activity` to hide or show the point messages.

You can play **10 times a day** per account.

| Machine | Cost | Win chance | Prize |
|---|---|---|---|
| Costume Headgear | 10 Activity Points | 10% | A random top, mid or lower costume |
| Costume Garment | 30 Activity Points | 5% | A random costume garment |

Prizes are account bound and announced to the server.

{% set h = arrays("npc/miracle/gacha_costume.txt", "Claw_Machine_Gacha") %}
<details class="abstract shop" markdown="1">
<summary>Costume headgear prizes <span class="count">{{ h.top|length + h.mid|length + h.low|length }} items</span></summary>

**Top:** {{ items_list(h.top) }}

**Mid:** {{ items_list(h.mid) }}

**Lower:** {{ items_list(h.low) }}

</details>

<details class="abstract shop" markdown="1">
<summary>Costume garment prizes</summary>

{{ items_list(arrays("npc/miracle/gacha_costume.txt", "Garment_Gacha").garments) }}

</details>

## Zeny Gacha Machine

**Location:** {{ npc_where("Zeny Gacha Machine") }} · Quest Room

**{{ fmt(scalar("npc/miracle/gacha_zeny.txt", "Cost")) }} Zeny** per roll, in packs of 1, 50 or 100.
Every roll gives one refine or grade material.

{% set z = array_seq("npc/miracle/gacha_zeny.txt", "Zeny Gacha Machine", "pool") %}
| Chance | Possible items |
|---|---|
| 2% | {{ items_list(z[0]) }} |
| 1% | {{ items_list(z[1]) }} |
| 2% | {{ items_list(z[2]) }} |
| 95% | {{ items_list(z[3]) }} |

## Antiquity Gacha

**Location:** {{ npc_where("Antiquity Gacha") }} · Quest Room

Each roll costs **1,000 Zeny** plus either **2 Mission Points** or **1 Event Point**.

{% set a = arrays("npc/miracle/script_oinit.txt", "Antiquity Gacha") %}
| Chance | Possible items |
|---|---|
| 1% (Ultra Rare) | {{ items_list(a.UltraRare) }} |
| 10% (Rare) | {{ items_list(a.Rare) }} |
| 89% (Common) | {{ items_list(a.Common) }} |

## Card albums

{% set c = array_seq("npc/miracle/jro.txt", "F_GetJROCard", "Pool") %}
{% set cm = array_seq("npc/miracle/jro.txt", "F_GetJROCardM", "Pool") %}
Opening an album may give a card. Most of the time it gives nothing.

| Tier | {{ item(616) }} | {{ item(12246) }} |
|---|---|---|
| Ultra Rare | 0.25% | 0.5% |
| Rare | 0.5% | 1% |
| Common | 1.5% | 3% |

<details class="abstract shop" markdown="1">
<summary>Album cards</summary>

**Ultra Rare:** {{ items_list(c[0]) }}

**Rare:** {{ items_list(c[1]) }}

**Common:** {{ items_list(c[2]) }}

</details>

Buy albums at the [Card Trader](../shops/card-trader.md).

## Exclusive Accessory Box

{% set x = arrays("npc/miracle/script_oinit.txt", "ex_acc") %}
{{ item(30062) }} (from the [Mission Shop](hunting-missions.md#mission-shop)) gives one accessory:

| Chance | Possible items |
|---|---|
| 5% (Ultra Rare) | {{ items_list(x.UltraRare) }} |
| 25% (Rare) | {{ items_list(x.Rare) }} |
| 70% (Common) | {{ items_list(x.Common) }} |
