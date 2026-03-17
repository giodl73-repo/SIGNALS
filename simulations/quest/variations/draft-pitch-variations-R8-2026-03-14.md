File written. Here's the summary of what was produced:

---

## draft-pitch — Variations R8

**Base**: R7 V-05 (100.0). BINDING DECLARATION in Phase 2 is inherited unchanged. R8 probes **Phase 5** — the first underspecified zone after the BINDING DECLARATION was fully closed in R7.

### Variation map

| ID | Axis | Change |
|----|------|--------|
| **V-01** | Inertia framing | INERTIA PROFILE pre-step: names arc (currently X → Signal changes to Y) for each audience before any version is drafted; "Why It Matters" required to cite it |
| **V-02** | Output format | VERSION DIFFERENTIATION GATE after all three drafts: 3-row table + 3 YES/NO gate questions; structural stop on convergence |
| **V-03** | Role sequence | Draft order Maker→Dev→Exec; EXEC OPENING SENTENCE gate (Phase 4) unchanged |
| **V-04** | V-01 + V-02 | INERTIA PROFILE + DIFFERENTIATION GATE; standard order |
| **V-05** | V-01 + V-02 + V-03 | Full synthesis: Maker-first + INERTIA PROFILE + DIFFERENTIATION GATE |

### Three open Phase 5 gaps being probed

| Gap | Current state |
|-----|--------------|
| Inertia traceability | Inertia lands in CTA only; Why-It-Matters sections are independent arguments |
| Version differentiation | No post-draft check; three versions can converge semantically |
| Draft sequence | Always Exec-first; jargon constraint applied last instead of first |

### Structural parallel to R7

V-05 mirrors the BINDING DECLARATION pattern: name the data flow before filling (INERTIA PROFILE), fill in constraint-ascending order (Maker→Dev→Exec), declare closure (DIFFERENTIATION GATE). This is the same pre-commit → fill → close structure that made the BINDING DECLARATION auditable. If the v8 rubric surfaces these as scorable properties, V-05 is the golden candidate.
st. Maker-first forces the jargon constraint (zero unexplained acronyms, zero CLI) to shape the message before exec vocabulary is added.

| Variation | Draft Order | Phase 5 Pre-step | Post-draft Gate |
|-----------|-------------|------------------|-----------------|
| V-01 | Exec→Dev→Maker | INERTIA PROFILE | (none) |
| V-02 | Exec→Dev→Maker | (none) | DIFFERENTIATION GATE |
| V-03 | Maker→Dev→Exec | (none) | (none) |
| V-04 | Exec→Dev→Maker | INERTIA PROFILE | DIFFERENTIATION GATE |
| V-05 | Maker→Dev→Exec | INERTIA PROFILE | DIFFERENTIATION GATE |

**Diagnostic questions for R8:**
1. Does naming the inertia pattern explicitly before drafting produce stronger Why-It-Matters sections, or does it overconstraint the prose?
2. Is a VERSION DIFFERENTIATION GATE enforceable by the skill, or does it generate false passes (superficial vocabulary swaps that still converge semantically)?
3. Does Maker-first draft order actually improve Core Belief clarity, or does the EXEC OPENING GATE in Phase 4 already anchor the message sufficiently?

---

## V-01 -- Single Axis: Inertia Framing

**Axis**: Inertia framing -- Phase 5 gains an INERTIA PROFILE pre-step that names the inertia arc (currently X → Signal changes to Y) for each audience before any version is drafted. Each "Why It Matters" section is required to reference the named inertia arc.

**Hypothesis**: Currently inertia framing lands primarily in the CTA. "Why It Matters" for Exec cites POSITIONING LOCK Competitor; for Dev cites active Dev friction; for Maker cites active Maker outcome. None of these explicitly connect to the inertia arc the CTA resolves. Adding an INERTIA PROFILE pre-step -- named, pre-committed, cited by name in each Why It Matters bullet -- forces Hook → Why → CTA to form a single inertia arc per audience rather than two parallel arguments. This is the same structural pattern that made the BINDING DECLARATION effective: naming the data flow before consuming it. Predicted composite: TBD.

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

This declaration makes the full DEFAULTS->BELIEF MAP data flow auditable from skill structure alone.

