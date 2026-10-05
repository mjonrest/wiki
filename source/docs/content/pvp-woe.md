# PvP & WoE

## PvP Ladder

**Location:** {{ npc_where("Ladder") }} · or type `@pvpladder` anywhere

{% set p = arrays("npc/miracle/s_pvp_rank.txt", "Ladder") %}
| Room | Map | Max players |
|---|---|---|
{% for m in p["MapName$"] %}| {% if p.MapMode[loop.index0] % 2 %}GvG (guild only){% else %}PvP{% endif %} | `{{ m }}` | {{ p.MaxPlayers[loop.index0] }} |
{% endfor %}

- Kills and deaths are tracked for a lifetime and a **monthly** ladder, for players and guilds.
- Killing the same player over and over stops counting after 5 kills.
- {{ item(1599) }} and {{ item(2199) }} must be stored before entering.
- [One character per computer](../guide/fair-play.md) in PvP rooms.

## PvP stats

The **PvP-StatsViewer** ({{ npc_where("PvP-StatsViewer") }}) shows your kill streaks and multi-kills, with
DotA-style kill announcements in PvP.

## War of Emperium

- Only guilds **approved by a GM** can enter castles during WoE. Contact a GM to register your guild.
- At most **15 members** of one guild may be in the same castle.

The **Guild Limiter** NPC is at {{ npc_where("Guild Limiter") }}.
