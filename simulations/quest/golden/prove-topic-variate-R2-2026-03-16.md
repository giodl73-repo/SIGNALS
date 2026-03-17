---
skill: quest-variate
skill_target: prove-topic
round: R2
date: 2026-03-16
rubric: prove-topic-rubric-v2-2026-03-16.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [enforcement_language, standalone_invariants_block, synthesis_field_isolation]
  combined: [V-04 (enforcement_language + standalone_block), V-05 (all_three_new + displacement_framing)]
round_targets: >
  v2 adds C-11/C-12/C-13 extracted from R1 failure modes.
  C-11 targets V-03 regression (62): advisory enforcement language disabled C-03/C-05.
  C-12 targets V-02 regression (76): inline invariants without standalone block degraded essentials.
  C-13 targets V-04 regression (85): narrative framing buried synthesis fields, passing C-04 but
  failing extractability. All five R2 variations maintain all 5 essentials and all 3 recommended.
  The axis in each variation determines which aspirational criteria it defends.
r1_scores:
  V-01: 90  # lifecycle emphasis — kept mechanical enforcement language intact
  V-02: 76  # output format — compressed preamble buried invariants inline
  V-03: 62  # inertia framing — softened enforcement to advisory; C-03/C-05 regressed
  V-04: 85  # combined phrasing+format — narrative buried confidence_composite and key_risk
  V-05: 88  # combined all four — solid but C-13 not targeted
---

# prove-topic -- Variation Round R2

Five complete, runnable skill body prompts targeting rubric v2.
Each is self-contained -- no diff, no cross-references between variations.

Axes: V-01 isolates enforcement language (C-11). V-02 isolates standalone invariants block (C-12).
V-03 isolates synthesis field isolation (C-13). V-04 combines C-11+C-12. V-05 combines all three
new criteria plus displacement framing (C-10).

All five include: 6 EXIT SIGNALs in order (C-01), 6 artifact writes with confirmation (C-02),
Invariant D templates verbatim at S2/S3/S4 (C-03), synthesis verdict fields (C-04), null tally
chain with cross-check (C-05), ROLE B scout loader (C-06), HANDOFF TABLE 11 fields (C-07),
counter-hypothesis resolution (C-08).

---

## V-01 -- Axis: Enforcement Language Mechanical (C-11)

**Variation axis**: Every SESSION INVARIANT enforcement checkpoint uses explicit hard-failure verbs
at the point of application -- not advisory phrasing. "deviation = FORMAT ERROR", "mismatch =
INTEGRITY FAILURE", "unlabeled field = FAIL", "batched write = ORDER ERROR". These appear inline
at each stage where the invariant fires, making soft drift structurally impossible without a
visible violation label. The SESSION INVARIANTS block is present (C-12 baseline), synthesis fields
are isolated (C-13 baseline), but the primary designed choice is the mechanical register at the
enforcement site.

**Hypothesis**: Advisory phrasing at invariant checkpoints is the root cause of C-03 and C-05
regressions under inertia framing (V-03, score 62). When each invariant checkpoint carries an
explicit failure label, the label functions as a commitment device -- the model cannot soften the
template wording without producing a visible "FORMAT ERROR" call that would mark the output
non-compliant. C-11 is not style; it is the structural enforcement mechanism for C-03 and C-05.

---

