Written to `simulations/quest/variations/mock-accept-variations-R1-2026-03-16.md`.

---

## mock-accept Variations R1 — Summary

**5 complete, runnable skill bodies.** Single-axis for V-01 through V-03, combined for V-04 and V-05.

---

### V-01 — Inertia framing (single axis)
The REAL-REQUIRED-as-gravity frame is not just a preamble position — it is repeated at every phase gate, every role evaluation sub-question, and both structural slots of the MOCK-ACCEPTED template. SLOT 2 moves *before* SLOT 1 to force the contrast argument (the escape justification) before the structural position claim. Tests whether front-loading the inertia frame throughout reduces zero-argument acceptances.

### V-02 — Role sequence: PM → Strategy → Architect (single axis)
PM structural completeness check runs first as the cheapest mechanical disqualifier. Strategy tier adequacy runs second, establishing the SLOT 1 anchor for any remaining candidates. Architect plausibility runs last — the most judgment-intensive check, reserved for namespaces that already cleared structural and strategic gates. Tests whether front-loading cheap disqualifiers reduces wasted evaluation work.

### V-03 — Output format: table-first throughout (single axis)
A decision table is initialized at STEP 1 and extended at each subsequent step (Auto-flag column, then Arch, Strategy, PM columns, then Final decision). STEP 6 *confirms* the table rather than reconstructing decisions from prose blocks. Tests whether the table-as-ledger format makes missing criteria immediately visible and reduces reconstruction errors.

### V-04 — Phrasing register + compressed lifecycle (combined)
All-caps STOP gates and DO NOT imperatives replaced with descriptive self-check language. Phases are delimited by output structure rather than explicit gate directives. Tests whether reducing parsing friction improves edge-case judgment without losing constraint enforcement.

### V-05 — Strategy-first sequence + inertia framing throughout (combined)
Strategy runs first because the tier decision anchor (SLOT 1) must be named before plausibility or structure can be evaluated against it. Inertia framing then requires the escape argument to be built layer by layer across all three roles. The SLOT 1 block is explicitly framed as "established before plausibility was checked." Tests whether establishing the tier anchor first, combined with layered inertia framing, produces stronger and more specific MOCK-ACCEPTED arguments.

---

**Rubric coverage notes:**
- C-01/C-02 (auto-flag correctness / FORBIDDEN OUTPUTS TRIAD): all 5 variations preserve the exact rules and all 3 triad labels; V-01/V-05 add explicit inertia notes per rule
- C-03 (CANARY ASSERTION): STEP 8 preserved and marked non-skippable in all variations
- C-04 (review artifact structure): STEP 7 preserved in all variations
- C-05 (SLOT 1 / SLOT 2 / reason codes): V-01 inverts slot order (SLOT 2 first); V-05 explicitly anchors SLOT 1 as "established before plausibility check" — both are hypotheses about which ordering better forces the positive argument
l
    evidence by definition. Mock structure cannot substitute.

  RULE 2 — TIER-CRITICAL (Tier 2+):
    IF tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
    THEN: REAL-REQUIRED, trigger = TIER-CRITICAL
    Inertia note: At Tier 2, these namespaces gate go/no-go decisions. Simulation
    cannot carry that weight.

  RULE 3 — COMPLIANCE (when active):
    IF compliance tags present AND namespace in {scout-compliance, trace-permissions}
    THEN: REAL-REQUIRED, trigger = COMPLIANCE
    Inertia note: Compliance namespaces require traceable real-world sources.
    Synthetic artifacts produce appearance without audit substance.

Output:
  Auto-flagged (REAL-REQUIRED, inertia unconditional): [{namespace}: trigger = {rule}]
  Remaining (REAL-REQUIRED by default — escape must be earned): [{namespace}: Category = {value}]

===================================================================
INERTIA GATE — THREE UNCONDITIONAL CONSTRAINTS — VERIFY ALL 3:

  [EVIDENCE-HEAVY]  FORBIDDEN: MOCK-ACCEPTED on any EVIDENCE-HEAVY namespace.
                    Inertia cannot be overcome by structural quality.
  [TIER-CRITICAL]   FORBIDDEN: MOCK-ACCEPTED on any TIER-CRITICAL namespace.
                    Inertia cannot be overcome by positive role verdicts.
  [COMPLIANCE]      FORBIDDEN: MOCK-ACCEPTED on any COMPLIANCE-tagged namespace.
                    Inertia cannot be overcome by user framing or override.

  A two-of-three acknowledgment does not satisfy this gate. All 3 labels
  must be present in output. Proceed only when all 3 are stated.

AUTO-RULE CONTAMINATION GUARD:
  DO NOT apply role evaluation to any auto-flagged namespace.
  Named error: AUTO-RULE CONTAMINATION. Verdicts on auto-flagged namespaces are void.

DO NOT proceed to STEP 3 until two-list partition is output and all 3 inertia
constraint labels are acknowledged.
===================================================================

---

STEP 3 — ARCHITECT EVALUATION (remaining namespaces only)

The inertia question for Architect: would a simulated architectural artifact mislead
the team about {topic}'s component structure, dependencies, or integration boundaries?
If yes: inertia holds (REAL-REQUIRED). If no: this role's inertia concern is overcome.

For each remaining namespace, answer three sub-questions using entity-naming grammar:

| SQ | Question | Inertia direction |
|----|----------|-------------------|
| 1  | Name the system component, dependency, or interface in the mock that confirms plausibility — or: "Contradiction found — name the specific element". | Contradiction = inertia holds |
| 2  | Name the data flow, state transition, or API shape the mock implies for {topic} — or: "Inconsistency found — name the specific element". | Inconsistency = inertia holds |
| 3  | Name the architectural fact about {topic} this namespace's mock most directly depends on. State whether the mock is consistent with that fact. | Inconsistency = inertia holds |

Verdict: CONSISTENT-WITH-ARCHITECTURE (inertia overcome — proceed to Strategy)
      or CONTRADICTS-ARCHITECTURE (inertia holds — REAL-REQUIRED, trigger = ARCH-IMPLAUSIBLE)

For any namespace where verdict = CONTRADICTS-ARCHITECTURE:
  preliminary decision = REAL-REQUIRED, trigger = ARCH-IMPLAUSIBLE
  DO NOT pass to Strategy Evaluation. Named error: ARCH-GUARD-BYPASS.

Record:
  Arch-blocked (inertia held by contradiction): [{list}]
  Proceeding to Strategy (Architect inertia overcome): [{list}]

DO NOT proceed to STEP 4 until Architect verdicts and guard assignments are complete.

---

STEP 4 — STRATEGY EVALUATION (non-auto, non-Arch-blocked only)

The inertia question for Strategy: does this namespace's mock provide an adequate
structural ground for the specific Tier {tier} decision it is intended to support?
If no: inertia holds. If yes, and the belief formed would be correct: this role's
inertia concern is overcome.

For each qualifying namespace, answer three sub-questions:

| SQ | Question | Inertia direction |
|----|----------|-------------------|
| 1  | Name the specific Tier {tier} decision this namespace is intended to support. (This becomes SLOT 1 anchor in MOCK-ACCEPTED — no decision name = inertia cannot be overcome at SLOT 1.) | No named decision = inertia holds |
| 2  | Name the belief the team would form about {topic} if this namespace runs as MOCK-ACCEPTED. State whether that belief would be correct or incorrect. | Incorrect belief = inertia holds |
| 3  | Name the coverage gap that would keep this namespace in its REAL-REQUIRED default — or: "No gap — namespace positively demonstrates coverage adequacy for Tier {tier}". | Named gap = inertia holds |

