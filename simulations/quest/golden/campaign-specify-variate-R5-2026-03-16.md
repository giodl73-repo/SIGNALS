---
skill: quest-variate
skill_target: campaign-specify
round: 5
date: 2026-03-16
rubric: simulations/quest/rubrics/campaign-specify-rubric-v5-2026-03-16.md
---

# Variations — campaign-specify / Round 5

Five complete, runnable skill body variations targeting the v5 rubric.
Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

**R4 diagnosis driving R5 axis choices:**

| New Criterion | R4 Status | Gap | R5 Target |
|---------------|-----------|-----|-----------|
| C-21 (canonical Form A/B + Completion Check citation confirm) | V-01 only | Phase 0 must produce a named Form A or Form B sentence; Phase 2 cites verbatim; Completion Check confirms citation occurred | Preserve mechanism; single-axis V-01 hardens citation lock |
| C-22 (full intra-Phase 0 gate chain) | V-01 only | Every adjacent step-to-step transition gated, not just "at least one" (upgrades C-18) | V-01 earns with 2 gates covering 3-step chain; R5 single-axis V-02 makes explicit for any Phase 0 length |
| C-23 (named Completion Index with existence status) | V-02 only | Post-execution block listing all three artifacts + paths + confirmed existence status per artifact; distinct from write gates and recovery check | New axis V-03 |

R4 V-01 earned C-21 + C-22 but missed C-19, C-20, C-23 (no inline write gates, no voice gate, no existence-status Completion Index).
R4 V-02 earned C-23 but missed C-21, C-22 (one-word stability tag instead of Form A/B sentence; no verbatim citation form).
No R4 variation earns C-21, C-22, C-23 simultaneously while also holding C-19 and C-20.
R4 V-05 earned all 12 v4 aspirational criteria; under v5 it likely earns C-21 + C-22 but misses C-23 (Completion Index table shows paths but has no per-artifact "[exists / missing]" status column).

R5 target ceiling: one variation earns C-19 + C-20 + C-21 + C-22 + C-23 simultaneously.

| Axis | Mechanism | Targets |
|------|-----------|---------|
| Citation lock | Step 0b emits a named STABILITY CITATION RECORD (Form A or Form B); Phase 2 pastes it by name; Completion Check confirms citation | C-21 |
| Explicit full gate chain | Phase 0 explicitly numbers its gates; every consecutive step pair has a blocking gate; terminal step is labeled | C-22 |
| Existence-status Completion Index | Named block with a three-row table: artifact | path | [exists / missing]; recovery instruction if status is missing; structurally separate from write gates | C-23 |
| C-21 + C-22 + C-23 combined | Citation lock + explicit full gate chain + existence-status Completion Index on an R4 V-04 base (already holding C-16, C-17, C-18, C-19) | C-21, C-22, C-23 |
| Full synthesis | All five unearned criteria: C-19 + C-20 + C-21 + C-22 + C-23 on R4 V-05 base | C-19, C-20, C-21, C-22, C-23 |

---

## V-01 — Axis: Citation Lock (C-21 target)

**Hypothesis**: R4 V-01 earns C-21 because Step 0b produces a complete Form A/Form B sentence
that can be pasted verbatim, and the Completion Check explicitly confirms the citation was made.
R4 V-02 and V-03 fail C-21 because they produce a one-word tag ("stable"/"worsening") with no
named citeable form. The upgrade in R5 V-01 is adding a named STABILITY CITATION RECORD block
in Step 0b — a labeled output box that the model must populate with the exact sentence —
and requiring Phase 2 to paste the RECORD by name, not by reference to "Step 0b."
This creates a harder citation anchor: the model cannot satisfy Phase 2 with a paraphrase
because the instruction names the block, not the concept.
The Completion Check must explicitly state: "CITATION CONFIRMED" or "CITATION MISSING."
A yes/no field is weaker than a required affirmative statement.

