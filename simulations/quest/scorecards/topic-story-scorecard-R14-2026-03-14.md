# /quest:score — topic-story — Round 14
**Rubric**: v14 | **Criteria**: 46 (4 essential, 3 recommended, 39 aspirational) | **Date**: 2026-03-15

---

## Criterion Evaluation

### Essential (C-01–C-04) — 15 pts each, 60 pts total

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 | PASS | PASS | PASS | PASS | PASS |
| C-02 | PASS | PASS | PASS | PASS | PASS |
| C-03 | PASS | PASS | PASS | PASS | PASS |
| C-04 | PASS | PASS | PASS | PASS | PASS |

All variations: essential subtotal = **60.0**. No essential failures.

---

### Recommended (C-05–C-07) — 10 pts each, 30 pts total

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-05 | PASS | PASS | PASS | PASS | PASS |
| C-06 | PASS | PASS | PASS | PASS | PASS |
| C-07 | PASS | PASS | PASS | PASS | PASS |

All variations: recommended subtotal = **30.0**. All at baseline.

---

### Aspirational (C-08–C-46) — 0.2564 pts each, 10 pts total

The inherited V-05 R13 baseline passes all 39 aspirational criteria under v14. The single axis of differentiation among R14 variations is **C-38** (cell-level entry conditions).

#### C-38 — Cell-Level Entry Conditions (three-coordinate: axis + row + field-name)

| Variation | Entry conditions | Verdict | Evidence |
|-----------|-----------------|---------|----------|
| V-01 | S2: "Signal inventory axis, S1 row, **Status field** — non-empty"; S3: "Signal survey axis, S2 row, **Key Finding field** — non-empty"; S4: "Pattern synthesis axis, S3 row, **pattern-claim sentence** — present" | **PASS** | All three section gates name axis + row + specific field-name |
| V-02 | S2: "Signal inventory axis, S1 row — all fields complete"; S3: "Signal survey axis, S2 row — all key findings and Inertia? flags recorded" | **PARTIAL** | Row-level conditions; named fields grouped as compound ("all fields"), not resolved to a single named column |
| V-03 | S2: "Signal inventory axis, S1 row — all fields complete"; S3: "Signal survey axis, S2 row — all key findings recorded and weights assigned" | **PARTIAL** | Row-level conditions; two fields named conjunctively, not as a three-coordinate single-field reference |
| V-04 | S2: "Signal registry axis, S1 row, **Status field** — non-empty"; S3: "Signal survey axis, S2 row, **Key Finding field** — non-empty"; S4: "Pattern synthesis axis, S3 row, **pattern-claim sentence** — present" | **PASS** | Cell-level throughout; exact field-name as third coordinate at every gate |
| V-05 | S2: "Signal inventory axis, S1 row, **Status field** — non-empty"; S3: "Signal survey axis, S2 row, **Key Finding field** — non-empty"; S4: "Pattern synthesis axis, S3 row, **pattern-claim sentence** — present" | **PASS** | Formal register produces precise three-coordinate references at every gate |

#### C-45 — Verbatim Hedge Prohibition Enumerates ≥2 Structurally Distinct Opening Patterns

| Variation | Patterns named | Verdict | Evidence |
|-----------|---------------|---------|----------|
| V-01 | "The signals show..." (noun-lead) + "Across the namespaces..." (prepositional-lead) | **PASS** | Two non-redundant patterns covering different grammatical entry points |
| V-02 | "The signals show..." + "Across the namespaces..." | **PASS** | Same two-pattern minimum set |
| V-03 | "The signals show..." + "Across the namespaces..." with explanations of failure mode | **PASS** | Two non-redundant patterns with failure mode annotation |
| V-04 | "The signals show..." + "Across the namespaces..." | **PASS** | Two non-redundant patterns |
| V-05 | "The signals show..." + "Across the namespaces..." + "What the signals reveal is..." with class label | **PASS** | Three patterns with explicit class name — exceeds the ≥2 threshold; C-45 fires on ≥2, all pass |

#### C-46 — S4c Para 2 Names Inertia Comparator + Cross-References S4b by Identifier

| Variation | Para 2 directive | Verdict | Evidence |
|-----------|-----------------|---------|----------|
| V-01 | "Why the recommendation is preferable to inertia — directly address the strongest inertia-supporting signal identified in S4b" | **PASS** | Names inertia as comparator; S4b identifier present in same directive |
| V-02 | "Why the recommendation is preferable to inertia — directly address the strongest inertia-supporting signal identified in S4b" | **PASS** | Both elements present |
| V-03 | "Why the recommendation is preferable to inertia — directly address the strongest inertia-supporting signal identified in S4b" | **PASS** | Both elements present |
| V-04 | "Why the recommendation is preferable to inertia — directly address the strongest inertia-supporting signal identified in S4b" | **PASS** | Both elements present |
| V-05 | "Why the recommendation is preferable to inertia — directly address the strongest inertia-supporting signal identified in Section 4b" | **PASS** | Both elements present; "Section 4b" = S4b identifier |

#### C-08–C-37, C-39–C-44 — Inherited Baseline

