Here is the complete updated rubric v10.

---

**Summary of changes from v9 to v10:**

Three new aspirational criteria extracted from the R11 excellence signals:

| ID | Name | Source | Pattern |
|----|------|--------|---------|
| C-36 | Synthesis F-IDs in Handoff Packet Cross-Stage Synthesis | V-01 R11 | Typed field + minimum-cardinality rule (>=2 F-IDs; 1 if only one row forwarded; deferred if empty) + 3 named invalid values. Closes the prose-boundary asymmetry at the synthesis slot. |
| C-37 | Risk Shift Source F-ID in Handoff Packet Downstream Risk Shift | V-02 R11 | Typed field + single-F-ID rule (current stage only; name the primary when multiple contribute) + 3 named invalid values. Closes the prose-boundary asymmetry at the most consequential forward-looking assertion slot. |
| C-38 | STAGE VERDICT AGGREGATE in ROB Summary | V-03 R11 | Pre-stated aggregation rule (BLOCKED > APPROVED WITH CONDITIONS > DEFERRED > APPROVED) + typed table (Stage, Stage Verdict, Governing F-ID, Propagation) + 3 named invalid values for Governing F-ID column. Converts Overall Verdict from editorial re-synthesis to mechanically derivable result. |

**Scoring change:** N_aspirational 27 -> 30. Ceiling still 100 (max contributable = 10). Raw count (max 30) is the tie-break. V-05 R11 is the new leader at 30 raw.

**Architectural note:** C-36 and C-37 apply the table-column citation mechanism to prose slots for the first time -- same typed-field + anti-pattern guard pattern, different target. The cardinality difference is semantically derived: synthesis requires >=2 (multi-finding by definition), risk shift requires exactly 1 (single vantage-point primary). C-38 operates at the derivation level: it adds the missing pre-stated rule and typed table that makes the Overall Verdict auditable without reading six Stage Verdict sections.
| The Handoff Packet Cross-Stage Synthesis prose slot requires a `Synthesis F-IDs` typed field immediately below the prose. The field must contain at least two F-IDs from the Cross-Stage References Forwarded table above that the synthesis characterizes -- not a prose description, a table deferral, or a generalized reference. The two-F-ID minimum is not a policy threshold but a semantic one: cross-stage synthesis by definition characterizes a pattern across multiple findings; a citation of one finding is a single-finding observation, not a cross-stage synthesis. Exception: when the Forwarded table contains exactly one row, one F-ID satisfies the field. When the Forwarded table is empty, the field must state "No F-IDs forwarded -- synthesis deferred". Field guard names at least three explicit invalid values: "See forwarded table" does not satisfy this field; "Based on overall stage findings" does not satisfy this field; "Forwarded findings reviewed" does not satisfy this field. A Synthesis F-IDs field with fewer than two F-IDs when the Forwarded table contains 2+ rows is a format failure. Converts the Cross-Stage Synthesis slot from an asserted characterization of a forwarded pattern into a finding-grounded one, closing the structural asymmetry where table columns had citation obligations but prose slots did not. Requires the Handoff Packet (N/A when absent). |
| C-37 | Risk Shift Source F-ID as Single-Citation Obligation in Handoff Packet Downstream Risk Shift | V-02 R11 (all v9 criteria pass baseline; no Risk Shift Source F-ID field present in v9) | The Handoff Packet Downstream Risk Shift prose slot requires a `Risk Shift Source F-ID` typed field immediately below the prose. The field must contain exactly one F-ID from the current stage's Findings table or Cross-Stage References that established the failure mode or ownership gap visibility -- not a prose description, a deferral to the stage in general, or a claim unsupported by a specific finding. The single-F-ID requirement is semantically derived: a risk shift identifies a net-new risk from a specific stage vantage point, which has a single primary source finding (when multiple findings contributed, name the primary). The F-ID must be from the current stage -- the risk shift is a net-new observation from this stage's vantage point, so its ground must be traceable to a finding at this stage or re-framed through this stage's cross-stage reading. Field guard names at least three explicit invalid values: "Based on stage review" does not satisfy this field; "See findings" does not satisfy this field; "General stage concerns" does not satisfy this field. An empty or generic cell when the Downstream Risk Shift prose names a specific failure mode or ownership gap is a format failure. Converts the Downstream Risk Shift slot from a stage-asserted claim into a finding-grounded one, extending prose-boundary citation discipline to the most consequential forward-looking assertion slot in the ROB architecture. Requires the Handoff Packet (N/A when absent). |
| C-38 | STAGE VERDICT AGGREGATE as Pre-Stated Worst-Verdict-Wins Derivation Table in ROB Summary | V-03 R11 (all v9 criteria pass baseline; no STAGE VERDICT AGGREGATE table present in v9) | The ROB Summary requires a `STAGE VERDICT AGGREGATE` table as a named typed section. The table contains one row per stage with four columns: Stage, Stage Verdict, Governing F-ID (the F-ID cited in that stage's Verdict Rationale that drove the verdict selection), and Propagation (YES if this stage's verdict equals the Overall Verdict and is the worst observed; NO otherwise). The aggregation rule must be stated in the table or immediately before it: BLOCKED > APPROVED WITH CONDITIONS > DEFERRED > APPROVED. The Overall Verdict in the ROB Summary header must equal the worst Stage Verdict in the table -- an Overall Verdict that diverges from the worst-verdict-wins result is a format failure. The Governing F-ID column guard names at least three explicit invalid values: "See stage findings" does not satisfy this column; "Multiple findings" does not satisfy this column; "General stage concerns" does not satisfy this column. A row without the F-ID cited in that stage's Verdict Rationale is a format failure. The Propagation column guard: a row where the Stage Verdict is worse than the Overall Verdict with Propagation=NO is a format failure (a verdict worse than the Overall Verdict must have driven it). Converts the ROB Summary Overall Verdict from an editorial re-synthesis of six stage verdicts into a mechanically derivable result that is independently auditable without reading all six Stage Verdict sections. Requires C-04 Stage Sequence (N/A when fewer than two stages are run). |