```
Run the campaign-specify skill for: {{topic}}

Produce three artifacts in sequence: spec, proposal, pitch. Execute phases 0-3 in order.
Do not begin a later phase until all required outputs of the current phase are complete.

---

## Phase 0 — Audience Foundation

Complete all four steps in sequence before Phase 1 begins.

**Step 0a — Inertia Costs (required first)**

Name what each audience LOSES if {{topic}} does not ship. Concrete and audience-specific.
Generic claims ("this would help") do not pass this step.

Exec inertia cost: [Specific revenue exposure, competitive gap, or risk that persists without
this feature. Name a consequence, not a category.]

Dev inertia cost: [Specific workaround burden, capability gap, or manual step that persists.
Name the friction, not the feeling.]

Maker inertia cost: [Specific workflow step that stays blocked, absent, or manual. Name the step.]

Do not advance to Step 0b until all three inertia costs are complete.

**Step 0b — Stability Citation Record**

Evaluate whether the Do Nothing cost is stable or worsening. Then produce the STABILITY
CITATION RECORD below. This record will be pasted verbatim into the Phase 2 Defeating Do
Nothing block. Complete the record now, before Phase 2 is written.

Choose one form and complete it:

FORM A (cost is worsening):
"Do Nothing is not stable: [specific mechanism — e.g., 'the exec exposure grows as competitors
ship quarterly', 'dev workaround accumulates 3-5 hours per sprint, compounding to 36h/quarter',
'maker volume increases making the blocked step more costly over time']. Becomes acute by:
[specific trigger or time window]."

FORM B (cost is stable):
"Do Nothing is stable: [rationale — e.g., 'the workaround is functional and the underlying
need does not grow with volume']. Remains at current cost level indefinitely."

STABILITY CITATION RECORD:
[Paste the complete Form A or Form B sentence here — the exact text that will appear in Phase 2]

A stability record containing only a tag ("worsening" or "stable") without a mechanism and
timeline fails this step. The record must be a complete sentence suitable for verbatim citation.

Do not advance to Step 0c until the STABILITY CITATION RECORD is complete.

**Step 0c — Voice Contracts**

Using the inertia costs and stability record above as grounding, write one sentence per audience:

Exec voice: [Outcomes/risk framing — reference the exec inertia cost and its stability trajectory]
Dev voice: [Capability/friction framing — reference the dev inertia cost]
Maker voice: [Workflow framing — plain language, reference the maker inertia cost]

**Step 0d — Scout Pull**

Glob `simulations/scout/**/*.md` for {{topic}}. List any files found and note which artifact
(spec, proposal, pitch) each file is most relevant to. If none found: record "no scout signals"
and proceed.

---

## Phase 1 — Technical Spec

Pull from `simulations/scout/` broadly. Note which files from Step 0d were used.

Write the spec. Save to: `simulations/draft/specs/{{topic}}-spec-{{date}}.md`

Six sections required. Do not skip or merge any section.

### Overview
One paragraph describing what {{topic}} does and why it exists.

### User Problem
The problem users face today. Reference the dev and maker inertia costs from Step 0a —
these are evidence of the problem, not invented examples.

### Proposed Solution
What {{topic}} does. Incorporate any scout-requirements or scout-feasibility signals
from Step 0d.

### Constraints
At least three: technical, scope, platform.

### Open Questions
At least three named ambiguities.

### Self-Review
At least one named gap. "No gaps found" fails this section.

---

## Phase 2 — Business Proposal

Pull from `simulations/scout/scout-feasibility/` before writing. Note files used.

Write the proposal. Save to: `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md`

Three options minimum. Option 1 MUST be named **Do Nothing**.

For each option: description, pros, cons, risk, effort.

Then write the **Recommendation** section with the following structure:

We recommend [chosen option].

**Defeating Do Nothing**

Do Nothing perpetuates [cite the most decisive inertia cost from Step 0a — name the audience
and the specific cost].

[PASTE THE STEP 0b STABILITY CITATION RECORD VERBATIM HERE. Do not summarize.
Do not paraphrase. Copy the exact Form A or Form B sentence from Step 0b.
If the record says "Do Nothing is not stable: [mechanism]..." then that sentence
must appear here, character for character.]

We choose to act because [one sentence: why this cost trajectory is not acceptable].

**Defeating [Other Option Name]**

We prefer [chosen option] over [other option] because [specific trade-off traceable to
a risk, effort, or cons field in the options analysis above — not a preference statement].

The Defeating Do Nothing block must contain the STABILITY CITATION RECORD from Step 0b
pasted verbatim. A defeat block that argues cost alone without the record, or that
references stability without the exact record language, does not satisfy C-17 or C-21.

---

## Phase 3 — Executive Pitch

Pull from `simulations/scout/scout-positioning/` before writing. Note files used.

Write the pitch. Save to: `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`

Four sections:

### Exec Version
Lead with the exec inertia cost from Step 0a. Structure:
[exec cost hook] -> [what changes] -> [business outcome/ROI] -> [call to action].
Do not open with a product description.

### Dev Version
Lead with the dev inertia cost from Step 0a. Structure:
[friction hook] -> [what you can now do] -> [capability unlocked] -> [call to action].
Do not open with an outcomes/ROI frame.

### Maker Version
Lead with the maker inertia cost from Step 0a. Plain language, no jargon. Structure:
[blocked step hook] -> [what you can now do] -> [why it matters] -> [call to action].

### Anti-Positioning
3-5 "This is not..." statements. Separate from the three audience versions above.

---

## Completion Check

After all three artifacts are written:

1. Verify spec exists at: `simulations/draft/specs/{{topic}}-spec-{{date}}.md`
2. Verify proposal exists at: `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md`
3. Verify pitch exists at: `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`

If any artifact is missing: write it now before continuing.
Do not emit the final index until all three files exist on disk.

Final index:
- Artifact paths (all three)
- Scout files used per phase
- Step 0a inertia costs confirmed (all three audiences)
- Step 0b STABILITY CITATION RECORD: which form was used (Form A / Form B)
- Citation confirmation: does the STABILITY CITATION RECORD appear verbatim in the
  Defeating Do Nothing block? State one of: CITATION CONFIRMED / CITATION MISSING.
  If CITATION MISSING: return to Phase 2 and paste the record now before stopping.
```

**Rubric targeting**:
- C-21: Step 0b produces a named STABILITY CITATION RECORD with Form A or Form B — a complete citeable sentence, not a tag. Phase 2 requires "PASTE THE STEP 0b STABILITY CITATION RECORD VERBATIM HERE" — citation by name, not by concept. Completion Check requires "CITATION CONFIRMED / CITATION MISSING" — a required affirmative statement, not a yes/no field. If CITATION MISSING, recovery instruction triggers before skill stops.
- C-17: Subsumed — STABILITY CITATION RECORD satisfies C-17's two-location requirement (established in Phase 0, cited in Phase 2). Form A requires mechanism and timeline; Form B requires rationale.
- C-18: "Do not advance to Step 0b until..." and "Do not advance to Step 0c until..." — two intra-Phase 0 gates.
- C-11: "write it now before continuing" active recovery per artifact.
- C-01 through C-15: Preserved from R4 V-01 base.

**Risk**: C-23 is not targeted — no existence-status Completion Index. C-19 and C-20 are not targeted — no inline write gates, no voice differentiation save gate. Single-axis isolation is intentional; V-04 and V-05 stack these.

---

## V-02 — Axis: Explicit Full Phase 0 Gate Chain (C-22 target)

**Hypothesis**: C-22 requires every adjacent step-to-step transition within Phase 0 to be
explicitly gated. R4 V-01 earns C-22 with two gates covering a 3-step chain (0a→0b, 0b→0c);
V-01's Phase 0 has 4 steps but the fourth (scout pull) is terminal — no gate is needed after
the last step because there is no subsequent Phase 0 step. R4 V-05 has a 5-step Phase 0 with
three gates (0a→0b, 0b→0c, 0c→0d) — the 0d→0e transition is ungated. Whether V-05 passes C-22
depends on whether the scorer treats 0e (Do Nothing Baseline) as a dependent step requiring
a gate from 0d, or as a terminal pre-compile step.

