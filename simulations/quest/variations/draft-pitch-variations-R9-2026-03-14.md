Done. `simulations/quest/variations/draft-pitch-variations-R9-2026-03-14.md` written.

---

## draft-pitch -- Variations R9

**Base**: R8 V-05 (100.0/100 on 30 criteria). R9 probes **C-38, C-39, C-40** — whether Phase 5 is *auditable*, not just *structurally present*.

### Three gaps in R8 V-05

| Criterion | Gap |
|-----------|-----|
| **C-38** Phase-level envelopment | INERTIA PROFILE + Maker-first + DIFFERENTIATION GATE all present, but no named block states their sequential relationship as pre-commit/fill/close |
| **C-39** Pre-committed anchor | EXEC OPENING SENTENCE named as locked at Phase 4, but no statement says Maker-first cannot weaken it |
| **C-40** Gate converts advisories | Q2 (zero acronyms) and Q3 (scenario hook) have advisory counterparts; Q1 (Core Belief distinctness) introduces a new constraint only at the gate |

### Variation map

| ID | Axis | Change |
|----|------|--------|
| **V-01** | Lifecycle emphasis | Named **PHASE 5 STRUCTURE** block before INERTIA PROFILE — declares the three envelope elements and their pre-commit/fill/close sequential relationship explicitly |
| **V-02** | Phrasing register | **Draft-order integrity** statement after Maker-first declaration — names EXEC OPENING SENTENCE as the pre-committed anchor and states Maker-first cannot weaken it |
| **V-03** | Role sequence + inertia framing | Advisory **Core Belief distinctness** instruction added to Phase 2 column definition — so DIFFERENTIATION GATE Q1 converts a pre-existing advisory, not a new constraint |
| **V-04** | V-01 + V-02 | PHASE 5 STRUCTURE + draft-order integrity (C-38 + C-39; C-40 still fails) |
| **V-05** | V-01 + V-02 + V-03 | Full synthesis — all three audibility gaps closed; **R9 golden candidate** |

### Structural logic

V-05 completes Phase 5 audibility the same way the R7 BINDING DECLARATION completed Phase 2 audibility: the PHASE 5 STRUCTURE block names the pattern before any draft is written, the draft-order integrity statement defends the pre-committed anchor, and the Phase 2 advisory grounds Q1 so the gate traces to pre-existing constraints on all three questions.
 three envelope elements present). R9 makes Phase 5 auditable from skill structure alone by (a) naming the envelope pattern explicitly, (b) closing the draft-order integrity question with a named anchor, and (c) grounding every gate question in a pre-existing advisory so the gate's pass/fail structure is derivable from the skill, not invented at the gate.

---

## V-01 -- Phase Envelope Declaration (C-38 only)

**Axis**: Lifecycle emphasis -- PHASE 5 STRUCTURE named block added before INERTIA PROFILE.

**Hypothesis**: C-38 requires that the sequential relationship of INERTIA PROFILE + Maker-first + DIFFERENTIATION GATE be made *explicit* in skill structure -- not merely present. Adding a named structural declaration block before Phase 5 drafting begins states the pre-commit/fill/close pattern explicitly, making the phase auditable as a unit. C-39 and C-40 remain unaddressed; predicted gains = C-38 only (+1 criterion over R8 V-05 base, but C-38 denominator is 33 so this yields fractional gains).

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

**PHASE 5 STRUCTURE** (read before any drafting step):

Phase 5 uses a pre-commit -> constrained-fill -> post-verify structure that mirrors the Phase 2 BINDING DECLARATION pattern:

1. **INERTIA PROFILE** (pre-commit step): commits each audience's inertia arc in writing before any version is drafted. Prevents post-hoc rationalization of Why-It-Matters sections.
2. **Constraint-ascending draft order -- Maker first, then Dev, then Exec** (constrained-fill step): ensures plain-language coherence is established before specialized framing is added. Each earlier version constrains the vocabulary permissions of the next.
3. **VERSION DIFFERENTIATION GATE** (post-verify step): verifies structural compliance at exit. Phase 5 cannot close until all gate questions reach passing state.

These three elements form a coherent pre-commit/fill/close envelope. All three must be present and executed in sequence. Having any two of three does not pass. Phase 5 is auditable from skill structure alone: the sequence is explicit before any draft is written.

---

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

## V-02 -- Draft-Order Integrity Statement (C-39 only)

**Axis**: Phrasing register -- explicit anchor-integrity statement added after Maker-first draft order declaration in Phase 5.

