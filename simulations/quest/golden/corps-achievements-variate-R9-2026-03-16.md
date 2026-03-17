---
skill: quest-variate
skill_target: corps-achievements
round: 9
date: 2026-03-16
rubric_version: 8
basis: V-05 R8 scored 100 on v8 rubric; R9 explores five style axes with full C-27/C-28 baseline
---

# Variate R9 — corps-achievements

5 complete prompt body variations for the `corps-achievements` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

R8 established C-27/C-28 as the new excellence tier. V-05 R8 scored 100 by integrating both
into the structural audit gate (super-gate name + exact IDs in C-27; "Label enumeration (C-25):
[...] verified." line item in pass confirmations for C-28). R9 carries that baseline across
all five variations and explores stylistic axes to find which presentation register is most
consistent and reliable in execution.

All variations carry the full v8 baseline: essential C-01—C-05, recommended C-06—C-08,
and aspirational C-09—C-28. The variation is in role sequence, output format,
lifecycle emphasis, phrasing register, and inertia framing — not in gate coverage.

---

## Variation Axes Selected

| Axis | Hypothesis | Used In |
|------|------------|---------|
| Role sequence: Leaderboard-first | Computing contributor standing before per-topic achievements anchors the model in team-wide attribution before drilling per-topic detail — reducing per-topic hallucination by requiring contributor data to exist first | V-01, V-04 |
| Output format: Dense table, prose-minimized | Eliminating prose in favor of table cells forces every claim into an individually checkable column — no vague summaries possible when data must fit a cell | V-02, V-05 |
| Inertia framing: Stagnation-first | Diagnosing the dominant stagnation pattern before scanning for achievements reverses the evaluative frame from celebration to correction — the team learns what they are NOT doing before confirming what they ARE doing | V-03, V-04 |
| Lifecycle emphasis: Explicit phase barriers | "STOP. Phase N complete. Do not read Phase N+1 instructions until the gate above passes." language prevents cross-phase contamination where later-phase context bleeds back into earlier-phase outputs | V-04 |
| Phrasing register: Conversational | Warm narrative framing connecting data to team context makes the output useful in standups and retros while retaining all verification gates | V-05 |

---

## Shared Resources (all variations reference these)

### Stagnation Pattern Registry

All variations draw anti-inertia actions from this registry. Use label syntax
`[PATTERN_LABEL from registry]` in action rows.

| Label | Pattern |
|-------|---------|
| SOLO_ISLAND | One contributor owns all signals — no team breadth or coverage diversity |
| NAMESPACE_MOAT | All signals from one namespace — no cross-namespace synthesis possible |
| SPRINT_FREEZE | No new signals added in the current sprint window — momentum stalled |
| SHALLOW_POOL | Multiple topics with <3 signals each — Signal Depth unreached across the board |
| ORPHAN_TOPIC | Topics exist with no contributor metadata — ownership and accountability unknown |

### Weighted Scoring Formula

All variations use this formula for the contributor leaderboard (C-16):

```
Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)
```

Where:
- **Signals** = total signal files attributed to this contributor
- **Topics** = count of distinct topics the contributor has contributed to
- **Milestones** = count of the three team milestones this contributor's work provided evidence toward

---

## V-01 — Role Sequence: Leaderboard-First

**Axis**: Role sequence — contributor leaderboard computed in Phase 1 (immediately after scan),
before per-topic achievement enumeration in Phase 2. Milestones in Phase 3. Synthesis in Phase 4.
**Hypothesis**: When the leaderboard is built first, every subsequent section inherits the
contributor attribution structure — achievements have contributor names before they need them,
and milestones can reference contributor counts from a live table rather than reconstructing
attribution from scratch. This creates a contributor-centric frame that reduces per-topic
hallucination by requiring contributor data to exist and be verified before achievement
enumeration begins.

---

You are running `corps-achievements`. Scan the workspace and compute team achievement state.
No arguments. Execute four phases in sequence. Do not begin a phase until the previous phase's
gate passes. Phase 4 contains the cross-phase continuity gate and final structural audit.

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

## PHASE 1 — SCAN AND CONTRIBUTOR LEADERBOARD

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
> Fail: "SCAN GATE FAIL [C-01/C-15]: condition ([n]) — [specific path or file]."

### 1B — CONTRIBUTOR LEADERBOARD AND FORMULA VERIFICATION

**Pre-write gate [C-11]**: "Are Signals/Topics/Milestones counts per contributor derived from
the scan state above — not estimated? If not, derive them before writing the table."

```markdown
## Contributor Leaderboard — Week of {{date}}

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
```

Formula: `Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

**LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]** — numbered sub-steps [C-23]:
This gate covers three interdependent leaderboard criteria: formula-driven scoring (C-16),
worked example render (C-19), and reconciliation correction loop (C-21). All three checked
together because C-19 without C-21 is display without enforcement, and C-16 without C-19 is
a formula claim that cannot be verified from the output alone.

> "(1) Leaderboard uses explicit formula Score=(Signals×1)+(Topics×3)+(Milestones×5) — not
>      a raw count rank. [C-16]
>  (2) Worked example for Rank 1: Score = {S}×1 + {T}×3 + {M}×5 = {total}. [C-19]
>  (3) Compare {total} to Score column for Rank 1. [C-21]
>  (4) If mismatch: correct Score column to {total}; state 'Corrected: {old}→{new}.' [C-21]
>  (5) Score column for Rank 1 now equals {total}. [C-21]
>  (6) This gate label [C-16/C-19/C-21] enumerates all criterion IDs it covers. [C-25]"
>
> Pass: "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]: Passed.
>   Formula (C-16): confirmed. Example (C-19): {total}. Reconciliation (C-21): [applied/clear].
>   Label enumeration (C-25): [C-16/C-19/C-21] verified."
> Not applicable: "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]: Not applicable — no contributors."

---

## PHASE 2 — ACHIEVEMENTS

### 2A — PER-TOPIC ACHIEVEMENTS [C-02/C-06/C-07]

**Pre-write gate [C-11]**: "Do all topics from scan state appear in either Earned or Locked
below? If not, identify the missing topic and add it before generating the section."

Achievement definitions (apply to each topic):

| Achievement | Condition |
|-------------|-----------|
| First Signal | >= 1 signal for this topic |
| Signal Depth | >= 3 signals for this topic |
| Full Sweep | signals span >= 3 distinct namespaces for this topic |
| Solo Pioneer | exactly 1 contributor, >= 1 signal |
| Team Topic | >= 2 contributors, >= 1 signal each |

Contributor names from Phase 1 leaderboard are available — use them in evidence cells.

```markdown
## Earned Achievements — {{date}}

**[topic path]** ([n] signals)
  - **[Achievement name]**: [evidence — counts, contributor names from Phase 1, or namespace list]

## Locked Achievements

**[topic path]** ([n] signals)
  - o [Achievement name]: needs [quantified gap — "2 more signals", "1 more namespace", etc.]
```

**COMPUTE GATE [C-02/C-15]** — numbered sub-steps [C-23]:
> "(1) Every topic in scan state appears in Earned or Locked — count must match scan state total.
>  (2) Every Earned entry names specific evidence — no bare achievement names without evidence.
>  (3) Every Locked entry quantifies the gap with a specific count or target.
>  (4) Contributor names in evidence cells match Phase 1 leaderboard."
>
> Fail: "COMPUTE GATE FAIL [C-02/C-15]: condition ([n]) — [specific topic or instance]."

### 2B — RECORD PHASE 2 STATE (internal)

```
PHASE 2 STATE:
  Achievements earned per topic: [list]
  Topics with no earned achievements: [list/"none"]
  Topics needing 1 more signal for depth: [list/"none"]
  Topics needing 1 more namespace for Full Sweep: [list/"none"]
```

---

## PHASE 3 — MILESTONES AND 1-AWAY GAPS

### 3A — TEAM MILESTONES [C-03]

```markdown
## Team Milestones — {{date}}

| Milestone | Status | Evidence | Gap |
|-----------|--------|----------|-----|
| first team signal | EARNED / NOT YET | [path/"—"] | [gap/"—"] |
| shared coverage | EARNED / NOT YET | [2+contrib×2+topics/"—"] | [gap/"—"] |
| debate starter | EARNED / NOT YET | [topic+namespaces/"—"] | [gap/"—"] |
```

Definitions: first team signal = any file found; shared coverage = 2+ contributors × 2+ topics
each; debate starter = 1 topic × 3+ distinct namespaces.

**MILESTONES GATE [C-03/C-15]** — numbered sub-steps [C-23]:
> "(1) Row 1 = 'first team signal'. (2) Row 2 = 'shared coverage'. (3) Row 3 = 'debate starter'.
>  (4) All Evidence cells populated or '—'. (5) No milestone row name paraphrased."
>
> Fail: "MILESTONES GATE FAIL [C-03/C-15]: condition ([n]) — [milestone name or row issue]."

### 3B — 1-AWAY GAPS [C-09/C-18]

```markdown
## Almost There — 1-Away Gaps

| Topic / Milestone | Achievement to Unlock | Gap | Exact Action Needed |
|-------------------|-----------------------|-----|---------------------|
```

**1-AWAY GATE [C-09/C-18]** — numbered sub-steps [C-23]:
> "(1) Checked all topics vs all achievement thresholds for exactly-1-step gaps.
>  (2) Checked all milestones for 1-step gaps.
>  (3) All table rows have all four columns populated."
>
> Fail: "1-AWAY GATE FAIL [C-09/C-18]: row '[topic]' missing column."

### 3C — RECORD PHASE 3 STATE (internal)

```
PHASE 3 STATE:
  Milestones not yet earned: [list/"all earned"]
  1-away gap topics: [list/"none"]
  Implied missing topics: [list/"none"]
  Implied missing contributors: [list/"none"]
```

---

## PHASE 4 — SYNTHESIS, CROSS-PHASE CORRECTION, AND STRUCTURAL AUDIT

### 4A — NEXT ACTIONS [C-05/C-12/C-14/C-17]

State dominant stagnation pattern from registry before writing actions.

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
This gate covers four interdependent next-action criteria: unlock naming (C-05), anti-inertia
format (C-12), registry-drawn labels (C-14), and gate ID enumeration (C-20). These four are
checked together because C-12's format requires C-14's label, and C-14's registry sourcing is
only verifiable when C-20's gate label exposes the dependency.

> "(1) Each action names a specific namespace and topic — not generic advice. [C-05]
>  (2) Each action names the exact achievement or milestone it unlocks. [C-05]
>  (3) Each action uses format [Action] → Unlocks [Achievement] → Breaks [Pattern]. [C-12]
>  (4) Every pattern label drawn from the Stagnation Pattern Registry — no invented labels. [C-14]
>  (5) At least 3 actions written. [C-05]
>  (6) This gate label [C-05/C-12/C-14/C-20] enumerates all criterion IDs it covers. [C-25]"
>
> Pass: "ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]: Passed.
>   Unlock named (C-05): confirmed. Anti-inertia format (C-12): confirmed.
>   Registry labels (C-14): confirmed. Label enumeration (C-25): [C-05/C-12/C-14/C-20] verified."
> Fail: "ACTIONS CLUSTER GATE FAIL [C-05/C-12/C-14/C-20]: action [n], condition ([n]) — [issue]."

### 4B — TEAM INSIGHT [C-10/C-13/C-22]

**Step A**: State candidate insight in one sentence with specific numbers and names.
**Step B**: For each topic in scan state: "Can this insight be derived from [topic] alone? YES/NO"
**Step C**: All NO → approved. Any YES → discard and generate a new candidate (up to 2 attempts).
**Step D**: Confirm the approved insight differs from any stagnation pattern or gap statement
already made in this run.

**INSIGHT GATE [C-10/C-13/C-22]** — numbered sub-steps [C-23]:
> "(1) Insight formatted as **TEAM INSIGHT — [descriptive name]:**. [C-13]
>  (2) Names specific topics, contributors, or numeric values — not generic. [C-10]
>  (3) Passed derivability elimination — single-topic test run for each topic in scan state. [C-22]
>  (4) Differs from stagnation pattern statement or gap statement already written above. [C-10]"
>
> Fail: "INSIGHT GATE FAIL [C-10/C-13/C-22]: condition ([n]) — [specific issue]."

```markdown
**TEAM INSIGHT — [descriptive name]:** [insight sentence]
```

### 4C — CROSS-PHASE CONTINUITY GATE [C-24]

**CROSS-PHASE GATE [C-24/C-01/C-02]** — numbered sub-steps [C-23]:
> "(1) Read Phase 3 State: milestone gaps, 1-away topics, implied missing topics/contributors.
>  (2) Did Phase 3 gaps surface topic names absent from Phase 1 scan state? YES/NO.
>  (3) Did Phase 3 gaps surface contributor names absent from Phase 1 leaderboard? YES/NO.
>  (4) YES to (2): add missing topics to Phase 2 Earned/Locked section with evidence or gap.
>      State: 'CROSS-PHASE UPDATE [C-24]: topic(s) [list] added from Phase 3 gap analysis.'
>  (5) YES to (3): flag contributor in frontmatter as `c24_missing_contributors: [list]`.
>  (6) NO to both: 'CROSS-PHASE GATE [C-24]: No Phase 3 additions to Phase 1/2 output.'
>  (7) Phase 1 topic list and Phase 2 achievement list are now finalized."
>
> Pass: "CROSS-PHASE GATE [C-24]: Passed. Additions: [n topics / 0]."

### 4D — STRUCTURAL AUDIT GATE [C-20/C-26]

After the cross-phase gate and before writing the artifact, audit every gate label
produced in this run. Scan back through the output of all four phases.

**STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]** — numbered sub-steps [C-23]:
> "(1) List every gate label executed in this run (read back through Phases 1–4).
>  (2) For each gate label: confirm it carries at least one [C-XX] criterion ID reference.
>  (3) Pay specific attention to the two multi-criterion super-gates — verify each by full
>      label name and exact IDs expected:
>      - 'LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]' — confirm label enumerates C-16, C-19, C-21.
>      - 'ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]' — confirm label enumerates C-05, C-12, C-14, C-20.
>  (4) Any gate label missing a criterion ID: state
>      'AUDIT FAIL [C-20/C-26]: gate "[full label]" missing criterion ID reference.'
>  (5) Any super-gate with wrong enumeration: state
>      'AUDIT FAIL [C-27]: gate "[label]" — expected [C-XX/C-XX/...], found [C-XX/C-XX/...].'
>  (6) Count: [n] gates audited, [n] correct, [n] violations.
>  (7) State outcome:
>      All pass: 'STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]: Passed. [n] gates correct,
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
role_sequence: leaderboard-first
gate_language: numbered-substeps
---
```

---

## V-02 — Output Format: Dense Table, Prose-Minimized

**Axis**: Output format — all output sections rendered as tables with explicit column headers.
Narrative prose reduced to gate instructions and phase headers only. Achievement section,
milestone section, insight, and next actions are all table-rendered.
**Hypothesis**: When every claim must occupy a named table column, the model cannot produce
vague summaries or omit required fields. A blank cell in a structured table is visually
obvious; a missing phrase in prose is invisible. Dense table format trades readability for
structural completeness — every row is individually checkable against its column contract.

---

You are running `corps-achievements`. Scan the workspace and compute team achievement state.
No arguments. Execute three phases in sequence. All output is rendered as tables with
explicit column headers. Do not begin a phase until the previous phase's gate passes.

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

## PHASE 1 — SCAN AND COMPUTE

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
> Fail: "SCAN GATE FAIL [C-01/C-15]: condition ([n]) — [specific path]."

### 1B — ACHIEVEMENTS TABLE [C-02/C-06/C-07]

**Pre-write gate [C-11]**: "Does the topic count below match the scan state topic count?
If not, add missing topics before generating the table."

Achievement definitions: First Signal (>=1 signal), Signal Depth (>=3 signals),
Full Sweep (>=3 namespaces), Solo Pioneer (exactly 1 contributor), Team Topic (>=2 contributors).

Render two explicitly labeled sections (C-06, C-07):

```markdown
## Earned Achievements — {{date}}

| Topic | Achievement | Evidence |
|-------|-------------|----------|
| [topic] | [achievement name] | [counts, names, or namespace list] |

## Locked Achievements

| Topic | Achievement | Gap (exact count or target) |
|-------|-------------|------------------------------|
| [topic] | [achievement name] | [e.g., "2 more signals", "1 more namespace"] |
```

**COMPUTE GATE [C-02/C-15]** — numbered sub-steps [C-23]:
> "(1) Topic count in Earned+Locked tables matches scan state total.
>  (2) Every Earned row has Evidence populated — no empty cells.
>  (3) Every Locked row has Gap populated with a specific count or target."
>
> Fail: "COMPUTE GATE FAIL [C-02/C-15]: condition ([n]) — [specific topic or row]."

### 1C — CONTRIBUTOR LEADERBOARD TABLE [C-04/C-16/C-19/C-21]

**Pre-write gate [C-11]**: "Are Signals/Topics/Milestones counts per contributor derived
from scan state — not estimated? Confirm before writing."

```markdown
## Contributor Leaderboard — Week of {{date}}

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
```

Formula: `Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

**LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]** — numbered sub-steps [C-23]:
This gate covers formula-driven scoring (C-16), worked example render (C-19), and
reconciliation correction loop (C-21). All three checked together — C-19 without C-21
is display without enforcement; C-16 without C-19 is an unverifiable claim.

> "(1) Leaderboard uses formula Score=(Signals×1)+(Topics×3)+(Milestones×5) — not raw count. [C-16]
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

## PHASE 2 — MILESTONES, GAPS, AND ACTIONS

### 2A — MILESTONES TABLE [C-03]

```markdown
## Team Milestones — {{date}}

| Milestone | Status | Evidence | Gap |
|-----------|--------|----------|-----|
| first team signal | EARNED / NOT YET | [path or "—"] | [gap or "—"] |
| shared coverage | EARNED / NOT YET | [2+contrib×2+topics or "—"] | [gap or "—"] |
| debate starter | EARNED / NOT YET | [topic+namespaces or "—"] | [gap or "—"] |
```

**MILESTONES GATE [C-03/C-15]** — numbered sub-steps [C-23]:
> "(1) Row 1 = 'first team signal'. (2) Row 2 = 'shared coverage'. (3) Row 3 = 'debate starter'.
>  (4) All Evidence and Gap cells populated or '—'. (5) No row name paraphrased."
>
> Fail: "MILESTONES GATE FAIL [C-03/C-15]: condition ([n]) — [row name or cell issue]."

### 2B — 1-AWAY GAPS TABLE [C-09/C-18]

```markdown
## Almost There — 1-Away Gaps

| Topic / Milestone | Achievement to Unlock | Gap | Exact Action Needed |
|-------------------|-----------------------|-----|---------------------|
```

**1-AWAY GATE [C-09/C-18]** — numbered sub-steps [C-23]:
> "(1) Checked all topics vs all achievement thresholds for exactly-1-step gaps.
>  (2) Checked all milestones for 1-step gaps.
>  (3) Every row has all four columns populated."
>
> Fail: "1-AWAY GATE FAIL [C-09/C-18]: row '[topic]' missing column."

### 2C — TEAM INSIGHT ROW [C-10/C-13/C-22]

**Step A**: State candidate insight in one sentence with specific numbers and names.
**Step B**: Per-topic derivability test — for each topic: "Can this be derived from [topic] alone? YES/NO"
**Step C**: All NO → approved. Any YES → generate new candidate (up to 2 attempts).

**INSIGHT GATE [C-10/C-13/C-22]** — numbered sub-steps [C-23]:
> "(1) Insight formatted as **TEAM INSIGHT — [descriptive name]:**. [C-13]
>  (2) Names specific topics, contributors, or numeric values. [C-10]
>  (3) Passed per-topic derivability elimination for all topics in scan state. [C-22]"
>
> Fail: "INSIGHT GATE FAIL [C-10/C-13/C-22]: condition ([n]) — [specific issue]."

```markdown
**TEAM INSIGHT — [descriptive name]:** [insight sentence]
```

### 2D — NEXT ACTIONS TABLE [C-05/C-12/C-14/C-17]

State dominant stagnation pattern from registry, then render actions as a table.

```markdown
## Next Actions

Dominant stagnation pattern: **[PATTERN_LABEL from registry]**

| # | Action (namespace + topic explicit) | Unlocks | Breaks (from registry) |
|---|-------------------------------------|---------|------------------------|
| 1 | [action] | [Achievement/Milestone] | [PATTERN_LABEL from registry] |
| 2 | [action] | [Achievement/Milestone] | [PATTERN_LABEL from registry] |
| 3 | [action] | [Achievement/Milestone] | [PATTERN_LABEL from registry] |
```

**ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]** — numbered sub-steps [C-23]:
This gate covers unlock naming (C-05), anti-inertia format (C-12), registry labels (C-14),
and gate ID enumeration (C-20). All four are checked together — C-12 requires C-14, and
C-14 is only verifiable when C-20 exposes the dependency in the gate label.

> "(1) Each action row names specific namespace and topic. [C-05]
>  (2) Each action row names exact unlock in Unlocks column. [C-05]
>  (3) Each action row has a Breaks entry from the registry — no invented labels. [C-14]
>  (4) At least 3 action rows. [C-05]
>  (5) Gate label [C-05/C-12/C-14/C-20] enumerates all covered criterion IDs. [C-25]"
>
> Pass: "ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]: Passed.
>   Unlock named (C-05): confirmed. Anti-inertia format (C-12): confirmed.
>   Registry labels (C-14): confirmed. Label enumeration (C-25): [C-05/C-12/C-14/C-20] verified."
> Fail: "ACTIONS CLUSTER GATE FAIL [C-05/C-12/C-14/C-20]: row [n], condition ([n]) — [issue]."

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
> "(1) Read Phase 2 State: milestone gaps, 1-away topics, implied missing topics/namespaces.
>  (2) Did Phase 2 gaps surface topic names absent from Phase 1 topic scan state? YES/NO.
>  (3) Did Phase 2 gaps imply namespaces absent from Phase 1 namespace list? YES/NO.
>  (4) YES to (2): add missing topics to Phase 1 Achievements tables with evidence or gap.
>      State: 'CROSS-PHASE UPDATE [C-24]: topic(s) [list] added from Phase 2 gap analysis.'
>  (5) YES to (3): record in frontmatter as `c24_namespace_gaps: [list]`.
>  (6) NO to both: 'CROSS-PHASE GATE [C-24]: No Phase 2 additions to Phase 1 output.'
>  (7) Phase 1 topic list finalized."
>
> Pass: "CROSS-PHASE GATE [C-24]: Passed. Additions: [n topics / 0]."

### 3B — STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]

Scan back through all output produced in Phases 1 and 2. List every gate label.

**STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]** — numbered sub-steps [C-23]:
> "(1) List every gate label executed in this run (read back through Phases 1–2 output).
>  (2) For each gate label: confirm it carries at least one [C-XX] criterion ID reference.
>  (3) Verify each multi-criterion super-gate by full label name and exact IDs expected:
>      - 'LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]' — confirm label enumerates C-16, C-19, C-21.
>      - 'ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]' — confirm label enumerates C-05, C-12, C-14, C-20.
>  (4) Any gate missing criterion ID: 'AUDIT FAIL [C-20/C-26]: gate "[label]" missing ID.'
>  (5) Any super-gate with wrong enumeration: 'AUDIT FAIL [C-27]: gate "[label]" — expected
>      [C-XX/...], found [C-XX/...].'
>  (6) Count: [n] gates audited, [n] correct, [n] violations.
>  (7) State outcome:
>      All pass: 'STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]: Passed. [n] gates correct,
>        super-gate enumeration verified for [C-16/C-19/C-21] and [C-05/C-12/C-14/C-20].'
>      Any fail: 'STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]: [n] violation(s). See findings.'"
>
> Violations are findings, not blockers. Record in frontmatter and proceed.

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
output_format: dense-table
gate_language: numbered-substeps
---
```

---

## V-03 — Inertia Framing: Stagnation-First

**Axis**: Inertia framing — the stagnation pattern diagnosis runs as Phase 0 before any
achievement computation. The model identifies what pattern the team is currently locked in
before it enumerates what has been accomplished. The dominant pattern becomes the organizing
frame for all subsequent sections.
**Hypothesis**: Diagnosing stagnation first changes the evaluative posture from "here is what
we've done, and here is what we haven't done yet" to "here is why the team is stuck, and here
is the evidence showing how stuck we are." This reversal produces more actionable outputs
because every achievement or gap is interpreted through the lens of the named pattern, making
the next actions feel consequential rather than mechanical.

---

You are running `corps-achievements`. Scan the workspace and compute team achievement state.
No arguments. Begin with a stagnation diagnosis before computing achievements. Execute four
phases in sequence. Phase 0 is the stagnation diagnosis. Phases 1–3 follow the pattern frame
established in Phase 0. Phase 3 contains cross-phase continuity and structural audit.

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

## PHASE 0 — STAGNATION DIAGNOSIS

Before computing achievements, perform a lightweight pattern diagnosis from the workspace
directory structure and file metadata alone (no content reading required).

**Preliminary scan**: Glob `simulations/**/*.md`. Record:
- Total signal count
- Distinct contributor count (from filenames or frontmatter author fields)
- Distinct namespace count (first subdirectory segment)
- Date of most recent signal file

**STAGNATION DIAGNOSIS GATE [C-14/C-17]** — numbered sub-steps [C-23]:
> "(1) Does contributor count = 1? → candidate pattern: SOLO_ISLAND.
>  (2) Does namespace count = 1? → candidate pattern: NAMESPACE_MOAT.
>  (3) Is most recent signal file > 7 days ago? → candidate pattern: SPRINT_FREEZE.
>  (4) Are total signals < (topic count × 3)? → candidate pattern: SHALLOW_POOL.
>  (5) Are any contributor fields absent or 'unknown'? → candidate pattern: ORPHAN_TOPIC.
>  (6) Select the single dominant pattern (most strongly evidenced from (1)–(5)).
>  (7) All pattern labels drawn from the registry above — no invented labels. [C-14]
>  (8) Pattern label is a semantic name encoding pattern type without a definition lookup. [C-17]"
>
> Pass: "STAGNATION DIAGNOSIS GATE [C-14/C-17]: Dominant pattern = [PATTERN_LABEL].
>   Evidence: [which condition(s) triggered it]."
> Fail: "STAGNATION DIAGNOSIS GATE FAIL [C-14/C-17]: condition ([n]) — [specific issue]."

State the dominant pattern prominently:

```markdown
## Team Stagnation Diagnosis — {{date}}

**Dominant pattern: [PATTERN_LABEL from registry]**
[One sentence explaining the evidence for this pattern from the preliminary scan.]

*All achievements, gaps, and next actions below are interpreted through this pattern frame.*
```

---

## PHASE 1 — FULL SCAN AND COMPUTE

### 1A — SCAN [C-01]

Full glob `simulations/**/*.md`. Extract topic path, namespace, contributor per file.

```
SCAN STATE (internal):
  Topics: [list]  Namespaces: [list]  Contributors: [list]  Total signals: [n]
  Pattern frame: [PATTERN_LABEL from Phase 0]
```

**SCAN GATE [C-01/C-15]** — numbered sub-steps [C-23]:
> "(1) `simulations/` accessible, >= 1 file from glob.
>  (2) Every file assigned to a real topic path from glob output.
>  (3) Scan state complete including pattern frame field. (4) No file skipped."
>
> Pass: "SCAN GATE [C-01]: [n] signals, [n] topics, contributors: [list]."
> Fail: "SCAN GATE FAIL [C-01/C-15]: condition ([n]) — [specific path]."

### 1B — ACHIEVEMENTS [C-02/C-06/C-07]

**Pre-write gate [C-11]**: "Do all topics from scan state appear below? If not, add before writing.
Does the stagnation pattern frame explain why any topics have only Locked achievements?"

Achievement definitions: First Signal (>=1), Signal Depth (>=3), Full Sweep (>=3 namespaces),
Solo Pioneer (1 contributor), Team Topic (>=2 contributors each with >=1 signal).

```markdown
## Earned Achievements — {{date}}
*(Pattern context: [PATTERN_LABEL] — achievements earned despite this pattern)*

**[topic path]** ([n] signals)
  - **[Achievement]**: [evidence]

## Locked Achievements
*(Pattern context: [PATTERN_LABEL] — achievements blocked by this pattern)*

**[topic path]** ([n] signals)
  - o [Achievement]: needs [quantified gap] — *pattern link: [PATTERN_LABEL explains why]*
```

**COMPUTE GATE [C-02/C-15]** — numbered sub-steps [C-23]:
> "(1) Every scan-state topic in Earned or Locked — count must match.
>  (2) Every Earned has specific evidence.
>  (3) Every Locked has specific quantified gap.
>  (4) At least one Locked entry connects gap to stagnation pattern."
>
> Fail: "COMPUTE GATE FAIL [C-02/C-15]: condition ([n]) — [specific topic or instance]."

### 1C — CONTRIBUTOR LEADERBOARD [C-04/C-16/C-19/C-21]

**Pre-write gate [C-11]**: "Are contributor counts derived from scan state? Does the
dominant stagnation pattern predict the leaderboard shape (e.g., SOLO_ISLAND → top score
dominates; ORPHAN_TOPIC → many 'unknown' contributors)?"

```markdown
## Contributor Leaderboard — Week of {{date}}

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
```

Formula: `Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

**LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]** — numbered sub-steps [C-23]:
This gate covers formula-driven scoring (C-16), worked example render (C-19), and
reconciliation correction loop (C-21). All three checked together.

> "(1) Leaderboard uses explicit formula — not raw count rank. [C-16]
>  (2) Worked example for Rank 1: Score = {S}×1 + {T}×3 + {M}×5 = {total}. [C-19]
>  (3) Compare {total} to Score column for Rank 1. [C-21]
>  (4) If mismatch: correct and state 'Corrected: {old}→{new}.' [C-21]
>  (5) Score column for Rank 1 = {total}. [C-21]
>  (6) Gate label [C-16/C-19/C-21] enumerates all covered IDs. [C-25]"
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
> "(1) Row 1 = 'first team signal'. (2) Row 2 = 'shared coverage'. (3) Row 3 = 'debate starter'.
>  (4) All Evidence and Gap cells populated or '—'."
>
> Fail: "MILESTONES GATE FAIL [C-03/C-15]: condition ([n]) — [row or cell issue]."

### 2B — 1-AWAY GAPS [C-09/C-18]

```markdown
## Almost There — 1-Away Gaps

| Topic / Milestone | Achievement to Unlock | Gap | Exact Action Needed |
|-------------------|-----------------------|-----|---------------------|
```

**1-AWAY GATE [C-09/C-18]** — numbered sub-steps [C-23]:
> "(1) Checked all topics vs all thresholds for exactly-1-step gaps.
>  (2) Checked all milestones for 1-step gaps.
>  (3) All rows have all four columns."
>
> Fail: "1-AWAY GATE FAIL [C-09/C-18]: row '[topic]' missing column."

### 2C — TEAM INSIGHT [C-10/C-13/C-22]

**Step A**: State candidate insight — it must relate to the stagnation pattern frame but
must NOT simply restate it.
**Step B**: Per-topic derivability test — for each topic: "Can this be derived from [topic] alone? YES/NO"
**Step C**: All NO → approved. Any YES → generate new candidate (up to 2 attempts).
**Step D**: Confirm the insight is distinct from the Phase 0 stagnation diagnosis.

**INSIGHT GATE [C-10/C-13/C-22]** — numbered sub-steps [C-23]:
> "(1) Formatted as **TEAM INSIGHT — [descriptive name]:**. [C-13]
>  (2) Names specific topics, contributors, or numeric values. [C-10]
>  (3) Passed per-topic derivability test for all scan state topics. [C-22]
>  (4) Distinct from Phase 0 stagnation diagnosis statement. [C-10]"
>
> Fail: "INSIGHT GATE FAIL [C-10/C-13/C-22]: condition ([n]) — [specific issue]."

```markdown
**TEAM INSIGHT — [descriptive name]:** [insight sentence]
```

### 2D — NEXT ACTIONS [C-05/C-12/C-14/C-17]

Actions must be pattern-breaking first — ordered by how directly they attack the dominant pattern.

```markdown
## Next Actions

Dominant stagnation pattern: **[PATTERN_LABEL from registry]**
*Actions ordered by pattern-breaking impact — highest first.*

1. **[action — namespace and topic explicit]**
   → Unlocks **[Achievement or Milestone]**
   → Breaks **[PATTERN_LABEL from registry]**: [one sentence on mechanism]

2. [same format]

3. [same format]
```

**ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]** — numbered sub-steps [C-23]:
This gate covers unlock naming (C-05), anti-inertia format (C-12), registry labels (C-14),
and gate ID enumeration (C-20). All four checked together.

> "(1) Each action names specific namespace and topic. [C-05]
>  (2) Each action names exact unlock. [C-05]
>  (3) Each action uses format [Action] → Unlocks [X] → Breaks [Pattern]. [C-12]
>  (4) Every pattern label from registry — no invented labels. [C-14]
>  (5) Actions ordered by pattern-breaking impact — highest-impact first. [C-12]
>  (6) At least 3 actions. [C-05]
>  (7) Gate label [C-05/C-12/C-14/C-20] enumerates all covered IDs. [C-25]"
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
  Pattern frame reconfirmed or revised: [reconfirmed/revised to PATTERN_LABEL]
```

---

## PHASE 3 — CROSS-PHASE CORRECTION AND STRUCTURAL AUDIT

### 3A — CROSS-PHASE CONTINUITY GATE [C-24]

**CROSS-PHASE GATE [C-24/C-01/C-02]** — numbered sub-steps [C-23]:
> "(1) Read Phase 2 State: milestone gaps, 1-away topics, implied missing topics/namespaces.
>  (2) Did Phase 2 gaps surface topic names absent from Phase 1 scan state? YES/NO.
>  (3) Did Phase 2 gaps imply namespaces absent from Phase 1 namespace list? YES/NO.
>  (4) YES to (2): add missing topics to Phase 1B Achievements with evidence or gap.
>      State: 'CROSS-PHASE UPDATE [C-24]: topic(s) [list] added.'
>  (5) YES to (3): record in frontmatter as `c24_namespace_gaps: [list]`.
>  (6) NO to both: 'CROSS-PHASE GATE [C-24]: No additions to Phase 1/2 output.'
>  (7) Phase 1 topic list finalized."
>
> Pass: "CROSS-PHASE GATE [C-24]: Passed. Additions: [n topics / 0]."

### 3B — STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]

Scan back through all output produced in Phases 0–2.

**STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]** — numbered sub-steps [C-23]:
> "(1) List every gate label executed in this run (Phases 0–2).
>  (2) For each: confirm it carries at least one [C-XX] criterion ID reference.
>  (3) Verify each multi-criterion super-gate by full label name and exact IDs expected:
>      - 'LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]' — confirm label enumerates C-16, C-19, C-21.
>      - 'ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]' — confirm label enumerates C-05, C-12, C-14, C-20.
>  (4) Missing criterion ID: 'AUDIT FAIL [C-20/C-26]: gate "[label]" missing ID.'
>  (5) Wrong enumeration: 'AUDIT FAIL [C-27]: gate "[label]" — expected [C-XX/...], found [C-XX/...].'
>  (6) Count: [n] gates audited, [n] correct, [n] violations.
>  (7) State outcome:
>      All pass: 'STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]: Passed. [n] gates correct,
>        super-gate enumeration verified for [C-16/C-19/C-21] and [C-05/C-12/C-14/C-20].'
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
c25_super_gates: ["LEADERBOARD CLUSTER [C-16/C-19/C-21]", "ACTIONS CLUSTER [C-05/C-12/C-14/C-20]"]
c26_structural_audit_gates_checked: [n]
c26_structural_audit_violations: [n or "none"]
c27_super_gate_enumeration_verified: [true/false]
c21_correction_applied: [true/false/not_applicable]
c22_derivability_passed: [true/false]
inertia_framing: stagnation-first
gate_language: numbered-substeps
---
```

---

## V-04 — Combined: Role Sequence + Lifecycle Emphasis + Inertia Framing

**Axes**: Leaderboard-first role sequence (V-01) + stagnation-first inertia framing (V-03)
+ explicit phase barriers with STOP instructions (lifecycle emphasis).
**Hypothesis**: Combining three axes creates the most tightly gated variation. The stagnation
diagnosis runs first (Phase 0), framing everything downstream. The leaderboard is computed
before achievements (Phase 1), anchoring contributor attribution. Explicit STOP barriers
between phases prevent any cross-phase bleeding. Together: the model cannot write a single
achievement without knowing both who produced the signals and what pattern is suppressing
further growth — making the output maximally action-oriented.

---

You are running `corps-achievements`. Scan the workspace and compute team achievement state.
No arguments. Execute four phases in strict sequence. Each phase ends with a STOP barrier.
Do not read the next phase's instructions until the current phase's gate passes.

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

## PHASE 0 — STAGNATION DIAGNOSIS

Glob `simulations/**/*.md`. Record: total signals, contributor count, namespace count,
date of most recent file.

**STAGNATION DIAGNOSIS GATE [C-14/C-17]** — numbered sub-steps [C-23]:
> "(1) contributor count = 1? → SOLO_ISLAND candidate.
>  (2) namespace count = 1? → NAMESPACE_MOAT candidate.
>  (3) most recent file > 7 days ago? → SPRINT_FREEZE candidate.
>  (4) total signals < (topic count × 3)? → SHALLOW_POOL candidate.
>  (5) contributor fields absent? → ORPHAN_TOPIC candidate.
>  (6) Select single dominant pattern (most strongly evidenced).
>  (7) Pattern label from registry — no invented labels. [C-14]
>  (8) Label is a semantic name encoding pattern type. [C-17]"
>
> Pass: "STAGNATION DIAGNOSIS GATE [C-14/C-17]: Dominant = [PATTERN_LABEL]. Evidence: [conditions]."
> Fail: "STAGNATION DIAGNOSIS GATE FAIL [C-14/C-17]: condition ([n]) — [issue]."

```markdown
## Team Stagnation Diagnosis — {{date}}
**Dominant pattern: [PATTERN_LABEL from registry]**
[One sentence evidence.]
```

> **PHASE 0 COMPLETE.** Do not read Phase 1 instructions until the gate above passes.

---

## PHASE 1 — FULL SCAN AND CONTRIBUTOR LEADERBOARD

### 1A — SCAN [C-01]

Glob `simulations/**/*.md` (full extraction). Extract topic path, namespace, contributor.

```
SCAN STATE (internal):
  Topics: [list]  Namespaces: [list]  Contributors: [list]  Total: [n]
  Pattern: [PATTERN_LABEL from Phase 0]
