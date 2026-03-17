Written to `simulations/quest/variations/scout-market-variations-R2-2026-03-14.md`.

---

## Round 2 — 5 Variations

| V | Axis | Base | Key change | Predicted score |
|---|------|------|-----------|-----------------|
| **V-01** | Revenue model standalone (post-ranking) | V-03 R1 | PM: REVENUE MODEL section after COMPOSITE RANK; one table, one price-point mandate | 97.5 |
| **V-02** | Revenue model per segment card | V-05 R1 | Revenue model + price point as pre-printed fields in every card | 100 |
| **V-03** | Revenue model at declaration (Strategy-owned) | V-01 R1 | Revenue model column in SEGMENT IDENTIFICATION; PRICE POINTS section before scoring | 92.5 |
| **V-04** | Revenue model at declaration + phrasing register (conversational) | V-01 R1 | Same as V-03 but Socratic register — sections are questions, not imperatives | 92.5 |
| **V-05** | Full synthesis (path to 100) | V-05 R1 | Revenue model per card + revenue model in COMPOSITE RANK + quantified "Not building this means:" tied to STATUS QUO do-nothing cost | 100 |

**Key design decisions:**

- V-01 is the minimal-addition test: one table closes C-10 without touching V-03 R1's proven structure. If it reaches 97.5, that confirms the gap was purely the absent field.
- V-02 and V-05 are both predicted at 100. The structural question is whether V-02's minimal addition (two card fields) is sufficient or whether V-05's quantified C-12 is load-bearing. If they score identically, V-02 is the preferred golden candidate — same coverage, less overhead.
- V-03 and V-04 are controlled against each other to test phrasing register. If they score identically, register is confirmed neutral for market-sizing skills and drops from future axis exploration.
- V-05's `Not building this means:` is strengthened with a format requirement (`"costing approximately [$ or hrs from STATUS QUO]"`) — this chains C-12 to C-11, making both more robust together.
 gap |

**Predicted scores (v2 rubric):**

| V | C-09 | C-10 | C-11 | C-12 | Aspirational | Composite |
|---|------|------|------|------|--------------|-----------|
| V-01 | PASS | PASS | PASS | FAIL | 3/4 | 97.5 |
| V-02 | PASS | PASS | PASS | PASS | 4/4 | 100 |
| V-03 | PARTIAL | PASS | FAIL | FAIL | 1/4 | 92.5 |
| V-04 | PARTIAL | PASS | FAIL | FAIL | 1/4 | 92.5 |
| V-05 | PASS | PASS | PASS | PASS | 4/4 | 100 |

**R2 open questions:**
1. Does V-02 (revenue model per card, V-05 R1 base) reach 100, or does any criterion degrade?
2. Do V-03 and V-04 score identically? If so, phrasing register is confirmed neutral for
   market-sizing skills and can be dropped as a future axis.
3. Does V-01's standalone revenue table produce the C-09 price-model insight (free beachhead vs.
   high-WTP enterprise) at the same rate as V-02's per-card placement?

---

## V-01: Revenue Model Standalone Table

**Axis:** Revenue model placement -- dedicated PM: REVENUE MODEL section runs after COMPOSITE
RANK; one row per segment; at least one concrete price point or ARR target required; no other
changes to V-03 R1 structure
**Hypothesis:** V-03 R1 already passes C-09, C-11, and all essentials. The only missing
criterion is C-10. A standalone revenue model table is the minimal addition: placed post-ranking
so PM states monetization in context of the final rank order (beachhead first), which creates a
surface for the insight that the beachhead may warrant a free or freemium model despite lower
WTP -- potentially extending the C-09 surface. C-12 is absent (no "Not building this means:"
line), so this variation predicts 97.5.

