# Grade Enhancement (Sratos and Suribell)

<!-- npcs: Sratos; Suribell -->

Grade Enhancement raises the **grade** of high-end gear one step at a time: no grade, then **D**, **C**, **B** and
finally **A**. Each grade adds a bonus to the item. Both NPCs open the same grade window and run the same
Etel exchange.

**Where:**

- **Sratos:** `/navi grademk 34/184`. The entrance to this room is at `/navi prontera 50/293`.
- **Suribell:** `/navi paramk 34/184` (Paramarket)

## Items it works on

- **Weapons of weapon level 5**
- **Armor of armor level 2** (any equipment slot)

The item must be refined to at least the level shown below for the next grade.

## Etel exchange

Choose **"Exchange Etel items"** to make the materials:

| You get | Zeny | Materials |
|---|---|---|
| {{ item(1000323) }} | 100,000 | 5 {{ item(1000322) }} |
| {{ item(1000337) }} | 100,000 | 5 {{ item(1000322) }}, 1 {{ item(6635) }} |
| {{ item(1000325) }} | 100,000 | 3 {{ item(1000323) }}, 1 {{ item(720) }} |
| {{ item(1000326) }} | 200,000 | 6 {{ item(1000323) }}, 1 {{ item(728) }} |
| {{ item(1000327) }} | 300,000 | 10 {{ item(1000323) }}, 1 {{ item(719) }} |
| {{ item(1000328) }} | 300,000 | 15 {{ item(1000323) }}, 1 {{ item(1000321) }} |

## Upgrading a grade

Choose **"Enhance the equipment's grade."**, then **"I'll still do it!"**. A window opens; put the item in and
pick one of two payment options.

**On success** the grade goes up by one and the item's **refine is reset to +0**. Cards, enchants and random
options stay.

### Success chance by refine

Weapons and armor use the same table. A dash means you cannot try at that refine.

| Upgrade | +9 | +10 | +11 to +15 | +16 to +20 |
|---|---|---|---|---|
| No grade → D | 10% | 20% | 70% | 80% |
| D → C | - | 20% | 60% | 70% |
| C → B | - | - | 50% | 60% |
| B → A | - | - | 40% | 50% |

### Cost options

| Upgrade | Cheap option | Safe option |
|---|---|---|
| No grade → D | 1 {{ item(1000325) }} + 175,000z | 5 {{ item(1000325) }} + 875,000z |
| D → C | 1 {{ item(1000326) }} + 175,000z | 5 {{ item(1000326) }} + 875,000z |
| C → B | 1 {{ item(1000327) }} + 175,000z | 5 {{ item(1000327) }} + 875,000z |
| B → A | 2 {{ item(1000328) }} + 175,000z | 10 {{ item(1000328) }} + 875,000z |

- **Cheap option:** if it fails, the item is **destroyed**.
- **Safe option:** if it fails, nothing happens to the item. Only the materials and zeny are used up.

### Blessed Etel Dust

You can add {{ item(1000337) }} in the window to raise the chance by **1% per step**, up to **10 steps** (+10%).

| Upgrade | Dust per step | Dust for +10% |
|---|---|---|
| No grade → D | 1 | 10 |
| D → C | 3 | 30 |
| C → B | 5 | 50 |
| B → A | 7 | 70 |

!!! tip
    Successes are announced to the whole server. From C → B upward, failures are announced too.

## Grading Ticket (Sratos only)

If you carry a {{ item(30055) }}, Sratos shows an extra option, **"Enchant with Ticket"**.

1. Wear the item. She lists every equipped weapon of weapon level 5 and armor of armor level 2.
2. Pick one and choose **"Use Ticket"**.
3. The ticket is used and the item goes straight to **grade A**, whatever grade it had.

There is no failure chance, no refine requirement, and the **refine is kept** (unlike a normal upgrade).

Items that are already grade A are not listed.
