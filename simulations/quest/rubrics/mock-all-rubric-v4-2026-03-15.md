Reading the R3 scorecard carefully to extract the two new patterns before writing the rubric.

The `new_patterns` block names:
- **C-16** — Stop-gate completeness specification (gates must enumerate specific required output fields, not generic "until complete" signals)
- **C-17** — Vocabulary-column anchoring (MUST/DO NOT rules embedded as columns in the classification table, co-located with category assignment)

I also need to complete the truncated C-15 body from v3 using the scorecard evidence (V-02 PARTIAL shows positive-guidance-only fails; V-01/V-03 PASS show DO NOT prohibition is required).

```markdown
skill: quest-rubric
skill_target: mock-all
date: 2026-03-15
version: 4
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

### Aspirational (raise the bar — 10% weight)

**C-09** *(unchanged)* — Tier flag correctly scopes output when --tier is supplied

**C-10** *(unchanged)* — Recommended next steps are actionable and namespace-specific

**C-11** *(added v2)* — Category classification table generated before any artifact body
> Pre-classify-then-generate ordering: a table assigning every namespace its Category must
> appear before the first artifact body is written. Interleaved or per-section classification
> does not pass.

**C-12** *(added v2)* — Handoff instruction isolated in a dedicated, explicitly-labelled section
> The `Next: /mock:review` line must appear in its own numbered/labelled block (e.g.
> "FINAL LINE"), structurally separate from the coverage table, with explicit
> anti-placeholder language for `{this-file}`.

**C-13** *(added v2)* — REAL-REQUIRED flag accompanied by explanatory rationale
> Every REAL-REQUIRED application must include a one-line rationale ("A synthetic artifact
> cannot substitute for real signal…"). Rationale may appear once as a preamble rule scoped
> to all placements.

**C-14** *(added v3)* — Explicit stop-gate phrase at each phase boundary
> When the skill defines named phases (e.g. CLASSIFY, GENERATE, SUMMARIZE, HANDOFF), each
> boundary must include an explicit stop-gate phrase such as "Do not proceed to [Phase N+1]
> until [Phase N output] is complete." Implied ordering via phase names or step labels alone
> does not pass; the gate must be a surface-level instruction the model can read and obey.

**C-15** *(added v3)* — Artifact body content matches the namespace's assigned category
> Each synthetic artifact body must use language appropriate to its assigned category:
> EVIDENCE-HEAVY namespaces (prove, listen) use study/data/interview language; HIGH-STRUCTURE
> namespaces (trace, flow) use interface/contract/specification language; SIGNAL-RICH
> namespaces use discovery/signal language. Positive guidance alone ("use X framing") is
> insufficient — explicit DO NOT prohibition clauses are required per category to prevent
> register drift. A skill that provides MUST vocabulary without corresponding DO NOT
> prohibitions earns PARTIAL credit only.

**C-16** *(new v4)* — Stop-gate phrases enumerate specific required output fields
> A stop-gate phrase must name the specific fields or rows the model must have produced
> before proceeding — not just signal generic task completion. For example: "Do not begin
> PHASE 2 until the classification table is complete and all nine namespaces have an assigned
> Category, Tier 2/3 Critical value, and Compliance-Tagged value" is self-checkable and
> resistant to partial-output bypass. A gate that says only "Do not begin PHASE 2 until
> PHASE 1 is complete" does not pass — without enumerated completeness criteria, the model
> can satisfy the gate with a partially-filled table. Gates at every phase boundary must meet
> this specificity standard to pass.

**C-17** *(new v4)* — Vocabulary rules anchored as columns in the classification table
> MUST/DO NOT vocabulary constraints for each category must appear as columns in the
> classification table itself, co-located with the category assignment row — not in a
> separate vocabulary section or block written after classification. Anchoring at the
> assignment step ensures constraints are registered before any artifact body is written.
> A skill that places vocabulary rules in a separate block downstream of the table does not
> pass, even if those rules are otherwise correct and complete.
```
