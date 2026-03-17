---
skill: quest-variate
skill_target: prove-topic
round: R10
date: 2026-03-15
rubric: prove-topic-rubric-v9-2026-03-15.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [ce_verdict_ownership, counter_hypothesis_closure, null_tally_chain_echo]
  combined: [V-04 (ce_verdict_ownership + counter_hypothesis_closure), V-05 (all_four)]
r9_anchor: "V-05 (schema_self_registration + symmetric_independence_chain + per_stage_schema_integrity_count + annotation_rule_precommitted — satisfies C-01 through C-30, 168/168)"
r10_targets: >
  Four patterns in R9 V-05 that exceed the v9 rubric ceiling (C-30). All
  variations are built on the full v9 stack (C-01 through C-30). Single-axis variations
  each introduce one new structural pattern; V-05 combines all four.

  (1) null_tally_final is derived from per-stage prose notes in R9 V-05. The three
  evidence stages each produce a CE verdict token, but the derivation chain from stage
  verdicts into null_tally_final is implicit — a reader must sum the null notes manually.
  Making each stage's CE verdict an OWNED FIELD (s2_ce_verdict, s3_ce_verdict,
  s4_ce_verdict) and declaring them as the explicit inputs to null_tally_final in the
  CAMPAIGN OUTCOME BLOCK creates a named upstream chain auditable from the CAMPAIGN
  OUTCOME BLOCK alone.

  (2) The counter-hypothesis formed at Stage 1 is not tracked through the collection
  phase or required to be resolved at synthesis. A synthesis can satisfy all 30 criteria
  while leaving the counter-hypothesis open without acknowledgment. Requiring a
  COUNTER-HYPOTHESIS RESOLUTION section at Stage 5 — with three possible verdicts
  (refuted, partially refuted, or open risk) and evidence traceable to Stages 2-4 —
  closes the hypothesis lifecycle.

  (3) The synthesis confirms null_tally_final as a single integer but does not reconstruct
  the per-stage accumulation history that produced it. A NULL TALLY CHAIN section in
  Stage 5 ("S2: [found/NULL] → tally N; S3: [found/NULL] → tally N; S4: [found/NULL]
  → tally N = null_tally_final") makes the accumulation history visible in the terminal
  artifact, enabling point-in-chain audit without replaying per-stage notes.

  (4) schema_compliance_confirmed at synthesis confirms field count and derivation sources
  but does not cross-reference the per-stage SCHEMA INTEGRITY NOTEs (C-29) that tracked
  schema population during collection. Adding cross-references to each stage's note
  creates a named backward chain from the terminal compliance check to the collection
  phase, making the per-stage audit trail reachable from the synthesis alone.
severity_stack_gap: >
  A variation satisfying C-01 through C-30 can still:
  (1) record null_tally_final as a prose count without naming the per-stage CE verdict
  tokens as its declared inputs — the tally satisfies C-20 but its derivation chain
  from stage-level decisions is implicit rather than field-named;
  (2) leave the counter-hypothesis from Stage 1 unaddressed at synthesis — no criterion
  requires Stage 5 to close the hypothesis lifecycle with an explicit resolution;
  (3) record null_tally_final = 3 at synthesis without showing the accumulation path
  (S2 NULL + S3 NULL + S4 NULL = 3) — the terminal value satisfies C-20 and C-28
  but the accumulation chain itself is not visible in the synthesis artifact;
  (4) confirm schema compliance at synthesis without cross-referencing the per-stage
  SCHEMA INTEGRITY NOTEs from C-29 — the compliance check passes but the backward
  chain from synthesis to collection is not traceable from the synthesis alone.
---

# prove-topic — Variation Round R10

Five complete, runnable skill body prompts. Each is self-contained — no diff, no cross-references.

Round 10 targets four patterns in R9 V-05 that exceed the v9 rubric ceiling (C-30). All
variations are built on the full v9 stack (C-01 through C-30). Single-axis variations each
introduce one new structural pattern; V-04 combines two; V-05 combines all four.

The four new axes:

- **R10 axis 1 (CE verdict ownership)**: Each evidence stage (S2, S3, S4) closes with a named
  OWNED CE VERDICT field (`s2_ce_verdict`, `s3_ce_verdict`, `s4_ce_verdict`). The CAMPAIGN
  OUTCOME BLOCK names these three fields as the declared inputs to `null_tally_final`, creating
  a derivation chain from stage-level decisions to the campaign outcome that is auditable from
  the CAMPAIGN OUTCOME BLOCK alone — not requiring per-stage note replay.

- **R10 axis 2 (counter-hypothesis closure)**: The hypothesis artifact declares a named
  `counter_hypothesis:` field at Stage 1. The synthesis contains a required
  COUNTER-HYPOTHESIS RESOLUTION section with a three-way verdict (REFUTED / PARTIALLY
  REFUTED / OPEN RISK) traceable to evidence from Stages 2-4. A synthesis that does not
  address the counter-hypothesis is structurally incomplete.

- **R10 axis 3 (null tally chain echo)**: The synthesis ATOMIC DUAL-LOCK section includes
  a NULL TALLY CHAIN block that reconstructs the per-stage accumulation in order:
  "S2: [found/NULL] → running tally N; S3: [found/NULL] → running tally N; S4: [found/NULL]
  → tally N = null_tally_final." This makes the accumulation history visible in the terminal
  artifact without stage-by-stage note replay.

- **R10 axis 4 (schema compliance cross-referenced to per-stage notes)**: The
  `schema_compliance_confirmed` field annotation names the specific per-stage SCHEMA
  INTEGRITY NOTEs (from Stages 2, 3, and 4) that confirmed field population during
  collection. The backward chain from terminal compliance check to collection-phase audits
  is traceable from the synthesis alone.

---

## V-01 — Axis: CE Verdict Ownership Per Evidence Stage

**Variation axis**: CE verdict ownership — each evidence stage closes by recording a named
OWNED CE VERDICT field (`s2_ce_verdict: found/null`, `s3_ce_verdict: found/null`,
`s4_ce_verdict: found/null`). The CAMPAIGN OUTCOME BLOCK in Stage 4 declares these three
fields as the explicit inputs to `null_tally_final`: "null_tally_final = count of [s2, s3,
s4] where verdict = null." This promotes the per-stage null tally from prose accumulation
(C-20) to a named derivation chain: three first-class boolean inputs feeding one computed
output.

**Hypothesis**: C-20 requires per-stage null tally accumulation with running count language.
The null tally satisfies C-20 when each stage records its result in a prose note. But the
derivation from stage-level CE results into `null_tally_final` is implicit — a reader
auditing the CAMPAIGN OUTCOME BLOCK must locate each stage's note, identify the CE verdict
token, and sum them manually. Making each stage's CE verdict an OWNED FIELD — named in
CAMPAIGN OPEN as declared inputs to `null_tally_final` — creates a named upstream chain
that is auditable from the CAMPAIGN OUTCOME BLOCK alone. The three verdict fields mirror
the attestation-field discipline of ROLE A and ROLE B: each stage is the sole producer
of its verdict token; the CAMPAIGN OUTCOME BLOCK is the sole consumer.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
Campaign opens with two blocking roles. Five evidence stages follow in fixed sequence.
Each evidence stage owns its CE verdict field. The CAMPAIGN OUTCOME BLOCK consumes
all three verdict fields to derive null_tally_final.

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

All session invariants and CE verdict ownership are now locked. Do not modify.

---

## ROLE A — INVARIANT REGISTRY LOCK

OWNED ATTESTATION FIELD: invariant_registry_confirmed
Sole producer of this field. No other role or stage may produce it.

