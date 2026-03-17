---

## draft-pitch — Variations R7

**R6 V-05 retrograde score under v7: 99.5** — fails only C-25 (no exhaustiveness scope-closure in the BINDING DECLARATION).

---

### Variation map

| ID | Axis | Hypothesis | Predicted |
|----|------|-----------|-----------|
| **V-01** | Lifecycle emphasis — C-25 only | Adds "No other DEFAULTS fields are directly bound to BELIEF MAP columns." after binding table; C-26/C-27 absent | 99.0 |
| **V-02** | Lifecycle emphasis — C-26 only | Adds Phase 5 access prohibition ("Phase 5 does not read SIGNAL DEFAULTS inertia fields directly."); C-25/C-27 absent | 99.0 |
| **V-03** | Lifecycle emphasis — C-27 only | Promotes meta-purpose to leading sentence before the binding table; C-25/C-26 absent | 99.0 |
| **V-04** | C-25 + C-26 | Exhaustiveness closure + Phase 5 prohibition; no meta-purpose | 99.5 |
| **V-05** | C-25 + C-26 + C-27 | Full synthesis: meta-purpose leads → table → exhaustiveness → prohibition | **100** |

---

### What's varying

The **only** structural change across all five variations is the BINDING DECLARATION in Phase 2. Everything else — SIGNAL DEFAULTS, Phases 1/3/4/5/6/7, CTA template, provenance bracket notation — is identical across all five and inherits from R6 V-05.

The BINDING DECLARATION structure by variation:

| Variation | Opening | Table | Post-table |
|-----------|---------|-------|------------|
| V-01 | binding intro | 3-row | exhaustiveness only (C-25) |
| V-02 | binding intro | 3-row | prohibition only (C-26) |
| V-03 | **meta-purpose** + binding intro | 3-row | *(none)* |
| V-04 | binding intro | 3-row | exhaustiveness (C-25) + prohibition (C-26) |
| V-05 | **meta-purpose** + binding intro | 3-row | exhaustiveness (C-25) + prohibition (C-26) |

**Diagnostic question**: C-27 requires the meta-purpose statement "at the site of the declaration." R6 V-05 had it as a trailing clause in the opening sentence and passed C-27. R7 V-03/V-05 promote it to a standalone leading sentence before the binding intro. If the scorecard rules that C-27 requires identifiable leading placement (not a trailing clause), V-03/V-05 would be stronger; if a trailing clause passes, V-03/V-05 are equivalent to R6 V-05 on C-27 and the only new delta is C-25.
e provenance at all Phase 5 gate-output citations |
| C-25 | **FAIL** | No exhaustiveness clause. No sentence declaring the binding set complete. |
| C-26 | PASS | "Phase 5 does not read SIGNAL DEFAULTS inertia fields directly." Names Phase 5, explicit prohibition. |
| C-27 | PASS | "This declaration makes the full DEFAULTS->BELIEF MAP data flow auditable from skill structure alone." |

```
R6 V-05 score under v7 = (4/4 * 60) + (3/3 * 30) + (19/20 * 10)
                        = 60 + 30 + 9.5
                        = 99.5
```

**R7 base** (used for all single-axis variations): R6 V-05 with BINDING DECLARATION stripped to C-23 only — formal table at top of Phase 2, no exhaustiveness statement, no Phase 5 prohibition, no meta-purpose. Base retroscore: 60 + 30 + (17/20)*10 = 98.5.

**Predicted R7 scores under v7 rubric:**

| Variation | C-25 | C-26 | C-27 | Aspirational | Composite |
|-----------|------|------|------|--------------|-----------|
| V-01 | PASS | FAIL | FAIL | 18/20 | 99.0 |
| V-02 | FAIL | PASS | FAIL | 18/20 | 99.0 |
| V-03 | FAIL | FAIL | PASS | 18/20 | 99.0 |
| V-04 | PASS | PASS | FAIL | 19/20 | 99.5 |
| V-05 | PASS | PASS | PASS | 20/20 | 100 |

---

## V-01 — Single Axis: Lifecycle Emphasis (C-25 Target)

