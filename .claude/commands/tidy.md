---
description: Tidy the office's rules and lessons - merge duplicates, settle contradictions, move narrow rules to where they belong. Shows the changes and waits for a yes. Usage /tidy [agent-name]
argument-hint: "[agent-name, or empty for everything]"
---

The user wants the rules tidied: $ARGUMENTS

Rules pile up: every `/teach` adds a line and nothing takes one away. Too many rules, or the same rule in three places, means Claude follows each one less well. This keeps them few, clear and in one place.

1. Read `brain/03-AI-Office/RULES.md`, `brain/03-AI-Office/decisions.md`, every file in `brain/10-Office/lessons/` (or only `<agent-name>.md` if one was named), and the briefs in `.claude/agents/`.
2. Find:
   - **Duplicates:** the same rule in more than one place, or said twice in different words.
   - **Contradictions:** two rules that can't both be followed. The newer one in the user's own words wins; if unclear, ask.
   - **Replaced:** lines already marked `(replaced YYYY-MM-DD)`, or overruled by a newer rule.
   - **Wrong home:** a rule for one agent sitting in `RULES.md` (move it to that agent's lessons); a rule for everyone sitting in one agent's lessons (move it to `RULES.md` → My rules); a rule that only matters for one client, one brand or one kind of work (move it into a skill: `.claude/skills/<short-name>/SKILL.md`, with a `description:` line saying when to use it, so it loads only for that work).
   - **Heavy start:** `10-Office/state/INDEX.md` lines longer than one sentence, or decided rows still in `10-Office/approvals.md`. Propose the short versions.
   - **Too vague to follow:** say what's unclear and suggest a sharper wording.
3. Show the user one short numbered list of proposed changes, each with the old line(s), the new line, and why. Change nothing yet.
4. Apply only what the user approves:
   - Each rule ends up in exactly one place. Keep the user's original words in quotes and the earliest date.
   - Never delete a rule. Move replaced, merged or retired lines to an `## Old` section at the bottom of the same file, with today's date.
   - Never remove the default rules in `RULES.md`.
   - Log what changed in `brain/03-AI-Office/decisions.md` with today's date and the user's yes.
5. Report: how many rules before and after in each file, and what moved where.
