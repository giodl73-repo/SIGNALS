Written to `simulations/quest/variations/scout-market-variations-R1-2026-03-14.md`.

---

## Round 1 Variations — Summary

**5 variations across 3 single-axis + 2 combinations:**

| V | Axis | Hypothesis |
|---|------|------------|
| **V-01** | Role sequence (Strategy-first) | TAM sizing before fit scoring anchors C-03 scores in real market data; standalone BEACHHEAD section with pre-printed highest-WTP prompt covers C-05 |
| **V-02** | Output format (per-segment ledger) | Pre-printed card fields make C-03 structurally unavoidable; no omission path for any of the 3 dimensions; rank score arithmetic embedded per card |
| **V-03** | Inertia framing (STATUS QUO section first) | Naming the do-nothing competitor before scoring grounds pain/WTP in observed behavior; GTM difficulty "Inertia anchor" column makes the high-WTP-killed-by-GTM flip (C-09) a natural output |
| **V-04** | Axes 1+2 (Strategy-first + ledger) | Combined: TAM sizing anchors identity first, then per-segment cards guarantee C-03/C-04 coverage |
| **V-05** | Full synthesis (all axes) | STATUS QUO + Strategy-first sizing + per-segment cards + unit consistency at declaration + pre-printed "Not building this means:" at BEACHHEAD — maximum coverage for all 10 criteria |

**Key design decisions:**
- Per-segment cards (V-02/V-04/V-05) eliminate the C-03 column-drop omission path that consolidated tables leave open
- Inertia framing (V-03/V-05) is the structural path to C-09 — without it, the high-WTP flip can only emerge from model discretion
- V-05 is the predicted ceiling; V-02 is the strongest non-inertia structural competitor
ongest -- STATUS QUO + inertia anchor in GTM card field + BEACHHEAD inertia line |

**Key design decision:** V-02 per-segment cards structurally prevent C-03 omissions -- each
dimension is a pre-printed field. The consolidated table in V-01/V-03 is more compact but relies
on the model not dropping a column. V-05 combines both structural guarantees.

**Predicted ceiling:** V-05 -- maximum surface coverage for all 10 criteria. V-02 is strongest
for structural C-03 coverage without inertia. V-03 is the minimum-overhead path to C-09.

---

## V-01: Role Sequence (Strategy-first)

**Axis:** Role sequence -- Strategy leads (TAM/SAM/SOM before fit scoring), PM scores fit
second, GTM rates difficulty third, Strategy synthesizes composite rank last
**Hypothesis:** Establishing segment identities and TAM sizes before scoring forces the model to
anchor fit scores against real market data rather than intuition. The consolidated fit-scoring
table is compact but relies on the model filling all three columns. C-05 (beachhead rationale)
is handled by a standalone section with a pre-printed "highest-WTP segment" prompt.

