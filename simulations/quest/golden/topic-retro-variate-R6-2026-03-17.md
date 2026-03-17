# topic-retro — Variations R6
**Date:** 2026-03-17
**Rubric:** v4 (C-01 through C-19; total available = 112)
**R5 top scorer:** V-01 (103/108, 95%) — table-enforced columns, exact recommendation template, explicit namespace coverage table. V-02 scored 95/108 (88%); V-03–V-05 not provided to scorer.
**New criteria to target:** C-18 (echo-systemic-pattern-named) and C-19 (phase-completion-self-contained).

R6 variations all target C-18 and C-19. Axes test different mechanisms:
- C-18 mechanism variants: pattern taxonomy column with named-pattern structure (V-01, V-04), inline REQUIRED field with pattern format (V-03)
- C-19 mechanism variants: phase seal checklist (V-02, V-05), inline REQUIRED markers at every required field (V-03)
- Additional axes: phrasing register (V-03), role sequence with dedicated Pattern Classifier role (V-04), inertia framing + seals (V-05)

Single-axis variations: V-01, V-02, V-03. Combined: V-04, V-05.

---

## V-01 — Pattern-Taxonomy: C-18 via Named Failure Mode Column in Echo Table

**Axis:** C-18 mechanism — the Echo table adds a `Pattern` column requiring a named failure mode in the rubric's exact format: `[name] — [description of recurring failure mode]`. A pattern taxonomy is embedded in the prompt; selecting from it or naming a new entry satisfies C-18 structurally.

**Hypothesis:** Making C-18 a table column (not a prose instruction) forces the named pattern to appear at Echo time. A column cannot be silently skipped — the same mechanism that earns C-14 in R5-V-01 (CORRECT/WRONG/PARTIAL cannot drift to prose) now applies to C-18. Embedding a taxonomy gives the model the vocabulary it needs to populate the column rather than paraphrasing the finding a second time.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, classify the systemic failure mode, and identify gaps.

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
  Step 5: If no candidates remain: Echo = "No Echo — all post-ship outcomes were within signal bounds."

Pattern taxonomy — name the repeating systemic failure mode this Echo represents:
  adoption-assumption-gap     — team assumed adoption follows from quality or availability
  integration-surface-miss    — component boundary behavior (API, event, state) not validated
  timing-signal-gap           — timing dependency or sequencing not surfaced by any signal
  scale-behavior-gap          — behavior at real-world load or data scale not predicted
  dependency-chain-miss       — upstream/downstream dependency not traced by any signal
  unknown-unknown             — no available Signal skill covers this class of finding
  other: [name] — [one phrase describing the recurring failure category]

Output this table:

| Echo (one sentence) | Nearest signal artifact | Commit relevance: HIGH / MEDIUM / LOW | Pattern: [name] — [recurring failure mode description] |
|---------------------|------------------------|--------------------------------------|--------------------------------------------------------|
| [finding or "No Echo — all post-ship outcomes were within signal bounds"] | [name or "none"] | [level or "N/A"] | [named category from taxonomy — not blank, not a restatement of the Echo] |

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
Translate the Phase 1 Echo and its Pattern classification into one concrete change to signal gathering practice.

| Echo finding (from Phase 1) | Pattern (from Phase 1) | Proposed change | Change type |
|-----------------------------|------------------------|----------------|-------------|
| [finding] | [named category — must match Phase 1 Pattern column exactly] | [specific change] | new skill / rubric amendment / threshold adjustment |

If the Pattern is "other: [name]", propagate that name here. The Pattern column must not be blank.

Use this template exactly:
  > **Recommendation**: Addresses [Gap: name / Echo: pattern name] by [specific practice change].

---

Execute phases in order: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9.
The Pattern column in Phase 1 is mandatory — it names a repeating systemic failure mode, not just this Echo instance. Phase 9 must propagate the same pattern name, making the failure mode traceable from finding to practice change.
```

---

## V-02 — Phase-Seal: C-19 via Completion Contract per Phase

**Axis:** C-19 mechanism — each phase ends with a PHASE SEAL, a checklist of its required fields. The phase is not considered complete until every seal item is confirmed. Seal items name the exact required fields, not general aspirations.

**Hypothesis:** A phase seal makes C-19 structural. Truncated phases cannot pass the seal because the seal items are the minimum required for the phase to be rubric-scoreable. When the seal appears at the end of each phase, a model that exits before populating all fields produces a visibly incomplete seal — the same visibility as a missing Echo phase. Unlike V-01 (which enforces fields via table columns), the seal mechanism works for phases whose required content is not naturally tabular.

---

```
Run a post-commitment retrospective on topic: $ARGUMENTS

