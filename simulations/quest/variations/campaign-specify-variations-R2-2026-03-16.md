---

# campaign-specify — V-01 through V-05 (Round 2)

## R2 Context

R1 V-01 scored 100/100 and remains the golden baseline. R1 V-02 was corrupted (Phases 2-3 absent, scored 24.5 as structural void). R1 V-03-V-05 were never generated. Rubric v2 adds C-11/C-12/C-13 — all of which V-01 R1 already satisfies.

**C-12 experimental design:** V-02 deliberately omits Phase 0 to isolate whether handoff protocol alone prevents voice drift. If V-02 fails C-10, C-12 is confirmed as the structural driver of voice distinctness.

---

## V-01: Checklist-before-write axis

**Axis:** Pre-write section checklist — each phase begins with a table of required sections; the model marks each DONE before writing the artifact. Phase 0 is a checklist block, not prose.
**Hypothesis:** Mark-as-done row tracking creates a stronger commitment to section completeness than "do not skip" text instruction. The model cannot generate prose without first processing the structure.

See file at `simulations/quest/variations/campaign-specify-variations-R2-2026-03-16.md` for complete prompt bodies.

---

## V-02: Explicit handoff protocol axis

**Axis:** Setup + write + handoff statement at every phase boundary. Phase 0 audience framing is **deliberately absent** — isolates C-12 dependency.
**Hypothesis:** Explicit inheritance declarations are sufficient for C-05 (cross-artifact consistency) without a pre-flight frame. If C-10 fails, C-12 is confirmed as the structural driver of voice distinctness.

---

## V-03: Imperative runbook register axis

**Axis:** Direct command register — no "Role: X" persona framing. Phase 0 included as a lean inline "state four things" block.
**Hypothesis:** Removing persona framing reduces meta-commentary and hedging. The model acts rather than performs. Structural requirements identical to V-01; register is the variable.

---

## V-04: Inertia framing axis (new in R2)

**Axis:** Do-nothing competitor foregrounded throughout. Phase 0 names the inertia cost for each audience. Option 1 in the proposal gets full treatment as the real baseline. Pitch versions each lead with status-quo contrast before offering relief.
**Hypothesis:** Foregrounding inertia sharpens C-08 (trade-off rationale must defeat a concrete named baseline) and elevates C-10 (each audience voice is differentiated by its specific cost of inaction, not just framing register).

---

## V-05: Combination axis

**Axis:** Checklist (V-01) + handoff protocol (V-02) + inertia framing (V-04). Full Phase 0.
**Hypothesis:** Three orthogonal failure-mode patches without conflict. Should score 100/100 under v2.

---

## Variation Summary

| ID | Axis | Primary Criteria | C-12? | Key Differentiator |
|----|------|-----------------|-------|--------------------|
| V-01 | Checklist-before-write | C-02, C-03, C-04 | YES (Phase 0 checklist) | Mark-as-done state |
| V-02 | Explicit handoff protocol | C-05, C-09 | **NO** (experimental omission) | Inheritance declarations without pre-flight |
| V-03 | Imperative runbook | C-01, C-02, C-03 | YES (thin inline) | Register — no persona framing |
| V-04 | Inertia framing | C-08, C-10, C-03 | YES (full Phase 0) | Status quo as named competitor |
| V-05 | Checklist + handoff + inertia | All 13 | YES (full Phase 0) | Integration test |

**Predicted differentiators:**
- **C-10 failure**: V-02 most likely — no Phase 0. Confirms C-12 as voice-differentiation driver if it fails.
- **C-08 strength**: V-04 should show the strongest trade-off rationale (Do Nothing gets full-treatment comparison).
- **C-11 universal**: All five include active completion gates — should pass across the board.
- **C-12 edge case**: V-03's inline framing may or may not count as a "dedicated pre-write phase" — will be a scoreable boundary case.

Written to: `simulations/quest/variations/campaign-specify-variations-R2-2026-03-16.md`
ction. Do not write the artifact until all six rows are DONE.

Write artifact to: simulations/draft/specs/{topic}-spec-{date}.md
Print: "SPEC WRITTEN: simulations/draft/specs/{topic}-spec-{date}.md"

---

## Phase 2: draft-proposal

Role: Architect + PM

Read simulations/draft/specs/{topic}-spec-{date}.md before starting.

Scout signal check (before checklist):
Glob simulations/scout/feasibility/ for {topic}. List each signal found.
If any found: note how it informs option effort or risk estimates.
If none: "(no feasibility signal)"

Section checklist:

| Section | Status | Requirement |
|---------|--------|-------------|
| Context | [ ] | REQUIRED — what decision this proposal is making. One paragraph. References the spec. |
| Option 1: Do Nothing | [ ] | REQUIRED — describe status quo. Then: pros / cons / risk / effort. |
| Option 2: [name it] | [ ] | REQUIRED — describe the approach. Then: pros / cons / risk / effort. |
| Option 3: [name it] | [ ] | REQUIRED — describe the approach. Then: pros / cons / risk / effort. |
| Option 4+ | [ ] | OPTIONAL — add only if genuinely distinct from options 2 and 3. |
| Recommendation | [ ] | REQUIRED — name the option. Then write the trade-off sentence: "We chose [option] over [option] because [specific constraint or risk], accepting [what we give up]." Must be traceable to the options above. |

Mark each required row DONE before writing the artifact.

Write artifact to: simulations/draft/proposals/{topic}-proposal-{date}.md
Print: "PROPOSAL WRITTEN: simulations/draft/proposals/{topic}-proposal-{date}.md"

---

## Phase 3: draft-pitch

Role: PM + Strategy

Read simulations/draft/specs/{topic}-spec-{date}.md before starting.
Read simulations/draft/proposals/{topic}-proposal-{date}.md before starting.

Scout signal check (before checklist):
Glob simulations/scout/positioning/ for {topic}. List each signal found.
If any found: note which audience version it informs.
If none: "(no positioning signal)"

Recall the audience contracts from Phase 0. Each pitch version must open with a
sentence that matches its contract. If two versions share the same opening, rewrite
the later one.

Section checklist:

| Section | Status | Requirement |
|---------|--------|-------------|
| Exec Version | [ ] | REQUIRED — hook (outcome-first) / what it does (2 sentences, business level) / why it matters (ROI or risk) / call to action (specific ask). |
| Developer Version | [ ] | REQUIRED — hook (capability-first) / what it does (2 sentences, technical) / why it matters (pain removed) / call to action (next step). |
| Maker Version | [ ] | REQUIRED — hook (jargon-free, "you can now...") / what it does (plain language) / why it matters (time or friction saved) / call to action (how to start). |
| Anti-Positioning | [ ] | REQUIRED — three statements. Each: "{topic} is not [X]." Cover the three most likely misinterpretations. |

Mark all four rows DONE before writing the artifact.

Write artifact to: simulations/draft/pitches/{topic}-pitch-{date}.md
Print: "PITCH WRITTEN: simulations/draft/pitches/{topic}-pitch-{date}.md"

---

## Completion Gate

| Artifact | Path | Written? |
|----------|------|---------|
| Spec | simulations/draft/specs/{topic}-spec-{date}.md | [ ] |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md | [ ] |
| Pitch | simulations/draft/pitches/{topic}-pitch-{date}.md | [ ] |

Confirm each row. If any artifact is missing: write it now before stopping.
Do not end this skill with an empty row in the table above.
```

---

## V-02: Explicit handoff protocol axis

**Axis:** Setup + write + handoff at every phase boundary. Each phase emits a handoff statement naming what the next phase will inherit. Phase 0 audience framing is deliberately absent — to isolate whether handoff protocol alone prevents cross-artifact drift without pre-flight voice contracts.
**Hypothesis:** Explicit inheritance declarations ("the proposal will inherit: X, Y, Z") are a sufficient consistency mechanism for C-05 without needing an upfront audience frame. If C-10 (voice differentiation) fails on this variation, it confirms C-12 (Phase 0 audience framing) is the structural driver of voice distinctness, not consistency enforcement. Namespace-targeted scout pulls and completion fail-safe are included to prevent noise from C-09/C-11 failures.

```
You are running campaign-specify for: {topic}

Three artifacts. Three phases. Each phase has a mandatory setup step and a mandatory
handoff statement. You cannot begin writing an artifact until setup is complete. You
cannot move to the next phase until you have written the handoff statement.

---

## Phase 1: draft-spec

Role: Architect

### Setup
1. Glob simulations/scout/ for any signals related to {topic}.
   List each found: [namespace/skill] [path] [summary of content]
   If none: "(no scout signals — will author from intent)"

2. State the inheritance declaration:
   "This spec will incorporate from scout signals: [list items, or 'nothing — no signals']"

### Write
Author the spec. Pull requirements from scout-requirements if present.
All sections required — do not skip any:

**Purpose** — what {topic} is and why it exists. One paragraph.

**Requirements** — MoSCoW list. Source each requirement:
  "[M/S/C/W] [requirement] [source: scout-requirements or inferred]"

**Design** — how it works. Key architectural decisions. Not implementation code.
  Include ASCII diagram if the structure is non-obvious.

