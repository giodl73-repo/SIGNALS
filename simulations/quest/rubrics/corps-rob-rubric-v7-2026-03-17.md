# corps-rob rubric v7 -- 2026-03-17

## Change Log

| Version | Change |
|---------|--------|
| v1 | C-01 -- C-08: essential (x5) + recommended (x3) |
| v2 | C-09 -- C-10: inter-stage blocker detection, cross-cutting theme elevation |
| v3 | C-11 -- C-12: handoff packet, stage-boundary blocker field |
| v4 | C-13 -- C-18: inertia anchor, briefing envelope, anti-redundancy, lens-impact/risk-shift pair + guard, explicit lens fill field |
| v5 | C-19 -- C-23: Stage 1 lens coverage, pre-envelope Part 0 block, KEY CONCERNS back-ref, three-hop chain, chain health summary. N_aspirational 10 -> 15. |
| v6 | C-24 -- C-26: fill-slot structural completeness, displacement map with D-IDs, table-first findings format. N_aspirational 15 -> 18. |
| v7 | C-27 -- C-29: D-ID Ref column structural obligation, named anti-pattern rejection phrases in D-ID Ref guard, explicit scope-exception calibration for table-first format. N_aspirational 18 -> 21. |

---

## New in v7 -- What was extracted from the R7 scorecard

| ID | Name | Source | Mechanism |
|----|------|--------|-----------|
| C-27 | D-ID Ref Column as Per-Row Structural Obligation | V-01 R7, V-04 R7, V-05 R7 (C-25 PASS) vs V-02 R7, V-03 R7 (C-25 PARTIAL) | Findings table requires a dedicated D-ID Ref column as a 6th typed slot. When Inertia Stance is RESISTANT and Severity is HIGH, the cell must contain a D-ID from the Displacement Map register; otherwise N/A. Converts C-25's per-finding citation requirement from a prose Inertia Check note -- where "reference the inertia contribution as a factor" satisfies the wording without naming a D-ID -- into a per-row cell obligation that an executing model cannot satisfy without a specific register entry. V-02 and V-03 drifted to the prose form because no column existed to fill. |
| C-28 | Named Anti-Pattern Rejection Phrases in D-ID Ref Column Guard | V-04 R7, V-05 R7 (D-ID Ref column guard carries per-cell named rejection) | The D-ID Ref column guard names at least one explicit invalid cell value and rejects it by condition -- e.g., "N/A does not satisfy when Inertia Stance is RESISTANT and Severity is HIGH." Extends C-24/C-26's [fill]-with-rejection-language pattern into the D-ID Ref cell specifically: naming a borderline-valid response (N/A is syntactically valid; it is not semantically valid under RESISTANT+HIGH) closes the gap between structural presence and citation compliance. Distinguished from V-01's table-level footer by appearing inline in the column template, where it is visible to a model reading the column guide rather than the table footer. Requires C-27 (N/A when C-27 absent). |
| C-29 | Explicit Scope-Exception Calibration for Table-First Format | V-05 R7 (calibration table per C-05/C-26 scorecard evidence) | Template contains a named calibration section identifying output types exempt from C-26's table-first findings format, with rationale for each. GO/NO-GO signal is the canonical exempt type: unambiguous labeled signals are degraded, not improved, by tabular rendering. The section closes the table-first architecture by making the exception boundary explicit in the template itself rather than only in the rubric's design note. Requires C-27 (N/A when C-27 absent -- meaningful only within the 6-column architecture that introduces the conditional format-failure family and therefore requires a defined scope boundary). |

**Scoring change:** N_aspirational 18 -> 21. Max contributable to composite still 10 (ceiling = 100). Raw count (max 21) is the tie-break.

