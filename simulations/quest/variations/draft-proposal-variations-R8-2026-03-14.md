The file is written. Here's the summary:

---

## draft-proposal — Round 8 Variations (v8 rubric, /24)

Five complete, runnable skill body prompts targeting the four new criteria (C-28–C-31).

### Variation Map

| Var | Axis | New Criteria Targeted | Key Mechanism |
|-----|------|-----------------------|---------------|
| **V-01** | Role sequence — PM-first throughout | C-28 | PM leads every dual-role phase; T-19 fires if Architect sign-off appears at position 1 |
| **V-02** | Output format — canonical headers at Phase 0 | C-29 | Format contracts declared before any register is authored; T-14/T-15/T-16 are Phase 0-scoped |
| **V-03** | Lifecycle emphasis — phase manifest at Phase 0 | C-30 | PHASE MANIFEST block lists all 15 phases; LIFECYCLE ORDERING VERIFICATION note makes C-17 a single-block read |
| **V-04** | PM-first + table-dominant | C-28 + C-29 | Combination: PM framing phase anchors format discipline; canonical headers live from moment PM frames the decision |
| **V-05** | Lifecycle-heavy + inertia-forward | C-30 + C-31 | INERTIA-CHAIN CONTRACT at Phase 0 names the computation `TEMPORAL ANCHOR − INERTIA OFFSET = DECISION LEAD TIME`; phase manifest makes C-17 auditable without scanning |

### Key Design Decisions

**V-01** — PM-first is enforced structurally at every dual-role phase (framing, option authoring, perspectives) rather than only in the sign-off phase. T-19 fires on position detection alone.

**V-02** — The three register format contracts are declared at Phase 0 as `| A-NN | ASSUMPTION | VALIDATION PLAN |` etc. — not as per-phase instructions. Prose-format registers trigger named triggers immediately.

**V-03** — The phase manifest includes a LIFECYCLE ORDERING VERIFICATION section that explicitly names the Phase 8/9/10 < Phase 12 ordering, eliminating the document scan C-17 otherwise requires. T-01 and T-02 fire when the manifest is structurally incomplete.

**V-04** — Adds `PM FRAMING:` and `ARCHITECT VALIDATION:` as distinct labeled fields inside each option template, not just as phase-level instructions. Role sequence is enforced at the option-anatomy level.

**V-05** — The Phase 0 inertia-chain declaration creates a cross-phase link: it names TEMPORAL ANCHOR (Phase 2) as the input to DECISION LEAD TIME (Phase 4), making the chain's causal structure explicit before either phase executes. T-08 through T-11 are all labeled as "inertia-chain break" failures.

### Predicted Scores
All 5 variations predicted at **100.0** (31/31 criteria). The discriminator hypotheses section in the file specifies what would falsify each prediction.
