---
description: Save a correction as a lasting rule for the Chief or a named agent. Usage /teach [agent-name:] what to do differently
argument-hint: "[agent-name:] the correction"
---

The user is teaching you: $ARGUMENTS

1. Work out who it is for. If it starts with an agent name and a colon (e.g. `writer: shorter intros`), it is for that agent; check `.claude/agents/<name>.md` exists; if it doesn't, say so and offer to save the lesson for the Chief. Otherwise it is for the Chief (`chief-of-staff`). If the correction is empty or unclear, ask what should change.
2. Rewrite it as one clear rule line: what to do (or not do), and when. Keep the user's own words in quotes.
3. Append it to `brain/10-Office/lessons/<name>.md` (create the file with a `# Lessons for <name>` heading if missing) as:
   `- YYYY-MM-DD — <rule>. ("<user's words>")`
   If it contradicts an older line, mark the old line `(replaced YYYY-MM-DD)` instead of deleting it.
4. If it is a rule for everyone (safety, approvals, tone across all work), also add it to "My rules" in `brain/03-AI-Office/RULES.md` and log it in `brain/03-AI-Office/decisions.md`.
5. Show the saved line and confirm it applies from now on.
