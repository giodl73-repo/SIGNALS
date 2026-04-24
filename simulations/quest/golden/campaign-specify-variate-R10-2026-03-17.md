---
skill: quest-variate
skill_target: campaign-specify
round: 10
date: 2026-03-17
rubric: v10 (29 aspirational criteria; C-36 and C-37 are the new targets)
---

# Variations — campaign-specify / Round 10

Five complete, runnable skill body variations targeting the v10 rubric.
Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

**R9 diagnosis driving R10 axis choices:**

Under v10, two new criteria were added on top of the 27-criterion v9 baseline:

- **C-36** — Lexical verb consistency between the gate parenthetical (C-34) and each
  per-audience audit row (C-35). Both must use the same verb (e.g., "satisfied").
- **C-37** — Voice Compliance Audit presented as a structured table (Audience / Verdict /
  dedicated Step 0c contract column). Flat bullet-list format does not pass.

| Variation | Asp (v10) | C-34 | C-36 | C-37 | Diagnosis |
|-----------|-----------|------|------|------|-----------|
| R9 V-01 | 26/29 | Miss | Miss | Miss | Instruction + "verified" rows; no gate anchor |
| R9 V-02 | 28/29 | Pass | Miss | Pass | Table earned C-37; cell value `Step 0c exec voice contract` carries no verb — gate says "satisfied", cell has nothing — C-36 fails |
| R9 V-03 | 28/29 | Pass | Pass | Miss | "Satisfied" rows earn C-36; bullet format fails C-37 |
| R9 V-04 | 26/29 | Miss | Miss | Miss | Instruction + "satisfied" rows; no gate anchor → C-36 requires C-34 |

**Root cause for R9 failure to reach 29/29:**

Two paths tied at 28/29 via non-overlapping mechanisms:
- **V-02 path**: table (C-37) + gate anchor (C-34) but missing verb in table cells → C-36 fails
- **V-03 path**: "satisfied" bullets (C-36) + gate anchor (C-34) but bullet format → C-37 fails

The 29/29 synthesis requires: table format (C-37) AND "satisfied" in table cell values
(so C-36 matches the gate parenthetical verb) AND gate anchor (C-34).

**R10 question set:**

1. Does a table with "satisfied" in cell values earn C-37 without a gate anchor?
   (V-01: table + "satisfied" cells, no gate anchor — isolates C-37 + C-36 dependency)
2. Does the minimal 29/29 synthesis — table + "satisfied" cells + gate anchor — hit the ceiling?
   (V-02: the direct combination)
3. Does an explicit instruction naming the "satisfied" verb consistency requirement before the table
   improve robustness over the table template alone?
   (V-03: instruction + table + "satisfied" + gate anchor)
4. Does a forward reference pointer from the gate step to the audit table improve the verb
   carry-through from gate parenthetical to table cell?
   (V-04: V-02 base + forward reference in Step 4 of the gate)
5. Does an explicit lexical-consistency constraint block inside the Voice Compliance Audit
   section — naming the mismatch failure mode — make C-36 more reliable?
   (V-05: V-02 base + explicit C-36 constraint block before table)

| Variation | Axis | Gate anchor | Cell verb | Table format | Predicted |
|-----------|------|-------------|-----------|--------------|-----------|
| V-01 | Output format (table + satisfied, no C-34) | No | "satisfied" | Yes | 27/29 (C-34 miss, C-36 miss) |
| V-02 | Output format (full synthesis) | Yes | "satisfied" | Yes | 29/29 |
| V-03 | Lifecycle emphasis (explicit instruction) | Yes | "satisfied" | Yes | 29/29 |
| V-04 | Lifecycle emphasis (forward reference) | Yes | "satisfied" | Yes | 29/29 |
| V-05 | Lifecycle emphasis (explicit C-36 block) | Yes | "satisfied" | Yes | 29/29 |

**Predicted ceiling**: V-02 through V-05 each target 29/29. V-01 is the isolation test
confirming that C-36 is structurally dependent on C-34 (gate anchor required).

---

## V-01 — Axis: Output Format — Table with "Satisfied" Cell Values, No Gate Anchor

**Hypothesis**: R9 V-02 earned C-37 (table) but failed C-36 because table cell values
carried no verb (`Step 0c exec voice contract`, not `Step 0c exec voice contract satisfied`).
V-01 tests the correction: adding "satisfied" to the cell values while removing the gate anchor.
With no gate anchor (C-34 missing), C-36 cannot be earned — the criterion requires both C-34
and C-35 to exist before the verb-consistency check applies. V-01 therefore isolates the C-37
question: does a table format earn C-37 regardless of the verb in the cells? And does the
"satisfied" verb in cells alone (without a gate anchor) do anything for C-36?
Predicted: earns C-33, C-35, C-37; misses C-34, C-36 = 27/29.

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
- C-37: Table format with Audience, Verdict, and Step 0c Contract Verified columns. Earns C-37.
- C-35: Cell values name the applicable Step 0c contract inline within the row. Earns C-35.
- C-33: Three per-audience rows (one per audience). Earns C-33.
- C-36: Cell values use "satisfied" — but gate parenthetical in Step 3 is bare behavioral (no
  contract attribution) so C-34 fails. C-36 requires BOTH C-34 and C-35 to exist. Without C-34,
  C-36 is structurally inapplicable. Misses C-36.
