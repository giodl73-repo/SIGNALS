---
skill: quest-variate
skill_target: scout-size
round: 10
date: 2026-03-17
rubric: simulations/quest/rubrics/scout-size-rubric-v10-2026-03-17.md
axes_explored: [depth-behavior-disqualifying-forms, essential-recommended-scope-extension, minimal-combination-30-31, fuller-integration-table-format, full-integration-all-31-disqualifying]
r9_champion: V-05 (21/21 under v9 — fails C-30 and C-31 under v10)
r9_gap: C-09-C-17 self-check items carry pass-condition descriptions only (fails C-30); essential and recommended criteria absent from self-check scope (fails C-31)
r10_target: C-30 (depth/behavior aspirational criteria get exact disqualifying forms in self-check), C-31 (self-check extends to cover C-01-C-08)
---

# scout-size -- Prompt Variations R10

Five complete, runnable skill body prompts targeting the v10 rubric (31 criteria). Single-axis first
(V-01 through V-02), minimal combination (V-03), fuller integration (V-04), full gold standard (V-05).

## Context: what informed this round

R9 V-05 achieves 21/21 under v9. Under v10 it fails two new criteria:

| New criterion | What it requires | R9 V-05 gap |
|---|---|---|
| **C-30** | Self-check items for depth/behavior aspirational criteria (C-09-C-17) include exact disqualifying forms alongside pass conditions | C-09-C-17 self-check items carry pass-condition descriptions only -- same state structural criteria (C-18-C-25) were in before C-29 required disqualifying-form precision there |
| **C-31** | Self-check extends to cover essential (C-01-C-05) and recommended (C-06-C-08) criteria | Self-check is bounded at aspirational criteria -- C-01-C-08 absent from verification trace entirely |

C-30 and C-31 are orthogonal: C-30 is about *precision within a category* (depth/behavior criteria need the
same disqualifying-form treatment structural criteria got under C-29); C-31 is about *scope* (the self-check
needs to extend beyond aspirational criteria to all 31). An output can close C-30 while still failing C-31,
and vice versa.

**Three axes for R10:**
- **Axis A (V-01)**: Depth/behavior disqualifying forms -- adds exact disqualifying forms to C-09-C-17 in
  self-check; C-01-C-08 intentionally absent (fails C-31). Tests C-30 in isolation.
- **Axis B (V-02)**: Essential/recommended scope extension -- adds C-01-C-08 entries to self-check with
  pass/fail + evidence; C-09-C-17 retain pass-condition-only descriptions (fails C-30). Tests C-31 in isolation.
- **Axis C (V-03)**: Minimal combination -- adds both sets without other structural changes.

**All five variations share an identical body** (PRE-FLIGHT GATE through SIGNAL BOUNDARY CHECK). The body is
the R9 V-05 base unchanged. Only the SELF-CHECK section differs across variations.

---

## V-01 -- Axis: Depth/behavior disqualifying forms (C-30)

**Variation axis**: Self-check precision for depth/behavior criteria -- adds exact disqualifying forms to
C-09-C-17, mirroring the disqualifying-form treatment C-29 established for structural criteria (C-18-C-27).
C-01-C-08 intentionally absent from self-check (C-31 fails by design).

**Hypothesis**: C-30 is achievable by extending the disqualifying-form treatment from structural criteria to
depth/behavior criteria without adding C-01-C-08 scope. The discriminator is whether each depth/behavior
criterion names the exact output pattern that satisfies the surface signal but fails the criterion. C-31 is
intentionally absent: expected pass C-01-C-29, C-30; expected fail C-31. Score: 22/23 (99.57).

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal files). Do not prompt unless
context is absent.

Produce a sizing signal. This is NOT a project plan. Signal boundary: no task breakdowns, sprint assignments,
owner names, or milestone dates. Remove any violations before writing the artifact.

Follow every step in order. Every labeled row and field is required.

---

**PRE-FLIGHT GATE -- complete before any analysis begins**

All three fields below are preconditions for all analysis sections, including STEP 1 through STEP 7. Resolve
them from repo context now. Do not proceed until all three fields contain specific responses -- "TBD" or blank
fails any field.

Out-of-scope boundary:
[Name at least one sub-system, phase, integration, or behavior explicitly NOT covered by this sizing. If
genuinely full implementation scope: "No exclusions -- full scope assumed." Do not say "TBD."]

Break-even signal:
[At what usage level, team count, or time horizon does building this feature recover its cost vs. the current
workaround? State a rough signal or explicitly: "Cannot assess -- [specific reason]." Absence fails C-10
before analysis begins.]

Preliminary hypothesis:
Tier: [LOW / MEDIUM / HIGH / XL -- commit to one tier now]
Timeline: [N-M sprints -- commit now]
Reasoning: [one sentence -- what signals the scope before detailed analysis?]

STOP: All three fields must contain specific responses. Do not proceed to STEP 1 or any STEP below until this
gate is fully resolved.

Enforcement contract for this gate's commitments:
- Scope exclusions: enforced in STEP 1 INERTIA CHECK (prohibits scope qualifications), STEP 2 SURFACE AREA
  (prohibits scope exclusions), STEP 3 COMPLEXITY (prohibits scope exclusions), and STEP 7 SYNTHESIS
  (prohibits scope exclusions) -- each section is explicitly closed against scope content.
- Hypothesis: confirmed or revised in STEP 7 SYNTHESIS, which names this gate by label at both the anchor
  instruction ("look back at PRE-FLIGHT GATE") and the verdict close ("The preliminary hypothesis committed
  in PRE-FLIGHT GATE...").

---

**STEP 1: INERTIA CHECK**

> WRONG: "Teams use a workaround currently." -- No cost direction. Fails.
> CORRECT: "Manual CSV re-import per team -- building is more expensive upfront but cheaper to maintain;
> workaround costs ~2h/sprint/team and scales linearly with team count."

Workaround: [name the specific alternative in use]
Maintenance cost: [estimate the ongoing cost]
Cost direction: [cheaper / comparable / more expensive -- one word, required]

Do not add scope boundary notes or exclusion qualifications here -- scope was resolved in PRE-FLIGHT GATE,
not in analysis steps.

---

**STEP 2: SURFACE AREA**

Do not include scope exclusions here -- scope was resolved in PRE-FLIGHT GATE, not in analysis steps.

| # | Integration Point | Type | Description |
|---|-------------------|------|-------------|
| 1 | [name] | [API / event / data model / config / cross-service] | [brief] |
| ... | | | |
| **Total** | | | **N integration points** |

Total row required. "Several integration points" is not an enumeration.

---

**STEP 3: COMPLEXITY TIER AND DRIVER**

Tier: [LOW / MEDIUM / HIGH / XL -- exactly this vocabulary]
Primary driver: [one or two factors most responsible]

Tier sensitivity -- use this exact template:

    Tier rises to [LEVEL] if [single named condition].
    Tier falls to [LEVEL] if [single named condition].

Do not include scope exclusions here -- scope was resolved in PRE-FLIGHT GATE, not in analysis steps.
Do not embed unknowns here (e.g., "uncertainty about X may raise the tier") -- unknowns belong in STEP 6
OPEN UNKNOWNS, not in analysis sections.

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
  Failing: "3 engineers" -- no disciplines, no ownership.
  Passing: "1 backend engineer (owns event schema + API layer), 1 infra engineer (owns deployment pipeline),
           0.5 PM (owns stakeholder coordination)"

Timeline signal: [sprint range -- "N-M sprints"]
  Failing: "Q3 2026" (calendar date), "4 sprints" (point estimate, not a range)

---

**STEP 5: CONFIDENCE**

Confidence: [HIGH / MEDIUM / LOW]
Basis: [what IS known -- specific evidence, prior work, or verified reasoning]

Do not list unknowns here -- unknowns belong in STEP 6 OPEN UNKNOWNS, not in the confidence basis. This
section is explicitly closed against unknowns -- listing one here creates a second, unguarded record outside
the canonical home that STEP 6 provides.

---

**STEP 6: OPEN UNKNOWNS**

> **FAILURE MODE FOR THIS SECTION**: "Dependencies may exist" is a placeholder, not an unknown. An unknown
> must name a specific dependency, decision, or contract that has not been verified. A generic hedge fails
> exactly as silently as an absent section -- the structural separation from STEP 5 exists to make omissions
> visible, not to create a section that can be filled with vague language. Do not include scope exclusions
> here -- scope was resolved in PRE-FLIGHT GATE. Do not include break-even observations here -- break-even
> was resolved in PRE-FLIGHT GATE.

List open unknowns with typed fields. If none remain, state: "No open unknowns."

For each open unknown:

Unknown: [the specific unverified item -- concrete, testable]
Impact: [which dimension this most affects: complexity / timeline / team / confidence]
Movement: [the specific investigation or result that closes this unknown]

---

**STEP 7: SYNTHESIS**

> **FAILURE MODE FOR THIS SECTION**: Restating sections in sequence -- "Complexity is HIGH. Timeline is
> 4-6 sprints. Confidence is MEDIUM." -- is juxtaposition, not synthesis. This section fails if the
> conclusion is derivable from any single field alone. Do not embed unknowns here -- they belong in STEP 6.
> Do not include scope exclusions here -- scope was resolved in PRE-FLIGHT GATE.

First: look back at PRE-FLIGHT GATE -- the preliminary hypothesis committed there was [tier] at [N-M
sprints]. State whether the analysis confirms, revises, or partially revises the commitment made in
PRE-FLIGHT GATE using a structured commitment-chain trace. All three labeled lines must appear on separate
lines. A single sentence that mentions the tier, the analysis, and the verdict is juxtaposition-in-miniature
-- the chain must be scannable at a glance, with each step independently readable.

Commitment chain:
Gate commitment: [tier committed in PRE-FLIGHT GATE] / [sprint range committed in PRE-FLIGHT GATE]
Analysis: [key evidence from STEPs 1-6 bearing on the commitment -- name at least two signal dimensions]
Verdict: [use exactly one of the following forms -- the phrase "committed in PRE-FLIGHT GATE" is required]
  -- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N-M sprints]) is confirmed:
     [cross-signal observation combining at least two dimensions]."
  -- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N-M sprints]) is revised:
     [dimension] moved from [prior value] to [current value] because [reason]."
  -- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N-M sprints]) is partially revised:
     [what held]; [what changed] because [reason]."

