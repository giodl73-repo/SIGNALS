Written to `simulations/quest/golden/draft-brainstorm-variate-R7-2026-03-16.md`.

---

## Variate R7 -- draft-brainstorm

**R7 focus**: Close C-25 (Marking-Gate Schema Lock) and C-26 (AMEND Pool-Composition Constraint).

### Gap analysis going into R7

| R6 Variation | Score under v6 | Under v7 | Gap |
|---|---|---|---|
| R6-V-03 (Prohibition Battery) | 135 | 135-137.5 | C-25 absent; C-26 borderline |
| R6-V-04 (Schema Registry) | 135 | **137.5** | C-25 PASS (structural Top-5? column), C-26 FAIL |
| R6-V-05 (Layered Architecture) | 135 | **137.5** | C-26 PASS ("not different labels"), C-25 FAIL |

### Variation axes

| # | Axis | Criterion | Style |
|---|------|-----------|-------|
| **V-01** | Output format: structural Registry with null-gated `Selected?` column | **C-25 isolation** | Prohibition Battery base |
| **V-02** | Phrasing register: distribution-shift test named as AMEND criterion | **C-26 isolation** | Prohibition Battery base |
| **V-03** | Both axes combined | **C-25 + C-26** | Compact prohibition-battery |
| **V-04** | R6-V-04 lineage + distribution-shift added to Review B / Step 5 | **C-25 (inh) + C-26 (new)** | Schema Registry |
| **V-05** | R6-V-05 lineage + Check B prose batch upgraded to structural Registry | **C-26 (inh) + C-25 (new)** | Layered Architecture |

### Key design moves

**C-25**: The `Selected?` column is declared with an explicit **schema null condition** -- "this column cannot hold any value until all 5 rows are complete -- this is a schema constraint of the Registry, not a deferred choice." The gate is architectural, not instructional. C-23 (prose prohibition) coexists in V-01/V-03/V-05 but C-25 passes independently via the structural column.

**C-26**: Check C is renamed the **Distribution-Shift Test** with explicit language: "must surface candidate ideas that would not have appeared in the original pool -- **different ideas, not different labels on the same ideas**." Explicitly names what fails: "a directive that shifts only category names, framing emphasis, or grouping taxonomy without introducing different underlying candidates fails this test." This closes the loophole C-12 leaves open (same ideas under different framing can satisfy "noticeably different pool").

**Projected scores**: V-01 = 137.5, V-02 = 137.5, V-03 = **140**, V-04 = **140**, V-05 = **140**.
