Here are the five complete variations for **trace-state Round 14** against the v12 rubric (C-36 and C-37 as new targets):

---

## R14 Gap Summary

All five R13 variations fail both new v12 criteria:

| Gap | Why R13 fails | R14 fix |
|-----|--------------|---------|
| **C-36** | Column headers carry C-34 disqualification conditions on quantitative/behavioral fields (C-17, C-28, C-03) — but none on structural-format fields (C-01b state name, C-01c verb phrase, C-01d state name) | Add `[C-01b: disqualifies if description written instead of state name]` etc. to every state-name and operation column header |
| **C-37** | Pass headings (`### Pass 1 — Finance Domain`) carry no criterion ID or consequence clause | Add `[C-05: if states and operations are not recognizable as Finance lifecycle vocabulary, C-05 fails]` to every `### Pass N` heading |

---

## Variation Map

| Var | Axis | Domain | Key Probe | Missing (deliberate) |
|-----|------|--------|-----------|----------------------|
| **V-01** | Role sequence (Finance→Sales→CS) + **C-36 only** | All three | C-36 graft onto R13 V-01 base — structural-format disqualification in isolation | C-35, C-37 |
| **V-02** | Output format (step blocks) + **C-37 only** | Sales | C-37 Pass-N heading annotation in isolation — no C-36 | C-34, C-36 |
| **V-03** | Lifecycle emphasis (sub-step blocks, CS) + **C-36 on sub-element labels** | CS | C-36 earned at sub-element level rather than parent column — does sub-element placement qualify? | C-35, C-37 |
| **V-04** | Combined: CS→Finance→Sales + **C-36 + C-37** | All three | Both new criteria on R13 V-04 base — ceiling probe | None |
| **V-05** | Combined: conversational phrasing + "naive trace" foil + **C-36 + C-37** | Finance | Formal structural annotations survive conversational register? | C-14, C-21, C-25, C-26 |

---

## Key Structural Mechanics

**C-36 pattern** (applied to every state-name and operation column):
```
Starting State [C-01b: disqualifies if a description is written instead of a state name —
               "invoice has been submitted" disqualifies; "Submitted" qualifies]
Operation      [C-01c: disqualifies if a noun phrase is used instead of an imperative verb
               phrase — "Invoice Approval" disqualifies; "Approve Invoice" qualifies]
Ending State   [C-01d: disqualifies if a description is written instead of a state name]
```

**C-37 pattern** (applied to every `### Pass N` heading):
```
### Pass 1 — Finance Domain [C-05: if states and operations are not recognizable as Finance
invoice lifecycle vocabulary by a Finance expert, C-05 fails for this pass]
```

**V-04** is the ceiling variation — it combines the full R13 V-04 aspirational set (C-34, C-35, and 21 others) with both grafts, targeting 25/29 aspirationals.
