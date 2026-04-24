## quest-golden Scoring Rubric — v3

**14 criteria across 3 tiers.** 1 new aspirational added from Round 2 excellence signals.

---

### What changed from v2

**One new aspirational criterion extracted from Round 2 scorecard patterns:**

**C-14 — Inertia-anchored delta field** *(category: depth)*

The QU2 delta block must include a dedicated `INERTIA LACKED` slot that separately states what the inertia baseline lacked, distinct from the runner-up contrast. This prevents crediting inertia-present patterns as loop discoveries — if the inertia prompt already produces the structural mechanism, the loop did not discover it; the delta block must prove otherwise.

Round 2 signal: V-05 was the only variation to earn a perfect composite (100). It added `TOP HAD / INERTIA LACKED` as a structural field alongside `TOP HAD / SECOND LACKED`. V-02, which earned 98 and passed C-12, had a contrast delta block but no inertia anchor — its delta block could be satisfied even when the winning pattern was already present in unconstrained generation. The inertia slot closes that loophole by requiring the extractor to independently verify absence in the baseline.

---

### Formula update

Aspirational denominator changes from 5 → 6 as the tier grows:

```
Score = (essential_pass / 5)   * 60
      + (recommended_pass / 3) * 30
      + (aspirational_pass / 6) * 10
```

Golden threshold unchanged: all 5 essentials pass AND composite >= 80.

---

### Tier overview

| Tier | Criteria | Weight |
|------|----------|--------|
| Essential | C-01 through C-05 | 60 pts total |
| Recommended | C-06 through C-08 | 30 pts total |
| Aspirational | C-09 through C-14 | 10 pts total |

---

## Essential Criteria

---

**C-01 — Dual convergence termination**

Without a two-condition exit gate, the loop terminates too early, because trial convergence (top score stable across one round) is not the same as quest convergence (new excellence signals exhausted), and exiting on either alone abandons discovery prematurely. Not "stopping when the score is high," but "maintaining a named, structurally separate termination check that evaluates both gates independently and requires both to be true before exiting."

- **Weight:** essential
- **Category:** structure
- **Pass:**
  LOCATION: termination check (only at end of each iteration or as a dedicated phase/role).
  OBSERVABLE: two named conditions — trial convergence AND quest convergence — each evaluated independently; explicit continuation clause ("if either NO: continue") and exit clause ("if both YES: proceed to golden output").
  STANDARD: both gates named with distinct criteria; single-gate termination = FAIL.

---

**C-02 — Golden prompt written as full skill body**

Without writing the full verbatim prompt body, the golden output is not deployable, because a summary or label leaves the reader unable to run the skill without reconstructing it, which reintroduces interpretation error. Not "describing the golden prompt" or "referencing the winning variation," but "emitting the complete deployable text of the skill — every line — as a standalone file."

- **Weight:** essential
- **Category:** correctness
- **Pass:**
  LOCATION: final artifacts section (only at dual convergence).
  OBSERVABLE: complete prompt body written out in full, not summarized; labeled as the golden prompt; written to a named file at `simulations/quest/golden/{skill}-golden-{date}.md`.
  STANDARD: full verbatim body present; reference-only ("see V-03") or summary-only = FAIL.

---

**C-03 — Final rubric written as standalone artifact**

Without writing the final rubric, the theory of excellence is lost after the session ends, because only the example remains and the next maintainer cannot know what each criterion discovered or why it was added. Not "listing criteria inline," but "emitting the accumulated rubric as a separate versioned file with all converged criteria, composite formula, denominator, and golden threshold."

- **Weight:** essential
- **Category:** correctness
- **Pass:**
  LOCATION: final artifacts section (only at dual convergence).
  OBSERVABLE: rubric document written to `simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md` containing all criteria, composite formula, denominator, and golden threshold.
  STANDARD: standalone artifact present; embedding criteria only inside the golden file = FAIL.

---

**C-04 — Excellence signal extraction (QU2) precedes criterion proposal (QU3)**

Without QU2 preceding QU3, proposed criteria are not grounded in observed output differences, because a criterion that does not trace back to a measured output gap is an editorial guess, not a discovered signal. Not "proposing criteria based on domain knowledge," but "extracting the pattern from the observed gap between top and next-highest variation before writing any criterion text."

- **Weight:** essential
- **Category:** behavior
- **Pass:**
  LOCATION: each round where a criterion is proposed.
  OBSERVABLE: QU2 extraction section naming (a) which variation pair showed the gap and (b) the observable output difference, appearing before QU3 criterion text in that round; QU3 conditional on QU2 signal not none.
  STANDARD: QU2 populated before QU3 in every round with a criterion proposal; QU3 without preceding QU2 = FAIL for that round.

