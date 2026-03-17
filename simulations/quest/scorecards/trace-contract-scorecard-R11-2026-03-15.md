# trace-contract — Round 11 Scorecard

## Rubric Criteria (v11)

| ID | Description | Points |
|----|-------------|--------|
| C-26 | Gate-closure confirmation token (clauses-resolved echo) | 10 |
| C-27 | Branch-conditional Patterns template slots (pre-printed structural fields per branch) | 10 |
| C-28 | Mechanism taxonomy constraint (vocabulary-constrained per-finding type tokens) | 15 |
| C-29 | `mechanism-type-shared:` in Singleton + Multi-pattern branch templates | 15 |
| C-30 | `mechanism-distribution:` aggregate in Summary | 15 |
| C-31 | S5.5 mandatory interstitial Taxonomy Census step (single ordered walk, both aggregates) | 25 |
| C-32 | `group-candidate-N:` staging format in Sub-task B (before any branch template fill) | 20 |
| **Total** | | **110** |

---

## V-01 — Role Sequence

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-26 | PASS (10/10) | Baseline gate-closure established in prior rounds; role change does not break it |
| C-27 | PASS (10/10) | Baseline branch template slots intact; expert resumption is additive |
| C-28 | PARTIAL (8/15) | Taxonomy tokens must exist for Expert to verify/reclassify — but structural enforcement is not added; token presence depends on upstream compliance |
| C-29 | PASS (15/15) | Expert owns the synthesis layer; `mechanism-type-shared:` determination is a named "contract-level determination" within S5.5 Sub-task B |
| C-30 | PASS (15/15) | Expert owns census pass; `mechanism-distribution:` flows from expert verification, not a re-derivation pass |
| C-31 | PASS (22/25) | Expert explicitly resumes at S5.5 with both sub-tasks framed; `census-author:` token provides auditability. Slight deduction: the structural step itself isn't newly enforced — relies on role ownership |
| C-32 | PARTIAL (12/20) | Expert owns Sub-task B "contract-level determination," improving grouping quality. But the staged `group-candidate-N:` format lines are not structurally required — ownership improves accuracy without enforcing the staging schema |

**V-01 Total: 92/110**

---

## V-02 — Output Format

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-26 | PASS (10/10) | Baseline; tabular findings do not affect gate-closure token structure |
| C-27 | PARTIAL (7/10) | Tabular format restructures findings; branch template slots are not part of the findings table. Possible mismatch between tabular finding representation and prose-structured Patterns branches |
| C-28 | PASS (15/15) | Mechanism-Type as a dedicated column is structural enforcement — blank = visible gap; cell constraint is stronger than inline prose tag |
| C-29 | PARTIAL (8/15) | Column isolation reduces token drift feeding into branch templates, but `mechanism-type-shared:` in branch templates is not explicitly updated by V-02's column format |
| C-30 | PARTIAL (8/15) | Column tally in Sub-task A produces the data for `mechanism-distribution:` but the Summary field is not explicitly required by V-02 spec |
| C-31 | PASS (22/25) | Sub-task A becomes a mechanical column scan — straightforward tally with no prose-block parsing errors. Slight deduction: Sub-task B grouping is not enhanced by tabular format |
| C-32 | PARTIAL (10/20) | Column structure aids grouping inference but does not produce explicit `group-candidate-N:` staging lines; the branch template remains populated without a pre-template staging audit |

**V-02 Total: 80/110**

---

## V-03 — Lifecycle Emphasis

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-26 | PASS (10/10) | Baseline; STOP gate at S5.5 is distinct from gate-closure token at S5 boundary |
| C-27 | PASS (10/10) | Branch template slots baseline; STOP gate does not modify branch structure |
| C-28 | PARTIAL (7/15) | Not targeted; taxonomy token compliance depends on prior spec compliance, not on the STOP gate |
| C-29 | PARTIAL (7/15) | Not targeted; `mechanism-type-shared:` in branch templates is not addressed by lifecycle emphasis |
| C-30 | PARTIAL (7/15) | Not targeted; `mechanism-distribution:` in Summary not addressed |
| C-31 | PASS (25/25) | Hard STOP with BLOCKED signal converts C-31 from advisory to enforced. Zero-finding skip path explicitly patched ("zero findings → one-line outputs — still required"). Gate-lift as next visible action is strong emission enforcement |
| C-32 | PARTIAL (10/20) | Gate enforces that both Sub-task A and B are emitted; but the staging format `group-candidate-N:` is not structurally required — compliant format-fill without genuine grouping is still possible past the gate |

**V-03 Total: 76/110**

---

