---

## Rubric: `topic-echo` — v6

**Skill**: `topic:echo`
**Version**: v6
**Date**: 2026-03-16
**Criteria count**: 20 (4 essential / 3 recommended / **13** aspirational)

**Formula**: `(essential_pass/4 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/13 × 10)`

Each full aspirational pass ≈ **0.77 pts** (down from 0.91 in v5, because the denominator grew from 11 → 13).

---

### Two new criteria added

**C-19 | Synthesis-Section Independence** (aspirational, structure)

Encodes the R5 finding that V-04/V-05 silently dropped the META-REFLECTION section when adding enforcement axes, losing C-13 points for zero gain. The rule: synthesis sections and enforcement sections target *different criteria* and cannot substitute for each other. A combination that replaces a synthesis section with a gate/audit section is a structurally losing trade.

Pass condition: every synthesis section present in the base skill is retained when enforcement layers are added, or a compensating synthesis mechanism covering the same aspirational criterion is introduced. PARTIAL if synthesis is reduced in scope. FAIL if synthesis is replaced by enforcement with no recovery.

Cross-reference: **C-19 FAIL → C-13 cannot exceed PARTIAL** (the meta-reflection section is the primary path to C-13 coverage).

---

**C-20 | Audit Scope Differentiation** (aspirational, enforcement)

Encodes the R5 finding that three distinct audit mechanisms — phrase-list scan, PASS/FAIL gate, paired-contrast register audit — all hit the C-18 ceiling identically. Count without scope differentiation is non-additive. Three scope levels are defined: **phrase-level** (lexical anti-pattern scan), **section-level** (register audit), **structural-level** (gate/commitment declaration). A second mechanism at the same scope produces zero additional coverage.

Pass condition: ≥2 audit mechanisms each at a distinct scope from that set, each naming at least one failure class the other cannot catch. PARTIAL if scopes overlap or distinct failure classes are not named. FAIL if only one mechanism is present (that's C-18 territory) or all mechanisms are scope-redundant.

Cross-reference: **C-20 requires C-18 PASS as a precondition.**

---

Written to `simulations/quest/rubrics/topic-echo-rubric-v6-2026-03-16.md`.
