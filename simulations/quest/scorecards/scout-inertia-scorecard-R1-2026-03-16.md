# Quest Score — scout-inertia Round 1

> Evaluating V-01 and V-02. Note: the variate document was truncated — only two variations are available for scoring this round.

---

## Rubric Criteria Reference

| ID | Category | Weight |
|----|----------|--------|
| C-01 | Workaround mapped in detail | essential |
| C-02 | Switching cost quantified across dimensions | essential |
| C-03 | Inertia threat score is HIGH | essential |
| C-04 | "Why inertia loses" answered with specifics | essential |
| C-05 | Workaround failure modes identified | essential |
| R-01..R-03 | Recommended (not visible — rubric truncated) | recommended |

---

## V-01 — Role Sequence: Workaround-first pipeline

### Criterion Evaluation

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | Role 1 explicitly requires: named tool/file type, data/action handled, actor by role (not name), frequency, and output artifact. Failure check halts progress if only a category is stated. This is the strongest C-01 enforcement pattern in this round — generic answers are explicitly blocked. |
| C-02 | **PASS** | Role 2 states: "Qualitative labels ('high', 'moderate') are not acceptable — if you cannot estimate, say so explicitly." Cost table format with Estimate/Basis columns enforces number-or-range output on all three dimensions. |
| C-03 | **PASS** | Role 3 Step A states: "The default is HIGH. You may not downgrade it without naming a specific mitigating factor with documented evidence. 'The feature is compelling' is not a mitigating factor." Directly mirrors the rubric pass condition. |
| C-04 | **PASS** | Step C requires falsifiable conditions in the format "Teams switch when [observable trigger] because [workaround does X, which causes Y]." Gives a passing example and a failing example. |
| C-05 | **PASS** | Step B requires "at least two specific scenarios where the current workaround breaks, produces errors, causes re-work, or cannot scale." Explicitly rejects generic pain points. |

**All essential pass**: YES

### Recommended Criteria
Rubric recommended section not available (truncated). Estimated partial credit based on structural coverage: the sequential pipeline likely produces depth on narrative context but has no explicit recommended-dimension prompts. Estimated **1/3 pass**.

### Composite Score
```
essential:    5/5 × 60 = 60
recommended:  1/3 × 30 = 10  (estimated)
aspirational: 0/2 × 10 =  0  (no aspirational prompts present)
─────────────────────────────
V-01 composite ≈ 70
```

---

## V-02 — Output Format: Table-structured with inline scoring

### Criterion Evaluation

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | Section 1 table has explicit rows for workaround name, tool/file type, data handled, role, frequency, and output artifact. Self-score C-01 with PASS/FAIL checkbox that reads: "Named workaround with actor, frequency, and output artifact present." Gaps are visually obvious as empty table cells. |
| C-02 | **PASS** | Section 2 table has Dimension / Estimate / Unit / Basis columns. Unit column forces explicit unit choice ("hours or days/user", "hours of training", "sprint-days or people affected"). Self-score reads: "At least 2 of 3 rows carry a number or range." Strongly enforces quantification. |
| C-03 | **PASS** | Section 3 table has Score field (HIGH/MEDIUM/LOW), Rationale, Mitigating factor (if not HIGH), Evidence for mitigation. Self-score criterion: "Score is HIGH, or mitigation is documented with named evidence." Structure makes a silent downgrade impossible — the mitigation row is visibly empty. |
| C-04 | **PASS** | Section 5 table has Observable trigger / Why workaround fails at this trigger / What teams do instead. Self-score reads: "At least 2 rows with falsifiable trigger." The column header itself ("Observable trigger") prevents vague conditions. |
| C-05 | **PASS** | Section 4 table has Trigger / What goes wrong / User-visible symptom. Three columns force decomposition of each failure mode. Self-score reads: "At least 2 rows with specific trigger and symptom." |

**All essential pass**: YES

### Self-Score Mechanism (Section 6)
V-02 includes a Composite Self-Score table that lists all five essential criteria with PASS/FAIL and a gate: "If any essential criterion is FAIL, revise the corresponding section before finalizing." This is a revision gate that V-01 lacks.

### Recommended Criteria
Same caveat — rubric recommended section not available. The table format and self-scoring mechanism raise the likelihood of complete coverage and clean output; estimated **2/3 pass** (format aids completeness even on dimensions not explicitly prompted).

### Composite Score
```
essential:    5/5 × 60 = 60
recommended:  2/3 × 30 = 20  (estimated)
aspirational: 0/2 × 10 =  0
─────────────────────────────
V-02 composite ≈ 80
```

---

## Ranking

| Rank | Variation | Essential Pass | Composite | Distinguishing Factor |
|------|-----------|---------------|-----------|----------------------|
| 1 | **V-02** | YES (5/5) | ~80 | Inline self-scoring + revision gate + visually enforced structure |
| 2 | **V-01** | YES (5/5) | ~70 | Sequential role pipeline enforces depth but no self-correction mechanism |

---

## Excellence Signals from V-02

**1. Inline self-scoring per section** — Each section ends with a PASS/FAIL checkbox keyed to the rubric criterion. This catches misses before the output is finalized, reducing the rate of partial outputs that satisfy the intent but miss the letter of the criterion.

**2. Table column headers as constraints** — Column names like "Observable trigger" and "User-visible symptom" make vague entries structurally inconsistent. You cannot write "manual is slow" into a column labeled "User-visible symptom" without noticing the mismatch.

**3. Revision gate** — The composite self-score table in Section 6 includes an explicit instruction: if any essential criterion is FAIL, revise before finalizing. This turns the scoring logic into a production gate, not just a post-hoc assessment.

**4. Unit column forces quantification** — The Unit column in the switching cost table ("hours or days/user", "sprint-days or people affected") prevents the common failure mode of writing a number without a unit, which is as vague as a qualitative label.

---

```json
{"top_score": 80, "all_essential_pass": true, "new_patterns": ["inline-self-scoring per section with PASS/FAIL keyed to rubric criterion", "table column headers as structural constraints against vague entries", "composite revision gate: if any essential FAIL, revise before finalizing", "explicit Unit column to prevent unitless numbers from masquerading as quantification"]}
```
