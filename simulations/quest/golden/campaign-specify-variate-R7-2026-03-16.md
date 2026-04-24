---
skill: quest-variate
skill_target: campaign-specify
round: 7
date: 2026-03-16
rubric: v7 (23 aspirational criteria, C-27 through C-31 are the new targets)
---

# Variations — campaign-specify / Round 7

Five complete, runnable skill body variations targeting the v7 rubric.
Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

**R6 diagnosis driving R7 axis choices:**

Under v7, the scoring formula is `(essential/5 * 60) + (rec/3 * 30) + (asp/23 * 10)`.
Five new criteria (C-27 through C-31) were extracted from R6 excellence signals.

| Variation | Asp under v7 | Earned new | Missing new | Why |
|-----------|-------------|------------|-------------|-----|
| R6 V-01 | 18/23 | — | C-27,28,29,30,31 | Minimal gate, no per-audience labels, no COMPLETION INDEX voice row |
| R6 V-02 | 19/23 | C-28 | C-27,29,30,31 | Per-audience "gate" formalism earns C-28; no inline step-pair labels, no voice audit row |
| R6 V-03 | 20/23 | C-29, C-31 | C-27,28,30 | Step 0c named in criteria earns C-29; doubly-anchored earns C-31; "check" not "gate" per audience; no inline step-pair |
| R6 V-04 | 19/23 | C-27 | C-28,29,30,31 | Voice audit row in COMPLETION INDEX earns C-27; minimal gate format misses per-audience formalism |
| R6 V-05 | 20/23 | C-30, C-31 | C-27,C-28,C-29 | Inline step-pair labels earn C-30; doubly-anchored earns C-31; uses "check" (not "gate") per audience; gate criteria say "exec contract's frame" not "Step 0c exec contract" |

**R7 gap**: No R6 variation earns all five simultaneously. R6 V-05 is the richest base (earns
C-30 and C-31, has COMPLETION INDEX voice row, has doubly-anchored contracts, has inline
step-pair labels). The two unearned criteria in V-05 are:

- **C-28** (missing): V-05 uses "Exec check / Dev check / Maker check" — C-28 requires named
  audience-level GATE blocks with explicit `Pass (...) / Fail (...)` parenthetical criteria.
  V-02 (R6) earns C-28 by naming `Exec gate / Dev gate / Maker gate` with parenthetical Pass
  and Fail descriptions.

- **C-29** (missing): V-05 gate Step 3 says "match the exec contract's frame" — C-29 requires
  the gate to derive criteria "by name from the Step 0c voice contracts" (explicitly naming
  "Step 0c exec/dev/maker contract" in the criteria text) and the rewrite instruction to name
  "the Step 0c contract for that audience" as the revision anchor. V-03 (R6) earns C-29 by
  writing "match the frame of the Step 0c exec contract (outcomes/risk register)".

Note on C-27: R6 V-05 already has `Voice differentiation gate result: distinct /
rewritten-to-distinct` in the COMPLETION INDEX Additional index — the same line V-04 earns
C-27 for. Whether C-27 scoring requires a FORMAL SECTION HEADER (distinct from a bullet
point) is the axis tested in V-03. If V-05 already earns C-27, then V-04 (combining C-28
and C-29 into V-05) should reach 23/23.

| Axis | Mechanism | Targets |
|------|-----------|---------|
| C-28 gate formalism (V-01 style) | Change "Exec check / Dev check / Maker check" → "Exec gate / Dev gate / Maker gate" + parenthetical Pass/Fail descriptions | C-28 |
| C-29 Step 0c explicit naming (V-02 style) | Gate criteria name "the Step 0c exec/dev/maker voice contract"; rewrite anchor names "the Step 0c contract for that audience" | C-29 |
| C-27 formal section header (V-03 style) | COMPLETION INDEX voice result gets its own labeled section header ("Voice Compliance Audit") distinct from the bullet list | C-27 |
| C-28 + C-29 combined (V-04) | V-05 base + C-28 gate naming + C-29 Step 0c explicit naming; predicted 23/23 if V-05 already earns C-27 | C-28 + C-29 |
| Full synthesis (V-05) | V-04 + C-27 formal section header; maximum evidence density across all five new criteria | All five |

**Predicted ceiling**: V-04 or V-05 reaches 23/23. All five variations expected to hold
5/5 essential, 3/3 recommended, and C-09 through C-26 from R6 V-05 base.

