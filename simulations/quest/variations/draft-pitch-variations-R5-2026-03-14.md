Saved to `simulations/quest/variations/draft-pitch-variations-R5-2026-03-14.md`.

---

## draft-pitch — Variations R5

**Context**: R4 V-05 scored 100/Platinum on v4 (all 18 criteria). v5 adds C-19/C-20/C-21. Against v5 rubric, R4 V-05 passes C-19 (embedded negative example) and C-20 (`[active Exec inertia from SIGNAL DEFAULTS]` names source within placeholder) but **fails C-21** — the CTA sources exclusively from SIGNAL DEFAULTS (static block), and C-21 requires a placeholder naming a *dynamic gate output* produced by a prior gate step. R5 retroscore: **98.57**.

---

**Variation map:**

| ID | Axis | Key change | Predicted |
|----|------|-----------|-----------|
| V-01 | CTA template structure | Second CTA placeholder: `[Inertia Counter from AUDIENCE BELIEF MAP, X row]` | 100 |
| V-02 | Output format | BELIEF MAP cell template uses `[active X inertia from SIGNAL DEFAULTS]` (C-20); CTA cites `[inertia argument from AUDIENCE BELIEF MAP, X row]` (C-21) | 100 |
| V-03 | Phrasing register | Two-part CTA: "Status quo: [active X from SIGNAL DEFAULTS]. Action: [Counter from AUDIENCE BELIEF MAP, X row]." Tests whether C-18 requires "Instead of" form | borderline |
| V-04 | CTA + Lifecycle | Phase 2 binding declaration uses `[active X inertia from SIGNAL DEFAULTS]` (C-20 at binding step); CTA cites AUDIENCE BELIEF MAP exclusively (C-21) | 100 |
| V-05 | All axes | BELIEF MAP column cell templates name SIGNAL DEFAULTS; CTA has both `[active X inertia from SIGNAL DEFAULTS]` (C-20) + `[Inertia Counter from AUDIENCE BELIEF MAP, X row]` (C-21) + traceability declaration | 100 |

**The C-21 key insight**: AUDIENCE BELIEF MAP is produced by Phase 2 (*Produces: AUDIENCE BELIEF MAP*) — it is a named gate output, not a static block. Any template whose placeholder names it by exact name satisfies C-21. The R4 Platinum variation's CTA `[one concrete action]` placeholder named no source; every R5 variation replaces it with `[Inertia Counter from AUDIENCE BELIEF MAP, X row]`.

**Diagnostic variation**: V-03's two-part "Status quo / Action" template is structurally equivalent to "Instead of [X], [Y]" but syntactically different. If C-18 is form-agnostic, all five score 100. If C-18 requires the "Instead of" form, V-03 drops to 99.3.
-21). This separates the static and dynamic source citations into different template locations.

- **V-03**: Replaces the "Instead of [X], [Y]" CTA with a two-part structural template: "Status quo: [active X inertia from SIGNAL DEFAULTS]. Action: [Inertia Counter from AUDIENCE BELIEF MAP, X row]." Tests whether the "Instead of" form is required by C-18 or whether any explicit two-part structural template satisfies it.

- **V-04**: Makes the DEFAULTS-to-BELIEF MAP binding explicit as a step instruction in Phase 2 — "Inertia Excuse cells must be filled with `[active X inertia from SIGNAL DEFAULTS]`." This moves C-20's structural template from the CTA location to the BELIEF MAP step, and CTA then cites AUDIENCE BELIEF MAP directly.

- **V-05**: Full synthesis — BELIEF MAP Inertia Excuse column cell instructions use `[active [audience] inertia from SIGNAL DEFAULTS]` (C-20); CTA template uses `[Inertia Counter from AUDIENCE BELIEF MAP, [audience] row]` (C-21); a traceability declaration names the two distinct source types explicitly. Predicted 100 under v5 rubric.

---

## V-01 — Single Axis: CTA Template Structure (Minimal C-21 Fix)

**Axis**: CTA template structure — the second CTA placeholder changes from `[one concrete action]` to `[Inertia Counter from AUDIENCE BELIEF MAP, X row]`. All other V-05 R4 structure is preserved verbatim.

**Hypothesis**: V-05 R4 fails C-21 because its CTA template `"Instead of [active X inertia from SIGNAL DEFAULTS], [one concrete action]"` sources only from SIGNAL DEFAULTS (static). The placeholder `[one concrete action]` names no source. Adding `[Inertia Counter from AUDIENCE BELIEF MAP, X row]` as the second placeholder names AUDIENCE BELIEF MAP — produced by Phase 2 gate and locked before Phase 5 runs — satisfying C-21's requirement for a dynamic gate output reference. C-20 still passes via the first placeholder. C-18 still passes: per-audience DEFAULTS rows are present; the structural template now explicitly pre-commits the action to AUDIENCE BELIEF MAP rather than leaving it freeform. C-17 (Failure Mode column with negative example) and C-16 (3-node chain) are unchanged.

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
*Produces*: **AUDIENCE BELIEF MAP** (named output). Phase 5 references this output by exact name.