```

**SCAN GATE [C-01/C-15]** — numbered sub-steps [C-23]:
> "(1) `simulations/` accessible, >= 1 file. (2) Every file assigned to real topic path.
>  (3) Scan state complete with pattern field. (4) No file skipped."
>
> Pass: "SCAN GATE [C-01]: [n] signals, [n] topics, contributors: [list]."
> Fail: "SCAN GATE FAIL [C-01/C-15]: condition ([n]) — [specific path]."

### 1B — CONTRIBUTOR LEADERBOARD [C-04/C-16/C-19/C-21]

**Pre-write gate [C-11]**: "Are Signals/Topics/Milestones counts derived from scan state?
Does the dominant pattern predict leaderboard shape? Confirm before writing."

```markdown
## Contributor Leaderboard — Week of {{date}}

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
```

**LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]** — numbered sub-steps [C-23]:
This gate covers formula scoring (C-16), worked example (C-19), reconciliation loop (C-21).

> "(1) Formula Score=(Signals×1)+(Topics×3)+(Milestones×5) — not raw count. [C-16]
>  (2) Worked example Rank 1: {S}×1 + {T}×3 + {M}×5 = {total}. [C-19]
>  (3) Compare {total} to Score column. [C-21]
>  (4) If mismatch: correct; state 'Corrected: {old}→{new}.' [C-21]
>  (5) Score column for Rank 1 = {total}. [C-21]
>  (6) Gate label [C-16/C-19/C-21] enumerates all covered IDs. [C-25]"
>
> Pass: "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]: Passed.
>   Formula (C-16): confirmed. Example (C-19): {total}. Reconciliation (C-21): [applied/clear].
>   Label enumeration (C-25): [C-16/C-19/C-21] verified."
> Not applicable: "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]: Not applicable — no contributors."

> **PHASE 1 COMPLETE.** Do not read Phase 2 instructions until the gate above passes.

---

## PHASE 2 — ACHIEVEMENTS, MILESTONES, GAPS, INSIGHT, AND ACTIONS

### 2A — ACHIEVEMENTS [C-02/C-06/C-07]

**Pre-write gate [C-11]**: "All topics from scan state appear below? Contributors from Phase 1
leaderboard used in evidence cells? Pattern frame noted in section headers? If not, fix first."

Definitions: First Signal (>=1), Signal Depth (>=3), Full Sweep (>=3 namespaces),
Solo Pioneer (1 contributor), Team Topic (>=2 contributors).

```markdown
## Earned Achievements — {{date}}
*(Earned despite [PATTERN_LABEL])*

