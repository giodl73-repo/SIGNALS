# campaign-blueprint — Skill Body Variations R4 (V-01 through V-05)

---

## V-01 — Single Axis: Lifecycle Emphasis

**Axis:** Phase-gated lifecycle with mandatory entry/exit conditions  
**Hypothesis:** Hard-gating each phase with an explicit marker that must appear in output before the next phase begins eliminates implicit assumptions about completion and makes execution state fully auditable.

---

```markdown
You are running the campaign-blueprint skill for topic: {topic}.

This skill produces three coordinated artifacts — a technical spec, a business proposal, and an executive
pitch — in a single orchestrated session.

Execution is phase-gated. Each phase has an entry condition and an exit condition. You MUST emit the gate
marker before advancing to the next phase. Do not begin a later phase if the prior gate marker has not been
written into the output.

---

## Phase 0 — Setup Gate

**Entry condition:** Session starts.
**Exit condition:** You write `[PHASE-0-COMPLETE]` after completing all fields below.

Complete the artifact contract matrix before writing any artifact:

| Artifact | READS FROM | WRITES TO | PRESERVES | CARRIES FORWARD |
|---|---|---|---|---|
| Spec | Topic definition | spec file | open questions | constraints + decisions |
| Proposal | Spec decisions | proposal file | spec constraints | recommended option |
| Pitch | Proposal recommendation | pitch file | proposal framing | per-audience deltas |

Then complete the Phase 0 ledger. All four fields are required:

- **Inertia baseline** — What do users do today instead of this feature? One concrete sentence.
- **Option 0 name** — Assign the do-nothing option a name now. Format: "Option 0: [Label]." This name
  will propagate to the proposal and pitch unchanged.
- **Option 0 cost** — One concrete quantified dimension (time, effort, or risk). Not qualitative.
- **Scout result** — List available scout signals for this topic or write "scout: none available."

Write `[PHASE-0-COMPLETE]` when the matrix and all four ledger fields are complete.

---

## Phase 1 — Technical Spec

**Entry condition:** `[PHASE-0-COMPLETE]` is present in output.
**Exit condition:** You write `[SPEC WRITTEN]` after the spec is complete.

Write to `simulations/draft/specs/{topic}-spec-{date}.md`.

Required sections:
- **PURPOSE** — One paragraph. References the inertia baseline from Phase 0.
- **REQUIREMENTS** — MoSCoW table. Minimum: 2 Must-Have, 1 Should-Have, 1 Won't-Have.
- **DESIGN** — Technical approach. Incorporate any scout signals from Phase 0.
- **CONSTRAINTS** — What cannot be changed. What this feature must not break.
- **OPEN QUESTIONS** — Two minimum: one from the product/user domain, one from the
  technical/architecture domain. No boilerplate.

Write `[SPEC WRITTEN]` when complete. Do not begin Phase 2 until this marker is written.

---

## Phase 2 — Business Proposal

**Entry condition:** `[SPEC WRITTEN]` is present in output.
**Exit condition:** You write `[PROPOSAL WRITTEN — Option X recommended]` (replace X with the
recommended option number).

Write to `simulations/draft/proposals/{topic}-proposal-{date}.md`.

Required content:
- **Option 0** (the name from Phase 0) appears as the first option.
- **Three options minimum** including Option 0. Each has: description, cost/effort estimate, risk,
  and comparison to Option 0 on the quantified dimension.
- **Option 0's cost** uses the quantified dimension from Phase 0 ledger.
- **RECOMMENDATION section** names the recommended option and references at least two decisions
  from the spec.

Write `[PROPOSAL WRITTEN — Option X recommended]` when complete.

---

## Phase 3 — Executive Pitch

**Entry condition:** `[PROPOSAL WRITTEN — Option X recommended]` is present in output.
**Exit condition:** You write `[PITCH WRITTEN]` after all three audience versions are complete.

Write to `simulations/draft/pitches/{topic}-pitch-{date}.md`.

Required content:
- **Three audience versions:** exec, developer, maker.
- **Anti-positioning section** (shared or per-version): at least two "what this is NOT" statements.
- **Per-audience delta statement:** each version contains an explicit "what changes for [audience]" —
  a named delta from the base recommendation, not just audience-appropriate phrasing.
- The recommended option from Phase 2 is the pitch's subject throughout. No contradictions with the
  proposal.

Write `[PITCH WRITTEN]` when complete.

---

## Completion Check

When all four markers are present — `[PHASE-0-COMPLETE]`, `[SPEC WRITTEN]`,
`[PROPOSAL WRITTEN — Option X recommended]`, `[PITCH WRITTEN]` — verify:

1. Proposal references spec decisions (name at least two)
2. Pitch references proposal's recommended option by name
3. Option 0 name from Phase 0 appears in both proposal and pitch
4. No cross-artifact contradictions

Output: `campaign-blueprint complete: {topic} — {date} — Option {X} recommended.`
```

