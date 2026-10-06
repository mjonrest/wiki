# Susan Grey (Odin Temple gear)

<!-- npcs: Susan Grey -->

Susan Grey enchants the Soutanes and Clergy's gear from Odin Temple, up to 3 random enchants per item.

**Where:** `/navi hu_in01 97/323`

## Items it works on

Wear the item and pick its slot (Armor, Garment or Shoes):

| Slot | Items |
|---|---|
| Armor | {{ item(15397) }}, {{ item(15398) }}, {{ item(15399) }}, {{ item(15400) }}, {{ item(15401) }}, {{ item(15402) }} |
| Garment | {{ item(20947) }} |
| Shoes | {{ item(22209) }} |

The item must not have a normal card in its 2nd, 3rd or 4th slot. A card in the first slot is kept.

## Enchanting

**Cost per enchant:** 5 {{ item(25767) }} + 500,000 zeny. Enchanting **always succeeds**, never breaks the item,
and keeps refine and the first-slot card.

Enchants are added in order: 4th slot, then 3rd slot, then 2nd slot (3 in total). Every enchant is picked at
random from the same list, each entry equally likely ("Normal" column below).

### Better 3rd enchant at +9 or higher

If the item is **refined to +9 or higher** when you add the **3rd** enchant, she offers a choice:

- **Proceed with Angel's Dream:** the normal cost and the normal list.
- **Proceed with fruit:** costs 3 {{ item(6909) }} instead (no Angel's Dream, no zeny) and uses a better list
  that depends on the item type.

| Enchant | Normal (any slot) | Fruit 3rd enchant, Armor | Fruit 3rd enchant, Garment/Shoes |
|---|---|---|---|
| {{ item(4705) }} | 3.23% | - | - |
| {{ item(4706) }} | 3.23% | 2.94% | 4.35% |
| {{ item(4707) }} | 3.23% | 2.94% | 4.35% |
| {{ item(4735) }} | 3.23% | - | - |
| {{ item(4736) }} | 3.23% | 2.94% | 4.35% |
| {{ item(4737) }} | 3.23% | 2.94% | 4.35% |
| {{ item(4725) }} | 3.23% | - | - |
| {{ item(4726) }} | 3.23% | 2.94% | 4.35% |
| {{ item(4727) }} | 3.23% | 2.94% | 4.35% |
| {{ item(4745) }} | 3.23% | - | - |
| {{ item(4746) }} | 3.23% | 2.94% | 4.35% |
| {{ item(4747) }} | 3.23% | 2.94% | 4.35% |
| {{ item(4715) }} | 3.23% | - | - |
| {{ item(4716) }} | 3.23% | 2.94% | 4.35% |
| {{ item(4717) }} | 3.23% | 2.94% | 4.35% |
| {{ item(4755) }} | 3.23% | - | - |
| {{ item(4756) }} | 3.23% | 2.94% | 4.35% |
| {{ item(4757) }} | 3.23% | 2.94% | 4.35% |
| {{ item(4764) }} | 3.23% | - | - |
| {{ item(4765) }} | 3.23% | - | 4.35% |
| {{ item(29241) }} | 3.23% | 2.94% | 4.35% |
| {{ item(4762) }} | 3.23% | - | 4.35% |
| {{ item(29238) }} | 3.23% | 2.94% | 4.35% |
| {{ item(4794) }} | 3.23% | - | - |
| {{ item(4902) }} | 3.23% | - | 4.35% |
| {{ item(4786) }} | 3.23% | - | - |
| {{ item(4787) }} | 3.23% | - | - |
| {{ item(4867) }} | 3.23% | - | - |
| {{ item(4900) }} | 3.23% | 2.94% | 4.35% |
| {{ item(4801) }} | 3.23% | - | 4.35% |
| {{ item(4802) }} | 3.23% | 2.94% | 4.35% |
| {{ item(4903) }} | - | 2.94% | - |
| {{ item(4790) }} | - | 2.94% | - |
| {{ item(4820) }} | - | 2.94% | - |
| {{ item(4821) }} | - | 2.94% | - |
| {{ item(4812) }} | - | 2.94% | - |
| {{ item(4826) }} | - | 2.94% | - |
| {{ item(4835) }} | - | 2.94% | - |
| {{ item(4836) }} | - | 2.94% | - |
| {{ item(4843) }} | - | 2.94% | - |
| {{ item(4844) }} | - | 2.94% | - |
| {{ item(4873) }} | - | 2.94% | - |
| {{ item(4881) }} | - | 2.94% | - |
| {{ item(310076) }} | - | 2.94% | - |
| {{ item(310077) }} | - | 2.94% | - |
| {{ item(310078) }} | - | 2.94% | - |
| {{ item(310079) }} | - | 2.94% | - |
| {{ item(310080) }} | - | 2.94% | - |
| {{ item(310081) }} | - | 2.94% | - |
| {{ item(29026) }} | - | - | 4.35% |
| {{ item(4788) }} | - | - | 4.35% |
| {{ item(4789) }} | - | - | 4.35% |

!!! warning "Known issue"
    - Her explanation says Clergy's Manteau and Clergy's Boots get the better option above +7, and Soutanes above
      +9. In fact all items need **+9 or higher**.
    - To even see the fruit option you must have **5 Angel's Dream and 500,000 zeny** with you. They are not
      taken if you pick the fruit, but she will refuse without them.

## Reset

Choose **"Reset enchants."** and pick the slot. The item must have **all 3 enchants**; she refuses to reset a
partly enchanted item.

| Method | Cost | Chance |
|---|---|---|
| Fruit | 2 {{ item(6909) }} | Always succeeds |
| Zeny | 500,000 zeny | 70% success. On failure the zeny is lost, the item is not harmed and keeps its enchants |

A reset removes all three enchants. Refine and the first-slot card are kept.

!!! warning "Known issue"
    If you are wearing an item she does not work with, she says "I don't handle items like this." but then
    carries on with the enchant or reset anyway. A reset on such an item clears its 2nd, 3rd and 4th slots,
    including any cards in them.
