---
skill: quest-variate
skill_target: campaign-blueprint
date: 2026-03-17
round: 8
rubric: campaign-blueprint-rubric-v8-2026-03-17.md
---

# campaign-blueprint — Prompt Variations R8

Five complete, runnable skill body variations. Single-axis first (V-01 through V-03),
then two combinations (V-04 through V-05).

## R8 Context

R7 variants scored under v8 retroactive scoring:

| Variant | v7 | C-27 | v8 |
|---------|-----|------|-----|
| V-01 — C-26 Compact Mapping: Anchor Sentence | 163 | 0 | **163** |
| V-02 — C-25 SETUP Placement: Friction-First | 168 | +5 | **173** |
| V-03 — D8 Bracket Notation | 168 | 0 | **168** |
| V-04 — Minimal Density: C-25 + C-26 on Skeleton | 158 (expected) | 0 | **158** (expected) |
| V-05 — Minimum-Verbosity Path to 168 | 168 | 0 | **168** |

V-02 alone reaches the v8 ceiling of 173. The rubric states: "a future variant combining
SETUP placement with bracket notation is the R8 design space." V-03 validates bracket
notation as a D8-compliant per-site form; V-01 validates anchor sentence as a C-26-compliant
mapping form. The two 168-point R7 paths (V-03 and V-05) both place the table inside
REQUIREMENTS and earn C-27 NO CREDIT.

**What C-27 requires (v8):**

- The SCOUT TRACEABILITY TABLE must appear in CAMPAIGN SETUP — before any artifact
  instruction
- It must be pre-populated from the scout inventory (Originating Friction and Scout File
  columns filled from scout-requirements findings; Req-ID and Must-have filled during
  Artifact 1 writing)
- The REQUIREMENTS section must reference back to the campaign-level table rather than
  generating a new table
- FULL or NO CREDIT — no partial

R7 V-02 satisfies all three: (a) table declared in step 4 of CAMPAIGN SETUP before the
contract matrix print gate, (b) pre-population instruction explicit ("Fill Originating
Friction and Scout File now from scout-requirements findings"), (c) REQUIREMENTS instructs
"complete its Req-ID and Must-have entry in the SCOUT TRACEABILITY TABLE in CAMPAIGN SETUP
above."

**R8 variation axes:**

- V-01: D8 per-site form at SETUP placement — bracket notation replacing full prose per-site
  reminders while retaining SETUP placement. Tests whether bracket notation (validated in
  R7 V-03 for D8 compliance in isolation) remains D8-compliant when the table is at SETUP
  rather than inside REQUIREMENTS.
- V-02: C-26 form at SETUP placement — anchor sentence replacing five-line bulleted C-26
  mapping while retaining SETUP placement. Tests whether anchor sentence (validated in R7
  V-01 as a candidate C-26 form) earns C-26 FULL independently of table placement.
- V-03: C-27 back-reference minimality — minimal one-line REQUIREMENTS reference replacing
  the full directive instruction. Tests what "REQUIREMENTS references back to campaign-level
  table" minimally requires: a directional pointer ("see table above") or an explicit
  row-completion directive ("complete each Must-have row in the table above").
- V-04: Triple compact at SETUP — combination of V-01 bracket D8 + V-02 anchor C-26 + SETUP
  placement (moves the R7 V-05 minimum-verbosity form to SETUP). Tests whether all three
  compact mechanisms hold simultaneously when the table placement changes.
- V-05: Minimal density path to 173 — skeleton density + SETUP placement. Extends R7 V-04
  (skeleton, expected 158 under v8) by moving its table to SETUP. Tests whether skeleton
  density can satisfy C-27's pre-population and back-reference requirements.

**R8 diagnostic questions:**

1. Does bracket notation (D8-validated in R7 V-03 with table in REQUIREMENTS) remain valid
   when the table is in SETUP — or does the scoring context change? (V-01 vs R7 V-02)
2. Does anchor sentence (C-26 candidate from R7 V-01) earn C-26 FULL regardless of whether
   the table is in SETUP or REQUIREMENTS — or does SETUP placement affect the C-26 test?
   (V-02 vs R7 V-01 and R7 V-02)
3. Does C-27's "REQUIREMENTS references back" require a directive instruction ("complete each
   row"), or is a minimal pointer ("see table above") sufficient for FULL credit? (V-03 vs
   R7 V-02)
4. Does combining all three compact forms (V-01 bracket + V-02 anchor + SETUP) maintain 173,
   or does any compact form interfere with C-27 at SETUP placement? (V-04)
5. Can SETUP placement earn C-27 at skeleton density, or does the skeleton's brevity produce
   a pre-population or back-reference instruction below C-27's threshold? (V-05)

---

## V-01 — C-27 + D8 Bracket: Named R8 Design Space

**Axis:** D8 per-site form — bracket notation at SETUP placement