```
Topic: {topic}
Date:  {date}
Incumbent: {incumbent}

You are running the full prove evidence campaign for {topic}.
Goal: build six artifacts that support or refute the displacement claim.
Six stages. Each stage writes its artifact at CLOSE before advancing.

---

## SESSION INVARIANTS

Invariant A -- ADVERSARIAL REVIEWER
  Activation: null_tally_final >= 3.
  Register adversarial_reviewer_type at Stage 1 OPEN.
  If threshold met at Stage 5: Lock 1 fires -- name the registered reviewer type.
  Missing Lock 1 when threshold met = DUAL-LOCK ERROR.

Invariant B -- CONFIDENCE CAP (dual-lock with A)
  Activation: null_tally_final >= 3 (co-activates with A).
  Apply confidence_composite -= 2 and state the hard-cap note at Stage 5.
  Missing cap when threshold met = DUAL-LOCK ERROR.

Invariant C -- ONE WRITE PER STAGE
  Activation: every stage CLOSE.
  Write the artifact at CLOSE before moving to the next stage.
  Batched writes (any artifact written out of stage sequence) = ORDER ERROR.

Invariant D -- DISPLACEMENT TEMPLATE (verbatim)
  Activation: every INCUMBENT CHECK TABLE at Stages 2, 3, 4.
  Stage 2 template: "Does [evidence item] support the displacement of [incumbent] by [topic]?"
  Stage 3 template: "Does [practitioner account] reveal a viable transition path from [incumbent]
    to [topic]?"
  Stage 4 template: "Does [prototype result] make a credible case for displacing [incumbent]
    with [topic]?"
  Any deviation from the registered template wording = FORMAT ERROR.

---

## ROLE B -- SCOUT LOADER

Execute before Stage 1.

  scout_artifact: simulations/scout/record/{topic}-scout-record-{date}.md
  scout_loaded: [ ] true  [ ] false
  gate_s_cleared: true | false

If gate_s_cleared = false:
  Output: "CAMPAIGN BLOCKED: scout record absent at expected path."
  Do not proceed.

EXIT SIGNAL: gate_open

---

## STAGE 1 -- Hypothesis

OPEN: Load scout artifact. Identify the core claim the scout evidence supports.
Register: adversarial_reviewer_type (for Invariant A).
Name the incumbent: {incumbent}.

Frame:
  hypothesis:             [one sentence -- what {topic} enables that {incumbent} cannot]
  counter_hypothesis:     [one sentence -- {incumbent}'s strongest defense]
  adversarial_reviewer_type: [registered for Invariant A]
  scout_anchor:           [key finding from scout that grounds the hypothesis]

CLOSE -- write artifact (Invariant C: batched write = ORDER ERROR):
  path: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
  frontmatter:
    topic:                {topic}
    date:                 {date}
    scout_source:         simulations/scout/record/{topic}-scout-record-{date}.md
    hypothesis:           [displacement claim]
    counter_hypothesis:   [strongest opposing claim]
    adversarial_reviewer_type: [registered type]

Confirm write: "hypothesis artifact written."

EXIT SIGNAL: hypothesis_locked

---

## STAGE 2 -- Web Search

OPEN: Load simulations/prove/hypothesis/{topic}-hypothesis-{date}.md.
Prepare 3-5 search queries that test the hypothesis.

Run searches. Complete the INCUMBENT CHECK TABLE.

INCUMBENT CHECK TABLE -- Stage 2
(Invariant D: any deviation from template = FORMAT ERROR)

  | Evidence item | Does [evidence item] support the displacement of [incumbent] by [topic]? | Verdict |
  |---------------|-------------------------------------------------------------------------|---------|
  | [item 1]      | [answer]                                                                | Yes / Null |
  | ...           |                                                                         |         |

  s2_ce_verdict: Yes (at least one Yes) | Null (all Null)
  s2_null_count: [N]

CLOSE -- write artifact (Invariant C: batched write = ORDER ERROR):
  path: simulations/prove/websearch/{topic}-websearch-{date}.md
  frontmatter:
    topic:              {topic}
    date:               {date}
    hypothesis_source:  simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
    s2_ce_verdict:      [Yes | Null]
    s2_null_count:      [N]
  body: INCUMBENT CHECK TABLE, evidence summaries

Confirm write: "websearch artifact written."

EXIT SIGNAL: s2_complete

---

## STAGE 3 -- Interview (Practitioner Accounts)

OPEN: Load simulations/prove/hypothesis/{topic}-hypothesis-{date}.md.
Gather 3-5 practitioner accounts relevant to {topic}.

Complete the INCUMBENT CHECK TABLE.

INCUMBENT CHECK TABLE -- Stage 3
(Invariant D: any deviation from template = FORMAT ERROR)

  | Practitioner account | Does [practitioner account] reveal a viable transition path from
    [incumbent] to [topic]? | Verdict |
  |----------------------|--------------------------------------------------------------------------------------|---------|
  | [account 1]          | [answer]                                                                             | Yes / Null |
  | ...                  |                                                                                      |         |

  s3_ce_verdict: Yes (at least one Yes) | Null (all Null)
  s3_null_count: [N]
  running_null_tally: [s2_null_count + s3_null_count]

CLOSE -- write artifact (Invariant C: batched write = ORDER ERROR):
  path: simulations/prove/interview/{topic}-interview-{date}.md
  frontmatter:
    topic:              {topic}
    date:               {date}
    hypothesis_source:  simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
    s3_ce_verdict:      [Yes | Null]
    running_null_tally: [N]
  body: INCUMBENT CHECK TABLE, practitioner account summaries

Confirm write: "interview artifact written."

EXIT SIGNAL: s3_complete

---

## STAGE 4 -- Prototype (Displacement Testing)

OPEN: Load websearch and interview artifacts.
Design and evaluate a prototype test of the displacement claim.

Complete the INCUMBENT CHECK TABLE.

INCUMBENT CHECK TABLE -- Stage 4
(Invariant D: any deviation from template = FORMAT ERROR)

  | Prototype result | Does [prototype result] make a credible case for displacing [incumbent]
    with [topic]? | Verdict |
  |------------------|----------------------------------------------------------------------------|---------|
  | [result 1]       | [answer]                                                                   | Yes / Null |
  | ...              |                                                                            |         |

  s4_ce_verdict: Yes (at least one Yes) | Null (all Null)
  s4_null_count: [N]

STAGE 4 CLOSE -- NULL TALLY CROSS-CHECK
(Mismatch without integrity-failure flag = INTEGRITY FAILURE)

  Running count from Stage 3 was: [running_null_tally from interview artifact]
  Final count (s2 + s3 + s4): [N]
  Match: [true | false]
  null_tally_final: [N]
  incumbent_defense_closed: [true | false]

CLOSE -- write artifact (Invariant C: batched write = ORDER ERROR):
  path: simulations/prove/prototype/{topic}-prototype-{date}.md
  frontmatter:
    topic:                   {topic}
    date:                    {date}
    websearch_source:        simulations/prove/websearch/{topic}-websearch-{date}.md
    interview_source:        simulations/prove/interview/{topic}-interview-{date}.md
    s4_ce_verdict:           [Yes | Null]
    null_tally_final:        [N]
    incumbent_defense_closed: [true | false]
  body: INCUMBENT CHECK TABLE, prototype description, null tally cross-check

Confirm write: "prototype artifact written."

EXIT SIGNAL: s4_complete

---

## STAGE 5 -- Synthesis + Handoff

OPEN: Load all four prior artifacts:
  simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
  simulations/prove/websearch/{topic}-websearch-{date}.md
  simulations/prove/interview/{topic}-interview-{date}.md
  simulations/prove/prototype/{topic}-prototype-{date}.md

ATOMIC DUAL-LOCK CHECK
  null_tally_final: [from Stage 4 artifact]
  If null_tally_final >= 3:
    Lock 1 -- adversarial_reviewer_type: [name registered at Stage 1]
    Lock 2 -- confidence_composite -= 2 (hard-cap applied, state note)
    co_activation_confirmed: dual_lock_fired
  If null_tally_final < 3:
    co_activation_confirmed: not_triggered

NULL TALLY CHAIN RECONSTRUCTION
(Missing reconstruction = INTEGRITY FAILURE)
  S2 null count: [N]
  S3 null count: [N]
  S4 null count: [N]
  null_tally_final: [sum]
  Chain match: S2 + S3 + S4 = [N]. Match with Stage 4 declaration: [true | false]

COUNTER-HYPOTHESIS RESOLUTION TABLE
  | Field                | Value |
  |----------------------|-------|
  | counter_hypothesis   | [from Stage 1 artifact] |
  | verdict              | REFUTED / PARTIALLY REFUTED / OPEN RISK |
  | citation             | [stage and finding that resolves it] |
  | confidence_adjustment| [if OPEN RISK: -1 tier; otherwise: none] |

SYNTHESIS VERDICT BLOCK
(Each field must appear as a labeled declaration -- unlabeled field = FAIL)

  hypothesis_verdict:   SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED
  confidence_composite: [numeric value, 1-10, adjusted for dual-lock if applicable]
  key_risk:             [residual incumbent strength -- what {incumbent} still retains]

evidence_summary: [prose -- what the evidence shows; must cite: "Stage 4 displacement verdict:
  [Yes/No/Pending]"]

HANDOFF TABLE (unlabeled field = FAIL)
  | Field                      | Value                    | Derived from |
  |----------------------------|--------------------------|--------------|
  | scout_anchor               | [key scout claim]        | [derived from: scout artifact] |
  | incumbent_threat_locked    | [yes/no]                 | [derived from: Stage 4 incumbent_defense_closed] |
  | hypothesis                 | [displacement claim]     | [derived from: Stage 1 artifact] |
  | counter_hypothesis         | [opposing claim]         | [derived from: Stage 1 artifact] |
  | s2_ce_verdict              | [Yes/Null]               | [derived from: Stage 2 artifact] |
  | s3_ce_verdict              | [Yes/Null]               | [derived from: Stage 3 artifact] |
  | s4_ce_verdict              | [Yes/Null]               | [derived from: Stage 4 artifact] |
  | null_tally_final           | [N]                      | [derived from: Stage 4 null tally] |
  | co_activation_confirmed    | [fired/not_triggered]    | [derived from: dual-lock check above] |
  | incumbent_defense_closed   | [true/false]             | [derived from: Stage 4 artifact] |
  | confidence_composite       | [N]                      | [derived from: synthesis verdict block] |
  | schema_compliance_confirmed| true                     | [derived from: this table] |

CLOSE -- write artifacts (Invariant C: batched write = ORDER ERROR):

  path: simulations/prove/synthesize/{topic}-synthesize-{date}.md
  frontmatter:
    topic:              {topic}
    date:               {date}
    hypothesis_verdict: [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
    confidence_composite: [N]
  body: dual-lock check, chain reconstruction, counter-hyp table, verdict block, evidence_summary

  path: simulations/prove/handoff/{topic}-handoff-{date}.md
  frontmatter:
    topic:              {topic}
    date:               {date}
    synthesis_source:   simulations/prove/synthesize/{topic}-synthesize-{date}.md
  body: HANDOFF TABLE

Confirm writes: "synthesis artifact written. handoff artifact written."

EXIT SIGNAL: campaign_closed
```

