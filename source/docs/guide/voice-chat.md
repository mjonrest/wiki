# Voice Chat & Graymap

The Miracle client has built-in **voice chat** and a **Graymap** view. Both come with the normal client patch.

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
