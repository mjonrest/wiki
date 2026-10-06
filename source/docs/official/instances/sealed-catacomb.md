# Sealed Catacomb

## Guide

Also called the **Sealed Shrine**. The party descends under St. Capitolina Abbey to stop the Great Demon Baphomet
from breaking free. Floor 1 is a scavenger hunt against a timer; floor 2 is the fight against an invincible
Baphomet that can only be hurt while a magical seal is weakening him.

### How to enter

| | |
|---|---|
| **NPC** | Friar Patrick at St. Capitolina Abbey: `/navi monk_test 309/146` |
| **Level** | 75+ |
| **Party** | At least 2 members. The party leader asks Friar Patrick to open the seal |
| **Entering** | Everyone then touches the **Grave of Baphomet** next to him (`/navi monk_test 306/151`) |
| **Cooldown** | 12 hours per character ("The Curse of Baphomet"), starting when you enter |
| **Time limit** | 2 hours |

!!! warning
    Friar Patrick warns that some protective skills, such as **Safety Wall** and **Assumptio**, are blocked by the
    seal inside. Any Token of Apostle you carry is taken away when you touch the Grave of Baphomet.

### Floor 1: gathering the keys

1. **The hero's grave.** Go to the gravestone at the north (around 141/221) and choose *"Waited for me?"*.
2. **Pendant of Spirit.** Thirteen gravestones are scattered across the floor. Search them: twelve of the thirteen
   hold a {{ item(6003) }} (one is randomly empty). Only one pendant can be taken per run.
3. **Wake the hero.** The **party leader**, carrying the pendant, touches the north gravestone again. The
   **Ancient Hero's Soul** appears at the fire altar in the center (176/119).
4. **Start the trial.** Talk to the Ancient Hero's Soul and ask all three questions (Essence of Fire, Token of
   Apostle, what to do) before choosing *"I am ready."* When the **leader** does this:
    - 12 **Bobbing Torches** light up around the floor.
    - 15 **Apostles of Baphomet** spawn at random spots. Each one gives a {{ item(6002) }} to whoever kills it.
    - A timer starts (see below).
5. **Collect the Essence of Fire.** Only the **party leader** can take a {{ item(6001) }} from a torch. Anyone else
   who touches a torch loses half their HP.
6. **Open the gate.** The leader brings at least **10 Essence of Fire and 1 Token of Apostle** to the Ancient
   Hero's Soul, then talks to him once more. The gate to the Main Altar opens in the south-east corner (281/12).
7. **Go down.** Each player needs their **own Token of Apostle** to use the gate; it is used up on the way through.

!!! warning "The floor 1 timer"
    From the moment the leader starts the trial, the Ancient Hero's Soul warns you at 30 and 40 minutes, and at
    about 51 minutes the seal is announced as failed. At about **58 minutes** everyone still in the instance is
    thrown out to the abbey. Make sure every party member has a Token of Apostle before the Apostles run out.

### Floor 2: sealing Baphomet

1. Walking in triggers Baphomet's warnings. Three spots around the Main Altar (left 50/67, right 109/67, bottom
   79/39) are traps: stepping on one spawns 16 Apostles of Baphomet ({{ mob(1869) }}, {{ mob(1291) }},
   {{ mob(1292) }}, {{ mob(1117) }}, {{ mob(1132) }} and a {{ mob(1867) }}). These traps re-arm **every 5 minutes**
   during the Baphomet fight.
2. The **party leader** touches **The Main Altar** (79/65). About 17 seconds later {{ mob(1929) }} appears on the
   altar.
3. Baphomet keeps himself **invincible**. Five **Magical Seals** surround the altar; only one is active at a time:

    | Seal | Location |
    |---|---|
    | Center (Main Altar) | 79/81 |
    | 2 o'clock | 123/109 |
    | 4 o'clock | 123/22 |
    | 8 o'clock | 35/21 |
    | 10 o'clock | 35/109 |

    The center seal activates first; after that a random seal is announced roughly every 70 seconds.
4. Touching the active seal removes Baphomet's invincibility, **but only if Baphomet is within 10 cells of that
   seal**. The player who touches it loses half their HP and is turned to stone for 20 seconds, and cannot use
   another seal for 3 minutes (trying anyway costs half your HP and a 30-second petrify).
5. Seals only work for **1 hour** after Baphomet appears. After that he can no longer be made vulnerable.
6. When Baphomet dies the Ancient Hero's Soul appears at the altar (80/63). Talk to him to leave.

!!! tip
    The tank should drag Baphomet to the announced seal while a different player (not the one who touched the last
    seal) waits next to it. Rotate the seal duty so nobody is on the 3-minute lockout when the next seal lights up.

### Rewards

- **10 Instance Points** for each player who leaves through the Ancient Hero's Soul (see
  [Instance Points](../../content/instances.md)).
- Baphomet's drops, including the {{ item(6004) }}.

### Gigantic Majestic Goat

Show a {{ item(6004) }} to Friar Patrick, then talk to **Rust Blackhand** in the abbey (`/navi prt_monk 261/91`).
He crafts a {{ item(5374) }} from:

| Material | Amount |
|---|---|
| {{ item(6004) }} | 1 |
| {{ item(2256) }} | 1 |
| {{ item(7799) }} | 30 |
| {{ item(7798) }} | 50 |
| Zeny | 990,000 (you need slightly more than this on hand) |

{{ instance_page("sealed-catacomb") }}
