I now have everything I need. The existing R8/R9 golden files are for `corps-achievements` (team-wide, with contributor leaderboard). The current quest is for `topic-achievements` (per-topic scan) with a fresh v8 rubric (2026-03-17) targeting C-24 (registry primacy) and C-25 (severity-stratified FAIL blocks). Let me generate the five complete variations.

---

# Variate R8 — topic-achievements

**Skill**: `topic-achievements`
**Round**: 8
**Date**: 2026-03-17
**Rubric version**: v8
**Basis**: v7 round produced two separable excellence signals — V-02/V-04 showed registry primacy (C-24); V-03 showed severity-stratified FAIL blocks (C-25). R8 targets both new criteria directly while exploring role sequence, lifecycle emphasis, and phrasing register as independent axes.

---

## Variation Axes Selected

| Axis | Hypothesis | Used In |
|------|------------|---------|
| Registry primacy (C-24) | Declaring the achievement registry as the sole authoritative gate contract prevents per-phase qualification drift — classification is tighter when no phase can silently redefine a gate condition | V-01, V-04, V-05 |
| Role sequence: scanner-first | Completing artifact discovery as a fully terminated step before classification opens prevents classification from operating on a partial inventory — the model cannot classify what it has not yet found | V-02, V-05 |
| Severity-stratified FAIL blocks (C-25) | Three-tier FAIL architecture (structural → completeness → semantic bypass) makes the semantic-bypass tier — the most dangerous failure mode — explicitly named and therefore enforceable | V-03, V-04, V-05 |
| Lifecycle emphasis: explicit phase barriers | "STOP. Phase N complete." language at each boundary prevents later-phase context from bleeding back into earlier-phase outputs | V-05 |
| Phrasing register: conversational | Warm-but-precise framing in the Falsified note and next-action step makes those two outputs more useful in practice without compromising classification fidelity | V-02 |

---

## Achievement Registry (shared reference across all variations)

All five variations draw classification criteria from this catalog. The registry is listed here once; each variation either embeds it with a REGISTRY PRIMACY declaration (V-01, V-04, V-05) or embeds it without that declaration (V-02, V-03).

| ID | Category | Achievement | Gate Condition |
|----|----------|-------------|----------------|
| A-01 | Exploration | First Light | ≥1 signal artifact exists for this topic |
| A-02 | Exploration | Horizon Reached | Artifacts span ≥3 distinct namespaces |
| A-03 | Exploration | Full Spectrum | Artifacts span ≥7 distinct namespaces |
| A-04 | Depth | Signal Depth | ≥3 total signal artifacts for this topic |
| A-05 | Depth | Deep Scan | ≥3 artifacts in any single namespace |
| A-06 | Coverage | Hemisphere | ≥5 of 9 namespaces have ≥1 artifact |
| A-07 | Coverage | Complete Arc | All 9 namespaces have ≥1 artifact |
| A-08 | Quality | Golden Produced | A quest-golden artifact exists for this topic |
| A-09 | Quality | Scored | A quest-score artifact exists for this topic |
| A-10 | Quality | Rubric Defined | A quest-rubric artifact exists for this topic |
| A-11 | Chain | Signal Relay | Any artifact explicitly cites a prior artifact as its input |
| A-12 | Chain | Chain of Three | ≥3 artifacts form a linked input→output chain |
| A-13 | Discovery | **Falsified** | A prove artifact explicitly marks a hypothesis as FALSIFIED |
| A-14 | Discovery | Pivot | A topic-plan artifact was amended in response to signal evidence |
| A-15 | Discovery | Echo Found | A topic-echo artifact contains ≥1 explicitly unexpected finding |
| A-16 | Corps/Crew | Corps Founded | An org artifact marks corps created for this topic |
| A-17 | Corps/Crew | Committee Formed | An org-committee artifact exists for this topic |
| A-18 | Corps/Crew | Crew Reviewed | An org-review artifact exists for this topic |

---

## V-01 — Registry Primacy Declaration

**Axis**: Preamble registry with explicit REGISTRY PRIMACY statement.
**Hypothesis**: Declaring the registry as the sole authoritative source — and explicitly subordinating per-phase elaborations to it — prevents the single most common classification error: a phase instruction that seems to clarify a gate condition but actually narrows or widens it. If the primacy declaration is present, any apparent contradiction between the registry and a phase instruction resolves automatically in favor of the registry.

---

You are running `topic-achievements`. Scan all signal artifacts for a topic and compute its achievement state across all 7 categories. Produce: earned achievements (with dates), in-progress achievements (with numeric progress), locked achievements (gap to unlock), and a specific next recommended action.

Auto-detect the topic from the most recently active topic in `simulations/TOPICS.md`, or accept an explicit topic argument. Execute three phases in sequence. Do not begin Phase 2 until the Phase 1 gate passes. Do not begin Phase 3 until the Phase 2 gate passes.

---

### ACHIEVEMENT REGISTRY

**REGISTRY PRIMACY**: These 18 entries are the sole authoritative gate contracts for this skill. Phase instructions implement these contracts. They do not redefine, qualify, or supplement achievement conditions. Where any phase instruction appears to describe a gate condition differently from this registry, the registry governs.

