---
skill: quest-variate
skill_target: campaign-blueprint
date: 2026-03-17
round: 3
rubric: campaign-blueprint-rubric-v3-2026-03-17.md
---

# campaign-blueprint — Prompt Variations R3 (rubric v3-2026-03-17)

Five complete, runnable skill body variations. Single-axis first (V-01 through V-03),
then two combinations (V-04, V-05).

## R3 Context

Rubric v3 adds two criteria extracted from prior variation excellence signals:

| Criterion | Signal source | Pattern |
|-----------|---------------|---------|
| **C-15** — Pre-artifact forcing function | V-01 Signal 1 | Phase 0 as a mandatory pre-artifact block that anchors the inertia baseline and cross-artifact invariants, making C-06 and C-03 structurally enforced rather than instructionally hoped for |
| **C-16** — Named do-nothing propagation | V-01 Signal 2 | Do-nothing option assigned an explicit name in Phase 0 (e.g., "Option 0: Status Quo") that propagates through the proposal options list and pitch framing — tracked entity, not catch-all final option |

Max total: 130 pts. Golden threshold: all 5 essentials FULL + composite ≥ 87/130.

**R3 variation axes (single-axis first):**
- V-01: Inertia framing — inertia named first, Option 0 declared before the feature
- V-02: Lifecycle emphasis — Phase 0 as maximum-structure checklist with named ledger and explicit gate
- V-03: Phrasing register — conversational/imperative, Phase 0 as three direct questions
- V-04: Inertia framing + lifecycle emphasis (V-01 + V-02)
- V-05: Lifecycle emphasis + phrasing register + minimal density (V-02 + V-03 compressed)

---

## V-01 — Inertia Framing Axis

**Axis:** Inertia framing
**Hypothesis:** Naming Option 0 BEFORE naming the feature in Phase 0 establishes the do-nothing
state as the narrative anchor for the entire campaign. When inertia opens Phase 0, it cannot
collapse into a generic final option — the executor must confront what they are NOT building
before they write a single word about what they are building. This targeting strategy hits C-15
(Phase 0 as pre-artifact gate) and C-16 (Option 0 as named entity) through a single mechanism:
inertia-first ordering. The hypothesis is that front-loading the do-nothing name makes it
structurally impossible to omit from the proposal and pitch because it is already a first-class
entity in the executor's mental frame.

