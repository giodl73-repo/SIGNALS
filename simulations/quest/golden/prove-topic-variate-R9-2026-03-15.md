---
skill: quest-variate
skill_target: prove-topic
round: R9
date: 2026-03-15
rubric: prove-topic-rubric-v8-2026-03-15.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [schema_self_registration, symmetric_independence_chain, per_stage_schema_integrity_count, annotation_rule_precommitted]
  combined: [V-05]
r8_anchor: "V-05 (role_sequence + output_format + inertia_framing + handoff_derivation_annotations + precommitted_handoff_schema + independence_path_chain — satisfies C-01 through C-27, 156/156)"
r9_targets: >
  Four patterns in R8 V-05 that exceed any v8 criterion:
  (1) schema_compliance_confirmed is pre-declared as field 9 in the CAMPAIGN OPEN schema table.
  C-26 requires a compliance check at synthesis; it does not require the compliance-check field
  itself to be pre-declared as a schema contract member before Stage 0. R8 V-05's CAMPAIGN OPEN
  lists schema_compliance_confirmed as field 9 with derivation source "synthesis-time compliance
  check" — making the schema self-referential and the compliance field pre-obligated.
  (2) co_activation_confirmed carries only a brief NOT annotation ([NOT from incumbent_defense_closed])
  in R8 V-05. C-27 requires a full two-part chain on incumbent_defense_closed; it does not extend
  to co_activation_confirmed. A symmetric positive_derivation + independence_chain on
  co_activation_confirmed closes the reverse path with the same structural rigor.
  (3) Per-stage schema integrity notes in R8 V-05 say "Handoff schema locked — null result does
  not change the schema." This is a prose note. C-20 formalizes per-stage null tally as a running
  count. No criterion formalizes per-stage schema integrity as a structured count. A schema-
  integrity count per evidence stage creates an audit chain for the schema contract across the
  collection phase, symmetric to C-20's null tally chain.
  (4) The DERIVATION ANNOTATION RULE is declared at synthesis time in all R8 variations. C-25
  requires the rule at synthesis; C-19 pre-commits the null-CE protocol at CAMPAIGN OPEN with
  invariant language. No criterion requires the annotation rule to be pre-committed before Stage 0.
  Moving the DERIVATION ANNOTATION RULE to CAMPAIGN OPEN as SESSION INVARIANT C makes the
  annotation obligation a session property — pre-registered before any evidence runs, not
  assembled as a synthesis instruction.
severity_stack_gap: >
  A variation satisfying C-01 through C-27 can still:
  (1) add schema_compliance_confirmed reactively at synthesis without declaring it as a
  pre-committed field — the compliance check satisfies C-26 but the compliance-check field
  is not part of the pre-committed contract, and could be suppressed without creating a
  schema-violation audit trail;
  (2) label co_activation_confirmed with [derived from: dual_lock_fired] and satisfy C-25's
  annotation requirement while leaving the reverse independence path (NOT from
  incumbent_defense_closed) as an implicit prose note rather than a structured two-part chain;
  (3) include "Handoff schema locked" in null result notes without any running count, making
  per-stage schema integrity unauditable from the collection-phase artifacts alone;
  (4) declare the DERIVATION ANNOTATION RULE at synthesis time only — satisfying C-25's
  structural requirement while leaving the annotation obligation as a synthesis instruction
  that could be omitted before Stage 5 without any pre-committed invariant to enforce it.
---

# prove-topic — Variation Round R9

Five complete, runnable skill body prompts. Each is self-contained — no diff, no cross-references.

Round 9 targets four patterns in R8 V-05 that exceed the v8 rubric ceiling (C-27). All
variations are built on the full v8 stack (C-01 through C-27). Single-axis variations each
introduce one new structural pattern; V-05 combines all four.

The four new axes:

- **R9 axis 1 (schema self-registration)**: `schema_compliance_confirmed` declared as a
  pre-committed field in CAMPAIGN OPEN, with derivation source locked before Stage 0. The
  compliance check is itself a schema contract member — dropping it from synthesis is a
  schema violation, not just a missed annotation.

- **R9 axis 2 (symmetric independence chain)**: `co_activation_confirmed` carries a full
  `positive_derivation` + `independence_chain` record in the handoff, symmetric to the C-27
  chain on `incumbent_defense_closed`. Both campaign-sensitive fields now carry explicit
  two-part independence proofs, auditable without tracing dual-lock semantics.

- **R9 axis 3 (per-stage schema integrity count)**: Each evidence stage appends a SCHEMA
  INTEGRITY NOTE recording the pre-committed field count (N/N) and confirming no additions
  or omissions. This creates a per-stage audit chain for the schema contract, symmetric to
  C-20's per-stage null tally chain.

- **R9 axis 4 (annotation rule pre-committed)**: The DERIVATION ANNOTATION RULE is declared
  as SESSION INVARIANT C at CAMPAIGN OPEN with invariant language. ROLE A's registry lock
  covers all three invariants. At synthesis, the rule EXECUTES — it is not declared. The
  annotation obligation is pre-registered before any evidence runs.

---

## V-01 — Axis: Schema Self-Registration

**Variation axis**: Schema self-registration — `schema_compliance_confirmed` is declared as
a member of the PRE-COMMITTED HANDOFF SCHEMA at CAMPAIGN OPEN, with its derivation source
locked as "synthesis-time compliance check against this CAMPAIGN OPEN schema." The field is
not added reactively at synthesis; it is pre-obligated. Omitting it from the synthesis output
is a schema violation: the pre-committed schema declares it, so its absence is detectable from
the CAMPAIGN OPEN block alone without reading the synthesis.

**Hypothesis**: C-26 requires the handoff schema to be pre-committed at CAMPAIGN OPEN and
a compliance check included at synthesis. But the set of pre-committed fields can exclude
`schema_compliance_confirmed` — the builder satisfies C-26 by adding the compliance note
reactively at synthesis after writing the declared fields. Schema self-registration removes
this discretion: the schema contract declares `schema_compliance_confirmed` as a required
output field. A synthesis that omits it fails the schema check even if all other declared
fields are present. A synthesis that adds it without it being pre-declared satisfies C-26's
compliance check but violates the pre-commitment contract by introducing an undeclared field.
Self-registration makes the compliance check itself subject to the contract it certifies.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
The campaign opens with two blocking roles followed by five evidence stages in fixed sequence.
Stages run forward only — no skipping, no re-running, no reordering.

---

## CAMPAIGN OPEN

Fill before any role or stage begins.

  status_quo_comparator: [name the incumbent approach this topic must displace]

NULL COUNTER-EVIDENCE PROTOCOL — session-level invariants, pre-committed now:

  SESSION INVARIANT A — Adversarial Reviewer:
    adversarial_reviewer_type: [role most likely to challenge the claim]
    Activation: fires if ALL three evidence stages (S2, S3, S4) return null CE.
    Invariant language: pre-registered — cannot be modified or bypassed at synthesis.

  SESSION INVARIANT B — Confidence Cap:
    ce_score_formula: CE-score = -2 if all three evidence stages null; 0 otherwise.
    Invariant language: locked formula — cannot be softened or overridden at synthesis.

PRE-COMMITTED HANDOFF SCHEMA — session-level invariant, locked now:

Synthesis must produce exactly these 9 fields with exactly these derivation sources.
No additions. No omissions. Derivation-source mismatch = format error.

  FIELD                       | REQUIRED DERIVATION SOURCE
  ----------------------------|------------------------------------------------------
  scout_anchor                | ROLE B scout load
  hypothesis                  | Stage 1 artifact write
  analysis                    | Stage 4 artifact write
  null_tally_final            | Stage 4 CAMPAIGN OUTCOME BLOCK
  incumbent_defense_closed    | null_tally_final (NOT dual_lock_fired; NOT co_activation_confirmed)
  co_activation_confirmed     | dual_lock_fired in synthesis (NOT incumbent_defense_closed)
  confidence                  | evidence_score + ce_score formula per SESSION INVARIANT B
  next                        | static: "topic-story"
  schema_compliance_confirmed | synthesis-time compliance check against this CAMPAIGN OPEN schema

Field 9 (schema_compliance_confirmed) is pre-declared. It is not added reactively at
synthesis. Omitting it is a schema violation. Adding a different compliance-check field
in its place is an undeclared-field violation. Both are detectable from this block alone.

All session invariants (A, B, and Handoff Schema) are now locked for the full session.
Do not modify after this point.

---

## ROLE A — INVARIANT REGISTRY LOCK

OWNED ATTESTATION FIELD: invariant_registry_confirmed
Sole producer of this field. No other role or stage may produce it.

