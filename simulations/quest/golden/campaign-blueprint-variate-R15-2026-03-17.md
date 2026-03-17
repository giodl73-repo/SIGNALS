---
skill: quest-variate
skill_target: campaign-blueprint
date: 2026-03-17
round: 15
rubric: campaign-blueprint-rubric-v15-2026-03-17.md
---

# campaign-blueprint — Prompt Variations R15

Five complete, runnable skill body variations. Single-axis first (V-01 through V-03),
then two combinations (V-04 through V-05).

## R15 Context

R14 variants under v15 retroactive scoring:

| Variant | v14 | C-40 | C-41 | v15 |
|---------|-----|------|------|-----|
| V-01 — Single Axis Named-Row SETUP Linkage | 213 | 0 | 0 | **213** |
| V-02 — C-35 with Missing REFLECTION | ~198 | 0 | 0 | **~198** |

Neither R14 variant reaches the v14 ceiling (233) or earns C-40/C-41. V-01 has the
C-38-compliant TRACEABILITY AUDIT axis but no INERTIA MODEL MAP in SETUP. V-02 has
the INERTIA MODEL MAP in SETUP but REFLECTION is absent, failing C-34 before C-40
is reachable. The 243 ceiling requires both axes simultaneously plus C-40+C-41.

The R14 pattern isolates the two structural axes C-40 and C-41 will require:
- **Axis A** (from V-01): C-38-compliant TRACEABILITY AUDIT — named Req-ID rows
  drawn from SCOUT TRACEABILITY TABLE with explicit row-count match directive.
- **Axis B** (from V-02): INERTIA MODEL MAP in SETUP — 4-column map pre-declaring
  conviction type per artifact (Conv-ID | Artifact | Conviction type | Amplification
  chain starter), establishing named source rows for the REFLECTION CONVICTION DELTA.

C-40 requires Axis B (SETUP) AND pre-named CONVICTION DELTA rows in REFLECTION drawn
from that MAP. C-41 requires C-39 (Axis A at C-38 level + C-34 + C-35) AND C-40
simultaneously. No R14 variant holds both axes. The 243 path:

  Base from R13 V-02/V-04: 223 (C-34 + C-35 + C-36 + C-37 all FULL)
  + C-38 (named Req-ID TRACEABILITY AUDIT): +5 = 228
  + C-39 (three-table chain at C-38 level): +5 = 233
  + C-40 (INERTIA MODEL MAP + pre-named CONVICTION DELTA rows): +5 = 238
  + C-41 (inertia-linked four-table structural chain): +5 = 243

**R15 design questions:**

1. **INERTIA MODEL MAP SETUP only (V-01):** Does adding the 4-column INERTIA MODEL MAP
   to SETUP without changing CONVICTION DELTA rows establish the D15 step-1 precondition
   while confirming step-2 failure? Expected: C-40 NO CREDIT (D15 step 1 passes, step 2
   fails — anonymous Exec/Dev/Maker rows not traceable to MAP entries). Score: 233.

2. **Minimum C-40 implementation (V-02):** INERTIA MODEL MAP in SETUP plus CONVICTION
   DELTA rows pre-named from MAP (CT-Spec—Factual, CT-Prop—Optionality, CT-Pitch—
   Emotional) plus explicit row-count match directive. Combined with C-38-level
   TRACEABILITY AUDIT: does this earn C-40 FULL and C-41 FULL? Expected: 243.

3. **Phrasing register isolation (V-03):** V-02 structural tables, conversational
   imperative register throughout. Tests whether register affects ceiling scoring.
   Expected: 243.

4. **Maximum-density C-40+C-41 (V-04):** Tightest form of all four structural tables
   simultaneously — INERTIA MODEL MAP with inline match directive, CONVICTION DELTA
   with in-table MAP-citation sentinel row, TRACEABILITY AUDIT with RULE row + named
   identifiers, CONVICTION GAP DIAGNOSIS with pre-declared rows. Expected: 243.

5. **Minimum-density C-40+C-41 (V-05):** All four structural tables at minimum prose
   density. Tests whether adjacent prose is load-bearing at the 243-ceiling level.
   Expected: 243.

**Predicted scoring pattern:**

| Variant | Axis | C-38 | C-39 | C-40 | C-41 | v15 |
|---------|------|------|------|------|------|-----|
| V-01 — INERTIA MODEL MAP SETUP Only | SETUP structure | FULL | FULL | NO | NO | **233** |
| V-02 — Full C-40+C-41 Minimum Form | CONVICTION DELTA row pre-naming | FULL | FULL | FULL | FULL | **243** |
| V-03 — Conversational Register | Phrasing register | FULL | FULL | FULL | FULL | **243** |
| V-04 — Maximum-Density C-40+C-41 | All four structural axes | FULL | FULL | FULL | FULL | **243** |
| V-05 — Minimum-Density C-40+C-41 | Lifecycle compression | FULL | FULL | FULL | FULL | **243** |

V-01 is the diagnostic control: it confirms the D15 two-step inspection behaves as
specified (step 1 passes, step 2 fails when rows are anonymous). V-02 through V-05
each target 243 via different implementation paths for C-40+C-41.

---

## V-01 — INERTIA MODEL MAP SETUP Only

**Axis:** SETUP structure — add 4-column INERTIA MODEL MAP to CAMPAIGN SETUP. The
CONVICTION DELTA table in REFLECTION retains the C-34-level anonymous version rows
(Exec, Dev, Maker) unchanged from R13 V-04. The TRACEABILITY AUDIT retains the
C-38-level named Req-ID rows from SETUP SCOUT TRACEABILITY TABLE with match directive.

**Hypothesis:** The INERTIA MODEL MAP in SETUP passes D15 step 1 (the 4-column map
pre-declaring conviction type per artifact is present at rubric time, not deferred).
D15 step 2 fails: the CONVICTION DELTA rows in REFLECTION are labeled "Exec", "Dev",
"Maker" — pitch audience version names that are not traceable to any INERTIA MODEL MAP
entry. C-40 NO CREDIT. C-41 is a strict superset of C-40; C-41 NO CREDIT. The INERTIA
MODEL MAP addition is a structural precondition that does not itself earn C-40. Score
holds at 233 (C-38 FULL + C-39 FULL from the v14-ceiling base).

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

   Complete item 0 in full before proceeding to item 1.

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

