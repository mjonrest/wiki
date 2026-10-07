# 2nd OS Search

## Guide

The 2nd OS Search is the repeatable follow-up to the OS Occupation operation from the Episode 17.1 story. The
Rebellion sends your unit back into the OS facility to clear six sectors of A013 mutants and then put down the
S-class mutant {{ mob(20346) }}.

### Entering

- **Requirement:** you must have finished the **OS Occupation** operation (talk to **Est** at
  `/navi sp_cor 163/56` to start it). After that, the **Operation Officer** appears next to her at
  `/navi sp_cor 160/55`. He only shows up after you walk into that spot.
- **Party:** you must be in a party. The **party leader** talks to the Operation Officer and picks *Prepare 2nd OS
  Search*, then every member talks to him and picks *Enter*.
- **Quest:** the first time, the Operation Officer gives you *More Search Operations*. You need this quest active to
  get the reward at the end. He gives it again on your next visit after you have turned it in.
- **Cooldown:** entering gives you *Operation Waiting*, a daily cooldown that resets at **04:00** server time. Once it has passed, talk to the
  Operation Officer to clear it.
- **Time limit:** the instance lasts **2 hours**.

!!! note
    The 2nd OS Search uses the same facility map as OS Occupation, but you start at the other end, in the
    south-east (`1@os_a 335/34`).

### Walkthrough

1. The **party leader** walks onto the starting point. This starts the search, and the first two groups of
   mutants spawn at once.
2. Each group is a mix of {{ mob(20348) }}, {{ mob(20349) }} and {{ mob(20350) }}, labelled **CP1** to **CP6**
   by sector. Later groups are larger.
3. Every 10 seconds an announcement shows how many mutants are left. When the current group is dead the sector
   is reported **secured** and the next group spawns further into the facility.
4. The poison gas cloud near `1@os_a 253/107` is removed when the fifth group (CP5) spawns.
5. After the sixth group is cleared, **CP7 Miguel** appears at `1@os_a 205/188`.

| Group | Around | Mutants |
| --- | --- | --- |
| CP1 + CP2 (spawn together) | `1@os_a 270/90` and `1@os_a 257/72` | 9 + 7 |
| CP3 | `1@os_a 205/82` | 14 |
| CP4 | `1@os_a 214/130` | 15 |
| CP5 | `1@os_a 250/157` | 14 |
| CP6 | `1@os_a 210/186` | 22 |
| CP7 | `1@os_a 205/188` | {{ mob(20346) }} |

### Miguel

- Once Miguel drops to **70% HP**, he surrounds himself with **4 {{ mob(20351) }}** (7 cells away to the north,
  south, east and west), and moves them with him every time he walks.
- From **30% HP** he uses **8** Manholes: 4 more are added on the diagonals.
- The Manholes only move when Miguel moves, so holding him in one spot keeps them in place.

When he dies, the summons are removed and the **Operation Officer** appears at `1@os_a 187/195`.

### Rewards

Talk to the **Operation Officer** inside the instance. Each player with *More Search Operations* active receives:

| Reward | Amount |
| --- | --- |
| Base EXP | 150,000 |
| Job EXP | 150,000 |
| {{ item(25669) }} | 5 |
| {{ item(25723) }} | 1 |

Talk to him again and pick *Go Out* to return to `sp_cor`.

!!! tip
    If you forgot to pick up *More Search Operations* before entering, you get no reward for the run. Talk to the
    Operation Officer outside first.

{{ instance_page("2nd-os-search") }}
