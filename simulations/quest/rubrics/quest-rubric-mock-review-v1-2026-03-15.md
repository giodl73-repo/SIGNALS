---
skill: quest-rubric
skill_target: mock-review
date: 2026-03-15
version: 1
---

# Rubric: mock-review

**Skill**: `/mock:review`
**Step**: Step 2 of the mock-first workflow — review coverage picture, write decisions per namespace.
**Composite score formula**: (essential_pass/N * 60) + (recommended_pass/N * 30) + (aspirational_pass/N * 10)
**Golden threshold**: All essential criteria pass AND composite >= 80.

---

## Essential Criteria

*Must all pass. A failure on any essential criterion means the output is not useful.*

### C-01 — Decision completeness
**Category**: correctness
**Weight**: essential

Every namespace present in the mock artifact receives an explicit decision of either
MOCK-ACCEPTED or REAL-REQUIRED. No namespace is left without a decision. No namespace
is left in the ambiguous MOCK (awaiting review) state after the review runs.

**Pass condition**: The review artifact contains a decision row (or equivalent labeled
statement) for each namespace section found in the input mock artifact, and each row
carries exactly one of: MOCK-ACCEPTED or REAL-REQUIRED. Zero undecided namespaces.

---

### C-02 — Automatic rule correctness
**Category**: correctness
**Weight**: essential

The three automatic flagging rules are applied correctly before any PM/Architect/Strategy
evaluation begins:

1. EVIDENCE-HEAVY category → REAL-REQUIRED at any tier
2. Critical namespaces (trace, scout-feasibility, listen, scout-competitors) at Tier 2 or
   Tier 3 → REAL-REQUIRED
3. Compliance-tagged namespaces → REAL-REQUIRED when compliance tags are present in
   TOPICS.md or the `--compliance` flag was passed

**Pass condition**: Every namespace that satisfies one or more automatic rules is marked
REAL-REQUIRED. No EVIDENCE-HEAVY namespace at any tier receives MOCK-ACCEPTED. No
critical namespace at Tier 2+ receives MOCK-ACCEPTED. No compliance-adjacent namespace
receives MOCK-ACCEPTED when compliance context is active.

---

### C-03 — MOCK-ACCEPTED reason code present
**Category**: correctness
**Weight**: essential

Every MOCK-ACCEPTED decision carries at least one of the two valid reason codes:
- STRUCTURAL-COVERAGE-SUFFICIENT
- DOMAIN-KNOWLEDGE-CONSISTENT

No MOCK-ACCEPTED decision appears without a reason code. Fabricated or paraphrased
reason codes (e.g., "good enough", "structurally fine") do not satisfy this criterion —
only the exact codes from the annotation schema are valid.

**Pass condition**: Count of MOCK-ACCEPTED decisions == count of MOCK-ACCEPTED decisions
with at least one valid reason code from the defined set.

---

### C-04 — Status fields written back to source artifact
**Category**: behavior
**Weight**: essential

The skill WRITES updated Status annotations back into the source mock artifact. For each
namespace, the `Status: MOCK (awaiting review)` line is replaced with either:
- `Status: MOCK-ACCEPTED [STRUCTURAL-COVERAGE-SUFFICIENT | DOMAIN-KNOWLEDGE-CONSISTENT]`
- `Status: REAL-REQUIRED [{reason}]`

The source mock artifact's Status fields after the skill runs must match the decisions
recorded in the review artifact. An output that produces a review document but leaves all
Status fields as `MOCK (awaiting review)` fails this criterion entirely.

**Pass condition**: The source mock artifact is edited (not replaced). For each namespace
section, the Status line reflects the decision from the review artifact. Zero Status
fields remain `MOCK (awaiting review)` after the skill completes.

---

### C-05 — Next-steps list in priority order
**Category**: correctness
**Weight**: essential

The output includes a "Next steps" list naming the real skills to run, ordered by
recommended priority. The list covers all REAL-REQUIRED namespaces. The ordering reflects
decision risk (critical namespaces before non-critical, evidence-heavy after critical).
A list that names the right skills in arbitrary order satisfies coverage but not
ordering — both are required.

**Pass condition**: A labeled next-steps section (or equivalent) is present. It contains
one entry per REAL-REQUIRED namespace. The entries are ordered (numbered or priority-
labeled), with critical namespace real runs (trace, scout-feasibility, listen) appearing
before non-critical evidence-heavy runs.

---

## Recommended Criteria

*Output is meaningfully better with these. Two of three passing contributes +30 to the composite.*

### C-06 — Rule trigger named per REAL-REQUIRED decision
**Category**: depth
**Weight**: recommended

