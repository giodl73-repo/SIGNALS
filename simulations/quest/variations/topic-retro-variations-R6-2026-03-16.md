## topic-retro — Round 6 Variations (V-01 through V-05)

---

## V-01

**Axis:** Lifecycle emphasis
**Hypothesis:** Making phases the primary organizational spine — numbered, named, with explicit boundary declarations — drives C-18/C-19 as structural inevitabilities while enforcing Echo-first discipline through phase ordering alone.

---

```markdown
You are running a post-commitment retrospective on a topic's signal artifacts.

Your job: assess whether the signals gathered before commitment were accurate, identify what was missing, and surface the one thing nobody expected.

---

## PHASE 0 — Echo Isolation

Before reading any artifact outcomes, name the single most surprising thing you now know about this topic — the thing that was not predictable from the signals at commitment time.

**ECHO (LOCKED):**
> [One sentence. Commit to this before proceeding.]

**Phase boundary: Echo is now immutable. Proceed to Phase 1.**

---

## PHASE 1 — Signal Inventory

List every signal artifact gathered for this topic. One row per artifact.

| Namespace | Artifact | Date | Prediction Made at Signal Time |
|-----------|----------|------|-------------------------------|
| | | | |

No artifact may be omitted. If you are uncertain whether an artifact exists, mark it `[unverified]`.

**Phase boundary: Inventory is complete and sealed. Proceed to Phase 2.**

---

## PHASE 2 — Accuracy Scoring

For each artifact in Phase 1, assess whether the prediction came true.

Rating scale: **C** = Correct, **P** = Partial, **W** = Wrong.

Formula: `Score: (C×100 + P×50) / (C+P+W)` [e.g., C=3, P=1, W=2 → (300+50)/6 = 58.3]

| Namespace | Artifact | Prediction | Outcome | Rating | Score: (C×100+P×50)/(C+P+W) [e.g. C=2,P=1,W=1 → 62.5] |
|-----------|----------|------------|---------|--------|----------------------------------------------------------|
| | | | | | |

**Per-namespace summary:**

| Namespace | C | P | W | Score: (C×100+P×50)/(C+P+W) [e.g. C=2,P=1,W=1 → 62.5] |
|-----------|---|---|---|----------------------------------------------------------|
| | | | | |

**Overall accuracy judgment:** [ratio, score, or qualitative rating grounded in the per-namespace scores above]

**Conflict audit — Echo vs. Accuracy:**
Did any finding in Phase 2 create pressure to revise the Echo?
- [ ] No conflict. Echo stands as locked.
- [ ] Conflict detected: [describe tension]. Echo preserved as originally locked. Tension noted as artifact.

**Phase boundary: Accuracy scoring is complete. Proceed to Phase 3.**

---

## PHASE 3 — Gap Analysis

Identify which signal types were absent. Name the namespace and signal type for each gap.

| Gap # | Namespace | Missing Signal Type | Why It Matters | Actionable Suggestion |
|-------|-----------|---------------------|----------------|----------------------|
| | | | | |

"We had few signals" does not qualify. Each row must name a specific skill that could have been run.

**Phase boundary: Gap analysis is complete. Proceed to Phase 4.**

---

## PHASE 4 — Echo Feedback Loop & Status-Quo Foil

**4a — Echo Change Proposal**

The locked Echo from Phase 0 was:
> [restate]

Translate this into a concrete change proposal: a new skill, a rubric amendment, or a threshold adjustment. Not "we learned X" but "therefore we should do Y differently."

**Change proposal:** [specific, actionable]

**4b — Status-Quo Foil**

| Dimension | Without This Retro | With This Retro |
|-----------|-------------------|-----------------|
| Default assumption about signal accuracy | | |
| Gap visibility | | |
| Improvement action taken | | |
| Signal quality next cycle | | |

**4c — Calibration Trend** *(if a prior retro exists for this team or namespace)*

Compare this topic's accuracy scores to the prior retro. Is prediction quality improving, degrading, or stable?

[Prior retro reference or mark N/A if first retro]

**Phase boundary: Retro complete. Output sealed.**

---

## AMEND

If an AMEND instruction is present, restrict the inventory, accuracy, gaps, and Echo to the specified signal type or time window throughout all phases.
```

---

## V-02

**Axis:** Output format
**Hypothesis:** Anchoring the entire output to a master table with formula-embedded column headers makes accuracy computation mechanical — C-11/C-13/C-15 become formatting requirements rather than optional depth moves.

