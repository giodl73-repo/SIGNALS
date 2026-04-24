---
skill: quest-variate
skill_target: scout-size
round: 3
date: 2026-03-17
rubric: simulations/quest/rubrics/scout-size-rubric-v3-2026-03-17.md
axes_explored: [unknowns-as-section, hypothesis-revision-lifecycle, section-self-indictment, combined-unknowns+hypothesis, full-integration]
r2_champions: [V-04 table+split+template, V-05 full-integration]
r2_gap: C-14/C-15/C-16/C-17 absent from all R2 variations — new criteria added after R2 was written
r3_target: introduce structural mechanisms for C-14 (unknowns section), C-15 (hypothesis-revision), C-16 (AMEND cascade), C-17 (section self-indictment)
---

# scout-size — Prompt Variations R3

Five complete, runnable skill body prompts targeting the v3 rubric (17 criteria). Single-axis first (V-01 through V-03), then combinations (V-04, V-05).

## Context: what informed this round

R2 produced two co-champions: V-04 (table + confidence split + single-condition template) and V-05 (full integration with anti-pattern block and 12-criterion self-check). The v3 rubric adds four Aspirational criteria extracted from R2 excellence signals and cross-round pattern analysis:

| New criterion | What it requires | R2 gap |
|---------------|-----------------|--------|
| C-14 (unknowns-as-section) | Open unknowns in a dedicated section with typed fields (`Unknown:` / `Impact:` / `Movement:`), structurally separate from confidence prose | R2 Gap field is a single line in the confidence section — omissions are invisible without a structural section |
| C-15 (hypothesis-revision) | Preliminary hypothesis committed before analysis; synthesis explicitly confirms or revises it, naming the dimension that changed | R2 has no pre-analysis commitment; synthesis is written post-hoc from populated fields |
| C-16 (AMEND cascade) | When AMEND touches a dimension cited in synthesis, synthesis re-evaluates the cross-signal conclusion | R2 AMEND instruction changes the field but does not require synthesis re-evaluation |
| C-17 (section self-indictment) | At least one aspirational section names its own anti-pattern — synthesis or unknowns must say what form would fail | R2 anti-pattern block is a separate STEP 3 table, not co-located within the synthesis or unknowns section itself |

R3 design consequence: R2 V-04 and V-05 satisfy all 13 pre-v3 criteria. R3 explores three independent single-axis mechanisms that cover the new criteria, then combines.

**Three single-axis bets for R3:**
- **Axis A (V-01)**: Unknowns-as-section — extract the gap from confidence prose into a dedicated `## OPEN UNKNOWNS` section with typed `Unknown:` / `Impact:` / `Movement:` fields
- **Axis B (V-02)**: Hypothesis-revision lifecycle — `## PRELIMINARY HYPOTHESIS` block before all analysis sections, then `## SYNTHESIS` must explicitly confirm or revise it
- **Axis C (V-03)**: Section self-indictment — synthesis and unknowns sections each include an inline anti-pattern declaration naming the failure mode they avoid

---

## V-01 — Axis: Unknowns-as-Section

**Variation axis**: Output format — open unknowns extracted from confidence prose into a structurally separate section with typed fields

**Hypothesis**: The R2 confidence section's `Gap:` field satisfies C-12 (named unknowns) but embeds the unknown in a single prose line adjacent to the confidence basis. When confidence is MEDIUM or LOW, this makes omissions undetectable without parsing prose — a missing entry shows as absent text, not as a blank row. Extracting open unknowns into a standalone `## OPEN UNKNOWNS` section with three typed fields per entry (`Unknown:` / `Impact:` / `Movement:`) makes any gap structurally visible: a missing entry is a missing row, not absent prose. The typed fields also force three distinct questions per unknown — what it is, which dimension it affects, and how to close it — preventing the one-sentence collapse that was C-12's most common failure mode. Expected risk: the model may duplicate content between the confidence basis and the unknowns section; the instruction "do not list unknowns in the confidence section" is the guard.

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal files). Do not prompt unless context is absent.

