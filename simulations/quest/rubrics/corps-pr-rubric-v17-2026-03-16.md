Written to `simulations/quest/rubrics/corps-pr-rubric-v17-2026-03-17.md`.

---

## v16 -> v17: Four new criteria

The four excellence signals extracted from the R18 scorecard:

**C-51 -- IA section adversarial designation label**
Closes the gap left by C-11 (sequenced first + reference object). V-05's "Status-quo champion [C-11]:" framing showed the IA section's structural function can be declared at the header label, not just in content. C-51 requires the opening label to name the adversarial function with a criterion annotation -- auditable by label-reading alone.

**C-52 -- Pipeline sub-condition governing criterion cross-references**
Closes the gap left by C-22 (two independently auditable sub-conditions). The C-22 evidence note showed sub-condition descriptions carrying `[C-26]` inline, naming which criterion governs the result token format. C-52 requires each C1/C2 description to carry a bracketed criterion ID so the governing criterion is traceable from the pipeline declaration text without consulting the rubric.

**C-53 -- Output element governing criterion annotations**
Closes the gap left by C-25/C-28 (three-clause formula, one clause per line). The C-25 evidence note showed `<- B3 line 1 [C-25]` end-of-line annotations on each Budget verdict clause. C-53 requires named Budget verdict clause lines to carry inline governing criterion annotations -- compliance traceable by line-scan.

**C-54 -- C2 RESULT dual-form validation for field (e)**
Closes the gap left by C-32 (READ RECEIPT cross-references PRE-COMMITMENT for fields (d)/(e)). The C-32 evidence note showed `"valid: inline value OR cross-reference 'see PRE-COMMITMENT block: [row]'"` in the C2 RESULT template. C-54 requires both valid evidence forms named as explicit disjuncts in the field (e) validation instruction, preventing false fails when either form is used.

**Scoring update:**

| Band | Count | Per-criterion | Total |
|------|-------|--------------|-------|
| Essential (C-01--C-05) | 5 | 12.000 | 60 |
| Recommended (C-06--C-08) | 3 | 10.000 | 30 |
| Aspirational (C-09--C-54) | **46** | **~0.217** | 10 |
| **Max** | | | **100** |

R19 target: propagate all four annotation/designation patterns across all five variations.
