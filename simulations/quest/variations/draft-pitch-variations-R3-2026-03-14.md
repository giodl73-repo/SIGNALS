The file-writing tools are being blocked. I'll output the variations directly as Markdown as instructed. Here are the 5 complete prompt bodies:

---

## draft-pitch — Variations R3

**5 variations across 3 single-axis + 2 combined axes:**

| ID | Axis | Hypothesis | Criteria targeted |
|----|------|------------|-----------------|
| **V-01** | Role sequence -- Strategy before PM | Named BELIEF MAP + POSITIONING LOCK from a Strategy pass create a multi-node forward reference chain that PM cannot bypass | C-14, C-15 |
| **V-02** | Output format -- Tabular belief mapping | A 4-column belief table (Audience, Core Belief, Failure Mode, Inertia Excuse) makes C-15 structurally verifiable -- missing cells are visually incomplete | C-15, C-09 |
| **V-03** | Inertia framing -- Maximum saturation | Per-audience inertia fields in DEFAULTS TABLE + inertia required in every CTA -- C-09 enforced unconditionally across all three pitch versions, not only exec | C-09, C-15 |
| **V-04** | Role sequence + Lifecycle emphasis | Full three-node dependency chain: BELIEF MAP -> POSITIONING LOCK -> EXEC OPENING SENTENCE -- each phase gate references the prior by name; skipping any phase breaks multiple downstream citations | C-13, C-14, C-15 |
| **V-05** | Phrasing register + Output format | Conversational elicitation throughout + numbered reference list for proof citations -- removes checklist feel while keeping structural enforcement intact | C-13, C-14, C-15 |

**Key structural differences from R2:**

| Pattern | R2 best (V-05) | R3 innovation |
|---------|---------------|---------------|
| C-13 | DEFAULTS TABLE unconditional at top | All R3 variations carry this; axes vary what else goes in the table |
| C-14 | EXEC OPENING SENTENCE named, Step 5 cites it | V-01/V-04 chain three named outputs -- BELIEF MAP, POSITIONING LOCK, EXEC OPENING SENTENCE; V-02 names BELIEF TABLE; all forms stronger than a single reference |
| C-15 | Audience belief mapping: three prose sentences before drafting | V-02/V-04 formalize into a table with named columns; V-03 adds inertia column; V-01 isolates as Strategy-role output; V-05 uses conversational elicitation |

---

## V-01 -- Single Axis: Role Sequence (Strategy Before PM)

**Axis**: Role sequence -- an explicit STRATEGY PASS runs before any PM drafting. Strategy produces two named outputs: BELIEF MAP and POSITIONING LOCK. PM pass drafts exclusively from those named outputs and cannot introduce new positioning.

**Hypothesis**: Separating roles enforces C-14 more powerfully than a self-check within a single-pass skill. Every downstream PM step references a named Strategy output by exact name. Skipping the Strategy pass breaks multiple forward references simultaneously. C-15 is enforced by making belief mapping a Strategy obligation, structurally prior to all drafting.

---

### Prompt Body

You are executing the `draft-pitch` skill for: `{topic}`.

---

**SIGNAL DEFAULTS**

These apply unconditionally to all runs. Override individual fields with scout signal values when found.

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

**STRATEGY PASS**

The Strategy role runs first. All outputs from this pass are named and locked. PM pass references them by exact name and does not revise them.

---

**Strategy Step 1: Signal Intake**

Check for prior signals:
- `simulations/scout/positioning/{topic}-positioning-*.md`
- `simulations/scout/competitors/{topic}-competitors-*.md`
- `simulations/scout/requirements/{topic}-requirements-*.md`

Write: "Signals found: [list files]" or "No prior signals -- SIGNAL DEFAULTS apply."

For each signal found: note which SIGNAL DEFAULTS fields it overrides and what the override value is.

---

**Strategy Step 2: BELIEF MAP**