For each audience, fill all four columns. Column definitions:

- **Core Belief**: The one thing this audience must believe before any other argument can land.
- **Failure Mode**: What the pitch *fails to achieve for this audience* if Core Belief is absent. Name a pitch outcome failure -- what the pitch cannot accomplish for this audience (e.g., "Exec won't authorize the demo slot," "Dev won't try the command," "Maker won't raise the question in their next meeting"). A restatement of Core Belief in negative form does not pass (e.g., "Exec won't believe the ROI argument" -- this restates the belief and is not a Failure Mode).
- **Inertia Excuse**: What this audience says or does to justify not acting today. Use Phase 1 active inertia row for this audience from SIGNAL DEFAULTS if no scout override.
- **Inertia Counter**: The specific action that addresses this Inertia Excuse. One concrete step. This value is used by Phase 5 CTA construction.

**AUDIENCE BELIEF MAP:**

| Audience | Core Belief | Failure Mode | Inertia Excuse | Inertia Counter |
|----------|-------------|--------------|----------------|-----------------|
| Exec | [Write belief] | [Name the pitch outcome failure] | [Use active Exec inertia or scout override] | [Name the counter action] |
| Dev | [Write belief] | [Name the pitch outcome failure] | [Use active Dev inertia or scout override] | [Name the counter action] |
| Maker | [Write belief] | [Name the pitch outcome failure] | [Use active Maker inertia or scout override] | [Name the counter action] |

A cell is not complete if it restates the column header in general terms or contains a belief restatement in the Failure Mode column. Do not proceed until all twelve cells are filled.

**-- PHASE 2 COMPLETE. AUDIENCE BELIEF MAP is locked. Do not proceed until all rows are filled. --**

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

*Consumes*: AUDIENCE BELIEF MAP (from Phase 2), POSITIONING LOCK (from Phase 3), EXEC OPENING SENTENCE (from Phase 4).

Draft each version from the Core Belief in AUDIENCE BELIEF MAP. Use POSITIONING LOCK as the sole source for positioning claims. Each CTA addresses the audience's Inertia Excuse using the structural template: "Instead of [active audience inertia from SIGNAL DEFAULTS], [Inertia Counter from AUDIENCE BELIEF MAP, audience row]."

**Exec Version**
*Core Belief (from AUDIENCE BELIEF MAP, exec row).*

- **Hook**: EXEC OPENING SENTENCE (from Phase 4, locked, exact).
- **What It Does**: POSITIONING LOCK Outcome answer. One sentence.
- **Why It Matters**: POSITIONING LOCK Competitor named explicitly. "The alternative is not a competing product. It is [Competitor]." 2-3 sentences ROI framing.
- **Call to Action**: "Instead of [active Exec inertia from SIGNAL DEFAULTS], [Inertia Counter from AUDIENCE BELIEF MAP, exec row]."

**Dev Version**
*Core Belief (from AUDIENCE BELIEF MAP, dev row).*

- **Hook**: A scenario the developer is in right now -- the moment before Signal changes what happens next.
- **What It Does**: At least one concrete interaction. Example: `/scout:requirements topic={topic}` produces `{topic}-requirements-{date}.md`. Reader answers "what would I actually type?"
- **Why It Matters**: Active Dev friction from SIGNAL DEFAULTS. Named directly.
- **Call to Action**: "Instead of [active Dev inertia from SIGNAL DEFAULTS], [Inertia Counter from AUDIENCE BELIEF MAP, dev row]."

**Maker Version**
*Core Belief (from AUDIENCE BELIEF MAP, maker row).*

- **Hook**: The question they have already asked themselves. Zero unexplained acronyms. Zero namespace references. Zero CLI terminology.
- **What It Does**: Plain English. Translate every Signal term to what it does for a person.
- **Why It Matters**: Active Maker outcome from SIGNAL DEFAULTS. Connect to decision context.
- **Call to Action**: "Instead of [active Maker inertia from SIGNAL DEFAULTS], [Inertia Counter from AUDIENCE BELIEF MAP, maker row]."

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

All phase outputs (active values, AUDIENCE BELIEF MAP, POSITIONING LOCK, EXEC OPENING SENTENCE, proof audit) are working notes -- not in saved artifact.

**Save to**: `simulations/draft/pitches/{topic}-pitch-{date}.md`

---

## V-02 — Single Axis: Output Format (BELIEF MAP Cell Template as C-20 Source; CTA as C-21 Source)

**Axis**: Output format -- BELIEF MAP Inertia Excuse column cell instructions use an explicit template placeholder naming SIGNAL DEFAULTS: `[active X inertia from SIGNAL DEFAULTS]`. The CTA template changes to reference the inertia argument from the dynamic gate output: "Instead of [inertia argument from AUDIENCE BELIEF MAP, X row], [one concrete action]."

