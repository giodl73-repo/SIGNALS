## Scoring: scout-inertia — R1 Variations

### Methodology

Each variation is evaluated as a **prompt predictor**: how well does the prompt's structure mechanically enforce each rubric criterion in the output? PASS = strong enforcement, PARTIAL = weak or implicit enforcement, FAIL = absent.

Scoring formula: `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/2 × 10)`

PARTIAL counts as 0.5.

---

### V-01 — Inertia Framing (Competitor Zero)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Workaround described concretely | **PASS** | Section 1 explicitly requires "specific tools, manual steps, conventions, scripts"; warns generic statements fail |
| C-02 | Costs quantified 2+ dimensions | **PASS** | "Three line items, each with a numeric estimate or explicit N/A" — adjectives blocked |
| C-03 | Threat score = HIGH | **PASS** | "Absence of a score is an automatic analysis failure" — binary enforcement |
| C-04 | 2+ falsifiable loss conditions | **PASS** | Example given: "When teams have more than 3 concurrent projects" counts; "when teams want simplicity" does not |
| C-05 | 2+ workaround failure modes | **PASS** | Explicitly distinguished from switching costs; concrete example given |
| C-06 | Three cost dimensions separate | **PASS** | Time / Training / Disruption named as three separate line items |
| C-07 | Loss conditions threshold-based | **PASS** | "Falsifiable: a team could check whether it applies" — same framing as rubric |
| C-08 | Forward-looking risk | **PASS** | Section 6 asks for 6-12 month risk with named time horizon |
| C-09 | Failure modes ranked by severity | **FAIL** | Failure modes section asks for 2+ modes with no severity ranking instruction |
| C-10 | Steelman rebutted | **PARTIAL** | Section 7 asks for it and warns weak steelman is worse than none, but no adversarial role structure to force quality |

**Scores:** Essential 60 + Recommended 30 + Aspirational 2.5 = **92.5**

---

### V-02 — Output Format (Table-First)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Workaround described concretely | **PASS** | Prose section; "Do not use 'manual processes' without specifics" |
| C-02 | Costs quantified 2+ dimensions | **PASS** | Table structure; "Use numeric ranges. 'Significant' is not an estimate" |
| C-03 | Threat score = HIGH | **PASS** | Code-block `Threat: HIGH`; "Omitting this field fails the analysis" |
| C-04 | 2+ falsifiable loss conditions | **PASS** | Table with "Observable Threshold" and "Verifiable How" columns |
| C-05 | 2+ workaround failure modes | **PASS** | Table with Trigger column; "Two or more required" |
| C-06 | Three cost dimensions separate | **PASS** | Table rows explicitly named Time / Training / Disruption |
| C-07 | Loss conditions threshold-based | **PASS** | "Observable Threshold" is a named column — structurally impossible to skip |
| C-08 | Forward-looking risk | **PASS** | Section 6 with explicit 6-12 month horizon |
| C-09 | Failure modes ranked by severity | **PASS** | Severity column (HIGH/MED/LOW) in failure mode table — mechanically enforced |
| C-10 | Steelman rebutted | **PARTIAL** | Section 7 marked "*(optional but scored)*" — model may skip; no adversarial forcing |

**Scores:** Essential 60 + Recommended 30 + Aspirational 7.5 = **97.5**

---

### V-03 — Role Sequence (Adversarial First)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Workaround described concretely | **PASS** | Role 1: "Be specific enough that someone else could follow the same process" |
| C-02 | Costs quantified 2+ dimensions | **PASS** | Role 2: three dimensions listed; "Do not use adjectives alone. Numbers or ranges required" |
| C-03 | Threat score = HIGH | **PASS** | "Inertia threat is HIGH by default. Only downgrade with written justification. State the score explicitly" |
| C-04 | 2+ falsifiable loss conditions | **PASS** | "Each condition must be checkable against a real team's situation. Do not restate feature benefits" |
| C-05 | 2+ workaround failure modes | **PASS** | "Find 2+ specific failure modes: edge cases, scale limits, error-prone steps, silent failure conditions" |
| C-06 | Three cost dimensions separate | **PASS** | Time / Training / Disruption listed as three separate items |
| C-07 | Loss conditions threshold-based | **PARTIAL** | "Checkable against a real team's situation" — implicit threshold framing but no "observable threshold" column or explicit examples |
| C-08 | Forward-looking risk | **PASS** | "What happens in 6-12 months for teams that stay on the workaround?" |
| C-09 | Failure modes ranked by severity | **PASS** | Role 2: "Rank by severity" explicit instruction |
| C-10 | Steelman rebutted | **PASS** | Role 1 generates genuine advocate argument independently; Role 2 must "Take the strongest point from the Advocate Brief and specifically rebut it" — anchored to real prior output |

**Scores:** Essential 60 + Recommended 25 + Aspirational 10 = **95**

---

