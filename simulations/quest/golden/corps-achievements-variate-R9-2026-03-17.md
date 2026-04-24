---
skill: quest-variate
skill_target: corps-achievements
round: 9
date: 2026-03-17
rubric_version: 9
basis: Rubric v9 adds C-26 (explicit lifecycle phase barrier language). Prior best (V-05 R8,
       rubric v8) satisfied C-01--C-25 at 100. R9 carries that full baseline and explores
       three single-axis approaches to C-26 implementation (V-01/V-02/V-03), then combines
       them (V-04/V-05). C-26 is the only new criterion; all other criteria are baseline.
---

# Variate R9 — corps-achievements (2026-03-17)

5 complete prompt body variations for the `corps-achievements` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

Rubric v9 adds one new aspirational criterion beyond the v8 baseline:

- **C-26 (new)**: Explicit lifecycle phase barrier language — "STOP. Phase N complete." or
  equivalent declarative seal at each phase boundary, written before Phase N+1 context is
  introduced. Phase-do-not-begin instructions (prospective gating) do not satisfy C-26.
  The seal must be retrospective — it closes Phase N's output set at the moment Phase N
  completes, so subsequent context cannot reopen it.

All variations carry the full v8 baseline: essential C-01--C-05, recommended C-06--C-08,
and aspirational C-09--C-25. The single variation axis for V-01/V-02/V-03 is C-26 only:
three distinct structural mechanisms for implementing phase sealing. V-04 and V-05 combine.

---

## Variation Axes Selected

| Axis | Hypothesis | Used In |
|------|------------|---------|
| Lifecycle: terse STOP declaration | A bare "STOP. Phase N complete. [C-26]" on its own line is the minimal viable seal — instruction-enforced but low overhead | V-01, V-04 |
| Output format: pre-printed barrier in artifact template | Placing the sealed marker inside the pre-printed output skeleton means the model cannot omit it — structural rather than behavioral compliance | V-02, V-04, V-05 |
| Phrasing: formal closure gate with verification sub-steps | A named PHASE N CLOSURE GATE [C-26] with numbered sub-steps requires the model to confirm completeness before proceeding — making sealing a verifiable gate pass, not just a statement | V-03, V-05 |

---

## V-01 — Single Axis: Terse STOP Declaration

**Axis**: Lifecycle emphasis — explicit "STOP. Phase N complete. [C-26]" as a bare declarative
seal on its own line at each phase boundary, written after the final Phase N gate passes and
before Phase N+1 instructions appear.

**Hypothesis**: A terse STOP line is the minimal C-26 implementation. It is unambiguous and
low-overhead. The risk is instruction-dependency: the model must choose to write the line.
Without structural reinforcement (no pre-printed template, no closure gate), compliance is
behavioral. This variation isolates the pure instruction-based approach.

---

You are running `corps-achievements`. Scan all signal artifacts for the topic. Compute
achievement state. Show contributor leaderboard and next recommended action.

**INPUT**: `{{topic}}` (auto-detect from context or TOPICS.md if not provided)

---

### OUTPUT SCHEMAS [C-37]

**Achievement row**:
```
| Category | Achievement | State | Evidence | Progress |
```
- State: exactly one of EARNED, IN-PROGRESS, or LOCKED. [C-01]
- Evidence: specific artifact path from Phase 1 scan. Required for EARNED and IN-PROGRESS. [C-03]
- Progress: `n of m [requirement]` for IN-PROGRESS; `--` otherwise. [C-04]

**Leaderboard row**:
```
| Rank | Contributor | Signals | Topics | Milestones | Score | Pattern |
```

**1-Away gap row**:
```
| Topic/Milestone | Achievement | Gap | Exact Action |
```

**Next action block**:
```
Next: /[skill-name] [topic] -> produces [artifact-name] -> advances [Achievement] -> Unlocks [Achievement] -> Breaks [PATTERN]
```

**Artifact frontmatter**:
```yaml
---
skill: corps-achievements
topic: {{topic}}
date: {{date}}
skill_version: v1
input: {{topic}}
---
```

---

### REGISTRY PRIMACY GATE [C-24]

Read `simulations/TOPICS.md` before any phase begins.

The topic registry entry for `{{topic}}` is the **sole authoritative gate contract** for this
skill. All phase instructions below are subordinate to the registry entry. A registry field
that conflicts with a phase instruction governs.

FAIL Tier 1 [C-25]: Topic not found in TOPICS.md -> output "TOPIC NOT REGISTERED: {{topic}}" and halt.
FAIL Tier 3 [C-25]: Registry entry present but contradicts an achievement classification
  produced by phase instructions -> registry governs; record the override as a finding.

---

### ATTRIBUTION INTEGRITY GATE [C-24/C-30]

Fires before Phase 1 begins.

(1) Confirm `{{topic}}` appears in `simulations/TOPICS.md`. [C-24]
(2) Glob `simulations/**/{{topic}}-*.md`. Record file count and contributor list (from
    frontmatter `author:` or `contributor:` fields). This is the ATTRIBUTION BASELINE.
(3) Record: `ATTRIBUTION BASELINE: [N] artifacts. Contributors: [list]`.

FAIL Tier 1 [C-25]: 0 artifacts found -> output "NO ARTIFACTS FOUND: {{topic}}" and halt.
FAIL Tier 2 [C-25]: Frontmatter missing contributor fields in some artifacts -> record count,
  continue with available data.
FAIL Tier 3 [C-25]: Any achievement row names a contributor absent from ATTRIBUTION BASELINE ->
  halt, flag instance as Tier 3 violation.

---

## PHASE 1 -- EVIDENCE SCAN

**Scope**: Build the raw signal inventory. Record counts and citations. Do not classify
achievements in this phase. Achievement classification belongs to Phase 2.

**1A -- Signal Inventory**

Enumerate every artifact from the glob above. For each, record:
- Namespace (scout, draft, review, flow, trace, prove, listen, program, topic)
- File path
- Date (from frontmatter)
- Contributor (from frontmatter)

Aggregate per namespace:
- Signal count
- Unique contributor count

**SCAN GATE [C-01/C-15]** -- numbered sub-steps [C-23]:

> (1) `simulations/` is accessible; glob returned >= 1 file.
> (2) Every file is assigned to a known namespace.
> (3) Contributor list matches ATTRIBUTION BASELINE.
> (4) SCAN STATE is complete and ready for Phase 2.
>
> Pass: "SCAN GATE [C-01/C-15]: [N] signals across [M] namespaces. Contributors: [list]."
> Fail Tier 1: "SCAN GATE FAIL [C-01/C-15]: [specific condition] -- [path or instance]."

**1B -- Phase 1 State Record**

```
PHASE 1 STATE:
  Namespaces with signals: [list]
  Per-namespace signal count: [ns: n, ns: n, ...]
  Total signal count: N
  Milestone count (from TOPICS.md registry): M
  Contributors: [list]
  Earliest artifact: [date]  Latest artifact: [date]
```

**STOP. Phase 1 complete. [C-26]**