**Hypothesis**: V-05 R4 passed C-20 via `[active Exec inertia from SIGNAL DEFAULTS]` in the CTA and failed C-21 because the CTA's action placeholder was freeform. This variation inverts the source allocation: C-20 is satisfied by the BELIEF MAP step's cell instruction template (`[active X inertia from SIGNAL DEFAULTS]` in the column definition); C-21 is satisfied by the CTA template which now cites AUDIENCE BELIEF MAP (the dynamic gate output from Phase 2) as its inertia source. C-18 passes because per-audience DEFAULTS rows are present in SIGNAL DEFAULTS and the CTA addresses audience-specific inertia via a structural template; the indirection through AUDIENCE BELIEF MAP (which was populated from SIGNAL DEFAULTS per-audience rows) does not break C-18. Tests whether C-20 is satisfiable by a BELIEF MAP cell instruction template rather than only at the CTA level.

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
*Produces*: **AUDIENCE BELIEF MAP** (named output). Phase 5 references this output by exact name.

For each audience, fill all four columns. Column definitions:

- **Core Belief**: The one thing this audience must believe before any other argument can land.
- **Failure Mode**: What the pitch *fails to achieve for this audience* if Core Belief is absent. Name a pitch outcome failure -- what the pitch cannot accomplish for this audience (e.g., "Exec won't authorize the demo slot," "Dev won't try the command," "Maker won't raise the question in their next meeting"). A restatement of Core Belief in negative form does not pass (e.g., "Exec won't believe the ROI argument" -- this restates the belief and is not a Failure Mode).
- **Inertia Excuse**: Fill with the active inertia value from SIGNAL DEFAULTS for this audience. Template: `[active Exec inertia from SIGNAL DEFAULTS]` / `[active Dev inertia from SIGNAL DEFAULTS]` / `[active Maker inertia from SIGNAL DEFAULTS]`. Use scout override if available; otherwise use SIGNAL DEFAULTS value exactly. This becomes the inertia argument for Phase 5 CTA construction.
- **Inertia Counter**: The specific action that addresses this Inertia Excuse. One concrete step.

**AUDIENCE BELIEF MAP:**

| Audience | Core Belief | Failure Mode | Inertia Excuse | Inertia Counter |
|----------|-------------|--------------|----------------|-----------------|
| Exec | [Write belief] | [Name the pitch outcome failure] | [active Exec inertia from SIGNAL DEFAULTS] | [Name the counter action] |
| Dev | [Write belief] | [Name the pitch outcome failure] | [active Dev inertia from SIGNAL DEFAULTS] | [Name the counter action] |
| Maker | [Write belief] | [Name the pitch outcome failure] | [active Maker inertia from SIGNAL DEFAULTS] | [Name the counter action] |

A cell is not complete if it restates the column header in general terms or contains a belief restatement in the Failure Mode column. Do not proceed until all twelve cells are filled.

**-- PHASE 2 COMPLETE. AUDIENCE BELIEF MAP is locked. Do not proceed until all rows are filled. --**

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

*Consumes*: AUDIENCE BELIEF MAP (from Phase 2), POSITIONING LOCK (from Phase 3), EXEC OPENING SENTENCE (from Phase 4).

Draft each version from the Core Belief in AUDIENCE BELIEF MAP. Use POSITIONING LOCK as the sole source for positioning claims. Each CTA addresses the audience's inertia using the structural template: "Instead of [inertia argument from AUDIENCE BELIEF MAP, audience row], [one concrete action]."

**Exec Version**
*Core Belief (from AUDIENCE BELIEF MAP, exec row).*

- **Hook**: EXEC OPENING SENTENCE (from Phase 4, locked, exact).
- **What It Does**: POSITIONING LOCK Outcome answer. One sentence.
- **Why It Matters**: POSITIONING LOCK Competitor named explicitly. "The alternative is not a competing product. It is [Competitor]." 2-3 sentences ROI framing.
- **Call to Action**: "Instead of [inertia argument from AUDIENCE BELIEF MAP, exec row], [one specific decision, demo slot, or budget ask]."

**Dev Version**
*Core Belief (from AUDIENCE BELIEF MAP, dev row).*

- **Hook**: A scenario the developer is in right now -- the moment before Signal changes what happens next.
- **What It Does**: At least one concrete interaction. Example: `/scout:requirements topic={topic}` produces `{topic}-requirements-{date}.md`. Reader answers "what would I actually type?"
- **Why It Matters**: Active Dev friction from SIGNAL DEFAULTS. Named directly.
- **Call to Action**: "Instead of [inertia argument from AUDIENCE BELIEF MAP, dev row], [one runnable command or file path today]."

**Maker Version**
*Core Belief (from AUDIENCE BELIEF MAP, maker row).*

- **Hook**: The question they have already asked themselves. Zero unexplained acronyms. Zero namespace references. Zero CLI terminology.
- **What It Does**: Plain English. Translate every Signal term to what it does for a person.
- **Why It Matters**: Active Maker outcome from SIGNAL DEFAULTS. Connect to decision context.
- **Call to Action**: "Instead of [inertia argument from AUDIENCE BELIEF MAP, maker row], [something proposable in a meeting without a ticket]."

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

