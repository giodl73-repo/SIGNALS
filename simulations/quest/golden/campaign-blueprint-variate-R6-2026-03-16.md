---
skill: quest-variate
skill_target: campaign-blueprint
date: 2026-03-16
round: 6
rubric: campaign-blueprint-rubric-v6-2026-03-16.md
---

# campaign-blueprint — Prompt Variations R6

Five complete, runnable skill body variations. Single-axis first (V-01 through V-03),
then two combinations (V-04 through V-05).

## R6 Context

R5 differentiated all five variants under v6 retroactive scoring:

| Variant | R5 Total (v5) | C-22 | C-23 | C-24 | Total (v6) |
|---------|--------------|------|------|------|------------|
| V-01 — C-20 Proximity Resolution | 140.5 | +5 | 0 | 0 | **145.5** |
| V-02 — Phase Gate + Conviction Typing | 140.5 | 0 | 0 | 0 | **140.5** |
| V-03 — Full Triple Combination | 143 | +5 | 0 | 0 | **148** |
| V-04 — Full Triple + Minimal Density | 143 | +5 | 0 | 0 | **148** |
| V-05 — Full Triple + Inertia-Forward | 143 | +5 | +5 | +5 | **158** |

V-05 alone reached the v6 ceiling of 158. C-22 was earned by all variants carrying
three-field per-site reminders. C-23 and C-24 were earned only by V-05 (R5), through:

- **C-23**: inertia-grounded CONVICTION TYPE labels in the contract matrix CONVICTION TYPE
  row AND in the per-site reminder CONVICTION TYPE lines at each artifact
- **C-24**: REQUIREMENTS instruction "Each Must-have must trace to a specific friction the
  inertia baseline creates" combined with the READ field referencing scout-requirements

The v6 ceiling is 158 and R5 V-05 demonstrates it is reachable. R6 explores the
structural mechanics behind C-23 and C-24 — which specific implementations earn full
credit, whether equivalent alternatives exist, and whether the ceiling holds at minimum
density.

**R6 variation axes:**

- V-01: C-23 location — inertia grounding in contract matrix only; abstract labels
  per-site. Tests whether D7's "campaign-level architectural choice" means the matrix
  declaration alone satisfies C-23, or whether per-site restatement of inertia grounding
  is also required. Single-axis from R5 V-05.
- V-02: C-24 mechanism — dedicated SCOUT TRACEABILITY TABLE with explicit per-must-have
  origin citations. Tests whether a structured reverse-link table form earns C-24 more
  robustly than a general traceability instruction. Single-axis from R5 V-05.
- V-03: C-23 operationalization depth — named INERTIA MODEL architectural entity in
  SETUP. Tests whether elevating the inertia baseline from an inline sentence to a named,
  three-field structural entity (Name / Behavior / Cost) sharpens D7 satisfaction and
  whether conviction labels referencing model fields by name produce different scoring.
  Single-axis from R5 V-05.
- V-04: Minimal density — C-22 + C-23 + C-24 at minimum word count. R5 V-04 (minimal
  density) reached 148 under v6 because it lacked C-23 and C-24. R6 V-04 adds both at
  minimum expression. Tests whether 158 is achievable at skeleton density.
- V-05: Full convergence — named INERTIA MODEL + SCOUT TRACEABILITY TABLE + three-field
  per-site reminders referencing INERTIA MODEL fields. Maximum structural explicitness.
  Tests whether combining all three mechanisms simultaneously creates any interference
  with narrative quality (C-09) while maintaining the 158 ceiling.

**R6 diagnostic questions:**

1. Does C-23 require inertia-grounded phrasing specifically in the per-site CONVICTION
   TYPE reminder — or is the campaign-level matrix declaration alone sufficient for full
   credit? (V-01 vs. R5 V-05)
2. Does a dedicated SCOUT TRACEABILITY TABLE earn C-24 more robustly than a general
   instruction — and does it improve C-10 scoring by making scout signal consumption
   bidirectionally auditable? (V-02 vs. R5 V-05)
