Scorecard written to `simulations/quest/scorecards/topic-retro-scorecard-R5-2026-03-16.md`.

---

**Round 5 Summary**

| Variation | Score | Aspirational |
|-----------|-------|--------------|
| V-02 Table-dominant | 100 | 10/10 |
| V-03 Conversational | 100 | 10/10 |
| V-04 Evidence Steward | 100 | 10/10 |
| V-05 Status-quo foil | 100 | 10/10 |
| V-01 Forensic auditor | 98 | 8/10 |

**Four-way tie at 100.** All essential criteria passed across all five variations — the v5 rubric's C-17 (LOCKED label) and C-18 (named phases) were already satisfied by every variation that used the formula-in-header pattern from prior rounds. V-01's only misses: its Phase 3 template shows no Score column, making C-13 and C-15 structural fails even though the formula is correctly specified as a prose label.

**Two new excellence patterns extracted:**
- **C-19 candidate**: Explicit phase boundary markers (`Phase boundary: Echo is now immutable.`) from V-04 — makes phase-sealing an auditable event, not just a numbered header
- **C-20 candidate**: Status-quo foil table from V-05 — required counterfactual section that makes signal ROI and Echo feedback cost-of-inaction explicit

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Explicit phase boundary markers after each phase create machine-readable transition checkpoints -- V-04's 'Phase boundary: Echo is now immutable. Proceed to Phase 2.' makes phase-sealing an auditable event beyond phase numbering alone", "Status-quo foil as a structural table section grounds Echo feedback in demonstrated cost -- V-05's Part B counterfactual ('Without This Retro' vs 'With This Retro') makes C-10 actionability concrete by showing what the default assumption would have missed"]}
```
---|-----------|---------|----------|
| C-09 | Calibration trend surfaced | PASS | "Calibration (if prior retro provided)" section is structurally present |
| C-10 | Echo feeds back into signal design | PASS | "Echo Feedback Loop" section: "Not 'we learned X' -- but 'therefore, skill Y should be amended / rubric Z should add criterion'" |
| C-11 | Per-namespace accuracy uses explicit numeric formula | PASS | "Accuracy column header: `Score: (C x100 + P x50) / (C+P+W)  [e.g. C=2, P=1, W=1 -> 62.5]`" explicitly stated |
| C-12 | Echo phase precedes accuracy scoring | PASS | Phase 1 (Echo) structurally precedes Phase 3 (Accuracy) |
| C-13 | Formula embedded in column header itself | FAIL | "Accuracy column header:" is prose labeling -- the Phase 3 artifact table template shows Namespace / Artifact / Outcome / Result / Revision Log but no Score column; formula is not embedded in an actual table column header |
| C-14 | Echo-accuracy conflict explicitly named | PASS | Phase 5 mandatory table; "If no tension exists: state explicitly: 'No conflict detected. Echo preserved as written.'" |
| C-15 | Column header includes worked example | FAIL | Example `[e.g. C=2, P=1, W=1 -> 62.5]` exists in prose label but no Score column in template table; C-13 fail cascades |
| C-16 | Conflict audit runs unconditionally | PASS | Phase 5: "This phase produces an explicit result in all cases. Silence is not a valid output." Table always emits |
| C-17 | Echo block carries explicit immutability label | PASS | Phase 1 heading is "ECHO (LOCKED)"; output format is `> **ECHO (LOCKED):**` -- LOCKED is a visible structural label |
| C-18 | Output divided into explicitly numbered/named phases | PASS | Phase 1 through Phase 5 with descriptive names: "Phase 1 -- ECHO (LOCKED)", "Phase 2 -- Signal Inventory", etc. |

**Aspirational: 8/10**

### Score

```
composite = (5/5 x 60) + (3/3 x 30) + (8/10 x 10)
          = 60 + 30 + 8
          = 98
