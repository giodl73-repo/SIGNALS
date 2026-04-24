Written to `simulations/quest/variations/campaign-track-variations-R7-2026-03-16.md`.

---

## R7 Variations Summary

**Only criterion remaining**: C-10 (Dual-session delta). All five variations add it to the R6 V-05 full-stack baseline.

| | Axis | C-10 design | Checklist |
|---|---|---|---|
| **V-01** | Placement | Prose section, post-Phase 4 | 22 items |
| **V-02** | Format | Typed contract (session_number, signals_added, verdict_before/after/changed) | 22 items |
| **V-03** | Ownership | Analyst owns delta.md; Phase 3 gate requires status.md AND delta.md | 22 items |
| **V-04** | Typed + gated | V-02 contract + 5 delta fields in terminal checklist → 27 items | 27 items |
| **V-05** | Full stack | V-02 + V-03 + V-04; two-pass delta update post-Phase 4 | 27 items |

**Predicted leaderboard**: V-05 > V-04 > V-03 > V-02 > V-01

All five should score 98/98 if C-10 is binary — the open question for quest-score is whether structural quality (typed fields, role ownership, terminal gating) distinguishes within the aspirational tier or all five simply pass C-10 and tie.

Key new pattern in V-05: the **two-pass delta update** — delta.md is written in Phase 3 Step B with a placeholder `verdict_after`, then updated after Phase 4 with the actual `verdict_verb`. The terminal checklist item for `verdict_after` explicitly flags "placeholder fails" — the only order-dependent checklist item in any variation across all rounds.
ssion." The 22-item
checklist and four-phase typed contracts are unchanged from R6 V-05.

```
Run the full topic narrative campaign for: {{topic}}

Produce a complete topic dashboard showing what signals exist, what is missing, and
the narrative arc. Use at the start and end of a signal-gathering session.

This campaign runs in exactly four phases: Register -> Plan -> Status -> Narrative.
Each phase produces a distinct artifact. Do not proceed to the next phase until the
current phase artifact is written and satisfies its typed output contract.

---

## Full-Phase Type Coverage Rule

All four phases have typed output contracts. No phase is exempt. Partial coverage
fails. Each field typed as integer must contain an integer. Each field typed as
enumerated string must contain exactly one of the listed tokens.

---

## Typed Output Contracts

### Phase 1 Contract -- strategy.md

- topic_name: string (non-empty, human-readable)
- namespace: string, exactly one of:
  scout | draft | review | flow | trace | prove | listen | program | topic
- priority: string, exactly one of: High | Medium | Low
- planned_signals: list of >= 3 items; each item:
  - signal_name: string (unique within strategy)
  - target_skill: string (namespace/skill format, e.g. "scout/scout-competitors")
  - rationale: string (one sentence max)

### Phase 2 Contract -- roadmap.md

- namespace_coverage: list of namespace entries; each entry:
  - namespace: string (one of 9 Signal namespaces)
  - signals: list; each item:
    - signal_name: string (matches signal_name from strategy.md)
    - collection_purpose: string (one sentence: why this signal matters)

### Phase 3 Contract -- status.md

Coverage table -- all 9 namespace rows required; each row:
  - namespace: string
  - planned: integer >= 0 (no prose, no ranges)
  - collected: integer >= 0 (no prose, no ranges)
  - missing: list of strings (signal names; empty list [] if none missing)
  - zero_flag: "NO SIGNALS" if planned = 0 AND collected = 0; omit otherwise

Summary fields:
  - coverage_ratio: string, format "X/N" (X and N are integers)
  - readiness_verdict: string, exactly one of: READY | NOT READY | CONDITIONALLY READY

### Phase 4 Contract -- story.md

- verdict_verb: string, exactly one of:
  CONFIRMED | REFUTED | EVOLVING | INSUFFICIENT | NOT YET REACHED
- hypothesis_mutation:
  - s0: string (original hypothesis text at topic registration)
  - current: string (updated hypothesis, or literal "UNCHANGED")
- echoes: list of strings; if none, value must be ["NONE"]
- next_signal_recommendations: list of exactly 3 items; each item:
  - namespace: string
  - skill: string
  - gap_reason: string (one sentence)

---

## Prohibition Parity Rule

Each of the four campaign roles carries exactly 5 forbidden actions -- no more, no
fewer. This count is fixed. A role with 4 or 6 items is structurally invalid and
fails audit. The numbered list format is required: each item labeled 1 through 5.

---

## Roles and Prohibitions

### Registrar (Phase 1 -- topic-new)

Owns strategy.md. Produces Phase 1 Contract output.

Forbidden actions (exactly 5):
1. Must not produce coverage tables, coverage ratios, or readiness verdicts
2. Must not synthesize or interpret signal content across sources
3. Must not assign verdict verbs from Phase 4 controlled vocabulary
4. Must not invoke any sub-skill other than topic-new
5. Must not list signals not declared in the strategy planned_signals field

### Planner (Phase 2 -- topic-plan)

Owns roadmap.md. Produces Phase 2 Contract output.

Forbidden actions (exactly 5):
1. Must not register, rename, or modify the topic identity (Phase 1 domain)
2. Must not query or report which signals are collected (Phase 3 domain)
3. Must not produce readiness verdicts or coverage ratios
4. Must not synthesize findings or assign verdict verbs from Phase 4 vocabulary
5. Must not invoke any sub-skill other than topic-plan

### Analyst (Phase 3 -- topic-status)

Owns status.md. Produces Phase 3 Contract output.

Forbidden actions (exactly 5):
1. Must not add planned signals beyond what Phase 2 roadmap defines
2. Must not produce verdict verbs from Phase 4 vocabulary
3. Must not interpret meaning from signal content or editorialize on findings
4. Must not invoke any sub-skill other than topic-status
5. Must not use narrative counts ("several", "a few", "many") where integers are
   required by contract

### Narrator (Phase 4 -- topic-story)

Owns story.md. Produces Phase 4 Contract output.

Forbidden actions (exactly 5):
1. Must not modify the coverage table or coverage ratio (Phase 3 domain)
2. Must not add, remove, or reorder planned signals (Phase 2 domain)
3. Must not assign readiness verdicts (READY / NOT READY / CONDITIONALLY READY)
4. Must not invoke any sub-skill other than topic-story
5. Must not paraphrase verdict verbs -- only exact Phase 4 Contract tokens are valid;
   "likely confirmed" or "essentially confirmed" both fail

---

## Phase 1 -- Register (Registrar)

*Registrar active. Exactly 5 forbidden actions apply. Phase 1 Contract governs output.*

Invoke topic-new for {{topic}}.

Produce strategy.md conforming to Phase 1 Contract:
- topic_name (string), namespace (one of 9 tokens), priority (one of 3 tokens)
- planned_signals: >= 3 items with signal_name, target_skill, rationale

Phase 1 postcondition: strategy.md present, all Phase 1 Contract fields present and
typed correctly.

GATE: Do not proceed to Phase 2 until Phase 1 postcondition is satisfied.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan (Planner)

*Planner active. Exactly 5 forbidden actions apply. Phase 2 Contract governs output.*

Invoke topic-plan for {{topic}}.

Produce roadmap.md conforming to Phase 2 Contract:
- namespace_coverage entries for all namespaces with planned signals
- Each signal entry: signal_name (matched to strategy.md) + collection_purpose

Phase 2 postcondition: roadmap.md present with at least one namespace entry and
collection_purpose present per signal.

GATE: Do not proceed to Phase 3 until Phase 2 postcondition is satisfied.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status (Analyst)

*Analyst active. Exactly 5 forbidden actions apply. Phase 3 Contract governs output.*

Invoke topic-status for {{topic}}.

Produce status.md conforming to Phase 3 Contract:
- All 9 namespace rows present -- no row skipped
- planned and collected are integers -- narrative counts fail
- missing lists each signal by name -- counts alone fail
- zero_flag = "NO SIGNALS" where planned = 0 AND collected = 0
- coverage_ratio in "X/N" format; readiness_verdict from 3-token set

Phase 3 postcondition: status.md present, 9 rows with integer fields, readiness_verdict
assigned from enumerated set.

GATE: Do not proceed to Phase 4 until Phase 3 postcondition is satisfied.

Write to: simulations/topic/{{topic}}-status-{{date}}.md

---

## Phase 4 -- Narrative (Narrator)

*Narrator active. Exactly 5 forbidden actions apply. Phase 4 Contract governs output.*

Invoke topic-story for {{topic}}.

Produce story.md conforming to Phase 4 Contract:
- verdict_verb: exactly one of the 5 enumerated tokens (no paraphrase)
- hypothesis_mutation: s0 (original) + current (updated or "UNCHANGED")
- echoes: list present, minimum ["NONE"]
- next_signal_recommendations: exactly 3 items with namespace + skill + gap_reason

Phase 4 postcondition: story.md present with verdict_verb from 5-token set, s0
field, echoes list, and 3-item recommendations.

Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Session Delta

After Phase 4 completes, compute what changed since the prior session for {{topic}}.

If prior session artifacts exist (prior status.md and story.md are present):
- signals_added: list of signal names whose collected count increased from 0 to > 0
  since the last status.md. If none increased: "NONE".
- verdict_before: the verdict_verb from the prior session story.md
- verdict_after: the verdict_verb from the current story.md
- verdict_changed: "YES" if verdict_before != verdict_after, else "NO"

If no prior session artifacts exist (first invocation):
- signals_added: "Session 1 -- no prior session"
- verdict_before: "NONE"
- verdict_after: current verdict_verb from Phase 4
- verdict_changed: "N/A"

Write delta summary to: simulations/topic/{{topic}}-delta-{{date}}.md

---

## Empty-State Handling

### First Invocation (0 signals collected)

All four phases run and produce full artifacts per their typed contracts.

Phase 1 (Registrar): Create strategy.md per Phase 1 Contract. planned_signals must
  list >= 3 entries. This is the founding artifact.

Phase 2 (Planner): Create roadmap.md per Phase 2 Contract. All signals are planned;
  none are collected. roadmap.md documents what will be collected.

Phase 3 (Analyst): All rows have collected = 0 (integer). missing lists all planned
  signals from roadmap.md by signal_name. zero_flag = "NO SIGNALS" for namespaces
  where planned = 0 AND collected = 0. readiness_verdict = "NOT READY".

Phase 4 (Narrator): verdict_verb = "NOT YET REACHED". hypothesis_mutation.current
  = "UNCHANGED". echoes = ["NONE"]. next_signal_recommendations: top 3 signals from
  roadmap.md ordered by planned priority.

Session Delta (first invocation): signals_added = "Session 1 -- no prior session".
  verdict_before = "NONE". verdict_changed = "N/A".

---

## TERMINAL -- Field-Level Completion Checklist

Verify each field below independently before marking the campaign complete. Each item
names a specific artifact field and its constraint. A field that satisfies the
constraint PASSES. A field that fails triggers re-run of the affected phase only.
Implicit completion is not acceptable.

### Phase 1 -- strategy.md

[ ] topic_name: string present, non-empty
    FAIL: re-run Phase 1

[ ] namespace: exactly one of {scout|draft|review|flow|trace|prove|listen|program|topic}
    FAIL: re-run Phase 1

[ ] priority: exactly one of {High|Medium|Low}
    FAIL: re-run Phase 1

[ ] planned_signals: count >= 3 (integer count, not estimated)
    FAIL: re-run Phase 1

[ ] planned_signals[*].target_skill: each in namespace/skill format
    FAIL: re-run Phase 1

### Phase 2 -- roadmap.md

[ ] namespace_coverage: at least one entry present
    FAIL: re-run Phase 2

[ ] namespace_coverage[*].collection_purpose: string present per signal (not omitted)
    FAIL: re-run Phase 2

### Phase 3 -- status.md

[ ] row count: exactly 9 namespace rows present
    FAIL: re-run Phase 3

[ ] planned: integer value in all 9 rows (not prose, not a range)
    FAIL: re-run Phase 3

[ ] collected: integer value in all 9 rows (not prose, not a range)
    FAIL: re-run Phase 3

[ ] missing: list of signal names in each row (not a count -- names required)
    FAIL: re-run Phase 3

[ ] zero_flag: "NO SIGNALS" present for every row where planned = 0 AND collected = 0
    FAIL: re-run Phase 3

[ ] coverage_ratio: "X/N" format (X and N are both integers)
    FAIL: re-run Phase 3

[ ] readiness_verdict: exactly one of {READY|NOT READY|CONDITIONALLY READY}
    FAIL: re-run Phase 3

### Phase 4 -- story.md

[ ] verdict_verb: exactly one of
    {CONFIRMED|REFUTED|EVOLVING|INSUFFICIENT|NOT YET REACHED}
    FAIL: re-run Phase 4

[ ] hypothesis_mutation.s0: string present, non-empty
    FAIL: re-run Phase 4

[ ] hypothesis_mutation.current: string present ("UNCHANGED" or updated hypothesis)
    FAIL: re-run Phase 4

[ ] echoes: list present with at least one entry (minimum ["NONE"])
    FAIL: re-run Phase 4

[ ] next_signal_recommendations: exactly 3 items
    FAIL: re-run Phase 4

[ ] next_signal_recommendations[*].namespace: string present for all 3
    FAIL: re-run Phase 4

[ ] next_signal_recommendations[*].gap_reason: string present for all 3
    FAIL: re-run Phase 4

All 22 items PASS: campaign is complete. Dashboard ready to emit.
Any item FAIL: re-run the affected phase. Re-verify the failed item only.

---

## Output: Topic Dashboard

When all 22 TERMINAL items show PASS, emit consolidated dashboard in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Narrative verdict + hypothesis mutation + echoes + top-3 recommendations (Phase 4)
5. Session delta summary (signals added since last session, verdict change)
```