Execute first. Confirm SESSION INVARIANTs A, B, and C — and PRE-COMMITTED HANDOFF SCHEMA
including CE VERDICT OWNERSHIP TABLE — are active as session invariants.

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
If found: load record. Extract: market signal, competitor landscape, feasibility finding.

  gate_s_cleared: true    [ROLE B's owned field — produced here only]

ROLE B COMPLETE. Output: gate_s_cleared. Both attestation fields on record — open Stage 1.

---

## GATE S

Requires ROLE A and ROLE B both complete.

  gate_s_cleared: true                  (ROLE B — sole source)
  invariant_registry_confirmed: true    (ROLE A — sole source; covers INVARIANTs A, B, C + schema)

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
  gate_s_cleared: true                    [ROLE B — sole source]
  invariant_registry_confirmed: true      [ROLE A — sole source; covers A, B, C + schema]
  incumbent: [from status_quo_comparator — CAMPAIGN OPEN]
  adversarial_reviewer_type: [from SESSION INVARIANT A — CAMPAIGN OPEN]
  ce_score_formula: CE-score = -2 if all null [from SESSION INVARIANT B — CAMPAIGN OPEN]
  handoff_schema_locked: true             [9 fields locked; null_tally_final derived from
                                           s2/s3/s4_ce_verdict per CE VERDICT OWNERSHIP TABLE]

Body:
  Hypothesis statement: [one sentence — what {topic} does better than the incumbent]
  Basis: [3-5 signals from the scout record]
  Counter-hypothesis: [what the incumbent would claim in rebuttal]

Artifact written: {topic}-hypothesis-{date}.md.
Confirm: "Hypothesis written. CE VERDICT OWNERSHIP active: s2/s3/s4_ce_verdict fields
          pre-assigned to their respective stages. Advancing to Stage 2."

---

## Stage 2 — Web Search

Write: {topic}-websearch-{date}.md

Search for external evidence on {topic}. For each finding, record:
claim, source URL, CE-relevant (yes/no), quote.

Incumbent comparator: [from CAMPAIGN OPEN]. Note any evidence addressing whether the
incumbent has equivalent capability — this is CE for the hypothesis.

At stage close, record both notes:

NULL TALLY NOTE:
  s2_ce_verdict: [found / null]    [OWNED FIELD — Stage 2 sole producer]
  Running null tally: [count] null. 2 evidence stages remain.
  If null: Protocol status — SESSION INVARIANTs A and B active as pre-committed obligations.

SCHEMA INTEGRITY NOTE:
  Schema fields locked: 9/9 — 0 additions, 0 omissions, 0 source mismatches since CAMPAIGN OPEN.

Artifact written: {topic}-websearch-{date}.md.
Confirm: "Stage 2 complete. s2_ce_verdict: [found/null]. Schema: 9/9. Advancing to Stage 3."

---

## Stage 3 — Internal Intelligence

Write: {topic}-intelligence-{date}.md

Scan internal sources. For each finding, record: artifact path, claim, CE-relevant (yes/no).

At stage close, record both notes:

NULL TALLY NOTE:
  s3_ce_verdict: [found / null]    [OWNED FIELD — Stage 3 sole producer]
  Running null tally: [count] null. 1 evidence stage remains.
  If null: Protocol status — SESSION INVARIANTs A and B active — pre-committed obligations.

SCHEMA INTEGRITY NOTE:
  Schema fields locked: 9/9 — 0 additions, 0 omissions, 0 source mismatches since Stage 2 check.

Artifact written: {topic}-intelligence-{date}.md.
Confirm: "Stage 3 complete. s3_ce_verdict: [found/null]. Schema: 9/9. Advancing to Stage 4."

---

## Stage 4 — Analysis

Write: {topic}-analysis-{date}.md

Analyze all evidence across Stages 2 and 3.
- Supporting evidence strength.
- Counter-evidence summary: all CE found, sources, credibility.
- If CE null across all prior stages: acknowledge explicitly, list all sources checked.

### CAMPAIGN OUTCOME BLOCK

CE VERDICT INPUT — consume owned fields from Stages 2, 3, and final analysis:

  s2_ce_verdict: [found / null]    [produced by Stage 2 — sole source]
  s3_ce_verdict: [found / null]    [produced by Stage 3 — sole source]
  s4_ce_verdict: [found / null]    [produced by Stage 4 analysis — sole source]

Derive from the three verdict fields:

  null_tally_final: count of {s2_ce_verdict, s3_ce_verdict, s4_ce_verdict} where value = null
    derivation: "count of named verdict fields = null, per CE VERDICT OWNERSHIP TABLE formula.
                 NOT derived from dual_lock_fired or co_activation_confirmed."

  incumbent_defense_closed: [true if null_tally_final = 3; false otherwise]
    derivation: "null_tally_final via formula (null_tally_final >= 3 → true).
                 NOT derived from dual_lock_fired or co_activation_confirmed."

SCHEMA INTEGRITY NOTE:
  s4_ce_verdict is the final evidence-stage verdict. 9/9 declared fields intact.
  Schema contract confirmed clean through collection phase.

Artifact written: {topic}-analysis-{date}.md.
Confirm: "Stage 4 complete. CE verdicts: s2=[v], s3=[v], s4=[v].
          null_tally_final = [count] (derived from named verdict fields).
          incumbent_defense_closed = [true/false]. Advancing to Stage 5."

---

## Stage 5 — Synthesis

Write: {topic}-synthesize-{date}.md

Confirm SESSION INVARIANTs A, B, and C are in scope.
Retrieve PRE-COMMITTED HANDOFF SCHEMA and CE VERDICT OWNERSHIP TABLE from CAMPAIGN OPEN.

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

  LOCK 1 — Adversarial Reviewer (SESSION INVARIANT A — execution only):
    Reviewer: {adversarial_reviewer_type}
    Required before promotion.

  LOCK 2 — Confidence Cap (SESSION INVARIANT B — execution only):
    CE-score = -2 (all-null formula). Maximum claim: MEDIUM. HIGH blocked.

  dual_lock_fired: [true if null_tally_final = 3, false otherwise]
  co_activation_confirmed: [must equal dual_lock_fired — format error if they differ]

### Confidence Level

  evidence_score: [0-5]
  ce_score: [0 or -2 per SESSION INVARIANT B formula]
  confidence: [LOW / MEDIUM / HIGH — HIGH blocked if ce_score = -2]

### Handoff

SCHEMA COMPLIANCE CHECK — retrieve PRE-COMMITTED HANDOFF SCHEMA from CAMPAIGN OPEN.
Confirm all 9 declared fields with declared derivation sources.
Any mismatch: record "SCHEMA ERROR: {field} — expected derivation: {expected}, actual: {actual}."

DERIVATION ANNOTATION RULE (SESSION INVARIANT C — execution): every field in this section
must carry a [derived from: X] label. Unlabeled field = format error. Executing invariant,
not declaring it.

Write all 9 declared fields:

  scout_anchor: {topic}-scout-record-{date}.md
    [derived from: ROLE B scout load]

  hypothesis: {topic}-hypothesis-{date}.md
    [derived from: Stage 1 artifact write]

  analysis: {topic}-analysis-{date}.md
    [derived from: Stage 4 artifact write]

  null_tally_final: [0-3]
    positive_derivation: "count of {s2_ce_verdict, s3_ce_verdict, s4_ce_verdict} = null
                          per CE VERDICT OWNERSHIP TABLE formula"
    independence_chain: "NOT derived from dual_lock_fired; NOT derived from co_activation_confirmed"
    [derived from: Stage 4 CAMPAIGN OUTCOME BLOCK — CE verdict fields as declared inputs]

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
     derivation sources; CE VERDICT OWNERSHIP TABLE formula confirmed as null_tally_final
     derivation chain; no additions; no omissions; SESSION INVARIANT C executed]

Confirm: "Synthesis complete. CE verdict chain auditable from CAMPAIGN OUTCOME BLOCK alone:
          null_tally_final derived from s2_ce_verdict + s3_ce_verdict + s4_ce_verdict
          per CE VERDICT OWNERSHIP TABLE — no prose note reconstruction required.
          Evidence brief ready for topic-story.
          Artifact written: {topic}-synthesize-{date}.md."
