Written to `simulations/quest/golden/mock-ns-variate-R5-2026-03-15.md`.

---

## Round 5 — V-01 through V-05

Five complete skill body prompts. Single-axis first, then convergence.

### Variation map

| Variant | Axis | New criteria | Predicted score |
|---------|------|-------------|-----------------|
| **V-01** | Phrasing register (formal/imperative) | C-18 + C-19 | ~98.3 |
| **V-02** | Inertia framing (path class enumeration as primary mechanism) | C-18 only | ~97.5 |
| **V-03** | Lifecycle emphasis (consequence framing at consumption site) | C-18 + C-20 | ~97.5 |
| **V-04** | Output format (table-structured baseline) | None — C-16+C-17 only | ~97.5 |
| **V-05** | Role sequence (full convergence) | C-18 + C-19 + C-20 | 100 |

### What each variant tests

**V-01** (anti-displacement closure, no consequence): S-3 names all execution path classes — conditional branches, fallback paths, regeneration sequences, catch-all, and bypass-order clarifier. A-1 names the specific instruction types that cannot precede the rule and closes with a declarative assertion. No C-20 consequence statement. Tests whether closure alone is sufficient.

**V-02** (path class enumeration only): S-3 has the full C-18 enumeration. A-1 has first-rule only — no closure, no competitors named. Tests the single-axis hypothesis that compute-site protection dominates.

**V-03** (consequence framing without closure): A-1 has `RULE 1` followed immediately by the inertia-consequence statement (invisible mismatch, corrupts trust tier, undetectable by automated review). No anti-displacement closure — the prohibition doesn't name what it beats. Tests whether consequence visibility alone breaks inertia.

**V-04** (R3 baseline reproduced): Run-scoped at S-3 (`do not re-evaluate in any subsequent step of this run`), first-rule at A-1. No new v5 language anywhere. Scores ~97.5 as the prior-round ceiling — provides the denominator for evaluating C-18, C-19, C-20 individually.

**V-05** (all three simultaneously): S-3 has the full path class enumeration with catch-all and bypass-order clarifier. A-1 opens with the first rule, names three competing instruction types, asserts declarative closure, then names the consequence (category mismatch invisible to downstream tooling, silently corrupts trust tier). All twenty criteria reachable.

### Key discriminants for scoring

- **V-01 vs V-05** isolates C-20 — does naming the failure consequence add anything once anti-displacement closure is present?
- **V-02 vs V-01** isolates C-19 — is path class enumeration (C-18) alone sufficient, or does consumption-site closure add independent value?
- **V-03 vs V-01** isolates C-19 vs C-20 as the stronger individual criterion when only one can be added to the C-18 base.
- **V-04** anchors the R3 baseline, confirming each v5 criterion's marginal contribution.
