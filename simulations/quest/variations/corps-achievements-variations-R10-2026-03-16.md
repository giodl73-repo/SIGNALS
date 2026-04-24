Now I have the full picture. R9's 5 axes were: leaderboard-first, dense-table, stagnation-first (Phase 0), STOP-barriers+leaderboard+stagnation (triple combo), conversational+dense-table. R10 should introduce C-28 as a testbed and explore achievement-census-first, per-topic scorecard blocks, gate-failure retry, and their combinations.

---

```markdown
---
skill: quest-variate
skill_target: corps-achievements
round: 10
date: 2026-03-16
rubric_version: 9
basis: R9 covered leaderboard-first, dense-table, stagnation-first, STOP-barrier combos,
  and conversational+table. R10 introduces C-28 (first-person owner confirmation syntax)
  as an experimental criterion, and tests achievement-census-first role sequence and
  per-topic scorecard format — neither explored in R9.
---

# Variate R10 — corps-achievements

5 complete prompt body variations for the `corps-achievements` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

R9 established five stylistic axes but kept structural gates constant. R10 shifts
the exploration to two structural gaps and one new excellence criterion:

1. **Achievement-census-first** role sequence — R9 went leaderboard-first. R10 tries
   topic-achievement-first: enumerate what topics have earned before attributing credit
   to contributors. This inverts the dependency direction — contributor standing derives
   from achievement evidence, not the other way around.

2. **Per-topic scorecard blocks** output format — R9 used global tables or bulleted
   lists. R10 renders one self-contained scorecard block per topic with a fixed schema.
   A missing topic becomes a missing block, not a missing row in a shared table.

3. **C-28 (experimental)**: First-person owner confirmation syntax in pre-write gates.
   R9's V-05 surfaced "Before I write this section, I confirm [C-11]: ..." as a
   structural pattern worth testing at scale. R10 makes C-28 explicit: every pre-write
   gate is a first-person owner commitment, not a third-person procedural sub-step.
   V-03 is the pure C-28 testbed; V-04 and V-05 carry it into combinations.

All variations carry the full v8/v9 baseline: essential C-01—C-05, recommended
C-06—C-08, aspirational C-09—C-27. C-28 is marked experimental in variations that
introduce it, and the structural audit gate expands to [C-20/C-25/C-26/C-27/C-28]
in those variations.

---

## Variation Axes Selected

| Axis | Hypothesis | Used In |
|------|------------|---------|
| Role sequence: Achievement-census-first | Enumerating topic achievements before contributor attribution means every contributor score derives from verified achievement evidence — eliminating the reverse-direction hallucination where leaderboard rank implies achievements that weren't explicitly enumerated | V-01, V-04 |
| Output format: Per-topic scorecard blocks | One named block per topic (fixed schema) makes topic omission structurally impossible — a missing topic is a missing block, not a missing row that can be absorbed into table whitespace | V-02, V-05 |
| Phrasing register: First-person owner confirmations (C-28 testbed) | When every pre-write gate uses "Before I write [section], I confirm [C-XX]: ..." syntax, the model binds as responsible agent rather than procedural executor — silent gate skips become agent commitment violations, not missed checklist items | V-03, V-04, V-05 |
| Lifecycle emphasis: Gate-failure retry loop | Embedding explicit retry instructions ("GATE FAILED — state correction, re-run this section") eliminates the proceed-with-violation pattern — the model has a named path when a gate fails, not just a prohibition | V-05 |
| Inertia framing: (carried from R9 V-03/V-04 baseline) | All variations carry the stagnation registry and pattern-breaking action format from R9; no new inertia axis is needed for R10 | all |

---

## Shared Resources (all variations reference these)

### Stagnation Pattern Registry

| Label | Pattern |
|-------|---------|
| SOLO_ISLAND | One contributor owns all signals — no team breadth or coverage diversity |
| NAMESPACE_MOAT | All signals from one namespace — no cross-namespace synthesis possible |
| SPRINT_FREEZE | No new signals added in current sprint window — momentum stalled |
| SHALLOW_POOL | Multiple topics with <3 signals each — Signal Depth unreached across the board |
| ORPHAN_TOPIC | Topics with no contributor metadata — ownership and accountability unknown |

Use label syntax `[PATTERN_LABEL from registry]`. Do not invent labels.

### Scoring Formula

```
Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)
```

Where:
- **Signals** = total signal files attributed to this contributor
- **Topics** = count of distinct topics the contributor has contributed to
- **Milestones** = count of the three team milestones this contributor's work provided
  evidence toward

### C-28 Experimental Criterion

> **C-28 (experimental)**: Every pre-write gate in the run uses first-person owner
> confirmation syntax: "Before I write [section], I confirm [C-XX]: [commitment text]."
> The confirmation must name the criterion ID it is verifying and state what the model
> is committing to — not what a generic executor "should" do. This is distinct from C-11
> (which is about what the pre-write gate checks) — C-28 is about the syntactic form
> binding the model as the responsible agent for the commitment.

Variations that introduce C-28 include it in the Structural Audit Gate as
`STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27/C-28]` and audit each pre-write gate
for C-28 compliance.

---

## V-01 — Role Sequence: Achievement-Census-First

**Axis**: Role sequence — per-topic achievement census runs as Phase 1 (immediately
after scan), before the contributor leaderboard in Phase 2. The leaderboard is computed
from Phase 1 achievement evidence, not from a fresh attribution pass.
**Hypothesis**: When achievement enumeration runs before contributor attribution, every
contributor score is derived from explicit achievement evidence — eliminating the
reverse-direction failure where a leaderboard entry implies achievements that were
never individually verified. Phase 1 produces the claim; Phase 2 inherits it.

---

You are running `corps-achievements`. Scan the workspace and compute team achievement state.
No arguments. Execute four phases in sequence. Do not begin a phase until the previous
phase's gate passes. Phase 1 enumerates what topics have earned and locked before any
contributor attribution. Phase 2 builds the contributor leaderboard from Phase 1 evidence.

---

### STAGNATION PATTERN REGISTRY

| Label | Pattern |
|-------|---------|
| SOLO_ISLAND | One contributor owns all signals — no breadth |
| NAMESPACE_MOAT | All signals from one namespace — no synthesis possible |
| SPRINT_FREEZE | No new signals in current sprint — momentum stalled |
| SHALLOW_POOL | Multiple topics, none reaching Signal Depth |
| ORPHAN_TOPIC | Topics with no contributor metadata — ownership unknown |

Use label syntax `[PATTERN_LABEL from registry]`. Do not invent labels.

### SCORING FORMULA

`Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

---

## PHASE 1 — SCAN AND ACHIEVEMENT CENSUS

### 1A — SCAN [C-01]

Glob `simulations/**/*.md`. Extract topic path, namespace, contributor, signal count
per topic.

```
SCAN STATE (internal):
  Topics: [list]  Namespaces: [list]  Contributors: [list]  Total signals: [n]
  Per topic: {topic: {signals: n, namespaces: [list], contributors: [list]}}
```

**SCAN GATE [C-01/C-15]** — numbered sub-steps [C-23]:
> "(1) `simulations/` accessible, >= 1 file from glob.
>  (2) Every file assigned to a real topic path from glob output.
>  (3) Per-topic breakdown complete — each topic has signal count, namespace list,
>      contributor list. (4) No file skipped."
>
> Pass: "SCAN GATE [C-01]: [n] signals, [n] topics, contributors: [list]."
> Fail: "SCAN GATE FAIL [C-01/C-15]: condition ([n]) — [specific path or topic]."

### 1B — ACHIEVEMENT CENSUS [C-02/C-06/C-07]

**Pre-write gate [C-11]**: "Does the topic count below match scan state? If not,
add missing topics before writing. Confirm: all topic counts, namespace lists, and
contributor lists come from the per-topic scan breakdown above — not estimated."

Achievement definitions (evaluate each topic against scan state data):

| Achievement | Condition |
|-------------|-----------|
| First Signal | >= 1 signal for this topic |
| Signal Depth | >= 3 signals for this topic |
| Full Sweep | signals span >= 3 distinct namespaces |
| Solo Pioneer | exactly 1 contributor, >= 1 signal |
| Team Topic | >= 2 contributors, >= 1 signal each |

```markdown
## Earned Achievements — {{date}}

**[topic path]** ([n] signals, namespaces: [list], contributors: [list])
  - **[Achievement name]**: [evidence — exact counts from scan state]

## Locked Achievements

**[topic path]** ([n] signals)
  - o [Achievement name]: needs [quantified gap — "2 more signals", "1 more namespace"]
```

**COMPUTE GATE [C-02/C-15]** — numbered sub-steps [C-23]:
> "(1) Every topic in scan state appears in Earned or Locked — count matches scan state total.
>  (2) Every Earned entry names specific evidence from scan state — counts, namespaces, or names.
>  (3) Every Locked entry quantifies the gap with a specific number or target.
>  (4) No topic's achievement is inferred from contributor identity — all evidence
>      cites signal counts, namespaces, or file paths from scan state."
>
> Fail: "COMPUTE GATE FAIL [C-02/C-15]: condition ([n]) — [specific topic or instance]."

### 1C — RECORD PHASE 1 STATE (internal)

```
PHASE 1 STATE:
  Topics with >= 1 earned achievement: [list]
  Topics with zero earned achievements: [list/"none"]
  Per-topic signal counts: {topic: n, ...}
  Per-topic contributor lists: {topic: [contributors], ...}
  Topics needing 1 more signal for Signal Depth: [list/"none"]
  Topics needing 1 more namespace for Full Sweep: [list/"none"]
```

---