```

**Band: GOLDEN** (all essential pass, composite = 98)

---

## V-02 -- Output Format (Table-dominant, formula-anchored columns)

### Essential

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Signal inventory lists every artifact | PASS | PHASE 2 table: # / Namespace / Artifact Name / Date / Prediction; "No omissions" |
| C-02 | Accuracy uses predicted-vs-actual comparison | PASS | PHASE 3: C/P/W column per artifact; namespace subtotals at bottom |
| C-03 | Gap analysis identifies missing signals | PASS | PHASE 4 Gap Registry: Missing Signal Type / Namespace / Consequence / Action columns |
| C-04 | Exactly one Echo | PASS | PHASE 1: single-cell table `| ECHO (LOCKED) |` with one sentence |
| C-05 | Overall accuracy judgment rendered | PASS | PHASE 3 OVERALL row: "Tier: Strong / Adequate / Weak" with computed score |

**Essential: 5/5**

### Recommended

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-06 | Gap signals actionable | PASS | PHASE 4: "Action: Skill / Question / Threshold" column -- specific artifact required |
| C-07 | Accuracy differentiated by namespace | PASS | PHASE 3: namespace subtotal rows before OVERALL; per-namespace breakdown mandatory |
| C-08 | AMEND scope respected | PASS | "AMEND scope provided, include only in-scope artifacts" in PHASE 2; no AMEND -> pass by default |

**Recommended: 3/3**

### Aspirational

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-09 | Calibration trend surfaced | PASS | "Calibration Block (if prior retro available)" with Dimension / This Topic / Prior Retro / Trend table |
| C-10 | Echo feeds back into signal design | PASS | Echo Feedback table: Echo (Locked) / Proposed Change / Target Artifact -- concrete artifact required |
| C-11 | Per-namespace accuracy uses explicit numeric formula | PASS | Formula appears directly in PHASE 3 column header |
| C-12 | Echo phase precedes accuracy scoring | PASS | PHASE 1 (Echo) -> PHASE 3 (Accuracy): structural ordering enforced by phase sequence |
| C-13 | Formula embedded in column header itself | PASS | Header: `Score: (C x100+P x50)/(C+P+W) [e.g. C=2,P=1,W=1 -> 62.5]` -- formula IS the column label |
| C-14 | Echo-accuracy conflict explicitly named | PASS | PHASE 5 table with "Tension with ECHO?" column: "Yes / No" required; Revision Log in PHASE 3 feeds it |
| C-15 | Column header includes worked example | PASS | `[e.g. C=2,P=1,W=1 -> 62.5]` inline in the column header -- inputs and result both visible |
| C-16 | Conflict audit runs unconditionally | PASS | PHASE 5: "This table runs regardless of whether tension exists. If Revision Log was empty, produce one explicit row confirming no conflict." |
| C-17 | Echo block carries explicit immutability label | PASS | PHASE 1 is `| ECHO (LOCKED) |` single-cell table -- LOCKED is the structural header of the Echo block itself |
| C-18 | Output divided into explicitly numbered/named phases | PASS | `### PHASE 1 -- ECHO (LOCKED)` through `### PHASE 5 -- Conflict Audit (Unconditional)` -- numbered and named |

**Aspirational: 10/10**

### Score

```
composite = (5/5 x 60) + (3/3 x 30) + (10/10 x 10)
          = 60 + 30 + 10
          = 100
```

**Band: GOLDEN** (all essential pass, composite = 100)

---

## V-03 -- Phrasing Register (Conversational, first-person team voice)

### Essential

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Signal inventory lists every artifact | PASS | Phase 2: "Make a table. Every artifact the team produced for this topic gets a row. Don't leave any out." |
| C-02 | Accuracy uses predicted-vs-actual comparison | PASS | Phase 3: "For each artifact from Phase 2, write down what actually happened and grade it: C/P/W" |
| C-03 | Gap analysis identifies missing signals | PASS | Phase 4: "name the namespace, name the signal type, and say what you'd do differently next time (which skill to run, what question to ask, what threshold to check)" |
| C-04 | Exactly one Echo | PASS | Phase 1: `> **ECHO (LOCKED):** ___` -- single sentence, framed before numbers |
| C-05 | Overall accuracy judgment rendered | PASS | Phase 3: "give an overall judgment -- is the team's signal accuracy Strong, Adequate, or Weak, and what's the number behind that?" |

