Written to `simulations/quest/rubrics/campaign-behavior-rubric-v11-2026-03-17.md`.

---

## Summary of changes

**Three new aspirational criteria from R12 V-05 excellence signals:**

| Criterion | Pattern | Captures |
|-----------|---------|---------|
| C-35 | Registry-lock declaration at Phase 0 close | Explicit immutability contract on the terminus registry before any phase executes — C-27 requires the registry to exist; C-35 requires it to be locked |
| C-36 | Per-phase T-NN exit gate in EXIT CRITERIA | Fires at each phase boundary (Phases 1–5); counts chains produced/resolved/missed — the only enforcement layer that fires during execution, not pre- or post-output |
| C-37 | Q8 CONSOLIDATE completeness gate | Fires after CONSOLIDATE, before VERDICT; audits every finding block across three dimensions (7-field completeness, T-NN chain resolution, classification format) — analogous to Q7 for EXECUTIVE SUMMARY |

**Denominator:** 26 -> 29. Formula: `(passed/29) x 10`.

**Symmetric enforcement architecture (the key structural signal):**

| Layer | EXECUTIVE SUMMARY pipeline (v10) | CONSOLIDATE pipeline (v11) |
|-------|----------------------------------|---------------------------|
| Pre-production gate | C-32 VALIDITY RULES at write site | C-35 registry-lock at Phase 0 close |
| Production-time gate | C-34 Q2 pre-write preview | C-36 per-phase exit gates |
| Post-write gate | C-33 Q7 after EXECUTIVE SUMMARY | C-37 Q8 after CONSOLIDATE |

**R12 variations under v11:**

| Variation | C-35 | C-36 | C-37 | Aspirational | Total |
|-----------|------|------|------|-------------|-------|
| V-01 | FAIL | PASS | FAIL | 27/29 -> 9 | **89** |
| V-02 | PASS | FAIL | FAIL | 27/29 -> 9 | **89** |
| V-03 | FAIL | FAIL | PASS | 27/29 -> 9 | **89** |
| V-04 | PASS | PASS | FAIL | 28/29 -> 10 | **90** |
| V-05 | PASS | PASS | PASS | 29/29 -> 10 | **90** |

V-04 rounds to 90 (28/29 x 10 = 9.66). V-05 is the only variation achieving the true perfect score of 29/29. The new ceiling requires all eleven aspirational landmarks C-27 through C-37.
tected. A spec gap is a condition, state
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

## Aspirational Criteria (29 criteria, score = passed/29 x 10)

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

### C-18 — Q1–Qn calibration questions (n >= 3)
- **Category:** rigor
- **Text:** The campaign includes at least three named calibration questions (Q1–Qn)
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
  dependency chain. Anchor tags make the dependency scannable from headers alone —
  a reviewer can confirm anchor ordering without reading phase body text.
- **Pass condition:** Ph1 and Ph2 headers (or equivalent anchor-phase designations)
  include an `[ANCHOR:...]` tag or equivalent inline marker naming the anchor role.
  Anchor rationale present only in body text, with no scannable header marker = FAIL.

---

### C-25 — Q6 sequence integrity gate
- **Category:** rigor
- **Text:** A dedicated calibration question (Q6 or equivalent named gate) validates
  anchor ordering at runtime: it asks whether Ph1 ran before Ph2, Ph2 ran before
  Ph3–Ph5, and whether the ordering produced the intended pre-classification benefits.
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
  registry, or be flagged "unresolved chain — registry miss: [component name]." Chains
  that miss the registry are excluded from ranking. This converts terminus validation
  from a DEFINITIONS prose audit — where a reviewer must re-read definitional text
  and match free-form component names — to a table lookup against canonical entries.
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
  position-independent — a reader does not need to locate the ranked list and verify
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
  without the inline citation fails the block format — the citation is not a
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
  registry absent from V-02's design — bullets used free-form names that could diverge
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
  use plain tokens — V-03 (R10) demonstrated exactly this failure: template and VERDICT
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
  must state what is INVALID, not merely what is correct — correct-format examples
  without prohibition language constitute instructional register (V-03 pattern) and
  do not satisfy this criterion. The rejection gate fires at the point of production,
  before Q7 post-write audit, providing the first of three independent enforcement
  layers. V-04 (R11) demonstrated the minimum viable form: two numbered VALIDITY RULES
  — rule 1 prohibiting free-form terminal names (C-30 domain), rule 2 prohibiting
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
  T-NN terminus present — PASS; citation format present — PASS"). This makes C-30 and
  C-31 compliance visible in the artifact itself, not merely enforced by template
  instructions. Without a post-write gate, format drift is detectable only by manual
  re-read; Q7 closes the loop by generating an auditable compliance record. Q7 is the
  third enforcement layer in the V-05 architecture: VALIDITY RULES (C-32) rejects at
  write time, Q2 extension (C-34) previews compliance before writing, Q7 verifies
  after writing.
