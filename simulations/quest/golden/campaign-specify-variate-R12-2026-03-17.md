---
skill: quest-variate
skill_target: campaign-specify
round: 12
date: 2026-03-17
rubric: v12 (33 aspirational criteria; C-40 and C-41 established by R11 V-05)
---

# Variations — campaign-specify / Round 12

Five complete, runnable skill body variations targeting the v12 rubric.
Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

**R11 diagnosis driving R12 axis choices:**

Under v12, two new criteria were confirmed on top of the v11 baseline:

- **C-40** — Pre-table explicit instruction reinforcing audience-discriminating cell values.
  In R11 V-02, the instruction block before the VCA table names the audience-discriminator
  requirement directly ("Step 0c contract name with the audience identifier embedded").
  In R11 V-05, the equivalent mechanism: "Fill in the Step 0c Contract Verified column with
  the exact Step 0c contract name followed by 'satisfied'. A row without a named contract
  does not satisfy this section." Template cell values alone (C-38) do not pass C-40.

- **C-41** — Explicit COLUMN-HEADER REQUIREMENT statement. First seen in R11 V-05:
  "COLUMN-HEADER REQUIREMENT: The third column header must read exactly 'Step 0c Contract
  Verified'." The column header in the template alone (C-39) does not pass C-41.

R11 V-05 is the first 33/33 ceiling. It carries both dual-mechanism patterns:
- C-38 via template cell values + C-40 via pre-table instruction (two mechanisms for the cells)
- C-39 via template column header + C-41 via COLUMN-HEADER REQUIREMENT statement (two mechanisms for the header)

R11 V-05 also introduces a FORWARD AUDIT NOTICE in Step 0c creating forward binding from
Step 0c → VCA. This structural element has not been codified as a criterion.

**R12 question set:**

R11 V-05 is the first ceiling. R12 tests ceiling stability and probes for v13 excellence patterns.

1. Does a compressed-imperative phrasing register preserve 33/33? (V-01 — stability test)
2. Does a backward reference in the VCA explicitly naming Step 0c as the authoritative
   source ("contracts defined in Step 0c; text must match Step 0c exactly") create a v13
   pattern beyond forward binding alone? (V-02)
3. Does an explicit STEP 0C CONTRACT ANCHOR block at Phase 3 entry — copying contracts
   before pitch writing begins — create a v13 pattern? (V-03)
4. Do V-02 + V-03 axes coexist without structural conflict while preserving 33/33? (V-04)
5. Do V-02 + V-03 + a named CITATION FORM REQUIREMENT (an explicit labeled requirement
   for verbatim citation paste — the C-41 analog for the stability citation) produce v13
   patterns beyond what individual axes provide? (V-05)

| Variation | Axis | C-40 | C-41 | Predicted |
|-----------|------|------|------|-----------|
| V-01 | Phrasing register — compressed imperative | Preserved | Preserved | 33/33 |
| V-02 | Bidirectional VCA binding — STEP 0C SOURCE BINDING backward reference | Preserved | Preserved | 33/33 + v13 watch |
| V-03 | Phase 3 contract re-anchor — STEP 0C CONTRACT ANCHOR at Phase 3 entry | Preserved | Preserved | 33/33 + v13 watch |
| V-04 | Combined: V-02 bidirectional binding + V-03 re-anchor | Preserved | Preserved | 33/33 + v13 watch |
| V-05 | Combined: V-02 + V-03 + CITATION FORM REQUIREMENT (new axis) | Preserved | Preserved | 33/33 + v13 watch |

All five preserve C-40 and C-41 from R11 V-05. The v12 ceiling is the baseline; R12 probes above it.

---

## V-01 — Axis: Phrasing Register — Compressed Imperative

**Hypothesis**: R11 V-05 uses a formal structured register with narrative explanation in phase
headers, gate labels, and pre-table instruction text. V-01 tests whether a compressed
imperative-only register — removing explanatory preamble from phase headers and gate labels,
keeping only direct commands — preserves 33/33. This is a ceiling stability test: if the
dual-mechanism patterns (C-40, C-41) survive phrasing compression, the v12 ceiling is
form-independent. All structural mechanics, gate chain, template cell values, FORWARD AUDIT
NOTICE, COLUMN-HEADER REQUIREMENT, and pre-table instruction are preserved unchanged.
Predicted: 33/33.