Produce a sizing signal for the topic. A sizing signal answers: how much work is this, and how confident are we in that answer? It does NOT produce a project plan.

Follow the sections below in order. Every section is required.

---

## INERTIA CHECK

Before any sizing: what do teams or users do instead of this feature? Name the workaround and estimate its cost.

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

Each condition is ONE specific scenario that is absent today. "Several factors" is not a condition. "If requirements expand" is not specific.

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

This section is structurally separate from the confidence basis above. It lists the specific things that are NOT yet verified and that limit confidence.

Omitting this section when confidence is below HIGH fails the signal.
If confidence is fully grounded and no unknowns remain, state explicitly: "No open unknowns."

For each open unknown, fill all three fields:

Unknown: [the specific unverified item — name it concretely]
Impact: [which sizing dimension this most affects: complexity / timeline / team / confidence]
Movement: [the specific investigation or result that would close this unknown]

Repeat the three-field block for each distinct unknown. A generic placeholder like "dependencies may exist" fails — an unknown must name a specific dependency, decision, or contract.

---

## SYNTHESIS

Cross-reference at least two signal dimensions (complexity, timeline, confidence, inertia cost) to produce a decision-relevant observation. Dimensions must be combined to produce the conclusion — the conclusion must not be derivable from any single dimension alone.

Example form: "HIGH complexity + LOW confidence argues for a scoping spike before commitment" or "LOW inertia cost + MEDIUM complexity with known surface area argues for fast-track."

Restating each section in sequence ("Complexity is HIGH, timeline is 4–6 sprints, team needs 2 engineers") is juxtaposition, not synthesis.

---

## SIGNAL BOUNDARY

No task breakdowns. No sprint assignments. No owner names. No milestone dates.
This signal feeds program-plan. It does not replace it.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-02 — Axis: Hypothesis-Revision Lifecycle

**Variation axis**: Lifecycle emphasis — preliminary hypothesis committed before analysis; synthesis must explicitly confirm or revise it

**Hypothesis**: When the synthesis section is written after all other sections are populated, the model can construct a conclusion that merely echoes the inputs — a post-hoc rationalization that is indistinguishable from genuine cross-dimensional reasoning. Making the model commit to a preliminary hypothesis BEFORE the analysis sections creates a verifiable prior: the synthesis must either confirm or revise the hypothesis, naming the dimension that changed. If the hypothesis was "MEDIUM complexity, 3–5 sprints" and the analysis produces HIGH complexity, the synthesis must state "Hypothesis revised: complexity raised to HIGH because [driver]" — not describe HIGH complexity as if the hypothesis never existed. The prior commitment cannot be silently abandoned. This forces genuine reasoning: the synthesis becomes an audit of the analysis against the prior prediction, not a summary of it. Expected risk: the preliminary hypothesis may be vague enough ("medium effort") to provide no real constraint; the prompt requires a specific tier and sprint range, not a qualitative guess.

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal files). Do not prompt unless context is absent.

Produce a sizing signal. NOT a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates.

---

## PRELIMINARY HYPOTHESIS

Before analyzing the topic in detail, commit to a preliminary estimate. You will explicitly confirm or revise this hypothesis in the SYNTHESIS section at the end. Write it now, before the analysis sections below.

Hypothesis — complexity tier: [LOW / MEDIUM / HIGH / XL — pick one specific tier]
Hypothesis — timeline: [sprint range — "N–M sprints" — one range, not a range of ranges]
Reasoning: [one sentence — what prior knowledge or surface-level signal drives this guess?]

This commitment is required. A vague placeholder ("somewhere between medium and high") fails — state a specific tier and range. Imprecision is fine; absence is not.

---

## INERTIA CHECK

What do teams or users do instead of this feature?

