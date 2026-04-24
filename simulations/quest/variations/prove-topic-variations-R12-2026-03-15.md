Good — I have the full picture. R11 V-01 is the C-34 exemplar (180/180 under v10). All R12 variations must hit 184/184. Let me write the five complete variations now.

---

```markdown
---
skill: quest-variate
skill_target: prove-topic
round: R12
date: 2026-03-16
rubric: prove-topic-rubric-v11-2026-03-16.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [role_sequence, scorecard_format, sparse_lifecycle]
  combined: [V-04 (role_sequence + phrasing_register), V-05 (all_three + inertia_score)]
r11_anchor: >
  R11 V-01 is the exemplar for C-34: named INCUMBENT CHECK blocks at Stages 2, 3, and 4,
  with Stage 4 asking the displacement verdict question explicitly. R11 V-01 scored 180/180
  under v10. All R12 variations build on the complete v10+C-34 foundation — all target
  184/184 under v11. Presentation axis only; no structural criterion is relaxed.
r12_targets: >
  (1) Role sequence: C-34 requires named INCUMBENT CHECK blocks traceable to an incumbent
  locked at CAMPAIGN OPEN. In R11 V-01 the INCUMBENT THREAT BLOCK is populated in the open
  CAMPAIGN OPEN section alongside other session metadata — no dedicated role owns it. Adding
  ROLE C (INCUMBENT THREAT ANALYST) as a third blocking step gives the INCUMBENT CHECK
  blocks a role-level origin auditable via a gate field. Tests whether three-role incumbent
  locking strengthens the C-34 chain beyond R11's exemplar.

  (2) Scorecard format: Each evidence stage appends a row to a running CAMPAIGN SCORECARD
  table. Incumbent displacement signal, CE verdict, null tally, and schema count are
  columns — not prose notes. Stage 4's scorecard row includes the displacement verdict
  (Yes/No/Pending). Synthesis finalizes the scorecard and reads it as the evidence brief.
  Tests whether a running table makes per-stage audit cleaner than prose confirmation lines.

  (3) Sparse lifecycle: Minimal stage boundary prose. No explicit ENTER/WORK/CLOSE labels.
  INCUMBENT CHECK is the dominant section in each evidence stage. Structural tally and
  schema notes are compressed to a single footer line per stage. Tests whether structural
  obligations hold when ceremony is stripped and only the obligations themselves remain.

---

## V-01 — Axis: Role Sequence (Three-Role Gate)

**Variation axis**: A third blocking role — ROLE C (INCUMBENT THREAT ANALYST) — is inserted
after ROLE B and before Stage 1. ROLE C owns the INCUMBENT THREAT BLOCK: using the
competitor landscape loaded by ROLE B, it writes `incumbent_name`, `incumbent_strength`,
and `incumbent_vulnerability` and produces `incumbent_threat_locked: true` as its sole
owned attestation field. GATE S expands to require all three attestation fields before
Stage 1 opens. The INCUMBENT CHECK blocks at Stages 2, 3, and 4 each carry a named
reference to ROLE C as the structural origin of the threat fields — making the comparator's
provenance auditable from the stage block without session replay.

**Hypothesis**: R11 V-01 satisfies C-34 with named INCUMBENT CHECK blocks; the incumbent
is populated in an open CAMPAIGN OPEN preamble alongside other session metadata. Loss of
the INCUMBENT THREAT BLOCK is not auditable from the gate: GATE S in R11 V-01 checks two
fields (`gate_s_cleared`, `invariant_registry_confirmed`) — neither confirms the incumbent
threat was written. Moving the INCUMBENT THREAT BLOCK into ROLE C closes this gap: if the
incumbent was not analyzed, `incumbent_threat_locked` is absent from GATE S, Stage 1
cannot open. Each INCUMBENT CHECK block at Stages 2–4 now traces to a dedicated structural
role rather than an open preamble section, satisfying C-34 with a stronger audit chain
than R11 V-01.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
The campaign builds the case for displacing {status_quo_comparator} with {topic}.
Campaign opens with three blocking roles. Five evidence stages follow in fixed sequence.

---

## CAMPAIGN OPEN

Fill before any role begins.

  status_quo_comparator: [name the incumbent approach this topic must displace]

SESSION INVARIANTS — locked before Stage 0:

  SESSION INVARIANT A — Adversarial Reviewer:
    adversarial_reviewer_type: [role most likely to challenge {topic}'s claim]
    Activation: fires if ALL three evidence stages (S2, S3, S4) return null CE.
    Invariant language: pre-registered — cannot be modified or bypassed at synthesis.

  SESSION INVARIANT B — Confidence Cap:
    ce_score_formula: CE-score = -2 if all three stages null; 0 otherwise.
    Invariant language: locked formula — cannot be softened or overridden at synthesis.

  SESSION INVARIANT C — Derivation Annotation:
    annotation_rule: Every handoff field must carry [derived from: X]. Unlabeled field = format error.
    Invariant language: pre-registered — cannot be modified or bypassed at synthesis.

PRE-COMMITTED HANDOFF SCHEMA — session-level invariant, locked now:

Synthesis must produce exactly these 9 fields with exactly these derivation sources.
No additions. No omissions. Derivation-source mismatch = format error.

  FIELD                       | REQUIRED DERIVATION SOURCE
  ----------------------------|-----------------------------------------------------------
  scout_anchor                | ROLE B scout load
  hypothesis                  | Stage 1 artifact write
  analysis                    | Stage 4 artifact write
  null_tally_final            | Stage 4 CAMPAIGN OUTCOME BLOCK —
                              |   derived from {s2_ce_verdict, s3_ce_verdict, s4_ce_verdict}
  incumbent_defense_closed    | null_tally_final (NOT dual_lock_fired;
                              |   NOT co_activation_confirmed)
  co_activation_confirmed     | dual_lock_fired in synthesis (NOT incumbent_defense_closed;
                              |   NOT null_tally_final directly)
  confidence                  | evidence_score + ce_score per SESSION INVARIANT B
  next                        | static: "topic-story"
  schema_compliance_confirmed | synthesis-time compliance check against this schema

CE VERDICT OWNERSHIP TABLE — locked now:

  VERDICT FIELD  | SOLE PRODUCER | PERMISSIBLE VALUES | CONSUMER
  ---------------|---------------|--------------------|----------------------------
  s2_ce_verdict  | Stage 2       | found / null       | Stage 4 CAMPAIGN OUTCOME BLOCK
  s3_ce_verdict  | Stage 3       | found / null       | Stage 4 CAMPAIGN OUTCOME BLOCK
  s4_ce_verdict  | Stage 4       | found / null       | Stage 4 CAMPAIGN OUTCOME BLOCK

null_tally_final derivation formula:
  count of {s2_ce_verdict, s3_ce_verdict, s4_ce_verdict} where value = null

COUNTER-HYPOTHESIS CLOSURE RULE — locked now:
  counter_hypothesis at Stage 1 creates a Stage 5 resolution obligation.
  Stage 5 must produce REFUTED / PARTIALLY REFUTED / OPEN RISK plus evidence citation.
  OPEN RISK reduces confidence one tier from evidence_score baseline.

NULL TALLY CHAIN RULE — locked now:
  Stage 5 ATOMIC DUAL-LOCK must contain a NULL TALLY CHAIN block reconstructing:
    S2: [found/null] → running tally [N]
    S3: [found/null] → running tally [N]
    S4: [found/null] → tally [N] = null_tally_final
  Terminal tally must equal null_tally_final from Stage 4. Mismatch = format error.

All invariants, ownership table, closure rule, and tally chain rule are now locked.

---

## ROLE A — INVARIANT REGISTRY LOCK

OWNED ATTESTATION FIELD: invariant_registry_confirmed
Sole producer of this field. No other role or stage may produce it.

Execute first. Confirm all SESSION INVARIANTs (A, B, C), PRE-COMMITTED HANDOFF SCHEMA,
CE VERDICT OWNERSHIP TABLE, COUNTER-HYPOTHESIS CLOSURE RULE, and NULL TALLY CHAIN RULE
are active as session invariants.

  invariant_registry_confirmed: true    [ROLE A — produced here only]

ROLE A COMPLETE. Do not begin ROLE B without invariant_registry_confirmed = true.

---

## ROLE B — SCOUT LOAD

OWNED ATTESTATION FIELD: gate_s_cleared
Sole producer of this field. No other role or stage may produce it.

Execute after ROLE A. Locate: {topic}-scout-record-{date}.md
If not found: STOP. Record: "GATE S FAIL — scout record missing. Campaign cannot proceed."
If found: load record. Extract:
  - market signal
  - competitor landscape (identify {status_quo_comparator}; note all coverage)
  - feasibility finding

  gate_s_cleared: true    [ROLE B — produced here only]

ROLE B COMPLETE. Do not begin ROLE C without gate_s_cleared = true.

---

## ROLE C — INCUMBENT THREAT ANALYST

OWNED ATTESTATION FIELD: incumbent_threat_locked
Sole producer of this field. No other role or stage may produce it.

Execute after ROLE B. Using the competitor landscape loaded by ROLE B, populate:

  incumbent_name:          [name the incumbent — must match status_quo_comparator from CAMPAIGN OPEN]
  incumbent_strength:      [one sentence — why the incumbent is currently winning,
                            grounded in the scout competitor landscape]
  incumbent_vulnerability: [one sentence — where the incumbent is weakest,
                            grounded in the scout competitor landscape]

These three fields are ROLE C's sole production. All INCUMBENT CHECK blocks at Stages 2,
3, and 4 reference these fields by name. No stage may redefine or modify them.

  incumbent_threat_locked: true    [ROLE C — produced here only]

ROLE C COMPLETE. Do not open GATE S until all three roles are complete.

---

## GATE S

Requires ROLE A, ROLE B, and ROLE C all complete.

  invariant_registry_confirmed: true    (ROLE A — sole source; all invariants + rules)
  gate_s_cleared: true                  (ROLE B — sole source; scout record on file)
  incumbent_threat_locked: true         (ROLE C — sole source; INCUMBENT THREAT BLOCK written)

If any field is false or missing: STOP. Do not open Stage 1.
If all three fields are true: advance to Stage 1.

---

## Stage 1 — Hypothesis

Write: {topic}-hypothesis-{date}.md

Frontmatter:
  topic: {topic}
  date: {date}
  scout_anchor: {topic}-scout-record-{date}.md        [loaded in ROLE B]
  gate_s_cleared: true                                [ROLE B — sole source]
  invariant_registry_confirmed: true                  [ROLE A — sole source]
  incumbent_threat_locked: true                       [ROLE C — sole source]
  incumbent: [from ROLE C — incumbent_name]
  incumbent_strength: [from ROLE C — incumbent_strength]
  incumbent_vulnerability: [from ROLE C — incumbent_vulnerability]
  adversarial_reviewer_type: [from SESSION INVARIANT A]
  ce_score_formula: CE-score = -2 if all null [SESSION INVARIANT B]
  handoff_schema_locked: true
  counter_hypothesis_closure_rule: active
  null_tally_chain_rule: active

Body:
  Hypothesis statement: [one sentence — what {topic} does better than ROLE C's incumbent]
  Basis: [3-5 signals from the scout record; at least one speaks directly to
          ROLE C's incumbent_vulnerability]
  counter_hypothesis: [the incumbent's strongest defense — one sentence; creates Stage 5
                       COUNTER-HYPOTHESIS RESOLUTION obligation]

Artifact written: {topic}-hypothesis-{date}.md.
Confirm: "Stage 1 complete. Incumbent: {incumbent_name} (ROLE C). Counter-hypothesis declared.
          CE verdicts assigned to Stages 2/3/4. Advancing to Stage 2."

---

## Stage 2 — Web Search

Write: {topic}-websearch-{date}.md

Search for external evidence on {topic}. For each finding, record:
  claim, source URL, CE-relevant (yes/no), quote.

### INCUMBENT CHECK [origin: ROLE C — incumbent_threat_locked]

Using ROLE C's INCUMBENT THREAT BLOCK (incumbent_name, incumbent_strength, incumbent_vulnerability):
  Does this evidence help displace {incumbent_name}?
  - Flag findings that directly address ROLE C's incumbent_strength or incumbent_vulnerability.
  - Note any finding that strengthens the incumbent's position — this is counter-evidence (CE).
  Incumbent displacement signal: [yes / no / partial]

NULL TALLY NOTE:
  s2_ce_verdict: [found / null]    [OWNED FIELD — Stage 2 sole producer; CE VERDICT OWNERSHIP TABLE]
  Running null tally: [count] null. 2 evidence stages remain.
  If null: SESSION INVARIANTs A and B are active pre-committed obligations — not new decisions.

SCHEMA INTEGRITY NOTE:
  Schema fields locked: 9/9 — 0 additions, 0 omissions, 0 source mismatches since CAMPAIGN OPEN.

Artifact written: {topic}-websearch-{date}.md.
Confirm: "Stage 2 complete. s2_ce_verdict: [found/null]. Incumbent displacement signal: [signal].
          Schema: 9/9. Advancing to Stage 3."

---

## Stage 3 — Internal Intelligence

Write: {topic}-intelligence-{date}.md

Scan internal sources. For each finding, record:
  artifact path, claim, CE-relevant (yes/no).

### INCUMBENT CHECK [origin: ROLE C — incumbent_threat_locked]

Using ROLE C's INCUMBENT THREAT BLOCK (incumbent_name, incumbent_strength, incumbent_vulnerability):
  Does this evidence help displace {incumbent_name}?
  - Flag any internal artifact referencing {incumbent_name} or directly comparable approaches.
  - Note any finding that strengthens the incumbent's position — this is counter-evidence (CE).
  Incumbent displacement signal: [yes / no / partial]

NULL TALLY NOTE:
  s3_ce_verdict: [found / null]    [OWNED FIELD — Stage 3 sole producer; CE VERDICT OWNERSHIP TABLE]
  Running null tally: [count] null. 1 evidence stage remains.
  If null: SESSION INVARIANTs A and B are active pre-committed obligations — not new decisions.

SCHEMA INTEGRITY NOTE:
  Schema fields locked: 9/9 — 0 additions, 0 omissions, 0 source mismatches since Stage 2 check.

Artifact written: {topic}-intelligence-{date}.md.
Confirm: "Stage 3 complete. s3_ce_verdict: [found/null]. Incumbent displacement signal: [signal].
          Schema: 9/9. Advancing to Stage 4."

---

## Stage 4 — Analysis

Write: {topic}-analysis-{date}.md

Analyze all evidence from Stages 2 and 3.
  - Supporting evidence strength.
  - Counter-evidence summary: all CE found, sources, credibility.
  - If CE null: acknowledge explicitly; list all sources checked.

### INCUMBENT CHECK [origin: ROLE C — incumbent_threat_locked]

Using ROLE C's INCUMBENT THREAT BLOCK (incumbent_name, incumbent_strength, incumbent_vulnerability):
  Does the accumulated evidence from Stages 2, 3, and this analysis make a credible case
  for displacing {incumbent_name}?

  Displacement verdict: [ ] Yes  [ ] No  [ ] Pending

  Basis: [one sentence — cite specific findings and their relationship to ROLE C's
          incumbent_strength / incumbent_vulnerability]
  Residual: [if No or Pending — one sentence on what evidence would close the gap]

### CAMPAIGN OUTCOME BLOCK

CE VERDICT INPUT — consume owned fields:

  s2_ce_verdict: [found / null]    [produced by Stage 2 — sole source]
  s3_ce_verdict: [found / null]    [produced by Stage 3 — sole source]
  s4_ce_verdict: [found / null]    [produced by Stage 4 — sole source]

Derive:

  null_tally_final: count of {s2_ce_verdict, s3_ce_verdict, s4_ce_verdict} where value = null
    derivation: "count of named verdict fields = null per CE VERDICT OWNERSHIP TABLE formula.
                 NOT derived from dual_lock_fired or co_activation_confirmed."

  incumbent_defense_closed: [true if null_tally_final = 3; false otherwise]
    derivation: "null_tally_final >= 3 → true. NOT derived from dual_lock_fired
                 or co_activation_confirmed."

SCHEMA INTEGRITY NOTE:
  s4_ce_verdict is the final evidence-stage verdict. 9/9 declared fields intact.
  Schema contract confirmed clean through collection phase.

Artifact written: {topic}-analysis-{date}.md.
Confirm: "Stage 4 complete. CE verdicts: s2=[v], s3=[v], s4=[v].
          null_tally_final = [count] (from named verdict fields).
          incumbent_defense_closed = [true/false].
          Displacement verdict (ROLE C incumbent): [Yes/No/Pending].
          Advancing to Stage 5."

---

## Stage 5 — Synthesis

Write: {topic}-synthesize-{date}.md

Confirm SESSION INVARIANTs A, B, and C are in scope.
Retrieve PRE-COMMITTED HANDOFF SCHEMA, CE VERDICT OWNERSHIP TABLE,
COUNTER-HYPOTHESIS CLOSURE RULE, and NULL TALLY CHAIN RULE from CAMPAIGN OPEN.

### Findings

3-5 bullet points, each traceable to a specific artifact (path or stage reference).
For each finding, note whether it addresses ROLE C's incumbent_strength,
incumbent_vulnerability, or is neutral to the displacement question.

### COUNTER-HYPOTHESIS RESOLUTION

MANDATORY SECTION — unconditionally required.

  counter_hypothesis: [restate from {topic}-hypothesis-{date}.md]

Verdict (choose one):
  [ ] REFUTED — evidence from Stage(s) [X] directly defeats the incumbent's claim:
        [cite specific finding]
  [ ] PARTIALLY REFUTED — evidence weakens but does not eliminate the incumbent's claim:
        [cite finding; state what the incumbent can still credibly argue]
  [ ] OPEN RISK — no evidence gathered addressed the incumbent's claim:
        [state what evidence is needed; flag as live risk to adoption]

OPEN RISK: reduces confidence one tier from evidence_score baseline (SESSION INVARIANT execution).

### Counter-Evidence

MANDATORY SECTION — unconditionally required.
If CE found: list each item with source artifact and credibility rating.
If CE null: state: "No counter-evidence found. Sources checked: [Stage 2 sources],
  [Stage 3 sources]. This null result is the primary risk to the displacement case."

If CE null: apply SESSION INVARIANT A (adversarial reviewer) and SESSION INVARIANT B
  (confidence cap). These are pre-committed obligations — execution, not decisions.

### ATOMIC DUAL-LOCK (activates if null_tally_final = 3)

NULL TALLY CHAIN (NULL TALLY CHAIN RULE — execution, not declaration):

  S2: [found / null] → running tally [N]
  S3: [found / null] → running tally [N]
  S4: [found / null] → tally [N] = null_tally_final

Cross-check: terminal value must equal null_tally_final from Stage 4 CAMPAIGN OUTCOME BLOCK.
If mismatch: TALLY ERROR — record discrepancy before continuing.

  LOCK 1 — Adversarial Reviewer (SESSION INVARIANT A — execution):
    Reviewer: {adversarial_reviewer_type}
    Challenge frame: this reviewer represents {incumbent_name}'s perspective (ROLE C).
    Required before promotion.

  LOCK 2 — Confidence Cap (SESSION INVARIANT B — execution):
    CE-score = -2 (all-null formula). Maximum claim: MEDIUM. HIGH blocked.

  dual_lock_fired: [true if null_tally_final = 3, false otherwise]
  co_activation_confirmed: [must equal dual_lock_fired — format error if they differ]

### Confidence Level

  evidence_score: [0-5]
  ce_score: [0 or -2 per SESSION INVARIANT B]
  counter_hypothesis_verdict: [REFUTED / PARTIALLY REFUTED / OPEN RISK]
  displacement_rating: [STRONG / MODERATE / WEAK — from Stage 4 INCUMBENT CHECK]
  confidence: [LOW / MEDIUM / HIGH — HIGH blocked if ce_score = -2;
               OPEN RISK reduces one tier from evidence_score baseline]

### Handoff

SCHEMA COMPLIANCE CHECK — retrieve PRE-COMMITTED HANDOFF SCHEMA from CAMPAIGN OPEN.
Confirm all 9 declared fields with declared derivation sources.
Mismatch: "SCHEMA ERROR: {field} — expected: {expected}, actual: {actual}."

DERIVATION ANNOTATION RULE (SESSION INVARIANT C — execution): every field must carry
[derived from: X]. Unlabeled field = format error. Executing invariant, not declaring it.

  scout_anchor: {topic}-scout-record-{date}.md
    [derived from: ROLE B scout load]

  hypothesis: {topic}-hypothesis-{date}.md
    [derived from: Stage 1 artifact write — includes ROLE C incumbent framing
     and counter_hypothesis declaration]

  analysis: {topic}-analysis-{date}.md
    [derived from: Stage 4 artifact write]

  null_tally_final: [0-3]
    positive_derivation: "count of {s2_ce_verdict, s3_ce_verdict, s4_ce_verdict} = null
                          per CE VERDICT OWNERSHIP TABLE formula"
    independence_chain: "NOT derived from dual_lock_fired; NOT derived from
                         co_activation_confirmed"
    [derived from: Stage 4 CAMPAIGN OUTCOME BLOCK — CE verdict fields as declared inputs;
     tally chain cross-checked above in ATOMIC DUAL-LOCK]

  incumbent_defense_closed: [true if null_tally_final = 3, false otherwise]
    positive_derivation: "null_tally_final via formula null_tally_final >= 3"
    independence_chain: "NOT derived from dual_lock_fired; NOT derived from
                         co_activation_confirmed"
    [derived from: null_tally_final — independence confirmed per CAMPAIGN OPEN schema]

  co_activation_confirmed: [must equal dual_lock_fired]
    positive_derivation: "dual_lock_fired in ATOMIC DUAL-LOCK"
    independence_chain: "NOT derived from incumbent_defense_closed; NOT derived from
                         null_tally_final directly"
    [derived from: dual_lock_fired — independence confirmed per CAMPAIGN OPEN schema]

  confidence: [LOW/MEDIUM/HIGH]
    [derived from: evidence_score + ce_score per SESSION INVARIANT B
     + counter_hypothesis_verdict adjustment]

  next: topic-story
    [derived from: static handoff target]

  schema_compliance_confirmed: true
    [derived from: synthesis-time compliance check — 9 fields present with declared
     derivation sources; CE VERDICT OWNERSHIP TABLE formula confirmed as null_tally_final
     chain; COUNTER-HYPOTHESIS RESOLUTION completed; NULL TALLY CHAIN echoed and
     cross-checked; no additions; no omissions; SESSION INVARIANT C executed]

Confirm: "Synthesis complete. Displacement case against {incumbent_name} (ROLE C origin):
          [confidence] confidence. Counter-hypothesis verdict: [verdict].
          null_tally_final: [count] (CE chain: S2=[v] → S3=[v] → S4=[v]).
          Evidence brief ready for topic-story.
          Artifact written: {topic}-synthesize-{date}.md."
```