```
Run the campaign-specify skill for: {{topic}}

Produce three artifacts: spec, proposal, pitch. Execute phases 0–3 in order.
Complete each phase before starting the next. Write each artifact to disk before
the next phase begins.

---

## Phase 0 — Audience Foundation

Four steps. Gate chain: Gate 1 (0a→0b) | Gate 2 (0b→0c) | Gate 3 (0c→0d). Step 0d terminal.

**Step 0a — Inertia Costs**

What each audience LOSES if {{topic}} does not ship:

Exec inertia cost: [Revenue exposure, competitive gap, or risk. Name the consequence.
Quantify if possible.]

Dev inertia cost: [Workaround or capability gap. Name the friction. Estimate recurring cost.]

Maker inertia cost: [Blocked workflow step. Name the step. What does the maker do today
instead?]

--- GATE 1 (0a→0b): All three inertia costs must be complete before Step 0b. ---

**Step 0b — Stability Citation Record**

Evaluate whether the cost of Do Nothing is stable or worsening. Produce the STABILITY
CITATION RECORD using Form A or Form B. This record will be pasted verbatim into Phase 2.

FORM A (worsening): "Do Nothing is not stable: [specific mechanism and timeline]."
FORM B (stable): "Do Nothing is stable: [rationale]."

STABILITY CITATION RECORD:
[Complete Form A or Form B sentence — verbatim-ready]

A record containing only a tag ("worsening" / "stable") without mechanism or rationale fails.
Full sentence required.

--- GATE 2 (0b→0c): STABILITY CITATION RECORD must be complete before Step 0c. ---

**Step 0c — Voice Contracts**

One sentence per audience, grounded in Steps 0a and 0b:

Exec voice: [Outcomes/risk framing — reference exec inertia cost and stability trajectory]
Dev voice: [Capability/friction framing — reference dev inertia cost]
Maker voice: [Workflow framing — plain language, reference maker inertia cost]

FORWARD AUDIT NOTICE: These three voice contracts are the compliance criteria for the
COMPLETION INDEX Voice Compliance Audit. Each contract will be verified by its exact name
in the "Step 0c Contract Verified" column. Do not alter contract phrasing — the column
values must match the Step 0c names exactly.

--- GATE 3 (0c→0d): All three voice contracts must be written before Step 0d. ---

**Step 0d — Scout Pull** [TERMINAL]

Glob `simulations/scout/**/*.md` for {{topic}}. For each file found: path, one-sentence
summary, artifact served (spec / proposal / pitch).

If no scout files: record "no scout signals — proceeding without" and continue.

[Phase 0 complete. Gates 1–3 passed. Proceed to Phase 1.]

---

## Phase 1 — Technical Spec

Pull from `simulations/scout/` broadly. Note Step 0d files used.

Six sections required. No skipping. No merging.

### Overview
What {{topic}} does and why it exists.

### User Problem
Problem today. Reference dev and maker inertia costs from Step 0a directly.

### Proposed Solution
What {{topic}} does. Use scout-requirements or scout-feasibility signals from Step 0d.

### Constraints
Three minimum: technical, scope, platform.

### Open Questions
Three named ambiguities minimum.

### Self-Review
One named gap minimum. "No gaps found" fails.

**>> SPEC WRITE GATE <<**
Save to: `simulations/draft/specs/{{topic}}-spec-{{date}}.md`
File must exist on disk before Phase 2 begins.

---

## Phase 2 — Business Proposal

Pull from `simulations/scout/scout-feasibility/` before writing. Note files used.

Three options minimum. Option 1 must be named **Do Nothing**.

For each option: description, pros, cons, risk, effort.

### Recommendation

We recommend [chosen option].

#### Defeating Do Nothing

Do Nothing perpetuates [most decisive Step 0a inertia cost — name audience and specific cost].

[PASTE STABILITY CITATION RECORD FROM STEP 0b VERBATIM. No summary. No paraphrase.
Character for character.]

We choose to act because [why this cost trajectory is not acceptable].

#### Defeating [Other Option Name]

We prefer [chosen] over [other] because [specific trade-off traceable to risk, effort,
or cons — not a preference statement].

Note: Defeating Do Nothing must contain the STABILITY CITATION RECORD verbatim. A combined
recommendation paragraph does not satisfy C-16. A block without the verbatim record does
not satisfy C-17 or C-21.

**>> PROPOSAL WRITE GATE <<**
Save to: `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md`
File must exist on disk before Phase 3 begins.

---

## Phase 3 — Executive Pitch

Pull from `simulations/scout/scout-positioning/` before writing. Note files used.

Write all four sections below. Do not save the pitch until the voice differentiation gate passes.

### Exec Version
Lead with exec inertia cost. Use Step 0c exec voice contract as anchor.
Structure: [exec cost hook] → [what changes] → [outcome/ROI] → [call to action].
Do not open with a product description.

### Dev Version
Lead with dev inertia cost. Use Step 0c dev voice contract as anchor.
Structure: [friction hook] → [what you can now do] → [capability unlocked] → [call to action].
Do not open with outcomes/ROI framing.

### Maker Version
Lead with maker inertia cost. Use Step 0c maker voice contract as anchor.
Plain language, no jargon.
Structure: [blocked step hook] → [what you can now do] → [why it matters] → [call to action].

### Anti-Positioning
3–5 "This is not..." statements. Structurally separate from the three audience versions.

**>> VOICE DIFFERENTIATION GATE — Step 0c Contract Check (required before saving pitch) <<**

Step 1 — Copy Step 0c voice contracts:
  Step 0c exec voice contract: [exec sentence from Step 0c]
  Step 0c dev voice contract: [dev sentence from Step 0c]
  Step 0c maker voice contract: [maker sentence from Step 0c]

Step 2 — Extract opening sentence from each pitch version:
  Exec opening: [first sentence of Exec Version]
  Dev opening: [first sentence of Dev Version]
  Maker opening: [first sentence of Maker Version]

Step 3 — Per-audience gate (each must independently pass):

  Exec gate:
    Pass (Step 0c exec voice contract satisfied: opening names a business cost, risk,
      or revenue consequence) /
    Fail (opening does not satisfy Step 0c exec voice contract: opens with product
      description, capability framing, or workflow framing)

  Dev gate:
    Pass (Step 0c dev voice contract satisfied: opening names a tool friction,
      workaround, or capability gap) /
    Fail (opening does not satisfy Step 0c dev voice contract: opens with outcome/ROI
      or business consequence framing)

  Maker gate:
    Pass (Step 0c maker voice contract satisfied: opening names a blocked, absent, or
      manual step in plain language, no jargon) /
    Fail (opening does not satisfy Step 0c maker voice contract: opens with product
      description or technical jargon)

Step 4 — Resolution:
  Any Fail: rewrite the failing version anchored to its Step 0c contract. Re-run Steps 2–3.
    Do not save until all three gates Pass.
  All Pass: proceed to PITCH WRITE GATE.

**>> PITCH WRITE GATE <<**
Save to: `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`
File must exist on disk. Do not emit COMPLETION INDEX until it exists.

---

## COMPLETION INDEX

[Emitted after all write gates, voice differentiation gate, and recovery steps are complete.
Four named sections: Artifact Existence Record, Phase Gate Audit, Citation Audit, Voice
Compliance Audit.]

### Artifact Existence Record

| Artifact | Path | Status |
|----------|------|--------|
| Spec | `simulations/draft/specs/{{topic}}-spec-{{date}}.md` | [exists / missing] |
| Proposal | `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md` | [exists / missing] |
| Pitch | `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md` | [exists / missing] |

All three must show "exists." Any "missing": write now, then update the row.

### Phase Gate Audit
- Scout files used per phase
- Phase 0 inertia costs confirmed (all three audiences)
- Phase 0 gate chain: 3 gates passed (Gate 1: 0a→0b | Gate 2: 0b→0c | Gate 3: 0c→0d)

### Citation Audit
- STABILITY CITATION RECORD form used: Form A / Form B
- STABILITY CITATION RECORD pasted verbatim in Defeating Do Nothing block:
  CITATION CONFIRMED / CITATION MISSING
  (If CITATION MISSING: return to Phase 2 and paste before stopping.)
- Defeating Do Nothing block: separate labeled header: yes / no

### Voice Compliance Audit

COLUMN-HEADER REQUIREMENT: The third column header must read exactly "Step 0c Contract
Verified". A header reading "Contract Check", "Voice Contract", "Verified", or any other
label does not pass.

Record the verdict for each audience below. Fill in the Step 0c Contract Verified column
with the exact Step 0c contract name followed by "satisfied". A row without a named
contract in the verification column does not satisfy this section.

| Audience | Verdict | Step 0c Contract Verified |
|----------|---------|--------------------------|
| Exec | [Pass / Fail] | Step 0c exec voice contract satisfied |
| Dev | [Pass / Fail] | Step 0c dev voice contract satisfied |
| Maker | [Pass / Fail] | Step 0c maker voice contract satisfied |
```

