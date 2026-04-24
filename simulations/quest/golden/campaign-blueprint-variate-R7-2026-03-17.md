---
skill: quest-variate
skill_target: campaign-blueprint
date: 2026-03-17
round: 7
rubric: campaign-blueprint-rubric-v7-2026-03-17.md
---

# campaign-blueprint — Prompt Variations R7

Five complete, runnable skill body variations. Single-axis first (V-01 through V-03),
then two combinations (V-04 through V-05).

## R7 Context

R6 variants scored under v7 retroactive scoring:

| Variant | R6 Base (v6) | C-25 | C-26 | Total (v7) |
|---------|-------------|------|------|------------|
| V-01 — Per-Site Abstract Labels | 155.5 | 0 | 0 | **155.5** |
| V-02 — Scout Traceability Table | 158 | +5 | 0 | **163** |
| V-03 — Named INERTIA MODEL Entity | 158 | 0 | +5 | **163** |
| V-04 — Minimal Density | 153 | 0 | 0 | **153** |
| V-05 — Full Convergence | 158 | +5 | +5 | **168** |

V-05 alone reaches the v7 ceiling of 168. V-02 and V-03 each hold one of the two new
mechanisms but not both. The rubric states: "the two patterns are architecturally
separable — a future variant combining both without V-05's full convergence is the
expected R7 design space."

**What C-25 and C-26 require:**

- **C-25**: dedicated labeled table (Req-ID / Must-have / Originating Friction / Scout
  File). V-02 earns FULL through a SCOUT TRACEABILITY TABLE inside REQUIREMENTS. V-05
  also earns FULL through the same table combined with full structural explicitness.
- **C-26**: named, multi-field entity (Name / Behavior / Cost) with explicit
  field-to-conviction-type mapping. V-03 earns FULL through a three-field INERTIA MODEL
  entity with a five-line bulleted field-to-conviction mapping. V-05 also earns FULL.

**R6 V-05's overhead for earning both:**

R6 V-05 earns C-25 and C-26 through three mechanisms, each at maximum elaboration:

1. INERTIA MODEL entity with bulleted field-to-conviction-type mapping (five prose lines
   in SETUP)
2. SCOUT TRACEABILITY TABLE inside REQUIREMENTS (four-column labeled table with
   per-must-have rows)
3. Per-site CONVICTION TYPE reminder lines referencing INERTIA MODEL fields by name
   ("Factual — document the INERTIA MODEL Cost field as factual record; do not argue.")
   at all three artifact sites

R7 asks: what is the minimum-sufficient form of each mechanism — and can the three
mechanisms be combined at lower elaboration depth without losing either criterion?

**R7 variation axes:**

- V-01: C-26 mapping form — single anchor sentence vs bulleted list (single-axis from
  R6 V-05). Tests whether "Cost drives all three conviction types: spec documents it,
  proposal prices it, pitch makes it visceral" satisfies C-26's "explicit
  field-to-conviction-type mapping" equivalently to the R6 bulleted list.
- V-02: C-25 placement — SCOUT TRACEABILITY TABLE declared in CAMPAIGN SETUP
  (pre-artifact, as a friction-first planning tool) vs inside REQUIREMENTS (single-axis
  from R6 V-05). Tests whether table placement affects C-25 scoring and whether
  pre-artifact traceability planning changes requirement quality or C-24 scoring.
- V-03: D8 minimum expression — bracket-notation per-site CONVICTION TYPE labels
  ("[INERTIA MODEL Cost → factual record]") vs full prose (single-axis from R6 V-05).
  Matrix CONVICTION TYPE row retained at full prose inertia-grounded form. Tests whether
  bracket notation satisfies D8's per-site inertia grounding requirement.
- V-04: Minimal density with both C-25 + C-26 (combination). R6 V-04 scored 153 under
  v7 because it lacked both new criteria. R7 V-04 adds INERTIA MODEL entity (compact
  anchor-sentence mapping) and SCOUT TRACEABILITY TABLE (minimal template) at skeleton
  density throughout. Tests whether 168 is achievable at minimum word count.
- V-05: Minimum-verbosity path to 168 (combination). Combines V-01 compact C-26 anchor
  sentence + R6 V-02/V-05 proven C-25 table form (inside REQUIREMENTS) + V-03 bracket
  D8 per-site CONVICTION TYPE. Everything else at normal prose density. Tests whether
  trimming only the elaboration overhead of each new-criterion mechanism reaches 168
  without creating interference.

**R7 diagnostic questions:**

1. Is C-26's "explicit field-to-conviction-type mapping" satisfied by an anchor sentence,
   or does the bulleted five-line list form appear necessary? (V-01 vs R6 V-05)
2. Does C-25 scoring depend on placement — does the table need to be inside the spec
   REQUIREMENTS section, or does a SETUP-level table earn the same credit? Does
   friction-first table planning improve C-24 or C-10 quality? (V-02 vs R6 V-02/V-05)
3. Does D8's per-site inertia grounding require prose form, or does bracket notation
   ("[INERTIA MODEL Cost → factual record]") satisfy "inertia-grounded conviction type
   labels at the per-artifact execution-site reminder"? (V-03 vs R6 V-05)
4. Can both C-25 and C-26 earn full credit at skeleton density, or does compactness cause
   either mechanism to fall to PARTIAL or NO CREDIT? (V-04)
5. Does combining three compact mechanisms simultaneously (V-01 + V-02-placement-held +
   V-03) maintain the 168 ceiling, or does any compact form produce a scoring gap that a
   single mechanism would not create alone? (V-05)

---

## V-01 — C-26 Compact Mapping: Anchor Sentence Field-to-Conviction Mapping

**Axis:** C-26 mapping form — anchor sentence replaces bulleted field-to-conviction list

**Hypothesis:** R6 V-03 and V-05 both earned C-26 through a named INERTIA MODEL entity
(Name / Behavior / Cost) followed by a five-line bulleted field-to-conviction-type mapping:
"- Factual conviction (spec): documents the Cost field as factual record / - Optionality
conviction (proposal): prices the Cost field against each alternative / - Emotional
conviction (pitch): makes the Cost field visceral per audience." C-26 requires "named,
multi-field entity (Name / Behavior / Cost) with explicit field-to-conviction-type mapping."
R7 V-01 tests whether the three-field entity alone plus a single anchor sentence — "Cost
drives all three conviction types: the spec documents it as factual record, the proposal
prices it against each alternative, and the pitch makes it visceral per audience" —
satisfies the "explicit mapping" requirement. The anchor sentence states all three
field-to-conviction linkages in one line rather than five. The SCOUT TRACEABILITY TABLE
(C-25) and full prose per-site CONVICTION TYPE reminders referencing INERTIA MODEL fields
(D8) are retained from R6 V-05 unchanged. Predicted score: 168 if anchor sentence
satisfies "explicit field-to-conviction-type mapping"; 163 if the bulleted list form is
required for full credit.

