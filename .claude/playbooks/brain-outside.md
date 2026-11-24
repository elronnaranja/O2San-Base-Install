# Keep the brain outside the office

The brain is its own folder, next to the office, and it is the folder you open in Obsidian. The office only holds a link called `brain` that points to it. So the office (agents, commands, tools) and the memory stay separate: you can replace or reinstall the office without touching your notes, and open the brain in Obsidian without the office's files in it.

```
Claude/                      (or wherever the office folder lives)
  My AI Office/              the office: CLAUDE.md, .claude/, tools/, office/
    brain  ->  ../Brain      a link, not a folder
  Brain/                     the brain: open this folder in Obsidian
```

`/setup` does this once. On an office that was set up before, the user says **"Move my brain out"** and the Chief follows the same steps.

## Steps (the Chief)
1. **Already done?** If `brain` is a link (macOS/Linux: `test -L brain`; Windows PowerShell: `(Get-Item brain).LinkType` says `Junction` or `SymbolicLink`) and `brain/README.md` opens, say it's already outside and name the folder it points to. Stop there, unless the user wants it somewhere else: then take the new place (step 2), close Obsidian (step 3), move that folder (not the link), replace the link to point to the new place, and do steps 5 to 7.
2. **Where.** Propose the folder next to the office, called `Brain` (full path, e.g. `/Users/ana/Claude/Brain` or `C:\Users\Ana\Claude\Brain`). The user may pick another place or name. If a folder with that name already exists (even an empty one), ask for another name: never mix two brains, never overwrite.
3. **Close Obsidian** if it has the old `brain` folder open (ask the user, then wait for "done").
4. **Move, then link.** Use the full path from step 2 as TARGET.
   - macOS / Linux: `mv brain "TARGET" && ln -s "TARGET" brain`
   - Windows (PowerShell; Git Bash's `ln -s` makes a copy, not a link): `Move-Item brain "TARGET"; New-Item -ItemType Junction -Path brain -Target "TARGET"`
   Moving is not deleting: nothing is lost. If the move fails halfway, stop, say what is where, and don't retry on your own.
5. **Let Claude Code into it.** In `.claude/settings.local.json` (this computer only, never committed) add TARGET to `permissions.additionalDirectories`, keeping anything already in that file:
   ```json
   { "permissions": { "additionalDirectories": ["TARGET"] } }
   ```
   Claude Code asks before writing in `.claude/`: tell the user to say yes. Without this line, Claude Code asks for permission every time it writes a note.
6. **Check.** `brain` is a link (step 1's test), `brain/README.md` and `TARGET/README.md` are the same file, and a test line written to `brain/07-Daily-Logs/` shows up in `TARGET/07-Daily-Logs/` (write the real daily log, not a throwaway file).
7. **Tell the user:**
   - Open Obsidian → "Open folder as vault" → pick TARGET.
   - The brain is now outside the office: back it up on its own (Obsidian Sync, iCloud, OneDrive, Google Drive, or its own git repo). Never put keys or passwords in it.
   - Codex or another tool can't write to `brain/`? Allow TARGET in that tool's folder settings.
   - The office folder is a git repo (it was cloned)? Git now lists the brain files as removed: expected, they're in TARGET. Don't commit the link unless the user wants to.
   - Log it in `brain/03-AI-Office/decisions.md` with today's date: "Brain moved outside the office to TARGET."

## If the link breaks
`brain` missing, or pointing to a folder that's gone (moved, renamed, other computer): stop and ask where the brain is now, then redo steps 4 to 6 with that path (link only, nothing to move). Never create a new, empty `brain` folder to carry on: the office would forget everything.
