Written to `simulations/quest/variations/mock-accept-variations-R2-2026-03-17.md`.

---

## mock-accept R2 — Variations (V-01 through V-05)

### Variation Summary

| ID | Primary Axis | Secondary Axis | Key C-criteria targeted |
|----|-------------|----------------|------------------------|
| **V-01** | Artifact-as-subject grammar — standing rule block at top | — | C-09, C-11, C-12, C-14 |
| **V-02** | Named blocking completeness gates — GATE A/B/C/D pattern | — | C-11, C-12 (at column rule) |
| **V-03** | Inline CONSTRAINT blocks co-located with each field | — | C-11, C-12, C-14 (blank line) |
| **V-04** | Artifact-as-subject grammar | Phase exit assertions (N+M + artifact cite) | C-09, C-11, C-12, C-13 |
| **V-05** | Blank-line failure signal (checklist) | Artifact-as-subject grammar | C-09, C-11, C-12, C-14 |

### What changed from R1

**R1 ceiling was 95** — universal C-09 failure (no variation instructed artifact-as-subject grammar). Under rubric v2, all R1 goldens would now score ~91.7 (1/6 aspirational instead of 1/2).

**R2 primary target**: C-09 appears in V-01, V-04, and V-05 as an explicit standing instruction — the artifact section must be the grammatical subject of every decision claim. This affects Slot 1 and Slot 2 templates directly, requiring the form `"The mock artifact's [ns] section supports..."` rather than `"[NS] mock coverage supports..."`.

**C-11 through C-14** are now structural baselines embedded in all five variations:
- C-11 (count gate): inventory count check in every variation, with GATE naming in V-02
- C-12 (reason-code at point of use): column rule in V-02, CONSTRAINT frame in V-03, labeled-field instruction in V-01/V-04/V-05
- C-13 (phase exit assertions): full N+M=total exit assertions in V-04; lighter in others
- C-14 (blank-line failure): `Your answer: ___` fill-in pattern in V-01 Phase 3, checklist `___` lines in V-03/V-05

**Theoretical ceiling**: V-01, V-04, and V-05 target C-09 + all four new aspirational criteria. If any passes C-09, the new maximum is 60+30+(6/6×10) = **100**.
ation logic runs in this phase. Auto-flag decisions are final.

  RULE A — EVIDENCE-HEAVY: prove, listen
    "The mock artifact's [ns] section records an EVIDENCE-HEAVY property —
    auto-flagged REAL-REQUIRED. Auto-flag is unconditional."

  RULE B — TIER-CRITICAL: flow, trace
    "The mock artifact's [ns] section records a TIER-CRITICAL property —
    auto-flagged REAL-REQUIRED. Auto-flag is unconditional."

  RULE C — COMPLIANCE: any compliance-tagged namespace
    "The mock artifact's [ns] section carries a compliance-sensitive tag —
    auto-flagged REAL-REQUIRED. Auto-flag is unconditional."

Remaining namespaces: EVALUATION-ELIGIBLE.

Completeness check: "The mock artifact yields [N] auto-flagged and [M] evaluation-eligible
namespace sections. N + M = [total]. Expected: 9."
If total ≠ 9, halt: "Completeness check failed — [total] namespace sections found, 9 required.
Missing: [list]."

---

## Phase 2 — Evaluation Panel (EVALUATION-ELIGIBLE only)

For each evaluation-eligible namespace, run roles in sequence.
A role failure closes the namespace — later roles do not run.

  ROLE A — Architect
  Required artifact citation: "The mock artifact's [ns] section [shows/lacks]
  [contract boundaries / error surfaces / state transitions] at the [level] required
  for tier-1 pre-commitment validation."

  Verdict:
    CONSISTENT-WITH-ARCHITECTURE → continue to Role B
    STRUCTURALLY-INSUFFICIENT → Decision: REAL-REQUIRED (Architect: STRUCTURALLY-INSUFFICIENT)
                                 Skip Roles B and C.

  ROLE B — Strategy (only if Role A passed)
  Required artifact citation: "The mock artifact's [ns] entry [provides/does not provide]
  adequate signals for [specific tier decision] at the [gate name] gate."

  Verdict:
    ADEQUATE FOR TIER 1 → continue to Role C
    INADEQUATE FOR TIER 1 → Decision: REAL-REQUIRED (Strategy: INADEQUATE FOR TIER 1)
                             Skip Role C.

  ROLE C — PM (only if Roles A and B passed)
  Required artifact citation: "The mock artifact's [ns] scenarios [represent/do not represent]
  the usage patterns and edge conditions required for pre-commitment validation."

  Verdict:
    REPRESENTATIVE → Decision: MOCK-ACCEPTED
    INCOMPLETE → Decision: REAL-REQUIRED (PM: INCOMPLETE)

---

## Phase 3 — Structural Slot Population (MOCK-ACCEPTED only)

