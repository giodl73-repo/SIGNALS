---
skill: quest-variate
skill_target: campaign-specify
round: 3
date: 2026-03-16
rubric: simulations/quest/rubrics/campaign-specify-rubric-v3-2026-03-16.md
---

# Variations — campaign-specify / Round 3

Five complete, runnable skill body variations targeting the v3 rubric.
Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

**R2 diagnosis driving R3 axis choices:**

V-04 and V-05 from R2 scored 100/100 under v3. C-14 and C-15 are the differentiating axis —
both require argumentative completeness around inaction: concrete per-audience inertia costs
(C-14) and an explicit named-competitor defeat of Do Nothing with cost citation (C-15).

R3 targets structural diversity that reliably produces C-14 and C-15 through different mechanisms:

| Axis | Mechanism | C-14 path | C-15 path |
|------|-----------|-----------|-----------|
| Inertia framing | Loss-first Phase 0 ordering | Named audience loss fields required | Loss cost fed into Recommendation template |
| Output format | Tabular options with Do Nothing row first | Inertia cost column per audience | Do Nothing row comparison forces explicit defeat |
| Lifecycle emphasis | Phase 0 heavy / phases 1-3 lean | Expanded Phase 0 with audience-specific loss templates | Recommendation defeat-template in Phase 2 |
| Inertia + falsifiability (combined) | Per-audience inertia costs + named-competitor framing | Phase 0 names audience cost; tracked through all phases | Do Nothing introduced as competitor in Phase 0, defeated in Phase 2 |
| Full combination | All axes | All C-14 mechanisms stacked | All C-15 mechanisms stacked |

---

## V-01 — Axis: Inertia Framing (loss-first Phase 0 ordering)

**Hypothesis**: Requiring inertia costs BEFORE voice contracts in Phase 0 anchors all
subsequent writing in concrete loss language. When the model writes the spec, proposal,
and pitch, the per-audience loss is already defined — C-14 is satisfied by construction
because Phase 0 cannot complete without it. C-15 follows because the recommendation
section can reference the already-defined exec/dev/maker inertia costs directly.

```
Run the campaign-specify skill for: {{topic}}

Produce three artifacts in sequence: spec, proposal, pitch. Execute the four phases
below in order. Do not begin a later phase until all required fields in the current
phase are complete.

---

## Phase 0 — Audience Foundation

Before writing anything, complete the three blocks below. This phase must finish before
Phase 1 begins.

**Step 0a — Inertia Costs (required first)**

Name what each audience LOSES if {{topic}} does not ship. Be concrete and audience-specific.
Generic value claims ("this would help") do not pass. Required form:

Exec inertia cost: [What revenue exposure, competitive gap, or risk persists without this feature?
Name a specific consequence, not a category.]

Dev inertia cost: [What workaround burden, capability gap, or tool-friction remains?
Name the specific friction, not just "inefficiency."]

Maker inertia cost: [What workflow stays blocked, degraded, or manual?
Name the specific step that fails without this feature.]

Do not advance to Step 0b until all three inertia costs are complete.

**Step 0b — Voice Contracts**

Using the inertia costs above as grounding, write one sentence per audience:

Exec voice: [The one sentence the exec cares about — frame in terms of the cost named above]
Dev voice: [The one sentence the dev cares about — frame in terms of the friction named above]
Maker voice: [The one sentence the maker cares about — frame in terms of the blocked workflow above]

**Step 0c — Scout Pull**

Glob `simulations/scout/**/*.md` for {{topic}}. List any files found. These signals
inform Phase 1 through Phase 3.

---

## Phase 1 — Technical Spec

Pull from `simulations/scout/` broadly before writing. Note which files were used.

Write the spec. Save to: `simulations/draft/specs/{{topic}}-spec-{{date}}.md`

The spec MUST contain all six sections. Do not skip or merge any section.

### Overview
One paragraph describing what the feature does and why it exists.

### User Problem
Describe the problem users face without this feature. Reference the dev and maker
inertia costs from Phase 0 — they name the specific friction.

### Proposed Solution
Describe what the feature does. Incorporate any scout-requirements or scout-feasibility
signals found in Phase 0c.

### Constraints
List at least three constraints: technical, scope, and platform.

### Open Questions
Name at least three open questions or ambiguities. These become the basis for the spec
self-review.

### Self-Review
Identify gaps: which sections need more work, which questions are unresolved, what a
critical reviewer would challenge. Cite at least one specific gap. "No gaps found" fails
this section.

---

## Phase 2 — Business Proposal

Pull from `simulations/scout/scout-feasibility/` before writing. Note which files were used.

Write the proposal. Save to: `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md`

The proposal MUST contain at least three options. Option 1 MUST be named **Do Nothing**.

For each option, write:
- **Description**: What this option entails
- **Pros**: What it gains
- **Cons**: What it costs
- **Risk**: What could go wrong
- **Effort**: Estimated scope

Then write a **Recommendation** section. The recommendation MUST follow this structure:

We chose [chosen option] over **Do Nothing** because [cite the exec or dev inertia cost from
Phase 0 — this is the specific cost that Do Nothing perpetuates]. We chose [chosen option]
over [other rejected option] because [cite the specific trade-off or risk that drove the choice,
traceable to the options analysis above].

A recommendation that compares only non-default options, or defeats Do Nothing only implicitly,
fails C-15. The inertia cost citation must be the exact loss named in Phase 0.

---

## Phase 3 — Executive Pitch

Pull from `simulations/scout/scout-positioning/` before writing. Note which files were used.

Write the pitch. Save to: `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`

The pitch MUST contain four sections:

### Exec Version
Lead with outcomes/ROI. Open with the exec inertia cost from Phase 0 — what the exec
is currently losing. Structure: hook (the loss) → what changes → outcomes/ROI → call to action.

### Dev Version
Lead with the capability. Open with the dev inertia cost from Phase 0 — what friction
currently exists. Structure: hook (the friction) → what you can now do → why it matters
(capability unlocked) → call to action.

### Maker Version
Lead with plain-language workflow. No jargon. Open with the maker inertia cost from Phase 0.
Structure: hook (the blocked step) → what you can now do → why it matters → call to action.
Test: a non-technical user must understand this version without reading the spec.

### Anti-Positioning
What this feature is NOT. Write 3-5 "This is not..." statements. This section is separate
from the three audience versions above.

---

## Completion Check

After writing all three artifacts:

1. Verify spec exists at: `simulations/draft/specs/{{topic}}-spec-{{date}}.md`
2. Verify proposal exists at: `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md`
3. Verify pitch exists at: `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`

If any artifact is missing: write it now. Do not emit a completion summary until all
three files exist on disk. A warning that an artifact is missing is not a substitute
for writing the artifact.

Output a final index: artifact paths, scout signals used (by file), phase 0 inertia
costs (confirm all three were named), and whether the Do Nothing defeat in the
recommendation cited a Phase 0 inertia cost by name.
```