Verdict: ADEQUATE FOR TIER {tier} (Strategy inertia overcome — proceed to PM)
      or INSUFFICIENT FOR TIER {tier} (inertia holds — REAL-REQUIRED, trigger = STRATEGY-INADEQUATE)

For any namespace where verdict = INSUFFICIENT:
  preliminary decision = REAL-REQUIRED, trigger = STRATEGY-INADEQUATE
  DO NOT pass to PM Evaluation. Named error: STRATEGY-TO-PM-GUARD-BYPASS.

Record:
  Strategy-blocked (inertia held by inadequacy): [{list}]
  Proceeding to PM (Strategy inertia overcome): [{list}]

DO NOT proceed to STEP 5 until Strategy verdicts and guard assignments are complete.

---

STEP 5 — PM EVALUATION (qualifying namespaces only)

The inertia question for PM: does this namespace's mock contain the required sections
and structural enforcement gates? If any required element is absent: inertia holds.

For each qualifying namespace:

| SQ | Question | Inertia direction |
|----|----------|-------------------|
| 1  | Name the required sections present in the mock artifact for this namespace. | Missing required sections = inertia holds |
| 2  | Name the enforcement gate, decision table, or required output structure present — or: "Absent — name the missing element and which section defines it". | Absent gate = inertia holds |
| 3  | Name one structural gap that would keep this namespace in its REAL-REQUIRED default — or: "No gap — namespace positively demonstrates structural completeness". | Named gap = inertia holds |

Verdict: STRUCTURALLY ADEQUATE (PM inertia overcome — eligible for MOCK-ACCEPTED)
      or STRUCTURALLY INCOMPLETE (inertia holds — REAL-REQUIRED, trigger = PM-INCOMPLETE)

DO NOT proceed to STEP 6 until PM verdicts are written for every qualifying namespace.

---

STEP 6 — DECISIONS WITH INERTIA CITATION

Only namespaces where ALL THREE roles overcome inertia may receive MOCK-ACCEPTED.
The MOCK-ACCEPTED template requires the inertia escape argument in SLOT 2 first —
the contrast that explains why inertia is overcome here but holds elsewhere.

Trigger field: named, parseable artifact field. Second line of every block.
  Values: trigger = EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE |
                    STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE

MOCK-ACCEPTED template — inertia-escape form:

  Decision: MOCK-ACCEPTED
  trigger = n/a
  reason-code: [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; no paraphrase; no invented codes)

  Contrast (SLOT 2 — stated first to establish the inertia-escape argument):
    Unlike {namespace type}, which requires real evidence because {structural factor}
    makes simulation insufficient, this namespace's outputs are fully determined by
    {structural form property}. A confirmatory statement without a named contrasting
    namespace type = CONTRAST-INCOMPLETE. A single slot merging both positions =
    RATIONALE-INCOMPLETE.

  Structural position (SLOT 1 — the tier decision this escape argument supports):
    Feeds tier decision: {SQ-1 answer — name the specific Tier {tier} decision}.
    Generic adequacy statement without a named decision = SLOT-VIOLATION.
    Classify: STRUCTURAL-FORM | TIER-GATING.

REAL-REQUIRED template — evaluation-driven:
  Decision: REAL-REQUIRED
  trigger = {STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE}
  Failing evaluation: [Strategy | Architect | PM]
  Failing verdict: [full verdict string]
  SQ answer driving verdict:
    [Present-tense, artifact as subject. ERROR — VERDICT-ECHO: role as subject.]
  Artifact state: [present-tense, artifact as subject — propagates to next-steps entry]

REAL-REQUIRED template — auto-flagged:
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

DO NOT proceed to STEP 7 until all decision blocks are complete.

---

STEP 7 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-review-{date}.md.

Coverage Review table (inertia-outcome format):
  | Namespace | Category | Decision | trigger | Inertia outcome |

  Inertia outcome values:
    INERTIA-HELD (auto-flag) | INERTIA-HELD (evaluation) | INERTIA-ESCAPED

Ordering rule (state explicitly in artifact):
  "Critical namespaces first ({trace-*, scout-feasibility, listen-*, scout-competitors}),
   non-critical evaluation-driven next, evidence-heavy and compliance last."

  Priority 1 — Critical REAL-REQUIRED: /{skill-id} {topic} — {Artifact state}
  Priority 2 — Non-critical evaluation-driven: /{skill-id} {topic} — {Artifact state}
  Priority 3 — Evidence-heavy / compliance: /{skill-id} {topic} — trigger: {trigger value}

Cross-namespace risk statement (inertia-weighted):
  "Highest-risk inertia gap: {namespace} — {specific Tier {tier} decision at risk}
  — urgency: {BLOCKING | HIGH | MEDIUM}"
  Include urgency grouping commentary for each priority group when more than one namespace.

DO NOT proceed to STEP 8 until review artifact is confirmed written.

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable)

Edit {mock-artifact-path} in-place using Edit tool. Replace Status fields only.

  REPLACE: Status: MOCK (awaiting review)
  WITH one of:
    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
    Status: REAL-REQUIRED [{trigger value}]

CANARY ASSERTION (write only when verified true):
  "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
PROHIBITED if any Status field remains as MOCK (awaiting review). Named error: CANARY-FALSE-POSITIVE.
If condition not met: "CANARY SUPPRESSED: {N} field(s) not updated — {list}"

Full confirmation block:
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.
```

---

## V-02

**Axis:** Role sequence — PM evaluates before Strategy, Strategy before Architect
**Hypothesis:** Structural completeness (PM) is the most mechanical filter and the
cheapest disqualification. If required sections are absent, no tier analysis is
warranted. Strategy adequacy is the next filter — it establishes the tier decision
anchor that Architect must respect. Architect plausibility is the most judgment-intensive
check and is saved for namespaces that have cleared the structural and strategic gates.
This ordering minimizes judgment work by front-loading disqualifications.

---

```
---
name: mock-accept
description: Step 2 of mock-first workflow. Reads mock artifact, applies auto-flag rules,
  evaluates non-auto namespaces through PM / Strategy / Architect (in that order), writes
  MOCK-ACCEPTED or REAL-REQUIRED decisions per namespace, writes review artifact, writes
  Status fields back in-place.
allowed-tools: [Read, Write, Edit, Glob]
---

You are running /mock:accept.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION:
  Every namespace begins as REAL-REQUIRED. MOCK-ACCEPTED is an earned escape requiring
  a positive argument. Absence of disqualification is not positive evidence.

ROLE EVALUATION ORDER (this run):
  STEP 3 — PM (structural completeness gate, cheapest disqualification)
  STEP 4 — Strategy (tier adequacy gate, strategic anchor)
  STEP 5 — Architect (plausibility gate, most judgment-intensive)

This ordering concentrates the judgment-expensive Architect evaluation on namespaces
that have already cleared structural and strategic filters.

---

STEP 1 — READ

Read {mock-artifact-path}. Extract from each namespace section: namespace name,
Category field, Status field. Read TOPICS.md; record tier for {topic} and compliance tags.

Output: "Tier: {N} (source: TOPICS.md | --tier | default)"
DO NOT proceed to STEP 2 until all namespace fields are extracted and listed.

---

STEP 2 — AUTO-FLAG

