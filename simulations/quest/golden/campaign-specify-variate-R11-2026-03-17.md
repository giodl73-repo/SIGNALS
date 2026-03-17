---
skill: quest-variate
skill_target: campaign-specify
round: 11
date: 2026-03-17
rubric: v11 (31 aspirational criteria; C-38 and C-39 are the new targets)
---

# Variations — campaign-specify / Round 11

Five complete, runnable skill body variations targeting the v11 rubric.
Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

**R10 diagnosis driving R11 axis choices:**

Under v11, two new criteria were added on top of the 29-criterion v10 baseline:

- **C-38** — Audience identifier embedded in the contract attribution phrase. When gate anchor
  (C-34), verb consistency (C-36), and table format (C-37) all pass, each contract phrase in
  the gate parenthetical and the VCA table cell explicitly names the audience:
  "Step 0c **exec** voice contract satisfied" (not "Step 0c voice contract satisfied" generically).
  Structural dependency: requires C-34, C-36, and C-37.
- **C-39** — Step 0c step reference in the VCA contract column header. The column header reads
  "Step 0c Contract Verified" — "Step 0c" is an explicit workflow step reference, not a
  generic label. Structural dependency: requires C-37.

| Variation | Asp (v11) | C-38 | C-39 | Diagnosis |
|-----------|-----------|------|------|-----------|
| R10 V-01 | 28/31 | Fail | Pass | Table present (C-37); no gate anchor (C-34) → C-38 fails by structural dependency |
| R10 V-02 | 31/31 | Pass | Pass | First ceiling — gate anchor + table + "satisfied" + audience identifier + step-ref header all present |

**R11 question set:**

R10 V-02 is the first 31/31. R11 tests whether the ceiling is stable across axis variations
and searches for potential v12 excellence patterns.

1. Does a compressed-imperative phrasing register preserve 31/31?
   (V-01: phrasing compression — same structure, shorter instructions, fewer parentheticals)
2. Does an explicit pre-table instruction naming the audience-discriminator requirement for C-38
   improve robustness without raising the ceiling?
   (V-02: explicit audience-discriminator instruction before VCA table)
3. Does naming "Do Nothing" as an explicit competitor in Phase 0 (before voice contracts)
   improve the Defeating Do Nothing block quality? Any v12 excellence pattern?
   (V-03: inertia framing elevated — Do Nothing named as competitor in Step 0a)
4. Does combining phrasing compression with an explicit audience-discriminator instruction
   hold 31/31?
   (V-04: V-01 + V-02 combined)
5. Does adding a forward reference from Step 0c to the VCA and an explicit column-header
   call-out improve structural binding? Any v12 pattern in the connective tissue?
   (V-05: forward reference from Step 0c → VCA + explicit column-header naming)

| Variation | Axis | C-38 mechanism | C-39 mechanism | Predicted |
|-----------|------|----------------|----------------|-----------|
| V-01 | Phrasing register (compressed imperative) | Template cell values unchanged | Column header unchanged | 31/31 |
| V-02 | Lifecycle emphasis (explicit audience-discriminator pre-instruction) | Template + explicit instruction | Column header unchanged | 31/31 |
| V-03 | Inertia framing (Do Nothing named as competitor in Phase 0) | Template cell values unchanged | Column header unchanged | 31/31 |
| V-04 | Combined: V-01 + V-02 | Template + explicit instruction, compressed | Column header unchanged | 31/31 |
| V-05 | Combined: forward reference from Step 0c + explicit column-header call-out | Template + forward reference | Column header named explicitly | 31/31 |

**Predicted ceiling**: All five variations target 31/31. V-01 is the robustness test — if
the compressed register drops any criterion, it surfaces a fragility in the v11 ceiling.
V-05 tests whether explicit forward binding creates new excellence patterns not yet in v11.

---

## V-01 — Axis: Phrasing Register — Compressed Imperative (Robustness Test)

**Hypothesis**: R10 V-02 uses a detailed explanatory register throughout — instructions include
parentheticals, failure-mode descriptions, and elaborated conditions. V-01 compresses to a
direct imperative register: shorter instructions, active-voice commands, gates as one-liners,
no explanatory elaboration on failure modes. The VCA table template is preserved exactly —
"Step 0c Contract Verified" column header (C-39), cell values with audience identifier and
"satisfied" verb (C-38, C-36). The gate parentheticals preserve the "Step 0c exec voice
contract satisfied:" anchor structure (C-34). If all structural elements survive register
compression, V-01 scores 31/31 and confirms the ceiling is register-independent.
Predicted: 31/31.

