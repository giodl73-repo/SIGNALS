## scout-inertia R2 — Quest Score (rubric v2)

---

### Rubric Summary

| Tier | Criteria | Weight |
|------|----------|--------|
| Essential | C-01 (workaround described), C-02 (switching cost quantified), C-03 (threat = HIGH), C-04 (why inertia loses), C-05 (failure modes) | 60 pts |
| Recommended | C-06 (costs 3 dimensions), C-07 (threshold-based conditions), C-08 (long-term risk) | 30 pts |
| Aspirational | C-09 (severity ranked), C-10 (steelman rebutted), C-11 (verification method), C-12 (anchored rebuttal), C-13 (replication fidelity) | 10 pts |

Formula: `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/5 × 10)`

---

### V-01 — Replication Fidelity Standard (C-13 axis)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Workaround Concretely Described | PASS | Replication Fidelity Standard is a superset of C-01 — forces product names, enumerated steps |
| C-02 | Switching Cost Quantified | PASS | Explicit three line items with numeric estimate or N/A + justification |
| C-03 | Threat Score = HIGH | PASS | Section 3 assigns HIGH explicitly; downgrade requires written justification |
| C-04 | Why Inertia Loses | PASS | "2+ specific conditions... falsifiable" with threshold example included |
| C-05 | Failure Modes Identified | PASS | "2+ specific ways... name what triggers it and its severity" |
| C-06 | Cost Dimensions Separate | PASS | Time / Training / Disruption as three named line items |
| C-07 | Threshold-Based Conditions | PASS | Example "When teams have more than 3 concurrent projects" anchors standard |
| C-08 | Long-Term Risk | PASS | Section 6 requires compounding cost with 6-12 month horizon |
| C-09 | Severity Ranked | PASS | "severity (HIGH = data loss; MED = incorrect results; LOW = inefficiency only)" |
| C-10 | Steelman Rebutted | PASS | Section 7 "Case for Staying" — explicitly labeled, requires specific rebuttal, flags weak steelman |
| C-11 | Verification Method | FAIL | No Verification Command column or format; threshold-based conditions only |
| C-12 | Rebuttal Anchored to Named Claim | FAIL | "rebut it specifically" — no STRONGEST CLAIM extraction or NAMED CLAIM copy mechanism |
| C-13 | Replication Fidelity | PASS | Three-item checklist enforced: product names, numbered steps, institutional knowledge flagged |

**Aspirational count**: C-09 PASS, C-10 PASS, C-11 FAIL, C-12 FAIL, C-13 PASS → 3/5

**Score**: (5/5 × 60) + (3/3 × 30) + (3/5 × 10) = 60 + 30 + 6 = **96**

---

### V-02 — Verification Command Column (C-11 axis)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Workaround Concretely Described | PASS | "One paragraph... enough detail that a reader can picture the workflow" |
| C-02 | Switching Cost Quantified | PASS | 3-row table required; "Significant is not an estimate" |
| C-03 | Threat Score = HIGH | PASS | Code block `Threat: HIGH` required; omitting = analysis failure |
| C-04 | Why Inertia Loses | PASS | 4-column table, each condition must be falsifiable |
| C-05 | Failure Modes Identified | PASS | 4-column table, 2+ rows, specific trigger + severity |
| C-06 | Cost Dimensions Separate | PASS | Three rows forced by table structure |
| C-07 | Threshold-Based Conditions | PASS | "Observable Threshold" column explicitly required |
| C-08 | Long-Term Risk | PASS | Section 6 paragraph with 6-12 month horizon |
| C-09 | Severity Ranked | PASS | Severity column in failure mode table with HIGH/MED/LOW |
| C-10 | Steelman Rebutted | PARTIAL | Section 7 labeled "(optional but scored)" — if model treats optional literally, steelman absent; prompt creates structural unreliability |
| C-11 | Verification Method | PASS | "Verification Command" column with `[Tool/artifact]: [Action] → [Result]` format, passing/failing examples, named failure condition |
| C-12 | Rebuttal Anchored to Named Claim | FAIL | "The strongest argument... then the specific rebuttal" — no NAMED CLAIM extraction, no copy mechanism |
| C-13 | Replication Fidelity | FAIL | Workaround section stays at C-01 level ("reader can picture") — no product-naming mandate, no step enumeration, no institutional knowledge flag |