---

## V-01 — Axis: C-28 Per-Audience Gate Formalism

**Hypothesis**: R6 V-05 earns C-30 and C-31 but not C-28 because its gate Step 3 uses
"Exec check / Dev check / Maker check" — functional vocabulary that doesn't match the
"gate" formalism C-28 measures. R6 V-02 earns C-28 by naming each verdict block "Exec gate
/ Dev gate / Maker gate" AND providing explicit parenthetical Pass/Fail descriptions that
define what a passing and failing opening looks like per audience. Transplanting V-02's gate
labeling and parenthetical criteria into V-05's structure should earn C-28 while preserving
the C-30 (inline step-pair labels) and C-31 (doubly-anchored contracts) V-05 already holds.
Single change: replace Step 3 "check" labels with "gate" labels and add Pass/Fail
parentheticals. No Phase 0 changes. COMPLETION INDEX voice row preserved. Predicted: earns
C-28, C-30, C-31 = 21/23.

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

Step 3 — Per-audience gate (each audience gate must independently pass):

  Exec gate: Does the Exec Version opening match the exec contract's frame?
    Pass (opening names a business cost, risk, or revenue consequence) /
    Fail (opens with product description, capability framing, or workflow framing)

  Dev gate: Does the Dev Version opening match the dev contract's frame?
    Pass (opening names a tool friction, workaround, or capability gap) /
    Fail (opens with outcome/ROI framing or business consequence framing)

  Maker gate: Does the Maker Version opening match the maker contract's frame?
    Pass (opening names a blocked, absent, or manual step in plain language, no jargon) /
    Fail (opens with product description or technical jargon)

Step 4 — Resolution:
  IF any gate is Fail: Rewrite the failing version using the Step 0c contract for that
    audience as the revision anchor. Re-run Steps 2-3.
    Do not save the pitch until all three audience gates are Pass.
  IF all three gates are Pass: proceed to PITCH WRITE GATE.

**>> PITCH WRITE GATE <<**
[Save only after all three audience gates in the voice differentiation gate above are Pass.]
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
- C-28: Step 3 uses "Exec gate / Dev gate / Maker gate" labels with explicit parenthetical
  Pass/Fail descriptions per audience: `Pass (opening names a business cost, risk, or revenue
  consequence) / Fail (opens with product description...)`. Independent verdict per audience.
  "Each audience gate must independently pass." Active blocking: "Do not save the pitch until
  all three audience gates are Pass."
