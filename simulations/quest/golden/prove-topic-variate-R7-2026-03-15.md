---
skill: quest-variate
skill_target: prove-topic
round: R7
date: 2026-03-15
rubric: prove-topic-rubric-v7-2026-03-15.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [handoff_field_independence, role_field_ownership, campaign_open_schema]
  combined: [V-04, V-05]
r6_anchor: "V-05 (role_sequence + output_format + inertia_framing — satisfies C-01 through C-22)"
r7_targets: "C-23 (incumbent_defense_closed independent of co_activation_confirmed in handoff), C-24 (two blocking roles each owning one attestation field, construction-enforced)"
severity_stack_gap: >
  R6 V-05 satisfies C-01 through C-22. C-23 requires incumbent_defense_closed to be derived
  from null_tally_final — not inferred through dual_lock_fired or co_activation_confirmed. A
  variation with co_activation_confirmed in the handoff but no incumbent_defense_closed forces
  downstream to infer campaign state from the dual-lock chain (C-23 FAIL). C-24 requires each
  blocking role to declare sole ownership of its attestation field at ROLE definition time, not
  just produce the field at execution. A variation where both gate fields appear in GATE S without
  source-role ownership declarations makes C-24 instruction-enforced rather than
  construction-enforced: an auditor cannot identify the gap from the ROLE schema alone.
---

# prove-topic — Variation Round R7

Five complete, runnable skill body prompts. Each is self-contained — no diff, no cross-references.

Round 7 targets C-23 and C-24, the two new criteria in rubric v7. These criteria extend
prior-round gains from handoff presence into field independence and structural ownership:

- **C-23** addresses *how* `incumbent_defense_closed` is defined, not just whether it is present.
  R6 V-05 includes the field in the handoff (`incumbent_defense_closed: [true if all null, false
  if any found]`), satisfying the presence requirement lifted from C-21. But the field's definition
  is placed immediately after `co_activation_confirmed: [must equal dual_lock_fired]` inside the
  ATOMIC DUAL-LOCK block — a downstream consumer reading the handoff cannot confirm independence
  without tracing the derivation path backward through dual_lock_fired. C-23 requires the field to
  be computed from `null_tally_final` directly, at a step that precedes or is structurally separate
  from the dual-lock machinery, so that the derivation is visible in the field's origin — not just
  logically equivalent.

- **C-24** addresses *when* role-field ownership is declared, not just whether two fields exist.
  R6 V-05 has two blocking roles (ROLE A → `invariant_registry_confirmed`, ROLE B →
  `gate_s_cleared`) with the echo `← echoed from ROLE A` in the GATE S block. This satisfies
  C-22 (two distinct fields). But ownership is visible only by reading GATE S — not from the
  ROLE A or ROLE B headers themselves. C-24 requires each role to declare its owned field at
  definition time: `OWNED ATTESTATION FIELD: [field_name]`. An auditor reading only the ROLE
  header can identify the gap from dropping that role without reading any downstream instruction.

A variation satisfying v6 can fail both: `co_activation_confirmed` in the handoff but no
`incumbent_defense_closed` (C-23 FAIL); two roles producing two fields but neither role
declares ownership at definition time (C-24 FAIL). The v6 stack closes neither gap.

---

## Round 7 Variation Map

| Variation | Axis | Pass Type | What Changes | Criteria Targeted |
|-----------|------|-----------|--------------|-------------------|
| V-01 | handoff-field-independence | single-axis | Stage 4 adds CAMPAIGN OUTCOME block; `incumbent_defense_closed` computed from tally before DUAL-LOCK; handoff labels derivation source | C-23 |
| V-02 | role-field-ownership | single-axis | ATTESTATION MANIFEST at top; each ROLE declares OWNED FIELD; hypothesis frontmatter adds FIELD PROVENANCE MAP | C-24 |
| V-03 | campaign-open-schema | single-axis | HANDOFF SCHEMA declared at campaign open (before Stage 1); names all handoff fields with derivation sources; independence of `incumbent_defense_closed` visible before evidence runs | C-23 (from pre-commitment angle) |
| V-04 | handoff-field-independence x role-field-ownership | combination (V-01 x V-02) | Campaign Outcome block + Attestation Manifest + Role ownership declarations | C-23 and C-24 |
| V-05 | all R6 V-05 axes + V-01 + V-02 | full compound | Role sequence, table format, inertia framing (R6 V-05) + campaign outcome independence (V-01) + role ownership declarations (V-02) | C-23, C-24, and full R6 stack |

**Anchor designation (preliminary):** V-05.

**Score projections under v7 rubric:**

| Variation | C-23 | C-24 | Asp/16 | Composite | Band |
|-----------|------|------|--------|-----------|------|
| R6 V-05 (base) | PARTIAL | PARTIAL | ~14/16 | ~138/144 | Golden |
| V-01 | PASS | PARTIAL | 15/16 | ~140/144 | Golden |
| V-02 | PARTIAL | PASS | 15/16 | ~140/144 | Golden |
| V-03 | PASS | PARTIAL | 15/16 | ~140/144 | Golden |
| V-04 | PASS | PASS | 16/16 | 144/144 | Golden |
| V-05 | PASS | PASS | 16/16 | 144/144 | Golden |

All variations are Golden. V-04 and V-05 achieve maximum composite under v7.

---

## V-01 — Axis: Handoff Field Independence

**Variation axis**: Handoff field independence — `incumbent_defense_closed` is computed in a
dedicated CAMPAIGN OUTCOME sub-section at Stage 4, derived directly from `null_tally_final`
before Stage 5 begins. The field enters Stage 5 with an explicit derivation note: "from Stage 4
campaign outcome — not derived from dual_lock_fired or co_activation_confirmed." The handoff
schema reflects this with a source annotation on every field. The dual-lock block fires from the
same tally input but remains a separate mechanism — two independent consumers of the same
underlying count, not a chain where one derives the other.

**Hypothesis**: When `incumbent_defense_closed` is computed at Stage 4 in a CAMPAIGN OUTCOME
block that precedes and is structurally separate from Stage 5's ATOMIC DUAL-LOCK, the field's
independence is structurally visible: it has a declared source (null_tally_final from the
table), a computation step (Stage 4), and a note confirming it is not derived from
co_activation_confirmed. A variation that computes `incumbent_defense_closed` only inside the
DUAL-LOCK block (as a consequence of dual_lock_fired) fails C-23 because independence requires
a different structural origin, not just logical equivalence.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
Two blocking roles open the campaign. Five evidence stages follow in fixed sequence.
No step may be skipped or reordered.

---

## ROLE A — INVARIANT REGISTRY LOCK

Execute first. Lock the null counter-evidence protocol before any evidence runs.

  status_quo_comparator: [name the incumbent approach this topic must beat]

  SESSION INVARIANT A — Adversarial Reviewer:
    adversarial_reviewer_type: [role most likely to challenge the claim]
    Activation: fires if ALL three evidence stages (S2, S3, S4) return null CE.
    Status: pre-registered now. Execution at synthesis if triggered — not a new decision.

  SESSION INVARIANT B — Confidence Cap:
    ce_score_formula: CE-score = -2 if all three evidence stages null; 0 otherwise.
    Status: locked formula. Cannot be softened, overridden, or bypassed at synthesis.

  invariant_registry_confirmed: true
  registry_note: "Both invariants locked. Cannot be modified after ROLE A."

ROLE A COMPLETE. Do not begin ROLE B without invariant_registry_confirmed = true.

---

## ROLE B — SCOUT LOAD

Execute after ROLE A. Do not begin hypothesis work until this role completes.

Search: simulations/scout/**/{topic}-*.md

Record found artifacts:
  | Slug | Path | Key finding |
  |------|------|-------------|
  | [slug] | [path] | [one-line finding] |

GATE S (requires both ROLE A and ROLE B complete):
  gate_s_cleared: true                    (scout record found)
  scout_anchor: [slug]
  invariant_registry_confirmed: true      (echoed from ROLE A)

If scout not found: gate_s_cleared = false. STOP.
"GATE S FAIL — no scout record. ROLE A invariants are locked but scout prerequisite unmet."

ROLE B COMPLETE. Both prerequisites confirmed — open Stage 1.

---

## INCUMBENT-DEFENSE TABLE
(Fill one row per evidence stage as that stage runs. Do not fill forward.)