The following SIGNAL DEFAULTS fields are bound to AUDIENCE BELIEF MAP columns. This binding applies before any row is filled. Use Phase 1 active values (scout overrides if present; SIGNAL DEFAULTS otherwise).

| SIGNAL DEFAULTS field | Bound to | AUDIENCE BELIEF MAP column |
|----------------------|----------|---------------------------|
| Exec inertia | -> | Inertia Excuse, Exec row |
| Dev inertia | -> | Inertia Excuse, Dev row |
| Maker inertia | -> | Inertia Excuse, Maker row |

No other DEFAULTS fields are directly bound to BELIEF MAP columns. Core Belief, Failure Mode, and Inertia Counter are generated, not bound from DEFAULTS.

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

**Phase 5 INERTIA PROFILE** (complete before drafting any version):

State the inertia arc for each audience in one sentence using this template:
"[Audience] currently [Inertia Excuse from AUDIENCE BELIEF MAP [Phase 2 gate output], [audience] row]. Signal changes this to [Inertia Counter from AUDIENCE BELIEF MAP [Phase 2 gate output], [audience] row]."

**INERTIA PROFILE:**
- Exec: [Write one sentence: currently X, Signal changes to Y]
- Dev: [Write one sentence: currently X, Signal changes to Y]
- Maker: [Write one sentence: currently X, Signal changes to Y]

Each "Why It Matters" section below must reflect the inertia arc stated in the INERTIA PROFILE -- not a separate argument.

**-- INERTIA PROFILE COMPLETE. Do not draft any version until all three sentences are written. --**

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
- **Why It Matters**: Name the inertia arc from INERTIA PROFILE Exec sentence. "The alternative is not a competing product. It is [Competitor from POSITIONING LOCK [Phase 3 gate output]]." 2-3 sentences ROI framing grounded in the inertia arc.
- **Call to Action**: "Instead of [Inertia Excuse from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], exec row], [Inertia Counter from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], exec row]."

**Dev Version**
*Core Belief (from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], dev row).*

- **Hook**: A scenario the developer is in right now -- the moment before Signal changes what happens next.
- **What It Does**: At least one concrete interaction. Example: `/scout:requirements topic={topic}` produces `{topic}-requirements-{date}.md`. Reader answers "what would I actually type?"
- **Why It Matters**: Name the inertia arc from INERTIA PROFILE Dev sentence. Show the before-state (Inertia Excuse) and the after-state (Inertia Counter). Active Dev friction from SIGNAL DEFAULTS named directly within this arc.
- **Call to Action**: "Instead of [Inertia Excuse from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], dev row], [Inertia Counter from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], dev row]."

**Maker Version**
*Core Belief (from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], maker row).*

- **Hook**: The question they have already asked themselves. Zero unexplained acronyms. Zero namespace references. Zero CLI terminology.
- **What It Does**: Plain English. Translate every Signal term to what it does for a person.
- **Why It Matters**: Name the inertia arc from INERTIA PROFILE Maker sentence in plain language. Active Maker outcome from SIGNAL DEFAULTS. Connect to decision context. No jargon.
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

All phase outputs (active values, AUDIENCE BELIEF MAP, POSITIONING LOCK, EXEC OPENING SENTENCE, INERTIA PROFILE, proof audit) are working notes -- not in saved artifact.

**Save to**: `simulations/draft/pitches/{topic}-pitch-{date}.md`

---

## V-02 -- Single Axis: Output Format (Version Differentiation Gate)

**Axis**: Output format -- Phase 5 gains a VERSION DIFFERENTIATION GATE after all three versions are drafted. The gate checks: Core Beliefs are substantively distinct (not paraphrases), Maker version contains zero unexplained acronyms or CLI references, Dev version opens with a scenario (not an outcome statement).

**Hypothesis**: The current skill instructs audience-specific drafting but has no verification step. "Zero unexplained acronyms" and "show the tool, not the business case" are advisory. A post-draft gate that fills a 3-row table (Core Belief summary | Hook type | Jargon check) and applies explicit YES/NO questions turns these instructions into a checkable boundary. Without this gate, the three versions can converge semantically while appearing differentiated by surface vocabulary. The gate does not prescribe prose -- it names the structural properties that must be present before the phase is complete. Predicted composite: TBD.

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

This declaration makes the full DEFAULTS->BELIEF MAP data flow auditable from skill structure alone.