```
Run the campaign-specify skill for: {{topic}}

Produce three artifacts: spec, proposal, pitch. Execute phases 0-3 in order.
Each phase completes before the next begins. Each artifact is written to disk
before the next phase starts.

---

## Phase 0 — Audience Foundation

Four sequential steps. Gates enforce order.

**Step 0a — Inertia Costs**

For each audience: what is lost if {{topic}} does not ship?

Exec inertia cost: [Revenue exposure, competitive gap, or risk — name a consequence,
quantify if possible.]

Dev inertia cost: [Workaround or capability gap — name the friction, estimate recurring
cost if possible.]

Maker inertia cost: [Blocked workflow step — name the step, name what the maker does
today instead.]

--- GATE 1: Complete all three inertia costs before proceeding to Step 0b. ---

**Step 0b — Stability Citation Record**

Is the cost of Do Nothing stable or worsening? Write the STABILITY CITATION RECORD:

FORM A: "Do Nothing is not stable: [mechanism and timeline]."
FORM B: "Do Nothing is stable: [rationale]."

STABILITY CITATION RECORD:
[Complete Form A or Form B sentence here — verbatim citation source for Phase 2.]

--- GATE 2: Complete the STABILITY CITATION RECORD before proceeding to Step 0c. ---

**Step 0c — Voice Contracts**

One sentence per audience grounded in Steps 0a and 0b:

Exec voice: [Outcomes/risk framing — exec inertia cost + stability trajectory]
Dev voice: [Capability/friction framing — dev inertia cost]
Maker voice: [Workflow framing — plain language, maker inertia cost]

--- GATE 3: Complete all three voice contracts before proceeding to Step 0d. ---

**Step 0d — Scout Pull** [TERMINAL]

Glob `simulations/scout/**/*.md` for {{topic}}. List: path, one-sentence summary,
artifact served (spec / proposal / pitch). If none: "no scout signals — proceeding without."

[Phase 0 complete. Gates 1–3 passed. Proceed to Phase 1.]

---

## Phase 1 — Technical Spec

Pull from `simulations/scout/`. All six sections required — no skipping, no merging.

### Overview
One paragraph: what {{topic}} does and why it exists.

### User Problem
Problem users face today. Reference dev and maker inertia costs from Step 0a.

### Proposed Solution
What {{topic}} does. Incorporate scout-requirements or scout-feasibility signals if found.

### Constraints
Three minimum: technical, scope, platform.

### Open Questions
Three minimum named ambiguities.

### Self-Review
One named gap minimum. "No gaps found" fails.

**>> SPEC WRITE GATE <<**
Save: `simulations/draft/specs/{{topic}}-spec-{{date}}.md`
If the file does not exist: write it now. Do not begin Phase 2 until it exists.

---

## Phase 2 — Business Proposal

Pull from `simulations/scout/scout-feasibility/`. Note files used.

Three options minimum. Option 1 MUST be named **Do Nothing**.

For each option: description, pros, cons, risk, effort.

### Recommendation

We recommend [chosen option].

#### Defeating Do Nothing

Do Nothing perpetuates [most decisive Step 0a inertia cost — name audience and cost].

[PASTE STABILITY CITATION RECORD FROM STEP 0b VERBATIM. No summarizing. No paraphrasing.]

We choose to act because [one sentence: why this cost trajectory is not acceptable].

#### Defeating [Other Option Name]

We prefer [chosen] over [other] because [specific trade-off traceable to risk, effort,
or cons in the options analysis].

**>> PROPOSAL WRITE GATE <<**
Save: `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md`
If the file does not exist: write it now. Do not begin Phase 3 until it exists.

---

## Phase 3 — Executive Pitch

Pull from `simulations/scout/scout-positioning/`. Note files used.

### Exec Version
Lead with exec inertia cost. Use Step 0c exec voice contract as anchor.
Structure: [exec cost hook] → [what changes] → [outcome/ROI] → [call to action].
Do not open with a product description.

### Dev Version
Lead with dev inertia cost. Use Step 0c dev voice contract as anchor.
Structure: [friction hook] → [what you can now do] → [capability unlocked] → [call to action].
Do not open with an outcomes/ROI frame.

### Maker Version
Lead with maker inertia cost. Use Step 0c maker voice contract as anchor.
Plain language, no jargon.
Structure: [blocked step hook] → [what you can now do] → [why it matters] → [call to action].

### Anti-Positioning
3–5 "This is not..." statements. Structurally separate from the three audience versions.

**>> VOICE DIFFERENTIATION GATE — Step 0c Contract Check <<**

Step 1 — Copy Step 0c voice contracts:
  Step 0c exec voice contract: [exec voice sentence from Step 0c]
  Step 0c dev voice contract: [dev voice sentence from Step 0c]
  Step 0c maker voice contract: [maker voice sentence from Step 0c]

Step 2 — Extract opening sentence from each pitch version:
  Exec opening: [first sentence of Exec Version]
  Dev opening: [first sentence of Dev Version]
  Maker opening: [first sentence of Maker Version]

Step 3 — Per-audience gate:

  Exec gate:
    Pass (Step 0c exec voice contract satisfied: opening names a business cost,
      risk, or revenue consequence) /
    Fail (opening does not satisfy the Step 0c exec voice contract: opens with
      product description, capability framing, or workflow framing)

  Dev gate:
    Pass (Step 0c dev voice contract satisfied: opening names a tool friction,
      workaround, or capability gap) /
    Fail (opening does not satisfy the Step 0c dev voice contract: opens with
      outcome/ROI framing or business consequence framing)

  Maker gate:
    Pass (Step 0c maker voice contract satisfied: opening names a blocked, absent,
      or manual step in plain language, no jargon) /
    Fail (opening does not satisfy the Step 0c maker voice contract: opens with
      product description or technical jargon)

Step 4 — Resolution:
  Any Fail: rewrite the failing version anchored to its Step 0c contract. Re-run Steps 2–3.
  All Pass: proceed to PITCH WRITE GATE.

**>> PITCH WRITE GATE <<**
Save only after all three gates in Step 3 are Pass.
Save: `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`
Do not emit the COMPLETION INDEX until this file exists.

---

## COMPLETION INDEX

[Emitted after all write gates and voice differentiation gate are complete.
Four sections: Artifact Existence Record, Phase Gate Audit, Citation Audit,
Voice Compliance Audit.]

### Artifact Existence Record

| Artifact | Path | Status |
|----------|------|--------|
| Spec | `simulations/draft/specs/{{topic}}-spec-{{date}}.md` | [exists / missing] |
| Proposal | `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md` | [exists / missing] |
| Pitch | `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md` | [exists / missing] |

All three rows must show "exists."

### Phase Gate Audit
- Scout files used per phase
- Phase 0 inertia costs confirmed (all three audiences)
- Phase 0 gate chain: 3 gates passed (Gate 1: 0a→0b | Gate 2: 0b→0c | Gate 3: 0c→0d)

### Citation Audit
- STABILITY CITATION RECORD form used: Form A / Form B
- STABILITY CITATION RECORD pasted verbatim in Defeating Do Nothing block:
  CITATION CONFIRMED / CITATION MISSING
- Defeating Do Nothing block: separate labeled header: yes / no

### Voice Compliance Audit

| Audience | Verdict | Step 0c Contract Verified |
|----------|---------|--------------------------|
| Exec | [Pass / Fail] | Step 0c exec voice contract satisfied |
| Dev | [Pass / Fail] | Step 0c dev voice contract satisfied |
| Maker | [Pass / Fail] | Step 0c maker voice contract satisfied |
```

