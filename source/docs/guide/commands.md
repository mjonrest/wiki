# Commands

On top of the standard rAthena player commands, Miracle adds these:

| Command | What it does |
|---|---|
| `@eventjoin` | Shows your Event Points and lets you join the [automatic event](../content/events.md) that is open right now. |
| `@instancepoints` | Shows how many [Instance Points](../content/instances.md) you earned today (daily cap 1,200) and your total. |
| `@activity` | Turns the Activity Points messages on or off. See [Gacha Machines](../content/gacha.md). |
| `@HourlyBan` | Opts this character out of Activity Points until you relog. |
| `@donate` | Opens the donation shops (PoD Shop and Cash Shop). |
| `@statsview` | Lists every bonus on your character from gear, cards, enchants, combos and buffs. See [below](#statsview). |
| `@alootid2` | Saves up to 10 named autoloot lists and loads one with a single command. See [below](#alootid2). |
| `@hera <question>` | Asks [Hera](hera.md) a question about Miracle from anywhere. She answers you privately. |
| `@dummy` | Warps you to the Dummy Punching Bags in Prontera. |
| `@pvpladder` | Opens the PvP/GvG ladder menu from anywhere. See [PvP & WoE](../content/pvp-woe.md). |

!!! note "Commands are disabled in some places"
    Hell Raid, the Mining Zone and the World Boss map block most commands and the cash shop.

## @statsview

`@statsview` shows the **general** and **resist** pages. Add a page name to see another one, or `all` for everything.
You can use it once every 3 seconds.

| Page | What it lists |
|---|---|
| `@statsview general` | Stat, HP/SP, ATK/MATK and trait % bonuses |
| `@statsview offense` | Damage against race, element, size and class, ignore DEF/MDEF |
| `@statsview resist` | Damage reduction, element/race/size resist and status resists |
| `@statsview skill` | Cast time, delay, cooldown, per-skill damage and SP cost |
| `@statsview proc` | Autospells, autobonus, chances to cause statuses, HP/SP drain |
| `@statsview misc` | EXP and drop bonuses, extra drops, healing item bonuses and regen |
| `@statsview all` | Every page |

## @alootid2

`@alootid2` keeps **saved autoloot groups**: lists of up to 10 items you can switch between, instead of typing
`@alootid` for each item again. You can have **10 groups** per character, numbered 1 to 10.

| Command | What it does |
|---|---|
| `@alootid2 list` | Shows your groups. `@alootid2 list <#>` shows the items in one group |
| `@alootid2 load <#>` | Clears your current autoloot list and autoloots the items in group `#` |
| `@alootid2 save <#> <item> ...` | Saves your list of items into group `#`, replacing what it had |
| `@alootid2 add <#> <item> ...` | Adds items to group `#` |
| `@alootid2 remove <#> <item> ...` | Removes items from group `#` |
| `@alootid2 clear <#>` | Empties group `#` |
| `@alootid2 set <#> name <name>` | Names the group (up to 24 characters, spaces allowed) |
| `@alootid2 set <#> autoload 1` | Loads this group by itself every time you log in (`0` turns it off). Only one group can do this |

Give items by their **item ID** (find them in the [item database](../db/items.md)). Wait 2 seconds between `@alootid2` commands.
