The file is written. Here's a summary of the 5 variations:

---

## R18 Variations — quest-rubric (v18 rubric, targeting C-47/C-48)

**File:** `simulations/quest/golden/quest-rubric-variate-v18-R18-2026-03-16.md`

---

### Variation Map

| V | Axis | C-47 probe | C-48 probe | Prediction |
|---|------|-----------|-----------|-----------|
| V-01 | Role sequence | Phase 8.5 failure-mode clauses name criterion IDs ("Absent path 1, **C-43** is unenforced at Phase 8.5 entry") | Ablated — foil items cite failing criterion only | PASS C-47, FAIL C-48 |
| V-02 | Output format | Ablated — prose failure-mode only | STATUS QUO foil items pair passing + failing ("**passes C-01 through C-04 while failing C-05**") | FAIL C-47, PASS C-48 |
| V-03 | Lifecycle emphasis | PER-NOTE FORMAT TEMPLATE with mandatory `[C-NN]` slot — structural production gate, not prose instruction | Ablated | PASS C-47 (stronger form than V-01) |
| V-04 | Combined | V-01 mechanism preserved | V-02 mechanism preserved | PASS C-47 + C-48 jointly |
| V-05 | Phrasing register | V-04 + purpose declaration: *"converting the failure-mode argument to a criterion-indexed compliance claim verifiable by ID lookup"* | V-04 + purpose declaration: *"locating the STATUS QUO within the criterion lattice at paired-criterion resolution"* | PASS C-47 + C-48 at highest expression density |

---

**Key design decisions:**

- **Single-axis isolation first**: V-01 and V-02 are ablation controls for each other. V-01 confirms C-47 is independently satisfiable without C-48. V-02 confirms C-48 is independently satisfiable without C-47.

- **V-03 tests scaffolding vs instruction**: The PER-NOTE FORMAT TEMPLATE in V-03 forces `[C-NN]` to be a structural slot rather than a prose instruction. If V-03 produces higher C-47 pass rates than V-01, template scaffolding is load-bearing beyond prose.

- **V-04 tests joint satisfiability**: The two mechanisms govern structurally distinct sections (Phase 8.5 vs STATUS QUO COMPETITOR), so interference is not expected — but must be confirmed.

- **V-05 tests purpose-clause value**: Adds "locating the STATUS QUO within the criterion lattice at paired-criterion resolution" to each foil item and "criterion-indexed compliance claim verifiable by ID lookup" to each failure-mode clause. If V-05 scores above V-04, purpose framing is additive.
