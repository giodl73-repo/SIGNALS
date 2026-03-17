---
skill: quest-variate
skill_target: campaign-blueprint
date: 2026-03-17
round: 12
rubric: campaign-blueprint-rubric-v12-2026-03-17.md
---

# campaign-blueprint — Prompt Variations R12

Five complete, runnable skill body variations. Single-axis first (V-01 through V-03),
then two combinations (V-04 through V-05).

## R12 Context

R11 variants under v12 retroactive scoring:

| Variant | v11 | C-34 | C-35 | v12 |
|---------|-----|------|------|-----|
| V-01 — C-31 Citation Direction Table | 198 | +5 | 0 | **203** |
| V-02 — C-32 Subsection Prescription Table | 198 | 0 | +5 | **203** |
| V-03 — C-33 Falsifiable Hypothesis Addition | 203 | 0 | 0 | **203** |
| V-04 — Triple: Tightened C-31 + Tightened C-32 + Falsifiable C-33 | 203 | +5 | +5 | **213** |
| V-05 — Minimum-Density Path to 203 | 203 | 0 | 0 | **203** |

R11 V-04 alone reaches 213: C-34 (CONVICTION DELTA as 4-column table with Amplification
chain template) + C-35 (CONVICTION GAP DIAGNOSIS as 6-column table with Register found
and Register declared as structurally distinct columns) + C-33 (falsifiable hypothesis) +
C-31 + C-32 subsumed. No R11 single-axis variant combines all five active criteria. The
213 ceiling requires V-04's three-phase combination.

R11 V-01 earns C-34 FULL via the 4-column table form with template instruction immediately
below the table. R11 V-02 earns C-35 FULL via the 6-column table with one pre-declared
empty row. V-03 and V-05 do not earn C-34 or C-35 — both use inline prose forms for
CONVICTION DELTA and narrative prose for CONVICTION GAP DIAGNOSIS.

**R12 design question:**

C-34's identifying test is column-count plus cell-template pre-declaration. C-35's
identifying test is column-count plus Register found / Register declared as distinct
headers. The retroactive scoring confirms R11 V-01 passes C-34 and R11 V-02 passes C-35.
But both earned those criteria while leaving the other upgrade absent. R12 explores three
questions:

1. **Tighter C-34:** R11 V-01's Amplification chain cells were empty, with the template
   stated in the instruction block below the table. A tighter form pre-places the template
   string directly inside each data cell — "[Req-ID]'s [specific factual claim] is made
   visceral by [emotional register]" — converting the instruction into an ontological
   constraint at the cell level. Does in-cell pre-declaration change C-34 behavior, or is
   R11 V-01's form already the ceiling implementation?

2. **Tighter C-35:** R11 V-02's table pre-declared a single empty row. A tighter form
   pre-declares one row per artifact (Spec, Proposal, Pitch), making structural
   incompleteness immediately visible: a row that is blank where the CLOSE table shows
   partial or N is a visible gap at a glance. Does artifact-row pre-declaration reveal a
   latent criterion above C-35?

3. **Structural TRACEABILITY AUDIT (potential C-36):** C-29 is currently a prose
   instruction — "for each row, name the Req-ID, confirm it appears, name the gap." The
   C-34 and C-35 pattern converts epistemic instructions into ontological tables. A
   structural TRACEABILITY AUDIT would be a per-row fill-in table: Req-ID | Friction |
   Must-have found? | Must-have text | Gap | Scout namespace. This converts per-row
   verification from a prose directive into a structural constraint where a N row with
   a blank Gap column is visibly incomplete. V-03 probes whether this reveals a latent
   C-36.

**Predicted scoring pattern:**

| Variant | Axis | Hypothesis | Expected v12 |
|---------|------|------------|--------------|
| V-01 — C-34 In-Cell Template | Lifecycle emphasis | Template in cell vs template in instruction | **208** |
| V-02 — C-35 Artifact-Row Pre-Declaration | Output format | Per-artifact row pre-declaration vs single empty row | **208** |
| V-03 — Structural Traceability Audit (C-36 probe) | Output format | Per-row audit table as structural enforcement of C-29 | **208 or 213** |
| V-04 — C-34 + C-35 Combination | REFLECTION + CLOSE | Maximum confirmed 213 path | **213** |
| V-05 — Minimum-Density 213 | Lifecycle compression | Minimum form preserving all structural requirements | **213** |

V-01 and V-02 each add one structural criterion to the 203 base (R11 V-03 with C-33 +
C-31 + C-32). V-03 probes a structural upgrade to TRACEABILITY AUDIT on the same 203
base. V-04 combines C-34 + C-35 on the 203 base for the confirmed 213 path. V-05 compresses
V-04 to minimum density.

---

## V-01 — C-34 In-Cell Amplification Template

**Axis:** Lifecycle emphasis — CAMPAIGN REFLECTION's CONVICTION DELTA sub-field is
restructured as a 4-column table where the Amplification chain column has the template
string pre-placed inside each data cell, not in an instruction block below the table.
The cell itself becomes the constraint: filling it requires naming the Req-ID, the specific
factual claim, and the emotional register as a single atomic entry.

