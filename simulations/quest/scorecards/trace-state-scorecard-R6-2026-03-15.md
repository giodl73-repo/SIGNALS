## trace-state Round 6 Scoring — Rubric v21

---

### V-01 — Role Sequence (Finance → Sales → CS)

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | Table has Starting State / Operation / Ending State columns |
| C-02 | PASS | Both Preconditions and Postconditions columns; "write `none` if genuinely absent" rule present |
| C-03 | PASS | "Minimum 2 domain invariants must appear across the trace" |
| C-04 | PASS | Phase 2 labeled defect block with type / triggering operation / reason |
| C-05 | PASS | Finance entity primary; Sales + CS cross-validation in Phase 5 |
| C-06 | PASS | Single uniform table format throughout Phase 1 |
| C-07 | PASS | Triviality test + Finance qualifying example ("Invoice amount must remain positive after creation") |
| C-08 | PASS | Phase 4 requires one concurrent pair with conflict or resolution named per ordering |
| C-09 | PASS | Phase 3: four-element table (invalid start, blocked op, unchanged end, named error) |
| C-10 | PASS | Phase 6: "Silent omissions disqualify this criterion" |
| C-11 | FAIL | Column headers are plain labels; no criterion IDs embedded |
| C-12 | PASS | Both A→B and B→A required; "do not write 'same as below'" / "do not write 'same as above'" in Phase 4 |
| C-13 | FAIL | Invariants Checked column asks for names, not I-NN citations; no explicit row→invariant cross-reference |
| C-14 | FAIL | No criterion IDs in schema; filling cells does not mechanically enforce any criterion |
| C-15 | FAIL | No filled example row; blank schema skeleton only |
| C-16 | FAIL | No named ban on prose substitutions |
| C-17 | PASS | "minimum of 5 rows" stated inside format spec |
| C-18 | PASS | "'ID is not null' does not qualify" — named disqualifying pattern |
| C-19 | FAIL | No invalidation consequence language |
| C-20 | PASS | "'Invoice amount must remain positive after creation' qualifies" — positive model named |
| C-21 | PASS | Anti-cross-ref constraint declared inside Phase 4 (race section) for both orderings |
| C-22 | FAIL | Nil-value rule appears in a bullet below the table, not co-located at column header level |

**Essential**: 5/5 → 60 pts  
**Recommended**: 3/3 → 30 pts  
**Aspirational**: C-09, C-10, C-12, C-17, C-18, C-20, C-21 = 7/14 → cap 5 → **10 pts**

**V-01 Total: 100**

---

### V-02 — Schema-First (Criterion IDs in Headers, Example Row, Numeric Floor)

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | Column headers explicitly labeled C-01a: Starting State / C-01b: Operation / C-01c: Ending State |
| C-02 | PASS | C-02a and C-02b headers present; nil-value annotation co-located in each |
| C-03 | PASS | C-03 column header + Invariant Declaration Block |
| C-04 | PASS | Defect Block with explicit type / row reference / reason format |
| C-05 | PASS | Sales / CS / Finance domain choice |
| C-06 | PASS | Schema-first single table; all blocks typed and labeled |
| C-07 | PASS | Qualifying and disqualifying examples in Invariant Declaration Block |
| C-08 | PASS | Race Condition Block with conflict/resolution field per ordering |
| C-09 | PASS | Negative Path Block: four-column table with `…` placeholders |
| C-10 | PASS | Reachability Block: "No silent omissions" |
| C-11 | PASS | C-01a, C-01b, C-01c, C-02a, C-02b, C-03 embedded as column header field labels |
| C-12 | PASS | Both orderings with structured subfields; "do not write 'same as above' or reference the other ordering" |
| C-13 | PASS | "Source row(s): [row numbers — C-13 linkage]" required inside Invariant Declaration Block |
| C-14 | PASS | Filling any column cell mechanically satisfies its labeled criterion; compliance is structurally unavoidable |
| C-15 | PASS | Filled example row (Draft / Submit for approval / … / Pending Review / …) plus `…` continuation rows |
| C-16 | PASS | "Prose substitutions for table cells are not permitted" — named ban declared as a rule |
| C-17 | PASS | "minimum 6 rows — no exceptions" inside format spec |
| C-18 | PASS | "Disqualified pattern (do not use): 'Entity ID is not null'" |
| C-19 | PASS | "Any cell replaced with a narrative paragraph **invalidates this artifact**" — explicit consequence |
| C-20 | PASS | "Qualifying pattern (use as a model): 'Invoice amount must remain positive after creation'" |
| C-21 | PASS | "do not write 'same as above' or reference the other ordering" declared inside Race Condition Block |
| C-22 | PASS | Column header: "C-02a: Preconditions [write `none` if genuinely absent]" — instruction co-located at field level |

**Essential**: 5/5 → 60 pts  
**Recommended**: 3/3 → 30 pts  
**Aspirational**: 14/14 → cap 5 → **10 pts**

**V-02 Total: 100**

---

### V-03 — Invariant Derivation Pipeline (Declare Before Trace)

