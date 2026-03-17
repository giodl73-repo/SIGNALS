---
skill: quest-variate
skill_target: campaign-specify
round: 4
date: 2026-03-16
rubric: simulations/quest/rubrics/campaign-specify-rubric-v4-2026-03-16.md
---

# Variations -- campaign-specify / Round 4

Five complete, runnable skill body variations targeting the v4 rubric.
Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

**R3 diagnosis driving R4 axis choices:**

| New Criterion | R3 Status | Gap | R4 Target |
|---------------|-----------|-----|-----------|
| C-16 (named defeat block) | V-04 + V-05 | Structural label required | Preserve |
| C-17 (stability trajectory) | V-05 only | Must appear in BOTH Phase 0 AND Phase 2 cite | New axis V-01 |
| C-18 (intra-Phase 0 gate) | V-01 only | "do not advance" between Phase 0 steps | Preserve + combine |
| C-19 (per-artifact inline gate) | V-04 only | Gate at production point, not end-of-skill | New axis V-02 |
| C-20 (voice save gate) | None | Pre-save check + conditional rewrite trigger | New axis V-03 |

No R3 variation earned all five new criteria simultaneously.
V-05 (98.3) is closest: earned C-16, C-17, C-20 but lost C-19 (end-of-skill table != inline gate)
and its Step 0b stability row did not satisfy C-17 because the Phase 2 defeat block
did not explicitly cite it with the required form ("Do Nothing is not stable: [assessment]").

R4 single-axis variations each target one unearned criterion in isolation.
R4 combinations stack mechanisms toward the 12/12 ceiling.

| Axis | Mechanism | Targets |
|------|-----------|---------|
| Stability trajectory | Phase 0 stability assessment as named output + required citation in Phase 2 defeat block | C-17 |
| Per-artifact inline gate | Gate instruction collocated with each artifact write, not end-of-skill | C-19 |
| Voice save gate | Pre-save verification + conditional rewrite trigger before pitch file is created | C-20 |
| Stability + inline gates + named block | Combine V-01, V-02, V-04 R3 mechanisms | C-16, C-17, C-19 |
| Full synthesis | All five new criteria + all R3 essentials/recommended | C-16, C-17, C-18, C-19, C-20 |

---

## V-01 -- Axis: Stability Trajectory (C-17 target)

**Hypothesis**: Adding a named "Stability Assessment" step in Phase 0 that explicitly evaluates
whether the Do Nothing cost is stable or worsening -- and requiring the Phase 2 defeat block to
cite it verbatim with the form "Do Nothing is not stable: [assessment]" -- causes C-17 to be
earned without disrupting the other criteria. The stability argument must appear in BOTH Phase 0
(where it is established) and Phase 2 (where it is cited). A "this cost compounds" sentence in
Phase 2 alone does not satisfy C-17; the two-location requirement is the key structural constraint.

