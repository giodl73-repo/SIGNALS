Here is the complete updated rubric:

---

# Rubric — mock-accept v2

## What changed from v1

Four new aspirational criteria (C-11 to C-14) extracted directly from the R1 excellence signals:

| ID | Pattern | Source |
|----|---------|--------|
| C-11 | **Inline completeness gate** — count-rows=9 or N+M=total assertion as named checkpoint | V-02 self-check, V-04 sum assertion |
| C-12 | **Reason-code enforcement at point of use** — constraint inside column rule or checkbox, not preamble only | V-02 column rule, V-05 checkbox |
| C-13 | **Phase exit assertions** — explicit N+M=total before phase transition, prevents auto-flag/evaluation interleave | V-04 Phase 1 exit pattern |
| C-14 | **Blank-line failure signal** — incomplete slot is structurally visible without prose parsing | V-05 checklist format |

Scoring formula updated: aspirational denominator changes from 2 to 6. The 10pt aspirational pool is now divided across 6 criteria (`aspirational_pass / 6 * 10`). The C-09 N/A note is updated to use denominator 5 when triggered.

Four new failure modes added (MA-09 to MA-12), one per new criterion.

The R1 universal ceiling (C-09 fails all variations, composite capped at 95) is now codified — the ceiling exists because no variation instructs artifact-as-subject grammar, not because any essential criterion is fragile.
