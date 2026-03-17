Written to `simulations/quest/golden/corps-scan-variate-R13-2026-03-17.md`.

---

## Variate R13 — corps-scan

**R12 criteria are now invariants.** All five variations satisfy C-45 (typed hypothesis fields), C-46 (typed composite Penalty column), C-47 (independently verifiable Net Score delta), and C-48 (organizational cost dimension). The variation axes govern HOW, not whether.

### Variation Axes

| V | Axis | Key mechanism |
|---|------|---------------|
| V-01 | **Magnitude derivation protocol** | 5-level Severity Scale at DARK SIGNALS header; each entry carries `Severity: [0-4]` with derivation note; Penalty column sources magnitude directly from those fields — closes the C-46 traceability gap |
| V-02 | **Selection Audit phase** (ROLE 3.5) | Dedicated sub-phase between DELIBERATE and DRAFT+FINALIZE; reproduces winner + runner-up rows verbatim with line-by-line arithmetic trace; AMEND-A's C-47 verifiability claim cites this section by name rather than asserting it inline |
| V-03 | **Pipeline Debt as cost dimension** | C-48 satisfied by `Pipeline Debt [stages:string]` instead of Inertia Cost; each mode row names concrete corps-* stages disrupted if mode is selected and later changed — operationally specific, not abstract |
| V-04 | **Magnitude + Selection Audit** | V-01 + V-02: Severity fields feed Penalty column; Selection Audit reproduces those values with arithmetic trace; AMEND-A cites audit section AND Severity traceability — end-to-end audit chain |
| V-05 | **Full combination** | V-01 + V-02 + V-03: 7-column deliberation table (Evidence For / Penalty [label:magnitude] / Pipeline Debt [stages] / Base / Penalty / Net / Verdict); Selection Audit with Severity trace; AMEND-A carries all four invariant signals |

### Architecture note on the axes

V-01 and V-02 address the same criterion (C-47) from opposite directions: V-01 closes the upstream end (magnitude derivation is auditable at entry level), V-02 closes the downstream end (verification artifact exists for the AMEND-A claim). V-03 is fully orthogonal — it extends C-48 from abstract organizational cost to operationally named pipeline stages. The combination variations test that these axes compose cleanly without structural interference.
