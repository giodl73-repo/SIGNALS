---
skill: quest-variate
skill_target: campaign-specify
round: 8
date: 2026-03-16
rubric: v8 (26 aspirational criteria, C-33 and C-34 are the new targets)
---

# Variations — campaign-specify / Round 8

Five complete, runnable skill body variations targeting the v8 rubric.
Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

**R7 diagnosis driving R8 axis choices:**

Under v8, the scoring formula is `(essential/5 * 60) + (rec/3 * 30) + (asp/26 * 10)`.
Four new criteria (C-27 tightened, C-32, C-33, C-34) were added or tightened in v8.

| Variation | Asp under v8 | Earned new | Missing new | Why |
|-----------|-------------|------------|-------------|-----|
| R7 V-01 | 21/26 | C-28 | C-27,C-29,C-32,C-33,C-34 | Per-audience gate formalism earns C-28; no formal Voice Compliance Audit section, no Step 0c naming, no per-audience audit rows, no contract-anchor in Pass parenthetical |
| R7 V-02 | 21/26 | C-29 | C-27,C-28,C-32,C-33,C-34 | Step 0c named in criteria earns C-29; no formal section header for audit, no gate formalism, no per-audience audit rows, no contract-anchor in Pass |
| R7 V-03 | 21/26 | C-27 | C-28,C-29,C-32,C-33,C-34 | Formal Voice Compliance Audit section header earns C-27; single-line combined result fails C-33; no gate formalism, no Step 0c naming, no compliance categorization declaration |
| R7 V-04 | 22/26 | C-28,C-29 | C-27,C-32,C-33,C-34 | Gate formalism + Step 0c naming; no formal audit section, no categorization declaration, no per-audience audit rows, no contract-anchor in Pass |
| R7 V-05 | 24/26 | C-27,C-28,C-29,C-32 | C-33,C-34 | Full synthesis earns four new criteria; Voice Compliance Audit section exists (C-27) and preamble declares categorical purpose (C-32); BUT audit section has single combined line — fails C-33; AND Pass parentheticals name behavioral tests without Step 0c attribution — fails C-34 |

**R8 gap**: R7 V-05 leads at 24/26. The two unearned criteria are:

- **C-33** (missing): V-05's `### Voice Compliance Audit` section contains a single line:
  `- Voice differentiation gate result: distinct / rewritten-to-distinct`
  C-33 requires that when both C-27 (formal audit section) and C-28 (per-audience gate
  verdicts) exist, the audit section records exec, dev, and maker results **separately**.
  A combined single-line result does not pass, regardless of whether it says "distinct."

- **C-34** (missing): V-05's gate Step 3 Pass conditions say:
  `Pass (opening names a business cost, risk, or revenue consequence)`.
  C-34 requires that when C-28 (parenthetical Pass/Fail criteria) and C-29 (Step 0c
  naming in gate criteria) both exist, the parenthetical **Pass condition** explicitly names
  the applicable Step 0c contract — e.g., `Pass (Step 0c exec voice contract satisfied:
  opening names a business cost, risk, or revenue consequence)`. Behavioral criteria
  without contract attribution in the Pass parenthetical do not pass.

The two mechanisms are structurally independent:
- C-33 is a COMPLETION INDEX change: expand single audit line → three per-audience verdict rows
- C-34 is a gate Step 3 change: add "Step 0c [audience] voice contract satisfied:" prefix inside each Pass parenthetical

| Axis | Mechanism | Targets |
|------|-----------|---------|
| C-33 per-audience audit rows (V-01 style) | Expand `### Voice Compliance Audit` single line to three rows: `- Exec verdict: [Pass / Fail]`, `- Dev verdict: [Pass / Fail]`, `- Maker verdict: [Pass / Fail]` | C-33 |
| C-34 contract anchor in Pass (V-02 style) | Prefix each Pass parenthetical with the Step 0c contract name: `Pass (Step 0c exec voice contract satisfied: ...)` | C-34 |
| C-33 with Step 0c attribution per row (V-03 style) | Three per-audience audit rows each naming the Step 0c contract verified | C-33 (with richer attribution) |
| C-33 + C-34 combined (V-04) | V-05 R7 base + per-audience audit rows (C-33) + contract anchor in Pass parenthetical (C-34); predicted 26/26 | C-33 + C-34 |
| Full synthesis (V-05) | V-04 + per-row Step 0c attribution in audit + bidirectional cross-reference between gate Step 3 and Voice Compliance Audit; maximum evidence density | C-33 + C-34 |