```
You are running /scout:market. Fill in this structured template.
All section headers are fixed. STATUS QUO section runs before any segment scoring.
Do not reorder, rename, or remove any section header or template fragment.

---

## SETUP: TOPIC
Topic: [One sentence describing the feature or product being market-sized.]

## STATUS QUO: THE DO-NOTHING COMPETITOR
[Complete before any segment scoring. This baseline anchors pain severity and WTP scores below.]
[If behavior varies by segment, note the dominant pattern and flag exceptions.]

Current behavior: [What do target users do today without this product? One sentence per distinct behavior.]
Do-nothing cost: [Ongoing cost of current behavior. Estimate: hrs/wk per user, $ per year, or qualitative friction level.]
Switching trigger: [What event or threshold causes users to leave current behavior and adopt a new tool?]
Inertia anchor: [What makes users stay with current behavior. Name 1-2 specific anchors: e.g., "data already in spreadsheets", "procurement required for new tools", "existing workflow dependencies".]

## STRATEGY: SEGMENT IDENTIFICATION
[Identify 3-6 distinct addressable segments. Name each and describe in one sentence.]
[Tooling segments: use developer headcount. Platform/enterprise segments: use dollar TAM. Do not mix units within the same column.]

| Segment ID | Segment Name | Description | Unit Type |
|------------|--------------|-------------|-----------|
| S1 | [Name] | [One sentence.] | [devs / $TAM] |
| S2 | [Name] | [One sentence.] | [devs / $TAM] |
| S3 | [Name] | [One sentence.] | [devs / $TAM] |
[Add rows as needed. Minimum 3 segments, maximum 6.]

## STRATEGY: TAM/SAM/SOM
[Use units declared in SEGMENT IDENTIFICATION. Do not mix headcount and dollar TAM in the same column.]

| Segment ID | TAM | SAM | SOM | Unit |
|------------|-----|-----|-----|------|
| S1 | [N] | [N] | [N] | [devs / $M] |
| S2 | [N] | [N] | [N] | [devs / $M] |
| S3 | [N] | [N] | [N] | [devs / $M] |

## PM: FIT SCORING
[Score every segment. Scale: 1 (low) to 10 (high). Equal weights. Composite = (pain + WTP + accessibility) / 3.]
[Pain severity: reference STATUS QUO do-nothing cost -- segments where the cost is higher score higher on pain.]
[WTP: reference STATUS QUO switching trigger -- segments closer to the trigger score higher.]
[Accessibility: how reachable through existing channels?]
[All three columns required. Composite = arithmetic mean. Do not omit any dimension.]

| Segment ID | Pain Severity (1-10) | WTP (1-10) | Accessibility (1-10) | Fit Score (avg) |
|------------|---------------------|------------|----------------------|-----------------|
| S1 | [N] | [N] | [N] | [avg] |
| S2 | [N] | [N] | [N] | [avg] |
| S3 | [N] | [N] | [N] | [avg] |

## GTM: DIFFICULTY
[Rate GTM difficulty 1-10 (1 = easy, 10 = hard). Inertia anchor column required: name the
specific anchor from STATUS QUO or a segment-specific anchor that makes this segment hard to
reach. Segments with stronger anchors receive higher difficulty scores.]

| Segment ID | GTM Difficulty (1-10) | Inertia Anchor | Notes |
|------------|----------------------|----------------|-------|
| S1 | [N] | [Specific anchor from STATUS QUO or segment-specific.] | [Brief note.] |
| S2 | [N] | [Specific anchor.] | [Brief note.] |
| S3 | [N] | [Specific anchor.] | [Brief note.] |

## COMPOSITE RANK
[Rank score = Fit Score + (10 - GTM Difficulty). Show arithmetic. Sort descending by rank score.]

| Segment ID | Fit Score | GTM Difficulty | 10 - GTM | Rank Score | Rank |
|------------|-----------|----------------|----------|------------|------|
| S1 | [fit] | [gtm] | [10-gtm] | [fit + (10-gtm)] | [#] |
| S2 | [fit] | [gtm] | [10-gtm] | [fit + (10-gtm)] | [#] |
| S3 | [fit] | [gtm] | [10-gtm] | [fit + (10-gtm)] | [#] |

## PM: REVENUE MODEL
[State the revenue model for every segment. At least one segment must name a concrete price
point or ARR target -- do not leave all cells as TBD.]
[Revenue model types: free, freemium, seat license, usage-based, enterprise/custom, other.]
[Price point: specific $ amount (e.g., $12/seat/mo) OR ARR target (e.g., $50K ARR in Y1).]
[Note: the beachhead segment's revenue model informs sequencing -- a free entry model that locks
in methodology before monetization is a different strategic choice than a seat license.]

| Segment ID | Revenue Model | Price Point / ARR Target | Notes |
|------------|---------------|--------------------------|-------|
| S1 | [model type] | [$ or TBD] | [Optional note.] |
| S2 | [model type] | [$ or TBD] | [Optional note.] |
| S3 | [model type] | [$ or TBD] | [Optional note.] |
[At least one Price Point / ARR Target cell must contain a concrete value, not TBD.]

## BEACHHEAD RECOMMENDATION
Beachhead: [Segment ID and name.]
Rationale: [2-4 sentences. Address: (1) fit score, (2) GTM difficulty, (3) why this segment is
preferred over the highest-WTP segment, (4) how the STATUS QUO inertia anchor makes the
highest-WTP segment a worse entry point.]
Highest-WTP segment: [Segment ID and name.] WTP: [N]. Deferred because: [One sentence --
reference its inertia anchor or GTM difficulty score.]
Inertia note: [One sentence on how the beachhead choice is shaped by STATUS QUO inertia.]

## SEQUENCING PATH
Y1: [Segment ID] -- [Entry rationale -- cite inertia anchor strength if relevant.]
Y2+: [Segment ID] -- [Transition trigger -- what inertia barrier is resolved or what channel opens.]
Defer: [Segment ID(s)] -- [Deferral reason -- reference inertia anchor or GTM difficulty.]

## AMENDMENTS
1. [Concrete validation action. E.g., price-test WTP assumption for S1 with N discovery calls.]
[Additional actions optional.]

---

Write artifact: simulations/scout/market/{topic}-market-{date}.md
Frontmatter: skill, topic, date, beachhead_segment, beachhead_rank_score, highest_wtp_segment,
segments_count, status_quo_cost, inertia_anchor.
```

---

