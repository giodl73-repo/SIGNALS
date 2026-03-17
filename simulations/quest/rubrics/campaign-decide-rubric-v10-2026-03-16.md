Reading the scorecard carefully, I can identify two new excellence patterns:

1. **V-03** introduces a dual-signal pattern for inertia primacy: `[INERTIA IS THE PRIMARY COMPETITOR]` sub-annotation on the Phase 1a header *and* an explicit "primary competitor" label on F1-01 in the FINDING REGISTER — two independent structural signals, not just an ordering gate.

2. **V-04** surfaces a C-06 strict risk: Phase 5 sub-tables pass structurally only if bold named labels are present; the note explicitly flags "V-05 exists to eliminate this risk," which means that label-per-sub-table pattern is an extractable criterion.

→ **C-29** (inertia primacy dual-signal) and **C-30** (Phase 5 bold sub-table labels). Denominator rises to /22; max composite to 101.0.

---

```markdown
# campaign-decide-rubric-v10-2026-03-17.md

**Quest**: campaign-decide
**Version**: v10
**Date**: 2026-03-17
**Denominator**: /22 aspirational (11 pts total — 0.5 pts each)
**Max composite**: 101.0

---

## Version History

| Version | Date | Change Summary |
|---------|------|----------------|
| v1–v5 | 2026-03-14 | Initial criteria through V-04 R7 base |
| v6 | 2026-03-15 | C-14..C-22 added (V-04 R7 structural criteria); aspirational denominator /14 |
| v7 | 2026-03-16 | C-23 (column-header schema enforcement) and C-24 (sub-phase synthesis slot alignment) extracted from R6; C-17 updated: when C-21 in effect, 6-slot pass condition applies; denominator /16 |
| v8 | 2026-03-16 | C-25 (Because block column-schema enforcement), C-26 (per-rival response-strategy column), C-27 (prose-free structural sufficiency) extracted from R8; denominator /19 |
| v9 | 2026-03-17 | C-28 (Phase 0 experiment lifecycle schema) extracted from R9 V-02; denominator /20 |
| v10 | 2026-03-17 | C-29 (inertia primacy dual-signal) extracted from R10 V-03; C-30 (Phase 5 bold sub-table label enforcement) extracted from R10 V-04 C-06 strict risk; denominator /22 |

---

## Scoring Model

| Tier | IDs | Pts each | Total | Condition |
|------|-----|----------|-------|-----------|
| Essential | C-01..C-05 | 12.0 | 60.0 | All must pass — any fail = output fails |
| Recommended | C-06..C-08 | 10.0 | 30.0 | Output is better with these |
| Aspirational | C-09..C-30 | 0.5 | 11.0 | Raise the bar |
| **Max composite** | | | **101.0** | |

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
for each hypothesis. Omitting hypothesis disposition fails C-08.

---

## Aspirational Criteria

### C-09 — Confidence calibration

Phase 5 recommendation table includes a "Confidence Rationale" column that explicitly
requires FID citations, not a label alone (e.g., column header reads "Confidence Rationale
(cite FIDs — not label alone)"). Confidence stated without a citation-bearing rationale column
does not satisfy this criterion.

### C-10 — FID consistency

All FIDs referenced in body tables appear in the FINDING REGISTER. No out-of-register FID
citations are present. Pre-seeding the register before evidence phases runs is the standard
mechanism for satisfying this criterion structurally.

### C-11 — Cross-phase citation

The Because table Citation column uses a hybrid key format: "Phase N, F[N]-seq" (e.g.,
"Phase 2, F2-01"), linking each claim to both its evidence phase and its FINDING REGISTER
entry. Phase-only or FID-only citations do not satisfy C-11.

### C-12 — Segment scoring

Phase 3 (scout-market) table includes a numeric fit or attractiveness score column
(e.g., "Fit Score (1-10)") per market segment, enabling quantitative comparison across
segments rather than prose-only description.

### C-13 — Hypothesis-prior anchoring

Phase 0 includes a hypothesis table with a "Prior Confidence" column and an
"Expected Result (fill now)" column that commits the predicted outcome before any evidence
phase executes. The prior-confidence record must precede the Phase 1 gate annotation.

### C-14 — Phase boundaries

Every phase section header carries a `[COMPLETE BEFORE PHASE N]` gate annotation.
Phases without explicit gate annotations do not satisfy C-14.

### C-15 — Feasibility traffic-light

Phase 2 (scout-feasibility) table includes a signal column using a three-value traffic-light
scheme (R / Y / G or equivalent). Numeric-only or prose-only feasibility assessment does
not satisfy C-15.

### C-16 — Pre-seeded FINDING REGISTER

The full FINDING REGISTER (all FIDs across all phases) is committed at the top of the
document under a `[COMPLETE BEFORE PHASE 0]` gate annotation, before any evidence phase
section appears. Registers committed inline within phases or after evidence sections do not
satisfy C-16.

### C-17 — 6-slot Because block

The Because block contains exactly six rows, one per evidence slot:
Phase 0 / PRIOR, Phase 1a / INERTIA, Phase 1b / RIVALS, Phase 2 / FEASIBILITY,
Phase 3 / MARKET, Phase 4 / WEB EVIDENCE. Fewer rows, merged slots, or unnumbered
phase labels do not satisfy C-17. (When C-21 is in effect, the 6-slot pass condition applies.)

### C-18 — Recommendation record structure

The Phase 5 recommendation sub-table (F5-02 or equivalent) carries exactly four named
columns: FID, Recommendation, Confidence, Confidence Rationale. Missing or renamed
columns do not satisfy C-18.

### C-19 — Counter-evidence record

The Phase 5 counter-evidence sub-table (F5-03 / F5-04 or equivalent) carries named columns
for Counter-Evidence, Qualifying FID, Recommended Next Step, and Condition. Fewer columns
or unlabeled columns do not satisfy C-19.

### C-20 — Gate annotations in headers

Every phase section header (Phase 0 through Phase 5) carries a `[COMPLETE BEFORE PHASE N]`
gate annotation. Missing gate annotations on any phase header fail C-20.

### C-21 — Phase 1a/1b gate

Phase 1a section header explicitly carries `[COMPLETE BEFORE PHASE 1b]` as its gate
annotation, distinct from the inter-phase gate (which reads `[COMPLETE BEFORE PHASE 2]`).
A combined gate or merged Phase 1 header does not satisfy C-21.

### C-22 — Hybrid citations

The Because table Citation column header explicitly encodes the required citation format
(e.g., "Citation (Phase N, F[N]-seq)"), making the hybrid-key requirement part of the
schema itself rather than a prose instruction. Citation column with a generic label does
not satisfy C-22.

### C-23 — Domain-specific column headers (strict)

Every table in the output uses domain-specific column names. No table uses generic
placeholder column names (e.g., "Field", "Value", "Item", "Note"). Column semantics must
be expressed in the header text itself.

### C-24 — 1a/1b synthesis slot split

The Because table contains distinct rows for "Phase 1a / INERTIA" and "Phase 1b / RIVALS",
with the Phase column making the 1a/1b split structurally unambiguous. A single combined
"Phase 1 / COMPETITORS" row does not satisfy C-24.

### C-25 — Because table column schema

The Because table carries exactly four named columns: Phase, Label, Citation, Claim.
Tables with fewer columns, unlabeled columns, or merged Phase/Label columns do not satisfy
C-25.

### C-26 — Per-rival response strategy

Phase 1b (scout-competitors rivals) table includes a "Response Strategy" column specifying
how the team wins against each named rival. FINDING REGISTER labels for Phase 1b FIDs
also note "with response strategy" to enforce pre-commitment. Phase 1b tables with
competitive analysis but no response strategy column do not satisfy C-26.

### C-27 — Prose-free structural sufficiency

All criteria C-01 through C-26 can be verified from column headers, table structure, gate
annotations, and FINDING REGISTER labels alone, without relying on prose body text for
scoring. Outputs where prose is load-bearing for any criterion do not satisfy C-27.

### C-28 — Phase 0 experiment lifecycle schema

Phase 0 experiment table carries at minimum five columns: FID, Experiment Name,
Investigation Method, Expected Result (filled at Phase 0), Actual Outcome (filled at Phase 5).
The two temporal columns must encode which phase fills each column — either via parenthetical
in the column name (e.g., "Expected Result (Phase 0)") or via an explicit Phase 5 closure
directive. Tables where Actual Outcome is left structurally undefined at Phase 0 do not
satisfy C-28.

### C-29 — Inertia primacy dual-signal

Phase 1a header carries both the gate annotation and an `[INERTIA IS THE PRIMARY COMPETITOR]`
semantic sub-annotation (or equivalent), AND the FINDING REGISTER F1-01 entry is explicitly
labeled "Status quo (inertia) — primary competitor" or equivalent. Both structural signals
must be present independently. A gate-only Phase 1a header with no primacy callout, or a
primacy callout in prose only, does not satisfy C-29.

**Criterion interaction note:** The sub-annotation `[INERTIA IS THE PRIMARY COMPETITOR]`
follows the gate annotation in the header and is a semantic note, not a second gate. C-20 and
C-21 gate-format criteria are unaffected; the header parses as `[section] [gate] [semantic note]`.

### C-30 — Phase 5 bold sub-table labels

Each of the four Phase 5 synthesis sub-tables (hypothesis resolution, recommendation record,
counter-evidence, open questions / next steps) carries a distinct bold named label
(e.g., **Hypothesis resolution:**, **Recommendation record:**, **Counter-evidence:**,
**Open questions / next steps:**) immediately preceding the table. Labels must be bold and
present in the rendered output; gate annotations alone do not substitute. Outputs where Phase 5
sub-tables are separated only by whitespace or headings, with no bold per-table label, do not
satisfy C-30.

**C-06 interaction note:** C-30 is an aspirational extraction of the strict C-06 risk identified
in R10 V-04: when C-30 passes, C-06 strict scoring risk is eliminated. C-06 remains a
Recommended criterion (−10 pts if failed); C-30 is the aspirational hardening of that
structural requirement.
```
