Written to `simulations/quest/rubrics/campaign-behavior-rubric-v10-2026-03-17.md`.

---

## Summary of changes

**Three new aspirational criteria from R11 V-05 excellence signals:**

| Criterion | Pattern | Captures |
|-----------|---------|---------|
| C-32 | VALIDITY RULES rejection gate at write time | Co-located INVALID prohibition language in the EXECUTIVE SUMMARY template — instructional register (V-03) does not satisfy; explicit "is INVALID / NOT valid" language required |
| C-33 | Q7 post-write output-boundary gate | Fires after EXECUTIVE SUMMARY, before CONSOLIDATE; produces per-bullet traceable status statement — makes compliance visible in the artifact, not just instructed by template |
| C-34 | Q2 extended to preview EXECUTIVE SUMMARY compliance | Q2 forward-references the unwritten summary, flagging T-NN and citation gaps before production; Q7 verifies the fix — bridges calibration and output phases |

**Denominator:** 23 -> 26. Formula: `(passed/26) x 10`.

**V-04 retrogrades from 90 to 89** under v10 — its VALIDITY RULES section gets C-32 PARTIAL (covers both dimensions but Q7 and Q2-extension absent). V-05 is the sole variation at 90. The new ceiling requires all eight: C-27 through C-34.
nominator:** 23 -> 26. Formula: `(passed/26) x 10`.

**Cross-criterion dependencies:**
- C-32 requires C-28 (no EXECUTIVE SUMMARY = no write-time gate location); either C-30 or C-31 must also be present (the gate has no subject without the format constraints it enforces)
- C-33 requires C-28; no EXECUTIVE SUMMARY section = Q7 has no output to audit
- C-34 requires C-28 and C-18 (n >= 3 calibration questions); Q2 extension is not possible without an existing Q2

**Three-layer enforcement architecture (V-05):** C-32 (VALIDITY RULES at write time) + C-34 (Q2 pre-audit flag) + C-33 (Q7 post-write gate) are independent fallbacks — any single failure leaves two layers still operative. All three passing simultaneously constitutes the full enforcement stack demonstrated in V-05.

**R11 variations under v10:**

| Variation | C-32 | C-33 | C-34 | Aspirational | Total |
|-----------|------|------|------|-------------|-------|
| V-03 | FAIL | FAIL | FAIL | 21/26 -> 8 | **88** |
| V-01 | FAIL | FAIL | FAIL | 22/26 -> 8 | **88** |
| V-02 | FAIL | FAIL | FAIL | 22/26 -> 8 | **88** |
| V-04 | PARTIAL | FAIL | FAIL | 23/26 -> 9 | **89** |
| V-05 | PASS | PASS | PASS | 26/26 -> 10 | **90** |

V-05 is the only R11 variation that achieves the new ceiling under v10. V-04 drops from 90 to 89 because its VALIDITY RULES section passes C-32 only partially (covers one format dimension), and Q7 + Q2 extension are absent. The 90/90 ceiling now requires all eight: C-27 registry + C-28 EXECUTIVE SUMMARY + C-29 inline evidence + C-30 T-NN in summary chains + C-31 inline evidence in summary bullets + C-32 write-time rejection gate + C-33 Q7 post-write audit + C-34 Q2 pre-write preview.

---

## Scoring

| Tier | Criteria | Points |
|------|----------|--------|
| Essential    | C-01–C-05 (10 pts each)           | 50     |
| Recommended  | C-06–C-08 (10 pts each)           | 30     |
| Aspirational | C-09–C-34 — (passed/26) x 10     | 10     |
| **Total**    |                                   | **90** |

PASS = full credit. PARTIAL = half credit. FAIL = 0.
Aspirational tier is binary PASS/FAIL per criterion; score = (count passed / 26) x 10,
rounded to nearest integer.

---

## Essential Criteria (50 pts total)

