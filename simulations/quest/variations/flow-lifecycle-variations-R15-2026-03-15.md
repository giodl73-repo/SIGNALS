File written at `simulations/quest/golden/flow-lifecycle-variate-R15-2026-03-16.md` (1578 lines).

---

## flow-lifecycle Round 15 — 5 Variations

### New criteria probed (rubric v15)

| ID | Criterion | What R14 had | What v15 requires |
|----|-----------|-------------|------------------|
| **C-48** | Per-field anti-pattern vocabulary in SQ Declaration | FM-IDs assigned, field definitions present | Every field row carries inline "does not count" / "Mandatory" / "is a fail" token specific to that field |
| **C-49** | Mutual-audit relationship named as design principle | "these two columns audit each other" (structural observation) | Column header uses "mutual-audit design principle" or equivalent — naming the co-auditing behavior as intentional architecture |

---

### Hypothesis matrix

| Variation | Axis | C-48 | C-49 | Primary probe |
|-----------|------|:----:|:----:|---------------|
| **V-01** | Inertia Framing | TARGET | HOLD | Per-field anti-pattern tokens in every SQ Declaration field definition — practitioner filling a single row encounters the constraint inline |
| **V-02** | Output Format | HOLD (partial) | TARGET | Status-Quo Gap column header names the mutual-audit relationship explicitly as a design principle, not just a structural observation |
| **V-03** | Phrasing Register | FAIL | PARTIAL | Imperative prose instructions — effective for procedural criteria but cannot satisfy C-48/C-49's point-of-use placement requirements |
| **V-04** | Role Sequence + Lifecycle Emphasis | PARTIAL | PARTIAL | Pre-registry survey + phase-layer framing — strong on C-05/C-16 clusters but shows asymmetric C-48 (Inertia Driver field gap) and C-49 (caption vs. header placement) |
| **V-05** | Inertia Framing + Output Format | TARGET | TARGET | Full R15 floor: bidirectional integrity — SQ Declaration fields self-enforce at authorship (C-48), Phase Index header declares mutual-audit design intent (C-49) |

### Key structural additions in V-01 and V-05
- **AC-23** (Group A): Every SQ Declaration field row verified individually for inline anti-pattern token — bulk attestation is a fail
- **D-14**: Per-field anti-pattern gap (FM-IDs present, enforcement vocabulary absent from field definition)

### Key structural addition in V-02 and V-05
- **AC-24** (Group B): Status-Quo Gap column header verified for "mutual-audit design principle" or equivalent named-principle language — description without designation does not pass
- **D-15**: Unnamed mutual-audit design principle (relationship described but not designated as design intent)

### Expected scores against v15 rubric (denominator 49)

| Variation | Predicted score | Path |
|-----------|:--------------:|------|
| V-01 | 48.0 → 98 | C-49 held at R14 floor (no design-principle designation) |
| V-02 | 48.5 → 99 | C-48 partial (Inertia Driver field gap) |
| V-03 | 46.5 → 95 | C-48 fail (prose only), C-49 partial (caption not header) |
| V-04 | 47.0 → 96 | C-48 partial, C-49 partial |
| V-05 | 48.5 → 99 | Both C-48 and C-49 at full strength |
