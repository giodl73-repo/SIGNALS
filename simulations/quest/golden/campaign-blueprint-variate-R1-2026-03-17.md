---
skill: quest-variate
skill_target: campaign-blueprint
date: 2026-03-17
round: 1
rubric: campaign-blueprint-rubric-v1-2026-03-17.md
---

# campaign-blueprint Variations — Round 1

Five complete, runnable skill body variations. Single-axis first (V-01 through V-03),
then two combinations (V-04, V-05).

## R1 Context

This is Round 1 against rubric v1-2026-03-17. The rubric defines 5 essential criteria
(C-01 through C-05), 3 recommended (C-06 through C-08), and 2 aspirational (C-09, C-10).

Baseline skill: orchestrate draft-spec -> draft-proposal -> draft-pitch in sequence.
Stock roles: Architect (spec), Architect+PM (proposal), PM+Strategy (pitch).

## Variation Axes

| Axis | Label | Hypothesis |
|------|-------|-----------|
| A | Inertia-first framing | Opening with an explicit Inertia Baseline characterization before any artifact authoring forces all three artifacts to anchor to the status quo (C-06) and sharpens the proposal do-nothing option (C-03) |
| B | Contract matrix first | Printing the READ/WRITE/PRESERVE/CARRIES FORWARD table before Artifact 1 makes the dependency chain auditable (C-09) and prevents cross-artifact contradiction (C-05) |
| C | PM-first role sequence | PM leads all three artifacts; Architect advises on spec, Strategy advises on pitch. Improves inertia framing and audience resonance (C-06, C-04); risk: spec technical depth (C-02) depends on PM explicitly requesting architectural input |
| D | Conversational register | Question-driven framing surfaces gaps naturally (C-08), makes inertia concrete, risks missing required structural sections if questions are not comprehensive |
| E | Full combination | Axes A + B + C + mandatory scout scan gate: maximizes composite score across all rubric bands |

---

## V-01 — Axis A: Inertia-First Framing

**Variation axis**: Inertia framing
**Hypothesis**: Opening with an explicit Inertia Baseline before any artifact authoring forces all
three artifacts to anchor to what users do today (C-06), sharpens the do-nothing option (C-03),
and makes the pitch "why it matters" section specific rather than generic.

---

You are running the `campaign-blueprint` skill for topic: {{topic}}.

This skill produces a complete specification package: technical spec, business proposal, and
executive pitch. The three artifacts are written in sequence. Each artifact reads its predecessor.

**Before writing Artifact 1, establish the Inertia Baseline.**

### Step 0 — Inertia Baseline

State what users do today without this feature. Be specific. Name the tools, workarounds, manual
steps, or rituals they use instead. Identify the cost: time lost, errors introduced, decisions
delayed, or capability absent. This baseline is the primary competitor. It appears in every artifact.

Format:

```
INERTIA BASELINE — {{topic}}
Today users: [describe current behavior]
Cost of inertia: [quantify or characterize the pain]
Do-nothing trajectory: [what gets worse if nothing ships]
```

This baseline carries forward into all three artifacts. Do not re-derive it. Reference it by name.

---

### Artifact 1 — Technical Specification

**Role**: Architect
**Writes to**: `simulations/draft/specs/{{topic}}-spec-{{date}}.md`
**Reads**: Inertia Baseline. Scout signals at `simulations/scout/**/*{{topic}}*` if present.

Write the specification with these five sections:

**PURPOSE** — State what the feature does and why it is needed now. Open with a single sentence
that references the inertia baseline: what pain does this resolve that users currently absorb?

**REQUIREMENTS** — MoSCoW-tagged list. Must-have (M) items are the minimum for the inertia
baseline to be resolved. Should-have (S) items improve quality. Could-have (C) items are deferred.
Won't-have (W) items are explicitly ruled out. At least three M items required.

**DESIGN** — Describe the proposed technical approach. Reference any scout-requirements or
scout-feasibility signals if found. State what this approach does not include.

**CONSTRAINTS** — List technical, platform, timeline, and resource constraints. Be specific. Generic
constraints are not acceptable — name actual limits.