**Hypothesis:** R11 V-01 earned C-34 FULL by placing a 4-column table in CONVICTION DELTA
with the template "[Req-ID]'s [specific factual claim] is made visceral in this version by
[emotional register]" as an instruction below the table. The C-34 rubric language describes
the cell template as "pre-defined" and notes it converts three things to remember into "one
template cell to fill." V-01 (R12) pre-places the template string directly in each data
cell row — the Amplification chain column's Exec, Dev, and Maker cells all contain the
template as the fill-in placeholder, not as a post-table reminder. This is the in-cell
ontological form: the model must replace the template tokens, not recall that it should
produce them. Conviction DELTA narrative (C-31) is subsumed by the structural table; C-32
(CONVICTION GAP DIAGNOSIS) is retained in narrative prose form. C-33 (CAMPAIGN CONVICTION
HYPOTHESIS) is retained from the R11 V-03 base. TRACEABILITY AUDIT, NEAR-DUPLICATE, and
RESIDUAL QUESTIONS are unchanged. Base: R11 V-03 (203). Predicted score: 208.

```
You are running /campaign-blueprint for: {topic}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The INERTIA MODEL is the campaign's named architectural opponent — the status quo each
artifact must displace. Name what you are betting against before defining the evidence
entity that documents it.

0. CAMPAIGN CONVICTION HYPOTHESIS — state the dominant inertia barrier before filling any
   other SETUP field. Write two items:

   Hypothesis: "The {topic} campaign must establish that [specific friction from INERTIA
   MODEL Cost] is the dominant reason [audience] cannot [achieve desired outcome], so that
   displacing [INERTIA MODEL Name] becomes the obvious move."

   Falsification conditions: "This campaign fails if: (a) the spec cannot document
   [barrier named above] as a measured cost with factual record; (b) the proposal cannot
   price [barrier] against at least one do-something alternative; (c) the pitch cannot
   make [barrier] visceral for at least one audience version. Any unmet condition means
   the CAMPAIGN CONVICTION HYPOTHESIS is unproven and the campaign is incomplete."

   Complete item 0 in full before proceeding to item 1. The hypothesis names what the
   campaign is betting against; the falsification conditions name how to know if the bet
   is lost.

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

  TRACEABILITY AUDIT
    Return to the SCOUT TRACEABILITY TABLE in CAMPAIGN SETUP. For each row in the table:
    - Name the REQUIREMENTS Must-have that addresses this friction (by Req-ID).
    - Confirm the Must-have appears in the written spec as a distinct bulleted item.
    If any row has no corresponding Must-have in the written spec, name the gap explicitly.
    State which scout namespace could surface requirements to close it.

  CONVICTION DELTA
    Complete every cell in the amplification table below before writing any narrative
    interpretation. The Amplification chain column is pre-structured per row — each cell
    contains the fill-in template. Replace the bracketed tokens with the specific values
    from this campaign. An entry that leaves any bracket unfilled fails the row.

    | Version | Conviction established (visceral claim) | Grounding Req-ID(s) | Amplification chain |
    |---------|-----------------------------------------|---------------------|-----------------------------------------------------|
    | Exec    |                                         |                     | [Req-ID]'s [specific factual claim from Must-have] is made visceral in this version by [emotional register] |
    | Dev     |                                         |                     | [Req-ID]'s [specific factual claim from Must-have] is made visceral in this version by [emotional register] |
    | Maker   |                                         |                     | [Req-ID]'s [specific factual claim from Must-have] is made visceral in this version by [emotional register] |

    Conviction established: the single visceral claim this pitch version makes about the
    INERTIA MODEL Cost that the spec and proposal could not make — one sentence maximum.
    Grounding Req-ID(s): the canonical Must-have identifier(s) from Artifact 1 REQUIREMENTS
    (e.g., R-01, R-04) whose factual record this pitch version emotionally amplifies.
    Required per row. If no single Must-have is the primary foundation, name the closest
    Req-ID and replace the Amplification chain template with: "GAP — [Req-ID] is the
    closest anchor but does not fully ground this conviction claim because [reason]."

  NEAR-DUPLICATE CONTENT
    Name any passage you nearly copied from the spec or proposal.
    State what you changed to make it conviction-bearing rather than informational.

  RESIDUAL QUESTIONS
    What would a specific scout signal resolve that no artifact answered from existing evidence?
    Recommend a namespace for each.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN CLOSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

For "Conviction type met": assess whether each artifact's dominant register matches its
declared conviction type — Factual (spec), Optionality (proposal), Emotional (pitch).
Mark Y if dominant register matches; partial if conviction types are mixed; N if the
artifact's primary register fails the declared type.

| Artifact | Path                                                         | Scout signal consumed | Conviction type met | Open questions |
|----------|--------------------------------------------------------------|-----------------------|---------------------|----------------|
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md               | (namespace or none)   | Y / partial / N     | (list)         |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md       | (namespace or none)   | Y / partial / N     | (list)         |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md            | (namespace or none)   | Y / partial / N     | (list)         |

CONVICTION GAP DIAGNOSIS
  For each row marked partial or N in "Conviction type met":
  - Name the specific sub-section of the artifact where the conviction register breaks down
    (e.g., "Spec REQUIREMENTS — Must-haves are framed as emotional appeals rather than
    factual record; Cost is argued rather than documented").
  - Name the scout namespace and signal type that would supply evidence to strengthen the
    artifact's conviction register toward its declared type.
  If all rows are Y, write: "No conviction gaps detected."

List any open question a future signal could resolve, with recommended namespace for each.
```

---

## V-02 — C-35 Artifact-Row Pre-Declaration

