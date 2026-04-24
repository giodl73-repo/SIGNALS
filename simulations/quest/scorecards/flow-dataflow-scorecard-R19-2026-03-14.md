| 1 | V-05 CPG O→F→C 15SC | 4/4 | 3/3 | 9.89 | **99.89** | YES | PASS | PASS | PASS | PARTIAL |
| 4 | V-01 Pharma F→O→C | 4/4 | 3/3 | 9.67 | **99.67** | YES | FAIL | PASS | PASS | PARTIAL |
| 5 | V-03 SaaS prose | 4/4 | 3/3 | 9.46 | **99.46** | YES | FAIL | PARTIAL | PARTIAL | PARTIAL |

---

## Discriminator Analysis

### Why C-26 is the primary separator

C-26 costs 0.217 pts — the single largest per-criterion loss available. V-01 and V-03 both use F→O→C, the natural role sequence for Finance-led pipelines. No instruction phrasing compensates for natural ordering; the role sequence IS the criterion. V-01 would tie the top cluster if it used any non-natural sequence.

### Why C-53 is universally PARTIAL

Every variation has the same structural gap: SC-3, SC-4, SC-7 govern `[A-04]/[A-07]/[A-10]` or `[A-03]/[A-06]/[A-09]` in the governed-artifact slot but describe enforcement at the "column-header level" or "cell-value level" without re-citing those artifact tokens in the enforcement clause. Eliminating this gap would require each column-governing SC to repeat its artifact tokens in the enforcement description — e.g., "a `[A-04]`, `[A-07]`, or `[A-10]` boundary block with a missing `Elapsed (cumul.)` column fails." V-05's SC-14 demonstrates this pattern correctly for [A-00]; the gap is that SC-3, SC-4, SC-7 were not upgraded to match.

### Within the top cluster: structural differentiation

| Dimension | V-02 | V-04 | V-05 |
|-----------|------|------|------|
| DETECTABILITY INDEX columns | 2 | 2 | 3 (adds Responsible Role) |
| Phase Gate 0 items | 1 (row count) | 1 (row count) | 2 (row count + completeness) |
| SCs governing [A-00] | 1 (SC-0) | 1 (SC-0) | 2 (SC-0 + SC-14) |
| [A-00] dual-slot SCs | 1 | 1 | 2 |
| SC count | 14 | 14 | 15 |
| Incumbent depth | standard ≥3 | max ≥7 | standard ≥3 |

V-05 is the excellence candidate. V-04's ≥7-step incumbent framing is the deepest C-15 stress but doesn't generate a rubric score differential.

---

## Excellence Signals — Round 19

### E-1: Phase Gate 0 as multi-item structural completeness gate (V-05)

V-01 through V-04 attach Phase Gate 0 to [A-00] with a single item: row count = N. V-05 adds a second item: every row has a non-empty Responsible Role value. The structural advance is that Phase Gate 0 can enforce multiple independent dimensions of [A-00] simultaneously — count integrity AND column completeness — before any role content is produced. Each new structural property added to [A-00] maps to a new Phase Gate 0 checklist item. A single-item Phase Gate 0 can only catch count failures; a multi-item Phase Gate 0 catches structural omissions at the cell level without reading role content.

This is the projected **C-54** pattern: *Phase Gate 0 must carry one explicit verification item per structural dimension of [A-00]; a Phase Gate 0 with fewer items than [A-00] has structural dimensions is incomplete.*

### E-2: SC-14 as parallel [A-00] governor with dual-slot anchoring (V-05)

V-05's SC-14 ROLE ASSIGNMENT governs [A-00] (third column) with [A-00] in both governed-artifact slot and enforcement clause: "governs [A-00] (third column `Responsible Role`); enforced by per-row non-empty check in [A-00] — any row with empty Responsible Role is detectable from [A-00] column cells." SC-0 also governs [A-00] with dual-slot. The pattern is: [A-00] is a multi-governed artifact; each governance dimension requires its own SC; each such SC must have [A-00] in both slots. SC-0 + SC-14 together form a paired governance structure on [A-00] that is more machine-verifiable than a single SC governing all dimensions.

This is the projected **C-55** pattern: *Every SC governing [A-00] must name [A-00] in both its governed-artifact slot and its enforcement clause; a prompt with multiple [A-00]-governing SCs must maintain dual-slot anchoring in each.*

---

## Recommended Golden Candidate

**V-05** — 99.89, all essential PASS, non-natural O→F→C sequence, 3-column DETECTABILITY INDEX, Phase Gate 0 two-item gate, SC-14 paired with SC-0 on [A-00]. Highest structural advancement toward C-54/C-55.

**V-02** and **V-04** are peer goldens at 99.89. V-04's ≥7-step incumbent is a candidate for a future criterion on incumbent depth proportional to pipeline complexity.

---

```json
{"top_score": 99.89, "all_essential_pass": true, "new_patterns": ["Phase Gate 0 multi-item structural completeness gate: V-05 carries two verification items (row count = 15 AND every row has non-empty Responsible Role), establishing that Phase Gate 0 enforces one item per structural dimension of [A-00] — a single-item gate catches only count failures while a multi-item gate catches cell-level omissions before any role content is read", "SC-14 ROLE ASSIGNMENT as parallel [A-00] governor with dual-slot anchoring: SC-14 governs the third column of [A-00] with [A-00] in both governed-artifact slot and enforcement clause, paired with SC-0 which also governs [A-00] with dual-slot — establishing the pattern that [A-00] is a multi-governed artifact where each new structural dimension requires its own SC with [A-00] named in both slots"]}
```
