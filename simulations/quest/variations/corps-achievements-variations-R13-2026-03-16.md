Written to `simulations/quest/golden/corps-achievements-variate-R13-2026-03-16.md`.

---

## R13 — corps-achievements — 5 Variations

**Basis**: R12 V-01 (global RETRY PROTOCOL + standalone attribution gate + 9-gate structural audit). R13 targets all 7 new v12 criteria.

---

### Variation Axes

| Var | Axis | New Criteria Targeted |
|-----|------|-----------------------|
| **V-01** | C-35/C-36: Named retry step labels + row-count assertion | Rename steps to `Step 1 TRIAD` / `Step 2 DELIMIT` / `Step 3 CONTINUE`; add `"Row count = 9. All 9 enumerated."` to structural audit; absorb C-36 into `STRUCTURAL AUDIT GATE [C-26/C-27/C-34/C-36]` |
| **V-02** | C-37/C-38: Preamble OUTPUT SCHEMAS + Phase-0 attribution gate | `OUTPUT SCHEMAS` preamble block declares all 6 section schemas before any gate fires; attribution gate moves to Phase 0 — contributor list is empty before any artifact is read |
| **V-03** | C-39/C-40: Phase exit/entry contracts + universal first-person | `EXIT CONTRACT` / `ENTRY CONTRACT` objects at every phase boundary; all section headers and phase openers use "I will now..." / "I am generating..." framing |
| **V-04** | C-37/C-38 + C-41 combination: Pre-evidence commitments cluster | Combines preamble schemas + Phase-0 attribution with `HYPOTHESIS PRE-SCAN` block in preamble; insight hypothesis declared before evidence, then explicitly confirmed/revised after derivability test; absorbs C-41 into `INSIGHT GATE [C-10/C-13/C-22/C-24/C-25/C-41]` |
| **V-05** | Full combination: all 7 v12 criteria | All of the above: named step labels, row-count assertion, preamble schemas, Phase-0 attribution, exit/entry contracts, universal first-person, pre-evidence hypothesis |

---

### Key Structural Decisions

**C-35 vs R12**: R12 V-01 had `"Step 1 — Emit the named correction triad:"` (descriptive). R13 V-01+ uses `"Step 1 TRIAD:"` (shorthand label) — making the step individually addressable by name.

**C-36 gate absorption**: The row-count assertion (`Row count = 9. All 9 enumerated.`) is added as sub-condition (3) inside `STRUCTURAL AUDIT GATE`, and C-36 is absorbed into the gate's label. The structural audit's own C-27 enumeration then needs to list the updated label `[C-26/C-27/C-34/C-36]`.

**C-38 vs C-33**: C-33 required a standalone attribution gate (not a sub-step). C-38 now requires it fires *before Phase 1*. V-02+ moves it to a new Phase-0 section — no evidence exists yet, so backward inference is impossible rather than merely prohibited.

**C-41 hypothesis placement**: The `HYPOTHESIS PRE-SCAN` block is in the preamble (before any execution) rather than immediately before the insight gate — forcing the hypothesis to be declared before any evidence is available, not just before the gate fires.
