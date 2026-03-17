---
skill: quest-variate
skill_target: scout-size
round: 4
date: 2026-03-17
rubric: simulations/quest/rubrics/scout-size-rubric-v4-2026-03-17.md
axes_explored: [pre-write-gate, prohibition-guards, minimal-gate+guards, gate+guards+R3V05, full-integration-v4]
r3_champion: V-05 (100/100 on v3 rubric)
r3_gap: C-18/C-19 absent from all R3 variations — new criteria sourced from R3 scoring analysis
r4_target: C-18 (pre-analysis structural gate before first analysis section), C-19 (prohibition guards close adjacent sections against canonical-section content)
---

# scout-size — Prompt Variations R4

Five complete, runnable skill body prompts targeting the v4 rubric (19 criteria). Single-axis first (V-01 through V-02), minimal combination (V-03), R3 integration (V-04), full integration (V-05).

## Context: what informed this round

R3 produced V-05 as the sole variation to pass C-09 (scope exclusions) and C-10 (break-even) — exclusively because its 17-criterion self-check forced the model to verify those fields post-generation. The v4 rubric formalizes two structural mechanisms sourced from R3 excellence and failure analysis:

| New criterion | What it requires | R3 gap |
|---------------|-----------------|--------|
| **C-18** (pre-analysis self-check gate) | A confirmation block fires BEFORE the first analysis section, requiring scope boundary and break-even to be resolved as preconditions — the gate is structural, not an inline reminder | R3 V-05 achieves C-09 + C-10 via a post-write SELF-CHECK: the model fills all sections, then checks. The check fires after analysis, not before. C-18 requires the gate to precede all analysis sections, forcing resolution from repo context before any complexity/timeline reasoning begins |
| **C-19** (prohibition guards on adjacent sections) | When a canonical section exists for a field type (OPEN UNKNOWNS for unknowns), at least one adjacent section that could receive the same content carries an explicit prohibition rule | R3 V-03 scored C-14 PARTIAL: a dedicated OPEN UNKNOWNS section existed with typed fields, but CONFIDENCE still carried a Gap field with no prohibition — structural separation was present but leaky. V-01, V-04, V-05 all included "do not list unknowns here" in confidence but this was never isolated as a single-axis test |

**R4 design consequence**: C-18 and C-19 are orthogonal. C-18 governs temporal ordering (gate fires before analysis). C-19 governs spatial separation (canonical section exists AND adjacent sections are explicitly closed). An output can pass C-14 (unknowns section exists) without C-19 (confidence section not closed), and can pass C-09 (exclusion named somewhere) without C-18 (named during analysis, not as precondition). R4 tests each independently first.

**Three single-axis bets for R4:**
- **Axis A (V-01)**: Pre-write gate — mandatory PRE-FLIGHT GATE block fires before any analysis section; model resolves scope boundary and break-even from repo context before any analysis begins
- **Axis B (V-02)**: Prohibition guards — canonical homes established for unknowns (OPEN UNKNOWNS) and scope exclusions (SCOPE EXCLUSIONS); every adjacent section that could receive either content type carries an explicit prohibition rule
- **Axis C (V-03)**: Minimal combination — gate + prohibition guards, no R3 hypothesis-revision or self-indictment machinery

---

## V-01 — Axis: Pre-write gate

**Variation axis**: Structural gate — a mandatory PRE-FLIGHT GATE block fires before any analysis section, requiring scope boundary and break-even to be resolved from repo context before analysis begins

**Hypothesis**: In R3 V-05, scope boundary (C-09) and break-even (C-10) are enforced by a post-write SELF-CHECK: the model generates all sections, then scans for violations and fixes them before writing the artifact. This is enforcement after generation. C-18 requires resolution before generation: the model must think "what is NOT in scope" and "when does building pay off" before it can begin reasoning about surface area, complexity, or timeline. A structural gate that fires first — before INERTIA CHECK, before any analysis section — changes what information the model has committed to before it starts populating fields. The scope boundary resolution feeds into surface area (named points are those IN scope), and the break-even resolution feeds into inertia cost interpretation. Expected risk: the break-even field in the gate may be vague when the model hasn't yet analyzed the workaround. The instruction "a rough signal is sufficient; 'Cannot assess — [reason]' is acceptable; blank is not" is the guard against placeholder responses.

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal files). Do not prompt unless context is absent.

Produce a sizing signal for the topic. A sizing signal answers: how much work is this, and how confident are we in that answer? It does NOT produce a project plan.

Follow the sections below in order. Every section is required.

---

## PRE-FLIGHT GATE

Complete both fields before filling any section after this one. This is a structural gate — scope boundary and break-even must be resolved before analysis begins, not during or after.

Out-of-scope boundary:
[Name at least one sub-system, behavior, integration, or phase explicitly NOT covered by this sizing. If genuinely full scope: "No exclusions — full implementation assumed." Do not say "TBD." Do not leave blank.]

Break-even signal:
[At what usage level, team count, or time horizon does building this feature recover its cost relative to continuing the current workaround? A rough signal is sufficient: "breaks even at 3+ teams using weekly" or "never recovers if adoption stays below 10 daily users." If break-even cannot be assessed from available context, state explicitly: "Cannot assess — [specific reason]." Absence fails.]