**Hypothesis**: C-39 requires that the skill explicitly name a prior-phase output as a pre-committed anchor AND state that the constrained draft order cannot weaken it. R8 V-05 names EXEC OPENING SENTENCE as locked at Phase 4 and cites it by name in the Exec Hook instruction, but never states the relationship between the Phase 4 lock and the Maker-first order. Adding a two-sentence anchor integrity note after the draft order declaration closes this gap. C-38 (no phase envelope statement) and C-40 (Q1 has no advisory counterpart) remain unaddressed.

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

**Draft-order integrity**: EXEC OPENING SENTENCE is locked at Phase 4, before Phase 5 begins. The Maker-first constraint-ascending order cannot weaken the exec version: EXEC OPENING SENTENCE is pre-committed by Phase 4's binary gate and the Exec Hook must use exact text regardless of draft order. Maker-first affects only which version is drafted first -- it does not change any locked output from Phases 2, 3, or 4.

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

## V-03 -- Advisory Distinctness Instruction (C-40 only)

**Axis**: Role sequence + inertia framing -- advisory Core Belief distinctness instruction added in Phase 2 so DIFFERENTIATION GATE Q1 converts a pre-existing advisory rather than introducing a new constraint.

**Hypothesis**: C-40 requires that every gate question enforce a constraint that already exists as an advisory elsewhere in the skill. Q2 (zero acronyms) and Q3 (scenario hook) already have advisory counterparts in the Phase 5 version drafting instructions. Q1 (Core Belief summaries substantively distinct) does not -- it introduces a new constraint only at the gate. Adding a distinctness advisory at Phase 2 Core Belief fill time gives Q1 a pre-existing constraint to convert. C-38 (no phase envelope) and C-39 (no anchor integrity) remain unaddressed.

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

- **Core Belief**: The one thing this audience must believe before any other argument can land. Each Core Belief must be substantively distinct from the other two -- naming a claim that belongs specifically to this audience and could not be the primary belief anchor for a different audience. A Core Belief that paraphrases another audience's Core Belief does not pass.
- **Failure Mode**: What the pitch *fails to achieve for this audience* if Core Belief is absent. Name a pitch outcome failure -- what the pitch cannot accomplish for this audience (e.g., "Exec won't authorize the demo slot," "Dev won't try the command," "Maker won't raise the question in their next meeting"). A restatement of Core Belief in negative form does not pass (e.g., "Exec won't believe the ROI argument" -- this restates the belief and is not a Failure Mode).
- **Inertia Excuse**: Fill from BINDING DECLARATION above. Template: `[active Exec inertia from SIGNAL DEFAULTS]` / `[active Dev inertia from SIGNAL DEFAULTS]` / `[active Maker inertia from SIGNAL DEFAULTS]`. Use scout override if available; otherwise use SIGNAL DEFAULTS value exactly.
- **Inertia Counter**: The specific action that addresses this Inertia Excuse. One concrete step. Pre-commit this value -- Phase 5 CTA uses `[Inertia Counter from AUDIENCE BELIEF MAP, audience row]` by exact reference. Do not leave ambiguous.

**AUDIENCE BELIEF MAP:**

| Audience | Core Belief | Failure Mode | Inertia Excuse | Inertia Counter |
|----------|-------------|--------------|----------------|-----------------|
| Exec | [Write belief -- substantively distinct from Dev and Maker beliefs] | [Name the pitch outcome failure] | [active Exec inertia from SIGNAL DEFAULTS] | [Name the counter action] |
| Dev | [Write belief -- substantively distinct from Exec and Maker beliefs] | [Name the pitch outcome failure] | [active Dev inertia from SIGNAL DEFAULTS] | [Name the counter action] |
| Maker | [Write belief -- substantively distinct from Exec and Dev beliefs] | [Name the pitch outcome failure] | [active Maker inertia from SIGNAL DEFAULTS] | [Name the counter action] |

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
   *(This enforces the Core Belief distinctness advisory stated in Phase 2 Core Belief column definition.)*
2. Does the Maker version contain any unexplained acronym or CLI reference (e.g., `/scout:`, `{topic}`, namespace names)? YES / NO
   *(This enforces the zero-acronym advisory stated in Maker Version Hook and Why-It-Matters instructions.)*
3. Does the Dev version open with a scenario (a moment the developer is in) rather than an outcome statement? YES / NO
   *(This enforces the scenario-hook advisory stated in Dev Version Hook instruction.)*

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

## V-04 -- Phase Envelope + Draft-Order Integrity (C-38 + C-39)

