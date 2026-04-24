---
skill: quest-variate
skill_target: campaign-decide
round: 7
date: 2026-03-16
rubric: simulations/quest/rubrics/campaign-decide-rubric-v7-2026-03-16.md
---

# Variations -- campaign-decide / Round 7

Five complete, runnable skill body variations targeting the v7 rubric.
Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

**R6 -> R7 diagnosis:**

The v7 rubric added two new aspirational criteria (C-23 and C-24) and expanded the
denominator from /14 to /16. Under v7, all five R6 variants score below 100.0:

| R6 variation | v7 C-23 | v7 C-24 | v7 composite |
|--------------|---------|---------|--------------|
| V-01 R6 (inline rows, 5-slot synthesis) | FAIL -- inline row labels | FAIL -- single "Phase 1" Because slot | 98.8 |
| V-02 R6 (table format, 5-slot synthesis) | PASS -- column headers present; `\| FID \| Field \| Value \|` accepted liberal | FAIL -- single "Phase 1" slot | 99.4 |
| V-03 R6 (inline rows, 6-slot synthesis) | FAIL -- inline row labels | PASS -- separate 1a/1b Because slots | 99.4 |
| V-04 R6 (inline, lifecycle labels, 5-slot) | FAIL | FAIL | 98.8 |
| V-05 R6 (conversational, inline, 5-slot) | FAIL | FAIL | 98.8 |

V-02 R6 and V-03 R6 converge at 99.4 by opposite single-axis paths. The first template
combining column-header schema (C-23) with sub-phase synthesis slot alignment (C-24) on
the full 22-criterion base is the first to pass all 24 criteria = 100.0 under v7.

**R7 axes:**

| Axis | Criterion targeted | Single/Combined |
|------|--------------------|-----------------|
| C-24 add-on to V-02 R6 (minimal convergence) | C-24 only | V-01 (single) |
| Strict C-23 redesign of V-03 R6 (domain columns) | C-23 only | V-02 (single) |
| Phase 5 column decomposition on V-01 R6 | C-23 boundary test | V-03 (single) |
| Combined strict C-23 + C-24 + Phase 5 decomposition | C-23 strict + C-24 | V-04 (combined) |
| Conversational register + liberal C-23 + C-24 | C-23 liberal + C-24 | V-05 (combined) |

---

## V-01 -- Axis: C-24 only (applied to V-02 R6 base)

**Hypothesis**: V-02 R6 already passes C-23 under the liberal interpretation (table-format
with `| FID | Field | Value |` 3-column layout accepted). The single remaining gap is C-24:
the Because block has one merged "COMPETITORS (Phase 1)" slot where C-24 requires two
separately labeled slots for Phase 1a (inertia) and Phase 1b (rivals). Adding the split
requires only changing the Phase 5 Because block -- no other phase structure changes. Under
v7, C-17 explicitly accepts 6 slots when C-21 is active, so the slot-count change does not
create a C-17 failure. Predicted: first 100.0 under v7 via the minimal-change path.

Base: V-02 R6 (column tables, 5-slot synthesis, 22/22 criteria).
Single-axis change: Because block split from 5 slots to 6 -- "COMPETITORS (Phase 1)" becomes
"INERTIA (Phase 1a)" + "RIVALS (Phase 1b)". Preamble updated to say "exactly 6 slots."
All phase tables, FINDING REGISTER, and gate annotations: identical to V-02 R6.

