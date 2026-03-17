Written to `simulations/quest/rubrics/flow-throttle-rubric-v19-2026-03-16.md` (256 lines, up from 227).

---

**What changed in v19**

Four new aspirational criteria extracted from R18 excellence signals:

| ID | Source | Pattern |
|----|--------|---------|
| **C-49** | V-02 Field 5 | Audit gate-compliance field elevated from prose/flat verdict to typed-row table (`Item | Criterion | Evidence required | Status`). Parallels C-47's elevation of bypass defeat to typed register — same pattern applied to the C-42 audit artifact |
| **C-50** | V-04 + V-03 | Count verification atomized into individually-instructed sub-steps (G-1 through G-4) concluding in a multi-field VERIFICATION STATUS record with a separate fill field per component (SIG-01 confirmed / SIG-02 confirmed / Role 2 activation cleared). C-43 requires the verification role to exist; C-50 requires the sequence *within* that role to be atomized so no single gesture satisfies all components simultaneously |
| **C-51** | V-04 | `SHALL NOT activate if` column in the role activation chain table at the prompt header, making bypass conditions simultaneously header-scannable alongside activation and handoff signals. C-46 requires the chain at the header; C-51 extends the header table to carry the negative-activation constraint — three role-contract facts (activate, handoff, bypass) co-located in the header |
| **C-52** | V-05 | Non-conflation statement quotes the "Does NOT confirm" cell value verbatim (column reference → quoted-artifact citation). C-45 requires the column and a statement referencing it by name; C-52 requires verbatim quotation, making the non-conflation claim independently falsifiable by string match rather than content interpretation |

**Score delta**: 200 pts (40 × 5) → 220 pts (44 × 5), max composite 290 → 310. Golden threshold unchanged.

**Structural progression table** gains a second two-column extension block showing C-49–C-52 mapped as precision upgrades of the C-45/C-46/C-47/C-48 positions: left column traces signal-chain visibility (column-readable → verbatim cell citation; header chain → header chain + bypass conditions); right column traces verification enforcement (typed register row → audit field typed table; required-fill gate → atomized sub-steps with multi-field status record).
