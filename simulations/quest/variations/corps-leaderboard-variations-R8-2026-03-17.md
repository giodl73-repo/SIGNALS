Written to `simulations/quest/golden/corps-leaderboard-variate-R8-2026-03-17.md`.

---

## Variate R8 — corps-leaderboard

5 complete prompt body variations. Summary:

| Variation | Axis | C-24 | C-25 | Expected v8 Score |
|-----------|------|------|------|-------------------|
| V-01 | Phrasing register — direct imperative command style | no | no | ~98.82 |
| V-02 | Role sequence — Archivist → Analyst → Publisher + **prevents: count gate** | **yes** | no | ~99.41 |
| V-03 | Output format — prose health narrative (no tables except registry/leaderboard) | no | no | ~98.82 |
| V-04 | Lifecycle emphasis — milestones-first inverted order with phase exit gates | no | no | ~98.82 |
| V-05 | Inertia framing + **Skeptic-named synthesis novelty gate** | no | **yes** | ~99.41 |

### Design decisions

**C-24 isolated in V-02**: The Publisher role adds an explicit `ACTIONS GATE: prevents: prefix used for {N} zero-score conditions` line after all actions are written. This makes the count verifiable at review time. V-02 also satisfies C-22 via two structurally independent locations for the `prevents:` rule: once in the pre-write check construct (before actions), once inside the action template definition.

**C-25 isolated in V-05**: The Skeptic gate in Pass 2 section 2.2 carries explicit pass/fail examples — a restated inertia flag fails, a second-order cross-topic pattern passes. The Skeptic has read Pass 1 in full, so "already known" is operationally defined. This is a different mechanism from C-13 (structural form) — novelty is tested independently of whether the sentence has a number and a name.

**All five carry C-01–C-23**: Every variation includes the two-level nearest-miss cascade (Level 1 first, Level 2 only when no Level 1 exists), dual-statement `prevents:` rule redundancy, all five exact achievement names, all three exact milestone names, and ranked leaderboard with unknown-contributor fallback.

**R9 ceiling**: The first variation to embed both C-24 and C-25 together — a Publisher role with a count gate and a Skeptic-named novelty constraint on the Team Insight — should score 100 against v8.
