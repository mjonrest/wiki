# Abyssal Bloody Branch

{% set f = "npc/miracle/abyssal_bb.txt" %}
{% set mvps = arrays(f, "F_EP16_20_Branch")["list"] %}

The {{ item(30063) }} is the next tier of the normal Bloody Branch. Using it summons **one random MVP** from a
list of **{{ mvps | length }}** bosses next to you.

- **MVPs only.** No mini bosses.
- **Field and dungeon MVPs only.** Every boss on the list spawns on a normal map or an Illusion map. Instance and
  memorial dungeon bosses are not included.
- **No repeats from the normal Bloody Branch.** Nothing that the normal Bloody Branch can summon is on this list.
- **Almost all of them drop a card.** That includes the new Episode 21 and Chapter 1 MVPs.

## Where you can use it

It works on the same maps as a normal Bloody Branch. On maps that block branches, and on WoE, GvG and
Battleground maps, the game refuses it and you keep the item.

## Possible MVPs

{% set cols = 3 %}
| | | |
|---|---|---|
{% for i in range(0, mvps | length, cols) -%}
| {% for m in mvps[i:i+cols] %}{{ mob(m) }} | {% endfor %}{% for _ in range(cols - (mvps[i:i+cols] | length)) %} | {% endfor %}
{% endfor %}

Each boss on the list has the same chance to appear.
