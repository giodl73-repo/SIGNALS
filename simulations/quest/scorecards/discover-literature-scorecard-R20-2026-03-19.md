## discover-literature Scorecard — Round 20

**Rubric**: v19 (235-pt ceiling) | **Variations**: 5 (V-01 through V-05)

---

### Scoring Summary

| V | Description | Predicted | Actual | Delta |
|---|---|---|---|---|
| V-01 | Phrasing Register: conversational | 235 | **235** | 0 |
| V-02 | Lifecycle Emphasis: C-29 block omitted | 195 | **195** | 0 |
| V-03 | Inertia Framing: Phase-0, C-27(a) broken | 180 | **180** | 0 |
| V-04 | Combined: conversational + single-obligation preamble | 230 | **215** | **-15** |
| V-05 | Full synthesis: conversational + expanded inertia | 235 | **235** | 0 |

---

### V-01 — Phrasing Register: Conversational (235/235)

All essential, recommended, and aspirational criteria pass. The only change from the canonical form is prose register — all structural tokens, schemas, lifecycle annotations, C-29 block, and C-33 Compliance Declaration are structurally identical to V-05 R19.

**Critical checks:**

| Criterion | Result | Evidence |
|---|---|---|
| C-01 through C-05 | PASS | All phase structures intact |
| C-06 through C-08 | PASS | Contrary-to-claim mapping, search evidence, HIGH RISK format |
| C-15 | PASS | Both OBLIGATION A and B in preamble, non-optional |
| C-27 | PASS | `inertia_committed=[yes]` in PHASE 1 COMPLETE |
| C-30 | PASS | `## C-29 Operationalization Verification` block present |
| C-34 | PASS | `#### C-33 Compliance Declaration` labeled sub-section |
| C-36 | PASS | Analogy statement `C-34 is to C-33 what C-25 is to C-23` within sub-section boundary |
| C-37 | PASS | Chain reads `C-14 + C-23 -> C-27 -> C-28 -> C-29 -> C-30 -> C-31 -> C-32 -> C-33 -> C-34 -> C-35 -> C-36 complete` |

**Score: 235/235** — perfect ceiling, confirming register orthogonality.

---

### V-02 — Lifecycle Emphasis: C-29 Block Omitted (195/235)

C-28/C-29 per-boundary annotations in the lifecycle tokens are preserved. The `## C-29 Operationalization Verification` block is intentionally absent. The NOTE in Phase 4 explicitly flags this as the axis under test.

**Failure chain:**

| Criterion | Result | Reason |
|---|---|---|
| C-29 | PASS | Distributed in-token annotations at Phase 1 and Phase 4 boundaries satisfy all three elements per boundary |
| C-30 | **FAIL** | No named consolidation block present — "C-29 is satisfied by the per-boundary annotations above" is insufficient; C-30 requires the named block |
| C-31 | **FAIL** | Dependency: C-30 FAIL |
| C-32 | **FAIL** | Dependency chain |
| C-33 | **FAIL** | Dependency chain |
| C-34 | **FAIL** | Dependency chain |
| C-35 | **FAIL** | Dependency chain |
| C-36 | **FAIL** | Dependency chain |
| C-37 | **FAIL** | Dependency chain |

**Lost: C-30 through C-37 = 8 × 5 = 40 pts**

**Score: 195/235** — matches prediction. Demonstrates that distributed C-29 annotations satisfy C-29 but the named consolidation block (C-30) is an independently required structural element.

---

### V-03 — Inertia Framing: Phase-0 Architecture (180/235)

Inertia commitment is moved to a `## PRE-PHASE INERTIA FRAME` section before Phase 1. Phase 1 is redesigned without the INERTIA COMMITMENT block. `PHASE 1 COMPLETE:` token reads `claims=[n] | evidence_type_mapped=[yes/no] | counter-evidence-noted=[yes/no]` — no `inertia_committed` field.

**Failure chain:**

| Criterion | Result | Reason |
|---|---|---|
| C-14 | PASS | Inertia named pre-search (PRE-PHASE frame) and verified in Phase 4 with INERTIA RISK: — C-14's gap-analysis requirement met |
| C-27 | **FAIL** | C-27(a) requires `inertia_committed=[yes]` at the PHASE 1 COMPLETE: boundary. Field is absent. Inertia commitment in a pre-phase section does not satisfy the lifecycle-integration requirement |
| C-28 | **FAIL** | Requires C-27 PASS |
| C-29 | **FAIL** | C-29 block is present but cells (i)-(iii) are explicitly NOT CONFIRMED — "C-27(a) not established at PHASE 1 COMPLETE: boundary; inertia_committed field absent." Block cannot declare C-29 PASS |
| C-30 | **FAIL** | C-29 FAIL; block cannot consolidate a non-passing C-29 |
| C-31 through C-37 | **FAIL** | Dependency chain |

**Lost: C-27 through C-37 = 11 × 5 = 55 pts**

**Score: 180/235** — matches prediction. Confirms that architectural rearrangement of semantically correct inertia content fails when it breaks the lifecycle-token-layer integration point.

---

### V-04 — Combined: Conversational + Single-Obligation Preamble (215/235 — DEVIATION from predicted 230)

