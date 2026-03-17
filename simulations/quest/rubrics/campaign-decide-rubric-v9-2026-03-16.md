```markdown
# campaign-decide-rubric-v9-2026-03-17.md

**Quest**: campaign-decide
**Version**: v9
**Date**: 2026-03-17
**Denominator**: /20 aspirational (10 pts total — 0.5 pts each)
**Max composite**: 100.0

---

## Version History

| Version | Date | Change Summary |
|---------|------|----------------|
| v1–v5 | 2026-03-14 | Initial criteria through V-04 R7 base |
| v6 | 2026-03-15 | C-14..C-22 added (V-04 R7 structural criteria); aspirational denominator /14 |
| v7 | 2026-03-16 | C-23 (column-header schema enforcement) and C-24 (sub-phase synthesis slot alignment) extracted from R6; C-17 updated: when C-21 in effect, 6-slot pass condition applies; denominator /16 |
| v8 | 2026-03-16 | C-25 (Because block column-schema enforcement), C-26 (per-rival response-strategy column), C-27 (prose-free structural sufficiency) extracted from R8; denominator /19 |
| v9 | 2026-03-17 | C-28 (Phase 0 experiment lifecycle schema) extracted from R9 V-02; denominator /20 |

---

## Scoring Model

| Tier | IDs | Pts each | Total | Condition |
|------|-----|----------|-------|-----------|
| Essential | C-01..C-05 | 12.0 | 60.0 | All must pass — any fail = output fails |
| Recommended | C-06..C-08 | 10.0 | 30.0 | Output is better with these |
| Aspirational | C-09..C-28 | 0.5 | 10.0 | Raise the bar |
| **Max composite** | | | **100.0** | |

---

## Essential Criteria

### C-01 — Recommendation stated

Output contains an explicit recommendation from the set {COMMIT, PAUSE, PIVOT, ABANDON}.
A decision brief with no stated recommendation fails regardless of evidence quality.

### C-02 — Confidence stated

Output states a confidence level (H / M / L or equivalent) for the recommendation.
Confidence must be present as a named field, not embedded in prose.

### C-03 — All six domains covered

Output addresses all six evidence domains:
Phase 0 (prove-hypothesis), Phase 1a (scout-competitors), Phase 1b (scout-competitors rivals),
Phase 2 (scout-feasibility), Phase 3 (scout-market), Phase 4 (prove-websearch),
Phase 5 (prove-synthesize). Omission of any domain fails C-03.

### C-04 — Inertia-first ordering

Phase 1a precedes Phase 1b. A `[COMPLETE BEFORE Phase 1b]` gate annotation or equivalent
structural separator is required. Reversing the order or merging 1a/1b into a single block fails.

### C-05 — Evidence-to-recommendation traceability

Every claim in the synthesis block can be traced to a finding in the evidence phases via
citation. Synthesis claims with no traceable FID citation fail C-05.

---

## Recommended Criteria

### C-06 — Structured brief format

Output uses a formal document structure: FINDING REGISTER header, titled phase sections,
and a Phase 5 synthesis split into sub-tables. Prose-only output with no structural scaffold fails.

### C-07 — Risk / counter-evidence

Phase 5 includes a counter-evidence sub-table with named columns for counter-claim,
qualifying FID, and disposition. Omitting counter-evidence treatment fails C-07.

### C-08 — Hypothesis disposition

Phase 5 includes a hypothesis-outcome sub-table recording Confirmed / Refuted / Inconclusive
disposition per Phase 0 hypothesis. Missing or prose-only hypothesis disposition fails C-08.

---

## Aspirational Criteria

### C-09 — Confidence calibration (depth)

Confidence rationale cites specific FIDs rather than restating the label. A column header
such as `Confidence Rationale (cite FIDs — not label alone)` structurally blocks label-only
citations. Rationale that does not reference finding IDs fails C-09.

### C-10 — Actionable next steps (depth)

Phase 5 next-steps sub-table carries a two-branch gate: concrete action for the COMMIT path
and an exit trigger for the no-build path. A column schema such as
`Condition [COMMIT: concrete action | no-build: exit trigger]` encodes both branches.
Single-branch next steps fail C-10.

### C-11 — Per-phase required-field schema (format)

Every evidence phase uses domain-specific named-column tables. No phase is prose-only.
The schema for each phase must be defined by column headers, not by surrounding instructions.

### C-12 — Templated citation syntax (format)

Citations throughout the output use a consistent machine-readable format.
A column header such as `Citation (Phase N, F[N]-seq)` enforces the format structurally.
Free-form citation text fails C-12.

### C-13 — Hypothesis-prior anchoring (depth)

Phase 0 appears before Phase 1 in document order. Phase 0 includes `Prior Confidence` and
`Prior Rationale` columns that anchor the hypothesis commitment before any evidence is gathered.
Missing prior columns or Phase 0 positioned after evidence phases fails C-13.

### C-14 — FINDING REGISTER header block (format)

The document opens with a FINDING REGISTER block gated `[COMPLETE BEFORE PHASE 0]`.
All FIDs are registered in the header before any phase body. A document that introduces
findings inline within phase bodies without a header register fails C-14.

### C-15 — Phase gate annotations present (format)

Each phase carries an explicit gate annotation (e.g., `[COMPLETE BEFORE Phase N+1]`).
Phases without gate annotations fail C-15.

### C-16 — FID namespace consistency (format)

Finding IDs follow a consistent namespace: `F[phase]-[seq]` (e.g., F0-01, F1a-03).
Mixed formats or non-namespaced IDs fail C-16.

### C-17 — Because block present and slot-complete (depth)

A Because block synthesizes evidence across phases. When C-21 (6-slot alignment) is in
effect, the Because block must have exactly six slots — one per evidence sub-phase.
Fewer slots or an absent Because block fails C-17.

### C-18 — Phase 1a inertia-specific fields (depth)

Phase 1a scout-competitors table includes inertia-specific columns: switching cost,
lock-in mechanism, or equivalent. Generic competitor columns without inertia fields fail C-18.

### C-19 — Phase 2 feasibility risk quantification (depth)

Phase 2 scout-feasibility table includes a risk severity or effort estimate column.
Feasibility findings without quantified risk fail C-19.

### C-20 — Phase 3 market-signal citation (depth)

Phase 3 scout-market findings cite external signals (market data, analyst reports, or
comparable evidence). Unsupported market assertions fail C-20.

### C-21 — Phase 5 six-slot sub-table alignment (format)

Phase 5 synthesis is split into exactly four named sub-tables covering: hypothesis outcome
(F5-01), recommendation (F5-02), counter-evidence (F5-03), and next steps (F5-04).
Merged or missing sub-tables fail C-21.

### C-22 — No anonymous positional columns (format)

No table in the output uses positional columns (Column 1, Column 2, or unlabeled columns).
Every column has a named header. Any anonymous column fails C-22.

### C-23 — Column-header schema enforcement (format)

Column headers carry the format constraint, not surrounding prose. A header such as
`Citation (Phase N, F[N]-seq)` encodes the citation format; a header labeled `Citation`
with format instructions in a preamble paragraph does not satisfy C-23. The schema must
be in the header row itself.

### C-24 — Sub-phase synthesis slot alignment (format)

Phase 5 sub-tables are explicitly scoped to individual synthesis obligations: F5-01 for
hypothesis disposition, F5-02 for recommendation, F5-03 for counter-evidence, F5-04 for
next steps. A combined "synthesis" table covering multiple obligations in one block fails C-24.

### C-25 — Because block column-schema enforcement (format)

The Because block is a named-column table with a header row. The minimum viable schema is
`Phase | Label | Citation | Claim` or a superset. A bullet-list Because block — even one
with labeled Phase slots (C-24 PASS) and hybrid citations (C-12 PASS) — fails C-25.
The column-schema discipline required of evidence phases (C-23) applies to the synthesis
layer itself. Prerequisites: C-12, C-23, C-24.

### C-26 — Per-rival response-strategy column (depth)

Phase 1b rivals table carries an explicit response-strategy column: how the feature under
evaluation wins against each listed competitor. A four-column rivals table recording
identity, positioning, and weakness without a response column fails C-26. The response
strategy must appear as a named column in the Phase 1b table, not as prose in the synthesis
block. Prerequisite: C-11.

### C-27 — Prose-free structural sufficiency (format)

The template is informationally complete without prose wrappers. Every semantic requirement
is carried by column headers, gate annotations, section ordering, citation formats, FID
section labels, or slot-count annotations. Paragraph-form explanations in phase bodies
that are the sole carrier of a semantic requirement fail C-27. Structural annotations
such as `**Because [6 rows — one per evidence sub-phase]:**` satisfy C-27; an explanatory
paragraph describing what the Because block should contain does not.

### C-28 — Phase 0 experiment lifecycle schema (depth)

Phase 0 experiment sub-tables (F0-02, F0-03) carry both an `Expected Outcome` column and
an `Actual Outcome` column. The Expected Outcome column anchors the prior prediction at
the moment of hypothesis commitment; the Actual Outcome column records what the experiment
produced. Structural misalignment between the two columns is machine-visible without
evaluating row content. A Phase 0 experiment table with no Expected Outcome column fails
C-28 even if hypothesis disposition is present in Phase 5 (C-08 PASS). Prerequisite: C-13.

---

## v9 Changelog — New Criteria from Round 9

### C-28 — Phase 0 experiment lifecycle schema (depth)

V-02 R9's addition of `Expected Outcome` and `Actual Outcome` columns to Phase 0 experiment
sub-tables (F0-02, F0-03) demonstrates that hypothesis-outcome alignment can be made
structurally verifiable without reading row content. Prior versions recorded hypotheses in
Phase 0 (C-13: Prior Confidence + Prior Rationale) and dispositioned them in Phase 5
(C-08: Confirmed / Refuted / Inconclusive), but the experiment execution layer between
commitment and outcome was schema-free. C-28 closes this gap: the Expected Outcome column
encodes the prediction at the point of experimental design; the Actual Outcome column
records the result. A reviewer can detect hypothesis drift — cases where the actual result
contradicts the expected prediction — by comparing two columns without evaluating prose.
This is the same machine-visibility principle applied in C-23 (column headers carry schema
constraints), C-25 (Because block carries citation format in column names), and C-27
(prose is not the sole semantic carrier), now applied to the experiment execution loop
within Phase 0. Prerequisite: C-13.
```
