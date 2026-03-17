---
skill: quest-variate
skill_target: campaign-blueprint
date: 2026-03-17
round: 13
rubric: campaign-blueprint-rubric-v13-2026-03-17.md
---

# campaign-blueprint — Prompt Variations R13

Five complete, runnable skill body variations. Single-axis first (V-01 through V-03),
then two combinations (V-04 through V-05).

## R13 Context

R12 variants under v13 retroactive scoring:

| Variant | v12 | C-36 | C-37 | v13 |
|---------|-----|------|------|-----|
| V-01 — C-34 In-Cell Template | 208 | 0 | 0 | **208** |
| V-02 — C-35 Artifact-Row Pre-Declaration | 208 | 0 | 0 | **208** |
| V-03 — Structural Traceability Audit (C-36) | 203 | +5 | 0 | **208** |
| V-04 — C-34 + C-35 Full Combination | 213 | 0 | 0 | **213** |
| V-05 — Minimum-Density 213 | 213 | 0 | 0 | **213** |

No R12 variant reaches 223. V-04 (C-34 + C-35, 213) is the highest base. V-03
(C-36, 208) is the only R12 variant with a structural TRACEABILITY AUDIT table.
The 223 ceiling requires C-34 + C-35 + C-36 simultaneously — a cross-round
combination taking V-04's two-table base and adding V-03's structural TRACEABILITY AUDIT.

C-37 is a chain criterion: all three tables must be present simultaneously.
- CONVICTION DELTA: 4-column table with in-cell Amplification chain template (C-34)
- CONVICTION GAP DIAGNOSIS: 6-column table with Register found/declared as distinct columns (C-35)
- TRACEABILITY AUDIT: 6-column structural table with pre-declared rows (C-36)

**R13 design question:**

The three structural tables apply to three distinct lifecycle phases:
1. REFLECTION TRACEABILITY AUDIT (C-36): SETUP→REQUIREMENTS traceability closed retrospectively
2. REFLECTION CONVICTION DELTA (C-34): pitch conviction grounded against Req-IDs
3. CLOSE CONVICTION GAP DIAGNOSIS (C-35): register mismatch diagnosed per artifact row

All three are in CAMPAIGN REFLECTION or CAMPAIGN CLOSE — two adjacent sections.
R13 explores three implementation questions for C-36:

1. **Minimum C-36 addition (V-01):** V-04 R12 has C-34+C-35. Add V-03 R12's structural
   TRACEABILITY AUDIT table to V-04 R12 unchanged. Does the mechanical union of two
   R12 variants complete the C-37 chain, or does cross-variant combination expose a gap?

2. **Pre-named row linkage (V-02):** C-36 requires rows "pre-declared as named entries
   matching the scout-requirements friction sources pre-populated in the SCOUT TRACEABILITY
   TABLE in CAMPAIGN SETUP (C-27)." V-03 R12 used a template placeholder row. V-02
   tightens the linkage: the TRACEABILITY AUDIT table instructions explicitly direct
   pre-population of row identifiers from the SETUP table, making the row-level match
   between SETUP and REFLECTION tables an explicit structural requirement rather than an
   implied consequence of "one row per SETUP table row."

3. **Structural failure signal (V-03):** C-36 requires that a row with N in Must-have
   found and a blank Gap cell is "visibly structurally incomplete — the blank is not a
   passing omission but a cell-level gap that cannot be hidden in prose." V-03 makes this
   structural rule explicit inside the table as a sentinel note beneath the column headers,
   converting the rubric's ontological description into an active prompt-level instruction.

**Predicted scoring pattern:**

