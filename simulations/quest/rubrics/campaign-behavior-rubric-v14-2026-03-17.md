`simulations/quest/rubrics/campaign-behavior-rubric-v14-2026-03-17.md` written.

**Three new criteria extracted from R15 excellence signals:**

| Criterion | Source | Category | What it adds |
|-----------|--------|----------|-------------|
| **C-43** | R15 V-01 | rigor | QL concurrent-boundary gate fires between Q6 and QH; forces cross-row concurrent phase-boundary reasoning (re-entry collisions, escalation races) not prompted by the Phase 4 table; QL-sourced findings tagged `src: flow-lifecycle (QL)` as a named attribution class declared in DEFINITIONS |
| **C-44** | R15 V-02 | rigor | Q5 HIGH-RISK triage classifies I-NN assumptions by blast x spec-coverage; VERDICT restructured to open with inertia-averted paragraph before top-finding paragraph — shifts campaign narrative from what-we-found to what-would-have-shipped-unchallenged |
| **C-45** | R15 V-05 | structure | Q8 source-field vocabulary extended to declare `"flow-lifecycle (QL)"` as a recognized valid value; closes false-negative gap when QL-sourced findings enter the completeness gate |

**Structural notes:**
- Denominator 34 -> 37; formula `(passed/37) x 10`
- V-01/V-02: 35/37 = 9.46 -> 9, total **89**
- V-03: 34/37 = 9.19 -> 9, total **89**
- V-04: 36/37 = 9.73 -> 10, total **90**
- V-05: 37/37, total **90** (true perfect)
- New ceiling: all 19 aspirational landmarks C-27 through C-45
s how broadly a failure propagates
  across the system.
- **Pass condition:** Output includes a ranked findings list where ranking criterion is
  explicitly stated as blast radius (or equivalent: propagation scope, system-wide
  impact). Random order or severity-only ranking = FAIL.

---

### C-03 — Spec gaps identified or explicitly cleared
- **Weight:** essential
- **Category:** coverage
- **Text:** The report either names at least one spec gap found during the campaign, or
  explicitly states that no spec gaps were detected. A spec gap is a condition, state
  transition, or contract term that the spec does not address but the simulation exposes.
- **Pass condition:** Output contains a labeled "spec gaps" section (or equivalent
  heading) with findings or a clear "none found" statement. Omitting the section
  entirely = FAIL.

---

### C-04 — Contract violations surfaced or explicitly cleared
- **Weight:** essential
- **Category:** correctness
- **Text:** The report either names at least one contract violation found during the
  campaign, or explicitly states that no violations were detected. A contract violation
  is a producer/consumer mismatch, broken invariant, or privilege boundary crossed.
- **Pass condition:** Output contains a labeled "contract violations" section (or
  equivalent heading) with findings or a clear "none detected" statement, naming both
  producer and consumer for each violation. Omitting the section entirely = FAIL.

---

### C-05 — Lifecycle violations surfaced or explicitly cleared
- **Weight:** essential
- **Category:** correctness
- **Text:** The flow-lifecycle sub-skill evaluates exception paths for each lifecycle
  phase, not only the happy path. The report either names lifecycle violations found
  or explicitly states that none were detected.
- **Pass condition:** flow-lifecycle output includes an exception path column or
  equivalent evaluation. Exit criteria requires all phases evaluated. Omitting
  exception paths entirely = FAIL.

---

## Recommended Criteria (30 pts total)

### C-06 — Blast radius label per finding
- **Weight:** recommended
- **Category:** correctness
- **Text:** Every finding carries an explicit blast radius label. The label must use a
  named tier: WIDE / MEDIUM / NARROW (or equivalent: SYSTEMIC / ISOLATED / LOCAL).
  Unlabeled findings cannot be ranked and cannot be compared across campaigns.
- **Pass condition:** Every finding block includes a blast radius field with a named
  tier value. Any finding missing the label = FAIL.

---

### C-07 — Confirmation status per finding
- **Weight:** recommended
- **Category:** correctness
- **Text:** Every finding carries an explicit confirmation status: CONFIRMED, RUNTIME
  ANOMALY, or equivalent named tier. Status must appear as a labeled field, not
  inferred from prose.
- **Pass condition:** Every finding block includes a confirmation status field with a
  named value. Any finding missing the field = FAIL.

---

### C-08 — Sub-skill attribution per finding
- **Weight:** recommended
- **Category:** coverage
- **Text:** Every finding identifies the sub-skill (source phase) that produced it.
  Attribution enables traceability back to the originating analysis and supports
  compound finding detection across phases.
- **Pass condition:** Every finding block includes a source phase field naming the
  sub-skill. Any finding missing attribution = FAIL.

---

## Aspirational Criteria (37 criteria, score = passed/37 x 10)

### C-09 — F-NN sequential finding IDs
- **Category:** structure
- **Text:** Findings are assigned sequential IDs (F-01, F-02, ... or Finding 1, Finding
  2, ...) in blast-radius order. Sequential IDs enable cross-referencing in spec gap
  citations, compound finding declarations, and post-campaign tracking.
- **Pass condition:** All findings carry sequenced numeric IDs. IDs align with
  blast-radius ranking order. Unsequenced or missing IDs = FAIL.

---

### C-10 — Lifecycle phase tag per flow finding
- **Category:** structure
- **Text:** Flow-lifecycle and flow-trigger findings include a lifecycle phase tag
  (e.g., INIT, ACTIVE, SUSPENDED, TERMINAL) indicating which phase the finding
  belongs to. Phase tags enable phase-specific blast radius comparison.
- **Pass condition:** Phase tag column or field present in both flow sub-skill outputs.
  Phase values use named lifecycle tiers, not free text. Missing column = FAIL.

---

### C-11 — Compound findings identified
- **Category:** correctness
- **Text:** The campaign identifies findings that originate from multiple sub-skills
  (compound findings). A compound finding is one whose blast radius can only be
  determined by combining evidence from two or more phases.
- **Pass condition:** Exit criteria or CONSOLIDATE section explicitly tracks compound
  anchor hits or multi-source attributions. Absence of any compound tracking = FAIL.

---

### C-12 — Spec gap missing-clause citation
- **Category:** correctness
- **Text:** Each spec gap finding includes a citation to the specific clause, section,
  or contract term that is absent from the spec. "Gap exists" without locating the
  missing clause is incomplete.
- **Pass condition:** Every spec gap finding names the missing clause (or states
  "clause not present" with enough specificity to locate it). Gaps without citations
  = FAIL.

---

### C-13 — Contract violations name producer and consumer
- **Category:** correctness
- **Text:** Each contract violation finding names both the producing component and the
  consuming component. Violations identified without both parties cannot be resolved
  because ownership is ambiguous.
- **Pass condition:** Every contract violation finding names producer and consumer.
  Violations missing either party = FAIL.

---

### C-14 — Privilege escalation paths surfaced or cleared
- **Category:** coverage
- **Text:** The trace-permissions sub-skill tracks privilege escalation paths
  explicitly. The report either names escalation paths found or states "none
  detected."