The verdict close must name PRE-FLIGHT GATE by label -- not a hypothesis constructed after the sections were
filled, but the specific commitment made in the gate. Writing "my earlier estimate was confirmed" fails C-22.
Writing the verdict as a prose paragraph containing all three chain steps fails C-24.

After the verdict, add the cross-signal directional observation: combine at least two dimensions (complexity,
timeline, confidence, inertia cost) to produce a recommendation. The recommendation must require both
dimensions to state.

**STRUCTURAL AMEND RE-EVALUATION DIRECTIVE**: This synthesis section carries a written re-evaluation
requirement that applies on every invocation, independent of whether an AMEND directive is present. When
AMEND is absent: confirm no active amendment and proceed. When AMEND is present and the amended dimension
appears in the cross-signal conclusion or verdict above: re-evaluate that conclusion before closing this
section -- update it or explicitly reaffirm that it still holds. This requirement is a structural property
of this section's template, not a conditional check. Leaving this conclusion unchanged after amending a
dimension cited here is a structural failure of this section's integrity.

---

**SIGNAL BOUNDARY CHECK**

Before writing the artifact, scan and remove:
- [ ] Task breakdowns ("Step 1: implement X")
- [ ] Sprint assignments ("Sprint 2: auth integration")
- [ ] Owner names ("Alice owns the backend work")
- [ ] Milestone dates ("Targeting March delivery")

---

**SELF-CHECK -- ASPIRATIONAL CRITERIA (C-09 through C-31)**

Essential (C-01-C-05) and recommended (C-06-C-08) criteria are enforced by section templates above and are
not audited in this self-check. This check covers all 23 aspirational criteria.

- [ ] C-09: At least one explicit exclusion named in PRE-FLIGHT GATE.
  Disqualifying form: "Standard integrations excluded" fails C-09 -- it names a category, not a specific
  sub-system or integration; the exclusion must identify what is out of scope, not imply a class.

- [ ] C-10: Break-even signal present in PRE-FLIGHT GATE, or "Cannot assess -- [reason]" stated.
  Disqualifying form: "Break-even depends on adoption" fails C-10 -- it does not state a threshold or
  explain why the threshold cannot be estimated; a rough signal or explicit inability with a named reason
  is required.

- [ ] C-11: Each named specialization includes an implementation ownership area.
  Disqualifying form: "1 backend engineer, 1 infra engineer" fails C-11 -- disciplines named but no
  ownership scope follows; ownership must be attached to each role, not summarized in a separate sentence.

- [ ] C-12: At least one specific unknown named that would move confidence, or "No open unknowns" stated.
  Disqualifying form: "External dependencies may affect timeline" fails C-12 -- it names a risk category,
  not a specific dependency whose resolution would move the confidence level.

- [ ] C-13: Synthesis cross-references two or more dimensions to produce a conclusion not derivable from
  any single field alone.
  Disqualifying form: "Complexity is HIGH and timeline is 4-6 sprints, so this requires careful planning"
  fails C-13 -- "careful planning" is derivable from complexity alone; a C-13-passing conclusion would be
  unstateable if either dimension were unknown.

- [ ] C-14: Open unknowns in STEP 6 with typed fields; STEP 5 explicitly closed against unknowns.
  Disqualifying form: a CONFIDENCE basis reading "Timeline unclear pending auth service contract" fails
  C-14 -- STEP 5 carries an unknown that belongs in STEP 6; structural separation exists but is leaky.

- [ ] C-15: Preliminary hypothesis inside PRE-FLIGHT GATE; synthesis confirms or revises it naming
  the committed values.
  Disqualifying form: "My earlier estimate held" fails C-15 -- it confirms without naming the committed
  tier and sprint range; the confirmation must cite the specific values to be verifiable against the gate.

- [ ] C-16: If AMEND present and amended dimension in synthesis, synthesis updated or reaffirmed; default
  pass if no AMEND or no overlap.
  Disqualifying form: when AMEND changes confidence and confidence appears in the cross-signal conclusion,
  leaving the conclusion unrevised without a reaffirmation statement fails C-16.

- [ ] C-17: At least one aspirational section contains a sentence naming the specific anti-pattern.
  Disqualifying form: "This section may produce weak output" fails C-17 -- it names a quality risk without
  identifying the specific anti-pattern form (juxtaposition: restating fields in sequence); the named form
  must be specific enough that a reader could identify it in a failing output.

- [ ] C-18: PRE-FLIGHT GATE appears before all STEPs; contains scope boundary, break-even, and preliminary
  hypothesis fields; includes stop instruction; inline reminders inside sections do not count.
  Disqualifying form: a scope boundary field inside STEP 3 satisfies C-09 content but fails C-18 -- it is
  a section reminder, not a pre-analysis gate field; the gate must structurally precede STEP 1.

- [ ] C-19: At least one section adjacent to OPEN UNKNOWNS (STEP 5) and at least one adjacent to scope
  exclusion canonical home (STEP 2 or STEP 3) carry explicit prohibition rules.
  Disqualifying form: a CONFIDENCE section listing two unknowns without a prohibition fails C-19 -- the
  canonical home (STEP 6) exists but the adjacent section is unguarded.

- [ ] C-20: Every plausible recipient section for scope exclusion content (STEP 1, STEP 2, STEP 3, STEP 7)
  and for unknowns content (STEP 3, STEP 5, STEP 7) carries an explicit prohibition.
  Disqualifying form: STEP 2 and STEP 3 carry scope prohibitions but STEP 1 and STEP 7 do not -- fails
  C-20 even if C-19 passes; all plausible recipients must be guarded.

- [ ] C-21: Preliminary hypothesis is a field inside PRE-FLIGHT GATE. Synthesis references "PRE-FLIGHT
  GATE" by name and explicitly confirms or revises the commitment.
  Disqualifying form: a standalone "PRELIMINARY ESTIMATE" section after PRE-FLIGHT GATE but before STEP 1
  fails C-21 -- hypothesis is outside the gate block; passing C-18 and C-15 independently does not satisfy
  C-21 if the hypothesis field is structurally separate from the gate.

- [ ] C-22: Synthesis names PRE-FLIGHT GATE at both ends: (1) anchor instruction and (2) verdict close.
  Disqualifying form: "My earlier estimate was confirmed" fails C-22 -- "PRE-FLIGHT GATE" must appear by
  name at both the anchor ("look back at PRE-FLIGHT GATE") and the verdict ("committed in PRE-FLIGHT
  GATE...").

- [ ] C-23: For at least one canonical field type, prohibition guards in adjacent sections name the
  canonical home by label.
  Disqualifying form: "Do not include scope exclusions here" fails C-23 -- it closes a door without
  naming where scope belongs; passing form: "scope was resolved in PRE-FLIGHT GATE, not in analysis steps."

- [ ] C-24: Synthesis includes a Commitment chain with three labeled lines on separate lines:
  Gate commitment: / Analysis: / Verdict:.
  Disqualifying form: "The preliminary hypothesis committed in PRE-FLIGHT GATE (MEDIUM, 3-5 sprints) is
  confirmed: surface area is LOW and inertia cost is HIGH" fails C-24 -- all three steps in one sentence;
  the chain must be independently scannable with each step on its own labeled line.

- [ ] C-25: PRE-FLIGHT GATE includes an enforcement contract naming at least two sections responsible for
  scope exclusions AND the section responsible for hypothesis confirmation.
  Disqualifying form: "All three fields above are preconditions for STEP 1 through STEP 7" fails C-25 --
  naming steps as a continuation instruction is not an enforcement contract; scope vs. hypothesis
  enforcement must be distinguished.

- [ ] C-26: Synthesis contains a STRUCTURAL AMEND RE-EVALUATION DIRECTIVE applying on every invocation
  "independent of whether an AMEND directive is present," framing non-compliance as "a structural failure
  of this section's integrity."
  Disqualifying form: "If an AMEND directive is present in this invocation...it fails C-16" fails C-26 --
  "in this invocation" is conditional; "it fails C-16" is criterion-referenced, not a structural property.

- [ ] C-27: Both STEP 6 and STEP 7 carry a dedicated labeled FAILURE MODE block
  (> **FAILURE MODE FOR THIS SECTION**:) as a structurally separate element.
  Disqualifying form: > **Anti-pattern**: Restating sections in sequence is juxtaposition fails C-27 --
  it is structural annotation embedded in instruction prose, not a dedicated block whose absence leaves a
  visible structural gap.

- [ ] C-28: Output includes a structured self-check covering all aspirational criteria (C-09-C-31) with
  pass/fail determination and supporting evidence per criterion.
  Disqualifying form: section-level FAILURE MODE blocks in STEP 6 and STEP 7 do not satisfy C-28 -- they
  are section-level structural elements; C-28 requires a separate collective audit block evaluating every
  criterion by ID.

- [ ] C-29: Self-check items for all structural criteria (C-18-C-27) include both a pass condition and an
  exact structural disqualifying form.
  Disqualifying form: "C-25: PRE-FLIGHT GATE names its enforcement sections" fails C-29 -- it describes
  the pass condition without naming an exact pattern that satisfies the surface signal but fails.

- [ ] C-30: Self-check items for all depth and behavior aspirational criteria (C-09-C-17) include both a
  pass condition and an exact disqualifying form.
  Disqualifying form: "C-09: At least one explicit exclusion named" fails C-30 -- it describes the pass
  condition only; the disqualifying form must name the exact output pattern that looks like compliance
  but fails the criterion.

- [ ] C-31: Self-check includes coverage of all essential (C-01-C-05) and recommended (C-06-C-08) criteria
  with pass/fail determination and supporting evidence.
  Essential and recommended criteria are absent from this self-check. C-31 FAILS in this variation --
  intended single-axis design: C-30 is the only new criterion targeted.

Fix any violation before writing.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-02 -- Axis: Essential/recommended scope extension (C-31)

**Variation axis**: Self-check scope -- extends verification trace to cover C-01-C-08 with pass/fail
determination and supporting evidence. C-09-C-17 retain pass-condition-only descriptions (C-30 fails by
design).

**Hypothesis**: C-31 is achievable by adding C-01-C-08 entries to the self-check without adding disqualifying
forms to depth/behavior criteria. The discriminator is whether essential and recommended criteria appear in
the self-check with explicit pass/fail determinations -- not whether they have disqualifying forms. C-30 is
intentionally absent: expected pass C-01-C-29, C-31; expected fail C-30. Score: 22/23 (99.57).

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal files). Do not prompt unless
context is absent.

Produce a sizing signal. This is NOT a project plan. Signal boundary: no task breakdowns, sprint assignments,
owner names, or milestone dates. Remove any violations before writing the artifact.

