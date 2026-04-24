---
skill: quest-variate
skill_target: campaign-blueprint
date: 2026-03-16
round: 4
rubric: campaign-blueprint-rubric-v4-2026-03-16.md
---

# campaign-blueprint — Prompt Variations R4

Five complete, runnable skill body variations. Single-axis first (V-01 through V-03),
then two combinations (V-04, V-05).

## R4 Context

R3 closed all essential, recommended, and aspirational gaps through v3. V-04 (R3)
became the reference implementation and the first variation to reach the v4 ceiling
of 128 by earning both C-17 and C-18 full credit.

The v4 rubric adds two new aspirational criteria:

- **C-17 (Dual-mechanism defense in depth)**: pre-execution contract with all four
  labeled fields AND a named FINDINGS template. V-04 (R3) earns full credit; all
  other R3 variants earn PARTIAL because either the contract or the template is
  not in its structured form.
- **C-18 (Double-prohibition FINDINGS placement)**: placement instruction explicitly
  prohibits both "before" and "during." V-04 (R3) earns full credit with "not
  before, not during"; all other R3 variants earn PARTIAL (only "after" or equivalent).

**R4 variation axes:**
- V-01: FINDINGS gate separation — FINDINGS moves to its own campaign phase, gated
  after the pitch file is on disk, making the "not before, not during" structural
  rather than instructed
- V-02: Contract anchor reminders — full matrix in setup + condensed READ/PRESERVE
  reminder line at each artifact header, testing whether proximity of contract to
  enforcement point adds reliability over the matrix alone
- V-03: Conviction staging — each artifact declares its conviction type (factual /
  optionality / emotional) in both the matrix and the section header; CONVICTION
  DELTA asks per-version what emotional conviction is new here
- V-04: FINDINGS gate + contract reminders (V-01 + V-02 combination)
- V-05: Conviction staging + FINDINGS gate + minimal density (V-03 + V-01 + R3 V-05
  skeleton)

**R4 diagnostic questions:**
1. Does structural separation of FINDINGS into a named post-pitch phase (V-01, V-04,
   V-05) produce stronger C-18 reliability than inline double-prohibition language
   (V-02, V-03)?
2. Does per-artifact contract reminder (V-02, V-04) add measurable reliability over
   the matrix alone — or does the matrix already carry the obligation to the executor?
3. Does conviction-type labeling (V-03, V-05) improve narrative arc (C-09) and
   CONVICTION DELTA quality (C-13) beyond what the template structure achieves?
4. Does the minimal-density version (V-05) reach 128 with fewer words, or do the
   structural elements (matrix row + phase header + named sub-fields) impose a
   minimum word threshold below which one or more criteria slip to PARTIAL?

---

## V-01 — FINDINGS Gate Axis