**Rubric targeting**:
- C-40: Pre-table instruction "Fill in the Step 0c Contract Verified column with the exact
  Step 0c contract name followed by 'satisfied'. A row without a named contract does not
  satisfy this section." Compressed phrasing preserves the instruction. Earns C-40.
- C-41: COLUMN-HEADER REQUIREMENT statement unchanged from R11 V-05. Earns C-41.
- C-38: Template cell values carry audience identifier + "satisfied". Earns C-38.
- C-39: Column header "Step 0c Contract Verified" in template. Earns C-39.
- C-34/C-36/C-37: Gate parentheticals and table format preserved. All earn.
- FORWARD AUDIT NOTICE in Step 0c: preserved unchanged. No new criterion expected.
- V12 watch: phrasing compression does not degrade structural mechanics. 33/33 expected.

---

## V-02 — Axis: Bidirectional VCA Binding — STEP 0C SOURCE BINDING Backward Reference

**Hypothesis**: R11 V-05 creates forward binding from Step 0c to the VCA via the FORWARD
AUDIT NOTICE: "These contracts are the compliance criteria for the COMPLETION INDEX Voice
Compliance Audit. Each contract will be verified by its exact name in the Step 0c Contract
Verified column." This forward reference makes the binding visible at authoring time
(Step 0c). V-02 adds the corresponding backward reference at audit time: a named block
in the Voice Compliance Audit — STEP 0C SOURCE BINDING — that explicitly names Step 0c
as the authoritative source and requires the cell text to match Step 0c exactly. The
hypothesis: bidirectional binding (forward from Step 0c → VCA plus backward from VCA →
Step 0c) creates a v13 excellence pattern distinct from the forward reference alone.
The backward reference does not restate the contracts — it names the source and enforces
conformance. All C-40/C-41 mechanisms are preserved. Predicted: 33/33 + v13 watch.

