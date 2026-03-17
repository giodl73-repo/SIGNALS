Good — no prior campaign-specify goldens, clean slate. Now generating the 5 variations:

---

# campaign-specify — V-01 through V-05 (Round 1)

---

## V-01: Role Sequence axis

**Axis:** PM-first sequence — PM frames business context before Architect writes the spec, PM + Strategy close with the pitch.  
**Hypothesis:** Starting with PM role framing anchors scope in user value and audience differentiation before any writing begins. This should reduce cross-artifact scope drift (C-05) and improve exec/dev/maker voice distinctness in the pitch (C-10) by establishing audience framing up front.

```
You are running campaign-specify for: {topic}

This skill orchestrates three sub-skills in order: draft-spec, draft-proposal, draft-pitch.
Produce all three artifacts before stopping. Do not summarize — write the artifacts.

---

## Phase 0: Business Context Frame (PM role)

Before writing anything, establish the frame that all three artifacts will share.

Role: PM
State aloud (2-4 sentences):
- What problem does {topic} solve?
- Who are the three audiences this package serves: exec, developer, maker?
- What is the one sentence each audience cares about most?

Keep this frame visible. Every artifact will anchor to it.

---

## Phase 1: draft-spec

Role: Architect

Pull any scout signals from simulations/scout/ for {topic}.
List which signals were found (path + signal type). If none, note that.

Write the spec artifact. Required sections — do not skip any:

### Purpose
What {topic} is and why it exists. One paragraph.

### Requirements
List requirements. Mark each M (must), S (should), C (could), W (won't).
If scout-requirements signal found, pull requirements from it; note the source.

### Design
How it works. Key decisions, not implementation details. Diagrams as ASCII if useful.

### Constraints
What the design is bounded by. Technical, business, and policy constraints.

### Open Questions
Unresolved questions. At least one. Each question: who owns it, what unblocks it.

### Self-Review (Architect)
Look back at the five sections. Flag:
- Any section that is thin or needs more detail
- Any ambiguity that would confuse an engineer
- Any assumption that should be a requirement instead

Write artifact to: simulations/draft/specs/{topic}-spec-{date}.md

---

## Phase 2: draft-proposal

Role: Architect (technical options) + PM (business trade-offs)

Read simulations/draft/specs/{topic}-spec-{date}.md before writing.
Pull any scout-feasibility signal for {topic} if available.

Write the proposal artifact. Required structure:

### Context
One paragraph: what decision this proposal is for, grounded in the spec (Phase 1).

### Option 1: Do Nothing
Description | Pros | Cons | Risk | Effort

### Option 2: [Name the approach]
Description | Pros | Cons | Risk | Effort

### Option 3: [Name the approach]
Description | Pros | Cons | Risk | Effort

(Add Option 4+ if meaningfully distinct approaches exist)

### Recommendation
State the recommended option. Then state the key trade-off that drove the choice —
not just a preference. The trade-off must reference a concrete constraint or risk
from the options above.

Write artifact to: simulations/draft/proposals/{topic}-proposal-{date}.md

---

## Phase 3: draft-pitch

Role: PM + Strategy

Read simulations/draft/specs/{topic}-spec-{date}.md before writing.
Read simulations/draft/proposals/{topic}-proposal-{date}.md before writing.
Pull any scout-positioning signal for {topic} if available.

The PM frame from Phase 0 stated what each audience cares about. Use that to write
detectably different voices — not the same content reordered.

Write the pitch artifact. Required structure:

### Exec Version
Audience: decision-maker who will fund or block.
Voice contract: outcome-first, ROI framing, risk mention.
- Hook (one sentence — the outcome)
- What it does (two sentences max)
- Why it matters (business or risk framing)
- Call to action (specific ask)

### Developer Version
Audience: engineer who will build or integrate.
Voice contract: show the tool, not the business case.
- Hook (one sentence — the capability)
- What it does (technical framing, concrete)
- Why it matters (developer pain it removes)
- Call to action (specific next step)

### Maker Version
Audience: end user or creator who will use the feature.
Voice contract: jargon-free, "can I do this?" framing.
- Hook (one sentence — the thing they can now do)
- What it does (plain language)
- Why it matters (time or frustration saved)
- Call to action (how to start)

### Anti-Positioning
What {topic} is NOT. Three statements that preempt scope creep or misuse.
Each starts with: "{topic} is not..."

Write artifact to: simulations/draft/pitches/{topic}-pitch-{date}.md

---

## Completion Check

Confirm all three artifacts were written. State the path and approximate line count for each.
If any artifact was skipped, write it now — do not end without all three on disk.
```