R5 V-02 removes ambiguity by using a 4-step Phase 0 where the gate chain is unambiguously
complete: three steps require sequential completion (0a, 0b, 0c), each with a "do not advance"
gate, and the fourth step (0d, scout pull) is explicitly labeled "terminal — no gate required."
The prompt explicitly states how many gates Phase 0 contains and names each one.
This makes C-22 structurally verifiable rather than interpretive.

```
Run the campaign-specify skill for: {{topic}}

Produce three artifacts in sequence: spec, proposal, pitch. Execute phases 0-3 in order.
Phase 0 must complete in full before Phase 1 begins.

---

## Phase 0 — Audience Foundation

Phase 0 contains four steps. The first three steps are sequential and each requires the
previous step's output — each has an explicit advancement gate. The fourth step (scout pull)
is terminal and has no subsequent Phase 0 step.

PHASE 0 GATE CHAIN: Gate 1 (0a→0b) | Gate 2 (0b→0c) | Gate 3 (0c→0d) | Step 0d terminal

**Step 0a — Inertia Costs**

Name what each audience LOSES if {{topic}} does not ship. Concrete and audience-specific.
Generic claims ("this would help") do not pass this step.

Exec inertia cost: [Specific revenue exposure, competitive gap, or risk. Name a consequence,
not a category. Quantify if possible.]

Dev inertia cost: [Specific workaround, manual step, or capability gap. Name the friction,
not the feeling. Estimate recurring cost if possible.]

Maker inertia cost: [Specific blocked or missing workflow step. Name the step. What does
the maker do today instead, and why is it worse?]

--- GATE 1: Do not advance to Step 0b until all three inertia costs are complete. ---

**Step 0b — Do Nothing Stability Assessment**

Evaluate whether the cost of Do Nothing is stable or worsening. Choose one form:

FORM A: "Do Nothing is not stable: [specific mechanism and timeline]."
FORM B: "Do Nothing is stable: [rationale for why cost will not compound]."

Complete one form in full. A stability entry containing only "worsening" or "stable"
without a mechanism or rationale fails this step.

This assessment will be cited verbatim in the Phase 2 Defeating Do Nothing block.

--- GATE 2: Do not advance to Step 0c until the stability assessment (Form A or Form B)
is complete and contains a mechanism or rationale. ---

**Step 0c — Voice Contracts**

One sentence per audience, grounded in the inertia costs and stability assessment above:

Exec voice: [One sentence — outcomes/risk framing. Lead with the exec cost or its trajectory.]
Dev voice: [One sentence — capability/friction framing. Lead with the dev friction or its recurrence.]
Maker voice: [One sentence — workflow framing. Plain language. Lead with the blocked step.]

--- GATE 3: Do not advance to Step 0d until all three voice contracts are written. ---

**Step 0d — Scout Pull** [TERMINAL — no subsequent Phase 0 step]

Glob `simulations/scout/**/*.md` for {{topic}}. For each file found:
- Path
- Signal summary (one sentence)
- Artifact it serves: spec / proposal / pitch

If no scout files found: record "no scout signals" and proceed to Phase 1.

[Phase 0 complete. All three gates passed. Proceed to Phase 1.]

---

## Phase 1 — Technical Spec

Pull from `simulations/scout/` broadly. Note which Step 0d files were used.

Write the spec. All six sections required. Do not skip or merge.

### Overview
One paragraph: what {{topic}} does and why it exists.

### User Problem
The problem users face today. Reference dev and maker inertia costs from Step 0a directly.

### Proposed Solution
What {{topic}} does. Incorporate scout-requirements or scout-feasibility signals from Step 0d.

### Constraints
At least three: technical, scope, platform.

### Open Questions
At least three named ambiguities.

### Self-Review
At least one named gap. "No gaps found" fails.

Save spec to: `simulations/draft/specs/{{topic}}-spec-{{date}}.md`

---

## Phase 2 — Business Proposal

Pull from `simulations/scout/scout-feasibility/` before writing. Note files used.

Write the proposal. Three options minimum. Option 1 MUST be named **Do Nothing**.

For each option: description, pros, cons, risk, effort.

**Recommendation** section:

We recommend [chosen option].

**Defeating Do Nothing**

Do Nothing perpetuates [cite the most decisive Step 0a inertia cost — name the audience and
the specific cost]. [Cite the Step 0b stability assessment verbatim: paste Form A or Form B
here.] We choose to act because [one sentence: why this cost is not acceptable].

**Defeating [Other Option Name]**

We prefer [chosen] over [other] because [specific trade-off traceable to a risk, effort, or
cons field in the options analysis — not a preference statement].

Save proposal to: `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md`

---

## Phase 3 — Executive Pitch

Pull from `simulations/scout/scout-positioning/` before writing. Note files used.

Write the pitch. Four sections:

### Exec Version
Lead with exec inertia cost from Step 0a. Structure:
[exec cost hook] -> [what changes] -> [business outcome/ROI] -> [call to action].
Do not open with a product description.

### Dev Version
Lead with dev inertia cost from Step 0a. Structure:
[friction hook] -> [what you can now do] -> [capability unlocked] -> [call to action].
Do not open with an outcomes/ROI frame.

### Maker Version
Lead with maker inertia cost from Step 0a. Plain language, no jargon. Structure:
[blocked step hook] -> [what you can now do] -> [why it matters] -> [call to action].

### Anti-Positioning
3-5 "This is not..." statements. Separate from the three audience versions above.

Save pitch to: `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`

---

## Completion Check

After all three artifacts:

1. Spec exists at: `simulations/draft/specs/{{topic}}-spec-{{date}}.md` — if missing: write now.
2. Proposal exists at: `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md` — if missing: write now.
3. Pitch exists at: `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md` — if missing: write now.

Do not stop until all three files exist on disk.

Final index: artifact paths, scout files per phase, Step 0a inertia costs confirmed,
Step 0b stability form used (Form A / Form B), Phase 0 gate chain confirmed (3 gates passed).
```