**Rubric targeting**: C-01 through C-09, C-11 through C-16, C-22 through C-24 inherited
from R6 V-05 unchanged. C-10: Session Delta section present after Phase 4; signals_added
field names newly-collected signals; verdict_before/after/changed computes verdict delta;
first-invocation case handled; delta written to artifact. The dashboard output line 5
references the delta explicitly.

**Risk**: The delta section is untyped -- signals_added may render as a prose string
("Session 1 -- no prior session") rather than a list on first invocation, which is
technically a type inconsistency. A scorer checking C-10 passes on presence + content;
a scorer checking C-24 would note delta fields are absent from the terminal checklist
(delta is not in the 22-item checklist). C-10 should PASS; C-24 is not at risk because
it already passed in R6 V-05 via the 22 phase-field items.

---

## V-02 -- Axis: Typed session delta contract (format)

**Hypothesis**: Giving the delta a formal typed output contract (analogous to Phase
1-4 contracts) makes C-10 compliance mechanically auditable -- the same pattern that
distinguishes C-23 from C-15. A typed contract for delta.md forces the model to
produce structured fields rather than a prose summary. The Full-Phase Type Coverage
Rule explicitly scopes to the four campaign phases; the delta contract is supplemental.
No prohibition list changes, no checklist changes, no role ownership changes.