**Scoring change:** N_aspirational 27 -> 30. Max contributable to composite still 10 (ceiling = 100). Raw count (max 30) is the tie-break.

**Re-grades under v10:**
- V-05 R10 (prior overall leader): C-36 FAIL, C-37 FAIL, C-38 FAIL -> 27 raw / 10 contributable -> **100**; tie-break 27 (unchanged)
- V-01 R11 (Synthesis F-IDs): C-36 PASS, C-37 FAIL, C-38 FAIL -> 28 raw -> **100**; tie-break 28
- V-02 R11 (Risk Shift Source F-ID): C-36 FAIL, C-37 PASS, C-38 FAIL -> 28 raw -> **100**; tie-break 28
- V-03 R11 (Stage Verdict Aggregate): C-36 FAIL, C-37 FAIL, C-38 PASS -> 28 raw -> **100**; tie-break 28
- V-04 R11 (Synthesis F-IDs + Risk Shift Source F-ID): C-36 PASS, C-37 PASS, C-38 FAIL -> 29 raw -> **100**; tie-break 29
- V-05 R11 (all three axes): C-36 PASS, C-37 PASS, C-38 PASS -> 30 raw -> **100**; tie-break 30 -- new leader

**Design note:** The three R11 axes extend the citation-completeness architecture from table columns (v8/v9) to the remaining unguarded positions in the ROB output. C-36 and C-37 both operate at the prose boundary: they apply the table-column citation mechanism (typed field + cardinality rule + named invalid values + format failure condition) to the two prose slots in the Handoff Packet, where no equivalent enforcement existed. C-36 targets the Cross-Stage Synthesis slot; C-37 targets the Downstream Risk Shift slot. The cardinality difference between them is semantically derived from each slot's definition: C-36 requires at least two F-IDs because cross-stage synthesis by definition characterizes a pattern across multiple findings -- a single-finding synthesis is a contradiction in terms; C-37 requires exactly one because a risk shift identifies net-new risk with a single primary source at this stage's vantage point. C-38 operates at a structurally different level: it adds a pre-stated aggregation rule and a typed derivation table that makes the Overall Verdict mechanically auditable from six Stage Verdicts, eliminating the editorial re-synthesis step at the ROB Summary. As in prior rounds, the three axes are independent of each other -- V-01 through V-03 each introduce one axis in isolation; V-04 combines V-01 and V-02; V-05 applies all three. C-36 and C-37 together complete the citation architecture within the Handoff Packet artifact (every slot now has a grounding obligation). C-38 completes the verdict derivation chain end-to-end: finding -> [risk register Source F-IDs (C-33)] -> stage verdict -> [STAGE VERDICT AGGREGATE Governing F-ID] -> Overall Verdict. Together the three criteria close all three unguarded positions identified in the R11 baseline audit: the synthesis prose slot, the risk shift prose slot, and the cross-stage verdict aggregation step.