| Stage | Stage Name        | Incumbent Defense Found | Running Null Count | Obligations Active |
|-------|-------------------|-------------------------|--------------------|--------------------|
| S2    | Web Search        | [yes/no]                | [0 or 1]           | [None or A+B pending if S3+S4 null] |
| S3    | Intelligence Scan | [yes/no]                | [0-2]              | [None or A+B execute if S4 null] |
| S4    | Analysis          | [yes/no]                | [0-3]              | [None or DUAL-LOCK at synthesis] |

---

## STAGE 1 — HYPOTHESIS

Artifact: simulations/prove/{topic}/{topic}-hypothesis-{date}.md

Frontmatter:
  topic: {topic}
  date: {date}
  stage: prove-hypothesis
  scout_anchor: [from ROLE B]
  gate_s_cleared: true
  invariant_registry_confirmed: true    (distinct from gate_s_cleared — ROLE A output)
  incumbent: [from ROLE A]
  reviewer_type: [from ROLE A — pre-committed]
  ce_score_formula: CE-score = -2 if all null [from ROLE A — pre-committed]

Body:
  Claim: One testable sentence from the scout record.
  Falsification: What would disprove this?
  Why not [incumbent]?: One sentence — what does this claim provide that the incumbent can't?

Write: simulations/prove/{topic}/{topic}-hypothesis-{date}.md
Confirm: "Hypothesis written: {topic}-hypothesis-{date}.md. Advancing to Stage 2."

---

## STAGE 2 — WEB SEARCH

Artifact: simulations/prove/{topic}/{topic}-websearch-{date}.md

### Part A — Claim Evidence
External sources supporting the claim.
For each: Source, Finding, Verdict (Supports / Neutral / Contradicts).

### Part B — Incumbent Defense (MANDATORY)
Active search for evidence that [incumbent] is still adequate.
For each: Source, Finding, Type (Contradicts / Complicates / Weakens the claim).

If none after active search:
  "Stage 2 incumbent-defense search: null. Reason: [one specific reason].
   Running tally: 1 null. [Update INCUMBENT-DEFENSE TABLE row S2.]
   Both pre-committed obligations (A: reviewer, B: CE-score cap) remain pending
   until S3 and S4 complete. Pre-committed in ROLE A — not a synthesis decision."

Update INCUMBENT-DEFENSE TABLE row S2.

Write: simulations/prove/{topic}/{topic}-websearch-{date}.md
Confirm: "Artifact written: {topic}-websearch-{date}.md. S2 table row updated. Advancing to Stage 3."

---

## STAGE 3 — INTELLIGENCE SCAN

Artifact: simulations/prove/{topic}/{topic}-intelligence-{date}.md

### Part A — Internal Signals for Claim
Scan project files, prior artifacts, existing designs.
Record: Path, Signal type (supports / gap / risk), Finding.

### Part B — Incumbent Defense (MANDATORY)
Internal signals suggesting [incumbent] is adequate.
If none:
  "Stage 3 incumbent-defense scan: null. Running tally: [S2+1] null.
   [Update INCUMBENT-DEFENSE TABLE row S3.]
   A + B obligations execute at synthesis if S4 also null. Pre-committed."

Update INCUMBENT-DEFENSE TABLE row S3.

Write: simulations/prove/{topic}/{topic}-intelligence-{date}.md
Confirm: "Artifact written: {topic}-intelligence-{date}.md. S3 table row updated. Advancing to Stage 4."

---

## STAGE 4 — ANALYSIS

Artifact: simulations/prove/{topic}/{topic}-analysis-{date}.md

### Part A — Evidence Assessment
Assess signals from S2-S3 against the hypothesis.
For each: Source stage, Strength (HIGH / MEDIUM / LOW), Assessment.
Thin-evidence flag: fewer than 2 HIGH signals — flag THIN, describe the gap.

### Part B — Incumbent Defense Assessment (MANDATORY)
Assess all incumbent-defense evidence from S2 and S3. If none from either:
  "Stage 4 incumbent-defense assessment: null. Running tally: [S2+S3+1] null.
   All collection stages complete — 0 stages remain. [Update INCUMBENT-DEFENSE TABLE row S4.]
   DUAL-LOCK fires at synthesis. Both pre-committed in ROLE A — execution only."

Update INCUMBENT-DEFENSE TABLE row S4.

### CAMPAIGN OUTCOME
(Computed here from the completed table — independently of synthesis dual-lock.)

  null_tally_final: [0-3, from S4 Running Null Count above]
  incumbent_defense_closed: [true if null_tally_final = 3, false otherwise]
  derivation_source: "null_tally_final from INCUMBENT-DEFENSE TABLE — not derived from
    dual_lock_fired or co_activation_confirmed. This field is computed before Stage 5
    begins. It is independently readable at the handoff without referencing the dual-lock chain."

Write: simulations/prove/{topic}/{topic}-analysis-{date}.md
Confirm: "Artifact written: {topic}-analysis-{date}.md. S4 table row updated.
          Campaign outcome: incumbent_defense_closed = [true/false]. Advancing to Stage 5."

---

## STAGE 5 — SYNTHESIS

Artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md

Terminal stage.

### ROLE A Invariant Compliance
  reviewer_type: [confirmed from ROLE A]
  ce_score_formula: CE-score = -2 if all null [confirmed from ROLE A]
  invariant_registry_confirmed: true
Both on file: [yes / no]. If no: halt — session integrity issue.

### Campaign Outcome (from Stage 4)
  incumbent_defense_closed: [from Stage 4 CAMPAIGN OUTCOME — confirmed]
  null_tally_final: [from Stage 4]
  Independence confirmed: this field was derived at Stage 4 from null_tally_final.
  It is not derived from dual_lock_fired or co_activation_confirmed.
  Both fields in the handoff are independently readable.

### Incumbent-Defense Table (completed)
Paste filled INCUMBENT-DEFENSE TABLE here. All three rows required.

### ATOMIC DUAL-LOCK
If null_tally_final = 3 — one trigger, both locks fire simultaneously:

  dual_lock_fired: true
  co_activation_confirmed: true    (must equal dual_lock_fired)

  LOCK 1 — Reviewer Challenge (ROLE A Invariant A):
    [reviewer_type] is tasked: challenge the claim from the incumbent's position.
    Topic-story blocked until challenge addressed or explicitly deferred.

  LOCK 2 — Confidence Cap (ROLE A Invariant B):
    CE-score = -2. Ceiling: MEDIUM. HIGH not available while challenge is open.

If null_tally_final < 3: dual_lock_fired = false. co_activation_confirmed = false. CE-score = 0.

### Findings
Summary. Reference each artifact by slug: {topic}-hypothesis, {topic}-websearch,
{topic}-intelligence, {topic}-analysis.

### Incumbent Defense Register (MANDATORY)
| Stage | Source | Finding | Type |
|-------|--------|---------|------|
If all null: see DUAL-LOCK block above.

### Thin-Evidence
If Stage 4 flagged THIN: name the finding, qualify confidence.
If not: "Evidence density sufficient."

### Confidence
Level: [HIGH / MEDIUM / LOW]
CE-score applied: [0 / -2] (ROLE A Invariant B — not a synthesis decision)
If dual-lock fired: level cannot be HIGH.

### Handoff
  next: topic-story
  artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md
  confidence: [level]
  dual_lock_fired: [true / false]
  co_activation_confirmed: [must equal dual_lock_fired]
  null_tally_final: [0-3]
  incumbent_defense_closed: [from Stage 4 CAMPAIGN OUTCOME — independent of co_activation_confirmed]
  escalation_triggered: [true / false]
  escalation_reviewer: [reviewer_type or "N/A"]
  status: [Ready / Challenged — [reviewer_type] review required before topic-story]

Write: simulations/prove/{topic}/{topic}-synthesize-{date}.md
Confirm: "Evidence brief complete. Campaign outcome: incumbent_defense_closed = [true/false].
          Dual-lock: [fired / not triggered]. Co-activation: [true/false].
          Status: [Ready / Challenged]. Handoff: topic-story."
