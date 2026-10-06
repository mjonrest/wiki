# Regenschirm

## Guide

Regenschirm is the Episode 17.1 story memorial in which the rebels take back the Regenschirm laboratory under Lighthalzen. You fight through the guarded lobby, clear the poison gas from the lab wings, rescue the detained researchers and finally face the specimen held in the Central Room.

### Requirements and entry

| | |
|---|---|
| Quest | **Reclaim Regenschirm** (Episode 17.1 main story) |
| NPC | **Rekenber Guard Oscar** at `/navi lighthalzen 55/278` |
| Party | Required. Only the party leader can create the memorial. |
| Time limit | 2 hours |

The leader talks to Oscar and picks **Create 'Regenschirm'**, then everyone talks to him and picks **Enter 'Regenschirm'**.

### Walkthrough

**1. The lobby**

1. Talk to **Aas** at `131/58`. She stays behind to hack the security system and sends you into the hall (`127/67`).
2. A large group of {{ mob(3627) }} is spread over the lobby, the stairs and the two side rooms. Two spots near the lower door and the stairs (`94/68` and `95/93`) spawn extra {{ mob(3622) }} when you walk over them.
3. Kill every Heart Hunter Guard. An **Access Controller** appears at `60/138`. Talk to it to hear Aas over the intercom.
4. Talk to the **Researcher** next to it (`59/132`). He unlocks the door to the hallway.

**2. The poison gas**

1. Opening the door releases more guards and three clusters of **Poisonous Gas** ({{ mob(20352) }}): one in the west wing, one in the east wing and one in the north wing. Each wing's doors stay locked ("Access Denied") until that wing's gas is gone.
2. Clear the **west** gas first. **Est** appears behind the door at `36/211`. Talk to her, then use the **Access Controller** at `26/219` to call Aas.
3. Clear the **east** gas. The four lab doors along `214-216` (at `y` 44, 76, 108 and 136) now open. Rescue the three **Detained Researchers** at `235/143`, `237/108` and `237/71` by talking to each one.
4. Talk to **Aas** at `235/44`. She will not continue until all three researchers have been rescued. She opens the way to the **Central Room**.

The north wing (doors at `186-188/216`) only holds research reports to read. It is optional. The **Scattered Documents** at `241/51` start a side quest.

**3. The Central Room**

1. Click the **Central Room** device at `125/157`. Aas, Est and Goni gather there. Talk to Aas twice, then pick **Enter.** to go inside (`126/164`).
2. Click the **Restrained Specimen** at `125/188`. Then use the four **Control Devices** to release its gravity restraints. They must be pressed **in this order**, each with the right button:

    | Order | Control Device | Button |
    |---|---|---|
    | 1 | Blue device, `144/180` | **Blue** |
    | 2 | Red device, `108/168` | **Red** |
    | 3 | White device, `114/191` | **Yellow** |
    | 4 | Yellow device, `143/168` | **White** |

    A wrong button, or a device used out of order, only makes the specimen cry out. Nothing is reset, so you can simply try again.

3. When the last restraint is released, the specimen breaks free as the **Failed Specimen** (a {{ mob(20353) }}). Kill it.
4. Talk to **Aas** at `127/164` and choose where to go: Einbroch (`/navi einbroch 301/324`) or Lighthalzen (`/navi lighthalzen 54/272`).

### Rewards

Talking to Aas at the end completes **Reclaim Regenschirm**. The memorial gives no items or Instance Points. Since Oscar only lets you in while the quest is active, it can only be done once.

{{ instance_page("regenschirm") }}