```
You are running /scout:market. Fill in this structured template.
All section headers are fixed. Strategy leads. Every gate must fire before the next section begins.
Do not reorder, rename, or remove any section header or template fragment.

---

## SETUP: TOPIC
Topic: [One sentence describing the feature or product being market-sized.]

## STRATEGY: SEGMENT IDENTIFICATION
[Identify 3-6 distinct addressable segments. Name each segment and describe it in one sentence.]
[Tooling segments: use developer headcount. Platform/enterprise segments: use dollar TAM. Do not mix units within the same column.]

| Segment ID | Segment Name | Description | Unit Type |
|------------|--------------|-------------|-----------|
| S1 | [Name] | [One sentence.] | [devs / $TAM] |
| S2 | [Name] | [One sentence.] | [devs / $TAM] |
| S3 | [Name] | [One sentence.] | [devs / $TAM] |
[Add rows as needed. Minimum 3 segments, maximum 6.]

## STRATEGY: TAM/SAM/SOM
[Complete one row per segment. Use units declared in SEGMENT IDENTIFICATION. Do not mix headcount and dollar TAM in the same column.]
[TAM = total addressable market; SAM = serviceable addressable market; SOM = realistic share in Y1-Y2.]

| Segment ID | TAM | SAM | SOM | Unit |
|------------|-----|-----|-----|------|
| S1 | [N] | [N] | [N] | [devs / $M] |
| S2 | [N] | [N] | [N] | [devs / $M] |
| S3 | [N] | [N] | [N] | [devs / $M] |
[Mirror every segment from SEGMENT IDENTIFICATION.]

## PM: FIT SCORING
[Score every segment on three dimensions. Scale: 1 (low) to 10 (high). Equal weights. Composite = (pain + WTP + accessibility) / 3. Round to one decimal place.]
[Pain severity: how acute is the unmet need? WTP: willingness to pay for a solution. Accessibility: how reachable is this segment through existing channels?]
[All three columns required. Composite must be the arithmetic mean of the three scores -- do not omit any dimension.]

| Segment ID | Pain Severity (1-10) | WTP (1-10) | Accessibility (1-10) | Fit Score (avg) |
|------------|---------------------|------------|----------------------|-----------------|
| S1 | [N] | [N] | [N] | [avg] |
| S2 | [N] | [N] | [N] | [avg] |
| S3 | [N] | [N] | [N] | [avg] |

## GTM: DIFFICULTY
[Rate GTM difficulty for each segment on a 1-10 scale (1 = easy to reach, 10 = hard). Consider: channel access, sales cycle length, procurement complexity, competitive entrenchment.]

| Segment ID | GTM Difficulty (1-10) | Notes |
|------------|----------------------|-------|
| S1 | [N] | [Brief rationale.] |
| S2 | [N] | [Brief rationale.] |
| S3 | [N] | [Brief rationale.] |

## STRATEGY: COMPOSITE RANK
[Rank score = Fit Score + (10 - GTM Difficulty). Apply to every segment. Show arithmetic. Sort descending by rank score.]

| Segment ID | Fit Score | GTM Difficulty | 10 - GTM | Rank Score | Rank |
|------------|-----------|----------------|----------|------------|------|
| S1 | [fit] | [gtm] | [10-gtm] | [fit + (10-gtm)] | [#] |
| S2 | [fit] | [gtm] | [10-gtm] | [fit + (10-gtm)] | [#] |
| S3 | [fit] | [gtm] | [10-gtm] | [fit + (10-gtm)] | [#] |
[Rank 1 = highest rank score. Verify: rank column matches descending rank score order.]

## PM: BEACHHEAD RECOMMENDATION
Beachhead segment: [Segment ID and name.]
Rationale: [2-4 sentences. Must address: (1) fit score, (2) GTM difficulty, (3) why this segment is preferred over the highest-WTP segment. Explicitly name the highest-WTP segment and explain why it is deferred.]
Highest-WTP segment: [Segment ID and name.] WTP: [N]. Deferred because: [One sentence.]

## GTM: SEQUENCING PATH
Y1 target: [Segment ID] -- [One sentence: why this is the right entry point.]
Y2 expansion: [Segment ID] -- [One sentence: what unlocks this transition.]
Y3+ or defer: [Segment ID(s)] -- [One sentence: why these come last or are deferred.]

## AMENDMENTS
[List 1+ concrete next steps to validate or refine this analysis.]
1. [Open question or validation action. E.g., price-test the WTP assumption for S1 with N interviews.]
[Additional actions optional.]

---

Write artifact: simulations/scout/market/{topic}-market-{date}.md
Frontmatter: skill, topic, date, beachhead_segment, beachhead_rank_score, highest_wtp_segment, segments_count.
```

---

## V-02: Output Format (Per-Segment Scoring Ledger)

**Axis:** Output format -- each segment gets a standalone scoring card rather than consolidated
cross-segment tables; all dimensions, TAM sizing, and rank score are pre-printed fields in each
card; a final composite ranking table copies values from cards
**Hypothesis:** Pre-printed per-segment cards structurally prevent C-03 omissions -- each
dimension (pain, WTP, accessibility) is a named field the model must fill. The ledger format also
makes WTP visible per segment at the moment of comparison, making the C-05 beachhead/highest-WTP
contrast a direct lookup rather than a cross-table scan. Unit type is declared per card (C-06 path).
Rank score arithmetic is embedded in each card (C-04 path), so errors are localized.