### C-01 — All 5 sub-skills executed
- **Weight:** essential
- **Category:** coverage
- **Text:** The campaign runs all five sub-skills: trace-contract, trace-state,
  trace-permissions, flow-lifecycle, and flow-trigger. Partial execution invalidates
  blast radius ranking because findings from skipped sub-skills are absent.
- **Pass condition:** All five sub-skills are named in the output with evidence of
  execution (findings, tables, or explicit "none found" statements). Fewer than five
  named = FAIL.

---

### C-02 — Findings ranked by blast radius
- **Weight:** essential
- **Category:** correctness
- **Text:** The consolidated report presents findings ordered by blast radius
  (highest impact / widest system effect first). Blast radius is not interchangeable
  with severity or priority — it specifically captures how broadly a failure propagates
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

## Aspirational Criteria (26 criteria, score = passed/26 x 10)

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

---

## What changed v9 -> v10

**Source:** R11 scorecard — V-05 excellence signals; V-04 as minimum viable baseline

| Criterion | Source | Failure mode it addresses |
|-----------|--------|--------------------------|
| C-32 | V-04/V-05 VALIDITY RULES section | C-30/C-31 violations reach the output because templates show correct format without prohibiting incorrect format — co-located INVALID rejection language at the write site closes the production-time gap that Q7 alone cannot close retroactively |
| C-33 | V-05 Q7 dedicated post-write gate | Compliance is instructed (template) and pre-audited (Q2) but never verified in the artifact — Q7 fires after EXECUTIVE SUMMARY and before CONSOLIDATE, producing a traceable per-bullet record that converts implicit enforcement into explicit output evidence |
| C-34 | V-05 Q2 extended to summary preview | Q2 calibration reaches field 6 and VERDICT but not the unwritten EXECUTIVE SUMMARY — extending Q2 to preview summary slot compliance before writing creates a forward-reference checkpoint that Q7 then closes; without C-34, C-33 catches violations that C-34 would have prevented |

**Denominator:** 23 -> 26. Scoring formula updated: `(passed/26) x 10`.

**Cross-criterion dependencies introduced:**
- C-32 requires C-28; no EXECUTIVE SUMMARY = no production location for the write-time gate
- C-33 requires C-28; no EXECUTIVE SUMMARY = Q7 has no output section to audit
- C-34 requires C-28 and C-18 (Q2 must exist before it can be extended)
- The three criteria are designed as independent fallbacks: each can pass or fail without
  requiring the others; a template with only C-33 (Q7 alone) still passes C-33 even if
  C-32 and C-34 fail

**Three-layer enforcement stack (V-05 pattern):**
All three passing together constitutes the full enforcement architecture — C-32 rejects
at write time, C-34 previews before writing, C-33 verifies after writing. Each layer
catches failures the others miss: C-32 catches incorrect format before it is produced,
C-34 surfaces gaps before production even begins, C-33 confirms the produced output is
correct. No prior variation achieved all three.

**Scores the R11 variations achieve under v10:**

| Variation | C-32    | C-33 | C-34 | Aspirational | Asp score | Total |
|-----------|---------|------|------|-------------|-----------|-------|
| V-03      | FAIL    | FAIL | FAIL | 21/26       | 8         | 88    |
| V-01      | FAIL    | FAIL | FAIL | 22/26       | 8         | 88    |
| V-02      | FAIL    | FAIL | FAIL | 22/26       | 8         | 88    |
| V-04      | PARTIAL | FAIL | FAIL | 23/26       | 9         | 89    |
| V-05      | PASS    | PASS | PASS | 26/26       | 10        | 90    |

V-04 drops from 90 (v9) to 89 (v10): its VALIDITY RULES section satisfies C-32 only
partially (covers both format dimensions but Q7 and Q2-extension are absent). V-05
remains at 90 and is the sole variation achieving the new ceiling. The perfect score
now requires all eight aspirational landmarks: C-27 through C-34.