5. INERTIA MODEL MAP — pre-declare the conviction type per artifact. This map is present
   at campaign start; its entries establish the named source rows for the CONVICTION DELTA
   table in CAMPAIGN REFLECTION. Fill the Amplification chain starter column now, before
   Artifact 1. Do not defer to REFLECTION.

   | Conv-ID  | Artifact | Conviction type | Amplification chain starter                                    |
   |----------|----------|-----------------|----------------------------------------------------------------|
   | CT-Spec  | Spec     | Factual         | (fill in: what factual claim anchors the spec's Cost record)   |
   | CT-Prop  | Proposal | Optionality     | (fill in: what cost framing anchors the proposal's options)    |
   | CT-Pitch | Pitch    | Emotional       | (fill in: what visceral register anchors the pitch's hook)     |

   The map declares what conviction type each artifact is responsible for establishing.
   CAMPAIGN REFLECTION will assess whether each declaration was honored.

6. Artifact contract matrix — declares what each artifact inherits, produces, protects, and carries:

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
begins, not during pitch production. Retrospective assessment of completed artifacts only.

FINDINGS:

  TRACEABILITY AUDIT
    Copy each Req-ID and Scout-Requirements Friction from the SCOUT TRACEABILITY TABLE in
    CAMPAIGN SETUP into a named row in the audit table below — one row per SETUP row. Row
    count must match SETUP exactly; a missing row is a named-entry absence visible at a
    glance, not a count check requiring external comparison.
    Pre-populate Req-ID and Friction before Artifact 1; complete remaining columns after.

    | Req-ID | Scout-Requirements Friction | Must-have found in spec? | Must-have text (exact phrase) | Gap (if N) | Scout namespace |
    |--------|-----------------------------|--------------------------|-------------------------------|------------|-----------------|
    | R-01   | (copy from SETUP row 1)     | Y / N                    |                               |            |                 |
    | R-02   | (copy from SETUP row 2)     | Y / N                    |                               |            |                 |
    (add rows to match SETUP table exactly — do not reduce row count)

    Must-have found in spec?: Y if a distinct bulleted Must-have in Artifact 1 REQUIREMENTS
    directly addresses this friction; N otherwise.
    Must-have text (exact phrase): verbatim Must-have text from Artifact 1. Blank if N.
    Gap: if N, state absent requirement explicitly. A N row with a blank Gap cell is a
    structural incompleteness — the blank cannot be a passing omission.
    Scout namespace: specific scout sub-skill for each N row. Blank if Y.

  CONVICTION DELTA
    Complete every cell. The Amplification chain column carries the fill-in template
    pre-placed inside each data cell. Replace all bracketed tokens with campaign-specific
    values. Any unfilled bracket fails the row.

    | Version | Conviction established (visceral claim) | Grounding Req-ID(s) | Amplification chain |
    |---------|-----------------------------------------|---------------------|-----------------------------------------------------|
    | Exec    |                                         |                     | [Req-ID]'s [specific factual claim from Must-have] is made visceral in this version by [emotional register] |
    | Dev     |                                         |                     | [Req-ID]'s [specific factual claim from Must-have] is made visceral in this version by [emotional register] |
    | Maker   |                                         |                     | [Req-ID]'s [specific factual claim from Must-have] is made visceral in this version by [emotional register] |

    Conviction established: the single visceral claim this pitch version makes that spec
    and proposal could not — one sentence. Grounding Req-ID(s): canonical Must-have
    identifier(s) from Artifact 1 REQUIREMENTS. Required per row.
    If no Must-have grounds a version: "GAP — [Req-ID] is closest anchor but does not
    ground this claim because [reason]."

  NEAR-DUPLICATE CONTENT
    Name any passage nearly copied from the spec or proposal.
    State what you changed to make it conviction-bearing rather than informational.

  RESIDUAL QUESTIONS
    What would a specific scout signal resolve that no artifact answered?
    Recommend a namespace for each.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN CLOSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

For "Conviction type met": Y if dominant register matches declared conviction type
(Factual for spec, Optionality for proposal, Emotional for pitch); partial if mixed;
N if primary register fails declared type.

| Artifact | Path                                                         | Scout signal consumed | Conviction type met | Open questions |
|----------|--------------------------------------------------------------|-----------------------|---------------------|----------------|
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md               | (namespace or none)   | Y / partial / N     | (list)         |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md       | (namespace or none)   | Y / partial / N     | (list)         |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md            | (namespace or none)   | Y / partial / N     | (list)         |

CONVICTION GAP DIAGNOSIS
  For each row marked partial or N above: complete that artifact's pre-declared row in the
  diagnosis table. A row left blank when CLOSE shows partial or N is a structural
  incompleteness in this diagnosis. If all three CLOSE rows are Y, write
  "No conviction gaps detected." after the table.

  | Artifact | Sub-section where gap originates | Register found | Register declared | Scout sub-skill | Evidence needed |
  |----------|----------------------------------|----------------|-------------------|-----------------|-----------------|
  | Spec     |                                  |                |                   |                 |                 |
  | Proposal |                                  |                |                   |                 |                 |
  | Pitch    |                                  |                |                   |                 |                 |

  Sub-section where gap originates: specific named sub-section — not the artifact alone
  (e.g., "Spec REQUIREMENTS — Must-haves framed as prescriptions rather than facts").
  Register found: one word only — Factual, Optionality, or Emotional. Register declared:
  one word only. These are structurally distinct columns — a combined mismatch description
  written across both columns does not satisfy either column independently.
  Scout sub-skill: specific sub-skill identifier, not namespace alone (e.g.,
  scout-requirements, scout-feasibility, scout-positioning — not "scout").
  Evidence needed: one sentence describing the signal that closes this register gap.

List any open question a future signal could resolve, with recommended namespace for each.
```

---

## V-02 — Full C-40+C-41 Minimum Form

**Axis:** CONVICTION DELTA row pre-naming — CONVICTION DELTA in REFLECTION replaces
anonymous pitch-version rows (Exec/Dev/Maker) with rows pre-named from the INERTIA
MODEL MAP (CT-Spec—Factual, CT-Prop—Optionality, CT-Pitch—Emotional), with an
explicit row-count match directive binding the table to SETUP MAP entry count.

**Hypothesis:** The INERTIA MODEL MAP in SETUP (4-column, Conv-ID pre-declared per
artifact) satisfies D15 step 1. The CONVICTION DELTA rows pre-named from that MAP
satisfy D15 step 2 (each row's conviction-type entry is a named identifier traceable
to a MAP entry — CT-Spec, CT-Prop, CT-Pitch — not introduced anonymously in
REFLECTION). The explicit row-count match directive completes C-40 FULL. Combined with
C-38 FULL (TRACEABILITY AUDIT named Req-ID rows) and the chain criterion C-39 FULL
(C-34+C-35+C-38 simultaneously), C-41 is also FULL — both SETUP-anchored tables carry
pre-named rows from their respective SETUP sources. Predicted score: 243.

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

   Complete item 0 in full before proceeding to item 1.

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

5. INERTIA MODEL MAP — pre-declare the conviction type per artifact. This map establishes
   named source rows for the CONVICTION DELTA table in CAMPAIGN REFLECTION. Fill all four
   columns now, before Artifact 1. The map is the conviction-type source of truth; do not
   introduce conviction-type identifiers in REFLECTION that are not pre-declared here.

   | Conv-ID  | Artifact | Conviction type | Amplification chain starter                                    |
   |----------|----------|-----------------|----------------------------------------------------------------|
   | CT-Spec  | Spec     | Factual         | (fill in: what factual claim anchors the spec's Cost record)   |
   | CT-Prop  | Proposal | Optionality     | (fill in: what cost framing anchors the proposal's options)    |
   | CT-Pitch | Pitch    | Emotional       | (fill in: what visceral register anchors the pitch's hook)     |

   The CONVICTION DELTA table in CAMPAIGN REFLECTION must contain exactly 3 rows — one
   per INERTIA MODEL MAP entry. A missing row is a named-conviction-type absence: CT-Spec
   absent means the Spec's Factual conviction type is untracked. This is visible at a glance
   by named-entry absence, not discoverable only by count comparison.

6. Artifact contract matrix — declares what each artifact inherits, produces, protects, and carries:

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
                   factual record.
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

Each version opens with the INERTIA MODEL Cost as its hook.

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

This phase begins only after the pitch file exists on disk. Retrospective assessment of
completed artifacts only.

FINDINGS:

  TRACEABILITY AUDIT
    Copy each Req-ID and Scout-Requirements Friction from the SCOUT TRACEABILITY TABLE in
    CAMPAIGN SETUP into a named row in the audit table below — one row per SETUP row. Row
    count must match SETUP exactly; a missing row is a named-entry absence (R-01 absent =
    that friction unaudited), not a count check requiring external comparison.
    Pre-populate Req-ID and Friction before Artifact 1; complete remaining columns after.

    | Req-ID | Scout-Requirements Friction | Must-have found in spec? | Must-have text (exact phrase) | Gap (if N) | Scout namespace |
    |--------|-----------------------------|--------------------------|-------------------------------|------------|-----------------|
    | R-01   | (copy from SETUP row 1)     | Y / N                    |                               |            |                 |
    | R-02   | (copy from SETUP row 2)     | Y / N                    |                               |            |                 |
    (add rows to match SETUP table exactly)

    Must-have found in spec?: Y if a distinct bulleted Must-have in Artifact 1 REQUIREMENTS
    directly addresses this friction; N otherwise.
    Must-have text (exact phrase): verbatim text from Artifact 1. Blank if N.
    Gap: if N, state absent requirement explicitly. N row + blank Gap = structural fail.
    Scout namespace: specific scout sub-skill for N rows. Blank if Y.

  CONVICTION DELTA
    Rows are pre-named from the INERTIA MODEL MAP in CAMPAIGN SETUP. Do not introduce
    anonymous rows — each row's Conv-ID and Conviction type must be traceable to a MAP
    entry. This table must contain exactly 3 rows (one per MAP entry). A missing row is a
    named-conviction-type absence: CT-Pitch absent means the Emotional conviction type is
    untracked, visible at a glance without count comparison.

    The Amplification chain column carries a pre-templated fill-in sequence anchored to
    the MAP's Amplification chain starter for that Conv-ID. Replace all bracketed tokens
    with campaign-specific values. An unfilled bracket fails the row.

    | Conv-ID / Conviction type | Conviction established (one-sentence claim) | Grounding Req-ID(s) | Amplification chain |
    |---------------------------|---------------------------------------------|---------------------|-----------------------------------------------------|
    | CT-Spec — Factual         |                                             |                     | (MAP starter: [CT-Spec starter]) → [Req-ID's factual claim from Must-have] → [how that claim establishes factual conviction in the spec] |
    | CT-Prop — Optionality     |                                             |                     | (MAP starter: [CT-Prop starter]) → [INERTIA MODEL Cost as Option A baseline] → [how recommended option prices against that baseline] |
    | CT-Pitch — Emotional      |                                             |                     | (MAP starter: [CT-Pitch starter]) → [Req-ID's factual claim made visceral] → [audience-specific emotional register applied] |

    Conviction established: the single claim this artifact makes that the prior artifact
    could not — one sentence. Grounding Req-ID(s): canonical Must-have identifier(s) from
    Artifact 1 REQUIREMENTS. Required per row.
    If no Must-have grounds a row: "GAP — [Req-ID] is closest anchor but does not ground
    CT-[X] conviction because [reason]."

  NEAR-DUPLICATE CONTENT
    Name any passage nearly copied from the spec or proposal.
    State what you changed to make it conviction-bearing rather than informational.

  RESIDUAL QUESTIONS
    What would a specific scout signal resolve that no artifact answered?
    Recommend a namespace for each.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN CLOSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

For "Conviction type met": Y if dominant register matches declared conviction type
(Factual for spec, Optionality for proposal, Emotional for pitch); partial if mixed;
N if primary register fails declared type.

| Artifact | Path                                                         | Scout signal consumed | Conviction type met | Open questions |
|----------|--------------------------------------------------------------|-----------------------|---------------------|----------------|
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md               | (namespace or none)   | Y / partial / N     | (list)         |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md       | (namespace or none)   | Y / partial / N     | (list)         |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md            | (namespace or none)   | Y / partial / N     | (list)         |

CONVICTION GAP DIAGNOSIS
  For each row marked partial or N above: complete that artifact's pre-declared row.
  A row left blank when CLOSE shows partial or N is a structural incompleteness.
  If all three CLOSE rows are Y, write "No conviction gaps detected." after the table.

  | Artifact | Sub-section where gap originates | Register found | Register declared | Scout sub-skill | Evidence needed |
  |----------|----------------------------------|----------------|-------------------|-----------------|-----------------|
  | Spec     |                                  |                |                   |                 |                 |
  | Proposal |                                  |                |                   |                 |                 |
  | Pitch    |                                  |                |                   |                 |                 |

  Sub-section: specific named sub-section, not artifact name alone.
  Register found: one word only. Register declared: one word only. Distinct columns.
  Scout sub-skill: specific identifier, not namespace alone.
  Evidence needed: one sentence.

List any open question a future signal could resolve, with recommended namespace for each.
```

---

## V-03 — Conversational Register

**Axis:** Phrasing register — V-02 structural tables unchanged; all instructional prose
converted to second-person imperative. Specifications become commands ("Fill in", "Do
not"), column definitions become inline guards ("If you leave this blank you break the
row"), phase headers become directives ("Your only job in this phase is..."). The
structural tables — INERTIA MODEL MAP, SCOUT TRACEABILITY TABLE, TRACEABILITY AUDIT,
CONVICTION DELTA, CONVICTION GAP DIAGNOSIS — are identical to V-02 in column count,
column names, row pre-declaration, and match directives.

**Hypothesis:** Structural scoring criteria (C-34, C-35, C-38, C-39, C-40, C-41) are
column-count and row-naming properties of the tables, not prose register properties.
Conversational register leaves the structural tables intact; scoring results should
match V-02 exactly. Predicted score: 243. Open question: does imperative register
create more reliable execution (fewer unfilled brackets) than formal specification
language, even if rubric scoring is identical?

```
You are running /campaign-blueprint for: {topic}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Your job in SETUP is to name the enemy before you write a single word of the campaign.
The INERTIA MODEL is the status-quo behavior you are betting against. Fill every SETUP
field before Artifact 1 starts. Nothing is optional.

0. Write the CAMPAIGN CONVICTION HYPOTHESIS first. Two parts:

   Hypothesis: "The {topic} campaign must establish that [specific friction from INERTIA
   MODEL Cost] is the dominant reason [audience] cannot [achieve desired outcome], so that
   displacing [INERTIA MODEL Name] becomes the obvious move."

   Falsification conditions: "This campaign fails if: (a) the spec cannot document
   [barrier] as a measured cost with factual record; (b) the proposal cannot price
   [barrier] against at least one alternative; (c) the pitch cannot make [barrier]
   visceral for at least one audience version."

   Do not move to item 1 until both parts are written in full.

1. Write one sentence: feature name, audience, problem solved.

2. Declare the INERTIA MODEL:
     Name:     one short phrase — what is the current behavior called?
     Behavior: what do users do today without this feature?
     Cost:     what does that cost them? Cover factual, priceable, and emotional.

   How the conviction types use the INERTIA MODEL:
   - Spec   → documents Cost as factual record (Factual conviction)
   - Proposal → prices Cost against alternatives (Optionality conviction)
   - Pitch  → makes Cost visceral per audience (Emotional conviction)

3. Run glob simulations/scout/ for this topic right now. List every file. Do this
   unconditionally — do not skip if no scout signals exist.

4. Fill the SCOUT TRACEABILITY TABLE. One row per friction from scout-requirements.
   Fill Originating Friction and Scout File now. Fill Req-ID and Must-have during
   Artifact 1 REQUIREMENTS as you write each Must-have.

   | Req-ID       | Must-have (brief)    | Originating Scout-Requirements Friction      | Scout File (path or "none") |
   |--------------|----------------------|----------------------------------------------|-----------------------------|
   | (fill in A1) | (fill in A1)         |                                              |                             |
   (If no scout-requirements file: one row, Friction from INERTIA MODEL Cost, Scout File = "none")

5. Fill the INERTIA MODEL MAP now, before Artifact 1. Every cell. This map controls
   what row names the CONVICTION DELTA table will use in REFLECTION — you cannot add
   conviction-type identifiers in REFLECTION that are not in this MAP.

   | Conv-ID  | Artifact | Conviction type | Amplification chain starter                                    |
   |----------|----------|-----------------|----------------------------------------------------------------|
   | CT-Spec  | Spec     | Factual         | (write the opening factual move for spec's conviction chain)   |
   | CT-Prop  | Proposal | Optionality     | (write the opening optionality move for proposal's chain)      |
   | CT-Pitch | Pitch    | Emotional       | (write the opening emotional move for pitch's conviction chain) |

   The CONVICTION DELTA in REFLECTION gets exactly 3 rows — CT-Spec, CT-Prop, CT-Pitch.
   A missing row is CT-[X] absent. That is a named failure, not a count discrepancy.

6. Print the artifact contract matrix. Do not start Artifact 1 until it is printed.

| Field           | Spec                                                             | Proposal                                                                    | Pitch                                                                              |
|-----------------|------------------------------------------------------------------|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| READ            | Topic identity; INERTIA MODEL (all fields); scout-requirements if found | Spec file; INERTIA MODEL Cost; scout-feasibility if found          | Proposal file; INERTIA MODEL Cost; scout-positioning if found                      |
| WRITE           | simulations/draft/specs/{topic}-spec-{date}.md                   | simulations/draft/proposals/{topic}-proposal-{date}.md                      | simulations/draft/pitches/{topic}-pitch-{date}.md                                  |
| PRESERVE        | (first artifact)                                                 | All spec design decisions — do not re-open anything                         | Recommended option — crystallize it, do not reconsider                             |
| CARRIES FORWARD | Feature identity; INERTIA MODEL (all fields); design decisions   | Recommended option + rationale; INERTIA MODEL Cost                          | (final artifact)                                                                   |
| CONVICTION TYPE | Factual — INERTIA MODEL Cost as factual record                   | Optionality — Cost priced against each alternative                          | Emotional — Cost visceral per audience                                             |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 1: SPEC — Factual Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
READ: topic identity; INERTIA MODEL; scout-requirements if found.
Your conviction type here is Factual. Document what the INERTIA MODEL costs users
before you prescribe what replaces it.

Write these sections — all of them:

  PURPOSE        — Name the INERTIA MODEL, describe its Behavior, document the Cost as
                   factual record. Show the reader the problem before showing the solution.
  REQUIREMENTS   — Bulleted list, MoSCoW-tagged (M/S/C/W). For each Must-have: fill in
                   its Req-ID and entry in the SCOUT TRACEABILITY TABLE right then.
                   Every Must-have needs a SETUP table row. No orphan Must-haves.
  DESIGN         — Components, data flow, key decisions. Specific enough to build from.
  CONSTRAINTS    — Technical, team, timeline, dependency limits.
  OPEN QUESTIONS — What you do not know. Name a namespace for each.

Write to disk: simulations/draft/specs/{topic}-spec-{date}.md
Do not start Artifact 2 until that file exists.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 2: PROPOSAL — Optionality Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
READ: spec file; INERTIA MODEL Cost; scout-feasibility if found.
PRESERVE: every spec design decision — do not re-open anything the spec settled.
Your conviction type here is Optionality. Option A is do-nothing at full INERTIA MODEL
Cost — state that cost explicitly before presenting any other option.

Three options minimum. Option A = do-nothing; its cost = the INERTIA MODEL Cost, stated
concretely. Every other option is measured against Option A, not against zero.
Per option: Name / Description / Pros / Cons / Risk (H/M/L) / Effort (S/M/L).
Recommendation: pick one option, give three reasons, each citing a spec decision.

Write to disk: simulations/draft/proposals/{topic}-proposal-{date}.md
Do not start Artifact 3 until that file exists.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 3: PITCH — Emotional Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
READ: proposal file; INERTIA MODEL Cost; scout-positioning if found.
PRESERVE: the recommended option from the proposal — crystallize it, do not question it.
Your conviction type here is Emotional. Open every version with the INERTIA MODEL Cost
as the hook. The audience has facts (spec) and options (proposal). Make the Cost felt.

Write all three versions:

EXEC — urgency through compounding Cost:
  Hook: Cost in business terms. What it does: Cost elimination framed as outcome.
  Why: compounding risk of sustained Behavior. CTA: approve / fund / unblock.

DEV — urgency through blocked capability:
  Hook: what INERTIA MODEL Behavior blocks engineers from building.
  What it does: reference the spec's technical design explicitly.
  Why: technical debt of sustained Behavior. CTA: join beta / review spec / contribute.

MAKER — plain language only, no spec terms, no proposal jargon:
  Hook: the daily friction of INERTIA MODEL Behavior for this person.
  What it does: what changes in their daily work.
  Why: time saved, steps removed. CTA: try it / sign up / start now.

ANTI-POSITIONING: two sentences — what this feature is NOT.

Write to disk: simulations/draft/pitches/{topic}-pitch-{date}.md
Do not start Campaign Reflection until that file exists.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN REFLECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Start here only after the pitch file is on disk. This is retrospective — you are
assessing completed artifacts, not generating new ones.

FINDINGS:

  TRACEABILITY AUDIT
    Take every row from the SCOUT TRACEABILITY TABLE in CAMPAIGN SETUP. Copy its Req-ID
    and Friction into a named row here — one row per SETUP row, no more, no less.
    Row count here must match SETUP. If R-02 is missing here, that is R-02 absent — a
    named gap, not a count discrepancy. Pre-fill Req-ID and Friction before Artifact 1;
    complete the rest after all artifacts exist.

    | Req-ID | Scout-Requirements Friction | Must-have found in spec? | Must-have text (exact phrase) | Gap (if N) | Scout namespace |
    |--------|-----------------------------|--------------------------|-------------------------------|------------|-----------------|
    | R-01   | (paste from SETUP row 1)    | Y / N                    |                               |            |                 |
    | R-02   | (paste from SETUP row 2)    | Y / N                    |                               |            |                 |
    (match SETUP row count exactly)

    Must-have found in spec?: Y = a distinct Must-have in Artifact 1 REQUIREMENTS covers
    this friction directly. N = nothing covers it.
    Must-have text: the verbatim Must-have text. Leave blank only if Y/N = N.
    Gap: if N, write what requirement is absent. Blank + N = broken row. Fix it.
    Scout namespace: sub-skill name for N rows (e.g., scout-requirements). Blank if Y.

  CONVICTION DELTA
    Use exactly the three rows from the INERTIA MODEL MAP. Do not use Exec/Dev/Maker here
    — those are pitch audience labels, not conviction-type identifiers. Each row here
    answers: did this artifact establish its declared conviction type?

    Three rows required (CT-Spec, CT-Prop, CT-Pitch). If a row is missing, that conviction
    type is untracked. An unfilled bracket in the Amplification chain fails the row.

    | Conv-ID / Conviction type | Conviction established (one-sentence claim) | Grounding Req-ID(s) | Amplification chain |
    |---------------------------|---------------------------------------------|---------------------|-----------------------------------------------------|
    | CT-Spec — Factual         |                                             |                     | (MAP starter: [CT-Spec starter]) → [Req-ID's factual claim] → [how the spec locked that claim as record] |
    | CT-Prop — Optionality     |                                             |                     | (MAP starter: [CT-Prop starter]) → [Option A = INERTIA MODEL Cost stated] → [how the recommendation prices against that baseline] |
    | CT-Pitch — Emotional      |                                             |                     | (MAP starter: [CT-Pitch starter]) → [Req-ID's claim made visceral] → [which audience register carried it furthest] |

    Conviction established: what this artifact established that the previous one could not.
    One sentence. Grounding Req-ID(s): which Must-have anchors it. Required — no
    ungrounded claims.
    No grounding? Write: "GAP — [Req-ID] nearest; does not ground CT-[X] because [reason]."

  NEAR-DUPLICATE CONTENT — passage copied; what you changed to make it conviction-bearing.
  RESIDUAL QUESTIONS — what scout signal would resolve what no artifact answered; namespace.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN CLOSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Fill the summary table. Y = dominant register matches declared conviction type.
Partial = mixed. N = primary register fails declared type.

| Artifact | Path                                                         | Scout signal consumed | Conviction type met | Open questions |
|----------|--------------------------------------------------------------|-----------------------|---------------------|----------------|
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md               | (namespace or none)   | Y / partial / N     | (list)         |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md       | (namespace or none)   | Y / partial / N     | (list)         |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md            | (namespace or none)   | Y / partial / N     | (list)         |

CONVICTION GAP DIAGNOSIS
  For each partial or N row above: fill that artifact's row in the diagnosis table.
  A blank row when the CLOSE table shows partial or N is a broken diagnosis. Fix it.
  All three Y? Write "No conviction gaps detected." after the table.

  | Artifact | Sub-section where gap originates | Register found | Register declared | Scout sub-skill | Evidence needed |
  |----------|----------------------------------|----------------|-------------------|-----------------|-----------------|
  | Spec     |                                  |                |                   |                 |                 |
  | Proposal |                                  |                |                   |                 |                 |
  | Pitch    |                                  |                |                   |                 |                 |

  Sub-section: specific sub-section name, not just the artifact (e.g., "Spec PURPOSE —
  Cost described as opinion not factual record").
  Register found: one word. Register declared: one word. Separate columns — do not merge.
  Scout sub-skill: exact sub-skill name, not namespace (e.g., scout-requirements).
  Evidence needed: one sentence.

List open questions with recommended namespace for each.
```

---

## V-04 — Maximum-Density C-40+C-41

**Axis:** All four structural axes at maximum enforcement density simultaneously.
- INERTIA MODEL MAP: Conv-ID column is the primary key; in-table directive row appears
  below headers binding CONVICTION DELTA to MAP before any data row is read.
- CONVICTION DELTA: MAP-linked rows (CT-Spec/CT-Prop/CT-Pitch) with in-table sentinel
  row stating the match directive, parallel to the RULE row in TRACEABILITY AUDIT.
- TRACEABILITY AUDIT: named Req-ID rows from SETUP + RULE sentinel row (matching V-03
  R13 tightest form) + explicit match directive in instructions.
- CONVICTION GAP DIAGNOSIS: three pre-declared artifact rows with explicit Register
  found/declared column distinction directive embedded in table caption.

**Hypothesis:** The maximum-density combination tests whether structural enforcement
is more reliable when every constraint is embedded in the table structure itself rather
than described in adjacent prose. Each table carries its own enforcement rule as a
non-data row — the model encounters the rule before writing any data cell. This is the
tightest form achievable under the current structural criteria. Predicted score: 243.

```
You are running /campaign-blueprint for: {topic}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The INERTIA MODEL is the campaign's named architectural opponent. Fill all SETUP tables
before Artifact 1. No SETUP field may be deferred to REFLECTION.

0. CAMPAIGN CONVICTION HYPOTHESIS — two required items, completed before item 1:

   Hypothesis: "The {topic} campaign must establish that [specific friction from INERTIA
   MODEL Cost] is the dominant reason [audience] cannot [achieve desired outcome], so that
   displacing [INERTIA MODEL Name] becomes the obvious move."

   Falsification conditions: "This campaign fails if: (a) spec cannot document [barrier]
   as measured cost with factual record; (b) proposal cannot price [barrier] against an
   alternative; (c) pitch cannot make [barrier] visceral per version."

1. Topic identity — one sentence.

2. INERTIA MODEL:
     Name:     current behavior shorthand
     Behavior: what users do today — one sentence
     Cost:     what that costs them — one sentence, covering factual/priceable/emotional

   Conviction map: Factual→spec documents Cost; Optionality→proposal prices Cost;
   Emotional→pitch makes Cost visceral per audience.

3. Scout inventory — glob simulations/scout/ now. Unconditional.

4. SCOUT TRACEABILITY TABLE — source of truth for TRACEABILITY AUDIT row identifiers.
   Each Req-ID pre-declared here becomes a named row in REFLECTION. A missing REFLECTION
   row is a Req-ID absence — R-02 absent is visible at a glance, not by count comparison.

   | Req-ID       | Must-have (brief)    | Originating Scout-Requirements Friction      | Scout File (path or "none") |
   |--------------|----------------------|----------------------------------------------|-----------------------------|
   | (fill in A1) | (fill in A1)         |                                              |                             |
   (one row per friction; if none found: one row, Friction from INERTIA MODEL Cost, file = "none")

5. INERTIA MODEL MAP — source of truth for CONVICTION DELTA row identifiers. Each Conv-ID
   pre-declared here becomes a named row in REFLECTION. A missing CONVICTION DELTA row is a
   CT-[X] absence — CT-Spec absent means Factual conviction type is untracked.

   | Conv-ID  | Artifact | Conviction type | Amplification chain starter                                    |
   |----------|----------|-----------------|----------------------------------------------------------------|
   | RULE     | The CONVICTION DELTA in REFLECTION must contain exactly 3 rows (CT-Spec, CT-Prop, CT-Pitch). A missing row is a named-conviction-type absence. Do not introduce anonymous version rows. | — | — |
   | CT-Spec  | Spec     | Factual         | (fill in: opening factual move for spec's conviction chain)    |
   | CT-Prop  | Proposal | Optionality     | (fill in: opening optionality move for proposal's chain)       |
   | CT-Pitch | Pitch    | Emotional       | (fill in: opening emotional move for pitch's conviction chain) |

6. Artifact contract matrix:

| Field           | Spec                                                             | Proposal                                                                    | Pitch                                                                              |
|-----------------|------------------------------------------------------------------|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| READ            | Topic identity; INERTIA MODEL (all fields); scout-requirements if found | Spec file; INERTIA MODEL Cost; scout-feasibility if found          | Proposal file; INERTIA MODEL Cost; scout-positioning if found                      |
| WRITE           | simulations/draft/specs/{topic}-spec-{date}.md                   | simulations/draft/proposals/{topic}-proposal-{date}.md                      | simulations/draft/pitches/{topic}-pitch-{date}.md                                  |
| PRESERVE        | (first artifact)                                                 | All spec design decisions — no re-opening                                   | Recommended option — crystallize, do not reconsider                                |
| CARRIES FORWARD | Feature identity; INERTIA MODEL; design decisions                | Recommended option + rationale; INERTIA MODEL Cost                          | (final artifact)                                                                   |
| CONVICTION TYPE | Factual — INERTIA MODEL Cost as factual record                   | Optionality — Cost priced against each alternative                          | Emotional — Cost visceral per audience                                             |

Print the matrix. Do not begin Artifact 1 until printed.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 1: SPEC — Factual Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: topic identity; INERTIA MODEL; scout-requirements if found.
                    PRESERVE: (first artifact). CONVICTION TYPE: Factual.

  PURPOSE        — INERTIA MODEL Name + Behavior; Cost as factual record.
  REQUIREMENTS   — Bulleted, MoSCoW (M/S/C/W). Each Must-have: complete Req-ID + SETUP
                   SCOUT TRACEABILITY TABLE row simultaneously. Every Must-have = one row.
  DESIGN         — Components, data flow, decisions.
  CONSTRAINTS    — Technical, team, timeline, dependencies.
  OPEN QUESTIONS — Unknowns; namespace per item.

GATE: Write simulations/draft/specs/{topic}-spec-{date}.md before Artifact 2.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 2: PROPOSAL — Optionality Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: spec; INERTIA MODEL Cost; scout-feasibility if found.
                    PRESERVE: all spec decisions. CONVICTION TYPE: Optionality.

Option A = do-nothing at full INERTIA MODEL Cost. State Cost before alternatives.
Three options min. Per option: Name / Description / Pros / Cons / Risk / Effort.
Recommendation: option + three reasons citing spec decisions.

GATE: Write simulations/draft/proposals/{topic}-proposal-{date}.md before Artifact 3.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 3: PITCH — Emotional Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: proposal; INERTIA MODEL Cost; scout-positioning if found.
                    PRESERVE: recommended option. CONVICTION TYPE: Emotional.

Each version opens with INERTIA MODEL Cost as hook. Three versions in full:

EXEC — Cost in business terms; Cost elimination; compounding risk; CTA: approve/fund/unblock.
DEV  — Blocked capability; spec design referenced; technical debt; CTA: join beta/review spec.
MAKER — Daily friction; plain language only; time saved; CTA: try it/sign up/start now.
ANTI-POSITIONING: what this feature is NOT, two sentences.

GATE: Write simulations/draft/pitches/{topic}-pitch-{date}.md before Campaign Reflection.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN REFLECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

After pitch file exists on disk only. Retrospective — completed artifacts only.

FINDINGS:

  TRACEABILITY AUDIT
    One row per SETUP SCOUT TRACEABILITY TABLE row. Copy Req-ID and Friction from SETUP
    now; complete remaining columns after Artifact 1. Row count must match SETUP.

    | Req-ID | Scout-Requirements Friction | Must-have found in spec? | Must-have text (exact phrase) | Gap (if N) | Scout namespace |
    |--------|-----------------------------|--------------------------|-------------------------------|------------|-----------------|
    | RULE   | N in col 3 + blank col 5 = STRUCTURAL FAIL — not an acceptable omission  | — | — | — | — |
    | R-01   | (copy from SETUP row 1)     | Y / N                    |                               |            |                 |
    | R-02   | (copy from SETUP row 2)     | Y / N                    |                               |            |                 |
    (match SETUP row count exactly — do not reduce)

    Must-have found: Y = distinct Must-have in Artifact 1 REQUIREMENTS covers friction.
    Must-have text: verbatim from Artifact 1. Blank if N.
    Gap: if N, state absent requirement. N + blank = STRUCTURAL FAIL per RULE row.
    Scout namespace: specific sub-skill for N rows. Blank if Y.

  CONVICTION DELTA
    Three rows only — CT-Spec, CT-Prop, CT-Pitch from INERTIA MODEL MAP. No anonymous
    version rows. Each row's Amplification chain anchors to the MAP starter for that
    Conv-ID. Replace all bracketed tokens. An unfilled bracket fails the row.

    | Conv-ID / Conviction type | Conviction established (one-sentence claim) | Grounding Req-ID(s) | Amplification chain |
    |---------------------------|---------------------------------------------|---------------------|-----------------------------------------------------|
    | RULE | Each Conv-ID must match an INERTIA MODEL MAP entry. Missing row = named-conviction-type absent. Do not add rows. | — | — |
    | CT-Spec — Factual         |                                             |                     | (MAP starter: [CT-Spec starter]) → [Req-ID's factual claim from Must-have] → [how spec locked claim as record] |
    | CT-Prop — Optionality     |                                             |                     | (MAP starter: [CT-Prop starter]) → [Option A = INERTIA MODEL Cost] → [how recommendation prices against baseline] |
    | CT-Pitch — Emotional      |                                             |                     | (MAP starter: [CT-Pitch starter]) → [Req-ID's claim made visceral] → [audience register that carried it] |

    No grounding: "GAP — [Req-ID] nearest; does not ground CT-[X] because [reason]."

  NEAR-DUPLICATE CONTENT — passage copied; what changed to make it conviction-bearing.
  RESIDUAL QUESTIONS — scout signal needed; namespace per item.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN CLOSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Artifact | Path                                                         | Scout signal consumed | Conviction type met | Open questions |
|----------|--------------------------------------------------------------|-----------------------|---------------------|----------------|
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md               | (namespace or none)   | Y / partial / N     | (list)         |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md       | (namespace or none)   | Y / partial / N     | (list)         |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md            | (namespace or none)   | Y / partial / N     | (list)         |

CONVICTION GAP DIAGNOSIS — complete partial or N rows. Blank row when partial or N = fail.
All Y: "No conviction gaps detected."

  | Artifact | Sub-section where gap originates | Register found | Register declared | Scout sub-skill | Evidence needed |
  |----------|----------------------------------|----------------|-------------------|-----------------|-----------------|
  | Spec     |                                  |                |                   |                 |                 |
  | Proposal |                                  |                |                   |                 |                 |
  | Pitch    |                                  |                |                   |                 |                 |

  Register found / Register declared: one word each, distinct columns.
  Scout sub-skill: specific identifier (e.g., scout-requirements), not namespace alone.
  Evidence needed: one sentence.

Open questions: namespace for each.
```

---

## V-05 — Minimum-Density C-40+C-41

**Axis:** Lifecycle compression — all four structural tables (INERTIA MODEL MAP, SCOUT
TRACEABILITY TABLE, TRACEABILITY AUDIT, CONVICTION DELTA, CONVICTION GAP DIAGNOSIS)
are present at minimum prose density. Explanatory blocks around each table are stripped
to the shortest form that still identifies the table's role and cell-fill instructions.
The structural tables carry the requirement; prose carries only what tables cannot.

**Hypothesis:** C-38, C-39, C-40, and C-41 are column-count, row-naming, and match-
directive properties. Adjacent prose volume is not scored. If V-05 earns all four at
FULL, prose context is not load-bearing at the 243-ceiling level. If any criterion
fails, the failing table's minimum prose is insufficient and at least one explanatory
element is structurally necessary. Predicted score: 243.

```
You are running /campaign-blueprint for: {topic}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0. CAMPAIGN CONVICTION HYPOTHESIS:
   Hypothesis: "The {topic} campaign must establish that [friction from INERTIA MODEL Cost]
   is the dominant reason [audience] cannot [desired outcome], so displacing [INERTIA MODEL
   Name] becomes the obvious move."
   Falsification: (a) spec cannot document barrier as measured cost; (b) proposal cannot
   price barrier against alternative; (c) pitch cannot make barrier visceral per version.
   Complete before item 1.

1. Topic identity — feature name, audience, problem solved. One sentence.

2. INERTIA MODEL:
     Name:     current behavior shorthand
     Behavior: what users do today — one sentence
     Cost:     what that costs — one sentence (factual, priceable, emotional)
   Conviction map: Factual→spec; Optionality→proposal; Emotional→pitch.

3. Scout inventory — glob simulations/scout/ for this topic. Unconditional.

4. SCOUT TRACEABILITY TABLE — fill Friction + Scout File from scout-requirements;
   fill Req-ID + Must-have during Artifact 1:

   | Req-ID       | Must-have (brief)    | Originating Scout-Requirements Friction      | Scout File (path or "none") |
   |--------------|----------------------|----------------------------------------------|-----------------------------|
   | (fill in A1) | (fill in A1)         |                                              |                             |
   (one row per friction; if none: one row, Friction from INERTIA MODEL Cost, file = "none")

5. INERTIA MODEL MAP — fill all cells before Artifact 1. CONVICTION DELTA row count must
   match this table. CT-[X] absent in REFLECTION = named-conviction-type absent.

   | Conv-ID  | Artifact | Conviction type | Amplification chain starter     |
   |----------|----------|-----------------|---------------------------------|
   | CT-Spec  | Spec     | Factual         | (fill in)                       |
   | CT-Prop  | Proposal | Optionality     | (fill in)                       |
   | CT-Pitch | Pitch    | Emotional       | (fill in)                       |

6. Artifact contract matrix:

| Field           | Spec                                                             | Proposal                                                                    | Pitch                                                                              |
|-----------------|------------------------------------------------------------------|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| READ            | Topic identity; INERTIA MODEL; scout-requirements if found       | Spec; INERTIA MODEL Cost; scout-feasibility if found                        | Proposal; INERTIA MODEL Cost; scout-positioning if found                           |
| WRITE           | simulations/draft/specs/{topic}-spec-{date}.md                   | simulations/draft/proposals/{topic}-proposal-{date}.md                      | simulations/draft/pitches/{topic}-pitch-{date}.md                                  |
| PRESERVE        | (first)                                                          | All spec decisions — no re-opening                                          | Recommended option — crystallize, no reconsideration                               |
| CARRIES FORWARD | Feature identity; INERTIA MODEL; decisions                       | Recommended option + rationale; INERTIA MODEL Cost                          | (final)                                                                            |
| CONVICTION TYPE | Factual                                                          | Optionality                                                                 | Emotional                                                                          |

Print matrix. Do not begin Artifact 1 until printed.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 1: SPEC — Factual Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
READ: topic identity; INERTIA MODEL; scout-requirements if found. CONVICTION TYPE: Factual.

  PURPOSE        — INERTIA MODEL Name + Behavior; Cost as factual record.
  REQUIREMENTS   — Bulleted, MoSCoW (M/S/C/W). Each Must-have: fill Req-ID + SETUP row.
  DESIGN         — Components, data flow, decisions.
  CONSTRAINTS    — Technical, team, timeline, dependencies.
  OPEN QUESTIONS — Unknowns; namespace per item.

GATE: Write simulations/draft/specs/{topic}-spec-{date}.md before Artifact 2.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 2: PROPOSAL — Optionality Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
READ: spec; INERTIA MODEL Cost; scout-feasibility if found. CONVICTION TYPE: Optionality.
Option A = do-nothing at full INERTIA MODEL Cost. State Cost before alternatives.
Three options min. Per option: Name / Description / Pros / Cons / Risk / Effort.
Recommendation: option + three reasons citing spec decisions.

GATE: Write simulations/draft/proposals/{topic}-proposal-{date}.md before Artifact 3.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 3: PITCH — Emotional Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
READ: proposal; INERTIA MODEL Cost; scout-positioning if found. CONVICTION TYPE: Emotional.
Each version opens with INERTIA MODEL Cost as hook.

EXEC — Cost in business terms; Cost elimination; compounding risk; CTA: approve/fund/unblock.
DEV  — Blocked capability; spec design referenced explicitly; technical debt; CTA: join beta.
MAKER — Plain language only; daily friction; time saved; CTA: try it / sign up / start now.
ANTI-POSITIONING: what this is NOT, two sentences.

GATE: Write simulations/draft/pitches/{topic}-pitch-{date}.md before Campaign Reflection.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN REFLECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

After pitch file exists on disk only. Retrospective.

FINDINGS:

  TRACEABILITY AUDIT
    One row per SETUP SCOUT TRACEABILITY TABLE row. Copy Req-ID + Friction before
    Artifact 1; complete remaining columns after. N + blank Gap = structural fail.
    Row count must match SETUP; missing row = named Req-ID absent.

    | Req-ID | Scout-Requirements Friction | Must-have found in spec? | Must-have text (exact phrase) | Gap (if N) | Scout namespace |
    |--------|-----------------------------|--------------------------|-------------------------------|------------|-----------------|
    | R-01   | (from SETUP)                | Y / N                    |                               |            |                 |
    | R-02   | (from SETUP)                | Y / N                    |                               |            |                 |
    (match SETUP row count)

  CONVICTION DELTA
    Three rows — CT-Spec, CT-Prop, CT-Pitch from INERTIA MODEL MAP. No other rows.
    Row count must match MAP. Unfilled bracket = row fail.

    | Conv-ID / Conviction type | Conviction established | Grounding Req-ID(s) | Amplification chain |
    |---------------------------|------------------------|---------------------|-----------------------------------------------------|
    | CT-Spec — Factual         |                        |                     | (MAP starter: [CT-Spec]) → [Req-ID's factual claim] → [how spec locked it] |
    | CT-Prop — Optionality     |                        |                     | (MAP starter: [CT-Prop]) → [Option A = INERTIA MODEL Cost] → [how recommendation prices] |
    | CT-Pitch — Emotional      |                        |                     | (MAP starter: [CT-Pitch]) → [Req-ID's claim made visceral] → [audience register] |

    No grounding: "GAP — [Req-ID] nearest; does not ground CT-[X] because [reason]."

  NEAR-DUPLICATE CONTENT — passage copied; what changed to make conviction-bearing.
  RESIDUAL QUESTIONS — scout signal needed; namespace per item.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN CLOSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Artifact | Path                                                         | Scout signal consumed | Conviction type met | Open questions |
|----------|--------------------------------------------------------------|-----------------------|---------------------|----------------|
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md               | (namespace or none)   | Y / partial / N     | (list)         |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md       | (namespace or none)   | Y / partial / N     | (list)         |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md            | (namespace or none)   | Y / partial / N     | (list)         |

CONVICTION GAP DIAGNOSIS — complete partial or N rows. Blank row when partial or N = fail.
All Y: "No conviction gaps detected."

  | Artifact | Sub-section where gap originates | Register found | Register declared | Scout sub-skill | Evidence needed |
  |----------|----------------------------------|----------------|-------------------|-----------------|-----------------|
  | Spec     |                                  |                |                   |                 |                 |
  | Proposal |                                  |                |                   |                 |                 |
  | Pitch    |                                  |                |                   |                 |                 |

  Register found / Register declared: one word each, distinct columns.
  Scout sub-skill: specific identifier, not namespace alone. Evidence needed: one sentence.

Open questions: namespace for each.
```

---

## R15 Predicted Score Summary

| Variant | Axis | C-38 | C-39 | C-40 | C-41 | v15 |
|---------|------|------|------|------|------|-----|
| V-01 — INERTIA MODEL MAP SETUP Only | SETUP structure (MAP present, CONVICTION DELTA anonymous rows) | FULL | FULL | NO | NO | **233** |
| V-02 — Full C-40+C-41 Minimum Form | CONVICTION DELTA row pre-naming (CT-Spec/CT-Prop/CT-Pitch from MAP) | FULL | FULL | FULL | FULL | **243** |
| V-03 — Conversational Register | Phrasing register (2nd person imperative, V-02 tables unchanged) | FULL | FULL | FULL | FULL | **243** |
| V-04 — Maximum-Density C-40+C-41 | All four structural axes at tightest form (in-table RULE rows for both MAP and TRACEABILITY AUDIT) | FULL | FULL | FULL | FULL | **243** |
| V-05 — Minimum-Density C-40+C-41 | Lifecycle compression (minimum prose, tables carry all structural requirements) | FULL | FULL | FULL | FULL | **243** |

**D15 inspection verification for V-01 (control case):**
- D15 step 1: INERTIA MODEL MAP present in SETUP (4-column, CT-Spec/CT-Prop/CT-Pitch
  pre-declared) → PASSES. Step 1 confirms the SETUP-level structural precondition.
- D15 step 2: CONVICTION DELTA rows are "Exec", "Dev", "Maker" — pitch audience version
  names with no traceability to any MAP Conv-ID entry → FAILS. C-40 NO CREDIT.
- C-41 chain test step 5 fails at D15 step 2 before full evaluation. C-41 NO CREDIT.

**D15 inspection verification for V-02 through V-05 (ceiling candidates):**
- D15 step 1: INERTIA MODEL MAP present in SETUP → PASSES.
- D15 step 2: CONVICTION DELTA rows labeled CT-Spec—Factual, CT-Prop—Optionality,
  CT-Pitch—Emotional — each traceable to a named MAP Conv-ID entry → PASSES.
  Explicit row-count match directive confirms C-40 FULL.
- C-41 chain test: (1) C-34 FULL — 4-column CONVICTION DELTA with in-cell Amplification
  chain template; (2) C-35 FULL — 6-column CONVICTION GAP DIAGNOSIS with three pre-
  declared artifact rows; (3) C-36 FULL — 6-column TRACEABILITY AUDIT with correct
  column names; (4) C-38 FULL — named Req-ID rows with SETUP match directive; (5) C-40
  FULL — INERTIA MODEL MAP with pre-named CONVICTION DELTA rows and match directive.
  All five steps pass → C-41 FULL.

**Open question for R15 scoring:** V-05 tests minimum-density against three structural
axes simultaneously (C-38, C-40, match directives). If V-05 earns all FULL, prose
context is not load-bearing at any of the four new criteria. If V-05 fails C-40 but
passes C-38, the MAP match directive requires more explicit framing than the minimum
provided. If V-05 fails both, the REFLECTION tables require adjacent prose to pass
at the 243-ceiling level. V-01 serves as the single diagnostic control confirming that
the MAP's presence alone (without pre-named CONVICTION DELTA rows) does not advance
the score beyond 233 — the D15 two-step inspection behaves as specified.

**The structural upgrade chain completed by R15:**
C-31 → C-34 → C-40: CONVICTION DELTA phase advances from prose Req-ID citation
(epistemic) to anonymous version rows (ontological at cell level) to MAP-linked named
rows (ontological at entry level). Parallel upgrade chain: C-29 → C-36 → C-38 for
TRACEABILITY AUDIT. C-41 closes the chain by requiring both SETUP-anchored tables to
reach maximum structural resolution simultaneously: no phase may rely on anonymous
template rows when a SETUP MAP source is available.