```
You are running /campaign-blueprint for: {topic}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 0: CAMPAIGN SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Complete all four steps before writing any artifact. Do not begin Artifact 1 until
[PHASE 0 COMPLETE] is printed.

Step 1 — Name what you will NOT build first:
  Option 0 name:  [short, memorable — e.g., "Status Quo", "Manual Workaround", "Current Process"]
  Option 0 desc:  [one sentence — what users do today without this feature]
  Option 0 cost:  [at least one concrete dimension: time / effort / risk — not qualitative only]
  Option 0 risk:  H / M / L

  This name is a tracked entity. It will appear verbatim as row 0 in the proposal and in
  the framing of each pitch version.

Step 2 — Name what you will build:
  Topic identity: [one sentence — feature name, primary audience, core problem solved]

Step 3 — Anchor the inertia baseline:
  Inertia baseline: [one sentence — the precise user behavior this feature replaces]
  Cross-artifact propagation: this sentence appears unchanged in spec PURPOSE,
  proposal Option 0 row, and exec pitch hook.

Step 4 — Scout inventory:
  Glob simulations/scout/ for {topic} now. List every file found, organized by namespace.
  Run unconditionally. If no files found, write: "Scout inventory: none."

[PHASE 0 COMPLETE]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 1: SPEC
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Read Phase 0. Pull scout-requirements if found in inventory.

Sections (all required):

  PURPOSE        — Open with the inertia baseline sentence from Phase 0 Step 3, verbatim.
                   Why does Option 0: [name] persist? What does it cost?
  REQUIREMENTS   — Bulleted, MoSCoW-tagged (M/S/C/W). Each Must-have anchored to the
                   inertia baseline. Include at least one requirement from the product/user
                   domain and one from the technical/architecture domain.
  DESIGN         — Components, data flow, key decisions. Specific enough to start from.
  CONSTRAINTS    — Technical, team, timeline, and dependency limits.
  OPEN QUESTIONS — At least two. At least one from the product/user domain and one from
                   the technical/architecture domain. For each: name the signal namespace
                   that could resolve it.

Write simulations/draft/specs/{topic}-spec-{date}.md

[SPEC WRITTEN]
GATE: Do not begin Artifact 2 until this file is confirmed written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 2: PROPOSAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Read the spec. Pull scout-feasibility if found in inventory.
PRESERVE: do not re-open any decision the spec resolved. No new design work.

Options (three minimum). Row 0 must be Option 0 using the exact name from Phase 0:

| Option | Name | Description | Pros | Cons | Risk (H/M/L) | Effort (S/M/L) |
|--------|------|-------------|------|------|--------------|----------------|
| 0 | [Phase 0 Option 0 name — verbatim] | [Phase 0 desc] | [what users keep] | [Phase 0 cost — quantified] | | |
| B | | | | | | |
| C | | | | | | |

Option 0 Cons cell must state at least one concrete dimension (time / effort / risk) —
not qualitative description only.

RECOMMENDATION: [option name]. Three reasons, each citing a spec decision or constraint.

Write simulations/draft/proposals/{topic}-proposal-{date}.md

[PROPOSAL WRITTEN — Option [X] recommended]
GATE: Do not begin Artifact 3 until this file is confirmed written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 3: PITCH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Read the proposal. Pull scout-positioning if found in inventory.
CARRIES FORWARD: the recommended option is the subject of all three versions.

Three versions in full. Each version names "Option 0: [Phase 0 name]" explicitly in framing.

EXEC VERSION (decision-makers)
  Hook: what does Option 0: [name] cost the organization while it remains the default?
        Use the Option 0 cost from Phase 0.
  What it does: business-level outcome from the recommended option.
  Why it matters: risk if Option 0 persists.
  What this is NOT: [two sentences of anti-positioning]
  What changes for this audience: [explicit delta — what conviction does this version
    establish that the spec and proposal did not?]
  CTA: approve / fund / unblock.

DEV VERSION (engineers and technical leads)
  Hook: what capability does Option 0: [name] prevent you from building today?
  What it does: references the technical design from the spec explicitly.
  Why it matters: technical debt or opportunity cost of maintaining Option 0.
  What this is NOT: [two sentences of anti-positioning]
  What changes for this audience: [explicit delta — what conviction does this version
    establish that the spec and proposal did not?]
  CTA: join beta / review the spec / contribute.

MAKER VERSION (practitioners — plain language only)
  Hook: the friction that Option 0: [name] requires every time. State it as the user feels it.
  What it does: plain language only — no spec terminology, no proposal jargon.
  Why it matters: time saved, steps removed, frustration resolved.
  What this is NOT: [two sentences of anti-positioning]
  What changes for this audience: [explicit delta — what conviction does this version
    establish that the spec and proposal did not?]
  CTA: try it / sign up / start now.

Write simulations/draft/pitches/{topic}-pitch-{date}.md

[PITCH WRITTEN]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN CLOSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Artifact | Path                                                         | Scout signal consumed | Open questions |
|----------|--------------------------------------------------------------|-----------------------|----------------|
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md               | (namespace or none)   | (list)         |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md       | (namespace or none)   | (list)         |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md            | (namespace or none)   | (list)         |

Option 0 propagation check: confirm Phase 0 name appears in proposal row 0 and in
all three pitch version framings. Correct any mismatch before closing.
```

---

## V-02 — Lifecycle Emphasis Axis

**Axis:** Lifecycle emphasis
**Hypothesis:** Giving Phase 0 maximum explicit structure — a numbered checklist, a named
Option 0 ledger template with fill-in fields, a cross-artifact invariants table, and a
hard gate — makes compliance requirements visible, auditable, and hard to skip. C-15
compliance becomes structural because Phase 0 is a distinct block with its own completion
marker. C-16 compliance becomes structural because the Option 0 ledger is a named artifact
with explicit propagation instructions — not a mention, a ledger. The risk is that ceremony
creates cognitive overhead and the executor fills in the template mechanically. The hypothesis
is that the template fields are specific enough (name / desc / cost-with-dimension / risk)
to prevent mechanical fill-in and that the propagation instruction embedded in the ledger
is more reliable than a downstream reminder.

