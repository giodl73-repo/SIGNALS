---
skill: quest-variate
skill_target: campaign-blueprint
date: 2026-03-17
round: 11
rubric: campaign-blueprint-rubric-v11-2026-03-16.md
---

# campaign-blueprint — Prompt Variations R11

Five complete, runnable skill body variations. Single-axis first (V-01 through V-03),
then two combinations (V-04 through V-05).

## R11 Context

R10 variants under v11 retroactive scoring:

| Variant | v10 | C-31 | C-32 | C-33 | v11 |
|---------|-----|------|------|------|-----|
| V-01 — CONVICTION DELTA: Req-ID Grounding | 188 | +5 | 0 | 0 | **193** |
| V-02 — CLOSE: Conviction Gap Remediation | 188 | 0 | +5 | 0 | **193** |
| V-03 — Inertia Prominence: Campaign Conviction Hypothesis | 188 | 0 | 0 | +5 | **193** |
| V-04 — Combination: Req-ID Grounding + Gap Remediation | 188 | +5 | +5 | 0 | **198** |
| V-05 — Minimum-Density Path to 188 | 168 | 0 | 0 | 0 | **168** |

R10 V-04 alone reaches 198: C-31 (CONVICTION DELTA per-version Req-ID grounding) + C-32
(CONVICTION GAP DIAGNOSIS with subsection-level prescription and scout namespace). C-33 was
earned only by R10 V-03 — no R10 variant combined all three axes. The 203 ceiling is
unbroken: a variant must hold C-31 + C-32 + C-33 simultaneously.

**R11 design question:**

With 198 as the highest confirmed score and C-33 structurally orthogonal to C-31 + C-32,
R11 explores two tiers:

1. **Primary — reach 203:** R10 V-04 has C-31 + C-32. Adding C-33 in its v11-specified
   falsifiable form — "the barrier is X; the campaign succeeds if the spec supplies factual
   proof, the proposal supplies priced alternatives, and the pitch supplies emotional
   translation of X" — should yield the first 203 variant. V-03 (R11) tests this as a
   single-axis addition to R10 V-04.

2. **Secondary — probe above 203:** The v11 rubric's C-31 language names "citation
   direction" — not just "R-04" but "this version amplifies R-04's cost-of-inaction data."
   A structured per-version table with a dedicated Amplification chain column makes the
   direction mandatory per cell rather than instructed. Similarly, C-32 specifies "which
   scout sub-skill would surface the missing signal" — a table with an explicit scout
   sub-skill column enforces sub-skill specificity as a structural requirement. V-01 and
   V-02 probe whether tighter implementations of C-31 and C-32 reveal latent C-34 or C-35
   criteria above the 203 ceiling.

**Predicted scoring pattern:**

| Variant | Axis | Hypothesis | Expected v11 |
|---------|------|------------|--------------|
| V-01 — C-31 Citation Direction Table | Lifecycle emphasis | Citation-direction table may probe latent C-34 | **198 + ?** |
| V-02 — C-32 Subsection Prescription Table | Output format | Scout sub-skill column may probe latent C-34 | **198 + ?** |
| V-03 — C-33 Falsifiable Hypothesis Addition | Inertia framing | Adding C-33 to R10 V-04 base reaches 203 | **203** |
| V-04 — Triple: Tightened C-31 + C-32 + Falsifiable C-33 | REFLECTION + CLOSE + SETUP | Maximum ceiling probe: 203 + potential latent criteria | **203 + ?** |
| V-05 — Minimum-Density Path to 203 | Lifecycle compression | Minimum form of R10 V-04 + minimal C-33 addition | **203** |

---

## V-01 — C-31 Tightened: Citation Direction Table

**Axis:** Lifecycle emphasis — CAMPAIGN REFLECTION's CONVICTION DELTA sub-field is
restructured from per-version inline instruction into a mandatory per-version grounding
table with a dedicated "Amplification chain" column that requires citation direction, not
just citation reference.