Follow every step in order. Every labeled row and field is required.

---

**PRE-FLIGHT GATE -- complete before any analysis begins**

All three fields below are preconditions for all analysis sections, including STEP 1 through STEP 7. Resolve
them from repo context now. Do not proceed until all three fields contain specific responses -- "TBD" or blank
fails any field.

Out-of-scope boundary:
[Name at least one sub-system, phase, integration, or behavior explicitly NOT covered by this sizing. If
genuinely full implementation scope: "No exclusions -- full scope assumed." Do not say "TBD."]

Break-even signal:
[At what usage level, team count, or time horizon does building this feature recover its cost vs. the current
workaround? State a rough signal or explicitly: "Cannot assess -- [specific reason]." Absence fails C-10
before analysis begins.]

Preliminary hypothesis:
Tier: [LOW / MEDIUM / HIGH / XL -- commit to one tier now]
Timeline: [N-M sprints -- commit now]
Reasoning: [one sentence -- what signals the scope before detailed analysis?]

STOP: All three fields must contain specific responses. Do not proceed to STEP 1 or any STEP below until this
gate is fully resolved.

Enforcement contract for this gate's commitments:
- Scope exclusions: enforced in STEP 1 INERTIA CHECK (prohibits scope qualifications), STEP 2 SURFACE AREA
  (prohibits scope exclusions), STEP 3 COMPLEXITY (prohibits scope exclusions), and STEP 7 SYNTHESIS
  (prohibits scope exclusions) -- each section is explicitly closed against scope content.
- Hypothesis: confirmed or revised in STEP 7 SYNTHESIS, which names this gate by label at both the anchor
  instruction ("look back at PRE-FLIGHT GATE") and the verdict close ("The preliminary hypothesis committed
  in PRE-FLIGHT GATE...").

---

**STEP 1: INERTIA CHECK**

> WRONG: "Teams use a workaround currently." -- No cost direction. Fails.
> CORRECT: "Manual CSV re-import per team -- building is more expensive upfront but cheaper to maintain;
> workaround costs ~2h/sprint/team and scales linearly with team count."

Workaround: [name the specific alternative in use]
Maintenance cost: [estimate the ongoing cost]
Cost direction: [cheaper / comparable / more expensive -- one word, required]

Do not add scope boundary notes or exclusion qualifications here -- scope was resolved in PRE-FLIGHT GATE,
not in analysis steps.

---

**STEP 2: SURFACE AREA**

Do not include scope exclusions here -- scope was resolved in PRE-FLIGHT GATE, not in analysis steps.

| # | Integration Point | Type | Description |
|---|-------------------|------|-------------|
| 1 | [name] | [API / event / data model / config / cross-service] | [brief] |
| ... | | | |
| **Total** | | | **N integration points** |

Total row required. "Several integration points" is not an enumeration.

---

**STEP 3: COMPLEXITY TIER AND DRIVER**

Tier: [LOW / MEDIUM / HIGH / XL -- exactly this vocabulary]
Primary driver: [one or two factors most responsible]

Tier sensitivity -- use this exact template:

    Tier rises to [LEVEL] if [single named condition].
    Tier falls to [LEVEL] if [single named condition].

Do not include scope exclusions here -- scope was resolved in PRE-FLIGHT GATE, not in analysis steps.
Do not embed unknowns here -- unknowns belong in STEP 6 OPEN UNKNOWNS, not in analysis sections.

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
  Failing: "3 engineers" -- no disciplines, no ownership.
  Passing: "1 backend engineer (owns event schema + API layer), 1 infra engineer (owns deployment pipeline),
           0.5 PM (owns stakeholder coordination)"

Timeline signal: [sprint range -- "N-M sprints"]
  Failing: "Q3 2026" (calendar date), "4 sprints" (point estimate, not a range)

---

**STEP 5: CONFIDENCE**

Confidence: [HIGH / MEDIUM / LOW]
Basis: [what IS known -- specific evidence, prior work, or verified reasoning]

Do not list unknowns here -- unknowns belong in STEP 6 OPEN UNKNOWNS, not in the confidence basis. This
section is explicitly closed against unknowns.

---

**STEP 6: OPEN UNKNOWNS**

> **FAILURE MODE FOR THIS SECTION**: "Dependencies may exist" is a placeholder, not an unknown. An unknown
> must name a specific dependency, decision, or contract that has not been verified. A generic hedge fails
> exactly as silently as an absent section. Do not include scope exclusions here -- scope was resolved in
> PRE-FLIGHT GATE. Do not include break-even observations here -- break-even was resolved in PRE-FLIGHT GATE.

List open unknowns with typed fields. If none remain, state: "No open unknowns."

For each open unknown:

Unknown: [the specific unverified item -- concrete, testable]
Impact: [which dimension this most affects: complexity / timeline / team / confidence]
Movement: [the specific investigation or result that closes this unknown]

---

**STEP 7: SYNTHESIS**

> **FAILURE MODE FOR THIS SECTION**: Restating sections in sequence -- "Complexity is HIGH. Timeline is
> 4-6 sprints. Confidence is MEDIUM." -- is juxtaposition, not synthesis. This section fails if the
> conclusion is derivable from any single field alone. Do not embed unknowns here -- they belong in STEP 6.
> Do not include scope exclusions here -- scope was resolved in PRE-FLIGHT GATE.

First: look back at PRE-FLIGHT GATE -- the preliminary hypothesis committed there was [tier] at [N-M
sprints]. State whether the analysis confirms, revises, or partially revises the commitment made in
PRE-FLIGHT GATE using a structured commitment-chain trace. All three labeled lines must appear on separate
lines.

Commitment chain:
Gate commitment: [tier committed in PRE-FLIGHT GATE] / [sprint range committed in PRE-FLIGHT GATE]
Analysis: [key evidence from STEPs 1-6 bearing on the commitment -- name at least two signal dimensions]
Verdict: [use exactly one of the following forms -- the phrase "committed in PRE-FLIGHT GATE" is required]
  -- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N-M sprints]) is confirmed:
     [cross-signal observation combining at least two dimensions]."
  -- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N-M sprints]) is revised:
     [dimension] moved from [prior value] to [current value] because [reason]."
  -- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N-M sprints]) is partially revised:
     [what held]; [what changed] because [reason]."

Writing "my earlier estimate was confirmed" fails C-22. A prose paragraph containing all three chain steps
fails C-24.

After the verdict, add the cross-signal directional observation: combine at least two dimensions (complexity,
timeline, confidence, inertia cost) to produce a recommendation. The recommendation must require both
dimensions to state.

**STRUCTURAL AMEND RE-EVALUATION DIRECTIVE**: This synthesis section carries a written re-evaluation
requirement that applies on every invocation, independent of whether an AMEND directive is present. When
AMEND is absent: confirm no active amendment and proceed. When AMEND is present and the amended dimension
appears in the cross-signal conclusion or verdict above: re-evaluate that conclusion before closing this
section -- update it or explicitly reaffirm that it still holds. This requirement is a structural property
of this section's template, not a conditional check. Leaving this conclusion unchanged after amending a
dimension cited here is a structural failure of this section's integrity.

---

**SIGNAL BOUNDARY CHECK**

Before writing the artifact, scan and remove:
- [ ] Task breakdowns ("Step 1: implement X")
- [ ] Sprint assignments ("Sprint 2: auth integration")
- [ ] Owner names ("Alice owns the backend work")
- [ ] Milestone dates ("Targeting March delivery")

---

**SELF-CHECK -- ALL 31 CRITERIA (C-01 through C-31)**

Essential criteria:
- [ ] C-01: Complexity tier uses exactly LOW / MEDIUM / HIGH / XL. Verify tier field contains exactly one of
  these four values.
- [ ] C-02: Timeline is a sprint range with two bounds (N-M sprints). Verify it is not a point estimate or
  calendar date.
- [ ] C-03: Surface area table includes a Total row with a specific count. Verify the total row is present
  with a number, not a qualitative summary.
- [ ] C-04: INERTIA CHECK names the workaround and carries a cost direction using exactly cheaper /
  comparable / more expensive. Verify the cost direction is a labeled field, not embedded in prose.
- [ ] C-05: Confidence level is present with a basis citing specific supporting evidence. Verify the basis
  names something concrete, not a category label.

Recommended criteria:
- [ ] C-06: Team signal names at least one specialist role or discipline, not headcount only. Verify at least
  one role type (engineer discipline, PM, design, etc.) is named.
- [ ] C-07: Complexity tier accompanied by at least one sentence naming the primary driver. Verify a driver
  sentence appears inline with or following the tier label.
- [ ] C-08: If AMEND is present, at least one substantive output change traces to the amendment; default pass
  if absent. Verify any AMEND-invoked section shows a changed value, not just an acknowledgment.

Aspirational -- depth/behavior (pass conditions only):
- [ ] C-09: At least one explicit exclusion or out-of-scope boundary named in PRE-FLIGHT GATE.
- [ ] C-10: Break-even signal present in PRE-FLIGHT GATE, or "Cannot assess -- [reason]" stated.
- [ ] C-11: Each named specialization includes an implementation ownership area.
- [ ] C-12: At least one specific unknown named that would move confidence, or "No open unknowns" stated.
- [ ] C-13: Synthesis cross-references two or more dimensions to produce a directional conclusion not
  derivable from any single field alone.
- [ ] C-14: Open unknowns in STEP 6 with typed fields; STEP 5 explicitly closed against unknowns.
- [ ] C-15: Preliminary hypothesis inside PRE-FLIGHT GATE; synthesis confirms or revises it naming committed
  values.
- [ ] C-16: If AMEND present and amended dimension in synthesis, synthesis updated or reaffirmed; default
  pass otherwise.
- [ ] C-17: At least one aspirational section contains a sentence naming the specific anti-pattern.

Aspirational -- structural/behavior (with disqualifying forms):
- [ ] C-18: PRE-FLIGHT GATE before all STEPs; contains scope boundary, break-even, and hypothesis fields;
  includes stop instruction.
  Disqualifying form: scope boundary field inside STEP 3 fails C-18 -- section reminder, not gate field.

- [ ] C-19: Adjacent sections to OPEN UNKNOWNS and to scope exclusion canonical home carry prohibitions.
  Disqualifying form: CONFIDENCE section listing unknowns without a prohibition fails C-19.

