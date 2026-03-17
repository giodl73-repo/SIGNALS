---
skill: quest-variate
skill_target: campaign-blueprint
date: 2026-03-17
round: 9
rubric: campaign-blueprint-rubric-v9-2026-03-16.md
---

# campaign-blueprint — Prompt Variations R9

Five complete, runnable skill body variations. Single-axis first (V-01 through V-03),
then two combinations (V-04 through V-05).

## R9 Context

R8 variants scored under v9 retroactive scoring:

| Variant | v8 | C-28 | v9 |
|---------|-----|------|----|
| V-01 — C-27 + D8 Bracket: Named R8 Design Space | 173 | +5 | **178** |
| V-02 — C-27 + Compact C-26: SETUP Placement with Anchor | 168 | +5 | **173** |
| V-03 — C-27 Back-Reference Minimality: Pointer vs Directive | 173 | 0 | **173** |
| V-04 — Triple Compact at SETUP | 163 (est.) | +5 | **168** (est.) |
| V-05 — Minimal Density Path to 173 | 168 | 0 | **168** |

V-01 alone reaches the v9 ceiling of 178. The unique realization: bracket D8 + SETUP
placement + bulleted C-26 + active fill directive (C-28). V-02 and V-03 each miss one
of the two differentiating criteria (C-26 bullet form vs C-28 directive form). The
ceiling is locked until a v10 criterion is named.

**R9 design question:**

With 178 as the confirmed ceiling, R9 explores four open dimensions not yet stress-tested:

1. **Register robustness** — Is the V-01 form fragile under phrasing register change, or
   do the structural invariants (C-26, C-27, C-28, C-23) survive a conversational
   imperative register? If register is load-bearing for any criterion, this isolates it.

2. **REFLECTION depth** — The REFLECTION section has never been stress-tested for latent
   criteria. Adding a TRACEABILITY AUDIT sub-field (explicit per-row verification that
   every SCOUT TABLE row maps to a written Must-have) probes whether REFLECTION closure
   earns a C-29 criterion not yet named in v9.

3. **CLOSE quality** — The CLOSE table currently tracks logistics only (path, scout
   consumed, open questions). Adding a "Conviction type met" self-assessment column probes
   whether CLOSE has latent scoring potential beyond its current logistic function.

4. **Minimum-density form** — V-01 carries prose beyond the structural minimum for each
   criterion. V-05 compresses to the smallest prompt body that can hold all four
   invariants simultaneously. This establishes the skeleton floor for future rounds.

**Predicted scoring pattern:**

| Variant | Axis | Hypothesis | Expected v9 |
|---------|------|------------|-------------|
| V-01 — Register: Conversational imperative | Phrasing register | Register-neutral; structural invariants survive | **178** |
| V-02 — REFLECTION: Traceability audit sub-field | Lifecycle emphasis / REFLECTION depth | Probes C-29; scores 178 + possible bonus if rubric extends | **178 + ?** |
| V-03 — CLOSE: Conviction quality column | Output format / CLOSE completeness | Probes C-29/C-30 at CLOSE; scores 178 + possible bonus | **178 + ?** |
| V-04 — Combination: Audit + conviction quality | REFLECTION + CLOSE combined | Full traceability-conviction loop; may earn two new criteria | **178 + ??** |
| V-05 — Minimum-density path to 178 | Lifecycle compression | Minimum form holding all four v9 invariants | **178** |

---

## V-01 — Register: Conversational Imperative

**Axis:** Phrasing register — conversational imperative replacing formal technical
directives throughout, all structural invariants (C-23, C-26, C-27, C-28) preserved
unchanged in content.

**Hypothesis:** The four ceiling-holding invariants of V-01 (R8) are structural — they
are defined by what is present (bracket notation, bulleted mapping, SETUP placement,
active fill directive), not how that content is phrased. Rewriting every prose instruction
in a conversational first-person register should leave all criterion scores unchanged. If
any criterion turns out to be register-sensitive, this variant will isolate it, because
the only change is surface phrasing — no structural element is added, removed, or
reordered. Predicted score: 178. If lower, a criterion is phrasing-dependent; isolate it
by comparing line-by-line against V-01 (R8).