**OPEN QUESTIONS** — Self-review output. After drafting the above, identify at least two specific
gaps or ambiguities that remain unresolved. At least one must reference a missing signal (e.g.,
"need scout-feasibility to confirm effort for Option B"). Do not use boilerplate language.

End the spec with: `SPEC COMPLETE — {count} open questions flagged.`

---

### Artifact 2 — Proposal / ADR

**Role**: Architect (technical options) + PM (business trade-offs)
**Writes to**: `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md`
**Reads**: Artifact 1 (spec). Uses spec REQUIREMENTS to bound option scope. Uses spec CONSTRAINTS
as the feasibility ceiling.

Write the proposal with at least three options. **Option A must be the do-nothing / status-quo option.**

For each option:
- **Description** — what is being proposed
- **Pros** — at least two, specific to this topic
- **Cons** — at least two, specific to this topic
- **Effort** — S/M/L/XL
- **Risk** — Low/Medium/High with one-line reason
- **Inertia impact** — how does this option change the inertia baseline? Option A must explicitly
  state what inertia costs continue or worsen under the do-nothing scenario.

**RECOMMENDATION** — Name the chosen option. State why it is preferred over the alternatives.
The rationale must reference the spec's stated constraints and at least one M-tier requirement.

End with: `PROPOSAL COMPLETE — Option [X] recommended.`

---

### Artifact 3 — Pitch

**Role**: PM + Strategy
**Writes to**: `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`
**Reads**: Artifact 2 (proposal). Opens with the recommended option from the proposal by name.
Uses the inertia baseline in the "why it matters" section of each audience version.

Write three audience versions: **Exec**, **Developer**, **Maker**.

Each version must contain:
- **Hook** — one sentence that lands the problem
- **What it does** — two to three sentences, audience-appropriate vocabulary
- **Why it matters** — reference the inertia baseline; state what changes for this audience
- **Call to action** — concrete next step for this audience

Audience framing:
- Exec: outcome-first, ROI framing, no implementation detail
- Developer: show the tool, what changes in their workflow, specific capability
- Maker: jargon-free, "can I do this?" framing

**Anti-Positioning** — After the three versions, write a section titled "What this is NOT."
List at least two specific exclusion statements. Each must rule out an adjacent or commonly
confused use case by name.

End with: `PITCH COMPLETE — 3 audience versions + anti-positioning written.`

---

### Completion Check

```
CAMPAIGN COMPLETE
Spec:     simulations/draft/specs/{{topic}}-spec-{{date}}.md
Proposal: simulations/draft/proposals/{{topic}}-proposal-{{date}}.md
Pitch:    simulations/draft/pitches/{{topic}}-pitch-{{date}}.md
Open questions: [count from spec]
Recommended option: [from proposal]
Inertia baseline anchored in: spec PURPOSE / proposal Option A / pitch "why it matters"
```

---

## V-02 — Axis B: Contract Matrix First

**Variation axis**: Output format — artifact contract matrix declared before execution
**Hypothesis**: Printing the full READ/WRITE/PRESERVE/CARRIES FORWARD table before Artifact 1
begins makes the dependency chain auditable (C-09), forces the author to reason about
cross-artifact consistency before writing (C-05), and produces a structured log easier to score.

---

You are running the `campaign-blueprint` skill for topic: {{topic}}.

This skill produces three artifacts in sequence: spec -> proposal -> pitch. Before writing any
artifact, declare the artifact contract matrix.

### Contract Matrix

Print this table, completed for {{topic}}, before beginning Artifact 1:

| Artifact | READS | WRITES | PRESERVES | CARRIES FORWARD |
|----------|-------|--------|-----------|-----------------|
| 1 — Spec | Scout signals (if present) at `simulations/scout/**/*{{topic}}*` | `simulations/draft/specs/{{topic}}-spec-{{date}}.md` | Feature name, scope boundary, constraint list | M-tier requirements, design approach, open questions, constraints |
| 2 — Proposal | Spec: feature name, scope, M-requirements, constraints | `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md` | Same feature name and scope as spec | Recommended option name, rationale, do-nothing cost |
| 3 — Pitch | Proposal: recommended option name, rationale. Spec: constraints. | `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md` | Same feature name, same recommended option from proposal | — |

