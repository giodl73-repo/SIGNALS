Now I have everything needed to score all five variations. Let me evaluate each systematically.

---

# scout-market Scorecard — Round 2 (v2 Rubric)
**Date:** 2026-03-14

---

## Scoring Method

Each variation is a prompt template. The question for each criterion: does the template *structurally guarantee* the criterion will pass when a model fills it in, or does it depend on model discretion?

---

## V-01: Revenue Model Standalone Table

**Base:** V-03 R1 | **Axis:** PM: REVENUE MODEL section placed after COMPOSITE RANK

### Essential (60 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Segment ID column present in all 6 tables: SEGMENT IDENTIFICATION, TAM/SAM/SOM, FIT SCORING, GTM DIFFICULTY, COMPOSITE RANK, PM: REVENUE MODEL. IDs propagate consistently. |
| C-02 | PASS | TAM/SAM/SOM table with fixed row structure, one row per segment, unit column present. |
| C-03 | PASS | FIT SCORING table requires all three dimensions. Instruction: "Composite = arithmetic mean. Do not omit any dimension." Formula is explicit. |
| C-04 | PASS | COMPOSITE RANK table shows `Rank score = Fit Score + (10 - GTM Difficulty)` with arithmetic columns. All segments required. |
| C-05 | PASS | BEACHHEAD RECOMMENDATION section with mandatory rationale addressing (1) fit score, (2) GTM difficulty, (3) preference over highest-WTP segment, (4) inertia anchor at highest-WTP. |

**Essential: 5/5 → 60 pts**

### Recommended (30 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | PASS | Unit Type column in SEGMENT IDENTIFICATION. TAM/SAM/SOM has Unit column. Instruction: "Do not mix units within the same column." |
| C-07 | PASS | SEQUENCING PATH section with Y1 / Y2+ / Defer, one-sentence justification per transition. |
| C-08 | PASS | AMENDMENTS section: "1+ concrete next steps to validate or refine the analysis." |

**Recommended: 3/3 → 30 pts**

### Aspirational (10 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Inertia anchor column required in GTM DIFFICULTY table. BEACHHEAD RECOMMENDATION forces "how the STATUS QUO inertia anchor makes the highest-WTP segment a worse entry point." PM: REVENUE MODEL note explicitly surfaces the free-beachhead-vs-seat-license insight: "a free entry model that locks in methodology before monetization is a different strategic choice than a seat license." Structural scaffolding is sufficient. |
| C-10 | PASS | PM: REVENUE MODEL section has one row per segment. Instruction: "At least one Price Point / ARR Target cell must contain a concrete value, not TBD." |
| C-11 | PASS | STATUS QUO section runs before any segment scoring. Do-nothing cost, inertia anchor, switching trigger all required. FIT SCORING instruction: "Pain severity: reference STATUS QUO do-nothing cost." GTM DIFFICULTY: "Inertia anchor column required: name the specific anchor from STATUS QUO." Anchor traceable to COMPOSITE RANK via GTM table. |
| C-12 | FAIL | BEACHHEAD RECOMMENDATION has no "Not building this means:" field or equivalent. Rationale covers (1-4) but does not require stating the cost of deferring at the decision point. Inertia note covers *why the beachhead was chosen* but not the opportunity cost of inaction. |

**Aspirational: 3/4 → 7.5 pts**

**Composite: 60 + 30 + 7.5 = 97.5 | Golden: YES**

---

## V-02: Revenue Model Per Segment Card

**Base:** V-05 R1 | **Axis:** Revenue model + price point embedded in each scoring card

### Essential (60 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | IDs appear in SEGMENT IDENTIFICATION, TAM/SAM/SOM, per-segment card headers (S1/S2/S3), and COMPOSITE RANK. Consistent propagation. |
| C-02 | PASS | STRATEGY: TAM/SAM/SOM table, one row per segment, unit from declaration above. |
| C-03 | PASS | Every scoring card pre-prints `PM -- Fit score: ([pain] + [WTP] + [access]) / 3 = [avg]`. All three dimensions are required fields in each card. |
| C-04 | PASS | Cards show `Rank score: [fit] + (10 - [gtm]) = [total]`. COMPOSITE RANK table copies from cards. Instruction: "Verify arithmetic matches cards." |
| C-05 | PASS | PM: BEACHHEAD RECOMMENDATION with fit score, GTM difficulty, rank score, rationale addressing highest-WTP comparison and STATUS QUO inertia. |