---

## V-02 — Axis: Output Format (Scorecard-Dominant)

**Variation axis**: Each evidence stage appends a row to a running CAMPAIGN SCORECARD
table. Every structural obligation that would appear as a prose note — incumbent
displacement signal, CE verdict, null tally count, schema field count — becomes a column
in the scorecard row. Stage 4's row adds a DISPLACEMENT VERDICT column (Yes/No/Pending)
satisfying C-34's Stage 4 requirement in tabular form. The confirmation line at each stage
is the completed scorecard row. Synthesis reads the finalized scorecard as its evidence
summary, with the handoff block remaining in prose form for field-level traceability.

**Hypothesis**: R11 V-01's INCUMBENT CHECK blocks satisfy C-34 as prose sub-sections
within each stage. Prose confirmation lines (one per stage) make per-stage audit require
reading the stage body. A running scorecard table exposes all per-stage signals in a
single accumulating artifact: at any point in the campaign, the scorecard shows the
current null tally, incumbent displacement signal per stage, schema field count, and
(at Stage 4) the displacement verdict — all in column-by-column form. Stage 4's
DISPLACEMENT VERDICT column makes the C-34 verdict requirement a named column header
visible from the table itself. This tests whether tabular accumulation produces a more
auditable C-34 structure than named prose blocks.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
Campaign opens with two blocking roles. Five evidence stages follow in fixed sequence.
All structured per-stage tracking renders as rows in a running CAMPAIGN SCORECARD table.

