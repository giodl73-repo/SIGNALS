## Quest Variate — signal-setup — Round 8

**Rubric v8 key additions**: C-22 (phase-indexed consequence anchors, not tool-indexed), C-23 (explicit phase labels at decline points), C-24 (secondary already-configured paths affirm tool-local consequence). Denominator: 16.

---

## V-01 — Single Axis: Lifecycle Emphasis (Explicit Named Gates)

**Variation axis**: How explicitly the skill names and sequences lifecycle phases
**Hypothesis**: Numbered, labeled gates with outcome triads (PROCEED/SKIP/EXIT) eliminate implicit sequencing and force every exit path into view.

---

```markdown
---
skill: signal-setup
version: 1
---

# Signal Setup

## Why This Configuration Must Exist

There is a force that wins every feature decision when no one intervenes: inertia.
It is not passive. It is the active continuation of what already exists — the tool
already licensed, the workflow already memorized, the vendor contract that renews
automatically. Inertia does not argue. It simply continues.

Signal names the question that defeats it: "Why would target teams do nothing instead?"

This step writes that question into your workspace context permanently. CLAUDE.md
loads at the start of every session. Once configured, the inertia question is present
every time you discuss a feature — not because you remembered to ask, but because
the setup made it ambient. The configuration must persist because the question must
persist. You are making that choice now.

---

## Gate Structure

Six named gates. Each has one of three outcomes: **PROCEED**, **SKIP** (with
reason stated), or **EXIT** (with consequence named). No gate is implicit.

---

## GATE 1 — Locate CLAUDE.md

Read the workspace root. Check for CLAUDE.md.

**Found:** → GATE 2.

**Not found:** Ask:
> "No CLAUDE.md exists here. Signal needs a persistent context file to load the
> inertia question every session. Create CLAUDE.md now?"

- Yes: Create. → GATE 3 (skip GATE 2).
- No: EXIT.
  > "CLAUDE.md not created. At the planning stage — when a feature topic is open
  > and you are deciding whether to build — there will be no persistent instruction
  > in your workspace asking 'why would teams do nothing instead?' That question
  > will not be present at the planning stage unless you return to this step."

---

## GATE 2 — Detect Existing Signal Section

Read CLAUDE.md. Search for `## Signal` or `<!-- signal-setup -->`.

**Found:** SKIP.
> "Signal section already present in CLAUDE.md. No write needed.
>
> Your configuration is active. CLAUDE.md loads automatically at the start of
> every session — the mechanism that keeps the inertia question present is the
> load itself, not you remembering to ask. The question 'why would teams do
> nothing?' is already in scope at the planning stage, every time, without
> manual invocation."

→ GATE 5.

**Not found:** → GATE 3.

---

## GATE 3 — Preview Signal Section

Before any write, display the content to be appended:

---
**Preview — Signal Section (to be appended to CLAUDE.md):**

```markdown
## Signal

Signal is installed in this workspace. Use Signal skills to gather evidence
before committing to build.

Namespaces:
/scout · /draft · /review · /flow · /trace · /prove · /listen · /program · /topic

### Inertia Rule
Before any feature topic is recommended for build, ask: "Why would target teams
do nothing instead?" A topic without a Signal-backed answer to this question is
not ready.
```
---

→ GATE 4.

---

## GATE 4 — Confirm Write to CLAUDE.md

Ask:
> "Append this Signal section to CLAUDE.md?"

- Yes: Append. → GATE 5.
- No: EXIT.
  > "CLAUDE.md not updated. At the planning stage — before the next feature topic
  > is named and you want a structured challenge to whether it deserves to be built
  > — there will be no standing instruction in your workspace context to ask the
  > inertia question. The next build decision begins at the planning stage without
  > a named opponent."

---

## GATE 5 — Locate .github/copilot-instructions.md

Check for `.github/copilot-instructions.md`.

**Not found:**
> "No .github/copilot-instructions.md found. Skipping Copilot configuration."
→ GATE 7.

**Found:** → GATE 6.

---

## GATE 6 — Detect and Offer Copilot Update

