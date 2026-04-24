---
skill: quest-variate
skill_target: campaign-blueprint
date: 2026-03-16
round: 3
rubric: campaign-blueprint-rubric-v3-2026-03-16.md
---

# campaign-blueprint — Prompt Variations R3

Five complete, runnable skill body variations. Single-axis first (V-01 through V-03),
then two combinations (V-04, V-05).

## R3 Context

R2 closed all essential and recommended gaps. All five R2 variations were Golden.
The R2 diagnostic codified two new aspirational criteria in v3:

- **C-15 (Artifact contract)**: READ/WRITE/PRESERVE/CARRIES FORWARD declared before execution.
  V-01 R2 introduced this pattern; it now earns 5 pts when all four fields are present for all
  three artifacts.
- **C-16 (Post-execution FINDINGS)**: labeled FINDINGS block written after the pitch, not before.
  V-02 and V-05 R2 earned PARTIAL because their conviction content was pre-execution (checklist /
  BEFORE WRITING). The label and post-execution placement are structural requirements.

Under v3, a variation that passes C-15 and C-16 in addition to all R2 patterns scores 118.
No R2 variation was evaluated against v3 at time of scoring. R3 tests which prompt mechanisms
most reliably deliver C-15 and C-16 full credit.

**R3 variation axes:**
- V-01: Contract matrix format — all three contracts declared in a single table during setup
- V-02: FINDINGS template — structured sub-fields replace open conviction prompt
- V-03: Carries-forward cascade — CF declared at artifact close rather than pre-execution matrix
- V-04: Contract matrix + FINDINGS template (combination of V-01 + V-02)
- V-05: Carries-forward cascade + FINDINGS template + minimal density (V-03 + V-02 + R2 V-03 skeleton)

---

## V-01 — Contract Matrix Axis

**Hypothesis:** Declaring all three artifact contracts as a single matrix during campaign setup —
before any execution begins — makes the full READ/WRITE/PRESERVE/CARRIES FORWARD dependency
chain visible at a glance. This reduces the per-artifact word cost of C-15 compliance
and maximizes the chance that PRESERVES (C-06) and CARRIES FORWARD (C-07) are honored
by the executor who sees obligations grouped rather than buried in each section.