**Predicted ceiling**: V-04 or V-05 reaches 26/26. All five variations expected to hold
5/5 essential, 3/3 recommended, and C-09 through C-32 from R7 V-05 base.

---

## V-01 — Axis: C-33 Per-Audience Verdicts in Voice Compliance Audit

**Hypothesis**: R7 V-05 earns C-27 (formal Voice Compliance Audit section) and C-28
(per-audience gate verdicts) but not C-33 because the Voice Compliance Audit section
contains a single combined line rather than individual verdicts per audience. C-33 is
the interaction criterion: when both C-27 and C-28 are satisfied, the audit section
must record exec, dev, and maker results separately. The fix is minimal — expand the
single `- Voice differentiation gate result: distinct / rewritten-to-distinct` line into
three rows, one per audience. No gate changes. No preamble changes. Predicted: earns
C-33, misses C-34 = 25/26.

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
- Exec verdict: [Pass / Fail]
- Dev verdict: [Pass / Fail]
- Maker verdict: [Pass / Fail]
```

**Rubric targeting**:
- C-33: `### Voice Compliance Audit` section records three separate per-audience rows
  (`Exec verdict`, `Dev verdict`, `Maker verdict`) instead of the single combined line from
  R7. C-27 (formal section) + C-28 (per-audience gate verdicts) both hold. The audit section
  now records the same per-audience granularity the gate enforces. Combined single-line
  result replaced.
- C-27: Formal `### Voice Compliance Audit` section header preserved from R7 V-05. Preamble
  enumerates four named sections. Section header still present, now with richer content.
- C-28: Gate Step 3 "Exec gate / Dev gate / Maker gate" labels and parenthetical Pass/Fail
  descriptions preserved unchanged from R7 V-05.
- C-29: Gate Step 3 names "the Step 0c exec/dev/maker voice contract" as criteria source;
  Step 4 names "the Step 0c voice contract for that audience" as rewrite anchor. Unchanged.
- C-32: Preamble declares "Each section classifies a distinct category of compliance state."
  Unchanged from R7 V-05.
- C-34: Gap — Pass parentheticals still say `Pass (opening names a business cost...)` without
  Step 0c contract attribution. Not earned.

**Risk**: Single-point change to COMPLETION INDEX. The three per-audience verdict rows replace
one bullet line. All other content in the Voice Compliance Audit section is structurally
identical to R7 V-05. Risk of breaking C-23 (COMPLETION INDEX structurally distinct from
write gates) is nil — the section preamble explicitly distinguishes the COMPLETION INDEX from
gates. Predicted: 25/26.

---

## V-02 — Axis: C-34 Step 0c Contract Anchor in Gate Parenthetical Pass