**[topic]** ([n] signals)
  - **[Achievement]**: [evidence using Phase 1 contributor names]

## Locked Achievements
*(Blocked by [PATTERN_LABEL])*

**[topic]** ([n] signals)
  - o [Achievement]: needs [quantified gap]
```

**COMPUTE GATE [C-02/C-15]** — numbered sub-steps [C-23]:
> "(1) All scan-state topics in Earned or Locked. (2) All Earned have evidence.
>  (3) All Locked have specific gap. (4) Evidence references Phase 1 contributor names."
>
> Fail: "COMPUTE GATE FAIL [C-02/C-15]: condition ([n]) — [specific instance]."

### 2B — TEAM MILESTONES [C-03]

```markdown
## Team Milestones — {{date}}

| Milestone | Status | Evidence | Gap |
|-----------|--------|----------|-----|
| first team signal | EARNED / NOT YET | [path/"—"] | [gap/"—"] |
| shared coverage | EARNED / NOT YET | [2+contrib×2+topics/"—"] | [gap/"—"] |
| debate starter | EARNED / NOT YET | [topic+namespaces/"—"] | [gap/"—"] |
```

**MILESTONES GATE [C-03/C-15]** — numbered sub-steps [C-23]:
> "(1) Row 1 = 'first team signal'. (2) Row 2 = 'shared coverage'. (3) Row 3 = 'debate starter'.
>  (4) Evidence/Gap cells populated or '—'."
>
> Fail: "MILESTONES GATE FAIL [C-03/C-15]: condition ([n]) — [row or cell]."

### 2C — 1-AWAY GAPS [C-09/C-18]

```markdown
## Almost There — 1-Away Gaps

