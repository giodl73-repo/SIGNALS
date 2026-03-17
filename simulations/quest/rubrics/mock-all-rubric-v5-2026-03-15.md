Done. Here is the complete updated rubric:

---

```yaml
skill: quest-rubric
skill_target: mock-all
date: 2026-03-15
version: 5
```

# Rubric: mock-all

Scoring rubric for the `/mock:all` skill — generates synthetic signal artifacts for all 9
namespaces in a single pass, producing a unified coverage picture.

---

## Criteria

### Essential (must all pass — 60% weight)

**C-01** — All nine namespaces present with MOCK ARTIFACT header blocks
**C-02** — Category classification correct for every namespace
**C-03** — REAL-REQUIRED flag applied to all EVIDENCE-HEAVY namespaces
**C-04** — Coverage summary table present with correct columns
**C-05** — Final line follows the prescribed handoff pattern

*(unchanged from v1)*

---

### Recommended (raise output quality — 30% weight)

**C-06** — Tier 2/3 critical namespaces flagged in coverage summary
**C-07** — Each namespace section contains a plausible synthetic artifact body
**C-08** — Compliance-tagged topics pre-flagged REAL-REQUIRED in summary

*(unchanged from v1)*

---

### Aspirational (raise the bar — 10% weight; denominator = 9)

**C-09** *(unchanged)* — Tier flag correctly scopes output when --tier is supplied

**C-10** *(unchanged)* — Recommended next steps are actionable and namespace-specific

**C-11** *(added v2)* — Category classification table generated before any artifact body
> Pre-classify-then-generate ordering: a table assigning every namespace its Category must appear before the first artifact body is written. Interleaved or per-section classification does not pass.

**C-12** *(added v2)* — Handoff instruction isolated in a dedicated, explicitly-labelled section
> The `Next: /mock:review` line must appear in its own numbered/labelled block (e.g. "FINAL LINE"), structurally separate from the coverage table, with explicit anti-placeholder language for `{this-file}`.

**C-13** *(added v2)* — REAL-REQUIRED flag accompanied by explanatory rationale
> Every REAL-REQUIRED application must include a one-line rationale ("A synthetic artifact cannot substitute for real signal…"). Rationale may appear once as a preamble rule scoped to all placements.

**C-14** *(added v3)* — Explicit stop-gate phrase at each phase boundary
> When the skill defines named phases, each boundary must include an explicit stop-gate phrase such as "Do not proceed to [Phase N+1] until [Phase N output] is complete." Implied ordering via phase names or step labels alone does not pass.

**C-15** *(added v3)* — Artifact body content matches the namespace's assigned category
> Each synthetic artifact body must use language appropriate to its assigned category: EVIDENCE-HEAVY namespaces (prove, listen) use study/data/interview language; HIGH-STRUCTURE namespaces (trace, flow) use interface/contract/specification language; SIGNAL-RICH namespaces use discovery/signal language. Positive guidance alone ("use X framing") is insufficient — explicit DO NOT prohibition clauses are required per category to prevent register drift. **A skill that provides MUST vocabulary without corresponding DO NOT prohibitions earns PARTIAL credit only.**

**C-16** *(added v4)* — Stop-gate phrases enumerate specific required output fields
> A stop-gate phrase must name the specific fields or rows the model must have produced before proceeding — not just signal generic task completion. "Do not begin PHASE 2 until all nine namespaces have an assigned Category, Tier 2/3 Critical value, and Compliance-Tagged value" passes. "Do not begin PHASE 2 until PHASE 1 is complete" does not — without enumerated completeness criteria, the model can satisfy the gate with a partially-filled table.

**C-17** *(added v4)* — Vocabulary rules anchored as columns in the classification table
> MUST/DO NOT vocabulary constraints must appear as columns in the classification table itself, co-located with the category assignment row — not in a separate vocabulary section written after classification. A skill that places vocabulary rules in a downstream prose block does not pass, even if those rules are otherwise correct and complete.

---

## Scoring Formula

```
Score = Essential_pass_rate × 60
      + Recommended_pass_rate × 30
      + (Aspirational_pass_count / 9) × 10
```

**Aspirational denominator: 9** (C-09 through C-17)

Perfect score: Essential 60 + Recommended 30 + Aspirational 10 = **100**

---

## Version History

| Version | Added | Key change |
|---------|-------|-----------|
| v1 | C-01–C-10 | Core essential + recommended + basic aspirational |
| v2 | C-11–C-13 | Pre-classify ordering, isolated handoff section, REAL-REQUIRED rationale |
| v3 | C-14–C-15 | Explicit stop-gate phrases, category-matched artifact vocabulary |
| v4 | C-16–C-17 | Stop-gate field enumeration, vocabulary-column anchoring |
| v5 | — | C-15 body completed; C-16/C-17 formalized from R4 excellence signals |

---

**What changed in v5 vs the draft v4 shown in the prompt:**

- **C-15 completed** — the truncated sentence ("A skill that provides MUST vocabulary without corresponding DO NOT") now closes: "…prohibitions earns PARTIAL credit only." This was confirmed by the R4 scorecard: V-03 and V-04 evidence shows DO NOT prohibitions are load-bearing, not optional.
- **C-16 formalized** — stop-gate specificity: field-enumerated gates (V-01/V-02 PASS) vs. generic completion signals (failure mode). The V-03 PASS with only 3 columns named confirms gates must enumerate *exactly the columns present*, not a superset.
- **C-17 formalized** — vocabulary-column co-location: V-03 FAIL makes the failure mode concrete — vocabulary rules in a separate prose block below the table do not pass even when the rules themselves are correct.
- **Scoring formula section added** with explicit denominator = 9 for the aspirational band.
