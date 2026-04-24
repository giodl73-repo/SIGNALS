---
skill: quest-variate
skill_target: prove-topic
round: R16
date: 2026-03-16
rubric: prove-topic-rubric-v14-2026-03-16.md
variations: [V-01, V-02, V-03, V-04, V-05]
axes_explored:
  single: [session_invariants, atomic_dual_lock, counter_hypothesis_resolution_block]
  combined: [V-04 (session_invariants + atomic_dual_lock), V-05 (all_three + R15_V05_stack)]
r15_anchor: >
  R15 V-05 (the current champion) combines four axes: numbered dependency-chain roles
  (ROLE 1 SCOUT LOADER / ROLE 2 INERTIA ANALYST / ROLE 3 CAMPAIGN DIRECTOR), table
  evidence format with displacement check columns at every evidence stage, explicit entry
  conditions + exit signals at every boundary, and inertia framing with displacement
  template registered verbatim by ROLE 3. This satisfies C-01 through C-04 against
  rubric v14 but two structural gaps remain: (a) campaign header fields (scout_artifact,
  status_quo_comparator) can be re-inferred mid-campaign without detection, and (b) Stage
  5 synthesis can emit synthesis_complete with hypothesis_verdict set but
  displacement_conclusion blank. A third gap: Stage 5 has no explicit block requiring
  counter_hypothesis resolution before the final verdict is stated.
r16_targets: >
  V-01 (single: session_invariants): A SESSION INVARIANTS block printed between CAMPAIGN
  OPEN and the PRE-STAGE roles, declaring four fields as read-only after this point:
  topic, date, scout_artifact, status_quo_comparator. Every stage entry condition
  references these by field name from SESSION INVARIANTS, not re-stating or re-inferring
  them. Tests whether a named immutability contract prevents field drift across stages.

  V-02 (single: atomic_dual_lock): Stage 5 synthesis requires two fields to be explicitly
  marked [LOCKED] before synthesis_complete fires: hypothesis_verdict [LOCKED] and
  displacement_conclusion [LOCKED]. A DUAL-LOCK GATE is printed between Stage 5 body
  and the EXIT SIGNAL. Tests whether a two-field structural exit constraint closes the
  most common synthesis shortcut (verdict without displacement case).

  V-03 (single: counter_hypothesis_resolution_block): Stage 5 is split into two
  sequential blocks. BLOCK 1 resolves the counter_hypothesis from Stage 1 against stage
  evidence, emitting resolution_verdict (REFUTED / PARTIALLY REFUTED / OPEN RISK).
  BLOCK 2 issues the synthesis verdict and requires BLOCK 1 resolution_verdict to be set.
  Tests whether an explicit two-block Stage 5 forces counter-hypothesis resolution as a
  structural gate rather than advisory text.

  V-04 (combined: session_invariants + atomic_dual_lock): SESSION INVARIANTS (V-01) +
  ATOMIC DUAL-LOCK (V-02), layered on the V-01 role-sequence skeleton with lifecycle
  gates. Tests whether tamper-resistant setup + enforced synthesis exit together satisfy
  C-02 and C-04 without the full structural density of V-05.

  V-05 (all three + complete R15 V-05 structural stack): R15 V-05 full stack (three
  named roles in dependency order, table evidence with displacement check columns, entry
  conditions + exit signals at every boundary, displacement template registered verbatim
  by ROLE 3) + V-01 SESSION INVARIANTS + V-02 ATOMIC DUAL-LOCK + V-03 counter-hypothesis
  resolution block. Tests whether maximum structural density with all three new
  mechanisms plus the R15 V-05 base satisfies the complete v14 criterion stack.
---

# prove-topic Variations — Round 16 (rubric v14)

**Skill**: prove-topic
**Rubric**: v14 (C-01–C-05 essential, C-06–C-08 recommended, C-09–C-10 aspirational)
**Date**: 2026-03-16
**Round**: 16

---

## Context: what informed this round

R15 V-05 established four structural axes and corrected the stage sequence to the v14
target (hypothesis -> websearch -> intelligence -> analysis -> synthesize). R16 identifies
three structural gaps in R15 V-05 and targets them with new single-axis mechanisms:

| Gap | Failure mode | R16 mechanism |
|-----|-------------|--------------|
| Field drift | scout_artifact / status_quo_comparator can be re-inferred mid-campaign | SESSION INVARIANTS (V-01) |
| Synthesis shortcut | synthesis_complete can fire with displacement_conclusion blank | ATOMIC DUAL-LOCK (V-02) |
| Counter-hypothesis skip | Stage 5 has no structural block for counter-hypothesis resolution before verdict | TWO-BLOCK STAGE 5 (V-03) |

| Var | Axis | Primary criteria targeted |
|-----|------|--------------------------|
| V-01 | Session invariants | C-02 (scout integrity), C-03 (field integrity) |
| V-02 | Atomic dual-lock | C-04 (synthesis exit completeness) |
| V-03 | Counter-hypothesis resolution block | C-05 (counter-hypothesis resolution) |
| V-04 | Session invariants + atomic dual-lock | C-02, C-04 |
| V-05 | All three + R15 V-05 full stack | C-01 through C-05 + recommended/aspirational |

**Artifact paths (all variations)**:

| Stage | Sub-skill | Artifact path |
|-------|-----------|---------------|
| 1 | prove-hypothesis | `simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md` |
| 2 | prove-websearch | `simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md` |
| 3 | prove-intelligence | `simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md` |
| 4 | prove-analysis | `simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md` |
| 5 | prove-synthesize | `simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md` |

---

## V-01 — Session Invariants

