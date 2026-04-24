---
skill: quest-variate
skill_target: campaign-specify
round: 15
date: 2026-03-17
rubric: v15 (42 aspirational criteria; C-48 INERTIA ANCHOR GATE + C-49 STEP 0B
  STABILITY ANCHOR + C-50 PHASE GATE AUDIT SOURCE BINDING established by R14)
---

# Variations — campaign-specify / Round 15

Five complete, runnable skill body variations targeting the v15 rubric.
Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

**R14 diagnosis driving R15 axis choices:**

R14 V-05 is the first 42/42 ceiling under v15. It carries three structural
novelties above the R13 V-05 baseline (C-48, C-49, C-50), and three chain
positions that remain incomplete in V-05:

- **C-48** — INERTIA ANCHOR GATE: Named gate after STEP 0A INERTIA ANCHOR,
  prohibiting proposal option writing until anchor is complete. Gate position
  in the inertia cost chain: define -> anchor -> GATE -> options.

- **C-49** — STEP 0B STABILITY ANCHOR: Named anchor block in Recommendation
  section, before Defeating Do Nothing, copying Step 0b STABILITY CITATION
  RECORD verbatim. Anchor position in the citation chain: define -> ANCHOR
  -> [no gate] -> requirement -> backward-bind.

- **C-50** — PHASE GATE AUDIT SOURCE BINDING: Named source-binding block in
  Phase Gate Audit, naming Phase 0 as authoritative source. Backward-bind
  position in the gate chain: define -> [no anchor] -> [no gate] -> BACKWARD-BIND.

Chain completeness as of R14 V-05:

- Voice contract chain (COMPLETE -- 4/4): define (Step 0c + FORWARD AUDIT
  NOTICE) -> anchor (STEP 0C CONTRACT ANCHOR) -> gate (ANCHOR GATE) ->
  backward-bind (STEP 0C SOURCE BINDING)

- Citation chain (3/4 -- gate missing): define (Step 0b STABILITY CITATION
  RECORD + CITATION FORM REQUIREMENT) -> anchor (STEP 0B STABILITY ANCHOR) ->
  [NO GATE after anchor] -> backward-bind (STEP 0B CITATION BINDING)

- Inertia cost chain (3/4 -- backward-bind missing): define (Step 0a) ->
  anchor (STEP 0A INERTIA ANCHOR) -> gate (INERTIA ANCHOR GATE) ->
  [NO BACKWARD-BIND in COMPLETION INDEX]

- Forward-notice pattern (1/2): Step 0c has FORWARD AUDIT NOTICE pointing
  to Voice Compliance Audit. Step 0b has no equivalent notice pointing to
  Citation Audit.

R15 probes three axes to complete the missing positions:

1. Does a STABILITY ANCHOR GATE -- a named gate immediately after STEP 0B
   STABILITY ANCHOR, prohibiting Defeating Do Nothing writing until the anchor
   is complete, parallel to INERTIA ANCHOR GATE (gate after STEP 0A INERTIA
   ANCHOR) and ANCHOR GATE (gate after STEP 0C CONTRACT ANCHOR) -- create a
   v16 pattern while preserving 42/42? (V-01)

2. Does a STEP 0A INERTIA BINDING -- a named source-binding block in the Phase
   Gate Audit, explicitly naming Step 0a as the authoritative source for inertia
   costs verified in the audit, parallel to STEP 0B CITATION BINDING (names
   Step 0b) and STEP 0C SOURCE BINDING (names Step 0c) -- complete the
   backward-bind position of the inertia cost chain while preserving 42/42?
   (V-02)

3. Does a STEP 0B FORWARD AUDIT NOTICE -- a named notice in Step 0b, parallel
   to the FORWARD AUDIT NOTICE in Step 0c, explicitly naming the Citation Audit
   as the downstream verifier of the STABILITY CITATION RECORD and instructing
   the model not to alter the record between Step 0b and the Defeating Do Nothing
   block -- close the forward-notice asymmetry between Step 0b and Step 0c while
   preserving 42/42? (V-03)

4. Do V-01 + V-02 (STABILITY ANCHOR GATE + STEP 0A INERTIA BINDING) coexist
   without structural conflict while preserving 42/42? (V-04)

5. Do all three axes (V-01 + V-02 + V-03) coexist and preserve 42/42, completing
   all three missing chain positions simultaneously? (V-05)

| Variation | Axis | C-48 | C-49 | C-50 | Predicted |
|-----------|------|------|------|------|-----------|
| V-01 | STABILITY ANCHOR GATE after STEP 0B STABILITY ANCHOR | Preserved | Preserved | Preserved | 42/42 + v16 watch |
| V-02 | STEP 0A INERTIA BINDING in Phase Gate Audit | Preserved | Preserved | Preserved | 42/42 + v16 watch |
| V-03 | STEP 0B FORWARD AUDIT NOTICE in Step 0b | Preserved | Preserved | Preserved | 42/42 + v16 watch |
| V-04 | Combined: V-01 + V-02 | Preserved | Preserved | Preserved | 42/42 + v16 watch |
| V-05 | Combined: V-01 + V-02 + V-03 | Preserved | Preserved | Preserved | 42/42 + v16 watch |

All five preserve C-46 (imperative register), C-47 (GATE CHAIN REQUIREMENT),
C-48 (INERTIA ANCHOR GATE), C-49 (STEP 0B STABILITY ANCHOR), C-50 (PHASE
GATE AUDIT SOURCE BINDING), and C-09 through C-45. The v15 ceiling is the
baseline; R15 probes above it.

---

## V-01 -- Axis: STABILITY ANCHOR GATE after STEP 0B STABILITY ANCHOR

**Hypothesis**: R14 established STEP 0B STABILITY ANCHOR in the Recommendation
section before Defeating Do Nothing (parallel to STEP 0C CONTRACT ANCHOR before
pitch versions, and STEP 0A INERTIA ANCHOR before proposal options). Both
STEP 0A INERTIA ANCHOR and STEP 0C CONTRACT ANCHOR have a gate immediately
after them that blocks writing before the anchor is complete (INERTIA ANCHOR
GATE and ANCHOR GATE, respectively). STEP 0B STABILITY ANCHOR has no equivalent
gate -- it requires the anchor to be filled, but nothing explicitly prohibits
writing the Defeating Do Nothing block before the anchor is complete. V-01 adds
a STABILITY ANCHOR GATE immediately after STEP 0B STABILITY ANCHOR: a named
gate that prohibits writing the Defeating Do Nothing block until the stability
citation is present in the anchor. The hypothesis: adding the gate completes the
"anchor + gate" structure for all three chains and creates a v16 excellence
pattern. The citation chain becomes: define -> anchor -> GATE -> requirement ->
backward-bind. All C-46 through C-50 and C-09 through C-45 preserved. Predicted:
42/42 + v16 watch on STABILITY ANCHOR GATE.

