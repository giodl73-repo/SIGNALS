---
skill: quest-variate
skill_target: corps-achievements
round: 8
date: 2026-03-16
rubric_version: 7
---

# Variate R8 — corps-achievements

5 complete prompt body variations for the `corps-achievements` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

R7 established C-24/C-25/C-26 as the next excellence tier. R8 targets these three criteria
directly. V-01 through V-03 each isolate one new criterion as the single variation axis.
V-04 combines C-24 + C-26. V-05 integrates all three.

All variations carry R7's baseline: essential C-01—C-05, recommended C-06—C-08,
and aspirational C-09—C-23. The variation is in how C-24, C-25, and C-26 are expressed.

---

## Variation Axes Selected

| Axis | Hypothesis | Used In |
|------|------------|---------|
| C-26 single: Meta-verification at SETUP (pre-flight) | Auditing gate labels before any step executes catches structural compliance before output is written — stronger than a post-hoc audit | V-01, V-04 |
| C-25 single: Aggressive super-gate clustering for Actions and Leaderboard clusters | Enumerating all interdependent criterion IDs in a single gate label makes inter-criterion dependency visible and prevents partial-cluster passes where one criterion in the group is checked but related ones are skipped | V-02, V-05 |
| C-24 single: Explicit three-phase structure with cross-phase gate at Phase 3 | Phase 3 gate asking "did Phase 2 gaps reveal topics not in Phase 1's scan?" turns sequential execution into a correction loop that upgrades Phase 1 outputs dynamically | V-03, V-04, V-05 |
| C-24 + C-26: Three phases with meta-verification as FINAL AUDIT | Post-execution meta-verification audits the gate labels the model actually wrote, not just the ones it intended to write — a stronger guarantee than pre-flight intent | V-04 |
| C-24 + C-25 + C-26: Full integration | Three phases create the scaffold C-24 threads; clustered super-gates give C-25 enumeration real content; C-26 meta-verification at the end audits the super-gates as a group — all three reinforce each other | V-05 |

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

## V-01 — C-26 Single Axis: Meta-Verification Gate as SETUP (Pre-Flight)

**Axis**: C-26 — meta-verification gate placed at the very start, auditing the skill's own
gate labels before any output step executes
**Hypothesis**: A pre-flight meta-verification gate — placed before Step 1 — forces the model
to read its own instruction set and confirm that every gate label carries a criterion ID
reference. Any gate label missing an ID is surfaced before a single artifact is written.
This is stronger than a post-hoc audit because structural compliance is verified against the
intended structure, not against whatever the model happened to write.

---

You are running `corps-achievements`. Scan the workspace and compute team achievement state.
No arguments. Execute each step in sequence. Do not begin a step until the previous gate passes.

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

### SETUP — PRE-FLIGHT STRUCTURAL AUDIT [C-20/C-26]

Before executing any step, read this skill body and list every gate label it contains.
For each gate label, confirm it carries at least one criterion ID in bracket notation [C-XX].

Execute this audit now:

> "(1) List every gate label in this skill, reading from top to bottom.
>  (2) For each gate label listed in (1), confirm it includes at least one [C-XX] reference.
>  (3) Any gate label without a criterion ID: state 'PREFLIGHT FAIL [C-20/C-26]:
>      gate label "[label]" missing criterion ID reference.'
>  (4) If all gate labels carry criterion IDs, state:
>      'PREFLIGHT PASS [C-20/C-26]: [n] gates audited, all carry criterion IDs: [list].'
>      Proceed to Step 1."
>
> A PREFLIGHT FAIL does not stop execution — it is a finding. State the finding,
> then proceed. The finding appears in the artifact frontmatter as
> `preflight_gate_violations: [n]`.

---

### STEP 1 — SCAN [C-01]

Glob `simulations/**/*.md`. For each file extract:
- Topic path (subdirectory under `simulations/`, e.g. `scout/competitors`)
- Namespace (first path segment, e.g. `scout`)
- Contributor identity (frontmatter `author:` or `contributor:` field; or filename prefix before
  the first digit-run)

Record an internal scan state (not part of final output):

```
SCAN STATE (internal):
  Topics: [list of unique topic paths]
  Namespaces: [list of unique first segments]
  Contributors: [deduplicated list, or "not detectable"]
  Total signals: [n]
```

**SCAN GATE [C-01/C-15]** — numbered sub-steps [C-23]:
> "(1) `simulations/` is accessible and the glob returned at least one file.
>  (2) Every file in the glob is assigned to a topic path derived from actual glob output.
>  (3) The scan state record above is complete.
>  (4) No file was skipped."
>
> Pass: "SCAN GATE [C-01]: Passed. [n] signals, [n] topics, [n] namespaces, contributors: [list]."
> Fail on (1)/(2): "SCAN GATE FAIL [C-01/C-15]: condition ([n]) — [specific file or path]."
> Fail on (3)/(4): "SCAN GATE FAIL [C-01/C-15]: condition ([n]) — file '[path]' not assigned."

---

### STEP 2 — ACHIEVEMENTS [C-02/C-06/C-07]

**Pre-write gate [C-11]**:
> "Do all topics from the scan state appear in either Earned or Locked below?
> If not, identify the missing topic and add it before generating the section."

Achievement definitions:

| Achievement | Condition |
|-------------|-----------|
| First Signal | >= 1 signal for this topic |
| Signal Depth | >= 3 signals for this topic |
| Full Sweep | signals span >= 3 distinct namespaces for this topic |
| Solo Pioneer | exactly 1 contributor, >= 1 signal for this topic |
| Team Topic | >= 2 contributors, >= 1 signal each for this topic |

Render two explicitly labeled sections [C-06, C-07]:

```markdown
## Earned Achievements — {{date}}

**[topic path]** ([n] signals)
  - **[Achievement name]**: [evidence — file count, contributor names, or namespace list]

## Locked Achievements

**[topic path]** ([n] signals)
  - o [Achievement name]: needs [quantified gap — "2 more signals", "1 more namespace", etc.]
```

**COMPUTE GATE [C-02/C-15]** — numbered sub-steps [C-23]:
> "(1) Every topic in the scan state appears in Earned or Locked — count must match.
>  (2) Every Earned entry names specific evidence — no bare achievement names without evidence.
>  (3) Every Locked entry quantifies the gap with a specific count or target."
>
> Fail: "COMPUTE GATE FAIL [C-02/C-15]: condition ([n]) — [specific instance]."

---

### STEP 3 — TEAM MILESTONES [C-03]

