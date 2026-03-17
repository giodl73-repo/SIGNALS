## Quest Score — `topic-retro` Round 4 (v4 Rubric)

> **Note**: Input contains V-01, V-02, and a partial V-03. V-04 and V-05 were not included in the prompt. Scoring covers the three visible variations only.

---

### Criterion Reference

| Tier | IDs | Max Points |
|------|-----|------------|
| Essential (5) | C-01…C-05 | 60 |
| Recommended (3) | C-06…C-08 | 30 |
| Aspirational (8) | C-09…C-16 | 10 |

---

## V-01 — Role Sequence: Echo-Lock-First

### Essential Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Signal inventory lists every artifact | PASS | Phase 2 table with Namespace / Date / Prediction columns |
| C-02 | Accuracy uses predicted-vs-actual comparison | PASS | Phase 3: C/P/W per namespace with formula stated in prose |
| C-03 | Gap analysis identifies missing signals | PASS | Phase 4: Gap Signal / Skill to Run / Decision Question columns |
| C-04 | Exactly one Echo | PASS | Phase 1 locked block: single sentence, labeled ECHO (LOCKED) |
| C-05 | Overall accuracy judgment rendered | PASS | Phase 3: "state the overall accuracy verdict — a score, ratio, or qualitative rating" |

**Essential: 5/5**

### Recommended Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-06 | Gap signals actionable | PASS | Phase 4 requires specific `/skill` and specific decision question; "Generic advice does not count" explicitly stated |
| C-07 | Accuracy differentiated by namespace | PASS | Per-namespace table in Phase 3 |
| C-08 | AMEND scope respected | PASS | AMEND constraint applied in Phase 2; no AMEND given → pass by default |

**Recommended: 3/3**

### Aspirational Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-09 | Calibration trend surfaced | FAIL | No reference to prior retro data |
| C-10 | Echo feeds back into signal design | FAIL | No mechanism for translating Echo into skill/rubric change |
| C-11 | Explicit numeric formula per namespace | PASS | Phase 3 prose: `(C×100 + P×50) / (C + P + W)` explicitly stated |
| C-12 | Echo precedes accuracy scoring | PASS | Phase 1 (Echo Lock) structurally precedes Phase 3 (Accuracy) |
| C-13 | Formula embedded in column header | FAIL | Header reads `Accuracy Score`; formula is in prose instruction above table |
| C-14 | Conflict named when tension arises | PASS | Phase 5 + Phase 1 both instruct: "record the tension — do not resolve it by silently updating the Echo" |
| C-15 | Header includes worked example | FAIL | Header has no formula and no example |
| C-16 | Conflict audit unconditional, always emits | PASS | Phase 5: "runs regardless of whether you perceived tension"; pre-populated `NO REVISION` cells; explicit statement those entries ARE the no-conflict signal |

**Aspirational: 4/8**

### Score

```
composite = (5/5 × 60) + (3/3 × 30) + (4/8 × 10)
          = 60 + 30 + 5
          = 95
```

**Band: GOLDEN** (all essential pass, composite = 95)

---

## V-02 — Output Format: Formula-in-Header with Worked Example

### Essential Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Signal inventory lists every artifact | PASS | Step 2 table with Namespace / Date / Prediction columns |
| C-02 | Accuracy uses predicted-vs-actual comparison | PASS | Step 3: C/P/W per namespace; header contains formula |
| C-03 | Gap analysis identifies missing signals | PASS | Step 4: Gap Signal / Skill to Run / Decision Question columns |
| C-04 | Exactly one Echo | PASS | Step 1: single Echo sentence, framed before inventory |
| C-05 | Overall accuracy judgment rendered | PASS | Step 3: "state the overall accuracy verdict: a score, ratio, or qualitative rating" |

**Essential: 5/5**

### Recommended Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-06 | Gap signals actionable | PASS | Step 4 requires specific skill and exact decision question; "Generic guidance does not pass" |
| C-07 | Accuracy differentiated by namespace | PASS | Per-namespace table in Step 3 |
| C-08 | AMEND scope respected | PASS | AMEND section present; no AMEND given → pass by default |

**Recommended: 3/3**

### Aspirational Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-09 | Calibration trend surfaced | FAIL | No reference to prior retro data |
| C-10 | Echo feeds back into signal design | FAIL | No mechanism for translating Echo into a change proposal |
| C-11 | Explicit numeric formula per namespace | PASS | Formula present in column header itself — strongest possible enforcement |
| C-12 | Echo precedes accuracy scoring | PASS | Step 1 framed as "Before reviewing signals, identify…"; structurally prior to Step 3 |
| C-13 | Formula embedded in column header | PASS | Header: `Score: (C×100+P×50)/(C+P+W) [e.g. C=2,P=1,W=1 → 62.5]` |
| C-14 | Conflict named when tension arises | PASS | Step 5 table with explicit CONFLICT DETECTED / NO CONFLICT states |
| C-15 | Header includes worked example alongside formula | PASS | Header contains `[e.g. C=2,P=1,W=1 → 62.5]` — inputs and result shown inline |
| C-16 | Conflict audit unconditional, always emits | PASS | Step 5: "This step runs unconditionally"; pre-populated `NO CONFLICT` cells; "this table must be present and populated whether or not tension occurred" |