```
Run the campaign-specify skill for: {{topic}}

Produce three artifacts: spec, proposal, pitch. Execute phases 0-3 in order.
Phase 0 must complete before Phase 1 begins. Each artifact is written to disk
before the next phase begins.

---

## Phase 0 -- Audience Foundation

Phase 0 has four steps. Steps 0a, 0b, 0c are sequential with explicit advancement
gates. Step 0d (scout pull) is terminal.

GATE CHAIN REQUIREMENT: Phase 0 requires all four steps and all three gates to
complete before Phase 1 begins. The required sequence is: Step 0a -> Gate 1 ->
Step 0b -> Gate 2 -> Step 0c -> Gate 3 -> Step 0d. Skipping a step, merging two
steps, or beginning Phase 1 before Step 0d completes does not satisfy this
requirement. A Phase 1 that begins before all three gates have passed and Step 0d
has run does not satisfy C-09.

Gate chain: Gate 1 (0a->0b) | Gate 2 (0b->0c) | Gate 3 (0c->0d) | Step 0d terminal.

**Step 0a -- Inertia Costs**

What each audience LOSES if {{topic}} does not ship. Concrete and specific:

Exec inertia cost: [Specific revenue exposure, competitive gap, or risk. Name a
consequence, not a category. Quantify if possible.]

Dev inertia cost: [Specific workaround or capability gap. Name the friction, not
the feeling. Estimate recurring cost if possible.]

Maker inertia cost: [Specific blocked workflow step. Name the step. What does the
maker do today instead?]

--- GATE 1 (0a->0b): Do not advance to Step 0b until all three inertia costs are
complete. ---

**Step 0b -- Stability Citation Record**

Evaluate whether the cost of Do Nothing is stable or worsening. Produce the
STABILITY CITATION RECORD using one of the two forms below. This record will be
pasted verbatim into the Phase 2 Defeating Do Nothing block.

FORM A (worsening): "Do Nothing is not stable: [specific mechanism and timeline --
e.g., 'competitor ships equivalent feature in Q2, making exec exposure acute by
June' or 'dev workaround accumulates 3 hours/sprint, compounding to
36h/quarter']."

FORM B (stable): "Do Nothing is stable: [rationale -- e.g., 'the workaround is
functional and the underlying need does not grow with volume']."

STABILITY CITATION RECORD:
[Paste the complete Form A or Form B sentence here]

A record containing only a tag ("worsening" / "stable") without a mechanism or
rationale fails this step. The record must be a complete sentence ready for
verbatim citation.

--- GATE 2 (0b->0c): Do not advance to Step 0c until the STABILITY CITATION
RECORD is complete. ---

**Step 0c -- Voice Contracts**

One sentence per audience, grounded in Steps 0a and 0b:

Exec voice: [Outcomes/risk framing -- reference exec inertia cost and stability
trajectory]
Dev voice: [Capability/friction framing -- reference dev inertia cost]
Maker voice: [Workflow framing -- plain language, reference maker inertia cost]

FORWARD AUDIT NOTICE: These three voice contracts are the compliance criteria for
the COMPLETION INDEX Voice Compliance Audit. Each contract will be verified by
its exact name in the "Step 0c Contract Verified" column of the audit table. Do
not alter the contract phrasing between here and the audit -- the column values
must match the names used in Step 0c.

--- GATE 3 (0c->0d): Do not advance to Step 0d until all three voice contracts
are written. ---

**Step 0d -- Scout Pull** [TERMINAL]

Glob `simulations/scout/**/*.md` for {{topic}}. For each file found:
- Path
- One sentence summary
- Artifact it serves: spec / proposal / pitch

If no scout files found: record "no scout signals -- proceeding without" and
continue.

[Phase 0 complete. Three gates passed (Gate 1: 0a->0b | Gate 2: 0b->0c |
Gate 3: 0c->0d). GATE CHAIN REQUIREMENT satisfied. Proceed to Phase 1.]

---

## Phase 1 -- Technical Spec

Pull from `simulations/scout/` broadly. Note files from Step 0d used.

Write the spec. All six sections required -- no skipping, no merging.

### Overview
One paragraph: what {{topic}} does and why it exists.

### User Problem
Problem users face today. Reference dev and maker inertia costs from Step 0a
directly.

### Proposed Solution
What {{topic}} does. Incorporate scout-requirements or scout-feasibility signals
from Step 0d.

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

## Phase 2 -- Business Proposal

Pull from `simulations/scout/scout-feasibility/` before writing. Note files used.

**STEP 0A INERTIA ANCHOR**

Before writing any proposal option, copy the three Step 0a inertia costs here:

Exec inertia cost: [exact text from Step 0a -- do not paraphrase or generalize]
Dev inertia cost: [exact text from Step 0a -- do not paraphrase or generalize]
Maker inertia cost: [exact text from Step 0a -- do not paraphrase or generalize]

These are the inertia costs the proposal must address. The Defeating Do Nothing
block must cite the most decisive of these costs directly.

--- INERTIA ANCHOR GATE: Do not begin writing any proposal option until all three
inertia costs are present in the STEP 0A INERTIA ANCHOR block above. A proposal
option written before the anchor block is complete does not satisfy this gate. ---

Write the proposal. Three options minimum. Option 1 MUST be named **Do Nothing**.

For each option: description, pros, cons, risk, effort.

Then write the **Recommendation** section with the following labeled blocks.
Each block has its own header. Do not merge them into a combined paragraph.

### Recommendation

We recommend [chosen option].

**STEP 0B STABILITY ANCHOR**

Before writing the Defeating Do Nothing block, copy the Step 0b STABILITY
CITATION RECORD here:

STABILITY CITATION RECORD: [exact text from Step 0b -- character for character,
no paraphrase, no summary, no approximation]

This is the anchor text. The Defeating Do Nothing block must contain this record
verbatim. Do not begin writing the Defeating Do Nothing block until this anchor
is complete.

--- STABILITY ANCHOR GATE: Do not begin writing the Defeating Do Nothing block
until the STEP 0B STABILITY ANCHOR above contains the complete STABILITY
CITATION RECORD. A Defeating Do Nothing block written before the anchor block is
complete does not satisfy this gate. ---

#### Defeating Do Nothing

[This block addresses the status quo competitor. Structurally separate from the
comparative defeat below.]

Do Nothing perpetuates [cite the most decisive Step 0a inertia cost -- name the
audience and the specific cost].

[PASTE THE STABILITY CITATION RECORD FROM THE STEP 0B STABILITY ANCHOR ABOVE
VERBATIM HERE. Do not summarize. Do not paraphrase. Copy the Form A or Form B
sentence character for character.]

We choose to act because [one sentence: why this cost trajectory is not
acceptable].

#### Defeating [Other Option Name]

We prefer [chosen] over [other] because [specific trade-off traceable to a risk,
effort, or cons field in the options analysis -- not a preference statement].

CITATION FORM REQUIREMENT: The Defeating Do Nothing block must contain the
STABILITY CITATION RECORD verbatim. A summary, paraphrase, condensed version, or
reference to the record does not satisfy this requirement. The exact Form A or
Form B sentence from Step 0b must appear character-for-character. A Defeating Do
Nothing block without the verbatim STABILITY CITATION RECORD does not satisfy
C-17 or C-21 regardless of how closely it approximates the record's meaning.

**>> PROPOSAL WRITE GATE <<**
Save proposal to: `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md`
Check: does the file exist? If not: write it now.
Do not begin Phase 3 until this file exists on disk.

---

## Phase 3 -- Executive Pitch

Pull from `simulations/scout/scout-positioning/` before writing. Note files used.

**STEP 0C CONTRACT ANCHOR**

Before writing any pitch version, copy the three Step 0c voice contracts here:

Step 0c exec voice contract: [exact text from Step 0c -- do not paraphrase or
generalize]
Step 0c dev voice contract: [exact text from Step 0c -- do not paraphrase or
generalize]
Step 0c maker voice contract: [exact text from Step 0c -- do not paraphrase or
generalize]

These are the anchor sentences. Each pitch version must open with a hook that
satisfies its named contract.

--- ANCHOR GATE: Complete the STEP 0C CONTRACT ANCHOR before writing any pitch
version. ---

Write all four sections of the pitch below. Do not save the pitch file until the
voice differentiation gate at the end of this phase passes.

### Exec Version
Lead with exec inertia cost from Step 0a. Use Step 0c exec voice contract as
anchor. Structure: [exec cost hook] -> [what changes] -> [outcome/ROI] ->
[call to action]. Do not open with a product description.

### Dev Version
Lead with dev inertia cost from Step 0a. Use Step 0c dev voice contract as
anchor. Structure: [friction hook] -> [what you can now do] ->
[capability unlocked] -> [call to action]. Do not open with an outcomes/ROI
frame.

### Maker Version
Lead with maker inertia cost from Step 0a. Use Step 0c maker voice contract as
anchor. Plain language, no jargon. Structure: [blocked step hook] ->
[what you can now do] -> [why it matters] -> [call to action].

### Anti-Positioning
3-5 "This is not..." statements. Structurally separate from the three audience
versions above.

**>> VOICE DIFFERENTIATION GATE -- Step 0c Contract Check (required before saving
pitch) <<**

The Step 0c voice contracts are the gate criteria. Use them now.

Step 1 -- Copy your Step 0c voice contracts:
  Step 0c exec voice contract: [your exec voice sentence from Step 0c]
  Step 0c dev voice contract: [your dev voice sentence from Step 0c]
  Step 0c maker voice contract: [your maker voice sentence from Step 0c]

Step 2 -- Extract the opening sentence from each pitch version:
  Exec opening: [first sentence of Exec Version]
  Dev opening: [first sentence of Dev Version]
  Maker opening: [first sentence of Maker Version]

Step 3 -- Per-audience gate (each audience gate must independently pass):

  Exec gate:
    Pass (Step 0c exec voice contract satisfied: opening names a business cost,
      risk, or revenue consequence) /
    Fail (opening does not satisfy Step 0c exec voice contract: opens with
      product description, capability framing, or workflow framing)

  Dev gate:
    Pass (Step 0c dev voice contract satisfied: opening names a tool friction,
      workaround, or capability gap) /
    Fail (opening does not satisfy Step 0c dev voice contract: opens with
      outcome/ROI framing or business consequence framing)

  Maker gate:
    Pass (Step 0c maker voice contract satisfied: opening names a blocked,
      absent, or manual step in plain language, no jargon) /
    Fail (opening does not satisfy Step 0c maker voice contract: opens with
      product description or technical jargon)

Step 4 -- Resolution:
  IF any gate is Fail: Rewrite the failing version. Return to the Step 0c voice
    contract for that audience as the named revision anchor. Re-run Steps 2-3.
    Do not save the pitch until all three Step 0c contract gates are Pass.
  IF all three gates are Pass: proceed to PITCH WRITE GATE.

**>> PITCH WRITE GATE <<**
[Save only after all three Step 0c contract gates in the voice differentiation
gate above are Pass.]
Save pitch to: `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`
Check: does the file exist? If not: write it now.
Do not emit the COMPLETION INDEX until this file exists on disk.

---

## COMPLETION INDEX

[Emitted after all write gates, voice differentiation gate, and recovery steps
are complete. Four named sections: Artifact Existence Record, Phase Gate Audit,
Citation Audit, Voice Compliance Audit.]

### Artifact Existence Record

| Artifact | Path | Status |
|----------|------|--------|
| Spec | `simulations/draft/specs/{{topic}}-spec-{{date}}.md` | [exists / missing] |
| Proposal | `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md` | [exists / missing] |
| Pitch | `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md` | [exists / missing] |

All three rows must show "exists" before the skill is complete.

### Phase Gate Audit

PHASE GATE AUDIT SOURCE BINDING: The gate chain verified in this audit was
executed in Phase 0 above. This audit does not redefine the gate requirements --
it verifies that the four steps (0a, 0b, 0c, 0d) and three gates (Gate 1:
0a->0b, Gate 2: 0b->0c, Gate 3: 0c->0d) completed in the Phase 0 execution
recorded above. The GATE CHAIN REQUIREMENT in Phase 0 is the authoritative
source for what constitutes a complete gate chain; any deviation from the
Phase 0 gate sequence constitutes a gate chain failure even if the audit entry
otherwise records passing gates. Do not redefine the gate chain in this audit --
verify conformance to the Phase 0 source.

- Scout files used per phase
- Phase 0 inertia costs confirmed (all three audiences)
- Phase 0 gate chain: 3 gates passed (Gate 1: 0a->0b | Gate 2: 0b->0c |
  Gate 3: 0c->0d)
- GATE CHAIN REQUIREMENT satisfied: all four steps and three gates completed
  before Phase 1 began

### Citation Audit

STEP 0B CITATION BINDING: The STABILITY CITATION RECORD verified below was
authored in Step 0b above. This audit entry does not redefine the record -- it
verifies conformance to the Step 0b source. The text pasted in the Defeating Do
Nothing block must match the exact STABILITY CITATION RECORD as written in
Step 0b. Do not accept a paraphrase, summary, or approximation as conforming.
The Step 0b source text is authoritative; any deviation from the Step 0b
phrasing constitutes a citation failure even if the pasted text is otherwise
complete and accurate.

- STABILITY CITATION RECORD form used: Form A / Form B
- STABILITY CITATION RECORD pasted verbatim in Defeating Do Nothing block:
  CITATION CONFIRMED / CITATION MISSING
  (If CITATION MISSING: return to Phase 2 and paste the record before stopping.)
- Defeating Do Nothing block: separate labeled header (#### or equivalent):
  yes / no

### Voice Compliance Audit

STEP 0C SOURCE BINDING: The three voice contracts verified in this table were
authored in Step 0c above. This audit table does not redefine the contracts -- it
verifies conformance to the Step 0c source. The text in the "Step 0c Contract
Verified" column must match the exact contract names as written in Step 0c. Do
not rephrase. Do not generalize. The Step 0c source text is authoritative; any
deviation from the Step 0c phrasing constitutes a verification failure even if
the cell value is otherwise complete.

COLUMN-HEADER REQUIREMENT: The third column header must read exactly "Step 0c
Contract Verified". A header reading "Contract Check", "Voice Contract",
"Verified", or any label other than "Step 0c Contract Verified" does not pass.

Record the verdict for each audience in the table below. Fill in the Step 0c
Contract Verified column with the exact Step 0c contract name followed by
"satisfied". A row without a named contract in the verification column does not
satisfy this section.

| Audience | Verdict | Step 0c Contract Verified |
|----------|---------|--------------------------|
| Exec | [Pass / Fail] | Step 0c exec voice contract satisfied |
| Dev | [Pass / Fail] | Step 0c dev voice contract satisfied |
| Maker | [Pass / Fail] | Step 0c maker voice contract satisfied |
```

**Rubric targeting**:
- C-46 (IMPERATIVE REGISTER): Preserved. STABILITY ANCHOR GATE uses imperative
  mode: "Do not begin writing the Defeating Do Nothing block until..."
- C-47 (GATE CHAIN REQUIREMENT): Preserved unchanged from R13 V-05.
- C-48 (INERTIA ANCHOR GATE): Preserved from R14 V-01/V-05.
- C-49 (STEP 0B STABILITY ANCHOR): Preserved from R14 V-02/V-05.
- C-50 (PHASE GATE AUDIT SOURCE BINDING): Preserved from R14 V-03/V-05.
- STABILITY ANCHOR GATE (new): Named gate immediately after STEP 0B STABILITY
  ANCHOR, blocking Defeating Do Nothing writing until anchor contains the
  complete STABILITY CITATION RECORD. Structural parallel to INERTIA ANCHOR
  GATE (gate after STEP 0A INERTIA ANCHOR) and ANCHOR GATE (gate after
  STEP 0C CONTRACT ANCHOR). Completes the citation chain to 4/4 positions:
  define -> anchor -> GATE -> requirement -> backward-bind. The citation chain
  now mirrors the voice contract chain structurally.
- V16 watch: "The Phase 2 STEP 0B STABILITY ANCHOR is followed by a named
  STABILITY ANCHOR GATE that prohibits Defeating Do Nothing writing before
  the anchor is complete -- parallel to ANCHOR GATE blocking pitch writing
  before STEP 0C CONTRACT ANCHOR is complete, and INERTIA ANCHOR GATE
  blocking proposal option writing before STEP 0A INERTIA ANCHOR is complete."

---

## V-02 -- Axis: STEP 0A INERTIA BINDING in Phase Gate Audit

