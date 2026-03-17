Written to `simulations/quest/rubrics/corps-scan-rubric-v2-2026-03-17.md`.

---

## What changed and why

**Three new aspirationals extracted from R1:**

**C-11 — Inventory formatted as typed table**
V-02's marginal quality advantage on C-02 and C-06 came entirely from structured columns. A bulleted list satisfies C-09; only a typed table with a signal identifier column and a relevance column makes each row independently verifiable. C-09 was the gate; C-11 is the quality ceiling above it.

**C-12 — Pivot rationale cites specific named signal**
C-06 passes with any explanatory sentence. V-05 earned the "most auditable rationale chain" callout because its rationale named a specific table row. C-12 makes that edge a scorable criterion: the rationale must contain a named path or identifier, not a generic observation about repo shape.

**C-13 — Hard ordering gate between inventory and YAML**
V-04's failure surface (C-03 and C-04 below threshold) came directly from having phase gates with conversational YAML phrasing. V-03 had no gate at all. The sentinel line or explicit "DO NOT begin" instruction is what converts C-09 from advisory to unconditional across phrasing registers. C-13 names this mechanism explicitly.

**Score correction:** v1 score table listed aspirationals at 5 pts each but the actual R1 scorecard applied 10 pts per criterion uniformly. v2 corrects this — 13 criteria × 10 pts = 130 pts max. The golden threshold (80 pts) is unchanged in absolute terms, still achievable with 5E + 3R + 0A.
ventory — the typed table is a
  stronger form that enables per-row auditability.

- **C-12** (rationale cites specific named signal): V-02 and V-05 both require rationale to
  "cite at least one specific Signal from the table above" by name or path. C-06 only requires
  "one sentence explaining why." V-05 earned the "most auditable rationale chain" callout; this
  criterion formalizes that edge.

- **C-13** (hard ordering gate): V-01 uses `--- [SCAN COMPLETE] ---`; V-02 uses "DO NOT begin
  STEP 2 until the table is written." V-04 had phase gates but conversational phrasing softened
  them — C-03 and C-04 were the resulting failure surface. V-03 had no gate at all. The hard
  gate is what makes pre-YAML inventory unconditional across phrasing register changes.

---

## ESSENTIAL

Five criteria. Each worth 10 pts (50 pts total if all pass). Any essential failure disqualifies
the output from golden regardless of composite score.

---

**C-01 -- Valid org.yaml code fence produced**
- Weight: essential
- Category: format
- Pass condition: Output contains a single `yaml` code fence identified as `org.yaml` that
  includes at minimum the keys `groups:`, `teams:`, and `exec-office:`. Output in any other
  format — prose description of an org chart, JSON, an informal bullet list of team names, or a
  partial YAML fragment — does not pass. A code fence containing only partial key coverage (e.g.,
  teams but no groups) does not pass.

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

**C-05 -- Does not write .craft/roles/**
- Weight: essential
- Category: behavior
- Pass condition: The output contains no role file content and makes no attempt to write, draft,
  or present `.craft/roles/` file markdown. Any output that writes role files or presents role
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
  draft reviewable and the mode choice reversible. Note: C-12 further requires the rationale to
  cite a specific named signal; C-06 passes with any explanatory sentence.

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

Five criteria. Each worth 10 pts (50 pts total if all pass).

C-09 and C-10 carry forward from v1. C-11, C-12, C-13 are new in v2.

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

**C-11 -- Inventory formatted as typed table**
- Weight: aspirational
- Category: depth
- Pass condition: The pre-YAML inventory is presented as a typed table with at least two named
  columns — minimally a signal identifier column (path, name, or module) and a relevance or
  category column (e.g., Pivot Relevance, Signal Type, Domain). A bulleted list alone does not
  pass. Typed columns make each signal's basis independently verifiable without re-reading the
  repo and enable the pivot rationale (C-06, C-12) to cite a specific table row rather than a
  free-form claim. Requires C-09 to pass — a typed table that appears after the YAML does not
  satisfy this criterion.

**C-12 -- Pivot rationale cites specific named signal**
- Weight: aspirational
- Category: format
- Pass condition: The rationale for pivot mode selection names at least one specific signal from
  the inventory by path or identifier (e.g., "/src/api/, /src/auth/, /src/billing/ — three
  parallel service directories → directory mode"). A generic justification ("this repo appears
  service-oriented" or "the repo structure suggests services") without naming a specific
  inventory signal does not pass. A named anchor makes the pivot choice independently auditable:
  a reviewer can verify the cited signal without re-reading the full scan. This criterion
  strengthens C-06 — C-06 can pass with any explanatory sentence; C-12 requires that sentence
  to contain a named signal from the inventory.

**C-13 -- Hard ordering gate between inventory and YAML**
- Weight: aspirational
- Category: behavior
- Pass condition: A structural ordering mechanism prevents YAML generation before the inventory
  is complete — e.g., a sentinel line (`--- [SCAN COMPLETE] ---`), an explicit "DO NOT begin
  YAML until inventory is written" instruction, or an equivalent phase gate that must be
  satisfied before YAML authoring begins. Advisory sequencing ("first do X, then do Y") without
  an explicit enforcement mechanism does not pass. The gate is what converts the pre-YAML
  inventory from advisory to unconditional, protecting C-09 across conversational phrasing
  registers. Root cause note: V-04 had phase gates but conversational YAML phrasing left C-03
  and C-04 below threshold — C-13 requires the gate itself to be explicit and unconditional.

---

## Score Reference

| Tier | Criteria | Points Available |
|------|----------|-----------------|
| Essential | C-01 through C-05 (5 criteria) | 50 pts |
| Recommended | C-06 through C-08 (3 criteria) | 30 pts |
| Aspirational | C-09 through C-13 (5 criteria) | 50 pts |
| **Total** | | **130 pts** |

**Scoring per criterion**: PASS = 10 pts, PARTIAL = 5 pts, FAIL = 0 pts.

**Golden**: all 5 essentials pass AND composite >= 80 pts.

| Score | Breakdown | Result |
|-------|-----------|--------|
| 130 / 130 | 5E + 3R + 5A all PASS | Perfect |
| 100 / 130 | 5E + 3R + 2A PASS | Golden |
| 80 / 130 | 5E + 3R + 0A PASS | Golden (threshold) |
| 70 / 130 | 5E + 2R + 0A PASS | Below threshold — not golden |
| any | 4E or fewer PASS | Disqualified (essential failure) |

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-17 | Initial rubric — 10 criteria, 100 pts max |
| v2 | 2026-03-17 | Added C-11 (typed inventory table), C-12 (rationale cites specific named signal), C-13 (hard ordering gate) from R1 excellence signals. Corrected score table: aspirationals are 10 pts each, not 5 pts. Max score now 130 pts. |