```
Run the full topic narrative campaign for: {{topic}}

Produce a complete topic dashboard showing what signals exist, what is missing, and
the narrative arc. Use at the start and end of a signal-gathering session.

This campaign runs in exactly four phases: Register -> Plan -> Status -> Narrative.
Each phase produces a distinct artifact. Do not proceed to the next phase until the
current phase artifact is written and satisfies its typed output contract.

---

## Full-Phase Type Coverage Rule

All four campaign phases have typed output contracts. No phase is exempt. Partial
coverage of the four phases fails. Each field typed as integer must contain an
integer. Each field typed as enumerated string must contain exactly one of the
listed tokens.

The Session Delta contract (below) is supplemental -- it applies after Phase 4
and does not affect the four-phase coverage rule.

---

## Typed Output Contracts

### Phase 1 Contract -- strategy.md

- topic_name: string (non-empty, human-readable)
- namespace: string, exactly one of:
  scout | draft | review | flow | trace | prove | listen | program | topic
- priority: string, exactly one of: High | Medium | Low
- planned_signals: list of >= 3 items; each item:
  - signal_name: string (unique within strategy)
  - target_skill: string (namespace/skill format, e.g. "scout/scout-competitors")
  - rationale: string (one sentence max)

### Phase 2 Contract -- roadmap.md

- namespace_coverage: list of namespace entries; each entry:
  - namespace: string (one of 9 Signal namespaces)
  - signals: list; each item:
    - signal_name: string (matches signal_name from strategy.md)
    - collection_purpose: string (one sentence: why this signal matters)

### Phase 3 Contract -- status.md

Coverage table -- all 9 namespace rows required; each row:
  - namespace: string
  - planned: integer >= 0 (no prose, no ranges)
  - collected: integer >= 0 (no prose, no ranges)
  - missing: list of strings (signal names; empty list [] if none missing)
  - zero_flag: "NO SIGNALS" if planned = 0 AND collected = 0; omit otherwise

Summary fields:
  - coverage_ratio: string, format "X/N" (X and N are integers)
  - readiness_verdict: string, exactly one of: READY | NOT READY | CONDITIONALLY READY

### Phase 4 Contract -- story.md

- verdict_verb: string, exactly one of:
  CONFIRMED | REFUTED | EVOLVING | INSUFFICIENT | NOT YET REACHED
- hypothesis_mutation:
  - s0: string (original hypothesis text at topic registration)
  - current: string (updated hypothesis, or literal "UNCHANGED")
- echoes: list of strings; if none, value must be ["NONE"]
- next_signal_recommendations: list of exactly 3 items; each item:
  - namespace: string
  - skill: string
  - gap_reason: string (one sentence)

### Session Delta Contract -- delta.md

- session_number: integer >= 1 (1 on first invocation, incremented each run)
- signals_added: list of strings (signal names newly collected since prior session;
  empty list [] if none added or if session_number = 1)
- signals_removed: list of strings (signals that were collected and are now missing;
  empty list [] if none or if session_number = 1)
- verdict_before: string, exactly one of:
  CONFIRMED | REFUTED | EVOLVING | INSUFFICIENT | NOT YET REACHED | NONE
  (NONE only when session_number = 1)
- verdict_after: string, exactly one of:
  CONFIRMED | REFUTED | EVOLVING | INSUFFICIENT | NOT YET REACHED
- verdict_changed: string, exactly one of: YES | NO | N/A
  (N/A only when session_number = 1)

---

## Prohibition Parity Rule

Each of the four campaign roles carries exactly 5 forbidden actions -- no more, no
fewer. This count is fixed. A role with 4 or 6 items is structurally invalid and
fails audit. The numbered list format is required: each item labeled 1 through 5.

---

## Roles and Prohibitions

### Registrar (Phase 1 -- topic-new)

Owns strategy.md. Produces Phase 1 Contract output.

Forbidden actions (exactly 5):
1. Must not produce coverage tables, coverage ratios, or readiness verdicts
2. Must not synthesize or interpret signal content across sources
3. Must not assign verdict verbs from Phase 4 controlled vocabulary
4. Must not invoke any sub-skill other than topic-new
5. Must not list signals not declared in the strategy planned_signals field

### Planner (Phase 2 -- topic-plan)

Owns roadmap.md. Produces Phase 2 Contract output.

Forbidden actions (exactly 5):
1. Must not register, rename, or modify the topic identity (Phase 1 domain)
2. Must not query or report which signals are collected (Phase 3 domain)
3. Must not produce readiness verdicts or coverage ratios
4. Must not synthesize findings or assign verdict verbs from Phase 4 vocabulary
5. Must not invoke any sub-skill other than topic-plan

### Analyst (Phase 3 -- topic-status)

Owns status.md. Produces Phase 3 Contract output.

Forbidden actions (exactly 5):
1. Must not add planned signals beyond what Phase 2 roadmap defines
2. Must not produce verdict verbs from Phase 4 vocabulary
3. Must not interpret meaning from signal content or editorialize on findings
4. Must not invoke any sub-skill other than topic-status
5. Must not use narrative counts ("several", "a few", "many") where integers are
   required by contract

### Narrator (Phase 4 -- topic-story)

Owns story.md. Produces Phase 4 Contract output.

Forbidden actions (exactly 5):
1. Must not modify the coverage table or coverage ratio (Phase 3 domain)
2. Must not add, remove, or reorder planned signals (Phase 2 domain)
3. Must not assign readiness verdicts (READY / NOT READY / CONDITIONALLY READY)
4. Must not invoke any sub-skill other than topic-story
5. Must not paraphrase verdict verbs -- only exact Phase 4 Contract tokens are valid;
   "likely confirmed" or "essentially confirmed" both fail

---

## Phase 1 -- Register (Registrar)

*Registrar active. Exactly 5 forbidden actions apply. Phase 1 Contract governs output.*

Invoke topic-new for {{topic}}.

Produce strategy.md conforming to Phase 1 Contract:
- topic_name (string), namespace (one of 9 tokens), priority (one of 3 tokens)
- planned_signals: >= 3 items with signal_name, target_skill, rationale

Phase 1 postcondition: strategy.md present, all Phase 1 Contract fields present and
typed correctly.

GATE: Do not proceed to Phase 2 until Phase 1 postcondition is satisfied.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan (Planner)

*Planner active. Exactly 5 forbidden actions apply. Phase 2 Contract governs output.*

Invoke topic-plan for {{topic}}.

Produce roadmap.md conforming to Phase 2 Contract:
- namespace_coverage entries for all namespaces with planned signals
- Each signal entry: signal_name (matched to strategy.md) + collection_purpose

Phase 2 postcondition: roadmap.md present with at least one namespace entry and
collection_purpose present per signal.

GATE: Do not proceed to Phase 3 until Phase 2 postcondition is satisfied.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status (Analyst)

*Analyst active. Exactly 5 forbidden actions apply. Phase 3 Contract governs output.*

Invoke topic-status for {{topic}}.

Produce status.md conforming to Phase 3 Contract:
- All 9 namespace rows present -- no row skipped
- planned and collected are integers -- narrative counts fail
- missing lists each signal by name -- counts alone fail
- zero_flag = "NO SIGNALS" where planned = 0 AND collected = 0
- coverage_ratio in "X/N" format; readiness_verdict from 3-token set

Phase 3 postcondition: status.md present, 9 rows with integer fields, readiness_verdict
assigned from enumerated set.

GATE: Do not proceed to Phase 4 until Phase 3 postcondition is satisfied.

Write to: simulations/topic/{{topic}}-status-{{date}}.md

---

## Phase 4 -- Narrative (Narrator)

*Narrator active. Exactly 5 forbidden actions apply. Phase 4 Contract governs output.*

Invoke topic-story for {{topic}}.

Produce story.md conforming to Phase 4 Contract:
- verdict_verb: exactly one of the 5 enumerated tokens (no paraphrase)
- hypothesis_mutation: s0 (original) + current (updated or "UNCHANGED")
- echoes: list present, minimum ["NONE"]
- next_signal_recommendations: exactly 3 items with namespace + skill + gap_reason

Phase 4 postcondition: story.md present with verdict_verb from 5-token set, s0
field, echoes list, and 3-item recommendations.

Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Session Delta

After Phase 4 completes, produce delta.md conforming to Session Delta Contract.

Step 1 -- Locate prior session artifacts:
  Look for the most recent prior {{topic}}-status-*.md and {{topic}}-story-*.md
  (any date earlier than {{date}}).

Step 2 -- Compute fields:
  If prior artifacts exist:
    session_number: increment prior session_number by 1 (or 2 if no prior delta.md)
    signals_added: signal names in current status.md with collected > 0 that had
      collected = 0 in prior status.md
    signals_removed: signal names in prior status.md with collected > 0 that now
      have collected = 0
    verdict_before: verdict_verb from prior story.md
    verdict_after: verdict_verb from current story.md
    verdict_changed: "YES" if verdict_before != verdict_after, else "NO"

  If no prior artifacts exist (first invocation):
    session_number: 1
    signals_added: []
    signals_removed: []
    verdict_before: "NONE"
    verdict_after: verdict_verb from current story.md
    verdict_changed: "N/A"

Write to: simulations/topic/{{topic}}-delta-{{date}}.md

---

## Empty-State Handling

### First Invocation (0 signals collected)

All four phases run and produce full artifacts per their typed contracts.

Phase 1 (Registrar): Create strategy.md per Phase 1 Contract. planned_signals must
  list >= 3 entries. This is the founding artifact.

Phase 2 (Planner): Create roadmap.md per Phase 2 Contract. All signals are planned;
  none are collected. roadmap.md documents what will be collected.

Phase 3 (Analyst): All rows have collected = 0 (integer). missing lists all planned
  signals from roadmap.md by signal_name. zero_flag = "NO SIGNALS" for namespaces
  where planned = 0 AND collected = 0. readiness_verdict = "NOT READY".

Phase 4 (Narrator): verdict_verb = "NOT YET REACHED". hypothesis_mutation.current
  = "UNCHANGED". echoes = ["NONE"]. next_signal_recommendations: top 3 signals from
  roadmap.md ordered by planned priority.

Session Delta (first invocation): session_number = 1. signals_added = [].
  signals_removed = []. verdict_before = "NONE". verdict_changed = "N/A".
  All fields conform to Session Delta Contract.

---

## TERMINAL -- Field-Level Completion Checklist

Verify each field below independently before marking the campaign complete. Each item
names a specific artifact field and its constraint. A field that satisfies the
constraint PASSES. A field that fails triggers re-run of the affected phase only.
Implicit completion is not acceptable.

### Phase 1 -- strategy.md

[ ] topic_name: string present, non-empty
    FAIL: re-run Phase 1

[ ] namespace: exactly one of {scout|draft|review|flow|trace|prove|listen|program|topic}
    FAIL: re-run Phase 1

[ ] priority: exactly one of {High|Medium|Low}
    FAIL: re-run Phase 1

[ ] planned_signals: count >= 3 (integer count, not estimated)
    FAIL: re-run Phase 1

[ ] planned_signals[*].target_skill: each in namespace/skill format
    FAIL: re-run Phase 1

### Phase 2 -- roadmap.md

[ ] namespace_coverage: at least one entry present
    FAIL: re-run Phase 2

[ ] namespace_coverage[*].collection_purpose: string present per signal (not omitted)
    FAIL: re-run Phase 2

### Phase 3 -- status.md

[ ] row count: exactly 9 namespace rows present
    FAIL: re-run Phase 3

[ ] planned: integer value in all 9 rows (not prose, not a range)
    FAIL: re-run Phase 3

[ ] collected: integer value in all 9 rows (not prose, not a range)
    FAIL: re-run Phase 3

[ ] missing: list of signal names in each row (not a count -- names required)
    FAIL: re-run Phase 3

[ ] zero_flag: "NO SIGNALS" present for every row where planned = 0 AND collected = 0
    FAIL: re-run Phase 3

[ ] coverage_ratio: "X/N" format (X and N are both integers)
    FAIL: re-run Phase 3

[ ] readiness_verdict: exactly one of {READY|NOT READY|CONDITIONALLY READY}
    FAIL: re-run Phase 3

### Phase 4 -- story.md

[ ] verdict_verb: exactly one of
    {CONFIRMED|REFUTED|EVOLVING|INSUFFICIENT|NOT YET REACHED}
    FAIL: re-run Phase 4

[ ] hypothesis_mutation.s0: string present, non-empty
    FAIL: re-run Phase 4

[ ] hypothesis_mutation.current: string present ("UNCHANGED" or updated hypothesis)
    FAIL: re-run Phase 4

[ ] echoes: list present with at least one entry (minimum ["NONE"])
    FAIL: re-run Phase 4

[ ] next_signal_recommendations: exactly 3 items
    FAIL: re-run Phase 4

[ ] next_signal_recommendations[*].namespace: string present for all 3
    FAIL: re-run Phase 4

[ ] next_signal_recommendations[*].gap_reason: string present for all 3
    FAIL: re-run Phase 4

All 22 items PASS: campaign is complete. Dashboard ready to emit.
Any item FAIL: re-run the affected phase. Re-verify the failed item only.

---

## Output: Topic Dashboard

When all 22 TERMINAL items show PASS, emit consolidated dashboard in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Narrative verdict + hypothesis mutation + echoes + top-3 recommendations (Phase 4)
5. Session delta: session_number, signals_added count, verdict_before -> verdict_after,
   verdict_changed
```

**Rubric targeting**: C-10: Session Delta Contract fully typed (session_number integer,
signals_added list, verdict_before/after enumerated tokens including NONE sentinel,
verdict_changed YES/NO/N/A). Signals added and verdict change summary both present per
contract. First-invocation behavior typed (not prose). C-23: Full-Phase Type Coverage
Rule explicitly scopes to the four campaign phases; supplemental note prevents C-23
scorer from reading the delta contract as a fifth required phase. All other criteria
inherited from R6 V-05 unchanged.

**Risk**: The "supplemental" framing for the delta contract may confuse a model that
reads the Full-Phase Type Coverage Rule as applying to all contracts in the document.
Adding the explicit scope note ("does not affect the four-phase coverage rule") is the
mitigation. The 22-item checklist has no delta fields -- a model that completes the
checklist but omits delta.md is not caught by the terminal gate.

---

## V-03 -- Axis: Analyst-owned session delta (ownership)

**Hypothesis**: Assigning delta computation to the Analyst role -- the role that already
owns status.md and has the most direct access to coverage data -- makes the delta an
integral part of Phase 3 rather than an afterthought. The Analyst's Phase 3
postcondition expands to require both status.md and delta.md. No prohibition list
changes (parity stays at exactly 5). No typed contract for delta (narrative ownership
only). No checklist changes. The ownership signal alone should pass C-10.