---

**C-05 — Rubric present at loop start**

Without a rubric at loop start, variation scoring has no grounded objective function, because rankings without defined criteria reflect the scorer's priors rather than measurable output properties, making scores incomparable across rounds. Not "recalling criteria from context," but "loading the current rubric file before scoring any variation in each round."

- **Weight:** essential
- **Category:** behavior
- **Pass:**
  LOCATION: loop initialization (before round 1 scoring and before each subsequent round).
  OBSERVABLE: explicit rubric load step — glob or read of `simulations/quest/rubrics/` — with gate: if no rubric exists, invoke `quest-rubric` before proceeding.
  STANDARD: rubric confirmed present before first score; proceeding without rubric gate = FAIL.

---

## Recommended Criteria

---

**C-06 — Per-round iteration record**

Without a per-round log, the discovery history is unrecoverable, because the rationale for each criterion addition cannot be reconstructed from the final rubric alone — the log is the audit trail. Not "summarizing at the end," but "appending a structured record after each round with round number, variations run, top composite score, excellence signal extracted, and criterion added."

- **Weight:** recommended
- **Category:** structure
- **Pass:**
  LOCATION: end of each round.
  OBSERVABLE: round log table or structured block with all four fields: Round, Variations, Top composite, QU2 signal (or "none"), Criterion added (or "none").
  STANDARD: all four fields present for every completed round; missing fields = PARTIAL.

---

**C-07 — Excellence signal isolation**

Without explicit contrast framing in QU2, extracted signals conflate winner properties with winner-minus-runner-up gaps, because listing what the winner had does not reveal what made it win. Not "describing the top variation," but "naming the specific output element the winner had that the runner-up lacked — the gap, not the property."

- **Weight:** recommended
- **Category:** depth
- **Pass:**
  LOCATION: QU2 extraction step each round.
  OBSERVABLE: signal stated as a contrast — "winner had X; runner-up lacked X" or structural equivalent; shared properties excluded.
  STANDARD: gap-as-contrast present; property-list-only (no runner-up reference) = PARTIAL; no extraction = FAIL.

---

**C-08 — Criterion proposal completeness**

Without a complete pass condition, a criterion cannot be reliably scored, because a criterion with text but no location or observable is ambiguous under adversarial generation, allowing the model to claim compliance without producing the required output. Not "naming the criterion and its weight," but "writing text, tier assignment, and a three-part pass condition (LOCATION, OBSERVABLE, STANDARD)."

- **Weight:** recommended
- **Category:** correctness
- **Pass:**
  LOCATION: QU3 criterion proposal step.
  OBSERVABLE: proposed criterion includes Text, Tier, and Pass condition decomposed into LOCATION, OBSERVABLE, and STANDARD.
  STANDARD: all three pass sub-fields present; missing any sub-field = PARTIAL.

---

## Aspirational Criteria

---

**C-09 — "What made it golden" narrative**

Without a mechanism narrative, the golden prompt is an existence proof without a lesson, because a reader who can run the skill still cannot know which structural decisions were discovered versus inherited. Not "labeling the golden prompt," but "writing a named section immediately after the body that identifies each structural mechanism the loop discovered, the round it emerged, and the output gap it closed."

- **Weight:** aspirational
- **Category:** depth
- **Pass:**
  LOCATION: golden output file, immediately after the prompt body.
  OBSERVABLE: "What Made It Golden" section naming >= 2 structural mechanisms, each with round citation and the output gap it closed.
  STANDARD: section present with >= 2 mechanisms + round citations; present but < 2 mechanisms = PARTIAL; absent = FAIL.

---

**C-10 — Persistent gap identification**

Without ablated-criteria reporting, zero-activation criteria accumulate silently, because a criterion that never fires across all rounds either covers a gap the variations never exposed or is incorrectly specified — neither case is visible without explicit audit. Not "assuming all criteria are live," but "listing any criteria with zero activations across all rounds with a suggested probe for each."

- **Weight:** aspirational
- **Category:** correctness
- **Pass:**
  LOCATION: golden output file, alongside or after mechanism narrative.
  OBSERVABLE: ablated criteria section listing criteria with zero round activations and a suggested probe; explicit null case "No ablated criteria" when all criteria fired.
  STANDARD: section present with null-case handling; absent = FAIL.

---

**C-11 — Structural termination isolation**

Without structural isolation, the convergence check is absorbed into the iteration body, because an inline termination condition is evaluated by the same role doing iteration work — creating a conflict of interest and making it easy to skip. Not "including a convergence condition inside the loop step," but "giving the convergence check its own named structural element — a dedicated phase, role, or section — whose sole mandate is dual-gate evaluation."