```markdown
## Team Milestones — {{date}}

| Milestone | Status | Evidence | Gap |
|-----------|--------|----------|-----|
| first team signal | EARNED / NOT YET | [file path, or "—"] | [gap, or "—"] |
| shared coverage | EARNED / NOT YET | [2+ contributors × 2+ topics, or "—"] | [gap, or "—"] |
| debate starter | EARNED / NOT YET | [topic path + namespaces, or "—"] | [gap, or "—"] |
```

Milestone definitions:
- **first team signal**: any signal file exists in `simulations/`
- **shared coverage**: 2+ contributors each contributing signals to 2+ distinct topics
- **debate starter**: 1 topic with signals spanning 3+ distinct namespaces

**MILESTONES GATE [C-03/C-15]** — numbered sub-steps [C-23]:
> "(1) Row 1 name is exactly 'first team signal'.
>  (2) Row 2 name is exactly 'shared coverage'.
>  (3) Row 3 name is exactly 'debate starter'.
>  (4) Every row has an Evidence cell that is either a file path, a contributor+topic pair,
>      or an explicit '—' — no empty cells."
>
> Fail: "MILESTONES GATE FAIL [C-03/C-15]: condition ([n]) — '[written name]' → '[exact name]'."

---

### STEP 4 — CONTRIBUTOR LEADERBOARD [C-04/C-16/C-19/C-21]

**Pre-write gate [C-11]**:
> "Do I have Signals, Topics, and Milestones counts for each contributor from the scan state?
> If not, derive these counts now from the scan state before building the table."

Formula: `Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

```markdown
## Contributor Leaderboard — Week of {{date}}

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
| 1 | [name or "unknown"] | [n] | [n] | [n] | [Score] |
| 2 | ... | ... | ... | ... | ... |
```

If no contributor metadata: one row `| — | (no contributor metadata found) | — | — | — | — |`

**FORMULA CORRECTION GATE [C-19/C-21]** — numbered sub-steps [C-23]:
> "(1) Render worked example for Rank 1: Score = {Signals}×1 + {Topics}×3 + {Milestones}×5 = {total}
>  (2) Compare {total} to the Score column entry for Rank 1.
>  (3) If {total} does not equal the Score column entry, correct the Score column to {total}.
>      State: 'Score corrected from {old} to {new}.'
>  (4) Confirm: Score column entry for Rank 1 equals {total}."
>
> Pass: "FORMULA GATE [C-19/C-21]: Passed. Rank-1 score = {total} (verified / corrected)."
> No metadata: "FORMULA GATE [C-19/C-21]: Not applicable — no contributor metadata."

---

### STEP 5 — 1-AWAY GAPS [C-09/C-18]

Scan for achievements or milestones requiring exactly 1 action to unlock.

```markdown
## Almost There — 1-Away Gaps

| Topic / Milestone | Achievement to Unlock | Gap | Exact Action Needed |
|-------------------|-----------------------|-----|---------------------|
| [topic or milestone] | [Achievement name] | [e.g., "1 more signal"] | [specific file or contributor action] |
```

**1-AWAY GATE [C-09/C-18]** — numbered sub-steps [C-23]:
> "(1) I checked every topic against every achievement threshold for exactly-1-step gaps.
>  (2) I checked every milestone for exactly-1-step gaps.
>  (3) Every row has all four columns: topic/milestone, achievement, gap (exact count), exact action."
>
> Fail: "1-AWAY GATE FAIL [C-09/C-18]: row '[topic]' missing column '[name]'. Adding before proceeding."
> No gaps found: single row "No single-step unlocks available."

---

### STEP 6 — NEXT ACTIONS [C-05/C-12/C-14/C-17]

Identify the dominant stagnation pattern from the registry. State the label before writing actions.

```markdown
## Next Actions

Dominant stagnation pattern: **[PATTERN_LABEL from registry]**

1. **[specific action — name namespace and topic explicitly]**
   → Unlocks **[Achievement or Milestone name]**
   → Breaks **[PATTERN_LABEL from registry]**: [one sentence explaining the disruption]

2. [same format]

3. [same format]
```

Write at least 3 actions. Each must name a specific namespace and topic.

**ACTIONS GATE [C-05/C-12/C-14/C-20]** — numbered sub-steps [C-23]:
> "(1) Each action names a specific namespace and topic — not generic advice.
>  (2) Each action names the exact achievement or milestone it unlocks.
>  (3) Each action uses a pattern label from the Stagnation Pattern Registry — no invented labels.
>  (4) At least 3 actions are written.
>  (5) This gate label [C-05/C-12/C-14/C-20] enumerates all criterion IDs it covers."
>
> Fail: "ACTIONS GATE FAIL [C-05/C-12/C-14/C-20]: action [n], condition ([n]) — [specific issue]."

---

### STEP 7 — TEAM INSIGHT [C-10/C-13/C-22]

Execute the derivability elimination protocol before writing the insight.

**Step A — Candidate**: State the candidate insight in one sentence:
> "Candidate: [insight with specific numbers and topic/contributor names]"

**Step B — Topic elimination test**: For each topic in the scan state, test:
> "Can this insight be reached from [topic path] data alone, without any other topic?
>  Answer: YES / NO"
List every topic and its answer.

**Step C — Verdict**:
- All NO: "DERIVABILITY GATE [C-22]: [n] topics tested. No single topic yields this conclusion
  alone. Candidate approved."
- Any YES: "DERIVABILITY GATE [C-22]: Candidate derivable from topic '[path]' alone. Discarding.
  Returning to Step A."
  Repeat up to 2 times. If no passing candidate:
  "DERIVABILITY GATE [C-22]: Insufficient cross-topic data for a non-derivable insight."

**INSIGHT GATE [C-10/C-13/C-22]** — numbered sub-steps [C-23]:
> "(1) Insight is written as **TEAM INSIGHT — [name]:** — a named, referenceable artifact.
>  (2) Insight names specific topics, contributors, or numeric values — not only pattern labels.
>  (3) Insight passed derivability elimination in Step C."
>
> Fail: cite condition number and specific instance before revising.

Write the approved insight:

```markdown
**TEAM INSIGHT — [descriptive name]:** [insight sentence with specific numbers and names]
```

---

### STEP 8 — WRITE ARTIFACT [C-08]

Write the complete output to `simulations/corps/achievements-{{date}}.md`.

```yaml
---
skill: corps-achievements
date: {{date}}
topics_scanned: [n]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
stagnation_pattern: [PATTERN_LABEL]
preflight_gate_violations: [n or "none"]
c21_correction_applied: [true/false/not_applicable]
c22_derivability_passed: [true/false]
gate_language: numbered-substeps
c26_preflight: executed
---
```

---

## V-02 — C-25 Single Axis: Aggressive Multi-Criterion Gate Clustering

**Axis**: C-25 — two named super-gates with fully enumerated criterion ID labels: one for the
Actions cluster (C-05/C-12/C-14/C-20) and one for the Leaderboard cluster (C-16/C-19/C-21).
Both gate labels enumerate every criterion ID in the cluster.
**Hypothesis**: When four interdependent criteria (Actions group) and three interdependent
criteria (Leaderboard group) are each checked under a single gate whose label names all member
criterion IDs, a scorer looking at the gate label alone can verify that no criterion in the
cluster was omitted — the enumeration is its own coverage audit. A gate labeled only [C-05]
that also checks C-12/C-14/C-20 creates invisible partial-cluster risk; a gate labeled
[C-05/C-12/C-14/C-20] eliminates it.

---

You are running `corps-achievements`. Scan the workspace and compute team achievement state.
No arguments. Execute each step in sequence. Do not begin a step until the previous gate passes.

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

### STEP 1 — SCAN [C-01]

Glob `simulations/**/*.md`. For each file extract:
- Topic path (subdirectory under `simulations/`)
- Namespace (first path segment)
- Contributor identity (frontmatter `author:`/`contributor:` or filename prefix before first digit-run)

```
SCAN STATE (internal):
  Topics: [list of unique topic paths]
  Namespaces: [list of unique first segments]
  Contributors: [deduplicated list, or "not detectable"]
  Total signals: [n]
