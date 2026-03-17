`scout-risk-rubric-v18-2026-03-17.md` written. Here's the summary of what changed:

---

## v17 -> v18: Two new criteria from R18

### C-54 — Closure declaration orders closed-world sentence before prohibition sentence (escalates C-51)
**Source**: V-01 reversal experiment — PASS on C-51 confirms order is not enforced by v17, but the reversal creates a forward-reference problem: the prohibition sentence ("No violation category outside this list...") invokes a closed list that hasn't been declared yet when it appears first. The canonical order resolves this: closed-world declaration first establishes the list, then the prohibition invokes it. Declaration-before-use applied to closure sentences.

---

### C-55 — Parity declaration is bi-directional: both peer blocks name each other (escalates C-52)
**Source**: V-02/V-04/V-05 pattern — Phase 0 adds a symmetric parity sentence naming Phase 0c. C-52 requires Phase 0c to name Phase 0 (one-directional). C-55 requires Phase 0 to also name Phase 0c, making structural equivalence verifiable from either entry point independently. Bi-directional parity also makes restructuring regressions detectable from either block rather than only from Phase 0c.

---

## Scoring delta

| Metric | v17 | v18 |
|--------|-----|-----|
| Aspirational criteria | 45 | 47 |
| Aspirational max | 90 | 94 |
| Max composite | 180 | 184 |
| Golden band | 174-180 | 178-184 |
| Strong band | 159-173 | 163-177 |
