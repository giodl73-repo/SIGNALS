**corps-leaderboard-variate-R9-2026-03-17.md** written.

---

## R9 Design Summary

**Key move**: R8 isolated C-24 in V-02 and C-25 in V-05. R9 embeds **both** in all five variations, closing that gap — while isolating the new v9 criteria in the same two variation slots.

### Variation Axes

| Variation | Axis | New in R9 | C-24 | C-25 | C-26 | C-27 |
|-----------|------|-----------|------|------|------|------|
| V-01 | Phrasing register (MUST/SHALL spec) | C-24 + C-25 | ✓ | ✓ | — | — |
| V-02 | Role sequence (Archivist→Analyst→Publisher) | C-25 added | ✓ | ✓ | ✓ | — |
| V-03 | Output format (gate-driven checklist) | C-24 + C-25 | ✓ | ✓ | — | — |
| V-04 | Lifecycle (milestones-first) + decision-table pre-write | C-24 + C-25 | ✓ | ✓ | — | — |
| V-05 | Inertia framing (health/inertia structural separation) | C-24 added | ✓ | ✓ | — | ✓ |

### Structural choices that enforce the new criteria

**C-24 in V-01 (MUST/SHALL)**: The ACTIONS GATE becomes a `SHALL output exactly this line` assertion — the imperative modal matches the register of the rest of the spec.

**C-24 in V-03 (checklist)**: The ACTIONS GATE appears as Phase 4 Gate item `[ ] ACTIONS GATE line written with actual N count substituted` — failure is a missing checkbox.

**C-24 in V-04 (decision table)**: The pre-write table has explicit Y/N rows for each zero-score condition; the gate count must match the `Y` rows that produced `prevents:` actions — mismatch is auditable.

**C-25 placement**: All five now gate the Team Insight with a Skeptic who has read the full prior output. V-02 places it inside the Publisher role naturally (Analyst output = "already known").

**C-26 preserved in V-02**: Three named roles, each with explicit `does NOT` scope constraints, and named handoff points (Archivist→Analyst, Analyst→Publisher).

**C-27 preserved in V-05**: Health Phase (1.2) and Inertia Phase (1.3) are explicitly named, defined, and sequentially required — with a structural note that "health reports what exists; inertia reports direction."

**Expected scoring against v9**: V-01/V-03/V-04 at **98.95** (17/19 aspirational), V-02 and V-05 co-ceiling at **99.47** (18/19). Ceiling remains open — combining C-26 + C-27 (named role pipeline with explicit health/inertia separation inside a role) is reserved for R10.
