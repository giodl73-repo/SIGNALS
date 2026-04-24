Saved to `simulations/quest/variations/draft-pitch-variations-R6-2026-03-14.md`.

---

## draft-pitch — Variations R6

**Context**: R5 V-05 retroscores **98.24** against v6. R5 V-04 retroscores **99.41** (already passes C-22 and C-23, fails C-24).

---

**Variation map:**

| ID | Axis | Key change | Predicted |
|----|------|-----------|-----------|
| V-01 | CTA template / output format | All CTA placeholders cite AUDIENCE BELIEF MAP; absorption declared in Inertia Excuse column instruction | 98.82 |
| V-02 | Lifecycle emphasis | Formal BINDING DECLARATION table at top of Phase 2; CTA unchanged (C-22 intentionally untargeted) | 98.82 |
| V-03 | Phrasing register | Inline provenance bracket notation `[Phase N gate output | type | locked before Phase 5]` at every Phase 5 gate-output citation | 98.82 |
| V-04 | CTA template + Lifecycle | C-22 CTA + C-23 binding table; no inline provenance | 99.41 |
| V-05 | All axes | C-22 CTA + C-23 binding table + C-24 inline provenance at all Phase 5 citations | **100** |

---

**Three structural changes across the round:**

**C-22** — The R5 V-05 CTA `"Instead of [active [audience] inertia from SIGNAL DEFAULTS], [Inertia Counter from AUDIENCE BELIEF MAP, row]"` has its first placeholder citing a static block. Fix: absorb DEFAULTS inertia into AUDIENCE BELIEF MAP Inertia Excuse cells at Phase 2 fill time, then change both CTA slots to `[Inertia Excuse from AUDIENCE BELIEF MAP, row]` and `[Inertia Counter from AUDIENCE BELIEF MAP, row]`. AUDIENCE BELIEF MAP becomes the sole CTA source.

**C-23** — R5 V-05 embeds the DEFAULTS→column binding inside the Inertia Excuse column definition paragraph. C-23 requires a formal declaration block *at the top* of Phase 2 that maps SIGNAL DEFAULTS fields to BELIEF MAP columns as an auditable table — readable before any column definitions are encountered.

**C-24** — R5 V-05's traceability declaration at the CTA construction step names both source types, but C-24 requires provenance *at each individual gate-output citation* in Phase 5 (at `*Consumes*`, at Hook, at What/Why, and inside CTA placeholder syntax). V-03 and V-05 add bracket notation `[Phase N gate output | type | locked before Phase 5 begins]` inline at every citation point.

**Diagnostic question:** Does C-24 require provenance embedded inside placeholder syntax (V-05 form: `[Inertia Counter from AUDIENCE BELIEF MAP [Phase 2 gate output, locked...], exec row]`) or is instruction-line-level annotation sufficient? The scorecard will resolve.

**Golden candidate: V-05** — three-axis synthesis, all C-22/C-23/C-24 patterns co-present, full provenance chain inspectable at BINDING DECLARATION (Phase 2), CTA template (Phase 5), and per-cite bracket annotations throughout version bodies.
eability declaration is a block in Phase 5 at CTA construction time that names both source types. C-24 requires provenance at every individual gate-output citation in Phase 5 -- at the *Consumes* line, at each Hook/What/Why reference, and at each CTA placeholder -- not just in one traceability block.

---

## V-01 -- Single Axis: CTA Template (C-22 Target)

**Axis**: Output format / inertia framing -- CTA structural template changes so all placeholders cite AUDIENCE BELIEF MAP (the Phase 2 dynamic gate output). DEFAULTS inertia values are absorbed into AUDIENCE BELIEF MAP Inertia Excuse cells at Phase 2 fill time. Phase 5 CTA does not reference SIGNAL DEFAULTS directly. Traceability declaration updated to single-source declaration.

