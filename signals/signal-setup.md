You are running /signal-setup for the current workspace.

Signal skills are installed in `.claude/skills/`. This skill adds Signal to your
workspace context so Claude knows the skills are available.

---

## Step 1: Check current state

Read `CLAUDE.md` in the current directory (or `.claude/CLAUDE.md`).
Check if a Signal section already exists (look for "## Signal" or "Signal is installed").

If Signal section already found:
> Signal is already configured in your CLAUDE.md. Nothing to do.
> Run `/signal` to see all available skills.
Stop here.

---

## Step 2: Preview

Show the user exactly what will be added:

```
## Signal — Feature Decision Intelligence

Signal is installed in `.claude/skills/` (77 skills, 14 namespaces).

Quick start:
  /decide <topic>        run the full pre-commitment decision campaign
  /signal                see all available commands
  /competitors <topic>   inertia-first competitive analysis

The one rule: the primary competitor is always inertia. Before any feature,
ask "why would teams do nothing instead?" If you cannot answer that,
you are not ready to build.

Docs: docs/QUICKSTART.md
```

Ask: "Add this Signal section to your CLAUDE.md? [y/N]"

If N: stop. Print "Run /signal-setup any time to configure Signal."

---

## Step 3: Write to CLAUDE.md

If confirmed:
1. If CLAUDE.md exists: append the Signal section at the end
2. If CLAUDE.md does not exist: create it with just the Signal section
3. Confirm: "Signal section added to CLAUDE.md ✓"

---

## Step 4: GitHub Copilot (optional)

Check if `.github/copilot-instructions.md` exists.

If yes, ask: "Also update .github/copilot-instructions.md for GitHub Copilot? [y/N]"

If confirmed, append:
```
## Signal — Feature Decision Intelligence

Signal prompt files are installed in `.github/prompts/`.
Use them via Copilot Chat: attach a prompt file or type @workspace and select a prompt.

Quick start: attach `decide.prompt.md` for the full pre-commitment decision campaign.
Primary rule: assess inertia (do nothing) before any named alternative.
```

Confirm: ".github/copilot-instructions.md updated ✓"

---

## Step 5: Done

Print:
```
Signal is configured. In Claude Code, type:
  /signal     — see all 77 available commands
  /decide     — run your first campaign
```
