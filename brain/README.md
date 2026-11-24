# The brain

The office's memory. The Chief of Staff (and every agent added later) reads it before working and writes back after. Chats are forgotten; these files are not.

The folders are numbered so they always sort the same way, in Obsidian and in any file list. Keep the numbers; you may rename the words after them (`01-Business` → `01-Bakery`), then update this map.

## Rules
1. **Read first:** `00-Core/about-me.md`, `03-AI-Office/RULES.md`, `10-Office/state/INDEX.md` and the state page for your task.
2. **Work output goes here**, in your room (map below; the Chief uses `10-Office/reports/`, including drafts). Never keep findings only in chat.
3. **Learn once, everyone knows.** Lasting preferences from the user go in `03-AI-Office/decisions.md` (their words + date) and as one line in `03-AI-Office/RULES.md` → My rules. Corrections from `/teach` go in `10-Office/lessons/<agent>.md`. Anything you work out yourself is only a proposal: it goes in `08-Inbox/` and becomes official after the user's yes.
4. **Never overwrite another agent's file.** Append, or make a new dated file.
5. **Sent, public or paid = approval** in `10-Office/approvals.md` first.
6. **Never delete.** Move to `08-Inbox/archive/`.
7. **File names:** `YYYY-MM-DD-short-slug.md`.
8. **No secrets.** No passwords, keys, tokens, card or account numbers anywhere in here.

## Map
| Path | Owner | What lives here |
|---|---|---|
| `00-Core/about-me.md` | chief-of-staff | Who the office works for; office name and Chief's name (filled by `/setup`) |
| `01-Business/` | user | Your main work: clients, offers, how it runs |
| `02-Brand/` | user | Your brand or second line of work (optional) |
| `03-AI-Office/RULES.md` | chief-of-staff | Rules in force: levels, defaults, the user's own rules |
| `03-AI-Office/decisions.md` | chief-of-staff | Append-only log of what the user decided, with their words and the date |
| `04-Personal/` | user | Personal notes you want the office to know (no secrets) |
| `05-Projects/` | everyone | One note per bigger project |
| `06-Research/` | everyone | What was looked up, with sources |
| `07-Daily-Logs/` | chief-of-staff | One short note per day: done and open |
| `08-Inbox/` | user | Drop zone and proposals; the Chief sorts it. `08-Inbox/archive/` holds anything retired |
| `09-Templates/` | chief-of-staff | `state-page.md`, copied for every new state page |
| `10-Office/board.md` | chief-of-staff | Running / waiting / done tasks |
| `10-Office/approvals.md` | chief-of-staff | Items waiting for the user's OK |
| `10-Office/state/` | everyone | `INDEX.md` + one short page per project and per agent |
| `10-Office/lessons/` | everyone | What `/teach` saved, one file per agent |
| `10-Office/reports/` | chief-of-staff | Longer write-ups and summaries |

Each agent added with `/new-agent` gets its own room in `10-Office/` (for example `10-Office/writer/`) and a row here.

This folder is the brain. `/setup` moves it out of the office to its own folder (default: `My AI Brain`, next to the office in your `Claude` folder) and leaves a `brain` link in the office, so the office and your notes stay separate. Works as a plain folder. For linked notes (`[[page-name]]`), install Obsidian, choose "Open folder as vault" and pick this folder (the moved one, not the link). Moving it again later? Say "Move my brain out" so the Chief fixes the link: `.claude/playbooks/brain-outside.md` in the office.
