# campaign-decide-rubric-v20-2026-03-17.md

**Quest**: campaign-decide
**Version**: v20
**Date**: 2026-03-17
**Denominator**: /44 aspirational (22.0 pts total — 0.5 pts each)
**Max composite**: 112.0

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
| v14 | 2026-03-17 | C-37 (hypothesis resolution schema pre-defined in SCHEMA PREAMBLE with explicit fill-forward directive) extracted from R14 V-01 excellence signal; C-38 (column-specific FINDING REGISTER closure directives) extracted from R14 V-02 variation axis; denominator /30 |
| v15 | 2026-03-17 | C-39 (fill-forward directive encoded as Phase 5 section-header gate annotation) extracted from R15 V-01 excellence signal; C-40 (bracket notation for FINDING REGISTER column-closure directives) extracted from R15 V-02 variation axis; denominator /32 |
| v16 | 2026-03-17 | C-41 (named-schema enumeration in Phase 5 fill-forward directive) extracted from R16 V-01 excellence signal; C-42 (per-column temporal commit annotation in bracket notation) extracted from R16 V-02 excellence signal; denominator /34 |
| v17 | 2026-03-17 | C-43 (temporal commit encoded at SCHEMA PREAMBLE definition time) extracted from R17 V-01 excellence signal; C-44 (per-phase minimum evidence count annotations) extracted from R17 V-03 excellence signal; denominator /36 |
| v18 | 2026-03-17 | C-45 (PRE-COMMITMENT block positioned before SCHEMA PREAMBLE — schema-free prior lock) extracted from R18 V-01/V-05 excellence signal; C-46 (evidence density closure annotation — header-entry/footer-close audit pair) extracted from R18 V-03/V-05 excellence signal; denominator /38 |
| v19 | 2026-03-17 | C-47 (PRE-COMMITMENT recommendation confidence with falsification condition — recommendation record gains Prior Recommendation Confidence column for Phase 5 delta) extracted from R19 V-01/V-04/V-05; C-48 (FINDING REGISTER expected FID count annotations aligned to C-44 minimums — three-point count chain) extracted from R19 V-02/V-05; C-49 (Phase 5 synthesis completeness exit annotation — four-sub-table filled/empty confirmation) extracted from R19 V-03/V-04/V-05; denominator /41 |
| v20 | 2026-03-17 | C-50 (phase gate check status annotation — three-field go/no-go verdict after C-46 density line) extracted from R20 V-01; C-51 (recommendation delta sentence after recommendation record — standalone before/after shift narrative for C-47 delta) extracted from R20 V-02; C-52 (Phase 3 Inertia Lock-in column — extends C-31 switching cost to segment level) extracted from R20 V-03; denominator /44 |

---

## Scoring Model

| Tier | IDs | Pts each | Total | Condition |
|------|-----|----------|-------|-----------|
| Essential | C-01..C-05 | 12.0 | 60.0 | All must pass — any fail = output fails |
| Recommended | C-06..C-08 | 10.0 | 30.0 | Output is better with these |
| Aspirational | C-09..C-52 | 0.5 | 22.0 | Raise the bar |
| **Max composite** | | | **112.0** | |

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
every table referencing that schema without repeated prose reminders. Outputs where the
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

### C-37 — Hypothesis resolution schema pre-defined in SCHEMA PREAMBLE with fill-forward directive