```
You are running /campaign-blueprint for: {topic}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The INERTIA MODEL is the campaign's named architectural opponent — the status quo each
artifact must displace. Define it as a structural entity before writing anything.

1. Topic identity — one sentence: feature name, audience, problem solved.

2. INERTIA MODEL — three-field declaration:
     Name:     one short phrase identifying the current behavior in shorthand
     Behavior: what users do today without this feature — one sentence
     Cost:     what that behavior costs them — one sentence covering factual,
               priceable, and emotional dimensions

   Cost drives all three conviction types: the spec documents it as factual record,
   the proposal prices it against each alternative, and the pitch makes it visceral
   per audience.

3. Scout inventory — glob simulations/scout/ for this topic now. List every file by namespace.
   Unconditional. Do not gate on signal presence.

4. Artifact contract matrix — declares what each artifact inherits, produces, protects, and carries:

| Field           | Spec                                                             | Proposal                                                                    | Pitch                                                                              |
|-----------------|------------------------------------------------------------------|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| READ            | Topic identity; INERTIA MODEL (all fields); scout-requirements if found | Spec file; INERTIA MODEL Cost; scout-feasibility if found          | Proposal file; INERTIA MODEL Cost; scout-positioning if found                      |
| WRITE           | simulations/draft/specs/{topic}-spec-{date}.md                   | simulations/draft/proposals/{topic}-proposal-{date}.md                      | simulations/draft/pitches/{topic}-pitch-{date}.md                                  |
| PRESERVE        | (first artifact)                                                 | All spec design decisions — no re-opening, no new design work               | Recommended option from proposal — crystallize, do not reconsider                  |
| CARRIES FORWARD | Feature identity; INERTIA MODEL (all fields); design decisions   | Recommended option name and rationale; INERTIA MODEL Cost                   | (final artifact)                                                                   |
| CONVICTION TYPE | Factual — documents INERTIA MODEL Cost as factual record         | Optionality — prices INERTIA MODEL Cost against each alternative            | Emotional — makes INERTIA MODEL Cost visceral per audience                         |

Print the contract matrix in full. Do not begin Artifact 1 until it is printed.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 1: SPEC — Factual Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: topic identity; INERTIA MODEL (Name, Behavior, Cost); scout-requirements if found.
                    PRESERVE: (first artifact — no prior decisions to protect).
                    CONVICTION TYPE: Factual — document the INERTIA MODEL Cost field as factual record; do not argue.

Document what the INERTIA MODEL costs users before prescribing what replaces it.

Sections (all required):

  PURPOSE        — State the INERTIA MODEL Name and Behavior, then document the Cost as
                   factual record. "The INERTIA MODEL creates [Cost] for [audience]
                   because [Behavior persists]."
  REQUIREMENTS   — Bulleted, MoSCoW-tagged (M/S/C/W). Pull scout-requirements if available.
                   Each Must-have traces to a specific friction the INERTIA MODEL Cost creates.

                   SCOUT TRACEABILITY TABLE — complete after listing all requirements:
                   | Req-ID | Must-have (brief)  | Originating Scout-Requirements Friction            | Scout File (path or "none") |
                   |--------|--------------------|----------------------------------------------------|-----------------------------|
                   | M-01   |                    |                                                    |                             |
                   (one row per Must-have; friction = the specific INERTIA MODEL Cost dimension the Must-have resolves)

  DESIGN         — Components, data flow, key decisions. Specific enough to start from.
  CONSTRAINTS    — Technical, team, timeline, and dependency limits.
  OPEN QUESTIONS — What you do not know. Which namespace could resolve each.

GATE: Do not begin Artifact 2 until simulations/draft/specs/{topic}-spec-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 2: PROPOSAL — Optionality Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: spec file; INERTIA MODEL Cost; scout-feasibility if found.
                    PRESERVE: all spec design decisions — do not re-open anything the spec resolved.
                    CONVICTION TYPE: Optionality — price the INERTIA MODEL Cost against each alternative; do not re-assert spec facts.

Option A is do-nothing — the INERTIA MODEL maintained at full Cost. State that Cost
explicitly and concretely before presenting alternatives. Every other option is measured
against the INERTIA MODEL Cost, not against zero.

Three options minimum. Option A: do-nothing — state the INERTIA MODEL Cost as the option cost.
Per option: Name / Description / Pros / Cons / Risk (H/M/L) / Effort (S/M/L).
Recommendation: chosen option + three reasons, each citing a spec decision or constraint.

GATE: Do not begin Artifact 3 until simulations/draft/proposals/{topic}-proposal-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 3: PITCH — Emotional Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: proposal file; INERTIA MODEL Cost; scout-positioning if found.
                    PRESERVE: recommended option from proposal — crystallize it, do not reconsider.
                    CONVICTION TYPE: Emotional — make the INERTIA MODEL Cost visceral per audience.

Each version opens with the INERTIA MODEL Cost as its hook. The audience already has the
facts (spec) and the options (proposal). What they need is to feel why the INERTIA MODEL
Cost exceeds the cost of acting now — and why that urgency is specific to them.

Three versions in full:

EXEC (decision-makers) — urgency through compounding INERTIA MODEL Cost:
  Hook: the INERTIA MODEL Cost in business terms — what keeps accumulating without this.
  What it does: the outcome the recommended option delivers, framed as Cost elimination.
  Why it matters: the compounding risk of sustained INERTIA MODEL Behavior.
  CTA: approve / fund / unblock.

DEV (engineers and technical leads) — urgency through blocked capability:
  Hook: what the INERTIA MODEL Behavior prevents engineers from doing or building.
  What it does: references the technical design from the spec explicitly.
  Why it matters: the technical debt or opportunity cost of sustained INERTIA MODEL Behavior.
  CTA: join beta / review spec / contribute.

MAKER (practitioners — plain language only) — urgency through daily INERTIA MODEL Cost:
  Hook: the specific daily friction of the INERTIA MODEL Behavior for this audience.
  What it does: no spec terminology, no proposal jargon — only what changes in daily work.
  Why it matters: time saved and steps removed from the INERTIA MODEL Behavior.
  CTA: try it / sign up / start now.

ANTI-POSITIONING (shared): what this feature is NOT, two sentences.

GATE: Do not begin Campaign Reflection until simulations/draft/pitches/{topic}-pitch-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN REFLECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This phase begins only after the pitch file exists on disk — not before pitch production
begins, not during pitch production. What follows is retrospective assessment of completed
artifacts. The question in each sub-field: did the artifact make the INERTIA MODEL Cost
visceral at its declared conviction level?

FINDINGS:

  CONVICTION DELTA
    Exec version: what emotional conviction about the INERTIA MODEL Cost does this
                  establish that the factual and optionality artifacts could not make visceral?
    Dev version: what emotional conviction about the INERTIA MODEL Cost does this
                 establish that the factual and optionality artifacts could not make visceral?
    Maker version: what emotional conviction about the INERTIA MODEL Cost does this
                   establish that the factual and optionality artifacts could not make visceral?

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

## V-02 — C-25 SETUP Placement: Friction-First Traceability Table

**Axis:** C-25 placement — SCOUT TRACEABILITY TABLE declared in CAMPAIGN SETUP before
Artifact 1, populated from the scout inventory as a friction-first planning tool

**Hypothesis:** R6 V-02 and V-05 earned C-25 by placing the SCOUT TRACEABILITY TABLE
inside the REQUIREMENTS section of Artifact 1 — after the Must-have list, as a
post-requirement traceability record. C-25 requires "a dedicated labeled table (Req-ID /
Must-have / Originating Friction / Scout File)" but the rubric is silent on placement.
R7 V-02 tests whether declaring the table in CAMPAIGN SETUP — as a campaign planning step
driven by the scout inventory, with friction and scout-file columns pre-populated before
any artifact is written — earns C-25 equivalently. This inverts the current flow: instead
of "write Must-haves then trace frictions," the model first inventories known frictions
from scout-requirements, then writes Must-haves that correspond to those pre-identified
rows. The REQUIREMENTS section references the campaign-level table rather than generating
a new one. If C-25 is placement-agnostic, V-02 scores 168; if C-25 requires the table
inside the REQUIREMENTS section specifically, V-02 scores 163. The named INERTIA MODEL
entity with full bulleted field mapping (C-26) and full prose per-site CONVICTION TYPE
reminders (D8) are retained unchanged from R6 V-05. Secondary question: does
friction-first table planning improve C-24 or C-10 quality scoring?

```
You are running /campaign-blueprint for: {topic}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The INERTIA MODEL is the campaign's named architectural opponent — the status quo each
artifact must displace. Define it as a structural entity before writing anything.