All Phase 1 scan results are now sealed. PHASE 1 STATE is closed.
Phase 2 uses PHASE 1 STATE as its only evidence source. Phase 2 may not alter signal
counts, contributor lists, namespace assignments, or artifact citations recorded above.

---

## PHASE 2 -- ACHIEVEMENT CLASSIFICATION

**Scope**: Classify achievements using PHASE 1 STATE only. Do not re-scan artifacts.
The topic registry (TOPICS.md) is the gate contract for all classification thresholds. [C-24]

**Achievement Categories** (all 7 must appear in output) [C-06]:

**1. Exploration**
- EARNED: signals in >= 5 namespaces.
- IN-PROGRESS: signals in 1-4 namespaces. Progress: `n of 5 namespaces covered`. [C-04]
- LOCKED: 0 namespaces.

**2. Depth**
- EARNED: any single namespace has >= 3 signals.
- IN-PROGRESS: max namespace signal count = 1-2. Progress: `n of 3 signals in [namespace]`. [C-04]
- LOCKED: no signals in any namespace.

**3. Coverage**
- EARNED: signals in all 9 namespaces.
- IN-PROGRESS: signals in 1-8 namespaces. Progress: `n of 9 namespaces`. [C-04]
- LOCKED: 0 signals.

**4. Quality / Falsified** [C-02]
- EARNED: any prove-* artifact records a falsified hypothesis (evidence contradicted claim).
- Frame as: "Followed evidence over assumptions -- investigative rigor confirmed." [C-02]
  Do NOT frame as failure or absence.
- IN-PROGRESS: prove artifacts exist, no falsification recorded. Progress: `0 of 1 falsification events`.
- LOCKED: no prove artifacts.

**5. Chain**
- EARNED: topic-story or topic-report artifact cites >= 3 prior namespace signals.
- IN-PROGRESS: story/report exists, cites < 3 signals. Progress: `n of 3 cited signals`.
- LOCKED: no story or report artifact.

**6. Discovery**
- EARNED: topic-echo artifact exists (unexpected findings documented).
- LOCKED: no echo artifact. (Binary achievement -- no IN-PROGRESS state.)

**7. Corps/Crew**
- EARNED: >= 2 distinct contributors have artifacts for this topic.
- IN-PROGRESS: 1 contributor. Progress: `1 of 2 contributors`. [C-04]
- LOCKED: 0 contributors.

**CLASSIFICATION GATE [C-03/C-25]** -- numbered sub-steps [C-23]:

> (1) Every EARNED row cites a specific artifact path from PHASE 1 STATE. [C-03]
> (2) Every IN-PROGRESS row cites the partial count from PHASE 1 STATE with `n of m` form. [C-04]
> (3) No state row is missing artifact evidence.
> (4) All 7 categories are represented. [C-06]
>
> Fail Tier 2: State assignment with no artifact citation -> mark row `(UNCITED)`, record finding.
> Fail Tier 3: Citation to a path not present in PHASE 1 STATE -> halt, flag as Tier 3.

**2B -- 1-Away Gaps** [C-09]

After classifying all categories, identify any IN-PROGRESS achievement where `n = m-1`.
Record in 1-AWAY TABLE with four columns: topic/milestone, achievement, gap, exact action. [C-18]

**2C -- Pattern Assignment** [C-17]

Assign the first matching pattern from STAGNATION PATTERN REGISTRY:

| Label | Condition |
|-------|-----------|
| SOLO_ISLAND | 1 contributor, all signals |
| NAMESPACE_MOAT | all signals from 1 namespace |
| SPRINT_FREEZE | 0 artifacts added in last 30 days |
| SHALLOW_POOL | total signal count < 3 |
| ORPHAN_TOPIC | no contributor metadata in any artifact |

Use label syntax `[PATTERN_LABEL from registry]`. Do not invent labels. [C-14]

**2D -- Phase 2 State Record**

```
PHASE 2 STATE:
  Achievement classifications: [7 rows, one per category]
  1-Away count: N
  Top pattern: [label or NONE]
  Dominant contributor: [name]
```

**STOP. Phase 2 complete. [C-26]**

All Phase 2 achievement classifications are now sealed. PHASE 2 STATE is closed.
Phase 3 reads Phase 2 outputs to generate tables. Phase 3 may not alter EARNED/IN-PROGRESS/LOCKED
assignments or category coverage decisions recorded above.

---

## PHASE 3 -- OUTPUT GENERATION

**Scope**: Emit the final achievement report from Phase 2 STATE. Do not reclassify.

**3A -- Pre-write Gate** [C-11]

Before writing any section: "Do all values in the tables below derive from PHASE 1 STATE
and PHASE 2 STATE? If any value would require rescanning artifacts, record that as a
pre-write gate failure and derive the value from the existing state records instead."

**3B -- Achievements Table** [C-01/C-03/C-04/C-06]

Emit one row per achievement. State must be exactly EARNED, IN-PROGRESS, or LOCKED.

| Category | Achievement | State | Evidence | Progress |
|----------|-------------|-------|----------|----------|
| Exploration | ... | | | |
| Depth | ... | | | |
| Coverage | ... | | | |
| Quality / Falsified | ... | | | |
| Chain | ... | | | |
| Discovery | ... | | | |
| Corps/Crew | ... | | | |

**3C -- 1-Away Gaps Table** [C-09/C-18]

| Topic/Milestone | Achievement | Gap | Exact Action |
|-----------------|-------------|-----|--------------|

**3D -- LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]** -- numbered sub-steps [C-23]

This gate covers three interdependent leaderboard criteria simultaneously. [C-25]

> (1) Apply formula `Score = (Signals x 1) + (Topics x 3) + (Milestones x 5)` to every contributor. [C-16]
> (2) Rank contributors by score descending.
> (3) Render worked example for Rank 1: `Score = {S}x1 + {T}x3 + {M}x5 = {total}`. [C-19]
> (4) Compare {total} to Score column for Rank 1. If mismatch: correct Score column to {total};
>     state "Corrected: {old}->{new}." [C-21]
> (5) Emit leaderboard table including Pattern column.
> (6) This gate label [C-16/C-19/C-21] enumerates all criterion IDs it covers. [C-25]
>
> Pass: "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]: Formula (C-16): confirmed.
>   Rank-1 example (C-19): {total}. Correction (C-21): [applied/not needed].
>   Label enumeration (C-25): [C-16/C-19/C-21] verified."

**3E -- Team Insight** [C-13]

`**TEAM INSIGHT -- [descriptive name]:** [finding]`

Derive from Phase 2 STATE. The insight must not be derivable directly from the achievements
table alone -- it must synthesize pattern + contributor + gap data. [C-22]

**INSIGHT GATE [C-13/C-22]** -- numbered sub-steps [C-23]:

> (1) Insight names a specific pattern or contributor.
> (2) Insight is not a restatement of a single table row.
> (3) Eliminate: is this insight derivable by reading only the achievements table?
>     If yes, it does not satisfy C-22. Rewrite to require cross-table synthesis. [C-22]

**3F -- ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]** -- numbered sub-steps [C-23]