For each MOCK-ACCEPTED namespace, complete all three fields.
An absent, paraphrased, or incorrectly formed field reverts the namespace to REAL-REQUIRED.

  Reason codes [write the exact token in this labeled field — no paraphrases, no invented codes,
  no prose summaries; the token must appear here or the field counts as absent]:
    STRUCTURAL-COVERAGE-SUFFICIENT   <- if structural properties are the primary basis
    DOMAIN-KNOWLEDGE-CONSISTENT      <- if domain predictability is the primary basis
    Both may apply — list each that fits.
  Your codes: _______________

  Slot 1 — SQ-1 Tier-Decision Anchor [artifact-as-subject grammar required]:
    "The mock artifact's [ns] section supports the [specific tier-1 decision name]
    determination at the [named gate] gate."
    SLOT-VIOLATION: subject is not the artifact's section, or no specific decision named.
    Violation -> revert to REAL-REQUIRED.
  Your statement: _______________

  Slot 2 — Contrast [artifact-as-subject grammar required]:
    "Unlike the mock artifact's [contrasting NS] section ([auto-flag property]),
    the [this NS] section does not record dependency on [structural factor] —
    [one-sentence reason]."
    CONTRAST-INCOMPLETE: no contrasting namespace named, or no structural factor named.
    Violation -> revert to REAL-REQUIRED.
  Your statement: _______________

---

## Phase 4 — In-Place Edit + Canary

Using the Edit tool, update simulations/mock/{topic}-mock-{date}.md.

For each namespace:
  Replace: Status: MOCK (awaiting review)
  With:    Status: [final decision]

After all edits, re-read the artifact.
Count remaining "Status: MOCK (awaiting review)" strings.

Artifact-as-subject count: "The mock artifact contains [count] Status fields still reading
MOCK (awaiting review)."

If count = 0, issue Canary:
  "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."

If count > 0, suppress Canary:
  "CANARY SUPPRESSED — the mock artifact still shows MOCK (awaiting review) in: [list]."

---

## Phase 5 — Review Artifact + Next Steps

Write: simulations/mock/{topic}-review-{date}.md

  Section 1 — Coverage Review table:
    Columns: Namespace | Category | Decision | Trigger
    Order: auto-flagged REAL-REQUIRED, evaluation REAL-REQUIRED, MOCK-ACCEPTED
    Header note: "Derived from: {topic}-mock-{date}.md"

  Section 2 — Structural records (one per MOCK-ACCEPTED namespace):
    Reason codes (labeled field) + Slot 1 (artifact-as-subject) + Slot 2 (artifact-as-subject)

  Section 3 — Cross-namespace risk (artifact-as-subject form):
    "The mock artifact's highest-risk gap is the [namespace] section: the [specific tier
    decision] determination is exposed. Urgency: [BLOCKING | HIGH | MEDIUM]."
    Select exactly one. A list without a single selection does not satisfy this requirement.

Next Steps — /{skill-id} {topic} format:

  Auto-flagged REAL-REQUIRED:
    /{skill-id} {topic} -- {namespace}: REAL-REQUIRED (AUTO-FLAG: {trigger})

  Evaluation-driven REAL-REQUIRED:
    /{skill-id} {topic} -- {namespace}: REAL-REQUIRED ({role}: {verdict})

  MOCK-ACCEPTED:
    /{skill-id} {topic} -- {namespace}: MOCK-ACCEPTED ({reason codes}), cleared
```

---

## V-02 — Single-Axis: Named Blocking Completeness Gates
**Axis**: Completeness assertions are elevated to named GATE checkpoints that produce a hard-fail output and block continuation when the count is wrong.
**Hypothesis**: Making completeness gates named, blocking, and format-identical (COMPLETENESS-GATE X pattern) forces count verification at multiple points in the workflow — not just at the end — eliminating the silent namespace omission pattern (C-11) more robustly than a single self-check.

---

```markdown
You are running /mock-accept {topic}.

## Input

Read: simulations/mock/{topic}-mock-{date}.md
Halt if not found — report missing path.

---

## COMPLETENESS-GATE A — NAMESPACE INVENTORY

Before producing any decision, count the namespaces in the artifact.

  NAMESPACE INVENTORY TABLE
  +------------+-------------------------------+
  | Namespace  | Status (from artifact)        |
  +------------+-------------------------------+
  | scout      | [Status field value]          |
  | draft      | [Status field value]          |
  | review     | [Status field value]          |
  | flow       | [Status field value]          |
  | trace      | [Status field value]          |
  | prove      | [Status field value]          |
  | listen     | [Status field value]          |
  | program    | [Status field value]          |
  | topic      | [Status field value]          |
  +------------+-------------------------------+

GATE A ASSERTION: "Inventory complete. Row count = [N]. Expected: 9."

If N != 9, halt:
  "COMPLETENESS-GATE A FAILED — [N] rows found, 9 required.
  Missing: [list namespace names]. Cannot proceed to Decision Grid."

Do not proceed until GATE A assertion is issued and passes.

---

## Step 1 — Decision Grid