## PHASE 2 — CONTRIBUTOR LEADERBOARD

### 2A — LEADERBOARD FROM PHASE 1 EVIDENCE [C-04/C-16/C-19/C-21]

**Pre-write gate [C-11]**: "Are Signals, Topics, and Milestones counts per contributor
derived from the Phase 1 State per-topic contributor lists — not from re-scanning?
If any contributor's topic count cannot be verified from Phase 1 State, re-derive
from scan state before writing."

Build the leaderboard by reading Phase 1 State per-topic contributor data:
- Signals = sum of all signal counts from topics this contributor appears in
- Topics = count of distinct topics this contributor appears in
- Milestones = (determined after Phase 3 milestone computation — set to 0 here,
  update after Phase 3 if milestones earned)

```markdown
## Contributor Leaderboard — Week of {{date}}

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
```

Formula: `Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

**LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]** — numbered sub-steps [C-23]:
This gate covers formula-driven scoring (C-16), worked example render (C-19), and
reconciliation correction loop (C-21). All three checked together — formula claim
without worked example is unverifiable; worked example without reconciliation loop
cannot self-correct.

> "(1) Leaderboard uses formula Score=(Signals×1)+(Topics×3)+(Milestones×5). [C-16]
>  (2) Contributor counts sourced from Phase 1 State — not re-scanned. [C-16]
>  (3) Worked example for Rank 1: Score = {S}×1 + {T}×3 + {M}×5 = {total}. [C-19]
>  (4) Compare {total} to Score column for Rank 1. [C-21]
>  (5) If mismatch: correct Score column to {total}; state 'Corrected: {old}→{new}.' [C-21]
>  (6) Score column for Rank 1 now equals {total}. [C-21]
>  (7) Gate label [C-16/C-19/C-21] enumerates all criterion IDs it covers. [C-25]"
>
> Pass: "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]: Passed.
>   Formula (C-16): confirmed. Example (C-19): {total}. Reconciliation (C-21): [applied/clear].
>   Label enumeration (C-25): [C-16/C-19/C-21] verified."
> Not applicable: "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]: Not applicable — no contributors."

---

## PHASE 3 — MILESTONES, GAPS, INSIGHT, AND ACTIONS

### 3A — TEAM MILESTONES [C-03]

```markdown
## Team Milestones — {{date}}

| Milestone | Status | Evidence | Gap |
|-----------|--------|----------|-----|
| first team signal | EARNED / NOT YET | [path/"—"] | [gap/"—"] |
| shared coverage | EARNED / NOT YET | [2+contrib×2+topics/"—"] | [gap/"—"] |
| debate starter | EARNED / NOT YET | [topic+namespaces/"—"] | [gap/"—"] |
```

Definitions: first team signal = any file found; shared coverage = 2+ contributors
× 2+ topics each; debate starter = 1 topic × 3+ distinct namespaces.

**MILESTONES GATE [C-03/C-15]** — numbered sub-steps [C-23]:
> "(1) Row 1 = 'first team signal'. (2) Row 2 = 'shared coverage'.
>  (3) Row 3 = 'debate starter'. (4) All Evidence and Gap cells populated or '—'.
>  (5) No milestone row name paraphrased."
>
> Fail: "MILESTONES GATE FAIL [C-03/C-15]: condition ([n]) — [row or cell]."

Update Phase 2 leaderboard Milestones column using earned milestone evidence above.

### 3B — 1-AWAY GAPS [C-09/C-18]

```markdown
## Almost There — 1-Away Gaps

| Topic / Milestone | Achievement to Unlock | Gap | Exact Action Needed |
|-------------------|-----------------------|-----|---------------------|
```

**1-AWAY GATE [C-09/C-18]** — numbered sub-steps [C-23]:
> "(1) Checked all topics from Phase 1 State vs all achievement thresholds for 1-step gaps.
>  (2) Checked all milestones for 1-step gaps. (3) All rows have all four columns."
>
> Fail: "1-AWAY GATE FAIL [C-09/C-18]: row '[topic]' missing column."

### 3C — TEAM INSIGHT [C-10/C-13/C-22]

**Step A**: State candidate insight — specific numbers and topic/contributor names.
**Step B**: Per-topic derivability test — for each topic in scan state: "Can this
insight be derived from [topic] alone? YES/NO."
**Step C**: All NO → approved. Any YES → generate new candidate (up to 2 attempts).
**Step D**: Confirm insight is distinct from any gap or stagnation statement in this run.

**INSIGHT GATE [C-10/C-13/C-22]** — numbered sub-steps [C-23]:
> "(1) Formatted as **TEAM INSIGHT — [descriptive name]:**. [C-13]
>  (2) Names specific topics, contributors, or numerical values. [C-10]
>  (3) Passed per-topic derivability elimination for all topics in scan state. [C-22]
>  (4) Distinct from any gap or stagnation statement already written. [C-10]"
>
> Fail: "INSIGHT GATE FAIL [C-10/C-13/C-22]: condition ([n]) — [specific issue]."

```markdown
**TEAM INSIGHT — [descriptive name]:** [insight sentence]
```

### 3D — NEXT ACTIONS [C-05/C-12/C-14/C-17]

State dominant stagnation pattern from registry before writing actions.

```markdown
## Next Actions

Dominant stagnation pattern: **[PATTERN_LABEL from registry]**

1. **[specific action — namespace and topic explicit]**
   → Unlocks **[Achievement or Milestone]**
   → Breaks **[PATTERN_LABEL from registry]**: [one sentence on mechanism]

2. [same format]

3. [same format]
```

**ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]** — numbered sub-steps [C-23]:
This gate covers unlock naming (C-05), anti-inertia format (C-12), registry labels
(C-14), and gate ID enumeration (C-20). All four checked together — C-12's format
requires C-14's label; C-14's sourcing is only verifiable when C-20 exposes the
dependency.

> "(1) Each action names a specific namespace and topic. [C-05]
>  (2) Each action names the exact achievement or milestone it unlocks. [C-05]
>  (3) Format: [Action] → Unlocks [X] → Breaks [Pattern]. [C-12]
>  (4) Every pattern label from registry — no invented labels. [C-14]
>  (5) At least 3 actions. [C-05]
>  (6) Gate label [C-05/C-12/C-14/C-20] enumerates all covered IDs. [C-25]"
>
> Pass: "ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]: Passed.
>   Unlock named (C-05): confirmed. Anti-inertia format (C-12): confirmed.
>   Registry labels (C-14): confirmed. Label enumeration (C-25): [C-05/C-12/C-14/C-20] verified."
> Fail: "ACTIONS CLUSTER GATE FAIL [C-05/C-12/C-14/C-20]: action [n], condition ([n]) — [issue]."

### 3E — RECORD PHASE 3 STATE (internal)

```
PHASE 3 STATE:
  Milestones not yet earned: [list/"all earned"]
  1-away gap topics: [list/"none"]
  Implied missing topics: [list/"none"]
  Implied missing contributors: [list/"none"]
```

---

## PHASE 4 — CROSS-PHASE CORRECTION AND STRUCTURAL AUDIT

### 4A — CROSS-PHASE CONTINUITY GATE [C-24]

**CROSS-PHASE GATE [C-24/C-01/C-02]** — numbered sub-steps [C-23]:
> "(1) Read Phase 3 State: milestone gaps, 1-away topics, implied missing topics/contributors.
>  (2) Did Phase 3 gaps surface topic names absent from Phase 1 scan state? YES/NO.
>  (3) Did Phase 3 gaps surface contributor names absent from Phase 2 leaderboard? YES/NO.
>  (4) YES to (2): add missing topics to Phase 1B Earned/Locked with evidence or gap.
>      State: 'CROSS-PHASE UPDATE [C-24]: topic(s) [list] added from Phase 3 gap analysis.'
>  (5) YES to (3): flag in frontmatter as `c24_missing_contributors: [list]`.
>  (6) NO to both: 'CROSS-PHASE GATE [C-24]: No Phase 3 additions to Phase 1/2 output.'
>  (7) Phase 1 topic list and Phase 2 leaderboard are now finalized."
>
> Pass: "CROSS-PHASE GATE [C-24]: Passed. Additions: [n topics / 0]."

### 4B — STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]

Scan back through all output produced in Phases 1–3. List every gate label.

**STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]** — numbered sub-steps [C-23]:
> "(1) List every gate label executed in this run (Phases 1–3).
>  (2) For each gate label: confirm it carries at least one [C-XX] criterion ID reference.
>  (3) Verify each multi-criterion super-gate by full label name and exact IDs expected:
>      - 'LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]' — confirm enumerates C-16, C-19, C-21.
>      - 'ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]' — confirm enumerates C-05, C-12, C-14, C-20.
>  (4) Missing ID: 'AUDIT FAIL [C-20/C-26]: gate "[label]" missing ID.'
>  (5) Wrong super-gate enumeration: 'AUDIT FAIL [C-27]: gate "[label]" — expected [C-XX/...],
>      found [C-XX/...].'
>  (6) Count: [n] gates audited, [n] correct, [n] violations.
>  (7) All pass: 'STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]: Passed. [n] gates correct,
>        super-gates [C-16/C-19/C-21] and [C-05/C-12/C-14/C-20] enumeration verified.'
>      Any fail: 'STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]: [n] violation(s). See findings.'"
>
> Violations are findings, not blockers — record count in frontmatter and proceed.

### WRITE ARTIFACT [C-08]

Write to `simulations/corps/achievements-{{date}}.md`.

```yaml
---
skill: corps-achievements
date: {{date}}
topics_scanned: [n]
topics_added_via_cross_phase: [n or 0]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
stagnation_pattern: [PATTERN_LABEL]
c24_cross_phase_gate: [additions_made/no_additions]
c25_super_gates: ["LEADERBOARD CLUSTER [C-16/C-19/C-21]", "ACTIONS CLUSTER [C-05/C-12/C-14/C-20]"]
c26_structural_audit_gates_checked: [n]
c26_structural_audit_violations: [n or "none"]
c27_super_gate_enumeration_verified: [true/false]
c21_correction_applied: [true/false/not_applicable]
c22_derivability_passed: [true/false]
role_sequence: achievement-census-first
gate_language: numbered-substeps
---
```

---

## V-02 — Output Format: Per-Topic Scorecard Blocks

**Axis**: Output format — each topic is rendered as a self-contained scorecard block
with a fixed four-row schema (signals, namespaces, contributors, achievements). There
are no global Earned/Locked tables. A missing topic is a missing block.
**Hypothesis**: Per-topic scorecard format eliminates the "omission by burial" failure
mode: in a global table, a missing topic is a missing row that disappears into
whitespace; in a named scorecard block, a missing topic is a structurally absent
section. The format forces completeness at the topic level, not at the table level,
and makes every topic's achievement state independently auditable without cross-row
scanning.

---

You are running `corps-achievements`. Scan the workspace and compute team achievement state.
No arguments. Execute three phases. All per-topic output is rendered as scorecard blocks —
one block per topic with a fixed schema. Do not begin a phase until the previous phase's
gate passes.

---

### STAGNATION PATTERN REGISTRY

| Label | Pattern |
|-------|---------|
| SOLO_ISLAND | One contributor owns all signals — no breadth |
| NAMESPACE_MOAT | All signals from one namespace — no synthesis possible |
| SPRINT_FREEZE | No new signals in current sprint — momentum stalled |
| SHALLOW_POOL | Multiple topics, none reaching Signal Depth |
| ORPHAN_TOPIC | Topics with no contributor metadata — ownership unknown |

Use label syntax `[PATTERN_LABEL from registry]`. Do not invent labels.

### SCORING FORMULA

`Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