The following SIGNAL DEFAULTS fields are bound to AUDIENCE BELIEF MAP columns. This binding applies before any row is filled. Use Phase 1 active values (scout overrides if present; SIGNAL DEFAULTS otherwise).

| SIGNAL DEFAULTS field | Bound to | AUDIENCE BELIEF MAP column |
|----------------------|----------|---------------------------|
| Exec inertia | -> | Inertia Excuse, Exec row |
| Dev inertia | -> | Inertia Excuse, Dev row |
| Maker inertia | -> | Inertia Excuse, Maker row |

No other DEFAULTS fields are directly bound to BELIEF MAP columns. Core Belief, Failure Mode, and Inertia Counter are generated, not bound from DEFAULTS.

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

**VERSION DIFFERENTIATION GATE** (complete after all three versions are drafted):

Fill this table from the drafts above:

| Version | Core Belief summary (10 words max) | Hook type | Jargon check |
|---------|------------------------------------|-----------|--------------|
| Exec | [summarize] | outcome/cost/risk sentence | business framing only |
| Dev | [summarize] | scenario/moment | technical terms permitted |
| Maker | [summarize] | question/feeling | zero unexplained acronyms |

Gate questions -- answer each before proceeding:
1. Are the three Core Belief summaries substantively distinct (not paraphrases of each other)? YES / NO
2. Does the Maker version contain any unexplained acronym or CLI reference (e.g., `/scout:`, `{topic}`, namespace names)? YES / NO
3. Does the Dev version open with a scenario (a moment the developer is in) rather than an outcome statement? YES / NO

Passing state: Q1=YES, Q2=NO, Q3=YES.
- Any gate NOT in passing state: rewrite the failing version. Re-fill the table. Re-answer all three questions. Repeat until passing state reached.

**-- VERSION DIFFERENTIATION GATE COMPLETE. Proceed to Phase 6 only when all gates pass. --**

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

All phase outputs (active values, AUDIENCE BELIEF MAP, POSITIONING LOCK, EXEC OPENING SENTENCE, differentiation gate table, proof audit) are working notes -- not in saved artifact.

**Save to**: `simulations/draft/pitches/{topic}-pitch-{date}.md`

---

## V-03 -- Single Axis: Role Sequence (Maker First)

**Axis**: Role sequence -- Phase 5 draft order changes from Exec→Dev→Maker to Maker→Dev→Exec. EXEC OPENING SENTENCE gate (Phase 4) is unchanged -- it still produces the locked sentence before Phase 5 begins. Only the order in which the three versions are written changes.

**Hypothesis**: The skill always drafts the most constrained version last (Maker: zero jargon, zero CLI, plain English). Drafting Maker first forces the Core Belief to be expressed without technical scaffolding before the more permissive Dev and Exec versions are written. This is the same principle as writing the simplest test case first: if you can't say it plainly, the message isn't clear yet. Drafting Exec last does not weaken it -- EXEC OPENING SENTENCE is pre-committed at Phase 4 and the exec Hook uses it by exact reference regardless of draft order. Predicted composite: TBD.

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

This declaration makes the full DEFAULTS->BELIEF MAP data flow auditable from skill structure alone.

The following SIGNAL DEFAULTS fields are bound to AUDIENCE BELIEF MAP columns. This binding applies before any row is filled. Use Phase 1 active values (scout overrides if present; SIGNAL DEFAULTS otherwise).

| SIGNAL DEFAULTS field | Bound to | AUDIENCE BELIEF MAP column |
|----------------------|----------|---------------------------|
| Exec inertia | -> | Inertia Excuse, Exec row |
| Dev inertia | -> | Inertia Excuse, Dev row |
| Maker inertia | -> | Inertia Excuse, Maker row |

No other DEFAULTS fields are directly bound to BELIEF MAP columns. Core Belief, Failure Mode, and Inertia Counter are generated, not bound from DEFAULTS.

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

Draft each version from the Core Belief in AUDIENCE BELIEF MAP. Use POSITIONING LOCK as the sole source for positioning claims. Draft order: Maker first, then Dev, then Exec.

**CTA construction template (all three versions)**:
> "Instead of [Inertia Excuse from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], [audience] row], [Inertia Counter from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], [audience] row]."

