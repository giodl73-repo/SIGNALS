Written to `simulations/quest/rubrics/corps-scan-rubric-v4-2026-03-16.md`.

---

**Four new aspirational criteria from R3 excellence signals:**

**C-17 -- Forward commitment to future-section criteria** (behavior)
P-1 (V-04 C-16 pre-scheduled). The pre-check contains at least one item whose satisfying section hasn't been written yet. Distinguishes from C-14: C-14 is retrospective confirmation; C-17 is prospective commitment. Must have at least one identifiably forward-committed item.

**C-18 -- Criterion ID as primary compliance key** (depth)
P-2 (criterion ID as checklist header). Compliance structure uses C-NN IDs as the primary key for at least 5 items. Rubric-to-output mapping becomes auditable without the rubric document present. Prose descriptions without the ID do not pass.

**C-19 -- Post-write criterion self-labeling** (behavior)
P-3 (C-14 self-labeled in artifact). Post-write verification block cites the criterion ID it is satisfying (e.g., "C-14 dual-bracket: both present"). Distinct from C-15 (pre-fact embedding) and C-14 (structure). At least one post-write block must cite a C-NN ID.

**C-20 -- Structural role ordering as mechanical enforcement** (behavior)
P-4 (role-sequence enforcement). Compliance pre-check is owned by a named role that must complete before any scan or YAML work is assigned. Instruction-level reminders do not pass; ownership must be structural.

**Scoring change**: 130 → 150 pts (12 aspirationals × 5 pts). Golden threshold stays at 80 pts.

**R3 projected under v4**: V-04 145, V-01 135, V-02/03/05 all 130 — correctly separates the two structurally distinct R3 leaders from the cluster.
isfying. No external rubric reference needed to audit compliance.