### SCORECARD BLOCK SCHEMA

Each topic scorecard block uses this fixed schema:

```markdown
### Topic Scorecard: [topic path] — {{date}}

| Field | Value |
|-------|-------|
| Signals | [n] |
| Namespaces | [list] |
| Contributors | [list or "unknown"] |

**Earned:**
- [Achievement name]: [evidence]

**Locked:**
- o [Achievement name]: needs [quantified gap]
```

If a topic has no earned achievements, write `**Earned:** (none yet)`.
If a topic has no locked achievements remaining, write `**Locked:** (all unlocked)`.

---

## PHASE 1 — SCAN AND TOPIC SCORECARDS

### 1A — SCAN [C-01]

Glob `simulations/**/*.md`. Extract topic path, namespace, contributor per file.

```
SCAN STATE (internal):
  Topics: [list]  Namespaces: [list]  Contributors: [list]  Total signals: [n]
```

**SCAN GATE [C-01/C-15]** — numbered sub-steps [C-23]:
> "(1) `simulations/` accessible, >= 1 file from glob.
>  (2) Every file assigned to a real topic path from glob output.
>  (3) Scan state complete. (4) No file skipped."
>
> Pass: "SCAN GATE [C-01]: [n] signals, [n] topics, contributors: [list]."
> Fail: "SCAN GATE FAIL [C-01/C-15]: condition ([n]) — [specific path or topic]."

### 1B — TOPIC SCORECARDS [C-02/C-06/C-07]

**Pre-write gate [C-11]**: "How many topics are in scan state? I will write exactly
that many scorecard blocks. Missing topics: [list or 'none']. Adding before writing."

Achievement definitions: First Signal (>=1), Signal Depth (>=3), Full Sweep (>=3
namespaces), Solo Pioneer (exactly 1 contributor), Team Topic (>=2 contributors).

Write one scorecard block per topic using the fixed schema above. Order scorecards
by signal count descending (most-signal topics first).

```markdown
## Topic Scorecards — {{date}}

### Topic Scorecard: [topic path] — {{date}}
...

### Topic Scorecard: [topic path] — {{date}}
...
```

**SCORECARD GATE [C-02/C-15]** — numbered sub-steps [C-23]:
> "(1) Scorecard block count equals topic count in scan state — count both.
>  (2) Every Earned entry has a populated evidence line — no bare achievement names.
>  (3) Every Locked entry has a specific quantified gap.
>  (4) Every block has all four fields: Signals, Namespaces, Contributors, Earned/Locked.
>  (5) No topic appears in more than one block."
>
> Fail: "SCORECARD GATE FAIL [C-02/C-15]: condition ([n]) — [topic path or field name]."

### 1C — CONTRIBUTOR LEADERBOARD [C-04/C-16/C-19/C-21]

**Pre-write gate [C-11]**: "Contributor counts derived from scorecard block data above
— not re-scanned. Ready to write."

```markdown
## Contributor Leaderboard — Week of {{date}}

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
```

Formula: `Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

**LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]** — numbered sub-steps [C-23]:
This gate covers formula-driven scoring (C-16), worked example render (C-19), and
reconciliation correction loop (C-21). All three checked together.

> "(1) Leaderboard uses formula Score=(Signals×1)+(Topics×3)+(Milestones×5). [C-16]
>  (2) Worked example for Rank 1: Score = {S}×1 + {T}×3 + {M}×5 = {total}. [C-19]
>  (3) Compare {total} to Score column for Rank 1. [C-21]
>  (4) If mismatch: correct Score column; state 'Corrected: {old}→{new}.' [C-21]
>  (5) Score column for Rank 1 = {total}. [C-21]
>  (6) Gate label [C-16/C-19/C-21] enumerates all covered criterion IDs. [C-25]"
>
> Pass: "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]: Passed.
>   Formula (C-16): confirmed. Example (C-19): {total}. Reconciliation (C-21): [applied/clear].
>   Label enumeration (C-25): [C-16/C-19/C-21] verified."
> Not applicable: "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]: Not applicable — no contributors."

---

## PHASE 2 — MILESTONES, GAPS, INSIGHT, AND ACTIONS

### 2A — TEAM MILESTONES [C-03]

```markdown
## Team Milestones — {{date}}

| Milestone | Status | Evidence | Gap |
|-----------|--------|----------|-----|
| first team signal | EARNED / NOT YET | [path/"—"] | [gap/"—"] |
| shared coverage | EARNED / NOT YET | [2+contrib×2+topics/"—"] | [gap/"—"] |
| debate starter | EARNED / NOT YET | [topic+namespaces/"—"] | [gap/"—"] |
```

**MILESTONES GATE [C-03/C-15]** — numbered sub-steps [C-23]:
> "(1) Row 1 = 'first team signal'. (2) Row 2 = 'shared coverage'.
>  (3) Row 3 = 'debate starter'. (4) Evidence and Gap cells populated or '—'.
>  (5) No row name paraphrased."
>
> Fail: "MILESTONES GATE FAIL [C-03/C-15]: condition ([n]) — [row or cell]."

### 2B — 1-AWAY GAPS [C-09/C-18]

Derive from scorecard blocks in Phase 1B — scan each block for locked achievements
that are exactly 1 step away.

```markdown
## Almost There — 1-Away Gaps

| Topic / Milestone | Achievement to Unlock | Gap | Exact Action Needed |
|-------------------|-----------------------|-----|---------------------|
```

**1-AWAY GATE [C-09/C-18]** — numbered sub-steps [C-23]:
> "(1) Checked all scorecard blocks from Phase 1B for exactly-1-step locked achievements.
>  (2) Checked all milestones for 1-step gaps.
>  (3) All rows have all four columns populated."
>
> Fail: "1-AWAY GATE FAIL [C-09/C-18]: row '[topic]' missing column."

### 2C — TEAM INSIGHT [C-10/C-13/C-22]

**Step A**: State candidate insight — must cite data from >= 2 scorecard blocks.
**Step B**: Per-topic derivability test — for each topic in scan state: "Could this
insight be derived from the [topic] scorecard block alone? YES/NO."
**Step C**: All NO → approved. Any YES → generate new candidate (up to 2 attempts).

**INSIGHT GATE [C-10/C-13/C-22]** — numbered sub-steps [C-23]:
> "(1) Formatted as **TEAM INSIGHT — [descriptive name]:**. [C-13]
>  (2) Names specific topics, contributors, or numeric values. [C-10]
>  (3) Passed per-topic derivability test for all topics in scan state. [C-22]
>  (4) Cites data from >= 2 scorecard blocks — not derivable from any single block. [C-10]"
>
> Fail: "INSIGHT GATE FAIL [C-10/C-13/C-22]: condition ([n]) — [specific issue]."

```markdown
**TEAM INSIGHT — [descriptive name]:** [insight sentence]
```

### 2D — NEXT ACTIONS [C-05/C-12/C-14/C-17]

State dominant stagnation pattern from registry, then write actions.

```markdown
## Next Actions

Dominant stagnation pattern: **[PATTERN_LABEL from registry]**

1. **[specific action — namespace and topic explicit]**
   → Unlocks **[Achievement or Milestone]**
   → Breaks **[PATTERN_LABEL from registry]**: [one sentence]

2. [same format]

