## topic-retro — Round 14 Variations (V-01 through V-05)

---

## V-01 — Output Format: Full Tabular Structure

**Axis**: Output format (table-first across all three phases)
**Hypothesis**: Forcing accuracy, gaps, and echo into named-column tables with explicit column contracts satisfies C-11 (named structural field for Echo), C-33 (mechanism-keyed tabular form), C-34 (cross-reference contract mechanism), and C-35 (one row per SEAL field) more reliably than prose-embedded structure.

---

```
You are running /topic-retro for topic: {{TOPIC}}.

Commitment: {{COMMITMENT_DESCRIPTION}}
Commitment date: {{COMMITMENT_DATE}}
AMEND: {{AMEND_SCOPE | "none"}}

---

## PRE-EXECUTION CONTRACT

Before writing any section, declare:

1. TOPIC: {{TOPIC}}
2. COMMITMENT NATURE: What was decided and on what date
3. SIGNAL WINDOW: The date range of signals reviewed
4. AMEND SCOPE: If set, which namespaces and/or signal types are in scope;
   all others are OUT-OF-SCOPE and must be marked as such in every table.

---

## SECTION 1 — Signal Coverage Summary

Produce a coverage table across all 9 namespaces. One row per namespace.
AMEND: mark excluded namespaces OUT-OF-SCOPE in the Status column.

| Namespace | Signals Gathered | Signals Absent | Status |
|-----------|-----------------|----------------|--------|
| scout      | ...             | ...            | IN / OUT-OF-SCOPE |
| draft      | ...             | ...            | IN / OUT-OF-SCOPE |
| review     | ...             | ...            | IN / OUT-OF-SCOPE |
| flow       | ...             | ...            | IN / OUT-OF-SCOPE |
| trace      | ...             | ...            | IN / OUT-OF-SCOPE |
| prove      | ...             | ...            | IN / OUT-OF-SCOPE |
| listen     | ...             | ...            | IN / OUT-OF-SCOPE |
| program    | ...             | ...            | IN / OUT-OF-SCOPE |
| topic      | ...             | ...            | IN / OUT-OF-SCOPE |

---

## SECTION 2 — Signal Accuracy Table

One row per signal gathered. Columns:

| Signal | Namespace | Prediction (pre-commit) | Actual (post-ship) | Verdict | Notes |
|--------|-----------|------------------------|--------------------|---------|-------|

Verdict values: CORRECT / WRONG / PARTIAL / NOT-VERIFIED

After the table, state the accuracy ratio: N_CORRECT / N_TOTAL = X%.

For every WRONG or PARTIAL verdict: write a one-paragraph explanation
immediately below the table under the heading "Failed Prediction Explanations".
Format each as:
  **[Signal name]**: What was predicted. What actually happened. Why the signal
  misled or was misread.

---

## SECTION 3 — Gap Analysis Table

Gaps are signals NOT gathered that, if present, would have changed the
commitment decision or its scope.

One row per gap identified.

| Gap Signal | Namespace | What It Would Have Revealed | Decision Impact |
|------------|-----------|----------------------------|-----------------|

Decision Impact values: REVERSAL / SCOPE-CHANGE / TIMING-CHANGE / CONFIDENCE-ONLY

After the table, write one sentence per gap explaining the specific practice
change that would cause this signal to be gathered in a future topic cycle.
Label each: "Improvement for [Gap Signal]: ..."

---

## SECTION 4 — Echo Table

The Echo is the ONE unexpected finding — something not predicted by any signal
and not a gap (it wasn't absent, it was genuinely unforeseeable from the
signals that existed).

If no genuine Echo exists, write: "ECHO: NONE — all findings traceable to
signals or known gaps."

| Field | Value |
|-------|-------|
| Echo Name | A short label for the unexpected finding |
| Description | What happened that no signal predicted |
| Discovery Point | When in the post-ship period this was discovered |
| Systemic Pattern | The broader recurring failure mode this instance represents |
| Cross-reference | Which PRE-EXECUTION CONTRACT item (if any) this challenges |

Rule: A wrong prediction restated as the Echo is disqualified. Wrong
predictions belong in Section 2.

---

## SECTION 5 — Design Guarantees Table

For each Phase 8 SEAL field, one row. Do not collapse SEAL fields into groups.

| SEAL Field | Mechanism | Guarantee | Verification Instructions | Cross-reference |
|------------|-----------|-----------|--------------------------|-----------------|

Cross-reference column: name the PRE-EXECUTION CONTRACT mechanism that
produces this guarantee. Format: "Cross-reference: PRE-EXECUTION CONTRACT
[mechanism name]".

Verification Instructions: independent check that does not rely on the
mechanism itself.

---

## SECTION 6 — Improvement Recommendation

State exactly one primary recommendation. It must:
- Name either a specific gap from Section 3 or the Echo from Section 4
- Specify the practice change (what signal, when in the topic lifecycle,
  who gathers it)
- Be actionable in the next topic cycle

Format:
**Recommendation**: [Practice change]
**Addresses**: [Gap: signal name] OR [Echo: echo name]
**Next cycle trigger**: [When/how this change activates]

---

## OUTPUT FILE

Write artifact to: simulations/topic/{{TOPIC}}-retro-{{DATE}}.md

Include the PRE-EXECUTION CONTRACT block at the top of the artifact.
```

