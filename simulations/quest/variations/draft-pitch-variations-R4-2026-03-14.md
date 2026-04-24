Saved to `simulations/quest/variations/draft-pitch-variations-R4-2026-03-14.md`.

---

## draft-pitch — Variations R4 Summary

**Context**: R3 saturated the v3 rubric ceiling (all 5 at Platinum/100). v4 added C-16/C-17/C-18 from R3's excellence signals. No R3 variation hits all 11 aspirational criteria simultaneously.

---

**Variation map:**

| ID | Axis | Targets | Base |
|----|------|---------|------|
| V-01 | Output format | C-17 alone | V-04 R3 + explicit Failure Mode column instruction with negative example |
| V-02 | Inertia framing | C-18 alone | V-04 R3 + per-audience DEFAULTS rows + "Instead of" CTA template |
| V-03 | Lifecycle emphasis | C-16 alone | V-03 R3 + *Produces*/*Consumes* declarations on all 3 named outputs |
| V-04 | Output format + Lifecycle | C-16 + C-17 | V-04 R3 + Failure Mode column; C-18 intentionally excluded |
| V-05 | All three axes | C-16 + C-17 + C-18 | V-04 R3 + all three changes; predicted 100/Platinum |

**Key structural innovations per variation:**

- **V-01**: Failure Mode column definition includes an explicit negative example: *"Exec won't believe the ROI argument" is a belief restatement, not a Failure Mode.* This is the minimal change to lift C-17 from borderline to PASS.

- **V-02**: SIGNAL DEFAULTS splits `Inertia cost` into `Exec inertia`, `Dev inertia`, `Maker inertia`. Phase 4 gate anchors rewrite in `active Exec inertia` (not generic `Inertia cost`). Each CTA uses `"Instead of [active X inertia from SIGNAL DEFAULTS], [action]"`.

- **V-03**: Purely additive to V-03 R3 — adds `*Produces*: AUDIENCE BELIEF MAP` in Step 2, `*Produces*: POSITIONING LOCK` in Step 3, and `*Consumes*: AUDIENCE BELIEF MAP / POSITIONING LOCK / EXEC OPENING SENTENCE` in Step 5. Inertia structure unchanged.

- **V-04**: 3-column BELIEF MAP (Core Belief | Failure Mode | Inertia Excuse) with same Failure Mode instruction as V-01, inside V-04 R3's phase structure. Clean C-16+C-17 test without C-18 noise.

- **V-05**: Full synthesis — 4-column BELIEF MAP (adds Inertia Counter), per-audience DEFAULTS, "Instead of" CTA template, Consumes/Produces chain. All three new criteria fire simultaneously.
L) and borderline Failure Mode (C-17) | V-03 R4: 3-node chain added to C-18-strong base; V-04/V-05 R4: 3-node chain + C-17 or all three |

---

## V-01 -- Single Axis: Output Format (Explicit Failure Mode Column)

**Axis**: Output format -- BELIEF MAP becomes a 4-column table (Core Belief | Failure Mode | Inertia Excuse | Inertia Counter). The Failure Mode column has an explicit instruction that distinguishes outcome failure from belief restatement, with a negative example built into the column definition.

**Hypothesis**: V-02 R3 had a "Failure Mode" column but the column header alone does not prevent a model from restating the belief in negative form. Adding an explicit instruction -- "Name an outcome failure for the pitch, e.g., 'Exec won't authorize the demo slot.' A restatement of the belief in negative form, e.g., 'Exec won't believe the ROI argument,' does not pass." -- makes C-17 structurally verifiable by inspection. No change to role sequence, lifecycle, or inertia framing; this is the minimal change needed to lift C-17 from borderline to PASS.

---

### Prompt Body

You are executing the `draft-pitch` skill for: `{topic}`.

---

**SIGNAL DEFAULTS**

These apply unconditionally to all runs. Override with scout signal values when found.

| Field | Default Value |
|-------|---------------|
| Primary competitor | "teams doing nothing -- the review that never happened" |
| Inertia cost | "features built on assumptions that a 30-minute investigation would have invalidated" |
| Exec outcome | "know what you know before you commit" |
| Dev friction | "late-stage requirement changes traced back to questions nobody asked before starting" |
| Maker outcome | "stop finding out you built the wrong thing after you built it" |
| Ruling out #1 | "Signal is not a test runner. It does not execute code or run CI." |
| Ruling out #2 | "Signal is not a documentation generator. It does not produce specs from existing code." |
| Ruling out #3 | "Signal is not a project manager. It does not assign work, track sprints, or file tickets." |
| Proof fallback | "technique experiments across 730+ scenarios (simulations/techniques/)" |

---

**=== PHASE 1: SIGNAL INTAKE ===**

Check for prior signals:
- `simulations/scout/positioning/{topic}-positioning-*.md`
- `simulations/scout/competitors/{topic}-competitors-*.md`
- `simulations/scout/requirements/{topic}-requirements-*.md`

Write: "Signals found: [list files]" or "No prior signals -- SIGNAL DEFAULTS apply."

For each signal found: note which SIGNAL DEFAULTS rows it overrides and the override value.

**Phase 1 output**: active values table -- which DEFAULTS fields are overridden and by what.

**-- PHASE 1 COMPLETE. Do not proceed until active values are written. --**

---

**=== PHASE 2: BELIEF MAP ===**

*Consumes*: Phase 1 active values.
*Produces*: **BELIEF MAP** (named output). Phase 5 references this output by exact name.

For each audience, fill all four columns. Column definitions:

- **Core Belief**: The one thing this audience must believe before any other argument can land.
- **Failure Mode**: What the pitch *fails to achieve for this audience* if Core Belief is absent. This is an outcome failure for the pitch -- name what the pitch cannot accomplish (e.g., "Exec won't authorize the demo slot"). A restatement of Core Belief in negative form does not pass (e.g., "Exec won't believe the ROI argument" is a belief restatement, not a Failure Mode).
- **Inertia Excuse**: What this audience says or does to avoid acting today. Use Phase 1 active Primary competitor as baseline for Exec row if no scout override.
- **Inertia Counter**: The specific action that addresses this Inertia Excuse. One concrete step.

**BELIEF MAP:**

| Audience | Core Belief | Failure Mode | Inertia Excuse | Inertia Counter |
|----------|-------------|--------------|----------------|-----------------|
| Exec | [Write belief] | [Name the pitch outcome failure] | [Name the inertia excuse] | [Name the counter action] |
| Dev | [Write belief] | [Name the pitch outcome failure] | [Name the inertia excuse] | [Name the counter action] |
| Maker | [Write belief] | [Name the pitch outcome failure] | [Name the inertia excuse] | [Name the counter action] |

A cell is not complete if it restates the column header in general terms or leaves the value as a placeholder. Do not proceed until all twelve cells are filled.

**-- PHASE 2 COMPLETE. BELIEF MAP is locked. Do not proceed until all rows are filled. --**

---

**=== PHASE 3: POSITIONING LOCK ===**

*Consumes*: Phase 1 active values.
*Produces*: **POSITIONING LOCK** (named output). Phase 5 references this output by exact name.

Answer all three questions in writing before proceeding. These are locked -- Phase 5 cannot revise their content.

**POSITIONING LOCK:**

1. **Competitor**: "The real competition for teams building {topic} is not a named tool. It is ___."
   (Use Phase 1 active Primary competitor, or scout override.)

2. **Outcome**: "Signal gives {primary audience} ___ before the first line of code is written."
   (Use Phase 1 active Exec outcome, or scout override.)

3. **Ruling out**: Three categories Signal is NOT. Use Phase 1 active Ruling Out values.
   Format: "[Category]. Signal does not [function]."

**-- PHASE 3 COMPLETE. POSITIONING LOCK is locked. Do not proceed until all three answers are written. --**

---

**=== PHASE 4: EXEC OPENING GATE ===**

*Consumes*: POSITIONING LOCK Competitor answer, active Inertia cost from SIGNAL DEFAULTS.
*Produces*: **EXEC OPENING SENTENCE** (named output). Phase 5 exec Hook references this output by exact name.

**Write: EXEC OPENING SENTENCE**
> [One sentence only -- nothing else in this phase.]

**Binary gate:**
Does EXEC OPENING SENTENCE name a cost, risk, or productivity consequence teams face today -- without mentioning a feature, tool, or product?

- **YES** -- EXEC OPENING SENTENCE is locked. Proceed to Phase 5.
- **NO** -- rewrite. Anchor in active Inertia cost from SIGNAL DEFAULTS. Re-apply gate. Repeat until YES.

**-- PHASE 4 COMPLETE. EXEC OPENING SENTENCE is locked. Do not proceed until gate passes. --**

---

**=== PHASE 5: FULL DRAFT ===**

*Consumes*: BELIEF MAP (from Phase 2), POSITIONING LOCK (from Phase 3), EXEC OPENING SENTENCE (from Phase 4).

Draft each version from the Core Belief in BELIEF MAP. Use POSITIONING LOCK as the sole source for positioning claims. Each CTA uses the Inertia Counter from the corresponding BELIEF MAP row.

**Exec Version**
*Core Belief (from BELIEF MAP, exec row).*

- **Hook**: EXEC OPENING SENTENCE (from Phase 4, locked, exact).
- **What It Does**: POSITIONING LOCK Outcome answer. One sentence.
- **Why It Matters**: POSITIONING LOCK Competitor named explicitly. "The alternative is not a competing product. It is [Competitor]." 2-3 sentences ROI framing.
- **Call to Action**: BELIEF MAP exec Inertia Counter, phrased as one specific decision, demo slot, or budget ask.

**Dev Version**
*Core Belief (from BELIEF MAP, dev row).*

- **Hook**: A scenario the developer is in right now -- the moment before Signal changes what happens next.
- **What It Does**: At least one concrete interaction. Example: `/scout:requirements topic={topic}` produces `{topic}-requirements-{date}.md`. Reader answers "what would I actually type?"
- **Why It Matters**: Active Dev friction from SIGNAL DEFAULTS. Named directly.
- **Call to Action**: BELIEF MAP dev Inertia Counter, phrased as one command or file path runnable today.

**Maker Version**
*Core Belief (from BELIEF MAP, maker row).*

- **Hook**: The question they have already asked themselves. Zero unexplained acronyms. Zero namespace references. Zero CLI terminology.
- **What It Does**: Plain English. Translate every Signal term to what it does for a person.
- **Why It Matters**: Active Maker outcome from SIGNAL DEFAULTS. Connect to decision context.
- **Call to Action**: BELIEF MAP maker Inertia Counter, phrased as something proposable in a meeting without a ticket.

**-- PHASE 5 COMPLETE. --**

---

**=== PHASE 6: ANTI-POSITIONING ===**

Write "## What Signal Is NOT" from POSITIONING LOCK Ruling Out values. Add one additional adjacent category not already in SIGNAL DEFAULTS.

Format: `[Category]. Signal does not [specific function]. [One sentence on why this distinction matters for {topic} specifically.]`

Minimum four bullets.

**-- PHASE 6 COMPLETE. --**

---

**=== PHASE 7: PROOF AUDIT ===**

For every factual claim in exec and dev versions:
- `[source: {artifact-path}]` -- direct file
- `[source: prior signal]` -- scout artifact
- `[UNVERIFIED]` -- flag; replace with hedged language or active Proof fallback from SIGNAL DEFAULTS before saving.

**-- PHASE 7 COMPLETE. --**

---

**Output format**:
```
## Exec Version
## Dev Version
## Maker Version
## What Signal Is NOT
```

All phase outputs (active values, BELIEF MAP, POSITIONING LOCK, EXEC OPENING SENTENCE, proof audit) are working notes -- not in saved artifact.

**Save to**: `simulations/draft/pitches/{topic}-pitch-{date}.md`

---

## V-02 -- Single Axis: Inertia Framing (Per-Audience DEFAULTS + "Instead Of" CTA Template)

**Axis**: Inertia framing -- SIGNAL DEFAULTS replaces the shared "Inertia cost" field with three distinct per-audience rows (Exec inertia, Dev inertia, Maker inertia). The CTA instruction for each version explicitly references the audience's DEFAULTS row and requires the structural template: "Instead of [inertia argument], [one concrete action]." No change to belief table format or phase structure from V-04 R3.

**Hypothesis**: V-03 R3 achieved C-18 (per-audience DEFAULTS + "Instead of" CTA) but failed C-16 (only one named gate output) and C-17 (no failure mode). V-04 R3 achieved C-16 (3-node chain) and borderline C-17 but failed C-18. This variation applies the C-18 changes from V-03 R3 to the V-04 R3 structural backbone, leaving belief table format and phase layout unchanged. Predicted: C-16 PASS (3-node chain preserved) + C-18 PASS (per-audience DEFAULTS + template) + C-17 borderline (BELIEF MAP retains "Argument fails if" column).

---

### Prompt Body

You are executing the `draft-pitch` skill for: `{topic}`.

---

**SIGNAL DEFAULTS**

These apply unconditionally to all runs. Override with scout signal values when found.

| Field | Default Value |
|-------|---------------|
| Primary competitor | "teams doing nothing -- the review that never happened" |
| Exec inertia | "the spec review that happened post-build, the go/no-go that nobody called before the sprint started" |
| Dev inertia | "running the sprint on assumptions, finding out at demo that the requirement was wrong" |
| Maker inertia | "waiting to see how it lands before asking if we should have built it differently" |
| Exec outcome | "know what you know before you commit" |
| Dev friction | "late-stage requirement changes traced back to questions nobody asked before starting" |
| Maker outcome | "stop finding out you built the wrong thing after you built it" |
| Ruling out #1 | "Signal is not a test runner. It does not execute code or run CI." |
| Ruling out #2 | "Signal is not a documentation generator. It does not produce specs from existing code." |
| Ruling out #3 | "Signal is not a project manager. It does not assign work, track sprints, or file tickets." |
| Proof fallback | "technique experiments across 730+ scenarios (simulations/techniques/)" |

---

**=== PHASE 1: SIGNAL INTAKE ===**

Check for prior signals:
- `simulations/scout/positioning/{topic}-positioning-*.md`
- `simulations/scout/competitors/{topic}-competitors-*.md`
- `simulations/scout/requirements/{topic}-requirements-*.md`

Write: "Signals found: [list files]" or "No prior signals -- SIGNAL DEFAULTS apply."

For each signal found: note which SIGNAL DEFAULTS rows it overrides and the override value.

**Phase 1 output**: active values table -- which DEFAULTS fields are overridden and by what.

**-- PHASE 1 COMPLETE. Do not proceed until active values are written. --**

---

**=== PHASE 2: BELIEF MAP ===**

*Consumes*: Phase 1 active values.
*Produces*: **BELIEF MAP** (named output). Phase 5 references this output by exact name.

Identify what each audience must believe first -- the single belief whose absence makes all other arguments fail.

**BELIEF MAP:**

| Audience | Must believe before anything else | Argument fails if |
|----------|----------------------------------|-------------------|
| Exec | [Write belief] | [Write failure mode] |
| Dev | [Write belief] | [Write failure mode] |
| Maker | [Write belief] | [Write failure mode] |

A row is not complete if it restates the column header. Use Phase 1 active values to anchor exec and dev rows.

**-- PHASE 2 COMPLETE. BELIEF MAP is locked. Do not proceed until all three rows are filled. --**

---

**=== PHASE 3: POSITIONING LOCK ===**

*Consumes*: Phase 1 active values.
*Produces*: **POSITIONING LOCK** (named output). Phase 5 references this output by exact name.

Answer all three questions in writing before proceeding. These are locked.

**POSITIONING LOCK:**

1. **Competitor**: "The real competition for teams building {topic} is not a named tool. It is ___."
   (Use Phase 1 active Primary competitor, or scout override.)

2. **Outcome**: "Signal gives {primary audience} ___ before the first line of code is written."
   (Use Phase 1 active Exec outcome, or scout override.)

3. **Ruling out**: Three categories Signal is NOT. Use Phase 1 active Ruling Out values.
   Format: "[Category]. Signal does not [function]."

**-- PHASE 3 COMPLETE. POSITIONING LOCK is locked. Do not proceed until all three answers are written. --**

---

**=== PHASE 4: EXEC OPENING GATE ===**

*Consumes*: POSITIONING LOCK Competitor answer, active Exec inertia from SIGNAL DEFAULTS.
*Produces*: **EXEC OPENING SENTENCE** (named output). Phase 5 exec Hook references this output by exact name.

**Write: EXEC OPENING SENTENCE**
> [One sentence only -- nothing else in this phase.]

**Binary gate:**
Does EXEC OPENING SENTENCE name a cost, risk, or productivity consequence teams face today -- without mentioning a feature, tool, or product?

- **YES** -- EXEC OPENING SENTENCE is locked. Proceed to Phase 5.
- **NO** -- rewrite. Anchor in active Exec inertia from SIGNAL DEFAULTS. Re-apply gate. Repeat until YES.

**-- PHASE 4 COMPLETE. EXEC OPENING SENTENCE is locked. Do not proceed until gate passes. --**

---

**=== PHASE 5: FULL DRAFT ===**

*Consumes*: BELIEF MAP (from Phase 2), POSITIONING LOCK (from Phase 3), EXEC OPENING SENTENCE (from Phase 4).

Draft each version starting from the audience belief in BELIEF MAP. Use POSITIONING LOCK as the sole source for positioning claims. Each CTA must address the audience's inertia argument using the structural template: "Instead of [audience inertia from SIGNAL DEFAULTS], [one concrete action]."

**Exec Version**
*Belief anchor (from BELIEF MAP, exec row).*

- **Hook**: EXEC OPENING SENTENCE (from Phase 4, locked, exact).
- **What It Does**: POSITIONING LOCK Outcome answer. One sentence.
- **Why It Matters**: POSITIONING LOCK Competitor named explicitly. "The alternative is not a competing product. It is [Competitor]." 2-3 sentences ROI framing.
- **Call to Action**: "Instead of [active Exec inertia from SIGNAL DEFAULTS], [one specific decision, demo slot, or budget ask]."

**Dev Version**
*Belief anchor (from BELIEF MAP, dev row).*

- **Hook**: A scenario the developer is in right now -- the moment before Signal changes what happens next.
- **What It Does**: At least one concrete interaction. Example: `/scout:requirements topic={topic}` produces `{topic}-requirements-{date}.md`. Reader answers "what would I actually type?"
- **Why It Matters**: Active Dev friction from SIGNAL DEFAULTS. Named directly.
- **Call to Action**: "Instead of [active Dev inertia from SIGNAL DEFAULTS], [one runnable command or file path today]."

**Maker Version**
*Belief anchor (from BELIEF MAP, maker row).*

- **Hook**: The question they have already asked themselves. Zero unexplained acronyms. Zero namespace references. Zero CLI terminology.
- **What It Does**: Plain English. Translate every Signal term to what it does for a person.
- **Why It Matters**: Active Maker outcome from SIGNAL DEFAULTS. Connect to decision context.
- **Call to Action**: "Instead of [active Maker inertia from SIGNAL DEFAULTS], [something proposable in a meeting without a ticket]."

**-- PHASE 5 COMPLETE. --**

---

**=== PHASE 6: ANTI-POSITIONING ===**

Write "## What Signal Is NOT" from POSITIONING LOCK Ruling Out values. Add one additional adjacent category not already in SIGNAL DEFAULTS.

Format: `[Category]. Signal does not [specific function]. [One sentence on why this distinction matters for {topic} specifically.]`

Minimum four bullets.

**-- PHASE 6 COMPLETE. --**

---

**=== PHASE 7: PROOF AUDIT ===**

For every factual claim in exec and dev versions:
- `[source: {artifact-path}]` -- direct file
- `[source: prior signal]` -- scout artifact
- `[UNVERIFIED]` -- flag; replace with hedged language or active Proof fallback from SIGNAL DEFAULTS before saving.

**-- PHASE 7 COMPLETE. --**

---

**Output format**:
```
## Exec Version
## Dev Version
## Maker Version
## What Signal Is NOT
```

All phase outputs (active values, BELIEF MAP, POSITIONING LOCK, EXEC OPENING SENTENCE, proof audit) are working notes -- not in saved artifact.

**Save to**: `simulations/draft/pitches/{topic}-pitch-{date}.md`

---

## V-03 -- Single Axis: Lifecycle Emphasis (3-Node Chain on C-18 Base)

**Axis**: Lifecycle emphasis -- named *Produces* declarations are added to the AUDIENCE BELIEF MAP step and POSITIONING LOCK step. The drafting step gains an explicit *Consumes* line referencing all three named outputs by exact name. Applied to V-03 R3 as base (per-audience DEFAULTS + "Instead of" CTA template). Belief mapping and CTA structure are preserved exactly; only lifecycle declarations are added.

**Hypothesis**: V-03 R3 had the strongest C-18 form but failed C-16 because only EXEC OPENING SENTENCE was a named output. Adding *Produces*: AUDIENCE BELIEF MAP in Step 2 and *Produces*: POSITIONING LOCK in Step 3, then requiring Step 5 to *Consume* all three by exact name, lifts C-16 from FAIL to PASS without altering the inertia structure. This demonstrates C-16 and C-18 are orthogonal -- achieving one does not require changing the other.

---

### Prompt Body

You are executing the `draft-pitch` skill for: `{topic}`.

---

**SIGNAL DEFAULTS**

These apply unconditionally to all runs. Override with scout signal values when found.

| Field | Default Value |
|-------|---------------|
| Primary competitor | "teams doing nothing -- the review that never happened" |
| Exec inertia | "the spec review that happened post-build, the go/no-go that nobody called before the sprint started" |
| Dev inertia | "running the sprint on assumptions, finding out at demo that the requirement was wrong" |
| Maker inertia | "waiting to see how it lands before asking if we should have built it differently" |
| Exec outcome | "know what you know before you commit" |
| Dev friction | "late-stage requirement changes traced back to questions nobody asked before starting" |
| Maker outcome | "stop finding out you built the wrong thing after you built it" |
| Ruling out #1 | "Signal is not a test runner. It does not execute code or run CI." |
| Ruling out #2 | "Signal is not a documentation generator. It does not produce specs from existing code." |
| Ruling out #3 | "Signal is not a project manager. It does not assign work, track sprints, or file tickets." |
| Proof fallback | "technique experiments across 730+ scenarios (simulations/techniques/)" |

---

**Step 1: Signal Intake**

Check for prior signals:
- `simulations/scout/positioning/{topic}-positioning-*.md`
- `simulations/scout/competitors/{topic}-competitors-*.md`
- `simulations/scout/requirements/{topic}-requirements-*.md`

Write: "Signals found: [list files]" or "No prior signals -- SIGNAL DEFAULTS apply."

For each signal found: note which SIGNAL DEFAULTS fields it overrides.

---

**Step 2: Audience Belief and Inertia Mapping**

*Produces*: **AUDIENCE BELIEF MAP** (named output). Step 5 references this output by exact name.

Before writing any pitch content, answer for each audience: what must they believe first, and what is the inertia argument they use to avoid believing it?

Write each answer before drafting begins. Do not draft pitch content until all six lines are written.

**AUDIENCE BELIEF MAP:**

**Exec must believe**: [Write the single belief that precedes any ROI argument.]
**Exec inertia argument**: [Write the specific thing the exec says or does instead. Use active Exec inertia from SIGNAL DEFAULTS if no scout override.]

**Dev must believe**: [Write the single belief that precedes any workflow argument.]
**Dev inertia argument**: [Write the specific thing the dev says or does instead. Use active Dev inertia from SIGNAL DEFAULTS if no scout override.]

**Maker must believe**: [Write the single belief that precedes any "can I do this?" argument.]
**Maker inertia argument**: [Write the specific thing the maker says or does instead. Use active Maker inertia from SIGNAL DEFAULTS if no scout override.]

**AUDIENCE BELIEF MAP is locked. Do not proceed until all six lines are written.**

---

**Step 3: Positioning Lock**

*Produces*: **POSITIONING LOCK** (named output). Step 4 and Step 5 reference this output by exact name.

Answer in writing before drafting begins. These are locked.

**POSITIONING LOCK:**

1. **Competitor**: "The real competition for teams building {topic} is not a named tool. It is ___."
   (Use active Primary competitor from SIGNAL DEFAULTS, or scout override.)

2. **Outcome**: "Signal gives {primary audience} ___ before the first line of code is written."
   (Use active Exec outcome, or scout override.)

3. **Ruling out**: Three categories Signal is NOT, from active Ruling Out values in SIGNAL DEFAULTS.
   Format: "[Category]. Signal does not [function]."

**POSITIONING LOCK is locked. Do not proceed until all three answers are written.**

---

**Step 4: EXEC OPENING GATE**

*Consumes*: POSITIONING LOCK Competitor answer, active Exec inertia from SIGNAL DEFAULTS.
*Produces*: **EXEC OPENING SENTENCE** (named output). Step 5 exec Hook cites it by exact name.

**Write: EXEC OPENING SENTENCE**
> [One sentence only.]

**Binary gate:**
Does EXEC OPENING SENTENCE name a cost, risk, or productivity consequence teams face today -- without mentioning a feature, tool, or product?

- **YES** -- EXEC OPENING SENTENCE is locked. Proceed to Step 5.
- **NO** -- rewrite. Use active Exec inertia from SIGNAL DEFAULTS as your anchor. Re-apply gate. Repeat until YES.

**EXEC OPENING SENTENCE is locked.**

---

**Step 5: Full Draft**

*Consumes*: AUDIENCE BELIEF MAP (from Step 2), POSITIONING LOCK (from Step 3), EXEC OPENING SENTENCE (from Step 4).

Each version's CTA must name the audience's inertia argument from AUDIENCE BELIEF MAP and counter it using the structural template: "Instead of [inertia argument], [one concrete action]."

**Exec Version**
*Belief anchor (from AUDIENCE BELIEF MAP, exec belief line).*

- **Hook**: EXEC OPENING SENTENCE (from Step 4, locked, exact).
- **What It Does**: POSITIONING LOCK Outcome answer. One sentence.
- **Why It Matters**: POSITIONING LOCK Competitor named explicitly. "The alternative is [Competitor]. Signal eliminates that cost before the build starts." 2-3 sentences ROI framing.
- **Call to Action**: "Instead of [exec inertia argument from AUDIENCE BELIEF MAP], [one specific decision, demo slot, or budget ask]."

**Dev Version**
*Belief anchor (from AUDIENCE BELIEF MAP, dev belief line).*

- **Hook**: A concrete scenario the developer is in right now -- the moment before Signal changes what happens next.
- **What It Does**: At least one concrete interaction. Example: `/scout:requirements topic={topic}` produces `{topic}-requirements-{date}.md`. Reader answers "what would I actually type?"
- **Why It Matters**: Active Dev friction from SIGNAL DEFAULTS. Named directly.
- **Call to Action**: "Instead of [dev inertia argument from AUDIENCE BELIEF MAP], [one runnable command or file path today]."

**Maker Version**
*Belief anchor (from AUDIENCE BELIEF MAP, maker belief line).*

- **Hook**: The question they have already asked themselves. Zero unexplained acronyms. Zero namespace references. Zero CLI terminology.
- **What It Does**: Plain English. Translate every Signal term to what it does for a person.
- **Why It Matters**: Active Maker outcome from SIGNAL DEFAULTS. Connect to their decision context.
- **Call to Action**: "Instead of [maker inertia argument from AUDIENCE BELIEF MAP], [something proposable in a meeting without a ticket]."

---

**Step 6: Anti-Positioning**

Write "## What Signal Is NOT" from POSITIONING LOCK Ruling Out values.

Format: `[Category]. Signal does not [specific function].`

Minimum three bullets.

---

**Step 7: Proof Points**

For every factual claim in exec and dev versions:
- `[source: {artifact-path}]` -- direct file
- `[source: prior signal]` -- scout artifact
- `[UNVERIFIED]` -- flag; replace with hedged language or active Proof fallback from SIGNAL DEFAULTS before saving.

---

**Output format**:
```
## Exec Version
## Dev Version
## Maker Version
## What Signal Is NOT
```

SIGNAL DEFAULTS, AUDIENCE BELIEF MAP, POSITIONING LOCK, EXEC OPENING SENTENCE, and proof points are working notes -- not in saved artifact.

**Save to**: `simulations/draft/pitches/{topic}-pitch-{date}.md`

---

## V-04 -- Combined: Output Format + Lifecycle Emphasis

**Axes**: Output format (explicit Failure Mode column in BELIEF MAP) + lifecycle emphasis (Consumes/Produces phase metadata, 3-node chain). No change to inertia framing -- SIGNAL DEFAULTS retains a single Inertia cost field; CTAs do not use "Instead of" template.

**Hypothesis**: Combining C-17 (explicit Failure Mode column with outcome-failure instruction) and C-16 (Consumes/Produces 3-node chain) tests whether the two structural changes are compatible and whether phase formality improves column completion. C-18 is intentionally not targeted; if this variation reaches Platinum, C-18 is confirmed independent of the other two new criteria.

---

### Prompt Body

You are executing the `draft-pitch` skill for: `{topic}`.

---

**SIGNAL DEFAULTS**

These apply unconditionally to all runs. Override with scout signal values when found.

| Field | Default Value |
|-------|---------------|
| Primary competitor | "teams doing nothing -- the review that never happened" |
| Inertia cost | "features built on assumptions that a 30-minute investigation would have invalidated" |
| Exec outcome | "know what you know before you commit" |
| Dev friction | "late-stage requirement changes traced back to questions nobody asked before starting" |
| Maker outcome | "stop finding out you built the wrong thing after you built it" |
| Ruling out #1 | "Signal is not a test runner. It does not execute code or run CI." |
| Ruling out #2 | "Signal is not a documentation generator. It does not produce specs from existing code." |
| Ruling out #3 | "Signal is not a project manager. It does not assign work, track sprints, or file tickets." |
| Proof fallback | "technique experiments across 730+ scenarios (simulations/techniques/)" |

---

**=== PHASE 1: SIGNAL INTAKE ===**

Check for prior signals:
- `simulations/scout/positioning/{topic}-positioning-*.md`
- `simulations/scout/competitors/{topic}-competitors-*.md`
- `simulations/scout/requirements/{topic}-requirements-*.md`

Write: "Signals found: [list files]" or "No prior signals -- SIGNAL DEFAULTS apply."

For each signal found: note which SIGNAL DEFAULTS rows it overrides and the override value.

**Phase 1 output**: active values table -- which DEFAULTS fields are overridden and by what.

**-- PHASE 1 COMPLETE. Do not proceed until active values are written. --**

---

**=== PHASE 2: BELIEF MAP ===**

*Consumes*: Phase 1 active values.
*Produces*: **BELIEF MAP** (named output). Phase 5 references this output by exact name.

For each audience, fill all three columns. Column definitions:

- **Core Belief**: The one thing this audience must believe before any other argument can land.
- **Failure Mode**: What the pitch *fails to achieve for this audience* if Core Belief is absent. Name a pitch outcome failure -- what the pitch cannot accomplish (e.g., "Exec won't authorize the demo slot," "Dev won't try the command," "Maker won't raise the question in their next meeting"). A restatement of Core Belief in negative form does not pass (e.g., "Exec won't believe the ROI argument" restates the belief -- it is not a Failure Mode).
- **Inertia Excuse**: What this audience says or does to justify not acting today. Use Phase 1 active Primary competitor as baseline for Exec row if no scout override.

**BELIEF MAP:**

| Audience | Core Belief | Failure Mode | Inertia Excuse |
|----------|-------------|--------------|----------------|
| Exec | [Write belief] | [Name the pitch outcome failure] | [Name the inertia excuse] |
| Dev | [Write belief] | [Name the pitch outcome failure] | [Name the inertia excuse] |
| Maker | [Write belief] | [Name the pitch outcome failure] | [Name the inertia excuse] |

A cell is not complete if it restates the column header or contains a belief restatement in the Failure Mode column. Do not proceed until all nine cells are filled.

**-- PHASE 2 COMPLETE. BELIEF MAP is locked. Do not proceed until all rows are filled. --**

---

**=== PHASE 3: POSITIONING LOCK ===**

*Consumes*: Phase 1 active values.
*Produces*: **POSITIONING LOCK** (named output). Phase 5 references this output by exact name.

Answer all three questions in writing before proceeding. These are locked.

**POSITIONING LOCK:**

1. **Competitor**: "The real competition for teams building {topic} is not a named tool. It is ___."
   (Use Phase 1 active Primary competitor, or scout override.)

2. **Outcome**: "Signal gives {primary audience} ___ before the first line of code is written."
   (Use Phase 1 active Exec outcome, or scout override.)

3. **Ruling out**: Three categories Signal is NOT. Use Phase 1 active Ruling Out values.
   Format: "[Category]. Signal does not [function]."

**-- PHASE 3 COMPLETE. POSITIONING LOCK is locked. Do not proceed until all three answers are written. --**

---

**=== PHASE 4: EXEC OPENING GATE ===**

*Consumes*: POSITIONING LOCK Competitor answer, active Inertia cost from SIGNAL DEFAULTS.
*Produces*: **EXEC OPENING SENTENCE** (named output). Phase 5 exec Hook references this output by exact name.

**Write: EXEC OPENING SENTENCE**
> [One sentence only -- nothing else in this phase.]

**Binary gate:**
Does EXEC OPENING SENTENCE name a cost, risk, or productivity consequence teams face today -- without mentioning a feature, tool, or product?

- **YES** -- EXEC OPENING SENTENCE is locked. Proceed to Phase 5.
- **NO** -- rewrite. Anchor in active Inertia cost from SIGNAL DEFAULTS. Re-apply gate. Repeat until YES.

**-- PHASE 4 COMPLETE. EXEC OPENING SENTENCE is locked. Do not proceed until gate passes. --**

---

**=== PHASE 5: FULL DRAFT ===**

*Consumes*: BELIEF MAP (from Phase 2), POSITIONING LOCK (from Phase 3), EXEC OPENING SENTENCE (from Phase 4).

Draft each version from the Core Belief in BELIEF MAP. Use POSITIONING LOCK as the sole source for positioning claims. Do not introduce claims not present in POSITIONING LOCK.

**Exec Version**
*Core Belief (from BELIEF MAP, exec row).*

- **Hook**: EXEC OPENING SENTENCE (from Phase 4, locked, exact).
- **What It Does**: POSITIONING LOCK Outcome answer. One sentence.
- **Why It Matters**: POSITIONING LOCK Competitor named explicitly. "The alternative is not a competing product. It is [Competitor]." 2-3 sentences ROI framing.
- **Call to Action**: One specific decision, demo slot, or budget ask. Not "learn more."

**Dev Version**
*Core Belief (from BELIEF MAP, dev row).*

- **Hook**: A scenario the developer is in right now -- the moment before Signal changes what happens next.
- **What It Does**: At least one concrete interaction. Example: `/scout:requirements topic={topic}` produces `{topic}-requirements-{date}.md`. Reader answers "what would I actually type?"
- **Why It Matters**: Active Dev friction from SIGNAL DEFAULTS. Named directly.
- **Call to Action**: One command or file path runnable today without PM involvement.

**Maker Version**
*Core Belief (from BELIEF MAP, maker row).*

- **Hook**: The question they have already asked themselves. Zero unexplained acronyms. Zero namespace references. Zero CLI terminology.
- **What It Does**: Plain English. Translate every Signal term to what it does for a person.
- **Why It Matters**: Active Maker outcome from SIGNAL DEFAULTS. Connect to decision context.
- **Call to Action**: Something proposable in a meeting without a ticket.

**-- PHASE 5 COMPLETE. --**

---

**=== PHASE 6: ANTI-POSITIONING ===**

Write "## What Signal Is NOT" from POSITIONING LOCK Ruling Out values. Add one additional adjacent category not already in SIGNAL DEFAULTS.

Format: `[Category]. Signal does not [specific function]. [One sentence on why this distinction matters for {topic} specifically.]`

Minimum four bullets.

**-- PHASE 6 COMPLETE. --**

---

**=== PHASE 7: PROOF AUDIT ===**

For every factual claim in exec and dev versions:
- `[source: {artifact-path}]` -- direct file
- `[source: prior signal]` -- scout artifact
- `[UNVERIFIED]` -- flag; replace with hedged language or active Proof fallback from SIGNAL DEFAULTS before saving.

**-- PHASE 7 COMPLETE. --**

---

**Output format**:
```
## Exec Version
## Dev Version
## Maker Version
## What Signal Is NOT
```

All phase outputs (active values, BELIEF MAP, POSITIONING LOCK, EXEC OPENING SENTENCE, proof audit) are working notes -- not in saved artifact.

**Save to**: `simulations/draft/pitches/{topic}-pitch-{date}.md`

---

## V-05 -- Combined: All Three Axes (C-16 + C-17 + C-18 Synthesis)

**Axes**: Output format (4-column BELIEF MAP with explicit Failure Mode) + inertia framing (per-audience DEFAULTS + "Instead of" CTA template) + lifecycle emphasis (Consumes/Produces 3-node chain).

**Hypothesis**: V-05 is the first variation designed to simultaneously satisfy all 11 aspirational criteria. Three structural changes applied to V-04 R3's phase backbone: (a) SIGNAL DEFAULTS gains three per-audience inertia rows replacing the single Inertia cost field, (b) BELIEF MAP becomes a 4-column table with an explicit Failure Mode column instruction that prohibits belief restatement by providing a negative example, (c) each CTA uses the structural template "Instead of [audience inertia from SIGNAL DEFAULTS], [action]" keyed to the per-audience DEFAULTS row. Consumes/Produces metadata from V-04 R3 is preserved. Predicted composite: 100 (Platinum) under v4 rubric.

---

### Prompt Body

You are executing the `draft-pitch` skill for: `{topic}`.

---

**SIGNAL DEFAULTS**

These apply unconditionally to all runs. Override with scout signal values when found.

| Field | Default Value |
|-------|---------------|
| Primary competitor | "teams doing nothing -- the review that never happened" |
| Exec inertia | "the spec review that happened post-build, the go/no-go that nobody called before the sprint started" |
| Dev inertia | "running the sprint on assumptions, finding out at demo that the requirement was wrong" |
| Maker inertia | "waiting to see how it lands before asking if we should have built it differently" |
| Exec outcome | "know what you know before you commit" |
| Dev friction | "late-stage requirement changes traced back to questions nobody asked before starting" |
| Maker outcome | "stop finding out you built the wrong thing after you built it" |
| Ruling out #1 | "Signal is not a test runner. It does not execute code or run CI." |
| Ruling out #2 | "Signal is not a documentation generator. It does not produce specs from existing code." |
| Ruling out #3 | "Signal is not a project manager. It does not assign work, track sprints, or file tickets." |
| Proof fallback | "technique experiments across 730+ scenarios (simulations/techniques/)" |

---

**=== PHASE 1: SIGNAL INTAKE ===**

Check for prior signals:
- `simulations/scout/positioning/{topic}-positioning-*.md`
- `simulations/scout/competitors/{topic}-competitors-*.md`
- `simulations/scout/requirements/{topic}-requirements-*.md`

Write: "Signals found: [list files]" or "No prior signals -- SIGNAL DEFAULTS apply."

For each signal found: note which SIGNAL DEFAULTS rows it overrides and the override value.

**Phase 1 output**: active values table -- which DEFAULTS fields are overridden and by what.

**-- PHASE 1 COMPLETE. Do not proceed until active values are written. --**

---

**=== PHASE 2: BELIEF MAP ===**

*Consumes*: Phase 1 active values.
*Produces*: **BELIEF MAP** (named output). Phase 5 references this output by exact name.

For each audience, fill all four columns. Column definitions:

- **Core Belief**: The one thing this audience must believe before any other argument can land.
- **Failure Mode**: What the pitch *fails to achieve for this audience* if Core Belief is absent. Name a pitch outcome failure -- what the pitch cannot accomplish for this audience (e.g., "Exec won't authorize the demo slot," "Dev won't try the command," "Maker won't raise the question in their next meeting"). A restatement of Core Belief in negative form does not pass (e.g., "Exec won't believe the ROI argument" -- this restates the belief and is not a Failure Mode).
- **Inertia Excuse**: What this audience says or does to justify not acting today. Use Phase 1 active inertia row for this audience from SIGNAL DEFAULTS if no scout override.
- **Inertia Counter**: The specific action that addresses this Inertia Excuse. One concrete step.

**BELIEF MAP:**

| Audience | Core Belief | Failure Mode | Inertia Excuse | Inertia Counter |
|----------|-------------|--------------|----------------|-----------------|
| Exec | [Write belief] | [Name the pitch outcome failure] | [Use active Exec inertia or scout override] | [Name the counter action] |
| Dev | [Write belief] | [Name the pitch outcome failure] | [Use active Dev inertia or scout override] | [Name the counter action] |
| Maker | [Write belief] | [Name the pitch outcome failure] | [Use active Maker inertia or scout override] | [Name the counter action] |

A cell is not complete if it restates the column header in general terms or contains a belief restatement in the Failure Mode column. Do not proceed until all twelve cells are filled.

**-- PHASE 2 COMPLETE. BELIEF MAP is locked. Do not proceed until all rows are filled. --**

---

**=== PHASE 3: POSITIONING LOCK ===**

*Consumes*: Phase 1 active values.
*Produces*: **POSITIONING LOCK** (named output). Phase 5 references this output by exact name.

Answer all three questions in writing before proceeding. These are locked -- Phase 5 cannot revise their content.

**POSITIONING LOCK:**

1. **Competitor**: "The real competition for teams building {topic} is not a named tool. It is ___."
   (Use Phase 1 active Primary competitor, or scout override.)

2. **Outcome**: "Signal gives {primary audience} ___ before the first line of code is written."
   (Use Phase 1 active Exec outcome, or scout override.)

3. **Ruling out**: Three categories Signal is NOT. Use Phase 1 active Ruling Out values.
   Format: "[Category]. Signal does not [function]."

**-- PHASE 3 COMPLETE. POSITIONING LOCK is locked. Do not proceed until all three answers are written. --**

---

**=== PHASE 4: EXEC OPENING GATE ===**

*Consumes*: POSITIONING LOCK Competitor answer, active Exec inertia from SIGNAL DEFAULTS.
*Produces*: **EXEC OPENING SENTENCE** (named output). Phase 5 exec Hook references this output by exact name.

**Write: EXEC OPENING SENTENCE**
> [One sentence only -- nothing else in this phase.]

**Binary gate:**
Does EXEC OPENING SENTENCE name a cost, risk, or productivity consequence teams face today -- without mentioning a feature, tool, or product?

- **YES** -- EXEC OPENING SENTENCE is locked. Proceed to Phase 5.
- **NO** -- rewrite. Anchor in active Exec inertia from SIGNAL DEFAULTS. Re-apply gate. Repeat until YES.

**-- PHASE 4 COMPLETE. EXEC OPENING SENTENCE is locked. Do not proceed until gate passes. --**

---

**=== PHASE 5: FULL DRAFT ===**

*Consumes*: BELIEF MAP (from Phase 2), POSITIONING LOCK (from Phase 3), EXEC OPENING SENTENCE (from Phase 4).

Draft each version from the Core Belief in BELIEF MAP. Use POSITIONING LOCK as the sole source for positioning claims. Each CTA must address the audience's Inertia Excuse using the structural template: "Instead of [active audience inertia from SIGNAL DEFAULTS], [one concrete action]."

**Exec Version**
*Core Belief (from BELIEF MAP, exec row).*

- **Hook**: EXEC OPENING SENTENCE (from Phase 4, locked, exact).
- **What It Does**: POSITIONING LOCK Outcome answer. One sentence.
- **Why It Matters**: POSITIONING LOCK Competitor named explicitly. "The alternative is not a competing product. It is [Competitor]." 2-3 sentences ROI framing.
- **Call to Action**: "Instead of [active Exec inertia from SIGNAL DEFAULTS], [one specific decision, demo slot, or budget ask]."

**Dev Version**
*Core Belief (from BELIEF MAP, dev row).*

- **Hook**: A scenario the developer is in right now -- the moment before Signal changes what happens next.
- **What It Does**: At least one concrete interaction. Example: `/scout:requirements topic={topic}` produces `{topic}-requirements-{date}.md`. Reader answers "what would I actually type?"
- **Why It Matters**: Active Dev friction from SIGNAL DEFAULTS. Named directly.
- **Call to Action**: "Instead of [active Dev inertia from SIGNAL DEFAULTS], [one runnable command or file path today]."

**Maker Version**
*Core Belief (from BELIEF MAP, maker row).*

- **Hook**: The question they have already asked themselves. Zero unexplained acronyms. Zero namespace references. Zero CLI terminology.
- **What It Does**: Plain English. Translate every Signal term to what it does for a person.
- **Why It Matters**: Active Maker outcome from SIGNAL DEFAULTS. Connect to decision context.
- **Call to Action**: "Instead of [active Maker inertia from SIGNAL DEFAULTS], [something proposable in a meeting without a ticket]."

**-- PHASE 5 COMPLETE. --**

---

**=== PHASE 6: ANTI-POSITIONING ===**

Write "## What Signal Is NOT" from POSITIONING LOCK Ruling Out values. Add one additional adjacent category not already in SIGNAL DEFAULTS.

Format: `[Category]. Signal does not [specific function]. [One sentence on why this distinction matters for {topic} specifically.]`

Minimum four bullets.

**-- PHASE 6 COMPLETE. --**

---

**=== PHASE 7: PROOF AUDIT ===**

For every factual claim in exec and dev versions:
- `[source: {artifact-path}]` -- direct file
- `[source: prior signal]` -- scout artifact
- `[UNVERIFIED]` -- flag; replace with hedged language or active Proof fallback from SIGNAL DEFAULTS before saving.

**-- PHASE 7 COMPLETE. --**

---

**Output format**:
```
## Exec Version
## Dev Version
## Maker Version
## What Signal Is NOT
```

All phase outputs (active values, BELIEF MAP, POSITIONING LOCK, EXEC OPENING SENTENCE, proof audit) are working notes -- not in saved artifact.

**Save to**: `simulations/draft/pitches/{topic}-pitch-{date}.md`

---

## R4 Design Notes

**What changed from R3:**

R3 confirmed C-13/C-14/C-15 as achievable baseline -- all five R3 variations hit 100 under v3 rubric. The R3 scorecard surfaced two excellence signals (ES-01: Consumes/Produces phase metadata; ES-02: CTA-level "Instead of" inertia counter) that became C-16/C-17/C-18 in the v4 rubric. R4's task: design variations that target these three criteria individually and in combination.

**Retroactive R3 scores under v4 rubric (denominator 11 aspirational):**

| Variation | C-16 | C-17 | C-18 | Aspirational | Composite |
|-----------|------|------|------|--------------|-----------|
| V-01 R3 | PASS (3-node chain) | BORDERLINE ("Argument fails if" col) | FAIL | ~10/11 | ~99.1 |
| V-02 R3 | FAIL (2-node) | PASS (Failure Mode col) | FAIL | ~9/11 | ~98.2 |
| V-03 R3 | FAIL (1-node) | FAIL | PASS (per-audience DEFAULTS + "Instead of") | ~9/11 | ~98.2 |
| V-04 R3 | PASS (3-node Consumes/Produces) | BORDERLINE | FAIL | ~10/11 | ~99.1 |
| V-05 R3 | FAIL | FAIL | FAIL | ~8/11 | ~97.3 |

**Predicted R4 scores under v4 rubric:**

| Variation | C-16 | C-17 | C-18 | Aspirational | Composite |
|-----------|------|------|------|--------------|-----------|
| V-01 | PASS (V-04 R3 base, 3-node chain) | PASS (explicit outcome-failure instruction) | FAIL (no per-audience DEFAULTS, no "Instead of") | 10/11 | ~99.1 |
| V-02 | PASS (V-04 R3 base, 3-node chain) | BORDERLINE ("Argument fails if" col unchanged) | PASS (per-audience DEFAULTS + "Instead of") | 10/11 | ~99.1 |
| V-03 | PASS (Produces declarations added to V-03 R3) | FAIL (prose belief mapping, no failure modes) | PASS (V-03 R3 inertia structure preserved) | 10/11 | ~99.1 |
| V-04 | PASS (V-04 R3 base) | PASS (explicit Failure Mode column) | FAIL (no per-audience DEFAULTS, no "Instead of") | 10/11 | ~99.1 |
| V-05 | PASS (V-04 R3 base) | PASS (explicit Failure Mode column) | PASS (per-audience DEFAULTS + "Instead of") | 11/11 | 100 |

**Predicted discriminator for R4:** V-05 is the only variation predicted to score 100. Discrimination between V-01/V-02/V-03/V-04 may emerge from:

1. **C-17 borderline threshold on V-02**: "Argument fails if" column from V-04 R3 -- the v4 pass condition explicitly says "a failure mode that restates the belief does not pass." If the scorer applies this strictly, V-02 may FAIL C-17 rather than pass borderline.

2. **C-18 DEFAULTS vs table inertia on V-01**: BELIEF MAP has Inertia Counter column, but those cells are not keyed to named DEFAULTS fields. C-18 requires SIGNAL DEFAULTS to contain per-audience inertia fields by name -- table columns alone may not satisfy the pass condition.

3. **"Instead of" template absence on V-01/V-04**: CTAs use BELIEF MAP Inertia Counter but without the structural "Instead of [X], [Y]" format. The C-18 pass condition requires both per-audience DEFAULTS fields and the explicit structural template -- missing either fails the criterion.