### V-04 — Phrasing Register + Lifecycle Phases

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Workaround described concretely | **PASS** | PHASE 1 has explicit fail condition: "'teams use manual processes' with no specifics" |
| C-02 | Costs quantified 2+ dimensions | **PASS** | PHASE 2 fail condition: "adjectives only ('moderate', 'significant') with no numeric basis" |
| C-03 | Threat score = HIGH | **PASS** | "Threat score: HIGH. This is required. Do not omit. Do not downgrade without a written justification that includes evidence" |
| C-04 | 2+ falsifiable loss conditions | **PASS** | PHASE 4 fail condition: "restating feature benefits instead of stating threshold conditions" — explicitly forbidden |
| C-05 | 2+ workaround failure modes | **PASS** | PHASE 3 fail condition: "'the workaround has limitations' or 'it doesn't scale' without specifics" |
| C-06 | Three cost dimensions separate | **PASS** | Three named dimensions in PHASE 2 |
| C-07 | Loss conditions threshold-based | **PASS** | PHASE 4: "a team could check by looking at observable facts (project count, team size, event frequency, etc.)" — examples given |
| C-08 | Forward-looking risk | **PASS** | PHASE 4: "what happens in 6-12 months... Name the compounding cost or accumulating risk" |
| C-09 | Failure modes ranked by severity | **PASS** | PHASE 3: "rank failure modes by severity: which ones cause data loss or compliance risk vs. which ones are merely inconvenient" |
| C-10 | Steelman rebutted | **FAIL** | No steelman section exists; V-04 has four phases, none of which includes a "case for inertia" |

**Scores:** Essential 60 + Recommended 30 + Aspirational 5 = **95**

---

### V-05 — Combined (Framing + Format + Roles + Phases)

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Workaround described concretely | **PASS** | STEP 1 (Advocate): "Name the workaround and describe it concretely: tools, steps, conventions, scripts. Enough detail to follow the process" |
| C-02 | Costs quantified 2+ dimensions | **PASS** | Table; "Numeric or range-based estimates required. 'Significant' is not an estimate" |
| C-03 | Threat score = HIGH | **PASS** | Code-block `Inertia Threat: HIGH`; "Omitting this field = analysis failure" |
| C-04 | 2+ falsifiable loss conditions | **PASS** | Table with "Observable Threshold" and "How to Verify" columns; "Each condition must be falsifiable" |
| C-05 | 2+ workaround failure modes | **PASS** | Table with Trigger and Severity columns; "'Does not scale' without a scale limit does not pass" |
| C-06 | Three cost dimensions separate | **PASS** | Table rows: Time / Training / Disruption |
| C-07 | Loss conditions threshold-based | **PASS** | "Observable Threshold" is a named column — structurally impossible to satisfy with adjectives |
| C-08 | Forward-looking risk | **PASS** | Section E: "Name a specific compounding cost, growing debt, or divergence risk with a time horizon" |
| C-09 | Failure modes ranked by severity | **PASS** | Severity column in failure mode table; "Severity column required" |
| C-10 | Steelman rebutted | **PASS** | STEP 1 generates genuine advocate argument first; Section F: "Take the strongest point from the Advocate Pass. Rebut it specifically... The rebuttal must address the point directly, not redirect to a different benefit" |

**Scores:** Essential 60 + Recommended 30 + Aspirational 10 = **100**

---

### Composite Scores & Ranking

| Rank | Variation | Essential | Recommended | Aspirational | Total | Band |
|------|-----------|-----------|-------------|--------------|-------|------|
| 1 | **V-05** | 60 (5/5) | 30 (3/3) | 10 (2/2) | **100** | Gold |
| 2 | **V-02** | 60 (5/5) | 30 (3/3) | 7.5 | **97.5** | Gold |
| 3 | **V-03** | 60 (5/5) | 25 (C-07 partial) | 10 (2/2) | **95** | Gold |
| 3 | **V-04** | 60 (5/5) | 30 (3/3) | 5 (C-10 fail) | **95** | Gold |
| 5 | **V-01** | 60 (5/5) | 30 (3/3) | 2.5 | **92.5** | Gold |

All five variations pass all essential criteria. All reach Gold band.

---

### Excellence Signals — V-05

**1. Table column names that directly instantiate rubric dimensions**

V-05's failure mode table has a required "Severity" column; its loss-conditions table has a required "Observable Threshold" column. These columns don't just request the criterion — they make any output that omits them structurally malformed. C-09 and C-07 become impossible to accidentally fail without violating the format constraint. This is stronger than instruction enforcement because the violation is visible in the table structure itself.

**2. Two-pass adversarial role structure anchors the steelman to independent prior output**

V-03 and V-05 both use the Advocate role. The key difference in V-05: Step 1 generates the workaround profile and the strongest objection to switching *as a complete output* before Step 2 runs. Step 2 then reads that output. The rebuttal is therefore anchored to an argument the model actually made, not one it constructs retroactively to rebut. This produces higher C-10 quality than "write the steelman and then rebut it" in a single pass.

**3. Rebuttal quality constraint prevents redirect**

V-05 Section F adds: "The rebuttal must address the point directly, not redirect to a different benefit." This constraint eliminates the most common C-10 failure mode — appearing to rebut the steelman by listing feature benefits that don't address the specific objection raised.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Table column names that directly map to rubric dimensions (e.g., 'Observable Threshold', 'Severity') make criterion satisfaction structurally enforced — a malformed table is visibly wrong, stronger than instruction-only enforcement", "Two-pass adversarial role structure anchors the rebuttal to an argument generated independently in Step 1, producing higher steelman quality than constructing advocate and rebuttal in a single pass", "Explicit rebuttal constraint ('address the point directly, not redirect to a different benefit') prevents the most common C-10 failure mode where outputs appear to rebut by listing unrelated feature benefits"]}
```