```

---

## V-02 — Axis: Role Field Ownership

**Variation axis**: Role field ownership — the campaign opens with an ATTESTATION MANIFEST that
names each blocking role's owned attestation field before any work begins. Each ROLE declares
`OWNED ATTESTATION FIELD:` at its header: ROLE A owns `invariant_registry_confirmed`, ROLE B
owns `gate_s_cleared`. Neither role may produce the other's field; no other stage may declare
or modify either field. The hypothesis frontmatter includes a FIELD PROVENANCE MAP that traces
each gate field to its source role. An auditor dropping ROLE A from the schema immediately sees
the gap — `invariant_registry_confirmed` has no other source.

**Hypothesis**: When each blocking role declares its owned field at ROLE definition time (header
level), the ownership contract is visible from the schema structure, not from the conditional
instructions inside GATE S. An auditor can read the two ROLE headers and produce the complete
attestation field inventory without reading any stage-level instruction. A variation where both
fields appear in GATE S without ROLE-level ownership declarations fails C-24 because the gap
from dropping a role is revealed only by tracing which gate field loses its source — requiring
an instruction-level read, not a schema-level read.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
Two blocking roles open the campaign. Each role owns one attestation field.
Five evidence stages follow in fixed sequence. No step may be skipped or reordered.

---

## ATTESTATION MANIFEST
(Declared at campaign open — read-only after this point.)

  ROLE A owns: invariant_registry_confirmed
    Sole structural source. No other step may declare or echo this field as original.
    Dropping ROLE A creates an auditable gap: invariant_registry_confirmed is absent.

  ROLE B owns: gate_s_cleared
    Sole structural source. No other step may declare or echo this field as original.
    Dropping ROLE B creates an auditable gap: gate_s_cleared is absent.

Both fields are required in the hypothesis frontmatter.
Absence of either field is a structural failure traceable to a dropped role.

---

## ROLE A — INVARIANT REGISTRY LOCK
OWNED ATTESTATION FIELD: invariant_registry_confirmed

Execute first. Lock the null counter-evidence protocol before any evidence runs.

  status_quo_comparator: [name the incumbent approach this topic must beat]

  SESSION INVARIANT A — Adversarial Reviewer:
    adversarial_reviewer_type: [role most likely to challenge the claim]
    Activation: fires if ALL three evidence stages (S2, S3, S4) return null CE.
    Status: pre-registered now. Execution at synthesis if triggered.

  SESSION INVARIANT B — Confidence Cap:
    ce_score_formula: CE-score = -2 if all three evidence stages null; 0 otherwise.
    Status: locked formula. Cannot be overridden at synthesis.

  invariant_registry_confirmed: true    [ROLE A's owned field — produced here only]

ROLE A COMPLETE. Output: invariant_registry_confirmed.
Do not begin ROLE B without invariant_registry_confirmed = true.

---

## ROLE B — SCOUT LOAD
OWNED ATTESTATION FIELD: gate_s_cleared

Execute after ROLE A. Do not begin hypothesis work until this role completes.

Search: simulations/scout/**/{topic}-*.md

Record found artifacts:
  | Slug | Path | Key finding |
  |------|------|-------------|
  | [slug] | [path] | [one-line finding] |

  gate_s_cleared: true              [ROLE B's owned field — produced here only]
  scout_anchor: [slug]

  GATE S — both owned fields confirmed:
    gate_s_cleared: true            (ROLE B — this role)
    invariant_registry_confirmed: true    (ROLE A — prior role, not re-declared here)
    Both fields present: proceed to Stage 1.

If scout not found: gate_s_cleared = false. STOP.
"GATE S FAIL — gate_s_cleared cannot be set. Scout prerequisite unmet."

ROLE B COMPLETE. Output: gate_s_cleared. Both attestation fields on record — open Stage 1.

---

## INCUMBENT-DEFENSE TABLE
(Fill one row per evidence stage as that stage runs. Do not fill forward.)

| Stage | Stage Name        | Incumbent Defense Found | Running Null Count | Obligations Active |
|-------|-------------------|-------------------------|--------------------|--------------------|
| S2    | Web Search        | [yes/no]                | [0 or 1]           | [None or pending if S3+S4 null] |
| S3    | Intelligence Scan | [yes/no]                | [0-2]              | [None or execute if S4 null] |
| S4    | Analysis          | [yes/no]                | [0-3]              | [None or DUAL-LOCK at synthesis] |

---

## STAGE 1 — HYPOTHESIS

Artifact: simulations/prove/{topic}/{topic}-hypothesis-{date}.md

Frontmatter:
  topic: {topic}
  date: {date}
  stage: prove-hypothesis
  scout_anchor: [from ROLE B]

  FIELD PROVENANCE MAP:
    gate_s_cleared: [ROLE B — sole source]
    invariant_registry_confirmed: [ROLE A — sole source]
  gate_s_cleared: true
  invariant_registry_confirmed: true

  incumbent: [from ROLE A]
  reviewer_type: [from ROLE A — pre-committed]
  ce_score_formula: CE-score = -2 if all null [from ROLE A — pre-committed]

Body:
  Claim: One testable sentence from the scout record.
  Falsification: What would disprove this?
  Why not [incumbent]?: One sentence — what does this claim provide that the incumbent can't?

Write: simulations/prove/{topic}/{topic}-hypothesis-{date}.md
Confirm: "Hypothesis written: {topic}-hypothesis-{date}.md. Field provenance: ROLE A +
          ROLE B both attested. Advancing to Stage 2."

---

## STAGE 2 — WEB SEARCH

Artifact: simulations/prove/{topic}/{topic}-websearch-{date}.md

### Part A — Claim Evidence
External sources supporting the claim.
For each: Source, Finding, Verdict (Supports / Neutral / Contradicts).

### Part B — Incumbent Defense (MANDATORY)
Active search for evidence that [incumbent] is still adequate.
For each: Source, Finding, Type (Contradicts / Complicates / Weakens).

If none after active search:
  "Stage 2 incumbent-defense search: null. Reason: [one specific reason].
   Running tally: 1 null. [Update INCUMBENT-DEFENSE TABLE row S2.]
   Pre-committed obligations (A + B) remain pending through S3, S4."

Update INCUMBENT-DEFENSE TABLE row S2.

Write: simulations/prove/{topic}/{topic}-websearch-{date}.md
Confirm: "Artifact written: {topic}-websearch-{date}.md. S2 row updated. Advancing to Stage 3."

---

## STAGE 3 — INTELLIGENCE SCAN

Artifact: simulations/prove/{topic}/{topic}-intelligence-{date}.md

### Part A — Internal Signals for Claim
Project files, prior artifacts, existing designs.
Record: Path, Signal type (supports / gap / risk), Finding.

### Part B — Incumbent Defense (MANDATORY)
Internal signals suggesting [incumbent] is adequate.
If none:
  "Stage 3 incumbent-defense scan: null. Running tally: [S2+1] null.
   [Update INCUMBENT-DEFENSE TABLE row S3.] Pre-committed A + B execute if S4 null."

Update INCUMBENT-DEFENSE TABLE row S3.

Write: simulations/prove/{topic}/{topic}-intelligence-{date}.md
Confirm: "Artifact written: {topic}-intelligence-{date}.md. S3 row updated. Advancing to Stage 4."

---

## STAGE 4 — ANALYSIS

Artifact: simulations/prove/{topic}/{topic}-analysis-{date}.md

### Part A — Evidence Assessment
Assess signals from S2-S3 against the hypothesis.
For each: Source stage, Strength (HIGH / MEDIUM / LOW), Assessment.
Thin-evidence flag: fewer than 2 HIGH signals — flag THIN, describe the gap.

### Part B — Incumbent Defense Assessment (MANDATORY)
Assess all incumbent-defense evidence from S2 and S3. If none:
  "Stage 4 incumbent-defense: null. Running tally: [S2+S3+1] null.
   All stages complete. [Update INCUMBENT-DEFENSE TABLE row S4.] DUAL-LOCK fires at synthesis."

Update INCUMBENT-DEFENSE TABLE row S4.

Write: simulations/prove/{topic}/{topic}-analysis-{date}.md
Confirm: "Artifact written: {topic}-analysis-{date}.md. S4 row updated.
          Thin flag: [yes/no]. Advancing to Stage 5."

---

## STAGE 5 — SYNTHESIS

Artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md

Terminal stage.

### Attestation Manifest Compliance
Confirm both ROLE-owned fields are on record:
  invariant_registry_confirmed: true    (ROLE A — source confirmed)
  gate_s_cleared: true                  (ROLE B — source confirmed)
  ce_score_formula: CE-score = -2 if all null (ROLE A Invariant B)
  reviewer_type: [confirmed from ROLE A] (ROLE A Invariant A)
Both fields present: [yes / no]. If no: halt — attestation gap.

### Incumbent-Defense Table (completed)
Paste filled INCUMBENT-DEFENSE TABLE here. All three rows required.
Running null count from S4 row: [0-3]

### CE State
  All three null: [yes / no]
  incumbent_defense_closed: [true if all null, false if any found]

### ATOMIC DUAL-LOCK
If all three null — one trigger, both locks fire simultaneously:

  dual_lock_fired: true
  co_activation_confirmed: true    (must equal dual_lock_fired)

  LOCK 1 — Reviewer Challenge (ROLE A Invariant A):
    [reviewer_type] is tasked: challenge the claim from the incumbent's position.
    Topic-story blocked until challenge addressed or explicitly deferred.

  LOCK 2 — Confidence Cap (ROLE A Invariant B):
    CE-score = -2. Ceiling: MEDIUM. HIGH not available while challenge is open.

If not all null: dual_lock_fired = false. co_activation_confirmed = false. CE-score = 0.

### Findings
Summary. Reference each artifact slug.

### Incumbent Defense Register (MANDATORY)
| Stage | Source | Finding | Type |
|-------|--------|---------|------|
If all null: see DUAL-LOCK block above.

### Thin-Evidence
If Stage 4 flagged THIN: name the finding, qualify confidence. If not: "Evidence density sufficient."

### Confidence
Level: [HIGH / MEDIUM / LOW]
CE-score applied: [0 / -2] (ROLE A Invariant B — not a synthesis decision)
If dual-lock fired: level cannot be HIGH.

### Handoff
  next: topic-story
  artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md
  confidence: [level]
  dual_lock_fired: [true / false]
  co_activation_confirmed: [must equal dual_lock_fired]
  null_tally_final: [0-3]
  incumbent_defense_closed: [true if all null, false if any found]
  escalation_triggered: [true / false]
  escalation_reviewer: [reviewer_type or "N/A"]
  status: [Ready / Challenged — [reviewer_type] review required before topic-story]

  FIELD PROVENANCE (handoff audit trail):
    invariant_registry_confirmed: [ROLE A — sole source]
    gate_s_cleared: [ROLE B — sole source]

Write: simulations/prove/{topic}/{topic}-synthesize-{date}.md
Confirm: "Evidence brief complete. Attestation: ROLE A + ROLE B.
          Dual-lock: [fired / not triggered]. Status: [Ready / Challenged]. Handoff: topic-story."
```