Both placeholders draw from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins]:
- `[Inertia Excuse from AUDIENCE BELIEF MAP, [audience] row]` -- Inertia Excuse cell, bound from SIGNAL DEFAULTS active inertia per PHASE 2 BINDING DECLARATION.
- `[Inertia Counter from AUDIENCE BELIEF MAP, [audience] row]` -- Inertia Counter cell, pre-committed at Phase 2 fill time.

AUDIENCE BELIEF MAP is the single authoritative source for both CTA slots. SIGNAL DEFAULTS inertia values were absorbed into AUDIENCE BELIEF MAP at Phase 2 via the BINDING DECLARATION; Phase 5 CTA does not cite SIGNAL DEFAULTS directly. A CTA with either placeholder unfilled does not pass.

**Maker Version** *(draft first)*
*Core Belief (from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], maker row).*

- **Hook**: The question they have already asked themselves. Zero unexplained acronyms. Zero namespace references. Zero CLI terminology.
- **What It Does**: Plain English. Translate every Signal term to what it does for a person.
- **Why It Matters**: Active Maker outcome from SIGNAL DEFAULTS. Connect to decision context.
- **Call to Action**: "Instead of [Inertia Excuse from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], maker row], [Inertia Counter from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], maker row]."

**Dev Version** *(draft second)*
*Core Belief (from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], dev row).*

- **Hook**: A scenario the developer is in right now -- the moment before Signal changes what happens next.
- **What It Does**: At least one concrete interaction. Example: `/scout:requirements topic={topic}` produces `{topic}-requirements-{date}.md`. Reader answers "what would I actually type?"
- **Why It Matters**: Active Dev friction from SIGNAL DEFAULTS. Named directly.
- **Call to Action**: "Instead of [Inertia Excuse from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], dev row], [Inertia Counter from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], dev row]."

**Exec Version** *(draft last)*
*Core Belief (from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], exec row).*

- **Hook**: EXEC OPENING SENTENCE [Phase 4 gate output | binary-gate verified | locked before Phase 5 begins] -- use exact text, no edits.
- **What It Does**: POSITIONING LOCK [Phase 3 gate output | locked before Phase 5 begins] Outcome answer. One sentence.
- **Why It Matters**: POSITIONING LOCK [Phase 3 gate output | locked before Phase 5 begins] Competitor named explicitly. "The alternative is not a competing product. It is [Competitor]." 2-3 sentences ROI framing.
- **Call to Action**: "Instead of [Inertia Excuse from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], exec row], [Inertia Counter from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], exec row]."

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

## V-04 -- Combined: V-01 + V-02 (Inertia Framing + Differentiation Gate)

**Axes**: Inertia framing + Output format -- Phase 5 gains the INERTIA PROFILE pre-step (V-01) and the VERSION DIFFERENTIATION GATE post-step (V-02). Draft order remains Exec→Dev→Maker. This is the two-axis combination without the Maker-first reorder.

**Hypothesis**: INERTIA PROFILE forces the inertia arc into Why-It-Matters sections before drafting. VERSION DIFFERENTIATION GATE verifies the three versions are substantively distinct after drafting. Together they address the two weakest enforcement points in Phase 5: upstream (inertia traceability) and downstream (differentiation). The combination does not introduce tension -- INERTIA PROFILE names the arc before drafts begin; the DIFFERENTIATION GATE checks structural properties after drafts complete. Predicted composite: TBD.

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

This declaration makes the full DEFAULTS->BELIEF MAP data flow auditable from skill structure alone.

The following SIGNAL DEFAULTS fields are bound to AUDIENCE BELIEF MAP columns. This binding applies before any row is filled. Use Phase 1 active values (scout overrides if present; SIGNAL DEFAULTS otherwise).

| SIGNAL DEFAULTS field | Bound to | AUDIENCE BELIEF MAP column |
|----------------------|----------|---------------------------|
| Exec inertia | -> | Inertia Excuse, Exec row |
| Dev inertia | -> | Inertia Excuse, Dev row |
| Maker inertia | -> | Inertia Excuse, Maker row |

No other DEFAULTS fields are directly bound to BELIEF MAP columns. Core Belief, Failure Mode, and Inertia Counter are generated, not bound from DEFAULTS.

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

**Phase 5 INERTIA PROFILE** (complete before drafting any version):

