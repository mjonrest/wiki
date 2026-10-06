# Weekend Dungeon

## Guide

A weekend-only training ground. You pick a level bracket, then farm endlessly respawning Familiars, Skeletons and
Zombies for experience, while hunting for treasure chests full of EXP elixirs.

### How to enter

| | |
|---|---|
| **NPC** | Marry Jae in Archer Village: `/navi pay_arche 44/124` |
| **Open** | **Saturday 00:00 ~ Sunday 23:59** (server time) only |
| **Level** | 60+ |
| **Party** | Required, but a party of one is fine. The party leader prepares the dungeon |
| **Re-entry** | After your first entry you may re-enter for **1 hour**; after that you must wait until the next **04:00** server time |
| **Time limit** | 1 hour |

!!! note
    Taming monsters inside does not count as a kill.

### Choosing the difficulty

Inside, the party leader talks to Marry Jae at the entrance and picks a bracket. The leader's own base level must
reach the bracket's minimum. The bracket sets which monsters spawn:

| Bracket | Familiar | Skeleton | Zombie |
|---|---|---|---|
| Lv 60 ~ 79 | {{ mob(3643) }} | {{ mob(3637) }} | {{ mob(3649) }} |
| Lv 80 ~ 99 | {{ mob(3644) }} | {{ mob(3638) }} | {{ mob(3650) }} |
| Lv 100 ~ 119 | {{ mob(3645) }} | {{ mob(3639) }} | {{ mob(3651) }} |
| Lv 120 ~ 139 | {{ mob(3646) }} | {{ mob(3640) }} | {{ mob(3652) }} |
| Lv 140 ~ 159 | {{ mob(3647) }} | {{ mob(3641) }} | {{ mob(3653) }} |
| Lv 160+ | {{ mob(3648) }} | {{ mob(3642) }} | {{ mob(3654) }} |

Once chosen, Marry Jae leaves and about 95 monsters (37 Familiars, 27 Skeletons, 31 Zombies) fill the map. The
bracket cannot be changed for that instance.

### Farming and treasure chests

- Every monster you kill respawns somewhere random on the map **10 seconds** later, so the map never empties.
- Each kill has a **1% chance** to make a treasure chest appear. The whole map is told when it happens. The chests
  appear in turn at four spots: 99/172, 235/60, 53/267 and 238/252.
- A chest disappears after **3 minutes**. Opening it drops **3 elixirs** on the ground, each randomly a
  {{ item(23142) }} or a {{ item(23143) }}.

| Elixir | Effect |
|---|---|
| {{ item(23142) }} | 15,000 base EXP below level 100, 1,500 base EXP at level 100+ |
| {{ item(23143) }} | 15,000 job EXP below level 100, 1,500 job EXP at level 100+ |

### Gift Supplies Clerk

Next to Marry Jae (`/navi pay_arche 44/121`). For 60,000 zeny she packs 5 {{ item(23142) }} into a
{{ item(23144) }}, or 5 {{ item(23143) }} into a {{ item(23145) }}.

{{ instance_page("weekend-dungeon") }}
