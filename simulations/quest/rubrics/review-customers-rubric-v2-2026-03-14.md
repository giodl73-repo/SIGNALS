Written to `simulations/quest/rubrics/review-customers-rubric-v2-2026-03-14.md`.

---

**v2 changes summary:**

The aspirational tier grows from 2 to 5 criteria. Three new ones:

| ID | Criterion | Category | R1 source |
|----|-----------|----------|-----------|
| C-11 | Inline blocker/leak flags at point of scoring | reliability | V-05 `[BLOCKER]`/`[LEAK]` inline markers outperformed V-03's post-hoc DETECT phase |
| C-12 | Hybrid table+prose format | format | V-02's table achieved completeness but capped rationale depth at 1 sentence — hybrid recovers both |
| C-13 | Causal rationale: feature gap named as mechanism | depth | V-04's "explain what produced these reactions" outperformed V-03's "don't restate the score" because it specifies the mechanism rather than prohibiting a behavior |

**Design intent for each:**

- **C-11** catches the failure mode where a blocker exists in the scores but the post-hoc section misses it. Inline flags make that structurally impossible.
- **C-12** resolves the completeness/depth trade-off directly — both structures must be present, so you can't sacrifice one for the other.
- **C-13** upgrades C-08 from "non-trivial rationale" to "causal rationale" — the output must name what the feature did to produce the score, not just describe who the persona is.
pth trade-off** — table guarantees all 12 personas and tiers
  are present; prose rationale guarantees non-trivial depth; both together eliminate the trade-off
- **C-13 is a depth upgrade over C-08** — C-08 requires non-trivial rationale; C-13 requires causal
  rationale that names a feature property or gap as the mechanism, not just the persona's context

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