3. [same format]
```

**ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]** — numbered sub-steps [C-23]:
This gate covers unlock naming (C-05), anti-inertia format (C-12), registry labels
(C-14), and gate ID enumeration (C-20).

> "(1) Each action names specific namespace and topic. [C-05]
>  (2) Each action names exact achievement or milestone unlocked. [C-05]
>  (3) Format: [Action] → Unlocks [X] → Breaks [Pattern]. [C-12]
>  (4) Every pattern label from registry. [C-14]
>  (5) At least 3 actions. [C-05]
>  (6) Gate label [C-05/C-12/C-14/C-20] enumerates all covered IDs. [C-25]"
>
> Pass: "ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]: Passed.
>   Unlock named (C-05): confirmed. Anti-inertia format (C-12): confirmed.
>   Registry labels (C-14): confirmed. Label enumeration (C-25): [C-05/C-12/C-14/C-20] verified."
> Fail: "ACTIONS CLUSTER GATE FAIL [C-05/C-12/C-14/C-20]: action [n], condition ([n]) — [issue]."

### 2E — RECORD PHASE 2 STATE (internal)

```
PHASE 2 STATE:
  Milestones not yet earned: [list/"all earned"]
  1-away gap topics: [list/"none"]
  Implied missing topics: [list/"none"]
  Implied missing namespaces: [list/"none"]
```

---

## PHASE 3 — CROSS-PHASE CORRECTION AND STRUCTURAL AUDIT

### 3A — CROSS-PHASE CONTINUITY GATE [C-24]

**CROSS-PHASE GATE [C-24/C-01/C-02]** — numbered sub-steps [C-23]:
> "(1) Read Phase 2 State.
>  (2) Did Phase 2 gaps surface topic names absent from Phase 1 scan state? YES/NO.
>  (3) Did Phase 2 gaps imply namespaces absent from Phase 1 namespace list? YES/NO.
>  (4) YES to (2): write a new scorecard block for each missing topic with evidence or gap.
>      State: 'CROSS-PHASE UPDATE [C-24]: scorecard block(s) added for [list].'
>  (5) YES to (3): record in frontmatter as `c24_namespace_gaps: [list]`.
>  (6) NO to both: 'CROSS-PHASE GATE [C-24]: No Phase 2 additions to Phase 1 output.'
>  (7) Scorecard block count is now finalized."
>
> Pass: "CROSS-PHASE GATE [C-24]: Passed. Additions: [n blocks / 0]."

### 3B — STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]

Scan back through all output produced in Phases 1–2. List every gate label.

**STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]** — numbered sub-steps [C-23]:
> "(1) List every gate label executed in this run (Phases 1–2).
>  (2) For each gate label: confirm it carries at least one [C-XX] criterion ID reference.
>  (3) Verify super-gates:
>      - 'LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]' — enumerates C-16, C-19, C-21.
>      - 'ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]' — enumerates C-05, C-12, C-14, C-20.
>  (4) Missing ID: 'AUDIT FAIL [C-20/C-26]: gate "[label]" missing ID.'
>  (5) Wrong enumeration: 'AUDIT FAIL [C-27]: gate "[label]" — expected [C-XX/...], found [C-XX/...].'
>  (6) Count: [n] gates audited, [n] correct, [n] violations.
>  (7) All pass: 'STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]: Passed. [n] gates correct,
>        super-gates enumeration verified for [C-16/C-19/C-21] and [C-05/C-12/C-14/C-20].'
>      Any fail: 'STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]: [n] violation(s). See findings.'"
>
> Violations are findings, not blockers.

### WRITE ARTIFACT [C-08]

Write to `simulations/corps/achievements-{{date}}.md`.

```yaml
---
skill: corps-achievements
date: {{date}}
topics_scanned: [n]
topics_added_via_cross_phase: [n or 0]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
stagnation_pattern: [PATTERN_LABEL]
c24_cross_phase_gate: [additions_made/no_additions]
c24_namespace_gaps: [list or "none"]
c25_super_gates: ["LEADERBOARD CLUSTER [C-16/C-19/C-21]", "ACTIONS CLUSTER [C-05/C-12/C-14/C-20]"]
c26_structural_audit_gates_checked: [n]
c26_structural_audit_violations: [n or "none"]
c27_super_gate_enumeration_verified: [true/false]
c21_correction_applied: [true/false/not_applicable]
c22_derivability_passed: [true/false]
output_format: per-topic-scorecard-blocks
gate_language: numbered-substeps
---
```

---

## V-03 — Phrasing Register: First-Person Owner Confirmations (C-28 Testbed)

**Axis**: Phrasing register — every pre-write gate uses first-person owner confirmation
syntax. Format: "Before I write [section], I confirm [C-XX]: [what I am committing to]."
This is the experimental C-28 testbed variation. All pre-write gates (C-11 instances)
and the phase-transition gate are first-person ownership statements. The structural audit
expands to cover C-28 compliance.
**Hypothesis**: When each pre-write gate is a first-person owner commitment rather than
a procedural sub-step check, the model binds itself as the responsible agent for the
commitment — a violation becomes an agent commitment failure, not a missed checklist
item. The ownership syntax also forces the gate criterion ID to appear naturally in
the confirmation ("I confirm [C-11]: ...") which improves C-25 label traceability
as a side effect. C-28 is tested here in isolation to determine how consistently the
model can maintain ownership syntax throughout a full run before it is carried into
combinations.

---

You are running `corps-achievements`. Scan the workspace and compute team achievement
state. No arguments. Execute three phases. Before writing any section, issue a first-person
owner confirmation in this form: "Before I write [section], I confirm [C-XX]: [commitment]."
Do not begin a phase until the previous phase's gate passes.

---

### STAGNATION PATTERN REGISTRY

| Label | Pattern |
|-------|---------|
| SOLO_ISLAND | One contributor owns all signals — no breadth |
| NAMESPACE_MOAT | All signals from one namespace — no synthesis possible |
| SPRINT_FREEZE | No new signals in current sprint — momentum stalled |
| SHALLOW_POOL | Multiple topics, none reaching Signal Depth |
| ORPHAN_TOPIC | Topics with no contributor metadata — ownership unknown |

Use label syntax `[PATTERN_LABEL from registry]`. Do not invent labels.

### SCORING FORMULA

`Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

### C-28 SYNTAX CONTRACT

Every pre-write confirmation must follow this exact form:
> "Before I write [section name], I confirm [C-XX]: [first-person commitment statement]."

The criterion ID must be the criterion the gate is verifying (e.g., C-11 for content
completeness, C-02 for achievement coverage, C-04 for leaderboard presence). If a
section verifies multiple criteria, list them: "I confirm [C-11/C-02]: ..."

---

## PHASE 1 — SCAN AND COMPUTE

### 1A — SCAN [C-01]

Glob `simulations/**/*.md`. Extract topic path, namespace, contributor per file.

```
SCAN STATE (internal):
  Topics: [list]  Namespaces: [list]  Contributors: [list]  Total signals: [n]
```

**SCAN GATE [C-01/C-15]** — numbered sub-steps [C-23]:
> "(1) `simulations/` accessible, >= 1 file from glob.
>  (2) Every file assigned to a real topic path.
>  (3) Scan state complete. (4) No file skipped."
>
> Pass: "SCAN GATE [C-01]: [n] signals, [n] topics, contributors: [list]."
> Fail: "SCAN GATE FAIL [C-01/C-15]: condition ([n]) — [specific path]."

### 1B — ACHIEVEMENTS [C-02/C-06/C-07]

Before I write the achievements section, I confirm [C-11/C-02]:
> "Every topic from scan state appears in either Earned or Locked below.
> Missing topics: [list or 'none']. I will add them before writing."

Achievement definitions: First Signal (>=1), Signal Depth (>=3), Full Sweep (>=3
namespaces), Solo Pioneer (exactly 1 contributor), Team Topic (>=2 contributors).

```markdown
## Earned Achievements — {{date}}

**[topic path]** ([n] signals)
  - **[Achievement name]**: [evidence — exact counts, contributors, or namespace list]

## Locked Achievements

**[topic path]** ([n] signals)
  - o [Achievement name]: needs [quantified gap]
```

**COMPUTE GATE [C-02/C-15]** — numbered sub-steps [C-23]:
> "(1) Every scan-state topic in Earned or Locked — counts match.
>  (2) Every Earned entry has specific evidence.
>  (3) Every Locked entry has quantified gap."
>
> Fail: "COMPUTE GATE FAIL [C-02/C-15]: condition ([n]) — [specific topic]."

### 1C — CONTRIBUTOR LEADERBOARD [C-04/C-16/C-19/C-21]

Before I write the contributor leaderboard, I confirm [C-11/C-04]:
> "Signals, Topics, and Milestones counts per contributor are derived from scan state,
> not estimated. I have attribution data for every contributor in the contributor list."

```markdown
## Contributor Leaderboard — Week of {{date}}

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
```

Formula: `Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

**LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]** — numbered sub-steps [C-23]:
This gate covers formula-driven scoring (C-16), worked example render (C-19), and
reconciliation correction loop (C-21). All three checked together.

> "(1) Formula Score=(Signals×1)+(Topics×3)+(Milestones×5) — not raw count rank. [C-16]
>  (2) Worked example for Rank 1: Score = {S}×1 + {T}×3 + {M}×5 = {total}. [C-19]
>  (3) Compare {total} to Score column for Rank 1. [C-21]
>  (4) Mismatch: correct to {total}; state 'Corrected: {old}→{new}.' [C-21]
>  (5) Score column for Rank 1 = {total}. [C-21]
>  (6) Gate label [C-16/C-19/C-21] enumerates all covered criterion IDs. [C-25]"
>
> Pass: "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]: Passed.
>   Formula (C-16): confirmed. Example (C-19): {total}. Reconciliation (C-21): [applied/clear].
>   Label enumeration (C-25): [C-16/C-19/C-21] verified."
> Not applicable: "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]: Not applicable — no contributors."

---

## PHASE 2 — MILESTONES, GAPS, INSIGHT, AND ACTIONS

### 2A — TEAM MILESTONES [C-03]

Before I write the milestones section, I confirm [C-11/C-03]:
> "I will use the exact milestone names 'first team signal', 'shared coverage', and
> 'debate starter' — not paraphrases. Evidence cells will cite specific file paths
> or contributor-topic combinations from scan state."

```markdown
## Team Milestones — {{date}}

