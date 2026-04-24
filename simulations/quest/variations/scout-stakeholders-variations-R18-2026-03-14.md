## Round 18 Variations — scout-stakeholders

Five complete variations written to `simulations/quest/rubrics/scout-stakeholders-rubric-v18-variate-R18-2026-03-15.md`.

---

### Variation summary

| V | Axis | New Gate Candidate | Distinct From |
|---|------|-------------------|---------------|
| V-01 | Output format — comms priority band | `FAIL_UNCALIBRATED_PRIORITY` at Step 6e-priority | C-25 (`FAIL_VAGUE_TIMING`): timing anchor absent vs. priority band uncalibrated |
| V-02 | Lifecycle emphasis — amendment verification | `FAIL_UNVERIFIED_AMENDMENT` at Step 8 | C-23 (`FAIL_OBSERVATION_ONLY`): no update applied vs. update applied but unconfirmed |
| V-03 | Inertia framing — status-quo competitor inventory | `FAIL_NO_COMPETITOR_ENTRY` at Step 2b | C-11 (`FAIL_NO_INERTIA`): no inertia vs. inertia present but competitor not inventoried |
| V-04 | V-01 + V-02 | Both above | Non-interfering: Step 6e (comms) vs. Step 8 (amendment) |
| V-05 | V-01 + V-02 + V-03 | All three | Step 0b, Step 6e, Step 8 — three independent lifecycle phases |

---

### v18 base criteria carried in all five

Every variation includes all 47 criteria (C-01 through C-47). The three v18 additions are:
- **C-45**: `Step 2a-prefill` (CRITICAL/SIGNIFICANT/MANAGEABLE) + `FAIL_UNCALIBRATED_SEVERITY` at conflict table
- **C-46**: `Step 3b-prefill` (OBSERVED/INFERRED/ASSUMED) + `FAIL_UNANNOTATED_SOURCE` at grid; ASSUMED entries mandatory Step 8 targets
- **C-47**: `Step 6d-sequence` audit table enforcing T+0 baseline on displacement-acknowledgment row

---

### New gate candidate analysis

**FAIL_UNCALIBRATED_PRIORITY** (V-01) — sixth instance of the calibration motif (prefill → constrained column → named failure). Prior instances: C-38 (veto probability), C-41 (velocity), C-44 (champion dimensions), C-45 (conflict severity). This one applies to comms scheduling precedence — orthogonal to timing anchor presence (C-25) and channel binding (C-39).

**FAIL_UNVERIFIED_AMENDMENT** (V-02) — first verification-tier gate in the amendment lifecycle. C-23 fires on absence of update; this fires on absence of confirmation. Mirrors the 3-cell completeness pattern from C-06 (Authority + Decision + Deadline).

**FAIL_NO_COMPETITOR_ENTRY** (V-03) — first gate linking Step 0b (pre-Phase 1) to Step 2b (inertia mapping). Forces the status-quo system to be a first-class named entity with calibrated adoption and switching cost bands, independently satisfiable from FAIL_NO_INERTIA.
