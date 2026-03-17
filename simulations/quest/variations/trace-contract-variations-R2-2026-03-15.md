File written. Here's the R2 variate summary:

---

## Round 2 — trace-contract Variation Map

| Variation | Axis | Target | Core Mechanism |
|-----------|------|--------|----------------|
| **V-01** | Phase-gate confirmation | **C-12 only** | Explicit GATE CHECK question answered in the document before Step 3 begins; the model writes `[EXPECTED SEALED]` as an affirmative claim, not just an ordering token |
| **V-02** | Structural field enforcement | **C-11 only** | Per-finding block with column-aligned labeled slots (`deviation :`, `severity :`, `spec-ref :`, `root-cause :`, `connector-impact :`); an empty slot line is immediately visible vs. silently absent in prose |
| **V-03** | Amendment embedded in finding | **C-09 only** | `recommended-action` slot is part of the `breaking` finding template itself, not deferred to Summary; the block stays open until the slot is filled |
| **V-04** | Pattern recognition + amendment | **C-09 + C-10** | V-03's inline amendment line + a required `## Patterns` section after findings that groups by shared root cause with a `single-fix` line per group |
| **V-05** | All aspirational combined | **C-09 + C-10 + C-11 + C-12** | Gate lock + labeled slots + amendment line + patterns section; a fully compliant response scores 100 |

**Key design decisions:**
- V-01's gate is a question answered and a token written — not just `[COMMITTED]` — so C-12's "explicit acknowledgment" requirement is met structurally
- V-02's `connector-impact` slot is mandatory, not optional, which also satisfies C-06 (Automate/Connectors lens) at the block level
- V-03 splits the finding format by severity: `degraded`/`cosmetic` use the 4-field R1 format; `breaking` adds the fifth `recommended-action` field inline
- V-04 is the minimum-viable combination: two structural additions, no format changes, targets the two "analysis depth" aspirationals
- V-05 is the full integration — evaluate last to confirm no interference between the four mechanisms

**Evaluation order:** V-01 → V-02 → V-03 → V-04 → V-05