After printing the matrix: "Contract declared. Beginning Artifact 1."

---

### Artifact 1 — Technical Specification

**Role**: Architect
**Writes to**: `simulations/draft/specs/{{topic}}-spec-{{date}}.md`

Required sections:

**PURPOSE** — What the feature does and why it is needed. Include a statement about what users
do today without it.

**REQUIREMENTS** — MoSCoW-tagged. At least three M items. Each M item must be necessary for the
feature to address the stated problem.

**DESIGN** — Technical approach. State what is included and what is explicitly excluded.

**CONSTRAINTS** — Specific, named constraints. Not generic.

**OPEN QUESTIONS** — At least two specific gaps flagged during authoring. At least one must be
an information dependency on a missing signal.

Write the full artifact. End with: `[SPEC WRITTEN]`

---

### Artifact 2 — Proposal / ADR

**Role**: Architect + PM
**Writes to**: `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md`

Dependency check before writing: "Reading spec. Feature name: [X]. Scope: [Y].
Constraints carried forward: [list]."

Required content:
- Three or more options. Option A = do-nothing.
- Each option: description, pros (2+), cons (2+), effort, risk.
- RECOMMENDATION section naming the chosen option with rationale referencing at least one
  M-tier requirement and at least one constraint.

Write the full artifact. End with: `[PROPOSAL WRITTEN — Option X recommended]`

---

### Artifact 3 — Pitch

**Role**: PM + Strategy
**Writes to**: `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`

Dependency check before writing: "Reading proposal. Recommended option: [X].
Reading spec. Constraints: [list]. Confirming no contradictions."

Required content:
- Three audience versions: Exec / Developer / Maker.
- Each version: hook, what it does, why it matters, call to action.
- Versions must be distinct in framing.
- Anti-positioning: at least two "What this is NOT" statements by name.

Write the full artifact. End with: `[PITCH WRITTEN]`

---

### Completion Summary

```
CONTRACT EXECUTED
Artifact 1 — Spec:     [path]  [WRITTEN]
Artifact 2 — Proposal: [path]  [WRITTEN — Option X recommended]
Artifact 3 — Pitch:    [path]  [WRITTEN]
Cross-references: proposal refs spec / pitch refs proposal recommended option
```

---

## V-03 — Axis C: PM-First Role Sequence

**Variation axis**: Role sequence — PM leads all three, Architect and Strategy advise
**Hypothesis**: Leading all three artifacts from a PM / business lens before technical detail
improves inertia framing and audience resonance (C-06, C-04). Risk: spec technical depth (C-02)
depends on PM explicitly requesting architectural input before finalizing DESIGN and CONSTRAINTS.

---

You are running the `campaign-blueprint` skill for topic: {{topic}}.

Produce a complete specification package: spec, proposal, pitch — in that order. The PM role
leads each artifact. Architect and Strategy advise where noted.

---

### Artifact 1 — Technical Specification

**Lead role**: PM (frames problem and requirements from user/business perspective)
**Advisory role**: Architect (reviews DESIGN and CONSTRAINTS before artifact is finalized)
**Writes to**: `simulations/draft/specs/{{topic}}-spec-{{date}}.md`

PM opens by scanning for scout signals: `simulations/scout/**/*{{topic}}*`. If any are found,
list them by name. If none: "No scout signals found. Proceeding from intent."

Write these sections:

**PURPOSE** — PM perspective: what user problem does this solve? What do users do today instead?
Why does this matter to ship now?

**REQUIREMENTS** — PM perspective: what must the feature do for users? MoSCoW-tagged. Must-have
items are what users need for the feature to address their stated pain. At least three M items.

**DESIGN** — PM perspective: describe the intended behavior from the user's point of view.
Then: "Architect review: does this approach work given platform constraints? Flag any technical
impossibilities or required changes." Incorporate architectural notes inline.

**CONSTRAINTS** — Architect perspective: specific technical, platform, timeline, and resource
constraints. PM confirms these are acceptable business constraints.

**OPEN QUESTIONS** — PM + Architect: at least two open questions that require decisions before
the feature can be built. At least one must name a missing signal. At least one must be a design
ambiguity not yet resolved between PM intent and Architect feasibility.

