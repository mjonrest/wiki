# Mining Zone

**Location:** {{ npc_where("Mining Gatekeeper") }}

A Novice-only mining area (`job_thief1`) full of **Mining Stones**. Hit the stones with a Pick Axe to dig up
refine and enchant-grade materials.

## Entering

- You must be a **Novice**.
- You may only carry mining tools, the materials you can mine, and {{ item(602) }}. Anything else blocks entry.
- All buffs, including food, are removed when you enter.

## Tools

Buy tools from the Gatekeeper with **Event Points**. You must equip the {{ item(30020) }} to mine.

{{ shop("mining_shop", collapsed=False) }}

## Mining EXP and refining tools

Every hit on a stone gives **1 Mining EXP**. Spend it at the Gatekeeper (**Refine Mining Equipment**) to refine your
equipped tools up to **+20**, with no chance of failure.
Refining to +N costs **N × 1,000 Mining EXP** (+1 costs 1,000, +20 costs 20,000).

Higher refines on your Pick Axe, armor, garment and shoes raise your chance of finding materials.

## What you can find

{% set m = arrays("npc/miracle/mining.txt", "mining") %}
| Tier | Items |
|---|---|
| Materials | {{ items_list(m.reward1) }} |
| Grade materials | {{ items_list(m.reward2) }} |
| Super rare | {{ items_list(m.group1) }} |
| Ultra rare | {{ items_list(m.group2) }} |
| Extremely rare | {{ items_list(m.group3) }} |
| Legendary | {{ items_list(m.group4) }} |

Super rare and better finds are announced to the whole server.