```
Run the campaign-specify skill for: {{topic}}

Produce three artifacts in sequence: spec, proposal, pitch. Execute phases 0-3 in order.
Do not begin a later phase until all required outputs of the current phase are complete.

---

## Phase 0 -- Audience Foundation

Before writing any artifact, complete all four steps below.

**Step 0a -- Inertia Costs (required first)**

Name what each audience LOSES if {{topic}} does not ship. Concrete and audience-specific.
Generic claims ("this would help") do not pass.

Exec inertia cost: [Specific revenue exposure, competitive gap, or risk that persists without
this feature. Name a consequence, not a category.]

Dev inertia cost: [Specific workaround burden, capability gap, or tool-friction that persists.
Name the friction, not the feeling.]

Maker inertia cost: [Specific blocked or degraded workflow step that persists. Name the step.]

Do not advance to Step 0b until all three inertia costs are complete.

**Step 0b -- Do Nothing Stability Assessment**

Evaluate the trajectory of the Do Nothing option. This output must be cited in Phase 2.

Stability assessment: [Is the cost of Do Nothing stable or worsening? Cite the specific
mechanism: does the exec exposure grow as competitors ship? Does the dev workaround accumulate
technical debt? Does the maker's blocked step become a larger obstacle as volume grows?
Choose one of: "Do Nothing is stable: [rationale]" or "Do Nothing is not stable: [rationale]."]

Timeline indicator: [If worsening, by when does the cost become acute? If stable, state "stable
at current cost level."]

Do not advance to Step 0c until the stability assessment is complete.

**Step 0c -- Voice Contracts**

Using the inertia costs and stability assessment above as grounding, write one sentence per audience:

Exec voice: [Outcomes/risk framing -- reference the exec inertia cost and stability timeline]
Dev voice: [Capability/friction framing -- reference the dev inertia cost]
Maker voice: [Workflow framing -- plain language, reference the maker inertia cost]

**Step 0d -- Scout Pull**

Glob `simulations/scout/**/*.md` for {{topic}}. List any files found and note which artifact
(spec, proposal, pitch) each file is most relevant to. If none found: note "no scout signals"
and proceed.

---

## Phase 1 -- Technical Spec

Pull from `simulations/scout/` broadly. Note which files from Step 0d were used.

Write the spec. Save to: `simulations/draft/specs/{{topic}}-spec-{{date}}.md`

Six sections required. Do not skip or merge any section.

### Overview
One paragraph describing what the feature does and why it exists.

### User Problem
The problem users face today. Reference the dev and maker inertia costs from Step 0a --
these are evidence of the problem, not invented examples.

### Proposed Solution
What the feature does. Incorporate any scout-requirements or scout-feasibility signals
from Step 0d.

### Constraints
At least three: technical, scope, platform.

### Open Questions
At least three named ambiguities.

### Self-Review
At least one named gap. "No gaps found" fails this section.

---

## Phase 2 -- Business Proposal

Pull from `simulations/scout/scout-feasibility/` before writing. Note files used.

Write the proposal. Save to: `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md`

Three options minimum. Option 1 MUST be named **Do Nothing**.

For each option: description, pros, cons, risk, effort.

Then write the **Recommendation** section with this exact structure:

We recommend [chosen option].

**Defeating Do Nothing**

Do Nothing perpetuates [cite the most decisive inertia cost from Step 0a -- name the audience
and the specific cost]. [Cite the Step 0b stability assessment verbatim: "Do Nothing is not
stable: [assessment from Step 0b]" or "Do Nothing is stable but absorbs [cost] permanently."]
We choose to build because [why the cost is not acceptable given the stability trajectory].

**Defeating [other option]**

We prefer [chosen option] over [other option] because [specific trade-off or risk from the
options analysis above -- traceable to a specific field in the options, not a preference statement].

The "Defeating Do Nothing" block must cite the Step 0b stability assessment by name.
A defeat block that argues cost alone without citing the stability trajectory fails C-17.

---

## Phase 3 -- Executive Pitch

Pull from `simulations/scout/scout-positioning/` before writing. Note files used.

Write the pitch. Save to: `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`

Four sections:

### Exec Version
Lead with the exec inertia cost from Step 0a. Structure: [exec cost hook] ->
[what changes] -> [business outcome/ROI] -> [call to action].
Do not open with a product description.

### Dev Version
Lead with the dev inertia cost from Step 0a. Structure: [friction hook] ->
[what you can now do] -> [capability unlocked] -> [call to action].
Do not open with an outcomes/ROI frame.

### Maker Version
Lead with the maker inertia cost from Step 0a. Plain language. No jargon.
Structure: [blocked step hook] -> [what you can now do] -> [why it matters] ->
[call to action]. Test: readable without the spec by a non-technical user.

### Anti-Positioning
3-5 "This is not..." statements. Separate from the three audience versions above.

---

## Completion Check

After all three artifacts are written:

1. Verify spec exists at: `simulations/draft/specs/{{topic}}-spec-{{date}}.md`
2. Verify proposal exists at: `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md`
3. Verify pitch exists at: `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`

If any artifact is missing: write it now before stopping.
Do not emit a completion summary until all three files exist on disk.

Final index:
- Artifact paths (all three)
- Scout files used per phase
- Step 0a inertia costs confirmed (all three audiences)
- Step 0b stability assessment: state which form was used ("stable" or "not stable")
- Confirm the Step 0b stability assessment was cited verbatim in the Defeating Do Nothing block
```

**Rubric targeting**:
- C-17: Step 0b establishes stability assessment as a named output; Phase 2 Defeating Do Nothing block requires verbatim citation. Two-location requirement (Phase 0 establish + Phase 2 cite) satisfied by construction. "Do Nothing is not stable: [assessment]" form prescribed explicitly.
- C-18: "Do not advance to Step 0b" and "Do not advance to Step 0c" gates between internal Phase 0 steps.
- C-16: "Defeating Do Nothing" as a labeled block structurally separate from "Defeating [other option]."
- C-01 through C-15: Preserved from R3 V-01 base with stability additions.

**Risk**: The "cite verbatim" instruction for Step 0b may produce a copy-paste that satisfies form but not substance -- a stability assessment that says "stable" produces a weaker defeat argument than one that says "not stable." The scorer must check whether the stability trajectory argument in Phase 2 is specific, not merely present.

---

## V-02 -- Axis: Per-Artifact Inline Write Gates (C-19 target)

**Hypothesis**: Placing a write gate immediately after each artifact production instruction --
collocated in the prompt before the next phase begins -- causes C-19 to be earned. The R3 V-05
failure pattern was using an end-of-skill completion table (which satisfies C-11, not C-19).
C-19 requires the gate to fire at the point of production. Three gates: one after Phase 1,
one after Phase 2, one after Phase 3 -- each triggering an immediate write if the artifact
is missing BEFORE the next phase begins. This is structurally distinct from an end-of-skill check.