- C-30: Inline step-pair gate labels `--- GATE 1 (0a→0b) ---` preserved from R6 V-05.
- C-31: Step 0c contracts referenced in pitch sections ("Use Step 0c exec/dev/maker voice
  contract as anchor") AND in gate Step 1 (explicit copy of voice contracts) AND in Step 4
  rewrite anchor. Doubly anchored.
- C-27: `Voice differentiation gate result: distinct / rewritten-to-distinct` in COMPLETION
  INDEX Additional index — preserved from R6 V-05.
- C-29: Gap — gate Step 3 says "exec contract's frame" not "Step 0c exec contract". Not earned.

**Risk**: The parenthetical Pass/Fail format ("Pass (opening names...) / Fail (opens with...)")
is taken directly from R6 V-02 which earned C-28. The only new element vs R6 V-05 is the
"gate" label and parenthetical criteria in Step 3. All other mechanisms unchanged.
Predicted: 21/23 (adds C-28 to R6 V-05's C-30 + C-31 baseline; C-27 conditional on whether
V-05's voice audit row already earned it in R6).

---

## V-02 — Axis: C-29 Step 0c Explicit Naming in Gate Criteria

**Hypothesis**: R6 V-05 earns C-31 (doubly-anchored contracts) but not C-29 because its
gate Step 3 says "the exec contract's frame" and "the dev contract's frame" — generic
references that do not name the Step 0c contract by its phase-step identifier. C-29 requires
the gate criteria to derive pass conditions "by name from the Step 0c voice contracts": the
phrase "the Step 0c exec voice contract" must appear in the criteria text so a scorer can
trace the gate's authority back to a named phase artifact. Similarly, Step 4's rewrite
anchor must name "the Step 0c contract for that audience" explicitly. R6 V-03 earns C-29
by writing "match the frame of the Step 0c exec contract (outcomes/risk register)". This
variation applies the same naming pattern to the richer V-05 gate structure, which already
has inline step-pair labels and the COMPLETION INDEX voice row. Single change: add "Step 0c"
qualifier to each contract reference in the gate criteria and rewrite anchor.
Predicted: earns C-29, C-30, C-31 = 21/23.

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

The Step 0c voice contracts are the gate criteria. Use them now.

Step 1 — Copy your Step 0c voice contracts:
  Step 0c exec voice contract: [your exec voice sentence from Step 0c]
  Step 0c dev voice contract: [your dev voice sentence from Step 0c]
  Step 0c maker voice contract: [your maker voice sentence from Step 0c]

Step 2 — Extract the opening sentence from each pitch version:
  Exec opening: [first sentence of Exec Version]
  Dev opening: [first sentence of Dev Version]
  Maker opening: [first sentence of Maker Version]

Step 3 — Contract check (each must independently pass):
  Exec check: Does the Exec Version opening match the frame of the Step 0c exec voice
    contract (outcomes/risk register — business cost, risk, or revenue consequence)?
    Pass / Fail
  Dev check: Does the Dev Version opening match the frame of the Step 0c dev voice
    contract (capability/friction register — tool friction, workaround, or capability gap)?
    Pass / Fail
  Maker check: Does the Maker Version opening match the frame of the Step 0c maker voice
    contract (jargon-free blocked-step register — a blocked, absent, or manual workflow step)?
    Pass / Fail

Step 4 — Resolution:
  IF any check is Fail: Rewrite the failing version. Return to the Step 0c voice contract
    for that audience as the named revision anchor. Re-run Steps 2-3.
    Do not save the pitch until all three Step 0c contract checks are Pass.
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
- C-29: Gate Step 3 says "match the frame of the **Step 0c exec voice contract**" (naming
  the contract by phase-step identifier). Step 4 rewrite anchor says "Return to the
  **Step 0c voice contract for that audience** as the named revision anchor." Both the
  criteria derivation and the rewrite instruction name Step 0c explicitly.
- C-31: Step 0c contracts referenced in pitch sections ("Use Step 0c exec/dev/maker voice
  contract as anchor") AND in gate Step 1 (copy) AND in Step 3 criteria names AND in Step 4
  rewrite anchor. Quadruply anchored — unambiguously doubly anchored.
- C-30: Inline step-pair gate labels `--- GATE 1 (0a→0b) ---` preserved from R6 V-05.
- C-27: `Voice differentiation gate result: distinct / rewritten-to-distinct` in COMPLETION
  INDEX Additional index — preserved from R6 V-05.
- C-28: Gap — Step 3 uses "Exec check / Dev check / Maker check" and lacks explicit
  parenthetical Pass/Fail descriptions. Not earned.

**Risk**: The naming change is minimal — adding "Step 0c" qualifier before "exec/dev/maker
voice contract" in three criteria lines and one rewrite anchor line. This is the only
structural difference from R6 V-05. The risk is that C-29's requirement for "named rewrite
anchor" is already partially met in R6 V-05 and this variation makes it unambiguously explicit.
Predicted: 21/23.

---

## V-03 — Axis: C-27 Formal Voice Compliance Section in COMPLETION INDEX

**Hypothesis**: R6 V-04 and V-05 both have the voice audit bullet line
`Voice differentiation gate result: distinct / rewritten-to-distinct` in the Additional index.
The v7 rubric credits V-04 with C-27 but not V-05. One possible explanation: C-27 requires
the voice gate result to be recorded as a "named audit entry" — not merely a bullet among
other bullets, but a structurally classified element with its own header that formalizes the
COMPLETION INDEX as having discrete sections: artifact existence, phase gate chain, citation
audit, AND voice compliance audit. If C-27 requires formal section classification (not just
a bullet in a list), then neither R6 V-04 nor V-05 fully earns it and this variation's
formal "Voice Compliance Audit" section header is the correct targeting mechanism. This axis
tests whether formal section naming within the COMPLETION INDEX is what C-27 measures.

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
complete. This block is the post-execution existence record and unified compliance audit.
It is structurally distinct from: (1) write gates (fire at artifact production time),
(2) the voice differentiation gate (fires before pitch save), (3) recovery instructions
embedded in write gates. The index has four named sections: Artifact Existence Record,
Phase Gate Audit, Citation Audit, and Voice Compliance Audit.]

### Artifact Existence Record

Confirm each artifact exists. Fill in the status column from actual file check results.
If any status is "missing": write that artifact now, then update the row to "exists."

| Artifact | Path | Status |
|----------|------|--------|
| Spec | `simulations/draft/specs/{{topic}}-spec-{{date}}.md` | [exists / missing] |
| Proposal | `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md` | [exists / missing] |
| Pitch | `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md` | [exists / missing] |

All three rows must show "exists" before the skill is complete.

### Phase Gate Audit
- Scout files used per phase
- Phase 0 inertia costs confirmed (all three audiences)
- Phase 0 gate chain: 3 gates passed (Gate 1: 0a→0b | Gate 2: 0b→0c | Gate 3: 0c→0d)

### Citation Audit
- STABILITY CITATION RECORD form used: Form A / Form B
- STABILITY CITATION RECORD pasted verbatim in Defeating Do Nothing block:
  CITATION CONFIRMED / CITATION MISSING
  (If CITATION MISSING: return to Phase 2 and paste the record before stopping.)
- Defeating Do Nothing block: separate labeled header (#### or equivalent): yes / no

### Voice Compliance Audit
- Voice differentiation gate result: distinct / rewritten-to-distinct
```

**Rubric targeting**:
- C-27: COMPLETION INDEX formally classifies its contents into four named sections, including
  "Voice Compliance Audit" as a structurally named element at the same heading level as
  Artifact Existence Record, Phase Gate Audit, and Citation Audit. The voice gate result is
  recorded as a named section entry, not merely a bullet. The preamble explicitly enumerates
  the four sections: "The index has four named sections: Artifact Existence Record, Phase
  Gate Audit, Citation Audit, and Voice Compliance Audit."
- C-30: Inline step-pair gate labels `--- GATE 1 (0a→0b) ---` preserved from R6 V-05.
- C-31: Step 0c contracts referenced in pitch sections AND in gate Steps 1+3+4.
- C-28: Gap — Step 3 uses "check" not "gate" labels. Not earned.
- C-29: Gap — Step 3 says "exec contract's frame" not "Step 0c exec contract". Not earned.

**Risk**: The COMPLETION INDEX restructuring adds three section headers (### Artifact Existence
Record, ### Phase Gate Audit, ### Citation Audit, ### Voice Compliance Audit) without changing
the content of each section. The only substantive new element is the formal naming of sections
in the preamble. Risk: the section-header restructuring could interfere with C-23 (COMPLETION
INDEX structurally distinct from write gates) if scorers interpret the new header nesting as
conflating the write gate section. The preamble explicitly addresses this by naming what the
COMPLETION INDEX is distinct from. Predicted: 21/23 if formal classification earns C-27, 20/23
otherwise.

---

## V-04 — Combined: C-28 Gate Formalism + C-29 Step 0c Naming (targeting 23/23)

**Hypothesis**: The R7 ceiling is earned by combining the two mechanisms that each individually
unblock one gap in R6 V-05. V-01 demonstrates the C-28 mechanism (per-audience "gate" labels
with parenthetical Pass/Fail). V-02 demonstrates the C-29 mechanism (Step 0c explicitly named
in gate criteria and rewrite anchor). R6 V-05 already carries C-27 (voice audit row),
C-30 (inline step-pair labels), and C-31 (doubly-anchored contracts). Adding both C-28 and
C-29 mechanisms to V-05's base produces a variation that earns all five new criteria
simultaneously. The two mechanisms are structurally independent — C-28 affects the label
and parenthetical format of gate Step 3 verdicts; C-29 affects the contract reference text
in gate Step 3 criteria and Step 4 anchor. They do not interfere with each other or with
any of the existing 18 criteria.

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

The Step 0c voice contracts are the gate criteria. Use them now.

Step 1 — Copy your Step 0c voice contracts:
  Step 0c exec voice contract: [your exec voice sentence from Step 0c]
  Step 0c dev voice contract: [your dev voice sentence from Step 0c]
  Step 0c maker voice contract: [your maker voice sentence from Step 0c]

Step 2 — Extract the opening sentence from each pitch version:
  Exec opening: [first sentence of Exec Version]
  Dev opening: [first sentence of Dev Version]
  Maker opening: [first sentence of Maker Version]

Step 3 — Per-audience gate (each audience gate must independently pass):

  Exec gate: Does the Exec Version opening match the frame of the Step 0c exec voice
    contract (outcomes/risk register)?
    Pass (opening names a business cost, risk, or revenue consequence) /
    Fail (opens with product description, capability framing, or workflow framing)

  Dev gate: Does the Dev Version opening match the frame of the Step 0c dev voice
    contract (capability/friction register)?
    Pass (opening names a tool friction, workaround, or capability gap) /
    Fail (opens with outcome/ROI framing or business consequence framing)

  Maker gate: Does the Maker Version opening match the frame of the Step 0c maker voice
    contract (jargon-free blocked-step register)?
    Pass (opening names a blocked, absent, or manual step in plain language, no jargon) /
    Fail (opens with product description or technical jargon)

Step 4 — Resolution:
  IF any gate is Fail: Rewrite the failing version. Return to the Step 0c voice contract
    for that audience as the named revision anchor. Re-run Steps 2-3.
    Do not save the pitch until all three Step 0c contract gates are Pass.
  IF all three gates are Pass: proceed to PITCH WRITE GATE.

**>> PITCH WRITE GATE <<**
[Save only after all three Step 0c contract gates in the voice differentiation gate
above are Pass.]
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
- C-28: Step 3 uses "Exec gate / Dev gate / Maker gate" labels. Each gate carries explicit
  parenthetical Pass/Fail criteria: `Pass (opening names a business cost, risk, or revenue
  consequence) / Fail (opens with product description, capability framing, or workflow
  framing)`. Independent verdicts: "each audience gate must independently pass."
- C-29: Step 3 criteria name "the Step 0c exec/dev/maker voice contract" explicitly as the
  named source of pass criteria. Step 4 rewrite anchor: "Return to the Step 0c voice contract
  for that audience as the named revision anchor." Both the criteria derivation AND the
  rewrite anchor explicitly name Step 0c.
- C-30: Inline step-pair gate labels `--- GATE 1 (0a→0b): Do not advance... ---` preserved
  from R6 V-05 base.
- C-31: Step 0c contracts referenced in pitch sections ("Use Step 0c exec/dev/maker voice
  contract as anchor") AND in gate Step 1 (copy) AND in gate Step 3 criteria
  ("frame of the Step 0c exec voice contract") AND in Step 4 rewrite anchor.
- C-27: `Voice differentiation gate result: distinct / rewritten-to-distinct` in COMPLETION
  INDEX Additional index — preserved from R6 V-05.

**Risk**: The two added mechanisms (C-28 gate labels and C-29 Step 0c naming) are structurally
independent and each proven in prior R6 variations. The interaction point is gate Step 3,
where "Exec gate" (C-28) and "the Step 0c exec voice contract" (C-29) co-inhabit the same
sentence: "Does the Exec Version opening match the frame of the Step 0c exec voice contract
(outcomes/risk register)? Pass (...) / Fail (...)". This sentence simultaneously satisfies
the named-gate formalism, the per-audience verdict, the contract-derived criteria, and the
Step 0c explicit naming. No existing criterion is disturbed. Predicted: 23/23 aspirational.

---

## V-05 — Full Synthesis: C-28 + C-29 + C-27 Formal Section + Maximum Evidence Density

**Hypothesis**: V-04 is the predicted 23/23 variation. V-05 tests whether the formal
COMPLETION INDEX section structure from V-03 (which makes C-27 unambiguous if it was
ambiguous in V-04) can co-exist with the C-28 and C-29 mechanisms from V-04 without
interference. The only structural difference from V-04 is the COMPLETION INDEX
restructuring into four named sections (Artifact Existence Record / Phase Gate Audit /
Citation Audit / Voice Compliance Audit) and the preamble's explicit enumeration of those
sections. This is additive: if V-04 already earns C-27 via the Additional index bullet,
V-05 earns it via formal section header, making the evidence doubly strong. If V-04 does
NOT earn C-27 (because the bullet form is insufficient), V-05 adds the formal section
header mechanism that should earn it. In either case, V-05 is the maximum evidence
density variation for all five new criteria simultaneously.

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

The Step 0c voice contracts are the gate criteria. Use them now.

Step 1 — Copy your Step 0c voice contracts:
  Step 0c exec voice contract: [your exec voice sentence from Step 0c]
  Step 0c dev voice contract: [your dev voice sentence from Step 0c]
  Step 0c maker voice contract: [your maker voice sentence from Step 0c]

Step 2 — Extract the opening sentence from each pitch version:
  Exec opening: [first sentence of Exec Version]
  Dev opening: [first sentence of Dev Version]
  Maker opening: [first sentence of Maker Version]

Step 3 — Per-audience gate (each audience gate must independently pass):

  Exec gate: Does the Exec Version opening match the frame of the Step 0c exec voice
    contract (outcomes/risk register)?
    Pass (opening names a business cost, risk, or revenue consequence) /
    Fail (opens with product description, capability framing, or workflow framing)

  Dev gate: Does the Dev Version opening match the frame of the Step 0c dev voice
    contract (capability/friction register)?
    Pass (opening names a tool friction, workaround, or capability gap) /
    Fail (opens with outcome/ROI framing or business consequence framing)

  Maker gate: Does the Maker Version opening match the frame of the Step 0c maker voice
    contract (jargon-free blocked-step register)?
    Pass (opening names a blocked, absent, or manual step in plain language, no jargon) /
    Fail (opens with product description or technical jargon)

Step 4 — Resolution:
  IF any gate is Fail: Rewrite the failing version. Return to the Step 0c voice contract
    for that audience as the named revision anchor. Re-run Steps 2-3.
    Do not save the pitch until all three Step 0c contract gates are Pass.
  IF all three gates are Pass: proceed to PITCH WRITE GATE.

**>> PITCH WRITE GATE <<**
[Save only after all three Step 0c contract gates in the voice differentiation gate
above are Pass.]
Save pitch to: `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`
Check: does the file exist? If not: write it now.
Do not emit the COMPLETION INDEX until this file exists on disk.

---

## COMPLETION INDEX

[Emitted after all write gates, voice differentiation gate, and recovery steps are
complete. This block is the post-execution existence record and unified compliance audit.
It is structurally distinct from: (1) write gates (fire at artifact production time),
(2) the voice differentiation gate (fires before pitch save), (3) recovery instructions
embedded in write gates. The index has four named sections: Artifact Existence Record,
Phase Gate Audit, Citation Audit, and Voice Compliance Audit. Each section classifies
a distinct category of compliance state.]

### Artifact Existence Record

Confirm each artifact exists. Fill in the status column from actual file check results.
If any status is "missing": write that artifact now, then update the row to "exists."

| Artifact | Path | Status |
|----------|------|--------|
| Spec | `simulations/draft/specs/{{topic}}-spec-{{date}}.md` | [exists / missing] |
| Proposal | `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md` | [exists / missing] |
| Pitch | `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md` | [exists / missing] |

All three rows must show "exists" before the skill is complete.

### Phase Gate Audit
- Scout files used per phase
- Phase 0 inertia costs confirmed (all three audiences)
- Phase 0 gate chain: 3 gates passed (Gate 1: 0a→0b | Gate 2: 0b→0c | Gate 3: 0c→0d)

### Citation Audit
- STABILITY CITATION RECORD form used: Form A / Form B
- STABILITY CITATION RECORD pasted verbatim in Defeating Do Nothing block:
  CITATION CONFIRMED / CITATION MISSING
  (If CITATION MISSING: return to Phase 2 and paste the record before stopping.)
- Defeating Do Nothing block: separate labeled header (#### or equivalent): yes / no

### Voice Compliance Audit
- Voice differentiation gate result: distinct / rewritten-to-distinct
```

**Rubric targeting**:
- C-27: COMPLETION INDEX has a formal "Voice Compliance Audit" section with its own header
  (### level, parallel to Artifact Existence Record and Phase Gate Audit). The preamble
  formally enumerates four named sections including Voice Compliance Audit. The voice gate
  result is a classified section entry, not a bullet. Unambiguous formal classification.
- C-28: Step 3 uses "Exec gate / Dev gate / Maker gate" with parenthetical Pass/Fail
  descriptions per audience. "Each audience gate must independently pass." Full V-02
  formalism carried into V-05 base.
- C-29: Step 3 criteria name "the Step 0c exec/dev/maker voice contract" explicitly. Step 4
  names "the Step 0c voice contract for that audience" as the revision anchor. Both
  derivation and rewrite anchor name Step 0c explicitly.
- C-30: Inline step-pair gate labels `--- GATE 1 (0a→0b): Do not advance... ---` throughout
  Phase 0. COMPLETION INDEX Phase Gate Audit row matches: "Gate 1: 0a→0b | Gate 2: 0b→0c |
  Gate 3: 0c→0d".
- C-31: Step 0c contracts referenced in: (a) pitch section instructions ("Use Step 0c
  exec/dev/maker voice contract as anchor"), (b) gate Step 1 copy, (c) gate Step 3 criteria
  names ("frame of the Step 0c exec/dev/maker voice contract"), (d) gate Step 4 rewrite
  anchor ("Step 0c voice contract for that audience"). Doubly anchored in both production
  guidance AND gate enforcement criteria.

**Risk**: Highest structural complexity in this round. The COMPLETION INDEX restructuring into
four named sections (from V-03) plus the C-28/C-29 gate changes (from V-04) are each proven
independently. The co-presence risk is minimal because the COMPLETION INDEX restructuring
is strictly additive — the same information is present, now under section headers. The
voice gate modifications affect only Step 3 and Step 4 of the gate block. No existing
criterion has its evidence location disturbed. Predicted: 23/23 aspirational.

---

## Variation Summary

| ID | Primary Axis | Key Mechanism | Targets | Predicted Score (v7) | Risk |
|----|--------------|---------------|---------|----------------------|------|
| V-01 | C-28 gate formalism | "Exec gate / Dev gate / Maker gate" with parenthetical Pass/Fail descriptions; "each audience gate must independently pass" | C-28 | 21/23 asp = 99.1 | Single change at Step 3 labels; V-02 R6 proved this mechanism earns C-28 |
| V-02 | C-29 Step 0c naming | Gate criteria name "the Step 0c exec/dev/maker voice contract" explicitly; rewrite anchor names "Step 0c voice contract for that audience" | C-29 | 21/23 asp = 99.1 | Minimal wording addition; V-03 R6 proved this naming earns C-29 |
| V-03 | C-27 formal section header | COMPLETION INDEX restructured into four named sections with ### headers; "Voice Compliance Audit" as formally named section; preamble enumerates all four sections | C-27 | 21/23 asp = 99.1 (if V-05 R6 didn't already earn C-27) | COMPLETION INDEX restructuring is additive; section headers may clarify C-23 distinction rather than weaken it |
| V-04 | C-28 + C-29 combined | V-05 R6 base + per-audience gate labels with parenthetical Pass/Fail (C-28) + Step 0c explicitly named in criteria and rewrite anchor (C-29) | C-28 + C-29 | 23/23 asp = 100.0 | Two proven mechanisms combined; structurally independent; co-presence in Step 3 sentence is clean |
| V-05 | Full synthesis | V-04 + formal COMPLETION INDEX section headers (C-27 formal version); maximum evidence density for all five | C-27 + C-28 + C-29 + C-30 + C-31 | 23/23 asp = 100.0 | Highest complexity; each mechanism independent; COMPLETION INDEX restructuring from V-03 co-exists cleanly with V-04's gate changes |

**Predicted leaderboard**: V-04 = V-05 > V-01 = V-02 = V-03

V-04 and V-05 are both predicted to reach 23/23. V-04 is the minimal path to 23/23 (only two
targeted changes to R6 V-05 base). V-05 is the maximum-evidence path (adds formal section
classification for C-27 robustness). V-01, V-02, V-03 are each 21/23 predictions — they
isolate one of the remaining single-criterion mechanisms, confirming whether each earns
its target independently.

**The key R7 unlock**: R6 proved that C-20 can coexist with C-24, C-25, C-26 simultaneously
(V-05 R6 baseline). R7 asks whether the three mechanisms extracted from R6 as C-27, C-28,
C-29, C-30, C-31 can coexist in a single skill. R6 V-05 already holds C-30 and C-31. The
two remaining additions (C-28 gate formalism, C-29 Step 0c naming) are isolated changes at
a single structural location (gate Step 3 + Step 4 rewrite anchor). Their co-presence in
one sentence is the structural test of R7: "Does the Exec Version opening match the frame
of the Step 0c exec voice contract (outcomes/risk register)? Pass (...) / Fail (...)".
This single sentence carries C-28 (gate label + parenthetical verdict), C-29 (Step 0c
named as criteria source), and C-31 (contract as enforcement criterion) simultaneously.