---

## V-03 — Axis: Campaign-Open Schema

**Variation axis**: Campaign-open handoff schema — after ROLE B completes and before Stage 1
opens, the campaign declares a HANDOFF SCHEMA block that names every field that will appear
in the final synthesis handoff and specifies its derivation source. `incumbent_defense_closed`
is declared here with source `null_tally_final` and an explicit note: "independent of
co_activation_confirmed." This makes C-23 visible as a structural commitment before any
evidence runs — not just as an outcome visible at synthesis. A downstream consumer reading the
handoff schema at campaign open can verify that two independently sourced boolean fields will
be produced, without waiting for Stage 5 to confirm it.

**Hypothesis**: When the independence of `incumbent_defense_closed` is declared at campaign-open
time (before Stage 1), the contract is front-loaded into the campaign structure itself. A
variation that only establishes the field at synthesis — placing it after `co_activation_confirmed`
inside the DUAL-LOCK block — leaves independence implicit until the last stage. Pre-declaring
the schema at campaign open makes the independence contract an invariant of the campaign design,
not an outcome of the synthesis. This is a different structural angle from V-01 (which computes
the field at Stage 4) and can be combined with either approach.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
Two blocking roles open the campaign. A handoff schema is declared before Stage 1 opens.
Five evidence stages follow in fixed sequence. No step may be skipped or reordered.

---

## ROLE A — INVARIANT REGISTRY LOCK

Execute first. Lock the null counter-evidence protocol before any evidence runs.

  status_quo_comparator: [name the incumbent approach this topic must beat]

  SESSION INVARIANT A — Adversarial Reviewer:
    adversarial_reviewer_type: [role most likely to challenge the claim]
    Activation: fires if ALL three evidence stages (S2, S3, S4) return null CE.
    Status: pre-registered now. Execution at synthesis if triggered — not a new decision.

  SESSION INVARIANT B — Confidence Cap:
    ce_score_formula: CE-score = -2 if all three evidence stages null; 0 otherwise.
    Status: locked formula. Cannot be overridden at synthesis.

  invariant_registry_confirmed: true
  registry_note: "Both invariants locked. Cannot be modified after ROLE A."

ROLE A COMPLETE. Do not begin ROLE B without invariant_registry_confirmed = true.

---

## ROLE B — SCOUT LOAD

Execute after ROLE A. Do not begin hypothesis work until this role completes.

Search: simulations/scout/**/{topic}-*.md

Record found artifacts:
  | Slug | Path | Key finding |
  |------|------|-------------|
  | [slug] | [path] | [one-line finding] |

GATE S:
  gate_s_cleared: true
  scout_anchor: [slug]
  invariant_registry_confirmed: true    (echoed from ROLE A)

If scout not found: gate_s_cleared = false. STOP.

ROLE B COMPLETE.

---

## HANDOFF SCHEMA
(Declared now — before Stage 1 opens. All handoff fields and their derivation sources.)

The synthesis artifact will contain the following fields. Each field's source is declared here
so downstream consumers and auditors can verify independence without reading Stage 5.

  | Field | Source | Independence Note |
  |-------|--------|-------------------|
  | dual_lock_fired | INCUMBENT-DEFENSE TABLE (null_tally_final = 3) | N/A — primary field |
  | co_activation_confirmed | dual_lock_fired (must equal) | Dependent on dual_lock_fired by design |
  | incumbent_defense_closed | null_tally_final from INCUMBENT-DEFENSE TABLE | INDEPENDENT — not derived from dual_lock_fired or co_activation_confirmed. Both are consumers of the same tally; neither derives the other. |
  | null_tally_final | S4 row, Running Null Count | Direct from table |
  | confidence | CE-score formula (ROLE A Invariant B) + evidence assessment | N/A |
  | escalation_triggered | dual_lock_fired (true = triggered) | N/A |

Independence contract: `incumbent_defense_closed` and `co_activation_confirmed` are both
derived from the same underlying tally but through separate derivation paths. A downstream
consumer checking `incumbent_defense_closed` does not need to read `co_activation_confirmed`
to determine campaign state. Both fields are present; neither infers from the other.

This schema is a campaign invariant. Stage 5 must produce all declared fields.
A handoff missing any declared field is a structural failure.

---

## INCUMBENT-DEFENSE TABLE
(Fill one row per evidence stage as that stage runs. Do not fill forward.)

| Stage | Stage Name        | Incumbent Defense Found | Running Null Count | Obligations Active |
|-------|-------------------|-------------------------|--------------------|--------------------|
| S2    | Web Search        | [yes/no]                | [0 or 1]           | [None or pending if S3+S4 null] |
| S3    | Intelligence Scan | [yes/no]                | [0-2]              | [None or execute if S4 null] |
| S4    | Analysis          | [yes/no]                | [0-3]              | [None or DUAL-LOCK at synthesis] |

---

## STAGE 1 — HYPOTHESIS

Artifact: simulations/prove/{topic}/{topic}-hypothesis-{date}.md

Frontmatter:
  topic: {topic}
  date: {date}
  stage: prove-hypothesis
  scout_anchor: [from ROLE B]
  gate_s_cleared: true
  invariant_registry_confirmed: true
  incumbent: [from ROLE A]
  reviewer_type: [from ROLE A — pre-committed]
  ce_score_formula: CE-score = -2 if all null [from ROLE A — pre-committed]

Body:
  Claim: One testable sentence from the scout record.
  Falsification: What would disprove this?
  Why not [incumbent]?: One sentence — what does this claim provide that the incumbent can't?

