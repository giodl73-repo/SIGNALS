Reading the scorecard carefully to identify the four structural mechanisms introduced by V-01 through V-04, then composing the v4 rubric.

---

## quest-golden Scoring Rubric — v4

**18 criteria across 3 tiers.** 4 new aspirationals added from Round 3 excellence signals.

---

### What changed from v3

**Four new aspirational criteria extracted from Round 3 scorecard patterns:**

**C-15 — Spread-design phase with hypothesis rationale** *(category: structure)*

The loop must begin with an explicit spread-design phase that articulates what each variation tests before running it. V-01 introduced a dedicated SPREAD-DESIGN phase as Phase 0/1 that states the hypothesis each variation covers and confirms the spread reaches distinct territory. Without this, variations are generated ad-hoc: coverage is accidental, redundant hypotheses go undetected, and the loop cannot distinguish "we tested this" from "we never tried this angle."

Round 3 signal: V-01 was the only variation to open with an explicit SPREAD-DESIGN phase. All other variations implied variation rationale but did not structurally commit to it before execution. V-05 (synthesis) inherited this mechanism. The phase prevents the loop from producing five variations that are all slight rewrites of the same hypothesis.

**C-16 — Named-round convergence citation** *(category: correctness)*

The convergence gate must name specific round numbers — "Round [N] signal = [value] AND Round [N-1] signal = [value]" — and the values must be traceable to the Round Log. V-02 introduced this named-round precision as a structural requirement: "Do not declare Quest convergence YES unless both named rounds are shown in the Round Log with explicit signal values." Without named-round citation, a single round of `none` can satisfy a loosely worded convergence check; the executor can claim two consecutive `none` rounds without showing both in the log.

Round 3 signal: V-01 used the structural convergence gate but did not require naming round numbers. V-02 added named-round precision as an independent enforcement mechanism. V-05 (synthesis) inherited both. The named-round citation closes the gap between structural presence of the gate and auditability of the convergence claim.

**C-17 — PARTIAL trajectory amplifier** *(category: depth)*

The round log must include a trajectory column or table that tracks partial-pass evolution across rounds, distinguishing variations that are improving from those that are plateauing. V-03 introduced a PARTIAL amplifier mechanism: criteria that a variation partially satisfies in one round are flagged and tracked into the next, so near-miss variations are not invisible to the spread-design phase. Without trajectory tracking, a variation that scores 0 on C-08 in Round 1 and 0 in Round 2 looks identical to one that scores 0 then near-passes; both look like failures, but only one is a productive lead.

Round 3 signal: V-03 was the only variation to add explicit trajectory tracking of PARTIAL passes. Its round log extended the standard Round / Top / vs Inertia / QU2 delta columns with partial-pass amplification. No other variation captured this mechanism. The trajectory table makes the loop's learning curve legible.

**C-18 — Pre-committed scoring matrix** *(category: correctness)*

The scoring matrix for each round must be printed before variations are run, committing to the evaluation structure prior to seeing outputs. V-04 introduced a pre-printed matrix that lists all criteria and their pass conditions at the start of each phase, before the variation responses are generated or scored. Without pre-commitment, scores can be assigned post-hoc: the extractor sees which variation produced the best output and works backward to justify its score, introducing hindsight bias. The pre-printed matrix makes the scoring sequence auditable — if a criterion was not listed before execution, any score on it is suspect.

Round 3 signal: V-04 was the only variation to require pre-printing the scoring matrix before variation execution. Its PHASE 1 explicitly printed the criteria table before generating responses. V-05 (synthesis) inherited this mechanism alongside the spread-design phase and named-round gate. Pre-commitment is the structural complement to rationale-grounded sequencing (C-13): sequencing orders the phases; pre-commitment orders the evaluation within each phase.

---

### Formula update

Aspirational denominator changes from 6 → 10 as the tier grows:

```
Score = (essential_pass / 5)    * 60
      + (recommended_pass / 3)  * 30
      + (aspirational_pass / 10) * 10
```

Golden threshold unchanged: all 5 essentials pass AND composite >= 80.

---

### Tier overview

| Tier | Criteria | Weight |
|------|----------|--------|
| Essential | C-01 through C-05 | 60 pts total |
| Recommended | C-06 through C-08 | 30 pts total |
| Aspirational | C-09 through C-18 | 10 pts total |

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
  OBSERVABLE: standalone rubric file written to `simulations/quest/rubrics/{skill}-rubric-v{N}-{date}.md`; contains all converged criteria with text, tier, and three-part pass conditions; composite formula with current denominator; golden threshold stated explicitly; version history table.
  STANDARD: standalone file present and self-contained; inline-only or summary-only = FAIL.

---

**C-04 — QU2 precedes QU3**

Without enforcing QU2 before QU3, criterion proposals are editorial guesses, because the only valid source for a new criterion is an observed output gap — what the winner had that the runner-up lacked. Not "suggesting improvements to the rubric," but "grounding every proposed criterion in a named structural gap observed in this round's outputs, before proposing it."