**Hypothesis:** The surest path to C-18 full credit is architectural, not instructional.
If FINDINGS lives in its own named campaign phase — gated behind "Do not begin Campaign
Reflection until the pitch file is written to disk" — the "not before, not during"
constraint is enforced by phase ordering, not by a clause the executor might overlook
inside the artifact section. Spatial separation across phase boundaries is a stronger
C-18 mechanism than an inline prohibition sentence. The phase header can then state the
double prohibition as a description of the phase structure ("begins only after the pitch
file exists on disk — not before production begins, not during production") rather than
as an imperative instruction to the executor.

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

4. Artifact contract matrix — declare all obligations before execution begins:

| Field           | Spec                                                    | Proposal                                                          | Pitch                                                         |
|-----------------|---------------------------------------------------------|-------------------------------------------------------------------|---------------------------------------------------------------|
| READ            | Topic identity; inertia baseline; scout-requirements if found | Spec file; scout-feasibility if found                       | Proposal file; scout-positioning if found                     |
| WRITE           | simulations/draft/specs/{topic}-spec-{date}.md          | simulations/draft/proposals/{topic}-proposal-{date}.md            | simulations/draft/pitches/{topic}-pitch-{date}.md             |
| PRESERVE        | (first artifact)                                        | All spec design decisions — no re-opening, no new design work     | Recommended option from proposal — crystallize, do not reconsider |
| CARRIES FORWARD | Feature identity; inertia baseline; design decisions    | Recommended option name and rationale; do-nothing cost            | (final artifact)                                              |

Print the contract matrix in full. Do not begin Artifact 1 until it is printed.

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

GATE: Do not begin Campaign Reflection until simulations/draft/pitches/{topic}-pitch-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN REFLECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This phase begins only after the pitch file exists on disk — not before pitch production begins,
not during pitch production. What follows is reflection on a completed artifact, not intent
declaration or progress annotation.

FINDINGS:

  CONVICTION DELTA
    Exec version: what conviction does this version establish that the spec and proposal did not?
    Dev version: what conviction does this version establish that the spec and proposal did not?
    Maker version: what conviction does this version establish that the spec and proposal did not?

  NEAR-DUPLICATE CONTENT
    Name any passage you nearly copied from the spec or proposal.
    State what you changed to make it conviction-bearing rather than informational.

  RESIDUAL QUESTIONS
    What would a specific scout signal resolve that no artifact answered from existing evidence?
    Recommend a namespace for each.

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

## V-02 — Contract Anchor Reminders Axis

**Hypothesis:** The contract matrix (R3 V-04) declares all obligations upfront, but
executor compliance may erode as distance from the matrix grows — the pitch executor
may not recall the PRESERVE obligation printed forty lines above. Per-artifact contract
reminder lines — a condensed READ / PRESERVE row pulled directly from the matrix —
test whether proximity of obligation to its enforcement point adds reliability without
abandoning the upfront visibility benefit. The matrix still earns C-15 full credit; the
reminder lines are not a substitute but an anchor repetition. The double-prohibition
FINDINGS language ("not before, not during") is retained inline in the pitch section, as
in R3 V-04, to isolate the reminder-line variable cleanly.

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

4. Artifact contract matrix — declare all obligations before execution begins:

| Field           | Spec                                                    | Proposal                                                          | Pitch                                                         |
|-----------------|---------------------------------------------------------|-------------------------------------------------------------------|---------------------------------------------------------------|
| READ            | Topic identity; inertia baseline; scout-requirements if found | Spec file; scout-feasibility if found                       | Proposal file; scout-positioning if found                     |
| WRITE           | simulations/draft/specs/{topic}-spec-{date}.md          | simulations/draft/proposals/{topic}-proposal-{date}.md            | simulations/draft/pitches/{topic}-pitch-{date}.md             |
| PRESERVE        | (first artifact)                                        | All spec design decisions — no re-opening, no new design work     | Recommended option from proposal — crystallize, do not reconsider |
| CARRIES FORWARD | Feature identity; inertia baseline; design decisions    | Recommended option name and rationale; do-nothing cost            | (final artifact)                                              |

Print the contract matrix in full. Do not begin Artifact 1 until it is printed.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 1: SPEC
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: topic identity; inertia baseline; scout-requirements if found.
                    PRESERVE: (first artifact — no prior decisions to protect)

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
Contract reminder — READ: spec file; scout-feasibility if found.
                    PRESERVE: all spec design decisions — do not re-open anything the spec resolved.

Three options minimum. Option A: do-nothing — state the inertia cost honestly.
Per option: Name / Description / Pros / Cons / Risk (H/M/L) / Effort (S/M/L).
Recommendation: chosen option + three reasons, each citing a spec decision or constraint.

GATE: Do not begin Artifact 3 until simulations/draft/proposals/{topic}-proposal-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 3: PITCH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: proposal file; scout-positioning if found.
                    CARRIES FORWARD: recommended option is the subject of all three pitch versions.

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
    Recommend a namespace for each.

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

## V-03 — Conviction Staging Axis

**Hypothesis:** The three artifacts produce structurally different types of conviction:
the spec builds factual conviction (what is true), the proposal builds optionality
conviction (which trade-off is worth taking), the pitch builds emotional conviction
(why to act now, per audience). Declaring conviction type as a fifth contract matrix row
and repeating it in each artifact section header does two things: it prevents the pitch
executor from re-arguing facts the spec established (C-09 anti-duplication), and it
frames the CONVICTION DELTA audit as a typed question — "what emotional conviction does
this version establish that the factual and optionality artifacts could not?" — which is
more precise than the open "what conviction does this add?" prompt and makes C-13
content more reliable.

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

4. Artifact contract matrix — declare all obligations before execution begins:

| Field           | Spec                                                    | Proposal                                                          | Pitch                                                              |
|-----------------|---------------------------------------------------------|-------------------------------------------------------------------|--------------------------------------------------------------------|
| READ            | Topic identity; inertia baseline; scout-requirements if found | Spec file; scout-feasibility if found                       | Proposal file; scout-positioning if found                          |
| WRITE           | simulations/draft/specs/{topic}-spec-{date}.md          | simulations/draft/proposals/{topic}-proposal-{date}.md            | simulations/draft/pitches/{topic}-pitch-{date}.md                  |
| PRESERVE        | (first artifact)                                        | All spec design decisions — no re-opening, no new design work     | Recommended option from proposal — crystallize, do not reconsider  |
| CARRIES FORWARD | Feature identity; inertia baseline; design decisions    | Recommended option name and rationale; do-nothing cost            | (final artifact)                                                   |
| CONVICTION TYPE | Factual — asserts what is true; does not argue          | Optionality — evaluates trade-offs against spec facts             | Emotional — converts factual + optionality into per-audience urgency |

Print the contract matrix in full. Do not begin Artifact 1 until it is printed.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 1: SPEC — Factual Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This artifact asserts what is true about the problem and solution. It does not argue or
persuade — it establishes the factual record that the proposal and pitch draw from.

Sections (all required):

  PURPOSE        — Problem and why it exists. Anchor to the inertia baseline.
  REQUIREMENTS   — Bulleted, MoSCoW-tagged (M/S/C/W). Pull scout-requirements if available.
                   Each Must-have traces to the inertia baseline.
  DESIGN         — Components, data flow, key decisions. Specific enough to start from.
  CONSTRAINTS    — Technical, team, timeline, and dependency limits.
  OPEN QUESTIONS — What you do not know. Which namespace could resolve each.

GATE: Do not begin Artifact 2 until simulations/draft/specs/{topic}-spec-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 2: PROPOSAL — Optionality Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This artifact evaluates options against spec facts; it does not re-assert facts the spec
established. The reader finishes knowing which trade-off is worth taking and why.

Read the spec. PRESERVES: do not re-open any design question the spec resolved.
Pull scout-feasibility if available.

Three options minimum. Option A: do-nothing — state the inertia cost honestly.
Per option: Name / Description / Pros / Cons / Risk (H/M/L) / Effort (S/M/L).
Recommendation: chosen option + three reasons, each citing a spec decision or constraint.

GATE: Do not begin Artifact 3 until simulations/draft/proposals/{topic}-proposal-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 3: PITCH — Emotional Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This artifact converts factual and optionality conviction into per-audience urgency. It
does not re-argue facts or re-litigate options — both are assumed. Each version amplifies
a different urgency dimension unavailable to the earlier artifacts.

Read the proposal. CARRIES FORWARD: the recommended option is the subject of all three versions.
Pull scout-positioning if available.

Three versions in full:

EXEC (decision-makers) — urgency through cost and risk:
  Hook: inertia cost — what keeps happening without this?
  What it does: business outcome from the recommended option.
  Why it matters: risk of continued inertia.
  CTA: approve / fund / unblock.

DEV (engineers and technical leads) — urgency through capability and craft:
  Hook: capability unlocked.
  What it does: references the technical design from the spec explicitly.
  Why it matters: technical debt or opportunity cost.
  CTA: join beta / review spec / contribute.

MAKER (practitioners — plain language only) — urgency through friction relief:
  Hook: friction from the inertia baseline.
  What it does: no spec terminology, no proposal jargon.
  Why it matters: time saved, steps removed.
  CTA: try it / sign up / start now.

ANTI-POSITIONING (shared): what this feature is NOT, two sentences.

Write simulations/draft/pitches/{topic}-pitch-{date}.md

FINDINGS (write this block after the pitch file is complete — not before, not during):

  CONVICTION DELTA
    Exec version: what emotional conviction does this establish that the factual and
                  optionality artifacts could not? What urgency is new here?
    Dev version: what emotional conviction does this establish that the factual and
                 optionality artifacts could not? What urgency is new here?
    Maker version: what emotional conviction does this establish that the factual and
                   optionality artifacts could not? What urgency is new here?

  NEAR-DUPLICATE CONTENT
    Name any passage you nearly copied from the spec or proposal.
    State what you changed to make it conviction-bearing rather than informational.

  RESIDUAL QUESTIONS
    What would a specific scout signal resolve that no artifact answered from existing evidence?
    Recommend a namespace for each.

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

## V-04 — FINDINGS Gate + Contract Reminders (Combination: V-01 + V-02)

**Hypothesis:** FINDINGS gate separation (V-01) makes C-18 structural; contract anchor
reminders (V-02) improve C-15/PRESERVE compliance across the distance between matrix and
each artifact. Combined, they produce defense in depth across the full artifact lifecycle:
the matrix declares obligations before execution, per-artifact reminders enforce obligations
at the point of execution, and FINDINGS gate separation enforces post-execution reflection
timing architecturally. The combination tests whether layered structural constraints outperform
either axis alone, and whether the dual-mechanism (C-17) can be delivered at higher reliability
when the contract is visible at both setup and execution time.

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

4. Artifact contract matrix — declare all obligations before execution begins:

| Field           | Spec                                                    | Proposal                                                          | Pitch                                                         |
|-----------------|---------------------------------------------------------|-------------------------------------------------------------------|---------------------------------------------------------------|
| READ            | Topic identity; inertia baseline; scout-requirements if found | Spec file; scout-feasibility if found                       | Proposal file; scout-positioning if found                     |
| WRITE           | simulations/draft/specs/{topic}-spec-{date}.md          | simulations/draft/proposals/{topic}-proposal-{date}.md            | simulations/draft/pitches/{topic}-pitch-{date}.md             |
| PRESERVE        | (first artifact)                                        | All spec design decisions — no re-opening, no new design work     | Recommended option from proposal — crystallize, do not reconsider |
| CARRIES FORWARD | Feature identity; inertia baseline; design decisions    | Recommended option name and rationale; do-nothing cost            | (final artifact)                                              |

Print the contract matrix in full. Do not begin Artifact 1 until it is printed.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 1: SPEC
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract — READ: topic identity; inertia baseline; scout-requirements if found.
           PRESERVE: (first artifact — no prior decisions)

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
Contract — READ: spec file; scout-feasibility if found.
           PRESERVE: all spec design decisions — do not re-open anything the spec resolved.

Three options minimum. Option A: do-nothing — state the inertia cost honestly.
Per option: Name / Description / Pros / Cons / Risk (H/M/L) / Effort (S/M/L).
Recommendation: chosen option + three reasons, each citing a spec decision or constraint.

GATE: Do not begin Artifact 3 until simulations/draft/proposals/{topic}-proposal-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 3: PITCH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract — READ: proposal file; scout-positioning if found.
           CARRIES FORWARD: recommended option is the subject of all three pitch versions.

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

GATE: Do not begin Campaign Reflection until simulations/draft/pitches/{topic}-pitch-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN REFLECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This phase begins only after the pitch file exists on disk — not before pitch production begins,
not during pitch production. What follows is reflection on a completed artifact, not intent
declaration or progress annotation.

FINDINGS:

  CONVICTION DELTA
    Exec version: what conviction does this version establish that the spec and proposal did not?
    Dev version: what conviction does this version establish that the spec and proposal did not?
    Maker version: what conviction does this version establish that the spec and proposal did not?

  NEAR-DUPLICATE CONTENT
    Name any passage you nearly copied from the spec or proposal.
    State what you changed to make it conviction-bearing rather than informational.

  RESIDUAL QUESTIONS
    What would a specific scout signal resolve that no artifact answered from existing evidence?
    Recommend a namespace for each.

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

## V-05 — Conviction Staging + FINDINGS Gate + Minimal Density (Combination: V-03 + V-01 + skeleton)

**Hypothesis:** R3 V-05 demonstrated that trigger phrases carry the structural weight;
ceremony is optional. R4 tests whether conviction staging (V-03) and FINDINGS gate
separation (V-01) can be expressed at minimum word count while preserving the full
128-pt ceiling. The CONVICTION TYPE row adds one matrix row; conviction-type labels in
section headers add one line each; FINDINGS gate separation replaces an inline instruction
sentence with a gated phase header. These additions are compact enough that the density
principle holds. If V-05 scores 128, the ceiling is achievable at minimal word count
through compact structural elements. If it scores below 128, the gap identifies which
compact element failed to carry its full structural weight.

```
You are running /campaign-blueprint for: {topic}

SETUP — run before Artifact 1:
  Topic identity: one sentence.
  Inertia baseline: one sentence — what users do today without this feature.
  Glob simulations/scout/ for this topic now. List all files by namespace. Unconditional.

  Artifact contract matrix:

| Field           | Spec                                         | Proposal                                              | Pitch                                                  |
|-----------------|----------------------------------------------|-------------------------------------------------------|--------------------------------------------------------|
| READ            | Topic identity; inertia; scout-requirements  | Spec file; scout-feasibility if found                 | Proposal file; scout-positioning if found              |
| WRITE           | simulations/draft/specs/{topic}-spec-{date}.md | simulations/draft/proposals/{topic}-proposal-{date}.md | simulations/draft/pitches/{topic}-pitch-{date}.md    |
| PRESERVE        | (first artifact)                             | All spec design decisions — no re-opening             | Recommended option — crystallize only                  |
| CARRIES FORWARD | Feature identity; inertia; design decisions  | Recommended option; do-nothing cost                   | (final)                                                |
| CONVICTION TYPE | Factual                                      | Optionality                                           | Emotional                                              |

Print the matrix. Do not begin Artifact 1 until it is printed.

---

ARTIFACT 1: SPEC — Factual conviction. Asserts what is true; does not argue.
READ: topic identity; inertia baseline; scout-requirements if found.
PRESERVE: (first artifact)

Sections: PURPOSE / REQUIREMENTS (MoSCoW) / DESIGN / CONSTRAINTS / OPEN QUESTIONS
Each Must-have anchored to the inertia baseline.

Write simulations/draft/specs/{topic}-spec-{date}.md
GATE: Do not begin Artifact 2 until this file is written to disk.

---

ARTIFACT 2: PROPOSAL — Optionality conviction. Evaluates options; does not repeat spec facts.
READ: spec file; scout-feasibility if found.
PRESERVE: all spec design decisions — do not re-open anything the spec resolved.

Three options min including do-nothing (honest inertia cost).
Per option: Name / Description / Pros / Cons / Risk (H/M/L) / Effort (S/M/L).
Recommendation: chosen option + three reasons citing spec decisions or constraints.

Write simulations/draft/proposals/{topic}-proposal-{date}.md
GATE: Do not begin Artifact 3 until this file is written to disk.

---

ARTIFACT 3: PITCH — Emotional conviction. Converts factual + optionality into per-audience urgency.
READ: proposal file; scout-positioning if found.
PRESERVE: recommended option — crystallize it, do not reopen the choice.

EXEC: inertia-cost hook / recommended option outcome / risk of inertia / CTA: approve or fund.
DEV: capability hook / references technical design from spec explicitly / opportunity cost / CTA: join beta.
MAKER: friction hook / plain language only, no spec or proposal terminology / time saved / CTA: try it.
Shared: ANTI-POSITIONING — what this is NOT, two sentences.

Write simulations/draft/pitches/{topic}-pitch-{date}.md
GATE: Do not begin Campaign Reflection until this file is written to disk.

---

CAMPAIGN REFLECTION — begins only after pitch file is on disk, not before, not during production.

FINDINGS:

  CONVICTION DELTA
    Exec: what emotional conviction does this establish that the factual and optionality artifacts could not?
    Dev: what emotional conviction does this establish that the factual and optionality artifacts could not?
    Maker: what emotional conviction does this establish that the factual and optionality artifacts could not?

  NEAR-DUPLICATE CONTENT
    Name any passage nearly copied from spec or proposal.
    State what changed to make it conviction-bearing.

  RESIDUAL QUESTIONS
    What would a specific scout signal resolve that no artifact answered?
    Recommend a namespace for each.

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

| ID   | Axis                                                        | Hypothesis shorthand |
|------|-------------------------------------------------------------|----------------------|
| V-01 | FINDINGS gate separation                                    | Moving FINDINGS to a named post-pitch phase makes C-18 structural, not instructed |
| V-02 | Contract anchor reminders                                   | Matrix upfront + per-artifact reminder lines improve PRESERVE compliance across distance |
| V-03 | Conviction staging                                          | CONVICTION TYPE row + typed DELTA audit reduces duplication and improves C-09/C-13 quality |
| V-04 | FINDINGS gate + contract reminders                          | Layered structural constraints across setup, execution, and reflection phases |
| V-05 | Conviction staging + FINDINGS gate + minimal density        | Tests whether the 128 ceiling is achievable with compact structural elements |

## C-17 / C-18 Coverage by Variation

| ID   | C-17 mechanism                                                              | C-18 mechanism |
|------|-----------------------------------------------------------------------------|----------------|
| V-01 | Matrix (all four fields) + named CONVICTION DELTA / NEAR-DUPLICATE template | Phase header: "not before production begins, not during production" |
| V-02 | Matrix (all four fields) + named CONVICTION DELTA / NEAR-DUPLICATE template | Inline: "not before, not during" |
| V-03 | Matrix (four required fields + CONVICTION TYPE) + named CONVICTION DELTA template | Inline: "not before, not during" |
| V-04 | Matrix (all four fields) + contract reminders + named CONVICTION DELTA template | Phase header: "not before production begins, not during production" |
| V-05 | Matrix (four required fields + CONVICTION TYPE) + named CONVICTION DELTA template | Phase header: "not before, not during production" |

## R4 Diagnostic Questions

1. Does FINDINGS gate separation (V-01, V-04, V-05) produce stronger C-18 assurance
   than inline "not before, not during" language (V-02, V-03)? Or are both equivalent
   when the double prohibition is explicit?
2. Do per-artifact contract reminders (V-02, V-04) produce higher C-06/PRESERVE
   compliance than the matrix alone — or does the matrix already carry full weight?
3. Does conviction-type labeling (V-03, V-05) improve CONVICTION DELTA quality (C-13)
   by making "what is new" more precise — or does the named sub-field template already
   constrain the question sufficiently?
4. Does the minimal-density version (V-05) reach 128, confirming that structural
   elements carry the weight at any word count — or does compactness of the matrix row
   or CONVICTION DELTA prompt cause PARTIAL on any criterion?
5. Does adding CONVICTION TYPE as a fifth matrix row (V-03, V-05) interfere with C-15
   scoring, which requires exactly four labeled fields? Or does a superset of those four
   fields still earn full credit?
