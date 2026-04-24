**flow-trigger-rubric-v14** written to `simulations/quest/rubrics/flow-trigger-rubric-v14-2026-03-16.md`.

---

**One new aspirational criterion (C-41), N_aspirational: 32 → 33, max (raw): 145.0 → 147.5:**

| ID | Source | What it captures | Extends |
|----|--------|-----------------|---------|
| C-41 | V-05 combined-axis signal — the NOTE block inside the CLOSURE CHECK uses the same assertion register (`PROPERTY: VALUE [must be VALUE]`) as the surrounding counters, making it a detection-record peer rather than an appended annotation | Register-uniform embedded structural sub-blocks: the C-40 NOTE block adopts assertion-register framing consistent with the surrounding CLOSURE CHECK counter assertions, eliminating the annotation/obligation register boundary that C-40's physical inseparability was designed to close | C-40 (same container requirement — C-41 is the same-register requirement), C-29 (same C-26→C-29 progression logic: C-40 ensures physical inseparability; C-41 ensures functional co-domain — the rationale and counters belong to the same assertion domain, not different linguistic registers) |

**Structural relationship:** C-40 is the "physical inseparability" criterion — removal requires editing the code fence. C-41 is the "functional inseparability" criterion — the NOTE block operates in the same assertion domain as the counters, so a reader scanning the CLOSURE CHECK cannot distinguish the rationale from the enforcement content by register alone. V-05's NOTE block demonstrated both simultaneously; the scorecard's "combined axis" signal (phrasing register + inseparability) explicitly identified the pairing as non-trivial and as the mechanism that makes the NOTE block read as "part of the detection record rather than as an appended annotation."

**Retroactive R16 scoring adjustment under v14:**

| Variation | C-41 Verdict | Reason |
|-----------|-------------|--------|
| V-01 | FAIL (vacuous path) | No embedded NOTE block (C-40 FAIL) |
| V-02 | FAIL (vacuous path) | No named note block (C-40 PARTIAL) |
| V-03 | FAIL (vacuous path) | No embedded NOTE block (C-40 FAIL) |
| V-04 | FAIL (vacuous path) | INERTIA CONTRAST path — no NOTE inside CLOSURE CHECK (C-40 PARTIAL) |
| V-05 | **PASS** | NOTE block uses assertion-register declarations co-equal with surrounding counters |
