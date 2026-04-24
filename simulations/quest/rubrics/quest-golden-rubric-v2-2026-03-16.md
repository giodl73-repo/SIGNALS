Written. Here is the complete updated rubric:

---

## quest-golden Scoring Rubric — v2

**13 criteria across 3 tiers.** 3 new aspirationals added from Round 1 excellence signals.

---

### What changed from v1

**Three new aspirational criteria extracted from Round 1 scorecard patterns:**

**C-11 — Structural termination isolation** *(category: structure)*

The convergence/termination check must be a named, structurally separate element — a dedicated role, phase, or section — whose mandate is exclusively dual-gate evaluation. Round 1 signal: V-01 (CONVERGENCE JUDGE role) and V-03 (PHASE 4 exit gate) earned PASS on C-01; V-02 and V-04 earned PARTIAL. The difference was entirely whether termination was isolated or inlined into the iteration body.

**C-12 — Contrast-enforced signal isolation** *(category: depth)*

The QU2 extraction step must include a structural contrast mechanism — a contrast column, a before/after field pair, or a delta block — that forces the extractor to state a gap rather than list properties. Round 1 signal: V-02 was the only variation to earn PASS on C-07, exclusively because its contrast column structurally prevented filling the cell with top-variation description. All other variations earned PARTIAL on C-07 for precisely this reason.

**C-13 — Rationale-grounded sequencing** *(category: behavior)*

The QU2→QU3 ordering must include an explanatory clause ("because...") so the model can reason toward compliance rather than follow a bare rule. Round 1 signal: V-04 earned PASS on C-04 by grounding the ordering in purpose; V-02 — which enforced it via table layout — earned PARTIAL because the table mapped rounds but did not order QU2/QU3 within a round, leaving no rationale to invoke.

---

### Formula update

Aspirational denominator changes from 2 → 5 as the tier grows:

```
Score = (essential_pass / 5)   * 60
      + (recommended_pass / 3) * 30
      + (aspirational_pass / 5) * 10
```

Golden threshold unchanged: all 5 essentials pass AND composite >= 80.
at dual convergence).
  OBSERVABLE: complete prompt body written out in full, not summarized; labeled as the golden
  prompt; written to a named file at simulations/quest/golden/{skill}-golden-{date}.md.
  STANDARD: full verbatim body present; reference-only ("see V-03") or summary-only = FAIL.

---

**C-03 -- Final rubric written as standalone artifact**

Without writing the final rubric, the theory of excellence is lost after the session ends,
because only the example remains and the next maintainer cannot know what each criterion
discovered or why it was added. Not "listing criteria inline," but "emitting the accumulated
rubric as a separate versioned file with all converged criteria, composite formula, denominator,
and golden threshold."

- **Weight:** essential
- **Category:** correctness
- **Pass:**
  LOCATION: final artifacts section (only at dual convergence).
  OBSERVABLE: rubric document written to simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md
  containing all criteria, composite formula, denominator, and golden threshold.
  STANDARD: standalone artifact present; embedding criteria only inside the golden file = FAIL.

---

**C-04 -- Excellence signal extraction (QU2) precedes criterion proposal (QU3)**

Without QU2 preceding QU3, proposed criteria are not grounded in observed output differences,
because a criterion that does not trace back to a measured output gap is an editorial guess,
not a discovered signal. Not "proposing criteria based on domain knowledge," but "extracting
the pattern from the observed gap between top and next-highest variation before writing any
criterion text."

- **Weight:** essential
- **Category:** behavior
- **Pass:**
  LOCATION: each round where a criterion is proposed.
  OBSERVABLE: QU2 extraction section naming (a) which variation pair showed the gap and
  (b) the observable output difference, appearing before QU3 criterion text in that round.
  STANDARD: QU2 populated before QU3 in every round with a criterion proposal; QU3 without
  preceding QU2 = FAIL for that round.

---

**C-05 -- Rubric present at loop start (loaded or created)**

Without a rubric as the scoring objective function before the first score step, variation
rankings have no grounded standard and excellence signals cannot be derived from criterion
gaps. Not "scoring by qualitative judgment," but "loading an existing rubric for the target
skill or creating one via quest:rubric before the first variation is scored."

- **Weight:** essential
- **Category:** correctness
- **Pass:**
  LOCATION: loop initialization.
  OBSERVABLE: rubric artifact reference (loaded filename or creation confirmation) present
  before first score step.
  STANDARD: rubric present at loop start; scoring without a rubric reference = FAIL.

