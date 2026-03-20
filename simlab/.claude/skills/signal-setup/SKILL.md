---
name: signal-setup
description: Configure Signal in your workspace. Sets up CLAUDE.md and walks through CONTEXT.md so every skill knows what you are building.
allowed-tools: [Read, Write, Edit, Bash]
param_set: lean
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

**Context**: Read CONTEXT.md at the start of every skill run for workspace context.

**Artifacts**: signals/{namespace}/{skill}/{topic}-{skill}-{date}.md
Use /tools-coverage {topic} to check coverage gaps.
Use /signal-health to check workspace health.
```

---

## STEP 3 -- CHECK FOR CONTEXT.MD

Check if CONTEXT.md exists.

If CONTEXT.md exists:
  Display: "CONTEXT.md found -- workspace context is ready."
  Jump to STEP 5.

---

## STEP 4 -- CREATE CONTEXT.MD

Tell the user:
"Signal uses CONTEXT.md as shared context for every skill. Fill it in once and every investigation will be grounded in your actual world."

Ask the user these questions one at a time. Wait for each answer before asking the next.

1. "What product or system are you building signals for? (e.g. Dynamics 365 CRM, an internal Azure tool, a VS Code extension)"
2. "What is your tech stack? (e.g. React + .NET + Azure, Python + FastAPI, Power Platform)"
3. "Who are your primary users? (e.g. enterprise sales teams, internal Microsoft FTEs, SMB customers)"
4. "What is your team's biggest constraint right now? (e.g. shipping by Q2, limited eng headcount, no design resources)"
5. "Anything else every skill should know about your context? (optional — press enter to skip)"

Then write CONTEXT.md with their answers:

```markdown
# Workspace Context

Every Signal skill reads this file. Keep it current.

## Product
{answer 1}

## Tech stack
{answer 2}

## Users
{answer 3}

## Constraints
{answer 4}

## Notes
{answer 5 or "None."}
```

---

## STEP 5 -- CONFIRM

Display:
```
Signal setup complete.

  CLAUDE.md     -- Signal context installed
  CONTEXT.md    -- Workspace context ready

First commands:
  /discover-competitors <feature>   Scout inertia and named competitors
  /specify-spec <feature>           Write a spec from intent
  /rhythm-decide <feature>          Full pre-commitment decision campaign
  /signal                           See all 68 commands
```
