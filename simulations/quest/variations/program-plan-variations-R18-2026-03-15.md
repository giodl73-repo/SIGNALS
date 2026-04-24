Written to `simulations/quest/golden/program-plan-variate-R18-2026-03-16.md`.

---

# program-plan R18 Variate Prompt Bodies (V-01 through V-05)

**Rubric**: v18 (C-01 through C-54, 47 aspirational, 325 pts)

## Design summary

| Variate | Axis | Protocol name | C-50 | C-51 | C-52 | C-53 | C-54 | Anticipated |
|---------|------|---------------|------|------|------|------|------|-------------|
| V-01 | Output format (carry-forward) | SCAN PROTOCOL | PASS | FAIL | -- | -- | -- | ~305/325 |
| V-02 | Role sequence (carry-forward) | BOUNDED BLOCK PROTOCOL | FAIL | PASS | -- | -- | -- | ~305/325 |
| V-03 | Inertia framing (new) | INERTIA CONTRAST PROTOCOL | FAIL | FAIL | -- | -- | -- | ~295/325 |
| V-04 | Exclusion-boundary architecture (new) | EXCLUSION-BOUNDARY PROTOCOL | FAIL | FAIL | -- | -- | -- | ~295/325 |
| V-05 | Full chain (combined) | BOUNDED BLOCK PROTOCOL | PASS | PASS | PASS | PASS | PASS | 325/325 |

## Key design decisions

**V-03 (new -- inertia framing):** Each of the 10 construction steps opens with an explicit "Inertia action prevented:" label naming what a no-program-plan team does at that decision point. The failure mode is not just a preamble — it appears as a per-step foil at the exact moment each authoring choice is made. Step 9 adds an "Inertia flag" column to the compliance table.

**V-04 (new -- exclusion-boundary architecture):** The C-54 negative boundary pattern applied globally as a design philosophy. Every major requirement (gate values, stage names, skill names, echo structure, plan framing) leads with a "NOT: [X, Y, Z]" exclusion list before the positive "IS: [A]" rule. The FIELD CO-LOCATION PRINCIPLE table gains a "Forbidden forms (NOT)" column. Terminal checklist uses "IS"/"NOT" framing throughout.

**V-05 (C-54 chain):** Three changes from R17 V-05:
1. C-54 form strengthened — forbidden alternatives listed as three separately named items with "Each of these formats is individually disqualified" rather than a parenthetical
2. Self-review diagnostic step added after column mandate: four NOT/IS checks the model runs before completing Component 1
3. BAD PLAN header adds `# (NOT prose enumeration / NOT indented list / NOT bulleted entries)` as a format reminder inline at the block
4. Terminal checklist explicitly confirms C-54 pass with self-review step present