The Phase 5 hypothesis resolution table schema (including the `Prior Confidence` column
required by C-35) is defined in a SCHEMA PREAMBLE section that precedes Phase 0, and
the Phase 5 section carries an explicit fill-forward directive (e.g., "Fill the Phase 5
hypothesis resolution schema from the Schema Preamble"). This achieves maximum propagation
depth: the schema is committed once before any evidence runs, and the directive at Phase 5
routes the agent back to that definition rather than requiring schema reconstruction at
synthesis time. Outputs where the hypothesis resolution schema is defined only inline within
Phase 5 — without a pre-Phase-0 preamble definition and a corresponding fill-forward
directive — do not satisfy C-37.

**C-35 interaction note:** C-35 requires `Prior Confidence` in the Phase 5 resolution table.
C-37 requires that the full resolution schema be defined in the SCHEMA PREAMBLE before
Phase 0, with Phase 5 explicitly referencing it via a fill-forward directive. C-37 implies
C-35 (the preamble schema carries `Prior Confidence`, which propagates); C-35 does not imply
C-37. A Phase 5 table that carries `Prior Confidence` without a preamble definition passes
C-35 but fails C-37.

**C-34 interaction note:** C-34 requires confidence thresholds in the pre-Phase-0 schema
definition. C-37 requires the hypothesis resolution schema in the pre-Phase-0 preamble. Both
criteria use the SCHEMA PREAMBLE as the propagation mechanism but operate on different
schemas: C-34 on the confidence scale, C-37 on the hypothesis resolution table. They are
independent: a preamble can carry one schema without the other.

### C-38 — Column-specific FINDING REGISTER closure directives

Per-phase FINDING REGISTER closure directives (required by C-36) name the specific columns
being committed at that phase closure point (e.g., "Close FINDING REGISTER Phase 2 rows
[columns: FID, Finding Summary, Severity, Notes]"). Column-specific granularity enables
partial-fill detection: a reviewer can verify that each named column has been filled before the
phase gate closes, rather than treating the directive as a binary open/closed toggle. Outputs
where closure directives name only the phase and row set — without identifying which columns
are being committed — do not satisfy C-38.

**C-36 interaction note:** C-36 requires the existence of per-phase closure directives. C-38
requires those directives to enumerate the columns being committed. C-38 implies C-36;
C-36 does not imply C-38. A directive reading "Close FINDING REGISTER Phase 2 rows"
satisfies C-36 but fails C-38; a directive reading "Close FINDING REGISTER Phase 2 rows
[columns: FID, Finding Summary, Severity, Notes]" satisfies both.

**C-16 interaction note:** C-16 requires pre-seeding with all FID placeholders at document
top. C-38 column specificity applies at the per-phase closure point, not at pre-seed time.
The two criteria are independent: the pre-seed commits FID identity; the column-specific
closure directive commits which fields are filled per phase.

### C-39 — Fill-forward directive encoded as Phase 5 section-header gate annotation

The SCHEMA PREAMBLE fill-forward directive (required by C-37) is encoded as a formal
gate-style annotation in the Phase 5 section header itself (e.g.,
`[USE SCHEMA PREAMBLE DEFINITIONS FOR ALL PHASE 5 SUB-TABLES]`), rather than appearing
only as inline prose within Phase 5 body text or as a per-sub-table instruction. Placing the
directive at the phase-header level achieves maximum propagation: it is committed once at the
phase boundary and governs all Phase 5 sub-tables simultaneously — the agent cannot enter
Phase 5 without the directive being visible before any sub-table is constructed. Outputs where
the fill-forward directive appears only within a sub-table's schema definition or as prose below
the Phase 5 heading — but not in the Phase 5 section header itself — satisfy C-37 but do not
satisfy C-39.

**C-37 interaction note:** C-37 requires a fill-forward directive somewhere in Phase 5 pointing
back to the SCHEMA PREAMBLE. C-39 requires that directive to be encoded as a gate-style
header annotation on the Phase 5 section. C-39 implies C-37; C-37 does not imply C-39.
The annotation in the header is the strongest structural location: gate-level visibility precedes
all sub-table content, whereas an inline fill-forward directive is local to the sub-table where
it appears.

**C-14 / C-20 interaction note:** C-14 and C-20 require `[COMPLETE BEFORE PHASE N]` gate
annotations on all phase headers. C-39's preamble-reference annotation is a semantic directive,
not a completion gate — the Phase 5 header carries both annotations independently. C-14 and
C-20 are satisfied by the completion gate; C-39 is satisfied by the preamble-reference
annotation. Their coexistence in the same header is additive, not conflicting.

### C-40 — Bracket notation for FINDING REGISTER column-closure directives

Per-phase FINDING REGISTER closure directives that enumerate specific columns (required
by C-38) encode the column list using bracket notation: `[columns: FID, Finding Summary,
Severity, Notes]` (or equivalent bracketed enumeration). Bracket notation is structurally
distinct from the surrounding directive prose — the column list is delimited, not embedded
in a sentence — making it machine-parseable without regex parsing and enabling automated
partial-fill verification at each phase gate. Outputs where closure directives name specific
columns in prose sentence form (e.g., "fill Finding Summary, Severity, and Notes") satisfy
C-38 but do not satisfy C-40.

**C-38 interaction note:** C-38 requires column-specific closure directives (any form). C-40
requires those directives to use bracket notation specifically. C-40 implies C-38; C-38 does
not imply C-40. The variation axis between C-38 and C-40 is syntactic form: prose naming
satisfies C-38; bracket notation satisfies both. Both forms achieve partial-fill verifiability
in principle; bracket notation makes it structural rather than requiring natural-language
parsing.

**C-36 interaction note:** C-36 requires the existence of per-phase closure directives. C-40
adds a syntax requirement on the column enumeration within those directives. The implication
chain is C-40 → C-38 → C-36: each criterion implies the one below it.

### C-41 — Named-schema enumeration in Phase 5 fill-forward directive

The Phase 5 section-header fill-forward directive (required by C-39) names each SCHEMA
PREAMBLE schema individually rather than referencing all schemas collectively (e.g.,
`[SCHEMAS: hypothesis-resolution, recommendation-record, because-block — from SCHEMA PREAMBLE]`
rather than `[USE SCHEMA PREAMBLE DEFINITIONS FOR ALL PHASE 5 SUB-TABLES]`). Named
enumeration makes each fill-forward relationship individually verifiable: a reviewer confirms
that hypothesis-resolution, recommendation-record, and because-block schemas are each
resolved from the preamble definition, rather than inferring which schemas "all" applies to.
Outputs where the Phase 5 header directive references preamble schemas generically — without
naming each schema — satisfy C-39 but do not satisfy C-41.

**C-39 interaction note:** C-39 requires the fill-forward directive to appear in the Phase 5
section header. C-41 hardens the directive's content from a collective reference to a
per-schema enumeration. C-41 implies C-39; C-39 does not imply C-41. The distinction
is verifiability granularity: "all" is a single check that the directive exists; named enumeration
produces one independently verifiable relationship per schema.

**C-13 / C-35 / C-37 interaction note:** C-41 closes the propagation chain C-13 → C-35 →
C-37 → C-39 → C-41: prior anchored at Phase 0 (C-13), carried into Phase 5 resolution
(C-35), schema pre-defined in preamble (C-37), fill-forward in Phase 5 section header (C-39),
each preamble schema individually named in that directive (C-41). Each step raises verifiability
at a finer structural grain.

### C-42 — Per-column temporal commit annotation in bracket notation

Bracket notation column lists in FINDING REGISTER closure directives (required by C-40)
annotate each column with its temporal commit phase: `(fill-now)` for columns committed at
the current phase closure, and `(defer-to-Phase-5)` for columns whose values are deferred
to synthesis (e.g., `[columns: FID (key, fill-now), Actual Outcome (defer-to-Phase-5)]`).
Per-column temporal annotations convert closure directives into two-pass audit gates: at
Phase N close, a reviewer verifies that all `(fill-now)` columns are populated; at Phase 5
close, that all `(defer-to-Phase-5)` columns are populated. Outputs where bracket notation
column lists name columns without per-column temporal annotations satisfy C-40 but do not
satisfy C-42.

**C-40 interaction note:** C-40 requires bracket notation for the column list. C-42 requires
per-column temporal annotations within that bracket notation. C-42 implies C-40; C-40 does
not imply C-42. The variation axis between C-40 and C-42 is annotation depth: column
identity only satisfies C-40; column identity plus temporal commit phase satisfies both.

**C-28 interaction note:** C-28 requires the Phase 0 experiment table to encode which phase
fills each temporal column (Expected Result vs. Actual Outcome). C-42 extends this temporal
encoding from the Phase 0 table schema into the closure directive syntax, so the fill-now vs.
deferred distinction is auditable at every phase gate, not only at Phase 0 schema definition
time. The two criteria are independent: C-28 governs schema definition; C-42 governs
closure-directive annotation.

**C-36 / C-38 / C-40 interaction note:** The implication chain extends to C-42 → C-40 →
C-38 → C-36: per-phase closure exists (C-36), columns named (C-38), column list in bracket
notation (C-40), each column annotated with temporal commit phase (C-42).

### C-43 — Temporal commit encoded at SCHEMA PREAMBLE definition time

The SCHEMA PREAMBLE lifecycle schema (required by C-28) encodes `(fill-now)` and
`(defer-to-Phase-5)` annotations directly in the column headers at definition time (e.g.,
`| FID (key, fill-now) | Hypothesis (fill-now) | Actual Outcome (Phase 5, defer-to-Phase-5) |
Status (defer-to-Phase-5) |`), so the temporal commit role of each column is declared at the
point of schema definition rather than first appearing in downstream closure directives. When
encoded at preamble time, downstream closure directives inherit the temporal annotations as
confirmations — the fill-now / deferred distinction propagates automatically to every
downstream gate without redeclaration. Outputs where the SCHEMA PREAMBLE column headers
use phase-neutral parentheticals (e.g., "Expected Result (Phase 0)" / "Actual Outcome
(Phase 5)") rather than explicit `(fill-now)` / `(defer-to-Phase-5)` annotations satisfy C-28
but do not satisfy C-43.

**C-42 interaction note:** C-42 requires per-column temporal annotations in closure directive
bracket notation (gate-time declaration). C-43 moves the temporal declaration upstream to
the SCHEMA PREAMBLE (definition-time declaration). C-43 implies C-42: a schema with
preamble-time temporal encoding produces closure directives that confirm rather than declare,
which satisfies the C-42 annotation requirement structurally. C-42 does not imply C-43: a
document can annotate closure directives with `(fill-now)`/`(defer-to-Phase-5)` without
encoding those roles in the preamble column headers. The distinction is declaration point:
gate-time satisfies C-42; definition-time satisfies both.

**C-28 interaction note:** C-28 requires the Phase 0 experiment table to encode which phase
fills each temporal column, in any form. C-43 hardens the encoding to use explicit
`(fill-now)`/`(defer-to-Phase-5)` vocabulary in the preamble column headers specifically.
C-43 implies C-28; C-28 does not imply C-43.

**Propagation chain note:** C-43 extends the temporal-commit chain from C-28 → C-42 → C-43:
temporal columns identified in schema (C-28), fill-now vs. deferred annotated per column in
closure directives (C-42), fill-now vs. deferred encoded in preamble column headers so
propagation is automatic (C-43). Each step moves the declaration earlier in document lifecycle.

### C-44 — Per-phase minimum evidence count annotations

Phase section headers carry bracket-notation minimum evidence count annotations specifying
the floor for each phase before its gate can close (e.g., `[min: 3 experiments]` in the Phase 0
header, `[min: 1 inertia entry]` in Phase 1a, `[min: 2 named rivals]` in Phase 1b,
`[min: 1 named barrier]` in Phase 2, `[min: 1 segment with fit score]` in Phase 3,
`[min: 1 web-sourced entry with source and date]` in Phase 4). Minimum count annotations
create a header-level under-population failure class: a reviewer can determine by header scan
alone that a phase is complete, without counting table rows. Outputs where phase headers carry
gate annotations (satisfying C-14/C-20) but no minimum evidence count annotations do not
satisfy C-44.

**C-14 / C-20 interaction note:** C-14 and C-20 require `[COMPLETE BEFORE PHASE N]` gate
annotations on all phase headers. C-44's minimum count annotations are additive: the phase
header carries both the completion gate and the minimum count bracket in parallel. C-14 and
C-20 are satisfied by the completion gate; C-44 is satisfied by the minimum count bracket.
Their coexistence in the same header is additive, not conflicting.

**C-40 interaction note:** C-40 requires bracket notation in FINDING REGISTER closure
directives (column lists). C-44 requires bracket notation in phase section headers (evidence
counts). Both criteria use bracket notation as the structural mechanism, but at different
document locations: closure-directive column lists (C-40) vs. section-header gate annotations
(C-44). The two criteria are independent: either can be present without the other.

**C-27 interaction note:** When C-44 passes, under-population detection becomes header-scannable
without reading table body content. This extends C-27's prose-free structural sufficiency
from schema and gate verification to evidence quantity verification.

### C-45 — PRE-COMMITMENT block positioned before SCHEMA PREAMBLE

The output includes a PRE-COMMITMENT block that appears *before* the SCHEMA PREAMBLE,
capturing analyst hypotheses and prior beliefs in plain prose or plain-form table before any
schema column structure is visible. This creates a schema-free prior lock: because the analyst
commits prior beliefs before reading any column definitions, schema-conformance pressure
cannot shape the hypothesis content — the failure mode C-13 cannot prevent (C-13 only
requires `Prior Confidence` inside Phase 0 rows, which can be written while reading the
schema). The PRE-COMMITMENT block enables a three-point accountability chain: PRE-COMMITMENT
(prior locked before schema) → Phase 0 transcription (prior carried into structured hypothesis
table) → Phase 5 calibration delta (prior compared against evidence outcome). All three
structural points must be traceable for full satisfaction. Outputs that carry `Prior Confidence`
in Phase 0 rows without a pre-schema PRE-COMMITMENT block satisfy C-13 but do not satisfy
C-45.

**C-13 interaction note:** C-13 requires `Prior Confidence` in the Phase 0 schema before
evidence runs. C-45 moves the prior-commitment point upstream of the schema itself,
foreclosing schema-conformance pressure as a confound. C-45 implies C-13: a document with
a PRE-COMMITMENT block necessarily produces a Phase 0 prior-confidence record (via
transcription). C-13 does not imply C-45: a Phase 0 `Prior Confidence` column can be written
while reading the SCHEMA PREAMBLE — no schema-free lock is created.

**C-37 interaction note:** C-37 requires the hypothesis resolution schema to be defined in
the SCHEMA PREAMBLE before Phase 0. C-45 requires the PRE-COMMITMENT block to appear
before the SCHEMA PREAMBLE. The two criteria are independent: C-37 governs schema
propagation (preamble → Phase 5); C-45 governs prior isolation (pre-schema commitment).
A document can satisfy C-37 without C-45 (preamble schema with no pre-preamble commitment)
or C-45 without C-37 (pre-preamble commitment with inline Phase 5 schema). When both pass,
the document lifecycle reads: PRE-COMMITMENT (plain-form priors) → SCHEMA PREAMBLE
(schema definitions) → Phase 0 (structured experiments) → Phase 5 (calibration resolution).

**C-35 interaction note:** C-35 requires the prior-belief value from Phase 0 to appear in the
Phase 5 hypothesis resolution table. C-45 extends the prior chain one step earlier: the
plain-form prior from PRE-COMMITMENT is transcribed into Phase 0, then carried forward to
Phase 5. When C-45 passes, the prior is verifiable at three structural points rather than two.

### C-46 — Evidence density closure annotation (header-entry / footer-close audit pair)

After each evidence phase section (Phase 0 through Phase 4), the output includes an explicit
evidence density closure annotation in the form `Evidence density: [actual count] of [min] —
gate clears when actual >= min` (or equivalent). This annotation appears at the close of each
phase as a structural footer artifact, pairing with the C-44 minimum count bracket in the
phase section header to create a two-point audit per evidence phase: at phase entry, the
header declares the minimum (`[min: N ...]`); at phase close, the footer confirms the actual
count against that minimum. Under-population is therefore detectable without reading the
table body at *either* structural point — the header declares the floor, the footer confirms
the fill. Outputs that carry C-44 minimum count annotations in phase headers but provide no
corresponding density closure annotation at phase close satisfy C-44 but do not satisfy C-46.

**C-44 interaction note:** C-44 requires minimum count brackets in phase section headers
(header-entry audit point). C-46 requires a matching density closure annotation at phase close
(footer-close audit point). C-46 implies C-44: a density closure annotation (`actual of min`)
is meaningful only if the minimum was declared, which C-44 requires. C-44 does not imply
C-46: a header-level minimum annotation requires body-reading to verify the minimum was
met; the density closure annotation creates the structural confirmation artifact that makes
verification body-read-free at close time. The two criteria form an audit pair — neither is
redundant with the other.

**C-36 interaction note:** C-36 requires per-phase FINDING REGISTER closure directives
(instructing the agent to fill register rows before proceeding). C-46 requires per-phase
evidence density closure annotations (confirming the evidence count against the declared
minimum). Both criteria operate at phase close time but govern different artifacts: C-36 governs
register row completion; C-46 governs evidence quantity confirmation. They are independent:
either can be present without the other; when both pass, a phase close carries both a register
closure directive and a density confirmation.

**C-27 interaction note:** When C-46 passes alongside C-44, under-population detection is
fully body-read-free: the header declares the floor, the footer confirms the fill, and neither
requires counting table rows. This completes the extension of C-27's prose-free structural
sufficiency to evidence quantity verification — C-44 creates the entry-point check; C-46
creates the exit-point confirmation.

**Independence note (R18 V-04):** Combined preamble-time temporal encoding (C-43), per-phase
minimum evidence budgets (C-44), PRE-COMMITMENT prior lock (C-45), and density closure
(C-46) were confirmed independent and additive in R18 V-04/V-05 — no interaction degradation
when all four are present simultaneously.

### C-47 — PRE-COMMITMENT recommendation confidence with falsification condition

The PRE-COMMITMENT block (required by C-45) includes not only hypothesis priors but also
a recommendation confidence prior with a falsification condition: an explicit statement of the
analyst's expected final recommendation and the condition under which that recommendation
would be falsified (e.g., "Expected recommendation: COMMIT — falsified if Phase 2 surfaces
a blocking technical constraint or Phase 1a Switching Cost rates H for more than one segment").
The Phase 5 recommendation record schema is extended with a `Prior Recommendation
Confidence (from PRE-COMMITMENT)` column, enabling an explicit before/after recommendation
delta at synthesis time: the prior confidence locked before schema exposure is compared against
the post-evidence recommendation confidence at Phase 5. Outputs where the PRE-COMMITMENT
block captures hypothesis priors but no recommendation prior with falsification condition, and
where the Phase 5 recommendation record omits the `Prior Recommendation Confidence`
column, satisfy C-45 but do not satisfy C-47.

**C-45 interaction note:** C-45 requires a PRE-COMMITMENT block before the SCHEMA PREAMBLE
capturing hypothesis priors. C-47 extends that block to also capture recommendation confidence
with a falsification condition. C-47 implies C-45: a PRE-COMMITMENT block with recommendation
prior necessarily satisfies C-45. C-45 does not imply C-47: a PRE-COMMITMENT block with
hypothesis priors only satisfies C-45 but not C-47.

**C-18 interaction note:** C-18 requires the Phase 5 recommendation record to carry exactly
four named columns (FID, Recommendation, Confidence, Confidence Rationale). C-47 adds a
fifth column (`Prior Recommendation Confidence (from PRE-COMMITMENT)`) as an upward
structural extension. The four required C-18 columns remain present and are not renamed;
C-18's stated fail condition (missing or renamed required columns) is not triggered. C-47 and
C-18 are independent: C-18 governs minimum column completeness; C-47 governs the prior
delta column that enables before/after recommendation comparison.

**C-35 interaction note:** C-35 requires the hypothesis prior-belief value from Phase 0 to
appear in Phase 5 for calibration delta. C-47 applies the same pattern to the recommendation:
the recommendation confidence prior locked in PRE-COMMITMENT is carried forward to Phase 5
as a delta column. The two criteria are parallel in structure but independent in subject:
C-35 governs hypothesis-resolution delta; C-47 governs recommendation-confidence delta.
When both pass, Phase 5 presents two prior-versus-evidence deltas: one per hypothesis
(C-35) and one for the overall recommendation (C-47).

### C-48 — FINDING REGISTER expected FID count annotations (three-point count chain)

The FINDING REGISTER pre-seeded at document top (required by C-16) includes bracket-notation
`[expect: N FIDs]` annotations in each phase-group header within the register, aligned to the
minimum evidence counts declared in the corresponding phase section headers by C-44 (e.g.,
the Phase 0 block in the FINDING REGISTER header reads `Phase 0 [expect: 3 FIDs — aligned
to min: 3 experiments]`). This creates a three-point count chain: (1) C-44 phase section header
declares the minimum evidence floor; (2) FINDING REGISTER phase-group header declares the
expected FID count, making FID budget explicit at pre-seed time; (3) C-46 phase close footer
confirms the actual count. The chain is verifiable at all three structural points without body-reading.
Outputs where the FINDING REGISTER phase-group headers are unlabeled or carry only phase
identifiers — without `[expect: N FIDs]` aligned to C-44 minimums — satisfy C-16 but do not
satisfy C-48.

**C-16 interaction note:** C-16 requires the FINDING REGISTER to be pre-seeded at document
top before any evidence phase. C-48 adds expected FID count annotations to the register's
phase-group headers, making the FID budget explicit at pre-seed time. C-48 implies C-16;
C-16 does not imply C-48.

**C-44 interaction note:** C-44 requires per-phase minimum evidence count brackets in phase
section headers. C-48 requires the FINDING REGISTER phase-group headers to carry aligned
`[expect: N FIDs]` annotations. Both criteria use the same minimum count values; C-48
propagates that count into the register structure, creating a two-location declaration (phase
header + register header) before C-46 confirms at phase close. The three criteria form a
count chain: C-44 (phase header minimum) → C-48 (register header expected count) → C-46
(phase footer actual count).

**C-46 interaction note:** C-46 creates the footer-close confirmation (third point in the count
chain). C-48 creates the register-header declaration (second point). C-44 creates the
section-header floor (first point). All three are independent: the chain can be broken at any
point. When all three pass, evidence quantity is verifiable at three structural locations —
entry header, register header, close footer — without any body-reading.

### C-49 — Phase 5 synthesis completeness exit annotation

Phase 5 closes with an explicit synthesis completeness annotation naming each of the four
required sub-tables and confirming its population status (e.g.,
`Synthesis completeness: [hypothesis-resolution: filled | recommendation-record: filled |
counter-evidence: filled | open-questions: filled]`). This annotation appears as a structural
footer at the close of Phase 5 — the exit-point complement to the Phase 5 section-header
gate annotation required by C-39. It confirms that all four sub-tables have been populated
before the document closes, surfacing any skipped or empty sub-table at a single scannable
point. Outputs where Phase 5 ends after the last sub-table without a synthesis completeness
annotation satisfy C-30 (which verifies that bold labels precede each sub-table) but do not
satisfy C-49.

**C-30 interaction note:** C-30 requires each Phase 5 sub-table to carry a bold named label
immediately preceding the table, confirming structural presence at entry time. C-49 requires
a synthesis completeness annotation at Phase 5 close, confirming population status at exit
time. C-30 creates the per-table entry-point check; C-49 creates the aggregate exit-point
check. The two criteria form an entry/exit audit pair for Phase 5 sub-tables, parallel to the
C-44 (header minimum) / C-46 (footer density) audit pair for evidence phases. C-30 can pass
if all four bold labels are present but sub-table bodies are empty; C-49 would then fail (empty
status). Both criteria are required for full Phase 5 structural verification.

**C-46 interaction note:** C-46 requires per-phase evidence density closure annotations at
phase close for Phase 0–4 (confirming evidence quantity). C-49 requires a synthesis
completeness annotation at Phase 5 close (confirming sub-table population). Both are
phase-close footer artifacts; C-46 governs evidence phases, C-49 governs the synthesis phase.
They are structurally parallel and independent: either can be present without the other.

**C-39 interaction note:** C-39 requires the SCHEMA PREAMBLE fill-forward directive to be
encoded as a gate-style annotation in the Phase 5 section header (entry-point). C-49 requires
the synthesis completeness annotation at Phase 5 close (exit-point). Together they bracket
Phase 5 at both ends: C-39 at the header gate (entry), C-49 at the completeness annotation
(exit). Their coexistence is additive, not conflicting.

**Independence note (R19 V-05):** PRE-COMMITMENT recommendation confidence (C-47),
FINDING REGISTER expected FID count chain (C-48), and Phase 5 synthesis completeness
exit annotation (C-49) were confirmed independent and additive in R19 V-05 — no interaction
degradation when all three are present simultaneously alongside the full C-01..C-46 baseline.

### C-50 — Phase gate check status annotation (three-field go/no-go verdict)

After each evidence phase close, following the C-46 evidence density annotation, the output
includes an explicit gate check status line in bracket notation:
`Gate check: [min met? Y/N] | [FIDs closed? Y/N] | [Proceed? Y/N]` (or equivalent
three-field form). This gate check converts the C-46 count comparison into a binary
proceed decision and simultaneously confirms FINDING REGISTER closure for the phase —
the reviewer reads `Proceed: Y` rather than computing whether actual >= min and separately
verifying the register closure directive. The three fields are individually verifiable: the
first maps to C-44 minimum satisfaction; the second maps to C-36 register closure; the
third is the composite go/no-go verdict. Outputs where phase close carries C-46 density
annotations but no gate check status line satisfy C-46 but do not satisfy C-50.

**C-46 interaction note:** C-46 requires a density closure annotation (`actual of min`) at
phase close. C-50 requires a gate check line immediately following that annotation, encoding
the proceed verdict in bracket notation. C-50 implies C-46: a gate check `[min met? Y/N]`
is only meaningful if the density count was declared, which C-46 requires. C-46 does not
imply C-50: a density annotation is a count confirmation; the gate check converts that
confirmation into an explicit binary decision. The two lines together form a two-line
phase-close block — count and verdict — where C-46 supplies the arithmetic and C-50
supplies the decision.

**C-36 interaction note:** C-36 requires per-phase FINDING REGISTER closure directives.
C-50's second field (`FIDs closed? Y/N`) encodes the closure status of that directive as a
scannable binary annotation. When C-50 passes, register closure is verifiable at phase close
without locating the C-36 directive. The two criteria are independent: C-36 governs the
existence of the closure directive; C-50 governs the status confirmation that pairs with it.

**C-44 interaction note:** C-44 requires minimum count brackets in phase section headers.
C-50's first field (`min met? Y/N`) is the per-phase verdict on C-44 satisfaction at close
time — converting the header-declared floor into a binary pass/fail at the close footer.
The three criteria form a three-part phase audit: C-44 declares the minimum (entry), C-46
confirms the count (close), C-50 renders the verdict (close, second line).

**C-27 interaction note:** When C-50 passes alongside C-44 and C-46, phase-ready determination
is fully body-read-free and arithmetic-free: the header declares the floor (C-44), the footer
confirms the fill (C-46), and the gate check renders the binary verdict (C-50). This extends
C-27's prose-free structural sufficiency to phase-gate decision verification.

### C-51 — Recommendation delta sentence after recommendation record table

Immediately following the Phase 5 recommendation record table (after the last row, before
the next sub-table), the output includes an explicit recommendation delta sentence capturing
the before/after shift from the PRE-COMMITMENT recommendation prior to the post-evidence
recommendation (e.g., "Recommendation held at COMMIT — confidence increased from M to H;
falsification condition not triggered." or "Recommendation shifted from COMMIT (prior) to
PAUSE — Phase 2 barrier triggered the falsification condition."). The delta sentence converts
the C-47 `Prior Recommendation Confidence (from PRE-COMMITMENT)` column comparison
into a standalone scannable statement: the reviewer assesses recommendation movement by
reading one sentence rather than comparing two column values across table rows. The
falsification condition outcome must be explicitly named — triggered or not triggered —
making C-47's falsification condition verifiable at a glance without re-reading the PRE-COMMITMENT
block. Outputs where the Phase 5 recommendation record carries the C-47 `Prior Recommendation
Confidence` column but no standalone delta sentence satisfy C-47 but do not satisfy C-51.

**C-47 interaction note:** C-47 requires the PRE-COMMITMENT block to include a recommendation
prior with falsification condition, and the Phase 5 recommendation record to carry a
`Prior Recommendation Confidence` column. C-51 requires a delta sentence after that table
that makes the before/after shift and falsification condition outcome scannable in natural
language. C-51 implies C-47: a delta sentence naming the prior recommendation and
falsification outcome is only structurally coherent if C-47's prior column and falsification
condition are present. C-47 does not imply C-51: the `Prior Recommendation Confidence`
column enables a table-based comparison; the delta sentence makes that comparison
body-read-free. The variation axis between C-47 and C-51 is output form: column comparison
(C-47) vs. standalone sentence (C-51).

**C-35 interaction note:** C-35 requires the hypothesis prior-belief value from Phase 0 to
appear in Phase 5 for per-hypothesis calibration delta. C-51 creates the parallel mechanism
for the recommendation: a standalone sentence surfaces the recommendation-level delta at
a single scannable point. The two criteria are structurally parallel and independent: C-35
governs hypothesis-resolution delta (table-column form); C-51 governs recommendation-level
delta (sentence form). When both pass, Phase 5 surfaces calibration deltas at both the
hypothesis level (table) and the recommendation level (sentence).

**C-49 interaction note:** C-49 requires a synthesis completeness annotation at Phase 5 close,
confirming all four sub-tables are populated. C-51 requires a delta sentence after the
recommendation record table (a mid-Phase-5 structural artifact, not a close footer). The
two criteria are independent: C-49 governs Phase 5 exit completeness; C-51 governs
recommendation-level delta legibility within Phase 5. Their coexistence is additive.

### C-52 — Phase 3 Inertia Lock-in column

Phase 3 (scout-market) segment table includes an `Inertia Lock-in (H/M/L)` column alongside
the fit score column required by C-12, capturing the degree to which each market segment
is behaviorally locked into the status quo. This extends the Phase 1a switching cost concept
(C-31) from the competitor level to the market segment level: each segment is scored on both
market attractiveness (Fit Score) and behavioral switching resistance (Inertia Lock-in),
enabling segment prioritization that accounts for acquisition difficulty alongside strategic fit.
A high-fit segment with high inertia lock-in is structurally differentiated from a high-fit
segment with low lock-in — the column encodes that distinction at Phase 3 so the Because
block Phase 3 citation can surface it at synthesis. When C-44 is in effect, the Phase 3
section header `[min: ...]` annotation is updated to reflect both dimensions (e.g.,
`[min: 1 segment with fit score and inertia lock-in]`). Outputs where Phase 3 carries a
Fit Score column (C-12) but no Inertia Lock-in column satisfy C-12 but do not satisfy C-52.

**C-12 interaction note:** C-12 requires a numeric fit or attractiveness score column in the
Phase 3 table. C-52 requires an additional `Inertia Lock-in (H/M/L)` column in that same
table. C-52 implies C-12: a Phase 3 table with Inertia Lock-in necessarily carries segment
scoring as well. C-12 does not imply C-52: a Phase 3 table can carry Fit Score without
Inertia Lock-in. The two columns are complementary dimensions — attractiveness and
switching resistance — and together produce a two-axis segment classification.

**C-31 interaction note:** C-31 requires the Phase 1a FINDING REGISTER to carry a
`Switching Cost (H/M/L)` column, capturing the behavioral cost of abandoning the status
quo at the competitor level. C-52 propagates the same switching-resistance concept to the
Phase 3 market segment level. The two criteria are independent: C-31 governs Phase 1a
register schema; C-52 governs Phase 3 table schema. When both pass, switching resistance
is quantified at two structural levels — competitor (C-31) and market segment (C-52) —
enabling the Because block to connect inertia primacy (Phase 1a) to segment-level lock-in
(Phase 3) with FID citations at both levels.

**C-44 interaction note:** C-44 requires per-phase minimum evidence count annotations in
section headers. When C-52 is in scope, the Phase 3 `[min: ...]` annotation reflects the
Inertia Lock-in column as a required dimension of each qualifying entry (e.g., `[min: 1 segment
with fit score and inertia lock-in]`). The C-44 minimum count bracket is updated to name
both columns, making the combined C-12/C-52 requirement header-scannable. C-44 does not
imply C-52: a Phase 3 header can carry `[min: 1 segment with fit score]` (C-44 only) without
naming Inertia Lock-in; C-52 requires the column to be present in the table and reflected in
the minimum annotation.

**Independence note (R20 V-05):** Phase gate check status annotation (C-50), recommendation
delta sentence (C-51), and Phase 3 Inertia Lock-in column (C-52) were confirmed independent
and additive in R20 V-05 — no interaction degradation when all three are present simultaneously
alongside the full C-01..C-49 baseline.