| Topic / Milestone | Achievement to Unlock | Gap | Exact Action Needed |
|-------------------|-----------------------|-----|---------------------|
```

**1-AWAY GATE [C-09/C-18]** — numbered sub-steps [C-23]:
> "(1) All topics checked vs thresholds. (2) All milestones checked. (3) All rows four columns."
>
> Fail: "1-AWAY GATE FAIL [C-09/C-18]: row '[topic]' missing column."

### 2D — TEAM INSIGHT [C-10/C-13/C-22]

**Step A**: Candidate insight — must relate to the stagnation pattern frame without restating it.
**Step B**: Per-topic derivability test.
**Step C**: All NO → approved. Any YES → generate new candidate (up to 2 attempts).

**INSIGHT GATE [C-10/C-13/C-22]** — numbered sub-steps [C-23]:
> "(1) Formatted as **TEAM INSIGHT — [name]:**. [C-13]
>  (2) Specific values, not generic. [C-10]
>  (3) Passed per-topic derivability test. [C-22]
>  (4) Distinct from Phase 0 stagnation diagnosis. [C-10]"
>
> Fail: "INSIGHT GATE FAIL [C-10/C-13/C-22]: condition ([n]) — [issue]."

```markdown
**TEAM INSIGHT — [descriptive name]:** [insight sentence]
```

### 2E — NEXT ACTIONS [C-05/C-12/C-14/C-17]

Order by pattern-breaking impact. First action must directly attack the dominant pattern.

```markdown
## Next Actions

