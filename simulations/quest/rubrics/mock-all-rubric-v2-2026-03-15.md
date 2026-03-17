Here is the complete updated rubric:

---

```
skill: quest-rubric
skill_target: mock-all
date: 2026-03-15
version: 2
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

**C-11** *(new)* — Category classification table generated before any artifact body
> Pre-classify-then-generate ordering: a table assigning every namespace its Category must appear before the first artifact body is written. Interleaved or per-section classification does not pass.

**C-12** *(new)* — Handoff instruction isolated in a dedicated, explicitly-labelled section
> The `Next: /mock:review` line must appear in its own numbered/labelled block (e.g. "FINAL LINE"), structurally separate from the coverage table, with explicit anti-placeholder language for `{this-file}`.

**C-13** *(new)* — REAL-REQUIRED flag accompanied by explanatory rationale
> Every REAL-REQUIRED application must include a one-line rationale ("A synthetic artifact cannot substitute for real signal…"). Rationale may appear once as a preamble rule scoped to all placements.

---

## Composite Scoring

```
score = (essential_pass / 5 * 60)
      + (recommended_pass / 3 * 30)
      + (aspirational_pass / 5 * 10)   ← denominator was 2, now 5
```

**Golden threshold**: all 5 essential criteria pass AND composite score >= 80.

| Band | Weight | Criteria |
|------|--------|----------|
| Essential | 60% | C-01 – C-05 |
| Recommended | 30% | C-06 – C-08 |
| Aspirational | 10% | C-09 – C-13 |

---

**Key change from v1:** The three excellence signals from V-01 are now testable criteria. The aspirational denominator changes from 2 to 5, so the band still contributes 10 points maximum but a V-01-quality prompt that passes C-11/C-12/C-13 in addition to C-09/C-10 scores the full 10 rather than earning no extra credit. V-02's C-05 failure would have been caught by C-12 in this rubric.
 MOCK ARTIFACT header, each namespace section includes at least
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

**C-11** — Category classification table generated before any artifact body
- Weight: aspirational
- Category: behavior
- Pass condition: The prompt or output includes an explicit pre-classification step — a table or
  enumeration that assigns every namespace its Category value — before the first artifact body
  is written. When the classification is front-loaded, the model holds ground-truth labels in
  active context during generation and cannot produce a C-02 mismatch by drift. A prompt that
  interleaves classification with generation, or classifies inline per section, does not satisfy
  this criterion.
- Source: V-01 excellence signal — pre-classify-then-generate ordering eliminates mid-generation
  category drift.

**C-12** — Handoff instruction isolated in a dedicated, explicitly-labelled section
- Weight: aspirational
- Category: format
- Pass condition: The final-line handoff (`Next: /mock:review {topic} {this-file}`) appears in
  its own numbered or labelled block (e.g., "FINAL LINE", "Step N: Handoff") that is
  structurally separate from the coverage summary table. The section must include explicit
  anti-placeholder language indicating that `{this-file}` must be the actual artifact filename
  for this run, not a template token. A handoff line buried in prose or appended without a
  dedicated section label does not satisfy this criterion.
- Source: V-01 excellence signal — dedicated FINAL LINE section with anti-placeholder annotation
  prevents C-05 failures that occur when the instruction is buried in a prose block.

**C-13** — REAL-REQUIRED flag accompanied by explanatory rationale
- Weight: aspirational
- Category: depth
- Pass condition: Every application of the REAL-REQUIRED flag (whether in EVIDENCE-HEAVY
  namespace headers or compliance-tagged summary rows) is accompanied by a one-line rationale
  explaining why synthetic signal cannot substitute (e.g., "A synthetic artifact cannot
  substitute for real signal in these namespaces" or equivalent). Flag assertions without
  rationale satisfy C-03 but fail C-13. Rationale may appear once as a preamble rule rather
  than repeated per section, provided it is unambiguously scoped to all REAL-REQUIRED
  placements.
- Source: V-01 excellence signal — rationale injection alongside bare imperatives increases
  flag compliance by giving the model a causal anchor for the rule.

---

## Composite Scoring

```
score = (essential_pass / 5 * 60)
      + (recommended_pass / 3 * 30)
      + (aspirational_pass / 5 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite score >= 80.

| Band | Weight | Criteria |
|------|--------|----------|
| Essential | 60% | C-01, C-02, C-03, C-04, C-05 |
| Recommended | 30% | C-06, C-07, C-08 |
| Aspirational | 10% | C-09, C-10, C-11, C-12, C-13 |

---

## Design Notes

The essential band focuses on structural completeness (C-01), classification accuracy (C-02),
automatic flag propagation (C-03, C-05), and the handoff contract (C-05) — without these the
output cannot be used as a reliable coverage baseline. The REAL-REQUIRED mechanic (C-03, C-08)
is essential rather than recommended because an unflagged EVIDENCE-HEAVY or compliance-tagged
namespace would give a false sense of mock coverage sufficiency.

C-08 (compliance pre-flagging) is recommended rather than essential because it only activates
for compliance-tagged topics; the criterion cannot be graded on a topic with no such tags and
should not penalize the base case.

C-09 (--tier scoping) and C-10 (actionable next steps) are aspirational because they require
either a specific flag invocation or richer per-namespace knowledge of the skill catalog --
both raise quality once the foundation is stable.

C-11, C-12, and C-13 are aspirational criteria added in v2 from Round 1 excellence signals.
C-11 encodes the pre-classify-then-generate ordering that prevents C-02 drift. C-12 encodes
the dedicated-section pattern that prevents C-05 failures in complex output structures. C-13
encodes rationale injection alongside REAL-REQUIRED flags, which increases compliance over
bare imperatives. All three are aspirational rather than recommended because they constrain
prompt structure rather than output content -- a prompt can pass the lower bands without them,
but adopting them closes the most common failure modes observed in Round 1.