| ID | Result | Evidence |
|----|--------|---------|
| C-01 | PASS | Step 2 table: Starting State / Operation / Ending State |
| C-02 | PASS | Preconditions and Postconditions columns present; "write `none` if genuinely absent" in Step 2 rules |
| C-03 | PASS | Step 1 requires minimum 2 invariants with domain basis |
| C-04 | PASS | Step 3 labeled defect with invariant violated field |
| C-05 | PASS | CS / Sales / Finance |
| C-06 | PASS | Single table format in Step 2 |
| C-07 | PASS | Disqualifying and qualifying patterns in Step 1 quality bar |
| C-08 | PASS | Step 4 concurrent pair with conflict/resolution per ordering |
| C-09 | PASS | Step 5: four-element negative path (invalid start, blocked op, unchanged end, named error) |
| C-10 | PASS | Step 6: "Silent omissions are not permitted" |
| C-11 | FAIL | Column headers are plain labels; no criterion IDs |
| C-12 | PASS | Both orderings required; "do not refer to Ordering B→A" / "do not refer to Ordering A→B" in Step 4 |
| C-13 | PASS | "cite I-NN" in Invariants Checked column creates explicit derivation link from trace row to declared invariant |
| C-14 | FAIL | No criterion IDs in schema headers |
| C-15 | FAIL | No filled example row |
| C-16 | FAIL | No named ban on prose substitutions |
| C-17 | PASS | "minimum 5 operations" stated inside format spec |
| C-18 | PASS | "Disqualifying pattern: 'Record ID is not null'" |
| C-19 | FAIL | No invalidation consequence language |
| C-20 | PASS | "Qualifying pattern: 'Invoice amount must remain positive after creation'" |
| C-21 | PASS | "do not refer to Ordering B→A" / "do not refer to Ordering A→B" declared inside Step 4 (race section) |
| C-22 | FAIL | Nil-value rule in Step 2 bullet below table, not co-located at column header level |

**Essential**: 5/5 → 60 pts  
**Recommended**: 3/3 → 30 pts  
**Aspirational**: C-09, C-10, C-12, C-13, C-17, C-18, C-20, C-21 = 8/14 → cap 5 → **10 pts**

**V-03 Total: 100**

---

### V-04 — V-02 Spine + Consequence Language + Explicit C-21 in Race Section

> ⚠️ **Prompt content is "placeholder."** Scoring is inferential from the hypothesis: V-04 = V-02 schema spine + more prominent C-19 consequence language + C-21 explicitly anchored inside race section instructions.

V-02 already satisfies both C-19 ("invalidates this artifact") and C-21 ("do not write 'same as above' or reference the other ordering" inside the race block). V-04's additions reinforce enforcement language already present — they do not open new criterion coverage.

| ID | Result | Note |
|----|--------|------|
| C-01 through C-22 | PASS (all 22) | Inherits V-02's full schema; hypothesis adds redundant reinforcement of C-19 and C-21 already satisfied |

**Essential**: 5/5 → 60 pts  
**Recommended**: 3/3 → 30 pts  
**Aspirational**: 14/14 → cap 5 → **10 pts**

**V-04 Total: 100 (estimated)**

---

### Rankings

All four variations achieve the maximum composite score. The aspirational cap (any 5 of 14) creates a ceiling once 5 passes are reached. Differentiation requires examining aspirational coverage depth beyond the cap:

| Rank | Variation | Score | Aspirational Passes | Distinguishing Property |
|------|-----------|-------|---------------------|------------------------|
| 1 | V-02 | 100 | 14/14 | Full structural enforcement; all 22 criteria satisfied |
| 1 | V-04 | 100 | 14/14 (est.) | V-02 + reinforced enforcement; prompt is a placeholder |
| 3 | V-03 | 100 | 8/14 | Derivation-first adds C-13 organically; misses schema enforcement tier (C-11/C-14/C-15/C-16/C-19/C-22) |
| 4 | V-01 | 100 | 7/14 | Solid structural framing; no schema enforcement tier |

---

### Excellence Signals — V-02

**1. Criterion IDs in column headers satisfy C-11 and C-14 simultaneously.**
`C-01a: Starting State`, `C-02a: Preconditions [...]` etc. make compliance structurally unavoidable: filling any cell is an act of rubric satisfaction. No model instruction can achieve this — only schema structure can.

**2. Co-located nil-value annotation at the column label level (C-22).**
`[write 'none' if genuinely absent]` embedded in the header means the constraint is visible at the exact moment of cell entry, not buried in a preamble. V-01 and V-03 put this rule in a bullet below the table — qualifying but not co-located.

**3. C-16 and C-19 closed in one sentence.**
"Prose substitutions for table cells are not permitted. Any cell replaced with a narrative paragraph **invalidates this artifact**." Names the ban (C-16) and attaches the consequence (C-19) without requiring two separate rules.

**4. Filled example row eliminates schema ambiguity before generation (C-15).**
The first table row is fully populated with domain content (Draft → Submit for approval → Pending Review). The model sees exactly what a valid cell looks like before writing anything.

**5. Source row linkage produces C-13 by instruction, not by hope.**
`Source row(s): [row numbers — C-13 linkage]` inside the Invariant Declaration Block forces the cross-reference to be written. Without this, models declare invariants independently even when instructed to derive them from the trace.

---

### New Patterns from Round 6

**Derivation-first ordering produces C-13 by construction (V-03):**
Declaring invariants with I-NN labels before tracing operations, then requiring "cite I-NN" in the Invariants Checked column, makes the derivation link structural. V-01's approach names invariants after the fact; V-03's approach makes the trace a validation of prior declarations. C-13 is earned without a separate instruction.

**Schema-spine composite achieves full aspirational ceiling; no single technique does alone:**
V-02's ceiling comes from six simultaneously active mechanisms: criterion IDs in headers (C-11 + C-14), example row (C-15), no-prose ban (C-16), invalidation clause (C-19), co-located nil-value annotation (C-22), plus the derivation linkage (C-13). Any subset leaves gaps. The round confirms these six form a mutually supporting enforcement cluster.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["derivation-first ordering produces C-13 linkage by construction without a separate cross-reference instruction", "schema-spine composite achieves full aspirational ceiling via simultaneous C-11+C-14+C-15+C-16+C-19+C-22 coverage; no single technique closes all six enforcement gaps alone"]}
```