Read `.github/copilot-instructions.md`. Search for existing Signal section.

**Signal section already present:** SKIP.
> "Signal section already present in copilot-instructions.md. No write needed.
>
> Your Copilot configuration is active. During the implementation phase — while
> Copilot is generating code — the inertia question is already in that context.
> When Copilot receives a prompt to implement a feature, the standing instruction
> to ask 'why would teams do nothing?' is present in its working scope. The
> implementation phase is already covered."

→ GATE 7.

**Not found:** Ask:
> "Would you also like to update .github/copilot-instructions.md with the Signal
> section? This places the inertia check in Copilot's context — present during
> the implementation phase, not only at the planning stage."

- Yes: Append. → GATE 7.
- No: EXIT this gate.
  > "copilot-instructions.md not updated. During the implementation phase — before
  > Copilot generates the first function body or endpoint for a feature — there
  > will be no instruction in that context asking whether the feature was challenged
  > at the planning stage. The implementation phase proceeds without the inertia
  > check in Copilot's scope."

---

## GATE 7 — Report Outcome

| File | Status |
|------|--------|
| CLAUDE.md | [written \| created \| already configured \| skipped by user] |
| .github/copilot-instructions.md | [written \| already configured \| not found \| skipped by user] |

Signal setup complete. Inertia now has a named opponent in the contexts listed above.
```

---

## V-02 — Single Axis: Phrasing Register (Conversational / Descriptive)

**Variation axis**: Tone and voice — formal/imperative vs. conversational/explanatory
**Hypothesis**: A conversational register that walks the user through each step as a guided conversation increases comprehension of stakes without sacrificing structural completeness or consequence naming.

---

```markdown
---
skill: signal-setup
version: 1
---

# Signal Setup

Let me configure Signal in your workspace.

Here's what's about to happen and why it matters.

You've installed Signal skills — a toolkit for gathering evidence before you
commit to a feature. But having skills available isn't the same as having them
work for you. Every time Claude starts a session in your workspace, it reads
CLAUDE.md to understand context. If the Signal section isn't there, the inertia
question — "why would teams do nothing?" — starts every session unasked.

Inertia is not a concept; it's a competitor. It wins when nothing challenges it.
This setup writes the challenge in once. From that point, every session carries it
automatically. You don't need to remember. Claude does.

Let me check what's in your workspace.

---

**Step 1: Finding your CLAUDE.md**

I'll look for CLAUDE.md at the workspace root.

If I find it, I'll check whether a Signal section is already there.

If I don't find it, I'll ask whether you want me to create one. If you'd rather
not, let me be clear about what stays missing: at the planning stage, when you're
deciding whether a feature should exist, there will be no standing instruction in
your workspace asking Claude to challenge that decision. The inertia question will
need to be asked manually, or it won't be asked at all.

---

**Step 2: Checking for an existing Signal section**

If CLAUDE.md exists, I'll search for a Signal section.

If one's already there — the work is done. Your configuration is active: CLAUDE.md
loads at the start of every session, which means the inertia question is already in
scope at the planning stage without you having to invoke it. CLAUDE.md's automatic
load is the mechanism that keeps it present, session after session.

If there's no Signal section yet, I'll move on to showing you what I'd add.

---

**Step 3: Showing you what I'd write**

Before touching any file, I'll show you exactly what would be appended:

```markdown
## Signal

Signal is installed. Use Signal skills to gather evidence before committing to build.

Namespaces:
/scout · /draft · /review · /flow · /trace · /prove · /listen · /program · /topic

### Inertia Rule
Before any feature topic is recommended for build, ask: "Why would target teams
do nothing instead?" A topic without a Signal-backed answer is not ready.
```

---

**Step 4: Asking before writing**

I'll ask for confirmation before appending anything.

If you say no, that's fine — but I'll name what remains unresolved: at the planning
stage, before the next feature topic is open and you want a structured challenge to
whether it should be built, there will be no standing instruction in your workspace
context to raise that question. The next build decision begins without a named opponent.

---

**Step 5: Copilot instructions (optional)**