---

## CAMPAIGN OPEN

  status_quo_comparator: [name the incumbent approach this topic must displace]

### INCUMBENT THREAT BLOCK

  incumbent_name:          [from status_quo_comparator]
  incumbent_strength:      [one sentence — why the incumbent is currently winning]
  incumbent_vulnerability: [one sentence — where the incumbent is weakest]

### SESSION INVARIANTS

| INVARIANT | RULE                                                                              | STATUS |
|-----------|-----------------------------------------------------------------------------------|--------|
| A         | adversarial_reviewer_type: [role most likely to challenge the claim].             | LOCKED |
|           | Fires if ALL three evidence stages return null CE.                                |        |
|           | Pre-registered — cannot be modified or bypassed at synthesis.                    |        |
| B         | ce_score_formula: CE-score = -2 if all three stages null; 0 otherwise.            | LOCKED |
|           | Cannot be softened or overridden at synthesis.                                    |        |
| C         | annotation_rule: Every handoff field must carry [derived from: X].               | LOCKED |
|           | Unlabeled field = format error. Cannot be modified or bypassed at synthesis.     |        |

### PRE-COMMITTED HANDOFF SCHEMA

| # | FIELD                    | REQUIRED DERIVATION SOURCE                                                  |
|---|--------------------------|-----------------------------------------------------------------------------|
| 1 | scout_anchor             | ROLE B scout load                                                           |
| 2 | hypothesis               | Stage 1 artifact write                                                      |
| 3 | analysis                 | Stage 4 artifact write                                                      |
| 4 | null_tally_final         | Stage 4 CAMPAIGN OUTCOME BLOCK — derived from {s2, s3, s4}_ce_verdict      |
| 5 | incumbent_defense_closed | null_tally_final (NOT dual_lock_fired; NOT co_activation_confirmed)         |
| 6 | co_activation_confirmed  | dual_lock_fired (NOT incumbent_defense_closed; NOT null_tally_final)        |
| 7 | confidence               | evidence_score + ce_score per SESSION INVARIANT B                           |
| 8 | next                     | static: "topic-story"                                                       |
| 9 | schema_compliance_confirmed | synthesis-time compliance check against this schema                      |

No additions. No omissions. Source mismatch = format error.

### CE VERDICT OWNERSHIP TABLE

| VERDICT FIELD  | SOLE PRODUCER | PERMISSIBLE VALUES | CONSUMER                       |
|----------------|---------------|--------------------|--------------------------------|
| s2_ce_verdict  | Stage 2       | found / null       | Stage 4 CAMPAIGN OUTCOME BLOCK |
| s3_ce_verdict  | Stage 3       | found / null       | Stage 4 CAMPAIGN OUTCOME BLOCK |
| s4_ce_verdict  | Stage 4       | found / null       | Stage 4 CAMPAIGN OUTCOME BLOCK |

null_tally_final: count of {s2_ce_verdict, s3_ce_verdict, s4_ce_verdict} where value = null

COUNTER-HYPOTHESIS CLOSURE RULE — locked: counter_hypothesis at Stage 1 creates Stage 5
resolution obligation. Verdict: REFUTED / PARTIALLY REFUTED / OPEN RISK. OPEN RISK reduces
confidence one tier.

NULL TALLY CHAIN RULE — locked: Stage 5 ATOMIC DUAL-LOCK must contain NULL TALLY CHAIN
reconstructing S2→N, S3→N, S4→N = null_tally_final. Terminal tally must match Stage 4.
Mismatch = format error.

All invariants, ownership, closure rule, and tally chain rule are locked.

---

## CAMPAIGN SCORECARD — Running Table

Append one row per evidence stage. Read at synthesis.

| STAGE   | ARTIFACT                         | INCUMBENT DISPLACEMENT | CE VERDICT     | NULL TALLY | SCHEMA | DISPLACEMENT VERDICT |
|---------|----------------------------------|------------------------|----------------|------------|--------|----------------------|
| Stage 2 | {topic}-websearch-{date}.md      |                        |                |            |        | N/A                  |
| Stage 3 | {topic}-intelligence-{date}.md   |                        |                |            |        | N/A                  |
| Stage 4 | {topic}-analysis-{date}.md       |                        |                |            |        |                      |

