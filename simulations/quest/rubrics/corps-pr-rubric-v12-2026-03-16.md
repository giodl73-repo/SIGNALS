`corps-pr-rubric-v12-2026-03-17.md` written to `simulations/quest/rubrics/`.

---

## Three new criteria extracted from Round 13

**C-39 — C2 RESULT block is self-contained: per-field evidence and terminal verdict co-appear in a single named block** *(C-37 self-containment gap)*

C-37 requires per-field enumeration; C-39 requires that the checklist AND the derived terminal verdict appear in one named block — no cross-block reading. A C2 RESULT that splits the per-field rows into one block and the "SATISFIED" conclusion into adjacent prose satisfies C-37 and fails C-39.

**C-40 — [IA-VERDICT] and [ROLE-MECHANISM] are promoted to named table column headers** *(C-38 column-elevation gap)*

C-38 requires named slots in the Description field; C-40 requires those same slots to be the table column headers. Compliance becomes an O(1) column-count check rather than cell-content parsing. Inline labels in a single Description cell satisfy C-38 and fail C-40.

**C-41 — Pipeline declaration explicitly partitions C-36/C-37+C-39/C-38+C-40 across three named structural enforcement levels** *(three-level hierarchy gap)*

The three criterion families already enforce at distinct levels (exit-condition / block / table-column). C-41 requires the pipeline declaration to name that partition explicitly so each family's structural layer is independently auditable without reading output. Satisfying all three families in output without declaring the partition fails C-41.

---

### Updated scoring

| Band | Count | Per-criterion | Total |
|------|-------|--------------|-------|
| Essential (C-01–C-05) | 5 | 12.000 | 60 |
| Recommended (C-06–C-08) | 3 | 10.000 | 30 |
| Aspirational (C-09–C-41) | **33** | **0.303** | 10 |
| **Max** | | | **100** |

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 33 * 10)
```

**R14 target**: V-05 achieved 30/30 aspirational in R13 (100/100). Against v12, V-05 would fail C-39 (no self-contained audit block), C-40 (no column-header promotion), and C-41 (no declared three-level partition). The tightest integration point is C-40 + C-41 — C-40 requires restructuring the findings table, and C-41 requires the pipeline to name the structural level that C-40 occupies.
