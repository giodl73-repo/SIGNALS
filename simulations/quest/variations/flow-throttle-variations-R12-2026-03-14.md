Written to `simulations/quest/rubrics/flow-throttle-rubric-v12-variations-R12-2026-03-15.md`.

---

# flow-throttle — Round 12 Variations (v12 Rubric, 178-point max)

## Variation Axes and Hypotheses

R11 established C-36 (Phase-4 Anchor Heading Evaluation-Type Subtitle) as the sole
discriminator — only V-04's "Capacity Synthesis and PA Validation" heading passed. R12
probes the boundaries of both new criteria:

**Three single-axis tests (V-01, V-02, V-03), two combination tests (V-04, V-05):**

| Variation | Axis | C-35 | C-36 | Predicted |
|-----------|------|------|------|-----------|
| V-01 | Phase 4 heading — alternative evaluation-type subtitle text ("Remediation Registry and Throttle Budget Corrections") | PASS | PASS | **178/178** |
| V-02 | Phase 4 heading — operation-description subtitle ("Synthesis and Validation"), not evaluation-type | PASS | FAIL | **175/178** |
| V-03 | Phase 0 plain ordinal heading `### PHASE 0`, no content-type subtitle | FAIL | PASS | **175/178** |
| V-04 | Combination: role sequence (PA throttle scenario analyst R1 + platform entitlement verifier R2) + Phase 0 "Current-State Inventory" + Phase 4 "Throttle Budget Corrections" | PASS | PASS | **178/178** |
| V-05 | Combination: Phase 0 plain heading (C-35 fail) + Phase 4 "Synthesis and Validation" (C-36 fail) | FAIL | FAIL | **172/178** |

**Score spread: 178 / 175 / 175 / 178 / 172**

---

## What each variation confirms

**V-01** — C-36 subtitle-text inertness: "Remediation Registry and Throttle Budget Corrections" is an alternative conforming form. If it passes, C-36 is text-inert for evaluation-type subtitles, matching the C-32 inertness pattern confirmed in R10.

**V-02** — C-36 failure boundary: "Synthesis and Validation" lists operations rather than naming an output class. The heading is structurally present but carries no class declaration — the Phase 4 analog of `### PHASE 0` failing C-35. Scores 175 (loses 3 via C-36).

**V-03** — C-35 failure: `### PHASE 0` with no subtitle. Section content satisfies C-33 (structurally distinct, establishes baseline). Heading alone fails C-35. Phase 4 uses R11 V-04's confirmed "Capacity Synthesis and PA Validation" to isolate the single axis. Also confirms C-35/C-36 independence: V-03 (fail C-35, pass C-36) scores identically to V-02 (pass C-35, fail C-36) at 175/178.

**V-04** — Role-sequence inertness for both criteria: analyst/verifier persona assignment doesn't interact with Phase 0 or Phase 4 heading structure. Also confirms C-35 text-inertness via "Current-State Inventory" and C-36 text-inertness via "Throttle Budget Corrections" (from the C-36 explicit pass-example list).

**V-05** — Double-failure floor at 172/178: confirms C-35 and C-36 each contribute exactly 3 points independently, and failing both returns to the R11 full-pass baseline score. The floor is identical to R11 V-04's score (172/172 under v11 = 172/178 under v12 when both new criteria fail).