```

**SCAN GATE [C-01/C-15]** — numbered sub-steps [C-23]:
> "(1) `simulations/` accessible and glob returned >= 1 file.
>  (2) Every file assigned to a topic path from actual glob output — no assumed topic names.
>  (3) Scan state record complete.
>  (4) No file skipped."
>
> Pass: "SCAN GATE [C-01]: Passed. [n] signals, [n] topics, [n] namespaces, contributors: [list]."
> Fail: "SCAN GATE FAIL [C-01/C-15]: condition ([n]) — [specific file or path]."

---

### STEP 2 — ACHIEVEMENTS [C-02/C-06/C-07]

**Pre-write gate [C-11]**:
> "Do all topics from the scan state appear in Earned or Locked below?
> If not, identify the missing topic and add it before generating the section."

Achievement definitions:

| Achievement | Condition |
|-------------|-----------|
| First Signal | >= 1 signal for this topic |
| Signal Depth | >= 3 signals for this topic |
| Full Sweep | signals span >= 3 distinct namespaces |
| Solo Pioneer | exactly 1 contributor, >= 1 signal |
| Team Topic | >= 2 contributors, >= 1 signal each |

```markdown
## Earned Achievements — {{date}}

**[topic path]** ([n] signals)
  - **[Achievement name]**: [evidence — count, contributor names, or namespace list]

## Locked Achievements

**[topic path]** ([n] signals)
  - o [Achievement name]: needs [quantified gap]
```

**COMPUTE GATE [C-02/C-15]** — numbered sub-steps [C-23]:
> "(1) Every topic in scan state appears in Earned or Locked — count matches.
>  (2) Every Earned entry names specific evidence.
>  (3) Every Locked entry quantifies the gap specifically."
>
> Fail: "COMPUTE GATE FAIL [C-02/C-15]: condition ([n]) — [specific instance]."

---

### STEP 3 — TEAM MILESTONES [C-03]

```markdown
## Team Milestones — {{date}}

| Milestone | Status | Evidence | Gap |
|-----------|--------|----------|-----|
| first team signal | EARNED / NOT YET | [file path, or "—"] | [gap, or "—"] |
| shared coverage | EARNED / NOT YET | [2+ contributors × 2+ topics, or "—"] | [gap, or "—"] |
| debate starter | EARNED / NOT YET | [topic path + namespaces, or "—"] | [gap, or "—"] |
```

Definitions: first team signal = any signal file exists; shared coverage = 2+ contributors
× 2+ distinct topics each; debate starter = 1 topic spanning 3+ distinct namespaces.

**MILESTONES GATE [C-03/C-15]** — numbered sub-steps [C-23]:
> "(1) Row 1 is exactly 'first team signal'.
>  (2) Row 2 is exactly 'shared coverage'.
>  (3) Row 3 is exactly 'debate starter'.
>  (4) Every row Evidence cell is a path, contributor+topic pair, or explicit '—'."
>
> Fail: "MILESTONES GATE FAIL [C-03/C-15]: condition ([n]) — '[written]' → '[required]'."

---

### STEP 4 — CONTRIBUTOR LEADERBOARD

**Pre-write gate [C-11]**:
> "Do I have Signals, Topics, and Milestones counts per contributor from the scan state?
> If not, derive these counts from the scan state before building the table."

```markdown
## Contributor Leaderboard — Week of {{date}}

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
| 1 | [name or "unknown"] | [n] | [n] | [n] | [Score] |
```

Formula: `Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

If no contributor metadata: `| — | (no contributor metadata found) | — | — | — | — |`

**LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]** — numbered sub-steps [C-23]:
This gate covers three interdependent leaderboard criteria simultaneously.
C-16: formula-driven scoring is used (not rank-ordered count).
C-19: worked example is rendered for Rank 1.
C-21: table is reconciled if example reveals a mismatch.

> "(1) The leaderboard uses the explicit formula Score = (Signals×1) + (Topics×3) + (Milestones×5)
>      — not a raw count ranking. [C-16]
>  (2) Rendered worked example for Rank 1: Score = {Signals}×1 + {Topics}×3 + {Milestones}×5 = {total}. [C-19]
>  (3) Compared {total} to Score column entry for Rank 1. If mismatch: correct Score column to {total}
>      and state 'Score corrected from {old} to {new}.' [C-21]
>  (4) Score column entry for Rank 1 now equals {total}. [C-21]"
>
> Pass: "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]: Passed.
>   Formula used (C-16): confirmed. Rank-1 example (C-19): {total}. Correction (C-21): [applied/not needed]."
> No metadata: "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]: Not applicable."

---

### STEP 5 — 1-AWAY GAPS [C-09/C-18]

```markdown
## Almost There — 1-Away Gaps

| Topic / Milestone | Achievement to Unlock | Gap | Exact Action Needed |
|-------------------|-----------------------|-----|---------------------|
```

