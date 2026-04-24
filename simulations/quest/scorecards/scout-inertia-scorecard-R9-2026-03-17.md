# scout-inertia R9 — Quest Score Evaluation

## Scoring Framework

- **Essential** (C-01–C-05): 12 pts each / 60 pts total — structural pass/fail gate
- **Recommended** (C-06–C-08): 10 pts each / 30 pts total
- **Aspirational**: `aspirational_pass / 21 * 10` pts (denominator raised from 18 → 21 with C-27/C-28/C-29)
- **Total**: 100 pts

---

## Per-Variation Scoring

### V-01 — Constraint-Before-Site Placement (targets C-27)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Workaround mapped | PASS | Section 2 prohibits "a manual process", requires specific artifact name + named role + unit cost |
| C-02 Switching costs quantified | PASS | MANIFEST-03 requires explicit units; Section 3 table has Unit column; "significant without a number fails" implied by manifest |
| C-03 Threat score HIGH | PASS | Section 4 explicit declaration with deviation-justification requirement |
| C-04 Why inertia loses | PASS | Section 5 defeat conditions table + Section 6 synthesis requiring FM/DC cross-references |
| C-05 Failure modes identified | PASS | Section 1 FM inventory with Actor/Trigger columns, minimum 2 rows enforced |
| C-06 Dimensions separate | PASS | Section 3 has four distinct labeled rows (migration / training / disruption / in-flight) |
| C-07 Forward-looking risk | PARTIAL | Not explicitly mandated; Section 6 synthesis may surface it but scaffold doesn't require it |
| C-08 Adoption trigger conditions | PARTIAL | Section 5 defeat conditions can serve as triggers but no explicit "trigger" framing required |
| **C-27 Constraint-before-site** | **PASS** | MANIFEST-01–04 block appears before Section 1; each manifest entry labels its governed section(s) |
| **C-28 Criterion-ID-labeled scan** | **PASS** | Completeness checklist uses explicit IDs: "C-01:", "C-02:", "MANIFEST-01:", "MANIFEST-02:" |
| **C-29 Manifest-bound verbatim directive** | **FAIL** | Manifest contains structural enforcement rules (units, falsifiability) but no verbatim-alignment directive co-located inside the manifest block adjacent to canonical strings |

**Aspirational estimate**: C-27 + C-28 pass (2 new) + ~15/18 prior criteria = 17/21 → **8.1 pts**

**V-01 Total: 60 + 20 + 8.1 = 88.1**

---

### V-02 — Criterion-ID-Labeled Verification Scan (targets C-28)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Workaround mapped | PASS | Section 2 prohibits "a manual process"; requires named tool/format/procedure |
| C-02 Switching costs quantified | PASS | Section 3: "Significant without a number fails" |
| C-03 Threat score HIGH | PASS | Section 4 explicit declaration with deviation justification |
| C-04 Why inertia loses | PASS | Section 5 defeat conditions + Section 6 synthesis |
| C-05 Failure modes identified | PASS | Section 1 FM inventory with Actor/Trigger columns |
| C-06 Dimensions separate | PASS | Section 3 four-row table |
| C-07 Forward-looking risk | PARTIAL | Not mandated |
| C-08 Adoption trigger conditions | PARTIAL | Not mandated |
| **C-27 Constraint-before-site** | **FAIL** | PRIMARY KEY CONSTRAINT is inline in Section 1 — co-located with the governed table, not placed in a pre-section manifest block. No document-level preamble manifest exists. |
| **C-28 Criterion-ID-labeled scan** | **PASS** | `[C-05-INT]` label at Section 5 citation-point check; variation description confirms criterion-ID bracket notation throughout |
| **C-29 Manifest-bound verbatim directive** | **FAIL** | No manifest block; verbatim-alignment not addressed |

**Aspirational estimate**: C-28 pass (1 new) + ~14/18 prior = 15/21 → **7.1 pts**

**V-02 Total: 60 + 20 + 7.1 = 87.1**

---

### V-03 — Manifest-Bound Verbatim Directives (targets C-29)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Workaround mapped | PASS | Section directive inside Section 2 prohibits generic language |
| C-02 Switching costs quantified | PASS | Section 3 directive co-located with cost table |
| C-03 Threat score HIGH | PASS | Section 4 declaration |
| C-04 Why inertia loses | PASS | Section 5 + Section 6 |
| C-05 Failure modes identified | PASS | Section 1 FM inventory with verbatim identifier reproduction directive adjacent to FM-[N] strings |
| C-06 Dimensions separate | PASS | Section 3 structure |
| C-07 Forward-looking risk | PARTIAL | Not mandated |
| C-08 Adoption trigger conditions | PARTIAL | Not mandated |
| **C-27 Constraint-before-site** | **FAIL** | Directives are co-located INSIDE their governed sections, not extracted to a pre-document manifest preamble. C-27 explicitly excludes "co-located with the final section" — V-03's pattern is precisely what C-27 disallows for structural constraints. (Note: co-location is correct for verbatim directives per C-29, but structural constraints per C-27 must precede governed sections.) |
| **C-28 Criterion-ID-labeled scan** | **FAIL** | No criterion-ID labeling mentioned in trailing verification or section checks |
| **C-29 Manifest-bound verbatim directive** | **PASS** | FM Inventory table contains verbatim identifier reproduction directive adjacent to canonical FM-[N] strings — model reads directive and reference strings in a single pass |

**Aspirational estimate**: C-29 pass (1 new) + ~14/18 prior = 15/21 → **7.1 pts**

**V-03 Total: 60 + 20 + 7.1 = 87.1**

---