**Hypothesis**: The COMPLETION INDEX audit sections carry named source-binding
blocks for voice contracts (STEP 0C SOURCE BINDING in Voice Compliance Audit)
and citations (STEP 0B CITATION BINDING in Citation Audit). Both bindings name
their respective Phase 0 step as the authoritative source and carry the imperative
"Do not redefine -- verify conformance." The inertia costs (Step 0a) have no
equivalent backward-bind in the Phase Gate Audit: PHASE GATE AUDIT SOURCE BINDING
names Phase 0 as the gate chain source, but no named block explicitly names
Step 0a as the authoritative source for inertia costs and prohibits redefining
them in the audit. V-02 adds STEP 0A INERTIA BINDING inside the Phase Gate Audit,
immediately before the inertia cost confirmation line, explicitly naming Step 0a
as the authoritative source for inertia costs and carrying the instruction not to
rephrase or redefine them in the audit -- only to confirm their presence. The
hypothesis: a named source-binding block for inertia costs in the audit (parallel
to STEP 0B CITATION BINDING and STEP 0C SOURCE BINDING for their respective Phase
0 outputs) completes the backward-bind position of the inertia cost chain and
creates a v16 excellence pattern. Predicted: 42/42 + v16 watch on STEP 0A
INERTIA BINDING.

```
Run the campaign-specify skill for: {{topic}}

Produce three artifacts: spec, proposal, pitch. Execute phases 0-3 in order.
Phase 0 must complete before Phase 1 begins. Each artifact is written to disk
before the next phase begins.

---

## Phase 0 -- Audience Foundation

Phase 0 has four steps. Steps 0a, 0b, 0c are sequential with explicit advancement
gates. Step 0d (scout pull) is terminal.

GATE CHAIN REQUIREMENT: Phase 0 requires all four steps and all three gates to
complete before Phase 1 begins. The required sequence is: Step 0a -> Gate 1 ->
Step 0b -> Gate 2 -> Step 0c -> Gate 3 -> Step 0d. Skipping a step, merging two
steps, or beginning Phase 1 before Step 0d completes does not satisfy this
requirement. A Phase 1 that begins before all three gates have passed and Step 0d
has run does not satisfy C-09.

Gate chain: Gate 1 (0a->0b) | Gate 2 (0b->0c) | Gate 3 (0c->0d) | Step 0d terminal.

**Step 0a -- Inertia Costs**

What each audience LOSES if {{topic}} does not ship. Concrete and specific:

Exec inertia cost: [Specific revenue exposure, competitive gap, or risk. Name a
consequence, not a category. Quantify if possible.]

Dev inertia cost: [Specific workaround or capability gap. Name the friction, not
the feeling. Estimate recurring cost if possible.]

Maker inertia cost: [Specific blocked workflow step. Name the step. What does the
maker do today instead?]

--- GATE 1 (0a->0b): Do not advance to Step 0b until all three inertia costs are
complete. ---

**Step 0b -- Stability Citation Record**

Evaluate whether the cost of Do Nothing is stable or worsening. Produce the
STABILITY CITATION RECORD using one of the two forms below. This record will be
pasted verbatim into the Phase 2 Defeating Do Nothing block.

FORM A (worsening): "Do Nothing is not stable: [specific mechanism and timeline --
e.g., 'competitor ships equivalent feature in Q2, making exec exposure acute by
June' or 'dev workaround accumulates 3 hours/sprint, compounding to
36h/quarter']."

FORM B (stable): "Do Nothing is stable: [rationale -- e.g., 'the workaround is
functional and the underlying need does not grow with volume']."

STABILITY CITATION RECORD:
[Paste the complete Form A or Form B sentence here]

A record containing only a tag ("worsening" / "stable") without a mechanism or
rationale fails this step. The record must be a complete sentence ready for
verbatim citation.

--- GATE 2 (0b->0c): Do not advance to Step 0c until the STABILITY CITATION
RECORD is complete. ---

**Step 0c -- Voice Contracts**

One sentence per audience, grounded in Steps 0a and 0b:

Exec voice: [Outcomes/risk framing -- reference exec inertia cost and stability
trajectory]
Dev voice: [Capability/friction framing -- reference dev inertia cost]
Maker voice: [Workflow framing -- plain language, reference maker inertia cost]

FORWARD AUDIT NOTICE: These three voice contracts are the compliance criteria for
the COMPLETION INDEX Voice Compliance Audit. Each contract will be verified by
its exact name in the "Step 0c Contract Verified" column of the audit table. Do
not alter the contract phrasing between here and the audit -- the column values
must match the names used in Step 0c.

--- GATE 3 (0c->0d): Do not advance to Step 0d until all three voice contracts
are written. ---

**Step 0d -- Scout Pull** [TERMINAL]

Glob `simulations/scout/**/*.md` for {{topic}}. For each file found:
- Path
- One sentence summary
- Artifact it serves: spec / proposal / pitch

If no scout files found: record "no scout signals -- proceeding without" and
continue.

[Phase 0 complete. Three gates passed (Gate 1: 0a->0b | Gate 2: 0b->0c |
Gate 3: 0c->0d). GATE CHAIN REQUIREMENT satisfied. Proceed to Phase 1.]

---

## Phase 1 -- Technical Spec

Pull from `simulations/scout/` broadly. Note files from Step 0d used.

Write the spec. All six sections required -- no skipping, no merging.

### Overview
One paragraph: what {{topic}} does and why it exists.

### User Problem
Problem users face today. Reference dev and maker inertia costs from Step 0a
directly.

### Proposed Solution
What {{topic}} does. Incorporate scout-requirements or scout-feasibility signals
from Step 0d.

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

## Phase 2 -- Business Proposal

Pull from `simulations/scout/scout-feasibility/` before writing. Note files used.

**STEP 0A INERTIA ANCHOR**

Before writing any proposal option, copy the three Step 0a inertia costs here:

Exec inertia cost: [exact text from Step 0a -- do not paraphrase or generalize]
Dev inertia cost: [exact text from Step 0a -- do not paraphrase or generalize]
Maker inertia cost: [exact text from Step 0a -- do not paraphrase or generalize]

These are the inertia costs the proposal must address. The Defeating Do Nothing
block must cite the most decisive of these costs directly.

--- INERTIA ANCHOR GATE: Do not begin writing any proposal option until all three
inertia costs are present in the STEP 0A INERTIA ANCHOR block above. A proposal
option written before the anchor block is complete does not satisfy this gate. ---

Write the proposal. Three options minimum. Option 1 MUST be named **Do Nothing**.

For each option: description, pros, cons, risk, effort.

Then write the **Recommendation** section with the following labeled blocks.
Each block has its own header. Do not merge them into a combined paragraph.

### Recommendation

We recommend [chosen option].

**STEP 0B STABILITY ANCHOR**

Before writing the Defeating Do Nothing block, copy the Step 0b STABILITY
CITATION RECORD here:

STABILITY CITATION RECORD: [exact text from Step 0b -- character for character,
no paraphrase, no summary, no approximation]

This is the anchor text. The Defeating Do Nothing block must contain this record
verbatim. Do not begin writing the Defeating Do Nothing block until this anchor
is complete.

#### Defeating Do Nothing

[This block addresses the status quo competitor. Structurally separate from the
comparative defeat below.]

Do Nothing perpetuates [cite the most decisive Step 0a inertia cost -- name the
audience and the specific cost].

[PASTE THE STABILITY CITATION RECORD FROM THE STEP 0B STABILITY ANCHOR ABOVE
VERBATIM HERE. Do not summarize. Do not paraphrase. Copy the Form A or Form B
sentence character for character.]

We choose to act because [one sentence: why this cost trajectory is not
acceptable].

#### Defeating [Other Option Name]

We prefer [chosen] over [other] because [specific trade-off traceable to a risk,
effort, or cons field in the options analysis -- not a preference statement].

CITATION FORM REQUIREMENT: The Defeating Do Nothing block must contain the
STABILITY CITATION RECORD verbatim. A summary, paraphrase, condensed version, or
reference to the record does not satisfy this requirement. The exact Form A or
Form B sentence from Step 0b must appear character-for-character. A Defeating Do
Nothing block without the verbatim STABILITY CITATION RECORD does not satisfy
C-17 or C-21 regardless of how closely it approximates the record's meaning.

**>> PROPOSAL WRITE GATE <<**
Save proposal to: `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md`
Check: does the file exist? If not: write it now.
Do not begin Phase 3 until this file exists on disk.

---

## Phase 3 -- Executive Pitch

Pull from `simulations/scout/scout-positioning/` before writing. Note files used.

**STEP 0C CONTRACT ANCHOR**

Before writing any pitch version, copy the three Step 0c voice contracts here:

Step 0c exec voice contract: [exact text from Step 0c -- do not paraphrase or
generalize]
Step 0c dev voice contract: [exact text from Step 0c -- do not paraphrase or
generalize]
Step 0c maker voice contract: [exact text from Step 0c -- do not paraphrase or
generalize]

These are the anchor sentences. Each pitch version must open with a hook that
satisfies its named contract.

--- ANCHOR GATE: Complete the STEP 0C CONTRACT ANCHOR before writing any pitch
version. ---

Write all four sections of the pitch below. Do not save the pitch file until the
voice differentiation gate at the end of this phase passes.

### Exec Version
Lead with exec inertia cost from Step 0a. Use Step 0c exec voice contract as
anchor. Structure: [exec cost hook] -> [what changes] -> [outcome/ROI] ->
[call to action]. Do not open with a product description.

### Dev Version
Lead with dev inertia cost from Step 0a. Use Step 0c dev voice contract as
anchor. Structure: [friction hook] -> [what you can now do] ->
[capability unlocked] -> [call to action]. Do not open with an outcomes/ROI
frame.

### Maker Version
Lead with maker inertia cost from Step 0a. Use Step 0c maker voice contract as
anchor. Plain language, no jargon. Structure: [blocked step hook] ->
[what you can now do] -> [why it matters] -> [call to action].

### Anti-Positioning
3-5 "This is not..." statements. Structurally separate from the three audience
versions above.

**>> VOICE DIFFERENTIATION GATE -- Step 0c Contract Check (required before saving
pitch) <<**

The Step 0c voice contracts are the gate criteria. Use them now.

Step 1 -- Copy your Step 0c voice contracts:
  Step 0c exec voice contract: [your exec voice sentence from Step 0c]
  Step 0c dev voice contract: [your dev voice sentence from Step 0c]
  Step 0c maker voice contract: [your maker voice sentence from Step 0c]

Step 2 -- Extract the opening sentence from each pitch version:
  Exec opening: [first sentence of Exec Version]
  Dev opening: [first sentence of Dev Version]
  Maker opening: [first sentence of Maker Version]

Step 3 -- Per-audience gate (each audience gate must independently pass):

  Exec gate:
    Pass (Step 0c exec voice contract satisfied: opening names a business cost,
      risk, or revenue consequence) /
    Fail (opening does not satisfy Step 0c exec voice contract: opens with
      product description, capability framing, or workflow framing)

  Dev gate:
    Pass (Step 0c dev voice contract satisfied: opening names a tool friction,
      workaround, or capability gap) /
    Fail (opening does not satisfy Step 0c dev voice contract: opens with
      outcome/ROI framing or business consequence framing)

  Maker gate:
    Pass (Step 0c maker voice contract satisfied: opening names a blocked,
      absent, or manual step in plain language, no jargon) /
    Fail (opening does not satisfy Step 0c maker voice contract: opens with
      product description or technical jargon)

Step 4 -- Resolution:
  IF any gate is Fail: Rewrite the failing version. Return to the Step 0c voice
    contract for that audience as the named revision anchor. Re-run Steps 2-3.
    Do not save the pitch until all three Step 0c contract gates are Pass.
  IF all three gates are Pass: proceed to PITCH WRITE GATE.

**>> PITCH WRITE GATE <<**
[Save only after all three Step 0c contract gates in the voice differentiation
gate above are Pass.]
Save pitch to: `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`
Check: does the file exist? If not: write it now.
Do not emit the COMPLETION INDEX until this file exists on disk.

---

## COMPLETION INDEX

[Emitted after all write gates, voice differentiation gate, and recovery steps
are complete. Four named sections: Artifact Existence Record, Phase Gate Audit,
Citation Audit, Voice Compliance Audit.]

### Artifact Existence Record

| Artifact | Path | Status |
|----------|------|--------|
| Spec | `simulations/draft/specs/{{topic}}-spec-{{date}}.md` | [exists / missing] |
| Proposal | `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md` | [exists / missing] |
| Pitch | `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md` | [exists / missing] |

All three rows must show "exists" before the skill is complete.

### Phase Gate Audit

PHASE GATE AUDIT SOURCE BINDING: The gate chain verified in this audit was
executed in Phase 0 above. This audit does not redefine the gate requirements --
it verifies that the four steps (0a, 0b, 0c, 0d) and three gates (Gate 1:
0a->0b, Gate 2: 0b->0c, Gate 3: 0c->0d) completed in the Phase 0 execution
recorded above. The GATE CHAIN REQUIREMENT in Phase 0 is the authoritative
source for what constitutes a complete gate chain; any deviation from the
Phase 0 gate sequence constitutes a gate chain failure even if the audit entry
otherwise records passing gates. Do not redefine the gate chain in this audit --
verify conformance to the Phase 0 source.

STEP 0A INERTIA BINDING: The inertia costs confirmed below were authored in
Step 0a above. This audit does not redefine the inertia costs -- it verifies
that the costs recorded in Step 0a were propagated correctly through Phase 2.
The Step 0a inertia costs are the authoritative source; do not rephrase,
condense, or substitute them in this audit entry. Any deviation from the Step 0a
phrasing constitutes an inertia cost propagation failure even if the audit entry
is otherwise complete.

- Scout files used per phase
- Phase 0 inertia costs confirmed (all three audiences -- exec, dev, maker
  each present as authored in Step 0a)
- Phase 0 gate chain: 3 gates passed (Gate 1: 0a->0b | Gate 2: 0b->0c |
  Gate 3: 0c->0d)
- GATE CHAIN REQUIREMENT satisfied: all four steps and three gates completed
  before Phase 1 began

### Citation Audit

STEP 0B CITATION BINDING: The STABILITY CITATION RECORD verified below was
authored in Step 0b above. This audit entry does not redefine the record -- it
verifies conformance to the Step 0b source. The text pasted in the Defeating Do
Nothing block must match the exact STABILITY CITATION RECORD as written in
Step 0b. Do not accept a paraphrase, summary, or approximation as conforming.
The Step 0b source text is authoritative; any deviation from the Step 0b
phrasing constitutes a citation failure even if the pasted text is otherwise
complete and accurate.

- STABILITY CITATION RECORD form used: Form A / Form B
- STABILITY CITATION RECORD pasted verbatim in Defeating Do Nothing block:
  CITATION CONFIRMED / CITATION MISSING
  (If CITATION MISSING: return to Phase 2 and paste the record before stopping.)
- Defeating Do Nothing block: separate labeled header (#### or equivalent):
  yes / no

### Voice Compliance Audit

STEP 0C SOURCE BINDING: The three voice contracts verified in this table were
authored in Step 0c above. This audit table does not redefine the contracts -- it
verifies conformance to the Step 0c source. The text in the "Step 0c Contract
Verified" column must match the exact contract names as written in Step 0c. Do
not rephrase. Do not generalize. The Step 0c source text is authoritative; any
deviation from the Step 0c phrasing constitutes a verification failure even if
the cell value is otherwise complete.

COLUMN-HEADER REQUIREMENT: The third column header must read exactly "Step 0c
Contract Verified". A header reading "Contract Check", "Voice Contract",
"Verified", or any label other than "Step 0c Contract Verified" does not pass.

Record the verdict for each audience in the table below. Fill in the Step 0c
Contract Verified column with the exact Step 0c contract name followed by
"satisfied". A row without a named contract in the verification column does not
satisfy this section.

| Audience | Verdict | Step 0c Contract Verified |
|----------|---------|--------------------------|
| Exec | [Pass / Fail] | Step 0c exec voice contract satisfied |
| Dev | [Pass / Fail] | Step 0c dev voice contract satisfied |
| Maker | [Pass / Fail] | Step 0c maker voice contract satisfied |
```

