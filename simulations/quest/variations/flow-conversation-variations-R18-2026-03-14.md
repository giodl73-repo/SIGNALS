Written to `simulations/quest/rubrics/flow-conversation-rubric-v17-variations-R18-2026-03-15.md`.

---

## Round 18 — Variation Summary

**Axes selected:**

| Axis | Criterion | Structural addition |
|------|-----------|---------------------|
| V | C-73 | `LIFECYCLE_POINTER_AUDIT` block in Phase 6-A — enumerates every `per LIFECYCLE_PROTOCOL Transition N` reference, checks each resolves to a labeled entry; `DANGLING_LIFECYCLE_POINTER` finding if not |
| W | C-72 | Sweep gate field gains scope citation: `CLEAN (no WRONG_SCHEMA rows; sweep scope: Deviation Budget [0-A-8], Constraint Chain Budget [0-A-9], Turn Prediction Contract [0-A-10], Status Quo Method [0-A-11])` |
| X | C-74 | Parenthetical gate field gains declaration citation: `PASS; declarations verified: DEVIATION_BUDGET: [N] rows CONFIRMED, CONV_CHAIN_BUDGET: [N] rows CONFIRMED, ...` |

**Variation matrix:**

| Variation | Axis | Lifecycle protocol | LIFECYCLE_POINTER_AUDIT | Sweep gate field | Parenthetical gate field |
|-----------|------|--------------------|------------------------|------------------|--------------------------|
| V-01 | V only | SOLE_AUTHORITY section + pointer-only | YES | simple toggle (C-69) | simple toggle (C-71) |
| V-02 | W only | inline | NO | WITH scope citation (C-72) | simple toggle (C-71) |
| V-03 | X only | inline + CONSTRAINT phrasing | NO | simple toggle (C-69) | WITH declaration citation (C-74) |
| V-04 | V+W | SOLE_AUTHORITY section + pointer-only | YES | WITH scope citation (C-72) | simple toggle (C-71) |
| V-05 | V+W+X | SOLE_AUTHORITY section + pointer-only | YES | WITH scope citation (C-72) | WITH declaration citation (C-74) |

**Key isolation decisions:**
- V-01 carries C-69 + C-71 from baseline but adds only the pointer audit — proving C-73 is achievable without C-72/C-74
- V-02 carries C-70 baseline but uses inline lifecycle, deliberately keeping C-73 unaddressed — isolating C-72 to the format change only
- V-03 uses CONSTRAINT phrasing register to emphasize C-74 as a structural traceability obligation rather than a quality observation
- V-04 tests that Axis V (audit table) and Axis W (gate field format) do not interfere — they operate on different Phase 6-A locations
- V-05 is the R18 benchmark: all three criteria simultaneously, gate fully self-describing without cross-referencing Phase 0-CA-1
