The file is written. Here is the Round 8 output:

---

## org-pr — Round 8 Variations

**Saved**: `simulations/quest/golden/org-pr-variate-R8-2026-03-16.md`

---

### Round 8 Objectives

Two structural findings from R7 drive R8:

1. **The embedded-conflict path caps at 99.41** — C-22 FAIL when conflict resolution is a *procedure* (not a table). Never tested with a conditional *per-role table*.
2. **The 2-axis path (R7 V-02) never had escape closure** — it sat at 99.41 with C-14 PARTIAL.

Four open questions investigated:

| Question | Criterion |
|---|---|
| Does a per-role conflict sub-table (inline, conditional) satisfy C-22? | C-22 |
| Can 2-axis + standalone Conflict section + escape closure reach 100.00? | C-14, C-19 |
| Is single-axis + standalone Conflict + escape closure a valid 100.00 path? | C-21, C-26, C-27 |
| Can C-23 fire from the opening reconciliation rule alone (not the resolution column)? | C-23 |

---

### Variation Plan

| V | Axis | Hypothesis |
|---|------|------------|
| **V-01** | Per-role conflict sub-table, 2-axis, no escape closure | C-22 PASS from per-role table → 99.41; C-22 FAIL → 98.82 |
| **V-02** | V-01 + escape closure | C-22 PASS + C-14 PASS → **100.00** via embedded-conflict path |
| **V-03** | 2-axis + standalone Conflict section + escape closure (no priority table) | R7 V-02 + escape closure → **100.00**; minimum-structure path |
| **V-04** | Single-axis + standalone Conflict section + escape closure | Single-axis hits **100.00**; C-21/C-26/C-27 all N/A→PASS |
| **V-05** | V-03 + C-23 phrase in opening rule only (not in resolution column) | Tests C-23 location sensitivity: PASS → 100.00; FAIL → 99.41 |

---

### Key structural findings

**C-22 is the pivotal question for V-01/V-02.** The R7 failure mode was an embedded *procedure* — no table structure. V-01 adds an actual per-role conflict *table* with a resolution column. If the criterion fires on structural presence (table + resolution column, anywhere), V-02 is the first 100.00 without a global standalone Conflict section. If C-22 requires a dedicated standalone section, both drop 0.59 pts.

**V-04 (single-axis) opens the minimum-complexity 100.00 path.** With no axis declaration (C-26 N/A→PASS), no reconciliation rule (C-21 N/A→PASS), and no priority table (C-18/C-20/C-27 all N/A→PASS), the if-stays column satisfies C-13 as a format feature without being a governance axis. If V-04 = 100.00, the minimum viable design is: authority chain + per-role finding table + standalone Conflict section + escape closure.

**R9 direction**: If V-04 = 100.00, investigate the minimum *content* within each criterion — can the invalid-form catalog be reduced, the self-check compacted, the phase gate made implicit?