**Aspirational count**: C-09 PASS, C-10 PARTIAL (0.5), C-11 PASS, C-12 FAIL, C-13 FAIL → 2.5/5

**Score**: (5/5 × 60) + (3/3 × 30) + (2.5/5 × 10) = 60 + 30 + 5 = **95**

---

### V-03 — Anchored Rebuttal Sequence (C-12 axis)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Workaround Concretely Described | PASS | Role 1 "tools, commands, conventions, manual steps... specific enough that someone else could follow" |
| C-02 | Switching Cost Quantified | PASS | Role 2 requires numeric/range estimates; "adjectives alone" fail condition |
| C-03 | Threat Score = HIGH | PASS | Role 2 Step 1 assigns HIGH by default; downgrade requires justification |
| C-04 | Why Inertia Loses | PASS | Role 2 Step 4 "2+ falsifiable conditions checkable against a real team's situation" |
| C-05 | Failure Modes Identified | PASS | Role 2 Step 3 "2+ specific failure modes... edge cases, scale limits, error-prone steps, silent failure" |
| C-06 | Cost Dimensions Separate | PASS | Time / Training / Disruption as explicit bullets |
| C-07 | Threshold-Based Conditions | PASS | "Falsifiable — checkable against a real team's situation" implies threshold; Role 1 Step 4 adds holding conditions |
| C-08 | Long-Term Risk | PASS | Role 2 Step 5 "What happens in 6-12 months for teams that stay" |
| C-09 | Severity Ranked | PASS | "Rank by severity" with HIGH/MED/LOW classification in Role 2 |
| C-10 | Steelman Rebutted | PASS | Full adversarial sequence; Role 1 writes advocate case; Role 2 performs anchored rebuttal |
| C-11 | Verification Method | FAIL | No Verification Command column; conditions are falsifiable but no tool/action format required |
| C-12 | Rebuttal Anchored to Named Claim | PASS | STRONGEST CLAIM label in Role 1 → NAMED CLAIM verbatim copy in Role 2 Step 6 → rebuttal constraint "do not address a weaker point instead" |
| C-13 | Replication Fidelity | PARTIAL | "tools, commands, conventions, manual steps... specific enough that someone else could follow" covers product naming and step enumeration but does not explicitly require institutional knowledge flagging |

**Aspirational count**: C-09 PASS, C-10 PASS, C-11 FAIL, C-12 PASS, C-13 PARTIAL (0.5) → 3.5/5

**Score**: (5/5 × 60) + (3/3 × 30) + (3.5/5 × 10) = 60 + 30 + 7 = **97**

---

### V-04 — Combined C-11 + C-12, Phase Structure (C-11 + C-12 axes)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Workaround Concretely Described | PASS | Phase 1 "tools involved, manual steps, conventions... enough that a reader unfamiliar can picture" |
| C-02 | Switching Cost Quantified | PASS | Phase 2 three dimensions with numeric or N/A + justification |
| C-03 | Threat Score = HIGH | PASS | Phase 2 "Threat score: HIGH. Required. Do not omit." |
| C-04 | Why Inertia Loses | PASS | Phase 4 Part A table, 2+ falsifiable conditions |
| C-05 | Failure Modes Identified | PASS | Phase 3 "2+ specific failure modes... name what triggers it" |
| C-06 | Cost Dimensions Separate | PASS | Three explicitly named dimensions in Phase 2 |
| C-07 | Threshold-Based Conditions | PASS | "Observable Threshold" column in Phase 4 table |
| C-08 | Long-Term Risk | PASS | Phase 4 Part C "What accumulates over 6-12 months" |
| C-09 | Severity Ranked | PASS | Phase 3 "Rank failure modes by severity: HIGH / MED / LOW" |
| C-10 | Steelman Rebutted | PASS | Phase 4 Part B step 1 writes STEELMAN; step 3 rebuts the NAMED CLAIM |
| C-11 | Verification Method | PASS | "Verification Command" column in Phase 4 table with format, fail conditions, examples inline |
| C-12 | Rebuttal Anchored to Named Claim | PASS | Three-step STEELMAN → NAMED CLAIM: "[exact text]" → rebuttal-of-named-claim; "do not address a weaker point instead" |
| C-13 | Replication Fidelity | FAIL | Phase 1 stays at C-01 level: "reader can picture" — no Replication Fidelity Standard, no product-name mandate, no institutional knowledge flag |