**Hypothesis**: R7 V-05 earns C-28 (parenthetical Pass/Fail per audience) and C-29 (Step 0c
named as criteria source) but not C-34 because the parenthetical **Pass** condition names only
the behavioral test: `Pass (opening names a business cost, risk, or revenue consequence)`.
C-34 requires that the Step 0c contract name appear **inside** the parenthetical Pass
condition itself. The fix is equally minimal — prefix each Pass parenthetical with
"Step 0c [audience] voice contract satisfied:". The behavioral criteria stay identical;
the contract attribution is prepended. Voice Compliance Audit unchanged (single combined
line, so C-33 remains unearned). Predicted: earns C-34, misses C-33 = 25/26.

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
    Pass (Step 0c exec voice contract satisfied: opening names a business cost, risk,
      or revenue consequence) /
    Fail (opening does not satisfy the Step 0c exec voice contract: opens with product
      description, capability framing, or workflow framing)

  Dev gate: Does the Dev Version opening match the frame of the Step 0c dev voice
    contract (capability/friction register)?
    Pass (Step 0c dev voice contract satisfied: opening names a tool friction,
      workaround, or capability gap) /
    Fail (opening does not satisfy the Step 0c dev voice contract: opens with outcome/ROI
      framing or business consequence framing)

  Maker gate: Does the Maker Version opening match the frame of the Step 0c maker voice
    contract (jargon-free blocked-step register)?
    Pass (Step 0c maker voice contract satisfied: opening names a blocked, absent, or
      manual step in plain language, no jargon) /
    Fail (opening does not satisfy the Step 0c maker voice contract: opens with product
      description or technical jargon)

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
- C-34: Each audience gate's Pass parenthetical now begins with the Step 0c contract name:
  `Pass (Step 0c exec voice contract satisfied: ...)`. The Fail parenthetical symmetrically
  reads `Fail (opening does not satisfy the Step 0c exec voice contract: ...)`. Both the
  Pass and Fail sides name the applicable Step 0c contract. The contract attribution is
  embedded structurally inside the parenthetical verdict, not mentioned in surrounding text.
- C-28: Gate labels "Exec gate / Dev gate / Maker gate" preserved. Parenthetical Pass/Fail
  criteria remain per audience. The attribution addition strengthens rather than weakens the
  formalism. "Each audience gate must independently pass" still applies.
- C-29: Step 3 criteria still derive from "the Step 0c exec/dev/maker voice contract" as
  the named source. Step 4 rewrite anchor still names "the Step 0c voice contract for that
  audience." C-34 adds attribution inside Pass parentheticals without displacing C-29 source
  attribution in the gate criteria text.
- C-33: Gap — Voice Compliance Audit section still contains single combined line. Not earned.
- C-27, C-32: Formal section header and preamble categorization declaration unchanged.

**Risk**: The Pass parenthetical wording becomes slightly longer. Risk: excessive verbosity
could read as redundant given C-29 already names Step 0c in the gate criteria. However, C-34
is explicit that the contract name must appear inside the Pass condition itself — the gate
criteria text is not the Pass parenthetical. The two co-exist cleanly: one names the contract
as the source of pass criteria (C-29), the other names the contract as the satisfied entity
inside the Pass verdict (C-34). Predicted: 25/26.

---

## V-03 — Axis: C-33 with Step 0c Contract Attribution Per Audit Row

**Hypothesis**: V-01 earns C-33 by expanding the Voice Compliance Audit to three separate
verdict rows. V-03 tests a richer form of the same mechanism: each audit row names the
Step 0c contract it verified, creating a bidirectional record (gate Step 3 names the contract
as the pass criterion; audit rows name the contract as the verified entity). This richer
form should earn C-33 at least as reliably as V-01, and may strengthen C-27 evidence by
making the audit section's categorical purpose more explicit. Single change from R7 V-05:
expand Voice Compliance Audit from one line to three rows with contract attribution. Gate
Step 3 unchanged (C-34 not targeted). Predicted: earns C-33 = 25/26.

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
- Exec verdict: [Pass / Fail] — Step 0c exec voice contract verified
- Dev verdict: [Pass / Fail] — Step 0c dev voice contract verified
- Maker verdict: [Pass / Fail] — Step 0c maker voice contract verified
```

**Rubric targeting**:
- C-33: Three separate per-audience verdict rows, each naming the Step 0c contract
  verified. Richer than V-01's bare `[Pass / Fail]` rows — contract attribution makes
  the per-audience structure unmistakable. C-27 (formal section) + C-28 (per-audience
  gate) coexist; audit section records three separate results rather than one combined line.
- C-27: `### Voice Compliance Audit` section header preserved. Section now contains three
  content rows, making the section's categorical purpose more substantive than a single line.
- C-32: Preamble "Each section classifies a distinct category of compliance state."
  Preserved. Voice Compliance Audit is now more clearly classified (per-audience, per-contract).