Before any argument is constructed, identify what each audience must believe first. Write one sentence per audience -- the single belief whose absence makes all other arguments fail.

**BELIEF MAP:**

| Audience | Must believe before anything else | Argument fails if they don't believe this |
|----------|----------------------------------|------------------------------------------|
| Exec | [Write the first belief] | [Name the failure] |
| Dev | [Write the first belief] | [Name the failure] |
| Maker | [Write the first belief] | [Name the failure] |

This output is named **BELIEF MAP**. PM Step 5 drafts from it. Do not proceed until all three rows are filled.

---

**Strategy Step 3: POSITIONING LOCK**

Answer the three positioning questions in writing. These are locked inputs. PM pass cannot revise them.

**POSITIONING LOCK:**

1. **Competitor**: "The real competition for teams building {topic} is not a named tool. It is ___."
   (Use active Primary competitor from SIGNAL DEFAULTS, or override from scout signal.)

2. **Outcome**: "Signal gives {primary audience} ___ before the first line of code is written."
   (Use active Exec outcome, or override from scout signal.)

3. **Ruling out**: List the three active Ruling Out values from SIGNAL DEFAULTS. Format each as:
   "[Category]. Signal does not [function]."

This output is named **POSITIONING LOCK**. PM Step 4 and PM Step 5 reference it by this name.

---

**PM PASS**

The PM role drafts from BELIEF MAP and POSITIONING LOCK. Both are locked. PM does not introduce positioning not present in POSITIONING LOCK. PM does not re-derive beliefs beyond what is in BELIEF MAP.

---

**PM Step 4: EXEC OPENING GATE**

This step produces a single named output. PM Step 5 references it by exact name.

**Write: EXEC OPENING SENTENCE**
> [One sentence only -- nothing else in this step.]

**Binary gate:**
Does EXEC OPENING SENTENCE name a cost, risk, or productivity consequence teams face today -- without mentioning a feature, tool, or product?

- **YES** -- proceed to PM Step 5.
- **NO** -- rewrite EXEC OPENING SENTENCE. Anchor rewrite in the active Inertia cost from SIGNAL DEFAULTS. Re-apply gate. Repeat until YES.

**EXEC OPENING SENTENCE is locked.**

---

**PM Step 5: Full Draft**

Draft each version starting from the audience belief in BELIEF MAP. Use POSITIONING LOCK Competitor, Outcome, and Ruling Out answers as your only source for positioning claims. Do not introduce claims not present in those outputs.

**Exec Version**
*Audience belief anchor (from BELIEF MAP): exec row.*

- **Hook**: EXEC OPENING SENTENCE (locked, exact as written in PM Step 4).
- **What It Does**: POSITIONING LOCK Outcome answer. One sentence.
- **Why It Matters**: POSITIONING LOCK Competitor answer named explicitly. "The alternative is not a competing product. It is [Competitor]." 2-3 sentences ROI framing.
- **Call to Action**: One specific decision, demo slot, or budget ask. Not "learn more."

**Dev Version**
*Audience belief anchor (from BELIEF MAP): dev row.*

- **Hook**: A scenario the developer is already in -- the moment before Signal changes what they do next. Not a business case.
- **What It Does**: At least one concrete interaction. Example: `/scout:requirements topic={topic}` produces `{topic}-requirements-{date}.md`. Reader can answer "what would I actually type?"
- **Why It Matters**: Active Dev friction value from SIGNAL DEFAULTS. Named directly.
- **Call to Action**: One command or file path runnable today without PM involvement.

**Maker Version**
*Audience belief anchor (from BELIEF MAP): maker row.*

- **Hook**: The question they have already asked themselves. Zero unexplained acronyms. Zero namespace references. Zero CLI terminology.
- **What It Does**: Plain English. Translate every Signal term to what it does for a person.
- **Why It Matters**: Active Maker outcome from SIGNAL DEFAULTS. Connect to their decision work.
- **Call to Action**: Something proposable in a meeting without filing a ticket.