**Aspirational count**: C-09 PASS, C-10 PASS, C-11 PASS, C-12 PASS, C-13 FAIL → 4/5

**Score**: (5/5 × 60) + (3/3 × 30) + (4/5 × 10) = 60 + 30 + 8 = **98**

---

### V-05 — Full Combined: R1 V-05 Scaffold + C-11 + C-12 + C-13

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Workaround Concretely Described | PASS | Replication Fidelity Standard is a superset of C-01 |
| C-02 | Switching Cost Quantified | PASS | Section A table; "Significant is not an estimate" |
| C-03 | Threat Score = HIGH | PASS | Section B code block; "Omitting this field = analysis failure" |
| C-04 | Why Inertia Loses | PASS | Section D table, 2+ rows, each falsifiable |
| C-05 | Failure Modes Identified | PASS | Section C table, minimum 2 rows, severity column required |
| C-06 | Cost Dimensions Separate | PASS | Three-row table in Section A; all rows required |
| C-07 | Threshold-Based Conditions | PASS | "Observable Threshold" column in Section D |
| C-08 | Long-Term Risk | PASS | Section E "What accumulates over 6-12 months" |
| C-09 | Severity Ranked | PASS | Section C severity column with HIGH/MED/+ |
| C-10 | Steelman Rebutted | PASS | Two-pass structure: Advocate writes it; Analyst rebuts via Section F |
| C-11 | Verification Method | PASS | Section D "Verification Command" column with `[Tool]: [Action] → [Result]` format, passing/failing examples, "without a follow-up question" constraint |
| C-12 | Rebuttal Anchored to Named Claim | PASS | STRONGEST CLAIM in Step 1 Advocate → NAMED CLAIM verbatim copy in Step 2 Section F → "traceable to the named claim" constraint |
| C-13 | Replication Fidelity | PASS | Full Replication Fidelity Standard: product names (not categories), numbered sequence, institutional knowledge flagged — three-item checklist explicit |

**Aspirational count**: C-09 PASS, C-10 PASS, C-11 PASS, C-12 PASS, C-13 PASS → 5/5

**Score**: (5/5 × 60) + (3/3 × 30) + (5/5 × 10) = 60 + 30 + 10 = **100**

---

### Variation Rankings

| Rank | Variation | Score | Band | C-11 | C-12 | C-13 |
|------|-----------|-------|------|------|------|------|
| 1 | V-05 | 100 | Gold | PASS | PASS | PASS |
| 2 | V-04 | 98 | Gold | PASS | PASS | FAIL |
| 3 | V-03 | 97 | Gold | FAIL | PASS | PARTIAL |
| 4 | V-01 | 96 | Gold | FAIL | FAIL | PASS |
| 5 | V-02 | 95 | Gold | PASS | FAIL | FAIL |

All five variations pass all essential criteria. All achieve Gold band.

---

### Excellence Signals from V-05

**Signal 1 — Format constraints eliminate structural loopholes**

Naming what's needed (R1: "Verifiable How") is not enough; naming the column allows generic text to pass inspection. V-05's `[Tool]: [Action] → [What you see when threshold applies]` format makes non-compliance visibly malformed — a cell reading "you can check project count" fails the pattern match without judgment. Format constraint > instruction is the generalizable principle.

**Signal 2 — Verbatim copy-before-rebut prevents paraphrase drift**

Generic rebuttal instructions ("rebut it specifically") permit the model to rebut a weaker paraphrase or the steelman category rather than its strongest claim. The STRONGEST CLAIM label in the Advocate Pass forces distillation to one declarative sentence. The NAMED CLAIM verbatim copy mandate in the Analyst Pass makes non-traceability structurally impossible — the reader can match rebuttal to claim by construction, not by judgment.

**Signal 3 — Two-pass role structure places each mechanism in its natural home**

The Advocate Pass is the natural location for replication-fidelity workaround description and STRONGEST CLAIM extraction. The Analyst Pass is the natural location for quantified costs, verification commands, failure modes, and anchored rebuttal. V-05's two-pass structure assigns all three new mechanisms to the role where they arise from the perspective of the role-holder, reducing friction and increasing compliance probability.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Format constraints eliminate structural loopholes: requiring [Tool]: [Action] -> [Result] makes non-compliance visibly malformed rather than requiring judgment", "Verbatim copy-before-rebut prevents paraphrase drift: NAMED CLAIM copy step makes claim-to-rebuttal link traceable by construction"]}
```
