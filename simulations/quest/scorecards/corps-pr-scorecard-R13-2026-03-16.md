Scorecard written.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["self-contained audit block pairs evidence with derived verdict in a single named block — no split across adjacent structural elements", "column-header naming promotes slot labels to table-structure level making compliance an O(1) column-count check rather than cell-content parsing", "three-level enforcement hierarchy partitions new criteria across pipeline/block/template-column levels without mutual interference"]}
```

---

**Summary**

| Rank | Variation | Score | Failing |
|------|-----------|-------|---------|
| 1 | **V-05** | **100.00** | — |
| 2 | V-04 | 99.67 | C-38 |
| 3 | V-01 / V-02 / V-03 | 99.33 | 2 each |

**V-05 achieves 30/30 aspirational** — the R13 target. All five variations are golden (all essential pass, composite ≥ 80).

**Three excellence signals extracted from V-05:**

1. **Self-contained audit block** — C2 RESULT block holds both the per-field evidence (a)-(e) PRESENT/ABSENT and the terminal verdict ("all five fields PRESENT") in one named block. No cross-block reading required.

2. **Column-header naming** — [IA-VERDICT] and [ROLE-MECHANISM] promoted from inline cell labels to named table column headers. Slot compliance is auditable by column count; no cell-content parsing.

3. **Three-level enforcement hierarchy** — C-36 at pipeline exit condition level, C-37 at block level, C-38 at table-column level. Independent axes; no mutual interference. Each gap closed at its natural structural layer.