- **Pass condition:** A calibration question explicitly fires after EXECUTIVE SUMMARY
  is written and before CONSOLIDATE, audits each bullet for C-30 and C-31 compliance,
  and produces a per-bullet status statement in the output. Q7 scope limited to other
  content (not EXECUTIVE SUMMARY bullets) = FAIL. Post-write audit present only in
  DEFINITIONS instructions without a named calibration question = FAIL. EXECUTIVE
  SUMMARY absent = FAIL.

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
  SUMMARY slot compliance does not satisfy this criterion — the extension must be
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
  or renamed after this point. Without the lock, a model executing Phases 1–5 can
  silently introduce new terminus components — chains that resolve to unlisted
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
  phase boundary — before the next phase begins. The check counts chains produced in
  that phase, chains resolved to T-NN registry entries, and registry misses; it emits
  a traceable status statement (e.g., "[N] chains produced, [N] resolved to T-NN,
  [N] registry miss"). Any registry miss is flagged inline as "unresolved chain —
  registry miss: [component name]" and carried forward to Q1. This is the only
  enforcement layer that fires during execution at each phase boundary, as distinct
  from pre-execution (Phase 0 / C-35) and post-output (Q1 / Q8). Without per-phase
  gates, chain drift accumulates silently across all five phases and is caught only
  by Q1 post-hoc, after CONSOLIDATE and EXECUTIVE SUMMARY are already written. The
  per-phase gate catches drift at source: a miss in Phase 2 is flagged before Phase 3
  begins, allowing correction before the chain propagates downstream.
- **Pass condition:** EXIT CRITERIA in each of the five phases (Phases 1–5) includes
  a T-NN resolution check with chain count, resolved count, and registry miss count.
  Resolution check present in some but not all phases = PARTIAL (PASS if 4+ phases
  covered, PARTIAL if 2–3 phases covered, FAIL if 0–1 phases covered). EXIT CRITERIA
  present without T-NN resolution check = FAIL. C-27 must be present for C-36 to be
  satisfiable.

---

### C-37 — Q8 CONSOLIDATE completeness gate
- **Category:** rigor
- **Text:** A dedicated calibration question (Q8 or equivalent named gate) fires after
  CONSOLIDATE is written and before VERDICT is called. Q8 audits every finding block
  individually across three dimensions: (1) 7-field completeness — all seven fields
  present and labeled; (2) T-NN chain resolution — field 3 propagation chain resolves
  to a registered T-NN entry; (3) classification format — field 6 confirmation slot
  uses the inline evidence citation format, not a bare CONFIRMED token. Q8 produces a
  per-block status statement (e.g., "Finding [N]: 7-field PASS, T-NN PASS
  (terminal: T-NN), classification PASS"). This is the post-write audit for CONSOLIDATE
  finding blocks, exactly analogous to Q7's role for EXECUTIVE SUMMARY bullets, with
  the addition of the 7-field completeness dimension (EXECUTIVE SUMMARY bullets have no
  equivalent of fields 1, 4, 5, and 7). The gap Q8 closes: Q1–Q6 validate inputs and
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
| Production-time gate | C-36 per-phase exit | At each phase boundary (Phases 1–5) | Chain drift at source before downstream propagation |
| Post-write gate | C-37 Q8 | After CONSOLIDATE, before VERDICT | 7-field gaps, free-form chains, bare tokens in finding blocks |

Both pipelines are independently operative. All six criteria passing together
constitutes the full dual-pipeline enforcement stack first demonstrated in R12 V-05.

---

## Version History

| Version | Date       | Changes |
|---------|------------|---------|
| v1      | 2026-03-14 | Initial rubric (C-01–C-08, essential + recommended only) |
| v2      | 2026-03-14 | Added aspirational tier C-09–C-13 (denominator 5) |
| v3      | 2026-03-15 | Extended aspirational to C-09–C-16 (denominator 8) |
| v4      | 2026-03-15 | Extended aspirational to C-09–C-19 (denominator 11) |
| v5      | 2026-03-16 | Extended aspirational to C-09–C-21 (denominator 13) |
| v6      | 2026-03-17 | Added C-22 state-anchor order, C-23 permissions-anchor position (denominator 15) |
| v7      | 2026-03-17 | Added C-24 anchor tags, C-25 Q6 gate, C-26 propagation chain (denominator 18) |
| v8      | 2026-03-17 | Added C-27 terminus registry, C-28 dedicated exec summary, C-29 inline evidence citation (denominator 21) |
| v9      | 2026-03-17 | Added C-30 EXECUTIVE SUMMARY x T-NN cross-link, C-31 EXECUTIVE SUMMARY inline evidence citations (denominator 23) |
| v10     | 2026-03-17 | Added C-32 write-time rejection gate, C-33 Q7 post-write audit, C-34 Q2 pre-write preview (denominator 26) |
| v11     | 2026-03-17 | Added C-35 registry-lock, C-36 per-phase exit gates, C-37 Q8 CONSOLIDATE gate (denominator 29) |

---

## What changed v10 -> v11

**Source:** R12 scorecard — V-05 excellence signals; V-01/V-02/V-03 as single-layer
baselines; V-04 as two-layer baseline

| Criterion | Source | Failure mode it addresses |
|-----------|--------|--------------------------|
| C-35 | R12 V-02/V-04/V-05 registry-lock | Terminus registry exists (C-27) but models can silently introduce new terminus components during Phases 1–5; the lock converts Phase 0 from a reference table into an authority contract — post-lock chain additions are structurally invalid without an explicit declaration |
| C-36 | R12 V-01/V-04/V-05 per-phase EXIT CRITERIA | Chain drift accumulates silently across all five phases and is caught by Q1 post-hoc only, after CONSOLIDATE and EXECUTIVE SUMMARY are written; per-phase gates catch drift at source before it propagates downstream, producing a traceable status at each phase boundary |
| C-37 | R12 V-03/V-04/V-05 Q8 post-CONSOLIDATE gate | Q1–Q6 validate inputs and calibration before CONSOLIDATE is written but no gate fires after; structurally deficient finding blocks (missing fields, free-form chains, bare CONFIRMED tokens) face no structural challenge before VERDICT; Q8 closes this gap with a three-dimension per-block audit analogous to Q7's role for EXECUTIVE SUMMARY |

**Denominator:** 26 -> 29. Scoring formula updated: `(passed/29) x 10`.

**Symmetric architecture:** C-35/C-36/C-37 complete the CONSOLIDATE pipeline
enforcement stack, mirroring C-32/C-34/C-33 for the EXECUTIVE SUMMARY pipeline.
Both three-layer stacks address the same failure modes (format drift, terminus
mismatch, structural incompleteness) in their respective output sections.

**Cross-criterion dependencies introduced:**
- C-35 requires C-27; no registry = nothing to lock
- C-36 requires C-27; no registry = T-NN resolution check has no authority source
- C-37 requires C-19 and C-27; no 7-field blocks = 7-field check is vacuous; no
  registry = T-NN chain check is unsatisfiable
- The three criteria are independent enforcement layers: each can pass or fail without
  requiring the others

**R12 variations under v11:**

| Variation | C-35 | C-36 | C-37 | Aspirational | Asp score | Total |
|-----------|------|------|------|-------------|-----------|-------|
| V-01      | FAIL | PASS | FAIL | 27/29       | 9         | 89    |
| V-02      | PASS | FAIL | FAIL | 27/29       | 9         | 89    |
| V-03      | FAIL | FAIL | PASS | 27/29       | 9         | 89    |
| V-04      | PASS | PASS | FAIL | 28/29       | 10        | 90    |
| V-05      | PASS | PASS | PASS | 29/29       | 10        | 90    |

V-04 reaches 90 by rounding (28/29 x 10 = 9.66 -> 10). V-05 is the only variation
achieving the true perfect score of 29/29. The new ceiling requires all eleven
aspirational landmarks C-27 through C-37 — the full dual-pipeline enforcement stack.
