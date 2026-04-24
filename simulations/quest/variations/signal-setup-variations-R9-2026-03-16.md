# /quest:variate — signal-setup — Round 9

---

## V-01 — Gate-Explicit Lifecycle
**Axis**: Lifecycle emphasis — every phase is a numbered, named gate; edge cases are first-class gates, not inline branches
**Hypothesis**: Naming gates explicitly enforces sequencing and makes the already-configured and missing-file paths structurally equal to the happy path, satisfying C-11 and C-12 more reliably than prose conditionals.

```markdown
# signal-setup

Configure Signal in your workspace. This skill appends a Signal section to CLAUDE.md
so every Claude Code session opens with Signal's vocabulary and the inertia question
already present — no re-introduction required.

---

## Why Setup Matters

Inertia is not a concept. It is your real competitor — the force that keeps teams
building what they would have built anyway. Inertia wins by default. The path of least
resistance runs straight to implementation without pausing to ask "why would teams do
nothing?" That question only gets asked if something names it. Signal names it. But
Signal only shows up in your sessions if this configuration exists.

This is the one write that makes Signal permanent. CLAUDE.md loads automatically at
the start of every Claude Code session. Configure it now and the inertia question is
present without you having to remember — every session, before the first decision.

---

## Execution Gates

### GATE 1 — Detect CLAUDE.md

Read `CLAUDE.md` in the current working directory.

- Found → **GATE 2**
- Not found → **GATE 1A**

---

### GATE 1A — Missing CLAUDE.md (First-Class Gate)

CLAUDE.md does not exist in this workspace. Without it there is no persistent
context — Signal's vocabulary would need to be re-introduced every session.

Show the user what would be created: a new CLAUDE.md containing only the Signal
section (preview from **Signal Section Template** below).

Ask: "No CLAUDE.md found. Create one with the Signal section? (yes/no)"

- Yes → **GATE 3**
- No →
  > "Setup declined. At the planning stage — before your next feature spec is
  > written — Signal's skills won't appear in Claude's context. There will be no
  > prompt to ask 'why would teams do nothing?' before the approach is committed.
  > Run /signal-setup when ready."

  → **STOP**

---

### GATE 2 — Check Existing Signal Section

Scan CLAUDE.md for an existing Signal section. Look for `## Signal` or the marker
`<!-- signal-configured -->`.

- Section found → **GATE 2A**
- Not found → **GATE 3**

---

### GATE 2A — Already Configured (First-Class Gate)

Signal is already present in CLAUDE.md. Because CLAUDE.md loads automatically every
session, inertia already has a named opponent in every conversation — before the
first skill runs, before the first decision. The configuration is doing its work
continuously, without you maintaining it.

Output:
> "Signal section found. CLAUDE.md loads automatically — inertia's question is
> present at session start without any action on your part. No changes made."

→ **GATE 5** (offer Copilot update)

---

### GATE 3 — Preview

Generate the Signal section from the **Signal Section Template** below.
Display it in full.

Ask: "This section will be appended to CLAUDE.md. Proceed? (yes/no)"

- Yes → **GATE 4**
- No →
  > "Append declined. At the planning stage — before your next feature spec is
  > committed — Signal won't be in Claude's context. The inertia question has no
  > standing invitation here. Run /signal-setup when ready."

  → **GATE 5** (offer Copilot update, or STOP)

---

### GATE 4 — Write

Append the Signal section to CLAUDE.md exactly as previewed. Do not modify any
existing content above the append point.

Output:
> "Signal section appended to CLAUDE.md. Every session going forward opens with
> Signal's skills and the inertia question already in context. Setup complete."

→ **GATE 5**

---

### GATE 5 — Offer Copilot Instructions

Ask: "Update .github/copilot-instructions.md with a Signal section too? (yes/no)"

