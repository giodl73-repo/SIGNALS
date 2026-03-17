---
skill: quest-rubric
skill_target: narrate-behavior
date: 2026-03-17
version: 10
---

# Scoring Rubric — narrate-behavior

**Skill**: Run the full technical simulation campaign. Orchestrates: flow-lifecycle,
flow-conversation, trace-state, trace-contract, trace-permissions in sequence. Output:
simulation findings report ranked by blast radius. Use before implementation to find spec
gaps and contract violations.

**Scoring formula**:
- Essential: 4 criteria x 10 pts = 40 pts (all must pass)
- Recommended: 3 criteria x 10 pts = 30 pts
- Aspirational: cap 10 pts (any 13 of 27 criteria earn full cap; each criterion +1 pass toward threshold)
- **Total maximum: 80 pts**

**Golden threshold**: all essential pass + composite >= 80.

---

## Essential Criteria (40 points total, 10 pts each -- all must pass)

### C-01 -- Declared Execution Sequence
- **Weight**: essential
- **Category**: correctness
- **Text**: The skill variation explicitly declares the execution sequence of sub-skills
  before any simulation section begins. Execution must match the declared order. Reordering
  sub-skills mid-execution without updating the declaration is a violation.
- **Pass condition**: Variation contains an explicit sequence declaration before the first
  simulation section, and the simulation sections appear in that declared order. Fail if
  no sequence is declared, or if the executed order differs from the declared order.

### C-02 -- Output Is a Single Unified Report
- **Weight**: essential
- **Category**: format
- **Text**: All five sub-skill simulation sections and the consolidated findings must be
  produced as one continuous output -- not as five separate outputs, not as a series of
  individual sub-skill reports delivered one at a time. The report must carry a single
  title and date stamp at the top.
- **Pass condition**: The output is a single document with one CONSOLIDATED FINDINGS REPORT
  title block. Fail if sub-skill sections are delivered as separate outputs, or if the
  report has no unifying title/date.

### C-03 -- Findings Ranked by Blast Radius
- **Weight**: essential
- **Category**: completeness
- **Text**: Findings are ranked by blast radius -- the scope of downstream impact if the
  finding is not addressed before implementation. High blast radius = many flows, components,
  or contracts affected; low blast radius = isolated, contained impact. The ranking must be
  explicit, not implied by position alone.
- **Pass condition**: Report contains a ranked findings list (numbered or tiered) with blast
  radius as the stated sort key. At least one finding is labeled or annotated with its blast
  radius scope. Fail if findings are unranked, sorted alphabetically, or sorted by any key
  other than blast radius without justification.

### C-04 -- At Least One Spec Gap or Contract Violation Identified
- **Weight**: essential
- **Category**: coverage
- **Text**: The report surfaces at least one concrete spec gap (something underspecified or
  absent from the target spec) or contract violation (a boundary condition where caller and
  callee assumptions diverge). The finding must name the specific spec location or contract
  boundary affected.
- **Pass condition**: Report contains at least one finding with: (a) finding type labeled as
  spec-gap or contract-violation, (b) a specific reference to where in the spec the gap or
  violation occurs, (c) a description of what is missing or mismatched. Fail if all findings
  are vague observations without spec anchoring.

---

## Recommended Criteria (30 points total, 10 pts each)

### C-05 -- Finding Schema: Source + Location + Impact
- **Weight**: recommended
- **Category**: depth
- **Text**: Each finding includes three fields as distinct labeled entries: (1) source
  sub-skill that discovered it, (2) spec or contract location where it was found, (3) impact
  description of what breaks if the finding is unresolved before implementation. Impact must
  be a standalone labeled field -- merging impact into the problem description does not
  satisfy this criterion.
- **Pass condition**: At least 80% of findings include all three fields as separately labeled
  entries. Pass if the report uses a consistent finding schema (e.g., table or structured
  list) that captures source, location, and impact as distinct columns or fields. Partial
  pass (half credit) if fields are present but inconsistently populated, or if impact is
  merged with the problem description.

### C-06 -- Cross-Sub-Skill Coverage
- **Weight**: recommended
- **Category**: coverage
- **Text**: The ranked findings list draws from at least three of the five sub-skills,
  demonstrating that the campaign exercised the full skill set rather than concentrating
  findings in one area. Sub-skill attribution must be explicit -- each finding identifies
  which sub-skill surface produced it.
- **Pass condition**: Findings section attributes results to three or more distinct
  sub-skills by name. Fail if all findings are attributed to one or two sub-skills, or if
  sub-skill attribution is absent. Partial pass (half credit) if attribution is present for
  exactly two sub-skills.

### C-07 -- Remediation Guidance Present
- **Weight**: recommended
- **Category**: depth
- **Text**: Each finding includes a remediation field -- a concrete recommended action, spec
  update, or contract clarification that would close the finding before implementation. The
  remediation must be a standalone labeled field, not folded into the impact or problem
  description.
- **Pass condition**: At least 80% of findings include a populated remediation field as a
  distinct labeled entry. Partial pass (half credit) if remediation is present but merged
  with impact, or is a generic placeholder ("address this") rather than a concrete action.

---

## Aspirational Criteria (10 points total, capped; any 13 of 27 earns the cap)

### C-08 -- Severity Classification Applied
- **Weight**: aspirational
- **Category**: depth
- **Text**: Each finding carries an explicit severity label (e.g., critical/high/medium/low
  or an equivalent named scale). The scale must be defined or cited in the report before
  it is applied. Severity enables readers to triage findings without reading the full blast
  radius rationale.
- **Pass condition**: All findings have a severity label from a declared scale. The scale
  definition appears in the report header or a preamble section. Fail if severity is absent
  from any finding, or if the scale is applied inconsistently without a definition.

### C-09 -- Empty Sub-Skill Disposition Declared
- **Weight**: aspirational
- **Category**: format
- **Text**: Sub-skills that produce no findings explicitly declare "no findings" with a brief
  rationale (e.g., "scope clean under current spec version") rather than being silently
  omitted. Silent omission is indistinguishable from a skipped execution -- an explicit
  disposition is needed for the report to be auditable.
