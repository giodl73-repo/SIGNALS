`trace-contract-rubric-v8-2026-03-15.md` written.

---

**Two new criteria extracted from R7 scorecard:**

**C-31 — GATE 1 inertia anti-contamination clause uses two-clause confirmable form**
Source: V-01 R7 C-23 evidence: `"not just ordered after, but excluded entirely — [CONFIRMED / NOT CONFIRMED]"`. C-23 tests the clause exists; C-31 tests it adopts the same structural form C-14 requires for actual-output isolation — two-clause with explicit attestation slot. Mirrors the C-12 → C-14 upgrade one contamination-path rung up. Scoped to inertia-framing variations.

**C-32 — Phase 1B challenge gate is owned by a different named role than Phase 1A author**
Source: V-01 R7 C-27 evidence: `"Automate owns GATE 1B"`. C-27/C-29 test log existence and independent key; C-32 tests that role separation is structurally enforced by assignment. When Expert owns Phase 1A and Automate owns GATE 1B, the same agent cannot both build and pass the challenge gate. Without explicit role assignment, two-reader independence is operationally variable, not structurally guaranteed.

**Formula update:** `A/22 × 10` → `A/24 × 10` (C-09 through C-32 = 24 aspirational criteria).

**Distinction ladder additions:**
- `C-23 → C-31`: inertia clause exists → inertia clause uses two-clause confirmable form
- `C-27/C-29 → C-32`: challenge log + independent key → challenge gate role is distinct from Phase 1A construction role
