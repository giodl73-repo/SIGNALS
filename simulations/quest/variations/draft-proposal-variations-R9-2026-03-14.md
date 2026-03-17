`draft-proposal-rubric-v9-variations-R9-2026-03-15.md` written.

---

## Round 9 Variation Design Summary

| Var | Single/Combo | Axis | Primary Criteria | Predicted Score |
|-----|-------------|------|-----------------|----------------|
| V-01 | Single | Option anatomy field-level role enforcement | C-32 | ~96.2 |
| V-02 | Single | Phase 0 causal contract declaration | C-33 | ~96.2 |
| V-03 | Single | Phrasing register (strict imperative) | C-32 + C-33 incidentally | ~100.0 |
| V-04 | Combo | C-32 + C-33 | C-32 + C-33 | ~100.0 |
| V-05 | Combo (all six) | PM-first + tables + manifest + DLT + anatomy + causal | C-28 through C-33 | 100.0 |

**Key structural moves per variation:**

**V-01** — Adds a `OPTION ANATOMY CONTRACT` block to Phase 0 that declares `PM FRAMING:` and `ARCHITECT VALIDATION:` as required typed slots before any option is authored. Three enforcement points: Phase 0 template, Phase 4 every option body, Phase 12 every sign-off block. New T-25.

**V-02** — Adds a `CAUSAL CHAIN CONTRACT` block to Phase 0 declaring `TEMPORAL ANCHOR − INERTIA OFFSET = DECISION LEAD TIME` with source phase attribution for each term and explicit T-GUARD routing rule per term. Phase 2 and Phase 4 cross-reference the contract. New T-25 for contract absence.

**V-03** — Converts all phase instructions to SHALL/MUST/PROHIBITED register. No new structure, but the obligation frame forces explicit contract declarations in Phase 0 (you need something to obligate against). Incidentally covers both C-32 and C-33.

**V-04** — Both Phase 0 contracts coexist: option anatomy + causal chain. Tests composability. T-25 (anatomy) and T-26 (causal contract) are both wired.

**V-05** — All six axes. Phase 0 declares four contracts (manifest, register formats, option anatomy, causal chain). PM-first role ordering throughout. PM-relevant dimensions precede technical in Phase 7. Prerequisite gate has 14 items. Should reach 100.0.

**Interesting note on V-03:** The imperative register variation incidentally satisfies C-32 and C-33 because you can't write `PM FRAMING: — REQUIRED. Absence fires T-25.` without first declaring what the contract is. Register shift pulls structural declarations forward.
