# Honor Token Enhancers (Dylan and Hogar)

<!-- npcs: Dylan; Hogar -->

Two black-market craftsmen add stat enchants to robes and accessories in exchange for honor tokens.
**Dylan** works for {{ item(6919) }} in the Prontera prison, and **Hogar** works for {{ item(25155) }}
in the rebel hideout.

| NPC | Items | Currency | Where |
|---|---|---|---|
| Dylan | {{ item(15146) }}, {{ item(15147) }}, {{ item(28356) }} | {{ item(6919) }} | `/navi prt_pri00 61/136` |
| Hogar | {{ item(15163) }}, {{ item(15164) }}, {{ item(28425) }}, {{ item(28426) }} | {{ item(25155) }} | `/navi rebel_in 90/40` |

Both need at least 1,000 free weight and room for one more item. The first time you talk to each of them
you hear his story, and then you can trade.

## How it works

- **Wear** the item. Robes go in the armor slot. The badge and the rings must be worn in the
  **left** accessory slot.
- Each enhancement adds one random enchant: slot 4 first, then slot 3. After two enhancements the item is
  full.
- The item is taken off and comes back in your inventory, so put it on again for the next try.
- Robes keep their refine and card. Rings keep their card.
- A reset only works on a **full** item (both slots enchanted).

## Dylan

| Service | Cost | Result |
|---|---|---|
| Enhance Robe | 20 {{ item(6919) }} | One random rune (table below) |
| Enhance Badge | 5 {{ item(6919) }} | One random stat bonus (table below) |
| Reset Enhanced Robe Stats | 10 {{ item(6919) }} | Removes both runes. Always succeeds. |
| Reset Enhanced Badge Stats | 10 {{ item(6919) }} | 79% success. On failure the **badge is destroyed** |

### Robe runes

| Stat | Lv 1 | Lv 2 | Lv 3 |
|---|---|---|---|
| STR | {{ item(4994) }} 8.64% | {{ item(4995) }} 5.93% | {{ item(4996) }} 2.08% |
| AGI | {{ item(4997) }} 8.64% | {{ item(4998) }} 5.93% | {{ item(4999) }} 2.08% |
| INT | {{ item(29000) }} 8.64% | {{ item(29001) }} 5.93% | {{ item(29002) }} 2.08% |
| DEX | {{ item(29003) }} 8.64% | {{ item(29004) }} 5.93% | {{ item(29005) }} 2.08% |
| VIT | {{ item(29009) }} 8.64% | {{ item(29010) }} 5.93% | {{ item(29011) }} 2.08% |
| LUK | {{ item(29006) }} 8.64% | {{ item(29007) }} 5.93% | {{ item(29008) }} 2.08% |

### Badge bonuses

| Stat | +1 | +2 | +3 | +4 | +5 |
|---|---|---|---|---|---|
| STR | {{ item(4700) }} 13.49% | {{ item(4701) }} 2.7% | {{ item(4702) }} 0.45% | {{ item(4703) }} 0.018% | {{ item(4704) }} 0.0045% |
| AGI | {{ item(4730) }} 13.49% | {{ item(4731) }} 2.7% | {{ item(4732) }} 0.45% | {{ item(4733) }} 0.018% | {{ item(4734) }} 0.0045% |
| VIT | {{ item(4740) }} 13.49% | {{ item(4741) }} 2.7% | {{ item(4742) }} 0.45% | {{ item(4743) }} 0.018% | {{ item(4744) }} 0.0045% |
| INT | {{ item(4710) }} 13.49% | {{ item(4711) }} 2.7% | {{ item(4712) }} 0.45% | {{ item(4713) }} 0.018% | {{ item(4714) }} 0.0045% |
| DEX | {{ item(4720) }} 13.49% | {{ item(4721) }} 2.7% | {{ item(4722) }} 0.45% | {{ item(4723) }} 0.018% | {{ item(4724) }} 0.0045% |
| LUK | {{ item(4750) }} 13.49% | {{ item(4751) }} 2.7% | {{ item(4752) }} 0.45% | {{ item(4753) }} 0.018% | {{ item(4754) }} 0.0045% |

!!! warning "Known issue: an enhancement can give nothing"
    A tiny share of rolls gives no enchant at all: 0.1% for the robe and 0.0045% for the badge. The tokens
    are still used and the slot stays empty, so you can simply enhance again.

### Badge reset

Dylan says the reset works 80% of the time. It actually works **79%** of the time. On success you get a
clean {{ item(28356) }}. On failure the badge is destroyed and you get {{ item(6920) }} instead:

| Rune Magic Powder | Chance |
|---|---|
| 9 | 60% |
| 10 | 20% |
| 11 | 6% |
| 12 | 6% |
| 13 | 5% |
| 14 | 2% |
| 15 | 1% |

## Hogar

| Service | Cost | Result |
|---|---|---|
| Upgrade my robe | 20 {{ item(25155) }} | One random rune: any of the 18 runes above, **5.56% each** |
| Upgrade my ring | 5 {{ item(25155) }} | One random stat bonus, **8.33% each** (list below) |
| Initialize robe | 10 {{ item(25155) }} | Removes both runes. Always succeeds. |
| Initialize ring | 10 {{ item(25155) }} | 80% success. On failure the **ring is destroyed** and you get nothing |

**Ring bonuses** (8.33% each): {{ item(4700) }}, {{ item(4730) }}, {{ item(4740) }}, {{ item(4710) }},
{{ item(4720) }}, {{ item(4750) }}, {{ item(4701) }}, {{ item(4731) }}, {{ item(4741) }}, {{ item(4711) }},
{{ item(4721) }}, {{ item(4751) }}