**Hypothesis**: R5 V-05 fails C-22 because the CTA's first placeholder `[active [audience] inertia from SIGNAL DEFAULTS]` cites a static block directly. C-22 requires all placeholders in the CTA template to cite the same dynamic gate output. The fix: change the CTA first placeholder from the DEFAULTS inertia row to `[Inertia Excuse from AUDIENCE BELIEF MAP, [audience] row]`. Phase 2 Inertia Excuse column instruction already uses `[active [audience] inertia from SIGNAL DEFAULTS]` as the fill template -- this absorption step is the binding that transfers DEFAULTS values into AUDIENCE BELIEF MAP. Once both CTA slots reference AUDIENCE BELIEF MAP, C-22 passes. No Phase 2 top binding declaration (C-23 not targeted). No inline provenance changes (C-24 not targeted). Predicted composite: 98.82 (C-22 PASS, C-23 FAIL, C-24 FAIL).

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
- **Inertia Excuse**: Fill with the active inertia for this audience from SIGNAL DEFAULTS using the per-audience template: `[active Exec inertia from SIGNAL DEFAULTS]` / `[active Dev inertia from SIGNAL DEFAULTS]` / `[active Maker inertia from SIGNAL DEFAULTS]`. Use scout override value if one exists; otherwise use the SIGNAL DEFAULTS value exactly. **These cells absorb SIGNAL DEFAULTS inertia values into AUDIENCE BELIEF MAP and become the single authoritative source for Phase 5 CTA construction. Phase 5 CTA references AUDIENCE BELIEF MAP, not SIGNAL DEFAULTS directly.**
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
> "Instead of [Inertia Excuse from AUDIENCE BELIEF MAP, [audience] row], [Inertia Counter from AUDIENCE BELIEF MAP, [audience] row]."

Both placeholders draw from the same source -- AUDIENCE BELIEF MAP (Phase 2 gate output, produced and locked before Phase 5 begins):
- `[Inertia Excuse from AUDIENCE BELIEF MAP, [audience] row]` -- the Inertia Excuse cell for this audience, absorbed from SIGNAL DEFAULTS active inertia at Phase 2 fill time.
- `[Inertia Counter from AUDIENCE BELIEF MAP, [audience] row]` -- the Inertia Counter cell for this audience, pre-committed at Phase 2 fill time.

AUDIENCE BELIEF MAP is the single authoritative source for both CTA slots. Phase 5 does not reference SIGNAL DEFAULTS inertia values directly. A CTA with either placeholder unfilled does not pass.

**Exec Version**
*Core Belief (from AUDIENCE BELIEF MAP, exec row).*

- **Hook**: EXEC OPENING SENTENCE (from Phase 4, locked, exact).
- **What It Does**: POSITIONING LOCK Outcome answer. One sentence.
- **Why It Matters**: POSITIONING LOCK Competitor named explicitly. "The alternative is not a competing product. It is [Competitor]." 2-3 sentences ROI framing.
- **Call to Action**: "Instead of [Inertia Excuse from AUDIENCE BELIEF MAP, exec row], [Inertia Counter from AUDIENCE BELIEF MAP, exec row]."

**Dev Version**
*Core Belief (from AUDIENCE BELIEF MAP, dev row).*

- **Hook**: A scenario the developer is in right now -- the moment before Signal changes what happens next.
- **What It Does**: At least one concrete interaction. Example: `/scout:requirements topic={topic}` produces `{topic}-requirements-{date}.md`. Reader answers "what would I actually type?"
- **Why It Matters**: Active Dev friction from SIGNAL DEFAULTS. Named directly.
- **Call to Action**: "Instead of [Inertia Excuse from AUDIENCE BELIEF MAP, dev row], [Inertia Counter from AUDIENCE BELIEF MAP, dev row]."

**Maker Version**
*Core Belief (from AUDIENCE BELIEF MAP, maker row).*

- **Hook**: The question they have already asked themselves. Zero unexplained acronyms. Zero namespace references. Zero CLI terminology.
- **What It Does**: Plain English. Translate every Signal term to what it does for a person.
- **Why It Matters**: Active Maker outcome from SIGNAL DEFAULTS. Connect to decision context.
- **Call to Action**: "Instead of [Inertia Excuse from AUDIENCE BELIEF MAP, maker row], [Inertia Counter from AUDIENCE BELIEF MAP, maker row]."

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