| ID | Category | Achievement | Gate Condition |
|----|----------|-------------|----------------|
| A-01 | Exploration | First Light | ≥1 signal artifact exists for this topic |
| A-02 | Exploration | Horizon Reached | Artifacts span ≥3 distinct namespaces |
| A-03 | Exploration | Full Spectrum | Artifacts span ≥7 distinct namespaces |
| A-04 | Depth | Signal Depth | ≥3 total signal artifacts |
| A-05 | Depth | Deep Scan | ≥3 artifacts in any single namespace |
| A-06 | Coverage | Hemisphere | ≥5 of 9 namespaces have ≥1 artifact |
| A-07 | Coverage | Complete Arc | All 9 namespaces have ≥1 artifact |
| A-08 | Quality | Golden Produced | quest-golden artifact exists for this topic |
| A-09 | Quality | Scored | quest-score artifact exists for this topic |
| A-10 | Quality | Rubric Defined | quest-rubric artifact exists for this topic |
| A-11 | Chain | Signal Relay | Any artifact explicitly cites a prior artifact as its input |
| A-12 | Chain | Chain of Three | ≥3 artifacts form a linked input→output chain |
| A-13 | Discovery | **Falsified** | A prove artifact explicitly marks a hypothesis as FALSIFIED |
| A-14 | Discovery | Pivot | A topic-plan artifact was amended in response to signal evidence |
| A-15 | Discovery | Echo Found | A topic-echo artifact contains ≥1 explicitly unexpected finding |
| A-16 | Corps/Crew | Corps Founded | An org artifact marks corps created for this topic |
| A-17 | Corps/Crew | Committee Formed | An org-committee artifact exists for this topic |
| A-18 | Corps/Crew | Crew Reviewed | An org-review artifact exists for this topic |

---

## PHASE 1 — ARTIFACT SCAN

Glob `simulations/**/*[topic]*.md`. For every file found, extract:
- Namespace (scout / draft / review / flow / trace / prove / listen / program / topic)
- Skill name (from frontmatter `skill:` or path segment)
- Date (from frontmatter `date:` or filename date segment)
- Notable content flags: FALSIFIED, AMENDED, UNEXPECTED FINDING, CORPS-FOUNDED, COMMITTEE, ORG-REVIEW (scan first 20 lines of each file)

Write the Phase 1 State block (internal, not output):

```
PHASE 1 STATE:
  Topic: [topic]
  Total artifacts: [n]
  Namespaces covered: [list] ([count] of 9)
  Artifacts per namespace: {ns: count, ...}
  Namespace with most artifacts: [ns] ([n])
  Content flags found: [list or "none"]
  Earliest artifact date: [date or "unknown"]
  Chain candidates: [artifacts with input citations, or "none"]
```

**SCAN GATE [C-03/C-15]**:
> "(1) Glob executed; result count written in Phase 1 State.
>  (2) Every artifact assigned to one of the 9 canonical namespace labels.
>  (3) Phase 1 State block complete — no field left blank.
>  (4) No artifact count derived from memory or assumption — counts come from glob results only."
>
> Pass: "SCAN GATE [C-03/C-15]: [n] artifacts, [n] namespaces covered."
> Fail: "SCAN GATE FAIL [C-03/C-15]: condition ([n]) — [specific file or field]."

---

## PHASE 2 — ACHIEVEMENT CLASSIFICATION

For each achievement A-01 through A-18 in the ACHIEVEMENT REGISTRY:
1. State the gate condition verbatim from the registry
2. Apply it to Phase 1 State evidence
3. Assign exactly one state: EARNED, IN-PROGRESS, or LOCKED
4. For EARNED: cite the qualifying artifact path and its date
5. For IN-PROGRESS: express progress as "n of m [unit]" (e.g., "2 of 3 namespaces")
6. For LOCKED: state the specific gap ("needs 1 more artifact in any new namespace")

A-13 (Falsified) receives this treatment: assign EARNED only if Phase 1 found an explicit FALSIFIED flag in a prove artifact. Do not assign EARNED because a hypothesis evolved, was refined, or was not confirmed. Evolution is not falsification.

**CLASSIFY GATE [C-01/C-02/C-04]**:
> "(1) All 18 achievements assigned exactly one state.
>  (2) No achievement has multiple states or an ambiguous state.
>  (3) A-13 (Falsified) state derives from an explicit content flag — not from the absence of
>      confirmatory evidence or from hypothesis evolution.
>  (4) All EARNED entries cite a specific artifact path and date.
>  (5) All IN-PROGRESS entries express progress as n of m."
>
> Pass: "CLASSIFY GATE [C-01/C-02/C-04]: [n] EARNED, [n] IN-PROGRESS, [n] LOCKED."
> Fail: "CLASSIFY GATE FAIL [C-01/C-02/C-04]: achievement [ID], condition ([n]) — [issue]."

---

## PHASE 3 — OUTPUT AND NEXT ACTION

### Frontmatter [C-08]

```yaml
---
skill: topic-achievements
topic: [topic]
date: [date]
earned: [n]
in_progress: [n]
locked: [n]
---
```

### Achievement Table [C-01/C-06/C-07]

```markdown
## Achievement State — [topic] — [date]

| Category | Achievement | State | Evidence / Progress | Date Earned |
|----------|-------------|-------|---------------------|-------------|
| Exploration | First Light | EARNED | simulations/scout/[path] | 2026-03-10 |
| Exploration | Horizon Reached | IN-PROGRESS | 2 of 3 namespaces | — |
| Exploration | Full Spectrum | LOCKED | needs 5 more namespaces | — |
...
```

All 7 categories must appear as labeled groups. EARNED entries must carry the date. IN-PROGRESS entries must show n of m. LOCKED entries must show the gap.

### Falsified Achievement Note [C-02]

Include this section regardless of A-13's state:

```markdown
### Falsified

State: **[EARNED / LOCKED]**

[If EARNED]: Falsification is the strongest honesty signal in the achievement system. The hypothesis
in [artifact path] was falsified on [date] — the team followed evidence over assumptions.

[If LOCKED]: Not yet earned. Falsification is awarded when a prove investigation finds evidence
that contradicts its opening hypothesis and marks the claim FALSIFIED. This is a mark of
investigative rigor, not investigative failure.
```

### Next Recommended Action [C-05]

```markdown
## Next Action

Run **/[skill-name]** for topic **[topic]** to produce a **[artifact-type]** artifact.
This advances **[A-ID: Achievement Name]**[, and **[A-ID: Achievement Name]** if two are unlocked].
[One sentence explaining why this is the highest-leverage next move given the current state.]
```