Write: simulations/prove/{topic}/{topic}-hypothesis-{date}.md
Confirm: "Hypothesis written: {topic}-hypothesis-{date}.md. Advancing to Stage 2."

---

## STAGE 2 — WEB SEARCH

Artifact: simulations/prove/{topic}/{topic}-websearch-{date}.md

### Part A — Claim Evidence
External sources supporting the claim. For each: Source, Finding, Verdict.

### Part B — Incumbent Defense (MANDATORY)
Active search for evidence that [incumbent] is still adequate.
For each: Source, Finding, Type (Contradicts / Complicates / Weakens).

If none after active search:
  "Stage 2 incumbent-defense search: null. Reason: [one specific reason].
   Running tally: 1 null. [Update INCUMBENT-DEFENSE TABLE row S2.]
   Pre-committed obligations remain pending through S3 and S4."

Update INCUMBENT-DEFENSE TABLE row S2.

Write: simulations/prove/{topic}/{topic}-websearch-{date}.md
Confirm: "Artifact written: {topic}-websearch-{date}.md. S2 row updated. Advancing to Stage 3."

---

## STAGE 3 — INTELLIGENCE SCAN

Artifact: simulations/prove/{topic}/{topic}-intelligence-{date}.md

### Part A — Internal Signals for Claim
Project files, prior artifacts, designs. Record: Path, Signal type, Finding.

### Part B — Incumbent Defense (MANDATORY)
Anything internal suggesting [incumbent] is adequate.
If none:
  "Stage 3 incumbent-defense scan: null. Running tally: [S2+1] null.
   [Update INCUMBENT-DEFENSE TABLE row S3.] A + B execute if S4 null."

Update INCUMBENT-DEFENSE TABLE row S3.

Write: simulations/prove/{topic}/{topic}-intelligence-{date}.md
Confirm: "Artifact written: {topic}-intelligence-{date}.md. S3 row updated. Advancing to Stage 4."

---

## STAGE 4 — ANALYSIS

Artifact: simulations/prove/{topic}/{topic}-analysis-{date}.md

### Part A — Evidence Assessment
Assess signals from S2-S3. For each: Source stage, Strength (HIGH / MEDIUM / LOW), Assessment.
Thin-evidence flag: fewer than 2 HIGH signals — flag THIN.

### Part B — Incumbent Defense Assessment (MANDATORY)
Assess all incumbent-defense evidence from S2 and S3. If none:
  "All collection stages null. Running tally: [N] null. All stages complete.
   [Update INCUMBENT-DEFENSE TABLE row S4.] DUAL-LOCK fires at synthesis."

Update INCUMBENT-DEFENSE TABLE row S4.

Write: simulations/prove/{topic}/{topic}-analysis-{date}.md
Confirm: "Artifact written: {topic}-analysis-{date}.md. S4 row updated. Advancing to Stage 5."

---

## STAGE 5 — SYNTHESIS

Artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md

Terminal stage.

### Schema Compliance Check
Retrieve HANDOFF SCHEMA from campaign open. Confirm all declared fields will be produced.
  dual_lock_fired: [declared source: INCUMBENT-DEFENSE TABLE]
  co_activation_confirmed: [declared source: dual_lock_fired]
  incumbent_defense_closed: [declared source: null_tally_final — INDEPENDENT]
  null_tally_final: [declared source: S4 row]
All fields present: [yes / no].

### ROLE A Invariant Compliance
  reviewer_type: [confirmed from ROLE A]
  ce_score_formula: CE-score = -2 if all null [confirmed from ROLE A]
  invariant_registry_confirmed: true
Both on file: [yes / no]. If no: halt.

### Incumbent-Defense Table (completed)
Paste filled INCUMBENT-DEFENSE TABLE. All three rows required.
  null_tally_final: [from S4 row]
  incumbent_defense_closed: [true if null_tally_final = 3, false otherwise]
  Independence: derived from null_tally_final, not from co_activation_confirmed.

### ATOMIC DUAL-LOCK
If null_tally_final = 3 — both locks fire from one trigger:

  dual_lock_fired: true
  co_activation_confirmed: true    (must equal dual_lock_fired)

  LOCK 1 — Reviewer Challenge: [reviewer_type] challenges the claim before topic-story.
  LOCK 2 — Confidence Cap: CE-score = -2. HIGH not available while challenge is open.

If null_tally_final < 3: dual_lock_fired = false. co_activation_confirmed = false. CE-score = 0.

### Findings
Summary. Reference each artifact slug.

### Incumbent Defense Register (MANDATORY)
| Stage | Source | Finding | Type |
|-------|--------|---------|------|
If all null: see DUAL-LOCK block.

### Thin-Evidence
If THIN flagged at Stage 4: name it, qualify confidence. If not: "Evidence density sufficient."

### Confidence
Level: [HIGH / MEDIUM / LOW]
CE-score: [0 / -2] (ROLE A Invariant B — not a synthesis call)
If dual-lock fired: level cannot be HIGH.

### Handoff
(Per HANDOFF SCHEMA declared at campaign open.)

  next: topic-story
  artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md
  confidence: [level]
  dual_lock_fired: [true / false]
  co_activation_confirmed: [must equal dual_lock_fired]
  null_tally_final: [0-3]
  incumbent_defense_closed: [from null_tally_final — per HANDOFF SCHEMA, independent of co_activation_confirmed]
  escalation_triggered: [true / false]
  escalation_reviewer: [reviewer_type or "N/A"]
  status: [Ready / Challenged — [reviewer_type] review required before topic-story]

Write: simulations/prove/{topic}/{topic}-synthesize-{date}.md
Confirm: "Evidence brief complete. Schema compliance: all declared fields produced.
          incumbent_defense_closed = [true/false]. Dual-lock: [fired / not triggered].
          Status: [Ready / Challenged]. Handoff: topic-story."