If `.github/copilot-instructions.md` exists, I'll offer to add the Signal section
there too.

If it's already there: Signal is active in Copilot's context too. During the
implementation phase — while Copilot is generating code — the inertia question is
already present in its working scope. No action needed.

If it's not there and you decide to skip it: during the implementation phase, before
Copilot generates the first function body or endpoint, there will be no instruction
in that context asking whether the feature was challenged at the planning stage. The
implementation phase runs without the inertia check in Copilot's scope.

---

**Step 6: Reporting what happened**

When everything is done, I'll give you a clear summary: what was written, what was
skipped, and where each file ended up.
```

---

## V-03 — Single Axis: Inertia Framing (Adversary-First)

**Variation axis**: How prominently inertia is foregrounded — as a named opponent, not a concept
**Hypothesis**: Naming inertia as an active competitor in the opening and threading adversary language through every gate produces the strongest, most specific consequence anchors at every exit point.

---

```markdown
---
skill: signal-setup
version: 1
---

# Signal Setup

## Name the Opponent

There is a force in every product organization that requires no resources,
no advocates, and no approval to win. It wins by default when nothing
challenges it. It has already won more features than you know.

Its name is inertia.

Inertia is not hesitation. It is the institutional weight of what is already
happening: the licensed tool that renews automatically, the workflow teams
have already memorized, the integration nobody wants to renegotiate. Inertia
does not make arguments. It simply continues.

Signal exists to ask the one question inertia cannot answer: "Why would target
teams do nothing instead?" This setup writes that question into your workspace
context permanently. CLAUDE.md loads at the start of every session — once
configured, the inertia question is present every time you discuss a feature,
without you needing to invoke it.

Configuration must persist because the question must persist. You are choosing
a side. This step completes that choice.

---

## Gates

### GATE 1 — Workspace Scan

Read workspace root. Check for:
- CLAUDE.md (and if found, whether it contains a Signal section)
- .github/copilot-instructions.md (and if found, whether it contains a Signal section)

Report findings before proceeding to any write gate.

---

### GATE 2 — CLAUDE.md

**Not found:**
> "No CLAUDE.md found. Without it, there is no file for the inertia question
> to live in — nothing for Claude to load at session start. Create CLAUDE.md
> now with the Signal section?"

- Yes: Create. → GATE 3 (preview).
- No:
  > "CLAUDE.md not created. At the planning stage — before a feature topic is
  > named and you need a structured way to ask whether it should be built — there
  > will be no standing instruction in your workspace context to raise the inertia
  > question. Inertia remains unnamed at the planning stage."

**Found, Signal section already present:**
> "CLAUDE.md already carries the inertia question. The named opponent is present
> at the planning stage — in your workspace context, every session, loaded
> automatically. You do not need to summon it. Inertia already has an adversary
> here. No write needed."

→ GATE 5.

**Found, no Signal section:**
→ GATE 3.

---

### GATE 3 — Preview

Show the Signal section to be appended:

```markdown
## Signal

Signal is installed. Use Signal skills to challenge feature decisions before build.

Namespaces:
/scout · /draft · /review · /flow · /trace · /prove · /listen · /program · /topic

### The Inertia Rule
Before any feature topic is recommended for build, ask: "Why would target teams
do nothing instead?" A topic without a Signal-backed answer to this question is
not ready. Inertia wins by default. Signal exists to prevent that.
```

---

### GATE 4 — Confirm Write to CLAUDE.md

> "Append this Signal section to CLAUDE.md?"

- Yes: Append. → GATE 5.
- No:
  > "CLAUDE.md not updated. At the planning stage — when the next feature topic
  > is open and the question 'should we build this?' is live — there will be no
  > instruction in your workspace context naming inertia as the opponent. The next
  > build decision begins at the planning stage with inertia already ahead."

---

### GATE 5 — .github/copilot-instructions.md

**Not found:**
> ".github/copilot-instructions.md not found. Copilot configuration skipped."
→ GATE 7.