---

**PM Step 6: Anti-Positioning**

Write "## What Signal Is NOT" from POSITIONING LOCK Ruling Out values. Add one additional adjacent category not already present in SIGNAL DEFAULTS.

Format: `[Category]. Signal does not [specific function]. [One sentence on why this distinction matters for {topic} specifically.]`

Minimum four bullets.

---

**PM Step 7: Proof Points**

For every factual claim in exec and dev versions, annotate:
- `[source: {artifact-path}]` -- direct file reference
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

SIGNAL DEFAULTS, BELIEF MAP, POSITIONING LOCK, sentence gate, and proof audit are working notes -- not in saved artifact.

**Save to**: `simulations/draft/pitches/{topic}-pitch-{date}.md`

---

## V-02 -- Single Axis: Output Format (Tabular Belief Mapping)

**Axis**: Output format -- the belief mapping step uses a structured 4-column table instead of prose Q&A. Columns are named: Audience, Core Belief, Failure Mode, Inertia Excuse. A table with named columns cannot be answered in ambient prose -- each cell requires a discrete, inspectable value.

**Hypothesis**: A table with named columns makes C-15 structurally verifiable. Missing cells are visually incomplete. The Inertia Excuse column also forces C-09 framing per audience, not just in exec framing -- integrating C-15 and C-09 in a single step that applies to all three pitch versions simultaneously.

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

**Step 1: Signal Intake**

Check for prior signals:
- `simulations/scout/positioning/{topic}-positioning-*.md`
- `simulations/scout/competitors/{topic}-competitors-*.md`
- `simulations/scout/requirements/{topic}-requirements-*.md`

Write: "Signals found: [list files]" or "No prior signals -- SIGNAL DEFAULTS apply."

For each signal found: note which SIGNAL DEFAULTS rows it overrides.

---

**Step 2: BELIEF TABLE**

Before writing any pitch content, fill this table. Every cell must contain a specific, written value. A cell is not complete if it restates the column header in general terms.

This output is named **BELIEF TABLE**. Step 5 drafts each version from the corresponding row.

| Audience | Core Belief (must hold before any argument lands) | Failure Mode (what they think if this belief is absent) | Inertia Excuse (what they say to justify not acting) |
|----------|--------------------------------------------------|-------------------------------------------------------|-----------------------------------------------------|
| Exec | [Complete] | [Complete] | [Complete] |
| Dev | [Complete] | [Complete] | [Complete] |
| Maker | [Complete] | [Complete] | [Complete] |

For the Inertia Excuse column: use the active Primary competitor value from SIGNAL DEFAULTS as the baseline if no scout override exists.

Do not draft any pitch content until all nine cells are filled.

---

**Step 3: Positioning Lock**

Answer in writing before any pitch content is drafted. These are locked.

1. **Competitor**: "The real competition for teams building {topic} is not a named tool. It is ___."
   (Use active Primary competitor, or override from scout signal.)

2. **Outcome**: "Signal gives {primary audience} ___ before the first line of code is written."
   (Use active Exec outcome, or override from scout signal.)

3. **Ruling out**: List three categories Signal is NOT, using active Ruling Out values from SIGNAL DEFAULTS.

---

**Step 4: EXEC OPENING GATE**

This step produces a single named output. Step 5's exec Hook references it by exact name.

**Write: EXEC OPENING SENTENCE**
> [One sentence only.]

**Binary gate:**
Does EXEC OPENING SENTENCE name a cost, risk, or productivity consequence teams face today -- without mentioning a feature, tool, or product name?

- **YES** -- EXEC OPENING SENTENCE is locked. Proceed to Step 5.
- **NO** -- rewrite. Use active Inertia cost from SIGNAL DEFAULTS. Re-apply gate. Repeat until YES.

**EXEC OPENING SENTENCE is locked.**