All phase outputs (active values, AUDIENCE BELIEF MAP, POSITIONING LOCK, EXEC OPENING SENTENCE, proof audit) are working notes -- not in saved artifact.

**Save to**: `simulations/draft/pitches/{topic}-pitch-{date}.md`

---

## V-03 — Single Axis: Phrasing Register (Two-Part CTA with Explicit Source Declarations)

**Axis**: Phrasing register -- the CTA construction changes from the "Instead of [X], [Y]" form to a two-part structural template: "Status quo: [active X inertia from SIGNAL DEFAULTS]. Action: [Inertia Counter from AUDIENCE BELIEF MAP, X row]." Each part cites its source within its placeholder.

**Hypothesis**: C-18 requires a "structural template" for CTA construction addressing audience-specific inertia. This variation tests whether the "Instead of [X], [Y]" form is required, or whether any explicit two-part structural form satisfies C-18. The two-part form has the same structural property (placeholder naming static source + placeholder naming dynamic gate output) but in a different presentation register. If C-18 is form-agnostic (structural template present, per-audience DEFAULTS rows present), V-03 will pass C-18 and both C-20 and C-21. If C-18 requires the "Instead of" form specifically, V-03 will fail C-18. This distinction determines whether the rubric tests structure or syntax.

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
*Produces*: **AUDIENCE BELIEF MAP** (named output). Phase 5 references this output by exact name.

For each audience, fill all four columns. Column definitions:

- **Core Belief**: The one thing this audience must believe before any other argument can land.
- **Failure Mode**: What the pitch *fails to achieve for this audience* if Core Belief is absent. Name a pitch outcome failure -- what the pitch cannot accomplish for this audience (e.g., "Exec won't authorize the demo slot," "Dev won't try the command," "Maker won't raise the question in their next meeting"). A restatement of Core Belief in negative form does not pass (e.g., "Exec won't believe the ROI argument" -- this restates the belief and is not a Failure Mode).
- **Inertia Excuse**: What this audience says or does to justify not acting today. Use Phase 1 active inertia row for this audience from SIGNAL DEFAULTS if no scout override.
- **Inertia Counter**: The specific action that addresses this Inertia Excuse. One concrete step.

**AUDIENCE BELIEF MAP:**

| Audience | Core Belief | Failure Mode | Inertia Excuse | Inertia Counter |
|----------|-------------|--------------|----------------|-----------------|
| Exec | [Write belief] | [Name the pitch outcome failure] | [Use active Exec inertia or scout override] | [Name the counter action] |
| Dev | [Write belief] | [Name the pitch outcome failure] | [Use active Dev inertia or scout override] | [Name the counter action] |
| Maker | [Write belief] | [Name the pitch outcome failure] | [Use active Maker inertia or scout override] | [Name the counter action] |

A cell is not complete if it restates the column header in general terms or contains a belief restatement in the Failure Mode column. Do not proceed until all twelve cells are filled.

**-- PHASE 2 COMPLETE. AUDIENCE BELIEF MAP is locked. Do not proceed until all rows are filled. --**

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

*Consumes*: AUDIENCE BELIEF MAP (from Phase 2), POSITIONING LOCK (from Phase 3), EXEC OPENING SENTENCE (from Phase 4).

Draft each version from the Core Belief in AUDIENCE BELIEF MAP. Use POSITIONING LOCK as the sole source for positioning claims. Each CTA uses the two-part structural template: first state the inertia cost from SIGNAL DEFAULTS; then state the counter action from AUDIENCE BELIEF MAP.

**CTA structural template (all three versions)**:
> "Status quo: [active X inertia from SIGNAL DEFAULTS]. Action: [Inertia Counter from AUDIENCE BELIEF MAP, X row]."

**Exec Version**
*Core Belief (from AUDIENCE BELIEF MAP, exec row).*

- **Hook**: EXEC OPENING SENTENCE (from Phase 4, locked, exact).
- **What It Does**: POSITIONING LOCK Outcome answer. One sentence.
- **Why It Matters**: POSITIONING LOCK Competitor named explicitly. "The alternative is not a competing product. It is [Competitor]." 2-3 sentences ROI framing.
- **Call to Action**: "Status quo: [active Exec inertia from SIGNAL DEFAULTS]. Action: [Inertia Counter from AUDIENCE BELIEF MAP, exec row]."

**Dev Version**
*Core Belief (from AUDIENCE BELIEF MAP, dev row).*

- **Hook**: A scenario the developer is in right now -- the moment before Signal changes what happens next.
- **What It Does**: At least one concrete interaction. Example: `/scout:requirements topic={topic}` produces `{topic}-requirements-{date}.md`. Reader answers "what would I actually type?"
- **Why It Matters**: Active Dev friction from SIGNAL DEFAULTS. Named directly.
- **Call to Action**: "Status quo: [active Dev inertia from SIGNAL DEFAULTS]. Action: [Inertia Counter from AUDIENCE BELIEF MAP, dev row]."