**Found, Signal section already present:**
> "Signal is already in copilot-instructions.md. Inertia has a named opponent
> during the implementation phase as well. While Copilot is generating code,
> the standing instruction to ask 'why would teams do nothing?' is present in
> its working context. No write needed: the implementation phase is already
> covered."

→ GATE 7.

**Found, no Signal section:**
→ GATE 6.

---

### GATE 6 — Confirm Write to Copilot Instructions

> "Would you also like to add the Signal section to .github/copilot-instructions.md?
>
> This extends the inertia challenge into the implementation phase: while Copilot
> is generating code, not only while you are planning, inertia will have a named
> opponent in that context too."

- Yes: Append. → GATE 7.
- No:
  > "copilot-instructions.md not updated. During the implementation phase — as
  > Copilot generates the first endpoint or function body — there will be no
  > instruction in that context asking whether the feature it is building was
  > challenged at the planning stage. Inertia has no named opponent in Copilot's
  > implementation scope."

---

### GATE 7 — Outcome Report

| File | Status |
|------|--------|
| CLAUDE.md | [written \| created \| already configured \| skipped] |
| .github/copilot-instructions.md | [written \| already configured \| not found \| skipped] |

Inertia now has a named opponent in the contexts listed above.
```

---

## V-04 — Single Axis: Role Sequence (Detection-First)

**Variation axis**: Order of operations — workspace scan runs before motivational framing, not after
**Hypothesis**: Running detection first and reporting state before delivering motivation allows the framing to be contextually specific (e.g., "I found X missing" vs. abstract preamble) and produces cleaner conditional gate logic.

---

```markdown
---
skill: signal-setup
version: 1
---

# Signal Setup

## Phase 1 — Workspace Scan (Run Before Any Explanation)

Before framing or motivation, collect workspace state.

1. Check for CLAUDE.md at workspace root.
2. If found, search for Signal section (`## Signal` or `<!-- signal-setup -->`).
3. Check for `.github/copilot-instructions.md`.
4. If found, search for Signal section there too.

Report findings immediately:

> **Workspace scan:**
> - CLAUDE.md: [found / not found] — Signal section: [present / absent / N/A]
> - copilot-instructions.md: [found / not found] — Signal section: [present / absent / N/A]

Now proceed to Phase 2.

---

## Phase 2 — Context

With workspace state known, explain what Signal configuration does and why it matters.

Signal is a feature decision toolkit. Its operating premise is the inertia rule:
before a feature topic is ready to build, someone must produce an answer to "why
would target teams do nothing instead?" Without a standing instruction in CLAUDE.md,
that question starts every session unasked.

This setup writes the question in permanently. CLAUDE.md loads at the start of every
session — the inertia check becomes ambient, not manual. You chose Signal. This step
completes that choice.

Proceed to Phase 3 based on what was found in Phase 1.

---

## Phase 3 — Gates

---

### GATE 1 — Create or Use CLAUDE.md

**CLAUDE.md not found:**
> "CLAUDE.md not found (confirmed in scan). Signal needs a persistent file to load
> the inertia question every session. Create CLAUDE.md now?"

- Yes: Create. → GATE 3 (skip GATE 2).
- No:
  > "CLAUDE.md not created. At the planning stage — before you sit with a feature
  > topic and want structured help asking whether it deserves to be built — there
  > will be no standing instruction in this workspace to raise the inertia question.
  > That question remains your responsibility to ask manually."

**CLAUDE.md found:** → GATE 2.

---

### GATE 2 — Signal Section in CLAUDE.md

**Present:**
> "Signal section confirmed in CLAUDE.md. The inertia question is present at the
> planning stage. CLAUDE.md's automatic load is the mechanism: every session begins
> with the question already in scope — you do not invoke it, the context load does.
> The persistence is structural, not behavioral."

→ GATE 5.

**Absent:** → GATE 3.

---

### GATE 3 — Preview

Show content to be appended:

```markdown
## Signal

Signal is installed in this workspace.

Namespaces:
/scout · /draft · /review · /flow · /trace · /prove · /listen · /program · /topic

### Inertia Rule
Before any feature topic is recommended for build, ask: "Why would target teams
do nothing instead?" A topic without a Signal-backed answer to this question is
not ready.
```

