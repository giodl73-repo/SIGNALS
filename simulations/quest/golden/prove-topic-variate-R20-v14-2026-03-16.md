---
skill: quest-variate
skill_target: prove-topic
round: R20
date: 2026-03-16
rubric: prove-topic-rubric-v14-2026-03-16.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [phrasing_register, role_sequence, evidence_quality_mandatory]
  combined: [V-04 (phrasing_register + role_sequence), V-05 (all_three + full_R19_baseline)]
r19_anchor: >
  R19 V-05 (all_three + full_structural_stack) is the structural floor for R20. It includes:
  RESUME AUDIT block, ROLE OWNERSHIP TABLE with dependency annotations (C -> B -> A),
  SESSION INVARIANTS TABLE (D/A/B/C), count-gated exits (S2 >= 5, S3 >= 3, S4 >= 3),
  confidence_delta chain across stages, three-block Stage 5 (BLOCK 1 confidence chain /
  BLOCK 2 counter-hypothesis / BLOCK 3 ATOMIC DUAL-LOCK), HANDOFF TABLE with derivation
  annotations enforced by SESSION INVARIANT C.
r20_context: >
  R19 explored output_format, inertia_framing, lifecycle_emphasis. v14 rubric has 10
  criteria (5 essential C-01 to C-05, 3 recommended C-06 to C-08, 2 aspirational C-09
  to C-10). Remaining unprobed surface areas for v14:

  C-08 (evidence gaps flagged at point of discovery) and C-09 (thin-evidence propagates
  to synthesis with confidence qualification) are recommended/aspirational but consistently
  partial: evidence quality is observed by the model but not structurally forced. A
  mandatory evidence_quality field per evidence stage with carry-forward rule addresses
  this without restructuring the whole prompt.

  C-10 (hypothesis structurally blocked until scout confirmation recorded) is aspirational.
  The current ROLE B mechanism names the scout artifact but the blocking behavior depends
  on ROLE B executing in the right sequence. Making ROLE B the PRIMARY EXECUTION GATE (runs
  before all others, halts immediately if scout absent) converts a named-anchor pattern into
  a structural block.

  phrasing_register is unexplored: the current prompt uses mixed formal/passive imperatives
  ("Fill before any role", "Confirms analysis complete"). Second-person direct register
  ("You fill this before any role", "You confirm the analysis is complete") may improve
  model execution fidelity by reducing ambiguity about who performs each action.

  Axis summary:
    V-01 (single: phrasing_register): formal passive -> second-person direct throughout.
    V-02 (single: role_sequence): ROLE B executes first as primary blocking gate; ROLE C
      and ROLE A cannot execute until ROLE B clears gate_s_cleared. Stage 0 clearance
      steps reordered to match execution dependency.
    V-03 (single: evidence_quality_mandatory): mandatory evidence_quality field at each
      evidence stage (S2, S3, S4); Stage 5 opens with THIN-EVIDENCE CARRY block that
      names each thin stage, the claim weakened, and the confidence penalty carried forward.
    V-04 (combined: phrasing_register + role_sequence): V-01 + V-02.
    V-05 (full: all three + complete R19 V-05 baseline stack).
---

# prove-topic Variations -- Round 20 (rubric v14)

**Skill**: prove-topic
**Rubric**: v14 (C-01 to C-05 essential, C-06 to C-08 recommended, C-09 to C-10 aspirational)
**Date**: 2026-03-16
**Round**: R20

---

## Context: what informed this round

R19 explored three axes against the v14 rubric. R20 explores the three remaining uncovered axes:

| Axis | What it changes | Primary criterion target |
|------|-----------------|--------------------------|
| phrasing_register | formal passive -> second-person direct | C-01 (execution fidelity), C-03 (write instruction clarity) |
| role_sequence | ROLE B runs first as blocking gate owner | C-10 (structural block until scout confirmed), C-06 (gate enforces scout presence) |
| evidence_quality_mandatory | mandatory quality rating per evidence stage + carry-forward | C-08 (gaps flagged at discovery), C-09 (thin-evidence to synthesis) |

---

## V-01 -- Phrasing Register (Formal Passive to Second-Person Direct)