3. Does naming the inertia baseline as a three-field INERTIA MODEL entity (Name / Behavior
   / Cost) sharpen C-23 scoring over R5 V-05's inline sentence form? (V-03 vs. R5 V-05)
4. Can all three new v6 criteria (C-22, C-23, C-24) be expressed at minimum density while
   retaining full credit — or does compacting the inertia labels or traceability
   instruction cause any criterion to fall to PARTIAL? (V-04)
5. Does maximum structural explicitness (V-05) maintain the 158 ceiling without degrading
   C-09 narrative quality — or does over-engineering the inertia and traceability
   apparatus introduce instruction friction? (V-05)

---

## V-01 — C-23 Location Test: Matrix Inertia Grounding, Abstract Per-Site Labels

**Axis:** C-23 location — campaign-level (matrix) inertia grounding; per-site reminders
use abstract labels

**Hypothesis:** R5 V-05 grounded the CONVICTION TYPE labels in the inertia baseline at
two locations: the contract matrix CONVICTION TYPE row (campaign-level) and each per-site
reminder CONVICTION TYPE line (artifact-level). The rubric's D7 dependency states C-23
requires "an inertia model defined at the campaign level — a campaign-level architectural
choice, not a local improvement." If D7's phrase "campaign-level" means the matrix
declaration is the satisfying mechanism, then per-site reminders using abstract labels
(Factual / Optionality / Emotional without inertia grounding) should still earn C-23
FULL. If C-23 scoring follows whichever location conveys the inertia grounding to the
executing model most proximally, then abstract per-site labels will cause C-23 PARTIAL.
C-22 is fully retained (three-field per-site reminder: READ + PRESERVE + CONVICTION
TYPE). C-24 is retained (traceability instruction in REQUIREMENTS). Predicted score: 158
if matrix declaration alone satisfies D7; 153 if per-site inertia grounding is also
required for C-23 FULL.

