All essential and target criteria (C-01–C-05, C-46, C-47, C-48, C-51) are present and intact. Here is the full simplification report:

---

## Simplification Report — flow-ratelimit V-05

### Word counts
- **Original (V-05):** 2,676 words
- **Simplified:** 2,141 words
- **Reduction:** 535 words (20.0%)

### All essential criteria: YES

---

### What was removed and why

**1. SCHEMA-A BASELINE definition verbosity (~70 words cut to ~35)**
Original repeated "forward/backward traceability anchor" three times with a reader-walkthrough explanation ("a reader locates the BURST PATH TABLE in Role 3, finds the endpoint row..."). Removed: the walkthrough prose and the redundant "This definition does not independently cite a Finding ID; it routes through the BURST PATH TABLE" sentence (kept as a single clause). Core obligation preserved: routes through BURST PATH TABLE by name and column.

**2. SCHEMA-A CELL ANCHOR rationale sentence (~25 words)**
"This prefix makes each cell independently verifiable: a reader locates BP-xx in the BURST PATH TABLE and confirms the cell's measurement without reading the Format Contract column definition." — explains the benefit, not the requirement. The requirement (prefix form + both violation classes) is retained.

**3. SCHEMA-V column definitions for BASELINE BEHAVIOR and PROTECTED BEHAVIOR (~20 words)**
Self-descriptive column headers. Only VOLUME RANGE (derived from Verdict Claim (a)) and Delta (quantified) needed glosses; the other two were redundant with the column names themselves.

**4. Registry completeness rule trailing sentence (~10 words)**
"The per-entry annotations in the body below remain required." Structural obviousness; adds no testable obligation.

**5. BURST PATH TABLE requirements consolidation (~65 words)**
Collapsed forward/backward explanation into one compact line. Removed: "A reader who sees this column name knows it feeds SCHEMA-A." and the UNRESOLVED REFERENCE example ("A cell with 'BP-05:' prefix is an UNRESOLVED REFERENCE if BP-05 does not appear in this table's BP ID column") — already fully defined in the SCHEMA-A body entry in Role 2.

**6. Role 9 Plane 1 e.1 class-description sentence (~10 words)**
"This class detects undercounting: the registry is smaller than it should be." — captured by REGISTRY GAP name and the count-comparison rule already stated.

**7. Role 9 Plane 1 e.3 explanatory footnote (~40 words)**
"REGISTRY GAP and ORPHANED SCHEMA are logically independent: REGISTRY GAP = producing role without registry entry (undercounting...); ORPHANED SCHEMA = schema body entry without registry entry (misalignment...)." — description of the logic already stated in e.1 and e.3 individually. Kept only the actual obligation: "Both classes must appear under separate named labels in the findings output."

**8. Role 9 Plane 2 e.4 parentheticals (~20 words)**
"(the definition is independently anchored, satisfying C-41 but not C-45)" and "(C-41 satisfied; BURST PATH TABLE routing not satisfied)" — backward references to prior criteria for explanation only. Violation class names and detection rules retained.

**9. Role 9 Plane 3 e.5–e.6 structural redundancy (~30 words)**
Removed "This is scan-time detectable." (already noted in violation class name and format), "If cell opens with 'BP-xx:' prefix: proceed to e.6 for this cell." (structural branching prose), and "If exists: prefix is resolved — no violation." (obvious negative branch).

**10. Micro-trims across gates and intros (~45 words total)**
Role 2 header (condensed), Gate 2→3 (condensed: "All schema body entries declared with per-entry annotations" → "All schema body entries present"), Gate 3→4 backward traceability confirmation (already stated in BURST PATH TABLE requirements), Role 7 cell anchor intro (13-word reduction), CHECK (e) intro sentence, Plane 2 e.4 intro clause.

---

### Criteria verification

| Criterion | Preserved? | Evidence |
|-----------|------------|----------|
| C-01 (tier distinction) | YES | Role 4: ≥3 structurally distinct tiers with scope |
| C-02 (no single-category) | YES | Role 4 scope-distinction check item 5 |
| C-03 (UX per tier) | YES | Role 5 SCHEMA-B, FIELD-B |
| C-04 (burst path) | YES | Role 3 STRUCTURAL/INCIDENTAL classification |
| C-05 (retry handling) | YES | Role 8c RH-xx finding IDs |
| C-06 (cascade scenario) | YES | Role 8a causal chain prose |
| C-07 (numeric specificity) | YES | Role 4 + Verdict Claim (a) |
| C-08 (volume mapping) | YES | Role 6 SCHEMA-V |
| C-46 (merge prohibition) | YES | Plane 3: named "missing or invalid prefix" prohibition |
| C-47 (orphaned schema) | YES | Plane 1 e.3: ORPHANED SCHEMA, separate labels |
| C-48 (named rejection clause) | YES | SCHEMA-A BASELINE SOURCE VIOLATION in Format Contract |
| C-51 (cell-plane FC clauses) | YES | SCHEMA-A CELL ANCHOR VIOLATION + UNRESOLVED REFERENCE VIOLATION as rejection clauses |

```json
{"simplified_word_count": 2141, "original_word_count": 2676, "all_essential_still_pass": true}
```
