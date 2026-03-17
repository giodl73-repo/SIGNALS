Written to `simulations/quest/golden/flow-conversation-variate-R8-2026-03-15.md`.

---

**Round 8 summary:**

| Variation | New Mechanism | C-20+ Candidate | Predicted (v7) |
|-----------|---------------|-----------------|----------------|
| V-01 | Phase 6 REMEDIATION_VERIFICATION_CYCLE | `remediation_verification_cycle` | 150/150 |
| V-02 | DEFECT_SEVERITY formula + SEVERITY_GATE | `formula_based_defect_severity` | 150/150 |
| V-03 | Phase 3.5 CONCURRENT_SESSION_TRACE | `concurrent_session_interference` | 150/150 |
| V-04 | V-01 + V-02 combined | two candidates | 150/150 |
| V-05 | All three new + all R7 | three candidates | 150/150 |

**Three new mechanisms, each independently non-redundant with C-01 through C-19:**

- **C-20 candidate** — `remediation_verification_cycle`: C-09 names what to fix; Phase 6 re-simulates after the fix. A prompt passing C-09 and C-17 can still terminate at "apply this change" with no re-trace.
- **C-21 candidate** — `formula_based_defect_severity`: C-18 measures how much of the graph was traced; C-21 measures how dangerous each found defect is. No intersection.
- **C-22 candidate** — `concurrent_session_interference`: C-02's four-type taxonomy has no concurrency class; C-05 tracks one user; C-06 is sequential paths, not simultaneous sessions.

V-05 is the evidence pool for v8 rubric generation. All three tokens (`REMEDIATION_CYCLE_COMPLETE`, `SEVERITY_GATE`, `SESSION_ISOLATION_VERDICT`) are present and independently attributable.
