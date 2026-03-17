# quest:score — topic-retro — Round 10 (Rubric v8)

**Trace artifact:** None available — scoring against skill prompt structure and spec.

---

## Scoring Notes

Only **V-01** was provided in full. **V-02** was truncated at Phase 0 header; V-03–V-05 were not included. Scoring proceeds on V-01 in full; V-02 is scored on what is visible (hypothesis + axis only).

---

## V-01 — Axis: Role Sequence

**Hypothesis:** Sealed Phase 0 eliminates hindsight contamination at the source.

### Essential Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Signal inventory lists every artifact | **PASS** | Phase 2 table: namespace, artifact, date, prediction at signal time, C/P/W |
| C-02 | Accuracy uses predicted-vs-actual comparison | **PASS** | Phase 3 populates C/P/W per artifact; explicit C/P/W taxonomy enforced |
| C-03 | Gap analysis identifies missing signals | **PASS** | Phase 4 table requires namespace + signal type per row; "not a generic observation" |
| C-04 | Exactly one Echo | **PASS** | Phase 1 emits exactly one Echo as a single sentence; no list form permitted |
| C-05 | Overall accuracy judgment rendered | **PASS** | Phase 3 requires "Overall accuracy judgment: {ratio or qualitative rating grounded in per-namespace scores}" |

All essential: ✅ 5/5

### Recommended Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-06 | Gap signals actionable | **PASS** | Phase 4 column "Actionable recommendation" with constraint: specific namespace and skill named |
| C-07 | Accuracy differentiated by namespace | **PASS** | Phase 3 per-namespace accuracy table explicit |
| C-08 | AMEND scope respected | **PASS** | Output checklist item: "AMEND scope honored throughout (if provided)" |

All recommended: ✅ 3/3

### Aspirational Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-09 | Calibration trend surfaced | **PASS** | Phase 6 — prior retro comparison table when prior exists |
| C-10 | Echo feeds back into signal design | **PASS** | Phase 5 "Change proposal: specific skill to add, rubric to amend, or threshold to adjust — one concrete action" |
| C-11 | Per-namespace accuracy uses explicit numeric formula | **PASS** | `(C×100 + P×50) / (C+P+W)` stated in Phase 3 |
| C-12 | Echo phase precedes accuracy scoring | **PASS** | Phase 1 (Echo) structurally before Phase 3 (Accuracy); boundary enforced |
| C-13 | Formula embedded in column header | **PASS** | Header: `Score: (C×100 + P×50) / (C+P+W) [e.g. C=2,P=1,W=1 → 62.5]` |
| C-14 | Echo-accuracy conflict explicitly named | **PASS** | Conflict audit checkboxes in Phase 3: explicit no-conflict or conflict-detected paths |
| C-15 | Column header includes worked example | **PASS** | `[e.g. C=2,P=1,W=1 → 62.5]` in Phase 3 header |
| C-16 | Conflict audit runs unconditionally | **PASS** | Labeled "mandatory — runs unconditionally"; checkbox structure forces explicit result |
| C-17 | Echo carries immutability label | **PASS** | `ECHO (LOCKED)` label; `ECHO IS NOW IMMUTABLE.` declarative sentence |
| C-18 | Output divided into numbered/named phases | **PASS** | Phase 0 through Phase 6, each numbered and named |
| C-19 | Explicit phase boundary markers | **PASS** | `Phase boundary: [state]. Proceed to Phase N.` between every phase |
| C-20 | Status-quo foil section | **PASS** | Phase 5 foil table: "Without this retro (default assumption)" vs "With this retro (actual)" |
| C-21 | Multi-field lock artifact | **PASS** | Echo block contains: Finding / Why surprising / Lock time — three named fields |
| C-22 | Prior belief captured before signals opened | **PASS** | Phase 0 explicitly requires completion before any signal artifact is opened |
| C-23 | Phase 0 sealed standalone phase | **PASS** | `PHASE 0 SEALED — no revision permitted after this point.` + dedicated phase boundary |
| C-24 | Foil table uses three named dimensions | **PASS** | Phase 5 rows: (1) Echo finding, (2) Signal accuracy assumption, (3) Signal design default |
| C-25 | Calibration emits baseline when no prior retro | **PASS** | Phase 6 explicit `CALIBRATION BASELINE RECORD` block with "No prior retro available" path |

All aspirational: ✅ 17/17

### V-01 Score

```
aspirational_pass / 17 × 10 = 17/17 × 10 = 10.0
```

**V-01: 100 / 100**

---

## V-02 — Axis: Output Format

**Hypothesis:** Formula + worked example embedded in column header makes scoring self-auditing.

**Status:** Prompt body not provided — truncated after Phase 0 section header.

Hypothesis alignment: Targets C-13 and C-15 specifically. Cannot assess C-01 through C-25 against an executable prompt.

**V-02: UNSCORED (insufficient content)**

---

## V-03 through V-05

**Status:** Not provided in input. Cannot score.

---

## Rankings

| Rank | Variation | Score | Essential | New |
|------|-----------|-------|-----------|-----|
| 1 | V-01 — Role Sequence | **100** | ✅ | — |
| — | V-02 through V-05 | N/A | — | — |

---

## Excellence Signals

V-01 is the reference implementation for the three R8 excellence signals already codified as C-23, C-24, C-25. No new patterns beyond the rubric: the sealed Phase 0, three-dimension foil table, and calibration baseline record are all structurally enforced and traceable. The output checklist at the end of V-01 (a pre-emission self-verification pass) is a quality mechanism built into the skill prompt itself — not a separate scoreable criterion but worth noting as a structural pattern that reinforces auditability without adding runtime complexity.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": []}
```