```
Run the full pre-commitment decision campaign for: {{topic}}

FINDING REGISTER: The complete finding skeleton below is committed before any evidence
phase executes. Each phase fills its registered rows in table format. Cite by hybrid key
"Phase N, F[N]-seq" in synthesis. Do not create FIDs outside this register.

---

## FINDING REGISTER [COMPLETE BEFORE PHASE 0]

| FID   | Phase              | Domain               | Value |
|-------|--------------------|----------------------|-------|
| F0-01 | Phase 0 (prior)    | Claim                | --    |
| F0-02 | Phase 0 (prior)    | Falsification cond.  | --    |
| F0-03 | Phase 0 (prior)    | Confidence prior     | --    |
| F0-04 | Phase 0 (prior)    | Prior rationale      | --    |
| F0-05 | Phase 0 (prior)    | Experiment 1         | --    |
| F0-06 | Phase 0 (prior)    | Experiment 2         | --    |
| F1-01 | Phase 1a (inertia) | Status-quo inertia   | --    |
| F1-02 | Phase 1a (inertia) | Switching cost       | --    |
| F1-03 | Phase 1a (inertia) | Good-enough thresh.  | --    |
| F1-04 | Phase 1b (rivals)  | Rival A              | --    |
| F1-05 | Phase 1b (rivals)  | Rival B              | --    |
| F2-01 | Phase 2 (feasib.)  | Tech complexity      | --    |
| F2-02 | Phase 2 (feasib.)  | Team capability      | --    |
| F2-03 | Phase 2 (feasib.)  | Timeline             | --    |
| F2-04 | Phase 2 (feasib.)  | Cost                 | --    |
| F2-05 | Phase 2 (feasib.)  | Overall feasibility  | --    |
| F2-06 | Phase 2 (feasib.)  | Top risk             | --    |
| F3-01 | Phase 3 (market)   | Addressable market   | --    |
| F3-02 | Phase 3 (market)   | Segment 1            | --    |
| F3-03 | Phase 3 (market)   | Segment 2            | --    |
| F3-04 | Phase 3 (market)   | Primary segment      | --    |
| F4-01 | Phase 4 (web)      | Source 1             | --    |
| F4-02 | Phase 4 (web)      | Source 2             | --    |
| F4-03 | Phase 4 (web)      | Source 3             | --    |
| F5-01 | Phase 5 (synth)    | Hypothesis outcome   | --    |
| F5-02 | Phase 5 (synth)    | Recommendation       | --    |
| F5-03 | Phase 5 (synth)    | Confidence           | --    |
| F5-04 | Phase 5 (synth)    | Confidence rationale | --    |
| F5-05 | Phase 5 (synth)    | Counter-evidence     | --    |
| F5-06 | Phase 5 (synth)    | Next step            | --    |

---

## Phase 0 -- prove-hypothesis [COMPLETE BEFORE PHASE 1]

| FID   | Field               | Value |
|-------|---------------------|-------|
| F0-01 | Claim               |       |
| F0-02 | Falsification cond. |       |
| F0-03 | Confidence prior    |       |
| F0-04 | Prior rationale     |       |
| F0-05 | Experiment 1        |       |
| F0-06 | Experiment 2        |       |

---

## Phase 1 -- scout-competitors [COMPLETE BEFORE PHASE 2]

### Phase 1a -- Inertia Analysis [COMPLETE BEFORE PHASE 1b]

| FID   | Field                 | Value |
|-------|-----------------------|-------|
| F1-01 | Status-quo inertia    |       |
| F1-02 | Switching cost        |       |
| F1-03 | Good-enough threshold |       |

### Phase 1b -- Named Rivals

| FID   | Name | Threat (Low/Med/High) | Notes (one sentence) |
|-------|------|-----------------------|----------------------|
| F1-04 |      |                       |                      |
| F1-05 |      |                       |                      |

---

## Phase 2 -- scout-feasibility [COMPLETE BEFORE PHASE 3]

| FID   | Dimension            | Rating (R/Y/G) | Reason |
|-------|----------------------|----------------|--------|
| F2-01 | Technical complexity |                |        |
| F2-02 | Team capability      |                |        |
| F2-03 | Timeline             |                |        |
| F2-04 | Cost                 |                |        |
| F2-05 | Overall feasibility  |                |        |
| F2-06 | Top risk             |                |        |

---

## Phase 3 -- scout-market [COMPLETE BEFORE PHASE 4]

| FID   | Field              | Value |
|-------|--------------------|-------|
| F3-01 | Addressable market |       |
| F3-02 | Segment 1          |       |
| F3-03 | Segment 2          |       |
| F3-04 | Primary segment    |       |

---

## Phase 4 -- prove-websearch [COMPLETE BEFORE PHASE 5]

| FID   | Source | Direct quote (not paraphrase) | Strength | Verdict |
|-------|--------|-------------------------------|----------|---------|
| F4-01 |        |                               |          |         |
| F4-02 |        |                               |          |         |
| F4-03 |        |                               |          |         |

---

## Phase 5 -- prove-synthesize

| FID   | Field                | Value |
|-------|----------------------|-------|
| F5-01 | Hypothesis outcome   | [Confirmed/Refuted/Inconclusive -- resolves F0-01] |
| F5-02 | Recommendation       | [COMMIT/PAUSE/PIVOT/ABANDON] |
| F5-03 | Confidence           | [High/Medium/Low] |
| F5-04 | Confidence rationale | [cite FIDs that drove this rating -- not the label alone] |
| F5-05 | Counter-evidence     | [one risk or caveat -- cite the FID it qualifies] |
| F5-06 | Next step            | [COMMIT: concrete action | no-build: exit condition or revisit trigger] |

Because (one citation per evidence sub-phase -- exactly 6 slots):
- PRIOR (Phase 0): [claim] because Phase 0, F0-[seq]
- INERTIA (Phase 1a): [claim] because Phase 1a, F1-[seq]
- RIVALS (Phase 1b): [claim] because Phase 1b, F1-[seq]
- FEASIBILITY (Phase 2): [claim] because Phase 2, F2-[seq]
- MARKET (Phase 3): [claim] because Phase 3, F3-[seq]
- WEB EVIDENCE (Phase 4): [claim] because Phase 4, F4-[seq]

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting -- V-01 R7 criterion analysis:**
- C-01 through C-22: All criteria hold from V-02 R6. The only structural change is the Because
  block -- nothing that affects any C-01 through C-22 criterion.
- **C-23**: PASS. Same as V-02 R6 -- table format throughout. The `| FID | Field | Value |`
  3-column layout is the same as V-02 R6, which the R6 rubric scored as PASS (liberal
  interpretation: column headers enumerate column contents even when "Field" is a generic
  label). No regression.
- **C-24**: PASS. Because block now carries two separately labeled Phase 1 slots:
  "INERTIA (Phase 1a)" and "RIVALS (Phase 1b)." The structural split enforced in the evidence
  layer (C-21) now propagates to the synthesis layer. C-24 is satisfied.
- **C-17 (v7)**: PASS. 6 slots, C-21 is active. v7 explicitly accepts 6 slots when C-21
  is in effect. No C-17 failure -- the v7 update directly addresses the slot-count tension
  that made V-03 R6 fail C-17 under v6.
- **C-14**: PASS. Six labeled slots covering Phase 0, Phase 1a, Phase 1b, Phase 2, Phase 3,
  Phase 4 = at minimum 5 distinct phase numbers cited. Exceeds the 3-phase threshold.
- **C-22**: PASS. "because Phase 1a, F1-[seq]" and "because Phase 1b, F1-[seq]" both carry a
  phase-prefix token and a FID key. "Phase 1a" is a valid phase-prefix token; a strict scorer
  disputing it would be unreasonable.

**C-23 liberal vs strict note**: V-01 R7 inherits V-02 R6's `| FID | Field | Value |` format
for Phases 0, 1a, 3, and 5. A strict scorer who reads C-23 as requiring domain-specific column
headers (not generic "Field") would fail those phases. The liberal interpretation -- accepted by
the R6 rubric grader -- is that a 3-column format with an FID identity column satisfies C-23.
V-02 R7 tests the strict path.

**Predicted v7 score**: 16/16 aspirational --> composite **100.0**.
Confirms V-02 R6 + C-24 as the minimal convergence path.

---

## V-02 -- Axis: Strict C-23 (domain-specific column headers for all phases)

**Hypothesis**: V-02 R6 passed C-23 under the liberal interpretation by using table format
with a generic "Field" column. A strict scorer would reject `| FID | Field | Value |` because
"Field" is not a domain-specific column header -- it carries schema in the row-label cells,
not the column header row. V-02 R7 eliminates this ambiguity by redesigning ALL phase tables
with column headers that enumerate domain-specific field names. Phase 0 becomes two named-
column tables (hypothesis record + experiments). Phase 3 becomes a segment matrix table.
Phase 5 becomes three sub-tables (resolution, decision, risk+next-step). Every column header
names a specific field; no generic "Field" or "Value" appears anywhere. This variant passes
C-23 under both liberal and strict interpretations. It also inherits V-03 R6's 6-slot synthesis
(C-24 PASS). Predicted: 100.0, with no residual C-23 scoring ambiguity.

Base: V-03 R6 (6-slot synthesis, inline rows, 21/22 pass under v6 / 15/16 aspirational under v7).
Single-axis change: ALL phase content converted from inline rows to domain-specific column tables.
FINDING REGISTER redesigned to match the record-per-row table architecture. Because block
and gate annotations identical to V-03 R6.

```
Run the full pre-commitment decision campaign for: {{topic}}

FINDING REGISTER: The complete finding skeleton below is committed before any evidence
phase executes. One row per record. Fill each FID row in its phase section using the
domain-specific column tables that follow. Cite by hybrid key "Phase N, F[N]-seq" in the
synthesis Because block. Do not create FIDs outside this register.

---

## FINDING REGISTER [COMPLETE BEFORE PHASE 0]