**Rubric targeting**:
- C-34: Gate Step 3 parentheticals open with audience-specific contract name and "satisfied".
  `Pass (Step 0c exec voice contract satisfied: ...)`. Earns C-34.
- C-36: Gate parenthetical verb is "satisfied". Table cell values carry "satisfied" — verb
  matches. Earns C-36.
- C-37: Table format with Audience, Verdict, Step 0c Contract Verified columns. Earns C-37.
- C-38: Cell values embed audience identifier: "Step 0c exec voice contract satisfied" for exec,
  "Step 0c dev voice contract satisfied" for dev, "Step 0c maker voice contract satisfied" for
  maker. Gate parentheticals carry same identifiers. Earns C-38.
- C-39: Column header is "Step 0c Contract Verified" — carries "Step 0c" step reference.
  Earns C-39.
- Compression risk: phrasing register is shorter throughout. Gate descriptions use fewer words.
  If the scoring model requires the failure-mode parentheticals that V-02 R10 carried in the
  gate sections, some criteria may be fragile. This is the primary uncertainty being tested.

---

## V-02 — Axis: Lifecycle Emphasis — Explicit Audience-Discriminator Pre-Instruction for VCA

**Hypothesis**: R10 V-02 earns C-38 because the VCA table template explicitly carries audience
identifiers in the cell values ("Step 0c exec voice contract satisfied"). However, when a model
uses this prompt without the template as a guide — filling in the cell values from memory — it
may drop the audience discriminator and write "Step 0c voice contract satisfied" generically.
V-02 adds an explicit instruction block before the VCA table naming the audience-discriminator
requirement: each contract cell must carry the audience identifier embedded in the phrase. This
tests whether explicit instruction is more robust than template-only for C-38 across model runs.
Gate anchor (C-34), verb consistency (C-36), and column header (C-39) are unchanged from R10 V-02.
Predicted: 31/31.

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

