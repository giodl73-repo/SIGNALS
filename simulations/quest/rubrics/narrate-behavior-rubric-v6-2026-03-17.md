Written to `simulations/quest/rubrics/narrate-behavior-rubric-v6-2026-03-17.md`.

---

**What changed — summary:**

**2 new criteria extracted from R5 scorecard:**

| Criterion | Pattern | Source | Key rule |
|-----------|---------|--------|----------|
| C-21 -- Back-Annotation of S1-S2 Findings with B-IDs | `back-annotate-findings-with-bids` | V-22, V-24 | BACK-ANNOTATE step updates FINDING TABLE rows (not EXIT GATEs) with "text-name (B-NN)" after registry compilation |
| C-22 -- Discovery Pathway Audit in REPORT | `registry-type-discovery-audit` | V-23 | REPORT includes `| Registry Type | B-IDs | Finding Count | F-IDs |` audit table enabling the inertia-vs-contract meta-finding |

**1 signal not codified:** `condensed-simulate-equivalence` (V-24) — condensed SIMULATE blocks satisfy all structural requirements. Same treatment as R4 SIGNAL-3. Notes added to C-10 and C-11 pass conditions crediting V-24.

**C-19 pass condition updated:** Added clause clarifying that back-annotation is not required for C-19 (that's C-21's job), keeping the two criteria cleanly separated.

**Tier rebalancing:** Aspirational 13→15. Threshold 7→8. Cap unchanged at 10 pts.
-08--C-22  | 10     | Any 8 of 15 earns the cap       |
| **Total**     |             | **80** |                                 |

---

## Essential Criteria (40 points total, 10 pts each)

### C-01 -- Declared Execution Sequence
- **Weight**: essential
- **Category**: format
- **Text**: The skill variation declares the order in which sub-skills will be simulated
  before the first simulation section executes. The declared sequence must be explicit and
  complete -- naming each sub-skill step -- and the simulation sections must follow that
  declared order. Reordering sub-skills mid-execution without updating the declaration
  is a violation.
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

## Aspirational Criteria (10 points total, capped; any 8 of 15 earns the cap)

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
  sections are independent of upstream sections with no cross-reference. Partial pass (half
  credit) if cross-references exist but use only section numbers without naming the specific
  boundary.
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
  meaningful; without type labels, grouping is not possible.
- **Pass condition**: The REPORT includes a DISCOVERY PATHWAY AUDIT table (or equivalent
  named block) with columns for: Registry Type, B-IDs, Finding Count, and F-IDs. At least
  two registry types are represented. Fail if the audit table is absent. Partial pass (half
  credit) if a type-based grouping is present but omits Finding Count or F-ID enumeration,
  making the table a summary rather than an auditable cross-reference.
- **Source pattern**: registry-type-discovery-audit (R5 excellence signal; V-23)

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