| Variant | Axis | Hypothesis | Expected v13 |
|---------|------|------------|--------------|
| V-01 — Mechanical C-34+C-35+C-36 Union | Output format | V-04 R12 base + V-03 R12 TRACEABILITY AUDIT table = C-37 complete | **223** |
| V-02 — Pre-Named SETUP-Linked Rows | Lifecycle emphasis | Explicit SETUP→REFLECTION row-ID linkage passes C-36 more reliably | **223** |
| V-03 — In-Table Structural Failure Signal | Output format | Sentinel note beneath headers converts C-36's ontological guarantee into explicit prompt rule | **223** |
| V-04 — Maximum-Density Three-Table Chain | All three structural axes | Tightest C-34 + tightest C-35 + tightest C-36 simultaneously | **223** |
| V-05 — Minimum-Density 223 | Lifecycle compression | Minimum prose preserving all three structural table requirements | **223** |

All five variants target 223. The single-axis variants (V-01 through V-03) each add C-36
to the confirmed V-04 R12 213 base, varying the form of C-36 implementation. V-04 and V-05
combine all structural refinements at maximum and minimum density respectively.

---

## V-01 — Mechanical C-34+C-35+C-36 Union

**Axis:** Output format — TRACEABILITY AUDIT in REFLECTION replaced with structural
6-column table from V-03 R12, grafted directly onto V-04 R12's body (which already
carries C-34 CONVICTION DELTA table and C-35 CONVICTION GAP DIAGNOSIS table).

**Hypothesis:** V-04 R12 earns C-34 FULL and C-35 FULL. V-03 R12 earns C-36 FULL.
Both exist in the same rubric round at the same base score tier. V-01 combines them
mechanically: V-04 R12 body, with only the TRACEABILITY AUDIT section replaced by
V-03 R12's structural 6-column table form. If C-37 is a chain criterion that requires
all three tables simultaneously, mechanical union of two passing R12 variants should
complete the chain. Predicted score: 223.

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
    Must-have text (exact phrase): the verbatim text of the Must-have from Artifact 1
    REQUIREMENTS. Leave blank if Must-have found = N.
    Gap: if Must-have found = N, state explicitly what requirement is absent and why this
    friction is unaddressed. A N row with a blank Gap cell is a structural incompleteness
    in this audit — the table form makes the absence visible without prose scanning.
    Scout namespace: for each N row, name the scout sub-skill that could surface the missing
    requirement (e.g., scout-requirements, scout-market, scout-stakeholders). Leave blank
    if Must-have found = Y.

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

## V-02 — C-36 Pre-Named SETUP-Linked Rows

**Axis:** Lifecycle emphasis — TRACEABILITY AUDIT rows are pre-declared with explicit
SETUP identifier linkage. The audit table instructions direct population of row identifiers
from the SETUP SCOUT TRACEABILITY TABLE by name, making the row-level match an explicit
structural requirement rather than an implied consequence of "one row per SETUP row."

