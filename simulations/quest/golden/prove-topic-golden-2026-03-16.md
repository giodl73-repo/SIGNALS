Written to `simulations/quest/golden/prove-topic-golden-2026-03-16.md`.

**Winning variation**: V-05 (R20) — score **90** (60 + 20 + 10), all 5 essential pass.

**What made it golden** (five patterns):

1. **ROLE B as primary blocking gate** — moves scout check from named anchor to structural halt; ROLE C/A cannot execute until `gate_s_cleared = true`. C-10 and C-06 go from partial to full.

2. **Second-person direct register throughout** — "You fill this before any role" vs "Fill before any role" eliminates actor ambiguity on every instruction. Directly supports C-01 and C-03 execution fidelity.

3. **Mandatory `evidence_quality` field at S2/S3/S4** — `[thin / moderate / strong]` with required `evidence_quality_note` if thin. Converts C-08 from organic observation to a structural format requirement.

4. **THIN-EVIDENCE CARRY block before BLOCK 1** — enumerates thin stages, names weakened claims, computes `thin_evidence_penalty` fed into `chain_equation`. C-09 is now enforced, not optional. `evidence_summary` must mention thin stages.

5. **All three axes are orthogonal on the complete R19 stack** — voice, execution order, and quality fields stack without contradiction. RESUME AUDIT, count gates, three-block synthesis, ATOMIC DUAL-LOCK, and HANDOFF annotations are all preserved intact.

**One remaining gap**: C-07 (inline citation traceability on individual S2/S3/S4 source items) is still partial — the HANDOFF enforces derivation but per-source citations aren't required. Future round target.
entence: where the incumbent is most exposed to {topic}]

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

## What Made It Golden

**1. ROLE B as primary blocking gate (role_sequence axis)**
Moving ROLE B to execute first converts the scout check from a named anchor into a structural
halt. If `gate_s_cleared = false`, the prompt emits CAMPAIGN BLOCKED and stops before ROLE C
or ROLE A can run. The dependency chain (B -> C -> A) and the Stage 0 step ordering both
reflect this. C-10 (structural block before hypothesis) and C-06 (gate enforces scout presence)
go from partial to full.

**2. Second-person direct register throughout (phrasing_register axis)**
Every imperative is addressed to "you" ("You fill this before any role", "You confirm the
analysis is complete", "You cannot modify or bypass this"). This eliminates the ambiguity of
formal passive constructions where the actor is implicit. C-01 and C-03 compliance no longer
depends on the model inferring who acts.

**3. Mandatory evidence_quality field at each evidence stage (evidence_quality_mandatory axis)**
S2, S3, and S4 each require `evidence_quality: [thin / moderate / strong]` with a required
`evidence_quality_note` if thin. This converts C-08 (gaps flagged at discovery) from organic
observation to a structural format requirement. A missing or unlabeled field is an omission,
not a style choice.

**4. THIN-EVIDENCE CARRY block before BLOCK 1 (evidence_quality_mandatory axis)**
Stage 5 opens by enumerating every thin stage, naming the weakened hypothesis claim, and
computing `thin_evidence_penalty` (sum of -1 per thin stage). That penalty feeds directly
into the `chain_equation` in BLOCK 1. C-09 (thin-evidence propagates to synthesis with
confidence qualification) is structurally enforced. The `evidence_summary` field is required
to mention thin stages explicitly.

**5. All three axes are orthogonal on the complete R19 structural stack**
`phrasing_register` changes instruction voice only. `role_sequence` changes execution order
and adds a halt guard. `evidence_quality_mandatory` adds fields and a carry block without
restructuring the three-block synthesis. The complete R19 baseline (RESUME AUDIT, count gates
S2>=5/S3>=3/S4>=3, three-block Stage 5, ATOMIC DUAL-LOCK, HANDOFF with derivation annotations)
is preserved intact. There is no structural contradiction between the three axes.

---

## Final Rubric Criteria

**Rubric**: v14 | **Threshold**: all 5 essential pass AND composite >= 80

| Criterion | Weight | V-05 | What it tests |
|-----------|--------|------|---------------|
| C-01 | Essential | PASS | All five sub-skills in sequence |
| C-02 | Essential | PASS | Scout artifact named before hypothesis formation |
| C-03 | Essential | PASS | Progressive artifact writes -- one per stage |
| C-04 | Essential | PASS | Synthesis explicitly signals readiness for topic-story |
| C-05 | Essential | PASS | Artifact naming convention followed |
| C-06 | Recommended | PASS | Gate enforces scout presence (blocks if absent) |
| C-07 | Recommended | PARTIAL | Evidence chain cited to source / citation traceability |
| C-08 | Recommended | PASS | Evidence quality assessed at each discovery stage |
| C-09 | Aspirational | PASS | Thin-evidence gaps carried forward to synthesis |
| C-10 | Aspirational | PASS | Structural block before hypothesis (ROLE B gate) |

**Score**: (5/5 x 60) + (2/3 x 30) + (2/2 x 10) = 60 + 20 + 10 = **90**

**C-07 note**: Citation traceability remains partially organic. The HANDOFF TABLE enforces
`[derived from: X]` on synthesis fields but does not require inline citations on individual
source items in S2/S3/S4 body. This is the one remaining gap for a future round.