| FID   | Phase              | Record Type                       |
|-------|--------------------|-----------------------------------|
| F0-01 | Phase 0 (prior)    | Hypothesis record                 |
| F0-02 | Phase 0 (prior)    | Experiment 1 design               |
| F0-03 | Phase 0 (prior)    | Experiment 2 design               |
| F1-01 | Phase 1a (inertia) | Inertia force 1 (status-quo)      |
| F1-02 | Phase 1a (inertia) | Inertia force 2 (switching cost)  |
| F1-03 | Phase 1a (inertia) | Inertia force 3 (good-enough)     |
| F1-04 | Phase 1b (rivals)  | Named rival A                     |
| F1-05 | Phase 1b (rivals)  | Named rival B                     |
| F2-01 | Phase 2 (feasib.)  | Buildability dimension 1          |
| F2-02 | Phase 2 (feasib.)  | Buildability dimension 2          |
| F2-03 | Phase 2 (feasib.)  | Buildability dimension 3          |
| F2-04 | Phase 2 (feasib.)  | Buildability dimension 4          |
| F2-05 | Phase 2 (feasib.)  | Buildability dimension 5          |
| F2-06 | Phase 2 (feasib.)  | Top buildability risk             |
| F3-01 | Phase 3 (market)   | Total addressable market          |
| F3-02 | Phase 3 (market)   | Segment 1                         |
| F3-03 | Phase 3 (market)   | Segment 2                         |
| F3-04 | Phase 3 (market)   | Primary segment selection         |
| F4-01 | Phase 4 (web)      | Web source 1                      |
| F4-02 | Phase 4 (web)      | Web source 2                      |
| F4-03 | Phase 4 (web)      | Web source 3                      |
| F5-01 | Phase 5 (synth)    | Hypothesis resolution record      |
| F5-02 | Phase 5 (synth)    | Recommendation + confidence record|
| F5-03 | Phase 5 (synth)    | Counter-evidence record           |
| F5-04 | Phase 5 (synth)    | Recommended next-step record      |

---

## Phase 0 -- prove-hypothesis [COMPLETE BEFORE PHASE 1]

Commit the hypothesis claim and falsification condition before any competitor or market
data is gathered.

**Hypothesis record:**

| FID   | Hypothesis Claim | Falsification Condition | Prior Confidence (L/M/H) | Prior Rationale |
|-------|-----------------|-------------------------|--------------------------|-----------------|
| F0-01 |                 |                         |                          |                 |

**Experiments:**

| FID   | Experiment Name | Investigation Method |
|-------|----------------|---------------------|
| F0-02 |                |                     |
| F0-03 |                |                     |

---

## Phase 1 -- scout-competitors [COMPLETE BEFORE PHASE 2]

### Phase 1a -- Inertia Analysis [COMPLETE BEFORE PHASE 1b]

| FID   | Inertia Force | Hidden Cost / Why Users Stay | Severity (L/M/H) |
|-------|--------------|------------------------------|-----------------|
| F1-01 |              |                              |                 |
| F1-02 |              |                              |                 |
| F1-03 |              |                              |                 |

### Phase 1b -- Named Rivals

| FID   | Rival Name | Threat Level (L/M/H) | Key Differentiator | Notes (one sentence) |
|-------|-----------|----------------------|-------------------|----------------------|
| F1-04 |           |                      |                   |                      |
| F1-05 |           |                      |                   |                      |

---

## Phase 2 -- scout-feasibility [COMPLETE BEFORE PHASE 3]

| FID   | Buildability Dimension | Signal (R/Y/G) | Supporting Evidence |
|-------|----------------------|----------------|---------------------|
| F2-01 | Technical complexity |                |                     |
| F2-02 | Team capability      |                |                     |
| F2-03 | Timeline             |                |                     |
| F2-04 | Cost                 |                |                     |
| F2-05 | Overall feasibility  |                |                     |
| F2-06 | Top risk             |                |                     |

---

## Phase 3 -- scout-market [COMPLETE BEFORE PHASE 4]

| FID   | Segment / Market          | Size Estimate | Fit Score (1-10) | Target Profile | Selection Rationale |
|-------|--------------------------|---------------|-----------------|----------------|---------------------|
| F3-01 | Total addressable market |               | N/A             | All            |                     |
| F3-02 | Segment 1                |               |                 |                |                     |
| F3-03 | Segment 2                |               |                 |                |                     |
| F3-04 | Primary selection        | N/A           |                 |                |                     |

---

## Phase 4 -- prove-websearch [COMPLETE BEFORE PHASE 5]

| FID   | Source / Citation | Direct Quote (not paraphrase) | Strength (Weak/Mod/Strong) | Verdict (Supports/Refutes/Neutral) |
|-------|------------------|-------------------------------|--------------------------|-----------------------------------|
| F4-01 |                  |                               |                          |                                   |
| F4-02 |                  |                               |                          |                                   |
| F4-03 |                  |                               |                          |                                   |

---

## Phase 5 -- prove-synthesize

**Hypothesis resolution:**

| FID   | Outcome (Confirmed/Refuted/Inconclusive) | Resolving Evidence FID |
|-------|----------------------------------------|----------------------|
| F5-01 |                                        |                      |

**Recommendation and confidence:**

| FID   | Recommendation (COMMIT/PAUSE/PIVOT/ABANDON) | Confidence (H/M/L) | Confidence Rationale (cite FIDs, not label alone) |
|-------|---------------------------------------------|-------------------|---------------------------------------------------|
| F5-02 |                                             |                   |                                                   |

**Counter-evidence and next step:**

| FID   | Counter-Evidence Description | Qualifying Finding FID | Recommended Next Step | Condition (if-build / if-no-build) |
|-------|-----------------------------|-----------------------|----------------------|-----------------------------------|
| F5-03 |                             |                       | N/A                  | N/A                               |
| F5-04 | N/A                         | N/A                   |                      |                                   |

Because (one citation per evidence sub-phase -- exactly 6 slots):
- PRIOR (Phase 0): [claim] because Phase 0, F0-[seq]
- INERTIA (Phase 1a): [claim] because Phase 1a, F1-[seq]
- RIVALS (Phase 1b): [claim] because Phase 1b, F1-[seq]
- FEASIBILITY (Phase 2): [claim] because Phase 2, F2-[seq]
- MARKET (Phase 3): [claim] because Phase 3, F3-[seq]
- WEB EVIDENCE (Phase 4): [claim] because Phase 4, F4-[seq]

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting -- V-02 R7 criterion analysis:**
- C-01 through C-22: All criteria hold from V-03 R6 (C-17 now PASS under v7 with 6 slots +
  C-21 active). FINDING REGISTER redesign changes the FID count (25 FIDs vs 26 in V-03 R6)
  but does not affect any criterion -- C-16 requires pre-seeded skeleton rows before Phase 0,
  which the new FINDING REGISTER satisfies; C-15 requires unique enumerable keys, which
  F0-01..F5-04 provide.
- **C-23**: PASS strict. Every phase uses named-column tables with domain-specific headers.
  Phase 0 has "Hypothesis Claim | Falsification Condition | Prior Confidence | Prior Rationale"
  -- each column is a named field. No `| Field | Value |` pattern anywhere. A strict scorer
  cannot dispute C-23 compliance because column headers enumerate the required fields directly.
  Phase 5's three sub-tables use named columns per record type. PASS under both liberal and
  strict interpretations.
- **C-24**: PASS. 6-slot Because block from V-03 R6, unchanged. "INERTIA (Phase 1a)" and
  "RIVALS (Phase 1b)" are separately labeled.
- **C-17 (v7)**: PASS. 6 slots, C-21 active. Same as V-01 R7.

