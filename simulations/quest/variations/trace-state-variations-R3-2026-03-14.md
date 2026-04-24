**R3 variations written** — `simulations/quest/variations/trace-state-variations-R3-2026-03-14.md`

### Variation map

| V | Axis | Key mechanism |
|---|------|---------------|
| **V-01** | Role sequence | Pre-sweep hypothesis: ANOMALY FINDER predicts structural risk after Domain Expert, before Compiler; sweep table gains `Predicted?` column; discrepancies are their own signal |
| **V-02** | Output format | Evidence-scored sweep: strength 1/2/3 per found row; gate requires ≥2 found **AND** ≥1 strength ≥ 2; blocks all-pattern-based completions |
| **V-03** | Lifecycle emphasis | Compressed trace (exactly 4 steps, exactly 1 rejection); expanded anomaly section with consequence chain (trigger → corruption → detection → remediation) per finding |
| **V-04** | Role sequence + lifecycle | Pre-sweep + compressed trace + consequence chains — the three phases prime each other; Compiler step selection is guided by Pre-Sweep predictions |
| **V-05** | Phrasing register + inertia framing | Conversational second-person throughout; inertia framing opens with "a team that skips this ships state logic untested"; C-14/C-15/C-16/C-17 requirements preserved verbatim |

### What R3 is testing beyond R2

R2 V-04 already implements all four new rubric criteria (C-14/C-15/C-16/C-17) — so R3 doesn't need to find a structure that includes them. R3 is testing:

- Whether **prediction before execution** improves finding accuracy (V-01, V-04)
- Whether **quality scoring** on the sweep gate is stronger than a quantity gate alone (V-02)
- Whether **shifting cognitive weight to anomaly analysis** produces deeper findings (V-03, V-04)
- Whether **register and framing** affect output depth or are neutral (V-05)
anding the anomaly section improve finding depth? | V-03, V-04 |
| Does conversational register affect output depth or specificity? | V-05 |
| Does inertia framing (naming what this replaces) anchor model behavior? | V-05 |

### Key design choices

**V-01 pre-sweep**: The ANOMALY FINDER sees only the Domain Expert tables -- not the trace.
It predicts which anomaly types are structurally likely, referencing specific S-IDs and OP-IDs.
The Predicted? column in the final sweep creates a falsifiable record: predictions that miss
actual findings reveal structural blind spots; predictions confirmed by the trace validate the
analysis. This is a detect-before-trace pattern that doesn't exist in R1/R2.

**V-02 evidence strength**: Scale is 1 (pattern suggests this could occur -- no direct step),
2 (direct trace evidence -- a specific step shows it happening), 3 (multi-step chain -- confirmed
across multiple steps with cascading evidence). A sweep with all strength-1 findings doesn't
pass the gate. This converts C-14's quantity gate into a quality gate.

**V-03 lifecycle compression**: The trace cap (exactly 4 steps, exactly 1 rejection) forces the
model to choose the 4 most anomaly-exposing transitions rather than expanding the trace to avoid
difficult analysis. The consequence chain format forces impact reasoning in 4 dimensions per
finding. The explicit "N/A: [reason]" rule for blank anomaly register cells enforces C-17
mechanically rather than declaratively.

**V-04 combination**: Pre-sweep prediction forces structural analysis before execution evidence
is available. Compressed trace forces commitment to the 4 most informative steps. Consequence
chains force deep impact analysis. The three mechanisms operate at different phases and
reinforce each other -- the expected cost is cognitive overhead; the expected gain is that
each phase primes the next.