## V-02 -- Single Axis: Lifecycle Emphasis (C-23 Target)

**Axis**: Lifecycle emphasis -- Phase 2 begins with an explicit BINDING DECLARATION table that enumerates which SIGNAL DEFAULTS fields feed which AUDIENCE BELIEF MAP columns. Data flow is a named, auditable map at the top of Phase 2 before any column definition or table fill instruction. CTA is unchanged from R5 V-05 (first placeholder still cites SIGNAL DEFAULTS -- C-22 intentionally not targeted). No inline provenance (C-24 not targeted).

**Hypothesis**: C-23 requires the binding to be a structured declaration at the top of Phase 2, not embedded in column definitions. R5 V-05 puts the SIGNAL DEFAULTS->Inertia Excuse binding inside the Inertia Excuse column definition paragraph, auditable only by reading column definitions in sequence. C-23's pass condition says "data flow is auditable from skill structure alone without tracing execution" -- this implies a single visible map, not diffused across column definitions. A top-of-Phase-2 binding table makes the entire DEFAULTS->BELIEF MAP data flow readable in one place before any fill instruction is encountered. Predicted composite: 98.82 (C-22 FAIL, C-23 PASS, C-24 FAIL).

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

**PHASE 2 BINDING DECLARATION** (read before filling the table):

The following SIGNAL DEFAULTS fields are bound to AUDIENCE BELIEF MAP columns. This binding applies before any row is filled. Use Phase 1 active values (scout overrides if present; SIGNAL DEFAULTS otherwise).

| SIGNAL DEFAULTS field | Bound to | AUDIENCE BELIEF MAP column |
|----------------------|----------|---------------------------|
| Exec inertia | -> | Inertia Excuse, Exec row |
| Dev inertia | -> | Inertia Excuse, Dev row |
| Maker inertia | -> | Inertia Excuse, Maker row |

No other DEFAULTS fields are directly bound to BELIEF MAP columns. Core Belief, Failure Mode, and Inertia Counter are generated, not bound from DEFAULTS.

For each audience, fill all four columns. Column definitions:

- **Core Belief**: The one thing this audience must believe before any other argument can land.
- **Failure Mode**: What the pitch *fails to achieve for this audience* if Core Belief is absent. Name a pitch outcome failure -- what the pitch cannot accomplish for this audience (e.g., "Exec won't authorize the demo slot," "Dev won't try the command," "Maker won't raise the question in their next meeting"). A restatement of Core Belief in negative form does not pass (e.g., "Exec won't believe the ROI argument" -- this restates the belief and is not a Failure Mode).
- **Inertia Excuse**: Fill from BINDING DECLARATION above (Exec inertia / Dev inertia / Maker inertia row). Template: `[active Exec inertia from SIGNAL DEFAULTS]` / `[active Dev inertia from SIGNAL DEFAULTS]` / `[active Maker inertia from SIGNAL DEFAULTS]`. Use scout override if available.
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
- `[active [audience] inertia from SIGNAL DEFAULTS]` -- draws from SIGNAL DEFAULTS (static block, available before any phase runs; bound to Inertia Excuse column per PHASE 2 BINDING DECLARATION).
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

## V-03 -- Single Axis: Phrasing Register (C-24 Target)

**Axis**: Phrasing register -- every Phase 5 gate-output citation carries an inline provenance parenthetical that names origin phase, output type, and confirms lock-before-execution. The *Consumes* declaration expands to a provenance-annotated list. Each version body instruction that references a gate output includes provenance inline. CTA is unchanged from R5 V-05 (first placeholder still cites SIGNAL DEFAULTS -- C-22 intentionally not targeted). No Phase 2 top binding declaration (C-23 not targeted).