**Constraints** — what bounds this design. List at least three:
  one technical constraint, one business constraint, one scope or policy boundary.

**Open Questions** — unresolved items that must be answered before engineering.
  Each: [question] | [owner] | [what unblocks it]

**Self-Review (Architect)** — inspect the five sections. Flag:
  - any section vague enough to cause misimplementation
  - any open question that is actually a constraint in disguise
  - any requirement implied by the design but missing from the list
  At least one item flagged. "No issues found" is not acceptable.

Write artifact to: simulations/draft/specs/{topic}-spec-{date}.md

### Handoff Statement (required before Phase 2)
State exactly:
"Phase 1 complete. Proposal will inherit:
  - Feature name: [{topic} as named in spec]
  - Core behavior: [one sentence summary]
  - Key constraints: [list top two from Constraints section]
  - Spec path: simulations/draft/specs/{topic}-spec-{date}.md"

---

## Phase 2: draft-proposal

Role: Architect (options) + PM (trade-offs)

### Setup
1. Read simulations/draft/specs/{topic}-spec-{date}.md
2. Confirm inheritance from Phase 1 handoff:
   "Inherited: feature name = [X], core behavior = [Y], top constraints = [Z1, Z2]"
   Feature name and core behavior must match the handoff exactly.
3. Glob simulations/scout/feasibility/ for {topic}. List any signals found.
4. State what feasibility signals contribute:
   "[signal name] informs [option name] effort/risk estimates" — or "(no feasibility signal)"

### Write
Author the proposal. Three options minimum; do-nothing must be one of them.

**Context** — what decision this proposal records. One paragraph. Reference the spec by path.

**Option 1: Do Nothing** — describe status quo. Then list:
  - Pros: [what is preserved or avoided]
  - Cons: [what remains broken or missing]
  - Risk: [what gets worse over time]
  - Effort: [cost of doing nothing — maintenance, opportunity, technical debt]

**Option 2: [Name the approach]** — describe it. Then list:
  - Pros / Cons / Risk / Effort

**Option 3: [Name the approach]** — describe it. Then list:
  - Pros / Cons / Risk / Effort

Add Option 4+ only if genuinely distinct from options 2 and 3.

**Recommendation** — name the chosen option. Then write:
  "The deciding trade-off: [chosen option] accepts [cost X] in exchange for [benefit Y],
  which outweighs [what rejected option offered] given [specific constraint from the spec
  or from the options above]."
  This sentence must be falsifiable — a reader should be able to disagree with it.
  "Option 2 is best" does not pass.

Feature name and core behavior must match the Phase 2 setup inheritance exactly.

Write artifact to: simulations/draft/proposals/{topic}-proposal-{date}.md

### Handoff Statement (required before Phase 3)
State exactly:
"Phase 2 complete. Pitch will inherit:
  - Feature name: [same as inherited in Phase 2 setup]
  - Recommended option: [name]
  - Primary rationale: [one sentence trade-off summary]
  - Proposal path: simulations/draft/proposals/{topic}-proposal-{date}.md"

---

## Phase 3: draft-pitch

Role: PM + Strategy

### Setup
1. Read simulations/draft/specs/{topic}-spec-{date}.md
2. Read simulations/draft/proposals/{topic}-proposal-{date}.md
3. Confirm inheritance from Phase 2 handoff:
   "Inherited: feature name = [X], recommended option = [Y], rationale = [Z]"
4. Glob simulations/scout/positioning/ for {topic}. List any signals found.
5. State what positioning signals contribute:
   "[signal name] informs [exec/dev/maker] hook" — or "(no positioning signal)"

### Write
Author the pitch. All three audience versions required.

**Exec Version** — this person funds or blocks. Lead with the outcome they care about.
- Hook: one sentence. Leads with outcome or business risk.
- What it does: two sentences. Business-level description — no API details.
- Why it matters: one paragraph. ROI framing, risk reduction, or strategic positioning.
- Call to action: one sentence. Specific ask: approve, fund, unblock, or schedule.

**Developer Version** — this person builds or integrates. Lead with the tool/capability.
- Hook: one sentence. Leads with what the developer can now do or what pain disappears.
- What it does: two sentences. Technical framing — what the API, tool, or behavior is.
- Why it matters: one paragraph. Names the specific developer frustration this eliminates.
- Call to action: one sentence. Concrete next step: read spec, try prototype, join review.

**Maker Version** — this person uses the feature. Lead with what they can now accomplish.
- Hook: one sentence. Opens with "You can now..." or equivalent jargon-free statement.
- What it does: two sentences. Plain language — no technical terminology.
- Why it matters: one paragraph. Concrete time saved or friction removed.
- Call to action: one sentence. How to start using it today.

