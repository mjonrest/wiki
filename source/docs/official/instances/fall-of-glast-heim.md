# Fall of Glast Heim

## Guide

Fall of Glast Heim (shown in game as *Fogh_Normal* / *Fogh_Hard*) follows Oscar through the cursed castle while time
keeps looping. You clear four rooms of cursed servants and knights, then fight the Cursed King. The materials you
bring back buy and enchant **King Schmidt's** armor, manteau and insignias next to the entrance.

### Entering

- **NPC:** **Oscar** at `/navi glast_01 241/290`.
- **Modes:** Normal or Hard, picked in Oscar's first menu. A party can only have one of them open at a time.
- **Party:** the **party leader** picks the mode and *Create*; everyone then talks to Oscar, picks the same mode and
  *Enter*.
- **Level:** the script has no level check.
- **Cooldown:** Normal and Hard have **separate** cooldowns. Each starts when you enter and ends at the next
  **04:00** server time.
- **Time limit:** 1 hour.

| | Normal | Hard |
|---|---|---|
| Knights | {{ mob(20388) }}, {{ mob(20390) }} | {{ mob(20389) }}, {{ mob(20391) }} |
| Boss | {{ mob(20386) }} | {{ mob(20387) }} |
| Reward | 3 {{ item(25739) }}, 10 Instance Points | 6 {{ item(25740) }}, 20-40 Instance Points |

### Walkthrough

Every room is started by walking up to its trigger (Oscar, or a spot near the entrance in room 1). Once the counted
monsters are dead, Oscar announces it and the party is moved to the next room 5 seconds later.

Every room also spawns **20 "cursed flame"** ({{ mob(1960) }}). They do not count toward clearing the room;
Oscar warns that they are the most troublesome monsters here, so avoid them rather than fight them.

| Room | Kill to continue |
|---|---|
| 1 | 20 {{ mob(20392) }} |
| 2 | 23 Mad Knights and 2 {{ mob(20394) }} |
| 3 | 30 Cursed Knights |
| 4 | 15 Cursed Knights and 15 Mad Knights |

**Boss: the Cursed King**

After room 4 the party is moved to the throne room. Walk up to **Oscar**: he gathers time energy for 10 seconds, pulls
the whole party to him and the Cursed King appears just north. When it dies, Oscar comes back.

### Rewards

Talk to Oscar after the boss dies. He gives the reward in the table above (each player) and sends you back to
`glast_01`. Instance Points count toward the daily cap of 1,200.

### Exchange

The **exchange** NPC at `/navi glast_01 245/296` trades:

| You get | Cost |
|---|---|
| {{ item(15388) }} or {{ item(15389) }} | 5 {{ item(25739) }} + 10 {{ item(6607) }} |
| One insignia: {{ item(32228) }} (STR), {{ item(32232) }} (AGI), {{ item(32231) }} (VIT), {{ item(32229) }} (INT), {{ item(32233) }} (DEX), {{ item(32230) }} (LUK) | 5 {{ item(25740) }} + 5 {{ item(6755) }} |

### Enchanting

The **enchanter** NPC at `/navi glast_01 243/296` adds up to three random enchants to an equipped King Schmidt item,
one per visit, starting from the last slot.

| Item (must be equipped) | Materials (consumed) | 1st and 2nd enchant | 3rd enchant |
|---|---|---|---|
| {{ item(15388) }} | 5 {{ item(25739) }} + 10 {{ item(6608) }} | STR, AGI, VIT, INT, DEX or LUK +3 to +5 | A stat +3 or an armor element ({{ item(29302) }}, {{ item(29303) }}, {{ item(29304) }}, {{ item(29305) }}, {{ item(29306) }}, {{ item(29307) }}, {{ item(29308) }}, {{ item(29309) }}) |
| {{ item(15389) }} | 5 {{ item(25739) }} + 10 {{ item(6608) }} | Fighting Spirit 4-6, Spell 3-5, Sharp 2-4, Expert Archer 3-5, Fatal 1-3 | Same list |
| Insignia, in the **left** accessory slot | 10 {{ item(25740) }} + 40 {{ item(6755) }} | 1st: a stat +3 to +5. 2nd: Fighting Spirit 6-7, Spell 4-5, Sharp 4-5, Expert Archer 4-5, Fatal 2-3 | {{ item(29587) }}, {{ item(29588) }}, {{ item(29589) }}, {{ item(29590) }}, {{ item(29591) }} or {{ item(29592) }} |

{{ instance_page("fall-of-glast-heim") }}
