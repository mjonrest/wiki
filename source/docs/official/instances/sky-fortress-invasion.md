# Sky Fortress Invasion

## Guide

A fortress floating above invaded Prontera keeps spawning undead. Scientist Doyeon opens a warp into it, and your party has to fight through the fortress and destroy the golem **Stefan.J.E.Wolf**. Along the way you can collect keys that open side rooms with treasure and two optional bosses.

### How to enter

- **NPC:** Scientist Doyeon in invaded Prontera, `/navi prt_q 249/79`. The **Fortress Entry Warp Portal** is next to her at `/navi prt_q 243/75`.
- **Level:** Base Level 145 or higher. You also need some free inventory space to talk to Doyeon.
- **Party:** The party leader talks to Doyeon and picks **"Enter the Sky Fortress."** (later runs: **"Yes"**). Then everyone steps into the portal.
- **Cooldown:** After your first run, talk to Doyeon again to report. This completes the quest and starts a **3 day 4 hour** cooldown ("Attack Sky Fortress Invading Prontera"). The first time you report, you also get a 1-hour {{ item(14505) }}.
- **Skipping the cooldown:** With a **Sky Fortress Ticket** ({{ item(14505) }} or {{ item(14506) }}), the leader can pick **"Show the -Dungeon Pass-"** to open the fortress during the cooldown. Members use **"Put the - Dungeon Pass - near to the warp"** at the portal. A second portal in the Dimensional Gap (`/navi dali02 115/61`) also takes ticket holders in. Entering with a ticket does not change your cooldown, and the ticket is not used up.

### Step 1: The courtyard

You arrive at the fortress gate. Walk forward a few steps and {{ mob(3484) }} appears. Once his HP drops below **19,000,000**, he retreats, and the fortress sends three waves of 8 {{ mob(3476) }}. The last wave includes a {{ mob(3478) }}.

When the waves are cleared, walk up to Stefan at `64/67`. He leaves, and the rest of the fortress opens:

- the stairs at `73/71`, which lead to the upper floor
- the warp at `93/77` to the east wing (`210/96`)
- the warp at `190/54` in the east wing, which leads to **Stefan's room** (the final boss)
- six **Deactivated Warps** to the side rooms

Walking into the corridors and the east wing triggers groups of {{ mob(3477) }}, {{ mob(3479) }} and {{ mob(3480) }}. Each group has a **20% chance** to include another Key Keeper.

### Keys and side rooms (optional)

Every {{ mob(3478) }} drops a {{ item(6960) }}. Use a key on a **Deactivated Warp** to activate it. Each warp leads to one of six rooms, and the warp-to-room order is shuffled every run.

| Room | What happens | Reward |
|---|---|---|
| 4 Shadow rooms | 10 {{ mob(3481) }} or {{ mob(3482) }} spawn. Kill them all | A **Sky Fortress Gold Treasure** (party leader opens) |
| Cursed Knight room | Several {{ mob(3483) }} spawn and a treasure box appears | The leader opens the box to summon {{ mob(3474) }} |
| Wind Ghost room | Several {{ mob(3483) }} spawn and a test tube appears | The leader examines it to summon {{ mob(3475) }} |

The Gold Treasure gives the party leader one item:

| Item | Chance |
|---|---|
| {{ item(985) }} | 32% |
| {{ item(984) }} | 32% |
| {{ item(608) }} | 20% |
| {{ item(607) }} | 10% |
| {{ item(616) }} | 5% |
| {{ item(12246) }} | 1% |

### Final boss: Stefan.J.E.Wolf

Take the warp at `190/54` and walk toward the center of the room. {{ mob(3473) }} awakens with **20,000,000 HP**.

- **Between 14,000,000 and 6,000,000 HP:** {{ mob(3476) }} keep spawning in groups of 3, up to 8 at a time.
- **Below 5,000,000 HP:** Those adds disappear. Pairs of {{ mob(3485) }} spawn every 8 seconds.
- **Ground-shaking zones (below 5,000,000 HP):** Every 6 seconds, several spots around the room shake with a 4-second warning bar. Then each spot becomes deadly for a moment, and **anyone standing in it dies instantly**. Move as soon as a warning appears under you.

When Stefan dies, the remaining adds vanish and the **Sky Fortress Escape Warp** appears in the middle of the room.

### Rewards

- Boss drops from Stefan and the optional bosses.
- Gold Treasures from the side rooms (see above).
- **20–40 [Instance Points](../../content/instances.md)** when you leave through the Escape Warp. This counts toward the daily 1,200 cap. The warp takes you back to where you entered (Prontera or the Dimensional Gap).

!!! warning "Known issue"
    When you summon the Immortal Cursed Knight or the Immortal Wind Ghost, an announcement saying it has died shows up about 2 seconds later, even though the boss is still alive. Ignore it and keep fighting.

{{ instance_page("sky-fortress-invasion") }}