- C-34: Gap — Pass parentheticals unchanged from R7 V-05. Step 0c attribution per audit
  row is a COMPLETION INDEX record, not a gate Pass condition. Does not earn C-34.

**Risk**: The per-row Step 0c attribution adds 3 short annotations. Risk of conflating the
audit record with the gate enforcement criteria is low because: (a) COMPLETION INDEX preamble
explicitly distinguishes itself from gates, (b) the audit rows say "verified" (past tense
completion record), not "Pass condition" (gate enforcement). Predicted: 25/26.

---

## V-04 — Combined: C-33 Per-Audience Audit Rows + C-34 Contract Anchor in Pass

**Hypothesis**: V-01 isolates C-33 (three per-audience verdict rows in Voice Compliance Audit).
V-02 isolates C-34 (Step 0c contract name inside Pass parenthetical). Each earns its single
target at 25/26. Combining both mechanisms into R7 V-05 base should earn both criteria
simultaneously, reaching 26/26. The two changes are at different structural locations:
C-33 change is in COMPLETION INDEX Voice Compliance Audit section; C-34 change is in Phase 3
gate Step 3 Pass parentheticals. They do not share any text location and cannot interfere.
The co-presence test: can a gate that says `Pass (Step 0c exec voice contract satisfied: ...)`
be reconciled with an audit section that says `Exec verdict: [Pass / Fail]`? Yes — the gate
enforces the criterion at execution time; the audit records the result afterward. No
criterion is disturbed by the addition of the other mechanism. Predicted: 26/26.

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
    Pass (Step 0c exec voice contract satisfied: opening names a business cost, risk,
      or revenue consequence) /
    Fail (opening does not satisfy the Step 0c exec voice contract: opens with product
      description, capability framing, or workflow framing)

  Dev gate: Does the Dev Version opening match the frame of the Step 0c dev voice
    contract (capability/friction register)?
    Pass (Step 0c dev voice contract satisfied: opening names a tool friction,
      workaround, or capability gap) /
    Fail (opening does not satisfy the Step 0c dev voice contract: opens with outcome/ROI
      framing or business consequence framing)

  Maker gate: Does the Maker Version opening match the frame of the Step 0c maker voice
    contract (jargon-free blocked-step register)?
    Pass (Step 0c maker voice contract satisfied: opening names a blocked, absent, or
      manual step in plain language, no jargon) /
    Fail (opening does not satisfy the Step 0c maker voice contract: opens with product
      description or technical jargon)

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
- Exec verdict: [Pass / Fail]
- Dev verdict: [Pass / Fail]
- Maker verdict: [Pass / Fail]
```

**Rubric targeting**:
- C-33: Three per-audience verdict rows in `### Voice Compliance Audit`. Combined single-line
  eliminated. Each audience recorded separately: `Exec verdict`, `Dev verdict`, `Maker verdict`.
  C-27 (formal section) and C-28 (per-audience gate) both present → audit records
  per-audience granularity. Earns C-33.
- C-34: Pass parenthetical for each audience gate now begins with the Step 0c contract name:
  `Pass (Step 0c exec voice contract satisfied: ...)`. Contract attribution is inside the
  parenthetical Pass condition itself, not in surrounding text. The Fail parenthetical mirrors:
  `Fail (opening does not satisfy the Step 0c exec voice contract: ...)`. Earns C-34.
- C-27: `### Voice Compliance Audit` section header unchanged. Preamble enumerates four named
  sections. Formal section structure unambiguous.
- C-28: Gate labels "Exec gate / Dev gate / Maker gate" and independent per-audience
  Pass/Fail verdicts preserved. C-34 attribution adds contract name inside Pass — does not
  remove or weaken the parenthetical formalism.
- C-29: Gate Step 3 criteria name "the Step 0c exec/dev/maker voice contract" as the source
  of pass criteria. Step 4 names "the Step 0c voice contract for that audience" as rewrite
  anchor. Both derivation and rewrite attribution unchanged.
