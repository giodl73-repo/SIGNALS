---
skill: quest-variate
skill_target: prove-topic
round: R11
date: 2026-03-16
rubric: prove-topic-rubric-v10-2026-03-16.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [inertia_framing, table_dominant_format, lifecycle_emphasis]
  combined: [V-04 (phrasing_register + role_sequence), V-05 (all_four)]
r10_anchor: >
  R10 V-05 satisfies C-01 through C-33 (180/180). It combines CE verdict ownership
  (C-31), counter-hypothesis closure (C-32), and null tally chain echo (C-33) on the
  full v9 stack. All R11 variations build on the complete v10 structural foundation
  and vary presentation axis only — no structural criterion is relaxed.
r11_targets: >
  R10 established the three evidence-chain-integrity patterns (C-31/C-32/C-33).
  R11 explores whether the same structural obligations can be expressed across
  radically different presentation registers while remaining fully v10-compliant.

  (1) Inertia framing: The incumbent is currently named once in CAMPAIGN OPEN and
  referenced incidentally. Making the status-quo comparator a persistent antagonist —
  with its own named block in CAMPAIGN OPEN, a per-stage "incumbent check" prompt,
  and a synthesis framed as "the case against {incumbent}" — tests whether inertia
  awareness can be threaded through all five stages without displacing any structural
  requirement.

  (2) Table-dominant format: Structured metadata (schema, CE verdict ownership,
  per-stage integrity, handoff block) currently mixes table and prose formats.
  Collapsing all structured data into 3-column tables with explicit COLUMN headers
  tests whether the same derivation chain and ownership information compresses cleanly
  without losing auditing clarity.

  (3) Lifecycle emphasis: Stages currently have implicit ENTER/WORK/CLOSE boundaries
  visible only from confirmation lines. Making ENTER and CLOSE explicit labeled
  sub-sections within each stage tests whether stronger phase delineation improves
  campaign trackability without expanding overall prompt length.

  (4) Phrasing register + role sequence: The formal "SESSION INVARIANT" register
  may be replaced by direct second-person imperatives ("Record here:", "You own this
  field:") while keeping all structural obligations intact. Role sequence is surfaced
  as a numbered checklist gate rather than attestation-field blocking.

---

## V-01 — Axis: Inertia Framing

**Variation axis**: The status-quo comparator is elevated to a named antagonist that
appears at every stage as an explicit checkpoint. CAMPAIGN OPEN opens with a dedicated
INCUMBENT THREAT block. Stages 2, 3, and 4 each contain an INCUMBENT CHECK prompt
asking whether the evidence helps displace the named incumbent. Stage 5 frames the
synthesis as "The case against {incumbent}." The counter-hypothesis is explicitly
attributed to the incumbent's voice. Inertia framing is threaded throughout without
displacing any C-01 through C-33 structural requirement.

**Hypothesis**: The incumbent/status-quo comparator is named in CAMPAIGN OPEN (C-06)
but then recedes — stages gather evidence without surfacing the displacement question
at each step. A practitioner running the campaign may gather strong supporting evidence
while never asking "does this evidence help unseat the thing we're trying to replace?"
Threading the incumbent check as a per-stage prompt ensures that inertia is a live
question throughout collection, not just a framing assumption at CAMPAIGN OPEN. The
displacement framing also makes the counter-hypothesis (C-32) feel organic: the
counter_hypothesis field is the incumbent's strongest defense rather than an abstract
rebuttal.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
The campaign builds the case for displacing {status_quo_comparator} with {topic}.
Campaign opens with two blocking roles. Five evidence stages follow in fixed sequence.

---

## CAMPAIGN OPEN

Fill before any role or stage begins.

  status_quo_comparator: [name the incumbent approach this topic must displace]

### INCUMBENT THREAT BLOCK

The incumbent is the entity most likely to resist adoption of {topic}. Every evidence
stage asks: "does this evidence help displace {status_quo_comparator}?" The synthesis
frames the brief as the case against the incumbent.

  incumbent_name: [from status_quo_comparator above]
  incumbent_strength: [one sentence — why the incumbent is currently winning]
  incumbent_vulnerability: [one sentence — where the incumbent is weakest]

SESSION INVARIANTS — locked now before Stage 0:

  SESSION INVARIANT A — Adversarial Reviewer:
    adversarial_reviewer_type: [role most likely to challenge {topic}'s claim against the incumbent]
    Activation: fires if ALL three evidence stages (S2, S3, S4) return null CE.
    Invariant language: pre-registered — cannot be modified or bypassed at synthesis.

  SESSION INVARIANT B — Confidence Cap:
    ce_score_formula: CE-score = -2 if all three evidence stages null; 0 otherwise.
    Invariant language: locked formula — cannot be softened or overridden at synthesis.

  SESSION INVARIANT C — Derivation Annotation:
    annotation_rule: Every handoff field must carry [derived from: X]. Unlabeled field = format error.
    Invariant language: pre-registered — cannot be modified or bypassed at synthesis.

PRE-COMMITTED HANDOFF SCHEMA — session-level invariant, locked now:

Synthesis must produce exactly these 9 fields with exactly these derivation sources.
No additions. No omissions. Derivation-source mismatch = format error.

  FIELD                       | REQUIRED DERIVATION SOURCE
  ----------------------------|------------------------------------------------------
  scout_anchor                | ROLE B scout load
  hypothesis                  | Stage 1 artifact write
  analysis                    | Stage 4 artifact write
  null_tally_final            | Stage 4 CAMPAIGN OUTCOME BLOCK — derived from
                              |   {s2_ce_verdict, s3_ce_verdict, s4_ce_verdict}
  incumbent_defense_closed    | null_tally_final (NOT dual_lock_fired; NOT co_activation_confirmed)
  co_activation_confirmed     | dual_lock_fired in synthesis (NOT incumbent_defense_closed;
                              |   NOT null_tally_final directly)
  confidence                  | evidence_score + ce_score formula per SESSION INVARIANT B
  next                        | static: "topic-story"
  schema_compliance_confirmed | synthesis-time compliance check against this CAMPAIGN OPEN schema

CE VERDICT OWNERSHIP TABLE — locked now:

Each evidence stage is the sole producer of its named verdict field.
The CAMPAIGN OUTCOME BLOCK is the sole consumer of all three fields.

  VERDICT FIELD    | SOLE PRODUCER | PERMISSIBLE VALUES
  -----------------|---------------|--------------------
  s2_ce_verdict    | Stage 2       | found / null
  s3_ce_verdict    | Stage 3       | found / null
  s4_ce_verdict    | Stage 4       | found / null

null_tally_final derivation formula:
  count of {s2_ce_verdict, s3_ce_verdict, s4_ce_verdict} where value = null

COUNTER-HYPOTHESIS CLOSURE RULE — locked now:

The counter_hypothesis declared at Stage 1 is the incumbent's strongest defense.
Stage 5 must resolve it with: REFUTED / PARTIALLY REFUTED / OPEN RISK plus evidence
citation. OPEN RISK reduces confidence one tier from the evidence_score baseline.

NULL TALLY CHAIN RULE — locked now:

Stage 5 ATOMIC DUAL-LOCK must contain a NULL TALLY CHAIN block reconstructing:
  S2: [found/null] → running tally [N]
  S3: [found/null] → running tally [N]
  S4: [found/null] → tally [N] = null_tally_final
Terminal tally must equal null_tally_final from Stage 4. Mismatch = format error.

All invariants, verdict ownership, closure rule, and tally chain rule are now locked.

---

## ROLE A — INVARIANT REGISTRY LOCK

OWNED ATTESTATION FIELD: invariant_registry_confirmed
Sole producer of this field. No other role or stage may produce it.

Execute first. Confirm all SESSION INVARIANTs (A, B, C), PRE-COMMITTED HANDOFF SCHEMA,
CE VERDICT OWNERSHIP TABLE, COUNTER-HYPOTHESIS CLOSURE RULE, and NULL TALLY CHAIN RULE
are active as session invariants.

  invariant_registry_confirmed: true    [ROLE A's owned field — produced here only]

ROLE A COMPLETE. Do not begin ROLE B without invariant_registry_confirmed = true.

---

## ROLE B — SCOUT LOAD

OWNED ATTESTATION FIELD: gate_s_cleared
Sole producer of this field. No other role or stage may produce it.

Execute after ROLE A. Do not begin hypothesis work until this role completes.

Locate: {topic}-scout-record-{date}.md
If not found: STOP. Record: "GATE S FAIL — scout record missing. Campaign cannot proceed."
If found: load record. Extract:
  - market signal
  - competitor landscape (note incumbent {status_quo_comparator} coverage)
  - feasibility finding

  gate_s_cleared: true    [ROLE B's owned field — produced here only]

ROLE B COMPLETE. Both attestation fields on record — open Stage 1.

---

## GATE S

Requires ROLE A and ROLE B both complete.

  gate_s_cleared: true                  (ROLE B — sole source)
  invariant_registry_confirmed: true    (ROLE A — sole source; covers all invariants + rules)

If either field is false or missing: STOP. Do not open Stage 1.
If both fields are true: advance to Stage 1.

---

## Stage 1 — Hypothesis

Write: {topic}-hypothesis-{date}.md

Frontmatter:
  topic: {topic}
  date: {date}
  scout_anchor: {topic}-scout-record-{date}.md   [loaded in ROLE B]
  gate_s_cleared: true                    [ROLE B — sole source]
  invariant_registry_confirmed: true      [ROLE A — sole source; covers all rules]
  incumbent: [from CAMPAIGN OPEN — incumbent_name]
  adversarial_reviewer_type: [from SESSION INVARIANT A]
  ce_score_formula: CE-score = -2 if all null [from SESSION INVARIANT B]
  handoff_schema_locked: true
  counter_hypothesis_closure_rule: active
  null_tally_chain_rule: active

Body:
  Hypothesis statement: [one sentence — what {topic} does better than {incumbent}]
  Basis: [3-5 signals from the scout record; at least one speaks directly to
          {incumbent}'s vulnerability identified in CAMPAIGN OPEN]
  counter_hypothesis: [the incumbent's strongest defense — one sentence spoken in the
                       incumbent's voice; this field creates a Stage 5 resolution obligation]

Artifact written: {topic}-hypothesis-{date}.md.
Confirm: "Hypothesis written. Incumbent antagonist: {incumbent}. Counter-hypothesis declared
          — Stage 5 COUNTER-HYPOTHESIS RESOLUTION obligated. Advancing to Stage 2."

---

## Stage 2 — Web Search

Write: {topic}-websearch-{date}.md

Search for external evidence on {topic}. For each finding, record:
  claim, source URL, CE-relevant (yes/no), quote.

INCUMBENT CHECK:
  For each finding, ask: does this evidence help displace {incumbent}?
  Flag findings that directly address incumbent_strength or incumbent_vulnerability from CAMPAIGN OPEN.
  Note any evidence that strengthens the incumbent's position — this is counter-evidence (CE).

NULL TALLY NOTE:
  s2_ce_verdict: [found / null]    [OWNED FIELD — Stage 2 sole producer; CE VERDICT OWNERSHIP TABLE]
  Running null tally: [count] null. 2 evidence stages remain.
  If null: Protocol status — SESSION INVARIANTs A and B active as pre-committed obligations.

SCHEMA INTEGRITY NOTE:
  Schema fields locked: 9/9 — 0 additions, 0 omissions, 0 source mismatches since CAMPAIGN OPEN.

Artifact written: {topic}-websearch-{date}.md.
Confirm: "Stage 2 complete. s2_ce_verdict: [found/null]. Incumbent displacement signal: [yes/no/partial].
          Schema: 9/9. Advancing to Stage 3."

---

## Stage 3 — Internal Intelligence

Write: {topic}-intelligence-{date}.md

Scan internal sources. For each finding, record:
  artifact path, claim, CE-relevant (yes/no).

INCUMBENT CHECK:
  For each finding, ask: does this evidence help displace {incumbent}?
  Flag any internal artifact that references {incumbent} or directly comparable approaches.

NULL TALLY NOTE:
  s3_ce_verdict: [found / null]    [OWNED FIELD — Stage 3 sole producer; CE VERDICT OWNERSHIP TABLE]
  Running null tally: [count] null. 1 evidence stage remains.
  If null: Protocol status — SESSION INVARIANTs A and B active — pre-committed obligations.

SCHEMA INTEGRITY NOTE:
  Schema fields locked: 9/9 — 0 additions, 0 omissions, 0 source mismatches since Stage 2 check.

Artifact written: {topic}-intelligence-{date}.md.
Confirm: "Stage 3 complete. s3_ce_verdict: [found/null]. Incumbent displacement signal: [yes/no/partial].
          Schema: 9/9. Advancing to Stage 4."

---

## Stage 4 — Analysis

Write: {topic}-analysis-{date}.md

Analyze all evidence from Stages 2 and 3.
  - Supporting evidence strength.
  - Displacement assessment: taken together, does the evidence make a credible case
    for displacing {incumbent}? Rate: STRONG / MODERATE / WEAK.
  - Counter-evidence summary: all CE found, sources, credibility. Does the CE strengthen
    the incumbent's position or merely challenge {topic}'s claims?
  - If CE null: acknowledge explicitly; list all sources checked.

### CAMPAIGN OUTCOME BLOCK

CE VERDICT INPUT — consume owned fields from Stages 2, 3, and current analysis:

  s2_ce_verdict: [found / null]    [produced by Stage 2 — sole source]
  s3_ce_verdict: [found / null]    [produced by Stage 3 — sole source]
  s4_ce_verdict: [found / null]    [produced by Stage 4 analysis — sole source]

Derive from the three named verdict fields:

  null_tally_final: count of {s2_ce_verdict, s3_ce_verdict, s4_ce_verdict} where value = null
    derivation: "count of named verdict fields = null per CE VERDICT OWNERSHIP TABLE formula.
                 NOT derived from dual_lock_fired or co_activation_confirmed."

  incumbent_defense_closed: [true if null_tally_final = 3; false otherwise]
    derivation: "null_tally_final >= 3 → true. NOT derived from dual_lock_fired or co_activation_confirmed."

SCHEMA INTEGRITY NOTE:
  s4_ce_verdict is the final evidence-stage verdict. 9/9 declared fields intact.
  Schema contract confirmed clean through collection phase.

Artifact written: {topic}-analysis-{date}.md.
Confirm: "Stage 4 complete. CE verdicts: s2=[v], s3=[v], s4=[v].
          null_tally_final = [count] (derived from named verdict fields).
          incumbent_defense_closed = [true/false].
          Displacement assessment: [STRONG/MODERATE/WEAK].
          Advancing to Stage 5."

---

## Stage 5 — Synthesis

Write: {topic}-synthesize-{date}.md

Confirm SESSION INVARIANTs A, B, and C are in scope.
Retrieve PRE-COMMITTED HANDOFF SCHEMA, CE VERDICT OWNERSHIP TABLE,
COUNTER-HYPOTHESIS CLOSURE RULE, and NULL TALLY CHAIN RULE from CAMPAIGN OPEN.

### The Case Against {incumbent}

Frame findings as displacement evidence — what does this topic do better than {incumbent}?

3-5 bullet points, each traceable to a specific artifact (path or stage reference).
For each finding, note whether it addresses incumbent_strength, incumbent_vulnerability,
or is neutral to the displacement question.

### COUNTER-HYPOTHESIS RESOLUTION

MANDATORY SECTION — unconditionally required.
The counter_hypothesis is the incumbent's strongest defense, declared at Stage 1.

  counter_hypothesis: [restate from {topic}-hypothesis-{date}.md]

Verdict (choose one):
  [ ] REFUTED — evidence from Stage(s) [X] directly defeats the incumbent's claim:
        [cite specific finding]
  [ ] PARTIALLY REFUTED — evidence weakens but does not eliminate the incumbent's claim:
        [cite finding; state what the incumbent can still credibly argue]
  [ ] OPEN RISK — no evidence gathered addressed the incumbent's claim:
        [state what evidence would be needed; flag as live risk to adoption]

OPEN RISK: reduces confidence one tier from evidence_score baseline (INVARIANT execution).

### Counter-Evidence

MANDATORY SECTION. Counter-evidence is unconditionally required.
If CE found: list each item with source artifact and credibility rating.
If CE null: state: "No counter-evidence found. Sources checked: [Stage 2 sources],
[Stage 3 sources]. This null result is the primary risk to the displacement case."

If CE null: apply SESSION INVARIANT A (adversarial reviewer) and SESSION INVARIANT B
(confidence cap). These are pre-committed obligations — execution, not new decisions.

### ATOMIC DUAL-LOCK (activates if null_tally_final = 3)

NULL TALLY CHAIN (NULL TALLY CHAIN RULE — execution, not declaration):

Load per-stage CE verdicts from Stage 2, Stage 3, and Stage 4 notes. Reconstruct:

  S2: [found / null] → running tally [N]
  S3: [found / null] → running tally [N]
  S4: [found / null] → tally [N] = null_tally_final

Cross-check: chain terminal value must equal null_tally_final from Stage 4 CAMPAIGN OUTCOME BLOCK.
If mismatch: TALLY ERROR — record discrepancy before continuing.

  LOCK 1 — Adversarial Reviewer (SESSION INVARIANT A — execution only):
    Reviewer: {adversarial_reviewer_type}
    Challenge frame: this reviewer represents the incumbent's perspective.
    Required before promotion.

  LOCK 2 — Confidence Cap (SESSION INVARIANT B — execution only):
    CE-score = -2 (all-null formula). Maximum claim: MEDIUM. HIGH blocked.

  dual_lock_fired: [true if null_tally_final = 3, false otherwise]
  co_activation_confirmed: [must equal dual_lock_fired — format error if they differ]

### Confidence Level

  evidence_score: [0-5]
  ce_score: [0 or -2 per SESSION INVARIANT B]
  counter_hypothesis_verdict: [REFUTED / PARTIALLY REFUTED / OPEN RISK]
  displacement_rating: [STRONG / MODERATE / WEAK — from Stage 4 analysis]
  confidence: [LOW / MEDIUM / HIGH — HIGH blocked if ce_score = -2;
               OPEN RISK counter_hypothesis_verdict reduces one tier from evidence_score baseline]

### Handoff

SCHEMA COMPLIANCE CHECK — retrieve PRE-COMMITTED HANDOFF SCHEMA from CAMPAIGN OPEN.
Confirm all 9 declared fields with declared derivation sources.
Any mismatch: record "SCHEMA ERROR: {field} — expected: {expected}, actual: {actual}."

DERIVATION ANNOTATION RULE (SESSION INVARIANT C — execution): every field must carry
[derived from: X]. Unlabeled field = format error. Executing invariant, not declaring it.

Write all 9 declared fields:

  scout_anchor: {topic}-scout-record-{date}.md
    [derived from: ROLE B scout load]

  hypothesis: {topic}-hypothesis-{date}.md
    [derived from: Stage 1 artifact write — includes incumbent framing and counter_hypothesis]

  analysis: {topic}-analysis-{date}.md
    [derived from: Stage 4 artifact write]

  null_tally_final: [0-3]
    positive_derivation: "count of {s2_ce_verdict, s3_ce_verdict, s4_ce_verdict} = null
                          per CE VERDICT OWNERSHIP TABLE formula"
    independence_chain: "NOT derived from dual_lock_fired; NOT derived from co_activation_confirmed"
    [derived from: Stage 4 CAMPAIGN OUTCOME BLOCK — CE verdict fields as declared inputs;
     tally chain cross-checked above in ATOMIC DUAL-LOCK]

  incumbent_defense_closed: [true if null_tally_final = 3, false otherwise]
    positive_derivation: "null_tally_final via formula null_tally_final >= 3"
    independence_chain: "NOT derived from dual_lock_fired; NOT derived from co_activation_confirmed"
    [derived from: null_tally_final — independence confirmed per CAMPAIGN OPEN schema constraint]

  co_activation_confirmed: [must equal dual_lock_fired]
    positive_derivation: "dual_lock_fired in ATOMIC DUAL-LOCK"
    independence_chain: "NOT derived from incumbent_defense_closed; NOT derived from null_tally_final directly"
    [derived from: dual_lock_fired — independence confirmed per CAMPAIGN OPEN schema constraint]

  confidence: [LOW/MEDIUM/HIGH]
    [derived from: evidence_score + ce_score per SESSION INVARIANT B + counter_hypothesis_verdict adjustment]

  next: topic-story
    [derived from: static handoff target]

  schema_compliance_confirmed: true
    [derived from: synthesis-time compliance check — 9 fields present with declared
     derivation sources; CE VERDICT OWNERSHIP TABLE formula confirmed as null_tally_final
     chain; counter_hypothesis resolution completed; null tally chain echoed and cross-checked;
     no additions; no omissions; SESSION INVARIANT C executed]

Confirm: "Synthesis complete. The case against {incumbent}: [confidence] confidence.
          Counter-hypothesis verdict: [verdict]. null_tally_final: [count]
          (CE chain: S2=[v] → S3=[v] → S4=[v]).
          Evidence brief ready for topic-story.
          Artifact written: {topic}-synthesize-{date}.md."
```

---

## V-02 — Axis: Output Format (Table-Dominant)

**Variation axis**: All structured metadata uses 3-column tables throughout. The
PRE-COMMITTED HANDOFF SCHEMA, CE VERDICT OWNERSHIP TABLE, per-stage notes, ATOMIC
DUAL-LOCK activation state, and handoff block all render as tables with explicit column
headers. Prose description is reserved for non-tabular obligations (hypothesis body,
findings bullets, counter-evidence list). This tests whether the v10 structural
requirements compress cleanly into table format without losing auditing clarity.

**Hypothesis**: The v10 structure mixes table and prose formats — the handoff schema
is a table, but per-stage integrity notes are prose sentences, the ATOMIC DUAL-LOCK
fields are indented key-value pairs, and the handoff block mixes prose and indentation.
A fully table-dominant format places every structured data element in a named-column
table, making column-by-column auditing possible without reading prose for structural
conformance. Derivation sources, verdict fields, and compliance checks all have the
same visual grammar, reducing the cognitive load of cross-checking the chain.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
Campaign opens with two blocking roles. Five evidence stages follow in fixed sequence.
All structured data renders as tables with explicit column headers.

---

## CAMPAIGN OPEN

| FIELD                   | VALUE                                                     |
|-------------------------|-----------------------------------------------------------|
| status_quo_comparator   | [name the incumbent approach this topic must displace]    |

### SESSION INVARIANTS

| INVARIANT | RULE                                                                        | STATUS   |
|-----------|-----------------------------------------------------------------------------|----------|
| A         | adversarial_reviewer_type: [role most likely to challenge the claim].       | LOCKED   |
|           | Fires if ALL three evidence stages return null CE.                          |          |
|           | Cannot be modified or bypassed at synthesis.                                |          |
| B         | ce_score_formula: CE-score = -2 if all three stages null; 0 otherwise.      | LOCKED   |
|           | Cannot be softened or overridden at synthesis.                              |          |
| C         | annotation_rule: Every handoff field must carry [derived from: X].          | LOCKED   |
|           | Unlabeled field = format error. Cannot be modified or bypassed at synthesis.| |

### PRE-COMMITTED HANDOFF SCHEMA

| # | FIELD                    | REQUIRED DERIVATION SOURCE                                              |
|---|--------------------------|-------------------------------------------------------------------------|
| 1 | scout_anchor             | ROLE B scout load                                                       |
| 2 | hypothesis               | Stage 1 artifact write                                                  |
| 3 | analysis                 | Stage 4 artifact write                                                  |
| 4 | null_tally_final         | Stage 4 CAMPAIGN OUTCOME BLOCK — derived from {s2, s3, s4}_ce_verdict  |
| 5 | incumbent_defense_closed | null_tally_final (NOT dual_lock_fired; NOT co_activation_confirmed)     |
| 6 | co_activation_confirmed  | dual_lock_fired (NOT incumbent_defense_closed; NOT null_tally_final)    |
| 7 | confidence               | evidence_score + ce_score formula per SESSION INVARIANT B               |
| 8 | next                     | static: "topic-story"                                                   |
| 9 | schema_compliance_confirmed | synthesis-time compliance check against this schema                  |

Schema is a session-level invariant. No additions. No omissions. Source mismatch = format error.

### CE VERDICT OWNERSHIP TABLE

| VERDICT FIELD  | SOLE PRODUCER | PERMISSIBLE VALUES | CONSUMER                    |
|----------------|---------------|--------------------|-----------------------------|
| s2_ce_verdict  | Stage 2       | found / null       | Stage 4 CAMPAIGN OUTCOME BLOCK |
| s3_ce_verdict  | Stage 3       | found / null       | Stage 4 CAMPAIGN OUTCOME BLOCK |
| s4_ce_verdict  | Stage 4       | found / null       | Stage 4 CAMPAIGN OUTCOME BLOCK |

null_tally_final derivation formula:
  count of {s2_ce_verdict, s3_ce_verdict, s4_ce_verdict} where value = null

COUNTER-HYPOTHESIS CLOSURE RULE — locked now:
The counter_hypothesis field at Stage 1 creates a Stage 5 resolution obligation.
Stage 5 must produce COUNTER-HYPOTHESIS RESOLUTION with verdict: REFUTED / PARTIALLY REFUTED / OPEN RISK.
OPEN RISK reduces confidence one tier from evidence_score baseline.

NULL TALLY CHAIN RULE — locked now:
Stage 5 ATOMIC DUAL-LOCK must contain NULL TALLY CHAIN:
  S2 → tally N | S3 → tally N | S4 → tally N = null_tally_final
Terminal tally must match null_tally_final from Stage 4. Mismatch = format error.

All invariants and rules locked. Do not modify.

---

## ROLE A — INVARIANT REGISTRY LOCK

OWNED ATTESTATION FIELD: invariant_registry_confirmed (sole producer — no other role or stage)

Confirm all SESSION INVARIANTs, PRE-COMMITTED HANDOFF SCHEMA, CE VERDICT OWNERSHIP TABLE,
COUNTER-HYPOTHESIS CLOSURE RULE, and NULL TALLY CHAIN RULE are active.

| FIELD                        | VALUE | PRODUCER |
|------------------------------|-------|----------|
| invariant_registry_confirmed | true  | ROLE A   |

ROLE A COMPLETE. Do not begin ROLE B without invariant_registry_confirmed = true.

---

## ROLE B — SCOUT LOAD

OWNED ATTESTATION FIELD: gate_s_cleared (sole producer — no other role or stage)

Execute after ROLE A. Locate: {topic}-scout-record-{date}.md
If not found: STOP — "GATE S FAIL — scout record missing."
If found: load. Extract: market signal, competitor landscape, feasibility finding.

| FIELD          | VALUE | PRODUCER |
|----------------|-------|----------|
| gate_s_cleared | true  | ROLE B   |

ROLE B COMPLETE. Both attestation fields on record — open Stage 1.

---

## GATE S

| FIELD                        | VALUE | SOLE SOURCE | COVERS                              |
|------------------------------|-------|-------------|-------------------------------------|
| gate_s_cleared               | true  | ROLE B      | scout load confirmed                |
| invariant_registry_confirmed | true  | ROLE A      | all invariants + rules active       |

If either field false or missing: STOP. If both true: advance to Stage 1.

---

## Stage 1 — Hypothesis

Write: {topic}-hypothesis-{date}.md

| FRONTMATTER FIELD             | VALUE / SOURCE                                          |
|-------------------------------|---------------------------------------------------------|
| topic                         | {topic}                                                 |
| date                          | {date}                                                  |
| scout_anchor                  | {topic}-scout-record-{date}.md [ROLE B]                 |
| gate_s_cleared                | true [ROLE B sole source]                               |
| invariant_registry_confirmed  | true [ROLE A sole source; covers all invariants + rules]|
| incumbent                     | [from status_quo_comparator — CAMPAIGN OPEN]            |
| adversarial_reviewer_type     | [from SESSION INVARIANT A — CAMPAIGN OPEN]              |
| ce_score_formula              | CE-score = -2 if all null [SESSION INVARIANT B]         |
| handoff_schema_locked         | true [9 fields; null_tally_final from CE verdict fields]|
| counter_hypothesis_rule       | active [Stage 5 resolution obligated]                   |
| null_tally_chain_rule         | active [Stage 5 chain echo obligated]                   |

Body:
  Hypothesis statement: [one sentence — what {topic} does better than the incumbent]
  Basis: [3-5 signals from the scout record]
  counter_hypothesis: [strongest incumbent rebuttal — one sentence; Stage 5 obligation]

Artifact written: {topic}-hypothesis-{date}.md.
Confirm: "Stage 1 complete. counter_hypothesis declared. CE verdict fields pre-assigned to Stages 2/3/4. Advancing to Stage 2."

---

## Stage 2 — Web Search

Write: {topic}-websearch-{date}.md

Search for external evidence on {topic}. For each finding:

| FINDING | SOURCE URL | CE-RELEVANT | QUOTE |
|---------|------------|-------------|-------|
| [claim] | [url]      | yes / no    | [excerpt] |

Stage close:

| NOTE TYPE       | FIELD           | VALUE                         | RULE                              |
|-----------------|-----------------|-------------------------------|-----------------------------------|
| CE VERDICT      | s2_ce_verdict   | [found / null]                | OWNED — Stage 2 sole producer     |
| NULL TALLY      | running count   | [N] null; 2 stages remain     | INVARIANT A+B active if null      |
| SCHEMA INTEGRITY| fields locked   | 9/9 — 0 additions, 0 omissions| 0 source mismatches since OPEN    |

Artifact written: {topic}-websearch-{date}.md.
Confirm: "Stage 2 complete. s2_ce_verdict: [found/null]. Schema: 9/9. Advancing to Stage 3."

---

## Stage 3 — Internal Intelligence

Write: {topic}-intelligence-{date}.md

Scan internal sources. For each finding:

| ARTIFACT PATH | CLAIM | CE-RELEVANT |
|---------------|-------|-------------|
| [path]        | [claim] | yes / no  |

Stage close:

| NOTE TYPE       | FIELD           | VALUE                         | RULE                              |
|-----------------|-----------------|-------------------------------|-----------------------------------|
| CE VERDICT      | s3_ce_verdict   | [found / null]                | OWNED — Stage 3 sole producer     |
| NULL TALLY      | running count   | [N] null; 1 stage remains     | INVARIANT A+B active if null      |
| SCHEMA INTEGRITY| fields locked   | 9/9 — 0 additions, 0 omissions| 0 source mismatches since Stage 2 |

Artifact written: {topic}-intelligence-{date}.md.
Confirm: "Stage 3 complete. s3_ce_verdict: [found/null]. Schema: 9/9. Advancing to Stage 4."

---

## Stage 4 — Analysis

Write: {topic}-analysis-{date}.md

Supporting evidence strength: [prose]
Counter-evidence summary: [prose or null acknowledgment]

### CAMPAIGN OUTCOME BLOCK

| VERDICT FIELD         | VALUE          | SOLE SOURCE | NOTE                                         |
|-----------------------|----------------|-------------|----------------------------------------------|
| s2_ce_verdict         | [found / null] | Stage 2     | consumed here only                           |
| s3_ce_verdict         | [found / null] | Stage 3     | consumed here only                           |
| s4_ce_verdict         | [found / null] | Stage 4     | OWNED — Stage 4 sole producer                |

| DERIVED FIELD            | VALUE            | DERIVATION FORMULA                                          |
|--------------------------|------------------|-------------------------------------------------------------|
| null_tally_final         | [0-3]            | count of {s2, s3, s4}_ce_verdict = null (CE OWNERSHIP TABLE formula) |
| incumbent_defense_closed | [true / false]   | null_tally_final >= 3; NOT dual_lock_fired; NOT co_activation_confirmed |

| NOTE TYPE       | VALUE                                                          |
|-----------------|----------------------------------------------------------------|
| SCHEMA INTEGRITY| 9/9 fields intact. Schema contract confirmed through collection.|

Artifact written: {topic}-analysis-{date}.md.
Confirm: "Stage 4 complete. CE verdicts: s2=[v], s3=[v], s4=[v]. null_tally_final=[count]. Advancing to Stage 5."

---

## Stage 5 — Synthesis

Write: {topic}-synthesize-{date}.md

Retrieve all locked rules from CAMPAIGN OPEN: SESSION INVARIANTs A/B/C, PRE-COMMITTED HANDOFF SCHEMA,
CE VERDICT OWNERSHIP TABLE, COUNTER-HYPOTHESIS CLOSURE RULE, NULL TALLY CHAIN RULE.

### Findings

3-5 bullet points, each traceable to a specific artifact (path or stage reference).

### COUNTER-HYPOTHESIS RESOLUTION

MANDATORY — unconditionally required.

| FIELD                | VALUE                                             |
|----------------------|---------------------------------------------------|
| counter_hypothesis   | [restate from {topic}-hypothesis-{date}.md]       |
| verdict              | REFUTED / PARTIALLY REFUTED / OPEN RISK           |
| evidence_citation    | [cite Stage 2, 3, or 4 artifact with finding]     |
| confidence_impact    | OPEN RISK: -1 tier from evidence_score baseline   |

### Counter-Evidence

MANDATORY — unconditionally required.
If found: list with source and credibility rating.
If null: "No CE found. Sources checked: [Stage 2], [Stage 3]. This is the primary risk."
If null: apply SESSION INVARIANT A (adversarial reviewer) and B (confidence cap) — execution only.

### ATOMIC DUAL-LOCK (activates if null_tally_final = 3)

NULL TALLY CHAIN (NULL TALLY CHAIN RULE — execution, not declaration):

| STAGE | CE VERDICT     | RUNNING TALLY |
|-------|----------------|---------------|
| S2    | [found / null] | [N]           |
| S3    | [found / null] | [N]           |
| S4    | [found / null] | [N] = null_tally_final |

Cross-check: chain terminal = Stage 4 null_tally_final. Mismatch → TALLY ERROR.

| LOCK   | FIELD                    | VALUE / RULE                                    |
|--------|--------------------------|-------------------------------------------------|
| LOCK 1 | adversarial_reviewer     | {adversarial_reviewer_type} [SESSION INV A]     |
| LOCK 2 | ce_score                 | -2 (all-null formula) [SESSION INV B]            |
| STATE  | dual_lock_fired          | [true if null_tally_final = 3, else false]      |
| STATE  | co_activation_confirmed  | [must equal dual_lock_fired — error if differ]  |

### Confidence Level

| FIELD                        | VALUE                                                    |
|------------------------------|----------------------------------------------------------|
| evidence_score               | [0-5]                                                    |
| ce_score                     | [0 or -2 per SESSION INVARIANT B]                        |
| counter_hypothesis_verdict   | [REFUTED / PARTIALLY REFUTED / OPEN RISK]               |
| confidence                   | [LOW / MEDIUM / HIGH — HIGH blocked if ce_score = -2;    |
|                              |  OPEN RISK reduces one tier from evidence_score baseline]|

### Handoff

SCHEMA COMPLIANCE CHECK — confirm all 9 PRE-COMMITTED HANDOFF SCHEMA fields.
DERIVATION ANNOTATION RULE (SESSION INVARIANT C — execution): every field carries [derived from: X].

| # | FIELD                    | VALUE              | DERIVATION                                                   |
|---|--------------------------|--------------------|--------------------------------------------------------------|
| 1 | scout_anchor             | {topic}-scout-record-{date}.md | [derived from: ROLE B scout load]              |
| 2 | hypothesis               | {topic}-hypothesis-{date}.md   | [derived from: Stage 1 artifact write]         |
| 3 | analysis                 | {topic}-analysis-{date}.md     | [derived from: Stage 4 artifact write]         |
| 4 | null_tally_final         | [0-3]              | positive: count of {s2,s3,s4}_ce_verdict=null per CE OWNERSHIP formula; independence: NOT dual_lock_fired; NOT co_activation_confirmed; [derived from: Stage 4 CAMPAIGN OUTCOME BLOCK] |
| 5 | incumbent_defense_closed | [true/false]       | positive: null_tally_final >= 3; independence: NOT dual_lock_fired; NOT co_activation_confirmed; [derived from: null_tally_final] |
| 6 | co_activation_confirmed  | [equals dual_lock_fired] | positive: dual_lock_fired in ATOMIC DUAL-LOCK; independence: NOT incumbent_defense_closed; NOT null_tally_final directly; [derived from: dual_lock_fired] |
| 7 | confidence               | [LOW/MEDIUM/HIGH]  | [derived from: evidence_score + ce_score + counter_hypothesis_verdict adjustment] |
| 8 | next                     | topic-story        | [derived from: static handoff target]                        |
| 9 | schema_compliance_confirmed | true            | [derived from: synthesis-time check — 9/9 fields; CE chain; counter-hypothesis closed; tally chain echoed; INV C executed] |

Confirm: "Synthesis complete. CE tally chain: S2=[v]→S3=[v]→S4=[v]=null_tally_final=[count].
          Counter-hypothesis: [verdict]. Confidence: [level].
          Evidence brief ready for topic-story. Artifact written: {topic}-synthesize-{date}.md."
```

---

## V-03 — Axis: Lifecycle Emphasis (ENTER / WORK / CLOSE Sub-Sections)

**Variation axis**: Each evidence stage is divided into three explicit sub-sections:
ENTER (verify gate conditions, load inputs, confirm inherited state), WORK (the actual
evidence-gathering task), and CLOSE (record owned verdict field, null tally, schema
integrity count, issue confirmation). Phase boundaries are labeled rather than implied
from confirmation lines. The CAMPAIGN OPEN also gains an explicit LOCK phase. This
tests whether stronger stage delineation helps practitioners track campaign position
without restructuring the underlying evidence obligations.

**Hypothesis**: In the current format, a practitioner running a stage can conflate
entry conditions (gate passed? invariants in scope?) with the stage's actual work, and
can defer the owned verdict recording until after the confirmation line. Making ENTER,
WORK, and CLOSE explicit sub-sections enforces that gate verification happens before
work begins and that owned verdict recording happens before the confirmation fires.
This is the prove-campaign analog to a structured transaction: BEGIN (assert
preconditions), WORK (perform the operation), COMMIT (record the result). The structure
does not add new obligations — it sequences existing obligations unambiguously.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
Campaign opens with two blocking roles. Five evidence stages follow in fixed sequence.
Each stage has three explicit sub-sections: ENTER, WORK, and CLOSE.

---

## CAMPAIGN OPEN

### OPEN: FILL

  status_quo_comparator: [name the incumbent approach this topic must displace]

### OPEN: INVARIANTS

  SESSION INVARIANT A — Adversarial Reviewer:
    adversarial_reviewer_type: [role most likely to challenge the claim]
    Activation: fires if ALL three evidence stages (S2, S3, S4) return null CE.
    Invariant language: pre-registered — cannot be modified or bypassed at synthesis.

  SESSION INVARIANT B — Confidence Cap:
    ce_score_formula: CE-score = -2 if all three evidence stages null; 0 otherwise.
    Invariant language: locked formula — cannot be softened or overridden at synthesis.

  SESSION INVARIANT C — Derivation Annotation:
    annotation_rule: Every handoff field must carry [derived from: X]. Unlabeled field = format error.
    Invariant language: pre-registered — cannot be modified or bypassed at synthesis.

### OPEN: SCHEMA

PRE-COMMITTED HANDOFF SCHEMA — session-level invariant:

  FIELD                       | REQUIRED DERIVATION SOURCE
  ----------------------------|------------------------------------------------------
  scout_anchor                | ROLE B scout load
  hypothesis                  | Stage 1 artifact write
  analysis                    | Stage 4 artifact write
  null_tally_final            | Stage 4 CAMPAIGN OUTCOME BLOCK — derived from
                              |   {s2_ce_verdict, s3_ce_verdict, s4_ce_verdict}
  incumbent_defense_closed    | null_tally_final (NOT dual_lock_fired; NOT co_activation_confirmed)
  co_activation_confirmed     | dual_lock_fired (NOT incumbent_defense_closed;
                              |   NOT null_tally_final directly)
  confidence                  | evidence_score + ce_score per SESSION INVARIANT B
  next                        | static: "topic-story"
  schema_compliance_confirmed | synthesis-time compliance check against this schema

### OPEN: CE VERDICT OWNERSHIP

  VERDICT FIELD    | SOLE PRODUCER | PERMISSIBLE VALUES
  -----------------|---------------|--------------------
  s2_ce_verdict    | Stage 2       | found / null
  s3_ce_verdict    | Stage 3       | found / null
  s4_ce_verdict    | Stage 4       | found / null

null_tally_final derivation formula:
  count of {s2_ce_verdict, s3_ce_verdict, s4_ce_verdict} where value = null

### OPEN: CLOSURE RULES

  COUNTER-HYPOTHESIS CLOSURE RULE:
    counter_hypothesis declared at Stage 1 obligates Stage 5 COUNTER-HYPOTHESIS RESOLUTION.
    Verdict options: REFUTED / PARTIALLY REFUTED / OPEN RISK.
    OPEN RISK: reduces confidence one tier from evidence_score baseline.

  NULL TALLY CHAIN RULE:
    Stage 5 ATOMIC DUAL-LOCK must contain NULL TALLY CHAIN:
      S2: [found/null] → tally [N] | S3: [found/null] → tally [N] | S4: [found/null] → tally [N] = null_tally_final
    Terminal tally must match null_tally_final from Stage 4. Mismatch = format error.

### OPEN: LOCK

All invariants, ownership table, and closure rules are now locked. Do not modify.

---

## ROLE A — INVARIANT REGISTRY LOCK

OWNED ATTESTATION FIELD: invariant_registry_confirmed
Sole producer of this field. No other role or stage may produce it.

Execute first. Confirm all OPEN sections (invariants, schema, CE verdict ownership,
counter-hypothesis closure rule, null tally chain rule) are active as session invariants.

  invariant_registry_confirmed: true    [ROLE A — sole source]

ROLE A COMPLETE. Do not begin ROLE B without invariant_registry_confirmed = true.

---

## ROLE B — SCOUT LOAD

OWNED ATTESTATION FIELD: gate_s_cleared
Sole producer of this field. No other role or stage may produce it.

Execute after ROLE A. Locate: {topic}-scout-record-{date}.md
If not found: STOP — "GATE S FAIL — scout record missing."
If found: load. Extract: market signal, competitor landscape, feasibility finding.

  gate_s_cleared: true    [ROLE B — sole source]

ROLE B COMPLETE. Both attestation fields on record.

---

## GATE S

  gate_s_cleared: true                  (ROLE B — sole source)
  invariant_registry_confirmed: true    (ROLE A — sole source)

If either false or missing: STOP. If both true: advance to Stage 1.

---

## Stage 1 — Hypothesis

### ENTER

  Verify: gate_s_cleared = true [ROLE B sole source]
  Verify: invariant_registry_confirmed = true [ROLE A sole source]
  Load: {topic}-scout-record-{date}.md (extracted by ROLE B)
  Confirm: counter_hypothesis_closure_rule and null_tally_chain_rule active

### WORK

Write: {topic}-hypothesis-{date}.md

  Frontmatter:
    topic: {topic}
    date: {date}
    scout_anchor: {topic}-scout-record-{date}.md   [ROLE B]
    gate_s_cleared: true                    [ROLE B — sole source]
    invariant_registry_confirmed: true      [ROLE A — sole source; covers all rules]
    incumbent: [from CAMPAIGN OPEN]
    adversarial_reviewer_type: [from SESSION INVARIANT A]
    ce_score_formula: CE-score = -2 if all null [SESSION INVARIANT B]
    handoff_schema_locked: true

  Body:
    Hypothesis statement: [one sentence — what {topic} does better than the incumbent]
    Basis: [3-5 signals from the scout record]
    counter_hypothesis: [strongest incumbent rebuttal — one sentence;
                         creates Stage 5 COUNTER-HYPOTHESIS RESOLUTION obligation]

### CLOSE

  Artifact written: {topic}-hypothesis-{date}.md
  counter_hypothesis declared: [yes] — Stage 5 resolution obligated
  CE verdict fields pre-assigned to their respective stages per CE VERDICT OWNERSHIP TABLE
  Confirm: "Stage 1 closed. counter_hypothesis on record. Advancing to Stage 2."

---

## Stage 2 — Web Search

### ENTER

  Verify: {topic}-hypothesis-{date}.md written [Stage 1 CLOSE]
  Load: incumbent from CAMPAIGN OPEN — note for CE relevance assessment
  Confirm: s2_ce_verdict is this stage's owned field

### WORK

Write: {topic}-websearch-{date}.md

  Search for external evidence on {topic}. For each finding:
    claim, source URL, CE-relevant (yes/no), quote.
  Incumbent comparator: [from CAMPAIGN OPEN]. Note evidence addressing whether incumbent
  has equivalent capability — this is CE for the hypothesis.

### CLOSE

  VERDICT (OWNED FIELD — Stage 2 sole producer):
    s2_ce_verdict: [found / null]    [produced here; consumed only by Stage 4 CAMPAIGN OUTCOME BLOCK]

  NULL TALLY NOTE:
    Running null tally: [count] null. 2 evidence stages remain.
    If null: SESSION INVARIANTs A and B active as pre-committed obligations.

  SCHEMA INTEGRITY NOTE:
    Schema fields locked: 9/9 — 0 additions, 0 omissions, 0 source mismatches since CAMPAIGN OPEN.

  Artifact written: {topic}-websearch-{date}.md
  Confirm: "Stage 2 closed. s2_ce_verdict: [found/null]. Tally: [N]. Schema: 9/9. Advancing to Stage 3."

---

## Stage 3 — Internal Intelligence

### ENTER

  Verify: {topic}-websearch-{date}.md written [Stage 2 CLOSE]
  Retrieve: s2_ce_verdict from Stage 2 CLOSE (for running tally)
  Confirm: s3_ce_verdict is this stage's owned field

### WORK

Write: {topic}-intelligence-{date}.md

  Scan internal sources. For each finding:
    artifact path, claim, CE-relevant (yes/no).

### CLOSE

  VERDICT (OWNED FIELD — Stage 3 sole producer):
    s3_ce_verdict: [found / null]    [produced here; consumed only by Stage 4 CAMPAIGN OUTCOME BLOCK]

  NULL TALLY NOTE:
    Running null tally: [count] null. 1 evidence stage remains.
    If null: SESSION INVARIANTs A and B active — pre-committed obligations.

  SCHEMA INTEGRITY NOTE:
    Schema fields locked: 9/9 — 0 additions, 0 omissions, 0 source mismatches since Stage 2 check.

  Artifact written: {topic}-intelligence-{date}.md
  Confirm: "Stage 3 closed. s3_ce_verdict: [found/null]. Tally: [N]. Schema: 9/9. Advancing to Stage 4."

---

## Stage 4 — Analysis

### ENTER

  Verify: {topic}-intelligence-{date}.md written [Stage 3 CLOSE]
  Retrieve: s2_ce_verdict from Stage 2 CLOSE, s3_ce_verdict from Stage 3 CLOSE
  Confirm: s4_ce_verdict is this stage's owned field; CAMPAIGN OUTCOME BLOCK is the sole consumer

### WORK

Write: {topic}-analysis-{date}.md

  Analyze all evidence from Stages 2 and 3.
  - Supporting evidence strength.
  - Counter-evidence summary: all CE found, sources, credibility.
  - If CE null across all stages: acknowledge explicitly, list all sources checked.

### CLOSE

  VERDICT (OWNED FIELD — Stage 4 sole producer):
    s4_ce_verdict: [found / null]    [produced here; final CE verdict field]

  CAMPAIGN OUTCOME BLOCK:
    Consume all three owned verdict fields:

      s2_ce_verdict: [found / null]    [Stage 2 — sole source; retrieved from Stage 2 CLOSE]
      s3_ce_verdict: [found / null]    [Stage 3 — sole source; retrieved from Stage 3 CLOSE]
      s4_ce_verdict: [found / null]    [Stage 4 — sole source; produced above]

    Derive:
      null_tally_final: count of {s2_ce_verdict, s3_ce_verdict, s4_ce_verdict} where value = null
        derivation: "named verdict fields per CE VERDICT OWNERSHIP TABLE formula.
                     NOT dual_lock_fired. NOT co_activation_confirmed."

      incumbent_defense_closed: [true if null_tally_final = 3; false otherwise]
        derivation: "null_tally_final >= 3. NOT dual_lock_fired. NOT co_activation_confirmed."

  SCHEMA INTEGRITY NOTE:
    s4_ce_verdict is the final evidence-stage verdict. 9/9 fields intact.
    Schema contract confirmed clean through collection phase.

  Artifact written: {topic}-analysis-{date}.md
  Confirm: "Stage 4 closed. CE verdicts: s2=[v], s3=[v], s4=[v].
            null_tally_final=[count] (derived from named fields).
            incumbent_defense_closed=[true/false]. Schema: 9/9. Advancing to Stage 5."

---

## Stage 5 — Synthesis

### ENTER

  Verify: {topic}-analysis-{date}.md written [Stage 4 CLOSE]
  Retrieve from CAMPAIGN OPEN: SESSION INVARIANTs A/B/C, PRE-COMMITTED HANDOFF SCHEMA,
    CE VERDICT OWNERSHIP TABLE, COUNTER-HYPOTHESIS CLOSURE RULE, NULL TALLY CHAIN RULE
  Load: counter_hypothesis from {topic}-hypothesis-{date}.md [Stage 5 resolution obligation]
  Load: null_tally_final from Stage 4 CAMPAIGN OUTCOME BLOCK [for NULL TALLY CHAIN echo]

### WORK

Write: {topic}-synthesize-{date}.md

#### Findings

  3-5 bullet points, each traceable to a specific artifact (path or stage reference).

#### COUNTER-HYPOTHESIS RESOLUTION

  MANDATORY — unconditionally required (COUNTER-HYPOTHESIS CLOSURE RULE — execution).
  counter_hypothesis: [restate from {topic}-hypothesis-{date}.md]

  Verdict (choose one):
    [ ] REFUTED — evidence from Stage(s) [X] directly defeats this claim:
          [cite specific finding from Stage 2 or Stage 3 artifact]
    [ ] PARTIALLY REFUTED — evidence weakens but does not eliminate this claim:
          [cite finding; state what remains unaddressed]
    [ ] OPEN RISK — no evidence gathered addressed this claim:
          [state what evidence would be needed; note as live risk in confidence reasoning]

  OPEN RISK execution: reduce confidence one tier from evidence_score baseline (INVARIANT execution).

#### Counter-Evidence

  MANDATORY — unconditionally required.
  If CE found: list each item with source artifact and credibility rating.
  If null: "No CE found. Sources checked: [Stage 2 sources], [Stage 3 sources].
           Null result is the primary risk to the hypothesis."
  If null: execute SESSION INVARIANT A (adversarial reviewer) and B (confidence cap).

#### ATOMIC DUAL-LOCK (activates if null_tally_final = 3)

  NULL TALLY CHAIN (NULL TALLY CHAIN RULE — execution, not declaration):

    Load per-stage CE verdicts from Stage 2, Stage 3, and Stage 4 CLOSEs. Reconstruct:
      S2: [found / null] → running tally [N]
      S3: [found / null] → running tally [N]
      S4: [found / null] → tally [N] = null_tally_final

    Cross-check: chain terminal must equal null_tally_final from Stage 4.
    If mismatch: TALLY ERROR — record discrepancy before continuing.

  LOCK 1 — Adversarial Reviewer (SESSION INVARIANT A — execution):
    Reviewer: {adversarial_reviewer_type}
    Required before promotion. Pre-committed obligation.

  LOCK 2 — Confidence Cap (SESSION INVARIANT B — execution):
    CE-score = -2 (all-null formula). Maximum claim: MEDIUM. HIGH blocked.

  dual_lock_fired: [true if null_tally_final = 3, false otherwise]
  co_activation_confirmed: [must equal dual_lock_fired — format error if they differ]

#### Confidence Level

  evidence_score: [0-5]
  ce_score: [0 or -2 per SESSION INVARIANT B]
  counter_hypothesis_verdict: [REFUTED / PARTIALLY REFUTED / OPEN RISK]
  confidence: [LOW / MEDIUM / HIGH — HIGH blocked if ce_score = -2;
               OPEN RISK reduces one tier from evidence_score baseline]

#### Handoff

  SCHEMA COMPLIANCE CHECK — retrieve PRE-COMMITTED HANDOFF SCHEMA.
  Confirm all 9 declared fields with declared derivation sources.
  DERIVATION ANNOTATION RULE (SESSION INVARIANT C — execution): every field carries [derived from: X].

  scout_anchor: {topic}-scout-record-{date}.md
    [derived from: ROLE B scout load]

  hypothesis: {topic}-hypothesis-{date}.md
    [derived from: Stage 1 artifact write — counter_hypothesis field included]

  analysis: {topic}-analysis-{date}.md
    [derived from: Stage 4 artifact write]

  null_tally_final: [0-3]
    positive_derivation: "count of {s2_ce_verdict, s3_ce_verdict, s4_ce_verdict} = null
                          per CE VERDICT OWNERSHIP TABLE formula"
    independence_chain: "NOT derived from dual_lock_fired; NOT derived from co_activation_confirmed"
    [derived from: Stage 4 CAMPAIGN OUTCOME BLOCK — tally chain echoed in ATOMIC DUAL-LOCK above]

  incumbent_defense_closed: [true if null_tally_final = 3, false otherwise]
    positive_derivation: "null_tally_final via formula null_tally_final >= 3"
    independence_chain: "NOT derived from dual_lock_fired; NOT derived from co_activation_confirmed"
    [derived from: null_tally_final — independence confirmed per CAMPAIGN OPEN schema]

  co_activation_confirmed: [must equal dual_lock_fired]
    positive_derivation: "dual_lock_fired in ATOMIC DUAL-LOCK"
    independence_chain: "NOT derived from incumbent_defense_closed; NOT derived from null_tally_final directly"
    [derived from: dual_lock_fired — independence confirmed per CAMPAIGN OPEN schema]

  confidence: [LOW/MEDIUM/HIGH]
    [derived from: evidence_score + ce_score per SESSION INVARIANT B + counter_hypothesis_verdict tier adjustment]

  next: topic-story
    [derived from: static handoff target]

  schema_compliance_confirmed: true
    [derived from: synthesis-time check — 9/9 fields present with declared derivation sources;
     CE VERDICT OWNERSHIP TABLE formula confirmed; counter_hypothesis resolved;
     null tally chain echoed and cross-checked; SESSION INVARIANT C executed; 0 omissions]

### CLOSE

  Artifact written: {topic}-synthesize-{date}.md
  Confirm: "Stage 5 closed. CE tally chain: S2=[v]→S3=[v]→S4=[v]=null_tally_final=[count].
            Counter-hypothesis resolution: [verdict]. Confidence: [level].
            Evidence brief ready for topic-story."
```

---

## V-04 — Combined Axes: Phrasing Register (Conversational/Imperative) + Role Sequence (Numbered Gate)

**Variation axes**:
1. **Phrasing register**: Second-person imperative throughout ("You are ROLE A.", "Fill
   this in:", "You own s2_ce_verdict — record it here:"). SESSION INVARIANT blocks use
   direct declarative sentences rather than formal locked-language. Confirmation lines
   use first-person present tense ("I've written...").
2. **Role sequence**: Roles and gate are framed as a numbered checklist (Step 1, Step 2,
   Step 3: Gate) rather than named attestation-field blocking. The gate reads as a
   pass/fail checklist rather than a field-presence assertion.

**Hypothesis**: The formal register of "SESSION INVARIANT A — locked formula — cannot be
modified or bypassed at synthesis" is structurally precise but may be opaque to practitioners
unfamiliar with the invariant-registry pattern. A conversational/imperative register
expresses the same obligations as direct instructions ("You must cap confidence at MEDIUM
if all three stages return null — this is pre-decided, not a judgment call at synthesis")
without reducing structural rigor. The numbered gate sequence makes campaign entry feel
like a pre-flight checklist rather than a bureaucratic attestation, which may increase
adherence to the gate discipline.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
Start at Step 1. Do not skip ahead. Each step has a clear completion condition.

---

## CAMPAIGN OPEN

Before anything else, fill these in:

  Who you're displacing: status_quo_comparator = [name the incumbent approach]

Now lock these decisions. They apply for the whole campaign — you will not re-decide them:

  Adversarial reviewer: adversarial_reviewer_type = [the role most likely to challenge
    the claim; activates automatically if all three evidence stages return null]

  Confidence rule: If all three evidence stages return null, CE-score = -2. This caps
    confidence at MEDIUM. You cannot override this at synthesis — it's decided now.

  Annotation rule: Every field in the final handoff must say [derived from: X].
    Missing label = format error. You will execute this rule at synthesis.

Now lock the handoff schema. Synthesis must produce exactly these 9 fields with exactly
these sources. No extras. No substitutions.

  FIELD                       | WHERE IT COMES FROM
  ----------------------------|---------------------------------------------------
  scout_anchor                | Step 2 (ROLE B) scout load
  hypothesis                  | Stage 1 write
  analysis                    | Stage 4 write
  null_tally_final            | Stage 4 outcome block — computed from s2, s3, s4 CE verdicts
  incumbent_defense_closed    | null_tally_final only (not from dual_lock_fired or co_activation_confirmed)
  co_activation_confirmed     | dual_lock_fired only (not from incumbent_defense_closed or null_tally_final)
  confidence                  | evidence_score + CE-score rule above
  next                        | always "topic-story"
  schema_compliance_confirmed | your compliance check at synthesis

Now lock the CE verdict ownership. Each evidence stage owns exactly one verdict field:

  s2_ce_verdict   — you record it at Stage 2 close. No other stage may write it.
  s3_ce_verdict   — you record it at Stage 3 close. No other stage may write it.
  s4_ce_verdict   — you record it at Stage 4 close. No other stage may write it.

  null_tally_final = count of {s2_ce_verdict, s3_ce_verdict, s4_ce_verdict} that are null.

Counter-hypothesis rule: You will declare counter_hypothesis at Stage 1. You must
resolve it at Stage 5 with one of: REFUTED / PARTIALLY REFUTED / OPEN RISK, plus a
source citation. If OPEN RISK, reduce confidence one tier from the evidence_score.

Null tally chain rule: At Stage 5, inside the dual-lock section, you will reconstruct
the tally chain step by step: S2=[v]→tally N, S3=[v]→tally N, S4=[v]→tally N=null_tally_final.
The final count must match Stage 4. Mismatch = tally error.

Everything above is locked now. You will execute these rules, not re-decide them.

---

## Step 1 — Lock the Registry (ROLE A)

You are ROLE A. You own exactly one field: invariant_registry_confirmed.
Only you produce this field. No other step produces it.

Confirm that everything in CAMPAIGN OPEN is active: all rules, the schema, the CE
verdict ownership table, the counter-hypothesis rule, the tally chain rule.

  invariant_registry_confirmed: true    [you — sole producer]

Checklist item 1 complete. Do not begin Step 2 until this is true.

---

## Step 2 — Load the Scout Record (ROLE B)

You are ROLE B. You own exactly one field: gate_s_cleared.
Only you produce this field. No other step produces it.

Do this after Step 1. Find: {topic}-scout-record-{date}.md
  Not found: STOP. Write "GATE S FAIL — scout record missing. Campaign cannot continue."
  Found: load it. Pull out: market signal, competitor landscape, feasibility finding.

  gate_s_cleared: true    [you — sole producer]

Checklist item 2 complete. Both fields are now on record.

---

## Step 3 — Gate Check

Checklist:
  [ ] invariant_registry_confirmed = true   (Step 1 — ROLE A)
  [ ] gate_s_cleared = true                 (Step 2 — ROLE B)

Both checked? Move to Stage 1.
Any unchecked? STOP — do not open Stage 1.

---

## Stage 1 — Hypothesis

Write: {topic}-hypothesis-{date}.md

Put these in the frontmatter:
  topic: {topic}
  date: {date}
  scout_anchor: {topic}-scout-record-{date}.md   [loaded at Step 2]
  gate_s_cleared: true                    [Step 2 — ROLE B only]
  invariant_registry_confirmed: true      [Step 1 — ROLE A only; covers all locked rules]
  incumbent: [from status_quo_comparator]
  adversarial_reviewer_type: [from CAMPAIGN OPEN]
  ce_score_formula: CE-score = -2 if all null
  handoff_schema_locked: true

In the body, write three things:
  1. Hypothesis: one sentence — what {topic} does better than the incumbent.
  2. Basis: 3-5 signals from the scout record.
  3. counter_hypothesis: the strongest thing the incumbent could say in rebuttal — one
     sentence. This creates an obligation: Stage 5 must resolve it. Write it now.

Done: artifact written, counter_hypothesis on record.
Say: "Stage 1 done. counter_hypothesis declared. CE verdict fields s2/s3/s4 assigned to their stages. Moving to Stage 2."

---

## Stage 2 — Web Search

Write: {topic}-websearch-{date}.md

Search for external evidence on {topic}. For each finding, write down:
  claim, URL, CE-relevant (yes/no), quote.

Note: CE = evidence that the incumbent already does what {topic} claims, or that
{topic}'s approach has known problems. Flag anything that looks like CE.

Stage 2 close — record your owned verdict field:

  s2_ce_verdict: [found / null]    [you own this — write it here; Stage 4 will read it]

Running tally: [count] null so far. Two stages left.
If null: the adversarial reviewer and confidence cap rules from CAMPAIGN OPEN are still
active — you will execute them at Stage 5, not decide them there.

Schema check: 9/9 fields still intact. No additions, no omissions, no source changes.

Done: artifact written.
Say: "Stage 2 done. s2_ce_verdict: [found/null]. Tally: [N]. Schema: 9/9. Moving to Stage 3."

---

## Stage 3 — Internal Intelligence

Write: {topic}-intelligence-{date}.md

Scan internal sources. For each finding, write down:
  artifact path, claim, CE-relevant (yes/no).

Stage 3 close — record your owned verdict field:

  s3_ce_verdict: [found / null]    [you own this — write it here; Stage 4 will read it]

Running tally: [count] null so far. One stage left.
If null: adversarial reviewer and confidence cap rules still active — execute at Stage 5.

Schema check: 9/9 fields intact. No additions, no omissions since Stage 2 check.

Done: artifact written.
Say: "Stage 3 done. s3_ce_verdict: [found/null]. Tally: [N]. Schema: 9/9. Moving to Stage 4."

---

## Stage 4 — Analysis

Write: {topic}-analysis-{date}.md

Write up: how strong is the supporting evidence? What did the CE look like — list
everything found with source and credibility. If null: say so explicitly, list everything
you checked.

Stage 4 close — record your owned verdict field, then compute the outcome block:

  s4_ce_verdict: [found / null]    [you own this — write it here]

Now consume all three verdict fields you've recorded:

  s2_ce_verdict: [found / null]    [from Stage 2 — you're reading it, not re-deciding it]
  s3_ce_verdict: [found / null]    [from Stage 3 — you're reading it, not re-deciding it]
  s4_ce_verdict: [found / null]    [from above — Stage 4 sole source]

Compute:
  null_tally_final: count of the three where value = null
    Source: the three verdict fields above. Not from dual_lock_fired. Not from co_activation_confirmed.

  incumbent_defense_closed: true if null_tally_final = 3, false otherwise
    Source: null_tally_final only. Not from dual_lock_fired. Not from co_activation_confirmed.

Schema check: s4_ce_verdict is the last evidence verdict. 9/9 fields intact.

Done: artifact written.
Say: "Stage 4 done. CE verdicts: s2=[v], s3=[v], s4=[v]. null_tally_final=[count]. incumbent_defense_closed=[true/false]. Moving to Stage 5."

---

## Stage 5 — Synthesis

Write: {topic}-synthesize-{date}.md

You have everything you need. Pull it all together now.

### Findings

3-5 bullets. Each one must point to a specific artifact (path or stage).

### Counter-Hypothesis Resolution

You declared a counter_hypothesis at Stage 1. You must resolve it now.

Load it: counter_hypothesis from {topic}-hypothesis-{date}.md
Write it out again here.

Pick your verdict:
  REFUTED — cite the evidence from Stage 2, 3, or 4 that defeats it.
  PARTIALLY REFUTED — cite what weakens it; say what's still standing.
  OPEN RISK — say what would be needed to refute it; flag it as an open risk.

If OPEN RISK: drop confidence one tier from your evidence_score. You decided this rule
at CAMPAIGN OPEN — execute it now, don't deliberate.

### Counter-Evidence

Required. No exceptions.

If you found CE: list each item with source and credibility.
If CE was null: write "No CE found. I checked: [sources from Stage 2], [sources from Stage 3].
This is the primary risk." Then execute the adversarial reviewer rule (from CAMPAIGN OPEN)
and apply CE-score = -2. These are pre-decided — execute them.

### Dual-Lock Section (runs if null_tally_final = 3)

First, reconstruct the tally chain:

  S2: [found / null] → running tally [N]
  S3: [found / null] → running tally [N]
  S4: [found / null] → tally [N] = null_tally_final

Check: does the final number match null_tally_final from Stage 4? If not, record the mismatch.

  Lock 1 — Adversarial Reviewer: {adversarial_reviewer_type} must review before any promotion.
  Lock 2 — Confidence Cap: CE-score = -2. Maximum confidence is MEDIUM.

  dual_lock_fired: [true if null_tally_final = 3, false otherwise]
  co_activation_confirmed: [same as dual_lock_fired — error if different]

### Confidence

  evidence_score: [0-5]
  ce_score: [0 or -2]
  counter_hypothesis_verdict: [REFUTED / PARTIALLY REFUTED / OPEN RISK]
  confidence: [LOW / MEDIUM / HIGH — HIGH blocked if ce_score = -2;
               OPEN RISK drops one tier from evidence_score]

### Handoff

Check the schema you locked at CAMPAIGN OPEN. Every field must be present with the
right source. Label every field [derived from: X] — this is the annotation rule you
committed to at CAMPAIGN OPEN. Execute it now.

  scout_anchor: {topic}-scout-record-{date}.md
    [derived from: Step 2 (ROLE B) scout load]

  hypothesis: {topic}-hypothesis-{date}.md
    [derived from: Stage 1 write — includes counter_hypothesis field]

  analysis: {topic}-analysis-{date}.md
    [derived from: Stage 4 write]

  null_tally_final: [0-3]
    positive_derivation: "count of s2/s3/s4_ce_verdict = null per CE verdict ownership formula"
    independence_chain: "not from dual_lock_fired; not from co_activation_confirmed"
    [derived from: Stage 4 outcome block; tally chain echoed above]

  incumbent_defense_closed: [true / false]
    positive_derivation: "null_tally_final >= 3"
    independence_chain: "not from dual_lock_fired; not from co_activation_confirmed"
    [derived from: null_tally_final]

  co_activation_confirmed: [same as dual_lock_fired]
    positive_derivation: "dual_lock_fired in dual-lock section"
    independence_chain: "not from incumbent_defense_closed; not from null_tally_final directly"
    [derived from: dual_lock_fired]

  confidence: [LOW/MEDIUM/HIGH]
    [derived from: evidence_score + ce_score + counter_hypothesis_verdict tier adjustment]

  next: topic-story
    [derived from: static — always topic-story]

  schema_compliance_confirmed: true
    [derived from: compliance check now — 9 fields present with declared sources;
     CE verdict chain confirmed; counter_hypothesis resolved; tally chain echoed and checked;
     annotation rule executed; no omissions]

Done: artifact written.
Say: "Stage 5 done. Tally chain: S2=[v]→S3=[v]→S4=[v]=null_tally_final=[count].
      Counter-hypothesis: [verdict]. Confidence: [level].
      Evidence brief ready for topic-story. Artifact: {topic}-synthesize-{date}.md."
```

---

## V-05 — Combined Axes: All Four (Inertia Framing + Table Format + Lifecycle Emphasis + Phrasing Register)

**Variation axes**: All four axes combined.
1. **Inertia Framing**: Incumbent is a named antagonist with a dedicated block; each
   stage contains an INCUMBENT CHECK; synthesis is "the case against {incumbent}."
2. **Table Format**: All structured metadata (schema, CE verdict ownership, per-stage
   notes, handoff block) renders as tables.
3. **Lifecycle Emphasis**: Each stage has ENTER / WORK / CLOSE sub-sections.
4. **Phrasing Register**: Second-person imperative, direct sentences, pre-flight
   checklist framing for roles and gate.

**Hypothesis**: Each single-axis variation demonstrates that a specific presentation
choice is compatible with the full v10 structural stack. A full-combination variation
tests whether all four choices cohere without creating competing structural signals —
e.g., whether table-dominant format survives the ENTER/WORK/CLOSE sectioning without
losing the table structure, and whether the conversational register can coexist with
the formal ownership language required by C-22/C-23 (sole-producer declarations for
ROLE A/B). The combined prompt is also the most likely to diverge from the reference
format in subtle ways, making it the sharpest test of axis-invariance for all 33 criteria.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic. This campaign builds
the case for displacing {status_quo_comparator} with {topic}. Start at Step 1.
Do not skip ahead. Each step has a clear completion condition.

---

## CAMPAIGN OPEN

### Fill — Incumbent Threat

| FIELD                | VALUE                                                             |
|----------------------|-------------------------------------------------------------------|
| status_quo_comparator| [name the incumbent approach this topic must displace]            |
| incumbent_strength   | [one sentence — why the incumbent is currently winning]           |
| incumbent_vulnerability | [one sentence — where the incumbent is weakest]               |

### Lock — Rules

These are decided now. You will execute them, not re-decide them at synthesis.

| RULE                       | CONTENT                                                                |
|----------------------------|------------------------------------------------------------------------|
| Adversarial reviewer       | adversarial_reviewer_type = [role most likely to challenge the claim;  |
|                            | represents the incumbent's perspective]. Fires if all 3 stages null.   |
| Confidence cap             | CE-score = -2 if all 3 evidence stages null; 0 otherwise.              |
|                            | Maximum confidence = MEDIUM if CE-score = -2. Cannot be overridden.   |
| Annotation rule            | Every handoff field carries [derived from: X]. Missing = format error. |
| Counter-hypothesis closure | counter_hypothesis declared at Stage 1 must be resolved at Stage 5.   |
|                            | Options: REFUTED / PARTIALLY REFUTED / OPEN RISK + evidence citation.  |
|                            | OPEN RISK drops confidence one tier from evidence_score.               |
| Null tally chain           | Stage 5 dual-lock section includes NULL TALLY CHAIN:                  |
|                            | S2→tally N | S3→tally N | S4→tally N=null_tally_final.                 |
|                            | Terminal must match Stage 4. Mismatch = format error.                 |

### Lock — Handoff Schema

| # | FIELD                    | SOURCE                                                            |
|---|--------------------------|-------------------------------------------------------------------|
| 1 | scout_anchor             | Step 2 (ROLE B) scout load                                        |
| 2 | hypothesis               | Stage 1 write                                                     |
| 3 | analysis                 | Stage 4 write                                                     |
| 4 | null_tally_final         | Stage 4 outcome block — count of {s2,s3,s4}_ce_verdict = null    |
| 5 | incumbent_defense_closed | null_tally_final only (NOT dual_lock_fired; NOT co_activation_confirmed) |
| 6 | co_activation_confirmed  | dual_lock_fired only (NOT incumbent_defense_closed; NOT null_tally_final) |
| 7 | confidence               | evidence_score + CE-score rule                                    |
| 8 | next                     | always "topic-story"                                              |
| 9 | schema_compliance_confirmed | your synthesis-time compliance check                           |

### Lock — CE Verdict Ownership

| VERDICT FIELD  | WHO WRITES IT | WHEN          | WHO READS IT                      | VALUES       |
|----------------|---------------|---------------|-----------------------------------|--------------|
| s2_ce_verdict  | You at Stage 2 close | Stage 2 | Stage 4 CAMPAIGN OUTCOME BLOCK | found / null |
| s3_ce_verdict  | You at Stage 3 close | Stage 3 | Stage 4 CAMPAIGN OUTCOME BLOCK | found / null |
| s4_ce_verdict  | You at Stage 4 close | Stage 4 | Stage 4 CAMPAIGN OUTCOME BLOCK | found / null |

null_tally_final = count of the three verdict fields that equal null.

Everything above is locked. Do not modify.

---

## Step 1 — Lock the Registry (ROLE A)

You are ROLE A. You own one field: invariant_registry_confirmed. Only you write it.

Confirm every locked item in CAMPAIGN OPEN is active: rules, schema, CE verdict ownership.

| FIELD                        | VALUE | PRODUCER     |
|------------------------------|-------|--------------|
| invariant_registry_confirmed | true  | ROLE A — you |

Checklist item 1 done. Do not move to Step 2 until this is true.

---

## Step 2 — Load Scout Record (ROLE B)

You are ROLE B. You own one field: gate_s_cleared. Only you write it.

After Step 1: find {topic}-scout-record-{date}.md
  Not found: STOP — "GATE S FAIL — scout record missing."
  Found: load it. Pull: market signal, competitor landscape, feasibility finding.
    Note anything about {status_quo_comparator} — you'll need it for Stage 2 incumbent checks.

| FIELD          | VALUE | PRODUCER     |
|----------------|-------|--------------|
| gate_s_cleared | true  | ROLE B — you |

Checklist item 2 done. Both fields on record.

---

## Step 3 — Gate Check

| CHECKLIST ITEM               | STATUS  | SOLE SOURCE |
|------------------------------|---------|-------------|
| invariant_registry_confirmed | [✓ / ✗] | Step 1 (ROLE A) |
| gate_s_cleared               | [✓ / ✗] | Step 2 (ROLE B) |

Both checked? Move to Stage 1. Any unchecked? STOP.

---

## Stage 1 — Hypothesis

### ENTER

| VERIFY                       | VALUE  | SOURCE      |
|------------------------------|--------|-------------|
| gate_s_cleared               | true   | Step 2 only |
| invariant_registry_confirmed | true   | Step 1 only |
| counter_hypothesis_rule      | active | CAMPAIGN OPEN |
| null_tally_chain_rule        | active | CAMPAIGN OPEN |

Load: {topic}-scout-record-{date}.md (loaded at Step 2).
Note: incumbent_strength and incumbent_vulnerability from CAMPAIGN OPEN.

### WORK

Write: {topic}-hypothesis-{date}.md

Frontmatter:

| FIELD                        | VALUE / SOURCE                                                  |
|------------------------------|-----------------------------------------------------------------|
| topic                        | {topic}                                                         |
| date                         | {date}                                                          |
| scout_anchor                 | {topic}-scout-record-{date}.md [Step 2]                         |
| gate_s_cleared               | true [Step 2 — sole source]                                     |
| invariant_registry_confirmed | true [Step 1 — sole source; all rules active]                   |
| incumbent                    | [from status_quo_comparator]                                    |
| adversarial_reviewer_type    | [from locked rules]                                             |
| ce_score_formula             | CE-score = -2 if all null                                       |
| handoff_schema_locked        | true                                                            |

Body:
  Hypothesis: one sentence — what {topic} does better than {incumbent}.
  Basis: 3-5 signals from the scout record; at least one addresses incumbent_vulnerability.
  counter_hypothesis: the incumbent's strongest defense — one sentence in the incumbent's
    voice. This creates a Stage 5 obligation. Write it now.

### CLOSE

| FIELD                   | STATUS | NOTE                                    |
|-------------------------|--------|-----------------------------------------|
| Artifact written        | yes    | {topic}-hypothesis-{date}.md            |
| counter_hypothesis      | declared| Stage 5 resolution required            |
| CE verdict fields       | assigned| s2/s3/s4 pre-assigned per ownership table|

Say: "Stage 1 done. counter_hypothesis on record. Moving to Stage 2."

---

## Stage 2 — Web Search

### ENTER

| VERIFY                               | VALUE | SOURCE  |
|--------------------------------------|-------|---------|
| {topic}-hypothesis-{date}.md written | yes   | Stage 1 |
| s2_ce_verdict ownership confirmed    | yes   | you own it |

Note: incumbent = {status_quo_comparator}. You are looking for evidence that the
incumbent already does what {topic} claims — that's CE.

### WORK

Write: {topic}-websearch-{date}.md

| FINDING | SOURCE URL | CE-RELEVANT | ADDRESSES INCUMBENT? | QUOTE |
|---------|------------|-------------|----------------------|-------|
| [claim] | [url]      | yes / no    | yes / no / partial   | [excerpt] |

INCUMBENT CHECK: for each finding, note if it helps displace {incumbent} by addressing
incumbent_strength or incumbent_vulnerability from CAMPAIGN OPEN.

### CLOSE

| NOTE TYPE        | FIELD          | VALUE                      | RULE                              |
|------------------|----------------|----------------------------|-----------------------------------|
| CE VERDICT (owned)| s2_ce_verdict | [found / null]             | You — sole writer; Stage 4 reads  |
| NULL TALLY       | running count  | [N] null; 2 stages left    | Adversarial + cap rules still on  |
| SCHEMA INTEGRITY | fields locked  | 9/9 — 0 deltas since OPEN  |                                   |

| ARTIFACT  | STATUS |
|-----------|--------|
| {topic}-websearch-{date}.md | written |

Say: "Stage 2 done. s2_ce_verdict: [found/null]. Displacement signal: [yes/no/partial]. Schema: 9/9. Moving to Stage 3."

---

## Stage 3 — Internal Intelligence

### ENTER

| VERIFY                              | VALUE | SOURCE  |
|-------------------------------------|-------|---------|
| {topic}-websearch-{date}.md written | yes   | Stage 2 |
| s2_ce_verdict recorded              | yes   | Stage 2 close |
| s3_ce_verdict ownership confirmed   | yes   | you own it |

### WORK

Write: {topic}-intelligence-{date}.md

| ARTIFACT PATH | CLAIM | CE-RELEVANT | ADDRESSES INCUMBENT? |
|---------------|-------|-------------|----------------------|
| [path]        | [claim] | yes / no  | yes / no / partial   |

INCUMBENT CHECK: flag any internal artifact that references {incumbent} or comparable approaches.

### CLOSE

| NOTE TYPE        | FIELD          | VALUE                      | RULE                              |
|------------------|----------------|----------------------------|-----------------------------------|
| CE VERDICT (owned)| s3_ce_verdict | [found / null]             | You — sole writer; Stage 4 reads  |
| NULL TALLY       | running count  | [N] null; 1 stage left     | Adversarial + cap rules still on  |
| SCHEMA INTEGRITY | fields locked  | 9/9 — 0 deltas since Stage 2|                                  |

| ARTIFACT  | STATUS |
|-----------|--------|
| {topic}-intelligence-{date}.md | written |

Say: "Stage 3 done. s3_ce_verdict: [found/null]. Displacement signal: [yes/no/partial]. Schema: 9/9. Moving to Stage 4."

---

## Stage 4 — Analysis

### ENTER

| VERIFY                                  | VALUE | SOURCE  |
|-----------------------------------------|-------|---------|
| {topic}-intelligence-{date}.md written  | yes   | Stage 3 |
| s2_ce_verdict available                 | yes   | Stage 2 close |
| s3_ce_verdict available                 | yes   | Stage 3 close |
| s4_ce_verdict ownership confirmed       | yes   | you own it |

### WORK

Write: {topic}-analysis-{date}.md

  Supporting evidence strength: [prose]
  Displacement assessment: does the evidence make a credible case against {incumbent}?
    Rate: STRONG / MODERATE / WEAK
  Counter-evidence summary: list all CE; credibility. Does CE strengthen {incumbent}?
  If CE null: acknowledge; list everything checked.

### CLOSE

Record your owned verdict, then compute the outcome block:

| VERDICT FIELD  | VALUE          | WRITER         | NOTE                               |
|----------------|----------------|----------------|------------------------------------|
| s4_ce_verdict  | [found / null] | Stage 4 — you  | Stage 4 sole writer; owned field   |

CAMPAIGN OUTCOME BLOCK — consume all three verdict fields:

| VERDICT FIELD  | VALUE          | SOLE SOURCE    |
|----------------|----------------|----------------|
| s2_ce_verdict  | [found / null] | Stage 2 only   |
| s3_ce_verdict  | [found / null] | Stage 3 only   |
| s4_ce_verdict  | [found / null] | Stage 4 only   |

| DERIVED FIELD            | VALUE        | FORMULA                                                                     |
|--------------------------|--------------|-----------------------------------------------------------------------------|
| null_tally_final         | [0-3]        | count of the three verdict fields = null (CE ownership table formula)       |
|                          |              | NOT from dual_lock_fired. NOT from co_activation_confirmed.                 |
| incumbent_defense_closed | [true/false] | null_tally_final >= 3. NOT from dual_lock_fired. NOT from co_activation_confirmed. |

| NOTE TYPE        | VALUE                                              |
|------------------|----------------------------------------------------|
| SCHEMA INTEGRITY | 9/9 fields intact; confirmed through collection    |

| ARTIFACT  | STATUS |
|-----------|--------|
| {topic}-analysis-{date}.md | written |

Say: "Stage 4 done. CE verdicts: s2=[v], s3=[v], s4=[v]. null_tally_final=[count]. incumbent_defense_closed=[true/false]. Moving to Stage 5."

---

## Stage 5 — Synthesis

### ENTER

| RETRIEVE FROM CAMPAIGN OPEN         | STATUS  |
|-------------------------------------|---------|
| Adversarial reviewer rule           | active  |
| Confidence cap rule                 | active  |
| Annotation rule                     | active  |
| Handoff schema (9 fields)           | locked  |
| CE verdict ownership table          | locked  |
| Counter-hypothesis closure rule     | active  |
| Null tally chain rule               | active  |

Load: counter_hypothesis from {topic}-hypothesis-{date}.md
Load: null_tally_final from Stage 4 outcome block

### WORK

Write: {topic}-synthesize-{date}.md

#### The Case Against {incumbent}

Frame findings as displacement evidence. For each finding, note whether it addresses
incumbent_strength, incumbent_vulnerability, or is neutral.

3-5 bullets, each traceable to a specific artifact.

#### Counter-Hypothesis Resolution

MANDATORY — no exceptions. You declared counter_hypothesis at Stage 1. Resolve it now.

| FIELD                | VALUE                                                          |
|----------------------|----------------------------------------------------------------|
| counter_hypothesis   | [restate from {topic}-hypothesis-{date}.md]                   |
| verdict              | REFUTED / PARTIALLY REFUTED / OPEN RISK                       |
| evidence_citation    | [cite Stage 2, 3, or 4 finding with artifact path]            |
| confidence_impact    | OPEN RISK: drop confidence one tier from evidence_score. Execute now. |

#### Counter-Evidence

MANDATORY — no exceptions.

If found: list each item with source and credibility.
If null: "No CE found. Sources checked: [Stage 2], [Stage 3]. Null is the primary risk."
If null: execute adversarial reviewer rule and confidence cap — these are pre-decided.

#### Dual-Lock Section (runs if null_tally_final = 3)

NULL TALLY CHAIN — reconstruct step by step:

| STAGE | CE VERDICT     | RUNNING TALLY |
|-------|----------------|---------------|
| S2    | [found / null] | [N]           |
| S3    | [found / null] | [N]           |
| S4    | [found / null] | [N] = null_tally_final |

Cross-check: does the chain total match Stage 4 null_tally_final? If not: TALLY ERROR.

| LOCK   | CONTENT                                                          |
|--------|------------------------------------------------------------------|
| LOCK 1 | {adversarial_reviewer_type} must review before any promotion.    |
|        | Execution of pre-decided rule — not a new decision.              |
| LOCK 2 | CE-score = -2. Max confidence = MEDIUM. Not a new decision.      |

| FIELD                    | VALUE                                                        |
|--------------------------|--------------------------------------------------------------|
| dual_lock_fired          | [true if null_tally_final = 3, else false]                  |
| co_activation_confirmed  | [must equal dual_lock_fired — format error if different]     |

#### Confidence

| FIELD                      | VALUE                                                          |
|----------------------------|----------------------------------------------------------------|
| evidence_score             | [0-5]                                                          |
| ce_score                   | [0 or -2]                                                      |
| counter_hypothesis_verdict | [REFUTED / PARTIALLY REFUTED / OPEN RISK]                     |
| displacement_rating        | [STRONG / MODERATE / WEAK from Stage 4]                       |
| confidence                 | [LOW / MEDIUM / HIGH — HIGH blocked if ce_score = -2;         |
|                            |  OPEN RISK drops one tier from evidence_score]                 |

#### Handoff

Schema compliance check: all 9 fields from CAMPAIGN OPEN schema. Annotation rule: every
field carries [derived from: X] — executing now, not declaring.

| # | FIELD                    | VALUE                         | DERIVATION                                                                        |
|---|--------------------------|-------------------------------|-----------------------------------------------------------------------------------|
| 1 | scout_anchor             | {topic}-scout-record-{date}.md| [derived from: Step 2 (ROLE B) scout load]                                        |
| 2 | hypothesis               | {topic}-hypothesis-{date}.md  | [derived from: Stage 1 write — includes incumbent framing + counter_hypothesis]   |
| 3 | analysis                 | {topic}-analysis-{date}.md    | [derived from: Stage 4 write]                                                     |
| 4 | null_tally_final         | [0-3]                         | positive: count of s2/s3/s4_ce_verdict=null per CE ownership formula; independence: NOT dual_lock_fired; NOT co_activation_confirmed; [derived from: Stage 4 outcome block; chain echoed above] |
| 5 | incumbent_defense_closed | [true/false]                  | positive: null_tally_final >= 3; independence: NOT dual_lock_fired; NOT co_activation_confirmed; [derived from: null_tally_final] |
| 6 | co_activation_confirmed  | [= dual_lock_fired]           | positive: dual_lock_fired in dual-lock section; independence: NOT incumbent_defense_closed; NOT null_tally_final directly; [derived from: dual_lock_fired] |
| 7 | confidence               | [LOW/MEDIUM/HIGH]             | [derived from: evidence_score + ce_score + counter_hypothesis_verdict tier adjustment] |
| 8 | next                     | topic-story                   | [derived from: static handoff target]                                              |
| 9 | schema_compliance_confirmed | true                       | [derived from: synthesis-time check — 9/9 fields present; CE chain; counter-hypothesis closed; tally chain echoed + matched; annotation rule executed; 0 omissions] |

### CLOSE

| ARTIFACT  | STATUS |
|-----------|--------|
| {topic}-synthesize-{date}.md | written |

| SUMMARY FIELD              | VALUE                                    |
|----------------------------|------------------------------------------|
| Tally chain                | S2=[v]→S3=[v]→S4=[v]=null_tally_final=[count] |
| Counter-hypothesis verdict | [REFUTED / PARTIALLY REFUTED / OPEN RISK] |
| Case against {incumbent}   | [confidence] — displacement: [STRONG/MODERATE/WEAK] |
| Next                       | topic-story                               |

Say: "Stage 5 done. The case against {incumbent}: [confidence] confidence.
      Counter-hypothesis: [verdict]. Evidence brief ready for topic-story.
      Artifact: {topic}-synthesize-{date}.md."
```