---

## V-02: Output Format axis

**Axis:** Checklist-before-write format — each sub-skill declares its required section checklist as a table, marks each section REQUIRED or OPTIONAL, then fills it.  
**Hypothesis:** Declaring required sections explicitly as a pre-write checklist prevents silent section skips (C-02, C-03, C-04). The model commits to the structure before prose generation begins, reducing the drift toward omitting "hard" sections like constraints and open questions.

```
You are running campaign-specify for: {topic}

Produce three artifacts in sequence: spec → proposal → pitch. All three must be
written to disk before this skill ends. Each phase begins with a section checklist —
mark each row DONE as you complete it.

---

## Phase 1: draft-spec

Role: Architect

Scout signal check: glob simulations/scout/ for {topic} signals.
List found: [signal name | path] for each. If none: "(no scout signals found)"

Section checklist — mark DONE as each is written:

| Section | Status | Requirement |
|---------|--------|-------------|
| Purpose | [ ] | REQUIRED — what it is and why it exists |
| Requirements | [ ] | REQUIRED — MoSCoW list; pull from scout-requirements if present |
| Design | [ ] | REQUIRED — how it works, key decisions |
| Constraints | [ ] | REQUIRED — technical, business, policy bounds |
| Open Questions | [ ] | REQUIRED — at least one unresolved question with owner |
| Self-Review | [ ] | REQUIRED — gaps, ambiguities, thin sections called out |

Write each section fully before moving to the next. Update the checklist as you go.
When all six rows are DONE, write the full artifact.

Write artifact to: simulations/draft/specs/{topic}-spec-{date}.md
Print: "SPEC DONE: simulations/draft/specs/{topic}-spec-{date}.md"

---

## Phase 2: draft-proposal

Role: Architect + PM

Read Phase 1 artifact before writing.
Scout signal check: glob simulations/scout/feasibility/ for {topic}.

Section checklist:

| Section | Status | Requirement |
|---------|--------|-------------|
| Context | [ ] | REQUIRED — what decision this is for, grounded in spec |
| Option: Do Nothing | [ ] | REQUIRED — description, pros, cons, risk, effort |
| Option 2 | [ ] | REQUIRED — named approach, same five fields |
| Option 3 | [ ] | REQUIRED — named approach, same five fields |
| Option 4+ | [ ] | OPTIONAL — add only if meaningfully distinct |
| Recommendation | [ ] | REQUIRED — chosen option + the trade-off that drove it |

For the Recommendation section: the stated trade-off must be traceable to a specific
pro/con/risk in one of the options above. "Option 2 balances X against Y from Option 3"
is acceptable. "Option 2 is best" is not.

When all required rows are DONE, write the full artifact.

Write artifact to: simulations/draft/proposals/{topic}-proposal-{date}.md
Print: "PROPOSAL DONE: simulations/draft/proposals/{topic}-proposal-{date}.md"

---

## Phase 3: draft-pitch

Role: PM + Strategy

Read Phase 1 and Phase 2 artifacts before writing.
Scout signal check: glob simulations/scout/positioning/ for {topic}.

Section checklist:

| Section | Status | Requirement |
|---------|--------|-------------|
| Exec Version | [ ] | REQUIRED — hook, what, why (ROI/risk), CTA |
| Developer Version | [ ] | REQUIRED — hook, what (technical), why (pain removed), CTA |
| Maker Version | [ ] | REQUIRED — hook, what (plain), why (time/friction), CTA |
| Anti-Positioning | [ ] | REQUIRED — 3+ statements of what this is NOT |

Voice rule: each version must open with a different first sentence. If exec and dev
versions share the same hook, rewrite the dev version.

When all four rows are DONE, write the full artifact.

Write artifact to: simulations/draft/pitches/{topic}-pitch-{date}.md
Print: "PITCH DONE: simulations/draft/pitches/{topic}-pitch-{date}.md"

---

## Final Checklist

| Artifact | Path | Written? |
|----------|------|---------|
| Spec | simulations/draft/specs/{topic}-spec-{date}.md | [ ] |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md | [ ] |
| Pitch | simulations/draft/pitches/{topic}-pitch-{date}.md | [ ] |

All three must be DONE. If any is missing, write it now.
```

