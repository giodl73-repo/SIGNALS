`simulations/quest/variations/draft-pitch-variations-R10-2026-03-14.md` written.

---

## R10 Variations Summary

**Base**: R9 V-05 (100.0/100 on 33 criteria). R10 probes C-41, C-42, C-43 — the declaration-site precision gaps that parallel the C-27/C-25/C-24 maturation arc of the BINDING DECLARATION.

### Three gaps in R9 V-05

| Criterion | R9 V-05 state | Gap |
|-----------|--------------|-----|
| **C-41** | PHASE 5 STRUCTURE opens with pattern citation; ends with auditability declaration — 8 lines apart | Auditability intent not at the declaration site |
| **C-42** | "does not change any locked output from Phases 2, 3, or 4" — set-scope by phase number | Protected outputs not named by canonical identifier |
| **C-43** | Gate citations use descriptive phrases ("Core Belief distinctness advisory in Phase 2 Core Belief column definition") | Not exact canonical names as they appear in skill headings |

### Variation map

| ID | Axis | Targets |
|----|------|---------|
| **V-01** | Lifecycle emphasis | PHASE 5 STRUCTURE heading: "applies the Phase 2 **BINDING DECLARATION** pattern at the phase level; Phase 5 is auditable from skill structure alone" — both elements at the opening line (C-41) |
| **V-02** | Phrasing register | Draft-order integrity: "does not change **AUDIENCE BELIEF MAP** [Phase 2], **POSITIONING LOCK** [Phase 3], or **EXEC OPENING SENTENCE** [Phase 4]" — canonical names, not phase numbers (C-42) |
| **V-03** | Role sequence + inertia framing | Gate citations use exact instruction text: Q1 cites the Core Belief column text verbatim, Q2/Q3 cite Maker/Dev Hook instructions verbatim (C-43) |
| **V-04** | V-01 + V-02 | C-41 + C-42; C-43 still fails |
| **V-05** | V-01 + V-02 + V-03 | All three closed — R10 golden candidate |

The structural logic: C-41 ↔ C-27, C-42 ↔ C-25, C-43 ↔ C-24. The same three sub-patterns that matured the BINDING DECLARATION in R5/R6 now apply one tier up at the phase-structure and gate-citation level.
ings. C-43 requires each citation to name the source instruction using the exact canonical heading text. |

### Variation map

| ID | Axis | Change |
|----|------|--------|
| **V-01** | Lifecycle emphasis | PHASE 5 STRUCTURE heading and opening sentence declare auditability intent + cite BINDING DECLARATION by name -- both at the declaration site (C-41) |
| **V-02** | Phrasing register | Draft-order integrity statement enumerates all three prior-phase locked outputs by canonical name (AUDIENCE BELIEF MAP, POSITIONING LOCK, EXEC OPENING SENTENCE) as the protected set (C-42) |
| **V-03** | Role sequence + inertia framing | Gate YES/NO citations rewritten to use exact canonical instruction heading names as they appear in skill structure (C-43) |
| **V-04** | V-01 + V-02 | PHASE 5 STRUCTURE declaration + named-output enumeration (C-41 + C-42; C-43 still fails) |
| **V-05** | V-01 + V-02 + V-03 | Full synthesis -- all three declaration-site precision gaps closed; **R10 golden candidate** |

### Structural logic

R9 V-05 closed the Phase 5 structural presence gaps (C-38, C-39, C-40). R10 closes the Phase 5 declaration-site precision gaps (C-41, C-42, C-43). The pattern matches the BINDING DECLARATION maturation arc in R5/R6:
- C-41 corresponds to C-27: auditability intent at the declaration site itself
- C-42 corresponds to C-25: exhaustive named-output enumeration closing the set
- C-43 corresponds to C-24: exact canonical provenance at each cite site

V-05 completes Phase 5 declaration-site precision the same way R5/R6 completed BINDING DECLARATION precision: the opening of PHASE 5 STRUCTURE is now a self-contained auditable declaration (C-41), the draft-order integrity statement names every protected output by canonical name (C-42), and each gate citation names the source instruction by its exact heading text from the skill body (C-43).

---

## V-01 -- PHASE 5 STRUCTURE Declaration Site (C-41)

**Axis**: Lifecycle emphasis -- PHASE 5 STRUCTURE heading and opening sentence declare auditability intent + cite BINDING DECLARATION by name at the declaration site.

**Hypothesis**: C-41 requires both elements at the declaration site, not distributed across the block. R9 V-05 opens the PHASE 5 STRUCTURE block with the pattern citation and ends the block with the auditability declaration -- these are two sentences 8 lines apart. C-41 passes when both appear together at the opening: in the heading itself or in the first sentence immediately following it. V-01 moves the auditability declaration to the heading line so a reader can determine (a) that Phase 5 follows the BINDING DECLARATION pattern and (b) that Phase 5 is auditable from skill structure alone -- both without reading further into the block.

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
- **Failure Mode**: What the pitch *fails to achieve for this audience* if Core Belief is absent. Name a pitch outcome failure -- what the pitch cannot accomplish for this audience (e.g., "Exec won't authorize the demo slot," "Dev won't try the command," "Maker won't raise the question in their next meeting"). A restatement of Core Belief in negative form does not pass.
- **Inertia Excuse**: Fill from BINDING DECLARATION above. Use scout override if available; otherwise use SIGNAL DEFAULTS value exactly.
- **Inertia Counter**: The specific action that addresses this Inertia Excuse. One concrete step. Pre-commit this value -- Phase 5 CTA uses it by exact reference.

**AUDIENCE BELIEF MAP:**

| Audience | Core Belief | Failure Mode | Inertia Excuse | Inertia Counter |
|----------|-------------|--------------|----------------|-----------------|
| Exec | [Write belief -- substantively distinct from Dev and Maker beliefs] | [Name the pitch outcome failure] | [active Exec inertia from SIGNAL DEFAULTS] | [Name the counter action] |
| Dev | [Write belief -- substantively distinct from Exec and Maker beliefs] | [Name the pitch outcome failure] | [active Dev inertia from SIGNAL DEFAULTS] | [Name the counter action] |
| Maker | [Write belief -- substantively distinct from Exec and Dev beliefs] | [Name the pitch outcome failure] | [active Maker inertia from SIGNAL DEFAULTS] | [Name the counter action] |

Do not proceed until all twelve cells are filled.

**-- PHASE 2 COMPLETE. AUDIENCE BELIEF MAP is locked. --**

---

**=== PHASE 3: POSITIONING LOCK ===**

*Consumes*: Phase 1 active values.
*Produces*: **POSITIONING LOCK** (named output). Phase 5 references this output by exact name.

**POSITIONING LOCK:**

1. **Competitor**: "The real competition for teams building {topic} is not a named tool. It is ___."
2. **Outcome**: "Signal gives {primary audience} ___ before the first line of code is written."
3. **Ruling out**: Three categories Signal is NOT. Format: "[Category]. Signal does not [function]."

