---
skill: quest-variate
skill_target: campaign-blueprint
date: 2026-03-17
round: 5
rubric: campaign-blueprint-rubric-v4-2026-03-17.md
---

# campaign-blueprint -- Prompt Variations R5 (rubric v4-2026-03-17)

Five complete, runnable skill body variations. Single-axis first (V-01 through V-03),
then two combinations (V-04, V-05).

## R5 Context

Rubric v4 adds two criteria extracted from R4 variation signals:

| Criterion | Signal source | Pattern |
|-----------|---------------|---------|
| **C-17** -- Compound Phase 0 co-location | V-02, V-04 (130/130) | C-09 + C-15 + C-16 all placed inside Phase 0 forms a single structural gate; completing Phase 0 satisfies all three simultaneously |
| **C-18** -- Canonical Phase 0 form | V-05 (127.5/130) | 4-field minimum (inertia baseline, Option 0 name, Option 0 cost, scout result); gate marker and propagation rule named as load-bearing elements |

Max total: 140 pts. Golden threshold: all 5 essentials FULL + composite >= 94/140 (67%).

Note: Signal 2 (inertia-first ordering in V-04 vs V-02) was NOT codified. The signal showed
inertia-first ordering does not add score over neutral ordering when a ledger template is present.
The ledger template (Option 0 name + cost) is the load-bearing element, already captured by C-16.

**R5 variation axes:**

| Axis | Label | Hypothesis |
|------|-------|-----------|
| A | Output format -- compound gate declaration | Explicitly labeling Phase 0 as containing three co-equal elements (C-09, C-15, C-16) and requiring all three before Artifact 1 achieves C-17 through structural declaration rather than structural coincidence |
| B | Lifecycle emphasis -- 4-field canonical minimum | Replacing multi-item Phase 0 checklists with exactly 4 labeled fields and naming gate marker + propagation rule as "load-bearing" achieves C-18 and removes executor confusion about over-specification |
| C | Phrasing register -- load-bearing vs density distinction | Using conversational register with an explicit "load-bearing vs optional" framing makes C-18's minimal sufficiency signal actionable without prescribing density |
| D | A + B combined (C-17 + C-18 compound gate) | Co-locating all three Phase 0 elements with canonical 4-field form achieves both C-17 and C-18 simultaneously |
| E | Full aspirational stack (D + C-13 + C-14 + C-11) | Adding discipline-split open questions, per-audience delta statements, and quantified Option 0 cost template on top of the compound Phase 0 maximizes composite score across all rubric bands |

---

## V-01 -- Axis A: Compound Gate Declaration

**Variation axis**: Output format -- compound Phase 0 structure with three labeled elements
**Hypothesis**: Explicitly labeling Phase 0 as containing three co-equal structural elements
(contract matrix = C-09, inertia forcing function = C-15, named do-nothing propagation = C-16)
and requiring all three to be printed before any artifact begins achieves C-17 through structural
declaration. When the three elements are named and co-located, an executor cannot satisfy C-15
without incidentally satisfying C-09 and C-16, and cannot skip C-09 without visibly failing the
Phase 0 gate. This achieves structural co-dependency without requiring an executor to know the
rubric numbers.

---

