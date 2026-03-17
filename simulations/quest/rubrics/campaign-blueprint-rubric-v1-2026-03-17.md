---
skill: quest-rubric
skill_target: campaign-blueprint
date: 2026-03-17
version: 1
---

# campaign-blueprint Rubric — v1

Scoring rubric for the `campaign-blueprint` skill. This skill orchestrates three
sub-skills in sequence — draft-spec, draft-proposal, draft-pitch — producing a
complete specification package for a feature topic.

**Composite score formula:**
`(essential_pass/N * 60) + (recommended_pass/N * 30) + (aspirational_pass/N * 10)`

**Golden threshold:** all essential pass + composite >= 80.

**Score ceiling:** 100 pts (5 essential x 12 + 3 recommended x 10 + 2 aspirational x 5 = 100)

---

## Essential Criteria

All must pass. Failure on any essential criterion means the output is not useful.

---

### C-01 — All Three Artifacts Present

**Weight:** essential
**Category:** correctness
**Points:** 12

**Criterion:** The campaign produces all three required artifacts: a technical specification
(spec), a proposal or ADR (proposal), and a pitch deck narrative (pitch). Each artifact
must be written as a distinct, non-trivial document — not a stub or placeholder.

**Pass condition:** Three complete artifact files are written to the correct paths:
`simulations/draft/specs/{topic}-spec-{date}.md`,
`simulations/draft/proposals/{topic}-proposal-{date}.md`,
`simulations/draft/pitches/{topic}-pitch-{date}.md`.
All three files must be non-empty and contain substantive content (more than headings alone).

FULL or NO CREDIT. Partial credit: if two of three are present and substantive, score 6.

---

### C-02 — Spec Has Required Sections

**Weight:** essential
**Category:** correctness
**Points:** 12

**Criterion:** The technical specification produced by the campaign contains the required
structural sections defined by the draft-spec sub-skill: PURPOSE, REQUIREMENTS
(MoSCoW-tagged), DESIGN, CONSTRAINTS, and OPEN QUESTIONS.

**Pass condition:** All five sections are present in the spec artifact with substantive
content. REQUIREMENTS must include at least one Must-have item with MoSCoW tag (M).
The OPEN QUESTIONS section must list at least one item (self-review output).

FULL or PARTIAL (8 pts if 4 of 5 sections present with content).

---

### C-03 — Proposal Has Three Options Minimum

**Weight:** essential
**Category:** correctness
**Points:** 12

**Criterion:** The proposal produced by the campaign contains at minimum three options,
one of which must be a do-nothing or status-quo option. Each option must include at
minimum: description, pros, cons, and a recommendation or rationale selecting among them.

**Pass condition:** Three or more options present, including do-nothing. A RECOMMENDATION
section (or equivalent) explicitly names the chosen option and states why. Each option
includes pros and cons (even if brief).

FULL or NO CREDIT.

---

### C-04 — Pitch Has Three Audience Versions

**Weight:** essential
**Category:** correctness
**Points:** 12

**Criterion:** The pitch produced by the campaign contains distinct versions for three
audiences: exec (outcome-first, ROI framing), developer (show the tool), and maker
(jargon-free, "can I do this?" framing). Each version must include at minimum: hook,
what it does, why it matters, and a call to action.

**Pass condition:** Three labeled versions present (exec/developer/maker or equivalent
labels identifying the audience). Each version is distinct in framing — not the same
text reformatted. Each version contains hook + value + CTA structure.

FULL or PARTIAL (8 pts if two versions present and distinct).

---

### C-05 — Sequence Integrity: Each Artifact Reads Its Predecessor

**Weight:** essential
**Category:** behavior
**Points:** 12

**Criterion:** The campaign respects the dependency chain: proposal must reference or
incorporate decisions from the spec; pitch must reference the proposal's recommended
option. The final pitch must be coherent with the spec's constraints — no factual
contradiction between artifacts about what the feature does or who it is for.

**Pass condition:** Proposal content is consistent with and references the spec
(e.g., uses the same feature name, same scope). Pitch's exec version references the
recommended option from the proposal by name or paraphrase. No artifact contradicts
a prior artifact's stated constraints or decisions.

FULL or PARTIAL (6 pts if two of three cross-references are traceable).

---

## Recommended Criteria

Output is better with these. Pass/fail affects the 30-point recommended band.

---

### C-06 — Inertia Baseline Anchored Across All Three Artifacts

**Weight:** recommended
**Category:** depth
**Points:** 10

**Criterion:** The feature is anchored to what users do today without it — the inertia
baseline — in each of the three artifacts. The spec's PURPOSE section, the proposal's
do-nothing option, and the pitch's "why it matters" section should all reference
the inertia state, making the cost of not building explicit.