```
Run the full topic narrative campaign for: {{topic}}

Produce a complete topic dashboard showing what signals exist, what is missing, and
the narrative arc. Use at the start and end of a signal-gathering session.

This campaign runs in exactly four phases: Register -> Plan -> Status -> Narrative.
Each phase produces a distinct artifact. Do not proceed to the next phase until the
current phase artifact is written and satisfies its typed output contract.

---

## Full-Phase Type Coverage Rule

All four phases have typed output contracts. No phase is exempt. Partial coverage
fails. Each field typed as integer must contain an integer. Each field typed as
enumerated string must contain exactly one of the listed tokens.

---

## Typed Output Contracts

### Phase 1 Contract -- strategy.md

- topic_name: string (non-empty, human-readable)
- namespace: string, exactly one of:
  scout | draft | review | flow | trace | prove | listen | program | topic
- priority: string, exactly one of: High | Medium | Low
- planned_signals: list of >= 3 items; each item:
  - signal_name: string (unique within strategy)
  - target_skill: string (namespace/skill format, e.g. "scout/scout-competitors")
  - rationale: string (one sentence max)

### Phase 2 Contract -- roadmap.md

- namespace_coverage: list of namespace entries; each entry:
  - namespace: string (one of 9 Signal namespaces)
  - signals: list; each item:
    - signal_name: string (matches signal_name from strategy.md)
    - collection_purpose: string (one sentence: why this signal matters)

### Phase 3 Contract -- status.md

Coverage table -- all 9 namespace rows required; each row:
  - namespace: string
  - planned: integer >= 0 (no prose, no ranges)
  - collected: integer >= 0 (no prose, no ranges)
  - missing: list of strings (signal names; empty list [] if none missing)
  - zero_flag: "NO SIGNALS" if planned = 0 AND collected = 0; omit otherwise

Summary fields:
  - coverage_ratio: string, format "X/N" (X and N are integers)
  - readiness_verdict: string, exactly one of: READY | NOT READY | CONDITIONALLY READY

### Phase 4 Contract -- story.md

- verdict_verb: string, exactly one of:
  CONFIRMED | REFUTED | EVOLVING | INSUFFICIENT | NOT YET REACHED
- hypothesis_mutation:
  - s0: string (original hypothesis text at topic registration)
  - current: string (updated hypothesis, or literal "UNCHANGED")
- echoes: list of strings; if none, value must be ["NONE"]
- next_signal_recommendations: list of exactly 3 items; each item:
  - namespace: string
  - skill: string
  - gap_reason: string (one sentence)

---

## Prohibition Parity Rule

Each of the four campaign roles carries exactly 5 forbidden actions -- no more, no
fewer. This count is fixed. A role with 4 or 6 items is structurally invalid and
fails audit. The numbered list format is required: each item labeled 1 through 5.

---

## Roles and Prohibitions

### Registrar (Phase 1 -- topic-new)

Owns strategy.md. Produces Phase 1 Contract output.

Forbidden actions (exactly 5):
1. Must not produce coverage tables, coverage ratios, or readiness verdicts
2. Must not synthesize or interpret signal content across sources
3. Must not assign verdict verbs from Phase 4 controlled vocabulary
4. Must not invoke any sub-skill other than topic-new
5. Must not list signals not declared in the strategy planned_signals field

### Planner (Phase 2 -- topic-plan)

Owns roadmap.md. Produces Phase 2 Contract output.

Forbidden actions (exactly 5):
1. Must not register, rename, or modify the topic identity (Phase 1 domain)
2. Must not query or report which signals are collected (Phase 3 domain)
3. Must not produce readiness verdicts or coverage ratios
4. Must not synthesize findings or assign verdict verbs from Phase 4 vocabulary
5. Must not invoke any sub-skill other than topic-plan

### Analyst (Phase 3 -- topic-status + session delta)

Owns status.md AND delta.md. Produces Phase 3 Contract output and session delta.
The Analyst is the only role with access to both current and prior coverage data.

Forbidden actions (exactly 5):
1. Must not add planned signals beyond what Phase 2 roadmap defines
2. Must not produce verdict verbs from Phase 4 vocabulary
3. Must not interpret meaning from signal content or editorialize on findings
4. Must not invoke any sub-skill other than topic-status
5. Must not use narrative counts ("several", "a few", "many") where integers are
   required by contract

### Narrator (Phase 4 -- topic-story)

Owns story.md. Produces Phase 4 Contract output.

Forbidden actions (exactly 5):
1. Must not modify the coverage table or coverage ratio (Phase 3 domain)
2. Must not add, remove, or reorder planned signals (Phase 2 domain)
3. Must not assign readiness verdicts (READY / NOT READY / CONDITIONALLY READY)
4. Must not invoke any sub-skill other than topic-story
5. Must not paraphrase verdict verbs -- only exact Phase 4 Contract tokens are valid;
   "likely confirmed" or "essentially confirmed" both fail

---

## Phase 1 -- Register (Registrar)

*Registrar active. Exactly 5 forbidden actions apply. Phase 1 Contract governs output.*

Invoke topic-new for {{topic}}.

Produce strategy.md conforming to Phase 1 Contract:
- topic_name (string), namespace (one of 9 tokens), priority (one of 3 tokens)
- planned_signals: >= 3 items with signal_name, target_skill, rationale

Phase 1 postcondition: strategy.md present, all Phase 1 Contract fields present and
typed correctly.

GATE: Do not proceed to Phase 2 until Phase 1 postcondition is satisfied.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan (Planner)

*Planner active. Exactly 5 forbidden actions apply. Phase 2 Contract governs output.*

Invoke topic-plan for {{topic}}.

Produce roadmap.md conforming to Phase 2 Contract:
- namespace_coverage entries for all namespaces with planned signals
- Each signal entry: signal_name (matched to strategy.md) + collection_purpose

Phase 2 postcondition: roadmap.md present with at least one namespace entry and
collection_purpose present per signal.

GATE: Do not proceed to Phase 3 until Phase 2 postcondition is satisfied.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status + Session Delta (Analyst)

*Analyst active. Exactly 5 forbidden actions apply. Phase 3 Contract governs output.*

### Step A -- Status

Invoke topic-status for {{topic}}.

Produce status.md conforming to Phase 3 Contract:
- All 9 namespace rows present -- no row skipped
- planned and collected are integers -- narrative counts fail
- missing lists each signal by name -- counts alone fail
- zero_flag = "NO SIGNALS" where planned = 0 AND collected = 0
- coverage_ratio in "X/N" format; readiness_verdict from 3-token set

### Step B -- Session Delta

After status.md is written, compute what changed since the prior session.

If prior session artifacts exist (prior status.md or story.md for {{topic}}):
  - signals_added: list of signal names whose collected count increased from 0 to > 0
    since the last status.md. Write each name. If none: write "NONE".
  - verdict_before: the verdict_verb from the prior session story.md
  - verdict_after: the readiness_verdict direction from current status.md
    (use "NOT YET REACHED" if no story.md exists yet for this session)
  - verdict_changed: "YES" if verdict changed, "NO" if unchanged

If no prior session artifacts exist (first invocation):
  - signals_added: "Session 1 -- no prior session"
  - verdict_before: "NONE"
  - verdict_changed: "N/A"

Phase 3 postcondition: status.md AND delta.md both present. status.md has 9 rows
with integer fields. delta.md has signals_added and verdict change summary.

GATE: Do not proceed to Phase 4 until Phase 3 postcondition is satisfied.

Write status to: simulations/topic/{{topic}}-status-{{date}}.md
Write delta to:  simulations/topic/{{topic}}-delta-{{date}}.md

---

## Phase 4 -- Narrative (Narrator)

*Narrator active. Exactly 5 forbidden actions apply. Phase 4 Contract governs output.*

Invoke topic-story for {{topic}}.

Produce story.md conforming to Phase 4 Contract:
- verdict_verb: exactly one of the 5 enumerated tokens (no paraphrase)
- hypothesis_mutation: s0 (original) + current (updated or "UNCHANGED")
- echoes: list present, minimum ["NONE"]
- next_signal_recommendations: exactly 3 items with namespace + skill + gap_reason

Phase 4 postcondition: story.md present with verdict_verb from 5-token set, s0
field, echoes list, and 3-item recommendations.

Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Empty-State Handling

### First Invocation (0 signals collected)

All four phases run and produce full artifacts per their typed contracts.

Phase 1 (Registrar): Create strategy.md per Phase 1 Contract. planned_signals must
  list >= 3 entries. This is the founding artifact.

Phase 2 (Planner): Create roadmap.md per Phase 2 Contract. All signals are planned;
  none are collected. roadmap.md documents what will be collected.

Phase 3 (Analyst): All rows have collected = 0 (integer). missing lists all planned
  signals from roadmap.md by signal_name. zero_flag = "NO SIGNALS" for namespaces
  where planned = 0 AND collected = 0. readiness_verdict = "NOT READY".
  Session delta (Step B): signals_added = "Session 1 -- no prior session".
  verdict_before = "NONE". verdict_changed = "N/A". Write delta.md.

Phase 4 (Narrator): verdict_verb = "NOT YET REACHED". hypothesis_mutation.current
  = "UNCHANGED". echoes = ["NONE"]. next_signal_recommendations: top 3 signals from
  roadmap.md ordered by planned priority.

---

## TERMINAL -- Field-Level Completion Checklist

Verify each field below independently before marking the campaign complete. Each item
names a specific artifact field and its constraint. A field that satisfies the
constraint PASSES. A field that fails triggers re-run of the affected phase only.
Implicit completion is not acceptable.

### Phase 1 -- strategy.md

[ ] topic_name: string present, non-empty
    FAIL: re-run Phase 1

[ ] namespace: exactly one of {scout|draft|review|flow|trace|prove|listen|program|topic}
    FAIL: re-run Phase 1

[ ] priority: exactly one of {High|Medium|Low}
    FAIL: re-run Phase 1

[ ] planned_signals: count >= 3 (integer count, not estimated)
    FAIL: re-run Phase 1

[ ] planned_signals[*].target_skill: each in namespace/skill format
    FAIL: re-run Phase 1

### Phase 2 -- roadmap.md

[ ] namespace_coverage: at least one entry present
    FAIL: re-run Phase 2

[ ] namespace_coverage[*].collection_purpose: string present per signal (not omitted)
    FAIL: re-run Phase 2

### Phase 3 -- status.md

[ ] row count: exactly 9 namespace rows present
    FAIL: re-run Phase 3

[ ] planned: integer value in all 9 rows (not prose, not a range)
    FAIL: re-run Phase 3

[ ] collected: integer value in all 9 rows (not prose, not a range)
    FAIL: re-run Phase 3

[ ] missing: list of signal names in each row (not a count -- names required)
    FAIL: re-run Phase 3

[ ] zero_flag: "NO SIGNALS" present for every row where planned = 0 AND collected = 0
    FAIL: re-run Phase 3

[ ] coverage_ratio: "X/N" format (X and N are both integers)
    FAIL: re-run Phase 3

[ ] readiness_verdict: exactly one of {READY|NOT READY|CONDITIONALLY READY}
    FAIL: re-run Phase 3

### Phase 4 -- story.md

[ ] verdict_verb: exactly one of
    {CONFIRMED|REFUTED|EVOLVING|INSUFFICIENT|NOT YET REACHED}
    FAIL: re-run Phase 4

[ ] hypothesis_mutation.s0: string present, non-empty
    FAIL: re-run Phase 4

[ ] hypothesis_mutation.current: string present ("UNCHANGED" or updated hypothesis)
    FAIL: re-run Phase 4

[ ] echoes: list present with at least one entry (minimum ["NONE"])
    FAIL: re-run Phase 4

[ ] next_signal_recommendations: exactly 3 items
    FAIL: re-run Phase 4

[ ] next_signal_recommendations[*].namespace: string present for all 3
    FAIL: re-run Phase 4

[ ] next_signal_recommendations[*].gap_reason: string present for all 3
    FAIL: re-run Phase 4

All 22 items PASS: campaign is complete. Dashboard ready to emit.
Any item FAIL: re-run the affected phase. Re-verify the failed item only.

---

## Output: Topic Dashboard

When all 22 TERMINAL items show PASS, emit consolidated dashboard in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Narrative verdict + hypothesis mutation + echoes + top-3 recommendations (Phase 4)
5. Session delta summary from delta.md (signals added, verdict change)
```