```
You are running /campaign-blueprint for: {topic}

PHASE 0 MUST BE COMPLETED BEFORE ANY ARTIFACT IS WRITTEN. Do not produce Artifact 1
until the Phase 0 gate token is printed.

================================
PHASE 0 -- COMPOUND GATE
================================

Phase 0 contains three co-equal structural elements. All three must be completed
and printed in this phase. They are declared together -- not separately, not
conditionally, not split across phases.

ELEMENT A -- ARTIFACT CONTRACT MATRIX

Print this table before proceeding:

| Field           | Spec                                                   | Proposal                                               | Pitch                                                  |
|-----------------|--------------------------------------------------------|--------------------------------------------------------|--------------------------------------------------------|
| READ            | Topic identity; scout signals (if found)               | Spec decisions; Option 0 cost                          | Proposal recommended option; Option 0 cost             |
| WRITE           | simulations/draft/specs/{topic}-spec-{date}.md         | simulations/draft/proposals/{topic}-proposal-{date}.md | simulations/draft/pitches/{topic}-pitch-{date}.md      |
| PRESERVE        | (first artifact)                                       | All spec decisions; Option 0 name                      | Recommended option name; Option 0 name                 |
| CARRIES FORWARD | Feature identity; Option 0 name+cost; decisions        | Recommended option; Option 0 cost                      | (final)                                                |

ELEMENT B -- PRE-ARTIFACT FORCING FUNCTION

Establish the inertia baseline and scout inventory here. Do not defer to Artifact 1.

  Topic:           [one sentence -- {topic} feature identity and primary audience]
  Inertia:         [what users do today without {topic} -- specific behavior]
  Scout inventory: glob simulations/scout/ for {topic} -- list files found, or "none"

ELEMENT C -- NAMED DO-NOTHING PROPAGATION

Assign the do-nothing option a proper name now. It is a tracked entity.

  Option 0 name:  "Option 0: [short behavior label]"
                  e.g., "Option 0: Manual Review" or "Option 0: {topic} Absent"
                  Not "do nothing." A name that characterizes the current behavior.

  Option 0 cost:  [what the current behavior costs -- time, errors, risk, or effort]
                  At least one concrete dimension.

  Propagation rule: Option 0 name appears verbatim in Artifact 2's options list
  (row 0) and in at least one pitch audience version's framing. It does not appear
  as an unnamed "do nothing" or "status quo" catch-all.

Gate token -- print this line to close Phase 0:
  [PHASE 0 COMPLETE -- Contract declared | Inertia anchored | Option 0: {name} assigned]

Artifact 1 does not begin until this token is printed.

================================
ARTIFACT 1: SPEC
================================

Write to: simulations/draft/specs/{topic}-spec-{date}.md
Read: Phase 0 Elements B and C. Pull scout-requirements if found in inventory.

Required sections:
  PURPOSE        -- First sentence references the Phase 0 inertia baseline.
                    Why does Option 0 persist? What does it cost?
  REQUIREMENTS   -- MoSCoW-tagged. At least three M items. M items address
                    known user gaps from the inertia baseline.
  DESIGN         -- Technical approach; what is included; what is explicitly excluded.
  CONSTRAINTS    -- Specific named technical, platform, timeline, and resource limits.
  OPEN QUESTIONS -- At least two specific non-boilerplate gaps. At least one names
                    a missing signal by namespace.

[SPEC WRITTEN]
GATE: Artifact 2 does not begin until simulations/draft/specs/{topic}-spec-{date}.md
is confirmed written to disk.

================================
ARTIFACT 2: PROPOSAL
================================

Write to: simulations/draft/proposals/{topic}-proposal-{date}.md
Read: Spec. Pull scout-feasibility if found in inventory.

Minimum three options. Row 0 uses the Phase 0 Option 0 name verbatim:

| Option | Name                    | Description | Pros | Cons                              | Risk | Effort |
|--------|-------------------------|-------------|------|-----------------------------------|------|--------|
| 0      | [Phase 0 Option 0 name] |             |      | [Option 0 cost -- concrete dimension] |      |        |
| B      |                         |             |      |                                   |      |        |
| C      |                         |             |      |                                   |      |        |

RECOMMENDATION: Named option. Rationale references at least one M-tier spec requirement
and at least one spec constraint. Acknowledges the strongest objection.

[PROPOSAL WRITTEN -- Option {X} recommended]
GATE: Artifact 3 does not begin until simulations/draft/proposals/{topic}-proposal-{date}.md
is confirmed written to disk.

================================
ARTIFACT 3: PITCH
================================

Write to: simulations/draft/pitches/{topic}-pitch-{date}.md
Read: Proposal recommended option. Pull scout-positioning if found in inventory.

Three audience versions: EXEC / DEV / MAKER.
Each version: hook (Option 0 cost as anchor) / what it does / why it matters / CTA.

  EXEC  -- Business outcome; Option 0 cost in business terms; CTA: approve/fund/unblock.
  DEV   -- Workflow change; spec design referenced; CTA: join beta/review spec.
  MAKER -- Daily friction resolved; plain language; CTA: try it/sign up/start now.

Option 0 name from Phase 0 appears verbatim in at least one version.
ANTI-POSITIONING: "What {topic} is NOT." At least two specific named exclusion statements.

[PITCH WRITTEN]

================================
CAMPAIGN CLOSE
================================

| Artifact | Path                                                   | Gate token printed | Option 0 name tracked |
|----------|--------------------------------------------------------|--------------------|-----------------------|
| Phase 0  | --                                                     | Y/N                | Y/N (assigned)        |
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md         | Y/N                | --                    |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md | Y/N                | Y/N (verbatim row 0)  |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md      | Y/N                | Y/N (verbatim framing)|
```