STOP: Do not proceed to INERTIA CHECK or any section below until both fields contain specific responses.

---

## INERTIA CHECK

What do teams or users do instead of this feature?

Workaround: [the specific alternative currently in use — name it, do not describe it generically]
Maintenance cost: [hours/sprint, error rate, manual effort, or qualitative estimate]
Cost direction: [choose exactly one: cheaper / comparable / more expensive]

The cost direction is a verdict. "It depends" is not a verdict. Pick the closest word; note any qualifying condition in parentheses.

---

## SURFACE AREA

Name each integration point individually: API endpoints, auth hooks, event bus subscriptions, data model changes, config surfaces, cross-service contracts.

| # | Integration Point | Type | Description |
|---|-------------------|------|-------------|
| 1 | [name] | [API / event / data model / config / cross-service] | [brief] |
| ... | | | |
| **Total** | | | **N integration points** |

The Total row is required. A general description without named points fails.

---

## COMPLEXITY TIER AND DRIVER

Tier: [exactly one of: LOW / MEDIUM / HIGH / XL — no other values]
Primary driver: [the one or two factors most responsible for this tier]

Tier sensitivity:
- Rises to [LEVEL] if [single named condition].
- Falls to [LEVEL] if [single named condition].

Each condition is ONE specific, testable scenario absent today. "If requirements expand" fails — it cannot be tested.

---

## TEAM AND TIMELINE SIGNAL

Team signal: [specialist disciplines + FTE fractions + implementation ownership per role]
  Failing: "2 engineers" — no disciplines, no ownership named.
  Passing: "1 backend engineer (owns event schema + storage layer), 0.5 PM (owns stakeholder coordination)"

Timeline signal: [sprint range — "N–M sprints" — not a point estimate, not a calendar date]

---

## CONFIDENCE

Confidence: [HIGH / MEDIUM / LOW]
Basis: [what IS known — specific evidence, prior work, or verified reasoning that supports this rating]

Do not list unknowns here. Unknowns go in the OPEN UNKNOWNS section below.

---

## OPEN UNKNOWNS

This section is structurally separate from the confidence basis above. It lists the specific things not yet verified that limit confidence.

If confidence is fully grounded and no unknowns remain, state explicitly: "No open unknowns."

For each open unknown, fill all three fields:

Unknown: [the specific unverified item — name it concretely]
Impact: [which sizing dimension this most affects: complexity / timeline / team / confidence]
Movement: [the specific investigation or result that would close this unknown]

A generic placeholder like "dependencies may exist" fails — an unknown must name a specific dependency, decision, or contract.

---

## SYNTHESIS

Cross-reference at least two signal dimensions (complexity, timeline, confidence, inertia cost) to produce a decision-relevant observation. Dimensions must be combined to produce the conclusion — the conclusion must not be derivable from any single dimension alone.

Restating each section in sequence ("Complexity is HIGH, timeline is 4–6 sprints, team needs 2 engineers") is juxtaposition, not synthesis.

---

## SIGNAL BOUNDARY

No task breakdowns. No sprint assignments. No owner names. No milestone dates.
This signal feeds program-plan. It does not replace it.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-02 — Axis: Prohibition guards

**Variation axis**: Output format — canonical homes established for unknowns (OPEN UNKNOWNS) and scope exclusions (SCOPE EXCLUSIONS); every adjacent section that could plausibly receive either content type carries an explicit prohibition rule

**Hypothesis**: R3 V-03 scored C-14 PARTIAL because the CONFIDENCE section retained a Gap field alongside a dedicated OPEN UNKNOWNS section — no prohibition closed the confidence section against unknowns, so the model used both. The test for C-19 is not just "does a canonical section exist?" but "are the sections adjacent to that canonical home explicitly closed?" Prohibition guards make cross-contamination impossible rather than merely unlikely: when CONFIDENCE says "do not list unknowns here — they belong in OPEN UNKNOWNS below," the model cannot accidentally fail C-19. The same logic extends to scope exclusions: without a canonical home and without guards on neighboring sections, exclusions drift into COMPLEXITY ("note: auth is out of scope") or SURFACE AREA ("we are not covering X"), making them invisible to scoring. Adding SCOPE EXCLUSIONS as a canonical section — then closing SURFACE AREA, COMPLEXITY, and SYNTHESIS against scope content — tests whether prohibition alone (without a pre-write gate) achieves the structural separation. Expected risk: the SCOPE EXCLUSIONS section at the end may not force resolution before analysis; that is the single-axis limitation this variation intentionally accepts (C-18 is not targeted here).

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal files). Do not prompt unless context is absent.

Produce a sizing signal. NOT a project plan. Every section below is required.

---

## INERTIA CHECK

Canonical home for workaround observations. Name the current workaround and its cost.

Workaround: [the specific alternative in use]
Maintenance cost: [hours/sprint, error rate, manual effort, or qualitative]
Cost direction: [cheaper / comparable / more expensive — one word]

---

## SURFACE AREA

Name each integration point individually: API endpoints, auth hooks, event bus subscriptions, data model changes, config surfaces, cross-service contracts.

