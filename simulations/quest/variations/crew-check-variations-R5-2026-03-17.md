**crew-check — Variate R5** written to `simulations/quest/golden/crew-check-variate-R5-2026-03-17.md`.

---

### Summary

Five complete variations holding the R4 floor (C-11 through C-18 in all), with C-19 and C-20 as the load-bearing new criteria:

| Var | Axis | C-19 | C-20 | New structural property |
|-----|------|------|------|------------------------|
| V-01 | Sub-gate precision routing | DEEP | incidental | Halt routes to minimum restart point (G4c-{role} not G4a-{role}) |
| V-02 | Audit-as-numbered-action-queue | yes | DEEP | Audit is a numbered sequential list, not a table; top-to-bottom execution |
| V-03 | Two-tier halt classification (BLOCKING vs SCOPED) | incidental | incidental | Halt scope determines presentation — row-level skips vs run-level stops |
| V-04 | Cross-referenced halt + audit | yes | yes | Halt message offers two paths (inline command + audit lookup); both lead to same command |
| V-05 | Recovery-first flow | yes | yes | RECOVERY BLOCK appears before AMEND on failed runs; three independent recovery paths |

**Key structural progressions:**
- V-01 deepens C-19 beyond R4 V-03: sub-gate precision eliminates over-restarting
- V-02 deepens C-20 beyond R4 V-02: list format makes the audit a procedure, not a reference table
- V-03 introduces a genuinely new axis (halt triage tier) not present in R1–R4
- V-04 closes the loop between C-19 and C-20 as cross-referencing complementary systems
- V-05 makes recovery output primary and review output primary in a single structural rule (recovery block present iff any halt fired)
