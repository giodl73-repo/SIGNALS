Written to `simulations/quest/rubrics/corps-scan-rubric-v6-2026-03-16.md`.

---

**Four new criteria extracted from R5 excellence signals:**

**C-25 -- Universal output section self-labeling** (behavior)
From V-02. C-22 requires at least one pre-YAML section to self-label. V-02 extends this universally: every structural section -- pre-YAML, YAML-adjacent, and post-YAML -- carries a C-NN self-label. The labeling is applied as a structural rule with no unlabeled exceptions. Distinct from C-22 (one pre-YAML section) and C-19 (post-write section only).

**C-26 -- Multi-criterion section header** (behavior)
From V-02. A section header cites 2+ distinct C-NN criterion IDs simultaneously -- e.g., `"C-22: C-08 + C-16 satisfier"`. The section is architecturally designed to satisfy multiple criteria at once and declares them all at point of execution. Distinct from C-22 (one criterion per header).

**C-27 -- Pivot deliberation tri-part candidate assessment** (behavior)
From V-01. Each candidate pivot mode in the C-23 deliberation carries a formal three-part structure: Evidence For / Evidence Against / Assessment. All candidates follow the same triad. Distinct from C-23 (enumeration with any per-candidate assessment) -- requires the auditable tri-part form, not a single-verdict summary.

**C-28 -- Forward-committed pre-check items carry explicit execution-state marker** (behavior)
From V-01. Pre-check items whose satisfying content has not yet been written carry an explicit execution-state label (e.g., `"SCHEDULED"`) distinguishing them from already-satisfied items. Distinct from C-17 (forward commitment present) -- requires each deferred item to be annotated with its execution state on the item itself.

**Scoring change**: 170 → 190 pts (20 aspirationals × 5 pts). Golden threshold stays at 80 pts.

**R5 projected under v6**: V-01 180 (C-27 + C-28), V-02 180 (C-25 + C-26), V-03 170 -- breaks the R5 three-way tie at 170, with V-01 and V-02 tied at 180 via distinct technique clusters.
 be pre-populated in the scan output.