- **Weight:** aspirational
- **Category:** structure
- **Pass:**
  LOCATION: termination logic.
  OBSERVABLE: convergence check is a named, distinct structural element (e.g., PHASE 4, CONVERGENCE JUDGE role) separate from all iteration elements (variator, scorer, analyst, criterion author); its only content is the two-condition gate.
  STANDARD: isolation present and sole mandate is dual-gate; convergence inlined into loop step = FAIL.

---

**C-12 — Contrast-enforced signal isolation**

Without a structural contrast mechanism in QU2, the extraction step can be satisfied with winner description that sounds contrastive but is not, because instructional language alone ("name the gap, not the property") does not prevent the model from filling the field with a property-list. Not "instructing the extractor to state a contrast," but "providing a structural slot — a delta block, contrast column, or paired field — that makes it mechanically impossible to fill without stating an absence."

- **Weight:** aspirational
- **Category:** depth
- **Pass:**
  LOCATION: QU2 extraction step.
  OBSERVABLE: structural mechanism present — delta block with paired fields (e.g., TOP HAD / SECOND LACKED), contrast column, or before/after field pair — that requires the extractor to state what the runner-up lacked, not just what the winner had.
  STANDARD: structural mechanism present and enforces gap-stating; instructional language only = FAIL.

---

**C-13 — Rationale-grounded sequencing**

Without an explanatory clause for the QU2→QU3 ordering, a model under pressure to produce criteria quickly can treat the ordering as a bureaucratic step and violate it, because a bare ordering rule gives no reason to resist the violation. Not "stating the ordering rule," but "accompanying the ordering constraint with a 'because' clause that makes non-compliance self-evidently wrong — grounding compliance in purpose rather than procedure."

- **Weight:** aspirational
- **Category:** behavior
- **Pass:**
  LOCATION: wherever the QU2→QU3 ordering is specified.
  OBSERVABLE: explanatory clause present — "QU2 precedes QU3 because a criterion not grounded in an observed gap is an editorial guess" or equivalent — making the reason for the ordering explicit.
  STANDARD: rationale clause present; ordering stated without explanation = FAIL.

---

**C-14 — Inertia-anchored delta field** *(new in v3)*

Without a dedicated inertia slot in the delta block, the contrast mechanism cannot distinguish loop discoveries from patterns the unconstrained baseline already produces, because a `TOP HAD / SECOND LACKED` pair is satisfied even when inertia produces the same structural feature — making it impossible to tell whether the loop found something or merely confirmed what the model does by default. Not "mentioning inertia in prose," but "including a dedicated `INERTIA LACKED` structural field in the QU2 delta block that requires the extractor to independently verify absence of the winning pattern in the inertia baseline."

- **Weight:** aspirational
- **Category:** depth
- **Pass:**
  LOCATION: QU2 delta block.
  OBSERVABLE: dedicated `INERTIA LACKED` field (or structurally equivalent slot) present alongside the runner-up contrast, requiring the extractor to state what the inertia baseline lacked separately from what the runner-up lacked.
  STANDARD: inertia slot structurally present and distinct from runner-up contrast; prose inertia reference without a dedicated field = PARTIAL; no inertia reference = FAIL.

Round 2 signal: V-05 was the only perfect scorer (100). Its `TOP HAD / INERTIA LACKED` field meant the extractor had to prove the inertia baseline lacked the winning mechanism separately. V-02 (98) had the contrast delta block (C-12) but no inertia anchor, leaving open the possibility that the winning pattern was inertia-present and not a loop discovery.

---

### Scoring formula

```
Score = (essential_pass / 5)   * 60
      + (recommended_pass / 3) * 30
      + (aspirational_pass / 6) * 10
```

| Tier | Criteria | Max pts |
|------|----------|---------|
| Essential (C-01–C-05) | 5 | 60 |
| Recommended (C-06–C-08) | 3 | 30 |
| Aspirational (C-09–C-14) | 6 | 10 |
| **Total** | **14** | **100** |

**Golden threshold:** all 5 essentials pass AND composite >= 80.

### Version history

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-16 | Initial 10 criteria (5E / 3R / 2A) |
| v2 | 2026-03-16 | +3 aspirationals from R1 signals: C-11 (termination isolation), C-12 (contrast enforcement), C-13 (rationale sequencing); denominator 2→5 |
| v3 | 2026-03-16 | +1 aspirational from R2 signal: C-14 (inertia-anchored delta field); denominator 5→6 |