| Milestone | Status | Evidence | Gap |
|-----------|--------|----------|-----|
| first team signal | EARNED / NOT YET | [path/"—"] | [gap/"—"] |
| shared coverage | EARNED / NOT YET | [2+contrib×2+topics/"—"] | [gap/"—"] |
| debate starter | EARNED / NOT YET | [topic+namespaces/"—"] | [gap/"—"] |
```

**MILESTONES GATE [C-03/C-15]** — numbered sub-steps [C-23]:
> "(1) Row 1 = 'first team signal'. (2) Row 2 = 'shared coverage'.
>  (3) Row 3 = 'debate starter'. (4) Evidence/Gap cells populated or '—'.
>  (5) No row name paraphrased."
>
> Fail: "MILESTONES GATE FAIL [C-03/C-15]: condition ([n]) — [row or cell]."

### 2B — 1-AWAY GAPS [C-09/C-18]

Before I write the 1-away gaps section, I confirm [C-11/C-09]:
> "I have checked every topic against every achievement threshold and every milestone
> against its definition. I will only list items that are exactly one step away —
> not items requiring two or more steps."

```markdown
## Almost There — 1-Away Gaps

| Topic / Milestone | Achievement to Unlock | Gap | Exact Action Needed |
|-------------------|-----------------------|-----|---------------------|
```

**1-AWAY GATE [C-09/C-18]** — numbered sub-steps [C-23]:
> "(1) All topics checked vs all thresholds for exactly-1-step gaps.
>  (2) All milestones checked for 1-step gaps.
>  (3) All rows have all four columns."
>
> Fail: "1-AWAY GATE FAIL [C-09/C-18]: row '[topic]' missing column."

### 2C — TEAM INSIGHT [C-10/C-13/C-22]

Before I write the team insight, I confirm [C-11/C-10/C-22]:
> "My candidate insight is not derivable from any single topic. I will run the
> per-topic derivability test explicitly before committing to this insight."

**Step A**: State candidate insight with specific numbers and names.
**Step B**: For each topic in scan state: "Can this be derived from [topic] alone? YES/NO."
**Step C**: All NO → approved. Any YES → generate new candidate (up to 2 attempts).

**INSIGHT GATE [C-10/C-13/C-22]** — numbered sub-steps [C-23]:
> "(1) Formatted as **TEAM INSIGHT — [descriptive name]:**. [C-13]
>  (2) Names specific topics, contributors, or numeric values. [C-10]
>  (3) Passed per-topic derivability elimination for all topics in scan state. [C-22]"
>
> Fail: "INSIGHT GATE FAIL [C-10/C-13/C-22]: condition ([n]) — [specific issue]."

```markdown
**TEAM INSIGHT — [descriptive name]:** [insight sentence]
```

### 2D — NEXT ACTIONS [C-05/C-12/C-14/C-17]

Before I write the next actions section, I confirm [C-11/C-05/C-14]:
> "Each action I write will name a specific namespace and topic, name an exact
> unlock, use the [Action] → Unlocks [X] → Breaks [Pattern] format, and draw
> the pattern label from the Stagnation Pattern Registry only."

State dominant stagnation pattern before writing actions.

```markdown
## Next Actions

Dominant stagnation pattern: **[PATTERN_LABEL from registry]**

1. **[specific action — namespace and topic explicit]**
   → Unlocks **[Achievement or Milestone]**
   → Breaks **[PATTERN_LABEL from registry]**: [one sentence]

2. [same format]

3. [same format]
```

**ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]** — numbered sub-steps [C-23]:
This gate covers unlock naming (C-05), anti-inertia format (C-12), registry labels
(C-14), and gate ID enumeration (C-20). All four checked together.

> "(1) Each action names specific namespace and topic. [C-05]
>  (2) Each action names exact unlock. [C-05]
>  (3) Format: [Action] → Unlocks [X] → Breaks [Pattern]. [C-12]
>  (4) Registry labels only — no invented labels. [C-14]
>  (5) At least 3 actions. [C-05]
>  (6) Gate label [C-05/C-12/C-14/C-20] enumerates all covered criterion IDs. [C-25]"
>
> Pass: "ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]: Passed.
>   Unlock named (C-05): confirmed. Anti-inertia format (C-12): confirmed.
>   Registry labels (C-14): confirmed. Label enumeration (C-25): [C-05/C-12/C-14/C-20] verified."
> Fail: "ACTIONS CLUSTER GATE FAIL [C-05/C-12/C-14/C-20]: action [n], condition ([n]) — [issue]."

### 2E — RECORD PHASE 2 STATE (internal)

```
PHASE 2 STATE:
  Milestones not yet earned: [list/"all earned"]
  1-away gap topics: [list/"none"]
  Implied missing topics: [list/"none"]
  Implied missing contributors: [list/"none"]
```

---

## PHASE 3 — CROSS-PHASE CORRECTION AND STRUCTURAL AUDIT

### 3A — CROSS-PHASE CONTINUITY GATE [C-24]

Before I run cross-phase correction, I confirm [C-11/C-24]:
> "I will read Phase 2 State and compare every implied topic/contributor name against
> the Phase 1 scan state. If I find a gap, I will add the missing item before writing
> the artifact — not suppress it."

**CROSS-PHASE GATE [C-24/C-01/C-02]** — numbered sub-steps [C-23]:
> "(1) Read Phase 2 State.
>  (2) Did Phase 2 gaps surface topic names absent from Phase 1 scan state? YES/NO.
>  (3) Did Phase 2 gaps surface contributors absent from Phase 1 contributor list? YES/NO.
>  (4) YES to (2): add to Phase 1B Earned/Locked with evidence or gap.
>      'CROSS-PHASE UPDATE [C-24]: topic(s) [list] added.'
>  (5) YES to (3): flag in frontmatter as `c24_missing_contributors: [list]`.
>  (6) NO to both: 'CROSS-PHASE GATE [C-24]: No additions.'
>  (7) Lists finalized."
>
> Pass: "CROSS-PHASE GATE [C-24]: Passed. Additions: [n topics / 0]."

### 3B — STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27/C-28]

Scan back through all output produced in Phases 1–2. List every gate label AND
every pre-write confirmation.

**STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27/C-28]** — numbered sub-steps [C-23]:
> "(1) List every gate label executed in this run (Phases 1–2).
>  (2) Each gate label carries at least one [C-XX] criterion ID. [C-26]
>  (3) Verify super-gates:
>      - 'LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]' — enumerates C-16, C-19, C-21. [C-27]
>      - 'ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]' — enumerates C-05, C-12, C-14, C-20. [C-27]
>  (4) List every pre-write confirmation issued in this run.
>  (5) For each pre-write confirmation: confirm it uses form
>      'Before I write [section], I confirm [C-XX]: [commitment].' [C-28]
>  (6) Missing criterion ID: 'AUDIT FAIL [C-20/C-26]: gate "[label]" missing ID.'
>  (7) Wrong super-gate enumeration: 'AUDIT FAIL [C-27]: expected [C-XX/...], found [C-XX/...].'
>  (8) Pre-write confirmation not in first-person owner form: 'AUDIT FAIL [C-28]:
>      confirmation "[text]" does not use required syntax.'
>  (9) Count: [n] gates checked, [n] confirmations checked, [n] total violations.
>  (10) All pass: 'STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27/C-28]: Passed.
>         [n] gates correct, [n] confirmations in C-28 form, super-gates verified.'
>       Any fail: 'STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27/C-28]: [n] violation(s). See findings.'"
>
> Violations are findings, not blockers.

### WRITE ARTIFACT [C-08]

Write to `simulations/corps/achievements-{{date}}.md`.

```yaml
---
skill: corps-achievements
date: {{date}}
topics_scanned: [n]
topics_added_via_cross_phase: [n or 0]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
stagnation_pattern: [PATTERN_LABEL]
c24_cross_phase_gate: [additions_made/no_additions]
c25_super_gates: ["LEADERBOARD CLUSTER [C-16/C-19/C-21]", "ACTIONS CLUSTER [C-05/C-12/C-14/C-20]"]
c26_structural_audit_gates_checked: [n]
c26_structural_audit_violations: [n or "none"]
c27_super_gate_enumeration_verified: [true/false]
c28_owner_confirmations_issued: [n]
c28_owner_confirmations_compliant: [n]
c28_violations: [n or "none"]
c21_correction_applied: [true/false/not_applicable]
c22_derivability_passed: [true/false]
phrasing_register: first-person-owner-confirmations
gate_language: numbered-substeps
---
```

---

## V-04 — Combined: Achievement-Census-First + First-Person Owner Confirmations

**Axes**: Achievement-census-first role sequence (V-01 axis) + first-person owner
confirmation phrasing (V-03 axis / C-28 testbed).
**Hypothesis**: When the topic achievement census runs before contributor attribution,
AND every pre-write gate is a first-person owner commitment, the two mechanisms
reinforce each other: the achievement-first sequence means Phase 1 owner confirmations
are about topic completeness (not contributor attribution), and Phase 2 confirmations
are about leaderboard derivation from verified achievement evidence. The ownership
syntax makes the dependency explicit — "I confirm I am deriving this contributor's
score from achievements I have already verified above" — which should produce the
fewest cross-phase attribution errors of any R10 variation.

---

You are running `corps-achievements`. Scan the workspace and compute team achievement
state. No arguments. Execute four phases in strict sequence. Phase 1 enumerates
per-topic achievements before any contributor attribution. Phase 2 derives contributor
standing from Phase 1 achievements. Before writing any section, issue a first-person
owner confirmation: "Before I write [section], I confirm [C-XX]: [commitment]."
Do not begin a phase until the previous phase's gate passes.

---

### STAGNATION PATTERN REGISTRY

| Label | Pattern |
|-------|---------|
| SOLO_ISLAND | One contributor owns all signals — no breadth |
| NAMESPACE_MOAT | All signals from one namespace — no synthesis possible |
| SPRINT_FREEZE | No new signals in current sprint — momentum stalled |
| SHALLOW_POOL | Multiple topics, none reaching Signal Depth |
| ORPHAN_TOPIC | Topics with no contributor metadata — ownership unknown |

Use label syntax `[PATTERN_LABEL from registry]`. Do not invent labels.

### SCORING FORMULA

`Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

