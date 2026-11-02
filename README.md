# My AI Office

_AI Office Base: a small starter for your own AI team in Claude Code. One room for now: a **Chief of Staff** and the brain. You name the office and the Chief during `/setup`; the rest of the team follows when you need it._

## Install (3 steps)
1. **Get the folder.** Clone it (`git clone <repo-url> my-ai-office`) or download the ZIP and unzip it.
2. **Open the folder in Claude Code** (desktop app: Code tab → open folder; or run `claude` inside it).
3. **Type `/setup`.** Name your office and your Chief, answer a few questions. The Chief saves who you are, your rules and your first project.

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
.claude/playbooks/         quick commands ("Status", "What needs me?")
.claude/skills/            skills you add later
tools/                     API scripts you add later (keys in .env)
brain/README.md            how the memory works + map of rooms
brain/about-me.md          you, your office's name, your Chief's name
brain/RULES.md             levels A-D, safe defaults, your own rules
brain/decisions.md         what you decided, in your words
brain/board.md             running / waiting / done
brain/approvals.md         things waiting for your yes
brain/state/               one page per project and agent (+ INDEX, _template)
brain/lessons/             what /teach saves
brain/reports/             longer write-ups
brain/inbox/               drop zone (archive/ instead of deleting)
```

Each agent you add with `/new-agent` gets its own room in `brain/`.

## Safety defaults
Asks before anything sent, public or paid. No passwords or keys in files (use `.env`, never committed). Never deletes; archives instead. Plain language.

**Codex users:** open the folder in Codex; it reads `AGENTS.md`. Say "run setup" and it follows `.claude/commands/setup.md`.