**Rubric targeting**: C-10: Delta is owned by Analyst (named role, explicit assignment
in role description and Phase 3 body). signals_added section present. verdict_before/
verdict_after/verdict_changed computed and written to delta.md. First-invocation case
handled per-phase in empty-state section. C-22: Parity rule unchanged -- Analyst still
has exactly 5 prohibitions; delta ownership is in role description, not prohibition
list. C-23: Full-Phase Type Coverage Rule unchanged -- delta is a Step B within Phase 3,
not a 5th phase. All other criteria inherited from R6 V-05.

**Risk**: The delta contract is not typed in V-03 -- signals_added may render as a prose
string ("Session 1 -- no prior session") on first invocation. C-10 should PASS because
the criterion only requires signals added + verdict change summary to be present; type
constraints are not part of C-10. The delta is gated at Phase 3 postcondition
("status.md AND delta.md both present"), which means a model that omits delta.md cannot
advance to Phase 4 -- stronger enforcement than V-01 and V-02.

---

## V-04 -- Combined: Typed delta contract + delta fields in terminal checklist

**Axes**: Format (V-02 typed contract) + Behavior (terminal checklist fields for delta)

**Hypothesis**: A typed delta contract satisfies C-10 structurally. Adding delta fields
to the terminal checklist makes delta compliance mechanically verifiable at the same
level as Phase 1-4 fields. The checklist grows from 22 to 27 items. The item count is
stated explicitly -- "All 27 items PASS" -- making incomplete delta output visible.
Combined, C-10 is both structurally typed AND terminally gated.