---

## V-03: Lifecycle Emphasis axis

**Axis:** Explicit handoff protocol — each sub-skill begins with a mandatory prior-artifact read and an inheritance statement declaring what it pulled. Phase boundaries are hard: nothing is written until the inheritance statement is complete.  
**Hypothesis:** Forcing an explicit inheritance step before each write eliminates the silent scope drift that causes C-05 failures. The model cannot skip it because the inheritance statement is the gate to writing. Also surfaces scout signal pull-through (C-09) as a natural side effect of the setup phase.

```
You are running campaign-specify for: {topic}

Three artifacts. Three phases. Each phase has a mandatory setup step before writing.
You cannot begin writing an artifact until its setup step is complete.

---

## Phase 1: draft-spec
Role: Architect

### Setup (run before writing)
1. Glob simulations/scout/ for any signals related to {topic}.
   List each found signal: [namespace/skill] [path] [what it contains]
   If none found: state "(no scout signals — will author from intent)"

2. State what the spec will pull from scout signals:
   "This spec will inherit: [list items, or 'nothing — no signals present']"

### Write
Author the spec. Pull requirements from scout-requirements if present.
Sections (all required):
- Purpose — what {topic} is and why it exists
- Requirements — MoSCoW; source each requirement (scout-signal or inferred)
- Design — how it works, key architectural decisions
- Constraints — technical, business, policy
- Open Questions — unresolved; each has an owner and unblocking condition
- Self-Review — gaps, thin sections, ambiguities flagged

Write artifact to: simulations/draft/specs/{topic}-spec-{date}.md

### Handoff Statement
After writing, state:
"Phase 1 complete. The proposal will inherit: [core behavior], [key constraints], [feature name as used in spec]"

---

## Phase 2: draft-proposal
Role: Architect (options) + PM (trade-offs)

### Setup (run before writing)
1. Read simulations/draft/specs/{topic}-spec-{date}.md
2. State the inheritance:
   "Inherited from spec: feature name = [X], core behavior = [Y], key constraints = [Z]"
3. Glob simulations/scout/feasibility/ for {topic}. List any signals found.
4. State what the proposal will pull from feasibility signals:
   "[signal name] informs option effort/risk estimates" or "(no feasibility signal)"

### Write
Author the proposal. Three options minimum; do-nothing must be one of them.
Each option: description, pros, cons, risk, effort.
Recommendation: name the option + state the explicit trade-off that drove selection.
The trade-off must be traceable to the options above — not a preference statement.

Feature name and core behavior must match what was stated in the Phase 2 inheritance.

Write artifact to: simulations/draft/proposals/{topic}-proposal-{date}.md

### Handoff Statement
After writing, state:
"Phase 2 complete. The pitch will inherit: [recommended option name], [primary rationale], [feature name as used in proposal]"

---

## Phase 3: draft-pitch
Role: PM + Strategy

### Setup (run before writing)
1. Read simulations/draft/specs/{topic}-spec-{date}.md
2. Read simulations/draft/proposals/{topic}-proposal-{date}.md
3. State the inheritance:
   "Inherited: feature name = [X], recommended approach = [Y], key rationale = [Z]"
4. Glob simulations/scout/positioning/ for {topic}. List any signals found.
5. State what positioning signals contribute:
   "[signal] informs [exec|dev|maker] hook" or "(no positioning signal)"

### Write
Author the pitch. Three audience versions required.

Exec version — outcome-first, ROI/risk framing:
  Hook | What it does | Why it matters | Call to action

Developer version — tool-first, capability framing:
  Hook | What it does (technical) | Why it matters (pain removed) | Call to action

Maker version — jargon-free, "can I do this?" framing:
  Hook | What it does (plain) | Why it matters (time/friction) | Call to action

Anti-positioning — three statements: "{topic} is not..."
All three audience versions must use the feature name from the Phase 3 inheritance.

Write artifact to: simulations/draft/pitches/{topic}-pitch-{date}.md

---

## Verification
State:
- simulations/draft/specs/{topic}-spec-{date}.md — written? Y/N
- simulations/draft/proposals/{topic}-proposal-{date}.md — written? Y/N  
- simulations/draft/pitches/{topic}-pitch-{date}.md — written? Y/N

If any N: write it now. End only when all three are Y.
```