- C-32: Preamble "Each section classifies a distinct category of compliance state." Unchanged.
- C-30, C-31: Inline step-pair gate labels and doubly-anchored contracts preserved throughout.

**Risk**: Two independent changes, each proven in single-axis variations. The co-presence
point: gate Step 3 now reads `Pass (Step 0c exec voice contract satisfied: opening names
a business cost...)` AND Voice Compliance Audit reads `Exec verdict: [Pass / Fail]`.
These are structurally disjoint — one is inside the gate enforcement block; the other is
inside the COMPLETION INDEX post-execution record. The preamble explicitly distinguishes the
two. No criterion evidence location is disturbed by either addition. Predicted: 26/26.

---

## V-05 — Full Synthesis: C-33 + C-34 + Maximum Evidence Density

**Hypothesis**: V-04 is the predicted 26/26 minimal path. V-05 tests whether adding
V-03's richer audit row attribution (each row names the Step 0c contract verified) to
V-04's combined structure increases robustness without introducing interference. The
structural difference from V-04: Voice Compliance Audit rows include Step 0c contract
attribution ("Step 0c exec voice contract verified"), creating bidirectional traceability
between the gate enforcement criterion (Step 3: names the contract as the Pass source)
and the audit record (Voice Compliance Audit: names the contract as the verified entity).
If V-04 already earns C-33, V-05 earns it with higher evidence density. If V-04's bare
`[Pass / Fail]` rows are ambiguously interpreted, V-03's contract attribution is the
tiebreaker. In either case, V-05 is the maximum evidence density variation for all
26 criteria simultaneously.

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
    Pass (Step 0c exec voice contract satisfied: opening names a business cost, risk,
      or revenue consequence) /
    Fail (opening does not satisfy the Step 0c exec voice contract: opens with product
      description, capability framing, or workflow framing)

  Dev gate: Does the Dev Version opening match the frame of the Step 0c dev voice
    contract (capability/friction register)?
    Pass (Step 0c dev voice contract satisfied: opening names a tool friction,
      workaround, or capability gap) /
    Fail (opening does not satisfy the Step 0c dev voice contract: opens with outcome/ROI
      framing or business consequence framing)

  Maker gate: Does the Maker Version opening match the frame of the Step 0c maker voice
    contract (jargon-free blocked-step register)?
    Pass (Step 0c maker voice contract satisfied: opening names a blocked, absent, or
      manual step in plain language, no jargon) /
    Fail (opening does not satisfy the Step 0c maker voice contract: opens with product
      description or technical jargon)

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
- Exec verdict: [Pass / Fail] — Step 0c exec voice contract verified
- Dev verdict: [Pass / Fail] — Step 0c dev voice contract verified
- Maker verdict: [Pass / Fail] — Step 0c maker voice contract verified
```

**Rubric targeting**:
- C-33: Three per-audience verdict rows in `### Voice Compliance Audit`, each naming the
  Step 0c contract verified. The per-audience granularity is explicit: separate rows for exec,
  dev, and maker, matching the per-audience gate verdict structure from Step 3. C-27 (formal
  section) + C-28 (per-audience gate) both present. Audit section records three separate
  results, not a combined single line. Earns C-33.
- C-34: Pass parenthetical for each audience gate names the applicable Step 0c contract:
  `Pass (Step 0c exec voice contract satisfied: opening names a business cost, risk, or
  revenue consequence)`. The contract name is embedded structurally inside the parenthetical
  Pass condition, not in the gate criteria text above it. Earns C-34.
- C-27: `### Voice Compliance Audit` formal section header present. Preamble enumerates
  four named sections. Section header preserved and strengthened by three-row content.
- C-28: "Exec gate / Dev gate / Maker gate" labels. Parenthetical Pass/Fail per audience.
  "Each audience gate must independently pass." C-34 attribution inside Pass parenthetical
  strengthens rather than replaces the formalism.
- C-29: Step 3 gate criteria name "the Step 0c exec/dev/maker voice contract" explicitly.
  Step 4 rewrite anchor: "the Step 0c voice contract for that audience." C-34 adds contract
  attribution inside Pass parentheticals — distinct from C-29's attribution in gate criteria
  text. Both co-present, structurally independent.
