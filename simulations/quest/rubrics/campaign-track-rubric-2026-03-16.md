Rubric written to `simulations/quest/rubrics/campaign-track-rubric-v1-2026-03-16.md`.

**Structure:**

| ID | Text | Weight | Category |
|----|------|--------|----------|
| C-01 | Orchestration sequence — all 4 sub-skills invoked in order | essential | correctness |
| C-02 | Topic registration artifact — strategy.md with planned signals | essential | correctness |
| C-03 | Coverage delta display — collected vs missing, named gaps | essential | coverage |
| C-04 | Narrative synthesis — verdict verb + hypothesis mutation | essential | depth |
| C-05 | Session-bookend utility — handles both empty and populated state | essential | behavior |
| C-06 | Actionable next-signal recommendations with namespace/skill | recommended | depth |
| C-07 | Coverage ratio + explicit readiness statement | recommended | format |
| C-08 | Cross-namespace balance check, flags zero-signal namespaces | recommended | coverage |
| C-09 | Echo integration — unexpected findings surfaced distinctly | aspirational | depth |
| C-10 | Dual-session delta — what changed this session | aspirational | behavior |

The minimum viable bar (C-01 + C-03 + C-04) catches the most common failure mode: a skill that runs sub-skills but produces no coverage picture or no verdict. C-05 is the edge-case guard for empty-session invocations, which this orchestrator skill must handle gracefully.