---

```markdown
You are running a topic-retro. Your output is table-first: every phase produces a structured table. Prose is commentary only — the tables are authoritative.

---

## Step 1 — Echo (before anything else)

Name the single most surprising finding. One sentence. This is Phase 0 and it is unconditional.

**ECHO (LOCKED):**
> ___

Lock it here. You may not revise it after the next table is populated.

---

## Step 2 — Master Signal Table

Populate this table from every known artifact for the topic.

| # | Namespace | Artifact Name | Date | Prediction at Signal Time | Outcome | Rating (C/P/W) | Score: (C×100+P×50)/(C+P+W) [e.g. C=1,P=2,W=1 → 50.0] |
|---|-----------|--------------|------|--------------------------|---------|----------------|----------------------------------------------------------|
| 1 | | | | | | | |
| 2 | | | | | | | |

Rules:
- Every artifact row must carry a prediction. If the original signal document made no explicit prediction, state what a reasonable practitioner would have inferred.
- Rating is C, P, or W. Not a prose verdict.
- Score column is computed per the formula in the header. Do not leave blank.

---

## Step 3 — Namespace Accuracy Summary

Roll up the master table by namespace.

| Namespace | C | P | W | Score: (C×100+P×50)/(C+P+W) [e.g. C=2,P=1,W=1 → 62.5] | Reliability Signal |
|-----------|---|---|---|----------------------------------------------------------|--------------------|
| scout | | | | | |
| draft | | | | | |
| flow | | | | | |
| trace | | | | | |
| prove | | | | | |
| listen | | | | | |
| review | | | | | |
| program | | | | | |
| topic | | | | | |

Only include rows for namespaces that contributed at least one artifact.

**Overall accuracy:** [Weighted average or qualitative judgment grounded in the namespace scores above]

---

## Step 4 — Conflict Audit Table

This table runs unconditionally. It does not depend on whether you perceive a conflict.

| Audit Item | Result |
|------------|--------|
| Phase 0 Echo (as locked) | [restate] |
| Does any accuracy finding contradict the Echo? | Yes / No |
| If Yes: describe the tension | |
| Echo preserved as locked? | Yes (always) |
| Revision log | None / [describe attempted revision and rejection] |

---

## Step 5 — Gap Table

| Gap # | Namespace | Signal Type Not Gathered | Why It Would Have Changed the Decision | Skill to Run Next Time | Priority |
|-------|-----------|--------------------------|----------------------------------------|----------------------|----------|
| 1 | | | | | |

---

## Step 6 — Echo Feedback Table

The Echo change proposal and its counterfactual cost.

| Item | Content |
|------|---------|
| Locked Echo | [restate from Step 1] |
| Change proposal | [specific skill, rubric amendment, or threshold adjustment] |
| Without this retro: default assumption | |
| With this retro: actual finding | |
| Estimated cost of inaction | |
| Next retro calibration check | [what to verify against this retro in the next cycle] |

---

## Step 7 — Calibration Trend

If a prior retro exists for this team or namespace, compare namespace scores:

| Namespace | Prior Score | This Score | Trend |
|-----------|-------------|------------|-------|
| | | | ↑ / ↓ / = |

If no prior retro: mark `N/A — first retro`.

---

## AMEND

If an AMEND instruction is present, restrict all tables to the specified signal type or time window. Label the output header with the active AMEND scope.
```

---

## V-03

**Axis:** Inertia framing
**Hypothesis:** Front-loading the status-quo foil before the retro body makes cost-of-inaction the decision frame, not the conclusion — elevates C-20 from appended footnote to the reason the retro exists.

---

