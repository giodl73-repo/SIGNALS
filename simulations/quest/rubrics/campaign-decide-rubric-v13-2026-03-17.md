# campaign-decide-rubric-v13-2026-03-17.md

**Quest**: campaign-decide
**Version**: v13
**Date**: 2026-03-17
**Denominator**: /28 aspirational (14.0 pts total — 0.5 pts each)
**Max composite**: 104.0

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
| v11 | 2026-03-17 | C-31 (Phase 1a FINDING REGISTER Switching Cost column) extracted from R11 V-03; C-32 (Phase 5 Counter Block schema) extracted from R11 V-04/V-05; C-33 (confidence calibration quantified thresholds) extracted from R11 V-05; denominator /25 |
| v12 | 2026-03-17 | C-34 (confidence threshold propagated via top-level schema definition) extracted from R12 V-05 Excellence Signal 1; denominator /26 |
| v13 | 2026-03-17 | C-35 (Prior Confidence propagated from Phase 0 preamble into Phase 5 hypothesis resolution) and C-36 (per-phase FINDING REGISTER closure directives) extracted from R13 V-05 new structural patterns; denominator /28 |

---

## Scoring Model

| Tier | IDs | Pts each | Total | Condition |
|------|-----|----------|-------|-----------|
| Essential | C-01..C-05 | 12.0 | 60.0 | All must pass — any fail = output fails |
| Recommended | C-06..C-08 | 10.0 | 30.0 | Output is better with these |
| Aspirational | C-09..C-36 | 0.5 | 14.0 | Raise the bar |
| **Max composite** | | | **104.0** | |

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

Phase 1a section header explicitly carries `[COMPLETE BEFORE Phase 1b]` as its gate
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

### C-31 — Phase 1a FINDING REGISTER Switching Cost column

Phase 1a FINDING REGISTER uses a 4-column extended schema: `FID / Finding Summary /
Primary Competitor / Switching Cost`. The `Switching Cost` column (H / M / L) surfaces the
behavioral cost of abandoning the status quo and is the structural reason inertia is listed first
among competitors. A 3-column register that omits `Switching Cost` does not satisfy C-31,
even when C-29 (dual-signal) passes.

**C-29 interaction note:** C-29 requires the `primary competitor: YES` flag in the register;
C-31 requires the full 4-column schema including Switching Cost. The two criteria are
independent: a register can carry the C-29 flag in a 3-column schema (C-31 fails) or carry
4 columns without both signals (C-29 fails).

### C-32 — Phase 5 Counter Block schema

Phase 5 includes a dedicated **Counter Block** sub-table with exactly three named columns:
`FID / Counter Claim / Rebuttal`. The Counter Block captures the single strongest argument
against the recommendation and must rebut it inline via the Rebuttal column. A Gap Block
that lists risks without an explicit rebuttal column does not satisfy C-32, even if C-07 passes.
The Counter Block must be a structurally distinct sub-table from the Gap Block, with its own
bold label and its own schema.

**C-30 interaction note:** C-30 requires 4 bold-labeled Phase 5 sub-tables; the Counter Block
is the sub-table that satisfies the fourth slot in C-30. When C-32 passes, C-30's fourth
sub-table requirement is satisfied structurally. C-30 may pass with any bold-labeled fourth
sub-table; C-32 hardens the schema requirement for that sub-table specifically.

### C-33 — Confidence calibration quantified thresholds

The output annotates its confidence levels (H / M / L) with explicit percentage alignment
thresholds: H = 80%+ findings align, M = 50–79%, L = below 50% (or equivalent quantified
scale). A bare confidence label (H / M / L) without stated quantified thresholds does not
satisfy C-33. The thresholds may appear inline with the recommendation, in a confidence
calibration note, or as a parenthetical on the Confidence column header; any of these
structural locations satisfies C-33.

**C-09 interaction note:** C-09 requires a Confidence Rationale column with FID citations;
C-33 requires quantified thresholds on the confidence scale itself. Both can be satisfied
independently or together. A threshold annotation without per-decision FID rationale passes
C-33 but fails C-09; a FID-cited rationale without percentage thresholds passes C-09 but
fails C-33.

### C-34 — Confidence threshold propagated via top-level schema definition

The quantified confidence thresholds are encoded directly in the Confidence column header
of the schema definition that appears before Phase 0 (e.g., in the Because block or
recommendation schema at the structural preamble of the document), such that the annotation
reads `Confidence (H=80%+ / M=50-79% / L<50%)` or equivalent in the column header itself.
When the schema is defined once at document top in this form, the threshold propagates to
every table referiting that schema without repeated prose reminders. Outputs where the
threshold appears only inline with a recommendation value or only in a Phase 5 output table
column header — but not in a pre-Phase-0 schema definition — do not satisfy C-34.

**C-33 interaction note:** C-33 passes if thresholds appear in any structural location (inline,
per-table header, or preamble schema). C-34 requires the threshold specifically in the
pre-Phase-0 schema definition so it propagates globally — one definition, unlimited reach.
C-34 implies C-33; C-33 does not imply C-34. A threshold encoded only in the Phase 5
recommendation table header passes C-33 but fails C-34.

### C-35 — Prior Confidence propagated into Phase 5 hypothesis resolution

The Phase 5 hypothesis resolution sub-table carries a `Prior Confidence` column (matching
the column defined in the Phase 0 preamble schema), enabling an explicit before/after
confidence comparison per hypothesis at the point of disposition. The column must contain
the prior belief value committed in Phase 0 — not merely a placeholder — so the reader can
assess calibration: how far the evidence moved confidence from the prior. Outputs where
Phase 5 hypothesis resolution records only the outcome status (CONFIRMED / REFUTED /
INCONCLUSIVE) without the prior-belief anchor do not satisfy C-35.

**C-13 interaction note:** C-13 requires `Prior Confidence` in the Phase 0 schema (before
evidence runs). C-35 requires that same column to appear in the Phase 5 resolution table
so the prior and actual outcome are co-located at the point of synthesis. C-35 implies C-13;
C-13 does not imply C-35. A Phase 0 schema with `Prior Confidence` that is not carried
forward to Phase 5 passes C-13 but fails C-35.

**C-08 interaction note:** C-08 requires a Phase 5 hypothesis disposition sub-table (any form).
C-35 hardens the schema of that table to include the prior-belief column. C-08 can pass with
a table that has only Hypothesis / Outcome / Status; C-35 requires Prior Confidence as an
additional column.

### C-36 — Per-phase FINDING REGISTER closure directives

After each evidence phase section (Phase 0 through Phase 4), the output includes an explicit
`Close FINDING REGISTER Phase N rows` directive (or equivalent), instructing the agent to
fill in the pre-seeded register entries for that phase before proceeding. This creates a
two-stage commit architecture: FID placeholders are pre-seeded at document top (C-16),
and each phase's register rows are closed progressively as evidence is gathered. Outputs
where the FINDING REGISTER is pre-seeded but lacks per-phase closure directives — leaving
all fill-in to Phase 5 or implicit — do not satisfy C-36.

**C-10 interaction note:** C-10 verifies FID consistency (no out-of-register citations). C-16
verifies pre-seeding at document top. C-36 hardens the commit discipline by requiring
explicit per-phase closure — enforcing that the register is updated as the work proceeds,
not left as open placeholders until synthesis. All three criteria are independent: a document
can pre-seed and close progressively (all pass), pre-seed without closing (C-10/C-16 may
pass, C-36 fails), or close inline without pre-seeding (C-36 may satisfy intent but C-16 fails).