**Essential: 5/5**

### Recommended

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-06 | Gap signals actionable | PASS | Phase 4: "which skill to run, what question to ask, what threshold to check. 'We should have more signals' isn't useful here." |
| C-07 | Accuracy differentiated by namespace | PASS | Phase 3: "compute a score per namespace" explicitly required |
| C-08 | AMEND scope respected | PASS | "If you're working within a narrowed scope (AMEND), only list the in-scope artifacts" in Phase 2 |

**Recommended: 3/3**

### Aspirational

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-09 | Calibration trend surfaced | PASS | "Calibration (if you have a prior retro)" section present |
| C-10 | Echo feeds back into signal design | PASS | "What Does the Echo Tell Us to Change?" section: "Translate it into one concrete change: amend a skill, adjust a rubric criterion, shift a threshold" |
| C-11 | Per-namespace accuracy uses explicit numeric formula | PASS | Phase 3 column header: `Score: (C x100+P x50)/(C+P+W) [e.g. C=2,P=1,W=1 -> 62.5]` |
| C-12 | Echo phase precedes accuracy scoring | PASS | Phase 1 (Echo) before Phase 3 (Accuracy); "Do this before you look at any numbers" |
| C-13 | Formula embedded in column header itself | PASS | Phase 3 table shows header: `Score: (C x100+P x50)/(C+P+W) [e.g. C=2,P=1,W=1 -> 62.5]` as the column label |
| C-14 | Echo-accuracy conflict explicitly named | PASS | Phase 5: "If yes: don't revise it -- write down the tension here. If no: write that explicitly too. Silence doesn't count." |
| C-15 | Column header includes worked example | PASS | `[e.g. C=2,P=1,W=1 -> 62.5]` in the column header -- both formula and example in one label |
| C-16 | Conflict audit runs unconditional | PASS | Phase 5: "*This phase runs no matter what. Even if you think nothing conflicts with the Echo.*" + explicit table with "No conflict -- Echo stands" state |
| C-17 | Echo block carries explicit immutability label | PASS | `> **ECHO (LOCKED):** ___` -- LOCKED is in the output format; "You don't get to revise it later" |
| C-18 | Output divided into explicitly numbered/named phases | PASS | Phase 1 -- ECHO (LOCKED) through Phase 5 -- Conflict Audit; numbered and descriptively named |

**Aspirational: 10/10**

### Score

```
composite = (5/5 x 60) + (3/3 x 30) + (10/10 x 10)
          = 60 + 30 + 10
          = 100
```

**Band: GOLDEN** (all essential pass, composite = 100)

---

## V-04 -- Combined Axes: Role Sequence + Lifecycle Emphasis (Evidence Steward)

### Essential

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Signal inventory lists every artifact | PASS | Phase 2: "The Steward certifies that no known artifact is omitted." |
| C-02 | Accuracy uses predicted-vs-actual comparison | PASS | Phase 3 Layer A: artifact-level C/P/W per row; Layer C: aggregate judgment |
| C-03 | Gap analysis identifies missing signals | PASS | Phase 4: "Generic entries ('should gather more') fail Steward standards. Each gap must specify namespace, signal type, and a concrete next action." |
| C-04 | Exactly one Echo | PASS | Phase 1: `> **ECHO (LOCKED):** [One sentence. The genuinely unexpected thing. Sealed at this phase boundary.]` |
| C-05 | Overall accuracy judgment rendered | PASS | Phase 3 Layer C: "State the ratio, the composite score (formula above applied to totals), and the overall tier" |

**Essential: 5/5**

### Recommended

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-06 | Gap signals actionable | PASS | Phase 4: "Corrective Action (Skill / Question / Threshold)" column required |
| C-07 | Accuracy differentiated by namespace | PASS | Phase 3 Layer B: "Do not collapse namespaces into a single number" -- per-namespace table explicit |
| C-08 | AMEND scope respected | PASS | "If AMEND scope is active, note it here and restrict to in-scope artifacts only" in Phase 2 |