### C-28 SYNTAX CONTRACT

Every pre-write confirmation must follow this form:
> "Before I write [section name], I confirm [C-XX]: [first-person commitment]."

---

## PHASE 1 — SCAN AND ACHIEVEMENT CENSUS

### 1A — SCAN [C-01]

Glob `simulations/**/*.md`. Extract topic path, namespace, contributor, and
signal count per topic.

```
SCAN STATE (internal):
  Topics: [list]  Namespaces: [list]  Contributors: [list]  Total signals: [n]
  Per topic: {topic: {signals: n, namespaces: [list], contributors: [list]}}
```

**SCAN GATE [C-01/C-15]** — numbered sub-steps [C-23]:
> "(1) `simulations/` accessible, >= 1 file. (2) Every file assigned to real topic path.
>  (3) Per-topic breakdown complete — signal count, namespaces, contributors per topic.
>  (4) No file skipped."
>
> Pass: "SCAN GATE [C-01]: [n] signals, [n] topics, contributors: [list]."
> Fail: "SCAN GATE FAIL [C-01/C-15]: condition ([n]) — [path or topic]."

### 1B — ACHIEVEMENT CENSUS [C-02/C-06/C-07]

Before I write the achievement census, I confirm [C-11/C-02]:
> "Every topic from scan state appears below. Missing topics: [list or 'none'].
> I am deriving all achievement evidence from the per-topic scan state breakdown
> above — not from contributor identity or estimation."

Achievement definitions: First Signal (>=1), Signal Depth (>=3), Full Sweep (>=3
namespaces), Solo Pioneer (exactly 1 contributor), Team Topic (>=2 contributors).

```markdown
## Earned Achievements — {{date}}

**[topic path]** ([n] signals, namespaces: [list], contributors: [list])
  - **[Achievement name]**: [evidence from scan state]

## Locked Achievements

**[topic path]** ([n] signals)
  - o [Achievement name]: needs [quantified gap]
```

**COMPUTE GATE [C-02/C-15]** — numbered sub-steps [C-23]:
> "(1) Topic count in Earned+Locked matches scan state. (2) Every Earned has evidence.
>  (3) Every Locked has quantified gap. (4) No achievement inferred from contributor
>      identity — all evidence from signal counts, namespaces, or file paths."
>
> Fail: "COMPUTE GATE FAIL [C-02/C-15]: condition ([n]) — [topic or instance]."

### 1C — PHASE 1 STATE (internal)

```
PHASE 1 STATE:
  Topics with >= 1 earned achievement: [list]
  Topics with zero earned achievements: [list/"none"]
  Per-topic contributor lists: {topic: [contributors], ...}
  Per-topic signal counts: {topic: n, ...}
```

---

## PHASE 2 — CONTRIBUTOR LEADERBOARD DERIVED FROM PHASE 1

### 2A — LEADERBOARD [C-04/C-16/C-19/C-21]

Before I write the contributor leaderboard, I confirm [C-11/C-04/C-16]:
> "I am building contributor scores by reading Phase 1 State per-topic contributor
> lists. I am not re-scanning the workspace. Every Signals and Topics count
> is derived from Phase 1 State — not estimated."

```markdown
## Contributor Leaderboard — Week of {{date}}

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
```

Formula: `Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

**LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]** — numbered sub-steps [C-23]:
This gate covers formula scoring (C-16), worked example (C-19), and reconciliation
loop (C-21). All three checked together — formula without example is unverifiable;
example without reconciliation cannot self-correct.

> "(1) Formula Score=(Signals×1)+(Topics×3)+(Milestones×5). [C-16]
>  (2) Contributor data sourced from Phase 1 State. [C-16]
>  (3) Worked example Rank 1: {S}×1 + {T}×3 + {M}×5 = {total}. [C-19]
>  (4) Compare {total} to Score column. [C-21]
>  (5) Mismatch: correct; state 'Corrected: {old}→{new}.' [C-21]
>  (6) Score column for Rank 1 = {total}. [C-21]
>  (7) Gate label [C-16/C-19/C-21] enumerates all covered IDs. [C-25]"
>
> Pass: "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]: Passed.
>   Formula (C-16): confirmed. Example (C-19): {total}. Reconciliation (C-21): [applied/clear].
>   Label enumeration (C-25): [C-16/C-19/C-21] verified."
> Not applicable: "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]: Not applicable — no contributors."

---

## PHASE 3 — MILESTONES, GAPS, INSIGHT, AND ACTIONS

### 3A — TEAM MILESTONES [C-03]

Before I write the milestones section, I confirm [C-11/C-03]:
> "I will use exact milestone names without paraphrase. Evidence will be specific
> file paths or contributor-topic pairs from Phase 1 State — not generic descriptions."

```markdown
## Team Milestones — {{date}}

| Milestone | Status | Evidence | Gap |
|-----------|--------|----------|-----|
| first team signal | EARNED / NOT YET | [path/"—"] | [gap/"—"] |
| shared coverage | EARNED / NOT YET | [2+contrib×2+topics/"—"] | [gap/"—"] |
| debate starter | EARNED / NOT YET | [topic+namespaces/"—"] | [gap/"—"] |
```

Update Phase 2 leaderboard Milestones column from milestone evidence above.

**MILESTONES GATE [C-03/C-15]** — numbered sub-steps [C-23]:
> "(1) Row 1 = 'first team signal'. (2) Row 2 = 'shared coverage'.
>  (3) Row 3 = 'debate starter'. (4) Evidence/Gap cells populated or '—'.
>  (5) No row name paraphrased."
>
> Fail: "MILESTONES GATE FAIL [C-03/C-15]: condition ([n]) — [row or cell]."

### 3B — 1-AWAY GAPS [C-09/C-18]

Before I write the 1-away section, I confirm [C-11/C-09]:
> "I am checking Phase 1 State per-topic signal counts and namespace lists against
> each achievement threshold. I will only list topics exactly one step away —
> not topics two or more steps away."

```markdown
## Almost There — 1-Away Gaps

| Topic / Milestone | Achievement to Unlock | Gap | Exact Action Needed |
|-------------------|-----------------------|-----|---------------------|
```

**1-AWAY GATE [C-09/C-18]** — numbered sub-steps [C-23]:
> "(1) All topics checked vs thresholds from Phase 1 State for 1-step gaps.
>  (2) All milestones checked. (3) All rows have all four columns."
>
> Fail: "1-AWAY GATE FAIL [C-09/C-18]: row '[topic]' missing column."

### 3C — TEAM INSIGHT [C-10/C-13/C-22]

Before I write the team insight, I confirm [C-11/C-10/C-22]:
> "My insight will not be derivable from any single topic in Phase 1 State.
> I will run the per-topic derivability test before committing to this insight."

**Step A**: State candidate insight with specific numbers and names.
**Step B**: Per-topic derivability — for each topic: "Can this be derived from [topic] alone? YES/NO."
**Step C**: All NO → approved. Any YES → new candidate (up to 2 attempts).

**INSIGHT GATE [C-10/C-13/C-22]** — numbered sub-steps [C-23]:
> "(1) Formatted as **TEAM INSIGHT — [descriptive name]:**. [C-13]
>  (2) Specific values — not generic. [C-10]
>  (3) Passed per-topic derivability for all topics in scan state. [C-22]"
>
> Fail: "INSIGHT GATE FAIL [C-10/C-13/C-22]: condition ([n]) — [issue]."

```markdown
**TEAM INSIGHT — [descriptive name]:** [insight sentence]
```

### 3D — NEXT ACTIONS [C-05/C-12/C-14/C-17]

Before I write the next actions section, I confirm [C-11/C-05/C-14]:
> "Each action will name a specific namespace and topic, name the exact unlock,
> use the required format, and draw its pattern label from the registry only.
> I will not invent pattern labels."

```markdown
## Next Actions

Dominant stagnation pattern: **[PATTERN_LABEL from registry]**

1. **[action — namespace and topic explicit]**
   → Unlocks **[Achievement or Milestone]**
   → Breaks **[PATTERN_LABEL from registry]**: [one sentence]

2. [same format]

