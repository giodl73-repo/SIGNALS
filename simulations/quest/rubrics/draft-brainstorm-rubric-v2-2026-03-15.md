Written to `simulations/quest/rubrics/draft-brainstorm-rubric-v2-2026-03-15.md`.

---

**Four new extended aspirational criteria (C-11 – C-14), each worth 2.5 bonus points:**

| ID | Criterion | Source signal | What it catches |
|----|-----------|---------------|-----------------|
| C-11 | Sequential-Default Guard | V-04 only R1 full C-10 pass | Prompts that use positive framing ("pick the best") but never say "don't pick in order" — the anchoring trap stays open |
| C-12 | Amendment Re-Runnability Bar | V-02, V-04 full C-09 pass vs V-01, V-03 partial | Prompts that describe amendment direction and pool change (sub-conditions a+b) but never state the re-invocability test (sub-condition c) |
| C-13 | Category Dimension Taxonomy | V-04 "strongest enforcement" note on C-08 | Prompts that require 4+ categories but leave axis selection to the model — surface label variety without dimensional diversity |
| C-14 | Inertia-First Framing Paragraph | V-02 Phase 0 pattern | Prompts where Do Nothing is a table row (C-04 passing) but there is no framing paragraph before alternatives — inertia is a list entry, not a strategic anchor |

**Scoring structure update**: max is now **110**. The formula gains a fourth term `+ (extended_aspirational_pass/4 * 10)`. Golden threshold stays at 80. R1's best variation (V-04) scores 107.5.
d fields: name, one-line pitch, category, and rationale.
- **Pass condition**: Sample at least 5 ideas (including first, last, and middle). Every sampled idea has all four fields present and non-empty. If any sampled idea is missing a field, fail. If all four fields are consistently present, pass.

### C-03 -- Top-5 Marker
- **Category**: correctness
- **Weight**: essential
- **Text**: Exactly 5 ideas are marked with `**` to indicate immediate viability.
- **Pass condition**: Count ideas marked with `**` (double asterisk, typically as a bold marker or inline `**name**` or `**` suffix). Pass if exactly 5. Fail if 0, fewer than 5, or more than 5.

### C-04 -- Inertia Check
- **Category**: coverage
- **Weight**: essential
- **Text**: A "do nothing" candidate is present that describes the status quo path.
- **Pass condition**: At least one idea explicitly represents the inertia/status-quo option (e.g., named "Do Nothing", "Status Quo", "No Change", or equivalent). The rationale must describe what the current state looks like, not just say "do nothing." Pass if present with rationale; fail if absent or present but unnamed/undescribed.

### C-05 -- AMEND Section
- **Category**: correctness
- **Weight**: essential
- **Text**: The output contains an AMEND section with exactly 3 specific adjustments that would shift the pool.
- **Pass condition**: A labeled AMEND section exists (heading, label, or prefix "AMEND:"). It contains exactly 3 adjustment items. Each adjustment names a direction of change (e.g., "more ambitious," "conservative," "different audience") AND states what would change in the pool. Pass if all three are present and directional; fail if section is absent, has fewer than 3, or adjustments are vague.

---

## Recommended Criteria (weight: 30%)

Output is better with these. Missing one lowers the score but does not block golden.

### C-06 -- Category Grouping
- **Category**: format
- **Weight**: recommended
- **Text**: Ideas are organized under explicit category headers, not presented as a flat list with category as a field only.
- **Pass condition**: The document uses visible grouping (e.g., markdown headers `## Category Name`, bold category labels, or clearly separated sections) so a reader can scan by category. A flat numbered list where category is only a field attribute fails. Pass if at least 3 distinct category groups are visually separated.