**Axis**: session_invariants
**Hypothesis**: Declaring four campaign fields as read-only in a named SESSION INVARIANTS
block — printed once after CAMPAIGN OPEN, referenced by field name at every stage entry
condition — prevents scout_artifact and status_quo_comparator from being re-inferred or
silently overridden mid-campaign, enforcing C-02 as a structural immutability contract
rather than advisory instruction.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for a topic. SESSION INVARIANTS declared once after
CAMPAIGN OPEN and read-only for the full campaign duration. Five stages in strict forward
sequence: prove-hypothesis -> prove-websearch -> prove-intelligence -> prove-analysis ->
prove-synthesize. Scout artifact named before hypothesis. One artifact written per stage,
write confirmed before stage exit. Final output: evidence brief ready for /topic-story.

---

## CAMPAIGN OPEN

  topic:  {topic}
  date:   {date}

---

## SESSION INVARIANTS

These four fields are declared once and read-only for the duration of this campaign.
Stages do not re-infer or re-state these values. They reference them by field name from
this block only.

  SI-01  topic:                  {topic}
  SI-02  date:                   {date}
  SI-03  scout_artifact:         [{topic}-scout-record-{date}.md — or most recent scout
                                   signal for {topic}. Locate now. If not found, record
                                   which path was searched and halt campaign.]
  SI-04  status_quo_comparator:  [incumbent approach SI-01 must displace. Name before
                                   any stage begins.]

SESSION INVARIANTS LOCKED. Do not modify these fields after this point.
If SI-03 is not found: CAMPAIGN BLOCKED. Record search path. Halt.

---

## CAMPAIGN PRE-CHECK

  [ ] SI-03 scout_artifact found and accessible
  [ ] SI-04 status_quo_comparator named (not blank)
  [ ] SI-01 and SI-02 match the invocation parameters

PRE-CHECK EXIT: invariants_locked
  "SESSION INVARIANTS locked. Advancing to Stage 1."
Do not begin Stage 1 until PRE-CHECK EXIT is printed.

---

## STAGE 1 — HYPOTHESIS

STAGE 1 ENTRY CONDITIONS:
  [ ] PRE-CHECK EXIT received: invariants_locked
  [ ] SI-03 (scout_artifact) from SESSION INVARIANTS — do not re-infer