> (1) Draft next recommended action in format:
>     `Next: /[skill-name] [topic] -> produces [artifact-name] -> advances [Achievement]` [C-05]
>     Action must name a specific skill, a specific artifact, and a specific advancement.
> (2) Append unlock chain: `-> Unlocks [Achievement] -> Breaks [PATTERN]` where applicable. [C-12]
> (3) Confirm all achievement labels match exact registry labels. No invented labels. [C-14]
> (4) Confirm action names a specific skill, artifact, and advancement -- not generic. [C-05]
> (5) Confirm every gate label in this run carries a criterion ID reference `[C-XX]`. [C-20]
> (6) This gate label [C-05/C-12/C-14/C-20] enumerates all criterion IDs it covers. [C-25]
>
> Fail Tier 1 [C-25]: Gate label missing from any gate executed above -> halt, list instances.
> Fail Tier 3 [C-25]: Gate present but criterion reference deliberately replaced by narrative -> halt.
>
> Pass: "ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]: Action specificity (C-05): confirmed.
>   Unlock format (C-12): confirmed. Registry labels (C-14): confirmed. Gate IDs (C-20): confirmed.
>   Label enumeration (C-25): [C-05/C-12/C-14/C-20] verified."

**3G -- STRUCTURAL AUDIT GATE [C-20/C-26]** -- numbered sub-steps [C-23]

> (1) List every gate executed in this run by its full label.
> (2) Confirm each gate label carries at least one criterion ID reference `[C-XX]`. [C-20]
> (3) Confirm LEADERBOARD CLUSTER GATE label enumerates C-16, C-19, C-21. [C-25]
> (4) Confirm ACTIONS CLUSTER GATE label enumerates C-05, C-12, C-14, C-20. [C-25]
> (5) Confirm "STOP. Phase 1 complete. [C-26]" was written after Phase 1. [C-26]
> (6) Confirm "STOP. Phase 2 complete. [C-26]" was written after Phase 2. [C-26]
> (7) Record: "Structural audit: [N] gates checked. [M] STOP barriers verified. Violations: [n]."
>
> Fail Tier 1 [C-25]: Any gate missing criterion ID -> record violation, halt.
> Fail Tier 2 [C-25]: STOP barrier written but missing `[C-26]` reference -> record as finding.
> Fail Tier 3 [C-25]: STOP barrier language present but modified to permit Phase N+1 to alter
>   Phase N output -> halt, flag as highest-severity violation.

**3H -- Write Artifact**

Write to: `simulations/topic/{{topic}}-achievements-{{date}}.md`

---

## V-02 -- Single Axis: Pre-printed Barrier in Output Template

**Axis**: Output format -- phase barriers are pre-printed in the output artifact skeleton as
section dividers. The model fills cells and gate-body lines, but the barriers exist on the page
before execution begins. Compliance is structural: the model cannot skip what is already printed.

**Hypothesis**: Pre-printing the barrier lines eliminates the class of C-26 failures where the
model follows intent (generates sequential output) without writing the seal. A pre-printed
"--- PHASE 1 SEALED [C-26] ---" divider cannot be omitted or reformatted because the model
transcribes it rather than generating it. This is the same structural guarantee mechanism
used for section headers in prior rounds.

---

You are running `corps-achievements`. Scan all signal artifacts for the topic. Compute
achievement state. Show contributor leaderboard and next recommended action.

**INPUT**: `{{topic}}` (auto-detect from context or TOPICS.md if not provided)

---

### REGISTRY PRIMACY GATE [C-24]

Read `simulations/TOPICS.md` before any phase begins.

The topic registry entry for `{{topic}}` is the **sole authoritative gate contract** for this
skill. Phase instructions below are subordinate to the registry. Registry governs on conflict.

FAIL Tier 1 [C-25]: Topic not found in TOPICS.md -> halt.
FAIL Tier 3 [C-25]: Registry classification contradicts phase instruction result -> registry governs.

---

### ATTRIBUTION INTEGRITY GATE [C-24/C-30]

Fires before Phase 1 begins.

(1) Confirm `{{topic}}` in TOPICS.md. [C-24]
(2) Glob `simulations/**/{{topic}}-*.md`. Build ATTRIBUTION BASELINE: file count + contributor list.
(3) Record: `ATTRIBUTION BASELINE: [N] artifacts. Contributors: [list]`.

FAIL Tier 1 [C-25]: 0 artifacts -> halt.
FAIL Tier 3 [C-25]: Achievement names contributor not in ATTRIBUTION BASELINE -> halt.

---

### OUTPUT TEMPLATE

Execute phases in order. Fill all `[FIELD]` values. Do not modify pre-printed section headers,
dividers, or barrier lines. The pre-printed text defines the output structure.

```
## PHASE 1 -- EVIDENCE SCAN

SCAN STATE:
  Namespaces with signals: [list]
  Per-namespace count: [ns: n, ns: n, ...]
  Total signals: [N]
  Milestones (from registry): [M]
  Contributors: [list]
  Earliest: [date]  Latest: [date]

SCAN GATE [C-01/C-15]: [Pass confirmation or Fail finding]

--- PHASE 1 SEALED [C-26] ---
Phase 1 scan results are closed. Phase 2 reads SCAN STATE above. Phase 2 may not
alter signal counts, contributor lists, namespace assignments, or artifact citations.

## PHASE 2 -- ACHIEVEMENT CLASSIFICATION

Achievement rows (one per category, state = EARNED / IN-PROGRESS / LOCKED): [C-01/C-06]

| Category       | Achievement         | State | Evidence [C-03] | Progress [C-04] |
|----------------|---------------------|-------|-----------------|-----------------|
| Exploration    | Namespace Spread    | [   ] | [artifact path] | [n of m or --]  |
| Depth          | Signal Depth        | [   ] | [artifact path] | [n of m or --]  |
| Coverage       | Full Coverage       | [   ] | [artifact path] | [n of m or --]  |
| Quality        | Falsified [C-02]    | [   ] | [artifact path] | [n of m or --]  |
| Chain          | Signal Chain        | [   ] | [artifact path] | [n of m or --]  |
| Discovery      | Unexpected Echo     | [   ] | [artifact path] | [--]            |
| Corps/Crew     | Team Breadth        | [   ] | [artifact path] | [n of m or --]  |

CLASSIFICATION GATE [C-03/C-25]: [Pass confirmation or Fail finding]

1-AWAY TABLE [C-09/C-18]:

| Topic/Milestone | Achievement | Gap | Exact Action |
|-----------------|-------------|-----|--------------|
| [item]          | [name]      | [n] | [action]     |

Pattern assignment [C-17]: [LABEL from registry or NONE]

--- PHASE 2 SEALED [C-26] ---
Phase 2 classifications are closed. Phase 3 reads Phase 2 table above. Phase 3 may not
alter EARNED/IN-PROGRESS/LOCKED assignments or category coverage decisions.

## PHASE 3 -- OUTPUT

PRE-WRITE GATE [C-11]: All values in tables below derive from Phase 1 SCAN STATE and
Phase 2 achievement table. No artifact rescanning required.
[Confirmation: pass / Fail: [specific value requiring rescan]]

LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]:

| Rank | Contributor | Signals | Topics | Milestones | Score | Pattern |
|------|-------------|---------|--------|------------|-------|---------|
| 1    | [name]      | [S]     | [T]    | [M]        | [tot] | [label] |

Worked example Rank 1 [C-19]: Score = [S]x1 + [T]x3 + [M]x5 = [total]
Correction [C-21]: [applied: old->new / not needed]
Label enumeration (C-25): [C-16/C-19/C-21] verified.

**TEAM INSIGHT -- [descriptive name] [C-13]:** [cross-table synthesis finding]

INSIGHT GATE [C-13/C-22]:
(1) Insight names specific pattern or contributor: [confirmed]
(2) Insight not restatement of single row: [confirmed]
(3) Requires cross-table synthesis (not derivable from achievements table alone): [confirmed] [C-22]

ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]:

Next: /[skill-name] [topic] -> produces [artifact-name] -> advances [Achievement] [C-05]
  -> Unlocks [Achievement] -> Breaks [PATTERN] [C-12]

(1) Action names specific skill, artifact, advancement [C-05]: [confirmed]
(2) Unlock chain present [C-12]: [confirmed]
(3) Registry labels exact, no invented labels [C-14]: [confirmed]
(4) Gate IDs present on all gates [C-20]: [confirmed]
(5) Label enumeration (C-25): [C-05/C-12/C-14/C-20] verified.

STRUCTURAL AUDIT GATE [C-20/C-26]:
Gates executed: [list all gate labels]
Criterion IDs present on all gates [C-20]: [confirmed / violations: list]
LEADERBOARD CLUSTER label enumerates C-16, C-19, C-21 [C-25]: [confirmed]
ACTIONS CLUSTER label enumerates C-05, C-12, C-14, C-20 [C-25]: [confirmed]
PHASE 1 barrier "--- PHASE 1 SEALED [C-26] ---" written [C-26]: [confirmed]
PHASE 2 barrier "--- PHASE 2 SEALED [C-26] ---" written [C-26]: [confirmed]
Result: [N] gates checked. [M] barriers verified. Violations: [n]
```