- Yes → **GATE 6**
- No →
  > "Copilot instructions not updated. While implementing — when Copilot suggests
  > the first function in a new feature — Signal's inertia question won't be in
  > that context. Run /signal-setup to add it later."

  → **STOP**

---

### GATE 6 — Detect Copilot File (First-Class Gate)

Read `.github/copilot-instructions.md`.

- Not found → offer to create it; if user declines apply GATE 5 no-path
  consequence text → **STOP**
- Signal section already present →
  > "Signal already present in Copilot instructions. While implementing, Copilot
  > carries Signal's vocabulary — the inertia question is active at the point of
  > code suggestion, inside the editor, not only at planning. No changes made."

  → **STOP**
- Found, no Signal section → preview Copilot Signal section, ask confirmation,
  write on yes → **GATE 7**

---

### GATE 7 — Final Report

Output a complete summary: files written, sections appended, gates that were
skipped and why.

---

## Signal Section Template

```markdown
## Signal
<!-- signal-configured -->

Signal is installed. Before committing to any feature approach, ask:
*why would teams do nothing?*

**Inertia rule**: A topic is not ready until signals together answer what makes
inaction more likely than adoption.

### Available Skills

| Namespace | Skills |
|-----------|--------|
| `/scout`   | competitors, market, feasibility, requirements, compliance, naming, stakeholders, positioning |
| `/draft`   | brainstorm, spec, proposal, pitch |
| `/review`  | code, design, customers, users |
| `/flow`    | trigger, throttle, lifecycle, resilience, dataflow, conversation, integration |
| `/trace`   | skill, state, contract, permissions, request, component, migration, deployment |
| `/prove`   | hypothesis, interview, topic, prototype, analysis, synthesize, intelligence, program, websearch, publish |
| `/listen`  | support, feedback, adoption |
| `/program` | plan, program |
| `/topic`   | new, plan, status, report, story, echo |

Run `/topic:status` to see what signals exist for the current topic.
```
```

---

## V-02 — Adversary-First Inertia Framing
**Axis**: Inertia framing — inertia is introduced as a named adversary in the opening and referenced at every gate where the user could leave without configuring
**Hypothesis**: Consistently naming inertia as the adversary (not a concept) shifts user psychology: each decline becomes a choice to let inertia win, not merely a deferral.

```markdown
# signal-setup

You are about to choose a side. Inertia — the force that keeps teams building
what they would have built anyway — wins by default. Every feature that ships
without asking "why would teams do nothing?" is a point to inertia. Signal gives
you the tools to ask that question before it costs you a launch.

But the tools are only available if your context knows they exist. This setup
writes Signal's vocabulary into CLAUDE.md so the question is present at the
start of every session — not as a habit you have to maintain, but as a standing
instruction that loads automatically. Configure it once; Signal opposes inertia
in every session that follows.

---

## Step 1 — Read CLAUDE.md

Read `CLAUDE.md` in the current working directory.

**If not found**: CLAUDE.md does not exist here. There is no persistent context
for Claude Code — inertia will face no named opponent in any session.

Show what would be created (preview from Signal Section Template), then ask:
"No CLAUDE.md found. Create one so Signal can oppose inertia here? (yes/no)"

- Yes → Step 3
- No →
  > "Inertia wins this one. At the planning stage — when you next open a spec or
  > run a /draft skill — there will be no reminder that inertia is the real
  > competitor. The question 'why would teams do nothing?' won't be in your
  > context. Run /signal-setup when you're ready to give Signal a seat at the table."

  → STOP

**If found**: → Step 2

---

## Step 2 — Check for Existing Signal Section

Scan CLAUDE.md for `## Signal` or `<!-- signal-configured -->`.

**If Signal section already present**:

Inertia already has a named opponent in this workspace. CLAUDE.md loads at session
start — Signal's vocabulary is present before the first decision, automatically,
every time. You chose this side; the configuration is holding the line.