Produce the Decision Grid FIRST. No prose before this table.

  DECISION GRID
  +-----------+------------------+----------------------------------------------+----------+
  | Namespace | Decision         | Reason / Trigger                             | Auto-flag|
  +-----------+------------------+----------------------------------------------+----------+
  | scout     | [decision]       | [exact code or AUTO-FLAG trigger]            | [YES/NO] |
  | draft     | [decision]       | [exact code or AUTO-FLAG trigger]            | [YES/NO] |
  | review    | [decision]       | [exact code or AUTO-FLAG trigger]            | [YES/NO] |
  | flow      | [decision]       | [exact code or AUTO-FLAG trigger]            | [YES/NO] |
  | trace     | [decision]       | [exact code or AUTO-FLAG trigger]            | [YES/NO] |
  | prove     | [decision]       | [exact code or AUTO-FLAG trigger]            | [YES/NO] |
  | listen    | [decision]       | [exact code or AUTO-FLAG trigger]            | [YES/NO] |
  | program   | [decision]       | [exact code or AUTO-FLAG trigger]            | [YES/NO] |
  | topic     | [decision]       | [exact code or AUTO-FLAG trigger]            | [YES/NO] |
  +-----------+------------------+----------------------------------------------+----------+

Rules for the Decision column:
  MOCK-ACCEPTED  -- only if NOT auto-flagged AND all three evaluation roles pass
  REAL-REQUIRED  -- if auto-flagged OR any evaluation role fails

Rules for the Reason / Trigger column [constraint -- write the exact token in this column cell,
not in prose before or after the table]:
  Auto-flagged namespaces:  write exactly one of:
    AUTO-FLAG: EVIDENCE-HEAVY  |  AUTO-FLAG: TIER-CRITICAL  |  AUTO-FLAG: COMPLIANCE
  MOCK-ACCEPTED namespaces:  write exactly one or both of:
    STRUCTURAL-COVERAGE-SUFFICIENT  |  DOMAIN-KNOWLEDGE-CONSISTENT
  No paraphrases. No invented codes. No prose summaries. Exact token required in this cell.

COMPLETENESS-GATE B — GRID INTEGRITY:
After filling the grid: "Grid contains [N] rows. Expected: 9.
Auto-flagged: [N1]. Evaluation-eligible: [N2]. N1 + N2 = [sum]. Confirmed: [YES/NO]."
If NO, return to Step 1 and correct before proceeding.

---

## Step 2 — Auto-Flag Verification

For each auto-flagged namespace (prove, listen, flow, trace, any compliance-tagged):
  "[Namespace] — REAL-REQUIRED. Auto-flag: [trigger]. Decision not subject to evaluation override."

If any auto-flagged namespace appears in the Decision Grid as MOCK-ACCEPTED:
  "AUTO-FLAG INTEGRITY FAILURE — [namespace] marked MOCK-ACCEPTED but is auto-flagged.
  Return to Step 1 and correct."

---

## Step 3 — Evaluation Panel (non-auto-flagged only)

For each non-auto-flagged namespace:

  Namespace: [name]
  Architect verdict:  [CONSISTENT-WITH-ARCHITECTURE | STRUCTURALLY-INSUFFICIENT]
  Strategy verdict:   [ADEQUATE FOR TIER 1 | INADEQUATE FOR TIER 1]
  PM verdict:         [REPRESENTATIVE | INCOMPLETE]
  Outcome:            [MOCK-ACCEPTED | REAL-REQUIRED -- driven by: [role]]

If any role fails, record the failing role and close the namespace as REAL-REQUIRED.
Later roles do not run for a failed namespace.

---

## Step 4 — Structural Slot Table (MOCK-ACCEPTED only)

For each MOCK-ACCEPTED namespace, complete BOTH slots.
A blank slot = SLOT-VIOLATION -> revert to REAL-REQUIRED.

  STRUCTURAL SLOT TABLE
  +-----------+------------------------------------------------------+------------------------------------------------------+
  | Namespace | Slot 1 -- SQ-1 Tier-Decision Anchor                  | Slot 2 -- Contrast + Structural Factor               |
  +-----------+------------------------------------------------------+------------------------------------------------------+
  | [name]    | "[NS] mock section supports the [specific tier       | "Unlike [NS2] ([property]), [this NS] does not       |
  |           |  decision] determination at the [gate] gate."        |  depend on [structural factor] -- [reason]."         |
  +-----------+------------------------------------------------------+------------------------------------------------------+

Slot 1 VIOLATION: generic adequacy statement without a named tier decision.
Slot 2 VIOLATION: contrast without naming the structural factor.

COMPLETENESS-GATE C — SLOT INTEGRITY:
After filling: "Slot table contains [N] rows. Each MOCK-ACCEPTED namespace has a row: [YES/NO].
Both slots populated in every row: [YES/NO]."
If either NO, correct before continuing.

---

## Step 5 — In-Place Edit + Canary

Using the Edit tool, update simulations/mock/{topic}-mock-{date}.md.

For each namespace, replace:
  Status: MOCK (awaiting review)
with:
  Status: [decision from Step 1 grid]

After all edits, re-read the file.
Count remaining "Status: MOCK (awaiting review)" strings.

COMPLETENESS-GATE D — EDIT VERIFICATION:
"Post-edit count: [N] Status fields still reading MOCK (awaiting review)."

If N = 0, issue Canary:
  "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."

If N > 0, suppress Canary:
  "COMPLETENESS-GATE D FAILED -- [N] fields not updated: [list namespace names]."

---

## Step 6 — Coverage Review Artifact

