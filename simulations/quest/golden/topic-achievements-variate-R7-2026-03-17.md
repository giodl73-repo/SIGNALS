---
skill: quest-variate
skill_target: topic-achievements
round: 7
date: 2026-03-17
rubric_version: 7
basis: R6 V-05 (Golden Synthesis) passes C-01 through C-21 under the v6 rubric and appears to
       satisfy C-22 (gate registry table at preamble) and C-23 (FAIL conditions per gate) as
       patterns. Under v7, both are formalized as aspirational criteria with the scoring formula
       updated to aspirational_pass/15×10. Re-evaluating R6 V-05 against v7: the registry
       satisfies C-22 structurally (all schemas co-located before Phase 1), and FAIL blocks per
       gate satisfy C-23 (bi-directional contracts). However, R6 V-05 has two properties that v7
       now sharply distinguishes: (1) registry schemas are compressed/abbreviated inline in the
       table cell — the full schema is only fully expressed in per-phase prefaces; (2) the registry
       has no explicit primacy declaration — per-phase prefaces are parallel sources of truth, not
       subordinate to the registry. C-22 requires the full gate contract to be "discoverable by
       inspection before executing any phase" — abbreviated schemas that require cross-referencing
       per-phase text to be fully understood may not fully satisfy this. R7 isolates three new axes:
       (1) lifecycle emphasis — registry full-schema expansion (registry rows contain complete
       multi-line schemas, not abbreviations, so the registry alone is self-sufficient for C-22
       inspection); (2) output format — registry primacy declaration (an explicit contractual
       statement that the registry is the sole authoritative schema source, not one of several
       parallel sources); (3) phrasing register — severity-stratified FAIL blocks (FAIL modes
       organized into three tiers: Tier 1 structural, Tier 2 completeness, Tier 3 semantic bypass
       — making the semantic bypass case, the hardest to detect, explicitly visible as the most
       important FAIL mode for C-23). All R6 V-05 baseline wins are preserved: C-01 through C-19,
       session invariants A-D, pre-printed Falsified row, pre-printed LOCKED cell text, pre-printed
       table skeleton, CLASSIFY before STATE, all 4 phases gated, FAIL conditions per gate.
---

# Variate R7 — topic-achievements

5 complete prompt body variations for the `topic-achievements` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

---

## Variation Axes Selected

| Axis | Targets | Used In |
|------|---------|---------|
| Lifecycle emphasis (registry full-schema expansion — complete schemas in registry, no abbreviation) | C-22 | V-01, V-04, V-05 |
| Output format (registry primacy declaration — explicit contractual statement of sole authority) | C-22 | V-02, V-04, V-05 |
| Phrasing register (severity-stratified FAIL blocks — Tier 1/2/3 taxonomy) | C-23 | V-03, V-04, V-05 |

---

## V-01 — Lifecycle Emphasis: Registry Full-Schema Expansion

