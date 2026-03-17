Here are the five R14 variations, written to `simulations/quest/rubrics/flow-trigger-rubric-v10-2026-03-15.md`.

---

**Design summary:**

| V | Axis | Primary C-27 mechanism | Key hypothesis |
|---|------|----------------------|----------------|
| V-01 | Lifecycle emphasis | Phase 4B as named gate with CHAIN-LINK-4B; Role 5 reads `R4B-REM-GATE.*` by key | Phase 4B as a distinct lifecycle step forces coverage check out of Role 4's self-attestation zone |
| V-02 | Phrasing register | Same structure as V-01 but all mandates are reasoning-forward ("this role exists because...") | Explaining WHY the gate exists reduces structural drift when the model understands the failure mode it guards against |
| V-03 | Inertia framing | "Charges Closed Review"; IF-* = formal charges; remediation = "remedy on record" | Prosecution narrative creates natural "open charge" pressure when a remedy is absent — C-27 compliance through story logic |
| V-04 | Role sequence + Lifecycle | Dedicated `Role 4B — Remediation Coverage Analyst` declared explicitly distinct from Role 4 and Role 5 at definition time | Three independent terminal artifact owners (Inertia/PCR, RCA/Phase4B, Audit/Certificate) prevent any role from self-certifying |
| V-05 | Lifecycle + Output format + Inertia | Full seven-link CHAIN-LINK chain (0→1→PCR→2→3→4→4B); Role 5 schema references `CHAIN-LINK-4B.REM_STORM` by key name | A missing CHAIN-LINK-4B creates a named reference gap in Role 5's schema — C-29 extended to the remediation dimension makes C-27 compliance detectable from the certificate structure alone |

**Key structural advance over R13:** All five variations now have Phase 4B as a named gate with its own `⛔ Gate 4B→5` condition and verbatim emission. The role independence declarations (C-28) are present in all five. The verbatim-chain read-by-key-name references (C-29) are present in all five. The first variation to achieve all three simultaneously in actual simulation should score 100/100 on v10.