---

## V-02 -- Axis B: Canonical Phase 0 Minimum Form

**Variation axis**: Lifecycle emphasis -- Phase 0 as a 4-field canonical template with load-bearing elements explicitly named
**Hypothesis**: Providing Phase 0 as a fill-in template with exactly 4 labeled fields (inertia
baseline, Option 0 name, Option 0 cost, scout result) and explicitly identifying the gate marker
and propagation rule as "load-bearing" -- not optional density -- achieves C-18 at minimum word
count. The key signal from the rubric: a 4-field Phase 0 achieves full C-15/C-16 credit. The
gate marker and propagation rule are the load-bearing elements, not density. This variation makes
that design principle visible to the executor so they do not over-specify Phase 0 while also not
under-specifying it.

---

```
You are running /campaign-blueprint for: {topic}

This skill produces three artifacts in sequence: spec, proposal, pitch. Phase 0 is
the structural gate. Complete Phase 0 and print the gate marker before Artifact 1.

================================
PHASE 0 -- CAMPAIGN GATE (canonical form)
================================

Four fields. These are the minimum required for Phase 0 to be complete. Fill them in.
Additional fields are permitted but are not required -- density beyond these four does
not change Phase 0 compliance status.

  INERTIA BASELINE:  [what users do today without {topic} -- one sentence, specific]

  OPTION 0 NAME:     [a proper name for the do-nothing option]
                     Format: "Option 0: [short behavior label]"
                     Example: "Option 0: Manual Coordination" or "Option 0: {topic} Absent"
                     Not "Status Quo" alone. A name that characterizes the current behavior.

  OPTION 0 COST:     [what the current behavior costs -- time, errors, risk, or effort]
                     One concrete dimension is sufficient.

  SCOUT RESULT:      [glob simulations/scout/ for {topic}; list files found or "none"]
                     Run unconditionally.

Two load-bearing elements. These are structural -- they enforce downstream compliance.
They are not optional even when the four-field minimum is otherwise met.

  GATE MARKER (load-bearing):
    Print this exact token when all four fields above are filled:
      [PHASE 0 COMPLETE]
    Artifact 1 does not begin until this token appears in the output.

  PROPAGATION RULE (load-bearing):
    The OPTION 0 NAME assigned above propagates verbatim to:
      -- Artifact 2: named as row 0 in the options list (the do-nothing option)
      -- Artifact 3: referenced by name in at least one audience version's framing
    It may not appear only as an unnamed "do nothing" or generic "status quo."

================================
ARTIFACT 1: SPEC
================================

Write to: simulations/draft/specs/{topic}-spec-{date}.md
Read: INERTIA BASELINE and SCOUT RESULT from Phase 0.

Five required sections:
  PURPOSE        -- Feature intent; INERTIA BASELINE from Phase 0 referenced.
  REQUIREMENTS   -- MoSCoW-tagged. At least three M items.
  DESIGN         -- Technical approach; inclusions and exclusions both stated.
  CONSTRAINTS    -- Specific named limits. Not generic.
  OPEN QUESTIONS -- At least two specific gaps. At least one names a missing signal.

[SPEC WRITTEN]

================================
ARTIFACT 2: PROPOSAL
================================

Write to: simulations/draft/proposals/{topic}-proposal-{date}.md
Read: Spec. Pull scout-feasibility if in inventory.

Minimum three options. First option: use OPTION 0 NAME from Phase 0 verbatim as the
row name. Option 0 Cons must include at least one concrete dimension from OPTION 0 COST.

Per option: Description / Pros / Cons / Effort / Risk.
RECOMMENDATION: Named option. Rationale references spec requirements and constraints.

[PROPOSAL WRITTEN -- Option {X} recommended]

================================
ARTIFACT 3: PITCH
================================

Write to: simulations/draft/pitches/{topic}-pitch-{date}.md
Read: Proposal recommended option. Pull scout-positioning if in inventory.

Three audience versions: EXEC / DEV / MAKER.
Each version: hook / what it does / why it matters / CTA.
OPTION 0 NAME from Phase 0 appears verbatim in at least one version.
ANTI-POSITIONING: At least two named "What this is NOT" statements.

[PITCH WRITTEN]

================================
CAMPAIGN CLOSE
================================

| Artifact | Path                                                   | [PHASE 0 COMPLETE] | OPTION 0 NAME propagated |
|----------|--------------------------------------------------------|--------------------|--------------------------|
| Phase 0  | --                                                     | Y/N                | (assigned)               |
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md         | --                 | --                       |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md | --                 | Y/N (row 0 verbatim)     |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md      | --                 | Y/N (at least 1 version) |
```