---

### GATE 4 — Confirm Write to CLAUDE.md

> "Append Signal section to CLAUDE.md?"

- Yes: Append. → GATE 5.
- No:
  > "CLAUDE.md not updated. At the planning stage — before the next feature decision
  > opens — there will be no instruction in this workspace asking whether the case for
  > building holds up against inertia. The question 'why do nothing?' will not be in
  > the room at the planning stage."

---

### GATE 5 — Copilot File Status

**Not found:**
> "No .github/copilot-instructions.md found. Copilot step skipped."
→ GATE 7.

**Found, Signal section present:**
> "Signal section confirmed in copilot-instructions.md. During the implementation
> phase — while Copilot is generating code — the inertia question is present in
> that context. Copilot already carries the standing instruction in this workspace.
> No write needed."

→ GATE 7.

**Found, no Signal section:** → GATE 6.

---

### GATE 6 — Confirm Write to Copilot Instructions

> "Add Signal section to .github/copilot-instructions.md?
>
> This extends the inertia check into the implementation phase: the question
> will be present while Copilot generates code, not only while you plan."

- Yes: Append. → GATE 7.
- No:
  > "copilot-instructions.md not updated. During the implementation phase — before
  > Copilot generates the first endpoint or function body — there will be no
  > instruction in that context asking whether the feature was challenged at the
  > planning stage. The implementation phase runs without the inertia check."

---

## Phase 4 — Outcome Report

> **Signal Setup Summary**
>
> | File | Outcome |
> |------|---------|
> | CLAUDE.md | [written / created / already configured / skipped] |
> | .github/copilot-instructions.md | [written / already configured / not found / skipped] |
```

---

## V-05 — Combined: Phase-Indexed Anchors + Explicit Phase Labels + Tool-Local Affirm

**Variation axes combined**: C-22 (phase-indexed vocabulary, not tool-name substitution) + C-23 (explicit phase labels at every decline point) + C-24 (tool-local affirm at secondary already-configured gates)
**Hypothesis**: When decline anchors draw vocabulary from distinct development phases and name those phases explicitly as categories, and when secondary gates affirm tool-local consequences rather than reusing primary-gate language, all three new criteria are satisfied simultaneously without structural redundancy.

---

```markdown
---
skill: signal-setup
version: 1
---

# Signal Setup

## Why This Configuration Must Exist

Inertia is not a concept. It is a competitor. It wins every feature decision that
goes unchallenged. The existing tool keeps getting renewed. The team's current
workflow keeps being defended. The vendor contract auto-renews. Inertia does not
make arguments. It simply continues.

Signal names the question that names inertia: "Why would target teams do nothing
instead?" This step writes that question into two contexts: your planning context
(CLAUDE.md, where feature decisions begin) and your implementation context
(Copilot instructions, where those decisions become code).

The configuration must persist because the question must persist. CLAUDE.md loads
automatically at the start of every session. Once written, the inertia challenge is
ambient — present at the planning stage without you having to remember it. This step
makes that true. You are choosing it now.

---

## Gates

### GATE 1 — Locate CLAUDE.md

Check for CLAUDE.md at workspace root.

**Not found:**
> "No CLAUDE.md found. Signal needs a persistent context file to load the inertia
> question each session. Create CLAUDE.md now?"

- Yes: Create. → GATE 3.
- No:
  > "CLAUDE.md not created. At the planning stage — when a feature topic is open
  > and you are deciding whether to build — there will be no persistent instruction
  > in your workspace asking 'why would teams do nothing instead?' That question will
  > not be present at the planning stage unless you return to this step."

**Found:** → GATE 2.

---

### GATE 2 — Detect Existing Signal Section in CLAUDE.md

Search CLAUDE.md for `## Signal` or `<!-- signal-setup -->`.

**Present:**
> "Signal section already in CLAUDE.md. No write needed.
>
> Your planning context is configured. CLAUDE.md loads automatically at the start
> of every session — that load is the mechanism that keeps the inertia question
> present at the planning stage. Every time you discuss a feature, 'why would teams
> do nothing?' is already in scope. You do not invoke it. The session load does."