Workaround: [the specific alternative]
Maintenance cost: [hours/sprint, error rate, manual effort, or qualitative]
Cost direction: [cheaper / comparable / more expensive — one word]

---

## SURFACE AREA

| # | Integration Point | Type | Description |
|---|-------------------|------|-------------|
| 1 | [name] | [API / event / data model / config / cross-service] | [brief] |
| ... | | | |
| **Total** | | | **N integration points** |

Total row required. Named points required.

---

## COMPLEXITY TIER AND DRIVER

Tier: [LOW / MEDIUM / HIGH / XL]
Primary driver: [one or two factors most responsible for this tier]

Tier sensitivity:
- Rises to [LEVEL] if [single named condition].
- Falls to [LEVEL] if [single named condition].

---

## TEAM AND TIMELINE SIGNAL

Team signal: [specialist disciplines + FTE fractions — e.g., "1 backend engineer, 0.5 PM"]
  "3 engineers" fails — no disciplines named.

Timeline signal: [sprint range — "N–M sprints"]

---

## CONFIDENCE

Confidence: [HIGH / MEDIUM / LOW]
Basis: [what IS known that supports this rating]
Gap: [the specific thing NOT yet verified — the primary unknown that limits confidence]
What would raise it: [specific investigation result that would move confidence up]

---

## SYNTHESIS

Look back at your PRELIMINARY HYPOTHESIS above. The synthesis must explicitly state whether the analysis confirms, revises, or partially revises it.

Choose one of these required forms:

- "Hypothesis confirmed: [tier] at [sprint range] holds because [cross-signal observation that required combining dimensions]"
- "Hypothesis revised: [dimension] changed from [prior value] to [current value] because [reason from analysis]"
- "Hypothesis partially revised: [what held] confirmed; [what changed] changed from [prior] to [current] because [reason]"

After the hypothesis statement, add the cross-signal observation: combine at least two dimensions (complexity, timeline, confidence, inertia cost) to produce a decision-relevant conclusion that requires both dimensions to state.

This section fails if it does not reference the preliminary hypothesis by name. Writing a synthesis that ignores the hypothesis is post-hoc rationalization — the conclusion was never actually constrained.

---

## SIGNAL BOUNDARY

No task breakdowns. No sprint assignments. No owner names. No milestone dates.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-03 — Axis: Section Self-Indictment

**Variation axis**: Phrasing register — synthesis and unknowns sections each include an inline declaration naming the failure mode they must avoid

**Hypothesis**: A synthesis that avoids juxtaposition and an unknowns section that avoids placeholders both require the model to enforce a quality standard actively, not passively populate a field. When a section's instruction explicitly names its own failure mode — "This section fails if it restates sections in sequence" / "A placeholder unknown like 'dependencies may exist' fails this section" — the model must check its output against the named anti-pattern rather than simply filling the field. This anti-pattern declaration changes the generation task from "produce a synthesis" to "produce a synthesis that is not juxtaposition," which is a more constrained and verifiable target. The key design decision is co-location: the anti-pattern must appear inside the section instruction, not in a separate step. Co-located anti-pattern language signals to the model that the quality check is part of that section's requirement, not an advisory. Expected risk: the model may add meta-commentary ("This is synthesis, not juxtaposition") without improving the actual conclusion quality; the instruction to demonstrate the standard through the conclusion form, not assert it, is the guard.

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal files). Do not prompt unless context is absent.

Produce a sizing signal. NOT a project plan. Every section below is required.

---

## INERTIA CHECK

Name the current workaround and its cost. Mandatory before any sizing begins.

Workaround: [the specific alternative in use]
Maintenance cost: [hours/sprint, error rate, manual effort, or qualitative]
Cost direction: [cheaper / comparable / more expensive — one word, required]

---

## SURFACE AREA

| # | Integration Point | Type | Description |
|---|-------------------|------|-------------|
| 1 | [name] | [API / event / data model / config / cross-service] | [brief] |
| ... | | | |
| **Total** | | | **N integration points** |