**Rubric targeting**:
- C-01: Three artifacts required, completion check enforces all three exist
- C-02: Six sections required with no-skip rule
- C-03: Three options + Do Nothing + recommendation with rationale
- C-04: Exec/dev/maker versions + anti-positioning section
- C-05: Inertia costs from Phase 0 flow into spec, proposal, pitch — consistency by construction
- C-06: Self-review required with named gap
- C-07: Anti-positioning section required in Phase 3
- C-08: Recommendation trade-off traceable to options analysis
- C-09: Scout pull in 0c, with per-phase targeted pulls in 1-3
- C-10: Exec/dev/maker voices all open with the Phase 0 inertia cost unique to each audience
- C-11: Active write-gate in completion check ("write it now")
- C-12: Phase 0 precedes Phase 1 and establishes voice contracts
- C-13: Phase 1 pulls scout/ broadly; Phase 2 targets scout-feasibility; Phase 3 targets scout-positioning
- C-14: Phase 0 Step 0a requires concrete named loss per audience — completion gated on all three
- C-15: Recommendation template prescribes "over Do Nothing because [Phase 0 inertia cost]" form

**Risk**: The Recommendation template is prescriptive ("must follow this structure") — a model
that partially fills the template but doesn't cite the exact Phase 0 inertia cost may still
pass a lenient scorer. The "exact loss named in Phase 0" requirement needs the scorer to
cross-reference Phase 0 against the recommendation.

---

## V-02 — Axis: Output Format (tabular Do Nothing comparison)

**Hypothesis**: Placing Do Nothing as the FIRST row in a comparison table forces every
subsequent option to be scored against the baseline. The column structure (pros/cons/risk/effort)
makes the Do Nothing cost visible in every row by contrast. The recommendation section then
references specific column values, satisfying C-15 naturally. C-14 is satisfied because the
table's "Audience impact" column requires per-audience framing.