---

## V-04: Phrasing Register axis

**Axis:** Conversational/imperative register — direct commands with brief inline rationale; no role-play persona framing; reads like a runbook rather than a character brief.  
**Hypothesis:** Dropping the "Role: Architect" persona framing and replacing it with direct action commands ("Do X. Then do Y. Check Z before continuing.") reduces model hedging and meta-commentary about playing a role, improving the signal-to-noise ratio of the output and the likelihood of hitting the structural requirements.

```
You are running campaign-specify for: {topic}

Write three artifacts. In this order: spec first, proposal second, pitch third.
Do not skip any artifact. Do not summarize what you plan to do — just do it.

---

## Step 1: Write the spec

Check simulations/scout/ for any existing signals about {topic}. List what you find.
If you find scout-requirements signals, use them as your requirements source.

Write simulations/draft/specs/{topic}-spec-{date}.md with these sections:

**Purpose** — what {topic} is and why it exists. One paragraph.

**Requirements** — bulleted list. Tag each: [M] must / [S] should / [C] could / [W] won't.
  If you pulled from scout-requirements, say so. If you inferred, say so.

**Design** — how it works. Focus on decisions, not implementation. ASCII diagram if helpful.

**Constraints** — what the design cannot exceed or ignore. List at least three.

**Open Questions** — questions that must be answered before engineering starts.
  Each question: what it is, who owns answering it.

**Self-Review** — look back at the five sections above.
  Call out: anything thin, anything ambiguous, any assumption masquerading as a requirement.
  At least one item. "No gaps found" is not acceptable.

---

## Step 2: Write the proposal

Read the spec you just wrote.
Check simulations/scout/feasibility/ for {topic} signals. Note what you find.

Write simulations/draft/proposals/{topic}-proposal-{date}.md with these sections:

**Context** — what decision this proposal is making. One paragraph. Reference the spec.

**Option 1: Do Nothing** — describe it, then list pros / cons / risk / effort.

**Option 2: [name it]** — describe it, then list pros / cons / risk / effort.

**Option 3: [name it]** — describe it, then list pros / cons / risk / effort.

Add more options only if they are genuinely different approaches.

**Recommendation** — pick one option. Then write the trade-off sentence:
  "We chose [option] over [option] because [specific constraint or risk], accepting [what we give up]."
  This sentence must name something from the options above — not a general preference.

---

## Step 3: Write the pitch

Read the spec and proposal you just wrote.
Check simulations/scout/positioning/ for {topic} signals. Note what you find.

Write simulations/draft/pitches/{topic}-pitch-{date}.md with these sections:

**Exec version** — this person funds or blocks. They want outcomes and risk.
  Write: hook (one sentence, outcome) / what it does (two sentences) / why it matters (business or risk) / call to action (specific ask)

**Developer version** — this person builds or integrates. They want to know what the tool does.
  Write: hook (one sentence, capability) / what it does (concrete, technical) / why it matters (removes what pain) / call to action (next step)

**Maker version** — this person uses it. They want to know if they can do the thing.
  Write: hook (one sentence, "you can now...") / what it does (plain language) / why it matters (time or friction) / call to action (how to start)

**Anti-positioning** — three sentences. Each one: "{topic} is not [thing people will assume it is]."
  These should preempt the three most common misinterpretations.

---

## Done?

Check:
- simulations/draft/specs/{topic}-spec-{date}.md — exists?
- simulations/draft/proposals/{topic}-proposal-{date}.md — exists?
- simulations/draft/pitches/{topic}-pitch-{date}.md — exists?

If any is missing, write it before stopping.
```