**C-20 -- Structural role ordering as mechanical enforcement** (behavior)
V-01 assigned sole ownership of the compliance pre-check to a named role that must complete
before any scan or YAML work is assigned to another role. The sequence enforces compliance
structurally: a model following the role ordering cannot begin repo analysis or YAML
production until the compliance role finishes. Instruction-level compliance ("remember to
check...") does not pass; the check must be assigned to a distinct first-completing role
whose completion is a prerequisite for the roles that follow.

**Scoring change**: Total bumps from 130 to 150 pts (12 aspirationals x 5 pts). Golden
threshold stays at 80 pts absolute.

**R3 projected scores under v4**:
- V-04 (Pre-Check + Debt): 145/150 -- C-17 PASS, C-18 PASS, C-19 PASS, C-20 FAIL
- V-01 (Role Sequence): 135/150 -- C-17 FAIL, C-18 FAIL, C-19 FAIL, C-20 PASS
- V-02 (Signal Schema): 130/150 -- C-17/18/19/20 all FAIL
- V-03 (Formal Reqs): 130/150 -- same
- V-05 (Phase Gates): 130/150 -- same

The new criteria correctly separate V-04 (pre-commitment + ID-keyed compliance) and V-01
(structural role enforcement) from the R3 130/130 cluster.

---

## Criterion Definitions

### ESSENTIAL

**C-01 -- Draft org.yaml block present**
- Weight: essential
- Category: correctness
- Pass condition: Output contains an actual YAML block representing the draft org structure.
  Prose that describes what the YAML would contain does NOT pass. The YAML must be present in
  the output, not deferred.

**C-02 -- Detected team areas derived from repo**
- Weight: essential
- Category: coverage
- Pass condition: org.yaml contains at least 2 team areas whose names or paths are traceable to
  actual repo signals (directory names, service identifiers, module paths, or domain terms found
  in the repo). Generic placeholder names like "team-a" or "area-1" without repo grounding fail.

**C-03 -- Group structure present**
- Weight: essential
- Category: correctness
- Pass condition: org.yaml includes at least one level of structural grouping above individual
  teams -- a division, tribe, or pillar -- that organizes the detected areas into a hierarchy.
  A flat list of teams with no grouping fails.

**C-04 -- Standard roles per team**
- Weight: essential
- Category: coverage
- Pass condition: Each team area in org.yaml lists at least 2 standard role suggestions. Roles
  must be named (e.g., PM, Engineer, Tech Lead, Security Architect) not described as "roles go
  here." Inertia Advocate does not count toward the minimum -- it is always included by
  corp-build automatically.

**C-05 -- Does not write .roles/**
- Weight: essential
- Category: behavior
- Pass condition: Output explicitly states this is a draft for human review and does NOT produce
  .roles/ files, does NOT instruct the user to create role files, and does NOT include
  role file content. The boundary between corp-scan (draft) and corp-build (build) must be
  respected. Any output that writes role files or presents role file markdown fails.

---

### RECOMMENDED

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

### ASPIRATIONAL

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
  write .roles/ files," "2+ named roles per team area." This makes the scoring criteria
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

---

## Criterion Summary

| ID   | Text (short)                                        | Weight       | Category    |
|------|-----------------------------------------------------|--------------|-------------|
| C-01 | Draft org.yaml block present                        | essential    | correctness |
| C-02 | Team areas derived from repo                        | essential    | coverage    |
| C-03 | Group structure present                             | essential    | correctness |
| C-04 | Standard roles per team                             | essential    | coverage    |
| C-05 | Does not write .roles/                        | essential    | behavior    |
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

---

## Scoring

**Point weights:**
- Essential (C-01 to C-05): 12 pts each = 60 pts
- Recommended (C-06 to C-08): 10 pts each = 30 pts
- Aspirational (C-09 to C-20): 5 pts each = 60 pts
- **Total: 150 pts**

PASS = full points. PARTIAL = half points. FAIL = 0.

**Golden threshold: 80 pts with all 5 essential passing.**

---

## Score Examples

**Minimum passing (golden threshold)**:
- All 5 essential pass: 60 pts
- 2/3 recommended pass: 20 pts
- 0/12 aspirational: 0 pts
- Composite: 80 -- passes golden threshold

**Strong output**:
- All 5 essential pass: 60 pts
- All 3 recommended pass: 30 pts
- 4/12 aspirational pass: 20 pts
- Composite: 110

**Ceiling output**:
- All 5 essential pass: 60 pts
- All 3 recommended pass: 30 pts
- All 12 aspirational pass: 60 pts
- Composite: 150

**Failing output (common failure)**:
- C-05 fails (wrote .roles/): essential fail -- not golden regardless of composite score

**R3 reference scores (projected under v4)**:
- V-04 (Pre-Check + Debt): 145/150 -- C-17 PASS, C-18 PASS, C-19 PASS, C-20 FAIL
- V-01 (Role Sequence): 135/150 -- C-17 FAIL, C-18 FAIL, C-19 FAIL, C-20 PASS
- V-02 (Signal Schema): 130/150 -- C-17/18/19/20 all FAIL
- V-03 (Formal Reqs): 130/150 -- same
- V-05 (Phase Gates): 130/150 -- same

---

## Change Log

| Version | Date       | Change |
|---------|------------|--------|
| v1      | 2026-03-16 | Initial rubric -- 10 criteria (5E/3R/2A), 100 pts |
| v2      | 2026-03-16 | Add C-11 (pre-YAML scan inventory) and C-12 (draft boundary front-loaded) from R1 excellence signals; total now 12 criteria (5E/3R/4A), 110 pts |
| v3      | 2026-03-16 | Add C-13 through C-16 from R2 excellence signals: self-referential compliance check, dual-stage YAML bracketing, rubric criteria embedded in skill, debt-framed amend options; total now 16 criteria (5E/3R/8A), 130 pts |
| v4      | 2026-03-16 | Add C-17 through C-20 from R3 excellence signals: forward commitment to future-section criteria, criterion ID as primary compliance key, post-write criterion self-labeling, structural role ordering as mechanical enforcement; total now 20 criteria (5E/3R/12A), 150 pts |