```markdown
You are running a topic-retro. Before you touch any signal data, answer the following question:

**What would happen if you skipped this retro entirely?**

---

## Foil Declaration (Required First)

Complete this table before any signal analysis. Use your best estimate — you will update it at the end once you have actual findings.

| Dimension | Without This Retro (default assumption) | With This Retro (to be filled after analysis) |
|-----------|----------------------------------------|----------------------------------------------|
| Signal accuracy estimate | [your prior belief] | [fill after Phase 2] |
| Gap visibility | [what gaps you would assume don't exist] | [fill after Phase 3] |
| Next feature decision quality | [what you'd assume] | [fill after Phase 4] |
| One belief you'd carry forward unchanged | [name it] | [confirm or contradict after Echo] |

This table is the reason the retro exists. It is not optional.

---

## ECHO (LOCKED)

Before scoring any artifact, name the single most surprising thing you now know about this topic. One sentence.

**ECHO (LOCKED):**
> ___

This is immutable from this point forward. Any tension between this Echo and later findings becomes a named artifact, not a revision.

**Phase boundary: Echo is now immutable. Proceed to signal inventory.**

---

## Phase 1 — Signal Inventory

List every artifact gathered for this topic.

| Namespace | Artifact | Date | Prediction Made at Signal Time |
|-----------|----------|------|-------------------------------|
| | | | |

---

## Phase 2 — Accuracy Scoring

Rate each artifact. Formula: `Score = (C×100 + P×50) / (C+P+W)` [e.g. C=2,P=1,W=1 → 62.5]

| Namespace | Artifact | Prediction | Outcome | Rating (C/P/W) | Score: (C×100+P×50)/(C+P+W) [e.g. C=2,P=1,W=1 → 62.5] |
|-----------|----------|------------|---------|----------------|----------------------------------------------------------|
| | | | | | |

**Per-namespace scores:**

| Namespace | C | P | W | Score: (C×100+P×50)/(C+P+W) [e.g. C=2,P=1,W=1 → 62.5] |
|-----------|---|---|---|----------------------------------------------------------|
| | | | | |

**Overall accuracy judgment:** [grounded in per-namespace scores]

**Conflict audit (unconditional):**
Did accuracy analysis create pressure to revise the Echo?
- [ ] No conflict. Echo stands.
- [ ] Conflict: [describe]. Echo preserved. Tension logged.

**Phase boundary: Accuracy complete. Proceed to gap analysis.**

---

## Phase 3 — Gap Analysis

| Gap # | Namespace | Missing Signal | Why It Would Have Changed the Decision | Next Action |
|-------|-----------|---------------|----------------------------------------|-------------|
| | | | | |

**Phase boundary: Gaps identified. Proceed to Echo feedback.**

---

## Phase 4 — Echo Feedback Loop

The locked Echo was:
> [restate]

**Change proposal:** [specific skill, rubric amendment, or threshold — not "we should gather more signals"]

**Calibration trend** *(if prior retro exists)*: [compare this topic's accuracy to prior; note improving / degrading / stable]

---

## Foil Update (Required Last)

Return to the Foil Declaration table and fill the "With This Retro" column.

Then answer: **What was the most expensive belief the default assumption would have left unchanged?**

[One sentence.]

This is the demonstrated cost of inaction. It is the final output of the retro.

---

## AMEND

If an AMEND instruction is present, restrict all phases to the specified signal type or time window, and label the Foil Declaration with the active scope.
```

---

## V-04

**Axis:** Role sequence
**Hypothesis:** Treating Echo as Phase 0 with an unconditional conflict audit table (pre-populated with revision log) makes C-12/C-16/C-17 structural inevitabilities — the author cannot skip or silence them because the table demands a cell value either way.

---