---

**Step 5: Full Draft**

Draft each version from the corresponding row in BELIEF TABLE. The Core Belief column anchors the Hook. The Inertia Excuse column anchors the CTA -- each call to action must address why this audience won't act.

**Exec Version**
*Row from BELIEF TABLE: exec.*

- **Hook**: EXEC OPENING SENTENCE (locked, exact from Step 4).
- **What It Does**: Positioning Lock Outcome answer. One sentence.
- **Why It Matters**: Positioning Lock Competitor named explicitly. ROI framing. 2-3 sentences.
- **Call to Action**: One specific decision, demo slot, or budget ask. Must address the Inertia Excuse from BELIEF TABLE exec row.

**Dev Version**
*Row from BELIEF TABLE: dev.*

- **Hook**: A concrete scenario the developer is in right now -- not a business case.
- **What It Does**: At least one concrete interaction. Example: `/scout:requirements topic={topic}` produces `{topic}-requirements-{date}.md`. Reader answers "what would I actually type?"
- **Why It Matters**: Active Dev friction from SIGNAL DEFAULTS. Named directly.
- **Call to Action**: One runnable command or file path today. Must address the Inertia Excuse from BELIEF TABLE dev row.

**Maker Version**
*Row from BELIEF TABLE: maker.*

- **Hook**: The question they've already had. Zero acronyms. Zero namespace references. Zero CLI terminology.
- **What It Does**: Plain English. Replace every Signal term with what it does for a person.
- **Why It Matters**: Active Maker outcome from SIGNAL DEFAULTS. Connect to their decision context.
- **Call to Action**: Something proposable in a meeting without a ticket. Must address the Inertia Excuse from BELIEF TABLE maker row.

---

**Step 6: Anti-Positioning**

Write "## What Signal Is NOT" from Positioning Lock Ruling Out values.

Format: `[Category]. Signal does not [specific function].`

Minimum three bullets.

---

**Step 7: Proof Points**

For every factual claim in exec and dev:
- `[source: {artifact-path}]` -- direct file
- `[source: prior signal]` -- scout artifact
- `[UNVERIFIED]` -- flag; replace with hedged language or active Proof fallback before saving.

---

**Output format**:
```
## Exec Version
## Dev Version
## Maker Version
## What Signal Is NOT
```

SIGNAL DEFAULTS, BELIEF TABLE, Positioning Lock, sentence gate, and proof audit are working notes -- not in saved artifact.

**Save to**: `simulations/draft/pitches/{topic}-pitch-{date}.md`

---

## V-03 -- Single Axis: Inertia Framing (Maximum Inertia Saturation)

**Axis**: Inertia framing -- inertia is named in the SIGNAL DEFAULTS table with per-audience fields, embedded as a required element in the belief mapping step, and required in every version's CTA. C-09 is enforced at the pitch level (all three versions), not only at the exec positioning level.

**Hypothesis**: R2's C-09 framing appears primarily in the exec's Why It Matters section. The dev CTA ("one action available today") and maker CTA ("proposable in a meeting") don't structurally address why someone wouldn't act. Requiring each CTA to name the audience's inertia default forces the pitch to compete with status quo at every version level, not just exec.

---

### Prompt Body

You are executing the `draft-pitch` skill for: `{topic}`.

---

**SIGNAL DEFAULTS**

These apply unconditionally to all runs. Override with scout signal values when found.

| Field | Default Value |
|-------|---------------|
| Primary competitor | "teams doing nothing -- the review that never happened" |
| Exec inertia | "the meeting that was rescheduled, the spec review that happened post-build, the go/no-go that nobody called" |
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

Before writing any pitch content, answer for each audience: what must they believe first, and what is the inertia argument they use to avoid believing it?

Write each answer before drafting begins. Do not draft pitch content until all six lines are written.