**1-AWAY GATE [C-09/C-18]** — numbered sub-steps [C-23]:
> "(1) Checked every topic against every achievement threshold for exactly-1-step gaps.
>  (2) Checked every milestone for exactly-1-step gaps.
>  (3) Every row has all four columns populated."
>
> Fail: "1-AWAY GATE FAIL [C-09/C-18]: row '[topic]' missing '[column]'. Adding."
> No gaps: "No single-step unlocks available."

---

### STEP 6 — NEXT ACTIONS

Identify the dominant stagnation pattern from the registry. State the label first.

```markdown
## Next Actions

Dominant stagnation pattern: **[PATTERN_LABEL from registry]**

1. **[specific action — namespace and topic explicit]**
   → Unlocks **[Achievement or Milestone name]**
   → Breaks **[PATTERN_LABEL from registry]**: [one sentence]

2. [same format]

3. [same format]
```

Write at least 3 actions. Each must name a specific namespace and topic.

**ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]** — numbered sub-steps [C-23]:
This gate covers four interdependent next-action criteria simultaneously.
C-05: each action names the achievement it unlocks.
C-12: each action uses the anti-inertia format (Action → Unlocks → Breaks).
C-14: pattern labels drawn from the registry, not invented.
C-20: gate labels carry criterion IDs (this gate label enumerates all four).

> "(1) Each action names a specific namespace and topic. [C-05]
>  (2) Each action names the exact achievement or milestone it unlocks. [C-05]
>  (3) Each action uses anti-inertia format: [Action] → Unlocks [Achievement] → Breaks [Pattern]. [C-12]
>  (4) Every pattern label in (3) appears in the Stagnation Pattern Registry above — no invented labels. [C-14]
>  (5) This gate label [C-05/C-12/C-14/C-20] enumerates all criterion IDs it covers. [C-20]
>  (6) At least 3 actions are written."
>
> Pass: "ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]: Passed.
>   Action count: [n]. Unlocks named (C-05): confirmed. Anti-inertia format (C-12): confirmed.
>   Registry labels only (C-14): confirmed. Gate ID enumeration (C-20): confirmed."
> Fail: "ACTIONS CLUSTER GATE FAIL [C-05/C-12/C-14/C-20]: action [n], condition ([n]) — [issue]."

---

### STEP 7 — TEAM INSIGHT [C-10/C-13/C-22]

**Step A — Candidate**: State the candidate insight:
> "Candidate: [insight with specific numbers and topic/contributor names]"

**Step B — Topic elimination test**: For each topic, test:
> "Can this insight be reached from [topic path] alone? YES / NO"

**Step C — Verdict**:
- All NO: "DERIVABILITY GATE [C-22]: [n] topics tested. Candidate approved."
- Any YES: discard, return to Step A (up to 2 attempts).

**INSIGHT GATE [C-10/C-13/C-22]** — numbered sub-steps [C-23]:
> "(1) Insight formatted as **TEAM INSIGHT — [name]:** — named and referenceable. [C-13]
>  (2) Insight names specific topics, contributors, or numeric values. [C-10]
>  (3) Insight passed derivability elimination — no single topic yields it alone. [C-22]"
>
> Fail: cite condition and specific instance.

```markdown
**TEAM INSIGHT — [descriptive name]:** [insight sentence]
```

---

### STEP 8 — WRITE ARTIFACT [C-08]

Write to `simulations/corps/achievements-{{date}}.md`.

```yaml
---
skill: corps-achievements
date: {{date}}
topics_scanned: [n]
contributors_detected: [n or "unknown"]
milestones_earned: [n]/3
stagnation_pattern: [PATTERN_LABEL]
c25_cluster_gates: ["LEADERBOARD CLUSTER [C-16/C-19/C-21]", "ACTIONS CLUSTER [C-05/C-12/C-14/C-20]"]
c21_correction_applied: [true/false/not_applicable]
c22_derivability_passed: [true/false]
gate_language: numbered-substeps
---
```

---

## V-03 — C-24 Single Axis: Explicit Three-Phase Structure with Cross-Phase Gate Threading

**Axis**: C-24 — three named phases (SCAN, COMPUTE, SYNTHESIZE) with an explicit Phase 3
gate that asks whether Phase 2's findings alter what Phase 1 computed.
**Hypothesis**: Naming three execution phases and requiring Phase 3 to explicitly ask "did
Phase 2's milestone gaps reveal topics not already in Phase 1's scan?" forces the model to
treat Phase 1 output as provisional, not final. Phase 1 produces a topic list; Phase 2 computes
milestones and leaderboard gaps; Phase 3's cross-phase gate checks whether Phase 2's gaps imply
Phase 1 missed topics, creating a dynamic correction loop. Without this gate, topics discovered
through gap analysis never feed back to update the scan results.

---

You are running `corps-achievements`. Scan the workspace and compute team achievement state.
No arguments. Execute three phases in sequence. Each phase has a gate; Phase 3 has a
cross-phase gate that explicitly references Phase 2 findings. Do not begin a phase until
the previous phase gate passes.

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

Phase 1 produces three artifacts: (a) the topic list, (b) per-topic achievements, (c) the
contributor leaderboard. Phase 1 output is provisional — Phase 3 may revise it.

### 1A — SCAN [C-01]

Glob `simulations/**/*.md`. For each file extract topic path, namespace, and contributor.

```
SCAN STATE (internal):
  Topics: [list]
  Namespaces: [list]
  Contributors: [list, or "not detectable"]
  Total signals: [n]
```

**SCAN GATE [C-01/C-15]** — numbered sub-steps [C-23]:
> "(1) `simulations/` accessible, glob returned >= 1 file.
>  (2) Every file assigned to a real topic path from glob output.
>  (3) Scan state complete.
>  (4) No file skipped."
>
> Pass: "SCAN GATE [C-01]: Passed. [n] signals, [n] topics, contributors: [list]."
> Fail: "SCAN GATE FAIL [C-01/C-15]: condition ([n]) — [specific file or path]."

### 1B — ACHIEVEMENTS [C-02/C-06/C-07]

**Pre-write gate [C-11]**:
> "Do all topics from scan state appear in Earned or Locked?
> If not, add the missing topic before generating the section."

Achievement definitions:

| Achievement | Condition |
|-------------|-----------|
| First Signal | >= 1 signal |
| Signal Depth | >= 3 signals |
| Full Sweep | >= 3 distinct namespaces |
| Solo Pioneer | exactly 1 contributor |
| Team Topic | >= 2 contributors, >= 1 signal each |

```markdown
## Earned Achievements — {{date}}

**[topic path]** ([n] signals)
  - **[Achievement]**: [evidence]

## Locked Achievements

**[topic path]** ([n] signals)
  - o [Achievement]: needs [quantified gap]
```