---

## V-02 — Single Axis: Inertia Framing

**Axis:** Status-quo competitor as primary structural anchor throughout all artifacts  
**Hypothesis:** Naming "Option 0: Status Quo" as a tracked entity before any artifact is written and treating it as the primary comparison baseline throughout all three artifacts produces stronger inertia coverage than positioning do-nothing as a catch-all final option.

---

```markdown
You are running the campaign-blueprint skill for topic: {topic}.

Before writing a single word of any artifact, name the enemy.

The enemy is not a competitor product. The enemy is what your users do today instead of this feature. It
has a name. That name is "Option 0: [Status Quo Label]." You will choose this label now, in Phase 0. Once
named, Option 0 appears in every artifact — not as a throwaway alternative, but as the baseline against
which all other options are measured.

---

## Phase 0 — Name the Enemy

Answer these four questions before anything else:

1. **What do users do today?** One concrete sentence describing current behavior.
2. **What does that cost them?** One quantified dimension — time, effort, or risk. Be specific.
3. **What is the name of Option 0?** Format: "Option 0: [Status Quo Label]" — e.g., "Option 0: Manual
   Export" or "Option 0: Spreadsheet Tracking."
4. **What scout signals exist for this topic?** List them or write "scout: none available."

Declare the artifact handoff chain:
- Spec reads from topic definition → carries forward constraints and decisions
- Proposal reads from spec decisions → carries forward the recommended option
- Pitch reads from proposal recommendation → carries forward per-audience delta framing

Also declare the contract matrix:

| Artifact | READS FROM | WRITES TO | PRESERVES | CARRIES FORWARD |
|---|---|---|---|---|
| Spec | Topic definition | spec file | open questions | constraints + decisions |
| Proposal | Spec decisions | proposal file | spec constraints | recommended option |
| Pitch | Proposal recommendation | pitch file | proposal framing | per-audience deltas |

Write `[PHASE-0-COMPLETE]` when all four questions are answered and the matrix is declared.

---

## Phase 1 — Technical Spec

Write to `simulations/draft/specs/{topic}-spec-{date}.md`.

Open the PURPOSE section with a direct reference to Option 0 by its Phase 0 name: "Today, [Option 0
label]. This feature changes that by..." This sets the inertia baseline in the first sentence so every
design decision is grounded in what it replaces.

Required sections:
- **PURPOSE** — Opens with Option 0 reference. What this feature does and why it exists.
- **REQUIREMENTS** — MoSCoW table. Include at least one requirement that directly addresses a gap in
  Option 0. Min: 2 Must-Have, 1 Should-Have, 1 Won't-Have.
- **DESIGN** — Technical approach. Incorporate scout signals from Phase 0 if available.
- **CONSTRAINTS** — Hard limits. What cannot change. What must not break.
- **OPEN QUESTIONS** — Two minimum: one product/user question, one technical/architecture question.

Write `[SPEC WRITTEN]` when complete.

---

## Phase 2 — Business Proposal

Write to `simulations/draft/proposals/{topic}-proposal-{date}.md`.

Option 0 is your first option. Write it first, name it by its Phase 0 label, and quantify its cost using
the dimension identified in Phase 0. Do not bury it at the end. It sets the floor. Every other option is
measured against it.

Required content:
- **Option 0: [Phase 0 label]** — First option, listed first. Quantified cost. Concrete.
- **Two or more additional options.** Each compares to Option 0 on the same quantified dimension.
- **RECOMMENDATION** — Names the recommended option. Explains why it beats Option 0 on the quantified
  dimension. References at least two decisions from the spec.

Write `[PROPOSAL WRITTEN — Option X recommended]` when complete.

---

## Phase 3 — Executive Pitch

Write to `simulations/draft/pitches/{topic}-pitch-{date}.md`.

Each audience version opens with the Option 0 cost framed for that audience. Executives see it as
organizational risk. Developers see it as engineering friction. Makers see it as wasted effort. The
quantified cost from Phase 0 is the same number — the framing shifts, not the stakes.

Required content:
- **Exec version** — Leads with Option 0 risk. Recommends Option X. Names the exec-specific delta.
- **Developer version** — Leads with Option 0 friction. Recommends Option X. Names the developer delta.
- **Maker version** — Leads with Option 0 wasted effort. Recommends Option X. Names the maker delta.
- **Anti-positioning section** (shared or per-version): at least two "what this is NOT" statements.

Write `[PITCH WRITTEN]` when complete.

---

## Inertia Propagation Check

Before declaring done, verify the propagation chain:
- Option 0 by Phase 0 name appears in spec (PURPOSE), proposal (first option), and all three pitch
  versions
- The quantified cost from Phase 0 appears in the proposal's Option 0 section and at least one pitch
  version
- Proposal's recommended option matches the pitch's subject
- No artifact contradicts another on what Option 0 is or costs

Output: `campaign-blueprint complete: {topic} — {date} — Option {X} recommended over Option 0: {label}.`
```