**-- PHASE 3 COMPLETE. POSITIONING LOCK is locked. --**

---

**=== PHASE 4: EXEC OPENING GATE ===**

*Produces*: **EXEC OPENING SENTENCE** (named output).

**Write: EXEC OPENING SENTENCE**
> [One sentence only.]

**Binary gate:** Does EXEC OPENING SENTENCE name a cost, risk, or productivity consequence teams face today -- without mentioning a feature, tool, or product?
- **YES** -- locked. Proceed to Phase 5.
- **NO** -- rewrite. Anchor in active Exec inertia. Re-apply gate. Repeat until YES.

**-- PHASE 4 COMPLETE. EXEC OPENING SENTENCE is locked. --**

---

**=== PHASE 5: FULL DRAFT ===**

*Consumes* (with provenance):
- **AUDIENCE BELIEF MAP** [Phase 2 gate output | named table | locked before Phase 5 begins]
- **POSITIONING LOCK** [Phase 3 gate output | named block | locked before Phase 5 begins]
- **EXEC OPENING SENTENCE** [Phase 4 gate output | named sentence | binary-gate verified | locked before Phase 5 begins]

**PHASE 5 STRUCTURE** -- applies the Phase 2 **BINDING DECLARATION** pattern at the phase level; Phase 5 is auditable from skill structure alone (read before any drafting step):

Phase 5 uses a pre-commit -> constrained-fill -> post-verify structure that mirrors the Phase 2 BINDING DECLARATION pattern at the phase level. The three elements below are declared here, before any draft is written, so that their sequential relationship is readable from skill structure alone without tracing execution:

1. **INERTIA PROFILE** (pre-commit step): commits each audience's inertia arc in writing before any version is drafted. Prevents post-hoc rationalization of Why-It-Matters sections.
2. **Constraint-ascending draft order -- Maker first, then Dev, then Exec** (constrained-fill step): ensures plain-language coherence is established before specialized framing is added.
3. **VERSION DIFFERENTIATION GATE** (post-verify step): verifies structural compliance at exit. Converts pre-existing advisory instructions into pass/fail exits -- introduces no new constraints.

All three must be present and executed in sequence. Having any two of three does not pass.

---

**Phase 5 INERTIA PROFILE** (complete before drafting any version):

"[Audience] currently [Inertia Excuse from AUDIENCE BELIEF MAP, [audience] row]. Signal changes this to [Inertia Counter from AUDIENCE BELIEF MAP, [audience] row]."

**INERTIA PROFILE:**
- Exec: [Write one sentence]
- Dev: [Write one sentence]
- Maker: [Write one sentence]

**-- INERTIA PROFILE COMPLETE. Do not draft any version until all three sentences are written. --**

Draft order: Maker first, then Dev, then Exec.

**Draft-order integrity**: EXEC OPENING SENTENCE is locked at Phase 4, before Phase 5 begins. Maker-first affects only which version is drafted first -- it does not change any locked output from Phases 2, 3, or 4.

**CTA construction template (all three versions)**:
> "Instead of [Inertia Excuse from AUDIENCE BELIEF MAP [Phase 2 gate output], [audience] row], [Inertia Counter from AUDIENCE BELIEF MAP [Phase 2 gate output], [audience] row]."

**Maker Version** *(draft first)*
- **Hook**: The question they have already asked themselves. Zero unexplained acronyms. Zero namespace references. Zero CLI terminology.
- **What It Does**: Plain English. Translate every Signal term to what it does for a person.
- **Why It Matters**: Inertia arc from INERTIA PROFILE Maker sentence. Maker outcome from SIGNAL DEFAULTS. No jargon.
- **Call to Action**: CTA template, maker row.

**Dev Version** *(draft second)*
- **Hook**: A scenario the developer is in right now -- the moment before Signal changes what happens next.
- **What It Does**: At least one concrete interaction. Example: `/scout:requirements topic={topic}` produces `{topic}-requirements-{date}.md`.
- **Why It Matters**: Inertia arc from INERTIA PROFILE Dev sentence. Before-state and after-state named. Dev friction from SIGNAL DEFAULTS.
- **Call to Action**: CTA template, dev row.

**Exec Version** *(draft last)*
- **Hook**: EXEC OPENING SENTENCE [Phase 4 gate output] -- use exact text, no edits.
- **What It Does**: POSITIONING LOCK [Phase 3 gate output] Outcome answer. One sentence.
- **Why It Matters**: Inertia arc from INERTIA PROFILE Exec sentence. "The alternative is not a competing product. It is [Competitor from POSITIONING LOCK]." 2-3 sentences ROI framing.
- **Call to Action**: CTA template, exec row.

**VERSION DIFFERENTIATION GATE** (complete after all three versions are drafted):

| Version | Core Belief summary (10 words max) | Hook type | Jargon check |
|---------|------------------------------------|-----------|--------------|
| Exec | [summarize] | outcome/cost/risk sentence | business framing only |
| Dev | [summarize] | scenario/moment | technical terms permitted |
| Maker | [summarize] | question/feeling | zero unexplained acronyms |

Gate questions:
1. Are the three Core Belief summaries substantively distinct (not paraphrases of each other)? YES / NO
   *(Enforces Core Belief distinctness advisory in Phase 2 Core Belief column definition.)*
2. Does the Maker version contain any unexplained acronym or CLI reference? YES / NO
   *(Enforces zero-acronym advisory in Maker Version Hook and Why-It-Matters instructions.)*
3. Does the Dev version open with a scenario rather than an outcome statement? YES / NO
   *(Enforces scenario-hook advisory in Dev Version Hook instruction.)*

Passing state: Q1=YES, Q2=NO, Q3=YES. Rewrite and re-gate any failing version.

**-- PHASE 5 COMPLETE. --**

---

**=== PHASE 6: ANTI-POSITIONING ===**

Write "## What Signal Is NOT" from POSITIONING LOCK Ruling Out values. Add one additional adjacent category. Minimum four bullets. Format: `[Category]. Signal does not [specific function]. [One sentence on why this distinction matters for {topic} specifically.]`

**-- PHASE 6 COMPLETE. --**

---

**=== PHASE 7: PROOF AUDIT ===**

For every factual claim in exec and dev versions: `[source: {artifact-path}]`, `[source: prior signal]`, or `[UNVERIFIED]` -- replace UNVERIFIED with hedged language or Proof fallback before saving.

**-- PHASE 7 COMPLETE. --**

---

**Output format**: `## Exec Version` / `## Dev Version` / `## Maker Version` / `## What Signal Is NOT`

Phase outputs are working notes -- not in saved artifact.

**Save to**: `simulations/draft/pitches/{topic}-pitch-{date}.md`

---

## V-02 -- Draft-Order Integrity Named Set (C-42)

**Axis**: Phrasing register -- draft-order integrity statement enumerates all three prior-phase locked outputs by canonical name as the protected set.