**COMPUTE GATE [C-02/C-15]** — numbered sub-steps [C-23]:
> "(1) Every scan-state topic appears in Earned or Locked.
>  (2) Every Earned entry has specific evidence.
>  (3) Every Locked entry has a specific quantified gap."
>
> Fail: "COMPUTE GATE FAIL [C-02/C-15]: condition ([n]) — [instance]."

### 1C — CONTRIBUTOR LEADERBOARD [C-04/C-16/C-19/C-21]

**Pre-write gate [C-11]**:
> "Do I have Signals, Topics, Milestones counts per contributor?
> If not, derive from scan state before building the table."

```markdown
## Contributor Leaderboard — Week of {{date}}

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
```

**FORMULA CORRECTION GATE [C-19/C-21]** — numbered sub-steps [C-23]:
> "(1) Worked example Rank 1: Score = {S}×1 + {T}×3 + {M}×5 = {total}. [C-19]
>  (2) Compare {total} to Score column for Rank 1. [C-21]
>  (3) If mismatch: correct Score column to {total}. State 'Corrected: {old} → {new}.' [C-21]
>  (4) Score column for Rank 1 equals {total}. [C-21]"

---

## PHASE 2 — MILESTONE AND GAP ANALYSIS

Phase 2 computes the three team milestones and the 1-away gap table. Phase 2 output is
recorded as **Phase 2 State** — a structured finding that Phase 3 will explicitly interrogate.

### 2A — TEAM MILESTONES [C-03]

```markdown
## Team Milestones — {{date}}

| Milestone | Status | Evidence | Gap |
|-----------|--------|----------|-----|
| first team signal | EARNED / NOT YET | [path, or "—"] | [gap, or "—"] |
| shared coverage | EARNED / NOT YET | [contributors × topics, or "—"] | [gap, or "—"] |
| debate starter | EARNED / NOT YET | [topic + namespaces, or "—"] | [gap, or "—"] |
```

**MILESTONES GATE [C-03/C-15]** — numbered sub-steps [C-23]:
> "(1) Row 1 name exactly 'first team signal'.
>  (2) Row 2 name exactly 'shared coverage'.
>  (3) Row 3 name exactly 'debate starter'.
>  (4) Every Evidence cell is a path, pair, or explicit '—'."
>
> Fail: "MILESTONES GATE FAIL [C-03/C-15]: condition ([n]) — '[written]' → '[required]'."

### 2B — 1-AWAY GAPS [C-09/C-18]

```markdown
## Almost There — 1-Away Gaps

| Topic / Milestone | Achievement to Unlock | Gap | Exact Action Needed |
|-------------------|-----------------------|-----|---------------------|
```

**1-AWAY GATE [C-09/C-18]** — numbered sub-steps [C-23]:
> "(1) Checked every topic vs every threshold for exactly-1-step gaps.
>  (2) Checked every milestone for exactly-1-step gaps.
>  (3) Every row has all four columns."
>
> Fail: "1-AWAY GATE FAIL [C-09/C-18]: row '[topic]' missing '[column]'."

### 2C — RECORD PHASE 2 STATE

Before advancing to Phase 3, record this structured summary (internal, not output):

```
PHASE 2 STATE:
  Milestones NOT YET earned: [list, or "all earned"]
  Topics with 1-away gaps: [list of topic paths, or "none"]
  Topics with no signals (discovered via gaps): [list, or "none"]
  Namespace gaps: [list of namespaces implied by 1-away gaps but not present in scan state]
```

---

## PHASE 3 — SYNTHESIS AND CROSS-PHASE CORRECTION

Phase 3 generates the team insight, the next actions list, and then applies the cross-phase
gate. The cross-phase gate asks whether Phase 2's findings alter what Phase 1 computed.

### 3A — NEXT ACTIONS [C-05/C-12/C-14/C-17]

Identify the dominant stagnation pattern. State the label first.

```markdown
## Next Actions

Dominant stagnation pattern: **[PATTERN_LABEL from registry]**

1. **[specific action — namespace and topic explicit]**
   → Unlocks **[Achievement or Milestone name]**
   → Breaks **[PATTERN_LABEL from registry]**: [one sentence]

2. [same format]

3. [same format]
```

**ACTIONS GATE [C-05/C-12/C-14/C-20]** — numbered sub-steps [C-23]:
> "(1) Each action names specific namespace and topic.
>  (2) Each action names exact achievement or milestone unlocked.
>  (3) Each pattern label from registry — no invented labels.
>  (4) At least 3 actions written.
>  (5) This gate label [C-05/C-12/C-14/C-20] carries all criterion IDs it covers."
>
> Fail: "ACTIONS GATE FAIL [C-05/C-12/C-14/C-20]: action [n], condition ([n]) — [issue]."

### 3B — TEAM INSIGHT [C-10/C-13/C-22]

**Step A**: State candidate insight in one sentence.
**Step B**: For each topic in scan state: "Can this be derived from [topic] alone? YES / NO"
**Step C**: Verdict — all NO approves; any YES discards and restarts (up to 2 attempts).

**INSIGHT GATE [C-10/C-13/C-22]** — numbered sub-steps [C-23]:
> "(1) Insight formatted as **TEAM INSIGHT — [name]:**.
>  (2) Names specific topics, contributors, or values.
>  (3) Passed derivability elimination."

```markdown
**TEAM INSIGHT — [descriptive name]:** [insight sentence]
```

### 3C — CROSS-PHASE CONTINUITY GATE [C-24]

This gate explicitly asks whether Phase 2's findings alter what Phase 1 computed.
Run this gate after the insight and actions are written, before writing the artifact.

**CROSS-PHASE GATE [C-24/C-01/C-02]** — numbered sub-steps [C-23]:
> "(1) Read Phase 2 State: 'Milestones NOT YET earned', 'Topics with 1-away gaps',
>      'Topics with no signals', and 'Namespace gaps'.
>  (2) Did Phase 2's milestone gaps surface any topic names not present in Phase 1's
>      topic list? Answer: YES (list them) / NO.
>  (3) Did Phase 2's 1-away gap analysis imply any namespaces not found in Phase 1's
>      namespace list? Answer: YES (list them) / NO.
>  (4) If YES to (2): add the missing topics to the Earned/Locked section (Step 1B) and
>      restate which achievement they earn or are locked for. State:
>      'CROSS-PHASE UPDATE [C-24]: topic(s) [list] added from Phase 2 gap analysis.'
>  (5) If YES to (3): note the namespace gap in the artifact frontmatter.
>  (6) If NO to both: state 'CROSS-PHASE GATE [C-24]: No Phase 2 additions to Phase 1 output.'
>  (7) Phase 1 topic list is now finalized."
>
> Pass: "CROSS-PHASE GATE [C-24]: Passed. Phase 2 additions: [n topics / 0]."