---

## Scoring Formula

| Band | Criteria | Max pts |
|------|----------|---------|
| Essential | C-01 -- C-05 | 5 x 12 = 60 |
| Recommended | C-06 -- C-08 | 3 x 10 = 30 |
| Aspirational | C-09 -- C-38 | N_pass (max contributable = 10) |

**PARTIAL = 0.5 pass. Ceiling = 100.**

Aspirational score = N_pass (each full pass = 1 point, PARTIAL = 0.5 pts).
Max contributable to composite = 10. Raw count max = 30 (tie-break when composite = 100).

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
- **Text**: Findings name specific artifacts, components, decisions, or constraints -- not general characterizations of a topic area. Each finding is tied to something concrete in the feature under review.
- **Pass condition**: Every finding in every stage names at least one specific artifact (a spec section, a schema field, a contract, a dependency, a schedule milestone) or a concrete observable gap. Findings that could apply unchanged to any feature without modification do not pass.

---

### C-04 -- Stage Sequence
- **Category**: format
- **Weight**: essential
- **Text**: The six stages appear in canonical order: `leadership` -> `teams` -> `pm` -> `tpm` -> `arch-board` -> `exec-office`. No stage is omitted and no stage appears out of sequence.
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

*Each full pass = 1 point toward the aspirational band (max contributable = 10). PARTIAL = 0.5 pts. Raw count (max 30) used as tie-break.*

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
- **Pass condition**: Stage 1 findings cover all lenses specified for the `leadership` role in `.roles/`. Missing lenses in Stage 1 are a failure.

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
- **Pass condition**: At least one explicit three-hop chain is present: lens -> finding (F-ID) -> recommendation or blocker, with each hop named and connected.

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

---

### C-36 -- Synthesis F-IDs as Minimum-Cardinality Citation Obligation in Handoff Packet Cross-Stage Synthesis
- **Category**: synthesis
- **Weight**: aspirational
- **Text**: The Handoff Packet Cross-Stage Synthesis prose slot requires a `Synthesis F-IDs` typed field immediately below the prose. The field must contain at least two F-IDs from the Cross-Stage References Forwarded table that the synthesis characterizes -- not a table deferral, a generalized reference, or a prose paraphrase. The two-F-ID minimum is semantic, not arbitrary: cross-stage synthesis characterizes a pattern across multiple findings; a citation of one finding is a single-finding observation, not a cross-stage pattern. Exception: when the Forwarded table contains exactly one row, one F-ID satisfies; when the Forwarded table is empty, the field must state "No F-IDs forwarded -- synthesis deferred". Field guard names at least three explicit invalid values: "See forwarded table" does not satisfy this field; "Based on overall stage findings" does not satisfy this field; "Forwarded findings reviewed" does not satisfy this field. A Synthesis F-IDs field with fewer than two F-IDs when the Forwarded table contains 2+ rows is a format failure. Applies the table-column citation mechanism (typed field + cardinality rule + named invalid values + format failure condition) to a prose slot, closing the structural asymmetry where all table columns had citation obligations but the Cross-Stage Synthesis prose slot did not.
- **Pass condition**: Synthesis F-IDs field is present immediately below the Cross-Stage Synthesis prose in every stage's Handoff Packet. Every field contains at least two F-IDs when the Forwarded table has 2+ rows, or exactly one F-ID when the Forwarded table has one row, or the deferred statement when the Forwarded table is empty. Field guard names at least three invalid values. Requires C-11 (N/A when absent).

