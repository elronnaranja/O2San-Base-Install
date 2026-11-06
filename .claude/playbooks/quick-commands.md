# Quick commands

Short things the user can say. The Chief does the matching action.

| Say | Chief does |
|---|---|
| "Status" | One line per row of `brain/state/INDEX.md` that changed or waits on the user, plus what's Running on `brain/board.md`. |
| "What needs me?" | Every Pending row in `brain/approvals.md`, every proposal file in `brain/inbox/` (not `archive/`) with what it says, and every "Open / waiting on" line for the user in the state pages. |
| "approve A-00X" / "reject A-00X" | Marks the row decided (`unchanged` / `changed`), then does or drops the action. No tool for it? Says so and hands over the final text. |
| "change A-00X: <what>" | Changes the draft, shows it again, and marks it `changed` once approved. |
| "approve proposal <file>" / "reject proposal <file>" | Yes: applies it (a rule goes to `RULES.md` and `decisions.md`, a fact to `about-me.md` or a state page). Either way, moves the file to `brain/inbox/archive/`. |
| "Sort the inbox" | Files everything in `brain/inbox/` into the right state page or report; asks about anything unclear. Leaves `archive/` alone, and leaves proposals until the user decides. |
| "Stop all" / "Resume" | Stops every running agent and waits / carries on. |