- [ ] C-20: Every plausible recipient for scope exclusions (STEP 1, 2, 3, 7) and unknowns (STEP 3, 5, 7)
  carries an explicit prohibition.
  Disqualifying form: STEP 2/3 guarded but STEP 1/7 unguarded fails C-20.

- [ ] C-21: Hypothesis is a field inside PRE-FLIGHT GATE; synthesis names PRE-FLIGHT GATE and confirms
  or revises it.
  Disqualifying form: standalone "PRELIMINARY ESTIMATE" section after the gate but before STEP 1 fails
  C-21 -- passing C-18 and C-15 independently does not satisfy C-21.

- [ ] C-22: Synthesis names PRE-FLIGHT GATE at both anchor instruction and verdict close.
  Disqualifying form: "My earlier estimate was confirmed" fails C-22 -- "PRE-FLIGHT GATE" must appear by
  name at both points.

- [ ] C-23: At least one prohibition guard names the canonical home by label.
  Disqualifying form: "Do not include scope exclusions here" fails C-23 -- must name where scope belongs.

- [ ] C-24: Synthesis Commitment chain has three separately labeled lines: Gate commitment: / Analysis: /
  Verdict:.
  Disqualifying form: all three steps in one sentence fails C-24.

- [ ] C-25: PRE-FLIGHT GATE enforcement contract names sections for scope exclusions and section for
  hypothesis.
  Disqualifying form: "All three fields are preconditions for STEP 1-7" fails C-25.

- [ ] C-26: Synthesis STRUCTURAL AMEND RE-EVALUATION DIRECTIVE states requirement applies on every
  invocation independent of AMEND, frames non-compliance as structural failure.
  Disqualifying form: "If AMEND is present in this invocation...it fails C-16" fails C-26.

- [ ] C-27: STEP 6 and STEP 7 both carry dedicated labeled FAILURE MODE blocks.
  Disqualifying form: > **Anti-pattern**: inline blockquote fails C-27 -- not a dedicated labeled block.

- [ ] C-28: Structured self-check covers all aspirational criteria (C-09-C-31) with pass/fail per criterion.
  Disqualifying form: section-level FAILURE MODE blocks do not satisfy C-28.

- [ ] C-29: Structural criteria (C-18-C-27) self-check items include exact disqualifying forms.
  Disqualifying form: "C-25: PRE-FLIGHT GATE names enforcement sections" fails C-29 -- no disqualifying
  form named.

- [ ] C-30: Depth/behavior criteria (C-09-C-17) self-check items include exact disqualifying forms.
  Depth/behavior items above contain pass conditions only -- exact disqualifying forms are absent.
  C-30 FAILS in this variation -- intended single-axis design: C-31 is the only new criterion targeted.

- [ ] C-31: Self-check includes coverage of all essential (C-01-C-05) and recommended (C-06-C-08) criteria.
  Essential (C-01-C-05) and recommended (C-06-C-08) are present above -- PASS.

Fix any violation before writing.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-03 -- Minimal combination (C-30 + C-31)

**Variation axes**: Both C-30 and C-31 together, minimal additional structure beyond adding disqualifying
forms to C-09-C-17 and extending scope to C-01-C-08. No format changes relative to V-01/V-02.

**Hypothesis**: C-30 and C-31 are both closed by combining the two single-axis additions. No further
integration is needed to reach 23/23. Expected pass: all 23 aspirational criteria (C-09-C-31). Score: 100.

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal files). Do not prompt unless
context is absent.

Produce a sizing signal. This is NOT a project plan. Signal boundary: no task breakdowns, sprint assignments,
owner names, or milestone dates. Remove any violations before writing the artifact.

Follow every step in order. Every labeled row and field is required.

---

**PRE-FLIGHT GATE -- complete before any analysis begins**

All three fields below are preconditions for all analysis sections, including STEP 1 through STEP 7. Resolve
them from repo context now. Do not proceed until all three fields contain specific responses -- "TBD" or blank
fails any field.

Out-of-scope boundary:
[Name at least one sub-system, phase, integration, or behavior explicitly NOT covered by this sizing. If
genuinely full implementation scope: "No exclusions -- full scope assumed." Do not say "TBD."]

Break-even signal:
[At what usage level, team count, or time horizon does building this feature recover its cost vs. the current
workaround? State a rough signal or explicitly: "Cannot assess -- [specific reason]." Absence fails C-10
before analysis begins.]

Preliminary hypothesis:
Tier: [LOW / MEDIUM / HIGH / XL -- commit to one tier now]
Timeline: [N-M sprints -- commit now]
Reasoning: [one sentence -- what signals the scope before detailed analysis?]

STOP: All three fields must contain specific responses. Do not proceed to STEP 1 or any STEP below until this
gate is fully resolved.

Enforcement contract for this gate's commitments:
- Scope exclusions: enforced in STEP 1 INERTIA CHECK (prohibits scope qualifications), STEP 2 SURFACE AREA
  (prohibits scope exclusions), STEP 3 COMPLEXITY (prohibits scope exclusions), and STEP 7 SYNTHESIS
  (prohibits scope exclusions) -- each section is explicitly closed against scope content.
- Hypothesis: confirmed or revised in STEP 7 SYNTHESIS, which names this gate by label at both the anchor
  instruction ("look back at PRE-FLIGHT GATE") and the verdict close ("The preliminary hypothesis committed
  in PRE-FLIGHT GATE...").

---

**STEP 1: INERTIA CHECK**

> WRONG: "Teams use a workaround currently." -- No cost direction. Fails.
> CORRECT: "Manual CSV re-import per team -- building is more expensive upfront but cheaper to maintain;
> workaround costs ~2h/sprint/team and scales linearly with team count."

Workaround: [name the specific alternative in use]
Maintenance cost: [estimate the ongoing cost]
Cost direction: [cheaper / comparable / more expensive -- one word, required]

Do not add scope boundary notes or exclusion qualifications here -- scope was resolved in PRE-FLIGHT GATE,
not in analysis steps.

---

**STEP 2: SURFACE AREA**

Do not include scope exclusions here -- scope was resolved in PRE-FLIGHT GATE, not in analysis steps.

| # | Integration Point | Type | Description |
|---|-------------------|------|-------------|
| 1 | [name] | [API / event / data model / config / cross-service] | [brief] |
| ... | | | |
| **Total** | | | **N integration points** |

Total row required.

---

**STEP 3: COMPLEXITY TIER AND DRIVER**

Tier: [LOW / MEDIUM / HIGH / XL -- exactly this vocabulary]
Primary driver: [one or two factors most responsible]

Tier sensitivity -- use this exact template:

    Tier rises to [LEVEL] if [single named condition].
    Tier falls to [LEVEL] if [single named condition].

Do not include scope exclusions here -- scope was resolved in PRE-FLIGHT GATE, not in analysis steps.
Do not embed unknowns here -- unknowns belong in STEP 6 OPEN UNKNOWNS, not in analysis sections.

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
  Failing: "3 engineers" -- no disciplines, no ownership.
  Passing: "1 backend engineer (owns event schema + API layer), 1 infra engineer (owns deployment pipeline),
           0.5 PM (owns stakeholder coordination)"

Timeline signal: [sprint range -- "N-M sprints"]
  Failing: "Q3 2026" (calendar date), "4 sprints" (point estimate, not a range)

---

**STEP 5: CONFIDENCE**

Confidence: [HIGH / MEDIUM / LOW]
Basis: [what IS known -- specific evidence, prior work, or verified reasoning]

Do not list unknowns here -- unknowns belong in STEP 6 OPEN UNKNOWNS, not in the confidence basis. This
section is explicitly closed against unknowns.

---

**STEP 6: OPEN UNKNOWNS**

> **FAILURE MODE FOR THIS SECTION**: "Dependencies may exist" is a placeholder, not an unknown. An unknown
> must name a specific dependency, decision, or contract that has not been verified. A generic hedge fails
> exactly as silently as an absent section. Do not include scope exclusions here -- scope was resolved in
> PRE-FLIGHT GATE. Do not include break-even observations here -- break-even was resolved in PRE-FLIGHT GATE.

List open unknowns with typed fields. If none remain, state: "No open unknowns."

For each open unknown:

Unknown: [the specific unverified item -- concrete, testable]
Impact: [which dimension this most affects: complexity / timeline / team / confidence]
Movement: [the specific investigation or result that closes this unknown]

---

**STEP 7: SYNTHESIS**

> **FAILURE MODE FOR THIS SECTION**: Restating sections in sequence -- "Complexity is HIGH. Timeline is
> 4-6 sprints. Confidence is MEDIUM." -- is juxtaposition, not synthesis. This section fails if the
> conclusion is derivable from any single field alone. Do not embed unknowns here -- they belong in STEP 6.
> Do not include scope exclusions here -- scope was resolved in PRE-FLIGHT GATE.

First: look back at PRE-FLIGHT GATE -- the preliminary hypothesis committed there was [tier] at [N-M
sprints]. State whether the analysis confirms, revises, or partially revises the commitment made in
PRE-FLIGHT GATE using a structured commitment-chain trace. All three labeled lines must appear on separate
lines.

Commitment chain:
Gate commitment: [tier committed in PRE-FLIGHT GATE] / [sprint range committed in PRE-FLIGHT GATE]
Analysis: [key evidence from STEPs 1-6 bearing on the commitment -- name at least two signal dimensions]
Verdict: [use exactly one of the following forms -- the phrase "committed in PRE-FLIGHT GATE" is required]
  -- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N-M sprints]) is confirmed:
     [cross-signal observation combining at least two dimensions]."
  -- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N-M sprints]) is revised:
     [dimension] moved from [prior value] to [current value] because [reason]."
  -- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N-M sprints]) is partially revised:
     [what held]; [what changed] because [reason]."

Writing "my earlier estimate was confirmed" fails C-22. A prose paragraph containing all three chain steps
fails C-24.

After the verdict, add the cross-signal directional observation: combine at least two dimensions to produce
a recommendation that requires both dimensions to state.

**STRUCTURAL AMEND RE-EVALUATION DIRECTIVE**: This synthesis section carries a written re-evaluation
requirement that applies on every invocation, independent of whether an AMEND directive is present. When
AMEND is absent: confirm no active amendment and proceed. When AMEND is present and the amended dimension
appears in the cross-signal conclusion or verdict above: re-evaluate that conclusion before closing this
section -- update it or explicitly reaffirm that it still holds. This requirement is a structural property
of this section's template, not a conditional check. Leaving this conclusion unchanged after amending a
dimension cited here is a structural failure of this section's integrity.