**Anti-Positioning** — three statements. Each: "{topic} is not [X]."
  Derive from the spec constraints. Cover the three most likely scope misinterpretations.

Feature name in all three versions must match the Phase 3 setup inheritance.

Write artifact to: simulations/draft/pitches/{topic}-pitch-{date}.md

---

## Completion Verification

State for each artifact:
- simulations/draft/specs/{topic}-spec-{date}.md — written? Y/N
- simulations/draft/proposals/{topic}-proposal-{date}.md — written? Y/N
- simulations/draft/pitches/{topic}-pitch-{date}.md — written? Y/N

If any N: write that artifact now. End only when all three are confirmed Y on disk.
Stating Y without having written the file is not acceptable.
```

---

## V-03: Imperative runbook register axis

**Axis:** Direct command register — no "Role: X" persona framing, no character briefs. Every instruction is a direct action verb. Phase 0 is included as a brief inline "state three things" block to preserve C-12, but in the leanest possible form.
**Hypothesis:** Dropping persona framing ("Role: Architect") and replacing it with direct imperative commands reduces model meta-commentary about playing a role and decreases the probability of hedging prefixes. The model acts rather than performing. Structural requirements are identical to V-01; the variable is the register of the instruction, not the content.

```
You are running campaign-specify for: {topic}

Write three artifacts to disk: a spec, a proposal, and a pitch — in that order.
Do not summarize or explain your plan. Execute the steps below.

---

## Before writing anything: state the audience frame

Say the following three things before Phase 1 starts:
1. "{topic} does [X] for [Y] so that [Z]."
2. "The exec cares about: [outcome or risk in one phrase]."
3. "The developer cares about: [capability or pain removed in one phrase]."
4. "The maker cares about: [what they can now do, jargon-free, in one phrase]."

These four statements are your anchor. Every audience-facing section must be traceable
to statement 2, 3, or 4. Do not skip this block.

---

## Phase 1: Write the spec

Check simulations/scout/ for any existing signals about {topic}. List what you find:
[namespace/skill path] for each. If none, write "(no scout signals found)".
If scout-requirements signals exist, use them as the requirements source and cite them.

Write simulations/draft/specs/{topic}-spec-{date}.md. Include every section below.
No section may be omitted. No section may be a single line.

**Purpose**
What {topic} is and why it exists. One paragraph. Not a bullet list.

**Requirements**
Bulleted list. Tag each: [M] must / [S] should / [C] could / [W] won't.
If you pulled from scout-requirements, say so. If you inferred, label [inferred].

**Design**
How it works. Describe decisions, not implementation. Use ASCII diagram if
the structure has non-obvious component relationships.

**Constraints**
What the design cannot exceed or ignore.
List at least three: one technical, one business, one scope or policy constraint.
Each constraint: state what is bounded and why the bound exists.

**Open Questions**
Questions that must be answered before engineering starts.
At least one. For each: what the question is / who owns answering it.

**Self-Review**
Inspect the five sections you just wrote. Call out:
- anything thin enough to cause misimplementation
- any ambiguity a reasonable engineer would interpret differently than you intend
- any assumption written as a fact that should be an open question instead
Write at least one item. If you wrote "no gaps" — that is a gap.

---

## Phase 2: Write the proposal

Read simulations/draft/specs/{topic}-spec-{date}.md before writing anything.

Check simulations/scout/feasibility/ for {topic}. Note what you find.
If a feasibility signal exists, use it to inform option effort or risk estimates.

Write simulations/draft/proposals/{topic}-proposal-{date}.md. Include every section below.

**Context**
What decision this proposal is making. One paragraph. Reference the spec — cite its path.

**Option 1: Do Nothing**
Describe continuing the status quo. Then list:
pros / cons / risk / effort

**Option 2: [name it]**
Describe this approach. Then list:
pros / cons / risk / effort

**Option 3: [name it]**
Describe this approach. Then list:
pros / cons / risk / effort

Add more options only if they are genuinely different approaches — not variations
of the same approach.

**Recommendation**
Name the chosen option. Then write this sentence:
"We chose [option] over [option] because [specific constraint or risk from above],
accepting [what we give up]."
The constraint or risk must be traceable to the options section above.
A general preference statement does not pass.

---

## Phase 3: Write the pitch

Read simulations/draft/specs/{topic}-spec-{date}.md before writing.
Read simulations/draft/proposals/{topic}-proposal-{date}.md before writing.

Check simulations/scout/positioning/ for {topic}. Note what you find.
If a positioning signal exists, note which audience version it informs.