```

---

## V-02 — Axis: Counter-Hypothesis Closure at Synthesis

**Variation axis**: Counter-hypothesis closure — the hypothesis artifact at Stage 1 declares
a named `counter_hypothesis:` field (the strongest rebuttal the incumbent could offer). The
synthesis at Stage 5 contains a required COUNTER-HYPOTHESIS RESOLUTION section with a
three-way verdict: REFUTED (evidence from Stages 2-4 directly addresses and defeats the
claim), PARTIALLY REFUTED (evidence weakens but does not eliminate the claim), or OPEN
RISK (no evidence gathered addressed the claim). The evidence citation is mandatory in all
three cases.

**Hypothesis**: The prove campaign frames a hypothesis at Stage 1, then gathers evidence at
Stages 2-4 to support or challenge it. But the counter-hypothesis — the incumbent's strongest
rebuttal — is written in Stage 1 and never explicitly revisited. A synthesis can satisfy all
30 v9 criteria while leaving the counter-hypothesis unaddressed: the findings section is
traceable, the CE section is mandatory, the confidence is capped, but whether the specific
threat identified in Stage 1 was answered by the evidence is not tracked. The
COUNTER-HYPOTHESIS RESOLUTION section closes the lifecycle: the Stage 1 rebuttal becomes
a forward obligation that Stage 5 must explicitly resolve or acknowledge as open risk.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
Campaign opens with two blocking roles. Five evidence stages follow in fixed sequence.
The counter-hypothesis formed at Stage 1 must be resolved at Stage 5.

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
  null_tally_final            | Stage 4 CAMPAIGN OUTCOME BLOCK
  incumbent_defense_closed    | null_tally_final (NOT dual_lock_fired; NOT co_activation_confirmed)
  co_activation_confirmed     | dual_lock_fired in synthesis (NOT incumbent_defense_closed;
                              |   NOT null_tally_final directly)
  confidence                  | evidence_score + ce_score formula per SESSION INVARIANT B
  next                        | static: "topic-story"
  schema_compliance_confirmed | synthesis-time compliance check against this CAMPAIGN OPEN schema

COUNTER-HYPOTHESIS CLOSURE RULE — locked now:

The counter_hypothesis field declared at Stage 1 creates a forward obligation for Stage 5.
Stage 5 synthesis must contain a COUNTER-HYPOTHESIS RESOLUTION section with verdict:
  REFUTED / PARTIALLY REFUTED / OPEN RISK
and evidence citation traceable to Stage 2, Stage 3, or Stage 4.
A synthesis that does not resolve the counter-hypothesis is structurally incomplete.

All session invariants and closure rule are now locked. Do not modify.

---

## ROLE A — INVARIANT REGISTRY LOCK

OWNED ATTESTATION FIELD: invariant_registry_confirmed
Sole producer of this field. No other role or stage may produce it.

Execute first. Confirm SESSION INVARIANTs A, B, and C — PRE-COMMITTED HANDOFF SCHEMA —
and COUNTER-HYPOTHESIS CLOSURE RULE are all active.

  invariant_registry_confirmed: true    [ROLE A's owned field — produced here only]

ROLE A COMPLETE. Do not begin ROLE B without invariant_registry_confirmed = true.

---

## ROLE B — SCOUT LOAD

OWNED ATTESTATION FIELD: gate_s_cleared
Sole producer of this field. No other role or stage may produce it.

Execute after ROLE A. Do not begin hypothesis work until this role completes.

Locate: {topic}-scout-record-{date}.md
If not found: STOP. Record: "GATE S FAIL — scout record missing. Campaign cannot proceed."
If found: load record. Extract: market signal, competitor landscape, feasibility finding.

  gate_s_cleared: true    [ROLE B's owned field — produced here only]

ROLE B COMPLETE. Both attestation fields on record — open Stage 1.

---

## GATE S

  gate_s_cleared: true                  (ROLE B — sole source)
  invariant_registry_confirmed: true    (ROLE A — sole source; covers A, B, C + schema + closure rule)

If either is false or missing: STOP.
If both true: advance to Stage 1.

---

## Stage 1 — Hypothesis

Write: {topic}-hypothesis-{date}.md

Frontmatter:
  topic: {topic}
  date: {date}
  scout_anchor: {topic}-scout-record-{date}.md   [loaded in ROLE B]
  gate_s_cleared: true                    [ROLE B — sole source]
  invariant_registry_confirmed: true      [ROLE A — sole source; covers A, B, C + schema + closure]
  incumbent: [from CAMPAIGN OPEN]
  adversarial_reviewer_type: [from SESSION INVARIANT A]
  ce_score_formula: CE-score = -2 if all null [from SESSION INVARIANT B]
  handoff_schema_locked: true             [9 fields locked]

Body:
  Hypothesis statement: [one sentence — what {topic} does better than the incumbent]
  Basis: [3-5 signals from the scout record]
  counter_hypothesis: [the strongest rebuttal the incumbent can offer — one sentence;
                       this field creates a Stage 5 resolution obligation]

Artifact written: {topic}-hypothesis-{date}.md.
Confirm: "Hypothesis written. counter_hypothesis declared — Stage 5 resolution obligated.
          Advancing to Stage 2."

---

## Stage 2 — Web Search

Write: {topic}-websearch-{date}.md

Search for external evidence on {topic}. For each finding, record:
claim, source URL, CE-relevant (yes/no), quote.

Note whether any evidence addresses the counter_hypothesis from Stage 1.
Flag any finding that directly supports or undermines the counter-hypothesis claim.

NULL TALLY NOTE (if no CE found):
  Stage 2 CE result: NULL
  Running null tally: [count] null. 2 evidence stages remain.
  Protocol status: SESSION INVARIANTs A and B remain active — pre-committed obligations.

SCHEMA INTEGRITY NOTE:
  Schema fields locked: 9/9 — 0 additions, 0 omissions, 0 source mismatches since CAMPAIGN OPEN.

Artifact written: {topic}-websearch-{date}.md.
Confirm: "Stage 2 complete. CE: [found/NULL]. Counter-hypothesis addressed: [yes/not yet].
          Schema: 9/9. Advancing to Stage 3."

---

## Stage 3 — Internal Intelligence

Write: {topic}-intelligence-{date}.md

Scan internal sources. For each finding, record: artifact path, claim, CE-relevant (yes/no).

Note whether any finding addresses the counter_hypothesis from Stage 1.

NULL TALLY NOTE (if no CE found):
  Stage 3 CE result: NULL
  Running null tally: [count] null. 1 stage remains.
  Protocol status: SESSION INVARIANTs A and B remain active — pre-committed obligations.

SCHEMA INTEGRITY NOTE:
  Schema fields locked: 9/9 — 0 additions, 0 omissions, 0 source mismatches since Stage 2 check.

Artifact written: {topic}-intelligence-{date}.md.
Confirm: "Stage 3 complete. CE: [found/NULL]. Counter-hypothesis addressed: [yes/not yet].
          Schema: 9/9. Advancing to Stage 4."

---

## Stage 4 — Analysis

Write: {topic}-analysis-{date}.md

Analyze all evidence from Stages 2 and 3.
- Supporting evidence strength.
- Counter-evidence summary: all CE found, sources, credibility.
- Counter-hypothesis tracking: which evidence, if any, directly addresses the Stage 1
  counter-hypothesis claim.
- If CE null: acknowledge explicitly, list sources checked.

### CAMPAIGN OUTCOME BLOCK

  null_tally_final: [0-3 — count of evidence stages returning null CE]
  incumbent_defense_closed: [true if null_tally_final = 3; false otherwise]
  derivation: "null_tally_final via formula. NOT derived from dual_lock_fired or co_activation_confirmed."

SCHEMA INTEGRITY NOTE:
  Stage 4 is the final pre-synthesis schema check. 9/9 fields intact.
  Schema contract confirmed clean through collection phase.

Artifact written: {topic}-analysis-{date}.md.
Confirm: "Stage 4 complete. Campaign outcome: incumbent_defense_closed = [true/false].
          null_tally_final = [count]. Advancing to Stage 5."

---

## Stage 5 — Synthesis

Write: {topic}-synthesize-{date}.md

Confirm SESSION INVARIANTs A, B, and C in scope.
Retrieve PRE-COMMITTED HANDOFF SCHEMA and COUNTER-HYPOTHESIS CLOSURE RULE from CAMPAIGN OPEN.
Load counter_hypothesis field from {topic}-hypothesis-{date}.md.

### Findings

3-5 bullet points, each traceable to a specific artifact.

### COUNTER-HYPOTHESIS RESOLUTION

MANDATORY SECTION — unconditionally required.
Load: counter_hypothesis from {topic}-hypothesis-{date}.md.

  counter_hypothesis: [restate from Stage 1 artifact]

Verdict (choose one):
  [ ] REFUTED — evidence from Stage(s) [X] directly defeats this claim:
        [cite specific finding from {topic}-websearch-{date}.md or {topic}-intelligence-{date}.md]
  [ ] PARTIALLY REFUTED — evidence weakens but does not eliminate this claim:
        [cite finding; state what remains unaddressed]
  [ ] OPEN RISK — no evidence gathered addressed this claim:
        [state what would be needed to refute it; flag as open risk in confidence reasoning]

Confidence is qualified by this verdict: an OPEN RISK counter-hypothesis reduces
confidence by one tier from the evidence_score baseline, regardless of CE state.

### Counter-Evidence

MANDATORY SECTION. Unconditionally required.
If CE found: list with source and credibility.
If null: record null, list sources checked. Apply SESSION INVARIANT A and B.

### ATOMIC DUAL-LOCK (activates if null_tally_final = 3)

  LOCK 1 — Adversarial Reviewer (SESSION INVARIANT A — execution only):
    Reviewer: {adversarial_reviewer_type}
    Required before promotion.

  LOCK 2 — Confidence Cap (SESSION INVARIANT B — execution only):
    CE-score = -2. Maximum claim: MEDIUM. HIGH blocked.

  dual_lock_fired: [true if null_tally_final = 3, false otherwise]
  co_activation_confirmed: [must equal dual_lock_fired — format error if they differ]

### Confidence Level

  evidence_score: [0-5]
  ce_score: [0 or -2 per SESSION INVARIANT B]
  counter_hypothesis_verdict: [REFUTED / PARTIALLY REFUTED / OPEN RISK]
  confidence: [LOW / MEDIUM / HIGH — HIGH blocked if ce_score = -2;
               OPEN RISK verdict reduces one tier from evidence_score baseline]

### Handoff

SCHEMA COMPLIANCE CHECK — retrieve PRE-COMMITTED HANDOFF SCHEMA. Confirm all 9 fields.

DERIVATION ANNOTATION RULE (SESSION INVARIANT C — execution): every field must carry
[derived from: X]. Unlabeled field = format error. Executing invariant, not declaring it.

Write all 9 declared fields:

  scout_anchor: {topic}-scout-record-{date}.md
    [derived from: ROLE B scout load]

  hypothesis: {topic}-hypothesis-{date}.md
    [derived from: Stage 1 artifact write — includes counter_hypothesis field]

  analysis: {topic}-analysis-{date}.md
    [derived from: Stage 4 artifact write]

  null_tally_final: [0-3]
    [derived from: Stage 4 CAMPAIGN OUTCOME BLOCK]

  incumbent_defense_closed: [true if null_tally_final = 3, false otherwise]
    positive_derivation: "null_tally_final via formula null_tally_final >= 3"
    independence_chain: "NOT derived from dual_lock_fired; NOT derived from co_activation_confirmed"
    [derived from: null_tally_final — independence confirmed]

  co_activation_confirmed: [must equal dual_lock_fired]
    positive_derivation: "dual_lock_fired in ATOMIC DUAL-LOCK"
    independence_chain: "NOT derived from incumbent_defense_closed; NOT derived from null_tally_final directly"
    [derived from: dual_lock_fired — independence confirmed]

  confidence: [LOW/MEDIUM/HIGH]
    [derived from: evidence_score + ce_score + counter_hypothesis_verdict adjustment]

  next: topic-story
    [derived from: static handoff target]

  schema_compliance_confirmed: true
    [derived from: synthesis-time compliance check — 9 fields present with declared derivation
     sources; counter_hypothesis resolution completed; no additions; no omissions]

Confirm: "Synthesis complete. Counter-hypothesis resolution: [verdict]. Lifecycle closed:
          Stage 1 counter_hypothesis addressed by Stage 5 verdict with evidence citation.
          Evidence brief ready for topic-story.
          Artifact written: {topic}-synthesize-{date}.md."
```