- **Pass condition:** A labeled "privilege escalation paths" field or section appears
  in the output with findings or a clear "none detected" statement. Omitting the
  field entirely = FAIL.

---

### C-15 — Severity with defined scale
- **Category:** structure
- **Text:** Each finding includes a severity rating using a defined scale (high / med
  / low or equivalent). The scale definition must appear in the output (DEFINITIONS
  section or equivalent) so reviewers can interpret ratings consistently.
- **Pass condition:** Severity field present in every finding block; scale definition
  present in output. Any finding missing severity, or scale undefined, = FAIL.

---

### C-16 — Executive summary top-3 surfaced
- **Category:** communication
- **Text:** A reader assessing campaign risk can identify the three highest-impact
  findings without reading the full report. This may be satisfied by a dedicated
  Executive Summary section or by a ranked findings list where the top three appear
  first with blast radius and confirmation labeled.
- **Pass condition:** Top three findings are identifiable (by position or explicit
  labeling) with blast radius and confirmation status present for each. No way to
  identify top three = FAIL.

---

### C-17 — Evidence basis per CONFIRMED finding
- **Category:** correctness
- **Text:** Every finding classified CONFIRMED cites the matching evidence from
  earlier phases (e.g., "matches Phase 1 finding F-03"). CONFIRMED without an
  evidence citation is an unverified assertion.
- **Pass condition:** Every CONFIRMED finding names the matching prior-phase finding
  or evidence source. CONFIRMED without citation = FAIL.

---

### C-18 — Q1-Qn calibration questions (n >= 3)
- **Category:** rigor
- **Text:** The campaign includes at least three named calibration questions (Q1-Qn)
  with specific re-grounding targets. Calibration questions serve as explicit
  checkpoints that prevent the campaign from drifting into generic analysis.
- **Pass condition:** n >= 3 calibration questions present, each with a named
  re-grounding target. Fewer than three, or questions without targets, = FAIL.

---

### C-19 — Atomic 7-field finding block
- **Category:** structure
- **Text:** Each finding uses a standardized atomic block with exactly seven labeled
  fields: (1) finding name/title, (2) source phase, (3) blast radius, (4) severity,
  (5) description, (6) confirmation status, (7) recommendation or next action.
  Consistent structure enables mechanical comparison across findings and campaigns.
- **Pass condition:** All seven fields explicitly numbered and labeled in every
  finding block. Missing or merged fields = FAIL.

---

### C-20 — Tiebreaker protocol stated and applied
- **Category:** correctness
- **Text:** When two findings have equal blast radius, a tiebreaker protocol
  determines their relative order. The protocol must be stated in the output and
  its application documented (stating whether any ties were encountered).
- **Pass condition:** Tiebreaker protocol appears in DEFINITIONS or equivalent; output
  states whether ties occurred and how they were resolved. Protocol absent = FAIL.

---

### C-21 — SYSTEMIC findings enumerate affected phases
- **Category:** correctness
- **Text:** Any finding classified SYSTEMIC must enumerate the specific lifecycle
  phases affected. Binary "SYSTEMIC: yes" without a phase list is not valid because
  it cannot be verified or compared. Phase enumeration is what distinguishes a
  genuine SYSTEMIC classification from an inflated one.
- **Pass condition:** Every SYSTEMIC finding lists the affected phases by name.
  SYSTEMIC without phase list = FAIL.

---

### C-22 — State-anchor execution order
- **Category:** structure
- **Text:** trace-state is designated as the first sub-skill to execute, with explicit
  rationale that it pre-classifies blast radius candidates from shared-state topology
  before contract, access, or flow analysis begins. This sequencing ensures downstream
  sub-skills inherit the state topology classification rather than producing
  independent and potentially inconsistent blast radius assessments.
- **Pass condition:** trace-state is identified as Phase 1 (or equivalent first
  position) with stated rationale linking its execution order to blast radius
  pre-classification. Any ordering that places trace-state after other analytical
  sub-skills = FAIL. Rationale without explicit first-position designation = PARTIAL.

---

### C-23 — Permissions-anchor positioned before flow sub-skills
- **Category:** structure
- **Text:** trace-permissions is designated before flow-lifecycle and flow-trigger,
  with explicit rationale that flow violations crossing a privilege boundary are
  SYSTEMIC by definition. Without the permissions anchor in place, flow sub-skills
  cannot correctly classify blast radius for privilege-crossing findings.
- **Pass condition:** trace-permissions is identified as executing before all flow
  sub-skills, with stated rationale linking privilege boundary classification to
  flow blast radius correctness. Any ordering that places trace-permissions after a
  flow sub-skill = FAIL. Rationale without explicit ordering statement = PARTIAL.

---

### C-24 — Anchor tags on phase headers
- **Category:** structure
- **Text:** Phase headers for the state anchor (Ph1) and permissions anchor (Ph2)
  carry explicit `[ANCHOR:...]` tags identifying their role in the execution
  dependency chain. Anchor tags make the dependency scannable from headers alone --
  a reviewer can confirm anchor ordering without reading phase body text.
- **Pass condition:** Ph1 and Ph2 headers (or equivalent anchor-phase designations)
  include an `[ANCHOR:...]` tag or equivalent inline marker naming the anchor role.
  Anchor rationale present only in body text, with no scannable header marker = FAIL.

---

### C-25 — Q6 sequence integrity gate
- **Category:** rigor
- **Text:** A dedicated calibration question (Q6 or equivalent named gate) validates
  anchor ordering at runtime: it asks whether Ph1 ran before Ph2, Ph2 ran before
  Ph3-Ph5, and whether the ordering produced the intended pre-classification benefits.
  The sequence integrity gate is a self-check that fires after the phases complete,
  not a structural declaration made before execution begins.
- **Pass condition:** A calibration question explicitly validates anchor execution
  order and asks whether the pre-classification benefit was realized. Structural
  ordering stated in DEFINITIONS without a post-execution validation question = FAIL.

---

### C-26 — Propagation chain in blast radius field
- **Category:** correctness
- **Text:** Field 3 (blast radius) of each finding block includes an explicit
  propagation chain tracing the failure path from origin to terminus
  (e.g., "ComponentA -> ServiceB -> ConsumerC -> terminus"). The chain makes the blast
  radius classification mechanically auditable: a reviewer can follow each hop and
  verify the WIDE / MEDIUM / NARROW tier assignment rather than accepting an
  asserted label. The chain must also appear in the finding's VERDICT and in the
  campaign DEFINITIONS, and Q1 must trace the chain to terminus.
- **Pass condition:** Field 3 includes a propagation chain with named hops. VERDICT
  restates the chain. DEFINITIONS establish chain format. Q1 traces to terminus.
  All four elements required. Blast radius label without a chain = FAIL. Chain in
  field 3 only, without VERDICT and Q1 restatement = PARTIAL.

---

