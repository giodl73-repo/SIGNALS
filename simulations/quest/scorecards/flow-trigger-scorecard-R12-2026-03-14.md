# Flow-Trigger Skill — Round 12 Scorecard (Rubric v8)

## Results

| Variation | Essential | Recommended | Aspirational | Composite | Band | Rank |
|-----------|-----------|-------------|--------------|-----------|------|------|
| **V-02** | 4/4 → 60 | 3/3 → 30 | 15/16 → 9.4 | **99** | Gold | 1st (tied) |
| **V-05** | 4/4 → 60 | 3/3 → 30 | 15/16 → 9.4 | **99** | Gold | 1st (tied) |
| V-01 | 4/4 → 60 | 3/3 → 30 | 14/16 → 8.75 | **99** | Gold | 3rd |
| V-03 | 4/4 → 60 | 3/3 → 30 | 14/16 → 8.75 | **99** | Gold | 3rd |
| V-04 | 4/4 → 60 | 3/3 → 30 | 14/16 → 8.75 | **99** | Gold | 3rd |

**All five Gold. All essential pass.**

## R11 → R12 delta: +11 points (88 → 99)

- **C-07 closed** (all variations): recommended 2/3 → 3/3 = +10 pts. R12 added explicit enforcement with named examples and forbidden labels — every variation resolves the ambiguous-label gap.
- **C-13 closed** (all variations): per-automation arithmetic table now explicitly required in every Budget Analyst section with an enforcement rule against aggregate-only answers.
- **C-11 closed** (V-02, V-05): the verbatim-emit caption instruction is the differentiator — other variations still write enforcement as mandate text the model applies silently rather than emits as output.

## Only unscored criterion

**C-09 (storm quantification)** — still zero across twelve rounds. Budget sections produce API totals and run duration but not cascade depth as a named number. Gap analysis written to scorecard.

## JSON

```json
{"top_score": 99, "all_essential_pass": true, "new_patterns": ["Verbatim-emit caption instruction: 'Caption (emit this text verbatim immediately after the table)' forces enforcement text into model output — converts a directive rule into a required output artifact, scoring C-11 for the first time across twelve rounds", "Schema field inline annotation: inline comments within schema definitions (e.g., '<- specific named environment only') bind the requirement to the output position the model must complete, closing C-07 more reliably than narrative enforcement instructions", "Mesh Closure Certificate: a required final block that unifies all four coverage dimensions (TC-2/TC-3 annotation, TC-1 annotation, forward mesh fulfillment, pathology verdict) into a single PASS/FAIL/N/A audit artifact per IF-* label, replacing four scattered checks with one verifiable compliance signal"]}
```