**Hypothesis:** C-36 requires that each audit row "pre-declared as a named entry, matching
the scout-requirements friction sources pre-populated in the SCOUT TRACEABILITY TABLE in
CAMPAIGN SETUP." V-03 R12 satisfied this with a template placeholder row and instruction
to produce "one audit row per SETUP table row." V-02 tightens this: the audit table
instructions explicitly direct: "Copy each Req-ID and Friction from the SETUP SCOUT
TRACEABILITY TABLE into a row in this table now. The row count in this table must match
the row count in SETUP." This makes the structural linkage between SETUP and REFLECTION
tables an explicit, verifiable constraint — a REFLECTION table with fewer rows than the
SETUP table is a visible structural incompleteness at a glance. Base: V-04 R12.
Predicted score: 223.

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
    CAMPAIGN SETUP into a named row in the audit table below — one row per SETUP table row.
    The row count in this table must match the row count in the SETUP table; a missing row
    is a visible structural incompleteness at a glance, not a prose-level omission.
    Pre-populate Req-ID and Friction before Artifact 1; complete remaining columns after.

    | Req-ID | Scout-Requirements Friction | Must-have found in spec? | Must-have text (exact phrase) | Gap (if N) | Scout namespace |
    |--------|-----------------------------|--------------------------|-------------------------------|------------|-----------------|
    | R-01   | (from SETUP row 1)          | Y / N                    |                               |            |                 |
    | R-02   | (from SETUP row 2)          | Y / N                    |                               |            |                 |
    (add rows to match SETUP table exactly — do not reduce row count)

    Must-have found in spec?: Y if a distinct bulleted Must-have in Artifact 1 REQUIREMENTS
    directly addresses this friction; N otherwise.
    Must-have text (exact phrase): verbatim text of the Must-have. Blank if Must-have found = N.
    Gap: if N, state the absent requirement explicitly. A N row with a blank Gap cell is a
    structural incompleteness — the blank cannot be a passing omission.
    Scout namespace: specific scout sub-skill for each N row. Blank if Must-have found = Y.

  CONVICTION DELTA
    Complete every cell in the amplification table. The Amplification chain column carries
    the fill-in template pre-placed in each data cell. Replace all bracketed tokens with
    campaign-specific values. Any unfilled bracket fails the row.

    | Version | Conviction established (visceral claim) | Grounding Req-ID(s) | Amplification chain |
    |---------|-----------------------------------------|---------------------|-----------------------------------------------------|
    | Exec    |                                         |                     | [Req-ID]'s [specific factual claim from Must-have] is made visceral in this version by [emotional register] |
    | Dev     |                                         |                     | [Req-ID]'s [specific factual claim from Must-have] is made visceral in this version by [emotional register] |
    | Maker   |                                         |                     | [Req-ID]'s [specific factual claim from Must-have] is made visceral in this version by [emotional register] |

    If no Must-have fully grounds a version: replace Amplification chain with
    "GAP — [Req-ID] is closest anchor but does not ground this claim because [reason]."

  NEAR-DUPLICATE CONTENT
    Name any passage nearly copied from the spec or proposal.
    State what you changed to make it conviction-bearing.

  RESIDUAL QUESTIONS
    Scout signal that would resolve what no artifact answered. Namespace for each.

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
  Complete each artifact's row if marked partial or N above. One row pre-declared per
  artifact. A row left blank when CLOSE shows partial or N is a structural incompleteness.
  If all three CLOSE rows are Y, write "No conviction gaps detected." after the table.

  | Artifact | Sub-section where gap originates | Register found | Register declared | Scout sub-skill | Evidence needed |
  |----------|----------------------------------|----------------|-------------------|-----------------|-----------------|
  | Spec     |                                  |                |                   |                 |                 |
  | Proposal |                                  |                |                   |                 |                 |
  | Pitch    |                                  |                |                   |                 |                 |

  Sub-section: specific named sub-section — not the artifact name alone.
  Register found: one word (Factual, Optionality, or Emotional). Register declared: one
  word. Distinct columns — a combined description does not satisfy both.
  Scout sub-skill: specific sub-skill identifier, not namespace alone.
  Evidence needed: one sentence per row.