```
You are running /scout:market. Fill in this structured template.
All segment cards are pre-printed. Fill every field in every card.
Do not skip, collapse, merge, or reorder any card or field.

---

## SETUP: TOPIC
Topic: [One sentence describing the feature or product being market-sized.]
Segment count: [N. Minimum 3, maximum 6. Confirm here before filling cards.]

## SEGMENT CARDS
[Fill one card per segment. Every field is required. Do not omit any field.]

### Segment S1
Name: [Segment name]
Description: [One sentence.]
Unit: [developer headcount (devs) OR dollar TAM ($) -- tooling segments use devs; platform/enterprise use $. Do not mix in the same table column.]
TAM: [N devs or $N]
SAM: [N devs or $N]
SOM: [N devs or $N]
Pain severity (1-10): [N] -- [One sentence rationale.]
WTP (1-10): [N] -- [One sentence rationale.]
Accessibility (1-10): [N] -- [One sentence rationale.]
Fit score: ([pain] + [WTP] + [accessibility]) / 3 = [avg]
GTM difficulty (1-10): [N] -- [One sentence rationale: channel, sales cycle, procurement, entrenchment.]
Rank score: [fit score] + (10 - [GTM difficulty]) = [total]

### Segment S2
Name: [Segment name]
Description: [One sentence.]
Unit: [devs / $]
TAM: [N devs or $N]
SAM: [N devs or $N]
SOM: [N devs or $N]
Pain severity (1-10): [N] -- [One sentence rationale.]
WTP (1-10): [N] -- [One sentence rationale.]
Accessibility (1-10): [N] -- [One sentence rationale.]
Fit score: ([pain] + [WTP] + [accessibility]) / 3 = [avg]
GTM difficulty (1-10): [N] -- [One sentence rationale.]
Rank score: [fit score] + (10 - [GTM difficulty]) = [total]

### Segment S3
Name: [Segment name]
Description: [One sentence.]
Unit: [devs / $]
TAM: [N devs or $N]
SAM: [N devs or $N]
SOM: [N devs or $N]
Pain severity (1-10): [N] -- [One sentence rationale.]
WTP (1-10): [N] -- [One sentence rationale.]
Accessibility (1-10): [N] -- [One sentence rationale.]
Fit score: ([pain] + [WTP] + [accessibility]) / 3 = [avg]
GTM difficulty (1-10): [N] -- [One sentence rationale.]
Rank score: [fit score] + (10 - [GTM difficulty]) = [total]

[Add S4, S5, S6 cards if segment count above is 4, 5, or 6. Same format -- do not omit any field.]

## COMPOSITE RANKING
[Copy rank scores from segment cards. Sort descending by rank score. Verify arithmetic matches cards.]

| Rank | Segment ID | Segment Name | Fit Score | GTM Difficulty | Rank Score |
|------|------------|--------------|-----------|----------------|------------|
| 1 | [ID] | [Name] | [fit] | [gtm] | [rank] |
| 2 | [ID] | [Name] | [fit] | [gtm] | [rank] |
| 3 | [ID] | [Name] | [fit] | [gtm] | [rank] |
[Mirror all segments. Rank 1 = highest rank score.]

## BEACHHEAD RECOMMENDATION
Beachhead: [Segment ID and name.]
Fit score: [N] | GTM difficulty: [N] | Rank score: [N]
Rationale: [2-4 sentences. Must name the highest-WTP segment and explain why this segment is preferred over it. Address fit score and GTM difficulty explicitly.]
Highest-WTP segment: [Segment ID and name.] WTP score: [N]. Deferred because: [One sentence.]

## SEQUENCING PATH
Y1: [Segment ID] -- [Why this is the entry point.]
Y2+: [Segment ID] -- [What transition unlocks this.]
Defer: [Segment ID(s)] -- [Why deferred.]

## AMENDMENTS
1. [Concrete validation action or open question.]
[Additional actions optional.]

---

Write artifact: simulations/scout/market/{topic}-market-{date}.md
Frontmatter: skill, topic, date, beachhead_segment, beachhead_rank_score, highest_wtp_segment, segments_count.
```

---

## V-03: Inertia Framing (STATUS QUO Section First)