**Rubric targeting**:
- C-22: Phase 0 gate chain is made explicit by the header "PHASE 0 GATE CHAIN: Gate 1 (0a→0b) | Gate 2 (0b→0c) | Gate 3 (0c→0d) | Step 0d terminal." Three sequential steps each have a labeled gate (`--- GATE N: Do not advance to Step 0N+1 until... ---`). Step 0d is explicitly labeled "TERMINAL — no subsequent Phase 0 step" — the scorer can verify N gates for N+1 steps where the last is terminal. The "do not advance" form is used for each. No ambiguity about whether the chain is complete.
- C-18: Subsumed — C-22's full chain satisfies C-18's "at least one" requirement plus more.
- C-17: Step 0b stability assessment uses Form A/Form B; Phase 2 cites verbatim. Two-location requirement preserved.
- C-01 through C-15: Preserved.

**Risk**: C-23 not targeted (no existence-status Completion Index). C-19 and C-20 not targeted. C-21's Completion Check confirmation is absent — the final index says "Step 0b stability form used" but does not have the "CITATION CONFIRMED / CITATION MISSING" check that specifically targets C-21. C-22 mechanism is strong; C-21 is partial. Intentional single-axis isolation.

---

## V-03 — Axis: Existence-Status Completion Index (C-23 target)

**Hypothesis**: R4 V-02 earns C-23 because its Completion Index uses "-- exists" per artifact,
providing explicit confirmed existence status. R4 V-05's Completion Index table has paths but
no per-artifact "[exists / missing]" status field — the existence check is done via write gates
(C-19) but is not recapitulated in the Completion Index as a structural element. C-23 requires
the Completion Index to be a NAMED block that is structurally distinct from write gates (C-19)
and the recovery check (C-11), and which lists existence status per artifact.
R5 V-03 strengthens this by: (1) using a 3-column table (artifact | path | status) rather than
inline "-- exists" notation, (2) making the status field a required fill-in ("[exists / missing]")
that triggers recovery if missing, and (3) labeling the block with a distinct header that
the scorer can identify as structurally separate from the write gates above.

```
Run the campaign-specify skill for: {{topic}}

Produce three artifacts in sequence: spec, proposal, pitch. Execute phases 0-3 in order.
Each phase's artifact must exist on disk before the next phase begins.

---

## Phase 0 — Audience Foundation

Complete all four steps before Phase 1. Do not begin Phase 1 until Phase 0 is complete.

**Step 0a — Inertia Costs**

What each audience LOSES if {{topic}} never ships. Concrete and specific:

Exec inertia cost: [Specific business consequence — revenue, competitive gap, or risk.
Name it, not the category.]

Dev inertia cost: [Specific technical friction — workaround, capability gap, named step.
The actual manual operation, not a feeling.]

Maker inertia cost: [Specific workflow block — the step that fails or is absent today.
The exact missing capability, not "inefficiency."]

Do not advance to Step 0b until all three costs are named.

**Step 0b — Do Nothing Stability**

Is the Do Nothing cost stable or worsening? Choose one form:

FORM A: "Do Nothing is not stable: [specific mechanism and timeline]."
FORM B: "Do Nothing is stable: [rationale]."

Complete the form. This will be cited in Phase 2.

**Step 0c — Voice Contracts**

One sentence per audience, grounded in the inertia costs above:

Exec voice: [Outcomes/risk framing]
Dev voice: [Capability/friction framing]
Maker voice: [Workflow framing — plain language, no jargon]

**Step 0d — Scout Pull**

Glob `simulations/scout/**/*.md` for {{topic}}. List files found and relevance by artifact.

---

## Phase 1 — Technical Spec

Pull from `simulations/scout/` broadly. Note files used.

Write the spec. All six sections required — no skipping, no merging.

### Overview
One paragraph: what {{topic}} does and why it exists.

### User Problem
Problem users face today. Reference dev and maker inertia costs from Step 0a.

### Proposed Solution
What {{topic}} does. Reference scout signals from Step 0d if available.

### Constraints
At least three: technical, scope, platform.

### Open Questions
At least three named ambiguities.

### Self-Review
At least one named gap. "No gaps found" fails.

**>> PHASE 1 WRITE GATE <<**
Save spec to: `simulations/draft/specs/{{topic}}-spec-{{date}}.md`
Confirm the file was written. If it does not exist: write it again now.
Do not begin Phase 2 until `simulations/draft/specs/{{topic}}-spec-{{date}}.md` exists on disk.

---

## Phase 2 — Business Proposal

Pull from `simulations/scout/scout-feasibility/` before writing. Note files used.

Write the proposal with at least three options. Option 1 MUST be named **Do Nothing**.

For each option: description, pros, cons, risk, effort.

**Recommendation** section:

We recommend [chosen option].

**Defeating Do Nothing**: Do Nothing perpetuates [cite inertia cost from Step 0a —
specific audience and cost]. [One sentence on stability from Step 0b: cite the Form A or
Form B text.] We choose to act because [rationale traceable to options analysis].

**Defeating [Other Option]**: We prefer [chosen] over [other] because [specific trade-off
from options analysis — not a preference statement].

**>> PHASE 2 WRITE GATE <<**
Save proposal to: `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md`
Confirm the file was written. If it does not exist: write it again now.
Do not begin Phase 3 until `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md` exists on disk.

---

## Phase 3 — Executive Pitch

Pull from `simulations/scout/scout-positioning/` before writing. Note files used.

Write the pitch with four sections:

### Exec Version
Lead with exec inertia cost from Step 0a. Structure:
[exec cost hook] -> [what changes] -> [business outcome/ROI] -> [call to action].

### Dev Version
Lead with dev inertia cost from Step 0a. Structure:
[friction hook] -> [what you can now do] -> [capability unlocked] -> [call to action].

### Maker Version
Lead with maker inertia cost from Step 0a. Plain language, no jargon. Structure:
[blocked step hook] -> [what you can now do] -> [why it matters] -> [call to action].

### Anti-Positioning
3-5 "This is not..." statements. Separate from the three versions above.

**>> PHASE 3 WRITE GATE <<**
Save pitch to: `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`
Confirm the file was written. If it does not exist: write it again now.
Do not emit the COMPLETION INDEX until `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`
exists on disk.

---

## COMPLETION INDEX

[This block is emitted after all write gates and recovery steps above are complete.
It is structurally distinct from the write gates (which fire at production time) and
from the recovery steps (which are embedded in each write gate). The COMPLETION INDEX
is the post-execution record of confirmed artifact existence.]

Confirm each artifact exists by checking the file path. Then fill in the status column.
If status is "missing": write the artifact now, then update the status to "exists."

| Artifact | Path | Status |
|----------|------|--------|
| Spec | `simulations/draft/specs/{{topic}}-spec-{{date}}.md` | [exists / missing] |
| Proposal | `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md` | [exists / missing] |
| Pitch | `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md` | [exists / missing] |

All three rows must show "exists" before this skill is complete.

Additional index:
- Scout files used per phase
- Phase 0 inertia costs confirmed (all three audiences named)
- Step 0b stability form used (Form A / Form B)
- Do Nothing defeated by name with specific cost citation: yes / no
```