Recall the audience frame you stated before Phase 1. Each version must lead with
a sentence traceable to its audience contract. If exec and dev versions share the
same first sentence, rewrite the dev version.

Write simulations/draft/pitches/{topic}-pitch-{date}.md. Include every section below.

**Exec version**
Lead with the outcome or risk the exec cares about.
Hook (one sentence) / What it does (two sentences, business level) /
Why it matters (ROI or risk framing) / Call to action (specific: approve, fund, unblock)

**Developer version**
Lead with the tool capability or the pain it removes.
Hook (one sentence) / What it does (two sentences, technical) /
Why it matters (names the frustration this eliminates) / Call to action (next step)

**Maker version**
Lead with what the person can now accomplish.
Hook ("You can now..." or equivalent) / What it does (plain language, no jargon) /
Why it matters (time saved or friction removed) / Call to action (how to start)

**Anti-positioning**
Write three sentences. Each: "{topic} is not [X]."
Cover the three most likely scope misinterpretations. Derive from spec constraints.

---

## Done check

Before stopping, verify:
- simulations/draft/specs/{topic}-spec-{date}.md exists and was written this session?
- simulations/draft/proposals/{topic}-proposal-{date}.md exists and was written this session?
- simulations/draft/pitches/{topic}-pitch-{date}.md exists and was written this session?

If any artifact is missing, write it now. Do not end until all three files are on disk.
```

---

## V-04: Inertia framing axis

**Axis:** Do-nothing competitor foregrounded throughout. The cost of inaction is named at every phase — not just as a proposal option, but as the implicit frame the entire package is working against.
**Hypothesis:** Foregrounding inertia (the status quo as the real competitor) sharpens trade-off writing (C-08) because the proposal must defeat a concrete named baseline, not just choose between abstract options. It also strengthens pitch differentiation (C-10) because each audience version becomes a case against the status quo for that audience specifically — exec, developer, and maker each have a different cost of inaction. Structural requirements are identical to V-01; the variable is the prominence and consistency of the inertia frame.

```
You are running campaign-specify for: {topic}

Produce a complete specification package: spec, proposal, and pitch.
All three artifacts must be written to disk.

The frame for all three artifacts:

  The real competitor for {topic} is doing nothing.
  Before this feature exists, teams work around the problem manually, skip the step,
  or build something ad-hoc. The spec, proposal, and pitch exist to show why that
  status quo is not acceptable — and what {topic} offers instead.

Keep this frame visible throughout.

---

## Phase 0: Audience frame + inertia cost

Before writing anything, state:
1. Feature sentence: "{topic} does [X] for [Y] so that [Z]."
2. Status quo cost (exec perspective): "Without {topic}, execs accept [risk or cost]."
3. Status quo cost (developer perspective): "Without {topic}, developers [do this manually / work around this / lack this capability]."
4. Status quo cost (maker perspective): "Without {topic}, makers [can't do X / spend time on Y / hit friction at Z]."
5. Audience contracts:
   - Exec: cares about [outcome / risk stated above]
   - Developer: cares about [capability / pain stated above]
   - Maker: cares about [thing they can do / friction removed stated above]

These inertia costs are the foil for every audience-facing section. The pitch
must make the status quo feel more expensive than building {topic}.

---

## Phase 1: draft-spec

Role: Architect

Scout signal check: glob simulations/scout/ for {topic}.
List each signal found: [namespace/skill] [path] [summary].
If none: "(no scout signals — will author from intent)"
If scout-requirements found: pull requirements from it and cite the source.

Write the spec. All sections required:

### Purpose
What {topic} is and why it exists. One paragraph.
Name the status quo problem in the first two sentences. What breaks, wastes time,
or is missing when {topic} does not exist?

### Requirements
MoSCoW list. For each requirement, note whether it addresses a status quo gap
or adds new capability beyond current practice:
  "[M/S/C/W] [requirement] [gap-fill or new-capability]"

### Design
How {topic} works. Key architectural decisions. ASCII diagram if useful.

### Constraints
What bounds the design. At least three: one technical, one business, one scope/policy.
For each constraint: state why this bound matters for adoption (not just for correctness).

### Open Questions
Unresolved items before engineering starts. At least one.
Each: [question] / [owner] / [what unblocks it]

### Self-Review (Architect)
Inspect the five sections above. Flag:
- sections too thin to prevent misimplementation
- ambiguities that would cause scope expansion during build
- assumptions that should be stated constraints instead
At least one item. "No gaps found" is a gap.

Write artifact to: simulations/draft/specs/{topic}-spec-{date}.md

---

## Phase 2: draft-proposal

Role: Architect + PM

