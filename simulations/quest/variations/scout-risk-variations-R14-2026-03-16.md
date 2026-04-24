Written to `simulations/quest/variations/scout-risk-variations-R14-2026-03-17.md`.

---

## Scout-Risk R14 — Variations (v13 Rubric)

**Baseline**: R13 V-05 scores **153/156** against v13 — C-38 already PASS (+2), but C-39/C-40/C-41 each PARTIAL (+1 each).

### Three single axes selected

| Axis | Criterion | Gap in R13 V-05 | Fix |
|------|-----------|----------------|-----|
| **Lifecycle emphasis** | C-39 | "Add MEDIUM and LOW rows" = implicit restriction, not explicit prohibition | Added: "Do not add HIGH-severity rows in Phase 2 — adding one is a format violation" |
| **Role sequence** | C-40 | "A deficit here means type monoculture — not a HIGH coverage gap" = diagnosis redirection, not declarative exclusion from repair scope | Added: "This audit does not repair per-dimension HIGH coverage (which Phase 1b guarantees) — its scope is type-class distribution only. Do not revise Phase 1b entries..." |
| **Output format** | C-41 | Phase 0b names consumers via negative constraint ("no columns added during X") — not an affirmative forward-reference coverage declaration | Added: "This schema is consumed by three generation phases: Phase 1 [...], Phase 1b [...], and Phase 2 [...]." |

### Expected scores

| Variation | Axes | C-39 | C-40 | C-41 | Score |
|-----------|------|------|------|------|-------|
| V-01 | C-39 only | PASS | PARTIAL | PARTIAL | 154/156 |
| V-02 | C-40 only | PARTIAL | PASS | PARTIAL | 154/156 |
| V-03 | C-41 only | PARTIAL | PARTIAL | PASS | 154/156 |
| V-04 | C-39 + C-40 | PASS | PASS | PARTIAL | 155/156 |
| V-05 | All three | PASS | PASS | PASS | **156/156** |

### Key design insight

C-39 and C-40 form a **Phase 1b boundary pair** — C-39 guards the forward boundary (no new HIGH enters Phase 2), C-40 guards the backward boundary (Phase 2b cannot repair what Phase 1b already sealed). C-41 is independent — it converts Phase 0b's consumer list from a negative constraint to an affirmative coverage claim. All three changes are phase-local and non-interacting.
