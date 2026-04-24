## Scout-Size Prompt Variations — R12 Scorecard

---

### Scoring Summary

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | **Composite** |
|-----------|---------------|-----------------|-------------------|---------------|
| V-01 | 60 | 30 | 7.2 (18/25) | **97.2** |
| V-02 | 60 | 30 | 7.2 (18/25) | **97.2** |
| V-03 | 60 | 30 | 7.2 (18/25) | **97.2** |
| V-04 | 60 | 30 | 9.2 (23/25) | **99.2** |
| V-05 | 60 | 30 | 9.2 (23/25) | **99.2** |

**Rank**: V-04 = V-05 > V-01 = V-02 = V-03

---

### Essential Criteria — All Variations (60 pts)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|----|------|------|------|------|------|-------|
| C-01 | PASS | PASS | PASS | PASS | PASS | All have named-point tables with count column |
| C-02 | PASS | PASS | PASS | PASS | PASS | LOW/MEDIUM/HIGH/XL enforced with off-vocabulary WRONG examples |
| C-03 | PASS | PASS | PASS | PASS | PASS | Workaround + cost direction in all; V-05 adds gate semantics |
| C-04 | PASS | PASS | PASS | PASS | PASS | Level + basis paired with WRONG/CORRECT |
| C-05 | PASS | PASS | PASS | PASS | PASS | Opening statement + signal boundary check throughout |

---

### Recommended Criteria — All Variations (30 pts)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|----|------|------|------|------|------|-------|
| C-06 | PASS | PASS | PASS | PASS | PASS | Specialist discipline column header, WRONG: "3 engineers" |
| C-07 | PASS | PASS | PASS | PASS | PASS | N–M sprint range format enforced; single-sprint and date WRONG |
| C-08 | PASS | PASS | PASS | PASS | PASS | Named causal factor required; "it's complex" WRONG |

---