State the inertia arc for each audience in one sentence using this template:
"[Audience] currently [Inertia Excuse from AUDIENCE BELIEF MAP [Phase 2 gate output], [audience] row]. Signal changes this to [Inertia Counter from AUDIENCE BELIEF MAP [Phase 2 gate output], [audience] row]."

**INERTIA PROFILE:**
- Exec: [Write one sentence: currently X, Signal changes to Y]
- Dev: [Write one sentence: currently X, Signal changes to Y]
- Maker: [Write one sentence: currently X, Signal changes to Y]

Each "Why It Matters" section below must reflect the inertia arc stated in the INERTIA PROFILE -- not a separate argument.

**-- INERTIA PROFILE COMPLETE. Do not draft any version until all three sentences are written. --**

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
- **Why It Matters**: Name the inertia arc from INERTIA PROFILE Exec sentence. "The alternative is not a competing product. It is [Competitor from POSITIONING LOCK [Phase 3 gate output]]." 2-3 sentences ROI framing grounded in the inertia arc.
- **Call to Action**: "Instead of [Inertia Excuse from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], exec row], [Inertia Counter from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], exec row]."

**Dev Version**
*Core Belief (from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], dev row).*

- **Hook**: A scenario the developer is in right now -- the moment before Signal changes what happens next.
- **What It Does**: At least one concrete interaction. Example: `/scout:requirements topic={topic}` produces `{topic}-requirements-{date}.md`. Reader answers "what would I actually type?"
- **Why It Matters**: Name the inertia arc from INERTIA PROFILE Dev sentence. Show the before-state (Inertia Excuse) and the after-state (Inertia Counter). Active Dev friction from SIGNAL DEFAULTS named directly within this arc.
- **Call to Action**: "Instead of [Inertia Excuse from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], dev row], [Inertia Counter from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], dev row]."

**Maker Version**
*Core Belief (from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], maker row).*

- **Hook**: The question they have already asked themselves. Zero unexplained acronyms. Zero namespace references. Zero CLI terminology.
- **What It Does**: Plain English. Translate every Signal term to what it does for a person.
- **Why It Matters**: Name the inertia arc from INERTIA PROFILE Maker sentence in plain language. Active Maker outcome from SIGNAL DEFAULTS. Connect to decision context. No jargon.
- **Call to Action**: "Instead of [Inertia Excuse from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], maker row], [Inertia Counter from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], maker row]."

**VERSION DIFFERENTIATION GATE** (complete after all three versions are drafted):

Fill this table from the drafts above:

| Version | Core Belief summary (10 words max) | Hook type | Jargon check |
|---------|------------------------------------|-----------|--------------|
| Exec | [summarize] | outcome/cost/risk sentence | business framing only |
| Dev | [summarize] | scenario/moment | technical terms permitted |
| Maker | [summarize] | question/feeling | zero unexplained acronyms |

Gate questions -- answer each before proceeding:
1. Are the three Core Belief summaries substantively distinct (not paraphrases of each other)? YES / NO
2. Does the Maker version contain any unexplained acronym or CLI reference (e.g., `/scout:`, `{topic}`, namespace names)? YES / NO
3. Does the Dev version open with a scenario (a moment the developer is in) rather than an outcome statement? YES / NO

Passing state: Q1=YES, Q2=NO, Q3=YES.
- Any gate NOT in passing state: rewrite the failing version. Re-fill the table. Re-answer all three questions. Repeat until passing state reached.

**-- VERSION DIFFERENTIATION GATE COMPLETE. Proceed to Phase 6 only when all gates pass. --**

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

All phase outputs (active values, AUDIENCE BELIEF MAP, POSITIONING LOCK, EXEC OPENING SENTENCE, INERTIA PROFILE, differentiation gate table, proof audit) are working notes -- not in saved artifact.

**Save to**: `simulations/draft/pitches/{topic}-pitch-{date}.md`

---

## V-05 -- Combined: All Axes (Maker First + Inertia Framing + Differentiation Gate)

**Axes**: Role sequence + Inertia framing + Output format -- Phase 5 drafts Maker first, uses INERTIA PROFILE before drafting, and applies the VERSION DIFFERENTIATION GATE after all three versions are complete. This is the R8 golden candidate.

