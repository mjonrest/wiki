# Security Area 1

## Guide

Security Area 1 is the normal daily mode of the Flower Garden's security zone in Varmundt's Mansion (Episode 17.2). The Red Pepper doll **Lambda** wants to "evaluate" the garden's security, so your party fights through four zones of automatic dolls and plants and then defeats **Kappa**. [Security Area 2](security-area-2.md) is the harder version on the same map.

### How to enter

- **Where:** Walk up to the security perimeter at `/navi ba_maison 120/320`. The **Flower Garden Manager** appears.
- **Requirement:** Finish the [Hidden Flower Garden](hidden-flower-garden.md) story instance first ("Security Clearance").
- **Level:** Base Level 150 or higher.
- **Party:** The party leader picks **"Identity Authentication"** and then **"1st Security Zone."**. Then everyone picks **"Enter Zone"** and **"1st Security Zone."**.
- **Cooldown:** Entering starts a **4 hour** cooldown ("Security Clearance - Waiting"). It is **shared with Security Area 2**. After it ends, talk to the manager once to clear it.

### Walkthrough

The run starts when the **party leader** steps onto the entrance point. An automatic doll arrives with a warning from Sigma, and Lambda's security test begins.

| Zone | Monsters | Exit warp |
|---|---|---|
| 1. Entrance | 16 | `80/196` |
| 2. North garden | 21 | `174/229` |
| 3. East garden | 28 | `254/212` |
| 4. Far east garden | 31 | `297/264` (to the boss room) |

Each zone is filled with **Flower Garden Watchers**: {{ mob(20622) }}, {{ mob(20624) }} and {{ mob(20626) }}. The next zone spawns when someone takes the warp into it. **Every monster in a zone must die** before its exit warp activates.

### Boss: Kappa

After zone 4, Kappa opens her room. Take the warp at `297/264`, walk up to Kappa, and the **party leader** talks to her. {{ mob(20620) }} then attacks.

- **Energy shield:** When she appears, and again at **80%, 60%, 40% and 20%** of her HP, she summons **4 {{ mob(20679) }}** in the corners of the room. She also raises a strong damage-reducing shield.
- Every Guardian Part you destroy weakens the shield. Destroy **all 4** to remove it completely.
- If parts are still standing after **40 seconds**, they disappear and Kappa keeps whatever shield she has left. Split up and break the parts quickly.

When Kappa falls, a warp opens to **Sigma**, who waits at `85/77`.

### Rewards

Talk to **Sigma**:

| Reward | Notes |
|---|---|
| {{ item(1000103) }} ×6 | Requires the "Red Pepper - Kappa Suppression" quest you got on entry, so you must have been in the room when Kappa died |
| 10 [Instance Points](../../content/instances.md) | When you choose **"I'll leave."**. Counts toward the daily 1,200 cap |

{{ instance_page("security-area-1") }}