**C-05 -- Does not write .craft/roles/**
- Weight: essential
- Category: behavior
- Pass condition: The output does not write, create, or present the content of any
  `.craft/roles/` file. corp-scan is a draft-only skill whose sole output is org.yaml. The
  output must not purport to create role files, and does NOT include role file content. The
  boundary between corp-scan (draft) and corp-build (build) must be respected. Any output that
  writes role files or presents role file markdown fails.

---

## RECOMMENDED

Recommended criteria carry 10 pts each. A minimum-passing output (golden threshold) typically
satisfies 2 of 3 recommended criteria alongside all 5 essentials.

---

**C-06 -- Pivot mode declared with rationale**
- Weight: recommended
- Category: format
- Pass condition: Output names the pivot mode used (directory / concept / service / domain) and
  provides at least one sentence explaining why that mode was selected based on repo signals
  (e.g., "using directory mode: repo has clear top-level service directories under /src").
  Declaring a mode without rationale is partial credit -- does not pass.

**C-07 -- Exec office placeholder present**
- Weight: recommended
- Category: coverage
- Pass condition: org.yaml contains an exec-office section (even a minimal placeholder with a
  name and no teams). Absence of exec office means the output cannot feed corp-rob exec-office
  stage without manual addition.

**C-08 -- Amend options listed**
- Weight: recommended
- Category: behavior
- Pass condition: Output concludes with at least 2 named amend options drawn from the documented
  AMEND set: (a) change pivot mode, (b) rename exec office, (c) adjust group structure. Options
  must be actionable (e.g., "AMEND: switch to service mode -- run /corps-scan --pivot service").
  A generic "let me know if you want changes" does not pass.

---

## ASPIRATIONAL

Aspirational criteria carry 5 pts each. They are not required for golden status but distinguish
strong outputs from excellent ones. 20 criteria x 5 pts = 100 pts available.

---

**C-09 -- Detection rationale per area**
- Weight: aspirational
- Category: depth
- Pass condition: At least half of the detected team areas include an inline comment or
  annotation explaining the repo evidence that produced them (e.g., "# detected from
  /services/payments/, 3 service directories"). This makes the draft reviewable without
  re-reading the repo.

**C-10 -- Inertia Advocate noted**
- Weight: aspirational
- Category: depth
- Pass condition: Output notes -- at least once, in prose or as a YAML comment -- that Inertia
  Advocate will be auto-included per team when corp-build runs. This primes the user to expect
  the Inertia Advocate in the role files without configuring it manually.

**C-11 -- Pre-YAML scan inventory listed**
- Weight: aspirational
- Category: depth
- Pass condition: Before the YAML block, the output lists the repo signals it detected as a
  readable inventory of directory names, service paths, module identifiers, or domain terms.
  The inventory must be distinct from the YAML (not just the YAML itself) and must appear
  before the YAML block begins. This makes C-02 grounding verifiable by the reviewer without
  re-reading the repo.
- R1 signal: V-01 (inline annotations only, no pre-YAML inventory) received C-02 PARTIAL
  because "detection may be shallow." V-03 (explicit SCAN phase) and V-04 (Repo Archaeologist
  stage) both passed C-02 fully because the inventory step was structurally enforced before
  YAML production began.

**C-12 -- Draft boundary front-loaded before first output**
- Weight: aspirational
- Category: behavior
- Pass condition: The draft-only framing -- that this output is a proposal for human review, not
  a build instruction -- is stated explicitly before any YAML or structural content appears. A
  single sentence like "This is a draft org.yaml for review -- no role files will be created"
  appearing as the first substantive line passes. Burying the boundary acknowledgment after the
  YAML, or only at the end, does not pass.
- R1 signal: V-03 showed "DRAFT GATE states the draft-only constraint as an entry condition --
  cannot enter DRAFT without acknowledging boundary." This is a stronger compliance pattern than
  C-05 (which tests whether role files were written) -- it tests whether the reviewer is primed
  to read the YAML as a draft before they encounter it.

**C-13 -- Self-referential compliance check**
- Weight: aspirational
- Category: behavior
- Pass condition: The draft-only constraint (or a key C-05 / C-12 requirement) appears as an
  item in a checklist that explicitly confirms itself in the output -- e.g., "The draft-only
  statement appears before any YAML in this response. STATUS: CONFIRMED." The model cannot
  satisfy the checklist item without having already satisfied the criterion it names. A
  checklist that simply lists the requirement without confirming it in-response does not pass;
  the confirmation must be present in the output, not implied.
- R2 signal: V-04's PRE-CHECK item 3 demonstrated the pattern -- C-12 was embedded in a
  required checklist as a self-confirming item. The constraint becomes structurally
  self-enforcing rather than declarative.

**C-14 -- Dual-stage YAML bracketing**
- Weight: aspirational
- Category: behavior
- Pass condition: The output contains explicit constraint verification both BEFORE the YAML
  block (e.g., a pre-check or compliance confirmation section) AND AFTER the YAML block
  (e.g., a post-write checklist or verification note). Both gates must be present; a pre-check
  without a post-write note, or a post-write note without a pre-check, is PARTIAL.
- R2 signal: V-04 is the only R2 variation that brackets the YAML on both sides. No other
  variation detected a post-write failure mode after producing the artifact. The dual bracket
  makes constraint violations detectable mid-output rather than only at the end.

**C-15 -- Rubric criteria embedded as skill requirements**
- Weight: aspirational
- Category: depth
- Pass condition: The skill's own pre-check, instruction list, or checklist explicitly names at
  least 3 of the rubric criteria (by their behavior, if not by ID) as the skill's own
  requirements -- e.g., "I will produce a repo signal inventory before the YAML," "I will not
  write .craft/roles/ files," "2+ named roles per team area." This makes the scoring criteria
  transparent and enforceable in the output itself rather than implicit in the rubric document.
  A skill that lists general instructions without criterion-level specificity does not pass.
- R2 signal: V-04's PRE-CHECK items correspond 1:1 with C-04, C-05, C-07, C-11, and C-12.
  The connection between rubric design and skill execution became explicit in the output.

**C-16 -- Debt-framed amend options**
- Weight: aspirational
- Category: depth
- Pass condition: At least 2 of the listed amend options (C-08) name the downstream
  organizational or pipeline debt that accumulates if the option is skipped -- e.g., "Debt if
  skipped: exec-office stage cannot run without this section" or "Skipping this leaves role
  boundary unclear for corp-build." Naming the debt converts amend options from navigation aids
  into decision-support tools. Options that name the alternative without naming the consequence
  do not pass.
- R2 signal: V-05 introduced "Debt if skipped" notation for each AMEND option -- the strongest
  amend form in R2. No other variation named downstream consequences; all others listed options
  with commands but no organizational stakes.

**C-17 -- Forward commitment to future-section criteria**
- Weight: aspirational
- Category: behavior
- Pass condition: The pre-check or declaration section contains at least one item that names a
  criterion whose satisfying content has not yet been written -- e.g., C-16 appears as a
  pre-check item before the amend section is produced. The model pre-commits to compliance
  before executing the relevant section. A post-hoc checklist that only confirms criteria
  whose content already appeared above it is C-14, not C-17. At least one forward-committed
  item must be identifiable (the satisfying section must follow the pre-check, not precede it).
- R3 signal: V-04's pre-check listed C-16 as a required item before the amend section was
  written. This is the only R3 variation to pre-commit to a future-section criterion at
  declaration time rather than verify it retrospectively.

**C-18 -- Criterion ID as primary compliance key**
- Weight: aspirational
- Category: depth
- Pass condition: The compliance structure (pre-check, requirements list, or checklist) uses
  rubric criterion IDs (C-NN) as the primary header or key for at least 5 items -- e.g.,
  "[ ] C-12 -- draft boundary front-loaded", "[ ] C-16 -- debt-framed amend options." Using
  criterion IDs as keys makes the rubric-to-output mapping explicit and auditable without
  consulting the rubric document. Describing the criterion in prose without citing the ID does
  not pass; the C-NN label must be present as the item's primary identifier.
- R3 signal: V-04's checklist used criterion IDs as primary keys throughout, enabling a scorer
  to map each item to the rubric without the rubric present. No other R3 variation adopted
  ID-keyed compliance headers.

**C-19 -- Post-write criterion self-labeling**
- Weight: aspirational
- Category: behavior
- Pass condition: At least one post-write verification block cites the rubric criterion ID it
  is satisfying -- e.g., "C-14 dual-bracket: pre-check at line 3 and post-write here -- both
  present." The artifact names the criterion it satisfies by C-NN ID, not just by description.
  Distinct from C-15 (embedding criteria as requirements before the fact) and C-14 (dual-stage
  bracketing structure) -- C-19 requires the post-write section to self-identify by criterion
  ID at the point of satisfaction. No external rubric reference should be needed to confirm
  which criterion the block is fulfilling.
- R3 signal: V-04's post-write block stated "C-14 dual-bracket: ...Both present." The artifact
  named the criterion it satisfied rather than leaving the mapping implicit for the scorer.

**C-20 -- Structural role ordering as mechanical enforcement**
- Weight: aspirational
- Category: behavior
- Pass condition: The skill assigns sole ownership of the compliance pre-check (or equivalent
  constraint gate) to a named role that must complete before any scan, inventory, or YAML work
  begins. The role ordering is defined such that a model following the sequence structurally
  cannot begin repo analysis or YAML production until the compliance role finishes. Instruction-
  level reminders ("before writing YAML, check...") do not pass; the compliance work must be
  owned by a distinct named role whose completion precedes the assignment of any analytical or
  generative work to other roles.
- R3 signal: V-01's role sequence assigned the Compliance Officer role first, with scan and
  YAML work assigned only to roles that follow. The sequence makes it structurally impossible
  to bypass the compliance gate without violating the role ordering itself.

**C-21 -- Schema-typed inventory with criterion-labeled columns**
- Weight: aspirational
- Category: depth
- Pass condition: The pre-YAML inventory (C-11) is structured as a typed schema or table whose
  column headers include at least 2 C-NN criterion IDs -- e.g., "YAML name (C-02)", "Proposed
  roles (C-04)", "Detection evidence (C-09)." Each column enforces a rubric criterion at the
  schema level, making the inventory simultaneously serve as a compliance instrument. A generic
  table without C-NN-labeled columns (e.g., columns named "Team", "Roles", "Evidence" without
  criterion IDs) does not pass; the C-NN label must be present as part of the column header.
- R4 signal: V-02's Signal Schema used C-NN-labeled columns throughout, requiring every schema
  row to satisfy multiple rubric criteria by column. The schema enforced criterion-level
  compliance at the data-entry stage, before YAML production began. No other R4 variation
  applied C-NN labeling to inventory column structure.

**C-22 -- Pre-write section criterion self-labeling**
- Weight: aspirational
- Category: behavior
- Pass condition: At least one pre-YAML section announces which rubric criterion it satisfies
  in its own header or opening line -- e.g., "C-11 satisfier -- precedes YAML block" or
  "Signal Schema (satisfies C-11, C-02, C-09)." The section declares its criterion-level
  purpose before executing it. Distinct from C-19 (post-write labeling after the YAML) and
  C-15 (listing criteria as requirements in a compliance checklist) -- C-22 requires a
  structural section to self-identify by criterion at the point of execution, not in a separate
  checklist or verification block.
- R4 signal: V-02's Signal Schema section was introduced with "C-11 satisfier -- precedes YAML
  block," making the section's rubric purpose explicit before any schema rows were written.
  This is the pre-write analogue of C-19: the artifact labels what it is doing and why before
  the reader encounters the content, not after.

**C-23 -- Pivot deliberation before selection**
- Weight: aspirational
- Category: behavior
- Pass condition: Before declaring the pivot mode (C-06), the output enumerates at least 2
  candidate pivot modes with per-candidate assessment, then selects one with a rationale that
  cites a specific row or item from the repo signal inventory produced earlier in the output.
  Declaring a single mode directly with a rationale (C-06 baseline) does not pass; the
  deliberation step -- enumeration of alternatives before selection -- must be present and
  the selection rationale must be traceable to an inventory row, not just a general repo
  observation.
- R4 signal: V-01's Role 2 produced a pivot mode candidates section (multiple modes assessed)
  before the "Selected pivot mode / Rationale" requiring a row citation. This makes pivot
  selection an auditable two-step process: enumerate alternatives with evidence, then select
  with a citation. No other R4 variation enumerated alternatives before selecting.

**C-24 -- Inertia Advocate embedded at group level in YAML hierarchy**
- Weight: aspirational
- Category: depth
- Pass condition: The org.yaml template or output contains Inertia Advocate governance
  annotations at the group/division/tribe/pillar level of the hierarchy -- not only at team
  level. The annotation must appear as a YAML comment or structural element on each named
  group, indicating that Inertia Advocate governance applies at the group level, not just
  within individual teams. A single top-level note (C-10 baseline) or per-team comments
  without group-level comments do not pass.
- R4 signal: V-03's YAML template included a dedicated Inertia Advocate governance comment on
  each group element in the hierarchy (division/tribe/pillar level), embedding the governance
  structure at every level of the org tree. This makes the Inertia Advocate pattern visible to
  a reviewer reading the org structure top-down, not only visible within team blocks.

**C-25 -- Universal output section self-labeling**
- Weight: aspirational
- Category: behavior
- Pass condition: Every structural section in the output -- pre-YAML, YAML-adjacent, and
  post-YAML -- carries a C-NN self-label in its header or opening line. No structural section
  is unlabeled. A single unlabeled section fails. Applying C-22 selectively (to pre-YAML
  sections only) does not pass; the labeling must be a universal structural rule applied to
  the entire output. Distinct from C-22 (at least one pre-YAML section) and C-19 (post-write
  section only) -- C-25 requires the criterion-labeling pattern to cover every section
  without exception.
- R5 signal: V-02 was explicitly noted as "strongest implementation (universal, not just one)"
  when scoring C-22. Every section opened with its C-NN identity, converting the entire output
  into a self-auditing criterion map. No other R5 variation applied the labeling pattern
  universally rather than selectively.

**C-26 -- Multi-criterion section header**
- Weight: aspirational
- Category: behavior
- Pass condition: At least one section header cites 2 or more distinct C-NN criterion IDs as
  simultaneous satisfiers -- e.g., "Section N: C-08 + C-16 satisfier." The section must be
  structurally designed to intersect with multiple criteria, and both criterion IDs must appear
  in the header. A section that satisfies multiple criteria but labels only one in its header
  does not pass; both C-NN labels must be present at point of declaration. Distinct from
  C-22 (one criterion per pre-write header) and C-25 (universal labeling without requiring
  multi-criterion intersection).
- R5 signal: V-02's Section 5 was labeled "C-22: C-08 + C-16 satisfier" -- the amend section
  was deliberately designed to satisfy both the amend listing criterion and the debt-framing
  criterion simultaneously, then declared both in the header. This shows the output was
  architected with criterion intersection in mind, not just criterion coverage.

**C-27 -- Pivot deliberation tri-part candidate assessment**
- Weight: aspirational
- Category: behavior
- Pass condition: Each candidate pivot mode in the deliberation (C-23) carries a three-part
  assessment using a consistent structure: Evidence For / Evidence Against / Assessment (or
  equivalent named triad). At least 2 candidate modes must be assessed in this structure. A
  candidate assessment that gives a summary conclusion without decomposing into a for/against
  evidence structure does not pass. Distinct from C-23 (enumeration with any per-candidate
  assessment) -- C-27 requires the assessment to be structured as an auditable tri-part
  evaluation, not a single-verdict summary.
- R5 signal: V-01's Role 3 (dedicated Pivot Analyst) enumerated all 4 pivot modes, each with
  "Evidence For:", "Evidence Against:", and "Assessment:" entries. The tri-part structure makes
  the deliberation independently falsifiable: a scorer can evaluate whether each Evidence For
  claim is accurate without relying on the model's Assessment conclusion. No other R5 variation
  structured its pivot deliberation as a formal evidence triad.

**C-28 -- Forward-committed pre-check items carry explicit execution-state marker**
- Weight: aspirational
- Category: behavior
- Pass condition: The pre-check or compliance section uses a consistent execution-state
  vocabulary that distinguishes at least 2 states on the pre-check items themselves -- e.g.,
  items marked "SCHEDULED" (committed to a future role, not yet satisfied) vs. items with an
  inline confirmation (already satisfied in this role). The execution-state markers must appear
  on the pre-check items, not in a separate legend or footnote. A pre-check that lists items
  without distinguishing execution state does not pass even if some items are forward-committed
  (C-17 baseline). Distinct from C-17 (forward commitment present) -- C-28 requires each
  forward-committed item to carry an explicit deferred-execution annotation.
- R5 signal: V-01's pre-check marked forward-committed items as "SCHEDULED" for Role 2-4,
  making the deferred execution chain auditable from the pre-check alone. A scorer reading
  the pre-check could immediately identify which items were already satisfied (Compliance
  Officer role) and which were committed to future roles, without reading the rest of the
  output. No other R5 variation used execution-state vocabulary on individual pre-check items.

---

## Criterion Summary

| ID   | Text (short)                                        | Weight       | Category    |
|------|-----------------------------------------------------|--------------|-------------|
| C-01 | Draft org.yaml block present                        | essential    | correctness |
| C-02 | Team areas derived from repo                        | essential    | coverage    |
| C-03 | Group structure present                             | essential    | correctness |
| C-04 | Standard roles per team                             | essential    | coverage    |
| C-05 | Does not write .craft/roles/                        | essential    | behavior    |
| C-06 | Pivot mode declared with rationale                  | recommended  | format      |
| C-07 | Exec office placeholder present                     | recommended  | coverage    |
| C-08 | Amend options listed                                | recommended  | behavior    |
| C-09 | Detection rationale per area                        | aspirational | depth       |
| C-10 | Inertia Advocate noted                              | aspirational | depth       |
| C-11 | Pre-YAML scan inventory listed                      | aspirational | depth       |
| C-12 | Draft boundary front-loaded                         | aspirational | behavior    |
| C-13 | Self-referential compliance check                   | aspirational | behavior    |
| C-14 | Dual-stage YAML bracketing                          | aspirational | behavior    |
| C-15 | Rubric criteria embedded in skill                   | aspirational | depth       |
| C-16 | Debt-framed amend options                           | aspirational | depth       |
| C-17 | Forward commitment to future-section criteria       | aspirational | behavior    |
| C-18 | Criterion ID as primary compliance key              | aspirational | depth       |
| C-19 | Post-write criterion self-labeling                  | aspirational | behavior    |
| C-20 | Structural role ordering as mechanical enforcement  | aspirational | behavior    |
| C-21 | Schema-typed inventory with criterion-labeled cols  | aspirational | depth       |
| C-22 | Pre-write section criterion self-labeling           | aspirational | behavior    |
| C-23 | Pivot deliberation before selection                 | aspirational | behavior    |
| C-24 | Inertia Advocate embedded at group level            | aspirational | depth       |
| C-25 | Universal output section self-labeling              | aspirational | behavior    |
| C-26 | Multi-criterion section header                      | aspirational | behavior    |
| C-27 | Pivot deliberation tri-part candidate assessment    | aspirational | behavior    |
| C-28 | Forward-committed pre-check items carry exec-state  | aspirational | behavior    |

---

## Scoring

**Point weights:**
- Essential (C-01 to C-05): 12 pts each = 60 pts
- Recommended (C-06 to C-08): 10 pts each = 30 pts
- Aspirational (C-09 to C-28): 5 pts each = 100 pts
- **Total: 190 pts**

PASS = full points. PARTIAL = half points. FAIL = 0.

**Golden threshold: 80 pts with all 5 essential passing.**

---

## Score Examples

**Minimum passing (golden threshold)**:
- All 5 essential pass: 60 pts
- 2/3 recommended pass: 20 pts
- 0/20 aspirational: 0 pts
- Composite: 80 -- passes golden threshold

**Strong output**:
- All 5 essential pass: 60 pts
- All 3 recommended pass: 30 pts
- 4/20 aspirational pass: 20 pts
- Composite: 110

**Ceiling output**:
- All 5 essential pass: 60 pts
- All 3 recommended pass: 30 pts
- All 20 aspirational pass: 100 pts
- Composite: 190

**Failing output (common failure)**:
- C-05 fails (wrote .craft/roles/): essential fail -- not golden regardless of composite score

**R5 reference scores (all scored 170/170 under v5; v6 separates V-01 and V-02 from V-03)**:
- V-01 (Role Sequence): 180/190 -- C-27 PASS (tri-part deliberation), C-28 PASS (SCHEDULED
  markers), C-25 FAIL, C-26 FAIL
- V-02 (Universal Self-Labeling): 180/190 -- C-25 PASS (universal labeling), C-26 PASS
  (multi-criterion header), C-27 FAIL, C-28 FAIL
- V-03 (Inertia Framing): 170/190 -- C-25 FAIL, C-26 FAIL, C-27 FAIL, C-28 FAIL

V-01 and V-02 both reach 180, each earning different 10-pt gains from distinct technique
clusters (deliberation structure + execution tracking vs. universal labeling + criterion
intersection). V-03 stays at 170 -- its R5 innovations were fully captured by C-09 through
C-24. The new criteria correctly identify the R5 frontier as split between two approaches
rather than converged on a single winner.

---

## Change Log

| Version | Date       | Change |
|---------|------------|--------|
| v1      | 2026-03-16 | Initial rubric -- 10 criteria (5E/3R/2A), 100 pts |
| v2      | 2026-03-16 | Add C-11 (pre-YAML scan inventory) and C-12 (draft boundary front-loaded) from R1 excellence signals; 12 criteria (5E/3R/4A), 110 pts |
| v3      | 2026-03-16 | Add C-13 through C-16 from R2 excellence signals: self-referential compliance check, dual-stage YAML bracketing, rubric criteria embedded in skill, debt-framed amend options; 16 criteria (5E/3R/8A), 130 pts |
| v4      | 2026-03-16 | Add C-17 through C-20 from R3 excellence signals: forward commitment to future-section criteria, criterion ID as primary compliance key, post-write criterion self-labeling, structural role ordering as mechanical enforcement; 20 criteria (5E/3R/12A), 150 pts |
| v5      | 2026-03-16 | Add C-21 through C-24 from R4 excellence signals: schema-typed inventory with criterion-labeled columns (V-02), pre-write section criterion self-labeling (V-02), pivot deliberation before selection (V-01), Inertia Advocate embedded at group level (V-03); R4 first round where all variations scored 150/150; 24 criteria (5E/3R/16A), 170 pts |
| v6      | 2026-03-16 | Add C-25 through C-28 from R5 excellence signals: universal output section self-labeling (V-02 -- C-22 extended to all sections), multi-criterion section header (V-02 -- one header cites 2+ C-NN IDs), pivot deliberation tri-part candidate assessment (V-01 -- Evidence For/Against/Assessment triad), forward-committed pre-check items carry execution-state marker (V-01 -- SCHEDULED annotation); R5 first round where all variations scored 170/170; 28 criteria (5E/3R/20A), 190 pts |
