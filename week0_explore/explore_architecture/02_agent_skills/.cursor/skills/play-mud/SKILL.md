---
name: play-tbamud
description: Play tbaMUD (a CircleMUD variant) running on localhost:4000 using the existing dummy/helloworld character. Use when the user asks to play, explore, or interact with the MUD, or to log in and run in-game commands like look, walk, or fight.
---

# Play tbaMUD

## Connection

- The MUD server runs at `localhost:4000` (tbaMUD, a CircleMUD variant).
- Player credentials: `dummy` / `helloworld`.
- Use `scripts/mud_client.py` to manage the connection instead of raw `telnet`/`nc` calls — it handles the socket, login sequence, and reading output for you.

## Usage

Run one or more in-game commands in a single session:

```bash
python3 scripts/mud_client.py "look" "score" "exits"
```

- The first arguments are commands sent after login completes.
- Each command's output is printed with a `>>> <command>` header so you can read the game's response.
- The script logs in automatically using the credentials above before sending your commands.
- The connection closes after the last command; run the script again to start a new session (character location/state persists on the MUD server between sessions).

## Memory

Track what you learn across turns in these files (create them if missing):

- `data/player.md` — character state: location, health, mana, moves, status.
- `data/world.md` — locations, NPCs, and shops discovered, with exits.

Update both files after each session using the command output, so future sessions don't need to rediscover the same rooms.

## Notes

- If a command produces no visible output, wait and re-send `look` to re-sync with the current room.
- If you get logged out or lost, re-run the login flow — the character will resume at Temple of Midgaard (or their rented location if they used `offer`/`rent` at an Inn).