## V-02: Revenue Model Per Segment Card

**Axis:** Revenue model per-card field -- revenue model type and price point embedded in each
scoring card as pre-printed fields; no other changes to V-05 R1 structure
**Hypothesis:** Per-card placement eliminates the C-10 omission path the same way per-card PM
fields eliminated the C-03 omission path in R1. Model cannot skip a segment without leaving a
visibly blank field. Juxtaposition of WTP score and revenue model in the same card creates a
surface for the C-09 insight: a segment with high WTP and a seat-license model may rank below a
segment with moderate WTP and a free model because the latter has lower GTM difficulty. V-05 R1
already passes C-09/C-11/C-12; adding revenue model fields closes C-10. Predicted: 100.

```
You are running /scout:market. Fill in this structured template.
All section headers are fixed. STATUS QUO runs first. Strategy leads sizing. Per-segment cards
score fit, GTM, and revenue model. Do not reorder, rename, or remove any section header, card
header, or template fragment.

---

## SETUP: TOPIC
Topic: [One sentence describing the feature or product being market-sized.]

## STATUS QUO: THE DO-NOTHING COMPETITOR
[Complete before any segmentation. This baseline anchors pain severity and WTP scores in all
cards below.] [If behavior varies by segment, note the dominant pattern and flag exceptions.]

Current behavior: [What do target users do today without this product? One sentence per distinct behavior.]
Do-nothing cost: [Ongoing cost. Estimate: hrs/wk per user, $ per year, or qualitative friction level.]
Inertia anchor: [What makes users stay with current behavior. Name 1-2 specific anchors.]
Switching trigger: [What event causes users to adopt a new tool.]

## STRATEGY: SEGMENT IDENTIFICATION
[Identify 3-6 distinct addressable segments. Name each and describe in one sentence.]
[UNIT RULE: tooling segments use developer headcount (devs); platform/enterprise segments use
dollar TAM ($M). Declare unit per segment here. Carry this unit through all cards and tables --
do not change mid-table.]

| Segment ID | Segment Name | Description | Unit (devs / $M) |
|------------|--------------|-------------|------------------|
| S1 | [Name] | [One sentence.] | [devs / $M] |
| S2 | [Name] | [One sentence.] | [devs / $M] |
| S3 | [Name] | [One sentence.] | [devs / $M] |
[Add rows as needed. Minimum 3 segments, maximum 6.]

## STRATEGY: TAM/SAM/SOM
[Use the unit declared for each segment above. Do not change units mid-table.]
[This section must complete before scoring cards begin.]

| Segment ID | TAM | SAM | SOM | Unit |
|------------|-----|-----|-----|------|
| S1 | [N] | [N] | [N] | [from above] |
| S2 | [N] | [N] | [N] | [from above] |
| S3 | [N] | [N] | [N] | [from above] |

## PM + GTM: SEGMENT SCORING CARDS
[Fill one card per segment. All fields required. Reference STATUS QUO when scoring pain and WTP.
Do not omit rank score, revenue model, or price point fields -- all must appear in every card.
At least one card must name a concrete price point or ARR target (not TBD).]

### S1: [Segment Name]
PM -- Pain severity (1-10): [N] -- [Rationale; reference STATUS QUO do-nothing cost if applicable.]
PM -- WTP (1-10): [N] -- [Rationale; reference STATUS QUO switching trigger if applicable.]
PM -- Accessibility (1-10): [N] -- [Rationale.]
PM -- Fit score: ([pain] + [WTP] + [access]) / 3 = [avg]
PM -- Revenue model: [free / freemium / seat license / usage-based / enterprise / other]
PM -- Price point or ARR target: [$ concrete value, or "TBD -- validate in Phase X"]
GTM -- Difficulty (1-10): [N] -- [Rationale; name specific inertia anchor from STATUS QUO or
segment-specific. Do not leave blank.]
Rank score: [fit] + (10 - [gtm]) = [total]

### S2: [Segment Name]
PM -- Pain severity (1-10): [N] -- [Rationale; reference STATUS QUO if applicable.]
PM -- WTP (1-10): [N] -- [Rationale; reference STATUS QUO if applicable.]
PM -- Accessibility (1-10): [N] -- [Rationale.]
PM -- Fit score: ([pain] + [WTP] + [access]) / 3 = [avg]
PM -- Revenue model: [free / freemium / seat license / usage-based / enterprise / other]
PM -- Price point or ARR target: [$ concrete value, or "TBD -- validate in Phase X"]
GTM -- Difficulty (1-10): [N] -- [Rationale; name inertia anchor. Do not leave blank.]
Rank score: [fit] + (10 - [gtm]) = [total]

### S3: [Segment Name]
PM -- Pain severity (1-10): [N] -- [Rationale; reference STATUS QUO if applicable.]
PM -- WTP (1-10): [N] -- [Rationale; reference STATUS QUO if applicable.]
PM -- Accessibility (1-10): [N] -- [Rationale.]
PM -- Fit score: ([pain] + [WTP] + [access]) / 3 = [avg]
PM -- Revenue model: [free / freemium / seat license / usage-based / enterprise / other]
PM -- Price point or ARR target: [$ concrete value, or "TBD -- validate in Phase X"]
GTM -- Difficulty (1-10): [N] -- [Rationale; name inertia anchor. Do not leave blank.]
Rank score: [fit] + (10 - [gtm]) = [total]

[Add S4, S5, S6 cards for additional segments. Same format -- do not omit any field.]

## COMPOSITE RANK
[Copy rank scores from cards. Sort descending by rank score. Verify arithmetic matches cards.]

| Rank | Segment ID | Segment Name | Fit Score | GTM Difficulty | Rank Score |
|------|------------|--------------|-----------|----------------|------------|
| 1 | [ID] | [Name] | [fit] | [gtm] | [rank] |
| 2 | [ID] | [Name] | [fit] | [gtm] | [rank] |
| 3 | [ID] | [Name] | [fit] | [gtm] | [rank] |
[Rank 1 = highest rank score. Mirror all segments.]

## PM: BEACHHEAD RECOMMENDATION
Beachhead: [Segment ID and name.]
Fit score: [N] | GTM difficulty: [N] | Rank score: [N]
Rationale: [2-4 sentences. Address: (1) fit score, (2) GTM difficulty, (3) why this segment is
preferred over the highest-WTP segment, (4) how STATUS QUO inertia shapes this choice.]
Highest-WTP segment: [Segment ID and name.] WTP: [N]. Deferred because: [One sentence --
reference its inertia anchor or GTM difficulty score.]
Not building this means: [What users continue doing. Reference STATUS QUO do-nothing cost.
Do not omit this line.]

## GTM: SEQUENCING PATH
Y1: [Segment ID] -- [Entry rationale -- cite inertia anchor strength if relevant.]
Y2+: [Segment ID] -- [Transition trigger -- name what inertia barrier is resolved or what channel opens.]
Defer: [Segment ID(s)] -- [Deferral reason -- reference inertia anchor or GTM difficulty score.]

## AMENDMENTS
[1+ concrete next steps to validate or refine this analysis.]
1. [Validation action. E.g., test WTP assumption for S1 with N discovery calls.]
[Additional actions optional.]

---

Write artifact: simulations/scout/market/{topic}-market-{date}.md
Frontmatter: skill, topic, date, beachhead_segment, beachhead_rank_score, highest_wtp_segment,
segments_count, status_quo_cost, inertia_anchor.
```

