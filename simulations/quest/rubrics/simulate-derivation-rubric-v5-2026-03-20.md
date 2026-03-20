v5 rubric written. Here's what changed:

**Three new aspirational criteria (C-20, C-21, C-22)** — each generalizes an R4 pattern beyond the specific context where it was first observed:

| ID | Pattern | What it detects |
|----|---------|-----------------|
| C-20 | Consequence-naming as hard gate | Gate instruction names the BLOCKED verdict token, not just the required correction -- "SOUND BLOCKED" forces the LLM to verify the prohibition is cleared, not just that some action was taken |
| C-21 | Commitment label alignment | Each axis label in any commitment table names the exact mechanistic operation, not a general category -- test: could a non-compliant behavior satisfy the label by reasonable reading? If yes, fail |
| C-22 | Unconditional three-tier ordering | Any multi-tier ordering rule is stated as a single unconditional enumeration -- the conditional form ("if P1 exists... if P2 exists...") closes the top tier but leaves all subordinate ordering gaps invisible |

**Point structure:** 60 + 30 + 70 = **160 total** (14 aspirational × 5).

**Scoring bands:**
- Exemplary: 130-160 (scaled from v4's 81.4%)
- Proficient: 100-129
- Adequate: 60-99
- Failing: <60

**R4 ceiling in v5 terms:** V-05 satisfies all three new criteria by construction, so it maps 145/145 → 160/160 Exemplary. The new criteria create ceiling room for R5's V-07 to demonstrate these patterns as first-principles commitments rather than downstream fixes.
criteria
(names "SOUND BLOCKED", axis C label is "NEW-tagged fault detection", three-tier ordering is
unconditional), so V-05 maps to 160/160 -- Exemplary. R5 objective: a V-07 prompt that encodes
all three new patterns as independently verifiable commitments from first principles, not as
downstream fixes to existing language.

---

## Essential Criteria (60 pts total)

### C-01 | Derivation map present and complete
- **Category**: correctness
- **Weight**: essential
- **Points**: 12
- **Pass condition**: A derivation map table is present with columns: S-ID, expression
  applied, resulting expression, justification, and type
  (EXACT / APPROX / DEFINITION / PHYSICAL). Every non-trivial derivation step in the
  source artifact has a corresponding row. At least 3 rows present (or all steps if
  fewer than 3 exist).

---

### C-02 | Step-by-step verification block for each step
- **Category**: correctness
- **Weight**: essential
- **Points**: 12
- **Pass condition**: Each S-ID in the derivation map has a corresponding verification
  block containing: algebraic correctness verdict (YES / NO / CONDITIONAL), dimensional
  consistency check (YES / NO / NOT APPLICABLE), sign check (YES / NO), and a final
  verdict (SOUND / WEAK / BROKEN). No S-ID is skipped.

---

### C-03 | Every APPROX step is explicitly flagged
- **Category**: correctness
- **Weight**: essential
- **Points**: 12
- **Pass condition**: For every step typed APPROX in the derivation map, the verification
  block states: (a) what quantity or relationship is being approximated, (b) the validity
  condition under which the approximation holds, and (c) whether the source paper states
  this approximation. If the paper has zero APPROX steps, this criterion auto-passes with
  a note confirming that fact.

---

### C-04 | Derivation Fault Register present and actionable
- **Category**: coverage
- **Weight**: essential
- **Points**: 12
- **Pass condition**: A fault register table exists with columns F-ID, S-ID, verdict,
  type, description, and fix. Every step with verdict WEAK or BROKEN appears in the
  fault register. Each fault has a severity label (P1 / P2 / P3): P1 = algebraically
  wrong, P2 = unstated approximation, P3 = notational/clarity issue. If no faults are
  found, the register explicitly states "No faults found" with a brief justification.

---

### C-05 | Artifact written with required frontmatter
- **Category**: format
- **Weight**: essential
- **Points**: 12
- **Pass condition**: The artifact is written to `signals/simulate/derivation/` (or the
  `--output` path if provided). Frontmatter contains exactly: `skill: simulate-derivation`,
  `topic`, `date`, `steps_traced` (integer), `p1_errors` (integer), `unstated_approx`
  (integer). Values are consistent with the derivation map and fault register.

---

## Recommended Criteria (30 pts total)

### C-06 | Overall derivation soundness verdict is explicit
- **Category**: depth
- **Weight**: recommended
- **Points**: 10
- **Pass condition**: The artifact states whether the derivation is globally sound. The
  verdict is one of: SOUND (all steps verified), CONDITIONALLY SOUND (all steps verified
  under stated approximations), or BROKEN (at least one P1 error blocks the conclusion).
  The verdict appears in a summary section, not buried in a step block.

---

### C-07 | Amend section maps to actual faults found
- **Category**: behavior
- **Weight**: recommended
- **Points**: 10
- **Pass condition**: The AMEND section provides exactly three targeted fixes. Each fix
  references a specific F-ID from the fault register. If P1 faults exist, at least one
  fix addresses a P1. If P2 faults exist, at least one fix addresses a P2. Fixes are
  ordered by severity: P1 fixes precede P2 fixes, which precede P3 fixes -- the
  first fix is always the highest-severity fault present. Fixes are specific enough to
  act on (not generic advice like "check the algebra"). An Amend section that cites
  correct F-IDs but applies no ordering rule does not satisfy this criterion.

---

### C-08 | Step types are correctly classified
- **Category**: correctness
- **Weight**: recommended
- **Points**: 10
- **Pass condition**: EXACT steps cite or sketch the algebraic identity that makes them
  exact (e.g., "product rule," "distributivity," "substitution of Eq. 3"). PHYSICAL steps
  state the physical assumption being encoded (e.g., "at equilibrium, dR/dt = 0").
  Spot-check: at least 2 randomly selected EXACT or PHYSICAL steps have traceable
  justifications; none are labeled EXACT when they contain an unexplained jump.

---

## Aspirational Criteria (70 pts total)

### C-09 | Catches at least one fault not acknowledged by the paper
- **Category**: depth
- **Weight**: aspirational
- **Points**: 5
- **Pass condition**: At least one fault in the fault register identifies an error,
  unstated approximation, or dimensional inconsistency not already flagged or caveated
  in the source paper itself. The fault register entry notes "not acknowledged by paper"
  or equivalent.

---

### C-10 | Expands compressed steps with intermediate lines
- **Category**: depth
- **Weight**: aspirational
- **Points**: 5
- **Pass condition**: At least one step in the derivation map where the paper skips an
  intermediate algebraic step is expanded. The intermediate expression is supplied as a
  sub-step (S-03a, S-03b pattern) and marked as "(interpolated)" to distinguish it from
  the paper's own steps.

---

### C-11 | APPROX verification includes tracer's independent validity statement
- **Category**: depth
- **Weight**: aspirational
- **Points**: 5
- **Source**: V-04 excellence signal -- prose-required-approx-sub-block
- **Pass condition**: For each APPROX step, the tracer provides an independent
  substantive statement of (a) what is being approximated and (b) the conditions under
  which the approximation holds -- stated in the tracer's own words, derived from domain
  knowledge or first principles. Simply reporting whether the source paper states the
  approximation (YES/NO) does not satisfy this criterion. The paper's coverage is noted
  separately as (c). If the artifact has zero APPROX steps, this criterion auto-passes
  with a confirming note.

---

### C-12 | Fault severity labels appear inline in Amend fixes
- **Category**: behavior
- **Weight**: aspirational
- **Points**: 5
- **Source**: V-04 excellence signal -- severity-inline-amend
- **Pass condition**: Each fix in the AMEND section includes the fault's severity label
  in the format "[F-ID] [P1/P2/P3]: [specific fix]", making severity triage visible at
  the point of recommended action, not only in the fault register. A fix that cites the
  F-ID but omits the severity label does not satisfy this criterion.

---

### C-13 | Verification blocks contain substantive prose per check
- **Category**: correctness
- **Weight**: aspirational
- **Points**: 5
- **Source**: V-04 excellence signal -- token-budget-redirect (output translation)
- **Pass condition**: For at least half of the verification blocks, each of the three
  primary checks (algebraic, dimensional, sign) is accompanied by at least one sentence
  of reasoning -- not bare YES/NO verdicts. Example: "YES -- both sides have units of
  [kg/s]; the time derivative of mass is dimensionally consistent." Blocks providing
  only YES/NO with no explanation for any check do not satisfy this criterion.

---

### C-14 | APPROX validity reasoning is demonstrably independent of source phrasing
- **Category**: depth
- **Weight**: aspirational
- **Points**: 5
- **Source**: V-05 excellence signal -- own-words-gate
- **Pass condition**: For each APPROX step, the tracer's statement of (b) the validity
  condition uses vocabulary and framing that cannot be produced by lightly rewording the
  source sentence. The reasoning traces to a named domain principle (e.g., "small-angle
  regime," "quasi-static assumption," "low Reynolds number") or a first-principles
  argument that the tracer could have stated without reading the source sentence. A
  statement that paraphrases what the paper says -- even using different words -- does
  not satisfy this criterion. The distinguishing test: if the source sentence were
  removed, would the tracer's (b) statement still be fully supportable? If yes, it is
  independent. If no, it is paraphrase. If the artifact has zero APPROX steps, this
  criterion auto-passes with a confirming note.

---

### C-15 | All structural axes present simultaneously without phase-dropping
- **Category**: coverage
- **Weight**: aspirational
- **Points**: 5
- **Source**: V-05 excellence signal -- three-axis-no-degradation
- **Pass condition**: If and only if the artifact contains all three structural axes --
  (a) interpolated sub-steps from a Phase 1b expansion pass, (b) NEW-tagged faults in
  the fault register identifying paper-unacknowledged errors, and (c) prose reasoning in
  verification blocks -- then all three must hold simultaneously with no silent
  degradation. Specifically: every interpolated sub-step has a corresponding verification
  block (no Phase 2 holes at expanded rows); every NEW-tagged fault has a complete fault
  register entry with F-ID, description, and fix; and the prose rule applies to both
  APPROX sub-blocks and primary checks with no block reverting to bare YES/NO. If fewer
  than all three axes are present in the artifact, this criterion scores 0 -- it rewards
  full integration only.

---

### C-16 | Prose reasoning density is uniform across APPROX sub-blocks and primary checks
- **Category**: correctness
- **Weight**: aspirational
- **Points**: 5
- **Source**: V-05 excellence signal -- prose-rule-synergy
- **Pass condition**: The artifact does not exhibit a two-tier reasoning density where
  APPROX sub-blocks contain explanatory sentences but the primary verification checks
  (algebraic, dimensional, sign) in the same step are bare YES/NO tokens -- or vice
  versa. In any step block where the APPROX sub-block contains at least one sentence of
  reasoning, the primary checks in that same block must also contain at least one sentence
  of reasoning. Uniform density -- sparse throughout or rich throughout -- passes. Mixed
  density within a single step block fails. The behavioral inconsistency of
  prose-required APPROX alongside bare-allowed primary checks is a token-budget leak
  regardless of whether the individual check verdicts are technically correct.

---

### C-17 | APPROX independence gate includes mandatory recovery instruction
- **Category**: depth
- **Weight**: aspirational
- **Points**: 5
- **Source**: R3 excellence signal -- source-removal-recovery-path
- **Pass condition**: For each APPROX step where the source-removal test is applied, the
  skill includes an explicit mandatory recovery path: "If the validity statement (b) does
  not survive removal of the source sentence -- i.e., it is paraphrase -- replace (b)
  with a statement grounded in a named domain principle or first-principles argument
  before completing the verification block." The recovery instruction is unconditional:
  the tracer cannot record a SOUND verdict on an APPROX block while (b) remains a
  paraphrase. A skill that identifies paraphrase via the source-removal test but treats
  correction as optional (advisory language: "consider revising," "may want to replace")
  does not satisfy this criterion. If the artifact has zero APPROX steps, this criterion
  auto-passes with a confirming note.

---

### C-18 | Axis-commitment gateway table gates Phase 2 entry
- **Category**: coverage
- **Weight**: aspirational
- **Points**: 5
- **Source**: R3 excellence signal -- pre-phase-gateway-table
- **Pass condition**: The artifact includes a three-row commitment table immediately
  before Phase 2, asserting ACTIVE or ABSENT for each structural axis: (A) interpolated
  sub-step expansion, (B) prose reasoning rule, and (C) NEW-tagged fault detection. The
  table is followed by an unconditional gate statement: "Do NOT proceed to Phase 2 until
  all present axes show ACTIVE." If an axis is ABSENT, the artifact records the reason.
  The gate is a commitment device, not a checklist -- it must be structurally positioned
  to block Phase 2 entry, not appended after Phase 2 begins. An artifact that enters
  Phase 2 without this explicit commitment table does not satisfy this criterion, even if
  all three axes are in fact active throughout the output.

---

### C-19 | Amend fixes are ordered by severity (P1 first)
- **Category**: behavior
- **Weight**: aspirational
- **Points**: 5
- **Source**: R3 excellence signal -- severity-priority-ordering-amend
- **Pass condition**: The AMEND section applies an explicit severity-ordering rule: P1
  fixes appear first, then P2 fixes, then P3 fixes. When the fault register contains
  faults at multiple severity levels, the first fix in AMEND always addresses the
  highest-severity fault present. The ordering rule must be stated explicitly in the
  skill instruction or AMEND preamble ("order fixes by severity: P1 first, then P2,
  then P3") -- an Amend section that incidentally lists a P1 fix first without an
  explicit ordering rule does not satisfy this criterion. When only one severity level
  is present, any ordering passes. Artifacts with no faults auto-pass with a confirming
  note.

---

### C-20 | Mandatory gates name the prohibited action explicitly
- **Category**: depth
- **Weight**: aspirational
- **Points**: 5
- **Source**: R4 excellence signal -- consequence-naming-as-hard-gate
- **Pass condition**: Where the skill includes a mandatory gate (e.g., APPROX
  source-removal failure, axis-commitment failure), the gate instruction explicitly names
  the downstream action that is BLOCKED until compliance -- not merely the correction
  that is required. Accepted forms: "[VERDICT TOKEN] BLOCKED for this step" or "A
  [VERDICT TOKEN] verdict may not be recorded... while [condition] remains." The
  prohibited-action name functions as a re-check signal: the LLM must evaluate whether
  the prohibition has been cleared, not merely whether some action was taken. A recovery
  instruction that states only what TO DO ("replace (b) before recording your verdict")
  without naming what CANNOT happen does not satisfy this criterion -- an LLM can perform
  a cosmetically different but still-non-compliant action and proceed. This criterion
  applies to all mandatory gates in the skill, not only the APPROX gate. If the artifact
  contains no mandatory gates, this criterion auto-passes with a confirming note.

---

### C-21 | Gateway axis labels name exact mechanistic behaviors
- **Category**: coverage
- **Weight**: aspirational
- **Points**: 5
- **Source**: R4 excellence signal -- commitment-label-alignment
- **Pass condition**: Each row label in every axis-commitment gateway table names the
  precise mechanistic operation being committed to -- specific enough that the LLM cannot
  satisfy the label without performing the correct action. A label that names a general
  category rather than the specific operation does not satisfy this criterion.
  Distinguishing test: could a different, non-compliant behavior satisfy the label by a
  reasonable reading? If yes, the label is too general. Failing examples: "Source
  acknowledgment gate" (satisfiable by any acknowledgment act); "Expansion pass"
  (satisfiable by any expansion). Passing examples: "NEW-tagged fault detection for
  unacknowledged errors" (requires the specific tagging operation); "Interpolated
  sub-step expansion with S-NNa/S-NNb labeling" (requires the specific format). This
  criterion applies to every commitment table in the artifact. If the artifact contains
  no commitment tables, this criterion scores 0.

---

### C-22 | Ordering rules stated as unconditional enumeration, not conditional chain
- **Category**: behavior
- **Weight**: aspirational
- **Points**: 5
- **Source**: R4 excellence signal -- unconditional-three-tier-ordering
- **Pass condition**: Any multi-tier ordering rule in the skill (severity ordering, phase
  ordering, or any ranked sequence) is stated as a single unconditional sentence that
  enumerates all tiers in order: "P1 fixes first, then P2 fixes, then P3 fixes" (or
  equivalent). A conditional chain -- "if P1 faults exist, address P1 first; if no P1
  but P2 faults exist, address P2 first" -- does not satisfy this criterion. The
  conditional form ensures the top tier leads but leaves all subordinate-tier relative
  ordering implicit: an Amend with P2 and P3 faults where a P3 fix precedes a P2 fix
  satisfies the conditional form while violating the intended ordering. The unconditional
  form makes every tier relationship explicit in a single declarative statement, leaving
  no gap invisible. If the artifact contains no multi-tier ordering rules, this criterion
  auto-passes with a confirming note.

---

## Quick Reference

| ID   | Criterion                                              | Weight       | Category    | Pts |
|------|--------------------------------------------------------|--------------|-------------|-----|
| C-01 | Derivation map present and complete                    | essential    | correctness | 12  |
| C-02 | Verification block for each step                       | essential    | correctness | 12  |
| C-03 | Every APPROX step explicitly flagged                   | essential    | correctness | 12  |
| C-04 | Fault register present and actionable                  | essential    | coverage    | 12  |
| C-05 | Artifact with required frontmatter                     | essential    | format      | 12  |
| C-06 | Overall soundness verdict explicit                     | recommended  | depth       | 10  |
| C-07 | Amend maps to actual faults (P1-first ordered)         | recommended  | behavior    | 10  |
| C-08 | Step types correctly classified                        | recommended  | correctness | 10  |
| C-09 | Catches fault not in paper                             | aspirational | depth       | 5   |
| C-10 | Expands compressed steps                               | aspirational | depth       | 5   |
| C-11 | APPROX verified independently (prose)                  | aspirational | depth       | 5   |
| C-12 | Severity labels inline in Amend fixes                  | aspirational | behavior    | 5   |
| C-13 | Verification blocks contain prose reasoning            | aspirational | correctness | 5   |
| C-14 | APPROX reasoning independent of source                 | aspirational | depth       | 5   |
| C-15 | All axes stack without phase-dropping                  | aspirational | coverage    | 5   |
| C-16 | Prose density uniform across block types               | aspirational | correctness | 5   |
| C-17 | APPROX independence gate has mandatory recovery        | aspirational | depth       | 5   |
| C-18 | Axis-commitment gateway table gates Phase 2 entry      | aspirational | coverage    | 5   |
| C-19 | Amend fixes ordered by severity (P1 first)             | aspirational | behavior    | 5   |
| C-20 | Mandatory gates name the prohibited action explicitly  | aspirational | depth       | 5   |
| C-21 | Gateway axis labels name exact mechanistic behaviors   | aspirational | coverage    | 5   |
| C-22 | Ordering rules stated as unconditional enumeration     | aspirational | behavior    | 5   |
|      | **Total**                                              |              |             | **160** |

---

## Scoring Bands (v5)

| Band       | Score Range | Meaning                                                              |
|------------|-------------|----------------------------------------------------------------------|
| Exemplary  | 130-160     | All essential + recommended pass; 8+ aspirational earned             |
| Proficient | 100-129     | All essential pass; all recommended pass; 2+ aspirational earned     |
| Adequate   | 60-99       | All essential pass; recommended partially met                        |
| Failing    | < 60        | One or more essential criteria fail                                  |

A score below 60 (any essential failure) is a failing output regardless of total points.

**R4 ceiling in v5 terms**: V-05 scored 145/145 under v4. V-05 satisfies all three new
criteria -- names "SOUND BLOCKED" (C-20), axis C label is "NEW-tagged fault detection" (C-21),
three-tier ordering stated unconditionally (C-22) -- so V-05 maps to 160/160 in v5, Exemplary.
The R5 objective is a V-07 prompt that encodes all three new patterns as independently
verifiable commitments from first principles, not as downstream fixes to existing language.