Read simulations/draft/specs/{topic}-spec-{date}.md before writing.

Scout signal check: glob simulations/scout/feasibility/ for {topic}.
List any signals found and note how they inform effort or risk estimates.
If none: "(no feasibility signal)"

Write the proposal. The do-nothing option is not a formality — it is the baseline
the other options must defeat. Give it full treatment.

### Context
What decision this proposal is making. One paragraph. Reference the spec.
State the cost of reaching this decision point: what has the status quo already cost?

### Option 1: Do Nothing
This is the status quo. Describe what teams currently do instead of {topic}.
Then:
- Pros: what the status quo preserves (inertia, familiarity, zero migration cost)
- Cons: what the status quo costs (manual work, errors, missing capability)
- Risk: what gets worse over time if nothing is built
- Effort: ongoing cost of maintaining the workaround

### Option 2: [Name the approach]
Description. Then:
- Pros / Cons / Risk / Effort

### Option 3: [Name the approach]
Description. Then:
- Pros / Cons / Risk / Effort

Add Option 4+ only if genuinely distinct.

### Recommendation
Name the chosen option. Then write:
"We chose [option] over Do Nothing because [specific cost from Option 1 cons/risk],
and over [other option] because [specific trade-off from their comparison]."
The trade-off must reference named content from the options above.
A preference statement without a named cost does not pass.

Write artifact to: simulations/draft/proposals/{topic}-proposal-{date}.md

---

## Phase 3: draft-pitch

Role: PM + Strategy

Read simulations/draft/specs/{topic}-spec-{date}.md before writing.
Read simulations/draft/proposals/{topic}-proposal-{date}.md before writing.

Scout signal check: glob simulations/scout/positioning/ for {topic}.
List any signals and note which audience version each informs.
If none: "(no positioning signal)"

Recall the inertia costs from Phase 0. Each audience version must make the
status quo feel expensive for that specific audience — then offer {topic} as the
relief. The hook is not just a feature pitch; it is a contrast with the current state.

Recall the audience contracts from Phase 0. Each version must open with a sentence
traceable to its contract. No two versions may share the same opening sentence.

Write the pitch. All sections required:

### Exec Version
Audience: decision-maker who will fund or block.
The exec's inertia cost: what risk or cost does the status quo impose on the business?
- Hook: one sentence. Names the outcome or risk the exec cares about.
- What it does: two sentences. Business-level description.
- Why it matters: one paragraph. Lead with status quo cost, then show {topic}'s relief.
  Reference ROI, risk reduction, or strategic positioning.
- Call to action: one sentence. Specific ask.

### Developer Version
Audience: engineer who will build or integrate.
The developer's inertia cost: what does the developer currently do instead?
- Hook: one sentence. Names the capability or the pain that disappears.
- What it does: two sentences. Technical description — what the tool or API does.
- Why it matters: one paragraph. Name the specific workaround this replaces.
- Call to action: one sentence. Concrete next step.

### Maker Version
Audience: end user or creator who will use the feature.
The maker's inertia cost: what friction or limitation do they live with today?
- Hook: one sentence. Opens with "You can now..." or names the thing they couldn't do before.
- What it does: two sentences. Plain language — no technical terminology.
- Why it matters: one paragraph. Name the specific friction or time cost removed.
- Call to action: one sentence. How to start.

### Anti-Positioning
Three statements. Each: "{topic} is not [X]."
The first should address the most common status quo workaround: why {topic} is not
the same as the manual approach teams use today.
Cover the two additional most likely misinterpretations.

Write artifact to: simulations/draft/pitches/{topic}-pitch-{date}.md

---

## Completion Gate

Check: were all three artifacts written?
- simulations/draft/specs/{topic}-spec-{date}.md: [written?]
- simulations/draft/proposals/{topic}-proposal-{date}.md: [written?]
- simulations/draft/pitches/{topic}-pitch-{date}.md: [written?]

If any artifact is missing: write it now before ending.
Do not exit this skill with an unwritten artifact.
```

---

## V-05: Combination axis

**Axis:** Checklist-before-write (V-01) + explicit handoff protocol (V-02) + inertia framing (V-04). All three mechanisms operate simultaneously: the checklist enforces section completeness, handoff statements enforce cross-artifact inheritance, and inertia framing sharpens trade-off and pitch writing. Phase 0 is a full audience frame per V-01.
**Hypothesis:** The three axes address orthogonal failure modes without conflict:
- Checklist → prevents C-02/C-03/C-04 (section omission)
- Handoff protocol → prevents C-05 (scope drift between artifacts)
- Inertia framing → elevates C-08 (trade-off rationale) and C-10 (voice differentiation via per-audience status quo cost)

None of these mechanisms compete for the same instruction space. The combination should score 100/100 under v2 by preserving all of V-01 R1's winning patterns while adding the inertia frame as an additional quality layer.

```
You are running campaign-specify for: {topic}