---

## V-03 -- Axis C: Load-Bearing vs Density Distinction (Conversational Register)

**Variation axis**: Phrasing register -- conversational framing that makes "load-bearing vs
optional density" explicit
**Hypothesis**: Using conversational register to explicitly distinguish between load-bearing
requirements (the 4 canonical Phase 0 fields, the gate marker, the propagation rule) and
"optional additional context" achieves C-18's minimal sufficiency intent without being terse
to the point of ambiguity. The executor who reads "these two things are not optional even if
you have filled in the four fields" understands what compliance means independently of rubric
knowledge. This variation tests whether the load-bearing distinction is more legible in prose
than in table format.

---

```
You are running /campaign-blueprint for: {topic}

Your job is to produce three artifacts that together make the case for building {topic}:
a spec, a proposal, and a pitch. Work through them in order -- each builds on the last.

Before writing anything, run Phase 0. It sets up the campaign. It must finish before
any artifact starts.

================================
PHASE 0 -- SETUP
================================

Answer four questions. These are the load-bearing fields -- the ones you actually need
to proceed. More context is fine if you have it, but it is not required for this phase
to be complete.

  Question 1: What do users do today instead of {topic}?
  One sentence. Specific behavior -- tools, manual steps, or workarounds.
  --> INERTIA BASELINE: ___

  Question 2: What do you call the option of not building {topic}?
  Give it a name that reflects the actual current behavior, not just "do nothing."
  Specific enough that a reader knows what they are choosing if they pick it.
  --> OPTION 0 NAME: "Option 0: ___"

  Question 3: What does that inertia cost?
  Name at least one concrete dimension: time lost, errors introduced, decisions
  blocked, or risk carried. A number is better than a word.
  --> OPTION 0 COST: ___

  Question 4: What scout signals already exist?
  Glob simulations/scout/ for {topic}. List what you find, or write "none."
  --> SCOUT RESULT: ___

Two things that are not optional -- even if the four questions above are answered:

  The gate marker. Print [PHASE 0 COMPLETE] when the four fields are filled.
  Artifact 1 does not start until you see that token in the output. This is the
  structural stop, not a formatting suggestion.

  The propagation rule. The OPTION 0 NAME you wrote above must appear verbatim in the
  proposal's options list and in at least one pitch audience version. Not "the status
  quo" or "do nothing" -- the exact name you assigned. This makes it a tracked entity
  across the campaign, not a catch-all final option.

================================
ARTIFACT 1: SPEC
================================

Think of the spec as answering: "What are we actually building and why?"
Write simulations/draft/specs/{topic}-spec-{date}.md

Work through these five sections:

  PURPOSE        -- What problem are we solving? Reference INERTIA BASELINE from Phase 0.
                    Why does the current workaround persist? What does it cost users?
  REQUIREMENTS   -- What must the feature do? MoSCoW-tagged. At least three M items.
                    M items are what removes Option 0 friction.
  DESIGN         -- How would it work? At a level someone could evaluate. What's excluded?
  CONSTRAINTS    -- What are the real limits? Specific, not aspirational.
  OPEN QUESTIONS -- What don't we know yet? At least two. At least one names a signal
                    namespace that would answer it.

[SPEC WRITTEN]

================================
ARTIFACT 2: PROPOSAL
================================

Think of the proposal as answering: "What are the real options and which one do we pick?"
Write simulations/draft/proposals/{topic}-proposal-{date}.md

Read the spec first. Three or more options. First option is OPTION 0 NAME from Phase 0 --
verbatim, as row 0. Its cost is in the Cons column. At least one concrete dimension.

Per option: Description / Pros / Cons / Effort / Risk.
RECOMMENDATION: Which option and why, citing spec requirements and constraints.
Acknowledge the strongest objection to the recommended option.

[PROPOSAL WRITTEN -- Option {X} recommended]

================================
ARTIFACT 3: PITCH
================================

Think of the pitch as answering: "How do we talk about this to three different audiences?"
Write simulations/draft/pitches/{topic}-pitch-{date}.md

Read the proposal first. Three audience versions: EXEC / DEV / MAKER.
Each version: hook / what it does / why it matters to this audience specifically / CTA.

  EXEC  -- They want the outcome. What problem goes away? What does inaction cost? Ask.
  DEV   -- They want to know what changes. Show them the tool. What can they do now?
  MAKER -- They want to know if this is for them. Skip jargon. Is it complicated?

OPTION 0 NAME from Phase 0 appears verbatim in at least one version.
ANTI-POSITIONING: What {topic} is NOT. Name at least two specific use cases it excludes.

[PITCH WRITTEN]

================================
WHEN YOU'RE DONE
================================

List the three file paths. Note how many open questions are in the spec. Confirm the
pitch opens from the proposal's recommended option. Note whether OPTION 0 NAME
appeared verbatim in the proposal and pitch.
```

