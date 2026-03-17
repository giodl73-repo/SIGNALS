```markdown
# corps-rob rubric v9 -- 2026-03-17

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
| v8 | C-30 -- C-32: resolution evidence in blocker resolution status table, primary F-IDs in cross-cutting themes table, addressing F-IDs in handoff packet. N_aspirational 21 -> 24. |
| v9 | C-33 -- C-35: source F-IDs in TPM risk register, supporting F-IDs in mission cascade, remediation action in chain health table. N_aspirational 24 -> 27. |

---

## New in v9 -- What was extracted from the R9 scorecard

| ID | Name | Source | Mechanism |
|----|------|--------|-----------|
| C-33 | Source F-IDs Column as Per-Risk Citation Obligation in TPM Risk Register | V-01 R9 (C-09/C-12/C-30 PASS baseline; no source F-ID column present in v8) | The TPM Risk Register requires a `Source F-IDs` column as a named typed slot. Each risk row must contain at least one F-ID identifying the finding from which the risk is derived -- not a prose description, an inferred claim, or a general characterization. Column guard names at least two explicit invalid cell values: "Inferred from ROB" does not satisfy this column; "General concerns" does not satisfy this column. A risk row without a Source F-ID is a format failure. Converts the TPM Risk Register from an inferred or asserted risk list into a finding-grounded register, making each risk traceable to a specific stage finding rather than synthesized from review memory. Requires the TPM stage Risk Register section (N/A when absent). |
| C-34 | Supporting F-IDs Column as Per-Row Citation Obligation in Mission Cascade | V-02 R9 (C-19/C-21 PASS baseline; no supporting F-ID column present in v8) | The Mission Cascade table requires a `Supporting F-IDs` column as a named typed slot. PARTIAL and GAP rows must contain at least one F-ID identifying the finding that grounds the partial coverage or gap assessment -- not a prose rationale for the status. COMPLETE rows may use N/A or equivalent. Column guard names at least two explicit invalid cell values: "Based on general review" does not satisfy this column; "See ROB findings" does not satisfy this column. A PARTIAL or GAP row without a Supporting F-ID is a format failure. Converts Mission Cascade from a status-only assessment (COMPLETE/PARTIAL/GAP) into a finding-grounded citation obligation, making cascade gaps traceable to specific findings rather than asserted from general review. Requires the Mission Cascade table (N/A when absent). |
| C-35 | Remediation Action Column as Per-Row Corrective Obligation in Chain Health Table | V-03 R9 (C-23 PASS baseline; no remediation action column present in v8) | The LENS ACTIVATION CHAIN HEALTH table requires a `Remediation Action` column as a named typed slot. BROKEN and PARTIAL rows must contain a specific identification of the missing chain element and a named corrective action -- not a status label, a vague directive, or a restatement of the status. COMPLETE rows must contain N/A or equivalent. Column guard names at least two explicit invalid cell values: "Chain incomplete" does not satisfy this column; "Needs review" does not satisfy this column. A BROKEN or PARTIAL row without a specific remediation action is a format failure. Converts Chain Health from a diagnostic-only table (COMPLETE/PARTIAL/BROKEN status) into an actionable table that names both the gap and the corrective step, extending chain health tracking from identification to remediation. Requires C-23 Chain Health Summary (N/A when absent). |

**Scoring change:** N_aspirational 24 -> 27. Max contributable to composite still 10 (ceiling = 100). Raw count (max 27) is the tie-break.

**Re-grades under v9:**
- V-05 R8 (prior overall leader): C-33 FAIL, C-34 FAIL, C-35 FAIL -> 24 raw / 10 contributable -> **100**; tie-break 24 (unchanged)
- V-01 R9 (Source F-IDs in Risk Register): C-33 PASS, C-34 FAIL, C-35 FAIL -> 25 raw -> **100**; tie-break 25
- V-02 R9 (Supporting F-IDs in Mission Cascade): C-33 FAIL, C-34 PASS, C-35 FAIL -> 25 raw -> **100**; tie-break 25
- V-03 R9 (Remediation Action in Chain Health): C-33 FAIL, C-34 FAIL, C-35 PASS -> 25 raw -> **100**; tie-break 25
- V-04 R9 (Risk Register + Mission Cascade): C-33 PASS, C-34 PASS, C-35 FAIL -> 26 raw -> **100**; tie-break 26
- V-05 R9 (all three axes): C-33 PASS, C-34 PASS, C-35 PASS -> 27 raw -> **100**; tie-break 27 -- new leader

**Design note:** The three R9 axes extend the citation-completeness architecture from synthesis tables (v8: C-30 through C-32) into the ROB's operational output tables. Each axis targets a different operational table: C-33 targets the TPM Risk Register, C-34 targets the Mission Cascade, and C-35 targets the LENS ACTIVATION CHAIN HEALTH table. The shared mechanism across all three: add a typed citation or action column where a status-only or assertion-only field existed, and name at least two invalid cell values in the column guard. The R9 axes differ from R8 in one structural respect: C-35 is not purely a citation obligation -- it requires a corrective action alongside the gap identification. This makes C-35 the first criterion that demands forward-looking remediation, not just backward-looking traceability. C-33 and C-34 follow the pure citation pattern established in R8 (typed F-ID column + anti-pattern guard); C-35 introduces a hybrid: diagnosis (missing element identification) + prescription (corrective action) in a single typed column. As in R8, the three axes are independent of each other -- V-01 through V-03 each introduce one axis in isolation; V-04 combines V-01 and V-02; V-05 applies all three. Together the three criteria extend finding-citation discipline from the ROB Summary tables into the tables produced by individual stage roles, completing a uniform citation and action obligation across all structured tables in the corps-rob output format.

---

## Scoring Formula

| Band | Criteria | Max pts |
|------|----------|---------|
| Essential | C-01 -- C-05 | 5 x 12 = 60 |
| Recommended | C-06 -- C-08 | 3 x 10 = 30 |
| Aspirational | C-09 -- C-35 | N_pass (max contributable = 10) |

**PARTIAL = 0.5 pass. Ceiling = 100.**

Aspirational score = N_pass (each full pass = 1 point, PARTIAL = 0.5 pts).
Max contributable to composite = 10. Raw count max = 27 (tie-break when composite = 100).

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
- **Text**: Each stage review reflects the documented lens of the persona loaded from `.craft/roles/` via `org.yaml` -- not a generic review any role could have written. The role's orientation shapes which concerns are surfaced and how they are framed.
- **Pass condition**: At least one finding per stage is grounded in the loaded persona's specific lens (e.g., a TPM flags schedule risk and dependency gaps, a Principal Architect flags interface coupling, a PM flags adoption risk, a Chief of Staff flags mission alignment). Findings that are fully generic -- applicable by any reviewer to any topic -- do not satisfy this criterion for any stage in which they appear.

---

### C-03 -- Finding Specificity
- **Category**: correctness
- **Weight**: essential
- **Text**: Findings name specific artifacts, components, decisions, or constraints -- not general characterizations of a topic area. Each finding is tied to something concrete in the feature under review.
- **Pass condition**: Every finding in every stage names at least one specific artifact (a spec section, a schema field, a contract, a dependency, a schedule milestone) or a concrete observable gap. Findings that could apply unchanged to any feature without modification do not pass.

---

### C-04 -- Stage Sequence
- **Category**: format
- **Weight**: essential
- **Text**: The six stages appear in canonical order: `leadership` → `teams` → `pm` → `tpm` → `arch-board` → `exec-office`. No stage is omitted and no stage appears out of sequence.
- **Pass condition**: All six canonical stages are present and appear in the specified order. Missing or reordered stages are a failure.

---

### C-05 -- Output Completeness
- **Category**: format
- **Weight**: essential
- **Text**: The output includes all mandatory sections: per-stage findings, the ROB Summary (Blocker Resolution Status, Cross-Cutting Themes, Handoff Packet), and the Briefing Envelope.
- **Pass condition**: All mandatory sections are present with non-empty content. A section present as a header with no content does not pass.

---

## Recommended Criteria

*Each is worth 10 points. PARTIAL = 5 pts.*

---

### C-06 -- Finding Depth
- **Category**: quality
- **Weight**: recommended
- **Text**: Findings include root-cause framing -- not just an observation of a gap but an identification of why the gap exists or what structural condition produces it.
- **Pass condition**: At least half of the findings across all stages include a root-cause or causal framing statement. Findings that only describe the symptom without any causal analysis do not count toward this criterion.

---

### C-07 -- Risk Calibration
- **Category**: quality
- **Weight**: recommended
- **Text**: Risk severity assessments are tied to scope evidence from the feature under review -- not default severity assignments. A risk rated HIGH must be traceable to a specific scope characteristic that justifies that rating.
- **Pass condition**: Every HIGH or CRITICAL risk in every stage cites a specific feature scope element (timeline, dependency, integration surface, team size, or adoption constraint) that grounds the severity assignment.

---

### C-08 -- Recommendation Actionability
- **Category**: quality
- **Weight**: recommended
- **Text**: Recommendations name owners, artifacts, or checkpoints -- not generic directives. A recommendation is actionable when a specific person or role can execute it against a named deliverable.
- **Pass condition**: At least two-thirds of recommendations across all stages name an owner role or artifact. Recommendations phrased as "the team should consider" without a named owner or deliverable do not pass.

---

## Aspirational Criteria

*Each full pass = 1 point toward the aspirational band (max contributable = 10). PARTIAL = 0.5 pts. Raw count (max 27) used as tie-break.*

---

### C-09 -- Inter-Stage Blocker Detection
- **Category**: synthesis
- **Weight**: aspirational
- **Text**: Blockers that span stage boundaries are identified explicitly -- not left as implicit tensions between per-stage findings. A cross-stage blocker is named when a finding in one stage creates a dependency or gate condition for a downstream stage.
- **Pass condition**: The Blocker Resolution Status table is present and contains at least one blocker with an explicit cross-stage scope annotation. Requires C-05.

---

### C-10 -- Cross-Cutting Theme Elevation
- **Category**: synthesis
- **Weight**: aspirational
- **Text**: Concerns that appear across multiple stages are elevated into named cross-cutting themes rather than left as repeated per-stage observations. Each theme names the stages in which it appears.
- **Pass condition**: The Cross-Cutting Themes table is present and contains at least one theme with named stage scope. A theme entry without stage scope annotation does not satisfy this criterion. Requires C-05.

---

### C-11 -- Handoff Packet
- **Category**: synthesis
- **Weight**: aspirational
- **Text**: Findings that require action in downstream stages are forwarded explicitly in a handoff structure -- not left as implicit implications of per-stage findings.
- **Pass condition**: The Handoff Packet Cross-Stage References Forwarded section is present and contains at least one forwarded finding with a named receiving stage. Requires C-05.

---

### C-12 -- Stage-Boundary Blocker Field
- **Category**: format
- **Weight**: aspirational
- **Text**: Each stage section includes an explicit blocker field at its boundary -- a named slot that declares whether a blocker to downstream progression exists, rather than leaving blocker status implicit.
- **Pass condition**: Every stage section contains a named blocker field (e.g., `STAGE BLOCKER:` or equivalent) at the stage boundary with an explicit NONE or named blocker value.

---

### C-13 -- Inertia Anchor
- **Category**: correctness
- **Weight**: aspirational
- **Text**: The output calls out the inertia signal -- the structural or organizational force that is most likely to prevent findings from being acted upon -- not just the findings themselves.
- **Pass condition**: At least one stage or the ROB Summary names an inertia signal: a specific organizational pattern, process constraint, or resource condition that would cause the identified risks to persist even after the review.

---

### C-14 -- Briefing Envelope
- **Category**: format
- **Weight**: aspirational
- **Text**: A pre-ROB briefing envelope is present that frames the review context: the topic under review, the stage sequence being run, and any scope constraints in effect.
- **Pass condition**: The Briefing Envelope section is present before Stage 1 with non-empty topic, stage sequence, and scope content.

---

### C-15 -- Anti-Redundancy
- **Category**: quality
- **Weight**: aspirational
- **Text**: Findings are not duplicated across stages. When the same concern appears in multiple stages, it is elevated to a cross-cutting theme (C-10) rather than restated verbatim in each stage.
- **Pass condition**: No finding text is substantially repeated across two or more stage sections. Concerns that appear in multiple stages must appear only once in per-stage findings and be elevated to the Cross-Cutting Themes table.

---

### C-16 -- Lens-Impact Pair
- **Category**: correctness
- **Weight**: aspirational
- **Text**: Each lens activation is paired with an impact statement -- the output names not just which lens was activated but what the activation surfaces about the feature's risk or readiness.
- **Pass condition**: Every named lens activation includes an adjacent impact statement. A lens named without an impact characterization does not satisfy this criterion.

---

### C-17 -- Risk-Shift Guard
- **Category**: correctness
- **Weight**: aspirational
- **Text**: The output distinguishes between risks that are new to this review cycle and risks that have shifted in severity from a prior cycle. Risk shifts are labeled as shifts rather than presented as new findings.
- **Pass condition**: At least one finding includes an explicit risk-shift label when the risk represents a change from a prior assessment. Outputs with no prior cycle context may mark this N/A with explanation.

---

### C-18 -- Explicit Lens Fill Field
- **Category**: format
- **Weight**: aspirational
- **Text**: Each stage section includes a named lens fill field -- an explicit slot that declares which lens was loaded for that stage, not left implicit in the finding framing.
- **Pass condition**: Every stage section contains a named lens fill field (e.g., `LENS:` or equivalent) with the loaded lens name present.

---

### C-19 -- Stage 1 Lens Coverage
- **Category**: correctness
- **Weight**: aspirational
- **Text**: Stage 1 (leadership) covers all required lenses for its role -- not a subset. The leadership lens set must be fully instantiated, not partially populated.
- **Pass condition**: Stage 1 findings cover all lenses specified for the `leadership` role in `.craft/roles/`. Missing lenses in Stage 1 are a failure.

---

### C-20 -- Pre-Envelope Part 0 Block
- **Category**: format
- **Weight**: aspirational
- **Text**: A Part 0 block is present before the Briefing Envelope that declares the review mode, the corpus being reviewed, and the rubric version in effect.
- **Pass condition**: The Part 0 block is present and contains non-empty review mode, corpus reference, and rubric version fields.

---

### C-21 -- KEY CONCERNS Back-Ref
- **Category**: synthesis
- **Weight**: aspirational
- **Text**: The KEY CONCERNS section of the ROB Summary references upstream findings by F-ID -- not by prose paraphrase. Key concerns are grounded in specific findings, not restated from memory.
- **Pass condition**: Every KEY CONCERN entry includes at least one F-ID back-reference to the upstream finding that grounds it.

---

### C-22 -- Three-Hop Chain
- **Category**: correctness
- **Weight**: aspirational
- **Text**: The output demonstrates a three-hop traceability chain: from a lens activation to a finding to a downstream recommendation or blocker. The chain must be explicit, not implied.
- **Pass condition**: At least one explicit three-hop chain is present: lens → finding (F-ID) → recommendation or blocker, with each hop named and connected.

---

### C-23 -- Chain Health Summary
- **Category**: synthesis
- **Weight**: aspirational
- **Text**: The LENS ACTIVATION CHAIN HEALTH summary is present and covers the health status of each active lens chain in the review.
- **Pass condition**: The Chain Health table is present and contains a row for each lens activated in the review with a COMPLETE/PARTIAL/BROKEN status assigned. A table with missing lens rows is a partial pass (PARTIAL).

---

### C-24 -- Fill-Slot Structural Completeness
- **Category**: format
- **Weight**: aspirational
- **Text**: All named fill slots in the output template are present and typed -- not omitted or collapsed. A fill slot is present when its label appears in the output; it is typed when its content matches the declared slot type (e.g., a list slot contains a list, a citation slot contains a citation).
- **Pass condition**: Every fill slot defined in the stage template appears in the output with typed content. An absent or untyped slot is a format failure.

---

### C-25 -- Displacement Map with D-IDs
- **Category**: synthesis
- **Weight**: aspirational
- **Text**: The Displacement Map is present and every displacement entry carries a D-ID -- a stable identifier that allows displacement entries to be referenced from other sections.
- **Pass condition**: The Displacement Map table is present and every row has a non-empty D-ID in the designated column.

---

### C-26 -- Table-First Findings Format
- **Category**: format
- **Weight**: aspirational
- **Text**: Findings are presented in table-first format -- a structured table before any prose elaboration. Prose elaboration may follow the table but the table is the primary record.
- **Pass condition**: Every stage's findings section leads with a findings table. A stage where findings appear only in prose without a leading table does not satisfy this criterion for that stage.

---

### C-27 -- D-ID Ref Column
- **Category**: format
- **Weight**: aspirational
- **Text**: The Displacement Map table includes a `D-ID Ref` column as a named typed slot. The column records the D-ID of the displacement entry that each finding displaces or is displaced by, creating a bidirectional reference between findings and displacements.
- **Pass condition**: The Displacement Map contains a `D-ID Ref` column. Rows without a D-ID Ref value when a displacement relationship exists are a format failure. Requires C-25.

---

### C-28 -- Anti-Pattern Rejection Phrases in D-ID Ref Guard
- **Category**: format
- **Weight**: aspirational
- **Text**: The D-ID Ref column guard names at least two explicit invalid cell values -- cell values that superficially resemble a D-ID reference but do not satisfy the citation obligation.
- **Pass condition**: The D-ID Ref column definition or guard statement names at least two explicit invalid values (e.g., "See findings" does not satisfy this column; "Derived from review" does not satisfy this column). Requires C-27.

---

### C-29 -- Scope-Exception Calibration for Table-First Format
- **Category**: format
- **Weight**: aspirational
- **Text**: The table-first findings format exception scope is explicitly named -- the output identifies which finding types or stages are permitted to deviate from table-first format and why.
- **Pass condition**: At least one explicit scope-exception statement is present naming the conditions under which prose-first findings are permitted. A blanket exception without scope is a partial pass (PARTIAL). Requires C-26.

---

### C-30 -- Resolution Evidence as Per-Row Citation Obligation in Blocker Resolution Status Table
- **Category**: synthesis
- **Weight**: aspirational
- **Text**: The Blocker Resolution Status table requires a `Resolution Evidence` column as a named typed slot. When Resolution Status is RESOLVED, the cell must contain a specific artifact citation -- a finding F-ID, a handoff packet reference, or an equivalent traceable pointer -- not a prose summary. Column guard names at least two explicit invalid cell values: "Discussed" does not satisfy this column; "See findings" does not satisfy this column. An empty or generic cell when Resolution Status is RESOLVED is a format failure. Converts C-09/C-12's blocker tracking from status-only (RESOLVED/UNRESOLVED) to traceable resolution, closing the gap between declaring a blocker resolved and citing the evidence for that resolution.
- **Pass condition**: Resolution Evidence column is present in the Blocker Resolution Status table. Every RESOLVED row contains a specific F-ID or artifact citation. Column guard names at least two invalid values. Requires C-09 and C-12 (N/A when absent).

---

### C-31 -- Primary F-IDs Column as Per-Stage Citation Obligation in Cross-Cutting Themes Table
- **Category**: synthesis
- **Weight**: aspirational
- **Text**: The Cross-Cutting Themes table requires a `Primary F-IDs` column as a named typed slot. Each theme row must contain at least one F-ID per named stage in which the concern appears -- not a prose description of the theme's scope. Column guard names at least two explicit invalid cell values: "Multiple findings" does not satisfy this column; "See findings" does not satisfy this column. A theme row without an F-ID per named stage is a format failure. Converts cross-cutting theme identification from a prose claim into a per-stage finding citation obligation.
- **Pass condition**: Primary F-IDs column is present in the Cross-Cutting Themes table. Every theme row contains at least one F-ID per named stage. Column guard names at least two invalid values. Requires C-10 (N/A when absent).

---

### C-32 -- Addressing F-IDs Column as Forward-Citation Obligation in Handoff Packet
- **Category**: synthesis
- **Weight**: aspirational
- **Text**: The Handoff Packet's Cross-Stage References Forwarded section requires an `Addressing F-IDs` column as a named typed slot. For each finding forwarded to a downstream stage, the cell names the F-IDs in the receiving stage expected to address it -- or explicitly marks the entry OPEN when no addressing finding has yet been identified. Column guard names at least one explicit invalid cell value: "TBD" does not satisfy this column. An empty cell for a forwarded finding is a format failure. Extends C-11's handoff tracking from a one-way forwarding record into a bidirectional citation.
- **Pass condition**: Addressing F-IDs column is present in the Handoff Packet. Every forwarded finding row contains either specific F-IDs or OPEN. Column guard names at least one invalid value. Requires C-11 (N/A when absent).

---

### C-33 -- Source F-IDs Column as Per-Risk Citation Obligation in TPM Risk Register
- **Category**: synthesis
- **Weight**: aspirational
- **Text**: The TPM Risk Register requires a `Source F-IDs` column as a named typed slot. Each risk row must contain at least one F-ID identifying the finding from which the risk is derived -- not a prose description, an inferred claim, or a general characterization of the risk's origin. Column guard names at least two explicit invalid cell values: "Inferred from ROB" does not satisfy this column; "General concerns" does not satisfy this column. A risk row without a Source F-ID is a format failure. Converts the TPM Risk Register from an inferred or asserted risk list into a finding-grounded register, making each risk traceable to a specific stage finding rather than synthesized from review memory.
- **Pass condition**: Source F-IDs column is present in the TPM Risk Register. Every risk row contains at least one F-ID. Column guard names at least two invalid values. Requires the TPM stage Risk Register section (N/A when absent).

---

### C-34 -- Supporting F-IDs Column as Per-Row Citation Obligation in Mission Cascade
- **Category**: synthesis
- **Weight**: aspirational
- **Text**: The Mission Cascade table requires a `Supporting F-IDs` column as a named typed slot. PARTIAL and GAP rows must contain at least one F-ID identifying the finding that grounds the partial coverage or gap assessment -- not a prose rationale for the status assignment. COMPLETE rows may use N/A or equivalent. Column guard names at least two explicit invalid cell values: "Based on general review" does not satisfy this column; "See ROB findings" does not satisfy this column. A PARTIAL or GAP row without a Supporting F-ID is a format failure. Converts Mission Cascade from a status-only assessment (COMPLETE/PARTIAL/GAP) into a finding-grounded citation obligation, making cascade gaps traceable to specific findings rather than asserted from general review.
- **Pass condition**: Supporting F-IDs column is present in the Mission Cascade table. Every PARTIAL and GAP row contains at least one F-ID. COMPLETE rows contain N/A or equivalent. Column guard names at least two invalid values. Requires the Mission Cascade table (N/A when absent).

---

### C-35 -- Remediation Action Column as Per-Row Corrective Obligation in Chain Health Table
- **Category**: synthesis
- **Weight**: aspirational
- **Text**: The LENS ACTIVATION CHAIN HEALTH table requires a `Remediation Action` column as a named typed slot. BROKEN and PARTIAL rows must contain a specific identification of the missing chain element and a named corrective action -- not a status label, a vague directive, or a restatement of the diagnostic status. COMPLETE rows must contain N/A or equivalent. Column guard names at least two explicit invalid cell values: "Chain incomplete" does not satisfy this column; "Needs review" does not satisfy this column. A BROKEN or PARTIAL row without a specific remediation action is a format failure. Converts Chain Health from a diagnostic-only table (COMPLETE/PARTIAL/BROKEN status) into an actionable table that names both the gap and the corrective step, extending chain health tracking from identification to remediation.
- **Pass condition**: Remediation Action column is present in the Chain Health table. Every BROKEN and PARTIAL row contains a named missing element and a named corrective action. COMPLETE rows contain N/A or equivalent. Column guard names at least two invalid values. Requires C-23 (N/A when absent).
```
