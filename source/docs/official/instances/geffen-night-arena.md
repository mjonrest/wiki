# Geffen Night Arena

## Guide

Geffen Night Arena is a **solo** boss-rush tournament. You face up to 10 rounds of Midnight duelists, one at a time, each with a 60-second time limit. The tournament ends at your first failure, or when you beat the champion in round 10, and the reward depends on how far you got.

### Requirements and entry

| | |
|---|---|
| Level | Base Level 210 or higher |
| Party | You must be the leader of a party with **only yourself** in it. The portal refuses you if anyone else has joined the party. |
| NPC | **Greedy Looking Man** at `/navi geffen_in 82/62` |
| Entrance | **Portal** at `/navi dali02 79/60` |
| Cooldown | Once per day. Entering starts the cooldown, which resets at 04:00 server time. |
| Time limit | The instance closes 60 minutes after it is created. |

1. Talk to the Greedy Looking Man in Geffen and agree to join the tournament. This creates the arena.
2. Talk to him again and choose **Yes** to be sent to the arena entrance in the Dimensional Gap (`dali02`).
3. Step into the **Portal** to enter.

### How the tournament works

1. Inside, talk to the **Greedy Looking Man** (around `1@ge_sn 111/62`) to start the next round.
2. Your opponent is announced and walks into the ring, and a 5-second countdown starts. The opponent appears around 10 seconds after you talk to him.
3. **You have 60 seconds to kill the opponent.**
    - If you win, talk to the Greedy Looking Man again to start the next round.
    - If time runs out, the opponent disappears and the tournament is over.
4. Rounds 1 to 9 draw a random opponent from:
    {{ mob(20856) }}, {{ mob(20857) }}, {{ mob(20858) }}, {{ mob(20859) }}, {{ mob(20860) }}, {{ mob(20861) }}, {{ mob(20862) }}, {{ mob(20863) }}, {{ mob(20864) }}, {{ mob(20865) }}, {{ mob(20866) }}, {{ mob(20867) }}, {{ mob(20868) }}, {{ mob(20869) }}, {{ mob(20870) }}
5. Round 10 is always {{ mob(20872) }}. Beating him completes the tournament.
6. When the tournament is over (either way), talk to the Greedy Looking Man to collect your reward. You are then sent back to `dali02`.

### Rewards

The reward depends on the last round you **cleared**:

| Rounds cleared | {{ item(1000316) }} | {{ item(1000317) }} | {{ item(1000366) }} |
|---|---|---|---|
| 0 | — | — | — |
| 1 | 2 | — | — |
| 2 | 3 | — | — |
| 3 | 4 | — | — |
| 4 | 6 | 1 | — |
| 5 | 9 | 1 | — |
| 6 | 14 | 2 | — |
| 7 | 22 | 2 | 1 |
| 8 | 35 | 3 | 1 |
| 9 | 56 | 4 | 2 |
| 10 (champion) | 89 | 5 | 3 |

You also get **20 to 40 Instance Points** when you collect the reward.

Spend the coins and certificates at the **Reward Geffen Night Arena** vending machine at `/navi dali02 85/70`. It has a default, special and card shop, plus an enchant option.

!!! tip "Instance Points"
    Instance Points can be earned once per device for each instance run, up to 1200 per account per day. A rented {{ item(30034) }} adds 50 points per claim. Use `@instancepoints` to see your total.

{{ instance_page("geffen-night-arena") }}