```
You are running /campaign-blueprint for: {topic}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Before you write anything, name the enemy. The INERTIA MODEL is the current behavior
this campaign has to displace — the status-quo opponent every artifact argues against.

1. Topic identity — one sentence: what is the feature, who is it for, what problem does
   it solve.

2. INERTIA MODEL — fill in all three fields:
     Name:     a short phrase that names the current behavior in shorthand
     Behavior: one sentence describing what users do today without this feature
     Cost:     one sentence covering what that behavior costs them — factual,
               priceable, and emotional dimensions in a single statement

   Each of the three conviction types draws on a different INERTIA MODEL field:
   - Factual conviction (spec):         puts the Cost on the record as verified fact
   - Optionality conviction (proposal): prices the Cost against every alternative
   - Emotional conviction (pitch):      makes the Cost feel urgent per audience

3. Scout inventory — run glob simulations/scout/ for this topic right now. List every
   file you find, organized by namespace. Do this unconditionally — do not skip it if
   signal files are sparse or absent.

4. SCOUT TRACEABILITY TABLE — use the scout inventory you just listed to pre-populate
   this table now. Each row stands for one friction the spec Must-haves will address.
   Fill Originating Friction and Scout File right now from scout-requirements findings.
   Leave Req-ID and Must-have blank — you will fill those in during REQUIREMENTS writing
   in Artifact 1.

   | Req-ID       | Must-have (brief)    | Originating Scout-Requirements Friction      | Scout File (path or "none") |
   |--------------|----------------------|----------------------------------------------|-----------------------------|
   | (fill in A1) | (fill in A1)         |                                              |                             |
   (one row per identified friction; if no scout-requirements file exists, add one row
   with Friction drawn from the INERTIA MODEL Cost and Scout File = "none")

5. Artifact contract matrix — what each artifact reads, writes, protects, and carries
   forward:

| Field           | Spec                                                             | Proposal                                                                    | Pitch                                                                              |
|-----------------|------------------------------------------------------------------|-----------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| READ            | Topic identity; INERTIA MODEL (all fields); scout-requirements if found | Spec file; INERTIA MODEL Cost; scout-feasibility if found          | Proposal file; INERTIA MODEL Cost; scout-positioning if found                      |
| WRITE           | simulations/draft/specs/{topic}-spec-{date}.md                   | simulations/draft/proposals/{topic}-proposal-{date}.md                      | simulations/draft/pitches/{topic}-pitch-{date}.md                                  |
| PRESERVE        | (first artifact)                                                 | All spec design decisions — no re-opening, no new design work               | Recommended option from proposal — crystallize, do not reconsider                  |
| CARRIES FORWARD | Feature identity; INERTIA MODEL (all fields); design decisions   | Recommended option name and rationale; INERTIA MODEL Cost                   | (final artifact)                                                                   |
| CONVICTION TYPE | Factual — documents INERTIA MODEL Cost as factual record         | Optionality — prices INERTIA MODEL Cost against each alternative            | Emotional — makes INERTIA MODEL Cost visceral per audience                         |

Print the full contract matrix before you start Artifact 1.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 1: SPEC — Factual Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: topic identity; INERTIA MODEL (Name, Behavior, Cost); scout-requirements if found.
                    PRESERVE: (first artifact — nothing to protect yet).
                    CONVICTION TYPE: Factual [INERTIA MODEL Cost → factual record]

Start with what the current behavior costs users. Do not move to what replaces it until
you have put that cost on the record as fact.

Sections (all required):

  PURPOSE        — Name the INERTIA MODEL and its Behavior, then document the Cost as
                   factual record. Frame: "The INERTIA MODEL creates [Cost] for [audience]
                   because [Behavior persists]."
  REQUIREMENTS   — Bulleted, MoSCoW-tagged (M/S/C/W). Pull scout-requirements if you
                   found one. As you write each Must-have, go to the SCOUT TRACEABILITY
                   TABLE in CAMPAIGN SETUP above and fill in its Req-ID and Must-have entry
                   before continuing. Every Must-have must have a row in that table.
  DESIGN         — Components, data flow, key decisions. Enough detail to start building.
  CONSTRAINTS    — Technical, team, timeline, and dependency limits.
  OPEN QUESTIONS — What you do not know yet. Name the namespace that could answer each.

GATE: Do not begin Artifact 2 until simulations/draft/specs/{topic}-spec-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 2: PROPOSAL — Optionality Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: spec file; INERTIA MODEL Cost; scout-feasibility if found.
                    PRESERVE: every spec design decision — do not reopen anything the spec settled.
                    CONVICTION TYPE: Optionality [INERTIA MODEL Cost → priced against each alternative]

Option A is always do-nothing — the INERTIA MODEL running at full Cost. Name that Cost
explicitly and concretely before you present any alternative. Every other option gets
measured against the INERTIA MODEL Cost, not against zero.

Three options minimum. Option A: do-nothing — state the INERTIA MODEL Cost as the price
of this option. Per option: Name / Description / Pros / Cons / Risk (H/M/L) / Effort
(S/M/L). Recommendation: the chosen option plus three reasons, each citing a specific
spec decision or constraint.

GATE: Do not begin Artifact 3 until simulations/draft/proposals/{topic}-proposal-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 3: PITCH — Emotional Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: proposal file; INERTIA MODEL Cost; scout-positioning if found.
                    PRESERVE: the recommended option from the proposal — crystallize it, do not revisit.
                    CONVICTION TYPE: Emotional [INERTIA MODEL Cost → visceral per audience]

Open every version with the INERTIA MODEL Cost as its hook. By now the audience has the
facts and the options — what they still need is to feel why the Cost of inaction exceeds
the cost of acting, and why that urgency is specific to them.

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

This phase opens only after the pitch file is on disk. Everything here looks backward
at completed work. The question running through every sub-field: did the artifact make
the INERTIA MODEL Cost land at its declared conviction level?

FINDINGS:

  CONVICTION DELTA
    Exec version: what conviction about the INERTIA MODEL Cost does this pitch establish
                  that the spec and proposal could not make visceral?
    Dev version: what conviction about the INERTIA MODEL Cost does this pitch establish
                 that the spec and proposal could not make visceral?
    Maker version: what conviction about the INERTIA MODEL Cost does this pitch establish
                   that the spec and proposal could not make visceral?

  NEAR-DUPLICATE CONTENT
    Name any passage you nearly copied from the spec or proposal.
    Say what you changed to make it conviction-bearing rather than informational.

  RESIDUAL QUESTIONS
    What would a specific scout signal resolve that no artifact answered from existing
    evidence? Name a namespace for each.

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

## V-02 — REFLECTION: Traceability Audit Sub-field

**Axis:** Lifecycle emphasis — REFLECTION section gains a TRACEABILITY AUDIT sub-field
that closes the SCOUT TRACEABILITY TABLE loop (table pre-populated in SETUP → rows
filled in REQUIREMENTS → rows audited in REFLECTION).

**Hypothesis:** The SCOUT TRACEABILITY TABLE criterion (C-27) and the active fill
directive (C-28) both operate in SETUP-to-REQUIREMENTS direction: the table is created
in SETUP, cells are filled during REQUIREMENTS writing. The loop has no explicit closing
instruction — REFLECTION currently asks about conviction delta, near-duplicate content,
and residual questions, but never asks whether every table row was actually addressed by
a written Must-have. Adding a TRACEABILITY AUDIT sub-field that instructs the model to
return to the SCOUT TRACEABILITY TABLE and verify per-row Must-have coverage closes this
loop. If the rubric extends to a C-29 (REFLECTION closes the traceability loop), this
variant earns it. If not, the structural invariants remain unchanged and the score holds
at 178. V-01 (R8) structural form is preserved in full; the only addition is the
TRACEABILITY AUDIT sub-field in CAMPAIGN REFLECTION.

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

## V-03 — CLOSE: Conviction Quality Column

**Axis:** Output format — CAMPAIGN CLOSE table gains a "Conviction type met" column
that self-assesses whether each artifact's dominant register matches its declared
conviction type.

**Hypothesis:** The CLOSE table currently earns whatever it earns as a pure logistics
record (path, scout consumed, open questions). It makes no quality judgment. The
conviction type for each artifact is declared at the contract matrix and enforced at each
artifact reminder — but there is no instruction to verify after completion that the
artifact's dominant register actually matches. Adding a self-assessment column (Factual /
Optionality / Emotional met? Y/partial/N) creates a closing quality gate. This may reveal
a C-29 or C-30 criterion (CLOSE self-assessment matches declared conviction types) not
yet named in v9. V-01 (R8) structural form is preserved in full; the only addition is
the conviction-quality column and its instruction in CAMPAIGN CLOSE. Predicted score: 178
minimum; possibly higher if CLOSE quality has latent scoring potential.

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

For "Conviction type met": assess whether each artifact's dominant register matches its
declared conviction type — Factual (spec), Optionality (proposal), Emotional (pitch).
Mark Y if dominant register matches; partial if conviction types are mixed; N if the
artifact's primary register fails the declared type.

| Artifact | Path                                                         | Scout signal consumed | Conviction type met | Open questions |
|----------|--------------------------------------------------------------|-----------------------|---------------------|----------------|
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md               | (namespace or none)   | Y / partial / N     | (list)         |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md       | (namespace or none)   | Y / partial / N     | (list)         |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md            | (namespace or none)   | Y / partial / N     | (list)         |

List any open question a future signal could resolve, with recommended namespace for each.
```

