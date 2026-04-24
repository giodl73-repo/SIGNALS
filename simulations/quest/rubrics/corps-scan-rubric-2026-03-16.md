Rubric written to `simulations/quest/rubrics/corps-scan-rubric-2026-03-16.md`.

**10 criteria across 3 tiers:**

**Essential (5)** -- all must pass:
- **C-01** Actual YAML block in output (not prose promises)
- **C-02** Team areas grounded in repo signals (not generic placeholders)
- **C-03** Group hierarchy above team level (division/tribe/pillar)
- **C-04** Named roles per team (2+ per area)
- **C-05** Hard boundary: no .roles/ output (corp-scan is draft-only)

**Recommended (3)**:
- **C-06** Pivot mode named + rationale
- **C-07** Exec office placeholder in YAML
- **C-08** Amend options at the end (actionable, not generic)

**Aspirational (2)**:
- **C-09** Detection rationale inline per area (makes the draft reviewable)
- **C-10** Inertia Advocate noted (primes the user for corp-build behavior)

The hard constraint is C-05 -- a corp-scan that writes role files is broken by design regardless of how good the YAML looks. That's the failure pattern most worth detecting early.
at the YAML would
  contain does NOT pass. The YAML must be present in the output, not deferred.

**C-02 — Detected team areas derived from repo**
- Weight: essential
- Category: coverage
- Pass condition: org.yaml contains at least 2 team areas whose names or paths are traceable to
  actual repo signals (directory names, service identifiers, module paths, or domain terms found
  in the repo). Generic placeholder names like "team-a" or "area-1" without repo grounding fail.

**C-03 — Group structure present**
- Weight: essential
- Category: correctness
- Pass condition: org.yaml includes at least one level of structural grouping above individual
  teams -- a division, tribe, or pillar -- that organizes the detected areas into a hierarchy.
  A flat list of teams with no grouping fails.

**C-04 — Standard roles per team**
- Weight: essential
- Category: coverage
- Pass condition: Each team area in org.yaml lists at least 2 standard role suggestions. Roles
  must be named (e.g., PM, Engineer, Tech Lead, Security Architect) not described as "roles go
  here." Inertia Advocate does not count toward the minimum -- it is always included by
  corp-build automatically.

**C-05 — Does not write .roles/**
- Weight: essential
- Category: behavior
- Pass condition: Output explicitly states this is a draft for human review and does NOT produce
  .roles/ files, does NOT instruct the user to create role files, and does NOT include
  role file content. The boundary between corp-scan (draft) and corp-build (build) must be
  respected. Any output that writes role files or presents role file markdown fails.

---

### RECOMMENDED

**C-06 — Pivot mode declared with rationale**
- Weight: recommended
- Category: format
- Pass condition: Output names the pivot mode used (directory / concept / service / domain) and
  provides at least one sentence explaining why that mode was selected based on repo signals
  (e.g., "using directory mode: repo has clear top-level service directories under /src").
  Declaring a mode without rationale is partial credit -- does not pass.

**C-07 — Exec office placeholder present**
- Weight: recommended
- Category: coverage
- Pass condition: org.yaml contains an exec-office section (even a minimal placeholder with a
  name and no teams). Absence of exec office means the output cannot feed corp-rob exec-office
  stage without manual addition.

**C-08 — Amend options listed**
- Weight: recommended
- Category: behavior
- Pass condition: Output concludes with at least 2 named amend options drawn from the documented
  AMEND set: (a) change pivot mode, (b) rename exec office, (c) adjust group structure. Options
  must be actionable (e.g., "AMEND: switch to service mode -- run /corps-scan --pivot service").
  A generic "let me know if you want changes" does not pass.

---

### ASPIRATIONAL

**C-09 — Detection rationale per area**
- Weight: aspirational
- Category: depth
- Pass condition: At least half of the detected team areas include an inline comment or
  annotation explaining the repo evidence that produced them (e.g., "# detected from
  /services/payments/, 3 service directories"). This makes the draft reviewable without
  re-reading the repo.

**C-10 — Inertia Advocate noted**
- Weight: aspirational
- Category: depth
- Pass condition: Output notes -- at least once, in prose or as a YAML comment -- that Inertia
  Advocate will be auto-included per team when corp-build runs. This primes the user to expect
  the Inertia Advocate in the role files without configuring it manually.

---

## Criterion Summary

| ID   | Text (short)                       | Weight        | Category    |
|------|------------------------------------|---------------|-------------|
| C-01 | Draft org.yaml block present       | essential     | correctness |
| C-02 | Team areas derived from repo       | essential     | coverage    |
| C-03 | Group structure present            | essential     | correctness |
| C-04 | Standard roles per team            | essential     | coverage    |
| C-05 | Does not write .roles/       | essential     | behavior    |
| C-06 | Pivot mode declared with rationale | recommended   | format      |
| C-07 | Exec office placeholder present    | recommended   | coverage    |
| C-08 | Amend options listed               | recommended   | behavior    |
| C-09 | Detection rationale per area       | aspirational  | depth       |
| C-10 | Inertia Advocate noted             | aspirational  | depth       |

---

## Score Examples

**Minimum passing (golden threshold)**:
- All 5 essential pass: 60 pts
- 2/3 recommended pass: 20 pts
- 0/2 aspirational: 0 pts
- Composite: 80 -- passes golden threshold

**Strong output**:
- All 5 essential pass: 60 pts
- All 3 recommended pass: 30 pts
- 1/2 aspirational pass: 5 pts
- Composite: 95

**Failing output (common failure)**:
- C-05 fails (wrote .roles/): essential fail -- not golden regardless of composite score
