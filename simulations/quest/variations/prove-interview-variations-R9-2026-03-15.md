The R9 variations are written. Here's a summary of what was generated and the structural reasoning:

---

## prove-interview — R9 Variations Summary

**File**: `simulations/quest/golden/prove-interview-variate-R9-2026-03-15.md`

### New v9 Territory (C-31 + C-32)

| New Criterion | What It Requires | R8 Gap Being Closed |
|---|---|---|
| **C-31** | PRE-INTERVIEW MASTER GATE names 4 items: Subject Cards, Register, Vocab Signatures, Decision Taxonomy | R8 V-01/V-04 had 3-item gate (C-22/C-13/C-28); "Subject Cards complete" was never explicitly named |
| **C-32** | Phase gates as consolidated named blocks: `PHASE N GATE: [ ] item...` | R8 V-02 had only inline checkboxes (C-20 PARTIAL); R8 V-03 had "do three things" instruction language |

### Variation Design

| Variation | Axis | Key Move vs R8 | C-31/C-32 Prediction |
|---|---|---|---|
| **V-01** | Lifecycle emphasis | Minimal delta: adds "Subject Cards complete" as explicit item 1 in Step 0D; renames it PRE-INTERVIEW MASTER GATE | Both PASS |
| **V-02** | Output format | Fixes R8's C-30 FAIL and C-20 PARTIAL: adds explicit prerequisite confirmations + SECTION N GATE named blocks + PRE-INTERVIEW MASTER GATE as named schema element | Both PASS |
| **V-03** | Phrasing register | Adds BEFORE-INTERVIEW CHECKLIST (4 named items) and INTERVIEW N COMPLETE named accountability blocks in friendly language; fixes C-19/C-22/C-30 PARTIAL/FAIL from R8 | C-31 PASS; C-32 PASS if named blocks count |
| **V-04** | Role sequence + inertia | Builds on R8 100/100 baseline; adds "Subject Cards complete" as explicit item 1; Inertia Stance field adds 7th Subject Card field | Both PASS |
| **V-05** | Format + lifecycle | Extends R8 100/100 baseline: Section 0-D table grows to 4 rows; renamed PRE-INTERVIEW MASTER GATE; all phase gates use PHASE N GATE: [...] blocks | Both PASS |

The discriminating variable for v9 will likely be **V-03**: whether conversational named blocks (`BEFORE-INTERVIEW CHECKLIST`, `INTERVIEW N COMPLETE`) satisfy C-32's "consolidated named block" requirement, or whether they score PARTIAL because they use friendly language without the `PHASE N GATE:` exact format.
