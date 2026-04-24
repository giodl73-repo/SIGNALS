---
skill: quest-variate
skill_target: campaign-blueprint
date: 2026-03-16
round: 1
---

# campaign-blueprint — Prompt Variations R1

Five complete, runnable skill body variations. Single-axis first (V-01 through V-03),
then two combinations (V-04, V-05).

---

## V-01 — Role Sequence Axis

**Hypothesis:** Explicitly assigning a campaign-level Strategy role before any sub-skill
runs prevents topic drift and locks consistent framing across all three artifacts.
A shared brief written at the top reduces contamination risk between artifacts.

```
You are running /campaign-blueprint for: {topic}

CAMPAIGN SETUP — run this before any sub-skill:
Role: Strategy. Write a 4-line campaign brief covering: (1) the feature in one sentence,
(2) the primary problem it solves, (3) the intended audience, (4) what success looks like.
This brief is the shared contract for all three artifacts. Do not deviate from it.

--- ARTIFACT 1: SPEC ---
Role: Architect.
Author the technical specification. Sections: purpose, requirements, design, constraints,
open questions. Pull from scout-requirements if available. Self-review on completion:
flag any open questions, gaps, and ambiguity. The campaign brief governs scope — do not
expand beyond it. Write to: simulations/draft/specs/{topic}-spec-{date}.md

--- ARTIFACT 2: PROPOSAL ---
Role: Architect (technical options) + PM (business trade-offs).
Author a proposal grounded in the spec just written. Three options minimum including
do-nothing. Each option: description, pros, cons, risk, effort. Recommendation section
with rationale. Pull from scout-feasibility if available. Do not re-open design questions
the spec resolved. Write to: simulations/draft/proposals/{topic}-proposal-{date}.md

--- ARTIFACT 3: PITCH ---
Role: PM + Strategy.
Author a pitch in exec, developer, and maker versions. Each version: hook, what it does,
why it matters, call to action. Anti-positioning section (what we are NOT). Lead the exec
version with the outcome of the recommended option from the proposal. Pull from
scout-positioning if available. Maker version must be jargon-free. Write to:
simulations/draft/pitches/{topic}-pitch-{date}.md

CAMPAIGN CLOSE:
List: (1) artifacts written and their paths, (2) scout signals consumed, (3) open
questions flagged during the run that a future signal could resolve.
```

---

## V-02 — Output Format Axis

**Hypothesis:** Requiring tabular structure for the proposal options and a summary table
at campaign close reduces thin-artifact failures (C-05) by forcing explicit coverage
of all required fields per option — harder to accidentally drop a field than in prose.

```
You are running /campaign-blueprint for: {topic}

Produce three artifacts in sequence. Each artifact is written to disk before the next begins.

=== ARTIFACT 1: SPEC ===
Write a technical specification. Use this section structure:

| Section | Required content |
|---------|-----------------|
| Purpose | One-paragraph problem statement |
| Requirements | Bulleted list, MoSCoW-tagged (M/S/C/W) |
| Design | Approach, components, key decisions |
| Constraints | Technical, timeline, and resource limits |
| Open questions | Items requiring a future signal to resolve |

Pull from scout-requirements if the file exists.
Write to: simulations/draft/specs/{topic}-spec-{date}.md

=== ARTIFACT 2: PROPOSAL ===
Write a proposal with three options minimum (including do-nothing). Use this table per option:

| Field | Content |
|-------|---------|
| Name | Option label |
| Description | What this option does |
| Pros | Comma-separated list |
| Cons | Comma-separated list |
| Risk | H/M/L with one-line justification |
| Effort | S/M/L with one-line justification |

Follow the options table with a Recommendation section: state the chosen option and give
three reasons grounded in the spec. Pull from scout-feasibility if the file exists.
Write to: simulations/draft/proposals/{topic}-proposal-{date}.md

=== ARTIFACT 3: PITCH ===
Write three pitch versions. For each version use this structure:

| Field | Exec version | Dev version | Maker version |
|-------|-------------|------------|--------------|
| Audience | Business decision-makers | Engineers and technical leads | Builders and practitioners |
| Hook | ROI / outcome first | Tool / capability first | "Can I do this?" first |
| What it does | Business-level summary | Technical summary | Plain-language summary |
| Why it matters | Risk of inaction | Technical debt / opportunity cost | Time saved / friction removed |
| Call to action | Approve / fund | Join the beta | Try it now |

Add a one-paragraph Anti-positioning section (what we are NOT).
Pull from scout-positioning if the file exists.
Write to: simulations/draft/pitches/{topic}-pitch-{date}.md

=== CAMPAIGN SUMMARY ===
Produce a summary table:

| Artifact | Path | Status | Open questions |
|----------|------|--------|---------------|
| Spec | simulations/draft/specs/... | written | (list) |
| Proposal | simulations/draft/proposals/... | written | (list) |
| Pitch | simulations/draft/pitches/... | written | (list) |
```

---

## V-03 — Lifecycle Emphasis Axis