Write: simulations/mock/{topic}-review-{date}.md

  1. Copy of Decision Grid from Step 1 (canonical record)
  2. Copy of Structural Slot Table from Step 4
  3. Cross-namespace risk: single highest-risk gap namespace + specific tier decision at risk +
     urgency: BLOCKING | HIGH | MEDIUM
     (A list of risks without a single selection does not satisfy this requirement.)

---

## Step 7 — Next Steps

/{skill-id} {topic} format:

  Auto-flagged REAL-REQUIRED:
    /{skill-id} {topic} -- {namespace}: REAL-REQUIRED (AUTO-FLAG: {trigger})

  Evaluation-driven REAL-REQUIRED:
    /{skill-id} {topic} -- {namespace}: REAL-REQUIRED ({role}: {verdict})

  MOCK-ACCEPTED:
    /{skill-id} {topic} -- {namespace}: MOCK-ACCEPTED ({reason codes}), simulation ready
```

---

## V-03 — Single-Axis: Inline Reason-Code Constraint Blocks
**Axis**: Reason-code constraints are placed inside framed CONSTRAINT blocks co-located with the field definition — the rule and the field share a visible boundary, not separated by sections.
**Hypothesis**: Co-locating the constraint inside a framed block at the exact point where the code is written (C-12) eliminates the failure mode where the code requirement appears in preamble but is forgotten or paraphrased at the field; the visual frame makes the constraint impossible to skip.

---

```markdown
You are running /mock-accept {topic}.

## Input

Read: simulations/mock/{topic}-mock-{date}.md
If not found, halt and report the missing path.

---

## Phase 1 — Namespace Inventory

List every namespace found in the artifact:
  - [namespace]: Status: [value from artifact]
  - ...

Count check: "Inventory total = [N]. Required: 9."
If N != 9, halt: "Inventory incomplete -- [N] of 9 namespaces found. Missing: [list].
Cannot proceed."

---

## Phase 2 — Auto-Flag Classification

Classify each namespace. No evaluation reasoning in this phase.

Auto-flag rules (unconditional):
  prove, listen -> REAL-REQUIRED (AUTO-FLAG: EVIDENCE-HEAVY)
  flow, trace   -> REAL-REQUIRED (AUTO-FLAG: TIER-CRITICAL)
  Any compliance-tagged namespace -> REAL-REQUIRED (AUTO-FLAG: COMPLIANCE)

For each auto-flagged namespace:
  [Namespace]: REAL-REQUIRED -- AUTO-FLAG: [rule]
  Note: evaluation-eligible check skipped. Auto-flag is unconditional.

Remaining namespaces: EVALUATION-ELIGIBLE.

Exit check: "Auto-flagged: [N1]. Evaluation-eligible: [N2]. N1 + N2 = [total].
Matches inventory: [YES/NO]."
If NO, identify the discrepancy before continuing.

---

## Phase 3 — Evaluation Panel (EVALUATION-ELIGIBLE only)

For each evaluation-eligible namespace, run roles in sequence.
First failure closes the namespace.

  Role A -- Architect: Does the mock capture contract boundaries, error surfaces,
  and state transitions at a level sufficient for tier-1 pre-commitment validation?
    PASS -> CONSISTENT-WITH-ARCHITECTURE -> continue to Role B
    FAIL -> STRUCTURALLY-INSUFFICIENT -> REAL-REQUIRED (Architect: STRUCTURALLY-INSUFFICIENT)
            Close namespace. Skip Roles B and C.

  Role B -- Strategy (only if Role A passed):
  Does this mock give the team confidence to pass through the next tier gate?
    PASS -> ADEQUATE FOR TIER 1 -> continue to Role C
    FAIL -> INADEQUATE FOR TIER 1 -> REAL-REQUIRED (Strategy: INADEQUATE FOR TIER 1)
            Close namespace. Skip Role C.

  Role C -- PM (only if Roles A and B passed):
  Are the scenarios representative of real usage patterns and edge conditions?
    PASS -> REPRESENTATIVE -> MOCK-ACCEPTED
    FAIL -> INCOMPLETE -> REAL-REQUIRED (PM: INCOMPLETE)

---

## Phase 4 — Structural Documentation (MOCK-ACCEPTED only)

For each MOCK-ACCEPTED namespace, complete the form below.
Each field has an inline CONSTRAINT block. A field left blank, or completed in a form that
violates its CONSTRAINT, reverts the namespace to REAL-REQUIRED.

---