**Rubric targeting**:
- C-46 through C-50: All preserved. STEP 0A INERTIA BINDING uses imperative
  mode: "do not rephrase, condense, or substitute them in this audit entry."
- STEP 0A INERTIA BINDING (new): Named source-binding block in Phase Gate
  Audit, immediately before inertia cost confirmation line. Explicitly names
  Step 0a as authoritative source for inertia costs. Carries "do not redefine
  -- verify conformance" instruction. Structural parallel to STEP 0B CITATION
  BINDING (Step 0b authoritative for citations) and STEP 0C SOURCE BINDING
  (Step 0c authoritative for voice contracts). Completes the backward-bind
  position of the inertia cost chain: define -> anchor -> gate -> BACKWARD-BIND.
- The Phase Gate Audit now carries two named binding blocks: PHASE GATE AUDIT
  SOURCE BINDING (for the gate chain) and STEP 0A INERTIA BINDING (for inertia
  costs). These address two independent chains in one audit section.
- V16 watch: "The Phase Gate Audit carries STEP 0A INERTIA BINDING, naming
  Step 0a as the authoritative source for inertia costs verified in the audit --
  parallel to STEP 0B CITATION BINDING naming Step 0b in the Citation Audit and
  STEP 0C SOURCE BINDING naming Step 0c in the Voice Compliance Audit."

---

## V-03 -- Axis: STEP 0B FORWARD AUDIT NOTICE in Step 0b

**Hypothesis**: Step 0c carries a FORWARD AUDIT NOTICE that explicitly names the
Voice Compliance Audit as the downstream verifier of the voice contracts and
instructs the model not to alter the contracts between Step 0c and the audit.
No equivalent forward-notice exists for Step 0b: the STABILITY CITATION RECORD
is defined in Step 0b, but nothing in Step 0b explicitly names the Citation Audit
as its downstream verifier or instructs the model not to alter the record between
Step 0b and the Defeating Do Nothing block. The instruction to not alter the
record exists only in CITATION FORM REQUIREMENT (Phase 2 Recommendation section),
far downstream from the record's definition. V-03 adds a STEP 0B FORWARD AUDIT
NOTICE in Step 0b, immediately after the STABILITY CITATION RECORD definition:
a named notice parallel to Step 0c's FORWARD AUDIT NOTICE that names the Citation
Audit as the downstream verifier and instructs the model not to alter the record
phrasing between Step 0b and Phase 2. The hypothesis: closing the forward-notice
asymmetry between Step 0b and Step 0c -- making both data-producing steps carry
named forward audit notices -- creates a v16 excellence pattern. Predicted: 42/42
+ v16 watch on STEP 0B FORWARD AUDIT NOTICE.