**Axis:** Inertia framing -- a STATUS QUO section runs before segmentation and is referenced
explicitly during fit scoring and GTM difficulty rating; inertia anchors per segment are named
in the GTM table; BEACHHEAD rationale references status-quo behavior
**Hypothesis:** Naming the incumbent behavior (spreadsheets, manual process, do-nothing) before
any scoring forces the model to ground pain severity and WTP in observed current behavior rather
than abstract potential. The GTM difficulty table carries an "Inertia anchor" column that makes
the high-WTP-killed-by-GTM-difficulty flip (C-09) a structurally likely finding: segments with
high WTP but strong inertia anchors will naturally receive high GTM difficulty scores, reversing
naive rank order. C-05 rationale is strengthened because inertia is cited by name.

```
You are running /scout:market. Fill in this structured template.
All section headers are fixed. STATUS QUO section runs before any segment scoring.
Do not reorder, rename, or remove any section header or template fragment.

---

## SETUP: TOPIC
Topic: [One sentence describing the feature or product being market-sized.]

## STATUS QUO: THE DO-NOTHING COMPETITOR
[Complete before any segment scoring. This baseline anchors pain severity and WTP scores below.]
[If the status quo is heterogeneous across segments, note the most common behavior and flag differences.]

Current behavior: [What do target users do today without this product? One sentence per distinct behavior.]
Do-nothing cost: [Ongoing cost of current behavior. Estimate: hrs/wk per user, $ per year, or qualitative friction level.]
Switching trigger: [What event or threshold causes users to leave current behavior and adopt a new tool?]
Inertia anchor: [What makes users stay with current behavior even after discovering this product? Name 1-2 specific anchors: e.g., "data already in spreadsheets", "procurement required for new tools", "existing workflow dependencies".]

## STRATEGY: SEGMENT IDENTIFICATION
[Identify 3-6 distinct addressable segments. Name each and describe in one sentence.]
[Tooling segments: use developer headcount. Platform/enterprise segments: use dollar TAM. Do not mix units within the same column.]

| Segment ID | Segment Name | Description | Unit Type |
|------------|--------------|-------------|-----------|
| S1 | [Name] | [One sentence.] | [devs / $TAM] |
| S2 | [Name] | [One sentence.] | [devs / $TAM] |
| S3 | [Name] | [One sentence.] | [devs / $TAM] |

## STRATEGY: TAM/SAM/SOM
[Use units declared in SEGMENT IDENTIFICATION. Do not mix headcount and dollar TAM in the same column.]

| Segment ID | TAM | SAM | SOM | Unit |
|------------|-----|-----|-----|------|
| S1 | [N] | [N] | [N] | [devs / $M] |
| S2 | [N] | [N] | [N] | [devs / $M] |
| S3 | [N] | [N] | [N] | [devs / $M] |

## PM: FIT SCORING
[Score every segment. Scale: 1 (low) to 10 (high). Equal weights. Composite = (pain + WTP + accessibility) / 3.]
[Pain severity: reference STATUS QUO do-nothing cost -- segments where the cost is higher should score higher on pain.]
[WTP: reference STATUS QUO switching trigger -- segments closer to the trigger score higher.]
[Accessibility: how reachable through existing channels?]
[All three columns required. Composite = arithmetic mean. Do not omit any dimension.]

| Segment ID | Pain Severity (1-10) | WTP (1-10) | Accessibility (1-10) | Fit Score (avg) |
|------------|---------------------|------------|----------------------|-----------------|
| S1 | [N] | [N] | [N] | [avg] |
| S2 | [N] | [N] | [N] | [avg] |
| S3 | [N] | [N] | [N] | [avg] |

## GTM: DIFFICULTY
[Rate GTM difficulty 1-10 (1 = easy, 10 = hard). Inertia anchor column required: name the specific anchor from STATUS QUO or a segment-specific anchor that makes this segment hard to reach. Segments with stronger anchors receive higher difficulty scores.]

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

## BEACHHEAD RECOMMENDATION
Beachhead: [Segment ID and name.]
Rationale: [2-4 sentences. Address: (1) fit score, (2) GTM difficulty, (3) why this segment is preferred over the highest-WTP segment, (4) how the STATUS QUO inertia anchor makes the highest-WTP segment a worse entry point.]
Highest-WTP segment: [Segment ID and name.] WTP: [N]. Deferred because: [One sentence -- reference its inertia anchor or GTM difficulty score.]
Inertia note: [One sentence on how the beachhead choice is shaped by STATUS QUO inertia. E.g., "the beachhead has the weakest inertia anchor, making switching lowest-friction."]

## SEQUENCING PATH
Y1: [Segment ID] -- [Entry rationale.]
Y2+: [Segment ID] -- [Transition trigger -- what inertia barrier is resolved or what channel opens.]
Defer: [Segment ID(s)] -- [Deferral reason -- reference inertia anchor or GTM difficulty if applicable.]

## AMENDMENTS
1. [Concrete validation action. E.g., test switching trigger assumption for S1 with N discovery calls.]
[Additional actions optional.]

---

Write artifact: simulations/scout/market/{topic}-market-{date}.md
Frontmatter: skill, topic, date, beachhead_segment, beachhead_rank_score, highest_wtp_segment, segments_count, status_quo_cost, inertia_anchor.
```