---

**SIGNAL BOUNDARY CHECK**

Before writing the artifact, scan and remove:
- [ ] Task breakdowns ("Step 1: implement X")
- [ ] Sprint assignments ("Sprint 2: auth integration")
- [ ] Owner names ("Alice owns the backend work")
- [ ] Milestone dates ("Targeting March delivery")

---

**SELF-CHECK -- ALL 31 CRITERIA (C-01 through C-31)**

Essential (C-01-C-05):
- [ ] C-01: Complexity tier is exactly LOW / MEDIUM / HIGH / XL.
- [ ] C-02: Timeline is a sprint range (N-M), not a point estimate or calendar date.
- [ ] C-03: Surface area table has a Total row with a specific count.
- [ ] C-04: Inertia workaround named; cost direction is exactly cheaper / comparable / more expensive.
- [ ] C-05: Confidence present with a basis naming specific supporting evidence.

Recommended (C-06-C-08):
- [ ] C-06: Team signal names at least one specialist discipline (not headcount only).
- [ ] C-07: Primary driver accompanies the complexity tier.
- [ ] C-08: If AMEND present, at least one substantive output change traces to it; absent -- pass by default.

Aspirational -- depth/behavior (C-09-C-17, with disqualifying forms):
- [ ] C-09: At least one explicit exclusion named in PRE-FLIGHT GATE.
  Disqualifying form: "Standard integrations excluded" fails -- names a category, not a specific sub-system.

- [ ] C-10: Break-even signal in PRE-FLIGHT GATE, or "Cannot assess -- [reason]" stated.
  Disqualifying form: "Break-even depends on adoption" fails -- no threshold or explicit inability stated.

- [ ] C-11: Each named specialization includes an implementation ownership area.
  Disqualifying form: "1 backend engineer, 1 infra engineer" fails -- ownership scope absent.

- [ ] C-12: At least one specific unknown named that would move confidence, or "No open unknowns" stated.
  Disqualifying form: "External dependencies may affect timeline" fails -- risk category, not specific item.

- [ ] C-13: Synthesis cross-references two or more dimensions for a conclusion not derivable from any
  single field.
  Disqualifying form: "Complexity is HIGH and timeline is 4-6 sprints, so this requires careful planning"
  fails -- "careful planning" derivable from complexity alone.

- [ ] C-14: Open unknowns in STEP 6 with typed fields; STEP 5 closed against unknowns.
  Disqualifying form: CONFIDENCE basis reading "Timeline unclear pending auth contract" fails -- STEP 5
  carries an unknown that belongs in STEP 6.

- [ ] C-15: Hypothesis inside PRE-FLIGHT GATE; synthesis names committed values when confirming/revising.
  Disqualifying form: "My earlier estimate held" fails -- committed tier and sprint range not cited.

- [ ] C-16: If AMEND + amended dimension in synthesis -- synthesis updated or reaffirmed; default pass.
  Disqualifying form: AMEND changes confidence; confidence in conclusion; conclusion unchanged without
  reaffirmation fails C-16.

- [ ] C-17: At least one aspirational section names the specific anti-pattern being avoided.
  Disqualifying form: "This section may produce weak output" fails -- no specific anti-pattern form named.

Aspirational -- structural/behavior (C-18-C-31, with disqualifying forms):
- [ ] C-18: PRE-FLIGHT GATE before all STEPs; scope boundary, break-even, hypothesis fields; stop
  instruction present.
  Disqualifying form: scope boundary inside STEP 3 fails C-18 -- section reminder, not gate field.

- [ ] C-19: Adjacent sections to OPEN UNKNOWNS and scope exclusion canonical home carry prohibitions.
  Disqualifying form: CONFIDENCE listing unknowns without prohibition fails C-19.

- [ ] C-20: All plausible recipient sections for scope exclusions (STEP 1, 2, 3, 7) and unknowns
  (STEP 3, 5, 7) carry explicit prohibitions.
  Disqualifying form: STEP 2/3 guarded, STEP 1/7 unguarded fails C-20.

- [ ] C-21: Hypothesis is a field inside PRE-FLIGHT GATE; synthesis names PRE-FLIGHT GATE and confirms
  or revises it.
  Disqualifying form: standalone hypothesis section after gate but before STEP 1 fails C-21.

- [ ] C-22: Synthesis names PRE-FLIGHT GATE at both anchor instruction and verdict close.
  Disqualifying form: "My earlier estimate was confirmed" fails C-22.

- [ ] C-23: At least one prohibition guard names the canonical home by label.
  Disqualifying form: "Do not include scope exclusions here" fails -- no canonical home named.

- [ ] C-24: Synthesis Commitment chain has three separately labeled lines: Gate commitment: / Analysis: /
  Verdict:.
  Disqualifying form: all three steps in one sentence fails C-24.

- [ ] C-25: PRE-FLIGHT GATE enforcement contract names sections for scope AND section for hypothesis.
  Disqualifying form: "All three fields are preconditions for STEP 1-7" fails C-25.

- [ ] C-26: Synthesis STRUCTURAL AMEND RE-EVALUATION DIRECTIVE states requirement applies every invocation
  independent of AMEND; frames non-compliance as structural failure.
  Disqualifying form: "If AMEND in this invocation...it fails C-16" fails C-26.

- [ ] C-27: STEP 6 and STEP 7 both carry dedicated labeled FAILURE MODE blocks.
  Disqualifying form: inline > **Anti-pattern**: blockquote fails C-27.

- [ ] C-28: Structured self-check covers all aspirational criteria (C-09-C-31) with pass/fail per criterion.
  Disqualifying form: section-level FAILURE MODE blocks alone do not satisfy C-28.

- [ ] C-29: Structural criteria (C-18-C-27) self-check items include exact disqualifying forms.
  Disqualifying form: pass-condition-only item for any structural criterion fails C-29.

- [ ] C-30: Depth/behavior criteria (C-09-C-17) self-check items include exact disqualifying forms.
  Disqualifying form: pass-condition-only item for any depth/behavior criterion fails C-30.

- [ ] C-31: Self-check includes coverage of all essential (C-01-C-05) and recommended (C-06-C-08) criteria.
  Essential and recommended are present above -- PASS.

Fix any violation before writing.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-04 -- Fuller integration (C-30 + C-31, table format for essential/recommended)

**Variation axes**: C-30 + C-31 from V-03 plus a structural format change for the essential/recommended
self-check entries: a table showing ID / Criterion / Disqualifying form for C-01-C-08, making the
essential/recommended entries as structurally scannable as the aspirational ones. Phrasing register is more
imperative throughout the self-check.

**Hypothesis**: Presenting C-01-C-08 in a table format increases scan reliability vs. a flat checklist for
essential/recommended entries. A reader (or model) checking for C-31 compliance can verify the table is
present at a glance; a flat list can be visually merged with the aspirational section. Structural format
difference, not content difference. Expected pass: 23/23. Score: 100.

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal files). Do not prompt unless
context is absent.

Produce a sizing signal. This is NOT a project plan. Signal boundary: no task breakdowns, sprint assignments,
owner names, or milestone dates. Remove any violations before writing the artifact.

Follow every step in order. Every labeled row and field is required.

---

**PRE-FLIGHT GATE -- complete before any analysis begins**

All three fields below are preconditions for all analysis sections, including STEP 1 through STEP 7. Resolve
them from repo context now. Do not proceed until all three fields contain specific responses -- "TBD" or blank
fails any field.

Out-of-scope boundary:
[Name at least one sub-system, phase, integration, or behavior explicitly NOT covered by this sizing. If
genuinely full implementation scope: "No exclusions -- full scope assumed." Do not say "TBD."]

Break-even signal:
[At what usage level, team count, or time horizon does building this feature recover its cost vs. the current
workaround? State a rough signal or explicitly: "Cannot assess -- [specific reason]." Absence fails C-10
before analysis begins.]

Preliminary hypothesis:
Tier: [LOW / MEDIUM / HIGH / XL -- commit to one tier now]
Timeline: [N-M sprints -- commit now]
Reasoning: [one sentence -- what signals the scope before detailed analysis?]

STOP: All three fields must contain specific responses. Do not proceed to STEP 1 or any STEP below until this
gate is fully resolved.

Enforcement contract for this gate's commitments:
- Scope exclusions: enforced in STEP 1 INERTIA CHECK (prohibits scope qualifications), STEP 2 SURFACE AREA
  (prohibits scope exclusions), STEP 3 COMPLEXITY (prohibits scope exclusions), and STEP 7 SYNTHESIS
  (prohibits scope exclusions) -- each section is explicitly closed against scope content.