```
You are running /campaign-blueprint for: {topic}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Before writing anything, establish:

1. Topic identity — one sentence: feature name, audience, problem solved.
2. Inertia baseline — one sentence: what users do today without this feature.
3. Scout inventory — glob simulations/scout/ for this topic now. List every file
   found, organized by namespace. This is not conditional on signal existence.

4. Artifact contract matrix — declare all obligations before any artifact begins:

| Field           | Spec                                                    | Proposal                                                      | Pitch                                                              |
|-----------------|---------------------------------------------------------|---------------------------------------------------------------|--------------------------------------------------------------------|
| READ            | Topic identity; inertia baseline; scout-requirements if found | Spec file; scout-feasibility if found                    | Proposal file; scout-positioning if found                          |
| WRITE           | simulations/draft/specs/{topic}-spec-{date}.md          | simulations/draft/proposals/{topic}-proposal-{date}.md        | simulations/draft/pitches/{topic}-pitch-{date}.md                  |
| PRESERVE        | (first artifact — no prior decisions)                   | All spec design decisions and constraints                     | Recommended option from proposal; all spec decisions               |
| CARRIES FORWARD | Feature identity; inertia baseline; design decisions    | Recommended option name and rationale; do-nothing cost stated | Conviction established per audience version                        |

Print the completed contract matrix in full. Do not begin Artifact 1 until it is printed.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 1: SPEC
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Write the technical specification. Sections required:

  PURPOSE        — What this feature does and why it exists. Anchor to the inertia baseline.
  REQUIREMENTS   — Bulleted, MoSCoW-tagged (M/S/C/W). Pull scout-requirements if available.
                   Each Must-have traces to the inertia baseline.
  DESIGN         — How it works: components, data flow, key decisions. Specific enough to start from.
  CONSTRAINTS    — Technical, team, timeline, and dependency limits.
  OPEN QUESTIONS — What you do not know. For each: which signal namespace could resolve it.

GATE: Do not begin Artifact 2 until simulations/draft/specs/{topic}-spec-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 2: PROPOSAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Read the spec. PRESERVES: do not re-open any design question the spec resolved or
introduce new design work. Pull scout-feasibility if available.

Three options minimum. Option A must be do-nothing — state the inertia cost honestly.
Per option: Name / Description / Pros / Cons / Risk (H/M/L) / Effort (S/M/L).

Recommendation: state the chosen option. Give three reasons. Every reason must reference
a spec decision or constraint — no new analysis here.

GATE: Do not begin Artifact 3 until simulations/draft/proposals/{topic}-proposal-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 3: PITCH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Read the proposal. CARRIES FORWARD: the recommended option from the proposal is the
subject of all three pitch versions. Pull scout-positioning if available.

Write three pitch versions in full:

EXEC VERSION (decision-makers)
  Hook: cost of inertia — what keeps happening without this?
  What it does: business-level outcome from the recommended option.
  Why it matters: risk of continued inertia.
  CTA: specific ask — approve, fund, or unblock.

DEV VERSION (engineers and technical leads)
  Hook: capability unlocked — what can you build that you could not before?
  What it does: references the technical design from the spec explicitly.
  Why it matters: technical debt or opportunity cost of the current approach.
  CTA: join beta / review the spec / contribute.

MAKER VERSION (practitioners — plain language only)
  Hook: the friction you feel today.
  What it does: plain language only. No spec terminology. No proposal jargon.
  Why it matters: time saved, steps removed, frustration resolved.
  CTA: try it / sign up / start now.

ANTI-POSITIONING (shared across all three versions): what this feature is NOT, in two sentences.

Write simulations/draft/pitches/{topic}-pitch-{date}.md

FINDINGS (write this block after the pitch file is written, not before):
State what conviction each version establishes that the spec and proposal did not.
Note any content you nearly duplicated from spec or proposal — name it explicitly.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN CLOSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Artifact | Path                                                         | Scout signal consumed | Open questions |
|----------|--------------------------------------------------------------|-----------------------|----------------|
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md               | (namespace or none)   | (list)         |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md       | (namespace or none)   | (list)         |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md            | (namespace or none)   | (list)         |

List any open question a future signal could resolve, with recommended namespace for each.
```

---

## V-02 — FINDINGS Template Axis

**Hypothesis:** An explicit FINDINGS template with named sub-fields — CONVICTION DELTA /
NEAR-DUPLICATE CONTENT / RESIDUAL QUESTIONS — produces a richer, more reliably post-execution
reflection than an open "state what conviction..." prompt. Named sub-fields make it harder to
write the block pre-execution (because CONVICTION DELTA asks per-version, requiring the
completed pitch to exist), and harder to satisfy with checklist items (because each sub-field
demands narrative content, not a checkbox). This targets C-16 full credit and C-13 full credit
simultaneously, while keeping READ/WRITE/PRESERVE/CARRIES FORWARD as per-artifact inline
declarations for C-15.