**Architecture interaction note**: The FINDING REGISTER redesign from 26 FIDs (6 Phase 0 FIDs
for 6 individual fields) to 25 FIDs (3 Phase 0 FIDs for 3 records) changes the granularity of
pre-registered findings. F0-01 now represents the entire hypothesis record (claim + falsification
condition + confidence + rationale as columns), where V-03 R6's F0-01 represented only the
claim. A strict C-16 scorer applying the "individual skeleton placeholder rows" interpretation
may note that the column cells within F0-01 do not have their own FID pre-registrations. Liberal
C-16 interpretation (range table pre-declared before Phase 0) passes. C-16 and C-15 remain
PASS under both interpretations because all FIDs that appear in phase table rows and synthesis
citations are pre-registered.

**Phase 4 wide-quote note**: The Phase 4 table has 5 columns including "Direct Quote (not
paraphrase)." Cell-width pressure on quotes is a practical concern noted in R6. For V-02 R7,
the column header instruction "not paraphrase" is embedded in the column name itself -- a filler
who sees the column header knows the requirement without reading surrounding prose. This is
strictly better C-23 evidence than V-02 R6's column header ("Direct quote (not paraphrase)").

**Predicted v7 score**: 16/16 aspirational --> composite **100.0**.
First template with no residual C-23 scoring ambiguity. Passes under both liberal and strict
C-23 interpretation.

---

## V-03 -- Axis: Phase 5 column decomposition only (C-23 boundary test)

**Hypothesis**: The synthesis section (Phase 5) is the hardest phase for C-23 compliance
because its rows are heterogeneous -- recommendation, confidence, hypothesis outcome, and next
step are semantically distinct fields, not homogeneous instances of the same record type. V-01 R6
through V-05 R6 all used inline rows (`F5-01  Hypothesis outcome: [...]`) for Phase 5; even V-02
R6's table version used `| FID | Field | Value |`, which is the two-column-spirit layout. V-03 R7
tests whether Phase 5 can be redesigned as named-column sub-tables (as demonstrated in V-02 R7)
WITHOUT changing any other phase. The experiment isolates the Phase 5 redesign: if Phases 0-4
remain inline and only Phase 5 gets domain-specific columns, does anything break? Expected result:
C-23 FAIL (inline phases 0-4 still fail), but no new failures introduced by the Phase 5 redesign.
This documents the Phase 5 column approach as combinable with future full-phase column migration.

Base: V-01 R6 (canonical, inline rows, 5-slot synthesis, all 22 pass).
Single-axis change: Phase 5 only -- rewritten as three named-column sub-tables with a
5-slot Because block. All phases 0-4 are identical inline rows from V-01 R6.

