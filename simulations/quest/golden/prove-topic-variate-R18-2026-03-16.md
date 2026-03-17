---
skill: quest-variate
skill_target: prove-topic
round: R18
date: 2026-03-16
rubric: prove-topic-rubric-v17-2026-03-16.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [role_dependency_annotation, displacement_momentum_score, block3_multi_stage_chain]
  combined: [V-04 (role_dependency_annotation + block3_multi_stage_chain), V-05 (all_three + full_structural_stack)]
r17_anchor: >
  R17 V-05 established three new excellence patterns now codified as aspirational criteria:
  C-15 (entry conditions read prior artifact on disk, extract concrete value, validate
  received signal against that extracted value — tamper-resistant), C-16 (Stage 5 declares
  three named blocks: CONFIDENCE CHAIN RESOLUTION -> COUNTER-HYPOTHESIS RESOLUTION ->
  DISPLACEMENT INTEGRITY CHECK, synthesis hard-gated on BLOCK 3 completion), C-17
  (dependency-driven block inversion: declared structure preserved, execution order adapts
  causally when a block requires output from a later-declared block). Denominator updates
  to 9.
r18_context: >
  R17 V-05 achieves C-15 and C-16 and introduces C-17. R18 treats the full R17 V-05
  structural stack as the mandatory baseline, then explores NEW axes that probe the
  edges of C-15/C-16/C-17 and adjacent structural territory:

  V-01 (single: role_dependency_annotation): C-17 exists as a pattern but the current
  baseline does not make data dependencies explicit in the role declaration table. V-01
  adds a DEPENDENCY column to the ROLE OWNERSHIP TABLE, listing the exact field each
  role requires before it can execute. When Role A (HYPOTHESIS ARCHITECT) depends on
  Role C output (incumbent_threat_locked), the dependency annotation forces execution
  inversion even if A is declared first. Tests whether making dependencies a first-class
  column in the role table produces a more auditable C-17 than informal role ordering.

  V-02 (single: displacement_momentum_score): The current baseline tracks yes/no/inconclusive
  per incumbent check per stage. V-02 adds a numeric DISPLACEMENT DELTA (range: -2 to +2)
  to each stage's incumbent check table, representing directional evidence strength. The
  deltas accumulate into a displacement_momentum_score that flows into Stage 5 BLOCK 3
  (DISPLACEMENT INTEGRITY CHECK) alongside the Stage 4 aggregate verdict. Tests whether
  a continuous momentum signal across all three evidence stages produces a more defensible
  displacement_conclusion than a single Stage 4 verdict.

  V-03 (single: block3_multi_stage_chain): C-16 defines BLOCK 3 as DISPLACEMENT INTEGRITY
  CHECK but the current implementation only cross-checks Stage 4's aggregate vs Stage 5's
  displacement_conclusion. V-03 expands BLOCK 3 to reconstruct displacement evidence from
  all three stages (S2, S3, S4 incumbent checks individually), compare the per-stage
  trajectory to the final conclusion, and flag any stage where the conclusion runs counter
  to that stage's evidence. Tests whether a full three-stage displacement chain inside
  BLOCK 3 (rather than a single Stage 4 reference) closes the loop more completely.

  V-04 (combined: role_dependency_annotation + block3_multi_stage_chain): V-01 + V-03.
  Role dependency annotations feed auditable execution order; BLOCK 3 reconstructs the
  full three-stage displacement chain. Together they form a complete dependency-audit
  stack from pre-stage roles through Stage 5 synthesis.

  V-05 (full: all three + full structural stack): V-01 + V-02 + V-03 on top of the
  complete R17 V-05 baseline (C-15 exact-value artifact reads, C-16 three-block Stage 5,
  C-17 dependency inversion, confidence chain, compound exit signals, count-gated
  thresholds, ATOMIC DUAL-LOCK). Tests whether all three new axes simultaneously produce
  a 9/9 aspirational score against the v17 rubric.
---

# prove-topic Variations — Round 18 (rubric v17)

**Skill**: prove-topic
**Rubric**: v17 (C-01–C-05 essential, C-06–C-08 recommended, C-09–C-17 aspirational)
**Date**: 2026-03-16
**Round**: R18

---

## Context: what informed this round

R17 V-05 established the structural stack used as R18 baseline. The v17 rubric extracted
three new patterns as aspirational criteria C-15, C-16, C-17:

| Change | R17 V-05 | R18 target | Design consequence |
|--------|----------|------------|-------------------|
| C-15 (tamper-resistant reads) | Entry conditions read prior artifact, extract exact value, validate signal against it | Carried as baseline in all R18 variations | V-05 extends reads to every inter-stage handoff field |
| C-16 (Stage 5 three-block) | CONFIDENCE CHAIN RESOLUTION -> COUNTER-HYPOTHESIS RESOLUTION -> DISPLACEMENT INTEGRITY CHECK, synthesis hard-gated on BLOCK 3 | Carried as baseline | V-03 expands BLOCK 3 to full three-stage displacement chain reconstruction |
| C-17 (dependency-driven inversion) | Execution inverts when a block requires output from a later-declared block | Carried as pattern | V-01 makes this a first-class DEPENDENCY column in the ROLE OWNERSHIP TABLE |

All five R18 variations carry the full R17 V-05 structural stack as their floor.

---

## V-01 — Role Dependency Annotation

**Axis**: role_dependency_annotation (single)
**Hypothesis**: C-17 is currently demonstrated by role execution order (C runs before A
because A needs incumbent_threat_locked from C) but the dependency itself is implicit —
a reader must infer it from field names. If the ROLE OWNERSHIP TABLE gains a DEPENDS ON
column listing exact required fields, the dependency inversion becomes auditable: any
reader can verify that execution order is causally justified by declared dependencies,
not arbitrary. This makes C-17 tamper-evident (structure declared) rather than emergent.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

depth: standard
confidence: standard
for: {value}
iterations: 1

Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
The campaign builds the case for displacing {status_quo_comparator} with {topic}.
Six stages (Stage 0 = gate, Stages 1-5 = evidence + synthesis). Each stage has numbered
ENTRY CONDITIONS and a named EXIT SIGNAL. No stage body begins until entry conditions confirm.

---

## CAMPAIGN OPEN

  topic:                 {topic}
  date:                  {date}
  status_quo_comparator: [name the incumbent approach this topic must displace]

### INCUMBENT ANCHOR

Fill before any role or invariant registration.

  incumbent_name:          [full name of status_quo_comparator]
  incumbent_strength:      [one sentence: why the incumbent is currently winning]
  incumbent_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]

### SESSION INVARIANTS TABLE

SESSION INVARIANT D leads. All invariants carry: "cannot be modified or bypassed at
any subsequent stage." Register all four before roles execute.

  ID   | NAME                      | DECLARATION
  -----|---------------------------|------------------------------------------------------
  D    | INCUMBENT CHECK PHRASING  | Stage 2: "Does [evidence item] support the displacement
       | REGISTER                  |   of {status_quo_comparator} by {topic} on [dimension]?
       |                           |   [Yes / No / Inconclusive]"
       |                           | Stage 3: "Does [practitioner account] reveal a viable
       |                           |   transition path from {status_quo_comparator} to
       |                           |   {topic} for [use case]? [Yes / No / Inconclusive]"
       |                           | Stage 4: "Does [prototype result] make a credible case
       |                           |   for displacing {status_quo_comparator} with {topic}?
       |                           |   [Yes / No / Pending]"
       |                           | Enforcement: Template deviation = format error.
       |                           | Cannot be modified or bypassed at any stage.
  -----|---------------------------|------------------------------------------------------
  A    | ADVERSARIAL REVIEWER      | adversarial_reviewer_type: [role most likely to
       | TYPE                      |   challenge the displacement claim].
       |                           | Activation: null_tally_final >= 3.
       |                           | Cannot be modified or bypassed at synthesis.
  -----|---------------------------|------------------------------------------------------
  B    | CONFIDENCE CAP            | null_ce_cap_rule: confidence_composite -= 2 if
       |                           |   null_tally_final >= 3 (hard cap).
       |                           | Cannot be softened or overridden at synthesis.
  -----|---------------------------|------------------------------------------------------
  C    | DERIVATION ANNOTATION     | annotation_rule: Every handoff field carries
       |                           |   [derived from: X]. Unlabeled = format error.
       |                           | Cannot be modified or bypassed at synthesis.

### ROLE OWNERSHIP TABLE

DEPENDENCY DECLARATIONS: Each role lists its required fields. If Role M declares a
dependency on a field owned by Role N (where N is declared after M), execution inverts:
Role N executes before Role M to satisfy the dependency. Declared order is preserved
in the table; execution order adapts to dependencies. Execution inversion is NOT an
error — it is the correct causal response.

  ROLE   | TITLE                    | OWNED FIELD               | DEPENDS ON          | EXECUTE
  -------|--------------------------|---------------------------|---------------------|--------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked   | (none)              | FIRST (no deps)
  ROLE B | SCOUT LOADER             | gate_s_cleared            | (none)              | SECOND (no deps)
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | incumbent_threat_locked (ROLE C),
         |                          |                           | gate_s_cleared (ROLE B) | THIRD (deps: C and B must precede)

DEPENDENCY INVERSION RULE (active):
  If any role's DEPENDS ON field references a field owned by a role declared later
  in this table, execution inverts to satisfy the dependency. The EXECUTE column reflects
  post-inversion order. Execution order deviations from declared order require a
  dependency justification annotation in the EXECUTE column.

ROLE C execution (fill now):
  Reads INCUMBENT ANCHOR above. Confirms analysis complete.
  incumbent_threat_locked: [true when incumbent_name, incumbent_strength,
                             incumbent_vulnerability all filled]
  dependency_satisfied_by: [n/a — no upstream dependencies]

ROLE B execution (fill now):
  scout_artifact:  [{topic}-scout-record-{date}.md or equivalent]
  scout_loaded:    [true / false]
  gate_s_cleared:  [true if scout_loaded; CAMPAIGN BLOCKED otherwise]
  dependency_satisfied_by: [n/a — no upstream dependencies]

ROLE A execution (fill now):
  Confirms all four SESSION INVARIANT TABLE rows filled and active.
  invariant_registry_confirmed: [true when all four invariants in table are registered]
  dependency_satisfied_by: [incumbent_threat_locked from ROLE C — confirmed; gate_s_cleared from ROLE B — confirmed]
  execution_inversion_note: [ROLE A declared third; executed third — no inversion required because C and B precede by declaration]

### CE VERDICT OWNERSHIP TABLE

  FIELD            | OWNED BY      | FORMULA
  -----------------|---------------|-----------------------------------------------------
  s2_ce_verdict    | Stage 2       | null if no CE; citation if CE found
  s3_ce_verdict    | Stage 3       | null if no CE; citation if CE found
  s4_ce_verdict    | Stage 4       | null if no CE; description if CE found
  null_tally_final | Stage 4 close | count(null) across s2 + s3 + s4

NULL TALLY CHAIN RULE (locked): Running tally from Stage 2. Stage 4 close reconstructs
full chain. ATOMIC DUAL-LOCK cross-checks at synthesis. Mismatch = integrity failure.

### PRE-COMMITTED HANDOFF SCHEMA TABLE

  FIELD                      | DERIVATION SOURCE                         | IND. CHAIN
  ---------------------------|-------------------------------------------|------------------
  scout_anchor               | ROLE B scout load                         | n/a
  incumbent_threat_locked    | ROLE C analysis                           | n/a
  hypothesis                 | Stage 1 artifact                          | n/a
  counter_hypothesis         | Stage 1 artifact                          | n/a
  s2_ce_verdict              | Stage 2 artifact                          | n/a
  s3_ce_verdict              | Stage 3 artifact                          | n/a
  s4_ce_verdict              | Stage 4 artifact                          | n/a
  null_tally_final           | s2+s3+s4 CE verdicts                      | not through co_activation
  co_activation_confirmed    | ATOMIC DUAL-LOCK                          | not through incumbent_defense
  incumbent_defense_closed   | s2+s3+s4 direct chain                     | not through co_activation
  confidence_composite       | Stage 5 minus reductions                  | capped by INV B

---

## STAGE 0 — GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] CAMPAIGN OPEN fields filled (topic, date, status_quo_comparator)
  [ ] INCUMBENT ANCHOR filled (incumbent_name, strength, vulnerability)
  [ ] SESSION INVARIANTS TABLE complete — all four rows filled
  [ ] ROLE OWNERSHIP TABLE dependency declarations complete — DEPENDS ON column filled for all roles
  [ ] Execution inversion check complete — any role with upstream dependencies has dependency_satisfied_by confirmed
  [ ] ROLE C executed — incumbent_threat_locked = true
  [ ] ROLE B executed — gate_s_cleared = true
  [ ] ROLE A executed — invariant_registry_confirmed = true

STAGE 0 BODY:

  CLEARANCE TABLE:
  STEP | FIELD                        | OWNER   | REQUIRED | RESULT
  -----|------------------------------|---------|----------|--------
  1    | incumbent_threat_locked      | ROLE C  | true     | [confirm or BLOCKED]
  2    | gate_s_cleared               | ROLE B  | true     | [confirm or BLOCKED]
  3    | invariant_registry_confirmed | ROLE A  | true     | [confirm or BLOCKED]
  4    | dependency_declarations_complete | TABLE | true   | [confirm or BLOCKED]

  First BLOCKED step halts campaign. Record step and owning role.

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open — Steps 1-4 all confirmed. SESSION INVARIANT D active.
   Dependency declarations auditable. Advancing to Stage 1."