- Hypothesis: confirmed or revised in STEP 7 SYNTHESIS, which names this gate by label at both the anchor
  instruction ("look back at PRE-FLIGHT GATE") and the verdict close ("The preliminary hypothesis committed
  in PRE-FLIGHT GATE...").

---

**STEP 1: INERTIA CHECK**

> WRONG: "Teams use a workaround currently." -- No cost direction. Fails.
> CORRECT: "Manual CSV re-import per team -- building is more expensive upfront but cheaper to maintain;
> workaround costs ~2h/sprint/team and scales linearly with team count."

Workaround: [name the specific alternative in use]
Maintenance cost: [estimate the ongoing cost]
Cost direction: [cheaper / comparable / more expensive -- one word, required]

Do not add scope boundary notes or exclusion qualifications here -- scope was resolved in PRE-FLIGHT GATE,
not in analysis steps.

---

**STEP 2: SURFACE AREA**

Do not include scope exclusions here -- scope was resolved in PRE-FLIGHT GATE, not in analysis steps.

| # | Integration Point | Type | Description |
|---|-------------------|------|-------------|
| 1 | [name] | [API / event / data model / config / cross-service] | [brief] |
| ... | | | |
| **Total** | | | **N integration points** |

Total row required.

---

**STEP 3: COMPLEXITY TIER AND DRIVER**

Tier: [LOW / MEDIUM / HIGH / XL -- exactly this vocabulary]
Primary driver: [one or two factors most responsible]

Tier sensitivity -- use this exact template:

    Tier rises to [LEVEL] if [single named condition].
    Tier falls to [LEVEL] if [single named condition].

Do not include scope exclusions here -- scope was resolved in PRE-FLIGHT GATE, not in analysis steps.
Do not embed unknowns here -- unknowns belong in STEP 6 OPEN UNKNOWNS, not in analysis sections.

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
  Failing: "3 engineers" -- no disciplines, no ownership.
  Passing: "1 backend engineer (owns event schema + API layer), 1 infra engineer (owns deployment pipeline),
           0.5 PM (owns stakeholder coordination)"

Timeline signal: [sprint range -- "N-M sprints"]
  Failing: "Q3 2026" (calendar date), "4 sprints" (point estimate, not a range)

---

**STEP 5: CONFIDENCE**

Confidence: [HIGH / MEDIUM / LOW]
Basis: [what IS known -- specific evidence, prior work, or verified reasoning]

Do not list unknowns here -- unknowns belong in STEP 6 OPEN UNKNOWNS, not in the confidence basis. This
section is explicitly closed against unknowns.

---

**STEP 6: OPEN UNKNOWNS**

> **FAILURE MODE FOR THIS SECTION**: "Dependencies may exist" is a placeholder, not an unknown. An unknown
> must name a specific dependency, decision, or contract that has not been verified. A generic hedge fails
> exactly as silently as an absent section. Do not include scope exclusions here -- scope was resolved in
> PRE-FLIGHT GATE. Do not include break-even observations here -- break-even was resolved in PRE-FLIGHT GATE.

List open unknowns with typed fields. If none remain, state: "No open unknowns."

For each open unknown:

Unknown: [the specific unverified item -- concrete, testable]
Impact: [which dimension this most affects: complexity / timeline / team / confidence]
Movement: [the specific investigation or result that closes this unknown]

---

**STEP 7: SYNTHESIS**

> **FAILURE MODE FOR THIS SECTION**: Restating sections in sequence -- "Complexity is HIGH. Timeline is
> 4-6 sprints. Confidence is MEDIUM." -- is juxtaposition, not synthesis. This section fails if the
> conclusion is derivable from any single field alone. Do not embed unknowns here -- they belong in STEP 6.
> Do not include scope exclusions here -- scope was resolved in PRE-FLIGHT GATE.

First: look back at PRE-FLIGHT GATE -- the preliminary hypothesis committed there was [tier] at [N-M
sprints]. State whether the analysis confirms, revises, or partially revises the commitment made in
PRE-FLIGHT GATE using a structured commitment-chain trace. All three labeled lines must appear on separate
lines.

Commitment chain:
Gate commitment: [tier committed in PRE-FLIGHT GATE] / [sprint range committed in PRE-FLIGHT GATE]
Analysis: [key evidence from STEPs 1-6 bearing on the commitment -- name at least two signal dimensions]
Verdict: [use exactly one of the following forms -- the phrase "committed in PRE-FLIGHT GATE" is required]
  -- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N-M sprints]) is confirmed:
     [cross-signal observation combining at least two dimensions]."
  -- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N-M sprints]) is revised:
     [dimension] moved from [prior value] to [current value] because [reason]."
  -- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N-M sprints]) is partially revised:
     [what held]; [what changed] because [reason]."

Writing "my earlier estimate was confirmed" fails C-22. A prose paragraph containing all three chain steps
fails C-24.

After the verdict, add the cross-signal directional observation combining at least two dimensions to produce
a recommendation that requires both dimensions to state.

**STRUCTURAL AMEND RE-EVALUATION DIRECTIVE**: This synthesis section carries a written re-evaluation
requirement that applies on every invocation, independent of whether an AMEND directive is present. When
AMEND is absent: confirm no active amendment and proceed. When AMEND is present and the amended dimension
appears in the cross-signal conclusion or verdict above: re-evaluate that conclusion before closing this
section -- update it or explicitly reaffirm that it still holds. This requirement is a structural property
of this section's template, not a conditional check. Leaving this conclusion unchanged after amending a
dimension cited here is a structural failure of this section's integrity.

---

**SIGNAL BOUNDARY CHECK**

Before writing the artifact, scan and remove:
- [ ] Task breakdowns ("Step 1: implement X")
- [ ] Sprint assignments ("Sprint 2: auth integration")
- [ ] Owner names ("Alice owns the backend work")
- [ ] Milestone dates ("Targeting March delivery")

---

**SELF-CHECK -- ALL 31 CRITERIA**

**Essential and recommended (C-01-C-08) -- verify each before proceeding:**

| ID | What to verify | Failing form |
|----|----------------|--------------|
| C-01 | Tier is exactly LOW / MEDIUM / HIGH / XL | "medium-high" or any intermediate form |
| C-02 | Timeline is N-M sprints (two bounds) | "4 sprints" or "Q3 2026" |
| C-03 | Surface area Total row has a specific count | "Several integration points" as total row |
| C-04 | Workaround named; cost direction is cheaper / comparable / more expensive | Workaround present but no labeled cost direction field |
| C-05 | Confidence present with specific evidence basis | "Reasonably well-understood area" -- category, not evidence |
| C-06 | Team signal names at least one discipline | "2 engineers" -- headcount only |
| C-07 | Primary driver sentence accompanies tier | "Tier: HIGH" with no driver sentence |
| C-08 | If AMEND present, substantive change traces to it; absent -- pass | Acknowledgment phrase added but no changed value |

**Aspirational -- depth/behavior (C-09-C-17):**

- [ ] C-09: At least one explicit exclusion named in PRE-FLIGHT GATE.
  Disqualifying form: "Standard integrations excluded" -- category label, not a named sub-system.

- [ ] C-10: Break-even signal in PRE-FLIGHT GATE, or explicit "Cannot assess -- [reason]."
  Disqualifying form: "Break-even depends on adoption" -- no threshold and no explicit inability.

- [ ] C-11: Each named specialization includes an implementation ownership area.
  Disqualifying form: "1 backend engineer, 1 infra engineer" -- disciplines without ownership scope.

- [ ] C-12: At least one specific unknown that would move confidence named, or "No open unknowns."
  Disqualifying form: "External dependencies may affect timeline" -- risk category, not specific item.

- [ ] C-13: Synthesis cross-references two or more dimensions; conclusion not derivable from any single
  field.
  Disqualifying form: "HIGH complexity and 4-6 sprint timeline means careful planning needed" -- conclusion
  derivable from complexity alone.

- [ ] C-14: Open unknowns in STEP 6 with typed fields; STEP 5 closed against unknowns.
  Disqualifying form: CONFIDENCE basis reading "Timeline unclear pending auth contract" -- STEP 5 leaky.

- [ ] C-15: Hypothesis inside PRE-FLIGHT GATE; synthesis names committed values in confirm/revise.
  Disqualifying form: "My earlier estimate held" -- committed tier and sprint range not cited.

- [ ] C-16: If AMEND + amended dimension in synthesis -- synthesis updated or reaffirmed; default pass.
  Disqualifying form: confidence amended, confidence in conclusion, conclusion unchanged and unreaffirmed.

- [ ] C-17: At least one aspirational section names the specific anti-pattern.
  Disqualifying form: "This section may produce weak output" -- quality risk named, anti-pattern form not.

**Aspirational -- structural/behavior (C-18-C-31):**

- [ ] C-18: PRE-FLIGHT GATE before all STEPs; all three field types present; stop instruction included.
  Disqualifying form: scope boundary field inside STEP 3 -- section reminder, not gate precondition.

- [ ] C-19: Adjacent sections to unknowns canonical home and scope canonical home carry prohibitions.
  Disqualifying form: CONFIDENCE lists unknowns without prohibition.

- [ ] C-20: All plausible recipients for scope content (STEP 1, 2, 3, 7) and unknowns (STEP 3, 5, 7)
  carry prohibitions.
  Disqualifying form: STEP 2/3 guarded, STEP 1/7 unguarded -- partial closure fails C-20.

- [ ] C-21: Hypothesis inside PRE-FLIGHT GATE gate block; synthesis names gate and confirms/revises.
  Disqualifying form: hypothesis in standalone section after gate but before STEP 1 fails C-21.

- [ ] C-22: Synthesis names PRE-FLIGHT GATE at both anchor and verdict close.
  Disqualifying form: "My earlier estimate was confirmed" -- gate not named.

- [ ] C-23: At least one prohibition guard names the canonical home by label.
  Disqualifying form: "Do not include scope exclusions here" -- no canonical home named.

- [ ] C-24: Commitment chain on three labeled lines: Gate commitment: / Analysis: / Verdict:.
  Disqualifying form: all three chain steps in one sentence.

- [ ] C-25: Enforcement contract names sections for scope exclusions and section for hypothesis.
  Disqualifying form: "All three fields are preconditions for STEP 1-7" -- no scope/hypothesis split.

- [ ] C-26: Synthesis STRUCTURAL AMEND RE-EVALUATION DIRECTIVE: applies every invocation, independent of
  AMEND; non-compliance is structural failure.
  Disqualifying form: "If AMEND present in this invocation...it fails C-16" -- conditional + criterion ref.

- [ ] C-27: STEP 6 and STEP 7 carry dedicated labeled FAILURE MODE blocks.
  Disqualifying form: > **Anti-pattern**: inline blockquote embedded in instruction prose.

- [ ] C-28: Structured self-check covers all aspirational criteria (C-09-C-31) with pass/fail per criterion.
  Disqualifying form: section-level FAILURE MODE blocks alone without a collective audit block.

- [ ] C-29: Structural criteria (C-18-C-27) items include exact disqualifying forms.
  Disqualifying form: pass-condition-only item for any structural criterion.

- [ ] C-30: Depth/behavior criteria (C-09-C-17) items include exact disqualifying forms.
  Disqualifying form: pass-condition-only item for any depth/behavior criterion.

- [ ] C-31: Self-check includes coverage of all essential (C-01-C-05) and recommended (C-06-C-08).
  Essential/recommended table is present above -- PASS. Disqualifying form: aspirational-only self-check
  with no essential/recommended entries.

Fix any violation before writing.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## V-05 -- Full integration (all 31 criteria with complete disqualifying forms)

**Variation axes**: All V-04 mechanisms plus disqualifying forms added to essential (C-01-C-05) and
recommended (C-06-C-08) entries in the self-check table. No rubric criterion requires this -- the rubric
only requires pass/fail + evidence for C-01-C-08. V-05 extends beyond what's required for maximum
reliability: a model running this self-check can identify a violation in any of the 31 criteria without
inferring what "failing" looks like from context alone. The disqualifying-form treatment that C-29 and C-30
established for aspirational criteria is applied uniformly to all 31.

