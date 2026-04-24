Written at 420 lines. Here's the summary of what changed:

---

**`org-roles-rubric-v13-2026-03-16.md`** — 420 lines.

## What changed

**Three new aspirational criteria** extracted from R13 excellence signals:

| ID | Source | Short name | Distinguishes from |
|----|--------|------------|--------------------|
| **C-53** | R13 V-01/V-04/V-05 | VERIFY-MAP verify-question-to-gap-failure-mode traceability | C-45 tests that expert *names* derive from GAP vocabulary; C-53 tests that expert *verify_questions[0]* interrogates the GAP Failure mode — the interrogation focus must connect to the named failure mode, not merely share vocabulary; establishes Chain E as a traceable provenance chain with a named Phase 2 transit artifact |
| **C-54** | R13 V-02/V-04/V-05 | SIMPLIFY-DOMAIN GATE domain-term specificity | [FC-5] "opinionated exclusion" prevents scope descriptions but allows domain-agnostic exclusions; C-54 requires each simplify_rule to contain at least one named domain artifact/mechanism/vocabulary term — parallel to what POSITIVE SOURCING does for role names; enforced via SIMPLIFY-DOMAIN REQUIREMENT in [FC-5] + per-role pre-YAML CHECK gate item |
| **C-55** | R13 V-03/V-05 | CHALLENGE-COVERAGE MAP post-anchor-card artifact | C-01/C-02 test structural existence (min 2 questions, devil-advocate present); C-55 tests coverage completeness — every Phase 1 challenge question confirmed as represented in anchor verify_questions via a named MAP artifact written after ANCHOR-CARD and before subsequent cards; introduces Chain F to PROVENANCE-CHAIN DECLARATION |

**Formula**: `/44` → `/47`

**R13 scores under v13**:

| Variate | Score | New criteria |
|---------|-------|-------------|
| V-05 | **100.00** | C-53 PASS + C-54 PASS + C-55 PASS |
| V-04 | 99.79 | C-53 PASS + C-54 PASS |
| V-01 | 99.57 | C-53 PASS only |
| V-02 | 99.57 | C-54 PASS only |
| V-03 | 99.57 | C-55 PASS only |

The v13 frontier is closed by R13 V-05. R11 V-05 and R12 V-05 both retroactively drop from 100.00 to 99.36 (fail all three new criteria). V-05's YAML write order change (anchor → stock → domain experts) confirmed non-load-bearing: no existing criterion regressed, so no C-56 emerges.
