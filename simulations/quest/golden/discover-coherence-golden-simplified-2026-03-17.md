You are running /discover-coherence for topic: {topic}.

--- STEP 1: INVENTORY ---

Scan for all discover artifacts:
- Glob: simulations/discover/**/{topic}-*-*.md
- Glob: simulations/scout/**/{topic}-*-*.md

Print the inventory:
| Skill | Date | Path |
|-------|------|------|

If fewer than 2 rows from 2 distinct skills:
  "GATE FAILED: {N} signal(s) found, need 2+. Run discover skills before coherence check."
Stop.

--- STEP 2: SILENT SCAN ---

Read every file. For each factor carrying a rating (HIGH/MEDIUM/LOW), prediction ("likely",
"unlikely", "expected to"), or scored finding, compare claims across skills.

For each factor where 2+ skills disagree, record:
  Factor; Skill A + exact claim; Skill B + exact claim
  Type:     rating-conflict | prediction-conflict | evidence-conflict
  Severity: blocking (cannot both be true; decision depends on which is right)
             advisory (tension worth noting; does not block specifying)
  Inertia:  does this factor touch inertia, switching cost, workaround quality, or
    adoption prediction? Inertia contradictions render first regardless of count.

Do not emit any output. Count N total, M blocking, K advisory; R/P/E by type.

--- STEP 3: TALLY HEADER (output before any table) ---

---
COHERENCE FINDINGS: {N} contradiction(s) -- {M} blocking, {K} advisory
By type: {R} rating-conflict, {P} prediction-conflict, {E} evidence-conflict
Signals compared: {skill-1}, {skill-2}, ... ({total} signals)
---

--- STEP 4: TABLES ---

Two tables. Inertia table renders first, even if empty.

**Inertia Contradictions** (inertia / switching-cost / workaround-quality / adoption)

| # | Type | Severity | Skill A (date) | Claim A | Skill B (date) | Claim B | Resolution |
|---|------|----------|----------------|---------|----------------|---------|------------|

**Other Contradictions**

| # | Type | Severity | Skill A (date) | Claim A | Skill B (date) | Claim B | Resolution |
|---|------|----------|----------------|---------|----------------|---------|------------|

  Type: `rating-conflict` | `prediction-conflict` | `evidence-conflict` -- no other values

  Severity: `blocking` | `advisory` -- no other values

  Claim A / Claim B: the specific conflicting statement in its own words

  Resolution:
    BLOCKING -- required token format:
      "Resolve with: /{skill-name} [--focus {parameter}]"
      Wrong: "Run discover-inertia to check switching cost" (no slash token)

    ADVISORY -- concrete prose action:
      Name a field to update, claim to amend, or skill to run.
      Example:  "Update discover-competitors inertia threat rating from MEDIUM to HIGH."
      Not acceptable: "investigate further"

  Cross-skill: Skill A and Skill B must be different discover skills.

--- STEP 5: VERDICT + ARTIFACT ---

Summary: "Compared: {skill list} ({total} signals). Inertia: {A} ({B} blocking).
Other: {C} ({D} blocking). Total blocking: {B+D}. Total advisory: {remaining}."

Readiness:
  M = 0   -> "Ready to specify."
  M >= 1  -> "Not ready to specify -- {M} blocking contradiction(s) must be resolved."

Write to simulations/discover/coherence/{topic}-coherence-{date}.md
Frontmatter:
  topic: {topic}
  date: {date}
  signals_compared: [{skill-1}, {skill-2}, ...]
  inertia_blocking: {N}
  inertia_advisory: {N}
  other_blocking: {N}
  other_advisory: {N}
  verdict: ready | not-ready
