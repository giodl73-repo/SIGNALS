Written to `simulations/quest/golden/flow-resilience-variate-R11-2026-03-15.md`.

---

## Round 11 Variations — Summary

**R11 target**: Crack C-09 (chaos engineering) and C-10 (observability hooks) — both persistently uncracked through R10. V-05 ceiling entering R11 was 50/54.

| Variation | Axis | C-09 mechanism | C-10 mechanism | Predicted uncapped |
|---|---|---|---|---|
| **V-01** | Output format | Gate 2b: 3-column chaos table; each row cites Gate 2 Trigger Condition as activation threshold | — | 52/54 |
| **V-02** | Lifecycle emphasis | — | Observable Signal column in each OEG/DCV/MRF table; unobservable gaps emit MRF-OBS-NN | 52/54 |
| **V-03** | Phrasing register | Gate 2b (conversational "Step 3") | Step 4 Observable Signal column (conversational) | 52/54 |
| **V-04** | Role seq + lifecycle | Gate 6 (Act 3 SRE Expert); RULE-CHAOS-INJECT registered | Gate 7 (Act 3 SRE Expert); RULE-OBS-GAP registered; Operational Readiness Declaration | 54/54 |
| **V-05** | Full integration | Gate 2b + RULE-CHAOS-INJECT in Act 1 registry | Gate 3 Observable Signal + Detection Horizon + RULE-OBS-GAP + MRF-OBS-NN + Chaos-Observability Coverage Matrix | 54/54 |

**New excellence signals to watch** (potential C-36+):
- **E-22** (V-01, V-05): Chaos test activation threshold linked to Gate 2 Trigger Condition threshold expression — chaos and monitoring share the same boundary
- **E-23** (V-02, V-03, V-05): MRF-OBS-NN: observability absence is itself a named missing recovery flow, not a silent omission
- **E-24** (V-05): Chaos-Observability Coverage Matrix — joint falsifiability view across scenarios and gap findings in a single scannable table
- **E-25** (V-05): Detection Horizon per Observable Signal — makes observability SLA comparable to recovery SLA targets
- **E-26** (V-04): Operational Readiness Declaration pre-Gate 6 — commits to chaos and observability coverage minimums before analysis begins, parallel to Act 1's Coverage Accountability Roster