> "Signal already configured. CLAUDE.md loads every session, so inertia is named
> before you open the first spec. The adversary has a title here. No changes needed."

→ Step 4 (offer Copilot update)

**If not present**: → Step 3

---

## Step 3 — Preview and Confirm

Generate and display the full Signal section (from **Signal Section Template**).

Ask: "Append this to CLAUDE.md and put Signal in Claude's context permanently? (yes/no)"

**If yes**:

Append the Signal section exactly as shown. Output:
> "Done. Inertia is named. Every session going forward, Claude opens with Signal's
> skills in context and the question already present: why would teams do nothing?
> Setup complete."

→ Step 4

**If no**:
> "Not appended. Inertia wins this session and every session that follows until
> setup runs. At the planning stage — when the next feature approach gets committed
> without the question being asked — there will be no opponent in your context.
> Run /signal-setup when ready."

→ Step 4 (offer Copilot, or STOP)

---

## Step 4 — Offer Copilot Instructions

Ask: "Also update .github/copilot-instructions.md so Signal's vocabulary is
present inside GitHub Copilot interactions? (yes/no)"

**If no**:
> "Copilot instructions not updated. While implementing — at the moment Copilot
> suggests the first function in a new feature — Signal won't be present in that
> context. Inertia has no named opponent inside your editor. Run /signal-setup
> to change that."

→ STOP

**If yes**: → Step 5

---

## Step 5 — Handle Copilot File

Read `.github/copilot-instructions.md`.

**Not found**: Offer to create it. If declined:
> "Copilot instructions not created. While implementing, inertia faces no opponent
> in that context. Run /signal-setup to add it."
→ STOP

**Signal section already present**:
> "Signal already present in Copilot instructions. While implementing — at the
> moment Copilot offers a completion inside a new feature — Signal's vocabulary
> is active, the inertia question is live in that context. Inertia already has
> an opponent here too. No changes made."
→ STOP

**Found, no Signal section**: Preview Copilot-specific Signal section (abbreviated,
editor-context focused). Ask confirmation. Write on yes.

Output when done:
> "Copilot instructions updated. Inertia now faces Signal in Claude Code sessions
> and inside your editor. Both planning and implementation contexts are covered."

---

## Step 6 — Final Summary

List all files written, sections appended, and any paths where inertia remains
without a named opponent (and what would add one).

---

## Signal Section Template

```markdown
## Signal
<!-- signal-configured -->

Inertia is the adversary. Before committing to any feature approach, ask:
*why would teams do nothing?*

**Inertia rule**: A topic is not ready until its signals together answer what
makes inaction more likely than adoption.

### Available Skills

| Namespace | Skills |
|-----------|--------|
| `/scout`   | competitors, market, feasibility, requirements, compliance, naming, stakeholders, positioning |
| `/draft`   | brainstorm, spec, proposal, pitch |
| `/review`  | code, design, customers, users |
| `/flow`    | trigger, throttle, lifecycle, resilience, dataflow, conversation, integration |
| `/trace`   | skill, state, contract, permissions, request, component, migration, deployment |
| `/prove`   | hypothesis, interview, topic, prototype, analysis, synthesize, intelligence, program, websearch, publish |
| `/listen`  | support, feedback, adoption |
| `/program` | plan, program |
| `/topic`   | new, plan, status, report, story, echo |

Run `/topic:status` to see what signals exist for the current topic.
```
```

---

## V-03 — Explicit Phase Labels at Every Decline Gate
**Axis**: Phrasing register — explicit phase category labels ("at the planning stage," "while implementing") at every decline anchor; no phase left implied by vocabulary alone
**Hypothesis**: Stating the phase as a named category forces the user to visualize the concrete moment of consequence, making the decline decision more visceral and the criterion C-23 more reliably satisfied than vocabulary-implied phases.

```markdown
# signal-setup