---

## Recommended Criteria (weight 0.5 -- output is better with these)

**C-06 -- Per-round iteration record**

Without a per-round iteration record, convergence cannot be audited, because the reader
cannot verify that dual convergence conditions were actually met or trace which excellence
signals produced which rubric additions. Not "summarizing results at the end," but "recording
each round's variation IDs, scores, named excellence signal (or explicit 'no new signal'),
and rubric delta (criterion added or none) as a navigable history."

- **Weight:** recommended
- **Category:** coverage
- **Pass:**
  LOCATION: iteration history section or per-round log.
  OBSERVABLE: entry per round with (a) variation IDs scored, (b) top composite score,
  (c) excellence signal name or "none," (d) criterion added or "none."
  STANDARD: >= 1 entry per round executed; missing any of the four fields = suboptimal.

---

**C-07 -- Excellence signal isolation (not just top-variation properties)**

Without excellence signal isolation, the extracted pattern names what the best variation
contains rather than what made it better than its nearest competitor, because shared
properties of all high-scoring variations are not signals of excellence. Not "listing
properties of the top variation," but "differentiating the top variation's winning property
from properties shared by all variations at the same score level."

- **Weight:** recommended
- **Category:** depth
- **Pass:**
  LOCATION: QU2 extraction for each round with a proposed criterion.
  OBSERVABLE: contrast statement naming what the top variation had that the next-highest
  variation lacked (e.g., "V-03 had X; V-01 and V-02 did not").
  STANDARD: isolation contrast present; listing top-variation properties without a contrast
  against the next-highest = FAIL.

---

**C-08 -- Criterion proposal includes tier and pass condition**

Without tier assignment and a pass condition in criterion proposals, the proposed criterion
is incomplete and cannot be integrated into the rubric without editorial judgment, because
tier determines score weight and the pass condition determines whether the criterion is
evaluable. Not "proposing criterion text alone," but "proposing criterion text with tier
(essential/recommended/aspirational) and a slot-filled pass condition."

- **Weight:** recommended
- **Category:** format
- **Pass:**
  LOCATION: QU3 criterion proposal.
  OBSERVABLE: three fields present -- text, tier, pass condition -- in each criterion proposal.
  STANDARD: all three present; missing any one = suboptimal.

---

## Aspirational Criteria (weight 0.25 -- raise the bar once essential/recommended are stable)

**C-09 -- "What made it golden" mechanism narrative**

Without a mechanism narrative accompanying the golden prompt, the golden prompt is an example
without a theory, because the structural discoveries made during the loop are not explained
and the next maintainer cannot know which decisions were load-bearing. Not "emitting the
converged prompt body alone," but "accompanying it with a named section explaining each
structural mechanism discovered, which round found it, and what output gap it closed."

- **Weight:** aspirational
- **Category:** depth
- **Pass:**
  LOCATION: golden prompt output, adjacent to the prompt body.
  OBSERVABLE: named section (e.g., "What Made It Golden") with >= 2 mechanism descriptions;
  each citing (a) the round it was discovered and (b) the output gap it closed.
  STANDARD: mechanism descriptions with round citations present; generic praise without
  round citation = FAIL.

---

**C-10 -- Persistent gap identification (ablated criteria)**

Without persistent gap identification, the rubric presents a false ceiling, because criteria
that were proposed but never activated across all rounds represent open hypotheses -- not
settled knowledge -- and the next round's designer needs to know they exist. Not "emitting
only active criteria," but "naming criteria with zero activations across all rounds as ablated,
with a suggested targeted probe approach."

- **Weight:** aspirational
- **Category:** coverage
- **Pass:**
  LOCATION: final rubric or convergence output.
  OBSERVABLE: named section or annotation for criteria with zero activations across all rounds;
  each ablated criterion named with a suggested probe; OR explicit "no ablated criteria"
  statement if none exist.
  STANDARD: present if any criteria were ablated; omission without a "none" declaration = FAIL.

---

**C-11 -- Structural termination isolation**

Without a structurally isolated termination element, the convergence check can be absorbed
into the iteration body and weakened by the same register or style that governs the loop,
because a convergence check embedded in a conversational or tabular iteration step carries no
hard-exit force. Round 1 showed that V-01 (CONVERGENCE JUDGE role) and V-03 (PHASE 4 exit
gate) earned PASS on C-01 while V-02 and V-04 earned PARTIAL -- the difference traced
entirely to whether termination was a named, separate element or inlined. Not "mentioning
termination conditions somewhere," but "naming a distinct structural element -- a role, a
phase, or a section -- whose only mandate is dual-gate evaluation and whose execution cannot
be skipped by completing prior steps."

