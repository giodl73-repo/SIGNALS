Looking at the R2 scorecard, I can identify two new excellence patterns from V-02 and V-03 that aren't yet captured as criteria:

**From V-02 (Named Phases + Stop Gates):** V-02 earned C-12 via a dedicated HANDOFF phase, but C-11 only got PARTIAL because "CLASSIFY as Phase 1 implies ordering, but no explicit classification table with all rows before Phase 2." The pattern: named phases need **explicit stop-gate phrases at each boundary**, not just implied ordering.

**From V-03 (Phrasing Register) + V-04 (Combination):** V-03 passed C-13 but C-07 was a target in V-04's combination axis. The combination of pre-classification + named phases implies artifact bodies should be **category-specific**, not generic. C-07 currently requires 3 substantive lines but doesn't require they match the assigned category.

New criteria:

- **C-14** — Explicit stop-gate phrase at each phase boundary
- **C-15** — Artifact body content matches the namespace's assigned category

---

```markdown
skill: quest-rubric
skill_target: mock-all
date: 2026-03-15
version: 3
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

**C-09** — Tier flag correctly scopes output when --tier is supplied *(unchanged)*
**C-10** — Recommended next steps are actionable and namespace-specific *(unchanged)*

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

**C-14** *(new v3)* — Explicit stop-gate phrase at each phase boundary
> When the skill defines named phases (e.g. CLASSIFY, GENERATE, SUMMARIZE, HANDOFF), each
> boundary must include an explicit stop-gate phrase such as "Do not proceed to [Phase N+1]
> until [Phase N output] is complete." Implied ordering via phase names alone does not pass;
> the gate must be a surface-level instruction the model can read and obey.

**C-15** *(new v3)* — Artifact body content matches the namespace's assigned category
> Each synthetic artifact body must use language appropriate to its assigned category:
> EVIDENCE-HEAVY namespaces (prove, listen) use study/data/interview language; SIGNAL-RICH
> namespaces (scout, trace, review) use coverage/scan/audit language; SYNTHESIS namespaces
> (draft, flow, program, topic) use narrative/design/plan language. Generic filler that
> could be copy-pasted unchanged into any namespace does not pass C-15, even if it satisfies
> C-07's 3-line minimum.

---

## Composite Scoring

```
score = (essential_pass / 5 * 60)
      + (recommended_pass / 3 * 30)
      + (aspirational_pass / 7 * 10)   ← denominator was 5, now 7
```

**Golden threshold**: all 5 essential criteria pass AND composite score >= 80.

| Band | Weight | Criteria |
|------|--------|----------|
| Essential | 60% | C-01 – C-05 |
| Recommended | 30% | C-06 – C-08 |
| Aspirational | 10% | C-09 – C-15 |

---

**Key changes from v2:**

- **C-14** elevates the V-02 excellence signal: named phases are necessary but not sufficient.
  V-02 scored PARTIAL on C-11 precisely because phase names imply ordering without enforcing
  it. C-14 makes the stop-gate phrase a testable surface requirement. V-02 would pass C-14
  only if its CLASSIFY phase explicitly gates the GENERATE phase.

- **C-15** elevates the V-04 combination-axis target (C-07 + C-11 + C-12): once a
  classification table exists before generation, the model has the category in context and
  can write category-appropriate content. V-03's phrasing-register axis showed rationale
  preamble lifts C-13; C-15 applies the same preamble-shapes-output logic to artifact body
  language. A prompt that passes C-11 but writes generic bodies passes C-07 and fails C-15.

- Aspirational denominator changes from 5 to 7. The band still contributes 10 points
  maximum. A V-01-quality prompt passing all 7 aspirational criteria scores the full 10.
```