**Hypothesis**: R5 V-05 passes C-24 partially -- the EXEC OPENING SENTENCE citation in the Exec Hook says "(from Phase 4, locked, exact)" which names origin phase and confirms locking. But the AUDIENCE BELIEF MAP citations in the CTA have no inline provenance beyond the output name, and POSITIONING LOCK citations in What/Why steps have no provenance. C-24 requires provenance "at each gate-output citation." Adding inline parentheticals at every Phase 5 citation -- *Consumes*, Hook, What, Why, all three CTAs -- provides complete coverage. Bracket notation `[Phase N gate output | type | locked before Phase 5]` is compact enough to avoid bloating version body instructions. Predicted composite: 98.82 (C-22 FAIL, C-23 FAIL, C-24 PASS).

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

*Consumes* (with provenance):
- **AUDIENCE BELIEF MAP** [Phase 2 gate output | named table | locked before Phase 5 begins]
- **POSITIONING LOCK** [Phase 3 gate output | named block | locked before Phase 5 begins]
- **EXEC OPENING SENTENCE** [Phase 4 gate output | named sentence | binary-gate verified | locked before Phase 5 begins]

Draft each version from the Core Belief in AUDIENCE BELIEF MAP. Use POSITIONING LOCK as the sole source for positioning claims.

**CTA construction template (all three versions)**:
> "Instead of [active [audience] inertia from SIGNAL DEFAULTS], [Inertia Counter from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], [audience] row]."

The two placeholders have distinct source types:
- `[active [audience] inertia from SIGNAL DEFAULTS]` -- static block, available before any phase runs.
- `[Inertia Counter from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], [audience] row]` -- dynamic gate output from Phase 2, locked before this phase begins.

Both placeholders must be resolved before CTA construction is complete.

**Exec Version**
*Core Belief (from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], exec row).*

- **Hook**: EXEC OPENING SENTENCE [Phase 4 gate output | binary-gate verified | locked before Phase 5 begins] -- use exact text, no edits.
- **What It Does**: POSITIONING LOCK [Phase 3 gate output | locked before Phase 5 begins] Outcome answer. One sentence.
- **Why It Matters**: POSITIONING LOCK [Phase 3 gate output | locked before Phase 5 begins] Competitor named explicitly. "The alternative is not a competing product. It is [Competitor]." 2-3 sentences ROI framing.
- **Call to Action**: "Instead of [active Exec inertia from SIGNAL DEFAULTS], [Inertia Counter from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], exec row]."

**Dev Version**
*Core Belief (from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], dev row).*

- **Hook**: A scenario the developer is in right now -- the moment before Signal changes what happens next.
- **What It Does**: At least one concrete interaction. Example: `/scout:requirements topic={topic}` produces `{topic}-requirements-{date}.md`. Reader answers "what would I actually type?"
- **Why It Matters**: Active Dev friction from SIGNAL DEFAULTS. Named directly.
- **Call to Action**: "Instead of [active Dev inertia from SIGNAL DEFAULTS], [Inertia Counter from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], dev row]."

**Maker Version**
*Core Belief (from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], maker row).*

- **Hook**: The question they have already asked themselves. Zero unexplained acronyms. Zero namespace references. Zero CLI terminology.
- **What It Does**: Plain English. Translate every Signal term to what it does for a person.
- **Why It Matters**: Active Maker outcome from SIGNAL DEFAULTS. Connect to decision context.
- **Call to Action**: "Instead of [active Maker inertia from SIGNAL DEFAULTS], [Inertia Counter from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], maker row]."

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

## V-04 -- Combined: CTA Template + Lifecycle (C-22 + C-23)

**Axes**: CTA template + lifecycle emphasis -- Phase 2 gains a formal BINDING DECLARATION table at the top (C-23); CTA structural template changes to reference AUDIENCE BELIEF MAP for both placeholders (C-22); DEFAULTS inertia values are absorbed at Phase 2 fill time; traceability declaration updated to single-source. No inline provenance at individual citations (C-24 not targeted).