**Axis:** Output format — CAMPAIGN CLOSE's CONVICTION GAP DIAGNOSIS is restructured as a
6-column table with one row pre-declared per artifact (Spec, Proposal, Pitch), making
structural incompleteness visible: if the CLOSE tracking table marks an artifact partial or
N, its row in the diagnosis table must be populated. A blank row where the CLOSE table
shows partial or N is a visible structural gap — no scanning of prose to detect omission.

**Hypothesis:** R11 V-02 earned C-35 FULL with a 6-column table and a single pre-declared
empty row. The C-35 rubric tests whether "the table structure makes it impossible to record
a gap without populating observed and declared registers as separate data fields." Pre-
declaring three rows (one per artifact) tightens this structural constraint: the model must
fill each artifact's row or explicitly leave it blank — and a blank row when the CLOSE
table marks partial or N is immediately visible as a structural incompleteness, without
requiring the reviewer to check whether an artifact was omitted. The distinct-column test
(Register found vs Register declared) is preserved from R11 V-02. CONVICTION DELTA is
retained in narrative C-31 form. C-33 (CAMPAIGN CONVICTION HYPOTHESIS) is retained from
the R11 V-03 base. TRACEABILITY AUDIT, NEAR-DUPLICATE, and RESIDUAL QUESTIONS are
unchanged. Base: R11 V-03 (203). Predicted score: 208.

```
You are running /campaign-blueprint for: {topic}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The INERTIA MODEL is the campaign's named architectural opponent — the status quo each
artifact must displace. Name what you are betting against before defining the evidence
entity that documents it.

0. CAMPAIGN CONVICTION HYPOTHESIS — state the dominant inertia barrier before filling any
   other SETUP field. Write two items:

   Hypothesis: "The {topic} campaign must establish that [specific friction from INERTIA
   MODEL Cost] is the dominant reason [audience] cannot [achieve desired outcome], so that
   displacing [INERTIA MODEL Name] becomes the obvious move."

   Falsification conditions: "This campaign fails if: (a) the spec cannot document
   [barrier named above] as a measured cost with factual record; (b) the proposal cannot
   price [barrier] against at least one do-something alternative; (c) the pitch cannot
   make [barrier] visceral for at least one audience version. Any unmet condition means
   the CAMPAIGN CONVICTION HYPOTHESIS is unproven and the campaign is incomplete."

   Complete item 0 in full before proceeding to item 1. The hypothesis names what the
   campaign is betting against; the falsification conditions name how to know if the bet
   is lost.

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

  TRACEABILITY AUDIT
    Return to the SCOUT TRACEABILITY TABLE in CAMPAIGN SETUP. For each row in the table:
    - Name the REQUIREMENTS Must-have that addresses this friction (by Req-ID).
    - Confirm the Must-have appears in the written spec as a distinct bulleted item.
    If any row has no corresponding Must-have in the written spec, name the gap explicitly.
    State which scout namespace could surface requirements to close it.

  CONVICTION DELTA
    Exec version: what emotional conviction about the INERTIA MODEL Cost does this establish
                  that the factual and optionality artifacts could not make visceral?
                  Name the specific spec Must-have Req-ID(s) whose factual record this version
                  emotionally amplifies. If no single Must-have is the primary foundation,
                  name the closest Req-ID and state the gap.
    Dev version: what emotional conviction about the INERTIA MODEL Cost does this establish
                 that the factual and optionality artifacts could not make visceral?
                 Name the specific spec Must-have Req-ID(s) whose factual record this version
                 emotionally amplifies. If no single Must-have is the primary foundation,
                 name the closest Req-ID and state the gap.
    Maker version: what emotional conviction about the INERTIA MODEL Cost does this establish
                   that the factual and optionality artifacts could not make visceral?
                   Name the specific spec Must-have Req-ID(s) whose factual record this version
                   emotionally amplifies. If no single Must-have is the primary foundation,
                   name the closest Req-ID and state the gap.

  NEAR-DUPLICATE CONTENT
    Name any passage you nearly copied from the spec or proposal.
    State what you changed to make it conviction-bearing rather than informational.

  RESIDUAL QUESTIONS
    What would a specific scout signal resolve that no artifact answered from existing evidence?
    Recommend a namespace for each.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN CLOSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

For "Conviction type met": assess whether each artifact's dominant register matches its
declared conviction type — Factual (spec), Optionality (proposal), Emotional (pitch).
Mark Y if dominant register matches; partial if conviction types are mixed; N if the
artifact's primary register fails the declared type.

| Artifact | Path                                                         | Scout signal consumed | Conviction type met | Open questions |
|----------|--------------------------------------------------------------|-----------------------|---------------------|----------------|
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md               | (namespace or none)   | Y / partial / N     | (list)         |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md       | (namespace or none)   | Y / partial / N     | (list)         |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md            | (namespace or none)   | Y / partial / N     | (list)         |

CONVICTION GAP DIAGNOSIS
  For each row marked partial or N above, complete that artifact's row in the diagnosis
  table below. One row is pre-declared per artifact. A row left blank when the CLOSE table
  marks that artifact partial or N is a structural incompleteness in this diagnosis.
  If all three CLOSE rows are Y, write "No conviction gaps detected." after the table.

  | Artifact | Sub-section where gap originates | Register found | Register declared | Scout sub-skill | Evidence needed |
  |----------|----------------------------------|----------------|-------------------|-----------------|-----------------|
  | Spec     |                                  |                |                   |                 |                 |
  | Proposal |                                  |                |                   |                 |                 |
  | Pitch    |                                  |                |                   |                 |                 |

  Sub-section where gap originates: the specific named sub-section within the artifact
  where register mismatch originates — not the artifact name alone (e.g., not "Spec" but
  "Spec REQUIREMENTS — Must-haves framed as prescriptions rather than documented facts").
  Register found: one word — Factual, Optionality, or Emotional — the dominant register
  observed in that sub-section as written. A single word; no phrases.
  Register declared: the conviction type declared in the artifact contract matrix for that
  artifact — Factual for Spec, Optionality for Proposal, Emotional for Pitch. Copy from
  the contract matrix verbatim; do not infer or paraphrase. Register found and Register
  declared are structurally distinct data fields: a combined mismatch description does not
  satisfy both columns.
  Scout sub-skill: the specific sub-skill identifier — not the namespace alone — that
  would surface evidence to shift Register found toward Register declared (e.g.,
  scout-requirements, scout-feasibility, scout-market, scout-positioning,
  scout-competitors, scout-stakeholders, scout-compliance). A namespace-only entry
  (e.g., "scout") does not pass this column.
  Evidence needed: one sentence describing the specific signal the named Scout sub-skill
  would produce that closes the register gap in this row.

List any open question a future signal could resolve, with recommended namespace for each.
```