---

## STAGE 1 — HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] STAGE 0 EXIT SIGNAL received: gate_open
  [ ] scout_artifact path available from ROLE B
  [ ] Read scout_artifact from disk: extract scout_anchor_value (source of truth)
  [ ] SESSION INVARIANT D templates registered

STAGE 1 BODY:
Load scout artifact from disk path. Extract scout_anchor_value. Frame hypothesis.

  scout_artifact_path:          [path from ROLE B — not inferred]
  scout_anchor_value:           [extracted from disk at {scout_artifact_path} — not from memory]
  validation: scout_anchor == scout_anchor_value: [match / INTEGRITY FAILURE]
  hypothesis:                   [falsifiable claim about {topic}]
  counter_hypothesis:           [incumbent's best defense — grounded in ROLE C analysis]
  confidence_prior:             [initial confidence score: 1–10]
  incumbent_threat_locked:      [true — from ROLE C]
  gate_s_cleared:               [true — from ROLE B]
  invariant_registry_confirmed: [true — from ROLE A]

Write artifact: {topic}-hypothesis-{date}.md. Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked(confidence_prior=[value])
  "STAGE 1 EXIT: hypothesis_locked — {topic}-hypothesis-{date}.md written.
   confidence_prior=[value]. Stage 2 ready."

---

## STAGE 2 — WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] STAGE 1 EXIT SIGNAL received: hypothesis_locked(confidence_prior=[value])
  [ ] Read {topic}-hypothesis-{date}.md from disk: extract confidence_prior_disk
  [ ] Validate: confidence_prior from signal == confidence_prior_disk — mismatch = INTEGRITY FAILURE
  [ ] hypothesis artifact confirmed written
  [ ] SESSION INVARIANT D Stage 2 template active

STAGE 2 BODY:
Gather minimum 3 external sources.

INCUMBENT CHECK TABLE — Stage 2 (SESSION INVARIANT D, Stage 2 template applied verbatim):
Structural origin: ROLE C `incumbent_threat_locked` (confirmed GATE S Step 1).

  ITEM | SOURCE (URL or citation) | SUMMARY (1 sentence) | TEMPLATE APPLIED & VERDICT
  -----|--------------------------|----------------------|------------------------------
  1    | [source]                 | [summary]            | "Does [item 1] support
  2    | [source]                 | [summary]            |  displacement of [comparator]
  3    | [source]                 | [summary]            |  by [topic] on [dim]? [verdict]"

  s2_incumbent_check_summary: [N support / M counter / P inconclusive]
  s2_ce_verdict:              [null if no CE; cite item if found]
  confidence_delta_s2:        [+1 / 0 / -1 based on evidence weight]
  running_confidence:         [confidence_prior + confidence_delta_s2]

Running null tally: "Running tally: [N] null across 1 stage complete. 2 stages remain."
SCHEMA INTEGRITY: [N]/11 handoff fields populated — 0 additions, 0 omissions.
Write artifact: {topic}-websearch-{date}.md. Confirm write.

STAGE 2 EXIT SIGNAL: websearch_complete(count=[N], running_confidence=[value])
  "STAGE 2 EXIT: websearch_complete — s2_ce_verdict = [value]. Tally: [N].
   running_confidence=[value]. Stage 3 ready."

---

## STAGE 3 — INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT SIGNAL received: websearch_complete(count=[N], running_confidence=[value])
  [ ] Read {topic}-websearch-{date}.md from disk: extract running_confidence_disk
  [ ] Validate: running_confidence from signal == running_confidence_disk — mismatch = INTEGRITY FAILURE
  [ ] s2_ce_verdict recorded (null or value — not blank)
  [ ] SESSION INVARIANT D Stage 3 template active

STAGE 3 BODY:
Simulate 2-3 practitioner interviews.

INCUMBENT CHECK TABLE — Stage 3 (SESSION INVARIANT D, Stage 3 template applied verbatim):
Structural origin: ROLE C `incumbent_threat_locked` (confirmed GATE S Step 1).

  PRACTITIONER     | KEY ACCOUNT (1 sentence)     | TEMPLATE APPLIED & VERDICT
  -----------------|------------------------------|------------------------------
  [type 1]         | [quote or paraphrase]        | "Does [account 1] reveal a viable
  [type 2]         | [quote or paraphrase]        |  transition path from [comparator]
  [type 3]         | [quote or paraphrase]        |  to [topic] for [use case]? [verdict]"

  s3_incumbent_check_summary: [N support / M counter / P inconclusive]
  s3_ce_verdict:              [null if no CE; cite account if found]
  confidence_delta_s3:        [+1 / 0 / -1 based on interview weight]
  running_confidence:         [prev_running_confidence + confidence_delta_s3]

Running null tally: "Running tally: [N] null across 2 stages complete. 1 stage remains."
SCHEMA INTEGRITY: [N]/11 handoff fields populated — 0 additions, 0 omissions.
Write artifact: {topic}-interview-{date}.md. Confirm write.

STAGE 3 EXIT SIGNAL: interview_complete(count=[N], running_confidence=[value])
  "STAGE 3 EXIT: interview_complete — s3_ce_verdict = [value]. Tally: [N].
   running_confidence=[value]. Stage 4 ready."

---

## STAGE 4 — PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT SIGNAL received: interview_complete(count=[N], running_confidence=[value])
  [ ] Read {topic}-interview-{date}.md from disk: extract running_confidence_disk
  [ ] Validate: running_confidence from signal == running_confidence_disk — mismatch = INTEGRITY FAILURE
  [ ] s3_ce_verdict recorded (null or value — not blank)
  [ ] SESSION INVARIANT D Stage 4 template active

STAGE 4 BODY:
Design and assess minimal prototype.

  prototype_design:   [brief description]
  prototype_result:   [what was learned — 1-3 sentences]

INCUMBENT CHECK TABLE — Stage 4 (SESSION INVARIANT D, Stage 4 template applied verbatim):
Structural origin: ROLE C `incumbent_threat_locked` (confirmed GATE S Step 1).

  ITEM       | PROTOTYPE RESULT (1 sentence) | TEMPLATE APPLIED & VERDICT
  -----------|-------------------------------|-------------------------------
  prototype  | [prototype_result]            | "Does [prototype result] make a
             |                               |  credible case for displacing
             |                               |  [comparator] with [topic]?
             |                               |  [Yes / No / Pending]"

  s4_displacement_verdict: [Yes / No / Pending]
  s4_ce_verdict:           [null if no CE; description if found]
  confidence_delta_s4:     [+1 / 0 / -1 based on prototype result]
  running_confidence:      [prev_running_confidence + confidence_delta_s4]

Final null tally:
  null_tally_final = [N]
  Cross-check: "Running count from Stage 3 was [M]. Final is [N]. Match: [true/false]."

SCHEMA INTEGRITY: [N]/11 handoff fields populated.
Write artifact: {topic}-prototype-{date}.md. Confirm write.

STAGE 4 EXIT SIGNAL: prototype_complete(count=[null_tally_final], running_confidence=[value])
  "STAGE 4 EXIT: prototype_complete — s4_ce_verdict = [value]. null_tally_final = [N].
   running_confidence=[value]. Stage 5 ready."

---

## STAGE 5 — SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT SIGNAL received: prototype_complete(count=[N], running_confidence=[value])
  [ ] Read {topic}-prototype-{date}.md from disk: extract running_confidence_disk, null_tally_final_disk
  [ ] Validate: running_confidence from signal == running_confidence_disk — mismatch = INTEGRITY FAILURE
  [ ] Validate: null_tally_final from signal == null_tally_final_disk — mismatch = INTEGRITY FAILURE
  [ ] counter_hypothesis from Stage 1 present for resolution
  [ ] All four SESSION INVARIANT TABLE rows active

STAGE 5 BODY: THREE-BLOCK STRUCTURE
BLOCK 1 and BLOCK 2 run first. BLOCK 3 requires output from BLOCK 1 and BLOCK 2.
DEPENDENCY: BLOCK 3 depends on confidence_chain_resolved (BLOCK 1) and
counter_hypothesis_verdict (BLOCK 2). If BLOCK 3 were declared first, execution would
invert to BLOCK 1 then BLOCK 2 then BLOCK 3 by the dependency rule. As declared, order
is causal: BLOCK 1 -> BLOCK 2 -> BLOCK 3.

SYNTHESIS HARD GATE: no synthesis fields may be populated until BLOCK 3 COMPLETE signal received.

### BLOCK 1: CONFIDENCE CHAIN RESOLUTION

  confidence_chain_equation: [confidence_prior] + [delta_s2] + [delta_s3] + [delta_s4] = [sum]
  null_cap_applied:          [yes (sum -= 2) if null_tally_final >= 3; no otherwise]
  confidence_chain_resolved: [final value after cap]

BLOCK 1 COMPLETE signal: "BLOCK 1 COMPLETE — confidence_chain_resolved = [value]."

### BLOCK 2: COUNTER-HYPOTHESIS RESOLUTION

  COUNTER_HYPOTHESIS     | VERDICT                                  | EVIDENCE
  -----------------------|------------------------------------------|-------------------
  [from Stage 1]         | REFUTED / PARTIALLY REFUTED / OPEN RISK  | [cite stage artifact]

OPEN RISK: reduce confidence_chain_resolved by one tier per OPEN RISK item.
  open_risk_count:         [N]
  cr_delta:                [N * -1]
  confidence_post_cr:      [confidence_chain_resolved + cr_delta]
  counter_hypothesis_verdict: [recorded]

BLOCK 2 COMPLETE signal: "BLOCK 2 COMPLETE — counter_hypothesis_verdict recorded. confidence_post_cr = [value]."

### BLOCK 3: DISPLACEMENT INTEGRITY CHECK

DEPENDENCY: requires confidence_chain_resolved (BLOCK 1) and counter_hypothesis_verdict (BLOCK 2).
Both BLOCK 1 COMPLETE and BLOCK 2 COMPLETE signals must be received before BLOCK 3 begins.

ATOMIC DUAL-LOCK (runs inside BLOCK 3):
NULL TALLY CHAIN reconstruction:
  S2 -> [s2_ce_verdict: null or value]
  S3 -> [s3_ce_verdict: null or value]
  S4 -> [s4_ce_verdict: null or value]
  null_tally_final = [N]
  Cross-check vs Stage 4 exit count: [Match / Mismatch]

If null_tally_final >= 3:
  Lock 1 (SESSION INVARIANT A): adversarial review by [adversarial_reviewer_type]. BLOCKED.
  Lock 2 (SESSION INVARIANT B): confidence_composite -= 2 (hard cap).
  co_activation_confirmed: dual_lock_fired
Else:
  co_activation_confirmed: not_triggered

  displacement_conclusion_check:  [s4_displacement_verdict from Stage 4 artifact]
  displacement_conclusion:        [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED — must be consistent with s4_displacement_verdict]
  consistency_flag:               [CONSISTENT / INCONSISTENT — mismatch = structural error before synthesis closes]

BLOCK 3 COMPLETE signal: "BLOCK 3 COMPLETE — displacement_conclusion = [value]. consistency_flag = [CONSISTENT/INCONSISTENT]."

SYNTHESIS GATE CHECK: [ ] BLOCK 3 COMPLETE received. If not: SYNTHESIS BLOCKED.

### SYNTHESIS BODY

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:      [2-3 sentences integrating Stages 2, 3, 4 — with explicit
                           incumbent displacement verdict from Stage 4 check]
  confidence_composite:  [confidence_post_cr — final value after all reductions]
  key_risk:              [primary adoption risk framed as residual incumbent strength]

### HANDOFF TABLE

SESSION INVARIANT C enforced. All fields carry [derived from: X]. Unlabeled = format error.

  FIELD                      | VALUE   | DERIVATION                          | IND. CHAIN
  ---------------------------|---------|-------------------------------------|------------------
  scout_anchor               | [value] | [derived from: ROLE B scout load]   | n/a
  incumbent_threat_locked    | [true]  | [derived from: ROLE C analysis]     | n/a
  hypothesis                 | [value] | [derived from: Stage 1 artifact]    | n/a
  counter_hypothesis         | [value] | [derived from: Stage 1 artifact]    | n/a
  s2_ce_verdict              | [value] | [derived from: Stage 2 artifact]    | n/a
  s3_ce_verdict              | [value] | [derived from: Stage 3 artifact]    | n/a
  s4_ce_verdict              | [value] | [derived from: Stage 4 artifact]    | n/a
  null_tally_final           | [N]     | [derived from: s2+s3+s4 CE verdicts]| does not pass through co_activation
  co_activation_confirmed    | [value] | [derived from: ATOMIC DUAL-LOCK]    | does not pass through incumbent_defense
  incumbent_defense_closed   | [t/f]   | [derived from: s2+s3+s4 direct]     | does not pass through co_activation
  confidence_composite       | [value] | [derived from: Stage 5 Block 3]     | capped by INV B
  schema_compliance_confirmed| [true]  | [all 11 fields, sources match]      | n/a

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete — Evidence brief ready for topic-story."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## V-02 — Displacement Momentum Score

**Axis**: displacement_momentum_score (single)
**Hypothesis**: The current baseline tracks displacement evidence as Yes/No/Inconclusive
per incumbent check per stage. This produces a binary aggregate (supported or not) at
Stage 4. If each stage's incumbent check produces a DISPLACEMENT DELTA on a -2 to +2
scale (reflecting evidence direction and strength), the deltas accumulate into a running
displacement_momentum_score. By Stage 5 BLOCK 3, the displacement_conclusion can reference
not just the Stage 4 verdict but the full momentum trajectory — revealing whether
displacement evidence strengthened or weakened across the campaign. A decelerating
trajectory (strong S2, weak S4) warrants different confidence framing than an accelerating
one.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

depth: standard
confidence: standard
for: {value}
iterations: 1

Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
The campaign builds the case for displacing {status_quo_comparator} with {topic}.
Six stages (Stage 0 = gate, Stages 1-5 = evidence + synthesis). Each stage has numbered
ENTRY CONDITIONS and a named EXIT SIGNAL. No stage body begins until entry conditions confirm.

---

## CAMPAIGN OPEN

  topic:                 {topic}
  date:                  {date}
  status_quo_comparator: [name the incumbent approach this topic must displace]

### INCUMBENT ANCHOR

Fill before any role or invariant registration.

  incumbent_name:          [full name of status_quo_comparator]
  incumbent_strength:      [one sentence: why the incumbent is currently winning]
  incumbent_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]