### C-27 — Chain Terminus Registry in Phase 0
- **Category:** correctness
- **Text:** A numbered T-NN table is declared in Phase 0 (or a dedicated REGISTRY
  section) listing every valid terminal blast surface. Every propagation chain in
  field 3, EXECUTIVE SUMMARY, and VERDICT must resolve to a T-NN entry from the
  registry, or be flagged "unresolved chain -- registry miss: [component name]." Chains
  that miss the registry are excluded from ranking. This converts terminus validation
  from a DEFINITIONS prose audit -- where a reviewer must re-read definitional text
  and match free-form component names -- to a table lookup against canonical entries.
  Without the registry, two chains that describe the same terminal surface can use
  different component names and appear distinct.
- **Pass condition:** A T-NN numbered table appears before phase execution begins.
  Every chain resolves to a T-NN entry or is explicitly flagged. Registry absent, or
  chains not referencing T-NN entries = FAIL. Registry present but chains use free-form
  names without T-NN notation = PARTIAL.

---

### C-28 — Dedicated Executive Summary heading
- **Category:** communication
- **Text:** A `## EXECUTIVE SUMMARY` section (or equivalent dedicated heading) appears
  before the ranked findings list and contains exactly three structured bullets, one
  per top finding. Each bullet carries: F-NN ID, blast-radius tier, abbreviated
  propagation chain, and confirmation status. This makes top-3 identification
  position-independent -- a reader does not need to locate the ranked list and verify
  that the first three entries carry the required fields. C-16 can pass without this
  criterion (via ranked-list inference); C-28 requires the dedicated heading
  specifically.
- **Pass condition:** A dedicated `## EXECUTIVE SUMMARY` (or equivalent labeled)
  section appears with exactly three structured bullets. Each bullet names F-NN,
  blast-radius tier, chain, and confirmation. Top-3 identified only through ranked
  list position = FAIL for C-28 (does not affect C-16 score).

---

### C-29 — Inline CONFIRMED evidence citation in field 6
- **Category:** correctness
- **Text:** The field 6 template encodes the evidence citation directly: format is
  `"CONFIRMED -- evidence: [phase name]: [matching finding description]"`. CONFIRMED
  without the inline citation fails the block format -- the citation is not a
  recommended practice but a structural requirement enforced at four locations:
  field 6 template, VERDICT format, EXECUTIVE SUMMARY bullet format, and Q2
  calibration question. C-17 can pass with a DEFINITIONS-level instruction to cite
  evidence; C-29 requires the citation to be embedded in the field template itself
  so that omission fails the block without requiring a separate prose check.
- **Pass condition:** Field 6 template uses `CONFIRMED -- evidence: [phase]: [finding]`
  format (or equivalent structural embedding). VERDICT and EXECUTIVE SUMMARY bullets
  encode the same citation requirement. Q2 audits inline citation presence. Evidence
  citation present only as a DEFINITIONS instruction, not in the field template = FAIL.
  Template present in field 6 but absent from VERDICT or EXECUTIVE SUMMARY = PARTIAL.

---

### C-30 — EXECUTIVE SUMMARY chains reference T-NN terminus codes
- **Category:** correctness
- **Text:** When both a Phase 0 terminus registry (C-27) and a dedicated EXECUTIVE
  SUMMARY section (C-28) are present, the propagation chain in each EXECUTIVE SUMMARY
  bullet must reference the terminus using its T-NN registry code, not a free-form
  component name (e.g., `-> T-04` not `-> DataLayer`). This cross-links the two
  structures: the summary is not an independent narrative but a view over the same
  canonical registry that governs chain validation in field 3 and VERDICT. Without
  T-NN notation in the summary, a reviewer cannot confirm that the summary terminal
  matches the registry entry without manually re-reading the Phase 0 table.
  V-02 (R10) demonstrated the failure mode: EXECUTIVE SUMMARY present, terminus
  registry absent from V-02's design -- bullets used free-form names that could diverge
  from registry entries without triggering a validation error.
- **Pass condition:** Every EXECUTIVE SUMMARY bullet chain terminus uses `[terminal: T-NN]`
  notation (or inline T-NN code) matching a Phase 0 registry entry. Free-form terminal
  names in EXECUTIVE SUMMARY bullets = FAIL. EXECUTIVE SUMMARY or registry absent =
  FAIL (both C-27 and C-28 must be present for C-30 to be satisfiable).

---

### C-31 — EXECUTIVE SUMMARY bullets carry inline evidence citations
- **Category:** correctness
- **Text:** The confirmation slot in each EXECUTIVE SUMMARY bullet uses the inline
  evidence citation format: `CONFIRMED -- evidence: [source-phase]: [finding-name]`,
  not a plain `[CONFIRMED | RUNTIME ANOMALY]` token. This is the fourth checkpoint
  of C-29 made explicit as its own criterion. C-29 can be PARTIAL when field 6,
  VERDICT, and Q2 all carry the inline format but the EXECUTIVE SUMMARY bullets still
  use plain tokens -- V-03 (R10) demonstrated exactly this failure: template and VERDICT
  correct, Q2 scoped correctly, but no EXECUTIVE SUMMARY section meant the fourth
  checkpoint was structurally unreachable. C-31 enforces the fourth checkpoint
  independently of whether C-29 passes or is partial, and independently of C-28,
  because the EXECUTIVE SUMMARY bullet format is a distinct output location from field
  6 and VERDICT. A template that has C-28 (EXECUTIVE SUMMARY section present) but uses
  plain confirmation tokens in bullets fails C-31 regardless of C-29 status.
- **Pass condition:** Every EXECUTIVE SUMMARY bullet confirmation slot uses
  `CONFIRMED -- evidence: [source-phase]: [finding-name]` format (or equivalent
  structural embedding). Plain `[CONFIRMED | RUNTIME ANOMALY]` tokens in EXECUTIVE
  SUMMARY bullets = FAIL. EXECUTIVE SUMMARY absent = FAIL (cannot satisfy this
  criterion without the section that hosts the bullets).

---

### C-32 — VALIDITY RULES rejection gate at write time
- **Category:** rigor
- **Text:** A VALIDITY RULES section (or equivalent inline rejection block) is
  co-located with the EXECUTIVE SUMMARY write instruction and contains explicit
  prohibition language for the format violations addressed by C-30 and C-31. The gate
  must state what is INVALID, not merely what is correct -- correct-format examples
  without prohibition language constitute instructional register (V-03 pattern) and
  do not satisfy this criterion. The rejection gate fires at the point of production,
  before Q7 post-write audit, providing the first of three independent enforcement
  layers. V-04 (R11) demonstrated the minimum viable form: two numbered VALIDITY RULES
  -- rule 1 prohibiting free-form terminal names (C-30 domain), rule 2 prohibiting
  plain confirmation tokens (C-31 domain). V-05 (R11) demonstrated the same gate
  integrated with Q7 post-write audit and Q2 pre-write extension.