**Essential: 5/5 → 60 pts**

### Recommended (30 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | PASS | UNIT RULE stated at SEGMENT IDENTIFICATION: "tooling segments use developer headcount (devs); platform/enterprise use dollar TAM ($M). Declare per segment. Carry through all cards and tables -- do not change mid-table." |
| C-07 | PASS | GTM: SEQUENCING PATH with Y1 / Y2+ / Defer and transition trigger field. |
| C-08 | PASS | AMENDMENTS section with concrete validation actions. |

**Recommended: 3/3 → 30 pts**

### Aspirational (10 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | STATUS QUO section present (V-05 R1 base). Cards require pain/WTP reference to STATUS QUO. GTM requires naming inertia anchor per card. BEACHHEAD RECOMMENDATION forces "how STATUS QUO inertia shapes this choice." Per-card revenue model juxtaposed with WTP creates additional surface for the free-model rank-reversal insight. |
| C-10 | PASS | Revenue model and price point are pre-printed required fields in every card. "Do not omit rank score, revenue model, or price point fields -- all must appear in every card. At least one card must name a concrete price point or ARR target (not TBD)." No omission path. |
| C-11 | PASS | STATUS QUO section with Do-nothing cost, Inertia anchor, Switching trigger runs before ANY scoring. Cards reference STATUS QUO for pain and WTP. Inertia anchor traceable through cards → COMPOSITE RANK. |
| C-12 | PASS | PM: BEACHHEAD RECOMMENDATION pre-prints `Not building this means: [What users continue doing. Reference STATUS QUO do-nothing cost. Do not omit this line.]` This line is mandatory and explicitly tied to STATUS QUO. Basis: same as V-05 R1 C-12 pass, which calibrated this field as sufficient in R1. |

**Aspirational: 4/4 → 10 pts**

**Composite: 60 + 30 + 10 = 100 | Golden: YES | Exemplary**

---

## V-03: Revenue Model at Declaration (Strategy-Owned)

**Base:** V-01 R1 | **Axis:** Revenue model column in SEGMENT IDENTIFICATION; no STATUS QUO section

### Essential (60 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Segment ID column in all five tables. |
| C-02 | PASS | STRATEGY: TAM/SAM/SOM table present. |
| C-03 | PASS | PM: FIT SCORING table requires all three dimensions with explicit arithmetic instruction. |
| C-04 | PASS | STRATEGY: COMPOSITE RANK with full rank formula. |
| C-05 | PASS | PM: BEACHHEAD RECOMMENDATION requires addressing fit score, GTM difficulty, and highest-WTP comparison. |

**Essential: 5/5 → 60 pts**

### Recommended (30 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | PASS | Unit Type column in SEGMENT IDENTIFICATION. "Do not mix units within the same column." |
| C-07 | PASS | GTM: SEQUENCING PATH section with Y1 / Y2 / Y3+ or defer. |
| C-08 | PASS | AMENDMENTS section with "1+ concrete next steps." |

**Recommended: 3/3 → 30 pts**

### Aspirational (10 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PARTIAL | Revenue model column at declaration creates a new insight surface (free model declared before WTP is scored, making the structural tension visible early). BEACHHEAD RECOMMENDATION notes "whether the beachhead's revenue model is consistent with its rank score rationale." However: no inertia anchor column in GTM DIFFICULTY (only "Notes"), no STATUS QUO anchoring pain/WTP. The rank-reversal insight depends on model discretion. R1 calibration confirms: without structural inertia anchor, C-09 is fragile. Scored PARTIAL -- insight surface exists but not structurally enforced. |
| C-10 | PASS | Revenue model column in SEGMENT IDENTIFICATION covers every segment. STRATEGY: PRICE POINTS table requires at least one concrete value. Both tables together satisfy the pass condition. |
| C-11 | FAIL | No STATUS QUO section. FIT SCORING does not reference a pre-stated do-nothing cost. GTM DIFFICULTY has no inertia anchor column. Pain and WTP scores are not anchored to observable inertia -- they are abstract ratings. |
| C-12 | FAIL | BEACHHEAD RECOMMENDATION has no "Not building this means:" field or equivalent. No opportunity cost statement at the decision point. |