---

## V-03 — Axis: Null Tally Chain Echo in Synthesis Terminal Artifact

**Variation axis**: Null tally chain echo — the ATOMIC DUAL-LOCK section in Stage 5 includes
a NULL TALLY CHAIN block that reconstructs the per-stage accumulation in sequential order:
"S2: [found/NULL] → running tally N; S3: [found/NULL] → running tally N; S4: [found/NULL]
→ tally N = null_tally_final." This makes the accumulation history visible in the terminal
artifact without requiring per-stage note replay to reconstruct the tally path.

**Hypothesis**: C-20 requires per-stage null tally accumulation — each evidence stage records
its CE result with running count language. The per-stage notes satisfy C-20 and make the
accumulation auditable at each collection checkpoint. But the synthesis artifact (Stage 5)
receives only `null_tally_final` as a scalar — the path from three separate stage decisions
to the terminal count is not visible in the synthesis without loading each prior stage's
note. A NULL TALLY CHAIN block in Stage 5 echoes the per-stage accumulation in order,
making the derivation chain from stage-level CE results to `null_tally_final` visible in
the synthesis itself. A reader auditing the synthesis can reconstruct the tally path from
a single artifact. This is symmetric to C-28's requirement that both lock fields carry
explicit derivation chains: the null tally accumulation also benefits from a named chain.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
Campaign opens with two blocking roles. Five evidence stages follow in fixed sequence.
The null tally accumulation chain is echoed in the terminal synthesis artifact.

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
  null_tally_final            | Stage 4 CAMPAIGN OUTCOME BLOCK
  incumbent_defense_closed    | null_tally_final (NOT dual_lock_fired; NOT co_activation_confirmed)
  co_activation_confirmed     | dual_lock_fired in synthesis (NOT incumbent_defense_closed;
                              |   NOT null_tally_final directly)
  confidence                  | evidence_score + ce_score formula per SESSION INVARIANT B
  next                        | static: "topic-story"
  schema_compliance_confirmed | synthesis-time compliance check against this CAMPAIGN OPEN schema

NULL TALLY CHAIN RULE — locked now:

Stage 5 synthesis must include a NULL TALLY CHAIN block inside ATOMIC DUAL-LOCK that
reconstructs the per-stage accumulation in sequential order:
  S2: [found/null] → running tally [N]
  S3: [found/null] → running tally [N]
  S4: [found/null] → tally [N] = null_tally_final
This block must appear before dual_lock_fired is computed, and its terminal tally value
must equal null_tally_final from Stage 4. Tally mismatch = format error.

All session invariants and NULL TALLY CHAIN RULE are now locked. Do not modify.

---

## ROLE A — INVARIANT REGISTRY LOCK

OWNED ATTESTATION FIELD: invariant_registry_confirmed
Sole producer of this field. No other role or stage may produce it.