The ENFORCEMENT CONTRACT preamble covers only OBLIGATION A (anti-placeholder recovery) with full typed schema. OBLIGATION B (empty-tier acknowledgment) is absent from the global preamble. The NOTE explicitly identifies this as C-15 PARTIAL. TIER EMPTY: schema appears in Phase 3 where it is used, but is not part of the global enforcement contract.

**Failure chain:**

| Criterion | Result | Reason |
|---|---|---|
| C-15 | **PARTIAL** (0 pts) | "A preamble covering only one of the two obligations is a PARTIAL, not a PASS." OBLIGATION B absent from preamble |
| C-17 | **FAIL** | Pass condition: "If C-15 is FAIL or PARTIAL, this criterion cannot PASS." — hard gate, no exception for partial presence of OBLIGATION A's typed schema |
| C-19 | **FAIL** | Pass condition: "If C-17 is FAIL or PARTIAL, this criterion cannot PASS." |
| C-21 | **FAIL** | Pass condition: "If C-19 is FAIL, this criterion cannot PASS." |
| C-27 through C-37 | **PASS** | `inertia_committed=[yes]` present in PHASE 1 COMPLETE; C-29 block fully present with all six cells confirmed; chain extended to C-36 |
| All others | **PASS** | C-18, C-20, C-22–C-26, C-28–C-37 all intact |

**Lost: C-15 + C-17 + C-19 + C-21 = 4 × 5 = 20 pts**

**Score: 215/235 — 15 pts below predicted 230.**

**Why the deviation:** The prediction accounted for C-15 PARTIAL (-5) but did not trace the mandatory cascade. The rubric explicitly names "FAIL or PARTIAL" as the C-17 gate condition — not just "FAIL." Since OBLIGATION A's typed schema satisfies C-17's main structural requirement, the prediction assumed C-17 would hold, but the explicit dependency clause overrides this: a partial C-15 gates C-17, which gates C-19, which gates C-21, for a total of 20 pts lost.

---

### V-05 — Full Synthesis: Conversational + Expanded Inertia + All Tokens (235/235)

All structural tokens preserved. Inertia framing expanded with two-question concrete format in Phase 1 and explicit "moment of measurement" language in Phase 4. All criteria pass identically to V-01.

**Critical checks (same as V-01, confirm independently):**

| Criterion | Result | Evidence |
|---|---|---|
| C-15 | PASS | Both OBLIGATION A and B with full typed schemas |
| C-27 | PASS | `inertia_committed=[yes]` in PHASE 1 COMPLETE |
| C-36 | PASS | `C-34 is to C-33 what C-25 is to C-23` within C-34 labeled sub-section |
| C-37 | PASS | `C-14 + C-23 -> ... -> C-34 -> C-35 -> C-36 complete` |

**Score: 235/235** — full ceiling confirmed with expanded inertia prose and conversational register.

---

### Ranking

| Rank | V | Score | Key factor |
|---|---|---|---|
| 1 (tie) | V-01 | 235/235 | Conversational register, all tokens preserved |
| 1 (tie) | V-05 | 235/235 | Full synthesis, expanded inertia framing |
| 3 | V-04 | 215/235 | C-15 PARTIAL cascades to C-17, C-19, C-21 |
| 4 | V-02 | 195/235 | C-30 absent cascades C-30 through C-37 |
| 5 | V-03 | 180/235 | C-27(a) broken cascades C-27 through C-37 |

---

### Excellence Signals from Top-Scoring Variations (V-01, V-05)

**1. Register orthogonality (V-01 — new in R20)**
Conversational prose achieves 235/235 identically to formal prose. Every criterion from C-01 through C-37 is structure-sensitive, not style-sensitive. This is the first explicit confirmation in the quest loop. Implication: the rubric could accommodate a C-38 register criterion without modifying any existing criterion.

**2. Two-question inertia commitment format (V-05)**
Phase 1 INERTIA COMMITMENT expands from a single answer to two explicit questions: "What does a team actually do if they never run this literature review? What does that cost them — concretely?" This forces the pre-search commitment to name both the default behavior and its concrete cost, making Phase 4 measurement more tractable.

**3. Measurement-framed Phase 4 inertia verification (V-05)**
The inertia verification opens: "This is the moment of measurement: does the literature gathered actually make the inertia default worse than acting? Be direct. Name the specific harm the inertia path creates." The PROCEED gate explicitly requires showing the evidence is "strong enough to move a skeptical team." This operationalizes C-14's "overcome inertia" requirement in prose.

**4. Cascade sensitivity of C-15 PARTIAL (V-04 — diagnostic)**
V-04 surfaces a non-obvious rubric property: C-15 PARTIAL (single-obligation preamble) does not merely lose 5 pts — it cascades through C-17 → C-19 → C-21, losing 20 pts total. Any skill prompt that defines only one obligation in the preamble should be treated as a C-15 PARTIAL and expected to score 215, not 230.

---

```json
{"top_score": 235, "all_essential_pass": true, "new_patterns": ["Register orthogonality confirmed: conversational prose achieves 235/235 identically to formal prose -- style is fully orthogonal to structural compliance across all 29 aspirational criteria", "C-15 PARTIAL cascades to C-17 FAIL, C-19 FAIL, C-21 FAIL via explicit rubric gates -- single-obligation preamble loses 20 pts not 5; any prompt missing one preamble obligation should score 215 not 230"]}
```
