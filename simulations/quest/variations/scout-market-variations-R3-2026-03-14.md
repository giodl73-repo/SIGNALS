Written to `simulations/quest/variations/scout-market-variations-R3-2026-03-14.md`.

---

## Round 3 -- 5 Variations

| V | Axis | Base | Predicted score |
|---|------|------|-----------------|
| **V-01** | C-13 table format | R2-V-01 structure | 100 (C-13 is the swing criterion) |
| **V-02** | C-14 explicit inertia-break trigger | R2-V-02 | 100 |
| **V-03** | No STATUS QUO (isolation test) | R2-V-02 | 95 |
| **V-04** | Table format + explicit C-14 (combined) | V-01 + V-02 axes | 100 (C-13 swing) |
| **V-05** | Condensed V-02 R2 (golden candidate) | R2-V-02 + R2-V-05 | 100 |

**Predicted scores under v3 rubric:**

| V | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | Asp | Composite |
|---|------|------|------|------|------|------|-----|-----------|
| V-01 | PASS | PASS | PASS | PASS | PASS* | PASS | 6/6 | 100 |
| V-02 | PASS | PASS | PASS | PASS | PASS | PASS | 6/6 | 100 |
| V-03 | PASS | PASS | FAIL | FAIL | PASS | FAIL | 3/6 | 95 |
| V-04 | PASS | PASS | PASS | PASS | PASS* | PASS | 6/6 | 100 |
| V-05 | PASS | PASS | PASS | PASS | PASS | PASS | 6/6 | 100 |

*C-13 is the primary test for V-01 and V-04. Predicted PASS via table row adjacency, but this is the key open question.

**What R3 resolves:**

1. **C-13 table format** -- Does `| WTP | Revenue Model | Price Point |` in the same table row satisfy "alongside the fit scoring view," or is per-card vertical proximity load-bearing? V-01 and V-04 are the controlled test. If they reach 100, table-based layout is a valid path. If they hit 98.3, per-card structure is the only C-13 guarantee.

2. **C-14 explicit mandate** -- R2-V-02's "transition trigger -- what inertia barrier is resolved" already passed C-14. V-02 and V-05 make it explicit: pre-printed `Inertia-break condition:` field with "must cite named STATUS QUO anchor, not a time period." If they score identically to R2-V-02, the mandate is confirmed redundant. If stronger, it's load-bearing.

3. **STATUS QUO gate count** -- V-03 predicts three aspirational criteria gate on STATUS QUO: C-11, C-12, C-14. The three that don't (C-09, C-10, C-13) are all structural/coverage -- they pass via per-card co-location regardless of baseline analysis.

4. **Golden candidate consolidation** -- V-05 is the target production template: V-02 R2 structure + quantified C-12 chain (V-05 R2 style) + explicit C-14 trigger + condensed instructions. If it reaches 100 cleanly, it becomes the candidate for promotion.
able axes (C-13 table + C-14 explicit trigger). If V-01 passes C-13 via
  table co-location, V-04 is the table-based path to 100 -- no per-segment cards required.

- V-05 is the golden candidate consolidation: takes R2-V-02 (first 100), adds V-05 R2 C-12
  quantification chain, adds V-02 R3 explicit C-14 trigger, removes verbose redundant guidance.
  Goal: cleanest possible 100-scoring template for production use.

**Predicted scores under v3 rubric:**

| V | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | Asp | Composite |
|---|------|------|------|------|------|------|-----|-----------|
| V-01 | PASS | PASS | PASS | PASS | PASS* | PASS | 6/6 | 100 |
| V-02 | PASS | PASS | PASS | PASS | PASS | PASS | 6/6 | 100 |
| V-03 | PASS | PASS | FAIL | FAIL | PASS | FAIL | 3/6 | 95 |
| V-04 | PASS | PASS | PASS | PASS | PASS* | PASS | 6/6 | 100 |
| V-05 | PASS | PASS | PASS | PASS | PASS | PASS | 6/6 | 100 |

*C-13 is the primary test axis for V-01 and V-04. Predicted PASS (table row co-location satisfies
"alongside or within the fit scoring view") but this is the key open question for R3. If C-13
FAIL: V-01 = 98.3, V-04 = 98.3.

**R3 open questions:**
1. Does a wide scoring table (WTP -> Revenue Model -> Price Point as adjacent columns) satisfy
   C-13, or does C-13 require per-card vertical proximity?
2. Does an explicit "Inertia-break condition:" mandate in sequencing improve C-14 structural
   guarantee beyond R2-V-02's "transition trigger" field?
3. How many aspirational criteria fail when STATUS QUO is removed? (C-11, C-14 FAIL confirmed;
   C-12 FAIL predicted -- does the "estimated" pass condition in C-12 save it without STATUS QUO?)

---

## V-01: Unified Scoring Table with Adjacent Revenue Model Columns