## V-04 — Role Sequence + Lifecycle Emphasis

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-26 | PASS (10/10) | Baseline |
| C-27 | PASS (10/10) | Baseline |
| C-28 | PARTIAL (8/15) | Expert reclassification at S5.5 improves taxonomy accuracy but structural enforcement not added |
| C-29 | PASS (15/15) | Expert owns synthesis layer — `mechanism-type-shared:` is a contract-level determination |
| C-30 | PASS (15/15) | Expert census pass + gate enforces emission → `mechanism-distribution:` aggregate is covered by expert ownership and STOP enforcement |
| C-31 | PASS (25/25) | Dual mechanism: expert ownership addresses quality failure mode; STOP gate addresses emission failure mode. The hypothesis correctly identifies these as orthogonal — combined they close both |
| C-32 | PARTIAL (13/20) | Expert owns Sub-task B + gate ensures it is emitted. But the `group-candidate-N:` staging schema is not structurally required; format-compliant fill-in remains possible; the determination is auditable by author but not by schema |

**V-04 Total: 96/110**

---

## V-05 — Output Format + Phrasing Register (Rationale Staging)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-26 | PASS (10/10) | Baseline; tabular findings + rationale staging are additive |
| C-27 | PASS (10/10) | Baseline branch template slots; branch templates copy from staged `group-candidate-N:` lines — structural flow is cleaner, not broken |
| C-28 | PASS (15/15) | Tabular column enforces taxonomy structurally; blank cell = visible enforcement gap |
| C-29 | PASS (15/15) | Staging lines explicitly produce `mechanism-type-shared:` entries; branch templates copy from staging rather than re-deriving — C-29 propagation path is made explicit and copyable |
| C-30 | PARTIAL (10/15) | Sub-task A column tally produces the data needed for `mechanism-distribution:` in Summary. However, V-05 does not explicitly require the Summary field — Summary copying from Sub-task A is implied but not enforced by the variation spec |
| C-31 | PASS (25/25) | Tabular column makes Sub-task A purely mechanical (column scan → tally). Rationale clause makes Sub-task B deliberate. The cognitive mode split is the strongest S5.5 specification: each sub-task has a matching register |
| C-32 | PASS (20/20) | `rationale:` clause in each `group-candidate-N:` line directly addresses the fill-in weakness — a format-compliant staging line without genuine grouping analysis cannot produce a non-trivial `rationale:` value. Mixed declarations and false single-type groupings become visibly distinguishable from genuine determinations |

**V-05 Total: 105/110**

---

## Ranking

| Rank | Variation | Score | Gap Criterion |
|------|-----------|-------|---------------|
| 1 | V-05 Tabular + Rationale | 105/110 | C-30 partial (Summary distribution not explicitly required) |
| 2 | V-04 Expert + STOP | 96/110 | C-28 partial; C-32 partial (staging schema not enforced) |
| 3 | V-01 Role Sequence | 92/110 | C-28 partial; C-32 partial (ownership without staging format) |
| 4 | V-02 Output Format | 80/110 | C-29, C-30 partial; C-32 partial |
| 5 | V-03 Lifecycle Emphasis | 76/110 | C-28–C-30, C-32 partial |

---

## Excellence Signals (V-05)

**Signal 1 — Rationale clause as anti-fill-in constraint**
The `rationale:` field in `group-candidate-N:` staging lines eliminates the failure mode where a model writes format-compliant staging entries without performing genuine grouping analysis. A nontrivial rationale requires the model to have actually resolved the mechanism-alignment question before committing to the staging line. This is a stronger guard than a schema requirement alone — the schema enforces presence, the rationale enforces *content*.

**Signal 2 — Cognitive mode split in S5.5**
Sub-task A (column tally = mechanical) and Sub-task B (rationale staging = deliberate) match distinct cognitive registers to distinct task natures. The tabular column reduces Sub-task A to a scan with no prose-parsing errors; the rationale register elevates Sub-task B from fill-in to decision documentation. Separating mechanical counting from judgment-bearing determination within a single census step is the design pattern that most completely satisfies C-31 and C-32 simultaneously.

**Remaining gap — C-30 enforcement path**
V-05 produces the data for `mechanism-distribution:` (Sub-task A column tally) but does not explicitly require the Summary field. The next escalation should close this: require S5.5 Sub-task A to emit the `mechanism-distribution:` formatted line directly, and require Summary to copy it verbatim — mirroring the Sub-task B → branch template copy pattern already established.

---

```json
{"top_score": 105, "all_essential_pass": false, "new_patterns": ["rationale clause in Sub-task B staging lines forces genuine grouping decisions and makes spurious mixed declarations visibly distinguishable from real determinations", "cognitive mode split in S5.5: Sub-task A as mechanical column tally, Sub-task B as deliberate rationale-bearing decision documentation — matching cognitive register to task nature within a single census step"]}
```
