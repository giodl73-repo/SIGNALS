Scorecard written to `simulations/quest/scorecards/validate-inertia-scorecard-R5-2026-03-17.md`.

---

## Results

**Top score: 99.29** (V-02 and V-05, tied)  
**All essential pass: YES**

### Final scores

| Rank | V | Strategy | Score |
|------|---|----------|-------|
| 1T | V-02 | Scan-forward-ref (C-21) | **99.29** |
| 1T | V-05 | Scan-table hybrid (C-21+C-22) | **99.29** |
| 3T | V-01 | Three-layer distributed (C-20) | 98.57 |
| 3T | V-03 | Gate-2-canonical (C-22) | 98.57 |
| 3T | V-04 | Gate-2-equivalent + distributed (C-20+C-22) | 98.57 |

### Key finding: V-03 prediction error

The variations file predicted V-03 at 13/14 → 99.29, but the same file's coverage table already showed C-20 FAIL and C-21 FAIL — that's 2 failures = 12/14. The pass count row was wrong. Scoring confirms **V-03 = 98.57**, not 99.29. The 99.29 ceiling belongs only to C-21 designs.

### Open questions resolved

1. **C-22 applies to narrow evidence gates (V-01/V-04):** YES — any checkpoint carrying C-18 is a valid Gate-2-equivalent. C-22 is architecture-agnostic.  
2. **Scan is a valid Gate-2-equivalent for C-22 (V-02/V-05):** YES — scan carries C-18; block-to-table is local repair; C-19 auto-derives.  
3. **13/14 ceiling confirmed as structural:** C-16 PASS and C-20 PASS are mutually exclusive by definition. No design can score 14/14.

```json
{"top_score": 99.29, "all_essential_pass": true, "new_patterns": ["Named enforcement checkpoint (V-05 Enforcement Bridge) makes Gate-2-equivalent role legible from the header alone -- V-02 achieves identical structure with unlabeled scan; naming is a legibility improvement not captured by any current criterion; C-23 candidate", "C-22 scope is architecture-agnostic: minimum-patch rule holds for narrow evidence gates, scan-based checkpoints, and full Gate-2 designs -- the Gate-2-equivalent is any checkpoint carrying C-18, not only a full C-16 consolidating gate; R4 open question closed", "13/14 ceiling is provable by construction, not empirical -- C-16 PASS and C-20 PASS are logically mutually exclusive; V-03 prediction error confirmed (coverage table showed C-20+C-21 both FAIL = 12/14, not 13/14)"]}
```
nce Notes

### V-01 (Three-Layer Distributed, C-20 single-axis) -- 98.57

**C-16 PARTIAL:** Pre-flight holds C-12/C-13; Kill Barrier Evidence Gate holds C-11+C-18; Gate 4 holds C-14. Three separate enforcement layers, no single consolidation point.

**C-18 PASS:** Kill Barrier Evidence Gate: "NOTE: Each AMEND option in the AMEND DIRECTIVE will require (a) a named persona and (b) a specific gap from the Step 3 table, enforced at Gate 4."

**C-20 PASS:** Three-layer architecture achieves C-19 (C-15 table column + C-18 forward ref co-occur) with C-16 PARTIAL. Orthogonality demonstrated.

**C-21 FAIL:** Gate-based design. C-21 requires scan-based (non-gate) register.

**C-22 PASS:** Evidence gate carries C-18 verbatim. Block-to-table in Step 3 is complete local repair; Gate 4 untouched; C-19 auto-derives. Narrow evidence gate qualifies as Gate-2-equivalent -- C-22 is architecture-agnostic.

---

### V-02 (Scan-Forward-Ref, C-21 single-axis) -- 99.29

**C-16 PASS:** Pre-Step-4 Scan bundles all four: C-11 (kill barrier confirmation), C-12 (vocab), C-13 (rationale), C-14 via fourth bullet ("Each AMEND option in Step 4 will require (a) a named persona and (b) a specific gap from the Step 3 table, enforced at the Step 4 check").

**C-18 PASS:** Fourth scan bullet IS the forward reference sentence.

**C-20 FAIL:** C-16 PASS excludes C-20 by definition (C-20 requires C-16 PARTIAL / multi-layer distribution).

**C-21 PASS:** Scan covers C-11/C-12/C-13. One announcement sentence simultaneously promotes scan to C-16 consolidation point and achieves C-18. Exact C-21 definition.

**C-22 PASS:** Scan carries C-18. Table carries C-15. Block-to-table repair local to Step 3; scan unchanged; C-19 auto-derives.

---

### V-03 (Gate-2-Canonical, C-22 single-axis) -- 98.57

**C-16 PASS:** Gate 2 bundles C-11 (kill barrier confirmation), C-12 (vocab), C-13 (rationale), C-14 via forward reference ("Each AMEND option in Gate 4 will require (a) a named persona and (b) a specific gap from the Phase 2 table, enforced at Gate 4").

**C-18 PASS:** Gate 2 fourth bullet = forward reference to Gate 4.

**C-20 FAIL:** C-16 PASS excludes C-20 by definition.

**C-21 FAIL:** Gate-based design (Phase/Gate structure). C-21 requires scan-based non-gate register.

**C-22 PASS:** Gate 2 carries C-18. Phase 2 has table (C-15 PASS). Block-to-table is minimum complete repair; Gate 2 and Gate 4 unchanged; C-19 auto-derives.

> **Prediction discrepancy confirmed:** Variations file predicted 13/14 -> 99.29 for V-03. The coverage table in the same file correctly showed C-20 FAIL + C-21 FAIL but the pass count row stated 13/14 in error. Scoring confirms 12/14 -> 98.57.

---

### V-04 (Three-Layer + Gate-2-Equivalent, C-20+C-22 combined) -- 98.57