---

## V-04: Axes 1+2 (Strategy-first + Per-Segment Scoring Ledger)

**Axes:** Role sequence (Strategy-first with TAM sizing before fit scoring) + output format
(per-segment scoring cards that embed PM fit scoring and GTM difficulty per segment)
**Hypothesis:** Strategy-first ordering (V-01 axis) anchors segment identity in real market data
before any fit judgments are made. Per-segment cards (V-02 axis) then make C-03 structurally
unavoidable: PM dimensions are pre-printed fields, arithmetic is pre-printed, and GTM difficulty
is in the same card as fit. Together they create the strongest coverage for C-01 through C-04
without adding a STATUS QUO section. The final composite ranking table copies from cards,
isolating arithmetic errors to their source card.

```
You are running /scout:market. Fill in this structured template.
All section headers are fixed. Strategy leads with market sizing. Scoring uses per-segment cards.
Do not reorder, rename, or remove any section header, card header, or template fragment.

---

## SETUP: TOPIC
Topic: [One sentence describing the feature or product being market-sized.]

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
[This section must complete before scoring cards begin.]

| Segment ID | TAM | SAM | SOM | Unit |
|------------|-----|-----|-----|------|
| S1 | [N] | [N] | [N] | [from above] |
| S2 | [N] | [N] | [N] | [from above] |
| S3 | [N] | [N] | [N] | [from above] |

## PM + GTM: SEGMENT SCORING CARDS
[Fill one card per segment identified above. Every field required. Do not skip any field.]
[Pain severity 1-10: how acute is the unmet need? WTP 1-10: willingness to pay. Accessibility 1-10: reachable via existing channels?]
[GTM difficulty 1-10: channel access, sales cycle, procurement complexity, competitive entrenchment.]

### S1: [Segment Name]
PM -- Pain severity (1-10): [N] -- [Rationale.]
PM -- WTP (1-10): [N] -- [Rationale.]
PM -- Accessibility (1-10): [N] -- [Rationale.]
PM -- Fit score: ([pain] + [WTP] + [access]) / 3 = [avg]
GTM -- Difficulty (1-10): [N] -- [Rationale.]
Rank score: [fit] + (10 - [gtm]) = [total]

### S2: [Segment Name]
PM -- Pain severity (1-10): [N] -- [Rationale.]
PM -- WTP (1-10): [N] -- [Rationale.]
PM -- Accessibility (1-10): [N] -- [Rationale.]
PM -- Fit score: ([pain] + [WTP] + [access]) / 3 = [avg]
GTM -- Difficulty (1-10): [N] -- [Rationale.]
Rank score: [fit] + (10 - [gtm]) = [total]

### S3: [Segment Name]
PM -- Pain severity (1-10): [N] -- [Rationale.]
PM -- WTP (1-10): [N] -- [Rationale.]
PM -- Accessibility (1-10): [N] -- [Rationale.]
PM -- Fit score: ([pain] + [WTP] + [access]) / 3 = [avg]
GTM -- Difficulty (1-10): [N] -- [Rationale.]
Rank score: [fit] + (10 - [gtm]) = [total]

[Add S4, S5, S6 cards for additional segments. Same format -- do not omit any field.]

## STRATEGY: COMPOSITE RANK
[Copy rank scores from scoring cards. Sort descending by rank score. Verify arithmetic matches cards.]

| Rank | Segment ID | Segment Name | Fit Score | GTM Difficulty | Rank Score |
|------|------------|--------------|-----------|----------------|------------|
| 1 | [ID] | [Name] | [fit] | [gtm] | [rank] |
| 2 | [ID] | [Name] | [fit] | [gtm] | [rank] |
| 3 | [ID] | [Name] | [fit] | [gtm] | [rank] |
[Mirror all segments. Rank 1 = highest rank score.]

## PM: BEACHHEAD RECOMMENDATION
Beachhead: [Segment ID and name.]
Rationale: [2-4 sentences. Address: fit score, GTM difficulty, and why this segment is preferred over the highest-WTP segment. Explicitly name the highest-WTP segment.]
Highest-WTP segment: [Segment ID and name.] WTP: [N]. Deferred because: [One sentence.]

## GTM: SEQUENCING PATH
Y1: [Segment ID] -- [Entry rationale.]
Y2+: [Segment ID] -- [Transition trigger.]
Defer: [Segment ID(s)] -- [Deferral reason.]

## AMENDMENTS
1. [Concrete validation action or open question.]
[Additional actions optional.]

---

Write artifact: simulations/scout/market/{topic}-market-{date}.md
Frontmatter: skill, topic, date, beachhead_segment, beachhead_rank_score, highest_wtp_segment, segments_count.
```