**Recommended: 3/3**

### Aspirational

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-09 | Calibration trend surfaced | PASS | Calibration section with Metric / This Topic / Prior Retro / Trend table |
| C-10 | Echo feeds back into signal design | PASS | Echo Feedback section: "concrete artifact proposal... State what changes as a result." Table: Locked Echo / Proposed Change / Type / Target |
| C-11 | Per-namespace accuracy uses explicit numeric formula | PASS | Phase 3 Layer B column header: `Score: (C x100+P x50)/(C+P+W) [e.g. C=2,P=1,W=1 -> 62.5]` |
| C-12 | Echo phase precedes accuracy scoring | PASS | Phase 1 boundary sealed before Phase 3 begins; "Proceed to Phase 2" after Echo capture |
| C-13 | Formula embedded in column header itself | PASS | Layer A AND Layer B both carry `Score: (C x100+P x50)/(C+P+W) [e.g. C=2,P=1,W=1 -> 62.5]` as column headers |
| C-14 | Echo-accuracy conflict explicitly named | PASS | Phase 5: Revision Log Entry / Conflict With Echo? / Disposition table; always runs |
| C-15 | Column header includes worked example | PASS | Both Layer A and Layer B headers include `[e.g. C=2,P=1,W=1 -> 62.5]` -- formula + example inline |
| C-16 | Conflict audit runs unconditionally | PASS | Phase 5: "Unconditional -- Steward runs this regardless of perceived tension"; "produce one explicit row: 'No tension detected. Echo preserved as written.'" |
| C-17 | Echo block carries explicit immutability label | PASS | Phase 1 section header: "Echo Capture (LOCKED)"; output format: `> **ECHO (LOCKED):**`; "Phase boundary: Echo is now immutable." |
| C-18 | Output divided into explicitly numbered/named phases | PASS | Phase 1 -- Echo Capture through Phase 5 -- Conflict Audit; each has a named phase boundary marker |

**Aspirational: 10/10**

### Score

```
composite = (5/5 x 60) + (3/3 x 30) + (10/10 x 10)
          = 60 + 30 + 10
          = 100
```

**Band: GOLDEN** (all essential pass, composite = 100)

---

## V-05 -- Combined Axes: Output Format + Inertia Framing (Status-Quo Foil)

### Essential

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Signal inventory lists every artifact | PASS | Phase 2: "Zero omissions." |
| C-02 | Accuracy uses predicted-vs-actual comparison | PASS | Phase 3: C/P/W per artifact; "Overall accuracy: [ratio] -> [score] -> [tier]" |
| C-03 | Gap analysis identifies missing signals | PASS | Phase 4 Part A Gap Registry: Missing Signal Type / Namespace / What It Would Have Changed / Action |
| C-04 | Exactly one Echo | PASS | Phase 1: `> **ECHO (LOCKED):** ___` -- single sentence before signal analysis |
| C-05 | Overall accuracy judgment rendered | PASS | Phase 3: "**Overall accuracy:** [ratio] -> [score] -> [tier]" |

**Essential: 5/5**

### Recommended

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-06 | Gap signals actionable | PASS | Phase 4 Part A: "Action: Skill / Question / Threshold" column; gap registry format requires specific action |
| C-07 | Accuracy differentiated by namespace | PASS | Phase 3: "**Namespace accuracy breakdown** (do not skip)" -- per-namespace table with per-namespace scores |
| C-08 | AMEND scope respected | PASS | "(AMEND scope: restrict to in-scope artifacts only if provided)" in Phase 2 |

**Recommended: 3/3**