**Hypothesis**: Adding disqualifying forms to C-01-C-08 does not change the rubric score (C-31 passes as
long as C-01-C-08 are present with pass/fail; disqualifying forms are surplus). But the same structural
reliability argument that justified C-29 (uniform disqualifying forms for structural criteria) and C-30
(uniform disqualifying forms for depth/behavior criteria) applies to essential/recommended: a self-check
item that only states the pass condition requires the model to infer the failing form, introducing a
detection gap. Eliminating the gap uniformly across all 31 criteria is the highest-reliability form.
Expected pass: 23/23. Score: 100.

---

```
Auto-detect topic from repo context (CLAUDE.md, plugin-plan.md, recent signal files). Do not prompt unless
context is absent.

Produce a sizing signal. This is NOT a project plan. Signal boundary: no task breakdowns, sprint assignments,
owner names, or milestone dates. Remove any violations before writing the artifact.

Follow every step in order. Every labeled row and field is required.

---

**PRE-FLIGHT GATE -- complete before any analysis begins**

All three fields below are preconditions for all analysis sections, including STEP 1 through STEP 7. Resolve
them from repo context now. Do not proceed until all three fields contain specific responses -- "TBD" or blank
fails any field.

Out-of-scope boundary:
[Name at least one sub-system, phase, integration, or behavior explicitly NOT covered by this sizing. If
genuinely full implementation scope: "No exclusions -- full scope assumed." Do not say "TBD."]

Break-even signal:
[At what usage level, team count, or time horizon does building this feature recover its cost vs. the current
workaround? State a rough signal or explicitly: "Cannot assess -- [specific reason]." Absence fails C-10
before analysis begins.]

Preliminary hypothesis:
Tier: [LOW / MEDIUM / HIGH / XL -- commit to one tier now]
Timeline: [N-M sprints -- commit now]
Reasoning: [one sentence -- what signals the scope before detailed analysis?]

STOP: All three fields must contain specific responses. Do not proceed to STEP 1 or any STEP below until this
gate is fully resolved.

Enforcement contract for this gate's commitments:
- Scope exclusions: enforced in STEP 1 INERTIA CHECK (prohibits scope qualifications), STEP 2 SURFACE AREA
  (prohibits scope exclusions), STEP 3 COMPLEXITY (prohibits scope exclusions), and STEP 7 SYNTHESIS
  (prohibits scope exclusions) -- each section is explicitly closed against scope content.
- Hypothesis: confirmed or revised in STEP 7 SYNTHESIS, which names this gate by label at both the anchor
  instruction ("look back at PRE-FLIGHT GATE") and the verdict close ("The preliminary hypothesis committed
  in PRE-FLIGHT GATE...").

---

**STEP 1: INERTIA CHECK**

> WRONG: "Teams use a workaround currently." -- No cost direction. Fails.
> CORRECT: "Manual CSV re-import per team -- building is more expensive upfront but cheaper to maintain;
> workaround costs ~2h/sprint/team and scales linearly with team count."

Workaround: [name the specific alternative in use]
Maintenance cost: [estimate the ongoing cost]
Cost direction: [cheaper / comparable / more expensive -- one word, required]

Do not add scope boundary notes or exclusion qualifications here -- scope was resolved in PRE-FLIGHT GATE,
not in analysis steps.

---

**STEP 2: SURFACE AREA**

Do not include scope exclusions here -- scope was resolved in PRE-FLIGHT GATE, not in analysis steps.

| # | Integration Point | Type | Description |
|---|-------------------|------|-------------|
| 1 | [name] | [API / event / data model / config / cross-service] | [brief] |
| ... | | | |
| **Total** | | | **N integration points** |

Total row required.

---

**STEP 3: COMPLEXITY TIER AND DRIVER**

Tier: [LOW / MEDIUM / HIGH / XL -- exactly this vocabulary]
Primary driver: [one or two factors most responsible]

Tier sensitivity -- use this exact template:

    Tier rises to [LEVEL] if [single named condition].
    Tier falls to [LEVEL] if [single named condition].

Do not include scope exclusions here -- scope was resolved in PRE-FLIGHT GATE, not in analysis steps.
Do not embed unknowns here -- unknowns belong in STEP 6 OPEN UNKNOWNS, not in analysis sections.

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
  Failing: "3 engineers" -- no disciplines, no ownership.
  Passing: "1 backend engineer (owns event schema + API layer), 1 infra engineer (owns deployment pipeline),
           0.5 PM (owns stakeholder coordination)"

Timeline signal: [sprint range -- "N-M sprints"]
  Failing: "Q3 2026" (calendar date), "4 sprints" (point estimate, not a range)

---

**STEP 5: CONFIDENCE**

Confidence: [HIGH / MEDIUM / LOW]
Basis: [what IS known -- specific evidence, prior work, or verified reasoning]

Do not list unknowns here -- unknowns belong in STEP 6 OPEN UNKNOWNS, not in the confidence basis. This
section is explicitly closed against unknowns.

---

**STEP 6: OPEN UNKNOWNS**

> **FAILURE MODE FOR THIS SECTION**: "Dependencies may exist" is a placeholder, not an unknown. An unknown
> must name a specific dependency, decision, or contract that has not been verified. A generic hedge fails
> exactly as silently as an absent section. Do not include scope exclusions here -- scope was resolved in
> PRE-FLIGHT GATE. Do not include break-even observations here -- break-even was resolved in PRE-FLIGHT GATE.

List open unknowns with typed fields. If none remain, state: "No open unknowns."

For each open unknown:

Unknown: [the specific unverified item -- concrete, testable]
Impact: [which dimension this most affects: complexity / timeline / team / confidence]
Movement: [the specific investigation or result that closes this unknown]

---

**STEP 7: SYNTHESIS**

> **FAILURE MODE FOR THIS SECTION**: Restating sections in sequence -- "Complexity is HIGH. Timeline is
> 4-6 sprints. Confidence is MEDIUM." -- is juxtaposition, not synthesis. This section fails if the
> conclusion is derivable from any single field alone. Do not embed unknowns here -- they belong in STEP 6.
> Do not include scope exclusions here -- scope was resolved in PRE-FLIGHT GATE.

First: look back at PRE-FLIGHT GATE -- the preliminary hypothesis committed there was [tier] at [N-M
sprints]. State whether the analysis confirms, revises, or partially revises the commitment made in
PRE-FLIGHT GATE using a structured commitment-chain trace. All three labeled lines must appear on separate
lines.

Commitment chain:
Gate commitment: [tier committed in PRE-FLIGHT GATE] / [sprint range committed in PRE-FLIGHT GATE]
Analysis: [key evidence from STEPs 1-6 bearing on the commitment -- name at least two signal dimensions]
Verdict: [use exactly one of the following forms -- the phrase "committed in PRE-FLIGHT GATE" is required]
  -- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N-M sprints]) is confirmed:
     [cross-signal observation combining at least two dimensions]."
  -- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N-M sprints]) is revised:
     [dimension] moved from [prior value] to [current value] because [reason]."
  -- "The preliminary hypothesis committed in PRE-FLIGHT GATE ([tier], [N-M sprints]) is partially revised:
     [what held]; [what changed] because [reason]."

Writing "my earlier estimate was confirmed" fails C-22. A prose paragraph containing all three chain steps
fails C-24.

After the verdict, add the cross-signal directional observation combining at least two dimensions to produce
a recommendation that requires both dimensions to state.

**STRUCTURAL AMEND RE-EVALUATION DIRECTIVE**: This synthesis section carries a written re-evaluation
requirement that applies on every invocation, independent of whether an AMEND directive is present. When
AMEND is absent: confirm no active amendment and proceed. When AMEND is present and the amended dimension
appears in the cross-signal conclusion or verdict above: re-evaluate that conclusion before closing this
section -- update it or explicitly reaffirm that it still holds. This requirement is a structural property
of this section's template, not a conditional check. Leaving this conclusion unchanged after amending a
dimension cited here is a structural failure of this section's integrity.

---

**SIGNAL BOUNDARY CHECK**

Before writing the artifact, scan and remove:
- [ ] Task breakdowns ("Step 1: implement X")
- [ ] Sprint assignments ("Sprint 2: auth integration")
- [ ] Owner names ("Alice owns the backend work")
- [ ] Milestone dates ("Targeting March delivery")

---

**SELF-CHECK -- ALL 31 CRITERIA**

**Essential (C-01-C-05) -- disqualifying forms included:**

| ID | Pass condition | Disqualifying form |
|----|----------------|-------------------|
| C-01 | Tier is exactly LOW / MEDIUM / HIGH / XL | "medium-high", "HIGH-ish", or any form outside the four-value vocabulary fails even if intent is clear |
| C-02 | Timeline is N-M sprints with two numeric bounds | "4 sprints" (one bound), "Q3 2026" (calendar anchor), "several sprints" (no bounds) |
| C-03 | Surface area table has a Total row with a specific integer count | "Several integration points" or "~5 points" as the Total row -- qualitative or approximate |
| C-04 | Workaround named; cost direction is labeled cheaper / comparable / more expensive | "Teams work around this manually -- it's somewhat expensive" -- workaround described but cost direction not a labeled field |
| C-05 | Confidence present with a basis citing specific evidence (prior work, named contract, verified schema) | "Confidence: MEDIUM -- this is a reasonably well-understood area" -- the basis names a category, not specific evidence |

**Recommended (C-06-C-08) -- disqualifying forms included:**

| ID | Pass condition | Disqualifying form |
|----|----------------|-------------------|
| C-06 | Team signal names at least one specialist role or discipline | "2 engineers" or "small team" -- headcount with no role type named |
| C-07 | At least one sentence names the primary driver alongside the tier label | "Tier: HIGH" followed by no driver sentence -- bare tier label with no named factor |
| C-08 | If AMEND present: at least one substantive output change (different value, expanded section) traces to the amendment; absent -- pass by default | AMEND directs "focus on team complexity"; response adds only "team complexity is relevant here" without expanding the team analysis -- acknowledgment only |

**Aspirational -- depth/behavior (C-09-C-17):**

- [ ] C-09: At least one explicit exclusion named in PRE-FLIGHT GATE.
  Disqualifying form: "Standard integrations excluded" -- names a category, not a specific sub-system or
  integration point; the exclusion must identify what is out of scope, not imply a class.

- [ ] C-10: Break-even signal in PRE-FLIGHT GATE, or explicit "Cannot assess -- [reason]."
  Disqualifying form: "Break-even depends on adoption" -- no threshold stated and no explicit inability
  with a named reason; rough signals like "~3 teams / week" are sufficient.

- [ ] C-11: Each named specialization includes an implementation ownership area.
  Disqualifying form: "1 backend engineer, 1 infra engineer" -- disciplines named, ownership absent; a
  separate ownership sentence in a different field does not satisfy C-11 per role.

- [ ] C-12: At least one specific unknown that would move confidence named, or "No open unknowns."
  Disqualifying form: "External dependencies may affect timeline" -- risk category without a specific
  dependency, contract, or decision whose resolution would change the confidence level.

- [ ] C-13: Synthesis cross-references two or more dimensions; conclusion not derivable from any single
  field alone.
  Disqualifying form: "HIGH complexity and a 4-6 sprint timeline means this requires careful planning" --
  "careful planning" is derivable from complexity alone; a failing conclusion survives removing one of the
  cited dimensions.

- [ ] C-14: Open unknowns in STEP 6 with typed fields; STEP 5 explicitly closed against unknowns.
  Disqualifying form: CONFIDENCE basis reading "Timeline unclear pending auth service contract" -- STEP 5
  carries an unverified item that belongs exclusively in STEP 6; structural separation exists but is leaky.

- [ ] C-15: Hypothesis inside PRE-FLIGHT GATE; synthesis names committed tier and sprint range when
  confirming or revising.
  Disqualifying form: "My earlier estimate held" -- confirmed without citing the specific committed values;
  "The hypothesis was confirmed: HIGH complexity and 4-6 sprints" passes even if C-22 phrasing is absent.

- [ ] C-16: If AMEND + amended dimension in synthesis -- synthesis updated or explicitly reaffirmed; default
  pass if no AMEND or no overlap.
  Disqualifying form: AMEND changes confidence from MEDIUM to LOW; confidence appears in cross-signal
  conclusion; conclusion still reads "MEDIUM confidence supports this investment" without reaffirmation or
  update -- amended dimension cited but not re-evaluated.

- [ ] C-17: At least one aspirational section (synthesis or unknowns) contains a sentence naming the
  specific anti-pattern being avoided.
  Disqualifying form: "This section may produce weak output if not filled carefully" -- quality risk named
  without identifying the specific anti-pattern form; "juxtaposition: restating fields in sequence" is the
  required specificity level.

**Aspirational -- structural/behavior (C-18-C-31):**

- [ ] C-18: PRE-FLIGHT GATE appears before all STEPs; contains scope boundary, break-even, and hypothesis
  fields with specific responses; includes stop instruction.
  Disqualifying form: a scope boundary note inside STEP 3 ("Note: migrations excluded from this sizing")
  satisfies C-09 content but fails C-18 -- it is a section reminder, not a structural gate that precedes
  all analysis.

- [ ] C-19: At least one section adjacent to unknowns canonical home (STEP 5) and at least one adjacent to
  scope exclusion canonical home carry explicit prohibition rules.
  Disqualifying form: CONFIDENCE basis section lists two unknowns without a prohibition against unknowns --
  canonical home (STEP 6) exists but the immediately adjacent section is unguarded.

- [ ] C-20: All plausible recipient sections for scope exclusion content (STEP 1, STEP 2, STEP 3, STEP 7)
  and for unknowns content (STEP 3, STEP 5, STEP 7) carry explicit prohibitions.
  Disqualifying form: STEP 2 and STEP 3 carry scope prohibitions but STEP 1 and STEP 7 do not -- fails
  C-20 even if C-19 passes; every plausible recipient must be guarded.

- [ ] C-21: Preliminary hypothesis is a field inside PRE-FLIGHT GATE gate block; synthesis names
  PRE-FLIGHT GATE and explicitly confirms or revises the commitment.
  Disqualifying form: a standalone "PRELIMINARY ESTIMATE" section appearing after PRE-FLIGHT GATE but
  before STEP 1 fails C-21 -- the hypothesis is structurally separate from the gate; passing C-18 (gate
  exists) and C-15 (synthesis confirms) independently does not satisfy C-21.

- [ ] C-22: Synthesis names PRE-FLIGHT GATE at (1) anchor instruction and (2) verdict close.
  Disqualifying form: "My earlier estimate was confirmed" fails -- "PRE-FLIGHT GATE" must appear by name at
  both points; "The preliminary estimate was confirmed" also fails even with the correct verdict form.

- [ ] C-23: At least one prohibition guard in an adjacent section names the canonical home by label.
  Disqualifying form: "Do not include scope exclusions here" fails C-23 -- it closes a door without naming
  where scope belongs; passing form: "scope was resolved in PRE-FLIGHT GATE, not in analysis steps."

- [ ] C-24: Synthesis Commitment chain has three labeled lines on separate lines: Gate commitment: /
  Analysis: / Verdict:.
  Disqualifying form: "The preliminary hypothesis committed in PRE-FLIGHT GATE (MEDIUM, 3-5 sprints) is
  confirmed: surface area is LOW and inertia cost is HIGH" fails C-24 -- all three steps embedded in one
  sentence; the chain must be scannable with each step independently readable.

- [ ] C-25: PRE-FLIGHT GATE enforcement contract names at least two downstream sections for scope exclusions
  AND names the section for hypothesis confirmation.
  Disqualifying form: "All three fields above are preconditions for STEP 1 through STEP 7" fails C-25 --
  naming steps as a continuation instruction does not distinguish scope enforcement sections from hypothesis
  enforcement section.

- [ ] C-26: Synthesis STRUCTURAL AMEND RE-EVALUATION DIRECTIVE states the requirement applies on every
  invocation "independent of whether an AMEND directive is present" and frames non-compliance as "a
  structural failure of this section's integrity."
  Disqualifying form: "If an AMEND directive is present in this invocation, complete the amendment fully
  ...Leaving synthesis unchanged is a silent contradiction -- it fails C-16" fails C-26 -- "in this
  invocation" is conditional; "it fails C-16" is criterion-referenced, not a structural property of the
  template.

- [ ] C-27: Both STEP 6 OPEN UNKNOWNS and STEP 7 SYNTHESIS carry a dedicated labeled FAILURE MODE block
  (> **FAILURE MODE FOR THIS SECTION**:) as a structurally separate element.
  Disqualifying form: > **Anti-pattern**: Restating sections in sequence is juxtaposition fails C-27 --
  it is structural annotation embedded in instruction prose, not a dedicated block whose absence creates a
  visible structural gap in the section's layout.

- [ ] C-28: Output includes a structured self-check block covering all aspirational criteria (C-09-C-31)
  with explicit pass/fail determination and supporting evidence per criterion.
  Disqualifying form: FAILURE MODE blocks in STEP 6 and STEP 7 do not satisfy C-28 -- they are
  section-level structural elements; C-28 requires a separate collective audit that evaluates every
  criterion by ID; a STEP 7 that "naturally demonstrates" C-13 compliance without a separate audit fails.

- [ ] C-29: Self-check items for all structural criteria (C-18-C-27) include both a pass condition and an
  exact structural disqualifying form.
  Disqualifying form: a self-check item reading "C-25: PRE-FLIGHT GATE names its enforcement sections"
  fails C-29 -- it describes the pass condition without naming the exact pattern that satisfies the surface
  signal but fails the criterion (e.g., "All fields are preconditions for STEP 1-7" looks like compliance).

- [ ] C-30: Self-check items for all depth and behavior aspirational criteria (C-09-C-17) include both a
  pass condition and an exact disqualifying form.
  Disqualifying form: a self-check item reading "C-09: At least one explicit exclusion named" fails C-30 --
  it describes the pass condition only; the disqualifying form must name the exact output pattern that looks
  like compliance but fails (e.g., "Standard integrations excluded" -- category label, not named sub-system).

- [ ] C-31: Self-check includes coverage of all essential (C-01-C-05) and recommended (C-06-C-08) criteria
  with pass/fail determination and supporting evidence.
  Essential and recommended tables are present above -- PASS.
  Disqualifying form: a self-check that covers all 23 aspirational criteria with complete precision but
  omits C-01-C-08 entries entirely fails C-31 -- the highest-consequence weight classes are outside the
  verification trace.

Fix any violation before writing.

---

Write artifact to: simulations/scout/size/{topic}-size-{date}.md
```