```
Run the full pre-commitment decision campaign for: {{topic}}

FINDING REGISTER: The complete finding skeleton below is committed before any evidence
phase executes. Fill each registered row in its phase section. Cite by hybrid key
"Phase N, F[N]-seq" in the synthesis Because block. Do not create FIDs outside this
register.

---

## FINDING REGISTER [COMPLETE BEFORE PHASE 0]

| FID   | Phase              | Domain               | Value |
|-------|--------------------|----------------------|-------|
| F0-01 | Phase 0 (prior)    | Claim                | --    |
| F0-02 | Phase 0 (prior)    | Falsification cond.  | --    |
| F0-03 | Phase 0 (prior)    | Confidence prior     | --    |
| F0-04 | Phase 0 (prior)    | Prior rationale      | --    |
| F0-05 | Phase 0 (prior)    | Experiment 1         | --    |
| F0-06 | Phase 0 (prior)    | Experiment 2         | --    |
| F1-01 | Phase 1a (inertia) | Status-quo inertia   | --    |
| F1-02 | Phase 1a (inertia) | Switching cost       | --    |
| F1-03 | Phase 1a (inertia) | Good-enough thresh.  | --    |
| F1-04 | Phase 1b (rivals)  | Rival A              | --    |
| F1-05 | Phase 1b (rivals)  | Rival B              | --    |
| F2-01 | Phase 2 (feasib.)  | Tech complexity      | --    |
| F2-02 | Phase 2 (feasib.)  | Team capability      | --    |
| F2-03 | Phase 2 (feasib.)  | Timeline             | --    |
| F2-04 | Phase 2 (feasib.)  | Cost                 | --    |
| F2-05 | Phase 2 (feasib.)  | Overall feasibility  | --    |
| F2-06 | Phase 2 (feasib.)  | Top risk             | --    |
| F3-01 | Phase 3 (market)   | Addressable market   | --    |
| F3-02 | Phase 3 (market)   | Segment 1            | --    |
| F3-03 | Phase 3 (market)   | Segment 2            | --    |
| F3-04 | Phase 3 (market)   | Primary segment      | --    |
| F4-01 | Phase 4 (web)      | Source 1             | --    |
| F4-02 | Phase 4 (web)      | Source 2             | --    |
| F4-03 | Phase 4 (web)      | Source 3             | --    |
| F5-01 | Phase 5 (synth)    | Hypothesis outcome   | --    |
| F5-02 | Phase 5 (synth)    | Recommendation       | --    |
| F5-03 | Phase 5 (synth)    | Confidence           | --    |
| F5-04 | Phase 5 (synth)    | Confidence rationale | --    |
| F5-05 | Phase 5 (synth)    | Counter-evidence     | --    |
| F5-06 | Phase 5 (synth)    | Next step            | --    |

---

## Phase 0 -- prove-hypothesis [COMPLETE BEFORE PHASE 1]

F0-01  Claim: [one falsifiable sentence -- what must be true for this to be worth building]
F0-02  Falsification condition: [what single piece of evidence would disprove this claim]
F0-03  Confidence prior: [Low/Medium/High]
F0-04  Prior rationale: [reason for your prior before any external data is gathered]
F0-05  Experiment 1: [name and method]
F0-06  Experiment 2: [name and method]

---

## Phase 1 -- scout-competitors [COMPLETE BEFORE PHASE 2]

### Phase 1a -- Inertia Analysis [COMPLETE BEFORE PHASE 1b]

F1-01  Status-quo inertia: [why people pay the hidden cost of not changing]
F1-02  Switching cost: [what users lose by moving to any alternative]
F1-03  Good-enough threshold: [when the current approach feels acceptable]

### Phase 1b -- Named Rivals

F1-04  Rival A -- name: [name] | threat: [Low/Medium/High] | notes: [one sentence]
F1-05  Rival B -- name: [name] | threat: [Low/Medium/High] | notes: [one sentence]

---

## Phase 2 -- scout-feasibility [COMPLETE BEFORE PHASE 3]

F2-01  Technical complexity: [R/Y/G] -- [reason]
F2-02  Team capability: [R/Y/G] -- [reason]
F2-03  Timeline: [R/Y/G] -- [reason]
F2-04  Cost: [R/Y/G] -- [reason]
F2-05  Overall feasibility: [R/Y/G]
F2-06  Top risk: [single biggest buildability threat]

---

## Phase 3 -- scout-market [COMPLETE BEFORE PHASE 4]

F3-01  Addressable market: [size estimate with stated basis]
F3-02  Segment 1 -- name: [name] | fit: [1-10] | reason: [one sentence]
F3-03  Segment 2 -- name: [name] | fit: [1-10] | reason: [one sentence]
F3-04  Primary segment: [name] | justification: [one sentence]

---

## Phase 4 -- prove-websearch [COMPLETE BEFORE PHASE 5]

F4-01  Source: [URL or citation]
       Quote: "[direct quote -- not paraphrase]"
       Strength: [Weak/Moderate/Strong]
       Verdict: [Supports/Refutes/Neutral]

F4-02  Source: [URL or citation]
       Quote: "[direct quote]"
       Strength: [Weak/Moderate/Strong]
       Verdict: [Supports/Refutes/Neutral]

F4-03  Source: [URL or citation]
       Quote: "[direct quote]"
       Strength: [Weak/Moderate/Strong]
       Verdict: [Supports/Refutes/Neutral]

---

## Phase 5 -- prove-synthesize

**Hypothesis resolution:**

| FID   | Outcome (Confirmed / Refuted / Inconclusive) | Resolving Evidence FID |
|-------|---------------------------------------------|----------------------|
| F5-01 |                                             | [FID of finding that resolved F0-01] |

**Recommendation and confidence:**

| FID   | Recommendation (COMMIT / PAUSE / PIVOT / ABANDON) | Confidence (H/M/L) | Confidence Rationale (cite FIDs -- not label alone) |
|-------|---------------------------------------------------|--------------------|-----------------------------------------------------|
| F5-02 |                                                   |                    |                                                     |
| F5-03 | N/A (confidence record, see F5-02)                |                    |                                                     |

**Counter-evidence and next step:**

| FID   | Counter-Evidence (one risk or caveat) | Qualifying FID | Recommended Next Step | Condition |
|-------|--------------------------------------|----------------|----------------------|-----------|
| F5-05 |                                      |                | N/A                  | N/A       |
| F5-06 | N/A                                  | N/A            |                      | [COMMIT: concrete \| no-build: exit trigger] |

Because (one citation per evidence phase -- exactly 5 slots):
- PRIOR (Phase 0): [claim] because Phase 0, F0-[seq]
- COMPETITORS (Phase 1): [claim] because Phase 1, F1-[seq]
- FEASIBILITY (Phase 2): [claim] because Phase 2, F2-[seq]
- MARKET (Phase 3): [claim] because Phase 3, F3-[seq]
- WEB EVIDENCE (Phase 4): [claim] because Phase 4, F4-[seq]

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting -- V-03 R7 criterion analysis:**
- C-01 through C-22: All criteria hold from V-01 R6. Phases 0-4 are identical inline rows.
  Phase 5 column redesign does not affect any structural criterion -- gate annotations, FID
  system, and citation format are unchanged.
- **C-23**: FAIL. Phases 0, 1a, 2, 3, 4 use inline FID rows. Even though Phase 5 now uses
  named-column sub-tables, C-23 requires "each evidence phase" to have column-header schema.
  The inline phases fail. Phase 5 does pass C-23 as a standalone, but the "each" requirement
  is not satisfied overall.
- **C-24**: FAIL. Because block retains 5 slots -- no Phase 1a/1b split. This variant
  intentionally does not change the synthesis slot count.
- **C-17 (v7)**: PASS. 5 slots, C-21 active. v7's 6-slot requirement kicks in only when
  C-24 is also in effect. A 5-slot template with C-21 active but no C-24 claim passes C-17
  under the liberal v7 reading (same as V-01 R6).

**Phase 5 redesign mechanics note**: F5-03 (confidence) and F5-04 (confidence rationale) from the
original FINDING REGISTER are now combined into the recommendation table row F5-02 (confidence
as a column). F5-03 is registered as "Confidence" but its column-table expression is a column of
F5-02's row. The FINDING REGISTER still pre-seeds F5-03, and the recommendation table header
includes "Confidence (H/M/L)" as a named column -- so F5-03 is structurally expressed even
without a dedicated row. This FID-to-column mapping is the same tension that V-02 R7 addresses
by redesigning the FINDING REGISTER. V-03 deliberately does not redesign the FINDING REGISTER
-- it tests Phase 5 column format in isolation.

**Boundary finding for V-04**: The Phase 5 sub-table design from V-03 R7 is the component
that V-04 combines with full column-schema phases. V-03 documents that Phase 5 column
decomposition introduces no new criterion failures when applied in isolation.

**Predicted v7 score**: 14/16 aspirational (C-23 FAIL, C-24 FAIL) --> composite **98.8**.
Same score as V-01 R6 under v7. Confirms that partial column migration does not help.

---

## V-04 -- Combined: Strict C-23 + C-24 + Phase 5 decomposition

**Hypothesis**: V-02 R7 demonstrated that strict C-23 (domain-specific columns throughout)
passes cleanly when combined with V-03 R6's 6-slot synthesis. V-03 R7 documented the Phase 5
sub-table decomposition in isolation. V-04 combines three elements: (a) strict C-23 columns
from V-02 R7 for all phases, (b) C-24 6-slot synthesis from V-03 R6 and V-01 R7, and (c) a
refined Phase 5 synthesis layout that decomposes the synthesis record into named-column sub-
tables while hosting the Because block as a standalone section below. The combined variant
also addresses the Phase 4 quote-fidelity concern noted in R6 by widening the quote column
label to include the "not paraphrase" constraint and adding a Notes column for source context.
This is the most structurally robust template in R7 -- it has no `| Field | Value |` anywhere
and its 6-slot synthesis mirrors the evidence structure exactly.

Base: V-02 R7 (strict C-23 columns, 6-slot synthesis).
Combined changes relative to V-02 R7:
1. Phase 5 sub-tables refined from V-03 R7's design (consolidated, no N/A placeholder rows)
2. Phase 4 table column "Direct Quote" renamed to "Direct Quote (verbatim -- no paraphrase)" and
   a "Source Context" column added to reduce cell-compression risk for long quotes
3. Phase 0 hypothesis table column "Prior Rationale" split into two columns: "Prior Rationale"
   and "Prior Confidence (L/M/H)" -- making confidence its own column so it does not get buried
All other elements: identical to V-02 R7.

```
Run the full pre-commitment decision campaign for: {{topic}}

FINDING REGISTER: The complete finding skeleton below is committed before any evidence
phase executes. One row per record. Fill each FID row in its phase section using the
domain-specific column tables that follow. Cite by hybrid key "Phase N, F[N]-seq" in
the synthesis Because block. Do not create FIDs outside this register.

---

## FINDING REGISTER [COMPLETE BEFORE PHASE 0]