```
You are running /campaign-blueprint for: {topic}

CAMPAIGN SETUP
Run before any artifact:

  Topic identity: one sentence — feature name, audience, problem solved.
  Inertia baseline: one sentence — what exists today without this feature.
  Scout inventory: glob simulations/scout/ for this topic. List all files by namespace.
    Run this now — not conditionally.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 1: SPEC
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

READ:            Topic identity; inertia baseline; scout-requirements if found in inventory.
WRITE:           simulations/draft/specs/{topic}-spec-{date}.md
PRESERVE:        (first artifact — no prior decisions to protect)
CARRIES FORWARD: Feature identity; inertia baseline; design decisions; open questions.

Sections (all required):
  PURPOSE        — Problem statement anchored to the inertia baseline. One paragraph.
  REQUIREMENTS   — Bulleted, MoSCoW-tagged. Each Must-have maps to the inertia baseline.
  DESIGN         — Components, data flow, key decisions. Specific enough to start from.
  CONSTRAINTS    — Technical, team, timeline, and dependency limits.
  OPEN QUESTIONS — What you do not know. Recommended namespace to resolve each.

GATE: Do not begin Artifact 2 until this file is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 2: PROPOSAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

READ:            Spec file above; scout-feasibility if found in inventory.
WRITE:           simulations/draft/proposals/{topic}-proposal-{date}.md
PRESERVE:        All spec design decisions and constraints — do not re-open anything the spec resolved.
CARRIES FORWARD: Recommended option name and rationale; do-nothing cost stated explicitly.

Three options minimum. Option A must be do-nothing — state the inertia cost honestly.
Per option: Name / Description / Pros / Cons / Risk (H/M/L) / Effort (S/M/L).
Recommendation: chosen option + three reasons, each citing a spec decision or constraint.

GATE: Do not begin Artifact 3 until this file is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 3: PITCH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

READ:            Proposal file above; scout-positioning if found in inventory.
WRITE:           simulations/draft/pitches/{topic}-pitch-{date}.md
PRESERVE:        Recommended option from proposal — pitch crystallizes this choice, does not reopen it.
CARRIES FORWARD: (final artifact)

Three versions in full:

EXEC: cost-of-inertia hook / recommended option outcome / risk of continued inertia / CTA: approve or fund.
DEV: capability hook / references technical design from spec / opportunity cost of current approach / CTA: join beta.
MAKER: friction-today hook / plain language only — no spec or proposal terminology / time saved / CTA: try it.
Shared: ANTI-POSITIONING section — what this is NOT, in two sentences.

Write the pitch file. Then write the FINDINGS block below.

FINDINGS (write after the pitch file is complete):

  CONVICTION DELTA
    Exec version: what conviction does this version establish that the spec and proposal did not?
    Dev version: what conviction does this version establish that the spec and proposal did not?
    Maker version: what conviction does this version establish that the spec and proposal did not?

  NEAR-DUPLICATE CONTENT
    Name any passage you nearly copied from the spec or proposal.
    State what you changed to make it conviction-bearing rather than informational.

  RESIDUAL QUESTIONS
    What would a specific scout signal resolve that no artifact could answer from existing evidence?
    Recommend a namespace for each.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN CLOSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Artifact | Path                                                         | Scout signal consumed | Open questions |
|----------|--------------------------------------------------------------|-----------------------|----------------|
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md               | (namespace or none)   | (list)         |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md       | (namespace or none)   | (list)         |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md            | (namespace or none)   | (list)         |
```

---

## V-03 — Carries-Forward Cascade Axis

**Hypothesis:** Declaring CARRIES FORWARD at the close of each artifact — after execution, as a
handoff declaration the next artifact reads — rather than in a pre-execution matrix produces
stronger C-07 compliance. The pitch executor sees the Proposal's CARRIES FORWARD immediately
before starting, not a matrix written twenty lines above. This tests whether proximity of the
handoff declaration to its consumer matters more than completeness of the upfront contract.
The GATE fires after the CARRIES FORWARD declaration, enforcing that inheritance is visible
before blocking clears.

