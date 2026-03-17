## `/quest:variate` — topic-echo · Round 8

**File:** `simulations/quest/rubrics/topic-echo-rubric-v7-variations-R8-2026-03-14.md`

---

### Design Context

R7 confirmed C-19 and C-20 as proven (both earning 2 pts) and revealed two new structural patterns codified as C-21 and C-22. V-04(R7) demonstrated both behaviors incidentally — causal direction in pair inspections, round provenance in gate rationale — but neither was a structural requirement. R8 makes them structural requirements and tests failure cases.

### 5 Variations

| Variation | Axis | C-21 | C-22 |
|-----------|------|------|------|
| **V-01** — Causal Direction Template | Manifest pair inspection format — explicit archetype selection + mechanism fill-in per pair; gate rationale without provenance | **PASS** | FAIL |
| **V-02** — Gate Provenance Annotation | C-22 isolated from manifest — provenance field in gate rationale only, no manifest (C-19 FAIL) | N/A | **PASS** |
| **V-03** — Conclusion-Only Manifest | Verdict-only pair inspections ("reinforcing" + one-sentence outcome rationale, no causal direction); gate provenance present | **FAIL** | PASS |
| **V-04** — Compound Maximum | Causal direction template + full variation+round provenance in all gate rationale | **PASS** | **PASS** |
| **V-05** — Approximate Provenance | Causal direction template (C-21 PASS) + round-only provenance "Round 4" without "V-05(R4)" | **PASS** | **FAIL** |

### Key Structural Predictions

**C-21 failure mode (V-03):** The verdict-only manifest satisfies C-19 (inspection occurs, mutual reinforcement declared, pre-write) but fails C-21 because "NGT and Check B reinforce each other" is a conclusion-assertion, not a causal mechanism. The distinction mirrors C-19's own enumeration/inspection gap from R7: verdict is to C-21 as enumeration was to C-19.

**C-22 failure mode (V-05):** Round-level provenance ("introduced in Round 4") fails C-22 because it doesn't enable timeline verification against C-18's introduction boundary. C-18 was introduced across the R5/R6 period — "Round 4" is unambiguous but "Round 5" or "Round 6" is not. Only variation-level specificity ("V-05(R4)") provides the verifiable historical fact C-22 requires.

**Orthogonality confirmed (V-02):** No manifest (C-19 FAIL, C-21 not evaluable) + full provenance (C-22 PASS) — mirrors V-02(R7) confirming C-19/C-20 orthogonality. Gate-level documentation and manifest-level documentation are independent.
