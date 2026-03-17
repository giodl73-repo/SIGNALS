Written to `simulations/quest/rubrics/corps-scan-rubric-v3-2026-03-16.md`.

---

**Four new aspirational criteria added from R2 excellence signals:**

**C-13 -- Self-referential compliance check** (behavior)
V-04's PRE-CHECK item 3 confirmed itself in-output: "The draft-only statement appears before any YAML. STATUS: CONFIRMED." The model cannot satisfy the checklist item without having already satisfied C-12. Constraint becomes self-enforcing at execution time, not just declared.

**C-14 -- Dual-stage YAML bracketing** (behavior)
V-04 is the only R2 variation to verify constraints both BEFORE (PRE-CHECK) and AFTER (post-write checklist) the YAML artifact. A pre-check without a post-write note, or vice versa, is PARTIAL. Makes violations detectable mid-output.

**C-15 -- Rubric criteria embedded as skill requirements** (depth)
V-04's PRE-CHECK items map 1:1 to C-04, C-05, C-07, C-11, C-12. The rubric criteria become the skill's own stated requirements — scoring criteria are transparent and enforceable in the output itself. Minimum bar: 3 criteria explicitly named.

**C-16 -- Debt-framed amend options** (depth)
V-05 introduced "Debt if skipped" notation per AMEND option — the only variation to name downstream pipeline consequences. Converts C-08 from navigation aids into decision-support tools. At least 2 options must name the debt to pass.

**Scoring change**: Total bumps from 110 to 130 pts (8 aspirationals × 5 pts). Golden threshold stays at 80 pts absolute.

**R2 projected scores under v3**: V-04 ~125, V-05 ~118, V-01/02/03 all ~110. The new criteria correctly separate the two structurally distinct top performers from the pack.
rganizational debt that accumulates if each amend option
is skipped (e.g., "Debt if skipped: exec-office stage cannot run without this"). Converts C-08
amend options from navigation aids into decision-support tools, giving the reviewer a reason to
act rather than just names of options.

**Scoring change**: Total bumps from 110 to 130 pts (8 aspirationals × 5 pts each). Golden
threshold stays at 80 pts absolute.

**R2 projected scores under v3**:
- V-04: 125/130 (C-13 PASS, C-14 PASS, C-15 PASS, C-16 FAIL -- no debt framing in amends)
- V-05: 118/130 (C-13 FAIL, C-14 PARTIAL -- post-YAML note but no full checklist, C-15 FAIL, C-16 PASS)
- V-01: 110/130 (C-13/14/15/16 all FAIL)
- V-02: 110/130 (same)
- V-03: 110/130 (same)

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

**C-05 -- Does not write .craft/roles/**
- Weight: essential
- Category: behavior
- Pass condition: Output explicitly states this is a draft for human review and does NOT produce
  .craft/roles/ files, does NOT instruct the user to create role files, and does NOT include
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

---

## Criterion Summary

| ID   | Text (short)                         | Weight       | Category    |
|------|--------------------------------------|--------------|-------------|
| C-01 | Draft org.yaml block present         | essential    | correctness |
| C-02 | Team areas derived from repo         | essential    | coverage    |
| C-03 | Group structure present              | essential    | correctness |
| C-04 | Standard roles per team              | essential    | coverage    |
| C-05 | Does not write .craft/roles/         | essential    | behavior    |
| C-06 | Pivot mode declared with rationale   | recommended  | format      |
| C-07 | Exec office placeholder present      | recommended  | coverage    |
| C-08 | Amend options listed                 | recommended  | behavior    |
| C-09 | Detection rationale per area         | aspirational | depth       |
| C-10 | Inertia Advocate noted               | aspirational | depth       |
| C-11 | Pre-YAML scan inventory listed       | aspirational | depth       |
| C-12 | Draft boundary front-loaded          | aspirational | behavior    |
| C-13 | Self-referential compliance check    | aspirational | behavior    |
| C-14 | Dual-stage YAML bracketing           | aspirational | behavior    |
| C-15 | Rubric criteria embedded in skill    | aspirational | depth       |
| C-16 | Debt-framed amend options            | aspirational | depth       |

---

## Scoring

**Point weights:**
- Essential (C-01 to C-05): 12 pts each = 60 pts
- Recommended (C-06 to C-08): 10 pts each = 30 pts
- Aspirational (C-09 to C-16): 5 pts each = 40 pts
- **Total: 130 pts**

PASS = full points. PARTIAL = half points. FAIL = 0.

**Golden threshold: 80 pts with all 5 essential passing.**

---

## Score Examples

**Minimum passing (golden threshold)**:
- All 5 essential pass: 60 pts
- 2/3 recommended pass: 20 pts
- 0/8 aspirational: 0 pts
- Composite: 80 -- passes golden threshold

**Strong output**:
- All 5 essential pass: 60 pts
- All 3 recommended pass: 30 pts
- 4/8 aspirational pass: 20 pts
- Composite: 110

**Ceiling output**:
- All 5 essential pass: 60 pts
- All 3 recommended pass: 30 pts
- All 8 aspirational pass: 40 pts
- Composite: 130

**Failing output (common failure)**:
- C-05 fails (wrote .craft/roles/): essential fail -- not golden regardless of composite score

**R2 reference scores (projected under v3)**:
- V-04 (Compliance Pre-Check): ~125 -- C-13 PASS, C-14 PASS, C-15 PASS, C-16 FAIL
- V-05 (Evidence Mandate): ~118 -- C-13 FAIL, C-14 PARTIAL, C-15 FAIL, C-16 PASS
- V-01 (Constraint-First): ~110 -- C-13/14/15/16 all FAIL
- V-02 (Signal-Table): ~110 -- same
- V-03 (Minimal): ~110 -- same

---

## Change Log

| Version | Date       | Change |
|---------|------------|--------|
| v1      | 2026-03-16 | Initial rubric -- 10 criteria (5E/3R/2A), 100 pts |
| v2      | 2026-03-16 | Add C-11 (pre-YAML scan inventory) and C-12 (draft boundary front-loaded) from R1 excellence signals; total now 12 criteria (5E/3R/4A), 110 pts |
| v3      | 2026-03-16 | Add C-13 through C-16 from R2 excellence signals: self-referential compliance check, dual-stage YAML bracketing, rubric criteria embedded in skill, debt-framed amend options; total now 16 criteria (5E/3R/8A), 130 pts |
