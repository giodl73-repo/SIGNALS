# topic-retro — Variations R3
**Date:** 2026-03-16
**Rubric:** v3 (C-01 through C-14; aspirational denominator = 6)
**R2 top scorers:** All R2 variations embedded formula in header (C-13 origin: V-02) and Echo-before-accuracy (C-12). C-14 origin: V-03 (explicit conflict instruction).
**New criteria to target:** C-13 (formula IS the column header, not only in prose) and C-14 (Echo-accuracy conflict named as a traceable artifact, not a silent revision).

R3 variations all achieve C-13 and C-14. The axes test different *mechanisms* for each:
- C-14 mechanism variants: mandatory conflict phase (V-01, V-04), revision log column (V-03, V-05), conditional annotation in header (V-02)
- C-13 mechanism variants: formula-only header (baseline), formula-with-worked-example header (V-02), two-table repetition (V-04), commit-impact column alongside formula (V-05)
- Role/sequence variants: phased (V-01, V-02, V-03), role-sequence (V-04), inertia-framing (V-05)

Single-axis variations: V-01, V-02, V-03. Combined: V-04, V-05.

---

## V-01 — Conflict-Phase: C-14 as a Mandatory Named Phase

**Axis:** C-14 mechanism — a "Conflict Audit" phase always runs after accuracy scoring and before the verdict, producing output regardless of whether conflict exists.

**Hypothesis:** Making the conflict check a named phase (not a conditional instruction) eliminates the primary C-14 failure mode. When Conflict Audit is a phase, skipping it is visible as a missing section — the same way skipping Echo or Inventory is visible. An always-emitting phase produces either a conflict artifact or an explicit "no conflict" declaration; neither is suppressible.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, and identify gaps.