---

### STEP — WRITE ARTIFACT [C-08]

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
c21_correction_applied: [true/false/not_applicable]
c22_derivability_passed: [true/false]
gate_language: numbered-substeps
---
```

---

## V-04 — Combination: C-24 + C-26 (Three Phases with Final Audit Meta-Verification)

**Axis**: C-24 (three-phase structure with cross-phase gate) combined with C-26 (meta-verification
gate placed at the END — after all output is written — auditing the gate labels in the output
the model actually produced, not the labels in the instructions it was given)
**Hypothesis**: End-of-run meta-verification is stronger than pre-flight meta-verification for
C-26 because it audits the actual gates executed during the run. Pre-flight checks the skill's
own instructions; end-of-run checks the model's output — catching cases where a gate label was
paraphrased or an ID reference dropped during synthesis. Combined with three-phase cross-phase
threading, this variation creates forward-correction (C-24) and backward-audit (C-26) in a
single execution.

---

You are running `corps-achievements`. Scan the workspace and compute team achievement state.
No arguments. Execute three phases in sequence. Each phase has a gate. Phase 3 includes a
cross-phase gate. After all phases complete, run a final structural audit gate.

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
>  (2) Every file assigned to a real topic path from glob.
>  (3) Scan state complete. (4) No file skipped."
>
> Pass: "SCAN GATE [C-01]: [n] signals, [n] topics, contributors: [list]."
> Fail: "SCAN GATE FAIL [C-01/C-15]: condition ([n]) — [specific path]."

### 1B — ACHIEVEMENTS [C-02/C-06/C-07]

**Pre-write gate [C-11]**: "All scan-state topics appear below? If not, add before writing."

Achievements: First Signal (>=1), Signal Depth (>=3), Full Sweep (>=3 namespaces),
Solo Pioneer (1 contributor), Team Topic (2+ contributors each >=1 signal).

```markdown
## Earned Achievements — {{date}}
**[topic]** ([n] signals)  - **[Achievement]**: [evidence]

## Locked Achievements
**[topic]** ([n] signals)  - o [Achievement]: needs [quantified gap]
```

**COMPUTE GATE [C-02/C-15]** — numbered sub-steps [C-23]:
> "(1) Every scan-state topic in Earned or Locked. (2) Every Earned has evidence.
>  (3) Every Locked has specific gap."
> Fail: "COMPUTE GATE FAIL [C-02/C-15]: condition ([n]) — [instance]."

### 1C — CONTRIBUTOR LEADERBOARD [C-04/C-16/C-19/C-21]

**Pre-write gate [C-11]**: "Signals/Topics/Milestones counts per contributor confirmed?"

```markdown
## Contributor Leaderboard — Week of {{date}}
| Rank | Contributor | Signals | Topics | Milestones | Score |
```

Formula: `Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

**FORMULA CORRECTION GATE [C-19/C-21]** — numbered sub-steps [C-23]:
> "(1) Worked example Rank 1: {S}×1 + {T}×3 + {M}×5 = {total}. [C-19]
>  (2) Compare to Score column. [C-21] (3) Mismatch: correct and state change. [C-21]
>  (4) Confirm match. [C-21]"
> Pass: "FORMULA GATE [C-19/C-21]: Rank-1={total} verified/corrected."

---

## PHASE 2 — MILESTONE AND GAP ANALYSIS

### 2A — TEAM MILESTONES [C-03]

```markdown
## Team Milestones — {{date}}
| Milestone | Status | Evidence | Gap |
| first team signal | EARNED / NOT YET | [path/"—"] | [gap/"—"] |
| shared coverage   | EARNED / NOT YET | [2+contrib×2+topic/"—"] | [gap/"—"] |
| debate starter    | EARNED / NOT YET | [topic+namespaces/"—"] | [gap/"—"] |
```

**MILESTONES GATE [C-03/C-15]** — numbered sub-steps [C-23]:
> "(1) Row 1 = 'first team signal'. (2) Row 2 = 'shared coverage'. (3) Row 3 = 'debate starter'.
>  (4) All Evidence cells populated or '—'."
> Fail: "MILESTONES GATE FAIL [C-03/C-15]: condition ([n]) — name mismatch."

### 2B — 1-AWAY GAPS [C-09/C-18]

```markdown
## Almost There — 1-Away Gaps
| Topic / Milestone | Achievement to Unlock | Gap | Exact Action Needed |
```

**1-AWAY GATE [C-09/C-18]** — numbered sub-steps [C-23]:
> "(1) Checked all topics vs all thresholds for 1-step gaps.
>  (2) Checked all milestones for 1-step gaps.
>  (3) All rows have four columns."
> Fail: "1-AWAY GATE FAIL [C-09/C-18]: row missing column."

### 2C — RECORD PHASE 2 STATE (internal)

```
PHASE 2 STATE:
  Milestones not yet earned: [list/"all earned"]
  1-away gap topics: [list/"none"]
  Implied missing topics: [list/"none"]
  Implied missing namespaces: [list/"none"]
```

---

## PHASE 3 — SYNTHESIS AND CROSS-PHASE CORRECTION

### 3A — NEXT ACTIONS [C-05/C-12/C-14/C-17]

State dominant stagnation pattern first, then actions.

```markdown
## Next Actions
Dominant stagnation pattern: **[PATTERN_LABEL from registry]**

1. **[action — namespace and topic explicit]**
   → Unlocks **[Achievement/Milestone]**
   → Breaks **[PATTERN_LABEL from registry]**: [one sentence]
```

**ACTIONS GATE [C-05/C-12/C-14/C-20]** — numbered sub-steps [C-23]:
> "(1) Each action names namespace+topic. (2) Names exact unlock. (3) Registry labels only.
>  (4) >=3 actions. (5) Gate label [C-05/C-12/C-14/C-20] carries all four criterion IDs."
> Fail: "ACTIONS GATE FAIL [C-05/C-12/C-14/C-20]: action [n], condition ([n])."

### 3B — TEAM INSIGHT [C-10/C-13/C-22]

Candidate → topic elimination test (YES/NO per topic) → verdict → approved insight.

**INSIGHT GATE [C-10/C-13/C-22]** — numbered sub-steps [C-23]:
> "(1) **TEAM INSIGHT — [name]:** format. (2) Specific values. (3) Derivability passed."

```markdown
**TEAM INSIGHT — [name]:** [insight]
```

