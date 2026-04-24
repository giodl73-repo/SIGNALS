# mock-accept — Skill Body Prompt Variations (V-01 through V-05)

---

## V-01 — Single-Axis: Role Sequence
**Axis**: Auto-flag gate runs as a blocking pre-pass before evaluation roles engage.
**Hypothesis**: Running the structural gate first as a hard checkpoint — before any evaluator sees the mock — eliminates C-02 failures by preventing persuasive mock quality from ever reaching evaluation logic.

---

```markdown
You are running /mock-accept {topic}.

## Inputs

Locate the source mock artifact:
  simulations/mock/{topic}-mock-{date}.md

Read it fully before proceeding. If not found, halt and report the missing path.

---

## Phase 1 — Auto-Flag Gate (BLOCKING)

Before any evaluation role runs, apply the auto-flag rules to every namespace in the
mock artifact. These rules are unconditional. No evaluation outcome can override them.

For each namespace, check:

  AUTO-FLAG RULE TABLE
  ┌─────────────────────────┬──────────────────┬──────────────────────────────────────────┐
  │ Namespace property      │ Decision         │ Trigger condition                        │
  ├─────────────────────────┼──────────────────┼──────────────────────────────────────────┤
  │ EVIDENCE-HEAVY          │ REAL-REQUIRED    │ prove, listen — always                   │
  │ TIER-CRITICAL           │ REAL-REQUIRED    │ flow, trace — always                     │
  │ COMPLIANCE              │ REAL-REQUIRED    │ Any namespace tagged compliance-sensitive │
  └─────────────────────────┴──────────────────┴──────────────────────────────────────────┘

Mark every auto-flagged namespace with:
  Decision: REAL-REQUIRED
  Trigger: [AUTO-FLAG: EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE]

Do not proceed to Phase 2 for these namespaces. Their decision is final.

List all auto-flagged namespaces before continuing.

---

## Phase 2 — Evaluation Panel (Non-Auto-Flagged Namespaces Only)

For each namespace that survived Phase 1 without an auto-flag, run the three-role
evaluation panel in this fixed sequence:

  ROLE 1 — Architect
  Review the mock's structural coverage: does it capture the namespace's contract
  boundaries, error surfaces, and state transitions at a level sufficient for
  tier-1 pre-commitment validation?

  Verdict must be one of:
    CONSISTENT-WITH-ARCHITECTURE
    STRUCTURALLY-INSUFFICIENT

  ROLE 2 — Strategy
  Review against the tier decision this namespace is meant to inform.
  Does mock coverage give the team confidence to proceed to the next gate?

  Verdict must be one of:
    ADEQUATE FOR TIER 1
    INADEQUATE FOR TIER 1

  ROLE 3 — PM
  Review coverage breadth: are the scenarios representative of real usage patterns
  and edge conditions a product team would need before committing?

  Verdict must be one of:
    REPRESENTATIVE
    INCOMPLETE

Decision rule:
  All three verdicts positive → MOCK-ACCEPTED
  Any verdict negative       → REAL-REQUIRED (record which role failed)

---

## Phase 3 — Structural Slot Population (MOCK-ACCEPTED only)

For every namespace receiving MOCK-ACCEPTED, populate BOTH structural slots.
Omitting either slot is a SLOT-VIOLATION and the decision reverts to REAL-REQUIRED.

  Slot 1 — Structural position (SQ-1 tier-decision anchor)
  State the specific tier-1 decision this namespace's mock coverage supports.
  REQUIRED format: "[Namespace] mock coverage supports the [specific tier decision]
  determination at the [gate name] gate."

  Example PASS: "scout mock coverage supports the build-vs-buy determination
  at the Feasibility Gate."
  Example FAIL (SLOT-VIOLATION): "scout mock coverage supports tier-1
  decision-making." ← no named decision

  Slot 2 — Contrast
  Name a contrasting namespace type and state the structural factor that
  distinguishes why IT requires real data while this namespace does not.

  Example PASS: "Unlike prove (EVIDENCE-HEAVY), scout signals do not depend on
  observed user behavior — competitive positioning is structurally enumerable
  from public data."
  Example FAIL (CONTRAST-INCOMPLETE): "Unlike prove, scout is less evidence-dependent."
  ← no structural factor named

---

## Phase 4 — In-Place Edit + Canary

Using the Edit tool, update the source mock artifact in-place.

For every namespace:
  Replace:  Status: MOCK (awaiting review)
  With:     Status: [final decision]

After all edits are applied, verify by re-reading the artifact and counting
remaining "Status: MOCK (awaiting review)" instances.

Issue the Canary assertion verbatim only after verification:
  "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."

If any Status field was not updated, suppress the Canary and list the remaining fields.
Do NOT emit the Canary before verification. A premature Canary is a hard fail.

---

## Phase 5 — Review Artifact

Write to: simulations/mock/{topic}-review-{date}.md

Include:
  1. Coverage Review table
     Columns: Namespace | Category | Decision | Trigger
     Order: REAL-REQUIRED auto-flagged → REAL-REQUIRED evaluation → MOCK-ACCEPTED

  2. Cross-namespace risk statement
     Identify the single highest-risk gap namespace, the specific tier decision
     at risk, and urgency: BLOCKING | HIGH | MEDIUM

---

## Phase 6 — Next Steps

List next actions in /skill {topic} invocation format:

  Priority 1 — Critical (auto-flagged REAL-REQUIRED):
    /[skill-id] {topic} -- [namespace]: Status REAL-REQUIRED (AUTO-FLAG: [trigger])

  Priority 2 — Evaluation-driven REAL-REQUIRED:
    /[skill-id] {topic} -- [namespace]: Status REAL-REQUIRED ([role] verdict: [verdict])

  Priority 3 — MOCK-ACCEPTED (cleared for simulation):
    /[skill-id] {topic} -- [namespace]: Status MOCK-ACCEPTED, proceed to simulation
```