Do not include scope exclusions here. Scope exclusions belong in the SCOPE EXCLUSIONS section below — noting them in this section creates a duplicate record outside the canonical home.

| # | Integration Point | Type | Description |
|---|-------------------|------|-------------|
| 1 | [name] | [API / event / data model / config / cross-service] | [brief] |
| ... | | | |
| **Total** | | | **N integration points** |

Total row required.

---

## COMPLEXITY TIER AND DRIVER

Tier: [LOW / MEDIUM / HIGH / XL — exactly this vocabulary]
Primary driver: [one or two factors most responsible]

Tier sensitivity:
- Rises to [LEVEL] if [single named condition].
- Falls to [LEVEL] if [single named condition].

Do not list what is out of scope here. Scope exclusions belong in the SCOPE EXCLUSIONS section below.

---

## TEAM AND TIMELINE SIGNAL

Team signal: [specialist disciplines + FTE fractions + implementation ownership area per role]
  Failing: "2 engineers" — no disciplines or ownership.
  Passing: "1 backend engineer (owns API + event schema), 0.5 PM (owns alignment)"

Timeline signal: [sprint range — "N–M sprints" form required]

---

## CONFIDENCE

Confidence: [HIGH / MEDIUM / LOW]
Basis: [what IS known — specific evidence or prior work that supports this rating]

Do not list unknowns here. Unknowns belong in the OPEN UNKNOWNS section below. Listing an unknown in the confidence basis creates a second, structurally invisible record — the separation this section enforces is what makes OPEN UNKNOWNS detectable as complete or incomplete.

---

## OPEN UNKNOWNS

Canonical home for unverified items. Do not list unknowns in CONFIDENCE above or in SYNTHESIS below — those sections are explicitly closed against unknowns.

If no unknowns remain: "No open unknowns — confidence is fully grounded."

For each open unknown:

Unknown: [the specific unverified item — concrete, not generic]
Impact: [which dimension this most affects: complexity / timeline / team / confidence]
Movement: [what investigation resolves this — specific action or result]

A generic placeholder like "dependencies may exist" fails.

---

## SYNTHESIS

Cross-reference at least two signal dimensions (complexity, timeline, confidence, inertia cost) to produce a directional observation that requires both dimensions to state.

Do not embed unknowns here — they belong in OPEN UNKNOWNS. Do not include scope exclusions here — they belong in SCOPE EXCLUSIONS. Those sections are the canonical homes for their content; this section is closed against both.

Restating sections in sequence is juxtaposition, not synthesis.

---

## SCOPE EXCLUSIONS

Canonical home for out-of-scope items. Scope exclusions noted in SURFACE AREA, COMPLEXITY, or SYNTHESIS instead of here will not be counted toward C-09 — only entries in this section are canonical.

State at least one explicit exclusion, assumption, or out-of-scope boundary. If the full implementation is genuinely in scope: "No exclusions — full scope assumed."

---

## SIGNAL BOUNDARY

No task breakdowns. No sprint assignments. No owner names. No milestone dates.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-03 — Axes: Pre-write gate + Prohibition guards (minimal combination)

**Variation axes**: Pre-write gate (C-18) + Prohibition guards (C-19) — both new R4 axes combined in the simplest possible structure, without R3 hypothesis-revision or self-indictment machinery

**Hypothesis**: V-01 and V-02 test C-18 and C-19 independently. V-03 tests whether combining both in the minimal structure — pre-flight gate at the top, prohibition guards throughout — achieves both criteria without requiring the full R3 V-05 machinery. The combination is expected to be non-interfering: the gate resolves scope boundary and break-even as temporal preconditions (before analysis starts), while the prohibition guards enforce spatial separation (canonical sections have closed adjacent sections). They address different failure modes and operate on different dimensions of the output structure. If V-03 passes C-18 and C-19 cleanly, V-04 and V-05 add the R3 mechanisms as separable improvements on other criteria. Expected risk: without the preliminary hypothesis mechanism, synthesis may revert to post-hoc juxtaposition; a lightweight synthesis anti-pattern reminder is included as a minimal guard (without full self-indictment machinery).

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal files). Do not prompt unless context is absent.

Produce a sizing signal. NOT a project plan. Every section below is required.

---

## PRE-FLIGHT GATE

Resolve both fields before proceeding to any analysis section. This gate fires before all other sections — scope boundary and break-even must be answered from repo context before any analysis section is filled. Do not proceed to INERTIA CHECK until both fields contain specific responses.

Out-of-scope boundary:
[Name at least one sub-system, behavior, or integration explicitly NOT covered by this sizing. "TBD" or blank fails. If genuinely full scope: "No exclusions — full scope assumed."]

Break-even signal:
[At what adoption level, team count, or time horizon does building recover its cost vs. the current workaround? A rough signal is sufficient. If it cannot be assessed: "Cannot assess — [specific reason]." Absence fails.]

---

## INERTIA CHECK

Workaround: [the specific alternative]
Maintenance cost: [hours/sprint, error rate, or qualitative]
Cost direction: [cheaper / comparable / more expensive — one word required]

Do not re-state the break-even estimate here — it was recorded in PRE-FLIGHT GATE above.