3. [same format]
```

**ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]** — numbered sub-steps [C-23]:
This gate covers unlock naming (C-05), anti-inertia format (C-12), registry labels
(C-14), and gate ID enumeration (C-20). All four together.

> "(1) Each action names namespace+topic. [C-05] (2) Each names exact unlock. [C-05]
>  (3) Format [Action] → Unlocks [X] → Breaks [Pattern]. [C-12]
>  (4) Registry labels only. [C-14] (5) At least 3 actions. [C-05]
>  (6) Gate label [C-05/C-12/C-14/C-20] enumerates all covered IDs. [C-25]"
>
> Pass: "ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]: Passed.
>   Unlock named (C-05): confirmed. Anti-inertia format (C-12): confirmed.
>   Registry labels (C-14): confirmed. Label enumeration (C-25): [C-05/C-12/C-14/C-20] verified."
> Fail: "ACTIONS CLUSTER GATE FAIL [C-05/C-12/C-14/C-20]: action [n], condition ([n]) — [issue]."

### 3E — PHASE 3 STATE (internal)

```
PHASE 3 STATE:
  Milestones not yet earned: [list/"all earned"]
  1-away gap topics: [list/"none"]
  Implied missing topics: [list/"none"]
  Implied missing contributors: [list/"none"]
```

---

## PHASE 4 — CROSS-PHASE CORRECTION AND STRUCTURAL AUDIT

### 4A — CROSS-PHASE CONTINUITY GATE [C-24]

Before I run cross-phase correction, I confirm [C-11/C-24]:
> "I will compare every implied topic and contributor in Phase 3 State against
> Phase 1 scan state. I will add any missing items before writing the artifact."

**CROSS-PHASE GATE [C-24/C-01/C-02]** — numbered sub-steps [C-23]:
> "(1) Read Phase 3 State.
>  (2) Topics absent from Phase 1 scan state? YES/NO.
>  (3) Contributors absent from Phase 1 contributor list? YES/NO.
>  (4) YES to (2): add to Phase 1B with evidence or gap.
>      'CROSS-PHASE UPDATE [C-24]: topic(s) [list] added.'
>  (5) YES to (3): frontmatter `c24_missing_contributors: [list]`.
>  (6) NO to both: 'CROSS-PHASE GATE [C-24]: No additions.'
>  (7) Lists finalized."
>
> Pass: "CROSS-PHASE GATE [C-24]: Passed. Additions: [n / 0]."

### 4B — STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27/C-28]

Scan back through all output in Phases 1–3. List every gate label AND every
pre-write owner confirmation.

**STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27/C-28]** — numbered sub-steps [C-23]:
> "(1) List every gate label in this run (Phases 1–3).
>  (2) Each gate label carries at least one [C-XX] criterion ID. [C-26]
>  (3) Verify super-gates:
>      - 'LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]' — enumerates C-16, C-19, C-21. [C-27]
>      - 'ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]' — enumerates C-05, C-12, C-14, C-20. [C-27]
>  (4) List every pre-write owner confirmation in this run (Phases 1–3). [C-28]
>  (5) Each confirmation uses form 'Before I write [section], I confirm [C-XX]: [commitment].' [C-28]
>  (6) Missing criterion ID: 'AUDIT FAIL [C-20/C-26]: gate "[label]" missing ID.'
>  (7) Wrong enumeration: 'AUDIT FAIL [C-27]: expected [C-XX/...], found [C-XX/...].'
>  (8) Non-compliant confirmation: 'AUDIT FAIL [C-28]: confirmation "[text]" wrong form.'
>  (9) Count: [n] gates, [n] confirmations, [n] total violations.
>  (10) All pass: 'STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27/C-28]: Passed.
>         [n] gates correct, [n] confirmations in C-28 form, super-gates verified.'
>       Any fail: 'STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27/C-28]: [n] violation(s). See findings.'"
>
> Violations are findings, not blockers.

### WRITE ARTIFACT [C-08]

Write to `simulations/corps/achievements-{{date}}.md`.

```yaml
---
skill: corps-achievements
date: {{date}}
topics_scanned: [n]
topics_added_via_cross_phase: [n or 0]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
stagnation_pattern: [PATTERN_LABEL]
c24_cross_phase_gate: [additions_made/no_additions]
c25_super_gates: ["LEADERBOARD CLUSTER [C-16/C-19/C-21]", "ACTIONS CLUSTER [C-05/C-12/C-14/C-20]"]
c26_structural_audit_gates_checked: [n]
c26_structural_audit_violations: [n or "none"]
c27_super_gate_enumeration_verified: [true/false]
c28_owner_confirmations_issued: [n]
c28_owner_confirmations_compliant: [n]
c28_violations: [n or "none"]
c21_correction_applied: [true/false/not_applicable]
c22_derivability_passed: [true/false]
role_sequence: achievement-census-first
phrasing_register: first-person-owner-confirmations
gate_language: numbered-substeps
---
```

---

## V-05 — Combined: Per-Topic Scorecard Blocks + Gate-Failure Retry Loops

**Axes**: Per-topic scorecard blocks output format (V-02 axis) + explicit gate-failure
retry lifecycle emphasis.
**Hypothesis**: Per-topic scorecard blocks prevent topic elision at the structure level
(a missing topic is a missing named block). Gate-failure retry loops prevent silent
violations at the execution level (when a gate fails, the model has a named recovery
path instead of a proceed-with-violation path). Together they close two distinct
failure modes from orthogonal directions: structural omission (fixed by scorecards)
and silent gate bypass (fixed by retry). Neither mechanism interferes with the other.
This combination should produce the most reliable output across varied workspace sizes.

---

You are running `corps-achievements`. Scan the workspace and compute team achievement
state. No arguments. Execute three phases. Per-topic output is rendered as scorecard
blocks (one block per topic, fixed schema). If any gate fails, do not proceed —
follow the GATE-FAIL RETRY protocol below instead. Do not begin a phase until the
previous phase's gate passes.

---

### GATE-FAIL RETRY PROTOCOL

When any gate produces a FAIL verdict:

1. State: "GATE FAILED — [gate name and criterion ID]: [specific failure condition]."
2. Identify the minimum correction needed for the gate to pass.
3. State: "RETRYING: [what is being corrected]."
4. Re-execute the section that the gate covers with the correction applied.
5. Re-run the gate. If it passes: "RETRY PASSED [gate name]." Proceed.
6. If it fails again: "RETRY FAILED [gate name] — escalating."
   State the violation in the frontmatter as a finding and proceed to the next section.

---

### STAGNATION PATTERN REGISTRY

| Label | Pattern |
|-------|---------|
| SOLO_ISLAND | One contributor owns all signals — no breadth |
| NAMESPACE_MOAT | All signals from one namespace — no synthesis possible |
| SPRINT_FREEZE | No new signals in current sprint — momentum stalled |
| SHALLOW_POOL | Multiple topics, none reaching Signal Depth |
| ORPHAN_TOPIC | Topics with no contributor metadata — ownership unknown |

Use label syntax `[PATTERN_LABEL from registry]`. Do not invent labels.

### SCORING FORMULA

`Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

### SCORECARD BLOCK SCHEMA

```markdown
### Topic Scorecard: [topic path] — {{date}}

| Field | Value |
|-------|-------|
| Signals | [n] |
| Namespaces | [list] |
| Contributors | [list or "unknown"] |

**Earned:**
- [Achievement name]: [evidence]

**Locked:**
- o [Achievement name]: needs [quantified gap]
```

---

## PHASE 1 — SCAN AND TOPIC SCORECARDS

### 1A — SCAN [C-01]

Glob `simulations/**/*.md`. Extract topic path, namespace, contributor per file.

```
SCAN STATE (internal):
  Topics: [list]  Namespaces: [list]  Contributors: [list]  Total signals: [n]
```

**SCAN GATE [C-01/C-15]** — numbered sub-steps [C-23]:
> "(1) `simulations/` accessible, >= 1 file from glob.
>  (2) Every file assigned to real topic path from glob output.
>  (3) Scan state complete. (4) No file skipped."
>
> Pass: "SCAN GATE [C-01]: [n] signals, [n] topics, contributors: [list]."
> Fail: apply GATE-FAIL RETRY PROTOCOL before proceeding to 1B.

### 1B — TOPIC SCORECARDS [C-02/C-06/C-07]

**Pre-write gate [C-11]**: "Topic count in scan state: [n]. I will write exactly [n]
scorecard blocks. Missing topics from prior pass: [list or 'none']."

Achievement definitions: First Signal (>=1), Signal Depth (>=3), Full Sweep (>=3
namespaces), Solo Pioneer (exactly 1 contributor), Team Topic (>=2 contributors).

Write one scorecard block per topic using the fixed schema. Order by signal count
descending.

```markdown
## Topic Scorecards — {{date}}
```

**SCORECARD GATE [C-02/C-15]** — numbered sub-steps [C-23]:
> "(1) Block count equals topic count in scan state — count both explicitly.
>  (2) Every Earned entry has specific evidence — no bare achievement names.
>  (3) Every Locked entry has quantified gap — no 'needs more work.'
>  (4) Every block has all four fields: Signals, Namespaces, Contributors, Earned/Locked."
>
> Pass: "SCORECARD GATE [C-02/C-15]: Passed. [n] blocks = [n] topics."
> Fail: apply GATE-FAIL RETRY PROTOCOL — re-write missing or malformed blocks before proceeding.

### 1C — CONTRIBUTOR LEADERBOARD [C-04/C-16/C-19/C-21]

**Pre-write gate [C-11]**: "Contributor counts derived from scorecard block data
above — not re-scanned. Ready to write."

```markdown
## Contributor Leaderboard — Week of {{date}}

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
```