---

### C-37 -- Risk Shift Source F-ID as Single-Citation Obligation in Handoff Packet Downstream Risk Shift
- **Category**: synthesis
- **Weight**: aspirational
- **Text**: The Handoff Packet Downstream Risk Shift prose slot requires a `Risk Shift Source F-ID` typed field immediately below the prose. The field must contain exactly one F-ID from the current stage's Findings table or Cross-Stage References that established the failure mode or ownership gap visibility named in the prose -- not a prose description, a stage-level deferral, or a generalized characterization. The single-F-ID requirement is semantically derived: a risk shift identifies net-new risk from a specific stage vantage point and has a single primary source finding; when multiple findings contributed, name the primary. The F-ID must be from the current stage -- the risk shift is a net-new observation from this stage's vantage point. Field guard names at least three explicit invalid values: "Based on stage review" does not satisfy this field; "See findings" does not satisfy this field; "General stage concerns" does not satisfy this field. An empty or generic cell when the Downstream Risk Shift prose names a specific failure mode or ownership gap is a format failure. Extends prose-boundary citation discipline to the most consequential forward-looking assertion slot in the ROB architecture: the slot that introduces net-new risk invisible to prior stages.
- **Pass condition**: Risk Shift Source F-ID field is present immediately below the Downstream Risk Shift prose in every stage's Handoff Packet. Every field contains exactly one current-stage F-ID when the prose names a specific failure mode or gap. Field guard names at least three invalid values. Requires C-11 (N/A when absent).

---

### C-38 -- STAGE VERDICT AGGREGATE as Pre-Stated Worst-Verdict-Wins Derivation Table in ROB Summary
- **Category**: synthesis
- **Weight**: aspirational
- **Text**: The ROB Summary requires a `STAGE VERDICT AGGREGATE` table as a named typed section. The table contains one row per stage with four columns: Stage, Stage Verdict (APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED), Governing F-ID (the F-ID cited in that stage's Verdict Rationale that drove the verdict selection), and Propagation (YES if this stage's verdict equals the Overall Verdict and is the worst observed; NO otherwise). The aggregation rule must be stated in the table header or immediately before the table: BLOCKED > APPROVED WITH CONDITIONS > DEFERRED > APPROVED. The Overall Verdict in the ROB Summary header must equal the worst Stage Verdict in the table -- an Overall Verdict that diverges from the worst-verdict-wins result is a format failure. Governing F-ID column guard names at least three explicit invalid values: "See stage findings" does not satisfy this column; "Multiple findings" does not satisfy this column; "General stage concerns" does not satisfy this column. A row without the F-ID cited in that stage's Verdict Rationale is a format failure. Propagation column guard: a row where the Stage Verdict is worse than the Overall Verdict with Propagation=NO is a format failure. Converts the Overall Verdict from an editorial re-synthesis of six stage verdicts into a mechanically derivable result that is independently auditable -- a reader can verify the Overall Verdict by inspecting the table alone without reading all six Stage Verdict sections.
- **Pass condition**: STAGE VERDICT AGGREGATE table is present in the ROB Summary. One row per stage run. Governing F-ID column is populated per row with the F-ID from that stage's Verdict Rationale. Propagation column correctly marks the worst-verdict stage(s) as YES. Aggregation rule is stated. Overall Verdict equals worst Stage Verdict in table. Column guards name at least three invalid values for Governing F-ID. Requires C-04 Stage Sequence (N/A when fewer than two stages are run).
```
