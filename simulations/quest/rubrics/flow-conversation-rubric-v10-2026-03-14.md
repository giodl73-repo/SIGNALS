Done. Here's a summary of what changed in v10:

---

**8 new aspirational criteria, C-30 through C-37 (+20 pts). Max score: 136 → 156.**

| ID | What it captures | Wt | Source variation |
|----|------------------|----|-----------------|
| C-30 | Mutation-first authoring — Phase 1-S before SESSION_STATE; state derived from replay, making TIMELINE_STATE_MISMATCH structurally impossible | 4 | V-01, V-04 PASS+ |
| C-31 | AUTHORIZED_REWRITERS in timeline contract — prevents false OFF_CONTRACT_WRITE on legitimate multi-topic re-writes | 2 | V-04 PASS+ |
| C-32 | CONTRACT AUDITOR Phase 0-CA-1 gate — VARS_IN_TOPOLOGY vs VARS_IN_CONTRACT delta blocks Phase 1 if incomplete | 3 | V-04 |
| C-33 | Phase 6-A CONTRACT_AUDIT_GATE_HONORED — closes the pre-execution gate loop at Auditor layer | 2 | V-04 |
| C-34 | COVERAGE_QUALITY_GATE CLEAN\|DEGRADED — PROVISIONAL ratios when anomaly rate > 0, prevents coverage-washing | 3 | V-03 PASS+ |
| C-35 | SIMULATION_DELTA / STATUS_QUO_GAP — adoption-justification layer with Auditor SIMULATION_DELTA_COMPLETE gate | 2 | V-02 |
| C-36 | CONSTRAINT_VERDICTS per turn — named CONV-NN IDs per turn, additive to CONFORMANCE column | 2 | V-05 |
| C-37 | CONV_NN arithmetic evidence — PRE+MUTATION=POST makes mutation correctness verifiable by inspection | 2 | V-05 |

The C-30/C-31/C-32/C-33 cluster forms a complete contract enforcement stack: declare rewriters (C-31) → pre-execution audit (C-32) → mutation-first ordering (C-30) → post-execution gate verification (C-33). The C-36/C-37 cluster upgrades conformance from binary verdicts to named, arithmetically-verified constraint proofs.