→ GATE 5.

**Absent:** → GATE 3.

---

### GATE 3 — Preview

Before any write, display the Signal section to be appended:

---
**Preview — to be appended to CLAUDE.md:**

```markdown
## Signal

Signal is installed in this workspace. Use Signal skills to gather evidence
before committing to build.

Namespaces:
/scout · /draft · /review · /flow · /trace · /prove · /listen · /program · /topic

### Inertia Rule
Before any feature topic is recommended for build, ask: "Why would target teams
do nothing instead?" A topic without a Signal-backed answer to this question is
not ready.
```
---

→ GATE 4.

---

### GATE 4 — Confirm Write to CLAUDE.md

> "Append this Signal section to CLAUDE.md?"

- Yes: Append. → GATE 5.
- No:
  > "CLAUDE.md not updated. At the planning stage — before you commit a feature topic
  > and want a structured challenge to whether it deserves to be built — there will be
  > no instruction in your workspace context asking the inertia question. The next
  > feature decision begins at the planning stage without a named opponent."

---

### GATE 5 — Locate .github/copilot-instructions.md

Check for `.github/copilot-instructions.md`.

**Not found:**
> "No .github/copilot-instructions.md found. Copilot configuration skipped."
→ GATE 7.

**Found:** → GATE 6.

---

### GATE 6 — Detect and Offer Copilot Update

Search copilot-instructions.md for existing Signal section.

**Already present:**
> "Signal section already in copilot-instructions.md. No write needed.
>
> Your implementation context is configured. While you are implementing — as
> Copilot generates code in response to your prompts — the inertia check is
> already present in its working context. When Copilot receives a prompt to
> build a feature, the standing instruction to ask 'why would teams do nothing?'
> is active during the implementation phase, inside the Copilot interaction
> itself. The implementation phase is already covered."

→ GATE 7.

**Not found:**
> "Would you also like to add the Signal section to .github/copilot-instructions.md?
>
> This extends the inertia check into the implementation phase: while you are
> implementing, before Copilot generates the first function body or endpoint, the
> question will be present in its context — not only at the planning stage."

- Yes: Append. → GATE 7.
- No:
  > "copilot-instructions.md not updated. While you are implementing — before Copilot
  > generates the first endpoint or function body for a feature — there will be no
  > instruction in that context asking whether the feature was challenged at the
  > planning stage. The implementation phase proceeds without the inertia check in
  > Copilot's scope."

---

### GATE 7 — Outcome Report

| File | Outcome |
|------|---------|
| CLAUDE.md | [written \| created \| already configured \| skipped by user] |
| .github/copilot-instructions.md | [written \| already configured \| not found \| skipped by user] |

Signal setup complete. The inertia question is now present in the contexts listed above.
```

---

## Variation Summary

| Variation | Axis | Key C-22/23/24 handling |
|-----------|------|-------------------------|
| V-01 | Lifecycle emphasis — explicit gate triads | GATE 4 decline: "planning stage" label; GATE 6 decline: "implementation phase" label; GATE 6 affirm: "implementation phase... Copilot's working scope" |
| V-02 | Phrasing register — conversational steps | Phase labels embedded in conversational explanation; GATE 6 affirm uses "implementation phase... Copilot's working context" language |
| V-03 | Inertia framing — adversary-first | "named opponent" threaded through every gate; phase-native vocabulary at each exit; GATE 5 affirm: "implementation phase... working context" distinct from GATE 2 affirm |
| V-04 | Role sequence — detection-first | Scan results precede framing; GATE 4/6 declines use "planning stage" / "implementation phase" labels explicitly; GATE 5 affirm names "implementation phase" separately |
| V-05 | Combined: C-22+C-23+C-24 all axes | Preamble names both contexts (planning/implementation); every decline carries explicit phase-category label; GATE 6 already-configured affirm describes Copilot-specific in-context behavior, not a restatement of GATE 2 |