**Hypothesis**: C-42 requires the draft-order integrity statement to name the protected outputs explicitly -- not by phase number but by their canonical identifiers (AUDIENCE BELIEF MAP, POSITIONING LOCK, EXEC OPENING SENTENCE). R9 V-05 says "does not change any locked output from Phases 2, 3, or 4" -- set-scope form (C-39 passes) but uses phase numbers rather than canonical names. A reader who has not memorized which phase produces which output cannot determine what is protected from the draft-order integrity statement alone. V-02 names all three locked outputs by their exact canonical identifiers, making the set legible without cross-referencing the phase headers.

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

**Phase 1 output**: active values table.

**-- PHASE 1 COMPLETE. --**

---

**=== PHASE 2: BELIEF MAP ===**

*Produces*: **AUDIENCE BELIEF MAP** (named output).

**PHASE 2 BINDING DECLARATION** (read before filling the table):

| SIGNAL DEFAULTS field | Bound to | AUDIENCE BELIEF MAP column |
|----------------------|----------|---------------------------|
| Exec inertia | -> | Inertia Excuse, Exec row |
| Dev inertia | -> | Inertia Excuse, Dev row |
| Maker inertia | -> | Inertia Excuse, Maker row |

AUDIENCE BELIEF MAP is the authoritative source for all Phase 5 CTA inertia references.

Column definitions:
- **Core Belief**: The one thing this audience must believe first. Substantively distinct from the other two. A paraphrase does not pass.
- **Failure Mode**: What the pitch fails to achieve if Core Belief is absent. A restatement in negative form does not pass.
- **Inertia Excuse**: From BINDING DECLARATION above. Use scout override or SIGNAL DEFAULTS value exactly.
- **Inertia Counter**: One concrete counter action. Pre-committed for Phase 5 CTA reference.

**AUDIENCE BELIEF MAP:**

| Audience | Core Belief | Failure Mode | Inertia Excuse | Inertia Counter |
|----------|-------------|--------------|----------------|-----------------|
| Exec | [distinct from Dev and Maker] | [pitch outcome failure] | [active Exec inertia] | [counter action] |
| Dev | [distinct from Exec and Maker] | [pitch outcome failure] | [active Dev inertia] | [counter action] |
| Maker | [distinct from Exec and Dev] | [pitch outcome failure] | [active Maker inertia] | [counter action] |

**-- PHASE 2 COMPLETE. AUDIENCE BELIEF MAP is locked. --**

---

**=== PHASE 3: POSITIONING LOCK ===**

*Produces*: **POSITIONING LOCK** (named output).

**POSITIONING LOCK:**

1. **Competitor**: "The real competition is not a named tool. It is ___."
2. **Outcome**: "Signal gives {primary audience} ___ before the first line of code is written."
3. **Ruling out**: Three categories. Format: "[Category]. Signal does not [function]."

**-- PHASE 3 COMPLETE. POSITIONING LOCK is locked. --**

---

**=== PHASE 4: EXEC OPENING GATE ===**

*Produces*: **EXEC OPENING SENTENCE** (named output).

Write one sentence. Binary gate: names a cost, risk, or productivity consequence -- no feature, tool, or product mention. YES = locked. NO = rewrite and re-gate.

**-- PHASE 4 COMPLETE. EXEC OPENING SENTENCE is locked. --**

---

**=== PHASE 5: FULL DRAFT ===**

*Consumes* (with provenance):
- **AUDIENCE BELIEF MAP** [Phase 2 gate output | named table | locked before Phase 5 begins]
- **POSITIONING LOCK** [Phase 3 gate output | named block | locked before Phase 5 begins]
- **EXEC OPENING SENTENCE** [Phase 4 gate output | named sentence | binary-gate verified | locked before Phase 5 begins]

**PHASE 5 STRUCTURE** (read before any drafting step):

Phase 5 uses a pre-commit -> constrained-fill -> post-verify structure that mirrors the Phase 2 BINDING DECLARATION pattern:

1. **INERTIA PROFILE** (pre-commit step): commits each audience's inertia arc in writing before any version is drafted.
2. **Constraint-ascending draft order -- Maker first, then Dev, then Exec** (constrained-fill step): plain-language coherence established before specialized framing added.
3. **VERSION DIFFERENTIATION GATE** (post-verify step): structural compliance check at exit. Converts pre-existing advisories into pass/fail exits -- no new constraints introduced.

All three must be present and executed in sequence. Having any two of three does not pass. Phase 5 is auditable from skill structure alone: the sequence is explicit before any draft is written.

---

**Phase 5 INERTIA PROFILE** (complete before drafting any version):

"[Audience] currently [Inertia Excuse from AUDIENCE BELIEF MAP, [audience] row]. Signal changes this to [Inertia Counter from AUDIENCE BELIEF MAP, [audience] row]."

- Exec: [Write one sentence]
- Dev: [Write one sentence]
- Maker: [Write one sentence]

**-- INERTIA PROFILE COMPLETE. Do not draft any version until all three sentences are written. --**

Draft order: Maker first, then Dev, then Exec.

**Draft-order integrity**: EXEC OPENING SENTENCE is locked at Phase 4, before Phase 5 begins. The Maker-first constraint-ascending order cannot weaken the exec version: EXEC OPENING SENTENCE is pre-committed by Phase 4's binary gate and the Exec Hook must use exact text regardless of draft order. Maker-first affects only which version is drafted first -- it does not change **AUDIENCE BELIEF MAP** [Phase 2 locked output], **POSITIONING LOCK** [Phase 3 locked output], or **EXEC OPENING SENTENCE** [Phase 4 locked output]. All three prior-phase locked outputs are unaffected by draft order.

**CTA construction template (all three versions)**:
> "Instead of [Inertia Excuse from AUDIENCE BELIEF MAP [Phase 2 gate output], [audience] row], [Inertia Counter from AUDIENCE BELIEF MAP [Phase 2 gate output], [audience] row]."

**Maker Version** *(draft first)*
- **Hook**: The question they have already asked themselves. Zero unexplained acronyms. Zero namespace references. Zero CLI terminology.
- **What It Does**: Plain English. Translate every Signal term to what it does for a person.
- **Why It Matters**: Inertia arc from INERTIA PROFILE Maker sentence. Maker outcome from SIGNAL DEFAULTS. No jargon.
- **Call to Action**: CTA template, maker row.

**Dev Version** *(draft second)*
- **Hook**: A scenario the developer is in right now -- the moment before Signal changes what happens next.
- **What It Does**: At least one concrete interaction. Example: `/scout:requirements topic={topic}` produces `{topic}-requirements-{date}.md`.
- **Why It Matters**: Inertia arc from INERTIA PROFILE Dev sentence. Before-state and after-state named. Dev friction from SIGNAL DEFAULTS.
- **Call to Action**: CTA template, dev row.