AUDIENCE-DISCRIMINATOR REQUIREMENT: Each row below names one audience (exec, dev, or maker).
The "Step 0c Contract Verified" column must carry the Step 0c contract name with the audience
identifier embedded in the phrase — e.g., "Step 0c exec voice contract satisfied" for exec.
A phrase without the audience identifier (e.g., "Step 0c voice contract satisfied" applied
generically) does not pass this audit regardless of which row it appears in.

| Audience | Verdict | Step 0c Contract Verified |
|----------|---------|--------------------------|
| Exec | [Pass / Fail] | Step 0c exec voice contract satisfied |
| Dev | [Pass / Fail] | Step 0c dev voice contract satisfied |
| Maker | [Pass / Fail] | Step 0c maker voice contract satisfied |
```

**Rubric targeting**:
- C-38: The explicit pre-table instruction names the audience-discriminator requirement
  directly. The table template cells carry "Step 0c exec/dev/maker voice contract satisfied".
  Two mechanisms (instruction + template) both earn C-38.
- C-39: Column header "Step 0c Contract Verified" unchanged. Earns C-39.
- C-34/C-36/C-37: Gate parentheticals and table format unchanged from R10 V-02. All earn.
- Possible v12 pattern: the explicit instruction block in the VCA may itself become a criterion —
  "VCA carries an explicit audience-discriminator requirement statement before the table."
  Watch for whether the scoring model awards this as a distinct quality signal.

---

## V-03 — Axis: Inertia Framing — Do Nothing Named as Explicit Competitor in Phase 0

**Hypothesis**: In R10 V-02, "Do Nothing" appears as an analysis option in Phase 2. The inertia
framing in Phase 0 (Step 0a) is implicit — it asks for what each audience loses, but does not
name the status quo as a competitor. V-03 elevates inertia framing: Step 0a opens with an
explicit statement naming Do Nothing as the primary competitor that {{topic}} must defeat. This
mirrors the scout-competitors convention (inertia as competitor #0) and may improve the quality
of the Defeating Do Nothing block in Phase 2 by setting up the competitor framing early. All
VCA structural elements from R10 V-02 are preserved unchanged — this is a pure inertia-framing
axis change. Tests if elevated inertia framing creates any v12 excellence pattern.
Predicted: 31/31.

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

THE PRIMARY COMPETITOR: Do Nothing — the status quo that {{topic}} must defeat. Before
writing voice contracts or artifacts, name what each audience loses if {{topic}} never ships.
This is not a hypothetical; it is the current state that Do Nothing preserves. Concrete and
specific:

Exec inertia cost: [Specific revenue exposure, competitive gap, or risk the exec faces TODAY
without {{topic}}. Name a consequence, not a category. Quantify if possible.]

Dev inertia cost: [Specific workaround or capability gap the dev lives with TODAY without
{{topic}}. Name the friction, not the feeling. Estimate recurring cost if possible.]

Maker inertia cost: [Specific blocked workflow step the maker hits TODAY without {{topic}}.
Name the step. What does the maker do instead right now?]

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

One sentence per audience, grounded in Steps 0a and 0b. Each contract names the cost Do
Nothing imposes on that audience and what {{topic}} does about it:

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
Do Nothing is Competitor #0 — the status quo the team must consciously choose against.

For each option: description, pros, cons, risk, effort.

Then write the **Recommendation** section with the following labeled blocks.
Each block has its own header. Do not merge them into a combined paragraph.

### Recommendation

We recommend [chosen option].

#### Defeating Do Nothing

[This block defeats the primary competitor: Do Nothing — the status quo named in Step 0a.
Structurally separate from the comparative defeat below.]

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
- C-38/C-39/C-34/C-36/C-37: All VCA structural elements unchanged from R10 V-02. All earn.
- Inertia framing change: Step 0a opens with "THE PRIMARY COMPETITOR: Do Nothing" — mirrors
  the scout-competitors convention. Phase 2 Defeating Do Nothing block gains "Competitor #0"
  framing.
- Possible v12 pattern: "Do Nothing named as primary competitor in Phase 0 before voice
  contracts are written." Watch for whether this improves the Defeating Do Nothing block
  quality in scoring (depth axis) beyond what the current rubric measures.

---

## V-04 — Combined: Phrasing Register Compression + Explicit Audience-Discriminator Pre-Instruction

**Hypothesis**: V-01 tests phrasing compression (shorter instructions, active-voice). V-02 tests
the explicit audience-discriminator instruction before the VCA table. V-04 combines both: the
full prompt is compressed to a direct imperative register, AND the VCA carries the explicit
pre-table audience-discriminator requirement. If V-01 succeeds (31/31 with compression) and V-02
succeeds (31/31 with explicit instruction), the combination should preserve both and score 31/31.
The risk: compression might conflict with the explicit instruction's additional text — if the
combined length is seen as inconsistent, some structural criteria might behave unexpectedly.
Predicted: 31/31.

```
Run the campaign-specify skill for: {{topic}}