**Pass condition:** All three artifacts contain a statement (even brief) about what
users do today / the status quo / the cost of inaction. The do-nothing option in the
proposal explicitly states the cost of inertia, not just "nothing changes."

FULL (10) if all three. PARTIAL (5) if two of three.

---

### C-07 — Scout Signal Integration

**Weight:** recommended
**Category:** coverage
**Points:** 10

**Criterion:** The campaign checks for existing scout artifacts and incorporates
available signals. Specifically: scout-requirements informs the spec's REQUIREMENTS
section if available; scout-feasibility informs the proposal's option effort/risk
ratings if available; scout-positioning informs the pitch's per-audience framing if
available.

**Pass condition:** The campaign performs a glob or scan for scout signals before
writing artifacts. If signals are found, they are referenced (by file name or inline).
If no signals exist, the absence is acknowledged with a brief note — the campaign
does not silently skip the scan.

FULL (10) if scan performed and any found signals are incorporated.
PARTIAL (5) if scan performed but no found signals are incorporated, or scan skipped
but absence acknowledged.

---

### C-08 — Spec Self-Review: Open Questions and Gaps Flagged

**Weight:** recommended
**Category:** depth
**Points:** 10

**Criterion:** The spec ends with a self-review that explicitly flags open questions,
gaps, and ambiguities identified during authoring. This is the draft-spec sub-skill's
self-review phase — it should surface what is not yet decided or not yet known.

**Pass condition:** The spec's OPEN QUESTIONS section (or a labeled self-review block)
contains at least two distinct, specific open questions or gaps — not generic
boilerplate. At least one gap should point to an information dependency (e.g., "need
scout-feasibility result to confirm effort estimate for Option A").

FULL or PARTIAL (5 pts if one specific item present).

---

## Aspirational Criteria

Raise the bar. Pass/fail affects the 10-point aspirational band.

---

### C-09 — Artifact Contract Matrix Declared Before Execution

**Weight:** aspirational
**Category:** format
**Points:** 5

**Criterion:** Before writing any artifact, the campaign declares a full artifact
contract: for each of the three artifacts, what it READs, what it WRITEs,
what it PRESERVEs from prior artifacts, and what it CARRIES FORWARD to subsequent
artifacts. This contract is printed in the output (not merely executed silently),
making the dependency chain explicit and auditable.

**Pass condition:** A contract declaration appears before Artifact 1 content begins.
It covers all three artifacts and includes READ, WRITE, PRESERVE, and CARRIES FORWARD
fields for each. The contract is in a table or structured block, not prose paragraphs.

FULL or NO CREDIT.

---

### C-10 — Pitch Anti-Positioning Section

**Weight:** aspirational
**Category:** depth
**Points:** 5

**Criterion:** The pitch contains an explicit anti-positioning section stating what the
feature is NOT — ruling out adjacent or confused use cases that could dilute messaging
or attract the wrong audience. This is a requirement of the draft-pitch sub-skill and
sharpens all three audience versions by bounding the claim.

**Pass condition:** At least one labeled "NOT" or "Anti-positioning" or "What this is not"
section or subsection appears in the pitch artifact with at least two specific exclusion
statements (not generic disclaimer language).

FULL or NO CREDIT.

---

## Scoring Summary

| ID   | Criterion                                          | Weight        | Pts |
|------|----------------------------------------------------|---------------|-----|
| C-01 | All three artifacts present                        | essential     | 12  |
| C-02 | Spec has required sections                         | essential     | 12  |
| C-03 | Proposal has three options minimum                 | essential     | 12  |
| C-04 | Pitch has three audience versions                  | essential     | 12  |
| C-05 | Sequence integrity: each artifact reads predecessor | essential    | 12  |
| C-06 | Inertia baseline anchored across all three         | recommended   | 10  |
| C-07 | Scout signal integration                           | recommended   | 10  |
| C-08 | Spec self-review: open questions flagged           | recommended   | 10  |
| C-09 | Artifact contract matrix declared before execution | aspirational  |  5  |
| C-10 | Pitch anti-positioning section                     | aspirational  |  5  |
|      | **Total**                                          |               | **100** |

## Score Calculation

```
essential_pts  = sum of earned pts from C-01..C-05 (max 60)
recommended_pts = sum of earned pts from C-06..C-08 (max 30)
aspirational_pts = sum of earned pts from C-09..C-10 (max 10)

composite = essential_pts + recommended_pts + aspirational_pts
```

**Golden threshold:** all five essential criteria pass at FULL + composite >= 80.
