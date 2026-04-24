Written to `simulations/quest/rubrics/review-customers-rubric-v3-2026-03-14.md`.

---

**v3 changes summary:**

Three new aspirational criteria extracted from R2 patterns:

| ID | Criterion | Category | R2 source |
|----|-----------|----------|-----------|
| C-14 | Prose-first scoring order | reliability | V-05 prose-first resolved C-11 PARTIAL in V-01/V-04 by co-locating score and flag in the same block |
| C-15 | Flag deferral prohibition | reliability | V-03's "Do not defer flags" prohibition is the strongest C-11 enforcement language in R2 |
| C-16 | Causal precision: sub-feature specificity | depth | V-02's worked anti-pattern example drove sub-feature-level specificity that abstract rules cannot enforce |

**The three patterns map to distinct failure modes:**

- **C-14** targets the *structural phase gap* — table-first hybrids separate scores (Phase 2) from flags (Phase 3), so they can't be co-located. Prose-first makes the table a compiled artifact, not a preliminary scaffold.
- **C-15** targets the *deferral failure mode* — a post-hoc DETECT phase can still silently omit flags if skipped or incomplete. C-15 prohibits deferral rather than just encouraging inline placement, which is categorically stronger than C-11's presence check.
- **C-16** targets the *generality ceiling* — C-13 accepts feature-level causal framing ("the feature lacks X"). C-16 requires sub-feature granularity ("the feature's specific capability/threshold/design decision Y produced this reaction"), which is directly actionable as an amendment target.

**Scoring summary:** 8 aspirational criteria (was 5), reliability category now has 3 criteria (C-11, C-14, C-15), depth has 4 (C-08, C-09, C-13, C-16).
sible to defer, catching the failure mode before it occurs.
- **C-16** upgrades C-13 from "causal rationale that names a feature gap as mechanism" to "causal
  rationale that names a sub-feature property at specific granularity." C-13 accepts "the feature
  lacks X" as causal; C-16 requires "the feature's [specific capability/threshold/design decision Y]
  produced this reaction." Worked anti-pattern examples drive this distinction more reliably than
  abstract rules because the model sees what contextual framing looks like and explicitly avoids it.

---

## Essential Criteria

Failure on any essential criterion caps the total score regardless of other passes.

### C-01 -- All 12 Personas Present and Scored

- **Weight**: essential
- **Category**: correctness
- **Text**: Every persona in the stock set (C-01 through C-12) appears in the output with explicit
  scores for usefulness, clarity, and would-adopt on a 1-5 scale.
- **Pass condition**: Output contains all 12 persona identifiers (C-01 through C-12) with three
  numeric scores each. Missing persona or missing any of the three score dimensions = FAIL.

### C-02 -- Weighted Aggregate Score Computed

- **Weight**: essential
- **Category**: correctness
- **Text**: A weighted aggregate score is computed using the correct multipliers: primary audience
  3x, secondary audience 2x, non-target 1x. The final score is presented as a single number or
  range on a normalized scale.
- **Pass condition**: Output explicitly states the weighting scheme applied (3x/2x/1x) and
  presents a computed aggregate. An unweighted average or missing aggregate = FAIL.

### C-03 -- Adoption Blockers Identified

- **Weight**: essential
- **Category**: correctness
- **Text**: Any primary-audience persona with would-adopt < 3 is flagged as an adoption blocker.
  Blockers are named by persona ID and the low score is cited.
- **Pass condition**: If any primary persona scores would-adopt < 3, they appear in a dedicated
  blockers section. If no primary persona scores < 3, output explicitly states "no adoption
  blockers." Silently omitting the blocker check = FAIL.

### C-04 -- Positioning Leaks Identified

- **Weight**: essential
- **Category**: coverage
- **Text**: Any non-target persona who expresses confusion about whether the feature is meant for
  them (high usefulness or would-adopt despite being non-target, or explicit confusion in
  rationale) is flagged as a positioning leak.