Namespace: _______________

  Field 1 -- Reason Codes
  +-----------------------------------------------------------------------------------+
  | CONSTRAINT: Write only from this exact list. No paraphrases. No invented codes.  |
  | No prose. The token must appear on the "Your codes" line, not buried elsewhere.  |
  | Basis is structural properties -> STRUCTURAL-COVERAGE-SUFFICIENT                 |
  | Basis is domain predictability -> DOMAIN-KNOWLEDGE-CONSISTENT                    |
  | Both may apply -- list each that fits. Absent or paraphrased = CODE-VIOLATION.  |
  +-----------------------------------------------------------------------------------+
  Your codes: _______________

  Field 2 -- Slot 1: SQ-1 Tier-Decision Anchor
  +-----------------------------------------------------------------------------------+
  | CONSTRAINT: One sentence naming a specific tier-1 decision and a named gate.     |
  | Required form: "[NS] mock coverage supports the [specific decision name]         |
  | determination at the [gate name] gate."                                           |
  | VIOLATION: generic statement without a named decision -- e.g., "supports tier-1  |
  | decision-making." Violation -> revert to REAL-REQUIRED.                           |
  +-----------------------------------------------------------------------------------+
  Your statement: _______________

  Field 3 -- Slot 2: Contrast + Structural Factor
  +-----------------------------------------------------------------------------------+
  | CONSTRAINT: Name one auto-flagged namespace and the structural factor that        |
  | distinguishes it. Required form: "Unlike [auto-flagged NS] ([property]),          |
  | [this NS] does not depend on [structural factor] -- [one-sentence reason]."       |
  | VIOLATION: no named namespace, or no structural factor named.                     |
  | CONTRAST-INCOMPLETE -> revert to REAL-REQUIRED.                                   |
  +-----------------------------------------------------------------------------------+
  Your statement: _______________

---

## Phase 5 — In-Place Edit + Canary

Using the Edit tool, update simulations/mock/{topic}-mock-{date}.md.

For each namespace:
  Replace: Status: MOCK (awaiting review)
  With:    Status: [final decision]

After all edits, re-read the file.
Count remaining "Status: MOCK (awaiting review)" occurrences.

If count = 0:
  "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."

If count > 0, suppress Canary:
  "CANARY SUPPRESSED -- [count] fields not updated: [list namespace names]."

---

## Phase 6 — Review Artifact

Write: simulations/mock/{topic}-review-{date}.md

  1. Coverage Review table: Namespace | Category | Decision | Trigger
     Order: auto-flagged REAL-REQUIRED -> evaluation REAL-REQUIRED -> MOCK-ACCEPTED

  2. Structural records per MOCK-ACCEPTED namespace (Fields 1-3 from Phase 4 verbatim)

  3. Cross-namespace risk:
     Single highest-risk gap: name the namespace, the specific tier decision at risk,
     urgency: BLOCKING | HIGH | MEDIUM.
     Select exactly one. A list does not satisfy this requirement.

---

## Phase 7 — Next Steps

/{skill-id} {topic} format:

  Auto-flagged REAL-REQUIRED:
    /{skill-id} {topic} -- {namespace}: REAL-REQUIRED (AUTO-FLAG: {trigger})

  Evaluation-driven REAL-REQUIRED:
    /{skill-id} {topic} -- {namespace}: REAL-REQUIRED ({role}: {verdict})

  MOCK-ACCEPTED:
    /{skill-id} {topic} -- {namespace}: MOCK-ACCEPTED ({reason codes}), simulation ready
```

---

## V-04 — Combination: Artifact-as-Subject + Phase Exit Assertions
**Axes**: Artifact-as-subject grammar (C-09) combined with explicit named phase entry/exit assertions (C-13).
**Hypothesis**: Grounding every phase transition in artifact-sourced evidence (C-09) AND requiring named exit assertions before each phase (C-13) creates the tightest evaluation chain — each assertion is both a count gate and an artifact citation, preventing phase collapse and rationalized reasoning simultaneously.

---

```markdown
You are running /mock-accept {topic}.

## Artifact-as-Subject Rule

Throughout this skill, the artifact is the grammatical subject of every decision statement.

  PASS: "The mock artifact's [namespace] section [shows/records/lacks] [evidence]."
  FAIL: "I found..." / "This namespace has..." / "The evaluation shows..."

Every claim about namespace coverage must cite the artifact section as the source.
Applies to: all phase outputs, exit assertions, Slot 1, Slot 2, Canary, review artifact.

---

## PHASE 0 -- LOCATE AND READ

Entry condition: skill invoked with {topic}.
Exit assertion: working set established from artifact.

Read: simulations/mock/{topic}-mock-{date}.md
If not found, halt: "BLOCKED -- {topic}-mock-{date}.md not found. Run /mock {topic} first."

After reading, list each namespace found in the artifact:
  The mock artifact contains the following namespace sections:
  - [namespace]: Status: [value]
  - ...

PHASE 0 EXIT ASSERTION: "The mock artifact contains [N] namespace sections. Working set
confirmed. Expected: 9. Match: [YES/NO]."
If NO, halt: "Working set mismatch -- [N] sections found, 9 expected. Missing: [list]."

Do not proceed to Phase 1 until Phase 0 exit assertion is written.

---

## PHASE 1 -- AUTO-FLAG CLASSIFICATION

Entry condition: Phase 0 exit assertion written.
Exit assertion: every namespace classified, N + M = total confirmed.
No evaluation logic runs in this phase.

  Rule A -- EVIDENCE-HEAVY: prove, listen
    "The mock artifact's [ns] section records an EVIDENCE-HEAVY property --
    auto-flagged REAL-REQUIRED. Auto-flag is unconditional."

  Rule B -- TIER-CRITICAL: flow, trace
    "The mock artifact's [ns] section records a TIER-CRITICAL property --
    auto-flagged REAL-REQUIRED. Auto-flag is unconditional."

  Rule C -- COMPLIANCE: any compliance-tagged namespace
    "The mock artifact's [ns] section carries a compliance-sensitive tag --
    auto-flagged REAL-REQUIRED. Auto-flag is unconditional."