**Hypothesis:** R7 V-02 earns 173 using full prose per-site CONVICTION TYPE reminders: "Factual
— document the INERTIA MODEL Cost field as factual record; do not argue." R7 V-03 validates
bracket notation as a D8-compliant per-site form in isolation: "CONVICTION TYPE: Factual
[INERTIA MODEL Cost → factual record]" — earning C-23 FULL by explicitly naming the INERTIA
MODEL Cost field in a bracket notation per-site reminder. R8 V-01 is the exact combination
named in the v8 rubric: SETUP placement from R7 V-02, bracket notation from R7 V-03. The
contract matrix CONVICTION TYPE row retains full prose inertia-grounded form unchanged from
R7 V-02. The INERTIA MODEL entity retains the full five-line bulleted field-to-conviction
mapping (C-26). The SCOUT TRACEABILITY TABLE pre-population instruction is unchanged. The
REQUIREMENTS back-reference instruction is unchanged. The only change is swapping three
full-prose per-site reminders for bracket-notation equivalents at all artifact sites.
Predicted score: 173 if bracket notation is D8-compliant independent of table placement
(i.e., C-23 grading does not interact with C-27 placement); 168 if bracket notation fails
D8 when the table is at SETUP (i.e., the scoring context of SETUP placement somehow elevates
the per-site form requirement).

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
                    CONVICTION TYPE: Factual [INERTIA MODEL Cost → factual record]

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

## V-02 — C-27 + Compact C-26: SETUP Placement with Anchor Sentence

**Axis:** C-26 mapping form — anchor sentence at SETUP placement

**Hypothesis:** R7 V-01 tested anchor sentence C-26 without SETUP placement: it earned 163
(C-27 NO CREDIT, C-26 PARTIAL or FULL unknown — predicted 168 if anchor satisfies C-26, 163
if bulleted list required). R7 V-02 earned 173 using SETUP placement with the full five-line
bulleted field-to-conviction mapping for C-26. The two axes — C-26 form and C-27 placement
— have only been tested separately. R8 V-02 tests whether anchor sentence earns C-26 FULL
independently of table placement: if C-26 is placement-agnostic, the anchor sentence result
from R7 V-01 scoring should hold unchanged here, and V-02 scores 173 (C-27 FULL + C-26
anchor-sentence result). If the bulleted mapping is required for C-26 FULL, V-02 scores 168
(C-27 FULL + C-26 PARTIAL). Full prose D8 per-site reminders are retained unchanged from
R7 V-02. SCOUT TRACEABILITY TABLE pre-population and REQUIREMENTS back-reference are
unchanged. Only change: five-line bulleted field mapping replaced with anchor sentence.

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

## V-03 — C-27 Back-Reference Minimality: Pointer vs Directive

**Axis:** C-27 back-reference form — minimal pointer replacing full directive instruction