---

## COMPLEXITY TIER AND DRIVER

Tier: [LOW / MEDIUM / HIGH / XL — exactly this vocabulary]
Primary driver: [one or two factors most responsible]

Tier sensitivity:
- Rises to [LEVEL] if [single named condition].
- Falls to [LEVEL] if [single named condition].

---

## TEAM AND TIMELINE SIGNAL

Team signal: [specialist disciplines + FTE fractions + implementation ownership area per role]
  Failing: "2 engineers" — no disciplines or ownership.
  Passing: "1 backend engineer (owns API + event schema), 0.5 PM (owns alignment)"

Timeline signal: [sprint range — "N–M sprints" form required]

---

## CONFIDENCE

Confidence: [HIGH / MEDIUM / LOW]
Basis: [what IS known — specific evidence or prior work]
Gap: [what IS NOT yet verified — the primary unknown]
What would raise it: [specific investigation that closes the gap]

---

## OPEN UNKNOWNS

> **FAILURE MODE FOR THIS SECTION**: "Dependencies may exist" is a placeholder, not an unknown. "Third-party webhook rate limits are unverified" is an unknown — it names a specific item that has not been confirmed. This section fails if any entry is a generic hedge rather than a named specific dependency, decision, or contract.

For each open unknown, fill the typed fields. If no unknowns remain, state: "No open unknowns — confidence is fully grounded."

Unknown: [the specific unverified item — concrete, not generic]
Impact: [which dimension this most affects: complexity / timeline / team / confidence]
Movement: [what investigation resolves this — specific action or result]

---

## SYNTHESIS

> **FAILURE MODE FOR THIS SECTION**: Restating sections in sequence — "Complexity is HIGH. Timeline is 4–6 sprints. Confidence is MEDIUM." — is juxtaposition, not synthesis. This section fails if the conclusion can be produced by reading each field in order without combining them. Synthesis produces a conclusion that requires two or more dimensions to be combined; it cannot be derived from any single dimension alone.

Cross-reference at least two signal dimensions (complexity, timeline, confidence, inertia cost) to produce a directional observation.

Example form: "HIGH complexity + LOW confidence argues for deferral until contracts are published" or "LOW inertia cost + known surface area argues for fast-track even at MEDIUM complexity."

---

## SIGNAL BOUNDARY

No task breakdowns. No sprint assignments. No owner names. No milestone dates.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-04 — Axes: Unknowns-as-Section + Hypothesis-Revision Lifecycle

**Variation axes**: Output format (unknowns section) + Lifecycle emphasis (hypothesis-revision)

**Hypothesis**: C-14 and C-15 are orthogonal structural failures — C-14 governs where unknowns live (prose vs. dedicated section), C-15 governs when the synthesis conclusion is committed (post-hoc vs. pre-committed). They do not compete for the same structural real estate and adding both should not require trade-offs. The combination may also be self-reinforcing: having a standalone unknowns section gives the model explicit visibility into what it does not know, which may improve the accuracy of the preliminary hypothesis; and having the preliminary hypothesis creates a constraint that makes the synthesis more verifiable against the unknowns section (did the unknowns match the predicted gaps?). Expected risk: the preliminary hypothesis section appears before inertia, creating a long preamble before the first signal section; the ordering is intentional — the hypothesis is the only section that is not a signal field — so the preamble reads as a commitment record, not a warm-up.

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal files). Do not prompt unless context is absent.

Produce a sizing signal. NOT a project plan. No task breakdowns, sprint assignments, owner names, or milestone dates.

---

## PRELIMINARY HYPOTHESIS

Before detailed analysis, commit to a preliminary estimate. The SYNTHESIS section below must explicitly confirm or revise this commitment.

Hypothesis — complexity tier: [LOW / MEDIUM / HIGH / XL — one specific tier]
Hypothesis — timeline: [sprint range — "N–M sprints"]
Reasoning: [one sentence — what prior knowledge drives this estimate?]

