Reading the scorecard evidence carefully before writing.

The three axes from the preamble map to:
- **C-18** — already written in v6 (role-identity framing)
- **C-19** — still missing: V-02 C-07 evidence (`{3-5 sentence artifact body}` inside the placeholder, not in prose around it)
- **C-20** — still missing: V-03 C-07 + C-10 evidence (inertia question drives both body grounding and next-step specificity)

Adding both now brings aspirational count to 12, matching the stated denominator.

---

```yaml
skill: quest-rubric
skill_target: mock-all
date: 2026-03-15
version: 7
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

### Aspirational (raise the bar — 10% weight; denominator = 12)

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

**C-18** *(added v6)* — Named role-identity assignment per phase
> Each phase must assign a named role identity (e.g., CLASSIFIER, GENERATOR, SUMMARIZER, HANDOFF WRITER) rather than only step or phase numbers. The role name must make wrong-phase behavior an identity violation — the model knows it *is* the CLASSIFIER, not merely *is in step 1*. Phase labels or STEP numbers alone do not pass. Role identity blocks cross-phase contamination (e.g., generating artifact bodies during classification) at the ontological level, beyond what stop-gate phrases (C-14) enforce.

**C-19** *(added v7)* — Artifact template placeholder contains an inline depth anchor
> The template body placeholder must embed a length and depth constraint directly inside the placeholder token itself — for example, `{3-5 sentence artifact body, written in MUST vocabulary for this namespace, grounded in {topic}}`. A depth instruction placed in prose before or after the placeholder, even within the same role block, does not pass. The constraint must be readable at the exact point of generation without requiring the model to scan surrounding text. Template-level co-location (depth inside the placeholder) is distinct from table-level co-location (C-17); each satisfies only its own criterion.

**C-20** *(added v7)* — Inertia question anchors artifact body semantic quality
> Each namespace section must pose an inertia question of the form "Without this signal, {topic}'s feature story would be missing: ___" that the model answers before writing the artifact body. The artifact body must be traceable to the inertia answer — a body that could have been written without answering the question is too generic and must be revised. Additionally, recommended next steps for that namespace must address the specific gap named in the inertia answer; generic next steps derived solely from category assignment do not pass when an inertia answer is present. Vocabulary compliance alone (C-15) does not substitute for inertia-grounded specificity.