**3H -- Write Artifact**

Write to: `simulations/topic/{{topic}}-achievements-{{date}}.md`

---

## V-03 -- Single Axis: Formal Closure Gate with Verification Sub-steps

**Axis**: Phrasing register -- each phase boundary has a named PHASE N CLOSURE GATE [C-26]
with numbered sub-steps that require the model to verify completeness before proceeding.
Phase sealing is a gate pass, not a statement. The model must explicitly confirm the Phase N
output set is complete, enumerate what was produced, and declare closure before Phase N+1
context appears.

**Hypothesis**: A formal gate with verification sub-steps converts C-26 compliance from a
declaration into a verifiable gate pass. The sub-steps create an auditable record: the
model counted outputs, named them, and declared closure. This is stronger than a bare STOP
line (V-01) because it requires the model to demonstrate that Phase N is done before
proceeding, not just assert it. The weakness is that sub-step text is generated rather than
transcribed -- the model must follow the gate instructions.

---

You are running `corps-achievements`. Scan all signal artifacts for the topic. Compute
achievement state. Show contributor leaderboard and next recommended action.

**INPUT**: `{{topic}}` (auto-detect from context or TOPICS.md if not provided)

---

### OUTPUT SCHEMAS [C-37]

**Achievement row**: `| Category | Achievement | State | Evidence | Progress |`
State = EARNED / IN-PROGRESS / LOCKED (exactly one). [C-01]
Evidence = artifact path from Phase 1 scan. [C-03]
Progress = `n of m [requirement]` for IN-PROGRESS; `--` otherwise. [C-04]

**Leaderboard row**: `| Rank | Contributor | Signals | Topics | Milestones | Score | Pattern |`
Score formula: `(Signals x 1) + (Topics x 3) + (Milestones x 5)` [C-16]

**1-Away row**: `| Topic/Milestone | Achievement | Gap | Exact Action |` [C-09/C-18]

**Next action**: `Next: /[skill] [topic] -> produces [artifact] -> advances [Achievement] -> Unlocks [Achievement] -> Breaks [PATTERN]` [C-05/C-12]

---

### REGISTRY PRIMACY GATE [C-24]

Read `simulations/TOPICS.md` before any phase begins.
Registry entry for `{{topic}}` is the sole authoritative gate contract. Phase instructions
are subordinate. Registry governs on conflict.

FAIL Tier 1 [C-25]: Topic absent from registry -> halt.
FAIL Tier 3 [C-25]: Phase instruction result contradicts registry -> registry governs.

---

### ATTRIBUTION INTEGRITY GATE [C-24/C-30]

Before Phase 1 begins:
(1) Confirm `{{topic}}` in TOPICS.md.
(2) Glob `simulations/**/{{topic}}-*.md`. Record file count and contributors.
(3) ATTRIBUTION BASELINE: `[N] artifacts. Contributors: [list]`.

FAIL Tier 1 [C-25]: 0 artifacts -> halt.
FAIL Tier 3 [C-25]: Achievement names contributor not in baseline -> halt.

---

## PHASE 1 -- EVIDENCE SCAN

**Goal**: Build raw signal inventory. Record counts and citations. No achievement
classification in this phase.

**1A -- Glob and Enumerate**

Glob `simulations/**/{{topic}}-*.md`. For each artifact record:
namespace, file path, date (frontmatter), contributor (frontmatter).

Aggregate per namespace: signal count, unique contributor count.

**SCAN GATE [C-01/C-15]** -- numbered sub-steps [C-23]:

> (1) `simulations/` accessible; glob returned >= 1 file.
> (2) Every file assigned to a known namespace.
> (3) Contributor list matches ATTRIBUTION BASELINE.
> (4) PHASE 1 STATE ready.
>
> Pass: "SCAN GATE [C-01/C-15]: [N] signals, [M] namespaces. Contributors: [list]."
> Fail Tier 1: "SCAN GATE FAIL [C-01/C-15]: [condition] -- [path]."

**1B -- PHASE 1 STATE**

```
PHASE 1 STATE:
  Namespaces with signals: [list]
  Per-namespace count: [ns: n, ...]
  Total signals: N
  Milestones (registry): M
  Contributors: [list]
  Earliest: [date]  Latest: [date]
```

### PHASE 1 CLOSURE GATE [C-26]

> (1) Count items produced in Phase 1: [N namespaces enumerated], [M contributors recorded],
>     [K artifact paths cited]. Record totals.
> (2) Declare Phase 1 output set: "Phase 1 produced: PHASE 1 STATE with [N] namespace entries,
>     [M] contributors, [K] artifact paths."
> (3) Confirm that Phase 2 inputs are limited to items in the declared output set above.
>     Phase 2 may not introduce artifact data not present in PHASE 1 STATE.
> (4) Write the closure seal: "STOP. Phase 1 complete. [C-26]"
>
> Pass: "PHASE 1 CLOSURE GATE [C-26]: [N] namespace entries, [M] contributors, [K] artifact paths.
>   Phase 1 output set declared. Phase 2 inputs constrained. STOP. Phase 1 complete. [C-26]"

