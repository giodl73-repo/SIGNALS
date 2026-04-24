Written to `simulations/quest/rubrics/corps-scan-rubric-v2-2026-03-16.md`.

---

**Two new aspirational criteria added:**

**C-11 — Pre-YAML scan inventory listed** (depth)
The R1 signal: V-01 got C-02 PARTIAL because it jumped straight to YAML with inline annotations but no distinct inventory step. V-03 and V-04 both passed C-02 fully because their design forced an explicit enumeration of detected signals *before* YAML production started. The inventory step makes repo grounding verifiable rather than implicit.

**C-12 — Draft boundary front-loaded before first output** (behavior)
The R1 signal: V-03 showed "DRAFT GATE states the draft-only constraint as an entry condition." This is a stronger compliance form than C-05 (which tests *what* was produced) — C-12 tests whether the reviewer is primed to read the YAML as a draft *before* they encounter it. Burying the boundary acknowledgment after the YAML doesn't pass.

**Scoring change:** Total bumps from 100 to 110 pts (4 aspirationals at 5 pts each). Golden threshold stays at 80 pts absolute. V-03 and V-04 now project to ~98 and ~100 respectively under v2, confirming the new criteria correctly reward the best-performing variations.
he YAML looks. That is the failure pattern most worth detecting early.

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

---

## Criterion Summary

| ID   | Text (short)                         | Weight       | Category    |
|------|--------------------------------------|--------------|-------------|
| C-01 | Draft org.yaml block present         | essential    | correctness |
| C-02 | Team areas derived from repo         | essential    | coverage    |
| C-03 | Group structure present              | essential    | correctness |
| C-04 | Standard roles per team              | essential    | coverage    |
| C-05 | Does not write .roles/         | essential    | behavior    |
| C-06 | Pivot mode declared with rationale   | recommended  | format      |
| C-07 | Exec office placeholder present      | recommended  | coverage    |
| C-08 | Amend options listed                 | recommended  | behavior    |
| C-09 | Detection rationale per area         | aspirational | depth       |
| C-10 | Inertia Advocate noted               | aspirational | depth       |
| C-11 | Pre-YAML scan inventory listed       | aspirational | depth       |
| C-12 | Draft boundary front-loaded          | aspirational | behavior    |

---

## Scoring

**Point weights:**
- Essential (C-01 to C-05): 12 pts each = 60 pts
- Recommended (C-06 to C-08): 10 pts each = 30 pts
- Aspirational (C-09 to C-12): 5 pts each = 20 pts
- **Total: 110 pts**

PASS = full points. PARTIAL = half points. FAIL = 0.

**Golden threshold: 80 pts with all 5 essential passing.**

---

## Score Examples

**Minimum passing (golden threshold)**:
- All 5 essential pass: 60 pts
- 2/3 recommended pass: 20 pts
- 0/4 aspirational: 0 pts
- Composite: 80 -- passes golden threshold

**Strong output**:
- All 5 essential pass: 60 pts
- All 3 recommended pass: 30 pts
- 2/4 aspirational pass: 10 pts
- Composite: 100

**Ceiling output** (V-04 class):
- All 5 essential pass: 60 pts
- All 3 recommended pass: 30 pts
- All 4 aspirational pass: 20 pts
- Composite: 110

**Failing output (common failure)**:
- C-05 fails (wrote .roles/): essential fail -- not golden regardless of composite score

**R1 reference scores (adjusted for v2 criteria)**:
- V-01 (YAML-First, inline annotations): ~89 -- C-11 fails (no pre-YAML inventory), C-12 likely passes
- V-02 (Conversational): ~74 -- C-11 PARTIAL (conversational narration is close but unstructured), C-12 PARTIAL
- V-03 (Phase Gates): ~98 -- C-11 PASS (SCAN phase is the inventory), C-12 PASS (DRAFT gate entry condition)
- V-04 (Archaeologist + Inertia): ~100 -- C-11 PASS (Archaeologist inventory), C-12 PASS (two-stage framing is inherently draft-first)

---

## Change Log

| Version | Date       | Change |
|---------|------------|--------|
| v1      | 2026-03-16 | Initial rubric -- 10 criteria (5E/3R/2A), 100 pts |
| v2      | 2026-03-16 | Add C-11 (pre-YAML scan inventory) and C-12 (draft boundary front-loaded) from R1 excellence signals; total now 12 criteria (5E/3R/4A), 110 pts |
