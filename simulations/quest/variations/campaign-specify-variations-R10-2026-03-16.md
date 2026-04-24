Written to `simulations/quest/golden/campaign-specify-variate-R10-2026-03-17.md`.

---

## Round 10 — campaign-specify Variations

**Root cause from R9**: Two paths tied at 28/29 via non-overlapping mechanisms. V-02 had the table (C-37) but no verb in cell values. V-03 had "satisfied" bullet rows (C-36) but no table. The 29/29 ceiling requires table + "satisfied" verb in cells + gate anchor — simultaneously.

**R10 question set and variation axes:**

| Variation | Axis | Gate anchor | Cell verb | Table | Predicted |
|-----------|------|-------------|-----------|-------|-----------|
| **V-01** | Output format — table + "satisfied", no gate anchor | No | "satisfied" | Yes | 27/29 — isolates C-36 dependency on C-34 |
| **V-02** | Output format — minimal 29/29 synthesis | Yes | "satisfied" | Yes | **29/29** |
| **V-03** | Lifecycle emphasis — explicit verb consistency instruction before table | Yes | "satisfied" | Yes | 29/29 |
| **V-04** | Lifecycle emphasis — forward reference from Step 4 gate to audit table | Yes | "satisfied" | Yes | 29/29 |
| **V-05** | Lifecycle emphasis — explicit lexical-consistency constraint block in audit section | Yes | "satisfied" | Yes | 29/29 |

**Key structural finding baked into R10**: C-36 cannot be earned without C-34. The gate parenthetical is the reference verb; the audit cell is the echo. Without a parenthetical, there is no verb to echo — C-36 is structurally inapplicable. V-01 tests this dependency directly.

**V-02 is the minimal synthesis**. V-03/V-04/V-05 test whether making the verb-consistency requirement increasingly explicit at different locations (instruction before table, forward pointer from gate, constraint block in audit) adds reliability over the bare template.