---

## V-02 — Single-Axis: Output Format
**Axis**: Table-first structured output — every decision rendered in a grid before any prose explanation appears.
**Hypothesis**: Front-loading a machine-readable decision table forces completeness (C-01) and makes reason-code violations (C-03) immediately visible at a glance, reducing both omissions and paraphrase errors.

---

```markdown
You are running /mock-accept {topic}.

## Input

Read: simulations/mock/{topic}-mock-{date}.md
Halt if not found — report missing path.

---

## Step 1 — Decision Grid

After reading the mock artifact, produce the Decision Grid FIRST before any
explanation or reasoning. No prose before this table.

  DECISION GRID
  ┌───────────┬──────────────────┬──────────────────────────────────────────────┬──────────────────────┐
  │ Namespace │ Decision         │ Reason / Trigger                             │ Auto-flag?           │
  ├───────────┼──────────────────┼──────────────────────────────────────────────┼──────────────────────┤
  │ scout     │ [decision]       │ [exact code or AUTO-FLAG trigger]            │ [YES/NO]             │
  │ draft     │ [decision]       │ [exact code or AUTO-FLAG trigger]            │ [YES/NO]             │
  │ review    │ [decision]       │ [exact code or AUTO-FLAG trigger]            │ [YES/NO]             │
  │ flow      │ [decision]       │ [exact code or AUTO-FLAG trigger]            │ [YES/NO]             │
  │ trace     │ [decision]       │ [exact code or AUTO-FLAG trigger]            │ [YES/NO]             │
  │ prove     │ [decision]       │ [exact code or AUTO-FLAG trigger]            │ [YES/NO]             │
  │ listen    │ [decision]       │ [exact code or AUTO-FLAG trigger]            │ [YES/NO]             │
  │ program   │ [decision]       │ [exact code or AUTO-FLAG trigger]            │ [YES/NO]             │
  │ topic     │ [decision]       │ [exact code or AUTO-FLAG trigger]            │ [YES/NO]             │
  └───────────┴──────────────────┴──────────────────────────────────────────────┴──────────────────────┘

Rules for the Decision column:
  MOCK-ACCEPTED  — only if NOT auto-flagged AND all three evaluation roles pass
  REAL-REQUIRED  — if auto-flagged OR any evaluation role fails

Rules for the Reason / Trigger column:
  Auto-flagged namespaces: write exactly "AUTO-FLAG: EVIDENCE-HEAVY",
    "AUTO-FLAG: TIER-CRITICAL", or "AUTO-FLAG: COMPLIANCE"
  MOCK-ACCEPTED namespaces: write exactly one or both of:
    STRUCTURAL-COVERAGE-SUFFICIENT
    DOMAIN-KNOWLEDGE-CONSISTENT
  No paraphrases. No invented codes. No prose summaries in this column.

Self-check before proceeding: count rows. Must equal 9 (all namespaces present, no duplicates).

---

## Step 2 — Auto-Flag Verification

State explicitly for each auto-flagged namespace (prove, listen, flow, trace, and
any compliance-tagged namespace):

  "[Namespace] — REAL-REQUIRED. Auto-flag rule: [EVIDENCE-HEAVY | TIER-CRITICAL |
  COMPLIANCE]. This decision is not subject to evaluation override."

If any of these namespaces appear in the Decision Grid as MOCK-ACCEPTED, return
to Step 1 and correct before continuing.

---

## Step 3 — Evaluation Panel Summaries (Non-Auto-Flagged Only)

For each non-auto-flagged namespace, provide a three-role verdict block:

  Namespace: [name]
  Architect verdict: [CONSISTENT-WITH-ARCHITECTURE | STRUCTURALLY-INSUFFICIENT]
  Strategy verdict:  [ADEQUATE FOR TIER 1 | INADEQUATE FOR TIER 1]
  PM verdict:        [REPRESENTATIVE | INCOMPLETE]
  Outcome:           [MOCK-ACCEPTED | REAL-REQUIRED — driven by: [role]]

---

## Step 4 — Structural Slot Table (MOCK-ACCEPTED namespaces only)

Produce a second table for structural slot population.
Every MOCK-ACCEPTED namespace must have BOTH slots. Missing slots = SLOT-VIOLATION.

  STRUCTURAL SLOT TABLE
  ┌───────────┬────────────────────────────────────────────────────┬────────────────────────────────────────────────────┐
  │ Namespace │ Slot 1 — SQ-1 Tier-Decision Anchor                │ Slot 2 — Contrasting Namespace + Structural Factor │
  ├───────────┼────────────────────────────────────────────────────┼────────────────────────────────────────────────────┤
  │ [name]    │ "[NS] mock supports [specific tier decision] at    │ "Unlike [NS2] ([property]), [NS] does not depend   │
  │           │  [gate name] gate."                               │  on [factor] — [structural reason]."              │
  └───────────┴────────────────────────────────────────────────────┴────────────────────────────────────────────────────┘

Slot 1 fail pattern (SLOT-VIOLATION): generic statement without a named tier decision.
Slot 2 fail pattern (CONTRAST-INCOMPLETE): contrast without naming the structural factor.

---

## Step 5 — In-Place Edit + Canary

Using the Edit tool, update simulations/mock/{topic}-mock-{date}.md in-place.

For each namespace, replace:
  Status: MOCK (awaiting review)
with:
  Status: [decision from Step 1 grid]

After all edits, re-read the file and count remaining "Status: MOCK (awaiting review)" strings.

Canary assertion — issue verbatim only after count verification:
  "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."

Suppress Canary and list remaining fields if count > 0.

---

## Step 6 — Coverage Review Artifact

Write to: simulations/mock/{topic}-review-{date}.md

Contents:
  1. Copy of Decision Grid from Step 1 (canonical record)
  2. Copy of Structural Slot Table from Step 4
  3. Cross-namespace risk statement:
     Single highest-risk gap namespace + specific tier decision at risk +
     urgency: BLOCKING | HIGH | MEDIUM
     (A list of risks without a single selection does not satisfy this requirement.)

---

## Step 7 — Next Steps

Format: /{skill-id} {topic} -- {Artifact state}

  Critical (auto-flagged):
    /[skill-id] {topic} -- [namespace]: REAL-REQUIRED (AUTO-FLAG: [trigger])

  Evaluation-driven REAL-REQUIRED:
    /[skill-id] {topic} -- [namespace]: REAL-REQUIRED ([role]: [verdict])

  MOCK-ACCEPTED:
    /[skill-id] {topic} -- [namespace]: MOCK-ACCEPTED, simulation ready
```