```
You are running /campaign-blueprint for: {topic}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 0: PRE-ARTIFACT SETUP (mandatory — complete before any artifact begins)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

No artifact may be started until [PHASE 0 COMPLETE] is printed.

[ ] 1. OPTION 0 LEDGER — fill all fields:
        Name:         __________  (short, memorable — e.g., "Status Quo", "Manual Process")
        Description:  __________  (one sentence — what users do today without this feature)
        Cost:         __________  (at least one concrete dimension: time / effort / risk —
                                   not qualitative only; e.g., "~2 hrs/week per user",
                                   "3-step manual export for each record", "data loss risk
                                   on every deploy")
        Risk level:   H / M / L

        Propagation rule: this name appears verbatim in Artifact 2 option row 0 and in the
        framing of every pitch version in Artifact 3.

[ ] 2. FEATURE IDENTITY:
        One sentence — feature name, primary audience, core problem solved.

[ ] 3. INERTIA BASELINE (cross-artifact invariant):
        One sentence — the exact user behavior this feature replaces.
        This sentence propagates unchanged into:
          - Spec PURPOSE section (opening line)
          - Proposal Option 0 row (Description column)
          - Pitch EXEC version (hook)

[ ] 4. SCOUT INVENTORY:
        Glob simulations/scout/ for {topic} now. List all files by namespace.
        Unconditional. If none: "Scout inventory: none."

[ ] 5. ARTIFACT CONTRACT:
        | Field           | Spec                                              | Proposal                                            | Pitch                                              |
        |-----------------|---------------------------------------------------|-----------------------------------------------------|----------------------------------------------------|
        | READ            | Steps 1–4 above; scout-requirements if found      | Spec file; scout-feasibility if found               | Proposal file; scout-positioning if found          |
        | WRITE           | simulations/draft/specs/{topic}-spec-{date}.md    | simulations/draft/proposals/{topic}-proposal-{date}.md | simulations/draft/pitches/{topic}-pitch-{date}.md |
        | PRESERVE        | (first artifact — no prior decisions)             | All spec decisions — do not re-open                 | Recommended option — crystallize, not reopen       |
        | CARRIES FORWARD | Feature identity; inertia baseline; decisions     | Recommended option name; Option 0 cost              | (final artifact)                                   |

[PHASE 0 COMPLETE — do not begin Artifact 1 until this block is fully printed]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 1: SPEC
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Read Phase 0. Pull scout-requirements if found in inventory.

Sections (all required):

  PURPOSE        — Lead with the inertia baseline sentence from Phase 0 Step 3, verbatim.
                   What problem does Option 0: [ledger name] create or perpetuate?
  REQUIREMENTS   — Bulleted, MoSCoW-tagged (M/S/C/W). Pull scout-requirements if available.
                   Each Must-have anchored to the inertia baseline.
                   At least one from product/user domain; at least one from
                   technical/architecture domain.
  DESIGN         — Components, data flow, key decisions. Concrete enough to start building.
  CONSTRAINTS    — Technical, team, timeline, and dependency limits.
  OPEN QUESTIONS — At least two. One from product/user domain; one from
                   technical/architecture domain. For each: name the signal namespace
                   that could resolve it.

Write simulations/draft/specs/{topic}-spec-{date}.md

[SPEC WRITTEN]
GATE: Do not begin Artifact 2 until file is confirmed written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 2: PROPOSAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Read the spec. Pull scout-feasibility if found in inventory.
PRESERVE: do not re-open any spec decision. Do not add new design work.

Options table (three rows minimum). Row 0 is the Option 0 ledger entry from Phase 0:

| Option | Name | Description | Pros | Cons | Risk (H/M/L) | Effort (S/M/L) |
|--------|------|-------------|------|------|--------------|----------------|
| 0 | [Phase 0 ledger name — verbatim] | [Phase 0 description] | [what users keep] | [Phase 0 cost — quantified with concrete dimension] | | |
| B | | | | | | |
| C | | | | | | |

Option 0 name must be identical to the Phase 0 ledger. Cons cell must be quantified
(at least one concrete dimension — time, effort, or risk). Not qualitative only.

RECOMMENDATION: [option name]. Three reasons — each cites a specific spec decision
or constraint.

Write simulations/draft/proposals/{topic}-proposal-{date}.md

[PROPOSAL WRITTEN — Option [X] recommended]
GATE: Do not begin Artifact 3 until file is confirmed written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 3: PITCH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Read the proposal. Pull scout-positioning if found in inventory.
CARRIES FORWARD: recommended option is the subject of all three versions.

Three versions in full. Each version must name "Option 0: [ledger name]" in its framing.

EXEC VERSION (decision-makers)
  Hook: [Option 0 cost from ledger] — what accumulates while Option 0: [name] is the default?
  What it does: business outcome from the recommended option.
  Why it matters: risk if Option 0 continues.
  What this is NOT: [two sentences — anti-positioning]
  What changes for this audience: [named delta — conviction this version adds beyond spec/proposal]
  CTA: approve / fund / unblock.

DEV VERSION (engineers and technical leads)
  Hook: capability unlocked — what does Option 0: [name] prevent you from building?
  What it does: references the technical design from the spec explicitly.
  Why it matters: technical debt or opportunity cost of Option 0.
  What this is NOT: [two sentences — anti-positioning]
  What changes for this audience: [named delta — conviction this version adds beyond spec/proposal]
  CTA: join beta / review the spec / contribute.

MAKER VERSION (practitioners — plain language only)
  Hook: friction that Option 0: [name] requires, stated as the user feels it.
  What it does: plain language only — no spec terminology, no proposal jargon.
  Why it matters: time saved, steps removed, frustration resolved.
  What this is NOT: [two sentences — anti-positioning]
  What changes for this audience: [named delta — conviction this version adds beyond spec/proposal]
  CTA: try it / sign up / start now.

Write simulations/draft/pitches/{topic}-pitch-{date}.md

[PITCH WRITTEN]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN CLOSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Artifact | Path                                                         | Scout signal consumed | Open questions |
|----------|--------------------------------------------------------------|-----------------------|----------------|
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md               | (namespace or none)   | (list)         |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md       | (namespace or none)   | (list)         |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md            | (namespace or none)   | (list)         |

Option 0 propagation audit:
- Phase 0 ledger name: [name]
- Proposal row 0 name: [confirm verbatim match]
- Pitch framing (exec / dev / maker): [confirm present in all three versions]
```

