Here are the 5 complete variations for Round 8:

---

## trace-inspect Variations R8 (v5 rubric)

**Entry state**: R7 baseline passes C-01–C-18. Three new criteria (C-19, C-20, C-21) project FAIL against v5. All five variations are complete runnable prompts.

---

### V-01 — Single axis: C-19 (EG Evidence Pass as structural lifecycle event)

**Axis**: Role sequence
**Hypothesis**: Inserting a named `EG Evidence Pass` lifecycle event into Schema 3 — declared before `SA-TO-SG PROMOTION` — makes EVIDENCE-GROUNDED state architectural. The promotion gate is structurally blocked until every EG-capable role completes its pass. Violation of C-16 becomes impossible rather than just prohibited.

**Key changes from baseline**:
- Schema 3 now declares 4 events: `EG Evidence Pass → SA-TO-SG PROMOTION → Stage 1 relay → Stage 2 relay`
- Role-Schema Binding Summary gets an `EG-capable` column (YES / NO)
- A new `EG Evidence Pass` section runs between Stage 1 and SA-TO-SG PROMOTION with a carry-forward block: `Evidence pass state: COMPLETE`
- SA-TO-SG PROMOTION header adds `(requires Evidence pass state = COMPLETE)`
- Per-role Setup block adds `EG Evidence Pass completed: YES / N/A`
- VC-3 compliance ledger gets a row: `EG Evidence Pass (C-19) — pass completes before PROMOTION`

---

### V-02 — Single axis: C-20 (Criterion Inheritance Registry)

**Axis**: Inertia framing
**Hypothesis**: A pre-printed `Criterion Inheritance Registry` table before the Coverage Matrix names C-01 through C-21 explicitly — Inherited: YES or NEW — with a registry invariant: `Silence = inactive, not inherited`. A future version that silently drops C-06 must update this table, making the omission structurally visible. The registry competes with no other prompt section; it's preamble-layer.

**Key changes from baseline**:
- New `Criterion Inheritance Registry` section added as first structural block after the preamble
- 21-row table: C-01–C-18 as `Inherited: YES / Active`, C-19–C-21 as `NEW / Active -- v5`
- Registry invariant stated: removing an Active criterion requires updating the table
- No other sections modified — pure preamble addition

---

### V-03 — Single axis: C-21 (Attribution sub-table embedded in VC-4 G-1)

**Axis**: Output format
**Hypothesis**: Making the role-to-Source attribution a pre-printed sub-table inside the VC-4 G-1 `Observed behavior` cell eliminates drift between the ledger and the attribution. Filling the row and filling the attribution are a single operation — the cell format demands the sub-table. A note states: "This is the only location where attribution appears. Do not write attribution anywhere else."

**Key changes from baseline**:
- VC-4 G-1 row in the Verdict compliance ledger has its Observed behavior cell pre-structured as: `**ATTRIBUTION SUB-TABLE (required):** | Role | Source types contributed | Finding IDs | Count |`
- A note before the ledger: "The VC-4 G-1 row is invalid without a filled sub-table. Filling the ledger row and attribution are the same operation."
- No separate attribution section exists anywhere

---

### V-04 — Combined: C-19 + C-20

**Axes**: Role sequence + Inertia framing
**Hypothesis**: The two axes operate in non-overlapping sections (Schema 3 events vs. preamble registry). No interaction risk. Tests whether the inheritance registry and the EG Evidence Pass can coexist without one crowding the other's structural signal.

---

### V-05 — Combined: C-19 + C-20 + C-21 (Full integration)

**Axes**: Role sequence + Inertia framing + Output format
**Hypothesis**: All three R7 excellence patterns at full strength. C-19 (structural gate in Schema 3), C-20 (explicit registry prevents silent criterion drift), C-21 (attribution in VC-4 G-1 — single operation). Three distinct prompt sections, no cross-section interaction. V-05 is the projected golden candidate.

---

### Projected scoring against rubric v5

| Variation | C-19 | C-20 | C-21 | Projected score |
|-----------|------|------|------|-----------------|
| V-01 | **PASS** | FAIL | FAIL | 98.5 |
| V-02 | FAIL | **PASS** | FAIL | 98.5 |
| V-03 | FAIL | FAIL | **PASS** | 98.5 |
| V-04 | **PASS** | **PASS** | FAIL | 99.0 |
| V-05 | **PASS** | **PASS** | **PASS** | **99.5** |

File written to `simulations/quest/golden/trace-skill-variate-R8-2026-03-17.md`.
