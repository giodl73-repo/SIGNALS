# Quest:Score — scout-size R4

**Rubric**: v4 (16 criteria: 5 Essential, 3 Recommended, 8 Aspirational)
**Variations received**: V-01 (full prompt), V-02 (full prompt), V-03 (hypothesis only — no prompt text), V-04/V-05 (absent)

> **Note**: Only V-01 and V-02 carry complete prompt text. V-03 is scored as INCOMPLETE. V-04 and V-05 are absent and excluded from ranking.

---

## Scoring Method

Each criterion is evaluated against the **prompt's constraints** — whether the prompt text is strong enough to elicit compliant output. PASS = the prompt explicitly requires and guards the criterion. PARTIAL = the prompt implies but does not guard against the failure mode. FAIL = the prompt is silent on the criterion.

---

## V-01 — Inertia-First Framing

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Surface area enumerated | PASS | Step 2 requires naming each integration point individually by type, with "N integration points" total count as closing requirement |
| C-02 | Complexity tier on-scale | PASS | "Assign exactly one tier from this set: LOW / MEDIUM / HIGH / XL — No other vocabulary is valid" with explicit failure examples |
| C-03 | Inertia check present | PASS | Step 1 is the first output, requires workaround name AND cost direction (cheaper/comparable/more expensive), explicitly fails "in passing" mentions |
| C-04 | Confidence stated with basis | PASS | Step 7 requires HIGH/MEDIUM/LOW + Basis field defined as "concrete and named" — generic basis fails |
| C-05 | Signal boundary respected | PASS | Opening prohibition: "Do not include task lists, sprint assignments, owner names, or milestone dates anywhere in your output" |
| C-06 | Team-size names disciplines | PASS | Step 5 requires disciplines + allocation fractions; "Headcount alone ('3 engineers') fails" |
| C-07 | Timeline as sprint range | PASS | Step 6: "X–Y sprints. Not a calendar date. Not a single fixed number." |
| C-08 | Primary driver identified | PASS | Step 4: "Name the one or two specific factors that most drive the complexity tier"; "It's complex" explicitly fails |
| C-09 | Sensitivity tier up + down | PASS | Step 8: "exactly one condition... UP and exactly one... DOWN" |
| C-10 | Confidence calibration | PASS | Step 9: "Name what information or investigation result would materially raise or lower your stated confidence level" |
| C-11 | Confidence gap named | PASS | Gap field defined as "specific thing that, if verified, would most change your confidence" |
| C-12 | Sensitivity single named conditions | PASS | Requirement 1 in Step 8: "Single named condition — not a list of factors or a vague hedge" with pass/fail example |
| C-13 | Sensitivity names explicit tier destination | PASS | Requirement 2: "'Tier rises to [XL/HIGH/MEDIUM/LOW].' 'Could rise' without naming where it goes fails" |
| C-14 | Sensitivity conditions falsifiable | PASS | Requirement 4: "something a team member could investigate and settle"; "if requirements change" explicitly fails |
| C-15 | Basis and gap non-overlapping | PASS | Inline constraint block: "The gap must address a different dimension than the basis" with API contract example showing the failure mode |
| C-16 | Sensitivity destination differs from current tier | PASS | Requirement 3: "the destination tier must be different from the tier you assigned in Step 3. If you rated the feature HIGH, a tier-up condition must name XL" |

**Essential**: 5/5 PASS
**Recommended**: 3/3 PASS
**Aspirational**: 8/8 PASS

```
composite = (5/5 × 60) + (3/3 × 30) + (8/8 × 10) = 60 + 30 + 10 = 100
```

**Score: 100** | Golden: YES (all essential pass, composite >= 80)

---