**Axis:** Output format -- wide unified table merges PM fit scoring and GTM difficulty into one
view; revenue model and price point columns placed adjacent to WTP column; no per-segment cards
**Hypothesis:** C-13 pass condition says "alongside (or within) the fit scoring view for that
segment." In a table row, WTP (col 3) and Revenue Model (col 4) are adjacent columns for the
same segment -- the comparison is visible without cross-referencing. This is as co-located as
per-card adjacent lines. If C-13 passes via table co-location, this variation is a simpler path
to 100 that avoids per-card overhead. C-14 uses the same "transition trigger -- what inertia
barrier is resolved" field as R2-V-02, which confirmed C-14 pass. STATUS QUO and "Not building
this means:" preserved from R2-V-02. Predicted: 100 (C-13 is the swing criterion).

```
You are running /scout:market. Fill in this structured template.
All section headers are fixed. STATUS QUO runs first. Revenue model and price point appear in
the unified scoring table adjacent to WTP -- not in a separate section. Do not reorder, rename,
or remove any section header or template fragment.

---

## SETUP: TOPIC
Topic: [One sentence describing the feature or product being market-sized.]

## STATUS QUO: THE DO-NOTHING COMPETITOR
[Complete before any segment scoring. This baseline anchors pain severity, WTP scores, and the
"Not building this means:" statement at the beachhead. If behavior varies by segment, note the
dominant pattern and flag exceptions in the scoring table.]

Current behavior: [What do target users do today without this product? One sentence per distinct behavior.]
Do-nothing cost: [Ongoing cost of current behavior. Estimate: hrs/wk per user, $ per year, or
qualitative friction level.]
Inertia anchor: [What makes users stay with current behavior. Name 1-2 specific anchors: e.g.,
"data already in spreadsheets", "procurement required for new tools", "existing workflow
dependencies".]
Switching trigger: [What event or threshold causes users to adopt a new tool.]

## STRATEGY: SEGMENT IDENTIFICATION
[Identify 3-6 distinct addressable segments. Name each and describe in one sentence.]
[UNIT RULE: tooling segments use developer headcount (devs); platform/enterprise segments use
dollar TAM ($M). Declare unit per segment here. Do not mix units within the same column.]

| Segment ID | Segment Name | Description | Unit (devs / $M) |
|------------|--------------|-------------|------------------|
| S1 | [Name] | [One sentence.] | [devs / $M] |
| S2 | [Name] | [One sentence.] | [devs / $M] |
| S3 | [Name] | [One sentence.] | [devs / $M] |
[Add rows as needed. Minimum 3 segments, maximum 6.]

## STRATEGY: TAM/SAM/SOM
[Use the unit declared for each segment above. Do not change units mid-table.]

| Segment ID | TAM | SAM | SOM | Unit |
|------------|-----|-----|-----|------|
| S1 | [N] | [N] | [N] | [from above] |
| S2 | [N] | [N] | [N] | [from above] |
| S3 | [N] | [N] | [N] | [from above] |

## PM + GTM: UNIFIED SCORING TABLE
[Score every segment. Revenue model and price point appear in this table adjacent to WTP -- they
do not appear in a separate section. Adjacent columns make WTP-vs-revenue-model comparison
visible in a single row without cross-referencing. At least one segment must show a concrete
price point, not TBD.]
[Pain: reference STATUS QUO do-nothing cost. WTP: reference STATUS QUO switching trigger.]
[Accessibility: how reachable through existing channels?]
[Fit score = (pain + WTP + accessibility) / 3. Round to one decimal. Show arithmetic in Notes.]
[GTM: name the specific inertia anchor from STATUS QUO or a segment-specific anchor. Do not
leave blank. Rank score = fit + (10 - GTM difficulty).]

| Seg | Pain (1-10) | WTP (1-10) | Revenue Model | Price Point | Access (1-10) | Fit Score | GTM (1-10) | Inertia Anchor | Rank Score |
|-----|-------------|------------|---------------|-------------|---------------|-----------|------------|----------------|------------|
| S1 | [N] | [N] | [model type] | [$ or TBD] | [N] | [avg] | [N] | [named anchor] | [fit+(10-gtm)] |
| S2 | [N] | [N] | [model type] | [$ or TBD] | [N] | [avg] | [N] | [named anchor] | [fit+(10-gtm)] |
| S3 | [N] | [N] | [model type] | [$ or TBD] | [N] | [avg] | [N] | [named anchor] | [fit+(10-gtm)] |
[At least one Price Point cell must contain a concrete value, not TBD.]
[Notes: show fit score arithmetic per segment -- ([pain]+[WTP]+[access])/3 = [avg].]

## COMPOSITE RANK
[Copy rank scores from scoring table. Sort descending by rank score. Revenue model column
included -- copy from scoring table.]

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
preferred over the highest-WTP segment, (4) how STATUS QUO inertia shapes this choice.]
Highest-WTP segment: [Segment ID and name.] WTP: [N]. Deferred because: [One sentence --
reference its inertia anchor or GTM difficulty score.]
Not building this means: [What users continue doing. Reference STATUS QUO do-nothing cost.
Do not omit this line.]

## GTM: SEQUENCING PATH
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

## V-02: Explicit C-14 Inertia-Break Trigger

**Axis:** Inertia framing -- sequencing PATH restructured with pre-printed `Inertia-break
condition:` field per Y2+ transition; must cite named STATUS QUO anchor, not a time period;
all other structure identical to R2-V-02
**Hypothesis:** R2-V-02 passes C-14 via "Transition trigger -- what inertia barrier is resolved
or what channel opens." The trigger field nudges the model toward an inertia-break condition but
does not mandate it -- "Year 2 when adoption grows" technically answers "what channel opens"
without citing a STATUS QUO anchor. R3-V-02 forecloses this: the pre-printed field is labeled
"Inertia-break condition:" and the instruction states "must cite the named anchor from STATUS
QUO -- not a time period." If R3-V-02 and R2-V-02 score identically, the explicit mandate is
confirmed redundant (trigger field is already deterministic in practice). If V-02 shows stronger
structural guarantee, the mandate is load-bearing for edge cases.

```
You are running /scout:market. Fill in this structured template.
All section headers are fixed. STATUS QUO runs first. Strategy leads sizing. Per-segment cards
score fit, GTM, and revenue model. Sequencing transitions must cite named conditions from
STATUS QUO inertia analysis -- not time periods. Do not reorder, rename, or remove any section
header, card field, or template fragment.