### 3C — CROSS-PHASE CONTINUITY GATE [C-24]

**CROSS-PHASE GATE [C-24/C-01/C-02]** — numbered sub-steps [C-23]:
> "(1) Read Phase 2 State entries.
>  (2) Did Phase 2 gaps surface topics absent from Phase 1 topic list? YES/NO.
>  (3) Did Phase 2 gaps imply namespaces absent from Phase 1 namespace list? YES/NO.
>  (4) YES to (2): add missing topics to Earned/Locked with evidence/gap. State
>      'CROSS-PHASE UPDATE [C-24]: added topic(s) [list].'
>  (5) YES to (3): record namespace gap in frontmatter.
>  (6) NO to both: 'CROSS-PHASE GATE [C-24]: No Phase 2 additions to Phase 1.'
>  (7) Phase 1 topic list finalized."
>
> Pass: "CROSS-PHASE GATE [C-24]: Passed. Additions: [n/0]."

---

## FINAL — STRUCTURAL AUDIT GATE [C-20/C-26]

After all phases complete and before writing the artifact, audit every gate label
that was executed in this run.

Scan back through the output produced above. List every gate label that appears.

**STRUCTURAL AUDIT GATE [C-20/C-26]** — numbered sub-steps [C-23]:
> "(1) List every gate label executed in this run (by reading back through the output above).
>  (2) For each gate label, confirm it carries at least one [C-XX] criterion ID reference.
>  (3) Any gate label missing a criterion ID: state
>      'AUDIT FAIL [C-20/C-26]: gate "[label]" missing criterion ID.'
>  (4) Count: [n] gates audited, [n] with IDs, [n] without.
>  (5) If all carry IDs: 'STRUCTURAL AUDIT GATE [C-20/C-26]: Passed. [n] gates all carry IDs.'
>      If any fail: 'STRUCTURAL AUDIT GATE [C-20/C-26]: [n] violations found. Listed above.'
>      Violations are findings, not blockers — record in frontmatter and proceed."

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
c26_final_audit_gates_checked: [n]
c26_final_audit_violations: [n or "none"]
c21_correction_applied: [true/false/not_applicable]
c22_derivability_passed: [true/false]
gate_language: numbered-substeps
---
```

---

## V-05 — Full Integration: C-24 + C-25 + C-26 (Three Phases, Super-Gates, Final Audit)

**Axis**: All three new criteria combined — three-phase structure with cross-phase gate
threading (C-24), two named super-gates with fully enumerated criterion ID labels (C-25),
and a final meta-verification gate auditing all gate labels in the run output (C-26).
**Hypothesis**: The three new criteria are architecturally interdependent.
Three phases create the named structure C-24 needs to thread — without phases, "prior phase
findings" has no referent. Super-gates aggregate related criteria into dense clusters that
are worth enumerating in a label — without enough criteria per gate, a fully enumerated label
has no information advantage. The final meta-verification gate becomes most powerful when there
are named super-gates to audit, because it can check that both the LEADERBOARD CLUSTER and
ACTIONS CLUSTER labels enumerate all member criterion IDs. Together, C-24 + C-25 + C-26 form
a closed system: phases → threading → clustering → audit → self-enforcement.

---

You are running `corps-achievements`. Scan the workspace and compute team achievement state.
No arguments. Execute three phases in sequence. Phases 1 and 2 contain super-gates covering
interdependent criteria clusters. Phase 3 contains the cross-phase continuity gate and the
team synthesis. After all phases, a final structural audit gate verifies all gate labels.

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

## PHASE 1 — SCAN AND ACHIEVEMENTS

### 1A — SCAN [C-01]

Glob `simulations/**/*.md`. Extract topic path, namespace, contributor per file.

```
SCAN STATE (internal):
  Topics: [list]  Namespaces: [list]  Contributors: [list]  Total signals: [n]
```

**SCAN GATE [C-01/C-15]** — numbered sub-steps [C-23]:
> "(1) `simulations/` accessible, >= 1 file.
>  (2) Every file assigned to real topic path from glob.
>  (3) Scan state complete. (4) No file skipped."
>
> Pass: "SCAN GATE [C-01]: [n] signals, [n] topics, contributors: [list]."
> Fail: "SCAN GATE FAIL [C-01/C-15]: condition ([n]) — [specific path]."

### 1B — ACHIEVEMENTS [C-02/C-06/C-07]

**Pre-write gate [C-11]**: "All scan-state topics appear below? If not, add before writing."

Achievements: First Signal (>=1 signal), Signal Depth (>=3), Full Sweep (>=3 namespaces),
Solo Pioneer (exactly 1 contributor), Team Topic (>=2 contributors, >=1 signal each).

```markdown
## Earned Achievements — {{date}}

**[topic path]** ([n] signals)
  - **[Achievement]**: [evidence — count, names, namespace list]

## Locked Achievements

**[topic path]** ([n] signals)
  - o [Achievement]: needs [quantified gap]
```

**COMPUTE GATE [C-02/C-15]** — numbered sub-steps [C-23]:
> "(1) Every scan-state topic in Earned or Locked.
>  (2) Every Earned has specific evidence.
>  (3) Every Locked has specific quantified gap."
>
> Fail: "COMPUTE GATE FAIL [C-02/C-15]: condition ([n]) — [specific instance]."

---

## PHASE 2 — MILESTONES, LEADERBOARD, AND GAP ANALYSIS

### 2A — TEAM MILESTONES [C-03]

```markdown
## Team Milestones — {{date}}

| Milestone | Status | Evidence | Gap |
|-----------|--------|----------|-----|
| first team signal | EARNED / NOT YET | [path/"—"] | [gap/"—"] |
| shared coverage | EARNED / NOT YET | [contrib×topics/"—"] | [gap/"—"] |
| debate starter | EARNED / NOT YET | [topic+ns/"—"] | [gap/"—"] |
```

Definitions: first team signal = any file; shared coverage = 2+ contrib × 2+ topics each;
debate starter = 1 topic × 3+ distinct namespaces.

**MILESTONES GATE [C-03/C-15]** — numbered sub-steps [C-23]:
> "(1) Row 1 = 'first team signal'. (2) Row 2 = 'shared coverage'. (3) Row 3 = 'debate starter'.
>  (4) All Evidence cells populated or '—'."
> Fail: "MILESTONES GATE FAIL [C-03/C-15]: condition ([n]) — name mismatch."

### 2B — CONTRIBUTOR LEADERBOARD AND FORMULA VERIFICATION

**Pre-write gate [C-11]**: "Signals/Topics/Milestones counts per contributor derived?"

```markdown
## Contributor Leaderboard — Week of {{date}}