- **Pass condition**: Output includes a positioning leaks section. If leaks exist they are named.
  If none exist, output explicitly states "no positioning leaks." Missing the section entirely
  = FAIL.

### C-05 -- Persona Tier Assignment Stated

- **Weight**: essential
- **Category**: format
- **Text**: Each persona is explicitly assigned a tier (primary, secondary, or non-target) before
  or alongside their scores, making the weighting auditable.
- **Pass condition**: Every persona entry includes a tier label. Tier labels absent from 3 or more
  personas = FAIL.

---

## Recommended Criteria

Output is materially better when these pass.

### C-06 -- Delight Signals Identified

- **Weight**: recommended
- **Category**: coverage
- **Text**: Any persona awarding a score of 5 on any dimension is flagged as a delight signal.
  Delight signals are grouped separately from blockers/leaks and interpreted for positioning or
  marketing value.
- **Pass condition**: Output includes a delight signals section (or explicitly states "no delight
  signals"). Delight signals present but not surfaced = FAIL on this criterion.

### C-07 -- Amendment Guidance Prioritizes Blockers Then Leaks

- **Weight**: recommended
- **Category**: behavior
- **Text**: The amend section sequences recommended actions: (1) resolve adoption blockers,
  (2) close positioning leaks, (3) amplify delight signals. This ordering is explicit or implied
  by section structure.
- **Pass condition**: Amend guidance exists and addresses blockers before leaks (or states there
  are none). Amend section absent, or leaks addressed before blockers = FAIL on this criterion.

### C-08 -- Per-Persona Rationale Provided

- **Weight**: recommended
- **Category**: depth
- **Text**: Each persona entry includes a brief rationale (1-3 sentences) explaining why they
  scored as they did, grounded in the persona's role, goals, or known pain points.
- **Pass condition**: At least 10 of 12 personas have non-trivial rationale (not just restating
  the score). Fewer than 10 with rationale = FAIL on this criterion.

---

## Aspirational Criteria

Raise the bar once essential and recommended are stable.

### C-09 -- Cross-Persona Pattern Synthesis

- **Weight**: aspirational
- **Category**: depth
- **Text**: The output identifies a cross-cutting pattern across persona scores -- e.g., a role
  cluster that consistently scores low on clarity, or a segment where usefulness/would-adopt
  diverge -- and names the implication for feature design or messaging.
- **Pass condition**: Output includes at least one named cross-persona pattern with an explicit
  implication stated. Generic observations ("scores vary") do not count.

### C-10 -- Amend-to-Score Projection

- **Weight**: aspirational
- **Category**: behavior
- **Text**: The amend section projects how resolving each blocker or leak would move the weighted
  aggregate score. Even a directional estimate ("resolving C-03 blocker likely lifts aggregate
  by ~0.3") qualifies.
- **Pass condition**: At least one blocker or leak has an associated score-impact estimate. If no
  blockers or leaks exist, this criterion is waived (auto-pass).

### C-11 -- Inline Blocker/Leak Flags at Point of Scoring

- **Weight**: aspirational
- **Category**: reliability
- **Text**: Adoption blockers and positioning leaks are flagged inline at the persona entry where
  they are first identified -- not only surfaced in a post-hoc section. Inline flags (e.g.,
  `[BLOCKER]`, `[LEAK]`) make it structurally impossible for a qualifying signal to be present
  in the scores but absent from the findings.
- **Pass condition**: Every persona whose scores qualify as a blocker (primary with would-adopt
  < 3) or leak (non-target with would-adopt >= 3) carries an inline marker adjacent to the
  offending score, in addition to appearing in the dedicated section. A qualifying persona
  appearing in the section but without an inline marker = PARTIAL. Two or more missing inline
  markers = FAIL on this criterion.
- **R1 source**: V-05 inline `[BLOCKER]`/`[LEAK]` flags during scoring outperformed V-03's
  mandatory DETECT phase for C-03/C-04 reliability.

### C-12 -- Hybrid Format: Structured Table Plus Per-Persona Prose

- **Weight**: aspirational
- **Category**: format
- **Text**: The output uses both a structured summary (table or scored list with all 12 personas,
  tier labels, and three numeric scores) and separate per-persona prose blocks with substantive
  rationale. Neither format alone satisfies this criterion. The table guarantees completeness and
  auditability; the prose guarantees depth that a single-sentence row cannot provide.
- **Pass condition**: Output contains (a) a summary structure covering all 12 personas with tier
  and three scores, AND (b) at least 10 of 12 personas with prose rationale of 2+ sentences
  beyond the scores. Output that uses only a table (no prose) or only prose (no summary table)
  = FAIL on this criterion.
- **R1 source**: V-02's table-first format achieved strongest completeness but created a
  rationale-depth trade-off (C-08 PARTIAL at 1-sentence cap). The hybrid resolves both.

### C-13 -- Causal Rationale: Feature Gap Named as Mechanism

- **Weight**: aspirational
- **Category**: depth
- **Text**: Rationale for each persona identifies a specific feature property, design gap, or
  workflow mismatch as the causal driver of the observed score -- not merely what the persona
  values in general. The framing is "the feature's [property] produced this reaction" rather
  than "this persona values [thing]." Causal rationale is more actionable than contextual
  rationale because it directly implicates the feature, not just the audience.
- **Pass condition**: At least 8 of 12 persona rationales contain a causal statement that names
  a feature element (a specific capability, gap, framing choice, or workflow step) as the
  reason for the score. Rationale that only describes the persona's role, preferences, or goals
  without tying back to a feature property = contextual, not causal, and does not count.
  Fewer than 8 causal rationales = FAIL on this criterion.
- **R1 source**: V-04's instruction "explain what about the feature produced these specific
  reactions from this specific person" outperformed V-03's "not a restatement of the score"
  instruction because it specifies the mechanism, not just the prohibition.

### C-14 -- Prose-First Scoring Order

- **Weight**: aspirational
- **Category**: reliability
- **Text**: Per-persona reasoning blocks -- including tier label, scores, inline flags, and
  rationale -- appear before the summary table in the output. The summary table is compiled from
  already-scored and already-flagged reasoning, making it a verified artifact rather than a
  preliminary scaffold. Prose-first ordering structurally co-locates each score with its inline
  flag in the same block, eliminating the phase-gap that table-first hybrids create between the
  scoring section and the flag section.
- **Pass condition**: The summary table (or equivalent scored list) appears after all per-persona
  prose blocks, not before them. A table that precedes any per-persona prose = FAIL. A table
  interleaved between persona blocks = PARTIAL.
- **R2 source**: V-05's prose-first ordering was the structural variable that resolved C-11
  PARTIAL in V-01 and V-04 (both table-first hybrids). In V-01/V-04, scores live in Phase 2
  and flags land in Phase 3 headers -- a structural phase gap that prose-first ordering
  eliminates by co-locating score and flag in the same block before advancing to the next persona.

### C-15 -- Flag Deferral Prohibition

- **Weight**: aspirational
- **Category**: reliability
- **Text**: No persona entry that qualifies for an inline flag may end without that flag applied.
  The output must not rely on a post-hoc section (DETECT phase, verification block, or summary
  pass) to catch flags that belong inline. The flag deferral failure mode is: score a primary
  persona Would-Adopt: 2, advance to the next persona, then surface the blocker in a later
  section. C-15 makes that sequence structurally impermissible.
- **Pass condition**: Every persona block that contains a qualifying score closes with its inline
  flag before the output advances to the next persona. An output where a qualifying persona block
  ends without its flag -- even if the flag appears later in a DETECT or summary section --
  = PARTIAL. Two or more deferred flags = FAIL on this criterion.
- **R2 source**: V-03's "Do not defer flags to a later section" prohibition is the strongest
  C-11 enforcement language in R2. Prohibiting the failure mode (deferral) outperforms only
  encouraging the success mode (inline placement), because a system that catches deferred flags
  post-hoc can still silently omit them if the catch phase is skipped or incomplete.

### C-16 -- Causal Precision: Sub-Feature Specificity

- **Weight**: aspirational
- **Category**: depth
- **Text**: Causal rationale names the feature property at sub-feature granularity: a specific
  capability, threshold, design decision, or workflow step -- not the feature generically. The
  distinction is between "the feature lacks support for X" (feature-level, C-13 passes) and
  "the feature's [specific capability/limit/design choice Y] is the mechanism that produced this
  score" (sub-feature level, C-16 passes). Sub-feature specificity makes the causal statement
  directly actionable as a design amendment target.
- **Pass condition**: At least 6 of 12 persona rationales name a sub-feature property (a named
  capability, a specific threshold or limit, a design decision, or a workflow step) as the causal
  mechanism -- not the feature generically or the persona's general preferences. Rationale that
  reaches only feature-level generality ("the feature doesn't support X") does not count toward
  this criterion even if it passes C-13. Fewer than 6 sub-feature-specific causal rationales
  = FAIL on this criterion.
- **R2 source**: V-02's worked anti-pattern C-13 example drove more precise causal framing than
  V-04's abstract instruction. The worked example showed what contextual framing looks like
  ("this persona values Y") alongside what causal framing requires ("the feature's Z produced
  this reaction"), driving specificity to the sub-feature level that abstract rules cannot enforce.

---

## Persona Stock Reference

| ID   | Name            | Role       |
|------|-----------------|------------|
| C-01 | Maria Chen      | Maker      |
| C-02 | James Okafor    | Builder    |
| C-03 | Priya Nair      | Strategist |
| C-04 | Tom Bergstrom   | Operator   |
| C-05 | Aisha Mensah    | Researcher |
| C-06 | Carlos Reyes    | Designer   |
| C-07 | Lin Wei         | Analyst    |
| C-08 | Sophie Dubois   | Manager    |
| C-09 | Raj Patel       | Advocate   |
| C-10 | Yuki Tanaka     | Evaluator  |
| C-11 | Elena Vasquez   | Buyer      |
| C-12 | Frank Hoffmann  | Regulator  |

Tier assignment (primary/secondary/non-target) is feature-specific and must be declared in the
skill run, not assumed from the stock list.

---

## Scoring Summary

| ID   | Criterion                              | Weight       | Category    | Added |
|------|----------------------------------------|--------------|-------------|-------|
| C-01 | All 12 personas present and scored     | essential    | correctness | v1    |
| C-02 | Weighted aggregate score computed      | essential    | correctness | v1    |
| C-03 | Adoption blockers identified           | essential    | correctness | v1    |
| C-04 | Positioning leaks identified           | essential    | coverage    | v1    |
| C-05 | Persona tier assignment stated         | essential    | format      | v1    |
| C-06 | Delight signals identified             | recommended  | coverage    | v1    |
| C-07 | Amendment guidance order correct       | recommended  | behavior    | v1    |
| C-08 | Per-persona rationale provided         | recommended  | depth       | v1    |
| C-09 | Cross-persona pattern synthesis        | aspirational | depth       | v1    |
| C-10 | Amend-to-score projection              | aspirational | behavior    | v1    |
| C-11 | Inline blocker/leak flags at scoring   | aspirational | reliability | v2    |
| C-12 | Hybrid table+prose format              | aspirational | format      | v2    |
| C-13 | Causal rationale: feature gap named    | aspirational | depth       | v2    |
| C-14 | Prose-first scoring order              | aspirational | reliability | v3    |
| C-15 | Flag deferral prohibition              | aspirational | reliability | v3    |
| C-16 | Causal precision: sub-feature specific | aspirational | depth       | v3    |