**Maker Version**
*Core Belief (from AUDIENCE BELIEF MAP, maker row).*

- **Hook**: The question they have already asked themselves. Zero unexplained acronyms. Zero namespace references. Zero CLI terminology.
- **What It Does**: Plain English. Translate every Signal term to what it does for a person.
- **Why It Matters**: Active Maker outcome from SIGNAL DEFAULTS. Connect to decision context.
- **Call to Action**: "Status quo: [active Maker inertia from SIGNAL DEFAULTS]. Action: [Inertia Counter from AUDIENCE BELIEF MAP, maker row]."

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

All phase outputs (active values, AUDIENCE BELIEF MAP, POSITIONING LOCK, EXEC OPENING SENTENCE, proof audit) are working notes -- not in saved artifact.

**Save to**: `simulations/draft/pitches/{topic}-pitch-{date}.md`

---

## V-04 — Combined: CTA Template + Lifecycle (BELIEF MAP Binding Declaration + CTA References AUDIENCE BELIEF MAP)

**Axes**: CTA template structure + lifecycle emphasis -- Phase 2 adds an explicit binding declaration that names SIGNAL DEFAULTS fields as the source for Inertia Excuse cells using placeholder syntax; Phase 5 CTA template references AUDIENCE BELIEF MAP directly for the inertia argument (C-21) while the binding declaration in Phase 2 provides C-20.

**Hypothesis**: The structural template for C-20 does not have to be the CTA. If Phase 2 contains an explicit cell instruction using `[active X inertia from SIGNAL DEFAULTS]` as a template placeholder (naming SIGNAL DEFAULTS within the placeholder text), C-20 is satisfied at the binding step rather than the CTA step. Then the CTA can reference AUDIENCE BELIEF MAP exclusively, satisfying C-21 without a dual-placeholder CTA. This tests whether the C-20/C-21 source citations must both appear in the same template or whether they can appear in different templates at different steps in the skill.

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
- `simulations/scout/competitors/{topic}-positioning-*.md`
- `simulations/scout/requirements/{topic}-requirements-*.md`

Write: "Signals found: [list files]" or "No prior signals -- SIGNAL DEFAULTS apply."

For each signal found: note which SIGNAL DEFAULTS rows it overrides and the override value.

**Phase 1 output**: active values table -- which DEFAULTS fields are overridden and by what.

**-- PHASE 1 COMPLETE. Do not proceed until active values are written. --**

---

**=== PHASE 2: BELIEF MAP ===**

*Consumes*: Phase 1 active values.
*Produces*: **AUDIENCE BELIEF MAP** (named output). Phase 5 references this output by exact name.

**DEFAULTS binding**: Before filling the table, copy the active inertia values for each audience from SIGNAL DEFAULTS into the Inertia Excuse column using these templates:
- Exec row: `[active Exec inertia from SIGNAL DEFAULTS]` (or scout override)
- Dev row: `[active Dev inertia from SIGNAL DEFAULTS]` (or scout override)
- Maker row: `[active Maker inertia from SIGNAL DEFAULTS]` (or scout override)

These filled values become the AUDIENCE BELIEF MAP inertia arguments used in Phase 5 CTA construction.

For each audience, fill all four columns. Column definitions:

- **Core Belief**: The one thing this audience must believe before any other argument can land.
- **Failure Mode**: What the pitch *fails to achieve for this audience* if Core Belief is absent. Name a pitch outcome failure -- what the pitch cannot accomplish for this audience (e.g., "Exec won't authorize the demo slot," "Dev won't try the command," "Maker won't raise the question in their next meeting"). A restatement of Core Belief in negative form does not pass (e.g., "Exec won't believe the ROI argument" -- this restates the belief and is not a Failure Mode).
- **Inertia Excuse**: Fill from DEFAULTS binding above (or scout override).
- **Inertia Counter**: The specific action that addresses this Inertia Excuse. One concrete step.

**AUDIENCE BELIEF MAP:**

| Audience | Core Belief | Failure Mode | Inertia Excuse | Inertia Counter |
|----------|-------------|--------------|----------------|-----------------|
| Exec | [Write belief] | [Name the pitch outcome failure] | [active Exec inertia from SIGNAL DEFAULTS] | [Name the counter action] |
| Dev | [Write belief] | [Name the pitch outcome failure] | [active Dev inertia from SIGNAL DEFAULTS] | [Name the counter action] |
| Maker | [Write belief] | [Name the pitch outcome failure] | [active Maker inertia from SIGNAL DEFAULTS] | [Name the counter action] |

A cell is not complete if it restates the column header in general terms or contains a belief restatement in the Failure Mode column. Do not proceed until all twelve cells are filled.

**-- PHASE 2 COMPLETE. AUDIENCE BELIEF MAP is locked. Do not proceed until all rows are filled. --**

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