---

## V-03 — Single Axis: Phrasing Register (Imperative/Conversational)

**Axis:** Direct second-person imperative commands; no passive constructions; no phase preamble  
**Hypothesis:** Replacing structural phase descriptions with direct imperatives ("Write this field now," "Name it before moving on") reduces executor skipping of required steps because imperative commands are harder to interpret as optional than descriptive requirements.

---

```markdown
Run the full specification campaign for {topic}. You're producing three artifacts: a spec, a proposal,
and a pitch. They have to be coherent with each other. The proposal references the spec. The pitch
references the proposal. Do them in order. Don't skip ahead.

---

## Step 0 — Do this before you open any artifact file

Name the do-nothing option. Right now. What do users do today instead of building this feature? Give it
a specific label. Call it "Option 0: [Label]." Write it down before you forget it.

Quantify its cost. Pick one dimension — time, effort, or risk. Give a real number or estimate. Vague
doesn't count.

Declare your artifact contracts. What does the spec hand to the proposal? What does the proposal hand
to the pitch? One sentence per handoff.

Fill the contract matrix:

| Artifact | READS FROM | WRITES TO | PRESERVES | CARRIES FORWARD |
|---|---|---|---|---|
| Spec | Topic definition | spec file | open questions | constraints + decisions |
| Proposal | Spec decisions | proposal file | spec constraints | recommended option |
| Pitch | Proposal recommendation | pitch file | proposal framing | per-audience deltas |

Check scout signals. Do any scout artifacts exist for this topic? List them. If none, write "scout: none
available" and move on.

Write `[PHASE-0-COMPLETE]` when you're done. Don't open the spec file until you write it.

---

## Step 1 — Write the spec

File: `simulations/draft/specs/{topic}-spec-{date}.md`

Five sections. Write all five:

**PURPOSE** — What does this feature do and why? Reference what users do today (your Option 0 label).
One paragraph.

**REQUIREMENTS** — MoSCoW table. At least two Must-Haves, one Should-Have, one Won't-Have.

**DESIGN** — How does it work technically? Pull in any scout signals you found.

**CONSTRAINTS** — What can't you change? What must you not break? Be concrete.

**OPEN QUESTIONS** — Write two real questions. One about the user or product side. One about the
technical or architecture side. Not boilerplate — questions you actually need answered.

Write `[SPEC WRITTEN]` when you're done. Don't open the proposal file until you write it.

---

## Step 2 — Write the proposal

File: `simulations/draft/proposals/{topic}-proposal-{date}.md`

Three options minimum. Option 0 goes first. It's the floor. Don't bury it at the end.

**Option 0: [your label from Step 0]** — What happens if you build nothing. Use the cost you
quantified in Step 0. Concrete.

**Option 1 and Option 2 (or more)** — Real alternatives. For each: what it is, what it costs, what
the risk is, how it compares to Option 0 on your quantified dimension.

**RECOMMENDATION** — Pick one. Say why you're recommending it over Option 0. Reference at least two
specific decisions from the spec you wrote in Step 1.

Write `[PROPOSAL WRITTEN — Option X recommended]` when you're done. Don't open the pitch file until
you write it.

---

## Step 3 — Write the pitch

File: `simulations/draft/pitches/{topic}-pitch-{date}.md`

Three versions. One per audience. Write all three.

**Exec version** — Business framing. Risk and return. Why does Option X beat Option 0 for them?

**Developer version** — Technical framing. What actually changes in the system? Be specific.

**Maker version** — User framing. What problem goes away? What do they stop doing?

For each version, say explicitly what changes for that audience compared to the base recommendation.
Name the delta — don't just reframe the same thing in different words.

Add an anti-positioning section: at least two "this is NOT" statements.

Write `[PITCH WRITTEN]` when you're done.

---

## Final check — look for these four markers

`[PHASE-0-COMPLETE]` — `[SPEC WRITTEN]` — `[PROPOSAL WRITTEN — Option X recommended]` — `[PITCH WRITTEN]`

All four present? Good. Now check:
- Does the proposal name two spec decisions? 
- Does the pitch name the proposal's recommended option?
- Does Option 0's label appear in both the proposal and the pitch?
- Any contradictions between artifacts?

If the checks pass: `campaign-blueprint complete: {topic} — {date} — Option {X} recommended.`
```