---

## SETUP: TOPIC
Topic: [One sentence describing the feature or product being market-sized.]

## STATUS QUO: THE DO-NOTHING COMPETITOR
[Complete before any segmentation. This baseline anchors pain severity, WTP scores, and
sequencing transitions below. If behavior varies by segment, note dominant pattern and flag exceptions.]

Current behavior: [What do target users do today without this product? One sentence per distinct behavior.]
Do-nothing cost: [Ongoing cost. Estimate: hrs/wk per user, $ per year, or qualitative friction level.]
Inertia anchor: [What makes users stay with current behavior. Name 1-2 specific anchors. These
anchor names are required in sequencing transitions below -- write them clearly so they can be
cited by name.]
Switching trigger: [What event or threshold causes users to adopt a new tool.]

## STRATEGY: SEGMENT IDENTIFICATION
[Identify 3-6 distinct addressable segments. Name each and describe in one sentence.]
[UNIT RULE: tooling segments use developer headcount (devs); platform/enterprise segments use
dollar TAM ($M). Declare unit per segment. Carry through all cards and tables -- do not change mid-table.]

| Segment ID | Segment Name | Description | Unit (devs / $M) |
|------------|--------------|-------------|------------------|
| S1 | [Name] | [One sentence.] | [devs / $M] |
| S2 | [Name] | [One sentence.] | [devs / $M] |
| S3 | [Name] | [One sentence.] | [devs / $M] |
[Add rows as needed. Minimum 3 segments, maximum 6.]

## STRATEGY: TAM/SAM/SOM
[Use the unit declared for each segment above. Do not change units mid-table.]

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
the beachhead revenue model fits the entry strategy.]
Highest-WTP segment: [Segment ID and name.] WTP: [N]. Deferred because: [One sentence --
reference its inertia anchor or GTM difficulty score.]
Not building this means: [What users continue doing. Reference STATUS QUO do-nothing cost.
Do not omit this line.]

## GTM: SEQUENCING PATH
[Sequencing transitions must cite named conditions from STATUS QUO inertia analysis. "Year 2"
or "when adoption grows" are not valid triggers. "When [named STATUS QUO anchor] breaks" or
"after [named anchor] prevents reversion" are valid. Copy anchor name directly from STATUS QUO.]

Y1: [Segment ID]
  Entry rationale: [Why this segment is the right entry point -- reference inertia state if relevant.]
  Active inertia anchor at entry: [Which STATUS QUO anchor(s) apply? Copy name from STATUS QUO section.]

Y2+: [Segment ID]
  Inertia-break condition: [Name the observable condition drawn from STATUS QUO inertia analysis
  that enables this transition. Must cite the anchor by name -- not a calendar date or time period.
  E.g., "when compliance inertia breaks," "after methodology lock-in prevents reversion."]
  Expansion rationale: [What becomes accessible once the inertia-break condition is met.]

Defer: [Segment ID(s)]
  Deferral reason: [Reference inertia anchor name, GTM difficulty, or revenue model mismatch.
  Do not use calendar time as the deferral reason.]

## AMENDMENTS
1. [Concrete validation action. E.g., price-test WTP assumption for S1 with N discovery calls.]
[Additional actions optional.]

---