- **Pass condition**: Every sub-skill section -- including zero-finding sub-skills -- contains
  an explicit disposition. Fail if any sub-skill section is absent or blank. Partial pass
  (half credit) if a "no findings" declaration is present but carries no rationale.

### C-10 -- Pre-Committed Finding Table Schema
- **Weight**: aspirational
- **Category**: format
- **Text**: The skill variation commits to a finding table schema upfront -- before simulation
  sections execute -- with columns for all required schema fields: sub-skill source, spec or
  contract location, impact, remediation, and severity. A pre-committed column schema makes
  C-05/C-07/C-08 compliance structural rather than prose-dependent: field merging becomes a
  column violation, not just a style lapse.
- **Pass condition**: The skill variation defines a FINDING TABLE schema (or equivalent
  column header block) before findings are collected, with separate named columns for
  sub-skill, location, impact, remediation, and severity. Fail if findings are rendered as
  free prose without a column schema. Partial pass (half credit) if a table is used but
  omits one or more required columns. Condensed SIMULATE blocks (abbreviated simulation
  output) satisfy this criterion equivalently to full-prose simulation output; simulation
  verbosity is not a factor provided the schema commitment precedes all sections.
- **Source pattern**: pre-committed-table (R1 excellence signal); condensed-simulate
  equivalence confirmed R5 (V-24)

### C-11 -- Exit Gate Per Sub-Skill Section
- **Weight**: aspirational
- **Category**: format
- **Text**: Each sub-skill section ends with an explicit EXIT GATE block that requires the
  executor to declare: (a) all finding F-IDs produced (or NONE), (b) spec-gap F-IDs (or
  NONE), (c) contract-violation F-IDs (or NONE). The EXIT GATE converts C-09 from an
  aspirational style guideline into a structural prompt requirement -- a missing EXIT GATE
  block is a prompt structure violation, not merely an omitted entry. Condensed format
  ("Spec-gaps: [F-IDs or NONE]") satisfies this criterion; label length is not a factor.
  Condensed SIMULATE blocks do not affect EXIT GATE requirements: each section must still
  carry a complete EXIT GATE regardless of how condensed the simulation prose is.
- **Pass condition**: All five sub-skill sections contain an EXIT GATE block with fields for
  findings summary, spec-gap F-IDs, and contract-violation F-IDs. Fail if any section lacks
  an EXIT GATE. Partial pass (half credit) if EXIT GATE blocks are present but do not require
  explicit spec-gap and contract-violation F-ID enumeration.
- **Source pattern**: exit-gate-per-section (R1 excellence signal); condensed-simulate
  equivalence confirmed R5 (V-24)

### C-12 -- Report-Level Post-Conditions Declared
- **Weight**: aspirational
- **Category**: coverage
- **Text**: The REPORT assembly step includes an explicit REQUIRE or post-conditions block
  that states rubric-mirroring checks -- e.g., "3+ sub-skills represented", "1+ spec-gap or
  contract-violation with location", "findings sorted by blast radius". This acts as a late
  catch: a report assembled from sparse per-section outputs that individually passed their
  EXIT GATEs can still be flagged if the aggregate fails a post-condition.
- **Pass condition**: The report assembly step includes a REQUIRE block listing at minimum:
  cross-sub-skill coverage floor (3+), spec-gap or contract-violation requirement (1+), and
  blast-radius sort confirmation. Fail if the REQUIRE block is absent. Partial pass (half
  credit) if post-conditions are present but incomplete -- e.g., coverage check only, no
  spec-gap or sort check.
- **Source pattern**: report-level-postconditions (R1 excellence signal)

### C-13 -- Downstream-Anchored Simulation
- **Weight**: aspirational
- **Category**: depth
- **Text**: Sub-skill sections S3-S5 (or equivalent later sections) explicitly name and
  reference the contract boundaries established in S1-S2 (or equivalent earlier sections)
  when identifying findings. Each downstream finding traces back to a named upstream
  boundary -- not just to the spec in general. This creates a verification chain: a violation
  in S4 is anchored to the specific contract declared in S1, making blast radius estimation
  concrete rather than qualitative.
- **Pass condition**: At least two downstream sections (S3-S5) contain explicit named
  references to contract boundaries or findings from upstream sections (S1-S2). Each
  referenced boundary is named (not just cited by section number). Fail if downstream
  sections are independent of upstream sections with no cross-reference. Partial pass
  (half credit) if cross-references exist but use only section numbers without naming the
  specific boundary.
- **Source pattern**: downstream-anchored-simulation (R2 excellence signal; V-09)

### C-14 -- Inertia-as-Spec-Gap Mapping
- **Weight**: aspirational
- **Category**: coverage
- **Text**: When the simulation includes inertia or status-quo framing (e.g., INERTIA blocks,
  "what the current behavior assumes"), observations of status-quo silence or underspecified
  transition behavior are explicitly converted to labeled spec-gap findings rather than left
  as inertia commentary. Each inertia observation that exposes an underspecification names
  the comparison point -- the current behavior or assumption being contrasted with the target
  spec -- as part of the finding.
- **Pass condition**: All inertia observations that identify underspecification appear in the
  finding table as spec-gap type, with: (a) the status-quo behavior named as the comparison
  point, (b) the spec location where the gap exists, (c) EXIT GATE spec-gap F-ID
  enumeration. Fail if inertia blocks produce observations that do not appear in the finding
  table. Partial pass (half credit) if mapping is present but comparison points are unnamed
  or spec locations are absent.
- **Source pattern**: inertia-as-spec-gap (R2 excellence signal; V-08, V-10)

### C-15 -- Boundary Registry as Structural Artifact
- **Weight**: aspirational
- **Category**: format
- **Text**: A BOUNDARY REGISTRY block is compiled between S2 and S3 (after early sections
  establish contracts, before downstream sections consume them), assigning named boundary
  IDs (B-IDs) to each contract boundary identified. EXIT GATE fields in S3-S5 that require
  "B-IDs referenced" enumeration convert C-13 downstream cross-references from a style
  expectation into a structural, auditable constraint. Without B-IDs, a reviewer must
  interpret whether named references are sufficient; with B-IDs, a missing reference is an
  enumerable gap. Compact one-line-per-entry format (`B-NN: name -- type -- description`)
  satisfies this criterion equivalently to a full table; tabular structure is not required.