---

## V-04 — Combination: Traceability Audit + Conviction Quality

**Axis:** REFLECTION traceability audit (V-02) combined with CLOSE conviction quality
column (V-03) — full traceability-conviction loop: table pre-populated in SETUP → rows
filled active-directive in REQUIREMENTS → rows audited in REFLECTION → conviction quality
self-assessed in CLOSE.

**Hypothesis:** V-02 and V-03 each probe a different scoring frontier: V-02 tests
REFLECTION closure criteria; V-03 tests CLOSE quality criteria. Neither axis interacts
with the other — a REFLECTION audit does not affect CLOSE, and a CLOSE quality column
does not affect REFLECTION. If each independently earns a new criterion (C-29 for V-02,
C-30 for V-03), the combination earns both. If neither earns anything, V-04 still holds
178 because all v9 structural invariants are preserved unchanged. This variant is the
highest-ceiling candidate of R9: potential score 178 + C-29 + C-30 if both criteria
exist. V-01 (R8) structural form preserved throughout; REFLECTION and CLOSE are the
only additions.

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

For "Conviction type met": assess whether each artifact's dominant register matches its
declared conviction type — Factual (spec), Optionality (proposal), Emotional (pitch).
Mark Y if dominant register matches; partial if conviction types are mixed; N if the
artifact's primary register fails the declared type.