Execute first. Confirm SESSION INVARIANTs A, B, and C — PRE-COMMITTED HANDOFF SCHEMA —
and NULL TALLY CHAIN RULE are all active.

  invariant_registry_confirmed: true    [ROLE A's owned field — produced here only]

ROLE A COMPLETE. Do not begin ROLE B without invariant_registry_confirmed = true.

---

## ROLE B — SCOUT LOAD

OWNED ATTESTATION FIELD: gate_s_cleared
Sole producer of this field. No other role or stage may produce it.

Execute after ROLE A.

Locate: {topic}-scout-record-{date}.md
If not found: STOP. "GATE S FAIL — scout record missing."
If found: load record. Extract: market signal, competitor landscape, feasibility finding.

  gate_s_cleared: true    [ROLE B's owned field — produced here only]

ROLE B COMPLETE. Both attestation fields on record — open Stage 1.

---

## GATE S

  gate_s_cleared: true                  (ROLE B — sole source)
  invariant_registry_confirmed: true    (ROLE A — sole source; covers A, B, C + schema + tally chain rule)

If either false or missing: STOP.
If both true: advance to Stage 1.

---

## Stage 1 — Hypothesis

Write: {topic}-hypothesis-{date}.md

Frontmatter:
  topic: {topic}
  date: {date}
  scout_anchor: {topic}-scout-record-{date}.md   [loaded in ROLE B]
  gate_s_cleared: true                    [ROLE B — sole source]
  invariant_registry_confirmed: true      [ROLE A — sole source; covers A, B, C + schema + chain rule]
  incumbent: [from CAMPAIGN OPEN]
  adversarial_reviewer_type: [from SESSION INVARIANT A]
  ce_score_formula: CE-score = -2 if all null [from SESSION INVARIANT B]
  handoff_schema_locked: true             [9 fields locked; null_tally_chain_rule active]

Body:
  Hypothesis statement: [one sentence — what {topic} does better than the incumbent]
  Basis: [3-5 signals from the scout record]
  Counter-hypothesis: [strongest incumbent rebuttal]

Artifact written: {topic}-hypothesis-{date}.md.
Confirm: "Hypothesis written. NULL TALLY CHAIN RULE active — Stage 5 chain echo obligated.
          Advancing to Stage 2."

---

## Stage 2 — Web Search

Write: {topic}-websearch-{date}.md

Search for external evidence on {topic}. Record: claim, source URL, CE-relevant (yes/no).

NULL TALLY NOTE (if no CE found):
  Stage 2 CE result: NULL
  Running null tally: [count] null. 2 evidence stages remain.
  Protocol status: SESSION INVARIANTs A and B remain active — pre-committed obligations.
  Tally chain: S2=null → tally [1]  [this entry will be echoed in Stage 5]

SCHEMA INTEGRITY NOTE:
  Schema fields locked: 9/9 — 0 additions, 0 omissions, 0 source mismatches.

Artifact written: {topic}-websearch-{date}.md.
Confirm: "Stage 2 complete. CE: [found/NULL]. Tally: [N]. Schema: 9/9. Advancing to Stage 3."

---

## Stage 3 — Internal Intelligence

Write: {topic}-intelligence-{date}.md

Scan internal sources. Record: artifact path, claim, CE-relevant (yes/no).

NULL TALLY NOTE (if no CE found):
  Stage 3 CE result: NULL
  Running null tally: [count] null. 1 stage remains.
  Protocol status: SESSION INVARIANTs A and B active — pre-committed obligations.
  Tally chain: S3=null → tally [N]  [this entry will be echoed in Stage 5]

SCHEMA INTEGRITY NOTE:
  Schema fields locked: 9/9 — 0 additions, 0 omissions, 0 source mismatches since Stage 2 check.

Artifact written: {topic}-intelligence-{date}.md.
Confirm: "Stage 3 complete. CE: [found/NULL]. Tally: [N]. Schema: 9/9. Advancing to Stage 4."

---

## Stage 4 — Analysis

Write: {topic}-analysis-{date}.md

Analyze all evidence from Stages 2 and 3.
- Supporting evidence strength.
- Counter-evidence summary. If null: acknowledge explicitly.

### CAMPAIGN OUTCOME BLOCK

  null_tally_final: [0-3 — count of stages returning null CE]
  incumbent_defense_closed: [true if null_tally_final = 3; false otherwise]
  derivation: "null_tally_final via stage CE notes. NOT derived from dual_lock_fired or
               co_activation_confirmed."

SCHEMA INTEGRITY NOTE:
  9/9 fields intact. Schema contract confirmed clean through collection phase.

Artifact written: {topic}-analysis-{date}.md.
Confirm: "Stage 4 complete. null_tally_final = [count]. Advancing to Stage 5."

---

## Stage 5 — Synthesis

Write: {topic}-synthesize-{date}.md

Confirm SESSION INVARIANTs A, B, and C in scope.
Retrieve PRE-COMMITTED HANDOFF SCHEMA and NULL TALLY CHAIN RULE from CAMPAIGN OPEN.

### Findings

3-5 bullet points, each traceable to a specific artifact.

### Counter-Evidence

MANDATORY SECTION. Unconditionally required.
If CE found: list with source and credibility.
If null: record null, list sources. Assign adversarial reviewer (SESSION INVARIANT A).
Apply confidence cap (SESSION INVARIANT B).

### ATOMIC DUAL-LOCK (activates if null_tally_final = 3)

NULL TALLY CHAIN (per NULL TALLY CHAIN RULE — execution, not declaration):

Load per-stage CE verdicts from Stage 2, 3, and 4 notes. Reconstruct in order:

  S2: [found / null] → running tally [N]
  S3: [found / null] → running tally [N]
  S4: [found / null] → tally [N] = null_tally_final

Cross-check: tally chain terminal value must equal null_tally_final from Stage 4
CAMPAIGN OUTCOME BLOCK. If mismatch: TALLY ERROR — record discrepancy before continuing.

  LOCK 1 — Adversarial Reviewer (SESSION INVARIANT A — execution only):
    Reviewer: {adversarial_reviewer_type}
    Required before promotion.

  LOCK 2 — Confidence Cap (SESSION INVARIANT B — execution only):
    CE-score = -2 (all-null formula). HIGH blocked.

  dual_lock_fired: [true if null_tally_final = 3, false otherwise]
  co_activation_confirmed: [must equal dual_lock_fired — format error if they differ]

### Confidence Level

  evidence_score: [0-5]
  ce_score: [0 or -2]
  confidence: [LOW / MEDIUM / HIGH — HIGH blocked if ce_score = -2]

### Handoff

SCHEMA COMPLIANCE CHECK — retrieve PRE-COMMITTED HANDOFF SCHEMA.
Per-stage schema integrity confirmed 9/9 at each of Stages 2, 3, 4.
Synthesis compliance: confirm all 9 declared fields with declared derivation sources.

DERIVATION ANNOTATION RULE (SESSION INVARIANT C — execution): every field must carry
[derived from: X]. Executing invariant, not declaring it.

Write all 9 declared fields:

  scout_anchor: {topic}-scout-record-{date}.md
    [derived from: ROLE B scout load]

  hypothesis: {topic}-hypothesis-{date}.md
    [derived from: Stage 1 artifact write]

  analysis: {topic}-analysis-{date}.md
    [derived from: Stage 4 artifact write]

  null_tally_final: [0-3]
    positive_derivation: "per-stage CE verdicts via NULL TALLY CHAIN — S2+S3+S4 null count"
    independence_chain: "NOT derived from dual_lock_fired; NOT derived from co_activation_confirmed"
    [derived from: Stage 4 CAMPAIGN OUTCOME BLOCK; tally chain echoed above in ATOMIC DUAL-LOCK]

  incumbent_defense_closed: [true if null_tally_final = 3, false otherwise]
    positive_derivation: "null_tally_final via formula null_tally_final >= 3"
    independence_chain: "NOT derived from dual_lock_fired; NOT derived from co_activation_confirmed"
    [derived from: null_tally_final — independence confirmed]

  co_activation_confirmed: [must equal dual_lock_fired]
    positive_derivation: "dual_lock_fired in ATOMIC DUAL-LOCK"
    independence_chain: "NOT derived from incumbent_defense_closed; NOT derived from null_tally_final directly"
    [derived from: dual_lock_fired — independence confirmed]

  confidence: [LOW/MEDIUM/HIGH]
    [derived from: evidence_score + ce_score formula per SESSION INVARIANT B]

  next: topic-story
    [derived from: static handoff target]

  schema_compliance_confirmed: true
    [derived from: synthesis-time compliance check — 9 fields present; per-stage integrity
     confirmed at Stages 2, 3, 4; null tally chain echoed and cross-checked; no additions;
     no omissions; SESSION INVARIANT C executed]

Confirm: "Synthesis complete. NULL TALLY CHAIN echoed in synthesis:
          [S2: v → tally N; S3: v → tally N; S4: v → tally N = null_tally_final].
          Accumulation history visible from synthesis alone without stage replay.
          Evidence brief ready for topic-story.
          Artifact written: {topic}-synthesize-{date}.md."
```

---

## V-04 — Axes Combined: CE Verdict Ownership + Counter-Hypothesis Closure

**Variation axes**: CE verdict ownership (V-01 axis) + counter-hypothesis closure (V-02 axis).

**CE verdict ownership**: Each evidence stage owns a named CE verdict field; the CAMPAIGN
OUTCOME BLOCK names all three as declared inputs to `null_tally_final`. The tally derivation
chain is auditable from the CAMPAIGN OUTCOME BLOCK alone.

**Counter-hypothesis closure**: The hypothesis artifact declares a `counter_hypothesis:` field;
the synthesis contains a required COUNTER-HYPOTHESIS RESOLUTION section with a three-way
verdict traceable to evidence.

These two axes interact at Stage 4 and Stage 5: the CE verdict fields (V-01) make the
tally derivation named; the counter-hypothesis resolution (V-02) closes the hypothesis
lifecycle in Stage 5. Both forward obligations originate at CAMPAIGN OPEN / Stage 1 and
both are discharged at Stage 4 / Stage 5 respectively.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
Campaign opens with two blocking roles. Five evidence stages follow in fixed sequence.
Each evidence stage owns its CE verdict field. The counter-hypothesis from Stage 1 is
resolved at Stage 5.

---

## CAMPAIGN OPEN

Fill before any role or stage begins.

  status_quo_comparator: [name the incumbent approach this topic must displace]

SESSION INVARIANTS — locked now before Stage 0:

  SESSION INVARIANT A — Adversarial Reviewer:
    adversarial_reviewer_type: [role most likely to challenge the claim]
    Activation: fires if ALL three evidence stages return null CE.
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
  hypothesis                  | Stage 1 artifact write (includes counter_hypothesis field)
  analysis                    | Stage 4 artifact write
  null_tally_final            | Stage 4 CAMPAIGN OUTCOME BLOCK — derived from
                              |   {s2_ce_verdict, s3_ce_verdict, s4_ce_verdict}
  incumbent_defense_closed    | null_tally_final (NOT dual_lock_fired; NOT co_activation_confirmed)
  co_activation_confirmed     | dual_lock_fired in synthesis (NOT incumbent_defense_closed;
                              |   NOT null_tally_final directly)
  confidence                  | evidence_score + ce_score + counter_hypothesis_verdict adjustment
  next                        | static: "topic-story"
  schema_compliance_confirmed | synthesis-time compliance check against this CAMPAIGN OPEN schema

CE VERDICT OWNERSHIP TABLE — locked now:

  VERDICT FIELD    | SOLE PRODUCER | PERMISSIBLE VALUES
  -----------------|---------------|--------------------
  s2_ce_verdict    | Stage 2       | found / null
  s3_ce_verdict    | Stage 3       | found / null
  s4_ce_verdict    | Stage 4       | found / null

null_tally_final = count of {s2_ce_verdict, s3_ce_verdict, s4_ce_verdict} where value = null

COUNTER-HYPOTHESIS CLOSURE RULE — locked now:

counter_hypothesis field at Stage 1 creates a Stage 5 resolution obligation.
Stage 5 must include COUNTER-HYPOTHESIS RESOLUTION with verdict:
  REFUTED / PARTIALLY REFUTED / OPEN RISK
and evidence citation from Stages 2-4. No resolution = structurally incomplete.

All invariants and rules are now locked. Do not modify.

---

## ROLE A — INVARIANT REGISTRY LOCK

OWNED ATTESTATION FIELD: invariant_registry_confirmed
Sole producer of this field. No other role or stage may produce it.

Execute first. Confirm SESSION INVARIANTs A, B, C — PRE-COMMITTED HANDOFF SCHEMA —
CE VERDICT OWNERSHIP TABLE — and COUNTER-HYPOTHESIS CLOSURE RULE all active.

  invariant_registry_confirmed: true    [ROLE A's owned field — produced here only]

ROLE A COMPLETE. Do not begin ROLE B without invariant_registry_confirmed = true.

---

## ROLE B — SCOUT LOAD

OWNED ATTESTATION FIELD: gate_s_cleared
Sole producer of this field. No other role or stage may produce it.

Locate: {topic}-scout-record-{date}.md
If not found: STOP. "GATE S FAIL — scout record missing."
If found: load record. Extract: market signal, competitor landscape, feasibility finding.

  gate_s_cleared: true    [ROLE B's owned field — produced here only]

ROLE B COMPLETE. Both attestation fields on record — open Stage 1.

---

## GATE S

  gate_s_cleared: true                  (ROLE B — sole source)
  invariant_registry_confirmed: true    (ROLE A — sole source; covers all invariants + rules)

If either false or missing: STOP. If both true: advance to Stage 1.

---

## Stage 1 — Hypothesis

Write: {topic}-hypothesis-{date}.md

Frontmatter:
  topic: {topic}
  date: {date}
  scout_anchor: {topic}-scout-record-{date}.md
  gate_s_cleared: true                    [ROLE B]
  invariant_registry_confirmed: true      [ROLE A; covers all session invariants + CE ownership + closure]
  incumbent: [from CAMPAIGN OPEN]
  adversarial_reviewer_type: [from SESSION INVARIANT A]
  ce_score_formula: CE-score = -2 if all null
  handoff_schema_locked: true             [9 fields; CE verdict ownership + counter_hypothesis closure active]

Body:
  Hypothesis statement: [one sentence]
  Basis: [3-5 signals from scout record]
  counter_hypothesis: [strongest incumbent rebuttal — one sentence; creates Stage 5 obligation]

Artifact written: {topic}-hypothesis-{date}.md.
Confirm: "Hypothesis written. counter_hypothesis declared. CE verdict ownership active.
          Advancing to Stage 2."

---

## Stage 2 — Web Search

Write: {topic}-websearch-{date}.md

Search for external evidence. Record: claim, source URL, CE-relevant (yes/no).
Flag any finding that addresses the counter_hypothesis.

At stage close:

NULL TALLY NOTE:
  s2_ce_verdict: [found / null]    [OWNED FIELD — Stage 2 sole producer]
  Running null tally: [count] null. 2 stages remain.
  If null: SESSION INVARIANTs A and B active — pre-committed obligations.

SCHEMA INTEGRITY NOTE:
  Schema fields locked: 9/9 — 0 additions, 0 omissions since CAMPAIGN OPEN.

Artifact written: {topic}-websearch-{date}.md.
Confirm: "Stage 2 complete. s2_ce_verdict: [v]. Schema: 9/9. Advancing to Stage 3."

---

## Stage 3 — Internal Intelligence

Write: {topic}-intelligence-{date}.md

Scan internal sources. Record: artifact path, claim, CE-relevant (yes/no).
Flag any finding that addresses the counter_hypothesis.

At stage close:

NULL TALLY NOTE:
  s3_ce_verdict: [found / null]    [OWNED FIELD — Stage 3 sole producer]
  Running null tally: [count] null. 1 stage remains.
  If null: SESSION INVARIANTs A and B active — pre-committed obligations.

SCHEMA INTEGRITY NOTE:
  Schema fields locked: 9/9 — 0 additions, 0 omissions since Stage 2 check.

Artifact written: {topic}-intelligence-{date}.md.
Confirm: "Stage 3 complete. s3_ce_verdict: [v]. Schema: 9/9. Advancing to Stage 4."

---

## Stage 4 — Analysis

Write: {topic}-analysis-{date}.md

Analyze all evidence. Summarize CE state. Track evidence addressing counter_hypothesis.
If CE null: acknowledge explicitly.

### CAMPAIGN OUTCOME BLOCK

CE VERDICT INPUT:
  s2_ce_verdict: [v]    [Stage 2 — sole source]
  s3_ce_verdict: [v]    [Stage 3 — sole source]
  s4_ce_verdict: [v]    [Stage 4 — sole source]

  null_tally_final: count of above where value = null
    derivation: "count of named verdict fields = null per CE VERDICT OWNERSHIP TABLE.
                 NOT derived from dual_lock_fired or co_activation_confirmed."

  incumbent_defense_closed: [true if null_tally_final = 3; false otherwise]
    derivation: "null_tally_final formula. NOT derived from dual_lock_fired."

Counter-hypothesis tracking: which evidence, if any, addresses the Stage 1 claim.

SCHEMA INTEGRITY NOTE:
  Final collection-phase schema check. 9/9 intact.

Artifact written: {topic}-analysis-{date}.md.
Confirm: "Stage 4 complete. s2=[v], s3=[v], s4=[v]. null_tally_final=[count].
          incumbent_defense_closed=[v]. Advancing to Stage 5."

---

## Stage 5 — Synthesis

Write: {topic}-synthesize-{date}.md

Confirm SESSION INVARIANTs A, B, C in scope.
Retrieve PRE-COMMITTED HANDOFF SCHEMA, CE VERDICT OWNERSHIP TABLE, and
COUNTER-HYPOTHESIS CLOSURE RULE from CAMPAIGN OPEN.
Load counter_hypothesis from {topic}-hypothesis-{date}.md.

### Findings

3-5 bullet points, each traceable to a specific artifact.

### COUNTER-HYPOTHESIS RESOLUTION

MANDATORY — unconditionally required per COUNTER-HYPOTHESIS CLOSURE RULE.

  counter_hypothesis: [from {topic}-hypothesis-{date}.md]

  Verdict (one):
  [ ] REFUTED — Stage(s) [X] evidence defeats this claim:
        [cite finding with artifact path]
  [ ] PARTIALLY REFUTED — evidence weakens but does not eliminate:
        [cite finding; state what remains open]
  [ ] OPEN RISK — no gathered evidence addresses this claim:
        [state what would be needed; flag as open risk]

### Counter-Evidence

MANDATORY SECTION. Unconditionally required.
If found: list with source and credibility.
If null: record null, list sources, apply SESSION INVARIANT A and B.

### ATOMIC DUAL-LOCK (activates if null_tally_final = 3)

  LOCK 1: Reviewer — {adversarial_reviewer_type} (SESSION INVARIANT A — execution only).
  LOCK 2: Confidence cap — CE-score = -2, HIGH blocked (SESSION INVARIANT B — execution only).

  dual_lock_fired: [true if null_tally_final = 3, false otherwise]
  co_activation_confirmed: [must equal dual_lock_fired — format error if they differ]

### Confidence Level

  evidence_score: [0-5]
  ce_score: [0 or -2]
  counter_hypothesis_verdict: [REFUTED / PARTIALLY REFUTED / OPEN RISK]
  confidence: [LOW / MEDIUM / HIGH — HIGH blocked if ce_score = -2;
               OPEN RISK reduces one tier from evidence_score baseline]

### Handoff

SCHEMA COMPLIANCE CHECK — retrieve PRE-COMMITTED HANDOFF SCHEMA. Confirm all 9 fields.

DERIVATION ANNOTATION RULE (SESSION INVARIANT C — execution): every field must carry
[derived from: X]. Executing invariant, not declaring it.

Write all 9 declared fields:

  scout_anchor: {topic}-scout-record-{date}.md
    [derived from: ROLE B scout load]

  hypothesis: {topic}-hypothesis-{date}.md
    [derived from: Stage 1 artifact write — includes counter_hypothesis field]

  analysis: {topic}-analysis-{date}.md
    [derived from: Stage 4 artifact write]

  null_tally_final: [0-3]
    positive_derivation: "count of {s2_ce_verdict, s3_ce_verdict, s4_ce_verdict} = null
                          per CE VERDICT OWNERSHIP TABLE formula"
    independence_chain: "NOT derived from dual_lock_fired; NOT derived from co_activation_confirmed"
    [derived from: Stage 4 CAMPAIGN OUTCOME BLOCK — named verdict fields as inputs]

  incumbent_defense_closed: [true if null_tally_final = 3, false otherwise]
    positive_derivation: "null_tally_final via formula null_tally_final >= 3"
    independence_chain: "NOT derived from dual_lock_fired; NOT derived from co_activation_confirmed"
    [derived from: null_tally_final — independence confirmed]

  co_activation_confirmed: [must equal dual_lock_fired]
    positive_derivation: "dual_lock_fired in ATOMIC DUAL-LOCK"
    independence_chain: "NOT derived from incumbent_defense_closed; NOT derived from null_tally_final directly"
    [derived from: dual_lock_fired — independence confirmed]

  confidence: [LOW/MEDIUM/HIGH]
    [derived from: evidence_score + ce_score + counter_hypothesis_verdict adjustment]

  next: topic-story
    [derived from: static handoff target]

  schema_compliance_confirmed: true
    [derived from: synthesis-time compliance check — 9 fields present; CE verdict ownership
     chain confirmed; counter-hypothesis lifecycle closed; no additions; no omissions;
     SESSION INVARIANT C executed]

Confirm: "Synthesis complete. CE verdict chain: s2=[v] + s3=[v] + s4=[v] → null_tally_final=[N].
          Counter-hypothesis verdict: [REFUTED/PARTIALLY REFUTED/OPEN RISK].
          Evidence brief ready for topic-story.
          Artifact written: {topic}-synthesize-{date}.md."
```

---

## V-05 — Combined: All Four R10 Axes

**Variation axes**: CE verdict ownership (V-01) + counter-hypothesis closure (V-02) +
null tally chain echo (V-03) + schema compliance cross-referenced to per-stage notes (V-04).

**CE verdict ownership**: Named s2/s3/s4_ce_verdict fields declared in CAMPAIGN OPEN as
sole-producer, sole-consumer chain feeding null_tally_final in the CAMPAIGN OUTCOME BLOCK.

**Counter-hypothesis closure**: counter_hypothesis field at Stage 1 creates a Stage 5
COUNTER-HYPOTHESIS RESOLUTION obligation with three-way verdict.

**Null tally chain echo**: Stage 5 ATOMIC DUAL-LOCK reconstructs the per-stage accumulation
chain ("S2: v → tally N; S3: v → tally N; S4: v → tally N = null_tally_final") before
computing dual_lock_fired.

**Schema compliance cross-referenced**: schema_compliance_confirmed annotation names the
per-stage SCHEMA INTEGRITY NOTEs (Stage 2, Stage 3, Stage 4) as the upstream evidence for
the synthesis compliance confirmation, making the backward chain traceable from the
terminal compliance check.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
Campaign opens with two blocking roles. Five evidence stages follow in fixed sequence.
Forward only — no skipping, no re-running.

Four R10 structural disciplines are active:
  (1) CE verdict ownership: s2/s3/s4_ce_verdict as named fields feeding null_tally_final
  (2) Counter-hypothesis closure: Stage 1 counter_hypothesis obligated at Stage 5
  (3) Null tally chain echo: accumulation history visible in Stage 5 synthesis artifact
  (4) Schema compliance cross-referenced: synthesis compliance cites per-stage integrity notes

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

  SESSION INVARIANT C — Derivation Annotation:
    annotation_rule: Every handoff field must carry [derived from: X]. Unlabeled field = format error.
    Invariant language: pre-registered — cannot be modified or bypassed at synthesis.

PRE-COMMITTED HANDOFF SCHEMA — session-level invariant, locked now:

Synthesis must produce exactly these 9 fields with exactly these derivation sources.
No additions. No omissions. Derivation-source mismatch = format error.
schema_compliance_confirmed is pre-declared as field 9 — self-registered.
Omitting it is a schema violation. Adding a substitute is an undeclared-field violation.

  FIELD                       | REQUIRED DERIVATION SOURCE
  ----------------------------|------------------------------------------------------
  scout_anchor                | ROLE B scout load
  hypothesis                  | Stage 1 artifact write (includes counter_hypothesis field)
  analysis                    | Stage 4 artifact write
  null_tally_final            | Stage 4 CAMPAIGN OUTCOME BLOCK — derived from
                              |   {s2_ce_verdict, s3_ce_verdict, s4_ce_verdict}
  incumbent_defense_closed    | null_tally_final (NOT dual_lock_fired; NOT co_activation_confirmed)
  co_activation_confirmed     | dual_lock_fired in synthesis (NOT incumbent_defense_closed;
                              |   NOT null_tally_final directly)
  confidence                  | evidence_score + ce_score + counter_hypothesis_verdict adjustment
  next                        | static: "topic-story"
  schema_compliance_confirmed | synthesis-time compliance check cross-referenced to Stage 2,
                              |   Stage 3, Stage 4 SCHEMA INTEGRITY NOTEs

CE VERDICT OWNERSHIP TABLE — locked now:

  VERDICT FIELD    | SOLE PRODUCER | PERMISSIBLE VALUES
  -----------------|---------------|--------------------
  s2_ce_verdict    | Stage 2       | found / null
  s3_ce_verdict    | Stage 3       | found / null
  s4_ce_verdict    | Stage 4       | found / null

null_tally_final = count of {s2_ce_verdict, s3_ce_verdict, s4_ce_verdict} where value = null

NULL TALLY CHAIN RULE — locked now:

Stage 5 ATOMIC DUAL-LOCK must include a NULL TALLY CHAIN block:
  S2: [found/null] → running tally [N]
  S3: [found/null] → running tally [N]
  S4: [found/null] → tally [N] = null_tally_final
Chain terminal value must equal null_tally_final from Stage 4. Mismatch = format error.

COUNTER-HYPOTHESIS CLOSURE RULE — locked now:

counter_hypothesis field at Stage 1 creates a Stage 5 resolution obligation.
Stage 5 must include COUNTER-HYPOTHESIS RESOLUTION with verdict:
  REFUTED / PARTIALLY REFUTED / OPEN RISK
with evidence citation from Stages 2-4. No resolution = structurally incomplete.

All invariants, tables, and rules are now locked. Do not modify after this point.

---

## ROLE A — INVARIANT REGISTRY LOCK

OWNED ATTESTATION FIELD: invariant_registry_confirmed
Sole producer of this field. No other role or stage may produce it.

Execute first. Confirm all active before any stage opens:
  - SESSION INVARIANTs A, B, and C
  - PRE-COMMITTED HANDOFF SCHEMA (9 fields including self-registered field 9)
  - CE VERDICT OWNERSHIP TABLE (s2/s3/s4_ce_verdict sole-producer assignments)
  - NULL TALLY CHAIN RULE (Stage 5 accumulation echo obligated)
  - COUNTER-HYPOTHESIS CLOSURE RULE (Stage 1 counter_hypothesis → Stage 5 resolution)

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
If found: load record. Extract: market signal, competitor landscape, feasibility finding.

  gate_s_cleared: true    [ROLE B's owned field — produced here only]

ROLE B COMPLETE. Both attestation fields on record — open Stage 1.

---

## GATE S

Requires ROLE A and ROLE B both complete.

  gate_s_cleared: true                  (ROLE B — sole source)
  invariant_registry_confirmed: true    (ROLE A — sole source; covers all invariants + tables + rules)

Dropping ROLE A: invariant_registry_confirmed absent — auditable structural gap.
Dropping ROLE B: gate_s_cleared absent — auditable structural gap.

If either field is false or missing: STOP.
If both fields are true: advance to Stage 1.

---

## Stage 1 — Hypothesis

Write: {topic}-hypothesis-{date}.md

Frontmatter:
  topic: {topic}
  date: {date}
  scout_anchor: {topic}-scout-record-{date}.md   [loaded in ROLE B]
  gate_s_cleared: true                    [ROLE B — sole source]
  invariant_registry_confirmed: true      [ROLE A — sole source; all invariants + rules active]
  incumbent: [from status_quo_comparator — CAMPAIGN OPEN]
  adversarial_reviewer_type: [from SESSION INVARIANT A — CAMPAIGN OPEN]
  ce_score_formula: CE-score = -2 if all null [from SESSION INVARIANT B — CAMPAIGN OPEN]
  handoff_schema_locked: true             [9 fields including self-registered field 9;
                                           CE verdict ownership + tally chain rule + closure rule active]

Body:
  Hypothesis statement: [one sentence — what {topic} does better than the incumbent]
  Basis: [3-5 signals from the scout record]
  counter_hypothesis: [strongest incumbent rebuttal — one sentence; creates Stage 5 obligation]

Artifact written: {topic}-hypothesis-{date}.md.
Confirm: "Hypothesis written. counter_hypothesis declared — Stage 5 COUNTER-HYPOTHESIS
          RESOLUTION obligated. CE verdict ownership active: s2/s3/s4_ce_verdict assigned
          to their stages. Advancing to Stage 2."

---

## Stage 2 — Web Search

Write: {topic}-websearch-{date}.md

Search for external evidence on {topic}. For each finding, record:
claim, source URL, CE-relevant (yes/no), quote.

Incumbent comparator: [from CAMPAIGN OPEN]. Note evidence addressing incumbent equivalency.
Flag any finding that addresses the counter_hypothesis from Stage 1.

At stage close, record both notes:

NULL TALLY NOTE:
  s2_ce_verdict: [found / null]    [OWNED FIELD — Stage 2 sole producer]
  Running null tally: [count] null. 2 evidence stages remain.
  If null: SESSION INVARIANTs A and B active as pre-committed obligations.

SCHEMA INTEGRITY NOTE (Stage 2):
  Schema fields locked: 9/9 — 0 additions, 0 omissions, 0 source mismatches since CAMPAIGN OPEN.
  [This note will be cross-referenced by schema_compliance_confirmed at synthesis.]

Artifact written: {topic}-websearch-{date}.md.
Confirm: "Stage 2 complete. s2_ce_verdict: [found/null]. Schema: 9/9 confirmed.
          Advancing to Stage 3."

---

## Stage 3 — Internal Intelligence

Write: {topic}-intelligence-{date}.md

Scan internal sources. For each finding, record: artifact path, claim, CE-relevant (yes/no).
Flag any finding that addresses the counter_hypothesis.

At stage close, record both notes:

NULL TALLY NOTE:
  s3_ce_verdict: [found / null]    [OWNED FIELD — Stage 3 sole producer]
  Running null tally: [count] null. 1 evidence stage remains.
  If null: SESSION INVARIANTs A and B active as pre-committed obligations.

SCHEMA INTEGRITY NOTE (Stage 3):
  Schema fields locked: 9/9 — 0 additions, 0 omissions, 0 source mismatches since Stage 2 check.
  [This note will be cross-referenced by schema_compliance_confirmed at synthesis.]

Artifact written: {topic}-intelligence-{date}.md.
Confirm: "Stage 3 complete. s3_ce_verdict: [found/null]. Schema: 9/9 confirmed.
          Advancing to Stage 4."

---

## Stage 4 — Analysis

Write: {topic}-analysis-{date}.md

Analyze all evidence across Stages 2 and 3.
- Supporting evidence strength.
- Counter-evidence summary: all CE found, sources, credibility.
- Counter-hypothesis tracking: which evidence addresses the Stage 1 claim.
- If CE null across all prior stages: acknowledge explicitly, list sources checked.

### CAMPAIGN OUTCOME BLOCK

CE VERDICT INPUT — consume all three owned verdict fields:

  s2_ce_verdict: [found / null]    [Stage 2 — sole source]
  s3_ce_verdict: [found / null]    [Stage 3 — sole source]
  s4_ce_verdict: [found / null]    [Stage 4 analysis — sole source]

Derive:

  null_tally_final: count of {s2_ce_verdict, s3_ce_verdict, s4_ce_verdict} where value = null
    derivation: "count of named verdict fields = null per CE VERDICT OWNERSHIP TABLE formula.
                 NOT derived from dual_lock_fired or co_activation_confirmed."

  incumbent_defense_closed: [true if null_tally_final = 3; false otherwise]
    derivation: "null_tally_final via formula (null_tally_final >= 3 → true).
                 NOT derived from dual_lock_fired or co_activation_confirmed."

SCHEMA INTEGRITY NOTE (Stage 4):
  Final collection-phase schema check. 9/9 declared fields intact — 0 additions, 0 omissions.
  Schema contract confirmed clean through full collection phase.
  [This note will be cross-referenced by schema_compliance_confirmed at synthesis.]

Artifact written: {topic}-analysis-{date}.md.
Confirm: "Stage 4 complete. s2=[v], s3=[v], s4=[v].
          null_tally_final = [count] (derived from named verdict fields).
          incumbent_defense_closed = [true/false]. Schema: 9/9 through collection.
          Advancing to Stage 5."

---

## Stage 5 — Synthesis

Write: {topic}-synthesize-{date}.md

Confirm SESSION INVARIANTs A, B, and C in scope.
Retrieve PRE-COMMITTED HANDOFF SCHEMA, CE VERDICT OWNERSHIP TABLE,
NULL TALLY CHAIN RULE, and COUNTER-HYPOTHESIS CLOSURE RULE from CAMPAIGN OPEN.
Load counter_hypothesis from {topic}-hypothesis-{date}.md.

### Findings

3-5 bullet points, each traceable to a specific artifact (path or stage reference).

### COUNTER-HYPOTHESIS RESOLUTION

MANDATORY SECTION — unconditionally required per COUNTER-HYPOTHESIS CLOSURE RULE.

  counter_hypothesis: [restate from {topic}-hypothesis-{date}.md]

  Verdict (one — cite evidence source):
  [ ] REFUTED — Stage(s) [X] evidence defeats this claim:
        [cite finding: artifact path, claim summary, credibility]
  [ ] PARTIALLY REFUTED — evidence weakens but does not eliminate:
        [cite finding; state what remains open]
  [ ] OPEN RISK — no gathered evidence addresses this claim:
        [state what would be needed to refute it; flag as open risk below]

  counter_hypothesis_verdict: [REFUTED / PARTIALLY REFUTED / OPEN RISK]
  Note: OPEN RISK reduces confidence one tier from evidence_score baseline,
        independent of CE state.

### Counter-Evidence

MANDATORY SECTION. Unconditionally required.
If CE found: list each item with source artifact and credibility rating.
If CE null: state: "No counter-evidence found. Sources checked: [Stage 2 sources],
[Stage 3 sources]. This null result is the primary risk to the hypothesis."

If CE is null:
  - Adversarial review required before any promotion decision.
    Assign: {adversarial_reviewer_type} (SESSION INVARIANT A — execution, not new decision).
  - Confidence mechanically capped by SESSION INVARIANT B: CE-score = -2. Cannot be bypassed.

### ATOMIC DUAL-LOCK (activates if null_tally_final = 3)

NULL TALLY CHAIN (per NULL TALLY CHAIN RULE — execution, not declaration):

Load per-stage CE verdicts from Stage 2, 3, and 4. Reconstruct in order:

  S2: [found / null] → running tally [N]
  S3: [found / null] → running tally [N]
  S4: [found / null] → tally [N] = null_tally_final

Cross-check: chain terminal value must equal null_tally_final from Stage 4 CAMPAIGN
OUTCOME BLOCK. Mismatch = TALLY ERROR — record discrepancy before continuing.

  LOCK 1 — Adversarial Reviewer (SESSION INVARIANT A — execution only):
    Reviewer: {adversarial_reviewer_type}
    Required before promotion. Pre-committed.

  LOCK 2 — Confidence Cap (SESSION INVARIANT B — execution only):
    ce_score_formula applied: CE-score = -2 (all-null). Maximum claim: MEDIUM. HIGH blocked.

  dual_lock_fired: [true if null_tally_final = 3, false otherwise]
  co_activation_confirmed: [must equal dual_lock_fired — format error if they differ]
  Note: co_activation_confirmed and incumbent_defense_closed are parallel consumers of
        null_tally_final (via CE verdict ownership chain). Neither derives the other.

### Confidence Level

  evidence_score: [0-5]
  ce_score: [0 or -2 per SESSION INVARIANT B formula]
  counter_hypothesis_verdict: [REFUTED / PARTIALLY REFUTED / OPEN RISK]
  confidence: [LOW / MEDIUM / HIGH — HIGH blocked if ce_score = -2;
               OPEN RISK verdict reduces one tier from evidence_score baseline]

### Handoff

SCHEMA COMPLIANCE CHECK — retrieve PRE-COMMITTED HANDOFF SCHEMA from CAMPAIGN OPEN.
Confirm all 9 declared fields with declared derivation sources.
schema_compliance_confirmed is pre-declared as field 9. Omitting it is a schema violation.
Cross-reference per-stage SCHEMA INTEGRITY NOTEs:
  Stage 2 SCHEMA INTEGRITY NOTE: [9/9 confirmed at Stage 2]
  Stage 3 SCHEMA INTEGRITY NOTE: [9/9 confirmed at Stage 3]
  Stage 4 SCHEMA INTEGRITY NOTE: [9/9 confirmed at Stage 4]
Schema integrity confirmed across full collection phase before synthesis.
Any mismatch at any stage: record "SCHEMA ERROR: {field} — stage: {N}, expected: {expected}."

DERIVATION ANNOTATION RULE (SESSION INVARIANT C — execution): every field in this section
must carry a [derived from: X] label. Unlabeled field = format error.
Executing invariant, not declaring it.

Write all 9 declared fields:

  scout_anchor: {topic}-scout-record-{date}.md
    [derived from: ROLE B scout load]

  hypothesis: {topic}-hypothesis-{date}.md
    [derived from: Stage 1 artifact write — includes counter_hypothesis field;
     counter_hypothesis resolution completed at Stage 5 COUNTER-HYPOTHESIS RESOLUTION]

  analysis: {topic}-analysis-{date}.md
    [derived from: Stage 4 artifact write]

  null_tally_final: [0-3]
    positive_derivation: "count of {s2_ce_verdict, s3_ce_verdict, s4_ce_verdict} = null
                          per CE VERDICT OWNERSHIP TABLE; chain echoed in ATOMIC DUAL-LOCK:
                          S2=[v]→N, S3=[v]→N, S4=[v]→N = [null_tally_final]"
    independence_chain: "NOT derived from dual_lock_fired; NOT derived from co_activation_confirmed"
    [derived from: Stage 4 CAMPAIGN OUTCOME BLOCK — named verdict fields as declared inputs;
     accumulation chain verified via NULL TALLY CHAIN above]

  incumbent_defense_closed: [true if null_tally_final = 3, false otherwise]
    positive_derivation: "null_tally_final via formula null_tally_final >= 3"
    independence_chain: "NOT derived from dual_lock_fired; NOT derived from co_activation_confirmed"
    [derived from: null_tally_final — independence confirmed per CAMPAIGN OPEN schema constraint]

  co_activation_confirmed: [must equal dual_lock_fired]
    positive_derivation: "dual_lock_fired in ATOMIC DUAL-LOCK"
    independence_chain: "NOT derived from incumbent_defense_closed; NOT derived from null_tally_final directly"
    [derived from: dual_lock_fired — independence confirmed per CAMPAIGN OPEN schema constraint]

  confidence: [LOW/MEDIUM/HIGH]
    [derived from: evidence_score + ce_score formula (SESSION INVARIANT B) +
     counter_hypothesis_verdict adjustment]

  next: topic-story
    [derived from: static handoff target]

  schema_compliance_confirmed: true
    positive_derivation: "synthesis-time compliance check — all 9 fields present with declared
                           derivation sources; SESSION INVARIANT C executed; no additions;
                           no omissions; CE verdict ownership chain confirmed in null_tally_final
                           derivation; counter_hypothesis lifecycle closed"
    collection_phase_chain: "Stage 2 SCHEMA INTEGRITY NOTE: 9/9 confirmed;
                              Stage 3 SCHEMA INTEGRITY NOTE: 9/9 confirmed;
                              Stage 4 SCHEMA INTEGRITY NOTE: 9/9 confirmed —
                              schema integrity auditable from synthesis to collection phase
                              without stage replay"
    [derived from: synthesis-time compliance check cross-referenced to Stage 2, Stage 3,
     Stage 4 SCHEMA INTEGRITY NOTEs — pre-declared as field 9; self-registration confirmed]

Confirm: "Synthesis complete.
          CE verdict chain: s2=[v] + s3=[v] + s4=[v] → null_tally_final=[N]
            (auditable from CAMPAIGN OUTCOME BLOCK alone via named verdict fields).
          Null tally chain echoed: S2=[v]→tally [N], S3=[v]→tally [N], S4=[v]→tally [N]=[N]
            (accumulation history visible from synthesis artifact without stage replay).
          Counter-hypothesis verdict: [REFUTED / PARTIALLY REFUTED / OPEN RISK]
            (Stage 1 lifecycle closed at Stage 5).
          Schema compliance cross-referenced: Stage 2 9/9 + Stage 3 9/9 + Stage 4 9/9
            (backward chain from synthesis to collection phase traceable from synthesis alone).
          Evidence brief ready for topic-story.
          Artifact written: {topic}-synthesize-{date}.md."
```

---

## Round 10 — Axis Summary

| Variation | Axis | New structural discipline |
|-----------|------|--------------------------|
| V-01 | CE verdict ownership | s2/s3/s4_ce_verdict as named owned fields; null_tally_final derivation chain auditable from CAMPAIGN OUTCOME BLOCK alone |
| V-02 | Counter-hypothesis closure | counter_hypothesis at Stage 1 obligates COUNTER-HYPOTHESIS RESOLUTION at Stage 5 with three-way verdict |
| V-03 | Null tally chain echo | Stage 5 ATOMIC DUAL-LOCK reconstructs per-stage accumulation chain; history visible in terminal artifact |
| V-04 | CE verdict + counter-hypothesis | Two-axis combination; CE tally chain named; lifecycle closed in synthesis |
| V-05 | All four combined | Full R10 stack: verdict ownership + hypothesis closure + tally chain echo + schema cross-reference |

## Gap Analysis: What a C-01–C-30 Ceiling Variation Can Still Fail

A variation satisfying all 30 v9 criteria can still omit all four R10 patterns simultaneously:

1. `null_tally_final` recorded as a prose count — derivation from individual stage decisions
   is implicit, not field-named. A reader cannot reconstruct the three-stage source chain
   from the CAMPAIGN OUTCOME BLOCK alone.

2. `counter_hypothesis` from Stage 1 unaddressed at synthesis — the CE section is present,
   the findings are traceable, but the specific incumbent rebuttal identified at campaign
   open has no explicit resolution verdict.

3. Synthesis records `null_tally_final = 3` without showing "S2 NULL + S3 NULL + S4 NULL = 3"
   — the accumulation history is distributed across per-stage notes; no single artifact
   contains the chain.

4. `schema_compliance_confirmed` confirms "9/9 fields present" but names no per-stage
   SCHEMA INTEGRITY NOTEs — the backward chain from the terminal compliance check to the
   collection-phase audit trail is not traceable from the synthesis alone.