```
You are running /campaign-blueprint for: {topic}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Topic identity: one sentence — feature name, audience, problem solved.
2. Inertia baseline: one sentence — what users do today without this feature.
3. Scout inventory: glob simulations/scout/ for this topic now. List every file by namespace.
   Unconditional — run regardless of whether signals exist.

Artifact paths:
  Spec:     simulations/draft/specs/{topic}-spec-{date}.md
  Proposal: simulations/draft/proposals/{topic}-proposal-{date}.md
  Pitch:    simulations/draft/pitches/{topic}-pitch-{date}.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 1: SPEC
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

READ:     Topic identity; inertia baseline; scout-requirements if found.
PRESERVE: (first artifact — no prior decisions)

Write sections: PURPOSE / REQUIREMENTS (MoSCoW-tagged) / DESIGN / CONSTRAINTS / OPEN QUESTIONS.
Each Must-have requirement anchored to the inertia baseline.

Write simulations/draft/specs/{topic}-spec-{date}.md

CARRIES FORWARD (state these values before the GATE fires):
  Feature identity: [state it]
  Inertia baseline: [state it]
  Design decisions that constrain options: [list the key ones]
  Open questions that affect option viability: [list]

GATE: Do not begin Artifact 2 until this file is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 2: PROPOSAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

READ:     CARRIES FORWARD from Spec above; scout-feasibility if found.
PRESERVE: All spec design decisions and constraints — do not re-open anything the spec resolved;
          do not introduce new design work.

Three options minimum. Option A must be do-nothing — describe the inertia cost honestly.
Per option: Name / Description / Pros / Cons / Risk (H/M/L) / Effort (S/M/L).
Recommendation: chosen option + three reasons, each citing a spec decision or constraint.

Write simulations/draft/proposals/{topic}-proposal-{date}.md

CARRIES FORWARD (state these values before the GATE fires):
  Recommended option: [name it]
  Recommendation rationale: [one sentence per reason, citing spec decisions]
  Do-nothing cost: [state it — this feeds the pitch's exec hook]
  Scout signal consumed: [namespace or none]

GATE: Do not begin Artifact 3 until this file is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 3: PITCH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

READ:     CARRIES FORWARD from Proposal above; scout-positioning if found.
PRESERVE: Recommended option — pitch crystallizes this choice and does not reopen it.

Write three versions in full:

EXEC VERSION
  Hook: do-nothing cost from the CARRIES FORWARD above.
  What it does: outcome from the recommended option.
  Why it matters: risk if inertia continues.
  CTA: approve / fund / unblock.

DEV VERSION
  Hook: capability unlocked.
  What it does: references the technical design from the spec explicitly.
  Why it matters: technical debt or opportunity cost of today's approach.
  CTA: join beta / review the spec / contribute.

MAKER VERSION
  Hook: friction from the inertia baseline.
  What it does: plain language only — no spec terminology, no proposal jargon.
  Why it matters: time saved, steps removed, frustration resolved.
  CTA: try it / sign up / start now.

ANTI-POSITIONING (shared): what this feature is NOT, in two sentences.

Write simulations/draft/pitches/{topic}-pitch-{date}.md

FINDINGS (write this block after the pitch file is written, not before):
State what conviction each version establishes that the spec and proposal did not.
Note any content you nearly duplicated from spec or proposal — name it explicitly.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN CLOSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Artifact | Path                                                         | Scout signal consumed | Open questions |
|----------|--------------------------------------------------------------|-----------------------|----------------|
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md               | (namespace or none)   | (list)         |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md       | (namespace or none)   | (list)         |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md            | (namespace or none)   | (list)         |
```

---

## V-04 — Contract Matrix + FINDINGS Template (Combination: V-01 + V-02)

**Hypothesis:** A pre-execution contract matrix (V-01 axis) and a structured FINDINGS template
(V-02 axis) are complementary, not competing. The matrix declares obligations before execution,
making C-15 maximally visible. The FINDINGS template's named sub-fields ensure post-execution
reflection is structurally distinct from any pre-execution block, satisfying C-16 with the
specific label and timing required. Combined, they remove ambiguity at both ends of the
artifact lifecycle — what must be honored going in, and what must be reflected after completion.