Dominant stagnation pattern: **[PATTERN_LABEL from registry]**

1. **[action]**
   → Unlocks **[Achievement/Milestone]**
   → Breaks **[PATTERN_LABEL from registry]**: [mechanism]

2. [same format]

3. [same format]
```

**ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]** — numbered sub-steps [C-23]:
This gate covers unlock naming (C-05), anti-inertia format (C-12), registry labels (C-14),
and gate ID enumeration (C-20). All four checked together.

> "(1) Each action names namespace+topic. [C-05]
>  (2) Each names exact unlock. [C-05]
>  (3) Format [Action] → Unlocks [X] → Breaks [Pattern]. [C-12]
>  (4) Registry labels only. [C-14]
>  (5) At least 3 actions, ordered by impact. [C-05]
>  (6) Gate label [C-05/C-12/C-14/C-20] enumerates all IDs. [C-25]"
>
> Pass: "ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]: Passed.
>   Unlock named (C-05): confirmed. Anti-inertia format (C-12): confirmed.
>   Registry labels (C-14): confirmed. Label enumeration (C-25): [C-05/C-12/C-14/C-20] verified."
> Fail: "ACTIONS CLUSTER GATE FAIL [C-05/C-12/C-14/C-20]: action [n], condition ([n]) — [issue]."

### 2F — RECORD PHASE 2 STATE (internal)

```
PHASE 2 STATE:
  Milestones not yet earned: [list/"all earned"]
  1-away gap topics: [list/"none"]
  Implied missing topics: [list/"none"]
  Implied missing namespaces: [list/"none"]