---

## Variation Summary

| ID | C-30 treatment | C-31 treatment | Expected aspirational | Score |
|----|----------------|----------------|-----------------------|-------|
| V-01 | PASS -- C-09-C-17 have exact disqualifying forms | FAIL (intentional) -- C-01-C-08 absent from self-check | 22/23 (fails C-31) | 99.57 |
| V-02 | FAIL (intentional) -- C-09-C-17 have pass conditions only | PASS -- C-01-C-08 present as flat checklist | 22/23 (fails C-30) | 99.57 |
| V-03 | PASS -- C-09-C-17 have disqualifying forms | PASS -- C-01-C-08 present as flat checklist | 23/23 | 100 |
| V-04 | PASS -- C-09-C-17 have disqualifying forms | PASS -- C-01-C-08 in table with disqualifying forms | 23/23 | 100 |
| V-05 | PASS -- C-09-C-17 have disqualifying forms | PASS -- C-01-C-08 in table with disqualifying forms | 23/23 | 100 |

**Key design differences for R10:**

- **C-30 mechanism**: The discriminator between C-30 PASS and FAIL is whether every depth/behavior
  self-check item names an exact output pattern that satisfies the surface signal but fails the criterion.
  V-01/V-03/V-04/V-05 add this treatment uniformly across C-09-C-17; V-02 retains pass-condition-only
  descriptions, failing C-30 by design.

- **C-31 mechanism**: The discriminator is whether C-01-C-08 appear anywhere in the self-check with
  pass/fail determination. V-02/V-03/V-04/V-05 add essential and recommended entries; V-01 bounds the
  self-check at aspirational criteria, failing C-31 by design.

- **V-03 vs V-04**: V-03 adds C-01-C-08 as a flat checklist (same format as aspirational entries). V-04
  presents C-01-C-08 as a table with three columns (ID / Pass condition / Disqualifying form), making the
  essential/recommended coverage structurally distinct and scannable at a glance. C-31 passes in both;
  V-04 adds structural scan reliability not required by the rubric.

- **V-04 vs V-05**: V-04 adds disqualifying forms to C-01-C-08 entries in the essential/recommended table.
  V-05 makes the treatment fully uniform: disqualifying forms appear for all 31 criteria across all weight
  classes. No rubric criterion requires disqualifying forms for essential/recommended (the requirement stops
  at aspirational criteria under C-29 and C-30). V-05 extends uniformity beyond rubric requirements to
  eliminate the remaining detection gap category.