Formula: `Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

**LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]** — numbered sub-steps [C-23]:
This gate covers formula scoring (C-16), worked example (C-19), and reconciliation
loop (C-21). All three checked together.

> "(1) Formula Score=(Signals×1)+(Topics×3)+(Milestones×5). [C-16]
>  (2) Worked example Rank 1: {S}×1 + {T}×3 + {M}×5 = {total}. [C-19]
>  (3) Compare {total} to Score column. [C-21]
>  (4) Mismatch: correct; state 'Corrected: {old}→{new}.' [C-21]
>  (5) Score column for Rank 1 = {total}. [C-21]
>  (6) Gate label [C-16/C-19/C-21] enumerates all covered IDs. [C-25]"
>
> Pass: "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]: Passed.
>   Formula (C-16): confirmed. Example (C-19): {total}. Reconciliation (C-21): [applied/clear].
>   Label enumeration (C-25): [C-16/C-19/C-21] verified."
> Not applicable: "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]: Not applicable — no contributors."
> Fail: apply GATE-FAIL RETRY PROTOCOL.

---

## PHASE 2 — MILESTONES, GAPS, INSIGHT, AND ACTIONS

### 2A — TEAM MILESTONES [C-03]

```markdown
## Team Milestones — {{date}}

| Milestone | Status | Evidence | Gap |
|-----------|--------|----------|-----|
| first team signal | EARNED / NOT YET | [path/"—"] | [gap/"—"] |
| shared coverage | EARNED / NOT YET | [2+contrib×2+topics/"—"] | [gap/"—"] |
| debate starter | EARNED / NOT YET | [topic+namespaces/"—"] | [gap/"—"] |
```

**MILESTONES GATE [C-03/C-15]** — numbered sub-steps [C-23]:
> "(1) Row 1 = 'first team signal'. (2) Row 2 = 'shared coverage'.
>  (3) Row 3 = 'debate starter'. (4) Evidence/Gap cells populated or '—'.
>  (5) No row name paraphrased."
>
> Pass: "MILESTONES GATE [C-03/C-15]: Passed."
> Fail: apply GATE-FAIL RETRY PROTOCOL — identify which row(s) failed and re-write them.

### 2B — 1-AWAY GAPS [C-09/C-18]

Derive from scorecard blocks (Phase 1B) — scan each block for locked achievements
one step away.

```markdown
## Almost There — 1-Away Gaps

| Topic / Milestone | Achievement to Unlock | Gap | Exact Action Needed |
|-------------------|-----------------------|-----|---------------------|
```

**1-AWAY GATE [C-09/C-18]** — numbered sub-steps [C-23]:
> "(1) All scorecard blocks checked for exactly-1-step locked achievements.
>  (2) All milestones checked. (3) All rows have all four columns."
>
> Pass: "1-AWAY GATE [C-09/C-18]: Passed."
> Fail: apply GATE-FAIL RETRY PROTOCOL.

### 2C — TEAM INSIGHT [C-10/C-13/C-22]

**Step A**: Candidate insight citing >= 2 scorecard blocks.
**Step B**: Per-topic derivability — for each topic: "Can this be derived from [topic]
scorecard block alone? YES/NO."
**Step C**: All NO → approved. Any YES → new candidate (up to 2 attempts).

**INSIGHT GATE [C-10/C-13/C-22]** — numbered sub-steps [C-23]:
> "(1) Formatted as **TEAM INSIGHT — [name]:**. [C-13]
>  (2) Specific values. [C-10] (3) Passed per-topic derivability test. [C-22]"
>
> Pass: "INSIGHT GATE [C-10/C-13/C-22]: Passed."
> Fail: apply GATE-FAIL RETRY PROTOCOL — generate new candidate and re-run gate.

```markdown
**TEAM INSIGHT — [descriptive name]:** [insight sentence]
```

### 2D — NEXT ACTIONS [C-05/C-12/C-14/C-17]

State dominant stagnation pattern, then write actions.

```markdown
## Next Actions

Dominant stagnation pattern: **[PATTERN_LABEL from registry]**

1. **[action — namespace and topic explicit]**
   → Unlocks **[Achievement or Milestone]**
   → Breaks **[PATTERN_LABEL from registry]**: [one sentence]

2. [same format]

3. [same format]
```

**ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]** — numbered sub-steps [C-23]:
This gate covers unlock naming (C-05), anti-inertia format (C-12), registry labels
(C-14), and gate ID enumeration (C-20). All four together.

> "(1) Each action names namespace+topic. [C-05]
>  (2) Each names exact unlock. [C-05]
>  (3) Format [Action] → Unlocks [X] → Breaks [Pattern]. [C-12]
>  (4) Registry labels only. [C-14]
>  (5) At least 3 actions. [C-05]
>  (6) Gate label [C-05/C-12/C-14/C-20] enumerates all covered IDs. [C-25]"
>
> Pass: "ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]: Passed.
>   Unlock named (C-05): confirmed. Anti-inertia format (C-12): confirmed.
>   Registry labels (C-14): confirmed. Label enumeration (C-25): [C-05/C-12/C-14/C-20] verified."
> Fail: apply GATE-FAIL RETRY PROTOCOL — re-write failing action rows and re-run gate.

### 2E — RECORD PHASE 2 STATE (internal)

```
PHASE 2 STATE:
  Milestones not yet earned: [list/"all earned"]
  1-away gap topics: [list/"none"]
  Implied missing topics: [list/"none"]
  Implied missing namespaces: [list/"none"]
  Retry events this run: [list of "gate name: retry-passed/retry-failed" or "none"]
```

---

## PHASE 3 — CROSS-PHASE CORRECTION AND STRUCTURAL AUDIT

### 3A — CROSS-PHASE CONTINUITY GATE [C-24]

**CROSS-PHASE GATE [C-24/C-01/C-02]** — numbered sub-steps [C-23]:
> "(1) Read Phase 2 State.
>  (2) Topics absent from Phase 1 scan state? YES/NO.
>  (3) Namespaces implied but absent from Phase 1 namespace list? YES/NO.
>  (4) YES to (2): write new scorecard block(s) for missing topics.
>      'CROSS-PHASE UPDATE [C-24]: scorecard block(s) added for [list].'
>  (5) YES to (3): frontmatter `c24_namespace_gaps: [list]`.
>  (6) NO to both: 'CROSS-PHASE GATE [C-24]: No additions.'
>  (7) Scorecard count finalized."
>
> Pass: "CROSS-PHASE GATE [C-24]: Passed. Additions: [n blocks / 0]."
> Fail: apply GATE-FAIL RETRY PROTOCOL.

### 3B — STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]

Scan back through all output in Phases 1–2, including any GATE-FAIL RETRY events.
List every gate label and every retry event.

**STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]** — numbered sub-steps [C-23]:
> "(1) List every gate label executed in this run (Phases 1–2), including retry gates.
>  (2) Each gate label carries at least one [C-XX] criterion ID. [C-26]
>  (3) Verify super-gates:
>      - 'LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]' — enumerates C-16, C-19, C-21. [C-27]
>      - 'ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]' — enumerates C-05, C-12, C-14, C-20. [C-27]
>  (4) For each retry event: confirm the retry gate carried the same criterion ID as the
>      original gate label.
>  (5) Missing criterion ID: 'AUDIT FAIL [C-20/C-26]: gate "[label]" missing ID.'
>  (6) Wrong enumeration: 'AUDIT FAIL [C-27]: expected [C-XX/...], found [C-XX/...].'
>  (7) Count: [n] gate executions (including retries), [n] correct, [n] violations.
>  (8) All pass: 'STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]: Passed. [n] executions correct,
>        super-gates [C-16/C-19/C-21] and [C-05/C-12/C-14/C-20] enumeration verified.'
>      Any fail: 'STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]: [n] violation(s). See findings.'"
>
> Violations are findings, not blockers.

### WRITE ARTIFACT [C-08]

Write to `simulations/corps/achievements-{{date}}.md`.

```yaml
---
skill: corps-achievements
date: {{date}}
topics_scanned: [n]
topics_added_via_cross_phase: [n or 0]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
stagnation_pattern: [PATTERN_LABEL]
c24_cross_phase_gate: [additions_made/no_additions]
c24_namespace_gaps: [list or "none"]
c25_super_gates: ["LEADERBOARD CLUSTER [C-16/C-19/C-21]", "ACTIONS CLUSTER [C-05/C-12/C-14/C-20]"]
c26_structural_audit_gates_checked: [n]
c26_structural_audit_violations: [n or "none"]
c27_super_gate_enumeration_verified: [true/false]
c21_correction_applied: [true/false/not_applicable]
c22_derivability_passed: [true/false]
output_format: per-topic-scorecard-blocks
lifecycle_emphasis: gate-failure-retry-loops
retry_events: [list or "none"]
gate_language: numbered-substeps
---
```
```

---

That's the complete R10 variate document. Here's the summary of what each variation tests and why it's new relative to R9:

| Variation | Axis | What R9 Covered | What R10 Tests Differently |
|-----------|------|-----------------|----------------------------|
| V-01 | Role sequence: achievement-census-first | R9 V-01: leaderboard-first | Inverts the dependency — leaderboard derives from achievement evidence, not the other way around |
| V-02 | Output format: per-topic scorecard blocks | R9 V-02: dense global tables | Moves structural completeness guarantee from row-count to block-count — missing topic = missing named block |
| V-03 | Phrasing register: first-person owner confirmations (C-28 testbed) | R9 V-05: warm/conversational | Isolates C-28 as a distinct structural pattern from "conversational tone" — ownership syntax vs warmth |
| V-04 | Combined: achievement-census-first + first-person ownership | R9 V-04: leaderboard-first + stagnation-first + STOP barriers | Combines the two dependency-direction fixes: topic-first sequence + owner-commitment gates |
| V-05 | Combined: per-topic scorecards + gate-failure retry loops | R9 V-05: dense tables + conversational | Closes two orthogonal failure modes: structural omission (scorecards) + silent gate bypass (retry protocol) |