**Re-grades under v7:**
- V-05 R6 (prior overall leader): C-27 FAIL, C-28 N/A, C-29 N/A -> 18 raw / 10 contributable -> **100** (tie-break 18, unchanged from v6)
- V-02 R7 / V-03 R7 (no D-ID Ref column): C-27 FAIL -> C-28 N/A, C-29 N/A -> 17.5 raw -> **100**; tie-break 17.5 (unchanged)
- V-01 R7 (one axis -- D-ID Ref column, table-level footer only): C-27 PASS, C-28 FAIL, C-29 FAIL -> 19 raw -> **100**; tie-break 19
- V-04 R7 (two axes -- D-ID Ref column + named per-cell rejection): C-27 PASS, C-28 PASS, C-29 FAIL -> 20 raw -> **100**; tie-break 20
- V-05 R7 (all three axes): C-27 PASS, C-28 PASS, C-29 PASS -> 21 raw -> **100**; tie-break 21 -- new leader

**Design note:** The three R7 axes form a progressive strengthening chain on the D-ID citation mechanism introduced by C-25. C-27 provides the structural column (the cell exists and must be filled or explicitly N/A). C-28 provides named-anti-pattern rejection in the column guard (the cell cannot be satisfied with a borderline-valid value under the RESISTANT+HIGH condition). C-29 closes the table-first architecture by naming what falls outside it (preventing over-application of C-26 to signal types where tabular rendering degrades rather than enforces clarity). Each criterion requires the previous: C-28 strengthens C-27's column guard; C-29 is meaningful only when the 6-column architecture has introduced a conditional format-failure family that requires a scope boundary. The progressive chain explains the R7 ordering: V-01 introduces the D-ID Ref column (C-27 alone); V-04 -- as the V-01+V-02 combination -- applies V-02's named-anti-pattern technique to the D-ID Ref cell (C-28 added); V-05 completes the architecture with explicit scope-exception calibration (C-29 added). V-02 and V-03 lack C-27, making C-28 and C-29 N/A regardless of other patterns present. The GO/NO-GO signal exemption in C-26's design note is now promoted from rubric annotation to template-level calibration by C-29.

---

## Scoring Formula

| Band | Criteria | Max pts |
|------|----------|---------|
| Essential | C-01 -- C-05 | 5 x 12 = 60 |
| Recommended | C-06 -- C-08 | 3 x 10 = 30 |
| Aspirational | C-09 -- C-29 | N_pass (max contributable = 10) |

**PARTIAL = 0.5 pass. Ceiling = 100.**

Aspirational score = N_pass (each full pass = 1 point, PARTIAL = 0.5 pts).
Max contributable to composite = 10. Raw count max = 21 (tie-break when composite = 100).

**Any essential failure = not golden regardless of composite.**

---

## Essential Criteria

*All five must pass for golden. Each is worth 12 points. PARTIAL = 6 pts.*

---

### C-01 -- Stage Attribution
- **Category**: format
- **Weight**: essential
- **Text**: Every stage in the output has an explicit, non-anonymous attribution to a canonical label (`leadership`, `teams`, `pm`, `tpm`, `arch-board`, `exec-office`). Each stage section is headed by both the stage name and the role conducting it. No stage is anonymous and no stage is silently merged with another.
- **Pass condition**: Every stage run has a section header containing the canonical stage name and the name or role title of the assigned persona. Labels must match the six canonical names exactly -- no substitutions or abbreviations.

---

### C-02 -- Role-Loaded Perspective
- **Category**: correctness
- **Weight**: essential
- **Text**: Each stage review reflects the documented lens of the persona loaded from `.roles/` via `org.yaml` -- not a generic review any role could have written. The role's orientation shapes which concerns are surfaced and how they are framed.
- **Pass condition**: At least one finding per stage is grounded in the loaded persona's specific lens (e.g., a TPM flags schedule risk and dependency gaps, a Principal Architect flags interface coupling, a PM flags adoption risk, a Chief of Staff flags mission alignment). Findings that are fully generic -- applicable by any reviewer to any topic -- do not satisfy this criterion for any stage in which they appear.

---

### C-03 -- Finding Specificity
- **Category**: correctness
- **Weight**: essential
- **Text**: Each finding names the specific artifact, mechanism, or behavior at issue -- not a category label. "Dependency risk" is a category; "Stage 3 lacks a dependency map for the auth-service migration, and Stage 4's schedule assumes its completion" is a finding. Category-only findings cannot be actioned.
- **Pass condition**: No finding in any stage uses only a category label without identifying the specific artifact or behavior. Template inline guard: "name the specific artifact or behavior -- not a category label" must appear in the Finding column.