**Hypothesis:** Making the 4-phase signal lifecycle (setup / execute / findings / amend)
explicit at the campaign level — not just at sub-skill level — prevents the most common
failure pattern: starting artifact 2 before artifact 1 is complete, and producing a pitch
that references nothing from the proposal.

```
You are running /campaign-blueprint for: {topic}

This skill runs the full 4-phase signal lifecycle three times — once per artifact.
Complete each phase before moving to the next artifact.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 0: CAMPAIGN SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Identify the topic. Glob for any existing scout signals under simulations/scout/.
List signals found. Confirm topic identity — this identity must remain consistent
across all three artifacts.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 1 — SPEC
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SETUP: Pull purpose from scout-requirements if available. Identify any requirements
       already captured in scout signals.
EXECUTE: Author specification sections: purpose, requirements, design, constraints,
         open questions.
FINDINGS: List 3 findings from the spec process — decisions made, ambiguities
          surfaced, assumptions that need validation.
AMEND: For each finding that is an open question, note which signal namespace
       could resolve it (e.g., prove-hypothesis, scout-feasibility).
WRITE: simulations/draft/specs/{topic}-spec-{date}.md
GATE: Do not begin Artifact 2 until this file is written.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 2 — PROPOSAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SETUP: Read the spec just written. Pull from scout-feasibility if available.
       Identify the key decisions from the spec that constrain the option space.
EXECUTE: Author proposal with three options minimum (including do-nothing). Each option:
         description, pros, cons, risk, effort. Recommendation with rationale.
FINDINGS: State which spec decisions most influenced the recommendation. Note any
          spec gaps that made option comparison difficult.
AMEND: Flag any design question the proposal had to resolve that the spec left open.
       These are forward-contamination risks — note them explicitly.
WRITE: simulations/draft/proposals/{topic}-proposal-{date}.md
GATE: Do not begin Artifact 3 until this file is written.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 3 — PITCH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SETUP: Read the proposal. Identify the recommended option. Pull from
       scout-positioning if available.
EXECUTE: Author pitch in exec, developer, and maker versions. Each version: hook,
         what it does, why it matters, call to action. Anti-positioning section.
         Exec version leads with the outcome of the recommended option.
         Dev version references the technical design from the spec.
         Maker version uses no jargon from the spec.
FINDINGS: State what conviction each version establishes that the previous artifacts
          did not. Note any content you nearly duplicated from spec or proposal.
AMEND: List one thing each version could improve if a specific scout signal existed.
WRITE: simulations/draft/pitches/{topic}-pitch-{date}.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 4: CAMPAIGN CLOSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
List: artifacts written, scout signals consumed, open questions remaining,
and which signal namespace would resolve each open question.
```

---

## V-04 — Phrasing Register + Inertia Framing (Combination)

**Hypothesis:** A conversational, imperative register ("Do this. Then do this.") reduces
ambiguity for the model about what to execute next. Foregrounding inertia — "what happens
if we don't ship this?" — at the campaign level ensures the pitch's "why it matters"
is grounded in real cost-of-doing-nothing rather than feature enthusiasm.

```
You are running /campaign-blueprint for: {topic}

Three artifacts. One topic. One sequence. Don't skip ahead.

BEFORE YOU START — name the inertia baseline:
What does the user do today without this feature? That's the competition.
Every "why it matters" in every artifact must be grounded in this baseline.
Write it down in one sentence before you write anything else.

---

ARTIFACT 1 — SPEC
Write the spec. Don't start the proposal until this is done and written to disk.

Cover: purpose (what and why, anchored to the inertia baseline), requirements
(pull from scout-requirements if it exists), design (how it works), constraints
(what limits what), open questions (what you don't know yet).

One self-review pass when you finish: is every requirement traceable to the inertia
baseline? Is the design specific enough that a senior engineer could start from it?

Path: simulations/draft/specs/{topic}-spec-{date}.md

---

ARTIFACT 2 — PROPOSAL
Read the spec you just wrote. Now write the proposal.

Give three options minimum — and one of them has to be do-nothing. Do-nothing is
not a throwaway option. Describe it honestly: what does the team keep doing, what
cost do they keep paying, what opportunity stays closed? That's your inertia case.

For each option: what it is, what's good, what's bad, what it risks, how hard it is.
Pick one. Say why. Ground the recommendation in the spec's design and constraints —
don't re-invent anything the spec already decided.

Path: simulations/draft/proposals/{topic}-proposal-{date}.md

---

ARTIFACT 3 — PITCH
Read the proposal. You know the recommended option. Now write the pitch.

Three versions — exec, dev, maker. Different words, same conviction.

Exec: start with the cost of inertia. What keeps happening if we don't ship?
Then: what the recommended option changes, why it changes it, what they need to approve.

Dev: show the tool. What can an engineer do with this that they couldn't before?
Reference the technical design from the spec. No business jargon.

Maker: plain language only. "Can I build this?" "How long does it take?"
No spec terminology. No proposal jargon. Just: here's what changed, here's why
that matters for you, here's how to start.

Close each version with a clear call to action.
Add an anti-positioning section: what this is NOT, so it doesn't get mis-sold.

Path: simulations/draft/pitches/{topic}-pitch-{date}.md

---

WRAP UP
List what you wrote, where it is, and what questions came up that a future signal
could answer. Keep it short — one line per item.
```

