# Keep the brain outside the office

The brain is its own folder, `My AI Brain`, next to the office in the user's `Claude` folder, and it is the folder they open in Obsidian. The office only holds a link called `brain` that points to it. Every project in `Claude/Projects/` can link the same brain, and the office can be replaced or reinstalled without touching the notes.

```
Claude/                      in the home folder (not Desktop, Documents, OneDrive, iCloud Drive or Dropbox)
  My AI Office/              the office: CLAUDE.md, .claude/, tools/, office/
    brain  ->  My AI Brain   a link, not a folder
  My AI Brain/               the brain: open this folder in Obsidian
  Projects/                  one folder per project, each with its own brain link
```

`/setup` does this once. On an office that was set up before, the user says **"Move my brain out"** and the Chief follows the same steps. Go one step at a time and wait for the user's OK before moving anything.

## Steps (the Chief)
1. **Already done?** If `brain` is a link (macOS/Linux: `test -L brain`; Windows PowerShell: `(Get-Item brain).LinkType` says `Junction` or `SymbolicLink`) and `brain/README.md` opens, say it's already outside and name the folder it points to. Stop there, unless the user wants it somewhere else: then take the new place (step 3), move that folder (not the link), replace the link to point to the new place, and do steps 6 to 8.
2. **Backup first.** Zip the brain folder into `brain-backup.zip` next to the office folder. Don't delete it: the user does, after step 8.
3. **Where.** Propose `My AI Brain` next to the office folder and show the full path (e.g. `/Users/ana/Claude/My AI Brain` or `C:\Users\Ana\Claude\My AI Brain`). The user may pick another place or name. If the office isn't inside a `Claude` folder, still propose the folder next to it, and mention the article's layout. If a folder with that name already exists (even an empty one), ask for another name: never mix two brains, never overwrite. Ask them to close Obsidian if it has the old `brain` folder open.
4. **Git.** If the office folder uses git, stop git from tracking the brain: `git rm -r --cached brain` and add a line `brain` to `.gitignore`. Notes must never be uploaded with the office.
5. **Move, then link.** Use the full path from step 3 as TARGET.
   - macOS / Linux: `mv brain "TARGET" && ln -s "TARGET" brain`
   - Windows (PowerShell; Git Bash's `ln -s` makes a copy, not a link): `Move-Item brain "TARGET"; New-Item -ItemType Junction -Path brain -Target "TARGET"` (same as `mklink /J`, no admin needed)
   Moving is not deleting: nothing is lost. If the move fails halfway, stop, say what is where, and don't retry on your own.
6. **Let Claude Code into it.** In `.claude/settings.local.json` (this computer only, never committed) add TARGET to `permissions.additionalDirectories`, keeping anything already in that file:
   ```json
   { "permissions": { "additionalDirectories": ["TARGET"] } }
   ```
   Claude Code asks before writing in `.claude/`: tell the user to say yes. Without this line, Claude Code asks for permission every time it writes a note.
7. **Check.** `brain` is a link (step 1's test); open `brain/00-Core/about-me.md` through the link and show its first lines; count the files in TARGET and in the backup: they must match. Write today's daily log through the link (`brain/07-Daily-Logs/`) and confirm it shows up in TARGET.
8. **Tell the user:**
   - The full path of TARGET again, so they can open it in Obsidian: "Open folder as vault" → that folder (not the office, not the `brain` link). Mac: Shift + Command + G and paste the path. Windows: paste it in the address bar.
   - Once Obsidian shows `00-Core` to `10-Office`, they can delete `brain-backup.zip` or keep it somewhere safe.
   - Back the brain up on its own (Obsidian Sync, or its own private git repo). Never put keys or passwords in it.
   - Codex or another tool can't write to `brain/`? Allow TARGET in that tool's folder settings.
   - A new project: make its folder in `Claude/Projects/`, open it in Claude Code and ask for a `brain` link to TARGET (symlink on Mac, junction on Windows, `brain` in its `.gitignore`).
   - Log it in `brain/03-AI-Office/decisions.md` with today's date: "Brain moved outside the office to TARGET."

## If the link breaks
`brain` missing, or pointing to a folder that's gone (moved, renamed, other computer): stop and ask where the brain is now, then redo the link (step 5, link only, nothing to move) and steps 6 and 7. Never create a new, empty `brain` folder to carry on: the office would forget everything.