```
Run the campaign-specify skill for: {{topic}}

Produce three artifacts: spec, proposal, pitch. Execute phases 0-3 in order.
Phase 0 must complete before Phase 1 begins. Each artifact is written to disk
before the next phase begins.

---

## Phase 0 -- Audience Foundation

Phase 0 has four steps. Steps 0a, 0b, 0c are sequential with explicit advancement
gates. Step 0d (scout pull) is terminal.

GATE CHAIN REQUIREMENT: Phase 0 requires all four steps and all three gates to
complete before Phase 1 begins. The required sequence is: Step 0a -> Gate 1 ->
Step 0b -> Gate 2 -> Step 0c -> Gate 3 -> Step 0d. Skipping a step, merging two
steps, or beginning Phase 1 before Step 0d completes does not satisfy this
requirement. A Phase 1 that begins before all three gates have passed and Step 0d
has run does not satisfy C-09.

Gate chain: Gate 1 (0a->0b) | Gate 2 (0b->0c) | Gate 3 (0c->0d) | Step 0d terminal.

**Step 0a -- Inertia Costs**

What each audience LOSES if {{topic}} does not ship. Concrete and specific:

Exec inertia cost: [Specific revenue exposure, competitive gap, or risk. Name a
consequence, not a category. Quantify if possible.]

Dev inertia cost: [Specific workaround or capability gap. Name the friction, not
the feeling. Estimate recurring cost if possible.]

Maker inertia cost: [Specific blocked workflow step. Name the step. What does the
maker do today instead?]

--- GATE 1 (0a->0b): Do not advance to Step 0b until all three inertia costs are
complete. ---

**Step 0b -- Stability Citation Record**

Evaluate whether the cost of Do Nothing is stable or worsening. Produce the
STABILITY CITATION RECORD using one of the two forms below. This record will be
pasted verbatim into the Phase 2 Defeating Do Nothing block.

FORM A (worsening): "Do Nothing is not stable: [specific mechanism and timeline --
e.g., 'competitor ships equivalent feature in Q2, making exec exposure acute by
June' or 'dev workaround accumulates 3 hours/sprint, compounding to
36h/quarter']."

FORM B (stable): "Do Nothing is stable: [rationale -- e.g., 'the workaround is
functional and the underlying need does not grow with volume']."

STABILITY CITATION RECORD:
[Paste the complete Form A or Form B sentence here]

A record containing only a tag ("worsening" / "stable") without a mechanism or
rationale fails this step. The record must be a complete sentence ready for
verbatim citation.

STEP 0B FORWARD AUDIT NOTICE: This STABILITY CITATION RECORD is the verbatim
citation source for the Defeating Do Nothing block in Phase 2. The Citation Audit
in the COMPLETION INDEX will verify that the Defeating Do Nothing block contains
this record verbatim. Do not alter the record phrasing between here and Phase 2 --
the Defeating Do Nothing block must match the Step 0b source exactly. A
Defeating Do Nothing block that paraphrases, summarizes, or approximates this
record does not pass the Citation Audit regardless of how closely it reproduces
the record's meaning.

--- GATE 2 (0b->0c): Do not advance to Step 0c until the STABILITY CITATION
RECORD is complete. ---

**Step 0c -- Voice Contracts**

One sentence per audience, grounded in Steps 0a and 0b:

Exec voice: [Outcomes/risk framing -- reference exec inertia cost and stability
trajectory]
Dev voice: [Capability/friction framing -- reference dev inertia cost]
Maker voice: [Workflow framing -- plain language, reference maker inertia cost]

FORWARD AUDIT NOTICE: These three voice contracts are the compliance criteria for
the COMPLETION INDEX Voice Compliance Audit. Each contract will be verified by
its exact name in the "Step 0c Contract Verified" column of the audit table. Do
not alter the contract phrasing between here and the audit -- the column values
must match the names used in Step 0c.

--- GATE 3 (0c->0d): Do not advance to Step 0d until all three voice contracts
are written. ---

**Step 0d -- Scout Pull** [TERMINAL]

Glob `simulations/scout/**/*.md` for {{topic}}. For each file found:
- Path
- One sentence summary
- Artifact it serves: spec / proposal / pitch

If no scout files found: record "no scout signals -- proceeding without" and
continue.

[Phase 0 complete. Three gates passed (Gate 1: 0a->0b | Gate 2: 0b->0c |
Gate 3: 0c->0d). GATE CHAIN REQUIREMENT satisfied. Proceed to Phase 1.]

---

## Phase 1 -- Technical Spec

Pull from `simulations/scout/` broadly. Note files from Step 0d used.

Write the spec. All six sections required -- no skipping, no merging.

### Overview
One paragraph: what {{topic}} does and why it exists.

### User Problem
Problem users face today. Reference dev and maker inertia costs from Step 0a
directly.

### Proposed Solution
What {{topic}} does. Incorporate scout-requirements or scout-feasibility signals
from Step 0d.

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

## Phase 2 -- Business Proposal

Pull from `simulations/scout/scout-feasibility/` before writing. Note files used.

**STEP 0A INERTIA ANCHOR**

Before writing any proposal option, copy the three Step 0a inertia costs here:

Exec inertia cost: [exact text from Step 0a -- do not paraphrase or generalize]
Dev inertia cost: [exact text from Step 0a -- do not paraphrase or generalize]
Maker inertia cost: [exact text from Step 0a -- do not paraphrase or generalize]

These are the inertia costs the proposal must address. The Defeating Do Nothing
block must cite the most decisive of these costs directly.

--- INERTIA ANCHOR GATE: Do not begin writing any proposal option until all three
inertia costs are present in the STEP 0A INERTIA ANCHOR block above. A proposal
option written before the anchor block is complete does not satisfy this gate. ---

Write the proposal. Three options minimum. Option 1 MUST be named **Do Nothing**.

For each option: description, pros, cons, risk, effort.

Then write the **Recommendation** section with the following labeled blocks.
Each block has its own header. Do not merge them into a combined paragraph.

### Recommendation

We recommend [chosen option].

**STEP 0B STABILITY ANCHOR**

Before writing the Defeating Do Nothing block, copy the Step 0b STABILITY
CITATION RECORD here:

STABILITY CITATION RECORD: [exact text from Step 0b -- character for character,
no paraphrase, no summary, no approximation]

This is the anchor text. The Defeating Do Nothing block must contain this record
verbatim. Do not begin writing the Defeating Do Nothing block until this anchor
is complete.

#### Defeating Do Nothing

[This block addresses the status quo competitor. Structurally separate from the
comparative defeat below.]

Do Nothing perpetuates [cite the most decisive Step 0a inertia cost -- name the
audience and the specific cost].

[PASTE THE STABILITY CITATION RECORD FROM THE STEP 0B STABILITY ANCHOR ABOVE
VERBATIM HERE. Do not summarize. Do not paraphrase. Copy the Form A or Form B
sentence character for character.]

We choose to act because [one sentence: why this cost trajectory is not
acceptable].

#### Defeating [Other Option Name]

We prefer [chosen] over [other] because [specific trade-off traceable to a risk,
effort, or cons field in the options analysis -- not a preference statement].

CITATION FORM REQUIREMENT: The Defeating Do Nothing block must contain the
STABILITY CITATION RECORD verbatim. A summary, paraphrase, condensed version, or
reference to the record does not satisfy this requirement. The exact Form A or
Form B sentence from Step 0b must appear character-for-character. A Defeating Do
Nothing block without the verbatim STABILITY CITATION RECORD does not satisfy
C-17 or C-21 regardless of how closely it approximates the record's meaning.

**>> PROPOSAL WRITE GATE <<**
Save proposal to: `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md`
Check: does the file exist? If not: write it now.
Do not begin Phase 3 until this file exists on disk.

---

## Phase 3 -- Executive Pitch

Pull from `simulations/scout/scout-positioning/` before writing. Note files used.

**STEP 0C CONTRACT ANCHOR**

Before writing any pitch version, copy the three Step 0c voice contracts here:

Step 0c exec voice contract: [exact text from Step 0c -- do not paraphrase or
generalize]
Step 0c dev voice contract: [exact text from Step 0c -- do not paraphrase or
generalize]
Step 0c maker voice contract: [exact text from Step 0c -- do not paraphrase or
generalize]

These are the anchor sentences. Each pitch version must open with a hook that
satisfies its named contract.

--- ANCHOR GATE: Complete the STEP 0C CONTRACT ANCHOR before writing any pitch
version. ---

Write all four sections of the pitch below. Do not save the pitch file until the
voice differentiation gate at the end of this phase passes.

### Exec Version
Lead with exec inertia cost from Step 0a. Use Step 0c exec voice contract as
anchor. Structure: [exec cost hook] -> [what changes] -> [outcome/ROI] ->
[call to action]. Do not open with a product description.

### Dev Version
Lead with dev inertia cost from Step 0a. Use Step 0c dev voice contract as
anchor. Structure: [friction hook] -> [what you can now do] ->
[capability unlocked] -> [call to action]. Do not open with an outcomes/ROI
frame.

### Maker Version
Lead with maker inertia cost from Step 0a. Use Step 0c maker voice contract as
anchor. Plain language, no jargon. Structure: [blocked step hook] ->
[what you can now do] -> [why it matters] -> [call to action].

### Anti-Positioning
3-5 "This is not..." statements. Structurally separate from the three audience
versions above.

**>> VOICE DIFFERENTIATION GATE -- Step 0c Contract Check (required before saving
pitch) <<**

The Step 0c voice contracts are the gate criteria. Use them now.

Step 1 -- Copy your Step 0c voice contracts:
  Step 0c exec voice contract: [your exec voice sentence from Step 0c]
  Step 0c dev voice contract: [your dev voice sentence from Step 0c]
  Step 0c maker voice contract: [your maker voice sentence from Step 0c]

Step 2 -- Extract the opening sentence from each pitch version:
  Exec opening: [first sentence of Exec Version]
  Dev opening: [first sentence of Dev Version]
  Maker opening: [first sentence of Maker Version]

Step 3 -- Per-audience gate (each audience gate must independently pass):

  Exec gate:
    Pass (Step 0c exec voice contract satisfied: opening names a business cost,
      risk, or revenue consequence) /
    Fail (opening does not satisfy Step 0c exec voice contract: opens with
      product description, capability framing, or workflow framing)

  Dev gate:
    Pass (Step 0c dev voice contract satisfied: opening names a tool friction,
      workaround, or capability gap) /
    Fail (opening does not satisfy Step 0c dev voice contract: opens with
      outcome/ROI framing or business consequence framing)

  Maker gate:
    Pass (Step 0c maker voice contract satisfied: opening names a blocked,
      absent, or manual step in plain language, no jargon) /
    Fail (opening does not satisfy Step 0c maker voice contract: opens with
      product description or technical jargon)

Step 4 -- Resolution:
  IF any gate is Fail: Rewrite the failing version. Return to the Step 0c voice
    contract for that audience as the named revision anchor. Re-run Steps 2-3.
    Do not save the pitch until all three Step 0c contract gates are Pass.
  IF all three gates are Pass: proceed to PITCH WRITE GATE.

**>> PITCH WRITE GATE <<**
[Save only after all three Step 0c contract gates in the voice differentiation
gate above are Pass.]
Save pitch to: `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`
Check: does the file exist? If not: write it now.
Do not emit the COMPLETION INDEX until this file exists on disk.

---

## COMPLETION INDEX

[Emitted after all write gates, voice differentiation gate, and recovery steps
are complete. Four named sections: Artifact Existence Record, Phase Gate Audit,
Citation Audit, Voice Compliance Audit.]

### Artifact Existence Record

| Artifact | Path | Status |
|----------|------|--------|
| Spec | `simulations/draft/specs/{{topic}}-spec-{{date}}.md` | [exists / missing] |
| Proposal | `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md` | [exists / missing] |
| Pitch | `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md` | [exists / missing] |

All three rows must show "exists" before the skill is complete.

### Phase Gate Audit

PHASE GATE AUDIT SOURCE BINDING: The gate chain verified in this audit was
executed in Phase 0 above. This audit does not redefine the gate requirements --
it verifies that the four steps (0a, 0b, 0c, 0d) and three gates (Gate 1:
0a->0b, Gate 2: 0b->0c, Gate 3: 0c->0d) completed in the Phase 0 execution
recorded above. The GATE CHAIN REQUIREMENT in Phase 0 is the authoritative
source for what constitutes a complete gate chain; any deviation from the
Phase 0 gate sequence constitutes a gate chain failure even if the audit entry
otherwise records passing gates. Do not redefine the gate chain in this audit --
verify conformance to the Phase 0 source.

- Scout files used per phase
- Phase 0 inertia costs confirmed (all three audiences)
- Phase 0 gate chain: 3 gates passed (Gate 1: 0a->0b | Gate 2: 0b->0c |
  Gate 3: 0c->0d)
- GATE CHAIN REQUIREMENT satisfied: all four steps and three gates completed
  before Phase 1 began

### Citation Audit

STEP 0B CITATION BINDING: The STABILITY CITATION RECORD verified below was
authored in Step 0b above. This audit entry does not redefine the record -- it
verifies conformance to the Step 0b source. The text pasted in the Defeating Do
Nothing block must match the exact STABILITY CITATION RECORD as written in
Step 0b. Do not accept a paraphrase, summary, or approximation as conforming.
The Step 0b source text is authoritative; any deviation from the Step 0b
phrasing constitutes a citation failure even if the pasted text is otherwise
complete and accurate.

- STABILITY CITATION RECORD form used: Form A / Form B
- STABILITY CITATION RECORD pasted verbatim in Defeating Do Nothing block:
  CITATION CONFIRMED / CITATION MISSING
  (If CITATION MISSING: return to Phase 2 and paste the record before stopping.)
- Defeating Do Nothing block: separate labeled header (#### or equivalent):
  yes / no

### Voice Compliance Audit

STEP 0C SOURCE BINDING: The three voice contracts verified in this table were
authored in Step 0c above. This audit table does not redefine the contracts -- it
verifies conformance to the Step 0c source. The text in the "Step 0c Contract
Verified" column must match the exact contract names as written in Step 0c. Do
not rephrase. Do not generalize. The Step 0c source text is authoritative; any
deviation from the Step 0c phrasing constitutes a verification failure even if
the cell value is otherwise complete.

COLUMN-HEADER REQUIREMENT: The third column header must read exactly "Step 0c
Contract Verified". A header reading "Contract Check", "Voice Contract",
"Verified", or any label other than "Step 0c Contract Verified" does not pass.

Record the verdict for each audience in the table below. Fill in the Step 0c
Contract Verified column with the exact Step 0c contract name followed by
"satisfied". A row without a named contract in the verification column does not
satisfy this section.

| Audience | Verdict | Step 0c Contract Verified |
|----------|---------|--------------------------|
| Exec | [Pass / Fail] | Step 0c exec voice contract satisfied |
| Dev | [Pass / Fail] | Step 0c dev voice contract satisfied |
| Maker | [Pass / Fail] | Step 0c maker voice contract satisfied |
```

**Rubric targeting**:
- C-46 through C-50: All preserved. STEP 0B FORWARD AUDIT NOTICE uses
  imperative mode: "Do not alter the record phrasing between here and Phase 2."
- STEP 0B FORWARD AUDIT NOTICE (new): Named notice in Step 0b, immediately
  after the STABILITY CITATION RECORD definition, before Gate 2. Explicitly
  names the Citation Audit as the downstream verifier of the record. Carries
  "do not alter" instruction forward to Phase 2. Structural parallel to
  FORWARD AUDIT NOTICE in Step 0c (names the Voice Compliance Audit as
  downstream verifier of voice contracts). Closes the forward-notice asymmetry:
  both data-producing steps (0b and 0c) now carry named forward audit notices.
- V16 watch: "Step 0b carries STEP 0B FORWARD AUDIT NOTICE naming the Citation
  Audit as the downstream verifier of the STABILITY CITATION RECORD -- parallel
  to the FORWARD AUDIT NOTICE in Step 0c naming the Voice Compliance Audit as
  the downstream verifier of the voice contracts."

---

## V-04 -- Combined: STABILITY ANCHOR GATE (V-01) + STEP 0A INERTIA BINDING (V-02)

**Hypothesis**: V-01 adds the gate position to the citation chain (STABILITY
ANCHOR GATE after STEP 0B STABILITY ANCHOR). V-02 adds the backward-bind
position to the inertia cost chain (STEP 0A INERTIA BINDING in Phase Gate Audit).
These address two different chains in two different sections of the prompt -- no
structural conflict is predicted. V-04 combines both without V-03 to test whether
the two patterns coexist independently. The citation chain becomes 4/4. The
inertia cost chain becomes 4/4. The forward-notice pattern remains asymmetric
(Step 0c has FORWARD AUDIT NOTICE; Step 0b does not). If V-04 scores differently
from V-05, the forward-notice asymmetry is the distinguishing criterion. Predicted:
42/42 + v16 watch on both STABILITY ANCHOR GATE and STEP 0A INERTIA BINDING.

