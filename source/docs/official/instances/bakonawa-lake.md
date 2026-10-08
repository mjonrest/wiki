# Bakonawa Lake

## Guide

Bakonawa Lake is a three-phase boss fight against the sea serpent Bakonawa, who is trying to swallow the moon. Each phase has its own timer. If a timer runs out, Bakonawa escapes and the party has to start again from the first phase.

### How to enter

- **NPC:** Taho, in the Malaya cave scene at `/navi ma_scene01 174/179`.
- **Level:** Base Level 140 or higher.
- **Party:** You need a party. The party leader picks **"Please weave a rope."** to create the instance. Then every member picks **"Now I will go down."** to enter.
- **Inventory:** You need at least 1,000 free weight and some free inventory slots, or Taho refuses to talk to you. The same check applies when you claim the reward at the end.
- **Cooldown:** Entering starts a daily cooldown that resets at **04:00** server time. Until it ends, Taho tells you the rope is broken. Once it has passed, talk to Taho once to clear it, then talk to Taho again to enter.
- **Time limit:** The instance closes after 2 hours.

!!! note
    Taho also gives you the hunting quest "Get Rid of Bakonawa", which asks you to kill the final form of Bakonawa. You need to finish this quest to get the Ancient Grudge reward at the end. You get the quest again each time you talk to Taho with no cooldown running.

### Phase 1: Bakonawa surfaces

Inside, talk to **Taho** near the entrance. When the party leader picks **"Let's do it!"**, Taho pours Albopal into the lake and {{ mob(2320) }} rises from the water.

- You have **10 minutes** to kill it. A time warning is announced every minute.
- Bakonawa heals itself when its HP is below 30%. It also uses Meteor Storm, Sonic Blow, Dark Breath and bleeding attacks.

### Phase 2: Caldrons and gongs

After the first kill, Bakonawa dives and tries to swallow the moon. An {{ mob(2321) }} appears in the middle of the lake. Taho tells you not to fight it. Instead, make noise:

- Destroy the **2 Caldrons and 2 Gongs** ({{ mob(2328) }}, 200 HP each) on the left and right banks of the lake. Taho announces how many are left.
- You have **5 minutes**. When all four are destroyed, Bakonawa retreats and the next phase starts about 10 seconds later.

### Phase 3: Enraged Bakonawa

The final form, {{ mob(2322) }}, comes out of the lake. You have **10 minutes** to kill it.

- Starting 2 minutes into the phase, a wave of {{ mob(2334) }} ("Bakonawa's Puppet") spawns on the south shore every minute. Each new wave replaces the puppets still alive and is larger than the last: 10, 15, 20, 30, 35, 40, 45 and finally 50. A counter on screen shows how many are left.
- Bakonawa's final form heals itself below 30% HP. It casts Storm Gust, Lord of Vermilion, Meteor Storm and Water Ball, uses Dragon Fear, and can break your armor and weapon. Expect Reflect Shield too.

When it dies, a {{ mob(2335) }} appears in the lake. Open it, then go back to **Taho** at the top of the hill.

### Bakonawa's Will (all phases)

Throughout the fight, about 5 seconds after most time-limit announcements, invisible "Bakonawa's Will" monsters can appear at up to 9 spots around the lake. Some cast Meteor Storm ({{ mob(2337) }}) and others cast Storm Gust ({{ mob(2343) }}). They disappear 50 seconds later. Don't stand in one place around the lake edge for too long.

### Failing a phase

If any timer reaches zero, Bakonawa escapes. Taho reappears near the entrance, and the party leader can pick **"Of course! We cannot stand back now!"** to start again from **Phase 1**. You can retry as long as the instance is still open.

### Rewards

| Reward | Who | Notes |
|---|---|---|
| {{ item(6499) }} ×5 (×7 with VIP) | Each player who finished the hunting quest | Talk to Taho after the fight |
| 100,000 Job EXP | Same as above | |
| 20–40 [Instance Points](../../content/instances.md) | Each player who talks to Taho at the end | Random amount. Counts toward the daily 1,200 point cap |
| Treasure box drops | Party | From {{ mob(2335) }}, see the boss table below |

Talking to Taho at the end warps you back out to `ma_scene01`.

!!! tip
    Make sure everyone is buffed and in position before the leader starts Phase 1. A failure in any phase sends you back to the start, and the final phase gets harder the longer it lasts because the puppet waves keep growing.

{{ instance_page("bakonawa-lake") }}