A feature has shipped. Assess signal accuracy, name the unexpected, and identify gaps. Each phase ends with a PHASE SEAL — a required-field checklist. The phase is not complete until every seal item is confirmed.

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
  Step 5: If no candidates remain: Echo = "No Echo — all post-ship outcomes were within signal bounds."

Output this table:

| Echo (one sentence) | Nearest signal artifact | Commit relevance: HIGH / MEDIUM / LOW |
|---------------------|------------------------|--------------------------------------|
| [finding or "No Echo — all post-ship outcomes were within signal bounds"] | [name or "none"] | [level or "N/A"] |

After the table, name the systemic pattern:
  > **Pattern**: [name] — [description of the recurring failure mode this Echo represents, not just this instance]

Pattern examples: adoption-assumption-gap, integration-surface-miss, timing-signal-gap, scale-behavior-gap, dependency-chain-miss, unknown-unknown, or name your own.

LOCK: This table and Pattern entry are final. Phases 2–8 may not alter them.
If Phase 5 or Phase 6 analysis would revise the Echo, record the conflict in Phase 5 — do not edit this phase.

PHASE 1 SEAL — confirm before proceeding to Phase 2:
  [ ] Echo cell: one sentence (or explicit "No Echo" statement — not a restatement of a wrong prediction)
  [ ] Nearest signal: named artifact or "none"
  [ ] Commit relevance: HIGH, MEDIUM, or LOW (or "N/A" with "No Echo")
  [ ] Pattern entry: uses > **Pattern**: [name] — [description] format (not blank, not generic)
All items confirmed? PHASE 1 COMPLETE.

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

PHASE 2 SEAL — confirm before proceeding to Phase 3:
  [ ] Every artifact from simulations/ for this topic has a row
  [ ] Empty namespace list accounts for all 9 namespaces not in "with signals"
  [ ] Total count stated
All items confirmed? PHASE 2 COMPLETE.

---

PHASE 3 — PREDICTED VS ACTUAL
For each namespace with at least one Phase 2 artifact:

| Namespace | Predicted (what signals claimed post-ship) | Actual (what was observed) | Match: C / P / W / ND |
|-----------|--------------------------------------------|----------------------------|-----------------------|
| [name] | [required — cannot be blank] | [required — cannot be blank] | [verdict] |

Verdict: C = Correct, P = Partial (directionally right, wrong magnitude/timing), W = Wrong, ND = No data.
Both Predicted and Actual must be explicitly stated for every row.

PHASE 3 SEAL — confirm before proceeding to Phase 4:
  [ ] Every namespace from Phase 2 has a row
  [ ] No Predicted cell is blank
  [ ] No Actual cell is blank
  [ ] Every row has a verdict label (C / P / W / ND)
All items confirmed? PHASE 3 COMPLETE.

---

PHASE 4 — NAMESPACE ACCURACY
Score each namespace from Phase 3 using the formula in the column header.

| Namespace | C | P | W | ND | Score: (C×100 + P×50) ÷ (C+P+W) |
|-----------|---|---|---|-----|----------------------------------|
| [name] | | | | | |
| TOTAL | | | | | |

ND entries excluded from denominator. Leave Score blank if denominator = 0.

PHASE 4 SEAL — confirm before proceeding to Phase 5:
  [ ] Every Phase 3 namespace has a row
  [ ] TOTAL row present
  [ ] Score column: formula applied to each row (blank only when denominator = 0, noted as such)
All items confirmed? PHASE 4 COMPLETE.

---

PHASE 5 — CONFLICT AUDIT
This phase is mandatory. It always produces output.

Review the locked Echo from Phase 1.
Question: Does anything in Phase 3 (match verdicts) or Phase 4 (namespace scores) suggest the Echo finding should be revised to a different outcome?

If YES — emit:
  CONFLICT DETECTED
  Source: [Phase 3 / Phase 4 — which finding creates the tension]
  Proposed revision: [what the Echo would become under this analysis]
  Resolution: Echo from Phase 1 is preserved unchanged. This is the conflict artifact.

If NO — emit:
  CONFLICT AUDIT: No conflict. Phase 3 and Phase 4 findings are consistent with the locked Echo.

PHASE 5 SEAL — confirm before proceeding to Phase 6:
  [ ] Conflict audit question answered
  [ ] If YES: conflict artifact present with Source, Proposed revision, Resolution
  [ ] If NO: explicit "No conflict" declaration present
