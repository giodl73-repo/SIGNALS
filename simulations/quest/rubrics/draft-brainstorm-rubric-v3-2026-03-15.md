Written to `simulations/quest/rubrics/draft-brainstorm-rubric-v3-2026-03-15.md`.

---

**Four new R3 aspirational criteria (C-15 -- C-18), each worth 2.5 bonus points:**

| ID | Criterion | Source signal | What it catches |
|----|-----------|---------------|-----------------|
| C-15 | Structural Spine Guarantee | V-02 "structural guarantee, not just scaffolding" on C-13 | Prompts that name dimension types (passing C-13) but leave section structure to the model -- dimensional diversity is aspirational, not architectural |
| C-16 | Generation-Phase Sequential Guard | V-03 C-11 note ("interrogative rather than prohibitive") | Prompts where the anti-sequential prohibition lives in a post-generation check rather than as a generation-phase imperative -- same text effect, wrong cognitive timing |
| C-17 | Peer-Comparison Defensibility Test | V-01 + V-03 convergent sentence formulations | Prompts that require defensibility without embedding a specific "why this and not [unmarked peer]?" test -- the model has no comparison anchor to force the check |
| C-18 | Self-Review Phase Integration | V-03 Check A/B/C/D feeding back into top-5 and AMEND | Single-pass prompts where generation and selection happen in one block -- no explicit feedback loop from a review phase into output decisions |

**Scoring update**: max is now **120**. The formula gains a fifth term `+ (r3_asp_pass/4 * 10)`. Golden threshold stays at 80.

The R2 profiles now score: V-02 = 115, V-03 = 115, V-01 = 112.5. V-04 R3 profile requires a validation run.
 Nothing).
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
- **Text**: Ideas span at least 4 meaningfully distinct categories that represent
  different approaches or dimensions.
- **Pass condition**: Count distinct category labels across all ideas. Pass if >=
  4 and categories represent genuinely different angles (not "Approach A" and
  "Approach A variant"). Fail if fewer than 4 or if categories are superficially
  different but cover the same dimension.

---

## Aspirational Criteria (weight: 10%)

Raise the bar once essential and recommended are stable.

### C-09 -- AMEND Actionability

- **Category**: depth
- **Weight**: aspirational
- **Text**: Each AMEND adjustment is specific enough that a reader could
  immediately re-run the brainstorm in that direction -- naming what changes and
  why it produces a meaningfully different pool.