- **Pass condition**: A BOUNDARY REGISTRY block appears between the last early section (S2
  or equivalent) and the first downstream section (S3 or equivalent), with at least two
  named B-IDs. At least one downstream EXIT GATE explicitly enumerates B-IDs referenced in
  that section. Fail if BOUNDARY REGISTRY is absent or placed after S3. Partial pass (half
  credit) if BOUNDARY REGISTRY is present with B-IDs but no downstream EXIT GATE references
  B-IDs explicitly.
- **Source pattern**: boundary-registry-as-artifact (R3 excellence signal; V-11, V-15); compact
  equivalence confirmed R4 (SIGNAL-3)

### C-16 -- Inertia-Boundary Cross-Reference
- **Weight**: aspirational
- **Category**: depth
- **Text**: INERTIA blocks in downstream sections (S3-S5) open by identifying which named
  upstream boundary the status-quo behavior assumes. This construction satisfies C-13
  (named upstream reference) and C-14 (inertia-to-spec-gap conversion) simultaneously in a
  single finding row: the INERTIA block names the boundary, and the resulting finding enters
  the table as a spec-gap with the named boundary as the comparison point. When B-ID format
  is used (C-15), the linkage is maximally mechanical -- one B-ID reference closes both
  downstream-anchor and inertia-mapping requirements. C-16 applies to downstream sections
  (S3-S5) only; INERTIA blocks in upstream sections (S1-S2) are C-14 contributors, not
  C-16 obligors.
- **Pass condition**: At least one INERTIA block in a downstream section opens with an
  explicit statement of which named upstream boundary (by B-ID or boundary name) the
  status-quo assumes. The resulting observation appears in the finding table as a spec-gap
  with the named boundary as the comparison point and a spec location populated. Fail if
  INERTIA blocks in downstream sections make no reference to upstream boundaries. Partial
  pass (half credit) if the boundary reference exists but the resulting finding is not typed
  as spec-gap or lacks the comparison point.
- **Source pattern**: inertia-boundary-crossref (R3 excellence signal; V-14, V-15)

### C-17 -- Structural Column Independence for Severity and Blast Radius
- **Weight**: aspirational
- **Category**: format
- **Text**: Severity and Blast Radius appear as distinct named columns in the pre-committed
  finding table schema (C-10), structurally enforcing their independence. When column
  separation is present, prose instructions such as "independent of blast radius; never
  merge" are confirmed redundant -- a column violation is detectable without prose, and the
  prose is token overhead. Pass requires the two fields to be separate columns; presence or
  absence of prose instruction is neither required nor penalized.
- **Pass condition**: The pre-committed finding table schema includes Severity and Blast
  Radius as two separate named columns. Fail if either field is absent from the schema, or
  if the two fields share a column. Partial pass (half credit) if both fields are present
  but one is embedded in a combined column (e.g., "Severity / Blast Radius").
- **Source pattern**: severity-blast-column-independence (R3 excellence signal; V-13)

### C-18 -- Boundary Registry Type Field
- **Weight**: aspirational
- **Category**: depth
- **Text**: Each entry in the BOUNDARY REGISTRY (C-15) carries a named type field that
  categorizes the boundary by its discovery pathway. Recognized types include
  `contract-boundary` (explicitly declared in the spec), `permission-grant` (access-control
  or authorization boundary), and `inertia-boundary` (surfaced through INERTIA analysis
  rather than spec declaration). The `inertia-boundary` type is the key new class: it
  records how a boundary was found -- through implicit assumption analysis -- not just what
  it is. A typed registry is queryable by discovery method, enabling a reviewer to enumerate
  all assumption-surfaced boundaries separately from declared contracts.
- **Pass condition**: The BOUNDARY REGISTRY includes a named type label for each B-ID entry.
  At least one entry carries a named type (e.g., `contract-boundary`, `permission-grant`,
  `inertia-boundary`). Fail if the registry assigns B-IDs without any type labels. Partial
  pass (half credit) if type labels are present for some entries but not all, or if types
  are present but unlabeled (e.g., no type column name).
- **Source pattern**: inertia-boundary-type-in-registry (R4 excellence signal; V-17, V-19)

### C-19 -- Pre-Registry Inertia Discovery Pipeline
- **Weight**: aspirational
- **Category**: depth
- **Text**: INERTIA blocks in upstream sections (S1-S2) discover and name boundaries by
  text-name before the BOUNDARY REGISTRY is compiled. The BOUNDARY REGISTRY then promotes
  those text-names to formal B-IDs. Downstream INERTIA blocks (S3-S5) cite B-IDs that
  trace back to S1-S2 discoveries. This two-phase pipeline creates a full traceability
  chain: text-name discovery in S1-S2 -> formal B-ID assignment in the registry ->
  structural citation in S3-S5. S1-S2 findings referencing boundaries by text-name in the
  Location field are valid before registry compilation; back-annotation of S1-S2 findings
  with B-IDs is not required for this criterion (see C-21).
- **Pass condition**: INERTIA blocks appear in at least one upstream section (S1 or S2),
  naming boundaries by text. Those text-named boundaries appear in the BOUNDARY REGISTRY
  as formal B-IDs. At least one downstream INERTIA block (S3-S5) cites a B-ID that traces
  back to an S1-S2 text-name discovery. Fail if INERTIA analysis is confined to downstream
  sections only and no pre-registry boundary naming occurs in S1-S2. Partial pass (half
  credit) if S1-S2 INERTIA blocks are present and name boundaries, but those text-names do
  not appear in the BOUNDARY REGISTRY as B-IDs.
- **Source pattern**: text-name-to-BID-promotion-pipeline (R4 excellence signal; V-17, V-19, V-20)

