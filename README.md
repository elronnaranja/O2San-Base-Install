# AI Office Base

A small starter for your own AI team in Claude Code: one **Chief of Staff** and a simple memory folder. Start with one; add team members only when you need them.

## Install (3 steps)
1. **Get the folder.** Clone it (`git clone <repo-url> my-ai-office`) or download the ZIP and unzip it.
2. **Open the folder in Claude Code** (desktop app: Code tab → open folder; or run `claude` inside it).
3. **Type `/setup`.** Answer a few questions. The Chief saves who you are, your rules and your first project.

That's it. Ask for anything in plain words; the Chief plans it, does it, checks it, and asks before anything is sent, posted or paid.

## Grow it
- **`/teach <what to change>`** — corrected the Chief? Save it so it sticks. For an agent: `/teach writer: shorter intros`.
- **`/new-agent`** — when one kind of work keeps coming back, add one team member for it (one agent, one job).
- **One task, one session.** Start a fresh chat for each new task; the `brain/` folder remembers.

## What's inside
```
CLAUDE.md                  Chief of Staff instructions for Claude Code
AGENTS.md                  same, for ChatGPT Codex and other tools
.claude/agents/            the team (starts with chief-of-staff.md)
.claude/commands/          /setup, /teach, /new-agent
brain/README.md            how the memory works
brain/about-me.md          who the office works for (filled by /setup)
brain/RULES.md             safe defaults + your own rules
brain/state/               one page per project and agent (+ INDEX, _template)
brain/lessons/             what /teach saves
brain/inbox/               drop zone for notes and files
```

## Safety defaults
Asks before anything sent, public or paid. No passwords or keys in files (use `.env`, never committed). Never deletes; archives instead. Plain language.

**Codex users:** open the folder in Codex; it reads `AGENTS.md`. Say "run setup" and it follows `.claude/commands/setup.md`.