**Axis**: Lifecycle emphasis
**Hypothesis**: R6 registry table rows compress gate schemas into abbreviated inline text — the
CLASSIFY row spans a single cell that lists 7 category lines and a summary in shorthand. To read
the complete schema, the model must cross-reference per-phase preface blocks. C-22 requires the
full gate contract to be "discoverable by inspection before executing any phase" — if the registry
itself is incomplete (abbreviated), the inspection property is only partial. V-01 expands the
registry: each gate row contains a complete, multi-line schema block, fully specifiable without
consulting phase instructions. Per-phase prefaces reference back to the registry ("schema declared
in registry above") rather than re-stating schemas independently. The registry becomes a stand-alone
reference document, satisfying C-22 in the strongest possible form. FAIL conditions from R6 V-05
are preserved per phase.

---

You are running `topic-achievements` for topic: `{{topic}}`.

**Session invariants — apply throughout all phases:**

Invariant A (State): Each achievement row carries exactly one state: EARNED, IN-PROGRESS,
or LOCKED. No other values. No combined states.

Invariant B (Floor): Namespace-level evidence from the `prove` namespace is always
acceptable and is the safe floor for the Falsified achievement. Any prove artifact
containing a counter-signal or hypothesis revision qualifies Falsified for IN-PROGRESS.
No full synthesis required.

Invariant C (Citation): EARNED rows cite filename and date. IN-PROGRESS rows use `n of m`.
LOCKED rows name the exact artifact type or count required.

Invariant D (Preservation): The achievement table template in Phase 3 contains pre-printed
compliance text — in the Falsified row and in LOCKED cell detail. Do not rewrite, rephrase,
or restructure that pre-printed text. Fill only the placeholders as instructed.

---

**Gate Registry** — complete schemas for all 4 gates declared before Phase 1 begins.
Each schema below is the full required output. A phase is not complete until its gate
schema output is produced exactly as shown here.

**SCAN GATE** (Phase 1):
```
SCAN GATE CLEARED
Artifacts: [n]
Floor: active — Invariant B applies
```

**CLASSIFY GATE** (Phase 2):
```
CLASSIFY GATE CLEARED
Exploration: [list of qualifying artifact filenames, or "none"]
Depth: [n] artifacts
Coverage: [namespace prefixes list] — [n] of 9
Quality (Falsified candidates): [list of qualifying artifact filenames, or "none"]
Chain: hypothesis [present/absent] — evidence [present/absent] — synthesize [present/absent]
Discovery: [list of qualifying artifact filenames, or "none"]
Corps/Crew: contributors [list or "none"] — count [n]
[n] of 7 categories populated. Proceeding to template fill.
```

**STATE GATE** (Phase 3):
```
STATE GATE CLEARED
EARNED: [n]
IN-PROGRESS: [n]
LOCKED: [n]
All 7 rows filled. Invariants A–D applied.
```

**WRITE GATE** (Phase 4):
```
WRITE GATE CLEARED
Artifact path: simulations/topic/achievements/{{topic}}-achievements-{{date}}.md
Phases completed: 4
```

Phases must be completed in order. Entry condition for Phase N is the gate output of Phase N-1.

---

### PHASE 1 — SCAN GATE

Gate schema declared in registry above.

Glob `simulations/**/{{topic}}-*.md`. For each artifact, extract:
- Filename
- Skill (from `skill:` frontmatter or filename)
- Namespace prefix (first segment of skill name)
- Date (from `date:` frontmatter or filename)
- Contributor (`contributor:` or `author:` frontmatter, or "not set")

Produce the SCAN GATE schema from the registry.

FAIL — does not clear SCAN GATE:
- Missing "SCAN GATE CLEARED" label
- Missing artifact count line
- Missing floor confirmation line
- Count and listed artifacts inconsistent

If n = 0: produce gate output with n=0. All STATE cells will be LOCKED in Phase 3. Proceed.

---

### PHASE 2 — CLASSIFY GATE

Entry condition: SCAN GATE output produced.

Gate schema declared in registry above.

Assign each artifact from Phase 1 to exactly one category. Do not assign states.

| Category | Qualifying Skills |
|----------|------------------|
| Exploration | scout-*, topic-new, prove-hypothesis |
| Depth | All artifacts — count total; 5+ earns Signal Depth |
| Coverage | All artifacts — track unique namespace prefixes; 5+ of 9 earns Namespace Sweep |
| Quality | prove-synthesize or topic-echo containing a hypothesis revision |
| Chain | prove-hypothesis + (prove-websearch or prove-intelligence) + prove-synthesize |
| Discovery | topic-echo |
| Corps/Crew | 2+ distinct contributor values |

Produce the CLASSIFY GATE schema from the registry. All 7 labeled category lines and the
summary count line are required exactly as shown in the registry.

FAIL — does not clear CLASSIFY GATE:
- Summary count only ("3 of 7 categories populated") without the 7 labeled category lines
- Any of the 7 category lines missing (even if the result is "none")
- State assignments present (this phase classifies only — no state assignment here)
- Gate label present but category lines absent or partial
- Output matches a subset of the registry schema

---

### PHASE 3 — FILL TEMPLATE (STATE GATE)

Entry condition: CLASSIFY GATE output produced.

Gate schema declared in registry above.

Fill every `[PLACEHOLDER]` in the template below. Rules:
- Apply Invariant D: do not rewrite any pre-printed text.
- Do not reorder rows. Do not add or remove rows.
- Apply Invariants A, B, C to every row.
- EARNED: fill `[EARNED_ARTIFACT]` with `filename — date`.
- IN-PROGRESS: fill `[N]` and `[M]` with actual counts. No qualitative-only descriptions.
- LOCKED: the detail text is pre-printed. Fill only `[SPECIFIC_GAP]`.

```markdown
## topic-achievements — {{topic}}
_Scanned: {{date}} — Total artifacts: [TOTAL_COUNT]_

| Category | Achievement | State | Detail |
|----------|-------------|-------|--------|
| Exploration | Spark | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [EARNED_ARTIFACT] / IN-PROGRESS: [N] of 1 artifact / LOCKED: File any one artifact for topic `{{topic}}` using any Signal skill |
| Depth | Signal Depth | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [N] artifacts — earliest [EARNED_ARTIFACT] / IN-PROGRESS: [N] of 5 artifacts / LOCKED: File 5 total artifacts for topic `{{topic}}` across any Signal skills |
| Coverage | Namespace Sweep | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [N] of 9 namespaces — [LIST_NAMESPACES] / IN-PROGRESS: [N] of 5 namespaces — missing: [LIST_MISSING] / LOCKED: File artifacts from 5 of the 9 namespaces (scout, draft, review, flow, trace, prove, listen, program, topic) |
| Quality | Falsified | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [EARNED_ARTIFACT] — followed evidence over assumptions: [REVISION_EVENT] / IN-PROGRESS: [N] of [M] prove artifacts contain counter-signals — not yet synthesized / LOCKED: File a prove-synthesize or topic-echo artifact that records a hypothesis revision. Framing falsification as absence or as a result the investigation did not yield — including as a closing reflection — does not earn this achievement. Namespace-level evidence from the prove namespace is always acceptable and is the safe floor. |
| Chain | Hypothesis Chain | [EARNED / IN-PROGRESS / LOCKED] | EARNED: prove-hypothesis [DATE1] → prove-evidence [DATE2] → prove-synthesize [DATE3] / IN-PROGRESS: [N] of 3 chain links — missing: [LIST_MISSING_LINKS] / LOCKED: File prove-hypothesis, then prove-websearch or prove-intelligence, then prove-synthesize — in that order |
| Discovery | Echo Filed | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [EARNED_ARTIFACT] / IN-PROGRESS: topic-echo started but not finalized / LOCKED: Run /topic-echo to produce `{{topic}}-echo-{{date}}.md` |
| Corps/Crew | Team Contribution | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [N] contributors — [LIST_CONTRIBUTORS] — first joint artifact: [DATE] / IN-PROGRESS: [N] of 2 contributors active — second contributor needed / LOCKED: A second team member files any artifact for topic `{{topic}}` |

## Next Action

Run `/[SKILL]` to produce `{{topic}}-[ITEM]-{{date}}.md`.
This advances [CATEGORY: ACHIEVEMENT] from [CURRENT_STATE] toward [TARGET_STATE].
Why: [SPECIFIC_GAP — one sentence linking to the CLASSIFY GATE output].
```

Produce the STATE GATE schema from the registry.

FAIL — does not clear STATE GATE:
- Numeric counts absent (n EARNED, n IN-PROGRESS, n LOCKED all required)
- Counts do not sum to 7
- "All 7 rows filled" confirmation absent
- Gate label present but state counts absent

---

### PHASE 4 — WRITE GATE

Entry condition: STATE GATE output produced.

Gate schema declared in registry above.

Write the filled template to:
`simulations/topic/achievements/{{topic}}-achievements-{{date}}.md`

```yaml
---
skill: topic-achievements
topic: {{topic}}
date: {{date}}
artifacts_scanned: [TOTAL_COUNT]
phases_completed: 4
earned: [n from STATE GATE]
in_progress: [n from STATE GATE]
locked: [n from STATE GATE]
---
```

Produce the WRITE GATE schema from the registry.

FAIL — does not clear WRITE GATE:
- "WRITE GATE CLEARED" label absent
- Artifact path absent
- Path contains wrong topic or wrong date
- Gate label present but path absent

---

## V-02 — Output Format: Registry Primacy Declaration

**Axis**: Output format
**Hypothesis**: R6 V-05's registry table and per-phase prefaces are parallel sources of truth —
both declare schemas, and neither is explicitly authoritative over the other. A model that
reads a per-phase preface gets a complete schema without consulting the registry. This means
the registry is co-located (satisfying C-22 structurally) but not contractually authoritative.
V-02 adds a REGISTRY PRIMACY declaration: an explicit statement that the registry is the sole
authoritative contract and per-phase instructions implement the registry, they do not redefine
it. If a gate output matches the registry schema, the gate is cleared. Per-phase prefaces
are preserved as goal-state immediacy (goal-state benefit for C-20 satisfaction) but are
explicitly subordinated to the registry. This makes C-22's co-location property not just
structural (everything is in one place) but contractual (the one place is the binding source).
The implication for C-23: FAIL conditions per phase still apply, but their authority derives
from the registry contracts, not from the phase itself. R6 V-05 baseline wins preserved.

---

You are running `topic-achievements` for topic: `{{topic}}`.

**Session invariants — apply throughout all phases:**

Invariant A (State): Each achievement row carries exactly one state: EARNED, IN-PROGRESS,
or LOCKED. No other values. No combined states.

Invariant B (Floor): Namespace-level evidence from the `prove` namespace is always
acceptable and is the safe floor for the Falsified achievement. Any prove artifact
containing a counter-signal or hypothesis revision qualifies Falsified for IN-PROGRESS.
No full synthesis required.

Invariant C (Citation): EARNED rows cite filename and date. IN-PROGRESS rows use `n of m`.
LOCKED rows name the exact artifact type or count required.

Invariant D (Preservation): The achievement table template in Phase 3 contains pre-printed
compliance text — in the Falsified row and in LOCKED cell detail. Do not rewrite, rephrase,
or restructure that pre-printed text. Fill only the placeholders as instructed.

---

**Gate Registry** — all 4 phase gates and their required output schemas.

**REGISTRY PRIMACY**: The schemas in this registry are the sole authoritative gate contracts.
Phase instructions implement these contracts — they do not redefine them. A gate output that
matches the schema declared here clears the gate, regardless of any phase-level description.
A gate output that does not match the schema declared here does not clear the gate, regardless
of any phase-level elaboration. Read the registry before beginning Phase 1.

| Phase | Gate | Required output schema |
|-------|------|----------------------|
| 1 — SCAN | SCAN GATE | `SCAN GATE CLEARED` / `Artifacts: [n]` / `Floor: active — Invariant B applies` |
| 2 — CLASSIFY | CLASSIFY GATE | `CLASSIFY GATE CLEARED` / `Exploration: [list or "none"]` / `Depth: [n] artifacts` / `Coverage: [namespaces] — [n] of 9` / `Quality (Falsified candidates): [list or "none"]` / `Chain: hypothesis [p/a] — evidence [p/a] — synthesize [p/a]` / `Discovery: [list or "none"]` / `Corps/Crew: contributors [list] — count [n]` / `[n] of 7 categories populated. Proceeding to template fill.` |
| 3 — FILL | STATE GATE | `STATE GATE CLEARED` / `EARNED: [n]` / `IN-PROGRESS: [n]` / `LOCKED: [n]` / `All 7 rows filled. Invariants A–D applied.` |
| 4 — WRITE | WRITE GATE | `WRITE GATE CLEARED` / `Artifact path: simulations/topic/achievements/{{topic}}-achievements-{{date}}.md` / `Phases completed: 4` |

Phases must be completed in order. Entry condition for Phase N is the gate output of Phase N-1.

---

### PHASE 1 — SCAN GATE

**SCAN GATE schema** (goal state — produce this before Phase 2):
```
SCAN GATE CLEARED
Artifacts: [n]
Floor: active — Invariant B applies
```
*Authority: registry above. This preface restates the registry schema for immediacy.*

Glob `simulations/**/{{topic}}-*.md`. For each artifact, extract:
- Filename
- Skill (from `skill:` frontmatter or filename)
- Namespace prefix (first segment of skill name)
- Date (from `date:` frontmatter or filename)
- Contributor (`contributor:` or `author:` frontmatter, or "not set")

Produce the SCAN GATE schema.

FAIL — does not clear SCAN GATE (authority: registry primacy):
- Missing "SCAN GATE CLEARED" label
- Missing artifact count line
- Missing floor confirmation line
- Count and artifact list inconsistent

If n = 0: produce gate output with n=0. All STATE cells will be LOCKED in Phase 3. Proceed.

---

### PHASE 2 — CLASSIFY GATE

Entry condition: SCAN GATE output produced.

**CLASSIFY GATE schema** (goal state — produce this before Phase 3):
```
CLASSIFY GATE CLEARED
Exploration: [list or "none"]
Depth: [n] artifacts
Coverage: [namespaces list] — [n] of 9
Quality (Falsified candidates): [list or "none"]
Chain: hypothesis [present/absent] — evidence [present/absent] — synthesize [present/absent]
Discovery: [list or "none"]
Corps/Crew: contributors [list or "none"] — count [n]
[n] of 7 categories populated. Proceeding to template fill.
```
*Authority: registry above. This preface restates the registry schema for immediacy.*

Assign each artifact from Phase 1 to exactly one category. Do not assign states.

| Category | Qualifying Skills |
|----------|------------------|
| Exploration | scout-*, topic-new, prove-hypothesis |
| Depth | All artifacts — count total; 5+ earns Signal Depth |
| Coverage | All artifacts — track unique namespace prefixes; 5+ of 9 earns Namespace Sweep |
| Quality | prove-synthesize or topic-echo containing a hypothesis revision |
| Chain | prove-hypothesis + (prove-websearch or prove-intelligence) + prove-synthesize |
| Discovery | topic-echo |
| Corps/Crew | 2+ distinct contributor values |

Produce the CLASSIFY GATE schema.

FAIL — does not clear CLASSIFY GATE (authority: registry primacy):
- Summary count only without the 7 labeled category lines
- Any category line missing (even if "none")
- State assignments present (classify does not assign states)
- Gate label present but category lines absent or partial

---

### PHASE 3 — FILL TEMPLATE (STATE GATE)

Entry condition: CLASSIFY GATE output produced.

**STATE GATE schema** (goal state — produce this before Phase 4):
```
STATE GATE CLEARED
EARNED: [n]
IN-PROGRESS: [n]
LOCKED: [n]
All 7 rows filled. Invariants A–D applied.
```
*Authority: registry above. This preface restates the registry schema for immediacy.*

Fill every `[PLACEHOLDER]` in the template below. Rules:
- Apply Invariant D: do not rewrite any pre-printed text.
- Do not reorder rows. Do not add or remove rows.
- Apply Invariants A, B, C to every row.
- EARNED: fill `[EARNED_ARTIFACT]` with `filename — date`.
- IN-PROGRESS: fill `[N]` and `[M]` with actual counts.
- LOCKED: detail text is pre-printed; fill only `[SPECIFIC_GAP]`.

```markdown
## topic-achievements — {{topic}}
_Scanned: {{date}} — Total artifacts: [TOTAL_COUNT]_

| Category | Achievement | State | Detail |
|----------|-------------|-------|--------|
| Exploration | Spark | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [EARNED_ARTIFACT] / IN-PROGRESS: [N] of 1 artifact / LOCKED: File any one artifact for topic `{{topic}}` using any Signal skill |
| Depth | Signal Depth | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [N] artifacts — earliest [EARNED_ARTIFACT] / IN-PROGRESS: [N] of 5 artifacts / LOCKED: File 5 total artifacts for topic `{{topic}}` across any Signal skills |
| Coverage | Namespace Sweep | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [N] of 9 namespaces — [LIST_NAMESPACES] / IN-PROGRESS: [N] of 5 namespaces — missing: [LIST_MISSING] / LOCKED: File artifacts from 5 of the 9 namespaces (scout, draft, review, flow, trace, prove, listen, program, topic) |
| Quality | Falsified | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [EARNED_ARTIFACT] — followed evidence over assumptions: [REVISION_EVENT] / IN-PROGRESS: [N] of [M] prove artifacts contain counter-signals — not yet synthesized / LOCKED: File a prove-synthesize or topic-echo artifact that records a hypothesis revision. Framing falsification as absence or as a result the investigation did not yield — including as a closing reflection — does not earn this achievement. Namespace-level evidence from the prove namespace is always acceptable and is the safe floor. |
| Chain | Hypothesis Chain | [EARNED / IN-PROGRESS / LOCKED] | EARNED: prove-hypothesis [DATE1] → prove-evidence [DATE2] → prove-synthesize [DATE3] / IN-PROGRESS: [N] of 3 chain links — missing: [LIST_MISSING_LINKS] / LOCKED: File prove-hypothesis, then prove-websearch or prove-intelligence, then prove-synthesize — in that order |
| Discovery | Echo Filed | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [EARNED_ARTIFACT] / IN-PROGRESS: topic-echo started but not finalized / LOCKED: Run /topic-echo to produce `{{topic}}-echo-{{date}}.md` |
| Corps/Crew | Team Contribution | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [N] contributors — [LIST_CONTRIBUTORS] — first joint artifact: [DATE] / IN-PROGRESS: [N] of 2 contributors active — second contributor needed / LOCKED: A second team member files any artifact for topic `{{topic}}` |

## Next Action

Run `/[SKILL]` to produce `{{topic}}-[ITEM]-{{date}}.md`.
This advances [CATEGORY: ACHIEVEMENT] from [CURRENT_STATE] toward [TARGET_STATE].
Why: [SPECIFIC_GAP — one sentence linking to the CLASSIFY GATE output].
```

Produce the STATE GATE schema.

FAIL — does not clear STATE GATE (authority: registry primacy):
- Numeric counts absent
- Counts do not sum to 7
- "All 7 rows filled" confirmation absent
- Gate label present but state counts absent

---

### PHASE 4 — WRITE GATE

Entry condition: STATE GATE output produced.

**WRITE GATE schema** (goal state — produce this to complete):
```
WRITE GATE CLEARED
Artifact path: simulations/topic/achievements/{{topic}}-achievements-{{date}}.md
Phases completed: 4
```
*Authority: registry above.*

Write the filled template to:
`simulations/topic/achievements/{{topic}}-achievements-{{date}}.md`

```yaml
---
skill: topic-achievements
topic: {{topic}}
date: {{date}}
artifacts_scanned: [TOTAL_COUNT]
phases_completed: 4
earned: [n from STATE GATE]
in_progress: [n from STATE GATE]
locked: [n from STATE GATE]
---
```

Produce the WRITE GATE schema.

FAIL — does not clear WRITE GATE (authority: registry primacy):
- "WRITE GATE CLEARED" label absent
- Artifact path absent
- Path contains wrong topic or wrong date
- Gate label present but path absent

---

## V-03 — Phrasing Register: Severity-Stratified FAIL Blocks

**Axis**: Phrasing register
**Hypothesis**: R6 V-05's FAIL blocks list 3–5 failure modes as an unordered list. All failure
modes appear with equal weight. The most important failure mode for C-23 — semantic bypass, where
output matches the gate format but avoids the intent — is buried among structural failures (missing
label) and completeness failures (missing fields). A model that avoids obvious structural failures
might still commit a semantic bypass. V-03 restructures FAIL blocks into three severity tiers:
Tier 1 (Structural) — the gate label itself is missing; output cannot be interpreted as a gate
completion. Tier 2 (Completeness) — gate label present but required fields missing or wrong.
Tier 3 (Semantic bypass) — all required fields present and correctly formatted, but the output
bypasses the gate's intent without technically missing any field. Tier 3 is the failure mode
C-23 is designed to prevent — it is listed last but explicitly labeled as the most consequential.
A gate that lists only Tier 1 and Tier 2 failures is one-directional (positive pass, with named
failures); adding Tier 3 makes it two-sided in the deeper sense C-23 requires. R6 V-05 baseline
wins preserved. Registry format from R6 V-05 preserved.

---

You are running `topic-achievements` for topic: `{{topic}}`.

**Session invariants — apply throughout all phases:**

Invariant A (State): Each achievement row carries exactly one state: EARNED, IN-PROGRESS,
or LOCKED. No other values. No combined states.

Invariant B (Floor): Namespace-level evidence from the `prove` namespace is always
acceptable and is the safe floor for the Falsified achievement. Any prove artifact
containing a counter-signal or hypothesis revision qualifies Falsified for IN-PROGRESS.
No full synthesis required.

Invariant C (Citation): EARNED rows cite filename and date. IN-PROGRESS rows use `n of m`.
LOCKED rows name the exact artifact type or count required.

Invariant D (Preservation): The achievement table template in Phase 3 contains pre-printed
compliance text — in the Falsified row and in LOCKED cell detail. Do not rewrite, rephrase,
or restructure that pre-printed text. Fill only the placeholders as instructed.

---

**Gate Registry** — all 4 phases are gated. PASS schema for each, declared before Phase 1.

| Phase | Gate | PASS schema |
|-------|------|-------------|
| 1 — SCAN | SCAN GATE | `SCAN GATE CLEARED` / `Artifacts: [n]` / `Floor: active — Invariant B applies` |
| 2 — CLASSIFY | CLASSIFY GATE | `CLASSIFY GATE CLEARED` / `Exploration: [list or "none"]` / `Depth: [n] artifacts` / `Coverage: [namespaces] — [n] of 9` / `Quality (Falsified candidates): [list or "none"]` / `Chain: hypothesis [p/a] — evidence [p/a] — synthesize [p/a]` / `Discovery: [list or "none"]` / `Corps/Crew: contributors [list] — count [n]` / `[n] of 7 categories populated. Proceeding to template fill.` |
| 3 — FILL | STATE GATE | `STATE GATE CLEARED` / `EARNED: [n]` / `IN-PROGRESS: [n]` / `LOCKED: [n]` / `All 7 rows filled. Invariants A–D applied.` |
| 4 — WRITE | WRITE GATE | `WRITE GATE CLEARED` / `Artifact path: simulations/topic/achievements/{{topic}}-achievements-{{date}}.md` |

Phases must be completed in order. Entry condition for Phase N is the gate output of Phase N-1.

---

### PHASE 1 — SCAN GATE

**SCAN GATE schema** (preface — read before executing):
```
SCAN GATE CLEARED
Artifacts: [n]
Floor: active — Invariant B applies
```

Glob `simulations/**/{{topic}}-*.md`. For each artifact, extract:
- Filename
- Skill (from `skill:` frontmatter or filename)
- Namespace prefix (first segment of skill name)
- Date (from `date:` frontmatter or filename)
- Contributor (`contributor:` or `author:` frontmatter, or "not set")

Produce the SCAN GATE schema above.

**FAIL — severity-stratified:**

*Tier 1 (Structural — gate output uninterpretable):*
- "SCAN GATE CLEARED" label absent — output cannot be identified as a gate completion

*Tier 2 (Completeness — label present but fields missing):*
- Artifact count line absent
- Floor confirmation line absent

*Tier 3 (Semantic bypass — fields present but intent bypassed):*
- Count line present but count does not match the artifacts listed
- Floor line present but stated as "inactive" or "not applicable" when prove artifacts exist
  — Invariant B requires the floor to be active whenever any prove-namespace artifact exists;
  stating it inactive when artifacts are present bypasses the floor guarantee without
  technically omitting the line

If n = 0: produce gate output with n=0. All STATE cells will be LOCKED in Phase 3. Proceed.

---

### PHASE 2 — CLASSIFY GATE

Entry condition: SCAN GATE CLEARED output produced.

**CLASSIFY GATE schema** (preface — read before executing):
```
CLASSIFY GATE CLEARED
Exploration: [list or "none"]
Depth: [n] artifacts
Coverage: [namespaces list] — [n] of 9
Quality (Falsified candidates): [list or "none"]
Chain: hypothesis [present/absent] — evidence [present/absent] — synthesize [present/absent]
Discovery: [list or "none"]
Corps/Crew: contributors [list or "none"] — count [n]
[n] of 7 categories populated. Proceeding to template fill.
```

Assign each artifact from Phase 1 to exactly one category. Do not assign states.

| Category | Qualifying Skills |
|----------|------------------|
| Exploration | scout-*, topic-new, prove-hypothesis |
| Depth | All artifacts — count total; 5+ earns Signal Depth |
| Coverage | All artifacts — track unique namespace prefixes; 5+ of 9 earns Namespace Sweep |
| Quality | prove-synthesize or topic-echo containing a hypothesis revision |
| Chain | prove-hypothesis + (prove-websearch or prove-intelligence) + prove-synthesize |
| Discovery | topic-echo |
| Corps/Crew | 2+ distinct contributor values |

Produce the CLASSIFY GATE schema above.

**FAIL — severity-stratified:**

*Tier 1 (Structural — gate output uninterpretable):*
- "CLASSIFY GATE CLEARED" label absent — output cannot be identified as a gate completion

*Tier 2 (Completeness — label present but fields missing):*
- Any of the 7 labeled category lines absent (even if the category has no qualifying artifacts,
  the line must appear with "none")
- Summary count line absent

*Tier 3 (Semantic bypass — fields present but intent bypassed):*
- Summary count line present ("3 of 7 categories populated") without the 7 labeled category
  lines — count without enumeration satisfies the format of a summary but bypasses the
  enumeration requirement; any downstream phase that consumes this output cannot verify
  category-level accuracy
- State assignments embedded in category lines ("Exploration: artifact.md — EARNED") —
  this phase classifies, not assigns; state assignments in the CLASSIFY output contaminate
  Phase 3 state derivation with Phase 2 pre-judgments
- Artifacts from Phase 1 omitted from any category line without explanation — silent omission
  bypasses the exhaustive classification requirement even if each individual line is formatted
  correctly

---

### PHASE 3 — FILL TEMPLATE (STATE GATE)

Entry condition: CLASSIFY GATE CLEARED output produced.

**STATE GATE schema** (preface — read before executing):
```
STATE GATE CLEARED
EARNED: [n]
IN-PROGRESS: [n]
LOCKED: [n]
All 7 rows filled. Invariants A–D applied.
```

Fill every `[PLACEHOLDER]` in the template below. Rules:
- Apply Invariant D: do not rewrite any pre-printed text.
- Do not reorder rows. Do not add or remove rows.
- Apply Invariants A, B, C to every row.
- EARNED: fill `[EARNED_ARTIFACT]` with `filename — date`.
- IN-PROGRESS: fill `[N]` and `[M]` with actual counts. Qualitative-only descriptions fail.
- LOCKED: detail text is pre-printed; fill only `[SPECIFIC_GAP]`.

```markdown
## topic-achievements — {{topic}}
_Scanned: {{date}} — Total artifacts: [TOTAL_COUNT]_

| Category | Achievement | State | Detail |
|----------|-------------|-------|--------|
| Exploration | Spark | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [EARNED_ARTIFACT] / IN-PROGRESS: [N] of 1 artifact / LOCKED: File any one artifact for topic `{{topic}}` using any Signal skill |
| Depth | Signal Depth | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [N] artifacts — earliest [EARNED_ARTIFACT] / IN-PROGRESS: [N] of 5 artifacts / LOCKED: File 5 total artifacts for topic `{{topic}}` across any Signal skills |
| Coverage | Namespace Sweep | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [N] of 9 namespaces — [LIST_NAMESPACES] / IN-PROGRESS: [N] of 5 namespaces — missing: [LIST_MISSING] / LOCKED: File artifacts from 5 of the 9 namespaces (scout, draft, review, flow, trace, prove, listen, program, topic) |
| Quality | Falsified | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [EARNED_ARTIFACT] — followed evidence over assumptions: [REVISION_EVENT] / IN-PROGRESS: [N] of [M] prove artifacts contain counter-signals — not yet synthesized / LOCKED: File a prove-synthesize or topic-echo artifact that records a hypothesis revision. Framing falsification as absence or as a result the investigation did not yield — including as a closing reflection — does not earn this achievement. Namespace-level evidence from the prove namespace is always acceptable and is the safe floor. |
| Chain | Hypothesis Chain | [EARNED / IN-PROGRESS / LOCKED] | EARNED: prove-hypothesis [DATE1] → prove-evidence [DATE2] → prove-synthesize [DATE3] / IN-PROGRESS: [N] of 3 chain links — missing: [LIST_MISSING_LINKS] / LOCKED: File prove-hypothesis, then prove-websearch or prove-intelligence, then prove-synthesize — in that order |
| Discovery | Echo Filed | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [EARNED_ARTIFACT] / IN-PROGRESS: topic-echo started but not finalized / LOCKED: Run /topic-echo to produce `{{topic}}-echo-{{date}}.md` |
| Corps/Crew | Team Contribution | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [N] contributors — [LIST_CONTRIBUTORS] — first joint artifact: [DATE] / IN-PROGRESS: [N] of 2 contributors active — second contributor needed / LOCKED: A second team member files any artifact for topic `{{topic}}` |

## Next Action

Run `/[SKILL]` to produce `{{topic}}-[ITEM]-{{date}}.md`.
This advances [CATEGORY: ACHIEVEMENT] from [CURRENT_STATE] toward [TARGET_STATE].
Why: [SPECIFIC_GAP — one sentence linking to the CLASSIFY GATE output].
```

Produce the STATE GATE schema above.

**FAIL — severity-stratified:**

*Tier 1 (Structural — gate output uninterpretable):*
- "STATE GATE CLEARED" label absent

*Tier 2 (Completeness — label present but fields missing):*
- Any of the three numeric count lines absent (EARNED, IN-PROGRESS, LOCKED each required)
- "All 7 rows filled" confirmation absent

*Tier 3 (Semantic bypass — counts present but internally inconsistent):*
- EARNED + IN-PROGRESS + LOCKED counts do not sum to 7 — a count sum of ≠7 means at least
  one achievement row was omitted or double-counted, bypassing the completeness guarantee
  while producing apparently valid numeric output

---

### PHASE 4 — WRITE GATE

Entry condition: STATE GATE output produced.

**WRITE GATE schema** (preface — read before executing):
```
WRITE GATE CLEARED
Artifact path: simulations/topic/achievements/{{topic}}-achievements-{{date}}.md
```

Write the filled template to:
`simulations/topic/achievements/{{topic}}-achievements-{{date}}.md`

```yaml
---
skill: topic-achievements
topic: {{topic}}
date: {{date}}
artifacts_scanned: [TOTAL_COUNT]
phases_completed: 4
earned: [n from STATE GATE]
in_progress: [n from STATE GATE]
locked: [n from STATE GATE]
---
```

Produce the WRITE GATE schema above.

**FAIL — severity-stratified:**

*Tier 1 (Structural — gate output uninterpretable):*
- "WRITE GATE CLEARED" label absent

*Tier 2 (Completeness — label present but fields missing):*
- Artifact path absent

*Tier 3 (Semantic bypass — path present but incorrect):*
- Path contains wrong topic name — the artifact will be unreachable by topic-scanner
- Path contains wrong or missing date — the artifact will not be found by date-scoped queries

---

## V-04 — Combination: Registry Full-Schema Expansion + Registry Primacy Declaration

**Axes**: Lifecycle emphasis (full schema expansion in registry) + output format (registry
primacy declaration)
**Hypothesis**: V-01 makes the registry self-sufficient by expanding schemas to full multi-line
form, so C-22 inspection requires no cross-referencing. V-02 makes the registry contractually
authoritative so C-22 is not just structural but binding. V-04 combines: the registry contains
complete multi-line schemas (self-sufficient for inspection) AND is declared the sole authority
(binding, not advisory). Per-phase prefaces are preserved for goal-state immediacy but explicitly
labeled as restatements of registry authority, not independent schema sources. This closes the
remaining gap in C-22: not just "schemas co-located before Phase 1" but "complete, authoritative,
self-sufficient schemas co-located before Phase 1." FAIL conditions are preserved from R6 V-05
(not severity-stratified — that axis is reserved for V-05). R6 V-05 baseline wins preserved.

---

You are running `topic-achievements` for topic: `{{topic}}`.

**Session invariants — apply throughout all phases:**

Invariant A (State): Each achievement row carries exactly one state: EARNED, IN-PROGRESS,
or LOCKED. No other values. No combined states.

Invariant B (Floor): Namespace-level evidence from the `prove` namespace is always
acceptable and is the safe floor for the Falsified achievement. Any prove artifact
containing a counter-signal or hypothesis revision qualifies Falsified for IN-PROGRESS.
No full synthesis required.

Invariant C (Citation): EARNED rows cite filename and date. IN-PROGRESS rows use `n of m`.
LOCKED rows name the exact artifact type or count required.

Invariant D (Preservation): The achievement table template in Phase 3 contains pre-printed
compliance text — in the Falsified row and in LOCKED cell detail. Do not rewrite, rephrase,
or restructure that pre-printed text. Fill only the placeholders as instructed.

---

**Gate Registry** — complete, authoritative schemas for all 4 gates declared before Phase 1.

**REGISTRY PRIMACY**: These schemas are the sole authoritative gate contracts. Phase
instructions implement these contracts; they do not redefine them. A gate output that
matches a schema declared here clears that gate. A gate output that does not match a
schema declared here does not clear that gate. Read and retain these schemas before Phase 1.

**SCAN GATE** (Phase 1) — complete schema:
```
SCAN GATE CLEARED
Artifacts: [n]
Floor: active — Invariant B applies
```

**CLASSIFY GATE** (Phase 2) — complete schema:
```
CLASSIFY GATE CLEARED
Exploration: [list of qualifying artifact filenames, or "none"]
Depth: [n] artifacts
Coverage: [namespace prefixes list] — [n] of 9
Quality (Falsified candidates): [list of qualifying artifact filenames, or "none"]
Chain: hypothesis [present/absent] — evidence [present/absent] — synthesize [present/absent]
Discovery: [list of qualifying artifact filenames, or "none"]
Corps/Crew: contributors [list or "none"] — count [n]
[n] of 7 categories populated. Proceeding to template fill.
```

**STATE GATE** (Phase 3) — complete schema:
```
STATE GATE CLEARED
EARNED: [n]
IN-PROGRESS: [n]
LOCKED: [n]
All 7 rows filled. Invariants A–D applied.
```

**WRITE GATE** (Phase 4) — complete schema:
```
WRITE GATE CLEARED
Artifact path: simulations/topic/achievements/{{topic}}-achievements-{{date}}.md
Phases completed: 4
```

Phases must be completed in order. Entry condition for Phase N is the gate output of Phase N-1.

---

### PHASE 1 — SCAN GATE

**SCAN GATE schema** (preface — restatement of registry authority; read before executing):
```
SCAN GATE CLEARED
Artifacts: [n]
Floor: active — Invariant B applies
```

Glob `simulations/**/{{topic}}-*.md`. For each artifact, extract:
- Filename
- Skill (from `skill:` frontmatter or filename)
- Namespace prefix (first segment of skill name)
- Date (from `date:` frontmatter or filename)
- Contributor (`contributor:` or `author:` frontmatter, or "not set")

Produce the SCAN GATE schema. Authority: registry.

FAIL — does not clear SCAN GATE:
- "SCAN GATE CLEARED" label absent
- Artifact count line absent
- Floor confirmation line absent
- Count and artifact list inconsistent

If n = 0: produce gate output with n=0. All STATE cells will be LOCKED in Phase 3. Proceed.

---

### PHASE 2 — CLASSIFY GATE

Entry condition: SCAN GATE output produced.

**CLASSIFY GATE schema** (preface — restatement of registry authority; read before executing):
```
CLASSIFY GATE CLEARED
Exploration: [list or "none"]
Depth: [n] artifacts
Coverage: [namespaces list] — [n] of 9
Quality (Falsified candidates): [list or "none"]
Chain: hypothesis [present/absent] — evidence [present/absent] — synthesize [present/absent]
Discovery: [list or "none"]
Corps/Crew: contributors [list or "none"] — count [n]
[n] of 7 categories populated. Proceeding to template fill.
```

Assign each artifact from Phase 1 to exactly one category. Do not assign states.

| Category | Qualifying Skills |
|----------|------------------|
| Exploration | scout-*, topic-new, prove-hypothesis |
| Depth | All artifacts — count total; 5+ earns Signal Depth |
| Coverage | All artifacts — track unique namespace prefixes; 5+ of 9 earns Namespace Sweep |
| Quality | prove-synthesize or topic-echo containing a hypothesis revision |
| Chain | prove-hypothesis + (prove-websearch or prove-intelligence) + prove-synthesize |
| Discovery | topic-echo |
| Corps/Crew | 2+ distinct contributor values |

Produce the CLASSIFY GATE schema. Authority: registry.

FAIL — does not clear CLASSIFY GATE:
- Summary count only without the 7 labeled category lines
- Any category line missing (even if "none")
- State assignments present (classify does not assign states)
- Gate label present but category lines absent or partial

---

### PHASE 3 — FILL TEMPLATE (STATE GATE)

Entry condition: CLASSIFY GATE output produced.

**STATE GATE schema** (preface — restatement of registry authority; read before executing):
```
STATE GATE CLEARED
EARNED: [n]
IN-PROGRESS: [n]
LOCKED: [n]
All 7 rows filled. Invariants A–D applied.
```

Fill every `[PLACEHOLDER]` in the template below. Rules:
- Apply Invariant D: do not rewrite any pre-printed text.
- Do not reorder rows. Do not add or remove rows.
- Apply Invariants A, B, C to every row.
- EARNED: fill `[EARNED_ARTIFACT]` with `filename — date`.
- IN-PROGRESS: fill `[N]` and `[M]` with actual counts.
- LOCKED: detail text is pre-printed; fill only `[SPECIFIC_GAP]`.

```markdown
## topic-achievements — {{topic}}
_Scanned: {{date}} — Total artifacts: [TOTAL_COUNT]_

| Category | Achievement | State | Detail |
|----------|-------------|-------|--------|
| Exploration | Spark | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [EARNED_ARTIFACT] / IN-PROGRESS: [N] of 1 artifact / LOCKED: File any one artifact for topic `{{topic}}` using any Signal skill |
| Depth | Signal Depth | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [N] artifacts — earliest [EARNED_ARTIFACT] / IN-PROGRESS: [N] of 5 artifacts / LOCKED: File 5 total artifacts for topic `{{topic}}` across any Signal skills |
| Coverage | Namespace Sweep | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [N] of 9 namespaces — [LIST_NAMESPACES] / IN-PROGRESS: [N] of 5 namespaces — missing: [LIST_MISSING] / LOCKED: File artifacts from 5 of the 9 namespaces (scout, draft, review, flow, trace, prove, listen, program, topic) |
| Quality | Falsified | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [EARNED_ARTIFACT] — followed evidence over assumptions: [REVISION_EVENT] / IN-PROGRESS: [N] of [M] prove artifacts contain counter-signals — not yet synthesized / LOCKED: File a prove-synthesize or topic-echo artifact that records a hypothesis revision. Framing falsification as absence or as a result the investigation did not yield — including as a closing reflection — does not earn this achievement. Namespace-level evidence from the prove namespace is always acceptable and is the safe floor. |
| Chain | Hypothesis Chain | [EARNED / IN-PROGRESS / LOCKED] | EARNED: prove-hypothesis [DATE1] → prove-evidence [DATE2] → prove-synthesize [DATE3] / IN-PROGRESS: [N] of 3 chain links — missing: [LIST_MISSING_LINKS] / LOCKED: File prove-hypothesis, then prove-websearch or prove-intelligence, then prove-synthesize — in that order |
| Discovery | Echo Filed | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [EARNED_ARTIFACT] / IN-PROGRESS: topic-echo started but not finalized / LOCKED: Run /topic-echo to produce `{{topic}}-echo-{{date}}.md` |
| Corps/Crew | Team Contribution | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [N] contributors — [LIST_CONTRIBUTORS] — first joint artifact: [DATE] / IN-PROGRESS: [N] of 2 contributors active — second contributor needed / LOCKED: A second team member files any artifact for topic `{{topic}}` |

## Next Action

Run `/[SKILL]` to produce `{{topic}}-[ITEM]-{{date}}.md`.
This advances [CATEGORY: ACHIEVEMENT] from [CURRENT_STATE] toward [TARGET_STATE].
Why: [SPECIFIC_GAP — one sentence linking to the CLASSIFY GATE output].
```

Produce the STATE GATE schema. Authority: registry.

FAIL — does not clear STATE GATE:
- Numeric counts absent
- Counts do not sum to 7
- "All 7 rows filled" confirmation absent
- Gate label present but state counts absent

---

### PHASE 4 — WRITE GATE

Entry condition: STATE GATE output produced.

**WRITE GATE schema** (preface — restatement of registry authority; read before executing):
```
WRITE GATE CLEARED
Artifact path: simulations/topic/achievements/{{topic}}-achievements-{{date}}.md
Phases completed: 4
```

Write the filled template to:
`simulations/topic/achievements/{{topic}}-achievements-{{date}}.md`

```yaml
---
skill: topic-achievements
topic: {{topic}}
date: {{date}}
artifacts_scanned: [TOTAL_COUNT]
phases_completed: 4
earned: [n from STATE GATE]
in_progress: [n from STATE GATE]
locked: [n from STATE GATE]
---
```

Produce the WRITE GATE schema. Authority: registry.

FAIL — does not clear WRITE GATE:
- "WRITE GATE CLEARED" label absent
- Artifact path absent
- Path contains wrong topic or wrong date
- Gate label present but path absent

---

## V-05 — Golden Synthesis: Full-Schema Registry + Primacy + Severity-Stratified FAIL + Three-Layer Coverage

**Axes**: Lifecycle emphasis (full schema expansion in registry) + output format (registry
primacy declaration) + phrasing register (severity-stratified FAIL blocks) + R6 V-05
three-layer architecture (registry + schema preface + FAIL) preserved
**Hypothesis**: V-01 shows the registry can be self-sufficient for C-22 inspection (no
abbreviation). V-02 shows the registry can be contractually authoritative (not just co-located
but binding). V-03 shows FAIL blocks can be semantically taxonomized to explicitly surface
the semantic-bypass class (the hardest C-23 failure mode to detect). V-05 combines all three:
the registry is complete (full multi-line schemas, self-sufficient), authoritative (explicit
primacy declaration), and paired with severity-stratified FAIL blocks per phase (Tier 1/2/3
with Tier 3 naming the semantic bypass case). The three-layer architecture from R6 V-05
is preserved: registry (overview before work begins) + per-phase schema preface (goal-state
immediacy, labeled as registry restatement) + per-phase FAIL blocks (now severity-stratified).
These layers are not redundant — they act at different execution moments and now collectively
cover C-22 and C-23 at maximum depth: C-22 via a complete, authoritative, co-located registry;
C-23 via bi-directional per-gate contracts with semantic-bypass failure modes named explicitly.

---

You are running `topic-achievements` for topic: `{{topic}}`.

**Session invariants — apply throughout all phases:**

Invariant A (State): Each achievement row carries exactly one state: EARNED, IN-PROGRESS,
or LOCKED. No other values. No combined states.

Invariant B (Floor): Namespace-level evidence from the `prove` namespace is always
acceptable and is the safe floor for the Falsified achievement. Any prove artifact
containing a counter-signal or hypothesis revision qualifies Falsified for IN-PROGRESS.
No full synthesis required.

Invariant C (Citation): EARNED rows cite filename and date. IN-PROGRESS rows use `n of m`.
LOCKED rows name the exact artifact type or count required.

Invariant D (Preservation): The achievement table template in Phase 3 contains pre-printed
compliance text — in the Falsified row and in LOCKED cell detail. Do not rewrite, rephrase,
or restructure that pre-printed text. Fill only the placeholders as instructed.

---

**Gate Registry** — complete, authoritative schemas for all 4 gates, declared before Phase 1.

**REGISTRY PRIMACY**: The schemas below are the sole authoritative gate contracts. Phase
instructions implement these contracts; they do not redefine them. A gate output that
matches the schema declared here clears that gate. A gate output that does not match the
schema declared here does not clear that gate, regardless of any phase-level elaboration.
Retain these schemas throughout all phases.

**SCAN GATE** (Phase 1) — complete schema:
```
SCAN GATE CLEARED
Artifacts: [n]
Floor: active — Invariant B applies
```

**CLASSIFY GATE** (Phase 2) — complete schema:
```
CLASSIFY GATE CLEARED
Exploration: [list of qualifying artifact filenames, or "none"]
Depth: [n] artifacts
Coverage: [namespace prefixes list] — [n] of 9
Quality (Falsified candidates): [list of qualifying artifact filenames, or "none"]
Chain: hypothesis [present/absent] — evidence [present/absent] — synthesize [present/absent]
Discovery: [list of qualifying artifact filenames, or "none"]
Corps/Crew: contributors [list or "none"] — count [n]
[n] of 7 categories populated. Proceeding to template fill.
```

**STATE GATE** (Phase 3) — complete schema:
```
STATE GATE CLEARED
EARNED: [n]
IN-PROGRESS: [n]
LOCKED: [n]
All 7 rows filled. Invariants A–D applied.
```

**WRITE GATE** (Phase 4) — complete schema:
```
WRITE GATE CLEARED
Artifact path: simulations/topic/achievements/{{topic}}-achievements-{{date}}.md
Phases completed: 4
```

Phases must be completed in order. Entry condition for Phase N is the gate output of Phase N-1.

---

### PHASE 1 — SCAN GATE

**SCAN GATE schema** (preface — restatement of registry authority; read before executing):
```
SCAN GATE CLEARED
Artifacts: [n]
Floor: active — Invariant B applies
```

Glob `simulations/**/{{topic}}-*.md`. For each artifact, extract:
- Filename
- Skill (from `skill:` frontmatter or filename)
- Namespace prefix (first segment of skill name)
- Date (from `date:` frontmatter or filename)
- Contributor (`contributor:` or `author:` frontmatter, or "not set")

Produce the SCAN GATE schema above.

**FAIL — severity-stratified:**

*Tier 1 (Structural — gate output uninterpretable):*
- "SCAN GATE CLEARED" label absent

*Tier 2 (Completeness — label present but fields missing):*
- Artifact count line absent
- Floor confirmation line absent

*Tier 3 (Semantic bypass — fields present but intent bypassed):*
- Count present but does not match the artifacts listed
- Floor stated as "inactive" when prove-namespace artifacts exist — Invariant B is unconditional
  when prove artifacts are present; stating the floor inactive bypasses the guarantee while
  technically including the floor line

If n = 0: produce gate output with n=0. All STATE cells will be LOCKED in Phase 3. Proceed.

---

### PHASE 2 — CLASSIFY GATE

Entry condition: SCAN GATE CLEARED output produced.

**CLASSIFY GATE schema** (preface — restatement of registry authority; read before executing):
```
CLASSIFY GATE CLEARED
Exploration: [list or "none"]
Depth: [n] artifacts
Coverage: [namespaces list] — [n] of 9
Quality (Falsified candidates): [list or "none"]
Chain: hypothesis [present/absent] — evidence [present/absent] — synthesize [present/absent]
Discovery: [list or "none"]
Corps/Crew: contributors [list or "none"] — count [n]
[n] of 7 categories populated. Proceeding to template fill.
```

Assign each artifact from Phase 1 to exactly one category. Do not assign states.

| Category | Qualifying Skills |
|----------|------------------|
| Exploration | scout-*, topic-new, prove-hypothesis |
| Depth | All artifacts — count total; 5+ earns Signal Depth |
| Coverage | All artifacts — track unique namespace prefixes; 5+ of 9 earns Namespace Sweep |
| Quality | prove-synthesize or topic-echo containing a hypothesis revision |
| Chain | prove-hypothesis + (prove-websearch or prove-intelligence) + prove-synthesize |
| Discovery | topic-echo |
| Corps/Crew | 2+ distinct contributor values |

Produce the CLASSIFY GATE schema above.

**FAIL — severity-stratified:**

*Tier 1 (Structural — gate output uninterpretable):*
- "CLASSIFY GATE CLEARED" label absent

*Tier 2 (Completeness — label present but fields missing):*
- Any of the 7 labeled category lines absent (even if the result is "none", the line must appear)
- Summary count line absent

*Tier 3 (Semantic bypass — fields present but intent bypassed):*
- Summary count line present without the 7 labeled category lines — a count satisfies the
  summary field format but bypasses the per-category enumeration that makes the output
  verifiable; downstream phases cannot reconstruct category-level evidence from a count alone
- State assignments embedded in category lines — CLASSIFY assigns artifacts to categories,
  not states; embedding states in CLASSIFY output contaminates Phase 3 derivation
- Any artifact from Phase 1 absent from all 7 category lines without explanation — silent
  omission bypasses the exhaustive classification requirement while producing a correctly
  formatted gate output

---

### PHASE 3 — FILL TEMPLATE (STATE GATE)

Entry condition: CLASSIFY GATE CLEARED output produced.

**STATE GATE schema** (preface — restatement of registry authority; read before executing):
```
STATE GATE CLEARED
EARNED: [n]
IN-PROGRESS: [n]
LOCKED: [n]
All 7 rows filled. Invariants A–D applied.
```

Fill every `[PLACEHOLDER]` in the template below. Rules:
- Apply Invariant D: do not rewrite any pre-printed text.
- Do not reorder rows. Do not add or remove rows.
- Apply Invariants A, B, C to every row.
- EARNED: fill `[EARNED_ARTIFACT]` with `filename — date`. A date-less EARNED entry fails C-07.
- IN-PROGRESS: fill `[N]` and `[M]` with actual counts. Qualitative-only text without numbers
  fails C-04.
- LOCKED: detail text is pre-printed. Fill only `[SPECIFIC_GAP]` with the exact artifact
  type or action needed.

```markdown
## topic-achievements — {{topic}}
_Scanned: {{date}} — Total artifacts: [TOTAL_COUNT]_

| Category | Achievement | State | Detail |
|----------|-------------|-------|--------|
| Exploration | Spark | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [EARNED_ARTIFACT] / IN-PROGRESS: [N] of 1 artifact / LOCKED: File any one artifact for topic `{{topic}}` using any Signal skill |
| Depth | Signal Depth | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [N] artifacts — earliest [EARNED_ARTIFACT] / IN-PROGRESS: [N] of 5 artifacts / LOCKED: File 5 total artifacts for topic `{{topic}}` across any Signal skills |
| Coverage | Namespace Sweep | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [N] of 9 namespaces — [LIST_NAMESPACES] / IN-PROGRESS: [N] of 5 namespaces — missing: [LIST_MISSING] / LOCKED: File artifacts from 5 of the 9 namespaces (scout, draft, review, flow, trace, prove, listen, program, topic) |
| Quality | Falsified | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [EARNED_ARTIFACT] — followed evidence over assumptions: [REVISION_EVENT] / IN-PROGRESS: [N] of [M] prove artifacts contain counter-signals — not yet synthesized / LOCKED: File a prove-synthesize or topic-echo artifact that records a hypothesis revision. Framing falsification as absence or as a result the investigation did not yield — including as a closing reflection — does not earn this achievement. Namespace-level evidence from the prove namespace is always acceptable and is the safe floor. |
| Chain | Hypothesis Chain | [EARNED / IN-PROGRESS / LOCKED] | EARNED: prove-hypothesis [DATE1] → prove-evidence [DATE2] → prove-synthesize [DATE3] / IN-PROGRESS: [N] of 3 chain links — missing: [LIST_MISSING_LINKS] / LOCKED: File prove-hypothesis, then prove-websearch or prove-intelligence, then prove-synthesize — in that order |
| Discovery | Echo Filed | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [EARNED_ARTIFACT] / IN-PROGRESS: topic-echo started but not finalized / LOCKED: Run /topic-echo to produce `{{topic}}-echo-{{date}}.md` |
| Corps/Crew | Team Contribution | [EARNED / IN-PROGRESS / LOCKED] | EARNED: [N] contributors — [LIST_CONTRIBUTORS] — first joint artifact: [DATE] / IN-PROGRESS: [N] of 2 contributors active — second contributor needed / LOCKED: A second team member files any artifact for topic `{{topic}}` |

## Next Action

Run `/[SKILL]` to produce `{{topic}}-[ITEM]-{{date}}.md`.
This advances [CATEGORY: ACHIEVEMENT] from [CURRENT_STATE] toward [TARGET_STATE].
Why: [SPECIFIC_GAP — one sentence linking to the CLASSIFY GATE output].
```

Produce the STATE GATE schema above.

**FAIL — severity-stratified:**

*Tier 1 (Structural — gate output uninterpretable):*
- "STATE GATE CLEARED" label absent

*Tier 2 (Completeness — label present but fields missing):*
- Any of EARNED, IN-PROGRESS, or LOCKED count lines absent
- "All 7 rows filled" confirmation absent

*Tier 3 (Semantic bypass — counts present but internally inconsistent):*
- EARNED + IN-PROGRESS + LOCKED counts do not sum to 7 — a non-7 sum means at least one
  achievement was omitted or double-counted; the gate output appears complete (three count
  lines present) while bypassing the exhaustive coverage requirement

---

### PHASE 4 — WRITE GATE

Entry condition: STATE GATE output produced.

**WRITE GATE schema** (preface — restatement of registry authority; read before executing):
```
WRITE GATE CLEARED
Artifact path: simulations/topic/achievements/{{topic}}-achievements-{{date}}.md
Phases completed: 4
```

Write the filled template to:
`simulations/topic/achievements/{{topic}}-achievements-{{date}}.md`

```yaml
---
skill: topic-achievements
topic: {{topic}}
date: {{date}}
artifacts_scanned: [TOTAL_COUNT]
phases_completed: 4
earned: [n from STATE GATE]
in_progress: [n from STATE GATE]
locked: [n from STATE GATE]
---
```

Produce the WRITE GATE schema above.

**FAIL — severity-stratified:**

*Tier 1 (Structural — gate output uninterpretable):*
- "WRITE GATE CLEARED" label absent

*Tier 2 (Completeness — label present but fields missing):*
- Artifact path absent

*Tier 3 (Semantic bypass — path present but unreachable):*
- Path contains wrong topic name — artifact will not be found by topic-scanner glob
- Path contains wrong or missing date — artifact will not be found by date-scoped queries
  (path is structurally valid but semantically incorrect; the gate label and path line are
  both present, satisfying Tier 1 and Tier 2 while bypassing the path-correctness intent)