| Rank | Contributor | Signals | Topics | Milestones | Score |
|------|-------------|---------|--------|------------|-------|
```

Formula: `Score = (Signals × 1) + (Topics × 3) + (Milestones × 5)`

**LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]** — numbered sub-steps [C-23]:
This gate covers three interdependent leaderboard criteria: formula-driven scoring (C-16),
worked example render (C-19), and reconciliation loop (C-21). All three checked together
because C-19 without C-21 is display without enforcement, and C-16 without C-19 is
a formula claim that cannot be verified.

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
> No metadata: "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]: Not applicable."

### 2C — 1-AWAY GAPS [C-09/C-18]

```markdown
## Almost There — 1-Away Gaps

| Topic / Milestone | Achievement to Unlock | Gap | Exact Action Needed |
|-------------------|-----------------------|-----|---------------------|
```

**1-AWAY GATE [C-09/C-18]** — numbered sub-steps [C-23]:
> "(1) Checked all topics vs all thresholds for exactly-1-step gaps.
>  (2) Checked all milestones for 1-step gaps.
>  (3) All rows have four columns."
> Fail: "1-AWAY GATE FAIL [C-09/C-18]: missing column in row '[topic]'."

### 2D — RECORD PHASE 2 STATE (internal)

```
PHASE 2 STATE:
  Milestones not yet earned: [list/"all earned"]
  1-away gap topics: [list/"none"]
  Implied missing topics: [list/"none"]
  Implied missing namespaces: [list/"none"]
```

---

## PHASE 3 — SYNTHESIS, CROSS-PHASE CORRECTION, AND FINAL AUDIT

### 3A — NEXT ACTIONS [C-05/C-12/C-14/C-17]

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
This gate covers four interdependent next-action criteria: unlock naming (C-05),
anti-inertia format (C-12), registry-drawn labels (C-14), and gate ID enumeration (C-20).
These four are checked together because C-12's format requires C-14's label,
and C-14's registry sourcing is only verifiable when C-20's gate label exposes the dependency.

> "(1) Each action names a specific namespace and topic — not generic advice. [C-05]
>  (2) Each action names the exact achievement or milestone it unlocks. [C-05]
>  (3) Each action uses format [Action] → Unlocks [Achievement] → Breaks [Pattern]. [C-12]
>  (4) Every pattern label in (3) drawn from the Stagnation Pattern Registry — no invented labels. [C-14]
>  (5) At least 3 actions written. [C-05]
>  (6) This gate label [C-05/C-12/C-14/C-20] enumerates all criterion IDs it covers. [C-25]"
>
> Pass: "ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]: Passed.
>   Unlock named (C-05): confirmed. Anti-inertia format (C-12): confirmed.
>   Registry labels (C-14): confirmed. Label enumeration (C-25): [C-05/C-12/C-14/C-20] verified."
> Fail: "ACTIONS CLUSTER GATE FAIL [C-05/C-12/C-14/C-20]: action [n], condition ([n]) — [issue]."

### 3B — TEAM INSIGHT [C-10/C-13/C-22]

**Step A**: State candidate insight in one sentence with specific numbers and names.
**Step B**: For each topic in scan state: "Can this be derived from [topic] alone? YES / NO"
**Step C**: All NO → approved. Any YES → discard and restart (up to 2 attempts).

**INSIGHT GATE [C-10/C-13/C-22]** — numbered sub-steps [C-23]:
> "(1) Insight formatted as **TEAM INSIGHT — [name]:**. [C-13]
>  (2) Names specific topics, contributors, or numeric values. [C-10]
>  (3) Passed derivability elimination — single-topic-derivability test run for each topic. [C-22]"
> Fail: cite condition and specific instance.

```markdown
**TEAM INSIGHT — [descriptive name]:** [insight sentence]
```

### 3C — CROSS-PHASE CONTINUITY GATE [C-24]

**CROSS-PHASE GATE [C-24/C-01/C-02]** — numbered sub-steps [C-23]:
> "(1) Read Phase 2 State: milestone gaps, 1-away gap topics, implied missing topics/namespaces.
>  (2) Did Phase 2 gaps surface topic names absent from Phase 1 topic list? YES/NO.
>  (3) Did Phase 2 gaps imply namespaces absent from Phase 1 namespace list? YES/NO.
>  (4) YES to (2): add missing topics to Earned/Locked section (Phase 1B) with evidence or gap.
>      State: 'CROSS-PHASE UPDATE [C-24]: topic(s) [list] added from Phase 2 gap analysis.'
>  (5) YES to (3): record namespace gap in frontmatter as `c24_namespace_gaps: [list]`.
>  (6) NO to both: 'CROSS-PHASE GATE [C-24]: No Phase 2 additions to Phase 1 output.'
>  (7) Phase 1 topic list is now finalized — no further additions."
>
> Pass: "CROSS-PHASE GATE [C-24]: Passed. Additions: [n topics / 0]."

### 3D — STRUCTURAL AUDIT GATE [C-20/C-26]

After the cross-phase gate and before writing the artifact, audit every gate label
produced in this run. Scan back through the output of all three phases.

**STRUCTURAL AUDIT GATE [C-20/C-26]** — numbered sub-steps [C-23]:
> "(1) List every gate label executed in this run (read back through Phases 1–3 above).
>  (2) For each gate label: confirm it carries at least one [C-XX] criterion ID reference.
>  (3) Pay specific attention to the two super-gates:
>      - 'LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]' — confirm label enumerates C-16, C-19, C-21.
>      - 'ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]' — confirm label enumerates C-05, C-12, C-14, C-20.
>  (4) Any gate label missing a criterion ID: state
>      'AUDIT FAIL [C-20/C-26]: gate "[label]" missing criterion ID reference.'
>  (5) Count: [n] gates audited, [n] with IDs, [n] without.
>  (6) State outcome:
>      All pass: 'STRUCTURAL AUDIT GATE [C-20/C-26]: Passed. [n] gates all carry criterion IDs,
>        including super-gates [C-16/C-19/C-21] and [C-05/C-12/C-14/C-20].'
>      Any fail: 'STRUCTURAL AUDIT GATE [C-20/C-26]: [n] violation(s). See findings above.'"
>
> Violations are findings, not blockers. Record count in frontmatter and proceed.

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
c26_final_audit_gates_checked: [n]
c26_final_audit_violations: [n or "none"]
c21_correction_applied: [true/false/not_applicable]
c22_derivability_passed: [true/false]
gate_language: numbered-substeps
---
```