### DISPLACEMENT MOMENTUM SCALE

Applied at each evidence stage incumbent check. Records direction and strength of
displacement evidence. Accumulates into displacement_momentum_score at Stage 5.

  DELTA | MEANING
  ------|------------------------------------------------------------------
  +2    | Strong evidence supporting displacement — challenger clearly ahead
  +1    | Moderate evidence supporting displacement — challenger gaining
   0    | Neutral or inconclusive — no net displacement signal
  -1    | Moderate evidence for incumbent — challenger not clearly ahead
  -2    | Strong evidence for incumbent — incumbent clearly winning on this dimension

### SESSION INVARIANTS TABLE

SESSION INVARIANT D leads. All invariants carry: "cannot be modified or bypassed at
any subsequent stage." Register all four before roles execute.

  ID   | NAME                      | DECLARATION
  -----|---------------------------|------------------------------------------------------
  D    | INCUMBENT CHECK PHRASING  | Stage 2: "Does [evidence item] support the displacement
       | REGISTER                  |   of {status_quo_comparator} by {topic} on [dimension]?
       |                           |   [Yes / No / Inconclusive] — DELTA: [value]"
       |                           | Stage 3: "Does [practitioner account] reveal a viable
       |                           |   transition path from {status_quo_comparator} to
       |                           |   {topic} for [use case]? [Yes / No / Inconclusive]
       |                           |   — DELTA: [value]"
       |                           | Stage 4: "Does [prototype result] make a credible case
       |                           |   for displacing {status_quo_comparator} with {topic}?
       |                           |   [Yes / No / Pending] — DELTA: [value]"
       |                           | Enforcement: Template deviation = format error.
       |                           | Cannot be modified or bypassed at any stage.
  -----|---------------------------|------------------------------------------------------
  A    | ADVERSARIAL REVIEWER      | adversarial_reviewer_type: [role most likely to
       | TYPE                      |   challenge the displacement claim].
       |                           | Activation: null_tally_final >= 3.
       |                           | Cannot be modified or bypassed at synthesis.
  -----|---------------------------|------------------------------------------------------
  B    | CONFIDENCE CAP            | null_ce_cap_rule: confidence_composite -= 2 if
       |                           |   null_tally_final >= 3 (hard cap).
       |                           | Cannot be softened or overridden at synthesis.
  -----|---------------------------|------------------------------------------------------
  C    | DERIVATION ANNOTATION     | annotation_rule: Every handoff field carries
       |                           |   [derived from: X]. Unlabeled = format error.
       |                           | Cannot be modified or bypassed at synthesis.

### ROLE OWNERSHIP TABLE

ROLE C executes first. Roles run in sequence C -> B -> A before Stage 0 begins.

  ROLE   | TITLE                    | OWNED FIELD               | GATE S STEP | EXECUTE
  -------|--------------------------|---------------------------|-------------|--------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked   | Step 1      | FIRST
  ROLE B | SCOUT LOADER             | gate_s_cleared            | Step 2      | SECOND
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | Step 3   | THIRD

ROLE C execution (fill now):
  Reads INCUMBENT ANCHOR above. Confirms analysis complete.
  incumbent_threat_locked: [true when all three INCUMBENT ANCHOR fields filled]
  displacement_baseline_delta: [initial expected delta range given incumbent_vulnerability]

ROLE B execution (fill now):
  scout_artifact:  [{topic}-scout-record-{date}.md or equivalent]
  scout_loaded:    [true / false]
  gate_s_cleared:  [true if scout_loaded; CAMPAIGN BLOCKED otherwise]

ROLE A execution (fill now):
  Confirms all four SESSION INVARIANT TABLE rows filled and active.
  invariant_registry_confirmed: [true when all four invariants registered]
  displacement_scale_registered: [true — DISPLACEMENT MOMENTUM SCALE declared above]

### CE VERDICT OWNERSHIP TABLE

  FIELD                      | OWNED BY      | FORMULA
  ---------------------------|---------------|-----------------------------------------------------
  s2_ce_verdict              | Stage 2       | null if no CE; citation if CE found
  s3_ce_verdict              | Stage 3       | null if no CE; citation if CE found
  s4_ce_verdict              | Stage 4       | null if no CE; description if CE found
  null_tally_final           | Stage 4 close | count(null) across s2 + s3 + s4
  displacement_momentum_score| Stage 5       | sum of all DELTA values from S2 + S3 + S4

NULL TALLY CHAIN RULE (locked): Running tally from Stage 2. Stage 4 close reconstructs
full chain. ATOMIC DUAL-LOCK cross-checks at synthesis. Mismatch = integrity failure.

### PRE-COMMITTED HANDOFF SCHEMA TABLE

  FIELD                      | DERIVATION SOURCE                         | IND. CHAIN
  ---------------------------|-------------------------------------------|------------------
  scout_anchor               | ROLE B scout load                         | n/a
  incumbent_threat_locked    | ROLE C analysis                           | n/a
  hypothesis                 | Stage 1 artifact                          | n/a
  counter_hypothesis         | Stage 1 artifact                          | n/a
  s2_ce_verdict              | Stage 2 artifact                          | n/a
  s3_ce_verdict              | Stage 3 artifact                          | n/a
  s4_ce_verdict              | Stage 4 artifact                          | n/a
  null_tally_final           | s2+s3+s4 CE verdicts                      | not through co_activation
  co_activation_confirmed    | ATOMIC DUAL-LOCK                          | not through incumbent_defense
  incumbent_defense_closed   | s2+s3+s4 direct chain                     | not through co_activation
  confidence_composite       | Stage 5 minus reductions                  | capped by INV B
  displacement_momentum_score| S2 delta + S3 delta + S4 delta            | not through confidence chain

---

## STAGE 0 — GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] CAMPAIGN OPEN fields filled (topic, date, status_quo_comparator)
  [ ] INCUMBENT ANCHOR filled (incumbent_name, strength, vulnerability)
  [ ] DISPLACEMENT MOMENTUM SCALE declared
  [ ] SESSION INVARIANTS TABLE complete — all four rows filled, SESSION INVARIANT D
      includes DELTA annotation in each stage template
  [ ] ROLE C executed — incumbent_threat_locked = true
  [ ] ROLE B executed — scout_artifact identified and scout_loaded confirmed
  [ ] ROLE A executed — invariant_registry_confirmed = true, displacement_scale_registered = true

STAGE 0 BODY:

  CLEARANCE TABLE:
  STEP | FIELD                        | OWNER   | REQUIRED | RESULT
  -----|------------------------------|---------|----------|--------
  1    | incumbent_threat_locked      | ROLE C  | true     | [confirm or BLOCKED]
  2    | gate_s_cleared               | ROLE B  | true     | [confirm or BLOCKED]
  3    | invariant_registry_confirmed | ROLE A  | true     | [confirm or BLOCKED]
  4    | displacement_scale_registered| ROLE A  | true     | [confirm or BLOCKED]

  First BLOCKED step halts campaign. Record step and owning role.

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open — Steps 1-4 confirmed. SESSION INVARIANT D (with DELTA
   annotation) active. DISPLACEMENT MOMENTUM SCALE active. Advancing to Stage 1."

---

## STAGE 1 — HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] STAGE 0 EXIT SIGNAL received: gate_open
  [ ] scout_artifact path available from ROLE B
  [ ] SESSION INVARIANT D templates registered (including DELTA annotation)