You are setting up Signal — a skill system for gathering evidence before you
commit to a feature approach. The setup writes one section to CLAUDE.md.
That section loads automatically every Claude Code session, so Signal's
vocabulary is present from the first message without re-introduction.

The philosophy Signal teaches: inertia is a competitor, not a neutral force.
The question "why would teams do nothing?" deserves an answer before a spec
is written, not after a launch fails. Signal gives you the tools to find that
answer. This configuration gives those tools a permanent home in your context.

---

## Run

### 1. Detect CLAUDE.md

Read `CLAUDE.md` in the current directory.

**Not found** — CLAUDE.md does not exist. Show the user what would be created,
then ask:

"No CLAUDE.md found. Create one with the Signal section? (yes/no)"

- Yes → go to step 3
- No →
  > "Not created. At the **planning stage** — when you sit down to write the
  > first spec for a new feature — Claude won't know Signal exists. There will
  > be no prompt to ask what makes inaction likely before the approach is
  > locked in. Run /signal-setup when ready."

  → STOP

**Found** → step 2

---

### 2. Check for Existing Signal Section

Scan for `## Signal` or `<!-- signal-configured -->`.

**Already present**:

Signal is configured. Because CLAUDE.md loads at session start — automatically,
before the first message — Signal's vocabulary is in every conversation without
you maintaining it. At the planning stage, inertia already has a named opponent.

> "Signal section found in CLAUDE.md. CLAUDE.md auto-loads every session, so
> at the planning stage — before a spec or skill runs — inertia is already named
> as the adversary. No changes needed."

→ step 4 (Copilot offer)

**Not present** → step 3

---

### 3. Preview and Confirm

Generate the full Signal section from the template below. Display it.

Ask: "Append this to CLAUDE.md? (yes/no)"

- Yes: append exactly as shown →
  > "Appended. At the planning stage, every future session will open with
  > Signal's skills in context and the inertia question already named."

  → step 4

- No:
  > "Not appended. At the **planning stage** — before the next feature spec is
  > committed — Signal won't be in Claude's context. There's no standing
  > invitation for the inertia question. Run /signal-setup when ready."

  → step 4 (or STOP)

---

### 4. Offer Copilot Instructions

Ask: "Also update .github/copilot-instructions.md? (yes/no)"

- No:
  > "Copilot instructions not updated. While **implementing** — at the moment
  > Copilot suggests the first function body in a new feature — Signal's
  > vocabulary won't be in that context. The inertia question is absent
  > mid-build. Run /signal-setup to add it later."

  → STOP

- Yes → step 5

---

### 5. Handle Copilot File

Read `.github/copilot-instructions.md`.

**Not found**: Offer to create. If declined:
> "Not created. While **implementing**, Signal has no presence in Copilot
> interactions. Run /signal-setup to address that."
→ STOP

**Signal section already present**:
> "Signal already in Copilot instructions. While **implementing** — as Copilot
> generates function bodies and endpoint stubs — Signal's vocabulary is active
> in that context. Inertia is named at the point of code suggestion, not just
> at the planning stage. No changes needed."
→ STOP

**Found, no Signal section**: Preview, confirm, write on yes.

Output:
> "Copilot instructions updated. Signal now covers both the planning stage
> (CLAUDE.md) and the implementation stage (Copilot), so the inertia question
> has no gap in your workflow."

---

### 6. Final Report

List all files touched. For any path where Signal is absent, name the development
stage that lacks coverage.

---

## Signal Section Template