This is a commitment, not a hedge. "Somewhere in the medium range" fails. If genuinely unknown, state "LOW — no surface-level signals suggest otherwise" and explain.

---

## INERTIA CHECK

What do teams do instead of this feature?

Workaround: [the specific alternative]
Maintenance cost: [hours/sprint, error rate, manual effort, or qualitative]
Cost direction: [cheaper / comparable / more expensive — one word]

---

## SURFACE AREA

| # | Integration Point | Type | Description |
|---|-------------------|------|-------------|
| 1 | [name] | [API / event / data model / config / cross-service] | [brief] |
| ... | | | |
| **Total** | | | **N integration points** |

Total row required. Named points required.

---

## COMPLEXITY TIER AND DRIVER

Tier: [LOW / MEDIUM / HIGH / XL]
Primary driver: [one or two factors most responsible]

Tier sensitivity:
- Rises to [LEVEL] if [single named condition].
- Falls to [LEVEL] if [single named condition].

Each condition is one specific, testable scenario absent today.

---

## TEAM AND TIMELINE SIGNAL

Team signal: [specialist disciplines + FTE fractions + implementation ownership per role]
  Each named role must include its ownership scope.

Timeline signal: [sprint range — "N–M sprints"]

---

## CONFIDENCE

Confidence: [HIGH / MEDIUM / LOW]
Basis: [what IS known — specific evidence or reasoning that supports this rating]

Do not list unknowns here. They go in the OPEN UNKNOWNS section below.

---

## OPEN UNKNOWNS

This section is structurally separate from the confidence basis. It holds specific items not yet verified. Generic hedges fail.

If no unknowns remain, state: "No open unknowns."

For each open unknown:

Unknown: [the specific unverified item — name it concretely]
Impact: [which dimension this most affects: complexity / timeline / team / confidence]
Movement: [the specific investigation or result that would resolve this]

---

## SYNTHESIS

Look back at your PRELIMINARY HYPOTHESIS. State whether the analysis confirms, revises, or partially revises it.

Required form — choose one:
- "Hypothesis confirmed: [tier] at [sprint range] because [cross-signal observation]"
- "Hypothesis revised: [dimension] changed from [prior value] to [current value] because [reason]"
- "Hypothesis partially revised: [confirmed dimension] confirmed; [revised dimension] changed from [prior] to [current] because [reason]"

After the hypothesis statement, add the cross-signal observation: combine at least two dimensions (complexity, timeline, confidence, inertia cost) to produce a decision-relevant conclusion that requires both dimensions to state — not derivable from either alone.

This section fails if it does not reference the preliminary hypothesis. Ignoring the hypothesis and synthesizing directly from the analysis sections is post-hoc rationalization.

---

## SIGNAL BOUNDARY

No task breakdowns. No sprint assignments. No owner names. No milestone dates.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-05 — Full Integration (all v3 axes + AMEND cascade + R2 best practices)

**Variation axes**: All three v3 axes (C-14, C-15, C-17) + AMEND cascade (C-16) + R2 V-05 self-check expanded to 17 criteria

**Hypothesis**: The three independent structural mechanisms for the new v3 criteria each address a different failure mode: C-14 (unknowns section with typed fields) makes omissions structurally visible, C-15 (hypothesis-revision) makes synthesis verifiable against a prior commitment, C-17 (section self-indictment) makes quality enforcement active rather than passive. C-16 (AMEND cascade) adds a fourth mechanism: after any amendment, the synthesis must be re-evaluated if the amended dimension appears in it. In isolation, each mechanism may be sufficient for its target criterion. In combination, they create a mutually reinforcing structure — the hypothesis constrains the synthesis, the unknowns section constrains the confidence gap, the anti-pattern declarations constrain both, and the AMEND cascade prevents silent contradiction after amendment. The 17-criterion self-check enumerates all criteria so any violation is visible before the artifact is written. Expected risk: length is the primary failure mode for this variation; the ordered structure (hypothesis → analysis → unknowns → synthesis) and co-located anti-pattern callouts are the primary guards against rule dilution.

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal files). Do not prompt unless context is absent.