---

## V-02 — Role Sequence: Echo-Anchored Retrospective

**Axis**: Role sequence (Echo surfaces first, accuracy re-read through Echo's lens)
**Hypothesis**: Discovering the Echo before scoring predictions forces the analyst to re-examine whether the unexpected finding was already visible in the signal record, yielding richer systemic pattern connections (C-09) and preventing wrong predictions from being misclassified as Echoes (C-12).

---

```
You are running /topic-retro for topic: {{TOPIC}}.

Commitment: {{COMMITMENT_DESCRIPTION}}
Commitment date: {{COMMITMENT_DATE}}
AMEND: {{AMEND_SCOPE | "none"}}

---

## PRE-EXECUTION CONTRACT

Declare at the top of your response:
- TOPIC: {{TOPIC}}
- COMMITMENT NATURE: What was decided, what date
- SIGNAL WINDOW: Date range reviewed
- AMEND SCOPE: Namespaces in scope (mark all others OUT-OF-SCOPE per table)

---

## PHASE 1 — ECHO DISCOVERY (run this first)

Before scoring any prediction, find the Echo.

The Echo is the one thing you learned post-ship that no signal predicted AND
that was not merely an absent signal. It is genuinely unexpected — something
the full signal record, even if complete, would not have foreshadowed.

Write the Echo now:
  Echo Name: [short label]
  Description: [what happened]
  Why it wasn't foreseeable: [which signals were present and why none pointed here]

Hold this. You will use it in Phase 3.

If no Echo exists, declare: ECHO: NONE. Continue to Phase 2.

---

## PHASE 2 — ACCURACY SCORING (read through the Echo's lens)

Now score each signal gathered. The Echo you just found informs your reading:
if a signal touched the Echo domain, was there a subtle signal that could have
been interpreted differently in hindsight?

| Signal | Namespace | Prediction | Actual | Verdict | Echo-Adjacent? |
|--------|-----------|-----------|--------|---------|---------------|

Echo-Adjacent: YES if this signal could have pointed toward the Echo with
different interpretation; NO otherwise.

Accuracy ratio: N_CORRECT / N_TOTAL = X%

For every WRONG or PARTIAL: write one paragraph explaining the failure.
Check: Is this actually the Echo restated? If so, remove it from WRONG and
move it to NONE (the Echo already covers it).

---

## PHASE 3 — ECHO STRUCTURAL ANALYSIS

Return to the Echo from Phase 1. Now that you have scored all predictions:

1. Confirm the Echo is not a restatement of any WRONG prediction.
   (If it is, the Echo is not genuine — revise to ECHO: NONE.)

2. Name the systemic pattern:
   | Field | Value |
   |-------|-------|
   | Echo Name | (from Phase 1) |
   | Description | (from Phase 1) |
   | Systemic Pattern | The class of failure this represents across topics |
   | Signal Family | Which namespace family is structurally blind to this |
   | Pattern Frequency | Isolated instance / Recurring / Structural |

3. If Echo-Adjacent signals exist (from Phase 2): explain what signal
   redesign would make this pattern visible pre-commitment.

---

## PHASE 4 — GAP ANALYSIS

Gaps are signals not gathered. Identify gaps that would have changed the
decision. Do not include the Echo domain here unless a specific signal type
would have caught it.

| Gap Signal | Namespace | Would Have Revealed | Decision Impact |
|------------|-----------|-------------------|-----------------|

Decision Impact: REVERSAL / SCOPE-CHANGE / TIMING-CHANGE / CONFIDENCE-ONLY

Per gap, one improvement sentence:
"Improvement for [gap]: [practice change for next topic cycle]"

---

## PHASE 5 — COVERAGE SUMMARY

| Namespace | Gathered | Absent | Status |
|-----------|---------|--------|--------|
(9 rows, one per namespace; AMEND: mark excluded namespaces OUT-OF-SCOPE)

---

## PHASE 6 — IMPROVEMENT RECOMMENDATION

One recommendation. It must address either the Echo systemic pattern
(from Phase 3) or a specific gap (from Phase 4).

**Recommendation**: [Practice change]
**Addresses**: [Echo: name] OR [Gap: name]
**Next cycle trigger**: [Activation condition]

---

## THREE-WAY ISOLATION CHECK

Before writing the output file, verify:
- [ ] All WRONG predictions are in Phase 2 only
- [ ] All gaps are in Phase 4 only
- [ ] The Echo is in Phase 3 only, not restated elsewhere
- [ ] No wrong prediction appears as the Echo

If any check fails, revise before writing.

---

## OUTPUT FILE

Write artifact to: simulations/topic/{{TOPIC}}-retro-{{DATE}}.md

Phase order in artifact: PRE-EXECUTION CONTRACT → Phase 1 → Phase 2 →
Phase 3 → Phase 4 → Phase 5 → Phase 6.
```

---

## V-03 — Phrasing Register: Conversational/Descriptive

**Axis**: Phrasing register (past-tense descriptive, "you learned" framing vs imperative commands)
**Hypothesis**: Descriptive framing ("what you predicted", "what actually happened", "what surprised you") reduces mechanical table-filling behavior and encourages genuine analytical depth in gap explanations and Echo systemic pattern writing (C-07, C-09).

---

```
You are writing a post-commitment retrospective for topic: {{TOPIC}}.

This retrospective looks back at the signal-gathering period before the
commitment, compares what the signals predicted to what actually happened
after the feature shipped, and surfaces the one thing nobody saw coming.

Commitment: {{COMMITMENT_DESCRIPTION}}
Committed on: {{COMMITMENT_DATE}}
AMEND: {{AMEND_SCOPE | "none — all 9 namespaces in scope"}}

---

## What You're Writing

A topic-retro artifact has four movements:

1. **What the signals said you'd find** — your pre-commitment predictions
2. **What you actually found** — post-ship reality vs. those predictions
3. **What you wish you'd looked for** — signals that would have changed something
4. **What surprised everyone** — the one thing no signal pointed toward

The goal is not a scorecard. It's a learning document. The accuracy numbers
help you see where the signal system is working; the gaps and Echo help you
see where it isn't.

---

## Opening: Set the Scene

Start by grounding the reader:
- What is {{TOPIC}}?
- What decision was made, and when?
- Which signals were gathered in the pre-commitment window?
- If AMEND scope is set, note which namespaces this retrospective covers and
  which fall outside its window.

---

## Movement 1 — Signal Coverage

Walk through all 9 namespaces (or in-scope namespaces if AMEND applies).
For each, note whether signals were gathered or absent. A simple table works:

| Namespace | Gathered | Absent | In Scope? |
|-----------|---------|--------|-----------|

Mark any namespace excluded by AMEND as OUT-OF-SCOPE.

---

## Movement 2 — Accuracy: What the Signals Said vs. What Happened

For each signal that was gathered, describe what it predicted before
the commitment, and what actually happened after the feature shipped.

A table with Prediction / Actual / Verdict (CORRECT / WRONG / PARTIAL) works well.
After the table, state the accuracy ratio — something like "7 of 10 signals
were correct (70%)."

For every wrong or partial call: take a paragraph to explain the failure.
Not to assign blame — to understand whether the signal was gathered wrong,
interpreted wrong, or was genuinely ambiguous. Be specific. A vague
"the prediction was off" doesn't help future signal-gathering.

---

## Movement 3 — Gaps: What You Wish You'd Asked

A gap is a signal you didn't gather that, if present, would have changed
something — the decision itself, its scope, its timing, or just the
confidence you carried into it.

For each gap you identify:
- Name the signal and its namespace
- Describe what it would have revealed
- Say what kind of impact it would have had (would it have reversed the
  decision? changed the scope? only added confidence?)

After listing the gaps, suggest what practice change would make each one
routine in future topic cycles. Be concrete — name when in the topic
lifecycle it would be gathered and what triggers it.

---

## Movement 4 — Echo: The One Unexpected Thing

The Echo is different from a wrong prediction and different from a gap.

A wrong prediction means a signal pointed somewhere and reality went elsewhere.
A gap means you didn't look somewhere you should have.
The Echo means something happened that the full signal record — even if
perfect — wouldn't have foreshadowed. It was genuinely outside the
system's field of view.

To find it: look at what happened post-ship that surprised the team, then
ask whether any signal, even in retrospect, touched this territory.
If no signal did, you've found your Echo.

Name it. Describe what happened. Explain why no signal pointed here.
Then name the systemic pattern it belongs to — the class of thing this
signal system is structurally unable to see. This is the most valuable
part of the retrospective.

If nothing genuinely qualifies, write: Echo: None — all post-ship findings
trace back to known signals or identified gaps.

Note: A wrong prediction restated as the Echo doesn't count. If it appeared
in the accuracy table as WRONG, it belongs there, not here.

---

## Closing: One Recommendation

End with a single actionable recommendation. It should address either the
Echo (what practice change would make this class of surprise visible?) or
the most impactful gap (what would you add to the signal routine?).

Name the specific gap or Echo it addresses. Name the practice change.
Say when it would activate in the next topic cycle.

---

## Output File

Write this retrospective to:
simulations/topic/{{TOPIC}}-retro-{{DATE}}.md

Structure the artifact in the order of the four movements above, with
the Opening at the top and the Recommendation at the bottom.
AMEND scope (if set) should appear in the Opening section.
```

---

## V-04 — Lifecycle Emphasis + Inertia Framing

**Axes**: Lifecycle emphasis (explicit phase entry/exit boundaries) + Inertia framing (the default path named and confronted)
**Hypothesis**: Naming the "inertia competitor" — what the team would have done with no signals — and marking explicit phase entry/exit conditions forces more honest assessment of whether signals actually displaced prior assumptions (C-07 improvement recommendations) vs. merely confirmed them.

---

```
You are running /topic-retro for topic: {{TOPIC}}.

Commitment: {{COMMITMENT_DESCRIPTION}}
Commitment date: {{COMMITMENT_DATE}}
AMEND: {{AMEND_SCOPE | "none"}}

---

## PRE-EXECUTION CONTRACT

Declare before any output:

| Field | Value |
|-------|-------|
| Topic | {{TOPIC}} |
| Commitment | {{COMMITMENT_DESCRIPTION}} |
| Commitment Date | {{COMMITMENT_DATE}} |
| Signal Window | Start date → Commitment date |
| AMEND Scope | Namespaces in scope / "all 9" |
| Inertia Path | What the team would have done WITHOUT any signal gathering |

The Inertia Path is required. It names the default decision — the thing
momentum and prior assumptions would have produced. Every signal in this
retrospective is evaluated against whether it shifted the team away from
that path.

AMEND: All namespaces not listed in AMEND Scope are OUT-OF-SCOPE. Mark
them explicitly in every table that covers namespace dimension.

---

## PHASE BOUNDARY PROTOCOL

Each phase below has entry conditions and exit conditions.
Do not proceed to the next phase until the current phase's exit conditions
are satisfied.

---

## PHASE 1: CONTEXT ESTABLISHMENT
Entry: PRE-EXECUTION CONTRACT complete.
Exit: Inertia Path documented, topic and commitment clear, signal window set.

Write a brief narrative (3-5 sentences) covering:
- What {{TOPIC}} is and why it was pursued
- What the commitment consisted of
- What the inertia path was (the default the team would have followed without signals)
- Whether any signals ultimately displaced the inertia path or confirmed it

This is not a summary of findings — it is context for why the signals matter.

---

## PHASE 2: SIGNAL COVERAGE MAP
Entry: Phase 1 complete.
Exit: All 9 namespaces accounted for with gathered/absent status.

| Namespace | Signals Gathered | Signals Absent | Displaced Inertia? | Status |
|-----------|-----------------|----------------|-------------------|--------|

Displaced Inertia: YES if this signal caused a change from the Inertia Path;
NO if it confirmed it; N/A if absent.
Status: IN-SCOPE / OUT-OF-SCOPE (AMEND)

---

## PHASE 3: ACCURACY SCORING
Entry: Phase 2 coverage table complete.
Exit: Every gathered signal scored; accuracy ratio stated; all WRONG/PARTIAL verdicts explained.

For each signal gathered, score the pre-commitment prediction against post-ship actuality.

| Signal | Namespace | Prediction | Actual | Verdict | Displaced Inertia? |
|--------|-----------|-----------|--------|---------|-------------------|

Verdict: CORRECT / WRONG / PARTIAL / NOT-VERIFIED
Displaced Inertia: carry forward from Phase 2.

**Accuracy ratio**: N_CORRECT / N_TOTAL = X%

**Inertia displacement rate**: N_signals that displaced inertia / N_total signals gathered = X%

Failed Prediction Explanations (one paragraph per WRONG/PARTIAL):
  [Signal name]: What was predicted. What happened. Whether the failure
  was in signal design, interpretation, or genuine ambiguity. Whether
  the signal would have displaced inertia if it had been correct.

---

## PHASE 4: GAP ANALYSIS
Entry: Phase 3 complete.
Exit: All decision-relevant gaps identified; each has an improvement recommendation.

Gaps are ungathered signals that would have revealed something material.
Evaluate each gap against the inertia path: would this signal have
displaced the inertia path, or only refined execution of the committed path?

| Gap Signal | Namespace | Would Have Revealed | Inertia Impact | Decision Impact |
|------------|-----------|-------------------|----------------|-----------------|

Inertia Impact: WOULD-DISPLACE / WOULD-CONFIRM / UNCERTAIN
Decision Impact: REVERSAL / SCOPE-CHANGE / TIMING-CHANGE / CONFIDENCE-ONLY

Per gap, improvement recommendation:
  "Improvement for [gap]: [practice change]. Activation: [when in lifecycle].
   Inertia test: [how to check whether this signal would shift the default]."

---

## PHASE 5: ECHO
Entry: Phase 4 complete.
Exit: Echo named and systemic pattern identified, OR ECHO: NONE declared.

The Echo is the post-ship finding that no signal predicted AND that was
outside the scope of any identified gap.

Inertia framing for the Echo: Did the unexpected finding reveal a flaw
in the Inertia Path itself (something that would have gone wrong even on
the default path), or a flaw in the committed path specifically?

| Field | Value |
|-------|-------|
| Echo Name | |
| Description | |
| Discovery Point | When post-ship |
| Inertia Path Relevance | Would have manifested on inertia path / Only on committed path |
| Systemic Pattern | Recurring failure mode this represents |
| Signal Family Blind Spot | Which namespace family can't see this class of finding |

Three-way isolation check before proceeding:
- [ ] This finding does not appear as a WRONG verdict in Phase 3
- [ ] This finding is not covered by any gap in Phase 4
- [ ] This is genuinely unforeseeable, not merely unforeseen

---

## PHASE 6: IMPROVEMENT RECOMMENDATION
Entry: Phase 5 complete.
Exit: One recommendation written with gap/Echo attribution and lifecycle trigger.

**Recommendation**: [Practice change]
**Addresses**: [Gap: signal name] OR [Echo: echo name]
**Inertia relevance**: How this change would affect future inertia displacement
**Next cycle trigger**: When/how this activates

---

## OUTPUT FILE

Write artifact to: simulations/topic/{{TOPIC}}-retro-{{DATE}}.md

Phase order preserved in artifact. PRE-EXECUTION CONTRACT at top.
Inertia Path must appear in both the PRE-EXECUTION CONTRACT table and the
Phase 1 narrative.
```

---

## V-05 — Role Sequence + Output Format + Bidirectional Audit Cross-Linking

**Axes**: Role sequence (three-pass bidirectional audit) + Output format (cross-reference columns in every structural table)
**Hypothesis**: Running a forward pass (signals → predictions → accuracy) followed by a backward pass (post-ship actuals → which signal was responsible → verdict validation) and then a cross-link phase that maps each Phase 8 SEAL field to its originating mechanism (and back) maximally satisfies C-32 (per-field independent verification), C-33 (mechanism-keyed tabular form), C-34 (SEAL items cross-reference contract mechanism), and C-35 (one row per SEAL field in the guarantees table).

---

```
You are running /topic-retro for topic: {{TOPIC}}.

Commitment: {{COMMITMENT_DESCRIPTION}}
Commitment date: {{COMMITMENT_DATE}}
AMEND: {{AMEND_SCOPE | "none"}}

---

## PRE-EXECUTION CONTRACT

| Mechanism | Value |
|-----------|-------|
| TOPIC | {{TOPIC}} |
| COMMITMENT | {{COMMITMENT_DESCRIPTION}} |
| COMMITMENT-DATE | {{COMMITMENT_DATE}} |
| SIGNAL-WINDOW | Start → Commitment date |
| AMEND-SCOPE | In-scope namespaces or "all 9" |
| FORWARD-PASS-ANCHOR | Signal record as gathered |
| BACKWARD-PASS-ANCHOR | Post-ship actuals as discovered |
| CROSS-LINK-ANCHOR | Phase 8 SEAL fields |

Every table in this artifact must include a Cross-reference column naming the
PRE-EXECUTION CONTRACT mechanism it is anchored to. Format:
  "Cross-reference: PRE-EXECUTION CONTRACT [mechanism name]"

AMEND: Namespaces not in AMEND-SCOPE are OUT-OF-SCOPE. Every table covering
namespace dimension must mark them explicitly.

---

## PASS 1 — FORWARD PASS: Signal Record → Predictions

Start from the signals as they existed at commitment time.
For each signal gathered, state the prediction it carried into the commitment.

| Signal | Namespace | Pre-Commit Prediction | Confidence (H/M/L) | Cross-reference |
|--------|-----------|----------------------|--------------------|-----------------|

Cross-reference: PRE-EXECUTION CONTRACT FORWARD-PASS-ANCHOR

Rule: Write predictions as they were understood at commitment time, not
retroactively softened. If the original signal file is available, quote it.
If not available, reconstruct from team memory and mark RECONSTRUCTED.

Signal coverage summary (complete after table):

| Namespace | Gathered | Absent | Status |
|-----------|---------|--------|--------|
(9 rows; AMEND: OUT-OF-SCOPE for excluded namespaces)
Cross-reference: PRE-EXECUTION CONTRACT AMEND-SCOPE

---

## PASS 2 — BACKWARD PASS: Post-Ship Actuals → Signal Attribution

Start from what actually happened post-ship.
For each actual finding, trace it back: which signal predicted it (if any),
and what was the verdict?

| Actual Finding | Source (observed where) | Predicting Signal | Verdict | Explanation |
|----------------|------------------------|------------------|---------|-------------|

Cross-reference: PRE-EXECUTION CONTRACT BACKWARD-PASS-ANCHOR

Verdict: CORRECT (signal predicted this) / WRONG (signal predicted otherwise) /
PARTIAL (signal touched this but incompletely) / UNPREDICTED (no signal covered this)

UNPREDICTED findings are candidates for either Gap or Echo classification.
Do not classify them yet — collect them here first.

Accuracy reconciliation (after table):
- Forward pass identified N signals with predictions
- Backward pass attributed M actuals to signals
- Accuracy ratio from backward pass: N_CORRECT / N_attributed = X%
- Cross-check: Does this ratio match the forward pass accuracy?
  If not, explain the discrepancy.

---

## PASS 3 — CLASSIFICATION: Gap vs. Echo for UNPREDICTED Findings

For each UNPREDICTED finding from Pass 2, classify it:

| Finding | Was a signal available? | Classification | Reason |
|---------|------------------------|----------------|--------|
| ...     | YES (gap) / NO (echo candidate) | GAP / ECHO-CANDIDATE / NEITHER | ... |

Cross-reference: PRE-EXECUTION CONTRACT BACKWARD-PASS-ANCHOR

GAP: A signal type exists that would have predicted this; it wasn't gathered.
ECHO-CANDIDATE: No signal type in the 9 namespaces would have predicted this.
NEITHER: The finding was minor enough that no signal was required to cover it.

At most one ECHO-CANDIDATE may be elevated to the Echo.
If multiple ECHO-CANDIDATES exist, pick the one with the clearest systemic pattern.
If none qualify, declare ECHO: NONE.

---

## GAP TABLE

For each finding classified as GAP:

| Gap | Namespace | What Would Have Been Revealed | Decision Impact | Improvement |
|-----|-----------|------------------------------|-----------------|-------------|

Cross-reference: PRE-EXECUTION CONTRACT FORWARD-PASS-ANCHOR

Decision Impact: REVERSAL / SCOPE-CHANGE / TIMING-CHANGE / CONFIDENCE-ONLY
Improvement: One-sentence practice change for next topic cycle.

---

## ECHO TABLE

For the single Echo (or ECHO: NONE):

| Field | Value | Cross-reference |
|-------|-------|-----------------|
| Echo Name | | PRE-EXECUTION CONTRACT BACKWARD-PASS-ANCHOR |
| Description | | PRE-EXECUTION CONTRACT BACKWARD-PASS-ANCHOR |
| Why Not a Gap | | PRE-EXECUTION CONTRACT FORWARD-PASS-ANCHOR |
| Why Not a Wrong Prediction | | PRE-EXECUTION CONTRACT FORWARD-PASS-ANCHOR |
| Systemic Pattern | | PRE-EXECUTION CONTRACT CROSS-LINK-ANCHOR |
| Signal Family Blind Spot | | PRE-EXECUTION CONTRACT CROSS-LINK-ANCHOR |

Three-way isolation check:
- [ ] Echo name does not appear in Pass 2 WRONG column
- [ ] Echo name does not appear in Gap table
- [ ] Echo-candidate passed the "no signal type could have predicted this" test

---

## PHASE 8 SEAL FIELD CROSS-LINK TABLE

One row per Phase 8 SEAL field. Do not collapse SEAL fields.

| SEAL Field | Design Guarantee | Mechanism | Verification Instructions | CHECK | HOW | Cross-reference |
|------------|-----------------|-----------|--------------------------|-------|-----|-----------------|

Cross-reference column: "Cross-reference: PRE-EXECUTION CONTRACT [mechanism]"
— name the exact mechanism from the PRE-EXECUTION CONTRACT responsible for
this guarantee.

CHECK: The independent verification step (does not rely on the mechanism itself).
HOW: How to execute the check.

Bidirectionality requirement: Each row must support navigation in both directions:
- Forward: SEAL field → which mechanism guarantees it (Cross-reference column)
- Backward: mechanism failure → which SEAL fields are affected (note in Mechanism column)

If a SEAL field failure traces to a specific mechanism, that mechanism column
entry must read: "[mechanism name] — failure here affects: [other SEAL fields
this mechanism covers]"

Cross-reference: PRE-EXECUTION CONTRACT CROSS-LINK-ANCHOR

---

## IMPROVEMENT RECOMMENDATION

One recommendation. Must name either Echo or most impactful Gap.
Must specify practice change, attribution, and next cycle trigger.

**Recommendation**: [Practice change]
**Addresses**: [Gap: name] OR [Echo: name]
**Attribution**: Cross-reference: PRE-EXECUTION CONTRACT [mechanism]
**Next cycle trigger**: [Activation condition]

---

## BIDIRECTIONAL AUDIT CHECKLIST

Before writing the output file:

Forward audit (SEAL → mechanism):
- [ ] Every SEAL field row names its originating mechanism in Cross-reference
- [ ] Every table includes a Cross-reference column naming its PRE-EXECUTION CONTRACT anchor
- [ ] AMEND-SCOPE exclusions marked OUT-OF-SCOPE in all namespace-dimension tables

Backward audit (mechanism → SEAL):
- [ ] Every mechanism named in the SEAL table also appears in PRE-EXECUTION CONTRACT
- [ ] Mechanism failures traceable to affected SEAL fields (noted in Mechanism column)
- [ ] Accuracy ratio consistent between Forward Pass and Backward Pass

If any item fails: revise before writing the output file.

---

## OUTPUT FILE

Write artifact to: simulations/topic/{{TOPIC}}-retro-{{DATE}}.md

Section order in artifact:
1. PRE-EXECUTION CONTRACT
2. Pass 1 — Forward Pass
3. Pass 2 — Backward Pass
4. Pass 3 — Classification
5. Gap Table
6. Echo Table
7. SEAL Cross-Link Table
8. Improvement Recommendation
9. Bidirectional Audit Checklist (completed, all boxes checked)
```

---

## Summary Table

| Variation | Primary Axis | Key Differentiator | Strongest Criteria Targets |
|-----------|-------------|-------------------|---------------------------|
| V-01 | Output format (full tabular) | All phases in named-column tables; SEAL table explicit | C-11, C-33, C-34, C-35 |
| V-02 | Role sequence (Echo-first) | Echo discovered before accuracy scoring; three-way isolation check | C-09, C-12 |
| V-03 | Phrasing register (conversational) | Descriptive past-tense framing; "what you learned" structure | C-07, C-09 |
| V-04 | Lifecycle + Inertia framing | Phase entry/exit conditions; Inertia Path named throughout | C-07, C-10 |
| V-05 | Role sequence + format + bidirectional cross-linking | Three-pass structure; every table has Cross-reference column; SEAL fields non-collapsed | C-32, C-33, C-34, C-35 |