```
You are running /campaign-blueprint for: {topic}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The inertia baseline is the campaign's primary subject — the active competitor every
artifact must displace. Establish it before writing anything.

1. Topic identity — one sentence: feature name, audience, problem solved.
2. Inertia baseline — one sentence: what users do today without this feature.
   Every Must-have requirement, every option cost, every pitch hook traces here.
3. Scout inventory — glob simulations/scout/ for this topic now. List every file by namespace.
   Unconditional. Do not gate on signal presence.

4. Artifact contract matrix — declares what each artifact inherits, produces, protects, and carries:

| Field           | Spec                                                    | Proposal                                                          | Pitch                                                                  |
|-----------------|---------------------------------------------------------|-------------------------------------------------------------------|------------------------------------------------------------------------|
| READ            | Topic identity; inertia baseline; scout-requirements if found | Spec file; scout-feasibility if found                       | Proposal file; scout-positioning if found                              |
| WRITE           | simulations/draft/specs/{topic}-spec-{date}.md          | simulations/draft/proposals/{topic}-proposal-{date}.md            | simulations/draft/pitches/{topic}-pitch-{date}.md                      |
| PRESERVE        | (first artifact)                                        | All spec design decisions — no re-opening, no new design work     | Recommended option from proposal — crystallize, do not reconsider      |
| CARRIES FORWARD | Feature identity; inertia baseline; design decisions    | Recommended option name and rationale; do-nothing cost            | (final artifact)                                                       |
| CONVICTION TYPE | Factual — names the problem the inertia baseline creates | Optionality — prices the cost of inertia against each alternative | Emotional — makes the inertia cost visceral and per-audience-specific  |

Print the contract matrix in full. Do not begin Artifact 1 until it is printed.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 1: SPEC — Factual Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: topic identity; inertia baseline; scout-requirements if found.
                    PRESERVE: (first artifact — no prior decisions to protect).
                    CONVICTION TYPE: Factual — assert what is true; do not argue or persuade.

Sections (all required):

  PURPOSE        — What problem the inertia baseline creates and why it persists.
  REQUIREMENTS   — Bulleted, MoSCoW-tagged (M/S/C/W). Pull scout-requirements if available.
                   Each Must-have traces to a specific friction the inertia baseline creates.
  DESIGN         — Components, data flow, key decisions. Specific enough to start from.
  CONSTRAINTS    — Technical, team, timeline, and dependency limits.
  OPEN QUESTIONS — What you do not know. Which namespace could resolve each.

GATE: Do not begin Artifact 2 until simulations/draft/specs/{topic}-spec-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 2: PROPOSAL — Optionality Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: spec file; scout-feasibility if found.
                    PRESERVE: all spec design decisions — do not re-open anything the spec resolved.
                    CONVICTION TYPE: Optionality — evaluate trade-offs against spec facts; do not re-assert facts.

Option A is do-nothing — the inertia option. State its cost honestly before presenting
alternatives, so the cost of inertia is the baseline every option is measured against.

Three options minimum. Option A: do-nothing — state the inertia cost explicitly and concretely.
Per option: Name / Description / Pros / Cons / Risk (H/M/L) / Effort (S/M/L).
Recommendation: chosen option + three reasons, each citing a spec decision or constraint.

GATE: Do not begin Artifact 3 until simulations/draft/proposals/{topic}-proposal-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 3: PITCH — Emotional Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: proposal file; scout-positioning if found.
                    PRESERVE: recommended option from proposal — crystallize it, do not reconsider.
                    CONVICTION TYPE: Emotional — convert factual and optionality conviction into per-audience urgency.

Each version opens with the inertia cost as its hook. The audience does not need to be
sold on features — they need to feel why continued inertia is more costly than acting now.

Three versions in full:

EXEC (decision-makers) — urgency through cost and compounding risk:
  Hook: what keeps happening without this — the inertia cost in business terms.
  What it does: the outcome the recommended option delivers, stated as inertia reversal.
  Why it matters: the compounding risk of continued inertia.
  CTA: approve / fund / unblock.

DEV (engineers and technical leads) — urgency through blocked capability:
  Hook: what the inertia baseline prevents engineers from doing or building.
  What it does: references the technical design from the spec explicitly.
  Why it matters: the technical debt or opportunity cost of continued inertia.
  CTA: join beta / review spec / contribute.

MAKER (practitioners — plain language only) — urgency through daily friction:
  Hook: the specific daily friction the inertia baseline creates for this audience.
  What it does: no spec terminology, no proposal jargon — only what changes for the maker.
  Why it matters: time saved and steps removed.
  CTA: try it / sign up / start now.

ANTI-POSITIONING (shared): what this feature is NOT, two sentences.

GATE: Do not begin Campaign Reflection until simulations/draft/pitches/{topic}-pitch-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN REFLECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This phase begins only after the pitch file exists on disk — not before pitch production
begins, not during pitch production. What follows is retrospective assessment of completed
artifacts. The question in each sub-field is whether the artifact delivered its declared
conviction type against the inertia baseline.

FINDINGS:

  CONVICTION DELTA
    Exec version: what emotional conviction about the inertia cost does this establish
                  that the factual and optionality artifacts could not make visceral?
    Dev version: what emotional conviction about the inertia cost does this establish
                 that the factual and optionality artifacts could not make visceral?
    Maker version: what emotional conviction about the inertia cost does this establish
                   that the factual and optionality artifacts could not make visceral?

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

## V-02 — C-24 Mechanism: Scout Traceability Table

**Axis:** C-24 mechanism — dedicated SCOUT TRACEABILITY TABLE with explicit per-must-have
origin citations

**Hypothesis:** R5 V-05 earned C-24 through a general instruction in the REQUIREMENTS
section: "Each Must-have must trace to a specific friction the inertia baseline creates."
The rubric defines C-24 as requiring "each spec Must-have cites its originating
scout-requirements friction." R6 V-02 tests whether a dedicated SCOUT TRACEABILITY TABLE
— a labeled matrix following the requirements list, with one row per Must-have and
explicit columns for originating friction and scout file — earns C-24 more robustly than
a general instruction. The table form makes the reverse linkage auditable: each must-have
entry can be traced directly to its originating scout-requirements evidence. This also
tests whether C-10 (scout signal pull visibility) improves when the scout-to-must-have
connection is declared in a labeled structure rather than implied through instruction. All
other structural elements retained from R5 V-05: inertia-grounded CONVICTION TYPE in
matrix and per-site reminders, CAMPAIGN REFLECTION phase gate, three-field per-site
contract reminders. Predicted score: 158 (C-24 FULL; potential improvement in C-10
quality scoring).

```
You are running /campaign-blueprint for: {topic}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The inertia baseline is the campaign's primary subject — not as background, but as the
active competitor every artifact must displace. Establish it before writing anything.

