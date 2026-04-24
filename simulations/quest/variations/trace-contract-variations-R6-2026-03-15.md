Here are the 5 variations for **trace-contract R6 (rubric v6)**:

---

## Variation Map

| V | Axis | Base | Targets | Est. Score |
|---|------|------|---------|-----------|
| V-01 | output-format: pre-printed `## Patterns` slot | R5 V-01 | C-20 | 100 |
| V-02 | output-format: cosmetic-tier `connector-impact` field | R5 V-04 | C-21 | 101 |
| V-03 | lifecycle-emphasis: skeleton-first with Patterns pre-printed in artifact shape | R5 V-03 | C-20 (alt mechanism) | 99 |
| V-04 | compound: both C-20 + C-21 close | R5 V-04 | C-20 + C-21 | **103** |
| V-05 | all axes: full-strength synthesis + both R6 changes | R5 V-05 | C-01–C-21 full | **103** |

---

## R6 Gap Analysis

R5's two open gaps under v6:

- **C-20 gap** (R5 V-01 misses it): R5 V-01 puts a "Pattern note: If two or more findings share a root cause..." instruction in Phase 5. That satisfies C-10 but fails C-20 because the block is added conditionally. The fix is converting the instruction into a **pre-printed structural slot** — `## Patterns` appears unconditionally in the summary template, requiring either populated groups or an explicit "No patterns identified" statement.

- **C-21 gap** (R5 V-04 misses it): R5 V-04 has stratified templates with `connector-impact` in breaking and degraded tiers, but the cosmetic template has four fields only. C-21 requires the `connector-impact` slot in all three tiers on the basis that cosmetic deviations affect documentation generators and monitoring dashboards. The fix is adding a fifth `connector-impact` field to the cosmetic template with an explicit rationale for why cosmetic deviations carry integration risk.

**Single-axis priority**: V-04 is the cleanest path to 103 — minimal changes from the proven R5 V-04 base, no mechanism interference. V-01 and V-02 isolate each change independently for diagnostic value. V-03 tests whether the **skeleton-first mechanism** (making the Patterns block visible before Phase 1) is more reliable than the **template-slot mechanism** (pre-printing the block in Phase 5 instructions).

The file is at `simulations/quest/golden/trace-contract-variate-R6-2026-03-15-new.md`.