---

## V-03 — Single-Axis: Inertia Framing
**Axis**: REAL-REQUIRED is the default status quo; MOCK-ACCEPTED requires a positive case to be built and defended.
**Hypothesis**: Framing REAL-REQUIRED as the safe default forces the model to actively argue for MOCK-ACCEPTED rather than sliding toward acceptance on a strong-looking mock — directly countering the C-02 failure pattern.

---

```markdown
You are running /mock-accept {topic}.

## Framing

The default decision for every namespace is REAL-REQUIRED.

MOCK-ACCEPTED is not the neutral outcome. It is a claim: that mock coverage is
sufficient to substitute for real data at this tier. That claim requires a
positive case. If no positive case can be made, the decision stays REAL-REQUIRED.

This framing is not a tie-breaker. It is the operating stance.

---

## Input

Read: simulations/mock/{topic}-mock-{date}.md
If not found, halt and report the missing path.

---

## Pass 1 — Identify Non-Starters

Certain namespace properties make mock coverage structurally insufficient regardless
of mock quality. Identify these first and close them immediately.

REAL-REQUIRED regardless of mock quality:
  - prove: EVIDENCE-HEAVY — depends on observed user behavior, not enumerable structures
  - listen: EVIDENCE-HEAVY — adoption and support signals require real feedback loops
  - flow: TIER-CRITICAL — runtime boundary behavior cannot be structurally simulated
  - trace: TIER-CRITICAL — permission and state transitions require live execution context
  - Any compliance-tagged namespace

For each non-starter:
  Decision: REAL-REQUIRED
  Trigger: AUTO-FLAG: [EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE]
  Note: "No evaluation performed. Auto-flag is unconditional."

List all non-starters before proceeding. This list is final.

---

## Pass 2 — Build the Case for MOCK-ACCEPTED (Remaining Namespaces)

For each namespace not closed in Pass 1, attempt to build a positive case for
MOCK-ACCEPTED. You must succeed on all three dimensions or the default holds.

  DIMENSION 1 — Structural sufficiency (Architect role)
  Question: Does the mock capture the namespace's contract boundaries, error surfaces,
  and state transitions at a level sufficient for tier-1 pre-commitment validation?

  To pass: verdict must be CONSISTENT-WITH-ARCHITECTURE.
  If the mock is thin on any contract boundary or error surface: verdict is
  STRUCTURALLY-INSUFFICIENT and the case for MOCK-ACCEPTED fails here.

  DIMENSION 2 — Strategic adequacy (Strategy role)
  Question: Does this mock give the team sufficient confidence to proceed through
  the next tier gate without real data?

  To pass: verdict must be ADEQUATE FOR TIER 1.
  If a tier decision requires signals that only real usage produces: verdict is
  INADEQUATE FOR TIER 1 and the case fails here.

  DIMENSION 3 — Representative coverage (PM role)
  Question: Are the scenarios in this mock representative of real usage patterns
  and edge conditions a product team would rely on pre-commitment?

  To pass: verdict must be REPRESENTATIVE.
  If key usage patterns or edges are absent: verdict is INCOMPLETE and the case fails.

If all three dimensions pass → MOCK-ACCEPTED.
If any dimension fails → REAL-REQUIRED. Record which dimension failed and why.

---

## Pass 3 — Defend the MOCK-ACCEPTED Decisions

For every namespace where you reached MOCK-ACCEPTED in Pass 2,
complete the defense record. This record is what the skill writes to the artifact.

  Defense requires:
  
  Reason codes (exact enumeration only — no paraphrases):
    STRUCTURAL-COVERAGE-SUFFICIENT   ← use if Dimension 1 was the primary basis
    DOMAIN-KNOWLEDGE-CONSISTENT      ← use if Dimension 2 or 3 was the primary basis
    (Both may apply — list both if so)

  Structural position (Slot 1):
  State the specific tier-1 decision this namespace's mock coverage supports.
  Do not write a generic adequacy statement. Name the decision.
  
  Template: "[Namespace] mock coverage supports the [specific named tier decision]
  determination at the [named gate]."

  Contrast (Slot 2):
  Name a namespace from the non-starter list and state the structural factor that
  explains why that namespace cannot proceed on mock while this one can.
  
  Template: "Unlike [non-starter namespace] ([auto-flag property]), [this namespace]
  does not depend on [structural factor] — [one-sentence structural reason]."

  If either slot cannot be completed, the defense fails and the decision reverts to
  REAL-REQUIRED.

---

## Pass 4 — In-Place Edit + Canary

Using the Edit tool, update simulations/mock/{topic}-mock-{date}.md in-place.

Replace every:
  Status: MOCK (awaiting review)
with:
  Status: [final decision]

After all edits, re-read the file. Count remaining "Status: MOCK (awaiting review)" strings.

Canary — issue verbatim, only after count verification:
  "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."

If count > 0: suppress Canary, list the unchanged fields.

---

## Pass 5 — Review Artifact

Write: simulations/mock/{topic}-review-{date}.md

Structure:
  1. Coverage Review table
     Columns: Namespace | Category | Decision | Trigger
     Order: non-starters first, then evaluation-driven REAL-REQUIRED, then MOCK-ACCEPTED

  2. For each MOCK-ACCEPTED: defense record (reason codes + Slot 1 + Slot 2)

  3. Cross-namespace risk statement:
     Single highest-risk gap: name the namespace, the specific tier decision at risk,
     urgency: BLOCKING | HIGH | MEDIUM

---

## Pass 6 — Next Steps

/{skill-id} {topic} format required.

  [REAL-REQUIRED — Auto-flagged]:
    /{skill-id} {topic} -- {namespace}: REAL-REQUIRED (AUTO-FLAG: {trigger})

  [REAL-REQUIRED — Evaluation]:
    /{skill-id} {topic} -- {namespace}: REAL-REQUIRED ({dimension} failed: {verdict})

  [MOCK-ACCEPTED]:
    /{skill-id} {topic} -- {namespace}: MOCK-ACCEPTED ({reason codes}), simulation ready
```

