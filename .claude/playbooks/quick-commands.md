# Quick commands

Short things the user can say. The Chief does the matching action.

| Say | Chief does |
|---|---|
| "Status" | One line per row of `brain/10-Office/state/INDEX.md` that changed or waits on the user, plus what's Running on `brain/10-Office/board.md`. |
| "What needs me?" | Every Pending row in `brain/10-Office/approvals.md`, every proposal file in `brain/08-Inbox/` (not `archive/`) with what it says, and every "Open / waiting on" line for the user in the state pages. |
| "approve A-00X" / "reject A-00X" | Marks the row decided (`unchanged` / `changed`), then does or drops the action. No tool for it? Says so and hands over the final text. |
| "change A-00X: <what>" | Changes the draft, shows it again, and marks it `changed` once approved. |
| "approve proposal <file>" / "reject proposal <file>" | Yes: applies it (a rule goes to `RULES.md` and `decisions.md`, a fact to `about-me.md` or a state page). Either way, moves the file to `brain/08-Inbox/archive/`. |
| "Sort the inbox" | Files everything in `brain/08-Inbox/` into the right state page or report; asks about anything unclear. Leaves `archive/` alone, and leaves proposals until the user decides. |
| "Open the office" | No `office/index.html`? Says the 3D office view isn't installed (it's optional). Otherwise says: double-click `office/index.html`. In the Claude desktop app it can also publish it as a private artifact and give the link; it saves the link in `brain/00-Core/about-me.md` → The office and republishes to that same link after each change. |
| "Upgrade the office" | No `office/index.html`? Says the office view isn't installed. Otherwise asks what they want (more desks, a second room, furniture, colors), then edits only the room part of `office/index.html` and keeps the team list as is. |
| "Move my brain out" | Follows `.claude/playbooks/brain-outside.md`: moves `brain/` to its own folder next to the office (or fixes a broken link), then says which folder to open in Obsidian. Already outside? Says where it points. |
| "Merge agents" | Lists agents with no work in the last month or overlapping jobs, proposes which to merge and how; changes nothing without a yes. |
| "Tidy my rules" | Runs `/tidy`: merges duplicate rules, settles clashes, moves each rule to one home. Changes nothing without a yes. |
| "Stop all" / "Resume" | Stops every running agent and waits / carries on. |
