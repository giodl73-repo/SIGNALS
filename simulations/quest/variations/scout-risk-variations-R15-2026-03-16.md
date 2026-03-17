**scout-risk-variate-R15-2026-03-17.md** written.

---

## Summary

Five complete, runnable variations targeting the three new v14 criteria. Baseline passes C-01–C-41; each variation adds exactly what its new criterion requires.

**Structural analysis — what changes per variation:**

| Variation | Phase Changed | Change |
|-----------|--------------|--------|
| V-01 | Phase 2 only | Adds "Adding a HIGH-severity row here is a **format violation**" — converts behavioral prohibition to typed violation declaration (C-42) |
| V-02 | Phase 2b only | Replaces diagnosis note with two-part exclusion: declarative scope claim ("this audit does not repair...") + action prohibition ("Do not revise Phase 1b entries...") (C-43) |
| V-03 | Phase 0b only | Appends "**No generation phase outside this list adds columns or defines its own row anatomy**" — closes the consumer list from open enumeration to closed contract (C-44) |
| V-04 | Phase 2 + Phase 2b | V-01 + V-02 changes — the Phase 1b boundary pair: forward guard (no HIGH injection in expansion) + backward guard (no re-repair in audit), both typed/closed |
| V-05 | Phase 2 + Phase 2b + Phase 0b | All three — expected 162/162 |

**Score predictions:**

| Variation | C-42 | C-43 | C-44 | Score |
|-----------|------|------|------|-------|
| V-01 | PASS | FAIL | FAIL | 158/162 |
| V-02 | FAIL | PASS | FAIL | 158/162 |
| V-03 | FAIL | FAIL | PASS | 158/162 |
| V-04 | PASS | PASS | FAIL | 160/162 |
| V-05 | PASS | PASS | PASS | **162/162** |

**Key pattern from R15**: All three new criteria are single-sentence additions to existing phase text. None require structural phase surgery. C-42 adds one sentence to a header. C-43 replaces one sentence with two. C-44 appends one sentence to a footer. The smallest linguistic units carry the largest scoring leverage when the underlying structural machinery is already in place.