**Hypothesis**: The three axes reinforce each other in a single structural pattern: name the constraint before drafting (INERTIA PROFILE), draft in constraint-ascending order so the hardest constraint shapes the message first (Maker→Dev→Exec), then verify constraint compliance at exit (DIFFERENTIATION GATE). Each axis addresses a different failure mode in Phase 5: INERTIA PROFILE prevents inertia from being CTA-only; Maker-first prevents jargon-scaffold from dominating the message; DIFFERENTIATION GATE prevents semantic convergence from passing as differentiation. Together they close the three open enforcement gaps in Phase 5 that R7 V-05 left unaddressed. Predicted composite: TBD.

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

**PHASE 2 BINDING DECLARATION** (read before filling the table):

This declaration makes the full DEFAULTS->BELIEF MAP data flow auditable from skill structure alone.

The following SIGNAL DEFAULTS fields are bound to AUDIENCE BELIEF MAP columns. This binding applies before any row is filled. Use Phase 1 active values (scout overrides if present; SIGNAL DEFAULTS otherwise).

| SIGNAL DEFAULTS field | Bound to | AUDIENCE BELIEF MAP column |
|----------------------|----------|---------------------------|
| Exec inertia | -> | Inertia Excuse, Exec row |
| Dev inertia | -> | Inertia Excuse, Dev row |
| Maker inertia | -> | Inertia Excuse, Maker row |

No other DEFAULTS fields are directly bound to BELIEF MAP columns. Core Belief, Failure Mode, and Inertia Counter are generated, not bound from DEFAULTS.

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

**Phase 5 INERTIA PROFILE** (complete before drafting any version):

State the inertia arc for each audience in one sentence using this template:
"[Audience] currently [Inertia Excuse from AUDIENCE BELIEF MAP [Phase 2 gate output], [audience] row]. Signal changes this to [Inertia Counter from AUDIENCE BELIEF MAP [Phase 2 gate output], [audience] row]."

**INERTIA PROFILE:**
- Exec: [Write one sentence: currently X, Signal changes to Y]
- Dev: [Write one sentence: currently X, Signal changes to Y]
- Maker: [Write one sentence: currently X, Signal changes to Y]

Each "Why It Matters" section below must reflect the inertia arc stated in the INERTIA PROFILE -- not a separate argument.

**-- INERTIA PROFILE COMPLETE. Do not draft any version until all three sentences are written. --**

Draft each version from the Core Belief in AUDIENCE BELIEF MAP. Use POSITIONING LOCK as the sole source for positioning claims. Draft order: Maker first, then Dev, then Exec.

**CTA construction template (all three versions)**:
> "Instead of [Inertia Excuse from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], [audience] row], [Inertia Counter from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], [audience] row]."

Both placeholders draw from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins]:
- `[Inertia Excuse from AUDIENCE BELIEF MAP, [audience] row]` -- Inertia Excuse cell, bound from SIGNAL DEFAULTS active inertia per PHASE 2 BINDING DECLARATION.
- `[Inertia Counter from AUDIENCE BELIEF MAP, [audience] row]` -- Inertia Counter cell, pre-committed at Phase 2 fill time.

AUDIENCE BELIEF MAP is the single authoritative source for both CTA slots. SIGNAL DEFAULTS inertia values were absorbed into AUDIENCE BELIEF MAP at Phase 2 via the BINDING DECLARATION; Phase 5 CTA does not cite SIGNAL DEFAULTS directly. A CTA with either placeholder unfilled does not pass.

**Maker Version** *(draft first)*
*Core Belief (from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], maker row).*

- **Hook**: The question they have already asked themselves. Zero unexplained acronyms. Zero namespace references. Zero CLI terminology.
- **What It Does**: Plain English. Translate every Signal term to what it does for a person.
- **Why It Matters**: Name the inertia arc from INERTIA PROFILE Maker sentence in plain language. Active Maker outcome from SIGNAL DEFAULTS. Connect to decision context. No jargon.
- **Call to Action**: "Instead of [Inertia Excuse from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], maker row], [Inertia Counter from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], maker row]."

**Dev Version** *(draft second)*
*Core Belief (from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], dev row).*

- **Hook**: A scenario the developer is in right now -- the moment before Signal changes what happens next.
- **What It Does**: At least one concrete interaction. Example: `/scout:requirements topic={topic}` produces `{topic}-requirements-{date}.md`. Reader answers "what would I actually type?"
- **Why It Matters**: Name the inertia arc from INERTIA PROFILE Dev sentence. Show the before-state (Inertia Excuse) and the after-state (Inertia Counter). Active Dev friction from SIGNAL DEFAULTS named directly within this arc.
- **Call to Action**: "Instead of [Inertia Excuse from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], dev row], [Inertia Counter from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], dev row]."