```

> **PHASE 2 COMPLETE.** Do not read Phase 3 instructions until all Phase 2 gates pass.

---

## PHASE 3 — CROSS-PHASE CORRECTION AND STRUCTURAL AUDIT

### 3A — CROSS-PHASE CONTINUITY GATE [C-24]

**CROSS-PHASE GATE [C-24/C-01/C-02]** — numbered sub-steps [C-23]:
> "(1) Read Phase 2 State entries.
>  (2) Did Phase 2 gaps surface topics absent from Phase 1 scan state? YES/NO.
>  (3) Did Phase 2 gaps imply namespaces absent from Phase 1 namespace list? YES/NO.
>  (4) YES to (2): add to Phase 2A Achievements with evidence or gap.
>      'CROSS-PHASE UPDATE [C-24]: topic(s) [list] added.'
>  (5) YES to (3): frontmatter `c24_namespace_gaps: [list]`.
>  (6) NO to both: 'CROSS-PHASE GATE [C-24]: No additions.'
>  (7) Lists finalized."
>
> Pass: "CROSS-PHASE GATE [C-24]: Passed. Additions: [n / 0]."

### 3B — STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]

Scan back through all output in Phases 0–2.

**STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]** — numbered sub-steps [C-23]:
> "(1) List every gate label executed in this run (Phases 0–2).
>  (2) Each gate label carries at least one [C-XX] criterion ID.
>  (3) Verify each multi-criterion super-gate by full label and exact IDs expected:
>      - 'LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]' — confirm enumerates C-16, C-19, C-21.
>      - 'ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]' — confirm enumerates C-05, C-12, C-14, C-20.
>  (4) Missing ID: 'AUDIT FAIL [C-20/C-26]: gate "[label]" missing ID.'
>  (5) Wrong enumeration: 'AUDIT FAIL [C-27]: gate "[label]" — expected [C-XX/...], found [C-XX/...].'
>  (6) Count: [n] gates, [n] correct, [n] violations.
>  (7) Outcome:
>      All pass: 'STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]: Passed. [n] gates correct.'
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
role_sequence: leaderboard-first
inertia_framing: stagnation-first
lifecycle_barriers: explicit-stop
gate_language: numbered-substeps
---
```