1. Topic identity — one sentence: feature name, audience, problem solved.

2. INERTIA MODEL — three-field declaration:
     Name:     one short phrase identifying the current behavior in shorthand
     Behavior: what users do today without this feature — one sentence
     Cost:     what that behavior costs them — one sentence covering factual,
               priceable, and emotional dimensions

   The three conviction types map onto INERTIA MODEL fields directly:
   - Factual conviction (spec):         documents the Cost field as factual record
   - Optionality conviction (proposal): prices the Cost field against each alternative
   - Emotional conviction (pitch):      makes the Cost field visceral per audience

3. Scout inventory — glob simulations/scout/ for this topic now. List every file by namespace.
   Unconditional. Do not gate on signal presence.

4. SCOUT TRACEABILITY TABLE — pre-populate using the scout inventory above. Each row
   represents a friction the spec Must-haves will address. Fill Originating Friction and
   Scout File now from scout-requirements findings; complete Req-ID and Must-have during
   Artifact 1 REQUIREMENTS writing.

   | Req-ID       | Must-have (brief)    | Originating Scout-Requirements Friction      | Scout File (path or "none") |
   |--------------|----------------------|----------------------------------------------|-----------------------------|
   | (fill in A1) | (fill in A1)         |                                              |                             |
   (one row per identified friction; if no scout-requirements file found, one row with Friction
   derived from INERTIA MODEL Cost and Scout File = "none")

5. Artifact contract matrix — declares what each artifact inherits, produces, protects, and carries:

| Field           | Spec                                                             | Proposal                                                                    | Pitch                                                                              |
|-----------------|------------------------------------------------------------------|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| READ            | Topic identity; INERTIA MODEL (all fields); scout-requirements if found | Spec file; INERTIA MODEL Cost; scout-feasibility if found          | Proposal file; INERTIA MODEL Cost; scout-positioning if found                      |
| WRITE           | simulations/draft/specs/{topic}-spec-{date}.md                   | simulations/draft/proposals/{topic}-proposal-{date}.md                      | simulations/draft/pitches/{topic}-pitch-{date}.md                                  |
| PRESERVE        | (first artifact)                                                 | All spec design decisions — no re-opening, no new design work               | Recommended option from proposal — crystallize, do not reconsider                  |
| CARRIES FORWARD | Feature identity; INERTIA MODEL (all fields); design decisions   | Recommended option name and rationale; INERTIA MODEL Cost                   | (final artifact)                                                                   |
| CONVICTION TYPE | Factual — documents INERTIA MODEL Cost as factual record         | Optionality — prices INERTIA MODEL Cost against each alternative            | Emotional — makes INERTIA MODEL Cost visceral per audience                         |

Print the contract matrix in full. Do not begin Artifact 1 until it is printed.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 1: SPEC — Factual Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: topic identity; INERTIA MODEL (Name, Behavior, Cost); scout-requirements if found.
                    PRESERVE: (first artifact — no prior decisions to protect).
                    CONVICTION TYPE: Factual — document the INERTIA MODEL Cost field as factual record; do not argue.

Document what the INERTIA MODEL costs users before prescribing what replaces it.

Sections (all required):

  PURPOSE        — State the INERTIA MODEL Name and Behavior, then document the Cost as
                   factual record. "The INERTIA MODEL creates [Cost] for [audience]
                   because [Behavior persists]."
  REQUIREMENTS   — Bulleted, MoSCoW-tagged (M/S/C/W). Pull scout-requirements if available.
                   As you write each Must-have, complete its Req-ID and Must-have entry in
                   the SCOUT TRACEABILITY TABLE in CAMPAIGN SETUP above. Every Must-have
                   must correspond to a row in that table.
  DESIGN         — Components, data flow, key decisions. Specific enough to start from.
  CONSTRAINTS    — Technical, team, timeline, and dependency limits.
  OPEN QUESTIONS — What you do not know. Which namespace could resolve each.