---

### C-04 -- Ownership Floor
- **Category**: correctness
- **Weight**: essential
- **Text**: At least 50% of findings across all stages have an identified owner (a named role, team, or function). TBD is not an owner. Unowned findings are findings that have not been reviewed; they cannot be tracked to resolution.
- **Pass condition**: Count of findings with a non-TBD owner >= 50% of total findings. Owner column template explicitly rejects "TBD" -- the column guard must include language such as "TBD does not satisfy."

---

### C-05 -- GO/NO-GO Signal
- **Category**: format
- **Weight**: essential
- **Text**: The TPM stage produces a labeled, unambiguous GO/NO-GO signal using one of three canonical values: GO, GO WITH CONDITIONS, NO-GO. The signal appears as a standalone labeled output -- not embedded in prose, not rendered as a table cell. Unambiguous labeled signals are degraded, not improved, by tabular rendering.
- **Pass condition**: `**TPM GO/NO-GO: [fill: GO / GO WITH CONDITIONS / NO-GO]**` present as a standalone labeled output in the TPM stage. No other rendering is acceptable. This output is explicitly exempt from C-26's table-first scope.

---

## Recommended Criteria

*Each is worth 10 points. PARTIAL = 5 pts.*

---

### C-06 -- Cross-Stage References
- **Category**: correctness
- **Weight**: recommended
- **Text**: The review contains structured cross-stage references using typed relationship labels: confirms, escalates, contradicts. Each reference names the source stage and the specific finding being referenced. Generic "see Stage 2" citations do not satisfy.
- **Pass condition**: At least 2 cross-stage references total, rendered in a structured table. Each reference carries a typed label from {confirms, escalates, contradicts} and identifies the source stage and finding.

---

### C-07 -- Handoff Packet
- **Category**: format
- **Weight**: recommended
- **Text**: Each stage produces a handoff packet containing both a Cross-Stage Synthesis and a Downstream Risk Shift. The Downstream Risk Shift is a projection of how current-stage findings change risk for the next stage -- not a copy of those findings.
- **Pass condition**: Cross-Stage Synthesis and Downstream Risk Shift both present in each stage's handoff packet. Anti-copy constraint enforced in template: Downstream Risk Shift must not restate current-stage findings verbatim.

---

### C-08 -- ROB Summary
- **Category**: format
- **Weight**: recommended
- **Text**: The ROB concludes with an Overall Verdict, an Inertia Resolution statement, and a Cross-Cutting Themes section. These three elements together constitute the minimum viable ROB summary output.
- **Pass condition**: All three elements present. Overall Verdict carries a labeled disposition. Cross-Cutting Themes names recurring themes with their recurrence count or stage evidence. Inertia Resolution states the disposition of the inertia forces identified in the body.

---

## Aspirational Criteria

*Each full pass = 1 point; PARTIAL = 0.5 pts. Max contributable = 10. Raw count max = 21 (tie-break).*

---

### C-09 -- Inter-Stage Blocker Detection
- **Category**: correctness
- **Weight**: aspirational
- **Text**: The ROB explicitly identifies findings that block subsequent stages from proceeding. A blocker is a finding in stage N that makes stage N+1 execution invalid or misleading until resolved. Blockers must be identified at the time the finding is recorded, not only in the ROB summary.
- **Pass condition**: Blocker Field table present per stage, identifying YES/NO blocker status, the specific downstream stage blocked, and the reason the dependency exists.

---

### C-10 -- Cross-Cutting Theme Elevation
- **Category**: correctness
- **Weight**: aspirational
- **Text**: Findings that surface independently across multiple stages are elevated to Cross-Cutting Themes. The elevation is explained by recurrence -- a finding pattern appearing in three stages carries more signal than the same finding in one stage. Themes named without recurrence evidence are not elevated, they are repeated.
- **Pass condition**: Cross-Cutting Themes table present. Each theme names the stages in which it recurred. Elevation rationale explicitly references recurrence count or pattern.

---

