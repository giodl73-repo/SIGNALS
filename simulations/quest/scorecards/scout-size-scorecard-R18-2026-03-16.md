must select from it. This enables type-grounded correction rather than open-ended substitution.

2. **Category label required in produced gap text (V-05)**: The "Valid Gap Categories" schema requires the corrected gap to carry the label inline: `"[Category]: [description]"`. The gap's orthogonality becomes self-certifying — a reviewer can verify the gap is not a Phase 1 repetition by reading the category label alone, without consulting Phase 1. This is the C-02 pattern applied to the gap field: downstream consumers parse the category rather than infer it.

---

### C-45 Candidate Assessment

Both V-04 and V-05 explore the C-45 space. V-05's formulation is stronger: it makes the category label a structural property of the gap output, not an annotation the model produces alongside the gap. A gap that reads "Failure Semantics: exactly-once vs. at-least-once under concurrent writes" carries its own orthogonality certificate. V-04's formulation ("Name which category your corrected gap addresses") produces a separate category declaration that may diverge from the gap text itself. V-05 eliminates that divergence by embedding the label in the gap field's required output format.

**C-45 candidate definition (from R18 evidence)**: The REMEDIATION field's examples are elevated from parenthetical illustrations to a named type schema, and the produced gap carries a category label as a structural requirement — making the corrective scope's dimension class verifiable at the output level without cross-reference to Phase 1 or to the REMEDIATION field.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["REMEDIATION fourth diagnostic field carries a named positive taxonomy enabling type-grounded correction — model selects from a typed category list rather than inferring what qualifies as orthogonal", "V-05 Valid Gap Categories schema requires the category label embedded in the produced gap text itself making orthogonality self-certifying at the output level without Phase 1 cross-reference"]}
```