```
Run the campaign-specify skill for: {{topic}}

Produce three artifacts: spec, proposal, pitch. Execute phases 0-3 in order.
Phase 0 must complete before Phase 1 begins. Each artifact is written to disk
before the next phase begins.

---

## Phase 0 -- Audience Foundation

Phase 0 has four steps. Steps 0a, 0b, 0c are sequential with explicit advancement
gates. Step 0d (scout pull) is terminal.

GATE CHAIN REQUIREMENT: Phase 0 requires all four steps and all three gates to
complete before Phase 1 begins. The required sequence is: Step 0a -> Gate 1 ->
Step 0b -> Gate 2 -> Step 0c -> Gate 3 -> Step 0d. Skipping a step, merging two
steps, or beginning Phase 1 before Step 0d completes does not satisfy this
requirement. A Phase 1 that begins before all three gates have passed and Step 0d
has run does not satisfy C-09.

Gate chain: Gate 1 (0a->0b) | Gate 2 (0b->0c) | Gate 3 (0c->0d) | Step 0d terminal.

**Step 0a -- Inertia Costs**

What each audience LOSES if {{topic}} does not ship. Concrete and specific:

Exec inertia cost: [Specific revenue exposure, competitive gap, or risk. Name a
consequence, not a category. Quantify if possible.]

Dev inertia cost: [Specific workaround or capability gap. Name the friction, not
the feeling. Estimate recurring cost if possible.]

Maker inertia cost: [Specific blocked workflow step. Name the step. What does the
maker do today instead?]

--- GATE 1 (0a->0b): Do not advance to Step 0b until all three inertia costs are
complete. ---

**Step 0b -- Stability Citation Record**

Evaluate whether the cost of Do Nothing is stable or worsening. Produce the
STABILITY CITATION RECORD using one of the two forms below. This record will be
pasted verbatim into the Phase 2 Defeating Do Nothing block.

FORM A (worsening): "Do Nothing is not stable: [specific mechanism and timeline --
e.g., 'competitor ships equivalent feature in Q2, making exec exposure acute by
June' or 'dev workaround accumulates 3 hours/sprint, compounding to
36h/quarter']."

FORM B (stable): "Do Nothing is stable: [rationale -- e.g., 'the workaround is
functional and the underlying need does not grow with volume']."

STABILITY CITATION RECORD:
[Paste the complete Form A or Form B sentence here]

A record containing only a tag ("worsening" / "stable") without a mechanism or
rationale fails this step. The record must be a complete sentence ready for
verbatim citation.

--- GATE 2 (0b->0c): Do not advance to Step 0c until the STABILITY CITATION
RECORD is complete. ---

**Step 0c -- Voice Contracts**

One sentence per audience, grounded in Steps 0a and 0b:

Exec voice: [Outcomes/risk framing -- reference exec inertia cost and stability
trajectory]
Dev voice: [Capability/friction framing -- reference dev inertia cost]
Maker voice: [Workflow framing -- plain language, reference maker inertia cost]

FORWARD AUDIT NOTICE: These three voice contracts are the compliance criteria for
the COMPLETION INDEX Voice Compliance Audit. Each contract will be verified by
its exact name in the "Step 0c Contract Verified" column of the audit table. Do
not alter the contract phrasing between here and the audit -- the column values
must match the names used in Step 0c.

--- GATE 3 (0c->0d): Do not advance to Step 0d until all three voice contracts
are written. ---

**Step 0d -- Scout Pull** [TERMINAL]

Glob `simulations/scout/**/*.md` for {{topic}}. For each file found:
- Path
- One sentence summary
- Artifact it serves: spec / proposal / pitch

If no scout files found: record "no scout signals -- proceeding without" and
continue.

[Phase 0 complete. Three gates passed (Gate 1: 0a->0b | Gate 2: 0b->0c |
Gate 3: 0c->0d). GATE CHAIN REQUIREMENT satisfied. Proceed to Phase 1.]

---

## Phase 1 -- Technical Spec

Pull from `simulations/scout/` broadly. Note files from Step 0d used.

Write the spec. All six sections required -- no skipping, no merging.

### Overview
One paragraph: what {{topic}} does and why it exists.

### User Problem
Problem users face today. Reference dev and maker inertia costs from Step 0a
directly.

### Proposed Solution
What {{topic}} does. Incorporate scout-requirements or scout-feasibility signals
from Step 0d.

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

## Phase 2 -- Business Proposal

Pull from `simulations/scout/scout-feasibility/` before writing. Note files used.

**STEP 0A INERTIA ANCHOR**

Before writing any proposal option, copy the three Step 0a inertia costs here:

Exec inertia cost: [exact text from Step 0a -- do not paraphrase or generalize]
Dev inertia cost: [exact text from Step 0a -- do not paraphrase or generalize]
Maker inertia cost: [exact text from Step 0a -- do not paraphrase or generalize]

These are the inertia costs the proposal must address. The Defeating Do Nothing
block must cite the most decisive of these costs directly.

--- INERTIA ANCHOR GATE: Do not begin writing any proposal option until all three
inertia costs are present in the STEP 0A INERTIA ANCHOR block above. A proposal
option written before the anchor block is complete does not satisfy this gate. ---

Write the proposal. Three options minimum. Option 1 MUST be named **Do Nothing**.

For each option: description, pros, cons, risk, effort.

Then write the **Recommendation** section with the following labeled blocks.
Each block has its own header. Do not merge them into a combined paragraph.

### Recommendation

We recommend [chosen option].

**STEP 0B STABILITY ANCHOR**

Before writing the Defeating Do Nothing block, copy the Step 0b STABILITY
CITATION RECORD here:

STABILITY CITATION RECORD: [exact text from Step 0b -- character for character,
no paraphrase, no summary, no approximation]

This is the anchor text. The Defeating Do Nothing block must contain this record
verbatim. Do not begin writing the Defeating Do Nothing block until this anchor
is complete.

--- STABILITY ANCHOR GATE: Do not begin writing the Defeating Do Nothing block
until the STEP 0B STABILITY ANCHOR above contains the complete STABILITY
CITATION RECORD. A Defeating Do Nothing block written before the anchor block is
complete does not satisfy this gate. ---

#### Defeating Do Nothing

[This block addresses the status quo competitor. Structurally separate from the
comparative defeat below.]

Do Nothing perpetuates [cite the most decisive Step 0a inertia cost -- name the
audience and the specific cost].

[PASTE THE STABILITY CITATION RECORD FROM THE STEP 0B STABILITY ANCHOR ABOVE
VERBATIM HERE. Do not summarize. Do not paraphrase. Copy the Form A or Form B
sentence character for character.]

We choose to act because [one sentence: why this cost trajectory is not
acceptable].

#### Defeating [Other Option Name]

We prefer [chosen] over [other] because [specific trade-off traceable to a risk,
effort, or cons field in the options analysis -- not a preference statement].

CITATION FORM REQUIREMENT: The Defeating Do Nothing block must contain the
STABILITY CITATION RECORD verbatim. A summary, paraphrase, condensed version, or
reference to the record does not satisfy this requirement. The exact Form A or
Form B sentence from Step 0b must appear character-for-character. A Defeating Do
Nothing block without the verbatim STABILITY CITATION RECORD does not satisfy
C-17 or C-21 regardless of how closely it approximates the record's meaning.

**>> PROPOSAL WRITE GATE <<**
Save proposal to: `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md`
Check: does the file exist? If not: write it now.
Do not begin Phase 3 until this file exists on disk.

---

## Phase 3 -- Executive Pitch

Pull from `simulations/scout/scout-positioning/` before writing. Note files used.

**STEP 0C CONTRACT ANCHOR**

Before writing any pitch version, copy the three Step 0c voice contracts here:

Step 0c exec voice contract: [exact text from Step 0c -- do not paraphrase or
generalize]
Step 0c dev voice contract: [exact text from Step 0c -- do not paraphrase or
generalize]
Step 0c maker voice contract: [exact text from Step 0c -- do not paraphrase or
generalize]

These are the anchor sentences. Each pitch version must open with a hook that
satisfies its named contract.

--- ANCHOR GATE: Complete the STEP 0C CONTRACT ANCHOR before writing any pitch
version. ---

Write all four sections of the pitch below. Do not save the pitch file until the
voice differentiation gate at the end of this phase passes.

### Exec Version
Lead with exec inertia cost from Step 0a. Use Step 0c exec voice contract as
anchor. Structure: [exec cost hook] -> [what changes] -> [outcome/ROI] ->
[call to action]. Do not open with a product description.

### Dev Version
Lead with dev inertia cost from Step 0a. Use Step 0c dev voice contract as
anchor. Structure: [friction hook] -> [what you can now do] ->
[capability unlocked] -> [call to action]. Do not open with an outcomes/ROI
frame.

### Maker Version
Lead with maker inertia cost from Step 0a. Use Step 0c maker voice contract as
anchor. Plain language, no jargon. Structure: [blocked step hook] ->
[what you can now do] -> [why it matters] -> [call to action].

### Anti-Positioning
3-5 "This is not..." statements. Structurally separate from the three audience
versions above.

**>> VOICE DIFFERENTIATION GATE -- Step 0c Contract Check (required before saving
pitch) <<**

The Step 0c voice contracts are the gate criteria. Use them now.

Step 1 -- Copy your Step 0c voice contracts:
  Step 0c exec voice contract: [your exec voice sentence from Step 0c]
  Step 0c dev voice contract: [your dev voice sentence from Step 0c]
  Step 0c maker voice contract: [your maker voice sentence from Step 0c]

Step 2 -- Extract the opening sentence from each pitch version:
  Exec opening: [first sentence of Exec Version]
  Dev opening: [first sentence of Dev Version]
  Maker opening: [first sentence of Maker Version]

Step 3 -- Per-audience gate (each audience gate must independently pass):

  Exec gate:
    Pass (Step 0c exec voice contract satisfied: opening names a business cost,
      risk, or revenue consequence) /
    Fail (opening does not satisfy Step 0c exec voice contract: opens with
      product description, capability framing, or workflow framing)

  Dev gate:
    Pass (Step 0c dev voice contract satisfied: opening names a tool friction,
      workaround, or capability gap) /
    Fail (opening does not satisfy Step 0c dev voice contract: opens with
      outcome/ROI framing or business consequence framing)

  Maker gate:
    Pass (Step 0c maker voice contract satisfied: opening names a blocked,
      absent, or manual step in plain language, no jargon) /
    Fail (opening does not satisfy Step 0c maker voice contract: opens with
      product description or technical jargon)

Step 4 -- Resolution:
  IF any gate is Fail: Rewrite the failing version. Return to the Step 0c voice
    contract for that audience as the named revision anchor. Re-run Steps 2-3.
    Do not save the pitch until all three Step 0c contract gates are Pass.
  IF all three gates are Pass: proceed to PITCH WRITE GATE.

**>> PITCH WRITE GATE <<**
[Save only after all three Step 0c contract gates in the voice differentiation
gate above are Pass.]
Save pitch to: `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`
Check: does the file exist? If not: write it now.
Do not emit the COMPLETION INDEX until this file exists on disk.

---

## COMPLETION INDEX

[Emitted after all write gates, voice differentiation gate, and recovery steps
are complete. Four named sections: Artifact Existence Record, Phase Gate Audit,
Citation Audit, Voice Compliance Audit.]

### Artifact Existence Record

| Artifact | Path | Status |
|----------|------|--------|
| Spec | `simulations/draft/specs/{{topic}}-spec-{{date}}.md` | [exists / missing] |
| Proposal | `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md` | [exists / missing] |
| Pitch | `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md` | [exists / missing] |

All three rows must show "exists" before the skill is complete.

### Phase Gate Audit

PHASE GATE AUDIT SOURCE BINDING: The gate chain verified in this audit was
executed in Phase 0 above. This audit does not redefine the gate requirements --
it verifies that the four steps (0a, 0b, 0c, 0d) and three gates (Gate 1:
0a->0b, Gate 2: 0b->0c, Gate 3: 0c->0d) completed in the Phase 0 execution
recorded above. The GATE CHAIN REQUIREMENT in Phase 0 is the authoritative
source for what constitutes a complete gate chain; any deviation from the
Phase 0 gate sequence constitutes a gate chain failure even if the audit entry
otherwise records passing gates. Do not redefine the gate chain in this audit --
verify conformance to the Phase 0 source.

STEP 0A INERTIA BINDING: The inertia costs confirmed below were authored in
Step 0a above. This audit does not redefine the inertia costs -- it verifies
that the costs recorded in Step 0a were propagated correctly through Phase 2.
The Step 0a inertia costs are the authoritative source; do not rephrase,
condense, or substitute them in this audit entry. Any deviation from the Step 0a
phrasing constitutes an inertia cost propagation failure even if the audit entry
is otherwise complete.

- Scout files used per phase
- Phase 0 inertia costs confirmed (all three audiences -- exec, dev, maker
  each present as authored in Step 0a)
- Phase 0 gate chain: 3 gates passed (Gate 1: 0a->0b | Gate 2: 0b->0c |
  Gate 3: 0c->0d)
- GATE CHAIN REQUIREMENT satisfied: all four steps and three gates completed
  before Phase 1 began

### Citation Audit

STEP 0B CITATION BINDING: The STABILITY CITATION RECORD verified below was
authored in Step 0b above. This audit entry does not redefine the record -- it
verifies conformance to the Step 0b source. The text pasted in the Defeating Do
Nothing block must match the exact STABILITY CITATION RECORD as written in
Step 0b. Do not accept a paraphrase, summary, or approximation as conforming.
The Step 0b source text is authoritative; any deviation from the Step 0b
phrasing constitutes a citation failure even if the pasted text is otherwise
complete and accurate.

- STABILITY CITATION RECORD form used: Form A / Form B
- STABILITY CITATION RECORD pasted verbatim in Defeating Do Nothing block:
  CITATION CONFIRMED / CITATION MISSING
  (If CITATION MISSING: return to Phase 2 and paste the record before stopping.)
- Defeating Do Nothing block: separate labeled header (#### or equivalent):
  yes / no

### Voice Compliance Audit

STEP 0C SOURCE BINDING: The three voice contracts verified in this table were
authored in Step 0c above. This audit table does not redefine the contracts -- it
verifies conformance to the Step 0c source. The text in the "Step 0c Contract
Verified" column must match the exact contract names as written in Step 0c. Do
not rephrase. Do not generalize. The Step 0c source text is authoritative; any
deviation from the Step 0c phrasing constitutes a verification failure even if
the cell value is otherwise complete.

COLUMN-HEADER REQUIREMENT: The third column header must read exactly "Step 0c
Contract Verified". A header reading "Contract Check", "Voice Contract",
"Verified", or any label other than "Step 0c Contract Verified" does not pass.

Record the verdict for each audience in the table below. Fill in the Step 0c
Contract Verified column with the exact Step 0c contract name followed by
"satisfied". A row without a named contract in the verification column does not
satisfy this section.

| Audience | Verdict | Step 0c Contract Verified |
|----------|---------|--------------------------|
| Exec | [Pass / Fail] | Step 0c exec voice contract satisfied |
| Dev | [Pass / Fail] | Step 0c dev voice contract satisfied |
| Maker | [Pass / Fail] | Step 0c maker voice contract satisfied |
```