Execute first. Confirm SESSION INVARIANT A, SESSION INVARIANT B, and PRE-COMMITTED
HANDOFF SCHEMA (including field 9 self-registration) are all active as session invariants.

  invariant_registry_confirmed: true    [ROLE A's owned field — produced here only]

ROLE A COMPLETE. Output: invariant_registry_confirmed.
Do not begin ROLE B without invariant_registry_confirmed = true.

---

## ROLE B — SCOUT LOAD

OWNED ATTESTATION FIELD: gate_s_cleared
Sole producer of this field. No other role or stage may produce it.

Execute after ROLE A. Do not begin hypothesis work until this role completes.

Locate: {topic}-scout-record-{date}.md
If not found: STOP. Record: "GATE S FAIL — scout record missing. Campaign cannot proceed."
If found: load the record. Extract: market signal, competitor landscape, feasibility finding.

  gate_s_cleared: true    [ROLE B's owned field — produced here only]

ROLE B COMPLETE. Output: gate_s_cleared. Both attestation fields on record — open Stage 1.

---

## GATE S

Requires ROLE A and ROLE B both complete.

  gate_s_cleared: true              (ROLE B — sole source)
  invariant_registry_confirmed: true    (ROLE A — sole source; covers null-CE + handoff schema)

Dropping ROLE A: invariant_registry_confirmed absent — auditable structural gap.
Dropping ROLE B: gate_s_cleared absent — auditable structural gap.

If either field is false or missing: STOP. Do not open Stage 1.
If both fields are true: advance to Stage 1.

---

## Stage 1 — Hypothesis

Write: {topic}-hypothesis-{date}.md

Frontmatter:
  topic: {topic}
  date: {date}
  scout_anchor: {topic}-scout-record-{date}.md   [loaded in ROLE B]
  gate_s_cleared: true             [ROLE B — sole source]
  invariant_registry_confirmed: true    [ROLE A — sole source; covers all three session invariants]
  incumbent: [from status_quo_comparator — CAMPAIGN OPEN]
  adversarial_reviewer_type: [from SESSION INVARIANT A — CAMPAIGN OPEN]
  ce_score_formula: CE-score = -2 if all null [from SESSION INVARIANT B — CAMPAIGN OPEN]
  handoff_schema_locked: true      [PRE-COMMITTED HANDOFF SCHEMA active; 9 fields including
                                    schema_compliance_confirmed at field 9 — self-registered]

Body:
  Hypothesis statement: [one sentence — what {topic} does better than the incumbent]
  Basis: [3-5 signals from the scout record]
  Counter-hypothesis: [what the incumbent would claim in rebuttal]

Artifact written: {topic}-hypothesis-{date}.md.
Confirm: "Hypothesis written. ROLE A + ROLE B attested. Schema self-registration confirmed
          in frontmatter (field 9 pre-declared). Advancing to Stage 2."

---

## Stage 2 — Web Search

Write: {topic}-websearch-{date}.md

Search for external evidence on {topic}. For each finding, record:
claim, source URL, CE-relevant (yes/no), quote.

Incumbent comparator: [from CAMPAIGN OPEN]. Note any evidence addressing whether the
incumbent approach has equivalent capability — this is CE for the hypothesis.

NULL RESULT NOTE (if no CE found in this stage):
  Stage 2 CE result: NULL
  Running tally: [count] null. [X] evidence stages remain.
  Protocol status: SESSION INVARIANTs A and B remain active — no change.
  Schema integrity: pre-committed schema unchanged — 9 fields locked including
  schema_compliance_confirmed at field 9. Null result creates no schema modification.

Artifact written: {topic}-websearch-{date}.md.
Confirm: "Stage 2 complete. CE: [found / NULL]. Advancing to Stage 3."

---

## Stage 3 — Internal Intelligence

Write: {topic}-intelligence-{date}.md

Scan internal sources. For each finding, record: artifact path, claim, CE-relevant (yes/no).

NULL RESULT NOTE (if no CE found in this stage):
  Stage 3 CE result: NULL
  Running tally: [count] null. [X] stage remains.
  Protocol status: SESSION INVARIANTs A and B remain active — no change.
  Schema integrity: pre-committed schema unchanged — 9 fields locked including
  schema_compliance_confirmed at field 9. Null result creates no schema modification.

Artifact written: {topic}-intelligence-{date}.md.
Confirm: "Stage 3 complete. CE: [found / NULL]. Advancing to Stage 4."

---

## Stage 4 — Analysis

Write: {topic}-analysis-{date}.md

Analyze all evidence across Stages 2 and 3.
- Supporting evidence strength.
- Counter-evidence summary: all CE found, sources, credibility.
- If CE null: acknowledge explicitly, list sources checked.

### CAMPAIGN OUTCOME BLOCK

Compute from evidence tally before synthesis:

  null_tally_final: [0-3 — count of evidence stages returning null CE]
  incumbent_defense_closed: [true if null_tally_final = 3; false otherwise]
  derivation: "null_tally_final via formula (null_tally_final >= 3 → true).
               NOT derived from dual_lock_fired or co_activation_confirmed."

Confirm: "Stage 4 complete. Campaign outcome: incumbent_defense_closed = [true/false].
          null_tally_final = [count]. Advancing to Stage 5."

Artifact written: {topic}-analysis-{date}.md.

---

## Stage 5 — Synthesis

Write: {topic}-synthesize-{date}.md

Confirm SESSION INVARIANTs A and B are in scope.
Retrieve PRE-COMMITTED HANDOFF SCHEMA from CAMPAIGN OPEN. Confirm all 9 fields including
field 9 (schema_compliance_confirmed) will be produced.

### Findings

3-5 bullet points, each traceable to a specific artifact (path or stage reference).

### Counter-Evidence

MANDATORY SECTION. Counter-evidence is unconditionally required.
If CE was found: list each item with source artifact and credibility rating.
If CE was null: state: "No counter-evidence found. Sources checked: [Stage 2 sources],
[Stage 3 sources]. This null result is the primary risk to the hypothesis."

If CE is null:
  - Adversarial review required before any promotion decision.
    Assign: {adversarial_reviewer_type} (SESSION INVARIANT A — execution, not new decision).
  - Confidence mechanically capped by SESSION INVARIANT B: CE-score = -2. Cannot be bypassed.

### ATOMIC DUAL-LOCK (activates if null_tally_final = 3)

  LOCK 1 — Adversarial Reviewer (SESSION INVARIANT A):
    Reviewer: {adversarial_reviewer_type}
    Required before promotion. Pre-committed. Execution only.

  LOCK 2 — Confidence Cap (SESSION INVARIANT B):
    ce_score_formula applied: CE-score = -2 (all-null).
    Maximum claim: MEDIUM. HIGH blocked without adversarial input.

  dual_lock_fired: [true if null_tally_final = 3, false otherwise]
  co_activation_confirmed: [must equal dual_lock_fired — format error if they differ]
  Note: co_activation_confirmed and incumbent_defense_closed are parallel consumers of
        null_tally_final. Neither derives the other.

### Confidence Level

  evidence_score: [0-5]
  ce_score: [0 or -2 per SESSION INVARIANT B formula]
  confidence: [LOW / MEDIUM / HIGH — HIGH blocked if ce_score = -2]

### Handoff

SCHEMA COMPLIANCE CHECK — before writing this section, retrieve PRE-COMMITTED HANDOFF
SCHEMA from CAMPAIGN OPEN. Confirm all 9 declared fields — including field 9
(schema_compliance_confirmed) — will be produced with their declared derivation sources.
Any mismatch: record "SCHEMA ERROR: {field} — expected derivation: {expected}, actual: {actual}."
Note: schema_compliance_confirmed is pre-declared as field 9. Omitting it is a schema
violation. Adding a substitute note is an undeclared-field violation.

DERIVATION ANNOTATION RULE: every field in this section must carry a [derived from: X]
label. Unlabeled field = format error.

Write all 9 declared fields:

  scout_anchor: {topic}-scout-record-{date}.md
    [derived from: ROLE B scout load]

  hypothesis: {topic}-hypothesis-{date}.md
    [derived from: Stage 1 artifact write]

  analysis: {topic}-analysis-{date}.md
    [derived from: Stage 4 artifact write]

  null_tally_final: [0-3]
    [derived from: Stage 4 CAMPAIGN OUTCOME BLOCK]

  incumbent_defense_closed: [true if null_tally_final = 3, false otherwise]
    positive_derivation: "null_tally_final via formula null_tally_final >= 3"
    independence_chain: "NOT derived from dual_lock_fired; NOT derived from co_activation_confirmed"
    [derived from: null_tally_final — independent of co_activation_confirmed confirmed]

  co_activation_confirmed: [must equal dual_lock_fired]
    [derived from: dual_lock_fired in ATOMIC DUAL-LOCK — NOT from incumbent_defense_closed]

  confidence: [LOW/MEDIUM/HIGH]
    [derived from: evidence_score + ce_score formula per SESSION INVARIANT B]

  next: topic-story
    [derived from: static handoff target]

  schema_compliance_confirmed: true
    [derived from: synthesis-time compliance check against CAMPAIGN OPEN schema —
     pre-declared as field 9; self-registration confirmed; all 9 fields present
     with declared derivation sources; no additions; no omissions]

Confirm: "Synthesis complete. All 9 fields written including pre-declared field 9
          (schema_compliance_confirmed). Self-registration verified — compliance check
          field was itself a schema contract member before Stage 0.
          Evidence brief ready for topic-story.
          Artifact written: {topic}-synthesize-{date}.md."
```

---

## V-02 — Axis: Symmetric Independence Chain on `co_activation_confirmed`

**Variation axis**: Symmetric independence chain — `co_activation_confirmed` carries a full
two-part independence record in the handoff, mirroring the C-27 structure on
`incumbent_defense_closed`. The record includes: `positive_derivation: dual_lock_fired in
ATOMIC DUAL-LOCK` and `independence_chain: NOT derived from incumbent_defense_closed; NOT
derived from null_tally_final`. Both campaign-sensitive handoff fields now carry explicit
structural independence proofs in the same format.

**Hypothesis**: C-27 requires a two-part independence chain on `incumbent_defense_closed`:
positive derivation source plus explicit negative assertion naming what it is NOT derived from.
This closes the path from `incumbent_defense_closed` to `co_activation_confirmed`. But the
reverse path — `co_activation_confirmed` derived from `incumbent_defense_closed` — is only
closed by a brief NOT annotation in R8 V-05, not a structured chain. A downstream consumer
reading the handoff cannot verify the reverse independence claim without domain knowledge
of the dual-lock mechanism. Applying the same two-part pattern to `co_activation_confirmed`
closes both directions with identical structural rigor and makes the mutual independence of
the two campaign-sensitive fields auditable from the handoff alone.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
Two blocking roles open the campaign; five evidence stages follow in fixed sequence.
Forward only — no skipping, no re-running.

---

## CAMPAIGN OPEN

Fill before any role or stage begins.

  status_quo_comparator: [name the incumbent approach this topic must displace]

NULL COUNTER-EVIDENCE PROTOCOL — session-level invariants, pre-committed now:

  SESSION INVARIANT A — Adversarial Reviewer:
    adversarial_reviewer_type: [role most likely to challenge the claim]
    Activation: fires if ALL three evidence stages (S2, S3, S4) return null CE.
    Binding: pre-registered — cannot be modified or bypassed at synthesis.

  SESSION INVARIANT B — Confidence Cap:
    ce_score_formula: CE-score = -2 if all three evidence stages null; 0 otherwise.
    Binding: locked formula — cannot be softened or overridden at synthesis.

PRE-COMMITTED HANDOFF SCHEMA — session-level invariant, locked now:

Synthesis must produce exactly these 9 fields with these derivation sources.
No additions. No omissions. Derivation-source mismatch = format error.

  FIELD                       | REQUIRED DERIVATION SOURCE
  ----------------------------|------------------------------------------------------
  scout_anchor                | ROLE B scout load
  hypothesis                  | Stage 1 artifact write
  analysis                    | Stage 4 artifact write
  null_tally_final            | Stage 4 CAMPAIGN OUTCOME BLOCK
  incumbent_defense_closed    | null_tally_final (NOT dual_lock_fired; NOT co_activation_confirmed)
  co_activation_confirmed     | dual_lock_fired in synthesis (NOT incumbent_defense_closed;
                              |   NOT null_tally_final directly)
  confidence                  | evidence_score + ce_score formula per SESSION INVARIANT B
  next                        | static: "topic-story"
  schema_compliance_confirmed | synthesis-time compliance check

Both campaign-sensitive fields (incumbent_defense_closed, co_activation_confirmed)
have declared independence constraints. The derivation sources are mutually exclusive:
neither field derives the other.

All session invariants are now locked. Do not modify after this point.

---

## ROLE A — INVARIANT REGISTRY LOCK

OWNED ATTESTATION FIELD: invariant_registry_confirmed
Sole producer of this field.

Execute first. Confirm SESSION INVARIANT A, SESSION INVARIANT B, and PRE-COMMITTED
HANDOFF SCHEMA are active. Note: schema declares mutual independence of both
campaign-sensitive fields — this is part of the locked invariant state.

  invariant_registry_confirmed: true    [ROLE A's owned field — produced here only]

ROLE A COMPLETE. Do not begin ROLE B without invariant_registry_confirmed = true.

---

## ROLE B — SCOUT LOAD

OWNED ATTESTATION FIELD: gate_s_cleared
Sole producer of this field.

Execute after ROLE A.

Locate: {topic}-scout-record-{date}.md
If not found: STOP. "GATE S FAIL — scout record missing."
If found: load record. Extract: market signal, competitor landscape, feasibility finding.

  gate_s_cleared: true    [ROLE B's owned field — produced here only]

ROLE B COMPLETE. Both attestation fields on record — open Stage 1.

---

## GATE S

  gate_s_cleared: true              (ROLE B — sole source)
  invariant_registry_confirmed: true    (ROLE A — sole source; covers null-CE + handoff schema)

If either is false or missing: STOP.
If both true: advance to Stage 1.

---

## Stage 1 — Hypothesis

Write: {topic}-hypothesis-{date}.md

Frontmatter:
  topic: {topic}
  date: {date}
  scout_anchor: {topic}-scout-record-{date}.md   [loaded in ROLE B]
  gate_s_cleared: true             [ROLE B — sole source]
  invariant_registry_confirmed: true    [ROLE A — sole source]
  incumbent: [from CAMPAIGN OPEN]
  adversarial_reviewer_type: [from SESSION INVARIANT A]
  ce_score_formula: CE-score = -2 if all null [from SESSION INVARIANT B]
  handoff_schema_locked: true      [schema includes mutual-independence constraints on both
                                    incumbent_defense_closed and co_activation_confirmed]

Body:
  Hypothesis statement: [one sentence — what {topic} does better than the incumbent]
  Basis: [3-5 signals from the scout record]
  Counter-hypothesis: [strongest incumbent rebuttal]

Artifact written: {topic}-hypothesis-{date}.md.
Confirm: "Hypothesis written. Symmetric independence constraints noted in frontmatter.
          Advancing to Stage 2."

---

## Stage 2 — Web Search

Write: {topic}-websearch-{date}.md

Search for external evidence on {topic}. Record: claim, source URL, CE-relevant (yes/no).

NULL RESULT NOTE (if no CE found):
  Stage 2 CE result: NULL
  Running tally: [count] null. [X] evidence stages remain.
  Protocol status: SESSION INVARIANTs A and B remain active — pre-committed obligations.

Artifact written: {topic}-websearch-{date}.md.
Confirm: "Stage 2 complete. CE: [found / NULL]. Advancing to Stage 3."

---

## Stage 3 — Internal Intelligence

Write: {topic}-intelligence-{date}.md

Scan internal sources. Record: artifact path, claim, CE-relevant (yes/no).

NULL RESULT NOTE (if no CE found):
  Stage 3 CE result: NULL
  Running tally: [count] null. [X] stage remains.
  Protocol status: SESSION INVARIANTs A and B remain active — pre-committed obligations.

Artifact written: {topic}-intelligence-{date}.md.
Confirm: "Stage 3 complete. CE: [found / NULL]. Advancing to Stage 4."

---

## Stage 4 — Analysis

Write: {topic}-analysis-{date}.md

Analyze all evidence. Summarize CE state. Qualify hypothesis if CE found; acknowledge
null explicitly if not.

### CAMPAIGN OUTCOME BLOCK

  null_tally_final: [0-3]
  incumbent_defense_closed: [true if null_tally_final = 3; false otherwise]
  derivation: "null_tally_final via formula. NOT derived from dual_lock_fired or
               co_activation_confirmed — both are parallel consumers of null_tally_final."

Artifact written: {topic}-analysis-{date}.md.
Confirm: "Stage 4 complete. Campaign outcome: incumbent_defense_closed = [true/false]."

---

## Stage 5 — Synthesis

Write: {topic}-synthesize-{date}.md

Confirm SESSION INVARIANTs A and B in scope. Retrieve PRE-COMMITTED HANDOFF SCHEMA.

### Findings

3-5 bullet points, each traceable to a specific artifact.

### Counter-Evidence

MANDATORY SECTION. Unconditionally required.
If CE found: list with source and credibility.
If null: record null, list sources checked. Apply adversarial review (SESSION INVARIANT A).
Apply confidence cap (SESSION INVARIANT B).

### ATOMIC DUAL-LOCK (activates if null_tally_final = 3)

  LOCK 1: Adversarial Reviewer (SESSION INVARIANT A) — execution only.
  LOCK 2: Confidence Cap (SESSION INVARIANT B) — CE-score = -2, HIGH blocked.

  dual_lock_fired: [true if null_tally_final = 3, false otherwise]
  co_activation_confirmed: [must equal dual_lock_fired — format error if they differ]

### Confidence Level

  evidence_score: [0-5]
  ce_score: [0 or -2]
  confidence: [LOW/MEDIUM/HIGH — HIGH blocked if ce_score = -2]

### Handoff

SCHEMA COMPLIANCE CHECK — retrieve PRE-COMMITTED HANDOFF SCHEMA from CAMPAIGN OPEN.
Confirm all 9 declared fields with declared derivation sources and independence constraints.
Any mismatch: record "SCHEMA ERROR: {field} — expected: {expected}, actual: {actual}."

DERIVATION ANNOTATION RULE: every field must carry [derived from: X]. Unlabeled = format error.

Write all 9 declared fields:

  scout_anchor: {topic}-scout-record-{date}.md
    [derived from: ROLE B scout load]

  hypothesis: {topic}-hypothesis-{date}.md
    [derived from: Stage 1 artifact write]

  analysis: {topic}-analysis-{date}.md
    [derived from: Stage 4 artifact write]

  null_tally_final: [0-3]
    [derived from: Stage 4 CAMPAIGN OUTCOME BLOCK]

  incumbent_defense_closed: [true if null_tally_final = 3, false otherwise]
    positive_derivation: "null_tally_final via formula null_tally_final >= 3"
    independence_chain: "NOT derived from dual_lock_fired; NOT derived from co_activation_confirmed"
    [derived from: null_tally_final — independence confirmed per CAMPAIGN OPEN schema constraint]

  co_activation_confirmed: [must equal dual_lock_fired]
    positive_derivation: "dual_lock_fired in ATOMIC DUAL-LOCK"
    independence_chain: "NOT derived from incumbent_defense_closed; NOT derived from null_tally_final directly"
    [derived from: dual_lock_fired — independence confirmed per CAMPAIGN OPEN schema constraint]

  confidence: [LOW/MEDIUM/HIGH]
    [derived from: evidence_score + ce_score formula per SESSION INVARIANT B]

  next: topic-story
    [derived from: static handoff target]

  schema_compliance_confirmed: true
    [derived from: synthesis-time compliance check — all 9 fields present with declared
     derivation sources; symmetric independence chains on both campaign-sensitive fields
     confirmed; no additions; no omissions]

Confirm: "Synthesis complete. Symmetric independence chains applied to both
          incumbent_defense_closed and co_activation_confirmed — mutual independence
          proven by enumerated positive_derivation and independence_chain on each field.
          Evidence brief ready for topic-story.
          Artifact written: {topic}-synthesize-{date}.md."
```

---

## V-03 — Axis: Per-Stage Schema Integrity Count

**Variation axis**: Per-stage schema integrity count — each evidence stage (S2, S3, S4)
appends a SCHEMA INTEGRITY NOTE recording the pre-committed field count and confirming no
modifications have been made to the schema since CAMPAIGN OPEN. The note uses explicit count
language: "Schema fields locked: N/N — no additions, no omissions since CAMPAIGN OPEN." This
creates a per-stage audit chain for the schema contract across the collection phase, symmetric
to C-20's per-stage null tally accumulation.

**Hypothesis**: C-26 locks the handoff schema at CAMPAIGN OPEN and verifies compliance at
synthesis. C-20 requires per-stage null tally accumulation — null results recorded with a
running count and protocol reference at each evidence stage, not only at synthesis. By symmetry,
if the schema contract is declared at CAMPAIGN OPEN and checked at synthesis, there is an
unaudited window across the collection phase (Stages 2-4) where schema modifications could
occur without detection until synthesis. A per-stage schema integrity count creates the same
per-stage audit presence for the schema contract that C-20 created for null CE. A session where
both patterns are active enables cross-phase audit of both the evidence quality state and the
schema contract state at each collection checkpoint.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
Campaign opens with two blocking roles. Five evidence stages follow in fixed sequence.
The schema contract and the null tally are both tracked per-stage through the collection phase.

---

## CAMPAIGN OPEN

Fill before any role or stage begins.

  status_quo_comparator: [name the incumbent approach this topic must displace]

NULL COUNTER-EVIDENCE PROTOCOL — session-level invariants:

  SESSION INVARIANT A — Adversarial Reviewer:
    adversarial_reviewer_type: [role most likely to challenge the claim]
    Activation: fires if ALL three evidence stages return null CE.
    Binding: pre-registered — cannot be modified or bypassed.

  SESSION INVARIANT B — Confidence Cap:
    ce_score_formula: CE-score = -2 if all three evidence stages null; 0 otherwise.
    Binding: locked formula — cannot be softened or overridden.

PRE-COMMITTED HANDOFF SCHEMA — session-level invariant, locked now:

Synthesis must produce exactly these 8 fields. No additions. No omissions.
Derivation-source mismatch = format error.

  FIELD                       | REQUIRED DERIVATION SOURCE
  ----------------------------|----------------------------------------------
  scout_anchor                | ROLE B scout load
  hypothesis                  | Stage 1 artifact write
  analysis                    | Stage 4 artifact write
  null_tally_final            | Stage 4 CAMPAIGN OUTCOME BLOCK
  incumbent_defense_closed    | null_tally_final (NOT co_activation_confirmed)
  co_activation_confirmed     | dual_lock_fired in synthesis
  confidence                  | evidence_score + ce_score formula per SESSION INVARIANT B
  next                        | static: "topic-story"

Schema field count at lock: 8. This count is the reference for per-stage integrity checks.

All session invariants are now locked. Do not modify after this point.

---

## ROLE A — INVARIANT REGISTRY LOCK

OWNED ATTESTATION FIELD: invariant_registry_confirmed
Sole producer of this field.

Execute first. Confirm SESSION INVARIANTs A and B and PRE-COMMITTED HANDOFF SCHEMA active.

  invariant_registry_confirmed: true    [ROLE A — produced here only]

Do not begin ROLE B without invariant_registry_confirmed = true.

---

## ROLE B — SCOUT LOAD

OWNED ATTESTATION FIELD: gate_s_cleared
Sole producer of this field.

Locate: {topic}-scout-record-{date}.md
If not found: STOP. "GATE S FAIL — scout record missing."
If found: extract market signal, competitor landscape, feasibility finding.

  gate_s_cleared: true    [ROLE B — produced here only]

Both attestation fields on record — open Stage 1.

---

## GATE S

  gate_s_cleared: true              (ROLE B — sole source)
  invariant_registry_confirmed: true    (ROLE A — sole source)

If either false or missing: STOP.
If both true: advance to Stage 1.

---

## Stage 1 — Hypothesis

Write: {topic}-hypothesis-{date}.md

Frontmatter:
  topic: {topic}
  date: {date}
  scout_anchor: {topic}-scout-record-{date}.md
  gate_s_cleared: true             [ROLE B]
  invariant_registry_confirmed: true    [ROLE A]
  incumbent: [from CAMPAIGN OPEN]
  adversarial_reviewer_type: [from SESSION INVARIANT A]
  ce_score_formula: CE-score = -2 if all null [from SESSION INVARIANT B]
  handoff_schema_locked: true      [8 fields locked — schema field count: 8]

Body: Hypothesis statement, basis (3-5 scout signals), counter-hypothesis.

Confirm: "Hypothesis written: {topic}-hypothesis-{date}.md. Schema field count confirmed: 8.
          Advancing to Stage 2."

---

## Stage 2 — Web Search

Write: {topic}-websearch-{date}.md

Search for external evidence on {topic}. Record: claim, source URL, CE-relevant (yes/no).

After completing evidence search, append both notes:

NULL TALLY NOTE:
  Stage 2 CE result: [found / NULL]
  Running null tally: [count] null. [X] evidence stages remain.
  If NULL: Protocol status — SESSION INVARIANTs A and B active as pre-committed obligations.

SCHEMA INTEGRITY NOTE:
  Schema fields locked: 8/8 — no additions, no omissions since CAMPAIGN OPEN.
  Pre-committed field count unchanged. Schema contract is intact entering Stage 3.

Artifact written: {topic}-websearch-{date}.md.
Confirm: "Stage 2 complete. Null tally: [count]. Schema integrity: 8/8. Advancing to Stage 3."

---

## Stage 3 — Internal Intelligence

Write: {topic}-intelligence-{date}.md

Scan internal sources. Record: artifact path, claim, CE-relevant (yes/no).

After completing evidence scan, append both notes:

NULL TALLY NOTE:
  Stage 3 CE result: [found / NULL]
  Running null tally: [count] null. [X] stage remains.
  If NULL: Protocol status — SESSION INVARIANTs A and B active as pre-committed obligations.

SCHEMA INTEGRITY NOTE:
  Schema fields locked: 8/8 — no additions, no omissions since Stage 2 check.
  Pre-committed field count unchanged. Schema contract is intact entering Stage 4.

Artifact written: {topic}-intelligence-{date}.md.
Confirm: "Stage 3 complete. Null tally: [count]. Schema integrity: 8/8. Advancing to Stage 4."

---

## Stage 4 — Analysis

Write: {topic}-analysis-{date}.md

Analyze all evidence from Stages 2 and 3. Summarize findings and CE state.

### CAMPAIGN OUTCOME BLOCK

  null_tally_final: [0-3 — count of evidence stages returning null CE]
  incumbent_defense_closed: [true if null_tally_final = 3; false otherwise]
  derivation: "null_tally_final via formula. Not derived from co_activation_confirmed."

Schema integrity at Stage 4: 8/8 fields confirmed — schema contract intact at analysis.
This is the third and final per-stage schema check before synthesis.

Artifact written: {topic}-analysis-{date}.md.
Confirm: "Stage 4 complete. Null tally final: [count]. Schema integrity: 8/8 through
          collection phase. Advancing to Stage 5."

---

## Stage 5 — Synthesis

Write: {topic}-synthesize-{date}.md

Confirm SESSION INVARIANTs A and B in scope.
Retrieve PRE-COMMITTED HANDOFF SCHEMA — note: per-stage schema integrity checks at Stages
2, 3, and 4 all confirmed 8/8 fields locked. No modifications entered the collection phase.

### Findings

3-5 bullet points, each traceable to a specific artifact.

### Counter-Evidence

MANDATORY SECTION. Unconditionally required.
If CE found: list with source and credibility.
If null: record null with sources checked. Assign adversarial reviewer (SESSION INVARIANT A).
Apply confidence cap (SESSION INVARIANT B).

### ATOMIC DUAL-LOCK (activates if null_tally_final = 3)

  LOCK 1: Reviewer — {adversarial_reviewer_type} (pre-committed execution only).
  LOCK 2: Confidence cap — CE-score = -2, HIGH blocked.

  dual_lock_fired: [true/false]
  co_activation_confirmed: [must equal dual_lock_fired — format error if they differ]
  Note: co_activation_confirmed and incumbent_defense_closed are parallel consumers
        of null_tally_final. Neither derives the other.

### Confidence Level

  evidence_score: [0-5]
  ce_score: [0 or -2]
  confidence: [LOW/MEDIUM/HIGH — HIGH blocked if ce_score = -2]

### Handoff

SCHEMA COMPLIANCE CHECK — retrieve PRE-COMMITTED HANDOFF SCHEMA. Confirm all 8 fields.
Per-stage schema integrity confirmed 8/8 through Stages 2, 3, and 4 — schema contract
was intact throughout the collection phase. Synthesis compliance confirms end-to-end
schema integrity: collection phase + synthesis output both clean.

DERIVATION ANNOTATION RULE: every field must carry [derived from: X]. Unlabeled = format error.

Write all 8 declared fields:

  scout_anchor: {topic}-scout-record-{date}.md
    [derived from: ROLE B scout load]

  hypothesis: {topic}-hypothesis-{date}.md
    [derived from: Stage 1 artifact write]

  analysis: {topic}-analysis-{date}.md
    [derived from: Stage 4 artifact write]

  null_tally_final: [0-3]
    [derived from: Stage 4 CAMPAIGN OUTCOME BLOCK]

  incumbent_defense_closed: [true if null_tally_final = 3, false otherwise]
    positive_derivation: "null_tally_final via formula null_tally_final >= 3"
    independence_chain: "NOT derived from dual_lock_fired; NOT derived from co_activation_confirmed"
    [derived from: null_tally_final — independence confirmed]

  co_activation_confirmed: [must equal dual_lock_fired]
    [derived from: dual_lock_fired in ATOMIC DUAL-LOCK — NOT from incumbent_defense_closed]

  confidence: [LOW/MEDIUM/HIGH]
    [derived from: evidence_score + ce_score formula per SESSION INVARIANT B]

  next: topic-story
    [derived from: static handoff target]

  schema_compliance_confirmed: true
    [derived from: synthesis-time compliance check — 8/8 fields present with declared
     derivation sources; per-stage integrity confirmed at Stages 2, 3, and 4;
     no additions; no omissions at any phase]

Confirm: "Synthesis complete. Per-stage schema integrity chain verified: 8/8 confirmed
          at Stage 2, Stage 3, and Stage 4 before synthesis. Synthesis compliance confirmed
          (8/8 fields, derivation sources matched).
          Evidence brief ready for topic-story.
          Artifact written: {topic}-synthesize-{date}.md."
```

---

## V-04 — Axis: Annotation Rule Pre-Committed as Session Invariant

**Variation axis**: Annotation rule pre-committed — the DERIVATION ANNOTATION RULE is declared
as SESSION INVARIANT C at CAMPAIGN OPEN, with invariant language: "Every handoff field must
carry a `[derived from: X]` label. Unlabeled field = format error. Pre-registered now — this
is a session obligation, not a synthesis instruction." ROLE A's invariant registry lock covers
all three session invariants (A, B, and C). At synthesis, the rule EXECUTES; it is not
declared — the synthesis instruction references the pre-committed invariant and confirms
execution. C-25 requires the annotation rule at synthesis; SESSION INVARIANT C makes it
a session-level obligation pre-registered before Stage 0.

**Hypothesis**: C-25 requires the DERIVATION ANNOTATION RULE to be declared as an enforcement
clause at synthesis with an explicit consequence for violations. C-19 requires the null-CE
protocol to be declared as a session invariant at CAMPAIGN OPEN with invariant language —
making it a pre-committed obligation rather than a synthesis decision. The same argument
applies to the annotation rule: a rule declared only at synthesis can be suppressed before
Stage 5 without any pre-committed invariant to enforce it. Pre-committing the annotation rule
as SESSION INVARIANT C with invariant language at CAMPAIGN OPEN closes this gap — the
obligation to label all handoff fields is declared before any evidence runs. ROLE A's
registry lock confirms it. A synthesis that omits the annotation rule executes an invariant
(not ignores an instruction), and a GATE S that clears without ROLE A confirming INVARIANT C
is auditable as a gap.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
Three session invariants are pre-committed at CAMPAIGN OPEN. Two blocking roles open the
campaign. Five evidence stages follow in fixed sequence — forward only.

---

## CAMPAIGN OPEN

Fill before any role or stage begins.

  status_quo_comparator: [name the incumbent approach this topic must displace]

SESSION INVARIANTS — locked now before Stage 0:

  SESSION INVARIANT A — Adversarial Reviewer:
    adversarial_reviewer_type: [role most likely to challenge the claim]
    Activation: fires if ALL three evidence stages (S2, S3, S4) return null CE.
    Invariant language: pre-registered — cannot be modified or bypassed at synthesis.

  SESSION INVARIANT B — Confidence Cap:
    ce_score_formula: CE-score = -2 if all three evidence stages null; 0 otherwise.
    Invariant language: locked formula — cannot be softened or overridden at synthesis.

  SESSION INVARIANT C — Derivation Annotation Rule:
    annotation_rule: Every field in the handoff section of the synthesis artifact must
                     carry a [derived from: X] label naming its upstream source.
    enforcement: Unlabeled field = format error. This constraint applies unconditionally
                 to all handoff fields — no exceptions.
    Invariant language: pre-registered now — this is a session obligation, not a synthesis
                        instruction. It cannot be waived or softened at synthesis time.

PRE-COMMITTED HANDOFF SCHEMA — session-level invariant, locked now:

Synthesis must produce exactly these 8 fields with exactly these derivation sources.
No additions. No omissions. Derivation-source mismatch = format error.

  FIELD                       | REQUIRED DERIVATION SOURCE
  ----------------------------|----------------------------------------------
  scout_anchor                | ROLE B scout load
  hypothesis                  | Stage 1 artifact write
  analysis                    | Stage 4 artifact write
  null_tally_final            | Stage 4 CAMPAIGN OUTCOME BLOCK
  incumbent_defense_closed    | null_tally_final (NOT co_activation_confirmed)
  co_activation_confirmed     | dual_lock_fired in synthesis
  confidence                  | evidence_score + ce_score formula per SESSION INVARIANT B
  next                        | static: "topic-story"

All four session invariants (A, B, C, and Handoff Schema) are now locked.
Do not modify after this point.

---

## ROLE A — INVARIANT REGISTRY LOCK

OWNED ATTESTATION FIELD: invariant_registry_confirmed
Sole producer of this field.

Execute first. Confirm all four session invariants are active:
- SESSION INVARIANT A (adversarial reviewer)
- SESSION INVARIANT B (confidence cap)
- SESSION INVARIANT C (derivation annotation rule — every handoff field must be labeled)
- PRE-COMMITTED HANDOFF SCHEMA (8 declared fields)

  invariant_registry_confirmed: true    [ROLE A — produced here only; covers all four invariants]

ROLE A COMPLETE. Do not begin ROLE B without invariant_registry_confirmed = true.

---

## ROLE B — SCOUT LOAD

OWNED ATTESTATION FIELD: gate_s_cleared
Sole producer of this field.

Execute after ROLE A.

Locate: {topic}-scout-record-{date}.md
If not found: STOP. "GATE S FAIL — scout record missing."
If found: load record. Extract: market signal, competitor landscape, feasibility finding.

  gate_s_cleared: true    [ROLE B — produced here only]

Both attestation fields on record — open Stage 1.

---

## GATE S

  gate_s_cleared: true              (ROLE B — sole source)
  invariant_registry_confirmed: true    (ROLE A — sole source; covers all four invariants
                                         including SESSION INVARIANT C annotation rule)

If either false or missing: STOP.
If both true: advance to Stage 1.

Note: GATE S clears only when ROLE A has confirmed SESSION INVARIANT C. A GATE S that
clears without invariant_registry_confirmed = true carries no confirmation that the
annotation obligation is active. Gap is auditable from the GATE S output alone.

---

## Stage 1 — Hypothesis

Write: {topic}-hypothesis-{date}.md

Frontmatter:
  topic: {topic}
  date: {date}
  scout_anchor: {topic}-scout-record-{date}.md
  gate_s_cleared: true             [ROLE B — sole source]
  invariant_registry_confirmed: true    [ROLE A — covers all four invariants including
                                          SESSION INVARIANT C derivation annotation rule]
  incumbent: [from CAMPAIGN OPEN]
  adversarial_reviewer_type: [from SESSION INVARIANT A]
  ce_score_formula: CE-score = -2 if all null [from SESSION INVARIANT B]
  annotation_rule_active: true     [SESSION INVARIANT C locked at CAMPAIGN OPEN — all
                                    handoff fields must carry derivation labels]
  handoff_schema_locked: true      [8 fields locked at CAMPAIGN OPEN]

Body: Hypothesis statement, basis (3-5 scout signals), counter-hypothesis.

Confirm: "Hypothesis written: {topic}-hypothesis-{date}.md. SESSION INVARIANT C confirmed
          in frontmatter — annotation obligation active for full session. Advancing to Stage 2."

---

## Stage 2 — Web Search

Write: {topic}-websearch-{date}.md

Search for external evidence on {topic}. Record: claim, source URL, CE-relevant (yes/no).

NULL RESULT NOTE (if no CE found):
  Stage 2 CE result: NULL
  Running tally: [count] null. [X] evidence stages remain.
  Protocol status: SESSION INVARIANTs A and B active as pre-committed obligations.
  SESSION INVARIANT C status: annotation rule active — applies to synthesis handoff.

Artifact written: {topic}-websearch-{date}.md.
Confirm: "Stage 2 complete. CE: [found / NULL]. Advancing to Stage 3."

---

## Stage 3 — Internal Intelligence

Write: {topic}-intelligence-{date}.md

Scan internal sources. Record: artifact path, claim, CE-relevant (yes/no).

NULL RESULT NOTE (if no CE found):
  Stage 3 CE result: NULL
  Running tally: [count] null. [X] stage remains.
  Protocol status: SESSION INVARIANTs A and B active as pre-committed obligations.
  SESSION INVARIANT C status: annotation rule active — applies to synthesis handoff.

Artifact written: {topic}-intelligence-{date}.md.
Confirm: "Stage 3 complete. CE: [found / NULL]. Advancing to Stage 4."

---

## Stage 4 — Analysis

Write: {topic}-analysis-{date}.md

Analyze all evidence. Summarize findings and CE state.

### CAMPAIGN OUTCOME BLOCK

  null_tally_final: [0-3]
  incumbent_defense_closed: [true if null_tally_final = 3; false otherwise]
  derivation: "null_tally_final via formula. NOT from dual_lock_fired or co_activation_confirmed."

Artifact written: {topic}-analysis-{date}.md.
Confirm: "Stage 4 complete. Campaign outcome: incumbent_defense_closed = [true/false]."

---

## Stage 5 — Synthesis

Write: {topic}-synthesize-{date}.md

Confirm SESSION INVARIANTs A and B in scope.
Confirm PRE-COMMITTED HANDOFF SCHEMA in scope.

EXECUTE SESSION INVARIANT C — DERIVATION ANNOTATION RULE:
This rule was pre-committed at CAMPAIGN OPEN. Execution is required now.
Every field in the Handoff section below must carry a [derived from: X] label.
Unlabeled field = format error per SESSION INVARIANT C pre-committed obligation.
(This is execution of a pre-committed invariant — not a declaration.)

### Findings

3-5 bullet points, each traceable to a specific artifact.

### Counter-Evidence

MANDATORY SECTION. Unconditionally required.
If CE found: list with source and credibility.
If null: record null with sources checked. Assign adversarial reviewer (SESSION INVARIANT A —
execution only). Apply confidence cap (SESSION INVARIANT B — execution only).

### ATOMIC DUAL-LOCK (activates if null_tally_final = 3)

  LOCK 1: Reviewer — {adversarial_reviewer_type} (SESSION INVARIANT A — execution).
  LOCK 2: Cap — CE-score = -2, HIGH blocked (SESSION INVARIANT B — execution).

  dual_lock_fired: [true if null_tally_final = 3, false otherwise]
  co_activation_confirmed: [must equal dual_lock_fired — format error if they differ]

### Confidence Level

  evidence_score: [0-5]
  ce_score: [0 or -2]
  confidence: [LOW/MEDIUM/HIGH — HIGH blocked if ce_score = -2]

### Handoff

SCHEMA COMPLIANCE CHECK — retrieve PRE-COMMITTED HANDOFF SCHEMA. Confirm all 8 fields.

SESSION INVARIANT C EXECUTION — applying derivation annotation rule (pre-committed at
CAMPAIGN OPEN). Every field below carries [derived from: X] per locked obligation.

Write all 8 declared fields:

  scout_anchor: {topic}-scout-record-{date}.md
    [derived from: ROLE B scout load — per SESSION INVARIANT C]

  hypothesis: {topic}-hypothesis-{date}.md
    [derived from: Stage 1 artifact write — per SESSION INVARIANT C]

  analysis: {topic}-analysis-{date}.md
    [derived from: Stage 4 artifact write — per SESSION INVARIANT C]

  null_tally_final: [0-3]
    [derived from: Stage 4 CAMPAIGN OUTCOME BLOCK — per SESSION INVARIANT C]

  incumbent_defense_closed: [true if null_tally_final = 3, false otherwise]
    positive_derivation: "null_tally_final via formula null_tally_final >= 3"
    independence_chain: "NOT derived from dual_lock_fired; NOT derived from co_activation_confirmed"
    [derived from: null_tally_final — per SESSION INVARIANT C; independence confirmed]

  co_activation_confirmed: [must equal dual_lock_fired]
    [derived from: dual_lock_fired in ATOMIC DUAL-LOCK — per SESSION INVARIANT C;
     NOT from incumbent_defense_closed]

  confidence: [LOW/MEDIUM/HIGH]
    [derived from: evidence_score + ce_score formula per SESSION INVARIANT B — per SESSION INVARIANT C]

  next: topic-story
    [derived from: static handoff target — per SESSION INVARIANT C]

  schema_compliance_confirmed: true
    [derived from: synthesis-time compliance check — all 8 declared fields present with
     declared derivation sources; SESSION INVARIANT C executed (all fields labeled);
     no additions; no omissions]

Confirm: "Synthesis complete. SESSION INVARIANT C executed — derivation annotations applied
          to all 8 handoff fields per pre-committed obligation (not a synthesis instruction).
          Schema compliance confirmed (8/8 fields, derivation sources matched).
          Invariant C pre-commitment auditable from CAMPAIGN OPEN block and hypothesis
          frontmatter (annotation_rule_active: true).
          Evidence brief ready for topic-story.
          Artifact written: {topic}-synthesize-{date}.md."
```

---

## V-05 — Axes: All R9 Axes (full compound on R8 V-05 base)

**Variation axes**: All four R9 axes combined on top of the full R8 V-05 architecture:
(1) schema self-registration — `schema_compliance_confirmed` pre-declared as field 9;
(2) symmetric independence chain — both `incumbent_defense_closed` and `co_activation_confirmed`
carry full `positive_derivation` + `independence_chain`;
(3) per-stage schema integrity count — 9/9 confirmed at each evidence stage;
(4) annotation rule pre-committed — SESSION INVARIANT C at CAMPAIGN OPEN with invariant language.

Plus the full R8 V-05 base: role sequence (structural ownership), table output format,
inertia framing (status_quo comparator at every stage), handoff derivation annotations
(all fields labeled), pre-committed handoff schema, and independence path chain on
`incumbent_defense_closed`.

**Hypothesis**: The four R9 axes address distinct structural layers that do not interfere:
V-01 (schema self-registration) locks the compliance-check field as a pre-committed member —
this is consistent with V-03 (per-stage schema integrity count) tracking the field count
including field 9 at each collection stage. V-02 (symmetric independence chain) extends the
field-level independence proof to both campaign-sensitive fields — this is consistent with
V-04 (annotation rule pre-committed) which makes the derivation-label requirement a session
invariant covering all fields. All four patterns reinforce the same goal: audit-chain
completeness from CAMPAIGN OPEN through synthesis, with no phase where an obligation can
be suppressed without leaving a traceable gap.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
The campaign opens with two blocking roles followed by five evidence stages in fixed sequence.
Four session invariants are pre-committed at CAMPAIGN OPEN. Schema contract is self-referential
(field 9 is the compliance-check field, pre-declared). Both campaign-sensitive handoff fields
carry symmetric two-part independence chains. Schema integrity is tracked per-stage.

---

## CAMPAIGN OPEN

Fill before any role or stage begins.

  status_quo_comparator: [name the incumbent approach this topic must displace]

Current approach note: every evidence stage compares {topic} against this comparator.
Thin evidence does not displace an incumbent with an established record.

SESSION INVARIANTS — locked now before Stage 0:

  SESSION INVARIANT A — Adversarial Reviewer:
    adversarial_reviewer_type: [role most likely to challenge the claim]
    Activation: fires if ALL three evidence stages (S2, S3, S4) return null CE.
    Invariant language: pre-registered — cannot be modified or bypassed at synthesis.

  SESSION INVARIANT B — Confidence Cap:
    ce_score_formula: CE-score = -2 if all three evidence stages null; 0 otherwise.
    Invariant language: locked formula — cannot be softened or overridden at synthesis.

  SESSION INVARIANT C — Derivation Annotation Rule:
    annotation_rule: Every field in the synthesis handoff section must carry a
                     [derived from: X] label naming its upstream source.
    enforcement: Unlabeled field = format error per this pre-committed obligation.
    Invariant language: pre-registered now — session obligation, not synthesis instruction.
                        Cannot be waived or softened at synthesis time.

PRE-COMMITTED HANDOFF SCHEMA — session-level invariant, locked now:

Synthesis must produce exactly these 9 fields with exactly these derivation sources.
No additions. No omissions. Derivation-source mismatch = format error.

  FIELD                       | REQUIRED DERIVATION SOURCE
  ----------------------------|------------------------------------------------------
  scout_anchor                | ROLE B scout load
  hypothesis                  | Stage 1 artifact write
  analysis                    | Stage 4 artifact write
  null_tally_final            | Stage 4 INCUMBENT-DEFENSE TABLE
  incumbent_defense_closed    | null_tally_final (NOT dual_lock_fired; NOT co_activation_confirmed)
  co_activation_confirmed     | dual_lock_fired in synthesis (NOT incumbent_defense_closed;
                              |   NOT null_tally_final directly)
  confidence                  | evidence_score + ce_score formula (SESSION INVARIANT B)
  next                        | static: "topic-story"
  schema_compliance_confirmed | synthesis-time compliance check against this CAMPAIGN OPEN schema

Field 9 (schema_compliance_confirmed) is self-registered: pre-declared as a required field
with derivation source locked before Stage 0. Schema field count at lock: 9.
Omitting field 9 from synthesis is a schema violation. Adding a substitute note is an
undeclared-field violation. Both detectable from this block alone.

All session invariants (A, B, C, and Handoff Schema) are now locked.
Do not modify after this point.

---

## ROLE A — INVARIANT REGISTRY LOCK

OWNED ATTESTATION FIELD: invariant_registry_confirmed
Sole producer of this field. Structural ownership declared here.
Dropping ROLE A: invariant_registry_confirmed absent — auditable gap in GATE S manifest.

Execute first. Confirm all four session invariants are active and locked:
- SESSION INVARIANT A (adversarial reviewer — pre-committed)
- SESSION INVARIANT B (confidence cap — locked formula)
- SESSION INVARIANT C (derivation annotation rule — session obligation, not synthesis instruction)
- PRE-COMMITTED HANDOFF SCHEMA (9 fields including self-registered field 9)

  invariant_registry_confirmed: true    [ROLE A — sole producer; covers all four invariants]

ROLE A COMPLETE. Do not begin ROLE B without invariant_registry_confirmed = true.

---

## ROLE B — SCOUT LOAD

OWNED ATTESTATION FIELD: gate_s_cleared
Sole producer of this field. Structural ownership declared here.
Dropping ROLE B: gate_s_cleared absent — auditable gap in GATE S manifest.

Execute after ROLE A.

Locate: {topic}-scout-record-{date}.md
If not found: STOP. "GATE S FAIL — scout record missing. ROLE A invariants locked
but scout prerequisite unmet. Campaign cannot proceed."
If found: load record. Extract: market signal, competitor landscape, feasibility finding,
status_quo evidence (grounding comparator for each evidence stage).

  gate_s_cleared: true    [ROLE B — sole producer]

ROLE B COMPLETE. Both attestation fields on record — open Stage 1.

---

## GATE S

ROLE FIELD MANIFEST:
  | Role   | Owned Field                  | Status |
  |--------|------------------------------|--------|
  | ROLE A | invariant_registry_confirmed | true   |
  | ROLE B | gate_s_cleared               | true   |

Both fields required. Each owned by a structurally distinct role. Loss of either role
creates an auditable gap in this manifest without session replay.

  gate_s_cleared: true              (ROLE B — sole source)
  invariant_registry_confirmed: true    (ROLE A — sole source; covers all four invariants
                                         including SESSION INVARIANT C annotation rule and
                                         self-registered field 9 in handoff schema)

If either false or missing: STOP. Do not open Stage 1.
If both true: advance to Stage 1.

---

## Stage 1 — Hypothesis

Write: {topic}-hypothesis-{date}.md

Frontmatter:
  topic: {topic}
  date: {date}
  scout_anchor: {topic}-scout-record-{date}.md      [loaded in ROLE B]
  gate_s_cleared: true             [ROLE B — sole source]
  invariant_registry_confirmed: true    [ROLE A — sole source; covers all four invariants]
  incumbent: [from status_quo_comparator — CAMPAIGN OPEN]
  adversarial_reviewer_type: [from SESSION INVARIANT A]
  ce_score_formula: CE-score = -2 if all null [from SESSION INVARIANT B]
  annotation_rule_active: true     [SESSION INVARIANT C — pre-committed at CAMPAIGN OPEN;
                                    all synthesis handoff fields must carry derivation labels]
  handoff_schema_locked: true      [9 fields including self-registered field 9 — locked at
                                    CAMPAIGN OPEN; symmetric independence constraints on both
                                    incumbent_defense_closed and co_activation_confirmed]

Body:
  Hypothesis statement: [one sentence — what {topic} does better than the incumbent]
  Incumbent rebuttal: [what the status_quo_comparator claims — grounded in scout record]
  Basis: [3-5 signals from the scout record that support this hypothesis]
  Counter-hypothesis: [strongest incumbent defense]

Artifact written: {topic}-hypothesis-{date}.md.
Confirm: "Hypothesis written. All four session invariants confirmed in frontmatter.
          Self-registered field 9 locked. Symmetric independence schema active.
          SESSION INVARIANT C annotation obligation pre-committed. Advancing to Stage 2."

---

## Stage 2 — Web Search

Write: {topic}-websearch-{date}.md

Search for external evidence on {topic}. For each finding:

| Source | Claim | Supports Hypothesis | CE-Relevant | Incumbent Comparator Coverage | Quote |
|--------|-------|---------------------|-------------|-------------------------------|-------|
| ...    | ...   | yes/no              | yes/no      | yes/no                        | ...   |

Incumbent comparator: [from CAMPAIGN OPEN]. Note any evidence addressing whether the
incumbent has equivalent capability — this is counter-evidence to the hypothesis claim.

After completing evidence search, append both notes:

NULL TALLY NOTE:
  Stage 2 CE result: [found / NULL]
  Running null tally: [count] null. 2 evidence stages remain.
  If NULL: SESSION INVARIANTs A and B active — pre-committed obligations, not synthesis decisions.

SCHEMA INTEGRITY NOTE:
  Schema fields locked: 9/9 — no additions, no omissions since CAMPAIGN OPEN.
  Field 9 (schema_compliance_confirmed) still pre-declared. Symmetric independence constraints
  on incumbent_defense_closed and co_activation_confirmed unchanged.
  Schema contract intact entering Stage 3.

Artifact written: {topic}-websearch-{date}.md.
Confirm: "Stage 2 complete. CE: [found / NULL]. Null tally: [count]. Schema: 9/9. Advancing to Stage 3."

---

## Stage 3 — Internal Intelligence

Write: {topic}-intelligence-{date}.md

Scan internal sources. For each finding:

| Artifact | Claim | Supports Hypothesis | CE-Relevant | Incumbent Comparator Coverage |
|----------|-------|---------------------|-------------|-------------------------------|
| ...      | ...   | yes/no              | yes/no      | yes/no                        |

After completing scan, append both notes:

NULL TALLY NOTE:
  Stage 3 CE result: [found / NULL]
  Running null tally: [count] null. 1 evidence stage remains.
  If NULL: SESSION INVARIANTs A and B active — pre-committed obligations, not synthesis decisions.

SCHEMA INTEGRITY NOTE:
  Schema fields locked: 9/9 — no additions, no omissions since Stage 2 check.
  Field 9 (schema_compliance_confirmed) still pre-declared. Symmetric independence constraints
  unchanged. Schema contract intact entering Stage 4.

Artifact written: {topic}-intelligence-{date}.md.
Confirm: "Stage 3 complete. CE: [found / NULL]. Null tally: [count]. Schema: 9/9. Advancing to Stage 4."

---

## Stage 4 — Analysis

Write: {topic}-analysis-{date}.md

Analyze all evidence from Stages 2 and 3.

Evidence summary table:

| Stage | Evidence Found | CE Found | Incumbent Comparator Row Present |
|-------|---------------|----------|----------------------------------|
| S2    | yes/no        | yes/no   | yes/no                           |
| S3    | yes/no        | yes/no   | yes/no                           |

Supporting evidence assessment vs incumbent: [qualified comparison grounded in scout record].
CE summary: [all CE found, sources, credibility — or null with sources checked].

### INCUMBENT-DEFENSE TABLE (Campaign Outcome)

Compute from evidence tally before synthesis:

  | Stage | CE Result |
  |-------|-----------|
  | S2    | found / NULL |
  | S3    | found / NULL |
  | S4    | (this stage — analysis; CE assessed above) |

  null_tally_final: [0-3 — count of evidence stages returning null CE]
  incumbent_defense_closed: [true if null_tally_final = 3; false otherwise]

  Derivation record:
    positive_derivation: "null_tally_final via formula (null_tally_final >= 3 → true)"
    independence_note: "NOT derived from dual_lock_fired or co_activation_confirmed.
                        Both fields are parallel consumers of null_tally_final. Neither
                        derives the other."

Schema integrity at Stage 4: 9/9 — schema contract intact through full collection phase.
This is the third per-stage schema check. Pre-committed schema unchanged at analysis entry.

Artifact written: {topic}-analysis-{date}.md.
Confirm: "Stage 4 complete. null_tally_final = [count]. incumbent_defense_closed = [true/false].
          Schema: 9/9 through collection phase. Advancing to Stage 5."

---

## Stage 5 — Synthesis

Write: {topic}-synthesize-{date}.md

Confirm SESSION INVARIANTs A and B in scope.
Retrieve PRE-COMMITTED HANDOFF SCHEMA — note: per-stage integrity confirmed 9/9 at Stages
2, 3, and 4. Schema contract was intact throughout the collection phase.

EXECUTE SESSION INVARIANT C — DERIVATION ANNOTATION RULE:
Pre-committed at CAMPAIGN OPEN. Executing now — this is not a declaration.
Every handoff field below must carry [derived from: X]. Unlabeled = format error
per pre-committed obligation. Auditable from CAMPAIGN OPEN and hypothesis frontmatter.

### Findings

3-5 bullet points, each traceable to a specific artifact. Each finding includes
comparison against the incumbent where evidence allows.

### Counter-Evidence

MANDATORY SECTION. Unconditionally required.
If CE was found: list each item with source artifact and credibility rating.
If CE was null: state: "No counter-evidence found. Sources checked: [Stage 2 sources],
[Stage 3 sources]. This null result is the primary risk to the hypothesis. The incumbent
approach has not been credibly challenged by the evidence gathered."

If CE is null:
  - Adversarial review required before any promotion decision.
    Assign: {adversarial_reviewer_type} (SESSION INVARIANT A — execution only, pre-committed).
  - Confidence mechanically capped: CE-score = -2 (SESSION INVARIANT B — execution only).
    This cap cannot be bypassed.

### ATOMIC DUAL-LOCK (activates if null_tally_final = 3)

  LOCK 1 — Adversarial Reviewer (SESSION INVARIANT A):
    Reviewer: {adversarial_reviewer_type}
    Required before any promotion decision. Pre-committed. This is execution.

  LOCK 2 — Confidence Cap (SESSION INVARIANT B):
    ce_score_formula applied: CE-score = -2 (all-null).
    Maximum claim: MEDIUM. HIGH blocked without adversarial input.

  dual_lock_fired: [true if null_tally_final = 3, false otherwise]
  co_activation_confirmed: [must equal dual_lock_fired — format error if they differ]
  Note: co_activation_confirmed and incumbent_defense_closed are parallel consumers of
        null_tally_final. Neither derives the other. Mutual independence confirmed.

### Confidence Level

| Dimension        | Score       | Rule                                           |
|-----------------|-------------|------------------------------------------------|
| evidence_score  | [0-5]       | assessed from Findings                         |
| ce_score        | [0 or -2]   | SESSION INVARIANT B formula                    |
| incumbent_delta | [+/-]       | strength of finding vs status_quo comparator   |
| confidence      | [LOW/MED/HIGH] | HIGH blocked if ce_score = -2              |

### Handoff

SCHEMA COMPLIANCE CHECK — retrieve PRE-COMMITTED HANDOFF SCHEMA from CAMPAIGN OPEN.
Confirm all 9 declared fields — including field 9 (schema_compliance_confirmed) —
will be produced with their declared derivation sources and independence constraints.
Per-stage integrity confirmed 9/9 at Stages 2, 3, and 4. Synthesis compliance
confirms end-to-end schema integrity across collection phase and synthesis output.
Any mismatch: record "SCHEMA ERROR: {field} — expected: {expected}, actual: {actual}."

SESSION INVARIANT C EXECUTION — applying derivation annotation rule (pre-committed,
confirmed in hypothesis frontmatter as annotation_rule_active: true). Every field
below carries [derived from: X] per locked obligation.

Write all 9 declared fields:

  scout_anchor: {topic}-scout-record-{date}.md
    [derived from: ROLE B scout load — per SESSION INVARIANT C]

  hypothesis: {topic}-hypothesis-{date}.md
    [derived from: Stage 1 artifact write — per SESSION INVARIANT C]

  analysis: {topic}-analysis-{date}.md
    [derived from: Stage 4 artifact write — per SESSION INVARIANT C]

  null_tally_final: [0-3]
    [derived from: Stage 4 INCUMBENT-DEFENSE TABLE — per SESSION INVARIANT C]

  incumbent_defense_closed: [true if null_tally_final = 3, false otherwise]
    positive_derivation: "null_tally_final via formula null_tally_final >= 3"
    independence_chain: "NOT derived from dual_lock_fired; NOT derived from co_activation_confirmed"
    [derived from: null_tally_final — per SESSION INVARIANT C; independence confirmed by
     enumerated chain; CAMPAIGN OPEN schema constraint verified]

  co_activation_confirmed: [must equal dual_lock_fired]
    positive_derivation: "dual_lock_fired in ATOMIC DUAL-LOCK"
    independence_chain: "NOT derived from incumbent_defense_closed; NOT derived from null_tally_final directly"
    [derived from: dual_lock_fired — per SESSION INVARIANT C; symmetric independence chain
     confirmed; mutual independence of both campaign-sensitive fields verified]

  confidence: [LOW/MEDIUM/HIGH]
    [derived from: evidence_score + ce_score formula per SESSION INVARIANT B — per SESSION INVARIANT C]

  next: topic-story
    [derived from: static handoff target — per SESSION INVARIANT C]

  schema_compliance_confirmed: true
    [derived from: synthesis-time compliance check against CAMPAIGN OPEN schema —
     per SESSION INVARIANT C; self-registration confirmed (field 9 was pre-declared at
     CAMPAIGN OPEN, not added reactively); all 9 fields present with declared derivation
     sources and independence constraints; per-stage schema integrity confirmed at Stages
     2, 3, and 4; no additions; no omissions at any phase; SESSION INVARIANT C executed
     (all fields labeled); annotation_rule_active: true confirmed in hypothesis frontmatter]

Confirm: "Synthesis complete.
          All four R9 patterns confirmed:
          (1) Schema self-registration: field 9 (schema_compliance_confirmed) was pre-declared
              at CAMPAIGN OPEN, not added reactively. Omitting it would have been a schema
              violation detectable from CAMPAIGN OPEN alone.
          (2) Symmetric independence chains: incumbent_defense_closed and co_activation_confirmed
              both carry positive_derivation + independence_chain. Mutual independence proven
              by enumerated chains — no domain knowledge of dual-lock mechanism required.
          (3) Per-stage schema integrity: 9/9 confirmed at Stage 2, Stage 3, and Stage 4.
              Schema contract auditable across the full collection phase.
          (4) Annotation rule pre-committed: SESSION INVARIANT C executed — not declared —
              at synthesis. Obligation was pre-registered at CAMPAIGN OPEN and confirmed
              in hypothesis frontmatter (annotation_rule_active: true).
          Schema compliance confirmed (9/9 fields, derivation sources matched, all phases clean).
          Evidence brief ready for topic-story.
          Artifact written: {topic}-synthesize-{date}.md."
```

---

## Anchor Designation

**Anchor: V-05.**

V-05 is the full compound: all R8 V-05 axes (role sequence, table format, inertia framing,
handoff derivation annotations, pre-committed handoff schema, independence path chain) plus
all four R9 axes (schema self-registration, symmetric independence chain, per-stage schema
integrity count, annotation rule pre-committed). All 27 v8 criteria are satisfied, and all
four R9 targets are present.

| Criterion | Source in V-05 |
|-----------|----------------|
| C-01 through C-27 | Full v8 stack inherited from R8 V-05 architecture |
| R9 axis 1 (schema self-registration) | schema_compliance_confirmed declared as field 9 in PRE-COMMITTED HANDOFF SCHEMA at CAMPAIGN OPEN with derivation source locked; self-registration confirmed in synthesis |
| R9 axis 2 (symmetric independence chain) | Both incumbent_defense_closed and co_activation_confirmed carry positive_derivation + independence_chain; mutual independence of both campaign-sensitive fields proven by enumerated chains |
| R9 axis 3 (per-stage schema integrity count) | SCHEMA INTEGRITY NOTE at Stages 2, 3, and 4 records "9/9 fields locked — no additions, no omissions since CAMPAIGN OPEN"; third check at Stage 4 before synthesis |
| R9 axis 4 (annotation rule pre-committed) | SESSION INVARIANT C declared at CAMPAIGN OPEN with invariant language; ROLE A registry lock covers all four invariants; annotation_rule_active: true in hypothesis frontmatter; synthesis EXECUTES the rule — does not declare it |

**Stress test for V-05:**

- Drop axis 1 while keeping axes 2-4: schema_compliance_confirmed appears at synthesis as a
  reactive compliance note. C-26 PASS (schema declared, compliance checked). R9 axis 1 FAIL
  (field 9 was not a pre-committed schema member; the compliance check could be suppressed
  without violating the declared schema).

- Drop axis 2 while keeping axes 1, 3-4: co_activation_confirmed carries only
  `[derived from: dual_lock_fired — NOT from incumbent_defense_closed]`. C-27 PASS (chain on
  incumbent_defense_closed present). R9 axis 2 FAIL (reverse path only annotated, not a
  structured two-part chain — positive_derivation and independence_chain fields absent on
  co_activation_confirmed).

- Drop axis 3 while keeping axes 1, 2, 4: null result notes say "Handoff schema locked" but
  no structured count (N/N). C-26 PASS (schema declared and checked at synthesis). R9 axis 3
  FAIL (no per-stage running count — schema contract unauditable at collection-phase stages
  without reading the CAMPAIGN OPEN block and the synthesis simultaneously).

- Drop axis 4 while keeping axes 1-3: DERIVATION ANNOTATION RULE declared at Stage 5 only.
  C-25 PASS (rule declared at synthesis with enforcement clause). R9 axis 4 FAIL (annotation
  obligation is a synthesis instruction — not a SESSION INVARIANT — and carries no pre-committed
  invariant trace at CAMPAIGN OPEN or hypothesis frontmatter).

**Ceiling status under v8:** V-05 achieves 156/156 under the current rubric. All four R9 axes
are candidate criteria for v9 — none is required by any criterion in v8. A v8-compliant
variation can fail all four: schema_compliance_confirmed added reactively (R9 axis 1 gap),
co_activation_confirmed labeled with brief NOT annotation only (R9 axis 2 gap), schema
integrity present only as prose note without running count (R9 axis 3 gap), annotation rule
declared only at synthesis (R9 axis 4 gap).