---

## V-03: Revenue Model at Declaration (Strategy-Owned)

**Axis:** Revenue model at declaration -- Strategy declares revenue model type during SEGMENT
IDENTIFICATION via a revenue model column; price points captured in a dedicated STRATEGY: PRICE
POINTS section after segmentation; no STATUS QUO section; consolidated tables (no per-segment
cards)
**Hypothesis:** Revenue model is a market structure decision, not a scoring artifact. Declaring
it at segmentation forces Strategy to commit before fit scoring biases the choice -- a segment
identified as "enterprise platform buyers" carries a seat-license or custom model before any WTP
score is assigned. Revenue model conflicts become visible early: a beachhead with a free model
will have lower WTP than an enterprise segment, but that may be structurally correct. C-10
passes structurally. C-11 and C-12 are absent (no STATUS QUO, no inaction line). This is an
isolation test: does early revenue model declaration alone reach a useful score, or does the
absence of inertia framing cap it at 92.5?

```
You are running /scout:market. Fill in this structured template.
All section headers are fixed. Strategy leads with segment identification and market sizing.
Do not reorder, rename, or remove any section header or template fragment.

---

## SETUP: TOPIC
Topic: [One sentence describing the feature or product being market-sized.]

## STRATEGY: SEGMENT IDENTIFICATION
[Identify 3-6 distinct addressable segments. Name each and describe in one sentence.]
[Tooling segments: use developer headcount. Platform/enterprise segments: use dollar TAM.
Do not mix units within the same column.]
[Revenue model: declare the intended monetization model for each segment at identification time.
Revenue model types: free, freemium, seat license, usage-based, enterprise/custom, other.]

| Segment ID | Segment Name | Description | Unit Type | Revenue Model |
|------------|--------------|-------------|-----------|---------------|
| S1 | [Name] | [One sentence.] | [devs / $TAM] | [model type] |
| S2 | [Name] | [One sentence.] | [devs / $TAM] | [model type] |
| S3 | [Name] | [One sentence.] | [devs / $TAM] | [model type] |
[Add rows as needed. Minimum 3 segments, maximum 6.]

## STRATEGY: PRICE POINTS
[State a price point or ARR target for each segment. At least one must be a concrete value.
Mark segments where a concrete value is not yet known as TBD with a validation action.]

| Segment ID | Price Point / ARR Target | Validation action if TBD |
|------------|--------------------------|--------------------------|
| S1 | [$ or TBD] | [Validation action if TBD; otherwise leave blank.] |
| S2 | [$ or TBD] | [Validation action if TBD; otherwise leave blank.] |
| S3 | [$ or TBD] | [Validation action if TBD; otherwise leave blank.] |
[At least one Price Point / ARR Target must be a concrete number, not TBD.]

## STRATEGY: TAM/SAM/SOM
[Use units declared in SEGMENT IDENTIFICATION. Do not mix headcount and dollar TAM in the
same column.]

| Segment ID | TAM | SAM | SOM | Unit |
|------------|-----|-----|-----|------|
| S1 | [N] | [N] | [N] | [devs / $M] |
| S2 | [N] | [N] | [N] | [devs / $M] |
| S3 | [N] | [N] | [N] | [devs / $M] |

## PM: FIT SCORING
[Score every segment on three dimensions. Scale: 1 (low) to 10 (high). Equal weights.
Composite = (pain + WTP + accessibility) / 3. Round to one decimal place.]
[Pain severity: how acute is the unmet need? WTP: willingness to pay. Accessibility: reachable
via existing channels?]
[All three columns required. Composite must be the arithmetic mean -- do not omit any dimension.]

| Segment ID | Pain Severity (1-10) | WTP (1-10) | Accessibility (1-10) | Fit Score (avg) |
|------------|---------------------|------------|----------------------|-----------------|
| S1 | [N] | [N] | [N] | [avg] |
| S2 | [N] | [N] | [N] | [avg] |
| S3 | [N] | [N] | [N] | [avg] |

## GTM: DIFFICULTY
[Rate GTM difficulty for each segment on a 1-10 scale (1 = easy to reach, 10 = hard).
Consider: channel access, sales cycle length, procurement complexity, competitive entrenchment.]

| Segment ID | GTM Difficulty (1-10) | Notes |
|------------|----------------------|-------|
| S1 | [N] | [Brief rationale.] |
| S2 | [N] | [Brief rationale.] |
| S3 | [N] | [Brief rationale.] |

## STRATEGY: COMPOSITE RANK
[Rank score = Fit Score + (10 - GTM Difficulty). Apply to every segment. Show arithmetic.
Sort descending by rank score.]

| Segment ID | Fit Score | GTM Difficulty | 10 - GTM | Rank Score | Rank |
|------------|-----------|----------------|----------|------------|------|
| S1 | [fit] | [gtm] | [10-gtm] | [fit + (10-gtm)] | [#] |
| S2 | [fit] | [gtm] | [10-gtm] | [fit + (10-gtm)] | [#] |
| S3 | [fit] | [gtm] | [10-gtm] | [fit + (10-gtm)] | [#] |
[Rank 1 = highest rank score. Verify rank column matches descending rank score order.]

## PM: BEACHHEAD RECOMMENDATION
Beachhead segment: [Segment ID and name.]
Revenue model: [Copy from SEGMENT IDENTIFICATION.]
Rationale: [2-4 sentences. Must address: (1) fit score, (2) GTM difficulty, (3) why this
segment is preferred over the highest-WTP segment. Explicitly name the highest-WTP segment and
explain why it is deferred. Note whether the beachhead's revenue model is consistent with its
rank score rationale (e.g., free model enables low-friction entry despite lower WTP).]
Highest-WTP segment: [Segment ID and name.] WTP: [N]. Deferred because: [One sentence.]

## GTM: SEQUENCING PATH
Y1 target: [Segment ID] -- [One sentence: why this is the right entry point.]
Y2 expansion: [Segment ID] -- [One sentence: what unlocks this transition.]
Y3+ or defer: [Segment ID(s)] -- [One sentence: why these come last or are deferred.]

## AMENDMENTS
[List 1+ concrete next steps to validate or refine this analysis.]
1. [Open question or validation action. E.g., price-test the WTP assumption for S1 with N
interviews. Or: validate revenue model choice for S2 against procurement constraints.]
[Additional actions optional.]

---

Write artifact: simulations/scout/market/{topic}-market-{date}.md
Frontmatter: skill, topic, date, beachhead_segment, beachhead_rank_score, highest_wtp_segment,
segments_count.
```

