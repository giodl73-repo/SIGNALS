```markdown
# corps-rob rubric v8 -- 2026-03-17

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

---

## New in v8 -- What was extracted from the R8 scorecard

| ID | Name | Source | Mechanism |
|----|------|--------|-----------|
| C-30 | Resolution Evidence as Per-Row Citation Obligation in Blocker Resolution Status Table | V-01 R8 (C-09/C-12 PASS baseline; no resolution evidence column present in v7) | Blocker Resolution Status table requires a `Resolution Evidence` column as a named typed slot. When Resolution Status is RESOLVED, the cell must contain a specific artifact citation -- a finding F-ID, a handoff packet reference, or an equivalent traceable pointer -- not a prose summary. Column guard names at least two explicit invalid cell values: "Discussed" does not satisfy this column; "See findings" does not satisfy this column. An empty or generic cell when Resolution Status is RESOLVED is a format failure. Converts C-09/C-12's blocker tracking from status-only (RESOLVED/UNRESOLVED) to traceable resolution, closing the gap between declaring a blocker resolved and citing the evidence for that resolution. Requires C-09 and C-12 (N/A when absent). |
| C-31 | Primary F-IDs Column as Per-Stage Citation Obligation in Cross-Cutting Themes Table | V-02 R8 (C-10 PASS baseline; no primary F-ID column present in v7) | Cross-Cutting Themes table requires a `Primary F-IDs` column as a named typed slot. Each theme row must contain at least one F-ID per named stage in which the concern appears -- not a prose description of the theme's scope. Column guard names at least two explicit invalid cell values: "Multiple findings" does not satisfy this column; "See findings" does not satisfy this column. A theme row without an F-ID per named stage is a format failure. Converts cross-cutting theme identification from a prose claim (theme X appears in stages Y and Z) into a per-stage finding citation obligation, making themes traceable to specific findings rather than asserted from summary memory. Requires C-10 (N/A when absent). |
| C-32 | Addressing F-IDs Column as Forward-Citation Obligation in Handoff Packet | V-03 R8 (C-11 PASS baseline; no addressing F-ID column present in v7) | The Handoff Packet's Cross-Stage References Forwarded section requires an `Addressing F-IDs` column as a named typed slot. For each finding forwarded to a downstream stage, the cell names the F-IDs in the receiving stage expected to address it -- or explicitly marks the entry OPEN when no addressing finding has yet been identified. Column guard names at least one explicit invalid cell value: "TBD" does not satisfy this column. An empty cell for a forwarded finding is a format failure. Extends C-11's handoff tracking from a one-way forwarding record into a bidirectional citation that links each forwarded concern to its downstream treatment. Requires C-11 (N/A when absent). |

**Scoring change:** N_aspirational 21 -> 24. Max contributable to composite still 10 (ceiling = 100). Raw count (max 24) is the tie-break.

**Re-grades under v8:**
- V-05 R7 (prior overall leader): C-30 FAIL, C-31 FAIL, C-32 FAIL -> 21 raw / 10 contributable -> **100**; tie-break 21 (unchanged)
- V-01 R8 (Resolution Evidence column): C-30 PASS, C-31 FAIL, C-32 FAIL -> 22 raw -> **100**; tie-break 22
- V-02 R8 (Primary F-IDs column): C-30 FAIL, C-31 PASS, C-32 FAIL -> 22 raw -> **100**; tie-break 22
- V-03 R8 (Addressing F-IDs column): C-30 FAIL, C-31 FAIL, C-32 PASS -> 22 raw -> **100**; tie-break 22
- V-04 R8 (Resolution Evidence + Primary F-IDs): C-30 PASS, C-31 PASS, C-32 FAIL -> 23 raw -> **100**; tie-break 23
- V-05 R8 (all three axes): C-30 PASS, C-31 PASS, C-32 PASS -> 24 raw -> **100**; tie-break 24 -- new leader

**Design note:** The three R8 axes form a citation-completeness upgrade to the ROB Summary synthesis tables. Each axis targets a different summary table: C-30 targets the Blocker Resolution Status table (C-09/C-12), C-31 targets the Cross-Cutting Themes table (C-10), and C-32 targets the Handoff Packet (C-11). The shared mechanism across all three: add a typed citation column where a status-only or prose-only field existed, and name at least two invalid cell values in the column guard. Together the three criteria complete a finding-citation architecture across all ROB Summary tables -- every summary claim is now backed by a specific F-ID or artifact reference, not a status label or narrative assertion. The axes are independent of each other: they target different tables and impose no dependency chain among themselves. This independence distinguishes the R8 structure from R7's progressive chain (where C-28 required C-27, and C-29 required C-27): here V-01 through V-03 each introduce one axis in isolation; V-04 combines V-01 and V-02; V-05 applies all three. The common structural pattern -- typed citation column + named anti-pattern rejection -- applied independently to three previously unconstrained synthesis tables completes the citation architecture that the v5 through v7 series built for per-stage template slots and the D-ID mechanism.

---

## Scoring Formula

| Band | Criteria | Max pts |
|------|----------|---------|
| Essential | C-01 -- C-05 | 5 x 12 = 60 |
| Recommended | C-06 -- C-08 | 3 x 10 = 30 |
| Aspirational | C-09 -- C-32 | N_pass (max contributable = 10) |

**PARTIAL = 0.5 pass. Ceiling = 100.**

Aspirational score = N_pass (each full pass = 1 point, PARTIAL = 0.5 pts).
Max contributable to composite = 10. Raw count max = 24 (tie-break when composite = 100).

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
- **Text**: Each finding names the specific artifact, mechanism, or behavior at issue -- not a category label. "Dependency risk" is a category; "Stage 3 lacks a dependency map for the auth-service migration, and Stage 4's schedule assumes its completion" is a finding. Category-only findings cannot be actioned.
- **Pass condition**: Every finding in the output names a specific artifact, mechanism, or system behavior. Generic category labels (e.g., "dependency risk", "scalability concern") without a named artifact do not pass for any stage in which they appear.

---

### C-04 -- Finding Owner and Resolution
- **Category**: format
- **Weight**: essential
- **Text**: Each finding has a named owner (the role responsible for addressing it) and a concrete resolution action. Anonymous ownership and placeholder resolutions do not satisfy the template. "TBD" is not a role. "Needs attention" is not a resolution.
- **Pass condition**: Every finding row includes an Owner cell naming a canonical role (not "TBD" or blank) and a Resolution cell naming a concrete action (not "needs attention" or equivalent generic filler). Both columns carry inline rejection language.

---

### C-05 -- Verdict Calibration
- **Category**: correctness
- **Weight**: essential
- **Text**: Each stage template includes a VERDICT CALIBRATION table at the stage header defining the four valid verdict bands (PASS, PASS WITH CONCERNS, REVISE, BLOCK) and their semantic conditions. The Stage Verdict block cites the calibration row that justifies the verdict and names at least one supporting finding F-ID. A verdict without a calibration row citation is ungoverned.
- **Pass condition**: VERDICT CALIBRATION table present at Stage Template header with four rows. Stage Verdict block names the calibration band applied and includes at least one F-ID supporting the verdict selection.

---

## Recommended Criteria

*Each is worth 10 points. PARTIAL = 5 pts.*

---

### C-06 -- [Recommended criterion -- text preserved from v7]

---

### C-07 -- [Recommended criterion -- text preserved from v7]

---

### C-08 -- [Recommended criterion -- text preserved from v7]

---

## Aspirational Criteria

*Each full pass = 1 point. PARTIAL = 0.5. Max contributable to composite = 10. Raw count (max 24) is the tie-break.*

---

### C-09 -- Inter-Stage Blocker Detection
- **Category**: structure
- **Weight**: aspirational
- **Text**: The template includes a BLOCKER PROPAGATION RULE directing the executing model to tag any finding that creates a dependency on a downstream stage with a `[BLOCKER: F-ID from stage]` token. Absence of this token on a blocking finding is a named format failure, not a silent omission.
- **Pass condition**: BLOCKER PROPAGATION RULE present in the template. Template names absence of the token on a blocking finding as a format failure. Token format is `[BLOCKER: F-ID from stage]` or equivalent labeled form.

---

### C-10 -- Cross-Cutting Theme Elevation
- **Category**: structure
- **Weight**: aspirational
- **Text**: The ROB Summary includes a Cross-Cutting Themes table. When a concern appears across two or more stages, it must be elevated to a named cross-cutting theme row rather than remaining siloed in per-stage finding lists. The template specifies the minimum-one-row condition when multi-stage concerns exist.
- **Pass condition**: Cross-Cutting Themes table present in ROB Summary. Template states that any concern appearing in 2+ stages must be represented as a named theme row. Minimum-one-row condition when multi-stage concerns exist is explicit in the template.

---

### C-11 -- Handoff Packet
- **Category**: structure
- **Weight**: aspirational
- **Text**: The ROB Summary includes a Handoff Packet with three required labeled components: Cross-Stage References Forwarded (which findings travel to the downstream stage), Cross-Stage Synthesis (what the findings say together across stages), and Downstream Risk Shift (how the risk profile changes from the current stage's perspective). Prose without these labeled slots does not satisfy.
- **Pass condition**: Handoff Packet present with all three components as named labeled slots. Each component is structurally distinct -- not merged into a single prose block.

---

### C-12 -- Stage-Boundary Blocker Field
- **Category**: structure
- **Weight**: aspirational
- **Text**: Each stage includes a stage-boundary Blocker Field table recording four typed values: whether the stage is blocked (YES/NO), the F-ID of the blocking finding, the downstream stage affected, and the reason. This is a per-stage structural element distinct from the inter-stage blocker tokens in C-09.
- **Pass condition**: Blocker Field table present at each stage with four named columns: Blocker (YES/NO), F-ID, Downstream Stage, Reason. Template names all four as typed slots.

---

### C-13 -- Inertia Anchor
- **Category**: correctness
- **Weight**: aspirational
- **Text**: The template includes an INERTIA ANCHOR section with three required components: Status-Quo Competitor (naming what the proposed change displaces), Displacement Map (a register of labeled D-IDs documenting specific displacement risks), and Inertia Risk Statement (summarizing the combined inertia threat). The section converts inertia from a vague concern into a named, registered risk structure.
- **Pass condition**: INERTIA ANCHOR section present with all three components. Status-Quo Competitor names a specific entity. Displacement Map contains at least one D-ID labeled row. Inertia Risk Statement is a labeled slot, not a prose paragraph embedded in findings.

---

### C-14 -- Briefing Envelope
- **Category**: structure
- **Weight**: aspirational
- **Text**: Each stage template includes a Part 1 BRIEFING ENVELOPE with four named fields: ROLE (the persona assigned to this stage), LENS (the practice-domain orientation), KEY CONCERNS (top concerns selected through the Lens), and PRIOR-STAGE ESCALATIONS (findings forwarded from upstream stages). Anonymous or merged fields do not satisfy.
- **Pass condition**: BRIEFING ENVELOPE labeled as Part 1 and present with all four named fields as typed slots.

---

### C-15 -- Anti-Redundancy
- **Category**: format
- **Weight**: aspirational
- **Text**: The template includes explicit anti-redundancy guards on two slots. The Downstream Risk Shift field guard names Prior-Stage Lens Impact as the prohibited source of repetition ("Do not restate Prior-Stage Lens Impact"). The Cross-Stage Synthesis guard prohibits copying finding rows into prose ("do not copy rows into prose"). Both guards name the prohibited behavior explicitly -- not as a general style note.
- **Pass condition**: Anti-redundancy guard present on Downstream Risk Shift naming Prior-Stage Lens Impact as the prohibited repetition source. Anti-redundancy guard present on Cross-Stage Synthesis prohibiting row-to-prose copying. Both guards use named rejection language.

---

### C-16 -- Lens-Impact
- **Category**: structure
- **Weight**: aspirational
- **Text**: Stages 2 through 6 include a Prior-Stage Lens Impact table documenting how findings from the previous stage interact with the current stage's lens orientation. Stage 1 is exempt as it has no prior stage. The table is a named labeled slot, not embedded in the Briefing Envelope prose.
- **Pass condition**: Prior-Stage Lens Impact table present at stages 2 through 6. Stage 1 exempt. Table structurally distinct from Briefing Envelope fields.

---

### C-17 -- Risk-Shift Pair
- **Category**: structure
- **Weight**: aspirational
- **Text**: The template includes a Downstream Risk Shift field as a named structural slot distinct from the Prior-Stage Lens Impact table. The two form a directional pair: Lens Impact looks backward (what the prior stage surfaced), Risk Shift looks forward (what changes for the next stage). Merging them into a single slot collapses the direction distinction and fails this criterion.
- **Pass condition**: Downstream Risk Shift field present as a named slot. Field is structurally separate from Prior-Stage Lens Impact. Template does not merge or alias the two.

---

### C-18 -- Explicit Lens Fill Field
- **Category**: format
- **Weight**: aspirational
- **Text**: The Part 0 LENS ACTIVATION block includes an explicit fill field for the Dimension slot with inline rejection guidance specifying that role-title-only answers do not satisfy. The field prompts for a practice-domain term (e.g., "dependency sequencing", "adoption friction") rather than a role label (e.g., "TPM", "PM").
- **Pass condition**: Part 0 Dimension slot carries inline rejection guidance naming role-title-only as an insufficient fill. Guidance distinguishes a practice-domain term from a role label by example or by explicit statement.

---

### C-19 -- Stage 1 Lens Coverage
- **Category**: correctness
- **Weight**: aspirational
- **Text**: Stage 1 includes a Stage Identity Lens declaration specifying the lens dimension -- not just the role title. This is a Stage 1-specific element establishing lens coverage before any prior-stage context exists. It is not a substitute for Part 0 LENS ACTIVATION; it is a Stage 1 structural anchor.
- **Pass condition**: Stage 1 template contains a Stage Identity Lens declaration. Declaration requires a dimension (practice-domain term), not just the role title. Template names absence of the dimension as incomplete.

---

### C-20 -- Pre-Envelope Part 0 Block
- **Category**: format
- **Weight**: aspirational
- **Text**: The template places Part 0 LENS ACTIVATION before Part 1 BRIEFING ENVELOPE with an explicit sequencing instruction: Part 0 must be filled before reading any prior-stage context. This sequencing prevents lens contamination from upstream findings before the executing model has declared its own orientation.
- **Pass condition**: Part 0 LENS ACTIVATION block appears before Part 1 BRIEFING ENVELOPE in the template. Block includes explicit sequencing instruction ("Fill before reading any prior-stage context" or equivalent). Sequencing obligation is stated, not implied by ordering alone.

---

### C-21 -- KEY CONCERNS Back-Ref
- **Category**: correctness
- **Weight**: aspirational
- **Text**: The KEY CONCERNS cell in the BRIEFING ENVELOPE contains an explicit back-reference to Part 0 Dimension using the phrase "selected through the Lens declared in Part 0" or a functionally equivalent formulation. This enforces the Part 0 → KEY CONCERNS dependency as a template-visible obligation rather than an implicit expectation.
- **Pass condition**: KEY CONCERNS cell template text includes the phrase "selected through the Lens declared in Part 0" or equivalent back-reference naming Part 0 as the source of lens selection. Absence of the phrase means the dependency is not enforced structurally.

---

### C-22 -- Three-Hop Chain
- **Category**: structure
- **Weight**: aspirational
- **Text**: The template implements a navigable three-hop chain: Part 0 Dimension → KEY CONCERNS → Prior-Stage Lens Impact. Each hop carries an explicit cross-reference naming the source node by slot label. A reader tracing the chain can move from any node to the adjacent node using labeled references in the template itself.
- **Pass condition**: All three nodes present. Part 0 references forward to KEY CONCERNS. KEY CONCERNS references back to Part 0 (C-21) and forward to Lens Impact. Lens Impact references back to KEY CONCERNS. Cross-references are by slot name.

---

### C-23 -- Chain Health Summary
- **Category**: structure
- **Weight**: aspirational
- **Text**: The ROB Summary includes a LENS ACTIVATION CHAIN HEALTH table with one row per stage (6 rows) and 5 columns tracking chain completeness. Each row carries a COMPLETE / PARTIAL / BROKEN status reflecting the three-hop chain health for that stage. The table makes cross-stage lens coverage visible in a single scannable surface.
- **Pass condition**: LENS ACTIVATION CHAIN HEALTH table present in ROB Summary with 6 rows (one per stage) and 5 columns. Each row carries a COMPLETE / PARTIAL / BROKEN status. Table is in the ROB Summary section, not embedded within a stage.

---

### C-24 -- Fill-Slot Structural Completeness
- **Category**: format
- **Weight**: aspirational
- **Text**: Every template slot uses a declarative `[fill]` marker with inline rejection language naming at least one invalid fill value for that slot. The template includes an explicit statement (or equivalent) that a visible unfilled `[fill]` slot constitutes non-compliance. This structural obligation prevents partial completion from passing undetected.
- **Pass condition**: `[fill]` slot markers present throughout the template with inline rejection language per slot. Template states that a visible unfilled slot indicates non-compliance. At least one slot guard names a specific prohibited response by label.

---

### C-25 -- Displacement Map with D-IDs
- **Category**: correctness
- **Weight**: aspirational
- **Text**: The INERTIA ANCHOR's Displacement Map uses labeled D-IDs (e.g., D-01, D-02) as row identifiers. Each stage's INERTIA CHECK section must cite at least one D-ID from the Displacement Map register. Missing D-ID citation in an INERTIA CHECK is named as a format failure in the template. This converts the Displacement Map from a list of named risks into a citable register with per-stage citation obligations.
- **Pass condition**: Displacement Map rows carry labeled D-IDs. Template states that each stage's INERTIA CHECK must cite a D-ID from the Displacement Map. Missing D-ID citation in an INERTIA CHECK is explicitly named as a format failure.

---

### C-26 -- Table-First Findings Format
- **Category**: format
- **Weight**: aspirational
- **Text**: Findings are presented in a table-first format: the findings table appears before any narrative findings prose in each stage section. Each column in the findings table carries inline rejection language naming at least one invalid cell value. Table-first ordering makes findings machine-checkable before narrative interpretation and prevents prose from substituting for structured data.
- **Pass condition**: Findings table appears before narrative findings prose in each stage section. Inline column guards present naming at least one invalid response per column. Table-first format applied to all stage finding sections. See C-29 for named scope exceptions.

---

### C-27 -- D-ID Ref Column as Per-Row Structural Obligation
- **Category**: correctness
- **Weight**: aspirational
- **Text**: The findings table includes a dedicated `D-ID Ref` column as a 6th typed slot. When Inertia Stance is RESISTANT and Severity is HIGH, the cell must contain a D-ID from the Displacement Map register (C-25); otherwise N/A. This converts C-25's per-finding citation requirement from a prose Inertia Check note -- where "reference the inertia contribution as a factor" satisfies the wording without naming a D-ID -- into a per-row cell obligation that an executing model cannot satisfy without a specific register entry. Variations that lack this column drift to the prose form because no slot exists to fill.
- **Pass condition**: `D-ID Ref` column present as the 6th typed column in the findings table. Template names the conditional fill obligation: D-ID from the Displacement Map register when Inertia Stance is RESISTANT and Severity is HIGH; N/A otherwise. Template names the empty-cell case under RESISTANT+HIGH as a format failure.

---

### C-28 -- Named Anti-Pattern Rejection Phrases in D-ID Ref Column Guard
- **Category**: format
- **Weight**: aspirational
- **Text**: The `D-ID Ref` column guard names at least one explicit invalid cell value and rejects it by condition -- specifically, "N/A does not satisfy when Inertia Stance is RESISTANT and Severity is HIGH." Extends C-24/C-26's fill-with-rejection-language pattern into the D-ID Ref cell: naming the borderline-valid response (N/A is syntactically valid; it is not semantically valid under RESISTANT+HIGH) closes the gap between structural presence and citation compliance. The rejection phrase must appear inline in the column template, not only in a table-level footer. Requires C-27 (N/A when C-27 absent).
- **Pass condition**: D-ID Ref column guard names "N/A" (or equivalent) as an invalid cell value under the RESISTANT+HIGH condition. Rejection phrase is inline in the column guide, not only in a table footer or rubric annotation.

---

### C-29 -- Explicit Scope-Exception Calibration for Table-First Format
- **Category**: format
- **Weight**: aspirational
- **Text**: The template contains a named SCOPE-EXCEPTION CALIBRATION section identifying output types that are exempt from C-26's table-first findings format, with rationale for each exception. The GO/NO-GO signal and stage Verdict labels are the canonical exempt types: unambiguous labeled signals are degraded, not improved, by tabular rendering. The section closes the table-first architecture by making the exception boundary explicit in the template itself rather than only in the rubric's design note. Requires C-27 (N/A when C-27 absent -- meaningful only within the 6-column architecture that introduced the conditional format-failure family and therefore requires a defined scope boundary).
- **Pass condition**: SCOPE-EXCEPTION CALIBRATION section present in the template. Section names at least two exempt output types (TPM GO/NO-GO signal, stage Verdict labels) with rationale for each. Exemptions are declared in the template, not only in rubric annotations.

---

### C-30 -- Resolution Evidence as Per-Row Citation Obligation in Blocker Resolution Status Table
- **Category**: correctness
- **Weight**: aspirational
- **Text**: The Blocker Resolution Status table (C-09/C-12) includes a `Resolution Evidence` column as a named typed slot. When Resolution Status is RESOLVED, the cell must contain a specific artifact citation -- a finding F-ID, a handoff packet reference, or an equivalent traceable pointer -- not a prose summary of what was resolved. Column guard names at least two explicit invalid cell values: "Discussed" does not satisfy this column; "See findings" does not satisfy this column. An empty or generic cell when Resolution Status is RESOLVED is a format failure. Converts C-09/C-12's blocker tracking from status-only (RESOLVED/UNRESOLVED) to traceable resolution, closing the gap between declaring a blocker resolved and citing the evidence for that resolution. Requires C-09 and C-12 (N/A when absent).
- **Pass condition**: `Resolution Evidence` column present in Blocker Resolution Status table. Column guard names "Discussed" and "See findings" (or equivalent) as invalid. An empty or generic cell when Resolution Status is RESOLVED is explicitly named as a format failure.

---

### C-31 -- Primary F-IDs Column as Per-Stage Citation Obligation in Cross-Cutting Themes Table
- **Category**: correctness
- **Weight**: aspirational
- **Text**: The Cross-Cutting Themes table (C-10) includes a `Primary F-IDs` column as a named typed slot. Each theme row must contain at least one F-ID per named stage in which the concern appears -- not a prose description of the theme's scope. Column guard names at least two explicit invalid cell values: "Multiple findings" does not satisfy this column; "See findings" does not satisfy this column. A theme row without an F-ID per named stage is a format failure. Converts cross-cutting theme identification from a prose claim (theme X appears in stages Y and Z) into a per-stage finding citation obligation, making themes traceable to specific findings rather than asserted from summary memory. Requires C-10 (N/A when absent).
- **Pass condition**: `Primary F-IDs` column present in Cross-Cutting Themes table. Column guard names "Multiple findings" and "See findings" (or equivalent) as invalid. A theme row without an F-ID per named stage is explicitly named as a format failure.

---

### C-32 -- Addressing F-IDs Column as Forward-Citation Obligation in Handoff Packet
- **Category**: correctness
- **Weight**: aspirational
- **Text**: The Handoff Packet's Cross-Stage References Forwarded section (C-11) includes an `Addressing F-IDs` column as a named typed slot. For each finding forwarded to a downstream stage, the cell names the F-IDs in the receiving stage expected to address it -- or explicitly marks the entry OPEN when no addressing finding has yet been identified. Column guard names at least one explicit invalid cell value: "TBD" does not satisfy this column. An empty cell for a forwarded finding is a format failure. Extends C-11's handoff tracking from a one-way forwarding record into a bidirectional citation that links each forwarded concern to its downstream treatment. Requires C-11 (N/A when absent).
- **Pass condition**: `Addressing F-IDs` column present in the Handoff Packet's Cross-Stage References Forwarded section. Column guard names "TBD" (or equivalent) as invalid. An empty cell for a forwarded finding is explicitly named as a format failure. OPEN is the valid explicit marker for a forwarded concern with no current addressing finding.
```