```markdown
## Signal
<!-- signal-configured -->

Signal is installed. Before committing to any feature approach, ask:
*why would teams do nothing?*

**Inertia rule**: A topic is not ready until its signals together answer what
makes inaction more likely than adoption.

### Skills by Namespace

| Namespace | Skills |
|-----------|--------|
| `/scout`   | competitors, market, feasibility, requirements, compliance, naming, stakeholders, positioning |
| `/draft`   | brainstorm, spec, proposal, pitch |
| `/review`  | code, design, customers, users |
| `/flow`    | trigger, throttle, lifecycle, resilience, dataflow, conversation, integration |
| `/trace`   | skill, state, contract, permissions, request, component, migration, deployment |
| `/prove`   | hypothesis, interview, topic, prototype, analysis, synthesize, intelligence, program, websearch, publish |
| `/listen`  | support, feedback, adoption |
| `/program` | plan, program |
| `/topic`   | new, plan, status, report, story, echo |

Run `/topic:status` to see what signals exist for the current topic.
```
```

---

## V-04 — Phase Labels + Secondary Gate Coverage
**Axes**: Explicit phase labels (C-23) + secondary optional gates with tool-local and phase-distinct consequence anchors (C-21, C-22, C-24)
**Hypothesis**: Combining named phase categories at every decline gate with Copilot-specific consequence language that draws from implementation-phase vocabulary (not a substitution of tool name into planning-phase framing) satisfies C-21/C-22/C-23 simultaneously in a way no single-axis variation achieves.

```markdown
# signal-setup

Signal is a suite of skills for gathering evidence before you commit to a
feature approach. This skill writes Signal's vocabulary into your Claude Code
context so it persists across sessions — no re-introduction needed.

**The adversary**: Inertia. The force that keeps teams shipping what they would
have shipped anyway. Inertia wins when no one asks "why would teams do nothing?"
before the approach is locked in. Signal gives you the tools to ask that question
at the right moment. This configuration gives those tools a permanent seat at
the table.

**Why it must persist**: Signal's skills are only valuable if your context
knows they exist. CLAUDE.md loads automatically at session start — configure
it now and inertia faces a named opponent before the first message, every
session, without maintenance.

---

## GATE 1 — Detect CLAUDE.md

Read `CLAUDE.md` in the current directory.

→ Not found: **GATE 1A**
→ Found: **GATE 2**

### GATE 1A — No CLAUDE.md

Display what would be created (Signal section from template). Ask:
"No CLAUDE.md found. Create one with the Signal section? (yes/no)"

- Yes → **GATE 3**
- No →
  > "Not created. At the **planning stage** — before a spec is written or a
  > /scout skill is run — Signal's vocabulary won't be in Claude's context.
  > There will be no prompt to ask what makes inaction the likely outcome.
  > The approach will be committed without that question present. Run
  > /signal-setup when ready."

  → STOP

---

## GATE 2 — Check Signal Section

Scan CLAUDE.md for `## Signal` or `<!-- signal-configured -->`.

→ Found: **GATE 2A**
→ Not found: **GATE 3**

### GATE 2A — Already Configured

CLAUDE.md auto-loads at session start. At the planning stage — before any
spec is drafted or skill is run — inertia already has a named opponent in
your context. The configuration is active and requires no maintenance.

> "Signal section present. CLAUDE.md auto-loads every session, so at the
> planning stage, Signal's vocabulary is present from the first message —
> inertia is named before you open the first spec. No changes needed."

→ **GATE 5** (offer Copilot update)

---

## GATE 3 — Preview

Generate and display the full Signal section.

Ask: "Append this to CLAUDE.md? (yes/no)"

- Yes → **GATE 4**
- No →
  > "Not appended. At the **planning stage** — when you next write a feature
  > spec or run a /draft skill — there will be no reminder that inertia is
  > the competitor and Signal has tools to interrogate it. The inertia
  > question has no standing invitation. Run /signal-setup when ready."

  → **GATE 5** (or STOP)

---

## GATE 4 — Write

Append Signal section exactly as previewed. Do not alter existing content.

> "Appended. At the planning stage, every future session opens with Signal's
> skills in context — inertia faces a named opponent from the first message."

→ **GATE 5**

---

## GATE 5 — Offer Copilot Instructions

Ask: "Update .github/copilot-instructions.md with a Signal section too? (yes/no)"