---

## V-04: Revenue Model at Declaration + Phrasing Register (Conversational)

**Axes:** Revenue model at declaration (V-03 axis) + phrasing register (conversational /
Socratic -- sections framed as questions the role is answering, not imperatives to fill)
**Hypothesis:** Phrasing register was not tested in R1. The rubric has no criterion sensitive to
formal vs. conversational language -- all criteria test structure and arithmetic. This variation
tests whether a conversational register preserves the same structural coverage as V-03's
technical-imperative or introduces omission risk when instructions are framed as questions.
Revenue model at declaration is carried over from V-03 to isolate the register effect. If V-04
and V-03 score identically, register is confirmed neutral for market-sizing skills. If V-04
underperforms, conversational framing introduces structural risk worth characterizing.

```
You are running /scout:market. Work through the following questions in order.
Each role (Strategy, PM, GTM) answers its questions in sequence.
Fill every table and field. Do not skip a question or leave a table incomplete.

---

## What are we sizing?

Topic: [One sentence describing the feature or product being market-sized.]

---

## Strategy: Who are the addressable segments?

Name 3-6 distinct segments. For each, answer: who are they, what unit best measures their
size (developer headcount for tooling; dollar TAM for platform/enterprise), and what
monetization model fits them?

Do not mix developer headcount and dollar TAM in the same table column.

| Segment ID | Segment Name | Who are they? | Unit | Revenue model |
|------------|--------------|---------------|------|---------------|
| S1 | [Name] | [One sentence.] | [devs / $TAM] | [free / freemium / seat / usage / enterprise] |
| S2 | [Name] | [One sentence.] | [devs / $TAM] | [free / freemium / seat / usage / enterprise] |
| S3 | [Name] | [One sentence.] | [devs / $TAM] | [free / freemium / seat / usage / enterprise] |
[Add S4-S6 as needed.]

## Strategy: What does each segment pay?

For each segment, state the most credible price point or ARR target.
At least one segment must name a concrete number -- not all cells may be TBD.

| Segment ID | Price point / ARR target | How confident? |
|------------|--------------------------|----------------|
| S1 | [$ or TBD] | [high / medium / low -- note validation needed if TBD] |
| S2 | [$ or TBD] | [high / medium / low] |
| S3 | [$ or TBD] | [high / medium / low] |

## Strategy: How large is each segment?

For each segment, estimate TAM (total addressable), SAM (serviceable), and SOM (realistic Y1-Y2
share). Use the unit from the segment table above. Do not mix units mid-column.

| Segment ID | TAM | SAM | SOM | Unit |
|------------|-----|-----|-----|------|
| S1 | | | | [from above] |
| S2 | | | | [from above] |
| S3 | | | | [from above] |

---

## PM: How much does each segment need this?

Score each segment on three dimensions (1 = low, 10 = high). Equal weights.
Composite fit score = (pain + WTP + accessibility) / 3. Show the arithmetic.

Pain severity: how acute is the unmet need today?
WTP: how willing are they to pay for a solution?
Accessibility: how reachable are they through channels you already have?

All three scores required per segment. Composite is the arithmetic mean -- do not weight
unevenly or drop a dimension.

| Segment ID | Pain (1-10) | WTP (1-10) | Access (1-10) | Fit score |
|------------|-------------|------------|---------------|-----------|
| S1 | | | | ([P]+[W]+[A])/3 = |
| S2 | | | | ([P]+[W]+[A])/3 = |
| S3 | | | | ([P]+[W]+[A])/3 = |

---

## GTM: How hard is each segment to reach?

Rate GTM difficulty for each segment (1 = easy, 10 = hard).
Think about: channel access, sales cycle, procurement complexity, and how entrenched current
solutions are.

| Segment ID | GTM difficulty (1-10) | What makes it hard? |
|------------|----------------------|---------------------|
| S1 | | [One sentence.] |
| S2 | | [One sentence.] |
| S3 | | [One sentence.] |

---

## Strategy: Which segment should we enter first?

Rank score = fit score + (10 - GTM difficulty). Show the arithmetic. Sort highest to lowest.

| Segment ID | Fit score | GTM difficulty | 10 - GTM | Rank score | Rank |
|------------|-----------|----------------|----------|------------|------|
| S1 | | | | | |
| S2 | | | | | |
| S3 | | | | | |
[Rank 1 = highest rank score.]

---

## PM: What is the beachhead recommendation?

Beachhead segment: [Segment ID and name.]
Revenue model: [Copy from segment table.]
Rationale: [2-4 sentences. Address: (a) why this segment's fit score and GTM difficulty justify
it as the entry point, (b) why the highest-WTP segment is deferred despite its higher WTP score,
(c) whether the beachhead revenue model is consistent with a low-friction entry strategy.]
Highest-WTP segment: [Segment ID and name.] WTP score: [N]. Why deferred: [One sentence.]

---

## GTM: What is the expansion sequence?

Y1 -- enter: [Segment ID] -- [Why start here?]
Y2+ -- expand: [Segment ID] -- [What has to be true before expanding?]
Defer: [Segment ID(s)] -- [Why last or never?]

---

## What do we need to validate?

List 1+ concrete next steps. These should be falsifiable: a test, an interview set, a price
experiment, or a segment disaggregation.

1. [Validation action.]
[Additional actions optional.]

---

Write artifact: simulations/scout/market/{topic}-market-{date}.md
Frontmatter: skill, topic, date, beachhead_segment, beachhead_rank_score, highest_wtp_segment,
segments_count.
```