Produce three artifacts: spec, proposal, pitch. Execute phases 0-3 in order.
Each phase completes before the next begins. Each artifact is written to disk
before the next phase starts.

---

## Phase 0 — Audience Foundation

Four sequential steps. Gates enforce order.

**Step 0a — Inertia Costs**

For each audience: what is lost if {{topic}} does not ship?

Exec inertia cost: [Revenue exposure, competitive gap, or risk — name a consequence,
quantify if possible.]

Dev inertia cost: [Workaround or capability gap — name the friction, estimate recurring
cost if possible.]

Maker inertia cost: [Blocked workflow step — name the step, name what the maker does
today instead.]

--- GATE 1: Complete all three inertia costs before proceeding to Step 0b. ---

**Step 0b — Stability Citation Record**

Is the cost of Do Nothing stable or worsening? Write the STABILITY CITATION RECORD:

FORM A: "Do Nothing is not stable: [mechanism and timeline]."
FORM B: "Do Nothing is stable: [rationale]."

STABILITY CITATION RECORD:
[Complete Form A or Form B sentence here — verbatim citation source for Phase 2.]

--- GATE 2: Complete the STABILITY CITATION RECORD before proceeding to Step 0c. ---

**Step 0c — Voice Contracts**

One sentence per audience grounded in Steps 0a and 0b:

Exec voice: [Outcomes/risk framing — exec inertia cost + stability trajectory]
Dev voice: [Capability/friction framing — dev inertia cost]
Maker voice: [Workflow framing — plain language, maker inertia cost]

--- GATE 3: Complete all three voice contracts before proceeding to Step 0d. ---

**Step 0d — Scout Pull** [TERMINAL]

Glob `simulations/scout/**/*.md` for {{topic}}. List: path, one-sentence summary,
artifact served (spec / proposal / pitch). If none: "no scout signals — proceeding without."

[Phase 0 complete. Gates 1–3 passed. Proceed to Phase 1.]

---

## Phase 1 — Technical Spec

Pull from `simulations/scout/`. All six sections required — no skipping, no merging.