---

## V-05 — Combined: Output Format + Phrasing Register (Conversational + Dense Tables)

**Axes**: Dense table output format (V-02) + conversational/narrative phrasing register.
**Hypothesis**: The most readable variation for team consumers combines structured tables
(for auditability) with a warm narrative register that connects data to team context.
Conversational framing names the team's situation as an agent acts in it — "your team
has earned X because Y" rather than "topic X: First Signal: EARNED." Gates are phrased
as first-person confirmations ("Before we write this section, I confirm...") which can
improve model self-alignment with the verification intent. Tables preserve structural
completeness; tone makes the output useful in standups and sprint retros, not just
as an audit log.

---

You are helping your team understand its collective signal momentum. Run `corps-achievements`
to scan the workspace and compute team achievement state. No arguments. Execute three phases.
Write warmly and directly — your audience is the team, reading this in a sprint retro.
Every claim goes in a table so the team can verify it. Every gate runs before writing.

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

## PHASE 1 — WHAT THE TEAM HAS BUILT

### 1A — WORKSPACE SCAN [C-01]

Glob `simulations/**/*.md`. For each file, extract topic path, namespace, and contributor.

```
SCAN STATE (internal):
  Topics: [list]  Namespaces: [list]  Contributors: [list]  Total signals: [n]
```

Before I write any results, I confirm [C-11]:
> "Every topic I found in the glob is grounded in a real file path — I did not add topics
> from memory. My scan state is complete and no file was skipped."

**SCAN GATE [C-01/C-15]** — numbered sub-steps [C-23]:
> "(1) `simulations/` accessible and glob returned >= 1 file.
>  (2) Every file in the glob assigned to a topic path from actual glob output.
>  (3) Scan state complete. (4) No file skipped."
>
> Pass: "SCAN GATE [C-01]: [n] signals, [n] topics, contributors: [list]."
> Fail: "SCAN GATE FAIL [C-01/C-15]: condition ([n]) — [specific file or path]."

### 1B — WHAT YOUR TEAM HAS EARNED [C-02/C-06/C-07]

Before I write this section, I confirm [C-11]:
> "Every topic from scan state appears in either Earned or Locked below.
> Missing topics: [list or 'none']. Adding before writing."

```markdown
## Earned Achievements — {{date}}
*Your team has locked in these achievements through sustained signal work.*

| Topic | Achievement | Evidence |
|-------|-------------|----------|
| [topic] | [achievement] | [counts, names, namespace list] |

## Locked Achievements
*These are within reach — here is exactly what each topic still needs.*

| Topic | Achievement | Gap (specific count or target) |
|-------|-------------|--------------------------------|
| [topic] | [achievement] | [e.g., "2 more signals", "1 more contributor"] |
```

**COMPUTE GATE [C-02/C-15]** — numbered sub-steps [C-23]:
> "(1) Topic count across Earned+Locked tables matches scan state total.
>  (2) Every Earned row has a populated Evidence cell.
>  (3) Every Locked row has a specific quantified gap — not 'needs more work.'"
>
> Fail: "COMPUTE GATE FAIL [C-02/C-15]: condition ([n]) — [specific topic or row]."

### 1C — WHO IS CARRYING THE LOAD [C-04/C-16/C-19/C-21]

Before I write this section, I confirm [C-11]:
> "Signals, Topics, and Milestones counts per contributor are derived from scan state,
> not estimated. Ready to write the leaderboard."

```markdown
## Contributor Leaderboard — Week of {{date}}
*Scored on the formula: Signals×1 + Topics×3 + Milestones×5 — because breadth
and milestones reflect more leverage than signal volume alone.*

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
```

**LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]** — numbered sub-steps [C-23]:
This gate covers formula scoring (C-16), worked example (C-19), reconciliation loop (C-21).
All three together — a formula without a worked example is a claim; a worked example without
a reconciliation loop cannot self-correct.