---

## V-05: Full Synthesis (All Axes)

**Axes:** Inertia framing (V-03) + Strategy-first sizing (V-01) + per-segment scoring cards
(V-02) + explicit unit consistency enforcement at declaration
**Hypothesis:** Maximum structural coverage of all 10 criteria. STATUS QUO (V-03 axis) anchors
pain and WTP scores before any segment is identified, making C-09 (non-obvious insight) a natural
output: the inertia anchor column in cards will naturally produce high GTM difficulty for
high-WTP segments, reversing naive rank order. Strategy-first TAM sizing (V-01 axis) grounds
segments in market data before scoring begins. Per-segment cards (V-02 axis) make C-03 and C-04
structurally unavoidable -- all three PM dimensions and rank score arithmetic are pre-printed
fields. Unit consistency warning is embedded at the declaration point (C-06 path). BEACHHEAD
carries a pre-printed "Not building this means:" line (C-09 surface at decision point).

```
You are running /scout:market. Fill in this structured template.
All section headers are fixed. STATUS QUO runs first. Strategy leads sizing. Per-segment cards score fit and GTM.
Do not reorder, rename, or remove any section header, card header, or template fragment.

---

## SETUP: TOPIC
Topic: [One sentence describing the feature or product being market-sized.]

## STATUS QUO: THE DO-NOTHING COMPETITOR
[Complete before any segmentation. This baseline anchors pain severity and WTP scores in all cards below.]
[If behavior varies by segment, note the dominant pattern and flag exceptions.]

Current behavior: [What do target users do today without this product? One sentence per distinct behavior.]
Do-nothing cost: [Ongoing cost. Estimate: hrs/wk per user, $ per year, or qualitative friction level.]
Inertia anchor: [What makes users stay with current behavior. Name 1-2 specific anchors.]
Switching trigger: [What event causes users to adopt a new tool.]

## STRATEGY: SEGMENT IDENTIFICATION
[Identify 3-6 distinct addressable segments. Name each and describe in one sentence.]
[UNIT RULE: tooling segments use developer headcount (devs); platform/enterprise segments use dollar TAM ($M). Declare unit per segment here. Carry this unit through all cards and tables -- do not change mid-table.]

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
[Fill one card per segment. All fields required. Reference STATUS QUO when scoring pain and WTP.]
[Do not omit the rank score calculation -- it must appear in every card.]

### S1: [Segment Name]
PM -- Pain severity (1-10): [N] -- [Rationale; reference STATUS QUO do-nothing cost if applicable.]
PM -- WTP (1-10): [N] -- [Rationale; reference STATUS QUO switching trigger if applicable.]
PM -- Accessibility (1-10): [N] -- [Rationale.]
PM -- Fit score: ([pain] + [WTP] + [access]) / 3 = [avg]
GTM -- Difficulty (1-10): [N] -- [Rationale; name specific inertia anchor from STATUS QUO or segment-specific. Do not leave blank.]
Rank score: [fit] + (10 - [gtm]) = [total]

### S2: [Segment Name]
PM -- Pain severity (1-10): [N] -- [Rationale; reference STATUS QUO if applicable.]
PM -- WTP (1-10): [N] -- [Rationale; reference STATUS QUO if applicable.]
PM -- Accessibility (1-10): [N] -- [Rationale.]
PM -- Fit score: ([pain] + [WTP] + [access]) / 3 = [avg]
GTM -- Difficulty (1-10): [N] -- [Rationale; name inertia anchor. Do not leave blank.]
Rank score: [fit] + (10 - [gtm]) = [total]

### S3: [Segment Name]
PM -- Pain severity (1-10): [N] -- [Rationale; reference STATUS QUO if applicable.]
PM -- WTP (1-10): [N] -- [Rationale; reference STATUS QUO if applicable.]
PM -- Accessibility (1-10): [N] -- [Rationale.]
PM -- Fit score: ([pain] + [WTP] + [access]) / 3 = [avg]
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
Rationale: [2-4 sentences. Address: (1) fit score, (2) GTM difficulty, (3) why this segment is preferred over the highest-WTP segment, (4) how STATUS QUO inertia shapes this choice.]
Highest-WTP segment: [Segment ID and name.] WTP: [N]. Deferred because: [One sentence -- reference its inertia anchor or GTM difficulty score.]
Not building this means: [What users continue doing. Reference STATUS QUO do-nothing cost. Do not omit this line.]

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
Frontmatter: skill, topic, date, beachhead_segment, beachhead_rank_score, highest_wtp_segment, segments_count, status_quo_cost, inertia_anchor.
```

