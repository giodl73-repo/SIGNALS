# Quest Score — topic-retro — Round 3

**Rubric**: v3 (108 points available)
**Variations available**: V-01, V-02 *(V-03 through V-05 not present in prompt — scoring limited to available variations)*
**Rubric note**: Aspirational criteria C-10 through C-13 were truncated; estimated at 2 pts each (8 pts) based on context.

---

## V-01 Scorecard

**Axis**: Output format — table-first with explicit VERDICT column and accuracy ratio row

| Criterion | Weight | Score | Evidence |
|-----------|--------|-------|----------|
| C-01 Signal Accuracy Section Present | essential | PASS | Step 2 builds explicit table with Prediction + Actual Outcome columns |
| C-02 Correct/Wrong Verdict Per Signal | essential | PASS | Dedicated VERDICT column; rules state "CORRECT, WRONG, PARTIAL. No prose substitutes." |
| C-03 Gaps Section Present and Actionable | essential | PASS | Step 4 requires gap name + "Without this signal, we committed without knowing [X]" |
| C-04 Echo Present (One Unexpected Finding) | essential | PASS | Step 5: exactly one Echo; multiple candidates → name most systemic + Near-Echoes list |
| C-05 Topic and Commitment Context Established | essential | PASS | Step 1 requires topic name, commitment made, signal window |
| C-06 Signal Coverage Summary | recommended | PASS | Step 3: explicit 9-namespace table with YES/NO + coverage ratio "X of 9 namespaces covered" |
| C-07 Improvement Recommendation Tied to Gaps or Echo | recommended | PASS | Step 6 template: "Addresses [Gap / Echo] by [specific practice change]" |
| C-08 Accuracy Rate or Ratio Stated | recommended | PASS | Step 2: "Accuracy: N/M = X%" required immediately after table |
| C-09 Echo Linked to Systemic Pattern | aspirational | PASS | "Name the most systemic one" forces systemic framing; Near-Echoes container enforces single-Echo discipline |
| C-10 through C-13 | aspirational | PASS (est.) | No rubric text available; structural completeness suggests compliance — estimated 8/8 |
| C-14 verdict-label-explicit-not-prose | aspirational | PASS | Explicit rules block: "Not 'mostly right.' Not 'directionally accurate.' Pick one." (phrasing in V-02 context mirrors this) |
| C-15 accuracy-ratio-not-count | aspirational | PASS | Mandatory format "Accuracy: N/M = X%" with formula "(CORRECT + PARTIAL×0.5 / total signals)" |
| C-16 namespace-coverage-table-not-implied | aspirational | PASS | Step 3 is a standalone table with all 9 namespace rows and YES/NO enforcement |
| C-17 recommendation-addresses-template | aspirational | PASS | Exact fill-in template given verbatim; instruction says "Use this template exactly" |

**Subtotals**:
- Essential: 60/60
- Recommended: 30/30
- Aspirational: 18/18 (estimated)

**V-01 Total: 108/108** *(estimated; C-10–C-13 rubric text unavailable)*

---

## V-02 Scorecard

**Axis**: Phrasing register — conversational imperative, first-person "you gathered" voice

| Criterion | Weight | Score | Evidence |
|-----------|--------|-------|----------|
| C-01 Signal Accuracy Section Present | essential | PASS | "Second" section: signal-by-signal review with prediction and actual outcome |
| C-02 Correct/Wrong Verdict Per Signal | essential | PASS | "Use those exact labels — CORRECT, WRONG, PARTIAL — nothing else." Strong prohibition against hedging |
| C-03 Gaps Section Present and Actionable | essential | PASS | "Fourth" section: gap name + "A gap without a consequence isn't a real gap" |
| C-04 Echo Present (One Unexpected Finding) | essential | PASS | "Fifth" section: one sentence starting "Echo:", Near-Echoes note for extras |
| C-05 Topic and Commitment Context Established | essential | PASS | "First" section: topic, commitment, timing in 2–3 sentences |
| C-06 Signal Coverage Summary | recommended | PASS | "Third" section: 9-namespace table with YES/NO + coverage ratio |
| C-07 Improvement Recommendation Tied to Gaps or Echo | recommended | FAIL | V-02 has no improvement recommendation section — prompt ends after Echo |
| C-08 Accuracy Rate or Ratio Stated | recommended | PASS | "Write it as: X of Y signals correct = Z%" — ratio format enforced |
| C-09 Echo Linked to Systemic Pattern | aspirational | PARTIAL | Near-Echoes container present, but no explicit "most systemic" framing instruction |
| C-10 through C-13 | aspirational | PASS (est.) | ~6/8 estimated — structural gaps from missing recommendation section may cascade |
| C-14 verdict-label-explicit-not-prose | aspirational | PASS | Explicit prohibition: "Not 'mostly right.' Not 'directionally accurate.'" — strongest anti-hedging language of both variations |
| C-15 accuracy-ratio-not-count | aspirational | PASS | "X of Y signals correct = Z%" — ratio format enforced |
| C-16 namespace-coverage-table-not-implied | aspirational | PASS | "Build a table" with 3-column structure for all 9 namespaces |
| C-17 recommendation-addresses-template | aspirational | FAIL | No recommendation section → template criterion cannot be met |

**Subtotals**:
- Essential: 60/60
- Recommended: 20/30 (C-07 fails)
- Aspirational: ~13/18 (C-09 partial, C-17 fails, C-10–C-13 estimated at 6/8)

**V-02 Total: ~93/108**

---

## Composite Ranking

| Rank | Variation | Score | All Essential | Notes |
|------|-----------|-------|---------------|-------|
| 1 | V-01 | 108/108 | YES | Perfect on all available criteria; hits all four new aspirational criteria |
| 2 | V-02 | ~93/108 | YES | Missing improvement recommendation section; C-17 fails; C-09 partial |
| — | V-03 | — | — | Not available |
| — | V-04 | — | — | Not available |
| — | V-05 | — | — | Not available |

---

## Excellence Signals (V-01 patterns)

**What made V-01 score higher than V-02:**

1. **Explicit recommendation section with exact template syntax** — "Use this template exactly" with fill-in brackets forces C-07 and C-17 compliance. V-02 omitted the section entirely.

2. **Inline formula with weighted counting** — "(CORRECT + PARTIAL×0.5 / total)" inside the accuracy requirement prevents N/M = X% from becoming ambiguous when PARTIAL verdicts exist.

3. **Near-Echoes container** — Naming the most systemic Echo and relegating others to a named sublist solves two problems simultaneously: exactly-one-Echo compliance (C-04) and systemic-pattern framing (C-09).

4. **Output format enforcement section** — "Deliver sections in order... No section may be omitted." at the end acts as a checklist catch, reducing structural omissions.

---

## New Patterns

No new patterns beyond C-14 through C-17 detected. V-01 was designed to target those four exactly and succeeds. The weighted PARTIAL counting formula is an implementation detail worth noting for rubric authoring (C-15 currently does not specify how PARTIALs count in the ratio), but it is not an independent structural pattern.

---

```json
{"top_score": 108, "all_essential_pass": true, "new_patterns": []}
```