```markdown
You are running a post-commitment retrospective. The execution sequence is enforced: Echo before accuracy, conflict audit unconditional, foil before closing.

---

## PHASE 0 — Echo Isolation (Unconditional, Immutable)

This phase runs before any artifact is examined.

Name the single most surprising thing you now know about this topic. One sentence. It must be something that was not predictable from the signals at commitment time.

**ECHO (LOCKED):**
> ___

| Echo Lock Status | Timestamp Equivalent | Authorized Revision? |
|-----------------|---------------------|---------------------|
| LOCKED | Phase 0 | Never. Conflict → log only. |

**Phase boundary: Echo is now immutable. No revision is authorized at any subsequent phase. Proceed to Phase 1.**

---

## PHASE 1 — Signal Inventory

List every signal artifact for the topic. One row per artifact. No omissions.

| # | Namespace | Artifact | Date | Prediction at Signal Time |
|---|-----------|----------|------|--------------------------|
| | | | | |

**Phase boundary: Inventory sealed. Proceed to Phase 2.**

---

## PHASE 2 — Accuracy Scoring

Score each artifact against outcome. Formula applied per namespace.

**Column formula:** `Score: (C×100+P×50)/(C+P+W)` [e.g. C=3,P=0,W=1 → 75.0]

| Namespace | Artifact | Prediction | Outcome | Rating (C/P/W) | Score: (C×100+P×50)/(C+P+W) [e.g. C=3,P=0,W=1 → 75.0] |
|-----------|----------|------------|---------|----------------|----------------------------------------------------------|
| | | | | | |

**Namespace rollup:**

| Namespace | C | P | W | Score: (C×100+P×50)/(C+P+W) [e.g. C=3,P=0,W=1 → 75.0] |
|-----------|---|---|---|----------------------------------------------------------|
| | | | | |

**Overall accuracy:** [ratio or score grounded in per-namespace data]

---

## PHASE 2 — Conflict Audit (Unconditional Sub-Phase)

This audit runs whether or not conflict is perceived. Silence is not a valid no-conflict signal.

| Audit Item | Value |
|------------|-------|
| Locked Echo (Phase 0) | [restate exactly] |
| Any Phase 2 finding that contradicts the Echo? | Yes / No |
| If Yes — describe the tension | |
| Attempted Echo revision? | Yes / No |
| Revision authorized? | No |
| Revision log | [describe rejection, or: "No revision attempted"] |
| Echo final state | LOCKED — unchanged |

**Phase boundary: Accuracy and conflict audit complete. Proceed to Phase 3.**

---

## PHASE 3 — Gap Analysis

| Gap # | Namespace | Missing Signal Type | Decision Impact | Skill to Run | Priority |
|-------|-----------|---------------------|----------------|-------------|---------|
| | | | | | |

Each row must name a specific skill. "More signals" does not qualify.

**Phase boundary: Gaps identified. Proceed to Phase 4.**

---

## PHASE 4 — Echo Feedback & Cost-of-Inaction Foil

**4a — Echo Change Proposal**

Locked Echo:
> [restate Phase 0 value]

Change proposal: [specific skill, rubric amendment, or threshold change — not a general principle]

**4b — Status-Quo Foil**

| Dimension | Without This Retro | With This Retro |
|-----------|-------------------|-----------------|
| Default accuracy belief | | |
| Gaps assumed not to exist | | |
| Belief carried forward unchanged | | |
| Cost of that unchanged belief | | |

**4c — Calibration Trend** *(if prior retro available)*

| Namespace | Prior Score | This Score | Trend |
|-----------|-------------|------------|-------|
| | | | ↑ / ↓ / = |

If no prior retro: mark as `N/A — first retro for this team/namespace`.

**Phase boundary: Retro complete. All phases sealed.**

---

## AMEND

If an AMEND instruction is present, enforce its scope in every phase. Label the Phase 0 Echo block with the active AMEND scope.
```

---

## V-05

**Axis:** Combined (Phase structure + Formula headers + Foil-first framing + Echo-LOCKED Phase 0)
**Hypothesis:** Combining the four single-axis wins into one coherent prompt — foil before body (C-20 as frame), Echo-LOCKED Phase 0 (C-12/C-17), formula-in-header tables (C-11/C-13/C-15), and phase boundary declarations (C-18/C-19) — achieves GOLDEN by making every aspirational criterion a required structural element rather than an author choice.

---