---

## V-03 — Structural Traceability Audit Table (C-36 Probe)

**Axis:** Output format — CAMPAIGN REFLECTION's TRACEABILITY AUDIT sub-field is converted
from a prose verification directive into a structural per-row fill-in table. The table
pre-declares the Req-ID and Friction columns from the SETUP SCOUT TRACEABILITY TABLE,
making it impossible to complete without populating each row's Must-have verification
result. A N row with an empty Gap column is visibly incomplete — structural incompleteness
cannot be hidden in prose.

**Hypothesis:** C-29 instructs per-row verification in prose form: "for each row, name the
Req-ID, confirm it appears, name the gap." The C-34 and C-35 pattern shows that converting
epistemic instructions into ontological tables earns new structural criteria. A structural
TRACEABILITY AUDIT table (six columns: Req-ID | Scout-Requirements Friction | Must-have
found in spec? | Must-have text | Gap | Scout namespace) applies the same pattern to C-29:
the table enforces per-row completeness as a data constraint, not a remembered instruction.
A row where Must-have found = N and Gap is blank is visually incomplete in a way that prose
is not. CONVICTION DELTA is retained in narrative C-31 form. CONVICTION GAP DIAGNOSIS is
retained in narrative C-32 form. C-33 (CAMPAIGN CONVICTION HYPOTHESIS) is retained from
the R11 V-03 base. Base: R11 V-03 (203). Predicted score: 208 if C-36 exists; 203 if not.