```
Run the campaign-specify skill for: {{topic}}

Produce three artifacts: spec, proposal, pitch. Execute phases 0–3 in order.
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

Evaluate whether the cost of Do Nothing is stable or worsening. Produce the STABILITY
CITATION RECORD using one of the two forms below. This record will be pasted verbatim
into the Phase 2 Defeating Do Nothing block.

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

FORWARD AUDIT NOTICE: These three voice contracts are the compliance criteria for the
COMPLETION INDEX Voice Compliance Audit. Each contract will be verified by its exact name
in the "Step 0c Contract Verified" column of the audit table. Do not alter the contract
phrasing between here and the audit — the column values must match the names used in
Step 0c.

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
complete. Four named sections: Artifact Existence Record, Phase Gate Audit, Citation
Audit, Voice Compliance Audit.]

### Artifact Existence Record

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

STEP 0C SOURCE BINDING: The three voice contracts verified in this table were authored in
Step 0c above. This audit table does not redefine the contracts — it verifies conformance
to the Step 0c source. The text in the "Step 0c Contract Verified" column must match the
exact contract names as written in Step 0c. Do not rephrase. Do not generalize. The Step 0c
source text is authoritative; any deviation from the Step 0c phrasing constitutes a
verification failure even if the cell value is otherwise complete.

COLUMN-HEADER REQUIREMENT: The third column header must read exactly "Step 0c Contract
Verified". A header reading "Contract Check", "Voice Contract", "Verified", or any label
other than "Step 0c Contract Verified" does not pass.

Record the verdict for each audience in the table below. Fill in the Step 0c Contract
Verified column with the exact Step 0c contract name followed by "satisfied".
A row without a named contract in the verification column does not satisfy this section.

| Audience | Verdict | Step 0c Contract Verified |
|----------|---------|--------------------------|
| Exec | [Pass / Fail] | Step 0c exec voice contract satisfied |
| Dev | [Pass / Fail] | Step 0c dev voice contract satisfied |
| Maker | [Pass / Fail] | Step 0c maker voice contract satisfied |
```