---

## Round 1 Design Notes

### Axis selection rationale

Three single-axis variations chosen: role sequence (V-01), output format (V-02), inertia framing
(V-03). Role sequence is the direct analogue of the feasibility PM-first finding and tests whether
Strategy-first sizing produces better C-03 grounding. Output format tests whether per-segment
cards eliminate the C-03 omission path that a consolidated table leaves open. Inertia framing
tests whether surfacing the status-quo competitor before scoring produces the C-09 non-obvious
insight without adding much template overhead.

### Why these axes and not others

Lifecycle emphasis was not chosen as a single-axis variation because the market skill phases
(identify -> size -> score -> rank -> recommend) are already sequential; explicit gates add
overhead without unlocking new criteria. Phrasing register was not chosen because the rubric has
no criterion sensitive to formal vs. conversational language -- all criteria test structure and
arithmetic correctness.

### C-03 structural comparison

| V | C-03 mechanism | Omission path |
|---|----------------|---------------|
| V-01 | Consolidated 5-column table, labeled header | Model drops a column |
| V-02 | Pre-printed per-segment fields | No omission path (field must be filled) |
| V-03 | Consolidated table (same as V-01) | Model drops a column |
| V-04 | Pre-printed per-segment fields (same as V-02) | No omission path |
| V-05 | Pre-printed per-segment fields (same as V-02) | No omission path |

### C-09 structural comparison

C-09 passes when "output surfaces at least one finding that reverses naive intuition." The
inertia-framing axis (V-03, V-05) creates the condition structurally: when the GTM difficulty
column names an inertia anchor, high-WTP segments with strong anchors will naturally receive
high GTM difficulty, reversing their rank. V-01, V-02, V-04 can produce C-09 but require the
model to surface the insight without scaffolding.

### V-golden candidate

**V-05** is the direct synthesis target:
- STATUS QUO section grounds pain/WTP scores (C-09 path)
- Strategy-first TAM sizing anchors segments before scoring begins
- Per-segment cards make C-03 and C-04 structurally unavoidable
- BEACHHEAD "Not building this means:" line is a pre-printed C-09 surface at decision point
- Unit consistency enforced at declaration point (C-06 nudge without requiring a separate check)

**V-02** is the strongest structural competitor for C-01..C-04 without inertia overhead.
Key open question: does the STATUS QUO section in V-05 produce measurably better C-09 coverage
in live runs, or does the per-segment inertia anchor field in the GTM card achieve the same flip
without the standalone section?