**OUTPUT GATE [C-05/C-06/C-07/C-08]**:
> "(1) Frontmatter contains earned, in_progress, and locked counts — all three present.
>  (2) Achievement table contains all 7 category labels.
>  (3) Every EARNED entry in the table carries a date.
>  (4) Next Action names a specific skill, artifact type, and at least one achievement ID.
>  (5) Falsified Note section present."
>
> Pass: "OUTPUT GATE [C-05/C-06/C-07/C-08]: passed."
> Fail: "OUTPUT GATE FAIL [C-05/C-06/C-07/C-08]: condition ([n]) — [specific issue]."

Write to `simulations/topic/achievements/[topic]-achievements-[date].md`.

---

## V-02 — Role Sequence: Scanner-First with Terminal Inventory

**Axis**: The artifact scanner role runs to complete termination and writes a named TERMINAL ARTIFACT INVENTORY before the classifier role is permitted to begin. The INVENTORY is a named, checkable output, not an internal state block.
**Hypothesis**: When the artifact inventory is written as a visible, named terminal output rather than an internal scratch block, the classifier cannot operate on a partially populated list. The scanner cannot be "close enough" — it either writes the complete INVENTORY or the gate fails. This prevents the most common scan failure: classification beginning before discovery is complete.

---

You are running `topic-achievements`. Scan all signal artifacts for a topic and compute the achievement state across all 7 categories. Produce: earned achievements (with dates), in-progress achievements (numeric progress), locked achievements (what's needed), and a specific next action.

Auto-detect the topic from `simulations/TOPICS.md` or accept an explicit argument. Execute three phases in sequence. Phase 1 must produce a TERMINAL ARTIFACT INVENTORY before Phase 2 may begin.

---

### ACHIEVEMENT CATALOG

| ID | Category | Achievement | Gate Condition |
|----|----------|-------------|----------------|
| A-01 | Exploration | First Light | ≥1 signal artifact exists |
| A-02 | Exploration | Horizon Reached | Artifacts span ≥3 distinct namespaces |
| A-03 | Exploration | Full Spectrum | Artifacts span ≥7 distinct namespaces |
| A-04 | Depth | Signal Depth | ≥3 total artifacts |
| A-05 | Depth | Deep Scan | ≥3 artifacts in any single namespace |
| A-06 | Coverage | Hemisphere | ≥5 of 9 namespaces covered |
| A-07 | Coverage | Complete Arc | All 9 namespaces covered |
| A-08 | Quality | Golden Produced | quest-golden artifact exists |
| A-09 | Quality | Scored | quest-score artifact exists |
| A-10 | Quality | Rubric Defined | quest-rubric artifact exists |
| A-11 | Chain | Signal Relay | Any artifact cites a prior artifact as input |
| A-12 | Chain | Chain of Three | ≥3 artifacts form a cited input→output chain |
| A-13 | Discovery | **Falsified** | A prove artifact explicitly marks a hypothesis FALSIFIED |
| A-14 | Discovery | Pivot | A topic-plan artifact was amended in response to evidence |
| A-15 | Discovery | Echo Found | A topic-echo artifact contains ≥1 unexpected finding |
| A-16 | Corps/Crew | Corps Founded | An org artifact marks corps created |
| A-17 | Corps/Crew | Committee Formed | An org-committee artifact exists |
| A-18 | Corps/Crew | Crew Reviewed | An org-review artifact exists |

---

## PHASE 1 — SCANNER ROLE: ARTIFACT DISCOVERY

You are the Scanner. Your only job is to discover and enumerate artifacts. You do not classify. You do not make judgments about states. Discovery ends when the TERMINAL ARTIFACT INVENTORY is written and the INVENTORY GATE passes. No other role may proceed until that gate is in print.

**Step 1A — Glob**

Execute glob: `simulations/**/*[topic]*.md`. Record the file count.

**Step 1B — Enumerate**

For each file found, write one row:

```
| [path] | [namespace] | [skill] | [date] | [flags: FALSIFIED/AMENDED/UNEXPECTED/CORPS/COMMITTEE/ORG-REVIEW or "—"] |
```

Namespace is one of: scout, draft, review, flow, trace, prove, listen, program, topic.
Flags: scan first 20 lines. Record only flags explicitly present.

**Step 1C — Write TERMINAL ARTIFACT INVENTORY**

```markdown
## TERMINAL ARTIFACT INVENTORY — [topic] — [date]

| Path | Namespace | Skill | Date | Flags |
|------|-----------|-------|------|-------|
| ... | ... | ... | ... | ... |

Total: [n] artifacts
Namespaces covered: [list] ([n] of 9)
Namespace counts: [ns: n, ...]
Namespace with most artifacts: [ns] ([n])
Earliest date: [date]
Chain candidates (artifacts with input citations): [list or "none"]
```

**INVENTORY GATE [C-03/C-15]**:

STOP. The INVENTORY GATE must pass before Phase 2 begins.

> "(1) TERMINAL ARTIFACT INVENTORY table is written and visible above.
>  (2) Row count in table equals glob result count.
>  (3) Every row has a namespace from the canonical 9 — no 'unknown' namespaces.
>  (4) Summary totals (Total, Namespaces covered, Namespace counts) derived from the table above, not from memory.
>  (5) Flags column shows only flags actually found in file content."
>
> Pass: "INVENTORY GATE [C-03/C-15]: [n] artifacts enumerated. Phase 2 may begin."
> Fail: "INVENTORY GATE FAIL [C-03/C-15]: condition ([n]) — [specific row or field]. Phase 2 blocked."

---

## PHASE 2 — CLASSIFIER ROLE: ACHIEVEMENT CLASSIFICATION

You are the Classifier. The TERMINAL ARTIFACT INVENTORY from Phase 1 is your complete and final evidence base. Do not glob again. Do not reference files not in the Inventory. Apply each gate condition from the ACHIEVEMENT CATALOG to the Inventory evidence and assign one state.

For each A-01 through A-18:
- EARNED: cite the exact Inventory row (path + date)
- IN-PROGRESS: write "n of m [unit]" (e.g., "2 of 3 namespaces")
- LOCKED: write the gap in specific terms ("needs 1 more namespace — currently covers 4 of 5")

A-13 (Falsified): EARNED only if the Inventory contains a row where Flags includes FALSIFIED. Not EARNED because a hypothesis was refined, superseded, or not confirmed.

Build the classification table:

```markdown
| ID | Achievement | State | Evidence / Progress | Date |
|----|-------------|-------|---------------------|------|
| A-01 | First Light | EARNED | simulations/scout/[...] | 2026-03-10 |
| A-02 | Horizon Reached | IN-PROGRESS | 2 of 3 namespaces | — |
...
```

**CLASSIFY GATE [C-01/C-02/C-04]**:
> "(1) All 18 rows present. Each has exactly one state.
>  (2) A-13 state derives from FALSIFIED flag in Inventory — not from content inference.
>  (3) Every EARNED row cites an Inventory path.
>  (4) Every IN-PROGRESS row has n of m format.
>  (5) No row references a file outside the TERMINAL ARTIFACT INVENTORY."
>
> Pass: "CLASSIFY GATE [C-01/C-02/C-04]: [n] EARNED, [n] IN-PROGRESS, [n] LOCKED."
> Fail: "CLASSIFY GATE FAIL [C-01/C-02/C-04]: achievement [ID], condition ([n]) — [issue]."

---

## PHASE 3 — OUTPUT

### Frontmatter [C-08]

```yaml
---
skill: topic-achievements
topic: [topic]
date: [date]
earned: [n]
in_progress: [n]
locked: [n]
---
```

### Achievement State Table [C-01/C-06/C-07]

Organize the classification table by category. Group rows under labeled category headers. Every EARNED row must show a date. Every IN-PROGRESS row must show n of m.

### Falsified Note [C-02]

Whether A-13 is earned or locked, write this section:

> "The Falsified achievement rewards intellectual honesty. It is earned when a prove investigation
> discovers evidence that contradicts its opening hypothesis — when the team follows the evidence
> rather than confirming what they expected to find. [State: EARNED/not yet earned.] [If EARNED:
> Earned on [date] via [artifact path].] [If LOCKED: It can be unlocked by running /prove-hypothesis,
> following the evidence, and marking the claim FALSIFIED if the evidence does not support it.]"

### Next Action [C-05]

Name the single highest-leverage next step:

> "Run **/[skill]** for **[topic]** → produces **[artifact type]** → unlocks **[A-ID: Name]**
> [and **[A-ID: Name]** if two]. [One sentence on why this is the priority move.]"

**OUTPUT GATE [C-05/C-06/C-07/C-08]**:
> "(1) Frontmatter has earned, in_progress, locked counts.
>  (2) All 7 category labels present in table.
>  (3) All EARNED rows have dates.
>  (4) Next Action names a skill, artifact type, and achievement ID.
>  (5) Falsified Note written."
>
> Pass: "OUTPUT GATE: passed."
> Fail: "OUTPUT GATE FAIL: condition ([n]) — [issue]."

Write to `simulations/topic/achievements/[topic]-achievements-[date].md`.

---

## V-03 — Severity-Stratified FAIL Blocks

**Axis**: Every gate carries a three-tier FAIL block: Tier 1 (structural — required fields or labels absent), Tier 2 (completeness — fields present but insufficiently populated), Tier 3 (semantic bypass — fields present with correct form but intent circumvented).
**Hypothesis**: The third tier is the critical one. Tier 3 catches the output that looks correct on inspection — the state assignment present, the date present, the n of m present — but whose values were generated from assumption rather than from actual artifact evidence. Naming the tier forces an explicit check: do the values in the output trace to the artifact scan, or were they inferred?

---

You are running `topic-achievements`. Scan all signal artifacts for a topic and compute achievement state across all 7 categories. Produce: earned achievements (with dates), in-progress achievements (numeric progress), locked achievements (gap to unlock), and a specific next action.

Auto-detect topic from `simulations/TOPICS.md` or accept an explicit argument. Execute three phases in sequence. Do not begin a phase until the previous phase's gate passes.

---

### ACHIEVEMENT CATALOG

| ID | Category | Achievement | Gate Condition |
|----|----------|-------------|----------------|
| A-01 | Exploration | First Light | ≥1 signal artifact exists for this topic |
| A-02 | Exploration | Horizon Reached | Artifacts span ≥3 distinct namespaces |
| A-03 | Exploration | Full Spectrum | Artifacts span ≥7 distinct namespaces |
| A-04 | Depth | Signal Depth | ≥3 total artifacts |
| A-05 | Depth | Deep Scan | ≥3 artifacts in any single namespace |
| A-06 | Coverage | Hemisphere | ≥5 of 9 namespaces covered |
| A-07 | Coverage | Complete Arc | All 9 namespaces covered |
| A-08 | Quality | Golden Produced | quest-golden artifact exists |
| A-09 | Quality | Scored | quest-score artifact exists |
| A-10 | Quality | Rubric Defined | quest-rubric artifact exists |
| A-11 | Chain | Signal Relay | Any artifact explicitly cites a prior artifact as input |
| A-12 | Chain | Chain of Three | ≥3 artifacts form a linked input→output chain |
| A-13 | Discovery | **Falsified** | A prove artifact explicitly marks a hypothesis FALSIFIED |
| A-14 | Discovery | Pivot | A topic-plan artifact amended in response to signal evidence |
| A-15 | Discovery | Echo Found | A topic-echo artifact contains ≥1 unexpected finding |
| A-16 | Corps/Crew | Corps Founded | An org artifact marks corps created for this topic |
| A-17 | Corps/Crew | Committee Formed | An org-committee artifact exists |
| A-18 | Corps/Crew | Crew Reviewed | An org-review artifact exists |

---

## PHASE 1 — ARTIFACT SCAN

Glob `simulations/**/*[topic]*.md`. Extract namespace, skill, date, and content flags (FALSIFIED, AMENDED, UNEXPECTED FINDING, CORPS-FOUNDED, COMMITTEE, ORG-REVIEW) from each file.

Write Phase 1 State:

```
PHASE 1 STATE:
  Topic: [topic]
  Total artifacts: [n]
  Namespaces covered: [list] ([n] of 9)
  Per-namespace counts: {ns: n, ...}
  Max namespace depth: [ns] ([n] artifacts)
  Flags found: [list or "none"]
  Earliest date: [date]
```

**SCAN GATE [C-03/C-15]**:

PASS condition: "SCAN GATE [C-03/C-15]: [n] artifacts, [n] namespaces."

FAIL — Tier 1 (structural): Phase 1 State block absent, or glob not executed, or Total artifacts field blank.
FAIL — Tier 2 (completeness): Phase 1 State block present but a field is blank or "unknown"; or a namespace is labeled "other" rather than one of the 9 canonical labels.
FAIL — Tier 3 (semantic bypass): All fields populated with plausible values, but counts are not derived from the glob result — they were generated from prior knowledge, estimated, or fabricated. Specific check: does Total artifacts match the actual row count from the glob? State `"Tier 3 check: Total=[n], row count=[n], match=[YES/NO]."` A NO here is a Tier 3 failure.

---

## PHASE 2 — ACHIEVEMENT CLASSIFICATION

For each A-01 through A-18, apply the gate condition to Phase 1 State and assign one state.

EARNED → cite the exact artifact path and date from Phase 1 State.
IN-PROGRESS → write "n of m [unit]" (e.g., "3 of 5 namespaces").
LOCKED → write the specific gap.

Special treatment for A-13 (Falsified): the gate passes only when Phase 1 State records an explicit FALSIFIED flag on a prove artifact. Hypothesis evolution, claim refinement, and inconclusive investigations do not satisfy this gate.

**CLASSIFY GATE [C-01/C-02/C-04]**:

PASS condition: "CLASSIFY GATE [C-01/C-02/C-04]: [n] EARNED, [n] IN-PROGRESS, [n] LOCKED."

FAIL — Tier 1 (structural): Any of the 18 achievement IDs absent from the classification output; or any row lacks a state label.
FAIL — Tier 2 (completeness): A state is present but the required supporting field is empty — EARNED without a cited path, IN-PROGRESS without n of m, LOCKED without a stated gap.
FAIL — Tier 3 (semantic bypass): All required fields populated, but a value was not derived from Phase 1 State. Specific checks:
- EARNED on A-13 without a FALSIFIED flag in Phase 1 State: Tier 3 failure. State: `"A-13 Tier 3 check: FALSIFIED flag in Phase 1 = [YES/NO]. EARNED assignment [valid/INVALID]."`
- EARNED on any artifact-existence achievement (A-08, A-09, A-10, A-16, A-17, A-18) without a corresponding artifact in Phase 1 State: Tier 3 failure. State the check for each.
- Namespace count in A-02/A-03/A-06/A-07 not matching Phase 1 State namespace count: Tier 3 failure.

---

## PHASE 3 — OUTPUT AND NEXT ACTION

### Frontmatter [C-08]

```yaml
---
skill: topic-achievements
topic: [topic]
date: [date]
earned: [n]
in_progress: [n]
locked: [n]
---
```

### Achievement Table [C-01/C-06/C-07]

Grouped by category (7 labeled groups). EARNED rows carry dates. IN-PROGRESS rows show n of m.

### Falsified Note [C-02]

Include regardless of A-13 state. Frame falsification as evidence of investigative rigor — "followed evidence over assumptions" — not as failure.

### Next Action [C-05]

Name the single highest-leverage next step with skill name, artifact type, and achievement ID(s).

**OUTPUT GATE [C-05/C-06/C-07/C-08]**:

PASS condition: "OUTPUT GATE [C-05/C-06/C-07/C-08]: passed."

FAIL — Tier 1 (structural): Frontmatter block absent; or achievement table absent; or Falsified Note absent; or Next Action absent.
FAIL — Tier 2 (completeness): Frontmatter present but missing one of earned/in_progress/locked; or a category group label missing from the table; or Next Action present but skill name not specified.
FAIL — Tier 3 (semantic bypass): All sections present with correct form, but Next Action names a skill whose output cannot advance the cited achievement. Check: does the skill named in Next Action produce an artifact type that satisfies the gate condition of the cited achievement? If not, the recommendation is formally correct but intent is bypassed. State: `"Next Action Tier 3 check: [skill] → [artifact type] → does it satisfy [A-ID] gate? [YES/NO]."`

Write to `simulations/topic/achievements/[topic]-achievements-[date].md`.

---

## V-04 — Registry Primacy + Severity-Stratified FAIL Blocks

**Axis**: C-24 and C-25 combined — preamble registry with REGISTRY PRIMACY declaration, plus three-tier FAIL blocks on every gate.
**Hypothesis**: The registry establishes what passes; stratified FAIL blocks specify precisely what does not. Together they form a complete gate contract: the registry is the positive definition, and the Tier 3 FAIL block is the explicit guard against the most dangerous failure — an output that satisfies form but circumvents purpose. Neither property alone is sufficient; C-24 without C-25 leaves the FAIL surface undefined, and C-25 without C-24 leaves the gate contract subject to per-phase drift.

---

You are running `topic-achievements`. Scan all signal artifacts for a topic and compute achievement state across all 7 categories. Produce: earned achievements (with dates), in-progress achievements (numeric progress), locked achievements (gap to unlock), and a specific next action.

Auto-detect topic from `simulations/TOPICS.md` or accept an explicit argument. Execute three phases in sequence. Do not begin a phase until the previous phase's gate passes.

---

### ACHIEVEMENT REGISTRY

**REGISTRY PRIMACY**: The definitions in this table are the sole authoritative gate contracts for `topic-achievements`. Phase instructions implement these contracts. They do not redefine, narrow, widen, or supplement gate conditions. Where any phase instruction appears to describe a gate condition differently from this registry, the registry governs.

| ID | Category | Achievement | Gate Condition |
|----|----------|-------------|----------------|
| A-01 | Exploration | First Light | ≥1 signal artifact exists for this topic |
| A-02 | Exploration | Horizon Reached | Artifacts span ≥3 distinct namespaces |
| A-03 | Exploration | Full Spectrum | Artifacts span ≥7 distinct namespaces |
| A-04 | Depth | Signal Depth | ≥3 total artifacts |
| A-05 | Depth | Deep Scan | ≥3 artifacts in any single namespace |
| A-06 | Coverage | Hemisphere | ≥5 of 9 namespaces covered |
| A-07 | Coverage | Complete Arc | All 9 namespaces covered |
| A-08 | Quality | Golden Produced | quest-golden artifact exists for this topic |
| A-09 | Quality | Scored | quest-score artifact exists for this topic |
| A-10 | Quality | Rubric Defined | quest-rubric artifact exists for this topic |
| A-11 | Chain | Signal Relay | Any artifact explicitly cites a prior artifact as input |
| A-12 | Chain | Chain of Three | ≥3 artifacts form a linked input→output chain |
| A-13 | Discovery | **Falsified** | A prove artifact explicitly marks a hypothesis FALSIFIED |
| A-14 | Discovery | Pivot | A topic-plan artifact amended in response to signal evidence |
| A-15 | Discovery | Echo Found | A topic-echo artifact contains ≥1 unexpected finding |
| A-16 | Corps/Crew | Corps Founded | An org artifact marks corps created for this topic |
| A-17 | Corps/Crew | Committee Formed | An org-committee artifact exists |
| A-18 | Corps/Crew | Crew Reviewed | An org-review artifact exists |

These 18 entries are complete and self-sufficient for inspection. No phase instruction is required to understand what qualifies an artifact for any gate. The gate conditions above are the definitions; phase instructions describe mechanics only.

---

## PHASE 1 — ARTIFACT SCAN

Glob `simulations/**/*[topic]*.md`. For each file: extract namespace (one of the 9 canonical), skill, date, and content flags (FALSIFIED, AMENDED, UNEXPECTED FINDING, CORPS-FOUNDED, COMMITTEE, ORG-REVIEW).

Write Phase 1 State:

```
PHASE 1 STATE:
  Topic: [topic]
  Total: [n]
  Namespaces: [list] ([n] of 9)
  Per-namespace: {ns: n, ...}
  Flags: [list or "none"]
  Earliest date: [date]
```

**SCAN GATE [C-03/C-15]**:

PASS: `"SCAN GATE [C-03/C-15]: [n] artifacts, [n] namespaces."`

FAIL — Tier 1 (structural): Phase 1 State block not written; or Total field blank or absent.
FAIL — Tier 2 (completeness): State block present but a namespace listed as "other/unknown"; or Namespaces count contradicts the per-namespace list.
FAIL — Tier 3 (semantic bypass): All fields present and plausible, but Total or per-namespace counts not derived from glob results. State: `"Tier 3 check: glob row count = [n], Total field = [n], match = [YES/NO]."` NO = Tier 3 failure.

---

## PHASE 2 — ACHIEVEMENT CLASSIFICATION

For each A-01 through A-18 from the ACHIEVEMENT REGISTRY, apply the registry gate condition to Phase 1 State. Assign exactly one state. EARNED → cite artifact path and date. IN-PROGRESS → write n of m. LOCKED → write specific gap.

A-13 (Falsified): the registry gate condition requires an explicit FALSIFIED flag on a prove artifact. This is the complete and final definition. No phase instruction supplements it.

**CLASSIFY GATE [C-01/C-02/C-04]**:

PASS: `"CLASSIFY GATE [C-01/C-02/C-04]: [n] EARNED, [n] IN-PROGRESS, [n] LOCKED."`

FAIL — Tier 1 (structural): Fewer than 18 achievement rows in the output; or any row lacks a state value; or A-13 row absent.
FAIL — Tier 2 (completeness): Any EARNED row missing an artifact path; any IN-PROGRESS row missing n of m; any LOCKED row missing a stated gap.
FAIL — Tier 3 (semantic bypass): Form is complete but a state assignment contradicts the registry gate condition when checked against Phase 1 State evidence. Mandatory checks:
- A-13 EARNED without FALSIFIED flag in Phase 1 State: `"A-13 Tier 3: FALSIFIED flag = [YES/NO]."`
- A-01 EARNED when Phase 1 Total = 0: impossible without hallucination.
- A-02/A-06 namespace count in evidence cell mismatches Phase 1 per-namespace total: `"A-02 Tier 3: evidence says [n] namespaces, Phase 1 State says [n]."`
- Any flag-dependent achievement (A-08–A-18) EARNED without corresponding flag or artifact in Phase 1 State.

---

## PHASE 3 — OUTPUT AND NEXT ACTION

### Frontmatter [C-08]

```yaml
---
skill: topic-achievements
topic: [topic]
date: [date]
earned: [n]
in_progress: [n]
locked: [n]
---
```

### Achievement Table [C-01/C-06/C-07]

Seven labeled category groups. EARNED rows carry dates. IN-PROGRESS rows show n of m. LOCKED rows show the gap.

### Falsified Note [C-02]

Present regardless of A-13 state. Frame as honesty signal: "followed evidence over assumptions." Do not frame as failure or as absence.

### Next Action [C-05]

One highest-leverage step: skill name, artifact type, achievement ID(s) it advances.

**OUTPUT GATE [C-05/C-06/C-07/C-08]**:

PASS: `"OUTPUT GATE [C-05/C-06/C-07/C-08]: passed."`

FAIL — Tier 1 (structural): Any required section (frontmatter, achievement table, Falsified Note, Next Action) absent.
FAIL — Tier 2 (completeness): Frontmatter missing earned/in_progress/locked; table missing a category label; Next Action missing skill name or achievement ID.
FAIL — Tier 3 (semantic bypass): Next Action names a skill whose artifact type cannot satisfy the cited achievement's registry gate condition. State: `"Next Action Tier 3: [skill] → [artifact] → satisfies [A-ID] gate? [YES/NO]."`

Write to `simulations/topic/achievements/[topic]-achievements-[date].md`.

---

## V-05 — Full Integration: Registry Primacy + Stratified FAIL + Scanner Isolation + Phase Barriers

**Axis**: All of V-04 (registry primacy + stratified FAIL) plus scanner role isolation with an explicit STOP barrier after Phase 1, and explicit phase-entry/exit contracts between all three phases.
**Hypothesis**: The two structural properties (registry primacy, stratified FAIL) eliminate classification contract ambiguity. Scanner isolation prevents premature classification. Phase barriers prevent cross-phase context bleeding. These four properties address different failure modes and do not trade off against each other — combining them should yield the most reliable classification without any single property weakening another.

---

You are running `topic-achievements`. Scan all signal artifacts for a topic and compute the achievement state across all 7 categories. Produce: earned achievements (with dates), in-progress achievements (numeric progress), locked achievements (gap to unlock), and a specific next recommended action.

Auto-detect topic from `simulations/TOPICS.md` or accept an explicit argument. **Execute phases in strict sequence. Each phase ends with a STOP. Do not read the next phase's instructions until the current phase's gate passes.**

---

### ACHIEVEMENT REGISTRY

**REGISTRY PRIMACY**: These definitions are the sole authoritative gate contracts for this skill. Phase instructions describe mechanics and enforce these contracts. They do not redefine gate conditions. If a phase instruction appears to qualify a condition differently from this registry, the registry governs.

| ID | Category | Achievement | Gate Condition |
|----|----------|-------------|----------------|
| A-01 | Exploration | First Light | ≥1 signal artifact exists for this topic |
| A-02 | Exploration | Horizon Reached | Artifacts span ≥3 distinct namespaces |
| A-03 | Exploration | Full Spectrum | Artifacts span ≥7 distinct namespaces |
| A-04 | Depth | Signal Depth | ≥3 total artifacts |
| A-05 | Depth | Deep Scan | ≥3 artifacts in any single namespace |
| A-06 | Coverage | Hemisphere | ≥5 of 9 namespaces covered |
| A-07 | Coverage | Complete Arc | All 9 namespaces covered |
| A-08 | Quality | Golden Produced | quest-golden artifact exists |
| A-09 | Quality | Scored | quest-score artifact exists |
| A-10 | Quality | Rubric Defined | quest-rubric artifact exists |
| A-11 | Chain | Signal Relay | Any artifact explicitly cites a prior artifact as input |
| A-12 | Chain | Chain of Three | ≥3 artifacts form a linked input→output chain |
| A-13 | Discovery | **Falsified** | A prove artifact explicitly marks a hypothesis FALSIFIED |
| A-14 | Discovery | Pivot | A topic-plan artifact amended in response to signal evidence |
| A-15 | Discovery | Echo Found | A topic-echo artifact contains ≥1 unexpected finding |
| A-16 | Corps/Crew | Corps Founded | An org artifact marks corps created |
| A-17 | Corps/Crew | Committee Formed | An org-committee artifact exists |
| A-18 | Corps/Crew | Crew Reviewed | An org-review artifact exists |

The 18 entries above are complete and self-sufficient for inspection without reference to any phase instruction. No phase elaborates or qualifies a gate condition listed here.

---

## PHASE 1 — SCANNER ROLE: ARTIFACT DISCOVERY

**PHASE 1 ENTRY**: You are the Scanner. Classification is not permitted in this phase. Your output is the ARTIFACT INVENTORY TABLE and nothing else. You have no knowledge of what the Classifier will do with this table.

**Step 1A — Glob**: Execute `simulations/**/*[topic]*.md`. Record the row count.

**Step 1B — Build ARTIFACT INVENTORY TABLE**: For each file:

```
| Path | Namespace | Skill | Date | Flags |
|------|-----------|-------|------|-------|
```

- Namespace: one of scout / draft / review / flow / trace / prove / listen / program / topic
- Date: from frontmatter `date:` or filename segment
- Flags: scan first 20 lines; record FALSIFIED, AMENDED, UNEXPECTED FINDING, CORPS-FOUNDED, COMMITTEE, ORG-REVIEW if present; write "—" otherwise

**Step 1C — Write Summary Block**:

```
ARTIFACT INVENTORY SUMMARY:
  Total rows: [n]
  Namespaces: [list] ([n] of 9)
  Per-namespace counts: {ns: n, ...}
  Deepest namespace: [ns] ([n])
  Content flags: [list or "none"]
  Earliest artifact date: [date]
```

**INVENTORY GATE [C-03/C-15]**:

PASS: `"INVENTORY GATE [C-03/C-15]: [n] artifacts enumerated. Phase 2 may begin."`

FAIL — Tier 1 (structural): ARTIFACT INVENTORY TABLE absent; or Summary Block absent; or Total rows field blank.
FAIL — Tier 2 (completeness): Any row has "unknown" namespace; or Total rows contradicts table row count; or any flag cell is blank rather than "—".
FAIL — Tier 3 (semantic bypass): Table and Summary present with plausible values, but Summary Total does not equal actual table row count. The Tier 3 check is mandatory: `"Tier 3 check: table rows counted = [n], Summary Total = [n], match = [YES/NO]."` If NO, Phase 2 is blocked until the discrepancy is resolved.

**PHASE 1 EXIT — STOP.**
Phase 1 is complete. The ARTIFACT INVENTORY TABLE and INVENTORY SUMMARY are the classifier's complete evidence base.
Do not proceed to Phase 2 instructions until the INVENTORY GATE pass statement is in print.

---

## PHASE 2 — CLASSIFIER ROLE: ACHIEVEMENT CLASSIFICATION

**PHASE 2 ENTRY**: You are the Classifier. Your evidence base is the ARTIFACT INVENTORY TABLE produced in Phase 1. Do not glob again. Do not reference files outside the Inventory. Do not consult prior session knowledge about this topic's artifact state.

For each A-01 through A-18, apply the registry gate condition to the Inventory and assign exactly one state:
- EARNED: registry gate condition satisfied → cite Inventory row (path + date)
- IN-PROGRESS: condition partially met → write "n of m [unit]"
- LOCKED: condition not met → write specific gap ("needs 2 more namespaces — currently [n] of [m]")

A-13 (Falsified) specific protocol: EARNED requires FALSIFIED flag in at least one prove-namespace Inventory row. Check the Flags column explicitly. Do not infer falsification from file names, dates, or content summaries.

**CLASSIFY GATE [C-01/C-02/C-04]**:

PASS: `"CLASSIFY GATE [C-01/C-02/C-04]: [n] EARNED, [n] IN-PROGRESS, [n] LOCKED."`

FAIL — Tier 1 (structural): Fewer than 18 rows in the classification output; or any row has no state; or A-13 absent.
FAIL — Tier 2 (completeness): EARNED row missing Inventory path; IN-PROGRESS row missing n of m; LOCKED row missing gap statement.
FAIL — Tier 3 (semantic bypass): Form complete, but state contradicts the Inventory when checked. Mandatory tier 3 checks:
- `"A-13 Tier 3: Flags column has FALSIFIED on prove row? [YES/NO]. EARNED assignment [valid/INVALID]."`
- For each flag-dependent achievement (A-08–A-18): `"[A-ID] Tier 3: qualifying Inventory row present? [YES/NO]."`
- For each count-based achievement (A-01–A-07): `"[A-ID] Tier 3: count in evidence cell matches Inventory Summary? [YES/NO]."`

If any Tier 3 check returns NO: state `"CLASSIFY GATE TIER 3 FAIL [C-01/C-02/C-04]: [A-ID] — [specific contradiction]."` Correct the state assignment before proceeding.

**PHASE 2 EXIT — STOP.**
Phase 2 is complete. The classification table is final and locked.
Do not proceed to Phase 3 instructions until the CLASSIFY GATE pass statement is in print.

---

## PHASE 3 — OUTPUT ROLE: ARTIFACT WRITE

**PHASE 3 ENTRY**: You are the Output Writer. The classification table from Phase 2 is final. Your job is to format, enrich with the Falsified Note, produce the Next Action, and write the artifact.

### Frontmatter [C-08]

```yaml
---
skill: topic-achievements
topic: [topic]
date: [date]
earned: [n]
in_progress: [n]
locked: [n]
---
```

### Achievement Table [C-01/C-06/C-07]

Organize by 7 labeled category groups. Copy state, evidence, and date from the Phase 2 classification table. EARNED entries carry the date from the Inventory. IN-PROGRESS entries show n of m. LOCKED entries show the gap.

### Falsified Note [C-02]

Present for every run regardless of A-13 state. Use warm, honest framing:

> "The Falsified achievement is the most important signal in the achievement system. It recognizes
> that the investigation followed evidence rather than assumptions — and that the team was willing to
> say so. [If EARNED: Earned on [date] via [path]. The opening hypothesis did not survive contact
> with the evidence. That is the correct outcome.] [If LOCKED: It is unlocked by running
> /prove-hypothesis, following the evidence wherever it leads, and marking the claim FALSIFIED when
> the evidence contradicts the opening hypothesis. The achievement cannot be forced — it can only
> be earned by genuinely being wrong and saying so.]"

### Next Action [C-05]

One highest-leverage next step. Recommend the specific next skill given current achievement gaps — prioritize an IN-PROGRESS achievement that is closest to flipping to EARNED, unless Falsified is not yet earned and prove work is clearly missing.

Format:
> "Run **/[skill]** for **[topic]** to produce a **[artifact type]** signal artifact.
> This advances **[A-ID: Achievement Name]** [and optionally **[A-ID: Name]**].
> [One sentence: why this is the right move now given the specific gap.]"

**OUTPUT GATE [C-05/C-06/C-07/C-08]**:

PASS: `"OUTPUT GATE [C-05/C-06/C-07/C-08]: passed."`

FAIL — Tier 1 (structural): Any section (frontmatter, achievement table, Falsified Note, Next Action) absent.
FAIL — Tier 2 (completeness): Frontmatter missing any of earned/in_progress/locked; table missing any of the 7 category labels; Next Action missing skill name or achievement ID.
FAIL — Tier 3 (semantic bypass): All sections present and well-formed, but Next Action recommends a skill that cannot produce an artifact satisfying the cited achievement's registry gate condition. State: `"Next Action Tier 3: /[skill] → [artifact type] → satisfies A-[ID] gate ([condition])? [YES/NO]."` If NO, revise the recommendation.

Write to `simulations/topic/achievements/[topic]-achievements-[date].md`.

---

## Summary

| Variation | Axis | C-24 (Registry Primacy) | C-25 (Stratified FAIL) | Scanner Isolation | Phase Barriers |
|-----------|------|------------------------|------------------------|-------------------|----------------|
| V-01 | Registry primacy | YES — explicit REGISTRY PRIMACY declaration | No — flat FAIL | No | No |
| V-02 | Role sequence: scanner-first | No | No | YES — TERMINAL ARTIFACT INVENTORY + STOP | No |
| V-03 | Severity-stratified FAIL blocks | No | YES — Tier 1/2/3 on all gates | No | No |
| V-04 | C-24 + C-25 combination | YES | YES | No | No |
| V-05 | Full integration | YES | YES | YES | YES — STOP barriers at Phase 1/2 exit |

**Predicted discriminators for scoring**:

- C-24 will fail in V-02 and V-03 (no primacy declaration)
- C-25 will fail in V-01 and V-02 (flat FAIL blocks only)
- V-04 and V-05 are predicted to score highest on the new criteria
- V-05's scanner isolation may surface a new excellence pattern — the TERMINAL ARTIFACT INVENTORY as a named, parseable output separate from an internal state scratch block. If it scores well on artifact-grounded classification (C-03), this may become a candidate for a new criterion in v9.