**Aspirational: 1/4 (C-10 PASS only; C-09 PARTIAL does not count) → 2.5 pts**

**Composite: 60 + 30 + 2.5 = 92.5 | Golden: YES**

---

## V-04: Revenue Model at Declaration + Phrasing Register (Conversational)

**Base:** V-01 R1 | **Axes:** V-03 axis + Socratic/question-framed register

### Essential (60 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Segment ID column in all tables including the ranking table. IDs carry through consistently. |
| C-02 | PASS | "How large is each segment?" section has TAM/SAM/SOM table with one row per segment. |
| C-03 | PASS | "How much does each segment need this?" section has Pain/WTP/Access/Fit score table with explicit arithmetic. "All three scores required per segment. Composite is the arithmetic mean -- do not weight unevenly or drop a dimension." |
| C-04 | PASS | "Which segment should we enter first?" section has rank formula table with full arithmetic. |
| C-05 | PASS | "What is the beachhead recommendation?" section with rationale fields (a), (b), (c) addressing fit, GTM, and highest-WTP deferral. |

**Essential: 5/5 → 60 pts**

### Recommended (30 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | PASS | Unit column in segment table. "Do not mix developer headcount and dollar TAM in the same table column." |
| C-07 | PASS | "What is the expansion sequence?" section with Y1 / Y2+ / Defer. |
| C-08 | PASS | "What do we need to validate?" section with "1+ concrete next steps. These should be falsifiable." |

**Recommended: 3/3 → 30 pts**

### Aspirational (10 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PARTIAL | Same revenue model at declaration as V-03 creates the same insight surface. Beachhead section asks "(c) whether the beachhead revenue model is consistent with a low-friction entry strategy" which points toward C-09. However: conversational framing introduces a structural risk V-03 doesn't have. GTM section asks "What makes it hard?" rather than enforcing an inertia anchor column -- a conversational reply may produce prose rather than a named anchor. This weakens the rank-reversal insight surface vs. V-03's table form. Net effect: same PARTIAL as V-03. |
| C-10 | PASS | Revenue model column in segment table. "What does each segment pay?" table requires at least one concrete number. |
| C-11 | FAIL | No STATUS QUO section. No pre-stated do-nothing cost before scoring. |
| C-12 | FAIL | No "Not building this means:" field in beachhead section. |

**Aspirational: 1/4 → 2.5 pts**

**Composite: 60 + 30 + 2.5 = 92.5 | Golden: YES**

**V-03 and V-04 tie at 92.5. Register confirmed neutral for market-sizing skills.**

---

## V-05: Full Synthesis (Path to 100)

**Base:** V-05 R1 | **Axes:** Per-card revenue model (C-10) + quantified "Not building this means:" + revenue model column in COMPOSITE RANK

### Essential (60 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | IDs in all sections including COMPOSITE RANK and per-segment card headers. |
| C-02 | PASS | STRATEGY: TAM/SAM/SOM table present. |
| C-03 | PASS | Per-segment cards with all three dimensions pre-printed. |
| C-04 | PASS | COMPOSITE RANK table with full formula. Cards show arithmetic. Instruction: "Verify arithmetic matches cards." |
| C-05 | PASS | PM: BEACHHEAD RECOMMENDATION with rationale covering 5 dimensions including revenue model consistency. |

**Essential: 5/5 → 60 pts**

### Recommended (30 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | PASS | UNIT RULE at SEGMENT IDENTIFICATION. |
| C-07 | PASS | GTM: SEQUENCING PATH with transition trigger requiring inertia barrier or channel reference. |
| C-08 | PASS | AMENDMENTS section. |

**Recommended: 3/3 → 30 pts**