*Consumes*: AUDIENCE BELIEF MAP (from Phase 2), POSITIONING LOCK (from Phase 3), EXEC OPENING SENTENCE (from Phase 4).

Draft each version from the Core Belief in AUDIENCE BELIEF MAP. Use POSITIONING LOCK as the sole source for positioning claims. Each CTA uses the structural template: "Instead of [inertia argument from AUDIENCE BELIEF MAP, audience row], [Inertia Counter from AUDIENCE BELIEF MAP, audience row]."

**Exec Version**
*Core Belief (from AUDIENCE BELIEF MAP, exec row).*

- **Hook**: EXEC OPENING SENTENCE (from Phase 4, locked, exact).
- **What It Does**: POSITIONING LOCK Outcome answer. One sentence.
- **Why It Matters**: POSITIONING LOCK Competitor named explicitly. "The alternative is not a competing product. It is [Competitor]." 2-3 sentences ROI framing.
- **Call to Action**: "Instead of [inertia argument from AUDIENCE BELIEF MAP, exec row], [Inertia Counter from AUDIENCE BELIEF MAP, exec row]."

**Dev Version**
*Core Belief (from AUDIENCE BELIEF MAP, dev row).*

- **Hook**: A scenario the developer is in right now -- the moment before Signal changes what happens next.
- **What It Does**: At least one concrete interaction. Example: `/scout:requirements topic={topic}` produces `{topic}-requirements-{date}.md`. Reader answers "what would I actually type?"
- **Why It Matters**: Active Dev friction from SIGNAL DEFAULTS. Named directly.
- **Call to Action**: "Instead of [inertia argument from AUDIENCE BELIEF MAP, dev row], [Inertia Counter from AUDIENCE BELIEF MAP, dev row]."

**Maker Version**
*Core Belief (from AUDIENCE BELIEF MAP, maker row).*

- **Hook**: The question they have already asked themselves. Zero unexplained acronyms. Zero namespace references. Zero CLI terminology.
- **What It Does**: Plain English. Translate every Signal term to what it does for a person.
- **Why It Matters**: Active Maker outcome from SIGNAL DEFAULTS. Connect to decision context.
- **Call to Action**: "Instead of [inertia argument from AUDIENCE BELIEF MAP, maker row], [Inertia Counter from AUDIENCE BELIEF MAP, maker row]."

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

All phase outputs (active values, AUDIENCE BELIEF MAP, POSITIONING LOCK, EXEC OPENING SENTENCE, proof audit) are working notes -- not in saved artifact.

**Save to**: `simulations/draft/pitches/{topic}-pitch-{date}.md`

---

## V-05 — Combined: All Three Axes (C-19 + C-20 + C-21 Full Synthesis)

**Axes**: CTA template structure + output format + lifecycle emphasis -- BELIEF MAP Inertia Excuse column cell instructions use `[active [audience] inertia from SIGNAL DEFAULTS]` as explicit template placeholders (C-20 at binding step); CTA template uses `[Inertia Counter from AUDIENCE BELIEF MAP, [audience] row]` naming AUDIENCE BELIEF MAP as dynamic gate output (C-21); a traceability declaration in Phase 5 explicitly names the two distinct source types and their provenance; Failure Mode column retains embedded negative example (C-19).

**Hypothesis**: V-05 is the first variation designed to simultaneously satisfy all 14 aspirational criteria under v5 rubric. Three changes applied to V-05 R4's phase backbone: (a) BELIEF MAP Inertia Excuse column definition includes explicit cell templates naming SIGNAL DEFAULTS by name within the placeholder syntax, satisfying C-20 at the BELIEF MAP step; (b) CTA template adds AUDIENCE BELIEF MAP as the second placeholder source, satisfying C-21 with a named dynamic gate output; (c) a traceability declaration in Phase 5 identifies the two source types by kind (static vs. dynamic), making the dependency structure inspectable from skill text alone. C-19 is preserved from V-05 R4 (Failure Mode column with embedded negative example). Predicted composite: 100 (Platinum) under v5 rubric.

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
*Produces*: **AUDIENCE BELIEF MAP** (named output). Phase 5 references this output by exact name.

For each audience, fill all four columns. Column definitions:

- **Core Belief**: The one thing this audience must believe before any other argument can land.
- **Failure Mode**: What the pitch *fails to achieve for this audience* if Core Belief is absent. Name a pitch outcome failure -- what the pitch cannot accomplish for this audience (e.g., "Exec won't authorize the demo slot," "Dev won't try the command," "Maker won't raise the question in their next meeting"). A restatement of Core Belief in negative form does not pass (e.g., "Exec won't believe the ROI argument" -- this restates the belief and is not a Failure Mode).
- **Inertia Excuse**: Fill with the active inertia for this audience from SIGNAL DEFAULTS using the per-audience template: `[active Exec inertia from SIGNAL DEFAULTS]` / `[active Dev inertia from SIGNAL DEFAULTS]` / `[active Maker inertia from SIGNAL DEFAULTS]`. Use scout override value if one exists; otherwise use the SIGNAL DEFAULTS value exactly. These cells become the inertia arguments for Phase 5 CTA construction.
- **Inertia Counter**: The specific action that addresses this Inertia Excuse. One concrete step. Pre-commit this value -- Phase 5 CTA uses `[Inertia Counter from AUDIENCE BELIEF MAP, audience row]` by exact reference. Do not leave ambiguous.