```
You are running /campaign-blueprint for: {topic}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The INERTIA MODEL is the campaign's named architectural opponent — the status quo each
artifact must displace. Name what you are betting against before defining the evidence
entity that documents it.

0. CAMPAIGN CONVICTION HYPOTHESIS — state the dominant inertia barrier before filling any
   other SETUP field. Write two items:

   Hypothesis: "The {topic} campaign must establish that [specific friction from INERTIA
   MODEL Cost] is the dominant reason [audience] cannot [achieve desired outcome], so that
   displacing [INERTIA MODEL Name] becomes the obvious move."

   Falsification conditions: "This campaign fails if: (a) the spec cannot document
   [barrier named above] as a measured cost with factual record; (b) the proposal cannot
   price [barrier] against at least one do-something alternative; (c) the pitch cannot
   make [barrier] visceral for at least one audience version. Any unmet condition means
   the CAMPAIGN CONVICTION HYPOTHESIS is unproven and the campaign is incomplete."

   Complete item 0 in full before proceeding to item 1. The hypothesis names what the
   campaign is betting against; the falsification conditions name how to know if the bet
   is lost.

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

  TRACEABILITY AUDIT
    Return to the SCOUT TRACEABILITY TABLE in CAMPAIGN SETUP. Pre-populate the Req-ID and
    Friction columns of the audit table below from that table now; complete the remaining
    columns after writing Artifact 1. One audit row per SETUP table row.

    | Req-ID | Scout-Requirements Friction | Must-have found in spec? | Must-have text (exact phrase) | Gap (if N) | Scout namespace |
    |--------|-----------------------------|--------------------------|-------------------------------|------------|-----------------|
    |        |                             | Y / N                    |                               |            |                 |

    Req-ID: the canonical identifier from the SETUP SCOUT TRACEABILITY TABLE (e.g., R-01,
    R-02). Must match the identifier used in Artifact 1 REQUIREMENTS verbatim.
    Scout-Requirements Friction: the friction description copied directly from the SETUP
    table. Pre-fill this column before Artifact 1.
    Must-have found in spec?: Y if a distinct bulleted Must-have item in Artifact 1
    REQUIREMENTS directly addresses this friction; N if no such item exists.
    Must-have text: the exact phrase of the Must-have from Artifact 1 REQUIREMENTS. Leave
    blank if Must-have found = N.
    Gap: if Must-have found = N, state explicitly what requirement is absent and why this
    friction is unaddressed. A N row with a blank Gap column is a structural incompleteness
    in this audit — the table form makes the absence visible without prose scanning.
    Scout namespace: for each N row, name the scout namespace that could surface the missing
    requirement (e.g., scout-requirements, scout-market, scout-stakeholders). Leave blank
    if Must-have found = Y.

  CONVICTION DELTA
    Exec version: what emotional conviction about the INERTIA MODEL Cost does this establish
                  that the factual and optionality artifacts could not make visceral?
                  Name the specific spec Must-have Req-ID(s) whose factual record this version
                  emotionally amplifies. If no single Must-have is the primary foundation,
                  name the closest Req-ID and state the gap.
    Dev version: what emotional conviction about the INERTIA MODEL Cost does this establish
                 that the factual and optionality artifacts could not make visceral?
                 Name the specific spec Must-have Req-ID(s) whose factual record this version
                 emotionally amplifies. If no single Must-have is the primary foundation,
                 name the closest Req-ID and state the gap.
    Maker version: what emotional conviction about the INERTIA MODEL Cost does this establish
                   that the factual and optionality artifacts could not make visceral?
                   Name the specific spec Must-have Req-ID(s) whose factual record this version
                   emotionally amplifies. If no single Must-have is the primary foundation,
                   name the closest Req-ID and state the gap.

  NEAR-DUPLICATE CONTENT
    Name any passage you nearly copied from the spec or proposal.
    State what you changed to make it conviction-bearing rather than informational.

  RESIDUAL QUESTIONS
    What would a specific scout signal resolve that no artifact answered from existing evidence?
    Recommend a namespace for each.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN CLOSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

For "Conviction type met": assess whether each artifact's dominant register matches its
declared conviction type — Factual (spec), Optionality (proposal), Emotional (pitch).
Mark Y if dominant register matches; partial if conviction types are mixed; N if the
artifact's primary register fails the declared type.

| Artifact | Path                                                         | Scout signal consumed | Conviction type met | Open questions |
|----------|--------------------------------------------------------------|-----------------------|---------------------|----------------|
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md               | (namespace or none)   | Y / partial / N     | (list)         |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md       | (namespace or none)   | Y / partial / N     | (list)         |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md            | (namespace or none)   | Y / partial / N     | (list)         |

CONVICTION GAP DIAGNOSIS
  For each row marked partial or N in "Conviction type met":
  - Name the specific sub-section of the artifact where the conviction register breaks down
    (e.g., "Spec REQUIREMENTS — Must-haves are framed as emotional appeals rather than
    factual record; Cost is argued rather than documented").
  - Name the scout namespace and signal type that would supply evidence to strengthen the
    artifact's conviction register toward its declared type.
  If all rows are Y, write: "No conviction gaps detected."

List any open question a future signal could resolve, with recommended namespace for each.
```

---

## V-04 — C-34 + C-35 Full Combination

**Axis:** CAMPAIGN REFLECTION (C-34 in-cell template) + CAMPAIGN CLOSE (C-35 artifact-row
pre-declaration) — both structural upgrades applied simultaneously on the R11 V-03 base
(203: C-33 + C-31 + C-32). This is the confirmed 213 path: three phases each contribute
one structural criterion — SETUP item 0 (C-33), REFLECTION CONVICTION DELTA (C-34), CLOSE
CONVICTION GAP DIAGNOSIS (C-35).

**Hypothesis:** R11 V-04 (inferred 213) combines the tightened C-31 citation-direction
table, the tightened C-32 subsection-prescription table, and the falsifiable C-33
hypothesis. Under v12, that combination earns C-34 FULL + C-35 FULL because the tightened
C-31 implementation is the 4-column table (C-34) and the tightened C-32 implementation is
the 6-column table (C-35). V-04 (R12) replicates that combination explicitly: C-33 in
SETUP item 0 (falsifiable hypothesis with three-part falsification conditions), C-34 in
REFLECTION CONVICTION DELTA (4-column table with in-cell template placeholders), C-35 in
CLOSE CONVICTION GAP DIAGNOSIS (6-column table with per-artifact row pre-declaration).
TRACEABILITY AUDIT remains in C-29 prose form. NEAR-DUPLICATE and RESIDUAL unchanged.
Predicted score: 213.