**Rubric targeting**:
- C-40: Pre-table instruction "Fill in the Step 0c Contract Verified column with the exact
  Step 0c contract name followed by 'satisfied'. A row without a named contract does not
  satisfy this section." Unchanged from R11 V-05. Earns C-40.
- C-41: COLUMN-HEADER REQUIREMENT statement unchanged from R11 V-05. Earns C-41.
- C-38/C-39/C-34/C-36/C-37: All unchanged from R11 V-05. All earn.
- STEP 0C SOURCE BINDING (new): Named block before COLUMN-HEADER REQUIREMENT explicitly
  names Step 0c as the authoritative source and requires exact conformance. This is the
  backward reference from VCA → Step 0c, pairing with the FORWARD AUDIT NOTICE (Step 0c
  → VCA). V13 watch: "VCA carries explicit source-binding statement naming Step 0c as
  authoritative — deviation from Step 0c phrasing constitutes verification failure."

---

## V-03 — Axis: Phase 3 Contract Re-Anchor — STEP 0C CONTRACT ANCHOR Block at Phase 3 Entry

**Hypothesis**: In R11 V-05, Step 0c voice contracts appear at two structural positions:
(1) definition in Step 0c, (2) audit in the VCA. The FORWARD AUDIT NOTICE in Step 0c names
the VCA as the destination. But Phase 3 — where the contracts are used to anchor pitch writing
— does not include a structural moment that copies the contracts before use. V-03 adds a
named STEP 0C CONTRACT ANCHOR block at Phase 3 entry, before any pitch versions are written,
requiring the author to copy all three Step 0c contracts verbatim before beginning pitch
writing. The hypothesis: making contracts structurally present at the point of use (Phase 3
start) — not only at definition (Step 0c) and audit (VCA) — creates a v13 excellence
pattern: "Phase 3 carries an explicit contract re-anchor block that copies Step 0c contracts
before pitch writing begins." All C-40/C-41 mechanisms preserved. Predicted: 33/33 + v13 watch.

