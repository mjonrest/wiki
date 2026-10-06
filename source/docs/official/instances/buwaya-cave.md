# Buwaya Cave

## Guide

A one-room boss hunt in Malaya: go into the cave and kill {{ mob(2319) }}. The fight runs on timers. Buwaya keeps
grabbing people into his treasure box and sending clones after you, so the run is about dealing with those
interruptions while you bring the boss down.

### Entering

- **Level:** 130 or higher.
- **Party:** you must be in a party. The **party leader** talks to the **Guard** at `/navi ma_fild02 312/317` and
  picks *I'm here to hunt down Buwaya.* to open the tunnel.
- **Entrance:** walk onto the **Cave Entrance** at `/navi ma_fild02 315/323`.
- **Cooldown:** entering gives you the *Devil in the Cave* quest. The cooldown ends at the next **04:00** server time.
- You cannot change party members or the leader while you are inside the cave.

### The fight

You start in the west part of the cave. {{ mob(2319) }} (4,090,365 HP) waits in the middle of the big chamber
(around `1@ma_c 97/74`). The chamber is full of {{ mob(2331) }}, {{ mob(2329) }} and some {{ mob(2330) }}. Only
Buwaya has to die.

**Treasure box (every 35 seconds)**

- Buwaya shouts *"I will put you in my treasure box!"* and light pillars appear around the chamber.
- About 4 seconds later, **everyone within 50 cells of the middle of the chamber** is pulled into the treasure box.
  That is most of the room.
- Inside the box, every 2 seconds you lose **10% HP and SP** and get **Bleeding** and **Poison** for 60 seconds.
  Get out fast.
- Two captives are inside:
    - **Kidnapped People #1** ("Get me outta here!!") spawns two {{ mob(2333) }}. Kill both (20 HP each) to open
      the way out. It drops you at a random spot near the middle of the chamber.
    - **Kidnapped People #2** ("Tell me.") gives you **+45 ATK and +45 MATK for 60 seconds**. Grab it before you
      leave.
- The box resets every cycle, so you can be caught again.

**Clones (about every 105 seconds)**

- About a minute in, Buwaya counts down *"This is... MY... Deadly... ATTACK!"* and four {{ mob(2332) }} clones
  (30,000 HP each) spawn, one in each corner of the chamber.
- The clones disappear on their own 40 seconds later. If you kill all four sooner, the next set comes about 65 seconds
  after the last one dies.

**Monsters on the way out**

Every 60 seconds, 10× {{ mob(2331) }} and 10× {{ mob(2329) }} spawn near the cave entrance (only 1 of each once 30
or more are already there). They pile up if you take a long time, so expect a crowd on the way out.

### Finishing

When Buwaya dies, the box, the clones and the entrance spawns all stop, and the guard tells you to leave the way you
came in. The **exit** opens near the cave entrance (`1@ma_c 28/57`). Taking it gives **20–40 Instance Points**
(+50 with {{ item(30034) }}, within the daily Instance Point limit) and returns you to `ma_fild02`.

{{ instance_page("buwaya-cave") }}
