# draft-brainstorm Rubric -- v19

Evaluates the quality of a `draft-brainstorm` prompt against the signal plugin's
golden standard for AI-first idea generation.

---

## Essential Criteria (weight: 60%)

All five must pass. Any essential fail blocks golden regardless of score.

### C-01 -- Volume

- **Category**: correctness
- **Weight**: essential
- **Text**: The output contains between 20 and 40 distinct idea candidates
  (inclusive).
- **Pass condition**: Count total distinct idea entries. Pass if count >= 20 and
  <= 40. Fail if fewer than 20 (insufficient exploration) or more than 40
  (undisciplined pool).

### C-02 -- Idea Anatomy

- **Category**: correctness
- **Weight**: essential
- **Text**: Every idea has all four required fields: name, one-line pitch,
  category, and rationale.
- **Pass condition**: Sample at least 5 ideas (including first, last, and
  middle). Every sampled idea has all four fields present and non-empty. If any
  sampled idea is missing a field, fail. If all four fields are consistently
  present, pass.

### C-03 -- Top-5 Marker

- **Category**: correctness
- **Weight**: essential
- **Text**: Exactly 5 ideas are marked with `**` to indicate immediate viability.
- **Pass condition**: Count ideas marked with `**` (double asterisk, typically as
  a bold marker or inline `**name**` or `**` suffix). Pass if exactly 5. Fail if
  0, fewer than 5, or more than 5.

### C-04 -- Inertia Check

- **Category**: coverage
- **Weight**: essential
- **Text**: A "do nothing" candidate is present that describes the status quo
  path.