**Hypothesis**: V-01 passes C-22 (CTA all AUDIENCE BELIEF MAP) but fails C-23 (no top binding table). V-02 passes C-23 (top binding table) but fails C-22 (CTA still cites SIGNAL DEFAULTS). Combining both axes should pass C-22 and C-23 while failing C-24, scoring 99.41. The BINDING DECLARATION table shows where Inertia Excuse values originate (DEFAULTS); the CTA shows that Phase 5 reads only from AUDIENCE BELIEF MAP (which absorbed those values). The two structural elements create a complete, auditable DEFAULTS->BELIEF MAP->CTA chain readable from skill text alone. Predicted composite: 99.41 (C-22 PASS, C-23 PASS, C-24 FAIL).

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

**PHASE 2 BINDING DECLARATION** (read before filling the table):

The following SIGNAL DEFAULTS fields are bound to AUDIENCE BELIEF MAP columns. Binding applies before Phase 2 fill. Use Phase 1 active values (scout overrides if present; SIGNAL DEFAULTS otherwise).

| SIGNAL DEFAULTS field | Bound to | AUDIENCE BELIEF MAP column |
|----------------------|----------|---------------------------|
| Exec inertia | -> | Inertia Excuse, Exec row |
| Dev inertia | -> | Inertia Excuse, Dev row |
| Maker inertia | -> | Inertia Excuse, Maker row |

**These bindings transfer SIGNAL DEFAULTS inertia values into AUDIENCE BELIEF MAP at fill time. Phase 5 CTA construction reads from AUDIENCE BELIEF MAP, not from SIGNAL DEFAULTS directly.** AUDIENCE BELIEF MAP is the single authoritative source for Phase 5 CTA inertia slots.

For each audience, fill all four columns. Column definitions:

- **Core Belief**: The one thing this audience must believe before any other argument can land.
- **Failure Mode**: What the pitch *fails to achieve for this audience* if Core Belief is absent. Name a pitch outcome failure -- what the pitch cannot accomplish for this audience (e.g., "Exec won't authorize the demo slot," "Dev won't try the command," "Maker won't raise the question in their next meeting"). A restatement of Core Belief in negative form does not pass (e.g., "Exec won't believe the ROI argument" -- this restates the belief and is not a Failure Mode).
- **Inertia Excuse**: Fill from BINDING DECLARATION above. Use SIGNAL DEFAULTS active inertia row for this audience (or scout override). Template: `[active Exec inertia from SIGNAL DEFAULTS]` / `[active Dev inertia from SIGNAL DEFAULTS]` / `[active Maker inertia from SIGNAL DEFAULTS]`.
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
> "Instead of [Inertia Excuse from AUDIENCE BELIEF MAP, [audience] row], [Inertia Counter from AUDIENCE BELIEF MAP, [audience] row]."

Both placeholders draw from AUDIENCE BELIEF MAP (Phase 2 gate output, locked before Phase 5 begins):
- `[Inertia Excuse from AUDIENCE BELIEF MAP, [audience] row]` -- bound from SIGNAL DEFAULTS active inertia at Phase 2 fill time (per PHASE 2 BINDING DECLARATION).
- `[Inertia Counter from AUDIENCE BELIEF MAP, [audience] row]` -- pre-committed at Phase 2 fill time.

AUDIENCE BELIEF MAP is the single authoritative source for both CTA slots. SIGNAL DEFAULTS inertia values are accessible only through AUDIENCE BELIEF MAP after Phase 2 binds them. A CTA with either placeholder unfilled does not pass.

**Exec Version**
*Core Belief (from AUDIENCE BELIEF MAP, exec row).*

- **Hook**: EXEC OPENING SENTENCE (from Phase 4, locked, exact).
- **What It Does**: POSITIONING LOCK Outcome answer. One sentence.
- **Why It Matters**: POSITIONING LOCK Competitor named explicitly. "The alternative is not a competing product. It is [Competitor]." 2-3 sentences ROI framing.
- **Call to Action**: "Instead of [Inertia Excuse from AUDIENCE BELIEF MAP, exec row], [Inertia Counter from AUDIENCE BELIEF MAP, exec row]."

**Dev Version**
*Core Belief (from AUDIENCE BELIEF MAP, dev row).*