### C-11 -- Handoff Packet Substance
- **Category**: correctness
- **Weight**: aspirational
- **Text**: The handoff packet's Forwarded Refs field names specific findings from the current stage being forwarded downstream -- not generic stage summaries. The substance constraint closes the gap between structural presence (C-07) and actionable handoff content.
- **Pass condition**: Forwarded Refs, Cross-Stage Synthesis, and Downstream Risk Shift all present with substance constraint: each must reference specific findings by ID or sufficiently descriptive label. "See findings above" does not satisfy.

---

### C-12 -- Stage-Boundary Blocker Field
- **Category**: format
- **Weight**: aspirational
- **Text**: Each stage contains an explicit stage-boundary Blocker Field as a structured table element. The field forces a YES/NO determination at each boundary, preventing blockers from remaining implicit until the ROB summary.
- **Pass condition**: Blocker Field table present at each stage boundary. Contains YES/NO indicator, downstream stage identifier, and reason. All three sub-fields must be filled; partial population does not satisfy.

---

### C-13 -- Inertia Anchor
- **Category**: correctness
- **Weight**: aspirational
- **Text**: The ROB contains an INERTIA ANCHOR section documenting the displacement forces acting on the feature. The anchor includes a numbered Displacement Map register (D-01, D-02 ...) identifying each inertia source by name and type. Stages that declare RESISTANT Inertia Stance must reference this register.
- **Pass condition**: INERTIA ANCHOR section present. Displacement Map register contains at least one numbered D-ID entry. Stages with Inertia Stance RESISTANT reference at least one D-ID by register number.

---

### C-14 -- Briefing Envelope
- **Category**: format
- **Weight**: aspirational
- **Text**: Stages 2 through 6 include a Part 1 BRIEFING ENVELOPE that provides the reviewing persona with ROLE, LENS, KEY CONCERNS, and PRIOR-STAGE ESCALATIONS before the persona encounters the feature content. The envelope isolates lens activation from prior-stage contamination.
- **Pass condition**: Part 1 BRIEFING ENVELOPE present for each of Stages 2-6. All four fields (ROLE, LENS, KEY CONCERNS, PRIOR-STAGE ESCALATIONS) present and individually filled.

---

### C-15 -- Anti-Redundancy
- **Category**: correctness
- **Weight**: aspirational
- **Text**: The Downstream Risk Shift must not restate the Prior-Stage Lens Impact. The two sections serve distinct purposes: Prior-Stage Lens Impact records what the current stage found (retrospective); Downstream Risk Shift projects how those findings change risk for the next stage (prospective). Restating one as the other collapses the retrospective/prospective split.
- **Pass condition**: Template carries an explicit prohibition: "Do not restate Prior-Stage Lens Impact" (or equivalent) inline in the Downstream Risk Shift slot.

---

### C-16 -- Lens-Impact/Risk-Shift Pair
- **Category**: format
- **Weight**: aspirational
- **Text**: Every stage contains both a Prior-Stage Lens Impact table and a Downstream Risk Shift slot as a structural pair. The pair enforces the retrospective/prospective split structurally -- omitting either element removes a required analytical dimension from the stage.
- **Pass condition**: Both Prior-Stage Lens Impact table and Downstream Risk Shift slot present in every stage section.

---

### C-17 -- Lens-Impact/Risk-Shift Guard
- **Category**: format
- **Weight**: aspirational
- **Text**: The template carries an inline constraint preventing Downstream Risk Shift from restating Prior-Stage Lens Impact. The constraint must appear in the template itself, not only in the rubric. An executing model that has not read the rubric must still encounter the constraint.
- **Pass condition**: "Do not restate Prior-Stage Lens Impact" constraint (or equivalent) appears inline in the Downstream Risk Shift template slot.

---

### C-18 -- Explicit Lens Fill Field
- **Category**: format
- **Weight**: aspirational
- **Text**: Part 0 contains a Dimension field requiring the persona's lens to be stated as an analytical orientation (scope, risk axis, constraint type) rather than a role title. "Principal Architect" is a title; "Interface coupling and long-term maintainability" is a dimension. The field guides the persona toward the Part 0 commitment that drives the three-hop chain.
- **Pass condition**: Dimension field present in Part 0. Template rejection guidance states that role title alone does not satisfy the Dimension field.

---