---

## V-04 — Combination: Role Sequence + Lifecycle Emphasis
**Axes**: Role sequence (fixed gate-then-evaluate ordering) combined with explicit lifecycle emphasis (each phase has a named boundary, entry condition, and exit assertion).
**Hypothesis**: Making phase transitions explicit with named entry/exit conditions prevents the model from collapsing phases together — particularly the gap between auto-flag classification and evaluation reasoning that enables C-02 bypass.

---

```markdown
You are running /mock-accept {topic}.

---

## PHASE 0 — LOCATE AND READ

Entry condition: skill invoked with topic argument.
Exit assertion: mock artifact fully read; namespace list confirmed.

Read: simulations/mock/{topic}-mock-{date}.md

If artifact not found: halt. Output: "BLOCKED — mock artifact not found at
simulations/mock/{topic}-mock-{date}.md. Run /mock {topic} first."

After reading: list every namespace found in the artifact (with their current
"Status: MOCK (awaiting review)" fields). This list is the working set for all
subsequent phases.

---

## PHASE 1 — AUTO-FLAG CLASSIFICATION

Entry condition: working namespace list confirmed from Phase 0.
Exit assertion: every namespace classified as AUTO-FLAGGED or EVALUATION-ELIGIBLE.
No evaluation logic runs in this phase.

Apply these classification rules in order:

  Rule A — EVIDENCE-HEAVY: prove, listen → AUTO-FLAGGED: REAL-REQUIRED
  Rule B — TIER-CRITICAL: flow, trace → AUTO-FLAGGED: REAL-REQUIRED
  Rule C — COMPLIANCE: any compliance-tagged namespace → AUTO-FLAGGED: REAL-REQUIRED

For each AUTO-FLAGGED namespace, record:
  Classification: AUTO-FLAGGED
  Decision: REAL-REQUIRED
  Trigger: AUTO-FLAG: [rule that applied]
  Note: "Evaluation-eligible check skipped — auto-flag is unconditional."

For each remaining namespace:
  Classification: EVALUATION-ELIGIBLE

Phase 1 exit assertion: "[N] namespaces AUTO-FLAGGED, [M] namespaces
EVALUATION-ELIGIBLE. Sum = [total]. Matches working set. Phase 1 complete."

Do not proceed to Phase 2 until this assertion is written.

---

## PHASE 2 — ROLE-SEQUENCED EVALUATION (EVALUATION-ELIGIBLE ONLY)

Entry condition: Phase 1 exit assertion written.
Exit assertion: every EVALUATION-ELIGIBLE namespace has a final decision.

For each EVALUATION-ELIGIBLE namespace, run roles in this fixed sequence.
A role failure closes the namespace immediately — later roles do not run.

  ROLE A — ARCHITECT (runs first)
  Evaluate structural coverage: contract boundaries, error surfaces, state transitions.
  
  Pass verdict: CONSISTENT-WITH-ARCHITECTURE
    → continue to Role B
  Fail verdict: STRUCTURALLY-INSUFFICIENT
    → Decision: REAL-REQUIRED (Architect: STRUCTURALLY-INSUFFICIENT)
    → Skip Roles B and C for this namespace

  ROLE B — STRATEGY (runs only if Role A passed)
  Evaluate adequacy for the specific tier-1 decision this namespace informs.
  
  Pass verdict: ADEQUATE FOR TIER 1
    → continue to Role C
  Fail verdict: INADEQUATE FOR TIER 1
    → Decision: REAL-REQUIRED (Strategy: INADEQUATE FOR TIER 1)
    → Skip Role C for this namespace

  ROLE C — PM (runs only if Roles A and B passed)
  Evaluate coverage breadth against real usage patterns and edge conditions.
  
  Pass verdict: REPRESENTATIVE
    → Decision: MOCK-ACCEPTED
  Fail verdict: INCOMPLETE
    → Decision: REAL-REQUIRED (PM: INCOMPLETE)

Phase 2 exit assertion: "[M] EVALUATION-ELIGIBLE namespaces processed.
[X] MOCK-ACCEPTED, [Y] REAL-REQUIRED (evaluation). Phase 2 complete."

Do not proceed to Phase 3 until this assertion is written.

---

## PHASE 3 — STRUCTURAL SLOT POPULATION (MOCK-ACCEPTED ONLY)

Entry condition: Phase 2 exit assertion written.
Exit assertion: every MOCK-ACCEPTED namespace has both slots populated, or
decision has been reverted to REAL-REQUIRED.

For each MOCK-ACCEPTED namespace:

  Reason codes:
  Select from exact enumeration only:
    STRUCTURAL-COVERAGE-SUFFICIENT   (primary basis: structural)
    DOMAIN-KNOWLEDGE-CONSISTENT      (primary basis: domain knowledge)
  Both may be listed if applicable.
  No paraphrases. No invented codes. Code must appear in labeled field, not buried in prose.

  Slot 1 — SQ-1 Tier-Decision Anchor:
  Write: "[Namespace] mock coverage supports the [specific tier-1 decision name]
  determination at the [gate name] gate."
  
  Slot 1 SLOT-VIOLATION check: Does this sentence name a specific tier decision?
  If the only statement is generic (e.g., "supports tier-1 decision-making") →
  SLOT-VIOLATION → revert to REAL-REQUIRED.

  Slot 2 — Contrast:
  Write: "Unlike [contrasting namespace] ([property]), [this namespace] does not
  depend on [structural factor] — [one-sentence reason]."
  
  Slot 2 CONTRAST-INCOMPLETE check: Is a contrasting namespace named? Is a structural
  factor named? If either is absent → CONTRAST-INCOMPLETE → revert to REAL-REQUIRED.

Phase 3 exit assertion: "[X] MOCK-ACCEPTED namespaces with both slots confirmed.
[Z] reverted to REAL-REQUIRED (slot violation). Phase 3 complete."

Do not proceed to Phase 4 until this assertion is written.

---

## PHASE 4 — IN-PLACE EDIT + CANARY

Entry condition: Phase 3 exit assertion written.
Exit assertion: Canary issued (or suppressed with explanation).

Using the Edit tool, update simulations/mock/{topic}-mock-{date}.md.

For each namespace in the working set:
  Replace:  Status: MOCK (awaiting review)
  With:     Status: [final decision from Phase 2 or Phase 3]

After all Edit calls complete, re-read the artifact.
Count occurrences of "Status: MOCK (awaiting review)".

If count = 0, issue:
  "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."

If count > 0, suppress Canary. Output:
  "CANARY SUPPRESSED — [N] Status fields not updated: [list namespace names]."

Phase 4 exit assertion is the Canary line itself (or suppression notice).

---

## PHASE 5 — REVIEW ARTIFACT + NEXT STEPS

Entry condition: Phase 4 exit assertion written.

Write: simulations/mock/{topic}-review-{date}.md

File structure:
  Section 1 — Coverage Review table
    Columns: Namespace | Category | Decision | Trigger
    Row order: AUTO-FLAGGED first, evaluation REAL-REQUIRED second, MOCK-ACCEPTED last

  Section 2 — Structural records (one per MOCK-ACCEPTED namespace)
    Reason codes (labeled field) + Slot 1 + Slot 2

  Section 3 — Cross-namespace risk statement
    Exactly one highest-risk gap: namespace name + tier decision at risk +
    urgency classification: BLOCKING | HIGH | MEDIUM

Next Steps — /{skill-id} {topic} format:

  Group 1 — AUTO-FLAGGED REAL-REQUIRED:
    /{skill-id} {topic} -- {namespace}: REAL-REQUIRED (AUTO-FLAG: {trigger})

  Group 2 — Evaluation-driven REAL-REQUIRED:
    /{skill-id} {topic} -- {namespace}: REAL-REQUIRED ({role}: {verdict})

  Group 3 — MOCK-ACCEPTED:
    /{skill-id} {topic} -- {namespace}: MOCK-ACCEPTED ({reason codes}), cleared
```