### Aspirational (10 pts)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Maximum structural scaffolding: STATUS QUO section + inertia anchor per card + BEACHHEAD RECOMMENDATION addresses "how STATUS QUO inertia shapes this choice" + revenue model column in COMPOSITE RANK (model type visible at final ranking decision). The ranking table now shows `Revenue Model | Rank Score` side by side, making the free-beachhead vs. high-WTP rank-reversal the most structurally visible of all five variations. |
| C-10 | PASS | Revenue model and price point pre-printed in every card. Additional revenue model column in COMPOSITE RANK. Appears twice -- no omission path at either location. |
| C-11 | PASS | STATUS QUO section has quantification mandate: "Quantify: hrs/wk per user, $ per year, or a measurable friction level. This value will be referenced in 'Not building this means:' -- do not write a vague estimate here." Stronger than V-01/V-02 -- quantification enforced at the source field, not just at consumption. |
| C-12 | PASS | "Not building this means:" field has format instruction: "Users continue [behavior], costing approximately [$ or hrs from STATUS QUO]. Every [quarter / year] of delay = [estimated ongoing waste or lost capture]. Do not write a generic statement. Do not omit this line." This chains C-12 to C-11 structurally -- the quantified value from STATUS QUO must appear in the beachhead section. Stronger than V-02's version. |

**Aspirational: 4/4 → 10 pts**

**Composite: 60 + 30 + 10 = 100 | Golden: YES | Exemplary**

---

## Final Rankings

| Rank | V | Score | Label | Essential | Recommended | Aspirational |
|------|---|-------|-------|-----------|-------------|--------------|
| 1 | V-02 | 100 | Exemplary | 5/5 | 3/3 | 4/4 |
| 1 | V-05 | 100 | Exemplary | 5/5 | 3/3 | 4/4 |
| 3 | V-01 | 97.5 | Exemplary | 5/5 | 3/3 | 3/4 |
| 4 | V-03 | 92.5 | Exemplary | 5/5 | 3/3 | 1/4 |
| 4 | V-04 | 92.5 | Exemplary | 5/5 | 3/3 | 1/4 |

**Predicted vs. actual: all five match exactly.**

---

## Excellence Signals

**From V-02 and V-05 (joint top scorers):**

**ES-01: Per-card placement is the structurally sufficient form for any coverage criterion.**
V-02 closes C-10 with two card fields and reaches 100 with no other changes. A standalone post-ranking table (V-01) also passes C-10 but leaves a residual omission path if the model truncates output after COMPOSITE RANK. Per-card placement has no omission path because the field is visibly blank if skipped. Pattern: any coverage criterion that failed by omission in a prior round should be closed by a per-card pre-printed field, not a standalone table.

**ES-02: C-11 and C-12 form a traceable chain -- the chain's strength determines both criteria simultaneously.**
V-05's approach: STATUS QUO requires a quantified value; "Not building this means:" must reference that value by format instruction (`costing approximately [$ or hrs from STATUS QUO]`). This makes C-12 structurally dependent on C-11 being filled correctly. When two aspirational criteria share a traceable chain, they are more robust together than independently. Pattern: aspirational criteria that share a logical dependency should be linked by a format instruction that makes one's output the required input of the other.

**ES-03: Revenue model column in COMPOSITE RANK creates a decision-point insight surface for C-09 without adding text instructions.**
V-05 adds a revenue model column to the COMPOSITE RANK table. This means the model type is visible side-by-side with rank score at the exact point where the beachhead is decided -- making the free-beachhead/high-WTP inversion the most structurally available insight in the output. Pattern: non-obvious insights (C-09 class) are more reliably surfaced by column juxtaposition in the ranking table than by instructional prompting.

**R2 open questions answered:**
1. V-02 reaches 100. C-12 via the "Not building this means: Reference STATUS QUO" instruction is sufficient without the quantification format. V-02's minimal addition is confirmed sufficient.
2. V-03 and V-04 score identically. **Phrasing register is confirmed neutral for market-sizing skills.** Drop as a future axis.
3. V-01's standalone revenue table reaches C-09 PASS (the note about free beachhead insight is sufficient scaffolding). Per-card placement is not required for C-09 -- it is required only for C-10 omission resistance.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["per-card pre-printed fields are the structurally sufficient form for closing coverage criteria by omission -- standalone post-ranking tables leave a residual truncation path", "chaining aspirational criteria via format instruction makes both more robust -- C-11 quantified value becomes the required input for C-12 format, removing discretion from both", "revenue model column in COMPOSITE RANK creates a decision-point insight surface for C-09 without additional instructional text -- juxtaposition at ranking time is more reliable than prompting"]}
```