```
You are running /campaign-blueprint for: {topic}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The INERTIA MODEL is the campaign's named architectural opponent — the status quo each
artifact must displace. Name what you are betting against before defining the evidence
entity that documents it.

0. CAMPAIGN CONVICTION HYPOTHESIS — state the dominant inertia barrier before filling any
   other SETUP field. Write two items:

   Hypothesis: "The {topic} campaign must establish that [specific friction from INERTIA
   MODEL Cost] is the dominant reason [audience] cannot [achieve desired outcome], so that
   displacing [INERTIA MODEL Name] becomes the obvious move."

   Falsification conditions: "This campaign fails if: (a) the spec cannot document
   [barrier named above] as a measured cost with factual record; (b) the proposal cannot
   price [barrier] against at least one do-something alternative; (c) the pitch cannot
   make [barrier] visceral for at least one audience version. Any unmet condition means
   the CAMPAIGN CONVICTION HYPOTHESIS is unproven and the campaign is incomplete."

   Complete item 0 in full before proceeding to item 1. The hypothesis names what the
   campaign is betting against; the falsification conditions name how to know if the bet
   is lost.

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

  TRACEABILITY AUDIT
    Return to the SCOUT TRACEABILITY TABLE in CAMPAIGN SETUP. For each row in the table:
    - Name the REQUIREMENTS Must-have that addresses this friction (by Req-ID).
    - Confirm the Must-have appears in the written spec as a distinct bulleted item.
    If any row has no corresponding Must-have in the written spec, name the gap explicitly.
    State which scout namespace could surface requirements to close it.

  CONVICTION DELTA
    Complete every cell in the amplification table below before writing any narrative
    interpretation. The Amplification chain column is pre-structured per row — each cell
    contains the fill-in template. Replace the bracketed tokens with the specific values
    from this campaign. An entry that leaves any bracket unfilled fails the row.

    | Version | Conviction established (visceral claim) | Grounding Req-ID(s) | Amplification chain |
    |---------|-----------------------------------------|---------------------|-----------------------------------------------------|
    | Exec    |                                         |                     | [Req-ID]'s [specific factual claim from Must-have] is made visceral in this version by [emotional register] |
    | Dev     |                                         |                     | [Req-ID]'s [specific factual claim from Must-have] is made visceral in this version by [emotional register] |
    | Maker   |                                         |                     | [Req-ID]'s [specific factual claim from Must-have] is made visceral in this version by [emotional register] |

    Conviction established: the single visceral claim this pitch version makes about the
    INERTIA MODEL Cost that the spec and proposal could not make — one sentence maximum.
    Grounding Req-ID(s): the canonical Must-have identifier(s) from Artifact 1 REQUIREMENTS
    (e.g., R-01, R-04) whose factual record this pitch version emotionally amplifies.
    Required per row. If no single Must-have is the primary foundation, name the closest
    Req-ID and replace the Amplification chain template with: "GAP — [Req-ID] is the
    closest anchor but does not fully ground this conviction claim because [reason]."

  NEAR-DUPLICATE CONTENT
    Name any passage you nearly copied from the spec or proposal.
    State what you changed to make it conviction-bearing rather than informational.

  RESIDUAL QUESTIONS
    What would a specific scout signal resolve that no artifact answered from existing evidence?
    Recommend a namespace for each.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN CLOSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

For "Conviction type met": assess whether each artifact's dominant register matches its
declared conviction type — Factual (spec), Optionality (proposal), Emotional (pitch).
Mark Y if dominant register matches; partial if conviction types are mixed; N if the
artifact's primary register fails the declared type.

| Artifact | Path                                                         | Scout signal consumed | Conviction type met | Open questions |
|----------|--------------------------------------------------------------|-----------------------|---------------------|----------------|
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md               | (namespace or none)   | Y / partial / N     | (list)         |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md       | (namespace or none)   | Y / partial / N     | (list)         |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md            | (namespace or none)   | Y / partial / N     | (list)         |

CONVICTION GAP DIAGNOSIS
  For each row marked partial or N above, complete that artifact's row in the diagnosis
  table below. One row is pre-declared per artifact. A row left blank when the CLOSE table
  marks that artifact partial or N is a structural incompleteness in this diagnosis.
  If all three CLOSE rows are Y, write "No conviction gaps detected." after the table.

  | Artifact | Sub-section where gap originates | Register found | Register declared | Scout sub-skill | Evidence needed |
  |----------|----------------------------------|----------------|-------------------|-----------------|-----------------|
  | Spec     |                                  |                |                   |                 |                 |
  | Proposal |                                  |                |                   |                 |                 |
  | Pitch    |                                  |                |                   |                 |                 |

  Sub-section where gap originates: the specific named sub-section within the artifact
  where register mismatch originates — not the artifact name alone (e.g., not "Spec" but
  "Spec REQUIREMENTS — Must-haves framed as prescriptions rather than documented facts").
  Register found: one word — Factual, Optionality, or Emotional — the dominant register
  observed in that sub-section as written. A single word; no phrases.
  Register declared: the conviction type declared in the artifact contract matrix —
  Factual for Spec, Optionality for Proposal, Emotional for Pitch. Register found and
  Register declared are structurally distinct data fields in separate columns — a combined
  mismatch description does not satisfy both columns.
  Scout sub-skill: the specific sub-skill identifier — not the namespace alone — that
  would surface evidence to shift Register found toward Register declared (e.g.,
  scout-requirements, scout-feasibility, scout-market, scout-positioning,
  scout-competitors, scout-stakeholders, scout-compliance). A namespace-only entry
  (e.g., "scout") does not pass this column.
  Evidence needed: one sentence describing the specific signal the named Scout sub-skill
  would produce that closes the register gap in this row.

List any open question a future signal could resolve, with recommended namespace for each.
```

---

## V-05 — Minimum-Density 213 Path

**Axis:** Lifecycle compression — maximum compression of V-04 (R12) while preserving all
structural invariants required for the 213 ceiling. Every sentence not directly load-
bearing for a named criterion is stripped. The criteria that must survive intact:

- C-23: bracket notation at each of the three contract reminders (three lines retained)
- C-26: three-field INERTIA MODEL entity + three-bullet conviction-type mapping (retained)
- C-27: SCOUT TRACEABILITY TABLE in SETUP, four-column, pre-population instruction
- C-28: "As you write each Must-have, complete its Req-ID and Must-have entry in the
  SCOUT TRACEABILITY TABLE in CAMPAIGN SETUP above. Every Must-have must correspond to a
  row in that table." (retained word-for-word)
