Written to `simulations/quest/variations/scout-market-variations-R4-2026-03-14.md`.

---

## Round 4 -- 5 Variations

| V | Axis | Base | Predicted |
|---|------|------|-----------|
| **V-01** | C-15 via summary table (single) | R3-V-05 | **100** |
| **V-02** | Architecture swap to pure wide-table (single) | R3-V-05 elements | **100** |
| **V-03** | C-16 via sequencing sub-table column (single) | R3-V-01 | **98.9** |
| **V-04** | V-03 + C-17 chain (combined) | V-03 | **100 or 98.9** |
| **V-05** | V-01 refined, golden candidate R4 (combined) | R3-V-05 | **100** |

---

### Design logic

**V-01 (single-axis: C-15 via summary table).** Minimal change from R3-V-05 (8/9). Inserts a `## PM + GTM: CROSS-SEGMENT SCORING SUMMARY` section after all per-segment cards -- copies values from cards, presents Pain/WTP/Revenue Model/Price Point/Access/Fit/GTM/Rank as adjacent columns in one view. C-13 continues to pass via per-card vertical adjacency; C-15 now passes via the summary table. All R3-V-05 passes (C-16, C-17) are untouched.

**V-02 (single-axis: architecture swap).** Replaces per-cards with a unified wide scoring table -- carries R3-V-05's STATUS QUO, beachhead, and sequencing sections unchanged. C-15 passes because the wide table is the primary scoring view. C-16 and C-17 are preserved from R3-V-05 (they live in sequencing and beachhead, not the scoring section). Open question: does removing per-cards affect C-09? R3 confirmed wide-table variations pass C-09. Low risk.

**V-03 (single-axis: C-16 via sequencing table column).** Base is R3-V-01 (C-15 PASS, C-16 FAIL, C-17 FAIL). Only change: GTM SEQUENCING PATH becomes a structured table with a pre-printed `Inertia-break condition:` column header whose instruction explicitly states `"Year 2+" is not valid`. C-17 still fails (R3-V-01 has no STATUS QUO forward-reference). Predicted 98.9. This is the controlled C-16 test: does a table column header satisfy the "pre-printed or explicitly-labeled field" requirement, or does C-16 require a per-block key-value field?

**V-04 (combined: V-03 + C-17 chain).** Adds the two C-17 changes to V-03: (1) STATUS QUO do-nothing cost gets a forward-reference instruction, (2) beachhead "Not building this means:" gets a format-chain citation back to STATUS QUO value. If V-03 confirms C-16 PASS via column header, V-04 = 9/9 = 100 (Path B complete). If V-03 FAILS C-16, V-04 = 8/9 = 98.9 (C-15+C-17 PASS, C-16 FAIL) -- a new 98.9 configuration.

**V-05 (combined: Path A golden candidate).** V-01 architecture with deliberate instruction tightening -- every rule stated once, preamble explicitly names the summary table as required output, STATUS QUO and beachhead sections condensed to V-05 R3 quality. If V-01 = V-05 = 100, instruction wording is neutral and V-05 becomes the production template by concision advantage.

---

**The one structural question R4 will answer:** does a sequencing table column header satisfy C-16, or does C-16 require a per-block field label? V-03 isolates it; V-04 completes it. V-01 and V-02 are the two safe paths to 100 regardless of that answer.
eachhead). This is the minimal-change path from
98.9 to 100.