**Axes**: Lifecycle emphasis + phrasing register -- PHASE 5 STRUCTURE declaration (C-38) + draft-order integrity statement (C-39). No C-40 advisory instruction added.

**Hypothesis**: C-38 and C-39 are the two structural completeness criteria. C-38 asks whether the envelope is named; C-39 asks whether the anchor is declared. Together they close the audibility of Phase 5 structure without changing any Phase 2 advisory (C-40 remains unaddressed). Predicted to pass C-38 and C-39 but fail C-40 for the same reason as all prior variations -- Q1 still introduces distinctness as a new gate constraint.

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

**PHASE 5 STRUCTURE** (read before any drafting step):

Phase 5 uses a pre-commit -> constrained-fill -> post-verify structure that mirrors the Phase 2 BINDING DECLARATION pattern:

1. **INERTIA PROFILE** (pre-commit step): commits each audience's inertia arc in writing before any version is drafted. Prevents post-hoc rationalization of Why-It-Matters sections.
2. **Constraint-ascending draft order -- Maker first, then Dev, then Exec** (constrained-fill step): ensures plain-language coherence is established before specialized framing is added. Each earlier version constrains the vocabulary permissions of the next.
3. **VERSION DIFFERENTIATION GATE** (post-verify step): verifies structural compliance at exit. Phase 5 cannot close until all gate questions reach passing state.

These three elements form a coherent pre-commit/fill/close envelope. All three must be present and executed in sequence. Having any two of three does not pass. Phase 5 is auditable from skill structure alone: the sequence is explicit before any draft is written.

---

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

**Draft-order integrity**: EXEC OPENING SENTENCE is locked at Phase 4, before Phase 5 begins. The Maker-first constraint-ascending order cannot weaken the exec version: EXEC OPENING SENTENCE is pre-committed by Phase 4's binary gate and the Exec Hook must use exact text regardless of draft order. Maker-first affects only which version is drafted first -- it does not change any locked output from Phases 2, 3, or 4.

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

## V-05 -- Full Synthesis (C-38 + C-39 + C-40)

**Axes**: Lifecycle emphasis + phrasing register + role sequence -- PHASE 5 STRUCTURE declaration + draft-order integrity statement + advisory Core Belief distinctness instruction. R9 golden candidate.

**Hypothesis**: C-38, C-39, and C-40 are the three audibility completeness criteria for Phase 5. C-38 asks: is the envelope pattern named? C-39 asks: is the pre-committed anchor defended? C-40 asks: does every gate question convert a pre-existing advisory? V-05 adds all three. Together they make Phase 5 fully auditable from skill structure alone -- a reader can determine (a) that Phase 5 has a named pre-commit/fill/close structure, (b) that Maker-first is defended by a named pre-committed anchor, and (c) that every DIFFERENTIATION GATE question traces to an advisory instruction in the skill body. This completes the structural audibility of Phase 5 in the same way the BINDING DECLARATION completed Phase 2 in R7.

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

- **Core Belief**: The one thing this audience must believe before any other argument can land. Each Core Belief must be substantively distinct from the other two -- naming a claim that belongs specifically to this audience and could not serve as the primary belief anchor for a different audience. A Core Belief that paraphrases another audience's Core Belief does not pass.
- **Failure Mode**: What the pitch *fails to achieve for this audience* if Core Belief is absent. Name a pitch outcome failure -- what the pitch cannot accomplish for this audience (e.g., "Exec won't authorize the demo slot," "Dev won't try the command," "Maker won't raise the question in their next meeting"). A restatement of Core Belief in negative form does not pass (e.g., "Exec won't believe the ROI argument" -- this restates the belief and is not a Failure Mode).
- **Inertia Excuse**: Fill from BINDING DECLARATION above. Template: `[active Exec inertia from SIGNAL DEFAULTS]` / `[active Dev inertia from SIGNAL DEFAULTS]` / `[active Maker inertia from SIGNAL DEFAULTS]`. Use scout override if available; otherwise use SIGNAL DEFAULTS value exactly.
- **Inertia Counter**: The specific action that addresses this Inertia Excuse. One concrete step. Pre-commit this value -- Phase 5 CTA uses `[Inertia Counter from AUDIENCE BELIEF MAP, audience row]` by exact reference. Do not leave ambiguous.

**AUDIENCE BELIEF MAP:**