End: `SPEC COMPLETE.`

---

### Artifact 2 — Proposal / ADR

**Lead role**: PM (frames business trade-offs)
**Advisory role**: Architect (effort and risk estimates per option)
**Writes to**: `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md`

PM reads the spec. State: "Spec read. Feature: {{topic}}. M-tier requirements: [list].
Constraints: [list]."

At least three options. **Option A = do-nothing.**

PM frames each option from a business perspective. Architect estimates effort and flags technical
risks. For each option:
- **Description** — what is being proposed from a product/business angle
- **Pros** — business and user value
- **Cons** — business and technical costs
- **Effort** — Architect: S/M/L/XL
- **Risk** — Architect: Low/Medium/High + one-line reason
- **Inertia impact** — PM: how does this option affect the user's current workaround behavior?

**RECOMMENDATION** — PM makes the call, with Architect sign-off on feasibility. State which
option is recommended and why, referencing M-tier requirements from the spec.

End: `PROPOSAL COMPLETE — Option [X] recommended. Architect: feasibility confirmed.`

---

### Artifact 3 — Pitch

**Lead role**: Strategy (per-audience messaging)
**Advisory role**: PM (ensures recommended option is correctly represented)
**Writes to**: `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`

Strategy reads the proposal. State: "Proposal read. Recommended option: [X].
Rationale: [one sentence]."

Three audience versions: **Exec / Developer / Maker.**

Strategy selects framing per audience. PM advisory verifies alignment for each:
- **Exec**: outcome and ROI. PM: does this accurately represent the recommended option's
  business case?
- **Developer**: tool-level, workflow change. PM: does this match what is actually being built?
- **Maker**: accessible, jargon-free. PM: is this honest about the learning curve?

Each version: hook, what it does, why it matters, call to action.

**Anti-Positioning** — Strategy: what is this feature NOT? At least two specific exclusion
statements. Each must name a use case or concept users might confuse with this feature.

End: `PITCH COMPLETE.`

---

### Completion Check

```
CAMPAIGN COMPLETE
Spec:     [path]
Proposal: [path] — [recommended option]
Pitch:    [path]
Scout signals found: [list or "none"]
Role sequence: PM-led / Architect-advised / Strategy-closed
```

---

## V-04 — Axis D: Conversational Register

**Variation axis**: Phrasing register — question-driven, descriptive rather than imperative
**Hypothesis**: Framing each artifact phase as questions to answer surfaces gaps naturally (C-08),
produces more authentic open questions in the spec, and makes inertia framing feel grounded
rather than mechanical — at the risk of missing required structural elements if the questions
are not comprehensive enough to cover all five spec sections.

---

You are running the `campaign-blueprint` skill for topic: {{topic}}.

Your job is to understand the feature well enough to write three artifacts that together make
the case for building it: a spec, a proposal, and a pitch. Work through them in order. Each
one builds on the last.

---

### Before you start

Check whether there are any existing scout signals for this topic. Look in `simulations/scout/`
for files that mention {{topic}}. If you find any, note what they tell you — requirements
research, feasibility concerns, positioning ideas. If there are none, you are starting from intent alone.

---

### Artifact 1 — Technical Specification

Think of the spec as answering: "What are we actually building and why?"

Write `simulations/draft/specs/{{topic}}-spec-{{date}}.md`.

Work through these questions:

**What problem are we solving?** (This becomes the PURPOSE section.) Who has this problem today?
What do they do instead of using this feature? How painful is that workaround?

**What must the feature do?** (This becomes REQUIREMENTS.) Separate must-haves from nice-to-haves
from things that won't be in scope. Tag each item: M (must), S (should), C (could), W (won't).
You need at least three must-haves.

**How would it work?** (This becomes DESIGN.) Describe the approach at a level where someone
could evaluate whether it would actually solve the problem. What does it not include?

**What are the real limits?** (This becomes CONSTRAINTS.) Not aspirational ones — the actual
technical, timing, or resource ceilings that bound what can be built.

**What don't we know yet?** (This becomes OPEN QUESTIONS.) After drafting everything above, what
are the two biggest unresolved questions? At least one should name a specific signal that would
answer it if someone ran it (e.g., scout-feasibility, scout-requirements). These should be
specific to this feature — not generic boilerplate.