**Rubric targeting**:
- C-23: Named "COMPLETION INDEX" block with explicit header, emitted after all write gates and recovery steps. Three-column table (artifact | path | status) with "[exists / missing]" as a required fill-in per artifact. Recovery instruction embedded: "If status is 'missing': write the artifact now." Labeled as structurally distinct from write gates and recovery steps in the block header. Not a Completion Check (which is a recovery step) and not a write gate (which fires at production time).
- C-19: Three `>> PHASE N WRITE GATE <<` blocks, each collocated with the artifact production instruction, each with "Do not begin Phase N+1 until file exists." Structurally distinct from the COMPLETION INDEX.
- C-11: Each write gate contains "write it again now" recovery instruction. COMPLETION INDEX adds a second recovery path ("write the artifact now, then update the status").
- C-18: "Do not advance to Step 0b until all three costs are named" — at least one intra-Phase 0 gate.

**Risk**: C-21 is not fully targeted — Phase 2 says "cite the Form A or Form B text" but does not use the STABILITY CITATION RECORD label or require "CITATION CONFIRMED" in the Completion Index. C-22 is partially targeted (one intra-Phase 0 gate, not full chain). C-20 is not targeted. Intentional single-axis isolation; V-04 and V-05 stack these.

---

## V-04 — Combined: Citation Lock + Full Gate Chain + Existence-Status Index
## (C-21 + C-22 + C-23)

**Hypothesis**: Stacking the three new v5 mechanisms — V-01's citation lock for C-21,
V-02's explicit labeled gate chain for C-22, and V-03's existence-status COMPLETION INDEX
for C-23 — onto the R4 V-04 base (which already holds C-16, C-17, C-18, C-19) produces a
variation that earns all three new criteria simultaneously while preserving the v4 ceiling.
The three mechanisms are independent: failure of the citation lock does not affect the gate
chain, and failure of either does not affect the Completion Index. This is the targeted
combination with lowest interaction risk: each new criterion has its own structural location
and its own enforcement form.

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

Write the pitch. Four sections:

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

**>> PITCH WRITE GATE <<**
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
- C-21: STABILITY CITATION RECORD labeled and named; Phase 2 requires verbatim paste by name; COMPLETION INDEX has explicit "CITATION CONFIRMED / CITATION MISSING" line with recovery trigger. Three-point enforcement: named output, named citation instruction, named confirmation.
- C-22: "Gate chain: Gate 1 (0a→0b) | Gate 2 (0b→0c) | Gate 3 (0c→0d) | Step 0d terminal" appears in the Phase 0 header; each gate is labeled (`--- GATE N: Do not advance... ---`); the COMPLETION INDEX confirms "3 gates passed." Scorer can verify N gates for N+1 steps without interpretation.
- C-23: Named "COMPLETION INDEX" block with explicit "[exists / missing]" per artifact row; labeled as structurally distinct from write gates and recovery steps in the block header; recovery instruction embedded in the table ("If any status is 'missing': write that artifact now").
- C-16: `#### Defeating Do Nothing` and `#### Defeating [Other Option]` as separate labeled headers; explicit disqualification in the Note.
- C-17: STABILITY CITATION RECORD (Form A/B) satisfies two-location requirement; verbatim paste in Phase 2.
- C-18: Three intra-Phase 0 gates at each substantive step transition.
- C-19: Three write gates, each collocated at production point, each with "Do not begin Phase N+1 until file exists."
- C-11: "write it now" active recovery at each write gate; second recovery path in COMPLETION INDEX.
- C-20: Not targeted — no voice differentiation save gate. This is the one unearned criterion in V-04.

**Risk**: C-20 (voice differentiation save gate) is not included. Predicted score: 14/15 aspirational = 99.3. The interaction between GATE N labels and the Phase 0 header gate-chain summary creates a strong C-22 signal but duplicates text. A scorer applying strict criteria should accept this redundancy as reinforcing, not disqualifying.

---

## V-05 — Full Synthesis: All Five Unearned Criteria (C-19 + C-20 + C-21 + C-22 + C-23)

**Hypothesis**: A single variation that architects five independent mechanisms for the five
unearned criteria earns all 15 aspirational criteria simultaneously. The mechanisms are:
- C-19: Three inline write gates collocated at production points, each blocking the next phase
- C-20: Pre-save voice differentiation gate with conditional rewrite trigger
- C-21: Named STABILITY CITATION RECORD (Form A/Form B) + Phase 2 verbatim paste + Completion Index citation confirmation
- C-22: Explicit labeled gate chain in Phase 0 header; every adjacent transition gated; terminal step labeled
- C-23: Post-execution COMPLETION INDEX with "[exists / missing]" status column per artifact; structurally labeled as distinct from write gates

