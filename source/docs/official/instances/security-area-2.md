# Security Area 2

## Guide

Security Area 2 is the hard daily mode of the Flower Garden's security zone in Varmundt's Mansion (Episode 17.2). It uses the same map and layout as [Security Area 1](security-area-1.md), but every zone is filled with stronger **Senior** monsters, and the final boss is **Lambda** herself. It also pays extra rewards.

### How to enter

- **Where:** Walk up to the security perimeter at `/navi ba_maison 120/320`. The **Flower Garden Manager** appears.
- **Requirement:** Finish the [Hidden Flower Garden](hidden-flower-garden.md) story instance first ("Security Clearance").
- **Level:** Base Level **180** or higher.
- **Party:** The party leader picks **"Identity Authentication"** and then **"2nd Security Zone."**. Then everyone picks **"Enter Zone"** and **"2nd Security Zone."**.
- **Cooldown:** Entering starts a daily cooldown that resets at **04:00** server time ("Security Clearance - Waiting"). It is **shared with Security Area 1**. After it ends, talk to the manager once to clear it.

### Walkthrough

The run starts when the **party leader** steps onto the entrance point. Lambda announces her security test.

| Zone | Monsters | Exit warp |
|---|---|---|
| 1. Entrance | 16 | `80/196` |
| 2. North garden | 21 | `174/229` |
| 3. East garden | 27 | `254/212` |
| 4. Far east garden | 33 | `297/264` (to the boss room) |

The zones are filled with {{ mob(20623) }}, {{ mob(20625) }} and {{ mob(20627) }}. The next zone spawns when someone takes the warp into it. **Every monster in a zone must die** before its exit warp activates.

### Boss: Lambda

After zone 4, Lambda invites you to her room. Take the warp at `297/264`, walk up to Lambda, and the **party leader** talks to her. {{ mob(20621) }} then attacks.

- **Energy shield:** When she appears, and again at **80%, 60%, 40% and 20%** of her HP, she summons **4 {{ mob(20679) }}** in the corners of the room. She also raises a strong damage-reducing shield.
- Every Guardian Part you destroy weakens the shield. Destroy **all 4** to remove it completely.
- If parts are still standing after **40 seconds**, they disappear and Lambda keeps whatever shield she has left.

When Lambda falls, a warp opens to **Sigma**, who waits at `85/77`.

### Rewards

Talk to **Sigma**:

| Reward | Chance | Notes |
|---|---|---|
| {{ item(1000103) }} ×6 | Always | Requires the "Red Pepper - Lambda Suppression" quest you got on entry |
| {{ item(1000104) }} ×1–5 | 94% | Extra reward for Security Area 2 |
| {{ item(100161) }} | 6% | Replaces the Magical Soapstone |
| 10 [Instance Points](../../content/instances.md) | | When you choose **"I'll leave."**. Counts toward the daily 1,200 cap |

{{ instance_page("security-area-2") }}