**Exec Version** *(draft last)*
- **Hook**: EXEC OPENING SENTENCE [Phase 4 gate output] -- exact text, no edits.
- **What It Does**: POSITIONING LOCK [Phase 3 gate output] Outcome answer. One sentence.
- **Why It Matters**: Inertia arc from INERTIA PROFILE Exec sentence. "The alternative is not a competing product. It is [Competitor from POSITIONING LOCK]." 2-3 sentences ROI framing.
- **Call to Action**: CTA template, exec row.

**VERSION DIFFERENTIATION GATE** (complete after all three versions are drafted):

| Version | Core Belief summary (10 words max) | Hook type | Jargon check |
|---------|------------------------------------|-----------|--------------|
| Exec | [summarize] | outcome/cost/risk sentence | business framing only |
| Dev | [summarize] | scenario/moment | technical terms permitted |
| Maker | [summarize] | question/feeling | zero unexplained acronyms |

Gate questions:
1. Are the three Core Belief summaries substantively distinct? YES / NO
   *(Enforces Core Belief distinctness advisory in Phase 2 Core Belief column definition.)*
2. Does the Maker version contain any unexplained acronym or CLI reference? YES / NO
   *(Enforces zero-acronym advisory in Maker Version Hook and Why-It-Matters instructions.)*
3. Does the Dev version open with a scenario rather than an outcome statement? YES / NO
   *(Enforces scenario-hook advisory in Dev Version Hook instruction.)*

Passing state: Q1=YES, Q2=NO, Q3=YES. Rewrite and re-gate any failing version.

**-- PHASE 5 COMPLETE. --**

---

**=== PHASE 6: ANTI-POSITIONING ===**

Write "## What Signal Is NOT" from POSITIONING LOCK Ruling Out values. Add one additional adjacent category. Minimum four bullets. Format: `[Category]. Signal does not [specific function]. [One sentence on why this distinction matters for {topic} specifically.]`

**-- PHASE 6 COMPLETE. --**

---

**=== PHASE 7: PROOF AUDIT ===**

For every factual claim in exec and dev versions: `[source: {artifact-path}]`, `[source: prior signal]`, or `[UNVERIFIED]` -- replace UNVERIFIED before saving.

**-- PHASE 7 COMPLETE. --**

---

**Output format**: `## Exec Version` / `## Dev Version` / `## Maker Version` / `## What Signal Is NOT`

Phase outputs are working notes -- not in saved artifact.

**Save to**: `simulations/draft/pitches/{topic}-pitch-{date}.md`

---

## V-03 -- Gate Citations Use Exact Canonical Names (C-43)

**Axis**: Role sequence + inertia framing -- gate YES/NO citations replaced with exact canonical instruction heading names as they appear in the skill body.

**Hypothesis**: C-43 requires each gate citation to name the source instruction using its exact canonical name as it appears in skill structure -- not a descriptive phrase, not a category label. R9 V-05 citations say "Core Belief distinctness advisory in Phase 2 Core Belief column definition," "zero-acronym advisory in Maker Version Hook and Why-It-Matters instructions," and "scenario-hook advisory in Dev Version Hook instruction." These are descriptive paraphrases. The exact canonical names from the skill body are the verbatim instruction text at the advisory site: the Core Belief column definition states "Each Core Belief must be substantively distinct from the other two"; the Maker Version Hook states "Zero unexplained acronyms. Zero namespace references. Zero CLI terminology."; the Dev Version Hook states "A scenario the developer is in right now -- the moment before Signal changes what happens next." V-03 replaces the paraphrase citations with exact-text citations so a reader can verify the cite site matches the source site without interpretation.

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

**Phase 1 output**: active values table.

**-- PHASE 1 COMPLETE. --**

---

**=== PHASE 2: BELIEF MAP ===**

*Produces*: **AUDIENCE BELIEF MAP** (named output).

**PHASE 2 BINDING DECLARATION** (read before filling the table):

| SIGNAL DEFAULTS field | Bound to | AUDIENCE BELIEF MAP column |
|----------------------|----------|---------------------------|
| Exec inertia | -> | Inertia Excuse, Exec row |
| Dev inertia | -> | Inertia Excuse, Dev row |
| Maker inertia | -> | Inertia Excuse, Maker row |

AUDIENCE BELIEF MAP is the authoritative source for all Phase 5 CTA inertia references.

Column definitions:
- **Core Belief**: The one thing this audience must believe first. Each Core Belief must be substantively distinct from the other two -- naming a claim that belongs specifically to this audience and could not serve as the primary belief anchor for a different audience. A Core Belief that paraphrases another audience's Core Belief does not pass.
- **Failure Mode**: What the pitch fails to achieve if Core Belief is absent. A restatement in negative form does not pass.
- **Inertia Excuse**: From BINDING DECLARATION above.
- **Inertia Counter**: One concrete counter action. Pre-committed for Phase 5 CTA reference.

**AUDIENCE BELIEF MAP:**

| Audience | Core Belief | Failure Mode | Inertia Excuse | Inertia Counter |
|----------|-------------|--------------|----------------|-----------------|
| Exec | [distinct from Dev and Maker] | [pitch outcome failure] | [active Exec inertia] | [counter action] |
| Dev | [distinct from Exec and Maker] | [pitch outcome failure] | [active Dev inertia] | [counter action] |
| Maker | [distinct from Exec and Dev] | [pitch outcome failure] | [active Maker inertia] | [counter action] |

**-- PHASE 2 COMPLETE. AUDIENCE BELIEF MAP is locked. --**

---

**=== PHASE 3: POSITIONING LOCK ===**

*Produces*: **POSITIONING LOCK** (named output).

**POSITIONING LOCK:**

1. **Competitor**: "The real competition is not a named tool. It is ___."
2. **Outcome**: "Signal gives {primary audience} ___ before the first line of code is written."
3. **Ruling out**: Three categories. Format: "[Category]. Signal does not [function]."

**-- PHASE 3 COMPLETE. POSITIONING LOCK is locked. --**

---

**=== PHASE 4: EXEC OPENING GATE ===**

*Produces*: **EXEC OPENING SENTENCE** (named output).

Write one sentence. Binary gate: names a cost, risk, or productivity consequence -- no feature, tool, or product mention. YES = locked. NO = rewrite and re-gate.

**-- PHASE 4 COMPLETE. EXEC OPENING SENTENCE is locked. --**

---

**=== PHASE 5: FULL DRAFT ===**

*Consumes* (with provenance):
- **AUDIENCE BELIEF MAP** [Phase 2 gate output | named table | locked before Phase 5 begins]
- **POSITIONING LOCK** [Phase 3 gate output | named block | locked before Phase 5 begins]
- **EXEC OPENING SENTENCE** [Phase 4 gate output | named sentence | binary-gate verified | locked before Phase 5 begins]

**PHASE 5 STRUCTURE** (read before any drafting step):

Phase 5 uses a pre-commit -> constrained-fill -> post-verify structure that mirrors the Phase 2 BINDING DECLARATION pattern:

1. **INERTIA PROFILE** (pre-commit step): commits each audience's inertia arc in writing before any version is drafted.
2. **Constraint-ascending draft order -- Maker first, then Dev, then Exec** (constrained-fill step): plain-language coherence established before specialized framing added.
3. **VERSION DIFFERENTIATION GATE** (post-verify step): structural compliance check at exit. Converts pre-existing advisories into pass/fail exits -- no new constraints introduced.

All three must be present and executed in sequence. Phase 5 is auditable from skill structure alone: the sequence is explicit before any draft is written.

---

**Phase 5 INERTIA PROFILE** (complete before drafting any version):

"[Audience] currently [Inertia Excuse from AUDIENCE BELIEF MAP, [audience] row]. Signal changes this to [Inertia Counter from AUDIENCE BELIEF MAP, [audience] row]."

- Exec: [Write one sentence]
- Dev: [Write one sentence]
- Maker: [Write one sentence]

**-- INERTIA PROFILE COMPLETE. Do not draft any version until all three sentences are written. --**

Draft order: Maker first, then Dev, then Exec.

**Draft-order integrity**: EXEC OPENING SENTENCE is locked at Phase 4, before Phase 5 begins. Maker-first affects only which version is drafted first -- it does not change any locked output from Phases 2, 3, or 4.

**CTA construction template (all three versions)**:
> "Instead of [Inertia Excuse from AUDIENCE BELIEF MAP [Phase 2 gate output], [audience] row], [Inertia Counter from AUDIENCE BELIEF MAP [Phase 2 gate output], [audience] row]."

**Maker Version** *(draft first)*
- **Hook**: The question they have already asked themselves. Zero unexplained acronyms. Zero namespace references. Zero CLI terminology.
- **What It Does**: Plain English. Translate every Signal term to what it does for a person.
- **Why It Matters**: Inertia arc from INERTIA PROFILE Maker sentence. Maker outcome from SIGNAL DEFAULTS. No jargon.
- **Call to Action**: CTA template, maker row.

**Dev Version** *(draft second)*
- **Hook**: A scenario the developer is in right now -- the moment before Signal changes what happens next.
- **What It Does**: At least one concrete interaction. Example: `/scout:requirements topic={topic}` produces `{topic}-requirements-{date}.md`.
- **Why It Matters**: Inertia arc from INERTIA PROFILE Dev sentence. Before-state and after-state named. Dev friction from SIGNAL DEFAULTS.
- **Call to Action**: CTA template, dev row.

**Exec Version** *(draft last)*
- **Hook**: EXEC OPENING SENTENCE [Phase 4 gate output] -- exact text, no edits.
- **What It Does**: POSITIONING LOCK [Phase 3 gate output] Outcome answer. One sentence.
- **Why It Matters**: Inertia arc from INERTIA PROFILE Exec sentence. "The alternative is not a competing product. It is [Competitor from POSITIONING LOCK]." 2-3 sentences ROI framing.
- **Call to Action**: CTA template, exec row.

**VERSION DIFFERENTIATION GATE** (complete after all three versions are drafted):

| Version | Core Belief summary (10 words max) | Hook type | Jargon check |
|---------|------------------------------------|-----------|--------------|
| Exec | [summarize] | outcome/cost/risk sentence | business framing only |
| Dev | [summarize] | scenario/moment | technical terms permitted |
| Maker | [summarize] | question/feeling | zero unexplained acronyms |

Gate questions:
1. Are the three Core Belief summaries substantively distinct (not paraphrases of each other)? YES / NO
   *(Enforces advisory at AUDIENCE BELIEF MAP Core Belief column: "Each Core Belief must be substantively distinct from the other two -- naming a claim that belongs specifically to this audience and could not serve as the primary belief anchor for a different audience.")*
2. Does the Maker version contain any unexplained acronym or CLI reference? YES / NO
   *(Enforces advisory at Maker Version Hook: "Zero unexplained acronyms. Zero namespace references. Zero CLI terminology.")*
3. Does the Dev version open with a scenario rather than an outcome statement? YES / NO
   *(Enforces advisory at Dev Version Hook: "A scenario the developer is in right now -- the moment before Signal changes what happens next.")*

Passing state: Q1=YES, Q2=NO, Q3=YES. Rewrite and re-gate any failing version.

**-- PHASE 5 COMPLETE. --**

---

**=== PHASE 6: ANTI-POSITIONING ===**

Write "## What Signal Is NOT" from POSITIONING LOCK Ruling Out values. Add one additional adjacent category. Minimum four bullets. Format: `[Category]. Signal does not [specific function]. [One sentence on why this distinction matters for {topic} specifically.]`

**-- PHASE 6 COMPLETE. --**

---

**=== PHASE 7: PROOF AUDIT ===**

For every factual claim in exec and dev versions: `[source: {artifact-path}]`, `[source: prior signal]`, or `[UNVERIFIED]` -- replace UNVERIFIED before saving.

**-- PHASE 7 COMPLETE. --**

---

**Output format**: `## Exec Version` / `## Dev Version` / `## Maker Version` / `## What Signal Is NOT`

Phase outputs are working notes -- not in saved artifact.

**Save to**: `simulations/draft/pitches/{topic}-pitch-{date}.md`

---

## V-04 -- PHASE 5 STRUCTURE Declaration + Named Set (C-41 + C-42)

**Axes**: Lifecycle emphasis + phrasing register -- PHASE 5 STRUCTURE declaration site update + draft-order integrity named enumeration. C-41 and C-42 close; C-43 still fails.

**Hypothesis**: C-41 and C-42 are the two structural declaration gaps. V-04 closes both: the PHASE 5 STRUCTURE heading declares auditability intent and cites BINDING DECLARATION at the opening, and the draft-order integrity statement names all three prior-phase locked outputs by canonical identifier. A reader can determine from the PHASE 5 STRUCTURE heading alone that Phase 5 is auditable, and from the draft-order integrity statement alone which exact outputs are protected -- without reading elsewhere in the skill. C-43 is not addressed: gate citations remain in descriptive-phrase form.

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

**Phase 1 output**: active values table.

**-- PHASE 1 COMPLETE. --**

---

**=== PHASE 2: BELIEF MAP ===**

*Produces*: **AUDIENCE BELIEF MAP** (named output).

**PHASE 2 BINDING DECLARATION** (read before filling the table):

| SIGNAL DEFAULTS field | Bound to | AUDIENCE BELIEF MAP column |
|----------------------|----------|---------------------------|
| Exec inertia | -> | Inertia Excuse, Exec row |
| Dev inertia | -> | Inertia Excuse, Dev row |
| Maker inertia | -> | Inertia Excuse, Maker row |

AUDIENCE BELIEF MAP is the authoritative source for all Phase 5 CTA inertia references.

