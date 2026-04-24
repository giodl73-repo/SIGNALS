Looking at the Round 2 scorecard, the new excellence signals are the V-01 features that caused partials in V-02 and V-03:

- **V-02 C-02 partial** → verdict-label-explicit-not-prose (column/field enforcement vs. prose inference)
- **V-02 C-08 partial** → accuracy-ratio-not-count (N/M = X% vs. simple count)
- **V-03 C-06 partial** → namespace-coverage-table-not-implied (explicit 9-namespace table vs. structural implication)
- **V-03 C-07 partial** → recommendation-addresses-template (explicit "addresses [Gap/Echo] by [mechanism]" template)

Here is the complete v3 rubric:

---

```markdown
---
skill: quest-rubric
skill_target: topic-retro
date: 2026-03-17
version: 3
prior_version: topic-retro-rubric-v2-2026-03-17.md
changes: |
  Round 2 excellence signals promoted to aspirational criteria.
  C-14: verdict-label-explicit-not-prose
  C-15: accuracy-ratio-not-count
  C-16: namespace-coverage-table-not-implied
  C-17: recommendation-addresses-template
  Total available updated from 100 to 108 (4 new criteria × 2 pts each).
---
```

# Scoring Rubric: topic-retro (v3)

Post-commitment retrospective on a topic's signals. Evaluates whether the output delivers
structured retrospective value: what signals were gathered, which predictions held, which
failed, what gaps mattered, and the one unexpected finding (the Echo).

---

## Essential Criteria (60 points total)

### C-01 — Signal Accuracy Section Present
- **Weight**: essential  **Category**: correctness
- **Pass condition**: Named section lists at least one signal by name with both prediction and actual outcome. List without the comparison fails.

### C-02 — Correct/Wrong Verdict Per Signal
- **Weight**: essential  **Category**: correctness
- **Pass condition**: Every signal carries a verdict label. Vague language without a clear verdict fails.

### C-03 — Gaps Section Present and Actionable
- **Weight**: essential  **Category**: coverage
- **Pass condition**: At least one gap named with decision-impact statement. Gap without impact fails.

### C-04 — Echo Present (One Unexpected Finding)
- **Weight**: essential  **Category**: depth
- **Pass condition**: Exactly one Echo, framed as unpredicted (not a restatement of a wrong prediction). Multiple echoes or restatements fail.

### C-05 — Topic and Commitment Context Established
- **Weight**: essential  **Category**: correctness
- **Pass condition**: Topic name and commitment nature stated in first two sections.

---

## Recommended Criteria (30 points total)

### C-06 — Signal Coverage Summary
- **Weight**: recommended  **Category**: coverage
- **Pass condition**: Summary distinguishes "signals gathered" from "signals absent" across all 9 namespaces.

### C-07 — Improvement Recommendation Tied to Gaps or Echo
- **Weight**: recommended  **Category**: depth
- **Pass condition**: Recommendation names the specific gap or Echo it addresses and specifies a practice change.

### C-08 — Accuracy Rate or Ratio Stated
- **Weight**: recommended  **Category**: format
- **Pass condition**: Numerical accuracy summary (ratio or percentage) present in or immediately following the Signal Accuracy section.

---

## Aspirational Criteria (18 points total)

### C-09 — Echo Linked to Systemic Pattern *(baseline)*
- **Weight**: aspirational  **Category**: depth
- **Pass condition**: Echo section names a pattern or prior instance. One-off without pattern linkage fails.

### C-10 — AMEND Variants Handled Correctly *(AMEND only)*
- **Weight**: aspirational  **Category**: behavior
- **Pass condition**: When topic is an amendment, Steps 2–4 are restricted to AMEND scope, and out-of-scope omissions are noted at the table bottom.

### C-11 — Systemic Pattern Echo Field *(from R1)*
- **Weight**: aspirational  **Category**: depth
- **Pass condition**: Echo section contains a named "Systemic pattern" field (or equivalent labeled field). Pattern linkage that appears only in prose without a named field fails.

### C-12 — Three-Way Wrong/Gap/Echo Isolation *(from R1)*
- **Weight**: aspirational  **Category**: structure
- **Pass condition**: Wrong-signal verdicts, gaps, and the Echo occupy structurally separate sections or fields with independent framing rules. Logical isolation via prose alone does not satisfy this — structural separation (columns, labeled steps, or distinct headers) is required.

### C-13 — Inertia Framing for Gaps *(from R1)*
- **Weight**: aspirational  **Category**: depth
- **Pass condition**: Each gap entry includes an explicit inertia statement naming the assumption the team held without evidence. Generic "we didn't gather this signal" framing without an assumption named fails.

### C-14 — Verdict Label Explicit Not Prose *(from R2)*
- **Weight**: aspirational  **Category**: correctness
- **Pass condition**: Verdict labels (CORRECT / WRONG / PARTIAL) appear as explicit per-signal fields or column values, not inferred from surrounding prose. A conversational format that relies on prose tone to convey verdict fails this criterion even if C-02 passes via spirit.

### C-15 — Accuracy Ratio Not Count *(from R2)*
- **Weight**: aspirational  **Category**: format
- **Pass condition**: Accuracy is expressed as N/M = X% (ratio and percentage together). A count ("3 correct, 2 wrong") without the ratio calculation fails even if C-08 passes via spirit.

### C-16 — Namespace Coverage Table Not Implied *(from R2)*
- **Weight**: aspirational  **Category**: coverage
- **Pass condition**: Coverage is shown via an explicit 9-namespace table with per-namespace status (Present / Absent / Partial). Coverage implied by phase structure or discussed in prose without a table fails even if C-06 passes via spirit.

### C-17 — Recommendation Addresses Template *(from R2)*
- **Weight**: aspirational  **Category**: depth
- **Pass condition**: Recommendation uses an explicit linking template of the form "addresses [Gap N / Echo] by [mechanism]" or equivalent labeled structure. A recommendation that connects to a gap or Echo only through prose inference fails even if C-07 passes via spirit.

---

## Scoring Formula

**Total available: 108**

| Tier | Criteria | Points each | Subtotal |
|------|----------|-------------|---------|
| Essential | C-01 – C-05 | 12 | 60 |
| Recommended | C-06 – C-08 | 10 | 30 |
| Aspirational | C-09 – C-17 | 2 | 18 |

**PARTIAL on essential = FAIL for "All essential: YES".**
PARTIAL on recommended or aspirational = 1 pt (half credit).

When the topic is not an AMEND, C-10 is non-applicable (excluded from denominator):
- No AMEND: denominator = 106
- AMEND present: denominator = 108
```

---

Four new criteria added (C-14 – C-17). Each targets the specific failure mode exposed by the V-02/V-03 partials in Round 2 — the pattern in each case being that a variation satisfied the spirit of a recommended criterion but lacked the structural enforcement that V-01 demonstrated. The "from R2" tags distinguish them from the R1 promotions (C-11 – C-13).