---

## V-05: Full Synthesis (Path to 100)

**Axes:** V-05 R1 (STATUS QUO + Strategy-first sizing + per-segment cards + inertia anchor +
"Not building this means:") + revenue model per card (C-10) + quantified inaction cost at
beachhead (C-12 strengthening)
**Hypothesis:** V-05 R1 scored 97.5 (C-09/C-11/C-12 pass, C-10 fail under v2 rubric). Adding
the revenue model field to every scoring card eliminates the C-10 omission path (per-card,
same structural guarantee as C-03). Extending "Not building this means:" with a quantified
cost tied back to STATUS QUO do-nothing cost makes C-12 less fragile: the pass condition now
requires a traceable number, not a generic qualitative claim. Revenue model column added to
COMPOSITE RANK table for visibility at the ranking stage. All four aspirational criteria have
structural scaffolding. Predicted: 100.

```
You are running /scout:market. Fill in this structured template.
All section headers are fixed. STATUS QUO runs first. Strategy leads sizing. Per-segment cards
score fit, GTM, and revenue model. Do not reorder, rename, or remove any section header, card
header, or template fragment.

---

## SETUP: TOPIC
Topic: [One sentence describing the feature or product being market-sized.]

## STATUS QUO: THE DO-NOTHING COMPETITOR
[Complete before any segmentation. This baseline anchors pain severity, WTP scores, and the
"Not building this means:" statement at the beachhead. If behavior varies by segment, note the
dominant pattern and flag exceptions per card.]

Current behavior: [What do target users do today without this product? One sentence per distinct behavior.]
Do-nothing cost: [Quantify: hrs/wk per user, $ per year, or a measurable friction level. This
value will be referenced in "Not building this means:" -- do not write a vague estimate here.]
Inertia anchor: [What makes users stay with current behavior. Name 1-2 specific anchors that
will appear in segment cards below.]
Switching trigger: [What event or threshold causes users to adopt a new tool.]

## STRATEGY: SEGMENT IDENTIFICATION
[Identify 3-6 distinct addressable segments. Name each and describe in one sentence.]
[UNIT RULE: tooling segments use developer headcount (devs); platform/enterprise segments use
dollar TAM ($M). Declare unit per segment here. Carry this unit through all cards and tables --
do not change mid-table.]

| Segment ID | Segment Name | Description | Unit (devs / $M) |
|------------|--------------|-------------|------------------|
| S1 | [Name] | [One sentence.] | [devs / $M] |
| S2 | [Name] | [One sentence.] | [devs / $M] |
| S3 | [Name] | [One sentence.] | [devs / $M] |
[Add rows as needed. Minimum 3 segments, maximum 6.]

## STRATEGY: TAM/SAM/SOM
[Use the unit declared for each segment above. Do not change units mid-table.]
[This section must complete before scoring cards begin.]

| Segment ID | TAM | SAM | SOM | Unit |
|------------|-----|-----|-----|------|
| S1 | [N] | [N] | [N] | [from above] |
| S2 | [N] | [N] | [N] | [from above] |
| S3 | [N] | [N] | [N] | [from above] |

## PM + GTM: SEGMENT SCORING CARDS
[Fill one card per segment. All fields required. Reference STATUS QUO when scoring pain and WTP.
Do not omit rank score, revenue model, or price point -- all must appear in every card.
At least one card must name a concrete price point or ARR target (not TBD).]

### S1: [Segment Name]
PM -- Pain severity (1-10): [N] -- [Rationale; reference STATUS QUO do-nothing cost if applicable.]
PM -- WTP (1-10): [N] -- [Rationale; reference STATUS QUO switching trigger if applicable.]
PM -- Accessibility (1-10): [N] -- [Rationale.]
PM -- Fit score: ([pain] + [WTP] + [access]) / 3 = [avg]
PM -- Revenue model: [free / freemium / seat license / usage-based / enterprise / other]
PM -- Price point or ARR target: [$ concrete value, or "TBD -- validate in Phase X"]
GTM -- Difficulty (1-10): [N] -- [Rationale; name specific inertia anchor from STATUS QUO or
segment-specific. Do not leave blank.]
Rank score: [fit] + (10 - [gtm]) = [total]

### S2: [Segment Name]
PM -- Pain severity (1-10): [N] -- [Rationale; reference STATUS QUO if applicable.]
PM -- WTP (1-10): [N] -- [Rationale; reference STATUS QUO if applicable.]
PM -- Accessibility (1-10): [N] -- [Rationale.]
PM -- Fit score: ([pain] + [WTP] + [access]) / 3 = [avg]
PM -- Revenue model: [free / freemium / seat license / usage-based / enterprise / other]
PM -- Price point or ARR target: [$ concrete value, or "TBD -- validate in Phase X"]
GTM -- Difficulty (1-10): [N] -- [Rationale; name inertia anchor. Do not leave blank.]
Rank score: [fit] + (10 - [gtm]) = [total]

### S3: [Segment Name]
PM -- Pain severity (1-10): [N] -- [Rationale; reference STATUS QUO if applicable.]
PM -- WTP (1-10): [N] -- [Rationale; reference STATUS QUO if applicable.]
PM -- Accessibility (1-10): [N] -- [Rationale.]
PM -- Fit score: ([pain] + [WTP] + [access]) / 3 = [avg]
PM -- Revenue model: [free / freemium / seat license / usage-based / enterprise / other]
PM -- Price point or ARR target: [$ concrete value, or "TBD -- validate in Phase X"]
GTM -- Difficulty (1-10): [N] -- [Rationale; name inertia anchor. Do not leave blank.]
Rank score: [fit] + (10 - [gtm]) = [total]

[Add S4, S5, S6 cards for additional segments. Same format -- do not omit any field.]

## COMPOSITE RANK
[Copy rank scores from cards. Sort descending by rank score. Verify arithmetic matches cards.
Revenue model column included -- copy from cards.]

| Rank | Segment ID | Segment Name | Fit Score | GTM Difficulty | Revenue Model | Rank Score |
|------|------------|--------------|-----------|----------------|---------------|------------|
| 1 | [ID] | [Name] | [fit] | [gtm] | [model] | [rank] |
| 2 | [ID] | [Name] | [fit] | [gtm] | [model] | [rank] |
| 3 | [ID] | [Name] | [fit] | [gtm] | [model] | [rank] |
[Rank 1 = highest rank score. Mirror all segments.]

## PM: BEACHHEAD RECOMMENDATION
Beachhead: [Segment ID and name.]
Fit score: [N] | GTM difficulty: [N] | Rank score: [N] | Revenue model: [model type]
Rationale: [2-4 sentences. Address: (1) fit score, (2) GTM difficulty, (3) why this segment is
preferred over the highest-WTP segment, (4) how STATUS QUO inertia shapes this choice, (5) why
the beachhead revenue model is the right entry-point monetization strategy.]
Highest-WTP segment: [Segment ID and name.] WTP: [N]. Deferred because: [One sentence --
reference its inertia anchor or GTM difficulty score.]
Not building this means: [What users continue doing AND a quantified cost tied to STATUS QUO
do-nothing cost. Format: "Users continue [behavior], costing approximately [$ or hrs from
STATUS QUO]. Every [quarter / year] of delay = [estimated ongoing waste or lost capture]."
Do not write a generic statement. Do not omit this line.]

## GTM: SEQUENCING PATH
Y1: [Segment ID] -- [Entry rationale -- cite inertia anchor strength and revenue model fit.]
Y2+: [Segment ID] -- [Transition trigger -- what inertia barrier resolves or what channel opens.]
Defer: [Segment ID(s)] -- [Deferral reason -- reference inertia anchor, GTM difficulty, or
revenue model mismatch with current stage.]

## AMENDMENTS
[1+ concrete next steps to validate or refine this analysis.]
1. [Validation action. E.g., test WTP assumption for S1 with N discovery calls; or price-test
the beachhead price point against N comparable tools.]
[Additional actions optional.]

---

Write artifact: simulations/scout/market/{topic}-market-{date}.md
Frontmatter: skill, topic, date, beachhead_segment, beachhead_rank_score, highest_wtp_segment,
segments_count, status_quo_cost, inertia_anchor.
```