```
Run the campaign-specify skill for: {{topic}}

Produce three artifacts: spec, proposal, pitch. Execute phases 0–3 in order.
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

Evaluate whether the cost of Do Nothing is stable or worsening. Produce the STABILITY
CITATION RECORD using one of the two forms below. This record will be pasted verbatim
into the Phase 2 Defeating Do Nothing block.

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

FORWARD AUDIT NOTICE: These three voice contracts are the compliance criteria for the
COMPLETION INDEX Voice Compliance Audit. Each contract will be verified by its exact name
in the "Step 0c Contract Verified" column of the audit table. Do not alter the contract
phrasing between here and the audit — the column values must match the names used in
Step 0c.

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

**STEP 0C CONTRACT ANCHOR**

Before writing any pitch version, copy the three Step 0c voice contracts here:

Step 0c exec voice contract: [exact text from Step 0c — do not paraphrase or generalize]
Step 0c dev voice contract: [exact text from Step 0c — do not paraphrase or generalize]
Step 0c maker voice contract: [exact text from Step 0c — do not paraphrase or generalize]

These are the anchor sentences. Each pitch version must open with a hook that satisfies its
named contract. Do not begin writing Exec Version, Dev Version, or Maker Version until this
anchor block is complete.

--- ANCHOR GATE: Complete the STEP 0C CONTRACT ANCHOR before writing any pitch version. ---

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
complete. Four named sections: Artifact Existence Record, Phase Gate Audit, Citation
Audit, Voice Compliance Audit.]

### Artifact Existence Record

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

COLUMN-HEADER REQUIREMENT: The third column header must read exactly "Step 0c Contract
Verified". A header reading "Contract Check", "Voice Contract", "Verified", or any label
other than "Step 0c Contract Verified" does not pass.

Record the verdict for each audience in the table below. Fill in the Step 0c Contract
Verified column with the exact Step 0c contract name followed by "satisfied".
A row without a named contract in the verification column does not satisfy this section.

| Audience | Verdict | Step 0c Contract Verified |
|----------|---------|--------------------------|
| Exec | [Pass / Fail] | Step 0c exec voice contract satisfied |
| Dev | [Pass / Fail] | Step 0c dev voice contract satisfied |
| Maker | [Pass / Fail] | Step 0c maker voice contract satisfied |
```

**Rubric targeting**:
- C-40/C-41/C-38/C-39/C-34/C-36/C-37: All unchanged from R11 V-05. All earn.
- STEP 0C CONTRACT ANCHOR (new): Named block at Phase 3 entry, before any pitch version
  is written, requiring verbatim copy of all three Step 0c contracts. The ANCHOR GATE
  enforces completion before pitch writing begins. V13 watch: "Phase 3 carries an explicit
  named contract re-anchor block that copies Step 0c contracts before pitch writing begins."
- The contract anchor creates a third structural position for the contracts (definition in
  Step 0c, anchor in Phase 3 entry, audit in VCA) — testing whether this three-position
  pattern is an excellence signal beyond the two-position pattern in R11 V-05.

---

## V-04 — Combined: Bidirectional VCA Binding (V-02) + Phase 3 Contract Re-Anchor (V-03)

**Hypothesis**: V-02 adds backward binding at audit time (VCA → Step 0c via STEP 0C SOURCE
BINDING). V-03 adds contract re-anchoring at use time (Phase 3 entry via STEP 0C CONTRACT
ANCHOR). V-04 combines both. The combined prompt has three structural positions where Step 0c
contracts are explicitly named and their source is enforced: (1) definition with forward
notice (Step 0c), (2) re-anchor before use (Phase 3 entry), (3) backward reference at audit
(VCA). The hypothesis: the three-position naming pattern — define, re-anchor, verify — may
itself constitute a v13 excellence signal independent of any one position alone, and the two
new structural blocks coexist without conflict. Predicted: 33/33 + v13 watch.