Each REAL-REQUIRED decision names the specific rule that triggered it. Valid trigger
labels: EVIDENCE-HEAVY, TIER-CRITICAL, COMPLIANCE, or an explicit PM/Architect/Strategy
evaluation reason. "REAL-REQUIRED" alone without a trigger label is not sufficient.

**Pass condition**: Each REAL-REQUIRED row in the review table (or equivalent) includes
a reason field or note that identifies which rule caused the flag. The reason is drawn
from the defined rule vocabulary, not a freeform description.

---

### C-07 — PM / Architect / Strategy evaluation shown for non-auto namespaces
**Category**: depth
**Weight**: recommended

For namespaces that are not auto-flagged (HIGH-STRUCTURE at Tier 1, MIXED at Tier 1),
the review shows the three-role evaluation before concluding:
- PM: structural completeness assessment (required sections, gates, tables)
- Architect: technical plausibility check (does mock content contradict known facts?)
- Strategy: coverage adequacy for the current decision tier

The evaluation can be brief (one sentence per role), but all three roles must be
represented for each non-auto namespace. A review that jumps directly to the decision
without showing the evaluation fails this criterion.

**Pass condition**: For each namespace that did not receive an automatic flag, at least
three labeled evaluation inputs (PM, Architect, Strategy or equivalent) appear before or
alongside the decision. The decision is traceable to the evaluation.

---

### C-08 — Tier flag respected
**Category**: behavior
**Weight**: recommended

The `--tier` parameter (or tier read from TOPICS.md) is applied consistently throughout
the review. Tier 1 allows HIGH-STRUCTURE namespaces to be MOCK-ACCEPTED where structurally
adequate. Tier 2 and Tier 3 automatically flag critical namespaces. The tier used is
stated explicitly in the review artifact header or summary line.

**Pass condition**: The review artifact names the tier used. Critical namespace rules are
applied only at Tier 2+. At Tier 1, trace / scout-feasibility / listen are not
automatically REAL-REQUIRED unless also EVIDENCE-HEAVY. A review run with `--tier 2` that
does not flag any of the Tier 2 critical namespaces fails this criterion.

---

## Aspirational Criteria

*Raise the bar once essential and recommended are stable. One of two passing contributes +10 to composite.*

### C-09 — Coverage gap synthesis in next-steps
**Category**: depth
**Weight**: aspirational

The next-steps list goes beyond enumeration. It groups or annotates entries by urgency
tier (e.g., "gate-blockers before Tier 2 commit", "evidence-heavy after gates clear")
and includes a brief statement of cumulative coverage risk if the real runs are
deprioritized or skipped. The synthesis helps teams understand not just what to run but
why the sequence matters.

**Pass condition**: The next-steps section contains at least one grouping, urgency label,
or risk statement that synthesizes across namespaces rather than listing them
independently. A flat numbered list with no grouping or cross-namespace commentary does
not satisfy this criterion even if all entries are correct.

---

### C-10 — MOCK-ACCEPTED rationale is namespace-specific
**Category**: depth
**Weight**: aspirational

Each MOCK-ACCEPTED decision explains *why* structural coverage or domain knowledge is
sufficient for this specific namespace and topic, not just labels it with the reason
code. The explanation names the specific enforcement mechanism or structural property
that makes mock acceptance valid (e.g., "gate present and well-formed, tier 1 planning
decision does not require real stakeholder input at this stage").

**Pass condition**: Each MOCK-ACCEPTED reason code is accompanied by a namespace-specific
sentence (not a template phrase) connecting the reason code to the actual mock content
reviewed. Reason codes that appear without supporting explanation do not satisfy this
criterion, even if the code itself is correct.

---

## Scoring Summary

| ID | Criterion | Weight | Category |
|----|-----------|--------|----------|
| C-01 | Decision completeness | essential | correctness |
| C-02 | Automatic rule correctness | essential | correctness |
| C-03 | MOCK-ACCEPTED reason code present | essential | correctness |
| C-04 | Status fields written back to source | essential | behavior |
| C-05 | Next-steps list in priority order | essential | correctness |
| C-06 | Rule trigger named per REAL-REQUIRED | recommended | depth |
| C-07 | PM/Architect/Strategy shown for non-auto | recommended | depth |
| C-08 | Tier flag respected | recommended | behavior |
| C-09 | Coverage gap synthesis in next-steps | aspirational | depth |
| C-10 | MOCK-ACCEPTED rationale namespace-specific | aspirational | depth |

**Composite** = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/2 * 10)
**Golden threshold**: All 5 essential pass AND composite >= 80.