Three rules. All mandatory. Fire before role evaluation. Not role-overridable.

  RULE 1 — EVIDENCE-HEAVY (all tiers):
    IF Category == EVIDENCE-HEAVY THEN: REAL-REQUIRED, trigger = EVIDENCE-HEAVY
  RULE 2 — TIER-CRITICAL (Tier 2+):
    IF tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
    THEN: REAL-REQUIRED, trigger = TIER-CRITICAL
  RULE 3 — COMPLIANCE (when active):
    IF compliance tags present AND namespace in {scout-compliance, trace-permissions}
    THEN: REAL-REQUIRED, trigger = COMPLIANCE

Output two lists:
  Auto-flagged (REAL-REQUIRED): [{namespace}: trigger = {rule}]
  Remaining (default: REAL-REQUIRED): [{namespace}: Category = {value}]

===================================================================
PHASE GATE — AUTOMATIC RULES COMPLETE / ROLE EVALUATION BEGINS
===================================================================

FORBIDDEN OUTPUTS TRIAD (all 3 required — verify all 3 before proceeding):
  [EVIDENCE-HEAVY]  DO NOT mark any EVIDENCE-HEAVY namespace MOCK-ACCEPTED.
  [TIER-CRITICAL]   DO NOT mark any TIER-CRITICAL namespace MOCK-ACCEPTED.
  [COMPLIANCE]      DO NOT mark any COMPLIANCE-tagged namespace MOCK-ACCEPTED.
  Completeness check: all 3 labels present. Two-of-three does not satisfy this gate.

AUTO-RULE CONTAMINATION GUARD:
  DO NOT apply evaluation to any auto-flagged namespace. Named error: AUTO-RULE CONTAMINATION.

DO NOT proceed to STEP 3 until two-list partition is confirmed and FORBIDDEN OUTPUTS
TRIAD verified complete (3 of 3 labels present).
===================================================================

---

STEP 3 — PM EVALUATION (non-auto namespaces — runs first in this variation)

Entry condition: remaining namespaces from STEP 2 only.

For each remaining namespace, answer sub-questions using entity-naming grammar:

| Row # | Sub-question |
|-------|-------------|
| 1     | Name the required sections present in the mock artifact for this namespace. |
| 2     | Name the enforcement gate, decision table, or required output structure present — or: "Absent — name the missing element and which section defines it". |
| 3     | Name one structural gap that would keep this namespace in its REAL-REQUIRED default — or: "No gap — namespace positively demonstrates structural completeness". |

  PM Verdict: STRUCTURALLY ADEQUATE   or   STRUCTURALLY INCOMPLETE

CROSS-STEP GUARD — PM to Strategy:
  For any namespace where PM verdict = STRUCTURALLY INCOMPLETE:
    preliminary decision = REAL-REQUIRED, trigger = PM-INCOMPLETE
    DO NOT pass to Strategy Evaluation (STEP 4).
  Named error: PM-TO-STRATEGY-GUARD-BYPASS.
  Record:
    PM-blocked (PM verdict = STRUCTURALLY INCOMPLETE): [{list}]
    Proceeding to Strategy Evaluation: [{list}]

DO NOT proceed to STEP 4 until PM verdicts and guard assignments are complete.

---

STEP 4 — STRATEGY EVALUATION (non-auto, non-PM-blocked namespaces only)

Entry condition: STEP 4 applies ONLY to namespaces not on the PM-blocked list.
Named error: GUARD-BYPASS CONTAMINATION.

For each qualifying namespace, answer sub-questions using entity-naming grammar:

| Row # | Sub-question |
|-------|-------------|
| 1     | Name the specific Tier {tier} decision this namespace is intended to support. [This answer becomes the Structural position SQ-1 anchor in the MOCK-ACCEPTED template.] |
| 2     | Name the belief the team would form about {topic} if this runs as MOCK-ACCEPTED (state whether that belief would be correct or incorrect). |
| 3     | Name the coverage gap that would keep this namespace in its REAL-REQUIRED default — or: "No gap — namespace positively demonstrates coverage adequacy for Tier {tier}". |

  Strategy Verdict: ADEQUATE FOR TIER {tier}   or   INSUFFICIENT FOR TIER {tier}

CROSS-STEP GUARD — Strategy to Architect:
  For any namespace where strategy-verdict = INSUFFICIENT FOR TIER {tier}:
    preliminary decision = REAL-REQUIRED, trigger = STRATEGY-INADEQUATE
    DO NOT apply Architect Evaluation (STEP 5).
  Named error: STRATEGY-TO-ARCH-GUARD-BYPASS.
  Record:
    Strategy-blocked (strategy-verdict = INSUFFICIENT): [{list}]
    Proceeding to Architect Evaluation: [{list}]

DO NOT proceed to STEP 5 until Strategy verdicts and guard assignments are complete.

---

STEP 5 — ARCHITECT EVALUATION (qualifying namespaces only)

Entry condition: STEP 5 applies ONLY to namespaces not on the PM-blocked or
Strategy-blocked lists. Named error: GUARD-BYPASS CONTAMINATION.

For each qualifying namespace, answer sub-questions using entity-naming grammar.
Yes/no answers do not satisfy entity-naming sub-question requirements.

| Row # | Sub-question |
|-------|-------------|
| 1     | Name the system component, dependency, or interface in the mock that confirms plausibility — or: "Contradiction found — name the specific element". |
| 2     | Name the data flow, state transition, or API shape the mock implies for {topic} — or: "Inconsistency found — name the specific element". |
| 3     | Name the architectural fact about {topic} this namespace's mock most directly depends on. State whether the mock is consistent with that fact. |

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE   or   CONTRADICTS-ARCHITECTURE

For any namespace where verdict = CONTRADICTS-ARCHITECTURE:
  preliminary decision = REAL-REQUIRED, trigger = ARCH-IMPLAUSIBLE

DO NOT proceed to STEP 6 until Architect verdicts are written for every qualifying namespace.

---

STEP 6 — DECISIONS WITH CITATION

Trigger field: named, parseable artifact field at fixed position (second line of every block).
  Values: trigger = EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE |
                    STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE

MOCK-ACCEPTED template:
  Decision: MOCK-ACCEPTED
  trigger = n/a
  reason-code: [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; no paraphrase; no invented codes)

  Structural position (SLOT 1 — Strategy SQ-1 anchor):
    Feeds tier decision: [SQ-1 answer — name the specific Tier {tier} decision this
    namespace supports. Generic adequacy statement without SQ-1 decision name = SLOT-VIOLATION.
    Classify: STRUCTURAL-FORM | TIER-GATING.]

  Contrast (SLOT 2 — dedicated, structurally separate from Slot 1):
    [Unlike {namespace type}, which carries {structural factor} requiring real evidence
    because {reason}, this namespace's outputs are fully determined by {structural form
    property}. Confirmatory sentence without named contrasting namespace type =
    CONTRAST-INCOMPLETE. Single-slot rationale = RATIONALE-INCOMPLETE.]

REAL-REQUIRED template — evaluation-driven:
  Decision: REAL-REQUIRED
  trigger = {PM-INCOMPLETE | STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE}
  Failing evaluation: [PM | Strategy | Architect]
  Failing verdict: [full verdict string]
  SQ answer driving verdict:
    [Present-tense, artifact as subject. ERROR — VERDICT-ECHO: role as subject.]
  Artifact state: [present-tense, artifact as subject — propagates to next-steps entry]

REAL-REQUIRED template — auto-flagged:
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

DO NOT proceed to STEP 7 until all decision blocks are complete.

---

