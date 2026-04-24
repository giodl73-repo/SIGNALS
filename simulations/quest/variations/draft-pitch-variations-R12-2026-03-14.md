---
skill: draft-pitch
quest_round: R12
rubric: simulations/quest/rubrics/draft-pitch-rubric-v11-2026-03-14.md
date: 2026-03-14
---

## R12 Variations Summary

**Base**: R11 analysis confirmed the synthesis target: V-01's full Phase 2 BINDING DECLARATION (C-25/C-26/C-27 intact) + V-05's Phase 5 body (canonical draft-order integrity C-42, exact gate citations C-43). R12 is pure synthesis execution — no discovery, no new criteria.

**R12 variation map**:

| ID | Axis | Targets |
|----|------|---------|
| **V-01** | Synthesis | V-01 Phase 2 verbatim + V-05 Phase 5 draft-order integrity + V-05 Phase 5 gate citations |

One variation. Expected score: **100.0** (38/38 aspirationals).

---

## V-01 -- R12 Synthesis (C-25+C-26+C-27 + C-41+C-42+C-43 + C-44+C-45)

**Axis**: Full synthesis. Phase 2 BINDING DECLARATION carries the complete C-25/C-26/C-27 text from R10 V-01. Phase 5 carries V-05's canonical draft-order integrity (C-42) and exact gate citations (C-43). Phase 5 heading is the compound declaration from V-01/V-05 (C-41+C-44). Only Phase 5 body changed from V-01 baseline -- zero prior-phase regression (C-45).

**Hypothesis**: All 38 aspirational criteria pass simultaneously. C-25/C-26/C-27 are preserved because Phase 2 is untouched (C-45). C-41/C-44 are satisfied by the compound heading that V-01 and V-05 already share. C-42 is satisfied by the canonical-name enumeration from V-05. C-43 is satisfied by the exact-text gate citations from V-05. The synthesis has no structural conflict: V-01's Phase 2 precision and V-05's Phase 5 precision are independently achievable in the same prompt.

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

For every factual claim in exec and dev versions: `[source: {artifact-path}]`, `[source: prior signal]`, or `[UNVERIFIED]` -- replace UNVERIFIED with hedged language or Proof fallback before saving.

**-- PHASE 7 COMPLETE. --**

---

**Output format**: `## Exec Version` / `## Dev Version` / `## Maker Version` / `## What Signal Is NOT`

Phase outputs are working notes -- not in saved artifact.

**Save to**: `simulations/draft/pitches/{topic}-pitch-{date}.md`

---

## R12 Design Notes

**What changed from R10 V-01:**

Two targeted Phase 5 body changes. Phase 2 is verbatim-identical to R10 V-01.

| Change | R10 V-01 state | R12 synthesis |
|--------|---------------|---------------|
| C-42 Draft-order integrity | "does not change any locked output from Phases 2, 3, or 4" -- phase numbers | Names each output canonically: AUDIENCE BELIEF MAP [Phase 2 locked output], POSITIONING LOCK [Phase 3 locked output], EXEC OPENING SENTENCE [Phase 4 locked output] |
| C-43 Gate citations | Descriptive phrases: "Enforces Core Belief distinctness advisory in Phase 2 Core Belief column definition" | Exact advisory text verbatim from skill body at each cite site |

**What was NOT changed:**

Phase 2 BINDING DECLARATION: verbatim-identical to R10 V-01. All C-25/C-26/C-27 text preserved:
- C-25: "No other DEFAULTS fields are directly bound to BELIEF MAP columns."
- C-26: "Phase 5 does not read SIGNAL DEFAULTS inertia fields directly."
- C-27: "This declaration makes the full DEFAULTS->BELIEF MAP data flow auditable from skill structure alone."

Phase 5 STRUCTURE heading: verbatim-identical to R10 V-01/V-05. Compound heading with both pattern citation and auditability intent satisfies C-41 and C-44.

**C-45 satisfaction by construction**: Only Phase 5 body was changed (two sentences). Phase 2 content is unchanged. Zero prior-phase regression.