Produce a sizing signal. This is NOT a project plan. Signal boundary: no task breakdowns, sprint assignments, owner names, or milestone dates. Remove any violations before writing the artifact.

Follow every step in order. Every labeled row and field is required.

---

**MANDATORY OPENING: PRELIMINARY HYPOTHESIS**

Before any analysis, commit to a preliminary estimate. You will confirm or revise it in SYNTHESIS.

Hypothesis — complexity tier: [LOW / MEDIUM / HIGH / XL — one specific tier, commit]
Hypothesis — timeline: [sprint range — "N–M sprints" — one range]
Reasoning: [one sentence — what signals the scope before detailed analysis?]

Failing form: "Hard to say without more analysis." The hypothesis is a prior commitment — state a specific tier and range. If genuinely uncertain, pick LOW as default and note the uncertainty.

---

**STEP 1: INERTIA CHECK**

> WRONG: "Teams use a workaround currently." — Workaround named; cost direction absent. Fails.
> CORRECT: "Manual CSV re-import per team — building is **more expensive** upfront but **cheaper** to maintain long-term; the workaround costs ~2h/sprint/team and scales linearly with team count."

Workaround: [name the specific alternative in use]
Maintenance cost: [estimate the ongoing cost]
Cost direction: [cheaper / comparable / more expensive — one word, required]

---

**STEP 2: SURFACE AREA**

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

Failing forms for sensitivity:

| Failing form | Why it fails |
|---|---|
| "Several factors could push this to XL" | Not one named condition |
| "If requirements expand" | Cannot be tested |
| "If integration proves complex" | Restates the tier, names nothing new |
| "If the timeline slips" | Wrong dimension — timeline sensitivity, not tier sensitivity |

A named condition is specific and testable: "If offline sync is required" can be tested. "If requirements expand" cannot.

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

Do not list unknowns here. They go in STEP 6.

---

**STEP 6: OPEN UNKNOWNS**

> **FAILURE MODE FOR THIS SECTION**: "Dependencies may exist" is a placeholder, not an unknown. An unknown must name a specific dependency, decision, or contract that has not been verified. A generic hedge fails this section exactly as silently as an absent section — the structural separation from confidence prose exists to make omissions visible, not to create a section that can be filled with vague language.

List open unknowns with typed fields. If none remain (confidence is fully grounded), state: "No open unknowns."

For each open unknown:

Unknown: [the specific unverified item — concrete, testable]
Impact: [which dimension this most affects: complexity / timeline / team / confidence]
Movement: [the specific investigation or result that closes this unknown]

---

**STEP 7: SYNTHESIS**

> **FAILURE MODE FOR THIS SECTION**: Restating sections in sequence — "Complexity is HIGH. Timeline is 4–6 sprints. Confidence is MEDIUM." — is juxtaposition, not synthesis. This section fails if the conclusion is derivable from any single field alone. Synthesis requires a conclusion that could not be stated without combining two or more dimensions.

First, look back at your PRELIMINARY HYPOTHESIS. State whether the analysis confirms, revises, or partially revises it:

- "Hypothesis confirmed: [tier] at [sprint range] because [cross-signal observation]"
- "Hypothesis revised: [dimension] changed from [prior value] to [current value] because [reason]"
- "Hypothesis partially revised: [what held] confirmed; [what changed] changed from [prior] to [current] because [reason]"

After the hypothesis statement, add the cross-signal directional observation: combine at least two dimensions (complexity, timeline, confidence, inertia cost) to produce a recommendation. The recommendation must require both dimensions to state.