**Aspirational: 6/8**

### Score

```
composite = (5/5 × 60) + (3/3 × 30) + (6/8 × 10)
          = 60 + 30 + 7.5
          = 97.5
```

**Band: GOLDEN** (all essential pass, composite = 97.5)

---

## V-03 — Lifecycle Emphasis: Phase Contracts + Incremental Revision Log

> **Note**: Variation text is cut off after Phase 1 setup. Criteria requiring Phase 3–5 content are assessed from the design description and visible Phase 1 structure, with confidence noted.

### Essential Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Signal inventory lists every artifact | PASS (inferred) | Phase 2 implied by REQUIRES/PRODUCES contract structure |
| C-02 | Accuracy uses predicted-vs-actual comparison | PASS (inferred) | Phase 3 implied; revision log row exists for Phase 3 accuracy |
| C-03 | Gap analysis identifies missing signals | PASS (inferred) | Gap phase implied by design description |
| C-04 | Exactly one Echo | PASS | Phase 1 shows single locked Echo sentence |
| C-05 | Overall accuracy judgment rendered | PASS (inferred) | Accuracy phase in contract structure |

**Essential: 5/5**

### Recommended Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-06 | Gap signals actionable | PASS (inferred) | Consistent with skill spec; no contrary signal |
| C-07 | Accuracy differentiated by namespace | PASS (inferred) | Per-namespace breakdown implied |
| C-08 | AMEND scope respected | PASS | No AMEND given → pass by default |

**Recommended: 3/3**

### Aspirational Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-09 | Calibration trend surfaced | FAIL | No reference to prior retro data |
| C-10 | Echo feeds back into signal design | FAIL | No mechanism visible |
| C-11 | Explicit numeric formula per namespace | PASS (inferred) | Emphasis on lifecycle contracts implies Phase 3 has formula in prose; design description references Phase 3 accuracy computation |
| C-12 | Echo precedes accuracy scoring | PASS | Phase 1 REQUIRES nothing, runs before Phase 3 — structural ordering enforced by contract |
| C-13 | Formula embedded in column header | FAIL | Emphasis is on REQUIRES/PRODUCES contracts, not header-format innovation; no evidence of formula-in-header |
| C-14 | Conflict named when tension arises | PASS | Revision log column "Would have changed the Echo?" forces explicit per-phase conflict response |
| C-15 | Header includes worked example | FAIL | No evidence of worked example in any header |
| C-16 | Conflict audit unconditional, always emits | FAIL | Revision log row shows `*to be filled by Phase 3*` — this is a placeholder instruction, not a pre-populated NO REVISION default. If Phase 3 does not update the row, the cell value remains ambiguous rather than explicitly signaling no-conflict. Design description claims "pre-populated NO REVISION" but the shown template does not implement this. |

**Aspirational: 3/8**

### Score

```
composite = (5/5 × 60) + (3/3 × 30) + (3/8 × 10)
          = 60 + 30 + 3.75
          = 93.75
```

**Band: GOLDEN** (all essential pass, composite = 93.75)

---

## Ranking

| Rank | Variation | Score | Band | Aspirational Passes |
|------|-----------|-------|------|---------------------|
| 1 | V-02 Formula-in-Header + Worked Example | **97.5** | GOLDEN | 6/8 (C-11, C-12, C-13, C-14, C-15, C-16) |
| 2 | V-01 Echo-Lock-First | **95** | GOLDEN | 4/8 (C-11, C-12, C-14, C-16) |
| 3 | V-03 Phase Contracts (partial) | **93.75** | GOLDEN | 3/8 (C-11, C-12, C-14) |

V-04 and V-05: not provided — excluded from ranking.

---

## Excellence Signals

**From V-02 (top scorer):**

1. **The header IS the computation** — `Score: (C×100+P×50)/(C+P+W) [e.g. C=2,P=1,W=1 → 62.5]` places the formula and a worked example at the exact point of cell entry. The scorer cannot populate the column without seeing both. This collapses C-11, C-13, and C-15 into one structural mechanism rather than three separate instructions.

2. **"NO CONFLICT" as the structural default** — pre-populating conflict audit cells with `NO CONFLICT` rather than leaving them blank means the no-conflict signal is produced by doing nothing, while recording a conflict requires active change. Silence and no-conflict are no longer indistinguishable.

**From V-01:**

3. **Echo lock metadata embedded in the Echo block** — `Phase locked: 1 / Revision status: NO REVISION` appears inline with the Echo statement, making the lock state a machine-readable artifact rather than a narrative instruction. The lock is part of the output structure, not just the prompt framing.

**From V-03:**

4. **REQUIRES / PRODUCES phase contracts** — each phase declares what it needs as input and what it must produce as output before the next phase may begin. This enforces phase ordering at the structural level, not the instruction level. A phase that skips its PRODUCES obligation is visibly incomplete. This pattern is not yet captured in any rubric criterion (C-01 through C-16) and is a candidate for C-17.

---

```json
{"top_score": 97.5, "all_essential_pass": true, "new_patterns": ["REQUIRES/PRODUCES phase contracts enforce phase ordering structurally — each phase declares prerequisites and committed outputs before the next phase may begin, making incomplete phases visibly non-compliant rather than silently skipped"]}
```