```
You are running /campaign-blueprint for: {topic}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Before writing anything, establish:

1. Topic identity — one sentence: feature name, audience, problem solved.
2. Inertia baseline — one sentence: what users do today without this feature.
   This is the primary competitor for all three artifacts.
3. Scout inventory — glob simulations/scout/ for this topic now. List every file by namespace.
   Not conditional. Run regardless of whether signals are found.

4. Artifact contract matrix:

| Field           | Spec                                                    | Proposal                                                          | Pitch                                                         |
|-----------------|---------------------------------------------------------|-------------------------------------------------------------------|---------------------------------------------------------------|
| READ            | Topic identity; inertia baseline; scout-requirements if found | Spec file; scout-feasibility if found                       | Proposal file; scout-positioning if found                     |
| WRITE           | simulations/draft/specs/{topic}-spec-{date}.md          | simulations/draft/proposals/{topic}-proposal-{date}.md            | simulations/draft/pitches/{topic}-pitch-{date}.md             |
| PRESERVE        | (first artifact)                                        | All spec design decisions — no re-opening, no new design work     | Recommended option from proposal — pitch crystallizes, not reconsiders |
| CARRIES FORWARD | Feature identity; inertia baseline; design decisions    | Recommended option name and rationale; do-nothing cost            | (final artifact)                                              |

Print the contract matrix. Do not begin Artifact 1 until it is printed.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 1: SPEC
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Sections (all required):

  PURPOSE        — Problem and why it exists. Anchor to the inertia baseline.
  REQUIREMENTS   — Bulleted, MoSCoW-tagged (M/S/C/W). Pull scout-requirements if available.
                   Each Must-have traces to the inertia baseline.
  DESIGN         — Components, data flow, key decisions. Specific enough to start from.
  CONSTRAINTS    — Technical, team, timeline, and dependency limits.
  OPEN QUESTIONS — What you do not know. Which namespace could resolve each.

GATE: Do not begin Artifact 2 until simulations/draft/specs/{topic}-spec-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 2: PROPOSAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Read the spec. PRESERVES: do not re-open any design question the spec resolved.
Pull scout-feasibility if available.

Three options minimum. Option A: do-nothing — state the inertia cost honestly.
Per option: Name / Description / Pros / Cons / Risk (H/M/L) / Effort (S/M/L).
Recommendation: chosen option + three reasons, each citing a spec decision or constraint.

GATE: Do not begin Artifact 3 until simulations/draft/proposals/{topic}-proposal-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 3: PITCH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Read the proposal. CARRIES FORWARD: the recommended option is the subject of all three versions.
Pull scout-positioning if available.

Three versions in full:

EXEC (decision-makers):
  Hook: inertia cost — what keeps happening without this?
  What it does: business outcome from the recommended option.
  Why it matters: risk of continued inertia.
  CTA: approve / fund / unblock.

DEV (engineers and technical leads):
  Hook: capability unlocked.
  What it does: references the technical design from the spec explicitly.
  Why it matters: technical debt or opportunity cost.
  CTA: join beta / review spec / contribute.

MAKER (practitioners — plain language only):
  Hook: friction from the inertia baseline.
  What it does: no spec terminology, no proposal jargon.
  Why it matters: time saved, steps removed.
  CTA: try it / sign up / start now.

ANTI-POSITIONING (shared): what this feature is NOT, two sentences.

Write simulations/draft/pitches/{topic}-pitch-{date}.md

FINDINGS (write this block after the pitch file is complete — not before, not during):

  CONVICTION DELTA
    Exec version: what conviction does this version establish that the spec and proposal did not?
    Dev version: what conviction does this version establish that the spec and proposal did not?
    Maker version: what conviction does this version establish that the spec and proposal did not?

  NEAR-DUPLICATE CONTENT
    Name any passage you nearly copied from the spec or proposal.
    State what you changed to make it conviction-bearing rather than informational.

  RESIDUAL QUESTIONS
    What would a specific scout signal resolve that no artifact answered from existing evidence?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN CLOSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Artifact | Path                                                         | Scout signal consumed | Open questions |
|----------|--------------------------------------------------------------|-----------------------|----------------|
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md               | (namespace or none)   | (list)         |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md       | (namespace or none)   | (list)         |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md            | (namespace or none)   | (list)         |
```

---

## V-05 — Cascade + FINDINGS Template + Minimal Density (Combination: V-03 + V-02 + R2 V-03 skeleton)

**Hypothesis:** R2 V-03 (Minimal Density) tied for highest score with ~40% fewer words than V-04.
The trigger phrases carry the weight; ceremony is optional. R3 tests whether the same principle
applies to C-15 and C-16: can CARRIES FORWARD cascade declarations and a structured FINDINGS
template be expressed at minimal word count without losing structural signal? This variation
takes the R2 V-03 skeleton, adds per-artifact CF cascade at close time (V-03 axis), and
replaces the open FINDINGS prompt with named sub-fields (V-02 axis) — all at maximum density.