### C-20 -- Dual-Purpose B-IDs Exit Gate Field
- **Weight**: aspirational
- **Category**: format
- **Text**: In uniform condensed EXIT GATE format, a single B-IDs field serves dual
  semantics across section tiers: registration semantics in upstream sections (S1-S2,
  declaring boundaries-to-register) and audit semantics in downstream sections (S3-S5,
  enumerating B-IDs referenced in findings). Section context disambiguates field purpose;
  the executor instructions must explicitly state the dual-purpose semantics. This pattern
  reduces asymmetric per-tier EXIT GATE design -- where S1-S2 gates carry different field
  names than S3-S5 gates -- to a uniform 5-field format that is fully C-11 compliant and
  lower-overhead. Both Inertia=NONE (clean upstream section) and Inertia!=NONE (INERTIA
  block present in S1-S2) are valid configurations in the condensed gate.
- **Pass condition**: The variation uses a uniform condensed EXIT GATE format across all
  five sub-skill sections with a single B-IDs field whose content differs by section tier
  (registration list in S1-S2, audit list in S3-S5). Executor instructions explicitly state
  the dual-purpose semantics (e.g., "S1-S2: list boundaries to register; S3-S5: list
  B-IDs referenced"). Fail if the variation uses asymmetric EXIT GATE designs with
  different field names per section tier. Partial pass (half credit) if a uniform format
  is used but the dual-purpose semantics are not explicitly documented in the executor
  instructions.
- **Source pattern**: dual-purpose-BID-exit-gate-field (R4 excellence signal; V-18, V-20)

### C-21 -- Back-Annotation of S1-S2 Findings with B-IDs
- **Weight**: aspirational
- **Category**: depth
- **Text**: After the BOUNDARY REGISTRY is compiled, a BACK-ANNOTATE step updates S1-S2
  FINDING TABLE rows whose Location field contains a boundary text-name, adding the formal
  B-ID assigned in the registry. Format: "text-name (B-NN)". EXIT GATE content is not
  modified: S1-S2 EXIT GATEs carry text-names as emitted at section completion, which is
  correct because B-IDs do not exist at section-completion time. This creates bidirectional
  traceability -- S1-S2 findings retrospectively carry B-ID anchors that downstream sections
  can verify -- while preserving the C-19 pass condition that text-name discovery in S1-S2
  is valid before registry compilation. The REQUIRE block in REPORT can confirm back-
  annotation completeness by checking that all S1-S2 rows whose Location carried a boundary
  text-name now show "text-name (B-NN)" format.
- **Pass condition**: The variation includes a BACK-ANNOTATE step positioned between the
  BOUNDARY REGISTRY and S3. The step targets FINDING TABLE rows only (not EXIT GATE
  content), and the resulting S1-S2 rows show "text-name (B-NN)" format in Location for
  any row whose pre-annotation Location named a boundary. Fail if back-annotation modifies
  EXIT GATE content. Fail if no BACK-ANNOTATE step is present when S1-S2 INERTIA blocks
  named boundaries that were promoted to B-IDs. Partial pass (half credit) if a back-
  annotation step is present but incomplete -- some boundary-named rows are updated while
  others remain in text-name-only form.
- **Source pattern**: back-annotate-findings-with-bids (R5 excellence signal; V-22, V-24)

### C-22 -- Discovery Pathway Audit in REPORT
- **Weight**: aspirational
- **Category**: coverage
- **Text**: The REPORT assembly step includes a DISCOVERY PATHWAY AUDIT table that groups
  BOUNDARY REGISTRY entries by type, showing the B-IDs, finding count, and F-IDs associated
  with each registry type. This table enables a structural meta-finding: when inertia-
  boundary findings outnumber contract-boundary findings, the feature's implicit-assumption
  surface exceeds its declared contract surface -- a signal that the spec's explicit coverage
  understates behavioral complexity. The audit table requires C-18 (typed registry) to be
  meaningful; without type labels, grouping is not possible. Note: C-23 (unconditional
  discovery-pathway-ratio REQUIRE) adds an obligation on top of this criterion -- a variation
  may pass C-22 with a conditional observation while still failing C-23 for omitting the
  unconditional REQUIRE form.
- **Pass condition**: The REPORT includes a DISCOVERY PATHWAY AUDIT table (or equivalent
  named block) with columns for: Registry Type, B-IDs, Finding Count, and F-IDs. At least
  two registry types are represented. Fail if the audit table is absent. Partial pass (half
  credit) if a type-based grouping is present but omits Finding Count or F-ID enumeration,
  making the table a summary rather than an auditable cross-reference.
- **Source pattern**: registry-type-discovery-audit (R5 excellence signal; V-23)

### C-23 -- Unconditional Discovery-Pathway-Ratio REQUIRE
- **Weight**: aspirational
- **Category**: coverage
- **Text**: The variation promotes the discovery-pathway-ratio observation from a conditional
  signal ("if inertia > contract, note...") to an unconditional REQUIRE obligation. All
  three ratio directions must produce a required meta-finding statement in the REPORT: (a)
  inertia-boundary > contract-boundary, (b) contract-boundary > inertia-boundary, (c) equal
  counts. Equality is a signal -- a balanced registry indicates neither assumption surface
  nor declared contract surface dominates, which is itself diagnostic. A variation that only
  triggers a meta-finding on one direction (e.g., only when inertia dominates) fails this
  criterion even if C-22 passes. The unconditional form must appear in both DEFINITIONS
  (declaring the three ratio forms and their required statements) and in the REPORT REQUIRE
  block (confirming the meta-finding statement is present). Condensed DEFINITIONS that
  reference ratio codes (a)/(b)/(c) without spelling out individual forms with per-form
  required statements do not satisfy this criterion -- DEFINITIONS ratio-form declarations
  are load-bearing and cannot be condensed to code references.
- **Pass condition**: The variation's DEFINITIONS section declares three explicit ratio forms
  and states a required meta-finding statement for each. The REPORT REQUIRE block includes
  a check: "discovery-pathway-ratio meta-finding statement present -- required regardless
  of ratio direction." Fail if only one or two ratio directions trigger a required statement.
  Fail if the ratio rule appears only as a conditional observation in REPORT without a
  DEFINITIONS-level declaration. Fail if DEFINITIONS condenses the three forms to code
  references without individual per-form statements. Partial pass (half credit) if the
  unconditional form is declared in DEFINITIONS but the REPORT REQUIRE check is absent.
- **Source pattern**: unconditional-discovery-pathway-ratio-require (R6 SIGNAL-1; V-27, V-29, V-30);
  condensed-DEFINITIONS-failure confirmed R9 (V-43)

### C-24 -- Exhaustive Inertia-Disposition Completeness Check
- **Weight**: aspirational
- **Category**: coverage
- **Text**: Every named INERTIA assumption across the full simulation is assigned one of
  four outcome dispositions: FINDING (assumption exposed a spec-gap, entered in finding
  table), COVERED (spec already addresses the assumed behavior adequately), INVESTIGATION
  (coverage ambiguous -- needs further analysis but not confirmed underspecification), or
  NONE (no assumption identified in this section). A REQUIRE check in the REPORT verifies
  that no assumption is unresolved -- every named assumption carries exactly one disposition.
  COVERED satisfies C-09 zero-finding rationale (confirming spec coverage is a valid
  "no finding" outcome); INVESTIGATION is distinct from C-14 inertia-to-spec-gap mapping
  because it does not confirm underspecification -- it flags ambiguity for follow-up without
  claiming a gap. The REQUIRE check is aggregate: it verifies completeness across all
  assumptions enumerated in all INERTIA blocks, not section by section.
- **Pass condition**: The variation defines the four dispositions (FINDING / COVERED /
  INVESTIGATION / NONE) in DEFINITIONS or preamble. The REPORT REQUIRE block includes a
  completeness check: "all named INERTIA assumptions carry one of the four dispositions."
  Fail if any named assumption lacks a disposition. Fail if the completeness check is
  absent from REPORT REQUIRE. Partial pass (half credit) if dispositions are defined and
  applied per-section but no aggregate completeness check is present in REPORT REQUIRE.
- **Source pattern**: exhaustive-inertia-disposition-completeness-check (R6 SIGNAL-2; V-30)

### C-25 -- Inertia-Disposition Coverage Score
- **Weight**: aspirational
- **Category**: depth
- **Text**: The REPORT disposition summary computes a spec-coverage density score from the
  aggregate inertia-disposition counts: the percentage of INERTIA assumptions that became
  FINDING (spec-gap conversion rate), the percentage that were COVERED (confirmed spec
  coverage rate), and the percentage that remain INVESTIGATION (ambiguity rate). This score
  is distinct from C-23 (which compares registry types by discovery pathway -- inertia-
  boundary vs. contract-boundary -- to assess assumption-surface breadth) and from C-22
  (which audits finding counts per registry type). C-25 measures how inertia assumptions
  resolved: a high FINDING rate signals the spec has structural gaps in currently-assumed
  behavior; a high COVERED rate signals the spec is well-defended against inertia; a high
  INVESTIGATION rate signals ambiguity that should be resolved before implementation. The
  score requires C-24 (exhaustive disposition assignment) to be meaningful -- a coverage
  score computed from incomplete dispositions is not a valid density signal.
- **Pass condition**: The REPORT includes a disposition summary block that enumerates total
  INERTIA assumptions and computes at minimum: % FINDING, % COVERED, % INVESTIGATION as
  labeled fields. A brief interpretation statement accompanies the score (e.g., "high
  FINDING rate indicates..."). Fail if the coverage score is absent from REPORT. Fail if
  the score is present but uninterpreted (raw counts only, no percentage or density framing).
  Partial pass (half credit) if percentages are present but not labeled by disposition type,
  or if the interpretation statement is absent.
- **Source pattern**: inertia-disposition-ratio-as-coverage-score (R6 SIGNAL-3; V-30)

### C-26 -- Covered-Disposition Spec-Citation Registry
- **Weight**: aspirational
- **Category**: coverage
- **Text**: COVERED dispositions are not merely inline annotations within INERTIA blocks --
  each COVERED outcome must cite the specific spec section that addresses the assumed
  behavior (format: "spec covers: [section or clause]"). These citations are collected into
  a COVERAGE CITATION INDEX in REPORT, with one row per COVERED disposition containing:
  Assumption (text), Sub-Skill (source section), Spec Section Cited, and B-ID (if applicable).
  The INDEX creates an auditable "spec-defense surface" -- the set of assumptions the spec
  explicitly handles, enumerable and verifiable at REPORT level. A high COVERED count is
  only meaningful when the cited sections are enumerable; without the INDEX, a reviewer
  cannot distinguish well-defended coverage from uncited claims. REPORT REQUIRE enforces:
  "All COVERED dispositions cite a specific spec section" and "COVERAGE CITATION INDEX
  contains one row per COVERED disposition."
- **Pass condition**: COVERED dispositions within INERTIA blocks include a "spec covers:
  [section]" citation. A COVERAGE CITATION INDEX block appears in REPORT with columns for
  Assumption, Sub-Skill, Spec Section Cited, and B-ID. REPORT REQUIRE checks include both
  citation completeness and INDEX row count matching COVERED disposition count. Fail if
  COVERED dispositions are emitted without spec-section citations. Fail if no COVERAGE
  CITATION INDEX appears in REPORT. Partial pass (half credit) if citations are present
  within INERTIA blocks but not collected into a REPORT-level INDEX, or if the INDEX is
  present but REQUIRE checks are absent.
- **Source pattern**: covered-disposition-spec-citation-registry (R7 SIGNAL-1; V-32, V-34, V-35)

### C-27 -- Investigation Triage Gate as Structural Artifact
- **Weight**: aspirational
- **Category**: format
- **Text**: INVESTIGATION dispositions are routed to two targets simultaneously: an
  observation-type row in the FINDING TABLE (existing behavior) AND a resolution entry in
  a TRIAGE GATE compilation section positioned between S5 and REPORT. The TRIAGE GATE
  collects all INVESTIGATION findings with: (a) Priority assignment (HIGH/MED/LOW derived
  from Blast Radius and B-ID citation count), (b) a "Verify Before Implementation" field
  stating what must be confirmed before the ambiguity can be resolved. REQUIRE enforces
  zero-escape: no INVESTIGATION disposition exits the simulation without a corresponding
  TRIAGE GATE entry. This mirrors how BOUNDARY REGISTRY converts scattered text-name
  references into a named, typed structural artifact -- TRIAGE GATE converts scattered
  INVESTIGATION observations into a prioritized pre-implementation resolution queue. C-01
  compatibility: TRIAGE GATE is a compilation step, not a simulation section; it must be
  declared in the execution sequence before S1 and appear in the declared position (after
  S5 and before REPORT).
- **Pass condition**: A TRIAGE GATE block appears between S5 and REPORT in the declared
  execution sequence. The TRIAGE GATE contains one entry per INVESTIGATION disposition
  produced across all five sections, with Priority and Verify Before Implementation fields
  populated. REPORT REQUIRE includes: "all INVESTIGATION dispositions appear in TRIAGE GATE
  (zero-escape check)." TRIAGE GATE declared in the sequence before S1. Fail if no TRIAGE
  GATE is present when INVESTIGATION dispositions were emitted. Fail if TRIAGE GATE appears
  in the sequence but is not declared. Partial pass (half credit) if TRIAGE GATE is present
  with entries but lacks Priority assignment or Verify Before Implementation field, or if
  zero-escape REQUIRE check is absent from REPORT.
- **Source pattern**: investigation-triage-gate-as-structural-artifact (R7 SIGNAL-2; V-33, V-35)

### C-28 -- Full Disposition Traceability Chain
- **Weight**: aspirational
- **Category**: depth
- **Text**: Each of the four inertia dispositions routes to a named artifact target,
  declared explicitly in DEFINITIONS before any simulation section executes: FINDING ->
  FINDING TABLE (spec-gap or contract-violation row), COVERED -> COVERAGE CITATION INDEX
  (citation row), INVESTIGATION -> FINDING TABLE (observation row) + TRIAGE GATE
  (resolution entry), NONE -> inline statement only. This declaration makes the disposition
  system fully observable at REPORT level: a reviewer can audit which assumptions produced
  spec-gaps (FINDING TABLE), which are spec-defended (COVERAGE CITATION INDEX), which are
  unresolved ambiguities (TRIAGE GATE), and which are out-of-scope (inline). The traceability
  chain is the analog of C-19's text-name-to-B-ID pipeline: dispositions become first-class
  routing decisions rather than annotation tags, and completeness is verifiable per-artifact
  rather than per-assumption. Requires C-24 (four dispositions defined), C-26 (COVERAGE
  CITATION INDEX), and C-27 (TRIAGE GATE) to be structurally satisfiable; however C-28 can
  pass independently if artifact routing is declared in DEFINITIONS even when C-26/C-27
  criteria are not individually evaluated.
- **Pass condition**: DEFINITIONS (or preamble before S1) declares all four disposition
  artifact targets by name. REPORT can enumerate: total FINDING TABLE rows, total COVERAGE
  CITATION INDEX rows, total TRIAGE GATE entries, and total inline NONE statements. Fail
  if artifact routing is absent from DEFINITIONS. Fail if REPORT cannot audit completeness
  per-artifact (i.e., no row counts or entry counts per artifact type in REPORT REQUIRE).
  Partial pass (half credit) if artifact routing is declared in DEFINITIONS but REPORT does
  not enforce per-artifact completeness counts, or if INVESTIGATION dual-routing (FINDING
  TABLE + TRIAGE GATE) is not explicitly declared as a two-target route.
- **Source pattern**: full-disposition-traceability-chain (R7 SIGNAL-3; V-35)

### C-29 -- Inertia Surface as Pre-Simulation Structural Artifact
- **Weight**: aspirational
- **Category**: format
- **Text**: An INERTIA SURFACE compilation step is declared in the execution sequence and
  positioned before S1, cataloging all anticipated inertia assumptions upfront and assigning
  A-NN IDs before any simulation section executes. This is the pre-simulation analog of
  TRIAGE GATE (which compiles INVESTIGATION dispositions post-S5): INERTIA SURFACE compiles
  the assumption inventory before simulation rather than after. Pre-cataloging converts
  inertia discovery from an emergent per-section activity into a planned forward contract --
  the executor declares what assumptions will be evaluated before evaluating any of them.
  Without INERTIA SURFACE, assumption counts are only knowable by traversing all five
  sections after the fact; with it, the catalog total is declared at the start and REPORT
  can verify completeness as a count equation against a fixed baseline. C-01 compatibility:
  INERTIA SURFACE is a compilation step, not a simulation section; it must be declared in
  the execution sequence before S1.
- **Pass condition**: An INERTIA SURFACE block appears before S1 in the declared execution
  sequence. Each anticipated inertia assumption is assigned an A-NN ID with a brief
  description. REPORT REQUIRE references the catalog total (e.g., "A-NNs-assigned covers
  all N catalog entries") to confirm no assumption was discovered post-catalog without
  catalog update. Fail if no INERTIA SURFACE step is present when REPORT patterns reference
  an A-NN catalog total. Fail if INERTIA SURFACE appears in execution but is not declared
  in the sequence. Partial pass (half credit) if an INERTIA SURFACE step is present but
  A-NN IDs are not assigned, or if REPORT does not reference the catalog total in a REQUIRE
  check.
- **Source pattern**: inertia-surface-as-pre-simulation-artifact (R8 SIGNAL-1; V-38, V-40)

### C-30 -- Assumption Catalog Reconciliation as Report Arithmetic
- **Weight**: aspirational
- **Category**: coverage
- **Text**: The REPORT includes an ASSUMPTION CATALOG RECONCILIATION block that converts
  C-24's prose completeness obligation into verifiable arithmetic: (a) total catalog entries
  (A-NNs total from INERTIA SURFACE), (b) total A-NNs assigned to dispositions across all
  EXIT GATEs (A-NNs-assigned), (c) unassigned count (A-NNs total minus A-NNs-assigned,
  must equal 0). This promotes C-28's DEFINITIONS-level artifact routing declaration from
  a structural declaration to a quantitatively verified completeness claim -- a reviewer
  confirms disposition completeness by checking that unassigned = 0 rather than by reading
  routing intent in DEFINITIONS. New assumptions discovered mid-simulation that were not in
  the original INERTIA SURFACE catalog must be reflected in a catalog update before REPORT,
  keeping the reconciliation arithmetic valid. Requires C-29 (INERTIA SURFACE) to supply
  the catalog baseline; without a pre-committed catalog total, the reconciliation has no
  fixed reference and reduces to a tautology.
- **Pass condition**: REPORT includes an ASSUMPTION CATALOG RECONCILIATION block with three
  labeled fields: total catalog entries (A-NNs total), assigned entries (A-NNs-assigned
  summed across all EXIT GATEs), and unassigned count. REQUIRE check: "unassigned = 0."
  Fail if the reconciliation block is absent. Fail if the block is present but lacks the
  three-field structure or the unassigned=0 REQUIRE. Partial pass (half credit) if catalog
  total and assigned count are present but the unassigned delta is not computed or the
  REQUIRE check is absent.
- **Source pattern**: assumption-catalog-reconciliation-as-report-arithmetic (R8 SIGNAL-2;
  V-38, V-40)

### C-31 -- Assumption Conservation Equation in Report
- **Weight**: aspirational
- **Category**: depth
- **Text**: The REPORT includes an ASSUMPTION CONSERVATION section that states a four-term
  partition equation: N_finding + N_covered + N_investigation + N_none = N_total, where
  each term is the count of assumptions carrying that named disposition, and N_total equals
  the INERTIA SURFACE catalog total. A residual check confirms the equation balances
  (residual = 0). All four disposition counts must appear as separately labeled terms in the
  summation -- merging N_finding and N_investigation into a single N_inertia_rows term fails
  this criterion because a reviewer cannot verify the FINDING/INVESTIGATION split from the
  equation alone. Crucially, N_investigation must equal the TRIAGE GATE entry count (each
  INVESTIGATION A-NN produces exactly one TRIAGE GATE entry by zero-escape REQUIRE); this
  cross-artifact equality is independently verifiable and is the strongest realization of
  C-28 -- each N-term is derivable from its named artifact. REPORT REQUIRE must explicitly
  state "all 4 terms populated as labeled fields." Requires C-24 (four dispositions defined)
  and C-29 (INERTIA SURFACE catalog) to be structurally satisfiable.
- **Pass condition**: REPORT includes an ASSUMPTION CONSERVATION block (or equivalent named
  section) with per-disposition row counts as four separately labeled numeric fields
  (N_finding, N_covered, N_investigation, N_none), a four-term summation equation
  (N_finding + N_covered + N_investigation + N_none = N_total), and a residual check
  comparing N_total to the INERTIA SURFACE catalog count (residual = 0). REPORT REQUIRE
  states "all 4 terms populated as labeled fields." Fail if the conservation equation is
  absent from REPORT. Fail if any of the four disposition counts is merged or omitted from
  the summation (3-term form fails). Partial pass (half credit) if per-disposition counts
  are present and summed as four terms but no residual check against the INERTIA SURFACE
  catalog total is stated, or if the REQUIRE check omits the "all 4 terms" assertion.
- **Source pattern**: assumption-conservation-equation-in-report (R8 SIGNAL-3; V-39, V-40);
  4-term-assumption-conservation-equation (R9 SIGNAL-1; V-41, V-44, V-45) -- corrective
  form confirmed; 3-term form (V-40, V-42, V-43) confirmed FAIL

### C-32 -- Risk Density Matrix
- **Weight**: aspirational
- **Category**: depth
- **Text**: The REPORT includes a RISK DENSITY MATRIX -- a 3x3 grid with Blast Radius
  (WIDE / MEDIUM / NARROW) as rows and Severity (HIGH / MED / LOW) as columns, with F-IDs
  listed in each cell. The WIDE x HIGH quadrant is the critical triage zone. A REQUIRE
  check enforces that every F-ID in the FINDING TABLE appears in exactly one matrix cell
  (no duplicates, no omissions). The matrix is orthogonal to the sorted FINDING TABLE
  (which gives total order by blast radius but collapses intra-tier severity signal) and to
  the DISCOVERY PATHWAY AUDIT (which groups by registry type): the RISK DENSITY MATRIX
  surfaces cross-dimensional clustering -- e.g., whether WIDE-blast findings cluster in
  HIGH or LOW severity -- at a glance. Requires C-08 (severity scale) and C-17 (separate
  Severity and Blast Radius columns) to supply consistent scale labels.
- **Pass condition**: REPORT includes a RISK DENSITY MATRIX block with labeled rows for
  three blast-radius tiers (WIDE/MEDIUM/NARROW or equivalent named scale) and labeled
  columns for three severity tiers (HIGH/MED/LOW or equivalent). Each cell lists F-IDs
  (or NONE). REPORT REQUIRE includes: "every F-ID appears in exactly one matrix cell."
  Fail if the matrix is absent from REPORT. Fail if the matrix uses unlabeled rows or
  columns. Fail if the REQUIRE check is absent. Partial pass (half credit) if the matrix
  is present with labels and F-IDs but the zero-escape REQUIRE check is absent, or if the
  matrix uses fewer than 3x3 tiers without justification.
- **Source pattern**: risk-density-matrix (R9 SIGNAL-2; V-42)

### C-33 -- Lifecycle Phase Structure in S3
- **Weight**: aspirational
- **Category**: depth
- **Text**: S3 (flow-lifecycle simulation) decomposes into five named sequential lifecycle
  phases: INIT / NOMINAL / DEGRADED / TEARDOWN / HANDOFF (or an equivalent declared
  set). Each phase emits a PHASE EXIT CONDITION block that declares: (a) B-IDs active in
  this phase, (b) findings produced (F-IDs or NONE), (c) A-NNs assigned in this phase,
  (d) NONE-count if no findings. S3's single aggregate EXIT GATE sums across all five
  phases. REPORT gains an S3 phase breakdown table (phase / F-IDs / B-IDs active). The
  phase decomposition forces blast-radius attribution to a lifecycle stage: a finding
  in DEGRADED commonly stresses multiple B-IDs simultaneously and carries a different blast
  profile than the same finding in NOMINAL. Phase-boundary inertia -- assumptions that hold
  in one phase but not another -- is exposed by this structure and would collapse in a flat
  lifecycle simulation. C-01 compatibility: S3 remains one declared section in the execution
  sequence; PHASE blocks are structure within the section, not additional simulation
  sections.
- **Pass condition**: S3 contains five (or more) named sequential phase blocks with declared
  names. Each phase block ends with a PHASE EXIT CONDITION listing B-IDs active, F-IDs
  produced, and A-NNs assigned. S3's aggregate EXIT GATE sums phase outputs. REPORT includes
  an S3 phase breakdown table. Fail if S3 is executed as a flat simulation with no phase
  decomposition. Fail if PHASE EXIT CONDITIONs are absent from any phase block. Partial
  pass (half credit) if phases are declared and named but PHASE EXIT CONDITIONs omit one
  or more required fields (B-IDs active, F-IDs, A-NNs).
- **Source pattern**: lifecycle-phase-structure (R9 SIGNAL-3; V-44)

### C-34 -- Boundary Risk Density Score
- **Weight**: aspirational
- **Category**: depth
- **Text**: The CROSS-ARTIFACT UTILIZATION MATRIX (or equivalent boundary summary table in
  REPORT) is extended with a Risk Density Score (RDS) column per B-ID. For each boundary:
  RDS = sum of blast_weight(F) over all findings referencing that B-ID, where
  WIDE = 3, MEDIUM = 2, NARROW = 1. B-IDs are sorted by RDS descending in the matrix.
  A portfolio-level invariant is enforced in REPORT REQUIRE: sum of all RDS values equals
  the total blast-weighted finding count for B-ID-anchored findings. The RDS converts the
  qualitative per-artifact profile (FT/CI/TG presence) into an ordinal ranking: two
  boundaries with identical artifact profiles but different blast-radius distributions are
  distinguished by RDS. This is orthogonal to C-22 (which asks which discovery pathway
  yields more findings) and to C-32 (which surfaces cross-dimensional clustering across
  all findings): RDS answers which specific boundary carries the most blast-weighted risk,
  enabling prioritized boundary hardening before implementation.
- **Pass condition**: The REPORT boundary summary table includes an RDS column computed
  as sum(blast_weight(F)) per B-ID, with blast weights WIDE=3/MEDIUM=2/NARROW=1 declared
  or cited. B-IDs are sorted by RDS descending. REPORT REQUIRE includes the portfolio-level
  invariant check: "sum(all RDS) = total blast-weighted finding count for B-ID-anchored
  findings." Fail if no RDS column is present. Fail if blast weights are not declared.
  Fail if the portfolio-level invariant is absent from REPORT REQUIRE. Partial pass (half
  credit) if RDS is computed and B-IDs are sorted but the portfolio-level invariant REQUIRE
  check is absent, or if blast weights are applied inconsistently without a declared scale.
- **Source pattern**: boundary-risk-density-score (R9 SIGNAL-4; V-45)

---

## Version History

| Version | Criteria      | Essential  | Recommended | Aspirational                        | Notes                                                                                                                           |
|---------|---------------|------------|-------------|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| v1      | C-01 -- C-09  | C-01--C-04 | C-05--C-07  | C-08--C-09 (5 pts ea)               | Baseline rubric                                                                                                                 |
| v2      | C-01 -- C-12  | C-01--C-04 | C-05--C-07  | C-08--C-12 (2 pts ea)               | +C-10/C-11/C-12 from R1 excellence signals; aspirational tier rebalanced to 5 criteria                                          |
| v3      | C-01 -- C-14  | C-01--C-04 | C-05--C-07  | C-08--C-14 (cap 10; any 5 of 7)     | +C-13/C-14 from R2 excellence signals; condensed-register-equivalence confirmed, not codified                                   |
| v4      | C-01 -- C-17  | C-01--C-04 | C-05--C-07  | C-08--C-17 (cap 10; any 6 of 10)    | +C-15/C-16/C-17 from R3 excellence signals; severity-blast-column-independence confirmed structural                             |
| v5      | C-01 -- C-20  | C-01--C-04 | C-05--C-07  | C-08--C-20 (cap 10; any 7 of 13)    | +C-18/C-19/C-20 from R4 excellence signals; compact-registry-structural-equivalence confirmed in C-15, not codified separately  |
| v6      | C-01 -- C-22  | C-01--C-04 | C-05--C-07  | C-08--C-22 (cap 10; any 8 of 15)    | +C-21/C-22 from R5 excellence signals; condensed-simulate-equivalence confirmed in C-10/C-11 notes, not codified separately     |
| v7      | C-01 -- C-25  | C-01--C-04 | C-05--C-07  | C-08--C-25 (cap 10; any 10 of 18)   | +C-23/C-24/C-25 from R6 excellence signals; unconditional-meta-finding-additive-to-audit-table resolved (not codified)          |
| v8      | C-01 -- C-28  | C-01--C-04 | C-05--C-07  | C-08--C-28 (cap 10; any 11 of 21)   | +C-26/C-27/C-28 from R7 excellence signals; full disposition traceability chain codified; all R7 open questions resolved YES    |
| v9      | C-01 -- C-31  | C-01--C-04 | C-05--C-07  | C-08--C-31 (cap 10; any 12 of 24)   | +C-29/C-30/C-31 from R8 excellence signals; INERTIA SURFACE pre-simulation artifact, catalog reconciliation arithmetic, assumption conservation equation codified |
| v10     | C-01 -- C-34  | C-01--C-04 | C-05--C-07  | C-08--C-34 (cap 10; any 13 of 27)   | +C-32/C-33/C-34 from R9 excellence signals; C-31 updated to require 4-term form (3-term form confirmed FAIL); C-23 note added re: condensed DEFINITIONS failure; risk-density-matrix, lifecycle-phase-structure, boundary-risk-density-score codified |