---

## SURFACE AREA

Do not include scope exclusions here — they were resolved in PRE-FLIGHT GATE above.

| # | Integration Point | Type | Description |
|---|-------------------|------|-------------|
| 1 | [name] | [API / event / data model / config / cross-service] | [brief] |
| ... | | | |
| **Total** | | | **N integration points** |

Total row required.

---

## COMPLEXITY TIER AND DRIVER

Tier: [LOW / MEDIUM / HIGH / XL]
Primary driver: [one or two factors most responsible]

Tier sensitivity:
- Rises to [LEVEL] if [single named condition].
- Falls to [LEVEL] if [single named condition].

Do not include scope exclusions here — they were resolved in PRE-FLIGHT GATE.

---

## TEAM AND TIMELINE SIGNAL

Team signal: [specialist disciplines + FTE fractions + implementation ownership per role]
  Failing: "2 engineers" — no disciplines or ownership.
  Passing: "1 backend engineer (owns event schema + storage layer), 0.5 PM (owns stakeholder coordination)"

Timeline signal: [sprint range — "N–M sprints"]

---

## CONFIDENCE

Confidence: [HIGH / MEDIUM / LOW]
Basis: [what IS known — specific evidence or prior work]

Do not list unknowns here. Unknowns belong in OPEN UNKNOWNS below.

---

## OPEN UNKNOWNS

Canonical home for unverified items. Do not list unknowns in CONFIDENCE above or in SYNTHESIS below — those sections are closed against unknowns.

If no unknowns remain: "No open unknowns."

For each open unknown:

Unknown: [specific unverified item — name it concretely]
Impact: [complexity / timeline / team / confidence]
Movement: [specific investigation or result that closes this]

---

## SYNTHESIS

> **Anti-pattern**: Restating sections in sequence ("Complexity is HIGH. Timeline is 4–6 sprints.") is juxtaposition — it fails this section. Do not embed unknowns here (they go in OPEN UNKNOWNS). Do not re-state the scope boundary here (it was resolved in PRE-FLIGHT GATE).

Cross-reference at least two signal dimensions (complexity, timeline, confidence, inertia cost) to produce a decision-relevant observation that requires both dimensions to state.

---

## SIGNAL BOUNDARY

No task breakdowns. No sprint assignments. No owner names. No milestone dates.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-04 — Axes: Pre-write gate + Prohibition guards + R3 V-05 structure

**Variation axes**: C-18 (pre-write gate) + C-19 (prohibition guards) + R3 V-05 mechanisms (preliminary hypothesis, unknowns section, self-indictment, AMEND cascade) — with 17-criterion self-check unchanged

**Hypothesis**: R3 V-05 achieved 100/100 on v3 but lacks C-18 and C-19. V-04 grafts both new mechanisms onto R3 V-05 to test whether they co-exist without regressions. The PRE-FLIGHT GATE fires before MANDATORY OPENING: PRELIMINARY HYPOTHESIS — this is the correct ordering because the hypothesis is itself an analysis commitment (complexity tier, timeline range), and scope boundary resolution should precede any estimate. The prohibition guards are added to each STEP that could have field bleed: STEP 2 and STEP 3 get scope exclusion guards, STEP 5 (confidence) gets an unknowns guard (it already had one in R3 but it was not identified as a C-19 mechanism), STEP 6 (open unknowns) gets guards against break-even and scope exclusions drifting in. The 17-criterion self-check is intentionally left unchanged to isolate the structural mechanisms from checklist enforcement — V-05 will test whether updating the checklist to 19 adds value on top of the structural mechanisms. Expected risk: the prompt is long; the sequential label system (PRE-FLIGHT → MANDATORY OPENING → STEP 1–7 → SIGNAL BOUNDARY CHECK → SELF-CHECK) is the primary guard against section confusion.

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal files). Do not prompt unless context is absent.

Produce a sizing signal. This is NOT a project plan. Signal boundary: no task breakdowns, sprint assignments, owner names, or milestone dates.

Follow every step in order. Every labeled row and field is required.

---

**PRE-FLIGHT GATE — resolve before any analysis begins**

Complete both fields below before proceeding to MANDATORY OPENING or any analysis STEP. This gate is a structural precondition — scope boundary and break-even must be resolved from repo context before any sizing estimate is committed.

Out-of-scope boundary:
[What is explicitly NOT included in this sizing? Name at least one sub-system, phase, or integration excluded. If full scope: "No exclusions — full scope assumed." Blank or "TBD" fails.]

Break-even signal:
[When does building this feature recover its cost vs. continuing the workaround? State a rough signal — usage level, team count, or time horizon — or explicitly: "Cannot assess — [specific reason]." Absence fails.]

STOP: Do not proceed to MANDATORY OPENING until both fields above contain specific responses.

---

**MANDATORY OPENING: PRELIMINARY HYPOTHESIS**

After PRE-FLIGHT GATE, commit to a preliminary estimate. You will confirm or revise it in STEP 7.

Hypothesis — complexity tier: [LOW / MEDIUM / HIGH / XL — one specific tier, commit]
Hypothesis — timeline: [sprint range — "N–M sprints" — one range]
Reasoning: [one sentence — what signals the scope before detailed analysis?]

