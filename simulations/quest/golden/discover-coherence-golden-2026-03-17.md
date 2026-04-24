Written to `simulations/quest/golden/discover-coherence-golden-2026-03-17.md`.

**Summary:**

- **Prompt body**: V-05 simplified (423 words, 20% reduction from 529, all 17 criteria intact)
- **Score**: 130/130 — GOLDEN
- **5 patterns that made it golden**:
  1. **Two-phase scan** — STEP 2 fully silent; tally emitted in STEP 3 before any table row (closes C-15 + C-06 architecturally, not just by template)
  2. **Dual-table inertia-first + empty render** — topic-based priority (not severity-based); V-02's "Blocking first" variant proved the inertia label is structurally required
  3. **Severity-split resolution with `/skill-name` token** — BLOCKING = machine-parseable token; ADVISORY = concrete prose + explicit "not investigate further" prohibition (closes C-10 + C-12 + C-16 in one block)
  4. **Named gate `GATE FAILED`** — named token + count + directive; a prose stop can be silently dropped, a named token cannot
  5. **Merged VERDICT + ARTIFACT** — 6 phases → 5 steps with no criterion loss; R4 confirmed EXTRACT CLAIMS was scaffolding overhead, not a functional requirement
ll B + exact claim
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

---

## What Made It Golden

Five structural patterns distinguish V-05 from the baseline and close all 17 criteria:

**1. Two-phase scan (C-15 + C-06)**
STEP 2 is entirely silent — no output emitted. STEP 3 emits the tally header only after
all contradictions are counted. This architectural separation makes C-06 (tally before
first entry) structurally guaranteed in streaming output. A single-pass template that
places the tally "at the top" can still emit partial rows mid-stream; two-phase cannot.

**2. Dual-table with inertia-first + empty-render rule (C-13 + C-14)**
The inertia flag is set during the silent scan, not during output. Two Markdown tables
with named columns enforce C-14. Rendering the inertia table first — even when empty —
enforces C-13. V-02's "Blocking Contradictions first" alternative failed C-13: advisory
inertia contradictions would land in the second table, violating the topic-based
(not severity-based) priority requirement.

**3. Severity-split resolution with token syntax (C-16 + C-10 + C-12)**
BLOCKING resolutions require the exact `/skill-name [--focus param]` token — making them
machine-parseable and directly runnable. ADVISORY resolutions use concrete prose with
a named example. Both sections explicitly prohibit "investigate further" by name. This
closes C-10, C-12, and C-16 simultaneously in a single resolution block.

**4. Named gate with explicit failure message (C-11)**
The gate emits `GATE FAILED: {N} signal(s) found, need 2+.` — a named token with count
and directive. A prose stop condition ("if fewer than 2, stop") can be omitted by any
variation that skips the guard; the named token is structurally unmistakable.

**5. Merged VERDICT + ARTIFACT step (leanest 130-scoring structure)**
STEP 5 combines the readiness verdict and the artifact write into a single step, reducing
V-01's 6-phase structure to 5 steps. R4 confirmed this is lossless: the EXTRACT CLAIMS
sub-phase in earlier variations was scaffolding overhead, not a functional requirement.
No criterion required the separation — removing it reduces word count without removing
any structural guarantee.

---

## Rubric Criteria Summary (v3 — 130 pts)

### Essential (60 pts — all must pass)

| ID | Criterion | Pts | Enforced by |
|----|-----------|-----|-------------|
| C-01 | Gate check -- 2+ distinct skills required | 12 | STEP 1 GATE block with stop directive |
| C-02 | Side-by-side quotes -- specific claim in its own words | 12 | Claim A / Claim B column rule |
| C-03 | Type taxonomy -- exactly 3 values, no others | 12 | `rating-conflict \| prediction-conflict \| evidence-conflict -- no other values` |
| C-04 | Severity classification -- blocking or advisory only | 12 | `blocking \| advisory -- no other values` |
| C-05 | Cross-skill comparison | 12 | Cross-skill rule: Skill A and Skill B must be different discover skills |

### Recommended (30 pts)

| ID | Criterion | Pts | Enforced by |
|----|-----------|-----|-------------|
| C-06 | Tally before first entry | 10 | STEP 3 TALLY HEADER precedes STEP 4 tables |
| C-07 | Ready-to-specify verdict | 10 | M=0 / M>=1 branches in STEP 5 |
| C-08 | Evidence citations in contradiction entries | 10 | Skill A (date) / Skill B (date) named columns |

### Aspirational (40 pts)

| ID | Criterion | Pts | Enforced by |
|----|-----------|-----|-------------|
| C-09 | Contradiction taxonomy -- 3-value type column | 5 | Type column exact-values rule |
| C-10 | Skill reference per blocking contradiction | 5 | BLOCKING token format in Resolution block |
| C-11 | Named gate with explicit failure message | 5 | `GATE FAILED: {N} signal(s) found, need 2+.` |
| C-12 | Failure-mode negation in resolution instruction | 5 | `Not acceptable: "investigate further"` in ADVISORY block |
| C-13 | Inertia-first table rendering (topic-based, not severity-based) | 5 | Inertia table + inertia flag in STEP 2 scan; renders even if empty |
| C-14 | Table-format output with named columns | 5 | Two Markdown tables with `# / Type / Severity / Skill A / Claim A / Skill B / Claim B / Resolution` |
| C-15 | Two-phase scan structure | 5 | STEP 2 silent -> STEP 3 tally header |
| C-16 | Severity-split resolution with token syntax | 5 | BLOCKING `/skill-name` token + ADVISORY concrete prose, split by severity |

**Total**: 130 / 130 -- GOLDEN