1. Topic identity — one sentence: feature name, audience, problem solved.
2. Inertia baseline — one sentence: what users do today without this feature.
   Every Must-have requirement, every option cost, every pitch hook traces here.
3. Scout inventory — glob simulations/scout/ for this topic now. List every file by namespace.
   Unconditional. Do not gate on signal presence.

4. Artifact contract matrix — declares what each artifact inherits, produces, protects, and carries:

| Field           | Spec                                                    | Proposal                                                          | Pitch                                                                  |
|-----------------|---------------------------------------------------------|-------------------------------------------------------------------|------------------------------------------------------------------------|
| READ            | Topic identity; inertia baseline; scout-requirements if found | Spec file; scout-feasibility if found                       | Proposal file; scout-positioning if found                              |
| WRITE           | simulations/draft/specs/{topic}-spec-{date}.md          | simulations/draft/proposals/{topic}-proposal-{date}.md            | simulations/draft/pitches/{topic}-pitch-{date}.md                      |
| PRESERVE        | (first artifact)                                        | All spec design decisions — no re-opening, no new design work     | Recommended option from proposal — crystallize, do not reconsider      |
| CARRIES FORWARD | Feature identity; inertia baseline; design decisions    | Recommended option name and rationale; do-nothing cost            | (final artifact)                                                       |
| CONVICTION TYPE | Factual — names the problem the inertia baseline creates | Optionality — prices the cost of inertia against each alternative | Emotional — makes the inertia cost visceral and per-audience-specific  |

Print the contract matrix in full. Do not begin Artifact 1 until it is printed.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 1: SPEC — Factual Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: topic identity; inertia baseline; scout-requirements if found.
                    PRESERVE: (first artifact — no prior decisions to protect).
                    CONVICTION TYPE: Factual — name the problem the inertia baseline creates; do not argue.

Document what the inertia baseline costs users before prescribing what replaces it.

Sections (all required):

  PURPOSE        — What problem the inertia baseline creates and why it persists.
                   State it factually: not "users want X" but "without this, users do Y,
                   which costs them Z."
  REQUIREMENTS   — Bulleted, MoSCoW-tagged (M/S/C/W). Pull scout-requirements if available.
                   Each Must-have traces to a specific friction the inertia baseline creates.

                   SCOUT TRACEABILITY TABLE — complete after listing all requirements:
                   | Req-ID | Must-have (brief)  | Originating Scout-Requirements Friction      | Scout File (path or "none") |
                   |--------|--------------------|----------------------------------------------|-----------------------------|
                   | M-01   |                    |                                              |                             |
                   (one row per Must-have; friction = the user pain or system gap the Must-have resolves)

  DESIGN         — Components, data flow, key decisions. Specific enough to start from.
  CONSTRAINTS    — Technical, team, timeline, and dependency limits.
  OPEN QUESTIONS — What you do not know. Which namespace could resolve each.

GATE: Do not begin Artifact 2 until simulations/draft/specs/{topic}-spec-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 2: PROPOSAL — Optionality Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: spec file; scout-feasibility if found.
                    PRESERVE: all spec design decisions — do not re-open anything the spec resolved.
                    CONVICTION TYPE: Optionality — price the cost of inertia against each alternative; do not re-assert spec facts.

Option A is do-nothing — the inertia option. State its cost honestly before presenting
alternatives, so the inertia cost is the baseline every option is measured against.

Three options minimum. Option A: do-nothing — state the inertia cost explicitly and concretely.
Per option: Name / Description / Pros / Cons / Risk (H/M/L) / Effort (S/M/L).
Recommendation: chosen option + three reasons, each citing a spec decision or constraint.