Failing form: "Hard to say without more analysis." If genuinely uncertain, pick LOW as default and note the uncertainty.

---

**STEP 1: INERTIA CHECK**

> WRONG: "Teams use a workaround currently." — Workaround named; cost direction absent. Fails.
> CORRECT: "Manual CSV re-import per team — building is **more expensive** upfront but **cheaper** to maintain long-term; the workaround costs ~2h/sprint/team and scales linearly with team count."

Workaround: [name the specific alternative in use]
Maintenance cost: [estimate the ongoing cost]
Cost direction: [cheaper / comparable / more expensive — one word, required]

---

**STEP 2: SURFACE AREA**

Do not include scope exclusions here — they were resolved in PRE-FLIGHT GATE.

| # | Integration Point | Type | Description |
|---|-------------------|------|-------------|
| 1 | [name] | [API / event / data model / config / cross-service] | [brief] |
| ... | | | |
| **Total** | | | **N integration points** |

Total row required. "Several integration points" is not an enumeration.

---

**STEP 3: COMPLEXITY TIER AND DRIVER**

Tier: [LOW / MEDIUM / HIGH / XL — exactly this vocabulary]
Primary driver: [one or two factors most responsible]

Tier sensitivity — use this exact template:

    Tier rises to [LEVEL] if [single named condition].
    Tier falls to [LEVEL] if [single named condition].

Do not include scope exclusions here — they were resolved in PRE-FLIGHT GATE, not in analysis sections.

Failing forms for sensitivity:

| Failing form | Why it fails |
|---|---|
| "Several factors could push this to XL" | Not one named condition |
| "If requirements expand" | Cannot be tested |
| "If integration proves complex" | Restates the tier, names nothing new |
| "If the timeline slips" | Wrong dimension — timeline sensitivity, not tier sensitivity |

---

**STEP 4: TEAM AND TIMELINE SIGNAL**

Team signal: [specialist disciplines + FTE fractions + implementation ownership per role]
  Failing: "3 engineers" — no disciplines, no ownership.
  Passing: "1 backend engineer (owns event schema + API layer), 1 infra engineer (owns deployment pipeline), 0.5 PM (owns stakeholder coordination)"

Timeline signal: [sprint range — "N–M sprints"]
  Failing: "Q3 2026" (calendar date), "4 sprints" (point estimate, not a range)

---

**STEP 5: CONFIDENCE**

Confidence: [HIGH / MEDIUM / LOW]
Basis: [what IS known — specific evidence, prior work, or verified reasoning]

Do not list unknowns here. They go in STEP 6. Listing unknowns in the confidence section creates a second, unguarded record outside the canonical home — this section is explicitly closed against unknowns.

---

**STEP 6: OPEN UNKNOWNS**

> **FAILURE MODE FOR THIS SECTION**: "Dependencies may exist" is a placeholder, not an unknown. An unknown must name a specific dependency, decision, or contract that has not been verified. A generic hedge fails exactly as silently as an absent section. Do not include scope exclusions here — they were resolved in PRE-FLIGHT GATE. Do not include break-even observations here — they were resolved in PRE-FLIGHT GATE.

List open unknowns with typed fields. If none remain, state: "No open unknowns."

For each open unknown:

Unknown: [the specific unverified item — concrete, testable]
Impact: [which dimension this most affects: complexity / timeline / team / confidence]
Movement: [the specific investigation or result that closes this unknown]

---

**STEP 7: SYNTHESIS**

> **FAILURE MODE FOR THIS SECTION**: Restating sections in sequence — "Complexity is HIGH. Timeline is 4–6 sprints. Confidence is MEDIUM." — is juxtaposition, not synthesis. Do not embed unknowns here — they belong in STEP 6. Do not include scope exclusions here — they were resolved in PRE-FLIGHT GATE.

First, look back at your PRELIMINARY HYPOTHESIS. State whether the analysis confirms, revises, or partially revises it:

- "Hypothesis confirmed: [tier] at [sprint range] because [cross-signal observation]"
- "Hypothesis revised: [dimension] changed from [prior value] to [current value] because [reason]"
- "Hypothesis partially revised: [what held] confirmed; [what changed] changed from [prior] to [current] because [reason]"

After the hypothesis statement, add the cross-signal directional observation: combine at least two dimensions (complexity, timeline, confidence, inertia cost) to produce a recommendation that requires both dimensions to state.

**AMEND INSTRUCTION**: If an AMEND directive is present in this invocation, complete the amendment fully, then re-read this synthesis. If the amended dimension appears in the synthesis conclusion, update the conclusion or explicitly reaffirm it in light of the amendment. Leaving synthesis unchanged after amending a cited dimension is a silent contradiction — it fails C-16.

---

**SIGNAL BOUNDARY CHECK**

Before writing the artifact, scan and remove:
- [ ] Task breakdowns ("Step 1: implement X")
- [ ] Sprint assignments ("Sprint 2: auth integration")
- [ ] Owner names ("Alice owns the backend work")
- [ ] Milestone dates ("Targeting March delivery")

---

**SELF-CHECK — ALL 17 CRITERIA**