Column definitions:
- **Core Belief**: Substantively distinct from the other two. A paraphrase does not pass.
- **Failure Mode**: Pitch outcome failure if Core Belief absent. A restatement in negative form does not pass.
- **Inertia Excuse**: From BINDING DECLARATION above.
- **Inertia Counter**: Pre-committed for Phase 5 CTA reference.

**AUDIENCE BELIEF MAP:**

| Audience | Core Belief | Failure Mode | Inertia Excuse | Inertia Counter |
|----------|-------------|--------------|----------------|-----------------|
| Exec | [distinct] | [pitch failure] | [active Exec inertia] | [counter] |
| Dev | [distinct] | [pitch failure] | [active Dev inertia] | [counter] |
| Maker | [distinct] | [pitch failure] | [active Maker inertia] | [counter] |

**-- PHASE 2 COMPLETE. AUDIENCE BELIEF MAP is locked. --**

---

**=== PHASE 3: POSITIONING LOCK ===**

*Produces*: **POSITIONING LOCK** (named output).

**POSITIONING LOCK:**

1. **Competitor**: "The real competition is not a named tool. It is ___."
2. **Outcome**: "Signal gives {primary audience} ___ before the first line of code is written."
3. **Ruling out**: Three categories. Format: "[Category]. Signal does not [function]."

**-- PHASE 3 COMPLETE. POSITIONING LOCK is locked. --**

---

**=== PHASE 4: EXEC OPENING GATE ===**

*Produces*: **EXEC OPENING SENTENCE** (named output).

Write one sentence. Binary gate: cost/risk/productivity consequence -- no feature, tool, or product mention. YES = locked. NO = rewrite and re-gate.

**-- PHASE 4 COMPLETE. EXEC OPENING SENTENCE is locked. --**

---

**=== PHASE 5: FULL DRAFT ===**

*Consumes* (with provenance):
- **AUDIENCE BELIEF MAP** [Phase 2 gate output | named table | locked before Phase 5 begins]
- **POSITIONING LOCK** [Phase 3 gate output | named block | locked before Phase 5 begins]
- **EXEC OPENING SENTENCE** [Phase 4 gate output | named sentence | binary-gate verified | locked before Phase 5 begins]

**PHASE 5 STRUCTURE** -- applies the Phase 2 **BINDING DECLARATION** pattern at the phase level; Phase 5 is auditable from skill structure alone (read before any drafting step):

Phase 5 uses a pre-commit -> constrained-fill -> post-verify structure that mirrors the Phase 2 BINDING DECLARATION pattern at the phase level. The three elements below are declared here, before any draft is written, so that their sequential relationship is readable from skill structure alone without tracing execution:

1. **INERTIA PROFILE** (pre-commit step): commits each audience's inertia arc before any version is drafted.
2. **Constraint-ascending draft order -- Maker first, then Dev, then Exec** (constrained-fill step): plain-language coherence before specialized framing.
3. **VERSION DIFFERENTIATION GATE** (post-verify step): compliance check at exit. Converts pre-existing advisories into pass/fail exits -- no new constraints.

All three must be present and executed in sequence. Having any two of three does not pass.

---

**Phase 5 INERTIA PROFILE** (complete before drafting any version):

"[Audience] currently [Inertia Excuse from AUDIENCE BELIEF MAP, [audience] row]. Signal changes this to [Inertia Counter from AUDIENCE BELIEF MAP, [audience] row]."

- Exec: [Write one sentence]
- Dev: [Write one sentence]
- Maker: [Write one sentence]

**-- INERTIA PROFILE COMPLETE. Do not draft any version until all three sentences are written. --**

Draft order: Maker first, then Dev, then Exec.

**Draft-order integrity**: EXEC OPENING SENTENCE is locked at Phase 4, before Phase 5 begins. Maker-first affects only which version is drafted first -- it does not change **AUDIENCE BELIEF MAP** [Phase 2 locked output], **POSITIONING LOCK** [Phase 3 locked output], or **EXEC OPENING SENTENCE** [Phase 4 locked output]. All three prior-phase locked outputs are unaffected by draft order.

**CTA construction template (all three versions)**:
> "Instead of [Inertia Excuse from AUDIENCE BELIEF MAP [Phase 2 gate output], [audience] row], [Inertia Counter from AUDIENCE BELIEF MAP [Phase 2 gate output], [audience] row]."

**Maker Version** *(draft first)*
- **Hook**: The question they have already asked themselves. Zero unexplained acronyms. Zero namespace references. Zero CLI terminology.
- **What It Does**: Plain English. Translate every Signal term to what it does for a person.
- **Why It Matters**: Inertia arc from INERTIA PROFILE Maker sentence. Maker outcome from SIGNAL DEFAULTS. No jargon.
- **Call to Action**: CTA template, maker row.

**Dev Version** *(draft second)*
- **Hook**: A scenario the developer is in right now -- the moment before Signal changes what happens next.
- **What It Does**: At least one concrete interaction. Example: `/scout:requirements topic={topic}` produces `{topic}-requirements-{date}.md`.
- **Why It Matters**: Inertia arc from INERTIA PROFILE Dev sentence. Before-state and after-state named. Dev friction from SIGNAL DEFAULTS.
- **Call to Action**: CTA template, dev row.

**Exec Version** *(draft last)*
- **Hook**: EXEC OPENING SENTENCE [Phase 4 gate output] -- exact text, no edits.
- **What It Does**: POSITIONING LOCK [Phase 3 gate output] Outcome answer. One sentence.
- **Why It Matters**: Inertia arc from INERTIA PROFILE Exec sentence. "The alternative is not a competing product. It is [Competitor from POSITIONING LOCK]." 2-3 sentences ROI framing.
- **Call to Action**: CTA template, exec row.

**VERSION DIFFERENTIATION GATE** (complete after all three versions are drafted):

| Version | Core Belief summary (10 words max) | Hook type | Jargon check |
|---------|------------------------------------|-----------|--------------|
| Exec | [summarize] | outcome/cost/risk sentence | business framing only |
| Dev | [summarize] | scenario/moment | technical terms permitted |
| Maker | [summarize] | question/feeling | zero unexplained acronyms |

Gate questions:
1. Are the three Core Belief summaries substantively distinct? YES / NO
   *(Enforces Core Belief distinctness advisory in Phase 2 Core Belief column definition.)*
2. Does the Maker version contain any unexplained acronym or CLI reference? YES / NO
   *(Enforces zero-acronym advisory in Maker Version Hook and Why-It-Matters instructions.)*
3. Does the Dev version open with a scenario rather than an outcome statement? YES / NO
   *(Enforces scenario-hook advisory in Dev Version Hook instruction.)*

Passing state: Q1=YES, Q2=NO, Q3=YES. Rewrite and re-gate any failing version.

**-- PHASE 5 COMPLETE. --**

---

**=== PHASE 6: ANTI-POSITIONING ===**

Write "## What Signal Is NOT" from POSITIONING LOCK Ruling Out values. Add one additional adjacent category. Minimum four bullets. Format: `[Category]. Signal does not [specific function]. [One sentence on why this distinction matters for {topic} specifically.]`