STAGE 1 BODY:
Load scout artifact. Read signals. Frame hypothesis.

  source_scout_artifact:        [path from ROLE B — copied, not inferred]
  hypothesis:                   [falsifiable claim about {topic}]
  counter_hypothesis:           [incumbent's best defense — grounded in ROLE C analysis]
  confidence_prior:             [initial confidence score: 1-10]
  displacement_momentum:        0  [initializes at zero before evidence stages]
  gate_s_cleared:               [true — from ROLE B]
  invariant_registry_confirmed: [true — from ROLE A]
  incumbent_threat_locked:      [true — from ROLE C]

Write artifact: {topic}-hypothesis-{date}.md. Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked(confidence_prior=[value])
  "STAGE 1 EXIT: hypothesis_locked — {topic}-hypothesis-{date}.md written.
   confidence_prior=[value]. displacement_momentum=0. Stage 2 ready."

---

## STAGE 2 — WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] STAGE 1 EXIT SIGNAL received: hypothesis_locked(confidence_prior=[value])
  [ ] hypothesis artifact confirmed written
  [ ] SESSION INVARIANT D Stage 2 template active (includes DELTA annotation)

STAGE 2 BODY:
Gather minimum 3 external sources.

INCUMBENT CHECK TABLE — Stage 2 (SESSION INVARIANT D, Stage 2 template with DELTA applied):
Structural origin: ROLE C `incumbent_threat_locked`.

  ITEM | SOURCE (URL or citation) | SUMMARY (1 sentence) | TEMPLATE APPLIED & VERDICT | DELTA
  -----|--------------------------|----------------------|-----------------------------|---------
  1    | [source]                 | [summary]            | "Does [item 1] support      | [+2/+1/0/-1/-2]
  2    | [source]                 | [summary]            |  displacement of [comparator]| [value]
  3    | [source]                 | [summary]            |  by [topic] on [dim]? [v]"  | [value]

  s2_incumbent_check_summary: [N support / M counter / P inconclusive]
  s2_displacement_delta:      [sum of DELTA column across all S2 items]
  s2_ce_verdict:              [null if no CE; cite item if found]
  displacement_momentum:      [0 + s2_displacement_delta]

Running null tally: "Running tally: [N] null across 1 stage complete. 2 stages remain."
SCHEMA INTEGRITY: [N]/12 handoff fields populated.
Write artifact: {topic}-websearch-{date}.md. Confirm write.

STAGE 2 EXIT SIGNAL: websearch_complete(count=[null_tally], displacement_momentum=[value])
  "STAGE 2 EXIT: websearch_complete — s2_ce_verdict = [value].
   s2_displacement_delta = [value]. displacement_momentum = [value]. Stage 3 ready."

---

## STAGE 3 — INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT SIGNAL received: websearch_complete(count=[N], displacement_momentum=[value])
  [ ] s2_ce_verdict recorded (null or value — not blank)
  [ ] SESSION INVARIANT D Stage 3 template active (includes DELTA annotation)

STAGE 3 BODY:
Simulate 2-3 practitioner interviews.

INCUMBENT CHECK TABLE — Stage 3 (SESSION INVARIANT D, Stage 3 template with DELTA applied):

  PRACTITIONER     | KEY ACCOUNT (1 sentence)     | TEMPLATE APPLIED & VERDICT            | DELTA
  -----------------|------------------------------|---------------------------------------|-------
  [type 1]         | [quote or paraphrase]        | "Does [account 1] reveal a viable     | [value]
  [type 2]         | [quote or paraphrase]        |  transition path from [comparator]    | [value]
  [type 3]         | [quote or paraphrase]        |  to [topic] for [use case]? [verdict]"| [value]

  s3_incumbent_check_summary: [N support / M counter / P inconclusive]
  s3_displacement_delta:      [sum of DELTA column across all S3 items]
  s3_ce_verdict:              [null if no CE; cite account if found]
  displacement_momentum:      [prev_momentum + s3_displacement_delta]

Running null tally: "Running tally: [N] null across 2 stages complete. 1 stage remains."
Write artifact: {topic}-interview-{date}.md. Confirm write.

STAGE 3 EXIT SIGNAL: interview_complete(count=[null_tally], displacement_momentum=[value])
  "STAGE 3 EXIT: interview_complete — s3_ce_verdict = [value].
   s3_displacement_delta = [value]. displacement_momentum = [value]. Stage 4 ready."

---

## STAGE 4 — PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT SIGNAL received: interview_complete(count=[N], displacement_momentum=[value])
  [ ] s3_ce_verdict recorded (null or value — not blank)
  [ ] SESSION INVARIANT D Stage 4 template active (includes DELTA annotation)

STAGE 4 BODY:
Design and assess minimal prototype.

  prototype_design:   [brief description]
  prototype_result:   [what was learned — 1-3 sentences]

INCUMBENT CHECK TABLE — Stage 4 (SESSION INVARIANT D, Stage 4 template with DELTA applied):

  ITEM       | PROTOTYPE RESULT (1 sentence) | TEMPLATE APPLIED & VERDICT                | DELTA
  -----------|-------------------------------|-------------------------------------------|-------
  prototype  | [prototype_result]            | "Does [prototype result] make a credible  | [value]
             |                               |  case for displacing [comparator] with    |
             |                               |  [topic]? [Yes / No / Pending]"           |

  s4_displacement_verdict:   [Yes / No / Pending]
  s4_displacement_delta:     [DELTA value from table above]
  s4_ce_verdict:             [null if no CE; description if found]
  displacement_momentum:     [prev_momentum + s4_displacement_delta]

Momentum trajectory:
  s2_delta=[value], s3_delta=[value], s4_delta=[value]
  trajectory: [ACCELERATING / STABLE / DECELERATING]
  (ACCELERATING = each delta >= prior; DECELERATING = each delta <= prior)

Final null tally:
  null_tally_final = [N]
  Cross-check: "Running count from Stage 3 was [M]. Final is [N]. Match: [true/false]."

Write artifact: {topic}-prototype-{date}.md. Confirm write.

STAGE 4 EXIT SIGNAL: prototype_complete(count=[null_tally_final], displacement_momentum=[value])
  "STAGE 4 EXIT: prototype_complete — s4_ce_verdict = [value]. null_tally_final = [N].
   displacement_momentum = [value]. trajectory = [value]. Stage 5 ready."

---

## STAGE 5 — SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT SIGNAL received: prototype_complete(count=[N], displacement_momentum=[value])
  [ ] null_tally_final recorded
  [ ] counter_hypothesis from Stage 1 present for resolution
  [ ] All four SESSION INVARIANT TABLE rows active
  [ ] DISPLACEMENT MOMENTUM SCALE active for BLOCK 3

STAGE 5 BODY: THREE-BLOCK STRUCTURE
SYNTHESIS HARD GATE: no synthesis fields until BLOCK 3 COMPLETE signal received.

### BLOCK 1: CONFIDENCE CHAIN RESOLUTION

  chain_equation:       [confidence_prior] +/- [delta_s2] +/- [delta_s3] +/- [delta_s4] = [raw]
  null_cap_applied:     [yes: raw -= 2 if null_tally_final >= 3; no otherwise]
  confidence_resolved:  [raw after null cap]

BLOCK 1 COMPLETE signal: "BLOCK 1 COMPLETE — confidence_resolved = [value]."

### BLOCK 2: COUNTER-HYPOTHESIS RESOLUTION

  COUNTER_HYPOTHESIS     | VERDICT                                  | EVIDENCE
  -----------------------|------------------------------------------|-------------------
  [from Stage 1]         | REFUTED / PARTIALLY REFUTED / OPEN RISK  | [cite artifact]

OPEN RISK items reduce confidence_resolved by 1 tier each.
  confidence_post_cr:    [confidence_resolved - open_risk_count]

BLOCK 2 COMPLETE signal: "BLOCK 2 COMPLETE — confidence_post_cr = [value]."

### BLOCK 3: DISPLACEMENT INTEGRITY CHECK

Dependency: requires BLOCK 1 COMPLETE and BLOCK 2 COMPLETE.

Momentum reconstruction:
  s2_displacement_delta = [value]  trajectory_s2_to_s3: [improving/stable/declining]
  s3_displacement_delta = [value]  trajectory_s3_to_s4: [improving/stable/declining]
  s4_displacement_delta = [value]
  displacement_momentum_final = s2 + s3 + s4 = [total]
  overall_trajectory = [ACCELERATING / STABLE / DECELERATING]

ATOMIC DUAL-LOCK:
  S2 -> [s2_ce_verdict], S3 -> [s3_ce_verdict], S4 -> [s4_ce_verdict]
  null_tally_final = [N]
  Cross-check vs Stage 4 exit: [Match / Mismatch]

If null_tally_final >= 3:
  Lock 1 (INV A): adversarial review by [adversarial_reviewer_type]. BLOCKED.
  Lock 2 (INV B): confidence_composite -= 2.
  co_activation_confirmed: dual_lock_fired
Else:
  co_activation_confirmed: not_triggered

displacement_conclusion:       [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
displacement_conclusion_basis: [anchored in displacement_momentum_final and trajectory]
  Note: DECELERATING trajectory with positive final score warrants PARTIALLY SUPPORTED
  even if final score is positive — momentum matters.

BLOCK 3 COMPLETE signal: "BLOCK 3 COMPLETE — displacement_momentum_final = [value].
  trajectory = [value]. displacement_conclusion = [value]."

### SYNTHESIS BODY

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:      [2-3 sentences — include displacement_momentum trajectory]
  confidence_composite:  [confidence_post_cr after any dual-lock reduction]
  key_risk:              [residual incumbent strength; note if momentum was DECELERATING]

### HANDOFF TABLE

SESSION INVARIANT C enforced. All fields carry [derived from: X].

  FIELD                      | VALUE   | DERIVATION                                | IND. CHAIN
  ---------------------------|---------|-------------------------------------------|------------------
  scout_anchor               | [value] | [derived from: ROLE B scout load]         | n/a
  incumbent_threat_locked    | [true]  | [derived from: ROLE C analysis]           | n/a
  hypothesis                 | [value] | [derived from: Stage 1 artifact]          | n/a
  counter_hypothesis         | [value] | [derived from: Stage 1 artifact]          | n/a
  s2_ce_verdict              | [value] | [derived from: Stage 2 artifact]          | n/a
  s3_ce_verdict              | [value] | [derived from: Stage 3 artifact]          | n/a
  s4_ce_verdict              | [value] | [derived from: Stage 4 artifact]          | n/a
  null_tally_final           | [N]     | [derived from: s2+s3+s4 CE verdicts]      | does not pass through co_activation
  co_activation_confirmed    | [value] | [derived from: ATOMIC DUAL-LOCK]          | does not pass through incumbent_defense
  incumbent_defense_closed   | [t/f]   | [derived from: s2+s3+s4 direct]          | does not pass through co_activation
  confidence_composite       | [value] | [derived from: Stage 5 Block 2+3]         | capped by INV B
  displacement_momentum_score| [value] | [derived from: S2+S3+S4 deltas]          | not through confidence chain
  schema_compliance_confirmed| [true]  | [all 12 fields match]                    | n/a

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete — Evidence brief ready for topic-story."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## V-03 — Block 3 Multi-Stage Chain

**Axis**: block3_multi_stage_chain (single)
**Hypothesis**: C-16 defines BLOCK 3 as DISPLACEMENT INTEGRITY CHECK. The current R17 V-05
baseline implements this as a single cross-check: Stage 4 aggregate verdict vs Stage 5
displacement_conclusion. This is a two-point integrity check. A three-stage displacement
chain (S2 incumbent checks, S3 incumbent checks, S4 verdict — each independently compared
to the final displacement_conclusion) would reveal structural inconsistencies that a
two-point check misses: for example, a case where S2 and S3 both support displacement
but S4 does not, yet the conclusion reads SUPPORTED. The per-stage comparison table in
BLOCK 3 makes the chain reconstruction complete.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

depth: standard
confidence: standard
for: {value}
iterations: 1

Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
The campaign builds the case for displacing {status_quo_comparator} with {topic}.
Six stages (Stage 0 = gate, Stages 1-5 = evidence + synthesis). Each stage has numbered
ENTRY CONDITIONS and a named EXIT SIGNAL. No stage body begins until entry conditions confirm.

---

## CAMPAIGN OPEN

  topic:                 {topic}
  date:                  {date}
  status_quo_comparator: [name the incumbent approach this topic must displace]

### INCUMBENT ANCHOR

Fill before any role or invariant registration.

  incumbent_name:          [full name of status_quo_comparator]
  incumbent_strength:      [one sentence: why the incumbent is currently winning]
  incumbent_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]

### SESSION INVARIANTS TABLE

SESSION INVARIANT D leads. All invariants carry: "cannot be modified or bypassed at
any subsequent stage." Register all four before roles execute.

  ID   | NAME                      | DECLARATION
  -----|---------------------------|------------------------------------------------------
  D    | INCUMBENT CHECK PHRASING  | Stage 2: "Does [evidence item] support the displacement
       | REGISTER                  |   of {status_quo_comparator} by {topic} on [dimension]?
       |                           |   [Yes / No / Inconclusive]"
       |                           | Stage 3: "Does [practitioner account] reveal a viable
       |                           |   transition path from {status_quo_comparator} to
       |                           |   {topic} for [use case]? [Yes / No / Inconclusive]"
       |                           | Stage 4: "Does [prototype result] make a credible case
       |                           |   for displacing {status_quo_comparator} with {topic}?
       |                           |   [Yes / No / Pending]"
       |                           | Enforcement: Template deviation = format error.
  -----|---------------------------|------------------------------------------------------
  A    | ADVERSARIAL REVIEWER      | adversarial_reviewer_type: [role most likely to
       | TYPE                      |   challenge the displacement claim].
       |                           | Activation: null_tally_final >= 3.
  -----|---------------------------|------------------------------------------------------
  B    | CONFIDENCE CAP            | null_ce_cap_rule: confidence_composite -= 2 if
       |                           |   null_tally_final >= 3 (hard cap).
  -----|---------------------------|------------------------------------------------------
  C    | DERIVATION ANNOTATION     | annotation_rule: Every handoff field carries
       |                           |   [derived from: X]. Unlabeled = format error.

### ROLE OWNERSHIP TABLE

ROLE C executes first. Roles run in sequence C -> B -> A before Stage 0 begins.

  ROLE   | TITLE                    | OWNED FIELD               | GATE S STEP | EXECUTE
  -------|--------------------------|---------------------------|-------------|--------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked   | Step 1      | FIRST
  ROLE B | SCOUT LOADER             | gate_s_cleared            | Step 2      | SECOND
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | Step 3   | THIRD

ROLE C execution (fill now):
  incumbent_threat_locked: [true when INCUMBENT ANCHOR complete]
  s2_displacement_signal: [anticipated verdict direction at Stage 2 given incumbent_vulnerability]
  s3_displacement_signal: [anticipated verdict direction at Stage 3 given incumbent_vulnerability]
  s4_displacement_signal: [anticipated verdict direction at Stage 4 given incumbent_vulnerability]

ROLE B execution (fill now):
  scout_artifact:  [{topic}-scout-record-{date}.md or equivalent]
  scout_loaded:    [true / false]
  gate_s_cleared:  [true if scout_loaded; CAMPAIGN BLOCKED otherwise]

ROLE A execution (fill now):
  invariant_registry_confirmed: [true when all four invariants registered]

### CE VERDICT OWNERSHIP TABLE

  FIELD            | OWNED BY      | FORMULA
  -----------------|---------------|-----------------------------------------------------
  s2_ce_verdict    | Stage 2       | null if no CE; citation if CE found
  s3_ce_verdict    | Stage 3       | null if no CE; citation if CE found
  s4_ce_verdict    | Stage 4       | null if no CE; description if CE found
  null_tally_final | Stage 4 close | count(null) across s2 + s3 + s4

NULL TALLY CHAIN RULE (locked): Running tally from Stage 2. Stage 4 close reconstructs
full chain. ATOMIC DUAL-LOCK cross-checks at synthesis. Mismatch = integrity failure.

### PRE-COMMITTED HANDOFF SCHEMA TABLE

  FIELD                      | DERIVATION SOURCE                         | IND. CHAIN
  ---------------------------|-------------------------------------------|------------------
  scout_anchor               | ROLE B scout load                         | n/a
  incumbent_threat_locked    | ROLE C analysis                           | n/a
  hypothesis                 | Stage 1 artifact                          | n/a
  counter_hypothesis         | Stage 1 artifact                          | n/a
  s2_ce_verdict              | Stage 2 artifact                          | n/a
  s3_ce_verdict              | Stage 3 artifact                          | n/a
  s4_ce_verdict              | Stage 4 artifact                          | n/a
  null_tally_final           | s2+s3+s4 CE verdicts                      | not through co_activation
  co_activation_confirmed    | ATOMIC DUAL-LOCK                          | not through incumbent_defense
  incumbent_defense_closed   | s2+s3+s4 direct chain                     | not through co_activation
  confidence_composite       | Stage 5 minus reductions                  | capped by INV B

---

## STAGE 0 — GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] CAMPAIGN OPEN fields filled
  [ ] INCUMBENT ANCHOR filled (all three fields)
  [ ] SESSION INVARIANTS TABLE complete
  [ ] ROLE C executed — incumbent_threat_locked = true, s2/s3/s4 displacement signals recorded
  [ ] ROLE B executed — gate_s_cleared = true
  [ ] ROLE A executed — invariant_registry_confirmed = true

STAGE 0 BODY:

  CLEARANCE TABLE:
  STEP | FIELD                        | OWNER   | REQUIRED | RESULT
  -----|------------------------------|---------|----------|--------
  1    | incumbent_threat_locked      | ROLE C  | true     | [confirm or BLOCKED]
  2    | gate_s_cleared               | ROLE B  | true     | [confirm or BLOCKED]
  3    | invariant_registry_confirmed | ROLE A  | true     | [confirm or BLOCKED]
  4    | displacement_signals_anchored| ROLE C  | s2/s3/s4 all filled | [confirm or BLOCKED]

  First BLOCKED step halts campaign.

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open — Steps 1-4 confirmed. Displacement signal anchors active.
   Advancing to Stage 1."

---

## STAGE 1 — HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] STAGE 0 EXIT SIGNAL received: gate_open
  [ ] scout_artifact path available from ROLE B
  [ ] SESSION INVARIANT D templates registered

STAGE 1 BODY:
Load scout artifact. Read signals. Frame hypothesis.

  source_scout_artifact:        [path from ROLE B]
  hypothesis:                   [falsifiable claim about {topic}]
  counter_hypothesis:           [incumbent's best defense — grounded in ROLE C analysis]
  confidence_prior:             [initial confidence score: 1-10]
  incumbent_threat_locked:      [true]
  gate_s_cleared:               [true]
  invariant_registry_confirmed: [true]

Write artifact: {topic}-hypothesis-{date}.md. Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked(confidence_prior=[value])
  "STAGE 1 EXIT: hypothesis_locked — {topic}-hypothesis-{date}.md written.
   confidence_prior=[value]. Stage 2 ready."

---

## STAGE 2 — WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] STAGE 1 EXIT SIGNAL received: hypothesis_locked(confidence_prior=[value])
  [ ] Read {topic}-hypothesis-{date}.md from disk: extract confidence_prior_disk
  [ ] Validate: confidence_prior from signal == confidence_prior_disk — mismatch = INTEGRITY FAILURE
  [ ] SESSION INVARIANT D Stage 2 template active

STAGE 2 BODY:
Gather minimum 3 external sources.

INCUMBENT CHECK TABLE — Stage 2 (SESSION INVARIANT D, Stage 2 template verbatim):

  ITEM | SOURCE | SUMMARY (1 sentence) | TEMPLATE APPLIED & VERDICT
  -----|--------|----------------------|------------------------------
  1    | [url]  | [summary]            | "Does [item 1] support displacement? [verdict]"
  2    | [url]  | [summary]            | "Does [item 2] support displacement? [verdict]"
  3    | [url]  | [summary]            | "Does [item 3] support displacement? [verdict]"

  s2_aggregate_verdict:   [SUPPORTS / MIXED / COUNTERS — aggregate of above]
  s2_incumbent_check_summary: [N support / M counter / P inconclusive]
  s2_ce_verdict:          [null if no CE; cite item if found]
  confidence_delta_s2:    [+1 / 0 / -1]
  running_confidence:     [confidence_prior + confidence_delta_s2]

Running null tally: "Running tally: [N] null. 2 stages remain."
Write artifact: {topic}-websearch-{date}.md. Confirm write.

STAGE 2 EXIT SIGNAL: websearch_complete(count=[N], running_confidence=[value])
  "STAGE 2 EXIT: websearch_complete — s2_ce_verdict=[value]. s2_aggregate_verdict=[value].
   running_confidence=[value]. Stage 3 ready."

---

## STAGE 3 — INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT SIGNAL received: websearch_complete(count=[N], running_confidence=[value])
  [ ] Read {topic}-websearch-{date}.md from disk: extract running_confidence_disk
  [ ] Validate: running_confidence from signal == running_confidence_disk — mismatch = INTEGRITY FAILURE
  [ ] s2_ce_verdict recorded
  [ ] SESSION INVARIANT D Stage 3 template active

STAGE 3 BODY:
Simulate 2-3 practitioner interviews.

INCUMBENT CHECK TABLE — Stage 3:

  PRACTITIONER | KEY ACCOUNT (1 sentence) | TEMPLATE APPLIED & VERDICT
  -------------|--------------------------|------------------------------
  [type 1]     | [account]               | "Does [account] reveal viable transition? [verdict]"
  [type 2]     | [account]               | "Does [account] reveal viable transition? [verdict]"
  [type 3]     | [account]               | "Does [account] reveal viable transition? [verdict]"

  s3_aggregate_verdict:   [SUPPORTS / MIXED / COUNTERS]
  s3_ce_verdict:          [null if no CE; cite account if found]
  confidence_delta_s3:    [+1 / 0 / -1]
  running_confidence:     [prev + confidence_delta_s3]

Running null tally: "Running tally: [N] null. 1 stage remains."
Write artifact: {topic}-interview-{date}.md. Confirm write.

STAGE 3 EXIT SIGNAL: interview_complete(count=[N], running_confidence=[value])
  "STAGE 3 EXIT: interview_complete — s3_ce_verdict=[value]. s3_aggregate_verdict=[value].
   running_confidence=[value]. Stage 4 ready."

---

## STAGE 4 — PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT SIGNAL received: interview_complete(count=[N], running_confidence=[value])
  [ ] Read {topic}-interview-{date}.md from disk: extract running_confidence_disk
  [ ] Validate: running_confidence from signal == running_confidence_disk — mismatch = INTEGRITY FAILURE
  [ ] s3_ce_verdict recorded
  [ ] SESSION INVARIANT D Stage 4 template active

STAGE 4 BODY:

  prototype_design:   [brief description]
  prototype_result:   [what was learned — 1-3 sentences]

INCUMBENT CHECK TABLE — Stage 4:

  ITEM       | PROTOTYPE RESULT | TEMPLATE APPLIED & VERDICT
  -----------|------------------|------------------------------
  prototype  | [result]         | "Does [result] make credible case for displacement? [verdict]"

  s4_displacement_verdict: [Yes / No / Pending]
  s4_aggregate_verdict:    [SUPPORTS / MIXED / COUNTERS — consistent with s4_displacement_verdict]
  s4_ce_verdict:           [null if no CE; description if found]
  confidence_delta_s4:     [+1 / 0 / -1]
  running_confidence:      [prev + confidence_delta_s4]

Final null tally:
  null_tally_final = [N]
  Cross-check: "Stage 3 count was [M]. Final is [N]. Match: [true/false]."

Write artifact: {topic}-prototype-{date}.md. Confirm write.

STAGE 4 EXIT SIGNAL: prototype_complete(count=[null_tally_final], running_confidence=[value])
  "STAGE 4 EXIT: prototype_complete — s4_ce_verdict=[value]. s4_aggregate_verdict=[value].
   null_tally_final=[N]. running_confidence=[value]. Stage 5 ready."

---

## STAGE 5 — SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT SIGNAL received: prototype_complete(count=[N], running_confidence=[value])
  [ ] Read {topic}-prototype-{date}.md from disk: extract running_confidence_disk, null_tally_final_disk
  [ ] Validate both values from signal == disk — mismatch = INTEGRITY FAILURE
  [ ] counter_hypothesis from Stage 1 present
  [ ] s2_aggregate_verdict, s3_aggregate_verdict, s4_aggregate_verdict all recorded

STAGE 5 BODY: THREE-BLOCK STRUCTURE
SYNTHESIS HARD GATE: no synthesis fields until BLOCK 3 COMPLETE signal received.

### BLOCK 1: CONFIDENCE CHAIN RESOLUTION

  chain_equation:       [confidence_prior] +/- [delta_s2] +/- [delta_s3] +/- [delta_s4] = [raw]
  null_cap_applied:     [yes: raw -= 2 if null_tally_final >= 3; no otherwise]
  confidence_resolved:  [final]

BLOCK 1 COMPLETE signal: "BLOCK 1 COMPLETE — confidence_resolved = [value]."

### BLOCK 2: COUNTER-HYPOTHESIS RESOLUTION

  COUNTER_HYPOTHESIS     | VERDICT                                  | EVIDENCE
  -----------------------|------------------------------------------|-------------------
  [from Stage 1]         | REFUTED / PARTIALLY REFUTED / OPEN RISK  | [cite artifact]

  open_risk_count:    [N]
  confidence_post_cr: [confidence_resolved - open_risk_count]

BLOCK 2 COMPLETE signal: "BLOCK 2 COMPLETE — confidence_post_cr = [value]."

### BLOCK 3: DISPLACEMENT INTEGRITY CHECK

Dependency: requires BLOCK 1 COMPLETE and BLOCK 2 COMPLETE before this block begins.

THREE-STAGE DISPLACEMENT CHAIN:
Reconstructs the displacement evidence trajectory from each evidence stage individually.
Compares each stage's aggregate verdict to the final displacement_conclusion.

  STAGE | AGGREGATE VERDICT   | EXPECTED CONCLUSION DIRECTION | CONSISTENT?
  ------|---------------------|-------------------------------|-------------
  S2    | [s2_aggregate_verdict] | [SUPPORTED / PARTIALLY / UNSUPPORTED] | [YES / NO / FLAG]
  S3    | [s3_aggregate_verdict] | [SUPPORTED / PARTIALLY / UNSUPPORTED] | [YES / NO / FLAG]
  S4    | [s4_aggregate_verdict] | [SUPPORTED / PARTIALLY / UNSUPPORTED] | [YES / NO / FLAG]

  consistency_flags:    [count of FLAG entries — 0 = fully consistent chain]
  chain_pattern:        [e.g., "S2 SUPPORTED, S3 MIXED, S4 SUPPORTED = improving arc"]
  displacement_conclusion: [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  conclusion_justification: [must reconcile any FLAG entries — each FLAG requires explicit rationale]

ATOMIC DUAL-LOCK:
  S2 -> [s2_ce_verdict], S3 -> [s3_ce_verdict], S4 -> [s4_ce_verdict]
  null_tally_final = [N]
  Cross-check vs Stage 4: [Match / Mismatch]

If null_tally_final >= 3:
  Lock 1: adversarial review by [adversarial_reviewer_type]. BLOCKED.
  Lock 2: confidence_composite -= 2.
  co_activation_confirmed: dual_lock_fired
Else:
  co_activation_confirmed: not_triggered

BLOCK 3 COMPLETE signal: "BLOCK 3 COMPLETE — displacement_conclusion = [value].
  consistency_flags = [N]. chain_pattern = [value]."

### SYNTHESIS BODY

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:      [2-3 sentences — reference chain_pattern and any consistency flags]
  confidence_composite:  [confidence_post_cr after dual-lock if triggered]
  key_risk:              [residual incumbent strength; reference any FLAG entries in displacement chain]

### HANDOFF TABLE

SESSION INVARIANT C enforced.

  FIELD                      | VALUE   | DERIVATION                          | IND. CHAIN
  ---------------------------|---------|-------------------------------------|------------------
  scout_anchor               | [value] | [derived from: ROLE B scout load]   | n/a
  incumbent_threat_locked    | [true]  | [derived from: ROLE C analysis]     | n/a
  hypothesis                 | [value] | [derived from: Stage 1 artifact]    | n/a
  counter_hypothesis         | [value] | [derived from: Stage 1 artifact]    | n/a
  s2_ce_verdict              | [value] | [derived from: Stage 2 artifact]    | n/a
  s3_ce_verdict              | [value] | [derived from: Stage 3 artifact]    | n/a
  s4_ce_verdict              | [value] | [derived from: Stage 4 artifact]    | n/a
  null_tally_final           | [N]     | [derived from: s2+s3+s4 CE verdicts]| does not pass through co_activation
  co_activation_confirmed    | [value] | [derived from: ATOMIC DUAL-LOCK]    | does not pass through incumbent_defense
  incumbent_defense_closed   | [t/f]   | [derived from: s2+s3+s4 direct]     | does not pass through co_activation
  confidence_composite       | [value] | [derived from: Stage 5 synthesis]   | capped by INV B
  schema_compliance_confirmed| [true]  | [all 11 fields, chain verified]     | n/a

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete — Evidence brief ready for topic-story."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## V-04 — Role Dependency Annotation + Block 3 Multi-Stage Chain

**Axes**: role_dependency_annotation + block3_multi_stage_chain (combined)
**Hypothesis**: V-01 and V-03 each address a different part of the same auditability gap.
V-01 makes the pre-stage role execution order auditable through DEPENDS ON declarations.
V-03 makes the Stage 5 displacement conclusion auditable through per-stage chain
reconstruction. Together they form a complete dependency-audit stack: the dependency
audit begins at role execution (C-17 declared, not emergent) and ends at displacement
conclusion (C-16 BLOCK 3 reconstructs the full chain). Any tampering between pre-stage
and synthesis is detectable at two checkpoints.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

depth: standard
confidence: standard
for: {value}
iterations: 1

Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
The campaign builds the case for displacing {status_quo_comparator} with {topic}.
Six stages (Stage 0 = gate, Stages 1-5 = evidence + synthesis). Each stage has numbered
ENTRY CONDITIONS and a named EXIT SIGNAL. No stage body begins until entry conditions confirm.

---

## CAMPAIGN OPEN

  topic:                 {topic}
  date:                  {date}
  status_quo_comparator: [name the incumbent approach this topic must displace]

### INCUMBENT ANCHOR

  incumbent_name:          [full name of status_quo_comparator]
  incumbent_strength:      [one sentence: why the incumbent is currently winning]
  incumbent_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]

### SESSION INVARIANTS TABLE

  ID   | NAME                      | DECLARATION
  -----|---------------------------|------------------------------------------------------
  D    | INCUMBENT CHECK PHRASING  | Stage 2: "Does [evidence item] support the displacement
       | REGISTER                  |   of {status_quo_comparator} by {topic} on [dimension]?
       |                           |   [Yes / No / Inconclusive]"
       |                           | Stage 3: "Does [practitioner account] reveal a viable
       |                           |   transition path from {status_quo_comparator} to
       |                           |   {topic} for [use case]? [Yes / No / Inconclusive]"
       |                           | Stage 4: "Does [prototype result] make a credible case
       |                           |   for displacing {status_quo_comparator} with {topic}?
       |                           |   [Yes / No / Pending]"
       |                           | Template deviation = format error.
  -----|---------------------------|------------------------------------------------------
  A    | ADVERSARIAL REVIEWER      | adversarial_reviewer_type: [challenger role].
       | TYPE                      | Activation: null_tally_final >= 3.
  -----|---------------------------|------------------------------------------------------
  B    | CONFIDENCE CAP            | null_ce_cap_rule: confidence_composite -= 2 if
       |                           |   null_tally_final >= 3 (hard cap).
  -----|---------------------------|------------------------------------------------------
  C    | DERIVATION ANNOTATION     | Every handoff field carries [derived from: X].

### ROLE OWNERSHIP TABLE

DEPENDENCY DECLARATIONS: DEPENDS ON column specifies required fields by owning role.
When Role M depends on a field owned by Role N declared after M, execution inverts to
N-before-M. Declared order is preserved; execution order adapts.

  ROLE   | TITLE                    | OWNED FIELD                  | DEPENDS ON                            | EXECUTE
  -------|--------------------------|------------------------------|---------------------------------------|--------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked      | (none)                                | FIRST
  ROLE B | SCOUT LOADER             | gate_s_cleared               | (none)                                | SECOND
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | incumbent_threat_locked (C), gate_s_cleared (B) | THIRD (C and B precede by declaration — no inversion)

DEPENDENCY INVERSION RULE: Any role whose DEPENDS ON references a later-declared role
triggers execution inversion. EXECUTE column reflects post-inversion order.

ROLE C execution (fill now):
  incumbent_threat_locked: [true when INCUMBENT ANCHOR complete]
  s2_displacement_signal: [anticipated verdict direction at S2]
  s3_displacement_signal: [anticipated verdict direction at S3]
  s4_displacement_signal: [anticipated verdict direction at S4]
  dependency_satisfied_by: n/a

ROLE B execution (fill now):
  scout_artifact:  [{topic}-scout-record-{date}.md or equivalent]
  scout_loaded:    [true / false]
  gate_s_cleared:  [true if scout_loaded; BLOCKED otherwise]
  dependency_satisfied_by: n/a

ROLE A execution (fill now):
  invariant_registry_confirmed: [true when all four invariants registered]
  dependency_satisfied_by: [incumbent_threat_locked from ROLE C — confirmed;
                             gate_s_cleared from ROLE B — confirmed]

### CE VERDICT OWNERSHIP TABLE

  FIELD            | OWNED BY      | FORMULA
  -----------------|---------------|-----------------------------------------------------
  s2_ce_verdict    | Stage 2       | null if no CE; citation if CE found
  s3_ce_verdict    | Stage 3       | null if no CE; citation if CE found
  s4_ce_verdict    | Stage 4       | null if no CE; description if CE found
  null_tally_final | Stage 4 close | count(null) across s2 + s3 + s4

### PRE-COMMITTED HANDOFF SCHEMA TABLE

  FIELD                      | DERIVATION SOURCE                         | IND. CHAIN
  ---------------------------|-------------------------------------------|------------------
  scout_anchor               | ROLE B scout load                         | n/a
  incumbent_threat_locked    | ROLE C analysis                           | n/a
  hypothesis                 | Stage 1 artifact                          | n/a
  counter_hypothesis         | Stage 1 artifact                          | n/a
  s2_ce_verdict              | Stage 2 artifact                          | n/a
  s3_ce_verdict              | Stage 3 artifact                          | n/a
  s4_ce_verdict              | Stage 4 artifact                          | n/a
  null_tally_final           | s2+s3+s4 CE verdicts                      | not through co_activation
  co_activation_confirmed    | ATOMIC DUAL-LOCK                          | not through incumbent_defense
  incumbent_defense_closed   | s2+s3+s4 direct chain                     | not through co_activation
  confidence_composite       | Stage 5 minus reductions                  | capped by INV B

---

## STAGE 0 — GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] CAMPAIGN OPEN fields filled
  [ ] INCUMBENT ANCHOR filled
  [ ] SESSION INVARIANTS TABLE complete
  [ ] ROLE OWNERSHIP TABLE DEPENDS ON column complete for all roles
  [ ] ROLE C executed — incumbent_threat_locked = true, displacement signals recorded
  [ ] ROLE B executed — gate_s_cleared = true
  [ ] ROLE A executed — invariant_registry_confirmed = true, dependency_satisfied_by confirmed

STAGE 0 BODY:

  STEP | FIELD                        | OWNER   | REQUIRED | RESULT
  -----|------------------------------|---------|----------|--------
  1    | incumbent_threat_locked      | ROLE C  | true     | [confirm or BLOCKED]
  2    | gate_s_cleared               | ROLE B  | true     | [confirm or BLOCKED]
  3    | invariant_registry_confirmed | ROLE A  | true     | [confirm or BLOCKED]
  4    | dependency_declarations_complete | TABLE | all roles filled | [confirm or BLOCKED]
  5    | displacement_signals_anchored| ROLE C  | s2/s3/s4 filled  | [confirm or BLOCKED]

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open — Steps 1-5 confirmed. Dependencies auditable.
   Displacement signal anchors active. Advancing to Stage 1."

---

## STAGE 1 — HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] STAGE 0 EXIT SIGNAL received: gate_open
  [ ] scout_artifact path available from ROLE B
  [ ] Read scout_artifact from disk: extract scout_anchor_value
  [ ] SESSION INVARIANT D templates registered

STAGE 1 BODY:

  source_scout_artifact:        [path from ROLE B]
  scout_anchor_value:           [extracted from disk at path — not from memory]
  hypothesis:                   [falsifiable claim]
  counter_hypothesis:           [incumbent's best defense]
  confidence_prior:             [1-10]
  incumbent_threat_locked:      [true]
  gate_s_cleared:               [true]
  invariant_registry_confirmed: [true]

Write artifact: {topic}-hypothesis-{date}.md. Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked(confidence_prior=[value])
  "STAGE 1 EXIT: hypothesis_locked — confidence_prior=[value]. Stage 2 ready."

---

## STAGE 2 — WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] STAGE 1 EXIT SIGNAL received: hypothesis_locked(confidence_prior=[value])
  [ ] Read {topic}-hypothesis-{date}.md from disk: extract confidence_prior_disk
  [ ] Validate: signal confidence_prior == disk confidence_prior — mismatch = INTEGRITY FAILURE
  [ ] SESSION INVARIANT D Stage 2 template active

STAGE 2 BODY:

  ITEM | SOURCE | SUMMARY | TEMPLATE APPLIED & VERDICT
  -----|--------|---------|-----------------------------
  1    | [url]  | [text]  | "Does [item] support displacement? [verdict]"
  2    | [url]  | [text]  | "Does [item] support displacement? [verdict]"
  3    | [url]  | [text]  | "Does [item] support displacement? [verdict]"

  s2_aggregate_verdict:   [SUPPORTS / MIXED / COUNTERS]
  s2_ce_verdict:          [null or citation]
  confidence_delta_s2:    [+1/0/-1]
  running_confidence:     [confidence_prior + delta]

Running null tally: "[N] null. 2 stages remain."
Write artifact: {topic}-websearch-{date}.md. Confirm write.

STAGE 2 EXIT SIGNAL: websearch_complete(count=[N], running_confidence=[value])
  "STAGE 2 EXIT: s2_aggregate_verdict=[value]. running_confidence=[value]. Stage 3 ready."

---

## STAGE 3 — INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT SIGNAL received: websearch_complete(count=[N], running_confidence=[value])
  [ ] Read {topic}-websearch-{date}.md from disk: extract running_confidence_disk
  [ ] Validate: signal == disk — mismatch = INTEGRITY FAILURE
  [ ] SESSION INVARIANT D Stage 3 template active

STAGE 3 BODY:

  PRACTITIONER | ACCOUNT | TEMPLATE APPLIED & VERDICT
  -------------|---------|------------------------------
  [type 1]     | [text]  | "Does [account] reveal transition path? [verdict]"
  [type 2]     | [text]  | "Does [account] reveal transition path? [verdict]"
  [type 3]     | [text]  | "Does [account] reveal transition path? [verdict]"

  s3_aggregate_verdict:   [SUPPORTS / MIXED / COUNTERS]
  s3_ce_verdict:          [null or citation]
  confidence_delta_s3:    [+1/0/-1]
  running_confidence:     [prev + delta]

Running null tally: "[N] null. 1 stage remains."
Write artifact: {topic}-interview-{date}.md. Confirm write.

STAGE 3 EXIT SIGNAL: interview_complete(count=[N], running_confidence=[value])
  "STAGE 3 EXIT: s3_aggregate_verdict=[value]. running_confidence=[value]. Stage 4 ready."

---

## STAGE 4 — PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT SIGNAL received: interview_complete(count=[N], running_confidence=[value])
  [ ] Read {topic}-interview-{date}.md from disk: extract running_confidence_disk
  [ ] Validate: signal == disk — mismatch = INTEGRITY FAILURE
  [ ] SESSION INVARIANT D Stage 4 template active

STAGE 4 BODY:

  prototype_design:   [description]
  prototype_result:   [findings — 1-3 sentences]

  ITEM      | RESULT   | TEMPLATE APPLIED & VERDICT
  ----------|----------|-------------------------------------------------
  prototype | [result] | "Does result make credible case? [Yes/No/Pending]"

  s4_displacement_verdict: [Yes / No / Pending]
  s4_aggregate_verdict:    [SUPPORTS / MIXED / COUNTERS]
  s4_ce_verdict:           [null or description]
  confidence_delta_s4:     [+1/0/-1]
  running_confidence:      [prev + delta]

  null_tally_final = [N]
  Cross-check: "Stage 3 was [M]. Final [N]. Match: [true/false]."

Write artifact: {topic}-prototype-{date}.md. Confirm write.

STAGE 4 EXIT SIGNAL: prototype_complete(count=[null_tally_final], running_confidence=[value])
  "STAGE 4 EXIT: s4_aggregate_verdict=[value]. null_tally_final=[N].
   running_confidence=[value]. Stage 5 ready."

---

## STAGE 5 — SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT SIGNAL received: prototype_complete(count=[N], running_confidence=[value])
  [ ] Read {topic}-prototype-{date}.md from disk: extract running_confidence_disk, null_tally_disk
  [ ] Validate both: signal == disk — mismatch = INTEGRITY FAILURE
  [ ] counter_hypothesis from Stage 1 present
  [ ] s2/s3/s4 aggregate verdicts all recorded for BLOCK 3 chain reconstruction

STAGE 5 BODY: THREE-BLOCK STRUCTURE
SYNTHESIS HARD GATE: synthesis body may not execute until BLOCK 3 COMPLETE received.

### BLOCK 1: CONFIDENCE CHAIN RESOLUTION

  chain_equation:       [prior] + [ds2] + [ds3] + [ds4] = [raw]
  null_cap_applied:     [yes: raw -= 2 if null_tally_final >= 3; no otherwise]
  confidence_resolved:  [raw after cap]

BLOCK 1 COMPLETE: "BLOCK 1 COMPLETE — confidence_resolved = [value]."

### BLOCK 2: COUNTER-HYPOTHESIS RESOLUTION

  COUNTER_HYPOTHESIS | VERDICT                                  | EVIDENCE
  -------------------|------------------------------------------|-------------------
  [from Stage 1]     | REFUTED / PARTIALLY REFUTED / OPEN RISK  | [artifact citation]

  confidence_post_cr: [confidence_resolved - open_risk_count]

BLOCK 2 COMPLETE: "BLOCK 2 COMPLETE — confidence_post_cr = [value]."

### BLOCK 3: DISPLACEMENT INTEGRITY CHECK

Dependency: BLOCK 1 COMPLETE and BLOCK 2 COMPLETE both required before this block.

THREE-STAGE DISPLACEMENT CHAIN:

  STAGE | AGGREGATE VERDICT      | CONCLUSION DIRECTION          | CONSISTENT?
  ------|------------------------|-------------------------------|-------------
  S2    | [s2_aggregate_verdict] | [expected conclusion]         | [YES/NO/FLAG]
  S3    | [s3_aggregate_verdict] | [expected conclusion]         | [YES/NO/FLAG]
  S4    | [s4_aggregate_verdict] | [expected conclusion]         | [YES/NO/FLAG]

  consistency_flags: [count]
  chain_pattern:     [describe trajectory: e.g., "S2 SUPPORTS, S3 MIXED, S4 SUPPORTS"]
  displacement_conclusion: [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  flag_rationale:    [required for each FLAG — why conclusion diverges from stage verdict]

ATOMIC DUAL-LOCK:
  S2 -> [s2_ce_verdict], S3 -> [s3_ce_verdict], S4 -> [s4_ce_verdict]
  null_tally_final = [N]
  Cross-check vs Stage 4 exit: [Match / Mismatch]

If null_tally_final >= 3:
  Lock 1 (INV A): adversarial review required. BLOCKED.
  Lock 2 (INV B): confidence_composite -= 2.
  co_activation_confirmed: dual_lock_fired
Else:
  co_activation_confirmed: not_triggered

BLOCK 3 COMPLETE: "BLOCK 3 COMPLETE — displacement_conclusion = [value].
  consistency_flags = [N]. chain_pattern = [value]."

### SYNTHESIS BODY

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:      [2-3 sentences — reference chain_pattern and flags]
  confidence_composite:  [confidence_post_cr minus dual-lock cap if triggered]
  key_risk:              [residual incumbent strength; reference FLAG entries]

### HANDOFF TABLE

SESSION INVARIANT C enforced. All fields carry [derived from: X].

  FIELD                      | VALUE   | DERIVATION                          | IND. CHAIN
  ---------------------------|---------|-------------------------------------|------------------
  scout_anchor               | [value] | [derived from: ROLE B scout load]   | n/a
  incumbent_threat_locked    | [true]  | [derived from: ROLE C analysis]     | n/a
  hypothesis                 | [value] | [derived from: Stage 1 artifact]    | n/a
  counter_hypothesis         | [value] | [derived from: Stage 1 artifact]    | n/a
  s2_ce_verdict              | [value] | [derived from: Stage 2 artifact]    | n/a
  s3_ce_verdict              | [value] | [derived from: Stage 3 artifact]    | n/a
  s4_ce_verdict              | [value] | [derived from: Stage 4 artifact]    | n/a
  null_tally_final           | [N]     | [derived from: s2+s3+s4 CE verdicts]| does not pass through co_activation
  co_activation_confirmed    | [value] | [derived from: ATOMIC DUAL-LOCK]    | does not pass through incumbent_defense
  incumbent_defense_closed   | [t/f]   | [derived from: s2+s3+s4 direct]     | does not pass through co_activation
  confidence_composite       | [value] | [derived from: Stage 5 synthesis]   | capped by INV B
  schema_compliance_confirmed| [true]  | [all 11 fields verified]            | n/a

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete — Evidence brief ready for topic-story."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## V-05 — Full Integration

**Axes**: role_dependency_annotation + displacement_momentum_score + block3_multi_stage_chain
+ C-15 exact-value artifact reads at every stage transition (combined)
**Hypothesis**: V-01 (dependency annotations), V-02 (momentum score), and V-03 (three-stage
BLOCK 3 chain) each address one auditability gap in the R17 V-05 baseline. Applied
simultaneously, on top of the full C-15/C-16/C-17 structural stack, they should produce
a 9/9 aspirational score against the v17 rubric. The three patterns are structurally
orthogonal: dependency annotations apply before Stage 0 (pre-stage roles), momentum
score applies across Stages 2-4 (evidence accumulation), and the three-stage BLOCK 3
chain applies at Stage 5 (synthesis closure). No axis overlaps; all three can coexist
without structural conflict.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

depth: standard
confidence: standard
for: {value}
iterations: 1

Topic: {topic}
Date:  {date}

You are running the full prove evidence campaign for this topic.
The campaign builds the case for displacing {status_quo_comparator} with {topic}.
Six stages (Stage 0 = gate, Stages 1-5 = evidence + synthesis). Each stage has numbered
ENTRY CONDITIONS and a named EXIT SIGNAL. No stage body begins until entry conditions confirm.

---

## CAMPAIGN OPEN

  topic:                 {topic}
  date:                  {date}
  status_quo_comparator: [name the incumbent approach this topic must displace]

### INCUMBENT ANCHOR

  incumbent_name:          [full name of status_quo_comparator]
  incumbent_strength:      [one sentence: why the incumbent is currently winning]
  incumbent_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]

### DISPLACEMENT MOMENTUM SCALE

Applied at each evidence stage incumbent check. Accumulates into displacement_momentum_score.

  DELTA | MEANING
  ------|------------------------------------------------------------------
  +2    | Strong displacement evidence — challenger clearly ahead
  +1    | Moderate displacement evidence — challenger gaining
   0    | Neutral / inconclusive
  -1    | Moderate incumbent evidence — challenger not clearly ahead
  -2    | Strong incumbent evidence — incumbent clearly winning

### SESSION INVARIANTS TABLE

  ID   | NAME                      | DECLARATION
  -----|---------------------------|------------------------------------------------------
  D    | INCUMBENT CHECK PHRASING  | Stage 2: "Does [evidence item] support the displacement
       | REGISTER                  |   of {status_quo_comparator} by {topic} on [dimension]?
       |                           |   [Yes / No / Inconclusive] — DELTA: [value]"
       |                           | Stage 3: "Does [practitioner account] reveal a viable
       |                           |   transition path from {status_quo_comparator} to
       |                           |   {topic} for [use case]? [Yes / No / Inconclusive]
       |                           |   — DELTA: [value]"
       |                           | Stage 4: "Does [prototype result] make a credible case
       |                           |   for displacing {status_quo_comparator} with {topic}?
       |                           |   [Yes / No / Pending] — DELTA: [value]"
       |                           | Template deviation = format error.
  -----|---------------------------|------------------------------------------------------
  A    | ADVERSARIAL REVIEWER      | adversarial_reviewer_type: [challenger role].
       | TYPE                      | Activation: null_tally_final >= 3.
  -----|---------------------------|------------------------------------------------------
  B    | CONFIDENCE CAP            | null_ce_cap_rule: confidence_composite -= 2 if
       |                           |   null_tally_final >= 3 (hard cap).
  -----|---------------------------|------------------------------------------------------
  C    | DERIVATION ANNOTATION     | Every handoff field carries [derived from: X].

### ROLE OWNERSHIP TABLE

DEPENDENCY DECLARATIONS: DEPENDS ON column specifies required fields by role.
Execution inversion rule: if Role M depends on field owned by Role N (N declared after M),
execution order inverts to N -> M. Declared order preserved; EXECUTE column reflects
post-inversion order.

  ROLE   | TITLE                    | OWNED FIELD                  | DEPENDS ON                              | EXECUTE
  -------|--------------------------|------------------------------|-----------------------------------------|--------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked      | (none)                                  | FIRST
  ROLE B | SCOUT LOADER             | gate_s_cleared               | (none)                                  | SECOND
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | incumbent_threat_locked (C), gate_s_cleared (B) | THIRD

ROLE C execution (fill now):
  incumbent_threat_locked: [true when INCUMBENT ANCHOR all filled]
  s2_displacement_signal:  [anticipated verdict direction at S2 based on incumbent_vulnerability]
  s3_displacement_signal:  [anticipated verdict direction at S3]
  s4_displacement_signal:  [anticipated verdict direction at S4]
  dependency_satisfied_by: n/a

ROLE B execution (fill now):
  scout_artifact:  [{topic}-scout-record-{date}.md or equivalent]
  scout_loaded:    [true / false]
  gate_s_cleared:  [true if scout_loaded; CAMPAIGN BLOCKED otherwise]
  dependency_satisfied_by: n/a

ROLE A execution (fill now):
  invariant_registry_confirmed: [true when all four invariants registered]
  displacement_scale_registered: [true]
  dependency_satisfied_by: [incumbent_threat_locked from ROLE C — confirmed;
                             gate_s_cleared from ROLE B — confirmed]

### CE VERDICT OWNERSHIP TABLE

  FIELD                      | OWNED BY      | FORMULA
  ---------------------------|---------------|-----------------------------------------------------
  s2_ce_verdict              | Stage 2       | null if no CE; citation if CE found
  s3_ce_verdict              | Stage 3       | null if no CE; citation if CE found
  s4_ce_verdict              | Stage 4       | null if no CE; description if CE found
  null_tally_final           | Stage 4 close | count(null) across s2 + s3 + s4
  displacement_momentum_score| Stage 5 BLOCK 3 | sum of all DELTA values from S2 + S3 + S4

### PRE-COMMITTED HANDOFF SCHEMA TABLE

  FIELD                      | DERIVATION SOURCE                         | IND. CHAIN
  ---------------------------|-------------------------------------------|------------------
  scout_anchor               | ROLE B scout load                         | n/a
  incumbent_threat_locked    | ROLE C analysis                           | n/a
  hypothesis                 | Stage 1 artifact                          | n/a
  counter_hypothesis         | Stage 1 artifact                          | n/a
  s2_ce_verdict              | Stage 2 artifact                          | n/a
  s3_ce_verdict              | Stage 3 artifact                          | n/a
  s4_ce_verdict              | Stage 4 artifact                          | n/a
  null_tally_final           | s2+s3+s4 CE verdicts                      | not through co_activation
  co_activation_confirmed    | ATOMIC DUAL-LOCK                          | not through incumbent_defense
  incumbent_defense_closed   | s2+s3+s4 direct chain                     | not through co_activation
  confidence_composite       | Stage 5 minus reductions                  | capped by INV B
  displacement_momentum_score| S2+S3+S4 deltas                          | not through confidence chain

---

## STAGE 0 — GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] CAMPAIGN OPEN fields filled
  [ ] INCUMBENT ANCHOR filled
  [ ] DISPLACEMENT MOMENTUM SCALE declared
  [ ] SESSION INVARIANTS TABLE complete (INV D includes DELTA annotation)
  [ ] ROLE OWNERSHIP TABLE DEPENDS ON column complete for all roles
  [ ] ROLE C: incumbent_threat_locked = true, displacement signals (s2/s3/s4) recorded
  [ ] ROLE B: gate_s_cleared = true
  [ ] ROLE A: invariant_registry_confirmed = true, displacement_scale_registered = true,
              dependency_satisfied_by confirmed for both upstream fields

STAGE 0 BODY:

  STEP | FIELD                        | OWNER   | REQUIRED                | RESULT
  -----|------------------------------|---------|-------------------------|--------
  1    | incumbent_threat_locked      | ROLE C  | true                    | [confirm or BLOCKED]
  2    | gate_s_cleared               | ROLE B  | true                    | [confirm or BLOCKED]
  3    | invariant_registry_confirmed | ROLE A  | true                    | [confirm or BLOCKED]
  4    | dependency_declarations_complete | TABLE | all DEPENDS ON filled | [confirm or BLOCKED]
  5    | displacement_scale_registered| ROLE A  | true                    | [confirm or BLOCKED]
  6    | displacement_signals_anchored| ROLE C  | s2/s3/s4 all filled     | [confirm or BLOCKED]

  First BLOCKED step halts campaign.

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open — Steps 1-6 confirmed. Dependencies auditable.
   Displacement momentum scale active. Advancing to Stage 1."

---

## STAGE 1 — HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] STAGE 0 EXIT SIGNAL received: gate_open
  [ ] scout_artifact path available from ROLE B
  [ ] Read scout_artifact from disk at ROLE B path: extract scout_anchor_value
  [ ] SESSION INVARIANT D templates registered (including DELTA annotation)

STAGE 1 BODY:

  scout_artifact_path:          [path from ROLE B — not inferred]
  scout_anchor_value:           [field extracted from disk — not from memory or prior signal]
  validation — scout_anchor == scout_anchor_value: [MATCH / INTEGRITY FAILURE]
  hypothesis:                   [falsifiable claim about {topic}]
  counter_hypothesis:           [incumbent's best defense — grounded in ROLE C analysis]
  confidence_prior:             [1-10]
  displacement_momentum:        0  [initializes at zero]
  incumbent_threat_locked:      [true — from ROLE C]
  gate_s_cleared:               [true — from ROLE B]
  invariant_registry_confirmed: [true — from ROLE A]

Write artifact: {topic}-hypothesis-{date}.md. Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked(confidence_prior=[value])
  "STAGE 1 EXIT: hypothesis_locked — {topic}-hypothesis-{date}.md written.
   confidence_prior=[value]. displacement_momentum=0. Stage 2 ready."

---

## STAGE 2 — WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] STAGE 1 EXIT SIGNAL received: hypothesis_locked(confidence_prior=[value])
  [ ] Read {topic}-hypothesis-{date}.md from disk: extract confidence_prior_disk
  [ ] Validate: signal confidence_prior == confidence_prior_disk — mismatch = INTEGRITY FAILURE
  [ ] hypothesis artifact confirmed written
  [ ] SESSION INVARIANT D Stage 2 template active (includes DELTA annotation)

STAGE 2 BODY:
Gather minimum 3 external sources.

INCUMBENT CHECK TABLE — Stage 2 (SESSION INVARIANT D, Stage 2 template + DELTA):
Structural origin: ROLE C `incumbent_threat_locked`.

  ITEM | SOURCE (URL or citation) | SUMMARY (1 sentence) | TEMPLATE APPLIED & VERDICT           | DELTA
  -----|--------------------------|----------------------|--------------------------------------|-------
  1    | [source]                 | [summary]            | "Does [item] support displacement    | [+2/+1/0/-1/-2]
  2    | [source]                 | [summary]            |  of [comparator] by [topic] on       | [value]
  3    | [source]                 | [summary]            |  [dim]? [verdict] — DELTA: [value]"  | [value]

  s2_aggregate_verdict:   [SUPPORTS / MIXED / COUNTERS]
  s2_displacement_delta:  [sum of DELTA column]
  s2_incumbent_check_summary: [N support / M counter / P inconclusive]
  s2_ce_verdict:          [null if no CE; cite item if found]
  confidence_delta_s2:    [+1 / 0 / -1]
  running_confidence:     [confidence_prior + confidence_delta_s2]
  displacement_momentum:  [0 + s2_displacement_delta]

Running null tally: "[N] null. 2 stages remain."
SCHEMA INTEGRITY: [N]/12 fields populated.
Write artifact: {topic}-websearch-{date}.md. Confirm write.

STAGE 2 EXIT SIGNAL: websearch_complete(count=[N], running_confidence=[value], displacement_momentum=[value])
  "STAGE 2 EXIT: s2_aggregate_verdict=[value]. s2_displacement_delta=[value].
   running_confidence=[value]. displacement_momentum=[value]. Stage 3 ready."

---

## STAGE 3 — INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT SIGNAL received: websearch_complete(count=[N], running_confidence=[value], displacement_momentum=[value])
  [ ] Read {topic}-websearch-{date}.md from disk: extract running_confidence_disk, displacement_momentum_disk
  [ ] Validate: signal running_confidence == disk — mismatch = INTEGRITY FAILURE
  [ ] Validate: signal displacement_momentum == disk — mismatch = INTEGRITY FAILURE
  [ ] s2_ce_verdict recorded
  [ ] SESSION INVARIANT D Stage 3 template active (includes DELTA annotation)

STAGE 3 BODY:
Simulate 2-3 practitioner interviews.

INCUMBENT CHECK TABLE — Stage 3 (SESSION INVARIANT D, Stage 3 template + DELTA):

  PRACTITIONER | KEY ACCOUNT (1 sentence) | TEMPLATE APPLIED & VERDICT                               | DELTA
  -------------|--------------------------|----------------------------------------------------------|-------
  [type 1]     | [account]               | "Does [account] reveal transition path? [verdict] — DELTA: [v]" | [value]
  [type 2]     | [account]               | "Does [account] reveal transition path? [verdict] — DELTA: [v]" | [value]
  [type 3]     | [account]               | "Does [account] reveal transition path? [verdict] — DELTA: [v]" | [value]

  s3_aggregate_verdict:   [SUPPORTS / MIXED / COUNTERS]
  s3_displacement_delta:  [sum of DELTA column]
  s3_ce_verdict:          [null if no CE; cite account if found]
  confidence_delta_s3:    [+1 / 0 / -1]
  running_confidence:     [prev + confidence_delta_s3]
  displacement_momentum:  [prev + s3_displacement_delta]

Running null tally: "[N] null. 1 stage remains."
Write artifact: {topic}-interview-{date}.md. Confirm write.

STAGE 3 EXIT SIGNAL: interview_complete(count=[N], running_confidence=[value], displacement_momentum=[value])
  "STAGE 3 EXIT: s3_aggregate_verdict=[value]. s3_displacement_delta=[value].
   running_confidence=[value]. displacement_momentum=[value]. Stage 4 ready."

---

## STAGE 4 — PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT SIGNAL received: interview_complete(count=[N], running_confidence=[value], displacement_momentum=[value])
  [ ] Read {topic}-interview-{date}.md from disk: extract running_confidence_disk, displacement_momentum_disk
  [ ] Validate: signal running_confidence == disk — mismatch = INTEGRITY FAILURE
  [ ] Validate: signal displacement_momentum == disk — mismatch = INTEGRITY FAILURE
  [ ] s3_ce_verdict recorded
  [ ] SESSION INVARIANT D Stage 4 template active (includes DELTA annotation)

STAGE 4 BODY:

  prototype_design:   [description]
  prototype_result:   [findings — 1-3 sentences]

INCUMBENT CHECK TABLE — Stage 4 (SESSION INVARIANT D, Stage 4 template + DELTA):

  ITEM      | PROTOTYPE RESULT (1 sentence) | TEMPLATE APPLIED & VERDICT                       | DELTA
  ----------|-------------------------------|--------------------------------------------------|-------
  prototype | [result]                      | "Does result make credible case for displacement? | [value]
            |                               |  [Yes/No/Pending] — DELTA: [value]"              |

  s4_displacement_verdict: [Yes / No / Pending]
  s4_aggregate_verdict:    [SUPPORTS / MIXED / COUNTERS]
  s4_displacement_delta:   [DELTA value from table]
  s4_ce_verdict:           [null or description]
  confidence_delta_s4:     [+1 / 0 / -1]
  running_confidence:      [prev + confidence_delta_s4]
  displacement_momentum:   [prev + s4_displacement_delta]

Momentum trajectory:
  s2=[value], s3=[value], s4=[value]
  trajectory: [ACCELERATING / STABLE / DECELERATING]

  null_tally_final = [N]
  Cross-check: "Stage 3 was [M]. Final [N]. Match: [true/false]."

Write artifact: {topic}-prototype-{date}.md. Confirm write.

STAGE 4 EXIT SIGNAL: prototype_complete(count=[null_tally_final], running_confidence=[value], displacement_momentum=[value])
  "STAGE 4 EXIT: s4_aggregate_verdict=[value]. null_tally_final=[N].
   running_confidence=[value]. displacement_momentum=[value]. trajectory=[value]. Stage 5 ready."

---

## STAGE 5 — SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT SIGNAL received: prototype_complete(count=[N], running_confidence=[value], displacement_momentum=[value])
  [ ] Read {topic}-prototype-{date}.md from disk: extract running_confidence_disk, null_tally_disk, displacement_momentum_disk
  [ ] Validate running_confidence: signal == disk — mismatch = INTEGRITY FAILURE
  [ ] Validate null_tally_final: signal == disk — mismatch = INTEGRITY FAILURE
  [ ] Validate displacement_momentum: signal == disk — mismatch = INTEGRITY FAILURE
  [ ] counter_hypothesis from Stage 1 present
  [ ] s2/s3/s4 aggregate verdicts all recorded
  [ ] All four SESSION INVARIANT TABLE rows active

STAGE 5 BODY: THREE-BLOCK STRUCTURE
BLOCK execution order: BLOCK 1 -> BLOCK 2 -> BLOCK 3.
Dependency: BLOCK 3 requires output of BLOCK 1 (confidence_resolved) and BLOCK 2
(confidence_post_cr). This is a forward-dependency: BLOCK 3 declared third; no inversion
required. Declared order matches execution order.
SYNTHESIS HARD GATE: synthesis body may not execute until BLOCK 3 COMPLETE signal received.

### BLOCK 1: CONFIDENCE CHAIN RESOLUTION

  chain_equation: [confidence_prior] + [delta_s2] + [delta_s3] + [delta_s4] = [raw]
  null_cap_applied: [yes: raw -= 2 if null_tally_final >= 3; no otherwise]
  confidence_resolved: [raw after null cap]

BLOCK 1 COMPLETE: "BLOCK 1 COMPLETE — confidence_resolved = [value]."

### BLOCK 2: COUNTER-HYPOTHESIS RESOLUTION

  COUNTER_HYPOTHESIS | VERDICT                                  | EVIDENCE
  -------------------|------------------------------------------|-------------------
  [from Stage 1]     | REFUTED / PARTIALLY REFUTED / OPEN RISK  | [artifact citation]

  open_risk_count:    [N]
  cr_delta:           [N * -1]
  confidence_post_cr: [confidence_resolved + cr_delta]

BLOCK 2 COMPLETE: "BLOCK 2 COMPLETE — confidence_post_cr = [value]."

### BLOCK 3: DISPLACEMENT INTEGRITY CHECK

Dependency: BLOCK 1 COMPLETE and BLOCK 2 COMPLETE both required.

THREE-STAGE DISPLACEMENT CHAIN:
Reconstruct displacement evidence from each evidence stage. Compare each to the
prospective displacement_conclusion. FLAG any stage where conclusion diverges.

  STAGE | AGGREGATE VERDICT      | INCUMBENT DELTA SUM | EXPECTED DIRECTION    | CONSISTENT?
  ------|------------------------|---------------------|-----------------------|-------------
  S2    | [s2_aggregate_verdict] | [s2_displacement_delta] | [SUPPORTED / PARTIALLY / UNSUPPORTED] | [YES/NO/FLAG]
  S3    | [s3_aggregate_verdict] | [s3_displacement_delta] | [SUPPORTED / PARTIALLY / UNSUPPORTED] | [YES/NO/FLAG]
  S4    | [s4_aggregate_verdict] | [s4_displacement_delta] | [SUPPORTED / PARTIALLY / UNSUPPORTED] | [YES/NO/FLAG]

  consistency_flags:        [count of FLAG entries]
  chain_pattern:            [e.g., "S2 +3, S3 +1, S4 +2 = stable positive arc"]
  displacement_momentum_final: [sum: s2 + s3 + s4 = total]
  overall_trajectory:       [ACCELERATING / STABLE / DECELERATING]
  displacement_conclusion:  [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  conclusion_justification: [reconcile any FLAGs; note trajectory if DECELERATING]

ATOMIC DUAL-LOCK:
  S2 -> [s2_ce_verdict], S3 -> [s3_ce_verdict], S4 -> [s4_ce_verdict]
  null_tally_final = [N]
  Cross-check vs Stage 4 exit: [Match / Mismatch]

If null_tally_final >= 3:
  Lock 1 (INV A): adversarial review by [adversarial_reviewer_type]. BLOCKED.
  Lock 2 (INV B): confidence_composite -= 2.
  co_activation_confirmed: dual_lock_fired
Else:
  co_activation_confirmed: not_triggered

BLOCK 3 COMPLETE: "BLOCK 3 COMPLETE — displacement_momentum_final = [value].
  trajectory = [value]. displacement_conclusion = [value]. consistency_flags = [N]."

### SYNTHESIS BODY

  hypothesis_verdict:    [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:      [2-3 sentences — reference chain_pattern, trajectory, any flags]
  confidence_composite:  [confidence_post_cr minus dual-lock reduction if triggered]
  key_risk:              [residual incumbent strength; note DECELERATING trajectory if present;
                           reference FLAG entries in displacement chain]

### HANDOFF TABLE

SESSION INVARIANT C enforced. All fields carry [derived from: X]. Unlabeled = format error.

  FIELD                      | VALUE   | DERIVATION                              | IND. CHAIN
  ---------------------------|---------|------------------------------------------|------------------
  scout_anchor               | [value] | [derived from: ROLE B scout load]        | n/a
  incumbent_threat_locked    | [true]  | [derived from: ROLE C analysis]          | n/a
  hypothesis                 | [value] | [derived from: Stage 1 artifact]         | n/a
  counter_hypothesis         | [value] | [derived from: Stage 1 artifact]         | n/a
  s2_ce_verdict              | [value] | [derived from: Stage 2 artifact]         | n/a
  s3_ce_verdict              | [value] | [derived from: Stage 3 artifact]         | n/a
  s4_ce_verdict              | [value] | [derived from: Stage 4 artifact]         | n/a
  null_tally_final           | [N]     | [derived from: s2+s3+s4 CE verdicts]     | does not pass through co_activation
  co_activation_confirmed    | [value] | [derived from: ATOMIC DUAL-LOCK]         | does not pass through incumbent_defense
  incumbent_defense_closed   | [t/f]   | [derived from: s2+s3+s4 direct]          | does not pass through co_activation
  confidence_composite       | [value] | [derived from: Stage 5 BLOCK 3]          | capped by INV B
  displacement_momentum_score| [value] | [derived from: S2+S3+S4 displacement deltas] | not through confidence chain
  schema_compliance_confirmed| [true]  | [all 12 fields match schema]             | n/a

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete — Evidence brief ready for topic-story."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## Summary Table

| Variation | Axis | Single/Combined | New pattern probed | PASS+ candidate |
|-----------|------|-----------------|--------------------|-----------------|
| V-01 | role_dependency_annotation | single | C-17 made first-class via DEPENDS ON column | C-17 PASS+ |
| V-02 | displacement_momentum_score | single | Running delta (-2..+2) per stage, trajectory at Stage 5 | new C-18 candidate |
| V-03 | block3_multi_stage_chain | single | BLOCK 3 reconstructs S2+S3+S4 per-stage chain | C-16 PASS+ |
| V-04 | role_dependency_annotation + block3_multi_stage_chain | combined | V-01 + V-03 — full audit stack | C-16 PASS+ + C-17 PASS+ |
| V-05 | all three + full structural stack | full | V-01 + V-02 + V-03 + C-15 reads at every stage boundary | 9/9 aspirational target |