Write artifact: simulations/scout/market/{topic}-market-{date}.md
Frontmatter: skill, topic, date, beachhead_segment, beachhead_rank_score, highest_wtp_segment,
segments_count, status_quo_cost, inertia_anchor.
```

---

## V-03: No STATUS QUO (C-11 / C-14 Isolation Test)

**Axis:** Lifecycle emphasis -- STATUS QUO section removed; per-segment cards preserved with
full revenue model co-location; sequencing field preserved; tests which aspirational criteria
depend structurally on STATUS QUO presence
**Hypothesis:** Without STATUS QUO: C-11 FAIL (no do-nothing baseline stated before scoring).
C-14 FAIL (no named inertia anchor to cite in sequencing -- transition triggers fall back to
time periods or generic barriers). C-12 FAIL (no quantified do-nothing cost to reference in
"Not building this means:" -- model may produce a generic estimate but it is untethered to any
pre-stated baseline). C-09, C-10, C-13 should still pass: per-card revenue model and WTP remain
co-located; the WTP-vs-model comparison is structurally available; C-09 insight can surface from
fit score vs. GTM rank reversal even without STATUS QUO. Expected: 3/6 aspirational = 95.
This variation quantifies exactly how many aspirational criteria are gated on STATUS QUO.

```
You are running /scout:market. Fill in this structured template.
All section headers are fixed. Strategy leads sizing. Per-segment cards score fit, GTM, and
revenue model. Do not reorder, rename, or remove any section header, card field, or template fragment.

---

## SETUP: TOPIC
Topic: [One sentence describing the feature or product being market-sized.]

## STRATEGY: SEGMENT IDENTIFICATION
[Identify 3-6 distinct addressable segments. Name each and describe in one sentence.]
[UNIT RULE: tooling segments use developer headcount (devs); platform/enterprise segments use
dollar TAM ($M). Declare unit per segment here. Carry through all cards and tables -- do not
change mid-table.]

| Segment ID | Segment Name | Description | Unit (devs / $M) |
|------------|--------------|-------------|------------------|
| S1 | [Name] | [One sentence.] | [devs / $M] |
| S2 | [Name] | [One sentence.] | [devs / $M] |
| S3 | [Name] | [One sentence.] | [devs / $M] |
[Add rows as needed. Minimum 3 segments, maximum 6.]

## STRATEGY: TAM/SAM/SOM
[Use the unit declared for each segment above. Do not change units mid-table.]

| Segment ID | TAM | SAM | SOM | Unit |
|------------|-----|-----|-----|------|
| S1 | [N] | [N] | [N] | [from above] |
| S2 | [N] | [N] | [N] | [from above] |
| S3 | [N] | [N] | [N] | [from above] |

## PM + GTM: SEGMENT SCORING CARDS
[Fill one card per segment. All fields required. Do not omit rank score, revenue model, or
price point -- all must appear in every card. At least one card must name a concrete price
point or ARR target (not TBD).]

### S1: [Segment Name]
PM -- Pain severity (1-10): [N] -- [Rationale -- describe the unmet need.]
PM -- WTP (1-10): [N] -- [Rationale -- describe willingness to pay.]
PM -- Accessibility (1-10): [N] -- [Rationale -- how reachable through existing channels?]
PM -- Fit score: ([pain] + [WTP] + [access]) / 3 = [avg]
PM -- Revenue model: [free / freemium / seat license / usage-based / enterprise / other]
PM -- Price point or ARR target: [$ concrete value, or "TBD -- validate in Phase X"]
GTM -- Difficulty (1-10): [N] -- [Rationale; name the specific barrier that makes this
segment hard to reach -- channel access, sales cycle, procurement, competitive entrenchment.]
Rank score: [fit] + (10 - [gtm]) = [total]

### S2: [Segment Name]
PM -- Pain severity (1-10): [N] -- [Rationale.]
PM -- WTP (1-10): [N] -- [Rationale.]
PM -- Accessibility (1-10): [N] -- [Rationale.]
PM -- Fit score: ([pain] + [WTP] + [access]) / 3 = [avg]
PM -- Revenue model: [free / freemium / seat license / usage-based / enterprise / other]
PM -- Price point or ARR target: [$ concrete value, or "TBD -- validate in Phase X"]
GTM -- Difficulty (1-10): [N] -- [Rationale; name the specific barrier.]
Rank score: [fit] + (10 - [gtm]) = [total]

### S3: [Segment Name]
PM -- Pain severity (1-10): [N] -- [Rationale.]
PM -- WTP (1-10): [N] -- [Rationale.]
PM -- Accessibility (1-10): [N] -- [Rationale.]
PM -- Fit score: ([pain] + [WTP] + [access]) / 3 = [avg]
PM -- Revenue model: [free / freemium / seat license / usage-based / enterprise / other]
PM -- Price point or ARR target: [$ concrete value, or "TBD -- validate in Phase X"]
GTM -- Difficulty (1-10): [N] -- [Rationale; name the specific barrier.]
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
preferred over the highest-WTP segment, (4) why the beachhead revenue model fits the entry strategy.]
Highest-WTP segment: [Segment ID and name.] WTP: [N]. Deferred because: [One sentence --
reference its GTM difficulty or entry barrier.]
Not building this means: [What users continue doing and what it costs them. Estimate the cost
if exact figures are unavailable. Do not omit this line.]