- **Pass condition**: Each of the 3 AMEND items: (a) names a concrete shift axis,
  (b) explains what kind of ideas would appear or disappear, and (c) would
  produce a noticeably different ranked pool if applied. Pass if all 3 meet all
  three sub-conditions. Fail if any item is a generic restatement (e.g., "be
  more creative").

### C-10 -- Top-5 Defensibility

- **Category**: depth
- **Weight**: aspirational
- **Text**: The 5 ideas marked `**` are meaningfully differentiated from the rest
  -- they are the strongest candidates for immediate viability, and the selection
  is defensible given the pool.
- **Pass condition**: The 5 marked ideas are neither the first 5 listed
  (suggesting no real selection occurred) nor obviously inferior to unmarked
  peers. If the rationale for any marked idea is weaker than an unmarked idea in
  the same category, fail. Pass if marked ideas collectively represent the pool's
  most actionable, lowest-barrier, or highest-confidence candidates.

---

## Extended Aspirational Criteria -- R2 (bonus: up to +10 pts)

Patterns extracted from R1 excellence signals (V-02 and V-04). Each worth 2.5
bonus points. These criteria distinguish prompts that close specific failure modes
from prompts that merely describe desired output.

### C-11 -- Sequential-Default Guard

- **Category**: anti-pattern
- **Weight**: extended aspirational (2.5 pts)
- **Signal from**: V-04 (only R1 variation to pass C-10 fully)
- **Text**: The prompt explicitly prohibits marking ideas in the order they were
  generated, closing the most common top-5 failure mode.
- **Pass condition**: The prompt contains an explicit anti-sequential-default
  instruction (e.g., "Do not default to marking the first 5 you wrote" or
  equivalent). Positive framing alone ("pick the most viable") does not pass --
  the prohibitive instruction must be present. Fail if the prompt relies on
  quality framing without naming the sequencing trap.

### C-12 -- Amendment Re-Runnability Bar

- **Category**: depth
- **Weight**: extended aspirational (2.5 pts)
- **Signal from**: V-02, V-04 (C-09 full pass); V-01, V-03 partial
- **Text**: AMEND items are framed as actionable re-invocation directives -- the
  prompt states that a reader must be able to re-run the brainstorm from the
  directive and obtain a noticeably different pool.
- **Pass condition**: The prompt explicitly states the re-invocability test (e.g.,
  "a reader should be able to re-invoke the brainstorm with that directive and
  get a noticeably different pool"). Covering sub-conditions (a) direction named
  and (b) pool change described is necessary but not sufficient for this
  criterion -- the re-invocability bar must be stated. Fail if the prompt
  describes amendment quality without invoking the re-run test.

### C-13 -- Category Dimension Taxonomy

- **Category**: coverage
- **Weight**: extended aspirational (2.5 pts)
- **Signal from**: V-04 ("strongest enforcement" on C-08 -- supplied 6 named
  dimension types)
- **Text**: Beyond requiring a minimum category count, the prompt supplies named
  dimension types as scaffolding to ensure categories map to genuinely distinct
  conceptual axes.
- **Pass condition**: The prompt names at least 4 dimension types (e.g., scope,
  timing, integration, audience, build-vs-buy, status quo) as examples or
  required angles. A minimum count requirement alone (C-08) does not pass this
  criterion. Fail if categories are user-generated without dimensional
  scaffolding -- surface label variety without axis diversity remains possible.

### C-14 -- Inertia-First Framing Paragraph

- **Category**: depth
- **Weight**: extended aspirational (2.5 pts)
- **Signal from**: V-02 (Phase 0 mandatory framing paragraph before alternatives)
- **Text**: A dedicated framing paragraph appears before the idea list, describing
  the current trajectory if the team does nothing -- making Do Nothing a live
  strategic contender rather than a checkbox table entry.
- **Pass condition**: The prompt requires a framing section (paragraph, callout,
  or Phase 0 block) that precedes the idea candidates and describes the status
  quo trajectory. The inertia entry in the idea table (C-04) is not sufficient --
  the framing paragraph must appear before alternatives are introduced. Fail if
  Do Nothing appears only as a row in the idea pool without a prior structural
  anchor.

---

## Round-3 Aspirational Criteria (bonus: up to +10 pts)

Patterns extracted from R2 excellence signals. Each worth 2.5 bonus points.
These capture qualitative distinctions that all R2 variations passed at the
C-11--C-14 level but that expert scoring revealed as diverging in strength.

### C-15 -- Structural Spine Guarantee

- **Category**: coverage
- **Weight**: r3 aspirational (2.5 pts)
- **Signal from**: V-02 C-13/C-06 note ("structural guarantee, not just
  scaffolding" -- 7 named dimension types as mandatory output sections; cannot
  produce fewer than 7 categories by construction)
- **Text**: Dimension types are not merely named as examples or required angles
  (C-13) -- they are mandated as structural output sections, making dimensional
  diversity a property of output shape rather than a property of model compliance.
- **Pass condition**: The prompt requires named dimension types to serve as
  mandatory section headers or structural slots in the output (e.g., "one section
  per dimension, labeled with the dimension name"). Supplying named examples while
  leaving section structure to the model fails. Pass if at least 4 dimensions are
  mandated structural positions, not advisory scaffolding.
- **Distinguishes from C-13**: C-13 passes when types are named. C-15 passes only
  when those types are required output structure.

### C-16 -- Generation-Phase Sequential Guard

- **Category**: anti-pattern
- **Weight**: r3 aspirational (2.5 pts)
- **Signal from**: V-03 C-11 note ("prohibition lives in a verification check
  rather than as a generation-phase imperative. The effect is the same but the
  framing is interrogative rather than prohibitive.")
- **Text**: The anti-sequential-default instruction (C-11) is placed within the
  generation phase as an imperative constraint, not deferred to a post-generation
  review check.
- **Pass condition**: The sequential-default prohibition appears before or within
  the generation instruction, as an imperative statement (e.g., "Do not mark as
  you generate -- finish the full pool first"). If the prompt has a multi-phase
  structure and the guard appears only in a check/review phase (e.g., "Check: are
  the marked ideas the first 5 you wrote?"), this criterion fails. Pass requires
  generation-phase placement and imperative framing.
- **Distinguishes from C-11**: C-11 passes when prohibition is present anywhere.
  C-16 passes only when prohibition is in the generation phase as imperative.

### C-17 -- Peer-Comparison Defensibility Test

- **Category**: depth
- **Weight**: r3 aspirational (2.5 pts)
- **Signal from**: V-01 ("defensible if you could answer: Why these five and not
  the unmarked idea in the same category?"); V-03 ("can you complete this
  sentence: 'I chose this over [unmarked peer] because ___'?") -- both
  independently converged on a specific sentence-completion or peer-comparison
  formulation
- **Text**: The top-5 defensibility requirement (C-10) is enforced via a specific
  embedded test -- a sentence the model must be able to complete, naming an
  unmarked peer in the same category as the one being justified.
- **Pass condition**: The prompt includes a specific sentence-completion or
  peer-comparison question to be applied before finalizing the top-5 (e.g., "Why
  this and not [unmarked peer in the same category]?" or "I chose this over
  [peer] because ___"). Generic defensibility framing ("select the most viable")
  does not pass. The test must name the peer-comparison structure explicitly.
- **Distinguishes from C-10**: C-10 (rubric criterion) checks whether the OUTPUT
  selection is defensible. C-17 checks whether the PROMPT embeds a specific test
  mechanism to force that defensibility.

### C-18 -- Self-Review Phase Integration

- **Category**: depth
- **Weight**: r3 aspirational (2.5 pts)
- **Signal from**: V-03 ("Mark exactly 5 ideas with ** on their heading (informed
  by Check A and B)"); V-03 Check phases A/B/C/D that explicitly feed back into
  output decisions (Check A -> top-5 anti-sequential, Check B -> top-5
  defensibility, Check C -> AMEND finalization, Check D -> inertia placement)
- **Text**: The prompt structures the task as at least two phases -- a generation
  phase and a dedicated self-review phase -- with the review phase explicitly
  connected to at least one output decision (top-5 selection, AMEND finalization,
  or inertia placement).
- **Pass condition**: The prompt contains a distinct self-review or check phase
  (separate from generation instructions) that explicitly connects to an output
  decision (e.g., "After generating the full pool, run checks A and B before
  marking top-5" or "Finalize AMEND in Phase 3 after Check C"). Single-pass
  prompts where all instructions appear in one block without explicit feedback
  loops fail. Pass if at least one review-to-output feedback link is named.
- **Distinguishes from C-09/C-10**: C-09 and C-10 check output quality criteria.
  C-18 checks whether the prompt's process structure produces an explicit
  feedback loop from review to output decision.

---

## Scoring Summary

| ID   | Criterion                          | Weight                 | Category     |
|------|------------------------------------|------------------------|--------------|
| C-01 | Volume (20-40)                     | essential              | correctness  |
| C-02 | Idea anatomy (4 fields)            | essential              | correctness  |
| C-03 | Top-5 marker (**)                  | essential              | correctness  |
| C-04 | Inertia check                      | essential              | coverage     |
| C-05 | AMEND section (3 items)            | essential              | correctness  |
| C-06 | Category grouping                  | recommended            | format       |
| C-07 | Rationale specificity              | recommended            | depth        |
| C-08 | Category diversity (4+)            | recommended            | coverage     |
| C-09 | AMEND actionability                | aspirational           | depth        |
| C-10 | Top-5 defensibility                | aspirational           | depth        |
| C-11 | Sequential-default guard           | extended asp (R2)      | anti-pattern |
| C-12 | Amendment re-runnability bar       | extended asp (R2)      | depth        |
| C-13 | Category dimension taxonomy        | extended asp (R2)      | coverage     |
| C-14 | Inertia-first framing paragraph    | extended asp (R2)      | depth        |
| C-15 | Structural spine guarantee         | r3 aspirational        | coverage     |
| C-16 | Generation-phase sequential guard  | r3 aspirational        | anti-pattern |
| C-17 | Peer-comparison defensibility test | r3 aspirational        | depth        |
| C-18 | Self-review phase integration      | r3 aspirational        | depth        |

**Point allocation:**

| Tier | Criteria | Pts each | Total |
|------|----------|----------|-------|
| Essential | C-01..C-05 | 12 | 60 |
| Recommended | C-06..C-08 | 10 | 30 |
| Aspirational | C-09..C-10 | 5 | 10 |
| Extended asp (R2) | C-11..C-14 | 2.5 | 10 |
| R3 aspirational | C-15..C-18 | 2.5 | 10 |
| **Max** | | | **120** |

**Example scores:**

| Scenario | Ess | Rec | Asp | Ext | R3 | Score | Golden? |
|----------|-----|-----|-----|-----|----|-------|---------|
| All pass | 5/5 | 3/3 | 2/2 | 4/4 | 4/4 | 120 | Yes |
| R2 ceiling | 5/5 | 3/3 | 2/2 | 4/4 | 0/4 | 110 | Yes |
| Miss C-04 | fail | -- | -- | -- | -- | n/a | No (essential fail) |
| Essential only | 5/5 | 0/3 | 0/2 | 0/4 | 0/4 | 60 | No |
| Essential + rec | 5/5 | 3/3 | 0/2 | 0/4 | 0/4 | 90 | Yes |
| Essential + 1 rec | 5/5 | 1/3 | 0/2 | 0/4 | 0/4 | 70 | No |
| V-02 R2 profile | 5/5 | 3/3 | 2/2 | 4/4 | 2/4 | 115 | Yes |
| V-03 R2 profile | 5/5 | 3/3 | 2/2 | 4/4 | 2/4 | 115 | Yes |
| V-01 R2 profile | 5/5 | 3/3 | 2/2 | 4/4 | 1/4 | 112.5 | Yes |

*V-02 passes C-15 (7 dimensions are mandatory structural sections) and C-18
(Preliminary paragraph + Artifact order mandate a feedback loop); fails C-16
(no multi-phase check structure), C-17 (no sentence-completion test).*

*V-03 passes C-16 (generation-phase imperative "do not mark top-5 yet" precedes
checks) and C-18 (Check A/B/C/D phases explicitly feed top-5 and AMEND
decisions); fails C-15 (categories are scaffolding, not mandated sections), C-17
(Check B is close but formulated as "can you complete" not an embedded peer
formulation).*

*V-01 passes C-17 ("Why these five and not the unmarked idea in the same
category?" is an embedded peer-comparison test); fails C-15 (no structural
mandate), C-16 (single-phase), C-18 (no dedicated check phase).*

*V-04 R3 profile requires validation run.*

---

## Change Log

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-15 | Initial rubric -- 10 criteria across 3 tiers (essential / recommended / aspirational) |
| v2 | 2026-03-15 | Added C-11..C-14 as extended aspirational bonus criteria from R1 excellence signals; max raised to 110 |
| v3 | 2026-03-15 | Added C-15..C-18 as R3 aspirational bonus criteria from R2 scoring signals; max raised to 120. New criteria: C-15 structural spine guarantee (V-02 mandatory-sections pattern), C-16 generation-phase sequential guard (V-03 interrogative-vs-imperative note), C-17 peer-comparison defensibility test (V-01 + V-03 convergent sentence formulations), C-18 self-review phase integration (V-03 Check A/B/C/D feedback-loop pattern). |
