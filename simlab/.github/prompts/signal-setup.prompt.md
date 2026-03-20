---
mode: agent
description: "Configure Signal in your workspace. Sets up CLAUDE.md and walks through CONTEXT.md so every skill knows what you are building and which topics you are investigating."
---

You are running /signal-setup.

Configure this workspace for Signal: update CLAUDE.md and create CONTEXT.md.

---

## STEP 1 -- CHECK FOR EXISTING SIGNAL CONTEXT

Read CLAUDE.md if it exists. Check if Signal context is already present (look for "Signal is installed").

If Signal context already exists:
  Display: "Signal context already in CLAUDE.md -- skipping."
  Jump to STEP 3.

---

## STEP 2 -- WRITE SIGNAL CONTEXT BLOCK

Append the following block to CLAUDE.md (create CLAUDE.md if it does not exist):

```markdown
## Signal

Signal is installed in this workspace. Use Signal skills to gather evidence before
committing to a feature.

**Namespaces**:
- discover: /discover-competitors, /discover-feasibility, /discover-inertia, /discover-hypothesis, /discover-risk, /discover-analysis, /discover-synthesize
- specify: /specify-spec, /specify-proposal, /specify-pitch, /specify-commitment, /specify-abstract
- validate: /validate-design, /validate-users, /validate-customers, /validate-code, /validate-adoption, /validate-feedback, /validate-support
- simulate: /simulate-lifecycle, /simulate-request, /simulate-state, /simulate-contract, /simulate-conversation, /simulate-argument
- rhythm: /rhythm-decide, /rhythm-status, /rhythm-story, /rhythm-qa, /rhythm-brief, /rhythm-rebuttal
- roles: /roles-scan, /roles-build, /roles-check, /roles-product-review, /roles-pull-request
- research: /research-pre-write, /research-post-write
- tools: /tools-coverage, /tools-preview, /tools-accept
- signal: /signal, /signal-health, /signal-setup

**Inertia rule**: The primary competitor is always inertia. Every investigation answers
why teams would do nothing instead. If you cannot explain why inertia loses, the feature
does not have a clear value case.

**Context**: Read CONTEXT.md at the start of every skill run for workspace context,
active topics, and repo pointers.

**Artifacts**: signals/{namespace}/{skill}/{topic}-{skill}-{date}.md
Topic slugs come from CONTEXT.md ## Topics table.
Use /tools-coverage <topic> to check coverage gaps.
Use /rhythm-status <topic> to see readiness.
Use /signal-health to check workspace health.
```

---

## STEP 3 -- CHECK FOR CONTEXT.MD

Check if CONTEXT.md exists and has content beyond template comments.

If CONTEXT.md is filled in:
  Display: "CONTEXT.md found -- workspace context is ready."
  Jump to STEP 5.

---

## STEP 4 -- CREATE CONTEXT.MD

Tell the user:
"Signal uses CONTEXT.md as shared context for every skill. Fill it in once and every investigation is grounded in your actual world."

Ask these questions one at a time. Wait for each answer.

**Workspace:**
1. "What product or system are you building signals for? (e.g. Dynamics 365, an internal Azure tool, a VS Code extension)"
2. "What is your tech stack? (e.g. React + .NET + Azure, Python + FastAPI, Power Platform)"
3. "Who are your primary users? (e.g. enterprise sales teams, internal FTEs, SMB customers)"
4. "What is your team's biggest constraint right now? (e.g. shipping by Q2, limited eng headcount)"

**Repos:**
5. "List repos you will be investigating. For each: name | path | key files to read. Enter one per line, type 'done' when finished.
   Example: myrepo | C:\src\myrepo | README.md, CLAUDE.md"

**Topics:**
6. "What is your first topic slug? This is what you type to every skill. (e.g. dark-mode, auth-v2)"
7. "One-line description of that topic?"
8. "Any more topics? (slug | description, or press enter to skip)"
   Collect until user skips.

Write CONTEXT.md with collected answers:

```markdown
# Workspace Context

Every Signal skill reads this file. Keep it current.
Run /signal-setup to update interactively.

---

## Topics

Active investigations. The slug is what you pass to every skill.

| Slug | Description | Status | Repos | Started |
|------|-------------|--------|-------|---------|
{one row per topic, status = active, date = today}

To work a topic:
  /rhythm-status <slug>       See what signals exist
  /tools-coverage <slug>      See what is missing
  /rhythm-decide <slug>       Full pre-commitment campaign

---

## Workspace

### Product
{answer 1}

### Tech stack
{answer 2}

### Users
{answer 3}

### Constraints
{answer 4}

---

## Repos

Skills read these for source context.

| Name | Path | Key files |
|------|------|-----------|
{one row per repo collected}
```

---

## STEP 5 -- CONFIRM

Display:
```
Signal setup complete.

  CLAUDE.md     -- Signal context installed
  CONTEXT.md    -- Workspace context ready

Active topics:
{list each topic slug: /rhythm-status <slug>}

First commands:
  /rhythm-decide <topic>            Full pre-commitment campaign
  /discover-competitors <topic>     Scout inertia and named competitors
  /tools-coverage <topic>           See what signals are missing
  /signal                           See all 68 commands
```