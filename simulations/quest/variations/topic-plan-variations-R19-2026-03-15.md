Written to `simulations/quest/golden/topic-plan-variate-R19-2026-03-16.md`.

---

## Round 19 — topic-plan Variations Summary

**Three single-axis, two combinations. New criteria targeted: C-56 and C-57.**

---

### C-56: Downstream inertia recurrence as named labeled blocks

The key distinction from R18: R18 required verbatim blocks to be *present* (structurally visible by absence). R19 requires each block to be *independently scannable by site label* — a unique numbered label in the block header so you can identify which of the 3 gates you're looking at without reading surrounding text.

**Implementation**: The INERTIA-GATE template gains a `[SITE: ___]` slot with a closing verification line enumerating all 3 expected site labels. At each reproduction site, the instruction reads `INERTIA-GATE [SITE N of 3: Step X — context]`.

---

### C-57: Per-step analytical purpose declaration

From R18 V-05 pattern, now formalized. Each step opens with `This step exists so that: [purpose]` before any instructions — naming the downstream step it enables and the failure mode it prevents.

---

### Variation axes chosen

| Variation | Single axis | C-56 | C-57 |
|-----------|-------------|------|------|
| V-01 | Inertia framing — numbered site labels | PASS | FAIL |
| V-02 | Lifecycle emphasis — per-step purpose | partial (no labels) | PASS |
| V-03 | Role sequence — defense before strategy read | partial | FAIL |
| V-04 | V-01 + V-02 | PASS | PASS |
| V-05 | V-01 + V-02 + V-03 | PASS | PASS |

**Expected scoring order**: V-05 ≥ V-04 > V-01 > V-02 > V-03

The V-03 role-sequence reordering (pre-read defense register before `strategy.md`) is a new axis not tested in prior rounds. Its hypothesis: defense commitment is only genuine if made before reading the document it defends. The defense-basis column in Step 4c (`D-01` vs `"Post-read constructed"`) becomes a temporal audit column.