### C-07 -- Rationale Specificity
- **Category**: depth
- **Weight**: recommended
- **Text**: Rationales are specific to the topic at hand, not generic reasoning that could apply to any brainstorm.
- **Pass condition**: Sample 5 rationales. Each must reference the topic by name, a specific user need, constraint, or opportunity tied to the topic. Generic rationales like "this is a good idea because it provides value" fail. Pass if 4 of 5 sampled rationales are topic-specific.

### C-08 -- Category Diversity
- **Category**: coverage
- **Weight**: recommended
- **Text**: Ideas span at least 4 meaningfully distinct categories that represent different approaches or dimensions.
- **Pass condition**: Count distinct category labels across all ideas. Pass if >= 4 and categories represent genuinely different angles (not "Approach A" and "Approach A variant"). Fail if fewer than 4 or if categories are superficially different but cover the same dimension.

---

## Aspirational Criteria (weight: 10%)

Raise the bar once essential and recommended are stable.

### C-09 -- AMEND Actionability
- **Category**: depth
- **Weight**: aspirational
- **Text**: Each AMEND adjustment is specific enough that a reader could immediately re-run the brainstorm in that direction -- naming what changes and why it produces a meaningfully different pool.
- **Pass condition**: Each of the 3 AMEND items: (a) names a concrete shift axis, (b) explains what kind of ideas would appear or disappear, and (c) would produce a noticeably different ranked pool if applied. Pass if all 3 meet all three sub-conditions. Fail if any item is a generic restatement (e.g., "be more creative").

### C-10 -- Top-5 Defensibility
- **Category**: depth
- **Weight**: aspirational
- **Text**: The 5 ideas marked ** are meaningfully differentiated from the rest -- they are the strongest candidates for immediate viability, and the selection is defensible given the pool.
- **Pass condition**: The 5 marked ideas are neither the first 5 listed (suggesting no real selection occurred) nor obviously inferior to unmarked peers. If the rationale for any marked idea is weaker than an unmarked idea in the same category, fail. Pass if marked ideas collectively represent the pool's most actionable, lowest-barrier, or highest-confidence candidates.

---

## Extended Aspirational Criteria (bonus: up to +10 points)

Patterns extracted from R1 excellence signals (V-02 and V-04). Each worth 2.5 bonus points.
These criteria distinguish prompts that close specific failure modes from prompts that merely describe desired output.

### C-11 -- Sequential-Default Guard
- **Category**: anti-pattern
- **Weight**: extended aspirational (2.5 pts)
- **Signal from**: V-04 (only R1 variation to pass C-10 fully)
- **Text**: The prompt explicitly prohibits marking ideas in the order they were generated, closing the most common top-5 failure mode.
- **Pass condition**: The prompt contains an explicit anti-sequential-default instruction (e.g., "Do not default to marking the first 5 you wrote" or equivalent). Positive framing alone ("pick the most viable") does not pass -- the prohibitive instruction must be present. Fail if the prompt relies on quality framing without naming the sequencing trap.

### C-12 -- Amendment Re-Runnability Bar
- **Category**: depth
- **Weight**: extended aspirational (2.5 pts)
- **Signal from**: V-02, V-04 (C-09 full pass); V-01, V-03 earned only C-09 partial
- **Text**: AMEND items are framed as actionable re-invocation directives -- the prompt states that a reader must be able to re-run the brainstorm from the directive and obtain a noticeably different pool.
- **Pass condition**: The prompt explicitly states the re-invocability test (e.g., "a reader should be able to re-invoke the brainstorm with that directive and get a noticeably different pool"). Covering sub-conditions (a) direction named and (b) pool change described is necessary but not sufficient for this criterion -- the re-invocability bar must be stated. Fail if the prompt describes amendment quality without invoking the re-run test.