GATE: Do not begin Artifact 2 until simulations/draft/specs/{topic}-spec-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 2: PROPOSAL — Optionality Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: spec file; INERTIA MODEL Cost; scout-feasibility if found.
                    PRESERVE: all spec design decisions — do not re-open anything the spec resolved.
                    CONVICTION TYPE: Optionality — price the INERTIA MODEL Cost against each alternative; do not re-assert spec facts.

Option A is do-nothing — the INERTIA MODEL maintained at full Cost. State that Cost
explicitly and concretely before presenting alternatives. Every other option is measured
against the INERTIA MODEL Cost, not against zero.

Three options minimum. Option A: do-nothing — state the INERTIA MODEL Cost as the option cost.
Per option: Name / Description / Pros / Cons / Risk (H/M/L) / Effort (S/M/L).
Recommendation: chosen option + three reasons, each citing a spec decision or constraint.

GATE: Do not begin Artifact 3 until simulations/draft/proposals/{topic}-proposal-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 3: PITCH — Emotional Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: proposal file; INERTIA MODEL Cost; scout-positioning if found.
                    PRESERVE: recommended option from proposal — crystallize it, do not reconsider.
                    CONVICTION TYPE: Emotional — make the INERTIA MODEL Cost visceral per audience.

Each version opens with the INERTIA MODEL Cost as its hook. The audience already has the
facts (spec) and the options (proposal). What they need is to feel why the INERTIA MODEL
Cost exceeds the cost of acting now — and why that urgency is specific to them.

Three versions in full:

EXEC (decision-makers) — urgency through compounding INERTIA MODEL Cost:
  Hook: the INERTIA MODEL Cost in business terms — what keeps accumulating without this.
  What it does: the outcome the recommended option delivers, framed as Cost elimination.
  Why it matters: the compounding risk of sustained INERTIA MODEL Behavior.
  CTA: approve / fund / unblock.

DEV (engineers and technical leads) — urgency through blocked capability:
  Hook: what the INERTIA MODEL Behavior prevents engineers from doing or building.
  What it does: references the technical design from the spec explicitly.
  Why it matters: the technical debt or opportunity cost of sustained INERTIA MODEL Behavior.
  CTA: join beta / review spec / contribute.

MAKER (practitioners — plain language only) — urgency through daily INERTIA MODEL Cost:
  Hook: the specific daily friction of the INERTIA MODEL Behavior for this audience.
  What it does: no spec terminology, no proposal jargon — only what changes in daily work.
  Why it matters: time saved and steps removed from the INERTIA MODEL Behavior.
  CTA: try it / sign up / start now.

ANTI-POSITIONING (shared): what this feature is NOT, two sentences.

GATE: Do not begin Campaign Reflection until simulations/draft/pitches/{topic}-pitch-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN REFLECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This phase begins only after the pitch file exists on disk — not before pitch production
begins, not during pitch production. What follows is retrospective assessment of completed
artifacts. The question in each sub-field: did the artifact make the INERTIA MODEL Cost
visceral at its declared conviction level?

FINDINGS:

  CONVICTION DELTA
    Exec version: what emotional conviction about the INERTIA MODEL Cost does this
                  establish that the factual and optionality artifacts could not make visceral?
    Dev version: what emotional conviction about the INERTIA MODEL Cost does this
                 establish that the factual and optionality artifacts could not make visceral?
    Maker version: what emotional conviction about the INERTIA MODEL Cost does this
                   establish that the factual and optionality artifacts could not make visceral?

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

## V-03 — D8 Minimum Expression: Bracket-Notation Per-Site CONVICTION TYPE

**Axis:** D8 per-site compliance at minimum expression — bracket notation vs prose form

**Hypothesis:** R6 V-05 per-site CONVICTION TYPE reminder lines use full prose referencing
INERTIA MODEL fields: "Factual — document the INERTIA MODEL Cost field as factual record;
do not argue." D8 requires "inertia-grounded conviction type labels at BOTH the
campaign-level matrix AND the per-artifact execution-site reminders." The matrix
CONVICTION TYPE row establishes the campaign-level declaration; the per-site reminder is
"the proximal instruction at execution time." R7 V-03 tests whether bracket notation
satisfies D8 per-site: "CONVICTION TYPE: Factual [INERTIA MODEL Cost → factual record]"
/ "Optionality [INERTIA MODEL Cost → priced against alternatives]" / "Emotional [INERTIA
MODEL Cost → visceral per audience]." Bracket notation is inertia-grounded (references
INERTIA MODEL Cost field explicitly) but uses a symbol form rather than prose. The
contract matrix CONVICTION TYPE row retains full prose inertia-grounded form (unchanged
from R6 V-05). The INERTIA MODEL entity with full bulleted field mapping (C-26) and SCOUT
TRACEABILITY TABLE inside REQUIREMENTS (C-25) are also retained unchanged. If bracket
notation satisfies D8 per-site, V-03 scores 168; if D8 requires prose form at per-site
reminders, V-03 scores 163 (C-23 PARTIAL due to D8 violation).