GATE: Do not begin Artifact 3 until simulations/draft/proposals/{topic}-proposal-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 3: PITCH — Emotional Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: proposal file; scout-positioning if found.
                    PRESERVE: recommended option from proposal — crystallize it, do not reconsider.
                    CONVICTION TYPE: Emotional — make the inertia cost visceral and per-audience-specific.

Each version opens with the inertia cost as its hook. The audience does not need to be
sold on features — they need to feel why continued inertia is more costly than acting now.

Three versions in full:

EXEC (decision-makers) — urgency through cost and compounding risk:
  Hook: what keeps happening without this — the inertia cost in business terms.
  What it does: the outcome the recommended option delivers, stated as inertia reversal.
  Why it matters: the compounding risk of continued inertia.
  CTA: approve / fund / unblock.

DEV (engineers and technical leads) — urgency through blocked capability:
  Hook: what the inertia baseline prevents engineers from doing or building.
  What it does: references the technical design from the spec explicitly.
  Why it matters: the technical debt or opportunity cost of continued inertia.
  CTA: join beta / review spec / contribute.

MAKER (practitioners — plain language only) — urgency through daily friction:
  Hook: the specific daily friction the inertia baseline creates for this audience.
  What it does: no spec terminology, no proposal jargon — only what changes for the maker.
  Why it matters: time saved and steps removed.
  CTA: try it / sign up / start now.

ANTI-POSITIONING (shared): what this feature is NOT, two sentences.

GATE: Do not begin Campaign Reflection until simulations/draft/pitches/{topic}-pitch-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN REFLECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This phase begins only after the pitch file exists on disk — not before pitch production
begins, not during pitch production. What follows is retrospective assessment of completed
artifacts. The question in each sub-field is whether the artifact delivered its declared
conviction type against the inertia baseline.

FINDINGS:

  CONVICTION DELTA
    Exec version: what emotional conviction about the inertia cost does this establish
                  that the factual and optionality artifacts could not make visceral?
    Dev version: what emotional conviction about the inertia cost does this establish
                 that the factual and optionality artifacts could not make visceral?
    Maker version: what emotional conviction about the inertia cost does this establish
                   that the factual and optionality artifacts could not make visceral?

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

## V-03 — Named INERTIA MODEL Entity: Campaign-Level Architecture

**Axis:** C-23 operationalization depth — three-field INERTIA MODEL architectural entity
in SETUP