**Exec Version** *(draft last)*
*Core Belief (from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], exec row).*

- **Hook**: EXEC OPENING SENTENCE [Phase 4 gate output | binary-gate verified | locked before Phase 5 begins] -- use exact text, no edits.
- **What It Does**: POSITIONING LOCK [Phase 3 gate output | locked before Phase 5 begins] Outcome answer. One sentence.
- **Why It Matters**: Name the inertia arc from INERTIA PROFILE Exec sentence. "The alternative is not a competing product. It is [Competitor from POSITIONING LOCK [Phase 3 gate output]]." 2-3 sentences ROI framing grounded in the inertia arc.
- **Call to Action**: "Instead of [Inertia Excuse from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], exec row], [Inertia Counter from AUDIENCE BELIEF MAP [Phase 2 gate output, locked before Phase 5 begins], exec row]."

**VERSION DIFFERENTIATION GATE** (complete after all three versions are drafted):

Fill this table from the drafts above:

| Version | Core Belief summary (10 words max) | Hook type | Jargon check |
|---------|------------------------------------|-----------|--------------|
| Exec | [summarize] | outcome/cost/risk sentence | business framing only |
| Dev | [summarize] | scenario/moment | technical terms permitted |
| Maker | [summarize] | question/feeling | zero unexplained acronyms |

Gate questions -- answer each before proceeding:
1. Are the three Core Belief summaries substantively distinct (not paraphrases of each other)? YES / NO
2. Does the Maker version contain any unexplained acronym or CLI reference (e.g., `/scout:`, `{topic}`, namespace names)? YES / NO
3. Does the Dev version open with a scenario (a moment the developer is in) rather than an outcome statement? YES / NO

Passing state: Q1=YES, Q2=NO, Q3=YES.
- Any gate NOT in passing state: rewrite the failing version. Re-fill the table. Re-answer all three questions. Repeat until passing state reached.

**-- VERSION DIFFERENTIATION GATE COMPLETE. Proceed to Phase 6 only when all gates pass. --**

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

All phase outputs (active values, AUDIENCE BELIEF MAP, POSITIONING LOCK, EXEC OPENING SENTENCE, INERTIA PROFILE, differentiation gate table, proof audit) are working notes -- not in saved artifact.

**Save to**: `simulations/draft/pitches/{topic}-pitch-{date}.md`

---

## R8 Design Notes

**What changed from R7:**

R7 closed the BINDING DECLARATION in Phase 2 completely (C-25/C-26/C-27 all pass at 100.0). R8 base is R7 V-05 unchanged. R8 variations probe Phase 5 -- the full draft phase -- which remains underspecified after R7: inertia lands in the CTA but not consistently in Why-It-Matters; no gate verifies the three versions are substantively distinct; no structural reason forces the message to be expressed jargon-free before exec framing is added.

**Three open Phase 5 enforcement gaps identified:**

| Gap | Current state | R8 variation |
|-----|--------------|--------------|
| Inertia traceability | Inertia in CTA only; Why-It-Matters sections are independent arguments | V-01: INERTIA PROFILE forces arc into Why-It-Matters |
| Version differentiation | No post-draft check; convergence is advisory violation only | V-02: DIFFERENTIATION GATE makes convergence a structural stop |
| Draft sequence | Always Exec-first; jargon-constraint (Maker) applied last | V-03: Maker-first forces plain-language clarity before exec framing |

**Predicted structural effect of V-05:**

V-05 is the first variation where Phase 5 has a named pre-step (INERTIA PROFILE), a constraint-ascending draft order (Maker→Dev→Exec), and a named post-step (DIFFERENTIATION GATE). This mirrors the Phase 2 BINDING DECLARATION pattern: name the data flow before filling the table (INERTIA PROFILE = binding declaration for Phase 5), fill in constraint order, declare closure (DIFFERENTIATION GATE = exhaustiveness check for Phase 5). If the rubric surfaces these as scorable properties, V-05 would be the first variation to pass them. Predicted composite: TBD -- dependent on v8 rubric criteria not yet written.