### Aspirational

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-09 | Calibration trend surfaced | PASS | Calibration section with Metric / This Topic / Prior Retro / Trend table |
| C-10 | Echo feeds back into signal design | PASS | Echo Feedback Loop table: "Proposed Change", "Type", "Target Artifact", "Cost of Inaction (from Foil)" -- foil makes feedback consequential |
| C-11 | Per-namespace accuracy uses explicit numeric formula | PASS | Both Phase 3 artifact table and namespace breakdown table carry formula headers |
| C-12 | Echo phase precedes accuracy scoring | PASS | Phase 1 (Echo) before Phase 3 (Accuracy); "This line does not change after Phase 1." |
| C-13 | Formula embedded in column header itself | PASS | Phase 3 artifact table: `Score: (C x100+P x50)/(C+P+W) [e.g. C=2,P=1,W=1 -> 62.5]`; namespace breakdown carries same header |
| C-14 | Echo-accuracy conflict explicitly named | PASS | Phase 5 table: "Conflict With ECHO (LOCKED)?" column with Yes/No required; Revision Flag column in Phase 3 feeds it |
| C-15 | Column header includes worked example | PASS | `[e.g. C=2,P=1,W=1 -> 62.5]` inline in column header across both Phase 3 tables |
| C-16 | Conflict audit runs unconditionally | PASS | Phase 5: "(Unconditional)"; "If Phase 3 Revision Flag column was blank: produce one row: 'No flags raised. Conflict audit complete. Echo preserved as written.'" |
| C-17 | Echo block carries explicit immutability label | PASS | Phase 1: `> **ECHO (LOCKED):** ___`; "This line does not change after Phase 1." LOCKED is part of the output format |
| C-18 | Output divided into explicitly numbered/named phases | PASS | Phase 1 -- ECHO through Phase 5 -- Conflict Audit; Phase 4 subdivided into Part A and Part B |

**Aspirational: 10/10**

### Score

```
composite = (5/5 x 60) + (3/3 x 30) + (10/10 x 10)
          = 60 + 30 + 10
          = 100
```

**Band: GOLDEN** (all essential pass, composite = 100)

---

## Ranking

| Rank | Variation | Score | Band | Aspirational Passes |
|------|-----------|-------|------|---------------------|
| 1 (tie) | V-02 Table-dominant, formula-anchored | **100** | GOLDEN | 10/10 |
| 1 (tie) | V-03 Conversational team voice | **100** | GOLDEN | 10/10 |
| 1 (tie) | V-04 Evidence Steward, weighted Phase 3 | **100** | GOLDEN | 10/10 |
| 1 (tie) | V-05 Status-quo foil + inertia framing | **100** | GOLDEN | 10/10 |
| 5 | V-01 Forensic auditor, audit-locked Echo | **98** | GOLDEN | 8/10 (fails C-13, C-15) |

**V-01 miss**: "Accuracy column header:" is a prose label; the Phase 3 template table shows Namespace / Artifact / Outcome / Result / Revision Log but no Score column. The formula is specified as a prose instruction, not embedded in an actual column header. C-13 and C-15 fail.

---

## Excellence Signals

**From V-04:**

1. **Explicit phase boundary markers create machine-readable transition checkpoints** -- V-04 closes each phase with `**Phase boundary**: [state]. Proceed to Phase N.`. This makes phase-skipping visually detectable beyond numbered section headers. The boundary marker is declarative: a scorer can verify that the Echo was sealed before Phase 3 began without reading prose instructions. Not yet captured by any criterion.

**From V-05:**

2. **Status-quo foil as a structural table section makes signal ROI explicit** -- V-05 Phase 4 Part B compares "Without This Retro (Status Quo)" vs "With This Retro" across Accuracy Perception / Namespace Blind Spot / Next-Topic Strategy. The counterfactual baseline grounds C-10 in demonstrated cost: the "Cost of Inaction (from Foil)" column in Echo Feedback connects the proposed change to what the status quo loses if the change is not made. The foil is a required table, not a rhetorical device.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Explicit phase boundary markers after each phase create machine-readable transition checkpoints -- V-04's 'Phase boundary: Echo is now immutable. Proceed to Phase 2.' makes phase-sealing an auditable event beyond phase numbering alone", "Status-quo foil as a structural table section grounds Echo feedback in demonstrated cost -- V-05's Part B counterfactual ('Without This Retro' vs 'With This Retro') makes C-10 actionability concrete by showing what the default assumption would have missed"]}
```