---

## V-02 -- Axis: SESSION INVARIANTS Standalone Pre-Stage Block (C-12)

**Variation axis**: All four SESSION INVARIANTS appear in a dedicated, richly-structured TABLE before
Stage 0 executes. The table has five columns: Invariant | Description | Rule | Checkpoint | Failure
Label. After this table, no stage body re-states the invariant rule -- each stage references it by
label only ("Invariant D applies here"). The pre-stage block is the sole authoritative registration
of all invariant logic. Its structural position (before gate_open) forces verbatim attention before
execution begins. Enforcement language at each checkpoint is compact but mechanical ("Invariant D:
FORMAT ERROR if violated").

**Hypothesis**: V-02 in R1 (score 76) failed because compressing setup caused invariants to appear
only inline within stage bodies, which caused C-03 and C-05 to degrade to PARTIAL. The standalone
block forces the model to register all invariant rules once, completely, before any stage fires.
Inline references then carry only the label and failure verb -- no opportunity for rule drift. C-12
is the structural precondition for C-03 and C-05 compliance across all format and tone variations.

---

```
Topic: {topic}
Date:  {date}
Incumbent: {incumbent}

You are running the full prove evidence campaign for {topic}.
Six stages. One artifact per stage. Forward order only.

---

## SESSION INVARIANTS TABLE
(Registered here before any stage begins. All stages reference by label only.)

| Invariant | Description               | Rule                                                                                 | Checkpoint              | Failure Label    |
|-----------|---------------------------|--------------------------------------------------------------------------------------|-------------------------|------------------|
| A         | Adversarial reviewer      | If null_tally_final >= 3, name adversarial_reviewer_type and fire Lock 1 at Stage 5 | Stage 1 OPEN (register) | DUAL-LOCK ERROR  |
| B         | Confidence cap            | If null_tally_final >= 3, apply confidence_composite -= 2 with hard-cap note (co-activates with A) | Stage 5 verdict | DUAL-LOCK ERROR |
| C         | One write per stage       | Write artifact at stage CLOSE before advancing. No batching.                         | Every stage CLOSE       | ORDER ERROR      |
| D         | Displacement template     | Stage 2: "Does [evidence item] support the displacement of [incumbent] by [topic]?"  | Stage 2 INCUMBENT CHECK | FORMAT ERROR     |
|           |                           | Stage 3: "Does [practitioner account] reveal a viable transition path from [incumbent] to [topic]?" | Stage 3 INCUMBENT CHECK | FORMAT ERROR |
|           |                           | Stage 4: "Does [prototype result] make a credible case for displacing [incumbent] with [topic]?" | Stage 4 INCUMBENT CHECK | FORMAT ERROR |

This table is the authoritative source for all invariant logic. Inline stage references
use label + failure label only: "Invariant D applies -- FORMAT ERROR if violated."

---

## ROLE B -- SCOUT LOADER

  scout_artifact: simulations/scout/record/{topic}-scout-record-{date}.md
  scout_loaded:   [ ] true   [ ] false
  gate_s_cleared: true | false

If gate_s_cleared = false: "CAMPAIGN BLOCKED: scout record absent." Stop.

EXIT SIGNAL: gate_open

---

## STAGE 1 -- Hypothesis

Register for Invariant A: adversarial_reviewer_type = [name now].
Load scout artifact. Identify displacement claim.

  hypothesis:               [one sentence -- what {topic} enables that {incumbent} cannot]
  counter_hypothesis:       [one sentence -- {incumbent}'s strongest defense]
  scout_anchor:             [key scout finding grounding the claim]
  adversarial_reviewer_type: [registered]

Invariant C applies -- ORDER ERROR if write is deferred.
Write: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
  frontmatter: topic, date, scout_source, hypothesis, counter_hypothesis, adversarial_reviewer_type

Confirm: "hypothesis artifact written."

EXIT SIGNAL: hypothesis_locked

---

## STAGE 2 -- Web Search

Load simulations/prove/hypothesis/{topic}-hypothesis-{date}.md. Run 3-5 searches.

Invariant D applies -- FORMAT ERROR if template deviates.
INCUMBENT CHECK TABLE:
  | Evidence item | Does [evidence item] support the displacement of [incumbent] by [topic]? | Verdict |
  |---------------|-------------------------------------------------------------------------|---------|
  | [item 1]      | [answer]                                                                | Yes / Null |

  s2_ce_verdict: Yes | Null
  s2_null_count: [N]

Invariant C applies -- ORDER ERROR if write is deferred.
Write: simulations/prove/websearch/{topic}-websearch-{date}.md
  frontmatter: topic, date, hypothesis_source, s2_ce_verdict, s2_null_count
  body: INCUMBENT CHECK TABLE, evidence summaries

Confirm: "websearch artifact written."

EXIT SIGNAL: s2_complete

---

## STAGE 3 -- Interview (Practitioner Accounts)

Load simulations/prove/hypothesis/{topic}-hypothesis-{date}.md. Gather 3-5 accounts.

Invariant D applies -- FORMAT ERROR if template deviates.
INCUMBENT CHECK TABLE:
  | Practitioner account | Does [practitioner account] reveal a viable transition path from [incumbent] to [topic]? | Verdict |
  |----------------------|------------------------------------------------------------------------------------------|---------|
  | [account 1]          | [answer]                                                                                 | Yes / Null |

  s3_ce_verdict: Yes | Null
  s3_null_count: [N]
  running_null_tally: [s2 + s3]

Invariant C applies -- ORDER ERROR if write is deferred.
Write: simulations/prove/interview/{topic}-interview-{date}.md
  frontmatter: topic, date, hypothesis_source, s3_ce_verdict, running_null_tally
  body: INCUMBENT CHECK TABLE, account summaries

Confirm: "interview artifact written."

EXIT SIGNAL: s3_complete

---

## STAGE 4 -- Prototype (Displacement Testing)

Load websearch and interview artifacts.

Invariant D applies -- FORMAT ERROR if template deviates.
INCUMBENT CHECK TABLE:
  | Prototype result | Does [prototype result] make a credible case for displacing [incumbent] with [topic]? | Verdict |
  |------------------|--------------------------------------------------------------------------------------|---------|
  | [result 1]       | [answer]                                                                             | Yes / Null |

  s4_ce_verdict: Yes | Null
  s4_null_count: [N]

NULL TALLY CROSS-CHECK (Invariant -- mismatch = INTEGRITY FAILURE):
  Running count from Stage 3 was: [running_null_tally from interview artifact]
  Final count: [s2 + s3 + s4]
  Match: [true | false]
  null_tally_final: [N]
  incumbent_defense_closed: [true | false]

Invariant C applies -- ORDER ERROR if write is deferred.
Write: simulations/prove/prototype/{topic}-prototype-{date}.md
  frontmatter: topic, date, websearch_source, interview_source, s4_ce_verdict,
    null_tally_final, incumbent_defense_closed
  body: INCUMBENT CHECK TABLE, prototype description, null tally cross-check

Confirm: "prototype artifact written."

EXIT SIGNAL: s4_complete

---

## STAGE 5 -- Synthesis + Handoff

Load all four prior artifacts.

ATOMIC DUAL-LOCK CHECK (Invariants A + B):
  null_tally_final: [from Stage 4]
  If >= 3: Lock 1 fires (adversarial_reviewer_type: [registered at S1]) +
           Lock 2 fires (confidence_composite -= 2, hard-cap note stated).
           co_activation_confirmed: dual_lock_fired
  If < 3:  co_activation_confirmed: not_triggered

NULL TALLY CHAIN RECONSTRUCTION (Invariant -- missing reconstruction = INTEGRITY FAILURE):
  S2: [N]  S3: [N]  S4: [N]  Sum: [N]
  Match with Stage 4 null_tally_final: [true | false]

COUNTER-HYPOTHESIS RESOLUTION TABLE:
  | Field              | Value |
  |--------------------|-------|
  | counter_hypothesis | [from Stage 1] |
  | verdict            | REFUTED / PARTIALLY REFUTED / OPEN RISK |
  | citation           | [stage and finding] |
  | confidence_adjustment | [if OPEN RISK: -1 tier; else: none] |

SYNTHESIS VERDICT BLOCK:
  hypothesis_verdict:   SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED
  confidence_composite: [N, adjusted for dual-lock if applicable]
  key_risk:             [residual incumbent strength]

evidence_summary: [prose; must include "Stage 4 displacement verdict: [Yes/No/Pending]"]

HANDOFF TABLE (Invariant -- unlabeled field = FAIL):
  | Field                      | Value | Derived from |
  |----------------------------|-------|--------------|
  | scout_anchor               | ...   | [derived from: scout artifact] |
  | incumbent_threat_locked    | ...   | [derived from: Stage 4 incumbent_defense_closed] |
  | hypothesis                 | ...   | [derived from: Stage 1 artifact] |
  | counter_hypothesis         | ...   | [derived from: Stage 1 artifact] |
  | s2_ce_verdict              | ...   | [derived from: Stage 2 artifact] |
  | s3_ce_verdict              | ...   | [derived from: Stage 3 artifact] |
  | s4_ce_verdict              | ...   | [derived from: Stage 4 artifact] |
  | null_tally_final           | ...   | [derived from: Stage 4 null tally] |
  | co_activation_confirmed    | ...   | [derived from: dual-lock check] |
  | incumbent_defense_closed   | ...   | [derived from: Stage 4 artifact] |
  | confidence_composite       | ...   | [derived from: synthesis verdict block] |
  | schema_compliance_confirmed| true  | [derived from: this table] |

Invariant C applies -- ORDER ERROR if writes are batched or deferred.
Write: simulations/prove/synthesize/{topic}-synthesize-{date}.md
  frontmatter: topic, date, hypothesis_verdict, confidence_composite
  body: dual-lock check, chain reconstruction, counter-hyp table, verdict block, evidence_summary

Write: simulations/prove/handoff/{topic}-handoff-{date}.md
  frontmatter: topic, date, synthesis_source
  body: HANDOFF TABLE

Confirm: "synthesis artifact written. handoff artifact written."

EXIT SIGNAL: campaign_closed
```

---

## V-03 -- Axis: Stage 5 Synthesis Field Isolation (C-13)

**Variation axis**: Stage 5 uses a rigid SYNTHESIS DECLARATIONS section where each of the three
required fields appears as an explicit standalone key-value line, isolated from all prose, before
the evidence_summary block begins. The prompt names this section explicitly and states: "Each
declaration must appear on its own labeled line. Do not embed these values in prose sentences."
The HANDOFF TABLE uses the same isolation discipline: each field is a named cell, not a
narrative entry. This is the direct counter to the V-04 regression (score 85) where inertia
framing buried confidence_composite and key_risk as sub-items of a narrative paragraph.

**Hypothesis**: C-04 checks field presence; C-13 checks field extractability by pattern-match.
A model following inertia framing naturally wants to write "The evidence shows that {topic}
strongly supports displacement (confidence: 8/10), with the key risk being the incumbent's
existing integration." This sentence contains all three fields but none are extractable as
labeled declarations. Explicitly naming the SYNTHESIS DECLARATIONS section and requiring
key-value format before prose begins eliminates narrative burial as a structural option.

---

```
Topic: {topic}
Date:  {date}
Incumbent: {incumbent}

You are running the full prove evidence campaign for {topic}.
Six stages. One artifact per stage. Forward order only.

---

## SESSION INVARIANTS

Invariant A -- adversarial reviewer. Register adversarial_reviewer_type at Stage 1.
  Activate at Stage 5 if null_tally_final >= 3.

Invariant B -- confidence cap. Co-activates with A when null_tally_final >= 3.
  Apply confidence_composite -= 2 with hard-cap note.

Invariant C -- one write per stage. Artifact written at CLOSE before advancing.
  Batched write = ORDER ERROR.

Invariant D -- displacement template verbatim at Stages 2, 3, 4.
  Stage 2: "Does [evidence item] support the displacement of [incumbent] by [topic]?"
  Stage 3: "Does [practitioner account] reveal a viable transition path from [incumbent]
    to [topic]?"
  Stage 4: "Does [prototype result] make a credible case for displacing [incumbent]
    with [topic]?"
  Template deviation = FORMAT ERROR.

---

## ROLE B -- SCOUT LOADER

  scout_artifact: simulations/scout/record/{topic}-scout-record-{date}.md
  scout_loaded:   [ ] true   [ ] false
  gate_s_cleared: true | false

If gate_s_cleared = false: "CAMPAIGN BLOCKED: scout record absent." Stop.

EXIT SIGNAL: gate_open

---

## STAGE 1 -- Hypothesis

Load scout artifact. Register adversarial_reviewer_type for Invariant A.

  hypothesis:                [one sentence]
  counter_hypothesis:        [one sentence -- {incumbent}'s strongest defense]
  scout_anchor:              [key scout finding]
  adversarial_reviewer_type: [registered]

Write (Invariant C): simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
  frontmatter: topic, date, scout_source, hypothesis, counter_hypothesis,
    adversarial_reviewer_type

Confirm: "hypothesis artifact written."

EXIT SIGNAL: hypothesis_locked

---

## STAGE 2 -- Web Search

Load hypothesis artifact. Run 3-5 searches.

INCUMBENT CHECK TABLE (Invariant D: template deviation = FORMAT ERROR):
  | Evidence item | Does [evidence item] support the displacement of [incumbent] by [topic]? | Verdict |
  |---------------|-------------------------------------------------------------------------|---------|
  | [item 1]      | [answer]                                                                | Yes / Null |

  s2_ce_verdict: Yes | Null
  s2_null_count: [N]

Write (Invariant C): simulations/prove/websearch/{topic}-websearch-{date}.md
  frontmatter: topic, date, hypothesis_source, s2_ce_verdict, s2_null_count

Confirm: "websearch artifact written."

EXIT SIGNAL: s2_complete

---

## STAGE 3 -- Interview (Practitioner Accounts)

Load hypothesis artifact. Gather 3-5 practitioner accounts.

INCUMBENT CHECK TABLE (Invariant D: template deviation = FORMAT ERROR):
  | Practitioner account | Does [practitioner account] reveal a viable transition path from
    [incumbent] to [topic]? | Verdict |
  |----------------------|---------------------------------------------------------------------------------|---------|
  | [account 1]          | [answer]                                                                        | Yes / Null |

  s3_ce_verdict: Yes | Null
  s3_null_count: [N]
  running_null_tally: [s2 + s3]

Write (Invariant C): simulations/prove/interview/{topic}-interview-{date}.md
  frontmatter: topic, date, hypothesis_source, s3_ce_verdict, running_null_tally

Confirm: "interview artifact written."

EXIT SIGNAL: s3_complete

---

## STAGE 4 -- Prototype (Displacement Testing)

Load websearch and interview artifacts.

INCUMBENT CHECK TABLE (Invariant D: template deviation = FORMAT ERROR):
  | Prototype result | Does [prototype result] make a credible case for displacing [incumbent]
    with [topic]? | Verdict |
  |------------------|---------------------------------------------------------------------------|---------|
  | [result 1]       | [answer]                                                                  | Yes / Null |

  s4_ce_verdict: Yes | Null
  s4_null_count: [N]

NULL TALLY CROSS-CHECK:
  Running count from Stage 3: [N]
  Final count (s2 + s3 + s4): [N]
  Match: [true | false]
  null_tally_final: [N]
  incumbent_defense_closed: [true | false]

Write (Invariant C): simulations/prove/prototype/{topic}-prototype-{date}.md
  frontmatter: topic, date, s4_ce_verdict, null_tally_final, incumbent_defense_closed

Confirm: "prototype artifact written."

EXIT SIGNAL: s4_complete

---

## STAGE 5 -- Synthesis + Handoff

Load all four prior artifacts.

ATOMIC DUAL-LOCK CHECK:
  null_tally_final: [from Stage 4]
  If >= 3: Lock 1: adversarial_reviewer_type = [registered at Stage 1]
           Lock 2: confidence_composite -= 2, hard-cap note stated.
           co_activation_confirmed: dual_lock_fired
  If < 3:  co_activation_confirmed: not_triggered

NULL TALLY CHAIN RECONSTRUCTION:
  S2: [N]  S3: [N]  S4: [N]  Sum: [N]
  Match with Stage 4 null_tally_final: [true | false]

COUNTER-HYPOTHESIS RESOLUTION TABLE:
  | counter_hypothesis | [from Stage 1 artifact] |
  | verdict            | REFUTED / PARTIALLY REFUTED / OPEN RISK |
  | citation           | [stage and finding] |
  | confidence_adjustment | [if OPEN RISK: -1 tier; else: none] |

SYNTHESIS DECLARATIONS
(C-13: each field must appear as a labeled standalone declaration before evidence_summary.
Do not embed these values in prose sentences. Each on its own line, extractable by label.)

  hypothesis_verdict:   SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED
  confidence_composite: [numeric value, 1-10, adjusted for dual-lock if applicable]
  key_risk:             [residual incumbent strength -- stated as a standalone phrase]

EVIDENCE SUMMARY (begins only after SYNTHESIS DECLARATIONS are complete):
  evidence_summary: [prose; cite "Stage 4 displacement verdict: [Yes/No/Pending]" explicitly]

HANDOFF TABLE
(C-13 discipline: each field as a named cell, not embedded prose. Unlabeled field = FAIL.)

  | Field                      | Value | Derived from |
  |----------------------------|-------|--------------|
  | scout_anchor               | [key scout claim] | [derived from: scout artifact] |
  | incumbent_threat_locked    | [yes/no] | [derived from: Stage 4 incumbent_defense_closed] |
  | hypothesis                 | [claim] | [derived from: Stage 1 artifact] |
  | counter_hypothesis         | [opposing claim] | [derived from: Stage 1 artifact] |
  | s2_ce_verdict              | [Yes/Null] | [derived from: Stage 2 artifact] |
  | s3_ce_verdict              | [Yes/Null] | [derived from: Stage 3 artifact] |
  | s4_ce_verdict              | [Yes/Null] | [derived from: Stage 4 artifact] |
  | null_tally_final           | [N] | [derived from: Stage 4 null tally] |
  | co_activation_confirmed    | [fired/not_triggered] | [derived from: dual-lock check] |
  | incumbent_defense_closed   | [true/false] | [derived from: Stage 4 artifact] |
  | confidence_composite       | [N] | [derived from: synthesis declarations] |
  | schema_compliance_confirmed| true | [derived from: this table] |

Write (Invariant C):
  path: simulations/prove/synthesize/{topic}-synthesize-{date}.md
  frontmatter: topic, date, hypothesis_verdict, confidence_composite
  body: dual-lock check, chain reconstruction, counter-hyp table, SYNTHESIS DECLARATIONS
    (before prose), evidence_summary

  path: simulations/prove/handoff/{topic}-handoff-{date}.md
  frontmatter: topic, date, synthesis_source
  body: HANDOFF TABLE

Confirm: "synthesis artifact written. handoff artifact written."

EXIT SIGNAL: campaign_closed
```

---

## V-04 -- Combined: C-11 + C-12 (Enforcement Language + Standalone Block)

**Variation axes**: (1) SESSION INVARIANTS in a dedicated pre-stage TABLE with a Failure Label
column (C-12). (2) Mechanical enforcement language at every inline checkpoint where an invariant
fires: each reference names the invariant AND the failure label from the table (C-11). The SESSION
INVARIANTS TABLE becomes the source of truth for failure labels; inline checkpoints echo the label
verbatim. This creates a two-layer enforcement architecture: the table registers the rule and its
failure label; the inline checkpoint fires the label at the point of application.

**Hypothesis**: C-12 (standalone block) and C-11 (mechanical language) address the same failure
mode at different structural depths. C-12 prevents rule drift by centralizing invariant logic
before execution begins. C-11 prevents enforcement softening by requiring the failure label at
each firing site. Together they create redundant enforcement: a model that drifts from a template
at Stage 2 sees "FORMAT ERROR" both in the SESSION INVARIANTS TABLE (C-12) and in the Stage 2
inline checkpoint (C-11). V-04 tests whether this two-layer architecture yields better essential
compliance (C-03, C-05) than either layer alone.

---

```
Topic: {topic}
Date:  {date}
Incumbent: {incumbent}

You are running the full prove evidence campaign for {topic}.
Six stages. One artifact per stage. Forward order only.

---

## SESSION INVARIANTS TABLE
(Source of truth for all invariant rules and failure labels.
Inline stage references echo labels from this table verbatim.)

| Inv | Description               | Rule (condensed)                                                                    | Checkpoint              | Failure Label   |
|-----|---------------------------|-------------------------------------------------------------------------------------|-------------------------|-----------------|
| A   | Adversarial reviewer      | If null_tally_final >= 3, name reviewer type + fire Lock 1 at Stage 5               | Stage 1 (register) + S5 | DUAL-LOCK ERROR |
| B   | Confidence cap            | If null_tally_final >= 3, confidence_composite -= 2 + hard-cap note (co-locks w/ A) | Stage 5 verdict         | DUAL-LOCK ERROR |
| C   | One write per stage       | Artifact written at CLOSE, never deferred or batched                                | Every stage CLOSE       | ORDER ERROR     |
| D   | Displacement template     | S2: "Does [evidence item] support the displacement of [incumbent] by [topic]?"       | Stage 2 INCUMBENT CHECK | FORMAT ERROR    |
|     |                           | S3: "Does [practitioner account] reveal a viable transition path from [incumbent] to [topic]?" | Stage 3 INCUMBENT CHECK | FORMAT ERROR |
|     |                           | S4: "Does [prototype result] make a credible case for displacing [incumbent] with [topic]?" | Stage 4 INCUMBENT CHECK | FORMAT ERROR |

---

## ROLE B -- SCOUT LOADER

  scout_artifact: simulations/scout/record/{topic}-scout-record-{date}.md
  scout_loaded:   [ ] true   [ ] false
  gate_s_cleared: true | false

If gate_s_cleared = false: "CAMPAIGN BLOCKED: scout record absent." Stop.

EXIT SIGNAL: gate_open

---

## STAGE 1 -- Hypothesis

Register adversarial_reviewer_type (Invariant A: DUAL-LOCK ERROR if not registered here).
Load scout artifact.

  hypothesis:                [one sentence]
  counter_hypothesis:        [one sentence]
  scout_anchor:              [key scout finding]
  adversarial_reviewer_type: [registered -- Invariant A]

Invariant C: ORDER ERROR if write deferred.
Write: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
  frontmatter: topic, date, scout_source, hypothesis, counter_hypothesis,
    adversarial_reviewer_type

Confirm: "hypothesis artifact written."

EXIT SIGNAL: hypothesis_locked

---

## STAGE 2 -- Web Search

Load hypothesis artifact. Run 3-5 searches.

Invariant D: FORMAT ERROR if template deviates.
INCUMBENT CHECK TABLE:
  | Evidence item | Does [evidence item] support the displacement of [incumbent] by [topic]? | Verdict |
  |---------------|-------------------------------------------------------------------------|---------|
  | [item 1]      | [answer]                                                                | Yes / Null |

  s2_ce_verdict: Yes | Null
  s2_null_count: [N]

Invariant C: ORDER ERROR if write deferred.
Write: simulations/prove/websearch/{topic}-websearch-{date}.md
  frontmatter: topic, date, hypothesis_source, s2_ce_verdict, s2_null_count
  body: INCUMBENT CHECK TABLE, evidence summaries

Confirm: "websearch artifact written."

EXIT SIGNAL: s2_complete

---

## STAGE 3 -- Interview (Practitioner Accounts)

Load hypothesis artifact. Gather 3-5 practitioner accounts.

Invariant D: FORMAT ERROR if template deviates.
INCUMBENT CHECK TABLE:
  | Practitioner account | Does [practitioner account] reveal a viable transition path from
    [incumbent] to [topic]? | Verdict |
  |----------------------|---------------------------------------------------------------------------------|---------|
  | [account 1]          | [answer]                                                                        | Yes / Null |

  s3_ce_verdict: Yes | Null
  s3_null_count: [N]
  running_null_tally: [s2 + s3]

Invariant C: ORDER ERROR if write deferred.
Write: simulations/prove/interview/{topic}-interview-{date}.md
  frontmatter: topic, date, hypothesis_source, s3_ce_verdict, running_null_tally
  body: INCUMBENT CHECK TABLE, account summaries

Confirm: "interview artifact written."

EXIT SIGNAL: s3_complete

---

## STAGE 4 -- Prototype (Displacement Testing)

Load websearch and interview artifacts.

Invariant D: FORMAT ERROR if template deviates.
INCUMBENT CHECK TABLE:
  | Prototype result | Does [prototype result] make a credible case for displacing [incumbent]
    with [topic]? | Verdict |
  |------------------|---------------------------------------------------------------------------|---------|
  | [result 1]       | [answer]                                                                  | Yes / Null |

  s4_ce_verdict: Yes | Null
  s4_null_count: [N]

NULL TALLY CROSS-CHECK (mismatch without integrity-failure flag = INTEGRITY FAILURE):
  Running count from Stage 3: [N]
  Final count (s2 + s3 + s4): [N]
  Match: [true | false]
  null_tally_final: [N]
  incumbent_defense_closed: [true | false]

Invariant C: ORDER ERROR if write deferred.
Write: simulations/prove/prototype/{topic}-prototype-{date}.md
  frontmatter: topic, date, websearch_source, interview_source, s4_ce_verdict,
    null_tally_final, incumbent_defense_closed
  body: INCUMBENT CHECK TABLE, prototype description, null tally cross-check

Confirm: "prototype artifact written."

EXIT SIGNAL: s4_complete

---

## STAGE 5 -- Synthesis + Handoff

Load all four prior artifacts.

ATOMIC DUAL-LOCK CHECK (Invariants A + B: DUAL-LOCK ERROR if threshold met and lock not fired):
  null_tally_final: [from Stage 4]
  If >= 3: Lock 1 fires: adversarial_reviewer_type = [registered at Stage 1]
           Lock 2 fires: confidence_composite -= 2 (hard-cap note stated here)
           co_activation_confirmed: dual_lock_fired
  If < 3:  co_activation_confirmed: not_triggered

NULL TALLY CHAIN RECONSTRUCTION (missing reconstruction = INTEGRITY FAILURE):
  S2: [N]  S3: [N]  S4: [N]  Sum: [N]
  Match with Stage 4 null_tally_final: [true | false]

COUNTER-HYPOTHESIS RESOLUTION TABLE:
  | Field              | Value |
  |--------------------|-------|
  | counter_hypothesis | [from Stage 1] |
  | verdict            | REFUTED / PARTIALLY REFUTED / OPEN RISK |
  | citation           | [stage and finding] |
  | confidence_adjustment | [if OPEN RISK: -1 tier; else: none] |

SYNTHESIS VERDICT BLOCK:
  hypothesis_verdict:   SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED
  confidence_composite: [N, adjusted for dual-lock if applicable]
  key_risk:             [residual incumbent strength]

evidence_summary: [prose; cite "Stage 4 displacement verdict: [Yes/No/Pending]" explicitly]

HANDOFF TABLE (Invariant: unlabeled field = FAIL):
  | Field                      | Value | Derived from |
  |----------------------------|-------|--------------|
  | scout_anchor               | ... | [derived from: scout artifact] |
  | incumbent_threat_locked    | ... | [derived from: Stage 4 incumbent_defense_closed] |
  | hypothesis                 | ... | [derived from: Stage 1 artifact] |
  | counter_hypothesis         | ... | [derived from: Stage 1 artifact] |
  | s2_ce_verdict              | ... | [derived from: Stage 2 artifact] |
  | s3_ce_verdict              | ... | [derived from: Stage 3 artifact] |
  | s4_ce_verdict              | ... | [derived from: Stage 4 artifact] |
  | null_tally_final           | ... | [derived from: Stage 4 null tally] |
  | co_activation_confirmed    | ... | [derived from: dual-lock check] |
  | incumbent_defense_closed   | ... | [derived from: Stage 4 artifact] |
  | confidence_composite       | ... | [derived from: synthesis verdict block] |
  | schema_compliance_confirmed| true | [derived from: this table] |

Invariant C: ORDER ERROR if writes deferred or batched.
Write: simulations/prove/synthesize/{topic}-synthesize-{date}.md
  frontmatter: topic, date, hypothesis_verdict, confidence_composite
  body: dual-lock check, chain reconstruction, counter-hyp table, verdict block, evidence_summary

Write: simulations/prove/handoff/{topic}-handoff-{date}.md
  frontmatter: topic, date, synthesis_source
  body: HANDOFF TABLE

Confirm: "synthesis artifact written. handoff artifact written."

EXIT SIGNAL: campaign_closed
```

---

## V-05 -- Combined: All Three New Criteria + Displacement Framing (C-11 + C-12 + C-13 + C-10)

**Variation axes**: (1) C-11: mechanical enforcement language at every invariant checkpoint with
explicit failure labels. (2) C-12: rich SESSION INVARIANTS TABLE in standalone pre-stage block,
full five-column format, sole source of truth. (3) C-13: SYNTHESIS DECLARATIONS section in Stage
5 with each field isolated as a labeled standalone key-value line before any prose begins; prompt
explicitly prohibits narrative embedding. (4) C-10: incumbent displacement framing throughout --
CAMPAIGN OPEN names incumbent and its core strength; every stage body frames its evidence in
displacement terms ("Does this advance the displacement claim? Or does it reinforce {incumbent}?");
Stage 5 opens as "The case against {incumbent}."

**Hypothesis**: The four axes are designed to be mutually reinforcing. C-12 (standalone block) sets
the invariant vocabulary before Stage 0 -- no model drift possible before rules are registered.
C-11 (mechanical enforcement) fires at each checkpoint with the exact label from the TABLE --
redundant enforcement. C-10 (displacement framing) makes the INCUMBENT CHECK TABLEs feel organic
rather than checkbox-like, reducing the temptation to soften Invariant D's template to match
prose tone. C-13 (field isolation) in Stage 5 breaks the V-04 regression: inertia framing creates
narrative gravity toward prose synthesis, but the SYNTHESIS DECLARATIONS section appears before
the prose block and uses format that resists embedding. Combined, these four axes defend C-03,
C-05, C-04, C-10, C-11, C-12, C-13 simultaneously, testing whether a single variation can
approach 95+ without trading off any criterion against another.

---

```
Topic: {topic}
Date:  {date}
Incumbent: {incumbent}

You are running the full prove evidence campaign for {topic}.
The purpose: build the case for displacing {incumbent} with {topic}.
Six stages. Each stage asks: does this evidence advance the displacement claim?
One artifact per stage. Forward order only.

---

## CAMPAIGN OPEN

Register before any stage begins:
  topic:              {topic}
  date:               {date}
  incumbent:          {incumbent}
  incumbent_strength: [what makes {incumbent} hard to displace -- one sentence]
  scout_record:       simulations/scout/record/{topic}-scout-record-{date}.md

---

## SESSION INVARIANTS TABLE
(Registered here. All stages reference by label + failure label. No re-statement of rules.)

| Inv | Description               | Rule                                                                                         | Checkpoint              | Failure Label   |
|-----|---------------------------|----------------------------------------------------------------------------------------------|-------------------------|-----------------|
| A   | Adversarial reviewer      | null_tally_final >= 3: name reviewer type at Stage 5, fire Lock 1                           | Stage 1 (register) + S5 | DUAL-LOCK ERROR |
| B   | Confidence cap            | null_tally_final >= 3: confidence_composite -= 2, hard-cap note (co-locks with A)           | Stage 5 verdict         | DUAL-LOCK ERROR |
| C   | One write per stage       | Artifact written at CLOSE, not deferred, not batched                                         | Every stage CLOSE       | ORDER ERROR     |
| D   | Displacement template     | S2: "Does [evidence item] support the displacement of [incumbent] by [topic]?"               | Stage 2 CHECK TABLE     | FORMAT ERROR    |
|     |                           | S3: "Does [practitioner account] reveal a viable transition path from [incumbent] to [topic]?" | Stage 3 CHECK TABLE  | FORMAT ERROR    |
|     |                           | S4: "Does [prototype result] make a credible case for displacing [incumbent] with [topic]?"  | Stage 4 CHECK TABLE     | FORMAT ERROR    |

---

## ROLE B -- SCOUT LOADER

  scout_artifact: simulations/scout/record/{topic}-scout-record-{date}.md
  scout_loaded:   [ ] true   [ ] false
  gate_s_cleared: true | false

If gate_s_cleared = false: "CAMPAIGN BLOCKED: scout record absent." Stop.

EXIT SIGNAL: gate_open

---

## STAGE 1 -- Hypothesis

OPEN: Load scout artifact. The hypothesis is the displacement claim: what does {topic}
deliver that {incumbent} cannot?

Register for Invariant A: adversarial_reviewer_type = [name now; Invariant A: DUAL-LOCK ERROR
  if not registered here].
Name: scout_anchor = [key scout finding that grounds the displacement claim].

  hypothesis:                [what {topic} enables that {incumbent} cannot -- one sentence]
  counter_hypothesis:        [{incumbent}'s strongest defense -- one sentence]
  scout_anchor:              [key scout finding]
  adversarial_reviewer_type: [registered]

Invariant C: ORDER ERROR if write deferred.
Write: simulations/prove/hypothesis/{topic}-hypothesis-{date}.md
  frontmatter: topic, date, scout_source, hypothesis, counter_hypothesis,
    adversarial_reviewer_type, incumbent

Confirm: "hypothesis artifact written."

EXIT SIGNAL: hypothesis_locked

---

## STAGE 2 -- Web Search

OPEN: Load hypothesis artifact. Frame 3-5 queries: does external evidence support
displacement of {incumbent} by {topic}?

For each result: does this evidence advance or resist the displacement claim?

Invariant D: FORMAT ERROR if template deviates.
INCUMBENT CHECK TABLE:
  | Evidence item | Does [evidence item] support the displacement of [incumbent] by [topic]? | Verdict |
  |---------------|-------------------------------------------------------------------------|---------|
  | [item 1]      | [answer -- frame in displacement terms]                                 | Yes / Null |
  | ...           |                                                                         |         |

  s2_ce_verdict: Yes | Null
  s2_null_count: [N]

  Displacement read: [one sentence -- what the web evidence says about {topic} vs {incumbent}]

Invariant C: ORDER ERROR if write deferred.
Write: simulations/prove/websearch/{topic}-websearch-{date}.md
  frontmatter: topic, date, hypothesis_source, s2_ce_verdict, s2_null_count, incumbent
  body: INCUMBENT CHECK TABLE, displacement read, evidence summaries

Confirm: "websearch artifact written."

EXIT SIGNAL: s2_complete

---

## STAGE 3 -- Interview (Practitioner Accounts)

OPEN: Load hypothesis artifact. Gather 3-5 accounts from practitioners who have worked
with {topic} or {incumbent}. Does their experience reveal a transition path?

Invariant D: FORMAT ERROR if template deviates.
INCUMBENT CHECK TABLE:
  | Practitioner account | Does [practitioner account] reveal a viable transition path from
    [incumbent] to [topic]? | Verdict |
  |----------------------|---------------------------------------------------------------------------------|---------|
  | [account 1]          | [answer -- frame in displacement terms]                                         | Yes / Null |
  | ...                  |                                                                                 |         |

  s3_ce_verdict: Yes | Null
  s3_null_count: [N]
  running_null_tally: [s2 + s3]

  Displacement read: [one sentence -- what practitioner accounts say about transitioning
    from {incumbent} to {topic}]

Invariant C: ORDER ERROR if write deferred.
Write: simulations/prove/interview/{topic}-interview-{date}.md
  frontmatter: topic, date, hypothesis_source, s3_ce_verdict, running_null_tally, incumbent
  body: INCUMBENT CHECK TABLE, displacement read, account summaries

Confirm: "interview artifact written."

EXIT SIGNAL: s3_complete

---

## STAGE 4 -- Prototype (Displacement Testing)

OPEN: Load websearch and interview artifacts. The prototype tests the displacement claim
directly: can {topic} perform the core function for which {incumbent} is currently used?

Invariant D: FORMAT ERROR if template deviates.
INCUMBENT CHECK TABLE:
  | Prototype result | Does [prototype result] make a credible case for displacing [incumbent]
    with [topic]? | Verdict |
  |------------------|---------------------------------------------------------------------------|---------|
  | [result 1]       | [answer -- frame in displacement terms]                                   | Yes / Null |
  | ...              |                                                                           |         |

  s4_ce_verdict: Yes | Null
  s4_null_count: [N]

NULL TALLY CROSS-CHECK (mismatch = INTEGRITY FAILURE):
  Running count from Stage 3 was: [running_null_tally from interview artifact]
  Final count (s2 + s3 + s4): [N]
  Match: [true | false]
  null_tally_final: [N]
  incumbent_defense_closed: [true | false -- has {incumbent}'s stated strength been answered?]

Invariant C: ORDER ERROR if write deferred.
Write: simulations/prove/prototype/{topic}-prototype-{date}.md
  frontmatter: topic, date, websearch_source, interview_source, s4_ce_verdict,
    null_tally_final, incumbent_defense_closed, incumbent
  body: INCUMBENT CHECK TABLE, prototype description and results, null tally cross-check,
    incumbent_defense_closed explanation

Confirm: "prototype artifact written."

EXIT SIGNAL: s4_complete

---

## STAGE 5 -- Synthesis + Handoff

OPEN: Load all four prior artifacts. Frame the synthesis as: "The case against {incumbent}."

ATOMIC DUAL-LOCK CHECK (Invariants A + B: DUAL-LOCK ERROR if threshold met and lock not fired):
  null_tally_final: [from Stage 4 artifact]
  If null_tally_final >= 3:
    Lock 1 fires: adversarial_reviewer_type = [registered at Stage 1]
    Lock 2 fires: confidence_composite -= 2, hard-cap note: "cap applied -- null_tally_final >= 3"
    co_activation_confirmed: dual_lock_fired
  If null_tally_final < 3:
    co_activation_confirmed: not_triggered

NULL TALLY CHAIN RECONSTRUCTION (missing reconstruction = INTEGRITY FAILURE):
  S2 null count: [N]
  S3 null count: [N]
  S4 null count: [N]
  null_tally_final: [sum]
  Match with Stage 4 declaration: [true | false]

COUNTER-HYPOTHESIS RESOLUTION TABLE:
  | Field                 | Value |
  |-----------------------|-------|
  | counter_hypothesis    | [from Stage 1 artifact -- {incumbent}'s stated defense] |
  | verdict               | REFUTED / PARTIALLY REFUTED / OPEN RISK |
  | citation              | [stage and specific finding that resolves it] |
  | confidence_adjustment | [if OPEN RISK: -1 tier applied; else: none] |

SYNTHESIS DECLARATIONS
(C-13: each field on its own labeled line. Do not embed these values in prose.
These declarations appear before evidence_summary. Each is extractable by label match.)

  hypothesis_verdict:   SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED
  confidence_composite: [numeric value, 1-10, adjusted for dual-lock if applicable]
  key_risk:             [residual incumbent strength -- one phrase, not a sentence fragment]

EVIDENCE SUMMARY (begins only after SYNTHESIS DECLARATIONS block is complete):
  evidence_summary: [The case against {incumbent}. What did the evidence show across Stages 2-4?
    Must include: "Stage 4 displacement verdict: [Yes/No/Pending]".]

HANDOFF TABLE (unlabeled field = FAIL):
  | Field                      | Value | Derived from |
  |----------------------------|-------|--------------|
  | scout_anchor               | [key scout claim] | [derived from: scout artifact] |
  | incumbent_threat_locked    | [yes/no] | [derived from: Stage 4 incumbent_defense_closed] |
  | hypothesis                 | [displacement claim] | [derived from: Stage 1 artifact] |
  | counter_hypothesis         | [{incumbent}'s defense] | [derived from: Stage 1 artifact] |
  | s2_ce_verdict              | [Yes/Null] | [derived from: Stage 2 artifact] |
  | s3_ce_verdict              | [Yes/Null] | [derived from: Stage 3 artifact] |
  | s4_ce_verdict              | [Yes/Null] | [derived from: Stage 4 artifact] |
  | null_tally_final           | [N] | [derived from: Stage 4 null tally cross-check] |
  | co_activation_confirmed    | [dual_lock_fired / not_triggered] | [derived from: dual-lock check above] |
  | incumbent_defense_closed   | [true/false] | [derived from: Stage 4 artifact] |
  | confidence_composite       | [N] | [derived from: synthesis declarations] |
  | schema_compliance_confirmed| true | [derived from: this table] |

Invariant C: ORDER ERROR if writes deferred or batched.

Write: simulations/prove/synthesize/{topic}-synthesize-{date}.md
  frontmatter: topic, date, hypothesis_verdict, confidence_composite, incumbent
  body: dual-lock check, chain reconstruction, counter-hyp table, SYNTHESIS DECLARATIONS
    (before prose), evidence_summary

Write: simulations/prove/handoff/{topic}-handoff-{date}.md
  frontmatter: topic, date, synthesis_source
  body: HANDOFF TABLE

Confirm: "synthesis artifact written. handoff artifact written."

EXIT SIGNAL: campaign_closed
```