List any open question a future signal could resolve, with recommended namespace for each.
```

---

## V-03 — C-36 In-Table Structural Failure Signal

**Axis:** Output format — the TRACEABILITY AUDIT table carries an explicit structural
failure sentinel embedded below the column headers. The sentinel converts the rubric's
ontological guarantee ("a N row with blank Gap is visibly incomplete") into an active
prompt-level instruction that the model reads before filling any cell.

**Hypothesis:** C-36's defining structural property is that "a row with N in Must-have
found and a blank Gap cell is visibly structurally incomplete — the blank is not a passing
omission but a cell-level gap that cannot be hidden in prose." V-03 R12 expressed this
as a post-table instruction. V-03 (R13) moves this rule inside the table structure itself:
a sentinel row immediately below the header, before any data rows, reads:
"[RULE: Any row with N in Must-have found? and a blank Gap cell is a STRUCTURAL FAIL —
this is an incomplete audit row, not an acceptable omission]." The sentinel converts
structural enforcement from a post-hoc reminder into a pre-cell constraint that the model
encounters before writing any row. The structural failure is surfaced at the moment the
model begins filling the table, not after. Base: V-04 R12 + V-03 R12 TRACEABILITY AUDIT.
Predicted score: 223.

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

This phase begins only after the pitch file exists on disk. Retrospective assessment only.

FINDINGS:

  TRACEABILITY AUDIT
    Pre-populate the Req-ID and Friction columns from the SCOUT TRACEABILITY TABLE in
    CAMPAIGN SETUP now — one row per SETUP row. Complete remaining columns after Artifact 1.

    | Req-ID | Scout-Requirements Friction | Must-have found in spec? | Must-have text (exact phrase) | Gap (if N) | Scout namespace |
    |--------|-----------------------------|--------------------------|-------------------------------|------------|-----------------|
    | RULE   | A row with N in col 3 and a blank col 5 is a STRUCTURAL FAIL — not an acceptable omission | — | — | — | — |
    |        |                             | Y / N                    |                               |            |                 |

    Req-ID: canonical identifier from SETUP (e.g., R-01). Must match Artifact 1 verbatim.
    Scout-Requirements Friction: copied from SETUP. Pre-fill before Artifact 1.
    Must-have found in spec?: Y if a distinct Must-have in Artifact 1 REQUIREMENTS addresses
    this friction; N otherwise.
    Must-have text (exact phrase): verbatim Must-have text. Blank if col 3 = N.
    Gap: if col 3 = N, state the absent requirement explicitly. Blank + N = STRUCTURAL FAIL.
    Scout namespace: specific scout sub-skill for N rows. Blank if col 3 = Y.

  CONVICTION DELTA
    Complete every cell. Amplification chain has fill-in template pre-placed in each row.
    Replace all bracketed tokens. An unfilled bracket fails the row.

    | Version | Conviction established (visceral claim) | Grounding Req-ID(s) | Amplification chain |
    |---------|-----------------------------------------|---------------------|-----------------------------------------------------|
    | Exec    |                                         |                     | [Req-ID]'s [specific factual claim from Must-have] is made visceral in this version by [emotional register] |
    | Dev     |                                         |                     | [Req-ID]'s [specific factual claim from Must-have] is made visceral in this version by [emotional register] |
    | Maker   |                                         |                     | [Req-ID]'s [specific factual claim from Must-have] is made visceral in this version by [emotional register] |

    If no Must-have grounds a version: "GAP — [Req-ID] is closest anchor but does not
    ground this claim because [reason]."

  NEAR-DUPLICATE CONTENT
    Passage nearly copied; what changed to make it conviction-bearing.

  RESIDUAL QUESTIONS
    Scout signal that would resolve what no artifact answered. Namespace for each.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN CLOSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Mark Y / partial / N for "Conviction type met":

| Artifact | Path                                                         | Scout signal consumed | Conviction type met | Open questions |
|----------|--------------------------------------------------------------|-----------------------|---------------------|----------------|
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md               | (namespace or none)   | Y / partial / N     | (list)         |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md       | (namespace or none)   | Y / partial / N     | (list)         |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md            | (namespace or none)   | Y / partial / N     | (list)         |

CONVICTION GAP DIAGNOSIS
  Complete each row if marked partial or N. Blank row when CLOSE shows partial or N =
  structural incompleteness. All Y: write "No conviction gaps detected."

  | Artifact | Sub-section where gap originates | Register found | Register declared | Scout sub-skill | Evidence needed |
  |----------|----------------------------------|----------------|-------------------|-----------------|-----------------|
  | Spec     |                                  |                |                   |                 |                 |
  | Proposal |                                  |                |                   |                 |                 |
  | Pitch    |                                  |                |                   |                 |                 |

  Register found / Register declared: one word each; distinct columns.
  Scout sub-skill: specific identifier, not namespace alone.
  Evidence needed: one sentence.

List any open question a future signal could resolve, with recommended namespace for each.
```

---

## V-04 — Maximum-Density Three-Table Chain

