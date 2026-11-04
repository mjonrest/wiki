# Voice Chat, Graymap & Stats

The Miracle client has built-in **voice chat**, a **Graymap** view and a **Player Statistics** window. All three
come with the normal client patch.

## Signing in to voice chat

You are signed in on your own when you log in, and the server says **"Voice chat connected."**

If you play two game clients on the same internet connection, the server can't tell them apart. The screen then
shows `Voice: click the mic, or type @voice CODE`. Click the mic on the voice bar once in each client.

## The voice bar

A small bar sits at the bottom right of the game screen, next to the chat tabs.

- **Speaker icon:** turns all voices off and on.
- **Mic icon:** mutes your mic. It turns green while you talk.
- **Right-click the mic icon:** disconnects your microphone completely, so Windows shows no app using it.
  The icon turns grey with a red X. Click or right-click it again to reconnect. Listening still works while the
  mic is disconnected, and the game remembers it the next time you start.
- **Normal / Party / Guild / Room / Whisper:** pick who hears you. **Room** is the chat room you are sitting in.
  **Whisper** asks for a character name (click Whisper again, or right-click it, to change the name).
- Right-click anywhere else on the bar to open Voice Settings. Drag the bar by its edges to move it.

While someone is talking, their name shows near the top right of the game window. `/exall` (block all whispers)
also blocks voice whispers.

## Voice Settings (Ctrl+Shift+V)

| Tab | What it has |
|---|---|
| **Voice** | Push to talk or open mic, the push-to-talk key (Mouse 4 by default), who you talk to, the mic level meter, mic and speaker volume, an "only send when I speak" gate for open mic, and on/off switches. Turning voice chat off also releases the mic. |
| **Players** | Everyone you heard recently. Mute anyone or change their volume. |
| **Devices** | Which microphone and speakers to use, and the **Disconnect microphone / Reconnect microphone** button. |

The push-to-talk key and the shortcuts only work while the game window has focus. There is no echo cancelling, so
use headphones on open mic. Settings are saved in `miracle_voice.ini` in the game folder.

## Graymap

A **Graymap** button sits under the Cash Shop button at the top right of the screen.

- **Click** it to switch Graymap on or off. It replaces the 3D ground, water and buildings with flat coloured
  cells, so you can see exactly where you can walk. Players, monsters, NPCs and skill effects are still drawn.
- **Right-click** it, or press **Ctrl+Shift+G**, to pick the colours. **Drag** it to move it.

| Colour | Cells |
|---|---|
| Walkable | Cells you can walk on |
| Unwalkable | Walls and objects |
| Water | Walkable water |
| Shootable wall | Cells you can't walk on but can shoot over |
| Grid lines | The outline of every cell |

## Player Statistics (Ctrl+Shift+S)

A **Stats** button sits under the Graymap button. **Click** it, or press **Ctrl+Shift+S**, to open the Player
Statistics window. **Drag** the button to move it. The window works whether voice chat is on or off.

The tabs on the left show everything about your character. The numbers are live: they update every few seconds
while the window is open, so you can swap gear and watch them change.

| Tab | What it shows |
|---|---|
| **Overview** | Your stats, ATK/MATK, DEF/MDEF, HIT, FLEE, CRIT, ASPD, traits for 4th jobs, and your Combat Power total |
| **Combat Power** | The full [@cp](commands.md#cp) breakdown |
| **Bonuses** | Stat, HP/SP, ATK/MATK and trait % bonuses |
| **Offense** | Damage against race, element, size and class, ignore DEF/MDEF |
| **Resist** | Damage reduction, element/race/size resist and status resists |
| **Skills** | Cast time, delay, cooldown, per-skill damage and SP cost |
| **Procs** | Autospells, autobonus, chances to cause statuses, HP/SP drain |
| **EXP & Drops** | EXP and drop bonuses, extra drops, healing item bonuses and regen |

Scroll with the mouse wheel, the arrow keys or Page Up/Down. **Esc** closes the window.

### If it says "Not signed in"

The window signs in the same way voice chat does. If it shows `Not signed in: type @voice CODE in game chat, or
relog`, either type that `@voice` line in chat or log out and back in. This happens when two game clients play on
the same internet connection.

### Background pictures

You can put your own picture behind the window. Copy any `.png`, `.jpg` or `.bmp` into the
`plugins\stats_backgrounds` folder in your game folder. Any size works; it is scaled to fill the window and cropped
around the middle, so a picture of about 520x440 or bigger with the subject in the centre looks best.

- The **Background** button picks a picture, sets how see-through the text panels are, and opens the folder.
- The **<** and **>** buttons step through your pictures.

!!! tip "No client window?"
    Type `@mystats` (or `@playerstats`) to see the same tabs in an NPC dialog. See [Commands](commands.md#mystats).