{{#if amend}}AMEND SCOPE: {{amend}} — all phases operate within this constraint only.{{/if}}

---

PHASE 1 — ECHO
Run this phase before any signal comparison.

Search simulations/{namespace}/ for all artifacts associated with this topic.

The Echo is the single post-ship observable satisfying all three conditions:
  (a) Not predicted by any gathered signal — not even partially
  (b) Not a named risk or acknowledged unknown at commit time
  (c) Observable only after the feature shipped

Procedure:
  Step 1: List every post-ship outcome for this topic.
  Step 2: Eliminate any predicted by a gathered signal (fully or partially).
  Step 3: Eliminate any that were named risks or known unknowns.
  Step 4: From remaining candidates, select exactly one with highest commit-decision impact.
  Step 5: If no candidates remain: "No Echo — all post-ship outcomes were within signal bounds."

Output this table:

| Echo (one sentence) | Nearest signal artifact | Commit relevance: HIGH / MEDIUM / LOW |
|---------------------|------------------------|--------------------------------------|
| [finding or "No Echo — all post-ship outcomes were within signal bounds"] | [name or "none"] | [level or "N/A"] |

LOCK: This table is final. Phases 2–8 may not alter it.
If Phase 5 or Phase 6 analysis would revise the Echo, record the conflict in Phase 6 — do not edit this table.

---

PHASE 2 — SIGNAL INVENTORY
List every artifact gathered before commit, one row per file.

| Namespace | Artifact | Date | Prediction summary |
|-----------|----------|------|--------------------|
| [name] | [filename] | [YYYY-MM-DD] | [one phrase] |

After the table:
  Namespaces with signals: [list]
  Empty namespaces (from: scout, draft, review, flow, trace, prove, listen, program, topic): [list]
  Total: N signals across M namespaces

---

PHASE 3 — PREDICTED VS ACTUAL
For each namespace with at least one Phase 2 artifact:

| Namespace | Predicted (what signals claimed post-ship) | Actual (what was observed) | Match: C / P / W / ND |
|-----------|--------------------------------------------|----------------------------|-----------------------|
| [name] | [required — cannot be blank] | [required — cannot be blank] | [verdict] |

Verdict: C = Correct, P = Partial (directionally right, wrong magnitude/timing), W = Wrong, ND = No data.
Both Predicted and Actual must be explicitly stated for every row.

---

PHASE 4 — NAMESPACE ACCURACY
Score each namespace from Phase 3 using the formula in the column header.

| Namespace | C | P | W | ND | Score: (C×100 + P×50) ÷ (C+P+W) |
|-----------|---|---|---|-----|----------------------------------|
| [name] | | | | | |
| TOTAL | | | | | |

ND entries excluded from denominator. Leave Score blank if denominator = 0.

---

PHASE 5 — CONFLICT AUDIT
This phase is mandatory. It always produces output.

Review the locked Echo from Phase 1.
Question: Does anything in Phase 3 (match verdicts) or Phase 4 (namespace scores) suggest the Echo finding should be revised to a different outcome?

If YES — emit a conflict artifact:
  CONFLICT DETECTED
  Source: [Phase 3 / Phase 4 — which finding creates the tension]
  Proposed revision: [what the Echo would become under this analysis]
  Resolution: Echo from Phase 1 is preserved unchanged. This conflict entry is the C-14 artifact.

If NO — emit:
  CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 findings are consistent with the locked Echo.

Do not proceed to Phase 6 without emitting one of the two outputs above.

---

PHASE 6 — ACCURACY VERDICT
State the overall accuracy judgment, grounded in Phase 4 totals:

  "Signal accuracy for [topic]: [TOTAL score]/100 — [STRONG (>=75) / ADEQUATE (50-74) / WEAK (<50)]"

Do not introduce new observations. Reference Phase 4 TOTAL row only.

---

PHASE 7 — GAP ANALYSIS
For each namespace scoring W or P in Phase 3, and each empty namespace where absence is material:

| Gap (signal type absent) | Namespace | Skill to run | Would have surfaced | Changed commit? YES / NO |
|--------------------------|-----------|-------------|---------------------|--------------------------|
| [type] | [namespace] | [exact skill, e.g., /flow-resilience] | [one sentence] | [verdict] |

"Gather more data" does not satisfy the Skill column. Name an exact skill from the Signal namespace catalog.
If no gaps: "No gaps — signal coverage was sufficient for this commit decision."

---

PHASE 8 — CALIBRATION TREND

| Prior retro (topic / date) | Prior score | This score | Delta | Trend |
|---------------------------|-------------|------------|-------|-------|
| [reference or "none"] | | | | ↑ improving / ↓ degrading / = stable |

No prior retro: "First retro for this topic — this score establishes the calibration baseline."

---

PHASE 9 — ECHO → SIGNAL DESIGN
Translate the Phase 1 Echo into one concrete change to signal gathering practice.

| Echo finding (from Phase 1) | Proposed change | Change type |
|-----------------------------|----------------|-------------|
| [finding] | [specific change] | new skill / rubric amendment / threshold adjustment |

---

Execute phases in order: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9.
Accuracy (Phase 4) follows Echo (Phase 1). Conflict Audit (Phase 5) follows Accuracy (Phase 4) and precedes Verdict (Phase 6). These orderings are structural, not advisory.
```

---

## V-02 — Extended-Formula-Header: C-13 Strengthened with Inline Worked Example

**Axis:** C-13 mechanism — the column header embeds both the formula and a worked example inline: `Score: (C×100+P×50)÷(C+P+W) [e.g. C=2,P=1,W=1 → 62.5]`. The example is part of the header, not a prose footnote.

**Hypothesis:** Embedding a worked calculation inside the header notation makes C-13 self-demonstrating — the header not only states the formula but proves it has a computable form by showing one output. A model that copies the header and populates the rows has seen the formula applied; a model that ignores the header produces obviously wrong cells. Baseline C-14 is achieved via conditional annotation required immediately before the accuracy table.

---

```
Post-commitment retrospective for: $ARGUMENTS

A feature has shipped. You will assess which signals were accurate, what was unexpected, and what was missing.

{{#if amend}}AMEND: {{amend}} — all sections stay within this scope.{{/if}}

---

SECTION 1 — ECHO
Complete this section before examining any signal predictions.

The Echo is the single post-ship finding satisfying all of:
  (1) No gathered signal predicted it, even partially
  (2) It was not a named risk or known unknown at commit time
  (3) It is only observable after the feature shipped

Search simulations/{namespace}/ for all artifacts for this topic.
List post-ship outcomes → cross against signal predictions → eliminate predicted and known-risk outcomes.
From remaining candidates, select exactly one with highest commit-decision impact.
If no candidates qualify: "No Echo — all post-ship outcomes were within signal bounds."

Echo entry:
  ECHO: [one sentence]
  NEAREST SIGNAL: [artifact name or "none"]
  COMMIT RELEVANCE: HIGH (would have stopped commit) | MEDIUM (added conditions) | LOW (informational)
  DESIGN CHANGE: [new skill: [name] | rubric amendment: [rubric + change] | threshold: [metric + value] | new signal type: [description]]

This entry is locked. Do not revise it.
If Section 3 accuracy analysis would suggest a different Echo, write immediately before the accuracy table:
  > ECHO-ACCURACY CONFLICT: [Section 3 finding that creates tension] — [what the Echo would become].
  > ORIGINAL ECHO IS PRESERVED. This conflict entry is a permanent artifact of this retro.
Then proceed with the table. If no conflict exists, do not write the conflict block.

---

SECTION 2 — SIGNAL INVENTORY
List every artifact gathered before commit.

| # | Namespace | Artifact | Date | Prediction |
|---|-----------|----------|------|------------|
| 1 | | | | |

Coverage:
  Namespaces with signals: [list]
  Empty namespaces (scout, draft, review, flow, trace, prove, listen, program, topic — list those with none): [list]

---

SECTION 3 — PREDICTED VS ACTUAL + NAMESPACE ACCURACY

Step A: For each namespace with artifacts, state the prediction and what actually happened post-ship.

| Namespace | Predicted | Actual | Match: C / P / W / ND |
|-----------|-----------|--------|----------------------|
| [name] | [required] | [required] | [verdict] |

Verdict key: C = Correct, P = Partial, W = Wrong, ND = No post-ship data yet.
Both Predicted and Actual must be non-empty for every row.

Step B: Check for Echo conflict (see Section 1 instruction). Write conflict block here if applicable.

Step C: Score each namespace using the formula embedded in the header. The header contains both the formula and a worked example — apply the formula, not the example values.

| Namespace | C | P | W | ND | Score: (C×100+P×50)÷(C+P+W) [e.g. C=2,P=1,W=1 → 62.5] |
|-----------|---|---|---|-----|----------------------------------------------------------|
| [name] | | | | | |
| TOTAL | | | | | |

ND excluded from denominator. Score blank if denominator = 0.

Overall verdict:
  STRONG: total >= 75
  ADEQUATE: total 50–74
  WEAK: total < 50

State: "Signal accuracy for [topic]: [total]/100 — [verdict]"

Calibration:
  Prior retro found: "[prior score] → [this score]: [improving / degrading / stable]"
  No prior retro: "First retro — this score is the baseline."

---

SECTION 4 — GAPS
Signals not gathered that would have changed the commit decision.

| Gap (signal type) | Namespace | Skill to run | Would have surfaced | Changed commit? |
|-------------------|-----------|-------------|---------------------|-----------------|
| [type] | [ns] | [exact skill name] | [one sentence] | YES / NO |

Skill must be a named catalog skill. "Get more data" fails.
If no gaps: "No gaps — signal coverage was sufficient."

---

SECTION 5 — CALIBRATION TREND (standalone)

| Reference retro | Score | This retro | Delta | Trend |
|-----------------|-------|-----------|-------|-------|
| | | | | ↑ / ↓ / = |

No prior retro: "First retro for this topic."

---

SECTION 6 — ECHO → SIGNAL DESIGN

| Echo finding | Proposed change | Change type |
|-------------|----------------|-------------|
| [from Section 1] | [specific change] | new skill / rubric amendment / threshold |

---

Output order: Section 1 (Echo) → Section 2 (Inventory) → Section 3 (Accuracy, with conflict check immediately before the accuracy table) → Section 4 (Gaps) → Section 5 (Trend) → Section 6 (Design).
```

---

## V-03 — Revision-Log: C-14 as a Structural Column in the Echo Table

**Axis:** C-14 mechanism — the Echo table includes a "Revision log" column. Its initial value is always `LOCKED — no revisions`. If any later phase produces findings that would change the Echo, the revision log cell must be updated in place with a conflict entry. The column IS the C-14 artifact.

**Hypothesis:** Converting C-14 from a prose instruction ("if tension arises, note it") into a pre-existing column forces the conflict artifact into existence at Echo-identification time. A scorecard can verify C-14 by reading the Revision log cell — it either says "LOCKED — no revisions" (no conflict) or contains a conflict entry (conflict surfaced). The artifact cannot be omitted because the column always exists.

---

```
Topic retrospective for: $ARGUMENTS

Feature has shipped. Run the retro in phases. The Echo table uses a Revision log column — this column is the C-14 artifact for this retro.

{{#if amend}}SCOPE: {{amend}} — all phases stay within this constraint.{{/if}}

---

PHASE A — ECHO
Run this phase before any scoring.

Search simulations/{namespace}/ for all artifacts associated with this topic.

Identify THE ECHO: the single post-ship observable that:
  (1) No gathered signal predicted (not even partially)
  (2) Was not a named risk or acknowledged unknown at commit time
  (3) Is only observable post-ship

Procedure: list post-ship outcomes → eliminate predicted → eliminate known risks → select one with highest commit impact.
If none qualify: Echo = "No Echo — all post-ship outcomes were within signal bounds."

Output this table with four columns. The Revision log column starts as "LOCKED — no revisions" for every retro.

| Echo (one sentence) | Nearest signal | Commit relevance | Revision log |
|---------------------|----------------|-----------------|--------------|
| [finding] | [artifact or "none"] | HIGH / MEDIUM / LOW | LOCKED — no revisions |

PHASE A IS COMMITTED. The Echo cell in this table does not change.
The Revision log cell updates if Phase C or Phase D analysis creates tension with the Echo. Update it as:
  [Phase C / Phase D] conflict: analysis suggests Echo should be "[proposed revision]". Original Echo preserved.
The Revision log entry is the traceable C-14 artifact. A retro with "LOCKED — no revisions" passed C-14 by finding no conflict.

---

PHASE B — SIGNAL INVENTORY
List every artifact gathered before commit. One row per file.

| Namespace | Artifact | Date | Prediction summary |
|-----------|----------|------|--------------------|
| [name] | [filename] | [YYYY-MM-DD] | [one phrase] |

Coverage summary:
  With signals: [namespace list]
  Empty (scout, draft, review, flow, trace, prove, listen, program, topic): [list empty ones]
  Total: N

---

PHASE C — PREDICTED VS ACTUAL
For each namespace with Phase B artifacts, compare prediction to outcome.

| Namespace | Predicted | Actual | Match: C / P / W / ND |
|-----------|-----------|--------|----------------------|
| [name] | [required] | [required] | [verdict] |

C = Correct, P = Partial, W = Wrong, ND = No data.
If any match verdict contradicts the Phase A Echo — update the Revision log in Phase A before continuing.

---

PHASE D — NAMESPACE ACCURACY

| Namespace | C | P | W | ND | Score: (C×100 + P×50) ÷ (C+P+W) |
|-----------|---|---|---|-----|----------------------------------|
| [name] | | | | | |
| TOTAL | | | | | |

ND excluded from denominator. Score blank if denominator = 0.
If namespace scores reveal tension with Phase A Echo — update the Revision log in Phase A before continuing.

Accuracy verdict:
  STRONG: total >= 75 | ADEQUATE: 50–74 | WEAK: < 50
  "Signal accuracy for [topic]: [total]/100 — [verdict]"

Calibration: prior retro → this retro trend, or "First retro — baseline established."

---

PHASE E — GAPS
Missing signals that would have changed the commit decision.

| Gap signal | Namespace | Skill to run | Would have surfaced | Changed commit? YES / NO |
|-----------|-----------|-------------|---------------------|--------------------------|
| [type] | [ns] | [exact skill name] | [one sentence] | [verdict] |

No generic advice. Name a specific skill.
If no gaps: "No gaps — signal coverage was sufficient."

---

PHASE F — CALIBRATION TREND

| Reference retro | Prior score | This score | Delta | Trend |
|-----------------|-------------|------------|-------|-------|
| [topic / date or "none"] | | | | ↑ / ↓ / = |

No prior retro: "First retro for this topic."

---

PHASE G — ECHO → SIGNAL DESIGN

| Echo (from Phase A) | Proposed change | Change type |
|--------------------|----------------|-------------|
| [finding] | [specific change] | new skill / rubric amendment / threshold |

---

Output order: Phase A → Phase B → Phase C → Phase D → Phase E → Phase F → Phase G.
Accuracy (Phase D) follows Echo (Phase A). The Revision log column in Phase A is the retro's C-14 artifact — its final state at completion is the definitive record of whether Echo-accuracy conflict arose.
```

---

## V-04 — Combined: Conflict-Phase + Role-Sequence

**Axes:** C-14 as mandatory conflict-audit role (builds on V-01) + role-sequence framing from R2-V04 (three voices now four)

**Hypothesis:** A four-role protocol — Archivist, Echo Finder, Scorer, Conflict Auditor — where the Conflict Auditor is the terminal mandatory role enforces both C-12 and C-14 at role boundaries. C-12 is guaranteed by the Scorer receiving the Echo Finder's locked output as an input contract. C-14 is guaranteed by the Conflict Auditor existing as a required role — skipping it is visible as an absent role block. The Conflict Auditor always produces output, whether "no conflict" or a named conflict artifact.

---

```
Run topic-retro for: $ARGUMENTS

Four roles execute in sequence. Each role receives only what prior roles produced. No role may revise a prior role's output — if analysis creates conflict with a prior role's output, the conflict is logged, not the output revised.

{{#if amend}}SCOPE: {{amend}} — all roles stay within this constraint.{{/if}}

---

ROLE 1 — THE ARCHIVIST
The Archivist records. Does not interpret, predict, or assess.

Search simulations/{namespace}/ for all artifacts associated with this topic.

Produce the Signal Registry:

| # | Namespace | Artifact | Date | Prediction summary (one phrase) |
|---|-----------|----------|------|---------------------------------|
| 1 | [name] | [filename] | [YYYY-MM-DD] | [phrase] |

Coverage:
  Namespaces with artifacts: [list]
  Namespaces with no artifacts (scout, draft, review, flow, trace, prove, listen, program, topic): [list empty]
  Total artifacts: N

→ Hand Signal Registry to Role 2.

---

ROLE 2 — THE ECHO FINDER
The Echo Finder receives: Signal Registry (from Role 1).
The Echo Finder identifies what the signals failed to predict. Does not score accuracy. Does not assess gaps.

Task:
  Step 1 — Compile all predictions from the Signal Registry, grouped by namespace.
  Step 2 — List every post-ship observable outcome for this topic.
  Step 3 — Find THE ECHO: the single post-ship observable where:
    (a) No Signal Registry prediction covers it, even partially
    (b) It was not a named risk or acknowledged unknown at commit time
    (c) It is only observable post-ship
  Step 4 — Multiple candidates: select the one with highest commit-decision impact.
  Step 5 — No candidates: Echo = "No Echo — all post-ship outcomes were within signal bounds."

Echo Record (locked before Role 3 runs):
  ECHO: [one sentence]
  NEAREST SIGNAL: [artifact from the Signal Registry, or "none"]
  COMMIT RELEVANCE: HIGH (would have stopped commit) | MEDIUM (added conditions) | LOW (informational)
  DESIGN CHANGE: [new skill: [exact name] | rubric amendment: [rubric + detail] | threshold: [metric + value] | new signal type: [description]]

The Echo Record is final. Role 3 and Role 4 may reference it but may not change it.
If Role 3 analysis would change the Echo, Role 4 — the Conflict Auditor — will record the tension.

→ Hand Signal Registry (Role 1) + Echo Record (Role 2) to Role 3.

---

ROLE 3 — THE SCORER
The Scorer receives: Signal Registry (from Role 1) + Echo Record (from Role 2).
The Scorer may not revise the Echo Record.

Step A — Predicted vs Actual
For each namespace with Signal Registry artifacts:

| Namespace | Predicted (signals' collective claim) | Actual (post-ship observation) | Match: C / P / W / ND |
|-----------|--------------------------------------|-------------------------------|----------------------|
| [name] | [required] | [required] | [verdict] |

Both columns must be explicit. A verdict without both sides is invalid.

Step B — Namespace Accuracy
Apply formula from column header to Role 3 Step A verdicts.

| Namespace | C | P | W | ND | Score: (C×100 + P×50) ÷ (C+P+W) |
|-----------|---|---|---|-----|----------------------------------|
| [name] | | | | | |
| TOTAL | | | | | |

ND excluded from denominator. Score blank if denominator = 0.

Accuracy verdict:
  STRONG (>=75) | ADEQUATE (50-74) | WEAK (<50)
  "Signal accuracy for [topic]: [total]/100 — [verdict]"

Calibration: "[prior score] → [this score]: [trend]" or "First retro — this score is the baseline."

Step C — Gap Analysis
For each namespace scoring W or P, and each empty namespace where absence is material:

| Gap (signal type) | Namespace | Skill to run | Would have surfaced | Changed commit? YES / NO |
|-------------------|-----------|-------------|---------------------|--------------------------|
| [type] | [ns] | [exact skill name] | [one sentence] | [verdict] |

Exact skill required. "Gather more data" fails.
No gaps: "No gaps — coverage was sufficient."

→ Hand Signal Registry (Role 1) + Echo Record (Role 2) + Scorer output (Role 3) to Role 4.

---

ROLE 4 — THE CONFLICT AUDITOR
The Conflict Auditor receives: all prior role outputs.
This role is mandatory. It always produces one of two outputs.

Task: Review Role 3 Step A (match verdicts) and Role 3 Step B (namespace scores).
Question: Does any Role 3 finding suggest that the Echo Record from Role 2 should name a different finding?

If YES — emit this artifact:
  CONFLICT DETECTED (Role 4 — Conflict Audit)
  Source: [Role 3 Step A / Step B — which finding creates tension]
  Analysis: [what Role 3 data suggests the Echo should be revised to]
  Resolution: Echo Record from Role 2 is preserved as locked. This entry is the C-14 artifact.

If NO — emit:
  CONFLICT AUDIT COMPLETE: No conflict. Role 3 findings are consistent with the Role 2 Echo Record.

The Conflict Auditor's output is the final section of this retro.

---

Final output order: Echo Record (Role 2) → Signal Registry (Role 1) → Scorer output (Role 3: Steps A, B, C) → Conflict Auditor output (Role 4).
The Echo Record precedes all accuracy scoring. The Conflict Auditor follows all scoring. This sequencing is enforced by role handoffs, not by instruction alone.
```

---

## V-05 — Combined: Revision-Log + Inertia-Framing

**Axes:** C-14 as revision log column (builds on V-03) + commit-decision counterfactual framing from R2-V05 adapted for C-13/C-14 compliance

**Hypothesis:** The inertia framing (R2-V05) surfaces which namespaces added value over the status-quo baseline — it is inherently about commit-decision impact. When combined with the revision log column (V-03), the retro answers two questions simultaneously: "were our signals accurate?" (formula-scored per namespace) and "did our signals outperform the decision we'd have made without them?" (inertia framing). The revision log makes C-14 structural; the commit-impact column gives C-14 a decision-relevant consequence — if the Echo was truly unexpected, neither signals nor baseline predicted it.

---

```
Post-commitment retrospective for: $ARGUMENTS

This retro is structured against a counterfactual: what would the team have decided without signal gathering? Every accuracy row includes a baseline comparison — signals that matched the default assumption added no lift.

{{#if amend}}AMEND: {{amend}} — all sections stay within this constraint.{{/if}}

---

SECTION 0 — ECHO
Run this section before examining any signal predictions.

The Echo is the single post-ship observable satisfying all three tests:
  Test 1: Not predicted by any gathered signal, even partially
  Test 2: Not a named risk or acknowledged unknown at commit time — and not what the default assumption would have predicted either
  Test 3: Observable only after the feature shipped

The Echo is the thing neither signals nor the baseline saw coming.

Search simulations/{namespace}/ for all artifacts for this topic.
Procedure: list post-ship outcomes → eliminate those predicted by signals → eliminate those the default assumption would have predicted → select the highest-commit-impact remaining outcome as Echo.
If none qualify: "No Echo — all post-ship outcomes were within signal or baseline bounds."

Output this table with the Revision log column pre-filled:

| Echo (one sentence) | Nearest signal | Baseline predicted it? YES/NO | Commit relevance | Revision log |
|---------------------|----------------|-------------------------------|-----------------|--------------|
| [finding] | [artifact or "none"] | YES / NO | HIGH / MEDIUM / LOW | LOCKED — no revisions |

LOCK: Echo cell does not change. Revision log cell updates if Section 2 creates tension:
  Update to: "[Section 2 finding]: analysis suggests Echo should be [X]. Original Echo preserved."
The Revision log cell is the C-14 artifact. Its final state at completion is the definitive conflict record.

---

SECTION 1 — SIGNAL INVENTORY
List every artifact gathered before commit, grouped by namespace.

| # | Namespace | Artifact | Date | Prediction | Baseline assumption (what team assumed without this signal) |
|---|-----------|----------|------|------------|-------------------------------------------------------------|
| 1 | [name] | [file] | [date] | [one phrase] | [what the team would have assumed absent this signal] |

The baseline column surfaces where each signal challenged or confirmed default thinking.

Coverage:
  Namespaces with signals: [list]
  Empty namespaces (scout, draft, review, flow, trace, prove, listen, program, topic): [list empty]

---

SECTION 2 — PREDICTED VS ACTUAL + NAMESPACE ACCURACY

For each namespace with artifacts, assess prediction accuracy AND baseline accuracy.

Step A — Match comparison:

| Namespace | Signal prediction | Baseline assumption | Actual outcome | Signal match: C/P/W/ND | Baseline match: C/P/W/ND |
|-----------|------------------|--------------------|-----------------|-----------------------|--------------------------|
| [name] | [required] | [required] | [required] | [verdict] | [verdict] |

Step B — Check Echo conflict. If any row's outcome would revise the Section 0 Echo, update the Revision log cell in Section 0 now, then continue.

Step C — Namespace accuracy with inertia lift:

| Namespace | C | P | W | ND | Score: (C×100+P×50)÷(C+P+W) | Baseline score: (C×100+P×50)÷(C+P+W) | Signal lift (signal − baseline) |
|-----------|---|---|---|-----|------------------------------|---------------------------------------|--------------------------------|
| [name] | | | | | | | Δ |
| TOTAL | | | | | | | Δ |

Apply the header formula to both the signal score column and the baseline score column.
ND excluded from denominator. Score blank if denominator = 0.
Positive lift: signals improved on baseline. Negative lift: baseline intuition was more accurate.

Check: would any namespace score update tension with the Section 0 Echo? If yes, update Revision log before stating the verdict.

Accuracy verdict:
  Signal score: STRONG (>=75) | ADEQUATE (50-74) | WEAK (<50)
  "Signal accuracy for [topic]: [signal total]/100 — [verdict]. Baseline: [baseline total]/100. Net lift: Δ[lift]."

Calibration: prior retro → this retro trend, or "First retro — this score and lift are the baseline."

---

SECTION 3 — GAPS
Signals not gathered. Prioritize gaps where both signals AND baseline were wrong — highest-leverage areas.

| Gap signal | Namespace | Skill to run | Would have surfaced | Signal missed it? YES/NO | Baseline missed it? YES/NO | Changed commit? YES/NO |
|-----------|-----------|-------------|---------------------|--------------------------|----------------------------|------------------------|
| [type] | [ns] | [exact skill name] | [one sentence] | [verdict] | [verdict] | [verdict] |

Tier 1 — Both signal and baseline missed, commit impact YES: [list]
Tier 2 — Baseline missed, signal would have caught, commit impact YES: [list]
Tier 3 — Confidence builders (commit impact NO): [list]

Exact skill required. No generic advice.
No gaps: "No gaps — signal coverage was sufficient."

---

SECTION 4 — CALIBRATION TREND

| Reference retro | Signal score | Baseline score | This signal score | This baseline score | Signal trend | Lift trend |
|-----------------|-------------|----------------|------------------|--------------------:|:------------:|:----------:|
| [topic / date] | | | | | ↑/↓/= | ↑/↓/= |

No prior retro: "First retro — signal and baseline scores are the starting calibration."

---

SECTION 5 — ECHO → SIGNAL DESIGN

| Echo (from Section 0) | Baseline also missed it? YES/NO | Proposed change | Change type |
|-----------------------|--------------------------------|----------------|-------------|
| [finding] | [verdict] | [specific change] | new skill / rubric amendment / threshold |

If baseline also missed it, the proposed change addresses a genuine blind spot — neither prior experience nor signals covered it.

---

Output order: Section 0 (Echo with Revision log) → Section 1 (Inventory) → Section 2 (Accuracy, with Echo conflict check inline before the accuracy tables) → Section 3 (Gaps) → Section 4 (Trend) → Section 5 (Design).
Accuracy (Section 2) follows Echo (Section 0). The Revision log column in Section 0 is the definitive C-14 artifact — its state at the end of this retro records whether Echo-accuracy conflict arose and what it was.
```

---

## Summary Table

| ID | Primary Axis | C-13 Mechanism | C-14 Mechanism | Hypothesis Tested |
|----|-------------|----------------|----------------|-------------------|
| V-01 | C-14: mandatory conflict phase | Formula in Phase 4 column header | Phase 5 always runs; produces conflict artifact OR "no conflict" declaration | A named mandatory phase makes C-14 unskippable — same visibility as a missing Echo phase |
| V-02 | C-13: formula + worked example in header | Header includes formula AND inline example: `[e.g. C=2,P=1,W=1 → 62.5]` | Conditional annotation required immediately before accuracy table | Formula-with-example header is self-demonstrating — C-13 proves the formula was read, not just copied |
| V-03 | C-14: revision log column in Echo table | Formula in Phase D column header | Revision log column pre-exists in Echo table; updates in-place when conflict arises | Pre-existing column makes C-14 artifact permanent from Phase A; its state is the conflict record |
| V-04 | C-14 conflict role + role sequence | Formula in Role 3 Step B column header | Role 4 (Conflict Auditor) is a mandatory terminal role; always emits output | Four-role boundary enforces both C-12 (Echo Finder before Scorer) and C-14 (Auditor always runs) |
| V-05 | Revision log + inertia framing | Formula in Section 2 signal and baseline score column headers | Revision log column in Section 0 Echo table; baseline comparison creates Echo-conflict pressure | Inertia framing + revision log: when baseline columns are present, Echo-accuracy tension is more likely to surface — making C-14 more frequently tested |
