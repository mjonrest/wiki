# El Dicastes Enchanters

<!-- npcs: Jalapeno; Brare; Mancho; Kareka -->

Three cats outside El Dicastes and Kareka inside the city each upgrade one Sapha item in three steps for
{{ item(6304) }}.

| NPC | Item | Where |
|---|---|---|
| Jalapeno | {{ item(2463) }} | `/navi dic_fild01 240/198` |
| Brare | {{ item(2843) }} | `/navi dic_fild01 251/183` |
| Mancho | {{ item(2564) }} | `/navi dic_fild01 259/172` |
| Kareka | {{ item(2844) }} | `/navi dic_in01 353/37` |

You need at least 1 {{ item(6304) }} to talk business, at least 1,000 free weight and room for one more item.
The item only has to be in your **inventory**.

## How it works

Each upgrade step adds one random enchant. The steps always go in the same order:

| Step | Cost | Slot | Can break? |
|---|---|---|---|
| 1st upgrade | 1 {{ item(6304) }} | Slot 4 | No |
| 2nd upgrade | 2 {{ item(6304) }} | Slot 3 | No |
| 3rd upgrade | 3 {{ item(6304) }} | Slot 2 | Feral Boots and Feral Tail only |

Your progress is saved **on your character**, not on the item. Every step takes the item from your inventory
and gives you a new one with all the enchants you have rolled so far.

!!! note "Carry exactly one copy"
    The NPC builds the new item from your character's record, not from the item itself, so it can't tell copies
    apart. If you carry more than one copy of the item, it refuses to upgrade until you put the extras away.

## 1st upgrade (slot 4)

| Enchant | Jalapeno, Brare, Mancho | Kareka |
|---|---|---|
| {{ item(4766) }} | 15% | 28.89% |
| {{ item(4767) }} | 10% | 4.44% |
| {{ item(4764) }} | 15% | 17.78% |
| {{ item(4765) }} | 10% | 4.44% |
| {{ item(4762) }} | 15% | 17.78% |
| {{ item(4763) }} | 10% | 4.44% |
| {{ item(4760) }} | 15% | 17.78% |
| {{ item(4761) }} | 10% | 4.44% |

## 2nd upgrade (slot 3)

| Enchant | Jalapeno, Brare, Mancho | Kareka |
|---|---|---|
| {{ item(4730) }} | 20% | 28.89% |
| {{ item(4731) }} | 13.33% | 4.44% |
| {{ item(4710) }} | 20% | 28.89% |
| {{ item(4711) }} | 13.33% | 4.44% |
| {{ item(4720) }} | 20% | 28.89% |
| {{ item(4721) }} | 13.33% | 4.44% |

## 3rd upgrade (slot 2)

### Gold Trickle and Light of El Dicastes (Brare, Kareka)

Never breaks.

| Enchant | Chance |
|---|---|
| {{ item(4730) }} | 31.11% |
| {{ item(4731) }} | 2.22% |
| {{ item(4710) }} | 31.11% |
| {{ item(4711) }} | 2.22% |
| {{ item(4720) }} | 31.11% |
| {{ item(4721) }} | 2.22% |

!!! tip
    Brare warns that the Gold Trickle (he calls it the Golden Bell) can break on the 3rd upgrade. It
    cannot: only the Feral Boots and Feral Tail can break.

### Feral Boots and Feral Tail (Jalapeno, Mancho)

This step can **destroy the item**. When that happens your record is cleared too and you start over with a
new item. The break chance goes down the more accounts you have invested with the **Investment Cat Helper**
in Malangdo (`/navi mal_in02 134/31`):

| Invested accounts | Break chance |
|---|---|
| 0 | 35.71% |
| 1,000 | 30.77% |
| 2,000 | 25% |
| 3,000 | 18.18% |
| 4,000 | 10% |
| 4,500 or more | 5.26% (lowest) |

If the item does not break, the enchant is:

| Enchant | Chance (when it does not break) |
|---|---|
| {{ item(4730) }} | 16.67% |
| {{ item(4731) }} | 11.11% |
| {{ item(4732) }} | 5.56% |
| {{ item(4710) }} | 16.67% |
| {{ item(4711) }} | 11.11% |
| {{ item(4712) }} | 5.56% |
| {{ item(4720) }} | 16.67% |
| {{ item(4721) }} | 11.11% |
| {{ item(4722) }} | 5.56% |

## Reset

| NPC | When | Cost | Result |
|---|---|---|---|
| Jalapeno, Brare, Mancho | Any time (**I want to reset.**), or after the 3rd upgrade (**Please take it.**) | Free | The item is **taken away** and your record is cleared. Bring a new item to start over. |
| Kareka | Only after the 3rd upgrade | 6 {{ item(6304) }} | Your old {{ item(2844) }} is taken and you get a clean one. Your record is cleared. |
