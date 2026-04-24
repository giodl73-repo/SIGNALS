Written to `simulations/quest/rubrics/review-customers-rubric-v4-2026-03-14.md`.

---

**v4 changes summary:**

Three new aspirational criteria extracted from R3 patterns:

| ID | Criterion | Category | R3 source |
|----|-----------|----------|-----------|
| C-17 | Amendment specificity: sub-feature targets | behavior | V-02/V-05 pass C-16 in rationale but no criterion holds the amend section to matching granularity |
| C-18 | Cross-persona pattern at sub-feature resolution | depth | C-09 passes on named patterns that can stop at feature-level; R3's ceiling is a pattern that names a sub-feature property as the structural cause |
| C-19 | Three-tier causal chain traversal in blocker rationales | depth | Three-tier example (L1/L2/L3) is the necessary C-16 mechanism; at least one blocker must show all three levels traversable to prove chain completeness, not just terminological compliance |

**The three patterns extend the R3 ceiling in distinct directions:**

- **C-17** closes the scoring/amendment parity gap — C-16 requires sub-feature causal framing in rationale but the amend section has only C-07 (order) and C-10 (projection). C-17 requires each amendment recommendation to name the specific sub-feature property to target, making it directly assignable as a design decision without further decomposition.

- **C-18** propagates sub-feature resolution into the cross-persona synthesis. A pattern that names only "role cluster X scores low on clarity" passes C-09 but stops at feature-level framing. C-18 requires the pattern to name the sub-feature property that is the structural cause across the cluster — the highest-leverage location, since a single sub-feature cause that explains multiple personas is more actionable than N individual rationales pointing in different directions.

- **C-19** tests causal chain completeness vs. terminological compliance. An output can pass C-16 by learning to name sub-features without showing the chain that connects them to persona stakes. C-19 requires at least one blocker entry to contain all three levels (L1: persona context, L2: feature-level gap, L3: sub-feature mechanism) in traversable form. L1+L3 without L2 skips the bridge; L2+L3 without L1 names the mechanism without stakes.

**Totals:** 19 criteria, 11 aspirational (was 8), depth category gains two (now 6: C-08, C-09, C-13, C-16, C-18, C-19), behavior gains one (now 3: C-07, C-10, C-17).
egory gains C-18 and C-19 (now C-08, C-09, C-13, C-16,
C-18, C-19).

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

### C-17 -- Amendment Specificity: Sub-Feature Targets

- **Weight**: aspirational
- **Category**: behavior
- **Text**: The amend section names specific sub-feature properties as the amendment targets for
  each blocker and leak -- mirroring C-16's specificity requirement in the rationale section.
  The distinction is between "improve [feature] for [persona]" (generic, C-07 passes) and "add
  [specific capability/threshold/design decision Y] to address [persona ID]'s [specific friction
  point]" (sub-feature targeted, C-17 passes). Sub-feature amendment targeting makes each
  recommendation directly assignable to a design decision without further decomposition.
- **Pass condition**: Every blocker and every leak in the amend section is paired with an
  amendment recommendation that names a sub-feature property (specific capability, threshold,
  design decision, or workflow step) as the target. Generic amendments that name only the feature
  or the persona segment without a sub-feature target = PARTIAL per item. Two or more generic
  amendments when blockers or leaks exist = FAIL on this criterion. If no blockers or leaks
  exist, criterion is waived (auto-pass).
- **R3 source**: V-02 and V-05 both achieve C-16 sub-feature specificity in rationale but the
  amend section is not held to matching granularity by any existing criterion. C-17 closes the
  gap: the causal chain that drove the score must also drive the fix.

### C-18 -- Cross-Persona Pattern at Sub-Feature Resolution

- **Weight**: aspirational
- **Category**: depth
- **Text**: The cross-persona pattern identified under C-09 names a sub-feature property as the
  structural cause of the pattern -- not just the feature generically or the persona segment
  affected. The distinction is between "role cluster X scores low on clarity" (C-09 passes) and
  "role cluster X scores low on clarity because the feature's [specific design decision/workflow
  step Y] creates friction for personas whose workflow requires [Z]" (C-18 passes). A sub-feature
  cause is directly actionable as a single design intervention that would lift multiple personas
  simultaneously.