```
You are running /scout:market. Fill in this structured template.
STATUS QUO runs first -- its do-nothing cost and inertia anchor are required inputs for scoring
cards, beachhead quantification, and sequencing transitions. After all segment cards, a
cross-segment scoring summary table must be filled -- copy values from cards; it enables direct
cross-segment comparison in one view. Do not reorder, rename, or remove any section header, card
field, summary table, or template fragment.

---

## SETUP: TOPIC
Topic: [One sentence.]

## STATUS QUO: THE DO-NOTHING COMPETITOR
Current behavior: [What target users do today. One sentence per distinct behavior.]
Do-nothing cost: [Quantify -- hrs/wk per user or $ per year. Required in "Not building this means:"
below -- do not write a vague estimate.]
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

## PM + GTM: CROSS-SEGMENT SCORING SUMMARY
[Transcribe values from segment cards above. Do not recalculate -- copy exactly. Every segment
must appear. No column may be blank. This table enables direct cross-segment comparison of WTP,
revenue model, price point, fit, GTM, and rank in a single view without cross-referencing cards.
At least one Price Point cell must contain a concrete value, not TBD.]

| Seg | Pain | WTP | Revenue Model | Price Point | Access | Fit Score | GTM | Inertia Anchor | Rank Score |
|-----|------|-----|---------------|-------------|--------|-----------|-----|----------------|------------|
| S1 | [N] | [N] | [model] | [$ or TBD] | [N] | [avg] | [N] | [anchor name] | [total] |
| S2 | [N] | [N] | [model] | [$ or TBD] | [N] | [avg] | [N] | [anchor name] | [total] |
| S3 | [N] | [N] | [model] | [$ or TBD] | [N] | [avg] | [N] | [anchor name] | [total] |

## COMPOSITE RANK
[Copy from summary table. Sort descending by rank score. Verify arithmetic matches cards.]

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
($ or hrs from STATUS QUO do-nothing cost). Every (quarter/year) of delay = (estimated ongoing
waste or lost capture). Do not omit. Do not write a generic statement.]

## GTM: SEQUENCING PATH

Y1: [Segment ID]
  Entry rationale: [Why here -- reference inertia anchor state if relevant.]
  Active inertia anchor at entry: [Copy named anchor from STATUS QUO.]

Y2+: [Segment ID]
  Inertia-break condition: [Name the observable condition from STATUS QUO inertia analysis that
  enables this transition. Must cite the anchor by name -- not a calendar date or time period.
  E.g., "when compliance inertia breaks," "after methodology lock-in prevents reversion."]
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

## V-02: Architecture Swap to Pure Wide-Table

**Axis:** Output format -- replace per-segment scoring cards with a single unified wide scoring
table; STATUS QUO, beachhead, and sequencing sections carried from R3-V-05 unchanged
**Hypothesis:** R3-V-05 passes C-16 (explicit inertia-break field in sequencing) and C-17 (STATUS
QUO forward-reference + beachhead format-chain citation). Those sections are independent of whether
scoring is per-card or wide-table. Replacing per-cards with a unified wide scoring table means
C-15 passes (wide-table is the primary scoring view), C-13 continues to pass (wide-table column
adjacency confirmed equivalent in R3), and C-16 + C-17 are unaffected (live in sequencing and
beachhead sections). Open question: does removing per-cards affect C-09? R3 confirmed wide-table
variations (V-01, V-04) pass C-09 via WTP-vs-GTM rank reversal visible in table structure.
Predicted: 9/9 = 100.

```
You are running /scout:market. Fill in this structured template.
STATUS QUO runs first -- its do-nothing cost and inertia anchor are required inputs for the unified
scoring table, beachhead quantification, and sequencing transitions. All segment scoring appears in
a single unified wide table with WTP, revenue model, and price point as adjacent columns -- no
per-segment cards. Sequencing transitions must use the pre-printed "Inertia-break condition:" field
and must cite the named STATUS QUO anchor, not a calendar date or time period. Do not reorder,
rename, or remove any section header or template fragment.

---

## SETUP: TOPIC
Topic: [One sentence.]