```
You are running /campaign-blueprint for: {topic}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The INERTIA MODEL is the campaign's named architectural opponent — the status quo each
artifact must displace. Define it as a structural entity before writing anything.

1. Topic identity — one sentence: feature name, audience, problem solved.

2. INERTIA MODEL — three-field declaration:
     Name:     one short phrase identifying the current behavior in shorthand
     Behavior: what users do today without this feature — one sentence
     Cost:     what that behavior costs them — one sentence covering factual,
               priceable, and emotional dimensions

   The three conviction types map onto INERTIA MODEL fields directly:
   - Factual conviction (spec):         documents the Cost field as factual record
   - Optionality conviction (proposal): prices the Cost field against each alternative
   - Emotional conviction (pitch):      makes the Cost field visceral per audience

3. Scout inventory — glob simulations/scout/ for this topic now. List every file by namespace.
   Unconditional. Do not gate on signal presence.

4. Artifact contract matrix — declares what each artifact inherits, produces, protects, and carries:

| Field           | Spec                                                             | Proposal                                                                    | Pitch                                                                              |
|-----------------|------------------------------------------------------------------|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| READ            | Topic identity; INERTIA MODEL (all fields); scout-requirements if found | Spec file; INERTIA MODEL Cost; scout-feasibility if found          | Proposal file; INERTIA MODEL Cost; scout-positioning if found                      |
| WRITE           | simulations/draft/specs/{topic}-spec-{date}.md                   | simulations/draft/proposals/{topic}-proposal-{date}.md                      | simulations/draft/pitches/{topic}-pitch-{date}.md                                  |
| PRESERVE        | (first artifact)                                                 | All spec design decisions — no re-opening, no new design work               | Recommended option from proposal — crystallize, do not reconsider                  |
| CARRIES FORWARD | Feature identity; INERTIA MODEL (all fields); design decisions   | Recommended option name and rationale; INERTIA MODEL Cost                   | (final artifact)                                                                   |
| CONVICTION TYPE | Factual — documents INERTIA MODEL Cost as factual record         | Optionality — prices INERTIA MODEL Cost against each alternative            | Emotional — makes INERTIA MODEL Cost visceral per audience                         |

Print the contract matrix in full. Do not begin Artifact 1 until it is printed.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 1: SPEC — Factual Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: topic identity; INERTIA MODEL (Name, Behavior, Cost); scout-requirements if found.
                    PRESERVE: (first artifact — no prior decisions to protect).
                    CONVICTION TYPE: Factual [INERTIA MODEL Cost → factual record]

Document what the INERTIA MODEL costs users before prescribing what replaces it.

Sections (all required):

  PURPOSE        — State the INERTIA MODEL Name and Behavior, then document the Cost as
                   factual record. "The INERTIA MODEL creates [Cost] for [audience]
                   because [Behavior persists]."
  REQUIREMENTS   — Bulleted, MoSCoW-tagged (M/S/C/W). Pull scout-requirements if available.
                   Each Must-have traces to a specific friction the INERTIA MODEL Cost creates.

                   SCOUT TRACEABILITY TABLE — complete after listing all requirements:
                   | Req-ID | Must-have (brief)  | Originating Scout-Requirements Friction            | Scout File (path or "none") |
                   |--------|--------------------|----------------------------------------------------|-----------------------------|
                   | M-01   |                    |                                                    |                             |
                   (one row per Must-have; friction = the specific INERTIA MODEL Cost dimension the Must-have resolves)

  DESIGN         — Components, data flow, key decisions. Specific enough to start from.
  CONSTRAINTS    — Technical, team, timeline, and dependency limits.
  OPEN QUESTIONS — What you do not know. Which namespace could resolve each.

GATE: Do not begin Artifact 2 until simulations/draft/specs/{topic}-spec-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 2: PROPOSAL — Optionality Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: spec file; INERTIA MODEL Cost; scout-feasibility if found.
                    PRESERVE: all spec design decisions — do not re-open anything the spec resolved.
                    CONVICTION TYPE: Optionality [INERTIA MODEL Cost → priced against each alternative]

Option A is do-nothing — the INERTIA MODEL maintained at full Cost. State that Cost
explicitly and concretely before presenting alternatives. Every other option is measured
against the INERTIA MODEL Cost, not against zero.

Three options minimum. Option A: do-nothing — state the INERTIA MODEL Cost as the option cost.
Per option: Name / Description / Pros / Cons / Risk (H/M/L) / Effort (S/M/L).
Recommendation: chosen option + three reasons, each citing a spec decision or constraint.

GATE: Do not begin Artifact 3 until simulations/draft/proposals/{topic}-proposal-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 3: PITCH — Emotional Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: proposal file; INERTIA MODEL Cost; scout-positioning if found.
                    PRESERVE: recommended option from proposal — crystallize it, do not reconsider.
                    CONVICTION TYPE: Emotional [INERTIA MODEL Cost → visceral per audience]

Each version opens with the INERTIA MODEL Cost as its hook. The audience already has the
facts (spec) and the options (proposal). What they need is to feel why the INERTIA MODEL
Cost exceeds the cost of acting now — and why that urgency is specific to them.

Three versions in full:

EXEC (decision-makers) — urgency through compounding INERTIA MODEL Cost:
  Hook: the INERTIA MODEL Cost in business terms — what keeps accumulating without this.
  What it does: the outcome the recommended option delivers, framed as Cost elimination.
  Why it matters: the compounding risk of sustained INERTIA MODEL Behavior.
  CTA: approve / fund / unblock.

DEV (engineers and technical leads) — urgency through blocked capability:
  Hook: what the INERTIA MODEL Behavior prevents engineers from doing or building.
  What it does: references the technical design from the spec explicitly.
  Why it matters: the technical debt or opportunity cost of sustained INERTIA MODEL Behavior.
  CTA: join beta / review spec / contribute.

MAKER (practitioners — plain language only) — urgency through daily INERTIA MODEL Cost:
  Hook: the specific daily friction of the INERTIA MODEL Behavior for this audience.
  What it does: no spec terminology, no proposal jargon — only what changes in daily work.
  Why it matters: time saved and steps removed from the INERTIA MODEL Behavior.
  CTA: try it / sign up / start now.

ANTI-POSITIONING (shared): what this feature is NOT, two sentences.

GATE: Do not begin Campaign Reflection until simulations/draft/pitches/{topic}-pitch-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN REFLECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This phase begins only after the pitch file exists on disk — not before pitch production
begins, not during pitch production. What follows is retrospective assessment of completed
artifacts. The question in each sub-field: did the artifact make the INERTIA MODEL Cost
visceral at its declared conviction level?

FINDINGS:

  CONVICTION DELTA
    Exec version: what emotional conviction about the INERTIA MODEL Cost does this
                  establish that the factual and optionality artifacts could not make visceral?
    Dev version: what emotional conviction about the INERTIA MODEL Cost does this
                 establish that the factual and optionality artifacts could not make visceral?
    Maker version: what emotional conviction about the INERTIA MODEL Cost does this
                   establish that the factual and optionality artifacts could not make visceral?

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

## V-04 — Minimal Density: C-25 + C-26 Added to Skeleton

**Axis:** All v7 criteria (C-22 through C-26) expressed at minimum word count (combination)

**Hypothesis:** R6 V-04 (minimal density) scored 153 under v7 — earning C-22 (compact
three-field per-site reminders) but not C-25 or C-26, because it had no INERTIA MODEL
entity and no traceability table. The v7 rubric states C-25 requires a "dedicated labeled
table" and C-26 requires a "named, multi-field entity with explicit field-to-conviction-type
mapping." R7 V-04 adds both at minimum expression: (1) INERTIA MODEL entity declared in
three labeled lines plus a compact cost-mapping sentence for C-26, and (2) a minimal
four-column SCOUT TRACEABILITY TABLE template for C-25. Per-site reminders use compact
labeled lines with bracket notation (D8 test at minimum expression). All other elements
at skeleton density. The test is whether 168 is achievable at minimum word count — or
whether compactness causes C-26 ("explicit mapping" requires more than one sentence) or
C-25 ("dedicated labeled table" requires more than a minimal template) to drop. Predicted
score: 168 if compact forms satisfy both new criteria; 163 if one drops; 153 if both drop.

```
You are running /campaign-blueprint for: {topic}