STAGE 1 BODY:
Load SI-03 (scout_artifact). Read its signals. Frame hypothesis from those signals.

  source_artifact:    [SI-03 value — verbatim copy, not re-inferred]
  hypothesis:         [falsifiable claim derived from scout signals]
  counter_hypothesis: [incumbent's best defense — grounded in SI-04 (status_quo_comparator)]
  confidence_prior:   [Low / Medium / High]

STAGE 1 WRITE:
  Write: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
  Confirm write: [{topic}-prove-hypothesis-{date}.md written]

STAGE 1 EXIT SIGNAL: hypothesis_locked
  "STAGE 1 EXIT: hypothesis_locked — {topic}-prove-hypothesis-{date}.md written.
   Stage 2 entry conditions satisfied."

---

## STAGE 2 — WEB SEARCH

STAGE 2 ENTRY CONDITIONS:
  [ ] STAGE 1 EXIT received: hypothesis_locked
  [ ] SI-04 (status_quo_comparator) available from SESSION INVARIANTS

STAGE 2 BODY:
Gather minimum 3 external sources. Apply displacement check using SI-04 per row.

  ITEM | SOURCE (URL or citation) | SUMMARY (1 sentence) | SUPPORT (Y/N/Partial) | STRENGTH
  1    | [source]                 | [summary]            | [verdict]             | [S/M/W]
  2    | [source]                 | [summary]            | [verdict]             | [S/M/W]
  3    | [source]                 | [summary]            | [verdict]             | [S/M/W]
  add  |                          |                      |                       |

  s2_support_tally:     [N support / M counter / P partial]
  s2_key_gap:           [what external evidence does not cover]
  s2_displacement_read: [does web evidence support displacing SI-04? support/counter/mixed]

STAGE 2 WRITE:
  Write: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
  Confirm write: [{topic}-prove-websearch-{date}.md written]

STAGE 2 EXIT SIGNAL: websearch_complete
  "STAGE 2 EXIT: websearch_complete — s2_support_tally = [value].
   Stage 3 entry conditions satisfied."

---

## STAGE 3 — INTELLIGENCE

STAGE 3 ENTRY CONDITIONS:
  [ ] STAGE 2 EXIT received: websearch_complete
  [ ] s2_support_tally recorded (not blank)
  [ ] SI-04 (status_quo_comparator) available from SESSION INVARIANTS

STAGE 3 BODY:
Search internal sources: codebase, specs, docs, prior signal artifacts.

  FILE PATH          | SECTION         | FINDING (1 sentence) | RELEVANCE (H/M/L)
  [path]             | [section]       | [finding]            | [level]
  add rows as needed

  s3_sources_found:     [N internal sources with relevant evidence]
  s3_alignment:         [ALIGNED / CONTRADICTS / MIXED — vs Stage 2]
  s3_key_gap:           [what internal sources do not address]
  s3_displacement_read: [does internal evidence support displacing SI-04? support/counter/mixed]

STAGE 3 WRITE:
  Write: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
  Confirm write: [{topic}-prove-intelligence-{date}.md written]

STAGE 3 EXIT SIGNAL: intelligence_complete
  "STAGE 3 EXIT: intelligence_complete — s3_sources_found = [N].
   Stage 4 entry conditions satisfied."

---

## STAGE 4 — ANALYSIS

STAGE 4 ENTRY CONDITIONS:
  [ ] STAGE 3 EXIT received: intelligence_complete
  [ ] s3_sources_found recorded (not blank)
  [ ] SI-04 (status_quo_comparator) available from SESSION INVARIANTS

STAGE 4 BODY:
Analyze patterns across Stages 2 + 3. Distinguish correlation from causation.

  PATTERN            | SOURCES (S2 item# / S3 filepath) | CAUSAL?        | CONFIDENCE
  [pattern]          | [sources]                        | Yes/No/Unknown | Low/Med/High
  add rows as needed

  s4_primary_finding:   [dominant pattern, 1-2 sentences]
  s4_counter_evidence:  [strongest evidence against hypothesis — cite artifact + section]
  s4_causal_claim:      [what is asserted causal vs correlational]

STAGE 4 WRITE:
  Write: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
  Confirm write: [{topic}-prove-analysis-{date}.md written]

STAGE 4 EXIT SIGNAL: analysis_complete
  "STAGE 4 EXIT: analysis_complete — s4_primary_finding locked.
   Stage 5 entry conditions satisfied."

---

## STAGE 5 — SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] STAGE 4 EXIT received: analysis_complete
  [ ] counter_hypothesis from Stage 1 available
  [ ] SI-04 (status_quo_comparator) from SESSION INVARIANTS
  [ ] s4_primary_finding recorded

STAGE 5 BODY:

  hypothesis_verdict:   [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  displacement_case:    [1-2 sentences: does evidence support replacing SI-04 with SI-01?
                          Explicit answer required.]
  evidence_summary:     [2-3 sentences integrating Stages 2, 3, 4]
  confidence_final:     [Low / Medium / High — one sentence of reasoning]
  key_risk:             [primary risk remaining after evidence review]

STAGE 5 WRITE:
  Write: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
  Confirm write: [{topic}-prove-synthesize-{date}.md written]

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete — Evidence brief complete. Ready for /topic-story."

CAMPAIGN COMPLETE.
```

---

## V-02 — Atomic Dual-Lock

**Axis**: atomic_dual_lock
**Hypothesis**: Requiring both hypothesis_verdict and displacement_conclusion to carry a
[LOCKED] suffix before synthesis_complete fires — enforced by a DUAL-LOCK GATE between
the Stage 5 body and the EXIT SIGNAL — prevents the most common synthesis shortcut where
a verdict is stated but the displacement case is omitted, enforcing C-04 as a two-field
structural exit rather than advisory text.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for a topic. Five stages in strict forward sequence:
prove-hypothesis -> prove-websearch -> prove-intelligence -> prove-analysis ->
prove-synthesize. Scout artifact named before hypothesis. One artifact written per stage,
write confirmed before stage exit. Stage 5 uses ATOMIC DUAL-LOCK: hypothesis_verdict
[LOCKED] and displacement_conclusion [LOCKED] must both be set before synthesis_complete
fires. Final output: evidence brief ready for /topic-story.

---

## CAMPAIGN OPEN

  topic:                  {topic}
  date:                   {date}
  scout_artifact:         [{topic}-scout-record-{date}.md — or most recent scout signal
                            for {topic}. Locate now. If not found, halt and record path.]
  status_quo_comparator:  [incumbent approach {topic} must displace. Name before Stage 1.]

If scout_artifact is not found: CAMPAIGN BLOCKED. Do not advance.

---

## STAGE 1 — HYPOTHESIS

ENTRY CONDITIONS:
  [ ] scout_artifact located in CAMPAIGN OPEN
  [ ] status_quo_comparator named

Load scout_artifact. Use its signals to frame the hypothesis.

  source_artifact:    [path — copied from CAMPAIGN OPEN, not re-inferred]
  hypothesis:         [falsifiable claim derived from scout signals]
  counter_hypothesis: [incumbent's best defense — grounded in status_quo_comparator]
  confidence_prior:   [Low / Medium / High]

Write: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
Confirm write.

EXIT: hypothesis_locked — "{topic}-prove-hypothesis-{date}.md written. Stage 2 ready."

---

## STAGE 2 — WEB SEARCH

ENTRY CONDITIONS:
  [ ] hypothesis_locked received
  [ ] hypothesis artifact confirmed written

Gather minimum 3 external sources.

  ITEM | SOURCE (URL or citation) | SUMMARY (1 sentence) | SUPPORT (Y/N/Partial) | STRENGTH
  1    | [source]                 | [summary]            | [verdict]             | [S/M/W]
  2    | [source]                 | [summary]            | [verdict]             | [S/M/W]
  3    | [source]                 | [summary]            | [verdict]             | [S/M/W]
  add  |                          |                      |                       |

  s2_support_tally:  [N support / M counter / P partial]
  s2_key_gap:        [what external evidence does not cover]

Write: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
Confirm write.

EXIT: websearch_complete — "s2_support_tally = [value]. Stage 3 ready."

---

## STAGE 3 — INTELLIGENCE

ENTRY CONDITIONS:
  [ ] websearch_complete received
  [ ] s2_support_tally recorded (not blank)

Search internal sources: codebase, specs, docs, prior signal artifacts.

  FILE PATH          | SECTION         | FINDING (1 sentence) | RELEVANCE (H/M/L)
  [path]             | [section]       | [finding]            | [level]
  add rows as needed

  s3_sources_found:  [N internal sources]
  s3_alignment:      [ALIGNED / CONTRADICTS / MIXED — vs Stage 2]
  s3_key_gap:        [what internal sources do not address]

Write: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
Confirm write.

EXIT: intelligence_complete — "s3_sources_found = [N]. Stage 4 ready."

---

## STAGE 4 — ANALYSIS

ENTRY CONDITIONS:
  [ ] intelligence_complete received
  [ ] s3_sources_found recorded (not blank)

Analyze patterns across Stages 2 + 3. Distinguish causation from correlation.

  PATTERN            | SOURCES (S2 item# / S3 filepath) | CAUSAL?        | CONFIDENCE
  [pattern]          | [sources]                        | Yes/No/Unknown | Low/Med/High
  add rows as needed

  s4_primary_finding:   [dominant pattern, 1-2 sentences]
  s4_counter_evidence:  [strongest evidence against hypothesis — cite artifact + section]
  s4_causal_claim:      [what is asserted causal vs correlational]

Write: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
Confirm write.

EXIT: analysis_complete — "s4_primary_finding locked. Stage 5 ready."

---

## STAGE 5 — SYNTHESIS (ATOMIC DUAL-LOCK)

ENTRY CONDITIONS:
  [ ] analysis_complete received
  [ ] counter_hypothesis from Stage 1 available
  [ ] s4_primary_finding recorded

SYNTHESIS BODY:
Set both fields below. Both must carry the [LOCKED] suffix before the DUAL-LOCK GATE
clears. Do not proceed to DUAL-LOCK GATE until both are marked.

  hypothesis_verdict [LOCKED]:      [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED — LOCKED]
  displacement_conclusion [LOCKED]: [1-2 sentences: does evidence support replacing
                                      {status_quo_comparator} with {topic}? Explicit
                                      Yes / No / Conditional required. — LOCKED]

  evidence_summary:  [2-3 sentences integrating Stages 2, 3, 4]
  confidence_final:  [Low / Medium / High — one sentence of reasoning]
  key_risk:          [primary risk remaining after evidence review]

DUAL-LOCK GATE:
  [ ] hypothesis_verdict present AND marked [LOCKED]
  [ ] displacement_conclusion present AND marked [LOCKED]

  If either field is absent or not marked [LOCKED]: set it before proceeding.
  DUAL-LOCK CLEARED — both fields locked. Proceeding to write and exit.

Write: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
Confirm write.

EXIT: synthesis_complete — "DUAL-LOCK cleared. Evidence brief complete. Ready for /topic-story."

CAMPAIGN COMPLETE.
```

---

## V-03 — Counter-Hypothesis Resolution Block

**Axis**: counter_hypothesis_resolution_block
**Hypothesis**: Splitting Stage 5 into two sequential blocks — BLOCK 1 resolves the
counter_hypothesis from Stage 1 against collected evidence, emitting a typed
resolution_verdict (REFUTED / PARTIALLY REFUTED / OPEN RISK); BLOCK 2 issues the
synthesis verdict and requires BLOCK 1 resolution_verdict to be set — forces
counter-hypothesis resolution as a structural gate before the final verdict, satisfying
C-05 as a blocking dependency rather than an implied convention.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for a topic. Five stages in strict forward sequence:
prove-hypothesis -> prove-websearch -> prove-intelligence -> prove-analysis ->
prove-synthesize. Scout artifact named before hypothesis. One artifact written per stage.
Stage 5 is split into two blocks: BLOCK 1 resolves the counter-hypothesis from Stage 1;
BLOCK 2 issues the synthesis verdict. BLOCK 2 cannot begin until BLOCK 1 resolution_verdict
is set. Final output: evidence brief ready for /topic-story.

---

## CAMPAIGN OPEN

  topic:                  {topic}
  date:                   {date}
  scout_artifact:         [{topic}-scout-record-{date}.md — or most recent scout signal
                            for {topic}. Locate now. If not found, halt and record path.]
  status_quo_comparator:  [incumbent approach {topic} must displace. Name before Stage 1.]

If scout_artifact is not found: CAMPAIGN BLOCKED. Do not advance.

---

## STAGE 1 — HYPOTHESIS

ENTRY CONDITIONS:
  [ ] scout_artifact located
  [ ] status_quo_comparator named

Load scout_artifact. Frame hypothesis from its signals.
Note: the counter_hypothesis written here will be resolved explicitly in Stage 5 BLOCK 1.
Write it precisely: "The claim fails if [specific condition]."

  source_artifact:    [path — copied from CAMPAIGN OPEN, not re-inferred]
  hypothesis:         [falsifiable claim derived from scout signals]
  counter_hypothesis: [incumbent's best defense. Precise form: "The claim fails if ...".]
  confidence_prior:   [Low / Medium / High]

Write: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
Confirm write.

EXIT: hypothesis_locked — "{topic}-prove-hypothesis-{date}.md written. Stage 2 ready."

---

## STAGE 2 — WEB SEARCH

ENTRY CONDITIONS:
  [ ] hypothesis_locked received
  [ ] hypothesis artifact confirmed written

Gather minimum 3 external sources.

  ITEM | SOURCE (URL or citation) | SUMMARY (1 sentence) | SUPPORT (Y/N/Partial) | STRENGTH
  1    | [source]                 | [summary]            | [verdict]             | [S/M/W]
  2    | [source]                 | [summary]            | [verdict]             | [S/M/W]
  3    | [source]                 | [summary]            | [verdict]             | [S/M/W]
  add  |                          |                      |                       |

  s2_support_tally:  [N support / M counter / P partial]
  s2_key_gap:        [what external evidence does not cover]

Write: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
Confirm write.

EXIT: websearch_complete — "s2_support_tally = [value]. Stage 3 ready."

---

## STAGE 3 — INTELLIGENCE

ENTRY CONDITIONS:
  [ ] websearch_complete received
  [ ] s2_support_tally recorded (not blank)

Search internal sources: codebase, specs, docs, prior signal artifacts.

  FILE PATH          | SECTION         | FINDING (1 sentence) | RELEVANCE (H/M/L)
  [path]             | [section]       | [finding]            | [level]
  add rows as needed

  s3_sources_found:  [N internal sources]
  s3_alignment:      [ALIGNED / CONTRADICTS / MIXED — vs Stage 2]
  s3_key_gap:        [what internal sources do not address]

Write: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
Confirm write.

EXIT: intelligence_complete — "s3_sources_found = [N]. Stage 4 ready."

---

## STAGE 4 — ANALYSIS

ENTRY CONDITIONS:
  [ ] intelligence_complete received
  [ ] s3_sources_found recorded (not blank)

Analyze patterns across Stages 2 + 3. Distinguish causation from correlation.

  PATTERN            | SOURCES (S2 item# / S3 filepath) | CAUSAL?        | CONFIDENCE
  [pattern]          | [sources]                        | Yes/No/Unknown | Low/Med/High
  add rows as needed

  s4_primary_finding:   [dominant pattern, 1-2 sentences]
  s4_counter_evidence:  [strongest evidence against hypothesis — cite artifact + section]
  s4_causal_claim:      [what is asserted causal vs correlational]

Write: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
Confirm write.

EXIT: analysis_complete — "s4_primary_finding locked. Stage 5 ready."

---

## STAGE 5 — SYNTHESIS

STAGE 5 ENTRY CONDITIONS:
  [ ] analysis_complete received
  [ ] counter_hypothesis from Stage 1 available (exact wording)
  [ ] s4_primary_finding recorded

---

### STAGE 5 BLOCK 1 — COUNTER-HYPOTHESIS RESOLUTION

Retrieve counter_hypothesis from Stage 1. Evaluate it against the full evidence record
(Stages 2, 3, 4). Issue a typed resolution_verdict. BLOCK 2 cannot begin until
resolution_verdict is set.

  counter_hypothesis:   [from Stage 1 — verbatim copy, not paraphrased]
  evidence_against_ch:  [cite Stage artifact + section that most directly addresses it]
  resolution_verdict:   [REFUTED / PARTIALLY REFUTED / OPEN RISK]
  resolution_note:      [one sentence: why this verdict was reached]

BLOCK 1 GATE: resolution_verdict must be set before BLOCK 2 begins.
If resolution_verdict is blank: set it before proceeding.

BLOCK 1 EXIT: counter_hypothesis_resolved
  "BLOCK 1 EXIT: counter_hypothesis_resolved — resolution_verdict = [value].
   Proceeding to BLOCK 2."

---

### STAGE 5 BLOCK 2 — SYNTHESIS VERDICT

BLOCK 2 ENTRY CONDITIONS:
  [ ] BLOCK 1 EXIT received: counter_hypothesis_resolved
  [ ] resolution_verdict set (not blank)

Issue the final verdict. If resolution_verdict = OPEN RISK, name the unresolved risk
explicitly in key_risk.

  hypothesis_verdict:   [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED]
  displacement_case:    [1-2 sentences: does evidence support replacing
                          {status_quo_comparator} with {topic}?]
  evidence_summary:     [2-3 sentences integrating Stages 2, 3, 4]
  confidence_final:     [Low / Medium / High — one sentence of reasoning]
  key_risk:             [primary risk; if OPEN RISK from BLOCK 1, name that risk here]

Write: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
Confirm write.

STAGE 5 EXIT SIGNAL: synthesis_complete
  "STAGE 5 EXIT: synthesis_complete — Evidence brief complete. Ready for /topic-story."

CAMPAIGN COMPLETE.
```

---

## V-04 — Session Invariants + Atomic Dual-Lock

**Axes**: session_invariants + atomic_dual_lock
**Hypothesis**: Combining SESSION INVARIANTS (V-01 — four fields declared read-only after
CAMPAIGN OPEN) with ATOMIC DUAL-LOCK (V-02 — both hypothesis_verdict [LOCKED] and
displacement_conclusion [LOCKED] required before synthesis_complete) closes both the
field-drift gap and the synthesis-shortcut gap, satisfying C-02 and C-04 without
requiring the full structural density of V-05.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for a topic. SESSION INVARIANTS declared once,
read-only for campaign duration. Five stages in strict forward sequence:
prove-hypothesis -> prove-websearch -> prove-intelligence -> prove-analysis ->
prove-synthesize. One artifact written per stage, write confirmed before exit.
Stage 5 ATOMIC DUAL-LOCK requires hypothesis_verdict [LOCKED] and
displacement_conclusion [LOCKED] before synthesis_complete fires.
Final output: evidence brief ready for /topic-story.

---

## CAMPAIGN OPEN

  topic:  {topic}
  date:   {date}

---

## SESSION INVARIANTS

Declared once. Read-only after this point. Stages reference these by field name only.

  SI-01  topic:                  {topic}
  SI-02  date:                   {date}
  SI-03  scout_artifact:         [{topic}-scout-record-{date}.md — or most recent scout
                                   signal for {topic}. Locate now. If not found, record
                                   search path. CAMPAIGN BLOCKED if not found.]
  SI-04  status_quo_comparator:  [incumbent approach SI-01 must displace. Name now.]

SESSION INVARIANTS LOCKED. If SI-03 not found: CAMPAIGN BLOCKED. Do not advance.

---

## PRE-CHECK

  [ ] SI-03 scout_artifact found and accessible
  [ ] SI-04 status_quo_comparator named (not blank)

PRE-CHECK EXIT: invariants_locked — "SI-01 through SI-04 locked. Advancing to Stage 1."

---

## STAGE 1 — HYPOTHESIS

ENTRY CONDITIONS:
  [ ] invariants_locked received
  [ ] SI-03 (scout_artifact) from SESSION INVARIANTS — do not re-infer

Load SI-03. Frame hypothesis from its signals.

  source_artifact:    [SI-03 value — verbatim copy]
  hypothesis:         [falsifiable claim from scout signals]
  counter_hypothesis: [incumbent's best defense — grounded in SI-04]
  confidence_prior:   [Low / Medium / High]

Write: simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md
Confirm write.

EXIT: hypothesis_locked — "{topic}-prove-hypothesis-{date}.md written. Stage 2 ready."

---

## STAGE 2 — WEB SEARCH

ENTRY CONDITIONS:
  [ ] hypothesis_locked received
  [ ] SI-04 (status_quo_comparator) from SESSION INVARIANTS

Gather minimum 3 external sources.

  ITEM | SOURCE | SUMMARY (1 sentence) | SUPPORT (Y/N/Partial) | STRENGTH
  1    |        |                      |                       | [S/M/W]
  2    |        |                      |                       | [S/M/W]
  3    |        |                      |                       | [S/M/W]
  add  |        |                      |                       |

  s2_support_tally:     [N support / M counter / P partial]
  s2_key_gap:           [what external evidence does not cover]
  s2_displacement_read: [does web evidence support displacing SI-04? support/counter/mixed]

Write: simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md
Confirm write.

EXIT: websearch_complete — "s2_support_tally = [value]. Stage 3 ready."

---

## STAGE 3 — INTELLIGENCE

ENTRY CONDITIONS:
  [ ] websearch_complete received
  [ ] s2_support_tally recorded (not blank)
  [ ] SI-04 (status_quo_comparator) from SESSION INVARIANTS

Search internal sources.

  FILE PATH | SECTION | FINDING (1 sentence) | RELEVANCE (H/M/L)
  [path]    | [sect]  | [finding]            | [level]
  add rows as needed

  s3_sources_found:     [N sources with relevant evidence]
  s3_alignment:         [ALIGNED / CONTRADICTS / MIXED — vs Stage 2]
  s3_key_gap:           [what internal sources do not address]
  s3_displacement_read: [does internal evidence support displacing SI-04? support/counter/mixed]

Write: simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md
Confirm write.

EXIT: intelligence_complete — "s3_sources_found = [N]. Stage 4 ready."

---

## STAGE 4 — ANALYSIS

ENTRY CONDITIONS:
  [ ] intelligence_complete received
  [ ] s3_sources_found recorded (not blank)

Analyze patterns across Stages 2 + 3. Distinguish causation from correlation.

  PATTERN   | SOURCES (S2 item# / S3 filepath) | CAUSAL?        | CONFIDENCE
  [pattern] | [sources]                        | Yes/No/Unknown | Low/Med/High
  add rows as needed

  s4_primary_finding:   [dominant pattern, 1-2 sentences]
  s4_counter_evidence:  [strongest evidence against hypothesis — cite artifact + section]
  s4_causal_claim:      [what is asserted causal vs correlational]

Write: simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md
Confirm write.

EXIT: analysis_complete — "s4_primary_finding locked. Stage 5 ready."

---

## STAGE 5 — SYNTHESIS (ATOMIC DUAL-LOCK)

ENTRY CONDITIONS:
  [ ] analysis_complete received
  [ ] counter_hypothesis from Stage 1 available
  [ ] SI-04 (status_quo_comparator) from SESSION INVARIANTS
  [ ] s4_primary_finding recorded

SYNTHESIS BODY:
Set both [LOCKED] fields. Do not proceed to DUAL-LOCK GATE until both are marked.

  hypothesis_verdict [LOCKED]:      [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED — LOCKED]
  displacement_conclusion [LOCKED]: [1-2 sentences: does evidence support replacing SI-04
                                      (status_quo_comparator) with SI-01 (topic)? Explicit
                                      Yes / No / Conditional. — LOCKED]

  evidence_summary:  [2-3 sentences integrating Stages 2, 3, 4]
  confidence_final:  [Low / Medium / High — one sentence of reasoning]
  key_risk:          [primary risk remaining after evidence review]

DUAL-LOCK GATE:
  [ ] hypothesis_verdict present AND marked [LOCKED]
  [ ] displacement_conclusion present AND marked [LOCKED]

  If either absent or not marked [LOCKED]: set it before proceeding.
  DUAL-LOCK CLEARED.

Write: simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md
Confirm write.

EXIT: synthesis_complete — "DUAL-LOCK cleared. Evidence brief complete. Ready for /topic-story."

CAMPAIGN COMPLETE.
```

---

## V-05 — All Three + Complete R15 V-05 Structural Stack

**Axes**: session_invariants + atomic_dual_lock + counter_hypothesis_resolution_block +
R15 V-05 full stack (role sequence, table format, lifecycle gates, inertia framing)
**Hypothesis**: Layering all three new R16 mechanisms — SESSION INVARIANTS (field
immutability), ATOMIC DUAL-LOCK (synthesis exit constraint), two-block Stage 5 with
counter-hypothesis resolution as BLOCK 1 — on the complete R15 V-05 base (numbered
dependency-chain roles, table evidence with displacement check columns, entry
conditions + exit signals, displacement template registered verbatim by ROLE 3) produces
a prompt satisfying the full v14 criterion stack plus adjacent recommended/aspirational
territory in a single coherent structure.

---

```
---
name: prove-topic
description: Full prove evidence campaign orchestrating hypothesis through synthesis in one command.
allowed-tools: [Read, Write, Glob, WebSearch]
param_set: full
---

# prove-topic

Run the full prove evidence campaign for a topic. SESSION INVARIANTS declared read-only
at campaign open. Three named roles execute in numbered dependency order before Stage 1.
Five stages in strict sequence: prove-hypothesis -> prove-websearch ->
prove-intelligence -> prove-analysis -> prove-synthesize. Each stage has entry conditions,
table-format evidence with displacement check columns (SI-05 template), and a named exit
signal. Stage 5 is two blocks: BLOCK 1 resolves counter-hypothesis; BLOCK 2 issues
verdict via ATOMIC DUAL-LOCK. One artifact written per stage.
Final output: evidence brief ready for /topic-story.

---

## CAMPAIGN OPEN

  topic:  {topic}
  date:   {date}

---

## SESSION INVARIANTS

Declared once. Read-only for the full campaign duration. Roles and stages reference these
by field name only — no re-inference.

  SI-01  topic:                  {topic}
  SI-02  date:                   {date}
  SI-03  scout_artifact:         [set by ROLE 1 — locked after ROLE 1 CONFIRMED]
  SI-04  status_quo_comparator:  [set by ROLE 2 — locked after ROLE 2 CONFIRMED]
  SI-05  displacement_template:  [set by ROLE 3 — locked after ROLE 3 CONFIRMED]

SESSION INVARIANTS partially open. Fields SI-03 through SI-05 set by named roles below.

---

## PRE-STAGE: NAMED ROLE EXECUTION (Steps 1–3)

Three roles execute in numbered order. A later role cannot begin until the prior role
confirms its field. All three must confirm before Stage 1.

---

**ROLE 1 — SCOUT LOADER** (Step 1 of 3 — executes first)

Rationale: SI-03 (scout_artifact) must be locked before ROLE 2 can analyze the incumbent
and before the hypothesis can be grounded in real signals.

| Field | Value |
|-------|-------|
| SI-03 scout_artifact | [{topic}-scout-record-{date}.md — or most recent scout signal for {topic}] |
| scout_loaded | [true / false] |
| ROLE 1 STATUS | [CONFIRMED — SI-03 set and locked] or [BLOCKED — record search path; halt] |

If scout_loaded = false: CAMPAIGN BLOCKED. Do not advance to ROLE 2.
If ROLE 1 CONFIRMED: SI-03 is LOCKED.

---

**ROLE 2 — INERTIA ANALYST** (Step 2 of 3 — requires ROLE 1 CONFIRMED)

Rationale: SI-04 (status_quo_comparator) must be named before the displacement template
can be formulated and before displacement checks can be applied to evidence rows.

| Field | Value |
|-------|-------|
| SI-04 status_quo_comparator | [incumbent approach SI-01 must displace] |
| comparator_strength | [one sentence: why the incumbent wins today] |
| comparator_vulnerability | [one sentence: where the incumbent is most exposed to SI-01] |
| ROLE 2 STATUS | [CONFIRMED — SI-04 set and locked] |

If ROLE 2 CONFIRMED: SI-04 is LOCKED.

---

**ROLE 3 — CAMPAIGN DIRECTOR** (Step 3 of 3 — requires ROLES 1 + 2 CONFIRMED)

Rationale: Confirms roles 1 and 2. Registers SI-05 displacement_template verbatim —
the question applied to every evidence row in Stages 2, 3, and 4.

SI-05 displacement_template (verbatim):
  "Does [evidence item] support the displacement of SI-04 ({status_quo_comparator})
   by SI-01 ({topic})? [Yes / No / Inconclusive]"

| Field | Value |
|-------|-------|
| role_1_confirmed | true |
| role_2_confirmed | true |
| SI-05 displacement_template | [registered verbatim above] |
| ROLE 3 STATUS | CONFIRMED — SI-05 locked |

SESSION INVARIANTS FULLY LOCKED: SI-01 through SI-05 set. Do not modify.

**PRE-STAGE EXIT: campaign_open**
  "Roles 1, 2, 3 confirmed. SESSION INVARIANTS SI-01 through SI-05 locked.
   Displacement template registered. Advancing to Stage 1."

Do not begin Stage 1 until PRE-STAGE EXIT is printed.

---

## STAGE 1 — HYPOTHESIS

**STAGE 1 ENTRY CONDITIONS:**
- [ ] PRE-STAGE EXIT received: campaign_open
- [ ] SI-03 (scout_artifact) locked — read from SESSION INVARIANTS, do not re-infer

**STAGE 1 BODY:**

Load SI-03. Read its signals.

| Field | Value |
|-------|-------|
| source_artifact | [SI-03 value — verbatim copy, not re-inferred] |
| hypothesis | [falsifiable claim derived from scout signals] |
| counter_hypothesis | [incumbent's best defense, grounded in SI-04 comparator_strength. Precise form: "The claim fails if ..."] |
| confidence_prior | [Low / Medium / High] |

**WRITE:** `simulations/prove/prove-hypothesis/{topic}-prove-hypothesis-{date}.md`
Confirm write.

**STAGE 1 EXIT: hypothesis_locked — "{topic}-prove-hypothesis-{date}.md written. Stage 2 ready."**

---

## STAGE 2 — WEB SEARCH

**STAGE 2 ENTRY CONDITIONS:**
- [ ] STAGE 1 EXIT received: hypothesis_locked
- [ ] SI-05 (displacement_template) locked — apply verbatim to each evidence row

**STAGE 2 BODY:**

Gather minimum 3 external sources. Apply SI-05 displacement_template to each row.

| # | Source (URL or citation) | Key Finding (1 sentence) | Strength | Displacement Check (SI-05 applied) |
|---|--------------------------|--------------------------|----------|-------------------------------------|
| 1 | | | Strong/Moderate/Weak | Does [item 1] support displacement of SI-04 by SI-01? [Yes/No/Inconclusive] |
| 2 | | | Strong/Moderate/Weak | Does [item 2] support displacement of SI-04 by SI-01? [Yes/No/Inconclusive] |
| 3 | | | Strong/Moderate/Weak | Does [item 3] support displacement of SI-04 by SI-01? [Yes/No/Inconclusive] |
| + | add as needed | | | |

| Summary Field | Value |
|---------------|-------|
| s2_tally | [N Yes / M No / P Inconclusive] |
| s2_strength_tally | [Strong: N, Moderate: M, Weak: P] |
| s2_key_gap | [what external evidence does not address] |

**WRITE:** `simulations/prove/prove-websearch/{topic}-prove-websearch-{date}.md`
Confirm write.

**STAGE 2 EXIT: websearch_complete — "s2_tally = [value]. Stage 3 ready."**

---

## STAGE 3 — INTELLIGENCE

**STAGE 3 ENTRY CONDITIONS:**
- [ ] STAGE 2 EXIT received: websearch_complete
- [ ] s2_tally recorded (not blank)
- [ ] SI-05 (displacement_template) locked — apply verbatim to each finding

**STAGE 3 BODY:**

Search internal sources: codebase, specs, docs, prior signal artifacts.
Apply SI-05 displacement_template to each finding.

| # | File Path | Section | Finding (1 sentence) | Strength | Displacement Check (SI-05 applied) |
|---|-----------|---------|----------------------|----------|------------------------------------|
| 1 | | | | Strong/Moderate/Weak | Does [finding 1] support displacement of SI-04 by SI-01? [Yes/No/Inconclusive] |
| 2 | | | | Strong/Moderate/Weak | Does [finding 2] support displacement of SI-04 by SI-01? [Yes/No/Inconclusive] |
| 3 | | | | Strong/Moderate/Weak | Does [finding 3] support displacement of SI-04 by SI-01? [Yes/No/Inconclusive] |
| + | add as needed | | | | |

| Summary Field | Value |
|---------------|-------|
| s3_tally | [N Yes / M No / P Inconclusive] |
| s3_alignment | [ALIGNED / CONTRADICTS / MIXED — vs Stage 2] |
| s3_key_gap | [what internal sources do not address] |

**WRITE:** `simulations/prove/prove-intelligence/{topic}-prove-intelligence-{date}.md`
Confirm write.

**STAGE 3 EXIT: intelligence_complete — "s3_tally = [value]. Stage 4 ready."**

---

## STAGE 4 — ANALYSIS

**STAGE 4 ENTRY CONDITIONS:**
- [ ] STAGE 3 EXIT received: intelligence_complete
- [ ] s3_tally recorded (not blank)

**STAGE 4 BODY:**

Analyze patterns across Stages 2 + 3. Distinguish causation from correlation.

| # | Pattern | Evidence Sources (S2-# / S3-filepath) | Causal? | Confidence |
|---|---------|---------------------------------------|---------|------------|
| 1 | | | Yes/No/Unknown | Low/Med/High |
| 2 | | | | |
| 3 | | | | |
| + | add as needed | | | |

Aggregate displacement verdict (SI-05 applied to full pattern set):
  "Does the aggregate evidence pattern support the displacement of SI-04 by SI-01?
   [Yes / No / Inconclusive]"
  s4_aggregate_displacement_verdict: [Yes / No / Inconclusive]

| Summary Field | Value |
|---------------|-------|
| s4_primary_finding | [dominant pattern, 1-2 sentences] |
| s4_counter_evidence | [strongest evidence against hypothesis — cite artifact + section] |
| s4_aggregate_displacement_verdict | [Yes / No / Inconclusive] |

**WRITE:** `simulations/prove/prove-analysis/{topic}-prove-analysis-{date}.md`
Confirm write.

**STAGE 4 EXIT: analysis_complete — "s4_aggregate_displacement_verdict = [value]. Stage 5 ready."**

---

## STAGE 5 — SYNTHESIS (TWO-BLOCK + ATOMIC DUAL-LOCK)

**STAGE 5 ENTRY CONDITIONS:**
- [ ] STAGE 4 EXIT received: analysis_complete
- [ ] counter_hypothesis from Stage 1 available (exact wording)
- [ ] SI-04 (status_quo_comparator) from SESSION INVARIANTS
- [ ] s4_aggregate_displacement_verdict recorded

---

### STAGE 5 BLOCK 1 — COUNTER-HYPOTHESIS RESOLUTION

Retrieve counter_hypothesis from Stage 1. Evaluate it against the full evidence record
(Stages 2, 3, 4). BLOCK 2 cannot begin until resolution_verdict is set.

| Field | Value |
|-------|-------|
| counter_hypothesis | [from Stage 1 — verbatim copy, not paraphrased] |
| evidence_against_ch | [cite Stage artifact + section that most directly addresses it] |
| resolution_verdict | [REFUTED / PARTIALLY REFUTED / OPEN RISK] |
| resolution_note | [one sentence: why this verdict was reached] |

**BLOCK 1 GATE:** resolution_verdict must be set before BLOCK 2 begins.

**BLOCK 1 EXIT: counter_hypothesis_resolved — "resolution_verdict = [value]. Proceeding to BLOCK 2."**

---

### STAGE 5 BLOCK 2 — SYNTHESIS VERDICT (ATOMIC DUAL-LOCK)

**BLOCK 2 ENTRY CONDITIONS:**
- [ ] BLOCK 1 EXIT received: counter_hypothesis_resolved
- [ ] resolution_verdict set (not blank)

Set both [LOCKED] fields. Do not proceed to DUAL-LOCK GATE until both are marked.
If resolution_verdict = OPEN RISK, name the unresolved risk in key_risk explicitly.

| Field | Value |
|-------|-------|
| hypothesis_verdict [LOCKED] | [SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED — LOCKED] |
| displacement_conclusion [LOCKED] | [1-2 sentences: does evidence support replacing SI-04 with SI-01? Yes / No / Conditional. — LOCKED] |
| evidence_summary | [2-3 sentences integrating Stages 2, 3, 4] |
| confidence_final | [Low / Medium / High — one sentence of reasoning] |
| key_risk | [primary risk; if OPEN RISK from BLOCK 1, name that risk here] |

**DUAL-LOCK GATE:**
- [ ] hypothesis_verdict present AND marked [LOCKED]
- [ ] displacement_conclusion present AND marked [LOCKED]

If either absent or not marked [LOCKED]: set it before proceeding.
DUAL-LOCK CLEARED.

**WRITE:** `simulations/prove/prove-synthesize/{topic}-prove-synthesize-{date}.md`
Confirm write.

**STAGE 5 EXIT: synthesis_complete — "DUAL-LOCK cleared. Evidence brief complete. Ready for /topic-story."**

CAMPAIGN COMPLETE.
```