---

## V-04 -- Combined: Compound Phase 0 Gate (C-17 + C-18)

**Variation axes**: A (compound gate declaration) + B (canonical 4-field minimum)
**Hypothesis**: Consolidating the contract matrix (C-09), the pre-artifact forcing function (C-15),
and the named do-nothing propagation (C-16) inside a single Phase 0 block -- with the 4-field
canonical minimum explicitly named and gate marker + propagation rule identified as load-bearing --
achieves both C-17 and C-18 simultaneously at a single structural gate. An executor who completes
Phase 0 satisfies all three elements without a separate declaration step that can be skipped.
The compound structure prevents the dissociation failure mode (C-09 declared outside Phase 0,
C-16 deferred to proposal time) that the rubric targets.

---

```
You are running /campaign-blueprint for: {topic}

================================
PHASE 0 -- COMPOUND GATE
================================

Phase 0 is a single mandatory structural gate. It contains three elements. All three
are declared here, together. An executor who completes Phase 0 satisfies all three
simultaneously -- there is no separate declaration step elsewhere that can be deferred
or skipped.

Phase 0 minimum form: four fields (see Element 2). Density beyond these four is
permitted but is not required for Phase 0 to be complete. The gate marker and
propagation rule are the load-bearing elements -- they are not optional even when
the four fields are filled.

ELEMENT 1 -- ARTIFACT CONTRACT MATRIX (READ/WRITE/PRESERVE/CARRIES FORWARD)

| Field           | Spec                                                   | Proposal                                               | Pitch                                                  |
|-----------------|--------------------------------------------------------|--------------------------------------------------------|--------------------------------------------------------|
| READ            | Topic identity; scout signals (if found)               | Spec decisions; Option 0 cost                          | Proposal recommended option; Option 0 cost             |
| WRITE           | simulations/draft/specs/{topic}-spec-{date}.md         | simulations/draft/proposals/{topic}-proposal-{date}.md | simulations/draft/pitches/{topic}-pitch-{date}.md      |
| PRESERVE        | (first artifact)                                       | All spec decisions; Option 0 name                      | Recommended option name; Option 0 name                 |
| CARRIES FORWARD | Feature identity; Option 0 name+cost; decisions        | Recommended option; Option 0 cost                      | (final)                                                |

ELEMENT 2 -- PRE-ARTIFACT BASELINE (four canonical fields; additional fields permitted)

  INERTIA BASELINE:  [what users do today without {topic} -- one sentence, specific]
  OPTION 0 NAME:     "Option 0: [behavior label]" -- characterizes the current behavior,
                     not a generic "do nothing" or "status quo"
  OPTION 0 COST:     [what the current behavior costs -- time, errors, risk, or effort;
                     one concrete dimension is sufficient]
  SCOUT RESULT:      [glob simulations/scout/ for {topic}; list files found or "none";
                     run unconditionally]

ELEMENT 3 -- NAMED DO-NOTHING PROPAGATION

  GATE MARKER (load-bearing): print this token to close Phase 0:
    [PHASE 0 COMPLETE -- Option 0: {name} | Cost: {cost} | Scout: {result}]
  Artifact 1 does not begin until this token is printed.

  PROPAGATION RULE (load-bearing): OPTION 0 NAME from Element 2 propagates verbatim to:
    -- Artifact 2: row 0 of the options list, as the named do-nothing option
    -- Artifact 3: at least one audience version's framing
  It appears as the specific name assigned here. It may not appear only as an unnamed
  "do nothing" or "status quo" catch-all at the end of the options list.

================================
ARTIFACT 1: SPEC
================================

Write to: simulations/draft/specs/{topic}-spec-{date}.md
Reads: Phase 0 Elements 2 and 3. Pull scout-requirements if found in inventory.

Required sections:
  PURPOSE        -- First sentence references the Phase 0 INERTIA BASELINE verbatim.
                    Why does Option 0 persist? What does it cost?
  REQUIREMENTS   -- MoSCoW-tagged. At least three M items. M items address known user
                    gaps from the inertia baseline.
  DESIGN         -- Technical approach; what is included; what is explicitly excluded.
  CONSTRAINTS    -- Named specific limits (technical, platform, timeline, resource).
  OPEN QUESTIONS -- At least two specific non-boilerplate gaps. At least one names a
                    missing signal by namespace.

[SPEC WRITTEN]
GATE: Artifact 2 does not begin until simulations/draft/specs/{topic}-spec-{date}.md
is confirmed written to disk.

================================
ARTIFACT 2: PROPOSAL
================================

Write to: simulations/draft/proposals/{topic}-proposal-{date}.md
Reads: Spec. Pull scout-feasibility if found in inventory.

Minimum three options. Row 0 uses Phase 0 OPTION 0 NAME verbatim:

| Option | Name                    | Description | Pros | Cons                                    | Risk | Effort |
|--------|-------------------------|-------------|------|-----------------------------------------|------|--------|
| 0      | [Phase 0 OPTION 0 NAME] |             |      | [OPTION 0 COST -- concrete dimension]   |      |        |
| B      |                         |             |      |                                         |      |        |
| C      |                         |             |      |                                         |      |        |

Option 0 Cons cell: at least one concrete dimension (time / effort / risk / error rate).
Pull scout-feasibility for effort and risk estimates if found.

RECOMMENDATION: Named option. Rationale references at least one M-tier spec requirement
and at least one spec constraint.

[PROPOSAL WRITTEN -- Option {X} recommended]
GATE: Artifact 3 does not begin until simulations/draft/proposals/{topic}-proposal-{date}.md
is confirmed written to disk.

================================
ARTIFACT 3: PITCH
================================

Write to: simulations/draft/pitches/{topic}-pitch-{date}.md
Reads: Proposal recommended option. Pull scout-positioning if found in inventory.

Three audience versions: EXEC / DEV / MAKER.
Each version: hook (Option 0 cost as anchor) / what it does / why it matters / CTA.

  EXEC  -- Business outcome; Option 0 cost in business terms; CTA: approve/fund/unblock.
  DEV   -- Workflow change; spec design referenced; CTA: join beta/review spec.
  MAKER -- Daily friction resolved; plain language; CTA: try it/sign up/start now.

OPTION 0 NAME from Phase 0 appears verbatim in at least one version.
ANTI-POSITIONING: "What {topic} is NOT." At least two specific named exclusion statements.

[PITCH WRITTEN]

================================
CAMPAIGN CLOSE
================================

| Artifact | Path                                                   | Gate token                        | Option 0 name tracked         |
|----------|--------------------------------------------------------|-----------------------------------|-------------------------------|
| Phase 0  | --                                                     | [PHASE 0 COMPLETE] printed: Y/N   | assigned in Element 2: Y/N    |
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md         | [SPEC WRITTEN]: Y/N               | --                            |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md | [PROPOSAL WRITTEN]: Y/N           | verbatim row 0: Y/N           |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md      | [PITCH WRITTEN]: Y/N              | verbatim in at least 1: Y/N   |
```