All remaining namespaces: EVALUATION-ELIGIBLE.

PHASE 1 EXIT ASSERTION: "The mock artifact yields [N] AUTO-FLAGGED namespace sections and
[M] EVALUATION-ELIGIBLE namespace sections. N + M = [total]. Expected: 9.
Phase 1 complete."
If total != 9, do not proceed -- identify the discrepancy.

Do not proceed to Phase 2 until Phase 1 exit assertion is written.

---

## PHASE 2 -- ROLE-SEQUENCED EVALUATION (EVALUATION-ELIGIBLE ONLY)

Entry condition: Phase 1 exit assertion written.
Exit assertion: every EVALUATION-ELIGIBLE namespace has a final decision with artifact citation.

For each evaluation-eligible namespace, run roles in sequence.
A role failure closes the namespace -- later roles do not run.

  ROLE A -- Architect
  Required artifact citation: "The mock artifact's [ns] section [shows/lacks]
  [contract boundaries / error surfaces / state transitions] at the [level] required
  for tier-1 pre-commitment validation."

  Verdict:
    CONSISTENT-WITH-ARCHITECTURE -> continue to Role B
    STRUCTURALLY-INSUFFICIENT -> Decision: REAL-REQUIRED (Architect: STRUCTURALLY-INSUFFICIENT)
                                  Skip Roles B and C.

  ROLE B -- Strategy (only if Role A passed)
  Required artifact citation: "The mock artifact's [ns] entry [provides/does not provide]
  adequate signals for [specific tier decision] at the [gate name] gate."

  Verdict:
    ADEQUATE FOR TIER 1 -> continue to Role C
    INADEQUATE FOR TIER 1 -> Decision: REAL-REQUIRED (Strategy: INADEQUATE FOR TIER 1)
                              Skip Role C.

  ROLE C -- PM (only if Roles A and B passed)
  Required artifact citation: "The mock artifact's [ns] scenarios [represent/do not represent]
  the usage patterns and edge conditions required for pre-commitment validation."

  Verdict:
    REPRESENTATIVE -> Decision: MOCK-ACCEPTED
    INCOMPLETE -> Decision: REAL-REQUIRED (PM: INCOMPLETE)

PHASE 2 EXIT ASSERTION: "The mock artifact yields [M] EVALUATION-ELIGIBLE sections: [X]
MOCK-ACCEPTED, [Y] REAL-REQUIRED (evaluation). X + Y = M. Phase 2 complete."

Do not proceed to Phase 3 until Phase 2 exit assertion is written.

---

## PHASE 3 -- STRUCTURAL SLOT POPULATION (MOCK-ACCEPTED ONLY)

Entry condition: Phase 2 exit assertion written.
Exit assertion: every MOCK-ACCEPTED namespace has all fields confirmed, or decision reverted.

For each MOCK-ACCEPTED namespace:

  Reason codes [write the exact token in this labeled field -- no paraphrases, no invented
  codes, no prose; token must appear in the labeled field or it is absent]:
    STRUCTURAL-COVERAGE-SUFFICIENT   <- if structural coverage is the primary basis
    DOMAIN-KNOWLEDGE-CONSISTENT      <- if domain predictability is the primary basis
    Both may apply.
    Absent or paraphrased token = REASON-CODE-VIOLATION -> revert to REAL-REQUIRED.

  Slot 1 -- SQ-1 Tier-Decision Anchor [artifact-as-subject grammar required]:
    "The mock artifact's [ns] section supports the [specific tier-1 decision name]
    determination at the [named gate] gate."
    SLOT-VIOLATION: subject is not the artifact's section, or no specific decision named.
    Violation -> revert to REAL-REQUIRED.

  Slot 2 -- Contrast [artifact-as-subject grammar required]:
    "Unlike the mock artifact's [contrasting NS] section ([auto-flag property]),
    the [this NS] section does not record dependency on [structural factor] --
    [one-sentence reason]."
    CONTRAST-INCOMPLETE: no contrasting namespace named, or no structural factor named.
    Violation -> revert to REAL-REQUIRED.

PHASE 3 EXIT ASSERTION: "[X] MOCK-ACCEPTED namespace sections have all fields confirmed
(artifact-as-subject). [Z] reverted to REAL-REQUIRED (field violation). X + Z = [original
MOCK-ACCEPTED count from Phase 2]. Phase 3 complete."

Do not proceed to Phase 4 until Phase 3 exit assertion is written.

---

## PHASE 4 -- IN-PLACE EDIT + CANARY

Entry condition: Phase 3 exit assertion written.
Exit assertion: Canary issued or suppressed.

Using the Edit tool, update simulations/mock/{topic}-mock-{date}.md.

For each namespace:
  Replace: Status: MOCK (awaiting review)
  With:    Status: [final decision from Phase 2 or Phase 3]

After all edits, re-read the artifact.
Count "Status: MOCK (awaiting review)" occurrences.

Artifact-as-subject count: "The mock artifact contains [count] Status fields still reading
MOCK (awaiting review)."

If count = 0, issue Canary:
  "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."

If count > 0, suppress Canary:
  "CANARY SUPPRESSED -- the mock artifact still shows MOCK (awaiting review) in: [list]."