---

## PHASE 2 -- ACHIEVEMENT CLASSIFICATION

**Goal**: Classify achievements from PHASE 1 STATE only. Do not rescan. Registry governs. [C-24]

**Achievement Definitions (all 7 required)** [C-06]:

| Category | EARNED Condition | IN-PROGRESS Progress Form | LOCKED Condition |
|----------|-----------------|--------------------------|-----------------|
| Exploration | >= 5 namespaces | `n of 5 namespaces covered` | 0 namespaces |
| Depth | any ns >= 3 signals | `n of 3 signals in [ns]` | no signals |
| Coverage | all 9 namespaces | `n of 9 namespaces` | 0 signals |
| Quality/Falsified [C-02] | prove-* with falsification | `0 of 1 falsification events` | no prove artifacts |
| Chain | story/report citing >= 3 signals | `n of 3 cited signals` | no story/report |
| Discovery | topic-echo exists | -- (binary) | no echo artifact |
| Corps/Crew | >= 2 contributors | `1 of 2 contributors` | 0 contributors |

**Falsified Achievement** [C-02]: Frame as "Followed evidence over assumptions -- investigative
rigor confirmed." when EARNED. Do NOT frame as failure.

**CLASSIFICATION GATE [C-03/C-25]** -- numbered sub-steps [C-23]:

> (1) Every EARNED row cites specific artifact path from PHASE 1 STATE.
> (2) Every IN-PROGRESS row shows `n of m` form.
> (3) All 7 categories appear. [C-06]
> (4) No citation to a path not in PHASE 1 STATE.
>
> Fail Tier 2: Missing citation -> mark `(UNCITED)`, record.
> Fail Tier 3: Citation to absent path -> halt.

**2B -- 1-Away Gaps** [C-09/C-18]

Identify IN-PROGRESS achievements where n = m-1. Emit 1-AWAY TABLE with four columns.

**2C -- Pattern Assignment** [C-17]

Apply first matching label from registry:
SOLO_ISLAND / NAMESPACE_MOAT / SPRINT_FREEZE / SHALLOW_POOL / ORPHAN_TOPIC.
Use `[LABEL from registry]` syntax. No invented labels. [C-14]

**2D -- PHASE 2 STATE**

```
PHASE 2 STATE:
  Rows: [7 entries]
  1-Away count: N
  Pattern: [label or NONE]
  Dominant contributor: [name]
```

### PHASE 2 CLOSURE GATE [C-26]

> (1) Count items produced in Phase 2: [7 achievement rows], [N 1-away entries],
>     [1 pattern assignment]. Record totals.
> (2) Declare Phase 2 output set: "Phase 2 produced: 7 achievement rows ([N] EARNED,
>     [M] IN-PROGRESS, [K] LOCKED), [J] 1-away entries, pattern [LABEL]."
> (3) Confirm that Phase 3 inputs are limited to items in the declared output set above.
>     Phase 3 may not alter EARNED/IN-PROGRESS/LOCKED assignments or category coverage.
> (4) Write the closure seal: "STOP. Phase 2 complete. [C-26]"
>
> Pass: "PHASE 2 CLOSURE GATE [C-26]: 7 rows ([N] EARNED, [M] IN-PROGRESS, [K] LOCKED),
>   [J] 1-away entries, pattern [LABEL]. Phase 2 output set declared. Phase 3 inputs
>   constrained. STOP. Phase 2 complete. [C-26]"

---

## PHASE 3 -- OUTPUT GENERATION

**Goal**: Emit achievement report from Phase 2 STATE. No reclassification.

**PRE-WRITE GATE [C-11]** -- before writing any section:
> "Do all values derive from PHASE 1 STATE and PHASE 2 STATE?
>  If any value requires artifact rescan: derive from state records instead and record finding."

**3A -- Achievements Table** [C-01/C-03/C-04/C-06]

| Category | Achievement | State | Evidence | Progress |
|----------|-------------|-------|----------|----------|

**3B -- 1-Away Gaps Table** [C-09/C-18]

| Topic/Milestone | Achievement | Gap | Exact Action |
|-----------------|-------------|-----|--------------|

**3C -- LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]** -- numbered sub-steps [C-23]:

> (1) Apply formula `Score = (Signals x 1) + (Topics x 3) + (Milestones x 5)`. [C-16]
> (2) Rank descending.
> (3) Worked example Rank 1: `Score = {S}x1 + {T}x3 + {M}x5 = {total}`. [C-19]
> (4) Compare to Score column. Correct if mismatch. [C-21]
> (5) Emit leaderboard.
> (6) Label enumeration (C-25): [C-16/C-19/C-21] verified.
>
> Pass: "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]: Formula (C-16): confirmed.
>   Example (C-19): {total}. Correction (C-21): [applied/not needed].
>   Label enumeration (C-25): [C-16/C-19/C-21] verified."

**3D -- Team Insight** [C-13]

`**TEAM INSIGHT -- [name]:** [cross-table synthesis]`

**INSIGHT GATE [C-13/C-22]** -- numbered sub-steps [C-23]:
> (1) Insight names specific pattern or contributor.
> (2) Not a single-row restatement.
> (3) Requires cross-table synthesis; not derivable from achievements table alone. [C-22]

**3E -- ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]** -- numbered sub-steps [C-23]:

> (1) Draft: `Next: /[skill] [topic] -> produces [artifact] -> advances [Achievement]` [C-05]
> (2) Append: `-> Unlocks [Achievement] -> Breaks [PATTERN]` [C-12]
> (3) Registry labels exact. [C-14]
> (4) Action is specific (skill + artifact + advancement). [C-05]
> (5) All gates in run carry criterion ID `[C-XX]`. [C-20]
> (6) Label enumeration (C-25): [C-05/C-12/C-14/C-20] verified.
>
> Fail Tier 1: Gate missing ID -> halt.
> Fail Tier 3: Gate present but ID replaced by narrative -> halt.

**3F -- STRUCTURAL AUDIT GATE [C-20/C-26]** -- numbered sub-steps [C-23]:

> (1) List all gates executed by full label.
> (2) Confirm each carries criterion ID. [C-20]
> (3) LEADERBOARD CLUSTER enumerates C-16, C-19, C-21. [C-25]
> (4) ACTIONS CLUSTER enumerates C-05, C-12, C-14, C-20. [C-25]
> (5) PHASE 1 CLOSURE GATE [C-26] pass confirmation present. [C-26]
> (6) PHASE 2 CLOSURE GATE [C-26] pass confirmation present. [C-26]
> (7) Record: "[N] gates. [M] closure gates. Violations: [n]."
>
> Fail Tier 1: Gate missing ID -> halt.
> Fail Tier 2: Closure gate present but no pass confirmation recorded -> finding.
> Fail Tier 3: Closure gate present but confirmation falsified (claims seal while permitting
>   Phase N+1 alteration) -> halt, highest-severity violation.