Produce a specification package: spec, proposal, and pitch.
All three artifacts reach disk before this skill ends.

The implicit competitor throughout: the status quo. Before {topic} exists, people
work around the problem. Every artifact must show why that workaround is not acceptable.

---

## Phase 0: Audience frame + inertia costs (complete before any writing)

| Item | Status | Content |
|------|--------|---------|
| Feature sentence | [ ] | "{topic} does [X] for [Y] so that [Z]." |
| Exec inertia cost | [ ] | "Without {topic}, execs accept [specific risk or cost]." |
| Dev inertia cost | [ ] | "Without {topic}, developers [specific workaround or pain]." |
| Maker inertia cost | [ ] | "Without {topic}, makers [specific friction or limitation]." |
| Exec voice contract | [ ] | "Exec pitch leads with: [outcome / risk from row above]." |
| Dev voice contract | [ ] | "Dev pitch leads with: [capability / pain from row above]." |
| Maker voice contract | [ ] | "Maker pitch leads with: [what they can now do / friction removed]." |

Mark all seven rows DONE. These contracts and inertia costs govern Phases 1-3.
No Phase 1 writing until this table is complete.

---

## Phase 1: draft-spec

Role: Architect

### Setup
1. Glob simulations/scout/ for {topic} signals.
   List each found: [namespace/skill] [path] [summary]
   If none: "(no scout signals — authoring from intent)"
2. State inheritance:
   "Spec will incorporate from scout: [list, or 'nothing — no signals present']"

### Section checklist

| Section | Status | Requirement |
|---------|--------|-------------|
| Purpose | [ ] | REQUIRED — what {topic} is, what problem it solves. Open with the status quo gap. |
| Requirements | [ ] | REQUIRED — MoSCoW list. Pull from scout-requirements if found (cite it). Label [inferred] otherwise. |
| Design | [ ] | REQUIRED — how it works. Key decisions. ASCII diagram if non-obvious. |
| Constraints | [ ] | REQUIRED — at least three: technical / business / scope-policy. Each states why the bound matters for adoption. |
| Open Questions | [ ] | REQUIRED — at least one. Each: question / owner / unblocking condition. |
| Self-Review | [ ] | REQUIRED — flag thin sections, misimplementation risks, assumptions as facts. At least one item. "No gaps" fails this row. |

Mark each DONE after writing the section. Do not write the artifact until all six rows are DONE.

Write artifact to: simulations/draft/specs/{topic}-spec-{date}.md
Print: "SPEC WRITTEN: simulations/draft/specs/{topic}-spec-{date}.md"

### Handoff (required before Phase 2)
"Phase 1 complete. Proposal inherits:
  - Feature name: [as used in spec]
  - Core behavior: [one sentence]
  - Key constraints: [top two from Constraints section]
  - Status quo problem: [one sentence from Purpose]"

---

## Phase 2: draft-proposal

Role: Architect + PM

### Setup
1. Read simulations/draft/specs/{topic}-spec-{date}.md
2. Confirm Phase 1 handoff:
   "Inherited: feature name = [X], core behavior = [Y], top constraints = [Z1, Z2], status quo = [W]"
   Feature name and core behavior must match the handoff exactly.
3. Glob simulations/scout/feasibility/ for {topic}. List any signals found.
4. State feasibility contribution:
   "[signal name] informs [option name] effort/risk" — or "(no feasibility signal)"

### Section checklist

| Section | Status | Requirement |
|---------|--------|-------------|
| Context | [ ] | REQUIRED — what decision this records. References spec by path. States status quo cost. |
| Option 1: Do Nothing | [ ] | REQUIRED — describe the workaround teams use today. Pros / cons / risk / effort. Give full treatment. |
| Option 2: [name it] | [ ] | REQUIRED — describe the approach. Pros / cons / risk / effort. |
| Option 3: [name it] | [ ] | REQUIRED — describe the approach. Pros / cons / risk / effort. |
| Option 4+ | [ ] | OPTIONAL — only if genuinely distinct from 2 and 3. |
| Recommendation | [ ] | REQUIRED — name the option. Trade-off sentence: "We chose [X] over Do Nothing because [specific Option 1 cost], and over [Y] because [specific trade-off]. We accept [what we give up]." Must be falsifiable. |

Mark each required row DONE before writing the artifact.