### V-04 — C-27 + C-28 Combination

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Workaround mapped | PASS | Combined scaffold inherits Section 2 enforcement |
| C-02 Switching costs quantified | PASS | MANIFEST unit rule + ID-labeled verification scan |
| C-03 Threat score HIGH | PASS | Section 4 declaration |
| C-04 Why inertia loses | PASS | ID-labeled Section 5 + Section 6 |
| C-05 Failure modes identified | PASS | Section 1 FM inventory; three labeled enforcement opportunities |
| C-06 Dimensions separate | PASS | Section 3 table |
| C-07 Forward-looking risk | PARTIAL | Not mandated by V-04's scope |
| C-08 Adoption trigger conditions | PARTIAL | Not mandated |
| **C-27 Constraint-before-site** | **PASS** | CONSTRAINT MANIFEST with labeled IDs explicitly placed before governed sections |
| **C-28 Criterion-ID-labeled scan** | **PASS** | Criterion-ID bracket notation throughout; ID-labeled citation-point check at Section 5; ID-labeled trailing scan |
| **C-29 Manifest-bound verbatim directive** | **FAIL** | V-04 description does not include C-29; no verbatim co-location directive inside manifest |

**Aspirational estimate**: C-27 + C-28 (2 new) + ~16/18 prior (manifest improves several base criteria) = 18/21 → **8.6 pts**

**V-04 Total: 60 + 20 + 8.6 = 88.6**

---

### V-05 — Full Integration (C-27 + C-28 + C-29 + A-10 + A-12 + A-17–A-20)

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Workaround mapped | PASS | Fail-first declaration + all five criterion questions mandate Section 2 workaround specificity |
| C-02 Switching costs quantified | PASS | MANIFEST unit enforcement + criterion-ID-labeled scan + binary checklist |
| C-03 Threat score HIGH | PASS | Explicit declaration; criterion-chain reference audits it |
| C-04 Why inertia loses | PASS | Defeat conditions with `(closes C-05 -> C-04)` criterion-chain reference; bidirectional integrity |
| C-05 Failure modes identified | PASS | FM inventory with fail-first declaration; `(closes C-05 -> R-02)` chain reference surfaces forward risk |
| C-06 Dimensions separate | PASS | Binary checklist + full Section 3 table; inline column examples reduce misinterpretation |
| C-07 Forward-looking risk | **PASS** | Q3 named bridge artifact explicitly surfaces forward-looking risk; `(closes C-05 -> R-02)` creates a mechanical obligation to produce a compounding-risk artifact |
| C-08 Adoption trigger conditions | **PASS** | Q4 named bridge artifact explicitly surfaces trigger conditions; `(closes C-05 -> C-04)` connects failure mode escalation to defeat condition triggers |
| **C-27 Constraint-before-site** | **PASS** | Constraint manifest precedes governed sections; all structural rules placed before first governed site |
| **C-28 Criterion-ID-labeled scan** | **PASS** | Criterion-ID labeling at both enforcement points; version-stable ID trail throughout |
| **C-29 Manifest-bound verbatim directive** | **PASS** | Verbatim directives co-located inside manifest/table blocks adjacent to reference strings |

**C-07 and C-08 upgrade to PASS** is the critical V-05 differentiator: Q3/Q4 bridge artifacts turn recommended criteria from optional outputs into required structural deliverables with named IDs.

**Aspirational estimate**: 21/21 — full integration explicitly passes all three new criteria plus 6 named prior criteria (A-10/A-12/A-17–A-20); baseline scaffold covers remaining 12 → **10.0 pts**

**V-05 Total: 60 + 30 + 10.0 = 100**

---

## Score Summary

| Variation | Essential | Recommended | Aspirational | **Total** |
|-----------|-----------|-------------|--------------|-----------|
| V-01 | 60 | 20 | 8.1 | **88.1** |
| V-02 | 60 | 20 | 7.1 | **87.1** |
| V-03 | 60 | 20 | 7.1 | **87.1** |
| V-04 | 60 | 20 | 8.6 | **88.6** |
| **V-05** | **60** | **30** | **10.0** | **100** |

**Ranking**: V-05 > V-04 > V-01 > V-02 = V-03

---

## Excellence Signals from V-05

**1. Named bridge artifacts promote recommended criteria to required deliverables**
V-01 through V-04 treat C-07 and C-08 as "may emerge from synthesis" — the scaffold doesn't mandate them. V-05's Q3/Q4 bridge artifact naming creates structural slots for forward-looking risk (Q3) and trigger conditions (Q4). The `(closes C-05 -> R-02)` notation makes satisfying the recommended criteria a closure event with an identifiable artifact, not a stylistic choice.

**2. Criterion-chain closure converts cross-criterion dependencies into traceable arcs**
The `(closes C-05 -> R-02)` and `(closes C-05 -> C-04)` annotations are new infrastructure. They force the scaffold author to ask "which criterion does this site support downstream?" and give the reviewer a directed graph rather than an unstructured checklist. A failing item fails at a named arc, not at an unnamed property.

**3. Fail-first declaration combined with all five criterion questions**
Prior variations open with structural rules. V-05 opens with a fail-first declaration that makes the output semantically invalid until all five essential criterion questions are answered. This changes the model's operating mode from "fill in sections" to "answer five questions, then structure the answers" — which reduces section-skipping while answering another question.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Named bridge artifacts (Q3/Q4) promote recommended criteria C-07 and C-08 from optional synthesis outputs to required deliverables with structural slots and artifact IDs", "Criterion-chain closure notation (closes C-05 -> R-02) converts cross-criterion dependencies into traceable directed arcs, making downstream failures identifiable by criterion ID without content review", "Fail-first declaration combined with all-five-criterion-questions framing shifts model operating mode from section-filling to question-answering, reducing criterion-skipping under section-completion pressure"]}
```
