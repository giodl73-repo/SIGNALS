Written to `simulations/quest/rubrics/flow-conversation-rubric-v15-variations-R16-2026-03-15.md`.

---

## Round 16 — Variation Summary

**Target criteria:** C-66, C-67, C-68 (v15 additions, +6 pts, max → 234)

**New axes for R16:**

| Axis | Name | Target | Mechanism |
|------|------|--------|-----------|
| P | Protocol Section Artifact | C-66 | Extract lifecycle protocol into a dedicated named `## LIFECYCLE_PROTOCOL` section before all role definitions; "Silent fallthrough is a structural violation" as first statement; all 5 transitions as labeled HANDOFF_TO + Received pairs within that section |
| Q | WRONG_SCHEMA Enforcement Chain | C-67 | Phase 6-A opens with `WRONG_SCHEMA_RESIDUAL_CHECK` table before gate verification; unresolved WRONG_SCHEMA entries from Phase 0-CA-1 become `PHASE_6A_FINDING: WRONG_SCHEMA_UNRESOLVED` |
| R | Parenthetical Verification | C-68 | Phase 6-A includes `PARENTHETICAL_PRESENCE_VERIFICATION` table with one row per DECLARATION_SCHEMA_COMPLETE entry; `PARENTHETICAL_PRESENT: NO` triggers `PHASE_6A_FINDING: MISSING_ROW_COUNT_PARENTHETICAL` as a structural defect |

**Variation matrix:**

| Variation | Axes | C-66 | C-67 | C-68 |
|-----------|------|------|------|------|
| V-01 | P | TARGET | — | — |
| V-02 | Q | — | TARGET | — |
| V-03 | R | — | — | TARGET |
| V-04 | P+Q | TARGET | TARGET | — |
| V-05 | P+Q+R | TARGET | TARGET | TARGET |

**V-05 key integration:** In V-05, Axes Q and R are co-resident under a unified `Phase 6-A Block 2 — Phase 0-CA-1 Output Audit` structure. Block 1 sweeps WRONG_SCHEMA, Block 2 verifies parentheticals, Block 3 gate verification explicitly cites both. This makes the three enforcement layers (manifest-time detection → CA-time verification → audit-time residual check) a single traceable chain.