- **Weight:** essential
- **Category:** structure
- **Pass:**
  LOCATION: iteration body, signal extraction step.
  OBSERVABLE: QU2 (delta block extraction) completed and signal named before QU3 (criterion proposal) is attempted; QU3 explicitly gated on QU2 signal not being `none`.
  STANDARD: QU2 output present before QU3 in every round; QU3 proposed without prior QU2 signal = FAIL.

---

**C-05 — Rubric present at loop start**

Without loading the rubric before scoring, variation rankings have no grounded objective function, because scores assigned without a prior rubric cannot be compared across rounds and cannot detect when the rubric itself needs updating. Not "scoring variations and then checking the rubric," but "loading the current rubric version before generating or evaluating any variation."

- **Weight:** essential
- **Category:** structure
- **Pass:**
  LOCATION: loop initialization (Phase 0 or equivalent).
  OBSERVABLE: rubric loaded from `simulations/quest/rubrics/{skill}-rubric-*.md`; latest version identified; if no rubric exists, `quest-rubric` invoked before proceeding; rubric version logged.
  STANDARD: rubric load step present before first variation scored; post-hoc rubric loading = FAIL.

---

## Recommended Criteria

---

**C-06 — Per-round iteration record**

Without a round log, convergence claims are unverifiable, because the executor can declare two consecutive `none` rounds without showing the evidence. Not "summarizing what happened," but "maintaining a structured log entry for every round with all required fields filled."

- **Weight:** recommended
- **Category:** correctness
- **Pass:**
  LOCATION: round log (maintained across all iterations).
  OBSERVABLE: one entry per round containing: Round number / Top variation / vs Inertia delta (score gap) / QU2 delta (signal name or `none`) / Criterion proposed (name or `none`).
  STANDARD: all four fields present per round; missing fields = FAIL for that round.

---

**C-07 — Excellence signal isolation**

Without isolating the excellence signal as an absence in the runner-up, the delta block describes a winner but does not identify what the loop discovered, because "the winner was better" is not the same as "the runner-up lacked this specific structural element." Not "comparing scores," but "stating what the winner had that the runner-up structurally lacked."

- **Weight:** recommended
- **Category:** depth
- **Pass:**
  LOCATION: QU2 delta block (within iteration body).
  OBSERVABLE: structural paired field TOP HAD / SECOND LACKED present; runner-up gap stated as an absence, not a quality judgment; signal is `none` if no structural gap can be identified.
  STANDARD: absence statement present; "winner was clearer" or score-gap-only = FAIL.

---

**C-08 — Criterion proposal completeness**

Without a three-part pass condition, a proposed criterion cannot be operationalized, because a criterion without LOCATION, OBSERVABLE, and STANDARD cannot be applied consistently by a scorer who was not present. Not "describing what excellence looks like," but "specifying where to look, what to observe, and what the pass/fail line is."

- **Weight:** recommended
- **Category:** correctness
- **Pass:**
  LOCATION: QU3 criterion proposal (within iteration body, gated on QU2 signal).
  OBSERVABLE: proposal includes: criterion text / tier with rationale (essential = wrong without it; recommended = better with it; aspirational = excellent) / LOCATION / OBSERVABLE / STANDARD.
  STANDARD: all five components present; missing any one component = FAIL for that proposal.

---

## Aspirational Criteria

---

**C-09 — "What made it golden" narrative**

The golden output must include a section explaining what structural mechanisms the loop discovered and why each one mattered, with round citations and inertia-gap descriptions for each mechanism.

- **Weight:** aspirational
- **Category:** depth
- **Pass:**
  LOCATION: golden output artifact (final section after full prompt body).
  OBSERVABLE: section titled "What Made It Golden" or equivalent; minimum 2 mechanisms named; each mechanism includes the round it was discovered and the specific inertia gap it closed.
  STANDARD: 2+ mechanisms with round citations and inertia-gap descriptions present; single mechanism or no citations = FAIL.

---

**C-10 — Persistent gap identification**

The golden output must identify criteria that were never activated across any round, with a suggested probe for each, and must explicitly state `none` if all criteria were activated.

- **Weight:** aspirational
- **Category:** depth
- **Pass:**
  LOCATION: golden output artifact (ablated criteria section).
  OBSERVABLE: section listing criteria with zero activations across all rounds; suggested probe per ablated criterion; explicit null case ("No ablated criteria") if none.
  STANDARD: ablated criteria section present with null case handled; omission of this section = FAIL.

---

**C-11 — Structural termination isolation**

The termination check must occupy a dedicated named phase or structural role, not be merged with the iteration body, so that its evaluation is visually and structurally separable from the round's work.

- **Weight:** aspirational
- **Category:** structure
- **Pass:**
  LOCATION: dedicated phase/section after iteration body (not inside it).
  OBSERVABLE: phase has a distinct name (e.g., "PHASE 4 — CONVERGENCE CHECK"); entry condition states that iteration body is complete; sole mandate of the phase is dual-gate evaluation.
  STANDARD: termination check in its own named phase; merged with iteration body = FAIL.

---

**C-12 — Contrast-enforced signal isolation**

The delta block must use a structural paired-field format that makes it mechanically impossible to fill without stating an absence — both from the runner-up and from the inertia baseline.