### Overview
One paragraph: what {{topic}} does and why it exists.

### User Problem
Problem users face today. Reference dev and maker inertia costs from Step 0a.

### Proposed Solution
What {{topic}} does. Incorporate scout-requirements or scout-feasibility signals if found.

### Constraints
Three minimum: technical, scope, platform.

### Open Questions
Three minimum named ambiguities.

### Self-Review
One named gap minimum. "No gaps found" fails.

**>> SPEC WRITE GATE <<**
Save: `simulations/draft/specs/{{topic}}-spec-{{date}}.md`
If the file does not exist: write it now. Do not begin Phase 2 until it exists.

---

## Phase 2 — Business Proposal

Pull from `simulations/scout/scout-feasibility/`. Note files used.

Three options minimum. Option 1 MUST be named **Do Nothing**.

For each option: description, pros, cons, risk, effort.

### Recommendation

We recommend [chosen option].

#### Defeating Do Nothing

Do Nothing perpetuates [most decisive Step 0a inertia cost — name audience and cost].

[PASTE STABILITY CITATION RECORD FROM STEP 0b VERBATIM. No summarizing. No paraphrasing.]

We choose to act because [one sentence: why this cost trajectory is not acceptable].

#### Defeating [Other Option Name]

We prefer [chosen] over [other] because [specific trade-off traceable to risk, effort,
or cons in the options analysis].

**>> PROPOSAL WRITE GATE <<**
Save: `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md`
If the file does not exist: write it now. Do not begin Phase 3 until it exists.

---

## Phase 3 — Executive Pitch

Pull from `simulations/scout/scout-positioning/`. Note files used.

### Exec Version
Lead with exec inertia cost. Use Step 0c exec voice contract as anchor.
Structure: [exec cost hook] → [what changes] → [outcome/ROI] → [call to action].
Do not open with a product description.

### Dev Version
Lead with dev inertia cost. Use Step 0c dev voice contract as anchor.
Structure: [friction hook] → [what you can now do] → [capability unlocked] → [call to action].
Do not open with an outcomes/ROI frame.

### Maker Version
Lead with maker inertia cost. Use Step 0c maker voice contract as anchor.
Plain language, no jargon.
Structure: [blocked step hook] → [what you can now do] → [why it matters] → [call to action].

### Anti-Positioning
3–5 "This is not..." statements. Structurally separate from the three audience versions.

**>> VOICE DIFFERENTIATION GATE — Step 0c Contract Check <<**

Step 1 — Copy Step 0c voice contracts:
  Step 0c exec voice contract: [exec voice sentence from Step 0c]
  Step 0c dev voice contract: [dev voice sentence from Step 0c]
  Step 0c maker voice contract: [maker voice sentence from Step 0c]

Step 2 — Extract opening sentence from each pitch version:
  Exec opening: [first sentence of Exec Version]
  Dev opening: [first sentence of Dev Version]
  Maker opening: [first sentence of Maker Version]

Step 3 — Per-audience gate:

  Exec gate:
    Pass (Step 0c exec voice contract satisfied: opening names a business cost,
      risk, or revenue consequence) /
    Fail (opening does not satisfy the Step 0c exec voice contract: opens with
      product description, capability framing, or workflow framing)

  Dev gate:
    Pass (Step 0c dev voice contract satisfied: opening names a tool friction,
      workaround, or capability gap) /
    Fail (opening does not satisfy the Step 0c dev voice contract: opens with
      outcome/ROI framing or business consequence framing)

  Maker gate:
    Pass (Step 0c maker voice contract satisfied: opening names a blocked, absent,
      or manual step in plain language, no jargon) /
    Fail (opening does not satisfy the Step 0c maker voice contract: opens with
      product description or technical jargon)

Step 4 — Resolution:
  Any Fail: rewrite the failing version anchored to its Step 0c contract. Re-run Steps 2–3.
  All Pass: proceed to PITCH WRITE GATE.

**>> PITCH WRITE GATE <<**
Save only after all three gates in Step 3 are Pass.
Save: `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`
Do not emit the COMPLETION INDEX until this file exists.

---

## COMPLETION INDEX

[Emitted after all write gates and voice differentiation gate are complete.
Four sections: Artifact Existence Record, Phase Gate Audit, Citation Audit,
Voice Compliance Audit.]