---

## V-05 — Full Integration (Role Sequence + Format + Lifecycle + Register + Inertia)

**Hypothesis:** Combining explicit role assignment, gated lifecycle phases, a structural
format contract, conversational register, and a persistent inertia thread produces
the most coherent campaign output — each artifact builds directly on the last, the
inertia framing is consistent across all three, and no phase can be skipped because
each gate requires a written file before the next begins.

```
You are running /campaign-blueprint for: {topic}

Produce a complete specification package: spec, proposal, and pitch, in that order.
Each artifact must be written to disk before the next begins.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Role: Strategy + PM.

Before writing anything, establish:
1. Topic identity — one sentence: what feature, for whom, solving what.
2. Inertia baseline — one sentence: what users do today without this feature.
   This is the primary competitor for all three artifacts.
3. Scout signals — glob simulations/scout/ for this topic. List what exists.
   Note: spec will pull scout-requirements, proposal will pull scout-feasibility,
   pitch will pull scout-positioning, if each exists.

Print the setup block. Do not begin Artifact 1 until it is complete.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 1: SPEC
Role: Architect
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Sections (all required):

PURPOSE
  What this feature does and why it exists. Anchor to the inertia baseline.
  One paragraph.

REQUIREMENTS
  Bulleted, MoSCoW-tagged (M/S/C/W). Pull from scout-requirements if available.
  Each Must-have requirement maps directly to the inertia baseline.

DESIGN
  How it works. Components, data flow, key decisions. Specific enough to start from.

CONSTRAINTS
  Technical, team, timeline, and dependency limits that bound the design space.

OPEN QUESTIONS
  What you don't know. For each: which signal namespace could resolve it.

Self-review: flag any requirement not anchored to the inertia baseline as a scope risk.

GATE: Write simulations/draft/specs/{topic}-spec-{date}.md before continuing.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 2: PROPOSAL
Role: Architect (technical options) + PM (business trade-offs)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Read the spec. Pull from scout-feasibility if available.

Produce three options minimum. Option A must be do-nothing (inertia) — describe it
honestly with real cost. For each option provide:

  Name | Description | Pros | Cons | Risk (H/M/L) | Effort (S/M/L)

Recommendation:
  State the chosen option. Give three reasons. Every reason must reference a spec
  decision or constraint — no new design work here. State explicitly what the
  do-nothing option keeps costing.

Do not re-open any design question the spec resolved.

GATE: Write simulations/draft/proposals/{topic}-proposal-{date}.md before continuing.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 3: PITCH
Role: PM + Strategy
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Read the proposal. The recommended option is the subject of the pitch.
Pull from scout-positioning if available.

Three versions — write each in full:

EXEC VERSION (audience: decision-makers)
  Hook: cost of inertia — what keeps happening without this?
  What it does: business-level outcome from the recommended option.
  Why it matters: risk of continued inertia (from do-nothing option in proposal).
  Call to action: specific ask (approve, fund, unblock).

DEVELOPER VERSION (audience: engineers and technical leads)
  Hook: capability unlocked — what can you build that you couldn't before?
  What it does: reference the technical design from the spec.
  Why it matters: technical debt or opportunity cost of the current approach.
  Call to action: join beta / review the spec / contribute.

MAKER VERSION (audience: practitioners, no jargon)
  Hook: the friction you feel today (from inertia baseline).
  What it does: plain language only. No spec or proposal terminology.
  Why it matters: time saved, steps removed, frustration resolved.
  Call to action: try it / sign up / start now.

Anti-positioning (shared across all three):
  What this feature is NOT. Prevent mis-selling in two sentences.

GATE: Write simulations/draft/pitches/{topic}-pitch-{date}.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN CLOSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Artifact | Path | Scout signal consumed | Open questions |
|----------|------|-----------------------|---------------|
| Spec | simulations/draft/specs/... | (signal or none) | (list) |
| Proposal | simulations/draft/proposals/... | (signal or none) | (list) |
| Pitch | simulations/draft/pitches/... | (signal or none) | (list) |

List any open questions from across all three artifacts that a future signal could
resolve, with the recommended namespace for each.
```

---

## Variation Summary

| ID | Axis | Hypothesis shorthand |
|----|------|----------------------|
| V-01 | Role sequence | Front-load Strategy brief to lock topic identity early |
| V-02 | Output format | Tables enforce field coverage; harder to drop a required field |
| V-03 | Lifecycle emphasis | Explicit gates prevent out-of-order contamination (C-04 risk) |
| V-04 | Register + inertia | Conversational + do-nothing-is-real-cost anchors "why it matters" |
| V-05 | Full integration | Role + format + lifecycle + register + inertia in one prompt |