## V-02 — Structured Table Output Format

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Surface area enumerated | PASS | Section 2 table schema requires named rows + total row with "N integration points" |
| C-02 | Complexity tier on-scale | PASS | Table field: "LOW / MEDIUM / HIGH / XL" with "Use only this vocabulary — no other phrasing" |
| C-03 | Inertia check present | PASS | Section 1 table has "Cost direction" column with only three valid values; "cost direction field must be filled with one of the three options above" |
| C-04 | Confidence stated with basis | PASS | Table field "Confidence Level" + "Basis" with "Must be concrete and named; must identify a specific known thing" constraint |
| C-05 | Signal boundary respected | PASS | Opening: "Your output must not contain task lists, sprint assignments, owner names, or milestone dates" |
| C-06 | Team-size names disciplines | PASS | Table field with example "1 backend, 1 platform, 0.5 PM" and "Disciplines required, not headcount alone" |
| C-07 | Timeline as sprint range | PASS | Table field: "Sprint range only — no calendar dates, no point estimates" |
| C-08 | Primary driver identified | PASS | Table field: "Not 'it's complex' — name the factor" |
| C-09 | Sensitivity tier up + down | PASS | Table has explicit Tier UP and Tier DOWN rows |
| C-10 | Confidence calibration | PASS | Section 6 dedicated to this output |
| C-11 | Confidence gap named | PASS | Gap field with explicit constraint; API contract counter-example names the failure |
| C-12 | Sensitivity single named conditions | PASS | Constraint: "Each condition is a single named scenario — not a list of factors or a vague hedge" |
| C-13 | Sensitivity names explicit tier destination | PASS | "Destination Tier" is a named column; column headers show "[HIGH or XL — must be higher than current tier]" and "[MEDIUM or LOW — must be lower]" |
| C-14 | Sensitivity conditions falsifiable | PASS | "Falsifiable — how to settle it" is a named column; "if requirements change" explicitly fails |
| C-15 | Basis and gap non-overlapping | PASS | Block constraint with explicit fail example: "Writing 'Basis: API contract confirmed; Gap: API contract not yet verified' fills both fields from the same dimension and fails" |
| C-16 | Sensitivity destination differs from current tier | PASS | "Destination tier must differ from the complexity tier assigned in Section 3 — mapping a tier to itself is not a sensitivity" |

**Essential**: 5/5 PASS
**Recommended**: 3/3 PASS
**Aspirational**: 8/8 PASS

```
composite = (5/5 × 60) + (3/3 × 30) + (8/8 × 10) = 60 + 30 + 10 = 100
```

**Score: 100** | Golden: YES (all essential pass, composite >= 80)

---

## V-03 — Conversational / Imperative Register

**Status: INCOMPLETE** — Prompt text not provided. Variation axis and hypothesis are present; no scorable content.

Estimated exposure: C-11, C-15, C-16 are the highest-risk criteria in a conversational register because the anti-conflation guard and tier-movement requirement have historically depended on explicit structural framing. A pure question list ("What's the gap?") may leave these underspecified without the inline constraint language present in V-01 and V-02.

**Score: NOT SCORED**

---

## V-04, V-05

**Status: ABSENT** — Not included in input. Not scored.

---

## Ranking

| Rank | Variation | Score | Golden | Notes |
|------|-----------|-------|--------|-------|
| 1 (tie) | V-01 | 100 | YES | Inertia-first ordering; bundled 4-requirement constraint block in Step 8 |
| 1 (tie) | V-02 | 100 | YES | Table schema enforcement; destination tier and falsifiable as named columns |
| — | V-03 | N/A | — | Incomplete |
| — | V-04 | N/A | — | Absent |
| — | V-05 | N/A | — | Absent |

---

## Excellence Signals

Both V-01 and V-02 achieve structural perfection on all 16 criteria. Two distinct patterns emerge that explain why:

### Pattern 1 — Bundled constraint blocks (V-01)

V-01's Step 8 groups all four sensitivity requirements into a single numbered list (single named condition + explicit destination + destination differs + falsifiable). This is not four separate rules scattered through the output format — it is one structural unit that must all be satisfied before the sensitivity passes. A model reading Step 8 encounters the constraints as a checklist, making partial compliance immediately visible as incomplete compliance.

### Pattern 2 — Schema-enforced slot filling (V-02)

V-02's sensitivity table makes C-13 and C-16 structural rather than prose conventions. The column header "[HIGH or XL — must be higher than current tier]" means the model is not writing free text that happens to contain a tier name — it is filling a column that is labeled with the constraint. The "Falsifiable — how to settle it" column makes C-14 a schema requirement rather than an inline instruction. Empty cells in a table are conspicuously absent in a way that omitted prose is not.

### Differentiator

Neither pattern is strictly superior — they guard against different failure modes. V-01's bundled block is cleaner for models that read linearly and may skip inline callouts. V-02's table schema is more resistant to prompt-following shortcuts where a model answers the question but misses the constraint buried in parentheses. A V-04/V-05 combining both would be worth testing.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["bundled constraint blocks: grouping multi-criterion requirements into a single numbered list makes partial compliance immediately visible as incomplete", "schema-enforced slot filling: table column headers carrying the constraint rule make criteria structural rather than prose conventions, making omission conspicuous"]}
```