**-- PHASE 6 COMPLETE. --**

---

**=== PHASE 7: PROOF AUDIT ===**

For every factual claim in exec and dev versions: `[source: {artifact-path}]`, `[source: prior signal]`, or `[UNVERIFIED]` -- replace UNVERIFIED before saving.

**-- PHASE 7 COMPLETE. --**

---

**Output format**: `## Exec Version` / `## Dev Version` / `## Maker Version` / `## What Signal Is NOT`

Phase outputs are working notes -- not in saved artifact.

**Save to**: `simulations/draft/pitches/{topic}-pitch-{date}.md`

---

## V-05 -- Full Synthesis (C-41 + C-42 + C-43)

**Axes**: Lifecycle emphasis + phrasing register + role sequence -- PHASE 5 STRUCTURE declaration site + draft-order integrity named enumeration + gate exact canonical citations. R10 golden candidate.

**Hypothesis**: C-41, C-42, and C-43 are the three declaration-site precision gaps that parallel the C-27/C-25/C-24 maturation arc of the BINDING DECLARATION in R5/R6. V-05 closes all three simultaneously. The PHASE 5 STRUCTURE heading states "applies the Phase 2 BINDING DECLARATION pattern at the phase level; Phase 5 is auditable from skill structure alone" -- both elements at the declaration site (C-41). The draft-order integrity statement names AUDIENCE BELIEF MAP, POSITIONING LOCK, and EXEC OPENING SENTENCE explicitly as the protected set (C-42). Each gate question cites its source advisory by the exact canonical instruction text as it appears in the skill body (C-43). Together these three additions make Phase 5 declaration-site precision match Phase 2 declaration-site precision: the same standard the BINDING DECLARATION reached in R5/R6 now applies at the phase-structure and gate-citation level.

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

**Phase 1 output**: active values table.

**-- PHASE 1 COMPLETE. Do not proceed until active values are written. --**

---

**=== PHASE 2: BELIEF MAP ===**

*Consumes*: Phase 1 active values.
*Produces*: **AUDIENCE BELIEF MAP** (named output). Phase 5 references this output by exact name.

**PHASE 2 BINDING DECLARATION** (read before filling the table):

The following SIGNAL DEFAULTS fields are bound to AUDIENCE BELIEF MAP columns. This binding applies before any row is filled.

| SIGNAL DEFAULTS field | Bound to | AUDIENCE BELIEF MAP column |
|----------------------|----------|---------------------------|
| Exec inertia | -> | Inertia Excuse, Exec row |
| Dev inertia | -> | Inertia Excuse, Dev row |
| Maker inertia | -> | Inertia Excuse, Maker row |

AUDIENCE BELIEF MAP is the authoritative source for all Phase 5 CTA inertia references.

Column definitions:
- **Core Belief**: The one thing this audience must believe first. Each Core Belief must be substantively distinct from the other two -- naming a claim that belongs specifically to this audience and could not serve as the primary belief anchor for a different audience. A Core Belief that paraphrases another audience's Core Belief does not pass.
- **Failure Mode**: What the pitch fails to achieve if Core Belief is absent. A restatement in negative form does not pass.
- **Inertia Excuse**: From BINDING DECLARATION above.
- **Inertia Counter**: One concrete counter action. Pre-committed for Phase 5 CTA reference.

**AUDIENCE BELIEF MAP:**

| Audience | Core Belief | Failure Mode | Inertia Excuse | Inertia Counter |
|----------|-------------|--------------|----------------|-----------------|
| Exec | [distinct from Dev and Maker] | [pitch outcome failure] | [active Exec inertia] | [counter action] |
| Dev | [distinct from Exec and Maker] | [pitch outcome failure] | [active Dev inertia] | [counter action] |
| Maker | [distinct from Exec and Dev] | [pitch outcome failure] | [active Maker inertia] | [counter action] |

**-- PHASE 2 COMPLETE. AUDIENCE BELIEF MAP is locked. Do not proceed until all rows are filled. --**

---

**=== PHASE 3: POSITIONING LOCK ===**

*Produces*: **POSITIONING LOCK** (named output). Phase 5 references this output by exact name.

**POSITIONING LOCK:**

1. **Competitor**: "The real competition for teams building {topic} is not a named tool. It is ___."
2. **Outcome**: "Signal gives {primary audience} ___ before the first line of code is written."
3. **Ruling out**: Three categories. Format: "[Category]. Signal does not [function]."

**-- PHASE 3 COMPLETE. POSITIONING LOCK is locked. --**

---

**=== PHASE 4: EXEC OPENING GATE ===**

*Produces*: **EXEC OPENING SENTENCE** (named output). Phase 5 exec Hook references this output by exact name.

Write one sentence. Binary gate: names a cost, risk, or productivity consequence -- without mentioning a feature, tool, or product. YES = locked. NO = rewrite and re-gate.

**-- PHASE 4 COMPLETE. EXEC OPENING SENTENCE is locked. --**

---

**=== PHASE 5: FULL DRAFT ===**

*Consumes* (with provenance):
- **AUDIENCE BELIEF MAP** [Phase 2 gate output | named table | locked before Phase 5 begins]
- **POSITIONING LOCK** [Phase 3 gate output | named block | locked before Phase 5 begins]
- **EXEC OPENING SENTENCE** [Phase 4 gate output | named sentence | binary-gate verified | locked before Phase 5 begins]

**PHASE 5 STRUCTURE** -- applies the Phase 2 **BINDING DECLARATION** pattern at the phase level; Phase 5 is auditable from skill structure alone (read before any drafting step):

Phase 5 uses a pre-commit -> constrained-fill -> post-verify structure that mirrors the Phase 2 BINDING DECLARATION pattern at the phase level. The three elements below are declared here, before any draft is written, so that their sequential relationship is readable from skill structure alone without tracing execution:

1. **INERTIA PROFILE** (pre-commit step): commits each audience's inertia arc in writing before any version is drafted. Prevents post-hoc rationalization of Why-It-Matters sections.
2. **Constraint-ascending draft order -- Maker first, then Dev, then Exec** (constrained-fill step): plain-language coherence established before specialized framing added. Each earlier version constrains vocabulary permissions of the next.
3. **VERSION DIFFERENTIATION GATE** (post-verify step): structural compliance check at exit. Converts pre-existing advisories into pass/fail exits -- introduces no new constraints.

All three must be present and executed in sequence. Having any two of three does not pass.

---

**Phase 5 INERTIA PROFILE** (complete before drafting any version):

"[Audience] currently [Inertia Excuse from AUDIENCE BELIEF MAP [Phase 2 gate output], [audience] row]. Signal changes this to [Inertia Counter from AUDIENCE BELIEF MAP [Phase 2 gate output], [audience] row]."

**INERTIA PROFILE:**
- Exec: [Write one sentence]
- Dev: [Write one sentence]
- Maker: [Write one sentence]

