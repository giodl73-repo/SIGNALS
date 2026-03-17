File written. Here is the full output:

---

# flow-dataflow — Round 3 Variations (Rubric v2)

**File**: `simulations/quest/golden/flow-dataflow-variate-R3-2026-03-15.md`

---

## Variation Design Notes

Three single-axis variations, two combined. The rubric's three new aspirational criteria — C-10 (pre-trace entity inventory), C-11 (systematic boundary labeling), C-12 (verified-unchanged schema assertion) — are the structural targets for R3.

**Axes selected**: role sequence, output format, lifecycle emphasis, inertia framing.

**Three new signal candidates for the next rubric version:**
1. **Schema-diff table** (V-02) — 4-column Field/Entry/Transformations/Exit table makes silent schema drift visually detectable without reading prose
2. **Inline boundary gate with stage-open prohibition** (V-03) — "Stage N+1 does not open until gate B[N]->[N+1] is complete" makes C-02 omission a structural protocol violation, not a prose gap
3. **Label-embedded "no handling" flag** (V-05) — requiring the label inside the flag itself (`"no handling — risk accepted [B2->3]"`) makes every unhandled boundary directly addressable in recovery prescriptions

---

## Variation Summary

| Variation | Axis | Scenario | Key structural test |
|-----------|------|----------|---------------------|
| V-01 | Role sequence (natural F→O→C) | B2B AR-to-GL sync | Baseline: essentials + recommended with standard prose, no aspirational scaffolding |
| V-02 | Output format (table-dominant) | Customer order CDX sync | Schema-diff table per stage; BOUNDARY SUMMARY TABLE with required Domain Entity at Risk column |
| V-03 | Lifecycle emphasis (inline gates) | Inventory demand-to-replenishment | "Stage N+1 does not open until BOUNDARY GATE B[N]->[N+1] is fully stated" |
| V-04 | Role sequence (O→C→F) + inertia | Purchase-to-pay procurement | Operations-first incumbent baseline; Finance skip-level cites Operations (pos 1) |
| V-05 | C-10 + C-11 + C-12 all scaffolded | Subscription billing-to-revenue | Step 0 entity inventory, label-embedded "no handling" flags, schema-unchanged verification rule |

---

### Scoring predictions against rubric v2

| Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | Predicted composite |
|-----------|------|------|------|------|------|------|------|------|------|------|------|------|---------------------|
| V-01 | P | P | P | P | P | P | P | ? | ? | N | N | N | ~80 |
| V-02 | P | P | P | P | P | P | P | ? | ? | N | P | ? | ~82 |
| V-03 | P | P | P | P | P | P | P | P | ? | N | P | ? | ~84 |
| V-04 | P | P | P | P | P | P | P | P | P | N | ? | ? | ~86 |
| V-05 | P | P | P | P | P | P | P | P | ? | P | P | P | ~90 |

V-05 is the primary golden candidate. V-02's schema-diff table and V-03's gate language are the two most likely new signal sources for rubric v3.