```
You are running /campaign-blueprint for: {topic}

SETUP — run before Artifact 1:
  Topic identity: one sentence.
  Inertia baseline: one sentence.
  Glob simulations/scout/ for this topic now. List all files by namespace. Unconditional.

---

ARTIFACT 1: SPEC
READ: topic identity; inertia baseline; scout-requirements if found.
PRESERVE: (first artifact)

Sections: PURPOSE / REQUIREMENTS (MoSCoW) / DESIGN / CONSTRAINTS / OPEN QUESTIONS
Each Must-have anchored to the inertia baseline.

Write simulations/draft/specs/{topic}-spec-{date}.md

CARRIES FORWARD to Proposal:
  Feature identity; inertia baseline; design decisions; open questions affecting option space.

GATE: Do not begin Artifact 2 until this file is written to disk.

---

ARTIFACT 2: PROPOSAL
READ: CARRIES FORWARD from Spec; scout-feasibility if found.
PRESERVE: all spec design decisions — do not re-open anything the spec resolved.

Three options min including do-nothing (honest inertia cost).
Per option: Name / Description / Pros / Cons / Risk (H/M/L) / Effort (S/M/L).
Recommendation: chosen option + three reasons citing spec decisions or constraints.

Write simulations/draft/proposals/{topic}-proposal-{date}.md

CARRIES FORWARD to Pitch:
  Recommended option: [name]; Rationale: [one sentence]; Do-nothing cost: [one sentence].
  Scout signal consumed: [namespace or none].

GATE: Do not begin Artifact 3 until this file is written to disk.

---

ARTIFACT 3: PITCH
READ: CARRIES FORWARD from Proposal; scout-positioning if found.
PRESERVE: recommended option — crystallize it, do not reopen the choice.

EXEC: inertia-cost hook / recommended option outcome / risk of inertia / CTA: approve or fund.
DEV: capability hook / references technical design from spec / opportunity cost / CTA: join beta.
MAKER: friction hook / plain language only, no spec or proposal terminology / time saved / CTA: try it.
Shared: ANTI-POSITIONING — what this is NOT, two sentences.

Write simulations/draft/pitches/{topic}-pitch-{date}.md

FINDINGS (write after the pitch is written):

  CONVICTION DELTA
    Exec: what conviction does this establish that spec and proposal did not?
    Dev: what conviction does this establish that spec and proposal did not?
    Maker: what conviction does this establish that spec and proposal did not?

  NEAR-DUPLICATE CONTENT
    Name any passage nearly copied from spec or proposal.
    State what changed to make it conviction-bearing.

---

CAMPAIGN CLOSE

| Artifact | Path                                                         | Scout signal consumed | Open questions |
|----------|--------------------------------------------------------------|-----------------------|----------------|
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md               | (namespace or none)   | (list)         |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md       | (namespace or none)   | (list)         |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md            | (namespace or none)   | (list)         |
```

---

## Variation Summary

| ID   | Axis                                         | Hypothesis shorthand                                                                   |
|------|----------------------------------------------|----------------------------------------------------------------------------------------|
| V-01 | Contract matrix                              | Upfront matrix makes all three contracts visible before execution — reduces per-artifact overhead |
| V-02 | FINDINGS template                            | Named sub-fields (CONVICTION DELTA / NEAR-DUPLICATE / RESIDUAL) force post-execution placement |
| V-03 | Carries-forward cascade                      | CF at artifact close, not upfront matrix — proximity to consumer matters for C-07 enforcement |
| V-04 | Contract matrix + FINDINGS template          | Pre-execution visibility (C-15) + post-execution structure (C-16) are complementary |
| V-05 | Cascade + FINDINGS template + minimal density| R2 V-03 density principle applied to C-15/C-16: trigger phrases carry weight, ceremony is optional |

## C-15 / C-16 Coverage by Variation

| ID   | C-15 mechanism                                         | C-16 mechanism                                           |
|------|--------------------------------------------------------|----------------------------------------------------------|
| V-01 | Matrix with all four fields for all three artifacts    | Labeled FINDINGS block, post-execution placement explicit |
| V-02 | Per-artifact inline READ/WRITE/PRESERVE/CF             | FINDINGS template with named sub-fields, label + placement |
| V-03 | Per-artifact inline READ/PRESERVE + CF at close        | Labeled FINDINGS block, post-execution placement explicit |
| V-04 | Matrix + per-artifact section headers reinforce it     | FINDINGS template with named sub-fields, explicit timing |
| V-05 | Per-artifact inline + CF at close (minimal words)      | FINDINGS template, labeled, triggered post-write        |

## R3 Diagnostic Questions

1. Does contract matrix format (V-01) vs per-artifact inline (V-02, V-03) affect C-15 partial vs full?
2. Does the structured FINDINGS template (V-02, V-04, V-05) produce C-16 full credit more reliably than the open prompt (V-01, V-03)?
3. Does CF cascade at close time (V-03, V-05) vs upfront matrix (V-01, V-04) change C-07 compliance?
4. Does adding the FINDINGS template to the minimal-density skeleton (V-05) add word cost without score benefit, or does the template earn C-16 full credit where an open prompt would earn partial?