```
Run the campaign-specify skill for: {{topic}}

Produce three artifacts in sequence: spec, proposal, pitch. Execute phases 0-3 in order.
Each phase writes to disk before the next phase begins.

---

## Phase 0 — Audience Foundation

Complete both steps before Phase 1.

**Step 0a — Voice Contracts**

| Audience | Voice contract (one sentence: what they care about most) |
|----------|----------------------------------------------------------|
| Exec | |
| Dev | |
| Maker | |

**Step 0b — Inertia Costs**

For each audience, name the concrete cost of NOT having {{topic}}. Generic descriptions
("would help productivity") do not satisfy this step. Name the specific loss.

| Audience | If {{topic}} does not ship, they lose... |
|----------|-----------------------------------------|
| Exec | [specific revenue exposure, competitive gap, or risk] |
| Dev | [specific workaround or tool-friction] |
| Maker | [specific blocked or degraded workflow step] |

**Step 0c — Scout Pull**

Glob `simulations/scout/**/*.md`. List found files. Carry forward for phases 1-3.

---

## Phase 1 — Technical Spec

Pull from `simulations/scout/` broadly. Note files used.

Save to: `simulations/draft/specs/{{topic}}-spec-{{date}}.md`

Required sections (all six must be present):

**Overview** — What the feature does and why it exists (one paragraph).

**User Problem** — Problem users face today. Reference dev and maker inertia from Phase 0.

**Proposed Solution** — What the feature does. Reference any scout-requirements signals.

**Constraints** — At least three: technical, scope, platform.

**Open Questions** — At least three named ambiguities.

**Self-Review** — Identify at least one gap or section needing more work. "No gaps" fails.

---

## Phase 2 — Business Proposal

Pull from `simulations/scout/scout-feasibility/` before writing. Note files used.

Save to: `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md`

Write a comparison table with **Do Nothing as the first row**. Each row is one option.
Minimum three rows (Do Nothing + two build options).

| Option | Description | Pros | Cons | Risk | Effort | Audience impact |
|--------|-------------|------|------|------|--------|-----------------|
| **Do Nothing** | Status quo — {{topic}} is not built | | | [The cost of inaction — use Phase 0 inertia costs] | None | Exec: [cost] / Dev: [cost] / Maker: [cost] |
| [Option A] | | | | | | |
| [Option B] | | | | | | |

After the table, write the **Recommendation** section:

We recommend [chosen option].

We reject **Do Nothing** because [cite the specific Audience impact cell from the Do Nothing
row above — name which audience cost is most decisive and why it cannot be absorbed].

We prefer [chosen option] over [other build option] because [cite the specific Risk or Cons
difference that drove the trade-off — traceable to the table above].

The recommendation must defeat Do Nothing by name with a specific cost citation. Implicit
defeat ("the other options are better") fails C-15.

---

## Phase 3 — Executive Pitch

Pull from `simulations/scout/scout-positioning/` before writing. Note files used.

Save to: `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`

Write four sections:

**Exec Version** — Lead with outcomes/ROI. Use exec voice from Phase 0. Structure:
[hook: the exec inertia cost] → [what changes] → [business outcome] → [call to action].
Do not open with a tool description.

**Dev Version** — Lead with capability. Use dev voice from Phase 0. Structure:
[hook: the dev inertia cost] → [what you can now do] → [capability unlocked] → [call to action].
Do not open with an outcomes/ROI frame.

**Maker Version** — Lead with workflow in plain language. Use maker voice from Phase 0.
No jargon. Structure: [hook: the blocked step] → [what you can now do] → [why it matters]
→ [call to action]. Test: a non-technical user must understand without reading the spec.

**Anti-Positioning** — What {{topic}} is NOT. Write 3-5 "This is not..." statements.
This section is separate from the three audience versions.

---

## Completion Check

Verify all three files exist:
- `simulations/draft/specs/{{topic}}-spec-{{date}}.md`
- `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md`
- `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`

If any file is missing: write it now. Do not stop until all three files exist.

Final output: list artifact paths, scout signals used, confirm Phase 0 inertia costs
for all three audiences were named, confirm Do Nothing was defeated by name in the
recommendation with a specific cost citation.
```

**Rubric targeting**:
- C-01/C-02/C-03/C-04: Structure enforces all artifacts and their required sections
- C-05: Phase 0 inertia costs flow into proposal Audience impact column and pitch hooks — consistent by table reference
- C-06: Self-review with explicit gap required
- C-07: Anti-positioning as named fourth section in Phase 3
- C-08: Recommendation cites specific table cell (Cons or Risk column) — traceable
- C-09: Three targeted scout pulls
- C-10: Phase 3 opening instructions per version enforce distinct voice register
- C-11: Active write-gate
- C-12: Phase 0 with voice contracts precedes Phase 1
- C-13: Targeted per-phase scout pulls (scout/ → scout-feasibility → scout-positioning)
- C-14: Do Nothing row's "Audience impact" column requires per-audience cost — exec/dev/maker each named
- C-15: Recommendation template: "We reject Do Nothing because [specific Audience impact cell]"

