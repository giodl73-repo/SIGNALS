Here is the complete Round 18 variate, saved to `simulations/quest/golden/flow-throttle-variate-R18-2026-03-16.md`.

---

## Summary

**State analysis:**

| Variant | C-45 | C-46 | C-47 | C-48 | Score under v18 |
|---------|------|------|------|------|----------------|
| R17 V-01 | FAIL | FAIL | FAIL | FAIL | 270/290 |
| R17 V-02 | PASS | FAIL | PASS | FAIL | 280/290 |
| R17 V-03 | FAIL | FAIL | FAIL | FAIL | 270/290 |
| R17 V-04 | FAIL | FAIL | FAIL | FAIL | 270/290 |
| R17 V-05 | PASS | PASS | FAIL | PASS | 285/290 |

No R17 variant carries all four simultaneously. R18 must fix that.

---

**Five variations, all targeting 290/290:**

**V-01 — Output format (single):** Table-first throughout. The role activation chain (C-46) is a typed 4-role table at the header. The signal distinction register (C-45) is a 5-column table with "Does NOT confirm" as an explicit column header. The bypass rejection (C-47) is a 3-column register immediately adjacent. The BYPASS GATE CONDITION field (C-48) sits between the register and the count table, structurally blocking the table until filled.

**V-02 — Role sequence (single):** Dedicated Role 1.5 architecture. C-46 shows SIG-01/SIG-02 as separate Handoff cells in the header chain table. C-45 adds the "Does NOT confirm" column to Role 1.5's signal distinction table with the non-conflation statement referencing the column by name. C-47 is a standalone bypass-attempt rejection register (3 columns) in Role 1.5. C-48 is the INERTIA-FRAME REJECTION FIELD immediately above the verification table.

**V-03 — Lifecycle emphasis (single):** Every structural requirement is a named lifecycle phase. C-46 is a "lifecycle stage overview" table at the header with SIG-01 and SIG-02 in separate Phase rows. C-45 is the Phase 0.5 signal specification table. C-47 is the Phase 0.5 bypass defeat record (Attempt / Stage type / Gate reason). C-48 is the PHASE GATE FIELD — a required gate slot in the lifecycle sequence that must clear before Phase 1 (count check) opens.

**V-04 — Phrasing register + inertia framing (combined):** Maximum SHALL enforcement. C-46's table uses "SHALL NOT activate if" as a column. C-45's column is "DOES NOT CONFIRM" in caps; the non-conflation statement calls it "the authoritative statement of this limit." C-47 is the PROHIBITED FRAMING REGISTER with a "SHALL NOT proceed because" column. C-48 is the MANDATORY BYPASS DECLARATION, framed as an activation prerequisite with a SHALL FILL instruction.

**V-05 — Role sequence + output format + inertia framing (combined):** Full combination and strongest form. C-46 uses a "Signal chain" column in the header chain table where SIG-01 and SIG-02 are distinct cells in the same column — scannable top-down. C-45 in Role 1.5 has the "Does NOT confirm" column whose cell value is quoted verbatim in the non-conflation statement. C-47 is the named BYPASS DEFEAT REGISTER with 3 auditable columns. C-48 is the BYPASS REJECTION FIELD with explicit framing ("structurally unavailable until this field is filled") and the two-option form requiring active disambiguation.