STEP 7 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-review-{date}.md.
  Coverage Review table: | Namespace | Category | Decision | trigger |

  Ordering rule (state explicitly):
  "Critical namespaces first ({trace-*, scout-feasibility, listen-*, scout-competitors}),
   non-critical evaluation-driven next, evidence-heavy and compliance last."

  Priority 1 — Critical REAL-REQUIRED: /{skill-id} {topic} — {Artifact state}
  Priority 2 — Non-critical evaluation-driven: /{skill-id} {topic} — {Artifact state}
  Priority 3 — Evidence-heavy / compliance: /{skill-id} {topic} — trigger: {trigger value}

  Cross-namespace risk statement:
    "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk}
    — urgency: {BLOCKING | HIGH | MEDIUM}"
    Include urgency grouping commentary for each priority group if more than one namespace.

DO NOT proceed to STEP 8 until review artifact is confirmed written.

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable)

Edit {mock-artifact-path} in-place using Edit tool. Replace Status fields only.

  REPLACE: Status: MOCK (awaiting review)
  WITH one of:
    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
    Status: REAL-REQUIRED [{trigger value}]

CANARY ASSERTION (write only when verified true):
  "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
Named error if false: CANARY-FALSE-POSITIVE.
If condition not met: "CANARY SUPPRESSED: {N} field(s) not updated — {list}"

Full confirmation block:
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.
```

---

## V-03

**Axis:** Output format — table-first at every step
**Hypothesis:** Expressing each step's output as a structured table row rather than
prose blocks makes criterion gaps immediately visible (a missing column is obvious in
a table, invisible in prose) and creates a natural accumulating ledger that Step 6
can confirm rather than reconstruct. The decision table grows across steps; final
decisions are confirmed, not authored, at Step 6.

---

```
---
name: mock-accept
description: Step 2 of mock-first workflow. Reads mock artifact, applies auto-flag rules,
  evaluates non-auto namespaces through Architect / Strategy / PM roles, writes
  MOCK-ACCEPTED or REAL-REQUIRED decisions per namespace, writes review artifact, writes
  Status fields back in-place.
allowed-tools: [Read, Write, Edit, Glob]
---

You are running /mock:accept.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

DEFAULT DECISION POSITION:
  Every namespace begins as REAL-REQUIRED. MOCK-ACCEPTED is an earned escape requiring
  a positive argument. Absence of disqualification is not positive evidence.

TABLE ACCUMULATION PROTOCOL:
  This skill maintains a single decision table that grows across Steps 1–6.
  Each step adds rows or columns to the table. Step 6 confirms the final state
  of the table — it does not author new content. The table structure is fixed at
  Step 1 and extended at each subsequent step.

---

STEP 1 — READ + TABLE INITIALIZE

Read {mock-artifact-path}. Extract from each namespace section: namespace name,
Category field, Status field. Read TOPICS.md; record tier for {topic} and compliance tags.

State: "Tier: {N} (source: TOPICS.md | --tier | default)"

Initialize the decision table with one row per namespace:

| Namespace | Category | Auto-flag | Arch | Strategy | PM | Final decision | trigger |
|-----------|----------|-----------|------|----------|----|----------------|---------|
| {name}    | {value}  | —         | —    | —        | —  | REAL-REQUIRED  | TBD     |

Note: Final decision column initializes to REAL-REQUIRED for all rows. Updates occur
at each subsequent step. A row remains REAL-REQUIRED until all applicable steps
explicitly mark it as cleared.

DO NOT proceed to STEP 2 until all namespace rows are initialized.

---

STEP 2 — AUTO-FLAG (updates Auto-flag column)

Three rules. All mandatory. Fire before role evaluation. Not role-overridable.

  RULE 1 — EVIDENCE-HEAVY (all tiers):
    IF Category == EVIDENCE-HEAVY: Auto-flag = EVIDENCE-HEAVY, trigger = EVIDENCE-HEAVY
  RULE 2 — TIER-CRITICAL (Tier 2+):
    IF tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}:
    Auto-flag = TIER-CRITICAL, trigger = TIER-CRITICAL
  RULE 3 — COMPLIANCE (when active):
    IF compliance tags present AND namespace in {scout-compliance, trace-permissions}:
    Auto-flag = COMPLIANCE, trigger = COMPLIANCE

Update decision table — Auto-flag column populated:

| Namespace | Category | Auto-flag | Arch | Strategy | PM | Final decision | trigger |
|-----------|----------|-----------|------|----------|----|----------------|---------|

For auto-flagged rows: Final decision = REAL-REQUIRED, trigger = {rule label}.
Mark Arch, Strategy, PM = SKIP (auto-flagged — evaluation forbidden).

===================================================================
PHASE GATE — TABLE COMPLETENESS CHECK:

  [EVIDENCE-HEAVY]  FORBIDDEN: MOCK-ACCEPTED on any EVIDENCE-HEAVY row.
  [TIER-CRITICAL]   FORBIDDEN: MOCK-ACCEPTED on any TIER-CRITICAL row.
  [COMPLIANCE]      FORBIDDEN: MOCK-ACCEPTED on any COMPLIANCE row.
  Completeness check: all 3 labels acknowledged. Two-of-three fails this gate.

  AUTO-RULE CONTAMINATION GUARD: any row with a non-empty Auto-flag cell
  must have Arch = SKIP, Strategy = SKIP, PM = SKIP. Named error: AUTO-RULE CONTAMINATION.

DO NOT proceed to STEP 3 until table is updated and FORBIDDEN OUTPUTS TRIAD
acknowledged (3 of 3 labels).
===================================================================

---

STEP 3 — ARCHITECT EVALUATION (updates Arch column, non-auto rows only)

For each row where Auto-flag = —, answer three sub-questions using entity-naming grammar.
Record the Architect verdict in the Arch column.

Sub-questions per namespace (output as nested table):

| Namespace | SQ-1: Component/interface confirmed or contradiction | SQ-2: Data flow / state transition / API shape | SQ-3: Architectural fact — consistent? | Arch verdict |
|-----------|-----------------------------------------------------|-----------------------------------------------|----------------------------------------|--------------|

  Verdict values: CONSISTENT | CONTRADICTS

Update decision table — Arch column populated:

| Namespace | Category | Auto-flag | Arch       | Strategy | PM | Final decision | trigger |
|-----------|----------|-----------|------------|----------|----|----------------|---------|

For rows where Arch = CONTRADICTS:
  Final decision = REAL-REQUIRED, trigger = ARCH-IMPLAUSIBLE
  Mark Strategy = SKIP, PM = SKIP (ARCH-GUARD-BYPASS protection).

Named error for passing CONTRADICTS rows to STEP 4: ARCH-GUARD-BYPASS.

DO NOT proceed to STEP 4 until Arch column is populated for all non-auto rows.

---

STEP 4 — STRATEGY EVALUATION (updates Strategy column, non-auto non-CONTRADICTS rows only)

Entry condition: rows where Auto-flag = — AND Arch = CONSISTENT.
Named error for violating entry: GUARD-BYPASS CONTAMINATION.

For each qualifying row, answer three sub-questions:

| Namespace | SQ-1: Specific Tier {tier} decision supported (SLOT 1 anchor) | SQ-2: Belief formed — correct or incorrect | SQ-3: Coverage gap or "No gap" | Strategy verdict |
|-----------|---------------------------------------------------------------|---------------------------------------------|-------------------------------|------------------|

  Verdict values: ADEQUATE | INSUFFICIENT

Update decision table — Strategy column populated:

| Namespace | Category | Auto-flag | Arch       | Strategy  | PM | Final decision | trigger |
|-----------|----------|-----------|------------|-----------|-----|----------------|---------|

For rows where Strategy = INSUFFICIENT:
  Final decision = REAL-REQUIRED, trigger = STRATEGY-INADEQUATE
  Mark PM = SKIP (STRATEGY-TO-PM-GUARD-BYPASS protection).

DO NOT proceed to STEP 5 until Strategy column is populated for all qualifying rows.

---

STEP 5 — PM EVALUATION (updates PM column, qualifying rows only)

Entry condition: rows where Auto-flag = — AND Arch = CONSISTENT AND Strategy = ADEQUATE.
Named error for violating entry: GUARD-BYPASS CONTAMINATION.

For each qualifying row, answer three sub-questions:

| Namespace | SQ-1: Required sections present | SQ-2: Enforcement gate / decision table / required structure | SQ-3: Structural gap or "No gap" | PM verdict |
|-----------|--------------------------------|-------------------------------------------------------------|----------------------------------|------------|

  Verdict values: ADEQUATE | INCOMPLETE

Update decision table — PM column populated, Final decision resolved:

| Namespace | Category | Auto-flag | Arch       | Strategy  | PM       | Final decision | trigger |
|-----------|----------|-----------|------------|-----------|----------|----------------|---------|

For rows where PM = ADEQUATE AND Arch = CONSISTENT AND Strategy = ADEQUATE:
  Final decision = MOCK-ACCEPTED — pending SLOT 1 + SLOT 2 completion at STEP 6.

For rows where PM = INCOMPLETE:
  Final decision = REAL-REQUIRED, trigger = PM-INCOMPLETE.

DO NOT proceed to STEP 6 until PM column is populated for all qualifying rows
and Final decision column is resolved for all rows.

---

STEP 6 — DECISIONS WITH CITATION (confirm table; author SLOT 1 + SLOT 2 for MOCK-ACCEPTED)

Confirm the final decision table is complete. Then for each MOCK-ACCEPTED row,
author the decision block using the table values as source material.

Trigger field: second line of every decision block.
  Values: trigger = EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE |
                    STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE

MOCK-ACCEPTED template (uses Strategy SQ-1 as SLOT 1 anchor, SQ-3 "No gap" as SLOT 2 basis):
  Decision: MOCK-ACCEPTED
  trigger = n/a
  reason-code: [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; no paraphrase; no invented codes)

  Structural position (SLOT 1 — from Strategy SQ-1 cell):
    Feeds tier decision: [SQ-1 answer — name the specific Tier {tier} decision].
    Generic adequacy without a named decision = SLOT-VIOLATION.
    Classify: STRUCTURAL-FORM | TIER-GATING.

  Contrast (SLOT 2 — dedicated block, not merged with SLOT 1):
    Unlike {namespace type}, which carries {structural factor} requiring real evidence
    because {reason}, this namespace's outputs are fully determined by {structural form
    property}. Confirmatory sentence without named contrasting namespace = CONTRAST-INCOMPLETE.
    Merged slots = RATIONALE-INCOMPLETE.

REAL-REQUIRED template — evaluation-driven (sources from table row):
  Decision: REAL-REQUIRED
  trigger = {from Final decision trigger cell}
  Failing evaluation: [PM | Strategy | Architect]
  Failing verdict: [full verdict string from table]
  SQ answer driving verdict:
    [Present-tense, artifact as subject. ERROR — VERDICT-ECHO: role as subject.]
  Artifact state: [present-tense, artifact as subject — propagates to next-steps entry]

REAL-REQUIRED template — auto-flagged:
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

DO NOT proceed to STEP 7 until all decision blocks authored.

---

STEP 7 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-review-{date}.md.
  Coverage Review table (derived from final decision table):
    | Namespace | Category | Decision | trigger |

  Ordering rule (state explicitly):
  "Critical namespaces first ({trace-*, scout-feasibility, listen-*, scout-competitors}),
   non-critical evaluation-driven next, evidence-heavy and compliance last."

  Priority 1 — Critical REAL-REQUIRED: /{skill-id} {topic} — {Artifact state}
  Priority 2 — Non-critical evaluation-driven: /{skill-id} {topic} — {Artifact state}
  Priority 3 — Evidence-heavy / compliance: /{skill-id} {topic} — trigger: {trigger value}

  Cross-namespace risk statement:
    "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk}
    — urgency: {BLOCKING | HIGH | MEDIUM}"
    Include urgency grouping commentary for each priority group if more than one namespace.

DO NOT proceed to STEP 8 until review artifact is confirmed written.

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable)

Edit {mock-artifact-path} in-place using Edit tool. Replace Status fields only.

  REPLACE: Status: MOCK (awaiting review)
  WITH one of:
    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
    Status: REAL-REQUIRED [{trigger value}]

CANARY ASSERTION (write only when verified true):
  "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
Named error if false: CANARY-FALSE-POSITIVE.
If not met: "CANARY SUPPRESSED: {N} field(s) not updated — {list}"

Full confirmation block:
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.
```

---

## V-04

**Axes:** Phrasing register (conversational/descriptive) + Lifecycle emphasis (compressed
phases, soft self-check boundaries)
**Hypothesis:** Replacing imperative all-caps STOP gates and DO NOT directives with
descriptive phrasing and self-check bullets reduces parsing friction. The LLM may
exercise better judgment about edge cases when the framing describes what to look for
rather than commanding what is forbidden. Phase boundaries are conveyed by output
structure rather than explicit gate language.

---

```
---
name: mock-accept
description: Step 2 of mock-first workflow. Reads mock artifact, applies auto-flag rules,
  evaluates non-auto namespaces through Architect / Strategy / PM roles, writes
  MOCK-ACCEPTED or REAL-REQUIRED decisions per namespace, writes review artifact, writes
  Status fields back in-place.
allowed-tools: [Read, Write, Edit, Glob]
---

You are running /mock:accept.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

Starting position: every namespace is REAL-REQUIRED until a positive argument earns
it an escape. The review process is looking for namespaces where simulation genuinely
covers the decision need — not namespaces where nothing is visibly wrong.

---

Step 1 — Read the artifact

Read {mock-artifact-path} and collect the namespace name, Category field, and Status
field for each namespace section. Then read TOPICS.md and note the tier and any
compliance tags for {topic}.

Write out: "Tier: {N} (source: TOPICS.md | --tier | default)" and list all namespaces
with their Category and current Status.

When all namespaces are listed, move to Step 2.

---

Step 2 — Apply automatic flags

Three rules apply before any role-based evaluation. They are not overridable by role
verdicts or mock quality.

  If a namespace has Category EVIDENCE-HEAVY: mark it REAL-REQUIRED with trigger
  EVIDENCE-HEAVY. These namespaces require real empirical data by category definition.

  If tier >= 2 and the namespace is one of {trace-*, scout-feasibility, listen-*,
  scout-competitors}: mark it REAL-REQUIRED with trigger TIER-CRITICAL. At Tier 2,
  these gate go/no-go decisions.

  If compliance tags are present for the topic and the namespace is scout-compliance
  or trace-permissions: mark it REAL-REQUIRED with trigger COMPLIANCE. Compliance
  namespaces need traceable real sources.

Write two lists before continuing:
  - Auto-flagged (REAL-REQUIRED): each namespace with its trigger reason
  - Remaining (still in REAL-REQUIRED default, eligible for role evaluation): each with Category