```

---

## V-04 — Axes: Handoff Field Independence x Role Field Ownership

**Variation axis**: Two axes combined. Handoff field independence (V-01): `incumbent_defense_closed`
is computed in a dedicated CAMPAIGN OUTCOME block at Stage 4, derived directly from `null_tally_final`,
with an explicit independence note in the handoff. Role field ownership (V-02): an ATTESTATION
MANIFEST at campaign open declares ROLE A owns `invariant_registry_confirmed` and ROLE B owns
`gate_s_cleared`, and each ROLE header carries its owned field declaration. The hypothesis
frontmatter includes a FIELD PROVENANCE MAP. No axis conflicts: the CAMPAIGN OUTCOME block
is in Stage 4; the ATTESTATION MANIFEST is at campaign open; neither modifies the other's mechanism.

**Hypothesis**: When both axes are active simultaneously, C-23 and C-24 arise from structurally
distinct mechanisms — the campaign outcome block (V-01) closes C-23 by establishing independent
derivation; the attestation manifest (V-02) closes C-24 by declaring ownership at ROLE-definition
time. Neither mechanism is a prerequisite for the other. A variation dropping the campaign
outcome block fails C-23 while retaining C-24; dropping the attestation manifest fails C-24
while retaining C-23. The combination is more robust than single-axis because each criterion
has its own structural origin.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
Two blocking roles open the campaign. Each role owns one attestation field.
Five evidence stages follow in fixed sequence. No step may be skipped or reordered.

---

## ATTESTATION MANIFEST
(Declared at campaign open — read-only after this point.)

  ROLE A owns: invariant_registry_confirmed
    Sole structural source. Dropping ROLE A creates an auditable gap.

  ROLE B owns: gate_s_cleared
    Sole structural source. Dropping ROLE B creates an auditable gap.

Both fields are required in the hypothesis frontmatter.

---

## ROLE A — INVARIANT REGISTRY LOCK
OWNED ATTESTATION FIELD: invariant_registry_confirmed

Execute first. Lock the null counter-evidence protocol.

  status_quo_comparator: [name the incumbent approach this topic must beat]

  SESSION INVARIANT A — Adversarial Reviewer:
    adversarial_reviewer_type: [role most likely to challenge the claim]
    Activation: all three evidence stages (S2, S3, S4) return null CE.
    Status: pre-registered. Execution at synthesis if triggered.

  SESSION INVARIANT B — Confidence Cap:
    ce_score_formula: CE-score = -2 if all null; 0 otherwise.
    Status: locked. Cannot be overridden at synthesis.

  invariant_registry_confirmed: true    [ROLE A's owned field — produced here only]

ROLE A COMPLETE. Do not begin ROLE B without invariant_registry_confirmed = true.

---

## ROLE B — SCOUT LOAD
OWNED ATTESTATION FIELD: gate_s_cleared

Execute after ROLE A.

Search: simulations/scout/**/{topic}-*.md

Record found artifacts:
  | Slug | Path | Key finding |
  |------|------|-------------|
  | [slug] | [path] | [one-line finding] |

  gate_s_cleared: true              [ROLE B's owned field — produced here only]
  scout_anchor: [slug]

  GATE S — both owned fields on record:
    gate_s_cleared: true            (ROLE B — this role)
    invariant_registry_confirmed: true    (ROLE A — prior role, not re-declared here)

If scout not found: gate_s_cleared = false. STOP.

ROLE B COMPLETE. Both attestation fields confirmed — open Stage 1.

---

## INCUMBENT-DEFENSE TABLE
(Fill one row per evidence stage. Do not fill forward.)

| Stage | Stage Name        | Incumbent Defense Found | Running Null Count | Obligations Active |
|-------|-------------------|-------------------------|--------------------|--------------------|
| S2    | Web Search        | [yes/no]                | [0 or 1]           | [None or pending] |
| S3    | Intelligence Scan | [yes/no]                | [0-2]              | [None or pending] |
| S4    | Analysis          | [yes/no]                | [0-3]              | [None or DUAL-LOCK at synthesis] |

---

## STAGE 1 — HYPOTHESIS

Artifact: simulations/prove/{topic}/{topic}-hypothesis-{date}.md

Frontmatter:
  topic: {topic}
  date: {date}
  stage: prove-hypothesis
  scout_anchor: [from ROLE B]

  FIELD PROVENANCE MAP:
    gate_s_cleared: [ROLE B — sole source]
    invariant_registry_confirmed: [ROLE A — sole source]
  gate_s_cleared: true
  invariant_registry_confirmed: true

  incumbent: [from ROLE A]
  reviewer_type: [from ROLE A — pre-committed]
  ce_score_formula: CE-score = -2 if all null [from ROLE A — pre-committed]

Body:
  Claim: One testable sentence from the scout record.
  Falsification: What would disprove this?
  Why not [incumbent]?: One sentence addressing the incumbent directly.

Write: simulations/prove/{topic}/{topic}-hypothesis-{date}.md
Confirm: "Hypothesis written. Field provenance: ROLE A + ROLE B. Advancing to Stage 2."

---

## STAGE 2 — WEB SEARCH

Artifact: simulations/prove/{topic}/{topic}-websearch-{date}.md

### Part A — Claim Evidence
External sources. For each: Source, Finding, Verdict (Supports / Neutral / Contradicts).

### Part B — Incumbent Defense (MANDATORY)
Active search for evidence that [incumbent] is still adequate.
For each: Source, Finding, Type (Contradicts / Complicates / Weakens).

If none:
  "Stage 2 incumbent-defense: null. Reason: [one reason].
   Running tally: 1 null. [Update row S2.] Pre-committed obligations pending through S3, S4."

Update INCUMBENT-DEFENSE TABLE row S2.

Write: simulations/prove/{topic}/{topic}-websearch-{date}.md
Confirm: "S2 complete. Row updated. Advancing to Stage 3."

---

## STAGE 3 — INTELLIGENCE SCAN

Artifact: simulations/prove/{topic}/{topic}-intelligence-{date}.md

### Part A — Internal Signals for Claim
Project files, prior artifacts, designs. Record: Path, Signal type, Finding.

### Part B — Incumbent Defense (MANDATORY)
Internal signals suggesting [incumbent] is adequate.
If none:
  "Stage 3 incumbent-defense: null. Running tally: [S2+1] null.
   [Update row S3.] A + B execute if S4 null."

Update INCUMBENT-DEFENSE TABLE row S3.

Write: simulations/prove/{topic}/{topic}-intelligence-{date}.md
Confirm: "S3 complete. Row updated. Advancing to Stage 4."

---

## STAGE 4 — ANALYSIS

Artifact: simulations/prove/{topic}/{topic}-analysis-{date}.md

### Part A — Evidence Assessment
Assess signals from S2-S3. For each: Source stage, Strength, Assessment.
Thin-evidence flag: fewer than 2 HIGH signals — flag THIN.

### Part B — Incumbent Defense Assessment (MANDATORY)
Assess all incumbent-defense evidence from S2 and S3. If none:
  "All stages null. [Update row S4.] DUAL-LOCK fires at synthesis. Pre-committed."

Update INCUMBENT-DEFENSE TABLE row S4.

### CAMPAIGN OUTCOME
(Computed from table — independently of synthesis dual-lock machinery.)

  null_tally_final: [0-3 from S4 Running Null Count]
  incumbent_defense_closed: [true if null_tally_final = 3, false otherwise]
  derivation_source: "null_tally_final from INCUMBENT-DEFENSE TABLE"
  independence_note: "This field is derived from null_tally_final, not from dual_lock_fired
    or co_activation_confirmed. Computed at Stage 4 before synthesis begins. Independently
    readable — downstream consumers may check this field without referencing the dual-lock chain."

Write: simulations/prove/{topic}/{topic}-analysis-{date}.md
Confirm: "S4 complete. Table row updated. Campaign outcome: incumbent_defense_closed = [true/false].
          Thin flag: [yes/no]. Advancing to Stage 5."

---

## STAGE 5 — SYNTHESIS

Artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md

Terminal stage.

### Attestation Manifest Compliance
  invariant_registry_confirmed: true    (ROLE A — sole source, per manifest)
  gate_s_cleared: true                  (ROLE B — sole source, per manifest)
  reviewer_type: [confirmed from ROLE A]
  ce_score_formula: CE-score = -2 if all null [ROLE A Invariant B]
Both attestation fields present from declared sole sources: [yes / no]. If no: halt.

### Campaign Outcome (from Stage 4)
  incumbent_defense_closed: [confirmed from Stage 4]
  null_tally_final: [confirmed from Stage 4]
  Independence: confirmed — derived from null_tally_final at Stage 4, not from co_activation_confirmed.

### Incumbent-Defense Table (completed)
Paste filled INCUMBENT-DEFENSE TABLE. All three rows required.

### ATOMIC DUAL-LOCK
If null_tally_final = 3 — both locks fire from one trigger:

  dual_lock_fired: true
  co_activation_confirmed: true    (must equal dual_lock_fired)

  LOCK 1 — Reviewer Challenge (ROLE A Invariant A):
    [reviewer_type] is tasked: challenge the claim. Topic-story blocked until addressed.

  LOCK 2 — Confidence Cap (ROLE A Invariant B):
    CE-score = -2. HIGH not available while challenge is open.

If not all null: dual_lock_fired = false. co_activation_confirmed = false. CE-score = 0.

### Findings
Summary. Reference each artifact slug.

### Incumbent Defense Register (MANDATORY)
| Stage | Source | Finding | Type |
|-------|--------|---------|------|
If all null: see DUAL-LOCK block.

### Thin-Evidence
If Stage 4 flagged THIN: name it, qualify confidence. If not: "Evidence density sufficient."

### Confidence
Level: [HIGH / MEDIUM / LOW]
CE-score: [0 / -2] (ROLE A Invariant B — not a synthesis call)
If dual-lock fired: level cannot be HIGH.

### Handoff
  next: topic-story
  artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md
  confidence: [level]
  dual_lock_fired: [true / false]
  co_activation_confirmed: [must equal dual_lock_fired]
  null_tally_final: [0-3]
  incumbent_defense_closed: [from Stage 4 CAMPAIGN OUTCOME — independent of co_activation_confirmed]
  escalation_triggered: [true / false]
  escalation_reviewer: [reviewer_type or "N/A"]
  status: [Ready / Challenged — [reviewer_type] review required before topic-story]

  FIELD PROVENANCE (handoff audit trail):
    invariant_registry_confirmed: [ROLE A — sole source, per ATTESTATION MANIFEST]
    gate_s_cleared: [ROLE B — sole source, per ATTESTATION MANIFEST]
    incumbent_defense_closed: [Stage 4 CAMPAIGN OUTCOME — derived from null_tally_final]

Write: simulations/prove/{topic}/{topic}-synthesize-{date}.md
Confirm: "Evidence brief complete. Attestation: ROLE A + ROLE B (per manifest).
          Campaign outcome: incumbent_defense_closed = [true/false].
          Dual-lock: [fired / not triggered]. Co-activation: [true/false].
          Status: [Ready / Challenged]. Handoff: topic-story."
```

