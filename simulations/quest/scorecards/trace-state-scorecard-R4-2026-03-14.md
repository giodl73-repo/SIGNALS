# trace-state Quest Score — Round 4

## Scoring Method

Rubric weights: **Essential 60%** (C-01–C-05, 12% each) · **Recommended 30%** (C-06–C-08, 10% each) · **Aspirational 10%** (C-09–C-19, ~0.91% each). PARTIAL = half-credit.

Trace artifact is `placeholder` — scoring the prompt designs for their ability to elicit compliant outputs.

---

## V-01 — Finance Expert Leads (Role Sequence)

| ID | Tier | Verdict | Evidence |
|----|------|---------|---------|
| C-01 | Essential | PASS | Step template requires `Before: [S-ID]…` and `After: [S-ID]…` for every numbered step |
| C-02 | Essential | PASS | Template requires `Preconditions (state-specific):` and `Postconditions:` per step |
| C-03 | Essential | PASS | Section 2C requires INV-ID table with ≥2 invariants; at least one must be numeric or temporal |
| C-04 | Essential | PASS | ANOMALY FINDER Pass 2 demands explicit found/none verdicts per row; at least one "found" required by quality gate |
| C-05 | Essential | PASS | Role 1 (Finance Expert) anchors entity, vocabulary, and lifecycle in Finance before the analyst starts |
| C-06 | Recommended | PASS | Trace section explicitly requires "one negative path (rejected transition)" with precondition failure named |
| C-07 | Recommended | PASS | "Trace at least 7 operations as numbered steps" with full before/after template; reader can replay step-by-step |
| C-08 | Recommended | PARTIAL | Race condition appears as a sweep row but prompt does not require constructing a concurrent scenario — only detecting one if it exists |
| C-09 | Aspirational | PARTIAL | All four types represented in sweep table; quality gate requires ≥2 found, not all four |
| C-10 | Aspirational | PASS | Sections 2A–2C are full declaration tables for states, operations, invariants |
| C-11 | Aspirational | PASS | ANOMALY FINDER Pass 2 has 5-row sweep table; each row requires an explicit verdict |
| C-12 | Aspirational | PASS | OP-IDs declared in 2B; trace template references OP-IDs; undeclared use surfaces in undeclared-ID row |
| C-13 | Aspirational | PASS | Section 2A has Entry Condition column; at least one non-trivial entry required; anomaly must reference violated entry condition |
| C-14 | Aspirational | PASS | Quality gate states "PASS requires ≥2 rows 'Found'" explicitly |
| C-15 | Aspirational | PASS | Three ID classes (S-ID, OP-ID, INV-ID) declared; all trace, sweep, and register references must use declared IDs |
| C-16 | Aspirational | PASS | Fifth sweep row "Undeclared ID reference" with required found/none verdict |
| C-17 | Aspirational | PASS | Register columns include OP-ID, S-ID, INV-ID; "no blank cells in a found-verdict row" stated; N/A with reason required |
| C-18 | Aspirational | PASS | ANOMALY FINDER Pass 1 reads declarations only and predicts; Pass 2 reads full trace; reconciliation table with Surprise column |
| C-19 | Aspirational | PASS | Strength column in sweep table; quality gate requires ≥1 found row Strength ≥2 |

**Subtotals**:
- Essential: 5/5 × 60% = **60.0%**
- Recommended: 2.5/3 × 30% = **25.0%**
- Aspirational: 10.45/11 × 10% = **9.5%**

**V-01 Total: 94.5 → 95**

---

## V-02 — Evidence-Strength as First-Class Column (Output Format)

The prompt shows Sections 1–3 (entity table, state declarations, operation declarations header). Trace step template, invariant declarations, ANOMALY FINDER, sweep table, and anomaly register are all absent. The evidence-strength scale is defined at the top, which is the defining innovation — but it has no sweep table to attach to in the visible prompt.

| ID | Tier | Verdict | Evidence |
|----|------|---------|---------|
| C-01 | Essential | FAIL | No trace step template shown; before/after format undefined |
| C-02 | Essential | FAIL | No preconditions/postconditions template in visible prompt |
| C-03 | Essential | FAIL | No invariant declaration section shown |
| C-04 | Essential | FAIL | No ANOMALY FINDER section; anomaly detection mechanism absent |
| C-05 | Essential | PASS | Section 1 explicitly names Customer Service domain |
| C-06 | Recommended | FAIL | No negative path requirement shown |
| C-07 | Recommended | FAIL | No step-by-step trace format defined |
| C-08 | Recommended | FAIL | Race condition analysis absent |
| C-09 | Aspirational | FAIL | No anomaly type coverage mechanism |
| C-10 | Aspirational | PARTIAL | Tabular format declared for declaration sections; trace format missing |
| C-11 | Aspirational | FAIL | No sweep table shown |
| C-12 | Aspirational | PARTIAL | OP-ID column present in Section 3 header |
| C-13 | Aspirational | PASS | Section 2 has Entry Condition and Terminal? columns |
| C-14 | Aspirational | FAIL | No minimum-found threshold shown |
| C-15 | Aspirational | PARTIAL | S-IDs in Section 2, OP-IDs started in Section 3; no INV-ID section |
| C-16 | Aspirational | FAIL | No fifth anomaly row |
| C-17 | Aspirational | FAIL | No anomaly register shown |
| C-18 | Aspirational | FAIL | No dual-pass ANOMALY FINDER |
| C-19 | Aspirational | PARTIAL | Strength scale defined upfront with point-of-discovery instruction — genuine innovation — but no sweep table to receive it |

**Subtotals**:
- Essential: 1/5 × 60% = **12.0%**
- Recommended: 0/3 × 30% = **0.0%**
- Aspirational: 2.7/11 × 10% = **2.5%**

**V-02 Total: 14.5 → 15**

---

## Rankings

| Rank | Variation | Score | All Essential Pass |
|------|-----------|-------|--------------------|
| 1 | V-01 Finance Expert Leads | **95** | Yes |
| 2 | V-02 Evidence-Strength First | **15** | No |

---

## Excellence Signals from V-01

**Signal 1 — Numeric/temporal invariant gate in domain expert role**
Requiring at least one invariant that constrains a numeric or temporal value (`amount ≤ budget line remaining`, `payment date ≥ invoice date`) forces the Finance Expert to produce falsifiable invariants before the analyst starts. Generic structural invariants ("data must be valid") cannot satisfy this constraint. This is a domain-specificity gate not present in the base rubric.

**Signal 2 — Surprise column in reconciliation table**
The reconciliation table's `Surprise` column goes beyond binary match/mismatch — it requires labeling each outcome as expected or surprising, creating a calibration signal for the model's prediction quality. C-18 captured the dual-pass structure; the Surprise column is a new annotation layer on top of it.

---

## V-02 Signal (incomplete but real)

**Signal 3 — "Score at point of discovery" anti-retroactive instruction**
Explicitly forbidding retroactive score adjustment ("Do not average or adjust scores after the sweep. Score at point of discovery.") is a novel prompt engineering constraint. If the rest of the prompt were complete, this could improve Strength accuracy because the model reasons about reachability when first encountering the anomaly, not after constructing a narrative. This pattern is worth capturing even though the prompt was cut off.

---

```json
{"top_score": 95, "all_essential_pass": true, "new_patterns": ["numeric/temporal invariant gate in domain expert role — forces domain expert to declare ≥1 invariant constraining a numeric or temporal value, preventing generic structural invariants that cannot fail", "Surprise column in reconciliation table — labels each prediction as expected vs surprising beyond binary match/mismatch, creating a model calibration signal on prediction quality"]}
```
