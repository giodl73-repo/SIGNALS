## campaign-validate — Round 4 Scorecard

---

### Pre-scoring read

Three new v4 aspirational criteria added: C-17 (criterion-cascade-by-schema), C-18 (required-columns-as-inertia-enforcement), C-19 (pre-declared-rows-as-completeness-gate). Max = 145. Golden = all essential pass + composite ≥ 80.

**Critical observation before scoring:** Both V-01 and V-02 include `review-customers` as a sub-skill but omit `review-code`. The rubric's C-01 pass condition explicitly requires: "review-design, review-users, listen-feedback, listen-adoption, **review-code**." This is an unconditional fail on C-01 for both variations.

---

## V-01 — Adoption-first ordering

### Essential (12 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **FAIL** | Sub-skills listed: listen-adoption, listen-feedback, review-users, review-customers, review-design. `review-code` absent; `review-customers` substituted. Unconditional fail. |
| C-02 | **PASS** | Ranked findings table explicitly: "Rank ALL findings across all five sub-skills by adoption impact, not severity." Severity "may be noted but must not govern rank order" is reflected in "Adoption Impact" and "Segment Affected (~N%)" columns. |
| C-03 | **PASS** | Explicit GO / NO-GO / CONDITIONAL GO with named rule set per verdict: "GO: no P1 finding blocks the Early Majority." Condition must be specific and actionable. Unambiguous. |
| C-04 | **PASS** | "Source sub-skill" column in ranked findings table. NO-GO/CONDITIONAL GO section requires top-3 blocker attribution by name. |
| C-05 | **PASS** | "Write the complete validation brief to: `simulations/{topic}/validate-{date}.md`" + explicit `Confirm with:` string. |

**Essential subtotal: 48 / 60**

---

### Recommended (10 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** | Dedicated "Cross-signal synthesis" section required; "must identify a relationship not visible in any single sub-skill output." Anti-concatenation rule stated. |
| C-07 | **PASS** | Each sub-skill has a labeled section with explicit heading instruction: `**listen-adoption findings**`, etc. |
| C-08 | **PASS** | review-users section: "Score each finding: P1 (blocks usage), P2 (degrades usage), P3 (polish item)." P1/P2/P3 definitions present. |

**Recommended subtotal: 30 / 30**

---

### Aspirational (5 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | listen-adoption asks for "rough % of total addressable user base" per segment. Ranked findings table column: "Segment Affected (~N%)." Format requirement met. |
| C-10 | **PARTIAL** | Remediation implied only in CONDITIONAL GO verdict framing ("defined remediation paths"). No dedicated remediation column in ranked findings table. Partial credit: 3 pts. |
| C-11 | **FAIL** | No pre-declared table skeleton per sub-skill. Each sub-skill produces prose sections, not structured rows. |
| C-12 | **PASS** | Ranked findings table separates "Severity" and "Adoption Impact" into distinct columns. Adoption Impact is not derived from or merged with Severity. |
| C-13 | **PASS** | "Confirm with: `Artifact written: simulations/{topic}/validate-{date}.md`" — exact string format specified. |
| C-14 | **PASS** | Explicit: "Separate listen-feedback findings from listen-adoption findings. Do not merge these two sections." Categorical distinction stated with prohibition. |
| C-15 | **PASS** | All five Rogers segments named explicitly in listen-adoption phase: Innovators, Early Adopters, Early Majority, Late Majority, Laggards. % anchors requested per segment. |
| C-16 | **PASS** | listen-adoption: "Name the status-quo workaround this segment uses today." Ranked findings table: "Status-Quo Workaround" as required column. |
| C-17 | **PARTIAL** | Partial cascade: listen-adoption with Rogers segments causes C-15 and C-09 to emerge together. But not designed as a deliberate schema decision that satisfies a criterion cluster — it's sequencing logic, not schema architecture. 3 pts. |
| C-18 | **PASS** | "Status-Quo Workaround" and "Switching Cost" declared as required columns in ranked findings table. Explicitly noted as required "for every row — not just P1s." Systematic enforcement present. |
| C-19 | **PARTIAL** | Rogers segments named in prose instructions for listen-adoption but not pre-declared as table rows with blank mandatory fields. Missing rows would not be visually detectable. 3 pts. |

**Aspirational subtotal: 5+3+0+5+5+5+5+5+3+5+3 = 44 / 55**

### V-01 Composite: **122 / 145**
**Golden: NO** — C-01 fails (review-code absent).

---

## V-02 — Table skeleton with pre-declared rows

### Essential (12 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **FAIL** | Table 1 rows: review-design, review-users, review-customers, listen-feedback, listen-adoption. `review-code` absent. |
| C-02 | **PASS** | Table 2: "Rank 1 = highest adoption impact. Severity column is informational — it does not govern rank." |
| C-03 | **FAIL** | No go/no-go verdict section present in the variation text. V-02 ends at Table 5. |
| C-04 | **PASS** | Table 3 "P1 blockers with remediation paths" includes "Source sub-skill" as a required column. Attribution mechanism present for P1 blockers. |
| C-05 | **FAIL** | No artifact write instruction or confirmation string present in variation text. |

