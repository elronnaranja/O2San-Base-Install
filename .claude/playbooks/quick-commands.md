# Quick commands

Short things the user can say. The Chief does the matching action.

| Say | Chief does |
|---|---|
| "Status" | One line per row of `brain/state/INDEX.md` that changed or waits on the user, plus what's Running on `brain/board.md`. |
| "What needs me?" | Every Pending row in `brain/approvals.md` and every "waiting on <user>" line in the state pages. |
| "approve A-00X" / "reject A-00X" | Marks the row decided (`unchanged` / `changed`), then does or drops the action. |
| "Sort the inbox" | Files everything in `brain/inbox/` into the right state page or report; asks about anything unclear. |
| "Stop all" / "Resume" | Stops every running agent and waits / carries on. |