---

## Round 2 Design Notes

### Axis selection rationale

Three single-axis variations test revenue model placement: post-ranking standalone table (V-01),
per-segment card (V-02), and at-declaration Strategy column (V-03). These are the three
structurally distinct positions for C-10 content. Testing all three identifies which placement
produces the fewest omissions and the strongest C-09 surface at the lowest template overhead.

Phrasing register (V-04) is a fresh axis not explored in R1. The rubric has no register-sensitive
criterion. V-04 is a robustness test against V-03: if the conversational/Socratic framing
preserves the same score, register is confirmed neutral and can be eliminated from future axis
exploration. If V-04 underperforms, the failure mode characterizes the structural risk.

Lifecycle emphasis was not chosen as a single-axis variation. R1 confirmed that phase sequence
(identify -> size -> score -> rank -> recommend) is robust without explicit gates; the "This
section must complete before..." instruction is sufficient enforcement at zero overhead.

### C-10 structural comparison across R2 variations

| V | C-10 mechanism | Omission path |
|---|----------------|---------------|
| V-01 | Standalone table after COMPOSITE RANK | Possible if model truncates output after ranking |
| V-02 | Pre-printed per-card field (same as C-03 in R1) | No omission path -- field must be filled |
| V-03 | Column in SEGMENT IDENTIFICATION table | Low risk; declared before any scoring begins |
| V-04 | Column in Socratic segment question table | Moderate risk; conversational framing may elicit prose instead of table |
| V-05 | Pre-printed per-card field + COMPOSITE RANK column | No omission path -- appears twice |

### C-12 strengthening in V-05 vs. V-05 R1

V-05 R1's "Not building this means:" line was pre-printed but allowed qualitative completion
("Users continue doing X manually"). V-05 R2 extends the instruction with a format requirement:
"costing approximately [$ or hrs from STATUS QUO]" and "every [quarter/year] of delay =
[estimated waste]." This ties the C-12 pass condition to the C-11 input (STATUS QUO do-nothing
cost), making C-12 structurally dependent on C-11 being filled -- a chain that makes both more
robust together.

### Predicted score comparison: V-02 vs. V-05

V-02 and V-05 are both predicted to reach 100. The key difference:
- V-02 predicts 100 by minimal addition (two fields per card to V-05 R1 -- the known winner)
- V-05 predicts 100 by maximum reinforcement (same + quantified C-12 + revenue model in rank table)

If both reach 100, V-02 is the preferred golden candidate (simpler, same coverage). If V-05
reaches 100 and V-02 does not (e.g., C-12 fails because "Not building this means:" is weaker
without the format instruction), then the quantification extension in V-05 is load-bearing.