## GTM: SEQUENCING PATH
Y1: [Segment ID] -- [Entry rationale -- why this segment first.]
Y2+: [Segment ID] -- [Transition trigger -- what barrier is resolved or what channel opens.]
Defer: [Segment ID(s)] -- [Deferral reason -- reference GTM difficulty or revenue model mismatch.]

## AMENDMENTS
1. [Concrete validation action.]
[Additional actions optional.]

---

Write artifact: simulations/scout/market/{topic}-market-{date}.md
Frontmatter: skill, topic, date, beachhead_segment, beachhead_rank_score, highest_wtp_segment,
segments_count.
```

---

## V-04: Unified Scoring Table + Explicit C-14 Trigger (Combined)

**Axes:** Output format (C-13 table co-location, V-01 axis) + inertia framing (explicit
inertia-break condition in sequencing, V-02 axis)
**Hypothesis:** V-01 tests whether table column co-location passes C-13. V-02 tests whether
explicit C-14 mandate is load-bearing. Combining both is the table-based path to 100: if table
co-location passes C-13 and explicit trigger guarantees C-14, this variation achieves 100 without
per-segment cards. This is a structurally different golden template than R2-V-02: tables instead
of cards, explicit C-14 mandate rather than implicit trigger field. If V-04 reaches 100, two
structurally distinct paths to 100 exist -- per-card (V-02/V-05) and table-based (V-04). If V-04
hits 98.3, per-card structure is confirmed as the only path.

```
You are running /scout:market. Fill in this structured template.
All section headers are fixed. STATUS QUO runs first. Revenue model and price point appear in
the unified scoring table adjacent to WTP -- not in a separate section. Sequencing transitions
must cite named conditions from STATUS QUO inertia analysis -- not time periods. Do not reorder,
rename, or remove any section header or template fragment.

---

## SETUP: TOPIC
Topic: [One sentence describing the feature or product being market-sized.]

## STATUS QUO: THE DO-NOTHING COMPETITOR
[Complete before any segment scoring. This baseline anchors pain severity, WTP scores, and
sequencing transitions below.]

Current behavior: [What do target users do today without this product? One sentence per distinct behavior.]
Do-nothing cost: [Ongoing cost. Estimate: hrs/wk per user, $ per year, or qualitative friction level.]
Inertia anchor: [What makes users stay with current behavior. Name 1-2 specific anchors. These
names will be cited in sequencing transitions below -- write them clearly.]
Switching trigger: [What event or threshold causes users to adopt a new tool.]

## STRATEGY: SEGMENT IDENTIFICATION
[Identify 3-6 distinct addressable segments.]
[UNIT RULE: tooling segments use developer headcount (devs); platform/enterprise segments use
dollar TAM ($M). Declare unit per segment. Do not mix units within the same column.]

| Segment ID | Segment Name | Description | Unit (devs / $M) |
|------------|--------------|-------------|------------------|
| S1 | [Name] | [One sentence.] | [devs / $M] |
| S2 | [Name] | [One sentence.] | [devs / $M] |
| S3 | [Name] | [One sentence.] | [devs / $M] |
[Minimum 3 segments, maximum 6.]

## STRATEGY: TAM/SAM/SOM
[Use the unit declared for each segment above.]

| Segment ID | TAM | SAM | SOM | Unit |
|------------|-----|-----|-----|------|
| S1 | [N] | [N] | [N] | [from above] |
| S2 | [N] | [N] | [N] | [from above] |
| S3 | [N] | [N] | [N] | [from above] |

## PM + GTM: UNIFIED SCORING TABLE
[Revenue model and price point appear in this table adjacent to WTP -- not in a separate section.
Adjacent columns for the same segment row make WTP-vs-revenue-model comparison visible without
cross-referencing. At least one segment must show a concrete price point, not TBD.]
[Pain: reference STATUS QUO do-nothing cost. WTP: reference STATUS QUO switching trigger.]
[Accessibility: how reachable through existing channels?]
[Fit score = (pain + WTP + accessibility) / 3. GTM: name specific inertia anchor from STATUS
QUO or segment-specific. Rank score = fit + (10 - GTM difficulty).]