**V-05 register**: All R1/R2 variations use formal third-person ("The Domain Expert's state
machine is locked after its gate"). V-05 uses second-person throughout ("You are the Domain
Expert. Your tables are locked once you finish this section."). Inertia framing names what
this replaces: teams that skip this step ship state logic untested and find invalid transitions
in production. Testing whether register and framing affect output depth or are neutral.

---

## V-01: Role Sequence -- Pre-Sweep Hypothesis (Single-axis)

**Axis:** Role sequence -- ANOMALY FINDER runs twice: first to predict structural risk
from the Domain Expert tables alone (before the Compiler trace exists), then to verify
actual findings against the trace. The sweep table gains a Predicted? column creating
a falsifiable predict-then-verify record.

**Hypothesis:** In all R1/R2 variations, ANOMALY FINDER only sees the completed trace and
sweeps it reactively. Pre-declaring which anomaly types are structurally likely from the state
machine alone forces the model to reason about structural risk independently of execution
evidence. A prediction that misses an actual finding reveals a structural analysis gap;
a prediction confirmed by the trace is a stronger signal than a finding discovered reactively.
The Predicted? column makes discrepancies mechanically visible.

```
You are running /trace-state. Fill in this structured template.
Four sections execute in sequence. Each gate must complete before the next begins.
All table headers are fixed -- do not reorder, rename, or remove any column.
The Domain Expert's state machine is locked after its gate. All downstream sections are
read-only on it -- gaps become findings, not retroactive additions.

CROSS-REFERENCE DISCIPLINE: Every entity (state, operation, invariant) is declared once
and referenced everywhere by ID. An S-ID, OP-ID, or INV-ID used downstream that was not
declared in DOMAIN EXPERT is an anomaly finding, not a silent addition.

ROLE SEQUENCE: DOMAIN EXPERT -> PRE-SWEEP -> COMPILER -> ANOMALY FINDER
PRE-SWEEP reads only the Domain Expert tables and predicts structural risk before the trace
is run. ANOMALY FINDER later compares actual findings to those predictions.

---

## SETUP: PRIOR SIGNALS
[Search simulations/trace/ and simulations/scout/ for any prior state, request, or contract
artifacts on this topic.]
Prior signals: [List files found, or write "None -- starting fresh."]

---

## DOMAIN EXPERT: DECLARE

[Use vocabulary a Sales rep, support engineer, or finance analyst would recognize without
translation. Generic labels ("Pending", "Active", "Done") do not pass -- use the vocabulary
the domain actually uses in its systems.]

Entity: [Domain-realistic name -- the kind that appears in a CRM, helpdesk, or ERP]
Domain: [Sales / Customer Service / Finance]

State machine:
| State ID | State Name | Domain Description | Entry Condition | Terminal? |
|----------|-----------|-------------------|----------------|-----------|
| S-01 | [Name] | [What this state means to a domain practitioner] | [What must be true to enter this state] | yes / no |
| S-02 | [Name] | [What this state means to a domain practitioner] | [What must be true to enter this state] | yes / no |
[Minimum 4 rows. All S-IDs used downstream must be declared here.]

Valid transitions:
| Op ID | Operation Name | From State (S-ID) | To State (S-ID) | Domain Meaning |
|-------|---------------|------------------|----------------|----------------|
| OP-01 | [Name] | [S-ID] | [S-ID] | [Why a practitioner would trigger this operation] |
| OP-02 | [Name] | [S-ID] | [S-ID] | [Why a practitioner would trigger this operation] |
[All OP-IDs used downstream must be declared here.]

Invariants:
| INV ID | Invariant Statement | Scope (S-IDs) | Violation Consequence |
|--------|---------------------|---------------|----------------------|
| INV-01 | [Precisely stated invariant] | [S-IDs or "all states"] | [What breaks in production if violated] |
[Minimum 1 row. All INV-IDs used downstream must be declared here.]

Domain Expert gate:
[ ] Entity and domain named with domain vocabulary -- no generic placeholders
[ ] All states have S-IDs, entry conditions, and domain-language descriptions
[ ] All valid transitions declared with Op IDs before any trace steps are written
[ ] All invariants declared with INV-IDs, scope listed as S-IDs, and violation consequence
[ ] No duplicate IDs (each S-ID, OP-ID, INV-ID appears exactly once)

---

## PRE-SWEEP: HYPOTHESIS

[Read ONLY the Domain Expert tables above. The Compiler trace has not been written yet.
Based on the state machine structure alone, predict which anomaly types are structurally
likely. Reference specific S-IDs, OP-IDs, and INV-IDs where possible. This is a falsifiable
prediction -- it will be compared against actual findings after the trace completes.]

Hypothesis table:
| Anomaly Type | Likely? | Structural Reasoning | At-Risk IDs |
|-------------|---------|----------------------|-------------|
| Invalid transition | yes / no / unclear | [Why the transition table makes this likely -- which transitions look dangerous] | [OP-IDs + S-IDs, or --] |
| Missing precondition check | yes / no / unclear | [Which transitions appear under-guarded at the system boundary] | [OP-IDs + S-IDs, or --] |
| Invariant violation | yes / no / unclear | [Which invariant scope + transition combinations could produce a violation] | [INV-IDs + OP-IDs, or --] |
| Race condition | yes / no / unclear | [Whether multiple operations share a state and could interleave] | [OP-IDs + S-IDs, or --] |
| Undeclared reference | yes / no / unclear | [Whether the transition table appears complete or has visible gaps] | [Suspicious IDs, or --] |

Pre-sweep gate:
[ ] All 5 rows completed with a verdict and specific ID-referenced reasoning
[ ] At least 1 row predicts "yes" -- if all are "no/unclear", the state machine may be too simple
[ ] Reasoning references declared IDs, not generic statements

---

## COMPILER: TRACE

[Read-only on the Domain Expert tables. All references must use declared IDs.
If a state, operation, or invariant is referenced that was not declared in DOMAIN EXPERT,
do not add it retroactively -- flag it in the undeclared reference log below.]

Operation trace:
| Step | Before-State (S-ID: Name) | Operation (OP-ID: Name) | Preconditions (state-specific) | After-State (S-ID: Name) | Postconditions | INV Check |
|------|--------------------------|------------------------|-------------------------------|--------------------------|----------------|-----------|
| 1 | [S-ID: Name] | [OP-ID: Name] | - [Precondition] | [S-ID: Name] | - [Postcondition] | INV-01: pass |
| 2 | [S-ID: Name] | [OP-ID: Name] | - [Precondition] | [S-ID: Name] | - [Postcondition] | INV-01: pass |
[Minimum 4 happy-path steps. INV Check format: "INV-ID: pass" or "INV-ID: VIOLATION -- [reason]".]

Rejected transitions:
| Step | Before-State (S-ID: Name) | Attempted Op (OP-ID or "undeclared: [name]") | Failing Precondition | Rejection Behavior | After-State |
|------|--------------------------|---------------------------------------------|--------------------|--------------------|-------------|
| [N] | [S-ID: Name] | [OP-ID or "undeclared: [name]"] | [Specific precondition not met] | [reject / error / exception] | [Same S-ID: Name] |
[Minimum 1 row. Undeclared operations must use "undeclared: [name]" prefix.]

Undeclared reference log:
[List any S-ID, OP-ID, or INV-ID referenced but not declared in DOMAIN EXPERT.]
- [Type: S/OP/INV] [ID attempted] -- [what was needed and why it was not in the declaration]
[Write "None -- all references resolved to declared IDs." if no undeclared references.]

Compiler gate:
[ ] Every step references only declared S-IDs and OP-IDs
[ ] INV Check at every step references a declared INV-ID
[ ] At least 1 rejected transition with named failing precondition
[ ] Undeclared reference log is present (even if empty)

---

## ANOMALY FINDER: REVIEW

[Sweep the Compiler's trace for all five anomaly types. Compare actual findings to your
Pre-Sweep predictions. Every row requires a verdict.
MINIMUM-FOUND REQUIREMENT: At least 2 of the first 4 rows must have verdict = "found".
All findings must reference their triggering OP-ID, S-ID, and INV-ID (if applicable).
Blank ID in any "found" row is a cross-reference gap -- write "N/A: [reason]" instead.
Do not fabricate findings to meet the minimum. If genuinely fewer than 2 types present,
write "Trace insufficient: [reason]" and recommend scenario enrichment.]

Anomaly sweep:
| Anomaly Type | Verdict | OP-ID + S-ID | INV-ID | Production Consequence | Predicted? |
|-------------|---------|-------------|--------|----------------------|------------|
| Invalid transition | found / none | [OP-ID at S-ID, or --] | -- | [Consequence, or --] | yes / no |
| Missing precondition check | found / none | [OP-ID at S-ID, or --] | -- | [Consequence, or --] | yes / no |
| Invariant violation | found / none | [OP-ID at S-ID, or --] | [INV-ID, or --] | [Consequence, or --] | yes / no |
| Race condition | found / none | [OP-A + OP-B at S-ID, or --] | [INV-ID, or --] | [Consequence, or --] | yes / no |
| Undeclared reference | found / none | [ID attempted, or --] | -- | [Scope creep / silent drift, or --] | yes / no |

Minimum-found check:
[ ] At least 2 of the first 4 rows have verdict = "found"
[ ] Each "found" verdict cites declared IDs
[ ] No blank ID cells in any "found" row (use "N/A: [reason]" if genuinely inapplicable)

Prediction reconciliation:
[For each row where Predicted = "yes" but verdict = "none": explain why the prediction was wrong.]
[For each row where Predicted = "no" but verdict = "found": explain what structural signal was missed.]
[Write "All predictions confirmed." if no discrepancies.]

Race condition detail (complete if verdict = found):
  Concurrent ops:  [OP-A (OP-ID)] and [OP-B (OP-ID)] on entity in state [S-ID: Name]
  Interleave:      [Which reads and writes happen in what order, and where they conflict]
  Resolution:      [Which operation wins, or how conflict is detected; entity final state]

Anomaly register:
| A-ID | Type | OP-ID | S-ID | INV-ID | Description | Severity |
|------|------|-------|------|--------|-------------|---------|
| A-01 | [type] | [OP-ID or N/A: [reason]] | [S-ID] | [INV-ID or N/A: [reason]] | [Specific description] | HIGH / MEDIUM / LOW |
[Minimum 2 rows -- one per "found" verdict (including undeclared reference if found).]

---

Write artifact: simulations/trace/state/{topic}-state-{date}.md
Frontmatter: skill, topic, date, domain, entity, state_count, operation_count, anomaly_count,
             anomaly_types (list), invariant_count, race_condition_analyzed (true/false),
             rejected_transitions (count), anomaly_types_found (count),
             undeclared_references (count), predictions_accurate (count/total).
```

---

## V-02: Output Format -- Evidence-Scored Sweep (Single-axis)

**Axis:** Output format -- the anomaly sweep table gains an Evidence Strength column (1-3)
per found row. The gate requires >=2 found rows AND >=1 row at strength >= 2. An all-strength-1
sweep does not pass. The anomaly register gains a Strength column.

**Hypothesis:** C-14's minimum-found gate is a quantity gate: 2 found rows passes regardless
of how shallow those findings are. Evidence strength converts it to a quality gate. Strength 1
(indirect/pattern-based) is weaker than strength 2 (direct trace step) which is weaker than
strength 3 (multi-step cascade). Requiring at least one strength-2 or higher finding blocks
easy-path completions where a model fills in "found" with vague pattern-matching rather than
a specific step reference. The strength score also propagates to the anomaly register, making
each finding's depth visible in the artifact metadata.

```
You are running /trace-state. Fill in this structured template.
Three roles execute in sequence. Each role gate must complete before the next begins.
All table headers are fixed -- do not reorder, rename, or remove any column.
The Domain Expert's state machine is locked after its gate. COMPILER and ANOMALY FINDER are
read-only on it -- gaps become findings, not retroactive additions.

CROSS-REFERENCE DISCIPLINE: Every entity (state, operation, invariant) is declared once
and referenced everywhere by ID. An S-ID, OP-ID, or INV-ID used downstream that was not
declared in DOMAIN EXPERT is an anomaly finding, not a silent addition.

EVIDENCE STRENGTH SCALE (used in anomaly sweep and register):
  1 = Weak   -- pattern suggests this could occur; no direct trace step shows it happening
  2 = Direct -- a specific trace step shows this anomaly occurring
  3 = Chain  -- anomaly confirmed across multiple steps with cascading evidence
Only "found" verdicts receive a strength score. "None" rows leave the Strength column blank (--)

---

## SETUP: PRIOR SIGNALS
[Search simulations/trace/ and simulations/scout/ for any prior state, request, or contract
artifacts on this topic.]
Prior signals: [List files found, or write "None -- starting fresh."]

---

## DOMAIN EXPERT: DECLARE

[Use vocabulary a Sales rep, support engineer, or finance analyst would recognize without
translation. Generic labels ("Pending", "Active", "Done") do not pass -- use the vocabulary
the domain actually uses in its systems.]

Entity: [Domain-realistic name -- the kind that appears in a CRM, helpdesk, or ERP]
Domain: [Sales / Customer Service / Finance]

State machine:
| State ID | State Name | Domain Description | Entry Condition | Terminal? |
|----------|-----------|-------------------|----------------|-----------|
| S-01 | [Name] | [What this state means to a domain practitioner] | [What must be true to enter this state] | yes / no |
| S-02 | [Name] | [What this state means to a domain practitioner] | [What must be true to enter this state] | yes / no |
[Minimum 4 rows. All S-IDs used downstream must be declared here.]

Valid transitions:
| Op ID | Operation Name | From State (S-ID) | To State (S-ID) | Domain Meaning |
|-------|---------------|------------------|----------------|----------------|
| OP-01 | [Name] | [S-ID] | [S-ID] | [Why a practitioner would trigger this operation] |
| OP-02 | [Name] | [S-ID] | [S-ID] | [Why a practitioner would trigger this operation] |
[All OP-IDs used downstream must be declared here.]

Invariants:
| INV ID | Invariant Statement | Scope (S-IDs) | Violation Consequence |
|--------|---------------------|---------------|----------------------|
| INV-01 | [Precisely stated invariant] | [S-IDs or "all states"] | [What breaks in production if violated] |
[Minimum 1 row. All INV-IDs used downstream must be declared here.]

Domain Expert gate:
[ ] Entity and domain named with domain vocabulary -- no generic placeholders
[ ] All states have S-IDs, entry conditions, and domain-language descriptions
[ ] All valid transitions declared with Op IDs before any trace steps are written
[ ] All invariants declared with INV-IDs, scope listed as S-IDs, and violation consequence
[ ] No duplicate IDs

---

## COMPILER: TRACE

[Read-only on the Domain Expert tables. All references must use declared IDs.
Flag any undeclared reference in the log below -- do not add retroactively.]

Operation trace:
| Step | Before-State (S-ID: Name) | Operation (OP-ID: Name) | Preconditions (state-specific) | After-State (S-ID: Name) | Postconditions | INV Check |
|------|--------------------------|------------------------|-------------------------------|--------------------------|----------------|-----------|
| 1 | [S-ID: Name] | [OP-ID: Name] | - [Precondition] | [S-ID: Name] | - [Postcondition] | INV-01: pass |
| 2 | [S-ID: Name] | [OP-ID: Name] | - [Precondition] | [S-ID: Name] | - [Postcondition] | INV-01: pass |
[Minimum 4 happy-path steps. INV Check: "INV-ID: pass" or "INV-ID: VIOLATION -- [reason]".]

Rejected transitions:
| Step | Before-State (S-ID: Name) | Attempted Op (OP-ID or "undeclared: [name]") | Failing Precondition | Rejection Behavior | After-State |
|------|--------------------------|---------------------------------------------|--------------------|--------------------|-------------|
| [N] | [S-ID: Name] | [OP-ID or "undeclared: [name]"] | [Specific precondition not met] | [reject / error / exception] | [Same S-ID: Name] |
[Minimum 1 row.]

Undeclared reference log:
- [Type: S/OP/INV] [ID attempted] -- [why it was not declared]
[Write "None -- all references resolved to declared IDs." if no undeclared references.]

Compiler gate:
[ ] Every step references only declared S-IDs and OP-IDs
[ ] INV Check at every step references a declared INV-ID
[ ] At least 1 rejected transition with named failing precondition
[ ] Undeclared reference log is present (even if empty)

---

## ANOMALY FINDER: REVIEW

[Sweep the Compiler's trace for all five anomaly types. Every row requires a verdict.
MINIMUM-FOUND AND STRENGTH REQUIREMENT:
  (1) At least 2 of the first 4 rows must have verdict = "found"
  (2) At least 1 "found" row must have Evidence Strength >= 2 (direct or chain)
A sweep with all strength-1 findings does not pass requirement (2).
All findings must reference their triggering OP-ID, S-ID, and INV-ID (if applicable).
Blank ID in any "found" row is a cross-reference gap -- write "N/A: [reason]" instead.
Do not fabricate findings to meet thresholds. If genuinely insufficient, write
"Trace insufficient: [reason]" and recommend scenario enrichment.]

Anomaly sweep:
| Anomaly Type | Verdict | OP-ID + S-ID | INV-ID | Strength | Production Consequence |
|-------------|---------|-------------|--------|----------|----------------------|
| Invalid transition | found / none | [OP-ID at S-ID, or --] | -- | [1/2/3, or --] | [Consequence, or --] |
| Missing precondition check | found / none | [OP-ID at S-ID, or --] | -- | [1/2/3, or --] | [Consequence, or --] |
| Invariant violation | found / none | [OP-ID at S-ID, or --] | [INV-ID, or --] | [1/2/3, or --] | [Consequence, or --] |
| Race condition | found / none | [OP-A + OP-B at S-ID, or --] | [INV-ID, or --] | [1/2/3, or --] | [Consequence, or --] |
| Undeclared reference | found / none | [ID attempted, or --] | -- | [1/2/3, or --] | [Scope creep / silent drift, or --] |

Threshold check:
[ ] At least 2 of first 4 rows have verdict = "found"
[ ] At least 1 "found" row has Strength >= 2
[ ] Each "found" verdict cites declared IDs
[ ] No blank ID cells in any "found" row (use "N/A: [reason]" if genuinely inapplicable)

Race condition detail (complete if verdict = found):
  Concurrent ops:  [OP-A (OP-ID)] and [OP-B (OP-ID)] on entity in state [S-ID: Name]
  Interleave:      [Which reads and writes happen in what order, and where they conflict]
  Resolution:      [Which operation wins, or how conflict is detected; entity final state]

Anomaly register:
| A-ID | Type | OP-ID | S-ID | INV-ID | Strength | Description | Severity |
|------|------|-------|------|--------|----------|-------------|---------|
| A-01 | [type] | [OP-ID or N/A: [reason]] | [S-ID] | [INV-ID or N/A: [reason]] | [1/2/3] | [Specific description] | HIGH / MEDIUM / LOW |
[Minimum 2 rows -- one per "found" verdict. Blank ID in any row is a cross-reference gap.]

---

Write artifact: simulations/trace/state/{topic}-state-{date}.md
Frontmatter: skill, topic, date, domain, entity, state_count, operation_count, anomaly_count,
             anomaly_types (list), invariant_count, race_condition_analyzed (true/false),
             rejected_transitions (count), anomaly_types_found (count),
             undeclared_references (count), max_evidence_strength (int).
```

---

## V-03: Lifecycle Emphasis -- Anomaly-Heavy (Single-axis)

**Axis:** Lifecycle emphasis -- COMPILER is compressed to exactly 4 happy-path steps and
exactly 1 rejection (minimum = maximum). ANOMALY FINDER expands: each "found" anomaly requires
a full consequence chain (trigger -> corruption -> detection -> remediation). Cognitive weight
shifts from trace construction to anomaly analysis.

**Hypothesis:** R1/R2 variations give roughly equal weight to DOMAIN EXPERT, COMPILER, and
ANOMALY FINDER. The signal from trace-state is in the anomalies found, not in the length of
the trace. Compressing the trace forces the model to commit to the 4 most anomaly-exposing
transitions rather than expanding to avoid difficult analysis. The consequence chain format
forces impact reasoning in 4 structured dimensions per finding -- not a one-line description
of what breaks, but trigger, corruption, detection point, and remediation sketch. This is the
inverse of an easy-path completion, where more trace steps dilute the anomaly analysis.

```
You are running /trace-state. Fill in this structured template.
Three roles execute in sequence. Each role gate must complete before the next begins.
All table headers are fixed -- do not reorder, rename, or remove any column.
The Domain Expert's state machine is locked after its gate. COMPILER and ANOMALY FINDER are
read-only on it -- gaps become findings, not retroactive additions.

CROSS-REFERENCE DISCIPLINE: Every entity (state, operation, invariant) is declared once
and referenced everywhere by ID. An S-ID, OP-ID, or INV-ID used downstream that was not
declared in DOMAIN EXPERT is an anomaly finding, not a silent addition.

LIFECYCLE WEIGHT: COMPILER produces exactly 4 happy-path steps and exactly 1 rejection.
ANOMALY FINDER is the primary deliverable: each "found" anomaly requires a consequence chain.
The trace is evidence. The anomaly analysis is the signal.

---

## SETUP: PRIOR SIGNALS
[Search simulations/trace/ and simulations/scout/ for any prior state, request, or contract
artifacts on this topic.]
Prior signals: [List files found, or write "None -- starting fresh."]

---

## DOMAIN EXPERT: DECLARE

[Use vocabulary a Sales rep, support engineer, or finance analyst would recognize without
translation. Generic labels ("Pending", "Active", "Done") do not pass -- use the vocabulary
the domain actually uses in its systems.]

Entity: [Domain-realistic name -- the kind that appears in a CRM, helpdesk, or ERP]
Domain: [Sales / Customer Service / Finance]

State machine:
| State ID | State Name | Domain Description | Entry Condition | Terminal? |
|----------|-----------|-------------------|----------------|-----------|
| S-01 | [Name] | [What this state means to a domain practitioner] | [What must be true to enter this state] | yes / no |
| S-02 | [Name] | [What this state means to a domain practitioner] | [What must be true to enter this state] | yes / no |
[Minimum 4 rows. All S-IDs used downstream must be declared here.]

Valid transitions:
| Op ID | Operation Name | From State (S-ID) | To State (S-ID) | Domain Meaning |
|-------|---------------|------------------|----------------|----------------|
| OP-01 | [Name] | [S-ID] | [S-ID] | [Why a practitioner would trigger this operation] |
| OP-02 | [Name] | [S-ID] | [S-ID] | [Why a practitioner would trigger this operation] |
[All OP-IDs used downstream must be declared here.]

Invariants:
| INV ID | Invariant Statement | Scope (S-IDs) | Violation Consequence |
|--------|---------------------|---------------|----------------------|
| INV-01 | [Precisely stated invariant] | [S-IDs or "all states"] | [What breaks in production if violated] |
[Minimum 1 row. All INV-IDs used downstream must be declared here.]

Domain Expert gate:
[ ] Entity and domain named with domain vocabulary -- no generic placeholders
[ ] All states have S-IDs, entry conditions, and domain-language descriptions
[ ] All valid transitions declared with Op IDs before any trace steps are written
[ ] All invariants declared with INV-IDs, scope listed as S-IDs, and violation consequence
[ ] No duplicate IDs

---

## COMPILER: TRACE (minimal)

[Read-only on the Domain Expert tables. Produce exactly 4 happy-path steps and exactly
1 rejected transition. Choose the 4 steps that provide the most anomaly surface area --
transitions that cross invariant scope, contested states, or boundary conditions.
All references use declared IDs. Flag undeclared references in the log below.]

Operation trace (exactly 4 steps):
| Step | Before-State (S-ID: Name) | Operation (OP-ID: Name) | Preconditions | After-State (S-ID: Name) | Postconditions | INV Check |
|------|--------------------------|------------------------|---------------|--------------------------|----------------|-----------|
| 1 | [S-ID: Name] | [OP-ID: Name] | - [Precondition] | [S-ID: Name] | - [Postcondition] | INV-01: pass |
| 2 | [S-ID: Name] | [OP-ID: Name] | - [Precondition] | [S-ID: Name] | - [Postcondition] | INV-01: pass |
| 3 | [S-ID: Name] | [OP-ID: Name] | - [Precondition] | [S-ID: Name] | - [Postcondition] | INV-01: pass |
| 4 | [S-ID: Name] | [OP-ID: Name] | - [Precondition] | [S-ID: Name] | - [Postcondition] | INV-01: pass |

Rejected transitions (exactly 1 step):
| Step | Before-State (S-ID: Name) | Attempted Op (OP-ID or "undeclared: [name]") | Failing Precondition | Rejection Behavior | After-State |
|------|--------------------------|---------------------------------------------|--------------------|--------------------|-------------|
| 5 | [S-ID: Name] | [OP-ID or "undeclared: [name]"] | [Specific precondition not met] | [reject / error / exception] | [Same S-ID: Name] |

Undeclared reference log:
- [Type: S/OP/INV] [ID attempted] -- [why it was not declared]
[Write "None -- all references resolved to declared IDs." if no undeclared references.]

Compiler gate:
[ ] Exactly 4 happy-path steps (table has exactly 4 rows)
[ ] Exactly 1 rejected transition (table has exactly 1 row)
[ ] Every step references only declared S-IDs and OP-IDs
[ ] INV Check at every step references a declared INV-ID
[ ] Undeclared reference log is present (even if empty)

---

## ANOMALY FINDER: REVIEW

[Sweep the Compiler's trace for all five anomaly types. This section is the primary
deliverable -- allocate analysis depth here.
MINIMUM-FOUND REQUIREMENT: At least 2 of the first 4 rows must have verdict = "found".
Each "found" row requires a consequence chain (see format below).
All findings must reference their triggering OP-ID, S-ID, and INV-ID (if applicable).
Blank ID in any "found" row is a cross-reference gap -- write "N/A: [reason]" instead.
Do not fabricate findings. If genuinely insufficient, write "Trace insufficient: [reason]".]

Anomaly sweep:
| Anomaly Type | Verdict | OP-ID + S-ID | INV-ID | Production Consequence |
|-------------|---------|-------------|--------|----------------------|
| Invalid transition | found / none | [OP-ID at S-ID, or --] | -- | [Consequence, or --] |
| Missing precondition check | found / none | [OP-ID at S-ID, or --] | -- | [Consequence, or --] |
| Invariant violation | found / none | [OP-ID at S-ID, or --] | [INV-ID, or --] | [Consequence, or --] |
| Race condition | found / none | [OP-A + OP-B at S-ID, or --] | [INV-ID, or --] | [Consequence, or --] |
| Undeclared reference | found / none | [ID attempted, or --] | -- | [Scope creep / silent drift, or --] |

Minimum-found check:
[ ] At least 2 of the first 4 rows have verdict = "found"
[ ] Each "found" verdict cites declared IDs
[ ] No blank ID cells in any "found" row (use "N/A: [reason]" if genuinely inapplicable)

Consequence chains (complete for every "found" row):
[One block per finding. Label each block with A-ID and anomaly type.]

A-[N]: [Anomaly Type] -- [OP-ID at S-ID]
  Trigger:     [What operation + state combination causes this anomaly]
  Corruption:  [What state field or invariant is corrupted; which S-ID is affected]
  Detection:   [Where in production this would first be detected -- at API boundary, in logs,
               by the downstream operation, by a constraint]
  Remediation: [What specific change would prevent or detect this -- guard clause, schema
               constraint, idempotency key, optimistic lock, etc.]

Race condition detail (complete if verdict = found):
  Concurrent ops:  [OP-A (OP-ID)] and [OP-B (OP-ID)] on entity in state [S-ID: Name]
  Interleave:      [Which reads and writes happen in what order, and where they conflict]
  Resolution:      [Which operation wins, or how conflict is detected; entity final state]

Anomaly register:
| A-ID | Type | OP-ID | S-ID | INV-ID | Description | Severity |
|------|------|-------|------|--------|-------------|---------|
| A-01 | [type] | [OP-ID or N/A: [reason]] | [S-ID] | [INV-ID or N/A: [reason]] | [Specific description] | HIGH / MEDIUM / LOW |
[Minimum 2 rows. Blank ID in any row is a cross-reference gap.]

---

Write artifact: simulations/trace/state/{topic}-state-{date}.md
Frontmatter: skill, topic, date, domain, entity, state_count, operation_count, anomaly_count,
             anomaly_types (list), invariant_count, race_condition_analyzed (true/false),
             rejected_transitions (count), anomaly_types_found (count),
             undeclared_references (count), consequence_chains_written (count).
```

---

## V-04: Pre-Sweep + Consequence Chains (Combination: V-01 axes + V-03 axes)

**Axes:** Role sequence (pre-sweep prediction before trace) + lifecycle emphasis (compressed
trace, consequence chain per finding). Three mechanisms at three phases reinforce each other.

**Hypothesis:** V-01's pre-sweep forces structural analysis before execution evidence is available.
V-03's compressed trace forces commitment to the 4 most informative steps rather than expanding
away from difficult analysis. V-03's consequence chains force deep impact analysis per finding.
Together: the model must predict risk -> choose high-signal steps -> explain impact. Each phase
primes the next. Expected cost: cognitive overhead distributes attention across more requirements.
Expected gain: prediction accuracy and consequence depth compound. This is the highest-rigor R3
variation -- the R3 equivalent of R2's V-04.

```
You are running /trace-state. Fill in this structured template.
Four sections execute in sequence. Each gate must complete before the next begins.
All table headers are fixed -- do not reorder, rename, or remove any column.
The Domain Expert's state machine is locked after its gate. All downstream sections are
read-only on it -- gaps become findings, not retroactive additions.

CROSS-REFERENCE DISCIPLINE: Every entity (state, operation, invariant) is declared once
and referenced everywhere by ID. An S-ID, OP-ID, or INV-ID used downstream that was not
declared in DOMAIN EXPERT is an anomaly finding, not a silent addition.

ROLE SEQUENCE: DOMAIN EXPERT -> PRE-SWEEP -> COMPILER (minimal) -> ANOMALY FINDER
PRE-SWEEP reads only Domain Expert tables and predicts structural risk before the trace runs.
COMPILER produces exactly 4 happy-path steps and 1 rejection, chosen for anomaly surface area.
ANOMALY FINDER is the primary deliverable: sweep + consequence chains per finding + prediction
reconciliation.

---

## SETUP: PRIOR SIGNALS
[Search simulations/trace/ and simulations/scout/ for any prior state, request, or contract
artifacts on this topic.]
Prior signals: [List files found, or write "None -- starting fresh."]

---

## DOMAIN EXPERT: DECLARE

[Use vocabulary a Sales rep, support engineer, or finance analyst would recognize without
translation. Generic labels ("Pending", "Active", "Done") do not pass -- use the vocabulary
the domain actually uses in its systems.]

Entity: [Domain-realistic name -- the kind that appears in a CRM, helpdesk, or ERP]
Domain: [Sales / Customer Service / Finance]

State machine:
| State ID | State Name | Domain Description | Entry Condition | Terminal? |
|----------|-----------|-------------------|----------------|-----------|
| S-01 | [Name] | [What this state means to a domain practitioner] | [What must be true to enter this state] | yes / no |
| S-02 | [Name] | [What this state means to a domain practitioner] | [What must be true to enter this state] | yes / no |
[Minimum 4 rows. All S-IDs used downstream must be declared here.]

Valid transitions:
| Op ID | Operation Name | From State (S-ID) | To State (S-ID) | Domain Meaning |
|-------|---------------|------------------|----------------|----------------|
| OP-01 | [Name] | [S-ID] | [S-ID] | [Why a practitioner would trigger this operation] |
| OP-02 | [Name] | [S-ID] | [S-ID] | [Why a practitioner would trigger this operation] |
[All OP-IDs used downstream must be declared here.]

Invariants:
| INV ID | Invariant Statement | Scope (S-IDs) | Violation Consequence |
|--------|---------------------|---------------|----------------------|
| INV-01 | [Precisely stated invariant] | [S-IDs or "all states"] | [What breaks in production if violated] |
[Minimum 1 row. All INV-IDs used downstream must be declared here.]

Domain Expert gate:
[ ] Entity and domain named with domain vocabulary -- no generic placeholders
[ ] All states have S-IDs, entry conditions, and domain-language descriptions
[ ] All valid transitions declared with Op IDs before any trace steps are written
[ ] All invariants declared with INV-IDs, scope listed as S-IDs, and violation consequence
[ ] No duplicate IDs

---

## PRE-SWEEP: HYPOTHESIS

[Read ONLY the Domain Expert tables. The Compiler trace has not been written yet.
Predict which anomaly types are structurally likely from the state machine alone.
Reference specific S-IDs, OP-IDs, and INV-IDs. This prediction will be compared to
actual findings. Use it to inform your step selection in the Compiler trace.]

Hypothesis table:
| Anomaly Type | Likely? | Structural Reasoning | At-Risk IDs |
|-------------|---------|----------------------|-------------|
| Invalid transition | yes / no / unclear | [Specific reasoning from the transition table -- which transitions look dangerous] | [OP-IDs + S-IDs, or --] |
| Missing precondition check | yes / no / unclear | [Which transitions appear under-guarded at the system boundary] | [OP-IDs + S-IDs, or --] |
| Invariant violation | yes / no / unclear | [Which invariant scope + transition combinations could produce a violation] | [INV-IDs + OP-IDs, or --] |
| Race condition | yes / no / unclear | [Whether shared-state operations exist that could interleave] | [OP-IDs + S-IDs, or --] |
| Undeclared reference | yes / no / unclear | [Whether the transition table appears complete or has visible gaps] | [Suspicious IDs, or --] |

Pre-sweep gate:
[ ] All 5 rows completed with verdict and specific ID-referenced reasoning
[ ] At least 1 row predicts "yes"
[ ] Reasoning references declared IDs, not generic statements

---

## COMPILER: TRACE (minimal)

[Read-only on the Domain Expert tables. Produce exactly 4 happy-path steps and exactly
1 rejected transition. Choose steps that give maximum anomaly surface area for ANOMALY FINDER:
transitions that cross invariant scope, touch states predicted as at-risk, or test boundary
conditions. All references use declared IDs. Flag undeclared references in the log below.]

Operation trace (exactly 4 steps):
| Step | Before-State (S-ID: Name) | Operation (OP-ID: Name) | Preconditions | After-State (S-ID: Name) | Postconditions | INV Check |
|------|--------------------------|------------------------|---------------|--------------------------|----------------|-----------|
| 1 | [S-ID: Name] | [OP-ID: Name] | - [Precondition] | [S-ID: Name] | - [Postcondition] | INV-01: pass |
| 2 | [S-ID: Name] | [OP-ID: Name] | - [Precondition] | [S-ID: Name] | - [Postcondition] | INV-01: pass |
| 3 | [S-ID: Name] | [OP-ID: Name] | - [Precondition] | [S-ID: Name] | - [Postcondition] | INV-01: pass |
| 4 | [S-ID: Name] | [OP-ID: Name] | - [Precondition] | [S-ID: Name] | - [Postcondition] | INV-01: pass |

Rejected transitions (exactly 1 step):
| Step | Before-State (S-ID: Name) | Attempted Op (OP-ID or "undeclared: [name]") | Failing Precondition | Rejection Behavior | After-State |
|------|--------------------------|---------------------------------------------|--------------------|--------------------|-------------|
| 5 | [S-ID: Name] | [OP-ID or "undeclared: [name]"] | [Specific precondition not met] | [reject / error / exception] | [Same S-ID: Name] |

Undeclared reference log:
- [Type: S/OP/INV] [ID attempted] -- [why it was not declared]
[Write "None -- all references resolved to declared IDs." if no undeclared references.]

Compiler gate:
[ ] Exactly 4 happy-path steps
[ ] Exactly 1 rejected transition
[ ] Every step references only declared S-IDs and OP-IDs
[ ] INV Check at every step references a declared INV-ID
[ ] Undeclared reference log is present (even if empty)

---

## ANOMALY FINDER: REVIEW

[This section is the primary deliverable. Sweep the Compiler's trace for all five anomaly
types. Compare actual findings to your Pre-Sweep predictions.
MINIMUM-FOUND REQUIREMENT: At least 2 of the first 4 rows must have verdict = "found".
Each "found" row requires a consequence chain.
All findings must reference their triggering OP-ID, S-ID, and INV-ID (if applicable).
Blank ID in any "found" row is a cross-reference gap -- write "N/A: [reason]" instead.
Do not fabricate findings. If genuinely insufficient, write "Trace insufficient: [reason]".]

Anomaly sweep:
| Anomaly Type | Verdict | OP-ID + S-ID | INV-ID | Production Consequence | Predicted? |
|-------------|---------|-------------|--------|----------------------|------------|
| Invalid transition | found / none | [OP-ID at S-ID, or --] | -- | [Consequence, or --] | yes / no |
| Missing precondition check | found / none | [OP-ID at S-ID, or --] | -- | [Consequence, or --] | yes / no |
| Invariant violation | found / none | [OP-ID at S-ID, or --] | [INV-ID, or --] | [Consequence, or --] | yes / no |
| Race condition | found / none | [OP-A + OP-B at S-ID, or --] | [INV-ID, or --] | [Consequence, or --] | yes / no |
| Undeclared reference | found / none | [ID attempted, or --] | -- | [Scope creep / silent drift, or --] | yes / no |

Minimum-found check:
[ ] At least 2 of first 4 rows have verdict = "found"
[ ] Each "found" verdict cites declared IDs
[ ] No blank ID cells in any "found" row (use "N/A: [reason]" if genuinely inapplicable)

Consequence chains (complete for every "found" row):

A-[N]: [Anomaly Type] -- [OP-ID at S-ID]
  Trigger:     [What operation + state combination causes this anomaly]
  Corruption:  [What state field or invariant is corrupted; which S-ID is affected]
  Detection:   [Where in production this would first be detected]
  Remediation: [What specific change would prevent or detect this]

Race condition detail (complete if verdict = found):
  Concurrent ops:  [OP-A (OP-ID)] and [OP-B (OP-ID)] on entity in state [S-ID: Name]
  Interleave:      [Which reads and writes happen in what order, and where they conflict]
  Resolution:      [Which operation wins, or how conflict is detected; entity final state]

Prediction reconciliation:
[For each predicted "yes" that returned "none": why was the prediction wrong?]
[For each unpredicted "found": what structural signal was missed in pre-sweep?]
[Write "All predictions confirmed." if no discrepancies.]

Anomaly register:
| A-ID | Type | OP-ID | S-ID | INV-ID | Description | Severity |
|------|------|-------|------|--------|-------------|---------|
| A-01 | [type] | [OP-ID or N/A: [reason]] | [S-ID] | [INV-ID or N/A: [reason]] | [Specific description] | HIGH / MEDIUM / LOW |
[Minimum 2 rows. Blank ID in any row is a cross-reference gap.]

---

Write artifact: simulations/trace/state/{topic}-state-{date}.md
Frontmatter: skill, topic, date, domain, entity, state_count, operation_count, anomaly_count,
             anomaly_types (list), invariant_count, race_condition_analyzed (true/false),
             rejected_transitions (count), anomaly_types_found (count),
             undeclared_references (count), consequence_chains_written (count),
             predictions_accurate (count/total).
```

---

## V-05: Phrasing Register + Inertia Framing (Combination)

**Axes:** Phrasing register (conversational second-person throughout) + inertia framing
(explicit statement at the opening of what this skill replaces and why the alternative is
worse). All structural requirements from R2 V-04 (C-14/C-15/C-16/C-17) are preserved.

**Hypothesis:** All R1/R2 variations use formal third-person imperative ("The Domain Expert's
state machine is locked after its gate"). This variation uses second-person throughout ("You
are the Domain Expert. Your tables are locked once you finish this section."). Inertia framing
names what teams do without this skill -- ship state logic without a trace -- and names the
failure modes that follow. Testing whether register and framing affect output depth or are
neutral. Second-person may lower the sense of formality and invite shallow completion; or it
may increase ownership and raise specificity. Inertia framing may anchor model behavior by
making the "why" of each role concrete; or it may be ignored. Either result is informative.

```
You are running /trace-state.

Before you build anything, consider what this skill replaces. A team that skips state
tracing commits logic without a trace: invalid transitions ship as edge cases, missing
precondition checks surface in customer tickets, race conditions appear in production
at scale. This skill converts that unknown into a structured, auditable signal before
the commit. That is the only goal of this output.

Fill in the template below. Three roles run in sequence. Complete each gate before moving
to the next. Reference everything by declared ID -- any state, operation, or invariant used
without prior declaration is itself an anomaly finding, not a retroactive addition.

---

## SETUP: PRIOR SIGNALS
Before you start, check for existing context on this topic.
[Search simulations/trace/ and simulations/scout/ for prior artifacts.]
Prior signals: [List files found, or write "None -- starting fresh."]

---

## DOMAIN EXPERT: DECLARE

You are the domain expert. Your vocabulary comes from a real CRM, helpdesk, or ERP -- not
from a whiteboard or architecture diagram. Before you write a state name, ask: would a Sales
rep, support engineer, or finance analyst recognize this label in the status field they look
at every day?

Generic labels ("Pending", "Active", "Done") do not pass. Use the vocabulary the domain
puts in status fields and audit logs.

Your state machine is locked once you complete this section. The Compiler and Anomaly Finder
will read it but cannot modify it. Any gap they find is a finding, not a correction.

Entity: [Domain-realistic name -- the kind that appears in production systems]
Domain: [Sales / Customer Service / Finance]

State machine:
[Entry Condition is not how you got here -- it is what must be true right now for the entity
to legitimately be in this state. "Record exists" does not pass.]
| State ID | State Name | Domain Description | Entry Condition | Terminal? |
|----------|-----------|-------------------|----------------|-----------|
| S-01 | [Name] | [What a practitioner understands this state to mean] | [What must be true to be in this state] | yes / no |
| S-02 | [Name] | [What a practitioner understands this state to mean] | [What must be true to be in this state] | yes / no |
[Minimum 4 rows.]

Valid transitions:
[Every operation you trace later must be declared here first with an Op ID. If you reference
an operation that is not in this table, that is a finding -- not a late addition.]
| Op ID | Operation Name | From State (S-ID) | To State (S-ID) | Domain Meaning |
|-------|---------------|------------------|----------------|----------------|
| OP-01 | [Name] | [S-ID] | [S-ID] | [Why a practitioner triggers this] |
| OP-02 | [Name] | [S-ID] | [S-ID] | [Why a practitioner triggers this] |

Invariants:
[State at least one thing that must always be true. Be specific about which states it
applies to and what happens in production if it is violated.]
| INV ID | Invariant Statement | Scope (S-IDs) | Violation Consequence |
|--------|---------------------|---------------|----------------------|
| INV-01 | [Precisely stated invariant] | [S-IDs or "all states"] | [Production consequence if violated] |
[Minimum 1 row.]

Your gate -- before moving on, confirm:
[ ] Entity name is domain-specific, not a category label
[ ] Every state has a non-trivial entry condition
[ ] All operations you will trace are declared with Op IDs
[ ] At least one invariant is declared with scope and violation consequence
[ ] No duplicate IDs anywhere in this section

---

## COMPILER: TRACE

You are now the Compiler. Your job is mechanical: take the state machine above and trace
it step by step. You cannot add new states or operations -- if you need something that was
not declared, note it in the undeclared reference log and keep going. The Anomaly Finder
will deal with it.

Reference every state by S-ID and every operation by OP-ID. The INV Check column is not
optional: fill in "INV-ID: pass" or "INV-ID: VIOLATION -- [reason]" at every step.

Operation trace:
| Step | Before-State (S-ID: Name) | Operation (OP-ID: Name) | Preconditions | After-State (S-ID: Name) | Postconditions | INV Check |
|------|--------------------------|------------------------|---------------|--------------------------|----------------|-----------|
| 1 | [S-ID: Name] | [OP-ID: Name] | - [Precondition] | [S-ID: Name] | - [Postcondition] | INV-01: pass |
| 2 | [S-ID: Name] | [OP-ID: Name] | - [Precondition] | [S-ID: Name] | - [Postcondition] | INV-01: pass |
[Minimum 4 happy-path steps.]

Now trace at least one rejected transition -- an operation someone attempts but the system
should refuse. What specific precondition fails? What does the system do? Does the state
change? (It should not.)

Rejected transitions:
| Step | Before-State (S-ID: Name) | Attempted Op (OP-ID or "undeclared: [name]") | Failing Precondition | Rejection Behavior | After-State |
|------|--------------------------|---------------------------------------------|--------------------|--------------------|-------------|
| [N] | [S-ID: Name] | [OP-ID or "undeclared: [name]"] | [Specific precondition not met] | [reject / error / exception] | [Same S-ID: Name] |
[Minimum 1 row.]

If you referenced anything that was not declared above, log it here:
Undeclared reference log:
- [Type: S/OP/INV] [ID attempted] -- [why it was not in the declaration]
[Write "None -- all references resolved to declared IDs." if clean.]

Your gate:
[ ] Every step uses declared S-IDs and OP-IDs
[ ] INV Check column filled at every step with a declared INV-ID
[ ] At least 1 rejected transition
[ ] Undeclared reference log is present

---

## ANOMALY FINDER: REVIEW

You are now the Anomaly Finder. The trace above is evidence. Your job is to find what is
wrong with the state machine -- not what the trace did correctly, but what it reveals about
the gaps in the design.

There is no credit for a clean sweep. A trace that surfaces zero anomalies is a trace that
was not challenging enough -- the domain always has at least two anomaly types if you look.
At least 2 of the first 4 anomaly types must return a "found" verdict. If you genuinely
believe the domain only yields one, the trace needs to be enriched first: write
"Trace insufficient: [reason]" and stop.

Do not fabricate findings. Every "found" row must reference a real trace step by OP-ID,
S-ID, and (if applicable) INV-ID. Blank cells in a "found" row are gaps, not acceptable
blanks -- write "N/A: [reason]" if an ID genuinely does not apply.

Anomaly sweep:
| Anomaly Type | Verdict | OP-ID + S-ID | INV-ID | Production Consequence |
|-------------|---------|-------------|--------|----------------------|
| Invalid transition | found / none | [OP-ID at S-ID, or --] | -- | [What breaks in production, or --] |
| Missing precondition check | found / none | [OP-ID at S-ID, or --] | -- | [What breaks in production, or --] |
| Invariant violation | found / none | [OP-ID at S-ID, or --] | [INV-ID, or --] | [What breaks in production, or --] |
| Race condition | found / none | [OP-A + OP-B at S-ID, or --] | [INV-ID, or --] | [What breaks in production, or --] |
| Undeclared reference | found / none | [ID attempted, or --] | -- | [Silent drift / scope creep, or --] |

Your minimum-found check:
[ ] At least 2 of the first 4 rows have verdict = "found"
[ ] Each "found" verdict cites declared IDs
[ ] No blank cells in any "found" row (use "N/A: [reason]" instead)

If you found a race condition, trace the interleave in detail:
  Concurrent ops:  [OP-A (OP-ID)] and [OP-B (OP-ID)], both operating on entity in state [S-ID: Name]
  Interleave:      [Step-by-step: who reads what, who writes what, where they conflict]
  Resolution:      [Which wins, or how the system detects and resolves the conflict]

Log every finding:
| A-ID | Type | OP-ID | S-ID | INV-ID | Description | Severity |
|------|------|-------|------|--------|-------------|---------|
| A-01 | [type] | [OP-ID or N/A: [reason]] | [S-ID] | [INV-ID or N/A: [reason]] | [Specific description] | HIGH / MEDIUM / LOW |
[Minimum 2 rows -- one per "found" verdict. N/A is required where an ID genuinely does not
apply; a blank cell means the column was not checked.]

---

Write artifact: simulations/trace/state/{topic}-state-{date}.md
Frontmatter: skill, topic, date, domain, entity, state_count, operation_count, anomaly_count,
             anomaly_types (list), invariant_count, race_condition_analyzed (true/false),
             rejected_transitions (count), anomaly_types_found (count),
             undeclared_references (count).
```