## STATUS QUO: THE DO-NOTHING COMPETITOR
Current behavior: [What target users do today. One sentence per distinct behavior.]
Do-nothing cost: [Quantify -- hrs/wk per user or $ per year. Required in "Not building this means:"
below -- do not write a vague estimate.]
Inertia anchor: [1-2 named specific anchors. These names are required in the scoring table and
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

## PM + GTM: UNIFIED SCORING TABLE
[Score every segment in this table. WTP, revenue model, and price point appear as adjacent columns
so the WTP-vs-revenue-model comparison is visible in one row without cross-referencing. At least
one Price Point cell must show a concrete value, not TBD. Pain and WTP: anchor to STATUS QUO
do-nothing cost and switching trigger respectively. GTM: name the specific inertia anchor from
STATUS QUO or a segment-specific anchor -- do not leave blank. Fit score = (pain + WTP + access)
/ 3. Rank score = fit + (10 - GTM). Show fit arithmetic in Notes below table.]

| Seg | Pain (1-10) | WTP (1-10) | Revenue Model | Price Point | Access (1-10) | Fit Score | GTM (1-10) | Inertia Anchor | Rank Score |
|-----|-------------|------------|---------------|-------------|---------------|-----------|------------|----------------|------------|
| S1 | [N] | [N] | [model] | [$ or TBD] | [N] | [avg] | [N] | [anchor name] | [fit+(10-gtm)] |
| S2 | [N] | [N] | [model] | [$ or TBD] | [N] | [avg] | [N] | [anchor name] | [fit+(10-gtm)] |
| S3 | [N] | [N] | [model] | [$ or TBD] | [N] | [avg] | [N] | [anchor name] | [fit+(10-gtm)] |
Notes:
S1: ([pain]+[WTP]+[access])/3 = [avg]
S2: ([pain]+[WTP]+[access])/3 = [avg]
S3: ([pain]+[WTP]+[access])/3 = [avg]

## COMPOSITE RANK
[Sort descending by rank score. Revenue model column included. Verify arithmetic matches table.]

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
($ or hrs from STATUS QUO do-nothing cost). Every (quarter/year) of delay = (estimated ongoing
waste or lost capture). Do not omit. Do not write a generic statement.]

## GTM: SEQUENCING PATH

Y1: [Segment ID]
  Entry rationale: [Why here -- reference active inertia anchor from STATUS QUO.]
  Active inertia anchor at entry: [Copy named anchor from STATUS QUO.]

Y2+: [Segment ID]
  Inertia-break condition: [Name the observable condition from STATUS QUO inertia analysis that
  enables this transition. Must cite the anchor by name -- not a calendar date or time period.
  E.g., "when compliance inertia breaks," "after methodology lock-in prevents reversion."]
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

## V-03: C-16 via Sequencing Sub-Table Column

**Axis:** Inertia framing -- sequencing section restructured as a structured table with a
pre-printed "Inertia-break condition:" column header; base is R3-V-01 (wide-table scoring, passes
C-15); all other sections unchanged from R3-V-01
**Hypothesis:** R3-V-01 fails C-16 because its sequencing uses an implicit trigger field
("Transition trigger -- what inertia barrier is resolved or what channel opens"). V-03 replaces
that narrative sequencing with a table whose column header is labeled "Inertia-break condition:"
with explicit instruction that "Year 2+" is invalid. The C-16 pass condition requires "a
pre-printed or explicitly-labeled field whose label type requires a named observable condition."
A table column IS an explicitly-labeled field. The instruction in parentheses forecloses
time-based responses at the column level. Predicted: C-16 PASS if column header = explicit field;
FAIL if C-16 requires per-block key-value format. C-17 remains FAIL (R3-V-01 base has no STATUS
QUO forward-reference, no beachhead format-chain). Expected: 8/9 = 98.9. This is the controlled
test for whether C-16 passes via table column architecture.

