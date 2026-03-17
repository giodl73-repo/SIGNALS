---
skill: quest-variate
skill_target: prove-topic
round: R19
date: 2026-03-16
rubric: prove-topic-rubric-v14-2026-03-16.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [output_format, inertia_framing, lifecycle_emphasis]
  combined: [V-04 (output_format + inertia_framing), V-05 (all_three + full_structural_stack)]
baseline: >
  R19 V-01 (resume_audit_gate) serves as the structural floor for all variations.
  Baseline includes: RESUME AUDIT block, ROLE OWNERSHIP TABLE with dependency
  annotations, SESSION INVARIANTS TABLE (D/A/B/C), count-gated exits (S2 >= 5,
  S3 >= 3, S4 >= 3), three-block Stage 5 (BLOCK 1 confidence chain, BLOCK 2
  counter-hypothesis, BLOCK 3 ATOMIC DUAL-LOCK), HANDOFF TABLE with derivation
  annotations enforced by SESSION INVARIANT C.
r19_context: >
  Rubric v14 has 10 criteria (5 essential, 3 recommended, 2 aspirational).
  Essential criteria C-01 through C-05 cover: sub-skill sequence, scout grounding,
  progressive artifact writes, synthesis readiness signal for topic-story, and
  incumbant-displacement thread. This round explores axes that probe the surface
  area of those criteria from different structural angles: output_format tests
  whether table→prose conversion preserves criterion pass conditions; inertia_framing
  tests whether making displacement the narrative lead improves C-02/C-05 compliance;
  lifecycle_emphasis tests whether compressing early phases and expanding Stage 5
  produces sharper exit signals and stronger synthesis readiness.

  V-01 (single: output_format): All tables replaced with inline key: value blocks
  and numbered lists. Tests whether structured prose is as machine-parseable as
  tabular layout for rubric evaluation while potentially being more readable for
  model execution.

  V-02 (single: inertia_framing): Displacement thesis made explicit before SESSION
  INVARIANTS. Each evidence stage (S2, S3, S4) opens with a STAGE DISPLACEMENT
  QUESTION line. Stage 5 synthesis leads with displacement_conclusion before
  hypothesis_verdict. Tests whether foregrounding the incumbent-displacement frame
  at every decision point improves C-02/C-05 compliance.

  V-03 (single: lifecycle_emphasis): Stage 0 compressed to a tight checklist.
  Stages 1-4 compressed to essential output fields only. Stage 5 significantly
  expanded: each block gets its own entry conditions, intermediate compute steps,
  and BLOCK COMPLETE guard. Tests whether front-loading detail in Stage 5 produces
  a cleaner synthesis_complete exit signal recognizable to topic-story.

  V-04 (combined: output_format + inertia_framing): V-01 + V-02. Inline prose
  format throughout with displacement thesis as the narrative lead.

  V-05 (full: all_three + full_structural_stack): V-01 + V-02 + V-03 on top of
  the complete R19 baseline (RESUME AUDIT, tamper-resistant inter-stage reads,
  DEPENDENCY column in ROLE TABLE, count-gated exits, ATOMIC DUAL-LOCK, derivation
  annotations). Tests whether all three structural transformations simultaneously
  satisfy the full v14 rubric.
---

# prove-topic Variations — Round 19 (rubric v14)

**Skill**: prove-topic
**Rubric**: v14 (C-01–C-05 essential, C-06–C-08 recommended, C-09–C-10 aspirational)
**Date**: 2026-03-16
**Round**: R19

---

## Context: what informed this round

The R19 baseline (V-01, resume_audit_gate) is the structural floor. v14 rubric covers
10 criteria. This round explores three axes that are structurally orthogonal to the
resume_audit / count_gate improvements from R19:

| Axis | What it changes | Primary criterion target |
|------|-----------------|--------------------------|
| output_format | tables → inline blocks/lists | C-03, C-04 (artifact write clarity) |
| inertia_framing | displacement thesis leads everywhere | C-02, C-05 (scout grounding + displacement thread) |
| lifecycle_emphasis | compress S0-S4, expand S5 | C-04, C-05 (synthesis readiness signal) |

---

## V-01 — Output Format (Tables to Inline Blocks)

**Axis**: output_format (single)
**Hypothesis**: The current baseline uses tabular layout for SESSION INVARIANTS, ROLE
OWNERSHIP, INCUMBENT CHECK, and HANDOFF output. If tables are replaced with structured
inline key: value blocks and numbered lists, the prompt becomes more readable for model
execution while preserving the same structural constraints. The pass conditions for C-01
through C-05 depend on structural presence, not tabular layout. This tests whether format
transformation preserves rubric compliance.

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

### SESSION INVARIANTS

Register all four before roles execute. Each carries: cannot be modified or bypassed at any
subsequent stage.

1. INVARIANT D — INCUMBENT CHECK PHRASING REGISTER
   Stage 2 template: "Does [evidence item] support the displacement of {status_quo_comparator}
     by {topic} on [dimension]? [Yes / No / Inconclusive]"
   Stage 3 template: "Does [practitioner account] reveal a viable transition path from
     {status_quo_comparator} to {topic} for [use case]? [Yes / No / Inconclusive]"
   Stage 4 template: "Does [prototype result] make a credible case for displacing
     {status_quo_comparator} with {topic}? [Yes / No / Pending]"
   Enforcement: Template deviation = format error. Cannot be modified at any stage.

2. INVARIANT A — ADVERSARIAL REVIEWER TYPE
   adversarial_reviewer_type: [role most likely to challenge the displacement claim]
   Activation: null_tally_final >= 3. Cannot be modified at synthesis.

3. INVARIANT B — CONFIDENCE CAP
   null_ce_cap_rule: confidence_composite -= 2 if null_tally_final >= 3 (hard cap).
   Cannot be softened or overridden at synthesis.

4. INVARIANT C — DERIVATION ANNOTATION
   annotation_rule: Every handoff field carries [derived from: X]. Unlabeled = format error.
   Cannot be modified at synthesis.

### ROLE OWNERSHIP

ROLE C (INCUMBENT THREAT ANALYST) executes first. Owned field: incumbent_threat_locked.
  Reads INCUMBENT ANCHOR. Confirms analysis complete.
  incumbent_threat_locked: [true when incumbent_name, strength, vulnerability all filled]

ROLE B (SCOUT LOADER) executes second. Owned field: gate_s_cleared.
  scout_artifact:  [{topic}-scout-record-{date}.md or equivalent]
  scout_loaded:    [true / false]
  gate_s_cleared:  [true if scout_loaded; CAMPAIGN BLOCKED otherwise]

ROLE A (HYPOTHESIS ARCHITECT) executes third. Owned field: invariant_registry_confirmed.
  Confirms all four SESSION INVARIANT rows filled and active.
  invariant_registry_confirmed: [true when all four invariants registered]
  depends on: incumbent_threat_locked (ROLE C) and gate_s_cleared (ROLE B)

Execution order is C -> B -> A. ROLE A cannot execute until C and B complete.

---

## RESUME AUDIT

Run before Stage 0. Glob existing artifacts for {topic} on {date}.

For each stage artifact, record: FOUND (Y/N) and DECISION (RESUME-SKIP / RUN).

1. Stage 1 — {topic}-hypothesis-{date}.md:       found=[Y/N]  decision=[RESUME-SKIP / RUN]
2. Stage 2 — {topic}-websearch-{date}.md:         found=[Y/N]  decision=[RESUME-SKIP / RUN]
3. Stage 3 — {topic}-interview-{date}.md:         found=[Y/N]  decision=[RESUME-SKIP / RUN]
4. Stage 4 — {topic}-prototype-{date}.md:         found=[Y/N]  decision=[RESUME-SKIP / RUN]
5. Stage 5 — {topic}-synthesis-{date}.md:         found=[Y/N]  decision=[RESUME-SKIP / RUN]

  resume_audit_complete: [true]
  stages_to_run:         [list stages with RUN decision, or ALL if none found]

RESUME AUDIT EXIT: If all five stages are RESUME-SKIP, emit:
  "RESUME_AUDIT_EXIT — All stage artifacts already present. Campaign complete. No stages re-run."
  and STOP. Otherwise: "RESUME_AUDIT_PASS — Stages to run: [list]. Proceeding to Stage 0."

---

## STAGE 0 — GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] RESUME AUDIT completed — resume_audit_complete = true
  [ ] CAMPAIGN OPEN fields filled (topic, date, status_quo_comparator)
  [ ] INCUMBENT ANCHOR filled (incumbent_name, strength, vulnerability)
  [ ] All four SESSION INVARIANTS registered
  [ ] ROLE C executed — incumbent_threat_locked = true
  [ ] ROLE B executed — scout_artifact identified, scout_loaded confirmed
  [ ] ROLE A executed — invariant_registry_confirmed = true

STAGE 0 BODY:

Clearance check — record confirm or BLOCKED for each:
  Step 1: incumbent_threat_locked (ROLE C required) = [confirm or BLOCKED]
  Step 2: gate_s_cleared (ROLE B required)          = [confirm or BLOCKED]
  Step 3: invariant_registry_confirmed (ROLE A)     = [confirm or BLOCKED]

First BLOCKED step halts campaign. Record step number and owning role.

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open — Steps 1, 2, 3 all confirmed. SESSION INVARIANT D active.
   Advancing to Stage 1."

---

## STAGE 1 — HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] STAGE 0 EXIT SIGNAL received: gate_open
  [ ] RESUME AUDIT: Stage 1 decision = RUN (skip entire stage body if RESUME-SKIP)
  [ ] scout_artifact path available from ROLE B
  [ ] SESSION INVARIANT D templates registered

STAGE 1 BODY:

Load scout artifact from path. Read signals. Frame hypothesis.

  source_scout_artifact:        [path from ROLE B — copied, not inferred]
  hypothesis:                   [falsifiable claim about {topic}]
  counter_hypothesis:           [incumbent's best defense — grounded in ROLE C analysis]
  confidence_prior:             [initial confidence score: 1–10]
  gate_s_cleared:               [true — from GATE S Step 2]
  invariant_registry_confirmed: [true — from GATE S Step 3]
  incumbent_threat_locked:      [true — from GATE S Step 1]

Write artifact: {topic}-hypothesis-{date}.md. Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked(confidence_prior=[value])
  "STAGE 1 EXIT: hypothesis_locked — {topic}-hypothesis-{date}.md written.
   confidence_prior=[value]. Stage 2 ready."

---

## STAGE 2 — WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] STAGE 1 EXIT SIGNAL received: hypothesis_locked(confidence_prior=[value])
  [ ] RESUME AUDIT: Stage 2 decision = RUN (skip if RESUME-SKIP)
  [ ] hypothesis artifact confirmed written
  [ ] SESSION INVARIANT D Stage 2 template active

STAGE 2 BODY:

Gather minimum 5 external sources. For each, record:

  Source N:
    url_or_citation: [source]
    summary:         [1 sentence]
    verdict:         "Does [item N] support displacement of {status_quo_comparator}
                      by {topic} on [dimension]? [Yes / No / Inconclusive]"

Record after all sources gathered:

  s2_count:                   [N — must be >= 5]
  s2_incumbent_check_summary: [N support / M counter / P inconclusive]
  s2_ce_verdict:              [null if no CE; cite item if found]
  confidence_delta_s2:        [+1 / 0 / -1 based on evidence weight]
  running_confidence:         [confidence_prior + confidence_delta_s2]

Running null tally: "Running tally: [N] null across 1 stage complete. 2 stages remain."

GATE: Do not fire exit signal until s2_count >= 5. If s2_count < 5, gather
additional external sources before proceeding.

Write artifact: {topic}-websearch-{date}.md. Confirm write.

STAGE 2 EXIT SIGNAL: websearch_complete(count=[N], running_confidence=[value])
  "STAGE 2 EXIT: websearch_complete — s2_ce_verdict=[value]. s2_count=[N] (gate >= 5 met).
   running_confidence=[value]. Stage 3 ready."

---

## STAGE 3 — INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT SIGNAL received: websearch_complete(count=[N], running_confidence=[value])
  [ ] RESUME AUDIT: Stage 3 decision = RUN (skip if RESUME-SKIP)
  [ ] s2_ce_verdict recorded (null or value — not blank)
  [ ] SESSION INVARIANT D Stage 3 template active

STAGE 3 BODY:

Simulate minimum 3 practitioner interviews. For each, record:

  Practitioner N:
    type:    [practitioner type]
    account: [key quote or paraphrase — 1 sentence]
    verdict: "Does [account N] reveal a viable transition path from {status_quo_comparator}
              to {topic} for [use case]? [Yes / No / Inconclusive]"

Record after all interviews complete:

  s3_count:                   [N — must be >= 3]
  s3_incumbent_check_summary: [N support / M counter / P inconclusive]
  s3_ce_verdict:              [null if no CE; cite account if found]
  confidence_delta_s3:        [+1 / 0 / -1]
  running_confidence:         [prev + confidence_delta_s3]

Running null tally: "Running tally: [N] null across 2 stages complete. 1 stage remains."

GATE: Do not fire exit signal until s3_count >= 3. If s3_count < 3, simulate
additional practitioner interviews before proceeding.

Write artifact: {topic}-interview-{date}.md. Confirm write.

STAGE 3 EXIT SIGNAL: interview_complete(count=[N], running_confidence=[value])
  "STAGE 3 EXIT: interview_complete — s3_ce_verdict=[value]. s3_count=[N] (gate >= 3 met).
   running_confidence=[value]. Stage 4 ready."

---

## STAGE 4 — PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT SIGNAL received: interview_complete(count=[N], running_confidence=[value])
  [ ] RESUME AUDIT: Stage 4 decision = RUN (skip if RESUME-SKIP)
  [ ] s3_ce_verdict recorded (null or value — not blank)
  [ ] SESSION INVARIANT D Stage 4 template active

STAGE 4 BODY:

Design and assess minimum 3 prototype experiments. For each, record:

  Experiment N:
    design:  [what was built or tested — 1 sentence]
    result:  [what was learned — 1-2 sentences]
    verdict: "Does [result N] make a credible case for displacing {status_quo_comparator}
              with {topic}? [Yes / No / Pending]"

Record after all experiments complete:

  s4_count:                [N — must be >= 3]
  s4_displacement_verdict: [Yes / No / Pending — required; omission = format error]
  s4_ce_verdict:           [null if no CE; description if found]
  confidence_delta_s4:     [+1 / 0 / -1]
  running_confidence:      [prev + confidence_delta_s4]

Final null tally:
  null_tally_final = [N]
  Cross-check: "Running count from Stage 3 was [M]. Final is [N]. Match: [true/false]."

GATE: Do not fire exit signal until s4_count >= 3. If s4_count < 3, design
additional prototype experiments before proceeding.

Write artifact: {topic}-prototype-{date}.md. Confirm write.

STAGE 4 EXIT SIGNAL: prototype_complete(count=[null_tally_final], running_confidence=[value])
  "STAGE 4 EXIT: prototype_complete — s4_ce_verdict=[value]. null_tally_final=[N].
   running_confidence=[value]. Stage 5 ready."

---

## STAGE 5 — SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT SIGNAL received: prototype_complete(count=[N], running_confidence=[value])
  [ ] RESUME AUDIT: Stage 5 decision = RUN (skip if RESUME-SKIP)
  [ ] null_tally_final recorded
  [ ] counter_hypothesis from Stage 1 available
  [ ] All four SESSION INVARIANTS active

STAGE 5 BODY: THREE-BLOCK STRUCTURE.
SYNTHESIS GATE: no synthesis fields may be populated until BLOCK 3 COMPLETE received.

### BLOCK 1 — CONFIDENCE CHAIN RESOLUTION

  confidence_prior:       [value from Stage 1]
  confidence_delta_s2:    [+/- from Stage 2]
  confidence_delta_s3:    [+/- from Stage 3]
  confidence_delta_s4:    [+/- from Stage 4]
  chain_equation:         [prior + s2 + s3 + s4 = sum]
  null_cap_applied:       [yes — sum -= 2 if null_tally_final >= 3; no otherwise]
  confidence_chain_resolved: [final value after cap]

BLOCK 1 COMPLETE: "BLOCK 1 COMPLETE — confidence_chain_resolved = [value]."

### BLOCK 2 — COUNTER-HYPOTHESIS RESOLUTION

For each counter-hypothesis from Stage 1, record:
  Counter N:
    text:    [counter-hypothesis text]
    verdict: [REFUTED / PARTIALLY REFUTED / OPEN RISK]
    evidence: [cite stage artifact]

  open_risk_count:      [N — count of OPEN RISK verdicts]
  cr_delta:             [open_risk_count * -1]
  confidence_post_cr:   [confidence_chain_resolved + cr_delta]
  counter_hypothesis_verdict: [recorded]

BLOCK 2 COMPLETE: "BLOCK 2 COMPLETE — counter_hypothesis_verdict recorded.
  confidence_post_cr = [value]."

### BLOCK 3 — DISPLACEMENT INTEGRITY CHECK

Requires BLOCK 1 COMPLETE and BLOCK 2 COMPLETE before beginning.

ATOMIC DUAL-LOCK:

  Null tally chain reconstruction:
    s2_ce_verdict: [null or value — from Stage 2 artifact]
    s3_ce_verdict: [null or value — from Stage 3 artifact]
    s4_ce_verdict: [null or value — from Stage 4 artifact]
    null_tally_final = [N]
    Cross-check vs Stage 4 exit count: [Match / Mismatch]

  If null_tally_final >= 3:
    Lock 1 (INVARIANT A): adversarial review by [adversarial_reviewer_type]. BLOCKED.
    Lock 2 (INVARIANT B): confidence_composite -= 2 (hard cap).
    co_activation_confirmed: dual_lock_fired
  Else:
    co_activation_confirmed: not_triggered

  s4_displacement_verdict_confirmed: [value from Stage 4 artifact]
  displacement_conclusion: [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  consistency_flag: [CONSISTENT / INCONSISTENT — mismatch requires justification]

BLOCK 3 COMPLETE: "BLOCK 3 COMPLETE — displacement_conclusion = [value].
  co_activation_confirmed = [value]."

### SYNTHESIS BODY

(Do not populate until BLOCK 3 COMPLETE received.)

  displacement_conclusion:  [from BLOCK 3]
  hypothesis_verdict:       [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:         [2-3 sentences integrating S2, S3, S4 with displacement verdict]
  confidence_composite:     [confidence_post_cr — final after all reductions]
  key_risk:                 [primary adoption risk framed as residual incumbent strength]
  topic_story_readiness:    "Evidence brief complete. Displacement case: [displacement_conclusion].
                             Confidence: [value]. Ready for /topic-story."

### HANDOFF

SESSION INVARIANT C enforced. All fields carry [derived from: X]. Unlabeled = format error.

  scout_anchor:                [value]  [derived from: ROLE B scout load]
  incumbent_threat_locked:     [true]   [derived from: ROLE C analysis]
  hypothesis:                  [value]  [derived from: Stage 1 artifact]
  counter_hypothesis:          [value]  [derived from: Stage 1 artifact]
  s2_ce_verdict:               [value]  [derived from: Stage 2 artifact]
  s3_ce_verdict:               [value]  [derived from: Stage 3 artifact]
  s4_ce_verdict:               [value]  [derived from: Stage 4 artifact]
  null_tally_final:            [N]      [derived from: s2+s3+s4 CE verdicts] [not through co_activation]
  co_activation_confirmed:     [value]  [derived from: ATOMIC DUAL-LOCK] [not through incumbent_defense]
  incumbent_defense_closed:    [t/f]    [derived from: s2+s3+s4 direct] [not through co_activation]
  confidence_composite:        [value]  [derived from: Stage 5 synthesis] [capped by INVARIANT B]
  schema_compliance_confirmed: [true]   [all 11 fields present and sourced]

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete — Evidence brief ready for topic-story."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## V-02 — Inertia Framing (Displacement Thesis as Narrative Lead)

**Axis**: inertia_framing (single)
**Hypothesis**: The current baseline names the incumbent in INCUMBENT ANCHOR and SESSION
INVARIANT D templates, but does not foreground the displacement thesis as the organizing
question of the campaign. If a DISPLACEMENT THESIS block is inserted after CAMPAIGN OPEN,
and each evidence stage (S2, S3, S4) opens with a labeled STAGE DISPLACEMENT QUESTION,
and Stage 5 synthesis leads with displacement_conclusion before hypothesis_verdict, then
the model is more likely to maintain the incumbent thread throughout and satisfy C-02 and
C-05 without relying solely on INVARIANT D enforcement.

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

### DISPLACEMENT THESIS

State before roles run. This thesis drives the entire campaign.

  displacement_question:  "Can {topic} displace {status_quo_comparator} as the dominant
                           approach for [problem domain]?"
  why_change_is_needed:   [one sentence: what gap does the incumbent leave that {topic} fills]
  displacement_bar:       "The campaign succeeds when evidence from three stages independently
                           supports displacement and confidence_composite >= [threshold]."

All stages reference this thesis. The displacement question is answered at Stage 5.

### SESSION INVARIANTS TABLE

SESSION INVARIANT D leads. All invariants carry: "cannot be modified or bypassed at any
subsequent stage." Register all four before roles execute.

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
  -----|---------------------------|------------------------------------------------------
  B    | CONFIDENCE CAP            | null_ce_cap_rule: confidence_composite -= 2 if
       |                           |   null_tally_final >= 3 (hard cap).
  -----|---------------------------|------------------------------------------------------
  C    | DERIVATION ANNOTATION     | annotation_rule: Every handoff field carries
       |                           |   [derived from: X]. Unlabeled = format error.

### ROLE OWNERSHIP TABLE

Roles execute in order C -> B -> A before Stage 0 begins.

  ROLE   | TITLE                    | OWNED FIELD               | EXECUTE
  -------|--------------------------|---------------------------|--------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked   | FIRST
  ROLE B | SCOUT LOADER             | gate_s_cleared            | SECOND
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | THIRD

ROLE C execution (fill now):
  Reads INCUMBENT ANCHOR and DISPLACEMENT THESIS above.
  incumbent_threat_locked: [true when incumbent analysis complete — name/strength/vulnerability filled]

ROLE B execution (fill now):
  scout_artifact:  [{topic}-scout-record-{date}.md or equivalent]
  scout_loaded:    [true / false]
  gate_s_cleared:  [true if scout_loaded; CAMPAIGN BLOCKED otherwise]

ROLE A execution (fill now):
  Confirms all four SESSION INVARIANT TABLE rows filled and active.
  invariant_registry_confirmed: [true when all four invariants registered]

---

## RESUME AUDIT

Run before Stage 0. Glob existing artifacts for {topic} on {date}.

  STAGE | ARTIFACT PATTERN                                   | FOUND | DECISION
  ------|-----------------------------------------------------|-------|------------------
  1     | simulations/prove/{topic}-hypothesis-{date}.md     | [Y/N] | [RESUME-SKIP / RUN]
  2     | simulations/prove/{topic}-websearch-{date}.md      | [Y/N] | [RESUME-SKIP / RUN]
  3     | simulations/prove/{topic}-interview-{date}.md      | [Y/N] | [RESUME-SKIP / RUN]
  4     | simulations/prove/{topic}-prototype-{date}.md      | [Y/N] | [RESUME-SKIP / RUN]
  5     | simulations/prove/{topic}-synthesis-{date}.md      | [Y/N] | [RESUME-SKIP / RUN]

  resume_audit_complete: [true]
  stages_to_run: [list of RUN stages, or ALL if none found]

RESUME AUDIT EXIT: If all five RESUME-SKIP: "RESUME_AUDIT_EXIT — All stage artifacts
already present. Campaign complete." and STOP.
Otherwise: "RESUME_AUDIT_PASS — Stages to run: [list]. Proceeding to Stage 0."

---

## STAGE 0 — GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] RESUME AUDIT completed — resume_audit_complete = true
  [ ] CAMPAIGN OPEN, INCUMBENT ANCHOR, DISPLACEMENT THESIS all filled
  [ ] SESSION INVARIANTS TABLE complete — all four rows filled
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
  4    | displacement_thesis_filed    | OPEN    | true     | [confirm or BLOCKED]

  First BLOCKED step halts campaign.

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open — Steps 1-4 confirmed. Displacement thesis active.
   SESSION INVARIANT D registered. Advancing to Stage 1."

---

## STAGE 1 — HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] STAGE 0 EXIT SIGNAL received: gate_open
  [ ] RESUME AUDIT: Stage 1 decision = RUN (skip if RESUME-SKIP)
  [ ] scout_artifact path from ROLE B
  [ ] DISPLACEMENT THESIS filed and active

STAGE 1 BODY:

Load scout artifact. Extract signals. Frame hypothesis against the displacement question.

  source_scout_artifact:   [path from ROLE B — not inferred]
  displacement_context:    [how scout findings relate to the displacement question]
  hypothesis:              [falsifiable claim about {topic}'s ability to displace the incumbent]
  counter_hypothesis:      [incumbent's strongest defense — why {status_quo_comparator} holds]
  confidence_prior:        [initial confidence score: 1–10]

Write artifact: {topic}-hypothesis-{date}.md. Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked(confidence_prior=[value])
  "STAGE 1 EXIT: hypothesis_locked — {topic}-hypothesis-{date}.md written.
   confidence_prior=[value]. Displacement hypothesis active. Stage 2 ready."

---

## STAGE 2 — WEB SEARCH

STAGE DISPLACEMENT QUESTION: "Does external evidence support displacement of
{status_quo_comparator} by {topic}?"

STAGE 2 ENTRY CONDITIONS:
  [ ] STAGE 1 EXIT SIGNAL received: hypothesis_locked(confidence_prior=[value])
  [ ] RESUME AUDIT: Stage 2 decision = RUN (skip if RESUME-SKIP)
  [ ] hypothesis artifact confirmed written
  [ ] SESSION INVARIANT D Stage 2 template active

STAGE 2 BODY:

Gather minimum 5 external sources. Apply SESSION INVARIANT D Stage 2 template verbatim
to each item.

INCUMBENT CHECK TABLE — Stage 2:

  ITEM | SOURCE (URL or citation) | SUMMARY (1 sentence) | TEMPLATE APPLIED & VERDICT
  -----|--------------------------|----------------------|------------------------------
  1    | [source]                 | [summary]            | "Does [item 1] support
  2    | [source]                 | [summary]            |  displacement of [comparator]
  3    | [source]                 | [summary]            |  by [topic] on [dim]? [verdict]"
  4    | [source]                 | [summary]            |
  5    | [source]                 | [summary]            |

  s2_count:                   [N] — must be >= 5
  s2_incumbent_check_summary: [N support / M counter / P inconclusive]
  s2_stage_displacement_verdict: [overall direction — SUPPORTING / MIXED / OPPOSING]
  s2_ce_verdict:              [null if no CE; cite item if found]
  confidence_delta_s2:        [+1 / 0 / -1]
  running_confidence:         [prior + delta]

Running null tally: "Running tally: [N] null across 1 stage complete. 2 remain."

GATE: Do not fire exit signal until s2_count >= 5.

Write artifact: {topic}-websearch-{date}.md. Confirm write.

STAGE 2 EXIT SIGNAL: websearch_complete(count=[N], running_confidence=[value])
  "STAGE 2 EXIT: websearch_complete — s2_stage_displacement_verdict=[value].
   s2_ce_verdict=[value]. s2_count=[N] (gate >= 5 met). running_confidence=[value].
   Stage 3 ready."

---

## STAGE 3 — INTERVIEW

STAGE DISPLACEMENT QUESTION: "Do practitioners confirm a viable path from
{status_quo_comparator} to {topic}?"

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT SIGNAL received: websearch_complete
  [ ] RESUME AUDIT: Stage 3 decision = RUN (skip if RESUME-SKIP)
  [ ] s2_ce_verdict recorded (null or value)
  [ ] SESSION INVARIANT D Stage 3 template active

STAGE 3 BODY:

Simulate minimum 3 practitioner interviews. Apply SESSION INVARIANT D Stage 3 template
verbatim to each account.

INCUMBENT CHECK TABLE — Stage 3:

  PRACTITIONER     | KEY ACCOUNT (1 sentence)     | TEMPLATE APPLIED & VERDICT
  -----------------|------------------------------|------------------------------
  [type 1]         | [quote or paraphrase]        | "Does [account 1] reveal a viable
  [type 2]         | [quote or paraphrase]        |  transition path from [comparator]
  [type 3]         | [quote or paraphrase]        |  to [topic] for [use case]? [verdict]"

  s3_count:                      [N] — must be >= 3
  s3_incumbent_check_summary:    [N support / M counter / P inconclusive]
  s3_stage_displacement_verdict: [SUPPORTING / MIXED / OPPOSING]
  s3_ce_verdict:                 [null if no CE; cite account if found]
  confidence_delta_s3:           [+1 / 0 / -1]
  running_confidence:            [prev + delta]

Running null tally: "Running tally: [N] null across 2 stages complete. 1 remains."

GATE: Do not fire exit signal until s3_count >= 3.

Write artifact: {topic}-interview-{date}.md. Confirm write.

STAGE 3 EXIT SIGNAL: interview_complete(count=[N], running_confidence=[value])
  "STAGE 3 EXIT: interview_complete — s3_stage_displacement_verdict=[value].
   s3_ce_verdict=[value]. s3_count=[N] (gate >= 3 met). running_confidence=[value].
   Stage 4 ready."

---

## STAGE 4 — PROTOTYPE

STAGE DISPLACEMENT QUESTION: "Does prototype evidence make a credible case for
displacing {status_quo_comparator} with {topic}?"

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT SIGNAL received: interview_complete
  [ ] RESUME AUDIT: Stage 4 decision = RUN (skip if RESUME-SKIP)
  [ ] s3_ce_verdict recorded
  [ ] SESSION INVARIANT D Stage 4 template active

STAGE 4 BODY:

Design and assess minimum 3 prototype experiments.

  prototype_design:   [brief description]
  prototype_result:   [what was learned — 1-3 sentences]

INCUMBENT CHECK TABLE — Stage 4:

  ITEM       | PROTOTYPE RESULT (1 sentence)  | TEMPLATE APPLIED & VERDICT
  -----------|--------------------------------|-------------------------------
  prototype  | [prototype_result]             | "Does [result] make a credible case
             |                                |  for displacing [comparator] with
             |                                |  [topic]? [Yes / No / Pending]"

  s4_count:                      [N] — must be >= 3
  s4_stage_displacement_verdict: [overall: SUPPORTED / PARTIALLY / UNSUPPORTED]
  s4_displacement_verdict:       [Yes / No / Pending — required; omission = format error]
  s4_ce_verdict:                 [null if no CE; description if found]
  confidence_delta_s4:           [+1 / 0 / -1]
  running_confidence:            [prev + delta]

Final null tally:
  null_tally_final = [N]
  Cross-check: "Running count from Stage 3 was [M]. Final is [N]. Match: [true/false]."

GATE: Do not fire exit signal until s4_count >= 3.

Write artifact: {topic}-prototype-{date}.md. Confirm write.

STAGE 4 EXIT SIGNAL: prototype_complete(count=[null_tally_final], running_confidence=[value])
  "STAGE 4 EXIT: prototype_complete — s4_stage_displacement_verdict=[value].
   s4_ce_verdict=[value]. null_tally_final=[N]. running_confidence=[value]. Stage 5 ready."

---

## STAGE 5 — SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT SIGNAL received: prototype_complete
  [ ] RESUME AUDIT: Stage 5 decision = RUN (skip if RESUME-SKIP)
  [ ] null_tally_final recorded
  [ ] counter_hypothesis from Stage 1 present
  [ ] All four SESSION INVARIANTS active

SYNTHESIS BEGINS WITH DISPLACEMENT ANSWER. Do not populate synthesis body until
BLOCK 3 COMPLETE received.

STAGE 5 BODY: THREE-BLOCK STRUCTURE.
BLOCK 1 and BLOCK 2 run first. BLOCK 3 requires both BLOCK 1 and BLOCK 2 outputs.
SYNTHESIS HARD GATE: no synthesis fields populated until BLOCK 3 COMPLETE.

### BLOCK 1 — CONFIDENCE CHAIN RESOLUTION

  prior:                    [value at Stage 1]
  s2_delta:                 [from Stage 2]
  s3_delta:                 [from Stage 3]
  s4_delta:                 [from Stage 4]
  chain_equation:           prior + s2 + s3 + s4 = [sum]
  null_cap_applied:         [yes if null_tally_final >= 3; no otherwise]
  confidence_chain_resolved: [final after cap]

BLOCK 1 COMPLETE: "BLOCK 1 COMPLETE — confidence_chain_resolved = [value]."

### BLOCK 2 — COUNTER-HYPOTHESIS RESOLUTION

  COUNTER_HYPOTHESIS     | VERDICT                                  | EVIDENCE
  -----------------------|------------------------------------------|-------------------
  [from Stage 1]         | REFUTED / PARTIALLY REFUTED / OPEN RISK  | [cite stage artifact]

  open_risk_count:            [N]
  cr_delta:                   [N * -1]
  confidence_post_cr:         [confidence_chain_resolved + cr_delta]
  counter_hypothesis_verdict: [recorded]

BLOCK 2 COMPLETE: "BLOCK 2 COMPLETE — counter_hypothesis_verdict recorded.
  confidence_post_cr = [value]."

### BLOCK 3 — DISPLACEMENT INTEGRITY CHECK

Requires BLOCK 1 COMPLETE and BLOCK 2 COMPLETE.

ATOMIC DUAL-LOCK:
  S2 -> [s2_ce_verdict: null or value]
  S3 -> [s3_ce_verdict: null or value]
  S4 -> [s4_ce_verdict: null or value]
  null_tally_final = [N]
  Cross-check vs Stage 4 exit: [Match / Mismatch]

If null_tally_final >= 3:
  Lock 1 (INVARIANT A): adversarial review by [adversarial_reviewer_type]. BLOCKED.
  Lock 2 (INVARIANT B): confidence_composite -= 2 (hard cap).
  co_activation_confirmed: dual_lock_fired
Else:
  co_activation_confirmed: not_triggered

  displacement_per_stage: S2=[s2_stage_displacement_verdict], S3=[s3_stage_displacement_verdict], S4=[s4_stage_displacement_verdict]
  displacement_conclusion: [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED — answer to DISPLACEMENT THESIS question]
  consistency_flag:        [CONSISTENT / INCONSISTENT with s4_displacement_verdict]

BLOCK 3 COMPLETE: "BLOCK 3 COMPLETE — displacement_conclusion = [value].
  Per-stage verdict: S2=[v], S3=[v], S4=[v]. consistency_flag=[value]."

### SYNTHESIS BODY

(Do not populate until BLOCK 3 COMPLETE.)

  displacement_conclusion:  [from BLOCK 3 — leads synthesis]
  hypothesis_verdict:       [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:         [2-3 sentences: open with displacement verdict, then hypothesis,
                             then confidence trajectory]
  confidence_composite:     [confidence_post_cr — final]
  key_risk:                 [primary adoption risk framed as residual incumbent strength]
  topic_story_readiness:    "Displacement case for {topic} over {status_quo_comparator}:
                             [displacement_conclusion]. Evidence brief ready for /topic-story."

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
  null_tally_final           | [N]     | [derived from: s2+s3+s4 verdicts]   | not through co_activation
  co_activation_confirmed    | [value] | [derived from: ATOMIC DUAL-LOCK]    | not through incumbent_defense
  incumbent_defense_closed   | [t/f]   | [derived from: s2+s3+s4 direct]     | not through co_activation
  confidence_composite       | [value] | [derived from: Stage 5 synthesis]   | capped by INVARIANT B
  schema_compliance_confirmed| [true]  | [all 11 fields present and sourced] | n/a

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete — Displacement case: [displacement_conclusion].
   Confidence: [value]. Evidence brief ready for topic-story."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## V-03 — Lifecycle Emphasis (Compressed Setup, Expanded Stage 5)

**Axis**: lifecycle_emphasis (single)
**Hypothesis**: The current baseline allocates similar detail depth across all phases.
Stage 0 (gate) has a full clearance table; Stages 1-4 have comparable instruction density;
Stage 5 has three blocks but they are compact. If Stage 0 is compressed to a tight checklist,
Stages 1-4 are reduced to essential output fields only, and Stage 5 is significantly expanded
with per-block entry conditions, intermediate compute variables, and explicit block-complete
guards, the synthesis section will be more legible and the synthesis_complete exit signal
will be more clearly recognized by downstream consumers like /topic-story.

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

  ID | NAME                     | DECLARATION (summarized)
  ---|--------------------------|-------------------------------------------------------------
  D  | INCUMBENT CHECK PHRASING | Per-stage templates (S2/S3/S4) locked; deviation = error.
  A  | ADVERSARIAL REVIEWER     | Type locked; activates when null_tally_final >= 3.
  B  | CONFIDENCE CAP           | confidence_composite -= 2 if null_tally_final >= 3.
  C  | DERIVATION ANNOTATION    | All handoff fields carry [derived from: X]; unlabeled = error.

Full templates for INVARIANT D:
  S2: "Does [evidence item] support the displacement of {status_quo_comparator} by {topic}
       on [dimension]? [Yes / No / Inconclusive]"
  S3: "Does [practitioner account] reveal a viable transition path from
       {status_quo_comparator} to {topic} for [use case]? [Yes / No / Inconclusive]"
  S4: "Does [prototype result] make a credible case for displacing {status_quo_comparator}
       with {topic}? [Yes / No / Pending]"

### ROLE OWNERSHIP TABLE

  ROLE   | TITLE                    | OWNED FIELD               | EXECUTE
  -------|--------------------------|---------------------------|--------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked   | FIRST
  ROLE B | SCOUT LOADER             | gate_s_cleared            | SECOND
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | THIRD

ROLE C: incumbent_threat_locked = [true when INCUMBENT ANCHOR filled]
ROLE B: scout_artifact = [{topic}-scout-record-{date}.md]; gate_s_cleared = [true/false]
ROLE A: invariant_registry_confirmed = [true when all four rows filled]

---

## RESUME AUDIT

Glob existing artifacts. Record RESUME-SKIP or RUN per stage.

  Stage 1 ({topic}-hypothesis-{date}.md):  [RESUME-SKIP / RUN]
  Stage 2 ({topic}-websearch-{date}.md):   [RESUME-SKIP / RUN]
  Stage 3 ({topic}-interview-{date}.md):   [RESUME-SKIP / RUN]
  Stage 4 ({topic}-prototype-{date}.md):   [RESUME-SKIP / RUN]
  Stage 5 ({topic}-synthesis-{date}.md):   [RESUME-SKIP / RUN]

If all RESUME-SKIP: "RESUME_AUDIT_EXIT — All artifacts present. STOP."
Otherwise: "RESUME_AUDIT_PASS — Running: [list]."

---

## STAGE 0 — GATE S (compressed)

Required before advancing:
  [ ] All CAMPAIGN OPEN fields filled
  [ ] INCUMBENT ANCHOR filled
  [ ] All four SESSION INVARIANTS registered
  [ ] incumbent_threat_locked = true (ROLE C)
  [ ] gate_s_cleared = true (ROLE B)
  [ ] invariant_registry_confirmed = true (ROLE A)

If any item is false: "CAMPAIGN BLOCKED — item [N] not satisfied."
If all true: "STAGE 0 EXIT: gate_open — Advancing to Stage 1."

---

## STAGE 1 — HYPOTHESIS (compressed)

Skip if RESUME-SKIP. Otherwise:

  source_scout_artifact: [path from ROLE B]
  hypothesis:            [falsifiable claim about {topic}]
  counter_hypothesis:    [incumbent's best defense]
  confidence_prior:      [1–10]

Write {topic}-hypothesis-{date}.md. Confirm write.

EXIT: "STAGE 1 EXIT: hypothesis_locked — confidence_prior=[value]. Stage 2 ready."

---

## STAGE 2 — WEB SEARCH (compressed)

Skip if RESUME-SKIP. Gather minimum 5 sources. Apply INVARIANT D S2 template to each.

  ITEM | SOURCE | SUMMARY | TEMPLATE APPLIED & VERDICT
  -----|--------|---------|----------------------------
  1-5  | ...    | ...     | "Does [item] support displacement...? [verdict]"

  s2_count >= 5 required. s2_ce_verdict = [null/value]. confidence_delta_s2 = [+/-].
  running_confidence = [prior + delta].
  Running null tally: [N] null, 1 stage done, 2 remain.

GATE: s2_count >= 5 before exit fires.
Write {topic}-websearch-{date}.md.

EXIT: "STAGE 2 EXIT: websearch_complete — count=[N], running_confidence=[value]."

---

## STAGE 3 — INTERVIEW (compressed)

Skip if RESUME-SKIP. Simulate minimum 3 practitioners. Apply INVARIANT D S3 template.

  PRACTITIONER | ACCOUNT | TEMPLATE APPLIED & VERDICT
  -------------|---------|----------------------------
  1-3          | ...     | "Does [account] reveal a viable transition path...? [verdict]"

  s3_count >= 3 required. s3_ce_verdict = [null/value]. confidence_delta_s3 = [+/-].
  running_confidence = [prev + delta].
  Running null tally: [N] null, 2 stages done, 1 remains.

GATE: s3_count >= 3 before exit fires.
Write {topic}-interview-{date}.md.

EXIT: "STAGE 3 EXIT: interview_complete — count=[N], running_confidence=[value]."

---

## STAGE 4 — PROTOTYPE (compressed)

Skip if RESUME-SKIP. Design minimum 3 experiments. Apply INVARIANT D S4 template.

  ITEM | PROTOTYPE RESULT | TEMPLATE APPLIED & VERDICT
  -----|------------------|----------------------------
  1-3  | ...              | "Does [result] make a credible case for displacing...? [verdict]"

  s4_count >= 3 required. s4_displacement_verdict = [Yes/No/Pending — required].
  s4_ce_verdict = [null/value]. confidence_delta_s4 = [+/-]. running_confidence = [prev + delta].

  Final null tally:
    null_tally_final = [N]
    Cross-check: count from Stage 3 was [M]. Final [N]. Match: [true/false].

GATE: s4_count >= 3 before exit fires.
Write {topic}-prototype-{date}.md.

EXIT: "STAGE 4 EXIT: prototype_complete — null_tally_final=[N], running_confidence=[value]."

---

## STAGE 5 — SYNTHESIS (expanded)

Skip if RESUME-SKIP. SYNTHESIS HARD GATE: No synthesis fields populated until BLOCK 3 COMPLETE.

### BLOCK 1 — CONFIDENCE CHAIN RESOLUTION

BLOCK 1 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT SIGNAL received: prototype_complete
  [ ] confidence_prior value available from Stage 1 artifact (read from disk if BLOCK 2/3 depend on value)
  [ ] s2_delta, s3_delta, s4_delta available from respective stage artifacts

BLOCK 1 COMPUTE:

  Step 1 — Read prior confidence:
    confidence_prior_source: [Stage 1 artifact path]
    confidence_prior:        [value read from disk — not from memory]

  Step 2 — Accumulate deltas:
    chain_equation:           [prior] + [s2_delta] + [s3_delta] + [s4_delta] = [raw_sum]

  Step 3 — Apply null cap:
    null_tally_final:         [N — from Stage 4 exit signal]
    null_cap_applies:         [yes if N >= 3; no otherwise]
    cap_amount:               [2 if cap applies; 0 otherwise]
    confidence_chain_resolved: [raw_sum - cap_amount]

  Step 4 — Verify:
    chain_integrity_check:    [raw_sum matches running_confidence at Stage 4 close: yes/no]
    If no: record discrepancy and reconcile before proceeding.

BLOCK 1 COMPLETE SIGNAL:
  "BLOCK 1 COMPLETE — confidence_chain_resolved = [value]. Cap applied: [yes/no].
   Chain integrity: [ok / discrepancy — [detail]]."

---

### BLOCK 2 — COUNTER-HYPOTHESIS RESOLUTION

BLOCK 2 ENTRY CONDITIONS:
  [ ] BLOCK 1 COMPLETE signal received
  [ ] counter_hypothesis available from Stage 1 artifact

BLOCK 2 COMPUTE:

  Read counter_hypothesis from {topic}-hypothesis-{date}.md.

  For each counter-hypothesis item:

    Item N:
      text:    [counter-hypothesis text]
      verdict: [REFUTED / PARTIALLY REFUTED / OPEN RISK]
      basis:   [cite the stage artifact that determines this verdict]

  Summary:
    open_risk_count:            [N — count of OPEN RISK items]
    refuted_count:              [M]
    partially_refuted_count:    [P]

  Confidence adjustment:
    cr_delta:                   [open_risk_count * -1]
    confidence_post_cr:         [confidence_chain_resolved + cr_delta]
    confidence_floor_check:     [if confidence_post_cr < 1, set to 1]
    counter_hypothesis_verdict: [recorded — all items resolved]

BLOCK 2 COMPLETE SIGNAL:
  "BLOCK 2 COMPLETE — counter_hypothesis_verdict recorded. open_risk_count=[N].
   confidence_post_cr = [value]."

---

### BLOCK 3 — DISPLACEMENT INTEGRITY CHECK

BLOCK 3 ENTRY CONDITIONS:
  [ ] BLOCK 1 COMPLETE signal received: confidence_chain_resolved = [value]
  [ ] BLOCK 2 COMPLETE signal received: counter_hypothesis_verdict recorded,
      confidence_post_cr = [value]

BLOCK 3 COMPUTE:

ATOMIC DUAL-LOCK:

  Step 1 — Reconstruct null tally chain from stage artifacts:
    s2_ce_verdict (from {topic}-websearch-{date}.md):  [null or value]
    s3_ce_verdict (from {topic}-interview-{date}.md):  [null or value]
    s4_ce_verdict (from {topic}-prototype-{date}.md):  [null or value]
    null_tally_reconstructed:    [count of non-null verdicts above]
    null_tally_final_from_exit:  [N from Stage 4 exit signal]
    tally_cross_check:           [Match / Mismatch — Mismatch = integrity failure]

  Step 2 — Apply dual-lock if triggered:
    If null_tally_final >= 3:
      Lock 1 — ADVERSARIAL REVIEW: adversarial_reviewer_type=[type]. Synthesis BLOCKED
                until adversarial review complete. Record adversarial verdict.
      Lock 2 — CONFIDENCE CAP: confidence_composite = confidence_post_cr - 2.
      co_activation_confirmed: dual_lock_fired
    Else:
      co_activation_confirmed: not_triggered
      confidence_composite:    [confidence_post_cr]

  Step 3 — Displacement conclusion:
    s4_displacement_verdict_from_artifact: [read from {topic}-prototype-{date}.md]
    displacement_conclusion:               [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
    consistency_check: displacement_conclusion aligns with s4_displacement_verdict?
    consistency_flag:  [CONSISTENT / INCONSISTENT]
    If INCONSISTENT: record justification before proceeding.

  Step 4 — Incumbent defense closure:
    incumbent_defense_closed: [true if displacement evidence from S2, S3, S4 collectively
                               addresses the incumbent_vulnerability from ROLE C]
    closure_basis: [cite S2, S3, S4 incumbent check summaries]

BLOCK 3 COMPLETE SIGNAL:
  "BLOCK 3 COMPLETE — displacement_conclusion = [value]. consistency_flag = [value].
   co_activation_confirmed = [value]. incumbent_defense_closed = [true/false]."

---

### SYNTHESIS BODY

SYNTHESIS GATE CHECK: [ ] BLOCK 3 COMPLETE received. If not: SYNTHESIS BLOCKED.

  displacement_conclusion:  [from BLOCK 3]
  hypothesis_verdict:       [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:         [2-3 sentences integrating S2, S3, S4 with displacement verdict from S4]
  confidence_composite:     [final — from BLOCK 3, after all reductions]
  key_risk:                 [primary adoption risk framed as residual incumbent strength]
  topic_story_readiness:    "Evidence brief complete. Hypothesis [hypothesis_verdict].
                             Displacement: [displacement_conclusion]. Confidence: [value].
                             All five stage artifacts written. Ready for /topic-story."

### HANDOFF TABLE

SESSION INVARIANT C enforced. All fields carry [derived from: X]. Unlabeled = format error.

  FIELD                      | VALUE   | DERIVATION                               | IND. CHAIN
  ---------------------------|---------|------------------------------------------|------------------
  scout_anchor               | [value] | [derived from: ROLE B scout load]        | n/a
  incumbent_threat_locked    | [true]  | [derived from: ROLE C analysis]          | n/a
  hypothesis                 | [value] | [derived from: Stage 1 artifact]         | n/a
  counter_hypothesis         | [value] | [derived from: Stage 1 artifact]         | n/a
  s2_ce_verdict              | [value] | [derived from: Stage 2 artifact]         | n/a
  s3_ce_verdict              | [value] | [derived from: Stage 3 artifact]         | n/a
  s4_ce_verdict              | [value] | [derived from: Stage 4 artifact]         | n/a
  null_tally_final           | [N]     | [derived from: BLOCK 3 reconstruction]   | not through co_activation
  co_activation_confirmed    | [value] | [derived from: ATOMIC DUAL-LOCK]         | not through incumbent_defense
  incumbent_defense_closed   | [t/f]   | [derived from: BLOCK 3 closure check]    | not through co_activation
  confidence_composite       | [value] | [derived from: BLOCK 3 after all caps]   | capped by INVARIANT B
  schema_compliance_confirmed| [true]  | [all 11 fields present and sourced]      | n/a

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete — hypothesis_verdict=[value].
   displacement_conclusion=[value]. confidence_composite=[value].
   Five stage artifacts written. Evidence brief ready for topic-story."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## V-04 — Output Format + Inertia Framing (combined)

**Axes**: output_format + inertia_framing
**Hypothesis**: V-01 tests whether tables can be replaced by inline blocks without
degrading rubric compliance. V-02 tests whether foregrounding displacement thesis
improves C-02/C-05. If both axes hold independently, their combination should produce
a prompt that is both more readable (inline format) and more incumbent-aware (displacement
framing at every decision point) without any criterion regression.

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

### DISPLACEMENT THESIS

State before roles run. This thesis drives the entire campaign.

  displacement_question:  "Can {topic} displace {status_quo_comparator} as the dominant
                           approach for [problem domain]?"
  why_change_is_needed:   [one sentence: gap the incumbent leaves that {topic} fills]
  displacement_bar:       "Campaign succeeds when three evidence stages independently support
                           displacement AND confidence_composite >= [threshold]."

### SESSION INVARIANTS

Four invariants. Register all before roles execute. Each carries: cannot be modified
or bypassed at any subsequent stage.

1. INVARIANT D — INCUMBENT CHECK PHRASING REGISTER
   Stage 2 template: "Does [evidence item] support the displacement of {status_quo_comparator}
     by {topic} on [dimension]? [Yes / No / Inconclusive]"
   Stage 3 template: "Does [practitioner account] reveal a viable transition path from
     {status_quo_comparator} to {topic} for [use case]? [Yes / No / Inconclusive]"
   Stage 4 template: "Does [prototype result] make a credible case for displacing
     {status_quo_comparator} with {topic}? [Yes / No / Pending]"
   Enforcement: Template deviation = format error. Cannot be modified.

2. INVARIANT A — ADVERSARIAL REVIEWER TYPE
   adversarial_reviewer_type: [role most likely to challenge displacement]
   Activation: null_tally_final >= 3. Cannot be modified.

3. INVARIANT B — CONFIDENCE CAP
   null_ce_cap_rule: confidence_composite -= 2 if null_tally_final >= 3.
   Cannot be softened.

4. INVARIANT C — DERIVATION ANNOTATION
   annotation_rule: Every handoff field carries [derived from: X]. Unlabeled = error.

### ROLE OWNERSHIP

Three roles execute in sequence before Stage 0 begins.

ROLE C — INCUMBENT THREAT ANALYST (executes first)
  Purpose: Lock the incumbent threat analysis.
  Reads INCUMBENT ANCHOR and DISPLACEMENT THESIS.
  incumbent_threat_locked: [true when incumbent_name, strength, vulnerability filled]

ROLE B — SCOUT LOADER (executes second)
  Purpose: Confirm scout artifact is on disk.
  scout_artifact: [{topic}-scout-record-{date}.md or equivalent]
  scout_loaded:   [true / false]
  gate_s_cleared: [true if scout_loaded; CAMPAIGN BLOCKED otherwise]

ROLE A — HYPOTHESIS ARCHITECT (executes third, depends on C and B)
  Purpose: Confirm all invariants registered.
  invariant_registry_confirmed: [true when all four invariants registered]
  depends on: incumbent_threat_locked (ROLE C) and gate_s_cleared (ROLE B)
  note: ROLE A cannot execute until ROLE C and ROLE B are both complete.

---

## RESUME AUDIT

Run before Stage 0. Check all five stage artifact paths on disk.

For each stage, record found (Y/N) and decision (RESUME-SKIP or RUN):

1. Stage 1 — {topic}-hypothesis-{date}.md:    found=[Y/N]  decision=[RESUME-SKIP / RUN]
2. Stage 2 — {topic}-websearch-{date}.md:      found=[Y/N]  decision=[RESUME-SKIP / RUN]
3. Stage 3 — {topic}-interview-{date}.md:      found=[Y/N]  decision=[RESUME-SKIP / RUN]
4. Stage 4 — {topic}-prototype-{date}.md:      found=[Y/N]  decision=[RESUME-SKIP / RUN]
5. Stage 5 — {topic}-synthesis-{date}.md:      found=[Y/N]  decision=[RESUME-SKIP / RUN]

  resume_audit_complete: [true]
  stages_to_run: [list of RUN stages]

If all five RESUME-SKIP: "RESUME_AUDIT_EXIT — All artifacts present. STOP."
Otherwise: "RESUME_AUDIT_PASS — Running: [list]. Proceeding to Stage 0."

---

## STAGE 0 — GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] RESUME AUDIT complete — resume_audit_complete = true
  [ ] CAMPAIGN OPEN, INCUMBENT ANCHOR, DISPLACEMENT THESIS filled
  [ ] All four SESSION INVARIANTS registered
  [ ] ROLE C complete — incumbent_threat_locked = true
  [ ] ROLE B complete — gate_s_cleared = true
  [ ] ROLE A complete — invariant_registry_confirmed = true

STAGE 0 BODY:

Clearance check — record confirm or BLOCKED for each:

  Step 1: incumbent_threat_locked (ROLE C)          = [confirm or BLOCKED]
  Step 2: gate_s_cleared (ROLE B)                   = [confirm or BLOCKED]
  Step 3: invariant_registry_confirmed (ROLE A)     = [confirm or BLOCKED]
  Step 4: displacement_thesis_filed                 = [confirm or BLOCKED]

First BLOCKED step halts campaign.

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open — All steps confirmed. Displacement thesis active.
   SESSION INVARIANT D registered. Advancing to Stage 1."

---

## STAGE 1 — HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] STAGE 0 EXIT: gate_open received
  [ ] RESUME AUDIT: Stage 1 = RUN (skip if RESUME-SKIP)
  [ ] scout_artifact path available from ROLE B
  [ ] DISPLACEMENT THESIS active

STAGE 1 BODY:

Load scout artifact. Frame hypothesis against displacement question.

  source_scout_artifact:   [path from ROLE B — not inferred]
  displacement_context:    [how scout findings inform the displacement thesis]
  hypothesis:              [falsifiable claim: {topic} can displace {status_quo_comparator}
                            in [specific domain] because [mechanism]]
  counter_hypothesis:      [incumbent's strongest defense — why it holds despite {topic}]
  confidence_prior:        [1–10]

Write artifact: {topic}-hypothesis-{date}.md. Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked(confidence_prior=[value])
  "STAGE 1 EXIT: hypothesis_locked — {topic}-hypothesis-{date}.md written.
   confidence_prior=[value]. Displacement hypothesis active. Stage 2 ready."

---

## STAGE 2 — WEB SEARCH

STAGE DISPLACEMENT QUESTION: "Does external evidence support displacement of
{status_quo_comparator} by {topic}?"

STAGE 2 ENTRY CONDITIONS:
  [ ] STAGE 1 EXIT: hypothesis_locked received
  [ ] RESUME AUDIT: Stage 2 = RUN (skip if RESUME-SKIP)
  [ ] hypothesis artifact confirmed written
  [ ] INVARIANT D Stage 2 template active

STAGE 2 BODY:

Gather minimum 5 external sources. For each, record:

  Source N:
    url_or_citation: [source]
    summary:         [1 sentence]
    verdict:         "Does [item N] support displacement of {status_quo_comparator}
                      by {topic} on [dimension]? [Yes / No / Inconclusive]"

After all sources:

  s2_count:                      [N — must be >= 5]
  s2_incumbent_check_summary:    [N support / M counter / P inconclusive]
  s2_stage_displacement_verdict: [SUPPORTING / MIXED / OPPOSING]
  s2_ce_verdict:                 [null if no CE; cite item if found]
  confidence_delta_s2:           [+1 / 0 / -1]
  running_confidence:            [prior + delta]

Running null tally: "Running tally: [N] null across 1 stage complete. 2 remain."

GATE: Do not fire exit signal until s2_count >= 5. If s2_count < 5, gather
additional sources before proceeding.

Write artifact: {topic}-websearch-{date}.md. Confirm write.

STAGE 2 EXIT SIGNAL: websearch_complete(count=[N], running_confidence=[value])
  "STAGE 2 EXIT: websearch_complete — s2_stage_displacement_verdict=[value].
   s2_ce_verdict=[value]. s2_count=[N] (gate >= 5 met). running_confidence=[value].
   Stage 3 ready."

---

## STAGE 3 — INTERVIEW

STAGE DISPLACEMENT QUESTION: "Do practitioners confirm a viable path from
{status_quo_comparator} to {topic}?"

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT: websearch_complete received
  [ ] RESUME AUDIT: Stage 3 = RUN (skip if RESUME-SKIP)
  [ ] s2_ce_verdict recorded
  [ ] INVARIANT D Stage 3 template active

STAGE 3 BODY:

Simulate minimum 3 practitioner interviews. For each, record:

  Practitioner N:
    type:    [practitioner type]
    account: [key quote or paraphrase — 1 sentence]
    verdict: "Does [account N] reveal a viable transition path from {status_quo_comparator}
              to {topic} for [use case]? [Yes / No / Inconclusive]"

After all interviews:

  s3_count:                      [N — must be >= 3]
  s3_incumbent_check_summary:    [N support / M counter / P inconclusive]
  s3_stage_displacement_verdict: [SUPPORTING / MIXED / OPPOSING]
  s3_ce_verdict:                 [null if no CE; cite account if found]
  confidence_delta_s3:           [+1 / 0 / -1]
  running_confidence:            [prev + delta]

Running null tally: "Running tally: [N] null across 2 stages complete. 1 remains."

GATE: Do not fire exit signal until s3_count >= 3. If s3_count < 3, simulate
additional interviews before proceeding.

Write artifact: {topic}-interview-{date}.md. Confirm write.

STAGE 3 EXIT SIGNAL: interview_complete(count=[N], running_confidence=[value])
  "STAGE 3 EXIT: interview_complete — s3_stage_displacement_verdict=[value].
   s3_ce_verdict=[value]. s3_count=[N] (gate >= 3 met). running_confidence=[value].
   Stage 4 ready."

---

## STAGE 4 — PROTOTYPE

STAGE DISPLACEMENT QUESTION: "Does prototype evidence make a credible case for
displacing {status_quo_comparator} with {topic}?"

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT: interview_complete received
  [ ] RESUME AUDIT: Stage 4 = RUN (skip if RESUME-SKIP)
  [ ] s3_ce_verdict recorded
  [ ] INVARIANT D Stage 4 template active

STAGE 4 BODY:

Design and assess minimum 3 experiments. For each, record:

  Experiment N:
    design:  [what was built/tested — 1 sentence]
    result:  [what was learned — 1-2 sentences]
    verdict: "Does [result N] make a credible case for displacing {status_quo_comparator}
              with {topic}? [Yes / No / Pending]"

After all experiments:

  s4_count:                      [N — must be >= 3]
  s4_stage_displacement_verdict: [SUPPORTED / PARTIALLY / UNSUPPORTED]
  s4_displacement_verdict:       [Yes / No / Pending — required; omission = format error]
  s4_ce_verdict:                 [null if no CE]
  confidence_delta_s4:           [+1 / 0 / -1]
  running_confidence:            [prev + delta]

Final null tally:
  null_tally_final = [N]
  Cross-check: count from Stage 3 was [M]. Final [N]. Match: [true/false].

GATE: Do not fire exit signal until s4_count >= 3. If s4_count < 3, design
additional experiments before proceeding.

Write artifact: {topic}-prototype-{date}.md. Confirm write.

STAGE 4 EXIT SIGNAL: prototype_complete(count=[null_tally_final], running_confidence=[value])
  "STAGE 4 EXIT: prototype_complete — s4_stage_displacement_verdict=[value].
   s4_ce_verdict=[value]. null_tally_final=[N]. running_confidence=[value]. Stage 5 ready."

---

## STAGE 5 — SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT: prototype_complete received
  [ ] RESUME AUDIT: Stage 5 = RUN (skip if RESUME-SKIP)
  [ ] null_tally_final recorded
  [ ] counter_hypothesis from Stage 1 present
  [ ] All four SESSION INVARIANTS active

SYNTHESIS BEGINS WITH DISPLACEMENT ANSWER.
SYNTHESIS HARD GATE: no synthesis fields until BLOCK 3 COMPLETE.

STAGE 5 BODY: THREE-BLOCK STRUCTURE.

### BLOCK 1 — CONFIDENCE CHAIN RESOLUTION

  confidence_prior:          [value from Stage 1]
  confidence_delta_s2:       [from Stage 2]
  confidence_delta_s3:       [from Stage 3]
  confidence_delta_s4:       [from Stage 4]
  chain_equation:            prior + s2 + s3 + s4 = [sum]
  null_cap_applied:          [yes — -= 2 — if null_tally_final >= 3; no otherwise]
  confidence_chain_resolved: [final after cap]

BLOCK 1 COMPLETE: "BLOCK 1 COMPLETE — confidence_chain_resolved = [value]."

### BLOCK 2 — COUNTER-HYPOTHESIS RESOLUTION

For each counter-hypothesis item from Stage 1, record:

  Item N:
    text:     [counter-hypothesis]
    verdict:  [REFUTED / PARTIALLY REFUTED / OPEN RISK]
    evidence: [cite stage artifact]

  open_risk_count:            [N]
  cr_delta:                   [N * -1]
  confidence_post_cr:         [confidence_chain_resolved + cr_delta]
  counter_hypothesis_verdict: [recorded]

BLOCK 2 COMPLETE: "BLOCK 2 COMPLETE — confidence_post_cr = [value]."

### BLOCK 3 — DISPLACEMENT INTEGRITY CHECK

Requires BLOCK 1 COMPLETE and BLOCK 2 COMPLETE before beginning.

ATOMIC DUAL-LOCK:

  Null tally reconstruction:
    s2_ce_verdict: [null or value]
    s3_ce_verdict: [null or value]
    s4_ce_verdict: [null or value]
    null_tally_final = [N]
    Cross-check vs Stage 4 exit: [Match / Mismatch]

  If null_tally_final >= 3:
    Lock 1 (INVARIANT A): adversarial review by [type]. Synthesis BLOCKED until complete.
    Lock 2 (INVARIANT B): confidence_composite = confidence_post_cr - 2.
    co_activation_confirmed: dual_lock_fired
  Else:
    co_activation_confirmed: not_triggered
    confidence_composite:    [confidence_post_cr]

  displacement_per_stage:  S2=[value], S3=[value], S4=[value]
  displacement_conclusion: [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  consistency_flag:        [CONSISTENT / INCONSISTENT]
  incumbent_defense_closed: [true/false — incumbent_vulnerability addressed by S2+S3+S4]

BLOCK 3 COMPLETE: "BLOCK 3 COMPLETE — displacement_conclusion=[value].
  Per-stage: S2=[v], S3=[v], S4=[v]. incumbent_defense_closed=[value]."

### SYNTHESIS BODY

(Not populated until BLOCK 3 COMPLETE.)

  displacement_conclusion:  [from BLOCK 3 — LEADS synthesis]
  hypothesis_verdict:       [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:         [2-3 sentences: open with displacement conclusion, then
                             hypothesis verdict, then confidence trajectory]
  confidence_composite:     [final — confidence_post_cr after all caps]
  key_risk:                 [primary adoption risk — residual incumbent strength]
  topic_story_readiness:    "Displacement case for {topic} over {status_quo_comparator}:
                             [displacement_conclusion]. Hypothesis: [hypothesis_verdict].
                             Confidence: [value]. Ready for /topic-story."

### HANDOFF

SESSION INVARIANT C enforced. All fields carry [derived from: X]. Unlabeled = error.

  scout_anchor:                [value]  [derived from: ROLE B scout load]
  incumbent_threat_locked:     [true]   [derived from: ROLE C analysis]
  hypothesis:                  [value]  [derived from: Stage 1 artifact]
  counter_hypothesis:          [value]  [derived from: Stage 1 artifact]
  s2_ce_verdict:               [value]  [derived from: Stage 2 artifact]
  s3_ce_verdict:               [value]  [derived from: Stage 3 artifact]
  s4_ce_verdict:               [value]  [derived from: Stage 4 artifact]
  null_tally_final:            [N]      [derived from: s2+s3+s4 verdicts] [not through co_activation]
  co_activation_confirmed:     [value]  [derived from: ATOMIC DUAL-LOCK] [not through incumbent_defense]
  incumbent_defense_closed:    [t/f]    [derived from: BLOCK 3 closure] [not through co_activation]
  confidence_composite:        [value]  [derived from: Stage 5 synthesis] [capped by INVARIANT B]
  schema_compliance_confirmed: [true]   [all 11 fields present and sourced]

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete — Displacement case: [displacement_conclusion].
   Hypothesis: [hypothesis_verdict]. Confidence: [confidence_composite].
   Evidence brief ready for topic-story."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## V-05 — Full Integration (All Three Axes + Complete Structural Stack)

**Axes**: output_format + inertia_framing + lifecycle_emphasis + full R19 baseline
**Hypothesis**: V-01 (inline format), V-02 (displacement thesis as narrative lead), and
V-03 (compressed setup / expanded Stage 5) address different rubric criteria at different
points in the prompt. If all three improvements hold independently and their combination
does not produce conflicting constraints, V-05 should satisfy all 10 v14 rubric criteria:
inline format preserves structural compliance; displacement thesis framing strengthens
C-02/C-05; compressed setup reduces noise before Stage 5; expanded Stage 5 with per-block
entry conditions and explicit compute steps produces the clearest synthesis_complete exit
signal and handoff package recognizable to /topic-story.

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

### DISPLACEMENT THESIS

State before roles run. Drives the entire campaign.

  displacement_question:  "Can {topic} displace {status_quo_comparator} as the dominant
                           approach for [problem domain]?"
  why_change_is_needed:   [one sentence: gap the incumbent leaves that {topic} fills]
  displacement_bar:       "Campaign succeeds when three evidence stages independently support
                           displacement AND confidence_composite >= [threshold]."

### SESSION INVARIANTS

Four invariants. All carry: cannot be modified or bypassed at any subsequent stage.

1. INVARIANT D — INCUMBENT CHECK PHRASING REGISTER
   Stage 2 template: "Does [evidence item] support the displacement of {status_quo_comparator}
     by {topic} on [dimension]? [Yes / No / Inconclusive]"
   Stage 3 template: "Does [practitioner account] reveal a viable transition path from
     {status_quo_comparator} to {topic} for [use case]? [Yes / No / Inconclusive]"
   Stage 4 template: "Does [prototype result] make a credible case for displacing
     {status_quo_comparator} with {topic}? [Yes / No / Pending]"
   Enforcement: Template deviation = format error. Cannot be modified.

2. INVARIANT A — ADVERSARIAL REVIEWER TYPE
   adversarial_reviewer_type: [role most likely to challenge displacement]
   Activation: null_tally_final >= 3.

3. INVARIANT B — CONFIDENCE CAP
   null_ce_cap_rule: confidence_composite -= 2 if null_tally_final >= 3 (hard cap).

4. INVARIANT C — DERIVATION ANNOTATION
   annotation_rule: Every handoff field carries [derived from: X]. Unlabeled = format error.

### ROLE OWNERSHIP

Three roles. Execute in sequence C -> B -> A. ROLE A depends on C and B outputs.

ROLE C — INCUMBENT THREAT ANALYST (executes first, no dependencies)
  Reads INCUMBENT ANCHOR and DISPLACEMENT THESIS.
  incumbent_threat_locked: [true when incumbent analysis complete]

ROLE B — SCOUT LOADER (executes second, no dependencies)
  scout_artifact:  [{topic}-scout-record-{date}.md or equivalent]
  scout_loaded:    [true / false]
  gate_s_cleared:  [true if scout_loaded; CAMPAIGN BLOCKED otherwise]

ROLE A — HYPOTHESIS ARCHITECT (executes third, depends on C and B)
  invariant_registry_confirmed: [true when all four invariants registered]
  depends on: incumbent_threat_locked (ROLE C) and gate_s_cleared (ROLE B)
  execution note: ROLE A blocked until ROLE C and ROLE B complete.

---

## RESUME AUDIT

Run before Stage 0. For each stage artifact, record found and decision:

1. Stage 1 — {topic}-hypothesis-{date}.md:    found=[Y/N]  decision=[RESUME-SKIP / RUN]
2. Stage 2 — {topic}-websearch-{date}.md:      found=[Y/N]  decision=[RESUME-SKIP / RUN]
3. Stage 3 — {topic}-interview-{date}.md:      found=[Y/N]  decision=[RESUME-SKIP / RUN]
4. Stage 4 — {topic}-prototype-{date}.md:      found=[Y/N]  decision=[RESUME-SKIP / RUN]
5. Stage 5 — {topic}-synthesis-{date}.md:      found=[Y/N]  decision=[RESUME-SKIP / RUN]

  resume_audit_complete: [true]
  stages_to_run:         [list]

If all RESUME-SKIP: "RESUME_AUDIT_EXIT — All artifacts present. STOP."
Otherwise: "RESUME_AUDIT_PASS — Running: [list]."

---

## STAGE 0 — GATE S (compressed)

Pre-flight checklist. If any item false: "CAMPAIGN BLOCKED at item [N]."

  [ ] CAMPAIGN OPEN, INCUMBENT ANCHOR, DISPLACEMENT THESIS filled
  [ ] All four SESSION INVARIANTS registered
  [ ] incumbent_threat_locked = true (ROLE C)
  [ ] gate_s_cleared = true (ROLE B)
  [ ] invariant_registry_confirmed = true (ROLE A)
  [ ] displacement_thesis_filed = true

If all true: "STAGE 0 EXIT: gate_open — Displacement thesis active. Advancing to Stage 1."

---

## STAGE 1 — HYPOTHESIS (compressed)

Skip if RESUME-SKIP. Load scout artifact. Frame hypothesis against displacement question.

  source_scout_artifact:   [path from ROLE B — not inferred]
  displacement_context:    [how scout findings inform the displacement thesis]
  hypothesis:              [falsifiable claim: {topic} displaces {status_quo_comparator}
                            in [domain] because [mechanism]]
  counter_hypothesis:      [incumbent's strongest defense — grounds BLOCK 2 resolution]
  confidence_prior:        [1–10]

Write {topic}-hypothesis-{date}.md. Confirm write.
EXIT: "STAGE 1 EXIT: hypothesis_locked(confidence_prior=[value]) — Stage 2 ready."

---

## STAGE 2 — WEB SEARCH (compressed)

STAGE DISPLACEMENT QUESTION: "Does external evidence support displacement of
{status_quo_comparator} by {topic}?"

Skip if RESUME-SKIP. Gather minimum 5 sources. Apply INVARIANT D Stage 2 template verbatim.

  Source N:
    citation: [url or reference]
    summary:  [1 sentence]
    verdict:  "Does [item N] support displacement of {status_quo_comparator} by {topic}
               on [dimension]? [Yes / No / Inconclusive]"

  s2_count >= 5 required.
  s2_incumbent_check_summary:    [N support / M counter / P inconclusive]
  s2_stage_displacement_verdict: [SUPPORTING / MIXED / OPPOSING]
  s2_ce_verdict:                 [null / value]
  confidence_delta_s2:           [+1 / 0 / -1]
  running_confidence:            [prior + delta]
  null tally:                    "Running tally: [N] null, 1 stage done, 2 remain."

GATE: Do not fire exit signal until s2_count >= 5.
Write {topic}-websearch-{date}.md.
EXIT: "STAGE 2 EXIT: websearch_complete(count=[N], running_confidence=[value]) — Stage 3 ready."

---

## STAGE 3 — INTERVIEW (compressed)

STAGE DISPLACEMENT QUESTION: "Do practitioners confirm a viable path from
{status_quo_comparator} to {topic}?"

Skip if RESUME-SKIP. Simulate minimum 3 practitioners. Apply INVARIANT D Stage 3 template.

  Practitioner N:
    type:    [practitioner type]
    account: [1-sentence quote or paraphrase]
    verdict: "Does [account N] reveal a viable transition path from {status_quo_comparator}
              to {topic} for [use case]? [Yes / No / Inconclusive]"

  s3_count >= 3 required.
  s3_incumbent_check_summary:    [N support / M counter / P inconclusive]
  s3_stage_displacement_verdict: [SUPPORTING / MIXED / OPPOSING]
  s3_ce_verdict:                 [null / value]
  confidence_delta_s3:           [+1 / 0 / -1]
  running_confidence:            [prev + delta]
  null tally:                    "Running tally: [N] null, 2 stages done, 1 remains."

GATE: Do not fire exit signal until s3_count >= 3.
Write {topic}-interview-{date}.md.
EXIT: "STAGE 3 EXIT: interview_complete(count=[N], running_confidence=[value]) — Stage 4 ready."

---

## STAGE 4 — PROTOTYPE (compressed)

STAGE DISPLACEMENT QUESTION: "Does prototype evidence make a credible case for
displacing {status_quo_comparator} with {topic}?"

Skip if RESUME-SKIP. Design minimum 3 experiments. Apply INVARIANT D Stage 4 template.

  Experiment N:
    design:  [1 sentence]
    result:  [1-2 sentences]
    verdict: "Does [result N] make a credible case for displacing {status_quo_comparator}
              with {topic}? [Yes / No / Pending]"

  s4_count >= 3 required.
  s4_stage_displacement_verdict: [SUPPORTED / PARTIALLY / UNSUPPORTED]
  s4_displacement_verdict:       [Yes / No / Pending — required; omission = format error]
  s4_ce_verdict:                 [null / value]
  confidence_delta_s4:           [+1 / 0 / -1]
  running_confidence:            [prev + delta]
  null_tally_final = [N]
  Cross-check: count from Stage 3 was [M]. Final [N]. Match: [true/false].

GATE: Do not fire exit signal until s4_count >= 3.
Write {topic}-prototype-{date}.md.
EXIT: "STAGE 4 EXIT: prototype_complete(count=[null_tally_final], running_confidence=[value]) — Stage 5 ready."

---

## STAGE 5 — SYNTHESIS (expanded)

SYNTHESIS BEGINS WITH DISPLACEMENT ANSWER.
SYNTHESIS HARD GATE: no synthesis fields populated until BLOCK 3 COMPLETE received.

---

### BLOCK 1 — CONFIDENCE CHAIN RESOLUTION

BLOCK 1 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT received: prototype_complete
  [ ] confidence_prior available from Stage 1 artifact
  [ ] Stage deltas (s2, s3, s4) available from respective artifacts
  [ ] null_tally_final confirmed from Stage 4 exit signal

BLOCK 1 COMPUTE:

  confidence_prior (read from {topic}-hypothesis-{date}.md): [value]
  delta_s2: [value]    delta_s3: [value]    delta_s4: [value]
  chain_equation:            [prior] + [s2] + [s3] + [s4] = [raw_sum]
  null_cap_applies:          [yes if null_tally_final >= 3; no otherwise]
  cap_deduction:             [2 if yes; 0 if no]
  confidence_chain_resolved: [raw_sum - cap_deduction]
  chain_integrity_check:     [raw_sum matches running_confidence at Stage 4 close: yes/no]

BLOCK 1 COMPLETE: "BLOCK 1 COMPLETE — confidence_chain_resolved = [value].
  Cap applied: [yes/no]. Chain integrity: [ok / discrepancy]."

---

### BLOCK 2 — COUNTER-HYPOTHESIS RESOLUTION

BLOCK 2 ENTRY CONDITIONS:
  [ ] BLOCK 1 COMPLETE received
  [ ] counter_hypothesis available from Stage 1 artifact
  [ ] confidence_chain_resolved carried forward from BLOCK 1

BLOCK 2 COMPUTE:

Read counter_hypothesis from {topic}-hypothesis-{date}.md.

  Counter-hypothesis N:
    text:     [text]
    verdict:  [REFUTED / PARTIALLY REFUTED / OPEN RISK]
    evidence: [cite stage artifact that determines verdict]

  open_risk_count:            [N]
  refuted_count:              [M]
  cr_delta:                   [open_risk_count * -1]
  confidence_post_cr:         [confidence_chain_resolved + cr_delta]
  counter_hypothesis_verdict: [recorded — all items resolved]

BLOCK 2 COMPLETE: "BLOCK 2 COMPLETE — counter_hypothesis_verdict recorded.
  open_risk_count=[N]. confidence_post_cr=[value]."

---

### BLOCK 3 — DISPLACEMENT INTEGRITY CHECK

BLOCK 3 ENTRY CONDITIONS:
  [ ] BLOCK 1 COMPLETE received — confidence_chain_resolved = [value]
  [ ] BLOCK 2 COMPLETE received — counter_hypothesis_verdict recorded, confidence_post_cr = [value]

BLOCK 3 COMPUTE:

Step 1 — ATOMIC DUAL-LOCK (null tally reconstruction):
  s2_ce_verdict (from {topic}-websearch-{date}.md):  [null / value]
  s3_ce_verdict (from {topic}-interview-{date}.md):  [null / value]
  s4_ce_verdict (from {topic}-prototype-{date}.md):  [null / value]
  null_tally_reconstructed:    [count of non-null]
  null_tally_final_from_exit:  [N from Stage 4 exit]
  tally_cross_check:           [Match / Mismatch — Mismatch = integrity failure before synthesis]

  If null_tally_final >= 3:
    Lock 1 — adversarial_reviewer_type: [type]. Adversarial review required. BLOCKED until done.
    Lock 2 — confidence_composite: confidence_post_cr - 2 (hard cap — cannot be overridden).
    co_activation_confirmed: dual_lock_fired
  Else:
    co_activation_confirmed: not_triggered
    confidence_composite:    [confidence_post_cr]

Step 2 — Displacement conclusion:
  displacement_per_stage:  S2=[s2_stage_displacement_verdict], S3=[s3_stage_displacement_verdict], S4=[s4_stage_displacement_verdict]
  displacement_conclusion: [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED — final answer to displacement_question]
  s4_displacement_verdict_confirmed: [value from {topic}-prototype-{date}.md]
  consistency_flag: [CONSISTENT / INCONSISTENT — displacement_conclusion vs s4_displacement_verdict]
  If INCONSISTENT: record reconciliation justification before proceeding.

Step 3 — Incumbent defense closure:
  incumbent_defense_closed: [true if S2+S3+S4 incumbent checks collectively address
                             incumbent_vulnerability identified by ROLE C; false otherwise]
  closure_basis: [cite S2, S3, S4 incumbent check summaries]

BLOCK 3 COMPLETE: "BLOCK 3 COMPLETE — displacement_conclusion=[value].
  Per-stage: S2=[v], S3=[v], S4=[v]. incumbent_defense_closed=[value].
  co_activation_confirmed=[value]. consistency_flag=[value]."

---

### SYNTHESIS BODY

SYNTHESIS GATE CHECK: [ ] BLOCK 3 COMPLETE received. If not: SYNTHESIS BLOCKED.

SYNTHESIS LEADS WITH DISPLACEMENT ANSWER:

  displacement_conclusion:  [from BLOCK 3 — state first]
  hypothesis_verdict:       [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:         [2-3 sentences: open with displacement verdict, then hypothesis
                             assessment, then confidence trajectory across S2-S4]
  confidence_composite:     [final — from BLOCK 3 after all reductions and caps]
  key_risk:                 [primary adoption risk — framed as residual incumbent strength
                             from incumbent_vulnerability analysis]
  topic_story_readiness:    "Displacement case for {topic} over {status_quo_comparator}:
                             [displacement_conclusion]. Hypothesis [hypothesis_verdict].
                             Confidence [value]. Five stage artifacts written.
                             Evidence brief ready for /topic-story."

### HANDOFF

SESSION INVARIANT C enforced. All fields carry [derived from: X]. Unlabeled = format error.

  scout_anchor:                [value]  [derived from: ROLE B scout load]
  incumbent_threat_locked:     [true]   [derived from: ROLE C analysis]
  hypothesis:                  [value]  [derived from: Stage 1 artifact]
  counter_hypothesis:          [value]  [derived from: Stage 1 artifact]
  s2_ce_verdict:               [value]  [derived from: Stage 2 artifact]
  s3_ce_verdict:               [value]  [derived from: Stage 3 artifact]
  s4_ce_verdict:               [value]  [derived from: Stage 4 artifact]
  null_tally_final:            [N]      [derived from: BLOCK 3 reconstruction] [not through co_activation]
  co_activation_confirmed:     [value]  [derived from: ATOMIC DUAL-LOCK] [not through incumbent_defense]
  incumbent_defense_closed:    [t/f]    [derived from: BLOCK 3 closure check] [not through co_activation]
  confidence_composite:        [value]  [derived from: BLOCK 3 after all caps] [capped by INVARIANT B]
  schema_compliance_confirmed: [true]   [all 11 fields present and sourced]

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete — Displacement conclusion: [displacement_conclusion].
   Hypothesis verdict: [hypothesis_verdict]. Confidence: [confidence_composite].
   Incumbent defense closed: [true/false]. Five stage artifacts on disk.
   Evidence brief complete. Ready for /topic-story."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```
