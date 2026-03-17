Saved to `simulations/quest/golden/campaign-specify-variate-R7-2026-03-16.md`.

---

# Variations — campaign-specify / Round 7

## R6 gap diagnosis

R6 V-05 (20/23 = 98.7) is the base. Under v7 scoring it earns C-30 and C-31 but not C-28 or C-29. Two gaps:

| Gap | Root cause | Fix |
|-----|-----------|-----|
| **C-28** missing | V-05 gate Step 3 labels audience checks as `Exec check / Dev check / Maker check` — C-28 requires `Exec gate / Dev gate / Maker gate` with explicit parenthetical Pass/Fail descriptions | Add "gate" label + `Pass (opening names...) / Fail (opens with...)` per audience |
| **C-29** missing | V-05 gate says "exec contract's frame" — C-29 requires the gate criteria to derive from "the Step 0c exec voice contract" by name, and the rewrite anchor to name "the Step 0c contract for that audience" | Add "Step 0c" qualifier to contract references in Step 3 criteria + Step 4 anchor |

C-27 (COMPLETION INDEX voice audit row) may already be earned by R6 V-05 — the scoring table shows V-04 earning it but V-05 has the same line. V-03 tests whether **formal section classification** (`### Voice Compliance Audit` header) resolves any ambiguity.

## Variations

| ID | Axis | Key Change from R6 V-05 | Targets | Predicted |
|----|------|------------------------|---------|-----------|
| **V-01** | C-28 gate formalism | `Exec gate / Dev gate / Maker gate` + parenthetical `Pass (...) / Fail (...)` per audience | C-28 | 21/23 |
| **V-02** | C-29 Step 0c naming | Gate criteria name "the Step 0c exec/dev/maker voice contract"; Step 4 rewrite anchor names "the Step 0c voice contract for that audience" | C-29 | 21/23 |
| **V-03** | C-27 formal section | COMPLETION INDEX restructured into 4 named `###` sections; "Voice Compliance Audit" section header | C-27 | 21/23 |
| **V-04** | C-28 + C-29 combined | Both gate formalism and Step 0c naming; the critical sentence: "Does the Exec Version opening match the frame of the **Step 0c exec voice contract** (outcomes/risk register)? **Pass** (opening names a business cost...) / **Fail** (opens with...)" | C-28 + C-29 | **23/23** |
| **V-05** | Full synthesis | V-04 + formal COMPLETION INDEX section headers from V-03 | All 5 | **23/23** |

**Key R7 structural insight**: The three criteria C-28, C-29, and C-31 converge on a single sentence in gate Step 3. That one sentence must simultaneously carry the gate label (C-28), the Step 0c contract name (C-29), and serve as enforcement criterion (C-31). V-04 achieves this. V-05 adds the formal section header for C-27 robustness.