```
Run the campaign-specify skill for: {{topic}}

Produce three artifacts in sequence: spec, proposal, pitch. Execute phases 0-3 in order.
Each phase's artifact must exist on disk before the next phase begins.

---

## Phase 0 -- Audience Foundation

Complete all steps before Phase 1. Do not begin Phase 1 until Phase 0 is complete.

**Step 0a -- Inertia Costs**

What each audience LOSES if {{topic}} does not ship:

Exec inertia cost: [Specific business consequence -- revenue, competitive gap, or risk.
Not a category; a specific named consequence.]

Dev inertia cost: [Specific technical friction -- workaround, capability gap, named step.
Not a feeling; the actual manual operation.]

Maker inertia cost: [Specific workflow block -- the step that fails or is absent today.
Not "inefficiency"; the exact missing capability.]

Do not advance to Step 0b until all three costs are named.

**Step 0b -- Voice Contracts**

One sentence per audience, grounded in the inertia costs above:

Exec voice: [Outcomes/risk framing]
Dev voice: [Capability/friction framing]
Maker voice: [Workflow framing -- plain language, no jargon]

**Step 0c -- Do Nothing Stability**

Is the Do Nothing cost stable or worsening over time?

Stability: [Choose: "stable" or "worsening." If worsening, name the mechanism and timeline.]

**Step 0d -- Scout Pull**

Glob `simulations/scout/**/*.md` for {{topic}}. List files found and relevance by artifact.

---

## Phase 1 -- Technical Spec

Pull from `simulations/scout/` broadly. Note files used.

Write the spec. The spec must contain all six sections below. Do not skip or merge.

### Overview
One paragraph: what the feature does and why it exists.

### User Problem
Problem users face today. Reference dev and maker inertia costs from Step 0a.

### Proposed Solution
What {{topic}} does. Incorporate scout-requirements or scout-feasibility signals from Step 0d.

### Constraints
At least three: technical, scope, platform.

### Open Questions
At least three named ambiguities.

### Self-Review
At least one named gap. "No gaps found" fails.

**>> PHASE 1 WRITE GATE <<**
Save spec to: `simulations/draft/specs/{{topic}}-spec-{{date}}.md`
Confirm the file was written before proceeding to Phase 2.
If the spec file does not exist after writing: write it again now.
Do not begin Phase 2 until `simulations/draft/specs/{{topic}}-spec-{{date}}.md` exists on disk.

---

## Phase 2 -- Business Proposal

Pull from `simulations/scout/scout-feasibility/` before writing. Note files used.

Write the proposal with at least three options. Option 1 MUST be named **Do Nothing**.

For each option: description, pros, cons, risk, effort.

**Recommendation** section:

We recommend [chosen option].

**Defeating Do Nothing**: Do Nothing perpetuates [cite specific inertia cost from Step 0a --
name audience and cost]. [Add one sentence on stability from Step 0c: whether the cost is
stable or growing]. We choose to act because [specific rationale tied to the options analysis].

**Defeating [other option]**: We prefer [chosen] over [other] because [specific trade-off
traceable to risk or effort in the options analysis -- not a preference statement].

Do Nothing must be named and defeated by a specific cost. Implicit defeat fails.

**>> PHASE 2 WRITE GATE <<**
Save proposal to: `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md`
Confirm the file was written before proceeding to Phase 3.
If the proposal file does not exist after writing: write it again now.
Do not begin Phase 3 until `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md` exists on disk.

---

## Phase 3 -- Executive Pitch

Pull from `simulations/scout/scout-positioning/` before writing. Note files used.

Write the pitch with four sections:

### Exec Version
Lead with exec inertia cost from Step 0a. Structure:
[exec cost hook] -> [what changes] -> [business outcome/ROI] -> [call to action].

### Dev Version
Lead with dev inertia cost from Step 0a. Structure:
[friction hook] -> [what you can now do] -> [capability unlocked] -> [call to action].

### Maker Version
Lead with maker inertia cost from Step 0a. Plain language, no jargon. Structure:
[blocked step hook] -> [what you can now do] -> [why it matters] -> [call to action].

### Anti-Positioning
3-5 "This is not..." statements. Separate from the three audience versions.

**>> PHASE 3 WRITE GATE <<**
Save pitch to: `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`
Confirm the file was written before stopping.
If the pitch file does not exist after writing: write it again now.
Do not emit a completion summary until `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md` exists on disk.

---

## Completion Index

All three files confirmed. Final output:
- Spec: `simulations/draft/specs/{{topic}}-spec-{{date}}.md` -- exists
- Proposal: `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md` -- exists
- Pitch: `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md` -- exists
- Scout files used per phase
- Phase 0 inertia costs confirmed (all three audiences named)
- Do Nothing defeated by name with specific cost citation
```

**Rubric targeting**:
- C-19: Three inline write gates, each collocated with the artifact production instruction, each firing before the next phase begins. Gate language: "Confirm the file was written before proceeding to Phase N." Not an end-of-skill table -- each gate is at the point of production.
- C-11: Each gate also includes "write it again now" -- active recovery instruction, not passive warning.
- C-16: "Defeating Do Nothing" as labeled separate block in Recommendation.
- C-18: "Do not advance to Step 0b" gate between Phase 0 internal steps.
- All R3 essentials: preserved.

**Risk**: The `>> PHASE N WRITE GATE <<` notation is distinctive but non-standard. A model that treats the gate as a heading rather than a blocking instruction may proceed without actually verifying the file. The gate language uses "Do not begin Phase N+1 until..." which is explicit but relies on the model treating file-check as a mandatory step rather than advisory. The scorer should verify that the file-check instruction is collocated with the production step, not just present somewhere in the skill.

---

## V-03 -- Axis: Voice Differentiation Save Gate (C-20 target)