```
Run the full topic narrative campaign for: {{topic}}

Produce a complete topic dashboard showing what signals exist, what is missing, and
the narrative arc. Use at the start and end of a signal-gathering session.

This campaign runs in exactly four phases: Register -> Plan -> Status -> Narrative.
Each phase produces a distinct artifact. Do not proceed to the next phase until the
current phase artifact is written and satisfies its typed output contract.

---

## Full-Phase Type Coverage Rule

All four campaign phases have typed output contracts. No phase is exempt. Partial
coverage of the four phases fails. Each field typed as integer must contain an
integer. Each field typed as enumerated string must contain exactly one of the
listed tokens.

The Session Delta contract is supplemental -- it applies after Phase 4 and does not
affect the four-phase coverage rule.

---

## Typed Output Contracts

### Phase 1 Contract -- strategy.md

- topic_name: string (non-empty, human-readable)
- namespace: string, exactly one of:
  scout | draft | review | flow | trace | prove | listen | program | topic
- priority: string, exactly one of: High | Medium | Low
- planned_signals: list of >= 3 items; each item:
  - signal_name: string (unique within strategy)
  - target_skill: string (namespace/skill format, e.g. "scout/scout-competitors")
  - rationale: string (one sentence max)

### Phase 2 Contract -- roadmap.md

- namespace_coverage: list of namespace entries; each entry:
  - namespace: string (one of 9 Signal namespaces)
  - signals: list; each item:
    - signal_name: string (matches signal_name from strategy.md)
    - collection_purpose: string (one sentence: why this signal matters)

### Phase 3 Contract -- status.md

Coverage table -- all 9 namespace rows required; each row:
  - namespace: string
  - planned: integer >= 0 (no prose, no ranges)
  - collected: integer >= 0 (no prose, no ranges)
  - missing: list of strings (signal names; empty list [] if none missing)
  - zero_flag: "NO SIGNALS" if planned = 0 AND collected = 0; omit otherwise

Summary fields:
  - coverage_ratio: string, format "X/N" (X and N are integers)
  - readiness_verdict: string, exactly one of: READY | NOT READY | CONDITIONALLY READY

### Phase 4 Contract -- story.md

- verdict_verb: string, exactly one of:
  CONFIRMED | REFUTED | EVOLVING | INSUFFICIENT | NOT YET REACHED
- hypothesis_mutation:
  - s0: string (original hypothesis text at topic registration)
  - current: string (updated hypothesis, or literal "UNCHANGED")
- echoes: list of strings; if none, value must be ["NONE"]
- next_signal_recommendations: list of exactly 3 items; each item:
  - namespace: string
  - skill: string
  - gap_reason: string (one sentence)

### Session Delta Contract -- delta.md

- session_number: integer >= 1 (1 on first invocation, incremented each run)
- signals_added: list of strings (signal names newly collected since prior session;
  empty list [] if none added or if session_number = 1)
- signals_removed: list of strings (signals no longer collected; [] if none)
- verdict_before: string, exactly one of:
  CONFIRMED | REFUTED | EVOLVING | INSUFFICIENT | NOT YET REACHED | NONE
  (NONE only when session_number = 1)
- verdict_after: string, exactly one of:
  CONFIRMED | REFUTED | EVOLVING | INSUFFICIENT | NOT YET REACHED
- verdict_changed: string, exactly one of: YES | NO | N/A
  (N/A only when session_number = 1)

---

## Prohibition Parity Rule

Each of the four campaign roles carries exactly 5 forbidden actions -- no more, no
fewer. This count is fixed. A role with 4 or 6 items is structurally invalid and
fails audit. The numbered list format is required: each item labeled 1 through 5.

---

## Roles and Prohibitions

### Registrar (Phase 1 -- topic-new)

Owns strategy.md. Produces Phase 1 Contract output.

Forbidden actions (exactly 5):
1. Must not produce coverage tables, coverage ratios, or readiness verdicts
2. Must not synthesize or interpret signal content across sources
3. Must not assign verdict verbs from Phase 4 controlled vocabulary
4. Must not invoke any sub-skill other than topic-new
5. Must not list signals not declared in the strategy planned_signals field

### Planner (Phase 2 -- topic-plan)

Owns roadmap.md. Produces Phase 2 Contract output.

Forbidden actions (exactly 5):
1. Must not register, rename, or modify the topic identity (Phase 1 domain)
2. Must not query or report which signals are collected (Phase 3 domain)
3. Must not produce readiness verdicts or coverage ratios
4. Must not synthesize findings or assign verdict verbs from Phase 4 vocabulary
5. Must not invoke any sub-skill other than topic-plan

### Analyst (Phase 3 -- topic-status)

Owns status.md. Produces Phase 3 Contract output.

Forbidden actions (exactly 5):
1. Must not add planned signals beyond what Phase 2 roadmap defines
2. Must not produce verdict verbs from Phase 4 vocabulary
3. Must not interpret meaning from signal content or editorialize on findings
4. Must not invoke any sub-skill other than topic-status
5. Must not use narrative counts ("several", "a few", "many") where integers are
   required by contract

### Narrator (Phase 4 -- topic-story)

Owns story.md. Produces Phase 4 Contract output.

Forbidden actions (exactly 5):
1. Must not modify the coverage table or coverage ratio (Phase 3 domain)
2. Must not add, remove, or reorder planned signals (Phase 2 domain)
3. Must not assign readiness verdicts (READY / NOT READY / CONDITIONALLY READY)
4. Must not invoke any sub-skill other than topic-story
5. Must not paraphrase verdict verbs -- only exact Phase 4 Contract tokens are valid;
   "likely confirmed" or "essentially confirmed" both fail

---

## Phase 1 -- Register (Registrar)

*Registrar active. Exactly 5 forbidden actions apply. Phase 1 Contract governs output.*

Invoke topic-new for {{topic}}.

Produce strategy.md conforming to Phase 1 Contract:
- topic_name (string), namespace (one of 9 tokens), priority (one of 3 tokens)
- planned_signals: >= 3 items with signal_name, target_skill, rationale

Phase 1 postcondition: strategy.md present, all Phase 1 Contract fields present and
typed correctly.

GATE: Do not proceed to Phase 2 until Phase 1 postcondition is satisfied.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan (Planner)

*Planner active. Exactly 5 forbidden actions apply. Phase 2 Contract governs output.*

Invoke topic-plan for {{topic}}.

Produce roadmap.md conforming to Phase 2 Contract:
- namespace_coverage entries for all namespaces with planned signals
- Each signal entry: signal_name (matched to strategy.md) + collection_purpose

Phase 2 postcondition: roadmap.md present with at least one namespace entry and
collection_purpose present per signal.

GATE: Do not proceed to Phase 3 until Phase 2 postcondition is satisfied.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status (Analyst)

*Analyst active. Exactly 5 forbidden actions apply. Phase 3 Contract governs output.*

Invoke topic-status for {{topic}}.

Produce status.md conforming to Phase 3 Contract:
- All 9 namespace rows present -- no row skipped
- planned and collected are integers -- narrative counts fail
- missing lists each signal by name -- counts alone fail
- zero_flag = "NO SIGNALS" where planned = 0 AND collected = 0
- coverage_ratio in "X/N" format; readiness_verdict from 3-token set

Phase 3 postcondition: status.md present, 9 rows with integer fields, readiness_verdict
assigned from enumerated set.

GATE: Do not proceed to Phase 4 until Phase 3 postcondition is satisfied.

Write to: simulations/topic/{{topic}}-status-{{date}}.md

---

## Phase 4 -- Narrative (Narrator)

*Narrator active. Exactly 5 forbidden actions apply. Phase 4 Contract governs output.*

Invoke topic-story for {{topic}}.

Produce story.md conforming to Phase 4 Contract:
- verdict_verb: exactly one of the 5 enumerated tokens (no paraphrase)
- hypothesis_mutation: s0 (original) + current (updated or "UNCHANGED")
- echoes: list present, minimum ["NONE"]
- next_signal_recommendations: exactly 3 items with namespace + skill + gap_reason

Phase 4 postcondition: story.md present with verdict_verb from 5-token set, s0
field, echoes list, and 3-item recommendations.

Write to: simulations/topic/{{topic}}-story-{{date}}.md

---

## Session Delta

After Phase 4 completes, produce delta.md conforming to Session Delta Contract.

Locate prior session artifacts -- any {{topic}}-status-*.md or {{topic}}-story-*.md
with an earlier date than {{date}}.

If prior artifacts exist:
  session_number: increment prior delta.md session_number (or 2 if no prior delta.md)
  signals_added: names of signals with collected > 0 now that had collected = 0 before
  signals_removed: names of signals with collected = 0 now that had collected > 0 before
  verdict_before: verdict_verb from most recent prior story.md
  verdict_after: verdict_verb from current story.md
  verdict_changed: "YES" if they differ, "NO" if identical

If no prior artifacts exist:
  session_number: 1
  signals_added: []
  signals_removed: []
  verdict_before: "NONE"
  verdict_after: verdict_verb from current story.md
  verdict_changed: "N/A"

Write to: simulations/topic/{{topic}}-delta-{{date}}.md

---

## Empty-State Handling

### First Invocation (0 signals collected)

All four phases run and produce full artifacts per their typed contracts.

Phase 1 (Registrar): Create strategy.md per Phase 1 Contract. planned_signals must
  list >= 3 entries. This is the founding artifact.

Phase 2 (Planner): Create roadmap.md per Phase 2 Contract. All signals are planned;
  none are collected. roadmap.md documents what will be collected.

Phase 3 (Analyst): All rows have collected = 0 (integer). missing lists all planned
  signals from roadmap.md by signal_name. zero_flag = "NO SIGNALS" for namespaces
  where planned = 0 AND collected = 0. readiness_verdict = "NOT READY".

Phase 4 (Narrator): verdict_verb = "NOT YET REACHED". hypothesis_mutation.current
  = "UNCHANGED". echoes = ["NONE"]. next_signal_recommendations: top 3 signals from
  roadmap.md ordered by planned priority.

Session Delta (first invocation): session_number = 1. signals_added = [].
  signals_removed = []. verdict_before = "NONE". verdict_changed = "N/A".
  All fields conform to Session Delta Contract.

---

## TERMINAL -- Field-Level Completion Checklist

Verify each field below independently before marking the campaign complete. Each item
names a specific artifact field and its constraint. A field that satisfies the
constraint PASSES. A field that fails triggers re-run of the affected step only.
Implicit completion is not acceptable.

### Phase 1 -- strategy.md

[ ] topic_name: string present, non-empty
    FAIL: re-run Phase 1

[ ] namespace: exactly one of {scout|draft|review|flow|trace|prove|listen|program|topic}
    FAIL: re-run Phase 1

[ ] priority: exactly one of {High|Medium|Low}
    FAIL: re-run Phase 1

[ ] planned_signals: count >= 3 (integer count, not estimated)
    FAIL: re-run Phase 1

[ ] planned_signals[*].target_skill: each in namespace/skill format
    FAIL: re-run Phase 1

### Phase 2 -- roadmap.md

[ ] namespace_coverage: at least one entry present
    FAIL: re-run Phase 2

[ ] namespace_coverage[*].collection_purpose: string present per signal (not omitted)
    FAIL: re-run Phase 2

### Phase 3 -- status.md

[ ] row count: exactly 9 namespace rows present
    FAIL: re-run Phase 3

[ ] planned: integer value in all 9 rows (not prose, not a range)
    FAIL: re-run Phase 3

[ ] collected: integer value in all 9 rows (not prose, not a range)
    FAIL: re-run Phase 3

[ ] missing: list of signal names in each row (not a count -- names required)
    FAIL: re-run Phase 3

[ ] zero_flag: "NO SIGNALS" present for every row where planned = 0 AND collected = 0
    FAIL: re-run Phase 3

[ ] coverage_ratio: "X/N" format (X and N are both integers)
    FAIL: re-run Phase 3

[ ] readiness_verdict: exactly one of {READY|NOT READY|CONDITIONALLY READY}
    FAIL: re-run Phase 3

### Phase 4 -- story.md

[ ] verdict_verb: exactly one of
    {CONFIRMED|REFUTED|EVOLVING|INSUFFICIENT|NOT YET REACHED}
    FAIL: re-run Phase 4

[ ] hypothesis_mutation.s0: string present, non-empty
    FAIL: re-run Phase 4

[ ] hypothesis_mutation.current: string present ("UNCHANGED" or updated hypothesis)
    FAIL: re-run Phase 4

[ ] echoes: list present with at least one entry (minimum ["NONE"])
    FAIL: re-run Phase 4

[ ] next_signal_recommendations: exactly 3 items
    FAIL: re-run Phase 4

[ ] next_signal_recommendations[*].namespace: string present for all 3
    FAIL: re-run Phase 4

[ ] next_signal_recommendations[*].gap_reason: string present for all 3
    FAIL: re-run Phase 4

### Session Delta -- delta.md

[ ] session_number: integer >= 1
    FAIL: re-run Session Delta

[ ] signals_added: list present ([] permitted; absent field fails)
    FAIL: re-run Session Delta

[ ] verdict_before: exactly one of
    {CONFIRMED|REFUTED|EVOLVING|INSUFFICIENT|NOT YET REACHED|NONE}
    FAIL: re-run Session Delta

[ ] verdict_after: exactly one of
    {CONFIRMED|REFUTED|EVOLVING|INSUFFICIENT|NOT YET REACHED}
    FAIL: re-run Session Delta

[ ] verdict_changed: exactly one of {YES|NO|N/A}
    FAIL: re-run Session Delta

All 27 items PASS: campaign is complete. Dashboard ready to emit.
Any item FAIL: re-run the affected phase or step. Re-verify the failed item only.

---

## Output: Topic Dashboard

When all 27 TERMINAL items show PASS, emit consolidated dashboard in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Narrative verdict + hypothesis mutation + echoes + top-3 recommendations (Phase 4)
5. Session delta: session_number, signals_added, verdict_before -> verdict_after,
   verdict_changed
```

**Rubric targeting**: C-10: Session Delta Contract typed; signals_added (list) + verdict
change fields (verdict_before/after/verdict_changed) present and typed; first-invocation
case typed (empty lists, NONE sentinel). C-24: Terminal checklist grows from 22 to 27
items with 5 delta fields, each naming a specific field with targeted FAIL action
("re-run Session Delta"); signals_added uses list-type notation; verdict_before/after use
enumerated token sets. C-16: TERMINAL section updated to "All 27 items PASS"; dashboard
emitted only when all 27 pass. All other criteria inherited from R6 V-05.

**Risk**: C-24 specifies "at least one item uses array-field notation (e.g.,
planned_signals[*].target_skill)." The 22 inherited items include `planned_signals[*]`
and `namespace_coverage[*]` -- array notation is present; adding delta fields does not
remove it. The count update from 22 to 27 requires careful consistency: "All 27 items
PASS" must match the actual item count. V-04 carries no prohibition list changes, so
C-22 is not at risk.

---

## V-05 -- Full Stack: Typed delta contract + Analyst-owned + 27-item terminal checklist

**Combined axes**: Format (V-02 typed contract) + Ownership (V-03 Analyst-owned) +
Behavior (V-04 terminal checklist, 27 items)

**Hypothesis**: Combining all three C-10 axes produces a variation where the session
delta is simultaneously owned (Analyst role), typed (Session Delta Contract), gated
(Phase 3 postcondition requires delta.md), and terminally verified (5 delta checklist
items). Each axis defends against a different failure mode:
- Ownership (V-03): a model cannot skip delta because Phase 3 cannot close without it
- Typed contract (V-02): a model cannot produce prose -- fields are mechanically typed
- Terminal checklist (V-04): a model cannot declare completion without 27 PASS verdicts

Active-role annotation at Phase 3 now references BOTH the Phase 3 Contract AND the
Session Delta Contract at point of execution. This is the R7 analogue of R6 V-05's
active-role annotation pattern -- all constraints restated at the execution site.