- **Weight:** aspirational
- **Category:** structure
- **Pass:**
  LOCATION: loop design or termination section.
  OBSERVABLE: a named element (role name, phase heading, or section title) that is distinct
  from all per-round iteration elements and whose described mandate is exclusively the
  dual convergence check.
  STANDARD: named distinct element present; termination conditions stated only inside an
  iteration role or iteration phase = FAIL.

---

**C-12 -- Contrast-enforced signal isolation**

Without a structural contrast mechanism, the excellence extraction step collapses into a
description of the top variation, because prose or table cells that ask for "excellence
patterns" fill with properties rather than gaps. Round 1 showed that V-02 earned PASS on
C-07 -- the only variation to do so -- exclusively because its contrast column structurally
forced "what the top variation had that the next-highest lacked," not just "what the top
variation contained." No other variation provided a structural enforcement mechanism; all
others earned PARTIAL on C-07. Not "asking for what distinguished the winner," but "designing
a structural field -- a contrast column, a before/after pair, or a delta notation block --
that cannot be filled by description alone."

- **Weight:** aspirational
- **Category:** depth
- **Pass:**
  LOCATION: QU2 excellence extraction step.
  OBSERVABLE: an explicit structural mechanism (e.g., a named column labeled "contrast" or
  "delta," a paired field "top variation had / next-highest lacked," or an explicit delta
  notation block) that requires the extractor to state a gap, not a property.
  STANDARD: named contrast mechanism present in the extraction step design; prompting for
  "excellence" or "what stood out" without a structural gap-forcing mechanism = FAIL.

---

**C-13 -- Rationale-grounded sequencing**

Without an explanatory rationale for the QU2-before-QU3 ordering, the sequence is a rule
that the model may follow mechanically but cannot reason from, because a stated ordering
without a stated reason produces no self-correction when the sequence is tempted or ambiguous.
Round 1 showed that V-04 earned PASS on C-04 by grounding the ordering in purpose ("QU2 must
precede QU3 because..."), while V-02 -- which imposed the sequence structurally via table
layout -- earned PARTIAL because the table mapped rounds but did not order QU2/QU3 within a
round, and the model had no rationale to invoke. Not "stating that QU2 precedes QU3," but
"stating why QU2 must precede QU3 in terms the model can invoke when deciding whether to skip
or reorder."

- **Weight:** aspirational
- **Category:** behavior
- **Pass:**
  LOCATION: QU2/QU3 description in the loop design.
  OBSERVABLE: an explanatory clause accompanying the ordering constraint -- e.g., "QU2 must
  precede QU3 because criteria not grounded in observed gaps are editorial guesses, not
  discovered signals" or equivalent reasoning that makes non-compliance self-evidently wrong.
  STANDARD: explanatory rationale present; ordering stated as a bare sequence rule without
  a "because" clause or equivalent grounding = FAIL.

---

## Scoring

**Composite formula:**

```
Score = (essential_pass / 5)   * 60
      + (recommended_pass / 3) * 30
      + (aspirational_pass / 5) * 10
```

**Tier table:**

| Tier         | Weight | Count  | Max contribution |
|--------------|--------|--------|-----------------|
| Essential    | 1.0    | 5      | 60              |
| Recommended  | 0.5    | 3      | 30              |
| Aspirational | 0.25   | 5      | 10              |
| **Total**    |        | **13** | **100**         |

**Golden threshold:** All 5 essential criteria pass AND composite >= 80

**PARTIAL:** Score = 70-79.
Earn conditions: all 5 essential pass + exactly 1 of 3 recommended pass (composite = 70).
A partial output has the loop structure correct but missing iteration record, signal
isolation, or criterion completeness. Partial is not golden.

**FAIL:** Any essential criterion fails (composite irrelevant).

---

## Version History

| Version | Date       | Criteria   | Change                                                                                                           |
|---------|------------|------------|------------------------------------------------------------------------------------------------------------------|
| v1      | 2026-03-16 | C-01..C-10 | Initial rubric from /quest:rubric                                                                                |
| v2      | 2026-03-16 | C-11..C-13 | R1 excellence patterns: termination isolation, contrast-enforced signal isolation, rationale-grounded sequencing |