**3G -- Write Artifact**

Write to: `simulations/topic/{{topic}}-achievements-{{date}}.md`

---

## V-04 -- Combined: Terse STOP + Pre-printed Barrier in Template

**Axes**: Lifecycle emphasis (V-01 terse STOP declaration) + Output format (V-02 pre-printed
barrier in template skeleton).

**Hypothesis**: V-01 isolates instruction-based compliance; V-02 isolates structural compliance.
Combining them creates two independent layers: the STOP instruction tells the model what to
do, while the pre-printed barrier in the template ensures the model cannot skip it. The
redundancy addresses the class of failures where the model follows intent but omits the seal
line, and separately the class where the model includes the line but places it after Phase N+1
context has already been introduced.

---

You are running `corps-achievements`. Scan all signal artifacts for the topic. Compute
achievement state. Show contributor leaderboard and next recommended action.

**INPUT**: `{{topic}}` (auto-detect from context or TOPICS.md if not provided)

---

### REGISTRY PRIMACY GATE [C-24]

Read `simulations/TOPICS.md` first. The registry entry for `{{topic}}` is the sole
authoritative gate contract. Phase instructions are subordinate.

FAIL Tier 1 [C-25]: Topic absent -> halt.
FAIL Tier 3 [C-25]: Phase result contradicts registry -> registry governs.

---

### ATTRIBUTION INTEGRITY GATE [C-24/C-30]

Before Phase 1:
(1) Confirm `{{topic}}` in TOPICS.md.
(2) Glob `simulations/**/{{topic}}-*.md`. ATTRIBUTION BASELINE: `[N] artifacts, contributors: [list]`.

FAIL Tier 1 [C-25]: 0 artifacts -> halt.
FAIL Tier 3 [C-25]: Achievement names contributor not in baseline -> halt.

---

### OUTPUT TEMPLATE

Fill all `[FIELD]` values. Do not modify pre-printed headers, dividers, or barrier lines.

```
## PHASE 1 -- EVIDENCE SCAN

SCAN STATE:
  Namespaces: [list]  Per-namespace count: [ns: n, ...]  Total: [N]
  Milestones (registry): [M]  Contributors: [list]
  Earliest: [date]  Latest: [date]

SCAN GATE [C-01/C-15]:
  Pass: "[N] signals, [M] namespaces. Contributors: [list]."
  Fail Tier 1: "SCAN GATE FAIL [C-01/C-15]: [condition] -- [path]."

STOP. Phase 1 complete. [C-26]
--- PHASE 1 SEALED [C-26] ---
Phase 1 scan results are closed. Phase 2 reads SCAN STATE above only.
Phase 2 may not alter signal counts, contributors, or artifact citations.

## PHASE 2 -- ACHIEVEMENT CLASSIFICATION

Achievement table (all 7 categories required [C-06]):

| Category       | Achievement      | State              | Evidence [C-03]  | Progress [C-04]   |
|----------------|------------------|-------------------|------------------|-------------------|
| Exploration    | Namespace Spread | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |
| Depth          | Signal Depth     | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |
| Coverage       | Full Coverage    | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |
| Quality        | Falsified [C-02] | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |
| Chain          | Signal Chain     | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |
| Discovery      | Unexpected Echo  | [EARNED/LOC]      | [artifact path]  | [--]              |
| Corps/Crew     | Team Breadth     | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |

CLASSIFICATION GATE [C-03/C-25]:
  (1) Every EARNED row cites artifact from SCAN STATE.
  (2) Every IN-PROGRESS row shows `n of m`.
  (3) All 7 categories present.
  Fail Tier 2: Missing citation -> `(UNCITED)`.  Fail Tier 3: Absent path -> halt.

1-AWAY TABLE [C-09/C-18]:
| Topic/Milestone | Achievement | Gap | Exact Action |
|-----------------|-------------|-----|--------------|

Pattern [C-17]: [SOLO_ISLAND / NAMESPACE_MOAT / SPRINT_FREEZE / SHALLOW_POOL / ORPHAN_TOPIC / NONE]

STOP. Phase 2 complete. [C-26]
--- PHASE 2 SEALED [C-26] ---
Phase 2 classifications are closed. Phase 3 reads Phase 2 table only.
Phase 3 may not alter EARNED/IN-PROGRESS/LOCKED assignments or category coverage.

## PHASE 3 -- OUTPUT

PRE-WRITE GATE [C-11]: All values derive from Phase 1 SCAN STATE and Phase 2 table.
  [Confirmation or Fail: specific value requiring rescan]

LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]:
  Formula: Score = (Signals x 1) + (Topics x 3) + (Milestones x 5) [C-16]
  | Rank | Contributor | Signals | Topics | Milestones | Score | Pattern |
  Rank 1 example [C-19]: Score = [S]x1 + [T]x3 + [M]x5 = [total]
  Correction [C-21]: [applied: old->new / not needed]
  Label enumeration (C-25): [C-16/C-19/C-21] verified.

**TEAM INSIGHT -- [name] [C-13]:** [finding]
INSIGHT GATE [C-13/C-22]:
  (1) Names specific pattern/contributor.  (2) Not row restatement.
  (3) Requires cross-table synthesis [C-22]: [confirmed]

ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]:
  Next: /[skill] [topic] -> produces [artifact] -> advances [Achievement] [C-05]
    -> Unlocks [Achievement] -> Breaks [PATTERN] [C-12]
  (1) Specific skill+artifact+advancement [C-05]: confirmed
  (2) Unlock chain [C-12]: confirmed
  (3) Registry labels exact [C-14]: confirmed
  (4) Gate IDs on all gates [C-20]: confirmed
  (5) Label enumeration (C-25): [C-05/C-12/C-14/C-20] verified.
  Fail Tier 1: Gate missing ID -> halt.  Fail Tier 3: ID replaced by narrative -> halt.

STRUCTURAL AUDIT GATE [C-20/C-26]:
  Gates executed: [list]
  All carry criterion IDs [C-20]: [confirmed / violations: list]
  LEADERBOARD CLUSTER enumerates C-16,C-19,C-21 [C-25]: [confirmed]
  ACTIONS CLUSTER enumerates C-05,C-12,C-14,C-20 [C-25]: [confirmed]
  STOP barrier after Phase 1 [C-26]: [confirmed]
  STOP barrier after Phase 2 [C-26]: [confirmed]
  "--- PHASE 1 SEALED [C-26] ---" present [C-26]: [confirmed]
  "--- PHASE 2 SEALED [C-26] ---" present [C-26]: [confirmed]
  Result: [N] gates. [2] barriers. Violations: [n].
  Fail Tier 1: Missing ID -> halt.
  Fail Tier 2: Barrier present but [C-26] reference absent -> finding.
  Fail Tier 3: Barrier language permits retroactive alteration -> halt.
```

**Write artifact**: `simulations/topic/{{topic}}-achievements-{{date}}.md`

---

