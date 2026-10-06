# Thor Military Base

## Guide

Thor Military Base is a story instance from the Episode 18 main quest. You sneak into the Thor army camp with Maram, break through four locked barricades while avoiding watchtowers, and gather documents for Miriam. It can only be done once, at the right point of the main story.

### Requirements and entry

| | |
|---|---|
| **NPC** | Maram: `/navi que_thr 133/53` |
| **Prerequisite** | Episode 18 main quest, at the step where Maram asks you to infiltrate the base |
| **Party** | Required. Only the party leader can create the instance; party members can enter it |
| **Equipment** | {{ item(400127) }} (received at the start of Episode 18), worn on the upper head for the final step |
| **Time limit** | 60 minutes (closes after 5 minutes with nobody inside) |
| **Repeatable** | No, Maram only opens the base while you are on this story step |

1. Talk to Maram. The party leader picks **Apply for entry to Thor Military Base**.
2. Everyone talks to Maram again and picks **Enter Thor Military Base**.

### Walkthrough

The camp is patrolled by 18 {{ mob(21309) }} and 18 {{ mob(21310) }} placed at random.

#### Watchtowers

There are 17 **Watchtowers** spread through the base. Anyone who comes within 7 cells of a tower sets off an alarm, and 3 {{ mob(21309) }} plus 3 {{ mob(21310) }} spawn next to it. This happens every time someone walks into range, and being hidden does not stop it. Give the towers a wide berth.

#### Lock Devices

Four barricades block the path. Click any **Lock Device** of a barricade and wait out the 10 second progress bar to remove the whole barricade.

| Barricade | Location |
|---|---|
| 1 | `1@tcamp 138/216` |
| 2 | `1@tcamp 136/145` |
| 3 | `1@tcamp 223/109` |
| 4 | `1@tcamp 80/99` |

#### Documents and Miriam

Opening the fourth barricade reveals five **Piles of documents** in the west part of the base, at `32/100`, `49/123`, `29/86`, `60/122` and `31/84`. Each pile gives every player one {{ item(1000409) }}.

1. Collect all 5 {{ item(1000409) }}.
2. Put on {{ item(400127) }} and talk to **Miriam** (`34/100`). She takes the 5 files and the story moves on.
3. Talk to **Maram** next to her (`32/102`) to finish and get warped to `wolfvill 162/154`.

!!! tip
    Only one player needs to hand the files to Miriam. After that, every party member who is on this step of the main quest gets the reward from Maram.

### Rewards

| Reward | Who |
|---|---|
| {{ item(1000405) }} x50 | Each player on this step of the Episode 18 main quest, from Maram at the end |

{{ instance_page("thor-military-base") }}