All items confirmed? PHASE 5 COMPLETE.

---

PHASE 6 — ACCURACY VERDICT
State the overall accuracy judgment, grounded in Phase 4 totals:

  "Signal accuracy for [topic]: [TOTAL score]/100 — [STRONG (>=75) / ADEQUATE (50-74) / WEAK (<50)]"

Do not introduce new observations. Reference Phase 4 TOTAL row only.

PHASE 6 SEAL — confirm before proceeding to Phase 7:
  [ ] Verdict sentence present in the required format
  [ ] Score drawn from Phase 4 TOTAL (not recalculated here)
  [ ] Tier label correct for stated score
All items confirmed? PHASE 6 COMPLETE.

---

PHASE 7 — GAP ANALYSIS
For each namespace scoring W or P in Phase 3, and each empty namespace where absence is material:

| Gap (signal type absent) | Namespace | Skill to run | Would have surfaced | Changed commit? YES / NO |
|--------------------------|-----------|-------------|---------------------|--------------------------|
| [type] | [namespace] | [exact skill, e.g., /flow-resilience] | [one sentence] | [verdict] |

"Gather more data" does not satisfy the Skill column. Name an exact skill.
If no gaps: "No gaps — signal coverage was sufficient for this commit decision."

Use this template exactly:
  > **Recommendation**: Addresses [Gap: name / Echo: pattern name] by [specific practice change].

PHASE 7 SEAL — confirm before proceeding to Phase 8:
  [ ] Every W or P namespace from Phase 3 has a gap row (or explicit "no gaps")
  [ ] Skill column: exact named skill per row (not generic)
  [ ] Changed commit: YES or NO per row
  [ ] Recommendation template present
All items confirmed? PHASE 7 COMPLETE.

---

PHASE 8 — CALIBRATION TREND

| Prior retro (topic / date) | Prior score | This score | Delta | Trend |
|---------------------------|-------------|------------|-------|-------|
| [reference or "none"] | | | | ↑ improving / ↓ degrading / = stable |

No prior retro: "First retro for this topic — this score establishes the calibration baseline."

PHASE 8 SEAL — confirm before proceeding to Phase 9:
  [ ] Prior retro: named or "none"
  [ ] This score matches Phase 4 TOTAL
  [ ] Trend label present (or "first retro" statement)
All items confirmed? PHASE 8 COMPLETE.

---

PHASE 9 — ECHO → SIGNAL DESIGN

| Echo finding (from Phase 1) | Pattern (from Phase 1) | Proposed change | Change type |
|-----------------------------|------------------------|----------------|-------------|
| [finding] | [pattern name — must match Phase 1] | [specific change] | new skill / rubric amendment / threshold adjustment |

PHASE 9 SEAL — retro complete when confirmed:
  [ ] Echo finding matches Phase 1 (not paraphrased)
  [ ] Pattern matches Phase 1 Pattern entry (same name)
  [ ] Proposed change: specific (not "gather more data")
  [ ] Change type: one of the three options
All items confirmed? RETRO COMPLETE.

---

Execute phases in order: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9.
Each phase seal is a self-containedness contract — the phase cannot defer required fields to a later phase or continuation. A phase that cannot pass its own seal is incomplete: do not proceed until it passes.
```

---

## V-03 — Conversational: Phrasing Register with Inline [REQUIRED] Markers

**Axis:** Phrasing register — conversational imperative prose rather than formal phase headers, with `[REQUIRED]` markers at every required field position. Both C-18 and C-19 are addressed via inline enforcement rather than structural columns or seal checklists.

**Hypothesis:** Conversational register tests whether C-18/C-19 survive a less mechanical framing. `[REQUIRED]` markers inline create the same prevention-of-silent-omission as columns and seals, but through a different signal: blank markers are visible at any truncation point because the prompt named them explicitly. If this variation scores lower than V-01/V-02, it confirms that columns and seals outperform inline markers at preventing omission — a clear rubric insight.

---

```
You're running a post-commitment retrospective for: $ARGUMENTS

A feature shipped. Walk through what the signals said, what actually happened, what was missed, and what the one unexpected thing was. Every field marked [REQUIRED] must be populated before moving to the next section — leave none blank.

