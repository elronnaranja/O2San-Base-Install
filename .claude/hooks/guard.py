#!/usr/bin/env python3
"""Office guard: turns the most important rules into real checks, so they hold even when a chat forgets them.

Claude Code runs this before every tool call it matches (see .claude/settings.json). It reads the call as JSON and answers:
  - deny: reading or writing .env (keys live there and never leave it).
  - ask:  deleting files, force-pushing or wiping git history, and any connector action that sends, posts, publishes,
          shares, pays or deletes. Claude Code then stops and asks you to approve that one action.
Anything else passes. Standard library only. Change the lists below if your office needs something different.
"""
import json
import re
import sys

SECRET_FILE = re.compile(r"(^|[\\/\s'\"=:])\.env(\.(?!example\b)[\w-]+)?(?=$|[\s'\";|&)<>])")
DELETES = re.compile(r"(^|[;&|(\s])(rm|rmdir|del|erase|rd|unlink|shred|Remove-Item|trash)(\s|$)|git\s+(clean\b|reset\s+--hard|push\s+.*(--force|-f\b))|find\s.*-delete", re.I)
# Connector actions that send or publish but whose names don't say so. Add yours here, e.g. "mcp__myposter__createPost".
EXTRA_OUTWARD_TOOLS = set()
OUTWARD = re.compile(r"(send|reply|forward|post|publish|share|schedul|invite|pay|charge|refund|transfer|delete|trash|remove|archive_|unpublish)", re.I)


def answer(decision, reason):
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": decision, "permissionDecisionReason": reason}}))
    sys.exit(0)


def main():
    try:
        call = json.load(sys.stdin)
    except Exception:
        sys.exit(0)  # not a tool call we understand: let Claude Code handle it
    tool = call.get("tool_name", "") or ""
    args = call.get("tool_input", {}) or {}

    if tool in ("Read", "Edit", "Write", "MultiEdit", "NotebookEdit"):
        path = str(args.get("file_path") or args.get("notebook_path") or "")
        name = re.split(r"[\\/]", path)[-1]
        if name == ".env" or (name.startswith(".env.") and name != ".env.example"):
            answer("deny", "Rule: keys live in .env and are never read or written by the office. Scripts in tools/ load it themselves.")

    if tool == "Bash":
        cmd = str(args.get("command", ""))
        if SECRET_FILE.search(cmd):
            answer("deny", "Rule: keys live in .env and are never read or printed. Scripts in tools/ load it themselves.")
        if DELETES.search(cmd):
            answer("ask", "Rule: never delete. Move it to brain/08-Inbox/archive/ instead, or approve this one deletion.")

    if tool.startswith("mcp__"):
        action = tool.split("__")[-1]
        if tool in EXTRA_OUTWARD_TOOLS or OUTWARD.search(action):
            answer("ask", "Rule: anything sent, public, paid or deleted needs your yes first (brain/10-Office/approvals.md). Approve this one action?")

    sys.exit(0)


if __name__ == "__main__":
    main()