---

## V-05 — Combination: Phrasing Register + Output Format
**Axes**: Conversational/interrogative register (questions drive the workflow) combined with list-based output (decisions presented as a scannable checklist, not a prose narrative).
**Hypothesis**: Framing decisions as answers to explicit questions (rather than rendered prose) reduces verbose rationalization that buries reason codes in prose — the primary C-03 failure mode — while the checklist format makes slot violations visible as blank lines.

---

```markdown
You are running /mock-accept {topic}.

Read the mock artifact first: simulations/mock/{topic}-mock-{date}.md
Can't find it? Stop here and say so — don't guess a path.

---

## Question 1 — Which namespaces are in this mock?

List them. You need all nine to proceed:
  scout, draft, review, flow, trace, prove, listen, program, topic

If any are missing from the mock artifact, note the gap. All nine still need a decision.

---

## Question 2 — Which namespaces cannot use mock coverage, ever?

Answer by checking three structural properties:

  Is it EVIDENCE-HEAVY?
  → prove: yes. listen: yes. These namespaces depend on observed user behavior.
    No mock can substitute. Decision: REAL-REQUIRED (AUTO-FLAG: EVIDENCE-HEAVY).

  Is it TIER-CRITICAL?
  → flow: yes. trace: yes. Runtime and permission behavior requires live execution.
    No mock can substitute. Decision: REAL-REQUIRED (AUTO-FLAG: TIER-CRITICAL).

  Is it compliance-tagged?
  → Check the mock artifact. If yes: REAL-REQUIRED (AUTO-FLAG: COMPLIANCE).

Write your auto-flagged list:
  - [namespace]: REAL-REQUIRED — AUTO-FLAG: [property]
  - [namespace]: REAL-REQUIRED — AUTO-FLAG: [property]
  ...

These are closed. Skip them in Questions 3-5.

---

## Question 3 — For each remaining namespace: does the mock hold up structurally?

Ask the Architect for each non-auto-flagged namespace:
  "Does this mock capture the contract boundaries, error surfaces, and state
  transitions needed for tier-1 validation?"

  If yes → CONSISTENT-WITH-ARCHITECTURE → continue to Question 4
  If no  → STRUCTURALLY-INSUFFICIENT → REAL-REQUIRED, skip Questions 4-5 for this one

---

## Question 4 — Is it adequate for the tier decision?

Ask Strategy:
  "Does this mock give the team enough confidence to pass through the next gate
  without real data?"

  If yes → ADEQUATE FOR TIER 1 → continue to Question 5
  If no  → INADEQUATE FOR TIER 1 → REAL-REQUIRED, skip Question 5

---

## Question 5 — Is the coverage representative?

Ask PM:
  "Do these scenarios cover the usage patterns and edge conditions the team
  would rely on pre-commitment?"

  If yes → REPRESENTATIVE → MOCK-ACCEPTED
  If no  → INCOMPLETE → REAL-REQUIRED

---

## Question 6 — For each MOCK-ACCEPTED: what's the case?

For each namespace that reached MOCK-ACCEPTED, fill in this checklist.
A blank line in any item is a failure — the decision reverts to REAL-REQUIRED.

  Namespace: ___________

  [ ] Reason code (choose from exact list only — no paraphrasing):
      - STRUCTURAL-COVERAGE-SUFFICIENT
      - DOMAIN-KNOWLEDGE-CONSISTENT
      (Both may apply. List each that fits.)
      Your answer: ___________

  [ ] Slot 1 — What specific tier-1 decision does this mock support?
      Write exactly: "[NS] mock coverage supports the [decision name] determination
      at the [gate name] gate."
      Your answer: ___________
      (If you wrote "supports tier-1 decision-making" without a named decision → blank)

  [ ] Slot 2 — Which auto-flagged namespace contrasts with this one, and why?
      Write exactly: "Unlike [NS] ([property]), [this NS] does not depend on
      [structural factor] — [reason]."
      Your answer: ___________
      (If you named no structural factor → blank)

---

## Question 7 — Has the mock artifact been updated?

Using the Edit tool, replace every instance of:
  Status: MOCK (awaiting review)
with the correct decision for that namespace.

After editing, re-read the file. Count remaining "Status: MOCK (awaiting review)" strings.

Your count: ___

If count = 0, write:
  "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."

If count > 0, write which namespace fields were not updated. Do not issue the Canary.

---

## Question 8 — What does the full picture look like?

Write the review artifact: simulations/mock/{topic}-review-{date}.md

Include:
  - Coverage Review table: Namespace | Category | Decision | Trigger
    (auto-flagged first, evaluation REAL-REQUIRED second, MOCK-ACCEPTED last)
  - The completed checklists from Question 6
  - One cross-namespace risk call: which single namespace represents the highest-risk
    gap, which tier decision is at stake, and is it BLOCKING / HIGH / MEDIUM?

---

## Question 9 — What should the team do next?

List next steps using this format: /{skill-id} {topic} -- {state}

  Auto-flagged namespaces (do these first):
  - /{skill-id} {topic} -- {namespace}: REAL-REQUIRED (AUTO-FLAG: {trigger})

  Evaluation-driven REAL-REQUIRED (do these next):
  - /{skill-id} {topic} -- {namespace}: REAL-REQUIRED ({role}: {verdict})

  MOCK-ACCEPTED (cleared for simulation):
  - /{skill-id} {topic} -- {namespace}: MOCK-ACCEPTED, proceed to simulation
```

---

## Variation Summary

| ID | Primary Axis | Secondary Axis | Hypothesis |
|----|-------------|----------------|-----------|
| V-01 | Role sequence — gate blocks before evaluation | — | C-02 eliminated by hard gate checkpoint |
| V-02 | Output format — table-first, grid before prose | — | C-01/C-03 visible at glance in grid |
| V-03 | Inertia framing — REAL-REQUIRED is default | — | C-02 countered by requiring positive case for MOCK-ACCEPTED |
| V-04 | Role sequence — fixed gate→evaluate ordering | Lifecycle emphasis — explicit phase entry/exit assertions | Phase collapse prevented; C-02 isolated |
| V-05 | Phrasing register — interrogative/conversational | Output format — checklist with blank-line failure signal | C-03 prose burial prevented; C-05 blank = visible fail |