### C-19 -- Stage 1 Lens Coverage
- **Category**: format
- **Weight**: aspirational
- **Text**: Stage 1 lacks a Briefing Envelope by design (it is the initial stage with no prior-stage context to envelope). The lens dimension requirement must therefore be enforced in Stage 1's Stage Identity field explicitly. Without this instruction, Stage 1 persona declarations default to title-only.
- **Pass condition**: Stage 1 Stage Identity field carries the instruction "(Must contain dimension, not just title.)" or equivalent.

---

### C-20 -- Part 0 Pre-Envelope Block
- **Category**: format
- **Weight**: aspirational
- **Text**: Part 0 (Lens Activation) appears as a mandatory pre-reading block before Part 1 (Briefing Envelope). The persona must commit to a lens in Part 0 before encountering any prior-stage context in Part 1. Reversing this order allows prior-stage context to contaminate the lens declaration.
- **Pass condition**: `### Part 0 -- LENS ACTIVATION / Fill before reading any prior-stage context.` heading present (or equivalent that explicitly establishes the pre-envelope sequence).

---

### C-21 -- KEY CONCERNS Back-Reference
- **Category**: correctness
- **Weight**: aspirational
- **Text**: The KEY CONCERNS field in the Briefing Envelope traces back to the lens declared in Part 0. Concerns selected through a different lens, or without traceability to Part 0, break the first hop of the three-hop chain. A KEY CONCERNS list that does not reference Part 0 is anonymous with respect to the activating lens.
- **Pass condition**: KEY CONCERNS cell contains the phrase "selected through the Lens declared in Part 0" verbatim, or equivalent phrasing with the same explicit back-reference to Part 0.

---

### C-22 -- Three-Hop Chain
- **Category**: correctness
- **Weight**: aspirational
- **Text**: The Prior-Stage Lens Impact table names "the orientation declared in Part 0" as the governing lens for impact assessment. This closes the three-hop chain: (1) Part 0 declares lens; (2) Briefing Envelope KEY CONCERNS selected through Part 0 lens; (3) Prior-Stage Lens Impact assessed through Part 0 orientation. Breaking hop 3 reduces the chain to a two-hop sequence that does not trace impact back to the original lens commitment.
- **Pass condition**: Prior-Stage Lens Impact table template or its instructions reference "the orientation declared in Part 0" as the governing lens for impact assessment.

---

### C-23 -- Chain Health Summary
- **Category**: format
- **Weight**: aspirational
- **Text**: The ROB includes a LENS ACTIVATION CHAIN HEALTH summary table covering all six stages. The table provides a single-view audit of lens traceability across the full ROB -- confirming that each stage declared a lens, traced KEY CONCERNS to Part 0, and assessed Prior-Stage Lens Impact through Part 0 orientation. Without this summary, chain failures are detectable only by reading every stage individually.
- **Pass condition**: LENS ACTIVATION CHAIN HEALTH table present with one row per stage (6 rows total), covering at minimum: stage name, lens declared (yes/no), KEY CONCERNS back-referenced (yes/no), Prior-Stage Lens Impact traced to Part 0 (yes/no or N/A for Stage 1).

---

### C-24 -- Finding Slot Structural Completeness
- **Category**: format
- **Weight**: aspirational
- **Text**: All finding slots (severity, owner, resolution) are declared as mandatory `[fill]` fields with inline rejection language. The template enforces completeness at the format level: an absent slot is a format failure, not a prose quality gap. Converts C-04's 50% ownership floor into a per-finding structural guarantee -- ownership is not an aggregate target but a per-row requirement.
- **Pass condition**: All typed finding columns carry `[fill]` with inline rejection language. Template does not permit free-text omission of any typed slot. Absent slot = format failure (not a scoring deduction applied post-hoc).

---

### C-25 -- Displacement Map with Labeled D-IDs
- **Category**: correctness
- **Weight**: aspirational
- **Text**: The INERTIA ANCHOR section contains a numbered displacement register (D-01, D-02 ...). When a stage's Inertia Stance is RESISTANT and a finding carries HIGH severity, the finding must cite a D-ID from the register. Escalates C-13 from prose anchor to machine-scannable register with finding-level citations. A RESISTANT stage that does not produce D-ID-cited HIGH findings has acknowledged inertia abstractly but not concretely.
- **Pass condition**: INERTIA ANCHOR contains a numbered Displacement Map register. At least one D-ID defined. When Inertia Stance is RESISTANT and Severity is HIGH, the finding cites a D-ID from the register by number. N/A when C-13 absent.