- **Pass condition**: At least one named cross-persona pattern contains a causal statement that
  names a sub-feature property as the mechanism driving the pattern across the cluster. A pattern
  that names only the affected segment, the score dimension, or the feature generically -- without
  a sub-feature cause -- does not count. If C-09 FAIL, C-18 also FAIL. If C-09 passes with a
  pattern that reaches sub-feature resolution, C-18 PASS.
- **R3 source**: R3's ceiling is C-16 compliance in per-persona rationale. C-18 requires the
  same sub-feature causal resolution to appear in the cross-persona synthesis, which is the
  highest-leverage location: a single sub-feature cause that explains a cluster's scores is a
  more actionable finding than 12 individual sub-feature rationales pointing in different
  directions.

### C-19 -- Three-Tier Causal Chain Traversal in Blocker Rationales

- **Weight**: aspirational
- **Category**: depth
- **Text**: At least one adoption blocker rationale explicitly traverses all three causal levels:
  L1 (persona context -- the goal, workflow, or constraint that makes this persona care), L2
  (feature-level gap -- the feature does not support X), and L3 (sub-feature mechanism -- the
  feature's specific [capability/threshold/design decision Y] is why). The three levels may be
  implicit in prose structure or explicitly labeled, but all three must be identifiable in a
  single blocker entry. L1 establishes stakes; L2 names the gap; L3 names the mechanism. An
  entry that shows L1 and L3 without L2 skips the feature-level bridge and is not traversable.
  An entry that shows L2 and L3 without L1 names the mechanism but not why it matters to this
  persona.
- **Pass condition**: At least one adoption blocker rationale contains identifiable L1, L2, and
  L3 statements in traversable form (all three present in the same entry). If no adoption
  blockers exist, criterion is waived (auto-pass). An output where all blocker rationales contain
  L3 sub-feature names but omit L1 or L2 = FAIL (sub-feature name alone is not a causal chain).
  Fewer than one complete three-tier traversal = FAIL on this criterion.
- **R3 source**: The three-tier worked example (L1/L2/L3 as visually distinct named categories)
  is the necessary mechanism for C-16 compliance -- abstract rules plateau at L2 (feature-level).
  C-19 tests whether the model understood the chain or just learned to name sub-features. If the
  chain is present in at least one blocker, the output demonstrates causal chain completeness,
  not just terminological compliance.

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

| ID   | Criterion                                       | Weight       | Category    | Added |
|------|-------------------------------------------------|--------------|-------------|-------|
| C-01 | All 12 personas present and scored              | essential    | correctness | v1    |
| C-02 | Weighted aggregate score computed               | essential    | correctness | v1    |
| C-03 | Adoption blockers identified                    | essential    | correctness | v1    |
| C-04 | Positioning leaks identified                    | essential    | coverage    | v1    |
| C-05 | Persona tier assignment stated                  | essential    | format      | v1    |
| C-06 | Delight signals identified                      | recommended  | coverage    | v1    |
| C-07 | Amendment guidance order correct                | recommended  | behavior    | v1    |
| C-08 | Per-persona rationale provided                  | recommended  | depth       | v1    |
| C-09 | Cross-persona pattern synthesis                 | aspirational | depth       | v1    |
| C-10 | Amend-to-score projection                       | aspirational | behavior    | v1    |
| C-11 | Inline blocker/leak flags at scoring            | aspirational | reliability | v2    |
| C-12 | Hybrid table+prose format                       | aspirational | format      | v2    |
| C-13 | Causal rationale: feature gap named             | aspirational | depth       | v2    |
| C-14 | Prose-first scoring order                       | aspirational | reliability | v3    |
| C-15 | Flag deferral prohibition                       | aspirational | reliability | v3    |
| C-16 | Causal precision: sub-feature specific          | aspirational | depth       | v3    |
| C-17 | Amendment specificity: sub-feature targets      | aspirational | behavior    | v4    |
| C-18 | Cross-persona pattern at sub-feature resolution | aspirational | depth       | v4    |
| C-19 | Three-tier causal chain traversal in blockers   | aspirational | depth       | v4    |