**Axis**: Lifecycle emphasis — BINDING DECLARATION adds one exhaustiveness scope-closure sentence after the binding table: "No other DEFAULTS fields are directly bound to BELIEF MAP columns." The declaration set is now declared complete, not just enumerated. C-26 and C-27 are intentionally absent.

**Hypothesis**: C-25 requires the binding declaration to declare completeness — not just which fields are bound but that no others are. R6 V-05 omits this. Adding a single closing sentence after the binding table should pass C-25 without touching C-26 or C-27. Predicted composite: 99.0 (C-25 PASS, C-26 FAIL, C-27 FAIL).

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

## V-02 -- Single Axis: Lifecycle Emphasis (C-26 Target)

**Axis**: Lifecycle emphasis -- BINDING DECLARATION adds an explicit downstream access prohibition naming Phase 5 as the consuming step: "After binding, AUDIENCE BELIEF MAP is the authoritative source for all Phase 5 CTA inertia references. Phase 5 does not read SIGNAL DEFAULTS inertia fields directly." No exhaustiveness closure (C-25 intentionally absent). No meta-purpose statement (C-27 intentionally absent).

**Hypothesis**: C-26 requires naming Phase 5 as the consuming step AND explicitly forbidding direct DEFAULTS access. R6 V-02 passed C-25 without C-26 (had exhaustiveness but no prohibition). This variation confirms whether the prohibition alone passes C-26. Predicted composite: 99.0 (C-25 FAIL, C-26 PASS, C-27 FAIL).

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

## V-03 -- Single Axis: Lifecycle Emphasis (C-27 Target)

**Axis**: Lifecycle emphasis -- BINDING DECLARATION opens with a meta-purpose statement: "This declaration makes the full DEFAULTS->BELIEF MAP data flow auditable from skill structure alone." This leads the declaration before the binding table. No exhaustiveness closure (C-25 intentionally absent). No Phase 5 access prohibition (C-26 intentionally absent).

**Hypothesis**: C-27 requires the meta-purpose statement to appear at the site of the declaration -- making auditability intent declarative. Promoting it to the opening line of the BINDING DECLARATION (before the table) satisfies "at the site of the declaration." C-25 and C-26 are absent, confirming that the meta-purpose alone cannot carry the other two. Predicted composite: 99.0 (C-25 FAIL, C-26 FAIL, C-27 PASS).

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

## V-04 -- Combined: C-25 + C-26 (Exhaustiveness + Prohibition)

**Axes**: Lifecycle emphasis -- BINDING DECLARATION combines exhaustiveness scope-closure (C-25) with Phase 5 access prohibition (C-26). No meta-purpose statement (C-27 intentionally absent). Structurally equivalent to R6 V-05 minus meta-purpose, plus C-25.

**Hypothesis**: V-01 passes C-25 alone; V-02 passes C-26 alone. Combining them should pass both without needing meta-purpose. V-04 represents the minimal form that closes all bypass paths: the binding set is declared complete (C-25) and Phase 5 is explicitly prohibited from reading DEFAULTS directly (C-26). Meta-purpose (C-27) adds readability but is not required for auditable closure. Predicted composite: 99.5 (C-25 PASS, C-26 PASS, C-27 FAIL).

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

## V-05 -- Combined: All Axes (C-25 + C-26 + C-27 Full Synthesis)

**Axes**: Lifecycle emphasis -- BINDING DECLARATION gains all three elements: meta-purpose statement leading the declaration (C-27), exhaustiveness scope-closure after the binding table (C-25), and Phase 5 access prohibition closing the declaration (C-26). The declaration is now self-describing (C-27), set-complete (C-25), and bypass-closed (C-26). This is the R7 golden candidate.

**Hypothesis**: V-01/V-02/V-03 each pass one new criterion at 99.0. V-04 passes C-25 + C-26 at 99.5. V-05 adds C-27 as the leading purpose statement, completing the BINDING DECLARATION's three-layer structure: purpose → contents → constraints. The meta-purpose statement (C-27) is most readable as a leading sentence because it frames what follows; the exhaustiveness clause (C-25) follows naturally after the table (closing the positive assertion); the prohibition (C-26) closes the declaration by naming the downstream constraint. All three together produce the strongest auditable form. Predicted composite: 100 (Platinum).

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