- **Pass condition**: At least one idea explicitly represents the
  inertia/status-quo option (e.g., named "Do Nothing", "Status Quo", "No
  Change", or equivalent). The rationale must describe what the current state
  looks like, not just say "do nothing." Pass if present with rationale; fail if
  absent or present but unnamed/undescribed.

### C-05 -- AMEND Section

- **Category**: correctness
- **Weight**: essential
- **Text**: The output contains an AMEND section with exactly 3 specific
  adjustments that would shift the pool.
- **Pass condition**: A labeled AMEND section exists (heading, label, or prefix
  "AMEND:"). It contains exactly 3 adjustment items. Each adjustment names a
  direction of change (e.g., "more ambitious," "conservative," "different
  audience") AND states what would change in the pool. Pass if all three are
  present and directional; fail if section is absent, has fewer than 3, or
  adjustments are vague.

---

## Recommended Criteria (weight: 30%)

Output is better with these. Missing one lowers the score but does not block
golden.

### C-06 -- Category Grouping

- **Category**: format
- **Weight**: recommended
- **Text**: Ideas are organized under explicit category headers, not presented as
  a flat list with category as a field only.
- **Pass condition**: The document uses visible grouping (e.g., markdown headers
  `## Category Name`, bold category labels, or clearly separated sections) so a
  reader can scan by category. A flat numbered list where category is only a
  field attribute fails. Pass if at least 3 distinct category groups are visually
  separated.

### C-07 -- Rationale Specificity

- **Category**: depth
- **Weight**: recommended
- **Text**: Rationales are specific to the topic at hand, not generic reasoning
  that could apply to any brainstorm.
- **Pass condition**: Sample 5 rationales. Each must reference the topic by name,
  a specific user need, constraint, or opportunity tied to the topic. Generic
  rationales like "this is a good idea because it provides value" fail. Pass if
  4 of 5 sampled rationales are topic-specific.

### C-08 -- Category Diversity

- **Category**: coverage
- **Weight**: recommended
- **Text**: Ideas span at least 4 distinct categories, ensuring the pool isn't
  clustered in one approach.
- **Pass condition**: Count distinct category labels across all ideas. Pass if
  at least 4 distinct categories are present. Fail if 3 or fewer categories
  cover the entire pool (too homogeneous).

---

## Aspirational Criteria (bonus: up to +10 pts)

Bonus points awarded for patterns that distinguish excellent outputs from merely
correct ones.

### C-09 -- AMEND Actionability

- **Category**: depth
- **Weight**: aspirational (5 pts)
- **Text**: Each AMEND item states a specific direction AND explains what kind of
  candidates would appear or disappear from the pool -- not just "add more
  technical ideas" but "add more technical ideas: candidates like X and Y would
  appear, Z-type candidates would drop."
- **Pass condition**: All 3 AMEND items are directional AND pool-predictive.
  Fail if any item names a direction without describing the resulting pool
  composition change.

### C-10 -- Top-5 Defensibility

- **Category**: depth
- **Weight**: aspirational (5 pts)
- **Text**: The selection of the top 5 marked ideas is defensible against the
  full pool -- a reader can see why these 5 were selected over the next-best
  candidates.
- **Pass condition**: The marked ideas are meaningfully distinct from each other
  (not 5 variations of one approach) AND at least one non-obvious candidate is
  included (not all safe/obvious picks). Pass if selection appears deliberate and
  diverse. Fail if the top-5 are all from the same category cluster or are
  trivially obvious as a set.

---

## Extended Aspirational Criteria -- R2 (bonus: up to +10 pts)

Patterns extracted from R1 excellence signals. Each worth 2.5 bonus points.

### C-11 -- Sequential-Default Guard

- **Category**: anti-pattern
- **Weight**: extended asp (R2) (2.5 pts)
- **Signal from**: V-01 R1 -- sequential candidate generation (ideas numbered
  1-N in strict order without per-category grouping) introduces a sequential
  default where the model front-loads the most obvious candidates and exhausts
  obvious space before generating surprising ones; guard against this by
  requiring per-category generation rather than a single ordered sequence
- **Text**: The prompt guards against sequential generation default by requiring
  ideas to be generated within category buckets (not as a single numbered
  sequence), so the model explores each category before moving to the next rather
  than defaulting to the most obvious candidates first.
- **Pass condition**: The prompt explicitly instructs generating ideas within
  category sections (not as a flat numbered list), or includes a statement that
  prevents purely sequential generation. A prompt that allows a single flat
  numbered list without category structure fails. Pass if per-category generation
  is required or a sequential-default guard is present.

### C-12 -- Amendment Re-Runnability Bar

- **Category**: depth
- **Weight**: extended asp (R2) (2.5 pts)
- **Signal from**: V-02 R1 -- AMEND items that name only a direction without
  stating the re-runnability bar (running the prompt again with only this item
  as guidance must produce a noticeably different pool) allow directional
  descriptions that satisfy C-09 in letter but not in spirit -- the item sounds
  actionable but doesn't commit to a verifiable pool-shift
- **Text**: The AMEND section includes the re-runnability bar: each item must be
  specific enough that re-running the brainstorm with only that item as guidance
  would produce a noticeably different pool of candidates.
- **Pass condition**: The prompt states or implies that each AMEND direction must
  be actionable as a standalone re-run instruction. A prompt that requires
  directions but doesn't state what "different" means fails. Pass if the
  re-runnability standard is stated (e.g., "specific enough that re-running with
  only this directive produces a different pool").

### C-13 -- Category Dimension Taxonomy

- **Category**: coverage
- **Weight**: extended asp (R2) (2.5 pts)
- **Signal from**: V-03 R1 -- prompts that use a named taxonomy of category
  types (e.g., scope, timing, integration approach, audience, build vs. buy,
  status quo) produce more systematically diverse pools than prompts that leave
  category selection to the model
- **Text**: The prompt provides a named taxonomy of category dimensions that
  ideas should span -- not just "organize by category" but naming the types of
  dimensions (e.g., scope, timing, integration, audience, build vs. buy, status
  quo) so the model has a structured frame for generating diverse candidates.
- **Pass condition**: The prompt names at least 4 specific category dimension
  types. A generic instruction to "organize by category" fails. Pass if the
  prompt provides a named list of category dimensions the pool should cover.

### C-14 -- Inertia-First Framing Paragraph

- **Category**: depth
- **Weight**: extended asp (R2) (2.5 pts)
- **Signal from**: V-04 R1 -- placing the Do Nothing baseline after the idea
  pool allows the model to generate alternatives first and treat inertia as an
  afterthought; requiring an inertia-first framing paragraph before the idea pool
  anchors all alternatives against the status quo trajectory
- **Text**: Before generating any ideas, the prompt requires a framing paragraph
  that names the inertia option and describes what the status quo trajectory
  looks like -- anchoring the entire alternative pool against the baseline state.
- **Pass condition**: The prompt requires a framing statement (paragraph, section,
  or block) before the idea pool that names and describes the Do Nothing / status
  quo trajectory. A prompt that integrates Do Nothing only as one of the ideas
  in the pool fails -- the framing must precede the pool. Pass if a pre-pool
  inertia anchor is required.

---

## Round-3 Aspirational Criteria (bonus: up to +10 pts)

Patterns extracted from R2 excellence signals. Each worth 2.5 bonus points.

### C-15 -- Structural Spine Guarantee

- **Category**: coverage
- **Weight**: r3 aspirational (2.5 pts)
- **Signal from**: V-01 R2 -- prompts that name the required output sections
  (dimensions) as mandatory structural elements (not optional organization
  hints) guarantee that the output contains one labeled section per dimension
  regardless of how many ideas fall under each dimension
- **Text**: The prompt names each required output section (dimension) as a
  mandatory structural slot that must appear in the final artifact regardless of
  idea count -- closing the loophole where a model collapses sparse dimensions
  into other sections or omits them entirely.
- **Pass condition**: The prompt explicitly states that each named section is
  mandatory and cannot be omitted or collapsed. A list of suggested categories
  fails -- the structural guarantee must name the sections as required output
  structure. Pass if the prompt states that every named section must appear in
  the output.

### C-16 -- Generation-Phase Sequential Guard

- **Category**: anti-pattern
- **Weight**: r3 aspirational (2.5 pts)
- **Signal from**: V-02 R2 -- even with category-based generation (C-11), a
  model can still default to sequential ordering within a generation phase,
  front-loading obvious candidates; an explicit guard stating that sequential
  default introduces bias (earlier positions bias selection) closes this
  within-phase sequential gap
- **Text**: The prompt includes an explicit instruction that prevents placing
  selection markers (`**`) during the generation phase -- naming that marking
  while generating introduces sequential bias and must be deferred until the
  entire pool is written.
- **Pass condition**: The prompt explicitly prohibits placing `**` markers
  (or equivalent selection indicators) during the pool generation phase, stating
  that selection must be deferred until the full pool is written. A generic
  instruction to "generate ideas without bias" fails -- the prohibition must name
  the sequential-bias mechanism or the forbidden action (marking during
  generation). Pass if the generation-phase marking prohibition is present.

### C-17 -- Peer-Comparison Defensibility Test

- **Category**: depth
- **Weight**: r3 aspirational (2.5 pts)
- **Signal from**: V-03 R2 -- requiring a peer-comparison test (for each marked
  idea, name the best alternative not marked and explain why the marked idea
  wins) produces selections that are defensible against the full pool, not just
  internally consistent
- **Text**: The prompt requires a peer-comparison test: for each of the 5 marked
  ideas, name the strongest alternative candidate not selected and explain why
  the marked idea was preferred -- creating a per-selection accountability
  mechanism against the full pool.
- **Pass condition**: The prompt requires a peer-comparison step that names a
  specific peer (the best non-selected alternative) for each marked idea and
  requires a stated reason for the selection preference. A prompt that requires
  justification without naming a peer fails -- the comparison must be against
  a specific named alternative. Pass if the peer-comparison structure is present
  for all 5 marked ideas.

### C-18 -- Self-Review Phase Integration

- **Category**: depth
- **Weight**: r3 aspirational (2.5 pts)
- **Signal from**: V-04 R2 -- a dedicated self-review phase (separate from
  generation) that checks the pool against specific criteria (coverage, bias,
  amend quality, selection defensibility) produces higher-quality outputs than
  a single-pass generation-and-selection sequence
- **Text**: The prompt structures a dedicated self-review phase that is separate
  from the generation phase -- checking the pool against named quality criteria
  before advancing to selection -- rather than combining generation, review, and
  selection into a single flow.
- **Pass condition**: The prompt contains a named self-review phase (Check,
  Review, Audit, or equivalent) that is separate from the generation phase and
  specifies named criteria to verify before advancing to selection. A single-pass
  prompt without a dedicated review phase fails. Pass if a distinct review phase
  is present with at least 2 named check criteria.

---

## Round-4 Aspirational Criteria (bonus: up to +5 pts)

Patterns extracted from R3 excellence signals. Each worth 2.5 bonus points.
C-19 sharpens C-17: C-17 is the floor (peer-comparison test present -- for each
marked idea, name the strongest alternative and explain preference); C-19 is the
ceiling (the peer-comparison test is stated as an imperative output form -- "I
chose [Candidate] over [Peer] because ___" -- requiring the model to produce a
sentence-completion artifact, not just perform a comparison). C-20 sharpens C-17:
C-20 is a sibling sharpening that adds a consequence clause (the comparison must
have stakes -- if the comparison sentence cannot be completed, the marked
candidate must be replaced by the named peer).

### C-19 -- Peer-Test Imperative Form

- **Category**: anti-pattern
- **Weight**: r4 aspirational (2.5 pts)
- **Signal from**: V-01 R3 -- the peer-comparison test (C-17) can be stated as
  a descriptive requirement ("name the best alternative and explain why you
  prefer the marked idea") or as an imperative output form ("write the sentence:
  'I chose [Candidate] over [Peer] because ___'"); the imperative form requires
  the model to produce a specific sentence structure, closing the loophole where
  a model performs the comparison mentally but produces only a summary rather than
  the materialized comparison sentence
- **Text**: The peer-comparison test (C-17) is stated as an imperative sentence
  completion form -- "I chose [Candidate] over [Peer] because ___" -- requiring
  the model to produce the comparison as a materialized output artifact (a
  sentence the model must write), not as a reasoning step the model may perform
  internally.
- **Pass condition**: The prompt requires the peer-comparison as a sentence of
  the form "I chose [X] over [Y] because ___" or equivalent explicit sentence
  structure where the model must complete the sentence with the comparison
  reason. A prompt that requires comparison reasoning without specifying the
  output sentence structure fails -- the materialized output form must be present.
  Pass if the completion sentence structure appears in the prompt as the required
  output format for each comparison.
- **Distinguishes from C-17**: C-17 passes when a peer-comparison step is present
  that names a specific alternative and requires a stated reason. C-19 passes
  only when the comparison is stated as an imperative sentence-completion form
  that requires the model to produce the specific sentence structure as an output
  artifact, not just reason through the comparison.

### C-20 -- Peer-Test Consequence Clause

- **Category**: depth
- **Weight**: r4 aspirational (2.5 pts)
- **Signal from**: V-02 R3 -- a peer-comparison test (C-17) without a
  consequence clause allows the model to produce a weak comparison sentence that
  nominally satisfies the requirement but keeps the original selection; adding a
  consequence clause (if the comparison sentence cannot be completed with a
  specific reason, the marked candidate must be replaced by the named peer)
  gives the comparison teeth -- the model must produce a completable sentence or
  accept the replacement consequence
- **Text**: The peer-comparison test includes a consequence clause: if the
  comparison sentence cannot be completed with a specific, defensible reason,
  the marked idea must be replaced by the named peer candidate -- giving the test
  an actionable consequence rather than allowing a weak completion to stand.
- **Pass condition**: The prompt states a consequence clause that specifies what
  must happen if the comparison sentence cannot be completed defensibly (e.g.,
  "if you cannot complete this sentence with a specific reason, replace this
  candidate with the named peer"). A peer-comparison requirement without a
  consequence clause (C-17 only) fails -- the stakes of failing the test must
  be named. Pass if the replacement consequence is stated.
- **Distinguishes from C-17**: C-17 passes when a peer-comparison step is present.
  C-20 passes only when the comparison includes a consequence clause that names
  the required action (replacement with the named peer) when the comparison
  sentence cannot be completed defensibly.

---

## Round-5 Aspirational Criteria (bonus: up to +5 pts)

Patterns extracted from R4 excellence signals. Each worth 2.5 bonus points.
C-21 sharpens C-19: C-19 is the floor (peer-comparison test stated as imperative
sentence-completion form); C-21 is the ceiling (all five completion sentences
must be written as a batch before the selection phase advances -- preventing
the model from marking and advancing one at a time and accumulating sequential
confirmation bias). C-22 sharpens C-20: C-20 is the floor (consequence clause
present -- if the comparison fails, the named peer replaces the candidate); C-22
is the ceiling (the replacement source is fixed to the peer named in this
comparison row, not a replacement selected after reconsidering -- closing the
loophole where a model accepts the replacement obligation in principle but
substitutes a different, more favorable candidate).

### C-21 -- Peer-Test Batch-Completion Gate

- **Category**: anti-pattern
- **Weight**: r5 aspirational (2.5 pts)
- **Signal from**: V-01 R4 -- producing peer-comparison sentences one at a time
  (write sentence 1, evaluate, advance; write sentence 2, evaluate, advance)
  allows sequential confirmation bias to accumulate across comparisons; requiring
  all five sentences to be written as a batch before any evaluation closes this
  gap -- the model cannot advance to selection until all five completion sentences
  exist in the output
- **Text**: The peer-comparison phase requires all five "I chose [X] over [Y]
  because ___" sentences to be written as a complete batch before any of them
  are evaluated or before the selection phase may advance -- preventing
  one-at-a-time sequential evaluation that accumulates confirmation bias.
- **Pass condition**: The prompt requires all five completion sentences to be
  written before evaluation begins or before selection phase advance (e.g.,
  "write all five 'I chose ... because ___' sentences before evaluating any of
  them"). A prompt that allows or implies one-at-a-time comparison-and-advance
  fails. Pass if the batch-completion requirement is explicitly stated.
- **Distinguishes from C-19**: C-19 passes when the comparison is stated as an
  imperative sentence-completion form for each of the 5 marked ideas. C-21
  passes only when all five sentences must be written as a batch before phase
  advance -- the sequencing constraint closes the one-at-a-time loophole C-19
  leaves open.

### C-22 -- Consequence Replacement Source

- **Category**: depth
- **Weight**: r5 aspirational (2.5 pts)
- **Signal from**: V-02 R4 -- the consequence clause (C-20) names the replacement
  obligation but not the replacement source; adding "the replacement must come
  from the named peer in this comparison row, not an alternative selected after
  reconsidering" closes the loophole where a model accepts the swap obligation
  in principle but substitutes a different, more favorable candidate drawn from
  re-examination rather than from the comparison row
- **Text**: The consequence clause (C-20) specifies that the replacement source
  is fixed to the peer named in the comparison row -- not a candidate selected
  after reconsidering the pool -- closing the loophole where a model fulfills
  the replacement obligation with a substitute of its own choosing.
- **Pass condition**: The prompt states that the replacement source is the specific
  peer named in the comparison (e.g., "the replacement must be the peer named in
  this row, not an alternative candidate selected after reconsidering"). A
  consequence clause without a fixed source specification (C-20 only) fails --
  the source constraint must be explicit. Pass if the replacement is fixed to the
  named peer.
- **Distinguishes from C-20**: C-20 passes when a consequence clause naming the
  replacement obligation is present. C-22 passes only when the clause additionally
  specifies that the replacement source is the named peer from the comparison row,
  not a post-reconsideration substitute.

---

## Round-6 Aspirational Criteria (bonus: up to +5 pts)

Patterns extracted from R5 excellence signals. Each worth 2.5 bonus points.
C-23 sharpens C-21: C-21 is the floor (all five completions written as a batch
before phase advance); C-23 is the ceiling (the gate names the forbidden output
action, not just the required write order). C-24 sharpens C-22: C-22 is the
floor (replacement source fixed to the named peer); C-24 is the ceiling (the
post-comparison rationalization escape route is explicitly closed).

### C-23 -- Selection-Phase Marking Prohibition

- **Category**: anti-pattern
- **Weight**: r6 aspirational (2.5 pts)
- **Signal from**: V-01 R5 C-21 PASS ("Phase 3 is gated by batch completion:
  **do not place any `**` marks anywhere until all five Check B sentences appear
  in your output**" -- names the forbidden action explicitly, not just the
  required sequence; closes the loophole where a model satisfies the write-order
  requirement but begins marking mid-batch because no prohibition on marks was
  stated)
- **Text**: The batch-completion gate (C-21) is stated as an explicit prohibition
  on placing selection markers (`**`) during the batch phase -- naming what the
  model cannot do, not only specifying what must happen first.
- **Pass condition**: The prompt includes an explicit anti-marking instruction
  scoped to the batch phase (e.g., "do not place any `**` marks until all five
  sentences are written" or "no selection marks are permitted before batch
  completion"). A sequencing requirement alone ("write all five before marking")
  fails -- the prohibition must name the marking action as the forbidden
  behavior. Pass if the gate is framed as a marking prohibition, not only as a
  write-order constraint.
- **Distinguishes from C-21**: C-21 passes when a batch-write sequencing
  constraint is present (all completions before selection phase advance). C-23
  passes only when the gate explicitly prohibits placing marks as the named
  forbidden action -- the prohibition targets the output action, not just the
  sequence.

### C-24 -- Post-Comparison Rationalization Block

- **Category**: anti-pattern
- **Weight**: r6 aspirational (2.5 pts)
- **Signal from**: V-02 R5 C-22 PASS ("**Do not revise the marked idea's
  rationale to manufacture a distinction**... the peer from this check is the only
  permissible replacement source" -- explicitly closes the escape route where a
  model accepts the swap obligation in principle but rewrites the marked idea's
  justification post-comparison to make the distinction hold and avoid the
  replacement)
- **Text**: The consequence clause (C-22) includes an explicit prohibition on
  revising the marked idea's rationale or reopening the comparison after the test
  has been applied -- closing the escape route where a model manufactures a
  post-hoc distinction to avoid the replacement obligation.
- **Pass condition**: The prompt explicitly prohibits rationale revision or
  post-comparison reinterpretation to escape the swap (e.g., "do not revise the
  rationale to manufacture a distinction" or "once the comparison is applied, no
  re-examination of the candidate is permitted -- the peer from this check is the
  only permissible replacement source"). A replacement mandate with fixed source
  (C-22) fails -- the rationalization escape route must also be named and closed.
  Pass if the prompt explicitly prohibits using rationale revision as a mechanism
  to avoid a mandated swap.
- **Distinguishes from C-22**: C-22 passes when the replacement source is fixed
  to the named peer. C-24 passes only when the prompt also explicitly closes the
  rationalization escape -- the model cannot rewrite the original rationale
  post-comparison to manufacture a distinction that makes the swap unnecessary.

---

## Round-7 Aspirational Criteria (bonus: up to +5 pts)

Patterns extracted from R6 excellence signals. Each worth 2.5 bonus points.
C-25 sharpens C-23: C-23 is the floor (marking prohibition present as a prose
instruction); C-25 is the ceiling (the prohibition is encoded as a structural
output column that cannot be populated until the batch is architecturally
complete -- compliance is mechanical, not instructional). C-26 sharpens C-12:
C-12 is the floor (re-invocability bar stated); C-26 is the ceiling (the
directive is required to shift which candidate ideas appear, not merely how
existing ideas are framed or labeled).

### C-25 -- Marking-Gate Schema Lock

- **Category**: anti-pattern
- **Weight**: r7 aspirational (2.5 pts)
- **Signal from**: V-04 R6 C-23 PASS (Registry table encodes the peer comparison
  as a named output column; the `**YES**` selection-mark column physically
  cannot be populated until all batch rows are present -- the gate is a structural
  column-null constraint, not a prose prohibition the model must choose to respect)
- **Text**: The marking prohibition (C-23) is implemented as a structural output
  constraint -- a named column or schema slot for selection marks that is gated
  by the presence of all batch rows -- making compliance architectural rather than
  reliant on the model honoring a prose instruction.
- **Pass condition**: The prompt encodes the peer-comparison output as a named
  structural slot (e.g., a registry table column, a numbered schema field, or a
  labeled output section) AND specifies that the selection-mark slot cannot be
  populated until all comparison slots in the batch are filled. A prose
  prohibition on marks during the batch phase (C-23) does not satisfy this
  criterion -- the gate must be a property of the output schema, not a behavioral
  instruction. Pass if the marking action is gated by a structural column-null or
  slot-absent condition, not by a named prohibition alone.
- **Distinguishes from C-23**: C-23 passes when the prompt explicitly prohibits
  placing marks during the batch phase as a named forbidden action. C-25 passes
  only when the prohibition is encoded as a schema-level gate -- the mark column
  or slot cannot exist until all batch entries are structurally present.

### C-26 -- AMEND Pool-Composition Constraint

- **Category**: depth
- **Weight**: r7 aspirational (2.5 pts)
- **Signal from**: V-05 R6 C-09 PASS ("different candidate distribution, not
  different labels" -- explicitly requires AMEND items to shift which ideas
  appear in the pool, closing the loophole where a model satisfies C-12's
  re-invocability bar by naming directives that change category framing, emphasis,
  or labels without producing a materially different set of candidate ideas)
- **Text**: The re-invocability bar (C-12) is supplemented with an explicit
  pool-composition constraint -- AMEND items must shift which candidate ideas
  would appear, not merely how the same ideas are grouped, named, or emphasized.
- **Pass condition**: The prompt explicitly states that AMEND directives must
  produce a different candidate distribution (e.g., "different ideas appear, not
  just different labels" or "re-running with this directive must surface candidates
  that would not have appeared in the original pool"). A re-invocability
  requirement alone (C-12) does not pass -- a directive that changes category
  taxonomy or emphasis framing can satisfy C-12's bar while leaving the underlying
  candidate set unchanged. Pass if the prompt names the distribution-shift test
  as the criterion for a valid AMEND item.
- **Distinguishes from C-12**: C-12 passes when the re-invocability bar is stated
  (a reader can re-run and get a noticeably different pool). C-26 passes only when
  the prompt specifies that "different" means different candidate ideas, not
  different presentation of the same ideas -- closing the label-shift loophole
  that C-12 leaves open.

---

## Round-8 Aspirational Criteria (bonus: up to +5 pts)

Patterns extracted from R7 excellence signals. Each worth 2.5 bonus points.
C-27 sharpens C-25: C-25 is the floor (schema lock present); C-27 is the ceiling
(the schema gate is explicitly coupled to a phase-advance condition -- the gate
names which downstream phase cannot begin and what schema state must hold before
it may). C-28 sharpens C-24: C-24 is the floor (rationalization escape route
prohibited); C-28 is the ceiling (the rationalization impulse is inverted into a
positive trigger signal -- the desire to edit confirms the replacement obligation
applies, converting an exit route into enforcement evidence).

### C-27 -- Schema-Gate Phase-Advance Coupling

- **Category**: anti-pattern
- **Weight**: r8 aspirational (2.5 pts)
- **Signal from**: V-05 R7 C-25 PASS ("Layer 4 may begin only when all 5 rows
  exist and Selected? is blank across all rows" -- the schema null constraint is
  not stated as an abstract column property; it is explicitly coupled to a named
  downstream phase, stating which phase is blocked and what schema state must hold
  before that phase may begin; the gate is both structural and phase-specific)
- **Text**: The schema lock (C-25) is explicitly coupled to a phase-advance
  condition -- the prompt names the downstream phase that cannot begin and
  specifies the schema state that must hold before that phase is permitted to
  start.
- **Pass condition**: The prompt contains a phase-advance lock that names both
  (a) the phase that is blocked (e.g., "Layer 4", "Phase 3", "Step 5", "the
  selection step") and (b) the required schema state (e.g., "all 5 rows exist
  and Selected? is blank across all rows"). A structural null constraint alone
  (C-25) does not satisfy this criterion -- the schema gate must be expressed as
  a gating condition on a named phase, not merely as a column property. Pass if
  both the blocked phase and the required schema state are named in a single
  coupled condition.
- **Distinguishes from C-25**: C-25 passes when the selection-mark slot is gated
  by a structural column-null condition. C-27 passes only when that gate is
  additionally coupled to a named phase-advance condition -- specifying which phase
  cannot begin until the schema constraint is satisfied, making the gate both
  structural and temporally scoped.

### C-28 -- Rationalization-Impulse Trigger Inversion

- **Category**: anti-pattern
- **Weight**: r8 aspirational (2.5 pts)
- **Signal from**: V-05 R7 note ("If you want to edit the rationale, treat that
  impulse as confirmation that the replacement obligation applies" -- rather than
  merely prohibiting rationale revision (C-24), this formulation inverts the
  cognitive escape route: the desire to revise is itself named as positive
  evidence that the replacement constraint is in force; the exit impulse becomes
  the enforcement trigger)
- **Text**: The rationalization block (C-24) is strengthened by explicitly naming
  the impulse to revise the rationale as a trigger signal confirming the
  replacement obligation -- converting the escape-route impulse into enforcement
  evidence rather than merely closing the door.
- **Pass condition**: The prompt contains an inversion clause that names the
  desire or impulse to edit/revise the rationale as a confirmation signal (e.g.,
  "if you want to edit the rationale, treat that impulse as confirmation that the
  replacement obligation applies" or "the urge to revise is evidence the swap is
  mandatory, not permission to reopen the comparison"). A prohibition on revision
  alone (C-24) fails -- the inversion must be present: the prompt must explicitly
  connect the revision impulse to confirmation of the obligation, not merely
  prohibit acting on it. Pass if the revision impulse is named as a positive
  enforcement trigger, not only as a forbidden action.
- **Distinguishes from C-24**: C-24 passes when the prompt explicitly prohibits
  rationale revision to avoid the swap. C-28 passes only when the prompt inverts
  that impulse -- naming the desire to revise as the signal that the replacement
  obligation is active, closing not just the door but the reasoning path that
  leads to the door.

---

## Round-9 Aspirational Criteria (bonus: up to +5 pts)

Patterns extracted from R8 excellence signals. Each worth 2.5 bonus points.
C-29 sharpens C-27: C-27 is the floor (schema gate coupled to a named phase-advance
condition); C-29 is the ceiling (the phase-advance gate is restated at the entry
point of the phase it guards, creating a dual-anchor that the model encounters at
both schema definition and phase transition -- the gate cannot be read-and-forgotten).
C-30 sharpens C-28: C-28 is the floor (rationalization impulse inverted as a
confirmation trigger); C-30 is the ceiling (the inversion names the specific causal
mechanism that produces the revision desire -- the inability to complete the
comparison sentence -- tightening the trigger from any revision impulse to the exact
cognitive state that reveals comparison failure).

### C-29 -- Phase-Gate Entry-Point Restatement

- **Category**: anti-pattern
- **Weight**: r9 aspirational (2.5 pts)
- **Signal from**: V-05 R8 C-27 PASS ("Only after both Layer 3 gate conditions
  are satisfied (all 5 Registry rows written AND Selected? blank across all rows)"
  stated in Layer 4 itself -- the gate is declared twice: once at the Registry
  column definition and once at the entry of the phase it guards; a model
  beginning Layer 4 encounters the gate condition at the transition point, not
  only at the schema description written earlier in the prompt)
- **Text**: The phase-advance gate (C-27) is restated at the entry point of the
  phase it guards -- appearing both at the schema definition and as a pre-condition
  at the gated phase's opening -- so that the constraint is encountered at the
  moment of transition, not only during schema setup.
- **Pass condition**: The prompt contains two anchors for the phase-advance gate:
  (a) the gate stated at the schema level (column definition, Registry spec, or
  equivalent structural description) and (b) the gate restated as a pre-condition
  at the gated phase's opening (e.g., "Only after both preconditions hold: ...
  may [Phase N] begin" appearing as the first instruction of that phase). A single
  statement of the gate at schema definition alone (C-27) does not satisfy this
  criterion -- the restatement at phase entry must be present. Pass if both
  anchors are present: schema-level gate and phase-entry pre-condition.
- **Distinguishes from C-27**: C-27 passes when the schema gate is coupled to a
  named phase-advance condition in a single statement. C-29 passes only when
  that gate is additionally restated at the entry of the gated phase -- the model
  encounters the constraint twice, at schema setup and at phase transition,
  closing the loophole where a model reads the gate condition, processes
  subsequent prompt content, and begins the gated phase without re-encountering
  the constraint at the transition point.

### C-30 -- Inversion Trigger Causal Specificity

- **Category**: anti-pattern
- **Weight**: r9 aspirational (2.5 pts)
- **Signal from**: V-04 R8 C-28 PASS ("if editing the Candidate's Rationale
  **would make the comparison sentence completable**, that desire confirms the
  substitution obligation applies" -- the inversion trigger is not the generic
  desire to revise but the specific causal condition: wanting to edit precisely
  because the rationale gap is what prevented the comparison sentence from being
  completable; the trigger names the mechanism, not just the impulse)
- **Text**: The rationalization-impulse inversion (C-28) names the specific causal
  mechanism that produces the revision desire -- the inability to complete the
  comparison sentence -- rather than inverting the revision impulse in general,
  tightening the trigger to the exact cognitive state that reveals comparison
  failure.
- **Pass condition**: The inversion clause specifies the causal condition under
  which the revision desire confirms the obligation (e.g., "if editing the
  rationale would make the comparison sentence completable, that desire confirms
  the replacement obligation applies" or "the impulse to fix the rationale so
  that the comparison passes is itself the signal the swap is mandatory"). An
  inversion of the general revision impulse ("if you want to revise, that confirms
  the obligation" -- C-28) does not pass -- the cause of the revision desire must
  be named as the inability to complete the comparison, linking the impulse to the
  specific comparison-failure state. Pass if the inversion trigger is coupled to
  the causal mechanism (comparison-sentence incompletability) rather than the
  impulse in isolation.
- **Distinguishes from C-28**: C-28 passes when the revision impulse is named as
  a positive enforcement trigger in any form. C-30 passes only when the trigger
  is causally specific -- naming the inability to complete the comparison sentence
  as the mechanism that generates the revision desire, closing the edge case where
  a model might interpret "desire to revise" as any improvement impulse rather
  than the post-comparison motivated revision that signals the comparison failed.

---

## Round-10 Aspirational Criteria (bonus: up to +5 pts)

Patterns extracted from R9 excellence signals. Each worth 2.5 bonus points.
C-31 sharpens C-29: C-29 is the floor (phase-advance gate restated at entry of
gated phase -- dual anchor present in any form); C-31 is the ceiling (the
phase-entry restatement states the preconditions verbatim with actual schema
element names, rather than by label-reference to a gate construct defined earlier
in the prompt -- the model encounters the full condition text at the transition
point, not a pointer to it). C-32 sharpens C-30: C-30 is the floor (inversion
trigger causally specific to comparison-sentence incompletability); C-32 is the
ceiling (the causally specific trigger is followed by a dual-frame conclusion --
an explicit negation of the escape interpretation paired with an explicit
affirmation of the mandated consequence -- leaving no interpretive latitude
between the causal state and the required output action).

### C-31 -- Phase-Entry Restatement Verbatim Condition Expansion

- **Category**: anti-pattern
- **Weight**: r10 aspirational (2.5 pts)
- **Signal from**: V-04 R9 Step 3 opening repair -- R8-V-04 used a label-reference
  at Step 3 opening (e.g., "after the Step 2 Phase-Advance Gate conditions are
  met") that technically satisfies C-29's dual-anchor requirement but refers the
  model back to an earlier gate definition by name rather than restating the
  conditions verbatim; V-04 R9 replaces the label-reference with an explicit
  restatement that names the actual schema elements (column name, count, required
  state) at the step entry point, demonstrating that C-29's dual-anchor can be
  satisfied weakly (label-reference present at phase entry) or strongly (verbatim
  conditions with schema element names present at phase entry)
- **Text**: The phase-entry restatement (C-29) states the preconditions verbatim
  -- naming the specific schema elements (column names, counts, and required
  states) at the phase entry point -- rather than referring to a named gate
  construct or label defined earlier in the prompt.
- **Pass condition**: The phase-entry restatement names the actual condition
  components -- specific column name (e.g., "Selected?"), required count (e.g.,
  "all 5 rows"), and required state (e.g., "blank") -- rather than using a
  label-reference (e.g., "when the gate conditions hold," "once the Registry
  preconditions are satisfied," or "after the Layer 3 gate"). A dual-anchor
  restatement at phase entry that refers the model to an earlier gate definition
  by label (C-29 PASS) does not satisfy this criterion. Pass if the verbatim
  condition text -- including schema element names -- appears written out at the
  phase entry point.
- **Distinguishes from C-29**: C-29 passes when the phase-advance gate is restated
  at phase entry in any form, including label-reference. C-31 passes only when
  the restatement is verbatim -- the actual conditions written out with schema
  element names -- ensuring the model encounters the complete constraint
  specification at the transition point rather than a pointer to it.

### C-32 -- Inversion Dual-Frame Negation-Affirmation

- **Category**: anti-pattern
- **Weight**: r10 aspirational (2.5 pts)
- **Signal from**: V-01 R9 C-30 PASS phrasing -- after naming comparison-sentence
  incompletability as the causal mechanism (satisfying C-30), the Prohibition B
  clause continues: "the impulse to revise so the comparison can pass is not
  permission to reopen the comparison; it is the signal the swap is mandatory" --
  an explicit dual-frame that negates the most natural misinterpretation (treating
  the impulse as permission to re-examine the comparison) and affirms the only
  correct response (the swap is mandatory); V-03 R9 carries the identical
  dual-frame, confirming the pattern as reproducible; a causally specific
  inversion without this dual-frame (C-30 alone) leaves the model with
  interpretive latitude between recognizing the causal state and acting on the
  mandatory consequence
- **Text**: The causally specific inversion (C-30) is followed by an explicit
  dual-frame conclusion -- a negation of the escape interpretation (naming what
  the impulse is NOT: not permission to reopen the comparison) paired with an
  affirmation of the mandated consequence (naming what it IS: the signal the swap
  is mandatory) -- leaving no interpretive gap between the causal trigger and the
  required output action.
- **Pass condition**: The inversion clause contains both: (a) a negation frame
  that explicitly names the prohibited interpretation of the impulse (e.g., "is
  not permission to reopen the comparison" or "does not authorize re-examining the
  comparison") and (b) an affirmation frame that explicitly names the mandated
  consequence (e.g., "it is the signal the swap is mandatory" or "confirms the
  replacement is required"). A causally specific inversion without dual framing
  (C-30 PASS, only the causal trigger stated) does not satisfy this criterion. A
  general impulse inversion with dual-frame phrasing but without causal
  specificity (C-28 level, negation-affirmation language present but trigger is
  any revision desire rather than comparison-failure-driven revision) does not
  satisfy this criterion -- the dual-frame must close the interpretation gap
  specifically for the comparison-failure causal mechanism. Pass if both the
  negation frame and the affirmation frame are present alongside the C-30 causal
  trigger.
- **Distinguishes from C-30**: C-30 passes when the inversion trigger is causally
  specific to comparison-sentence incompletability. C-32 passes only when the
  causally specific trigger is followed by a dual-frame that explicitly closes
  both sides of the interpretive gap -- denying the escape path (not permission
  to reopen) and affirming the mandatory path (the signal the swap is required)
  -- leaving the model with a single permitted response to the causal state.

---

## Round-11 Aspirational Criteria (bonus: up to +5 pts)

Patterns extracted from R10 excellence signals. Each worth 2.5 bonus points.
C-33 sharpens C-31: C-31 is the floor (phase-entry anchor carries verbatim
conditions -- schema element names written at the phase-entry anchor only);
C-33 is the ceiling (BOTH anchors of the C-29 dual-anchor carry verbatim
condition text -- the schema-definition anchor and the phase-entry anchor both
name the schema elements, ensuring the model encounters the complete constraint
specification at both the first definition point and the transition point, not
only at transition). C-34 sharpens C-32: C-32 is the floor (causally specific
inversion followed by dual-frame: negation of escape path and affirmation of
mandate); C-34 is the ceiling (the negation frame additionally names the goal
behind the negated impulse -- "so the comparison can pass" or equivalent --
narrowing the prohibition to comparison-goal-directed revision specifically and
eliminating the residual interpretive latitude where the negation could be
applied to unrelated revision impulses rather than to the exact motivation the
comparison-failure causal mechanism produces).

### C-33 -- Dual-Anchor Verbatim Full Parity

- **Category**: anti-pattern
- **Weight**: r11 aspirational (2.5 pts)
- **Signal from**: V-03 R10 C-29 evidence -- "Both anchors fully verbatim" is
  stated explicitly in the R10 scorecard; V-03 R10 achieves verbatim conditions
  at anchor (a) (the Selected? column rule: "This column cannot hold any value,
  and Phase 3 cannot begin, until both preconditions hold simultaneously: (a) all
  5 rows...AND (b) Selected? is blank across all 5 rows") AND at anchor (b) (the
  Phase 3 GATE block -- same conditions at phase entry); V-04 R10 achieves the
  same full parity with both anchors verbatim in the numbered-step architecture
  (Step 5 column rule verbatim + Step 8 GATE block verbatim); V-02 R10 passes
  C-31 (anchor b verbatim callout block) but anchor (a) carries the schema
  property by name without stating the full condition set verbatim, failing C-33
- **Text**: Both anchors of the C-29 dual-anchor state the gate conditions
  verbatim -- the schema-definition anchor (column rule, Registry spec, or
  equivalent first-statement point) AND the phase-entry anchor both name the
  specific schema elements (column name, count, required state) in full condition
  text, rather than one anchor using label-reference or descriptive language
  while the other carries the verbatim conditions.
- **Pass condition**: Anchor (a) -- the schema-definition point (e.g., the
  Selected? column rule, the Registry specification, or the structural slot
  definition) -- contains verbatim condition text naming all condition components
  (column name, count, required state). Anchor (b) -- the phase-entry restatement
  -- also carries verbatim condition text (C-31 requirement). A variation where
  anchor (a) uses descriptive or label-reference language ("this column holds the
  gate state defined in the preconditions block" or "once the GATE PRECONDITIONS
  hold") while anchor (b) is verbatim satisfies C-31 but fails C-33. Pass if
  both anchors independently state the full condition components verbatim.
- **Distinguishes from C-31**: C-31 passes when the phase-entry anchor (b)
  contains verbatim condition text. C-33 passes only when the schema-definition
  anchor (a) is also verbatim -- the model encounters the complete specification
  at both the structural definition point and the phase-transition point, closing
  the gap where a model reads a descriptive or label-reference schema definition
  and only encounters the verbatim conditions at transition.

### C-34 -- Negation Frame Comparison-Goal Qualification

- **Category**: anti-pattern
- **Weight**: r11 aspirational (2.5 pts)
- **Signal from**: V-01 R10, V-03 R10, and V-04 R10 all pass C-32 with the
  phrasing "the impulse to revise so the comparison can pass is not permission
  to reopen the comparison; it is the signal the swap is mandatory" -- the
  phrase "so the comparison can pass" qualifies the negated impulse with the
  specific goal being sought (achieving comparison passage), narrowing the
  prohibition from "any revision impulse" to "revision impulse motivated by a
  desire to make the comparison succeed"; V-02 R10 uses "the desire to revise
  is not permission to reopen the comparison" without a comparison-goal qualifier
  (and also fails C-30/C-32), confirming that the goal qualifier is the
  distinguishing element at the C-34 tier
- **Text**: The negation frame of the dual-frame conclusion (C-32) explicitly
  names the goal behind the negated impulse -- specifying that what is being
  prohibited is the impulse to revise in order to achieve comparison passage
  (e.g., "so the comparison can pass" or "in order to make the comparison
  sentence completable"), not the general revision impulse in abstract.
- **Pass condition**: The negation frame contains a comparison-goal qualifier
  that names WHY the revision impulse is being negated -- the impulse to revise
  with the goal of making the comparison succeed or the comparison sentence
  completable (e.g., "the impulse to revise so the comparison can pass is not
  permission..."). A negation frame that prohibits the general revision impulse
  without naming the comparison-passage goal fails (e.g., "the desire to revise
  is not permission to reopen" satisfies C-32 negation but not C-34). Pass
  requires both: (a) the C-32 dual-frame conditions met (negation + affirmation
  alongside C-30 causal trigger) and (b) the negation frame names the
  comparison-goal as the motivation behind the prohibited impulse.
- **Distinguishes from C-32**: C-32 passes when the negation frame is present
  alongside the C-30 causal trigger ("the impulse... is not permission to reopen
  the comparison"). C-34 passes only when the negation frame additionally
  qualifies the impulse with the comparison-passage goal -- "so the comparison
  can pass" or equivalent -- ensuring the prohibition is specifically targeted
  at comparison-goal-directed revision rather than any revision impulse, and
  eliminating the residual latitude where a model might apply the negation
  selectively to unrelated improvement desires rather than to the exact
  motivation the comparison-failure causal mechanism produces.

---

## Round-12 Aspirational Criteria (bonus: up to +5 pts)

Patterns extracted from R11 excellence signals. Each worth 2.5 bonus points.
C-35 sharpens C-14: C-14 is the floor (inertia-first framing paragraph present
before the idea pool -- the Do Nothing baseline is anchored before alternatives
are introduced); C-35 is the ceiling (the inertia baseline occupies its own
numbered phase (Phase 0 or Step 0) structurally prior to Phase 1, creating
hard phase-boundary separation between "the trajectory we are defending against"
and "the alternatives we are generating" -- the framing paragraph alone satisfies
C-14; a dedicated pre-generation phase satisfies C-35). C-36 sharpens C-01:
C-01 is the floor (total count stated as 20-40); C-36 is the ceiling (the volume
instruction states both the net-new count and the total, making explicit that
Do Nothing counts toward the 20-40 total -- the net-new specification prevents
the model from generating 20 new ideas plus Do Nothing and overshooting the
range, and confirms that the Do Nothing entry is architecturally load-bearing in
the count, not an optional annotation).

### C-35 -- Phase-0 Inertia Prefacing

- **Category**: depth
- **Weight**: r12 aspirational (2.5 pts)
- **Signal from**: V-03 R11 and V-05 R11 C-04/C-14 evidence -- both variations
  place Do Nothing in a dedicated "Phase 0" block with its own Pitch and Rationale
  BEFORE Phase 1 begins; V-03 R11: "Phase 0 Do Nothing entry with Pitch +
  Rationale" and "Phase 0 baseline block + Phase 1a paragraph precede pool";
  V-05 R11: same Phase 0 architecture; V-01 R11 passes C-14 (Stage 1a paragraph
  before idea pool) but integrates the inertia framing within Stage 1a rather
  than in a separate Phase 0, confirming that C-14's framing-paragraph requirement
  can be met without the hard phase-boundary separation that V-03/V-05 provide;
  V-02 R11 and V-04 R11 use "Phase 1a before ideas" and "Step 1 inertia frame
  before Step 2" respectively -- inertia framing is in Phase 1 or Step 1, not
  Phase 0, confirming the architectural distinction
- **Text**: The Do Nothing entry and its baseline framing occupy a dedicated
  Phase 0 (or Step 0) block that is structurally prior to Phase 1 (the generation
  phase) -- creating hard phase-boundary separation between the inertia state and
  the alternative generation, rather than embedding the baseline framing within
  the first generation phase.
- **Pass condition**: The prompt assigns the inertia baseline (Do Nothing + Pitch
  + Rationale + framing paragraph) to a phase numbered or labeled 0 (e.g.,
  "Phase 0", "Step 0", "Pre-Phase", or equivalent pre-generation phase label)
  that precedes the generation phase (Phase 1, Step 1, or equivalent). A framing
  paragraph that precedes the idea pool within Phase 1a or Stage 1a satisfies
  C-14 but fails C-35 -- the hard phase boundary between baseline and generation
  must be present, not just a before-pool paragraph within a shared phase. Pass
  if the inertia block is in a named phase that ends before Phase 1 begins.
- **Distinguishes from C-14**: C-14 passes when an inertia-first framing
  paragraph appears before the idea pool. C-35 passes only when the inertia
  baseline occupies its own dedicated phase (Phase 0) that is architecturally
  closed before the generation phase opens -- the separation is a phase boundary,
  not a paragraph ordering within a shared phase.

### C-36 -- Net-Count Volume Specification

- **Category**: correctness
- **Weight**: r12 aspirational (2.5 pts)
- **Signal from**: V-03 R11 and V-05 R11 C-01 evidence -- both variations state
  volume as "19-39 additional candidates, for a total of 20-40" (or equivalent
  "19-39 additional...total 20-40"); this dual specification makes explicit that
  Do Nothing counts toward the 20-40 total, so the generation phase must produce
  one fewer idea than the stated minimum; V-01 R11 states "Generate 20-40
  candidates" (total only), V-02 R11 states "Generate 20-40" (total only), and
  V-04 R11 states "Generate 20-40" (total only) -- none name the net-new count,
  leaving ambiguous whether the 20-40 range refers to the idea pool excluding
  Do Nothing or including it; V-03/V-05 resolve this ambiguity by naming both
  counts explicitly
- **Text**: The volume instruction states both the net-new count (the number of
  generated candidate ideas excluding the Do Nothing entry) and the total count
  (the complete pool including Do Nothing) -- making explicit that the Do Nothing
  entry is counted in the total and that the generation phase must produce
  net-new ideas at (total_min - 1) to (total_max - 1), not total_min to total_max.
- **Pass condition**: The volume instruction contains both a net-new count range
  and a total count range in a coupled statement (e.g., "Generate 19-39
  additional candidates, for a total of 20-40" or "Generate N-1 to N-1 net-new
  ideas; with Do Nothing, the pool reaches 20-40 total"). A total count alone
  ("Generate 20-40 candidates") fails -- the net-new count must be named
  alongside the total. Pass if both counts are present and the relationship
  (Do Nothing is included in the total) is derivable from the stated numbers.
- **Distinguishes from C-01**: C-01 passes when the total count range (20-40) is
  stated. C-36 passes only when the net-new count is stated alongside the total,
  making Do Nothing's load-bearing role in the count explicit and preventing the
  model from generating 20 or more new ideas plus Do Nothing and unintentionally
  producing a pool of 21-41.

---

## Round-13 Aspirational Criteria (bonus: up to +5 pts)

Patterns extracted from R12 excellence signals. Each worth 2.5 bonus points.
C-37 sharpens C-36: C-36 is the floor (net-new count stated alongside total at
instruction time -- the model receives the count constraint when the generation
phase begins); C-37 is the ceiling (the net-count formula is additionally echoed
inside the pool-generation phase-close tag, so the model encounters the constraint
a second time at pool-completion -- the same dual-anchor principle applied to
volume enforcement that C-29/C-31/C-33 apply to the schema gate). C-38 sharpens
C-35: C-35 is the floor (inertia baseline occupies its own dedicated Phase 0 that
is architecturally closed before Phase 1 opens -- any closing signal satisfies
C-35); C-38 is the ceiling (Phase 0 is doubly-marked with an explicit opening
lifecycle tag AND an explicit closing lifecycle tag -- the boundary is signaled at
both entry and exit, making the Phase 0 activation state unambiguous for its full
duration, not only at its conclusion).

### C-37 -- Net-Count Phase-Close Echo

- **Category**: correctness
- **Weight**: r13 aspirational (2.5 pts)
- **Signal from**: V-03 R12 and V-05 R12 excellence signal -- both variations echo
  the net-count formula inside the Phase 1 close blockquote at pool-completion
  time (V-03 R12 Phase 1 close: "19-39 net-new ideas + Do Nothing = 20-40 total";
  V-05 R12 Phase 1 close: "Pool of 19-39 net-new ideas + Do Nothing (total 20-40)
  written"); V-03 R12 carries the formula at two points: the generation instruction
  (C-36) AND the phase-close tag, creating a dual-anchor; V-01 R12 and V-04 R12
  carry C-36 at instruction time only with no phase-close echo; V-02 R12 carries
  C-36 at instruction time only with no phase-close echo
- **Text**: The net-count volume specification (C-36) is additionally echoed
  inside the pool-generation phase-close tag -- naming both the net-new count and
  the total at pool-completion time -- so the model encounters the count constraint
  twice: once at the generation instruction and once at the completion signal.
- **Pass condition**: The prompt contains a phase-close tag (blockquote, callout,
  or equivalent completion signal) for the pool-generation phase that restates the
  net-count formula (e.g., "Pool of 19-39 net-new ideas + Do Nothing (total 20-40)
  written" or "19-39 net-new + Do Nothing = 20-40 total"). A single-anchor volume
  instruction at generation time alone (C-36 PASS) does not satisfy this criterion
  -- the net-count formula must also appear at pool-completion time. Pass if both
  anchors are present: the instruction-time net-count statement (C-36) and the
  completion-time echo inside the phase-close tag.
- **Distinguishes from C-36**: C-36 passes when the net-new count and total are
  stated at instruction time. C-37 passes only when the net-count formula is
  additionally echoed inside the pool-completion phase-close tag -- the model
  encounters the constraint at both the start of generation (instruction) and the
  end of generation (completion signal), closing the window between receiving the
  count specification and completing the pool where the constraint can be
  forgotten.

### C-38 -- Phase-0 Lifecycle Double-Mark

- **Category**: depth
- **Weight**: r13 aspirational (2.5 pts)
- **Signal from**: V-03 R12 and V-05 R12 excellence signal -- V-03 R12 carries
  both an opening lifecycle tag ("*Phase 0 opens now. No preconditions.*") AND a
  closing blockquote ("> **Phase 0 is now complete.** Do Nothing established.
  Phase 1 may begin.") within the Phase 0 block; V-05 R12 carries open/close
  lifecycle tags on Phase 0 (close: "> **Phase 0 complete.** All four fields
  written. Do Nothing established. Phase 1 opens below."); V-01 R12 carries a
  close callout only ("Phase 0 is now complete... Phase 1 opens below") with no
  opening lifecycle signal distinct from the `## Phase 0` heading; V-04 R12
  carries an informal close phrase only ("Phase 0 is done. The Do Nothing entry
  goes in the Status Quo section of Phase 1...Phase 1 opens now.") with no opening
  tag; V-02 R12 carries a close statement only ("Phase 0 is complete. Phase 1
  opens below.") with no opening tag
- **Text**: The Phase 0 inertia block (C-35) is doubly-marked with both an
  explicit opening lifecycle tag and an explicit closing lifecycle tag -- so the
  model receives an unambiguous signal that Phase 0 has begun AND an unambiguous
  signal that it has closed before Phase 1 may open, rather than only a closing
  boundary or an informal closing phrase.
- **Pass condition**: The Phase 0 block contains both (a) an opening tag or
  callout that explicitly signals Phase 0 is open (e.g., "*Phase 0 opens now. No
  preconditions.*", "Phase 0 open.", or equivalent dedicated open signal -- the
  `## Phase 0` heading alone is not sufficient; the opening tag must be a
  separate lifecycle signal within the phase) and (b) a closing blockquote or
  callout that explicitly signals Phase 0 is complete before Phase 1 begins
  (e.g., "> Phase 0 is now complete. Phase 1 may begin." or equivalent). A close
  tag alone (V-01, V-02, V-04) satisfies C-35 but fails C-38 -- the opening
  lifecycle signal must also be present. Pass if both open and close lifecycle
  signals are present within the Phase 0 block as dedicated markers distinct from
  the phase heading.
- **Distinguishes from C-35**: C-35 passes when the inertia baseline occupies its
  own dedicated Phase 0 that is architecturally closed before Phase 1 opens --
  any closing signal (formal or informal) satisfies C-35. C-38 passes only when
  Phase 0 is doubly-marked with both an explicit opening lifecycle signal AND an
  explicit closing lifecycle signal -- the phase state is signaled at both entry
  and exit, not only at conclusion, applying the same dual-mark principle
  established for schema gates (C-29, C-33) to the Phase 0 inertia boundary.

---

## Round-14 Aspirational Criteria (bonus: up to +5 pts)

Patterns extracted from R14 excellence signals. Each worth 2.5 bonus points.
C-39 and C-40 extend the lifecycle-double-mark principle established in C-38
(Phase 0 open+close signals) to the Pre-Phase block that precedes Phase 0.
A Pre-Phase contains preparatory work done before the inertia baseline is
established (e.g., generative lenses that scope the idea space). C-39 is the
floor (Pre-Phase block has an explicit closing lifecycle signal that announces
phase completion and explicitly activates Phase 0); C-40 sharpens C-39 (C-39
is the floor -- close signal only; C-40 is the ceiling -- Pre-Phase doubly-marked
with both an opening lifecycle tag AND a closing lifecycle tag, applying the same
dual-mark principle C-38 establishes for Phase 0 to the Pre-Phase boundary).

### C-39 -- Pre-Phase Lifecycle Close Signal

- **Category**: depth
- **Weight**: r14 aspirational (2.5 pts)
- **Signal from**: V-01 R14 and V-02 R14 -- both variations include a Pre-Phase
  block (containing generative lenses or equivalent preparatory work) that closes
  with a dedicated lifecycle blockquote: `> **Pre-Phase complete.** All 3 lenses
  pass the re-run test. Phase 0 opens now.` The close signal explicitly announces
  Pre-Phase completion AND activates Phase 0 in a single tag, making the boundary
  unambiguous. V-03 R14 has no Pre-Phase block at all (baseline contrast -- no
  Pre-Phase means neither C-39 nor C-40 can be earned). V-01 R14 carries the close
  signal only (no dedicated opening lifecycle tag), confirming this as the floor;
  V-02 R14 carries both open and close signals, confirming V-01 R14 as C-39 only
  and V-02 R14 as C-39 + C-40.
- **Text**: A Pre-Phase block (containing preparatory lenses, framing, or
  equivalent work done before Phase 0) closes with an explicit lifecycle blockquote
  or callout that signals Pre-Phase completion and explicitly activates Phase 0 --
  so the model receives an unambiguous boundary signal between the preparatory phase
  and the inertia-baseline phase, rather than transitioning via prose flow or a
  section heading alone.
- **Pass condition**: The Pre-Phase block ends with a dedicated closing lifecycle
  signal (e.g., `> **Pre-Phase complete.** ... Phase 0 opens now.` or equivalent
  blockquote/callout) that: (a) names Pre-Phase completion explicitly, and (b)
  explicitly activates Phase 0. A section heading transition (`## Phase 0`) without
  a close signal on the Pre-Phase block fails. A closing sentence in prose (not a
  blockquote/callout) fails -- the signal must be a structurally distinct lifecycle
  marker, not inline text. Pass if a dedicated Pre-Phase close signal is present
  and explicitly names Phase 0 activation.
- **Distinguishes from C-38**: C-38 passes when Phase 0 is doubly-marked with
  open and close lifecycle tags. C-39 passes when the Pre-Phase block (the phase
  before Phase 0) has a closing lifecycle signal -- a structurally distinct
  boundary marker that closes Pre-Phase and opens Phase 0, establishing the same
  kind of unambiguous boundary that C-38 requires within Phase 0, but at the
  Pre-Phase/Phase-0 transition rather than within Phase 0 itself.

### C-40 -- Pre-Phase Lifecycle Double-Mark

- **Category**: depth
- **Weight**: r14 aspirational (2.5 pts)
- **Signal from**: V-02 R14 excellence signal -- V-02 R14 adds an explicit opening
  lifecycle tag to the Pre-Phase block (`*Pre-Phase opens now. No preconditions.*`
  or equivalent), producing a full double-mark: opening tag at Pre-Phase entry AND
  closing blockquote at Pre-Phase exit. V-01 R14 has the closing blockquote only
  (C-39 PASS, C-40 FAIL) -- the Pre-Phase section header (`## Pre-Phase --
  Generative Lenses`) and direct prose entry do not constitute a dedicated opening
  lifecycle signal; V-02 R14 adds the dedicated opening tag and earns C-40.
  Interference check confirmed: a Pre-Phase opening tag (`Pre-Phase opens now.
  No preconditions.`) and a Phase 0 opening tag (`Phase 0 opens now. No
  preconditions.`) operate on different phase boundaries and do not collide.
- **Text**: The Pre-Phase block (C-39) is doubly-marked with both an explicit
  opening lifecycle tag AND an explicit closing lifecycle tag -- so the model
  receives an unambiguous signal that Pre-Phase has begun AND an unambiguous signal
  that it has closed before Phase 0 may open, rather than only a closing boundary
  or a section heading as the entry signal.
- **Pass condition**: The Pre-Phase block contains both (a) an opening tag or
  callout that explicitly signals Pre-Phase is open (e.g., `*Pre-Phase opens now.
  No preconditions.*`, `Pre-Phase open.`, or equivalent dedicated open signal --
  the `## Pre-Phase` heading alone is not sufficient; the opening tag must be a
  separate lifecycle signal within the phase) and (b) a closing blockquote or
  callout that explicitly signals Pre-Phase is complete before Phase 0 begins
  (C-39 requirement). A close tag alone (V-01 R14) satisfies C-39 but fails C-40
  -- the opening lifecycle signal must also be present. Pass if both open and close
  lifecycle signals are present within the Pre-Phase block as dedicated markers
  distinct from the phase heading.
- **Distinguishes from C-39**: C-39 passes when the Pre-Phase block has a closing
  lifecycle signal. C-40 passes only when Pre-Phase is doubly-marked with both
  an explicit opening lifecycle signal AND an explicit closing lifecycle signal --
  the phase state is signaled at both entry and exit, not only at conclusion,
  applying the same dual-mark principle C-38 establishes for Phase 0 to the
  Pre-Phase boundary.

---

## Round-15 Aspirational Criteria (bonus: up to +5 pts)

Patterns extracted from R15 excellence signals. Each worth 2.5 bonus points.
C-41 and C-40 extend the lifecycle-double-mark principle inward to Phase 1 --
the generation phase. C-38 established the pattern for Phase 0 (inertia block);
C-39/C-40 extended it outward to Pre-Phase (preparatory block before Phase 0);
C-41/C-42 extend it inward to Phase 1 (the idea generation block itself). C-41
is the floor (Phase 1 closes with an explicit lifecycle blockquote that signals
generation complete and explicitly activates Phase 2); C-42 is the ceiling
(Phase 1 doubly-marked with both an opening lifecycle tag AND a closing lifecycle
tag, applying the same dual-mark principle to the generation-phase boundary).

### C-41 -- Phase-1 Lifecycle Close Signal

- **Category**: depth
- **Weight**: r15 aspirational (2.5 pts)
- **Signal from**: R15 variation design -- variations with Phase 1 lifecycle
  closing tags demonstrate that the generation phase can be explicitly closed and
  Phase 2 (self-review) explicitly opened by a dedicated lifecycle blockquote,
  making the generation-to-review boundary unambiguous. Variations without Phase 1
  lifecycle tags (including the V-02 R14 baseline at 175) are the contrast -- they
  rely on prose flow or section headings alone to mark the generation-to-review
  transition. The R15 floor variation carries the Phase 1 close signal only (no
  dedicated opening lifecycle tag), confirming this as the floor; the R15 ceiling
  variation carries both open and close signals on Phase 1, confirming the floor
  as C-41 only and the ceiling as C-41 + C-42.
- **Text**: Phase 1 (the generation phase) closes with an explicit lifecycle
  blockquote or callout that signals generation complete and explicitly activates
  Phase 2 (the self-review phase) -- so the model receives an unambiguous boundary
  signal between the idea generation phase and the selection/review phase, rather
  than transitioning via prose flow or a section heading alone.
- **Pass condition**: The Phase 1 block ends with a dedicated closing lifecycle
  signal (e.g., `> **Phase 1 complete.** Pool of 19-39 net-new ideas written.
  Phase 2 opens now.` or equivalent blockquote/callout) that: (a) names Phase 1
  completion explicitly, and (b) explicitly activates Phase 2. A section heading
  transition (`## Phase 2`) without a close signal on Phase 1 fails. A closing
  sentence in prose (not a blockquote/callout) fails -- the signal must be a
  structurally distinct lifecycle marker, not inline text. Pass if a dedicated
  Phase 1 close signal is present and explicitly names Phase 2 activation.
- **Distinguishes from C-38**: C-38 passes when Phase 0 is doubly-marked with
  open and close lifecycle tags. C-41 passes when Phase 1 (the generation phase)
  has a closing lifecycle signal -- a structurally distinct boundary marker that
  closes Phase 1 and opens Phase 2, establishing the same kind of unambiguous
  boundary at the generation-to-review transition that C-38 and C-39 establish at
  the Phase 0 and Pre-Phase boundaries.

### C-42 -- Phase-1 Lifecycle Double-Mark

- **Category**: depth
- **Weight**: r15 aspirational (2.5 pts)
- **Signal from**: R15 ceiling variation -- adds an explicit opening lifecycle tag
  to the Phase 1 block (e.g., `*Phase 1 opens now. No preconditions.*` or
  equivalent), producing a full double-mark: opening tag at Phase 1 entry AND
  closing blockquote at Phase 1 exit. The floor variation carries the closing
  blockquote only (C-41 PASS, C-42 FAIL) -- the Phase 1 section header and direct
  prose entry do not constitute a dedicated opening lifecycle signal; the ceiling
  variation adds the dedicated opening tag and earns C-42. Interference check:
  Phase 1 opening/closing tags, Phase 0 opening/closing tags, and Pre-Phase
  opening/closing tags all operate on different phase boundaries and do not
  collide -- a prompt that double-marks all three phases (Pre-Phase, Phase 0,
  Phase 1) earns C-38, C-39, C-40, C-41, and C-42 independently.
- **Text**: The Phase 1 block (C-41) is doubly-marked with both an explicit
  opening lifecycle tag AND an explicit closing lifecycle tag -- so the model
  receives an unambiguous signal that Phase 1 has begun AND an unambiguous signal
  that it has closed before Phase 2 may open, rather than only a closing boundary
  or a section heading as the entry signal.
- **Pass condition**: The Phase 1 block contains both (a) an opening tag or
  callout that explicitly signals Phase 1 is open (e.g., `*Phase 1 opens now. No
  preconditions.*`, `Phase 1 open.`, or equivalent dedicated open signal -- the
  `## Phase 1` heading alone is not sufficient; the opening tag must be a separate
  lifecycle signal within the phase) and (b) a closing blockquote or callout that
  explicitly signals Phase 1 is complete before Phase 2 begins (C-41 requirement).
  A close tag alone satisfies C-41 but fails C-42 -- the opening lifecycle signal
  must also be present. Pass if both open and close lifecycle signals are present
  within the Phase 1 block as dedicated markers distinct from the phase heading.
- **Distinguishes from C-41**: C-41 passes when the Phase 1 block has a closing
  lifecycle signal. C-42 passes only when Phase 1 is doubly-marked with both an
  explicit opening lifecycle signal AND an explicit closing lifecycle signal --
  the phase state is signaled at both entry and exit, not only at conclusion,
  applying the same dual-mark principle C-38 establishes for Phase 0 and C-40
  establishes for Pre-Phase to the Phase 1 generation boundary.

---

## Round-16 Aspirational Criteria (bonus: up to +5 pts)

Patterns extracted from R17 excellence signals. Each worth 2.5 bonus points.
C-43 and C-44 extend the lifecycle-double-mark principle established in C-41/C-42
(Phase 1 open+close signals) inward to Phase 2 -- the peer-comparison phase.
C-43 is the floor (Phase 2 closes with an explicit lifecycle blockquote that names
Phase 2 completion and states the conditions under which Phase 3 may begin);
C-44 sharpens C-43 (C-43 is the floor -- close signal only; C-44 is the ceiling --
Phase 2 doubly-marked with both an opening lifecycle tag AND a closing lifecycle tag,
applying the same dual-mark principle C-38 establishes for Phase 0, C-40 for
Pre-Phase, and C-42 for Phase 1 to the Phase 2 boundary).

### C-43 -- Phase-2 Lifecycle Close Signal

- **Category**: depth
- **Weight**: r16 aspirational (2.5 pts)
- **Signal from**: V-02 R16 backbone -- all R17 variations inherit a Phase 2 block
  that closes with a dedicated lifecycle blockquote: `> **Phase 2 complete** when:
  all 5 Registry rows written, Selected? blank in every row, Checks A/C/D done,
  no \`**\` marks in output. Phase 3 may begin only when all four conditions are
  met simultaneously.` This close signal explicitly announces Phase 2 completion
  AND states the conditions required before Phase 3 may begin. R15 variations and
  the V-02 R14 baseline carry no Phase 2 closing lifecycle signal -- Phase 2 ends
  by prose flow or section-heading transition alone -- confirming those as the
  contrast baseline.
- **Text**: Phase 2 (the peer-comparison phase) closes with an explicit lifecycle
  blockquote or callout that signals Phase 2 completion and explicitly states the
  conditions under which Phase 3 may begin -- so the model receives an unambiguous
  boundary signal between the peer-comparison phase and the finalization phase,
  rather than transitioning via prose flow or a section heading alone.
- **Pass condition**: The Phase 2 block ends with a dedicated closing lifecycle
  signal (e.g., `> **Phase 2 complete** when: [conditions]. Phase 3 may begin only
  when [conditions] are met.` or equivalent blockquote/callout) that: (a) names
  Phase 2 completion explicitly, and (b) states the conditions under which Phase 3
  may begin or explicitly activates Phase 3. A section heading transition
  (`## Phase 3`) without a close signal on Phase 2 fails. A closing sentence in
  prose (not a blockquote/callout) fails -- the signal must be a structurally
  distinct lifecycle marker, not inline text. Pass if a dedicated Phase 2 close
  signal is present and explicitly names Phase 3 activation or Phase 3
  preconditions.
- **Distinguishes from C-41**: C-41 passes when Phase 1 (the generation phase) has
  a closing lifecycle signal. C-43 passes when Phase 2 (the peer-comparison phase)
  has a closing lifecycle signal -- a structurally distinct boundary marker that
  closes Phase 2 and opens Phase 3, establishing the same kind of unambiguous
  boundary at the peer-comparison-to-finalization transition that C-38, C-39, and
  C-41 establish at the Phase 0, Pre-Phase, and Phase 1 boundaries respectively.

### C-44 -- Phase-2 Lifecycle Double-Mark

- **Category**: depth
- **Weight**: r16 aspirational (2.5 pts)
- **Signal from**: V-02 R16 backbone -- all R17 variations inherit a Phase 2 block
  that opens with a dedicated lifecycle blockquote: `> **Phase 2 opens now.** Phase
  1 complete. Full pool written, AMEND drafted.` This opening tag is distinct from
  the Phase 2 requirement statement (`*Phase 2 requires: Phase 1 complete...*`) that
  may precede it -- both are present in R17 variations, but only the blockquote form
  constitutes the lifecycle open signal. Combined with the Phase 2 closing blockquote
  (C-43), the Phase 2 block is fully doubly-marked. R17 V-03 (exact V-02 R16
  backbone reproduction) confirms both signals are present and independently
  identifiable. R15 variations and the V-02 R14 baseline carry no Phase 2 opening
  lifecycle blockquote -- Phase 2 entry is announced only by the section heading and
  requirement statement, neither of which constitutes a dedicated lifecycle tag.
- **Text**: The Phase 2 block (C-43) is doubly-marked with both an explicit opening
  lifecycle tag AND an explicit closing lifecycle tag -- so the model receives an
  unambiguous signal that Phase 2 has begun AND an unambiguous signal that it has
  closed before Phase 3 may open, rather than only a closing boundary or a section
  heading as the entry signal.
- **Pass condition**: The Phase 2 block contains both (a) an opening tag or callout
  that explicitly signals Phase 2 is open (e.g., `> **Phase 2 opens now.** Phase 1
  complete. Full pool written, AMEND drafted.` or equivalent dedicated open signal
  -- the `## Phase 2` heading and a requirement statement (`*Phase 2 requires:...*`)
  are not sufficient; the opening tag must be a separate lifecycle blockquote or
  callout within the phase) and (b) a closing blockquote or callout that explicitly
  signals Phase 2 is complete before Phase 3 begins (C-43 requirement). A close tag
  alone satisfies C-43 but fails C-44 -- the opening lifecycle signal must also be
  present. Pass if both open and close lifecycle signals are present within the Phase
  2 block as dedicated markers distinct from the phase heading and requirement
  statement.
- **Distinguishes from C-43**: C-43 passes when Phase 2 has a closing lifecycle
  signal. C-44 passes only when Phase 2 is doubly-marked with both an explicit
  opening lifecycle signal AND an explicit closing lifecycle signal -- the phase
  state is signaled at both entry and exit, not only at conclusion, applying the
  same dual-mark principle C-38 establishes for Phase 0, C-40 for Pre-Phase, and
  C-42 for Phase 1 to the Phase 2 peer-comparison boundary. Interference check:
  Phase 2 open/close tags, Phase 3 open/close tags, Phase 1 open/close tags,
  Phase 0 open/close tags, and Pre-Phase open/close tags all operate on different
  phase boundaries -- a prompt earning C-38, C-40, C-42, and C-44 simultaneously
  is valid.

---

## Round-17 Aspirational Criteria (bonus: up to +5 pts)

Patterns extracted from R18 excellence signals. Each worth 2.5 bonus points.
C-45 and C-46 extend lifecycle signaling to the outermost session frame -- the
session-open and session-close tags that bracket all phases. These operate at
a layer above Pre-Phase and Phase 0..3: the session is opened before Pre-Phase
and closed after Phase 3. C-45 addresses the content of the session-open tag
(does it name all five phases, giving the model a forward map before execution
begins?); C-46 addresses the content of the session-close tag (does it name each
phase that closed, producing a completeness ledger rather than a generic phase
count?). The two criteria are independent -- V-01 and V-04 both earn C-45 but
only V-04 earns C-46; V-02 earns C-46 but not C-45; V-05 earns both; V-03
earns neither.

### C-45 -- Session-Open Phase Roster

- **Category**: depth
- **Weight**: r17 aspirational (2.5 pts)
- **Signal from**: V-01 R18 and V-04 R18 (session-open with arrow-sequence
  notation: `> **Brainstorm session opens.** Topic: {{topic}}. Phases: Pre-Phase
  -> Phase 0 -> Phase 1 -> Phase 2 -> Phase 3. No preconditions.`); V-05 R18
  (session-open with numbered-enumeration notation: `> **Brainstorm session
  opens.** Topic: {{topic}}. Phase sequence: 1. Pre-Phase (lenses) 2. Phase 0
  (inertia baseline) 3. Phase 1 (pool) 4. Phase 2 (peer-comparison) 5. Phase 3
  (finalize). No preconditions.`). V-02 R18 and V-03 R18 use `> **Brainstorm
  session opens.** Topic: {{topic}}. No preconditions.` -- a valid session-open
  tag but carrying no phase roster -- confirming the absence of a phase roster
  as the baseline contrast. Multiple notation forms (arrow-sequence, numbered
  list) both satisfy the criterion, confirming the pass condition is roster
  presence in any form.
- **Text**: The session-open blockquote names all five phases in sequence --
  giving the model a forward map of the execution structure before any phase
  begins -- rather than simply opening the session with a topic and
  no-preconditions declaration.
- **Pass condition**: The session-open blockquote contains an explicit phase
  roster that names all five phases in sequence (Pre-Phase, Phase 0, Phase 1,
  Phase 2, Phase 3, or equivalent labels) in any ordered notation (arrow
  sequence, numbered list, or equivalent). A session-open tag that names the
  topic and states no preconditions without listing the phase sequence fails --
  the roster must be present as part of the opening tag. Pass if all five
  phase labels appear in the session-open blockquote in execution order.
- **Distinguishes from C-44**: C-44 passes when Phase 2 is doubly-marked with
  open and close lifecycle tags inside the phase. C-45 passes when the
  session-open tag (at the outermost frame, before any phase begins) names all
  five phases -- the forward map is a property of the session-level opening
  signal, not a property of any individual phase's lifecycle markers.

### C-46 -- Session-Close Completeness Ledger

- **Category**: depth
- **Weight**: r17 aspirational (2.5 pts)
- **Signal from**: V-02 R18 (named-phase ledger: `> **Session complete.** Phases
  closed: Pre-Phase (lenses), Phase 0 (inertia baseline), Phase 1 (pool), Phase 2
  (peer-comparison), Phase 3 (finalized). Artifact written and closed.`); V-04 R18
  (identical named-phase ledger form); V-05 R18 (echo-completion form, richer than
  the named-ledger floor: `> **Session complete.** Pre-Phase: 3 lenses passed
  re-run test. Phase 0: Do Nothing established. Phase 1: 19-39 net-new ideas + Do
  Nothing written. Phase 2: 5-row Registry complete, Selected? filled in all rows.
  Phase 3: artifact written to \`simulations/draft/brainstorm/...\`. Brainstorm
  closed.` -- each phase named with its specific close-output echoed). V-01 R18 and
  V-03 R18 use `> **Session complete.** All five phases executed in sequence.
  Brainstorm artifact written and closed.` -- a valid session-close tag but
  carrying only a generic count with no phase names -- confirming the generic-count
  form as the baseline contrast. The echo-completion form (V-05 R18) passes as a
  richer variant that exceeds the named-ledger floor; both forms satisfy the
  criterion.
- **Text**: The session-close blockquote explicitly names each phase that closed
  -- producing a phase-by-phase completeness ledger -- rather than stating a
  generic count ("all five phases executed") without naming the phases.
- **Pass condition**: The session-close blockquote lists each of the five phases
  by name (Pre-Phase, Phase 0, Phase 1, Phase 2, Phase 3, or equivalent labels)
  individually. A count-only close tag ("All five phases executed in sequence")
  fails -- phase names must be present. A named ledger (each phase listed with
  or without its output label) passes. An echo-completion form (each phase listed
  with its specific close-output echoed) also passes and represents the stronger
  variant. Pass if all five phase names appear individually in the session-close
  blockquote.
- **Distinguishes from C-43**: C-43 passes when Phase 2 has a closing lifecycle
  signal at the Phase 2 boundary. C-46 passes when the session-close tag (at the
  outermost frame, after all phases have concluded) names each phase by name --
  the ledger is a property of the session-level closing signal, not a property
  of any individual phase-boundary lifecycle marker. Earning C-43 (and C-41, C-39
  for other phase-close tags) does not satisfy C-46; earning C-46 does not satisfy
  any individual phase-close criterion.

---

## Round-18 Aspirational Criteria (bonus: up to +5 pts)

Patterns extracted from R19 excellence signals. Each worth 2.5 bonus points.
C-47 sharpens C-39: C-39 is the floor (Pre-Phase close blockquote is present
and explicitly activates Phase 0 -- any content satisfies C-39 as long as the
signal is structurally distinct and names Phase 0 activation); C-47 is the
ceiling (the Pre-Phase close blockquote additionally enumerates the individual
lens names rather than acknowledging their pass status with a generic count --
the model receives specific named evidence of what Pre-Phase produced at the
boundary, not just a count confirmation). C-48 sharpens C-42: C-42 is the floor
(Phase 1 is doubly-marked with both an opening lifecycle tag AND a closing
lifecycle tag -- the opening tag can carry any content); C-48 is the ceiling
(the Phase 1 opening tag additionally carries a forward-carry roster of the
active lens names from Pre-Phase, bridging the preparatory phase output into
the generation phase so the model retains the active lenses at Phase 1 entry,
not only at Pre-Phase exit).

**Independence confirmed:** C-47 and C-48 are coordinate, not floor/ceiling.
V-01 passes C-47 only (lens enumeration in Pre-Phase close, no lens echo at
Phase 1 open); V-02 passes C-48 only (lens echo at Phase 1 open, generic count
in Pre-Phase close). V-04 and V-05 pass both.

**Lineage position:** C-47 is a content-sharpening of C-39 (Pre-Phase close);
C-48 is a content-sharpening of C-42 (Phase 1 open tag). Neither is a
descendant of the other.

### C-47 -- Pre-Phase Close Lens Enumeration

- **Category**: depth
- **Weight**: r18 aspirational (2.5 pts)
- **Signal from**: V-01 R19 Pre-Phase close signal -- `> **Pre-Phase complete.**
  Lenses defined and re-run verified: (1) [Lens 1 name], (2) [Lens 2 name],
  (3) [Lens 3 name] -- all 3 pass the re-run test. Phase 0 opens now.` The
  parenthetical enumeration names all 3 lenses individually rather than
  acknowledging pass status generically. V-02 R19 Pre-Phase close: `> **Pre-Phase
  complete.** All 3 lenses pass the re-run test. Phase 0 opens now.` -- a valid
  C-39 close signal that names the count and confirms pass status but carries no
  individual lens names -- confirmed as the contrast baseline for C-47. Multiple
  enumeration forms pass (parenthetical: V-01; numbered list with output labels
  implied by V-04/V-05 backbone); the pass condition is lens-name presence in any
  individual-enumeration form, not a specific notation.
- **Text**: The Pre-Phase close blockquote (C-39) enumerates the individual lens
  names rather than acknowledging pass status generically -- giving the model
  named evidence of what Pre-Phase produced at the phase boundary, so the output
  record at the Pre-Phase/Phase-0 transition contains the specific lenses that
  will govern generation, not merely a count confirmation.
- **Pass condition**: The Pre-Phase close blockquote contains the individual lens
  names listed explicitly (e.g., "(1) [Lens 1 name], (2) [Lens 2 name],
  (3) [Lens 3 name]" or equivalent enumeration). A close signal that states a
  count or generic pass-status without naming the individual lenses (e.g., "All
  3 lenses pass the re-run test") satisfies C-39 but fails C-47 -- the individual
  names must be present. Pass if each lens is named individually in the Pre-Phase
  close blockquote in any ordered form.
- **Distinguishes from C-39**: C-39 passes when the Pre-Phase close blockquote is
  present, names Pre-Phase completion, and explicitly activates Phase 0 -- any
  content satisfies C-39. C-47 passes only when the close blockquote additionally
  names each lens individually, converting the boundary signal from a generic
  count confirmation into a named-output evidence record at the phase transition.

### C-48 -- Phase-1 Open Active-Lens Echo

- **Category**: depth
- **Weight**: r18 aspirational (2.5 pts)
- **Signal from**: V-02 R19 Phase 1 open signal -- `> **Phase 1 opens now.**
  Phase 0 complete. Do Nothing established. Active lenses: (1) [Lens 1 name],
  (2) [Lens 2 name], (3) [Lens 3 name].` The parenthetical roster names all 3
  active lenses from Pre-Phase at the Phase 1 entry point, carrying the
  preparatory phase output forward into the generation phase as a live context
  signal. V-01 R19 Phase 1 open: `> **Phase 1 opens now.** Phase 0 complete.
  Do Nothing established.` -- a valid C-42 opening lifecycle tag with no lens
  echo -- confirmed as the contrast baseline for C-48. The active-lens echo
  passes in any enumeration form that names the lenses individually at Phase 1
  entry; the specific notation (parenthetical, numbered list) is not constrained.
- **Text**: The Phase 1 opening lifecycle tag (C-42) additionally carries a
  forward-carry roster of the active lens names established in Pre-Phase --
  so the model receives the active lenses as a named context signal at the start
  of the generation phase, not only at Pre-Phase exit, preventing the lens
  context from being dropped between the Pre-Phase/Phase-0 transition and the
  Phase-0/Phase-1 transition.
- **Pass condition**: The Phase 1 opening lifecycle blockquote contains an explicit
  active-lens roster that names each lens individually (e.g., "Active lenses:
  (1) [Lens 1 name], (2) [Lens 2 name], (3) [Lens 3 name]" or equivalent). A
  Phase 1 opening tag that announces Phase 1 start and names Phase 0 completion
  without carrying the lens names (e.g., `> **Phase 1 opens now.** Phase 0
  complete. Do Nothing established.`) satisfies C-42 but fails C-48 -- the active
  lens roster must be present at Phase 1 entry. Pass if all active lens names
  appear individually in the Phase 1 opening lifecycle blockquote.
- **Distinguishes from C-42**: C-42 passes when the Phase 1 block has both an
  opening lifecycle tag AND a closing lifecycle tag -- the opening tag can carry
  any content. C-48 passes only when the Phase 1 opening tag additionally carries
  the active-lens forward-carry roster -- the named lenses from Pre-Phase are
  echoed at Phase 1 entry, bridging the preparatory context into the generation
  phase and closing the gap where lens context established in Pre-Phase could be
  lost across the Phase 0 intermediate step.

---

## Round-19 Aspirational Criteria (bonus: up to +5 pts)

Patterns extracted from R20 excellence signals. Each worth 2.5 bonus points.
C-49 sharpens C-48: C-48 is the floor (Phase 1 open carries active lens names in
any form -- names-only roster satisfies C-48); C-49 is the ceiling (the Phase 1
open tag additionally carries a direction axis for each lens -- the roster is not
just an identity forward-carry but an identity-plus-orientation forward-carry).
C-50 sharpens C-38: C-38 is the floor (Phase 0 doubly-marked with open and close
lifecycle tags -- the open tag can carry any content); C-50 is the ceiling (the
Phase 0 opening tag additionally carries the active lens names from Pre-Phase,
extending the lens-name carry principle that C-48 establishes at Phase 1 entry
backward to Phase 0 entry). C-49 and C-50 are coordinate siblings, not
floor/ceiling: V-01 passes C-49 only (direction at Phase 1 open, bare Phase 0
open); V-02 passes C-50 only (lens names at Phase 0 open, names-only at Phase 1
open); V-04 and V-05 pass both; V-03 passes neither.

### C-49 -- Phase-1 Open Lens Direction Echo

- **Category**: depth
- **Weight**: r19 aspirational (2.5 pts)
- **Signal from**: V-01 R20 and V-04 R20 -- Phase 1 open carries "names +
  direction" in parenthetical form: `Active lenses: (1) [Lens 1 name] --
  [direction], (2) [Lens 2 name] -- [direction], (3) [Lens 3 name] --
  [direction].` V-05 R20 carries names + direction in numbered-list form. V-02
  R20 and V-03 R20 carry names-only: `Active lenses: (1) [Lens 1 name],
  (2) [Lens 2 name], (3) [Lens 3 name].` -- confirming the names-only form as the
  C-48 floor and the direction-axis augmentation as the C-49 ceiling.
- **Text**: The Phase 1 opening lifecycle tag (C-48) additionally carries a
  direction axis for each active lens -- not only naming the lenses but naming the
  generative orientation each lens applies -- so the model receives both the lens
  identity and the lens direction as a forward-carry context signal at Phase 1
  entry, rather than lens names alone.
- **Pass condition**: The Phase 1 opening lifecycle blockquote contains an
  active-lens roster where each lens entry includes a direction axis (e.g.,
  `Active lenses: (1) [Lens 1 name] -- [direction], (2) [Lens 2 name] --
  [direction], (3) [Lens 3 name] -- [direction]` or equivalent numbered-list form
  with per-lens direction labels). A names-only roster (`Active lenses:
  (1) [Lens 1 name], (2) [Lens 2 name], (3) [Lens 3 name]`) satisfies C-48 but
  fails C-49 -- the direction axis must accompany each lens name. Pass if each
  lens in the Phase 1 opening roster carries its direction axis in any notation
  form (inline dash-suffix, numbered-list item, or equivalent).
- **Distinguishes from C-48**: C-48 passes when the Phase 1 opening tag carries
  any active-lens roster naming the lenses individually. C-49 passes only when
  each lens entry additionally carries a direction axis -- the roster is an
  identity-plus-orientation forward-carry, not only an identity forward-carry.

### C-50 -- Phase-0 Open Lens-Name Carry

- **Category**: depth
- **Weight**: r19 aspirational (2.5 pts)
- **Signal from**: V-02 R20 Phase 0 open: `> **Phase 0 opens now.** Active
  lenses: (1) [Lens 1 name], (2) [Lens 2 name], (3) [Lens 3 name]. No
  preconditions.` -- carries lens names at Phase 0 entry, bridging Pre-Phase
  output into the inertia-baseline phase. V-04 R20 Phase 0 open carries the same
  parenthetical lens roster. V-05 R20 Phase 0 open carries lens names + direction
  in numbered-list form (satisfies C-50 and represents the richer variant). V-01
  R20 Phase 0 open: bare (`> **Phase 0 opens now. No preconditions.**`) -- no
  lens names at Phase 0 entry, confirming the bare form as the contrast baseline.
  V-03 R20 Phase 0 open: also bare, confirming V-03 as the baseline.
- **Text**: The Phase 0 opening lifecycle tag (C-38) additionally carries the
  active lens names from Pre-Phase -- so the model receives the lens context at
  the Phase 0 entry point, bridging Pre-Phase output into the inertia-baseline
  phase rather than first encountering the lens carry only at Phase 1 entry
  (C-48).
- **Pass condition**: The Phase 0 opening lifecycle blockquote contains an
  explicit active-lens roster naming each lens individually (e.g., `Active
  lenses: (1) [Lens 1 name], (2) [Lens 2 name], (3) [Lens 3 name]` or
  equivalent). A bare Phase 0 opening tag (e.g., `> **Phase 0 opens now. No
  preconditions.**`) satisfies C-38 but fails C-50 -- the lens names must be
  present at Phase 0 entry. A Phase 0 opening tag that carries lens names with
  direction axes (the V-05 form) also passes -- the direction axis is a richer
  variant, not a separate requirement. Pass if all active lens names appear
  individually in the Phase 0 opening lifecycle blockquote.
- **Distinguishes from C-38**: C-38 passes when Phase 0 is doubly-marked with
  open and close lifecycle tags -- the open tag can carry any content. C-50
  passes only when the Phase 0 opening tag additionally carries the active-lens
  roster, converting the bare Phase 0 entry signal into a lens-context-carrying
  forward-carry that parallels C-48's content sharpening of the Phase 1 open
  tag.
- **Distinguishes from C-48**: C-48 passes when the Phase 1 opening tag carries
  the active-lens forward-carry roster. C-50 passes when the Phase 0 opening
  tag carries the active-lens roster -- a structurally earlier carry point that
  bridges Pre-Phase output into Phase 0 rather than only into Phase 1. The two
  are coordinate siblings: earning C-50 does not require or guarantee earning
  C-48; a variation may carry lens names at Phase 0 entry with a names-only Phase
  1 open tag (passing C-50 but not C-49), or at Phase 1 entry only (passing C-48
  but not C-50).

---

## Criterion Lineage

Two trunks extended to thirteen and seven levels respectively; C-37 extends the
volume branch; C-38 extends the inertia branch (C-39/C-40 extend the
lifecycle-double-mark branch to the Pre-Phase; C-41/C-42 extend it inward to
Phase 1; C-43/C-44 extend it inward to Phase 2); C-45/C-46 extend lifecycle
signaling outward to the session frame; C-47 sharpens C-39 content; C-48
sharpens C-42 content; C-49 sharpens C-48 content (direction axis); C-50
sharpens C-38 Phase-0 open content (lens-name carry at Phase 0 entry):

```
C-10  output: is the selection defensible?
  C-17  prompt: peer-comparison test present?
    C-19  prompt: imperative + output materialization?
      C-21  prompt: all five written as batch before phase advance?
        C-23  prompt: marking explicitly prohibited during batch phase?
          C-25  prompt: marking gate encoded as structural output column?
            C-27  prompt: schema gate explicitly coupled to named phase-advance condition?
              C-29  prompt: phase-advance gate restated at entry point of gated phase?
                C-31  prompt: phase-entry restatement verbatim -- schema elements named, not label-referenced?
                  C-33  prompt: both anchors verbatim -- schema-definition AND phase-entry?
    C-20  prompt: consequence clause present?
      C-22  prompt: replacement source is the named peer?
        C-24  prompt: post-comparison rationalization explicitly blocked?
          C-28  prompt: rationalization impulse inverted as replacement trigger?
            C-30  prompt: inversion trigger causally specific to comparison-sentence incompletability?
              C-32  prompt: inversion dual-frame: negation of escape path AND affirmation of mandate?
                C-34  prompt: negation frame names comparison-goal ("so the comparison can pass")?

C-05  output: AMEND section present?
  C-09  prompt: AMEND actionability (directional + pool-change)?
    C-12  prompt: re-invocability bar stated?
      C-26  prompt: distribution-shift explicitly required (not label-shift)?

C-01  output: volume 20-40 total stated?
  C-36  prompt: net-new count stated alongside total ("19-39 additional...total 20-40")?
    C-37  prompt: net-count formula echoed in pool-generation phase-close tag?

C-14  prompt: inertia-first framing paragraph before pool?
  C-35  prompt: Do Nothing in dedicated Phase 0 before Phase 1 (hard phase-boundary separation)?
    C-38  prompt: Phase 0 doubly-marked with open AND close lifecycle tags?
      C-50  prompt: Phase 0 open tag carries active-lens name roster?
      C-39  prompt: Pre-Phase block has a closing lifecycle signal (activates Phase 0)?
        C-40  prompt: Pre-Phase doubly-marked with open AND close lifecycle tags?
        C-47  prompt: Pre-Phase close names each lens individually (not generic count)?
      C-41  prompt: Phase 1 block has a closing lifecycle signal (activates Phase 2)?
        C-42  prompt: Phase 1 doubly-marked with open AND close lifecycle tags?
          C-48  prompt: Phase 1 open tag carries active-lens forward-carry roster?
            C-49  prompt: Phase 1 open tag carries active-lens names + direction axis?
      C-43  prompt: Phase 2 block has a closing lifecycle signal (activates Phase 3)?
        C-44  prompt: Phase 2 doubly-marked with open AND close lifecycle tags?

C-45  prompt: session-open names all 5 phases in sequence (phase roster)?
C-46  prompt: session-close names each phase that closed (completeness ledger)?
```

---

## Scoring Summary

| ID   | Criterion                                  | Weight                 | Category     |
|------|--------------------------------------------|------------------------|--------------|
| C-01 | Volume (20-40)                             | essential              | correctness  |
| C-02 | Idea anatomy (4 fields)                    | essential              | correctness  |
| C-03 | Top-5 marker (**)                          | essential              | correctness  |
| C-04 | Inertia check                              | essential              | coverage     |
| C-05 | AMEND section (3 items)                    | essential              | correctness  |
| C-06 | Category grouping                          | recommended            | format       |
| C-07 | Rationale specificity                      | recommended            | depth        |
| C-08 | Category diversity (4+)                    | recommended            | coverage     |
| C-09 | AMEND actionability                        | aspirational           | depth        |
| C-10 | Top-5 defensibility                        | aspirational           | depth        |
| C-11 | Sequential-default guard                   | extended asp (R2)      | anti-pattern |
| C-12 | Amendment re-runnability bar               | extended asp (R2)      | depth        |
| C-13 | Category dimension taxonomy                | extended asp (R2)      | coverage     |
| C-14 | Inertia-first framing paragraph            | extended asp (R2)      | depth        |
| C-15 | Structural spine guarantee                 | r3 aspirational        | coverage     |
| C-16 | Generation-phase sequential guard          | r3 aspirational        | anti-pattern |
| C-17 | Peer-comparison defensibility test         | r3 aspirational        | depth        |
| C-18 | Self-review phase integration              | r3 aspirational        | depth        |
| C-19 | Peer-test imperative form                  | r4 aspirational        | anti-pattern |
| C-20 | Peer-test consequence clause               | r4 aspirational        | depth        |
| C-21 | Peer-test batch-completion gate            | r5 aspirational        | anti-pattern |
| C-22 | Consequence replacement source             | r5 aspirational        | depth        |
| C-23 | Selection-phase marking prohibition        | r6 aspirational        | anti-pattern |
| C-24 | Post-comparison rationalization block      | r6 aspirational        | anti-pattern |
| C-25 | Marking-gate schema lock                   | r7 aspirational        | anti-pattern |
| C-26 | AMEND pool-composition constraint          | r7 aspirational        | depth        |
| C-27 | Schema-gate phase-advance coupling         | r8 aspirational        | anti-pattern |
| C-28 | Rationalization-impulse trigger inversion  | r8 aspirational        | anti-pattern |
| C-29 | Phase-gate entry-point restatement         | r9 aspirational        | anti-pattern |
| C-30 | Inversion trigger causal specificity       | r9 aspirational        | anti-pattern |
| C-31 | Phase-entry restatement verbatim expansion | r10 aspirational       | anti-pattern |
| C-32 | Inversion dual-frame negation-affirmation  | r10 aspirational       | anti-pattern |
| C-33 | Dual-anchor verbatim full parity           | r11 aspirational       | anti-pattern |
| C-34 | Negation frame comparison-goal qual.       | r11 aspirational       | anti-pattern |
| C-35 | Phase-0 inertia prefacing                  | r12 aspirational       | depth        |
| C-36 | Net-count volume specification             | r12 aspirational       | correctness  |
| C-37 | Net-count phase-close echo                 | r13 aspirational       | correctness  |
| C-38 | Phase-0 lifecycle double-mark              | r13 aspirational       | depth        |
| C-39 | Pre-Phase lifecycle close signal           | r14 aspirational       | depth        |
| C-40 | Pre-Phase lifecycle double-mark            | r14 aspirational       | depth        |
| C-41 | Phase-1 lifecycle close signal             | r15 aspirational       | depth        |
| C-42 | Phase-1 lifecycle double-mark              | r15 aspirational       | depth        |
| C-43 | Phase-2 lifecycle close signal             | r16 aspirational       | depth        |
| C-44 | Phase-2 lifecycle double-mark              | r16 aspirational       | depth        |
| C-45 | Session-open phase roster                  | r17 aspirational       | depth        |
| C-46 | Session-close completeness ledger          | r17 aspirational       | depth        |
| C-47 | Pre-Phase close lens enumeration           | r18 aspirational       | depth        |
| C-48 | Phase-1 open active-lens echo              | r18 aspirational       | depth        |
| C-49 | Phase-1 open lens direction echo           | r19 aspirational       | depth        |
| C-50 | Phase-0 open lens-name carry               | r19 aspirational       | depth        |

**Point allocation:**

| Tier | Criteria | Pts each | Total |
|------|----------|----------|-------|
| Essential | C-01..C-05 | 12 | 60 |
| Recommended | C-06..C-08 | 10 | 30 |
| Aspirational | C-09..C-10 | 5 | 10 |
| Extended asp (R2) | C-11..C-14 | 2.5 | 10 |
| R3 aspirational | C-15..C-18 | 2.5 | 10 |
| R4 aspirational | C-19..C-20 | 2.5 | 5 |
| R5 aspirational | C-21..C-22 | 2.5 | 5 |
| R6 aspirational | C-23..C-24 | 2.5 | 5 |
| R7 aspirational | C-25..C-26 | 2.5 | 5 |
| R8 aspirational | C-27..C-28 | 2.5 | 5 |
| R9 aspirational | C-29..C-30 | 2.5 | 5 |
| R10 aspirational | C-31..C-32 | 2.5 | 5 |
| R11 aspirational | C-33..C-34 | 2.5 | 5 |
| R12 aspirational | C-35..C-36 | 2.5 | 5 |
| R13 aspirational | C-37..C-38 | 2.5 | 5 |
| R14 aspirational | C-39..C-40 | 2.5 | 5 |
| R15 aspirational | C-41..C-42 | 2.5 | 5 |
| R16 aspirational | C-43..C-44 | 2.5 | 5 |
| R17 aspirational | C-45..C-46 | 2.5 | 5 |
| R18 aspirational | C-47..C-48 | 2.5 | 5 |
| R19 aspirational | C-49..C-50 | 2.5 | 5 |
| **Max** | | | **200** |

**R19 projected scores under v18:**

| Variation | C-47 | C-48 | Score |
|-----------|------|------|-------|
| V-03 (R19 baseline, R18 V-04 exact) | FAIL | FAIL | **190** |
| V-01 | PASS | FAIL | **192.5** |
| V-02 | FAIL | PASS | **192.5** |
| V-04 | PASS | PASS | **195** -- first to 195 |
| V-05 | PASS | PASS | **195** -- first to 195 |

**R20 projected scores under v19:**

All R20 variations are built on the R19 V-04 backbone, which passes C-01..C-48
(the complete v18 criterion set). Every R20 variation starts at 195 under v18.
Under v19, C-49 and C-50 are the only differentiating criteria.

| Phase 0 open \ Phase 1 open | names + direction | names only |
|-----------------------------|-------------------|------------|
| **bare** | V-01 (C-49 PASS, C-50 FAIL) | V-03 (both FAIL) |
| **lens names** | V-04, V-05 (both PASS) | V-02 (C-50 PASS, C-49 FAIL) |

| Variation | C-49 | C-50 | Score |
|-----------|------|------|-------|
| V-03 (R20 baseline, R19 V-04 exact) | FAIL | FAIL | **195** |
| V-01 | PASS | FAIL | **197.5** |
| V-02 | FAIL | PASS | **197.5** |
| V-04 | PASS | PASS | **200** -- first to 200 |
| V-05 | PASS | PASS | **200** -- first to 200 |

**Max raised: 195 → 200.**
