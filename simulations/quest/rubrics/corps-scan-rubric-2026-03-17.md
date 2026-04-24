Rubric written to `simulations/quest/rubrics/corps-scan-rubric-2026-03-17.md`.

**Summary:**

| Tier | Criteria | Focus |
|------|----------|-------|
| Essential (x5) | C-01 YAML present, C-02 repo-grounded, C-03 group hierarchy, C-04 roles per team, C-05 no .roles writes | Output is valid and boundary-safe |
| Recommended (x3) | C-06 pivot mode + rationale, C-07 exec-office placeholder, C-08 amend options | Output is reviewable and pipeline-ready |
| Aspirational (x2) | C-09 pre-YAML scan inventory, C-10 draft boundary front-loaded | Output is auditable and primes the reviewer |

The 5 essentials are drawn from the stable core that survived all 13 prior rounds — they're the criteria that, if absent, make the output unusable (wrong artifact, ungrounded, flat, incomplete, or boundary violation). C-09 and C-10 as aspirationals represent the two patterns most consistently associated with high-scoring variations (structured pre-YAML inventory enables C-02 grounding; front-loaded draft declaration makes the output self-priming).
 not JSON, not an informal bullet
  list of team names. A code fence containing only partial key coverage (e.g., teams but no
  groups) does not pass.

**C-02 -- Team areas derived from repo signals**
- Weight: essential
- Category: coverage
- Pass condition: Team names and group structure in the YAML are grounded in actual repo signals
  (directory names, service paths, module identifiers, domain terms) rather than invented or
  generic. At least half the team names must have a traceable basis in repo signals named
  somewhere in the output — pre-YAML inventory, inline YAML comment, or prose explanation. A
  fully generic org chart (e.g., Frontend / Backend / Infrastructure with no repo grounding)
  fails even if syntactically valid.

**C-03 -- Group structure organizes teams**
- Weight: essential
- Category: correctness
- Pass condition: The YAML `groups:` section contains at least one named group container that
  organizes teams beneath it (e.g., divisions, tribes, pillars). An org.yaml that lists teams
  at the top level without grouping them fails — group structure is required for corps-build and
  corps-rob compatibility. A single group containing all teams passes; a flat team list with no
  group hierarchy does not.

**C-04 -- Standard roles present per team**
- Weight: essential
- Category: coverage
- Pass condition: Each team entry in the YAML includes a `roles:` list with at least one named
  role. Role names must be substantive (e.g., "Product Manager", "Engineer", "Tech Lead") rather
  than placeholder tokens (e.g., "role_1", "TBD"). The Inertia Advocate must NOT appear in the
  draft output — it is auto-added by corps-build and is outside corps-scan scope.

**C-05 -- Does not write .roles/**
- Weight: essential
- Category: behavior
- Pass condition: The output contains no role file content and makes no attempt to write, draft,
  or present `.roles/` file markdown. Any output that writes role files or presents role
  file markdown in any form fails. This boundary (scan = draft org.yaml only; build = role
  files) must be respected unconditionally.

---

## RECOMMENDED

Three criteria. Each worth 10 pts (30 pts total if all pass).

---

**C-06 -- Pivot mode declared with rationale**
- Weight: recommended
- Category: format
- Pass condition: Output names the pivot mode used (directory / concept / service / domain) and
  provides at least one sentence explaining why that mode was selected based on observed repo
  signals (e.g., "using directory mode: repo has clear top-level service directories under
  /src"). Declaring a mode without rationale does not pass — the rationale is what makes the
  draft reviewable and the mode choice reversible.

**C-07 -- Exec office placeholder present**
- Weight: recommended
- Category: coverage
- Pass condition: `org.yaml` contains an `exec-office:` section with at least a name field, even
  if no teams are listed under it. Absence of exec office means the output cannot feed the
  corps-rob exec-office stage without manual addition, breaking the downstream pipeline contract.

**C-08 -- Amend options listed**
- Weight: recommended
- Category: behavior
- Pass condition: Output concludes with at least 2 named amend options drawn from the documented
  AMEND set: (a) change pivot mode, (b) rename exec office, (c) adjust group structure. Options
  must be actionable — e.g., "AMEND: switch to service mode — run /corps-scan --pivot service".
  A generic "let me know if you want changes" does not pass; each option must name the change and
  the action to take.

---

## ASPIRATIONAL

Two criteria. Each worth 5 pts (10 pts total if both pass).

---

**C-09 -- Pre-YAML scan inventory listed**
- Weight: aspirational
- Category: depth
- Pass condition: Before the YAML block, the output lists the repo signals it detected as a
  readable inventory of directory names, service paths, module identifiers, or domain terms. The
  inventory must be structurally distinct from the YAML (not the YAML itself) and must appear
  before the YAML block begins. This makes C-02 grounding independently verifiable without
  re-reading the repo. Outputs with only inline YAML comments but no pre-YAML inventory do not
  pass.

**C-10 -- Draft boundary stated before first structural content**
- Weight: aspirational
- Category: behavior
- Pass condition: The draft-only framing — that this output is a proposal for human review, not
  a build instruction — is stated explicitly before any YAML or structural content appears. A
  single sentence such as "This is a draft org.yaml for review — no role files will be created"
  appearing as the first substantive line passes. Burying the boundary acknowledgment after the
  YAML, or only at the very end, does not pass.

---

## Score Reference

| Tier | Criteria | Points Available |
|------|----------|-----------------|
| Essential | C-01 through C-05 (5 criteria) | 60 pts |
| Recommended | C-06 through C-08 (3 criteria) | 30 pts |
| Aspirational | C-09 through C-10 (2 criteria) | 10 pts |
| **Total** | | **100 pts** |

**Golden**: all 5 essentials pass AND composite >= 80.

Example passing scores:
- 5E + 3R + 2A = 100 pts (perfect)
- 5E + 3R + 0A = 90 pts (golden)
- 5E + 2R + 2A = 80 pts (golden, threshold)
- 5E + 2R + 1A = 75 pts (below threshold — not golden)
- 4E + 3R + 2A = disqualified (essential failure)
