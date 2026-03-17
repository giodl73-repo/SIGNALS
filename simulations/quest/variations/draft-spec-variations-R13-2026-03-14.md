Written to `simulations/quest/rubrics/draft-spec-rubric-v12-variate-R13-2026-03-15.md`.

---

## Quest Variate — `draft-spec` — Round 13

### Axis Map

| Var | Axis | Hypothesis |
|-----|------|------------|
| **V-01** | **Lifecycle emphasis — compressed phase headers** | Verbose REQUIRES/PRODUCES/BLOCKS boilerplate removed; replaced with single-line `→ BLOCKED:` gate statements. All 37 pass; tests whether header verbosity matters for C-17/C-28 or token placement alone suffices. |
| **V-02** | **Inertia framing — STATUS-QUO-SNAPSHOT + C-36 + C-37** | `[STATUS-QUO-SNAPSHOT]` added first in Phase 2; `[INERTIA-ANALYZED]` Condition 1 extended to name it (C-36); co-located structural fail rule for blank gap statements (C-37). **Primary golden candidate.** |
| **V-03** | **Output format — additive columns** | `[PM-COVERAGE-TABLE]` gains Coverage Evidence column; Phase 3 Requirements table gains Confidence column (HIGH/MEDIUM/LOW). All required columns (Waiver Status, per-row Status) preserved. Tests additive format neutrality. |
| **V-04** | **Combined: V-02 + V-01** | STATUS-QUO-SNAPSHOT with C-36/C-37 AND compressed headers. Cleanest candidate — inertia depth without header verbosity. |
| **V-05** | **Combined: V-02 + Strategy inertia scoping (Phase 1.5)** | STATUS-QUO-SNAPSHOT with C-36/C-37 AND a new Phase 1.5 where Strategy nominates IG-IDs from SQ rows before `[IG-REGISTER]` authoring. Tests whether the Strategy nomination sub-step surfaces new aspirational patterns. |

**Key differences from R12**: R12's V-02 introduced `[STATUS-QUO-SNAPSHOT]` and spawned C-36/C-37 as new rubric criteria. R13 now targets both — V-02/V-04/V-05 each fully satisfy C-36 (Condition 1 explicitly names `[STATUS-QUO-SNAPSHOT]`) and C-37 (structural fail rule co-located with the snapshot row definition). V-02 is the single-axis targeting variant most likely to become the new golden.