- **Hook**: A scenario the developer is in right now -- the moment before Signal changes what happens next.
- **What It Does**: At least one concrete interaction. Example: `/scout:requirements topic={topic}` produces `{topic}-requirements-{date}.md`. Reader answers "what would I actually type?"
- **Why It Matters**: Active Dev friction from SIGNAL DEFAULTS. Named directly.
- **Call to Action**: "Instead of [Inertia Excuse from AUDIENCE BELIEF MAP, dev row], [Inertia Counter from AUDIENCE BELIEF MAP, dev row]."

**Maker Version**
*Core Belief (from AUDIENCE BELIEF MAP, maker row).*

- **Hook**: The question they have already asked themselves. Zero unexplained acronyms. Zero namespace references. Zero CLI terminology.
- **What It Does**: Plain English. Translate every Signal term to what it does for a person.
- **Why It Matters**: Active Maker outcome from SIGNAL DEFAULTS. Connect to decision context.
- **Call to Action**: "Instead of [Inertia Excuse from AUDIENCE BELIEF MAP, maker row], [Inertia Counter from AUDIENCE BELIEF MAP, maker row]."

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

## V-05 -- Combined: All Axes (C-22 + C-23 + C-24 Full Synthesis)

**Axes**: CTA template + lifecycle emphasis + phrasing register -- Phase 2 gains a formal BINDING DECLARATION table at the top naming the DEFAULTS->BELIEF MAP column mapping (C-23); CTA structural template changes to reference AUDIENCE BELIEF MAP for both placeholders, making AUDIENCE BELIEF MAP the single authoritative CTA source (C-22); every Phase 5 gate-output citation carries an inline provenance parenthetical naming origin phase, output type, and lock confirmation (C-24); traceability declaration at Phase 5 CTA construction step reflects the single-source architecture.

**Hypothesis**: V-04 passes C-22 and C-23 but fails C-24 because the *Consumes* block names origin phases but individual citation lines within the version bodies do not confirm lock-before-execution or output type inline. Adding per-cite provenance in bracket notation throughout Phase 5 -- at *Consumes*, at each Hook/What/Why reference, and inside each CTA placeholder -- satisfies C-24's "at each gate-output citation" requirement. The result is a skill where SIGNAL DEFAULTS->AUDIENCE BELIEF MAP binding (C-23), CTA single-source architecture (C-22), and per-cite lock confirmation (C-24) are all inspectable from the skill text at three distinct structural locations. Predicted composite: 100 (Platinum).

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

**PHASE 2 BINDING DECLARATION** (read before filling the table):

The following SIGNAL DEFAULTS fields are bound to AUDIENCE BELIEF MAP columns. This declaration makes the full DEFAULTS->BELIEF MAP data flow auditable from skill structure alone.

| SIGNAL DEFAULTS field | Bound to | AUDIENCE BELIEF MAP column |
|----------------------|----------|---------------------------|
| Exec inertia | -> | Inertia Excuse, Exec row |
| Dev inertia | -> | Inertia Excuse, Dev row |
| Maker inertia | -> | Inertia Excuse, Maker row |

After binding, AUDIENCE BELIEF MAP is the authoritative source for all Phase 5 CTA inertia references. Phase 5 does not read SIGNAL DEFAULTS inertia fields directly.

For each audience, fill all four columns. Column definitions:

- **Core Belief**: The one thing this audience must believe before any other argument can land.
- **Failure Mode**: What the pitch *fails to achieve for this audience* if Core Belief is absent. Name a pitch outcome failure -- what the pitch cannot accomplish for this audience (e.g., "Exec won't authorize the demo slot," "Dev won't try the command," "Maker won't raise the question in their next meeting"). A restatement of Core Belief in negative form does not pass (e.g., "Exec won't believe the ROI argument" -- this restates the belief and is not a Failure Mode).
- **Inertia Excuse**: Fill from BINDING DECLARATION above. Template: `[active Exec inertia from SIGNAL DEFAULTS]` / `[active Dev inertia from SIGNAL DEFAULTS]` / `[active Maker inertia from SIGNAL DEFAULTS]`. Use scout override if available; otherwise use SIGNAL DEFAULTS value exactly.
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

