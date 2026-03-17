# Quest Variate: signal-setup — Round 1

**Skill**: signal-setup | **Date**: 2026-03-16 | **Rubric version**: 1

---

## V-01: Sequential Gate Model

**Variation axis**: Lifecycle emphasis — each phase is an explicit named gate; no phase begins until the prior gate passes.

**Hypothesis**: Explicit gates prevent the most common failure mode (writing without confirmation) by making each boundary a named checkpoint rather than an implied flow.

---

```markdown
You are running /signal-setup.

Configure Signal in this workspace after installation.

---

## Gate 1 — Detect

Check whether this workspace already has Signal configured:

1. Read CLAUDE.md if it exists. Search for a Signal section (look for `## Signal` or `<!-- signal-setup -->`). If found, go to **Gate 4 (Already Configured)**.
2. Check whether `.github/copilot-instructions.md` exists. Note the result for Gate 3.
3. Report what you found:
   - Does CLAUDE.md exist? (yes/no/path)
   - Does it already have a Signal section? (yes/no)
   - Does .github/copilot-instructions.md exist? (yes/no)

Do not write anything yet.

---

## Gate 2 — Preview

Compose the Signal section that will be appended. Show it to the user exactly as it will appear.

The section must include:
- A heading: `## Signal`
- A brief statement of what Signal is (1–2 sentences)
- A list of the available skill namespaces: scout, draft, review, flow, trace, prove, listen, program, topic
- The inertia rule: "The default is to keep building. A topic becomes ready when signals across namespaces outweigh the cost of the unknown — not when a checklist completes."
- A note that skills are invoked as `/signal:{namespace}` or `/signal:{skill}`

Show the preview in a fenced code block so the user sees exactly what will be written.

Then ask: **"Append this Signal section to CLAUDE.md? (yes/no)"**

Do not write until the user confirms.

---

## Gate 3 — Write

After the user confirms:

1. Append the previewed Signal section to CLAUDE.md. Do not modify any existing content above it.
2. If .github/copilot-instructions.md exists, ask: **"Also update .github/copilot-instructions.md with a Signal reference? (yes/no)"** If yes, append a brief Signal reference there as well.
3. Report: what was written, to which file(s), at what line.

---

## Gate 4 — Already Configured

If a Signal section was already detected in Gate 1:

- Report: "Signal section already present in CLAUDE.md. No changes made."
- Show the existing section for review.
- Offer: "Run `/signal-setup --force` to replace it."

Do not write anything.

---

## Gate 5 — Missing CLAUDE.md

If CLAUDE.md does not exist:

- Inform the user: "No CLAUDE.md found. Signal setup will create one with just the Signal section."
- Show the preview as in Gate 2.
- Ask confirmation before creating the file.
```

---

## V-02: Structured Table Output

**Variation axis**: Output format — all status reporting uses structured tables; confirmation is a single yes/no prompt after a summary table.

**Hypothesis**: Table-format status output reduces ambiguity about what was found and what will change, making the confirmation decision easier and the outcome report machine-readable.

---

```markdown
You are running /signal-setup.

Set up Signal context in this workspace. Follow the steps below in order.

---

### Step 1: Workspace Scan

Read the workspace and produce this status table before doing anything else:

| Item | Status | Path |
|------|--------|------|
| CLAUDE.md exists | yes / no | (path if yes) |
| Signal section present | yes / no / n/a | (line range if yes) |
| .github/copilot-instructions.md exists | yes / no | (path if yes) |

If "Signal section present" is **yes**, skip to **Step 4**.

---

### Step 2: Preview

Compose the Signal section. Present it in a fenced code block:

```
## Signal

Signal is a developer tool for feature decision-making across 9 namespaces.
Know what you know before you commit.

### Available Namespaces
- /signal:scout — market, competitors, feasibility, requirements, stakeholders
- /signal:draft — brainstorm, pitch, proposal, spec
- /signal:review — code, design, customers, users
- /signal:flow — conversation, dataflow, integration, lifecycle, resilience, throttle, trigger
- /signal:trace — component, contract, deployment, migration, permissions, request, state
- /signal:prove — analysis, hypothesis, intelligence, interview, program, prototype, publish, synthesize, topic, websearch
- /signal:listen — adoption, feedback, support
- /signal:program — plan
- /signal:topic — echo, new, plan, report, status, story

### Inertia Rule
The default is to keep building. A topic is ready when signals across namespaces
outweigh the cost of the unknown — not when a checklist completes.
```

Then show a **Proposed Changes** table:

| Action | Target | Detail |
|--------|--------|--------|
| Append | CLAUDE.md | Add Signal section (~30 lines) |
| Append (optional) | .github/copilot-instructions.md | Add Signal reference (~5 lines) |

---

### Step 3: Confirm and Write

Ask: **"Proceed with these changes? (yes/no)"**

On yes:
1. Append the Signal section to CLAUDE.md.
2. If .github/copilot-instructions.md exists, ask separately whether to update it.
3. Output a **Write Report** table:

| Action | File | Result |
|--------|------|--------|
| Append | CLAUDE.md | Written (lines N–M) |
| Append | .github/copilot-instructions.md | Written / Skipped |

---

### Step 4: Already Configured

If the scan found an existing Signal section, output:

| Check | Result |
|-------|--------|
| Signal section | Already present (lines N–M) |
| Action taken | None — skipped |

Show the existing section. No writes performed.
```

---

## V-03: Conversational Guide

**Variation axis**: Phrasing register — fully conversational, first-person narration, imperative reduced to guidance; reads like a setup wizard dialogue.

**Hypothesis**: A conversational register reduces friction for first-time users who may be unfamiliar with Signal; the wizard style sets expectations at each step without feeling like a spec.

---

```markdown
You are running /signal-setup — the one-time Signal configuration wizard.

Hi! Let's get Signal set up in your workspace. This takes about 30 seconds. I'll check what's already here, show you what I'm going to add, and ask before touching anything.

---

**First, let me look around.**

Check for CLAUDE.md in the workspace root. Also check for `.github/copilot-instructions.md`. Tell the user what you found in plain language — something like "Found CLAUDE.md at the root. No copilot instructions file."

If CLAUDE.md already contains a Signal section (look for `## Signal`), skip the rest and say:
> "Looks like Signal is already configured here — I can see the Signal section in your CLAUDE.md. Nothing to do! If you want to refresh it, just delete the Signal section and re-run."

---

**Now let me show you what I'll add.**

Compose the Signal section and show it in a fenced code block. The section should feel like documentation, not boilerplate:

```
## Signal

Signal is a developer tool for feature decision-making. Before committing to a
feature, teams gather evidence across 9 namespaces — each artifact a signal toward
the feature story. When enough signals exist, the topic tells you you're ready.

**Namespaces**: scout · draft · review · flow · trace · prove · listen · program · topic

**How to invoke**: /signal:{skill} — e.g., /signal:scout-competitors, /signal:draft-spec

**The inertia rule**: The default is always to keep building. A topic shifts to ready
when the weight of signals outweighs the cost of remaining unknowns — not when a
checklist is complete. Momentum is the default; readiness is earned.
```

Then say something like: "Here's what I'll append to your CLAUDE.md. Take a look — does this look right?"

---

**Wait for the green light.**

Ask the user to confirm before writing. Something like:
> "Ready to add this? Just say yes and I'll append it. Or no if you want to adjust anything first."

Do not write until you have a yes.

---

**Write and wrap up.**

After confirmation:
1. Append the section to CLAUDE.md.
2. If `.github/copilot-instructions.md` exists, offer: "I also noticed you have a Copilot instructions file — want me to add a brief Signal reference there too?"
3. When done, tell the user what happened in plain language: which file(s) were updated, that Signal is now configured, and how to invoke the first skill if they want to try it: `/signal:topic-new`.
```

---

## V-04: Inertia-Forward Framing

**Variation axis**: Inertia framing — the inertia rule is introduced early in the preview and framed as the philosophical core of Signal, not an appendix item.

**Hypothesis**: Leading with the inertia rule in setup primes users to understand Signal's philosophy from the first moment, making skill output more legible later because users know the frame.

---

```markdown
You are running /signal-setup.

Configure Signal in this workspace.

---

### Phase 1: Detect

Check the workspace:
- Does CLAUDE.md exist? Read it if so.
- Does it already contain a Signal section (look for `## Signal` or `signal-setup`)? If yes, skip to **Phase 4**.
- Does `.github/copilot-instructions.md` exist?

Report findings before proceeding.

---

### Phase 2: Compose the Signal Section

The Signal section leads with the inertia rule because it is the governing principle of the entire system. Structure the section as follows:

```
## Signal

### The Inertia Rule

Building has momentum. The default is to keep building. A feature topic
shifts from "in progress" to "ready" only when the accumulated signals
across namespaces outweigh the cost of the remaining unknowns.

This is not a checklist. You do not need all nine namespaces to fire.
You need enough signal mass to overcome inertia — and inertia favors action.

### What Signal Does

Signal is a developer tool for feature decision-making. Nine namespaces.
Each skill produces one artifact. The /signal:topic namespace reads them
all and tells you what the signals say together.

### Namespaces and Skills

Invoke any skill as /signal:{skill-name}:

**scout** — competitors, compliance, feasibility, market, naming, positioning, requirements, stakeholders  
**draft** — brainstorm, pitch, proposal, spec  
**review** — code, customers, design, users  
**flow** — conversation, dataflow, integration, lifecycle, resilience, throttle, trigger  
**trace** — component, contract, deployment, migration, permissions, request, state  
**prove** — analysis, hypothesis, intelligence, interview, program, prototype, publish, synthesize, topic, websearch  
**listen** — adoption, feedback, support  
**program** — plan  
**topic** — echo, new, plan, report, status, story  
```

Show this preview in a fenced code block. Make clear this is exactly what will be written.

---

### Phase 3: Confirm and Write

Ask: **"Append this Signal section to CLAUDE.md?"**

On confirmation:
1. Append the section verbatim to CLAUDE.md.
2. If `.github/copilot-instructions.md` exists, ask whether to add a Signal reference there too. If yes, append a condensed version (inertia rule + namespace list, no full skill catalog).
3. Confirm what was written: file path(s), line range(s).

---

### Phase 4: Already Configured

Signal section detected. Output:

> "Signal section found in CLAUDE.md — skipping setup. No changes made."

Display the existing section. No writes.

---

### Phase 5: No CLAUDE.md

If CLAUDE.md does not exist:

Inform the user. Offer to create it with only the Signal section. Show the same preview from Phase 2. Ask confirmation before creating.
```

---

## V-05: Minimal Imperative

**Variation axis**: Role sequence + lifecycle emphasis — minimal prose, action-first, every instruction is a direct command; no explanatory scaffolding.

**Hypothesis**: A terse imperative prompt produces faster execution with less hallucinated narration; the skill does less explaining and more doing, which fits users who already know Signal and want a quick re-run.

---

```markdown
You are running /signal-setup.

---

**1. Check.**

Read CLAUDE.md if present. Search for `## Signal`. If found: print "Signal already configured. No changes made." and stop.

Also check: does `.github/copilot-instructions.md` exist? Note for step 4.

---

**2. Preview.**

Print the following block exactly — this is the Signal section you will append:

```
## Signal
<!-- signal-setup -->

Signal gathers feature evidence across 9 namespaces before you commit.
The inertia rule: keep building by default; a topic is ready when signal
mass outweighs remaining unknowns — not when a checklist is done.

Skills: /signal:{name}
  scout    – competitors, compliance, feasibility, market, naming, positioning, requirements, stakeholders
  draft    – brainstorm, pitch, proposal, spec
  review   – code, customers, design, users
  flow     – conversation, dataflow, integration, lifecycle, resilience, throttle, trigger
  trace    – component, contract, deployment, migration, permissions, request, state
  prove    – analysis, hypothesis, intelligence, interview, program, prototype, publish, synthesize, topic, websearch
  listen   – adoption, feedback, support
  program  – plan
  topic    – echo, new, plan, report, status, story
```

---

**3. Confirm.**

Ask: **"Append to CLAUDE.md? (yes/no)"**

Wait. Do not write until the answer is yes.

---

**4. Write.**

Append the block from step 2 to CLAUDE.md. Do not alter existing content.

If `.github/copilot-instructions.md` exists, ask: **"Also update copilot instructions? (yes/no)"** If yes, append:

```
# Signal
Use /signal:{skill} to gather feature evidence. Inertia rule: build by default;
ready when signals outweigh unknowns. Namespaces: scout draft review flow trace
prove listen program topic.
```

Print: "Done. Signal section written to [file path], lines [N–M]."

---

**5. Missing CLAUDE.md.**

If CLAUDE.md does not exist: inform the user, show the preview from step 2, ask confirmation, then create the file with that content. Print: "Created CLAUDE.md with Signal section."
```

---

## Variation Map

| Variation | Primary Axis | Secondary Axis | Key Bet |
|-----------|-------------|----------------|---------|
| V-01 | Lifecycle emphasis (gates) | — | Explicit gates prevent write-before-confirm |
| V-02 | Output format (tables) | — | Tables reduce ambiguity, aid re-run diagnostics |
| V-03 | Phrasing register (conversational) | — | Wizard feel lowers first-timer friction |
| V-04 | Inertia framing (lead position) | Lifecycle emphasis | Leading with philosophy primes skill output legibility |
| V-05 | Role sequence (action-first) | Lifecycle emphasis (minimal) | Terse imperative → faster execution, less narration |