**Axis**: phrasing_register (single)
**Hypothesis**: The current prompt uses formal passive or third-person imperatives ("Fill before
any role", "Confirms analysis complete", "Cannot be modified or bypassed"). These phrasings create
ambiguity: it is not always clear whether an instruction targets the model executing the skill or
describes a structural constraint. Switching to second-person direct ("You fill this before any
role", "You confirm the analysis is complete", "You cannot modify or bypass this") removes that
ambiguity while keeping all structural elements, entry conditions, tables, and exit signals
identical. If execution fidelity on C-03 (progressive artifact writes) and C-01 (stage sequence)
depends on instruction clarity rather than structure, this variation should improve those without
any structural cost. The risk: second-person phrasing may feel redundant in the body sections
where the model already implicitly understands it is the actor.

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
ENTRY CONDITIONS and a named EXIT SIGNAL. You do not begin any stage body until entry
conditions confirm.

---

## CAMPAIGN OPEN

  topic:                 {topic}
  date:                  {date}
  status_quo_comparator: [you name the incumbent approach this topic must displace]

### INCUMBENT ANCHOR

You fill this section before you run any role or register any invariant.

  incumbent_name:          [full name of status_quo_comparator]
  incumbent_strength:      [one sentence: why the incumbent is currently winning]
  incumbent_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]

### SESSION INVARIANTS TABLE

SESSION INVARIANT D leads. You register all four before any role executes. Each carries:
"you cannot modify or bypass this at any subsequent stage."

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
       |                           | You cannot modify or bypass this at any stage.
  -----|---------------------------|------------------------------------------------------
  A    | ADVERSARIAL REVIEWER      | adversarial_reviewer_type: [the role most likely to
       | TYPE                      |   challenge the displacement claim].
       |                           | Activation: null_tally_final >= 3.
       |                           | You cannot modify or bypass this at synthesis.
  -----|---------------------------|------------------------------------------------------
  B    | CONFIDENCE CAP            | null_ce_cap_rule: confidence_composite -= 2 if
       |                           |   null_tally_final >= 3 (hard cap).
       |                           | You cannot soften or override this at synthesis.
  -----|---------------------------|------------------------------------------------------
  C    | DERIVATION ANNOTATION     | annotation_rule: Every handoff field you write carries
       |                           |   [derived from: X]. Unlabeled = format error.
       |                           | You cannot modify or bypass this at synthesis.

### ROLE OWNERSHIP TABLE

You execute ROLE C first, then ROLE B, then ROLE A before Stage 0 begins.

  ROLE   | TITLE                    | OWNED FIELD               | DEPENDENCY
  -------|--------------------------|---------------------------|---------------------------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked   | none
  ROLE B | SCOUT LOADER             | gate_s_cleared            | none
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | depends on C and B

ROLE C (you execute now):
  You read the INCUMBENT ANCHOR above. You confirm the analysis is complete.
  incumbent_threat_locked: [true when incumbent_name, strength, vulnerability all filled]

ROLE B (you execute now):
  scout_artifact:  [{topic}-scout-record-{date}.md or equivalent]
  scout_loaded:    [true / false]
  gate_s_cleared:  [true if scout_loaded; CAMPAIGN BLOCKED otherwise]

ROLE A (you execute now):
  You confirm all four SESSION INVARIANT TABLE rows are filled and active.
  invariant_registry_confirmed: [true when all four invariants registered]
  You cannot set this to true until ROLE C and ROLE B have both completed.

---

## RESUME AUDIT

You run this before Stage 0. You glob existing artifacts for {topic} on {date}.

For each stage artifact, you record: FOUND (Y/N) and DECISION (RESUME-SKIP / RUN).

1. Stage 1 -- {topic}-hypothesis-{date}.md:   found=[Y/N]  decision=[RESUME-SKIP / RUN]
2. Stage 2 -- {topic}-websearch-{date}.md:    found=[Y/N]  decision=[RESUME-SKIP / RUN]
3. Stage 3 -- {topic}-interview-{date}.md:    found=[Y/N]  decision=[RESUME-SKIP / RUN]
4. Stage 4 -- {topic}-prototype-{date}.md:    found=[Y/N]  decision=[RESUME-SKIP / RUN]
5. Stage 5 -- {topic}-synthesis-{date}.md:    found=[Y/N]  decision=[RESUME-SKIP / RUN]

  resume_audit_complete: [true]
  stages_to_run:         [list stages with RUN decision, or ALL if none found]

RESUME AUDIT EXIT: If all five stages are RESUME-SKIP, you emit:
  "RESUME_AUDIT_EXIT -- All stage artifacts already present. Campaign complete. No stages re-run."
  and you STOP. Otherwise: "RESUME_AUDIT_PASS -- Stages to run: [list]. Proceeding to Stage 0."

---

## STAGE 0 -- GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] RESUME AUDIT completed -- resume_audit_complete = true
  [ ] CAMPAIGN OPEN fields filled (topic, date, status_quo_comparator)
  [ ] INCUMBENT ANCHOR filled (incumbent_name, strength, vulnerability)
  [ ] All four SESSION INVARIANTS registered
  [ ] ROLE C executed -- incumbent_threat_locked = true
  [ ] ROLE B executed -- scout_artifact identified, scout_loaded confirmed
  [ ] ROLE A executed -- invariant_registry_confirmed = true

STAGE 0 BODY:

You check clearance for each step and record confirm or BLOCKED:
  Step 1: incumbent_threat_locked (ROLE C required) = [confirm or BLOCKED]
  Step 2: gate_s_cleared (ROLE B required)          = [confirm or BLOCKED]
  Step 3: invariant_registry_confirmed (ROLE A)     = [confirm or BLOCKED]

The first BLOCKED step halts the campaign. You record the step number and owning role.

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open -- Steps 1, 2, 3 all confirmed. SESSION INVARIANT D active.
   Advancing to Stage 1."

---

## STAGE 1 -- HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] STAGE 0 EXIT SIGNAL received: gate_open
  [ ] RESUME AUDIT: Stage 1 decision = RUN (you skip entire stage body if RESUME-SKIP)
  [ ] scout_artifact path available from ROLE B
  [ ] SESSION INVARIANT D templates registered

STAGE 1 BODY:

You load the scout artifact from the path in ROLE B. You read the signals. You frame the
hypothesis.

  source_scout_artifact:        [path from ROLE B -- you copy this, do not infer]
  hypothesis:                   [falsifiable claim about {topic}]
  counter_hypothesis:           [incumbent's best defense -- grounded in ROLE C analysis]
  confidence_prior:             [initial confidence score: 1-10]
  gate_s_cleared:               [true -- from GATE S Step 2]
  invariant_registry_confirmed: [true -- from GATE S Step 3]
  incumbent_threat_locked:      [true -- from GATE S Step 1]

You write: {topic}-hypothesis-{date}.md. You confirm the write.

STAGE 1 EXIT SIGNAL: hypothesis_locked(confidence_prior=[value])
  "STAGE 1 EXIT: hypothesis_locked -- {topic}-hypothesis-{date}.md written.
   confidence_prior=[value]. Stage 2 ready."

---

## STAGE 2 -- WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] STAGE 1 EXIT SIGNAL received: hypothesis_locked(confidence_prior=[value])
  [ ] RESUME AUDIT: Stage 2 decision = RUN (you skip if RESUME-SKIP)
  [ ] hypothesis artifact confirmed written
  [ ] SESSION INVARIANT D Stage 2 template active

STAGE 2 BODY:

You gather at least 5 external sources. For each, you record:

  Source N:
    url_or_citation: [source]
    summary:         [1 sentence]
    verdict:         "Does [item N] support displacement of {status_quo_comparator}
                      by {topic} on [dimension]? [Yes / No / Inconclusive]"

You record after all sources are gathered:

  s2_count:                   [N -- must be >= 5]
  s2_incumbent_check_summary: [N support / M counter / P inconclusive]
  s2_ce_verdict:              [null if no CE; cite item if found]
  confidence_delta_s2:        [+1 / 0 / -1 based on evidence weight]
  running_confidence:         [confidence_prior + confidence_delta_s2]

Running null tally: "Running tally: [N] null across 1 stage complete. 2 stages remain."

GATE: You do not fire the exit signal until s2_count >= 5. If s2_count < 5, you gather
additional external sources before proceeding.

You write: {topic}-websearch-{date}.md. You confirm the write.

STAGE 2 EXIT SIGNAL: websearch_complete(count=[N], running_confidence=[value])
  "STAGE 2 EXIT: websearch_complete -- s2_ce_verdict=[value]. s2_count=[N] (gate >= 5 met).
   running_confidence=[value]. Stage 3 ready."

---

## STAGE 3 -- INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT SIGNAL received: websearch_complete(count=[N], running_confidence=[value])
  [ ] RESUME AUDIT: Stage 3 decision = RUN (you skip if RESUME-SKIP)
  [ ] s2_ce_verdict recorded (null or value -- not blank)
  [ ] SESSION INVARIANT D Stage 3 template active

STAGE 3 BODY:

You simulate at least 3 practitioner interviews. For each, you record:

  Practitioner N:
    type:    [practitioner type]
    account: [key quote or paraphrase -- 1 sentence]
    verdict: "Does [account N] reveal a viable transition path from {status_quo_comparator}
              to {topic} for [use case]? [Yes / No / Inconclusive]"

You record after all interviews are complete:

  s3_count:                   [N -- must be >= 3]
  s3_incumbent_check_summary: [N support / M counter / P inconclusive]
  s3_ce_verdict:              [null if no CE; cite account if found]
  confidence_delta_s3:        [+1 / 0 / -1]
  running_confidence:         [prev + confidence_delta_s3]

Running null tally: "Running tally: [N] null across 2 stages complete. 1 stage remains."

GATE: You do not fire the exit signal until s3_count >= 3. If s3_count < 3, you simulate
additional practitioner interviews before proceeding.

You write: {topic}-interview-{date}.md. You confirm the write.

STAGE 3 EXIT SIGNAL: interview_complete(count=[N], running_confidence=[value])
  "STAGE 3 EXIT: interview_complete -- s3_ce_verdict=[value]. s3_count=[N] (gate >= 3 met).
   running_confidence=[value]. Stage 4 ready."

---

## STAGE 4 -- PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT SIGNAL received: interview_complete(count=[N], running_confidence=[value])
  [ ] RESUME AUDIT: Stage 4 decision = RUN (you skip if RESUME-SKIP)
  [ ] s3_ce_verdict recorded (null or value -- not blank)
  [ ] SESSION INVARIANT D Stage 4 template active

STAGE 4 BODY:

You design and assess at least 3 prototype experiments. For each, you record:

  Experiment N:
    design:  [what was built or tested -- 1 sentence]
    result:  [what was learned -- 1-2 sentences]
    verdict: "Does [result N] make a credible case for displacing {status_quo_comparator}
              with {topic}? [Yes / No / Pending]"

You record after all experiments are complete:

  s4_count:                [N -- must be >= 3]
  s4_displacement_verdict: [Yes / No / Pending -- required; omission = format error]
  s4_ce_verdict:           [null if no CE; description if found]
  confidence_delta_s4:     [+1 / 0 / -1]
  running_confidence:      [prev + confidence_delta_s4]

Final null tally:
  null_tally_final = [N]
  Cross-check: "Running count from Stage 3 was [M]. Final is [N]. Match: [true/false]."

GATE: You do not fire the exit signal until s4_count >= 3. If s4_count < 3, you design
additional prototype experiments before proceeding.

You write: {topic}-prototype-{date}.md. You confirm the write.

STAGE 4 EXIT SIGNAL: prototype_complete(count=[null_tally_final], running_confidence=[value])
  "STAGE 4 EXIT: prototype_complete -- s4_ce_verdict=[value]. null_tally_final=[N].
   running_confidence=[value]. Stage 5 ready."

---

## STAGE 5 -- SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT SIGNAL received: prototype_complete(count=[N], running_confidence=[value])
  [ ] RESUME AUDIT: Stage 5 decision = RUN (you skip if RESUME-SKIP)
  [ ] null_tally_final recorded
  [ ] counter_hypothesis from Stage 1 available
  [ ] All four SESSION INVARIANTS active

STAGE 5 BODY: THREE-BLOCK STRUCTURE.
You do not populate any synthesis fields until you receive BLOCK 3 COMPLETE.

### BLOCK 1 -- CONFIDENCE CHAIN RESOLUTION

  confidence_prior:          [value from Stage 1]
  confidence_delta_s2:       [+/- from Stage 2]
  confidence_delta_s3:       [+/- from Stage 3]
  confidence_delta_s4:       [+/- from Stage 4]
  chain_equation:            [prior + s2 + s3 + s4 = sum]
  null_cap_applied:          [yes -- sum -= 2 if null_tally_final >= 3; no otherwise]
  confidence_chain_resolved: [final value after cap]

BLOCK 1 COMPLETE: "BLOCK 1 COMPLETE -- confidence_chain_resolved = [value]."

### BLOCK 2 -- COUNTER-HYPOTHESIS RESOLUTION

For each counter-hypothesis from Stage 1, you record:
  Counter N:
    text:     [counter-hypothesis text]
    verdict:  [REFUTED / PARTIALLY REFUTED / OPEN RISK]
    evidence: [cite stage artifact]

  open_risk_count:          [N -- count of OPEN RISK verdicts]
  cr_delta:                 [open_risk_count * -1]
  confidence_post_cr:       [confidence_chain_resolved + cr_delta]
  counter_hypothesis_verdict: [recorded]

BLOCK 2 COMPLETE: "BLOCK 2 COMPLETE -- counter_hypothesis_verdict recorded.
  confidence_post_cr = [value]."

### BLOCK 3 -- DISPLACEMENT INTEGRITY CHECK

You require BLOCK 1 COMPLETE and BLOCK 2 COMPLETE before you begin this block.

ATOMIC DUAL-LOCK:

  Null tally chain reconstruction:
    s2_ce_verdict: [null or value -- from Stage 2 artifact]
    s3_ce_verdict: [null or value -- from Stage 3 artifact]
    s4_ce_verdict: [null or value -- from Stage 4 artifact]
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
  consistency_flag: [CONSISTENT / INCONSISTENT -- mismatch requires justification]

BLOCK 3 COMPLETE: "BLOCK 3 COMPLETE -- displacement_conclusion = [value].
  co_activation_confirmed = [value]."

### SYNTHESIS BODY

(You do not populate until you receive BLOCK 3 COMPLETE.)

  displacement_conclusion:  [from BLOCK 3]
  hypothesis_verdict:       [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:         [2-3 sentences integrating S2, S3, S4 with displacement verdict]
  confidence_composite:     [confidence_post_cr -- final after all reductions]
  key_risk:                 [primary adoption risk framed as residual incumbent strength]
  topic_story_readiness:    "Evidence brief complete. Displacement case: [displacement_conclusion].
                             Confidence: [value]. Ready for /topic-story."

### HANDOFF

SESSION INVARIANT C enforced. Every field you write carries [derived from: X].
Unlabeled = format error.

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
  "STAGE 5 EXIT: synthesis_complete -- Evidence brief ready for topic-story."

You write: {topic}-synthesis-{date}.md
You write: {topic}-handoff-{date}.md
You confirm both writes. Campaign complete.
```

---

## V-02 -- Role Sequence (ROLE B Executes First as Blocking Gate Owner)

**Axis**: role_sequence (single)
**Hypothesis**: In the current prompt, ROLE C (Incumbent Threat Analyst) executes first. But
ROLE B (Scout Loader) owns the one field that can halt the entire campaign: gate_s_cleared = false
blocks Stage 0. If ROLE C executes and completes its full incumbent analysis before ROLE B runs,
that work is wasted when the scout is absent. More importantly, the current ordering does not make
the blocking dependency structurally visible to the model at execution time. If ROLE B executes
FIRST as the primary campaign gate -- with ROLE C and ROLE A explicitly annotated as depending on
ROLE B clearing gate_s_cleared -- the model encounters the blocking condition before any other role
work begins. This maps ROLE B from "step 2 in a sequence" to "primary gate owner, no campaign
without it." Stage 0 clearance steps reorder to match: Step 1 = gate_s_cleared (ROLE B), Step 2 =
incumbent_threat_locked (ROLE C), Step 3 = invariant_registry_confirmed (ROLE A). This directly
targets C-10 (structural block before hypothesis) and C-06 (gate enforces scout presence).
The risk: moving ROLE B first may disrupt models that look for incumbent framing before loading
the scout, since INCUMBENT ANCHOR (which ROLE C reads) is still filled first in the prompt body.

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

ROLE B executes FIRST. It is the primary blocking gate: gate_s_cleared = false halts
the campaign immediately. ROLE C and ROLE A cannot execute until ROLE B clears.
Execution order: B -> C -> A.

  ROLE   | TITLE                    | OWNED FIELD               | DEPENDENCY
  -------|--------------------------|---------------------------|---------------------------
  ROLE B | SCOUT LOADER             | gate_s_cleared            | NONE -- executes first
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked   | depends on ROLE B (gate_s_cleared = true)
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | depends on ROLE B and ROLE C

ROLE B execution (fill now -- CAMPAIGN BLOCKED if scout absent):
  scout_artifact:  [{topic}-scout-record-{date}.md or equivalent]
  scout_loaded:    [true / false]
  gate_s_cleared:  [true if scout_loaded; CAMPAIGN BLOCKED otherwise]

  If gate_s_cleared = false: emit "CAMPAIGN BLOCKED -- scout artifact not found.
    Locate {topic}-scout-record-{date}.md before proceeding." and STOP.

ROLE C execution (fill now -- only if gate_s_cleared = true):
  Reads INCUMBENT ANCHOR above. Confirms analysis complete.
  incumbent_threat_locked: [true when incumbent_name, incumbent_strength,
                             incumbent_vulnerability all filled]

ROLE A execution (fill now -- only if gate_s_cleared = true and incumbent_threat_locked = true):
  Confirms all four SESSION INVARIANT TABLE rows filled and active.
  invariant_registry_confirmed: [true when all four invariants in table are registered]

---

## RESUME AUDIT

Run before Stage 0. Glob existing artifacts for {topic} on {date}.

For each stage artifact, record: FOUND (Y/N) and DECISION (RESUME-SKIP / RUN).

1. Stage 1 -- {topic}-hypothesis-{date}.md:   found=[Y/N]  decision=[RESUME-SKIP / RUN]
2. Stage 2 -- {topic}-websearch-{date}.md:    found=[Y/N]  decision=[RESUME-SKIP / RUN]
3. Stage 3 -- {topic}-interview-{date}.md:    found=[Y/N]  decision=[RESUME-SKIP / RUN]
4. Stage 4 -- {topic}-prototype-{date}.md:    found=[Y/N]  decision=[RESUME-SKIP / RUN]
5. Stage 5 -- {topic}-synthesis-{date}.md:    found=[Y/N]  decision=[RESUME-SKIP / RUN]

  resume_audit_complete: [true]
  stages_to_run:         [list stages with RUN decision, or ALL if none found]

RESUME AUDIT EXIT: If all five stages are RESUME-SKIP, emit:
  "RESUME_AUDIT_EXIT -- All stage artifacts already present. Campaign complete. No stages re-run."
  and STOP. Otherwise: "RESUME_AUDIT_PASS -- Stages to run: [list]. Proceeding to Stage 0."

---

## STAGE 0 -- GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] RESUME AUDIT completed -- resume_audit_complete = true
  [ ] CAMPAIGN OPEN fields filled (topic, date, status_quo_comparator)
  [ ] INCUMBENT ANCHOR filled (incumbent_name, strength, vulnerability)
  [ ] All four SESSION INVARIANTS registered
  [ ] ROLE B executed FIRST -- gate_s_cleared confirmed (campaign cannot proceed otherwise)
  [ ] ROLE C executed -- incumbent_threat_locked = true
  [ ] ROLE A executed -- invariant_registry_confirmed = true

STAGE 0 BODY:

Clearance check -- reordered to match ROLE execution dependency (B -> C -> A):
  Step 1: gate_s_cleared (ROLE B required -- primary gate)   = [confirm or BLOCKED]
  Step 2: incumbent_threat_locked (ROLE C required)          = [confirm or BLOCKED]
  Step 3: invariant_registry_confirmed (ROLE A required)     = [confirm or BLOCKED]

First BLOCKED step halts campaign. Record step number and owning role.

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open -- Steps 1, 2, 3 all confirmed. SESSION INVARIANT D active.
   Advancing to Stage 1."

---

## STAGE 1 -- HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] STAGE 0 EXIT SIGNAL received: gate_open
  [ ] RESUME AUDIT: Stage 1 decision = RUN (skip entire stage body if RESUME-SKIP)
  [ ] scout_artifact path available from ROLE B
  [ ] SESSION INVARIANT D templates registered

STAGE 1 BODY:
Load scout artifact from path. Read signals. Frame hypothesis.

  source_scout_artifact:        [path from ROLE B -- copied, not inferred]
  hypothesis:                   [falsifiable claim about {topic}]
  counter_hypothesis:           [incumbent's best defense -- grounded in ROLE C analysis]
  confidence_prior:             [initial confidence score: 1-10]
  gate_s_cleared:               [true -- from GATE S Step 1]
  invariant_registry_confirmed: [true -- from GATE S Step 3]
  incumbent_threat_locked:      [true -- from GATE S Step 2]

Write artifact: {topic}-hypothesis-{date}.md. Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked(confidence_prior=[value])
  "STAGE 1 EXIT: hypothesis_locked -- {topic}-hypothesis-{date}.md written.
   confidence_prior=[value]. Stage 2 ready."

---

## STAGE 2 -- WEB SEARCH

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

  s2_count:                   [N -- must be >= 5]
  s2_incumbent_check_summary: [N support / M counter / P inconclusive]
  s2_ce_verdict:              [null if no CE; cite item if found]
  confidence_delta_s2:        [+1 / 0 / -1 based on evidence weight]
  running_confidence:         [confidence_prior + confidence_delta_s2]

Running null tally: "Running tally: [N] null across 1 stage complete. 2 stages remain."

GATE: Do not fire exit signal until s2_count >= 5. If s2_count < 5, gather
additional external sources before proceeding.

Write artifact: {topic}-websearch-{date}.md. Confirm write.

STAGE 2 EXIT SIGNAL: websearch_complete(count=[N], running_confidence=[value])
  "STAGE 2 EXIT: websearch_complete -- s2_ce_verdict=[value]. s2_count=[N] (gate >= 5 met).
   running_confidence=[value]. Stage 3 ready."

---

## STAGE 3 -- INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT SIGNAL received: websearch_complete(count=[N], running_confidence=[value])
  [ ] RESUME AUDIT: Stage 3 decision = RUN (skip if RESUME-SKIP)
  [ ] s2_ce_verdict recorded (null or value -- not blank)
  [ ] SESSION INVARIANT D Stage 3 template active

STAGE 3 BODY:

Simulate minimum 3 practitioner interviews. For each, record:

  Practitioner N:
    type:    [practitioner type]
    account: [key quote or paraphrase -- 1 sentence]
    verdict: "Does [account N] reveal a viable transition path from {status_quo_comparator}
              to {topic} for [use case]? [Yes / No / Inconclusive]"

Record after all interviews complete:

  s3_count:                   [N -- must be >= 3]
  s3_incumbent_check_summary: [N support / M counter / P inconclusive]
  s3_ce_verdict:              [null if no CE; cite account if found]
  confidence_delta_s3:        [+1 / 0 / -1]
  running_confidence:         [prev + confidence_delta_s3]

Running null tally: "Running tally: [N] null across 2 stages complete. 1 stage remains."

GATE: Do not fire exit signal until s3_count >= 3. If s3_count < 3, simulate
additional practitioner interviews before proceeding.

Write artifact: {topic}-interview-{date}.md. Confirm write.

STAGE 3 EXIT SIGNAL: interview_complete(count=[N], running_confidence=[value])
  "STAGE 3 EXIT: interview_complete -- s3_ce_verdict=[value]. s3_count=[N] (gate >= 3 met).
   running_confidence=[value]. Stage 4 ready."

---

## STAGE 4 -- PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT SIGNAL received: interview_complete(count=[N], running_confidence=[value])
  [ ] RESUME AUDIT: Stage 4 decision = RUN (skip if RESUME-SKIP)
  [ ] s3_ce_verdict recorded (null or value -- not blank)
  [ ] SESSION INVARIANT D Stage 4 template active

STAGE 4 BODY:

Design and assess minimum 3 prototype experiments. For each, record:

  Experiment N:
    design:  [what was built or tested -- 1 sentence]
    result:  [what was learned -- 1-2 sentences]
    verdict: "Does [result N] make a credible case for displacing {status_quo_comparator}
              with {topic}? [Yes / No / Pending]"

Record after all experiments complete:

  s4_count:                [N -- must be >= 3]
  s4_displacement_verdict: [Yes / No / Pending -- required; omission = format error]
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
  "STAGE 4 EXIT: prototype_complete -- s4_ce_verdict=[value]. null_tally_final=[N].
   running_confidence=[value]. Stage 5 ready."

---

## STAGE 5 -- SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT SIGNAL received: prototype_complete(count=[N], running_confidence=[value])
  [ ] RESUME AUDIT: Stage 5 decision = RUN (skip if RESUME-SKIP)
  [ ] null_tally_final recorded
  [ ] counter_hypothesis from Stage 1 available
  [ ] All four SESSION INVARIANTS active

STAGE 5 BODY: THREE-BLOCK STRUCTURE.
SYNTHESIS GATE: no synthesis fields may be populated until BLOCK 3 COMPLETE received.

### BLOCK 1 -- CONFIDENCE CHAIN RESOLUTION

  confidence_prior:          [value from Stage 1]
  confidence_delta_s2:       [+/- from Stage 2]
  confidence_delta_s3:       [+/- from Stage 3]
  confidence_delta_s4:       [+/- from Stage 4]
  chain_equation:            [prior + s2 + s3 + s4 = sum]
  null_cap_applied:          [yes -- sum -= 2 if null_tally_final >= 3; no otherwise]
  confidence_chain_resolved: [final value after cap]

BLOCK 1 COMPLETE: "BLOCK 1 COMPLETE -- confidence_chain_resolved = [value]."

### BLOCK 2 -- COUNTER-HYPOTHESIS RESOLUTION

For each counter-hypothesis from Stage 1, record:
  Counter N:
    text:     [counter-hypothesis text]
    verdict:  [REFUTED / PARTIALLY REFUTED / OPEN RISK]
    evidence: [cite stage artifact]

  open_risk_count:          [N -- count of OPEN RISK verdicts]
  cr_delta:                 [open_risk_count * -1]
  confidence_post_cr:       [confidence_chain_resolved + cr_delta]
  counter_hypothesis_verdict: [recorded]

BLOCK 2 COMPLETE: "BLOCK 2 COMPLETE -- counter_hypothesis_verdict recorded.
  confidence_post_cr = [value]."

### BLOCK 3 -- DISPLACEMENT INTEGRITY CHECK

Requires BLOCK 1 COMPLETE and BLOCK 2 COMPLETE before beginning.

ATOMIC DUAL-LOCK:

  Null tally chain reconstruction:
    s2_ce_verdict: [null or value -- from Stage 2 artifact]
    s3_ce_verdict: [null or value -- from Stage 3 artifact]
    s4_ce_verdict: [null or value -- from Stage 4 artifact]
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
  consistency_flag: [CONSISTENT / INCONSISTENT -- mismatch requires justification]

BLOCK 3 COMPLETE: "BLOCK 3 COMPLETE -- displacement_conclusion = [value].
  co_activation_confirmed = [value]."

### SYNTHESIS BODY

(Do not populate until BLOCK 3 COMPLETE received.)

  displacement_conclusion:  [from BLOCK 3]
  hypothesis_verdict:       [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:         [2-3 sentences integrating S2, S3, S4 with displacement verdict]
  confidence_composite:     [confidence_post_cr -- final after all reductions]
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
  "STAGE 5 EXIT: synthesis_complete -- Evidence brief ready for topic-story."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## V-03 -- Evidence Quality Mandatory (Per-Stage Quality Rating)

**Axis**: evidence_quality_mandatory (single)
**Hypothesis**: C-08 (evidence gaps flagged at point of discovery) and C-09 (thin-evidence
propagates to synthesis with confidence qualification) are currently partial because evidence
quality depends on the model noticing thinness organically rather than being structurally required
to assess it. If a mandatory `evidence_quality: [thin / moderate / strong]` field is added to each
evidence stage (S2, S3, S4), and Stage 5 opens with a THIN-EVIDENCE CARRY block that enumerates
any thin-rated stages, names the claim each one weakens, and computes a per-stage confidence
penalty, then C-08 and C-09 become structurally enforced rather than model-dependent. The carry
block links thin assessment back to the specific claim it weakens (required for C-09 full PASS: "the
confidence qualification must name the source stage and the weakened claim"). The risk: models may
default to rating all stages "moderate" to avoid the carry overhead, satisfying structure without
genuine quality assessment. Mitigation: require `evidence_quality_note` when rated "thin" -- a
mandatory explanation of why.

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

ROLE C executes first. Roles run in sequence C -> B -> A before Stage 0 begins.

  ROLE   | TITLE                    | OWNED FIELD               | DEPENDENCY
  -------|--------------------------|---------------------------|---------------------------
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked   | none
  ROLE B | SCOUT LOADER             | gate_s_cleared            | none
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | depends on C and B

ROLE C execution (fill now):
  Reads INCUMBENT ANCHOR above. Confirms analysis complete.
  incumbent_threat_locked: [true when incumbent_name, strength, vulnerability all filled]

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

For each stage artifact, record: FOUND (Y/N) and DECISION (RESUME-SKIP / RUN).

1. Stage 1 -- {topic}-hypothesis-{date}.md:   found=[Y/N]  decision=[RESUME-SKIP / RUN]
2. Stage 2 -- {topic}-websearch-{date}.md:    found=[Y/N]  decision=[RESUME-SKIP / RUN]
3. Stage 3 -- {topic}-interview-{date}.md:    found=[Y/N]  decision=[RESUME-SKIP / RUN]
4. Stage 4 -- {topic}-prototype-{date}.md:    found=[Y/N]  decision=[RESUME-SKIP / RUN]
5. Stage 5 -- {topic}-synthesis-{date}.md:    found=[Y/N]  decision=[RESUME-SKIP / RUN]

  resume_audit_complete: [true]
  stages_to_run:         [list stages with RUN decision, or ALL if none found]

RESUME AUDIT EXIT: If all five stages are RESUME-SKIP, emit:
  "RESUME_AUDIT_EXIT -- All stage artifacts already present. Campaign complete. No stages re-run."
  and STOP. Otherwise: "RESUME_AUDIT_PASS -- Stages to run: [list]. Proceeding to Stage 0."

---

## STAGE 0 -- GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] RESUME AUDIT completed -- resume_audit_complete = true
  [ ] CAMPAIGN OPEN fields filled (topic, date, status_quo_comparator)
  [ ] INCUMBENT ANCHOR filled (incumbent_name, strength, vulnerability)
  [ ] All four SESSION INVARIANTS registered
  [ ] ROLE C executed -- incumbent_threat_locked = true
  [ ] ROLE B executed -- scout_artifact identified, scout_loaded confirmed
  [ ] ROLE A executed -- invariant_registry_confirmed = true

STAGE 0 BODY:

Clearance check -- record confirm or BLOCKED for each:
  Step 1: incumbent_threat_locked (ROLE C required) = [confirm or BLOCKED]
  Step 2: gate_s_cleared (ROLE B required)          = [confirm or BLOCKED]
  Step 3: invariant_registry_confirmed (ROLE A)     = [confirm or BLOCKED]

First BLOCKED step halts campaign. Record step and owning role.

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open -- Steps 1, 2, 3 all confirmed. SESSION INVARIANT D active.
   Advancing to Stage 1."

---

## STAGE 1 -- HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] STAGE 0 EXIT SIGNAL received: gate_open
  [ ] RESUME AUDIT: Stage 1 decision = RUN (skip entire stage body if RESUME-SKIP)
  [ ] scout_artifact path available from ROLE B
  [ ] SESSION INVARIANT D templates registered

STAGE 1 BODY:
Load scout artifact from path. Read signals. Frame hypothesis.

  source_scout_artifact:        [path from ROLE B -- copied, not inferred]
  hypothesis:                   [falsifiable claim about {topic}]
  counter_hypothesis:           [incumbent's best defense -- grounded in ROLE C analysis]
  confidence_prior:             [initial confidence score: 1-10]
  gate_s_cleared:               [true -- from GATE S Step 2]
  invariant_registry_confirmed: [true -- from GATE S Step 3]
  incumbent_threat_locked:      [true -- from GATE S Step 1]

Write artifact: {topic}-hypothesis-{date}.md. Confirm write.

STAGE 1 EXIT SIGNAL: hypothesis_locked(confidence_prior=[value])
  "STAGE 1 EXIT: hypothesis_locked -- {topic}-hypothesis-{date}.md written.
   confidence_prior=[value]. Stage 2 ready."

---

## STAGE 2 -- WEB SEARCH

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

  s2_count:                   [N -- must be >= 5]
  s2_incumbent_check_summary: [N support / M counter / P inconclusive]
  s2_ce_verdict:              [null if no CE; cite item if found]
  confidence_delta_s2:        [+1 / 0 / -1 based on evidence weight]
  running_confidence:         [confidence_prior + confidence_delta_s2]
  evidence_quality:           [thin / moderate / strong]
  evidence_quality_note:      [required if thin -- one sentence: why this stage's evidence
                               is thin or conflicting. Omit if moderate or strong.]

Running null tally: "Running tally: [N] null across 1 stage complete. 2 stages remain."

GATE: Do not fire exit signal until s2_count >= 5. If s2_count < 5, gather
additional external sources before proceeding.

Write artifact: {topic}-websearch-{date}.md. Confirm write.

STAGE 2 EXIT SIGNAL: websearch_complete(count=[N], running_confidence=[value], quality=[thin/moderate/strong])
  "STAGE 2 EXIT: websearch_complete -- s2_ce_verdict=[value]. s2_count=[N] (gate >= 5 met).
   running_confidence=[value]. evidence_quality=[value]. Stage 3 ready."

---

## STAGE 3 -- INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT SIGNAL received: websearch_complete(...)
  [ ] RESUME AUDIT: Stage 3 decision = RUN (skip if RESUME-SKIP)
  [ ] s2_ce_verdict recorded (null or value -- not blank)
  [ ] SESSION INVARIANT D Stage 3 template active

STAGE 3 BODY:

Simulate minimum 3 practitioner interviews. For each, record:

  Practitioner N:
    type:    [practitioner type]
    account: [key quote or paraphrase -- 1 sentence]
    verdict: "Does [account N] reveal a viable transition path from {status_quo_comparator}
              to {topic} for [use case]? [Yes / No / Inconclusive]"

Record after all interviews complete:

  s3_count:                   [N -- must be >= 3]
  s3_incumbent_check_summary: [N support / M counter / P inconclusive]
  s3_ce_verdict:              [null if no CE; cite account if found]
  confidence_delta_s3:        [+1 / 0 / -1]
  running_confidence:         [prev + confidence_delta_s3]
  evidence_quality:           [thin / moderate / strong]
  evidence_quality_note:      [required if thin -- one sentence: why practitioner accounts
                               are thin or conflicting. Omit if moderate or strong.]

Running null tally: "Running tally: [N] null across 2 stages complete. 1 stage remains."

GATE: Do not fire exit signal until s3_count >= 3. If s3_count < 3, simulate
additional practitioner interviews before proceeding.

Write artifact: {topic}-interview-{date}.md. Confirm write.

STAGE 3 EXIT SIGNAL: interview_complete(count=[N], running_confidence=[value], quality=[thin/moderate/strong])
  "STAGE 3 EXIT: interview_complete -- s3_ce_verdict=[value]. s3_count=[N] (gate >= 3 met).
   running_confidence=[value]. evidence_quality=[value]. Stage 4 ready."

---

## STAGE 4 -- PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT SIGNAL received: interview_complete(...)
  [ ] RESUME AUDIT: Stage 4 decision = RUN (skip if RESUME-SKIP)
  [ ] s3_ce_verdict recorded (null or value -- not blank)
  [ ] SESSION INVARIANT D Stage 4 template active

STAGE 4 BODY:

Design and assess minimum 3 prototype experiments. For each, record:

  Experiment N:
    design:  [what was built or tested -- 1 sentence]
    result:  [what was learned -- 1-2 sentences]
    verdict: "Does [result N] make a credible case for displacing {status_quo_comparator}
              with {topic}? [Yes / No / Pending]"

Record after all experiments complete:

  s4_count:                [N -- must be >= 3]
  s4_displacement_verdict: [Yes / No / Pending -- required; omission = format error]
  s4_ce_verdict:           [null if no CE; description if found]
  confidence_delta_s4:     [+1 / 0 / -1]
  running_confidence:      [prev + confidence_delta_s4]
  evidence_quality:        [thin / moderate / strong]
  evidence_quality_note:   [required if thin -- one sentence: why prototype results are
                            thin or inconclusive. Omit if moderate or strong.]

Final null tally:
  null_tally_final = [N]
  Cross-check: "Running count from Stage 3 was [M]. Final is [N]. Match: [true/false]."

GATE: Do not fire exit signal until s4_count >= 3. If s4_count < 3, design
additional prototype experiments before proceeding.

Write artifact: {topic}-prototype-{date}.md. Confirm write.

STAGE 4 EXIT SIGNAL: prototype_complete(count=[null_tally_final], running_confidence=[value], quality=[thin/moderate/strong])
  "STAGE 4 EXIT: prototype_complete -- s4_ce_verdict=[value]. null_tally_final=[N].
   running_confidence=[value]. evidence_quality=[value]. Stage 5 ready."

---

## STAGE 5 -- SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT SIGNAL received: prototype_complete(...)
  [ ] RESUME AUDIT: Stage 5 decision = RUN (skip if RESUME-SKIP)
  [ ] null_tally_final recorded
  [ ] counter_hypothesis from Stage 1 available
  [ ] All four SESSION INVARIANTS active

STAGE 5 BODY: THIN-EVIDENCE CARRY, then THREE-BLOCK STRUCTURE.
SYNTHESIS GATE: no synthesis fields may be populated until BLOCK 3 COMPLETE received.

### THIN-EVIDENCE CARRY

Run this before BLOCK 1. For each stage where evidence_quality = thin, record:

  Thin Stage N (Stage [2/3/4]):
    evidence_quality:      thin
    evidence_quality_note: [copy from that stage's exit signal]
    hypothesis_claim_weakened: [which specific hypothesis claim this thin stage fails to support]
    confidence_penalty:    [-1]

  thin_stages:           [list stage numbers rated thin, or "none"]
  thin_evidence_penalty: [sum of confidence_penalty values -- 0 if no thin stages]

THIN-EVIDENCE CARRY COMPLETE: "THIN-EVIDENCE CARRY COMPLETE -- thin_stages=[list].
  thin_evidence_penalty=[value]."

### BLOCK 1 -- CONFIDENCE CHAIN RESOLUTION

(Incorporates thin_evidence_penalty from THIN-EVIDENCE CARRY.)

  confidence_prior:          [value from Stage 1]
  confidence_delta_s2:       [+/- from Stage 2]
  confidence_delta_s3:       [+/- from Stage 3]
  confidence_delta_s4:       [+/- from Stage 4]
  thin_evidence_penalty:     [from THIN-EVIDENCE CARRY]
  chain_equation:            [prior + s2 + s3 + s4 + thin_penalty = sum]
  null_cap_applied:          [yes -- sum -= 2 if null_tally_final >= 3; no otherwise]
  confidence_chain_resolved: [final value after cap and thin penalty]

BLOCK 1 COMPLETE: "BLOCK 1 COMPLETE -- confidence_chain_resolved = [value]
  (includes thin_evidence_penalty = [value])."

### BLOCK 2 -- COUNTER-HYPOTHESIS RESOLUTION

For each counter-hypothesis from Stage 1, record:
  Counter N:
    text:     [counter-hypothesis text]
    verdict:  [REFUTED / PARTIALLY REFUTED / OPEN RISK]
    evidence: [cite stage artifact]

  open_risk_count:          [N -- count of OPEN RISK verdicts]
  cr_delta:                 [open_risk_count * -1]
  confidence_post_cr:       [confidence_chain_resolved + cr_delta]
  counter_hypothesis_verdict: [recorded]

BLOCK 2 COMPLETE: "BLOCK 2 COMPLETE -- counter_hypothesis_verdict recorded.
  confidence_post_cr = [value]."

### BLOCK 3 -- DISPLACEMENT INTEGRITY CHECK

Requires BLOCK 1 COMPLETE and BLOCK 2 COMPLETE before beginning.

ATOMIC DUAL-LOCK:

  Null tally chain reconstruction:
    s2_ce_verdict: [null or value -- from Stage 2 artifact]
    s3_ce_verdict: [null or value -- from Stage 3 artifact]
    s4_ce_verdict: [null or value -- from Stage 4 artifact]
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
  consistency_flag: [CONSISTENT / INCONSISTENT -- mismatch requires justification]

BLOCK 3 COMPLETE: "BLOCK 3 COMPLETE -- displacement_conclusion = [value].
  co_activation_confirmed = [value]."

### SYNTHESIS BODY

(Do not populate until BLOCK 3 COMPLETE received.)

  displacement_conclusion:  [from BLOCK 3]
  hypothesis_verdict:       [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:         [2-3 sentences integrating S2, S3, S4 with displacement verdict
                             and explicit mention of any thin stages from THIN-EVIDENCE CARRY]
  confidence_composite:     [confidence_post_cr -- final after all reductions]
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
  "STAGE 5 EXIT: synthesis_complete -- Evidence brief ready for topic-story."

Write: {topic}-synthesis-{date}.md
Write: {topic}-handoff-{date}.md
Confirm both writes. Campaign complete.
```

---

## V-04 -- Combined: Phrasing Register + Role Sequence

**Axis**: phrasing_register + role_sequence (combined)
**Hypothesis**: V-01 and V-02 are structurally orthogonal -- V-01 changes instruction voice
throughout, V-02 changes role execution order. If V-01 (second-person direct) improves model
execution fidelity for C-01 and C-03, and V-02 (ROLE B first) improves structural blocking for
C-10 and C-06, then combining them should produce additive gains on all four criteria without
interference. The combined variation retains the full R19 baseline structure with two axes
simultaneously applied: every instruction is second-person direct, and ROLE B runs first as the
primary blocking gate with ROLE C and ROLE A annotated as depending on ROLE B clearance.

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
ENTRY CONDITIONS and a named EXIT SIGNAL. You do not begin any stage body until entry
conditions confirm.

---

## CAMPAIGN OPEN

  topic:                 {topic}
  date:                  {date}
  status_quo_comparator: [you name the incumbent approach this topic must displace]

### INCUMBENT ANCHOR

You fill this section before you run any role or register any invariant.

  incumbent_name:          [full name of status_quo_comparator]
  incumbent_strength:      [one sentence: why the incumbent is currently winning]
  incumbent_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]

### SESSION INVARIANTS TABLE

SESSION INVARIANT D leads. You register all four before any role executes. Each carries:
"you cannot modify or bypass this at any subsequent stage."

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
       |                           | You cannot modify or bypass this at any stage.
  -----|---------------------------|------------------------------------------------------
  A    | ADVERSARIAL REVIEWER      | adversarial_reviewer_type: [the role most likely to
       | TYPE                      |   challenge the displacement claim].
       |                           | Activation: null_tally_final >= 3.
       |                           | You cannot modify or bypass this at synthesis.
  -----|---------------------------|------------------------------------------------------
  B    | CONFIDENCE CAP            | null_ce_cap_rule: confidence_composite -= 2 if
       |                           |   null_tally_final >= 3 (hard cap).
       |                           | You cannot soften or override this at synthesis.
  -----|---------------------------|------------------------------------------------------
  C    | DERIVATION ANNOTATION     | annotation_rule: Every handoff field you write carries
       |                           |   [derived from: X]. Unlabeled = format error.
       |                           | You cannot modify or bypass this at synthesis.

### ROLE OWNERSHIP TABLE

ROLE B executes FIRST. It is the primary blocking gate: if gate_s_cleared = false you halt
the campaign immediately. ROLE C and ROLE A cannot execute until ROLE B clears.
You run roles in order: B -> C -> A.

  ROLE   | TITLE                    | OWNED FIELD               | DEPENDENCY
  -------|--------------------------|---------------------------|---------------------------
  ROLE B | SCOUT LOADER             | gate_s_cleared            | NONE -- you run this first
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked   | you depend on ROLE B (gate_s_cleared = true)
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | you depend on ROLE B and ROLE C

ROLE B (you execute now -- CAMPAIGN BLOCKED if scout absent):
  scout_artifact:  [{topic}-scout-record-{date}.md or equivalent]
  scout_loaded:    [true / false]
  gate_s_cleared:  [true if scout_loaded; CAMPAIGN BLOCKED otherwise]

  If gate_s_cleared = false: you emit "CAMPAIGN BLOCKED -- scout artifact not found.
    Locate {topic}-scout-record-{date}.md before proceeding." and you STOP.

ROLE C (you execute now -- only if gate_s_cleared = true):
  You read the INCUMBENT ANCHOR above. You confirm the analysis is complete.
  incumbent_threat_locked: [true when incumbent_name, strength, vulnerability all filled]

ROLE A (you execute now -- only if gate_s_cleared = true and incumbent_threat_locked = true):
  You confirm all four SESSION INVARIANT TABLE rows are filled and active.
  invariant_registry_confirmed: [true when all four invariants registered]

---

## RESUME AUDIT

You run this before Stage 0. You glob existing artifacts for {topic} on {date}.

For each stage artifact, you record: FOUND (Y/N) and DECISION (RESUME-SKIP / RUN).

1. Stage 1 -- {topic}-hypothesis-{date}.md:   found=[Y/N]  decision=[RESUME-SKIP / RUN]
2. Stage 2 -- {topic}-websearch-{date}.md:    found=[Y/N]  decision=[RESUME-SKIP / RUN]
3. Stage 3 -- {topic}-interview-{date}.md:    found=[Y/N]  decision=[RESUME-SKIP / RUN]
4. Stage 4 -- {topic}-prototype-{date}.md:    found=[Y/N]  decision=[RESUME-SKIP / RUN]
5. Stage 5 -- {topic}-synthesis-{date}.md:    found=[Y/N]  decision=[RESUME-SKIP / RUN]

  resume_audit_complete: [true]
  stages_to_run:         [list stages with RUN decision, or ALL if none found]

RESUME AUDIT EXIT: If all five stages are RESUME-SKIP, you emit:
  "RESUME_AUDIT_EXIT -- All stage artifacts already present. Campaign complete. No stages re-run."
  and you STOP. Otherwise: "RESUME_AUDIT_PASS -- Stages to run: [list]. Proceeding to Stage 0."

---

## STAGE 0 -- GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] RESUME AUDIT completed -- resume_audit_complete = true
  [ ] CAMPAIGN OPEN fields filled (topic, date, status_quo_comparator)
  [ ] INCUMBENT ANCHOR filled (incumbent_name, strength, vulnerability)
  [ ] All four SESSION INVARIANTS registered
  [ ] ROLE B executed FIRST -- gate_s_cleared confirmed (you cannot proceed otherwise)
  [ ] ROLE C executed -- incumbent_threat_locked = true
  [ ] ROLE A executed -- invariant_registry_confirmed = true

STAGE 0 BODY:

You check clearance for each step and record confirm or BLOCKED.
Steps reordered to match role execution dependency (B -> C -> A):
  Step 1: gate_s_cleared (ROLE B required -- primary gate)   = [confirm or BLOCKED]
  Step 2: incumbent_threat_locked (ROLE C required)          = [confirm or BLOCKED]
  Step 3: invariant_registry_confirmed (ROLE A required)     = [confirm or BLOCKED]

The first BLOCKED step halts the campaign. You record the step number and owning role.

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open -- Steps 1, 2, 3 all confirmed. SESSION INVARIANT D active.
   Advancing to Stage 1."

---

## STAGE 1 -- HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] STAGE 0 EXIT SIGNAL received: gate_open
  [ ] RESUME AUDIT: Stage 1 decision = RUN (you skip entire stage body if RESUME-SKIP)
  [ ] scout_artifact path available from ROLE B
  [ ] SESSION INVARIANT D templates registered

STAGE 1 BODY:
You load the scout artifact from the path in ROLE B. You read the signals. You frame the
hypothesis.

  source_scout_artifact:        [path from ROLE B -- you copy this, do not infer]
  hypothesis:                   [falsifiable claim about {topic}]
  counter_hypothesis:           [incumbent's best defense -- grounded in ROLE C analysis]
  confidence_prior:             [initial confidence score: 1-10]
  gate_s_cleared:               [true -- from GATE S Step 1]
  invariant_registry_confirmed: [true -- from GATE S Step 3]
  incumbent_threat_locked:      [true -- from GATE S Step 2]

You write: {topic}-hypothesis-{date}.md. You confirm the write.

STAGE 1 EXIT SIGNAL: hypothesis_locked(confidence_prior=[value])
  "STAGE 1 EXIT: hypothesis_locked -- {topic}-hypothesis-{date}.md written.
   confidence_prior=[value]. Stage 2 ready."

---

## STAGE 2 -- WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] STAGE 1 EXIT SIGNAL received: hypothesis_locked(confidence_prior=[value])
  [ ] RESUME AUDIT: Stage 2 decision = RUN (you skip if RESUME-SKIP)
  [ ] hypothesis artifact confirmed written
  [ ] SESSION INVARIANT D Stage 2 template active

STAGE 2 BODY:

You gather at least 5 external sources. For each, you record:

  Source N:
    url_or_citation: [source]
    summary:         [1 sentence]
    verdict:         "Does [item N] support displacement of {status_quo_comparator}
                      by {topic} on [dimension]? [Yes / No / Inconclusive]"

You record after all sources are gathered:

  s2_count:                   [N -- must be >= 5]
  s2_incumbent_check_summary: [N support / M counter / P inconclusive]
  s2_ce_verdict:              [null if no CE; cite item if found]
  confidence_delta_s2:        [+1 / 0 / -1 based on evidence weight]
  running_confidence:         [confidence_prior + confidence_delta_s2]

Running null tally: "Running tally: [N] null across 1 stage complete. 2 stages remain."

GATE: You do not fire the exit signal until s2_count >= 5. If s2_count < 5, you gather
additional external sources before proceeding.

You write: {topic}-websearch-{date}.md. You confirm the write.

STAGE 2 EXIT SIGNAL: websearch_complete(count=[N], running_confidence=[value])
  "STAGE 2 EXIT: websearch_complete -- s2_ce_verdict=[value]. s2_count=[N] (gate >= 5 met).
   running_confidence=[value]. Stage 3 ready."

---

## STAGE 3 -- INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT SIGNAL received: websearch_complete(count=[N], running_confidence=[value])
  [ ] RESUME AUDIT: Stage 3 decision = RUN (you skip if RESUME-SKIP)
  [ ] s2_ce_verdict recorded (null or value -- not blank)
  [ ] SESSION INVARIANT D Stage 3 template active

STAGE 3 BODY:

You simulate at least 3 practitioner interviews. For each, you record:

  Practitioner N:
    type:    [practitioner type]
    account: [key quote or paraphrase -- 1 sentence]
    verdict: "Does [account N] reveal a viable transition path from {status_quo_comparator}
              to {topic} for [use case]? [Yes / No / Inconclusive]"

You record after all interviews are complete:

  s3_count:                   [N -- must be >= 3]
  s3_incumbent_check_summary: [N support / M counter / P inconclusive]
  s3_ce_verdict:              [null if no CE; cite account if found]
  confidence_delta_s3:        [+1 / 0 / -1]
  running_confidence:         [prev + confidence_delta_s3]

Running null tally: "Running tally: [N] null across 2 stages complete. 1 stage remains."

GATE: You do not fire the exit signal until s3_count >= 3. If s3_count < 3, you simulate
additional practitioner interviews before proceeding.

You write: {topic}-interview-{date}.md. You confirm the write.

STAGE 3 EXIT SIGNAL: interview_complete(count=[N], running_confidence=[value])
  "STAGE 3 EXIT: interview_complete -- s3_ce_verdict=[value]. s3_count=[N] (gate >= 3 met).
   running_confidence=[value]. Stage 4 ready."

---

## STAGE 4 -- PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT SIGNAL received: interview_complete(count=[N], running_confidence=[value])
  [ ] RESUME AUDIT: Stage 4 decision = RUN (you skip if RESUME-SKIP)
  [ ] s3_ce_verdict recorded (null or value -- not blank)
  [ ] SESSION INVARIANT D Stage 4 template active

STAGE 4 BODY:

You design and assess at least 3 prototype experiments. For each, you record:

  Experiment N:
    design:  [what was built or tested -- 1 sentence]
    result:  [what was learned -- 1-2 sentences]
    verdict: "Does [result N] make a credible case for displacing {status_quo_comparator}
              with {topic}? [Yes / No / Pending]"

You record after all experiments are complete:

  s4_count:                [N -- must be >= 3]
  s4_displacement_verdict: [Yes / No / Pending -- required; omission = format error]
  s4_ce_verdict:           [null if no CE; description if found]
  confidence_delta_s4:     [+1 / 0 / -1]
  running_confidence:      [prev + confidence_delta_s4]

Final null tally:
  null_tally_final = [N]
  Cross-check: "Running count from Stage 3 was [M]. Final is [N]. Match: [true/false]."

GATE: You do not fire the exit signal until s4_count >= 3. If s4_count < 3, you design
additional prototype experiments before proceeding.

You write: {topic}-prototype-{date}.md. You confirm the write.

STAGE 4 EXIT SIGNAL: prototype_complete(count=[null_tally_final], running_confidence=[value])
  "STAGE 4 EXIT: prototype_complete -- s4_ce_verdict=[value]. null_tally_final=[N].
   running_confidence=[value]. Stage 5 ready."

---

## STAGE 5 -- SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT SIGNAL received: prototype_complete(count=[N], running_confidence=[value])
  [ ] RESUME AUDIT: Stage 5 decision = RUN (you skip if RESUME-SKIP)
  [ ] null_tally_final recorded
  [ ] counter_hypothesis from Stage 1 available
  [ ] All four SESSION INVARIANTS active

STAGE 5 BODY: THREE-BLOCK STRUCTURE.
You do not populate any synthesis fields until you receive BLOCK 3 COMPLETE.

### BLOCK 1 -- CONFIDENCE CHAIN RESOLUTION

  confidence_prior:          [value from Stage 1]
  confidence_delta_s2:       [+/- from Stage 2]
  confidence_delta_s3:       [+/- from Stage 3]
  confidence_delta_s4:       [+/- from Stage 4]
  chain_equation:            [prior + s2 + s3 + s4 = sum]
  null_cap_applied:          [yes -- sum -= 2 if null_tally_final >= 3; no otherwise]
  confidence_chain_resolved: [final value after cap]

BLOCK 1 COMPLETE: "BLOCK 1 COMPLETE -- confidence_chain_resolved = [value]."

### BLOCK 2 -- COUNTER-HYPOTHESIS RESOLUTION

For each counter-hypothesis from Stage 1, you record:
  Counter N:
    text:     [counter-hypothesis text]
    verdict:  [REFUTED / PARTIALLY REFUTED / OPEN RISK]
    evidence: [cite stage artifact]

  open_risk_count:          [N -- count of OPEN RISK verdicts]
  cr_delta:                 [open_risk_count * -1]
  confidence_post_cr:       [confidence_chain_resolved + cr_delta]
  counter_hypothesis_verdict: [recorded]

BLOCK 2 COMPLETE: "BLOCK 2 COMPLETE -- counter_hypothesis_verdict recorded.
  confidence_post_cr = [value]."

### BLOCK 3 -- DISPLACEMENT INTEGRITY CHECK

You require BLOCK 1 COMPLETE and BLOCK 2 COMPLETE before you begin this block.

ATOMIC DUAL-LOCK:

  Null tally chain reconstruction:
    s2_ce_verdict: [null or value -- from Stage 2 artifact]
    s3_ce_verdict: [null or value -- from Stage 3 artifact]
    s4_ce_verdict: [null or value -- from Stage 4 artifact]
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
  consistency_flag: [CONSISTENT / INCONSISTENT -- mismatch requires justification]

BLOCK 3 COMPLETE: "BLOCK 3 COMPLETE -- displacement_conclusion = [value].
  co_activation_confirmed = [value]."

### SYNTHESIS BODY

(You do not populate until you receive BLOCK 3 COMPLETE.)

  displacement_conclusion:  [from BLOCK 3]
  hypothesis_verdict:       [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:         [2-3 sentences integrating S2, S3, S4 with displacement verdict]
  confidence_composite:     [confidence_post_cr -- final after all reductions]
  key_risk:                 [primary adoption risk framed as residual incumbent strength]
  topic_story_readiness:    "Evidence brief complete. Displacement case: [displacement_conclusion].
                             Confidence: [value]. Ready for /topic-story."

### HANDOFF

SESSION INVARIANT C enforced. Every field you write carries [derived from: X].
Unlabeled = format error.

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
  "STAGE 5 EXIT: synthesis_complete -- Evidence brief ready for topic-story."

You write: {topic}-synthesis-{date}.md
You write: {topic}-handoff-{date}.md
You confirm both writes. Campaign complete.
```

---

## V-05 -- Full: All Three Axes + Complete R19 Baseline

**Axis**: phrasing_register + role_sequence + evidence_quality_mandatory (combined)
**Hypothesis**: V-01, V-02, and V-03 are structurally orthogonal. V-01 changes instruction
voice. V-02 changes role execution order to surface the blocking dependency. V-03 adds mandatory
quality assessment at each evidence stage with carry-forward to synthesis. Combining all three on
top of the complete R19 baseline (RESUME AUDIT, count-gated exits S2>=5/S3>=3/S4>=3, three-block
Stage 5 with confidence chain, counter-hypothesis resolution, and ATOMIC DUAL-LOCK, HANDOFF with
derivation annotations) tests whether the full stack simultaneously addresses C-01, C-03, C-04,
C-06, C-08, C-09, and C-10 without introducing structural contradiction. The THIN-EVIDENCE CARRY
block (V-03) precedes BLOCK 1 and feeds the confidence chain directly, adding one new chain input
without restructuring the existing three-block synthesis. ROLE B running first (V-02) reorders the
Stage 0 clearance steps. Second-person register (V-01) applies throughout without structural change.

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
ENTRY CONDITIONS and a named EXIT SIGNAL. You do not begin any stage body until entry
conditions confirm.

---

## CAMPAIGN OPEN

  topic:                 {topic}
  date:                  {date}
  status_quo_comparator: [you name the incumbent approach this topic must displace]

### INCUMBENT ANCHOR

You fill this section before you run any role or register any invariant.

  incumbent_name:          [full name of status_quo_comparator]
  incumbent_strength:      [one sentence: why the incumbent is currently winning]
  incumbent_vulnerability: [one sentence: where the incumbent is most exposed to {topic}]

### SESSION INVARIANTS TABLE

SESSION INVARIANT D leads. You register all four before any role executes. Each carries:
"you cannot modify or bypass this at any subsequent stage."

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
       |                           | You cannot modify or bypass this at any stage.
  -----|---------------------------|------------------------------------------------------
  A    | ADVERSARIAL REVIEWER      | adversarial_reviewer_type: [the role most likely to
       | TYPE                      |   challenge the displacement claim].
       |                           | Activation: null_tally_final >= 3.
       |                           | You cannot modify or bypass this at synthesis.
  -----|---------------------------|------------------------------------------------------
  B    | CONFIDENCE CAP            | null_ce_cap_rule: confidence_composite -= 2 if
       |                           |   null_tally_final >= 3 (hard cap).
       |                           | You cannot soften or override this at synthesis.
  -----|---------------------------|------------------------------------------------------
  C    | DERIVATION ANNOTATION     | annotation_rule: Every handoff field you write carries
       |                           |   [derived from: X]. Unlabeled = format error.
       |                           | You cannot modify or bypass this at synthesis.

### ROLE OWNERSHIP TABLE

ROLE B executes FIRST. It is the primary blocking gate: if gate_s_cleared = false you halt
the campaign immediately. ROLE C and ROLE A cannot execute until ROLE B clears.
You run roles in order: B -> C -> A.

  ROLE   | TITLE                    | OWNED FIELD               | DEPENDENCY
  -------|--------------------------|---------------------------|---------------------------
  ROLE B | SCOUT LOADER             | gate_s_cleared            | NONE -- you run this first
  ROLE C | INCUMBENT THREAT ANALYST | incumbent_threat_locked   | depends on ROLE B (gate_s_cleared = true)
  ROLE A | HYPOTHESIS ARCHITECT     | invariant_registry_confirmed | depends on ROLE B and ROLE C

ROLE B (you execute now -- CAMPAIGN BLOCKED if scout absent):
  scout_artifact:  [{topic}-scout-record-{date}.md or equivalent]
  scout_loaded:    [true / false]
  gate_s_cleared:  [true if scout_loaded; CAMPAIGN BLOCKED otherwise]

  If gate_s_cleared = false: you emit "CAMPAIGN BLOCKED -- scout artifact not found.
    Locate {topic}-scout-record-{date}.md before proceeding." and you STOP.

ROLE C (you execute now -- only if gate_s_cleared = true):
  You read the INCUMBENT ANCHOR above. You confirm the analysis is complete.
  incumbent_threat_locked: [true when incumbent_name, strength, vulnerability all filled]

ROLE A (you execute now -- only if gate_s_cleared = true and incumbent_threat_locked = true):
  You confirm all four SESSION INVARIANT TABLE rows are filled and active.
  invariant_registry_confirmed: [true when all four invariants registered]

---

## RESUME AUDIT

You run this before Stage 0. You glob existing artifacts for {topic} on {date}.

For each stage artifact, you record: FOUND (Y/N) and DECISION (RESUME-SKIP / RUN).

1. Stage 1 -- {topic}-hypothesis-{date}.md:   found=[Y/N]  decision=[RESUME-SKIP / RUN]
2. Stage 2 -- {topic}-websearch-{date}.md:    found=[Y/N]  decision=[RESUME-SKIP / RUN]
3. Stage 3 -- {topic}-interview-{date}.md:    found=[Y/N]  decision=[RESUME-SKIP / RUN]
4. Stage 4 -- {topic}-prototype-{date}.md:    found=[Y/N]  decision=[RESUME-SKIP / RUN]
5. Stage 5 -- {topic}-synthesis-{date}.md:    found=[Y/N]  decision=[RESUME-SKIP / RUN]

  resume_audit_complete: [true]
  stages_to_run:         [list stages with RUN decision, or ALL if none found]

RESUME AUDIT EXIT: If all five stages are RESUME-SKIP, you emit:
  "RESUME_AUDIT_EXIT -- All stage artifacts already present. Campaign complete. No stages re-run."
  and you STOP. Otherwise: "RESUME_AUDIT_PASS -- Stages to run: [list]. Proceeding to Stage 0."

---

## STAGE 0 -- GATE S

STAGE 0 ENTRY CONDITIONS:
  [ ] RESUME AUDIT completed -- resume_audit_complete = true
  [ ] CAMPAIGN OPEN fields filled (topic, date, status_quo_comparator)
  [ ] INCUMBENT ANCHOR filled (incumbent_name, strength, vulnerability)
  [ ] All four SESSION INVARIANTS registered
  [ ] ROLE B executed FIRST -- gate_s_cleared confirmed (you cannot proceed otherwise)
  [ ] ROLE C executed -- incumbent_threat_locked = true
  [ ] ROLE A executed -- invariant_registry_confirmed = true

STAGE 0 BODY:

You check clearance for each step and record confirm or BLOCKED.
Steps reordered to match role execution dependency (B -> C -> A):
  Step 1: gate_s_cleared (ROLE B required -- primary gate)   = [confirm or BLOCKED]
  Step 2: incumbent_threat_locked (ROLE C required)          = [confirm or BLOCKED]
  Step 3: invariant_registry_confirmed (ROLE A required)     = [confirm or BLOCKED]

The first BLOCKED step halts the campaign. You record the step number and owning role.

STAGE 0 EXIT SIGNAL: gate_open
  "STAGE 0 EXIT: gate_open -- Steps 1, 2, 3 all confirmed. SESSION INVARIANT D active.
   Advancing to Stage 1."

---

## STAGE 1 -- HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] STAGE 0 EXIT SIGNAL received: gate_open
  [ ] RESUME AUDIT: Stage 1 decision = RUN (you skip entire stage body if RESUME-SKIP)
  [ ] scout_artifact path available from ROLE B
  [ ] SESSION INVARIANT D templates registered

STAGE 1 BODY:
You load the scout artifact from the path in ROLE B. You read the signals. You frame the
hypothesis.

  source_scout_artifact:        [path from ROLE B -- you copy this, do not infer]
  hypothesis:                   [falsifiable claim about {topic}]
  counter_hypothesis:           [incumbent's best defense -- grounded in ROLE C analysis]
  confidence_prior:             [initial confidence score: 1-10]
  gate_s_cleared:               [true -- from GATE S Step 1]
  invariant_registry_confirmed: [true -- from GATE S Step 3]
  incumbent_threat_locked:      [true -- from GATE S Step 2]

You write: {topic}-hypothesis-{date}.md. You confirm the write.

STAGE 1 EXIT SIGNAL: hypothesis_locked(confidence_prior=[value])
  "STAGE 1 EXIT: hypothesis_locked -- {topic}-hypothesis-{date}.md written.
   confidence_prior=[value]. Stage 2 ready."

---

## STAGE 2 -- WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] STAGE 1 EXIT SIGNAL received: hypothesis_locked(confidence_prior=[value])
  [ ] RESUME AUDIT: Stage 2 decision = RUN (you skip if RESUME-SKIP)
  [ ] hypothesis artifact confirmed written
  [ ] SESSION INVARIANT D Stage 2 template active

STAGE 2 BODY:

You gather at least 5 external sources. For each, you record:

  Source N:
    url_or_citation: [source]
    summary:         [1 sentence]
    verdict:         "Does [item N] support displacement of {status_quo_comparator}
                      by {topic} on [dimension]? [Yes / No / Inconclusive]"

You record after all sources are gathered:

  s2_count:                   [N -- must be >= 5]
  s2_incumbent_check_summary: [N support / M counter / P inconclusive]
  s2_ce_verdict:              [null if no CE; cite item if found]
  confidence_delta_s2:        [+1 / 0 / -1 based on evidence weight]
  running_confidence:         [confidence_prior + confidence_delta_s2]
  evidence_quality:           [thin / moderate / strong]
  evidence_quality_note:      [required if thin -- one sentence: why this stage's evidence
                               is thin or conflicting. Omit if moderate or strong.]

Running null tally: "Running tally: [N] null across 1 stage complete. 2 stages remain."

GATE: You do not fire the exit signal until s2_count >= 5. If s2_count < 5, you gather
additional external sources before proceeding.

You write: {topic}-websearch-{date}.md. You confirm the write.

STAGE 2 EXIT SIGNAL: websearch_complete(count=[N], running_confidence=[value], quality=[value])
  "STAGE 2 EXIT: websearch_complete -- s2_ce_verdict=[value]. s2_count=[N] (gate >= 5 met).
   running_confidence=[value]. evidence_quality=[value]. Stage 3 ready."

---

## STAGE 3 -- INTERVIEW

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT SIGNAL received: websearch_complete(...)
  [ ] RESUME AUDIT: Stage 3 decision = RUN (you skip if RESUME-SKIP)
  [ ] s2_ce_verdict recorded (null or value -- not blank)
  [ ] SESSION INVARIANT D Stage 3 template active

STAGE 3 BODY:

You simulate at least 3 practitioner interviews. For each, you record:

  Practitioner N:
    type:    [practitioner type]
    account: [key quote or paraphrase -- 1 sentence]
    verdict: "Does [account N] reveal a viable transition path from {status_quo_comparator}
              to {topic} for [use case]? [Yes / No / Inconclusive]"

You record after all interviews are complete:

  s3_count:                   [N -- must be >= 3]
  s3_incumbent_check_summary: [N support / M counter / P inconclusive]
  s3_ce_verdict:              [null if no CE; cite account if found]
  confidence_delta_s3:        [+1 / 0 / -1]
  running_confidence:         [prev + confidence_delta_s3]
  evidence_quality:           [thin / moderate / strong]
  evidence_quality_note:      [required if thin -- one sentence: why practitioner accounts
                               are thin or conflicting. Omit if moderate or strong.]

Running null tally: "Running tally: [N] null across 2 stages complete. 1 stage remains."

GATE: You do not fire the exit signal until s3_count >= 3. If s3_count < 3, you simulate
additional practitioner interviews before proceeding.

You write: {topic}-interview-{date}.md. You confirm the write.

STAGE 3 EXIT SIGNAL: interview_complete(count=[N], running_confidence=[value], quality=[value])
  "STAGE 3 EXIT: interview_complete -- s3_ce_verdict=[value]. s3_count=[N] (gate >= 3 met).
   running_confidence=[value]. evidence_quality=[value]. Stage 4 ready."

---

## STAGE 4 -- PROTOTYPE

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT SIGNAL received: interview_complete(...)
  [ ] RESUME AUDIT: Stage 4 decision = RUN (you skip if RESUME-SKIP)
  [ ] s3_ce_verdict recorded (null or value -- not blank)
  [ ] SESSION INVARIANT D Stage 4 template active

STAGE 4 BODY:

You design and assess at least 3 prototype experiments. For each, you record:

  Experiment N:
    design:  [what was built or tested -- 1 sentence]
    result:  [what was learned -- 1-2 sentences]
    verdict: "Does [result N] make a credible case for displacing {status_quo_comparator}
              with {topic}? [Yes / No / Pending]"

You record after all experiments are complete:

  s4_count:                [N -- must be >= 3]
  s4_displacement_verdict: [Yes / No / Pending -- required; omission = format error]
  s4_ce_verdict:           [null if no CE; description if found]
  confidence_delta_s4:     [+1 / 0 / -1]
  running_confidence:      [prev + confidence_delta_s4]
  evidence_quality:        [thin / moderate / strong]
  evidence_quality_note:   [required if thin -- one sentence: why prototype results are
                            thin or inconclusive. Omit if moderate or strong.]

Final null tally:
  null_tally_final = [N]
  Cross-check: "Running count from Stage 3 was [M]. Final is [N]. Match: [true/false]."

GATE: You do not fire the exit signal until s4_count >= 3. If s4_count < 3, you design
additional prototype experiments before proceeding.

You write: {topic}-prototype-{date}.md. You confirm the write.

STAGE 4 EXIT SIGNAL: prototype_complete(count=[null_tally_final], running_confidence=[value], quality=[value])
  "STAGE 4 EXIT: prototype_complete -- s4_ce_verdict=[value]. null_tally_final=[N].
   running_confidence=[value]. evidence_quality=[value]. Stage 5 ready."

---

## STAGE 5 -- SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT SIGNAL received: prototype_complete(...)
  [ ] RESUME AUDIT: Stage 5 decision = RUN (you skip if RESUME-SKIP)
  [ ] null_tally_final recorded
  [ ] counter_hypothesis from Stage 1 available
  [ ] All four SESSION INVARIANTS active

STAGE 5 BODY: THIN-EVIDENCE CARRY, then THREE-BLOCK STRUCTURE.
You do not populate any synthesis fields until you receive BLOCK 3 COMPLETE.

### THIN-EVIDENCE CARRY

You run this before BLOCK 1. For each stage where evidence_quality = thin, you record:

  Thin Stage N (Stage [2/3/4]):
    evidence_quality:          thin
    evidence_quality_note:     [copy from that stage's exit signal parameter]
    hypothesis_claim_weakened: [which specific hypothesis claim this thin stage fails to support]
    confidence_penalty:        [-1]

  thin_stages:           [list stage numbers rated thin, or "none"]
  thin_evidence_penalty: [sum of confidence_penalty values -- 0 if no thin stages]

THIN-EVIDENCE CARRY COMPLETE: "THIN-EVIDENCE CARRY COMPLETE -- thin_stages=[list].
  thin_evidence_penalty=[value]."

### BLOCK 1 -- CONFIDENCE CHAIN RESOLUTION

(You incorporate thin_evidence_penalty from THIN-EVIDENCE CARRY.)

  confidence_prior:          [value from Stage 1]
  confidence_delta_s2:       [+/- from Stage 2]
  confidence_delta_s3:       [+/- from Stage 3]
  confidence_delta_s4:       [+/- from Stage 4]
  thin_evidence_penalty:     [from THIN-EVIDENCE CARRY]
  chain_equation:            [prior + s2 + s3 + s4 + thin_penalty = sum]
  null_cap_applied:          [yes -- sum -= 2 if null_tally_final >= 3; no otherwise]
  confidence_chain_resolved: [final value after cap and thin penalty]

BLOCK 1 COMPLETE: "BLOCK 1 COMPLETE -- confidence_chain_resolved = [value]
  (thin_evidence_penalty = [value] incorporated)."

### BLOCK 2 -- COUNTER-HYPOTHESIS RESOLUTION

For each counter-hypothesis from Stage 1, you record:
  Counter N:
    text:     [counter-hypothesis text]
    verdict:  [REFUTED / PARTIALLY REFUTED / OPEN RISK]
    evidence: [cite stage artifact]

  open_risk_count:          [N -- count of OPEN RISK verdicts]
  cr_delta:                 [open_risk_count * -1]
  confidence_post_cr:       [confidence_chain_resolved + cr_delta]
  counter_hypothesis_verdict: [recorded]

BLOCK 2 COMPLETE: "BLOCK 2 COMPLETE -- counter_hypothesis_verdict recorded.
  confidence_post_cr = [value]."

### BLOCK 3 -- DISPLACEMENT INTEGRITY CHECK

You require BLOCK 1 COMPLETE and BLOCK 2 COMPLETE before you begin this block.

ATOMIC DUAL-LOCK:

  Null tally chain reconstruction:
    s2_ce_verdict: [null or value -- from Stage 2 artifact]
    s3_ce_verdict: [null or value -- from Stage 3 artifact]
    s4_ce_verdict: [null or value -- from Stage 4 artifact]
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
  consistency_flag: [CONSISTENT / INCONSISTENT -- mismatch requires justification]

BLOCK 3 COMPLETE: "BLOCK 3 COMPLETE -- displacement_conclusion = [value].
  co_activation_confirmed = [value]."

### SYNTHESIS BODY

(You do not populate until you receive BLOCK 3 COMPLETE.)

  displacement_conclusion:  [from BLOCK 3]
  hypothesis_verdict:       [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  evidence_summary:         [2-3 sentences integrating S2, S3, S4 with displacement verdict
                             and explicit mention of any thin stages from THIN-EVIDENCE CARRY]
  confidence_composite:     [confidence_post_cr -- final after all reductions]
  key_risk:                 [primary adoption risk framed as residual incumbent strength]
  topic_story_readiness:    "Evidence brief complete. Displacement case: [displacement_conclusion].
                             Confidence: [value]. Ready for /topic-story."

### HANDOFF

SESSION INVARIANT C enforced. Every field you write carries [derived from: X].
Unlabeled = format error.

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
  "STAGE 5 EXIT: synthesis_complete -- Evidence brief ready for topic-story."

You write: {topic}-synthesis-{date}.md
You write: {topic}-handoff-{date}.md
You confirm both writes. Campaign complete.
```

---

## Axis Summary

| Variation | Axis | Single/Combined | Primary criteria targeted |
|-----------|------|-----------------|--------------------------|
| V-01 | phrasing_register | single | C-01, C-03 (execution fidelity) |
| V-02 | role_sequence | single | C-06, C-10 (structural gate, blocking) |
| V-03 | evidence_quality_mandatory | single | C-08, C-09 (gaps flagged, thin-evidence carry) |
| V-04 | phrasing_register + role_sequence | combined | C-01, C-03, C-06, C-10 |
| V-05 | all three + full R19 baseline | full | C-01, C-03, C-04, C-06, C-08, C-09, C-10 |