> "(1) Leaderboard uses explicit formula Signals×1 + Topics×3 + Milestones×5 — not raw count. [C-16]
>  (2) Worked example for Rank 1: Score = {S}×1 + {T}×3 + {M}×5 = {total}. [C-19]
>  (3) Compare {total} to Score column for Rank 1. [C-21]
>  (4) If mismatch: correct Score column to {total}; state 'Corrected: {old}→{new}.' [C-21]
>  (5) Score column for Rank 1 = {total}. [C-21]
>  (6) Gate label [C-16/C-19/C-21] enumerates all criterion IDs it covers. [C-25]"
>
> Pass: "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]: Passed.
>   Formula (C-16): confirmed. Example (C-19): {total}. Reconciliation (C-21): [applied/clear].
>   Label enumeration (C-25): [C-16/C-19/C-21] verified."
> Not applicable: "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]: Not applicable — no contributors."

---

## PHASE 2 — WHERE THE TEAM IS HEADING

### 2A — TEAM MILESTONES [C-03]

These three milestones show whether the team has graduated from individual effort to
genuine collective momentum.

```markdown
## Team Milestones — {{date}}

| Milestone | Status | Evidence | Gap |
|-----------|--------|----------|-----|
| first team signal | EARNED / NOT YET | [first file path or "—"] | [gap or "—"] |
| shared coverage | EARNED / NOT YET | [2+contrib×2+topics or "—"] | [gap or "—"] |
| debate starter | EARNED / NOT YET | [topic+namespaces or "—"] | [gap or "—"] |
```

**MILESTONES GATE [C-03/C-15]** — numbered sub-steps [C-23]:
> "(1) Row 1 = 'first team signal'. (2) Row 2 = 'shared coverage'. (3) Row 3 = 'debate starter'.
>  (4) Evidence and Gap cells populated or '—'. (5) No row name paraphrased."
>
> Fail: "MILESTONES GATE FAIL [C-03/C-15]: condition ([n]) — [specific row or cell]."

### 2B — ALMOST THERE [C-09/C-18]

Good news for the team: these achievements are one step away from being unlocked.

```markdown
## Almost There — 1-Away Gaps

| Topic / Milestone | Achievement to Unlock | Gap | Exact Action Needed |
|-------------------|-----------------------|-----|---------------------|
```

**1-AWAY GATE [C-09/C-18]** — numbered sub-steps [C-23]:
> "(1) Checked all topics vs all achievement thresholds for exactly-1-step gaps.
>  (2) Checked all milestones for 1-step gaps.
>  (3) Every row in the table has all four columns populated."
>
> Fail: "1-AWAY GATE FAIL [C-09/C-18]: row '[topic]' missing '[column name]'."

### 2C — WHAT THE DATA SHOWS TOGETHER [C-10/C-13/C-22]

Here is something the team would miss if they looked at any single topic in isolation.

**Step A**: Draft a candidate insight with specific numbers and contributor or topic names.
**Step B**: Per-topic derivability test — for each topic: "Could a reader derive this insight
from [topic] alone, without seeing any other topic? YES / NO"
**Step C**: All NO → approved. Any YES → draft new candidate (up to 2 attempts).
**Step D**: Confirm the insight is distinct from any gap or stagnation statement already made.

**INSIGHT GATE [C-10/C-13/C-22]** — numbered sub-steps [C-23]:
> "(1) Formatted as **TEAM INSIGHT — [descriptive name]:**. [C-13]
>  (2) Cites specific topics, contributors, or numerical values. [C-10]
>  (3) Passed per-topic derivability elimination for every topic in scan state. [C-22]
>  (4) Distinct from any gap or stagnation statement written above. [C-10]"
>
> Fail: "INSIGHT GATE FAIL [C-10/C-13/C-22]: condition ([n]) — [specific issue]."

```markdown
**TEAM INSIGHT — [descriptive name]:** [insight sentence]
```

### 2D — WHAT TO DO NEXT [C-05/C-12/C-14/C-17]

Here is what stands between the team and the next tier of achievement — and what rut each
action breaks.

```markdown
## Next Actions

Dominant stagnation pattern: **[PATTERN_LABEL from registry]**

1. **[specific action — namespace and topic explicit]**
   → Unlocks **[Achievement or Milestone name]**
   → Breaks **[PATTERN_LABEL from registry]**: [one sentence on how]

2. [same format]

3. [same format]
```

**ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]** — numbered sub-steps [C-23]:
This gate covers unlock naming (C-05), anti-inertia format (C-12), registry labels (C-14),
and gate ID enumeration (C-20). All four checked together — each depends on the others
to be individually verifiable.

> "(1) Each action names a specific namespace and topic — not 'add more signals.' [C-05]
>  (2) Each action names the exact achievement or milestone it unlocks. [C-05]
>  (3) Format used: [Action] → Unlocks [X] → Breaks [Pattern]. [C-12]
>  (4) Every pattern label from the Stagnation Pattern Registry — no invented labels. [C-14]
>  (5) At least 3 actions. [C-05]
>  (6) Gate label [C-05/C-12/C-14/C-20] enumerates all criterion IDs it covers. [C-25]"
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

## PHASE 3 — VERIFICATION AND WRITE

### 3A — DID PHASE 2 REVEAL ANYTHING PHASE 1 MISSED? [C-24]

**CROSS-PHASE GATE [C-24/C-01/C-02]** — numbered sub-steps [C-23]:
> "(1) Read Phase 2 State: milestone gaps, 1-away topics, implied missing topics/namespaces.
>  (2) Did Phase 2 gaps surface topic names absent from Phase 1 scan state? YES/NO.
>  (3) Did Phase 2 gaps imply namespaces absent from Phase 1 namespace list? YES/NO.
>  (4) YES to (2): add missing topics to Phase 1B Earned/Locked tables with evidence or gap.
>      State: 'CROSS-PHASE UPDATE [C-24]: topic(s) [list] added from Phase 2 gap analysis.'
>  (5) YES to (3): record in frontmatter as `c24_namespace_gaps: [list]`.
>  (6) NO to both: 'CROSS-PHASE GATE [C-24]: No Phase 2 additions to Phase 1 output.'
>  (7) Phase 1 topic list and achievement tables are now finalized."
>
> Pass: "CROSS-PHASE GATE [C-24]: Passed. Additions: [n topics / 0]."

### 3B — DID ALL GATES CARRY CRITERION IDs? [C-20/C-25/C-26/C-27]

Scan back through all output produced in Phases 1 and 2. List every gate label.

**STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]** — numbered sub-steps [C-23]:
> "(1) List every gate label executed in this run (Phases 1–2).
>  (2) For each gate label: confirm it carries at least one [C-XX] criterion ID reference.
>  (3) Verify each multi-criterion super-gate by full label name and exact IDs expected:
>      - 'LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]' — confirm label enumerates C-16, C-19, C-21.
>      - 'ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]' — confirm label enumerates C-05, C-12, C-14, C-20.
>  (4) Any gate missing a criterion ID: 'AUDIT FAIL [C-20/C-26]: gate "[label]" missing ID.'
>  (5) Any super-gate with wrong enumeration: 'AUDIT FAIL [C-27]: gate "[label]" — expected
>      [C-XX/...], found [C-XX/...].'
>  (6) Count: [n] gates audited, [n] correct, [n] violations.
>  (7) State outcome:
>      All pass: 'STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]: Passed. [n] gates correct,
>        super-gate enumeration verified for [C-16/C-19/C-21] and [C-05/C-12/C-14/C-20].'
>      Any fail: 'STRUCTURAL AUDIT GATE [C-20/C-25/C-26/C-27]: [n] violation(s). See findings.'"
>
> Violations are findings, not blockers — record in frontmatter and write the artifact.

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
output_format: dense-table
phrasing_register: conversational
gate_language: numbered-substeps
---
```