Each mechanism is independent. Failure of C-20 (voice gate) does not cascade to C-19 (inline write gates).
Failure of C-21 (citation lock) does not cascade to C-22 (gate chain). The COMPLETION INDEX
serves as a self-scoring instrument: a model that fills it honestly will self-expose any
criterion it did not satisfy.

```
Run the campaign-specify skill for: {{topic}}

Produce three artifacts: spec, proposal, pitch. Execute phases 0-3 in order.
Phase 0 must complete in full before Phase 1 begins.
Each artifact is written to disk before the next phase begins.

---

## Phase 0 — Audience Foundation (complete in full before Phase 1)

Phase 0 has five steps. Steps 0a through 0d are sequential with explicit advancement gates.
Step 0e (Do Nothing Baseline) is terminal — it compiles Phase 0 outputs for use in Phase 2.
Gate chain: Gate 1 (0a→0b) | Gate 2 (0b→0c) | Gate 3 (0c→0d) | Gate 4 (0d→0e) | Step 0e terminal.

**Step 0a — Inertia Costs (loss-first)**

Name what each audience LOSES if {{topic}} does not ship. Concrete and audience-specific.
Generic claims ("this would help") do not pass this step.

Exec inertia cost: [Specific revenue exposure, competitive gap, or risk. Name a consequence,
not a category. Quantify if possible ("$X quarterly" or "N% of pipeline").]

Dev inertia cost: [Specific workaround, manual step, or capability gap. Name the friction,
not the feeling. Estimate recurring cost if possible ("3-5 hours per sprint").]

Maker inertia cost: [Specific blocked or missing workflow step. Name the step. What does
the maker do today instead, and why is it worse?]

--- GATE 1: Do not advance to Step 0b until all three inertia costs are complete. ---

**Step 0b — Stability Citation Record**

Evaluate whether the cost of Do Nothing is stable or worsening. Choose one form and
complete it. This becomes the STABILITY CITATION RECORD — it will be pasted verbatim
into the Phase 2 Defeating Do Nothing block.

FORM A (worsening): "Do Nothing is not stable: [specific mechanism and timeline —
e.g., 'competitor ships equivalent feature in Q2, making exec exposure acute by June',
or 'dev workaround accumulates 3 hours/sprint, compounding to 36h/quarter']."

FORM B (stable): "Do Nothing is stable: [rationale — e.g., 'the workaround is functional
and the underlying need does not grow with volume']."

STABILITY CITATION RECORD:
[Paste the complete Form A or Form B sentence here — this exact text will appear in Phase 2]

A record containing only a tag without mechanism or rationale fails this step.

--- GATE 2: Do not advance to Step 0c until the STABILITY CITATION RECORD is complete. ---

**Step 0c — Voice Contracts**

One sentence per audience, grounded in Steps 0a and 0b:

Exec voice: [One sentence — outcomes/risk framing. Lead with exec cost or stability trajectory.]
Dev voice: [One sentence — capability/friction framing. Lead with dev friction or recurrence.]
Maker voice: [One sentence — workflow framing. Plain language. Lead with the blocked step.]

--- GATE 3: Do not advance to Step 0d until all three voice contracts are written. ---

**Step 0d — Scout Pull**

Glob `simulations/scout/**/*.md` for {{topic}}. For each file found:
- Path
- Signal summary (one sentence)
- Artifact it serves: spec / proposal / pitch

If no scout files found: record "no scout signals — proceeding without" and continue.

--- GATE 4: Do not advance to Step 0e until scout pull is complete (found or not found
recorded). ---

**Step 0e — Do Nothing Baseline** [TERMINAL]

Compile for direct use in Phase 2. Copy outputs from Steps 0a and 0b verbatim:

Do Nothing absorbs:
  Exec: [Step 0a exec cost]
  Dev: [Step 0a dev cost]
  Maker: [Step 0a maker cost]
  Stability: [STABILITY CITATION RECORD from Step 0b — paste Form A or Form B verbatim]

[Phase 0 complete. Four gates passed. Proceed to Phase 1.]

---

## Phase 1 — Technical Spec

Pull from `simulations/scout/` broadly. Note which Step 0d files were used.

Write the spec. All six sections required. Do not skip or merge any section.

### Overview
One paragraph: what {{topic}} does and why it exists.

### User Problem
The problem users face today. Open with or reference the dev and maker inertia costs
from Step 0a — these are evidence of the problem, not invented examples.

### Proposed Solution
What {{topic}} does. Incorporate scout-requirements or scout-feasibility signals
from Step 0d if available.

### Constraints
At least three: technical, scope, platform.

### Open Questions
At least three named ambiguities.

### Self-Review
At least one named gap. "No gaps found" fails this section.

**>> SPEC WRITE GATE <<**
Write spec to: `simulations/draft/specs/{{topic}}-spec-{{date}}.md`
After writing: confirm the file exists.
If the file does not exist: write it now before continuing.
Do not begin Phase 2 until `simulations/draft/specs/{{topic}}-spec-{{date}}.md` is on disk.

---

## Phase 2 — Business Proposal

Pull from `simulations/scout/scout-feasibility/` before writing. Note files used.

Write the proposal. Minimum three options. Option 1 MUST be named **Do Nothing**.

For each option: description, pros, cons, risk, effort.

Then write the **Recommendation** section. Two labeled blocks, each with its own header.
Do not merge them into a combined paragraph.

### Recommendation

We recommend [chosen option].

#### Defeating Do Nothing

[This block addresses the status quo competitor. Structurally separate from the
comparative defeat below.]

Do Nothing perpetuates [cite the most decisive Step 0e inertia cost — name the audience
and the specific cost].

[PASTE THE STEP 0e STABILITY LINE VERBATIM HERE — the Form A or Form B sentence from
Step 0b as recorded in Step 0e. Do not summarize. Do not paraphrase. Character for character.]

We choose to act because [one sentence: why this cost trajectory is not acceptable].

#### Defeating [Other Option Name]

We prefer [chosen] over [other] because [specific trade-off traceable to a risk, effort,
or cons field in the options analysis — not a preference statement].

[If additional rejected options exist, add a block for each: #### Defeating [Name].]

Note: A combined Recommendation paragraph defeats all options in prose — does not satisfy C-16.
A Defeating Do Nothing block without the verbatim Step 0e stability line — does not satisfy C-17 or C-21.

**>> PROPOSAL WRITE GATE <<**
Write proposal to: `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md`
After writing: confirm the file exists.
If the file does not exist: write it now before continuing.
Do not begin Phase 3 until `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md` is on disk.

---

## Phase 3 — Executive Pitch

Pull from `simulations/scout/scout-positioning/` before writing. Note files used.

Write all four sections of the pitch below. Do not save the pitch file until the
voice differentiation gate at the end of this phase passes.

### Exec Version
Lead with the exec inertia cost from Step 0a. Use the Step 0c exec voice contract
as your anchor. Opening = the business cost that exists today.
Structure: [exec cost hook] -> [what changes with {{topic}}] -> [business outcome/ROI]
-> [call to action]. Do not open with a product description.

### Dev Version
Lead with the dev inertia cost from Step 0a. Use the Step 0c dev voice contract
as your anchor. Opening = the friction that exists today.
Structure: [friction hook] -> [what you can now do] -> [capability unlocked] ->
[call to action]. Do not open with an outcomes/ROI frame.

### Maker Version
Lead with the maker inertia cost from Step 0a. Use the Step 0c maker voice contract
as your anchor. Opening = the blocked step that exists today. Plain language, no jargon.
Structure: [blocked step hook] -> [what you can now do] -> [why it matters] ->
[call to action]. Test: readable without the spec by a non-technical user.

### Anti-Positioning
3-5 "This is not..." statements. This section is structurally separate from the three
audience versions above.

**>> VOICE DIFFERENTIATION GATE (required before saving pitch) <<**

Before saving the pitch file, extract the opening sentence from each version:

  Exec opening: [first sentence of Exec Version]
  Dev opening: [first sentence of Dev Version]
  Maker opening: [first sentence of Maker Version]

Differentiation check: Do any two openings share the same frame?
(Same subject, same lead claim, or same opening phrase = same frame.)

Expected pattern:
  Exec opens with: a business cost, risk, or revenue consequence
  Dev opens with: a tool friction, workaround, or capability gap
  Maker opens with: a workflow step that is blocked, absent, or manual

IF any two openings are the same or use the same frame:
  Rewrite the duplicated version(s) until all three openings are detectably distinct.
  Re-run this check after rewriting.
  Do not save the pitch until all three opening frames are distinct.

IF all three openings are distinct: proceed.

**>> PITCH WRITE GATE <<**
[Save only after the voice differentiation gate above passes.]
Write pitch to: `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`
After writing: confirm the file exists.
If the file does not exist: write it now before stopping.
Do not emit the COMPLETION INDEX until `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`
is on disk.

---

## COMPLETION INDEX

[This block is emitted after all write gates, voice differentiation gate, and recovery steps
above are complete. It is structurally distinct from: (1) write gates, which fire at artifact
production time; (2) the voice differentiation gate, which fires before pitch save; and
(3) the recovery instructions embedded in each write gate. The COMPLETION INDEX is the
post-execution existence record and self-scoring summary.]

Confirm each artifact exists by checking the file path. Fill in the status column from
actual verification results. If any status is "missing": write that artifact now, then
update the row to "exists" before emitting the rest of this index.

| Artifact | Path | Status |
|----------|------|--------|
| Spec | `simulations/draft/specs/{{topic}}-spec-{{date}}.md` | [exists / missing] |
| Proposal | `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md` | [exists / missing] |
| Pitch | `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md` | [exists / missing] |

All three rows must show "exists" before the skill is complete.

Self-scoring index:

| Criterion check | Result |
|-----------------|--------|
| Scout files used — spec phase | [list or "none"] |
| Scout files used — proposal phase | [list or "none"] |
| Scout files used — pitch phase | [list or "none"] |
| Phase 0 inertia costs — all three audiences named | yes / no |
| Phase 0 gate chain — 4 gates passed | Gate 1: yes/no | Gate 2: yes/no | Gate 3: yes/no | Gate 4: yes/no |
| STABILITY CITATION RECORD — Form A or Form B | Form A / Form B |
| STABILITY CITATION RECORD — pasted verbatim in Defeating Do Nothing block | CITATION CONFIRMED / CITATION MISSING |
| Defeating Do Nothing block — separate labeled header (#### or equivalent) | yes / no |
| Voice differentiation gate result | distinct / rewritten-to-distinct |
```