SETUP — run before Artifact 1:
  Topic identity: one sentence — feature name, audience, problem solved.

  INERTIA MODEL:
    Name:     [one short phrase — the current behavior in shorthand]
    Behavior: [what users do today without this feature — one sentence]
    Cost:     [what that behavior costs them — one sentence]
  Cost maps: spec documents it (factual) / proposal prices it (optionality) / pitch makes it visceral (emotional).

  Glob simulations/scout/ for this topic now. List all files by namespace. Unconditional.

  Artifact contract matrix:

| Field           | Spec                                                 | Proposal                                                  | Pitch                                                          |
|-----------------|------------------------------------------------------|-----------------------------------------------------------|----------------------------------------------------------------|
| READ            | Topic identity; INERTIA MODEL; scout-requirements    | Spec file; INERTIA MODEL Cost; scout-feasibility          | Proposal file; INERTIA MODEL Cost; scout-positioning           |
| WRITE           | simulations/draft/specs/{topic}-spec-{date}.md       | simulations/draft/proposals/{topic}-proposal-{date}.md    | simulations/draft/pitches/{topic}-pitch-{date}.md              |
| PRESERVE        | (first artifact)                                     | All spec design decisions — no re-opening                 | Recommended option — crystallize only                          |
| CARRIES FORWARD | Feature identity; INERTIA MODEL; design decisions    | Recommended option; INERTIA MODEL Cost                    | (final)                                                        |
| CONVICTION TYPE | Factual [Cost → factual record]                      | Optionality [Cost → priced against alternatives]          | Emotional [Cost → visceral per audience]                       |

Print the matrix. Do not begin Artifact 1 until it is printed.

---

ARTIFACT 1: SPEC — Factual conviction.
READ: topic identity; INERTIA MODEL (Name, Behavior, Cost); scout-requirements if found.
PRESERVE: (first artifact — no prior decisions)
CONVICTION TYPE: Factual [INERTIA MODEL Cost → factual record]

Sections: PURPOSE / REQUIREMENTS (MoSCoW) / DESIGN / CONSTRAINTS / OPEN QUESTIONS

PURPOSE: state INERTIA MODEL Name and Behavior; document Cost as factual record.
REQUIREMENTS: each Must-have anchored to a friction the INERTIA MODEL Cost creates.

SCOUT TRACEABILITY TABLE — complete after requirements list:
| Req-ID | Must-have (brief) | Originating Friction              | Scout File      |
|--------|-------------------|-----------------------------------|-----------------|
| M-01   |                   |                                   |                 |
(one row per Must-have)

Write simulations/draft/specs/{topic}-spec-{date}.md
GATE: Do not begin Artifact 2 until this file is written to disk.

---

ARTIFACT 2: PROPOSAL — Optionality conviction.
READ: spec file; INERTIA MODEL Cost; scout-feasibility if found.
PRESERVE: all spec design decisions — no re-opening.
CONVICTION TYPE: Optionality [INERTIA MODEL Cost → priced against each alternative]

Three options min. Option A: do-nothing — state the INERTIA MODEL Cost explicitly (not zero).
Per option: Name / Description / Pros / Cons / Risk (H/M/L) / Effort (S/M/L).
Recommendation: chosen option + three reasons citing spec decisions or constraints.

Write simulations/draft/proposals/{topic}-proposal-{date}.md
GATE: Do not begin Artifact 3 until this file is written to disk.

---

ARTIFACT 3: PITCH — Emotional conviction.
READ: proposal file; INERTIA MODEL Cost; scout-positioning if found.
PRESERVE: recommended option — crystallize, do not reopen.
CONVICTION TYPE: Emotional [INERTIA MODEL Cost → visceral per audience]

EXEC: INERTIA MODEL Cost hook (business terms) / recommended outcome as Cost elimination / compounding risk / CTA: approve.
DEV: INERTIA MODEL Behavior blocks capability / references spec technical design / opportunity cost / CTA: join beta.
MAKER: INERTIA MODEL Behavior as daily friction / plain language only, no spec or proposal terminology / time saved / CTA: try it.
Shared: ANTI-POSITIONING — what this is NOT, two sentences.

Write simulations/draft/pitches/{topic}-pitch-{date}.md
GATE: Do not begin Campaign Reflection until this file is written to disk.

---

CAMPAIGN REFLECTION — begins only after the pitch file is on disk. Not before. Not during.

FINDINGS:

  CONVICTION DELTA
    Exec: what inertia urgency does this establish that factual + optionality could not make visceral?
    Dev: what inertia urgency does this establish that factual + optionality could not make visceral?
    Maker: what inertia urgency does this establish that factual + optionality could not make visceral?

  NEAR-DUPLICATE CONTENT
    Name any passage nearly copied from spec or proposal. State what changed.

  RESIDUAL QUESTIONS
    What scout signal resolves what no artifact answered? Recommend a namespace.

---

CAMPAIGN CLOSE

| Artifact | Path                                                         | Scout signal consumed | Open questions |
|----------|--------------------------------------------------------------|-----------------------|----------------|
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md               | (namespace or none)   | (list)         |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md       | (namespace or none)   | (list)         |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md            | (namespace or none)   | (list)         |