---

### Artifact 2 — Proposal / ADR

Think of the proposal as answering: "What are the real options and which one should we pick?"

Write `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md`.

Read the spec first. What are the must-have requirements and the constraints? Those bound your
option space.

What are the options? You need at least three. One of them has to be "we don't build this" —
the do-nothing option. What happens to users if we do nothing? The cost of that inertia should
be explicit, not just implied.

For each option: what it actually is, what goes well, what goes badly, how hard it is to build,
and how risky it is.

Then make a recommendation. Name the option you'd pick and explain why — using the must-have
requirements from the spec as your argument, and acknowledging the strongest objection.

---

### Artifact 3 — Pitch

Think of the pitch as answering: "How do we talk about this to three different audiences?"

Write `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`.

Read the proposal first. Which option did we recommend? That is the feature you are pitching.

Write three versions:

**For an exec**: They want the outcome, not the mechanism. What problem goes away? What becomes
possible? What does inaction cost? What is the ask? Keep it short.

**For a developer**: They want to know what changes in their workflow. Show them the tool. What
can they do that they couldn't before? What does it look like in practice?

**For a maker**: They want to know if this is for them. Skip the jargon. Can they do this? Is
it complicated? What is the one thing it changes for someone in their position?

Each version needs: a hook that lands the problem, what the feature does, why it matters to
that audience specifically, and a clear next step.

Then add a short section: **What this is NOT.** Name at least two things users might assume
this feature does that it actually doesn't. Be specific — name the use case or the thing
you are ruling out.

---

### When you are done

List the three file paths. Note how many open questions are in the spec. Note the recommended
option from the proposal. Confirm that the pitch opens from that recommendation.

---

## V-05 — Combined: Inertia + Contract Matrix + Scout Gate + Role Handoffs

**Variation axes**: A (inertia-first) + B (contract matrix) + C (role sequence) + scout scan gate
**Hypothesis**: The combination of an explicit inertia baseline, a printed artifact contract matrix,
a mandatory scout scan gate with acknowledgment, and explicit named role handoffs between artifacts
produces the highest composite score across all rubric bands — particularly C-05 (sequence
integrity), C-06 (inertia baseline), C-07 (scout integration), and C-09 (contract matrix).

---

You are running the `campaign-blueprint` skill for topic: {{topic}}.

This skill produces three artifacts in strict dependency sequence: spec -> proposal -> pitch.
Follow all phases in order. Do not begin an artifact until the prior phase is complete.

---

### Phase 0 — Pre-Execution Setup

**Step 0a — Scout Gate**

Scan: `simulations/scout/**/*{{topic}}*`

If signals are found, list each by file name and note what it contributes:
- scout-requirements -> feeds REQUIREMENTS section of Artifact 1
- scout-feasibility -> feeds option effort/risk ratings in Artifact 2
- scout-positioning -> feeds per-audience framing in Artifact 3

If no signals are found: "SCOUT GATE: No signals found. All artifacts authored from intent."

**Step 0b — Inertia Baseline**

Before writing any artifact, characterize what users do today without this feature:

```
INERTIA BASELINE
Today:      [specific current behavior — tools, manual steps, workarounds]
Cost:       [time, errors, decisions blocked, capabilities absent]
Trajectory: [what gets worse if this never ships]
```

This baseline is Competitor #1. It is referenced in every artifact. Do not re-derive it.

**Step 0c — Artifact Contract Matrix**

Print this table before beginning Artifact 1:

| # | Artifact | READS | WRITES | PRESERVES | CARRIES FORWARD |
|---|----------|-------|--------|-----------|-----------------|
| 1 | Spec | Scout signals (if found) | `simulations/draft/specs/{{topic}}-spec-{{date}}.md` | Inertia Baseline | Feature name, scope, M-tier requirements, constraints, open questions |
| 2 | Proposal | Artifact 1: feature name, M-reqs, constraints | `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md` | Feature name, scope, inertia baseline | Recommended option name, rationale, do-nothing cost |
| 3 | Pitch | Artifact 2: recommended option, rationale. Artifact 1: constraints. | `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md` | Feature name, recommended option | — |

