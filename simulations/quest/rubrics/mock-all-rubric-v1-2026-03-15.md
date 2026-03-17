---
skill: quest-rubric
skill_target: mock-all
date: 2026-03-15
version: 1
---

# Rubric: mock-all

Scoring rubric for the `/mock:all` skill — generates synthetic signal artifacts for all 9
namespaces in a single pass, producing a unified coverage picture.

---

## Criteria

### Essential (must all pass — 60% weight)

**C-01** — All nine namespaces present with MOCK ARTIFACT header blocks
- Weight: essential
- Category: correctness
- Pass condition: Output contains exactly 9 namespace sections (scout, draft, review, flow,
  trace, prove, listen, program, topic), each opening with a MOCK ARTIFACT block that includes
  Skill, Topic, Category, Date, and Status: MOCK fields. Any missing namespace or missing header
  field is a fail.

**C-02** — Category classification correct for every namespace
- Weight: essential
- Category: correctness
- Pass condition: prove-* and listen-* sections are classified EVIDENCE-HEAVY; scout, draft,
  review, flow, trace are classified HIGH-STRUCTURE; program and topic are classified MIXED or
  HIGH-STRUCTURE. No namespace may carry a category that contradicts the skill spec's
  HIGH-STRUCTURE | EVIDENCE-HEAVY | MIXED taxonomy.

**C-03** — REAL-REQUIRED flag applied to all EVIDENCE-HEAVY namespaces
- Weight: essential
- Category: behavior
- Pass condition: Every section whose Category is EVIDENCE-HEAVY (prove-*, listen-*) carries a
  REAL-REQUIRED flag — either in the header block or immediately beneath it. Absence of the flag
  in any EVIDENCE-HEAVY section is a fail.

**C-04** — Coverage summary table present with correct columns
- Weight: essential
- Category: format
- Pass condition: Output ends with a Markdown table whose columns are exactly: Namespace,
  Category, Flag, Recommended next step. Table contains one row per namespace (9 rows). Missing
  table, wrong column names, or fewer than 9 rows is a fail.

**C-05** — Final line follows the prescribed handoff pattern
- Weight: essential
- Category: format
- Pass condition: The very last line of the output is `Next: /mock:review {topic} {this-file}`
  where `{topic}` is the topic name supplied to the skill and `{this-file}` resolves to the
  artifact filename just produced. Literal placeholder tokens in the output are a fail.

---

### Recommended (raise output quality — 30% weight)

**C-06** — Tier 2/3 critical namespaces flagged in coverage summary
- Weight: recommended
- Category: coverage
- Pass condition: Rows for trace, scout-feasibility, and listen in the coverage summary table
  each carry a visible Tier-critical annotation (e.g., "TIER-2-CRITICAL" or "TIER-3-CRITICAL")
  in the Flag column. Absence of tier annotation on any of these three rows is a partial fail
  (each missing annotation reduces score proportionally across the recommended band).

**C-07** — Each namespace section contains a plausible synthetic artifact body
- Weight: recommended
- Category: depth
- Pass condition: Below the MOCK ARTIFACT header, each namespace section includes at least
  3 substantive content lines that represent realistic synthetic signal content for that
  namespace (not generic filler). Header-only sections with no artifact body are a fail for
  this criterion.

**C-08** — Compliance-tagged topics pre-flagged REAL-REQUIRED in summary
- Weight: recommended
- Category: behavior
- Pass condition: When the topic has scout-compliance or trace-permissions skills present (or
  the --compliance flag is passed), those rows in the coverage table carry REAL-REQUIRED in the
  Flag column regardless of the structural quality of the synthetic artifact. If the topic has
  no compliance-tagged skills, this criterion is skipped (auto-pass).

---

### Aspirational (raise the bar — 10% weight)

**C-09** — Tier flag correctly scopes output when --tier is supplied
- Weight: aspirational
- Category: behavior
- Pass condition: When invoked with --tier 2 or --tier 3, the output only produces namespace
  sections and coverage rows for namespaces at or above that tier level. Tier 1 (default) must
  produce all 9 namespaces. Output that ignores the --tier flag or produces wrong namespace
  sets fails this criterion.

**C-10** — Recommended next steps are actionable and namespace-specific
- Weight: aspirational
- Category: depth
- Pass condition: Every row's "Recommended next step" cell names a concrete skill invocation
  (e.g., `/scout:feasibility {topic}`, `/prove:prototype {topic}`) rather than generic advice
  such as "gather more data" or "run the skill". Rows with non-specific guidance fail this
  criterion.

---

## Composite Scoring

```
score = (essential_pass / 5 * 60)
      + (recommended_pass / 3 * 30)
      + (aspirational_pass / 2 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite score >= 80.

| Band | Weight | Criteria |
|------|--------|----------|
| Essential | 60% | C-01, C-02, C-03, C-04, C-05 |
| Recommended | 30% | C-06, C-07, C-08 |
| Aspirational | 10% | C-09, C-10 |

---

## Design Notes

The essential band focuses on structural completeness (C-01), classification accuracy (C-02),
automatic flag propagation (C-03, C-05), and the handoff contract (C-05) — without these the
output cannot be used as a reliable coverage baseline. The REAL-REQUIRED mechanic (C-03, C-08)
is essential rather than recommended because an unflaged EVIDENCE-HEAVY or compliance-tagged
namespace would give a false sense of mock coverage sufficiency.

C-08 (compliance pre-flagging) is recommended rather than essential because it only activates
for compliance-tagged topics; the criterion cannot be graded on a topic with no such tags and
should not penalize the base case.

C-09 (--tier scoping) and C-10 (actionable next steps) are aspirational because they require
either a specific flag invocation or richer per-namespace knowledge of the skill catalog —
both raise quality once the foundation is stable.