**Hypothesis:** R7 V-02 earns C-27 FULL through a REQUIREMENTS instruction that is both a
directive and a referential pointer: "As you write each Must-have, complete its Req-ID and
Must-have entry in the SCOUT TRACEABILITY TABLE in CAMPAIGN SETUP above. Every Must-have
must correspond to a row in that table." This instruction does two things: (1) it names the
campaign-level table ("SCOUT TRACEABILITY TABLE in CAMPAIGN SETUP above") — the referential
pointer — and (2) it tells the model what to do with that table ("complete its Req-ID and
Must-have entry") — the directive. C-27 says "REQUIREMENTS references back to campaign-level
table." The word "references" may require only the pointer (naming the table) or may require
the directive (instructing row completion). R8 V-03 tests the minimal form: "Each Must-have
must have a corresponding row in the SCOUT TRACEABILITY TABLE above." This retains the
referential pointer ("SCOUT TRACEABILITY TABLE above") and the correspondence assertion
("must have a corresponding row") but removes the explicit directive to complete specific
columns during writing. The full bulleted C-26 field mapping and full prose D8 per-site
reminders are retained unchanged from R7 V-02. Predicted score: 173 if a pointer-and-
correspondence assertion satisfies "REQUIREMENTS references back"; 168 if C-27 requires an
explicit row-completion directive ("complete Req-ID and Must-have entry") at the Artifact 1
writing site.

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
                   Each Must-have must have a corresponding row in the SCOUT TRACEABILITY
                   TABLE above.
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

## V-04 — Triple Compact at SETUP: Bracket + Anchor + SETUP Placement

**Axis:** All three compact mechanisms (V-01 bracket D8 + V-02 anchor C-26) at SETUP placement

**Hypothesis:** R7 V-05 (minimum-verbosity, 168 under v8) combines three compact mechanisms:
anchor sentence C-26, bracket notation D8, and proven C-25 table inside REQUIREMENTS. Each
compact form passed in that configuration. The one change from R7 V-05 that would earn C-27
is moving the table to SETUP. R8 V-04 makes exactly that move: takes R7 V-05 as its base
and substitutes SETUP placement for REQUIREMENTS placement. The REQUIREMENTS section gets
the full directive back-reference instruction from R7 V-02 (not the minimal pointer from
V-03 above) to hold C-27's back-reference requirement at maximum confidence. The anchor
sentence C-26 mapping, bracket D8 per-site reminders, and full prose contract matrix
CONVICTION TYPE row are all unchanged from R7 V-05. The test is whether any compact form
interferes with C-27 at SETUP placement — specifically, whether bracket notation at per-site
reminders (V-01 axis) or anchor sentence at INERTIA MODEL declaration (V-02 axis) degrades
any scoring criterion when the table is simultaneously moved to SETUP. Predicted score: 173
if both compact forms hold with SETUP placement (consistent with V-01 and V-02 hypotheses
independently); 168 if one compact form drops under combined pressure; 163 if two drop.

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
                    CONVICTION TYPE: Factual [INERTIA MODEL Cost → factual record]

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

## V-05 — Minimal Density Path to 173: Skeleton + SETUP Placement

**Axis:** C-27 at skeleton density — minimum word count + SETUP placement

**Hypothesis:** R7 V-04 (minimal/skeleton density, expected 158 under v8) earns C-25 and
C-26 at skeleton brevity but not C-27 (table inside REQUIREMENTS, not SETUP). Moving the
table to SETUP is the only architectural change needed to earn C-27. R8 V-05 makes that
substitution at full skeleton density — no instruction is padded above minimum. The test
has two sub-questions: (1) does skeleton brevity in the REQUIREMENTS back-reference
instruction still satisfy C-27's back-reference requirement (the instruction "each Must-have
needs a row in the SCOUT TRACEABILITY TABLE above" is shorter than R7 V-02's full directive);
(2) does skeleton-density pre-population instruction ("Fill Originating Friction and Scout
File from scout inventory now; fill Req-ID and Must-have in A1") satisfy C-27's
"pre-populated from scout inventory" requirement at compact form. All other elements at R7
V-04 skeleton density: compact three-field INERTIA MODEL with Cost-maps sentence, skeleton
artifact instructions, skeleton reflection. Per-site CONVICTION TYPE reminders use bracket
notation (consistent with R7 V-04). Contract matrix at compact column width (R7 V-04 form).
Predicted score: 163 if C-27 earns FULL at skeleton density (table in SETUP, both
pre-population and back-reference instructions present even if compact) — net gain of +5
over R7 V-04's 158; 158 if skeleton brevity fails C-27 on either pre-population or
back-reference threshold.

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

  SCOUT TRACEABILITY TABLE — pre-populate from scout inventory now. Fill Originating Friction
  and Scout File from scout-requirements findings; fill Req-ID and Must-have during A1.

  | Req-ID       | Must-have (brief) | Originating Friction              | Scout File      |
  |--------------|-------------------|-----------------------------------|-----------------|
  | (fill in A1) | (fill in A1)      |                                   |                 |
  (one row per friction; if no scout-requirements found, one row: friction from INERTIA MODEL
  Cost, Scout File = "none")

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
              Complete Req-ID and Must-have in the SCOUT TRACEABILITY TABLE above for each.

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

## Predicted Scoring Under v8

| Variant | Base | C-27 hypothesis | Predicted v8 |
|---------|------|-----------------|--------------|
| V-01 — C-27 + D8 Bracket (named R8 design space) | 168 (R7 V-03 base) | FULL — bracket notation is D8-independent of table placement | **173** |
| V-02 — C-27 + Compact C-26 Anchor Sentence | 168 (R7 V-02 base - C-26 swap) | FULL — C-26 anchor sentence is placement-agnostic | **173** if anchor earns C-26; **168** if bulleted list required |
| V-03 — C-27 Back-Reference Minimality | 173 (R7 V-02 base) | FULL if pointer satisfies "references back"; NO CREDIT if directive required | **173** or **168** |
| V-04 — Triple Compact at SETUP (combination) | 168 (R7 V-05 base + SETUP move) | FULL — compact forms tested independently in V-01/V-02 | **173** if no interference; **168** if one compact form drops |
| V-05 — Minimal Density Path to 173 (combination) | 158 (R7 V-04 base + SETUP move) | FULL if skeleton pre-population + back-reference satisfy C-27 | **163** if C-27 earns FULL; **158** if skeleton fails C-27 threshold |

**Key R8 decisions:** V-01 resolves whether bracket notation interacts with table placement.
V-02 resolves whether anchor sentence C-26 is placement-agnostic. V-03 resolves what
"references back" minimally requires. V-04 probes triple-compact interference. V-05 tests
whether the v8 ceiling is reachable at skeleton density at all (163 target, not 173).