Column definitions:
  INCUMBENT DISPLACEMENT — yes / no / partial (does this stage's evidence help displace {incumbent_name}?)
  CE VERDICT             — found / null (stage-owned field per CE VERDICT OWNERSHIP TABLE)
  NULL TALLY             — running count of null CE verdicts so far
  SCHEMA                 — field population count N/9 at this stage
  DISPLACEMENT VERDICT   — Stage 4 only: Yes / No / Pending
                           (does accumulated evidence make a credible case for displacing {incumbent_name}?)

---

## ROLE A — INVARIANT REGISTRY LOCK

OWNED ATTESTATION FIELD: invariant_registry_confirmed (sole producer)

Confirm all SESSION INVARIANTs (A, B, C), PRE-COMMITTED HANDOFF SCHEMA, CE VERDICT
OWNERSHIP TABLE, COUNTER-HYPOTHESIS CLOSURE RULE, and NULL TALLY CHAIN RULE are active.

| FIELD                        | VALUE | PRODUCER |
|------------------------------|-------|----------|
| invariant_registry_confirmed | true  | ROLE A   |

ROLE A COMPLETE. Do not begin ROLE B without invariant_registry_confirmed = true.

---

## ROLE B — SCOUT LOAD

OWNED ATTESTATION FIELD: gate_s_cleared (sole producer)

Execute after ROLE A. Locate: {topic}-scout-record-{date}.md
If not found: STOP — "GATE S FAIL — scout record missing. Campaign cannot proceed."
If found: load record. Extract: market signal, competitor landscape (note {incumbent_name}
coverage), feasibility finding.

| FIELD          | VALUE | PRODUCER |
|----------------|-------|----------|
| gate_s_cleared | true  | ROLE B   |

ROLE B COMPLETE. Both attestation fields on record — open GATE S.

---

## GATE S

| FIELD                        | VALUE | SOLE SOURCE | COVERS                        |
|------------------------------|-------|-------------|-------------------------------|
| invariant_registry_confirmed | true  | ROLE A      | all invariants + rules locked |
| gate_s_cleared               | true  | ROLE B      | scout record confirmed        |

If either field false or missing: STOP. If both true: advance to Stage 1.

---

## Stage 1 — Hypothesis

Write: {topic}-hypothesis-{date}.md

| FRONTMATTER FIELD              | VALUE / SOURCE                                              |
|--------------------------------|-------------------------------------------------------------|
| topic                          | {topic}                                                     |
| date                           | {date}                                                      |
| scout_anchor                   | {topic}-scout-record-{date}.md [ROLE B]                     |
| gate_s_cleared                 | true [ROLE B sole source]                                   |
| invariant_registry_confirmed   | true [ROLE A sole source; all invariants + rules]           |
| incumbent                      | [from INCUMBENT THREAT BLOCK — incumbent_name]              |
| adversarial_reviewer_type      | [from SESSION INVARIANT A]                                  |
| ce_score_formula               | CE-score = -2 if all null [SESSION INVARIANT B]             |
| handoff_schema_locked          | true [9 fields; null_tally_final from CE verdict fields]    |
| counter_hypothesis_closure_rule| active [Stage 5 COUNTER-HYPOTHESIS RESOLUTION obligated]    |
| null_tally_chain_rule          | active [Stage 5 NULL TALLY CHAIN obligated]                 |

Body:
  Hypothesis statement: [one sentence — what {topic} does better than {incumbent_name}]
  Basis: [3-5 signals from the scout record; at least one speaks to incumbent_vulnerability]
  counter_hypothesis: [incumbent's strongest defense — one sentence; Stage 5 obligation]

Artifact written: {topic}-hypothesis-{date}.md.
Confirm: "Stage 1 complete. counter_hypothesis declared. CE verdicts assigned to Stages 2/3/4.
          Advancing to Stage 2."

---

## Stage 2 — Web Search

Write: {topic}-websearch-{date}.md

Search for external evidence on {topic}. For each finding, record:
  claim, source URL, CE-relevant (yes/no), quote.

INCUMBENT CHECK: for each finding, ask whether it helps displace {incumbent_name}. Note
findings that address incumbent_strength or incumbent_vulnerability. Identify any finding
that strengthens the incumbent's position — this is CE.

Append CAMPAIGN SCORECARD row:

| STAGE   | ARTIFACT                    | INCUMBENT DISPLACEMENT | CE VERDICT   | NULL TALLY | SCHEMA |
|---------|-----------------------------|------------------------|--------------|------------|--------|
| Stage 2 | {topic}-websearch-{date}.md | [yes/no/partial]       | [found/null] | [count]    | [N/9]  |

  s2_ce_verdict: [found / null]    [OWNED FIELD — Stage 2 sole producer; CE VERDICT OWNERSHIP TABLE]
  If null: SESSION INVARIANTs A and B are active pre-committed obligations.

Artifact written: {topic}-websearch-{date}.md.
Confirm: "Stage 2 row appended to CAMPAIGN SCORECARD. Advancing to Stage 3."

---

## Stage 3 — Internal Intelligence

Write: {topic}-intelligence-{date}.md

Scan internal sources. For each finding, record: artifact path, claim, CE-relevant (yes/no).

INCUMBENT CHECK: for each finding, ask whether it helps displace {incumbent_name}. Flag
any internal artifact referencing {incumbent_name} or directly comparable approaches.

Append CAMPAIGN SCORECARD row:

| STAGE   | ARTIFACT                         | INCUMBENT DISPLACEMENT | CE VERDICT   | NULL TALLY | SCHEMA |
|---------|----------------------------------|------------------------|--------------|------------|--------|
| Stage 3 | {topic}-intelligence-{date}.md   | [yes/no/partial]       | [found/null] | [count]    | [N/9]  |

  s3_ce_verdict: [found / null]    [OWNED FIELD — Stage 3 sole producer; CE VERDICT OWNERSHIP TABLE]
  If null: SESSION INVARIANTs A and B are active pre-committed obligations.

Artifact written: {topic}-intelligence-{date}.md.
Confirm: "Stage 3 row appended to CAMPAIGN SCORECARD. Advancing to Stage 4."

---

## Stage 4 — Analysis

Write: {topic}-analysis-{date}.md

Analyze all evidence from Stages 2 and 3. Assess supporting evidence strength, counter-evidence
summary (all CE found, sources, credibility), and — if CE null — acknowledge explicitly with
source list.

INCUMBENT CHECK: does the accumulated evidence from Stages 2, 3, and this analysis make a
credible case for displacing {incumbent_name}? Record in the DISPLACEMENT VERDICT column.

Append CAMPAIGN SCORECARD row:

| STAGE   | ARTIFACT                    | INCUMBENT DISPLACEMENT | CE VERDICT   | NULL TALLY | SCHEMA | DISPLACEMENT VERDICT |
|---------|-----------------------------|------------------------|--------------|------------|--------|----------------------|
| Stage 4 | {topic}-analysis-{date}.md  | [yes/no/partial]       | [found/null] | [count]    | [N/9]  | [Yes/No/Pending]     |

Basis for displacement verdict: [one sentence — cite specific findings]

### CAMPAIGN OUTCOME BLOCK

  s2_ce_verdict: [found / null]    [Stage 2 sole source]
  s3_ce_verdict: [found / null]    [Stage 3 sole source]
  s4_ce_verdict: [found / null]    [Stage 4 sole source]

  null_tally_final: count of {s2_ce_verdict, s3_ce_verdict, s4_ce_verdict} where value = null
    derivation: "named verdict fields per CE VERDICT OWNERSHIP TABLE — NOT from
                 dual_lock_fired or co_activation_confirmed"

  incumbent_defense_closed: [true if null_tally_final = 3; false otherwise]
    derivation: "null_tally_final >= 3 → true — NOT from dual_lock_fired or co_activation_confirmed"

Artifact written: {topic}-analysis-{date}.md.
Confirm: "Stage 4 row appended. CAMPAIGN SCORECARD finalized:
          S2 [displacement/CE], S3 [displacement/CE], S4 [displacement/CE/verdict].
          null_tally_final = [count]. incumbent_defense_closed = [true/false].
          Advancing to Stage 5."

---

## Stage 5 — Synthesis

Write: {topic}-synthesize-{date}.md

Confirm SESSION INVARIANTs A, B, C in scope.
Read finalized CAMPAIGN SCORECARD. Retrieve PRE-COMMITTED HANDOFF SCHEMA, CE VERDICT
OWNERSHIP TABLE, COUNTER-HYPOTHESIS CLOSURE RULE, and NULL TALLY CHAIN RULE.

### Findings

Read CAMPAIGN SCORECARD. Write 3-5 bullet points, each traceable to a scorecard row or
artifact path. For each, note relationship to incumbent_strength, incumbent_vulnerability,
or neutral.

### COUNTER-HYPOTHESIS RESOLUTION

MANDATORY SECTION — unconditionally required.

  counter_hypothesis: [restate from {topic}-hypothesis-{date}.md]

| VERDICT           | EVIDENCE                        | STATUS |
|-------------------|---------------------------------|--------|
| [ ] REFUTED       | Stage(s) [X]: [cite finding]   |        |
| [ ] PART. REFUTED | [cite; state residual claim]   |        |
| [ ] OPEN RISK     | [state needed evidence; flag]  |        |

OPEN RISK: reduces confidence one tier from evidence_score baseline (SESSION INVARIANT execution).

### Counter-Evidence

MANDATORY SECTION — unconditionally required.
If CE found: list each item with source artifact and credibility rating.
If CE null: "No counter-evidence found. Sources: [Stage 2 sources], [Stage 3 sources].
  Null result = primary risk to the displacement case."

If CE null: apply SESSION INVARIANT A (adversarial reviewer) and SESSION INVARIANT B
(confidence cap) — pre-committed obligations, not decisions.

### ATOMIC DUAL-LOCK (activates if null_tally_final = 3)

NULL TALLY CHAIN (NULL TALLY CHAIN RULE — execution):
Read CAMPAIGN SCORECARD CE VERDICT column. Reconstruct:

  S2: [found / null] → running tally [N]
  S3: [found / null] → running tally [N]
  S4: [found / null] → tally [N] = null_tally_final

Cross-check: terminal value must equal null_tally_final from Stage 4 CAMPAIGN OUTCOME BLOCK.
Mismatch: TALLY ERROR — record before continuing.

  LOCK 1 — Adversarial Reviewer (SESSION INVARIANT A — execution):
    Reviewer: {adversarial_reviewer_type}
    Required before promotion.

  LOCK 2 — Confidence Cap (SESSION INVARIANT B — execution):
    CE-score = -2. Maximum claim: MEDIUM. HIGH blocked.

  dual_lock_fired: [true if null_tally_final = 3, false otherwise]
  co_activation_confirmed: [must equal dual_lock_fired — format error if they differ]

### Confidence Level

  evidence_score: [0-5]
  ce_score: [0 or -2 per SESSION INVARIANT B]
  counter_hypothesis_verdict: [REFUTED / PARTIALLY REFUTED / OPEN RISK]
  displacement_rating: [STRONG / MODERATE / WEAK — read from CAMPAIGN SCORECARD Stage 4 row]
  confidence: [LOW / MEDIUM / HIGH — HIGH blocked if ce_score = -2;
               OPEN RISK reduces one tier from evidence_score baseline]

### Handoff

SCHEMA COMPLIANCE CHECK: confirm all 9 declared fields against PRE-COMMITTED HANDOFF SCHEMA.
Mismatch: "SCHEMA ERROR: {field} — expected: {expected}, actual: {actual}."

DERIVATION ANNOTATION RULE (SESSION INVARIANT C — execution): all fields carry [derived from: X].

  scout_anchor: {topic}-scout-record-{date}.md
    [derived from: ROLE B scout load]

  hypothesis: {topic}-hypothesis-{date}.md
    [derived from: Stage 1 artifact write — includes counter_hypothesis declaration]

  analysis: {topic}-analysis-{date}.md
    [derived from: Stage 4 artifact write]

  null_tally_final: [0-3]
    positive_derivation: "count of {s2_ce_verdict, s3_ce_verdict, s4_ce_verdict} = null
                          per CE VERDICT OWNERSHIP TABLE formula; read from CAMPAIGN SCORECARD"
    independence_chain: "NOT derived from dual_lock_fired; NOT derived from co_activation_confirmed"
    [derived from: Stage 4 CAMPAIGN OUTCOME BLOCK — CE verdict fields; chain echoed in
     ATOMIC DUAL-LOCK above]

  incumbent_defense_closed: [true if null_tally_final = 3, false otherwise]
    positive_derivation: "null_tally_final >= 3 → true"
    independence_chain: "NOT derived from dual_lock_fired; NOT derived from co_activation_confirmed"
    [derived from: null_tally_final — independence confirmed per CAMPAIGN OPEN schema]

  co_activation_confirmed: [must equal dual_lock_fired]
    positive_derivation: "dual_lock_fired in ATOMIC DUAL-LOCK"
    independence_chain: "NOT derived from incumbent_defense_closed; NOT derived from
                         null_tally_final directly"
    [derived from: dual_lock_fired — independence confirmed per CAMPAIGN OPEN schema]

  confidence: [LOW/MEDIUM/HIGH]
    [derived from: evidence_score + ce_score per SESSION INVARIANT B
     + counter_hypothesis_verdict adjustment]

  next: topic-story
    [derived from: static handoff target]

  schema_compliance_confirmed: true
    [derived from: synthesis-time compliance check — 9 fields present; derivation sources
     match CAMPAIGN OPEN schema; CE verdict formula confirmed; NULL TALLY CHAIN echoed;
     COUNTER-HYPOTHESIS RESOLUTION complete; SESSION INVARIANT C executed]

Confirm: "Synthesis complete. CAMPAIGN SCORECARD read. [confidence] confidence.
          Counter-hypothesis: [verdict]. null_tally_final: [count]
          (S2=[v] → S3=[v] → S4=[v]).
          Evidence brief ready for topic-story.
          Artifact written: {topic}-synthesize-{date}.md."
```

---

## V-03 — Axis: Lifecycle Emphasis (Sparse Ceremony, Maximum Incumbent Weight)

**Variation axis**: Stage boundary prose is stripped to the minimum — no explicit
ENTER/WORK/CLOSE sub-labels, no schema integrity preamble paragraphs. Each evidence stage
has three elements: the write instruction (one line), the INCUMBENT CHECK block (the
dominant section — expanded with sub-questions), and a single-line footer combining CE
verdict, null tally, and schema count. The structural ceremony that would occupy several
prose paragraphs in earlier variations is compressed into footer tokens. Stage 4's
INCUMBENT CHECK is the largest block in the prompt, containing the displacement verdict
question, a structured evidence summary table, and a displacement confidence rating. The
effect: the prompt reads as evidence-gathering optimized for the displacement question —
each stage is a named checkpoint on the campaign's core question, with administrative
tally machinery in footers.

**Hypothesis**: In R11 V-01 and other prior variations, stage structure allocates roughly
equal space to hypothesis machinery (frontmatter, gate fields, tally notes, schema notes)
and to INCUMBENT CHECK. C-34's naming requirement can be satisfied with a terse block
while most stage space goes to structural bookkeeping. Inverting the weight — making
INCUMBENT CHECK the dominant section and compressing bookkeeping to footer tokens — tests
whether a practitioner-first layout (where every stage centers the displacement question)
still preserves all 34 structural criteria. The INCUMBENT CHECK blocks are larger and more
specific; the structural ceremony is compressed but not removed.

---

```
Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
Two blocking roles open. Five evidence stages follow. Each stage is centered on the
displacement question: does this evidence help unseat {status_quo_comparator}?

---

## CAMPAIGN OPEN

  status_quo_comparator: [name the incumbent approach this topic must displace]

### INCUMBENT THREAT BLOCK

  incumbent_name:          [from status_quo_comparator]
  incumbent_strength:      [one sentence — why the incumbent is currently winning]
  incumbent_vulnerability: [one sentence — where the incumbent is weakest]

SESSION INVARIANTS (A, B, C) — locked, invariant language:

  A: adversarial_reviewer_type: [role most likely to challenge the claim].
     Fires if all three evidence stages null. Pre-registered — cannot be bypassed at synthesis.
  B: ce_score_formula: CE-score = -2 if all three stages null; 0 otherwise.
     Locked formula — cannot be overridden at synthesis.
  C: annotation_rule: every handoff field carries [derived from: X]. Unlabeled = format error.
     Pre-registered — cannot be bypassed at synthesis.

PRE-COMMITTED HANDOFF SCHEMA — 9 fields, locked:

  scout_anchor → ROLE B scout load
  hypothesis → Stage 1 artifact
  analysis → Stage 4 artifact
  null_tally_final → Stage 4 CAMPAIGN OUTCOME BLOCK,
                     derived from {s2_ce_verdict, s3_ce_verdict, s4_ce_verdict}
  incumbent_defense_closed → null_tally_final (NOT dual_lock_fired; NOT co_activation_confirmed)
  co_activation_confirmed → dual_lock_fired (NOT incumbent_defense_closed; NOT null_tally_final)
  confidence → evidence_score + ce_score per SESSION INVARIANT B
  next → static: "topic-story"
  schema_compliance_confirmed → synthesis-time compliance check

No additions. No omissions. Source mismatch = format error.

CE VERDICT OWNERSHIP: s2_ce_verdict → Stage 2 (sole); s3_ce_verdict → Stage 3 (sole);
  s4_ce_verdict → Stage 4 (sole). Consumer: Stage 4 CAMPAIGN OUTCOME BLOCK.

null_tally_final: count of {s2, s3, s4}_ce_verdict where value = null.

COUNTER-HYPOTHESIS CLOSURE RULE — locked: counter_hypothesis at Stage 1 → Stage 5
resolution (REFUTED / PARTIALLY REFUTED / OPEN RISK). OPEN RISK reduces confidence one tier.

NULL TALLY CHAIN RULE — locked: Stage 5 ATOMIC DUAL-LOCK contains NULL TALLY CHAIN
reconstructing S2→N, S3→N, S4→N = null_tally_final. Terminal tally must match Stage 4.

---

## ROLE A — INVARIANT REGISTRY LOCK

Confirm all invariants, schema, ownership, closure rule, and tally chain rule are active.

  invariant_registry_confirmed: true    [ROLE A — sole producer]

---

## ROLE B — SCOUT LOAD

Locate: {topic}-scout-record-{date}.md
If not found: STOP — "GATE S FAIL — scout record missing."
If found: load. Extract: market signal, competitor landscape (note {incumbent_name}),
  feasibility finding.

  gate_s_cleared: true    [ROLE B — sole producer]

---

## GATE S

  invariant_registry_confirmed: true (ROLE A)    gate_s_cleared: true (ROLE B)
  Both true → open Stage 1.    Either missing → STOP.

---

## Stage 1 — Hypothesis

Write: {topic}-hypothesis-{date}.md

Frontmatter: topic | date | scout_anchor: {topic}-scout-record-{date}.md [ROLE B] |
  gate_s_cleared: true [ROLE B] | invariant_registry_confirmed: true [ROLE A] |
  incumbent: [incumbent_name] | adversarial_reviewer_type [SESSION INVARIANT A] |
  ce_score_formula: CE-score = -2 if all null [SESSION INVARIANT B] |
  handoff_schema_locked: true | counter_hypothesis_closure_rule: active |
  null_tally_chain_rule: active

Body:
  Hypothesis: [one sentence — what {topic} does better than {incumbent_name}]
  Basis: [3-5 scout signals; at least one speaks to incumbent_vulnerability]
  counter_hypothesis: [incumbent's strongest defense — one sentence; Stage 5 obligation]

Write artifact: {topic}-hypothesis-{date}.md. → Advance to Stage 2.

---

## Stage 2 — Web Search

Write: {topic}-websearch-{date}.md

Search for external evidence on {topic}. Record each finding: claim, source URL,
CE-relevant (yes/no), quote.

### INCUMBENT CHECK — Stage 2

The stage-level question: does this evidence help displace {incumbent_name}?

  1. For each finding: does it address incumbent_strength, incumbent_vulnerability,
     or neither? Label explicitly.
  2. Does any finding strengthen the incumbent's position?
     If yes: this is counter-evidence (CE). Record source and credibility.
  3. What is the net displacement signal from Stage 2's evidence?
     Displacement signal: [yes / no / partial]
  4. What does this stage's evidence NOT answer about the displacement case?
     Gap: [one sentence — what Stage 3 or 4 must address]

Footer: s2_ce_verdict=[found/null] [Stage 2 sole producer] | null_tally=[count] | schema=9/9
  If null: SESSION INVARIANTs A+B active — pre-committed obligations.

Write artifact: {topic}-websearch-{date}.md. → Advance to Stage 3.

---

## Stage 3 — Internal Intelligence

Write: {topic}-intelligence-{date}.md

Scan internal sources. Record each finding: artifact path, claim, CE-relevant (yes/no).

### INCUMBENT CHECK — Stage 3

The stage-level question: does this evidence help displace {incumbent_name}?

  1. For each finding: does it address incumbent_strength, incumbent_vulnerability,
     or neither? Label explicitly.
  2. Does any internal artifact reference {incumbent_name} or a directly comparable approach?
     If yes: flag as CE-relevant. Record artifact path and claim.
  3. Does any finding strengthen the incumbent's position?
     If yes: counter-evidence. Record source and credibility.
  4. What is the net displacement signal from Stage 3's evidence?
     Displacement signal: [yes / no / partial]

Footer: s3_ce_verdict=[found/null] [Stage 3 sole producer] | null_tally=[count] | schema=9/9
  If null: SESSION INVARIANTs A+B active — pre-committed obligations.

Write artifact: {topic}-intelligence-{date}.md. → Advance to Stage 4.

---

## Stage 4 — Analysis

Write: {topic}-analysis-{date}.md

Analyze all evidence from Stages 2 and 3. Summarize supporting evidence strength and
counter-evidence found. If CE null: acknowledge explicitly with source list.

### INCUMBENT CHECK — Stage 4

The stage-level question: does the accumulated evidence make a credible case for displacing
{incumbent_name}?

  1. Evidence addressing incumbent_strength (weakening it):

     | FINDING                     | STAGE | ARTIFACT PATH | STRENGTH |
     |-----------------------------|-------|---------------|----------|
     | [claim addressing strength] | [N]   | [path]        | [H/M/L]  |

  2. Evidence addressing incumbent_vulnerability (exploiting it):

     | FINDING                         | STAGE | ARTIFACT PATH | STRENGTH |
     |---------------------------------|-------|---------------|----------|
     | [claim addressing vulnerability]| [N]   | [path]        | [H/M/L]  |

  3. Evidence neutral to displacement:
     [brief note or "none"]

  4. Displacement verdict:
     [ ] Yes    — evidence is sufficient to make the displacement case
     [ ] No     — evidence does not yet support displacement
     [ ] Pending — evidence is suggestive but requires Stage 5 synthesis to resolve
     Basis: [one sentence]

### CAMPAIGN OUTCOME BLOCK

  s2_ce_verdict: [found / null]    [Stage 2 sole source]
  s3_ce_verdict: [found / null]    [Stage 3 sole source]
  s4_ce_verdict: [found / null]    [Stage 4 sole source]

  null_tally_final: count of {s2, s3, s4}_ce_verdict = null
    derivation: named verdict fields per CE VERDICT OWNERSHIP TABLE — NOT via dual_lock_fired
    or co_activation_confirmed.

  incumbent_defense_closed: [true if null_tally_final = 3; false otherwise]
    derivation: null_tally_final >= 3 → true. NOT via dual_lock_fired or co_activation_confirmed.

Footer: s4_ce_verdict=[found/null] [Stage 4 sole producer] | null_tally_final=[count] | schema=9/9

Write artifact: {topic}-analysis-{date}.md. → Advance to Stage 5.

---

## Stage 5 — Synthesis

Write: {topic}-synthesize-{date}.md

Confirm SESSION INVARIANTs A, B, C in scope.
Retrieve: PRE-COMMITTED HANDOFF SCHEMA, CE VERDICT OWNERSHIP TABLE, COUNTER-HYPOTHESIS
CLOSURE RULE, NULL TALLY CHAIN RULE.

### Displacement Case

3-5 bullet points. Each traces to a specific artifact. Each notes relationship to
incumbent_strength, incumbent_vulnerability, or neutral.

### COUNTER-HYPOTHESIS RESOLUTION

MANDATORY SECTION — unconditionally required.

  counter_hypothesis: [restate from {topic}-hypothesis-{date}.md]

  Verdict:
    [ ] REFUTED — Stage(s) [X] directly defeats the claim: [cite]
    [ ] PARTIALLY REFUTED — weakened but not eliminated: [cite; state residual]
    [ ] OPEN RISK — no evidence addressed the claim: [state needed evidence; live risk]

  OPEN RISK: reduces confidence one tier (SESSION INVARIANT execution).

### Counter-Evidence

MANDATORY SECTION — unconditionally required.
If CE found: list with source and credibility.
If CE null: "No counter-evidence found. Sources: [S2 sources], [S3 sources]. Null = primary risk."
  Apply SESSION INVARIANT A (adversarial reviewer) and SESSION INVARIANT B (cap) —
  pre-committed obligations.

### ATOMIC DUAL-LOCK (activates if null_tally_final = 3)

NULL TALLY CHAIN (execution):
  S2: [found/null] → tally [N]
  S3: [found/null] → tally [N]
  S4: [found/null] → tally [N] = null_tally_final

Cross-check: terminal = null_tally_final from Stage 4. Mismatch: TALLY ERROR.

  LOCK 1 (SESSION INVARIANT A — execution): Reviewer: {adversarial_reviewer_type}.
    Required before promotion.
  LOCK 2 (SESSION INVARIANT B — execution): CE-score = -2. MEDIUM max. HIGH blocked.
  dual_lock_fired: [true if null_tally_final = 3]
  co_activation_confirmed: [must equal dual_lock_fired]

### Confidence

  evidence_score: [0-5] | ce_score: [0/-2] | counter_hypothesis_verdict: [R/PR/OR]
  displacement_rating: [STRONG/MODERATE/WEAK] | confidence: [LOW/MEDIUM/HIGH]

### Handoff

SCHEMA COMPLIANCE: confirm 9 fields against PRE-COMMITTED HANDOFF SCHEMA. Log any mismatch.
DERIVATION ANNOTATION RULE (SESSION INVARIANT C — execution):

  scout_anchor: {topic}-scout-record-{date}.md
    [derived from: ROLE B scout load]
  hypothesis: {topic}-hypothesis-{date}.md
    [derived from: Stage 1 artifact write]
  analysis: {topic}-analysis-{date}.md
    [derived from: Stage 4 artifact write]
  null_tally_final: [0-3]
    positive_derivation: count of {s2, s3, s4}_ce_verdict = null per OWNERSHIP TABLE formula
    independence_chain: NOT via dual_lock_fired; NOT via co_activation_confirmed
    [derived from: Stage 4 CAMPAIGN OUTCOME BLOCK; chain echoed in ATOMIC DUAL-LOCK]
  incumbent_defense_closed: [true/false]
    positive_derivation: null_tally_final >= 3 → true
    independence_chain: NOT via dual_lock_fired; NOT via co_activation_confirmed
    [derived from: null_tally_final per CAMPAIGN OPEN schema]
  co_activation_confirmed: [must equal dual_lock_fired]
    positive_derivation: dual_lock_fired in ATOMIC DUAL-LOCK
    independence_chain: NOT via incumbent_defense_closed; NOT via null_tally_final directly
    [derived from: dual_lock_fired per CAMPAIGN OPEN schema]
  confidence: [LOW/MEDIUM/HIGH]
    [derived from: evidence_score + ce_score per SESSION INVARIANT B
     + counter_hypothesis_verdict]
  next: topic-story
    [derived from: static handoff target]
  schema_compliance_confirmed: true
    [derived from: synthesis-time check — 9 fields, sources match, CE formula confirmed,
     NULL TALLY CHAIN echoed, COUNTER-HYPOTHESIS RESOLUTION complete, INVARIANT C executed]

Confirm: "Evidence brief ready for topic-story. [confidence] confidence.
          Counter-hypothesis: [verdict]. CE chain: S2=[v] → S3=[v] → S4=[v].
          Artifact written: {topic}-synthesize-{date}.md."
```

---

## V-04 — Combined: Role Sequence + Phrasing Register

**Variation axis**: Three-role structure from V-01 (ROLE A: Invariant Registry, ROLE B:
Scout Load, ROLE C: Incumbent Threat Analyst) combined with direct second-person imperative
phrasing throughout. No "SESSION INVARIANT" formal labels — the rules are stated directly:
"This rule is locked. You cannot change it at synthesis." GATE S is a numbered checklist
rather than a field-verification block. The INCUMBENT CHECK blocks use imperative language:
"Ask now: does this help unseat {incumbent_name}?" Each ROLE is addressed as "you" with
explicit ownership language: "You own this field. No other role may produce it."

**Hypothesis**: R11 V-01 and V-04's formal "SESSION INVARIANT" registry language achieves
strong structural locking but may read as overly bureaucratic in a practitioner context.
Second-person imperatives ("You own this field.", "This rule cannot be changed.") may
achieve the same invariant-language requirement of C-19 and C-30 while feeling less like
a compliance framework and more like direct instructions. Adding ROLE C tests whether the
three-role structure remains auditable under conversational phrasing — the gate-field
ownership model persists but the language shifts from registry-attestation to direct
practitioner addressing. This tests whether two structural innovations (three roles from
V-01, imperative phrasing from R11 V-04) combine without conflicting.

---

```
Topic: {topic}
Date:  {date}

Run the full prove evidence campaign for this topic.
You will displace {status_quo_comparator} with {topic}.
Three blocking roles open the campaign. Run them in order. Five evidence stages follow.

---

## CAMPAIGN OPEN

Record these before any role begins:

  status_quo_comparator: [name the incumbent you are trying to displace]

Now lock the following rules. You cannot change them at synthesis. Not conditionally.
Not as a "synthesis decision." They are locked here.

  Rule A — Adversarial Reviewer:
    adversarial_reviewer_type: [the role most likely to argue for {status_quo_comparator}]
    This reviewer activates if all three evidence stages find no CE. Locked now. Cannot bypass.

  Rule B — Confidence Cap:
    ce_score_formula: CE-score = -2 if all three stages find no CE; 0 otherwise.
    This formula is locked. You cannot soften it. You cannot override it. Apply it at synthesis.

  Rule C — Derivation Annotation:
    Every handoff field you write must carry [derived from: X]. If you leave a field
    unlabeled, that is a format error. Locked now. Cannot bypass.

Lock the handoff schema now. These 9 fields with these sources. No additions. No omissions.
If a source doesn't match what you declared here, that is a format error.

  scout_anchor             → you loaded this in ROLE B
  hypothesis               → you wrote this at Stage 1
  analysis                 → you wrote this at Stage 4
  null_tally_final         → Stage 4 CAMPAIGN OUTCOME BLOCK, from {s2, s3, s4}_ce_verdict
  incumbent_defense_closed → null_tally_final (not from dual_lock_fired, not from co_activation_confirmed)
  co_activation_confirmed  → dual_lock_fired in synthesis (not from incumbent_defense_closed,
                             not directly from null_tally_final)
  confidence               → evidence_score + ce_score per Rule B
  next                     → "topic-story" — static
  schema_compliance_confirmed → you check this at synthesis

Lock CE verdict ownership now. Each stage owns exactly one verdict field. No sharing.

  s2_ce_verdict — you produce this at Stage 2 and nowhere else. Values: found / null.
  s3_ce_verdict — you produce this at Stage 3 and nowhere else. Values: found / null.
  s4_ce_verdict — you produce this at Stage 4 and nowhere else. Values: found / null.

  null_tally_final = count of those three fields where value = null. Nothing else.

Lock the counter-hypothesis closure rule now. You will declare a counter_hypothesis at
Stage 1. At Stage 5 you must resolve it: REFUTED, PARTIALLY REFUTED, or OPEN RISK. If
OPEN RISK, reduce your confidence one tier. This is locked. Cannot skip.

Lock the null tally chain rule now. In the ATOMIC DUAL-LOCK at Stage 5, you reconstruct
the per-stage null accumulation: S2→tally, S3→tally, S4→tally = null_tally_final. The
terminal tally must match what Stage 4 recorded. If it doesn't, that is a tally error.
This is locked. Cannot skip.

Everything above is locked. Move to ROLE A.

---

## ROLE A — INVARIANT REGISTRY LOCK

You are ROLE A. You own this field: invariant_registry_confirmed.
No other role or stage may produce it.

Your job: confirm that everything locked in CAMPAIGN OPEN is active. Go through each
rule, the schema, the ownership table, the closure rule, and the tally chain rule.
They are active. Record your confirmation.

  invariant_registry_confirmed: true    [you — ROLE A — sole producer]

You are done. Do not let ROLE B start until invariant_registry_confirmed = true.

---

## ROLE B — SCOUT LOAD

You are ROLE B. You own this field: gate_s_cleared.
No other role or stage may produce it.

Your job: find {topic}-scout-record-{date}.md.
If you cannot find it: stop. Write "GATE S FAIL — scout record missing." Do not proceed.
If you find it: load it. Pull out the market signal, the competitor landscape (locate
{status_quo_comparator} in it), and the feasibility finding.

  gate_s_cleared: true    [you — ROLE B — sole producer]

You are done. Do not let ROLE C start until gate_s_cleared = true.

---

## ROLE C — INCUMBENT THREAT ANALYST

You are ROLE C. You own this field: incumbent_threat_locked.
No other role or stage may produce it.

Your job: using the competitor landscape ROLE B just loaded, write the incumbent threat.
Do not invent. Ground every sentence in the scout record.

  incumbent_name:          [name the incumbent — confirm it matches status_quo_comparator]
  incumbent_strength:      [one sentence — what makes the incumbent hard to displace,
                            from the scout competitor landscape]
  incumbent_vulnerability: [one sentence — where the incumbent is weakest,
                            from the scout competitor landscape]

These three fields are yours. The INCUMBENT CHECK blocks at Stages 2, 3, and 4 will
reference them by name. No stage may change them.

  incumbent_threat_locked: true    [you — ROLE C — sole producer]

You are done. All three roles complete. Open GATE S.

---

## GATE S

Check off each item. All three must be true before you open Stage 1.

  [ ] 1. invariant_registry_confirmed = true   (ROLE A)
  [ ] 2. gate_s_cleared = true                 (ROLE B)
  [ ] 3. incumbent_threat_locked = true        (ROLE C)

All three checked? Advance to Stage 1.
Any item unchecked? Stop. Do not open Stage 1.

---

## Stage 1 — Hypothesis

Write: {topic}-hypothesis-{date}.md

Put in the frontmatter:
  topic: {topic} | date: {date}
  scout_anchor: {topic}-scout-record-{date}.md       [ROLE B loaded this]
  gate_s_cleared: true                               [ROLE B produced this]
  invariant_registry_confirmed: true                 [ROLE A produced this]
  incumbent_threat_locked: true                      [ROLE C produced this]
  incumbent: [from ROLE C — incumbent_name]
  adversarial_reviewer_type: [from Rule A]
  ce_score_formula: CE-score = -2 if all null        [from Rule B]
  handoff_schema_locked: true
  counter_hypothesis_closure_rule: active
  null_tally_chain_rule: active

Write the hypothesis body:
  Hypothesis: [one sentence — what {topic} does better than ROLE C's {incumbent_name}]
  Basis: [3-5 signals from the scout record; at least one speaks to incumbent_vulnerability]
  counter_hypothesis: [the incumbent's strongest defense; you resolve this at Stage 5]

Write artifact: {topic}-hypothesis-{date}.md.
Say: "Hypothesis written. Incumbent: {incumbent_name}. Counter-hypothesis declared.
      Moving to Stage 2."

---

## Stage 2 — Web Search

Write: {topic}-websearch-{date}.md

Search for external evidence on {topic}. For each finding: claim, source URL,
CE-relevant (yes/no), quote.

### INCUMBENT CHECK — Stage 2

Ask now: does this evidence help unseat {incumbent_name}?

  - Go through each finding. Does it attack ROLE C's incumbent_strength? Does it exploit
    ROLE C's incumbent_vulnerability? Label each finding explicitly.
  - Did any finding make the incumbent look stronger instead? That is CE. Record it.
  - Net signal: [yes / no / partial]

  s2_ce_verdict: [found / null]    [you own this field — Stage 2 sole producer]
  Running null tally: [count] null. 2 stages remain.
  If null: Rule A reviewer and Rule B cap are locked obligations. They will fire at Stage 5.
  Schema count: 9/9 fields locked since CAMPAIGN OPEN. 0 additions, 0 omissions.

Write artifact: {topic}-websearch-{date}.md.
Say: "Stage 2 done. s2_ce_verdict: [found/null]. Displacement signal: [signal].
      Moving to Stage 3."

---

## Stage 3 — Internal Intelligence

Write: {topic}-intelligence-{date}.md

Scan internal sources. For each finding: artifact path, claim, CE-relevant (yes/no).

### INCUMBENT CHECK — Stage 3

Ask now: does this evidence help unseat {incumbent_name}?

  - Go through each finding. Does it address ROLE C's incumbent_strength or vulnerability?
  - Did any internal artifact mention {incumbent_name} or directly compare approaches?
    If yes, flag as CE-relevant.
  - Did any finding strengthen the incumbent's position? That is CE. Record it.
  - Net signal: [yes / no / partial]

  s3_ce_verdict: [found / null]    [you own this field — Stage 3 sole producer]
  Running null tally: [count] null. 1 stage remains.
  If null: Rule A and Rule B are locked obligations — not decisions you make at synthesis.
  Schema count: 9/9 fields locked. 0 additions, 0 omissions.

Write artifact: {topic}-intelligence-{date}.md.
Say: "Stage 3 done. s3_ce_verdict: [found/null]. Displacement signal: [signal].
      Moving to Stage 4."

---

## Stage 4 — Analysis

Write: {topic}-analysis-{date}.md

Analyze all evidence from Stages 2 and 3. Assess supporting evidence strength. Summarize
all CE found (sources, credibility). If CE null: say so explicitly and list every source
you checked.

### INCUMBENT CHECK — Stage 4

Ask now: does the accumulated evidence — everything from Stages 2, 3, and this analysis —
make a credible case for displacing {incumbent_name}?

  Displacement verdict: [ ] Yes  [ ] No  [ ] Pending
  Basis: [one sentence — cite the specific findings; relate to ROLE C's strength/vulnerability]
  If No or Pending: what would close the gap?

Now produce the CAMPAIGN OUTCOME BLOCK. This is a derivation step, not a judgment call.

  s2_ce_verdict: [value from Stage 2 — sole source]
  s3_ce_verdict: [value from Stage 3 — sole source]
  s4_ce_verdict: [value you just produced — Stage 4 sole source]

  null_tally_final = count of those three where value = null.
    You derive this from the three named fields. Not from dual_lock_fired. Not from
    co_activation_confirmed. Use the ownership table formula.

  incumbent_defense_closed = true if null_tally_final = 3; false otherwise.
    You derive this from null_tally_final. Not from dual_lock_fired. Not from
    co_activation_confirmed.

Schema count: 9/9 fields intact — all derivation sources match CAMPAIGN OPEN.

Write artifact: {topic}-analysis-{date}.md.
Say: "Stage 4 done. CE verdicts: s2=[v], s3=[v], s4=[v]. null_tally_final=[count].
      incumbent_defense_closed=[true/false]. Displacement verdict: [Yes/No/Pending].
      Moving to Stage 5."

---

## Stage 5 — Synthesis

Write: {topic}-synthesize-{date}.md

Confirm Rules A, B, C are in scope. Retrieve the handoff schema, CE verdict ownership
table, counter-hypothesis closure rule, and null tally chain rule.

### Findings

3-5 bullets. Each traces to a specific artifact. For each, say whether it attacks
ROLE C's incumbent_strength, exploits incumbent_vulnerability, or is neutral.

### COUNTER-HYPOTHESIS RESOLUTION

You must do this. No exceptions.

  counter_hypothesis: [copy it from {topic}-hypothesis-{date}.md]

  Choose one verdict:
    [ ] REFUTED — evidence from Stage(s) [X] beats the incumbent's claim directly: [cite]
    [ ] PARTIALLY REFUTED — weakened but not gone: [cite; state what the incumbent can still argue]
    [ ] OPEN RISK — nothing you gathered addresses this claim: [state what's needed; live risk]

  OPEN RISK means you reduce your confidence one tier. Do it. Rule execution.

### Counter-Evidence

You must do this. No exceptions.
If you found CE: list each item with source artifact and credibility rating.
If CE is null: write "No counter-evidence found. Sources checked: [list]. This is the
  primary risk to the displacement case."

If CE is null: Rule A (adversarial reviewer) and Rule B (confidence cap) fire now.
  They were locked at CAMPAIGN OPEN. Execute them.

### ATOMIC DUAL-LOCK (fires if null_tally_final = 3)

Reconstruct the tally chain. This is required by the null tally chain rule.

  S2: [found / null] → tally [N]
  S3: [found / null] → tally [N]
  S4: [found / null] → tally [N] = null_tally_final

Check: does the terminal tally match what Stage 4 recorded?
If not: TALLY ERROR — write down the discrepancy before you continue.

  LOCK 1 — Rule A reviewer fires: {adversarial_reviewer_type}.
    This reviewer represents {incumbent_name}'s perspective. Required before promotion.

  LOCK 2 — Rule B cap fires: CE-score = -2. You cannot claim HIGH. Maximum is MEDIUM.

  dual_lock_fired: [true if null_tally_final = 3]
  co_activation_confirmed: [must equal dual_lock_fired — format error if they differ]

### Confidence

  evidence_score: [0-5] | ce_score: [0/-2] | counter_hypothesis_verdict: [R/PR/OR]
  displacement_rating: [STRONG/MODERATE/WEAK] | confidence: [LOW/MEDIUM/HIGH]

### Handoff

Schema compliance: check all 9 fields against the schema you locked at CAMPAIGN OPEN.
Rule C is active now: every field you write must carry [derived from: X]. No exceptions.

  scout_anchor: {topic}-scout-record-{date}.md
    [derived from: ROLE B scout load]

  hypothesis: {topic}-hypothesis-{date}.md
    [derived from: Stage 1 — you wrote this; includes counter_hypothesis and ROLE C framing]

  analysis: {topic}-analysis-{date}.md
    [derived from: Stage 4 — you wrote this]

  null_tally_final: [0-3]
    positive_derivation: count of {s2, s3, s4}_ce_verdict = null per CE VERDICT OWNERSHIP TABLE
    independence_chain: NOT via dual_lock_fired; NOT via co_activation_confirmed
    [derived from: Stage 4 CAMPAIGN OUTCOME BLOCK — named verdict fields; chain echoed above]

  incumbent_defense_closed: [true/false]
    positive_derivation: null_tally_final >= 3 → true
    independence_chain: NOT via dual_lock_fired; NOT via co_activation_confirmed
    [derived from: null_tally_final per CAMPAIGN OPEN schema]

  co_activation_confirmed: [must equal dual_lock_fired]
    positive_derivation: dual_lock_fired in ATOMIC DUAL-LOCK
    independence_chain: NOT via incumbent_defense_closed; NOT directly via null_tally_final
    [derived from: dual_lock_fired per CAMPAIGN OPEN schema]

  confidence: [LOW/MEDIUM/HIGH]
    [derived from: evidence_score + ce_score per Rule B + counter_hypothesis_verdict]

  next: topic-story
    [derived from: static handoff]

  schema_compliance_confirmed: true
    [derived from: you checked all 9 fields; sources match; CE formula confirmed;
     tally chain echoed; counter-hypothesis closed; Rule C executed]

Say: "Done. The case against {incumbent_name}: [confidence].
      Counter-hypothesis verdict: [verdict]. CE chain: S2=[v] → S3=[v] → S4=[v].
      Evidence brief ready for topic-story.
      Artifact written: {topic}-synthesize-{date}.md."
```

---

## V-05 — Combined: All Three + Inertia Framing Variant (Threat Score)

**Variation axis**: Three-role structure from V-01 + running CAMPAIGN SCORECARD from V-02
+ sparse lifecycle from V-03, combined with an inertia scoring variant: ROLE C produces a
numeric INCUMBENT THREAT SCORE (1–5) quantifying the difficulty of displacement, in
addition to `incumbent_threat_locked`. The threat score is a new field in the 10-field
handoff schema (pre-committed at CAMPAIGN OPEN). At Stage 5, the threat score gates the
displacement_rating: threat_score ≥ 4 caps displacement_rating at MODERATE regardless
of evidence_score, unless evidence_score = 5. The CAMPAIGN SCORECARD includes a
THREAT RELEVANCE column (how directly each stage's evidence addresses the threat score
dimension). The synthesis frames the confidence level as a product of two competing
pressures: the evidence score (what we found for {topic}) and the threat score (how hard
the incumbent is to unseat).

**Hypothesis**: Prior variations treat the incumbent as a binary presence — named, present,
displaced or not. In practice, incumbents vary in entrenchment difficulty. A strongly
entrenched incumbent (threat_score 5: broad adoption, switching cost, inertia) requires
stronger supporting evidence to justify HIGH confidence than a weakly entrenched incumbent
(threat_score 1: niche use, low switching cost). Threading a quantified threat score
through the handoff schema — pre-committed at CAMPAIGN OPEN, produced by ROLE C, capping
displacement_rating at Stage 5 — tests whether inertia framing can carry a mechanical
effect that modulates the confidence computation, not just a framing note. This combines
C-34's structural INCUMBENT CHECK presence with a score-based confidence gate that
extends C-17's mechanical cap to a second dimension.

---

```
Topic: {topic}
Date:  {date}

Run the full prove evidence campaign for this topic.
Build the case for displacing {status_quo_comparator} with {topic}.
Three blocking roles open. Five evidence stages follow. A running CAMPAIGN SCORECARD
tracks per-stage signals. The INCUMBENT THREAT SCORE quantifies displacement difficulty.

---

## CAMPAIGN OPEN

  status_quo_comparator: [name the incumbent]

### SESSION INVARIANTS (A, B, C) — pre-registered, invariant language, locked:

  A: adversarial_reviewer_type: [role most likely to challenge the claim].
     Fires if ALL three evidence stages null. Cannot be modified or bypassed at synthesis.
  B: ce_score_formula: CE-score = -2 if all three stages null; 0 otherwise.
     Cannot be softened or overridden at synthesis.
  C: annotation_rule: every handoff field carries [derived from: X]. Unlabeled = format error.
     Cannot be modified or bypassed at synthesis.

  THREAT SCORE CAP RULE — locked:
    If threat_score >= 4: displacement_rating capped at MODERATE unless evidence_score = 5.
    Locked now. Cannot be modified or overridden at synthesis.

### PRE-COMMITTED HANDOFF SCHEMA — 10 fields, locked. No additions. No omissions.

  FIELD                    | REQUIRED DERIVATION SOURCE
  -------------------------|-----------------------------------------------------------
  scout_anchor             | ROLE B scout load
  hypothesis               | Stage 1 artifact write
  analysis                 | Stage 4 artifact write
  null_tally_final         | Stage 4 CAMPAIGN OUTCOME BLOCK —
                           |   derived from {s2_ce_verdict, s3_ce_verdict, s4_ce_verdict}
  incumbent_defense_closed | null_tally_final (NOT dual_lock_fired; NOT co_activation_confirmed)
  co_activation_confirmed  | dual_lock_fired in synthesis (NOT incumbent_defense_closed;
                           |   NOT null_tally_final directly)
  threat_score             | ROLE C — INCUMBENT THREAT SCORE block
  confidence               | evidence_score + ce_score per SESSION INVARIANT B
                           |   + threat_score cap per THREAT SCORE CAP RULE
  next                     | static: "topic-story"
  schema_compliance_confirmed | synthesis-time compliance check against this 10-field schema

CE VERDICT OWNERSHIP TABLE — locked:

  s2_ce_verdict → Stage 2 (sole) | s3_ce_verdict → Stage 3 (sole) | s4_ce_verdict → Stage 4 (sole)
  Consumer: Stage 4 CAMPAIGN OUTCOME BLOCK.
  null_tally_final = count of {s2, s3, s4}_ce_verdict where value = null.

COUNTER-HYPOTHESIS CLOSURE RULE — locked: counter_hypothesis at Stage 1 → Stage 5 verdict
  (REFUTED / PARTIALLY REFUTED / OPEN RISK). OPEN RISK reduces confidence one tier.

NULL TALLY CHAIN RULE — locked: Stage 5 ATOMIC DUAL-LOCK contains NULL TALLY CHAIN
  (S2→N, S3→N, S4→N = null_tally_final). Terminal must match Stage 4. Mismatch = format error.

All invariants, ownership, rules, and schema are locked.

---

## CAMPAIGN SCORECARD — Running Table

Append one row per evidence stage. THREAT RELEVANCE column: how directly does this stage's
evidence address the THREAT SCORE dimension (ROLE C's incumbent_strength)?

| STAGE   | ARTIFACT                       | DISPLACE SIGNAL | CE VERDICT   | NULL TALLY | SCHEMA  | THREAT RELEVANCE | DISPLACE VERDICT |
|---------|--------------------------------|-----------------|--------------|------------|---------|------------------|------------------|
| Stage 2 | {topic}-websearch-{date}.md    |                 |              |            |         |                  | N/A              |
| Stage 3 | {topic}-intelligence-{date}.md |                 |              |            |         |                  | N/A              |
| Stage 4 | {topic}-analysis-{date}.md     |                 |              |            |         |                  |                  |

---

## ROLE A — INVARIANT REGISTRY LOCK

Confirm all SESSION INVARIANTs (A, B, C), THREAT SCORE CAP RULE, PRE-COMMITTED HANDOFF
SCHEMA (10 fields), CE VERDICT OWNERSHIP TABLE, COUNTER-HYPOTHESIS CLOSURE RULE, and
NULL TALLY CHAIN RULE are active.

  invariant_registry_confirmed: true    [ROLE A — sole producer]

---

## ROLE B — SCOUT LOAD

Locate: {topic}-scout-record-{date}.md
If not found: STOP — "GATE S FAIL — scout record missing."
If found: load. Extract: market signal, competitor landscape (locate {status_quo_comparator}),
  feasibility finding.

  gate_s_cleared: true    [ROLE B — sole producer]

---

## ROLE C — INCUMBENT THREAT ANALYST

Using the competitor landscape from ROLE B:

### INCUMBENT THREAT BLOCK

  incumbent_name:          [confirm against status_quo_comparator]
  incumbent_strength:      [one sentence — grounded in scout competitor landscape]
  incumbent_vulnerability: [one sentence — grounded in scout competitor landscape]

### INCUMBENT THREAT SCORE

Score the displacement difficulty on a 1–5 scale. Grounded in scout record only.

  | DIMENSION                 | EVIDENCE FROM SCOUT RECORD      | SCORE (1-5) |
  |---------------------------|---------------------------------|-------------|
  | Adoption breadth          | [what does the scout say?]      |             |
  | Switching cost            | [what does the scout say?]      |             |
  | Institutional inertia     | [what does the scout say?]      |             |
  | Active incumbent defense  | [what does the scout say?]      |             |

  threat_score: [average of four dimensions, rounded — 1=easy to displace, 5=very hard]
  threat_score_basis: [one sentence — what drives the score]

  If threat_score >= 4: apply THREAT SCORE CAP RULE at Stage 5.
    displacement_rating will be capped at MODERATE unless evidence_score = 5.

  incumbent_threat_locked: true    [ROLE C — sole producer]

ROLE C COMPLETE. Do not open GATE S until all three roles are complete.

---

## GATE S

  invariant_registry_confirmed: true (ROLE A) | gate_s_cleared: true (ROLE B)
  incumbent_threat_locked: true (ROLE C)
  All three true → open Stage 1. Any missing → STOP.

---

## Stage 1 — Hypothesis

Write: {topic}-hypothesis-{date}.md

Frontmatter (compressed): topic | date | scout_anchor: {topic}-scout-record-{date}.md [ROLE B] |
  gate_s_cleared: true [ROLE B] | invariant_registry_confirmed: true [ROLE A] |
  incumbent_threat_locked: true [ROLE C] | incumbent: [ROLE C — incumbent_name] |
  threat_score: [ROLE C — threat_score] | adversarial_reviewer_type [SESSION INVARIANT A] |
  ce_score_formula: CE-score = -2 if all null [SESSION INVARIANT B] |
  handoff_schema_locked: true [10 fields] | counter_hypothesis_closure_rule: active |
  null_tally_chain_rule: active | threat_score_cap_rule: active

Body:
  Hypothesis: [one sentence — what {topic} does better than ROLE C's {incumbent_name}]
  Basis: [3-5 scout signals; at least one speaks to ROLE C's incumbent_vulnerability]
  counter_hypothesis: [incumbent's strongest defense; Stage 5 obligation]
  threat_framing: [one sentence — given threat_score=[N], what level of evidence is needed?]

Write: {topic}-hypothesis-{date}.md. → Advance to Stage 2.

---

## Stage 2 — Web Search

Write: {topic}-websearch-{date}.md

Search for external evidence on {topic}. Record each finding: claim, source URL,
CE-relevant (yes/no), quote.

### INCUMBENT CHECK — Stage 2

Using ROLE C's INCUMBENT THREAT BLOCK (incumbent_name, incumbent_strength, incumbent_vulnerability):
  Does this evidence help displace {incumbent_name}?
  - Flag findings that address incumbent_strength or incumbent_vulnerability.
  - Note any finding that strengthens the incumbent — that is CE.
  - Does any finding directly address the threat_score dimension (incumbent_strength)?
    Flag as THREAT RELEVANT if yes.

Append CAMPAIGN SCORECARD row:

| STAGE   | ARTIFACT                    | DISPLACE SIGNAL | CE VERDICT   | NULL TALLY | SCHEMA | THREAT RELEVANCE | DISPLACE VERDICT |
|---------|-----------------------------|-----------------|--------------|------------|--------|------------------|------------------|
| Stage 2 | {topic}-websearch-{date}.md | [yes/no/partial]| [found/null] | [count]    | [N/10] | [high/med/low]   | N/A              |

  s2_ce_verdict: [found / null]    [Stage 2 sole producer — CE VERDICT OWNERSHIP TABLE]
  If null: SESSION INVARIANTs A and B active as pre-committed obligations.

Write: {topic}-websearch-{date}.md. → Advance to Stage 3.

---

## Stage 3 — Internal Intelligence

Write: {topic}-intelligence-{date}.md

Scan internal sources. Record each finding: artifact path, claim, CE-relevant (yes/no).

### INCUMBENT CHECK — Stage 3

Using ROLE C's INCUMBENT THREAT BLOCK:
  Does this evidence help displace {incumbent_name}?
  - Flag internal artifacts referencing {incumbent_name} or directly comparable approaches.
  - Note any finding that strengthens the incumbent — that is CE.
  - Does any finding address the threat_score dimension? Flag as THREAT RELEVANT.

Append CAMPAIGN SCORECARD row:

| STAGE   | ARTIFACT                       | DISPLACE SIGNAL | CE VERDICT   | NULL TALLY | SCHEMA | THREAT RELEVANCE | DISPLACE VERDICT |
|---------|--------------------------------|-----------------|--------------|------------|--------|------------------|------------------|
| Stage 3 | {topic}-intelligence-{date}.md | [yes/no/partial]| [found/null] | [count]    | [N/10] | [high/med/low]   | N/A              |

  s3_ce_verdict: [found / null]    [Stage 3 sole producer — CE VERDICT OWNERSHIP TABLE]
  If null: SESSION INVARIANTs A and B active as pre-committed obligations.

Write: {topic}-intelligence-{date}.md. → Advance to Stage 4.

---

## Stage 4 — Analysis

Write: {topic}-analysis-{date}.md

Analyze all evidence from Stages 2 and 3. Assess supporting evidence strength. Summarize
all CE found. If CE null: acknowledge with source list.

### INCUMBENT CHECK — Stage 4

Using ROLE C's INCUMBENT THREAT BLOCK and threat_score:
  Does the accumulated evidence from Stages 2, 3, and this analysis make a credible case
  for displacing {incumbent_name}? Consider threat_score=[N] in your verdict.

  Displacement verdict: [ ] Yes  [ ] No  [ ] Pending
  Basis: [one sentence — cite findings; relate to ROLE C's strength/vulnerability]
  Threat score check: given threat_score=[N], is the evidence proportionate to the
    displacement difficulty? [yes / no / needs more]

Append CAMPAIGN SCORECARD row:

| STAGE   | ARTIFACT                    | DISPLACE SIGNAL | CE VERDICT   | NULL TALLY | SCHEMA  | THREAT RELEVANCE | DISPLACE VERDICT     |
|---------|-----------------------------|-----------------|--------------|------------|---------|------------------|----------------------|
| Stage 4 | {topic}-analysis-{date}.md  | [yes/no/partial]| [found/null] | [count]    | [N/10]  | [high/med/low]   | [Yes/No/Pending]     |

### CAMPAIGN OUTCOME BLOCK

  s2_ce_verdict: [Stage 2 sole source] | s3_ce_verdict: [Stage 3 sole source]
  s4_ce_verdict: [Stage 4 sole source]

  null_tally_final: count of {s2, s3, s4}_ce_verdict = null
    derivation: named verdict fields per CE VERDICT OWNERSHIP TABLE — NOT via dual_lock_fired
    or co_activation_confirmed.

  incumbent_defense_closed: true if null_tally_final = 3; false otherwise.
    derivation: null_tally_final >= 3 → true. NOT via dual_lock_fired or co_activation_confirmed.

  Schema count: 10/10 declared fields intact.

Write: {topic}-analysis-{date}.md. → Advance to Stage 5.

---

## Stage 5 — Synthesis

Write: {topic}-synthesize-{date}.md

Confirm SESSION INVARIANTs A, B, C and THREAT SCORE CAP RULE in scope.
Retrieve PRE-COMMITTED HANDOFF SCHEMA (10 fields), CE VERDICT OWNERSHIP TABLE,
COUNTER-HYPOTHESIS CLOSURE RULE, NULL TALLY CHAIN RULE.

Read finalized CAMPAIGN SCORECARD.

### Findings

Read CAMPAIGN SCORECARD rows. Write 3-5 bullets traceable to scorecard rows or artifact
paths. For each, note relationship to ROLE C's incumbent_strength, incumbent_vulnerability,
or neutral to displacement. Flag THREAT RELEVANT findings separately.

### COUNTER-HYPOTHESIS RESOLUTION

MANDATORY — unconditionally required.

  counter_hypothesis: [restate from {topic}-hypothesis-{date}.md]

  Verdict:
    [ ] REFUTED — evidence directly defeats the claim: [cite]
    [ ] PARTIALLY REFUTED — weakened: [cite; state residual]
    [ ] OPEN RISK — nothing addresses the claim: [state needed evidence; flag]

  OPEN RISK: reduce confidence one tier (SESSION INVARIANT execution).

### Counter-Evidence

MANDATORY — unconditionally required.
If CE found: list with source and credibility.
If CE null: "No CE found. Sources: [S2 list], [S3 list]. Null = primary risk."
  Apply SESSION INVARIANT A and SESSION INVARIANT B — pre-committed obligations.

### ATOMIC DUAL-LOCK (activates if null_tally_final = 3)

NULL TALLY CHAIN (execution):
  S2: [found/null] → tally [N]
  S3: [found/null] → tally [N]
  S4: [found/null] → tally [N] = null_tally_final
Cross-check: terminal = Stage 4 null_tally_final. Mismatch: TALLY ERROR.

  LOCK 1 (SESSION INVARIANT A): Reviewer: {adversarial_reviewer_type}. Required before promotion.
  LOCK 2 (SESSION INVARIANT B): CE-score = -2. MEDIUM max. HIGH blocked.
  dual_lock_fired: [true if null_tally_final = 3]
  co_activation_confirmed: [must equal dual_lock_fired]

### Confidence and Displacement Rating

Apply THREAT SCORE CAP RULE:
  If threat_score >= 4 AND evidence_score < 5: displacement_rating capped at MODERATE.
  State explicitly: "THREAT SCORE CAP APPLIED: threat_score=[N] >= 4, evidence_score=[N] < 5.
    Displacement rating capped at MODERATE." OR "THREAT SCORE CAP NOT APPLIED: [reason]."

  evidence_score: [0-5]
  ce_score: [0/-2 per SESSION INVARIANT B]
  counter_hypothesis_verdict: [REFUTED / PARTIALLY REFUTED / OPEN RISK]
  displacement_rating: [STRONG / MODERATE / WEAK — THREAT SCORE CAP applied if applicable]
  threat_score: [from ROLE C]
  confidence: [LOW / MEDIUM / HIGH — HIGH blocked if ce_score = -2;
               OPEN RISK reduces one tier; threat_score cap considers displacement_rating]

### Handoff

SCHEMA COMPLIANCE: confirm 10 fields against PRE-COMMITTED HANDOFF SCHEMA. Log mismatches.
DERIVATION ANNOTATION RULE (SESSION INVARIANT C — execution):

  scout_anchor: {topic}-scout-record-{date}.md
    [derived from: ROLE B scout load]
  hypothesis: {topic}-hypothesis-{date}.md
    [derived from: Stage 1 artifact write]
  analysis: {topic}-analysis-{date}.md
    [derived from: Stage 4 artifact write]
  null_tally_final: [0-3]
    positive_derivation: count of {s2, s3, s4}_ce_verdict = null per CE VERDICT OWNERSHIP TABLE
    independence_chain: NOT via dual_lock_fired; NOT via co_activation_confirmed
    [derived from: Stage 4 CAMPAIGN OUTCOME BLOCK; chain echoed in ATOMIC DUAL-LOCK]
  incumbent_defense_closed: [true/false]
    positive_derivation: null_tally_final >= 3 → true
    independence_chain: NOT via dual_lock_fired; NOT via co_activation_confirmed
    [derived from: null_tally_final per CAMPAIGN OPEN schema]
  co_activation_confirmed: [must equal dual_lock_fired]
    positive_derivation: dual_lock_fired in ATOMIC DUAL-LOCK
    independence_chain: NOT via incumbent_defense_closed; NOT directly via null_tally_final
    [derived from: dual_lock_fired per CAMPAIGN OPEN schema]
  threat_score: [1-5]
    [derived from: ROLE C — INCUMBENT THREAT SCORE block; grounded in scout competitor landscape]
  confidence: [LOW/MEDIUM/HIGH]
    [derived from: evidence_score + ce_score per SESSION INVARIANT B
     + counter_hypothesis_verdict adjustment + THREAT SCORE CAP RULE]
  next: topic-story
    [derived from: static handoff target]
  schema_compliance_confirmed: true
    [derived from: synthesis-time check — 10 fields present; sources match; CE formula confirmed;
     NULL TALLY CHAIN echoed; COUNTER-HYPOTHESIS RESOLUTION complete; THREAT SCORE CAP evaluated;
     SESSION INVARIANT C executed]

Confirm: "Synthesis complete. Displacement case against {incumbent_name} (threat_score=[N],
          ROLE C): [confidence] confidence. Counter-hypothesis: [verdict].
          null_tally_final: [count] (S2=[v] → S3=[v] → S4=[v]).
          Displacement rating: [rating] [cap note if applicable].
          Evidence brief ready for topic-story.
          Artifact written: {topic}-synthesize-{date}.md."
```
```

---

**Variation summary for R12:**

| Variation | Axis | C-34 mechanism | Key structural difference from R11 |
|-----------|------|----------------|-------------------------------------|
| V-01 | Role Sequence | Named INCUMBENT CHECK blocks trace to ROLE C by name; GATE S has 3 fields | Third blocking role (ROLE C) owns the INCUMBENT THREAT BLOCK |
| V-02 | Scorecard Format | INCUMBENT CHECK produces scorecard column; Stage 4 has DISPLACEMENT VERDICT column | Running CAMPAIGN SCORECARD table; stage confirmation = appended row |
| V-03 | Sparse Lifecycle | INCUMBENT CHECK is dominant section per stage; expanded sub-questions at Stage 4 | Minimal boundary prose; structural notes compressed to footer tokens |
| V-04 | Role Sequence + Phrasing Register | "Ask now: does this help unseat {incumbent_name}?" imperative; GATE S is numbered checklist | Three roles + direct second-person throughout; no "SESSION INVARIANT" labels |
| V-05 | All Three + Inertia Score | INCUMBENT CHECK includes THREAT RELEVANCE column; Stage 4 checks threat proportionality | ROLE C scores threat 1–5; 10-field schema; threat_score caps displacement_rating |

**What R12 adds vs R11**: All five variations fully satisfy C-34 (named INCUMBENT CHECK at Stages 2, 3, 4 with Stage 4 displacement verdict). The variation axes test whether C-34's structural requirement holds under role proliferation (V-01/V-04), tabular compression (V-02/V-05), minimal ceremony (V-03/V-05), non-formal language (V-04), and a quantified inertia score that mechanically modulates the confidence output (V-05).