**Exec must believe**: [Write the single belief that precedes any ROI argument.]
**Exec inertia argument**: [Write the specific thing the exec says or does instead. Use active Exec inertia from SIGNAL DEFAULTS if no scout override.]

**Dev must believe**: [Write the single belief that precedes any workflow argument.]
**Dev inertia argument**: [Write the specific thing the dev says or does instead. Use active Dev inertia from SIGNAL DEFAULTS if no scout override.]

**Maker must believe**: [Write the single belief that precedes any "can I do this?" argument.]
**Maker inertia argument**: [Write the specific thing the maker says or does instead. Use active Maker inertia from SIGNAL DEFAULTS if no scout override.]

---

**Step 3: Positioning Lock**

Answer in writing before drafting begins. These are locked.

1. **Competitor**: "The real competition for teams building {topic} is not a named tool. It is ___."
   (Use active Primary competitor from SIGNAL DEFAULTS, or override from scout signal.)

2. **Outcome**: "Signal gives {primary audience} ___ before the first line of code is written."
   (Use active Exec outcome, or override from scout signal.)

3. **Ruling out**: List three categories Signal is NOT, from active Ruling Out values in SIGNAL DEFAULTS.

---

**Step 4: EXEC OPENING GATE**

Produce one named output. Step 5's exec Hook cites it by exact name.

**Write: EXEC OPENING SENTENCE**
> [One sentence only.]

**Binary gate:**
Does EXEC OPENING SENTENCE name a cost, risk, or productivity consequence teams face today -- without mentioning a feature, tool, or product?

- **YES** -- EXEC OPENING SENTENCE is locked. Proceed to Step 5.
- **NO** -- rewrite. Use active Exec inertia from SIGNAL DEFAULTS as your anchor. Re-apply gate. Repeat until YES.

**EXEC OPENING SENTENCE is locked.**

---

**Step 5: Full Draft**

Each version's CTA must name the audience's inertia argument from Step 2 and offer a specific counter. A generic "learn more" or "try it today" does not pass -- the CTA must address what this audience does instead.

**Exec Version**

- **Hook**: EXEC OPENING SENTENCE (locked, exact from Step 4).
- **What It Does**: Positioning Lock Outcome answer. One sentence.
- **Why It Matters**: Positioning Lock Competitor answer named explicitly. 2-3 sentences. "The alternative is [Competitor]. Signal eliminates that cost before the build starts."
- **Call to Action**: One specific ask. Must name the Exec inertia argument from Step 2 and counter it: "Instead of [inertia argument], [one concrete action]."

**Dev Version**

- **Hook**: A concrete scenario the developer is in right now -- the moment before Signal changes what happens next.
- **What It Does**: At least one concrete interaction. Example: `/scout:requirements topic={topic}` produces `{topic}-requirements-{date}.md`. Reader answers "what would I actually type?"
- **Why It Matters**: Active Dev friction from SIGNAL DEFAULTS. Named directly.
- **Call to Action**: One runnable action today. Must name the Dev inertia argument from Step 2: "Instead of [inertia argument], [specific command or file]."

**Maker Version**

- **Hook**: The question they have already asked themselves. Zero unexplained acronyms. Zero namespace references. Zero CLI terminology.
- **What It Does**: Plain English. Translate every Signal term to what it does for a person.
- **Why It Matters**: Active Maker outcome from SIGNAL DEFAULTS. Connect to their decision context.
- **Call to Action**: Something proposable in a meeting. Must name the Maker inertia argument from Step 2: "Instead of [inertia argument], [one proposable action]."

---

**Step 6: Anti-Positioning**

Write "## What Signal Is NOT" from Positioning Lock Ruling Out values.

Format: `[Category]. Signal does not [specific function].`

Minimum three bullets.

---

**Step 7: Proof Points**

For every factual claim in exec and dev:
- `[source: {artifact-path}]` -- direct file
- `[source: prior signal]` -- scout artifact
- `[UNVERIFIED]` -- flag; replace with hedged language or active Proof fallback before saving.

