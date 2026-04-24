Written to `simulations/quest/golden/corps-rob-variate-R15-2026-03-17.md`.

---

## Variate R15 -- corps-rob

**5 variations generated. Summary:**

| Var | Axis | New Criteria | Predicted Score (v15) |
|-----|------|-------------|----------------------|
| V-01 | Output format | C-45 only (count annotation: "Exactly 2 criteria require glossary scope") | 270/280 |
| V-02 | Lifecycle emphasis | C-46 only (two branches embedded in RULE AUDIT-TABLE) | 270/280 |
| V-03 | Phrasing register | C-46 only (two branches in dedicated RULE AUDIT-INDEPENDENCE) | 270/280 |
| V-04 | Output format + Lifecycle emphasis | C-45 + C-46 embedded + C-39 | **275/280** |
| V-05 | Output format + Phrasing register | C-45 + C-46 dedicated rule + C-39 | **275/280** |

**Key structural changes per new criterion:**

**C-45** (V-01, V-04, V-05): The glossary exclusivity preamble gains a count-fixing prefix -- `Exactly 2 criteria require glossary scope -- any addition of a third requires an explicit count update` -- before the C-30/C-34 label+description pairs.

**C-46 embedded** (V-02, V-04): RULE AUDIT-TABLE replaces the single "mandatory regardless of table presence" clause with two numbered branches: `(1) When table is present: AUDIT RESULT block preserved beneath it. (2) When table is absent: AUDIT RESULT block still required.`

**C-46 dedicated** (V-03, V-05): RULE AUDIT-TABLE sheds the independence clause entirely; a new RULE AUDIT-INDEPENDENCE carries both branches. RULE AUDIT-TABLE owns ordering only; RULE AUDIT-INDEPENDENCE owns conditionality only.

**V-04 vs V-05 comparison test**: same score prediction, different C-46 architecture. If they diverge in scoring, it surfaces the more reliable structural path -- the R15 equivalent of R14's V-01 vs V-02 (embedded clause vs dedicated named rule) for C-44.

**Persistent gap**: C-47+ territory -- R15's universal C-45/C-46 pass may reveal the next signal for v16.