```
Run the campaign-specify skill for: {{topic}}

Produce three artifacts: spec, proposal, pitch. Execute phases 0–3 in order.
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

Evaluate whether the cost of Do Nothing is stable or worsening. Produce the STABILITY
CITATION RECORD using one of the two forms below. This record will be pasted verbatim
into the Phase 2 Defeating Do Nothing block.

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

FORWARD AUDIT NOTICE: These three voice contracts are the compliance criteria for the
COMPLETION INDEX Voice Compliance Audit. Each contract will be verified by its exact name
in the "Step 0c Contract Verified" column of the audit table. Do not alter the contract
phrasing between here and the audit — the column values must match the names used in
Step 0c.

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

**STEP 0C CONTRACT ANCHOR**

Before writing any pitch version, copy the three Step 0c voice contracts here:

Step 0c exec voice contract: [exact text from Step 0c — do not paraphrase or generalize]
Step 0c dev voice contract: [exact text from Step 0c — do not paraphrase or generalize]
Step 0c maker voice contract: [exact text from Step 0c — do not paraphrase or generalize]

These are the anchor sentences. Each pitch version must open with a hook that satisfies its
named contract. Do not begin writing Exec Version, Dev Version, or Maker Version until this
anchor block is complete.

--- ANCHOR GATE: Complete the STEP 0C CONTRACT ANCHOR before writing any pitch version. ---

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
complete. Four named sections: Artifact Existence Record, Phase Gate Audit, Citation
Audit, Voice Compliance Audit.]

### Artifact Existence Record

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

STEP 0C SOURCE BINDING: The three voice contracts verified in this table were authored in
Step 0c above. This audit table does not redefine the contracts — it verifies conformance
to the Step 0c source. The text in the "Step 0c Contract Verified" column must match the
exact contract names as written in Step 0c. Do not rephrase. Do not generalize. The Step 0c
source text is authoritative; any deviation from the Step 0c phrasing constitutes a
verification failure even if the cell value is otherwise complete.

COLUMN-HEADER REQUIREMENT: The third column header must read exactly "Step 0c Contract
Verified". A header reading "Contract Check", "Voice Contract", "Verified", or any label
other than "Step 0c Contract Verified" does not pass.

Record the verdict for each audience in the table below. Fill in the Step 0c Contract
Verified column with the exact Step 0c contract name followed by "satisfied".
A row without a named contract in the verification column does not satisfy this section.

| Audience | Verdict | Step 0c Contract Verified |
|----------|---------|--------------------------|
| Exec | [Pass / Fail] | Step 0c exec voice contract satisfied |
| Dev | [Pass / Fail] | Step 0c dev voice contract satisfied |
| Maker | [Pass / Fail] | Step 0c maker voice contract satisfied |
```

**Rubric targeting**:
- C-40/C-41/C-38/C-39/C-34/C-36/C-37: All unchanged from R11 V-05. All earn.
- STEP 0C SOURCE BINDING (from V-02): Backward reference in VCA. V13 watch: "VCA carries
  explicit source-binding naming Step 0c as authoritative."
- STEP 0C CONTRACT ANCHOR (from V-03): Re-anchor at Phase 3 entry. V13 watch: "Phase 3
  carries explicit contract re-anchor before pitch writing."
- Combined watch: three-position contract naming (define → re-anchor → verify) may itself
  be the structural pattern — a v13 candidate beyond either position alone.

---

## V-05 — Combined: Bidirectional VCA Binding (V-02) + Phase 3 Re-Anchor (V-03) + Citation Form Requirement (new axis)

**Hypothesis**: V-04 tests two new structural positions for voice contracts (backward VCA
binding + Phase 3 re-anchor). V-05 adds a third new axis: a named CITATION FORM REQUIREMENT
in Phase 2, explicitly labeled analogous to the COLUMN-HEADER REQUIREMENT in the Voice
Compliance Audit. The C-41 pattern — a named, labeled requirement statement that makes an
existing template requirement structurally explicit — may apply equally to the stability
citation: the STABILITY CITATION RECORD has a verbatim-paste requirement (C-17/C-21), but
no named labeled statement calls this out explicitly as a requirement (the way COLUMN-HEADER
REQUIREMENT calls out the header). A CITATION FORM REQUIREMENT block in Phase 2 would be the
second dual-mechanism pattern in the prompt: template + named requirement statement for the
citation, mirroring template + named requirement statement for the column header. Predicted:
33/33 + v13 watch on CITATION FORM REQUIREMENT + three-position voice contract naming.

