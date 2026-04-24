Written to `simulations/quest/rubrics/trace-permissions-rubric-v7-2026-03-16.md`.

---

## Summary of v7 changes

**Four new aspirational criteria** extracted from Round 6 PARTIAL patterns and the v6 frontier projection. Aspirational tier grows from N=17 to N=21 (weight per criterion ~0.476).

| ID | Name | Source |
|----|------|--------|
| C-25 | Closing Mechanism column content exclusivity | C-21 PARTIAL — V-01 and V-03 had the column but permissive instructions allowed mixed content |
| C-26 | Universal three-field no-finding format at all required sites | C-23 PARTIAL — all three variants had partial-site or two-of-three-field coverage |
| C-27 | Explicit anti-back-reference prohibition in roll-up field definition | C-24 PARTIAL — all three variants: "list" framing compatible with "see table above" |
| C-28 | Composite verdict names mechanism type per vector, not counts | v6 frontier projection — splits V-04 (restated-mechanism list) from V-05 (count-based) |

**Discriminating logic:**
- C-25 separates columns with permissive instructions from columns with strict exclusivity rules — satisfying C-21 no longer implies satisfying C-25
- C-26 separates selective three-field coverage from universal three-field coverage across all five enumerated site types
- C-27 separates instructions that imply inline restatement from instructions that explicitly prohibit back-references — the constraint is at the instruction level, not just the output level
- C-28 separates composite verdicts that count from composite verdicts that name mechanism types inline — auditing the verdict requires no further table lookup

**Suggested v8 criterion:** verdict-level mechanism cross-audit — the closing mechanism cell and the pre-declaration assumption for the same vector explicitly confirm they name the same structural fact, separating accidental alignment from verified alignment.
