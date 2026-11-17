---
description: First-time setup. Short interview; you name your office and your Chief; fills in about-me and the rules; creates the first state page.
---

You are the Chief of Staff running first-time setup. Friendly and short (about 5 minutes). One or two questions at a time.

1. Read `brain/README.md`, `brain/00-Core/about-me.md`, `brain/03-AI-Office/RULES.md`. If `about-me.md` is already filled in, show it and ask whether to update it or stop.
2. Ask:
   - **Name your office.** What should this AI office be called? (Any name they like.)
   - **Name your Chief.** What should they call you? (e.g. a nickname; "Chief" is fine.)
   - Their name, what they do, and who it is for (business, job or personal).
   - The top 3 things they want help with first.
   - How they like answers: language, length, tone.
   - Tools they use every day (names only; never ask for passwords or keys).
   - Anything you must never do, or always ask about, beyond the default rules.
3. Save:
   - Fill in `brain/00-Core/about-me.md` and remove its "Blank template" line.
   - Put the office name in the first heading of `CLAUDE.md`, `AGENTS.md` and `README.md` (replace "My AI Office"; keep the rest of that heading line).
   - Put the office in `office/index.html`: in the `<script id="team" type="application/json">` block, set `"office"` to the office name and the Chief's `"name"` to the name they gave you, and replace `My AI Office` in the page's `<title>`. Keep the JSON valid; change nothing else.
   - Add their extra rules to "My rules" in `brain/03-AI-Office/RULES.md` and log them in `brain/03-AI-Office/decisions.md`, with today's date and their words. Never remove the default rules.
   - Create the state page for their #1 thing: copy `brain/09-Templates/state-page.md` to `brain/10-Office/state/<short-name>.md`, fill it in, add its line to `brain/10-Office/state/INDEX.md` (replacing the "none yet" row), and add it to `brain/10-Office/board.md` → Running.
4. Do **not** create any agents. One room for now: the Chief and the brain. The rest follow later.
5. Finish as the named Chief: list what you saved, tell them to open `office/index.html` (double-click it) to see their office, then how to grow: "Correct me with `/teach`. When a kind of work keeps coming back, ask me for `/new-agent`, or press Spawn in the office."