**Hypothesis**: Adding an explicit "Before saving the pitch" verification block that (1) names
the three opening frames side by side, (2) checks whether any two share the same frame, and (3)
triggers a conditional rewrite if they match -- earns C-20. The R3 variations that attempted
this (V-04: "Voice differentiation check before saving") included the check and a rewrite hint
but lacked the conditional rewrite trigger ("if two or more versions share the same opening
frame, rewrite until distinct before saving"). C-20 requires both the check AND the trigger.
A check without a trigger does not pass. A post-save reminder does not pass.

```
Run the campaign-specify skill for: {{topic}}

Produce three artifacts in sequence: spec, proposal, pitch. Execute phases 0-3 in order.
Phase 0 completes before Phase 1. Each phase writes to disk.

---

## Phase 0 -- Audience Foundation

Before writing anything, complete both steps below.

**Step 0a -- Inertia Costs**

What each audience LOSES if {{topic}} never ships. Concrete and specific.

Exec inertia cost: [Specific revenue, risk, or competitive consequence. Name it.]
Dev inertia cost: [Specific workaround, friction, or capability gap. Name the step.]
Maker inertia cost: [Specific blocked or missing workflow step. Name it.]

Do not advance to Step 0b until all three inertia costs are named.

**Step 0b -- Voice Contracts**

One sentence per audience, grounded in the inertia costs above:

Exec voice: [One sentence -- outcomes/risk framing]
Dev voice: [One sentence -- capability/friction framing]
Maker voice: [One sentence -- workflow framing, plain language]

**Step 0c -- Do Nothing Stability**

Is the Do Nothing cost stable or worsening? Name the trajectory.

Stability: [stable | worsening -- name the mechanism if worsening]

**Step 0d -- Scout Pull**

Glob `simulations/scout/**/*.md` for {{topic}}. List files found.

---

## Phase 1 -- Technical Spec

Pull from `simulations/scout/` broadly. Note files used.

Save to: `simulations/draft/specs/{{topic}}-spec-{{date}}.md`

All six sections required:

### Overview
What the feature does and why it exists (one paragraph).

### User Problem
The problem users face today. Reference dev and maker inertia costs from Step 0a.

### Proposed Solution
What {{topic}} does. Reference scout signals from Step 0d if available.

### Constraints
At least three: technical, scope, platform.

### Open Questions
At least three named ambiguities.

### Self-Review
At least one named gap. "No gaps found" fails.

---

## Phase 2 -- Business Proposal

Pull from `simulations/scout/scout-feasibility/`. Note files used.

Save to: `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md`

Three options minimum. Option 1 MUST be named **Do Nothing**.

For each option: description, pros, cons, risk, effort.

**Recommendation**:

We recommend [chosen option].

**Defeating Do Nothing**: Do Nothing perpetuates [cite inertia cost from Step 0a -- specific
audience and cost]. [One sentence on stability from Step 0c.] We choose to act because
[rationale traceable to options analysis].

**Defeating [other option]**: We prefer [chosen] over [other] because [specific trade-off
from options analysis -- not a preference statement].

---

## Phase 3 -- Executive Pitch

Pull from `simulations/scout/scout-positioning/`. Note files used.

Draft all three audience versions before saving. Do not save the pitch file until the
voice differentiation check below passes.

### Exec Version
Lead with exec inertia cost from Step 0a. Structure:
[exec cost hook] -> [what changes] -> [business outcome/ROI] -> [call to action].

### Dev Version
Lead with dev inertia cost from Step 0a. Structure:
[friction hook] -> [what you can now do] -> [capability unlocked] -> [call to action].

### Maker Version
Lead with maker inertia cost from Step 0a. Plain language, no jargon. Structure:
[blocked step hook] -> [what you can now do] -> [why it matters] -> [call to action].

### Anti-Positioning
3-5 "This is not..." statements. Separate from the three versions above.

**>> VOICE DIFFERENTIATION CHECK (required before saving) <<**

Before saving the pitch file, extract the opening sentence from each version:

Exec opening: [first sentence of Exec Version]
Dev opening: [first sentence of Dev Version]
Maker opening: [first sentence of Maker Version]

Differentiation test: Do any two versions share the same opening frame? (Same subject,
same first claim, or same lead phrase counts as shared.)

If YES (two or more openings are the same or nearly the same):
  Rewrite the duplicated version(s) until all three openings are detectably distinct.
  Exec must lead with business cost. Dev must lead with tool friction. Maker must lead
  with workflow step. Repeat the check after rewriting.
  Do not save the pitch until all three openings are distinct.

If NO (all three openings are distinct): proceed to save.

Save pitch to: `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`
[Save only after the check passes -- not before.]

---

## Completion Check

After all three artifacts:

1. Spec exists at: `simulations/draft/specs/{{topic}}-spec-{{date}}.md` -- if missing: write now.
2. Proposal exists at: `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md` -- if missing: write now.
3. Pitch exists at: `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md` -- if missing: write now.

Do not stop until all three files exist. A warning is not a substitute for writing.

Final index: artifact paths, scout files per phase, Step 0a inertia costs confirmed,
voice differentiation check result (distinct / rewritten-to-distinct), Do Nothing defeated by name.
```

**Rubric targeting**:
- C-20: "VOICE DIFFERENTIATION CHECK (required before saving)" is explicit; check extracts opening sentences side-by-side; conditional trigger: "If YES: rewrite... Do not save until all three openings are distinct." Both check and rewrite condition present. Save instruction collocated after the check passes.
- C-16: "Defeating Do Nothing" as labeled structural block separate from "Defeating [other option]."
- C-18: "Do not advance to Step 0b" intra-Phase 0 gate.
- C-11: Completion check with "write now" active gate per artifact.
- All R3 essentials: preserved.

**Risk**: The voice differentiation check fires as a blocking instruction, but a model may extract
openings that are superficially different while sharing the same conceptual frame (e.g., both exec
and dev opening with "Today, [audience] struggles with..."). The check's "Same subject, same first
claim, or same lead phrase counts as shared" disambiguation helps but requires model judgment.
The scorer should verify the extracted openings are inspected, not just the label "distinct."

---

## V-04 -- Combined: Stability Trajectory + Per-Artifact Inline Gates + Named Defeat Block
## (C-17 + C-19 + C-16)

**Hypothesis**: Combining the C-17 mechanism (stability assessment in Phase 0 + required Phase 2
citation), the C-19 mechanism (three inline write gates collocated at production points), and the
C-16 mechanism (labeled "Defeating Do Nothing" block) in a single variation earns all three
simultaneously while preserving the C-18 intra-Phase 0 gates from R3 V-01. This is the most
targeted combination: three new criteria, each with its own independent mechanism, with low
risk of interaction failure.

```
Run the campaign-specify skill for: {{topic}}

Produce three artifacts in sequence: spec, proposal, pitch. Execute phases 0-3 in order.
Phase 0 must complete before Phase 1. Each artifact is written to disk before the next phase.

---

## Phase 0 -- Audience Foundation

Complete all five steps in sequence. Each step has an advancement gate.

**Step 0a -- Inertia Costs**

What each audience LOSES if {{topic}} does not ship. Concrete and specific:

Exec inertia cost: [Specific revenue exposure, competitive gap, or risk. Name the consequence.]
Dev inertia cost: [Specific workaround or capability gap. Name the friction, not the feeling.]
Maker inertia cost: [Specific blocked workflow step. Name the step.]

Do not advance to Step 0b until all three inertia costs are named.

**Step 0b -- Do Nothing Stability Assessment**

Evaluate whether the cost of Do Nothing is stable or worsening. This assessment is a
named output -- it will be cited verbatim in Phase 2.

Stability assessment: [Required form: "Do Nothing is not stable: [specific mechanism --
e.g., 'the exec exposure grows as competitors ship quarterly', 'dev workaround accumulates
3-5 hours per sprint', 'maker volume increases making the blocked step more costly']."
OR if stable: "Do Nothing is stable: [rationale for why the cost will not compound]."]

Timeline: [If worsening: "Becomes acute by [specific trigger or time window]."
If stable: "Remains at current cost level indefinitely."]

Do not advance to Step 0c until the stability assessment is complete.

**Step 0c -- Voice Contracts**

One sentence per audience, grounded in Step 0a and Step 0b:

Exec voice: [Outcomes/risk framing -- reference the exec inertia cost]
Dev voice: [Capability/friction framing -- reference the dev inertia cost]
Maker voice: [Workflow framing -- plain language, reference the maker inertia cost]

Do not advance to Step 0d until all three voice contracts are written.

**Step 0d -- Scout Pull**

Glob `simulations/scout/**/*.md` for {{topic}}. For each file found:
- Path
- One sentence summary
- Which artifact it serves (spec / proposal / pitch)

**Step 0e -- Do Nothing Baseline**

Compile for use in Phase 2:
Do Nothing absorbs: Exec: [Step 0a cost] / Dev: [Step 0a cost] / Maker: [Step 0a cost]
Stability: [Step 0b assessment -- copy verbatim]

---

## Phase 1 -- Technical Spec

Pull from `simulations/scout/` broadly. Note files from Step 0d that were used.

Write the spec. All six sections required -- no skipping, no merging.

### Overview
One paragraph: what the feature does and why it exists.

### User Problem
The problem users face today. Reference dev and maker inertia costs from Step 0a directly.

### Proposed Solution
What {{topic}} does. Incorporate scout-requirements or scout-feasibility signals from Step 0d.

### Constraints
At least three: technical, scope, platform.

### Open Questions
At least three named ambiguities.

### Self-Review
At least one named gap. "No gaps found" fails.

**>> SPEC WRITE GATE <<**
Save spec to: `simulations/draft/specs/{{topic}}-spec-{{date}}.md`
Check: does the file exist? If not: write it now.
Do not begin Phase 2 until this file exists on disk.

---

## Phase 2 -- Business Proposal

Pull from `simulations/scout/scout-feasibility/` before writing. Note files used.

Write the proposal. Three options minimum. Option 1 MUST be named **Do Nothing**.

For each option: description, pros, cons, risk, effort.

Then write the **Recommendation** section with the following labeled blocks:

---

### Recommendation

We recommend [chosen option].

#### Defeating Do Nothing

[Named block -- structurally separate from the comparative defeat below.]

Do Nothing perpetuates [cite the most decisive Step 0a inertia cost -- name the audience
and the specific cost]. [Cite Step 0b stability assessment verbatim: paste the assessment
from Step 0b here.] We choose to act because [one sentence on why this cost trajectory
is not acceptable].

#### Defeating [Other Option Name]

We prefer [chosen] over [other] because [specific trade-off traceable to risk, effort, or
cons in the options analysis above -- not a preference statement].

---

The "Defeating Do Nothing" block must:
(a) carry a labeled header (not inline text in a combined paragraph)
(b) cite the Step 0b stability assessment verbatim
(c) name the specific audience cost from Step 0a

A combined recommendation paragraph that defeats all options in prose does not satisfy C-16.
A block without the Step 0b stability citation does not satisfy C-17.

**>> PROPOSAL WRITE GATE <<**
Save proposal to: `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md`
Check: does the file exist? If not: write it now.
Do not begin Phase 3 until this file exists on disk.

---

## Phase 3 -- Executive Pitch

Pull from `simulations/scout/scout-positioning/` before writing. Note files used.

Write the pitch with four sections:

### Exec Version
Lead with exec inertia cost from Step 0a. Opening hook = the exec cost.
Structure: [exec cost hook] -> [what changes] -> [outcome/ROI] -> [call to action].

### Dev Version
Lead with dev inertia cost from Step 0a. Opening hook = the friction.
Structure: [friction hook] -> [what you can now do] -> [capability unlocked] -> [call to action].

### Maker Version
Lead with maker inertia cost from Step 0a. Plain language, no jargon.
Opening hook = the blocked step. Structure: [blocked step hook] -> [what you can now do]
-> [why it matters] -> [call to action].

### Anti-Positioning
3-5 "This is not..." statements. Separate from the three audience versions above.

**>> PITCH WRITE GATE <<**
Save pitch to: `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`
Check: does the file exist? If not: write it now.
Do not emit a completion summary until this file exists on disk.

---

## Completion Index

Final index:
1. Spec: `simulations/draft/specs/{{topic}}-spec-{{date}}.md` -- confirmed
2. Proposal: `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md` -- confirmed
3. Pitch: `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md` -- confirmed
4. Scout files used by phase (from Step 0d routing)
5. Step 0a inertia costs: all three audiences named
6. Step 0b stability assessment: [stable | worsening] -- state which
7. Step 0b cited verbatim in Defeating Do Nothing block: yes/no
8. Do Nothing defeated by named labeled block: yes/no
```

**Rubric targeting**:
- C-16: "Defeating Do Nothing" block has its own `####` header, structurally separate from "Defeating [Other Option Name]" block. Combined paragraph does not satisfy -- explicit disqualification.
- C-17: Step 0b produces a named stability assessment; Phase 2 defeat block requires verbatim citation. Two-location requirement met by construction (Step 0b establishes, Phase 2 cites). Final index item 7 confirms citation occurred.
- C-18: Three "Do not advance" gates within Phase 0 (Steps 0a->0b, 0b->0c, 0c->0d).
- C-19: Three write gates, each collocated with artifact production, each firing before the next phase begins. Not an end-of-skill table.
- C-15: "Defeating Do Nothing" block cites specific inertia cost + "We choose to act because" rationale.

**Risk**: The Step 0b verbatim citation requirement creates a copy-paste risk -- a model may paste
a placeholder rather than the actual content. The final index item 7 ("cited verbatim: yes/no")
helps the scorer detect this. The three-layer Phase 0 gate sequence (0a->0b, 0b->0c, 0c->0d)
is longer than R3 -- under context pressure the model may merge steps. Each gate uses explicit
"do not advance" language which is the strongest available instruction.

---

## V-05 -- Full Synthesis: All Five New Criteria (C-16 + C-17 + C-18 + C-19 + C-20)

**Hypothesis**: A single variation that architects five independent mechanisms for the five new
criteria -- each with its own structural enforcement point -- earns all 12 aspirational criteria
simultaneously. The five mechanisms are:
- C-16: Named labeled "Defeating Do Nothing" block (distinct from comparative defeat)
- C-17: Phase 0 stability assessment + required verbatim citation in Phase 2 defeat block
- C-18: Explicit "do not advance" gates between Phase 0 internal steps
- C-19: Three inline write gates, each collocated with the production instruction, before the next phase
- C-20: Pre-save voice differentiation check + conditional rewrite trigger before pitch file is saved

Each mechanism is independent -- failure of one does not cascade to others.
This is the R4 target ceiling: 12/12 aspirational = 100.0 composite.

```
Run the campaign-specify skill for: {{topic}}

Produce three artifacts: spec, proposal, pitch. Execute phases 0-3 in order.
Phase 0 must complete in full before Phase 1 begins. Each artifact is written
to disk before the next phase begins.

---

## Phase 0 -- Audience Foundation (complete in full before Phase 1)

Five steps in sequence. Each step has an explicit advancement gate.

**Step 0a -- Inertia Costs (loss-first)**

Name what each audience LOSES if {{topic}} does not ship.
Concrete and audience-specific. Generic claims fail this step.

Exec inertia cost: [Specific revenue exposure, competitive gap, or risk. Name a consequence,
not a category. Quantify if possible ("$X quarterly" or "N% of pipeline").]

Dev inertia cost: [Specific workaround, manual step, or capability gap. Name the friction,
not the feeling. Estimate the recurring cost if possible ("3-5 hours per sprint").]

Maker inertia cost: [Specific blocked or missing workflow step. Name the step. What
does the maker do today instead, and why is that worse?]

Do not advance to Step 0b until all three inertia costs are complete.

**Step 0b -- Do Nothing Stability Assessment**

Is the Do Nothing cost stable or worsening? This is a named output cited in Phase 2.
Answer the stability question now, before the proposal is written.

Stability assessment: [Required -- choose one form and complete it:]
  FORM A (worsening): "Do Nothing is not stable: [specific mechanism and timeline --
  e.g., 'competitor ships equivalent feature in Q2, making exec exposure acute by
  June', or 'dev workaround accumulates 3 hours/sprint, compounding to 36h/quarter']."
  FORM B (stable): "Do Nothing is stable: [rationale -- e.g., 'the workaround is
  functional and the underlying need does not grow with volume']."

Note: a stability assessment without a mechanism or timeline fails C-17.

Do not advance to Step 0c until the stability assessment is complete.

**Step 0c -- Voice Contracts**

One sentence per audience, grounded in the inertia costs and stability assessment above.
Voice contracts anchor Phase 3 pitch openings -- write them precisely.

Exec voice: [One sentence -- outcomes/risk framing. Lead with the exec cost or its trajectory.]
Dev voice: [One sentence -- capability/friction framing. Lead with the friction or its recurrence.]
Maker voice: [One sentence -- workflow framing. Plain language. Lead with the blocked step.]

Do not advance to Step 0d until all three voice contracts are written.

**Step 0d -- Scout Pull**

Glob `simulations/scout/**/*.md` for {{topic}}. For each file found:
- Path
- Signal summary (one sentence)
- Artifact it serves: spec / proposal / pitch

If no scout files found: record "no scout signals -- proceeding without" and continue.

**Step 0e -- Do Nothing Baseline (pre-compile for Phase 2)**

Compile for direct use in the Phase 2 Recommendation block. Copy outputs from above:

Do Nothing absorbs:
  Exec: [Step 0a exec cost]
  Dev: [Step 0a dev cost]
  Maker: [Step 0a maker cost]
  Stability: [Step 0b assessment -- paste the full form-A or form-B text verbatim]

---

## Phase 1 -- Technical Spec

Pull from `simulations/scout/` broadly. Note which Step 0d files were used.

Write the spec. All six sections are required. Do not skip or merge any section.

### Overview
One paragraph: what {{topic}} does and why it exists.

### User Problem
The problem users face today. Open with or reference the dev and maker inertia costs
from Step 0a -- these are evidence of the problem, not invented examples.

### Proposed Solution
What {{topic}} does. Incorporate scout-requirements or scout-feasibility signals
from Step 0d if available.

### Constraints
At least three constraints: technical, scope, platform.

### Open Questions
At least three named ambiguities.

### Self-Review
At least one named gap. Which section needs more work and why?
"No gaps found" fails this section.

**>> SPEC WRITE GATE <<**
Write spec to: `simulations/draft/specs/{{topic}}-spec-{{date}}.md`
After writing: confirm the file exists.
If the file does not exist: write it now before continuing.
Do not begin Phase 2 until `simulations/draft/specs/{{topic}}-spec-{{date}}.md` is on disk.

---

## Phase 2 -- Business Proposal

Pull from `simulations/scout/scout-feasibility/` before writing. Note files used.

Write the proposal. Minimum three options. Option 1 MUST be named **Do Nothing**.

For each option: description, pros, cons, risk, effort.

Then write the **Recommendation** section. This section has two labeled blocks.
Each block is a separate `####` header -- do not merge them into a combined paragraph.

### Recommendation

We recommend [chosen option].

#### Defeating Do Nothing

[This block addresses the status quo competitor. It is structurally separate from
the comparative defeat below.]

Do Nothing perpetuates [cite the most decisive inertia cost from Step 0a -- name the
audience and the specific cost]. [Paste the Step 0e stability line here verbatim:
"Do Nothing is not stable: [mechanism]" or "Do Nothing is stable: [rationale]".]
We choose to act because [one sentence: why this cost is not acceptable given the
trajectory stated above].

#### Defeating [Other Option Name]

We prefer [chosen option] over [other option] because [specific trade-off traceable to
a risk, effort, or cons field in the options analysis -- not a preference statement].

[If there are additional rejected options, add a block for each: #### Defeating [Name].]

Note on structure:
- The "Defeating Do Nothing" block must have its own labeled header.
- The Step 0e stability line must appear verbatim inside that block.
- A recommendation paragraph that combines Do Nothing defeat with other comparisons
  in prose does not satisfy C-16 or C-17.

**>> PROPOSAL WRITE GATE <<**
Write proposal to: `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md`
After writing: confirm the file exists.
If the file does not exist: write it now before continuing.
Do not begin Phase 3 until `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md` is on disk.

---

## Phase 3 -- Executive Pitch

Pull from `simulations/scout/scout-positioning/` before writing. Note files used.

Write all four sections of the pitch below. Do not save the pitch file until the
voice differentiation check at the end of this phase passes.

### Exec Version
Lead with the exec inertia cost from Step 0a. Use the Step 0c exec voice contract as
your anchor. Opening = the business cost that exists today.
Structure: [exec cost hook] -> [what changes with {{topic}}] -> [business outcome/ROI]
-> [call to action]. Do not open with a product description.

### Dev Version
Lead with the dev inertia cost from Step 0a. Use the Step 0c dev voice contract as
your anchor. Opening = the friction that exists today.
Structure: [friction hook] -> [what you can now do] -> [capability unlocked] ->
[call to action]. Do not open with an outcomes/ROI frame.

### Maker Version
Lead with the maker inertia cost from Step 0a. Use the Step 0c maker voice contract
as your anchor. Opening = the blocked step that exists today. Plain language, no jargon.
Structure: [blocked step hook] -> [what you can now do] -> [why it matters] ->
[call to action]. Test: readable without the spec by a non-technical user.

### Anti-Positioning
3-5 "This is not..." statements. This section is structurally separate from the three
audience versions above.

**>> VOICE DIFFERENTIATION GATE (required before saving pitch) <<**

Before saving the pitch file, perform this check:

Extract the opening sentence from each audience version:
  Exec opening: [first sentence of Exec Version]
  Dev opening: [first sentence of Dev Version]
  Maker opening: [first sentence of Maker Version]

Differentiation check: Do any two openings share the same frame?
(Same subject, same lead claim, or same opening phrase = same frame.)

Expected pattern:
  Exec opens with: a business cost, risk, or revenue consequence
  Dev opens with: a tool friction, workaround, or capability gap
  Maker opens with: a workflow step that is blocked, absent, or manual

IF any two openings are the same or use the same frame:
  Rewrite the duplicated version(s) until all three openings are detectably distinct.
  Re-run this check after rewriting.
  Do not save the pitch until all three opening frames are distinct.

IF all three openings are distinct: proceed.

**>> PITCH WRITE GATE <<**
[Save only after the voice differentiation gate above passes.]
Write pitch to: `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`
After writing: confirm the file exists.
If the file does not exist: write it now before stopping.
Do not emit a completion summary until `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md` is on disk.

---

## Completion Index

Confirm all artifacts exist. Then output:

| Item | Value |
|------|-------|
| Spec path | `simulations/draft/specs/{{topic}}-spec-{{date}}.md` |
| Proposal path | `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md` |
| Pitch path | `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md` |
| Scout files used (spec phase) | [list] |
| Scout files used (proposal phase) | [list] |
| Scout files used (pitch phase) | [list] |
| Step 0a inertia costs confirmed | exec: yes / dev: yes / maker: yes |
| Step 0b stability | [stable / not stable] |
| Step 0b cited in Defeating Do Nothing | yes / no |
| Defeating Do Nothing block: separate labeled header | yes / no |
| Voice differentiation gate result | distinct / rewritten-to-distinct |
```

**Rubric targeting**:
- C-01: Three artifacts + three inline write gates + end-of-skill completion index
- C-02: Six sections, all named, no-skip rule
- C-03: Three options, Do Nothing as Option 1, recommendation with rationale
- C-04: Exec/dev/maker versions + Anti-Positioning as separate section
- C-05: Step 0a inertia costs flow into spec (User Problem), proposal (Do Nothing defeat), and pitch (opening hooks) -- consistent by Step 0e pre-compile reference
- C-06: Self-review with at least one named gap
- C-07: Anti-Positioning as explicit named section in Phase 3
- C-08: "Defeating [Other Option]" block cites specific options analysis field -- traceable
- C-09: Step 0d scout pull, per-phase targeted re-queries in Phases 1-3
- C-10: Phase 0c voice contracts anchor pitch openings; differentiation gate verifies distinct frames
- C-11: Each write gate includes "write it now" active recovery; not passive
- C-12: Phase 0 (five steps) precedes Phase 1; voice contracts defined at Step 0c
- C-13: Phase 0d -> Phase 1 (scout/ broad) -> Phase 2 (scout-feasibility) -> Phase 3 (scout-positioning)
- C-14: Step 0a requires concrete named costs per audience with specificity instruction
- C-15: Defeating Do Nothing block names Do Nothing + cites specific cost + explicit "We choose to act because"
- C-16: "Defeating Do Nothing" block has its own `####` header, structurally separate from "Defeating [Other Option]"; combined paragraph explicitly disqualified
- C-17: Step 0b produces named stability assessment with required form (Form A / Form B); Phase 2 "paste the Step 0e stability line here verbatim" enforces two-location requirement; mechanism+timeline required for Form A
- C-18: Three "Do not advance" gates within Phase 0 (after Steps 0a, 0b, 0c); all use "do not advance to Step N+1 until" form
- C-19: Three write gates (SPEC WRITE GATE, PROPOSAL WRITE GATE, PITCH WRITE GATE), each collocated with the artifact production instruction, each with "do not begin Phase N+1 until file exists" blocking language; structurally distinct from the end-of-skill Completion Index
- C-20: VOICE DIFFERENTIATION GATE appears before pitch save; extracts opening sentences side by side; conditional trigger: "IF any two openings share the same frame: rewrite... Do not save until all three opening frames are distinct"; save instruction follows gate result

**Risk**: This is the most complex variation. Five independent mechanisms increase total prompt
length. Context pressure risk is highest here. Mitigation: each mechanism is self-contained --
failure of C-20 (voice gate) does not affect C-19 (inline write gates), and failure of C-17
(stability citation) does not affect C-18 (intra-Phase 0 gates). The Completion Index table
functions as both a summary and a self-scoring instrument -- a model that fills it honestly
will expose any criterion it missed.

---

## Variation Summary

| ID | Primary Axis | Key Mechanism | Targets | Predicted Score (v4) | Risk |
|----|--------------|---------------|---------|----------------------|------|
| V-01 | Stability trajectory | Step 0b named assessment + Phase 2 verbatim citation | C-17, C-18 | 98.3 | Verbatim citation may be placeholder; scorer must check specificity |
| V-02 | Per-artifact inline gates | Three >> WRITE GATE << blocks, each collocated at production, each with "do not begin Phase N+1" | C-19, C-18, C-11 | 97.5 | Gate language may be treated as advisory; scorer must check collocation |
| V-03 | Voice save gate | Pre-save extraction + conditional rewrite trigger before pitch file saved | C-20, C-18 | 97.5 | Frame comparison may accept superficially different but conceptually same openings |
| V-04 | Stability + inline gates + named block | Step 0b verbatim cite + inline write gates + labeled Defeating Do Nothing block | C-16, C-17, C-18, C-19 | 99.2 | Step 0b verbatim copy risk; gate blocking may not be enforced |
| V-05 | Full synthesis | Five independent mechanisms for C-16 through C-20, with Completion Index self-scoring | C-16, C-17, C-18, C-19, C-20 | 100.0 | Complexity/length; each mechanism self-contained so failure does not cascade |

**Predicted leaderboard**: V-05 > V-04 > V-01 >= V-02 = V-03

V-05 targets all five new criteria with independent mechanisms. V-04 hits four of five (misses C-20).
V-01 and V-02 target their respective single criteria cleanly. V-03 targets C-20 but is otherwise
equivalent to V-01/V-02 in structure.

The critical unlock from R4: no R3 variation earned C-19 and C-20 simultaneously. V-05 is the
first variation to place both the per-artifact inline gates (C-19) and the voice save gate (C-20)
in the same prompt. These two criteria target different structural locations (production points
vs. pitch save) and do not interfere -- stacking them should earn both without trade-offs.