- C-32: Preamble "Each section classifies a distinct category of compliance state." Voice
  Compliance Audit now has richer content (three rows with contract attribution) that
  reinforces the categorical classification the preamble declares.
- C-30: Inline step-pair labels `--- GATE 1 (0a→0b): Do not advance... ---` throughout
  Phase 0. Phase Gate Audit row matches gate chain. Unchanged.
- C-31: Step 0c contracts referenced in (a) pitch section instructions, (b) gate Step 1
  copy, (c) gate Step 3 criteria names, (d) gate Step 4 rewrite anchor, AND now (e) Voice
  Compliance Audit rows ("Step 0c [audience] voice contract verified"). Five-point anchoring
  — the richest Step 0c contract evidence density in the series.

**Risk**: Highest evidence density of all R8 variations. Three structural layers name the
Step 0c contracts: the pitch section instructions (production), the gate Step 3 criteria
(enforcement), the gate Step 4 rewrite anchor (recovery), the Pass parentheticals (C-34),
and the audit rows (C-33). Each layer serves a different structural function; none overlap
or conflict. The only risk is that the density of Step 0c references is read as redundant
rather than reinforcing — but redundancy in different structural roles is the evidence
pattern the rubric rewards. Predicted: 26/26 aspirational.

---

## Variation Summary

| ID | Primary Axis | Key Mechanism | Targets | Predicted Score (v8) | Risk |
|----|--------------|---------------|---------|----------------------|------|
| V-01 | C-33 per-audience audit rows | Expand `### Voice Compliance Audit` from single combined line to three rows: `Exec verdict / Dev verdict / Maker verdict` | C-33 | 25/26 asp = 99.6 | Single-point COMPLETION INDEX change; minimal structural risk |
| V-02 | C-34 contract anchor in Pass | Prefix each Pass parenthetical with "Step 0c [audience] voice contract satisfied:" | C-34 | 25/26 asp = 99.6 | Wording addition inside parenthetical; co-exists cleanly with C-29 contract naming in criteria text |
| V-03 | C-33 with contract attribution | Three per-audience audit rows each naming "Step 0c [audience] voice contract verified" | C-33 (richer) | 25/26 asp = 99.6 | Stronger C-33 evidence than V-01; V-03 attribution is post-execution record, not gate enforcement |
| V-04 | C-33 + C-34 combined | V-05 R7 base + three per-audience audit rows (C-33) + Step 0c contract name in Pass parenthetical (C-34) | C-33 + C-34 | 26/26 asp = 100.0 | Two proven mechanisms combined; structurally disjoint change locations; co-presence clean |
| V-05 | Full synthesis | V-04 + V-03-style contract attribution per audit row; maximum evidence density across all 26 criteria | C-33 + C-34 | 26/26 asp = 100.0 | Highest complexity; each mechanism independent; five-point Step 0c anchoring reinforces without conflicting |

**Predicted leaderboard**: V-04 = V-05 > V-01 = V-02 = V-03

V-04 is the minimal path to 26/26: two targeted changes to R7 V-05 base, each at an
independent structural location. V-05 is the maximum-evidence path: V-04's two changes plus
V-03's richer audit row attribution. V-01, V-02, V-03 each isolate one new mechanism at
25/26, confirming that the mechanism independently earns its target criterion.

**The key R8 unlock**: R7 proved that C-27, C-28, C-29, C-32 can coexist in a single skill
(V-05 R7 at 24/26). R8 asks whether C-33 (per-audience audit rows) and C-34 (contract name
in Pass parenthetical) can be added to that structure without disturbing the 24 already-earned
criteria. The two R8 changes are at disjoint structural locations — COMPLETION INDEX Voice
Compliance Audit (C-33) and Phase 3 gate Step 3 Pass parentheticals (C-34) — and neither
touches any text that carries evidence for the 24 existing criteria. The predicted 26/26 is
structurally well-grounded.