**Risk**: The table format requires the model to populate the "Audience impact" column in the
Do Nothing row with Phase 0 inertia costs. If the model invents new costs rather than
referencing Phase 0, C-05 (consistency) may be strained. The tabular recommendation defeat
("cite the specific Audience impact cell") may produce a cell reference rather than a quoted
cost — the scorer may need to check the cell for specificity.

---

## V-03 — Axis: Lifecycle Emphasis (Phase 0 heavy, phases 1-3 lean)

**Hypothesis**: Allocating 60% of structural weight to Phase 0 forces thoroughness before
any artifact is written. When Phase 0 is expensive (and the model knows it), the outputs
— inertia costs, voice contracts, scout inventory — are used rather than discarded.
Phases 1-3 are directive (what to do) rather than prescriptive (how to structure it),
trusting Phase 0 outputs to carry the content. C-14 is satisfied by Phase 0 depth.
C-15 is satisfied by a compact but explicit defeat template in Phase 2.

```
Run the campaign-specify skill for: {{topic}}

Four phases. Phase 0 is the longest phase — invest here. Phases 1-3 are fast once
Phase 0 is done. Do not begin Phase 1 until Phase 0 is complete.

---

## Phase 0 — Pre-Write Investment (complete before any artifact)

This phase establishes everything the artifacts will need. Rushing Phase 0 produces
hollow artifacts. The time spent here is not overhead — it is the work.

**0a. Scout Inventory**

Search `simulations/scout/**/*.md` for {{topic}}. For each file found:
- File path
- One sentence: what signal this file carries
- Which phase it is most relevant to (spec, proposal, or pitch)

If no scout files exist for {{topic}}: note this and proceed.

**0b. Status Quo Analysis**

Name the current state before {{topic}} exists. Be specific:

- What do users do today instead? (Name the workaround or gap)
- What does the exec measure that {{topic}} would improve? (Name the metric or exposure)
- What does a maker attempt but fail at today? (Name the specific blocked step)
- What does a dev spend time on that {{topic}} would eliminate? (Name the specific friction)

**0c. Inertia Costs (one per audience — concrete and named)**

Using the status quo analysis above, complete each line. Vague answers fail this step.

Exec inertia cost: [What specific revenue, risk, or competitive position is degraded every
day {{topic}} does not exist? State a quantity or specific consequence if possible.]

Dev inertia cost: [What specific workaround does a dev perform today? How long does it take,
or what breaks when they do it?]

Maker inertia cost: [What specific step in a maker's workflow is blocked, missing, or
requires going outside the tool? Name the step.]

**0d. Voice Contracts**

One sentence per audience, grounded in the inertia costs above:

Exec voice: [What the exec wants — framed as: "Stop [inertia cost] by..."]
Dev voice: [What the dev wants — framed as: "Finally [capability unlocked] without [friction]"]
Maker voice: [What the maker wants — in plain language, no jargon, framed as "I can now..."]

**0e. Do Nothing Baseline**

State what happens if {{topic}} is never built:

- Exec absorbs: [the exec inertia cost stated in 0c]
- Dev absorbs: [the dev inertia cost stated in 0c]
- Maker absorbs: [the maker inertia cost stated in 0c]
- Timeline: [by when does this become a significant problem if unaddressed?]

Do Nothing is a real option. Understand its cost before writing a word of the spec.

---

## Phase 1 — Technical Spec

Pull from `simulations/scout/` broadly. Note which files from Phase 0a are used.

Save to: `simulations/draft/specs/{{topic}}-spec-{{date}}.md`

Write the spec using the Phase 0 outputs. Required sections:
- **Overview** (what + why)
- **User Problem** (reference dev/maker inertia from Phase 0c)
- **Proposed Solution** (reference scout signals from Phase 0a)
- **Constraints** (technical, scope, platform — at least three)
- **Open Questions** (at least three — use Phase 0 as source)
- **Self-Review** (one named gap; "no gaps" fails)

---

## Phase 2 — Business Proposal

Pull from `simulations/scout/scout-feasibility/`. Note which files were used.

Save to: `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md`

Options (minimum three, one must be **Do Nothing**):
For each option: description, pros, cons, risk, effort.

Recommendation:
We choose [X] over **Do Nothing** because [cite the Phase 0e Do Nothing baseline — name
which audience cost is decisive]. We choose [X] over [Y] because [name the specific trade-off
from the options analysis].

Do Nothing must be named and defeated by a specific cost. Implicit defeat fails.

---

## Phase 3 — Executive Pitch

Pull from `simulations/scout/scout-positioning/`. Note which files were used.

Save to: `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`

Write four sections using Phase 0d voice contracts as opening anchors:
- **Exec Version**: Phase 0d exec voice → outcomes/ROI → call to action
- **Dev Version**: Phase 0d dev voice → capability unlocked → call to action
- **Maker Version**: Phase 0d maker voice → plain language → call to action
- **Anti-Positioning**: 3-5 "This is not..." statements

Each version must open from a distinct Phase 0d voice contract — not the same frame
reworded. Exec leads with outcomes. Dev leads with capability. Maker leads with workflow.

---

## Completion Check

Verify all three files exist on disk. If any is missing: write it now before stopping.

- `simulations/draft/specs/{{topic}}-spec-{{date}}.md`
- `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md`
- `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`

Final index: paths, scout files used by phase, Phase 0e Do Nothing costs confirmed.
```