---

### C-26 -- Table-First Findings Format with Inline Rejection Guards
- **Category**: format
- **Weight**: aspirational
- **Text**: All stage findings are rendered in a structured table with mandatory typed columns (ID, Severity, Finding/Artifact or Concern, Owner, Resolution). Each column carries an inline rejection guard specifying invalid values. Converts C-04's prose-level quality check into a format-level check: a finding that does not fill every typed column is a format failure before it is a content judgment. The GO/NO-GO signal (C-05) is explicitly exempt from table-first scope -- unambiguous labeled signals are degraded, not improved, by tabular rendering.
- **Pass condition**: Findings table present with at minimum 5 typed columns (ID, Severity, Finding, Owner, Resolution). Each column carries an inline rejection guard. GO/NO-GO signal rendered as a standalone labeled signal, not a table cell.

---

### C-27 -- D-ID Ref Column as Per-Row Structural Obligation
- **Category**: format
- **Weight**: aspirational
- **Text**: The findings table includes a dedicated D-ID Ref column as a required 6th typed slot. When a stage's Inertia Stance is RESISTANT and a finding's Severity is HIGH, the D-ID Ref cell must contain a D-ID from the Displacement Map register; for all other findings the cell is N/A. This converts C-25's per-finding citation requirement from a prose Inertia Check note -- where "reference the inertia contribution as a factor" satisfies the wording without naming a specific register entry -- into a per-row cell obligation. Without this column, executing models drift to the prose form because no structural slot demands the D-ID.
- **Pass condition**: Findings table template has a D-ID Ref column with a fill instruction of the form `[fill: D-{ID} from Displacement Map; N/A if Inertia Stance is not RESISTANT or Severity is not HIGH]`. N/A when C-13 is absent.

---

### C-28 -- Named Anti-Pattern Rejection Phrase in D-ID Ref Column Guard
- **Category**: format
- **Weight**: aspirational
- **Text**: The D-ID Ref column guard names at least one explicit invalid cell value and rejects it by condition -- e.g., "N/A does not satisfy when Inertia Stance is RESISTANT and Severity is HIGH." The named-anti-pattern technique (sourced from C-24/C-26's [fill]-with-rejection-language pattern, applied here at the column-guard level) closes the gap between structural presence and citation compliance: N/A is a syntactically valid cell value; naming it as insufficient under RESISTANT+HIGH prevents a borderline-compliant fill. Distinguished from a table-level footer by appearing inline in the column template itself, where it is encountered during column-guide reading rather than only at table-footer inspection.
- **Pass condition**: D-ID Ref column guard contains at least one named anti-pattern with an explicit "does not satisfy" or equivalent rejection phrase tied to the RESISTANT+HIGH condition. Requires C-27 (N/A when C-27 absent).

---

### C-29 -- Explicit Scope-Exception Calibration for Table-First Format
- **Category**: format
- **Weight**: aspirational
- **Text**: The template includes a named calibration section identifying output types exempt from C-26's table-first findings format, with rationale for each named exception. The GO/NO-GO signal is the canonical exempt type: unambiguous labeled signals are degraded, not improved, by tabular rendering. The calibration section closes the table-first architecture by making the exception boundary explicit in the template itself -- promoting the design-note annotation in C-26 to a first-class template element. Without this section, the exception boundary exists only in the rubric, and an executing model that has not read the rubric has no template-level guidance against over-applying table-first format to signal types where structure changes semantics.
- **Pass condition**: Template contains a named calibration section (e.g., "Table-First Scope Exceptions" or equivalent heading) listing at least one exempt output type with rationale. GO/NO-GO must be explicitly named and its exemption rationale stated. Requires C-27 (N/A when C-27 absent -- calibration is meaningful only within the 6-column architecture that introduces the conditional format-failure family and therefore requires a defined scope boundary).