**-- INERTIA PROFILE COMPLETE. Do not draft any version until all three sentences are written. --**

Draft order: Maker first, then Dev, then Exec.

**Draft-order integrity**: EXEC OPENING SENTENCE is locked at Phase 4, before Phase 5 begins. The Maker-first constraint-ascending order cannot weaken the exec version: EXEC OPENING SENTENCE is pre-committed by Phase 4's binary gate and the Exec Hook must use exact text regardless of draft order. Maker-first affects only which version is drafted first -- it does not change **AUDIENCE BELIEF MAP** [Phase 2 locked output], **POSITIONING LOCK** [Phase 3 locked output], or **EXEC OPENING SENTENCE** [Phase 4 locked output]. All three prior-phase locked outputs are unaffected by draft order.

**CTA construction template (all three versions)**:
> "Instead of [Inertia Excuse from AUDIENCE BELIEF MAP [Phase 2 gate output], [audience] row], [Inertia Counter from AUDIENCE BELIEF MAP [Phase 2 gate output], [audience] row]."

**Maker Version** *(draft first)*
- **Hook**: The question they have already asked themselves. Zero unexplained acronyms. Zero namespace references. Zero CLI terminology.
- **What It Does**: Plain English. Translate every Signal term to what it does for a person.
- **Why It Matters**: Inertia arc from INERTIA PROFILE Maker sentence. Maker outcome from SIGNAL DEFAULTS. No jargon.
- **Call to Action**: CTA template, maker row.

**Dev Version** *(draft second)*
- **Hook**: A scenario the developer is in right now -- the moment before Signal changes what happens next.
- **What It Does**: At least one concrete interaction. Example: `/scout:requirements topic={topic}` produces `{topic}-requirements-{date}.md`.
- **Why It Matters**: Inertia arc from INERTIA PROFILE Dev sentence. Before-state and after-state named. Dev friction from SIGNAL DEFAULTS.
- **Call to Action**: CTA template, dev row.

**Exec Version** *(draft last)*
- **Hook**: EXEC OPENING SENTENCE [Phase 4 gate output | binary-gate verified | locked before Phase 5 begins] -- use exact text, no edits.
- **What It Does**: POSITIONING LOCK [Phase 3 gate output] Outcome answer. One sentence.
- **Why It Matters**: Inertia arc from INERTIA PROFILE Exec sentence. "The alternative is not a competing product. It is [Competitor from POSITIONING LOCK]." 2-3 sentences ROI framing.
- **Call to Action**: CTA template, exec row.

**VERSION DIFFERENTIATION GATE** (complete after all three versions are drafted):

| Version | Core Belief summary (10 words max) | Hook type | Jargon check |
|---------|------------------------------------|-----------|--------------|
| Exec | [summarize] | outcome/cost/risk sentence | business framing only |
| Dev | [summarize] | scenario/moment | technical terms permitted |
| Maker | [summarize] | question/feeling | zero unexplained acronyms |

Gate questions:
1. Are the three Core Belief summaries substantively distinct (not paraphrases of each other)? YES / NO
   *(Enforces advisory at AUDIENCE BELIEF MAP Core Belief column: "Each Core Belief must be substantively distinct from the other two -- naming a claim that belongs specifically to this audience and could not serve as the primary belief anchor for a different audience.")*
2. Does the Maker version contain any unexplained acronym or CLI reference? YES / NO
   *(Enforces advisory at Maker Version Hook: "Zero unexplained acronyms. Zero namespace references. Zero CLI terminology.")*
3. Does the Dev version open with a scenario rather than an outcome statement? YES / NO
   *(Enforces advisory at Dev Version Hook: "A scenario the developer is in right now -- the moment before Signal changes what happens next.")*

Passing state: Q1=YES, Q2=NO, Q3=YES. Rewrite and re-gate any failing version.

**-- PHASE 5 COMPLETE. --**

---

**=== PHASE 6: ANTI-POSITIONING ===**

Write "## What Signal Is NOT" from POSITIONING LOCK Ruling Out values. Add one additional adjacent category. Minimum four bullets. Format: `[Category]. Signal does not [specific function]. [One sentence on why this distinction matters for {topic} specifically.]`

**-- PHASE 6 COMPLETE. --**

---

**=== PHASE 7: PROOF AUDIT ===**

For every factual claim in exec and dev versions: `[source: {artifact-path}]`, `[source: prior signal]`, or `[UNVERIFIED]` -- replace UNVERIFIED before saving.

**-- PHASE 7 COMPLETE. --**

---

**Output format**: `## Exec Version` / `## Dev Version` / `## Maker Version` / `## What Signal Is NOT`

Phase outputs are working notes -- not in saved artifact.

**Save to**: `simulations/draft/pitches/{topic}-pitch-{date}.md`

---

## R10 Design Notes

**What changed from R9:**

R9 V-05 closed the Phase 5 structural audibility gap: PHASE 5 STRUCTURE block present, draft-order integrity defended, gate questions grounded in pre-existing advisories. R10 probes whether the Phase 5 structural declarations meet the same per-site precision standard that the BINDING DECLARATION meets at Phase 2. Three precision gaps identified:

| Gap | R9 V-05 state | R10 axis |
|-----|--------------|----------|
| C-41 Auditability not at declaration site | PHASE 5 STRUCTURE opens with pattern citation, ends with auditability declaration -- 8 lines apart | V-01: move both elements to opening line/heading |
| C-42 Protected set uses phase numbers, not canonical names | "does not change any locked output from Phases 2, 3, or 4" -- set-scope but not canonically named | V-02: enumerate AUDIENCE BELIEF MAP, POSITIONING LOCK, EXEC OPENING SENTENCE by exact name |
| C-43 Gate citations use descriptive paraphrases | "Core Belief distinctness advisory in Phase 2 Core Belief column definition" -- paraphrase not exact canonical text | V-03: cite using exact instruction text as it appears in skill body |

**Structural parallels:**

| R10 criterion | R9 criterion | Maturation arc |
|---------------|-------------|----------------|
| C-41 (declaration site) | C-38 (block named) | C-27 (auditability at creation site) |
| C-42 (canonical name set) | C-39 (set-scope) | C-25 (exhaustiveness closure) |
| C-43 (exact text at cite site) | C-40 (advisory traceability) | C-24 (provenance at cite site) |

**Predicted structural effect of V-05:**

V-05 makes Phase 5 declaration-site precision match Phase 2 declaration-site precision. The PHASE 5 STRUCTURE heading carries both the pattern name and the auditability claim in a single line (C-41). The draft-order integrity statement names every protected output by its exact canonical identifier, not by phase number (C-42). Each gate citation names the advisory source using the exact instruction text from the skill body, so a reader can verify cite-site to source-site without interpretation (C-43). These three changes complete the structural maturation arc that the BINDING DECLARATION completed in R5/R6, now applied one tier up to the phase-structure and gate-citation level.