- No →
  > "Copilot instructions not updated. While **implementing** — when Copilot
  > generates the first function stub or endpoint for a new feature — Signal's
  > inertia question won't be present inside the editor. Copilot will suggest
  > code without Signal's framing active. Run /signal-setup to add it."

  → STOP
- Yes → **GATE 6**

---

## GATE 6 — Detect Copilot File

Read `.github/copilot-instructions.md`.

**Not found**: Show what would be created. Ask confirmation.
- Declined →
  > "Not created. While **implementing**, Copilot has no Signal context — the
  > inertia question is absent at the point of code suggestion. Run
  > /signal-setup to add it."
  → STOP
- Confirmed → write file with Copilot Signal section → **GATE 7**

**Signal section already present**:
> "Signal already in Copilot instructions. While **implementing** — as Copilot
> generates completions for new feature code — Signal's vocabulary is live in
> that context. The inertia question is present at the point of code suggestion,
> not only at the planning stage where CLAUDE.md operates. No changes needed."
→ STOP

**Found, no Signal section**: Preview Copilot Signal section (implementation-
context framing: "Before accepting a Copilot suggestion for a new feature,
ask: does this code assume adoption without asking why teams would do nothing?").
Confirm, write on yes → **GATE 7**

---

## GATE 7 — Final Report

Summary: files modified, gates skipped, development stages now covered and
any gaps that remain.

---

## Signal Section Templates

### CLAUDE.md Section (Planning Context)

```markdown
## Signal
<!-- signal-configured -->

Signal is installed. Before committing to any feature approach, ask:
*why would teams do nothing?*

**Inertia rule**: A topic is not ready until its signals together answer what
makes inaction more likely than adoption.

### Skills

| Namespace | Skills |
|-----------|--------|
| `/scout`   | competitors, market, feasibility, requirements, compliance, naming, stakeholders, positioning |
| `/draft`   | brainstorm, spec, proposal, pitch |
| `/review`  | code, design, customers, users |
| `/flow`    | trigger, throttle, lifecycle, resilience, dataflow, conversation, integration |
| `/trace`   | skill, state, contract, permissions, request, component, migration, deployment |
| `/prove`   | hypothesis, interview, topic, prototype, analysis, synthesize, intelligence, program, websearch, publish |
| `/listen`  | support, feedback, adoption |
| `/program` | plan, program |
| `/topic`   | new, plan, status, report, story, echo |

Run `/topic:status` to see what signals exist for the current topic.
```

### Copilot Instructions Section (Implementation Context)

```markdown
## Signal Skills Available

Before accepting suggestions for new features, check: does this implementation
assume adoption without evidence? Run Signal skills to validate:

- At the planning stage: `/scout`, `/draft`, `/prove` to gather evidence before
  accepting an approach
- While implementing: `/trace`, `/flow`, `/review` to verify the implementation
  matches what signals support

Signal inertia rule: code that ships without evidence of why teams would adopt
it is code that assumes inertia is already solved.
```
```

---

## V-05 — Full Coverage: All Aspirational Patterns Threaded
**Axes**: Phase-indexed vocabulary (C-22) + explicit phase labels (C-23) + secondary already-configured affirmation (C-24) + persistence mechanism (C-20) + adversary framing (C-16) + temporal persistence preamble (C-17) + future-moment anchoring at all decline gates (C-18, C-19)
**Hypothesis**: Threading every C-19 through C-24 pattern into every applicable gate — with non-overlapping phase vocabulary between the planning-stage and implementation-stage decline paths — produces the highest total score by ensuring no exit gate is consequence-free and no two same-phase exits share identical framing.

```markdown
# signal-setup

Inertia is not a concept. It is your real competitor — the force that keeps
teams shipping what they would have shipped without Signal. Inertia wins by
default because the path of least resistance runs straight from idea to
implementation. The question "why would teams do nothing?" only gets asked if
something names it as mandatory. Signal names it. But Signal can only name it
in your sessions if your context knows it exists.

This setup writes one section to CLAUDE.md. That file loads automatically at
the start of every Claude Code session — before the first message, before the
first spec, without any action from you. Configure it now and inertia faces a
named opponent in every session going forward. The write happens once;
the opposition is permanent.

---

## GATE 1 — Detect CLAUDE.md

Read `CLAUDE.md` in the current directory.

- Not found → **GATE 1A**
- Found → **GATE 2**

### GATE 1A — Missing CLAUDE.md

No persistent context file exists. Signal has nowhere to live in this workspace.

Display the full Signal section as a preview (from template below). Then ask:
"No CLAUDE.md found. Create one with the Signal section? (yes/no)"

- Yes → **GATE 3**
- No →
  > "Not created. At the **planning stage** — before your next feature spec
  > is written — there will be no opponent named in your context. The question
  > of what makes inaction likely won't be present when the approach is being
  > chosen; it arrives, if at all, after the commitment is made. Run
  > /signal-setup when ready to name the adversary."

  → STOP

---

## GATE 2 — Check for Existing Signal Section

Scan CLAUDE.md for `## Signal` or `<!-- signal-configured -->`.

- Found → **GATE 2A**
- Not found → **GATE 3**

### GATE 2A — Already Configured

Signal is present. CLAUDE.md loads automatically at session start — not because
you open it, but because Claude Code reads it before the first message. That
means at the planning stage, before a spec exists, before a /draft skill runs,
inertia already has a named opponent in your context. The configuration is
doing its work permanently, in every session, without maintenance.

> "Signal section found. CLAUDE.md auto-loads each session — at the planning
> stage, Signal's skills and the inertia question are present before your first
> message, automatically. The adversary is named before you open the first spec.
> No changes needed."

→ **GATE 5** (offer Copilot update)

---

## GATE 3 — Preview

Generate the full Signal section from the template below. Display it completely.

Ask: "Append this to CLAUDE.md and make Signal permanent in this workspace?
(yes/no)"

- Yes → **GATE 4**
- No →
  > "Not appended. At the **planning stage** — before your next feature spec
  > is committed — Signal's skills won't be in Claude's context. There is no
  > standing prompt to ask what makes inaction the default outcome. The
  > adversary goes unnamed when it matters most. Run /signal-setup when ready."

  → **GATE 5** (or STOP)

---

## GATE 4 — Write

Append the Signal section to CLAUDE.md exactly as previewed. Do not alter
existing content.

> "Appended to CLAUDE.md. Starting with the next session, at the planning stage,
> Signal's vocabulary is present before the first message — inertia is named
> before the first spec is opened. The configuration is permanent and requires
> no maintenance."

→ **GATE 5**

---

## GATE 5 — Offer Copilot Instructions

Ask: "Also update .github/copilot-instructions.md to carry Signal's vocabulary
into GitHub Copilot interactions? (yes/no)"

- No →
  > "Copilot instructions not updated. While **implementing** — when Copilot
  > generates the first endpoint stub or function body for a new feature — there
  > will be no signal vocabulary active in that context. Code will be suggested
  > and accepted before the question 'does this implementation assume adoption?'
  > is present. Run /signal-setup to close that gap."

  → STOP
- Yes → **GATE 6**

---

## GATE 6 — Detect Copilot File

Read `.github/copilot-instructions.md`.

**Not found**:

Show what would be created (Copilot Signal section from template). Ask:
"No .github/copilot-instructions.md found. Create one? (yes/no)"

- No →
  > "Not created. While **implementing**, Copilot has no Signal context — the
  > inertia question is absent at the point of code suggestion. Code gets
  > written before the implementation is interrogated. Run /signal-setup to
  > add it."
  → STOP
- Yes → write Copilot Signal section → **GATE 7**

**Signal section already present**:

Signal is already in Copilot instructions. Inside GitHub Copilot interactions —
while implementing, as completions are suggested for new feature code — Signal's
vocabulary is active in that context. The inertia question operates at the
implementation stage, at the moment of code suggestion, inside the editor.
That is distinct from what CLAUDE.md does: CLAUDE.md protects the planning
stage; Copilot instructions protect the implementation stage. Both are covered.

> "Signal already in Copilot instructions. While implementing — as Copilot
> suggests function bodies and stubs for new feature code — Signal's
> vocabulary is present in that context. The implementation stage is protected:
> the inertia question is active inside your editor, not only at the planning
> stage. No changes made."

→ STOP

**Found, no Signal section**: → **GATE 6A**

### GATE 6A — Confirm Copilot Append

Display the Copilot Signal section (implementation-context framing). Ask:
"Append Signal section to Copilot instructions? (yes/no)"

- Yes → append → **GATE 7**
- No →
  > "Not appended. While **implementing** — as Copilot generates code for a
  > new feature — Signal's inertia question won't be active in that context.
  > The implementation stage proceeds without it. Run /signal-setup to add it."
  → STOP

---

## GATE 7 — Final Report

List all files modified, gates triggered, stages now covered (planning,
implementation), and any remaining gaps with the command to address them.

---

## Signal Section Templates

### CLAUDE.md Section (Planning Context)

```markdown
## Signal
<!-- signal-configured -->

Inertia is the adversary. Before committing to any feature approach, ask:
*why would teams do nothing?*

**Inertia rule**: A topic is not ready until its signals together answer what
makes inaction more likely than adoption.

### Skills

| Namespace | Skills |
|-----------|--------|
| `/scout`   | competitors, market, feasibility, requirements, compliance, naming, stakeholders, positioning |
| `/draft`   | brainstorm, spec, proposal, pitch |
| `/review`  | code, design, customers, users |
| `/flow`    | trigger, throttle, lifecycle, resilience, dataflow, conversation, integration |
| `/trace`   | skill, state, contract, permissions, request, component, migration, deployment |
| `/prove`   | hypothesis, interview, topic, prototype, analysis, synthesize, intelligence, program, websearch, publish |
| `/listen`  | support, feedback, adoption |
| `/program` | plan, program |
| `/topic`   | new, plan, status, report, story, echo |

Run `/topic:status` to see what signals exist for the current topic.
```

### Copilot Instructions Section (Implementation Context)

```markdown
## Signal

Signal skills are available. While implementing a new feature, before accepting
a Copilot suggestion, ask: does this code assume adoption without evidence?

Use Signal at the implementation stage to validate:

- `/trace` — verify the implementation matches what the spec and signals support
- `/flow` — check that behavior under real conditions matches the design
- `/review` — confirm the implementation reflects what customers and users need

**Signal inertia rule**: An implementation that ships without interrogating
adoption evidence treats inertia as already solved. It isn't.

Run `/topic:status` to check what signals exist before accepting an implementation.
```
```

---

## Variation Summary

| ID | Primary Axis | Key Differentiator | Strongest Criteria Hit |
|----|-------------|---------------------|----------------------|
| V-01 | Lifecycle emphasis | Every gate numbered and named; edge cases are first-class gates | C-11, C-12, C-20 |
| V-02 | Inertia as adversary | Inertia named as competitor at every decline gate; "inertia wins" framing | C-16, C-14, C-18 |
| V-03 | Explicit phase labels | Phase category stated directly at each decline ("at the planning stage," "while implementing") | C-23, C-22, C-19 |
| V-04 | Phase labels + secondary gates | Copilot decline draws from implementation-phase vocabulary distinct from planning-phase declines | C-21, C-22, C-23, C-24 |
| V-05 | Full threading | Phase-indexed + labeled + adversary + persistence + secondary-affirm + future-moment at every gate | C-16–C-24 all addressed |