**Essential subtotal: 24 / 60**

---

### Recommended (10 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** | Table 4 "Cross-signal synthesis" required with minimum 1 row. Anti-concatenation rule: "each row must name a relationship not visible in either sub-skill alone." |
| C-07 | **PASS** | Table 1 pre-declares all sub-skills as labeled rows. Reader can navigate directly to each sub-skill's summary. |
| C-08 | **PASS** | Table 2 column: "Severity (P1/P2/P3)." Tiers explicitly named. |

**Recommended subtotal: 30 / 30**

---

### Aspirational (5 pts each)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | Table 5 column "~% of base" per segment. Table 2 column "Segment blocked (~N%)." Both quantify adoption impact with segment+% format. |
| C-10 | **PASS** | Table 3 has dedicated "Remediation path" column per P1 blocker. Not limited to verdict framing — present for every blocker row. |
| C-11 | **PASS** | Table 1 pre-declares all five sub-skills as rows. Blank mandatory row = visible gap, not absent prose. Skeleton-as-completeness-gate. |
| C-12 | **PASS** | Table 2 separates "Severity (P1/P2/P3)" and "Adoption Impact" into distinct columns. |
| C-13 | **FAIL** | No artifact confirmation string present in visible text. |
| C-14 | **PASS** | listen-feedback and listen-adoption appear as separate rows in Table 1. Table 5 covers adoption curve independently. Categorical separation structurally enforced. |
| C-15 | **PASS** | Table 5 pre-declares all five Rogers segments as mandatory named rows. |
| C-16 | **PASS** | "Status-Quo Workaround" required column in Table 2 (every finding row) and Table 5 (every segment row). |
| C-17 | **PASS** | Table 5 exemplifies criterion-cascade: pre-declaring Rogers rows + adding Status-Quo Workaround + Switching Cost columns cascades C-09 (% per segment), C-15 (all five named), C-16 (workaround per blocker), and C-18 (switching cost as column) simultaneously. Schema decision → criterion cluster. |
| C-18 | **PASS** | "Status-Quo Workaround" and "Switching Cost" are required columns in Tables 2 and 5. Required column instructions explicitly stated: "Required for every row — not just P1s." |
| C-19 | **PASS** | Rogers segments pre-declared as named rows in Table 5. Sub-skills pre-declared as named rows in Table 1. Severity tiers not pre-declared but Tables 1 and 5 fully implement the pattern. |

**Aspirational subtotal: 5+5+5+5+0+5+5+5+5+5+5 = 50 / 55**

### V-02 Composite: **104 / 145**
**Golden: NO** — C-01, C-03, C-05 fail.

---

## Summary Table

| Variation | Essential | Recommended | Aspirational | Total | Golden |
|-----------|-----------|-------------|--------------|-------|--------|
| V-01 | 48/60 | 30/30 | 44/55 | **122** | NO (C-01) |
| V-02 | 24/60 | 30/30 | 50/55 | **104** | NO (C-01, C-03, C-05) |

**Rank: V-01 > V-02**

---

## Excellence Signals

**V-01 made it better through:**

1. **Complete synthesis pipeline** — V-01 includes cross-signal synthesis, go/no-go verdict with explicit rules, and artifact write. V-02 omits all three, losing 36 essential points. The skeleton pattern only wins if the skeleton covers the full output.

2. **Adoption-first sequencing as framing constraint** — Running listen-adoption before review-design forces the model to frame design findings in terms of adoption barriers rather than retrofitting adoption language after design critique. This structurally supports C-02 (ranked by adoption impact) and C-14 (listen-feedback vs listen-adoption separation) without requiring post-hoc reordering.

3. **Explicit merge-prohibition** — "Do not merge these two sections. listen-feedback is retrospective... listen-adoption is predictive." The prohibition is stronger than a heading alone. Headings can be followed with merged prose; the prohibition can't.

4. **Column completeness enforcement** — "Required for every row — not just P1s" applied to Status-Quo Workaround. This pushes C-18 beyond an aspirational pass into a behavioral constraint that prevents selective application.

**V-02's structural advantage** — Despite lower total score, V-02 demonstrates the canonical C-17 pattern (Table 5 with pre-declared Rogers rows + required columns cascades four criteria simultaneously). V-02 is the better template for aspirational criteria; V-01 is the better template for essential criteria. A composite variation combining V-01's synthesis pipeline with V-02's table skeleton would score near-maximum on both tiers.

---

## New Pattern Candidates

**`adoption-first-sequencing-as-framing-constraint`** — Sub-skill execution order is a design decision, not just an implementation detail. Running adoption analysis before review sub-skills forces findings to be expressed in adoption-barrier terms from the start. The sequence constraint is a rubric-shaping mechanism: it causes C-02 (adoption-impact ranking) to emerge naturally rather than require explicit post-hoc instruction. No current rubric criterion captures sequencing order as a quality mechanism.

---

```json
{"top_score": 122, "all_essential_pass": false, "new_patterns": ["adoption-first-sequencing-as-framing-constraint"]}
```