---

## V-05 — Axes: Role Sequence + Output Format + Inertia Framing + Handoff Field Independence + Role Field Ownership (full compound)

**Variation axis**: Five axes combined. Role sequence (R6 V-01): ROLE A locks the invariant
registry, ROLE B loads the scout record — separate blocking steps, independent outputs. Output
format (R6 V-02): each evidence stage fills a row in a cumulative INCUMBENT-DEFENSE TABLE,
making null accumulation structural. Inertia framing (R6 V-04): the status-quo comparator is
the "incumbent" throughout, framing every null result as an outstanding incumbent-defense
obligation. Handoff field independence (V-01): a CAMPAIGN OUTCOME block at Stage 4 computes
`incumbent_defense_closed` from the raw tally before synthesis, with explicit independence
notation. Role field ownership (V-02): an ATTESTATION MANIFEST at campaign open declares each
role's sole-owned field; each ROLE header carries its ownership declaration; the hypothesis
frontmatter includes a FIELD PROVENANCE MAP.

**Hypothesis**: When all five axes are active simultaneously, C-23 and C-24 arise from structurally
distinct mechanisms that are each traceable to their own axis:

- C-23 (independence): CAMPAIGN OUTCOME block (V-01 axis) computes `incumbent_defense_closed`
  at Stage 4 from the table tally — separate step, separate derivation, independence visible
  in the field's origin.
- C-24 (ownership): ATTESTATION MANIFEST (V-02 axis) declares ownership at ROLE definition time
  — each role's owned field is named before any stage runs; the provenance map in the hypothesis
  frontmatter makes the gap from dropping either role immediately auditable.

No axis can be dropped without losing at least one criterion. The full compound is the maximum
ceiling achievable under v7: C-01 through C-24 all satisfied, each criterion arising from its
own structural source.

---