```
Run the campaign-specify skill for: {{topic}}

Produce three artifacts: spec, proposal, pitch. Execute phases 0–3 in order.
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

Evaluate whether the cost of Do Nothing is stable or worsening. Produce the STABILITY
CITATION RECORD using one of the two forms below. This record will be pasted verbatim
into the Phase 2 Defeating Do Nothing block.

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

FORWARD AUDIT NOTICE: These three voice contracts are the compliance criteria for the
COMPLETION INDEX Voice Compliance Audit. Each contract will be verified by its exact name
in the "Step 0c Contract Verified" column of the audit table. Do not alter the contract
phrasing between here and the audit — the column values must match the names used in
Step 0c.

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

CITATION FORM REQUIREMENT: The Defeating Do Nothing block must contain the STABILITY
CITATION RECORD verbatim. A summary, paraphrase, condensed version, or reference to the
record does not satisfy this requirement. The exact Form A or Form B sentence from Step 0b
must appear character-for-character. A Defeating Do Nothing block without the verbatim
STABILITY CITATION RECORD does not satisfy C-17 or C-21 regardless of how closely it
approximates the record's meaning.

**>> PROPOSAL WRITE GATE <<**
Save proposal to: `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md`
Check: does the file exist? If not: write it now.
Do not begin Phase 3 until this file exists on disk.

---

## Phase 3 — Executive Pitch

Pull from `simulations/scout/scout-positioning/` before writing. Note files used.

**STEP 0C CONTRACT ANCHOR**

Before writing any pitch version, copy the three Step 0c voice contracts here:

Step 0c exec voice contract: [exact text from Step 0c — do not paraphrase or generalize]
Step 0c dev voice contract: [exact text from Step 0c — do not paraphrase or generalize]
Step 0c maker voice contract: [exact text from Step 0c — do not paraphrase or generalize]

These are the anchor sentences. Each pitch version must open with a hook that satisfies its
named contract. Do not begin writing Exec Version, Dev Version, or Maker Version until this
anchor block is complete.

--- ANCHOR GATE: Complete the STEP 0C CONTRACT ANCHOR before writing any pitch version. ---

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
complete. Four named sections: Artifact Existence Record, Phase Gate Audit, Citation
Audit, Voice Compliance Audit.]

### Artifact Existence Record

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

STEP 0C SOURCE BINDING: The three voice contracts verified in this table were authored in
Step 0c above. This audit table does not redefine the contracts — it verifies conformance
to the Step 0c source. The text in the "Step 0c Contract Verified" column must match the
exact contract names as written in Step 0c. Do not rephrase. Do not generalize. The Step 0c
source text is authoritative; any deviation from the Step 0c phrasing constitutes a
verification failure even if the cell value is otherwise complete.

COLUMN-HEADER REQUIREMENT: The third column header must read exactly "Step 0c Contract
Verified". A header reading "Contract Check", "Voice Contract", "Verified", or any label
other than "Step 0c Contract Verified" does not pass.

Record the verdict for each audience in the table below. Fill in the Step 0c Contract
Verified column with the exact Step 0c contract name followed by "satisfied".
A row without a named contract in the verification column does not satisfy this section.

| Audience | Verdict | Step 0c Contract Verified |
|----------|---------|--------------------------|
| Exec | [Pass / Fail] | Step 0c exec voice contract satisfied |
| Dev | [Pass / Fail] | Step 0c dev voice contract satisfied |
| Maker | [Pass / Fail] | Step 0c maker voice contract satisfied |
```

**Rubric targeting**:
- C-40/C-41/C-38/C-39/C-34/C-36/C-37: All unchanged from R11 V-05. All earn.
- STEP 0C SOURCE BINDING (from V-02): Backward reference in VCA. V13 watch: "VCA carries
  explicit source-binding statement naming Step 0c as authoritative contract source."
- STEP 0C CONTRACT ANCHOR (from V-03): Re-anchor at Phase 3 entry. V13 watch: "Phase 3
  carries explicit contract re-anchor block before pitch writing."
- CITATION FORM REQUIREMENT (new in V-05): Named labeled requirement in Phase 2 Defeating
  Do Nothing. The C-41 dual-mechanism pattern applied to citations: template requirement
  (the paste instruction) + named requirement statement (CITATION FORM REQUIREMENT block).
  V13 watch: "Phase 2 Defeating Do Nothing block carries a named CITATION FORM REQUIREMENT
  statement — the verbatim paste requirement is structurally stated, not only template-implied."
- Combined watch: V-05 carries three structural novelties simultaneously. If all three
  produce v13 signals, the v13 rubric may require 35+ criteria. If only one or two fire,
  the pattern hierarchy becomes clear for R13 targeting.
