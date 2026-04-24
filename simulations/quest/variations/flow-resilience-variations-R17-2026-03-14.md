Written to `simulations/quest/rubrics/flow-resilience-rubric-v16-variate-R17-2026-03-15.md`.

---

## R17 Variations Summary

**Root diagnosis entering R17**: V-04 (R16) has three independent enforcement locations spanning three hierarchy levels (preamble → sub-part → column contract) but lacks an explicit restatement label — C-50 FAIL by one phrase. V-05 (R16) has the restatement label but enforcement is embedded *within* sub-part 1d, not before all sub-parts — C-49 FAIL by position.

**The synthesis**: V-04's structure is already C-50-structurally eligible. The minimal fix: add `(restated for co-location)` to the Column Contract Recovery Path Rule B reference.

| Variation | Axis | C-49 | C-50 | Expected Total |
|---|---|---|---|---|
| **V-01** | Minimal synthesis — restatement label on Column Contract entry | PASS | PASS | **42/42** |
| **V-02** | Phrasing register — formal § enumeration throughout; `§ 1.2 restated at column-contract level` | PASS | PASS | **42/42** |
| **V-03** | Role sequence — D-Phase Enforcement Note at document-header scope (4th hierarchy level) | PASS | PASS | **42/42** |
| **V-04** | Lifecycle emphasis + synthesis — per-stage named sub-specs with Rule B restatement at stage level | PASS | PASS | **42/42** |
| **V-05** | Full synthesis — all axes (§ notation + inertia framing + lifecycle + role sequence + restatement) | PASS | PASS | **42/42** |

**What changed across variations**:

- **V-01**: Structural minimum — one phrase added to Column Contract Recovery Path entry. Everything else identical to V-04 (R16).
- **V-02**: Entire prompt shifts to formal legal § enumeration. Enforcement preamble becomes `§ 1` with `§ 1.1` / `§ 1.2`. Column Contract cites `§ 1.2 restated at column-contract level`.
- **V-03**: Adds a document-header Role Declaration section (before the enforcement preamble) that contains a D-Phase Enforcement Note — placing Rule B at a fourth distinct hierarchy level (document-header > preamble > sub-part > column-contract). The preamble explicitly acknowledges this with "Rule B restated from D-Phase Enforcement Note above."
- **V-04**: Expands Recovery Path specification to named per-stage sub-specs (following V-05 R16's pattern) with Rule B restatement on the Recover stage sub-spec specifically, creating a fifth enforcement location at stage-specification granularity.
- **V-05**: Full synthesis — § formal register, inertia-as-competitor framing in §1a, D-Phase `§ 0` at document header, per-stage sub-specs with `§ 1.2 restated for co-location at stage level` on the Recover stage.
