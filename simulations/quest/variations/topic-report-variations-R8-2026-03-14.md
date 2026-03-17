## Round 8 Variations -- `topic-report`

**File written**: `simulations/quest/rubrics/topic-report-rubric-v8-variations-R8-2026-03-14.md`

---

### Variation Axes Selected

| Axis | Single-axis | Description |
|------|-------------|-------------|
| A | V-01 | Dual-identifier violation -- `(no stall cost -- G-9 INERTIA / C-21 violation)` |
| B | V-02 | Recovery directive in Branch B header -- explicit re-read instruction |
| C | V-03 | Slot-indexed contract register -- `G-9 INERTIA [SLOT 4]: ...` |
| A+B | V-04 | Combined: dual-identifier + recovery directive |
| A+B+C | V-05 | Ceiling: all three |

---

### Design rationale

**Neutral base** = R7 V-05 stripped of two properties that exist structurally in v8 but are not captured by any C-01--C-27 pass condition:
1. The violation text at SLOT 4 carries only `C-21` (not `G-9 INERTIA / C-21`) -- C-23 only requires the rubric ID, C-24 only requires the register label at the annotation
2. Branch B THREE-LAYER header has no recovery directive -- C-25 only requires LAYER 1/2/3 enumeration

The slot-indexed register (Axis C) is entirely new -- no prior design carries `[SLOT n]` forward-navigation annotations in the register.

**Key discriminators for v9 rubric candidates:**
- **C-28**: dual-identifier violation -- register label AND rubric ID co-present in violation text at the same annotation
- **C-29**: Branch B recovery directive -- explicit named re-read instruction within the Branch B header, distinct from C-25's structural requirement
- **C-30**: slot-indexed register -- each contract register entry names its governed output slot, establishing forward-navigation from register to template position (the backward direction is C-19/C-24)

Under v8: all 5 score 19/19 = 100.0. Under potential v9 with `/22 * 10`: V-05 ceiling = 22/22 = 100.0; V-04 = 95.5; V-01/V-02/V-03 each = 90.9.