---

**Output format**:
```
## Exec Version
## Dev Version
## Maker Version
## What Signal Is NOT
```

SIGNAL DEFAULTS, belief mapping, positioning lock, sentence gate, and proof audit are working notes -- not in saved artifact.

**Save to**: `simulations/draft/pitches/{topic}-pitch-{date}.md`

---

## V-04 -- Combined: Role Sequence + Lifecycle Emphasis

**Axes**: Role sequence (Strategy before PM) + lifecycle emphasis (each phase gate produces a named output referenced by the next gate)

**Hypothesis**: Full three-node named dependency is the strongest form of C-14. R2 V-05 has one named output (EXEC OPENING SENTENCE) cited by one downstream step. V-04 chains BELIEF MAP, POSITIONING LOCK, and EXEC OPENING SENTENCE -- each referenced by the next phase. Lifecycle emphasis (explicit phase headers, hard stops, `*Consumes* / *Produces*` declarations) makes the chain impossible to abbreviate.

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

For each signal found: note which SIGNAL DEFAULTS rows it overrides and write the override value.

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

Draft each version starting from the audience belief in BELIEF MAP. Use POSITIONING LOCK as the sole source for positioning claims. Do not introduce claims not present in POSITIONING LOCK.

**Exec Version**
*Audience belief anchor (from BELIEF MAP, exec row).*

- **Hook**: EXEC OPENING SENTENCE (from Phase 4, locked, exact).
- **What It Does**: POSITIONING LOCK Outcome answer. One sentence.
- **Why It Matters**: POSITIONING LOCK Competitor named explicitly. "The alternative is not a competing product. It is [Competitor]." 2-3 sentences ROI framing.
- **Call to Action**: One specific decision, demo slot, or budget ask. Not "learn more."

**Dev Version**
*Audience belief anchor (from BELIEF MAP, dev row).*

- **Hook**: A scenario the developer is in right now -- the moment before Signal changes what happens next.
- **What It Does**: At least one concrete interaction. Example: `/scout:requirements topic={topic}` produces `{topic}-requirements-{date}.md`. Reader answers "what would I actually type?"
- **Why It Matters**: Active Dev friction from SIGNAL DEFAULTS. Named directly.
- **Call to Action**: One command or file path runnable today without PM involvement.

**Maker Version**
*Audience belief anchor (from BELIEF MAP, maker row).*

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

## V-05 -- Combined: Phrasing Register + Output Format

**Axes**: Phrasing register -- conversational throughout, imperative prompts replaced with first-person elicitation questions + structured proof citations as a numbered reference list at the end.

**Hypothesis**: Conversational phrasing changes how the model engages with each step. Imperative instructions can trigger pattern-completion; elicitation questions trigger reasoning. Combined with a numbered reference list for proof citations rather than inline `[UNVERIFIED]` tags, the output is cleaner and the audit is more scannable. All three new criteria are enforced through the same structural mechanics -- in a different register.

---

### Prompt Body

You are executing the `draft-pitch` skill for: `{topic}`.

---

**SIGNAL DEFAULTS**

Use these whenever you don't have a scout signal to draw from. These are always active -- override specific fields when prior signals are available, use as-is otherwise.

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

**Step 1: What signals already exist?**

Look for prior scout work at:
- `simulations/scout/positioning/{topic}-positioning-*.md`
- `simulations/scout/competitors/{topic}-competitors-*.md`
- `simulations/scout/requirements/{topic}-requirements-*.md`

Note what you found -- or write "No prior signals" if nothing is there. For each file found, note which SIGNAL DEFAULTS fields it changes and what the new value is.

---

**Step 2: What does each audience need to believe first?**

Before writing anything for the pitch, think through this question per audience: *what's the one thing they need to believe before any other argument can land?*

Write your answers here -- these anchor the drafts in Step 5.

