---
description: Add ONE new team member (agent brief, its brain room, state page, and a desk in the office). Only when the user asks for it. Usage /new-agent [Name] [(look 12345)] [— its one job]
argument-hint: "[Name] [(look 12345)] [— its one job]"
---

The user wants a new agent: $ARGUMENTS

Only run this because the user asked (typing it, or pasting the command from the office's Spawn button). Create exactly one agent.

0. Check the team first: if an existing agent in `.claude/agents/` could take this work, say so and suggest teaching that agent instead. Most offices need 3 to 7 agents (`RULES.md` 11). Go ahead if the user still wants a new one.
1. Read `brain/00-Core/about-me.md` (still the blank template? Say `/setup` comes first and ask whether to go on anyway), `brain/03-AI-Office/RULES.md`, `brain/10-Office/state/INDEX.md`. List existing agents in `.claude/agents/` so you don't make a duplicate.
2. Read what was given:
   - **Name:** the first word(s) before `(look …)` or `—`. None given, or the words read like a job rather than a name ("writes my newsletter")? Treat them as the job and pick a random name from the `NAMES` list in `office/index.html` that no agent uses yet (as a name or a file name). Tell the user they can change it.
   - **Look:** the number in `(look 12345)`. None given? Pick a random whole number from 10000 to 99999. This number sets the agent's random look and desk in the office.
   - **Job:** the text after `—`, if any.
3. Short interview, one or two questions at a time, skipping what is already given:
   - Its one job. (One agent, one job. Two jobs? Suggest picking one.)
   - What it may do alone and what it must ask first. Sent, public and paid always ask first.
   - Which tools it needs; give only those (e.g. `Read, Write, Edit, Glob, Grep`; add `WebSearch, WebFetch` for research; connectors only if needed).
   - What a good result looks like (one example).
   Write the brief's `description` and "How you work" steps yourself from these answers, and show the brief to the user when it's done.
   File name: the name in lowercase with dashes (`Mochi` → `mochi`). Room: `brain/10-Office/<file-name>/` unless the user wants another.
4. Write `.claude/agents/<file-name>.md`. Claude Code always asks before it writes inside `.claude/`; tell the user to expect that prompt and to approve it. If it wasn't approved, say so plainly and offer to try again: without that file the agent can't work.
   ```
   ---
   name: <file-name>
   description: <one line: what it does and when to use it>
   tools: <comma-separated list>
   model: inherit
   ---
   You are <Name>. Your one job: <job>.
   Before each task read brain/00-Core/about-me.md, brain/03-AI-Office/RULES.md, brain/10-Office/lessons/<file-name>.md (if it exists), brain/10-Office/state/INDEX.md, brain/10-Office/state/agent-<file-name>.md and the state page for the task.
   Your work goes in brain/10-Office/<file-name>/ (file names YYYY-MM-DD-short-slug.md).
   How you work: <steps>. Good result: <example>.
   Ask first: <list>. Anything sent, public or paid you only draft: the Chief puts it in brain/10-Office/approvals.md for the user's yes. Never: put secrets in files or delete files.
   At the end: update your state page and its line in brain/10-Office/state/INDEX.md, and report to the Chief of Staff.
   ```
5. Create the room `brain/10-Office/<file-name>/` (with a one-line `README.md`), `brain/10-Office/state/agent-<file-name>.md` from `brain/09-Templates/state-page.md`, its line under "Agents" in `brain/10-Office/state/INDEX.md`, and its row in the map in `brain/README.md` (after the last `10-Office/` row; Owner = the file name).
6. **Add it to the office.** In `office/index.html`, inside the `<script id="team" type="application/json">` block, append one entry at the end of `"agents"` (keep the JSON valid: a comma after the previous entry, no comment lines):
   `{ "id": "<file-name>", "name": "<Name>", "title": "<its one job, 2-5 words>", "seed": <look number> }`
   Never change or reorder the entries already there (that would move everyone's desk). The page gives it a random free desk and look from the seed. If `brain/00-Core/about-me.md` has an office page link, publish the office again to that same link.
7. Tell the user: the agent exists, it has its own table in the office (reload `office/index.html`; it brings its own table, up to 9; past that it stands until they say "upgrade the office"), the Chief hands it matching work, and `/teach <file-name>: ...` corrects it. Suggest a fresh session to try it.