**Rubric targeting**:
- C-14: Phase 0c requires three explicit inertia costs with specificity tests ("Vague answers fail")
- C-15: Recommendation template cites Phase 0e Do Nothing baseline — the cost is defined before the proposal is written
- C-10: Phase 0d voice contracts enforced with framing patterns (Exec: "Stop X by...", Dev: "Finally Y without Z", Maker: "I can now...")
- C-12: Phase 0 is a full multi-step phase preceding Phase 1 by design
- C-09/C-13: Phase 0a scout inventory with per-phase routing; phases 1-3 targeted re-queries
- C-11: Active write gate in completion check
- All essential: phases 1-3 directive instructions enforce all required sections

**Risk**: Phase 0 is large — a model that truncates output under context pressure may
produce shallow Phase 0 entries and proceed anyway. The "vague answers fail" language is
advisory rather than structural. The Phase 2 recommendation defeat template references
"Phase 0e Do Nothing baseline" — this cross-reference requires the model to recall the
specific Phase 0e content, which may decay under long context.

---

## V-04 — Combined: Inertia framing + Do Nothing as named falsifiable competitor

**Hypothesis**: Framing Do Nothing as a NAMED COMPETITOR (not just an option) from Phase 0
onward changes the cognitive frame throughout all phases. When Do Nothing is introduced as
a competitor in Phase 0 alongside exec/dev/maker inertia costs, every subsequent phase is
implicitly testing whether the proposed feature defeats this competitor. C-15 becomes
structurally unavoidable — the competitor has been named since Phase 0 and appears in the
proposal recommendation by design. C-14 is satisfied because the competitor framing requires
concrete audience-specific costs to characterize what Do Nothing perpetuates.