**Exec**: What must the exec believe before the business case works? Write one sentence. (Think: what objection instantly kills everything else if it isn't addressed first?)

**Dev**: What must the developer believe before the workflow argument works? Write one sentence. (Think: what makes them dismiss this as theoretical productivity?)

**Maker**: What must the maker believe before "can I do this?" becomes "yes"? Write one sentence. (Think: what makes them feel it isn't for them?)

Don't move to Step 3 until you have a written sentence for each audience.

---

**Step 3: Lock the positioning**

Before writing any pitch prose, answer these. They don't change during the draft -- if you want to revise them, do it here, not in Step 5.

*Who are we really competing with?*
Complete this sentence: "The real competition for teams working on {topic} isn't a named tool. It's ___."
Start from the active Primary competitor in SIGNAL DEFAULTS, or a scout override if one exists.

*What's the one thing Signal gives them?*
Complete this sentence: "Signal gives {primary audience} ___ before the first line of code is written."
Start from the active Exec outcome in SIGNAL DEFAULTS, or a scout override.

*What are we ruling out?*
Name three things Signal is not. Pull from the active Ruling Out fields in SIGNAL DEFAULTS as your starting point.

---

**Step 4: Write the exec opening, then test it**

Before drafting any pitch content, write just the opening sentence here. Nothing else yet.

**EXEC OPENING SENTENCE:**
> [Write it here.]

Now read it back. Does this sentence name a cost, risk, or consequence that teams face today -- without mentioning a product feature, tool name, or technology?

If yes, it passes. Keep going.

If no, rewrite it. Use the Inertia cost from SIGNAL DEFAULTS as your anchor. Try again. Keep going once it passes.

**EXEC OPENING SENTENCE is set.** Step 5's exec Hook uses it exactly as written here -- do not paraphrase it.

---

**Step 5: Draft all three versions**

Start each version from the audience belief you wrote in Step 2. The belief is your anchor -- lead toward it before arguing past it.

**Exec Version**
*Belief anchor from Step 2: exec.*

- **Hook**: EXEC OPENING SENTENCE exactly as written in Step 4. Do not paraphrase.
- **What It Does**: Your Outcome sentence from Step 3. One sentence.
- **Why It Matters**: Your Competitor answer from Step 3, named explicitly. "The alternative isn't a competing product -- it's [your answer]." 2-3 sentences.
- **Call to Action**: One specific ask -- a decision, a demo slot, a budget line. Not "reach out to learn more."

**Dev Version**
*Belief anchor from Step 2: dev.*

- **Hook**: Put them in a scenario they already recognize -- the moment before Signal would have changed what happened next. Not a business case.
- **What It Does**: Show them at least one concrete interaction -- a command, an artifact name, a file that shows up. Example: `/scout:requirements topic={topic}` produces `{topic}-requirements-{date}.md`. A reader should be able to answer "what would I actually type?"
- **Why It Matters**: Name the friction directly. Use the active Dev friction from SIGNAL DEFAULTS if no scout override.
- **Call to Action**: One thing they can run or open today -- no PM required.

**Maker Version**
*Belief anchor from Step 2: maker.*

- **Hook**: A question they've already asked themselves. No acronyms, no namespace names, no command-line references. If the vocabulary isn't theirs, they stop reading.
- **What It Does**: Plain English only. Every Signal term gets translated into what it does for a person.
- **Why It Matters**: Their decision context -- design direction, research, stakeholder alignment. Use the active Maker outcome from SIGNAL DEFAULTS.
- **Call to Action**: Something they can propose in a meeting without filing a ticket.

---

**Step 6: Write the anti-positioning section**

Write "## What Signal Is NOT" using your Ruling Out answers from Step 3.

Format: `[Category]. Signal does not [specific function].`

Minimum three bullets. Vague statements ("not just another AI tool") don't count.

---

**Step 7: Collect your references**

Go through the exec and dev versions. For each factual claim, note the source in a numbered list:

1. Claim: [claim text] -- Source: [artifact path or "prior signal"]
2. Claim: [claim text] -- Source: [artifact path or "prior signal"]
3. ...

For any claim you can't source: revise it to a hedged form, or replace it with the Proof fallback from SIGNAL DEFAULTS, before saving.

---

**Output format**:
```
## Exec Version
## Dev Version
## Maker Version
## What Signal Is NOT
```

Steps 1-4 and Step 7 (reference list) are working notes -- not in saved artifact.

**Save to**: `simulations/draft/pitches/{topic}-pitch-{date}.md`

---

## R3 Design Notes

**What changed from R2:**

R2 formalized three excellence signals into C-13/C-14/C-15. R2 V-05 was the only variation that hit all three. R3 makes C-13/C-14/C-15 baseline requirements for all five variations, then varies other axes to test whether different structural forms produce different output quality at the same pass/fail ceiling.

**Predicted scores under v3 rubric (denominator 8):**

| Variation | C-13 | C-14 | C-15 | Other aspirational | Predicted composite |
|-----------|------|------|------|--------------------|---------------------|
| V-01 | PASS (DEFAULTS TABLE before STRATEGY PASS) | PASS (BELIEF MAP + POSITIONING LOCK + EXEC OPENING SENTENCE chained; PM Step 5 cites all three) | PASS (Strategy Step 2 BELIEF MAP table, named output, produced before any PM drafting) | C-08-C-12 PASS | ~100 |
| V-02 | PASS (DEFAULTS TABLE at top) | PASS (BELIEF TABLE named in Step 2; EXEC OPENING SENTENCE named in Step 4; Step 5 cites it by exact name) | PASS (BELIEF TABLE with named columns; nine cells required before any drafting) | C-08-C-12 PASS | ~100 |
| V-03 | PASS (DEFAULTS TABLE with per-audience inertia fields) | PASS (EXEC OPENING SENTENCE named; Step 5 exec Hook cites it by exact name) | PASS (Step 2: six written fields required before drafting) | C-08-C-12 PASS | ~100 |
| V-04 | PASS (DEFAULTS TABLE before Phase 1) | PASS (three-node chain: BELIEF MAP named in Phase 2, POSITIONING LOCK named in Phase 3, EXEC OPENING SENTENCE named in Phase 4; Phase 5 cites all three by exact name) | PASS (Phase 2 BELIEF MAP table; Phase 2 hard stop before Phase 3 begins) | C-08-C-12 PASS | ~100 |
| V-05 | PASS (DEFAULTS TABLE at top) | PASS (EXEC OPENING SENTENCE named in Step 4; Step 5 says "exactly as written in Step 4 -- do not paraphrase") | PASS (Step 2 conversational elicitation; "write your answers here"; three written sentences required before Step 3) | C-08-C-12 PASS | ~100 |

**Predicted discriminator for R3:** Composite formula at full pass: (4/4 * 60) + (3/3 * 30) + (8/8 * 10) = 100. Discrimination may emerge from:

1. **C-15 pass condition edge**: The rubric flags "implicit or ambient audience framing" as failing. V-05's conversational "write your answers here" satisfies structurally, but the register may invite summarization. V-01/V-02/V-04's table format makes cells inspectable -- a table row cannot be ambient.

2. **C-14 forward reference chain depth**: V-04's three-node chain is the strongest form. V-01 has two named pre-outputs plus EXEC OPENING SENTENCE. V-02/V-03/V-05 have one named gate output. All five have at least one downstream reference, but chain depth varies.

3. **C-08 proof audit completeness**: V-05's numbered reference list may surface more claims than inline annotation (V-01-V-04), or the numbered format may invite selective coverage. V-04's Phase 7 with explicit phase header may produce more exhaustive audits than V-05's conversational Step 7.