**AUDIENCE BELIEF MAP:**

| Audience | Core Belief | Failure Mode | Inertia Excuse | Inertia Counter |
|----------|-------------|--------------|----------------|-----------------|
| Exec | [Write belief] | [Name the pitch outcome failure] | [active Exec inertia from SIGNAL DEFAULTS] | [Name the counter action] |
| Dev | [Write belief] | [Name the pitch outcome failure] | [active Dev inertia from SIGNAL DEFAULTS] | [Name the counter action] |
| Maker | [Write belief] | [Name the pitch outcome failure] | [active Maker inertia from SIGNAL DEFAULTS] | [Name the counter action] |

A cell is not complete if it restates the column header in general terms or contains a belief restatement in the Failure Mode column. Do not proceed until all twelve cells are filled.

**-- PHASE 2 COMPLETE. AUDIENCE BELIEF MAP is locked. Do not proceed until all rows are filled. --**

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

*Consumes*: AUDIENCE BELIEF MAP (from Phase 2), POSITIONING LOCK (from Phase 3), EXEC OPENING SENTENCE (from Phase 4).

Draft each version from the Core Belief in AUDIENCE BELIEF MAP. Use POSITIONING LOCK as the sole source for positioning claims.

**CTA construction template (all three versions)**:
> "Instead of [active [audience] inertia from SIGNAL DEFAULTS], [Inertia Counter from AUDIENCE BELIEF MAP, [audience] row]."

The two placeholders have distinct source types:
- `[active [audience] inertia from SIGNAL DEFAULTS]` -- draws from SIGNAL DEFAULTS (static block, available before any phase runs; row value for this audience).
- `[Inertia Counter from AUDIENCE BELIEF MAP, [audience] row]` -- draws from AUDIENCE BELIEF MAP (gate output from Phase 2, produced and locked before Phase 5 begins; exact name used in *Produces* declaration above).

Both placeholders must be resolved before CTA construction is complete. A CTA with either placeholder unfilled does not pass.

**Exec Version**
*Core Belief (from AUDIENCE BELIEF MAP, exec row).*

- **Hook**: EXEC OPENING SENTENCE (from Phase 4, locked, exact).
- **What It Does**: POSITIONING LOCK Outcome answer. One sentence.
- **Why It Matters**: POSITIONING LOCK Competitor named explicitly. "The alternative is not a competing product. It is [Competitor]." 2-3 sentences ROI framing.
- **Call to Action**: "Instead of [active Exec inertia from SIGNAL DEFAULTS], [Inertia Counter from AUDIENCE BELIEF MAP, exec row]."

**Dev Version**
*Core Belief (from AUDIENCE BELIEF MAP, dev row).*

- **Hook**: A scenario the developer is in right now -- the moment before Signal changes what happens next.
- **What It Does**: At least one concrete interaction. Example: `/scout:requirements topic={topic}` produces `{topic}-requirements-{date}.md`. Reader answers "what would I actually type?"
- **Why It Matters**: Active Dev friction from SIGNAL DEFAULTS. Named directly.
- **Call to Action**: "Instead of [active Dev inertia from SIGNAL DEFAULTS], [Inertia Counter from AUDIENCE BELIEF MAP, dev row]."

**Maker Version**
*Core Belief (from AUDIENCE BELIEF MAP, maker row).*

- **Hook**: The question they have already asked themselves. Zero unexplained acronyms. Zero namespace references. Zero CLI terminology.
- **What It Does**: Plain English. Translate every Signal term to what it does for a person.
- **Why It Matters**: Active Maker outcome from SIGNAL DEFAULTS. Connect to decision context.
- **Call to Action**: "Instead of [active Maker inertia from SIGNAL DEFAULTS], [Inertia Counter from AUDIENCE BELIEF MAP, maker row]."

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

All phase outputs (active values, AUDIENCE BELIEF MAP, POSITIONING LOCK, EXEC OPENING SENTENCE, proof audit) are working notes -- not in saved artifact.

**Save to**: `simulations/draft/pitches/{topic}-pitch-{date}.md`

---

## R5 Design Notes

**What changed from R4:**