**Rubric targeting**:
- C-01: Three artifacts + three inline write gates + COMPLETION INDEX existence verification.
- C-02: Six sections, all named, "Do not skip or merge any section."
- C-03: Three options, Do Nothing as Option 1, all fields + Recommendation with labeled blocks.
- C-04: Exec/Dev/Maker versions + Anti-Positioning as separate section.
- C-05: Step 0a costs flow into spec (User Problem), proposal (Step 0e Defeating Do Nothing), pitch (voice contract anchors) — consistent by Step 0e pre-compile reference.
- C-06: "Which section needs more work and why? 'No gaps found' fails."
- C-07: Anti-Positioning as explicit named section.
- C-08: "Defeating [Other Option]" requires trade-off traceable to options analysis field.
- C-09: Step 0d scout pull with per-artifact routing; per-phase targeted re-queries.
- C-10: Voice contracts (Step 0c) anchor pitch openings; voice differentiation gate verifies distinct frames.
- C-11: Each write gate includes "write it now" active recovery; COMPLETION INDEX adds second recovery path.
- C-12: Five-step Phase 0 (including Step 0c voice contracts) precedes Phase 1.
- C-13: Phase 0d → Phase 1 broad → Phase 2 scout-feasibility → Phase 3 scout-positioning.
- C-14: Step 0a requires named specific costs per audience with quantification prompts.
- C-15: Defeating Do Nothing block names Do Nothing + cites specific cost + verbatim stability + "We choose to act because."
- C-16: `#### Defeating Do Nothing` header structurally separate from `#### Defeating [Other Option]`; explicit disqualification in note.
- C-17: STABILITY CITATION RECORD (Form A/B) establishes named output in Phase 0; Step 0e compiles it verbatim; Phase 2 "PASTE THE STEP 0e STABILITY LINE VERBATIM HERE" enforces two-location requirement; Self-scoring index confirms citation.
- C-18: Four intra-Phase 0 gates (subsumed by C-22's full chain coverage).
- C-19: Three write gates (SPEC, PROPOSAL, PITCH), each collocated with production instruction, each with "Do not begin Phase N+1 until file is on disk." Structurally distinct from COMPLETION INDEX.
- C-20: VOICE DIFFERENTIATION GATE before pitch save; extracts opening sentences per audience; specifies expected patterns; conditional trigger: "IF any two openings share the same frame: Rewrite... Do not save until all three opening frames are distinct." Save collocated after gate passes.
- C-21: STABILITY CITATION RECORD is a named labeled block in Phase 0 (not a tag). Phase 2 requires "PASTE THE STEP 0e STABILITY LINE VERBATIM HERE." Self-scoring index has "CITATION CONFIRMED / CITATION MISSING" row — an affirmative declaration, not a yes/no checkbox. Recovery trigger if CITATION MISSING.
- C-22: Phase 0 header explicitly names the gate chain: "Gate 1 (0a→0b) | Gate 2 (0b→0c) | Gate 3 (0c→0d) | Gate 4 (0d→0e) | Step 0e terminal." Four labeled gates (`--- GATE N: Do not advance... ---`) for five steps. Step 0e is explicitly labeled TERMINAL. Self-scoring index confirms "4 gates passed" with individual gate results.
- C-23: Named "COMPLETION INDEX" block with explicit structural label distinguishing it from write gates, voice gate, and recovery steps. Three-column table with "[exists / missing]" as required fill-in per artifact. Recovery instruction embedded: "If any status is 'missing': write that artifact now, then update the row." Emitted after ALL gates and recovery steps complete.

**Risk**: This is the most complex variation. Five independent mechanisms increase total length.
Mitigation: each mechanism is self-contained — failure of C-20 (voice gate) does not affect
C-23 (COMPLETION INDEX). The self-scoring index in the COMPLETION INDEX is the strongest
self-exposure mechanism in any variation: a model that fills it honestly will report
"CITATION MISSING" or "Gate N: no" rather than a false affirmative. The four-gate Phase 0
chain (C-22) adds one gate over V-05 R4 (which had three gates). Gate 4 (0d→0e) guards the
scout pull → baseline compilation boundary, which is the weakest dependency but the one the
C-22 criterion's "every adjacent transition" language requires.

---

## Variation Summary

| ID | Primary Axis | Key Mechanism | New Targets | Predicted Score (v5) | Risk |
|----|--------------|---------------|-------------|----------------------|------|
| V-01 | Citation lock | STABILITY CITATION RECORD in Step 0b; Phase 2 verbatim paste by name; Completion Check "CITATION CONFIRMED / CITATION MISSING" | C-21 | 93.3 (14/15 asp minus C-19, C-20, C-23) | Citation confirmation label stronger than yes/no; verbatim-by-name harder to satisfy with paraphrase |
| V-02 | Explicit full gate chain | Phase 0 header names gate chain; each gate labeled `--- GATE N ---`; terminal step labeled | C-22 | 91.7 (13/15 asp minus C-19, C-20, C-23) | 4-gate chain adds Gate 4 (0d→0e) over R4 V-05; makes C-22 structurally unambiguous |
| V-03 | Existence-status Completion Index | Named COMPLETION INDEX block with 3-column table (artifact \| path \| status); "[exists / missing]" fill-in per row; recovery if missing | C-23 | 93.3 (14/15 asp minus C-21, C-22) | Three inline write gates (C-19) preserved; existence status is per-row, not aggregate; structurally labeled as distinct |
| V-04 | C-21 + C-22 + C-23 combined | Citation lock + labeled gate chain + existence-status Completion Index on R4 V-04 base | C-21, C-22, C-23 | 99.3 (14/15 asp; misses C-20 voice gate) | Three new mechanisms independent; interaction risk low; C-20 intentionally deferred to V-05 |
| V-05 | Full synthesis | Five independent mechanisms: C-19 write gates, C-20 voice gate, C-21 citation lock, C-22 four-gate chain, C-23 existence-status index | C-19, C-20, C-21, C-22, C-23 | 100.0 (15/15 asp) | Highest complexity; each mechanism self-contained so failure does not cascade; self-scoring index self-exposes any missed criterion |

**Predicted leaderboard**: V-05 > V-04 > V-01 = V-03 > V-02

V-05 targets all five unearned criteria with independent mechanisms and adds a four-gate Phase 0 chain. V-04 hits three of the five new criteria (misses C-20). V-01 and V-03 are equivalent in predicted score but target different criteria. V-02 is the weakest combination (adds only C-22 to the R4 V-05 base).

The critical unlock from R5: no R4 variation earned C-23 (existence-status Completion Index) while also holding C-19 and C-20. V-05 is the first variation to place all three — inline write gates (C-19), voice save gate (C-20), and existence-status COMPLETION INDEX (C-23) — in the same prompt. These three criteria target different structural locations (production points, pitch save, and post-execution respectively) and do not interfere. Stacking them should earn all three without trade-offs.