Write artifact to: simulations/draft/proposals/{topic}-proposal-{date}.md
Print: "PROPOSAL WRITTEN: simulations/draft/proposals/{topic}-proposal-{date}.md"

### Handoff (required before Phase 3)
"Phase 2 complete. Pitch inherits:
  - Feature name: [same as Phase 1 handoff]
  - Recommended option: [name]
  - Primary rationale: [trade-off summary, one sentence]
  - Status quo cost defeated: [what Option 1 cost made this decision easy/hard]"

---

## Phase 3: draft-pitch

Role: PM + Strategy

### Setup
1. Read simulations/draft/specs/{topic}-spec-{date}.md
2. Read simulations/draft/proposals/{topic}-proposal-{date}.md
3. Confirm Phase 2 handoff:
   "Inherited: feature name = [X], recommended option = [Y], rationale = [Z], status quo cost = [W]"
4. Glob simulations/scout/positioning/ for {topic}. List any signals found.
5. State positioning contribution:
   "[signal name] informs [exec/dev/maker] hook" — or "(no positioning signal)"
6. Recall Phase 0 contracts:
   - Exec contract: [from Phase 0]
   - Dev contract: [from Phase 0]
   - Maker contract: [from Phase 0]
   Each version must open with a sentence traceable to its contract. No two versions
   share the same opening. If two match: rewrite the later one before marking DONE.

### Section checklist

| Section | Status | Requirement |
|---------|--------|-------------|
| Exec Version | [ ] | REQUIRED — hook (outcome-first, traces to exec contract) / what it does (2 sentences, business level) / why it matters (status quo cost + relief, ROI or risk) / CTA (specific: approve, fund, unblock). |
| Developer Version | [ ] | REQUIRED — hook (capability-first, traces to dev contract) / what it does (2 sentences, technical) / why it matters (names the workaround this replaces) / CTA (next step). |
| Maker Version | [ ] | REQUIRED — hook ("you can now..." or jargon-free equivalent, traces to maker contract) / what it does (plain language) / why it matters (friction or time saved) / CTA (how to start). |
| Anti-Positioning | [ ] | REQUIRED — three statements: "{topic} is not [X]." First statement addresses most common status quo workaround. Other two cover top misinterpretations. |

Mark all four rows DONE before writing the artifact.

Write artifact to: simulations/draft/pitches/{topic}-pitch-{date}.md
Print: "PITCH WRITTEN: simulations/draft/pitches/{topic}-pitch-{date}.md"

---

## Completion Gate

| Artifact | Path | Written? |
|----------|------|---------|
| Spec | simulations/draft/specs/{topic}-spec-{date}.md | [ ] |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md | [ ] |
| Pitch | simulations/draft/pitches/{topic}-pitch-{date}.md | [ ] |

State line count for each artifact written.
If any row is empty: write that artifact now before stopping.
Do not end with an incomplete table.

---

## Variation Summary

| ID | Axis | Key Hypothesis | Primary Criteria Targeted | C-12 present? |
|----|------|----------------|--------------------------|---------------|
| V-01 | Checklist-before-write (clean R1 V-02) | Mark-as-done commitment prevents section skips more reliably than text instruction | C-02, C-03, C-04 | YES (Phase 0 checklist) |
| V-02 | Explicit handoff protocol (R1 V-03) | Inheritance declarations alone prevent scope drift — C-12 deliberately absent to isolate its effect | C-05, C-09 | NO (experimental omission) |
| V-03 | Imperative runbook register (R1 V-04) | Direct command register reduces meta-commentary and hedging, improving structural compliance | C-01, C-02, C-03 | YES (thin inline version) |
| V-04 | Inertia framing (new axis) | Foregrounding status quo as competitor sharpens trade-off rationale and per-audience voice distinctness | C-08, C-10, C-03 | YES (full Phase 0) |
| V-05 | Checklist + handoff + inertia (combination) | Three orthogonal failure-mode patches without conflict | All 13 criteria | YES (full Phase 0) |

**Predicted differentiators for R2 scoring:**
- C-10 (voice differentiation): V-02 most likely to fail — no Phase 0 framing. If it fails C-10, C-12 is confirmed as the structural driver.
- C-08 (trade-off rationale): V-04 should show the strongest performance due to Do Nothing full-treatment framing.
- C-05 (consistency): V-02 and V-05 most likely to pass cleanly; V-03 and V-04 depend on register carrying the read instructions.
- C-12 (Phase 0 pre-write): V-01/V-04/V-05 should pass; V-03 may pass depending on whether inline framing counts as a dedicated phase.
- C-11 (completion fail-safe): All five include an active gate — should pass universally, confirming it is not axis-dependent.
