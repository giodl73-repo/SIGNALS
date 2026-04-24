Rubric written to `simulations/quest/rubrics/mock-all-rubric-v1-2026-03-15.md`.

**Summary of criteria:**

| ID | Band | Category | What it tests |
|----|------|----------|---------------|
| C-01 | Essential | correctness | All 9 namespace sections present with complete MOCK ARTIFACT headers |
| C-02 | Essential | correctness | Category labels correct — EVIDENCE-HEAVY for prove-*/listen-*, HIGH-STRUCTURE/MIXED for rest |
| C-03 | Essential | behavior | REAL-REQUIRED flag auto-applied to every EVIDENCE-HEAVY section |
| C-04 | Essential | format | Coverage summary table present with exact 4 columns, 9 rows |
| C-05 | Essential | format | Final line is `Next: /mock:review {topic} {this-file}` with real values (no placeholders) |
| C-06 | Recommended | coverage | Tier-critical namespaces (trace, scout-feasibility, listen) annotated in summary table |
| C-07 | Recommended | depth | Each namespace section has a plausible synthetic artifact body (3+ substantive lines) |
| C-08 | Recommended | behavior | Compliance-tagged topics (scout-compliance, trace-permissions) pre-flagged REAL-REQUIRED |
| C-09 | Aspirational | behavior | --tier flag correctly scopes which namespace sections appear |
| C-10 | Aspirational | depth | Recommended next steps are concrete skill invocations, not generic advice |

**Score formula:** `(essential/5 * 60) + (recommended/3 * 30) + (aspirational/2 * 10)`. Golden threshold: all 5 essential pass + score >= 80.