Print: "Phase 0 complete. Beginning Artifact 1."

---

### Artifact 1 — Technical Specification

**Role**: Architect
**Writes to**: `simulations/draft/specs/{{topic}}-spec-{{date}}.md`

**PURPOSE** — What the feature does and why now. First sentence references the inertia baseline.
If scout-requirements was found, cite it as primary input.

**REQUIREMENTS** — MoSCoW-tagged. At least three M items. M items are requirements whose absence
leaves users on the workaround. If scout-requirements was found, pull requirements from it directly
and cite the file name.

**DESIGN** — Proposed technical approach. What is included. What is explicitly excluded. If
scout-feasibility was found, reference it here.

**CONSTRAINTS** — Specific named constraints (technical, platform, timeline, resource). No generic.

**OPEN QUESTIONS** — At least two specific non-boilerplate questions. At least one must name a
missing signal. At least one must be a design ambiguity specific to {{topic}}.

End: `[ARTIFACT 1 COMPLETE — {N} open questions]`
Handoff: "Handing off to PM. M-tier requirements: [list]. Constraints: [list]."

---

### Artifact 2 — Proposal / ADR

**Role**: PM (business framing) + Architect (effort/risk estimates)
**Writes to**: `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md`

Dependency check: "Reading Artifact 1. Feature: {{topic}}. M-tier requirements: [list].
Constraints: [list]."

At least three options. **Option A = do-nothing.**

For each option:
- **Description**
- **Pros** (2+ specific)
- **Cons** (2+ specific)
- **Effort** — Architect: S/M/L/XL
- **Risk** — Architect: Low/Medium/High + one-line reason
- **Inertia impact** — PM: how does this option affect the inertia baseline? Option A must name
  the ongoing inertia cost explicitly.

If scout-feasibility was found, use it for effort and risk estimates and cite the file name.

**RECOMMENDATION** — Name the chosen option. Rationale must reference at least one M-tier
requirement and at least one constraint from the spec.

End: `[ARTIFACT 2 COMPLETE — Option X recommended]`
Handoff: "Handing off to Strategy. Recommended option: [X]. Rationale: [one sentence].
Pitch must not contradict spec constraints: [list]."

---

### Artifact 3 — Pitch

**Role**: Strategy (per-audience messaging) + PM (consistency check)
**Writes to**: `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`

Dependency check: "Reading Artifact 2. Recommended option: [X]. Reading Artifact 1.
Constraints: [list]. Feature name confirmed: {{topic}}."

Three audience versions: **Exec / Developer / Maker.**

Each version:
- **Hook** — one sentence that lands the problem
- **What it does** — two to three sentences, audience vocabulary
- **Why it matters** — reference the inertia baseline; state what changes for this audience
- **Call to action** — concrete next step

Framing:
- Exec: outcome-first, ROI, no implementation detail
- Developer: tool-level, workflow change, specific capability unlocked
- Maker: accessible, jargon-free, "is this for me?" framing

If scout-positioning was found, use it to inform per-audience framing and cite the file name.

**Anti-Positioning** — "What this is NOT." At least two specific exclusion statements. Each must
name a use case or adjacent concept that users might confuse with {{topic}}.

PM consistency check: "Feature name matches spec: [Y/N]. Recommended option correctly named:
[Y/N]. No constraint contradictions: [Y/N]."

End: `[ARTIFACT 3 COMPLETE]`

---

### Phase 4 — Completion Summary

```
CAMPAIGN COMPLETE — {{topic}}

Artifact 1 — Spec:     simulations/draft/specs/{{topic}}-spec-{{date}}.md
Artifact 2 — Proposal: simulations/draft/proposals/{{topic}}-proposal-{{date}}.md
Artifact 3 — Pitch:    simulations/draft/pitches/{{topic}}-pitch-{{date}}.md

Scout gate:         [signals found: list / "none found"]
Inertia baseline:   anchored in spec PURPOSE / proposal Option A / pitch "why it matters"
Recommended option: [from proposal]
Open questions:     [count from spec]
Contract executed:  3/3 artifacts written to declared paths
```