---

## V-05: Combination

**Axis:** PM-first role sequence (V-01) + explicit handoff protocol (V-03) + audience voice contracts stated upfront.  
**Hypothesis:** The three single-axis wins address distinct failure modes without conflict: PM framing reduces scope drift (C-05) and voice uniformity (C-10); explicit handoffs enforce cross-artifact consistency (C-05) and scout pull-through (C-09); voice contracts stated before writing prevent all three pitch sections from defaulting to the same framing (C-10). This combination should be the highest scorer across the rubric.

```
You are running campaign-specify for: {topic}

Produce: spec, proposal, pitch — in that order, all three on disk.

---

## Pre-flight: Audience Frame (PM role)

Before writing anything, state:
1. The feature in one sentence: "{topic} does [X] for [Y] so that [Z]."
2. Exec audience contract: "The exec cares about [outcome/risk]."
3. Developer audience contract: "The developer cares about [capability/pain]."
4. Maker audience contract: "The maker cares about [can they do the thing / friction removed]."

These contracts govern all three artifacts. Every audience-facing section must
be traceable to its contract. State this frame — do not skip it.

---

## Phase 1: draft-spec (Architect role)

### Setup
Glob simulations/scout/ for {topic}. List each signal found: [namespace] [skill] [path].
State: "Inheriting from scout: [list items, or 'nothing found — authoring from intent']"

### Write
Sections — all required, all non-empty:

**Purpose** — one paragraph. What {topic} is, what problem it solves.

**Requirements** — MoSCoW list. If scout-requirements found: pull from it and cite it.
  If inferred: label each [inferred].

**Design** — how it works. Key decisions. Not implementation code.

**Constraints** — what bounds the design. Minimum three: one technical, one business,
  one policy or scope boundary.

**Open Questions** — unresolved before engineering can begin. Each: question / owner / unblocking condition.

**Self-Review (Architect)** — inspect the five sections above. Flag:
  - any section that is vague enough to cause misimplementation
  - any open question that is actually a constraint in disguise
  - any missing requirement that the design implies but the list omits

Write artifact to: simulations/draft/specs/{topic}-spec-{date}.md

### Handoff
State: "Spec written. Proposal inherits: feature name = [{topic}], core behavior = [one sentence], constraints = [list top two]"

---

## Phase 2: draft-proposal (Architect + PM roles)

### Setup
Read simulations/draft/specs/{topic}-spec-{date}.md.
Confirm inheritance: "Feature name: [X], core behavior: [Y], top constraints: [Z]"
Glob simulations/scout/feasibility/ for {topic}. Note any signal found.

### Write

**Context** — what decision this proposal records. One paragraph. Reference the spec directly.

**Option 1: Do Nothing** — describe status quo behavior. Then: pros / cons / risk / effort.

**Option 2: [Name]** — describe the approach. Then: pros / cons / risk / effort.

**Option 3: [Name]** — describe the approach. Then: pros / cons / risk / effort.

(Add Option 4+ only if genuinely distinct from 2 and 3.)

**Recommendation**
State: "We recommend Option [N]."
Then: "The deciding trade-off: [Option N] accepts [cost/risk X] in exchange for [benefit Y],
which matters more than [what Option M offered] given [specific constraint from the options above]."
The trade-off sentence must be falsifiable — a reader should be able to disagree with it.

Write artifact to: simulations/draft/proposals/{topic}-proposal-{date}.md

### Handoff
State: "Proposal written. Pitch inherits: recommended option = [X], primary rationale = [Y]"

---

## Phase 3: draft-pitch (PM + Strategy roles)

### Setup
Read simulations/draft/specs/{topic}-spec-{date}.md.
Read simulations/draft/proposals/{topic}-proposal-{date}.md.
Confirm inheritance: "Recommended option: [X], rationale: [Y]"
Glob simulations/scout/positioning/ for {topic}. Note any signal found.

Recall the audience contracts from the pre-flight:
- Exec: [contract from pre-flight]
- Developer: [contract from pre-flight]
- Maker: [contract from pre-flight]

Each pitch version must open with a sentence that matches its audience contract.
If two versions open the same way, rewrite the later one.

### Write

**Exec Version** — outcome-first, risk/ROI framing
- Hook: one sentence. Leads with the outcome the exec cares about.
- What it does: two sentences. Business-level description.
- Why it matters: one paragraph. References business risk or ROI.
- Call to action: one sentence. Specific ask (approve, fund, unblock).

**Developer Version** — tool-first, capability framing
- Hook: one sentence. Leads with the capability or problem removed.
- What it does: two sentences. Technical framing — what the API/tool/behavior is.
- Why it matters: one paragraph. Names the specific developer pain this eliminates.
- Call to action: one sentence. What to do next (read spec, try prototype, join review).

**Maker Version** — jargon-free, "can I do this?" framing
- Hook: one sentence. Starts with "You can now..." or equivalent.
- What it does: two sentences. Plain language — no technical terms.
- Why it matters: one paragraph. Concrete time saved or friction removed.
- Call to action: one sentence. How to start using it.

**Anti-Positioning** — three statements, each: "{topic} is not [X]."
  Cover the three most likely misinterpretations. Derive them from the spec constraints.

Write artifact to: simulations/draft/pitches/{topic}-pitch-{date}.md

---

## Completion

Verify all three artifacts exist. State path and line count for each.
If any is missing: write it now. Do not end until all three are confirmed on disk.
```

---

## Variation Summary

| ID | Axis | Single/Combo | Key Hypothesis | Primary Criteria Targeted |
|----|------|-------------|----------------|--------------------------|
| V-01 | Role sequence (PM-first) | Single | Business frame anchors scope, improves voice distinctness | C-05, C-10 |
| V-02 | Output format (checklist-before-write) | Single | Pre-commit to structure prevents section skip | C-02, C-03, C-04 |
| V-03 | Lifecycle emphasis (explicit handoff) | Single | Forced inheritance statement eliminates drift | C-05, C-09 |
| V-04 | Phrasing register (imperative runbook) | Single | Removes persona hedging, improves structural compliance | C-01, C-02, C-03 |
| V-05 | PM-first + handoff + voice contracts | Combination | Three failure modes addressed without conflict | C-05, C-09, C-10 |

**Recommended scoring order for quest-score R1:** Run all five against the same topic. Watch for C-05 (scope drift) and C-04 (pitch completeness) — those are the most likely differentiators between variations. V-02 and V-03 are the cleanest single-axis controls; V-05 is the integration test.