- C-34: Gate Step 3 uses bare behavioral criteria without contract attribution. Misses C-34.

This is the isolation test. If C-36 fails here (as predicted), it confirms that C-36 is
structurally dependent on C-34 — verb consistency only applies when both a gate parenthetical
AND audit row attribution exist.

---

## V-02 — Axis: Output Format — Table with "Satisfied" Cell Values + Gate Anchor (29/29 synthesis)

**Hypothesis**: R9 V-02 missed C-36 because the table column values carried no verb
(`Step 0c exec voice contract` vs gate parenthetical's `satisfied`). R9 V-03 missed C-37
because bullet rows don't pass the table format requirement. V-02 combines the R9 V-03
verb ("satisfied" in row attribution) with the R9 V-02 structure (table format), plus the
gate anchor (C-34) from both. The result is: table (C-37) + "satisfied" in cells matching
gate parenthetical's "satisfied" (C-36) + gate anchor (C-34). This is the minimal 29/29
synthesis. Single-axis change from R9 V-02: table cell values gain "satisfied". Predicted: 29/29.

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

| Audience | Verdict | Step 0c Contract Verified |
|----------|---------|--------------------------|
| Exec | [Pass / Fail] | Step 0c exec voice contract satisfied |
| Dev | [Pass / Fail] | Step 0c dev voice contract satisfied |
| Maker | [Pass / Fail] | Step 0c maker voice contract satisfied |
```

**Rubric targeting**:
- C-34: Gate Step 3 parentheticals open with contract name: `Pass (Step 0c exec voice contract
  satisfied: ...)`. Earns C-34.
- C-36: Gate parenthetical verb is "satisfied". Table cell values are `Step 0c exec voice
  contract satisfied` — same verb "satisfied". Lexical consistency achieved. Earns C-36.
- C-37: Table format with Audience, Verdict, and Step 0c Contract Verified columns. Earns C-37.
- C-35: Cell values name the applicable Step 0c contract inline within the row. Earns C-35.
- C-33: Three per-audience rows. Earns C-33.
- C-27, C-28, C-29, C-32: Section header, gate formalism, Step 0c naming in gate criteria,
  categorization declaration — unchanged from R9 V-03 baseline.

**Risk**: Minimal. The change from R9 V-02 is surgical: table cell values gain "satisfied".
The change from R9 V-03 is surgical: bullet rows become a table. Both prior-round earning
mechanisms are preserved in their respective domains. If the scoring system accepts the
combined form, this is 29/29.

---

## V-03 — Axis: Lifecycle Emphasis — Explicit Verb Consistency Instruction Before Audit Table

**Hypothesis**: V-02 achieves 29/29 via the template alone — the "satisfied" verb in cell
values implicitly creates lexical consistency with the gate parenthetical. V-03 tests whether
making the verb consistency requirement explicit in prose before the table increases robustness:
an instruction paragraph names (a) the table format requirement, (b) the required cell content
verb ("satisfied"), and (c) the consistency relationship with the gate parenthetical. A model
that might otherwise copy the table template without filling the "satisfied" verb is explicitly
directed to include it. If V-02 is sufficient, V-03 should score identically. If V-02 is fragile
(model drops the verb from cells), V-03 should be more robust. Gate anchor preserved (C-34).
Predicted: 29/29.

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

Each row below records the Step 3 gate verdict for one audience. Fill in the Step 0c
Contract Verified column using the exact form: `Step 0c [audience] voice contract satisfied`.
The word "satisfied" must match the verb in the gate parenthetical above. A cell that omits
the contract name, or substitutes a different verb (e.g., "verified"), does not satisfy this
section. Example: `Step 0c exec voice contract satisfied`.

| Audience | Verdict | Step 0c Contract Verified |
|----------|---------|--------------------------|
| Exec | [Pass / Fail] | Step 0c exec voice contract satisfied |
| Dev | [Pass / Fail] | Step 0c dev voice contract satisfied |
| Maker | [Pass / Fail] | Step 0c maker voice contract satisfied |
```

**Rubric targeting**:
- C-34: Gate anchor preserved (same as V-02). Earns C-34.
- C-36: Instruction paragraph explicitly names the required verb ("satisfied") and its
  consistency relationship with the gate parenthetical. Cell template shows "satisfied".
  Earns C-36 — with higher robustness than V-02 if the model treats the instruction as
  a requirement rather than an example.
- C-37: Table format. Earns C-37.
- C-35: Cell values attribute the Step 0c contract inline. Earns C-35.
- C-33: Three per-audience rows. Earns C-33.

**Risk**: If the instruction's failure-mode callout ("e.g., 'verified'") causes the model to
produce "verified" rows by pattern-matching on the non-passing example, C-36 fails. The
diagnostic value is whether an explicit failure-mode callout helps or interferes.

---

## V-04 — Combined: Table + Satisfied Verb + Gate Anchor + Forward Reference from Gate to Audit

**Hypothesis**: V-02 achieves 29/29 via the gate parenthetical and table cell values sharing
the "satisfied" verb. The verb consistency is implicit: the model must recall the gate
parenthetical's verb when filling in the table cells much later in the output. V-04 tests
whether an explicit forward reference — added to Step 4 of the gate — bridging the gate
step to the audit table reduces this cross-section amnesia. If the model carries the "satisfied"
verb forward when pointed toward the table, the forward reference acts as a consistency anchor.
All structural elements of V-02 are preserved. This is a lifecycle emphasis change: one sentence
added to Step 4 of the gate naming the audit table as the carry-forward destination.
Predicted: 29/29.

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
  IF all three gates are Pass: proceed to PITCH WRITE GATE. The audit record for these
    gate verdicts will appear in the Voice Compliance Audit table in the COMPLETION INDEX
    below. Use the verb "satisfied" in both the gate parenthetical above and the
    Step 0c Contract Verified cell below — the two records must use the same verb.

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

| Audience | Verdict | Step 0c Contract Verified |
|----------|---------|--------------------------|
| Exec | [Pass / Fail] | Step 0c exec voice contract satisfied |
| Dev | [Pass / Fail] | Step 0c dev voice contract satisfied |
| Maker | [Pass / Fail] | Step 0c maker voice contract satisfied |
```

**Rubric targeting**:
- C-34: Gate anchor (same as V-02). Earns C-34.
- C-36: Forward reference in Step 4 explicitly names the verb ("satisfied") that must appear
  in both the gate parenthetical and the audit cell. The bridge between gate and table is
  made visible before the COMPLETION INDEX is emitted. Earns C-36.
- C-37: Table format. Earns C-37.
- C-35: Cell values name the Step 0c contract inline. Earns C-35.
- C-33: Three per-audience rows. Earns C-33.

**Diagnostic value**: If V-04 outperforms V-02 on C-36, it confirms that cross-section verb
consistency benefits from an explicit carry-forward instruction rather than relying on the
template alone. If both score 29/29, the two approaches are equivalent.

---

## V-05 — Combined: Table + Satisfied Verb + Gate Anchor + Explicit Lexical-Consistency Block

**Hypothesis**: V-02 puts the "satisfied" verb in the table cell template and relies on the
model to notice the consistency with the gate parenthetical. V-04 adds a forward reference
from the gate to the table. V-05 takes a different approach: instead of bridging at the gate
step (V-04), it adds an explicit lexical-consistency constraint block INSIDE the Voice
Compliance Audit section itself — naming the mismatch failure mode and stating the requirement
in declarative form. If the model drops the "satisfied" verb from the table cells (the R9 V-02
failure mode), the constraint block catches it by naming a non-passing form explicitly:
"a cell using 'verified' when the gate parenthetical used 'satisfied' creates a traceability
mismatch." This makes the C-36 requirement self-enforcing within the audit section.
Predicted: 29/29.

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

Lexical consistency requirement: the verb in each Step 0c Contract Verified cell must match
the verb used in the gate parenthetical above. The gate parenthetical uses "satisfied"
(e.g., `Pass (Step 0c exec voice contract satisfied: ...)`). Each cell must therefore use
"satisfied" — not "verified" or any other verb. A cell using a different verb than the gate
parenthetical creates a traceability mismatch and does not pass this section.

| Audience | Verdict | Step 0c Contract Verified |
|----------|---------|--------------------------|
| Exec | [Pass / Fail] | Step 0c exec voice contract satisfied |
| Dev | [Pass / Fail] | Step 0c dev voice contract satisfied |
| Maker | [Pass / Fail] | Step 0c maker voice contract satisfied |
```

**Rubric targeting**:
- C-34: Gate anchor (same as V-02 through V-04). Earns C-34.
- C-36: The constraint block explicitly names the gate parenthetical verb ("satisfied"),
  the required cell verb ("satisfied"), and the failure mode ("a different verb"). The table
  cell template reinforces the requirement. The constraint block makes C-36's pass condition
  self-visible inside the audit section. Earns C-36.
- C-37: Table format. Earns C-37.
- C-35: Cell values attribute the Step 0c contract inline. Earns C-35.
- C-33: Three per-audience rows. Earns C-33.

**Diagnostic value vs V-02 and V-03**: V-02 relies on template-only verb consistency.
V-03 adds an instruction before the table naming the verb requirement. V-05 adds a constraint
block naming the mismatch failure mode explicitly. If all three hit 29/29, template alone
is sufficient and the instruction/constraint approaches add no marginal reliability. If V-03
and V-05 outperform V-02 across runs, explicit prose constraints improve verb consistency.
```
