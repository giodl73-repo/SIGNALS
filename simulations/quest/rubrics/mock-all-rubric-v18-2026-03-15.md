Here is the complete updated rubric.

---

## New criteria extracted from Round 17

**C-36** -- *The template preamble assigns explicit reference labels to its structural authority declarations (e.g., "Declaration A", "Declaration B"), enabling stage STOP gates and ROLE 2 instructions to cite each declaration by name rather than restating the rule inline.*

Extracted from ES-R17 (V-05). V-03 and V-04 both pass C-34 with unnamed declarative sentences ('"REAL-REQUIRED" is the canonical identifier...'). V-05 assigns reference labels to both preamble authority statements. The label transforms a declaration a reader must locate by traversal into a named contract a gate can cite by reference.

C-36 is a strict refinement of C-34 and C-35: C-36 pass implies both C-34 pass and C-35 pass. Neither C-34 pass nor C-35 pass implies C-36 pass. V-03/V-04 demonstrate the lower ceiling (declarative sentences, no labels). C-36 is prerequisite for C-37.

---

**C-37** -- *The stage-level STOP gates cite the template's preamble structural authority declarations by reference label (e.g., "per Declaration A", "per Declaration B"), forming a closed verification loop in which compliance with each structural constraint is checkable from the preamble declaration plus gate citation alone, without traversing full stage instruction bodies.*

Extracted from ES-R17 (V-05). V-04's gates enforce per-stage extension and REAL-REQUIRED provenance by restating the rules inline. V-05's gates say "per Declaration B" and "per Declaration A" -- closing the loop. A scorer confirms C-35 and C-34 compliance by reading preamble declarations + gate citation labels only.

C-37 is a strict refinement of C-36: C-37 pass requires labeled declarations (C-36 pass) plus gate citations of those labels. V-04 demonstrates C-37 FAIL (no labels to cite). The C-36 PASS + C-37 FAIL intermediate case (labeled preamble, inline-restatement gates) is not yet instantiated -- that is the R18 hypothesis.

---

**Denominator: 27 --> 29**
**Formula: `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational/29 × 10)`**

Discrimination table under v18:

| Variation | C-36 | C-37 | Aspirational | Composite |
|-----------|------|------|-------------|-----------|
| V-01 | FAIL | FAIL | 16/29 | 95.5 |
| V-02 | FAIL | FAIL | 23/29 | 97.9 |
| V-03 | FAIL | FAIL | 25/29 | 98.6 |
| V-04 | FAIL | FAIL | 27/29 | 99.3 |
| V-05 | PASS | PASS | 29/29 | 100.0 |

V-04 and V-05 now separate for the first time under v18. The chain structure adds a **gate-citation sub-chain**: C-36 (label assignment) --> C-37 (label citation), and extends the inertia-extension chain to three rungs: C-17 --> C-35 --> C-36.