Phase 4 exit assertion is the Canary line itself (or suppression notice).

Do not proceed to Phase 5 until Phase 4 exit assertion is written.

---

## PHASE 5 -- REVIEW ARTIFACT + NEXT STEPS

Entry condition: Phase 4 exit assertion written.

Write: simulations/mock/{topic}-review-{date}.md

  Section 1 -- Coverage Review table:
    Columns: Namespace | Category | Decision | Trigger
    Order: AUTO-FLAGGED first, evaluation REAL-REQUIRED second, MOCK-ACCEPTED last
    Header note: "Source: {topic}-mock-{date}.md"

  Section 2 -- Structural records (one per MOCK-ACCEPTED namespace):
    Reason codes (labeled field) + Slot 1 (artifact-as-subject) + Slot 2 (artifact-as-subject)

  Section 3 -- Cross-namespace risk (artifact-as-subject form):
    "The mock artifact's highest-risk gap is the [namespace] section: the [specific tier
    decision] determination is exposed. Urgency: [BLOCKING | HIGH | MEDIUM]."
    Select exactly one namespace. A list without a single selection does not satisfy this.

Next Steps -- /{skill-id} {topic} format:

  Group 1 -- AUTO-FLAGGED REAL-REQUIRED:
    /{skill-id} {topic} -- {namespace}: REAL-REQUIRED (AUTO-FLAG: {trigger})

  Group 2 -- Evaluation-driven REAL-REQUIRED:
    /{skill-id} {topic} -- {namespace}: REAL-REQUIRED ({role}: {verdict})

  Group 3 -- MOCK-ACCEPTED:
    /{skill-id} {topic} -- {namespace}: MOCK-ACCEPTED ({reason codes}), cleared
```

---

## V-05 — Combination: Blank-Line Failure Signal + Artifact-as-Subject
**Axes**: Blank-line failure signal (C-14) combined with artifact-as-subject grammar (C-09).
**Hypothesis**: Checklist items that require artifact-grounded fill-in answers (C-09) make blank-line failures doubly visible — a blank line signals both a missing field (C-14) and an absent artifact citation (C-09). The two patterns reinforce each other: you cannot satisfy either by writing generic prose.

---

```markdown
You are running /mock-accept {topic}.

Read the mock artifact first: simulations/mock/{topic}-mock-{date}.md
Can't find it? Stop here and say so -- don't guess a path.

---

## Question 1 -- What does the artifact contain?

List every namespace section found in the artifact, using artifact-as-subject grammar:
  The mock artifact contains:
  - The [namespace] section: Status: [value]
  - The [namespace] section: Status: [value]
  ...

Count: ___  (must equal 9 -- scout, draft, review, flow, trace, prove, listen, program, topic)

If count != 9, stop: "The mock artifact contains [N] namespace sections, expected 9.
Missing: [list]. Cannot proceed."

---

## Question 2 -- Which artifact sections are auto-flagged?

Check three structural properties. Write answers in artifact-as-subject grammar.
Each answer line must name the artifact section as subject.

  Is it EVIDENCE-HEAVY?
  -> The mock artifact's prove section records EVIDENCE-HEAVY -- REAL-REQUIRED (AUTO-FLAG: EVIDENCE-HEAVY).
     The mock artifact's listen section records EVIDENCE-HEAVY -- REAL-REQUIRED (AUTO-FLAG: EVIDENCE-HEAVY).

  Is it TIER-CRITICAL?
  -> The mock artifact's flow section records TIER-CRITICAL -- REAL-REQUIRED (AUTO-FLAG: TIER-CRITICAL).
     The mock artifact's trace section records TIER-CRITICAL -- REAL-REQUIRED (AUTO-FLAG: TIER-CRITICAL).

  Is it compliance-tagged?
  -> Check the artifact. If yes: REAL-REQUIRED (AUTO-FLAG: COMPLIANCE).

Your auto-flagged list:
  - The mock artifact's [namespace] section: REAL-REQUIRED (AUTO-FLAG: ___)
  - The mock artifact's [namespace] section: REAL-REQUIRED (AUTO-FLAG: ___)
  ...

These sections are closed. Skip them in Questions 3-5.

---

## Question 3 -- Does the artifact's structural coverage hold up?

Ask the Architect for each non-auto-flagged namespace:
"Does the mock artifact's [namespace] section show contract boundaries, error surfaces,
and state transitions at a level sufficient for tier-1 validation?"

  If yes -> CONSISTENT-WITH-ARCHITECTURE -> continue to Question 4
  If no  -> STRUCTURALLY-INSUFFICIENT -> REAL-REQUIRED (Architect: STRUCTURALLY-INSUFFICIENT)
            Skip Questions 4-5 for this namespace.

---

## Question 4 -- Is the artifact section adequate for the tier gate?

Ask Strategy:
"Does the mock artifact's [namespace] entry provide adequate signals for [specific tier
decision] at the [gate name] gate?"

  If yes -> ADEQUATE FOR TIER 1 -> continue to Question 5
  If no  -> INADEQUATE FOR TIER 1 -> REAL-REQUIRED (Strategy: INADEQUATE FOR TIER 1)
            Skip Question 5.

---