```
Run the full topic narrative campaign for: {{topic}}

Produce a complete topic dashboard showing what signals exist, what is missing, and
the narrative arc. Use at the start and end of a signal-gathering session.

This campaign runs in exactly four phases: Register -> Plan -> Status -> Narrative.
Each phase produces a distinct artifact. Do not proceed to the next phase until the
current phase artifact is written and satisfies its typed output contract.

---

## Full-Phase Type Coverage Rule

All four campaign phases have typed output contracts. No phase is exempt. Partial
coverage of the four phases fails. Each field typed as integer must contain an
integer. Each field typed as enumerated string must contain exactly one of the listed
tokens.

The Session Delta contract is supplemental -- it applies after Phase 3 (Analyst-owned)
and does not affect the four-phase coverage rule.

---

## Typed Output Contracts

### Phase 1 Contract -- strategy.md

- topic_name: string (non-empty, human-readable)
- namespace: string, exactly one of:
  scout | draft | review | flow | trace | prove | listen | program | topic
- priority: string, exactly one of: High | Medium | Low
- planned_signals: list of >= 3 items; each item:
  - signal_name: string (unique within strategy)
  - target_skill: string (namespace/skill format, e.g. "scout/scout-competitors")
  - rationale: string (one sentence max)

### Phase 2 Contract -- roadmap.md

- namespace_coverage: list of namespace entries; each entry:
  - namespace: string (one of 9 Signal namespaces)
  - signals: list; each item:
    - signal_name: string (matches signal_name from strategy.md)
    - collection_purpose: string (one sentence: why this signal matters)

### Phase 3 Contract -- status.md

Coverage table -- all 9 namespace rows required; each row:
  - namespace: string
  - planned: integer >= 0 (no prose, no ranges)
  - collected: integer >= 0 (no prose, no ranges)
  - missing: list of strings (signal names; empty list [] if none missing)
  - zero_flag: "NO SIGNALS" if planned = 0 AND collected = 0; omit otherwise

Summary fields:
  - coverage_ratio: string, format "X/N" (X and N are integers)
  - readiness_verdict: string, exactly one of: READY | NOT READY | CONDITIONALLY READY

### Phase 4 Contract -- story.md

- verdict_verb: string, exactly one of:
  CONFIRMED | REFUTED | EVOLVING | INSUFFICIENT | NOT YET REACHED
- hypothesis_mutation:
  - s0: string (original hypothesis text at topic registration)
  - current: string (updated hypothesis, or literal "UNCHANGED")
- echoes: list of strings; if none, value must be ["NONE"]
- next_signal_recommendations: list of exactly 3 items; each item:
  - namespace: string
  - skill: string
  - gap_reason: string (one sentence)

### Session Delta Contract -- delta.md (Analyst-owned, Phase 3 Step B)

- session_number: integer >= 1 (1 on first invocation, incremented each run)
- signals_added: list of strings (signal names newly collected since prior session;
  empty list [] if none added or if session_number = 1)
- signals_removed: list of strings (signals no longer collected; [] if none)
- verdict_before: string, exactly one of:
  CONFIRMED | REFUTED | EVOLVING | INSUFFICIENT | NOT YET REACHED | NONE
  (NONE only when session_number = 1)
- verdict_after: string, exactly one of:
  CONFIRMED | REFUTED | EVOLVING | INSUFFICIENT | NOT YET REACHED
- verdict_changed: string, exactly one of: YES | NO | N/A
  (N/A only when session_number = 1)

---

## Prohibition Parity Rule

Each of the four campaign roles carries exactly 5 forbidden actions -- no more, no
fewer. This count is fixed. A role with 4 or 6 items is structurally invalid and
fails audit. The numbered list format is required: each item labeled 1 through 5.

---

## Roles and Prohibitions

### Registrar (Phase 1 -- topic-new)

Owns strategy.md. Produces Phase 1 Contract output.

Forbidden actions (exactly 5):
1. Must not produce coverage tables, coverage ratios, or readiness verdicts
2. Must not synthesize or interpret signal content across sources
3. Must not assign verdict verbs from Phase 4 controlled vocabulary
4. Must not invoke any sub-skill other than topic-new
5. Must not list signals not declared in the strategy planned_signals field

### Planner (Phase 2 -- topic-plan)

Owns roadmap.md. Produces Phase 2 Contract output.

Forbidden actions (exactly 5):
1. Must not register, rename, or modify the topic identity (Phase 1 domain)
2. Must not query or report which signals are collected (Phase 3 domain)
3. Must not produce readiness verdicts or coverage ratios
4. Must not synthesize findings or assign verdict verbs from Phase 4 vocabulary
5. Must not invoke any sub-skill other than topic-plan

### Analyst (Phase 3 -- topic-status + session delta)

Owns status.md AND delta.md. Produces Phase 3 Contract output and Session Delta
Contract output. The Analyst is the only role with direct access to coverage counts
across sessions -- delta computation belongs here, not at narrative phase.

Forbidden actions (exactly 5):
1. Must not add planned signals beyond what Phase 2 roadmap defines
2. Must not produce verdict verbs from Phase 4 vocabulary
3. Must not interpret meaning from signal content or editorialize on findings
4. Must not invoke any sub-skill other than topic-status
5. Must not use narrative counts ("several", "a few", "many") where integers are
   required by Phase 3 Contract or Session Delta Contract

### Narrator (Phase 4 -- topic-story)

Owns story.md. Produces Phase 4 Contract output.

Forbidden actions (exactly 5):
1. Must not modify the coverage table or coverage ratio (Phase 3 domain)
2. Must not add, remove, or reorder planned signals (Phase 2 domain)
3. Must not assign readiness verdicts (READY / NOT READY / CONDITIONALLY READY)
4. Must not invoke any sub-skill other than topic-story
5. Must not paraphrase verdict verbs -- only exact Phase 4 Contract tokens are valid;
   "likely confirmed" or "essentially confirmed" both fail

---

## Phase 1 -- Register (Registrar)

*Registrar active. Exactly 5 forbidden actions apply. Phase 1 Contract governs output.*

Invoke topic-new for {{topic}}.

Produce strategy.md conforming to Phase 1 Contract:
- topic_name (string), namespace (one of 9 tokens), priority (one of 3 tokens)
- planned_signals: >= 3 items with signal_name, target_skill, rationale

Phase 1 postcondition: strategy.md present, all Phase 1 Contract fields present and
typed correctly.

GATE: Do not proceed to Phase 2 until Phase 1 postcondition is satisfied.

Write to: simulations/topic/{{topic}}-strategy-{{date}}.md

---

## Phase 2 -- Plan (Planner)

*Planner active. Exactly 5 forbidden actions apply. Phase 2 Contract governs output.*

Invoke topic-plan for {{topic}}.

Produce roadmap.md conforming to Phase 2 Contract:
- namespace_coverage entries for all namespaces with planned signals
- Each signal entry: signal_name (matched to strategy.md) + collection_purpose

Phase 2 postcondition: roadmap.md present with at least one namespace entry and
collection_purpose present per signal.

GATE: Do not proceed to Phase 3 until Phase 2 postcondition is satisfied.

Write to: simulations/topic/{{topic}}-roadmap-{{date}}.md

---

## Phase 3 -- Status + Session Delta (Analyst)

*Analyst active. Exactly 5 forbidden actions apply.*
*Phase 3 Contract governs status.md. Session Delta Contract governs delta.md.*

### Step A -- Status

Invoke topic-status for {{topic}}.

Produce status.md conforming to Phase 3 Contract:
- All 9 namespace rows present -- no row skipped
- planned and collected are integers -- narrative counts fail
- missing lists each signal by name -- counts alone fail
- zero_flag = "NO SIGNALS" where planned = 0 AND collected = 0
- coverage_ratio in "X/N" format; readiness_verdict from 3-token set

### Step B -- Session Delta

After status.md is written, compute delta.md conforming to Session Delta Contract.

Locate prior session artifacts -- any {{topic}}-status-*.md or {{topic}}-story-*.md
with an earlier date than {{date}}.

If prior artifacts exist:
  session_number: increment prior delta.md session_number (or 2 if no prior delta.md)
  signals_added: signal names with collected > 0 now that had collected = 0 before
  signals_removed: signal names with collected = 0 now that had collected > 0 before
  verdict_before: verdict_verb from most recent prior story.md
  verdict_after: verdict_verb from current story.md (Phase 4 not yet run; use
    readiness trend: if readiness_verdict = "READY" and prior verdict was NOT YET
    REACHED, set verdict_after to "EVOLVING" -- update after Phase 4 completes)
  verdict_changed: "YES" if they differ, "NO" if identical

If no prior artifacts exist:
  session_number: 1
  signals_added: []
  signals_removed: []
  verdict_before: "NONE"
  verdict_after: "NOT YET REACHED" (update after Phase 4 with actual verdict_verb)
  verdict_changed: "N/A"

Phase 3 postcondition: status.md AND delta.md both present. status.md: 9 rows with
integer fields, readiness_verdict from enumerated set. delta.md: all Session Delta
Contract fields present and typed correctly.

GATE: Do not proceed to Phase 4 until Phase 3 postcondition is satisfied.

Write status to: simulations/topic/{{topic}}-status-{{date}}.md
Write delta to:  simulations/topic/{{topic}}-delta-{{date}}.md

After Phase 4 completes: update delta.md verdict_after with actual verdict_verb from
story.md. Update verdict_changed accordingly.

---

## Phase 4 -- Narrative (Narrator)

*Narrator active. Exactly 5 forbidden actions apply. Phase 4 Contract governs output.*

Invoke topic-story for {{topic}}.

Produce story.md conforming to Phase 4 Contract:
- verdict_verb: exactly one of the 5 enumerated tokens (no paraphrase)
- hypothesis_mutation: s0 (original) + current (updated or "UNCHANGED")
- echoes: list present, minimum ["NONE"]
- next_signal_recommendations: exactly 3 items with namespace + skill + gap_reason

Phase 4 postcondition: story.md present with verdict_verb from 5-token set, s0
field, echoes list, and 3-item recommendations.

Write to: simulations/topic/{{topic}}-story-{{date}}.md

Update delta.md: set verdict_after = verdict_verb from story.md. Set verdict_changed
= "YES" if verdict_after != verdict_before, else "NO" (keep "N/A" if session_number = 1).

---

## Empty-State Handling

### First Invocation (0 signals collected)

All four phases run and produce full artifacts per their typed contracts.

Phase 1 (Registrar): Create strategy.md per Phase 1 Contract. planned_signals must
  list >= 3 entries. This is the founding artifact.

Phase 2 (Planner): Create roadmap.md per Phase 2 Contract. All signals are planned;
  none are collected. roadmap.md documents what will be collected.

Phase 3 (Analyst):
  Step A: All rows have collected = 0 (integer). missing lists all planned signals from
  roadmap.md by signal_name. zero_flag = "NO SIGNALS" for namespaces where planned = 0
  AND collected = 0. readiness_verdict = "NOT READY".
  Step B: session_number = 1. signals_added = []. signals_removed = [].
  verdict_before = "NONE". verdict_after = placeholder; updated after Phase 4.
  verdict_changed = "N/A".

Phase 4 (Narrator): verdict_verb = "NOT YET REACHED". hypothesis_mutation.current
  = "UNCHANGED". echoes = ["NONE"]. next_signal_recommendations: top 3 signals from
  roadmap.md ordered by planned priority.

Delta update: verdict_after = "NOT YET REACHED". verdict_changed = "N/A".

---

## TERMINAL -- Field-Level Completion Checklist

Verify each field below independently before marking the campaign complete. Each item
names a specific artifact field and its constraint. A field that satisfies the
constraint PASSES. A field that fails triggers re-run of the affected phase or step.
All 27 items must PASS before the dashboard is emitted.

### Phase 1 -- strategy.md

[ ] topic_name: string present, non-empty
    FAIL: re-run Phase 1

[ ] namespace: exactly one of {scout|draft|review|flow|trace|prove|listen|program|topic}
    FAIL: re-run Phase 1

[ ] priority: exactly one of {High|Medium|Low}
    FAIL: re-run Phase 1

[ ] planned_signals: count >= 3 (integer count, not estimated)
    FAIL: re-run Phase 1

[ ] planned_signals[*].target_skill: each in namespace/skill format
    FAIL: re-run Phase 1

### Phase 2 -- roadmap.md

[ ] namespace_coverage: at least one entry present
    FAIL: re-run Phase 2

[ ] namespace_coverage[*].collection_purpose: string present per signal (not omitted)
    FAIL: re-run Phase 2

### Phase 3 -- status.md

[ ] row count: exactly 9 namespace rows present
    FAIL: re-run Phase 3 Step A

[ ] planned: integer value in all 9 rows (not prose, not a range)
    FAIL: re-run Phase 3 Step A

[ ] collected: integer value in all 9 rows (not prose, not a range)
    FAIL: re-run Phase 3 Step A

[ ] missing: list of signal names in each row (not a count -- names required)
    FAIL: re-run Phase 3 Step A

[ ] zero_flag: "NO SIGNALS" present for every row where planned = 0 AND collected = 0
    FAIL: re-run Phase 3 Step A

[ ] coverage_ratio: "X/N" format (X and N are both integers)
    FAIL: re-run Phase 3 Step A

[ ] readiness_verdict: exactly one of {READY|NOT READY|CONDITIONALLY READY}
    FAIL: re-run Phase 3 Step A

### Phase 4 -- story.md

[ ] verdict_verb: exactly one of
    {CONFIRMED|REFUTED|EVOLVING|INSUFFICIENT|NOT YET REACHED}
    FAIL: re-run Phase 4

[ ] hypothesis_mutation.s0: string present, non-empty
    FAIL: re-run Phase 4

[ ] hypothesis_mutation.current: string present ("UNCHANGED" or updated hypothesis)
    FAIL: re-run Phase 4

[ ] echoes: list present with at least one entry (minimum ["NONE"])
    FAIL: re-run Phase 4

[ ] next_signal_recommendations: exactly 3 items
    FAIL: re-run Phase 4

[ ] next_signal_recommendations[*].namespace: string present for all 3
    FAIL: re-run Phase 4

[ ] next_signal_recommendations[*].gap_reason: string present for all 3
    FAIL: re-run Phase 4

### Session Delta -- delta.md

[ ] session_number: integer >= 1
    FAIL: re-run Phase 3 Step B

[ ] signals_added: list present ([] permitted; absent field or string "NONE" fails)
    FAIL: re-run Phase 3 Step B

[ ] verdict_before: exactly one of
    {CONFIRMED|REFUTED|EVOLVING|INSUFFICIENT|NOT YET REACHED|NONE}
    FAIL: re-run Phase 3 Step B

[ ] verdict_after: exactly one of
    {CONFIRMED|REFUTED|EVOLVING|INSUFFICIENT|NOT YET REACHED}
    (must reflect Phase 4 verdict_verb; placeholder fails)
    FAIL: re-run Phase 3 Step B after Phase 4 completes

[ ] verdict_changed: exactly one of {YES|NO|N/A}
    FAIL: re-run Phase 3 Step B

All 27 items PASS: campaign is complete. Dashboard ready to emit.
Any item FAIL: re-run the affected phase or step only. Re-verify the failed item only.

---

## Output: Topic Dashboard

When all 27 TERMINAL items show PASS, emit consolidated dashboard in order:
1. Topic registration summary (Phase 1)
2. Signal roadmap summary (Phase 2)
3. Coverage table with readiness verdict (Phase 3)
4. Narrative verdict + hypothesis mutation + echoes + top-3 recommendations (Phase 4)
5. Session delta: session_number, signals_added (count + names), verdict_before ->
   verdict_after, verdict_changed
```