### Artifact Existence Record

| Artifact | Path | Status |
|----------|------|--------|
| Spec | `simulations/draft/specs/{{topic}}-spec-{{date}}.md` | [exists / missing] |
| Proposal | `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md` | [exists / missing] |
| Pitch | `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md` | [exists / missing] |

All three rows must show "exists."

### Phase Gate Audit
- Scout files used per phase
- Phase 0 inertia costs confirmed (all three audiences)
- Phase 0 gate chain: 3 gates passed (Gate 1: 0a→0b | Gate 2: 0b→0c | Gate 3: 0c→0d)

### Citation Audit
- STABILITY CITATION RECORD form used: Form A / Form B
- STABILITY CITATION RECORD pasted verbatim in Defeating Do Nothing block:
  CITATION CONFIRMED / CITATION MISSING
- Defeating Do Nothing block: separate labeled header: yes / no

### Voice Compliance Audit

AUDIENCE-DISCRIMINATOR REQUIREMENT: Each row names one audience (exec, dev, or maker).
The "Step 0c Contract Verified" column must carry the Step 0c contract name with the
audience identifier embedded — e.g., "Step 0c exec voice contract satisfied" for exec.
A phrase without the audience identifier does not pass this audit.

| Audience | Verdict | Step 0c Contract Verified |
|----------|---------|--------------------------|
| Exec | [Pass / Fail] | Step 0c exec voice contract satisfied |
| Dev | [Pass / Fail] | Step 0c dev voice contract satisfied |
| Maker | [Pass / Fail] | Step 0c maker voice contract satisfied |
```

**Rubric targeting**:
- C-38: Explicit pre-table instruction + template cell values with audience identifiers.
  Both mechanisms active. Earns C-38.
- C-39: Column header "Step 0c Contract Verified" preserved. Earns C-39.
- C-34/C-36/C-37: Gate parentheticals compressed but structurally preserved. All earn.
- Compression risk assessment: Phase 0 gates shortened to one-liners. Phase 2 Recommendation
  loses the Note block warning. If any criterion depends on the note block language, that
  criterion is at risk. Note which criteria score differently from V-01 and V-02 individually.

---

## V-05 — Combined: Forward Reference from Step 0c + Explicit Column-Header Call-Out

**Hypothesis**: R10 V-02 builds structural binding between Step 0c voice contracts and the VCA
through template repetition (the same contract names appear in both places). V-05 adds two
explicit connective structures: (1) a forward reference in Step 0c: "These three contracts are
the audit criteria for the COMPLETION INDEX Voice Compliance Audit. They will be verified by
name in the Step 0c Contract Verified column." (2) An explicit column-header call-out in the
VCA instruction: "The third column header must read exactly: 'Step 0c Contract Verified'."
The forward reference makes the binding relationship visible at authoring time (Step 0c) rather
than only at audit time (COMPLETION INDEX). The explicit column-header call-out makes C-39
structurally stated rather than only pattern-embedded. Together, these test whether explicit
forward binding produces a v12 excellence pattern beyond what the template carries alone.
Predicted: 31/31. V12 watch: forward reference from Step 0c → VCA.

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
- C-38: Cell values carry audience identifier + "satisfied". Gate parentheticals carry same.
  Unchanged from R10 V-02. Earns C-38.
- C-39: Column header "Step 0c Contract Verified" now named explicitly in the pre-table
  instruction AND present in the template. Two mechanisms for C-39. Earns C-39.
- C-34/C-36/C-37: Gate parentheticals and table format unchanged from R10 V-02. All earn.
- Forward reference placement: Step 0c FORWARD AUDIT NOTICE creates a named binding from
  Step 0c → VCA before the artifact phases begin. Tests whether this creates a v12 criterion:
  "Step 0c carries a forward reference to the COMPLETION INDEX Voice Compliance Audit."
- Column-header call-out in VCA: the explicit requirement statement before the table names
  C-39 directly. Tests whether this creates a v12 criterion: "VCA carries an explicit
  column-header requirement statement naming 'Step 0c Contract Verified'."
- Both potential v12 patterns are additive — they do not change any existing criterion.
  Watch for whether quest-score flags them as excellence signals above the v11 ceiling.
```
