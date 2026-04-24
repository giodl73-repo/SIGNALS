Written to `simulations/quest/rubrics/org-chart-rubric-v18-2026-03-17.md`.

---

## v18 summary

**Three new criteria** extracted from Round 17 excellence signals. All three are parallel extensions from C-46 -- the first branch point in the GATE CHAIN deepening chain.

**C-47** -- CHECKPOINT-0 pass checklist item (b) count guard with named FAIL condition (behavior, 5 pts)
Signal: V-01 non-scoring note. Closes the **count-incompleteness bypass**: C-46 requires inline enumeration with anti-pointer prohibition but sets no count obligation; a model can write 3 items inline without violating any named rule. The COUNT CHECK converts count from implied-by-structure to explicitly-obligated-with-named-FAIL. Subsumes C-46.

**C-48** -- CHECKPOINT-0 pass checklist item (b) format anchor with canonical artifact-name constraint (behavior, 5 pts)
Signal: V-02 non-scoring note. Closes the **informal-name bypass**: C-46 prohibits pointer-reference form but does not require canonical artifact names; a model can satisfy C-46 using "role list" or "inertia output" instead of the canonical forms from the GATE CHAIN block. The format anchor enforces `GATE X->Y: [artifact name]` notation with named anti-forms for informal and paraphrase substitutions. Subsumes C-46.

**C-49** -- CHECKPOINT-0 pass checklist item (b) preamble-sentence prohibition (behavior, 5 pts)
Signal: V-03 C-46 evaluation note. Closes the **declarative-preamble bypass**: C-46 prohibits pointer-reference deferral phrases but not declarative-sentence preambles ("the following transitions are restated from the block above") that precede the inline list. The prohibition names two example preamble forms and requires item (b) to open directly with entry 1. Subsumes C-46.

**Updated totals: 295 pts. Golden = 236/295 (80%).**

The chain now branches at C-46:
```
... -> C-45 -> C-46 -> C-47 (count guard)
                    -> C-48 (format anchor)
                    -> C-49 (preamble prohibition)
```
C-47, C-48, C-49 are parallel; none subsumes any other.
