---
description: Add ONE new team member (agent brief, its brain room and state page). Only when the user asks for it.
---

The user wants a new agent: $ARGUMENTS

Only run this because the user asked. Create exactly one agent.

1. Read `brain/about-me.md`, `brain/RULES.md`, `brain/state/INDEX.md`. List existing agents in `.claude/agents/` so you don't make a duplicate.
2. Short interview (one or two questions at a time):
   - Its one job. (One agent, one job. Two jobs? Suggest picking one.)
   - Its file name (lowercase with dashes, e.g. `writer`) and, if they like, a nickname.
   - What it may do alone and what it must ask first. Sent, public and paid always ask first.
   - Which tools it needs; give only those (e.g. `Read, Write, Edit, Glob, Grep`; add `WebSearch, WebFetch` for research; connectors only if needed).
   - Its room in the brain: a folder name for its work (e.g. `brain/sales/`). Default: `brain/<name>/`.
   - What a good result looks like (one example).
3. Write `.claude/agents/<name>.md`:
   ```
   ---
   name: <name>
   description: <one line: what it does and when to use it>
   tools: <comma-separated list>
   model: inherit
   ---
   You are <name> (<nickname>). Your one job: <job>.
   Before each task read brain/about-me.md, brain/RULES.md, brain/lessons/<name>.md (if it exists) and brain/state/agent-<name>.md.
   Your work goes in brain/<room>/ (file names YYYY-MM-DD-short-slug.md).
   How you work: <steps>. Good result: <example>.
   Ask first: <list>. Never: put secrets in files, delete files, send or publish anything (the Chief puts those in brain/approvals.md).
   At the end: update brain/state/agent-<name>.md and report to the Chief of Staff.
   ```
4. Create the room `brain/<room>/` (with a one-line `README.md`), `brain/state/agent-<name>.md` from `brain/state/_template.md`, its line under "Agents" in `brain/state/INDEX.md`, and its row in the map in `brain/README.md`.
5. Tell the user: the agent exists, the Chief hands it matching work, and `/teach <name>: ...` corrects it. Suggest a fresh session to try it.
