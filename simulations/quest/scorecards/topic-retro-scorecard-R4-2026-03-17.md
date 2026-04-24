# Quest Score — topic-retro (Round 4)

**Rubric version**: v3 (108 pts total)
**Variations provided**: V-01, V-02, V-03 (V-04–V-05 not in prompt; V-03 prompt appears truncated)

---

## Scoring Key

| Weight | Points |
|--------|--------|
| Essential (C-01–C-05) | 12 pts each |
| Recommended (C-06–C-08) | 10 pts each |
| Aspirational C-09 | 10 pts |
| Aspirational C-14–C-17 | 2 pts each |
| **Total available** | **108** |

PASS = full points · PARTIAL = half points · FAIL = 0

---

## V-01 — Table-Heavy Format

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Signal Accuracy Section | PASS (12) | "Step 2 — Signal Accuracy Table" with Prediction/Actual Outcome columns |
| C-02 Correct/Wrong Verdict | PASS (12) | Explicit "Verdict" column header, values listed as CORRECT / WRONG / PARTIAL |
| C-03 Gaps Section Actionable | PASS (12) | Gaps table with "Decision Impact" column required |
| C-04 Echo Present | PASS (12) | "Write exactly one Echo"; explicitly distinguishes from "wrong prediction" |
| C-05 Topic & Commitment Context | PASS (12) | First output section named "Topic and Commitment Context" |
| C-06 Signal Coverage Summary | PASS (10) | 9-namespace table with Gathered? column explicitly listing all 9 names |
| C-07 Recommendation Tied to Gap/Echo | PASS (10) | Recommendation section present; template enforces naming the gap/echo |
| C-08 Accuracy Ratio Stated | PASS (10) | "**Accuracy: N/M = X%**" literal template below table |
| C-09 Echo Linked to Systemic Pattern | PARTIAL (5) | Asks whether Echo "points to a systemic gap in how signals were gathered" — systemic framing present but not explicitly labeled as a named pattern |
| C-14 verdict-label-explicit-not-prose | PASS (2) | "Verdict" is a named column header; CORRECT/WRONG/PARTIAL are column values |
| C-15 accuracy-ratio-not-count | PASS (2) | N/M = X% format specified, not raw count |
| C-16 namespace-coverage-table-not-implied | PASS (2) | All 9 namespace rows listed in the table template itself |
| C-17 recommendation-addresses-template | PASS (2) | Bold fill-in template: "This recommendation addresses [Gap or Echo] by [practice change]" |

**V-01 Total: 103 / 108 (95%)**
All essential criteria: **PASS**

---

## V-02 — Conversational + Imperative

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Signal Accuracy Section | PASS (12) | "Section 3 — Were they right?" with explicit prediction vs. actual instruction |
| C-02 Correct/Wrong Verdict | PASS (12) | "Give each signal a verdict: CORRECT, WRONG, or PARTIAL. Be blunt — vague verdicts like 'mostly right' don't count." |
| C-03 Gaps Section Actionable | PASS (12) | "Section 4 — What was missing" requires decision impact per gap |
| C-04 Echo Present | PASS (12) | "Not a wrong prediction — something genuinely new. Call it the Echo." One sentence + paragraph required |
| C-05 Topic & Commitment Context | PASS (12) | Context block at top + "Section 1 — What happened" |
| C-06 Signal Coverage Summary | PASS (10) | "Go through all 9 namespaces… Show this as a table — namespace, file name or 'none', gathered yes/no" |
| C-07 Recommendation Tied to Gap/Echo | PASS (10) | "Name the specific gap or Echo it responds to" + template sentence provided |
| C-08 Accuracy Ratio Stated | PASS (10) | "X out of M signals were correct or partially correct (X/M = Y%)" literal phrasing |
| C-09 Echo Linked to Systemic Pattern | PARTIAL (5) | "What it tells you about how signals were gathered" — process framing, not explicitly a systemic pattern link |
| C-14 verdict-label-explicit-not-prose | PARTIAL (1) | Labels CORRECT/WRONG/PARTIAL required in prose instruction; table columns not explicitly named — column header left implicit |
| C-15 accuracy-ratio-not-count | PASS (2) | X/M = Y% format present |
| C-16 namespace-coverage-table-not-implied | PASS (2) | Explicit table instruction for all 9 namespaces |
| C-17 recommendation-addresses-template | PASS (2) | "Use this sentence structure: 'This recommendation addresses [gap or echo name] by [what you'd do differently].'" |

**V-02 Total: 102 / 108 (94%)**
All essential criteria: **PASS**

---

## V-03 — Lifecycle Emphasis ⚠️ TRUNCATED

> **Note**: V-03's prompt was truncated in the input. Only the header and two template variables are visible:
> ```
> /topic-retro — Post-Commitment Signal Retrospective
> Topic: {{topic}}
> Commitment: {{commitment_description}}
> ```
> Scoring reflects visible content only.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Signal Accuracy Section | FAIL (0) | No instructions visible |
| C-02 Correct/Wrong Verdict | FAIL (0) | No instructions visible |
| C-03 Gaps Section | FAIL (0) | No instructions visible |
| C-04 Echo Present | FAIL (0) | No instructions visible |
| C-05 Topic & Commitment Context | PARTIAL (6) | {{topic}} and {{commitment_description}} present as template fields, but no instruction to establish as sections |
| C-06 through C-09, C-14–C-17 | FAIL (0) | No instructions visible |

**V-03 Total: 6 / 108 (6%) — INCOMPLETE, DO NOT RANK**

---

## Ranking

| Rank | Variation | Score | Essential Pass |
|------|-----------|-------|----------------|
| 1 | V-01 Table-Heavy | **103/108 (95%)** | Yes |
| 2 | V-02 Conversational | **102/108 (94%)** | Yes |
| — | V-03 Lifecycle | 6/108 (truncated) | No |

---

## Excellence Signals from V-01

1. **Column headers enforce field compliance** — Naming explicit column headers (`Signal`, `Namespace`, `Prediction`, `Actual Outcome`, `Verdict`) removes ambiguity; the AI cannot satisfy the table without populating all fields
2. **Template row in the table definition** — Showing `| ... | ... | CORRECT / WRONG / PARTIAL |` as the last row of the column spec locks in the allowed verdict values
3. **Accuracy ratio as a bold labeled formula** — `**Accuracy: N/M = X%**` as a literal template line below the table prevents the AI from restating counts as plain text
4. **All 9 namespace rows pre-listed in the table** — Avoids namespace omission by listing them as table content, not as prose instructions
5. **Section lockdown instruction** — `"Do not add sections. Do not omit sections."` at the end prevents drift; absent from V-02 and V-03
6. **Echo anti-restatement guard** — "not a restatement of a wrong prediction" framing directly blocks the most common Echo failure mode

---

## Delta: V-01 over V-02

V-01's 1-point margin comes from C-14: V-01 names the column `Verdict` explicitly in the table header, making it a field-enforcement mechanism. V-02 requires the same labels in prose ("Give each signal a verdict: CORRECT, WRONG, or PARTIAL") but leaves column naming implicit — passes the spirit, misses column enforcement.

---

```json
{"top_score": 103, "all_essential_pass": true, "new_patterns": ["section-lockdown-prevents-drift"]}
```