*Consumes* (with provenance):
- **AUDIENCE BELIEF MAP** [Phase 2 gate output | named table | locked before Phase 5 begins]
- **POSITIONING LOCK** [Phase 3 gate output | named block | locked before Phase 5 begins]
- **EXEC OPENING SENTENCE** [Phase 4 gate output | named sentence | binary-gate verified | locked before Phase 5 begins]

Draft each version from the Core Belief in AUDIENCE BELIEF MAP. Use POSITIONING LOCK as the sole source for positioning claims.

**CTA construction template (all three versions)**:
> "Instead of [Inertia Excuse from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], [audience] row], [Inertia Counter from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], [audience] row]."

Both placeholders draw from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins]:
- `[Inertia Excuse from AUDIENCE BELIEF MAP, [audience] row]` -- Inertia Excuse cell, bound from SIGNAL DEFAULTS active inertia per PHASE 2 BINDING DECLARATION.
- `[Inertia Counter from AUDIENCE BELIEF MAP, [audience] row]` -- Inertia Counter cell, pre-committed at Phase 2 fill time.

AUDIENCE BELIEF MAP is the single authoritative source for both CTA slots. SIGNAL DEFAULTS inertia values were absorbed into AUDIENCE BELIEF MAP at Phase 2 via the BINDING DECLARATION; Phase 5 CTA does not cite SIGNAL DEFAULTS directly. A CTA with either placeholder unfilled does not pass.

**Exec Version**
*Core Belief (from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], exec row).*

- **Hook**: EXEC OPENING SENTENCE [Phase 4 gate output | binary-gate verified | locked before Phase 5 begins] -- use exact text, no edits.
- **What It Does**: POSITIONING LOCK [Phase 3 gate output | locked before Phase 5 begins] Outcome answer. One sentence.
- **Why It Matters**: POSITIONING LOCK [Phase 3 gate output | locked before Phase 5 begins] Competitor named explicitly. "The alternative is not a competing product. It is [Competitor]." 2-3 sentences ROI framing.
- **Call to Action**: "Instead of [Inertia Excuse from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], exec row], [Inertia Counter from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], exec row]."

**Dev Version**
*Core Belief (from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], dev row).*

- **Hook**: A scenario the developer is in right now -- the moment before Signal changes what happens next.
- **What It Does**: At least one concrete interaction. Example: `/scout:requirements topic={topic}` produces `{topic}-requirements-{date}.md`. Reader answers "what would I actually type?"
- **Why It Matters**: Active Dev friction from SIGNAL DEFAULTS. Named directly.
- **Call to Action**: "Instead of [Inertia Excuse from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], dev row], [Inertia Counter from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], dev row]."

**Maker Version**
*Core Belief (from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], maker row).*

- **Hook**: The question they have already asked themselves. Zero unexplained acronyms. Zero namespace references. Zero CLI terminology.
- **What It Does**: Plain English. Translate every Signal term to what it does for a person.
- **Why It Matters**: Active Maker outcome from SIGNAL DEFAULTS. Connect to decision context.
- **Call to Action**: "Instead of [Inertia Excuse from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], maker row], [Inertia Counter from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], maker row]."

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

## R6 Design Notes

**What changed from R5:**

R5 confirmed V-05 as Platinum (100/100) under v5 rubric. The R5 scorecard surfaced three excellence signals that became C-22/C-23/C-24 in the v6 rubric. Against v6, R5 V-05 retroscores 98.24: fails C-22 (CTA first placeholder cites SIGNAL DEFAULTS static block), fails C-23 (no top-of-Phase-2 binding declaration listing DEFAULTS->BELIEF MAP column pairings as an auditable map), fails C-24 (no inline provenance at individual Phase 5 gate-output citations -- the traceability declaration covers CTA construction step only, not each cite). R5 V-04 retroscores 99.41 against v6: passes C-22 (both CTA placeholders cite AUDIENCE BELIEF MAP), passes C-23 (DEFAULTS binding block at Phase 2 top with per-audience templates), fails C-24 (origin phase in *Consumes* line but no output type or lock confirmation at individual citation sites in version bodies).