### C-13 -- Category Dimension Taxonomy
- **Category**: coverage
- **Weight**: extended aspirational (2.5 pts)
- **Signal from**: V-04 ("strongest enforcement" on C-08 -- supplied 6 named dimension types)
- **Text**: Beyond requiring a minimum category count, the prompt supplies named dimension types as scaffolding to ensure categories map to genuinely distinct conceptual axes.
- **Pass condition**: The prompt names at least 4 dimension types (e.g., scope, timing, integration, audience, build-vs-buy, status quo) as examples or required angles. A minimum count requirement alone (C-08) does not pass this criterion. Fail if categories are user-generated without dimensional scaffolding -- surface label variety without axis diversity remains possible.

### C-14 -- Inertia-First Framing Paragraph
- **Category**: depth
- **Weight**: extended aspirational (2.5 pts)
- **Signal from**: V-02 (Phase 0 mandatory framing paragraph before alternatives)
- **Text**: A dedicated framing paragraph appears before the idea list, describing the current trajectory if the team does nothing -- making Do Nothing a live strategic contender rather than a checkbox table entry.
- **Pass condition**: The prompt requires a framing section (paragraph, callout, or Phase 0 block) that precedes the idea candidates and describes the status quo trajectory. The inertia entry in the idea table (C-04) is not sufficient -- the framing paragraph must appear before alternatives are introduced. Fail if Do Nothing appears only as a row in the idea pool without a prior structural anchor.

---

## Scoring Summary

| ID   | Criterion                       | Weight                   | Category    |
|------|---------------------------------|--------------------------|-------------|
| C-01 | Volume (20-40)                  | essential                | correctness |
| C-02 | Idea anatomy (4 fields)         | essential                | correctness |
| C-03 | Top-5 marker (**)               | essential                | correctness |
| C-04 | Inertia check                   | essential                | coverage    |
| C-05 | AMEND section (3 items)         | essential                | correctness |
| C-06 | Category grouping               | recommended              | format      |
| C-07 | Rationale specificity           | recommended              | depth       |
| C-08 | Category diversity (4+)         | recommended              | coverage    |
| C-09 | AMEND actionability             | aspirational             | depth       |
| C-10 | Top-5 defensibility             | aspirational             | depth       |
| C-11 | Sequential-default guard        | extended aspirational    | anti-pattern|
| C-12 | Amendment re-runnability bar    | extended aspirational    | depth       |
| C-13 | Category dimension taxonomy     | extended aspirational    | coverage    |
| C-14 | Inertia-first framing paragraph | extended aspirational    | depth       |

**Example scores:**

| Scenario | Ess | Rec | Asp | Ext | Composite | Golden? |
|----------|-----|-----|-----|-----|-----------|---------|
| All pass | 5/5 | 3/3 | 2/2 | 4/4 | 110 | Yes |
| All core pass | 5/5 | 3/3 | 2/2 | 0/4 | 100 | Yes |
| Miss C-04 | fail | -- | -- | -- | n/a | No (essential fail) |
| Essential only | 5/5 | 0/3 | 0/2 | 0/4 | 60 | No (composite < 80) |
| Essential + rec | 5/5 | 3/3 | 0/2 | 0/4 | 90 | Yes |
| Essential + 1 rec | 5/5 | 1/3 | 0/2 | 0/4 | 70 | No (composite < 80) |
| R1 V-02 profile | 5/5 | 3/3 | 1.5/2 | 2/4 | 97.5+5 = 102.5 | Yes |
| R1 V-04 profile | 5/5 | 3/3 | 2/2 | 3/4 | 100+7.5 = 107.5 | Yes |

*(V-02: C-09=pass, C-10=partial; C-12 and C-14 pass, C-11 and C-13 fail)*
*(V-04: C-09=pass, C-10=pass; C-11, C-12, C-13 pass, C-14 fail)*

---

## Change Log

| Version | Date       | Change |
|---------|------------|--------|
| v1      | 2026-03-15 | Initial rubric -- 10 criteria across 3 tiers (essential/recommended/aspirational) |
| v2      | 2026-03-15 | Added C-11 through C-14 as extended aspirational bonus criteria from R1 excellence signals (V-02, V-04 patterns) |