- C-29: TRACEABILITY AUDIT — named sub-field, per-row Req-ID verification, gap naming,
  scout namespace prescription (retained; surrounding explanation stripped)
- C-30: "Conviction type met" column in CLOSE + scoring instruction defining Y/partial/N
  per conviction type (one-sentence instruction + table retained)
- C-31: subsumed by C-34 table; Grounding Req-ID(s) column satisfies C-31 requirement
- C-32: subsumed by C-35 table; Sub-section and Scout sub-skill columns satisfy C-32
- C-33: CAMPAIGN CONVICTION HYPOTHESIS as item 0 — hypothesis sentence template +
  falsification conditions in three-part form (compressed, both items retained)
- C-34: 4-column CONVICTION DELTA table with in-cell template in Amplification chain
  column; all three version rows pre-declared (minimum: table + column headers + 3 rows
  with template tokens)
- C-35: 6-column CONVICTION GAP DIAGNOSIS table with Register found and Register declared
  as distinct columns; one row pre-declared per artifact (minimum: table + headers + 3
  pre-declared rows)
- C-18/C-19: double-prohibition — "not before pitch production begins, not during pitch
  production" — two arms; no compression permitted

**Hypothesis:** V-04 carries explanatory prose beyond the structural minimum. V-05 strips
every sentence not directly load-bearing for a named criterion. If V-05 scores below 213,
a stripped sentence was load-bearing; identify by diff against V-04 (R12). Predicted
score: 213.