R4 confirmed V-05 as Platinum (100/100) under v4 rubric. The R4 scorecard surfaced three excellence signals that became C-19/C-20/C-21 in the v5 rubric. Against v5, R4 V-05 passes C-19 (embedded negative example in Failure Mode column definition) and C-20 (CTA template `[active Exec inertia from SIGNAL DEFAULTS]` names source within placeholder) but fails C-21 (CTA sources exclusively from SIGNAL DEFAULTS, a static block; C-21 requires a placeholder naming a dynamic gate output produced by a prior gate step). R5 task: add C-21 by introducing a template placeholder naming AUDIENCE BELIEF MAP (the Phase 2 gate output) while preserving all prior criteria.

**Retroactive R4 V-05 score under v5 rubric (denominator 14 aspirational):**

| Criterion | V-05 R4 Result | Evidence |
|-----------|---------------|----------|
| C-19 | PASS | "A restatement of Core Belief in negative form does not pass (e.g., 'Exec won't believe the ROI argument' -- this restates the belief and is not a Failure Mode)" -- embedded named negative example |
| C-20 | PASS | CTA template: `[active Exec inertia from SIGNAL DEFAULTS]` -- names SIGNAL DEFAULTS within the placeholder; SIGNAL DEFAULTS appears at top of skill |
| C-21 | FAIL | CTA template sources only from SIGNAL DEFAULTS (static block); no placeholder naming a dynamic gate output (AUDIENCE BELIEF MAP, POSITIONING LOCK, EXEC OPENING SENTENCE) |

```
R4 V-05 score under v5 = (4/4 * 60) + (3/3 * 30) + (12/14 * 10)
                        = 60 + 30 + 8.57
                        = 98.57
```

**Predicted R5 scores under v5 rubric:**

| Variation | C-19 | C-20 | C-21 | Aspirational | Composite |
|-----------|------|------|------|--------------|-----------|
| V-01 | PASS | PASS (first CTA placeholder names SIGNAL DEFAULTS) | PASS (second CTA placeholder names AUDIENCE BELIEF MAP) | 14/14 | 100 |
| V-02 | PASS | PASS (BELIEF MAP cell instruction uses `[active X inertia from SIGNAL DEFAULTS]`) | PASS (CTA cites `[inertia argument from AUDIENCE BELIEF MAP, X row]`) | 14/14 | 100 |
| V-03 | PASS | PASS (Part 1 template names SIGNAL DEFAULTS) | PASS (Part 2 template names AUDIENCE BELIEF MAP) | 14/14 if C-18 passes | borderline |
| V-04 | PASS | PASS (BELIEF MAP binding declaration uses `[active X inertia from SIGNAL DEFAULTS]`) | PASS (CTA cites `[inertia argument from AUDIENCE BELIEF MAP, X row]`) | 14/14 | 100 |
| V-05 | PASS | PASS (BELIEF MAP column cell template + CTA first placeholder) | PASS (CTA second placeholder names AUDIENCE BELIEF MAP) | 14/14 | 100 |

**Predicted discriminator for R5:** V-03 is the diagnostic variation. Its two-part CTA template ("Status quo: ... Action: ...") differs structurally from the "Instead of [X], [Y]" form. If C-18 requires the specific "Instead of" framing, V-03 fails C-18 and scores 99.3. If C-18 is form-agnostic (any explicit structural template with per-audience inertia from DEFAULTS), V-03 passes and all five variations score 100.

The four remaining variations (V-01, V-02, V-04, V-05) differ only in where the C-20 template appears (CTA vs. BELIEF MAP step) and whether both CTA placeholders appear in the same instruction or are split across phases. All four should score 100 under v5 rubric.

**Discrimination within predicted 100 cluster:**

| Variation | C-20 template location | C-21 template location | Structural integration |
|-----------|----------------------|----------------------|----------------------|
| V-01 | CTA (first placeholder) | CTA (second placeholder) | Both sources in same CTA line |
| V-02 | BELIEF MAP cell instruction | CTA | Sources split: static binding at BELIEF MAP step, dynamic at CTA |
| V-04 | BELIEF MAP binding declaration (prose + template) | CTA | Sources split: static binding as pre-table instruction, dynamic at CTA |
| V-05 | BELIEF MAP column definition + CTA (first placeholder) | CTA (second placeholder) | Both sources in CTA; also present in BELIEF MAP column definition |

V-05's traceability declaration in Phase 5 makes the two-source structure explicit in prose: it names both source types, their provenance, and the constraint that both placeholders must be resolved. This is the strongest structural enforcement of C-21's "visible execution dependency" requirement.

---

```json
{"context": "R5 targets C-21 (dynamic gate output in template placeholder)", "base": "R4 V-05 (Platinum, 100/100 on v4 rubric; 98.57 on v5 rubric)", "discriminator": "V-03 tests whether C-18 requires 'Instead of' form or accepts any structural two-part template", "predicted_platinum": ["V-01", "V-02", "V-04", "V-05"], "predicted_borderline": ["V-03"], "new_pattern_hypothesis": "Dual-source CTA template with explicit static+dynamic source declaration creates a visible three-tier traceability chain: SIGNAL DEFAULTS -> AUDIENCE BELIEF MAP cells (bound at Phase 2) -> CTA assembly (named at Phase 5)"}
```