List any open question a future signal could resolve, with recommended namespace for each.
```

---

## V-05 — Minimum-Verbosity Path to 168: Compact C-26 + Proven C-25 + Bracket D8

**Axis:** Minimum-verbosity combination of all three new-criterion mechanisms (combination)

**Hypothesis:** R6 V-05 reaches 168 at high verbosity: five-line bulleted C-26 field
mapping, full prose D8 per-site CONVICTION TYPE reminders referencing INERTIA MODEL fields,
and a full four-column SCOUT TRACEABILITY TABLE. R7 V-05 tests whether the ceiling holds
when exactly the elaboration overhead of each new mechanism is trimmed while the underlying
structural requirement for each criterion is preserved: (1) C-26 via anchor-sentence
mapping (V-01 mechanism — one sentence instead of five lines), (2) C-25 via SCOUT
TRACEABILITY TABLE inside REQUIREMENTS (proven form from R6 V-02/V-05, unchanged), and
(3) D8 via bracket-notation per-site CONVICTION TYPE labels (V-03 mechanism — bracket form
instead of prose). The contract matrix CONVICTION TYPE row and all non-new-criterion prose
(section instructions, pitch framing, reflection questions) retain normal density. The
hypothesis is that trimming elaboration from the three new-criterion mechanisms does not
introduce interference — each mechanism remains independently identifiable by the scorer
even in compact form — and 168 holds. Predicted score: 168 if anchor sentence + proven
table + bracket notation each meet their criterion's minimum; 163 if any single compact
form drops.

```
You are running /campaign-blueprint for: {topic}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The INERTIA MODEL is the campaign's named architectural opponent — the status quo each
artifact must displace. Define it as a structural entity before writing anything.

1. Topic identity — one sentence: feature name, audience, problem solved.

2. INERTIA MODEL — three-field declaration:
     Name:     one short phrase identifying the current behavior in shorthand
     Behavior: what users do today without this feature — one sentence
     Cost:     what that behavior costs them — one sentence covering factual,
               priceable, and emotional dimensions

   Cost drives all three conviction types: the spec documents it as factual record,
   the proposal prices it against each alternative, and the pitch makes it visceral
   per audience.

3. Scout inventory — glob simulations/scout/ for this topic now. List every file by namespace.
   Unconditional. Do not gate on signal presence.

4. Artifact contract matrix — declares what each artifact inherits, produces, protects, and carries:

| Field           | Spec                                                             | Proposal                                                                    | Pitch                                                                              |
|-----------------|------------------------------------------------------------------|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| READ            | Topic identity; INERTIA MODEL (all fields); scout-requirements if found | Spec file; INERTIA MODEL Cost; scout-feasibility if found          | Proposal file; INERTIA MODEL Cost; scout-positioning if found                      |
| WRITE           | simulations/draft/specs/{topic}-spec-{date}.md                   | simulations/draft/proposals/{topic}-proposal-{date}.md                      | simulations/draft/pitches/{topic}-pitch-{date}.md                                  |
| PRESERVE        | (first artifact)                                                 | All spec design decisions — no re-opening, no new design work               | Recommended option from proposal — crystallize, do not reconsider                  |
| CARRIES FORWARD | Feature identity; INERTIA MODEL (all fields); design decisions   | Recommended option name and rationale; INERTIA MODEL Cost                   | (final artifact)                                                                   |
| CONVICTION TYPE | Factual — documents INERTIA MODEL Cost as factual record         | Optionality — prices INERTIA MODEL Cost against each alternative            | Emotional — makes INERTIA MODEL Cost visceral per audience                         |

Print the contract matrix in full. Do not begin Artifact 1 until it is printed.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 1: SPEC — Factual Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: topic identity; INERTIA MODEL (Name, Behavior, Cost); scout-requirements if found.
                    PRESERVE: (first artifact — no prior decisions to protect).
                    CONVICTION TYPE: Factual [INERTIA MODEL Cost → factual record]

Document what the INERTIA MODEL costs users before prescribing what replaces it.

Sections (all required):

  PURPOSE        — State the INERTIA MODEL Name and Behavior, then document the Cost as
                   factual record. "The INERTIA MODEL creates [Cost] for [audience]
                   because [Behavior persists]."
  REQUIREMENTS   — Bulleted, MoSCoW-tagged (M/S/C/W). Pull scout-requirements if available.
                   Each Must-have traces to a specific friction the INERTIA MODEL Cost creates.

                   SCOUT TRACEABILITY TABLE — complete after listing all requirements:
                   | Req-ID | Must-have (brief)  | Originating Scout-Requirements Friction            | Scout File (path or "none") |
                   |--------|--------------------|----------------------------------------------------|-----------------------------|
                   | M-01   |                    |                                                    |                             |
                   (one row per Must-have; friction = the specific INERTIA MODEL Cost dimension the Must-have resolves)

  DESIGN         — Components, data flow, key decisions. Specific enough to start from.
  CONSTRAINTS    — Technical, team, timeline, and dependency limits.
  OPEN QUESTIONS — What you do not know. Which namespace could resolve each.

GATE: Do not begin Artifact 2 until simulations/draft/specs/{topic}-spec-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 2: PROPOSAL — Optionality Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: spec file; INERTIA MODEL Cost; scout-feasibility if found.
                    PRESERVE: all spec design decisions — do not re-open anything the spec resolved.
                    CONVICTION TYPE: Optionality [INERTIA MODEL Cost → priced against each alternative]

Option A is do-nothing — the INERTIA MODEL maintained at full Cost. State that Cost
explicitly and concretely before presenting alternatives. Every other option is measured
against the INERTIA MODEL Cost, not against zero.

Three options minimum. Option A: do-nothing — state the INERTIA MODEL Cost as the option cost.
Per option: Name / Description / Pros / Cons / Risk (H/M/L) / Effort (S/M/L).
Recommendation: chosen option + three reasons, each citing a spec decision or constraint.

GATE: Do not begin Artifact 3 until simulations/draft/proposals/{topic}-proposal-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 3: PITCH — Emotional Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: proposal file; INERTIA MODEL Cost; scout-positioning if found.
                    PRESERVE: recommended option from proposal — crystallize it, do not reconsider.
                    CONVICTION TYPE: Emotional [INERTIA MODEL Cost → visceral per audience]

Each version opens with the INERTIA MODEL Cost as its hook. The audience already has the
facts (spec) and the options (proposal). What they need is to feel why the INERTIA MODEL
Cost exceeds the cost of acting now — and why that urgency is specific to them.

Three versions in full:

EXEC (decision-makers) — urgency through compounding INERTIA MODEL Cost:
  Hook: the INERTIA MODEL Cost in business terms — what keeps accumulating without this.
  What it does: the outcome the recommended option delivers, framed as Cost elimination.
  Why it matters: the compounding risk of sustained INERTIA MODEL Behavior.
  CTA: approve / fund / unblock.

