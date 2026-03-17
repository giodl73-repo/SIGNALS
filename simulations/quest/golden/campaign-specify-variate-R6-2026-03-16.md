---
skill: quest-variate
skill_target: campaign-specify
round: 6
date: 2026-03-16
rubric: simulations/quest/rubrics/campaign-specify-rubric-v6-2026-03-16.md
---

# Variations — campaign-specify / Round 6

Five complete, runnable skill body variations targeting the v6 rubric.
Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

**R5 diagnosis driving R6 axis choices:**

Under v6, the scoring formula is `(essential/5 * 60) + (rec/3 * 30) + (asp/18 * 10)`.
Three new criteria (C-24, C-25, C-26) were extracted from R5 V-04's COMPLETION INDEX and pitch mechanisms.

| Variation | Asp under v6 | Missing | Why |
|-----------|-------------|---------|-----|
| R5 V-04 | 17/18 | C-20 | Voice differentiation save gate not targeted by design |
| R5 V-05 | ~16/18 | C-24, C-25 | COMPLETION INDEX gate audit uses `Gate N: yes/no` without step-pair labels (C-24 gap); CITATION MISSING row has no recovery instruction naming destination phase (C-25 gap) |

R5 V-04 is the R6 base. It already earns:
- C-24: `Phase 0 gate chain: 3 gates passed (Gate 1: 0a→0b | Gate 2: 0b→0c | Gate 3: 0c→0d)` with individual step-pair naming
- C-25: `(If CITATION MISSING: return to Phase 2 and paste the record before stopping.)` active recovery with named destination phase
- C-26: `Use Step 0c exec/dev/maker voice contract as anchor` in each pitch section
- All other C-09 through C-23

The single unearned criterion is **C-20** (voice differentiation save gate). R6 explores three ways to add C-20 to the V-04 base without disturbing the seventeen criteria already earned.