---

## V-04 — Combined Axes: Role Sequence + Output Format

**Axes:** (1) Pitch-alignment snapshot before spec; (2) Table-first output format throughout  
**Hypothesis:** Writing a lightweight pitch-alignment snapshot before the spec forces stakeholder framing to precede technical design, reducing spec/pitch divergence. Table-based format in Phase 0 and verification makes execution state scannable and reduces implicit interpretation.

---

```markdown
You are running the campaign-blueprint skill for topic: {topic}.

This skill produces three artifacts: a technical spec, a business proposal, and an executive pitch.

Standard sequence is spec → proposal → pitch. This variation inserts a lightweight pitch-alignment
snapshot (Phase A) before the spec to anchor stakeholder framing before technical decisions are locked.

Full sequence: Phase 0 (setup) → Phase A (pitch alignment) → Phase 1 (spec) → Phase 2 (proposal) →
Phase 3 (pitch, finalized).

---

## Phase 0 — Artifact Contract Matrix and Setup Ledger

Declare all contracts before writing. Fill both tables completely.

**Contract matrix:**

| Artifact | READS FROM | WRITES TO | PRESERVES | CARRIES FORWARD |
|---|---|---|---|---|
| Pitch alignment (Phase A) | Topic intent | scratch notes (not filed) | audience concerns | exec/dev/maker framing constraints |
| Spec (Phase 1) | Topic definition + alignment notes | spec file | open questions | constraints, decisions |
| Proposal (Phase 2) | Spec decisions + alignment framing | proposal file | spec constraints | recommended option |
| Pitch (Phase 3) | Proposal recommendation + alignment framing | pitch file | proposal framing | per-audience deltas |

**Phase 0 setup ledger:**

| Field | Value |
|---|---|
| Inertia baseline | What users do today instead of this feature |
| Option 0 name | "Option 0: [Label]" |
| Option 0 cost (concrete) | One quantified dimension — time, effort, or risk |
| Scout result | Available signals or "scout: none available" |

Write `[PHASE-0-COMPLETE]` when both tables are complete.

---

## Phase A — Pitch Alignment Snapshot

**Entry condition:** `[PHASE-0-COMPLETE]` present.

Before writing the spec, answer these three questions. These are not artifact content — they are
framing constraints the spec and proposal must honor.

| Audience | Alignment question | Your answer |
|---|---|---|
| Exec | One sentence: why does Option X beat Option 0 for them? | |
| Developer | One concrete technical change this feature introduces | |
| Maker | One thing they stop doing if this ships | |

Write `[PITCH-ALIGNMENT-COMPLETE]` when all three answers are written.

---

## Phase 1 — Technical Spec

**Entry condition:** `[PITCH-ALIGNMENT-COMPLETE]` present.

Write to `simulations/draft/specs/{topic}-spec-{date}.md`.

| Section | Requirement |
|---|---|
| PURPOSE | One paragraph. References inertia baseline from Phase 0. Consistent with exec framing from Phase A. |
| REQUIREMENTS | MoSCoW table. Min: 2 Must-Have, 1 Should-Have, 1 Won't-Have. |
| DESIGN | Technical approach. References developer framing from Phase A. Incorporates scout signals if available. |
| CONSTRAINTS | Hard limits. What cannot change. |
| OPEN QUESTIONS | Two minimum: one product/user, one technical/architecture. No boilerplate. |

Write `[SPEC WRITTEN]` when complete.

---

## Phase 2 — Business Proposal

**Entry condition:** `[SPEC WRITTEN]` present.

Write to `simulations/draft/proposals/{topic}-proposal-{date}.md`.

| Element | Requirement |
|---|---|
| Option 0 | First option listed. Uses Phase 0 name verbatim. Quantified cost from Phase 0 ledger. |
| Additional options | Two minimum beyond Option 0. Each compares to Option 0 on the quantified dimension. |
| RECOMMENDATION | Names recommended option. References two spec decisions. Echoes exec framing from Phase A. |

Write `[PROPOSAL WRITTEN — Option X recommended]` when complete.

---

## Phase 3 — Executive Pitch (Finalized)

**Entry condition:** `[PROPOSAL WRITTEN — Option X recommended]` present.

Write to `simulations/draft/pitches/{topic}-pitch-{date}.md`.

| Version | Requirement |
|---|---|
| Exec | Uses exec framing anchored in Phase A. Explicit delta: "what changes for this audience." |
| Developer | Uses developer framing anchored in Phase A. Explicit delta: "what changes for this audience." |
| Maker | Uses maker framing anchored in Phase A. Explicit delta: "what changes for this audience." |
| Anti-positioning | Shared or per-version. Min two "what this is NOT" statements. |

Write `[PITCH WRITTEN]` when complete.

---

## Completion Verification

| Check | Status |
|---|---|
| All four gate markers present | ✓ / ✗ |
| Proposal references two spec decisions (name them) | ✓ / ✗ |
| Pitch references proposal's recommended option by name | ✓ / ✗ |
| Option 0 name from Phase 0 appears in proposal and pitch | ✓ / ✗ |
| Phase A framing honored across spec, proposal, and pitch | ✓ / ✗ |
| No cross-artifact contradictions | ✓ / ✗ |

Output: `campaign-blueprint complete: {topic} — {date} — Option {X} recommended.`
```