**Rubric targeting**:
- C-46 through C-50: All preserved.
- STABILITY ANCHOR GATE (from V-01): Named gate after STEP 0B STABILITY
  ANCHOR. Citation chain: define -> anchor -> GATE -> requirement -> backward-bind.
- STEP 0A INERTIA BINDING (from V-02): Named source-binding in Phase Gate
  Audit. Inertia cost chain: define -> anchor -> gate -> BACKWARD-BIND.
- Combined watch: Two of the three new R15 patterns are simultaneously present.
  The forward-notice asymmetry (V-03) is absent -- Step 0b has no STEP 0B
  FORWARD AUDIT NOTICE. If V-04 scores lower than V-05, the distinguishing
  criterion is V-03's STEP 0B FORWARD AUDIT NOTICE. If V-04 scores the same
  as V-05, STEP 0B FORWARD AUDIT NOTICE is not a v16 criterion.

---

## V-05 -- Combined: STABILITY ANCHOR GATE (V-01) + STEP 0A INERTIA BINDING (V-02) + STEP 0B FORWARD AUDIT NOTICE (V-03)

**Hypothesis**: V-04 combines STABILITY ANCHOR GATE (citation chain gate) and
STEP 0A INERTIA BINDING (inertia cost backward-bind), completing both chains to
4/4 positions. V-05 adds the third axis: STEP 0B FORWARD AUDIT NOTICE in Step
0b. With this addition, the forward-notice pattern is symmetric: Step 0b and
Step 0c each carry a named forward audit notice pointing to their respective
downstream audit section. The hypothesis: completing the forward-notice pattern
symmetry across both data-producing Phase 0 steps -- in addition to the two
chain completions from V-04 -- creates the v16 ceiling. The citation chain (4/4),
inertia cost chain (4/4), and forward-notice pattern (2/2) are all complete.
The voice contract chain remains the only chain that has been complete since
R13. If V-05 uniquely achieves a ceiling V-04 does not, STEP 0B FORWARD AUDIT
NOTICE is a v16 criterion. If V-04 and V-05 are equal, the forward-notice
pattern is below the scoring threshold. Predicted: 42/42 + v16 watch on all
three new elements simultaneously.