All five variations inherit V-05 R13's structural properties. Each inherited criterion evaluates against the same baseline that yielded 100.0 under v14 for V-05 R13. No inherited criterion degrades: V-02's Inertia? column addition and S4b table-lead do not break C-44 (which fires specifically on S1/S2 table-first, not S4b); V-03's coverage verdict and obtainability fields add structure without contradicting any constraint.

**All C-08–C-37, C-39–C-44**: PASS for all five variations.

---

## Score Computation

| Variation | Essential | Recommended | Aspirational (PASS × 0.2564 + PARTIAL × 0.1282) | Total |
|-----------|-----------|-------------|--------------------------------------------------|-------|
| V-01 | 60.0 | 30.0 | 39 × 0.2564 = **10.00** | **100.00** |
| V-02 | 60.0 | 30.0 | 38 × 0.2564 + 1 × 0.1282 = 9.7432 + 0.1282 = **9.87** | **99.87** |
| V-03 | 60.0 | 30.0 | 38 × 0.2564 + 1 × 0.1282 = **9.87** | **99.87** |
| V-04 | 60.0 | 30.0 | 39 × 0.2564 = **10.00** | **100.00** |
| V-05 | 60.0 | 30.0 | 39 × 0.2564 = **10.00** | **100.00** |

---

## Ranking

| Rank | Variation | Score | C-38 | Novel structural pattern |
|------|-----------|-------|------|--------------------------|
| 1 (tied) | V-01 | 100.00 | PASS | Cell-level three-coordinate entry conditions |
| 1 (tied) | V-04 | 100.00 | PASS | Three-element Para 3: trigger + option + inertia-at-trigger; three-coordinate entry |
| 1 (tied) | V-05 | 100.00 | PASS | Class-labeled hedge prohibition; S4a obtainability field; three-coordinate entry |
| 4 (tied) | V-02 | 99.87 | PARTIAL | S4b inertia signal table; S2 Inertia? flag → S4b evidence chain |
| 4 (tied) | V-03 | 99.87 | PARTIAL | S1 coverage verdict (designed absence vs. signal gap); S4a obtainability |

---

## Excellence Signals

Top-scoring variations: V-01, V-04, V-05 (100.00).

Two structural patterns in the top tier are not captured by any criterion in v14:

**Signal 1 — V-04: Three-element reversal condition with explicit inertia-at-trigger evaluation (Para 3)**

V-04 structures Para 3 as three required elements: (a) the specific trigger signal/event, (b) the option the recommendation changes to, (c) whether the triggered option is preferable to inertia at that trigger point — with the instruction "if the triggered option also cannot beat inertia at that moment, say so." V-01, V-02, V-03, V-05 all include "whether that option is preferable to inertia at that trigger point" language, but V-04 makes the three elements explicit structural requirements with the additional mandate to report negative comparisons. C-46 fires only on Para 2 (the recommendation naming inertia + S4b cross-reference for the *current* state). No criterion fires on Para 3's requirement to evaluate inertia at the *triggered future state*. Governance consequence: a Para 3 that does not pre-evaluate inertia at the trigger leaves the inertia comparison forward-open — the decision tree is inertia-complete for the present state but not for the triggered state. A three-element Para 3 closes the comparison for both, creating a fully inertia-complete decision tree without leaving open branches.

**Signal 2 — V-05: Verbatim hedge prohibition names the prohibited class and makes it self-extending**

V-05 names three verbatim patterns and explicitly labels the class they constitute: "aggregate-first hedging cluster." The prohibition then states: "New instances of this class are prohibited even if not explicitly named above." C-45 fires on whether ≥2 non-redundant patterns are named; no criterion fires on whether the prohibition names the class itself. Governance consequence: a class-labeled prohibition changes compliance from surface avoidance ("avoid these two strings") to category understanding ("avoid any opening that positions the author as reporting rather than asserting"). An author satisfying a named-set prohibition can satisfy the letter while paraphrasing into an unlisted cousin with a different lead token; an author complying with a class-labeled prohibition cannot, because the class definition — not the enumerated list — is the constraint. The prohibition also becomes self-extending without structural change: new instances append to a named category, not to a numbered list.

---

## Notes on Non-Top-Tier Novel Patterns

V-02 and V-03 score at 99.87 due to row-level (not cell-level) C-38. Their novel patterns (V-02: S4b inertia signal table extending table-first discipline into analysis sections; V-03: S1 coverage verdict distinguishing designed absences from signal gaps) are not captured by existing criteria but are not carried by the top-scoring variations. These patterns are excellence signal candidates for future rounds if a top-scoring variation also includes them.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Three-element reversal condition: S4c Para 3 requires (a) trigger signal/event, (b) option it changes to, (c) whether triggered option is preferable to inertia at that trigger point — closes inertia comparison for the triggered future state, not only the current recommendation. C-46 fires on Para 2 only; no criterion fires on Para 3 inertia-at-trigger evaluation.", "Class-labeled hedge prohibition: names the prohibited class ('aggregate-first hedging cluster') and declares it self-extending — new instances of the class are prohibited even if not explicitly enumerated. C-45 fires on ≥2 named verbatim patterns; no criterion fires on whether the class is named and made extensible beyond the enumerated set."]}
```