| Artifact | Path                                                         | Scout signal consumed | Conviction type met | Open questions |
|----------|--------------------------------------------------------------|-----------------------|---------------------|----------------|
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md               | (namespace or none)   | Y / partial / N     | (list)         |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md       | (namespace or none)   | Y / partial / N     | (list)         |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md            | (namespace or none)   | Y / partial / N     | (list)         |

List any open question a future signal could resolve, with recommended namespace for each.
```

---

## V-05 — Minimum-Density Path to 178

**Axis:** Lifecycle emphasis — maximum compression of all non-load-bearing prose while
preserving all four structural invariants: bracket notation D8 (C-23), bulleted C-26
field mapping, SETUP table placement (C-27), active fill directive (C-28).

**Hypothesis:** V-01 (R8) carries explanatory prose beyond the structural minimum for
each criterion — the opening paragraph of each artifact section, the full REFLECTION
preamble, the trailing CLOSE instruction. V-05 removes every sentence that is not
directly load-bearing for a named criterion. The result is the smallest prompt body that
can hold 178. This establishes the skeleton floor — the minimum density surface area —
for future rounds. Load-bearing content is identified criterion-by-criterion:
- C-23 load-bearing: bracket notation line at each contract reminder + CONVICTION TYPE
  row in matrix (both retained exactly)
- C-26 load-bearing: the bulleted list (three lines) in INERTIA MODEL item 2 (retained
  exactly; opening INERTIA MODEL framing prose stripped to minimum)
- C-27 load-bearing: SETUP section label + pre-population instruction + table + back-
  reference in REQUIREMENTS (all retained; surrounding explanation prose stripped)
- C-28 load-bearing: the "As you write each Must-have, complete its Req-ID..." sentence
  (retained word-for-word; surrounding context compressed)
Predicted score: 178. If lower, a stripped sentence was load-bearing; identify by diff.

```
You are running /campaign-blueprint for: {topic}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Topic identity — one sentence: feature name, audience, problem solved.