---

## V-05 -- Combined: Full Aspirational Stack (C-17 + C-18 + C-13 + C-14 + C-11)

**Variation axes**: A + B + discipline open questions (C-13) + per-audience delta (C-14) +
quantified Option 0 cost template (C-11)
**Hypothesis**: Building on the V-04 compound Phase 0 and adding three additional aspirational
criteria -- discipline-split open questions (C-13: one product/user question + one technical/
architecture question), per-audience delta statements (C-14: explicit "what changes for [audience]"
in each pitch version), and a quantified cost-of-inertia template for Option 0 (C-11: time, effort,
or risk dimension filled in, not qualitative only) -- produces maximum composite score across all
rubric bands. This variation targets 9 of 10 aspirational criteria simultaneously. The only
aspirational criterion not directly targeted is C-10 (pitch anti-positioning), which is already
covered by the base artifact requirements.

---

```
You are running /campaign-blueprint for: {topic}

================================
PHASE 0 -- COMPOUND GATE
================================

Phase 0 is a single mandatory structural gate. Three elements. All co-located here.
Completing Phase 0 satisfies all three simultaneously.

Minimum form: four fields in Element 2. Additional fields permitted, not required.
Gate marker and propagation rule are load-bearing -- not optional.

ELEMENT 1 -- ARTIFACT CONTRACT MATRIX

| Field           | Spec                                                   | Proposal                                               | Pitch                                                  |
|-----------------|--------------------------------------------------------|--------------------------------------------------------|--------------------------------------------------------|
| READ            | Topic identity; scout signals (if found)               | Spec decisions; Option 0 cost template                 | Proposal recommended option; Option 0 cost             |
| WRITE           | simulations/draft/specs/{topic}-spec-{date}.md         | simulations/draft/proposals/{topic}-proposal-{date}.md | simulations/draft/pitches/{topic}-pitch-{date}.md      |
| PRESERVE        | (first artifact)                                       | All spec decisions; Option 0 name                      | Recommended option name; Option 0 name                 |
| CARRIES FORWARD | Feature identity; Option 0 name+cost; decisions        | Recommended option; Option 0 cost                      | (final)                                                |

ELEMENT 2 -- PRE-ARTIFACT BASELINE (four canonical fields)

  INERTIA BASELINE:  [what users do today without {topic} -- one sentence, specific]
  OPTION 0 NAME:     "Option 0: [behavior label]" -- characterizes the current behavior
  OPTION 0 COST:     complete this template:
                       Time dimension:   [e.g., "X hours/week per user" or "N/A"]
                       Effort dimension: [e.g., "X manual steps per operation" or "N/A"]
                       Risk dimension:   [e.g., "High -- no audit trail" or "N/A"]
                     At least one dimension must be filled with a non-N/A value.
  SCOUT RESULT:      [glob simulations/scout/ for {topic}; list files found or "none"]

ELEMENT 3 -- NAMED DO-NOTHING PROPAGATION

  GATE MARKER (load-bearing):
    [PHASE 0 COMPLETE -- Option 0: {name} | Cost: {one concrete dimension} | Scout: {result}]
  Artifact 1 does not begin until this token is printed.

  PROPAGATION RULE (load-bearing): OPTION 0 NAME propagates verbatim to:
    -- Artifact 2: row 0 of the options list
    -- Artifact 3: at least one audience version's framing
  It appears as the specific name, not as an unnamed catch-all.

================================
ARTIFACT 1: SPEC
================================

Write to: simulations/draft/specs/{topic}-spec-{date}.md
Reads: Phase 0 Elements 2 and 3. Pull scout-requirements if found in inventory.

Required sections:
  PURPOSE        -- First sentence references Phase 0 INERTIA BASELINE.
  REQUIREMENTS   -- MoSCoW-tagged. At least three M items.
  DESIGN         -- Technical approach; inclusions and exclusions stated.
  CONSTRAINTS    -- Named specific limits (technical, platform, timeline, resource).
  OPEN QUESTIONS -- At least two specific non-boilerplate gaps.
                    DISCIPLINE RULE: include at least one question from the product/user
                    domain (user behavior, adoption, workflow change) and at least one
                    from the technical/architecture domain (implementation, feasibility,
                    integration). For each question, name the signal namespace that could
                    resolve it (e.g., "scout-requirements", "prove-interview", "trace-contract").

[SPEC WRITTEN]
GATE: Artifact 2 does not begin until simulations/draft/specs/{topic}-spec-{date}.md
is confirmed written to disk.

================================
ARTIFACT 2: PROPOSAL
================================

Write to: simulations/draft/proposals/{topic}-proposal-{date}.md
Reads: Spec. Pull scout-feasibility if found in inventory.

Minimum three options. Row 0 uses Phase 0 OPTION 0 NAME verbatim.

OPTION 0 COST TEMPLATE: the Cons cell for Option 0 must use the cost template from
Phase 0 Element 2. The concrete dimension(s) filled in Phase 0 appear here as the
priced cost-of-inertia. Not qualitative description only.

| Option | Name                    | Description | Pros | Cons                                         | Risk | Effort |
|--------|-------------------------|-------------|------|----------------------------------------------|------|--------|
| 0      | [Phase 0 OPTION 0 NAME] |             |      | [Time/Effort/Risk from Phase 0 template]     |      |        |
| B      |                         |             |      |                                              |      |        |
| C      |                         |             |      |                                              |      |        |

Pull scout-feasibility for effort and risk estimates on non-zero options if found.
RECOMMENDATION: Named option. Rationale references at least one M-tier spec requirement
and at least one spec constraint.

[PROPOSAL WRITTEN -- Option {X} recommended]
GATE: Artifact 3 does not begin until simulations/draft/proposals/{topic}-proposal-{date}.md
is confirmed written to disk.

================================
ARTIFACT 3: PITCH
================================

Write to: simulations/draft/pitches/{topic}-pitch-{date}.md
Reads: Proposal recommended option. Pull scout-positioning if found in inventory.

Three audience versions: EXEC / DEV / MAKER.

Each version must contain these four elements:
  1. Hook -- Option 0 cost as the opening anchor (one sentence that lands the problem)
  2. What it does -- two to three sentences, audience-appropriate vocabulary
  3. Why it matters -- explicit DELTA STATEMENT: "What changes for [audience] is [X]."
                       This is not just audience-appropriate language. It is a named
                       delta from the base recommendation -- what specifically is
                       different for this audience compared to the others.
  4. CTA -- concrete next step for this audience

Framing per audience:
  EXEC  -- Outcome and approval framing; Option 0 cost in business terms.
           Delta: [what the executive gains / risk eliminated that others do not see]
           CTA: approve/fund/unblock.
  DEV   -- Workflow change; spec design referenced; specific capability unlocked.
           Delta: [what the developer can now do that was previously blocked or manual]
           CTA: join beta/review spec.
  MAKER -- Daily friction resolved; plain language; "is this for me?" framing.
           Delta: [what daily task changes or disappears for this user type]
           CTA: try it/sign up/start now.

OPTION 0 NAME from Phase 0 appears verbatim in at least one version.
ANTI-POSITIONING: "What {topic} is NOT." At least two specific named exclusion statements.
Each must rule out an adjacent or commonly confused use case by name -- not generic hedging.

[PITCH WRITTEN]

================================
CAMPAIGN CLOSE
================================

| Artifact | Path                                                   | Gate token                        | Option 0 name tracked         |
|----------|--------------------------------------------------------|-----------------------------------|-------------------------------|
| Phase 0  | --                                                     | [PHASE 0 COMPLETE] printed: Y/N   | assigned in Element 2: Y/N    |
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md         | [SPEC WRITTEN]: Y/N               | --                            |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md | [PROPOSAL WRITTEN]: Y/N           | verbatim row 0: Y/N           |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md      | [PITCH WRITTEN]: Y/N              | verbatim in at least 1: Y/N   |

Open questions discipline check:
  Product/user question present in spec: Y/N
  Technical/architecture question present in spec: Y/N

Per-audience delta check:
  EXEC delta statement present: Y/N
  DEV delta statement present: Y/N
  MAKER delta statement present: Y/N

Option 0 cost template check:
  At least one concrete dimension non-N/A in Phase 0: Y/N
  Carried into Proposal Option 0 Cons cell: Y/N
```