Before moving to role evaluation, acknowledge all three constraint labels:
  [EVIDENCE-HEAVY]: no auto-flagged namespace in this category will receive MOCK-ACCEPTED
  [TIER-CRITICAL]: no auto-flagged namespace in this category will receive MOCK-ACCEPTED
  [COMPLIANCE]: no auto-flagged namespace in this category will receive MOCK-ACCEPTED

Role evaluation only applies to namespaces on the "remaining" list. Applying evaluation
to an auto-flagged namespace is an AUTO-RULE CONTAMINATION error and any resulting
verdict is void.

When both lists are written and all three constraint labels acknowledged, move to Step 3.

---

Step 3 — Architect evaluation (remaining namespaces)

For each namespace on the remaining list, check architectural plausibility. Answer three
questions using specific entity names — generic statements like "the structure looks fine"
or "the mock is plausible" do not satisfy these questions:

  1. Which system component, dependency, or interface in the mock confirms plausibility?
     Or: what specific element creates a contradiction?

  2. Which data flow, state transition, or API shape does the mock imply for {topic}?
     Or: what specific element creates an inconsistency?

  3. Which architectural fact about {topic} does this namespace's mock most directly
     depend on, and is the mock consistent with that fact?

Based on the answers, reach a verdict: CONSISTENT-WITH-ARCHITECTURE or
CONTRADICTS-ARCHITECTURE.

For any namespace where the verdict is CONTRADICTS-ARCHITECTURE, record it as
REAL-REQUIRED with trigger ARCH-IMPLAUSIBLE and set it aside — it does not proceed
to Strategy evaluation.

Write out:
  - Which namespaces are set aside (CONTRADICTS-ARCHITECTURE)
  - Which namespaces continue to Step 4

---

Step 4 — Strategy evaluation (namespaces that passed Architect check)

For each namespace that cleared the Architect gate, evaluate strategic adequacy.
These three questions must be answered with specific named elements:

  1. Which specific Tier {tier} decision is this namespace intended to support?
     (This answer feeds the SLOT 1 position in any MOCK-ACCEPTED block — a generic
     answer like "supports planning needs" means SLOT 1 cannot be completed correctly.)

  2. What belief would the team form about {topic} if this namespace runs as MOCK-ACCEPTED,
     and would that belief be correct or incorrect?

  3. What coverage gap would keep this namespace in its REAL-REQUIRED default — or, if
     there is no gap, state that explicitly and name what the namespace positively demonstrates.

Verdict: ADEQUATE FOR TIER {tier} or INSUFFICIENT FOR TIER {tier}.

For any namespace with verdict INSUFFICIENT, record it as REAL-REQUIRED with trigger
STRATEGY-INADEQUATE and set it aside — it does not proceed to PM evaluation.

Write out:
  - Which namespaces are set aside (STRATEGY-INADEQUATE)
  - Which namespaces continue to Step 5

---

Step 5 — PM evaluation (namespaces that passed Strategy check)

For each namespace that cleared the Strategy gate, check structural completeness.

  1. Which required sections are present in the mock for this namespace?

  2. Which enforcement gate, decision table, or required output structure is present
     — or, if absent, which element is missing and where is it defined?

  3. Is there a structural gap that would keep this namespace in REAL-REQUIRED — or,
     if not, what does the namespace positively demonstrate about structural completeness?

Verdict: STRUCTURALLY ADEQUATE or STRUCTURALLY INCOMPLETE.

For any namespace with verdict STRUCTURALLY INCOMPLETE, record it as REAL-REQUIRED
with trigger PM-INCOMPLETE.

Namespaces where all three roles return positive verdicts are eligible for MOCK-ACCEPTED
— but they still need the positive argument in SLOT 1 and SLOT 2 to earn it.

---

Step 6 — Write decision blocks

For every namespace, write a decision block. The trigger field appears on the second
line of each block.

Allowed trigger values:
  EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE |
  STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE

For MOCK-ACCEPTED (only when all three roles returned positive verdicts):

  Decision: MOCK-ACCEPTED
  trigger = n/a
  reason-code: [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    Use these exact codes. No paraphrase. No invented codes.

  Structural position (SLOT 1):
    Name the specific Tier {tier} decision this namespace supports, using the
    Strategy SQ-1 answer. "Adequate for planning" without a named decision is a
    SLOT-VIOLATION. Classify as: STRUCTURAL-FORM or TIER-GATING.

  Contrast (SLOT 2 — a separate block from SLOT 1):
    Name a contrasting namespace type and explain what structural factor makes real
    evidence necessary there but not here. "Unlike {namespace type}, which requires
    real evidence because {structural factor}, this namespace's outputs are fully
    determined by {structural form property}." A statement without a named contrasting
    namespace is CONTRAST-INCOMPLETE. Merging SLOT 1 and SLOT 2 is RATIONALE-INCOMPLETE.

For REAL-REQUIRED driven by role evaluation:
  Decision: REAL-REQUIRED
  trigger = {STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE}
  Failing evaluation: [which role]
  Failing verdict: [full verdict text]
  SQ answer driving verdict: [present-tense with artifact as subject, not role as subject.
    "Section 4.2 lacks a tier-boundary gate" is valid. "Architect found no gate" is a
    VERDICT-ECHO error.]
  Artifact state: [present-tense, artifact as subject — this feeds next-steps]

For REAL-REQUIRED auto-flagged:
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

When all decision blocks are complete, move to Step 7.

---

Step 7 — Write the review artifact

Write simulations/mock/{topic}-review-{date}.md with three sections:

  Coverage Review table: | Namespace | Category | Decision | trigger |
  Include one row per namespace. Use this ordering:
    Critical namespaces first ({trace-*, scout-feasibility, listen-*, scout-competitors}),
    non-critical evaluation-driven next, evidence-heavy and compliance last.

  Next steps list (ordered: critical REAL-REQUIRED first, then evaluation-driven,
  then evidence-heavy/compliance):
    Priority 1: /{skill-id} {topic} — {Artifact state}
    Priority 2: /{skill-id} {topic} — {Artifact state}
    Priority 3: /{skill-id} {topic} — trigger: {trigger value}

  Risk statement:
    "Highest-risk gap: {namespace} — {specific Tier {tier} decision at risk}
    — urgency: {BLOCKING | HIGH | MEDIUM}"
    If more than one namespace is flagged REAL-REQUIRED, add urgency grouping commentary.

When the artifact is written, move to Step 8.

---

Step 8 — Write status back (this step is not skippable)

Use the Edit tool to update {mock-artifact-path} in-place. Change only the Status
fields. For each namespace, replace:

  Status: MOCK (awaiting review)

with one of:
  Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
  Status: REAL-REQUIRED [{trigger value}]

After all edits, verify that zero Status fields still read "MOCK (awaiting review)".

If verified: write the CANARY ASSERTION verbatim:
  "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."

If not verified (some fields unchanged): write:
  "CANARY SUPPRESSED: {N} field(s) not updated — {list}"

Do not write the CANARY ASSERTION unless the condition is confirmed true. Writing it
when it is false is a CANARY-FALSE-POSITIVE error.

Close with:
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.
```

---

## V-05

**Axes:** Role sequence (Strategy first, then Architect, then PM) + Inertia framing
throughout
**Hypothesis:** Running Strategy first establishes the tier decision anchor before
plausibility or structure is checked — this creates a stronger SLOT 1 argument because
the decision name is established before architectural or structural evidence is weighed.
Combined with inertia framing throughout, every role evaluation begins by asking "what
would earn escape?" rather than "is there anything wrong?" The combination amplifies
both effects: the tier anchor is front-loaded, and the escape argument must be built
layer by layer across all three roles.

---

```
---
name: mock-accept
description: Step 2 of mock-first workflow. Reads mock artifact, applies auto-flag rules,
  evaluates non-auto namespaces through Strategy / Architect / PM (in that order), writes
  MOCK-ACCEPTED or REAL-REQUIRED decisions per namespace, writes review artifact, writes
  Status fields back in-place.
allowed-tools: [Read, Write, Edit, Glob]
---

You are running /mock:accept.

INPUTS:
  topic:         {topic}
  mock-artifact: {mock-artifact-path}
  tier:          {1|2|3} — read from TOPICS.md if not specified; default 1

INERTIA POSITION:
  REAL-REQUIRED is the default and requires no argument. MOCK-ACCEPTED is an escape
  from gravity. A namespace earns escape only by producing a positive argument across
  all three evaluation roles: (1) a named tier decision the mock supports, (2) a
  confirmed plausible architecture, and (3) demonstrated structural completeness.
  Each role adds one layer of the escape argument. An incomplete argument = inertia holds.

ROLE EVALUATION ORDER (this run):
  STEP 3 — Strategy (tier decision anchor — establishes what the mock must support)
  STEP 4 — Architect (plausibility — checks whether the mock's architecture is consistent)
  STEP 5 — PM (structural completeness — checks whether the mock's structure is adequate)

Strategy runs first because the tier decision anchor (SLOT 1 in MOCK-ACCEPTED) must
be named before plausibility or structure can be evaluated against it.

---

STEP 1 — READ

Read {mock-artifact-path}. Extract from each namespace section: namespace name,
Category field, Status field. Read TOPICS.md; record tier for {topic} and compliance tags.

Output:
  Tier: {N} (source: TOPICS.md | --tier | default)
  Namespaces: [{name, Category, current Status}]

DO NOT proceed to STEP 2 until all namespace fields are extracted and listed.

---

STEP 2 — AUTO-FLAG

Three rules. All mandatory. Fire before role evaluation. Inertia is unconditional here:
no role evaluation, no mock quality, and no user override lifts these flags.

  RULE 1 — EVIDENCE-HEAVY (all tiers):
    IF Category == EVIDENCE-HEAVY THEN: REAL-REQUIRED, trigger = EVIDENCE-HEAVY
    Inertia note: Empirical namespaces carry unconditional inertia. Simulation
    produces structural appearance without the falsifiability that makes evidence meaningful.

  RULE 2 — TIER-CRITICAL (Tier 2+):
    IF tier >= 2 AND namespace in {trace-*, scout-feasibility, listen-*, scout-competitors}
    THEN: REAL-REQUIRED, trigger = TIER-CRITICAL
    Inertia note: These gate Tier 2 go/no-go decisions. The stakes cannot be held by simulation.

  RULE 3 — COMPLIANCE (when active):
    IF compliance tags present AND namespace in {scout-compliance, trace-permissions}
    THEN: REAL-REQUIRED, trigger = COMPLIANCE
    Inertia note: Compliance requires audit-traceable sources. Synthetic artifacts cannot
    provide that substance.

Output:
  Auto-flagged (inertia unconditional): [{namespace}: trigger = {rule}]
  Remaining (inertia default — escape must be earned): [{namespace}: Category = {value}]

===================================================================
INERTIA GATE — THREE UNCONDITIONAL CONSTRAINTS (all 3 required):

  [EVIDENCE-HEAVY]  FORBIDDEN: MOCK-ACCEPTED on any EVIDENCE-HEAVY namespace.
  [TIER-CRITICAL]   FORBIDDEN: MOCK-ACCEPTED on any TIER-CRITICAL namespace.
  [COMPLIANCE]      FORBIDDEN: MOCK-ACCEPTED on any COMPLIANCE namespace.

  All 3 labels must appear. Two-of-three does not satisfy this gate.

AUTO-RULE CONTAMINATION GUARD:
  DO NOT apply evaluation to auto-flagged namespaces. Named error: AUTO-RULE CONTAMINATION.

DO NOT proceed to STEP 3 until partition is confirmed and all 3 inertia labels stated.
===================================================================

---

STEP 3 — STRATEGY EVALUATION (non-auto namespaces — runs first in this variation)

The inertia question for Strategy: can this namespace earn its tier decision anchor?
Without a named Tier {tier} decision, SLOT 1 cannot be completed and escape is impossible.
Strategy runs first because it establishes what the mock is supposed to support — before
plausibility or structure is checked.

For each remaining namespace, answer three sub-questions using entity-naming grammar:

| Row # | Sub-question | Inertia direction |
|-------|-------------|-------------------|
| 1     | Name the specific Tier {tier} decision this namespace is intended to support. [This answer becomes SLOT 1 anchor in MOCK-ACCEPTED. No named decision = inertia holds at SLOT 1.] | No named decision = inertia unconditional |
| 2     | Name the belief the team would form about {topic} if this namespace runs as MOCK-ACCEPTED. State whether that belief would be correct or incorrect. | Incorrect belief = inertia holds |
| 3     | Name the coverage gap that would keep this namespace in REAL-REQUIRED — or: "No gap — namespace positively demonstrates coverage adequacy for Tier {tier}". | Named gap = inertia holds |

  Strategy Verdict: ADEQUATE FOR TIER {tier} (tier anchor established — proceed to Architect)
                 or INSUFFICIENT FOR TIER {tier} (inertia holds — REAL-REQUIRED)

CROSS-STEP GUARD — Strategy to Architect:
  For any namespace where strategy-verdict = INSUFFICIENT:
    preliminary decision = REAL-REQUIRED, trigger = STRATEGY-INADEQUATE
    DO NOT pass to Architect Evaluation. Named error: STRATEGY-TO-ARCH-GUARD-BYPASS.
  Record:
    Strategy-blocked (inertia held — no tier anchor): [{list}]
    Proceeding to Architect (tier anchor established): [{list}]

DO NOT proceed to STEP 4 until Strategy verdicts and guard assignments are complete.

---

STEP 4 — ARCHITECT EVALUATION (non-auto, Strategy-passed namespaces only)

The inertia question for Architect: is the mock's architecture consistent with {topic}'s
actual component structure, dependencies, and integration boundaries? A contradiction
means the mock would produce a misleading architectural belief — inertia holds regardless
of structural completeness.

Entry condition: namespaces not on the Strategy-blocked list.
Named error for violating entry: GUARD-BYPASS CONTAMINATION.

For each qualifying namespace, answer sub-questions using entity-naming grammar:

| Row # | Sub-question | Inertia direction |
|-------|-------------|-------------------|
| 1     | Name the system component, dependency, or interface in the mock that confirms plausibility — or: "Contradiction found — name the specific element". | Contradiction = inertia holds |
| 2     | Name the data flow, state transition, or API shape the mock implies for {topic} — or: "Inconsistency found — name the specific element". | Inconsistency = inertia holds |
| 3     | Name the architectural fact about {topic} this namespace most directly depends on. State whether the mock is consistent with that fact. | Inconsistent = inertia holds |

  Architect Verdict: CONSISTENT-WITH-ARCHITECTURE (architectural inertia overcome — proceed to PM)
                  or CONTRADICTS-ARCHITECTURE (inertia holds — REAL-REQUIRED, trigger = ARCH-IMPLAUSIBLE)

CROSS-STEP GUARD — Architect to PM:
  For any namespace where verdict = CONTRADICTS-ARCHITECTURE:
    preliminary decision = REAL-REQUIRED, trigger = ARCH-IMPLAUSIBLE
    DO NOT pass to PM Evaluation. Named error: ARCH-TO-PM-GUARD-BYPASS.
  Record:
    Arch-blocked (inertia held by contradiction): [{list}]
    Proceeding to PM (Architect inertia overcome): [{list}]

DO NOT proceed to STEP 5 until Architect verdicts and guard assignments are complete.

---

STEP 5 — PM EVALUATION (non-auto, Strategy-passed, Arch-passed namespaces only)

The inertia question for PM: does the mock contain the required structural elements?
If required sections or enforcement gates are absent, the escape argument is incomplete
even if Strategy and Architect returned positive verdicts. All three layers must hold.

Entry condition: namespaces not on Strategy-blocked or Arch-blocked lists.
Named error for violating entry: GUARD-BYPASS CONTAMINATION.

For each qualifying namespace:

| Row # | Sub-question | Inertia direction |
|-------|-------------|-------------------|
| 1     | Name the required sections present in the mock for this namespace. | Missing required sections = inertia holds |
| 2     | Name the enforcement gate, decision table, or required output structure present — or: "Absent — name the missing element and which section defines it". | Absent gate = inertia holds |
| 3     | Name one structural gap that would keep this namespace in REAL-REQUIRED — or: "No gap — namespace positively demonstrates structural completeness". | Named gap = inertia holds |

  PM Verdict: STRUCTURALLY ADEQUATE (all three inertia layers overcome — eligible for MOCK-ACCEPTED)
           or STRUCTURALLY INCOMPLETE (inertia holds — REAL-REQUIRED, trigger = PM-INCOMPLETE)

DO NOT proceed to STEP 6 until PM verdicts are written for every qualifying namespace.

---

STEP 6 — DECISIONS WITH INERTIA CITATION

Only namespaces where ALL THREE roles overcame inertia may receive MOCK-ACCEPTED.
The escape argument is composed across SLOT 1 (tier anchor from Strategy) and SLOT 2
(contrast establishing why inertia is overcome here but holds elsewhere). Both slots
are required; a single merged block is RATIONALE-INCOMPLETE.

Trigger field: second line of every decision block.
  Values: trigger = EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE |
                    STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE

MOCK-ACCEPTED template — full three-layer inertia-escape form:

  Decision: MOCK-ACCEPTED
  trigger = n/a
  reason-code: [STRUCTURAL-COVERAGE-SUFFICIENT] [DOMAIN-KNOWLEDGE-CONSISTENT]
    (exact codes only; no paraphrase; no invented codes)

  Structural position (SLOT 1 — Strategy SQ-1 anchor, established before plausibility
  and structure were checked):
    Feeds tier decision: {SQ-1 answer — name the specific Tier {tier} decision}.
    Generic adequacy without a named decision = SLOT-VIOLATION.
    Classify: STRUCTURAL-FORM | TIER-GATING.

  Contrast (SLOT 2 — dedicated, structurally separate from SLOT 1 — the inertia
  escape argument naming why escape is earned here but not elsewhere):
    Unlike {namespace type}, which carries {structural factor} requiring real evidence
    because {reason}, this namespace's outputs are fully determined by {structural form
    property}. Confirmatory sentence without a named contrasting namespace = CONTRAST-INCOMPLETE.
    Merged with SLOT 1 = RATIONALE-INCOMPLETE.

REAL-REQUIRED template — evaluation-driven:
  Decision: REAL-REQUIRED
  trigger = {STRATEGY-INADEQUATE | ARCH-IMPLAUSIBLE | PM-INCOMPLETE}
  Failing evaluation: [Strategy | Architect | PM]
  Failing verdict: [full verdict string]
  SQ answer driving verdict:
    [Present-tense, artifact as subject. ERROR — VERDICT-ECHO: role as subject.]
  Artifact state: [present-tense, artifact as subject — propagates to next-steps]

REAL-REQUIRED template — auto-flagged:
  Decision: REAL-REQUIRED
  trigger = {EVIDENCE-HEAVY | TIER-CRITICAL | COMPLIANCE}

DO NOT proceed to STEP 7 until all decision blocks are complete.

---

STEP 7 — WRITE REVIEW ARTIFACT

Write simulations/mock/{topic}-review-{date}.md.

Coverage Review table (inertia-outcome summary):
  | Namespace | Category | Decision | trigger |

Ordering rule (state explicitly in artifact):
  "Critical namespaces first ({trace-*, scout-feasibility, listen-*, scout-competitors}),
   non-critical evaluation-driven next, evidence-heavy and compliance last."

  Priority 1 — Critical REAL-REQUIRED: /{skill-id} {topic} — {Artifact state}
  Priority 2 — Non-critical evaluation-driven: /{skill-id} {topic} — {Artifact state}
  Priority 3 — Evidence-heavy / compliance: /{skill-id} {topic} — trigger: {trigger value}

Cross-namespace risk statement (inertia-weighted):
  "Highest-risk inertia gap: {namespace} — {specific Tier {tier} decision at risk}
  — urgency: {BLOCKING | HIGH | MEDIUM}"
  Include urgency grouping commentary for each priority group when more than one namespace.

DO NOT proceed to STEP 8 until review artifact is confirmed written.

---

STEP 8 — WRITE STATUS BACK (mandatory, non-skippable)

Edit {mock-artifact-path} in-place using Edit tool. Replace Status fields only.

  REPLACE: Status: MOCK (awaiting review)
  WITH one of:
    Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]
    Status: REAL-REQUIRED [{trigger value}]

CANARY ASSERTION (write only when verified true):
  "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."
PROHIBITED if any Status field remains. Named error: CANARY-FALSE-POSITIVE.
If not met: "CANARY SUPPRESSED: {N} field(s) not updated — {list}"

Full confirmation block:
  Annotations updated in: {mock-artifact-path}
  Review written: simulations/mock/{topic}-review-{date}.md
  Status fields updated: {N} of {N}
  Count: 0 Status fields remain as MOCK (awaiting review). Confirmed.
```

---

## Variation Summary

| ID | Axis | Hypothesis | Key structural change |
|----|------|------------|-----------------------|
| V-01 | Inertia framing | Front-loading the escape-from-gravity frame at every phase gate and decision slot reduces zero-argument acceptances | REAL-REQUIRED framed as gravity throughout; SLOT 2 moved before SLOT 1; inertia notes added per auto-rule |
| V-02 | Role sequence (PM → Strategy → Arch) | PM structural filter first minimizes judgment work by disqualifying incomplete mocks before strategic or plausibility analysis | PM runs first; guard chain inverted; cross-step guards renamed for new order |
| V-03 | Output format (table-first) | Structured tables at every step make missing criteria immediately visible and create an accumulating ledger rather than a reconstructed one | Decision table initialized at STEP 1, grows per step; STEP 6 confirms rather than authors |
| V-04 | Phrasing register + compressed lifecycle | Descriptive framing and soft self-checks reduce parsing friction and allow better judgment on edge cases | Imperative STOP gates removed; phrasing converted to descriptive; phase boundaries implied by output structure |
| V-05 | Role sequence (Strategy first) + inertia framing | Running Strategy first establishes the tier anchor before plausibility/structure; inertia framing amplifies by requiring the escape argument to be built layer by layer | Strategy → Architect → PM order; inertia notes at every step; SLOT 1 framed as "established before plausibility check" |