---

## V-05 — Combined Axes: Lifecycle Emphasis + Inertia Framing

**Axes:** (1) Canonical 4-field Phase 0 as the mandatory minimal gate; (2) Option 0 propagation rule named explicitly as load-bearing  
**Hypothesis:** Specifying Phase 0 as exactly four required fields (not "at minimum four") and naming the gate marker and Option 0 propagation rule as the two load-bearing elements — not the field density — produces the highest C-17/C-18 compliance. The executor knows precisely what Phase 0 requires, and the propagation rule removes ambiguity about what "carrying Option 0 forward" means in practice.

---

```markdown
You are running the campaign-blueprint skill for topic: {topic}.

This skill produces three artifacts: a technical spec, a business proposal, and an executive pitch. The
proposal references the spec. The pitch references the proposal.

Everything starts in Phase 0. Phase 0 has exactly four fields. Completing Phase 0 is the structural gate
for all three artifacts. You do not need more than four fields. You do not proceed without completing all
four.

---

## Phase 0 — Canonical Setup Gate

**This phase has exactly four required fields. No field is optional. No additional fields are required.**

**Field 1 — Inertia baseline**
What do users do today instead of this feature? One concrete sentence.

**Field 2 — Option 0 name**
Assign the do-nothing option a name. Format: `Option 0: [Status Quo Label]`.

This name is the load-bearing propagation element. It MUST appear verbatim in the proposal options list
(as the first option) and in all three pitch audience versions. This is the propagation rule:

> Phase 0 Option 0 name → proposal options list (first entry) → pitch framing (all versions), by exact
> name, unchanged.

**Field 3 — Option 0 cost**
One quantified dimension: time, effort, or risk. A number or estimate. Not qualitative.

**Field 4 — Scout result**
List available scout signals for this topic or write `scout: none available`.

**Artifact contract matrix** (declared alongside Phase 0 — satisfies the contract requirement with no
separate declaration step):

| Artifact | READS FROM | WRITES TO | PRESERVES | CARRIES FORWARD |
|---|---|---|---|---|
| Spec | Topic definition + Phase 0 fields | spec file | open questions | constraints + decisions |
| Proposal | Spec decisions | proposal file | spec constraints | recommended option |
| Pitch | Proposal recommendation | pitch file | proposal framing | per-audience deltas |

**Gate marker:** Write `[PHASE-0-COMPLETE]` exactly once, after all four fields and the matrix are
complete.

This marker is load-bearing. Phases 1, 2, and 3 each require the prior phase's gate marker to be present
in output. No phase may begin without it.

---

## Phase 1 — Technical Spec

**Entry condition:** `[PHASE-0-COMPLETE]` is in output.

Write to `simulations/draft/specs/{topic}-spec-{date}.md`.

Required sections:
- **PURPOSE** — References inertia baseline (Phase 0 Field 1) in the first or second sentence.
- **REQUIREMENTS** — MoSCoW table. Min: 2 Must-Have, 1 Should-Have, 1 Won't-Have.
- **DESIGN** — Technical approach. Incorporates scout signals (Phase 0 Field 4) if available.
- **CONSTRAINTS** — Hard limits and non-negotiables.
- **OPEN QUESTIONS** — Two minimum: one product/user question, one technical/architecture question.
  Specific — no boilerplate.

**Exit marker:** Write `[SPEC WRITTEN]`.

---

## Phase 2 — Business Proposal

**Entry condition:** `[SPEC WRITTEN]` is in output.

Write to `simulations/draft/proposals/{topic}-proposal-{date}.md`.

Required content:
- **Option 0 appears first, by exact name.** Use the Phase 0 Field 2 label verbatim — propagation rule
  in effect. It is the floor all other options are measured against.
- **Option 0 cost** uses the quantified dimension from Phase 0 Field 3.
- **Two or more additional options** beyond Option 0. Each compares to Option 0 on the quantified
  dimension.
- **RECOMMENDATION section** names the recommended option and references at least two decisions from
  the spec.

**Exit marker:** Write `[PROPOSAL WRITTEN — Option X recommended]` (replace X).

---

## Phase 3 — Executive Pitch

**Entry condition:** `[PROPOSAL WRITTEN — Option X recommended]` is in output.

Write to `simulations/draft/pitches/{topic}-pitch-{date}.md`.

Required content:
- **Three audience versions:** exec, developer, maker.
- **Option 0 by Phase 0 name** appears in each version as the comparison baseline — propagation rule
  enforced through the final artifact.
- **Per-audience delta statement:** each version contains an explicit "what changes for [audience]" — a
  named delta, not just reframing.
- **Anti-positioning section:** at least two "what this is NOT" statements.

**Exit marker:** Write `[PITCH WRITTEN]`.

---

## Completion Verification

When all four markers are present:
`[PHASE-0-COMPLETE]` — `[SPEC WRITTEN]` — `[PROPOSAL WRITTEN — Option X recommended]` — `[PITCH WRITTEN]`

**Propagation rule check:** Does the Phase 0 Field 2 Option 0 name appear verbatim in the proposal's
first option and in all three pitch versions?

**Sequence integrity check:** Does the proposal reference two spec decisions by name? Does the pitch
reference the proposal's recommended option?

Output: `campaign-blueprint complete: {topic} — {date} — Option {X} recommended over Option 0: {label}.`
```

---

## Variation Summary

| Variation | Axis | Single/Combined | Key Structural Bet |
|---|---|---|---|
| V-01 | Lifecycle emphasis | Single | Hard entry/exit conditions on every phase prevent implicit advancement |
| V-02 | Inertia framing | Single | Option 0 as named competitor from first line drives propagation naturally |
| V-03 | Phrasing register | Single | Imperative commands are harder to skip than descriptive requirements |
| V-04 | Role sequence + Output format | Combined | Pitch-alignment snapshot before spec anchors stakeholder framing; tables make state scannable |
| V-05 | Lifecycle emphasis + Inertia framing | Combined | Canonical 4-field Phase 0 with explicit propagation rule as the load-bearing element of the gate |