| Audience | Core Belief | Failure Mode | Inertia Excuse | Inertia Counter |
|----------|-------------|--------------|----------------|-----------------|
| Exec | [Write belief -- substantively distinct from Dev and Maker beliefs] | [Name the pitch outcome failure] | [active Exec inertia from SIGNAL DEFAULTS] | [Name the counter action] |
| Dev | [Write belief -- substantively distinct from Exec and Maker beliefs] | [Name the pitch outcome failure] | [active Dev inertia from SIGNAL DEFAULTS] | [Name the counter action] |
| Maker | [Write belief -- substantively distinct from Exec and Dev beliefs] | [Name the pitch outcome failure] | [active Maker inertia from SIGNAL DEFAULTS] | [Name the counter action] |

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

**PHASE 5 STRUCTURE** (read before any drafting step):

Phase 5 uses a pre-commit -> constrained-fill -> post-verify structure that mirrors the Phase 2 BINDING DECLARATION pattern:

1. **INERTIA PROFILE** (pre-commit step): commits each audience's inertia arc in writing before any version is drafted. Prevents post-hoc rationalization of Why-It-Matters sections.
2. **Constraint-ascending draft order -- Maker first, then Dev, then Exec** (constrained-fill step): ensures plain-language coherence is established before specialized framing is added. Each earlier version constrains the vocabulary permissions of the next.
3. **VERSION DIFFERENTIATION GATE** (post-verify step): verifies structural compliance at exit. Phase 5 cannot close until all gate questions reach passing state. The gate converts pre-existing advisory instructions (Core Belief distinctness from Phase 2, zero-acronym from Maker Hook/Why-It-Matters, scenario-hook from Dev Hook) into pass/fail exits -- it introduces no new constraints.

These three elements form a coherent pre-commit/fill/close envelope. All three must be present and executed in sequence. Having any two of three does not pass. Phase 5 is auditable from skill structure alone: the sequence is explicit before any draft is written.

---

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

**Draft-order integrity**: EXEC OPENING SENTENCE is locked at Phase 4, before Phase 5 begins. The Maker-first constraint-ascending order cannot weaken the exec version: EXEC OPENING SENTENCE is pre-committed by Phase 4's binary gate and the Exec Hook must use exact text regardless of draft order. Maker-first affects only which version is drafted first -- it does not change any locked output from Phases 2, 3, or 4.

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
   *(Enforces Core Belief distinctness advisory in Phase 2 Core Belief column definition.)*
2. Does the Maker version contain any unexplained acronym or CLI reference (e.g., `/scout:`, `{topic}`, namespace names)? YES / NO
   *(Enforces zero-acronym advisory in Maker Version Hook and Why-It-Matters instructions.)*
3. Does the Dev version open with a scenario (a moment the developer is in) rather than an outcome statement? YES / NO
   *(Enforces scenario-hook advisory in Dev Version Hook instruction.)*

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

## R9 Design Notes

**What changed from R8:**

R8 V-05 closed the Phase 5 structural presence gap: all three envelope elements (INERTIA PROFILE, Maker-first, DIFFERENTIATION GATE) are present and score at 100.0 on 30 criteria. R9 probes whether Phase 5 is **auditable** -- whether a reader can determine the structural pattern from the skill text alone without tracing execution. Three audibility gaps identified:

| Gap | R8 V-05 state | R9 axis |
|-----|--------------|---------|
| C-38 Envelope not named | Three elements present; no named block states their sequential relationship as a pre-commit/fill/close structure | V-01: PHASE 5 STRUCTURE declaration |
| C-39 Anchor not defended | EXEC OPENING SENTENCE named as locked; no statement that Maker-first cannot weaken it | V-02: draft-order integrity statement |
| C-40 Q1 introduces new constraint | Q2 and Q3 enforce pre-existing advisories; Q1 (Core Belief distinctness) has no prior advisory counterpart | V-03: advisory distinctness instruction in Phase 2 Core Belief column definition |

**Predicted structural effect of V-05:**

V-05 is the first variation where Phase 5 is both structurally present (R8) and structurally auditable (R9). The PHASE 5 STRUCTURE block names the pre-commit/fill/close pattern before any drafting step, making the phase auditable as a unit. The draft-order integrity statement closes the EXEC OPENING SENTENCE anchor defense, making the constraint-ascending order claim structurally unimpeachable. The Core Belief distinctness advisory in Phase 2 gives DIFFERENTIATION GATE Q1 a pre-existing constraint to convert, completing the gate-to-advisory traceability for all three questions. Together these three additions make Phase 5 auditable from skill structure alone -- the same standard Phase 2 reached with the BINDING DECLARATION in R7.