| FID   | Phase              | Record Type                       |
|-------|--------------------|-----------------------------------|
| F0-01 | Phase 0 (prior)    | Hypothesis record                 |
| F0-02 | Phase 0 (prior)    | Experiment 1 design               |
| F0-03 | Phase 0 (prior)    | Experiment 2 design               |
| F1-01 | Phase 1a (inertia) | Inertia force 1 (status-quo)      |
| F1-02 | Phase 1a (inertia) | Inertia force 2 (switching cost)  |
| F1-03 | Phase 1a (inertia) | Inertia force 3 (good-enough)     |
| F1-04 | Phase 1b (rivals)  | Named rival A                     |
| F1-05 | Phase 1b (rivals)  | Named rival B                     |
| F2-01 | Phase 2 (feasib.)  | Buildability dimension 1          |
| F2-02 | Phase 2 (feasib.)  | Buildability dimension 2          |
| F2-03 | Phase 2 (feasib.)  | Buildability dimension 3          |
| F2-04 | Phase 2 (feasib.)  | Buildability dimension 4          |
| F2-05 | Phase 2 (feasib.)  | Buildability dimension 5          |
| F2-06 | Phase 2 (feasib.)  | Top buildability risk             |
| F3-01 | Phase 3 (market)   | Total addressable market          |
| F3-02 | Phase 3 (market)   | Segment 1                         |
| F3-03 | Phase 3 (market)   | Segment 2                         |
| F3-04 | Phase 3 (market)   | Primary segment selection         |
| F4-01 | Phase 4 (web)      | Web source 1                      |
| F4-02 | Phase 4 (web)      | Web source 2                      |
| F4-03 | Phase 4 (web)      | Web source 3                      |
| F5-01 | Phase 5 (synth)    | Hypothesis resolution record      |
| F5-02 | Phase 5 (synth)    | Recommendation record             |
| F5-03 | Phase 5 (synth)    | Counter-evidence record           |
| F5-04 | Phase 5 (synth)    | Next-step record                  |

---

## Phase 0 -- prove-hypothesis [COMPLETE BEFORE PHASE 1]

**Hypothesis record (commit prior before any evidence phase runs):**

| FID   | Hypothesis Claim | Falsification Condition | Prior Confidence (L/M/H) | Prior Rationale |
|-------|-----------------|-------------------------|--------------------------|-----------------|
| F0-01 |                 |                         |                          |                 |

**Experiments (two methods you would run to test the claim):**

| FID   | Experiment Name | Investigation Method |
|-------|----------------|---------------------|
| F0-02 |                |                     |
| F0-03 |                |                     |

---

## Phase 1 -- scout-competitors [COMPLETE BEFORE PHASE 2]

### Phase 1a -- Inertia Analysis [COMPLETE BEFORE PHASE 1b]

| FID   | Inertia Force | Hidden Cost / Why Users Stay | Severity (L/M/H) |
|-------|--------------|------------------------------|-----------------|
| F1-01 |              |                              |                 |
| F1-02 |              |                              |                 |
| F1-03 |              |                              |                 |

### Phase 1b -- Named Rivals

| FID   | Rival Name | Threat Level (L/M/H) | Key Differentiator | Notes (one sentence) |
|-------|-----------|----------------------|-------------------|----------------------|
| F1-04 |           |                      |                   |                      |
| F1-05 |           |                      |                   |                      |

---

## Phase 2 -- scout-feasibility [COMPLETE BEFORE PHASE 3]

| FID   | Buildability Dimension | Signal (R/Y/G) | Supporting Evidence |
|-------|----------------------|----------------|---------------------|
| F2-01 | Technical complexity |                |                     |
| F2-02 | Team capability      |                |                     |
| F2-03 | Timeline             |                |                     |
| F2-04 | Cost                 |                |                     |
| F2-05 | Overall feasibility  |                |                     |
| F2-06 | Top risk             |                |                     |

---

## Phase 3 -- scout-market [COMPLETE BEFORE PHASE 4]

| FID   | Segment / Market          | Size Estimate | Fit Score (1-10) | Target Profile | Selection Rationale |
|-------|--------------------------|---------------|-----------------|----------------|---------------------|
| F3-01 | Total addressable market |               | N/A             | All            |                     |
| F3-02 | Segment 1                |               |                 |                |                     |
| F3-03 | Segment 2                |               |                 |                |                     |
| F3-04 | Primary selection        | N/A           |                 |                |                     |

---

## Phase 4 -- prove-websearch [COMPLETE BEFORE PHASE 5]

| FID   | Source / Citation | Direct Quote (verbatim -- no paraphrase) | Source Context | Strength (Weak/Mod/Strong) | Verdict (Supports/Refutes/Neutral) |
|-------|------------------|------------------------------------------|----------------|--------------------------|-----------------------------------|
| F4-01 |                  |                                          |                |                          |                                   |
| F4-02 |                  |                                          |                |                          |                                   |
| F4-03 |                  |                                          |                |                          |                                   |

---

## Phase 5 -- prove-synthesize

**Hypothesis resolution:**

| FID   | Outcome (Confirmed / Refuted / Inconclusive) | Resolving Evidence FID |
|-------|---------------------------------------------|----------------------|
| F5-01 |                                             |                      |

**Recommendation:**

| FID   | Recommendation (COMMIT / PAUSE / PIVOT / ABANDON) | Confidence (H/M/L) | Confidence Rationale (cite FIDs -- not label alone) |
|-------|---------------------------------------------------|--------------------|-----------------------------------------------------|
| F5-02 |                                                   |                    |                                                     |

**Counter-evidence and next step:**

| FID   | Counter-Evidence | Qualifying FID | Recommended Next Step | Condition |
|-------|-----------------|----------------|----------------------|-----------|
| F5-03 |                 |                | N/A                  | N/A       |
| F5-04 | N/A             | N/A            |                      | [COMMIT: concrete action \| no-build: exit trigger] |

Because (one citation per evidence sub-phase -- exactly 6 slots):
- PRIOR (Phase 0): [claim] because Phase 0, F0-[seq]
- INERTIA (Phase 1a): [claim] because Phase 1a, F1-[seq]
- RIVALS (Phase 1b): [claim] because Phase 1b, F1-[seq]
- FEASIBILITY (Phase 2): [claim] because Phase 2, F2-[seq]
- MARKET (Phase 3): [claim] because Phase 3, F3-[seq]
- WEB EVIDENCE (Phase 4): [claim] because Phase 4, F4-[seq]

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting -- V-04 R7 criterion analysis:**
- C-01 through C-22: All criteria from V-02 R7 hold. Phase 5 sub-table redesign does not
  affect gate annotations, FID citations, synthesis slot count, or hypothesis outcome structure.
  C-08 (hypothesis disposition explicit): F5-01 table has an "Outcome" column -- PASS.
  C-09 (confidence calibration narrative): F5-02 table has "Confidence Rationale (cite FIDs)"
  column -- PASS. C-10 (conditioned next step): F5-04 table has "Condition [COMMIT: concrete |
  no-build: exit trigger]" column -- PASS. C-18 (counter-evidence FID-pinned): F5-03 table
  has "Qualifying FID" column -- PASS. C-19 (hypothesis resolution FID-grounded): F5-01 table
  has "Resolving Evidence FID" column -- PASS.
- **C-23**: PASS strict. No `| Field | Value |` or inline rows anywhere. Every phase uses
  domain-specific column headers. Phase 4 column headers now include "Source Context" to
  reduce compression pressure on the quote cell. PASS under both liberal and strict
  interpretations. Most defensible C-23 evidence of any R7 variant.