**Axis:** All three structural axes at maximum enforcement density.
- C-34: CONVICTION DELTA table with in-cell Amplification chain template pre-placed in
  each data cell (tightest form from V-01 R12)
- C-35: CONVICTION GAP DIAGNOSIS table with pre-declared artifact rows, explicit
  Register found/declared column distinction directive, and scout sub-skill specificity
  requirement (tightest form from V-02 R12)
- C-36: TRACEABILITY AUDIT table with pre-named SETUP-linked rows AND in-table structural
  failure sentinel (combining V-02 R13 pre-named rows with V-03 R13 sentinel)

**Hypothesis:** Each structural table has a tighter and a looser form that both pass the
criterion. Maximum-density combines the tightest form of each simultaneously:
- C-34 tightest: in-cell template in each data row (not instruction block below table)
- C-35 tightest: three pre-declared artifact rows + explicit register comparison directive
- C-36 tightest: SETUP-matched named rows + in-table structural failure sentinel
This is the maximum enforcement form: every structural constraint is embedded in the
table itself, not described in adjacent prose. Predicted score: 223.

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
begins, not during pitch production. Retrospective assessment of completed artifacts only.

FINDINGS:

  TRACEABILITY AUDIT
    Copy each Req-ID and Scout-Requirements Friction from the SCOUT TRACEABILITY TABLE in
    CAMPAIGN SETUP into this table now — one named row per SETUP row. Row count must match
    SETUP exactly; a missing row is a structural incompleteness visible at a glance.
    Pre-populate Req-ID and Friction before Artifact 1; complete remaining columns after.

    | Req-ID | Scout-Requirements Friction | Must-have found in spec? | Must-have text (exact phrase) | Gap (if N) | Scout namespace |
    |--------|-----------------------------|--------------------------|-------------------------------|------------|-----------------|
    | RULE   | N in col 3 + blank col 5 = STRUCTURAL FAIL — not an acceptable omission | — | — | — | — |
    | R-01   | (copy from SETUP row 1)     | Y / N                    |                               |            |                 |
    | R-02   | (copy from SETUP row 2)     | Y / N                    |                               |            |                 |
    (add rows to match SETUP table exactly)

    Must-have found in spec?: Y if a distinct bulleted Must-have in Artifact 1 REQUIREMENTS
    directly addresses this friction; N otherwise.
    Must-have text (exact phrase): verbatim Must-have text from Artifact 1. Blank if N.
    Gap: if N, state absent requirement explicitly. Blank + N = structural fail per RULE row.
    Scout namespace: specific scout sub-skill for N rows (e.g., scout-requirements,
    scout-market). Blank if Y.

  CONVICTION DELTA
    The Amplification chain column has the fill-in template pre-placed inside each data
    cell row. Replace all bracketed tokens with campaign-specific values before writing
    any narrative. A cell with an unfilled bracket fails the row.

    | Version | Conviction established (visceral claim) | Grounding Req-ID(s) | Amplification chain |
    |---------|-----------------------------------------|---------------------|-----------------------------------------------------|
    | Exec    |                                         |                     | [Req-ID]'s [specific factual claim from Must-have] is made visceral in this version by [emotional register] |
    | Dev     |                                         |                     | [Req-ID]'s [specific factual claim from Must-have] is made visceral in this version by [emotional register] |
    | Maker   |                                         |                     | [Req-ID]'s [specific factual claim from Must-have] is made visceral in this version by [emotional register] |

    Conviction established: single visceral claim this version makes that spec/proposal
    could not — one sentence. Grounding Req-ID(s): canonical Must-have identifier(s) from
    Artifact 1 REQUIREMENTS. Required per row — no ungrounded impressionistic claims.
    If no Must-have grounds a version: replace Amplification chain with
    "GAP — [Req-ID] is closest anchor but does not ground this claim because [reason]."

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
  For each partial or N row above: complete that artifact's pre-declared row in the
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

## V-05 — Minimum-Density 223

