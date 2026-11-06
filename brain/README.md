# The brain

The office's memory. The Chief of Staff (and every agent added later) reads it before working and writes back after. Chats are forgotten; these files are not.

## Rules
1. **Read first:** `about-me.md`, `RULES.md`, `state/INDEX.md` and the state page for your task.
2. **Work output goes here**, in your room (map below; the Chief uses `reports/`, including drafts). Never keep findings only in chat.
3. **Learn once, everyone knows.** Lasting preferences from the user go in `decisions.md` (their words + date) and as one line in `RULES.md` → My rules. Corrections from `/teach` go in `lessons/<agent>.md`. Anything you work out yourself is only a proposal: it goes in `inbox/` and becomes official after the user's yes.
4. **Never overwrite another agent's file.** Append, or make a new dated file.
5. **Sent, public or paid = approval** in `approvals.md` first.
6. **Never delete.** Move to `inbox/archive/`.
7. **File names:** `YYYY-MM-DD-short-slug.md`.
8. **No secrets.** No passwords, keys, tokens, card or account numbers anywhere in here.

## Map
It starts with one room: the Chief's. Each agent added with `/new-agent` gets its own room and a row here.

| Path | Owner | What lives here |
|---|---|---|
| `about-me.md` | chief-of-staff | Who the office works for; office name and Chief's name (filled by `/setup`) |
| `RULES.md` | chief-of-staff | Rules in force: levels, defaults, the user's own rules |
| `decisions.md` | chief-of-staff | Append-only log of what the user decided, with their words and the date |
| `board.md` | chief-of-staff | Running / waiting / done tasks |
| `approvals.md` | chief-of-staff | Items waiting for the user's OK |
| `state/` | everyone | `INDEX.md` + one short page per project and per agent (copy `_template.md`) |
| `lessons/` | everyone | What `/teach` saved, one file per agent |
| `reports/` | chief-of-staff | Longer write-ups and summaries |
| `inbox/` | user | Drop zone; the Chief sorts it. `inbox/archive/` holds anything retired |

Works as a plain folder. For linked notes (`[[page-name]]`), install Obsidian, choose "Open folder as vault" and pick this `brain` folder.