- **C-24**: PASS. 6-slot Because block with separate Phase 1a and Phase 1b slots.
- **C-17 (v7)**: PASS. 6 slots, C-21 active.

**Phase 4 quote-fidelity note**: The "Source Context" column (added relative to V-02 R7)
provides a place for title, date, and author metadata, freeing the "Direct Quote" column to
hold only the verbatim string. This reduces the incentive to truncate quotes to fit a single
cell. A reviewer scoring C-23 sees 5 named columns on Phase 4 -- schema is fully visible in
the header row.

**Predicted v7 score**: 16/16 aspirational --> composite **100.0**.
Most structurally defensible 100.0 template: no interpretation ambiguity on C-23, no slot-count
ambiguity on C-24/C-17, quote-fidelity risk addressed.

---

## V-05 -- Combined: Conversational register + liberal C-23 + C-24

**Hypothesis**: V-05 R6 extended the canonical 22-criterion template into a conversational
phrasing register by adding explanatory prose before each phase while keeping gate annotations,
FINDING REGISTER, and Because format structurally identical to V-01 R6. Under v7, V-05 R6
scores 98.8 because it uses inline rows (C-23 FAIL) and a 5-slot Because block (C-24 FAIL).
V-05 R7 applies two targeted changes to V-05 R6: (a) convert all phase content from inline rows
to the liberal-interpretation table format used in V-02 R6 (preserving C-23 PASS), and (b) split
the Because block to 6 slots (C-24 PASS). The conversational prose wrapping each phase is
preserved -- tables replace only the inline FID rows, not the explanatory paragraphs. This tests
whether the narrative register survives the format change and whether a human-readable campaign
prompt can simultaneously satisfy the full 24-criterion bar.

Base: V-05 R6 (conversational, inline rows, 5-slot synthesis, 22/22 criteria under v6).
Combined changes:
1. All phase content: inline FID rows replaced by liberal-C-23 table format
   (| FID | Field | Value | for attribute phases; domain columns for record phases)
2. Because block: 5 slots expanded to 6 (INERTIA Phase 1a + RIVALS Phase 1b split)
3. Phase 5 preamble prose updated: "exactly five slots" changed to "exactly six slots"
4. All other conversational prose: identical to V-05 R6