**Hypothesis:** R10 V-01 earned C-31 by adding a per-version instruction: "Name the
specific spec Must-have Req-ID(s) whose factual record this version emotionally amplifies."
The v11 rubric's passing example distinguishes citation reference ("R-04") from citation
direction ("this version amplifies R-04's cost-of-inaction data"). The direction form
requires naming the specific factual claim being amplified — not just the identifier. A
per-version grounding table with an Amplification chain column enforces this structurally:
the model must complete "[Req-ID]'s [specific factual claim] is made visceral in this
version by [emotional register]" per cell, not just produce a Req-ID token. R10 V-04
structural form is preserved in full; only CONVICTION DELTA in CAMPAIGN REFLECTION is
modified. C-32 (CONVICTION GAP DIAGNOSIS) is retained from R10 V-04. C-33 absent.
Predicted score: 198 (C-31 + C-32 maintained) + possible C-34 for citation direction.

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

  TRACEABILITY AUDIT
    Return to the SCOUT TRACEABILITY TABLE in CAMPAIGN SETUP. For each row in the table:
    - Name the REQUIREMENTS Must-have that addresses this friction (by Req-ID).
    - Confirm the Must-have appears in the written spec as a distinct bulleted item.
    If any row has no corresponding Must-have in the written spec, name the gap explicitly.
    State which scout namespace could surface requirements to close it.

  CONVICTION DELTA
    For each pitch version, complete the grounding table before writing any delta claim.
    No impressionistic entry ("more visceral," "stronger fear of loss") earns the
    Amplification chain cell — only a statement naming the specific factual claim of the
    Req-ID being amplified:

    | Version | Conviction established (visceral claim) | Grounding Req-ID(s) | Amplification chain |
    |---------|-----------------------------------------|---------------------|---------------------|
    | Exec    |                                         |                     |                     |
    | Dev     |                                         |                     |                     |
    | Maker   |                                         |                     |                     |

    Grounding Req-ID(s): the canonical Must-have identifier(s) from the spec (e.g., R-01,
    R-04) whose factual record this pitch version emotionally amplifies. Required per row.
    Amplification chain: complete the form — "[Req-ID]'s [specific factual claim from
    Must-have] is made visceral in this version by [emotional register]." If no single
    Must-have is the primary foundation, name the closest Req-ID and mark the chain cell
    "GAP: [explanation of why no Must-have fully grounds this conviction claim]."

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

## V-02 — C-32 Tightened: Subsection Prescription Table

**Axis:** Output format — CAMPAIGN CLOSE's CONVICTION GAP DIAGNOSIS sub-section is
restructured from narrative prescription into a mandatory five-column table that requires
subsection-level specificity and a named scout sub-skill (not just scout namespace) per
diagnosed gap.

