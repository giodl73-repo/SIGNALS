Here are the 5 R6 variations:

---

## Round 6 Variations — flow-trigger

**File**: `simulations/quest/golden/flow-trigger-variate-R6-2026-03-16.md`

### Variation Summary

| Variation | Axis | New Mechanism | Predicted Criterion |
|-----------|------|---------------|---------------------|
| **V-01** | Lifecycle emphasis | **Execution Position Citation** — every firing entry carries a `Positioned because: EOR-{NN}` slot grounding its sequence position in a named platform rule | C-17: per-entry execution order citation, making ordering auditable at row level without platform expertise |
| **V-02** | Output format | **Cascade Depth Register** — pre-declared `MAX DEPTH N` before enumeration; cascade entries carry `[Depth: N/MAX]` counters; chains that exhaust the budget produce `[DEPTH EXCEEDED]` flags instead of silent additions | C-18: cascade depth budget + per-entry depth counter, converting storm detection from subjective count to numeric gate |
| **V-03** | Role sequence | **Exclusion Witness Role** — dedicated Role B sweeps all automation layers and logs every out-of-scope layer with an explicit exclusion reason, *before* the candidate scan; Role D uses the exclusion log in missing-trigger verdicts | C-19: formal exclusion log completing three-part accounting: (a) excluded layers, (b) in-scope non-firers, (c) firers |
| **V-04** | Phrasing register | **Formal Prescriptive Register Throughout** — all obligation positions use SHALL/MUST/PROHIBITED; all gate statements use the same obligation register as job descriptions; descriptive drift produces `[REG FAIL: {clause}]` inline | C-20: gate statement register must match job description register; register inconsistency is a named, taggable violation |
| **V-05** | Combined | **All three new mechanisms + R5 V-05 foundation** — five independent structural barriers: event tuple gate, authority contracts, per-entry EOR citation, cascade depth budget, exclusion log | Tests whether all three new mechanisms survive combination without interference |

### What Makes Each Mechanism New vs. R5

- **V-01 vs. C-14**: C-14 closes scope *before* candidates are named. V-01 closes the *ordering justification* per entry — each position is grounded in a rule, not just the global order declared once.
- **V-02 vs. C-10**: C-10 requires cascade rows to appear in the firing sequence. V-02 bounds *how far* that sequence can grow before it becomes pathological, making depth budget exhaustion a structural signal.
- **V-03 vs. C-11**: C-11 declares the denominator of *in-scope* candidates. V-03 accounts for what was inspected and *excluded*, completing the space: in-scope + excluded = all layers checked.
- **V-04 vs. C-05**: C-05 requires platform grounding. V-04 requires the protocol's own obligation language to be formally stated, so gate conditions can be mechanically audited without reviewer judgment.