## R7 Design Notes

**What changed from R6:**

R6 confirmed V-05 as Platinum (100/100) under v6 rubric (denominator 17). The R6 scorecard surfaced three excellence signals from the C-23 gradient that became C-25/C-26/C-27 in the v7 rubric. Against v7 (denominator 20), R6 V-05 retroscores 99.5: fails C-25 (no exhaustiveness scope-closure -- the BINDING DECLARATION lists what IS bound but never says "No other DEFAULTS fields are directly bound"). R6 V-05 already passes C-26 (has "Phase 5 does not read SIGNAL DEFAULTS inertia fields directly") and C-27 (has "This declaration makes the full DEFAULTS->BELIEF MAP data flow auditable from skill structure alone" -- but embedded in the opening sentence rather than as a leading purpose statement).

**Retroactive R6 scores under v7 rubric (denominator 20 aspirational):**

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-22 | P | F | F | P | P |
| C-23 | F | P | F | P | P |
| C-24 | F | F | P | F | P |
| C-25 | F | P | F | F | F |
| C-26 | F | F | F | P | P |
| C-27 | F | F | F | F | P |
| Aspirational | 15/20 | 16/20 | 15/20 | 17/20 | 19/20 |
| Composite | 97.5 | 98.0 | 97.5 | 98.5 | **99.5** |

**V-04 note**: R6 V-04 passes C-22+C-23+C-26 but not C-24, C-25, C-27. The BINDING DECLARATION had "Phase 5 CTA construction reads from AUDIENCE BELIEF MAP, not from SIGNAL DEFAULTS directly" (C-26) but lacked exhaustiveness statement (C-25) and meta-purpose (C-27). R7 V-04 adds C-25 to C-26 (no meta-purpose), and R7 V-05 adds all three with C-27 promoted to the leading sentence.

**BINDING DECLARATION structure progression:**

| Variation | Opening | Table | Post-table |
|-----------|---------|-------|------------|
| V-01 | Binding intro | 3-row | Exhaustiveness only (C-25) |
| V-02 | Binding intro | 3-row | Prohibition only (C-26) |
| V-03 | Meta-purpose (C-27) + binding intro | 3-row | (none) |
| V-04 | Binding intro | 3-row | Exhaustiveness (C-25) + Prohibition (C-26) |
| V-05 | Meta-purpose (C-27) + binding intro | 3-row | Exhaustiveness (C-25) + Prohibition (C-26) |

**Diagnostic question for R7:** Does C-27's "at the site of the declaration" placement requirement specify LEADING the declaration vs. appearing anywhere within it? R6 V-05 had the meta-purpose embedded in the opening sentence ("The following SIGNAL DEFAULTS fields are bound... This declaration makes the full DEFAULTS->BELIEF MAP data flow auditable...") as a trailing clause -- readable but not a standalone leading statement. V-03 promotes it to the opening standalone sentence before the binding intro. V-05 does the same. If C-27 requires the statement to be identifiable as a purpose statement (not embedded as a trailing clause), V-03/V-05 are the stronger form. The scorecard will resolve this.

```json
{"context": "R7 targets C-25/C-26/C-27 from R6 excellence signals", "base_retroscore": {"R6-V-05": 99.5}, "single_axis": ["V-01 (C-25: exhaustiveness scope-closure only)", "V-02 (C-26: Phase 5 access prohibition only)", "V-03 (C-27: meta-purpose leading statement only)"], "combined": ["V-04 (C-25 + C-26: exhaustiveness + prohibition)", "V-05 (C-25 + C-26 + C-27: full synthesis, meta-purpose leads declaration)"], "golden_candidate": "V-05", "diagnostic_question": "C-27: does 'at the site of the declaration' require leading placement vs. trailing clause? R6 V-05 had meta-purpose as trailing clause in opening sentence and passed C-27. R7 V-03/V-05 promote it to standalone leading statement."}
```
