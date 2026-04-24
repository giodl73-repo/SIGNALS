Here are the 5 complete variations for **trace-state Round 15** under rubric v13:

---

## Variation Map

| Var | Axis | Domain | New Criteria Targeted |
|-----|------|--------|-----------------------|
| **V-01** | Output format — tabular three-pass | Finance → Sales → CS | C-30, C-34, C-36, C-37 (tabular ceiling; C-38/C-39 not reachable in this format) |
| **V-02** | Output format — step-block single-pass | Sales | **C-38 + C-39** (new R15 ceiling, both simultaneously) |
| **V-03** | Role sequence — CS-first tabular | CS → Sales → Finance | C-30, C-34, C-36, C-37 (same tabular ceiling, different defect-class hypothesis) |
| **V-04** | Step-block + lifecycle emphasis (four sub-steps) | CS | **C-38 + C-39** + C-02/C-03 structural inevitability |
| **V-05** | Finance-first + conversational/foil register | Finance → Sales → CS | C-37, **C-38 + C-39** throughout all three passes |

---

## Key Design Decisions

**C-38 and C-39 mechanism** (V-02, V-04, V-05): Every field label uses the fused format:
```
[C-XX: directive — FAILS if: specific failing pattern] [C-38][C-39]
```
The `directive:` component satisfies C-38. The `FAILS if:` component satisfies C-39. A single annotation earns both — directly parallel to how V-01/V-03 earn C-30 + C-34 in the same column header.

**Why C-38/C-39 require step-block format**: Tabular column headers get C-30 and C-34. These do not cross-satisfy C-38/C-39, which require the same fusion at the field-annotation level in step-block format. V-01 and V-03 target the tabular ceiling; V-02, V-04, V-05 target the step-block ceiling.

**C-37 at pass headings** (V-01, V-03, V-05): Each `### Pass N` heading carries the form `[C-37: consequence clause — what fails if this pass omits its registry]`, making criterion enforcement visible at the navigation level before any field is read.
