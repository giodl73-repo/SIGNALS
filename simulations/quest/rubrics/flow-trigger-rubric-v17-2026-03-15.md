v17 written. Here is the summary of what was extracted and added:

---

## v17 — two new aspirational criteria extracted from R19

| ID | Source | What it captures | Extends | N_aspirational | Max (raw) |
|----|--------|-----------------|---------|----------------|-----------|
| C-46 | V-03 C-45 PARTIAL (phases 0–2 complete; phases 3–5 name dependency only — violation mode absent) | **Uniform per-phase forward-looking ordering completeness** — ALL lifecycle phases that embed a forward-looking ordering statement carry BOTH (a) the downstream dependency AND (b) the violation mode. No half-statement phases: a dependency without a violation mode is a structural preference, not a structural commitment. PARTIAL = ≥50% of ordering-statement phases carry both; FAIL = <50%. | C-45 (same domain — C-46 raises the per-phase coverage floor from "at least two complete phases" to "all phases complete"); mirrors C-44 extending C-42 exactly | 37 → 38 | 157.5 → 160.0 |
| C-47 | V-01 axis ("Domain Expert obligations precede Auditor in the PHASE 0 OBLIGATION REGISTRY row order") | **Execution-sequence-aligned Phase 0 registry row ordering** — registry rows appear in their execution sequence, with declaration-time obligations (Domain Expert, producing artifacts) above verification-time obligations (Auditor, detecting gaps). Row position encodes lifecycle precedence redundantly with the activation event column, enabling positional consistency checking. | C-32 (unified registry — C-47 adds a row-ordering invariant); C-38 (per-row temporal constraint — C-47 converts those constraints into a table-level ordering guarantee) | 38 → 39 | 160.0 → 162.5 |

**Structural relationships:**
- C-46 is to C-45 what C-44 is to C-42: the same "raise the coverage floor from partial to uniform" extension, applied at the phase-body level instead of the bracket level.
- C-47 is orthogonal to both — it operates on the registry's row ordering rather than on phase bodies or NOTE-block brackets. It makes the execution sequence inspectable from table position alone, creating a double-encoding that any row reordering makes structurally visible.