### Aspirational Criteria — Detailed (10 pts)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence notes |
|----|------|------|------|------|------|----------------|
| C-09 | PASS | PASS | PASS | PASS | PASS | Tier-up + tier-down conditions in sensitivity section |
| C-10 | PASS | PASS | PASS | PASS | PASS | Calibration table: what would raise / lower confidence |
| C-11 | PASS | PASS | PASS | PASS | PASS | `── CONFIDENCE GAP CHECKPOINT ──` standalone section in all |
| C-12 | PASS | PASS | PASS | PASS | PASS | "Single Named Falsifiable Condition" column label enforces singularity |
| C-13 | PASS | PASS | PASS | PASS | PASS | "Destination Tier [must differ from current — fill LOW / MEDIUM / HIGH / XL]" in column header |
| C-14 | PASS | PASS | PASS | PASS | PASS | WRONG: "scope grows" (deferral); CORRECT: "confirm by reviewing PRD offline-sync section" |
| C-15 | PASS | PASS | PASS | PASS | PASS | WRONG/CORRECT block + self-test enforce non-overlap in all; two-phase charter enforces structurally in V-04/V-05 |
| C-16 | PASS | PASS | PASS | PASS | PASS | "must differ from current tier" in column header for all |
| C-17 | PASS | PASS | PASS | PASS | PASS | Inline WRONG/CORRECT at C-11/C-15 (gap section) and C-16 (sensitivity) for all |
| C-18 | PASS | PASS | PASS | PASS | PASS | Tier destination encoded in column header; gap as standalone section |
| C-19 | PASS | PASS | PASS | PASS | PASS | WRONG/CORRECT precede all output field slots, including gap section — gap field at bottom of checkpoint, examples above it |
| **C-20** | **FAIL** | **FAIL** | **FAIL** | **PASS** | **PASS** | Single-phase cannot role-separate basis/gap; V-04/V-05 Phase 2 Risk Assessor owns gap production |
| C-21 | PASS | PASS | PASS | PASS | PASS | Named WRONG + named CORRECT in every checkpoint; V-02 adds labeled DIAGNOSIS in WRONG block |
| C-22 | PASS | PASS | PASS | PASS | PASS | Gap field label: "not a negation of it"; tier destination: "must differ from current" in column header |
| **C-23** | **FAIL** | **FAIL** | **FAIL** | **PASS** | **PASS** | No role charters in single-phase; V-04 two-phase: explicit "Fields owned / reserved" lists; V-05 three-phase: Phase 0/1/2 enumerated field ownership |
| **C-24** | **FAIL** | **FAIL** | **FAIL** | **PASS** | **PASS** | V-04/V-05 Phase 2 non-access clause names prohibited category: "confirmed API contracts, enumerated integration points, stable component interfaces" |
| **C-25** | **FAIL** | **FAIL** | **FAIL** | **PASS** | **PASS** | V-04/V-05 Phase 2 charter embeds executable self-test: "if I reversed a statement from P1-6/P1-5... If yes: you have written a basis-negation — a Phase 2 charter violation." |
| **C-26** | **FAIL** | **FAIL** | **FAIL** | **PASS** | **PASS** | V-04: "Produced By" column in compilation table; V-05: "Phase" column; both embed role tags in individual step column headers (e.g., "[Phase 1 Sizing Analyst]") |
| **C-27** | **FAIL** | **FAIL** | **FAIL** | **FAIL** | **FAIL** | C-32 extracts gap from compilation table → no gap column header exists to encode C-15 constraint in the table; footnote reference does not encode the relational rule |
| C-28 | PASS | PASS | PASS | **FAIL** | **FAIL** | C-28 applies only to single-phase designs; V-04/V-05 use C-20 role-separation, making C-28 N/A — C-25 is the applicable analog (satisfied) |
| **C-29** | **FAIL** | **FAIL** | **FAIL** | **PASS** | **PASS** | V-04 Phase 1 charter: "Fields reserved for Phase 2 [do not produce here]: Confidence Gap · Confidence Calibration · Tier Sensitivity" — explicit exclusion list matching Phase 2 ownership |
| C-30 | PASS | PASS | PASS | PASS | PASS | All three mechanisms converge on gap section: (1) field label constraint, (2) executable self-test, (3) WRONG/CORRECT within same section |
| C-31 | PASS | PASS | PASS | PASS | PASS | Vacuous: C-32 extracts gap from table; sensitivity achieves C-19 (WRONG/CORRECT precede table) |
| C-32 | PASS | PASS | PASS | PASS | PASS | Gap in `── CONFIDENCE GAP CHECKPOINT ──` standalone section; compilation table footnote: "See ── CONFIDENCE GAP CHECKPOINT ── section above" |
| C-33 | PASS | PASS | PASS | PASS | PASS | V-01: "you have written a basis-negation"; V-02: "DIAGNOSIS: basis-negation detected"; V-03: "you are in a basis-negation pattern"; V-04: "basis-negation — a Phase 2 charter violation"; V-05: "you have written a basis-negation. You are in a basis-negation pattern." |

---

### Aspirational Counts

| Variation | PASS | FAIL | Score (×0.4 each) |
|-----------|------|------|-------------------|
| V-01 | 18 | 7 | 7.20 |
| V-02 | 18 | 7 | 7.20 |
| V-03 | 18 | 7 | 7.20 |
| V-04 | 23 | 2 | 9.20 |
| V-05 | 23 | 2 | 9.20 |

---

### Failing Criteria by Design Class

**Single-phase (V-01, V-02, V-03) — 7 failing criteria:**
C-20 (no role separation), C-23 (no role charters), C-24 (no Phase 2 non-access), C-25 (no Phase 2 self-test), C-26 (no role-tagged field labels), C-27 (no compilation table cross-phase constraint encoding), C-29 (no Phase 1 exclusion list)