## Question 5 -- Is the artifact section's coverage representative?

Ask PM:
"Do the mock artifact's [namespace] scenarios represent the usage patterns and edge conditions
the team would rely on pre-commitment?"

  If yes -> REPRESENTATIVE -> MOCK-ACCEPTED
  If no  -> INCOMPLETE -> REAL-REQUIRED (PM: INCOMPLETE)

---

## Question 6 -- For each MOCK-ACCEPTED: what's the case?

For each namespace that reached MOCK-ACCEPTED, fill in this checklist.
Write in artifact-as-subject grammar throughout.
A blank line in any item is a structural failure -- the decision reverts to REAL-REQUIRED.

---

  Namespace: _______________

  [ ] Reason code (write from the exact list only -- no paraphrasing, no invented codes):
      STRUCTURAL-COVERAGE-SUFFICIENT  |  DOMAIN-KNOWLEDGE-CONSISTENT  |  both
      Your codes: _______________
      (Blank or paraphrased = REASON-CODE-VIOLATION -> revert to REAL-REQUIRED)

  [ ] Slot 1 -- What tier-1 decision does this artifact section support?
      Write in artifact-as-subject grammar:
      "The mock artifact's [NS] section supports the [specific decision name] determination
      at the [gate name] gate."
      Your statement: _______________
      (Blank = SLOT-VIOLATION -> revert to REAL-REQUIRED)
      (Generic statement not naming a specific decision also counts as blank)
      (Statement where the artifact section is not the subject also counts as blank)

  [ ] Slot 2 -- Which auto-flagged section contrasts with this one, and why?
      Write in artifact-as-subject grammar:
      "Unlike the mock artifact's [NS] section ([property]), the [this NS] section
      does not record dependency on [structural factor] -- [one-sentence reason]."
      Your statement: _______________
      (Blank = CONTRAST-INCOMPLETE -> revert to REAL-REQUIRED)
      (Statement without a named structural factor also counts as blank)
      (Statement where the artifact section is not the subject also counts as blank)

---

## Question 7 -- Has the artifact been updated?

Using the Edit tool, replace every instance in simulations/mock/{topic}-mock-{date}.md of:
  Status: MOCK (awaiting review)
with the correct final decision for that namespace.

After editing, re-read the artifact.
Count remaining "Status: MOCK (awaiting review)" strings.

The mock artifact now contains: ___ Status fields still reading MOCK (awaiting review).

If count = 0:
  "Count: 0 Status fields remain as MOCK (awaiting review). Confirmed."

If count > 0, do not issue the Canary:
  "CANARY SUPPRESSED -- the mock artifact still shows MOCK (awaiting review) in: [list]."

---

## Question 8 -- What does the full coverage picture show?

Write the review artifact: simulations/mock/{topic}-review-{date}.md

Include:
  - Coverage Review table: Namespace | Category | Decision | Trigger
    (auto-flagged first, evaluation REAL-REQUIRED second, MOCK-ACCEPTED last)
  - The completed checklists from Question 6 (verbatim, including artifact-as-subject statements)
  - Risk call in artifact-as-subject form:
    "The mock artifact's highest-risk gap is the [namespace] section: the [specific tier
    decision] determination is exposed. Urgency: [BLOCKING | HIGH | MEDIUM]."
    Select one. A list without a single selection does not satisfy this requirement.

---

## Question 9 -- What should the team do next?

/{skill-id} {topic} format:

  Auto-flagged (do these first):
    /{skill-id} {topic} -- {namespace}: REAL-REQUIRED (AUTO-FLAG: {trigger})

  Evaluation-driven REAL-REQUIRED:
    /{skill-id} {topic} -- {namespace}: REAL-REQUIRED ({role}: {verdict})

  MOCK-ACCEPTED (cleared for simulation):
    /{skill-id} {topic} -- {namespace}: MOCK-ACCEPTED ({reason codes}), proceed to simulation
```

---

## Variation Summary

| ID   | Primary Axis                                       | Secondary Axis                            | C-09 | C-11 | C-12 | C-13 | C-14 | Hypothesis                                                                  |
|------|----------------------------------------------------|-------------------------------------------|------|------|------|------|------|-----------------------------------------------------------------------------|
| V-01 | Artifact-as-subject grammar — standing rule at top | —                                         | YES  | YES  | YES  | NO   | YES  | Every claim traces to artifact section; C-09 cracked via standing rule      |
| V-02 | Named blocking completeness gates — GATE A/B/C/D  | —                                         | NO   | YES  | YES  | NO   | NO   | Multiple named gates prevent silent omission at every workflow checkpoint   |
| V-03 | Inline CONSTRAINT blocks at point of field use     | —                                         | NO   | YES  | YES  | NO   | YES  | Frame co-location makes code violation structurally impossible to miss      |
| V-04 | Artifact-as-subject grammar                        | Phase exit assertions (N+M=total + cite)  | YES  | YES  | YES  | YES  | NO   | C-09 + C-13 combined — grounded exit assertions prevent logic interleaving  |
| V-05 | Blank-line failure signal (checklist format)       | Artifact-as-subject grammar               | YES  | YES  | YES  | NO   | YES  | C-14 + C-09 combined — blank artifact citation line is doubly visible fail  |