- **Pass condition:** A rejection block co-located with the EXECUTIVE SUMMARY template
  contains explicit INVALID / NOT valid language for both the terminus format (C-30)
  and the confirmation slot format (C-31). Correct-format examples without prohibition
  statements = FAIL. Prohibition present for one format but not the other = PARTIAL.
  EXECUTIVE SUMMARY absent = FAIL (gate has no production location).

---

### C-33 — Q7 post-write output-boundary gate
- **Category:** rigor
- **Text:** A dedicated calibration question (Q7 or equivalent named gate) fires after
  EXECUTIVE SUMMARY is written and before CONSOLIDATE is called. Q7 audits each bullet
  individually and produces a traceable per-bullet status statement (e.g., "bullet 1:
  T-NN terminus present -- PASS; citation format present -- PASS"). This makes C-30 and
  C-31 compliance visible in the artifact itself, not merely enforced by template
  instructions. Without a post-write gate, format drift is detectable only by manual
  re-read; Q7 closes the loop by generating an auditable compliance record. Q7 is the
  third enforcement layer in the V-05 architecture: VALIDITY RULES (C-32) rejects at
  write time, Q2 extension (C-34) previews compliance before writing, Q7 verifies
  after writing.
- **Pass condition:** A calibration question explicitly fires after EXECUTIVE SUMMARY
  is written and before CONSOLIDATE, audits each bullet for C-30 and C-31 compliance,
  and produces a per-bullet status statement. Q7 scope limited to other content (not
  EXECUTIVE SUMMARY bullets) = FAIL. Post-write audit present only in DEFINITIONS
  instructions without a named calibration question = FAIL. EXECUTIVE SUMMARY absent
  = FAIL.

---

### C-34 — Q2 extended to preview EXECUTIVE SUMMARY compliance
- **Category:** rigor
- **Text:** Q2 (or the equivalent pre-CONSOLIDATE calibration question) is extended
  beyond its baseline scope to preview EXECUTIVE SUMMARY bullet compliance before the
  section is written. The extension makes Q2 a forward reference: it flags T-NN
  terminus code gaps and inline evidence citation gaps at calibration time so they can
  be corrected before EXECUTIVE SUMMARY is drafted. Q7 (C-33) then verifies the fix
  after writing. The Q2-preview + Q7-verify pairing bridges calibration and output
  phases: Q2 identifies, Q7 confirms resolution. A Q2 that audits field 6 and VERDICT
  inline citation format (C-29 compliance) without explicitly previewing EXECUTIVE
  SUMMARY slot compliance does not satisfy this criterion -- the extension must be
  explicit and scoped to the summary section.
- **Pass condition:** Q2 explicitly previews EXECUTIVE SUMMARY bullet compliance
  (T-NN terminus codes and inline evidence citation format) before the section is
  written. Q2 scoped only to field 6 and VERDICT, with no EXECUTIVE SUMMARY preview
  = FAIL. Preview present but limited to one format dimension (terminus only or
  citation only) = PARTIAL. EXECUTIVE SUMMARY absent = FAIL.

---

### C-35 — Registry-lock declaration at Phase 0 close
- **Category:** correctness
- **Text:** Phase 0 closes with an explicit registry-lock statement declaring the
  terminus registry immutable before any phase executes. The lock must name the count
  of registered entries and assert that no terminus component may be added, removed,
  or renamed after this point. Without the lock, a model executing Phases 1-5 can
  silently introduce new terminus components -- chains that resolve to unlisted
  components pass chain-format checks without triggering a registry-miss flag, because
  there is no authority record to check against. The lock converts Phase 0 from a
  reference table into an authority contract: once locked, any chain whose terminus is
  not in the table is structurally invalid regardless of how it is formatted. C-27
  requires the registry to exist; C-35 requires the registry to be explicitly closed
  before execution begins.
- **Pass condition:** Phase 0 (or the REGISTRY section) includes a lock statement
  explicitly naming the entry count and prohibiting post-lock modification. A terminus
  table without a lock declaration = FAIL for C-35 (does not affect C-27 score). Lock
  statement present but not co-located with Phase 0 close (e.g., placed mid-phase or
  after Phase 1 begins) = PARTIAL. C-27 must be present for C-35 to be satisfiable.

---

### C-36 — Per-phase T-NN exit gate in EXIT CRITERIA
- **Category:** rigor
- **Text:** Each phase's EXIT CRITERIA includes a T-NN resolution check that fires at
  phase boundary -- before the next phase begins. The check counts chains produced in
  that phase, chains resolved to T-NN registry entries, and registry misses; it emits
  a traceable status statement (e.g., "[N] chains produced, [N] resolved to T-NN,
  [N] registry miss"). Any registry miss is flagged inline as "unresolved chain --
  registry miss: [component name]" and carried forward to Q1. This is the only
  enforcement layer that fires during execution at each phase boundary, as distinct
  from pre-execution (Phase 0 / C-35) and post-output (Q1 / Q8). Without per-phase
  gates, chain drift accumulates silently across all five phases and is caught only
  by Q1 post-hoc, after CONSOLIDATE and EXECUTIVE SUMMARY are already written. The
  per-phase gate catches drift at source: a miss in Phase 2 is flagged before Phase 3
  begins, allowing correction before the chain propagates downstream.
- **Pass condition:** EXIT CRITERIA in each of the five phases (Phases 1-5) includes
  a T-NN resolution check with chain count, resolved count, and registry miss count.
  Resolution check present in some but not all phases = PARTIAL (PASS if 4+ phases
  covered, PARTIAL if 2-3 phases covered, FAIL if 0-1 phases covered). EXIT CRITERIA
  present without T-NN resolution check = FAIL. C-27 must be present for C-36 to be
  satisfiable.

---

### C-37 — Q8 CONSOLIDATE completeness gate
- **Category:** rigor
- **Text:** A dedicated calibration question (Q8 or equivalent named gate) fires after
  CONSOLIDATE is written and before VERDICT is called. Q8 audits every finding block
  individually across three dimensions: (1) 7-field completeness -- all seven fields
  present and labeled; (2) T-NN chain resolution -- field 3 propagation chain resolves
  to a registered T-NN entry; (3) classification format -- field 6 confirmation slot
  uses the inline evidence citation format, not a bare CONFIRMED token. Q8 produces a
  per-block status statement (e.g., "Finding [N]: 7-field PASS, T-NN PASS
  (terminal: T-NN), classification PASS"). This is the post-write audit for CONSOLIDATE
  finding blocks, exactly analogous to Q7's role for EXECUTIVE SUMMARY bullets, with
  the addition of the 7-field completeness dimension (EXECUTIVE SUMMARY bullets have no
  equivalent of fields 1, 4, 5, and 7). The gap Q8 closes: Q1-Q6 validate inputs and
  calibration before CONSOLIDATE is written; Q8 is the only gate that fires after
  CONSOLIDATE is written. Without Q8, structurally deficient finding blocks (missing
  fields, free-form chains, bare CONFIRMED tokens) face no structural challenge before
  VERDICT. Q8 is the third enforcement layer in the CONSOLIDATE pipeline:
  C-35 (registry-lock at declaration time) + C-36 (per-phase exit gates during
  execution) + C-37 (Q8 post-write audit) mirrors the C-32/C-34/C-33 architecture
  for EXECUTIVE SUMMARY introduced in R11 V-05.
- **Pass condition:** A calibration question explicitly fires after CONSOLIDATE is
  written and before VERDICT, audits each finding block for all three dimensions
  (7-field completeness, T-NN chain resolution, classification format), and produces
  a per-block status statement. Q8 scope limited to two dimensions only = PARTIAL.
  Post-write audit present only in DEFINITIONS instructions without a named calibration
  question = FAIL. CONSOLIDATE absent or Q8 placed before CONSOLIDATE = FAIL.
  C-19 must be present for the 7-field check to be satisfiable; C-27 must be present
  for the T-NN check to be satisfiable.

---

### C-38 — Exception path sub-tables in all trace phases
- **Category:** coverage
- **Text:** Each trace phase (trace-state Ph1, trace-permissions Ph2, trace-contract
  Ph3) and flow-trigger (Ph5) includes an exception path sub-table evaluating failure
  modes beyond the happy path -- specifically state failure modes (Ph1), permission
  denial and escalation failure modes (Ph2), contract breach modes (Ph3), and trigger
  failure modes (Ph5). C-05 requires flow-lifecycle (Ph4) to include exception path
  evaluation; C-38 extends the same requirement to all remaining phases. Without
  exception sub-tables in trace phases, the campaign evaluates each phase's success
  path but leaves failure paths un-analyzed -- a model can construct a plausible blast
  radius from success-path behavior while missing violations that only manifest on
  exception paths. R13 V-02 demonstrated the minimum viable form: sub-tables in
  Phases 1, 2, 3, and 5, each covering at least three failure mode categories. V-02
  confirmed that exception sub-tables add coverage depth without degrading C-22 or
  C-23 performance on the condensed register axis.
- **Pass condition:** Phases 1, 2, 3, and 5 each include an exception path sub-table
  (or equivalent labeled evaluation) with at least two named failure mode categories
  per phase. Sub-table present in some but not all four phases = PARTIAL (PASS if all
  four phases covered, PARTIAL if 2-3 phases covered, FAIL if 0-1 phases covered).
  Exception path evaluation present only in flow-lifecycle (C-05 scope) = FAIL for
  C-38 (does not affect C-05 score).

---

### C-39 — I-NN pre-committed inertia inventory in Phase 0
- **Category:** rigor
- **Text:** A numbered I-NN inertia table is declared in Phase 0 (or a dedicated
  INERTIA section) before any phase executes, listing every assumption the campaign
  brings in about existing system behavior that will be treated as stable during
  execution. Q5 (or equivalent calibration question) then verifies I-NN items by
  forward reference -- checking whether declared inertia assumptions held -- rather than
  reconstructing assumptions post-hoc after findings have already been produced.
  The forward-verification pattern has two effects: (1) it converts Q5 from a
  backward-reconstruction question ("what did the campaign assume?") into a checklist
  comparison ("did assumption I-03 hold?"), enabling precise miss detection; (2) it
  surfaces meta-findings -- inertia items the team declared but cannot verify, which
  reveal gaps in the spec or in the model's knowledge of the system. Without a
  pre-committed inventory, Q5 can only reconstruct assumptions that surfaced during
  execution; it cannot detect assumptions that were silently held and never surfaced.
  R13 V-03 demonstrated the full pattern: I-NN table in Phase 0, Q5 structured as
  forward-verification, meta-finding section listing assumptions that surfaced during
  the campaign but were not in the original I-NN inventory.
- **Pass condition:** Phase 0 (or a dedicated INERTIA section before phase execution)
  includes a numbered I-NN table with at least two declared inertia assumptions. Q5
  (or equivalent) explicitly references I-NN entries by code in its verification pass,
  not just by prose description. Inertia assumptions discussed in Q5 prose without an
  antecedent I-NN table = FAIL. I-NN table present but Q5 does not reference I-NN
  codes = PARTIAL. C-18 must be present (n >= 3 calibration questions) for C-39 to
  be satisfiable.

---

### C-40 — Field 7 remediation-tier sub-structure with Q8 4th check
- **Category:** structure
- **Text:** Field 7 (recommendation / next action) of every finding block (F-NN and
  M-NN) is partitioned into three ownership tiers using the sub-field format
  `spec: [...] | contract: [...] | implementation: [...]`. Each tier names the fix
  layer responsible: spec tier for missing clauses or spec amendments, contract tier
  for producer/consumer agreement changes, implementation tier for code-level
  corrections. This makes fix-layer assignment mechanically auditable rather than
  prose-evaluated -- a reviewer can confirm that every tier is populated without
  re-reading free-form recommendation text. Q8 (C-37) gains a 4th structural check
  dimension: remediation-tier completeness -- it audits whether all three sub-fields
  are present and labeled in every finding block. R14 V-01 demonstrated the minimum
  viable form: all F-NN blocks carry `spec/contract/implementation` in field 7; Q8's
  4th check emits per-block tier status alongside the existing 7-field, T-NN, and
  classification checks.
- **Pass condition:** Every finding block (F-NN and M-NN where present) has Field 7
  using the `spec: [...] | contract: [...] | implementation: [...]` sub-structure
  with all three sub-fields labeled. Q8 explicitly audits remediation-tier completeness
  as a 4th check dimension alongside the three required by C-37. Field 7 present but
  unpartitioned (single prose block) = FAIL. Tier sub-structure in field 7 without Q8
  4th check = PARTIAL. C-19 must be present (7-field block) for Field 7 to exist;
  C-37 must be present (Q8) for the 4th check to be satisfiable.

---

### C-41 — M-NN meta-finding elevation into EXECUTIVE SUMMARY blast-radius pool
- **Category:** correctness
- **Text:** Meta-findings (M-NN) are elevated to first-class 7-field finding blocks
  and enter the EXECUTIVE SUMMARY blast-radius ranking pool alongside F-NN findings.
  An M-NN item whose blast radius warrants it can outrank a regular F-NN finding in
  the ranked list and in the EXECUTIVE SUMMARY top-3. VALIDITY RULES rule 2 is
  extended to explicitly cover the M-NN confirmation token format
  (`meta-finding: I-NN inventory miss` or equivalent) in addition to the F-NN inline
  evidence format (`CONFIRMED -- evidence: [...]`), preserving C-31 integrity for
  the new item class. Without M-NN elevation, assumption-gap findings are treated as
  prose annotations rather than ranked signals -- they cannot be compared to F-NN
  findings by blast radius and are invisible to Q8's structural audit. R14 V-02
  demonstrated the minimum viable form: M-NN blocks with 7 labeled fields, M-NN items
  ranked in EXECUTIVE SUMMARY, VALIDITY RULES covering both F-NN and M-NN token
  formats, Q8 auditing M-NN blocks across all required dimensions.
- **Pass condition:** M-NN blocks have 7 numbered, labeled fields consistent with the
  C-19 atomic block structure. M-NN items appear in EXECUTIVE SUMMARY ranked by blast
  radius alongside F-NN findings. VALIDITY RULES explicitly names the M-NN token
  format as a distinct valid class alongside F-NN inline evidence format. Q8 audits
  M-NN blocks in addition to F-NN blocks. M-NN items present only as prose annotations
  (not in 7-field block structure) = FAIL. M-NN blocks present but not in EXECUTIVE
  SUMMARY pool = PARTIAL. C-19 must be present (7-field block) and C-39 must be
  present (I-NN inventory that M-NN codes reference) for C-41 to be satisfiable.

---

### C-42 — H-NN hypothesis pre-declaration with QH outcome gate
- **Category:** rigor
- **Text:** Hypotheses about system behavior are pre-declared as a numbered H-NN table
  before any phase executes. A dedicated hypothesis audit gate (QH) fires after Q6
  and before the EXECUTIVE SUMMARY write site, assigning each H-NN a three-state
  outcome: CONFIRMED (evidence found), REFUTED (contradicting evidence found), or
  NO-EVIDENCE (campaign evaluated the hypothesis and found no supporting evidence).
  The three-state trichotomy is critical: NO-EVIDENCE is explicitly distinct from
  absence -- it records that the campaign actively looked and found nothing, rather than
  never evaluating the area. NO-EVIDENCE hypotheses become explicit follow-up signals
  rather than silent omissions, and are reported in CONSOLIDATE under a dedicated
  `Hypothesis outcomes` section and in VERDICT as `Hypotheses: [N] confirmed,
  [N] refuted, [N] no-evidence`. QH does not duplicate Q2 scope (Q2 checks
  classification citations; QH checks hypothesis outcomes) and does not collide with
  VALIDITY RULES (VALIDITY RULES fires at the EXECUTIVE SUMMARY write site, after QH).
  R14 V-03 demonstrated the full pattern: H-NN table in Phase 0, QH between Q6 and
  EXECUTIVE SUMMARY, three-state outcomes per H-NN, hypothesis outcomes section in
  CONSOLIDATE, H-NN/M-NN summary counts in VERDICT.
- **Pass condition:** An H-NN numbered table appears before phase execution begins
  with at least two declared hypotheses. QH fires explicitly after Q6 and before
  EXECUTIVE SUMMARY, assigning CONFIRMED/REFUTED/NO-EVIDENCE to each H-NN.
  CONSOLIDATE includes a `Hypothesis outcomes` section listing per-H-NN results.
  VERDICT reports hypothesis counts by outcome. H-NN table present but QH absent
  = FAIL. QH present but using binary outcome (CONFIRMED/REFUTED only, no NO-EVIDENCE
  state) = PARTIAL. QH present but firing after EXECUTIVE SUMMARY rather than before
  = FAIL. C-18 must be present (n >= 3 calibration questions; QH extends the count)
  and C-25 must be present (Q6 must exist as QH fires after it) for C-42 to be
  satisfiable.

---

### C-43 — QL concurrent-boundary gate with named source attribution class
- **Category:** rigor
- **Text:** A dedicated concurrent-boundary calibration gate (QL) fires after Q6 and
  before QH. QL forces cross-row concurrent reasoning over the Phase 4 combined
  nominal+exception table -- specifically re-entry collisions, recovery-path
  escalations, and cross-phase races that the table format does not prompt when rows
  are evaluated independently. QL-sourced findings enter CONSOLIDATE as F-NN blocks
  with a source tag naming the gate: `src: flow-lifecycle (QL)`. This source attribution
  class extends the fixed 5-phase source vocabulary (trace-state, trace-permissions,
  trace-contract, flow-lifecycle, flow-trigger) with a named calibration-gate-derived
  class. DEFINITIONS must explicitly declare `flow-lifecycle (QL)` as a valid source
  attribution value alongside the five phase names; otherwise QL-sourced findings are
  structurally ambiguous -- a reviewer cannot tell whether `src: flow-lifecycle (QL)`
  is a valid attribution or an artifact error. The gate is hypothesis-testable: if QL
  finds nothing, the Phase 4 table format is sufficient for the scenario; if QL
  surfaces findings, the gate is load-bearing. R15 V-01 demonstrated the minimum
  viable form: QL fires between Q6 and QH; QL ordering stated in DEFINITIONS
  (`Q6 -> QL -> QH -> EXEC SUMMARY`); QL-sourced findings tagged with the named class;
  DEFINITIONS declares the class. R15 V-04 and V-05 confirmed composability with the
  HIGH-RISK tier (C-44) and Q8 vocabulary extension (C-45) without interaction
  degradation.
- **Pass condition:** QL fires explicitly between Q6 and QH with cross-row concurrent
  reasoning scope stated. QL-sourced findings enter CONSOLIDATE with
  `src: flow-lifecycle (QL)` tag (or equivalent named calibration-gate class).
  DEFINITIONS declares the QL source attribution class as a valid value. QL present
  but firing after QH = FAIL (ordering violation). QL fires in correct position but
  source attribution class absent from DEFINITIONS = PARTIAL. QL absent entirely =
  FAIL. C-18 must be present (QL extends the calibration question count) and C-42
  must be present (QH must exist as QL fires before it) for C-43 to be satisfiable.

---

### C-44 — HIGH-RISK inertia tier in Q5 with VERDICT inertia-lead
- **Category:** rigor
- **Text:** Q5 gains a risk-triage step that classifies I-NN assumptions as HIGH-RISK
  when both conditions hold: (a) if wrong, the assumption implies wide blast radius,
  and (b) no spec clause governs the assumption's domain. HIGH-RISK assumptions are
  surfaced by Q5 alongside the standard forward-verification pass rather than treated
  as ordinary unverified inertia. VERDICT is restructured to open with an
  "Inertia averted" paragraph that names the top HIGH-RISK assumption before the
  top-finding paragraph. This reframing is structurally distinct from the existing
  I-NN inventory (C-39) and meta-finding elevation (C-41): the HIGH-RISK tier operates
  on declared inertia assumptions before they surface as M-NN findings, and changes
  the narrative opening of VERDICT rather than the blast-radius ranking of findings.
  The inertia-lead VERDICT answers "what would have shipped unchallenged" before
  answering "what we found" -- a distinct risk communication posture. R15 V-02
  demonstrated the minimum viable form: Q5 risk-triage block with both HIGH-RISK
  conditions stated; VERDICT opening paragraph names the top HIGH-RISK assumption
  by I-NN code; top-finding paragraph follows. R15 V-04 and V-05 confirmed
  composability with QL (C-43) without interaction degradation in VERDICT structure.
- **Pass condition:** Q5 includes an explicit risk-triage step classifying I-NN
  assumptions as HIGH-RISK with both conditions stated (wide-blast implication AND
  no spec clause). VERDICT opens with an inertia-averted paragraph naming at least
  one HIGH-RISK assumption by I-NN code before the top-finding paragraph. Q5
  risk-triage present but VERDICT inertia-lead absent = PARTIAL. VERDICT inertia-lead
  present but Q5 conditions unstated = PARTIAL. Both absent = FAIL. C-39 must be
  present (I-NN inventory must exist for Q5 to apply triage) for C-44 to be
  satisfiable.

---

### C-45 — Q8 source-field vocabulary extension for calibration-gate-derived attribution
- **Category:** structure
- **Text:** When QL is present (C-43), Q8's per-block completeness check explicitly
  declares `"flow-lifecycle (QL)"` as a valid source-field value in the source
  attribution check dimension. Without this extension, QL-sourced findings produce
  false negatives in Q8 -- the source field `src: flow-lifecycle (QL)` does not match
  any of the five canonical phase names, causing Q8 to flag the attribution as an
  unrecognized value or silently skip the check. The vocabulary extension makes Q8's
  completeness gate accurate for the extended source class introduced by C-43. The
  extension is a structural Q8 modification (DEFINITIONS or Q8 template updated with
  recognized values) rather than an ad-hoc exception -- it is generalized to any
  calibration-gate-derived source class, not hardcoded to QL only. R15 V-05
  demonstrated the minimum viable form: Q8 template explicitly declares
  `"flow-lifecycle (QL)"` as a valid `src:` value; Q8 source-field check accepts the
  extended vocabulary without flagging QL-sourced findings as attribution errors.
- **Pass condition:** Q8 template (or equivalent DEFINITIONS block governing Q8 scope)
  explicitly names `"flow-lifecycle (QL)"` (or the named calibration-gate source class
  from C-43) as a recognized valid value for the source attribution field check. Q8
  audits QL-sourced blocks without false-negative source-field failures. Q8 present
  but silent on the QL source class (may silently skip or flag QL blocks) = FAIL.
  Q8 extended but via ad-hoc exception comment rather than declared vocabulary = PARTIAL.
  C-43 must be present (QL gate must exist to produce QL-sourced findings) and C-37
  must be present (Q8 must exist) for C-45 to be satisfiable.

---

## Cross-criterion dependencies

| Criterion | Requires | Because |
|-----------|----------|---------|
| C-30 | C-27 and C-28 | Registry and EXECUTIVE SUMMARY must both exist for T-NN cross-link to be satisfiable |
| C-31 | C-28 | EXECUTIVE SUMMARY section must exist to host the bullets |
| C-32 | C-28; C-30 or C-31 | Gate has no production location without EXECUTIVE SUMMARY; gate has no subject without the format constraints it enforces |
| C-33 | C-28 | Q7 has no output section to audit without EXECUTIVE SUMMARY |
| C-34 | C-28 and C-18 | Q2 extension not possible without an existing Q2; EXECUTIVE SUMMARY must exist as forward reference target |
| C-35 | C-27 | Registry must exist before it can be locked |
| C-36 | C-27 | T-NN resolution check requires the registry to resolve against |
| C-37 | C-19 and C-27 | 7-field check requires atomic blocks; T-NN check requires the registry |
| C-39 | C-18 | Forward-verification Q5 requires an existing calibration question structure (n >= 3) |
| C-40 | C-19 and C-37 | Field 7 sub-structure requires the 7-field block to exist; Q8 4th check requires Q8 to exist |
| C-41 | C-19, C-28, C-32, and C-39 | 7-field M-NN blocks require atomic block structure; EXECUTIVE SUMMARY pool requires the section; VALIDITY RULES coverage requires the rejection gate; M-NN codes reference I-NN inventory |
| C-42 | C-18 and C-25 | QH extends the calibration question count; QH fires after Q6 so Q6 must exist |
| C-43 | C-18 and C-42 | QL extends the calibration question count; QL fires before QH so QH must exist |
| C-44 | C-39 | HIGH-RISK tier operates on the I-NN inventory; Q5 must exist to host the triage step |
| C-45 | C-43 and C-37 | Vocabulary extension has no subject without QL-sourced findings; Q8 must exist to receive the extension |

---

## Enforcement architecture

### EXECUTIVE SUMMARY pipeline (introduced R11 V-05, captured v10)

| Layer | Criterion | When it fires | What it catches |
|-------|-----------|---------------|-----------------|
| Pre-production gate | C-32 VALIDITY RULES | At EXECUTIVE SUMMARY write site | Incorrect format before it is produced |
| Production-time preview | C-34 Q2 extension | Before EXECUTIVE SUMMARY is written | T-NN and citation gaps at calibration time |
| Post-write gate | C-33 Q7 | After EXECUTIVE SUMMARY, before CONSOLIDATE | Format drift after production |

### CONSOLIDATE pipeline (introduced R12 V-05, captured v11)

| Layer | Criterion | When it fires | What it catches |
|-------|-----------|---------------|-----------------|
| Declaration-time lock | C-35 registry-lock | At Phase 0 close | Silent terminus additions before execution begins |
| Production-time gate | C-36 per-phase exit | At each phase boundary (Phases 1-5) | Chain drift at source before downstream propagation |
| Post-write gate | C-37 Q8 | After CONSOLIDATE, before VERDICT | 7-field gaps, free-form chains, bare tokens in finding blocks |

Both pipelines are independently operative. All six criteria passing together
constitutes the full dual-pipeline enforcement stack first demonstrated in R12 V-05.

### Phase coverage expansion (introduced R13 V-02/V-03, captured v12)

| Criterion | Scope | What it adds |
|-----------|-------|-------------|
| C-38 exception sub-tables | Phases 1, 2, 3, 5 | Exception path coverage in trace phases; extends C-05 beyond flow-lifecycle to all analytical phases |
| C-39 I-NN inertia inventory | Phase 0 + Q5 | Pre-committed assumption declaration; converts Q5 from backward-reconstruction to forward-verification |

C-38 and C-39 are independent of each other and of the dual-pipeline enforcement
stack. R13 V-05 confirmed all three axes (condensed register, exception expansion,
I-NN inventory) are composable without interaction degradation across any existing
criterion.

### Finding structure expansion (introduced R14 V-01/V-02/V-03, captured v13)

| Criterion | Scope | What it adds |
|-----------|-------|-------------|
| C-40 remediation-tier sub-structure | Field 7 + Q8 4th check | Fix-layer ownership partitioned into spec/contract/implementation; Q8 gains a 4th structural audit dimension |
| C-41 M-NN elevation | EXECUTIVE SUMMARY + VALIDITY RULES + Q8 | Undeclared assumption gaps become first-class ranked signals, not prose annotations |
| C-42 H-NN hypothesis pre-declaration | Phase 0 + QH gate | Pre-declared hypotheses get CONFIRMED/REFUTED/NO-EVIDENCE outcomes; NO-EVIDENCE is traceable, not silent |

C-40, C-41, and C-42 are independent of each other and of the dual-pipeline and
phase coverage axes. R14 V-05 confirmed full composability across all five axes
(dual-pipeline, phase coverage, remediation tiering, M-NN elevation, H-NN
pre-declaration) with no interaction degradation.

### Calibration gate expansion (introduced R15 V-01/V-02/V-05, captured v14)

| Criterion | Scope | What it adds |
|-----------|-------|-------------|
| C-43 QL concurrent-boundary gate | Phase 4 + calibration chain + CONSOLIDATE attribution | Named concurrent-boundary gate forces cross-row race analysis not prompted by table format; introduces calibration-gate-derived source attribution class |
| C-44 HIGH-RISK inertia tier + VERDICT inertia-lead | Q5 risk-triage + VERDICT opening | Risk-tiers I-NN assumptions by blast x spec-coverage; reframes VERDICT as inertia-averted before what-we-found |
| C-45 Q8 source-field vocabulary extension | Q8 source-field check | Extends Q8 recognized vocabulary to include QL-derived attribution class; prevents false negatives for calibration-gate-sourced findings |

C-43, C-44, and C-45 are largely independent: C-43 and C-44 share no structural
dependency and can be composed without C-45 (C-45 requires C-43 but not C-44).
R15 V-05 confirmed full composability across all six axes (dual-pipeline, phase
coverage, remediation tiering, M-NN elevation, H-NN pre-declaration, calibration
gate expansion) with no interaction degradation.

---

## Version History

| Version | Date       | Changes |
|---------|------------|---------|
| v1      | 2026-03-14 | Initial rubric (C-01-C-08, essential + recommended only) |
| v2      | 2026-03-14 | Added aspirational tier C-09-C-13 (denominator 5) |
| v3      | 2026-03-15 | Extended aspirational to C-09-C-16 (denominator 8) |
| v4      | 2026-03-15 | Extended aspirational to C-09-C-19 (denominator 11) |
| v5      | 2026-03-16 | Extended aspirational to C-09-C-21 (denominator 13) |
| v6      | 2026-03-17 | Added C-22 state-anchor order, C-23 permissions-anchor position (denominator 15) |
| v7      | 2026-03-17 | Added C-24 anchor tags, C-25 Q6 gate, C-26 propagation chain (denominator 18) |
| v8      | 2026-03-17 | Added C-27 terminus registry, C-28 dedicated exec summary, C-29 inline evidence citation (denominator 21) |
| v9      | 2026-03-17 | Added C-30 EXECUTIVE SUMMARY x T-NN cross-link, C-31 EXECUTIVE SUMMARY inline evidence citations (denominator 23) |
| v10     | 2026-03-17 | Added C-32 write-time rejection gate, C-33 Q7 post-write audit, C-34 Q2 pre-write preview (denominator 26) |
| v11     | 2026-03-17 | Added C-35 registry-lock, C-36 per-phase exit gates, C-37 Q8 CONSOLIDATE gate (denominator 29) |
| v12     | 2026-03-17 | Added C-38 exception sub-tables in all trace phases, C-39 I-NN inertia inventory (denominator 31) |
| v13     | 2026-03-17 | Added C-40 field 7 remediation-tier sub-structure, C-41 M-NN elevation, C-42 H-NN hypothesis pre-declaration (denominator 34) |
| v14     | 2026-03-17 | Added C-43 QL concurrent-boundary gate, C-44 HIGH-RISK inertia tier + VERDICT inertia-lead, C-45 Q8 source-field vocabulary extension (denominator 37) |

---

## What changed v13 -> v14

**Source:** R15 scorecard -- V-01 QL concurrent-boundary gate excellence signal;
V-02 HIGH-RISK inertia tier + VERDICT inertia-lead excellence signal; V-05 Q8
source-field vocabulary extension interaction signal; V-04/V-05 composability
confirmation

| Criterion | Source | Failure mode it addresses |
|-----------|--------|--------------------------|
| C-43 | R15 V-01 QL concurrent-boundary gate | Phase 4 combined nominal+exception table evaluates each lifecycle transition independently; cross-row concurrent failure modes (re-entry collisions, recovery-path escalations, cross-phase races) are not prompted and go undetected without an explicit concurrent-boundary gate; QL-sourced findings lack a named attribution class, making them structurally ambiguous in CONSOLIDATE |
| C-44 | R15 V-02 HIGH-RISK inertia tier + VERDICT inertia-lead | Q5 forward-verification treats all unverified I-NN assumptions as equivalent regardless of blast exposure; wide-blast, spec-uncovered assumptions that would have shipped unchallenged are not separated from routine inertia; VERDICT framed as what-we-found obscures the campaign's risk-prevention value |
| C-45 | R15 V-05 Q8 source-field vocabulary extension | When QL is present, Q8's source-field check has no declared valid value for `flow-lifecycle (QL)` -- QL-sourced findings produce false negatives (unrecognized attribution) or are silently skipped; the completeness gate is inaccurate for the extended source class introduced by C-43 |

**Denominator:** 34 -> 37. Scoring formula updated: `(passed/37) x 10`.

**Calibration gate expansion:** C-43 adds a new named calibration gate (QL) between
Q6 and QH that forces concurrent phase-boundary reasoning not prompted by the Phase 4
table structure. C-44 deepens Q5 from forward-verification into risk-tiered triage and
restructures VERDICT as an inertia-averted narrative opening. C-45 closes the Q8
accuracy gap introduced when C-43 extends the source attribution vocabulary beyond the
five canonical phase names.

**Cross-criterion dependencies introduced:**
- C-43 requires C-18 (QL extends calibration question count) and C-42 (QH must exist as QL fires before it)
- C-44 requires C-39 (HIGH-RISK tier operates on the I-NN inventory; Q5 must exist to host the triage step)
- C-45 requires C-43 (QL gate must exist to produce QL-sourced findings) and C-37 (Q8 must exist to receive the extension)

**R15 variations under v14:**

| Variation | C-43 | C-44 | C-45 | Aspirational | Asp score | Total |
|-----------|------|------|------|-------------|-----------|-------|
| V-01      | PASS | FAIL | FAIL | 35/37       | 9         | 89    |
| V-02      | FAIL | PASS | FAIL | 35/37       | 9         | 89    |
| V-03      | FAIL | FAIL | FAIL | 34/37       | 9         | 89    |
| V-04      | PASS | PASS | FAIL | 36/37       | 10        | 90    |
| V-05      | PASS | PASS | PASS | 37/37       | 10        | 90    |

35/37 = 9.46 -> rounds to 9, total 89. 36/37 = 9.73 -> rounds to 10, total 90.
V-01 and V-02 each achieve 35/37. V-03 achieves 34/37 = 9.19 -> rounds to 9, total 89.
V-04 achieves 36/37. V-05 is the only variation achieving the true perfect score of
37/37. The new ceiling requires all nineteen aspirational landmarks C-27 through C-45 --
the full dual-pipeline enforcement stack, phase coverage expansion, finding structure
expansion, and calibration gate expansion.