```
Run the campaign-specify skill for: {{topic}}

Produce three artifacts: spec, proposal, pitch. Execute four phases in order.
Phase 0 must complete before Phase 1 begins.

---

## Phase 0 — Audience Foundation + Competitor Identification

**0a — Scout Pull**

Glob `simulations/scout/**/*.md`. List files found. Note relevance to spec, proposal, pitch.

**0b — Meet the Competition**

{{topic}} has one competitor that is always present and never goes away: **doing nothing**.
Before writing a word, characterize this competitor honestly.

Do Nothing profile:
- Current state: [What do users actually do today without {{topic}}? Name the workaround.]
- Hidden cost: [What is the accumulated cost of doing nothing? Name it per audience.]
- Good-enough threshold: [Under what conditions does "do nothing" feel acceptable to users?]
- When it breaks: [What triggers would force users off "do nothing" even without this feature?]

**0c — Per-Audience Inertia Costs**

Using the Do Nothing profile above, specify what each audience LOSES if {{topic}} never ships.
Each cost must be concrete and specific to that audience's context.

Exec inertia cost: [Specific business consequence — revenue, risk exposure, competitive gap —
that persists as long as Do Nothing is the default. Quantity or specific scenario preferred.]

Dev inertia cost: [Specific technical friction — workaround, manual step, capability gap —
that persists as long as Do Nothing is the default. Name the friction, not the feeling.]

Maker inertia cost: [Specific workflow block — step that fails, degrades, or requires leaving
the tool — that persists as long as Do Nothing is the default. Name the step.]

**0d — Voice Contracts**

The one sentence each audience cares about, grounded in the costs above:

Exec voice: [outcomes/risk framing]
Dev voice: [capability/friction framing]
Maker voice: [workflow framing, plain language]

---

## Phase 1 — Technical Spec

Pull from `simulations/scout/` broadly. Note files used.

Save to: `simulations/draft/specs/{{topic}}-spec-{{date}}.md`

Six required sections. Do not skip or merge:

### Overview
What the feature does and why it exists. One paragraph.

### User Problem
The problem users face today (the "do nothing" state). Reference dev and maker inertia
costs from Phase 0c as concrete evidence of the problem.

### Proposed Solution
What {{topic}} does. Reference any scout-requirements or scout-feasibility signals found.

### Constraints
At least three: technical, scope, platform.

### Open Questions
At least three named ambiguities. These become self-review fodder.

### Self-Review
At least one named gap. Cite which section needs more work and why.
"No gaps found" fails this section.

---

## Phase 2 — Business Proposal

Pull from `simulations/scout/scout-feasibility/`. Note files used.

Save to: `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md`

**Options** (minimum three — Do Nothing must be Option 1):

For each option: description, pros, cons, risk, effort.

Option 1 is **Do Nothing** — the competitor characterized in Phase 0b. Its "risk" entry
must name the Phase 0c inertia costs: what each audience absorbs by selecting this option.

**Recommendation**:

This section must explicitly defeat Do Nothing by name.

Required structure:
We recommend [chosen option].

**Against Do Nothing**: [chosen option] is worth building because Do Nothing perpetuates
[cite the most decisive Phase 0c inertia cost — name the audience and the specific cost].
This cost is not absorbed; it compounds. [One sentence on why the cost grows or is not stable.]

**Against [other option]**: We prefer [chosen option] over [other option] because
[cite the specific trade-off from the options analysis — traceable to risk or effort above].

A recommendation that defeats Do Nothing only implicitly ("the alternatives are better")
fails. The defeat must name Do Nothing and cite a specific cost.

---

## Phase 3 — Executive Pitch

Pull from `simulations/scout/scout-positioning/`. Note files used.

Save to: `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`

Four sections:

**Exec Version** — Lead with the exec inertia cost from Phase 0c. This is the hook:
what the exec is currently paying. Then: what {{topic}} changes, the business outcome,
the call to action. Do not open with a product description.

**Dev Version** — Lead with the dev inertia cost from Phase 0c. This is the hook:
the friction that exists today. Then: what you can do now, the capability unlocked,
the call to action. Do not open with an outcomes/ROI frame.

**Maker Version** — Lead with the maker inertia cost from Phase 0c. Plain language only.
This is the hook: the step that fails today. Then: what you can do now, why it matters,
the call to action. Test: no jargon, readable without the spec.

**Anti-Positioning** — 3-5 "This is not..." statements. Separate from the three versions above.

Voice differentiation check: Exec opens with business cost, Dev opens with tool friction,
Maker opens with workflow step. If all three open with the same frame, rewrite until distinct.

---

## Completion Check

After all phases:

1. `simulations/draft/specs/{{topic}}-spec-{{date}}.md` — exists? If not: write now.
2. `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md` — exists? If not: write now.
3. `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md` — exists? If not: write now.

Do not emit a completion summary until all three files exist on disk.

Final index: artifact paths, scout files used per phase, Phase 0c inertia costs for
all three audiences, confirmation that the recommendation defeated Do Nothing by name
with a specific cost citation from Phase 0c.
```

**Rubric targeting**:
- C-14: Phase 0c requires three named concrete inertia costs; "quantity or specific scenario preferred" raises the bar
- C-15: Recommendation requires "Against Do Nothing" block with explicit named cost — form prescribed, no implicit defeat
- C-12: Phase 0 with voice contracts, Do Nothing profile, and inertia costs — all before Phase 1
- C-10: Phase 3 opening instructions + voice differentiation check at end
- C-13: Scout pull in 0a + targeted per-phase in Phases 1-3
- C-09: Scout files noted by relevance to spec/proposal/pitch in Phase 0a
- C-11: Active write gate ("write now") per artifact
- All essential: sections enforced in phases 1-3