DEV (engineers and technical leads) — urgency through blocked capability:
  Hook: what the INERTIA MODEL Behavior prevents engineers from doing or building.
  What it does: references the technical design from the spec explicitly.
  Why it matters: the technical debt or opportunity cost of sustained INERTIA MODEL Behavior.
  CTA: join beta / review spec / contribute.

MAKER (practitioners — plain language only) — urgency through daily INERTIA MODEL Cost:
  Hook: the specific daily friction of the INERTIA MODEL Behavior for this audience.
  What it does: no spec terminology, no proposal jargon — only what changes in daily work.
  Why it matters: time saved and steps removed from the INERTIA MODEL Behavior.
  CTA: try it / sign up / start now.

ANTI-POSITIONING (shared): what this feature is NOT, two sentences.

GATE: Do not begin Campaign Reflection until simulations/draft/pitches/{topic}-pitch-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN REFLECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This phase begins only after the pitch file exists on disk — not before pitch production
begins, not during pitch production. What follows is retrospective assessment of completed
artifacts. The question in each sub-field: did the artifact make the INERTIA MODEL Cost
visceral at its declared conviction level?

FINDINGS:

  CONVICTION DELTA
    Exec version: what emotional conviction about the INERTIA MODEL Cost does this
                  establish that the factual and optionality artifacts could not make visceral?
    Dev version: what emotional conviction about the INERTIA MODEL Cost does this
                 establish that the factual and optionality artifacts could not make visceral?
    Maker version: what emotional conviction about the INERTIA MODEL Cost does this
                   establish that the factual and optionality artifacts could not make visceral?

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

## Variation Summary

| ID   | Axis                                                           | C-25 mechanism                                   | C-26 mechanism                                   | C-23/D8 mechanism                         | Predicted v7 score |
|------|----------------------------------------------------------------|--------------------------------------------------|--------------------------------------------------|-------------------------------------------|--------------------|
| V-01 | C-26 anchor sentence (single-axis from R6 V-05)                | SCOUT TRACEABILITY TABLE in REQUIREMENTS (proven) | Anchor sentence: "Cost drives all three types"   | Full prose per-site INERTIA MODEL refs    | 168 or 163         |
| V-02 | C-25 SETUP placement (single-axis from R6 V-05)                | Table in CAMPAIGN SETUP, pre-populated from scout | Full bulleted mapping (five lines, proven)        | Full prose per-site INERTIA MODEL refs    | 168 or 163         |
| V-03 | D8 bracket notation (single-axis from R6 V-05)                 | SCOUT TRACEABILITY TABLE in REQUIREMENTS (proven) | Full bulleted mapping (five lines, proven)        | Bracket notation: "[Cost → factual record]" | 168 or 163       |
| V-04 | Minimal density + both C-25/C-26 (combination)                 | Minimal table template in REQUIREMENTS            | INERTIA MODEL + anchor sentence, compact          | Compact bracket notation "[Cost→fact]"    | 168, 163, or 153   |
| V-05 | Minimum-verbosity path to 168 (combination)                    | SCOUT TRACEABILITY TABLE in REQUIREMENTS (proven) | Anchor sentence: "Cost drives all three types"   | Bracket notation per-site                 | 168 or 163         |

## C-25 / C-26 / D8 Coverage by Variation

| ID   | C-25 form                                                                 | C-26 form                                                               | D8 per-site form                                                          |
|------|---------------------------------------------------------------------------|-------------------------------------------------------------------------|---------------------------------------------------------------------------|
| V-01 | Four-column labeled table after requirements list — FULL (proven form)    | Anchor sentence: "Cost drives all three types" — FULL or NO CREDIT       | Full prose: "Factual — document INERTIA MODEL Cost field..." — FULL       |
| V-02 | Table in SETUP, pre-populated from scout inventory before Artifact 1 — FULL or NO CREDIT | Five-line bulleted mapping — FULL (proven form)       | Full prose: "Factual — document INERTIA MODEL Cost field..." — FULL       |
| V-03 | Four-column labeled table after requirements list — FULL (proven form)    | Five-line bulleted mapping — FULL (proven form)                          | Bracket notation: "[INERTIA MODEL Cost → factual record]" — FULL or PARTIAL |
| V-04 | Minimal table template (same four columns, in REQUIREMENTS) — FULL or NO CREDIT | Compact anchor sentence after three labeled fields — FULL or NO CREDIT | Compact bracket notation "[Cost→fact]" — FULL or PARTIAL                  |
| V-05 | Four-column labeled table after requirements list — FULL (proven form)    | Anchor sentence: "Cost drives all three types" — FULL or NO CREDIT       | Bracket notation: "[INERTIA MODEL Cost → factual record]" — FULL or PARTIAL |

## R7 Diagnostic Questions

1. Is C-26's "explicit field-to-conviction-type mapping" satisfied by an anchor sentence
   ("Cost drives all three conviction types: spec documents it, proposal prices it, pitch
   makes it visceral") — or does "explicit" require the enumerated form naming each
   conviction type separately? If V-01 and V-05 score 168, the anchor sentence is
   sufficient. If they score 163, C-26 requires enumerated form.

2. Does C-25 scoring depend on the table appearing inside the spec REQUIREMENTS section
   — or is a campaign-level SETUP table placement scoring-neutral? Does friction-first
   planning (pre-populating frictions before writing Must-haves) improve C-24 or C-10?
   (V-02 vs R6 V-02/V-05)

3. Does D8's per-site inertia grounding requirement admit bracket notation
   ("[INERTIA MODEL Cost → factual record]") as satisfying "inertia-grounded conviction
   type labels at the per-artifact execution-site reminder" — or does D8 require prose
   form because brackets may not constitute "labels" in the rubric's sense? (V-03 vs
   R6 V-05)

4. At skeleton density, do the compact INERTIA MODEL declaration (three labeled lines +
   one-sentence cost mapping) and minimal SCOUT TRACEABILITY TABLE template each
   independently satisfy their criterion — or does compactness cause the scorer to treat
   the cost-mapping sentence as insufficiently explicit for C-26, or the minimal table as
   insufficiently "dedicated/labeled" for C-25? (V-04)

5. When all three compact mechanisms appear together (V-05), does any form of interference
   emerge between the anchor-sentence C-26 and bracket-notation D8 — specifically, does
   the absence of field-named prose in both the SETUP mapping and the per-site reminders
   leave the INERTIA MODEL fields underspecified at execution time, causing C-23 PARTIAL
   via D8? Or are the two mechanisms independent enough that compact forms combine cleanly?
   (V-05 vs R6 V-05)
