# Mora Crafters (Army Padding, Guardian Pendant, Loki's Muffler)

<!-- npcs: Master Tailor; Pendant Crafter; Bulberry Westhood -->

Three crafters in north Mora each add three random enchants to one specific item for Mora Coins. They share the same enchant table; only the item and what happens on failure differ.

| NPC | Item | Where | On failure |
|---|---|---|---|
| Master Tailor | {{ item(15024) }} | `/navi mora 105/176` | The padding is **destroyed** |
| Pendant Crafter | {{ item(2858) }} | `/navi mora 123/177` | You get a plain pendant back (enchants removed) |
| Bulberry Westhood | {{ item(2568) }} | `/navi mora 134/166` | You get a plain muffler back (enchants removed) |

## How it works

- **Cost:** 5 {{ item(6380) }} per attempt, plus the item in your **inventory**.
- The NPC works on the item whether or not it was enchanted before. Any old enchants are replaced by the new roll (or wiped on failure).
- You always get a **brand-new copy** back: refine is reset to +0.
- Each attempt fills the 2nd, 3rd and 4th slots at once.

!!! tip
    The Master Tailor also sells {{ item(15024) }} for 1 {{ item(6380) }}. He offers this when you have at least one Mora Coin but not the full 5 coins and a padding.

!!! tip
    If you carry several copies, the NPC takes an unrefined, unenchanted copy first. Put any copy you want to keep in storage before you start.

## Chances

| Result | Chance |
|---|---|
| Normal enchant (see below) | 69.35% |
| Jackpot: {{ item(4761) }} + {{ item(4720) }} + {{ item(4700) }} | 0.24% |
| One of the 9 other jackpot sets below | 0.04% each |
| Failure | 30.01% |

### Normal enchant

Each slot rolls independently; every option in a column has the same chance.

| 2nd slot (12.5% each) | 3rd slot (1 in 6 each) | 4th slot (1 in 6 each) |
|---|---|---|
| {{ item(4766) }} | {{ item(4720) }} | {{ item(4700) }} |
| {{ item(4767) }} | {{ item(4721) }} | {{ item(4701) }} |
| {{ item(4764) }} | {{ item(4710) }} | {{ item(4730) }} |
| {{ item(4765) }} | {{ item(4711) }} | {{ item(4731) }} |
| {{ item(4762) }} | {{ item(4750) }} | {{ item(4740) }} |
| {{ item(4763) }} | {{ item(4751) }} | {{ item(4741) }} |
| {{ item(4760) }} |  |  |
| {{ item(4761) }} |  |  |

### Jackpot sets

| 2nd slot | 3rd slot | 4th slot | Chance |
|---|---|---|---|
| {{ item(4761) }} | {{ item(4720) }} | {{ item(4700) }} | 0.24% |
| {{ item(4761) }} | {{ item(4712) }} | {{ item(4712) }} | 0.04% |
| {{ item(4765) }} | {{ item(4732) }} | {{ item(4732) }} | 0.04% |
| {{ item(4763) }} | {{ item(4752) }} | {{ item(4753) }} | 0.04% |
| {{ item(4763) }} | {{ item(4742) }} | {{ item(4742) }} | 0.04% |
| {{ item(4763) }} | {{ item(4722) }} | {{ item(4722) }} | 0.04% |
| {{ item(4742) }} | {{ item(4742) }} | {{ item(4742) }} | 0.04% |
| {{ item(4761) }} | {{ item(4722) }} | {{ item(4722) }} | 0.04% |
| {{ item(4767) }} | {{ item(4702) }} | {{ item(4702) }} | 0.04% |
| {{ item(4763) }} | {{ item(4732) }} | {{ item(4732) }} | 0.04% |