- [ ] C-01: Complexity tier is exactly LOW / MEDIUM / HIGH / XL — no other form
- [ ] C-02: Timeline is a sprint range (N–M), not a point estimate or calendar date
- [ ] C-03: Surface area table has a Total row with a specific number
- [ ] C-04: Inertia workaround is named; cost direction is exactly cheaper / comparable / more expensive
- [ ] C-05: Confidence level is present with a basis naming specific supporting evidence
- [ ] C-06: Team signal names specialist disciplines (not headcount only)
- [ ] C-07: Primary driver accompanies the complexity tier
- [ ] C-08: If AMEND is present, at least one substantive output change traces to it; absent → pass by default
- [ ] C-09: At least one explicit exclusion, assumption, or out-of-scope boundary is named (was resolved in PRE-FLIGHT GATE)
- [ ] C-10: Break-even signal present in PRE-FLIGHT GATE, or explicitly stated "Cannot assess — [reason]"
- [ ] C-11: Each named specialization includes an implementation ownership area
- [ ] C-12: At least one specific unknown named that would move confidence if resolved, or "no open unknowns" stated
- [ ] C-13: Synthesis cross-references two or more signal dimensions to produce a directional conclusion
- [ ] C-14: Open unknowns appear in a named section separate from confidence basis, with Unknown: / Impact: / Movement: fields
- [ ] C-15: Preliminary hypothesis stated before analysis; synthesis explicitly confirms or revises it, naming the dimension that changed
- [ ] C-16: If AMEND present and amended dimension in synthesis, synthesis updated or reaffirmed; absent → pass by default
- [ ] C-17: At least one aspirational section (synthesis or unknowns) contains a sentence naming the anti-pattern being avoided

Fix any violation before writing.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-05 — Full Integration (all R4 axes + all R3 axes + 19-criterion self-check)

**Variation axes**: All R4 axes (C-18 pre-write gate, C-19 prohibition guards) + all R3 V-05 axes (preliminary hypothesis, unknowns section, self-indictment, AMEND cascade) + self-check updated to 19 criteria

**Hypothesis**: V-04 is R3 V-05 + C-18 gate + C-19 guards, with the 17-criterion self-check inherited from R3 unchanged. V-05 extends V-04 in two ways: (1) the self-check is updated to 19 criteria, explicitly adding C-18 ("PRE-FLIGHT GATE appears before MANDATORY OPENING and any STEP, contains both scope boundary and break-even responses, and includes a stop instruction") and C-19 ("at least one adjacent section carries an explicit prohibition rule"); (2) the prohibition guards are made more comprehensive — every section that could plausibly receive content from a canonical home is explicitly closed, not just the highest-risk adjacent sections. The dual-enforcement structure (structural mechanisms during generation + self-check enforcement after generation) was V-05 R3's core pattern: the structural mechanisms prevent violations during generation, while the checklist catches any residuals before writing. Updating the checklist to 19 criteria closes the loop for C-18 and C-19 just as it did for C-09 and C-10 in R3 V-05. Expected risk: length is the primary failure mode; the explicit sequential ordering (PRE-FLIGHT GATE → MANDATORY OPENING → STEP 1–7 → SIGNAL BOUNDARY CHECK → 19-criterion SELF-CHECK) and the stop instruction in the gate are the primary guards.

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal files). Do not prompt unless context is absent.

Produce a sizing signal. This is NOT a project plan. Signal boundary: no task breakdowns, sprint assignments, owner names, or milestone dates. Remove any violations before writing the artifact.

Follow every step in order. Every labeled row and field is required.

---

**PRE-FLIGHT GATE — complete before any analysis begins**

Both fields below are preconditions for all analysis sections, including MANDATORY OPENING. Resolve them from repo context now. Do not proceed until both fields contain specific responses — "TBD" or blank fails either field.

Out-of-scope boundary:
[Name at least one sub-system, phase, integration, or behavior explicitly NOT covered by this sizing. If genuinely full implementation scope: "No exclusions — full scope assumed." Do not say "TBD."]

Break-even signal:
[At what usage level, team count, or time horizon does building this feature recover its cost vs. the current workaround? State a rough signal or explicitly: "Cannot assess — [specific reason]." Absence fails C-10 before analysis begins.]

STOP: Both fields must contain specific responses. Do not proceed to MANDATORY OPENING or any STEP until this gate is resolved.

---

**MANDATORY OPENING: PRELIMINARY HYPOTHESIS**

After PRE-FLIGHT GATE, commit to a preliminary estimate. You will confirm or revise it in STEP 7.

Hypothesis — complexity tier: [LOW / MEDIUM / HIGH / XL — one specific tier, commit]
Hypothesis — timeline: [sprint range — "N–M sprints" — one range]
Reasoning: [one sentence — what signals the scope before detailed analysis?]

Failing form: "Hard to say without more analysis." If genuinely uncertain, pick LOW as default and note the uncertainty.

---

**STEP 1: INERTIA CHECK**

> WRONG: "Teams use a workaround currently." — No cost direction. Fails.
> CORRECT: "Manual CSV re-import per team — building is **more expensive** upfront but **cheaper** to maintain; workaround costs ~2h/sprint/team and scales linearly with team count."

