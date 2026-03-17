is a 4-column pipe-delimited table" with column definitions before the BAD PLAN block is reached. A model following C-51's protocol-first architecture encounters the table *specification* in the declaration section, then the table *instance* in the BAD PLAN header — dual exposure to the format. V-01 has the table but no pre-declaration of it; V-02 has the protocol-first position but a prose enumeration. Only V-05 lets the protocol frame describe the format of its own Component 1.

**Signal 2 — C-50 and C-51 are mutually reinforcing, not competing.** Placing the protocol first (C-51) creates a natural slot to declare the table format spec; having a table (C-50) gives the protocol declaration something concrete to pre-specify. The combination is tighter than either axis alone: the protocol says "Component 1 will be a 4-column table with columns X/Y/Z/W" before any construction step is read. No conflict, only compounding.

---

## Summary Table

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 through C-04 (essential) | PASS | PASS | PASS | PASS | PASS |
| C-05 through C-07 (recommended) | PASS | PASS | PASS | PASS | PASS |
| C-08 through C-49 (aspirational baseline) | PASS | PASS | PASS | PASS | PASS |
| **C-50** table index | **PASS** | FAIL | FAIL | FAIL | **PASS** |
| **C-51** protocol first | FAIL | **PASS** | FAIL | FAIL | **PASS** |
| **Composite** | **305** | **305** | **300** | **300** | **310** |
| Golden | YES | YES | YES | YES | YES |

```json
{"top_score": 310, "all_essential_pass": true, "new_patterns": ["Protocol declaration pre-specifies Component 1 table format before the BAD PLAN block — model encounters the 4-column structure in both the protocol spec and the BAD PLAN header, creating format verification before block entry", "C-50 table format and C-51 protocol-first placement are mutually reinforcing: protocol-first position creates a natural slot to declare the table column schema, converting C-50 from an implicit structural choice into an explicitly pre-declared format spec"]}
```