```
You are running /scout:market. Fill in this structured template.
All section headers are fixed. STATUS QUO runs first. Revenue model and price point appear in
the unified scoring table adjacent to WTP. Sequencing transitions appear as a structured table
with a pre-printed "Inertia-break condition:" column -- Y2+ entries must name a STATUS QUO
anchor, not a time period. Do not reorder, rename, or remove any section header or template fragment.

---

## SETUP: TOPIC
Topic: [One sentence describing the feature or product being market-sized.]

## STATUS QUO: THE DO-NOTHING COMPETITOR
[Complete before any segment scoring. This baseline anchors pain severity, WTP scores, and
the "Not building this means:" statement at the beachhead.]

Current behavior: [What do target users do today without this product? One sentence per distinct behavior.]
Do-nothing cost: [Ongoing cost of current behavior. Estimate: hrs/wk per user, $ per year, or
qualitative friction level.]
Inertia anchor: [What makes users stay with current behavior. Name 1-2 specific anchors. These
anchor names will be cited in the scoring table and sequencing Inertia-break condition column --
write them clearly so they can be cited by name.]
Switching trigger: [What event or threshold causes users to adopt a new tool.]

## STRATEGY: SEGMENT IDENTIFICATION
[Identify 3-6 distinct addressable segments.]
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
[Score every segment. Revenue model and price point appear in this table adjacent to WTP -- not
in a separate section. Adjacent columns make WTP-vs-revenue-model comparison visible in a single
row without cross-referencing. At least one segment must show a concrete price point, not TBD.]
[Pain: reference STATUS QUO do-nothing cost. WTP: reference STATUS QUO switching trigger.]
[Fit score = (pain + WTP + accessibility) / 3. Show arithmetic in Notes.]
[GTM: name the specific inertia anchor from STATUS QUO or a segment-specific anchor.]
[Rank score = fit + (10 - GTM difficulty).]

| Seg | Pain (1-10) | WTP (1-10) | Revenue Model | Price Point | Access (1-10) | Fit Score | GTM (1-10) | Inertia Anchor | Rank Score |
|-----|-------------|------------|---------------|-------------|---------------|-----------|------------|----------------|------------|
| S1 | [N] | [N] | [model type] | [$ or TBD] | [N] | [avg] | [N] | [named anchor] | [fit+(10-gtm)] |
| S2 | [N] | [N] | [model type] | [$ or TBD] | [N] | [avg] | [N] | [named anchor] | [fit+(10-gtm)] |
| S3 | [N] | [N] | [model type] | [$ or TBD] | [N] | [avg] | [N] | [named anchor] | [fit+(10-gtm)] |
[At least one Price Point cell must contain a concrete value, not TBD.]
Notes:
S1: ([pain]+[WTP]+[access])/3 = [avg]
S2: ([pain]+[WTP]+[access])/3 = [avg]
S3: ([pain]+[WTP]+[access])/3 = [avg]

## COMPOSITE RANK
[Copy rank scores from scoring table. Sort descending. Revenue model column included.]

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
[Y2+ entries in the "Inertia-break condition:" column must name an observable condition from
STATUS QUO inertia analysis. "Year 2+" or "when adoption grows" are not valid entries -- the
column requires a named anchor, not a time period or growth-based assumption.]

| Stage | Seg ID | Entry/Expansion Rationale | Inertia-break condition: (Y2+ required -- must name STATUS QUO anchor; "Year 2+" is not valid) | What it unlocks |
|-------|--------|--------------------------|--------------------------------------------------------------------------------------------------|-----------------|
| Y1 | [ID] | [Why first; active inertia anchor: copy name from STATUS QUO.] | N/A -- active anchor at entry | -- |
| Y2+ | [ID] | [Expansion rationale once inertia-break condition is met.] | [Named observable condition, e.g., "when [anchor name] breaks," "after [anchor] prevents reversion."] | [One sentence.] |
| Defer | [ID] | [Deferral reason; reference inertia anchor name or GTM difficulty.] | N/A | -- |

## AMENDMENTS
1. [Concrete validation action. E.g., price-test WTP assumption for S1 with N discovery calls.]
[Additional actions optional.]

---

Write artifact: simulations/scout/market/{topic}-market-{date}.md
Frontmatter: skill, topic, date, beachhead_segment, beachhead_rank_score, highest_wtp_segment,
segments_count, status_quo_cost, inertia_anchor.
```

---

## V-04: V-03 + C-17 Chain (Combined: Wide-Table Path B)