| Seg | Pain (1-10) | WTP (1-10) | Revenue Model | Price Point | Access (1-10) | Fit Score | GTM (1-10) | Inertia Anchor | Rank Score |
|-----|-------------|------------|---------------|-------------|---------------|-----------|------------|----------------|------------|
| S1 | [N] | [N] | [model type] | [$ or TBD] | [N] | [avg] | [N] | [named anchor] | [fit+(10-gtm)] |
| S2 | [N] | [N] | [model type] | [$ or TBD] | [N] | [avg] | [N] | [named anchor] | [fit+(10-gtm)] |
| S3 | [N] | [N] | [model type] | [$ or TBD] | [N] | [avg] | [N] | [named anchor] | [fit+(10-gtm)] |
[Notes: show fit score arithmetic per segment -- ([pain]+[WTP]+[access])/3 = [avg].]

## COMPOSITE RANK
[Sort descending by rank score. Revenue model column included.]

| Rank | Segment ID | Segment Name | Fit Score | GTM Difficulty | Revenue Model | Rank Score |
|------|------------|--------------|-----------|----------------|---------------|------------|
| 1 | [ID] | [Name] | [fit] | [gtm] | [model] | [rank] |
| 2 | [ID] | [Name] | [fit] | [gtm] | [model] | [rank] |
| 3 | [ID] | [Name] | [fit] | [gtm] | [model] | [rank] |

## PM: BEACHHEAD RECOMMENDATION
Beachhead: [Segment ID and name.]
Fit score: [N] | GTM difficulty: [N] | Rank score: [N] | Revenue model: [model type]
Rationale: [2-4 sentences. Address: (1) fit score, (2) GTM difficulty, (3) why preferred over
highest-WTP segment, (4) how STATUS QUO inertia shapes this choice.]
Highest-WTP segment: [Segment ID and name.] WTP: [N]. Deferred because: [One sentence --
reference its inertia anchor or GTM difficulty.]
Not building this means: [What users continue doing. Reference STATUS QUO do-nothing cost.
Do not omit this line.]

## GTM: SEQUENCING PATH
[Transitions must cite named conditions from STATUS QUO inertia analysis. "Year 2" is not valid.
"When [named STATUS QUO anchor] breaks" is valid. Copy anchor name directly from STATUS QUO.]

Y1: [Segment ID]
  Entry rationale: [Why this segment first -- reference inertia state if relevant.]
  Active inertia anchor at entry: [Copy named anchor from STATUS QUO that applies here.]