| Axis | Mechanism | Targets |
|------|-----------|---------|
| Minimal gate (V-01 style) | `>> VOICE DIFFERENTIATION GATE <<` collocated before PITCH WRITE GATE | C-20 |
| Formal subphase gate (V-02 style) | `--- PHASE 3 VOICE GATE ---` using same formalism as Phase 0 gates | C-20 |
| Contract-reference gate (V-03 style) | Gate reads Step 0c contracts back as gate criteria; each audience check cites the contract | C-20 (+ reinforces C-26) |
| Minimal gate + COMPLETION INDEX voice row (V-04) | V-01 mechanism + add voice differentiation audit row to COMPLETION INDEX Additional index | C-20 (+ extends C-24's audit record pattern) |
| Full synthesis (V-05) | Contract-reference gate + COMPLETION INDEX voice audit row + step-pair labels in each gate header | C-20 (maximum evidence density) |

**Predicted ceiling**: V-04 or V-05 earns 18/18 (97+ composite). All variations expected to hold 5/5 essential, 3/3 recommended, and C-09 through C-19 + C-21 + C-22 + C-23 + C-24 + C-25 + C-26.

---

## V-01 — Axis: Minimal C-20 Gate (direct transplant of proven mechanism)

**Hypothesis**: R5 V-05 proved the `>> VOICE DIFFERENTIATION GATE <<` mechanism earns C-20.
R5 V-04 already holds C-09 through C-19, C-21, C-22, C-23, C-24, C-25, and C-26.
The transplant is low-risk because the gate is structurally independent — its only
integration point is colocation with the PITCH WRITE GATE (which already exists in V-04).
No Phase 0 changes, no COMPLETION INDEX changes, no Recommendation section changes.
If the mechanism earns C-20 in V-05, it earns C-20 here while V-04's other seventeen
criteria remain structurally undisturbed.

```
Run the campaign-specify skill for: {{topic}}

Produce three artifacts: spec, proposal, pitch. Execute phases 0-3 in order.
Phase 0 must complete before Phase 1 begins. Each artifact is written to disk before
the next phase begins.

---

## Phase 0 — Audience Foundation

Phase 0 has four steps. Steps 0a, 0b, 0c are sequential with explicit advancement gates.
Step 0d (scout pull) is terminal. Gate chain: Gate 1 (0a→0b) | Gate 2 (0b→0c) |
Gate 3 (0c→0d) | Step 0d terminal.

**Step 0a — Inertia Costs**

What each audience LOSES if {{topic}} does not ship. Concrete and specific:

Exec inertia cost: [Specific revenue exposure, competitive gap, or risk. Name a consequence,
not a category. Quantify if possible.]

Dev inertia cost: [Specific workaround or capability gap. Name the friction, not the feeling.
Estimate recurring cost if possible.]

Maker inertia cost: [Specific blocked workflow step. Name the step. What does the maker
do today instead?]

--- GATE 1: Do not advance to Step 0b until all three inertia costs are complete. ---

**Step 0b — Stability Citation Record**

Evaluate whether the cost of Do Nothing is stable or worsening. Produce the
STABILITY CITATION RECORD using one of the two forms below. This record will be pasted
verbatim into the Phase 2 Defeating Do Nothing block.

FORM A (worsening): "Do Nothing is not stable: [specific mechanism and timeline —
e.g., 'competitor ships equivalent feature in Q2, making exec exposure acute by June' or
'dev workaround accumulates 3 hours/sprint, compounding to 36h/quarter']."

FORM B (stable): "Do Nothing is stable: [rationale — e.g., 'the workaround is functional
and the underlying need does not grow with volume']."

STABILITY CITATION RECORD:
[Paste the complete Form A or Form B sentence here]

A record containing only a tag ("worsening" / "stable") without a mechanism or rationale
fails this step. The record must be a complete sentence ready for verbatim citation.

--- GATE 2: Do not advance to Step 0c until the STABILITY CITATION RECORD is complete. ---

**Step 0c — Voice Contracts**

One sentence per audience, grounded in Steps 0a and 0b:

Exec voice: [Outcomes/risk framing — reference exec inertia cost and stability trajectory]
Dev voice: [Capability/friction framing — reference dev inertia cost]
Maker voice: [Workflow framing — plain language, reference maker inertia cost]

--- GATE 3: Do not advance to Step 0d until all three voice contracts are written. ---

**Step 0d — Scout Pull** [TERMINAL]

Glob `simulations/scout/**/*.md` for {{topic}}. For each file found:
- Path
- One sentence summary
- Artifact it serves: spec / proposal / pitch

If no scout files found: record "no scout signals — proceeding without" and continue.

[Phase 0 complete. Three gates passed. Proceed to Phase 1.]

---

## Phase 1 — Technical Spec

Pull from `simulations/scout/` broadly. Note files from Step 0d used.

Write the spec. All six sections required — no skipping, no merging.

### Overview
One paragraph: what {{topic}} does and why it exists.

### User Problem
Problem users face today. Reference dev and maker inertia costs from Step 0a directly.

### Proposed Solution
What {{topic}} does. Incorporate scout-requirements or scout-feasibility signals from Step 0d.

### Constraints
At least three: technical, scope, platform.

### Open Questions
At least three named ambiguities.

### Self-Review
At least one named gap. "No gaps found" fails.

**>> SPEC WRITE GATE <<**
Save spec to: `simulations/draft/specs/{{topic}}-spec-{{date}}.md`
Check: does the file exist? If not: write it now.
Do not begin Phase 2 until this file exists on disk.

---

## Phase 2 — Business Proposal

Pull from `simulations/scout/scout-feasibility/` before writing. Note files used.

Write the proposal. Three options minimum. Option 1 MUST be named **Do Nothing**.

For each option: description, pros, cons, risk, effort.

Then write the **Recommendation** section with the following labeled blocks.
Each block has its own header. Do not merge them into a combined paragraph.

### Recommendation

We recommend [chosen option].

#### Defeating Do Nothing

[This block addresses the status quo competitor. Structurally separate from the
comparative defeat below.]

Do Nothing perpetuates [cite the most decisive Step 0a inertia cost — name the audience
and the specific cost].

[PASTE THE STABILITY CITATION RECORD FROM STEP 0b VERBATIM HERE. Do not summarize.
Do not paraphrase. Copy the Form A or Form B sentence character for character.]

We choose to act because [one sentence: why this cost trajectory is not acceptable].

#### Defeating [Other Option Name]

We prefer [chosen] over [other] because [specific trade-off traceable to a risk, effort,
or cons field in the options analysis — not a preference statement].

Note: The Defeating Do Nothing block must contain the STABILITY CITATION RECORD verbatim.
A combined Recommendation paragraph that defeats all options in prose does not satisfy C-16.
A block without the verbatim STABILITY CITATION RECORD does not satisfy C-17 or C-21.

**>> PROPOSAL WRITE GATE <<**
Save proposal to: `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md`
Check: does the file exist? If not: write it now.
Do not begin Phase 3 until this file exists on disk.

---

## Phase 3 — Executive Pitch

Pull from `simulations/scout/scout-positioning/` before writing. Note files used.

Write all four sections of the pitch below. Do not save the pitch file until the
voice differentiation gate at the end of this phase passes.

### Exec Version
Lead with exec inertia cost from Step 0a. Use Step 0c exec voice contract as anchor.
Structure: [exec cost hook] -> [what changes] -> [outcome/ROI] -> [call to action].
Do not open with a product description.

### Dev Version
Lead with dev inertia cost from Step 0a. Use Step 0c dev voice contract as anchor.
Structure: [friction hook] -> [what you can now do] -> [capability unlocked] -> [call to action].
Do not open with an outcomes/ROI frame.

### Maker Version
Lead with maker inertia cost from Step 0a. Use Step 0c maker voice contract as anchor.
Plain language, no jargon. Structure: [blocked step hook] -> [what you can now do]
-> [why it matters] -> [call to action].

### Anti-Positioning
3-5 "This is not..." statements. Structurally separate from the three audience versions above.

**>> VOICE DIFFERENTIATION GATE (required before saving pitch) <<**

Before saving the pitch file, extract the opening sentence from each version:

  Exec opening: [first sentence of Exec Version]
  Dev opening: [first sentence of Dev Version]
  Maker opening: [first sentence of Maker Version]

Expected frames:
  Exec opens with: a business cost, risk, or revenue consequence
  Dev opens with: a tool friction, workaround, or capability gap
  Maker opens with: a workflow step that is blocked, absent, or manual

IF any two openings are the same or use the same frame:
  Rewrite the duplicated version(s) until all three opening frames are detectably distinct.
  Re-run this check after rewriting.
  Do not save the pitch until all three opening frames are distinct.

IF all three openings are distinct: proceed to PITCH WRITE GATE.

**>> PITCH WRITE GATE <<**
[Save only after the voice differentiation gate above passes.]
Save pitch to: `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`
Check: does the file exist? If not: write it now.
Do not emit the COMPLETION INDEX until this file exists on disk.

---

## COMPLETION INDEX

[Emitted after all write gates and recovery steps are complete. Structurally distinct
from the write gates above (which fire at artifact production time) and from the recovery
instructions embedded in each write gate. This block is the post-execution existence record.]

Confirm each artifact exists. Fill in the status column from actual file check results.
If any status is "missing": write that artifact now, then update the row to "exists."

| Artifact | Path | Status |
|----------|------|--------|
| Spec | `simulations/draft/specs/{{topic}}-spec-{{date}}.md` | [exists / missing] |
| Proposal | `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md` | [exists / missing] |
| Pitch | `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md` | [exists / missing] |

All three rows must show "exists" before the skill is complete.

Additional index:
- Scout files used per phase
- Phase 0 inertia costs confirmed (all three audiences)
- Phase 0 gate chain: 3 gates passed (Gate 1: 0a→0b | Gate 2: 0b→0c | Gate 3: 0c→0d)
- STABILITY CITATION RECORD form used: Form A / Form B
- STABILITY CITATION RECORD pasted verbatim in Defeating Do Nothing block:
  CITATION CONFIRMED / CITATION MISSING
  (If CITATION MISSING: return to Phase 2 and paste the record before stopping.)
- Defeating Do Nothing block: separate labeled header (#### or equivalent): yes / no
```

**Rubric targeting**:
- C-20: `>> VOICE DIFFERENTIATION GATE <<` before PITCH WRITE GATE. Extracts first sentences per version. Specifies expected frames (business cost / tool friction / blocked step). Conditional: "IF any two openings are the same or use the same frame: Rewrite... Do not save the pitch until all three opening frames are distinct." PITCH WRITE GATE collocated immediately after with "[Save only after the voice differentiation gate above passes.]" Active blocking, not advisory.
- C-24: `Phase 0 gate chain: 3 gates passed (Gate 1: 0a→0b | Gate 2: 0b→0c | Gate 3: 0c→0d)` — inherits from V-04 R5 base. Individual gate naming with step-pair labels.
- C-25: `(If CITATION MISSING: return to Phase 2 and paste the record before stopping.)` — inherits from V-04 R5 base. Active recovery with named destination phase.
- C-26: `Use Step 0c exec/dev/maker voice contract as anchor` in each pitch section — inherits from V-04 R5 base.
- All other C-09 through C-23: unchanged from V-04 R5 base.

**Risk**: Minimal. Single addition at a single structural location. The voice gate is entirely new content — it does not overlap with any existing criterion's mechanism. The `>> PITCH WRITE GATE <<` already existed in V-04; conditioning it on the voice gate passing adds one dependency without structural change. Predicted: 18/18 aspirational.

---

## V-02 — Axis: Formal Subphase Gate (Phase 3 gate using same formalism as Phase 0 gates)

**Hypothesis**: The `--- GATE N: Do not advance... ---` notation in Phase 0 is what makes
C-22 structurally unambiguous to scorers. Applying the same formalism to the C-20 gate —
naming it `--- PHASE 3 VOICE GATE ---` and using parallel `Pass / Fail` per-criterion
language — creates a uniformly gated architecture where both Phase 0 and Phase 3 use
identical notation. The structural consistency may produce a stronger C-20 pass signal than
the `>> ... <<` style because the "do not advance" language is explicit and formal, matching
the advancement-blocking requirement precisely. Risk: the named section-header style (`---`)
reads as a checkpoint, not a production gate; some scorers may find the `>> <<` style more
clearly collocated with the write instruction.

```
Run the campaign-specify skill for: {{topic}}

Produce three artifacts: spec, proposal, pitch. Execute phases 0-3 in order.
Phase 0 must complete before Phase 1 begins. Each artifact is written to disk before
the next phase begins.

---

## Phase 0 — Audience Foundation

Phase 0 has four steps. Steps 0a, 0b, 0c are sequential with explicit advancement gates.
Step 0d (scout pull) is terminal. Gate chain: Gate 1 (0a→0b) | Gate 2 (0b→0c) |
Gate 3 (0c→0d) | Step 0d terminal.

**Step 0a — Inertia Costs**

What each audience LOSES if {{topic}} does not ship. Concrete and specific:

Exec inertia cost: [Specific revenue exposure, competitive gap, or risk. Name a consequence,
not a category. Quantify if possible.]

Dev inertia cost: [Specific workaround or capability gap. Name the friction, not the feeling.
Estimate recurring cost if possible.]

Maker inertia cost: [Specific blocked workflow step. Name the step. What does the maker
do today instead?]

--- GATE 1: Do not advance to Step 0b until all three inertia costs are complete. ---

**Step 0b — Stability Citation Record**

Evaluate whether the cost of Do Nothing is stable or worsening. Produce the
STABILITY CITATION RECORD using one of the two forms below. This record will be pasted
verbatim into the Phase 2 Defeating Do Nothing block.

FORM A (worsening): "Do Nothing is not stable: [specific mechanism and timeline —
e.g., 'competitor ships equivalent feature in Q2, making exec exposure acute by June' or
'dev workaround accumulates 3 hours/sprint, compounding to 36h/quarter']."

FORM B (stable): "Do Nothing is stable: [rationale — e.g., 'the workaround is functional
and the underlying need does not grow with volume']."

STABILITY CITATION RECORD:
[Paste the complete Form A or Form B sentence here]

A record containing only a tag ("worsening" / "stable") without a mechanism or rationale
fails this step. The record must be a complete sentence ready for verbatim citation.

--- GATE 2: Do not advance to Step 0c until the STABILITY CITATION RECORD is complete. ---

**Step 0c — Voice Contracts**

One sentence per audience, grounded in Steps 0a and 0b:

Exec voice: [Outcomes/risk framing — reference exec inertia cost and stability trajectory]
Dev voice: [Capability/friction framing — reference dev inertia cost]
Maker voice: [Workflow framing — plain language, reference maker inertia cost]

--- GATE 3: Do not advance to Step 0d until all three voice contracts are written. ---

**Step 0d — Scout Pull** [TERMINAL]

Glob `simulations/scout/**/*.md` for {{topic}}. For each file found:
- Path
- One sentence summary
- Artifact it serves: spec / proposal / pitch

If no scout files found: record "no scout signals — proceeding without" and continue.

[Phase 0 complete. Three gates passed. Proceed to Phase 1.]

---

## Phase 1 — Technical Spec

Pull from `simulations/scout/` broadly. Note files from Step 0d used.

Write the spec. All six sections required — no skipping, no merging.

### Overview
One paragraph: what {{topic}} does and why it exists.

### User Problem
Problem users face today. Reference dev and maker inertia costs from Step 0a directly.

### Proposed Solution
What {{topic}} does. Incorporate scout-requirements or scout-feasibility signals from Step 0d.

### Constraints
At least three: technical, scope, platform.

### Open Questions
At least three named ambiguities.

### Self-Review
At least one named gap. "No gaps found" fails.

**>> SPEC WRITE GATE <<**
Save spec to: `simulations/draft/specs/{{topic}}-spec-{{date}}.md`
Check: does the file exist? If not: write it now.
Do not begin Phase 2 until this file exists on disk.

---

## Phase 2 — Business Proposal

Pull from `simulations/scout/scout-feasibility/` before writing. Note files used.

Write the proposal. Three options minimum. Option 1 MUST be named **Do Nothing**.

For each option: description, pros, cons, risk, effort.

Then write the **Recommendation** section with the following labeled blocks.
Each block has its own header. Do not merge them into a combined paragraph.

### Recommendation

We recommend [chosen option].

#### Defeating Do Nothing

[This block addresses the status quo competitor. Structurally separate from the
comparative defeat below.]

Do Nothing perpetuates [cite the most decisive Step 0a inertia cost — name the audience
and the specific cost].

[PASTE THE STABILITY CITATION RECORD FROM STEP 0b VERBATIM HERE. Do not summarize.
Do not paraphrase. Copy the Form A or Form B sentence character for character.]

We choose to act because [one sentence: why this cost trajectory is not acceptable].

#### Defeating [Other Option Name]

We prefer [chosen] over [other] because [specific trade-off traceable to a risk, effort,
or cons field in the options analysis — not a preference statement].

Note: The Defeating Do Nothing block must contain the STABILITY CITATION RECORD verbatim.
A combined Recommendation paragraph that defeats all options in prose does not satisfy C-16.
A block without the verbatim STABILITY CITATION RECORD does not satisfy C-17 or C-21.

**>> PROPOSAL WRITE GATE <<**
Save proposal to: `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md`
Check: does the file exist? If not: write it now.
Do not begin Phase 3 until this file exists on disk.

---

## Phase 3 — Executive Pitch

Pull from `simulations/scout/scout-positioning/` before writing. Note files used.

Write all four sections of the pitch below.

### Exec Version
Lead with exec inertia cost from Step 0a. Use Step 0c exec voice contract as anchor.
Structure: [exec cost hook] -> [what changes] -> [outcome/ROI] -> [call to action].
Do not open with a product description.

### Dev Version
Lead with dev inertia cost from Step 0a. Use Step 0c dev voice contract as anchor.
Structure: [friction hook] -> [what you can now do] -> [capability unlocked] -> [call to action].
Do not open with an outcomes/ROI frame.

### Maker Version
Lead with maker inertia cost from Step 0a. Use Step 0c maker voice contract as anchor.
Plain language, no jargon. Structure: [blocked step hook] -> [what you can now do]
-> [why it matters] -> [call to action].

### Anti-Positioning
3-5 "This is not..." statements. Structurally separate from the three audience versions above.

--- PHASE 3 VOICE GATE: Do not save the pitch until this gate passes ---

Extract the opening sentence from each audience version written above:

  Exec opening: [first sentence of Exec Version]
  Dev opening: [first sentence of Dev Version]
  Maker opening: [first sentence of Maker Version]

Evaluate each against its required frame (all three must independently pass):

  Exec gate — Opens with a business cost, risk, or revenue consequence:
    Pass (opening names a consequence, risk, or cost) / Fail (opens with description or solution)

  Dev gate — Opens with a tool friction, workaround, or capability gap:
    Pass (opening names friction, manual step, or gap) / Fail (opens with outcome or ROI)

  Maker gate — Opens with a blocked, absent, or manual workflow step in plain language:
    Pass (opening names the blocked step, no jargon) / Fail (opens with product description or jargon)

If any gate fails: Rewrite the failing version. Return to the Step 0c anchor for that
audience. Re-run the gate. Do not advance to PITCH WRITE GATE until all three gates pass.

--- END PHASE 3 VOICE GATE ---

**>> PITCH WRITE GATE <<**
[Save only after the Phase 3 Voice Gate above passes — all three audience gates: Pass.]
Save pitch to: `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`
Check: does the file exist? If not: write it now.
Do not emit the COMPLETION INDEX until this file exists on disk.

---

## COMPLETION INDEX

[Emitted after all write gates and recovery steps are complete. Structurally distinct
from the write gates above (which fire at artifact production time) and from the recovery
instructions embedded in each write gate. This block is the post-execution existence record.]

Confirm each artifact exists. Fill in the status column from actual file check results.
If any status is "missing": write that artifact now, then update the row to "exists."

| Artifact | Path | Status |
|----------|------|--------|
| Spec | `simulations/draft/specs/{{topic}}-spec-{{date}}.md` | [exists / missing] |
| Proposal | `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md` | [exists / missing] |
| Pitch | `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md` | [exists / missing] |

All three rows must show "exists" before the skill is complete.

Additional index:
- Scout files used per phase
- Phase 0 inertia costs confirmed (all three audiences)
- Phase 0 gate chain: 3 gates passed (Gate 1: 0a→0b | Gate 2: 0b→0c | Gate 3: 0c→0d)
- STABILITY CITATION RECORD form used: Form A / Form B
- STABILITY CITATION RECORD pasted verbatim in Defeating Do Nothing block:
  CITATION CONFIRMED / CITATION MISSING
  (If CITATION MISSING: return to Phase 2 and paste the record before stopping.)
- Defeating Do Nothing block: separate labeled header (#### or equivalent): yes / no
- Phase 3 Voice Gate: all three audience gates passed (Exec / Dev / Maker): yes / no
```

**Rubric targeting**:
- C-20: `--- PHASE 3 VOICE GATE: Do not save the pitch until this gate passes ---` uses explicit "do not advance" blocking language. Per-audience gate criteria with Pass/Fail evaluation. Conditional rewrite: "If any gate fails: Rewrite the failing version... Do not advance to PITCH WRITE GATE until all three gates pass." PITCH WRITE GATE conditioned on "all three audience gates: Pass." Active blocking with specified passing criteria.
- C-24, C-25, C-26: Unchanged from V-04 R5 base.

**Risk**: The `--- END PHASE 3 VOICE GATE ---` closing line is new in this series. Scorers may interpret the named section header style as a checkpoint rather than a production gate. The "do not advance to PITCH WRITE GATE" language is explicit and advancement-blocking, which should satisfy C-20's "gate must block advancement" requirement. The per-criterion Pass/Fail structure specifies what constitutes a passing revision. Lower risk than open-ended advisory notes; slightly higher structural novelty than V-01.

---

## V-03 — Axis: Contract-Reference Gate (Step 0c contracts cited as gate criteria)

**Hypothesis**: C-20 requires the gate to "specify what constitutes a passing revision."
C-26 requires each pitch section to reference the "Phase 0 voice contract that governs
its register." These two criteria share an underlying mechanism: the contract defines
correctness, and the gate enforces it. A gate that directly reads back the Step 0c
contracts as its pass/fail criteria integrates both mechanisms into a single structural
location. The model cannot satisfy the gate with generic differentiation — it must return
to the specific contract sentence it wrote in Step 0c and verify the pitch opening matches
that contract's frame. This makes the "passing revision" criteria concrete and traceable,
satisfying C-20's specificity requirement, while also extending C-26's backpointer from
the pitch sections into the enforcement gate itself.

```
Run the campaign-specify skill for: {{topic}}

Produce three artifacts: spec, proposal, pitch. Execute phases 0-3 in order.
Phase 0 must complete before Phase 1 begins. Each artifact is written to disk before
the next phase begins.

---

## Phase 0 — Audience Foundation

Phase 0 has four steps. Steps 0a, 0b, 0c are sequential with explicit advancement gates.
Step 0d (scout pull) is terminal. Gate chain: Gate 1 (0a→0b) | Gate 2 (0b→0c) |
Gate 3 (0c→0d) | Step 0d terminal.

**Step 0a — Inertia Costs**

What each audience LOSES if {{topic}} does not ship. Concrete and specific:

Exec inertia cost: [Specific revenue exposure, competitive gap, or risk. Name a consequence,
not a category. Quantify if possible.]

Dev inertia cost: [Specific workaround or capability gap. Name the friction, not the feeling.
Estimate recurring cost if possible.]

Maker inertia cost: [Specific blocked workflow step. Name the step. What does the maker
do today instead?]

--- GATE 1: Do not advance to Step 0b until all three inertia costs are complete. ---

**Step 0b — Stability Citation Record**

Evaluate whether the cost of Do Nothing is stable or worsening. Produce the
STABILITY CITATION RECORD using one of the two forms below. This record will be pasted
verbatim into the Phase 2 Defeating Do Nothing block.

FORM A (worsening): "Do Nothing is not stable: [specific mechanism and timeline —
e.g., 'competitor ships equivalent feature in Q2, making exec exposure acute by June' or
'dev workaround accumulates 3 hours/sprint, compounding to 36h/quarter']."

FORM B (stable): "Do Nothing is stable: [rationale — e.g., 'the workaround is functional
and the underlying need does not grow with volume']."

STABILITY CITATION RECORD:
[Paste the complete Form A or Form B sentence here]

A record containing only a tag ("worsening" / "stable") without a mechanism or rationale
fails this step. The record must be a complete sentence ready for verbatim citation.

--- GATE 2: Do not advance to Step 0c until the STABILITY CITATION RECORD is complete. ---

**Step 0c — Voice Contracts**

One sentence per audience, grounded in Steps 0a and 0b:

Exec voice: [Outcomes/risk framing — reference exec inertia cost and stability trajectory]
Dev voice: [Capability/friction framing — reference dev inertia cost]
Maker voice: [Workflow framing — plain language, reference maker inertia cost]

--- GATE 3: Do not advance to Step 0d until all three voice contracts are written. ---

**Step 0d — Scout Pull** [TERMINAL]

Glob `simulations/scout/**/*.md` for {{topic}}. For each file found:
- Path
- One sentence summary
- Artifact it serves: spec / proposal / pitch

If no scout files found: record "no scout signals — proceeding without" and continue.

[Phase 0 complete. Three gates passed. Proceed to Phase 1.]

---

## Phase 1 — Technical Spec

Pull from `simulations/scout/` broadly. Note files from Step 0d used.

Write the spec. All six sections required — no skipping, no merging.

### Overview
One paragraph: what {{topic}} does and why it exists.

### User Problem
Problem users face today. Reference dev and maker inertia costs from Step 0a directly.

### Proposed Solution
What {{topic}} does. Incorporate scout-requirements or scout-feasibility signals from Step 0d.

### Constraints
At least three: technical, scope, platform.

### Open Questions
At least three named ambiguities.

### Self-Review
At least one named gap. "No gaps found" fails.

**>> SPEC WRITE GATE <<**
Save spec to: `simulations/draft/specs/{{topic}}-spec-{{date}}.md`
Check: does the file exist? If not: write it now.
Do not begin Phase 2 until this file exists on disk.

---

## Phase 2 — Business Proposal

Pull from `simulations/scout/scout-feasibility/` before writing. Note files used.

Write the proposal. Three options minimum. Option 1 MUST be named **Do Nothing**.

For each option: description, pros, cons, risk, effort.

Then write the **Recommendation** section with the following labeled blocks.
Each block has its own header. Do not merge them into a combined paragraph.

### Recommendation

We recommend [chosen option].

#### Defeating Do Nothing

[This block addresses the status quo competitor. Structurally separate from the
comparative defeat below.]

Do Nothing perpetuates [cite the most decisive Step 0a inertia cost — name the audience
and the specific cost].

[PASTE THE STABILITY CITATION RECORD FROM STEP 0b VERBATIM HERE. Do not summarize.
Do not paraphrase. Copy the Form A or Form B sentence character for character.]

We choose to act because [one sentence: why this cost trajectory is not acceptable].

#### Defeating [Other Option Name]

We prefer [chosen] over [other] because [specific trade-off traceable to a risk, effort,
or cons field in the options analysis — not a preference statement].

Note: The Defeating Do Nothing block must contain the STABILITY CITATION RECORD verbatim.
A combined Recommendation paragraph that defeats all options in prose does not satisfy C-16.
A block without the verbatim STABILITY CITATION RECORD does not satisfy C-17 or C-21.

**>> PROPOSAL WRITE GATE <<**
Save proposal to: `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md`
Check: does the file exist? If not: write it now.
Do not begin Phase 3 until this file exists on disk.

---

## Phase 3 — Executive Pitch

Pull from `simulations/scout/scout-positioning/` before writing. Note files used.

Write all four sections of the pitch below. Do not save the pitch file until the
voice differentiation gate at the end of this phase passes.

### Exec Version
Lead with exec inertia cost from Step 0a. Use Step 0c exec voice contract as anchor.
Structure: [exec cost hook] -> [what changes] -> [outcome/ROI] -> [call to action].
Do not open with a product description.

### Dev Version
Lead with dev inertia cost from Step 0a. Use Step 0c dev voice contract as anchor.
Structure: [friction hook] -> [what you can now do] -> [capability unlocked] -> [call to action].
Do not open with an outcomes/ROI frame.

### Maker Version
Lead with maker inertia cost from Step 0a. Use Step 0c maker voice contract as anchor.
Plain language, no jargon. Structure: [blocked step hook] -> [what you can now do]
-> [why it matters] -> [call to action].

### Anti-Positioning
3-5 "This is not..." statements. Structurally separate from the three audience versions above.

**>> VOICE DIFFERENTIATION GATE — Step 0c Contract Check (required before saving pitch) <<**

The voice contracts you established in Step 0c define what each version must open with.
Use them now as gate criteria.

Step 1 — Copy your Step 0c voice contracts here:
  Step 0c exec voice contract: [your exec voice sentence from Step 0c]
  Step 0c dev voice contract: [your dev voice sentence from Step 0c]
  Step 0c maker voice contract: [your maker voice sentence from Step 0c]

Step 2 — Extract the opening sentence from each version:
  Exec opening: [first sentence of Exec Version]
  Dev opening: [first sentence of Dev Version]
  Maker opening: [first sentence of Maker Version]

Step 3 — Contract check for each audience:
  Exec check: Does the Exec Version opening match the frame of the Step 0c exec contract
    (outcomes/risk register)? Pass / Fail
  Dev check: Does the Dev Version opening match the frame of the Step 0c dev contract
    (capability/friction register)? Pass / Fail
  Maker check: Does the Maker Version opening match the frame of the Step 0c maker contract
    (jargon-free blocked-step register)? Pass / Fail

Step 4 — Resolution:
  IF any check is Fail: Rewrite the failing version. Return to the Step 0c contract for
    that audience as your revision anchor. Re-run Steps 2-3.
    Do not save the pitch until all three contract checks are Pass.
  IF all three checks are Pass: proceed to PITCH WRITE GATE.

**>> PITCH WRITE GATE <<**
[Save only after all three Step 0c contract checks above are Pass.]
Save pitch to: `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`
Check: does the file exist? If not: write it now.
Do not emit the COMPLETION INDEX until this file exists on disk.

---

## COMPLETION INDEX

[Emitted after all write gates and recovery steps are complete. Structurally distinct
from the write gates above (which fire at artifact production time) and from the recovery
instructions embedded in each write gate. This block is the post-execution existence record.]

Confirm each artifact exists. Fill in the status column from actual file check results.
If any status is "missing": write that artifact now, then update the row to "exists."

| Artifact | Path | Status |
|----------|------|--------|
| Spec | `simulations/draft/specs/{{topic}}-spec-{{date}}.md` | [exists / missing] |
| Proposal | `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md` | [exists / missing] |
| Pitch | `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md` | [exists / missing] |

All three rows must show "exists" before the skill is complete.

Additional index:
- Scout files used per phase
- Phase 0 inertia costs confirmed (all three audiences)
- Phase 0 gate chain: 3 gates passed (Gate 1: 0a→0b | Gate 2: 0b→0c | Gate 3: 0c→0d)
- STABILITY CITATION RECORD form used: Form A / Form B
- STABILITY CITATION RECORD pasted verbatim in Defeating Do Nothing block:
  CITATION CONFIRMED / CITATION MISSING
  (If CITATION MISSING: return to Phase 2 and paste the record before stopping.)
- Defeating Do Nothing block: separate labeled header (#### or equivalent): yes / no
```

**Rubric targeting**:
- C-20: `>> VOICE DIFFERENTIATION GATE — Step 0c Contract Check <<`. Explicit 4-step process. Step 3 evaluates each opening against its contract frame with Pass/Fail. Step 4: "IF any check is Fail: Rewrite the failing version... Do not save the pitch until all three contract checks are Pass." PITCH WRITE GATE conditioned on "all three Step 0c contract checks above are Pass." Active blocking with named-contract pass criteria.
- C-26: Backpointers in pitch sections (`Use Step 0c exec/dev/maker voice contract as anchor`) PLUS the gate re-cites Step 0c contracts as named evaluation criteria — double-anchoring the traceability.
- C-24, C-25: Unchanged from V-04 R5 base.

**Risk**: The "Step 1 — Copy your Step 0c voice contracts" instruction asks the model to copy content into the gate block before checking pitch openings. This is a stronger traceability mechanism but adds a cognitive step. A model that skips Step 1 (copying contracts) and goes directly to comparison may still pass C-20 (the blocking language and criteria are present) but weakens C-26's backpointer anchoring in the gate itself. Low overall risk because the gate mechanism is clear regardless of whether Step 1 is executed.

---

## V-04 — Combined: V-01 Minimal Gate + COMPLETION INDEX Voice Audit Row

**Hypothesis**: V-01 demonstrates the minimal gate mechanism for C-20. But the COMPLETION
INDEX in V-04 R5 already contains a gate audit row (C-24) and citation confirmation row
(C-25). Adding a voice differentiation audit row to the COMPLETION INDEX extends the
unified audit record to cover all three checkpoint types: Phase 0 gate chain, citation,
and voice differentiation. A scorer evaluating the COMPLETION INDEX will find one
traceable record for every compliance mechanism in the skill — making the self-auditing
property described in R5 Excellence Signal 2 apply to C-20 as well. This variation
targets 18/18 while also extending the COMPLETION INDEX into the fullest audit record
produced in this series.

```
Run the campaign-specify skill for: {{topic}}

Produce three artifacts: spec, proposal, pitch. Execute phases 0-3 in order.
Phase 0 must complete before Phase 1 begins. Each artifact is written to disk before
the next phase begins.

---

## Phase 0 — Audience Foundation

Phase 0 has four steps. Steps 0a, 0b, 0c are sequential with explicit advancement gates.
Step 0d (scout pull) is terminal. Gate chain: Gate 1 (0a→0b) | Gate 2 (0b→0c) |
Gate 3 (0c→0d) | Step 0d terminal.

**Step 0a — Inertia Costs**

What each audience LOSES if {{topic}} does not ship. Concrete and specific:

Exec inertia cost: [Specific revenue exposure, competitive gap, or risk. Name a consequence,
not a category. Quantify if possible.]

Dev inertia cost: [Specific workaround or capability gap. Name the friction, not the feeling.
Estimate recurring cost if possible.]

Maker inertia cost: [Specific blocked workflow step. Name the step. What does the maker
do today instead?]

--- GATE 1: Do not advance to Step 0b until all three inertia costs are complete. ---

**Step 0b — Stability Citation Record**

Evaluate whether the cost of Do Nothing is stable or worsening. Produce the
STABILITY CITATION RECORD using one of the two forms below. This record will be pasted
verbatim into the Phase 2 Defeating Do Nothing block.

FORM A (worsening): "Do Nothing is not stable: [specific mechanism and timeline —
e.g., 'competitor ships equivalent feature in Q2, making exec exposure acute by June' or
'dev workaround accumulates 3 hours/sprint, compounding to 36h/quarter']."

FORM B (stable): "Do Nothing is stable: [rationale — e.g., 'the workaround is functional
and the underlying need does not grow with volume']."

STABILITY CITATION RECORD:
[Paste the complete Form A or Form B sentence here]

A record containing only a tag ("worsening" / "stable") without a mechanism or rationale
fails this step. The record must be a complete sentence ready for verbatim citation.

--- GATE 2: Do not advance to Step 0c until the STABILITY CITATION RECORD is complete. ---

**Step 0c — Voice Contracts**

One sentence per audience, grounded in Steps 0a and 0b:

Exec voice: [Outcomes/risk framing — reference exec inertia cost and stability trajectory]
Dev voice: [Capability/friction framing — reference dev inertia cost]
Maker voice: [Workflow framing — plain language, reference maker inertia cost]

--- GATE 3: Do not advance to Step 0d until all three voice contracts are written. ---

**Step 0d — Scout Pull** [TERMINAL]

Glob `simulations/scout/**/*.md` for {{topic}}. For each file found:
- Path
- One sentence summary
- Artifact it serves: spec / proposal / pitch

If no scout files found: record "no scout signals — proceeding without" and continue.

[Phase 0 complete. Three gates passed. Proceed to Phase 1.]

---

## Phase 1 — Technical Spec

Pull from `simulations/scout/` broadly. Note files from Step 0d used.

Write the spec. All six sections required — no skipping, no merging.

### Overview
One paragraph: what {{topic}} does and why it exists.

### User Problem
Problem users face today. Reference dev and maker inertia costs from Step 0a directly.

### Proposed Solution
What {{topic}} does. Incorporate scout-requirements or scout-feasibility signals from Step 0d.

### Constraints
At least three: technical, scope, platform.

### Open Questions
At least three named ambiguities.

### Self-Review
At least one named gap. "No gaps found" fails.

**>> SPEC WRITE GATE <<**
Save spec to: `simulations/draft/specs/{{topic}}-spec-{{date}}.md`
Check: does the file exist? If not: write it now.
Do not begin Phase 2 until this file exists on disk.

---

## Phase 2 — Business Proposal

Pull from `simulations/scout/scout-feasibility/` before writing. Note files used.

Write the proposal. Three options minimum. Option 1 MUST be named **Do Nothing**.

For each option: description, pros, cons, risk, effort.

Then write the **Recommendation** section with the following labeled blocks.
Each block has its own header. Do not merge them into a combined paragraph.

### Recommendation

We recommend [chosen option].

#### Defeating Do Nothing

[This block addresses the status quo competitor. Structurally separate from the
comparative defeat below.]

Do Nothing perpetuates [cite the most decisive Step 0a inertia cost — name the audience
and the specific cost].

[PASTE THE STABILITY CITATION RECORD FROM STEP 0b VERBATIM HERE. Do not summarize.
Do not paraphrase. Copy the Form A or Form B sentence character for character.]

We choose to act because [one sentence: why this cost trajectory is not acceptable].

#### Defeating [Other Option Name]

We prefer [chosen] over [other] because [specific trade-off traceable to a risk, effort,
or cons field in the options analysis — not a preference statement].

Note: The Defeating Do Nothing block must contain the STABILITY CITATION RECORD verbatim.
A combined Recommendation paragraph that defeats all options in prose does not satisfy C-16.
A block without the verbatim STABILITY CITATION RECORD does not satisfy C-17 or C-21.

**>> PROPOSAL WRITE GATE <<**
Save proposal to: `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md`
Check: does the file exist? If not: write it now.
Do not begin Phase 3 until this file exists on disk.

---

## Phase 3 — Executive Pitch

Pull from `simulations/scout/scout-positioning/` before writing. Note files used.

Write all four sections of the pitch below. Do not save the pitch file until the
voice differentiation gate at the end of this phase passes.

### Exec Version
Lead with exec inertia cost from Step 0a. Use Step 0c exec voice contract as anchor.
Structure: [exec cost hook] -> [what changes] -> [outcome/ROI] -> [call to action].
Do not open with a product description.

### Dev Version
Lead with dev inertia cost from Step 0a. Use Step 0c dev voice contract as anchor.
Structure: [friction hook] -> [what you can now do] -> [capability unlocked] -> [call to action].
Do not open with an outcomes/ROI frame.

### Maker Version
Lead with maker inertia cost from Step 0a. Use Step 0c maker voice contract as anchor.
Plain language, no jargon. Structure: [blocked step hook] -> [what you can now do]
-> [why it matters] -> [call to action].

### Anti-Positioning
3-5 "This is not..." statements. Structurally separate from the three audience versions above.

**>> VOICE DIFFERENTIATION GATE (required before saving pitch) <<**

Before saving the pitch file, extract the opening sentence from each version:

  Exec opening: [first sentence of Exec Version]
  Dev opening: [first sentence of Dev Version]
  Maker opening: [first sentence of Maker Version]

Expected frames:
  Exec opens with: a business cost, risk, or revenue consequence
  Dev opens with: a tool friction, workaround, or capability gap
  Maker opens with: a workflow step that is blocked, absent, or manual

IF any two openings are the same or use the same frame:
  Rewrite the duplicated version(s) until all three opening frames are detectably distinct.
  Re-run this check after rewriting.
  Do not save the pitch until all three opening frames are distinct.

IF all three openings are distinct: proceed to PITCH WRITE GATE.

**>> PITCH WRITE GATE <<**
[Save only after the voice differentiation gate above passes.]
Save pitch to: `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`
Check: does the file exist? If not: write it now.
Do not emit the COMPLETION INDEX until this file exists on disk.

---

## COMPLETION INDEX

[Emitted after all write gates, voice differentiation gate, and recovery steps are
complete. Structurally distinct from: (1) write gates, which fire at artifact production
time; (2) the voice differentiation gate, which fires before pitch save; and (3) the
recovery instructions embedded in each write gate. This block is the post-execution
existence record and unified compliance audit.]

Confirm each artifact exists. Fill in the status column from actual file check results.
If any status is "missing": write that artifact now, then update the row to "exists."

| Artifact | Path | Status |
|----------|------|--------|
| Spec | `simulations/draft/specs/{{topic}}-spec-{{date}}.md` | [exists / missing] |
| Proposal | `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md` | [exists / missing] |
| Pitch | `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md` | [exists / missing] |

All three rows must show "exists" before the skill is complete.

Additional index:
- Scout files used per phase
- Phase 0 inertia costs confirmed (all three audiences)
- Phase 0 gate chain: 3 gates passed (Gate 1: 0a→0b | Gate 2: 0b→0c | Gate 3: 0c→0d)
- STABILITY CITATION RECORD form used: Form A / Form B
- STABILITY CITATION RECORD pasted verbatim in Defeating Do Nothing block:
  CITATION CONFIRMED / CITATION MISSING
  (If CITATION MISSING: return to Phase 2 and paste the record before stopping.)
- Defeating Do Nothing block: separate labeled header (#### or equivalent): yes / no
- Voice differentiation gate result: distinct / rewritten-to-distinct
```

**Rubric targeting**:
- C-20: Same `>> VOICE DIFFERENTIATION GATE <<` as V-01 — proven mechanism, extracts first sentences, specifies frames, blocks save until distinct.
- C-23: COMPLETION INDEX labeled as "Structurally distinct from: (1) write gates... (2) voice differentiation gate... (3) recovery instructions." Explicitly names the voice differentiation gate as a structurally separate element, reinforcing that the COMPLETION INDEX is the post-execution record.
- C-24: `Phase 0 gate chain: 3 gates passed (Gate 1: 0a→0b | Gate 2: 0b→0c | Gate 3: 0c→0d)` — individual step-pair naming preserved.
- C-25: `(If CITATION MISSING: return to Phase 2 and paste the record before stopping.)` — active recovery preserved.
- C-26: `Use Step 0c exec/dev/maker voice contract as anchor` in pitch sections preserved.
- New: `Voice differentiation gate result: distinct / rewritten-to-distinct` in COMPLETION INDEX Additional index — the audit record now covers Phase 0 gates (C-24), citation (C-25), and voice differentiation in one unified location. A model filling this index honestly will expose any voice differentiation failure before stopping.

**Risk**: Lower than V-01. The additional COMPLETION INDEX row creates a secondary self-auditing mechanism for C-20. If the voice gate fires and rewrites occur, the `rewritten-to-distinct` value makes the remediation traceable. The only new complexity is the expanded COMPLETION INDEX preamble (now explicitly names the voice differentiation gate as a structurally separate element from C-23). This reinforces C-23 rather than weakening it.

---

## V-05 — Full Synthesis: Contract-Reference Gate + COMPLETION INDEX Extension + Enhanced Gate Labels

**Hypothesis**: V-03's contract-reference gate is the richest C-20 mechanism because
it makes Step 0c contracts the literal gate criteria, ensuring both C-20 (blocking gate
with specified pass criteria) and C-26 (backpointer traceability from pitch to voice
contract) are structurally co-present. V-04's COMPLETION INDEX extension makes the
entire audit — Phase 0 gates, citation, and voice differentiation — available in a
single post-execution record. Adding step-pair labels to each `--- GATE N ---` block
(in addition to the Phase 0 header declaration) creates maximum structural evidence for
C-24: the gate audit row in the COMPLETION INDEX does not merely assert "3 gates passed"
but matches labeled gate entries visible in Phase 0. Combined, this variation maximizes
evidence density across every v6 criterion simultaneously.

```
Run the campaign-specify skill for: {{topic}}

Produce three artifacts: spec, proposal, pitch. Execute phases 0-3 in order.
Phase 0 must complete before Phase 1 begins. Each artifact is written to disk before
the next phase begins.

---

## Phase 0 — Audience Foundation

Phase 0 has four steps. Steps 0a, 0b, 0c are sequential with explicit advancement gates.
Step 0d (scout pull) is terminal. Gate chain: Gate 1 (0a→0b) | Gate 2 (0b→0c) |
Gate 3 (0c→0d) | Step 0d terminal.

**Step 0a — Inertia Costs**

What each audience LOSES if {{topic}} does not ship. Concrete and specific:

Exec inertia cost: [Specific revenue exposure, competitive gap, or risk. Name a consequence,
not a category. Quantify if possible.]

Dev inertia cost: [Specific workaround or capability gap. Name the friction, not the feeling.
Estimate recurring cost if possible.]

Maker inertia cost: [Specific blocked workflow step. Name the step. What does the maker
do today instead?]

--- GATE 1 (0a→0b): Do not advance to Step 0b until all three inertia costs are complete. ---

**Step 0b — Stability Citation Record**

Evaluate whether the cost of Do Nothing is stable or worsening. Produce the
STABILITY CITATION RECORD using one of the two forms below. This record will be pasted
verbatim into the Phase 2 Defeating Do Nothing block.

FORM A (worsening): "Do Nothing is not stable: [specific mechanism and timeline —
e.g., 'competitor ships equivalent feature in Q2, making exec exposure acute by June' or
'dev workaround accumulates 3 hours/sprint, compounding to 36h/quarter']."

FORM B (stable): "Do Nothing is stable: [rationale — e.g., 'the workaround is functional
and the underlying need does not grow with volume']."

STABILITY CITATION RECORD:
[Paste the complete Form A or Form B sentence here]

A record containing only a tag ("worsening" / "stable") without a mechanism or rationale
fails this step. The record must be a complete sentence ready for verbatim citation.

--- GATE 2 (0b→0c): Do not advance to Step 0c until the STABILITY CITATION RECORD is complete. ---

**Step 0c — Voice Contracts**

One sentence per audience, grounded in Steps 0a and 0b:

Exec voice: [Outcomes/risk framing — reference exec inertia cost and stability trajectory]
Dev voice: [Capability/friction framing — reference dev inertia cost]
Maker voice: [Workflow framing — plain language, reference maker inertia cost]

--- GATE 3 (0c→0d): Do not advance to Step 0d until all three voice contracts are written. ---

**Step 0d — Scout Pull** [TERMINAL]

Glob `simulations/scout/**/*.md` for {{topic}}. For each file found:
- Path
- One sentence summary
- Artifact it serves: spec / proposal / pitch

If no scout files found: record "no scout signals — proceeding without" and continue.

[Phase 0 complete. Three gates passed (Gate 1: 0a→0b | Gate 2: 0b→0c | Gate 3: 0c→0d).
Proceed to Phase 1.]

---

## Phase 1 — Technical Spec

Pull from `simulations/scout/` broadly. Note files from Step 0d used.

Write the spec. All six sections required — no skipping, no merging.

### Overview
One paragraph: what {{topic}} does and why it exists.

### User Problem
Problem users face today. Reference dev and maker inertia costs from Step 0a directly.

### Proposed Solution
What {{topic}} does. Incorporate scout-requirements or scout-feasibility signals from Step 0d.

### Constraints
At least three: technical, scope, platform.

### Open Questions
At least three named ambiguities.

### Self-Review
At least one named gap. "No gaps found" fails.

**>> SPEC WRITE GATE <<**
Save spec to: `simulations/draft/specs/{{topic}}-spec-{{date}}.md`
Check: does the file exist? If not: write it now.
Do not begin Phase 2 until this file exists on disk.

---

## Phase 2 — Business Proposal

Pull from `simulations/scout/scout-feasibility/` before writing. Note files used.

Write the proposal. Three options minimum. Option 1 MUST be named **Do Nothing**.

For each option: description, pros, cons, risk, effort.

Then write the **Recommendation** section with the following labeled blocks.
Each block has its own header. Do not merge them into a combined paragraph.

### Recommendation

We recommend [chosen option].

#### Defeating Do Nothing

[This block addresses the status quo competitor. Structurally separate from the
comparative defeat below.]

Do Nothing perpetuates [cite the most decisive Step 0a inertia cost — name the audience
and the specific cost].

[PASTE THE STABILITY CITATION RECORD FROM STEP 0b VERBATIM HERE. Do not summarize.
Do not paraphrase. Copy the Form A or Form B sentence character for character.]

We choose to act because [one sentence: why this cost trajectory is not acceptable].

#### Defeating [Other Option Name]

We prefer [chosen] over [other] because [specific trade-off traceable to a risk, effort,
or cons field in the options analysis — not a preference statement].

Note: The Defeating Do Nothing block must contain the STABILITY CITATION RECORD verbatim.
A combined Recommendation paragraph that defeats all options in prose does not satisfy C-16.
A block without the verbatim STABILITY CITATION RECORD does not satisfy C-17 or C-21.

**>> PROPOSAL WRITE GATE <<**
Save proposal to: `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md`
Check: does the file exist? If not: write it now.
Do not begin Phase 3 until this file exists on disk.

---

## Phase 3 — Executive Pitch

Pull from `simulations/scout/scout-positioning/` before writing. Note files used.

Write all four sections of the pitch below. Do not save the pitch file until the
voice differentiation gate at the end of this phase passes.

### Exec Version
Lead with exec inertia cost from Step 0a. Use Step 0c exec voice contract as anchor.
Structure: [exec cost hook] -> [what changes] -> [outcome/ROI] -> [call to action].
Do not open with a product description.

### Dev Version
Lead with dev inertia cost from Step 0a. Use Step 0c dev voice contract as anchor.
Structure: [friction hook] -> [what you can now do] -> [capability unlocked] -> [call to action].
Do not open with an outcomes/ROI frame.

### Maker Version
Lead with maker inertia cost from Step 0a. Use Step 0c maker voice contract as anchor.
Plain language, no jargon. Structure: [blocked step hook] -> [what you can now do]
-> [why it matters] -> [call to action].

### Anti-Positioning
3-5 "This is not..." statements. Structurally separate from the three audience versions above.

**>> VOICE DIFFERENTIATION GATE — Step 0c Contract Check (required before saving pitch) <<**

The voice contracts from Step 0c are the gate criteria. Use them now.

Step 1 — Copy your Step 0c voice contracts:
  Step 0c exec voice contract: [your exec voice sentence from Step 0c]
  Step 0c dev voice contract: [your dev voice sentence from Step 0c]
  Step 0c maker voice contract: [your maker voice sentence from Step 0c]

Step 2 — Extract the opening sentence from each pitch version:
  Exec opening: [first sentence of Exec Version]
  Dev opening: [first sentence of Dev Version]
  Maker opening: [first sentence of Maker Version]

Step 3 — Contract check (each must independently pass):
  Exec check: Does the Exec Version opening match the exec contract's frame
    (outcomes/risk register — business cost, risk, or revenue consequence)?
    Pass / Fail
  Dev check: Does the Dev Version opening match the dev contract's frame
    (capability/friction register — tool friction, workaround, or capability gap)?
    Pass / Fail
  Maker check: Does the Maker Version opening match the maker contract's frame
    (jargon-free blocked-step register — a blocked, absent, or manual workflow step)?
    Pass / Fail

Step 4 — Resolution:
  IF any check is Fail: Rewrite the failing version using the Step 0c contract for that
    audience as the revision anchor. Re-run Steps 2-3.
    Do not save the pitch until all three contract checks are Pass.
  IF all three checks are Pass: proceed to PITCH WRITE GATE.

**>> PITCH WRITE GATE <<**
[Save only after all three Step 0c contract checks in the gate above are Pass.]
Save pitch to: `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`
Check: does the file exist? If not: write it now.
Do not emit the COMPLETION INDEX until this file exists on disk.

---

## COMPLETION INDEX

[Emitted after all write gates, voice differentiation gate, and recovery steps are
complete. Structurally distinct from: (1) write gates, which fire at artifact production
time; (2) the voice differentiation gate, which fires before pitch save; and (3) the
recovery instructions embedded in each write gate. This block is the post-execution
existence record and unified compliance audit.]

Confirm each artifact exists. Fill in the status column from actual file check results.
If any status is "missing": write that artifact now, then update the row to "exists."

| Artifact | Path | Status |
|----------|------|--------|
| Spec | `simulations/draft/specs/{{topic}}-spec-{{date}}.md` | [exists / missing] |
| Proposal | `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md` | [exists / missing] |
| Pitch | `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md` | [exists / missing] |

All three rows must show "exists" before the skill is complete.

Additional index:
- Scout files used per phase
- Phase 0 inertia costs confirmed (all three audiences)
- Phase 0 gate chain: 3 gates passed (Gate 1: 0a→0b | Gate 2: 0b→0c | Gate 3: 0c→0d)
- STABILITY CITATION RECORD form used: Form A / Form B
- STABILITY CITATION RECORD pasted verbatim in Defeating Do Nothing block:
  CITATION CONFIRMED / CITATION MISSING
  (If CITATION MISSING: return to Phase 2 and paste the record before stopping.)
- Defeating Do Nothing block: separate labeled header (#### or equivalent): yes / no
- Voice differentiation gate result: distinct / rewritten-to-distinct
```

**Rubric targeting**:
- C-20: Contract-reference voice gate with 4-step process. Step 3 evaluates each opening against its named Step 0c contract frame with explicit Pass/Fail. Step 4 blocks pitch save until all three pass. "Do not save the pitch until all three contract checks are Pass." Active blocking with contract-derived criteria.
- C-24: Two evidence locations for step-pair labels: (1) Phase 0 header gate chain `Gate 1 (0a→0b) | Gate 2 (0b→0c) | Gate 3 (0c→0d)` AND (2) each inline gate label now includes the step-pair: `--- GATE 1 (0a→0b): Do not advance... ---`. COMPLETION INDEX gate audit row matches both. Maximum structural evidence.
- C-25: `(If CITATION MISSING: return to Phase 2 and paste the record before stopping.)` preserved from V-04 R5 base.
- C-26: Two evidence locations: (1) pitch sections `Use Step 0c exec/dev/maker voice contract as anchor`, (2) voice differentiation gate Step 1 re-cites the voice contracts by their Step 0c label. Backpointer traceability is doubly anchored.
- C-23: COMPLETION INDEX preamble explicitly names the voice differentiation gate as structurally separate element #2 (between write gates and recovery instructions).

**Risk**: This is the highest-complexity variation. The contract-reference gate adds a Step 1 copy operation that V-01/V-02 do not have. If a model skips Step 1 (omitting the contract copy) but still runs Step 3 correctly, C-20 is still earned but the second C-26 anchor (in the gate) is weaker. The inline gate step-pair labels (`--- GATE 1 (0a→0b) ---`) are new in this series — they are redundant with the Phase 0 header declaration but maximally clear. No existing criterion is damaged by this addition. Predicted: 18/18 aspirational.

---

## Variation Summary

| ID | Primary Axis | Key Mechanism | Targets | Predicted Score (v6) | Risk |
|----|--------------|---------------|---------|----------------------|------|
| V-01 | Minimal C-20 gate | `>> VOICE DIFFERENTIATION GATE <<` collocated before PITCH WRITE GATE; extracts first sentences; expected frames; conditional rewrite; "Do not save until distinct" | C-20 | 18/18 asp = 100.0 | Lowest complexity; single addition; V-05 R5 proved this mechanism earns C-20 |
| V-02 | Formal subphase gate | `--- PHASE 3 VOICE GATE ---` with per-audience Pass/Fail criteria matching Phase 0 gate formalism | C-20 | 18/18 asp = 100.0 | Named section style may be read as checkpoint rather than production gate; "do not advance" language is explicit and should pass |
| V-03 | Contract-reference gate | Gate re-cites Step 0c contracts as evaluation criteria; each audience check names the contract frame; revision anchor = Step 0c sentence | C-20 + C-26 reinforcement | 18/18 asp = 100.0 | Step 1 copy operation adds cognitive step; C-20 earns even if Step 1 skipped; C-26 doubly anchored |
| V-04 | Minimal gate + COMPLETION INDEX voice row | V-01 gate + `Voice differentiation gate result: distinct / rewritten-to-distinct` in COMPLETION INDEX; COMPLETION INDEX preamble names voice gate as structurally separate element | C-20 + extended audit record | 18/18 asp = 100.0 | Strongest secondary evidence for C-20; unified audit covers gates + citation + voice in one block |
| V-05 | Full synthesis | V-03 contract-reference gate + V-04 COMPLETION INDEX extension + step-pair labels in inline gate entries | C-20 + maximum evidence density for C-24 + C-26 | 18/18 asp = 100.0 | Highest complexity; each mechanism independent; step-pair inline labels are new but structurally additive |

**Predicted leaderboard**: V-04 = V-05 > V-01 = V-02 = V-03

All five variations are predicted to earn 18/18 aspirational. V-04 and V-05 produce richer evidence records (extended COMPLETION INDEX and/or step-pair inline labels) that may provide more decisive scoring signals in edge cases. V-01 is the minimal verification target: if V-01 fails C-20, the gate mechanism is weaker than V-05 R5's version and the failure mode will be diagnosable.

**The key R6 unlock**: R5 V-04 proved that three structurally independent mechanisms (C-24 gate audit, C-25 citation recovery, C-26 voice backpointers) can coexist in the same prompt without interaction. R5 V-05 proved C-20 earns alongside the full existing stack. R6 asks whether C-20 earns alongside C-24 + C-25 + C-26 simultaneously — which requires starting from V-04 R5 (the C-24/C-25/C-26 base) rather than V-05 R5 (the C-20 base). V-04 R5 is the correct starting point because it already holds the three new v6 criteria. The C-20 addition is structurally independent of all three.