{{#if amend}}Scope this retro to: {{amend}} only.{{/if}}

---

Start with the Echo.

The Echo is the one thing that happened after the feature shipped that no gathered signal predicted and no one named as a risk before the commit. It is not a wrong prediction — it is genuinely new. It is also not something the baseline assumption would have predicted.

Search simulations/{namespace}/ for everything tied to this topic. List the post-ship outcomes. Cross them against the predictions in your signal artifacts. Cross them against any named risks or known unknowns. What remains is Echo territory.

Pick the one finding with the highest impact on what the commit decision should have been.

Write the Echo entry now. All four fields are required before continuing.

Echo: [REQUIRED — one sentence describing the finding. Not "nothing was missed." Not a paraphrase of a wrong prediction.]
Nearest signal: [REQUIRED — name the closest artifact, or write "none"]
Commit relevance: [REQUIRED — HIGH if it would have changed the commit, MEDIUM if it would have added conditions, LOW if informational only]
Pattern: [REQUIRED — use this format exactly: **Pattern**: [name] — [description of the recurring failure mode this Echo represents, not just this instance]. Examples: adoption-assumption-gap — team systematically assumes adoption follows from delivery; integration-surface-miss — boundary behavior not validated before commit; timing-signal-gap — time-sensitive dependencies consistently missed; scale-behavior-gap — real-world load not stress-tested. Name your own if none fit.]

If all post-ship outcomes were within signal bounds, write: "No Echo — all post-ship outcomes were within signal bounds." The Pattern field still required: name the pattern that explains why signals were collectively sufficient.

This entry is locked. You will not change it. If your accuracy analysis would suggest a different Echo, write a conflict note immediately after the accuracy table — do not revise this entry.

---

Now inventory the signals. [REQUIRED — list every artifact before continuing to the comparison section]

List every artifact gathered before the commit. One row per file.

| Namespace | Artifact | Date | Prediction summary |
|-----------|----------|------|--------------------|
| [name] | [filename] | [YYYY-MM-DD] | [one phrase] |

State the coverage:
  Namespaces with signals: [REQUIRED — list them]
  Empty namespaces: [REQUIRED — list which of the 9 (scout, draft, review, flow, trace, prove, listen, program, topic) have nothing]
  Total: [REQUIRED — N signals across M namespaces]

---

Now compare predictions to outcomes. [REQUIRED — every row must have non-blank Predicted, Actual, and Match before continuing]

For each namespace in your inventory, state what the signals predicted would happen post-ship and what actually happened.

| Namespace | Predicted | Actual | Match |
|-----------|-----------|--------|-------|
| [name] | [REQUIRED — cannot be blank] | [REQUIRED — cannot be blank] | [C / P / W / ND] |

C = Correct, P = Partial (direction right, magnitude or timing off), W = Wrong, ND = No post-ship data yet.

If your analysis here would revise the Echo entry above, write this note before the accuracy table:
  > Echo-accuracy conflict: [which finding creates tension] — [what the Echo would become]. Original Echo preserved.
Write this note only if conflict exists. Do not alter the Echo entry.

Now score each namespace: [REQUIRED — every namespace row and TOTAL row before continuing]

| Namespace | C | P | W | ND | Score: (C×100 + P×50) ÷ (C+P+W) |
|-----------|---|---|---|-----|----------------------------------|
| [name] | | | | | |
| TOTAL | | | | | |

ND entries excluded from denominator. Leave Score blank if denominator = 0.

State the verdict: [REQUIRED]
  "Signal accuracy for [topic]: [TOTAL]/100 — [STRONG (>=75) / ADEQUATE (50-74) / WEAK (<50)]"

Calibration: [REQUIRED] "[prior retro score] → [this score]: [improving / degrading / stable]" or "First retro — this score is the baseline."

---

Now identify the gaps. [REQUIRED — at least one row or explicit "no gaps" before continuing]

A gap is a signal you didn't gather that would have changed the commit decision.

| Gap (signal type) | Namespace | Skill to run | Would have surfaced | Changed commit? |
|-------------------|-----------|-------------|---------------------|-----------------|
| [type] | [ns] | [REQUIRED — exact skill name, e.g., /flow-throttle] | [one sentence] | YES / NO |

No generic skill names. Every Skill cell must be a real Signal skill.
If there are no gaps, write: "No gaps — signal coverage was sufficient for this commit."

> **Recommendation**: Addresses [Gap: name / Echo: pattern name] by [specific practice change].

---

Record the calibration trend. [REQUIRED — table row and trend before continuing]

| Reference retro | Prior score | This score | Delta | Trend |
|-----------------|-------------|------------|-------|-------|
| [topic / date, or "none"] | | | | ↑ / ↓ / = |

No prior retro: "First retro for this topic."

---

Close with the signal design change. [REQUIRED — all four fields before this retro is complete]

The Echo told you something new. The Pattern you named tells you which class of gap this represents. Translate that into one concrete practice change.

| Echo finding | Pattern | Proposed change | Change type |
|-------------|---------|----------------|-------------|
| [REQUIRED — from Echo entry above, not paraphrased] | [REQUIRED — must match Pattern from Echo entry exactly] | [REQUIRED — specific, not "gather more data"] | [REQUIRED — new skill / rubric amendment / threshold adjustment] |

---

Order: Echo entry (with Pattern) → Signal inventory → Predictions vs actuals (with conflict check before accuracy table if applicable) → Gaps → Calibration trend → Signal design.

Every [REQUIRED] field must be populated in the section where it appears. A retro with blank [REQUIRED] fields is incomplete regardless of where truncation occurs.
```

---

## V-04 — Role+Pattern: Five Roles with Dedicated Pattern Classifier

**Axes:** Role sequence + C-18 pattern taxonomy — adds a Pattern Classifier role between Echo Finder and Scorer; the Scorer cannot receive the handoff until the Pattern Classification is complete.

**Hypothesis:** A dedicated Pattern Classifier role enforces C-18 at a role boundary, the same way the Conflict Auditor role in R3-V-04 enforces C-14. Role boundaries are more visible than inline field omissions: a missing role block is structurally absent, not just a blank field. The Scorer receiving `Signal Registry + Echo Record + Pattern Classification` as an input contract means a retro cannot reach accuracy scoring without a named pattern. C-19 is addressed by the handoff protocol — each role's output is complete before the next role begins.

---

```
Run topic-retro for: $ARGUMENTS

Five roles execute in sequence. Each role receives only what prior roles produced. No role may revise a prior role's output — if analysis creates conflict with a prior role's output, the conflict is logged, not the output revised.

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
The Echo Finder identifies what the signals failed to predict. Does not score accuracy. Does not classify systemic patterns — that is Role 3's responsibility.

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

The Echo Record is final after Role 2. Roles 3, 4, and 5 may reference it but may not change it.
If Role 4 analysis would change the Echo, Role 5 — the Conflict Auditor — will record the tension.

→ Hand Signal Registry (Role 1) + Echo Record (Role 2) to Role 3.

---

ROLE 3 — THE PATTERN CLASSIFIER
The Pattern Classifier receives: Signal Registry (from Role 1) + Echo Record (from Role 2).
The Pattern Classifier answers one question: which repeating systemic failure mode does this Echo represent?

Task:
  Step 1 — Read the Echo Record from Role 2.
  Step 2 — Classify the Echo to a named failure mode from this taxonomy:
    adoption-assumption-gap     — team assumed adoption follows from quality or availability
    integration-surface-miss    — component boundary behavior (API, event, state) not validated
    timing-signal-gap           — timing dependency or sequencing not surfaced by any signal
    scale-behavior-gap          — behavior at real-world load or data scale not predicted
    dependency-chain-miss       — upstream/downstream dependency not traced by any signal
    unknown-unknown             — no available Signal skill covers this class of finding
    other: [name]               — name a distinct repeating failure category

  Step 3 — If the Echo is "No Echo — all post-ship outcomes were within signal bounds", classify as:
    no-echo-sufficient          — signals covered all outcomes; no systemic gap identified

Pattern Classification (locked before Role 4 runs):
  > **Pattern**: [name from taxonomy or "other: [name]"] — [description of the recurring failure mode, not just this Echo instance]
  EVIDENCE: [one sentence explaining why this Echo fits this pattern category, not just a restatement]
  DESIGN IMPLICATION: [which Signal skill class or rubric change addresses this pattern broadly]

The Pattern Classification is final after Role 3. Roles 4 and 5 may reference it but may not change it.

→ Hand Signal Registry (Role 1) + Echo Record (Role 2) + Pattern Classification (Role 3) to Role 4.

---

ROLE 4 — THE SCORER
The Scorer receives: Signal Registry (Role 1) + Echo Record (Role 2) + Pattern Classification (Role 3).
The Scorer may not revise the Echo Record or Pattern Classification.

Step A — Predicted vs Actual
For each namespace with Signal Registry artifacts:

| Namespace | Predicted (signals' collective claim) | Actual (post-ship observation) | Match: C / P / W / ND |
|-----------|--------------------------------------|-------------------------------|----------------------|
| [name] | [required] | [required] | [verdict] |

Both columns must be explicit. A verdict without both sides is invalid.

Step B — Namespace Accuracy

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

Use this template:
  > **Recommendation**: Addresses [Gap: name / Echo: pattern name] by [specific practice change].

→ Hand all prior outputs to Role 5.

---

ROLE 5 — THE CONFLICT AUDITOR
The Conflict Auditor receives: all prior role outputs.
This role is mandatory. It always produces one of two outputs.

Task:
  Primary question — Does any Role 4 finding (Step A verdicts, Step B scores) suggest the Echo Record from Role 2 should name a different finding?
  Secondary question — Does the Pattern Classification from Role 3 correctly represent the Echo's failure class, given the full accuracy picture from Role 4?

If conflict exists for either question — emit:
  CONFLICT DETECTED (Role 5 — Conflict Audit)
  Source: [Role 4 Step A / Step B / Pattern Classification — which finding creates tension]
  Analysis: [what the data suggests should change]
  Resolution: Echo Record (Role 2) and Pattern Classification (Role 3) are preserved as locked. This entry is the conflict artifact.

If no conflict — emit:
  CONFLICT AUDIT COMPLETE: No conflict. Role 4 findings are consistent with Role 2 Echo Record and Role 3 Pattern Classification.

The Conflict Auditor's output is the final section of this retro.

---

Final output order: Echo Record (Role 2) → Pattern Classification (Role 3) → Signal Registry (Role 1) → Scorer output (Role 4: Steps A, B, C) → Conflict Auditor output (Role 5).

Echo Record precedes all accuracy scoring. Pattern Classification follows Echo — it is part of the Echo context, not the accuracy context. Conflict Auditor follows all scoring. This sequencing is enforced by role handoffs: each role cannot begin until it receives its inputs, and inputs are only available after prior roles complete.
```

---

## V-05 — Seal+Inertia: Phase Seals Combined with Baseline Comparison

**Axes:** C-19 via phase seal checklist + inertia framing — every phase ends with a seal, and the accuracy phase includes a baseline comparison column that surfaces signal lift over default-assumption decisions.

**Hypothesis:** Phase seals (V-02 mechanism) combined with inertia framing (R3-V-05 mechanism) create double-layer C-19 pressure. The seal prevents any phase from exiting without all required fields. The baseline column adds a second required output per accuracy row (baseline score alongside signal score) — when two required columns must be populated, the Actual observation cannot be deferred without producing two visibly blank cells. C-18 is addressed by the seal for Phase 0 (the Echo phase seal requires the Pattern field), and the signal design phase propagates the pattern. This variation tests whether multiple independent compliance mechanisms outperform a single strong mechanism.

---

```
Post-commitment retrospective for: $ARGUMENTS

This retro is structured against a counterfactual: what would the team have decided without signal gathering? Every accuracy row includes a baseline comparison — signals that matched the default assumption added no lift. Each phase ends with a PHASE SEAL confirming all required fields are populated.

{{#if amend}}AMEND: {{amend}} — all phases stay within this constraint.{{/if}}

---

PHASE 0 — ECHO
Run this phase before examining any signal predictions.

The Echo is the single post-ship observable satisfying all three tests:
  Test 1: Not predicted by any gathered signal, even partially
  Test 2: Not a named risk or acknowledged unknown at commit time — and not what the default team assumption would have predicted either
  Test 3: Observable only after the feature shipped

Search simulations/{namespace}/ for all artifacts for this topic.
Procedure: list post-ship outcomes → eliminate those predicted by signals → eliminate those the baseline assumption would have predicted → select the highest-commit-impact remaining outcome.
If none qualify: Echo = "No Echo — all post-ship outcomes were within signal or baseline bounds."

Output this table with the Revision log column pre-filled:

| Echo (one sentence) | Nearest signal | Baseline predicted it? YES / NO | Commit relevance | Revision log |
|---------------------|----------------|--------------------------------|-----------------|--------------|
| [finding] | [artifact or "none"] | YES / NO | HIGH / MEDIUM / LOW | LOCKED — no revisions |

Immediately after the table, name the systemic pattern:
  > **Pattern**: [name] — [description of the recurring failure mode this Echo represents, not just this instance]

Pattern examples: adoption-assumption-gap, integration-surface-miss, timing-signal-gap, scale-behavior-gap, dependency-chain-miss, unknown-unknown, or other: [name].

LOCK: Echo cell, Baseline column, and Pattern entry do not change.
Revision log cell updates if Phase 2 creates tension:
  Update to: "[Phase 2 finding]: analysis suggests Echo should be [X]. Original Echo preserved."
The Revision log cell is the definitive conflict record for this retro.

PHASE 0 SEAL — confirm before proceeding to Phase 1:
  [ ] Echo: one sentence (or "No Echo" statement)
  [ ] Nearest signal: named or "none"
  [ ] Baseline predicted it: YES or NO
  [ ] Commit relevance: HIGH, MEDIUM, or LOW (or N/A with No Echo)
  [ ] Revision log: "LOCKED — no revisions" (pre-filled)
  [ ] Pattern entry: present in > **Pattern**: [name] — [description] format (not blank)
All items confirmed? PHASE 0 COMPLETE.

---

PHASE 1 — SIGNAL INVENTORY
List every artifact gathered before commit, grouped by namespace, with baseline assumption surfaced.

| # | Namespace | Artifact | Date | Prediction | Baseline assumption (what team assumed without this signal) |
|---|-----------|----------|------|------------|-------------------------------------------------------------|
| 1 | [name] | [file] | [date] | [one phrase] | [what the team would have assumed absent this signal] |

Coverage:
  Namespaces with signals: [list]
  Empty namespaces (scout, draft, review, flow, trace, prove, listen, program, topic): [list empty]

PHASE 1 SEAL — confirm before proceeding to Phase 2:
  [ ] Every artifact from simulations/ for this topic is listed
  [ ] Every row has a Baseline assumption populated (not blank)
  [ ] Empty namespace list accounts for all 9
All items confirmed? PHASE 1 COMPLETE.

---

PHASE 2 — PREDICTED VS ACTUAL + NAMESPACE ACCURACY

Step A — Match comparison with baseline:

| Namespace | Signal prediction | Baseline assumption | Actual outcome | Signal match: C/P/W/ND | Baseline match: C/P/W/ND |
|-----------|------------------|--------------------|-----------------|-----------------------|--------------------------|
| [name] | [required] | [required] | [required] | [verdict] | [verdict] |

Step B — Echo conflict check. If any row's Actual outcome would revise the Phase 0 Echo, update the Revision log cell in Phase 0 now, then continue.

Step C — Namespace accuracy with inertia lift:

| Namespace | C | P | W | ND | Score: (C×100+P×50)÷(C+P+W) | Baseline score: (C×100+P×50)÷(C+P+W) | Signal lift (signal − baseline) |
|-----------|---|---|---|-----|------------------------------|---------------------------------------|--------------------------------|
| [name] | | | | | | | Δ |
| TOTAL | | | | | | | Δ |

Apply the header formula to both signal and baseline score columns.
ND excluded from denominator. Score blank if denominator = 0.
Positive lift: signals improved on baseline. Negative lift: baseline intuition was more accurate.

Accuracy verdict:
  "Signal accuracy for [topic]: [signal total]/100 — [STRONG (>=75) / ADEQUATE (50-74) / WEAK (<50)]. Baseline: [baseline total]/100. Net lift: Δ[lift]."

Calibration: prior retro → this retro trend, or "First retro — this score and lift are the baseline."

PHASE 2 SEAL — confirm before proceeding to Phase 3:
  [ ] Step A: no Signal prediction, Baseline assumption, or Actual outcome cell is blank
  [ ] Step B: Echo conflict check completed (Revision log updated if tension found, or no-tension noted)
  [ ] Step C: Signal score column populated per formula
  [ ] Step C: Baseline score column populated per formula
  [ ] Step C: Lift column populated (Δ value per row, even if Δ0)
  [ ] TOTAL row present with both signal and baseline scores
  [ ] Accuracy verdict sentence with signal score, baseline score, and lift present
All items confirmed? PHASE 2 COMPLETE.

---

PHASE 3 — GAPS
Missing signals that would have changed the commit decision. Prioritize gaps where both signals AND baseline missed — highest-leverage areas.

| Gap signal | Namespace | Skill to run | Would have surfaced | Signal missed? YES/NO | Baseline missed? YES/NO | Changed commit? YES/NO |
|-----------|-----------|-------------|---------------------|----------------------|------------------------|----------------------|
| [type] | [ns] | [exact skill name] | [one sentence] | [verdict] | [verdict] | [verdict] |

Tier 1 — Both signal and baseline missed, commit impact YES: [list]
Tier 2 — Baseline missed, signal would have caught, commit impact YES: [list]
Tier 3 — Confidence builders (commit impact NO): [list]

No generic skill names. Exact Signal skill required.
No gaps: "No gaps — signal coverage was sufficient."

Use this template:
  > **Recommendation**: Addresses [Gap: name / Echo: pattern name] by [specific practice change].

PHASE 3 SEAL — confirm before proceeding to Phase 4:
  [ ] Every W or P namespace from Phase 2 Step A has a gap row (or explicit "no gaps")
  [ ] Skill column: named exact skill per row
  [ ] Changed commit: YES or NO per row
  [ ] Tier classification present
  [ ] Recommendation template present
All items confirmed? PHASE 3 COMPLETE.

---

PHASE 4 — CALIBRATION TREND

| Reference retro | Signal score | Baseline score | This signal score | This baseline score | Signal trend | Lift trend |
|-----------------|-------------|----------------|------------------|---------------------|:------------:|:----------:|
| [topic / date or "none"] | | | | | ↑/↓/= | ↑/↓/= |

No prior retro: "First retro — signal and baseline scores are the starting calibration."

PHASE 4 SEAL — confirm before proceeding to Phase 5:
  [ ] Reference retro: named or "none"
  [ ] Both this-retro scores match Phase 2 Step C TOTAL rows
  [ ] Signal trend and Lift trend labeled (or "first retro" statement)
All items confirmed? PHASE 4 COMPLETE.

---

PHASE 5 — ECHO → SIGNAL DESIGN

| Echo (from Phase 0) | Pattern (from Phase 0) | Baseline also missed it? YES/NO | Proposed change | Change type |
|---------------------|------------------------|--------------------------------|----------------|-------------|
| [finding] | [named category — must match Phase 0 Pattern exactly] | [verdict] | [specific change] | new skill / rubric amendment / threshold |

If baseline also missed it, the proposed change addresses a genuine blind spot — neither prior experience nor signals covered it.

PHASE 5 SEAL — retro complete when confirmed:
  [ ] Echo matches Phase 0 (not paraphrased)
  [ ] Pattern matches Phase 0 Pattern entry (same named category)
  [ ] Baseline missed it: YES or NO
  [ ] Proposed change: specific (not "gather more data")
  [ ] Change type: one of the three options
All items confirmed? RETRO COMPLETE.

---

Output order: Phase 0 (Echo) → Phase 1 (Inventory) → Phase 2 (Accuracy, with conflict check at Step B) → Phase 3 (Gaps) → Phase 4 (Trend) → Phase 5 (Design).
Each phase seal is a self-containedness contract — the phase cannot defer required fields to a later phase or continuation turn. The Revision log column in Phase 0 is the definitive conflict record. The baseline columns throughout make signal lift measurable, not implied.
```

---

## Summary Table

| ID | Primary Axis | C-18 Mechanism | C-19 Mechanism | Hypothesis Tested |
|----|-------------|----------------|----------------|-------------------|
| V-01 | C-18: named pattern column in Echo table | Pattern column with taxonomy; format enforced: [name] — [recurring failure description]; propagates to Phase 9 | Not primary target — table-row structure inherits C-19 compliance from R5-V01 | Column structure makes C-18 unskippable — same mechanism that earns C-14 in R5-V01 now applied to pattern naming |
| V-02 | C-19: phase seal checklist per phase | Pattern entry required in Phase 1 Seal (> **Pattern**: format) | Each phase ends with a named-field checklist; phase cannot exit until all items confirmed | Phase seals make self-containedness verifiable at every boundary — a truncated phase produces a visible incomplete seal |
| V-03 | Phrasing register: conversational imperative | [REQUIRED] inline marker at Pattern field with format instruction | [REQUIRED] markers at every required field; blank markers visible at any truncation point | Conversational register + inline markers tests whether C-18/C-19 survive without structural columns or seals — if not, confirms structural enforcement superiority |
| V-04 | Role sequence: Pattern Classifier as dedicated fifth role | Role 3 (Pattern Classifier) is required before Scorer receives handoff; produces locked Pattern Classification | Role handoff protocol enforces phase completeness — each role output complete before next role begins | A dedicated pattern role enforces C-18 at a handoff boundary; missing role block is structurally absent, not just a blank field |
| V-05 | C-19 seals + inertia framing (combined) | Phase 0 seal requires Pattern entry; Phase 5 design table propagates pattern | Every phase has a seal; baseline columns add a second required output per accuracy row — two blank cells more visible than one | Double-layer compliance: seals prevent deferral; baseline columns create additional required outputs that cannot be skipped without producing visibly incomplete rows |