**Axis:** Lifecycle compression — all three structural tables present at minimum prose
density. Explanatory context around each table is stripped to the minimum needed for
the model to fill it correctly. The structural tables carry the requirement; the prose
carries only what the table cannot encode itself.

**Hypothesis:** Structural enforcement is an ontological property of table structure,
not of adjacent prose volume. If C-34, C-35, and C-36 each pass based on column count,
column names, and cell-level pre-declarations, then the prose explanations surrounding
the tables are scoring noise. V-05 strips each table's prose context to minimum:
- TRACEABILITY AUDIT: table + column labels only; no post-table instruction block
- CONVICTION DELTA: table + brief "replace tokens" instruction; no per-column definitions
- CONVICTION GAP DIAGNOSIS: table + pre-declared rows + one-line column summary
SETUP, ARTIFACTS, and GATES are also compressed. Tests whether minimum-density passes
all three structural criteria or whether adjacent prose is load-bearing for any criterion.
Predicted score: 223.

```
You are running /campaign-blueprint for: {topic}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0. CAMPAIGN CONVICTION HYPOTHESIS:
   Hypothesis: "The {topic} campaign must establish that [friction from INERTIA MODEL Cost]
   is the dominant reason [audience] cannot [desired outcome], so that displacing
   [INERTIA MODEL Name] becomes the obvious move."
   Falsification: (a) spec cannot document barrier as measured cost; (b) proposal cannot
   price barrier against an alternative; (c) pitch cannot make barrier visceral per version.
   Write item 0 completely before item 1.

1. Topic identity — one sentence: feature name, audience, problem solved.

2. INERTIA MODEL:
     Name:     current behavior in shorthand
     Behavior: what users do today — one sentence
     Cost:     what that costs — one sentence (factual, priceable, emotional)
   Conviction map: Factual→spec documents Cost; Optionality→proposal prices Cost;
   Emotional→pitch makes Cost visceral per audience.

3. Scout inventory — glob simulations/scout/ for this topic now. Unconditional.

4. SCOUT TRACEABILITY TABLE — fill Friction and Scout File from scout-requirements;
   complete Req-ID and Must-have during Artifact 1:

   | Req-ID       | Must-have (brief)    | Originating Scout-Requirements Friction      | Scout File (path or "none") |
   |--------------|----------------------|----------------------------------------------|-----------------------------|
   | (fill in A1) | (fill in A1)         |                                              |                             |
   (one row per friction; if none found: one row, Friction from INERTIA MODEL Cost, file = "none")

5. Artifact contract matrix:

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
READ: topic identity; INERTIA MODEL; scout-requirements if found. CONVICTION TYPE: Factual.

  PURPOSE        — INERTIA MODEL Name + Behavior; Cost as factual record.
  REQUIREMENTS   — Bulleted, MoSCoW (M/S/C/W). Each Must-have: complete Req-ID + entry in
                   SCOUT TRACEABILITY TABLE above. Every Must-have = one SETUP table row.
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

EXEC — urgency through compounding Cost:
  Hook: Cost in business terms. What it does: Cost elimination. Why: compounding risk.
  CTA: approve / fund / unblock.

DEV — urgency through blocked capability:
  Hook: what INERTIA MODEL Behavior blocks. What it does: spec design referenced explicitly.
  Why: technical debt of sustained Behavior. CTA: join beta / review spec / contribute.

MAKER — plain language only:
  Hook: daily friction of INERTIA MODEL Behavior. What it does: what changes in daily work.
  Why: time saved from Behavior. CTA: try it / sign up / start now.

ANTI-POSITIONING: what this is NOT, two sentences.

GATE: Write simulations/draft/pitches/{topic}-pitch-{date}.md before Campaign Reflection.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN REFLECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

After pitch file exists on disk only. Retrospective.

FINDINGS:

  TRACEABILITY AUDIT
    One row per SETUP SCOUT TRACEABILITY TABLE row. Copy Req-ID and Friction before
    Artifact 1; complete Must-have found, text, Gap, Scout namespace after.
    N + blank Gap = structural incompleteness.

    | Req-ID | Scout-Requirements Friction | Must-have found in spec? | Must-have text (exact phrase) | Gap (if N) | Scout namespace |
    |--------|-----------------------------|--------------------------|-------------------------------|------------|-----------------|
    | R-01   | (from SETUP)                | Y / N                    |                               |            |                 |
    | R-02   | (from SETUP)                | Y / N                    |                               |            |                 |
    (match SETUP row count exactly)

  CONVICTION DELTA
    Replace all bracketed tokens with campaign values. Unfilled bracket = row fail.

    | Version | Conviction established (visceral claim) | Grounding Req-ID(s) | Amplification chain |
    |---------|-----------------------------------------|---------------------|-----------------------------------------------------|
    | Exec    |                                         |                     | [Req-ID]'s [specific factual claim from Must-have] is made visceral in this version by [emotional register] |
    | Dev     |                                         |                     | [Req-ID]'s [specific factual claim from Must-have] is made visceral in this version by [emotional register] |
    | Maker   |                                         |                     | [Req-ID]'s [specific factual claim from Must-have] is made visceral in this version by [emotional register] |

    No grounding: "GAP — [Req-ID] nearest; does not ground because [reason]."

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

## R13 Predicted Score Summary

| Variant | Axis | C-34 | C-35 | C-36 | C-37 | v13 |
|---------|------|------|------|------|------|-----|
| V-01 — Mechanical C-34+C-35+C-36 Union | Output format (TRACEABILITY AUDIT table added to V-04 R12 base) | FULL | FULL | FULL | FULL | **223** |
| V-02 — Pre-Named SETUP-Linked Rows | Lifecycle emphasis (explicit row-ID match between SETUP and REFLECTION) | FULL | FULL | FULL | FULL | **223** |
| V-03 — In-Table Structural Failure Signal | Output format (RULE sentinel row embedded in table) | FULL | FULL | FULL | FULL | **223** |
| V-04 — Maximum-Density Three-Table Chain | All three structural axes at tightest form | FULL | FULL | FULL | FULL | **223** |
| V-05 — Minimum-Density 223 | Lifecycle compression (minimum prose, tables carry requirement) | FULL | FULL | FULL | FULL | **223** |

**Design principle for R13:** All five variants are combination variants — the 223 ceiling
requires C-34 + C-35 + C-36 simultaneously, and no single-axis path can reach it from
the 213 base without adding C-36. "Single-axis" for R13 means adding exactly one axis
(C-36) to the confirmed V-04 R12 213 base. V-01 through V-03 vary the form of C-36
implementation while holding C-34 and C-35 constant at their V-04 R12 forms. V-04 applies
maximum density to all three simultaneously. V-05 applies minimum density.

**D13 column-count verification:**
- V-01: CONVICTION DELTA = 4 cols (C-34 PASS); GAP DIAGNOSIS = 6 cols (C-35 PASS);
  TRACEABILITY AUDIT = 6 cols with pre-declared rows (C-36 PASS) → C-37 PASS candidate
- V-02: Same column counts; TRACEABILITY AUDIT adds explicit SETUP row-ID match directive → C-36 PASS
- V-03: Same column counts; TRACEABILITY AUDIT adds RULE sentinel row → C-36 PASS
- V-04: Same column counts; all three tables at maximum structural density → C-37 PASS
- V-05: Same column counts; all three tables at minimum prose density → C-37 PASS candidate
  pending whether minimum-density prose is sufficient for scorer to confirm column names

**Open question for R13 scoring:** V-05 tests whether adjacent prose is load-bearing for
any of the three structural criteria, or whether column structure alone passes each.
If V-05 earns C-36 FULL, prose context is not load-bearing. If V-05 fails C-36, the
TRACEABILITY AUDIT table requires at least the post-table column definitions to pass.