## V-05 -- Full Integration: Terse STOP + Pre-printed Barrier + Formal Closure Gate

**Axes**: All three C-26 mechanisms combined.
- V-01: Terse "STOP. Phase N complete. [C-26]" instruction-based declaration
- V-02: Pre-printed "--- PHASE N SEALED [C-26] ---" divider in the output template
- V-03: Formal PHASE N CLOSURE GATE [C-26] with verification sub-steps

**Hypothesis**: V-01 provides instruction-based declaration. V-02 provides structural
unavoidability. V-03 provides verifiability. Combined, these three layers address distinct
C-26 failure modes: (1) the model omits the seal entirely (blocked by V-02's pre-printed
marker), (2) the model includes the seal but Phase N+1 context bleeds back anyway (addressed
by V-03's gate requiring the model to enumerate and declare the Phase N output set before
proceeding), (3) the seal is present but informal and ambiguous (addressed by V-01's terse
STOP declaration and V-02's structural marker). V-05 is the belt-and-suspenders integration.

---

You are running `corps-achievements`. Scan all signal artifacts for the topic. Compute
achievement state. Show contributor leaderboard and next recommended action.

**INPUT**: `{{topic}}` (auto-detect from context or TOPICS.md if not provided)

---

### OUTPUT SCHEMAS [C-37]

**Achievement row**: `| Category | Achievement | State | Evidence | Progress |`
State: EARNED / IN-PROGRESS / LOCKED (exactly one). [C-01]
Evidence: artifact path from Phase 1 STATE. [C-03]
Progress: `n of m [requirement]` for IN-PROGRESS; `--` otherwise. [C-04]

**Leaderboard row**: `| Rank | Contributor | Signals | Topics | Milestones | Score | Pattern |`

**1-Away row**: `| Topic/Milestone | Achievement | Gap | Exact Action |`

**Next action**: `Next: /[skill] [topic] -> produces [artifact] -> advances [Achievement] -> Unlocks [Achievement] -> Breaks [PATTERN]`

---

### REGISTRY PRIMACY GATE [C-24]

Read `simulations/TOPICS.md` before any phase begins.
The registry entry for `{{topic}}` is the **sole authoritative gate contract** for this skill.
Phase instructions are subordinate. Registry governs on conflict.

FAIL Tier 1 [C-25]: Topic absent -> halt.
FAIL Tier 3 [C-25]: Phase result contradicts registry -> registry governs, record override.

---

### ATTRIBUTION INTEGRITY GATE [C-24/C-30]

Before Phase 1 begins:
(1) Confirm `{{topic}}` in TOPICS.md. [C-24]
(2) Glob `simulations/**/{{topic}}-*.md`. Build ATTRIBUTION BASELINE: file count + contributor list.
(3) Record: `ATTRIBUTION BASELINE: [N] artifacts. Contributors: [list]`.

FAIL Tier 1 [C-25]: 0 artifacts -> halt.
FAIL Tier 2 [C-25]: Some frontmatter missing contributor field -> record count, continue.
FAIL Tier 3 [C-25]: Achievement names contributor not in ATTRIBUTION BASELINE -> halt.

---

### OUTPUT TEMPLATE

Fill all `[FIELD]` values. The pre-printed headers, dividers, and barrier lines define the
output structure. Do not modify them.

```
## PHASE 1 -- EVIDENCE SCAN

SCAN STATE:
  Namespaces with signals: [list]
  Per-namespace count: [ns: n, ns: n, ...]
  Total signals: [N]
  Milestones (from registry): [M]
  Contributors: [list]
  Earliest: [date]  Latest: [date]

SCAN GATE [C-01/C-15]:
  (1) simulations/ accessible; glob >= 1 file.
  (2) All files assigned to known namespace.
  (3) Contributor list matches ATTRIBUTION BASELINE.
  (4) PHASE 1 STATE complete.
  Pass: "SCAN GATE [C-01/C-15]: [N] signals, [M] namespaces. Contributors: [list]."
  Fail Tier 1: "SCAN GATE FAIL [C-01/C-15]: [condition] -- [path]."

PHASE 1 CLOSURE GATE [C-26]:
  (1) Count Phase 1 items: [N] namespace entries, [M] contributors, [K] artifact paths.
  (2) Declare output set: "Phase 1 produced: PHASE 1 STATE with [N] namespace entries,
      [M] contributors, [K] artifact paths."
  (3) Phase 2 inputs are limited to items in the declared output set above. Phase 2 may
      not introduce artifact data not present in PHASE 1 STATE.
  Pass: "PHASE 1 CLOSURE GATE [C-26]: [N] namespace entries, [M] contributors,
    [K] artifact paths. Output set declared. Phase 2 inputs constrained."

STOP. Phase 1 complete. [C-26]
--- PHASE 1 SEALED [C-26] ---
Phase 1 scan results are closed. PHASE 1 STATE is immutable.
Phase 2 reads PHASE 1 STATE above. Phase 2 may not alter signal counts,
contributor lists, namespace assignments, or artifact citations.

## PHASE 2 -- ACHIEVEMENT CLASSIFICATION

Achievement table (use PHASE 1 STATE only; all 7 categories required) [C-06]:

| Category       | Achievement         | State              | Evidence [C-03]  | Progress [C-04]   |
|----------------|---------------------|-------------------|------------------|-------------------|
| Exploration    | Namespace Spread    | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |
| Depth          | Signal Depth        | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |
| Coverage       | Full Coverage       | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |
| Quality        | Falsified [C-02]    | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |
| Chain          | Signal Chain        | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |
| Discovery      | Unexpected Echo     | [EARNED/LOC]      | [artifact path]  | [--]              |
| Corps/Crew     | Team Breadth        | [EARNED/IN-P/LOC] | [artifact path]  | [n of m or --]    |

CLASSIFICATION GATE [C-03/C-25]:
  (1) Every EARNED row cites artifact path from PHASE 1 STATE. [C-03]
  (2) Every IN-PROGRESS row shows `n of m` form. [C-04]
  (3) All 7 categories appear. [C-06]
  (4) No citation to path absent from PHASE 1 STATE.
  Fail Tier 2: Missing citation -> `(UNCITED)`. Fail Tier 3: Absent path -> halt.

1-AWAY TABLE [C-09/C-18]:
| Topic/Milestone | Achievement | Gap | Exact Action |
|-----------------|-------------|-----|--------------|
| [item]          | [name]      | [n] | [action]     |

Pattern [C-17]: [SOLO_ISLAND / NAMESPACE_MOAT / SPRINT_FREEZE / SHALLOW_POOL / ORPHAN_TOPIC / NONE]

PHASE 2 STATE:
  Rows: [7] | 1-Away: [N] | Pattern: [label] | Dominant contributor: [name]

PHASE 2 CLOSURE GATE [C-26]:
  (1) Count Phase 2 items: [7] achievement rows ([N] EARNED, [M] IN-PROGRESS, [K] LOCKED),
      [J] 1-away entries, pattern [LABEL].
  (2) Declare output set: "Phase 2 produced: 7 rows ([N] EARNED, [M] IN-PROGRESS, [K] LOCKED),
      [J] 1-away entries, pattern [LABEL]."
  (3) Phase 3 inputs are limited to items in the declared output set above. Phase 3 may not
      alter EARNED/IN-PROGRESS/LOCKED assignments or category coverage decisions.
  Pass: "PHASE 2 CLOSURE GATE [C-26]: 7 rows ([N] EARNED, [M] IN-PROGRESS, [K] LOCKED),
    [J] 1-away entries, pattern [LABEL]. Output set declared. Phase 3 inputs constrained."

STOP. Phase 2 complete. [C-26]
--- PHASE 2 SEALED [C-26] ---
Phase 2 classifications are closed. PHASE 2 STATE is immutable.
Phase 3 reads PHASE 2 STATE above. Phase 3 may not alter EARNED/IN-PROGRESS/LOCKED
assignments or category coverage decisions.

## PHASE 3 -- OUTPUT

PRE-WRITE GATE [C-11]: All values in tables below derive from PHASE 1 STATE and PHASE 2 STATE.
No artifact rescanning required.
  [Confirmation: pass / Fail: [specific value requiring rescan and corrective action]]

LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]:
  Formula: Score = (Signals x 1) + (Topics x 3) + (Milestones x 5) [C-16]
  | Rank | Contributor | Signals | Topics | Milestones | Score | Pattern |
  Rank 1 worked example [C-19]: Score = [S]x1 + [T]x3 + [M]x5 = [total]
  Correction [C-21]: [applied: [old]->[new] / not needed]
  Label enumeration (C-25): [C-16/C-19/C-21] verified.
  Pass: "LEADERBOARD CLUSTER GATE [C-16/C-19/C-21]: Formula (C-16): confirmed.
    Example (C-19): [total]. Correction (C-21): [applied/not needed].
    Label enumeration (C-25): [C-16/C-19/C-21] verified."

**TEAM INSIGHT -- [descriptive name] [C-13]:** [cross-table synthesis finding not derivable from achievements table alone]

INSIGHT GATE [C-13/C-22]:
  (1) Names specific pattern or contributor: [confirmed]
  (2) Not a single-row restatement: [confirmed]
  (3) Requires cross-table synthesis; not derivable from achievements table alone [C-22]: [confirmed]

ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]:
  Next: /[skill] [topic] -> produces [artifact] -> advances [Achievement] [C-05]
    -> Unlocks [Achievement] -> Breaks [PATTERN] [C-12]
  (1) Names specific skill, artifact, advancement [C-05]: confirmed
  (2) Unlock chain present [C-12]: confirmed
  (3) Registry labels exact, no invented labels [C-14]: confirmed
  (4) All gates in this run carry criterion ID [C-20]: confirmed
  (5) Label enumeration (C-25): [C-05/C-12/C-14/C-20] verified.
  Fail Tier 1: Gate missing criterion ID -> halt, list instances.
  Fail Tier 3: Criterion ID present but replaced by narrative -> halt.
  Pass: "ACTIONS CLUSTER GATE [C-05/C-12/C-14/C-20]: Action (C-05): confirmed.
    Unlock chain (C-12): confirmed. Registry labels (C-14): confirmed.
    Gate IDs (C-20): confirmed. Label enumeration (C-25): [C-05/C-12/C-14/C-20] verified."

STRUCTURAL AUDIT GATE [C-20/C-26]:
  Gates executed: [list all gate labels in this run]
  All carry criterion ID [C-20]: [confirmed / violations: list]
  LEADERBOARD CLUSTER enumerates C-16, C-19, C-21 [C-25]: [confirmed]
  ACTIONS CLUSTER enumerates C-05, C-12, C-14, C-20 [C-25]: [confirmed]
  Phase 1 STOP barrier written [C-26]: [confirmed]
  Phase 1 "--- PHASE 1 SEALED [C-26] ---" pre-printed marker present [C-26]: [confirmed]
  Phase 1 CLOSURE GATE pass confirmation recorded [C-26]: [confirmed]
  Phase 2 STOP barrier written [C-26]: [confirmed]
  Phase 2 "--- PHASE 2 SEALED [C-26] ---" pre-printed marker present [C-26]: [confirmed]
  Phase 2 CLOSURE GATE pass confirmation recorded [C-26]: [confirmed]
  Result: [N] gates checked. [2] STOP barriers. [2] pre-printed markers. [2] closure gate confirmations.
    Violations: [n].
  Fail Tier 1: Gate missing criterion ID -> halt.
  Fail Tier 2: Barrier present but [C-26] reference absent -> finding.
  Fail Tier 3: Barrier or closure gate present but permits retroactive Phase N alteration -> halt.
```

**Write artifact**: `simulations/topic/{{topic}}-achievements-{{date}}.md`

---

## Variation Summary

| Axis | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| Terse STOP declaration | YES | -- | -- | YES | YES |
| Pre-printed barrier in template | -- | YES | -- | YES | YES |
| Formal closure gate + sub-steps | -- | -- | YES | -- | YES |
| C-26 mechanism count | 1 | 1 | 1 | 2 | 3 |

## C-26 Failure Mode Coverage

| Failure Mode | V-01 | V-02 | V-03 | V-04 | V-05 |
|--------------|------|------|------|------|------|
| Seal omitted entirely | Instruction dep. | BLOCKED (pre-printed) | Gate-required | BLOCKED | BLOCKED |
| Seal present but Phase N+1 bleeds back | Partial (declaration only) | Partial (structural) | VERIFIED (gate enumerates output set) | Partial | VERIFIED |
| Seal ambiguous / informal | Minimal risk (terse STOP) | Low (marker present) | Low (gate pass recorded) | Low | Lowest |
| Wrong phase sealed (out of order) | Undetected | Undetected | Detected (sub-step 1 counts items) | Undetected | Detected |
| Seal present, [C-26] reference missing | Partial | Partial | Structural audit catches | Audit catches | Audit catches |

## Predicted C-26 Scoring

| Variation | C-26 Likely? | Confidence | Risk |
|-----------|-------------|------------|------|
| V-01 | PASS | Medium | Model omits STOP line under length pressure |
| V-02 | PASS | High | Pre-printed marker is structural; cannot be omitted |
| V-03 | PASS | Medium-High | Gate sub-steps are generated (not transcribed); model must follow |
| V-04 | PASS | High | Two independent C-26 layers; both must fail simultaneously to miss |
| V-05 | PASS | Highest | Three layers; STOP + pre-printed + gate verification; redundancy maximized |

**Predicted top performer**: V-05 — all three C-26 mechanisms active, plus the structural
audit gate explicitly checks all six C-26 evidence points (2 STOP barriers, 2 pre-printed
markers, 2 closure gate confirmations).

**Predicted C-26 discriminator between V-04 and V-05**: V-04 has the STOP instruction and
the pre-printed marker but no closure gate. V-05 adds the closure gate sub-steps that require
the model to enumerate and declare the Phase N output set before proceeding — this addresses
the retroactive reframing risk directly, which is the core of C-26's definition.