Workaround: [name the specific alternative in use]
Maintenance cost: [estimate the ongoing cost]
Cost direction: [cheaper / comparable / more expensive — one word, required]

---

**STEP 2: SURFACE AREA**

Do not include scope exclusions here — they were resolved in PRE-FLIGHT GATE, not in analysis sections.

| # | Integration Point | Type | Description |
|---|-------------------|------|-------------|
| 1 | [name] | [API / event / data model / config / cross-service] | [brief] |
| ... | | | |
| **Total** | | | **N integration points** |

Total row required. "Several integration points" is not an enumeration.

---

**STEP 3: COMPLEXITY TIER AND DRIVER**

Tier: [LOW / MEDIUM / HIGH / XL — exactly this vocabulary]
Primary driver: [one or two factors most responsible]

Tier sensitivity — use this exact template:

    Tier rises to [LEVEL] if [single named condition].
    Tier falls to [LEVEL] if [single named condition].

Do not include scope exclusions here — they were resolved in PRE-FLIGHT GATE, not in analysis sections.

Failing forms for sensitivity:

| Failing form | Why it fails |
|---|---|
| "Several factors could push this to XL" | Not one named condition |
| "If requirements expand" | Cannot be tested |
| "If integration proves complex" | Restates the tier, names nothing new |
| "If the timeline slips" | Wrong dimension |

---

**STEP 4: TEAM AND TIMELINE SIGNAL**

Team signal: [specialist disciplines + FTE fractions + implementation ownership per role]
  Failing: "3 engineers" — no disciplines, no ownership.
  Passing: "1 backend engineer (owns event schema + API layer), 1 infra engineer (owns deployment pipeline), 0.5 PM (owns stakeholder coordination)"

Timeline signal: [sprint range — "N–M sprints"]
  Failing: "Q3 2026" (calendar date), "4 sprints" (point estimate, not a range)

---

**STEP 5: CONFIDENCE**

Confidence: [HIGH / MEDIUM / LOW]
Basis: [what IS known — specific evidence, prior work, or verified reasoning]

Do not list unknowns here. They go in STEP 6. This section is explicitly closed against unknowns — listing one here creates a second, unguarded record outside the canonical home that STEP 6 provides.

---

**STEP 6: OPEN UNKNOWNS**

> **FAILURE MODE FOR THIS SECTION**: "Dependencies may exist" is a placeholder, not an unknown. An unknown must name a specific dependency, decision, or contract that has not been verified. A generic hedge fails exactly as silently as an absent section — the structural separation from STEP 5 exists to make omissions visible, not to create a section that can be filled with vague language. Do not include scope exclusions here — they were resolved in PRE-FLIGHT GATE. Do not include break-even observations here — they were resolved in PRE-FLIGHT GATE.

List open unknowns with typed fields. If none remain, state: "No open unknowns."

For each open unknown:

Unknown: [the specific unverified item — concrete, testable]
Impact: [which dimension this most affects: complexity / timeline / team / confidence]
Movement: [the specific investigation or result that closes this unknown]

---

**STEP 7: SYNTHESIS**

> **FAILURE MODE FOR THIS SECTION**: Restating sections in sequence — "Complexity is HIGH. Timeline is 4–6 sprints. Confidence is MEDIUM." — is juxtaposition, not synthesis. This section fails if the conclusion is derivable from any single field alone. Do not embed unknowns here — they belong in STEP 6. Do not include scope exclusions here — they were resolved in PRE-FLIGHT GATE.

First, look back at your PRELIMINARY HYPOTHESIS. State whether the analysis confirms, revises, or partially revises it:

- "Hypothesis confirmed: [tier] at [sprint range] because [cross-signal observation]"
- "Hypothesis revised: [dimension] changed from [prior value] to [current value] because [reason]"
- "Hypothesis partially revised: [what held] confirmed; [what changed] changed from [prior] to [current] because [reason]"

After the hypothesis statement, add the cross-signal directional observation: combine at least two dimensions (complexity, timeline, confidence, inertia cost) to produce a recommendation. The recommendation must require both dimensions to state.

**AMEND INSTRUCTION**: If an AMEND directive is present in this invocation, complete the amendment fully, then re-read this synthesis. If the amended dimension appears in the synthesis conclusion, update the conclusion or explicitly reaffirm it. Leaving synthesis unchanged after amending a cited dimension is a silent contradiction — it fails C-16.

---

**SIGNAL BOUNDARY CHECK**

Before writing the artifact, scan and remove:
- [ ] Task breakdowns ("Step 1: implement X")
- [ ] Sprint assignments ("Sprint 2: auth integration")
- [ ] Owner names ("Alice owns the backend work")
- [ ] Milestone dates ("Targeting March delivery")

---

**SELF-CHECK — ALL 19 CRITERIA**