```
You are running /campaign-blueprint for: {topic}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0. CAMPAIGN CONVICTION HYPOTHESIS:
   Hypothesis: "The {topic} campaign must establish that [friction from INERTIA MODEL Cost]
   is the dominant reason [audience] cannot [desired outcome], so that displacing [INERTIA
   MODEL Name] becomes the obvious move."
   Falsification: (a) spec cannot document barrier as measured cost; (b) proposal cannot
   price barrier against an alternative; (c) pitch cannot make barrier visceral per version.
   Write item 0 before proceeding.

1. Topic identity — one sentence: feature name, audience, problem solved.

2. INERTIA MODEL — three-field declaration:
     Name:     current behavior in shorthand
     Behavior: what users do today — one sentence
     Cost:     what that costs them — one sentence (factual, priceable, emotional)

   - Factual conviction (spec):         documents the Cost field as factual record
   - Optionality conviction (proposal): prices the Cost field against each alternative
   - Emotional conviction (pitch):      makes the Cost field visceral per audience

3. Scout inventory — glob simulations/scout/ for this topic now. Unconditional.

4. SCOUT TRACEABILITY TABLE — pre-populate from scout inventory. Fill Friction and Scout
   File from scout-requirements findings; complete Req-ID and Must-have during Artifact 1.

   | Req-ID       | Must-have (brief)    | Originating Scout-Requirements Friction      | Scout File (path or "none") |
   |--------------|----------------------|----------------------------------------------|-----------------------------|
   | (fill in A1) | (fill in A1)         |                                              |                             |
   (one row per friction; if no scout-requirements file, one row with Friction from
   INERTIA MODEL Cost and Scout File = "none")

5. Artifact contract matrix:

| Field           | Spec                                                             | Proposal                                                                    | Pitch                                                                              |
|-----------------|------------------------------------------------------------------|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| READ            | Topic identity; INERTIA MODEL (all fields); scout-requirements if found | Spec file; INERTIA MODEL Cost; scout-feasibility if found          | Proposal file; INERTIA MODEL Cost; scout-positioning if found                      |
| WRITE           | simulations/draft/specs/{topic}-spec-{date}.md                   | simulations/draft/proposals/{topic}-proposal-{date}.md                      | simulations/draft/pitches/{topic}-pitch-{date}.md                                  |
| PRESERVE        | (first artifact)                                                 | All spec design decisions — no re-opening, no new design work               | Recommended option from proposal — crystallize, do not reconsider                  |
| CARRIES FORWARD | Feature identity; INERTIA MODEL (all fields); design decisions   | Recommended option name and rationale; INERTIA MODEL Cost                   | (final artifact)                                                                   |
| CONVICTION TYPE | Factual — documents INERTIA MODEL Cost as factual record         | Optionality — prices INERTIA MODEL Cost against each alternative            | Emotional — makes INERTIA MODEL Cost visceral per audience                         |

Print the contract matrix in full before Artifact 1.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 1: SPEC — Factual Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: topic identity; INERTIA MODEL (Name, Behavior, Cost); scout-requirements if found.
                    PRESERVE: (first artifact).
                    CONVICTION TYPE: Factual [INERTIA MODEL Cost → factual record]

Sections (all required):

  PURPOSE        — INERTIA MODEL Name and Behavior; Cost as factual record.
  REQUIREMENTS   — Bulleted, MoSCoW-tagged (M/S/C/W). Pull scout-requirements if available.
                   As you write each Must-have, complete its Req-ID and Must-have entry in
                   the SCOUT TRACEABILITY TABLE in CAMPAIGN SETUP above. Every Must-have
                   must correspond to a row in that table.
  DESIGN         — Components, data flow, key decisions.
  CONSTRAINTS    — Technical, team, timeline, dependency limits.
  OPEN QUESTIONS — Unknowns; namespace for each.

GATE: Do not begin Artifact 2 until simulations/draft/specs/{topic}-spec-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 2: PROPOSAL — Optionality Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: spec file; INERTIA MODEL Cost; scout-feasibility if found.
                    PRESERVE: all spec design decisions.
                    CONVICTION TYPE: Optionality [INERTIA MODEL Cost → priced against each alternative]

Option A is do-nothing — INERTIA MODEL at full Cost. State that Cost explicitly before
presenting alternatives. Every other option is measured against INERTIA MODEL Cost, not zero.

Three options minimum. Per option: Name / Description / Pros / Cons / Risk (H/M/L) /
Effort (S/M/L). Recommendation: chosen option + three reasons citing spec decisions.

GATE: Do not begin Artifact 3 until simulations/draft/proposals/{topic}-proposal-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 3: PITCH — Emotional Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: proposal file; INERTIA MODEL Cost; scout-positioning if found.
                    PRESERVE: recommended option from proposal — crystallize, do not reconsider.
                    CONVICTION TYPE: Emotional [INERTIA MODEL Cost → visceral per audience]

Each version opens with the INERTIA MODEL Cost as its hook.

Three versions in full:

EXEC (decision-makers) — urgency through compounding INERTIA MODEL Cost:
  Hook: INERTIA MODEL Cost in business terms.
  What it does: recommended option outcome framed as Cost elimination.
  Why it matters: compounding risk of sustained INERTIA MODEL Behavior.
  CTA: approve / fund / unblock.

DEV (engineers and technical leads) — urgency through blocked capability:
  Hook: what INERTIA MODEL Behavior prevents engineers from doing or building.
  What it does: references technical design from spec explicitly.
  Why it matters: technical debt or opportunity cost of sustained INERTIA MODEL Behavior.
  CTA: join beta / review spec / contribute.

MAKER (practitioners — plain language only) — urgency through daily INERTIA MODEL Cost:
  Hook: specific daily friction of INERTIA MODEL Behavior for this audience.
  What it does: no spec or proposal jargon — only what changes in daily work.
  Why it matters: time saved and steps removed from INERTIA MODEL Behavior.
  CTA: try it / sign up / start now.

ANTI-POSITIONING (shared): what this feature is NOT, two sentences.

GATE: Do not begin Campaign Reflection until simulations/draft/pitches/{topic}-pitch-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN REFLECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

This phase begins only after the pitch file exists on disk — not before pitch production
begins, not during pitch production. Retrospective assessment of completed artifacts.

FINDINGS:

  TRACEABILITY AUDIT
    Return to the SCOUT TRACEABILITY TABLE in CAMPAIGN SETUP. For each row:
    - Name the Must-have that addresses this friction by Req-ID.
    - Confirm it appears as a distinct bulleted item in the written spec.
    Name any row with no corresponding Must-have as a gap. State the scout namespace
    that could surface requirements to close it.

  CONVICTION DELTA
    Complete every cell. Amplification chain column has the fill-in template pre-placed
    in each row — replace bracketed tokens with campaign-specific values. No unfilled
    brackets.

    | Version | Conviction established (visceral claim) | Grounding Req-ID(s) | Amplification chain |
    |---------|-----------------------------------------|---------------------|-----------------------------------------------------|
    | Exec    |                                         |                     | [Req-ID]'s [specific factual claim] is made visceral in this version by [emotional register] |
    | Dev     |                                         |                     | [Req-ID]'s [specific factual claim] is made visceral in this version by [emotional register] |
    | Maker   |                                         |                     | [Req-ID]'s [specific factual claim] is made visceral in this version by [emotional register] |

    If no Must-have fully grounds a version, replace Amplification chain with:
    "GAP — [Req-ID] is nearest anchor but does not ground this claim because [reason]."

  NEAR-DUPLICATE CONTENT
    Any passage nearly copied from spec or proposal; what changed to make it
    conviction-bearing.

  RESIDUAL QUESTIONS
    Scout signal that would resolve what no artifact answered; namespace for each.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN CLOSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Mark "Conviction type met" Y if dominant register matches declared conviction type (Factual
for spec, Optionality for proposal, Emotional for pitch); partial if mixed; N if primary
register fails declared type.

| Artifact | Path                                                         | Scout signal consumed | Conviction type met | Open questions |
|----------|--------------------------------------------------------------|-----------------------|---------------------|----------------|
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md               | (namespace or none)   | Y / partial / N     | (list)         |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md       | (namespace or none)   | Y / partial / N     | (list)         |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md            | (namespace or none)   | Y / partial / N     | (list)         |

CONVICTION GAP DIAGNOSIS
  Complete each artifact's row if marked partial or N above. Blank row when CLOSE shows
  partial or N = structural incompleteness. If all Y: "No conviction gaps detected."

  | Artifact | Sub-section where gap originates | Register found | Register declared | Scout sub-skill | Evidence needed |
  |----------|----------------------------------|----------------|-------------------|-----------------|-----------------|
  | Spec     |                                  |                |                   |                 |                 |
  | Proposal |                                  |                |                   |                 |                 |
  | Pitch    |                                  |                |                   |                 |                 |

  Register found and Register declared: structurally distinct columns — one word each;
  combined mismatch descriptions do not satisfy both. Scout sub-skill: specific sub-skill
  identifier, not namespace (e.g., scout-requirements, not scout). Evidence needed: one
  sentence per row.

List any open question a future signal could resolve, with recommended namespace for each.
```
