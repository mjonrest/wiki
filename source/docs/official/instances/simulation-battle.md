# Simulation Battle

## Guide

Simulation Battle is the repeatable Episode 19 rematch against Juncea. Bagot's laboratory has been turned into a training room where you fight a simulated copy of her, {{ mob(21533) }}, once per cooldown.

### Requirements and entry

| | |
|---|---|
| **NPC** | Arolong, Nest of Jormungandr: `/navi jor_nest 66/260` |
| **Prerequisite** | Episode 19 main story completed (Arolong will not talk to you before then) |
| **Party** | Required. Only the party leader can create the instance; any member can then enter it |
| **Time limit** | 60 minutes (closes after 5 minutes with nobody inside) |
| **Cooldown** | 4 hours, starting when you hand in the battle to Arolong |

1. The party leader talks to Arolong, answers **Lift**, and picks **Prepare to enter Bagot's lab**.
2. Everyone talks to Arolong again and picks **Enter Bagot's Lab**. Entering adds the *Simulation Battle* quest to your log.
3. You arrive in the laboratory (`1@jorlab`).

!!! note
    Arolong also needs room for one more item in your inventory before he opens the menu.

### Walkthrough

1. Walk up to the **Summon Device** in the middle of the laboratory. Only the party leader can start it.
2. Confirm twice and the device summons {{ mob(21533) }} at its location.
3. Kill her. When she dies, the Summon Device reappears.
4. Each party member talks to the Summon Device and chooses **Yes** to collect the reward and get sent back to the Nest of Jormungandr (`jor_nest 63/257`).
5. Talk to Arolong to hand in the *Simulation Battle* quest. This gives the turn-in reward and starts the 4 hour cooldown.

### Rewards

| From | Reward | Who |
|---|---|---|
| Summon Device (after the kill) | {{ item(102563) }} x1 | Every member who claims it, once per character until the next turn-in to Arolong |
| Summon Device (after the kill) | 40-60 Instance Points | Every member who claims it (counts toward the server's daily Instance Point cap of 1200) |
| Arolong (quest turn-in) | {{ item(1000811) }} x1 | Each character who hands in the quest |

!!! tip
    If your inventory is full the Summon Device refuses to hand out the Antiquity box but does not send you out, so free a slot and click it again.

!!! warning "Known issue"
    Arolong counts the *Simulation Battle* quest as finished as soon as it is in your log; he does not check that Juncea was actually beaten. If you leave the laboratory (death, logout, warp) and talk to Arolong before winning, he hands in the quest and puts you on the 4 hour cooldown, so you cannot go back in through him. Finish the fight in one go before talking to Arolong again.

{{ instance_page("simulation-battle") }}