**Hypothesis:** R5 V-05 declared the inertia baseline as a one-sentence entry with an
annotation ("Every Must-have requirement, every option cost, every pitch hook traces
here."). This satisfied C-23 and D7. R6 V-03 tests whether elevating the inertia model
to a named, three-field structural entity — INERTIA MODEL with Name / Behavior / Cost —
produces a more precisely satisfied D7 and sharper C-23. The three fields map directly
onto the three conviction types: Factual conviction documents the Cost field, Optionality
conviction prices the Cost against alternatives, Emotional conviction makes the Cost
visceral. The CONVICTION TYPE labels in the contract matrix and per-site reminders
reference INERTIA MODEL fields by name, making the grounding explicit and auditable. This
also tests whether a named campaign entity (referenced consistently across all three
artifacts) produces better C-09 narrative quality by making the structural opponent
present at every decision point. Predicted score: 158 (or reveals whether named model vs.
inline sentence changes C-23 or C-09 scoring).

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
               (e.g., "manual sync loop", "spreadsheet workaround", "copy-paste audit")
     Behavior: what users do today without this feature — one sentence
     Cost:     what that behavior costs them — one sentence covering the factual,
               priceable, and emotional dimensions

   The three conviction types map onto INERTIA MODEL fields directly:
   - Factual conviction (spec):      documents the Cost field as factual record
   - Optionality conviction (proposal): prices the Cost field against each alternative
   - Emotional conviction (pitch):   makes the Cost field visceral per audience

3. Scout inventory — glob simulations/scout/ for this topic now. List every file by namespace.
   Unconditional. Do not gate on signal presence.

4. Artifact contract matrix — declares what each artifact inherits, produces, protects, and carries:

| Field           | Spec                                                             | Proposal                                                                   | Pitch                                                                            |
|-----------------|------------------------------------------------------------------|----------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| READ            | Topic identity; INERTIA MODEL (all fields); scout-requirements if found | Spec file; INERTIA MODEL Cost; scout-feasibility if found         | Proposal file; INERTIA MODEL Cost; scout-positioning if found                    |
| WRITE           | simulations/draft/specs/{topic}-spec-{date}.md                   | simulations/draft/proposals/{topic}-proposal-{date}.md                     | simulations/draft/pitches/{topic}-pitch-{date}.md                                |
| PRESERVE        | (first artifact)                                                 | All spec design decisions — no re-opening, no new design work              | Recommended option from proposal — crystallize, do not reconsider                |
| CARRIES FORWARD | Feature identity; INERTIA MODEL (all fields); design decisions   | Recommended option name and rationale; INERTIA MODEL Cost                  | (final artifact)                                                                 |
| CONVICTION TYPE | Factual — documents the INERTIA MODEL Cost field as factual record | Optionality — prices the INERTIA MODEL Cost against each alternative     | Emotional — makes the INERTIA MODEL Cost visceral per audience                   |

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
                   factual record. Not "users want X" but "the INERTIA MODEL creates
                   [Cost] for [audience] because [Behavior persists]."
  REQUIREMENTS   — Bulleted, MoSCoW-tagged (M/S/C/W). Pull scout-requirements if available.
                   Each Must-have traces to a specific friction the INERTIA MODEL Cost creates.
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

## V-04 — Minimal Density: C-22 + C-23 + C-24 Compressed

**Axis:** All three v6 new criteria at minimum word count (combination)

**Hypothesis:** R5 V-04 (minimal density) reached 148 under v6 retroactive scoring —
earning C-22 but not C-23 or C-24 because it used abstract CONVICTION TYPE labels in the
matrix (Factual / Optionality / Emotional without inertia grounding) and had no
traceability instruction in REQUIREMENTS. R6 V-04 adds both missing criteria at minimum
expression: C-23 is addressed by compact inertia-grounded CONVICTION TYPE entries in the
matrix (e.g., "Factual — names inertia problem"); C-24 is addressed by a one-line
traceability instruction per Must-have ("tag the scout-requirements friction it
addresses"). The test is whether a compact inertia-grounded label satisfies C-23 the same
way V-05 R5's longer formulation does, and whether a compact traceability instruction
satisfies C-24 the same way V-05 R5's longer formulation does. If minimal density can
hold 158, the ceiling is density-independent. Predicted score: 158 if compact forms are
sufficient; 148 if compactness causes C-23 or C-24 to fall to PARTIAL.

```
You are running /campaign-blueprint for: {topic}

SETUP — run before Artifact 1:
  Topic identity: one sentence — feature name, audience, problem solved.
  Inertia baseline: one sentence — what users do today without this feature. The campaign's active opponent.
  Glob simulations/scout/ for this topic now. List all files by namespace. Unconditional.

  Artifact contract matrix:

| Field           | Spec                                                    | Proposal                                                     | Pitch                                                                 |
|-----------------|---------------------------------------------------------|--------------------------------------------------------------|-----------------------------------------------------------------------|
| READ            | Topic identity; inertia; scout-requirements if found    | Spec file; scout-feasibility if found                        | Proposal file; scout-positioning if found                             |
| WRITE           | simulations/draft/specs/{topic}-spec-{date}.md          | simulations/draft/proposals/{topic}-proposal-{date}.md       | simulations/draft/pitches/{topic}-pitch-{date}.md                     |
| PRESERVE        | (first artifact)                                        | All spec design decisions — no re-opening                    | Recommended option — crystallize only                                 |
| CARRIES FORWARD | Feature identity; inertia; design decisions             | Recommended option; do-nothing cost                          | (final)                                                               |
| CONVICTION TYPE | Factual — names inertia problem                         | Optionality — prices inertia cost                            | Emotional — makes inertia cost visceral                               |

Print the matrix. Do not begin Artifact 1 until it is printed.

---

ARTIFACT 1: SPEC — Factual conviction.
READ: topic identity; inertia baseline; scout-requirements if found.
PRESERVE: (first artifact — no prior decisions)
CONVICTION TYPE: Factual — names inertia problem

Sections: PURPOSE / REQUIREMENTS (MoSCoW) / DESIGN / CONSTRAINTS / OPEN QUESTIONS
Each Must-have: tag the scout-requirements friction it addresses
(format: "[friction: {specific inertia or scout-requirements finding}]" after each Must-have item).
Anchor each Must-have to a specific friction the inertia baseline creates.

Write simulations/draft/specs/{topic}-spec-{date}.md
GATE: Do not begin Artifact 2 until this file is written to disk.

---

ARTIFACT 2: PROPOSAL — Optionality conviction.
READ: spec file; scout-feasibility if found.
PRESERVE: all spec design decisions — no re-opening.
CONVICTION TYPE: Optionality — prices inertia cost

Three options min. Option A: do-nothing — explicit inertia cost (not zero).
Per option: Name / Description / Pros / Cons / Risk (H/M/L) / Effort (S/M/L).
Recommendation: chosen option + three reasons citing spec decisions or constraints.

Write simulations/draft/proposals/{topic}-proposal-{date}.md
GATE: Do not begin Artifact 3 until this file is written to disk.

---

ARTIFACT 3: PITCH — Emotional conviction.
READ: proposal file; scout-positioning if found.
PRESERVE: recommended option — crystallize, do not reopen.
CONVICTION TYPE: Emotional — makes inertia cost visceral

EXEC: inertia-cost hook / recommended outcome as inertia reversal / compounding risk / CTA: approve.
DEV: blocked-capability hook / references spec technical design explicitly / opportunity cost / CTA: join beta.
MAKER: daily-friction hook / plain language only, no spec or proposal terminology / time saved / CTA: try it.
Shared: ANTI-POSITIONING — what this is NOT, two sentences.

Write simulations/draft/pitches/{topic}-pitch-{date}.md
GATE: Do not begin Campaign Reflection until this file is written to disk.

---

CAMPAIGN REFLECTION — begins only after the pitch file is on disk. Not before. Not during.

FINDINGS:

  CONVICTION DELTA
    Exec: what inertia cost urgency does this establish that factual + optionality could not make visceral?
    Dev: what inertia cost urgency does this establish that factual + optionality could not make visceral?
    Maker: what inertia cost urgency does this establish that factual + optionality could not make visceral?

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

## V-05 — Full Convergence: Named Model + Traceability Table + Inertia-Anchored Per-Site

**Axis:** Maximum structural explicitness — all three v6 mechanisms at maximum definition
depth (combination)

**Hypothesis:** R5 V-05 reached 158 with inertia grounding expressed throughout but
without naming it as a structural entity or tabulating the traceability linkage. R6 V-05
tests whether making every structural mechanism maximally explicit maintains or improves
the ceiling: (1) INERTIA MODEL as a named, three-field architectural entity in SETUP
(Name / Behavior / Cost), (2) SCOUT TRACEABILITY TABLE in the REQUIREMENTS section with
explicit per-must-have origin citations, (3) per-site contract reminders that reference
INERTIA MODEL fields by name in all three reminder fields (READ, PRESERVE, CONVICTION
TYPE). This is the "most auditable" version — every decision about inertia grounding and
scout traceability is named, labeled, and cross-referenced. The hypothesis is that maximum
explicitness maintains 158 without any criterion dropping, and may improve C-09 narrative
quality by making the campaign's architectural opponent structurally present at every
execution site. The risk is that over-specification introduces instruction friction that
degrades narrative flow or causes confusion between INERTIA MODEL field names and
artifact content. Predicted score: 158 (ceiling maintained; C-09 quality test).

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
   - Factual conviction (spec):      documents the Cost field as factual record
   - Optionality conviction (proposal): prices the Cost field against each alternative
   - Emotional conviction (pitch):   makes the Cost field visceral per audience

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

## Variation Summary

| ID   | Axis                                                   | New v6 criteria targeted            | Key structural change                                                         | Predicted v6 score |
|------|--------------------------------------------------------|-------------------------------------|-------------------------------------------------------------------------------|--------------------|
| V-01 | C-23 location test (single-axis)                       | C-22 FULL; C-23 location test; C-24 | Matrix: inertia-grounded; per-site: abstract labels                           | 153 or 158         |
| V-02 | C-24 mechanism: traceability table (single-axis)       | C-22 FULL; C-23 FULL; C-24 explicit | SCOUT TRACEABILITY TABLE in REQUIREMENTS after must-have list                 | 158                |
| V-03 | C-23 depth: named INERTIA MODEL entity (single-axis)   | C-22 FULL; C-23 named; C-24         | Three-field INERTIA MODEL entity; labels reference model fields by name       | 158                |
| V-04 | All three at minimal density (combination)             | C-22; C-23 compact; C-24 compact    | Compact inertia labels in matrix; inline friction-tag per Must-have           | 158 or 148         |
| V-05 | Full convergence: named model + table + per-site (combination) | C-22 FULL; C-23 FULL; C-24 FULL | INERTIA MODEL + TRACEABILITY TABLE + per-site INERTIA MODEL field references | 158                |

## C-22 / C-23 / C-24 Coverage by Variation

| ID   | C-22 mechanism                                                           | C-23 mechanism                                                        | C-24 mechanism                                                       |
|------|--------------------------------------------------------------------------|-----------------------------------------------------------------------|----------------------------------------------------------------------|
| V-01 | Three-field per-site (READ + PRESERVE + CONVICTION TYPE, abstract) → FULL | Inertia-grounded labels in matrix only; abstract per-site → FULL or PARTIAL | "traces to friction" instruction → FULL                    |
| V-02 | Three-field per-site (inertia-grounded, same as R5 V-05) → FULL          | Inertia-grounded labels in matrix + per-site → FULL                   | SCOUT TRACEABILITY TABLE with per-must-have rows → FULL              |
| V-03 | Three-field per-site referencing INERTIA MODEL fields → FULL             | Named INERTIA MODEL entity + field-referenced labels → FULL           | "traces to INERTIA MODEL Cost friction" instruction → FULL           |
| V-04 | Compact three-field per-site (labeled lines) → FULL or PARTIAL           | Compact inertia-grounded matrix labels ("Factual — names inertia problem") → FULL or PARTIAL | Inline friction-tag instruction per Must-have → FULL or PARTIAL |
| V-05 | Three-field per-site with INERTIA MODEL field references → FULL          | Named entity + field-referenced matrix + per-site → FULL              | SCOUT TRACEABILITY TABLE with per-must-have rows → FULL              |

## R6 Diagnostic Questions

1. Does C-23 require inertia-grounded phrasing specifically in the per-site CONVICTION
   TYPE reminder — or is the campaign-level matrix declaration alone sufficient for FULL
   credit? If V-01 scores 158, D7's "campaign-level" means matrix-only satisfies; if
   V-01 scores 153, per-site inertia grounding is also required.

2. Does a dedicated SCOUT TRACEABILITY TABLE earn C-24 more robustly than R5 V-05's
   general instruction — and does the table form improve C-10 (scout signal pull
   visibility) because the linkage is declared in a labeled structure rather than implied?

3. Does naming the inertia model as a three-field architectural entity (INERTIA MODEL:
   Name / Behavior / Cost) produce sharper C-23 scoring than R5 V-05's inline sentence
   form — or is the criterion indifferent to whether the inertia model is named or
   described inline?

4. Can all three new v6 criteria (C-22, C-23, C-24) be expressed at minimum density while
   retaining FULL credit — or do compact inertia labels ("Factual — names inertia
   problem") and one-line traceability instructions fall to PARTIAL?

5. Does maximum structural explicitness (V-05 — named model + traceability table +
   field-referenced per-site reminders) maintain the 158 ceiling without degrading C-09
   narrative quality — or does over-engineering the structural apparatus introduce
   instruction friction that reduces output quality?