- **Weight:** aspirational
- **Category:** depth
- **Pass:**
  LOCATION: QU2 delta block (within iteration body).
  OBSERVABLE: two structural fields present: TOP HAD / SECOND LACKED and TOP HAD / INERTIA LACKED; each field requires an absence statement; signal = `none` if either field cannot be filled with a structural difference.
  STANDARD: both paired fields present; single-field delta block = FAIL.

---

**C-13 — Rationale-grounded sequencing**

Phase and step ordering must include explanatory "because" clauses so that non-compliance is self-evidently wrong to the executor, not just structurally forbidden.

- **Weight:** aspirational
- **Category:** structure
- **Pass:**
  LOCATION: phase headers or step instructions for any ordering constraint.
  OBSERVABLE: at least one ordering constraint accompanied by an explanatory "because" clause stating the failure mode it prevents; the reasoning must be specific (not "order matters") and grounded in the output gap it closes.
  STANDARD: at least one "because" clause with specific failure-mode reasoning present; ordering-only without rationale = FAIL.

---

**C-14 — Inertia-anchored delta field**

The QU2 delta block must include a dedicated `INERTIA LACKED` slot that separately states what the inertia baseline lacked, distinct from the runner-up contrast, to prevent crediting inertia-present patterns as loop discoveries.

- **Weight:** aspirational
- **Category:** depth
- **Pass:**
  LOCATION: QU2 delta block (within iteration body).
  OBSERVABLE: structural field TOP HAD / INERTIA LACKED present as a dedicated slot; annotated as "this is the discovery"; signal = `none` if field cannot be filled with a structural difference absent from the inertia baseline.
  STANDARD: dedicated inertia slot present with discovery annotation; absence of inertia slot or merger with SECOND LACKED field = FAIL.

---

**C-15 — Spread-design phase with hypothesis rationale**

The loop must begin with an explicit spread-design phase that states what hypothesis each variation tests and confirms the spread reaches distinct territory before any variation is generated. Without this, variations are generated ad-hoc: coverage is accidental, redundant hypotheses go undetected, and the loop cannot distinguish "we tested this angle" from "we never considered this angle."

- **Weight:** aspirational
- **Category:** structure
- **Pass:**
  LOCATION: opening phase before first variation is generated (Phase 0 or Phase 1).
  OBSERVABLE: a named spread-design step that lists each planned variation with a one-line hypothesis statement; at least one check or assertion that the spread covers distinct territory (e.g., no two variations share the same hypothesis); phase appears before any variation response is generated.
  STANDARD: spread-design phase with per-variation hypothesis present before execution; post-hoc variation labeling = FAIL.

---

**C-16 — Named-round convergence citation**

The convergence gate must name specific round numbers — "Round [N] signal = [value] AND Round [N-1] signal = [value]" — with values traceable to the Round Log, making it mechanically impossible to declare convergence without showing both rounds in the log.

- **Weight:** aspirational
- **Category:** correctness
- **Pass:**
  LOCATION: convergence gate / termination check phase.
  OBSERVABLE: convergence gate contains named round references (e.g., "Round 3 signal = none AND Round 2 signal = none") rather than generic labels ("this round" / "previous round"); stated values are present in the Round Log; explicit instruction not to declare convergence YES without showing both named rounds.
  STANDARD: named round numbers with log-traceable values present; generic "previous round" phrasing without round numbers = FAIL.

---

**C-17 — PARTIAL trajectory amplifier**

The round log must track partial-pass evolution across rounds via a trajectory column or table, so that near-miss variations are distinguishable from far-miss variations and can guide next-round spread design.

- **Weight:** aspirational
- **Category:** depth
- **Pass:**
  LOCATION: round log (alongside per-round iteration records).
  OBSERVABLE: trajectory column or supplemental table that flags criteria where a variation partially satisfied the pass condition; partial-pass entries carried forward across rounds; spread-design phase for subsequent rounds explicitly references trajectory data when selecting variation hypotheses.
  STANDARD: trajectory tracking present and referenced in spread-design; round log with only binary pass/fail and no partial-pass tracking = FAIL.

---

**C-18 — Pre-committed scoring matrix**

The scoring matrix for each round must be printed before variations are run, committing to the evaluation structure prior to seeing outputs, so that scores cannot be assigned post-hoc after the winner is known.

- **Weight:** aspirational
- **Category:** correctness
- **Pass:**
  LOCATION: phase header, before variation responses are generated or evaluated.
  OBSERVABLE: criteria table (or scoring matrix) printed at the start of each round's evaluation phase, before any variation output is shown; table lists all active criteria and their pass conditions; scoring proceeds against the pre-printed table.
  STANDARD: scoring matrix printed before variation execution in each round; matrix introduced only after variations are shown = FAIL.

---

### Version history

| Version | Criteria | Aspirational denominator | Change |
|---------|----------|--------------------------|--------|
| v1 | 8 | — | Initial |
| v2 | 13 | 5 | +5 aspirationals from Round 1 |
| v3 | 14 | 6 | +1 aspirational (C-14) from Round 2 |
| v4 | 18 | 10 | +4 aspirationals (C-15..C-18) from Round 3 |