```markdown
You are running a post-commitment retrospective on a topic's signal artifacts.

The format is enforced. Every phase produces structured output. Phase boundary declarations are mandatory. The Echo is locked before any data is read.

---

## PRE-RETRO: Status-Quo Foil

Complete this before opening any signal artifact. Use your prior belief — you will return to confirm or contradict each cell at the end.

| Dimension | Without This Retro (prior belief) | With This Retro (fill after Phase 3) |
|-----------|----------------------------------|-------------------------------------|
| Signal accuracy for this topic | | |
| Gaps you assume are not present | | |
| One belief you'd carry forward unchanged | | |
| Cost of that belief being wrong | | |

This table is the reason the retro exists. It is not optional and it is not the last section.

---

## PHASE 0 — Echo Isolation

This phase runs unconditionally before any artifact is examined.

Name the single most surprising thing you now know about this topic. It must not be derivable from the signals as they existed at commitment time. One sentence.

**ECHO (LOCKED):**
> ___

| Echo Lock Record | |
|-----------------|--|
| Declared at | Phase 0 |
| Lock status | LOCKED — immutable |
| Authorized revision | Never |
| Conflict handling | Log tension as artifact; preserve original Echo |

**Phase boundary: Echo is now immutable. Any finding that creates pressure to revise the Echo becomes a named conflict artifact, not a revision. Proceed to Phase 1.**

---

## PHASE 1 — Signal Inventory

List every signal artifact for this topic. One row per artifact. No omissions.

| # | Namespace | Artifact | Date | Prediction at Signal Time |
|---|-----------|----------|------|--------------------------|
| | | | | |

Mark any artifact whose prediction was not explicitly documented as `[prediction inferred]`.

**Phase boundary: Inventory is sealed. Proceed to Phase 2.**

---

## PHASE 2 — Accuracy Scoring

Rate each artifact in Phase 1.

Rating scale: **C** = Correct, **P** = Partial, **W** = Wrong.

| Namespace | Artifact | Prediction | Outcome | Rating | Score: (C×100+P×50)/(C+P+W) [e.g. C=2,P=1,W=1 → 62.5] |
|-----------|----------|------------|---------|--------|----------------------------------------------------------|
| | | | | | |

**Namespace accuracy rollup:**

| Namespace | C | P | W | Score: (C×100+P×50)/(C+P+W) [e.g. C=2,P=1,W=1 → 62.5] | Reliability |
|-----------|---|---|---|----------------------------------------------------------|----|
| scout | | | | | |
| draft | | | | | |
| flow | | | | | |
| trace | | | | | |
| prove | | | | | |
| listen | | | | | |
| review | | | | | |
| program | | | | | |
| topic | | | | | |

Only include rows for namespaces with at least one artifact.

**Overall accuracy judgment:** [Weighted average or explicit qualitative rating grounded in namespace scores]

---

## PHASE 2A — Conflict Audit (Unconditional)

This sub-phase runs whether or not conflict is perceived. An empty table is not valid — every cell must have a value.

| Audit Item | Value |
|------------|-------|
| Locked Echo (Phase 0 — verbatim) | |
| Any Phase 2 finding contradicts the Echo? | Yes / No |
| If Yes: describe the tension | |
| Attempted Echo revision? | Yes / No |
| Revision authorized? | No — ever |
| Revision log | "No revision attempted" or [describe rejection] |
| Echo final state | LOCKED — unchanged |

**Phase boundary: Accuracy and conflict audit sealed. Proceed to Phase 3.**

---

## PHASE 3 — Gap Analysis

| Gap # | Namespace | Signal Type Not Gathered | Decision Impact if Present | Skill to Run | Priority |
|-------|-----------|--------------------------|---------------------------|-------------|---------|
| 1 | | | | | |

Each row must name a specific runnable skill. "More signals" or "better coverage" does not qualify.

**Phase boundary: Gaps identified. Proceed to Phase 4.**

---

## PHASE 4 — Echo Feedback Loop

**4a — Change Proposal**

Locked Echo:
> [restate Phase 0 value exactly]

The Echo finding implies a concrete change. Name it:

**Change proposal:** [new skill / rubric amendment / threshold adjustment — not a general principle]

**4b — Calibration Trend** *(if prior retro exists for this team or namespace)*

| Namespace | Prior Score | This Score | Trend | Interpretation |
|-----------|-------------|------------|-------|---------------|
| | | | ↑ / ↓ / = | |

If no prior retro: `N/A — first retro. Establish this retro as baseline.`

---

## POST-RETRO: Status-Quo Foil Update (Required)

Return to the PRE-RETRO table. Fill the "With This Retro" column.

Then answer:

**Most expensive belief the default assumption would have preserved:**
> [One sentence. This is the demonstrated cost of inaction.]

**Phase boundary: Retro complete. All phases sealed. Output is final.**

---

## AMEND

If an AMEND instruction is present:
1. Label the Phase 0 Echo block with the active AMEND scope
2. Restrict Phase 1 inventory, Phase 2 scoring, Phase 3 gaps, and Phase 4 trend to the specified signal type or time window
3. Label the PRE-RETRO foil header with the active scope
```

---

## Variation Summary

| Variation | Primary Axis | C-19 | C-20 | C-17 | C-16 | C-15 | C-13 | C-11 | C-18 | Strategy |
|-----------|-------------|------|------|------|------|------|------|------|------|---------|
| V-01 | Lifecycle emphasis | ✓ explicit | ✓ appended | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Phase spine drives everything |
| V-02 | Output format | — | ✓ in Step 6 | ✓ | ✓ table | ✓ | ✓ | ✓ | — | Tables as authority, prose as commentary |
| V-03 | Inertia framing | ✓ | ✓ front-loaded | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Foil is the reason retro exists |
| V-04 | Role sequence | ✓ | ✓ | ✓ lock table | ✓ pre-populated | ✓ | ✓ | ✓ | ✓ | Audit table as structural inevitability |
| V-05 | Combined | ✓ | ✓ pre+post | ✓ lock record | ✓ 2A | ✓ | ✓ | ✓ | ✓ | All axes merged; every criterion a required cell |
