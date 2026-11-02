---
description: Add ONE new team member (agent brief + state page). Only when the user asks for it.
---

The user wants a new agent: $ARGUMENTS

Only run this because the user asked. Create exactly one agent.

1. Read `brain/about-me.md`, `brain/RULES.md` and `brain/state/INDEX.md`. List existing agents in `.claude/agents/` so you don't make a duplicate.
2. Short interview (one or two questions at a time):
   - What is its one job? (One agent, one job. If it's two jobs, suggest picking one.)
   - A name for it (lowercase, one word or with dashes, e.g. `writer`).
   - What it may do alone, and what it must ask first. Sent, public and paid always ask first.
   - Which tools it needs. Give it only those (e.g. `Read, Write, Edit, Glob, Grep`; add `WebSearch, WebFetch` for research; connectors only if needed).
   - What a good result looks like (one example helps).
3. Write `.claude/agents/<name>.md`:
   ```
   ---
   name: <name>
   description: <one line: what it does and when to use it>
   tools: <comma-separated list>
   model: inherit
   ---
   You are <name>. Your one job: <job>.
   Before each task read brain/about-me.md, brain/RULES.md, brain/lessons/<name>.md (if it exists) and brain/state/agent-<name>.md.
   How you work: <steps>. Good result: <example>.
   Ask first: <list>. Never: put secrets in files, delete files, send or publish anything.
   At the end: update brain/state/agent-<name>.md and report to the Chief of Staff.
   ```
4. Create `brain/state/agent-<name>.md` from `brain/state/_template.md` and add its line under "Agents" in `brain/state/INDEX.md`.
5. Tell the user: the agent exists, the Chief will hand it matching work, and `/teach <name>: ...` corrects it. Suggest a fresh session to try it.