**Hypothesis:** R10 V-02 earned C-32 with a narrative instruction: "Name the specific
sub-section of the artifact where the conviction register breaks down...Name the scout
namespace and signal type." The v11 rubric's C-32 description tightens the scout field:
"specifying which scout sub-skill would surface the missing signal" — not just the
namespace (e.g., "scout") but the sub-skill within it (e.g., "scout-requirements,"
"scout-positioning"). A five-column table with a dedicated "Scout sub-skill" column makes
this mandatory per row, not optional within a prose block. The table also separates
"Register found" from "Register declared" as distinct columns, forcing the diagnosis to be
precise rather than implied. R10 V-04 structural form is preserved in full; only
CONVICTION GAP DIAGNOSIS in CAMPAIGN CLOSE is modified. C-31 (Req-ID grounding in
CONVICTION DELTA) is retained from R10 V-04. C-33 absent. Predicted score: 198 (C-31 +
C-32 maintained) + possible C-34 for sub-skill specificity.

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
  For each row marked partial or N in "Conviction type met", complete the diagnosis table.
  Leave the table empty and write "No conviction gaps detected." only if all rows are Y.

  | Artifact | Sub-section where gap originates | Register found | Register declared | Scout sub-skill | Evidence needed |
  |----------|----------------------------------|----------------|-------------------|-----------------|-----------------|
  |          |                                  |                |                   |                 |                 |

  Sub-section: the specific named section within the artifact where register breaks down —
  not the artifact alone (e.g., not "Spec") but the sub-section within it (e.g., "Spec
  REQUIREMENTS — Must-haves framed as emotional appeals rather than documented facts").
  Register found: one word — Factual, Optionality, or Emotional — describing what the
  artifact's dominant register actually is in that sub-section.
  Register declared: the conviction type the artifact was declared to produce (from the
  contract matrix: Factual for spec, Optionality for proposal, Emotional for pitch).
  Scout sub-skill: the specific signal-gathering sub-skill — not just the namespace — that
  would surface evidence to shift the register toward its declared type (e.g.,
  scout-requirements, scout-feasibility, scout-market, scout-positioning, scout-competitors).
  Evidence needed: one sentence describing the specific signal the scout sub-skill would
  produce that closes the register gap.

List any open question a future signal could resolve, with recommended namespace for each.
```

---

## V-03 — C-33 Falsifiable Hypothesis Addition

**Axis:** Inertia framing — CAMPAIGN SETUP gains a named CAMPAIGN CONVICTION HYPOTHESIS as
item 0 (before topic identity, before the INERTIA MODEL entity), framed as a falsifiable
hypothesis with an explicit falsification condition, per the v11 rubric's C-33 template.

**Hypothesis:** R10 V-04 reached 198 (C-31 + C-32) without a CAMPAIGN CONVICTION
HYPOTHESIS. C-33 requires item 0 in SETUP to name the dominant inertia barrier and frame
it as a falsifiable hypothesis: "the barrier is X; the campaign succeeds if the spec
supplies factual proof, the proposal supplies priced alternatives, and the pitch supplies
emotional translation of X." R10 V-03 earned C-33 but without the falsification condition
in explicit three-part form — it used a one-sentence hypothesis template. V-03 (R11) adds
C-33 to R10 V-04's base (198) using the v11 rubric's exact falsifiable form, with the
three falsification conditions spelled out as a named sub-item below the hypothesis
sentence. This is the most direct path to 203: R10 V-04 + C-33. C-31 and C-32 are
retained from R10 V-04. Predicted score: 203.

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

## V-04 — Triple Combination: Tightened C-31 + Tightened C-32 + Falsifiable C-33

**Axis:** CAMPAIGN REFLECTION (citation direction table) + CAMPAIGN CLOSE (subsection
prescription table) + CAMPAIGN SETUP item 0 (falsifiable conviction hypothesis) — all
three v11 criteria in their tightened R11 implementations.

**Hypothesis:** V-01 through V-03 each probe a single axis. V-04 combines all three. The
critical question: does combining tightened C-31 (citation direction table in REFLECTION)
with tightened C-32 (subsection prescription table in CLOSE) with falsifiable C-33 (item
0 in SETUP) simultaneously earn all three criteria at their v11-specified forms? If no
latent C-34 exists beyond the three v11 criteria, V-04 scores 203. If a latent C-34 exists
(probed by V-01 or V-02's tighter implementations), V-04 may score higher. V-04 is the
maximum-ceiling candidate of R11: it holds all structural invariants from prior rounds
intact and adds three structurally distinct new elements — one per phase of the campaign
(SETUP item 0, REFLECTION table, CLOSE table). Predicted score: 203 + possible C-34.

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
    For each pitch version, complete the grounding table before writing any delta claim.
    No impressionistic entry ("more visceral," "stronger fear of loss") earns the
    Amplification chain cell — only a statement naming the specific factual claim of the
    Req-ID being amplified:

    | Version | Conviction established (visceral claim) | Grounding Req-ID(s) | Amplification chain |
    |---------|-----------------------------------------|---------------------|---------------------|
    | Exec    |                                         |                     |                     |
    | Dev     |                                         |                     |                     |
    | Maker   |                                         |                     |                     |

    Grounding Req-ID(s): the canonical Must-have identifier(s) from the spec (e.g., R-01,
    R-04) whose factual record this pitch version emotionally amplifies. Required per row.
    Amplification chain: complete the form — "[Req-ID]'s [specific factual claim from
    Must-have] is made visceral in this version by [emotional register]." If no single
    Must-have is the primary foundation, name the closest Req-ID and mark the chain cell
    "GAP: [explanation of why no Must-have fully grounds this conviction claim]."

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
  For each row marked partial or N in "Conviction type met", complete the diagnosis table.
  Leave the table empty and write "No conviction gaps detected." only if all rows are Y.

  | Artifact | Sub-section where gap originates | Register found | Register declared | Scout sub-skill | Evidence needed |
  |----------|----------------------------------|----------------|-------------------|-----------------|-----------------|
  |          |                                  |                |                   |                 |                 |

  Sub-section: the specific named section within the artifact where register breaks down —
  not the artifact alone (e.g., not "Spec") but the sub-section within it (e.g., "Spec
  REQUIREMENTS — Must-haves framed as emotional appeals rather than documented facts").
  Register found: one word — Factual, Optionality, or Emotional — describing what the
  artifact's dominant register actually is in that sub-section.
  Register declared: the conviction type the artifact was declared to produce (from the
  contract matrix: Factual for spec, Optionality for proposal, Emotional for pitch).
  Scout sub-skill: the specific signal-gathering sub-skill — not just the namespace — that
  would surface evidence to shift the register toward its declared type (e.g.,
  scout-requirements, scout-feasibility, scout-market, scout-positioning, scout-competitors).
  Evidence needed: one sentence describing the specific signal the scout sub-skill would
  produce that closes the register gap.

List any open question a future signal could resolve, with recommended namespace for each.
```

---

## V-05 — Minimum-Density Path to 203

**Axis:** Lifecycle compression — maximum compression of V-04 (R11) while preserving all
nine structural invariants that must hold the 203 ceiling.

**Hypothesis:** V-04 (R11) carries explanatory and motivating prose beyond the structural
minimum for each criterion. V-05 strips every sentence not directly load-bearing for a
named criterion. The nine load-bearing structures that must survive intact:
- C-23: bracket notation line at each of the three contract reminders (three lines retained)
- C-26: three-field INERTIA MODEL entity + three-bullet conviction-type mapping (retained)
- C-27: SCOUT TRACEABILITY TABLE in CAMPAIGN SETUP, four-column, pre-population
  instruction (table + instruction retained; surrounding explanation stripped)
- C-28: "As you write each Must-have, complete its Req-ID and Must-have entry in the SCOUT
  TRACEABILITY TABLE in CAMPAIGN SETUP above. Every Must-have must correspond to a row in
  that table." (retained word-for-word)
- C-29: TRACEABILITY AUDIT sub-field in REFLECTION — all four components: explicit name,
  per-row Req-ID verification, gap naming, scout namespace prescription
- C-30: "Conviction type met" column in CLOSE + scoring instruction defining Y/partial/N
  per conviction type (one-sentence instruction + table retained)
- C-31: CONVICTION DELTA Req-ID grounding — minimum form: per-version Req-ID citation
  instruction retained; table form stripped to inline "Name Req-ID" instruction
- C-32: CONVICTION GAP DIAGNOSIS — minimum form: sub-section and scout namespace
  instruction retained; table form stripped to two-bullet prose
- C-33: CAMPAIGN CONVICTION HYPOTHESIS as item 0 — minimum form: hypothesis sentence
  template + falsification conditions in compressed two-item form
- C-18/C-19: double-prohibition preserved as two arms: "not before pitch production begins,
  not during pitch production" — no compression permitted here
Predicted score: 203. If lower, a stripped sentence was load-bearing; identify by diff
against V-04 R11.

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

3. Scout inventory — glob simulations/scout/ for this topic now. List every file by namespace.
   Unconditional.

4. SCOUT TRACEABILITY TABLE — pre-populate from the scout inventory. Fill Originating
   Friction and Scout File from scout-requirements findings; complete Req-ID and Must-have
   during Artifact 1 REQUIREMENTS writing.

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
    For each pitch version, name the specific spec Must-have Req-ID(s) whose factual
    record this version emotionally amplifies, then state the conviction established.
    If no single Must-have is primary, name the closest Req-ID and state the gap.
    Exec: [Req-ID grounded conviction delta]
    Dev: [Req-ID grounded conviction delta]
    Maker: [Req-ID grounded conviction delta]

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
register fails the declared type.

| Artifact | Path                                                         | Scout signal consumed | Conviction type met | Open questions |
|----------|--------------------------------------------------------------|-----------------------|---------------------|----------------|
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md               | (namespace or none)   | Y / partial / N     | (list)         |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md       | (namespace or none)   | Y / partial / N     | (list)         |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md            | (namespace or none)   | Y / partial / N     | (list)         |

CONVICTION GAP DIAGNOSIS
  For each row marked partial or N:
  - Name the specific sub-section where the conviction register breaks down (not the
    artifact name alone — the sub-section within it).
  - Name the scout sub-skill that would supply evidence to strengthen the register toward
    its declared type.
  If all rows are Y: "No conviction gaps detected."

List any open question a future signal could resolve, with recommended namespace for each.
```