2. INERTIA MODEL — three-field declaration:
     Name:     current behavior in shorthand
     Behavior: what users do today without this feature — one sentence
     Cost:     what that costs them — one sentence (factual, priceable, emotional)

   - Factual conviction (spec):         documents the Cost field as factual record
   - Optionality conviction (proposal): prices the Cost field against each alternative
   - Emotional conviction (pitch):      makes the Cost field visceral per audience

3. Scout inventory — glob simulations/scout/ for this topic now. List every file by
   namespace. Unconditional.

4. SCOUT TRACEABILITY TABLE — pre-populate from the scout inventory above. Fill
   Originating Friction and Scout File now from scout-requirements findings; complete
   Req-ID and Must-have during Artifact 1 REQUIREMENTS writing.

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

Print the contract matrix in full. Do not begin Artifact 1 until it is printed.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 1: SPEC — Factual Conviction
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contract reminder — READ: topic identity; INERTIA MODEL (Name, Behavior, Cost); scout-requirements if found.
                    PRESERVE: (first artifact).
                    CONVICTION TYPE: Factual [INERTIA MODEL Cost → factual record]

Sections (all required):

  PURPOSE        — INERTIA MODEL Name and Behavior; Cost as factual record.
  REQUIREMENTS   — Bulleted, MoSCoW-tagged. Pull scout-requirements if available.
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
alternatives. Every other option measured against INERTIA MODEL Cost, not zero.

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

DEV (engineers) — urgency through blocked capability:
  Hook: what INERTIA MODEL Behavior prevents engineers from doing or building.
  What it does: references technical design from spec explicitly.
  Why it matters: technical debt or opportunity cost of sustained INERTIA MODEL Behavior.
  CTA: join beta / review spec / contribute.

MAKER (practitioners — plain language only) — urgency through daily INERTIA MODEL Cost:
  Hook: specific daily friction of INERTIA MODEL Behavior for this audience.
  What it does: no spec or proposal jargon — only what changes in daily work.
  Why it matters: time saved and steps removed.
  CTA: try it / sign up / start now.

ANTI-POSITIONING (shared): what this feature is NOT, two sentences.

GATE: Do not begin Campaign Reflection until simulations/draft/pitches/{topic}-pitch-{date}.md is written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN REFLECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

After pitch file exists on disk only. Retrospective assessment of completed artifacts.

FINDINGS:

  CONVICTION DELTA
    Exec: conviction about INERTIA MODEL Cost this pitch establishes that spec and
          proposal could not make visceral.
    Dev: same question for Dev version.
    Maker: same question for Maker version.

  NEAR-DUPLICATE CONTENT
    Any passage nearly copied from spec or proposal; what changed to make it
    conviction-bearing.

  RESIDUAL QUESTIONS
    Scout signal that would resolve what no artifact answered; namespace for each.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN CLOSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Artifact | Path                                                         | Scout signal consumed | Open questions |
|----------|--------------------------------------------------------------|-----------------------|----------------|
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md               | (namespace or none)   | (list)         |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md       | (namespace or none)   | (list)         |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md            | (namespace or none)   | (list)         |
```