**Rubric targeting**: C-10: Session Delta Contract fully typed; Analyst owns delta.md as
Phase 3 Step B artifact; signals_added (list of strings) + verdict change summary
(verdict_before/after/verdict_changed) present and typed; first-invocation behavior per
typed contract (empty lists, NONE sentinel, N/A token); delta.md updated post-Phase 4
with actual verdict_verb. C-22: Parity rule unchanged; Analyst prohibition 5 updated to
extend "narrative counts" to both Phase 3 Contract and Session Delta Contract -- count
preserved at exactly 5. C-23: Full-Phase Type Coverage Rule scopes to four campaign
phases; delta contract explicitly labeled "supplemental." C-24: Terminal checklist
grows to 27 items; 5 delta fields added with field-level constraints and targeted FAIL
actions referencing "Phase 3 Step B"; signals_added item notes "absent field or string
'NONE' fails" -- tighter than V-04. Item count stated twice ("All 27 items" in section
header and at checklist end). C-12: Phase 3 gate references two artifacts in
postcondition (status.md AND delta.md), making gating tighter than V-03. All other
criteria inherited from R6 V-05.

**Risk**: The delta update loop (delta.md written in Phase 3, then updated in Phase 4
after verdict_verb is known) introduces a two-pass write that some models may skip --
producing a delta.md with a placeholder verdict_after. The terminal checklist item
explicitly flags this: "must reflect Phase 4 verdict_verb; placeholder fails." The FAIL
action for verdict_after is "re-run Phase 3 Step B after Phase 4 completes" -- the
only checklist item whose FAIL action is order-dependent. This is a structural
complexity that V-04 avoids by not assigning Analyst ownership, but the ownership
benefit (Phase 3 gate cannot close without delta.md) outweighs the placeholder risk.

---

## Variation Summary

| ID  | Primary Axes                          | C-10 Design          | Checklist | Score Prediction |
|-----|---------------------------------------|----------------------|-----------|-----------------|
| V-01 | Delta placement (post-Phase 4)       | Prose section        | 22 items  | 98/98           |
| V-02 | Delta typed contract                  | Typed contract       | 22 items  | 98/98           |
| V-03 | Delta Analyst-owned                   | Role-owned narrative | 22 items  | 98/98           |
| V-04 | Typed contract + checklist            | Typed + gated        | 27 items  | 98/98           |
| V-05 | Typed + Analyst-owned + checklist     | Typed + owned + gated| 27 items  | 98/98           |

All five variations should score 98/98 -- C-10 is the only unaddressed criterion and
all five satisfy the C-10 criterion definition ("session delta section: signals added,
verdict change summary"). The differentiator is not binary pass/fail but **structural
quality** of the C-10 implementation:

- V-01: prose delta, no gate, no typed fields -- passes C-10 minimally
- V-02: typed delta contract, no gate -- passes C-10 with type safety
- V-03: owned by Analyst, gated at Phase 3 postcondition -- passes C-10 with enforcement
- V-04: typed + terminally gated (27-item checklist) -- mechanically auditable
- V-05: typed + owned + terminally gated -- maximum verifiability at all three layers

**Predicted leaderboard going into quest-score**: V-05 > V-04 > V-03 > V-02 > V-01

If scoring distinguishes structural quality within C-10 (per-field evidence in
criterion evaluation), V-05 and V-04 separate from V-01 through V-03. If scoring
is binary (section present or absent), all five tie at 98/98.

**Open question for scoring**: Does C-10 require typed fields, role ownership, or
terminal verification -- or only presence of signals-added and verdict-change content?
The criterion definition is minimal ("session delta section: signals added, verdict
change summary"). V-01 satisfies this with two prose bullets. The quest-score run
will resolve whether V-01's minimal approach passes or whether structural quality
matters for partial credit within the aspirational tier.

```json
{"top_predicted": 98, "all_essential_pass": true, "target_criterion": "C-10",
 "new_patterns": [
   "typed Session Delta Contract as supplemental artifact with same field-type discipline as phase contracts",
   "Analyst ownership of delta.md -- Phase 3 postcondition requires two artifacts (status.md AND delta.md), making delta non-optional via progression gate",
   "delta fields in terminal checklist -- 5 new field-level items bring total to 27; verdict_after item explicitly flags placeholder-fails condition",
   "two-pass delta update -- delta.md written in Phase 3 Step B then updated after Phase 4 with actual verdict_verb; terminal checklist item enforces the update"
 ]}
```