```
Run the full pre-commitment decision campaign for: {{topic}}

Before gathering any evidence, we commit to a complete finding structure. Every finding
this campaign will produce -- from hypothesis through web evidence -- is registered here
with a placeholder value. This is not bureaucracy: registering slots before evidence
collection prevents the analyst from generating findings to fit a conclusion. Fill the
FINDING REGISTER first, then proceed to Phase 0.

---

## FINDING REGISTER [COMPLETE BEFORE PHASE 0]

Fill in the Value column when you reach each phase. Do not create new FIDs --
every finding slot this campaign needs is already allocated below.

| FID   | Phase              | Domain               | Value |
|-------|--------------------|----------------------|-------|
| F0-01 | Phase 0 (prior)    | Claim                | --    |
| F0-02 | Phase 0 (prior)    | Falsification cond.  | --    |
| F0-03 | Phase 0 (prior)    | Confidence prior     | --    |
| F0-04 | Phase 0 (prior)    | Prior rationale      | --    |
| F0-05 | Phase 0 (prior)    | Experiment 1         | --    |
| F0-06 | Phase 0 (prior)    | Experiment 2         | --    |
| F1-01 | Phase 1a (inertia) | Status-quo inertia   | --    |
| F1-02 | Phase 1a (inertia) | Switching cost       | --    |
| F1-03 | Phase 1a (inertia) | Good-enough thresh.  | --    |
| F1-04 | Phase 1b (rivals)  | Rival A              | --    |
| F1-05 | Phase 1b (rivals)  | Rival B              | --    |
| F2-01 | Phase 2 (feasib.)  | Tech complexity      | --    |
| F2-02 | Phase 2 (feasib.)  | Team capability      | --    |
| F2-03 | Phase 2 (feasib.)  | Timeline             | --    |
| F2-04 | Phase 2 (feasib.)  | Cost                 | --    |
| F2-05 | Phase 2 (feasib.)  | Overall feasibility  | --    |
| F2-06 | Phase 2 (feasib.)  | Top risk             | --    |
| F3-01 | Phase 3 (market)   | Addressable market   | --    |
| F3-02 | Phase 3 (market)   | Segment 1            | --    |
| F3-03 | Phase 3 (market)   | Segment 2            | --    |
| F3-04 | Phase 3 (market)   | Primary segment      | --    |
| F4-01 | Phase 4 (web)      | Source 1             | --    |
| F4-02 | Phase 4 (web)      | Source 2             | --    |
| F4-03 | Phase 4 (web)      | Source 3             | --    |
| F5-01 | Phase 5 (synth)    | Hypothesis outcome   | --    |
| F5-02 | Phase 5 (synth)    | Recommendation       | --    |
| F5-03 | Phase 5 (synth)    | Confidence           | --    |
| F5-04 | Phase 5 (synth)    | Confidence rationale | --    |
| F5-05 | Phase 5 (synth)    | Counter-evidence     | --    |
| F5-06 | Phase 5 (synth)    | Next step            | --    |

---

## Phase 0 -- prove-hypothesis [COMPLETE BEFORE PHASE 1]

State what you believe before you look at anything. The claim below is a prior -- a
bet you would make right now, before any competitor research or market data changes
your view. Write it down while it is still genuinely prior. Evidence collected in
Phases 1 through 4 will either confirm or challenge it.

| FID   | Field               | Value |
|-------|---------------------|-------|
| F0-01 | Claim               |       |
| F0-02 | Falsification cond. |       |
| F0-03 | Confidence prior    |       |
| F0-04 | Prior rationale     |       |
| F0-05 | Experiment 1        |       |
| F0-06 | Experiment 2        |       |

---

## Phase 1 -- scout-competitors [COMPLETE BEFORE PHASE 2]

### Phase 1a -- Inertia Analysis [COMPLETE BEFORE PHASE 1b]

The most important competitor in most markets is not a named product -- it is the
status quo. People have a cost of doing nothing and a threshold at which "good enough"
wins over "better." Understand why people stay put before naming any alternative. A
competitor analysis that opens with product names anchors on the wrong question.

| FID   | Field                 | Value |
|-------|-----------------------|-------|
| F1-01 | Status-quo inertia    |       |
| F1-02 | Switching cost        |       |
| F1-03 | Good-enough threshold |       |

### Phase 1b -- Named Rivals

With inertia established, name the products or approaches that actively compete.

| FID   | Name | Threat (Low/Med/High) | Notes (one sentence) |
|-------|------|-----------------------|----------------------|
| F1-04 |      |                       |                      |
| F1-05 |      |                       |                      |

---

## Phase 2 -- scout-feasibility [COMPLETE BEFORE PHASE 3]

| FID   | Dimension            | Rating (R/Y/G) | Reason |
|-------|----------------------|----------------|--------|
| F2-01 | Technical complexity |                |        |
| F2-02 | Team capability      |                |        |
| F2-03 | Timeline             |                |        |
| F2-04 | Cost                 |                |        |
| F2-05 | Overall feasibility  |                |        |
| F2-06 | Top risk             |                |        |

---

## Phase 3 -- scout-market [COMPLETE BEFORE PHASE 4]

| FID   | Field              | Value |
|-------|--------------------|-------|
| F3-01 | Addressable market |       |
| F3-02 | Segment 1          |       |
| F3-03 | Segment 2          |       |
| F3-04 | Primary segment    |       |

---

## Phase 4 -- prove-websearch [COMPLETE BEFORE PHASE 5]

| FID   | Source | Direct quote (not paraphrase) | Strength | Verdict |
|-------|--------|-------------------------------|----------|---------|
| F4-01 |        |                               |          |         |
| F4-02 |        |                               |          |         |
| F4-03 |        |                               |          |         |

---

## Phase 5 -- prove-synthesize

The Because block below is the audit trail. Each slot carries one citation from one
evidence sub-phase using the format "because Phase N, F[N]-seq" -- the phase prefix
proves which sub-phase the claim comes from; the FID key pins the specific finding in
the register. Phase 1 is split into two sub-phases (inertia and rivals) to mirror
the structural separation in the evidence layer, so exactly six slots are required.
A missing slot means that sub-phase's evidence didn't reach the recommendation.

| FID   | Field                | Value |
|-------|----------------------|-------|
| F5-01 | Hypothesis outcome   | [Confirmed/Refuted/Inconclusive -- resolves F0-01] |
| F5-02 | Recommendation       | [COMMIT/PAUSE/PIVOT/ABANDON] |
| F5-03 | Confidence           | [High/Medium/Low] |
| F5-04 | Confidence rationale | [cite FIDs that drove this rating -- not the label alone] |
| F5-05 | Counter-evidence     | [one risk or caveat -- cite the FID it qualifies] |
| F5-06 | Next step            | [COMMIT: concrete action | no-build: exit condition or revisit trigger] |

Because (one citation per evidence sub-phase -- exactly 6 slots):
- PRIOR (Phase 0): [claim] because Phase 0, F0-[seq]
- INERTIA (Phase 1a): [claim] because Phase 1a, F1-[seq]
- RIVALS (Phase 1b): [claim] because Phase 1b, F1-[seq]
- FEASIBILITY (Phase 2): [claim] because Phase 2, F2-[seq]
- MARKET (Phase 3): [claim] because Phase 3, F3-[seq]
- WEB EVIDENCE (Phase 4): [claim] because Phase 4, F4-[seq]

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting -- V-05 R7 criterion analysis:**
- C-01 through C-22: All criteria from V-05 R6 hold. The conversational prose paragraphs are
  body text, not header text -- they do not interfere with gate annotations (C-20), structural
  split (C-21), or citation format (C-22). Table format replacing inline rows does not affect
  any criterion scored on the structural or behavioral level.
- **C-23**: PASS liberal. Same table format as V-01 R7 and V-02 R6. `| FID | Field | Value |`
  3-column format for Phases 0, 1a, 3, 5. Domain-column format for Phases 2 (Dimension/Rating/
  Reason) and 4 (Source/Quote/Strength/Verdict). The R6 rubric grader accepted this format for
  C-23. A strict scorer would note the `| Field | Value |` columns -- see C-23 strict note.
- **C-24**: PASS. Because block has 6 labeled slots with separate Phase 1a and Phase 1b entries.
  Phase 5 preamble explicitly explains the 6-slot rationale ("Phase 1 is split into two sub-phases
  to mirror the structural separation in the evidence layer").
- **C-17 (v7)**: PASS. 6 slots, C-21 active.
- **C-09 (confidence calibration)**: The conversational Phase 5 preamble explains the Because
  block's purpose as an "audit trail." The F5-04 field explicitly requires "cite FIDs that drove
  this rating -- not the label alone." PASS.

**Conversational prose interaction test**: The Phase 0 preamble ("State what you believe before
you look at anything...") precedes the Phase 0 table. This prose does NOT replace the table --
it explains the table. C-23 scores the presence of column-header schema in the phase table, not
the surrounding prose. The prose is body text; the table is the evidence structure. No criterion
is harmed by the explanatory prose, and C-09 (confidence calibration narrative) is strengthened
by the Phase 5 preamble.

**Register coherence test**: V-05 R6's preamble said "Five evidence phases = exactly five slots."
V-05 R7's preamble now says "exactly six slots" with an explanation of WHY (the Phase 1a/1b split
mirrors the evidence layer). This is the only place in the conversational register where the slot-
count rationale is explicitly taught to the filler. No other variant explains WHY there are 6 slots
-- V-05 R7 does, making it the most pedagogically transparent variant.

**C-23 strict/liberal residual**: Phases 0, 1a, 3, and 5 use `| FID | Field | Value |` format
(same as V-01 R7 and V-02 R6). The liberal interpretation (3-column table accepted) gives
C-23 PASS. A strict scorer would distinguish "Field" as a generic column label from domain-
specific labels and fail these phases. V-04 R7 resolves the ambiguity for use cases where
strict compliance is required; V-05 R7 prioritizes readability over strict compliance.

**Predicted v7 score**: 16/16 aspirational --> composite **100.0** (liberal C-23).
Under strict C-23 interpretation: 15/16 (same as V-02 R6) --> composite **99.4**.

---

## R7 Predicted Score Summary

| Variant | C-23 | C-24 | C-17 (v7) | Aspirational pts | v7 Composite |
|---------|------|------|-----------|-----------------|--------------|
| V-01 R7 (V-02 R6 + 6-slot Because) | PASS liberal | PASS | PASS | 16/16 x 10 = 10.0 | **100.0** |
| V-02 R7 (strict C-23 + 6-slot + domain cols) | PASS strict | PASS | PASS | 16/16 x 10 = 10.0 | **100.0** |
| V-03 R7 (Phase 5 col decomp only, 5-slot) | FAIL (inline phases 0-4) | FAIL | PASS liberal | 14/16 x 10 = 8.75 | **98.8** |
| V-04 R7 (strict C-23 + C-24 + Phase 5 refined) | PASS strict | PASS | PASS | 16/16 x 10 = 10.0 | **100.0** |
| V-05 R7 (conversational + liberal C-23 + C-24) | PASS liberal | PASS | PASS | 16/16 x 10 = 10.0 | **100.0 (liberal)** |

V-01 R7 is the minimal convergence proof: one change (Because block split) on the nearest
passing template (V-02 R6 at 99.4). V-02 R7 eliminates all C-23 scoring ambiguity. V-03 R7
documents the Phase 5 column technique in isolation. V-04 R7 is the most robust combined
template -- strict C-23 + C-24 + no quote-fidelity risk. V-05 R7 extends the conversational
register to full 24-criterion coverage without sacrificing readability.

The first template to pass all 24 criteria under any interpretation is V-02 R7 (strict C-23
compliance, no residual scoring debates). V-04 R7 adds the Phase 4 quote-fidelity refinement
as the production-ready variant for V-02 R7's design intent.