- [ ] C-01: Complexity tier is exactly LOW / MEDIUM / HIGH / XL — no other form
- [ ] C-02: Timeline is a sprint range (N–M), not a point estimate or calendar date
- [ ] C-03: Surface area table has a Total row with a specific number
- [ ] C-04: Inertia workaround is named; cost direction is exactly cheaper / comparable / more expensive
- [ ] C-05: Confidence level is present with a basis naming specific supporting evidence
- [ ] C-06: Team signal names specialist disciplines (not headcount only)
- [ ] C-07: Primary driver accompanies the complexity tier
- [ ] C-08: If AMEND is present, at least one substantive output change traces to it; absent → pass by default
- [ ] C-09: At least one explicit exclusion or out-of-scope boundary named — must appear in PRE-FLIGHT GATE (canonical location); also acceptable anywhere else in the output
- [ ] C-10: Break-even signal present in PRE-FLIGHT GATE, or explicitly stated "Cannot assess — [reason]"
- [ ] C-11: Each named specialization includes an implementation ownership area
- [ ] C-12: At least one specific unknown named that would move confidence if resolved, or "no open unknowns" stated
- [ ] C-13: Synthesis cross-references two or more signal dimensions to produce a directional conclusion
- [ ] C-14: Open unknowns appear in a named section separate from confidence basis, with Unknown: / Impact: / Movement: typed fields
- [ ] C-15: Preliminary hypothesis stated before analysis (after PRE-FLIGHT GATE); synthesis explicitly confirms or revises it, naming the dimension that changed
- [ ] C-16: If AMEND present and amended dimension in synthesis, synthesis updated or reaffirmed; absent or no overlap → pass by default
- [ ] C-17: At least one aspirational section (synthesis or unknowns) contains a sentence naming the anti-pattern being avoided
- [ ] C-18: PRE-FLIGHT GATE appears before MANDATORY OPENING and before all STEPs; contains both scope boundary and break-even fields with specific responses; includes a stop instruction; inline reminders inside sections do not count
- [ ] C-19: At least one section adjacent to OPEN UNKNOWNS (specifically STEP 5 CONFIDENCE) and at least one section adjacent to the scope exclusion canonical location (STEP 2 SURFACE AREA or STEP 3 COMPLEXITY) carry an explicit prohibition rule — not just that the canonical sections exist, but that their neighbors are closed

Fix any violation before writing.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## Variation Summary

| ID | Axes | C-18 | C-19 | C-09 | C-10 | C-14 | C-15 | C-16 | C-17 |
|----|------|------|------|------|------|------|------|------|------|
| V-01 | Pre-write gate only | **High** | Low — no prohibition guards | High — gate forces resolution | High — gate forces resolution | Medium — "do not list here" in confidence but not isolated as C-19 | Low — no hypothesis | Low | Low |
| V-02 | Prohibition guards only | Low — no gate | **High** | Medium — SCOPE EXCLUSIONS section exists but no gate | Low — no break-even field | High — OPEN UNKNOWNS + confidence prohibition | Low — no hypothesis | Low | Low |
| V-03 | Pre-write gate + guards (minimal) | **High** | **High** | High | High | High | Low — no hypothesis | Low | Low — synthesis reminder only |
| V-04 | Pre-write gate + guards + R3 V-05 (17-criterion self-check) | **High** | **High** | **High** | **High** | **High** | **High** | **High** | **High** |
| V-05 | Full integration + 19-criterion self-check | **High** | **High** | **High** | **High** | **High** | **High** | **High** | **High** |

**Key design differences from R3:**

- **C-18 mechanism**: R3 V-05 achieves C-09 + C-10 via a post-write SELF-CHECK. The check fires after all sections are filled — scope boundary and break-even are afterthoughts verified at the end. R4 V-01, V-03, V-04, V-05 add a PRE-FLIGHT GATE that fires before PRELIMINARY HYPOTHESIS and before STEP 1: scope boundary and break-even are resolved as preconditions from repo context, before any sizing reasoning begins. The gate includes an explicit stop instruction; inline reminders within later sections do not satisfy C-18.

- **C-19 mechanism**: R3 V-03 scored C-14 PARTIAL: a dedicated OPEN UNKNOWNS section existed with typed fields, but CONFIDENCE retained a Gap field with no prohibition. V-03, V-04, V-05 add explicit prohibition rules to CONFIDENCE ("do not list unknowns here — they belong in STEP 6 / OPEN UNKNOWNS") and to STEP 2/STEP 3 ("do not include scope exclusions here — they were resolved in PRE-FLIGHT GATE"). The prohibition rule is a distinct structural property from canonical section existence: a canonical section can exist without its adjacent sections being closed against it.

- **V-02 single-axis design**: SCOPE EXCLUSIONS appears as a canonical section at the end (like SIGNAL BOUNDARY). This tests whether prohibition guards alone (without a pre-write gate) cause scope exclusions and unknowns to flow to their canonical homes. The known weakness: the SCOPE EXCLUSIONS section at the end does not force resolution before analysis, so C-18 is not expected to pass (by design — this is a single-axis C-19 test).

- **Self-check evolution**: R3 V-05 has a 17-criterion self-check. R4 V-04 intentionally keeps 17 criteria to isolate the structural mechanisms from checklist enforcement. R4 V-05 updates to 19 criteria, adding explicit C-18 and C-19 checklist items that define exactly what constitutes a pass — providing dual enforcement: structural mechanisms prevent violations during generation, checklist catches residuals before writing.
