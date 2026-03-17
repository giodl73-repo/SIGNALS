`topic-status-rubric-v18-2026-03-15.md` written. Summary of what was added:

---

## v18 changes — Structural Tier 17 (+10 pts, max 300 → 310)

| ID | Name | Points | Prerequisite |
|----|------|--------|--------------|
| C-50 | Phase-labeled STOP predicates | 5 | C-49 (conditional), C-47 (hard) |
| C-51 | Preamble adversary entry defeat forecast sub-components | 5 | C-47 (hard) |

**C-50** extends the adversary-defeat predicates at the STOP gate from positional form `(N)` to phase-labeled form `[PN-ADVERSARY DEFEAT:]`, closing the three-site label isomorphism: preamble labels (C-47) → execution-body adversary blocks (C-42/C-43/C-48) → STOP gate phase labels (C-50). Inherits C-49's vacuous-PASS behavior when C-48 is absent.

**C-51** extends each labeled `PN-ADVERSARY:` preamble entry from two-part form (adversary + consequence-of-skipping) to three-part form by adding a nested `DEFEAT CONDITION:` sub-component — a condensed forecast of the observable defeat property declared at execution sites by C-46/C-48. Per-entry completeness required: with C-48 present, all three entries must carry `DEFEAT CONDITION:`; partial satisfaction (V-05: P1 absent) = FAIL.

**Projected R20 scores under v18:**

| Variant | C-50 | C-51 | v18 Score |
|---------|------|------|-----------|
| V-01 | PASS | PASS | **310** |
| V-02 | FAIL | PASS | **305** |
| V-03 | PASS | FAIL | **305** |
| V-04 | FAIL | FAIL | **300** |
| V-05 | PASS | FAIL | **305** |