```
Run the campaign-specify skill for: {{topic}}

Produce three artifacts: spec, proposal, pitch. Execute phases 0-3 in order.
Phase 0 must complete before Phase 1 begins. Each artifact is written to disk
before the next phase begins.

---

## Phase 0 -- Audience Foundation

Phase 0 has four steps. Steps 0a, 0b, 0c are sequential with explicit advancement
gates. Step 0d (scout pull) is terminal.

GATE CHAIN REQUIREMENT: Phase 0 requires all four steps and all three gates to
complete before Phase 1 begins. The required sequence is: Step 0a -> Gate 1 ->
Step 0b -> Gate 2 -> Step 0c -> Gate 3 -> Step 0d. Skipping a step, merging two
steps, or beginning Phase 1 before Step 0d completes does not satisfy this
requirement. A Phase 1 that begins before all three gates have passed and Step 0d
has run does not satisfy C-09.

Gate chain: Gate 1 (0a->0b) | Gate 2 (0b->0c) | Gate 3 (0c->0d) | Step 0d terminal.

**Step 0a -- Inertia Costs**

What each audience LOSES if {{topic}} does not ship. Concrete and specific:

Exec inertia cost: [Specific revenue exposure, competitive gap, or risk. Name a
consequence, not a category. Quantify if possible.]

Dev inertia cost: [Specific workaround or capability gap. Name the friction, not
the feeling. Estimate recurring cost if possible.]

Maker inertia cost: [Specific blocked workflow step. Name the step. What does the
maker do today instead?]

--- GATE 1 (0a->0b): Do not advance to Step 0b until all three inertia costs are
complete. ---

**Step 0b -- Stability Citation Record**

Evaluate whether the cost of Do Nothing is stable or worsening. Produce the
STABILITY CITATION RECORD using one of the two forms below. This record will be
pasted verbatim into the Phase 2 Defeating Do Nothing block.

FORM A (worsening): "Do Nothing is not stable: [specific mechanism and timeline --
e.g., 'competitor ships equivalent feature in Q2, making exec exposure acute by
June' or 'dev workaround accumulates 3 hours/sprint, compounding to
36h/quarter']."

FORM B (stable): "Do Nothing is stable: [rationale -- e.g., 'the workaround is
functional and the underlying need does not grow with volume']."

STABILITY CITATION RECORD:
[Paste the complete Form A or Form B sentence here]

A record containing only a tag ("worsening" / "stable") without a mechanism or
rationale fails this step. The record must be a complete sentence ready for
verbatim citation.

STEP 0B FORWARD AUDIT NOTICE: This STABILITY CITATION RECORD is the verbatim
citation source for the Defeating Do Nothing block in Phase 2. The Citation Audit
in the COMPLETION INDEX will verify that the Defeating Do Nothing block contains
this record verbatim. Do not alter the record phrasing between here and Phase 2 --
the Defeating Do Nothing block must match the Step 0b source exactly. A
Defeating Do Nothing block that paraphrases, summarizes, or approximates this
record does not pass the Citation Audit regardless of how closely it reproduces
the record's meaning.

--- GATE 2 (0b->0c): Do not advance to Step 0c until the STABILITY CITATION
RECORD is complete. ---

**Step 0c -- Voice Contracts**

One sentence per audience, grounded in Steps 0a and 0b:

Exec voice: [Outcomes/risk framing -- reference exec inertia cost and stability
trajectory]
Dev voice: [Capability/friction framing -- reference dev inertia cost]
Maker voice: [Workflow framing -- plain language, reference maker inertia cost]

FORWARD AUDIT NOTICE: These three voice contracts are the compliance criteria for
the COMPLETION INDEX Voice Compliance Audit. Each contract will be verified by
its exact name in the "Step 0c Contract Verified" column of the audit table. Do
not alter the contract phrasing between here and the audit -- the column values
must match the names used in Step 0c.

--- GATE 3 (0c->0d): Do not advance to Step 0d until all three voice contracts
are written. ---

**Step 0d -- Scout Pull** [TERMINAL]

Glob `simulations/scout/**/*.md` for {{topic}}. For each file found:
- Path
- One sentence summary
- Artifact it serves: spec / proposal / pitch

If no scout files found: record "no scout signals -- proceeding without" and
continue.

[Phase 0 complete. Three gates passed (Gate 1: 0a->0b | Gate 2: 0b->0c |
Gate 3: 0c->0d). GATE CHAIN REQUIREMENT satisfied. Proceed to Phase 1.]

---

## Phase 1 -- Technical Spec

Pull from `simulations/scout/` broadly. Note files from Step 0d used.

Write the spec. All six sections required -- no skipping, no merging.

### Overview
One paragraph: what {{topic}} does and why it exists.

### User Problem
Problem users face today. Reference dev and maker inertia costs from Step 0a
directly.

### Proposed Solution
What {{topic}} does. Incorporate scout-requirements or scout-feasibility signals
from Step 0d.

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

## Phase 2 -- Business Proposal

Pull from `simulations/scout/scout-feasibility/` before writing. Note files used.

**STEP 0A INERTIA ANCHOR**

Before writing any proposal option, copy the three Step 0a inertia costs here:

Exec inertia cost: [exact text from Step 0a -- do not paraphrase or generalize]
Dev inertia cost: [exact text from Step 0a -- do not paraphrase or generalize]
Maker inertia cost: [exact text from Step 0a -- do not paraphrase or generalize]

These are the inertia costs the proposal must address. The Defeating Do Nothing
block must cite the most decisive of these costs directly.

--- INERTIA ANCHOR GATE: Do not begin writing any proposal option until all three
inertia costs are present in the STEP 0A INERTIA ANCHOR block above. A proposal
option written before the anchor block is complete does not satisfy this gate. ---

Write the proposal. Three options minimum. Option 1 MUST be named **Do Nothing**.

For each option: description, pros, cons, risk, effort.

Then write the **Recommendation** section with the following labeled blocks.
Each block has its own header. Do not merge them into a combined paragraph.

### Recommendation

We recommend [chosen option].

**STEP 0B STABILITY ANCHOR**

Before writing the Defeating Do Nothing block, copy the Step 0b STABILITY
CITATION RECORD here:

STABILITY CITATION RECORD: [exact text from Step 0b -- character for character,
no paraphrase, no summary, no approximation]

This is the anchor text. The Defeating Do Nothing block must contain this record
verbatim. Do not begin writing the Defeating Do Nothing block until this anchor
is complete.

--- STABILITY ANCHOR GATE: Do not begin writing the Defeating Do Nothing block
until the STEP 0B STABILITY ANCHOR above contains the complete STABILITY
CITATION RECORD. A Defeating Do Nothing block written before the anchor block is
complete does not satisfy this gate. ---

#### Defeating Do Nothing

[This block addresses the status quo competitor. Structurally separate from the
comparative defeat below.]

Do Nothing perpetuates [cite the most decisive Step 0a inertia cost -- name the
audience and the specific cost].

[PASTE THE STABILITY CITATION RECORD FROM THE STEP 0B STABILITY ANCHOR ABOVE
VERBATIM HERE. Do not summarize. Do not paraphrase. Copy the Form A or Form B
sentence character for character.]

We choose to act because [one sentence: why this cost trajectory is not
acceptable].

#### Defeating [Other Option Name]

We prefer [chosen] over [other] because [specific trade-off traceable to a risk,
effort, or cons field in the options analysis -- not a preference statement].

CITATION FORM REQUIREMENT: The Defeating Do Nothing block must contain the
STABILITY CITATION RECORD verbatim. A summary, paraphrase, condensed version, or
reference to the record does not satisfy this requirement. The exact Form A or
Form B sentence from Step 0b must appear character-for-character. A Defeating Do
Nothing block without the verbatim STABILITY CITATION RECORD does not satisfy
C-17 or C-21 regardless of how closely it approximates the record's meaning.

**>> PROPOSAL WRITE GATE <<**
Save proposal to: `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md`
Check: does the file exist? If not: write it now.
Do not begin Phase 3 until this file exists on disk.

---

## Phase 3 -- Executive Pitch

Pull from `simulations/scout/scout-positioning/` before writing. Note files used.

**STEP 0C CONTRACT ANCHOR**

Before writing any pitch version, copy the three Step 0c voice contracts here:

Step 0c exec voice contract: [exact text from Step 0c -- do not paraphrase or
generalize]
Step 0c dev voice contract: [exact text from Step 0c -- do not paraphrase or
generalize]
Step 0c maker voice contract: [exact text from Step 0c -- do not paraphrase or
generalize]

These are the anchor sentences. Each pitch version must open with a hook that
satisfies its named contract.

--- ANCHOR GATE: Complete the STEP 0C CONTRACT ANCHOR before writing any pitch
version. ---

Write all four sections of the pitch below. Do not save the pitch file until the
voice differentiation gate at the end of this phase passes.

### Exec Version
Lead with exec inertia cost from Step 0a. Use Step 0c exec voice contract as
anchor. Structure: [exec cost hook] -> [what changes] -> [outcome/ROI] ->
[call to action]. Do not open with a product description.

### Dev Version
Lead with dev inertia cost from Step 0a. Use Step 0c dev voice contract as
anchor. Structure: [friction hook] -> [what you can now do] ->
[capability unlocked] -> [call to action]. Do not open with an outcomes/ROI
frame.

### Maker Version
Lead with maker inertia cost from Step 0a. Use Step 0c maker voice contract as
anchor. Plain language, no jargon. Structure: [blocked step hook] ->
[what you can now do] -> [why it matters] -> [call to action].

### Anti-Positioning
3-5 "This is not..." statements. Structurally separate from the three audience
versions above.

**>> VOICE DIFFERENTIATION GATE -- Step 0c Contract Check (required before saving
pitch) <<**

The Step 0c voice contracts are the gate criteria. Use them now.

Step 1 -- Copy your Step 0c voice contracts:
  Step 0c exec voice contract: [your exec voice sentence from Step 0c]
  Step 0c dev voice contract: [your dev voice sentence from Step 0c]
  Step 0c maker voice contract: [your maker voice sentence from Step 0c]

Step 2 -- Extract the opening sentence from each pitch version:
  Exec opening: [first sentence of Exec Version]
  Dev opening: [first sentence of Dev Version]
  Maker opening: [first sentence of Maker Version]

Step 3 -- Per-audience gate (each audience gate must independently pass):

  Exec gate:
    Pass (Step 0c exec voice contract satisfied: opening names a business cost,
      risk, or revenue consequence) /
    Fail (opening does not satisfy Step 0c exec voice contract: opens with
      product description, capability framing, or workflow framing)

  Dev gate:
    Pass (Step 0c dev voice contract satisfied: opening names a tool friction,
      workaround, or capability gap) /
    Fail (opening does not satisfy Step 0c dev voice contract: opens with
      outcome/ROI framing or business consequence framing)

  Maker gate:
    Pass (Step 0c maker voice contract satisfied: opening names a blocked,
      absent, or manual step in plain language, no jargon) /
    Fail (opening does not satisfy Step 0c maker voice contract: opens with
      product description or technical jargon)

Step 4 -- Resolution:
  IF any gate is Fail: Rewrite the failing version. Return to the Step 0c voice
    contract for that audience as the named revision anchor. Re-run Steps 2-3.
    Do not save the pitch until all three Step 0c contract gates are Pass.
  IF all three gates are Pass: proceed to PITCH WRITE GATE.

**>> PITCH WRITE GATE <<**
[Save only after all three Step 0c contract gates in the voice differentiation
gate above are Pass.]
Save pitch to: `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md`
Check: does the file exist? If not: write it now.
Do not emit the COMPLETION INDEX until this file exists on disk.

---

## COMPLETION INDEX

[Emitted after all write gates, voice differentiation gate, and recovery steps
are complete. Four named sections: Artifact Existence Record, Phase Gate Audit,
Citation Audit, Voice Compliance Audit.]

### Artifact Existence Record

| Artifact | Path | Status |
|----------|------|--------|
| Spec | `simulations/draft/specs/{{topic}}-spec-{{date}}.md` | [exists / missing] |
| Proposal | `simulations/draft/proposals/{{topic}}-proposal-{{date}}.md` | [exists / missing] |
| Pitch | `simulations/draft/pitches/{{topic}}-pitch-{{date}}.md` | [exists / missing] |

All three rows must show "exists" before the skill is complete.

### Phase Gate Audit

PHASE GATE AUDIT SOURCE BINDING: The gate chain verified in this audit was
executed in Phase 0 above. This audit does not redefine the gate requirements --
it verifies that the four steps (0a, 0b, 0c, 0d) and three gates (Gate 1:
0a->0b, Gate 2: 0b->0c, Gate 3: 0c->0d) completed in the Phase 0 execution
recorded above. The GATE CHAIN REQUIREMENT in Phase 0 is the authoritative
source for what constitutes a complete gate chain; any deviation from the
Phase 0 gate sequence constitutes a gate chain failure even if the audit entry
otherwise records passing gates. Do not redefine the gate chain in this audit --
verify conformance to the Phase 0 source.

STEP 0A INERTIA BINDING: The inertia costs confirmed below were authored in
Step 0a above. This audit does not redefine the inertia costs -- it verifies
that the costs recorded in Step 0a were propagated correctly through Phase 2.
The Step 0a inertia costs are the authoritative source; do not rephrase,
condense, or substitute them in this audit entry. Any deviation from the Step 0a
phrasing constitutes an inertia cost propagation failure even if the audit entry
is otherwise complete.

- Scout files used per phase
- Phase 0 inertia costs confirmed (all three audiences -- exec, dev, maker
  each present as authored in Step 0a)
- Phase 0 gate chain: 3 gates passed (Gate 1: 0a->0b | Gate 2: 0b->0c |
  Gate 3: 0c->0d)
- GATE CHAIN REQUIREMENT satisfied: all four steps and three gates completed
  before Phase 1 began

### Citation Audit

STEP 0B CITATION BINDING: The STABILITY CITATION RECORD verified below was
authored in Step 0b above. This audit entry does not redefine the record -- it
verifies conformance to the Step 0b source. The text pasted in the Defeating Do
Nothing block must match the exact STABILITY CITATION RECORD as written in
Step 0b. Do not accept a paraphrase, summary, or approximation as conforming.
The Step 0b source text is authoritative; any deviation from the Step 0b
phrasing constitutes a citation failure even if the pasted text is otherwise
complete and accurate.

- STABILITY CITATION RECORD form used: Form A / Form B
- STABILITY CITATION RECORD pasted verbatim in Defeating Do Nothing block:
  CITATION CONFIRMED / CITATION MISSING
  (If CITATION MISSING: return to Phase 2 and paste the record before stopping.)
- Defeating Do Nothing block: separate labeled header (#### or equivalent):
  yes / no

### Voice Compliance Audit

STEP 0C SOURCE BINDING: The three voice contracts verified in this table were
authored in Step 0c above. This audit table does not redefine the contracts -- it
verifies conformance to the Step 0c source. The text in the "Step 0c Contract
Verified" column must match the exact contract names as written in Step 0c. Do
not rephrase. Do not generalize. The Step 0c source text is authoritative; any
deviation from the Step 0c phrasing constitutes a verification failure even if
the cell value is otherwise complete.

COLUMN-HEADER REQUIREMENT: The third column header must read exactly "Step 0c
Contract Verified". A header reading "Contract Check", "Voice Contract",
"Verified", or any label other than "Step 0c Contract Verified" does not pass.

Record the verdict for each audience in the table below. Fill in the Step 0c
Contract Verified column with the exact Step 0c contract name followed by
"satisfied". A row without a named contract in the verification column does not
satisfy this section.

| Audience | Verdict | Step 0c Contract Verified |
|----------|---------|--------------------------|
| Exec | [Pass / Fail] | Step 0c exec voice contract satisfied |
| Dev | [Pass / Fail] | Step 0c dev voice contract satisfied |
| Maker | [Pass / Fail] | Step 0c maker voice contract satisfied |
```

**Rubric targeting**:
- C-46 (IMPERATIVE REGISTER): Preserved. All three new blocks use imperative
  mode throughout: "Do not begin writing the Defeating Do Nothing block until..."
  (STABILITY ANCHOR GATE); "do not rephrase, condense, or substitute them..."
  (STEP 0A INERTIA BINDING); "Do not alter the record phrasing between here and
  Phase 2..." (STEP 0B FORWARD AUDIT NOTICE).
- C-47 (GATE CHAIN REQUIREMENT): Preserved unchanged from R13 V-05.
- C-48 (INERTIA ANCHOR GATE): Preserved from R14 V-01/V-05.
- C-49 (STEP 0B STABILITY ANCHOR): Preserved from R14 V-02/V-05.
- C-50 (PHASE GATE AUDIT SOURCE BINDING): Preserved from R14 V-03/V-05.
- STABILITY ANCHOR GATE (from V-01): Gate after STEP 0B STABILITY ANCHOR.
  Citation chain 4/4: define -> anchor -> GATE -> requirement -> backward-bind.
- STEP 0A INERTIA BINDING (from V-02): Source-binding in Phase Gate Audit.
  Inertia cost chain 4/4: define -> anchor -> gate -> BACKWARD-BIND.
- STEP 0B FORWARD AUDIT NOTICE (from V-03): Forward audit notice in Step 0b.
  Forward-notice pattern 2/2: Step 0b (-> Citation Audit) + Step 0c (-> VCA).
- Combined watch: The three new R15 patterns complete the following structural
  positions simultaneously -- citation chain gate, inertia cost backward-bind,
  and forward-notice symmetry. V-05 is the first variation to carry all three.
  V-01 through V-04 each carry one or two. If any single one is a v16 criterion,
  V-05 carries it. If the three together constitute a criterion (parallel to
  the named-requirement triple or the named-source-binding triple from prior
  rounds), V-05 is the first ceiling candidate under v16.
- R15 vs R14 asymmetry: R14 V-05 completed the source-binding triple (STEP 0C
  SOURCE BINDING / STEP 0B CITATION BINDING / PHASE GATE AUDIT SOURCE BINDING).
  R15 V-05 probes a second gate triple (ANCHOR GATE / INERTIA ANCHOR GATE /
  STABILITY ANCHOR GATE), one gate per anchor per chain. The gate triple was
  incomplete in all R14 variations: STABILITY ANCHOR GATE was absent from R14
  V-01 through V-05. If the gate triple pattern is itself a criterion, V-05 is
  the first to carry all three gates simultaneously.
