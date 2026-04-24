Written to `simulations/quest/golden/crew-roles-variate-R14-2026-03-17.md`.

---

## crew-roles -- Variate R14 summary

**Baseline**: R13 V-05 (7 phases; CONVERGENCE SUMMARY; CHECK 3B scope binding; CHECK 6 with 5 failure modes). C-28 and C-29 are now formalized in v8 -- all R14 variations include them as baseline.

**Gaps in R13 V-05 targeted by R14**:
- **Gap-1**: No CHECK validates simplify items are imperatives (C-06)
- **Gap-2**: No planning-phase vocab assignment per role -- CHECK 4 only audits post-write (C-11)
- **Gap-3**: No inertia-first write ordering -- scope gradient pressure could silently re-scope inertia during writing

---

### Variations

| # | Axis | Key change | Hypothesis |
|---|------|-----------|------------|
| **V-01** | Role sequence | Inertia-advocate written first; `INERTIA-ADVOCATE WRITTEN` confirmation gate before Step 3 | Locking the most-constrained role first prevents scope drift in non-inertia roles from creating back-pressure on inertia's cross-team scope |
| **V-02** | Output format | Phase 5 gains `Planned-Vocab-Term` column; Phase 7 CHECK 4 splits into 4A (coverage) + 4B (row-by-row vocab binding, flags `VOCAB BINDING MISMATCH`) | Closes the C-11 planning-to-execution gap exactly as CHECK 3B closed the C-09 gap |
| **V-03** | Lifecycle emphasis | Inline `LENS AUDIT` block per role in Phase 6: checks `?` terminator on verify items and imperative-verb start on simplify items before moving to next role | Catches C-06 violations per-role during writing rather than deferring to Phase 7 (which has no such check) |
| **V-04** | Role sequence + Output format | V-01 + V-02: inertia-first + `Planned-Vocab-Term` + CHECK 4B binding | Non-overlapping axes -- sequencing and planning-table format target different surfaces |
| **V-05** | Output format + Lifecycle emphasis | V-02 + V-03 consolidated: Phase 6 `ROLE AUDIT` block checks lens format, vocab binding, and scope binding per role in a single inline gate; Phase 7 re-runs CHECK 3B and CHECK 4B as terminal confirmation | Two per-role quality gates consolidated into one `ROLE AUDIT` block; inline + terminal dual enforcement |