**Risk**: The "Against Do Nothing" block structure is new and more prescriptive than the
rubric example. If the model produces the block with a vague cost citation ("the inertia
cost from Phase 0c") rather than quoting the specific cost, a strict C-15 scorer may flag it.
The "this cost is not absorbed; it compounds" requirement in the Do Nothing defeat block
adds an explanatory sentence not required by the rubric — could strengthen or over-commit.

---

## V-05 — Combined: All axes (inertia + format + emphasis + targeted scout + completion)

**Hypothesis**: Combining all four high-value axes produces a fully armored variation that
passes all 15 criteria through independent redundant mechanisms. C-14 is satisfied by
Phase 0 loss-first ordering, the tabular inertia cost summary, and the Phase 3 opening
hooks. C-15 is satisfied by the Phase 0e Do Nothing baseline, the proposal table with
Do Nothing as row 1, and the templated defeat language. No single mechanism failure
cascades to a criterion failure.

```
Run the campaign-specify skill for: {{topic}}

Produce three artifacts: spec, proposal, pitch. Execute phases 0-3 in order.
Phase 0 must be complete before Phase 1 begins. Each phase writes to disk.

---

## Phase 0 — Pre-Write Foundation (complete in full before Phase 1)

**Step 0a — Scout Inventory**

Glob `simulations/scout/**/*.md` for {{topic}}. For each file found, record:
- File path
- Signal summary (one sentence)
- Phase it serves (spec / proposal / pitch)

If no files found: record "no scout signals — proceeding without."

**Step 0b — Status Quo (Do Nothing profile)**

Name the current state. Specificity required — generic descriptions fail this step.

| Dimension | Current state without {{topic}} |
|-----------|----------------------------------|
| What users do instead | [Name the workaround or manual process] |
| Exec exposure | [The business metric or risk that is currently unmanaged] |
| Dev friction | [The specific repetitive or error-prone step devs do today] |
| Maker block | [The specific workflow step that fails or is absent] |
| Stability of Do Nothing | [Will this remain acceptable or does it worsen over time?] |

**Step 0c — Per-Audience Inertia Costs (required)**

For each audience, name the concrete specific cost of Do Nothing. Vague answers fail.

| Audience | If {{topic}} never ships, they absorb... |
|----------|------------------------------------------|
| Exec | [Revenue exposure, competitive gap, or risk — quantified or scenario-specific] |
| Dev | [Named workaround or capability gap — how long or how often?] |
| Maker | [Named blocked workflow step — what exactly fails or is missing?] |

**Step 0d — Voice Contracts**

One sentence per audience, grounded in Step 0c costs:

| Audience | Voice contract |
|----------|----------------|
| Exec | [Outcomes/risk frame — "By [date/event], if we do not..."] |
| Dev | [Capability frame — "I can finally... without..."] |
| Maker | [Workflow frame — plain language, "I can now..."] |

**Step 0e — Do Nothing Baseline**

Summarize the Do Nothing option before proposal writing begins. This row appears first
in the proposal table:

Do Nothing = status quo absorbs: Exec: [Step 0c exec cost] / Dev: [Step 0c dev cost] /
Maker: [Step 0c maker cost]. Timeline: [stable or worsening — from Step 0b].

---

## Phase 1 — Technical Spec

Pull from `simulations/scout/` broadly. Reference Step 0a file list; note which were used.

Save to: `simulations/draft/specs/{{topic}}-spec-{{date}}.md`

All six sections required:

**Overview** — What the feature does and why it exists (one paragraph).

**User Problem** — The problem today. Open with or reference the dev and maker inertia
costs from Step 0c — these are the evidence of the problem, not invented examples.

**Proposed Solution** — What {{topic}} does. Incorporate any scout-requirements or
scout-feasibility signals from Step 0a.

**Constraints** — At least three (technical, scope, platform).

**Open Questions** — At least three named ambiguities.

**Self-Review** — At least one named gap. "No gaps found" fails.

---

## Phase 2 — Business Proposal

Pull from `simulations/scout/scout-feasibility/`. Note files used.

Save to: `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md`

Options table (minimum three rows — **Do Nothing must be row 1**):

| Option | Description | Pros | Cons | Risk | Effort | Audience impact |
|--------|-------------|------|------|------|--------|-----------------|
| **Do Nothing** | Status quo | [benefits of inaction] | [Step 0e costs] | [Step 0b stability] | None | Exec: [Step 0c exec] / Dev: [Step 0c dev] / Maker: [Step 0c maker] |
| [Option A] | | | | | | |
| [Option B] | | | | | | |

**Recommendation**:

We recommend [chosen option].

**Defeating Do Nothing**: We reject Do Nothing because [cite the specific Audience impact
cell from the Do Nothing row — name which audience's cost is most decisive and why it cannot
continue to be absorbed]. Do Nothing is not stable: [cite Step 0b stability assessment].

**Defeating [other option]**: We prefer [chosen option] over [other option] because [cite
the specific Risk or Effort difference traceable to the table above — not a preference statement].

Defeat of Do Nothing must be explicit, named, and cite a specific cost from the options table.

---

## Phase 3 — Executive Pitch

Pull from `simulations/scout/scout-positioning/`. Note files used.

Save to: `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`

Four sections:

**Exec Version**
Open with Step 0c exec inertia cost. Do not open with a product description.
Structure: [exec cost hook] → [what changes] → [business outcome/ROI] → [call to action].

**Dev Version**
Open with Step 0c dev inertia cost. Do not open with an outcomes/ROI frame.
Structure: [friction hook] → [what you can now do] → [capability unlocked] → [call to action].

**Maker Version**
Open with Step 0c maker inertia cost. Plain language. No jargon.
Structure: [blocked step hook] → [what you can now do] → [why it matters] → [call to action].
Test: readable without the spec by a non-technical user.

**Anti-Positioning**
3-5 "This is not..." statements. Separate from the three versions above.

Voice differentiation check before saving: confirm exec opens with business cost, dev opens
with tool friction, maker opens with workflow step. If two versions use the same opening frame,
rewrite until distinct.

---

## Completion Check

After all phases, verify:

| Artifact | Path | Exists? |
|----------|------|---------|
| Spec | `simulations/draft/specs/{{topic}}-spec-{{date}}.md` | |
| Proposal | `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md` | |
| Pitch | `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md` | |

For any row where "Exists?" is No: write the artifact now. Do not emit a completion
summary until all three rows show Yes. A missing artifact is not a completion state.

Final index output:
1. Artifact paths (all three)
2. Scout files used per phase (from Step 0a routing)
3. Phase 0c inertia costs confirmed (all three audiences named)
4. Do Nothing defeat confirmed: named, with specific cost citation from the proposal table
5. Voice differentiation confirmed: distinct opening frame per audience version
```

**Rubric targeting**:
- C-01: Three artifacts + tabular completion check with active write gate
- C-02: Six sections, all named, no-skip rule
- C-03: Three options, Do Nothing as row 1, options table format
- C-04: Exec/dev/maker versions + anti-positioning section
- C-05: Step 0c flows into spec (User Problem), proposal (Do Nothing row), and pitch (hooks) — consistent by reference
- C-06: Self-review with named gap required
- C-07: Anti-positioning as explicit named section
- C-08: "Defeating [other option]" cites specific Risk/Effort column — traceable to table
- C-09: Three targeted scout pulls with file tracking from Step 0a
- C-10: Opening frame per version prescribed + voice differentiation check at end
- C-11: Tabular completion check with "write now" gate per row
- C-12: Phase 0 (five steps) precedes Phase 1 with full voice contracts
- C-13: Step 0a → Phase 1 (scout/ broad) → Phase 2 (scout-feasibility) → Phase 3 (scout-positioning)
- C-14: Step 0c table requires per-audience costs with specificity requirement; reflected in proposal Do Nothing row and pitch opening hooks
- C-15: Recommendation "Defeating Do Nothing" block names Do Nothing explicitly, cites Audience impact cell, adds stability argument from Step 0b

**Risk**: This variation is the most complex and most likely to produce a long output.
Under context pressure, a model may truncate Phase 0 steps or produce shallow table cells.
The Step 0b table has five dimensions — the "Stability of Do Nothing" row may produce
weak answers that undermine the C-15 stability argument. The final index (5 items) is
more elaborate than prior completion checks and requires the model to cross-reference
multiple Phase 0 outputs — possible decay on long context runs.

---

## Variation Summary

| ID | Primary Axis | C-14 Mechanism | C-15 Mechanism | Predicted Score | Risk |
|----|--------------|----------------|----------------|-----------------|------|
| V-01 | Inertia framing | Phase 0 Step 0a loss-first; completion gated | Recommendation template: "over Do Nothing because [Phase 0 inertia cost]" | 97-100 | Cross-reference decay under long context |
| V-02 | Output format (tabular) | Do Nothing row Audience impact column per audience | Recommendation template: "We reject Do Nothing because [specific cell]" | 97-100 | Model may invent rather than reference Phase 0 in table cells |
| V-03 | Lifecycle emphasis | Phase 0c with specificity test + Phase 0e Do Nothing baseline | Phase 2 compact defeat template citing Phase 0e | 90-97 | Phase 0 is advisory-gated; model may truncate and proceed |
| V-04 | Inertia + falsifiability | Phase 0c with quantity/scenario preference; Phase 3 hooks | "Against Do Nothing" block — named defeat with specific cost + stability sentence | 97-100 | "This cost compounds" requirement adds non-rubric sentence; over-commitment risk |
| V-05 | All combined | Step 0c table + proposal Do Nothing row + pitch opening hooks | "Defeating Do Nothing" block + tabular cell citation + Step 0b stability | 100 | Complexity/length risk; Step 0b Stability row may weaken; 5-item final index may decay |

**Predicted leaderboard**: V-05 >= V-04 >= V-01 = V-02 > V-03

V-05 has the most redundant C-14/C-15 mechanisms — a single mechanism failure doesn't
cascade. V-04 introduces the competitor-framing novelty which produces the strongest
C-15 language but adds a non-rubric sentence. V-01 and V-02 are simpler with fewer
moving parts — lower risk of context decay on C-14/C-15 cross-references. V-03 relies
on Phase 0 depth but lacks the structural enforcement of V-01/V-02's completion gates.
