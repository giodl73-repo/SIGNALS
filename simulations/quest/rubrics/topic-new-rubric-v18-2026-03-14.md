**v18 rubric written** to `simulations/quest/rubrics/topic-new-rubric-v18-2026-03-15.md`.

---

## Two new criteria extracted from R19 excellence signals

| ID | Sharpens | Gap closed | Source |
|----|----------|-----------|--------|
| **C-58** | C-56 | Enumeration sentence vs. instrument map — C-56 requires a flat list of IR-NN IDs in the opener; C-58 requires a structured two-column table mapping each IR-NN ID to its override instrument class (schema / gate / exit condition), so the model enters INERTIA REGISTER with both a closed list and a structural map of how each default is enforced | R19 V-04/V-05 (enumeration sentence + override table) |
| **C-59** | C-57 | Row-level exhaustiveness vs. table-level auditability declaration — C-57 requires every PCR entry to explicitly declare FER status; C-59 requires the PCR *header* to assert that FER coverage is auditable by structural inspection of the table, not by content inference — making auditability a named first-class property rather than an emergent consequence of row-level declarations | R19 V-05 (PCR header names auditability as structural property) |

**Denominator**: 49 → 51  
**Formula**: `aspirational_pass / 51 × 10`

The two criteria are structurally independent: C-58 operates at the prompt opener (before any schema), C-59 operates at the PCR header (terminal registry layer). A prompt can satisfy C-58 without C-59 (override table present, PCR header has no auditability assertion) and vice versa.