**AMEND INSTRUCTION**: If an AMEND directive is present in this invocation, complete the amendment fully, then re-read this synthesis. If the amended dimension appears in the synthesis conclusion, update the conclusion or explicitly reaffirm it in light of the amendment. Leaving the synthesis unchanged after amending a dimension it cites is a silent contradiction — it fails C-16.

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
- [ ] C-09: At least one explicit exclusion, assumption, or out-of-scope boundary is named in the output
- [ ] C-10: Break-even signal present, or explicitly stated that it cannot be assessed and why
- [ ] C-11: Each named specialization includes an implementation ownership area
- [ ] C-12: At least one specific unknown named that would move confidence if resolved, or "no open unknowns" stated
- [ ] C-13: Synthesis cross-references two or more signal dimensions to produce a directional conclusion
- [ ] C-14: Open unknowns appear in a named section separate from confidence basis, with Unknown: / Impact: / Movement: fields; or "No open unknowns" stated explicitly
- [ ] C-15: Preliminary hypothesis stated before analysis; synthesis explicitly confirms or revises it, naming the dimension that changed
- [ ] C-16: If AMEND present and amended dimension appears in synthesis, synthesis updated or reaffirmed; absent or no overlap → pass by default
- [ ] C-17: At least one aspirational section (synthesis or unknowns) contains a sentence naming the anti-pattern being avoided

Fix any violation before writing.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## Variation Summary

| ID | Axis | Primary bet | C-14 | C-15 | C-16 | C-17 |
|----|------|-------------|------|------|------|------|
| V-01 | Unknowns-as-section | Typed Unknown:/Impact:/Movement: fields make omissions structurally visible as blank rows | **High** | Low — no hypothesis mechanism | Low — no AMEND cascade | Medium — synthesis note only |
| V-02 | Hypothesis-revision lifecycle | Pre-committed hypothesis forces synthesis to confirm or revise; silent abandonment fails | Low — gap in confidence prose | **High** | Low — no AMEND cascade | Low — no inline anti-patterns |
| V-03 | Section self-indictment | Inline failure-mode declaration in synthesis + unknowns sections enforces quality at generation time | Medium — unknowns section present | Low — no hypothesis | Low — no AMEND cascade | **High** |
| V-04 | Unknowns-as-section + Hypothesis-revision | C-14 and C-15 are orthogonal; unknowns section improves hypothesis accuracy; hypothesis commitment constrains synthesis | **High** | **High** | Low — no AMEND cascade | Medium — synthesis anti-pattern inline |
| V-05 | Full integration | All axes + AMEND cascade instruction + 17-criterion self-check; mutually reinforcing structure | **High** | **High** | **High** | **High** |

**Key design differences from R2:**

- **C-14 mechanism**: R2 Gap field is a single prose line in the confidence section. R3 V-01, V-04, V-05 extract it into a standalone section with three typed fields per unknown — structural separation makes omissions visible as absent rows, not absent prose.
- **C-15 mechanism**: R2 has no pre-analysis commitment; synthesis is written post-hoc. R3 V-02, V-04, V-05 require a PRELIMINARY HYPOTHESIS block before any analysis section, and require the synthesis to explicitly reference and confirm or revise it — making the conclusion verifiable against a prior commitment.
- **C-16 mechanism**: R2 AMEND instruction changes the field value but does not instruct synthesis re-evaluation. R3 V-05 adds an explicit AMEND INSTRUCTION inside the synthesis step that requires re-reading and updating or reaffirming synthesis when the amended dimension appears in the conclusion.
- **C-17 mechanism**: R2 anti-pattern table appears in a separate STEP 3 block covering sensitivity. R3 V-03, V-04 (partial), V-05 co-locate the anti-pattern declaration inside the synthesis and unknowns sections themselves — making the quality check structurally part of each section's requirement rather than a separate advisory step.
- **Cross-coverage**: V-01 through V-03 each target one new criterion through independent structural mechanisms, establishing that each criterion can be achieved in isolation before combining.