**Retroactive R5 V-05 score under v6 rubric (denominator 17 aspirational):**

| Criterion | V-05 R5 Result | Evidence |
|-----------|---------------|----------|
| C-22 | FAIL | CTA first placeholder `[active [audience] inertia from SIGNAL DEFAULTS]` cites static block directly |
| C-23 | FAIL | Inertia Excuse column instruction has per-audience cell templates but no formal binding table at top of Phase 2 |
| C-24 | FAIL | Traceability declaration at CTA construction step names both source types but pass condition requires provenance at each individual gate-output citation |

```
R5 V-05 score under v6 = (4/4 * 60) + (3/3 * 30) + (14/17 * 10)
                        = 60 + 30 + 8.24
                        = 98.24
```

**Retroactive R5 V-04 score under v6 rubric:**

| Criterion | V-04 R5 Result | Evidence |
|-----------|---------------|----------|
| C-22 | PASS | CTA: both placeholders cite AUDIENCE BELIEF MAP |
| C-23 | PASS | DEFAULTS binding block at top of Phase 2 with per-audience cell templates |
| C-24 | FAIL | *Consumes* names origin phase but no output type or lock-before-execution confirmation at individual citation points |

```
R5 V-04 score under v6 = (4/4 * 60) + (3/3 * 30) + (16/17 * 10)
                        = 60 + 30 + 9.41
                        = 99.41
```

**Predicted R6 scores under v6 rubric:**

| Variation | C-22 | C-23 | C-24 | Aspirational | Composite |
|-----------|------|------|------|--------------|-----------|
| V-01 | PASS | FAIL | FAIL | 15/17 | 98.82 |
| V-02 | FAIL | PASS | FAIL | 15/17 | 98.82 |
| V-03 | FAIL | FAIL | PASS | 15/17 | 98.82 |
| V-04 | PASS | PASS | FAIL | 16/17 | 99.41 |
| V-05 | PASS | PASS | PASS | 17/17 | 100 |

**Diagnostic question for R6:** Does C-24's "at each gate-output citation" require provenance embedded inside the placeholder syntax itself (e.g., `[Inertia Counter from AUDIENCE BELIEF MAP [Phase 2 gate output], exec row]`) or is a provenance annotation at the instruction line level sufficient (e.g., a preceding bullet with `[Phase 2 gate output | type | locked]` notation)? V-03 uses inline bracket notation within each slot reference and at each instruction line. V-05 embeds provenance inside placeholder text itself. If C-24 requires provenance inside placeholder text, V-03 may pass partially and V-05 is the more robust form. The scorecard will resolve this.

**V-04 structural note:** V-04 is essentially R5 V-04 plus the enforcement text from the BINDING DECLARATION (the sentence "Phase 5 CTA construction reads from AUDIENCE BELIEF MAP, not from SIGNAL DEFAULTS directly"). R5 V-04 already passed C-22 and C-23; V-04 in this round clarifies the absorption language and confirms single-source CTA. The progression R5-V-04 -> R6-V-04 -> R6-V-05 is the cleanest incremental path to Platinum.

---

```json
{"context": "R6 targets C-22/C-23/C-24 from R5 excellence signals", "base_retroscores": {"R5-V-05": 98.24, "R5-V-04": 99.41}, "single_axis": ["V-01 (C-22: CTA all-AUDIENCE BELIEF MAP)", "V-02 (C-23: binding table at Phase 2 top)", "V-03 (C-24: inline provenance bracket notation at each Phase 5 cite)"], "combined": ["V-04 (C-22 + C-23)", "V-05 (C-22 + C-23 + C-24)"], "golden_candidate": "V-05", "diagnostic_question": "C-24: provenance inside placeholder syntax vs. at instruction-line level?"}
```