**Multi-phase (V-04, V-05) — 2 failing criteria:**
C-27 (C-32 architectural incompatibility: gap extracted from table, so no gap column header exists in compilation to encode C-15 constraint), C-28 (single-phase criterion; N/A when C-20 is used)

---

### Ranking

| Rank | Variation | Score | Distinguishing feature |
|------|-----------|-------|----------------------|
| 1 (tie) | **V-04** | 99.2 | Two-phase role separation; Phase 2 charter violation framing; "Produced By" column |
| 1 (tie) | **V-05** | 99.2 | Three-phase gate; Phase 0 CLOSED/OPEN inertia gate; "Failure class:" header in WRONG block |
| 3 (tie) | **V-01** | 97.2 | Pre-slot examples throughout; cleanest single-phase; "you have written a basis-negation" |
| 3 (tie) | **V-02** | 97.2 | DIAGNOSIS block elevates failure class to labeled structural event in WRONG example |
| 3 (tie) | **V-03** | 97.2 | Second-person register; "you are in a basis-negation pattern" as external detection |

---

### Excellence Signals from V-04/V-05

**What made V-04 and V-05 better (6 role-separation criteria gained simultaneously):**

1. **Charter-ownership cluster** — Two/three-phase design gains C-20 + C-23 + C-24 + C-25 + C-26 + C-29 as a unit. Each criterion requires the previous to have any meaning: role separation (C-20) makes charters possible; charters enable field ownership (C-23); ownership enables non-access prohibition (C-24); prohibition enables the self-test (C-25); self-test enables structural enforcement in labels (C-26). These are not independent — they form a dependency chain where each criterion scaffolds the next.

2. **Bidirectional boundary transparency** — Phase 1 exclusion list ("Fields reserved for Phase 2 [do not produce here]") combined with Phase 2 non-access clause creates ownership enforcement from both sides: Phase 2 cannot import from Phase 1 AND Phase 1 cannot encroach on Phase 2. Neither direction alone is sufficient.

3. **Charter-violation escalation** — Naming the failure class as "a Phase 2 charter violation" elevates correction motivation from rule compliance ("you've violated the constraint") to role-contract accountability ("you've broken your charter"). This framing activates role identity as an enforcement mechanism.

**What C-32 costs both V-04 and V-05 (architectural incompatibility):**

C-27 cannot be satisfied when C-32 is used because C-27 requires the C-15 relational constraint to appear in the gap column header of the compilation table — but C-32 removes the gap from the table entirely. These two criteria are architecturally mutually exclusive. A future variation would need to satisfy C-27 by either: (a) including a gap row in the compilation table that encodes the relational constraint while still pointing to the standalone section for content, or (b) accepting the C-27 loss as the price of C-32's superior enforcement architecture.

**New patterns emerging from V-05 not yet captured in rubric:**

- **"Failure class:" header within WRONG example block** — V-05 labels the failure class as `**Failure class: basis-negation.**` inside the WRONG example itself, making the class name visible as a document-structure event before the model encounters the self-test. This is distinct from C-33, which only requires the class name in the self-test affirmative branch.

- **Phase gate with explicit CLOSED/OPEN status field** — V-05's Phase 0 gate includes a `Gate status: [ CLOSED ] / [ OPEN ]` field that the model must fill before Phase 1 can begin. This transforms inertia from "a section to fill" into "a prerequisite to declare closed" — the gate status field makes non-compliance structurally visible.

---

```json
{"top_score": 99.2, "all_essential_pass": true, "new_patterns": ["Failure-class name elevated to standalone 'Failure class:' structural header within the WRONG example block, priming the class label as a document-structure event before the self-test encounter", "Phase gate with explicit CLOSED/OPEN status field makes inertia a hard architectural prerequisite — subsequent phases are blocked until the gate is declared closed", "Charter-violation qualifier appended to failure-class label ('basis-negation — a Phase 2 charter violation') escalates correction from self-assessment to role-contract enforcement, activating role identity as an enforcement mechanism"]}
```