**Axes:** C-16 via sequencing sub-table column (V-03 axis) + C-17 STATUS QUO quantification
chain at source and consumption (new axis)
**Hypothesis:** V-03 fails C-17 because R3-V-01 has no STATUS QUO forward-reference and no
beachhead format-chain citation. V-04 adds both: (1) STATUS QUO "Do-nothing cost" field gets a
forward-reference instruction that pre-commits to quantification at the beachhead ("required in
'Not building this means:' below -- do not write a vague estimate"), and (2) beachhead "Not
building this means:" gets the format-chain citation ("costing approximately $ or hrs from STATUS
QUO do-nothing cost -- cite the value from STATUS QUO, do not re-estimate"). All else from V-03
unchanged. If V-03 confirms C-16 PASS via table column, V-04 achieves 9/9 = 100 -- Path B
(pure wide-table) complete. If V-03 confirms C-16 FAIL, V-04 = 8/9 = 98.9 (C-15+C-17 PASS,
C-16 FAIL) -- a new 98.9 configuration useful as a baseline for future R5 testing.

```
You are running /scout:market. Fill in this structured template.
STATUS QUO runs first -- its do-nothing cost is required at the beachhead (cite value and source
format explicitly). Revenue model and price point appear in the unified scoring table adjacent to
WTP. Sequencing transitions appear as a structured table with a pre-printed "Inertia-break
condition:" column -- Y2+ entries must name a STATUS QUO anchor, not a time period. Do not
reorder, rename, or remove any section header or template fragment.

---

## SETUP: TOPIC
Topic: [One sentence.]

## STATUS QUO: THE DO-NOTHING COMPETITOR
Current behavior: [What target users do today. One sentence per distinct behavior.]
Do-nothing cost: [Quantify -- hrs/wk per user or $ per year. Required in "Not building this means:"
below -- do not write a vague estimate. This value will be cited by amount and source at the beachhead.]
Inertia anchor: [Name 1-2 specific anchors. These names are required in the scoring table and
the sequencing Inertia-break condition column -- write them clearly for verbatim citation.]
Switching trigger: [What event causes users to adopt a new tool.]

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

## PM + GTM: UNIFIED SCORING TABLE
[Score every segment. Revenue model and price point appear adjacent to WTP in this table. At
least one Price Point cell must show a concrete value. Pain: anchor to STATUS QUO do-nothing cost.
WTP: anchor to STATUS QUO switching trigger. GTM: name the specific STATUS QUO inertia anchor
or segment-specific anchor. Fit = (pain + WTP + access) / 3. Rank = fit + (10 - GTM).]

| Seg | Pain (1-10) | WTP (1-10) | Revenue Model | Price Point | Access (1-10) | Fit Score | GTM (1-10) | Inertia Anchor | Rank Score |
|-----|-------------|------------|---------------|-------------|---------------|-----------|------------|----------------|------------|
| S1 | [N] | [N] | [model] | [$ or TBD] | [N] | [avg] | [N] | [anchor name] | [fit+(10-gtm)] |
| S2 | [N] | [N] | [model] | [$ or TBD] | [N] | [avg] | [N] | [anchor name] | [fit+(10-gtm)] |
| S3 | [N] | [N] | [model] | [$ or TBD] | [N] | [avg] | [N] | [anchor name] | [fit+(10-gtm)] |
Notes:
S1: ([pain]+[WTP]+[access])/3 = [avg]
S2: ([pain]+[WTP]+[access])/3 = [avg]
S3: ([pain]+[WTP]+[access])/3 = [avg]

## COMPOSITE RANK
[Sort descending by rank score. Revenue model column included.]

| Rank | Segment ID | Segment Name | Fit Score | GTM Difficulty | Revenue Model | Rank Score |
|------|------------|--------------|-----------|----------------|---------------|------------|
| 1 | [ID] | [Name] | [fit] | [gtm] | [model] | [rank] |
| 2 | [ID] | [Name] | [fit] | [gtm] | [model] | [rank] |
| 3 | [ID] | [Name] | [fit] | [gtm] | [model] | [rank] |

## PM: BEACHHEAD RECOMMENDATION
Beachhead: [Segment ID and name.]
Fit: [N] | GTM difficulty: [N] | Rank: [N] | Revenue model: [type]
Rationale: [2-4 sentences. Cover: fit score, GTM difficulty, why preferred over highest-WTP
segment, how STATUS QUO inertia shaped this choice.]
Highest-WTP segment: [Segment ID and name.] WTP: [N]. Deferred because: [One sentence --
reference its inertia anchor or GTM difficulty.]
Not building this means: [Users continue (behavior from STATUS QUO), costing approximately
($ or hrs from STATUS QUO do-nothing cost -- cite the value from STATUS QUO, do not re-estimate).
Every (quarter/year) of delay = (estimated ongoing waste or lost capture). Do not omit.]

## GTM: SEQUENCING PATH
[Y2+ entries in the "Inertia-break condition:" column must name an observable condition from
STATUS QUO inertia analysis. "Year 2+" or "when adoption grows" are not valid entries -- the
column requires a named anchor, not a time period or growth-based assumption.]

| Stage | Seg ID | Entry/Expansion Rationale | Inertia-break condition: (Y2+ required -- must name STATUS QUO anchor; "Year 2+" is not valid) | What it unlocks |
|-------|--------|--------------------------|--------------------------------------------------------------------------------------------------|-----------------|
| Y1 | [ID] | [Why first; active inertia anchor: copy name from STATUS QUO.] | N/A -- active anchor at entry | -- |
| Y2+ | [ID] | [Expansion rationale once inertia-break condition is met.] | [Named observable condition, e.g., "when [anchor name] breaks," "after [anchor] prevents reversion."] | [One sentence.] |
| Defer | [ID] | [Deferral reason; reference inertia anchor name or GTM difficulty.] | N/A | -- |

## AMENDMENTS
1. [Concrete validation action.]
[Additional actions optional.]

---

Write artifact: simulations/scout/market/{topic}-market-{date}.md
Frontmatter: skill, topic, date, beachhead_segment, beachhead_rank_score, highest_wtp_segment,
segments_count, status_quo_cost, inertia_anchor.
```

---

## V-05: Golden Candidate R4 (Per-Card + Summary Table, Consolidated)

**Axes:** C-15 via cross-segment summary table (V-01 axis) + all R3-V-05 passes preserved +
full instruction tightening (every rule stated once, no residual verbosity from development rounds)
**Hypothesis:** V-01 is a mechanical insertion of the summary table into R3-V-05. V-05 is a
deliberate refinement: the preamble explicitly names the summary table as a required output, the
STATUS QUO forward-reference is tightened to a single clause, the beachhead format-chain is
conditioned more precisely, and per-card instructions are condensed to match V-05 R3's proven
concision. If V-01 = V-05 = 100, instruction wording is neutral and V-05 becomes the golden
candidate for production deployment by concision advantage. If V-05 differs from V-01, the
delta identifies which wording changes are load-bearing.

```
You are running /scout:market. Fill in this structured template.
STATUS QUO runs first -- do-nothing cost and inertia anchor power scoring cards, beachhead
quantification, and sequencing transitions. Scoring appears in per-segment cards. After all cards,
a cross-segment summary table is required -- copy values from cards; it presents all scoring
dimensions in one view for direct segment comparison. Do not reorder, rename, or remove any
section header, card field, summary table column, or template fragment.

---

## SETUP: TOPIC
Topic: [One sentence.]

## STATUS QUO: THE DO-NOTHING COMPETITOR
Current behavior: [What target users do today. One sentence per distinct behavior.]
Do-nothing cost: [Quantify -- hrs/wk per user or $ per year. This value is required in
"Not building this means:" below -- do not write a vague estimate.]
Inertia anchor: [1-2 named specific anchors. Required verbatim in scoring cards and sequencing
transitions -- name them so they can be cited exactly.]
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

## PM + GTM: CROSS-SEGMENT SCORING SUMMARY
[Required. Copy all values from cards above -- do not recalculate. This table presents Pain, WTP,
Revenue Model, Price Point, Accessibility, Fit Score, GTM Difficulty, Inertia Anchor, and Rank
Score as adjacent columns with one row per segment. Enables direct cross-segment comparison in
one view without card lookup. No column may be blank. At least one Price Point cell must contain
a concrete value.]

| Seg | Pain | WTP | Revenue Model | Price Point | Access | Fit Score | GTM | Inertia Anchor | Rank Score |
|-----|------|-----|---------------|-------------|--------|-----------|-----|----------------|------------|
| S1 | [N] | [N] | [model] | [$ or TBD] | [N] | [avg] | [N] | [anchor name] | [total] |
| S2 | [N] | [N] | [model] | [$ or TBD] | [N] | [avg] | [N] | [anchor name] | [total] |
| S3 | [N] | [N] | [model] | [$ or TBD] | [N] | [avg] | [N] | [anchor name] | [total] |

## COMPOSITE RANK
[Copy from summary table. Sort descending. Revenue model column included.]

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
($ or hrs from STATUS QUO do-nothing cost). Every (quarter/year) of delay = (estimated ongoing
waste or lost capture). Do not omit. Do not write a generic statement.]

## GTM: SEQUENCING PATH

Y1: [Segment ID]
  Entry rationale: [Why here -- reference inertia anchor state.]
  Active inertia anchor at entry: [Copy named anchor from STATUS QUO.]

Y2+: [Segment ID]
  Inertia-break condition: [Name the observable condition from STATUS QUO inertia analysis that
  enables this transition. Must cite the anchor by name -- not a calendar date or time period.
  E.g., "when compliance inertia breaks," "after methodology lock-in prevents reversion."]
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

## Round 4 Design Notes

### Axis selection rationale

R3 resolved all R2 questions and introduced three new criteria (C-15, C-16, C-17) via the v4
rubric update. R4 has one goal: combine all three. The axis selection follows the two open
architectural paths identified in the rubric's "Path to 100" note:

**Path A (per-card + summary table):** V-01 and V-05 test whether adding a cross-segment summary
table to R3-V-05's per-card architecture passes C-15 without disrupting existing passes. V-01 is
the minimal insertion test; V-05 is the same architecture with deliberate instruction refinement.
If both reach 100, instruction wording is neutral and V-05 becomes the golden candidate. If V-05
differs from V-01, the delta isolates which wording changes are load-bearing beyond structure.

**Path B (pure wide-table):** V-02 tests the aggressive swap: replace per-cards with wide-table
while carrying all R3-V-05's proven sections unchanged. V-03 approaches from R3-V-01's wide-table
base and tests C-16 via sequencing table column. V-04 adds C-17 to V-03.

### C-16 structural question: field vs. column header

The critical open question for R4 is whether C-16 passes via a table column header or requires
a per-block key-value field:

| Mechanism | Appears in | C-16 prediction | Evidence |
|-----------|------------|-----------------|----------|
| Per-block field: `Inertia-break condition: [...]` | R3-V-02, R3-V-05, R4-V-01, R4-V-02, R4-V-05 | PASS (confirmed R3) | V-02 and V-05 R3 scored 100 |
| Table column header: `Inertia-break condition: (Y2+ required...)` | R4-V-03, R4-V-04 | PASS? (open question) | No R3 test |

V-03 is the controlled test. If V-03 confirms C-16 PASS via column header, two structurally
distinct C-16 mechanisms exist. If V-03 FAILS C-16, per-block field is the sole C-16 guarantee.

### C-15 structural question: summary table vs. primary scoring view

C-15 says "no dimension requires lookup in a separate section." For Path A (per-card + summary
table): the summary table is self-contained (all dimensions in one place), so no lookup is needed
from the summary table itself. The per-cards still exist but are not required for C-15 -- the
summary table satisfies the criterion independently. For Path B (pure wide-table): the unified
table IS the primary scoring view; no separate section exists at all. Both should pass C-15, but
Path A's "summary table after cards" framing is untested. V-01 is the first controlled test.

### Predicted score comparison: R4 paths to 100

| V | Structure | C-15 | C-16 | C-17 | Asp | Predicted |
|---|-----------|------|------|------|-----|-----------|
| R3-V-05 | Per-card | FAIL | PASS | PASS | 8/9 | 98.9 |
| R4-V-01 | Per-card + summary table | PASS | PASS (from R3-V-05) | PASS (from R3-V-05) | 9/9 | **100** |
| R4-V-02 | Pure wide-table | PASS | PASS (from R3-V-05) | PASS (from R3-V-05) | 9/9 | **100** |
| R4-V-03 | Wide-table + seq table | PASS | PASS? (column) | FAIL | 8/9 | **98.9** |
| R4-V-04 | Wide-table + seq table | PASS | PASS? (column) | PASS | 9/9 | **100 or 98.9** |
| R4-V-05 | Per-card + summary table | PASS | PASS (from R3-V-05) | PASS (from R3-V-05) | 9/9 | **100** |

### What R4 resolves

1. **C-15 via summary table (V-01, V-05):** Can a post-card summary table pass C-15, or does
   C-15 require the unified table to BE the primary scoring view? V-01 is the first test of
   "summary table added to per-card architecture."

2. **C-16 via table column header (V-03, V-04):** The key open question. Resolution determines
   whether table column architecture is a valid C-16 mechanism or whether per-block field is
   the sole path.

3. **V-02 preservation test:** Does removing per-cards from a proven R3-V-05 structure (while
   keeping all other sections) preserve every existing pass? C-09 is the most likely risk
   (wide-table vs. per-card adjacency for the WTP-vs-revenue-model juxtaposition) -- but R3
   confirmed C-09 PASS for wide-table variations, so the risk is low.

4. **V-01 vs. V-05 scoring parity:** Confirms whether instruction wording is neutral once
   structural scaffolding is identical. If both = 100, V-05 is the golden candidate by
   concision advantage.