**C-16 PARTIAL:** Pre-flight holds C-12/C-13; Kill Barrier Gate 2 holds C-11+C-18; Gate 4 holds C-14. Same three-layer architecture as V-01, distinguished by explicit "Kill Barrier Gate 2" naming.

**C-18 PASS:** Kill Barrier Gate 2: "Each AMEND option in the AMEND DIRECTIVE will require (a) a named persona and (b) a specific gap from the Step 2 table, enforced at Gate 4."

**C-20 PASS:** Three-layer distribution achieves C-19 with C-16 PARTIAL. "Kill Barrier Gate 2" label makes Gate-2-equivalent role legible in a distributed architecture.

**C-21 FAIL:** Gate-based design.

**C-22 PASS:** Kill Barrier Gate 2 explicitly states the minimum-patch rule: "if Step 2 per-persona output were the only structural gap (blocks instead of table), converting to table is the complete repair -- Gate 2 and Gate 4 do not change." C-22 articulated directly in the prompt.

---

### V-05 (Scan-Table Hybrid, C-21+C-22 combined) -- 99.29

**C-16 PASS:** Enforcement Bridge bundles C-11 (kill barrier confirmation), C-12 (vocab), C-13 (rationale), C-14 via fourth bullet ("Each AMEND option in Phase 4 will require (a) a named persona and (b) a specific gap from the Phase 3 table, enforced at the Phase 4 check").

**C-18 PASS:** Enforcement Bridge fourth bullet = forward reference to Phase 4.

**C-20 FAIL:** C-16 PASS excludes C-20.

**C-21 PASS:** Enforcement Bridge labeled "ENFORCEMENT BRIDGE (scan before Phase 4)" -- scan-based register confirmed. Covers C-11/C-12/C-13; fourth bullet closes C-16 and C-18 simultaneously.

**C-22 PASS:** Enforcement Bridge carries C-18. Phase 3 table carries C-15. Block-to-table is complete local repair; Enforcement Bridge unchanged; C-19 auto-derives.

---

## Open Questions Resolved

**1. Does C-22 apply to narrow evidence gates (V-01, V-04)?**
YES. The evidence gate carries C-18; block-to-table repair is local to Step 2/3 output structure; gates unchanged; C-19 auto-derives. C-22 is architecture-agnostic: any checkpoint that carries C-18 qualifies as the Gate-2-equivalent.

**2. Is a scan a valid Gate-2-equivalent for C-22 (V-02, V-05)?**
YES. The scan carries C-18 via the forward-reference sentence; block-to-table repair does not touch the scan; C-19 auto-derives from C-15+C-18 co-occurrence. Confirmed by V-02 (unlabeled scan) and V-05 (named Enforcement Bridge).

**3. R5 ceiling confirmation?**
Confirmed at 99.29. The mutual exclusivity of C-16 PASS and C-20 PASS is logical: a design with a single consolidating gate cannot simultaneously demonstrate multi-layer distribution without consolidation. C-21 PASS requires C-16 PASS. Therefore the 14th aspirational slot is always occupied by exactly one of {C-20, C-21}. No single variation can score 14/14. Ceiling is structural, not empirical.

**4. V-03 prediction accuracy?**
V-03 was predicted at 13/14 -> 99.29. Actual: 12/14 -> 98.57. The ceiling at 99.29 is reached only by C-21 designs (V-02, V-05). V-03 as canonical gate-2 design does not trigger C-21 (gate-based, not scan-based).

---

## Excellence Signals (R5)

**Signal 1: Named enforcement checkpoint makes Gate-2-equivalent role explicitly legible**

V-05's "ENFORCEMENT BRIDGE (scan before Phase 4)" label communicates the scan's dual role (C-16 consolidation point + Gate-2-equivalent) from the header alone. V-02 achieves identical structure with an unlabeled "PRE-STEP-4 SCAN." Naming is a legibility improvement not captured by any current criterion. R6 C-23 candidate: *Enforcement checkpoint is named in a way that makes its Gate-2-equivalent role structurally legible from the checkpoint header, without requiring the reader to trace the design.*

**Signal 2: C-22 scope is architecture-agnostic -- minimum-patch rule is a property of C-18 presence, not gate format**

All five variations pass C-22. The rule holds for narrow evidence gates (V-01/V-04), scan-based checkpoints (V-02/V-05), and full Gate-2 designs (V-03). If C-18 is present in any checkpoint, block-to-table is always the minimum sufficient repair for C-15, and C-19 always auto-derives. C-22's Pass condition "Gate-2-equivalent" means "any checkpoint carrying C-18," not "a full C-16 consolidating gate." Primary R4 open question closed.

**Signal 3: The 13/14 ceiling is provable by construction**

The ceiling is a logical consequence of criterion definitions, not an observed pattern. R6 design space: criteria that reward designs for explicitly acknowledging the C-16/C-20 tradeoff as a named architectural decision, or that test for a new orthogonal dimension not yet covered by C-09..C-22.

---

## R6 Design Direction

Both the gate-consolidation strategy (V-02, V-03, V-05) and the multi-layer distribution strategy (V-01, V-04) reach equivalent capability depth. The next orthogonal dimension to probe:

- **Legibility of checkpoint naming** (C-23 candidate) -- V-05's "Enforcement Bridge" label vs. V-02's unlabeled scan. Does named-checkpoint legibility predict better model compliance at execution time?
- **Explicit tradeoff acknowledgment** -- Does a prompt that names the C-16/C-20 architectural choice ("multi-layer distribution chosen; consolidating gate is an alternative") perform differently than one that implements a strategy without naming it?
- **Cold-start completeness** -- All R5 variations assume the model knows what personas to use. Does the design provide sufficient scaffolding when /validate-inertia runs with no prior feature context?