```
Topic: {topic}
Date:  {date}

Full prove evidence campaign. The incumbent is the status-quo approach you must beat.
Two blocking roles open the campaign — each owns one attestation field.
Evidence stages track incumbent-defense results in a running table.
Both null-CE consequences fire atomically if all stages fail to find incumbent defense.

---

## ATTESTATION MANIFEST
(Declared at campaign open — read-only after this point.)

  ROLE A owns: invariant_registry_confirmed
    Sole structural source. Dropping ROLE A creates an auditable gap: this field absent.

  ROLE B owns: gate_s_cleared
    Sole structural source. Dropping ROLE B creates an auditable gap: this field absent.

No other stage may declare either field as an original output.
Both are required in the hypothesis frontmatter FIELD PROVENANCE MAP.

---

## ROLE A — INVARIANT REGISTRY LOCK
OWNED ATTESTATION FIELD: invariant_registry_confirmed

Execute first. Lock the incumbent identity and null-CE protocol.

  incumbent: [name the status-quo approach this topic must beat — be specific]
  reviewer_type: [role most likely to defend the incumbent]
  ce_score_formula: CE-score = -2 if all three evidence stages null; 0 otherwise

  SESSION INVARIANT A — Reviewer:
    Activation: all three evidence stages return null incumbent defense.
    Status: pre-registered. If activation fires, execution only — not a new decision.

  SESSION INVARIANT B — Cap:
    ce_score_formula above. Locked. Cannot be overridden at synthesis.

  invariant_registry_confirmed: true    [ROLE A's owned field]
  registry_note: "Locked. Cannot be modified after ROLE A."

ROLE A COMPLETE. Output: invariant_registry_confirmed.
Do not begin ROLE B without invariant_registry_confirmed = true.

---

## ROLE B — SCOUT LOAD
OWNED ATTESTATION FIELD: gate_s_cleared

Execute after ROLE A.

Search: simulations/scout/**/{topic}-*.md

Found:
  | Slug | Path | Key finding |
  |------|------|-------------|
  | [slug] | [path] | [finding] |

  gate_s_cleared: true              [ROLE B's owned field]
  scout_anchor: [slug]

  GATE S — both owned fields confirmed:
    gate_s_cleared: true            (ROLE B — this role)
    invariant_registry_confirmed: true    (ROLE A — prior role, not re-declared here)

If scout not found: gate_s_cleared = false. STOP.
"GATE S FAIL — gate_s_cleared cannot be set. Scout prerequisite unmet."

ROLE B COMPLETE. Both attestation fields confirmed — open Stage 1.

---

## INCUMBENT-DEFENSE TABLE
(Fill one row per evidence stage as that stage runs. Do not fill forward.)

| Stage | Stage Name        | Incumbent Defense Found | Running Null Count | Obligations Active |
|-------|-------------------|-------------------------|--------------------|--------------------|
| S2    | Web Search        | [yes/no]                | [0 or 1]           | [None / A+B pending if S3+S4 null] |
| S3    | Intelligence Scan | [yes/no]                | [0-2]              | [None / A+B execute if S4 null] |
| S4    | Analysis          | [yes/no]                | [0-3]              | [None / DUAL-LOCK at synthesis] |

---

## STAGE 1 — HYPOTHESIS

Artifact: simulations/prove/{topic}/{topic}-hypothesis-{date}.md

Frontmatter:
  topic: {topic}
  date: {date}
  stage: prove-hypothesis
  scout_anchor: [from ROLE B]

  FIELD PROVENANCE MAP:
    gate_s_cleared: [ROLE B — sole source, per ATTESTATION MANIFEST]
    invariant_registry_confirmed: [ROLE A — sole source, per ATTESTATION MANIFEST]
  gate_s_cleared: true
  invariant_registry_confirmed: true

  incumbent: [from ROLE A]
  reviewer_type: [from ROLE A — pre-committed]
  ce_score_formula: CE-score = -2 if all null [from ROLE A — pre-committed]

Body:
  Claim: One testable sentence from the scout record.
  Falsification: What would disprove this?
  Why not [incumbent]?: One sentence — what does this claim provide that the incumbent can't?

Write: simulations/prove/{topic}/{topic}-hypothesis-{date}.md
Confirm: "Hypothesis written: {topic}-hypothesis-{date}.md. Field provenance map: ROLE A +
          ROLE B attested per manifest. Advancing to Stage 2."

---

## STAGE 2 — WEB SEARCH

Artifact: simulations/prove/{topic}/{topic}-websearch-{date}.md

### Part A — Claim Evidence
External sources supporting the claim.
For each: Source, Finding, Verdict (Supports / Neutral / Contradicts).

### Part B — Incumbent Defense (MANDATORY)
Active search for evidence that [incumbent] is still the right approach.
For each: Source, Finding, Type (Contradicts / Complicates / Weakens the claim).

If none after active search:
  "Stage 2 incumbent-defense search: null. Reason: [one specific reason].
   [Update INCUMBENT-DEFENSE TABLE row S2: Defense Found = no, Running Null = 1,
    Obligations = A ([reviewer_type]) + B (CE-score = -2) pending if S3+S4 also null.
    Pre-committed in ROLE A — not a synthesis decision.]"

Update INCUMBENT-DEFENSE TABLE row S2.

Write: simulations/prove/{topic}/{topic}-websearch-{date}.md
Confirm: "Artifact written: {topic}-websearch-{date}.md. S2 table row updated. Advancing to Stage 3."

---

## STAGE 3 — INTELLIGENCE SCAN

Artifact: simulations/prove/{topic}/{topic}-intelligence-{date}.md

### Part A — Internal Signals for Claim
Project files, prior artifacts, existing designs.
Record: Path, Signal type (supports / gap / risk), Finding.

### Part B — Incumbent Defense (MANDATORY)
Internal signals suggesting [incumbent] is adequate or that this feature is redundant.
If none:
  "Stage 3 incumbent-defense scan: null.
   [Update INCUMBENT-DEFENSE TABLE row S3: Defense Found = no, Running Null = [S2+1],
    Obligations = A + B execute at synthesis if S4 also null.
    Pre-committed in ROLE A — not a new decision.]"

Update INCUMBENT-DEFENSE TABLE row S3.

Write: simulations/prove/{topic}/{topic}-intelligence-{date}.md
Confirm: "Artifact written: {topic}-intelligence-{date}.md. S3 table row updated. Advancing to Stage 4."

---

## STAGE 4 — ANALYSIS

Artifact: simulations/prove/{topic}/{topic}-analysis-{date}.md

### Part A — Evidence Assessment
Assess signals from S2-S3 against the hypothesis.
For each: Source stage, Strength (HIGH / MEDIUM / LOW), Assessment.
Thin-evidence flag: fewer than 2 HIGH signals — flag THIN, describe the gap.

### Part B — Incumbent Defense Assessment (MANDATORY)
Assess all incumbent-defense evidence from S2 and S3. If none from either:
  "Stage 4 incumbent-defense assessment: null. No defense found across S2, S3, S4.
   [Update INCUMBENT-DEFENSE TABLE row S4: Defense Found = no, Running Null = [S2+S3+1],
    Obligations = DUAL-LOCK fires at synthesis. Invariant A: [reviewer_type] executes.
    Invariant B: CE-score = -2 applies. Both pre-committed in ROLE A — execution only.]"

Update INCUMBENT-DEFENSE TABLE row S4.

### CAMPAIGN OUTCOME
(Computed from completed table — independently of synthesis dual-lock machinery.)

  null_tally_final: [0-3, from S4 Running Null Count]
  incumbent_defense_closed: [true if null_tally_final = 3, false otherwise]
  derivation_source: "null_tally_final from INCUMBENT-DEFENSE TABLE — not derived from
    dual_lock_fired or co_activation_confirmed. Computed at Stage 4 before synthesis begins.
    Independently readable: downstream consumers check this field without referencing the
    dual-lock chain. Both incumbent_defense_closed and co_activation_confirmed derive from
    the same underlying tally through separate derivation paths."

Write: simulations/prove/{topic}/{topic}-analysis-{date}.md
Confirm: "Artifact written: {topic}-analysis-{date}.md. S4 table row updated.
          Campaign outcome: incumbent_defense_closed = [true/false].
          Thin flag: [yes/no]. Advancing to Stage 5."

---

## STAGE 5 — SYNTHESIS

Artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md

Terminal stage.

### Attestation Manifest Compliance
Confirm both ROLE-owned fields are on record (per ATTESTATION MANIFEST):
  invariant_registry_confirmed: true    (ROLE A — sole source)
  gate_s_cleared: true                  (ROLE B — sole source)
  reviewer_type: [confirmed from ROLE A] (ROLE A Invariant A)
  ce_score_formula: CE-score = -2 if all null (ROLE A Invariant B)
Both attestation fields from declared sole sources: [yes / no]. If no: halt — attestation gap.

### Campaign Outcome (from Stage 4)
  incumbent_defense_closed: [confirmed from Stage 4 CAMPAIGN OUTCOME]
  null_tally_final: [confirmed from Stage 4]
  Independence confirmed: derived from null_tally_final at Stage 4.
    Not derived from dual_lock_fired or co_activation_confirmed.
    Both fields are independently readable in the handoff.

### Incumbent-Defense Table (completed)
Paste filled INCUMBENT-DEFENSE TABLE here. All three rows required.

### ATOMIC DUAL-LOCK
If null_tally_final = 3 — one trigger, both locks fire simultaneously:

  ======================================================================
  DUAL-LOCK ACTIVATION — table total = 3 null incumbent defense
  Both locks activate from this single entry. Partial activation is a format error.
  ======================================================================

  dual_lock_fired: true
  co_activation_confirmed: true    (must equal dual_lock_fired)

  LOCK 1 — Reviewer Challenge (ROLE A Invariant A):
    [reviewer_type] is tasked: challenge the claim from the incumbent's position.
    What evidence was absent? What risk does the incumbent handle that this claim doesn't?
    Promotion to topic-story blocked until challenge addressed or explicitly deferred.

  LOCK 2 — Confidence Cap (ROLE A Invariant B):
    CE-score = -2. Ceiling: MEDIUM. HIGH not available while challenge is open.
    cap_applied: true

  ======================================================================
  END DUAL-LOCK
  ======================================================================

If not all null: dual_lock_fired = false. co_activation_confirmed = false. CE-score = 0.

### Findings
Summary. Reference each artifact slug: {topic}-hypothesis, {topic}-websearch,
{topic}-intelligence, {topic}-analysis.

### Incumbent Defense Register (MANDATORY)
| Stage | Source | Finding | Type |
|-------|--------|---------|------|
If all null: see DUAL-LOCK block above.

### Thin-Evidence
If Stage 4 flagged THIN: name the finding, qualify confidence.
If not: "Evidence density sufficient."

### Confidence
Level: [HIGH / MEDIUM / LOW]
CE-score applied: [0 / -2] (ROLE A Invariant B — not a synthesis decision)
If dual-lock fired: level cannot be HIGH.

### Handoff
  next: topic-story
  artifact: simulations/prove/{topic}/{topic}-synthesize-{date}.md
  confidence: [level]
  dual_lock_fired: [true / false]
  co_activation_confirmed: [must equal dual_lock_fired]
  null_tally_final: [0-3]
  incumbent_defense_closed: [from Stage 4 CAMPAIGN OUTCOME — independent of co_activation_confirmed]
  escalation_triggered: [true / false]
  escalation_reviewer: [reviewer_type or "N/A"]
  status: [Ready / Challenged — [reviewer_type] review required before topic-story]

  FIELD PROVENANCE (handoff audit trail):
    invariant_registry_confirmed: [ROLE A — sole source, per ATTESTATION MANIFEST]
    gate_s_cleared: [ROLE B — sole source, per ATTESTATION MANIFEST]
    incumbent_defense_closed: [Stage 4 CAMPAIGN OUTCOME — derived from null_tally_final]

Write: simulations/prove/{topic}/{topic}-synthesize-{date}.md
Confirm: "Evidence brief complete. Attestation: ROLE A + ROLE B (per manifest).
          Campaign outcome: incumbent_defense_closed = [true/false].
          Dual-lock: [fired / not triggered]. Co-activation: [true/false].
          Status: [Ready / Challenged]. Handoff: topic-story."
```

---

## Anchor Designation

**Anchor: V-05.**

V-05 is the full compound: all three R6 V-05 axes (role sequence, output format, inertia framing)
plus both R7 axes (handoff field independence, role field ownership). It satisfies the complete
v7 severity stack C-01 through C-24 with each criterion arising from its own structural source:

| Criterion | Source in V-05 |
|-----------|----------------|
| C-23 | CAMPAIGN OUTCOME block at Stage 4 — `incumbent_defense_closed` derived from `null_tally_final`, independence declared in derivation_source field |
| C-24 | ATTESTATION MANIFEST at campaign open + OWNED FIELD declaration in each ROLE header + FIELD PROVENANCE MAP in hypothesis frontmatter |
| C-22 | Two distinct gate fields in hypothesis frontmatter, each traced to its source role via FIELD PROVENANCE MAP |
| C-21 | `co_activation_confirmed` in handoff with integrity constraint (`must equal dual_lock_fired`) |
| C-20 | Running Null Count column in INCUMBENT-DEFENSE TABLE, updated per stage |
| C-19 | Protocol pre-committed at ROLE A before Stage 1 |
| C-18 | ATOMIC DUAL-LOCK fires both locks from single trigger |
| C-17 | CE-score consequence present and locked |
| C-16 | Reviewer escalation path declared |
| C-14 | Recording of all incumbent-defense evidence per stage |

**Stress test for V-05**: A variation dropping the ATTESTATION MANIFEST while keeping V-05's
ROLE A and ROLE B fails C-24 (ownership not declared at ROLE definition time) but retains C-23
(CAMPAIGN OUTCOME block still present). A variation replacing the CAMPAIGN OUTCOME block with
`incumbent_defense_closed: [must equal co_activation_confirmed]` fails C-23 (dependent
definition) but retains C-24 (attestation manifest unchanged). The two criteria are
structurally independent — each has its own failure mode.

**Ceiling status under v7**: V-05 achieves 144/144. Both new criteria closed. The v7 ceiling
is V-05.