---

## V-03 — Phrasing Register Axis

**Axis:** Phrasing register (conversational / imperative)
**Hypothesis:** Short, direct imperative commands produce more reliable structural compliance
than formal headers and checklists. "Name the thing you won't build — call it Option 0: [name]"
is harder to skip than a labeled ledger template that can be filled mechanically. The
conversational register also reduces word count, which keeps the executor focused on the
semantic requirement rather than the ceremony. Phase 0 as three direct questions (what do
users do today? what won't you build? what scout signals exist?) communicates the mandatory
pre-artifact intent without bureaucratic framing. The risk is that minimal structure produces
minimal output — an executor who writes "Option 0: the old way" satisfies the letter but not
the spirit. This round tests whether imperative directness or structured completeness produces
more reliable C-16 propagation.

```
You are running /campaign-blueprint for: {topic}

Before you write anything, answer three questions. This is Phase 0. Do not begin the spec
until all three are answered and written.

  1. What do users do today?
     One sentence — the exact behavior this feature would replace. This is your inertia
     baseline. It opens the spec PURPOSE section, anchors the proposal Option 0 row, and
     drives the exec pitch hook.

  2. What are you NOT building?
     Name it. Assign it Option 0: [short, memorable name — e.g., "Status Quo", "The Manual
     Way", "Current Export Process"]. Write the cost: what does Option 0 cost users? Name
     at least one concrete dimension — time, effort, or risk. Not "it's inconvenient" —
     "~45 min per user per week" or "data integrity risk on every handoff".
     You will use this exact name in the proposal table and in all three pitch versions.

  3. What scout signals exist?
     Glob simulations/scout/{topic}/ now. List what you find. If nothing, write "none."

[PHASE 0 COMPLETE]

---

ARTIFACT 1: SPEC

Read your Phase 0 answers. Pull scout-requirements if you found one.
Write simulations/draft/specs/{topic}-spec-{date}.md

  PURPOSE — Start with your inertia baseline sentence. Why does Option 0: [name] keep
             happening? What does it cost?
  REQUIREMENTS — MoSCoW-tagged bullets. Every Must-have traces to the inertia baseline.
                 Include at least one question from the product/user world and one from
                 the technical world.
  DESIGN — How this works: components, data flow, key decisions. Enough to start building.
  CONSTRAINTS — What limits you: technology, team size, timeline, dependencies.
  OPEN QUESTIONS — At least two. One product/user question. One technical/architecture
                   question. For each, name the signal namespace that could answer it.

[SPEC WRITTEN]
Don't start the proposal until the spec file is on disk.

---

ARTIFACT 2: PROPOSAL

Read the spec. Pull scout-feasibility if you found one.
Don't reopen anything the spec already decided. No new design work.
Write simulations/draft/proposals/{topic}-proposal-{date}.md

Options table — at least three rows. Row 0 is Option 0 from your Phase 0 answer:

| Option | Name | Description | Pros | Cons | Risk (H/M/L) | Effort (S/M/L) |
|--------|------|-------------|------|------|--------------|----------------|
| 0 | [Phase 0 name — exact] | [Phase 0 description] | [what users keep] | [Phase 0 cost — quantified] | | |
| B | | | | | | |
| C | | | | | | |

Option 0 Cons must be quantified — at least one concrete dimension.
Pick one option. Three reasons why — each tied to a spec decision or constraint.

[PROPOSAL WRITTEN — Option [X] recommended]
Don't start the pitch until the proposal file is on disk.

---

ARTIFACT 3: PITCH

Read the proposal. Pull scout-positioning if you found one.
You're pitching the recommended option. Three full versions.
Write simulations/draft/pitches/{topic}-pitch-{date}.md

Each version names "Option 0: [your Phase 0 name]" in its framing — it is the alternative
the audience is weighing against.

EXEC
  Hook: what does Option 0: [name] cost the organization right now? (Use Phase 0 cost.)
  Then: what the recommended option changes, at the business level.
  Then: risk if Option 0 continues.
  Anti-positioning: what this is NOT — two sentences.
  What changes for this audience: what conviction does this version add that spec and proposal didn't?
  CTA: approve, fund, or unblock.

DEV
  Hook: what can you build or unblock that Option 0: [name] prevents today?
  Then: the technical components from the spec, named explicitly.
  Then: what Option 0 is costing in technical debt or opportunity.
  Anti-positioning: what this is NOT — two sentences.
  What changes for this audience: what conviction does this version add that spec and proposal didn't?
  CTA: join beta, review the spec, or contribute.

MAKER
  Hook: the thing Option 0: [name] makes you do every time — plain language, as the user
        feels it, not as the feature solves it.
  Then: what goes away when this ships. No spec terms. No proposal jargon.
  Then: time saved, steps removed, frustration resolved.
  Anti-positioning: what this is NOT — two sentences.
  What changes for this audience: what conviction does this version add that spec and proposal didn't?
  CTA: try it, sign up, or start now.

[PITCH WRITTEN]

---

Done. Fill in the close table:

| Artifact | Path                                                         | Scout signal used     | Open questions |
|----------|--------------------------------------------------------------|-----------------------|----------------|
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md               | (namespace or none)   | (list)         |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md       | (namespace or none)   | (list)         |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md            | (namespace or none)   | (list)         |

Confirm Option 0 name from Phase 0 appears in proposal row 0 and in all three pitch
versions. If it doesn't, fix it before closing.
```

---

## V-04 — Inertia Framing + Lifecycle Emphasis (V-01 + V-02)

**Axes:** Inertia framing + Lifecycle emphasis
**Hypothesis:** V-01 makes inertia the narrative anchor (Option 0 declared before the feature)
and V-02 gives Phase 0 maximum explicit structure (numbered checklist, ledger template, contract
table, gate). Combined: inertia-first ordering creates the semantic frame while the structured
ledger creates the auditable artifact. The contract table (C-09) is embedded in Phase 0
alongside the Option 0 ledger (C-16) and the inertia baseline propagation rule (C-06/C-15)
— all cross-artifact invariants live in one block. The hypothesis is that concentrating all
pre-execution obligations into a single Phase 0 with inertia as the organizing principle
achieves both C-15 full credit (mandatory pre-artifact gate) and C-16 full credit (named
entity with explicit propagation path) while also covering C-09 at the same site. The risk
is that the Phase 0 block becomes dense enough to overwhelm — the executor skims rather
than completes.

```
You are running /campaign-blueprint for: {topic}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 0: PRE-ARTIFACT INVARIANTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Complete all five items. Print [PHASE 0 COMPLETE] before any artifact begins.

1. OPTION 0 LEDGER — name the do-nothing state first:
   Name:         __________  [short, memorable — e.g., "Status Quo", "Manual Process"]
   Description:  __________  [one sentence — what users do today without this feature]
   Cost:         __________  [at least one concrete dimension: time / effort / risk]
   Risk level:   H / M / L
   Propagation:  this name appears verbatim in Artifact 2 options table (row 0) and in
                 the framing of all three Artifact 3 pitch versions.

2. FEATURE IDENTITY:
   One sentence — feature name, primary audience, core problem solved. The problem
   statement restates the Option 0 cost as an unsolved need.

3. INERTIA BASELINE (cross-artifact invariant):
   One sentence — the exact user behavior this feature replaces. Propagates unchanged into:
     - Spec PURPOSE (opening line)
     - Proposal Option 0 Description cell (same as ledger description)
     - Pitch EXEC version hook

4. SCOUT INVENTORY:
   Glob simulations/scout/ for {topic} now. List all files by namespace. Unconditional.
   If none: "Scout inventory: none."

5. ARTIFACT CONTRACT:
   | Field           | Spec                                           | Proposal                                            | Pitch                                               |
   |-----------------|------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|
   | READ            | Steps 1–4; scout-requirements if found         | Spec file; scout-feasibility if found               | Proposal file; scout-positioning if found           |
   | WRITE           | simulations/draft/specs/{topic}-spec-{date}.md | simulations/draft/proposals/{topic}-proposal-{date}.md | simulations/draft/pitches/{topic}-pitch-{date}.md |
   | PRESERVE        | (first artifact — no prior decisions)          | All spec decisions — do not re-open                 | Recommended option — crystallize, not reopen        |
   | CARRIES FORWARD | Feature identity; inertia baseline; decisions  | Recommended option name; Option 0 cost              | (final artifact)                                    |

[PHASE 0 COMPLETE — do not begin Artifact 1 until this block is fully printed]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 1: SPEC
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Read Phase 0. Pull scout-requirements if found in inventory.

Sections (all required):

  PURPOSE        — Lead with the inertia baseline sentence from Phase 0 Step 3, verbatim.
                   Why does Option 0: [ledger name] persist? What does it cost?
  REQUIREMENTS   — Bulleted, MoSCoW-tagged (M/S/C/W). Each Must-have anchored to the
                   inertia baseline. At least one from product/user domain; at least one
                   from technical/architecture domain.
  DESIGN         — Components, data flow, key decisions. Concrete enough to start building.
  CONSTRAINTS    — Technical, team, timeline, and dependency limits.
  OPEN QUESTIONS — At least two. One from product/user domain; one from
                   technical/architecture domain. For each: name the signal namespace
                   that could resolve it.

Write simulations/draft/specs/{topic}-spec-{date}.md

[SPEC WRITTEN]
GATE: Do not begin Artifact 2 until file is confirmed written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 2: PROPOSAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Read the spec. Pull scout-feasibility if found in inventory.
PRESERVE: do not re-open any spec decision. No new design work.

Options table (three rows minimum). Row 0 is the Phase 0 ledger entry — name verbatim:

| Option | Name | Description | Pros | Cons | Risk (H/M/L) | Effort (S/M/L) |
|--------|------|-------------|------|------|--------------|----------------|
| 0 | [Phase 0 ledger name — verbatim] | [Phase 0 description] | [what users keep] | [Phase 0 cost — concrete dimension] | | |
| B | | | | | | |
| C | | | | | | |

Option 0 Cons must be quantified — concrete dimension, not qualitative description.

RECOMMENDATION: [option name]. Three reasons — each cites a specific spec decision
or constraint.

Write simulations/draft/proposals/{topic}-proposal-{date}.md

[PROPOSAL WRITTEN — Option [X] recommended]
GATE: Do not begin Artifact 3 until file is confirmed written to disk.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ARTIFACT 3: PITCH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Read the proposal. Pull scout-positioning if found in inventory.
CARRIES FORWARD: recommended option is the subject of all three versions.

Three versions in full. Each version names "Option 0: [Phase 0 ledger name]" explicitly
as the alternative the audience is weighing.

EXEC VERSION (decision-makers)
  Hook: what does Option 0: [name] cost the organization today? Use Phase 0 cost.
  What it does: business outcome from the recommended option.
  Why it matters: risk if Option 0 persists.
  What this is NOT: [two sentences — anti-positioning]
  What changes for this audience: [named delta — what conviction does this version
    establish that spec and proposal did not?]
  CTA: approve / fund / unblock.

DEV VERSION (engineers and technical leads)
  Hook: what does Option 0: [name] prevent you from building today?
  What it does: references technical design from the spec explicitly.
  Why it matters: technical debt or opportunity cost of Option 0.
  What this is NOT: [two sentences — anti-positioning]
  What changes for this audience: [named delta — what conviction does this version
    establish that spec and proposal did not?]
  CTA: join beta / review the spec / contribute.

MAKER VERSION (practitioners — plain language only)
  Hook: the friction Option 0: [name] requires — stated as the user feels it.
  What it does: plain language only — no spec terminology, no proposal jargon.
  Why it matters: time saved, steps removed, frustration resolved.
  What this is NOT: [two sentences — anti-positioning]
  What changes for this audience: [named delta — what conviction does this version
    establish that spec and proposal did not?]
  CTA: try it / sign up / start now.

Write simulations/draft/pitches/{topic}-pitch-{date}.md

[PITCH WRITTEN]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAMPAIGN CLOSE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Artifact | Path                                                         | Scout signal consumed | Open questions |
|----------|--------------------------------------------------------------|-----------------------|----------------|
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md               | (namespace or none)   | (list)         |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md       | (namespace or none)   | (list)         |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md            | (namespace or none)   | (list)         |

Option 0 propagation audit: Phase 0 ledger name → Proposal row 0 → Pitch (exec/dev/maker).
Confirm all three match the Phase 0 ledger name exactly. Correct any mismatch before closing.
```

---

## V-05 — Lifecycle Emphasis + Phrasing Register, Minimal Density (V-02 + V-03 compressed)

**Axes:** Lifecycle emphasis + Phrasing register (minimal density combination)
**Hypothesis:** V-02's structured Phase 0 checklist earns C-15 most reliably; V-03's direct
imperative phrasing keeps word count low and intent clear. Combined at minimum density: the
Phase 0 block retains all four required sub-steps but uses compressed imperative formatting
instead of formal labeled sections. The hypothesis is that a minimal-density Phase 0 with
explicit structure achieves the same C-15 and C-16 coverage as V-02 at lower cognitive cost
— if it does, this becomes the canonical form. If V-02's longer format scores meaningfully
higher, the ceremony is earning its keep and should be retained. Secondary test: does the
Option 0 ledger name propagate more reliably when it is written into the options table
template (V-02) vs when it is a conversational instruction with a downstream reminder
(V-03) vs when it is minimal but structured (V-05)?

```
You are running /campaign-blueprint for: {topic}

PHASE 0 — complete before Artifact 1. Print all four items.

  Inertia baseline:  [one sentence — what users do today without this feature]
  Option 0 name:     [short name for the do-nothing state — e.g., "Status Quo", "Manual Process"]
  Option 0 cost:     [one concrete dimension — time / effort / risk; not qualitative only]
  Scout inventory:   glob simulations/scout/{topic}/ now — list files by namespace or "none"

Propagation rule: Option 0 name appears verbatim in proposal row 0 and in all three pitch versions.

[PHASE 0 COMPLETE]

---

ARTIFACT 1: SPEC
Reads: Phase 0. Scout-requirements if found.
Writes: simulations/draft/specs/{topic}-spec-{date}.md

  PURPOSE — lead with the inertia baseline sentence from Phase 0, verbatim.
  REQUIREMENTS — MoSCoW-tagged; each Must-have tied to inertia baseline;
                 at least one product/user question, one technical/architecture question.
  DESIGN — components, data flow, key decisions. Enough to start building.
  CONSTRAINTS — technical, team, timeline, dependencies.
  OPEN QUESTIONS — min two; one product/user; one technical/architecture;
                   namespace recommendation per question.

[SPEC WRITTEN]
GATE: do not begin Artifact 2 until spec file is confirmed on disk.

---

ARTIFACT 2: PROPOSAL
Reads: spec. Scout-feasibility if found.
Preserves: all spec decisions — do not re-open, no new design work.
Writes: simulations/draft/proposals/{topic}-proposal-{date}.md

Options (3 minimum):
| Option | Name | Description | Pros | Cons (quantified) | Risk (H/M/L) | Effort (S/M/L) |
|--------|------|-------------|------|-------------------|--------------|----------------|
| 0 | [Phase 0 name — verbatim] | [Phase 0 description] | [what users keep] | [Phase 0 cost — concrete dimension] | | |
| B | | | | | | |
| C | | | | | | |

Recommendation: [option]. Three reasons citing spec decisions or constraints.

[PROPOSAL WRITTEN — Option [X] recommended]
GATE: do not begin Artifact 3 until proposal file is confirmed on disk.

---

ARTIFACT 3: PITCH
Reads: proposal. Scout-positioning if found.
Carries forward: recommended option — crystallize it, do not reopen.
Writes: simulations/draft/pitches/{topic}-pitch-{date}.md

Three full versions. Each names "Option 0: [Phase 0 name]" in its framing.

EXEC: Option 0 cost hook (use Phase 0 cost) / recommended option business outcome /
      risk of Option 0 continuing / anti-positioning (2 sentences) /
      delta for exec audience (named conviction beyond spec/proposal) / CTA: approve or fund.

DEV: what Option 0 prevents you from building / spec technical design named explicitly /
     Option 0 technical cost / anti-positioning (2 sentences) /
     delta for dev audience (named conviction beyond spec/proposal) / CTA: join beta or review spec.

MAKER: friction Option 0 requires — plain language, no spec or proposal terms /
       time saved, steps removed / anti-positioning (2 sentences) /
       delta for maker audience (named conviction beyond spec/proposal) / CTA: try it.

[PITCH WRITTEN]

---

CLOSE
| Artifact | Path                                                         | Scout signal consumed | Open questions |
|----------|--------------------------------------------------------------|-----------------------|----------------|
| Spec     | simulations/draft/specs/{topic}-spec-{date}.md               | (namespace or none)   | (list)         |
| Proposal | simulations/draft/proposals/{topic}-proposal-{date}.md       | (namespace or none)   | (list)         |
| Pitch    | simulations/draft/pitches/{topic}-pitch-{date}.md            | (namespace or none)   | (list)         |

Option 0 propagation check: Phase 0 name → Proposal row 0 → Pitch (exec/dev/maker all three).
Fix any mismatch before closing.
```

---

## Variation Summary

| ID   | Axis                                              | Hypothesis shorthand                                                                                                       |
|------|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| V-01 | Inertia framing                                   | Option 0 named before feature name — inertia-first ordering makes do-nothing a tracked entity before any artifact begins  |
| V-02 | Lifecycle emphasis                                | Maximum-structure Phase 0 checklist + ledger + contract table — completeness and auditability over conciseness            |
| V-03 | Phrasing register (conversational / imperative)   | Three direct questions replace formal headers — imperative directness produces more reliable compliance at lower word cost |
| V-04 | Inertia framing + lifecycle emphasis              | Inertia-first semantic frame + structured ledger: C-09/C-15/C-16 all anchored in one Phase 0 block                        |
| V-05 | Lifecycle emphasis + phrasing register (minimal)  | V-02 structure at V-03 density — tests whether ceremony in V-02 earns score or whether compressed form scores equally     |

## C-15 / C-16 Coverage by Variation

| ID   | C-15 mechanism                                                          | C-16 mechanism                                                                      |
|------|-------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| V-01 | Phase 0 with 4 explicit steps + [PHASE 0 COMPLETE] gate                 | Option 0 ledger named in Step 1; propagation rule stated; downstream gates confirm  |
| V-02 | Phase 0 checklist with 5 numbered items + explicit gate before Artifact 1 | Option 0 ledger template with fill-in fields + verbatim match rule in proposal and pitch |
| V-03 | Phase 0 as 3 direct questions + [PHASE 0 COMPLETE] marker + gate prose  | "Name it — call it Option 0: [name]" imperative + downstream confirm instruction    |
| V-04 | Phase 0 with 5 items (ledger + identity + baseline + scout + contract) + gate | Option 0 ledger first, propagation stated in ledger, confirmed in close audit   |
| V-05 | Phase 0 compressed block (4 fields) + [PHASE 0 COMPLETE] + gate per artifact | Propagation rule stated in Phase 0; options table verbatim match; close check   |

## R3 Diagnostic Questions

1. Does inertia-first ordering (V-01, V-04) produce stronger C-16 propagation than question-first
   ordering (V-03) or neutral ordering (V-02, V-05)?
2. Does the Option 0 ledger template with fill-in fields (V-02, V-04) produce more reliable
   verbatim propagation than a conversational instruction with downstream reminder (V-03, V-05)?
3. Does Phase 0 word count correlate with C-15 partial vs full credit — or does a minimal Phase 0
   (V-05) earn full credit if the gate and completion marker are present?
4. Does the contract table in Phase 0 (V-02, V-04) create redundancy with the per-artifact
   READ/WRITE/PRESERVE headers, or does the upfront declaration add a measurable C-09 score
   advantage?
5. Does the named "propagation audit" in the campaign close (V-01, V-02, V-04, V-05) produce
   higher C-16 scores than the inline confirmation instruction (V-03) — or does the close-time
   check arrive too late to influence execution?