Y2+: [Segment ID]
  Inertia-break condition: [Name the observable condition from STATUS QUO inertia analysis that
  enables this transition. Must cite the anchor by name -- not a calendar date. E.g., "when
  compliance inertia breaks," "after methodology lock-in prevents reversion."]
  What it unlocks: [One sentence on what becomes accessible.]

Defer: [Segment ID(s)]
  Deferral reason: [Reference inertia anchor name or GTM difficulty from scoring table.]

## AMENDMENTS
1. [Concrete validation action.]
[Additional actions optional.]

---

Write artifact: simulations/scout/market/{topic}-market-{date}.md
Frontmatter: skill, topic, date, beachhead_segment, beachhead_rank_score, highest_wtp_segment,
segments_count, status_quo_cost, inertia_anchor.
```

---

## V-05: Condensed V-02 R2 (Golden Candidate Refinement)

**Axes:** V-02 R2 base (per-segment cards, first perfect score) + C-12 chain strengthened to
V-05 R2 quantification style + C-14 explicit inertia-break trigger + redundant instruction text
removed (single statement per rule rather than repeated reminders throughout the template)
**Hypothesis:** R2-V-02 at 100 is the proven golden candidate but carries verbose instruction
text inherited from R1 development (e.g., "Do not omit rank score, revenue model, or price
point -- all must appear in every card" repeated across sections). R3-V-05 condenses without
removing structural scaffolding: pre-printed required fields remain, formula lines remain, named
anchor requirements remain, but each rule is stated once. Adds V-05 R2's quantification chain
to C-12 ("costing approximately [$ from STATUS QUO]") and V-02 R3's explicit inertia-break
trigger to C-14. Goal: cleanest possible 100-scoring production template.

```
You are running /scout:market. Fill in this structured template.
STATUS QUO runs first -- its do-nothing cost and inertia anchor are required inputs for scoring
cards, beachhead quantification, and sequencing transitions. Do not reorder, rename, or remove
any section header, card field, or template fragment.

---

## SETUP: TOPIC
Topic: [One sentence.]

## STATUS QUO: THE DO-NOTHING COMPETITOR
Current behavior: [What target users do today. One sentence per distinct behavior.]
Do-nothing cost: [Quantify -- hrs/wk per user or $ per year. This value is required in
"Not building this means:" below. Do not write a vague estimate.]
Inertia anchor: [1-2 named specific anchors. These names are required in scoring cards and
sequencing transitions -- write them so they can be cited verbatim.]
Switching trigger: [What event causes adoption of a new tool.]

## STRATEGY: SEGMENT IDENTIFICATION
[UNIT RULE: tooling = developer headcount (devs). Platform/enterprise = dollar TAM ($M). No mixing.]

| Segment ID | Segment Name | Description | Unit (devs / $M) |
|------------|--------------|-------------|------------------|
| S1 | [Name] | [One sentence.] | [devs / $M] |
| S2 | [Name] | [One sentence.] | [devs / $M] |
| S3 | [Name] | [One sentence.] | [devs / $M] |
[Minimum 3 segments, maximum 6.]

## STRATEGY: TAM/SAM/SOM
[Use unit declared above. Do not change mid-table.]

| Segment ID | TAM | SAM | SOM | Unit |
|------------|-----|-----|-----|------|
| S1 | [N] | [N] | [N] | [from above] |
| S2 | [N] | [N] | [N] | [from above] |
| S3 | [N] | [N] | [N] | [from above] |

## PM + GTM: SEGMENT SCORING CARDS
[One card per segment. Every pre-printed field is required. At least one card must show a
concrete price point, not TBD.]

### S1: [Segment Name]
PM -- Pain (1-10): [N] -- [Rationale; anchor to STATUS QUO do-nothing cost.]
PM -- WTP (1-10): [N] -- [Rationale; anchor to STATUS QUO switching trigger.]
PM -- Accessibility (1-10): [N] -- [Rationale.]
PM -- Fit score: ([pain] + [WTP] + [access]) / 3 = [avg]
PM -- Revenue model: [free / freemium / seat license / usage-based / enterprise / other]
PM -- Price point: [$ concrete value, or "TBD -- validate in Phase X"]
GTM -- Difficulty (1-10): [N] -- [Name the specific STATUS QUO inertia anchor or segment anchor.]
Rank score: [fit] + (10 - [gtm]) = [total]

### S2: [Segment Name]
PM -- Pain (1-10): [N] -- [Rationale; anchor to STATUS QUO do-nothing cost.]
PM -- WTP (1-10): [N] -- [Rationale; anchor to STATUS QUO switching trigger.]
PM -- Accessibility (1-10): [N] -- [Rationale.]
PM -- Fit score: ([pain] + [WTP] + [access]) / 3 = [avg]
PM -- Revenue model: [free / freemium / seat license / usage-based / enterprise / other]
PM -- Price point: [$ concrete value, or "TBD -- validate in Phase X"]
GTM -- Difficulty (1-10): [N] -- [Name the specific inertia anchor.]
Rank score: [fit] + (10 - [gtm]) = [total]

### S3: [Segment Name]
PM -- Pain (1-10): [N] -- [Rationale; anchor to STATUS QUO do-nothing cost.]
PM -- WTP (1-10): [N] -- [Rationale; anchor to STATUS QUO switching trigger.]
PM -- Accessibility (1-10): [N] -- [Rationale.]
PM -- Fit score: ([pain] + [WTP] + [access]) / 3 = [avg]
PM -- Revenue model: [free / freemium / seat license / usage-based / enterprise / other]
PM -- Price point: [$ concrete value, or "TBD -- validate in Phase X"]
GTM -- Difficulty (1-10): [N] -- [Name the specific inertia anchor.]
Rank score: [fit] + (10 - [gtm]) = [total]

[Add S4-S6 if needed. Same format -- every field required.]

## COMPOSITE RANK
[Copy from cards. Sort descending. Verify arithmetic. Revenue model column included.]

| Rank | Segment ID | Segment Name | Fit Score | GTM Difficulty | Revenue Model | Rank Score |
|------|------------|--------------|-----------|----------------|---------------|------------|
| 1 | [ID] | [Name] | [fit] | [gtm] | [model] | [rank] |
| 2 | [ID] | [Name] | [fit] | [gtm] | [model] | [rank] |
| 3 | [ID] | [Name] | [fit] | [gtm] | [model] | [rank] |

## PM: BEACHHEAD RECOMMENDATION
Beachhead: [Segment ID and name.]
Fit: [N] | GTM difficulty: [N] | Rank: [N] | Revenue model: [type]
Rationale: [2-4 sentences. Cover: fit score, GTM difficulty, why preferred over highest-WTP
segment, how STATUS QUO inertia shaped this choice, why the revenue model fits the entry strategy.]
Highest-WTP segment: [Segment ID and name.] WTP: [N]. Deferred because: [One sentence --
reference its inertia anchor or GTM difficulty.]
Not building this means: [Users continue (behavior from STATUS QUO), costing approximately
($ or hrs from STATUS QUO do-nothing cost). Every (quarter/year) of delay = (estimated
ongoing waste or lost capture). Do not omit. Do not write a generic statement.]

## GTM: SEQUENCING PATH

Y1: [Segment ID]
  Entry rationale: [Why here -- reference inertia anchor state if relevant.]
  Active inertia anchor at entry: [Copy named anchor from STATUS QUO.]

Y2+: [Segment ID]
  Inertia-break condition: [Name the observable condition from STATUS QUO inertia analysis that
  enables this transition. Must cite the anchor by name -- not a calendar date. E.g., "when
  compliance inertia breaks," "after methodology lock-in prevents reversion."]
  What it unlocks: [One sentence.]

Defer: [Segment ID(s)]
  Why deferred: [Inertia anchor, GTM difficulty, or revenue model mismatch.]

## AMENDMENTS
1. [Concrete validation action.]
[Additional actions optional.]

---

Write artifact: simulations/scout/market/{topic}-market-{date}.md
Frontmatter: skill, topic, date, beachhead_segment, beachhead_rank_score, highest_wtp_segment,
segments_count, status_quo_cost, inertia_anchor.
```

---

## Round 3 Design Notes

### Axis selection rationale

R2 closed the revenue model placement question (C-10 + C-13 are structurally linked): per-segment
cards are the proven path; standalone trailing tables fail C-13. R3 explores two open questions
surfaced by the v3 rubric:

1. **C-13 via table co-location (V-01, V-04):** Can adjacent table columns satisfy "alongside
   the fit scoring view"? The C-13 rubric says "not in a separate trailing table" -- a unified
   scoring table with WTP and Revenue Model in adjacent columns of the same row is the strongest
   possible table-based co-location. If this passes C-13, per-segment cards are not the only
   path; they are the most rigid path. This matters for template simplicity and for operators
   who prefer tabular output over card-per-segment layout.

2. **C-14 explicit mandate vs. implicit trigger (V-02, V-04, V-05):** R2-V-02 passes C-14 with
   "transition trigger -- what inertia barrier is resolved." R3 tests whether making the mandate
   explicit ("must cite named STATUS QUO anchor, not a time period") changes the structural
   guarantee or is redundant. If explicit mandate = same score as R2-V-02, implicit trigger is
   sufficient and the mandate adds only verbosity.

Phrasing register was confirmed neutral in R2 (V-03 and V-04 tied). It is not explored in R3.
Lifecycle emphasis (no STATUS QUO) is tested in V-03 for isolation purposes only.

### C-13 structural comparison: per-card vs. table

| Format | C-13 mechanism | Proximity | Omission path |
|--------|----------------|-----------|---------------|
| Per-card (R2-V-02) | Adjacent lines in segment block: `WTP (1-10):` then `Revenue model:` | Vertical adjacency within one segment block | None -- field is visibly blank if skipped |
| Wide table (R3-V-01/V-04) | Adjacent columns in same row: `WTP | Revenue Model | Price Point` | Horizontal adjacency in same row | Low -- same as any table; truncation path if output is cut early |

Both mechanisms satisfy "alongside (or within) the fit scoring view" under the rubric wording.
The calibration question is whether the rubric scorer treats horizontal table adjacency
equivalently to vertical card adjacency for C-13. R3-V-01 and R3-V-04 are the controlled test.

### STATUS QUO dependency map (predicted after R3)

| Criterion | With STATUS QUO | Without STATUS QUO |
|-----------|-----------------|---------------------|
| C-09 | PASS (structural scaffolding) | PASS (WTP-vs-model still visible in cards) |
| C-10 | PASS | PASS (per-card revenue model independent) |
| C-11 | PASS | FAIL (no baseline stated) |
| C-12 | PASS (quantified chain) | FAIL (no baseline to quantify against) |
| C-13 | PASS | PASS (per-card co-location independent) |
| C-14 | PASS (anchor cited from STATUS QUO) | FAIL (no anchor to cite) |

If V-03 confirms this prediction: STATUS QUO gates exactly 3 of 6 aspirational criteria
(C-11, C-12, C-14). The three STATUS QUO-independent criteria (C-09, C-10, C-13) are all
coverage-type or structural -- they pass via per-card or table co-location regardless of the
baseline analysis. The three STATUS QUO-dependent criteria (C-11, C-12, C-14) are all depth-type
-- they require a grounded inertia analysis to function.

### Predicted score comparison: R3 paths to 100

| V | Structure | C-12 chain | C-14 mechanism | Notes |
|---|-----------|------------|----------------|-------|
| R2-V-02 | Per-card | Reference instruction | Implicit trigger field | Proven 100 |
| R3-V-01 | Wide table | Reference instruction | Implicit trigger field | 100 if table C-13 works |
| R3-V-02 | Per-card | Reference instruction | Explicit inertia-break mandate | 100 (more deterministic C-14) |
| R3-V-04 | Wide table | Reference instruction | Explicit inertia-break mandate | 100 if table C-13 works |
| R3-V-05 | Per-card | Quantified format chain | Explicit inertia-break mandate | 100 (strongest all criteria) |

If V-01 and V-04 both reach 100: table format is a valid alternative architecture for 100.
If V-01 and V-04 both hit 98.3: per-card is the only C-13-guaranteed architecture.
If V-02 and V-05 score identically to R2-V-02: explicit C-14 mandate is confirmed redundant.
If V-05 > R2-V-02: C-12 quantification chain and/or explicit C-14 are load-bearing improvements.
