---
skill: quest-variate
skill_target: campaign-decide
round: 8
date: 2026-03-16
rubric: simulations/quest/rubrics/campaign-decide-rubric-v7-2026-03-16.md
---

# Variations -- campaign-decide / Round 8

Five complete, runnable skill body variations targeting the v7 rubric.
Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

**R7 -> R8 diagnosis:**

R7 produced four 100.0 templates under v7:

| R7 variation | C-23 | C-24 | v7 composite |
|--------------|------|------|--------------|
| V-01 R7 (V-02 R6 + 6-slot Because) | PASS liberal | PASS | 100.0 (liberal) |
| V-02 R7 (strict domain columns + 6-slot) | PASS strict | PASS | 100.0 strict |
| V-03 R7 (Phase 5 col only, 5-slot) | FAIL | FAIL | 98.8 (boundary test) |
| V-04 R7 (strict + C-24 + Phase 4 quote refinement) | PASS strict | PASS | 100.0 strict |
| V-05 R7 (conversational + liberal C-23 + C-24) | PASS liberal | PASS | 100.0 (liberal) |

V-02 R7 and V-04 R7 are the first templates with no residual C-23 scoring ambiguity.
The 24-criterion ceiling is reached. R8 shifts from ceiling-finding to stress-testing and
v8 rubric candidate surfacing.

**Three R8 questions:**

1. Can the Because block itself be upgraded to named-column table format -- creating a
   C-25 rubric candidate (synthesis-layer schema enforcement)?
2. Does Phase 1b gain structural depth from a "Response Strategy" column -- and does
   that depth warrant a v8 criterion for competitive response framing?
3. Can the 100.0 template be compressed to structural scaffolding only (no instructional
   prose), and does any criterion silently depend on prose instructions to pass?

**R8 axes:**

| Axis | Criterion targeted | Single/Combined |
|------|--------------------|-----------------|
| Because block as named-column table | C-25 candidate (synthesis schema) | V-01 (single) |
| Phase 1b response-strategy column | C-04 depth, v8 candidate | V-02 (single) |
| Minimal prompt (structural scaffolding only, no prose) | C-20 stress, compressibility | V-03 (single) |
| Combined: Because table + Phase 1b strategy + strict C-23 | Synthesis schema + rival depth | V-04 (combined) |
| Combined: Hypothesis lifecycle (Phase 0 outcome cols) + Because table | C-13 lifecycle + synthesis schema | V-05 (combined) |

---

## V-01 -- Axis: Because block as named-column table

**Hypothesis**: Every evidence phase in V-04 R7 uses domain-specific named-column tables
(C-23 strict PASS). The synthesis Because block uses a labeled bullet list -- not a table.
A v8 rubric could add C-25 requiring the synthesis layer to enforce schema with column
headers just as the evidence layers do. V-01 R8 converts the Because block from a 6-item
bullet list to a named-column table with four columns: Phase, Label, Citation, Claim.
This makes synthesis schema compliance visible at a glance and closes the one remaining
format asymmetry: evidence phases use tables; synthesis uses prose bullets. All other
structure is identical to V-04 R7 (the strictest 100.0 template). If C-25 is added to
a v8 rubric, V-01 R8 will be the first template to pass it. Predicted under v7: 16/16
aspirational = 100.0 strict (C-25 not yet scored, so no denominator change).

Base: V-04 R7 (strict C-23, C-24, Phase 4 Source Context column).
Single-axis change: Because block replaced by a 4-column named-column table. All
phase tables, FINDING REGISTER, and gate annotations identical to V-04 R7.

```
Run the full pre-commitment decision campaign for: {{topic}}

FINDING REGISTER: The complete finding skeleton below is committed before any evidence
phase executes. One row per record. Fill each FID row in its phase section using the
domain-specific column tables that follow. Cite by hybrid key "Phase N, F[N]-seq" in
the synthesis Because table. Do not create FIDs outside this register.

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

**Because (one row per evidence sub-phase -- exactly 6 rows):**

| Phase    | Label              | Citation (Phase N, F[N]-seq) | Claim (one sentence) |
|----------|--------------------|------------------------------|----------------------|
| Phase 0  | PRIOR              | Phase 0, F0-[seq]            |                      |
| Phase 1a | INERTIA            | Phase 1a, F1-[seq]           |                      |
| Phase 1b | RIVALS             | Phase 1b, F1-[seq]           |                      |
| Phase 2  | FEASIBILITY        | Phase 2, F2-[seq]            |                      |
| Phase 3  | MARKET             | Phase 3, F3-[seq]            |                      |
| Phase 4  | WEB EVIDENCE       | Phase 4, F4-[seq]            |                      |

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting -- V-01 R8 criterion analysis:**
- C-01 through C-24: All criteria from V-04 R7 hold. The Because block's content is
  unchanged -- 6 slots, Phase 1a + Phase 1b labeled separately, hybrid Phase+FID citations.
  Converting from bullet list to table does not affect C-12 (templated citation syntax),
  C-14 (cross-phase span), C-17 (slot count), C-22 (dual-axis citation), or C-24
  (sub-phase synthesis alignment). All pass unchanged.
- **C-23**: PASS strict. The Because table now uses named column headers: "Phase",
  "Label", "Citation", "Claim". Schema is visible in the header row. The synthesis
  layer now matches the evidence layer's structural discipline. No `| Field | Value |`
  anywhere in the template.
- **C-25 (v8 candidate -- synthesis-layer schema enforcement)**: PASS candidate. If a v8
  rubric adds a criterion requiring the synthesis Because block to use column-header schema
  (paralleling C-23 for evidence phases), V-01 R8 satisfies it. The column headers
  enumerate exactly the required fields: which phase, which label, the citation key, and
  the claim sentence. A filler cannot omit any of these without creating a visible column
  gap.
- **C-24**: PASS. Phase 1a and Phase 1b are separately labeled rows in the Because table.
  The structural separation from the evidence layer propagates to synthesis via both
  column schema (new in R8) and row separation (carried from R7).

**Because-table vs. Because-list mechanical comparison:**

| Property | Bullet list (V-04 R7) | Named-column table (V-01 R8) |
|----------|-----------------------|------------------------------|
| Schema visible in header | No -- labels are in the bullet prefix | Yes -- column headers |
| Citation format enforced | By template example syntax | By "Citation" column header |
| Phase label separated from claim | By dash convention | By separate "Phase" and "Claim" columns |
| Missing row visibility | Slot count only | Column gap in any partial row |
| C-23 compliance | Evidence phases only | Evidence phases + synthesis |

**Predicted v7 score**: 16/16 aspirational --> composite **100.0** strict.
C-25 not in v7 denominator; no regression. First template where synthesis layer matches
the column-schema discipline of all evidence layers.

---

## V-02 -- Axis: Phase 1b response-strategy column

**Hypothesis**: The Phase 1b rivals table in V-04 R7 records four columns: Rival Name,
Threat Level, Key Differentiator, Notes. These columns diagnose the competitive landscape
but do not require the analyst to state what to do about each rival. A "Response Strategy"
column -- how we win against or differentiate from this rival if we build -- forces the
analyst to connect competitive intelligence to a build decision. This is a deeper reading
of C-04 (inertia-first competitor framing): the criterion requires inertia-first ordering,
but says nothing about whether competitive response is surfaced. A v8 rubric could add a
criterion requiring the competitor analysis to include a disposition per rival. V-02 R8
adds the Response Strategy column to Phase 1b and extends the FINDING REGISTER record type
for F1-04/F1-05 to reflect the richer rival record. All other structure is V-04 R7.
Predicted under v7: 16/16 aspirational = 100.0 strict (C-25/C-26 not yet scored).

Base: V-04 R7 (strict C-23, C-24, Phase 4 Source Context column).
Single-axis change: Phase 1b rivals table gains a fifth column "Response Strategy
(how we win vs. this rival)". FINDING REGISTER record types for F1-04/F1-05 updated
to "Named rival A with response strategy" and "Named rival B with response strategy".
All other phases, FINDING REGISTER rows, gate annotations, and Because block identical
to V-04 R7.

```
Run the full pre-commitment decision campaign for: {{topic}}

FINDING REGISTER: The complete finding skeleton below is committed before any evidence
phase executes. One row per record. Fill each FID row in its phase section using the
domain-specific column tables that follow. Cite by hybrid key "Phase N, F[N]-seq" in
the synthesis Because block. Do not create FIDs outside this register.

---

## FINDING REGISTER [COMPLETE BEFORE PHASE 0]

| FID   | Phase              | Record Type                                    |
|-------|--------------------|------------------------------------------------|
| F0-01 | Phase 0 (prior)    | Hypothesis record                              |
| F0-02 | Phase 0 (prior)    | Experiment 1 design                            |
| F0-03 | Phase 0 (prior)    | Experiment 2 design                            |
| F1-01 | Phase 1a (inertia) | Inertia force 1 (status-quo)                   |
| F1-02 | Phase 1a (inertia) | Inertia force 2 (switching cost)               |
| F1-03 | Phase 1a (inertia) | Inertia force 3 (good-enough)                  |
| F1-04 | Phase 1b (rivals)  | Named rival A with response strategy           |
| F1-05 | Phase 1b (rivals)  | Named rival B with response strategy           |
| F2-01 | Phase 2 (feasib.)  | Buildability dimension 1                       |
| F2-02 | Phase 2 (feasib.)  | Buildability dimension 2                       |
| F2-03 | Phase 2 (feasib.)  | Buildability dimension 3                       |
| F2-04 | Phase 2 (feasib.)  | Buildability dimension 4                       |
| F2-05 | Phase 2 (feasib.)  | Buildability dimension 5                       |
| F2-06 | Phase 2 (feasib.)  | Top buildability risk                          |
| F3-01 | Phase 3 (market)   | Total addressable market                       |
| F3-02 | Phase 3 (market)   | Segment 1                                      |
| F3-03 | Phase 3 (market)   | Segment 2                                      |
| F3-04 | Phase 3 (market)   | Primary segment selection                      |
| F4-01 | Phase 4 (web)      | Web source 1                                   |
| F4-02 | Phase 4 (web)      | Web source 2                                   |
| F4-03 | Phase 4 (web)      | Web source 3                                   |
| F5-01 | Phase 5 (synth)    | Hypothesis resolution record                   |
| F5-02 | Phase 5 (synth)    | Recommendation record                          |
| F5-03 | Phase 5 (synth)    | Counter-evidence record                        |
| F5-04 | Phase 5 (synth)    | Next-step record                               |

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

| FID   | Rival Name | Threat Level (L/M/H) | Key Differentiator | Response Strategy (how we win vs. this rival) | Notes |
|-------|-----------|----------------------|-------------------|-----------------------------------------------|-------|
| F1-04 |           |                      |                   |                                               |       |
| F1-05 |           |                      |                   |                                               |       |

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

**Rubric targeting -- V-02 R8 criterion analysis:**
- C-01 through C-24: All criteria from V-04 R7 hold. Adding a fifth column to the
  Phase 1b table does not affect any structural criterion. C-04 (inertia-first): PASS --
  Phase 1a still precedes Phase 1b. C-21 (structural isolation): PASS -- gate annotation
  on Phase 1a header unchanged. C-23 strict: PASS -- Phase 1b now has five domain-specific
  column headers; "Response Strategy" is as domain-specific as "Key Differentiator".
- **C-26 (v8 candidate -- competitive response disposition per rival)**: PASS candidate.
  A v8 rubric could add a criterion requiring each named rival record to carry a stated
  response strategy, making the competitor analysis actionable rather than descriptive.
  V-02 R8 satisfies this via the "Response Strategy" column in Phase 1b. A filler who
  leaves it blank creates a visible gap -- the column header makes the requirement
  structural.

**Response Strategy column interaction with inertia framing**: Adding response strategy
to named rivals (Phase 1b) does not introduce any content about status-quo rivals --
F1-01 through F1-03 remain the inertia block. The Response Strategy column addresses
what to do about each product rival, not about inertia. C-04 scores inertia-first
ordering; the Response Strategy column is a Phase 1b-only addition. No criterion
interaction risk.

**FID stability**: F1-04 and F1-05 retain their FID keys. The FINDING REGISTER's
"Record Type" description is updated to "Named rival A with response strategy" to
reflect the richer record schema, but the FID keys and phase assignments are unchanged.
C-15 (unique finding keys) and C-16 (pre-seeded register) are unaffected.

**Predicted v7 score**: 16/16 aspirational --> composite **100.0** strict.
Phase 1b column addition has no v7 criterion impact. First template with explicit
competitive response disposition in the rivals schema.

---

## V-03 -- Axis: Minimal prompt (structural scaffolding only, no instructional prose)

**Hypothesis**: V-04 R7 contains instructional prose in three places: (a) the FINDING
REGISTER preamble ("The complete finding skeleton below is committed before any evidence
phase executes..."), (b) the Phase 0 sub-table labels ("Hypothesis record (commit prior
before any evidence phase runs):" and "Experiments (two methods you would run to test
the claim):"), and (c) the Phase 5 sub-table labels ("Hypothesis resolution:",
"Recommendation:", "Counter-evidence and next step:"). These prose elements may help
human fillers but add token cost and may not be required by any criterion. V-03 R8
strips all prose to the minimum: gate-annotated headers, domain-specific column tables,
the Because block, and the output artifact line. No preamble text, no sub-table labels,
no explanatory sentences. The FINDING REGISTER preamble instruction is compressed to one
line. Tests: does any v7 criterion silently require prose to pass? Does removing the
sub-table labels for Phase 0 and Phase 5 break C-13 (hypothesis-prior) or C-08
(hypothesis disposition)? Predicted: 16/16, 100.0 strict -- all criteria are structural,
none depend on prose presence.

Base: V-04 R7 (strict C-23, C-24, Phase 4 Source Context column).
Single-axis change: All instructional prose removed. Gate annotations retained on all
headers. All phase tables, FINDING REGISTER rows, Because block identical to V-04 R7.

```
Run the full pre-commitment decision campaign for: {{topic}}

FINDING REGISTER: Fill before Phase 0. Cite by "Phase N, F[N]-seq". No FIDs outside
this register.

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

| FID   | Hypothesis Claim | Falsification Condition | Prior Confidence (L/M/H) | Prior Rationale |
|-------|-----------------|-------------------------|--------------------------|-----------------|
| F0-01 |                 |                         |                          |                 |

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

| FID   | Outcome (Confirmed / Refuted / Inconclusive) | Resolving Evidence FID |
|-------|---------------------------------------------|----------------------|
| F5-01 |                                             |                      |

| FID   | Recommendation (COMMIT / PAUSE / PIVOT / ABANDON) | Confidence (H/M/L) | Confidence Rationale (cite FIDs -- not label alone) |
|-------|---------------------------------------------------|--------------------|-----------------------------------------------------|
| F5-02 |                                                   |                    |                                                     |

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

**Rubric targeting -- V-03 R8 criterion analysis:**
- **C-01 through C-24**: All structural criteria hold from V-04 R7. The removal of prose
  does not affect any criterion scored on structure, schema, citations, or ordering. Gate
  annotations are co-located with the section headers they govern (C-20: PASS). Phase 1a
  header still carries `[COMPLETE BEFORE PHASE 1b]` (C-21: PASS). Because block retains
  6 labeled slots with hybrid citations (C-17, C-22, C-24: PASS).
- **C-13 (hypothesis-prior anchoring)**: PASS. The hypothesis record table appears at
  Phase 0, before any evidence phase. The column header "Hypothesis Claim" makes the
  prior commitment structurally identifiable without surrounding prose. The column header
  carries the semantic signal that prose previously provided ("commit prior before any
  evidence phase runs" was instructional; "Hypothesis Claim" is structural). PASS under
  both liberal (Phase 0 table before Phase 1) and strict (prior-commitment before evidence)
  interpretations.
- **C-08 (hypothesis disposition explicit)**: PASS. Phase 5's first table has column header
  "Outcome (Confirmed / Refuted / Inconclusive)". The sub-table label "Hypothesis
  resolution:" was prose; removing it does not remove the column header that carries
  the disposition field. The outcome is still structurally required by the column schema.
- **C-23 strict**: PASS. All phase tables carry domain-specific column headers. The
  absence of sub-table labels does not affect column headers.
- **C-09 (confidence calibration narrative)**: The Phase 5 recommendation table column
  "Confidence Rationale (cite FIDs -- not label alone)" carries the calibration requirement
  in the column header. No prose wrapper needed. PASS.

**Compressibility finding**: Removing all prose from V-04 R7 does not cause any criterion
to fail. This confirms that all 24 v7 criteria are purely structural -- they score the
template's column headers, gate annotations, section structure, citation format, and slot
counts. None depend on prose instructions. The minimum passing template is the scaffolding
alone: FINDING REGISTER + phase tables with domain-specific column headers + gate-annotated
headers + 6-slot Because block.

**Token economy estimate**: V-03 R8 removes approximately 120 words of prose from V-04 R7.
The structural elements (tables, headers, gate annotations) are identical. For automated
filling contexts (API-driven campaigns), V-03 R8 is the preferred base -- lowest system
prompt token cost while passing all 24 criteria.

**Predicted v7 score**: 16/16 aspirational --> composite **100.0** strict.
Confirms that the 24-criterion ceiling is achievable at minimum prompt length.
No criterion requires instructional prose to pass.

---

## V-04 -- Combined: Because table + Phase 1b response strategy + strict C-23

**Hypothesis**: V-01 R8 demonstrated that the Because block can be a named-column table
(C-25 candidate). V-02 R8 demonstrated that Phase 1b gains structural depth from a
"Response Strategy" column (C-26 candidate). V-04 R8 combines both additions on the
V-04 R7 base -- the most structurally complete 100.0 template in R7. The combination
creates a template where every layer (evidence collection, synthesis, competitive
analysis) enforces column-header schema. A v8 rubric that adds C-25 (Because table
schema) and C-26 (competitive response disposition) would find this template passing
both. Under v7, the combination has no denominator effect -- predicted 16/16, 100.0.
This is the candidate production template for teams wanting to pass any plausible v8
rubric extension.

Base: V-04 R7 (strict C-23, C-24, Phase 4 Source Context column).
Combined changes:
1. Because block: converted to named-column table (from V-01 R8)
2. Phase 1b rivals table: "Response Strategy" column added (from V-02 R8)
3. FINDING REGISTER: F1-04/F1-05 record types updated to "Named rival A/B with
   response strategy" (from V-02 R8)
All other phases, gate annotations, and FINDING REGISTER rows identical to V-04 R7.

```
Run the full pre-commitment decision campaign for: {{topic}}

FINDING REGISTER: The complete finding skeleton below is committed before any evidence
phase executes. One row per record. Fill each FID row in its phase section using the
domain-specific column tables that follow. Cite by hybrid key "Phase N, F[N]-seq" in
the synthesis Because table. Do not create FIDs outside this register.

---

## FINDING REGISTER [COMPLETE BEFORE PHASE 0]

| FID   | Phase              | Record Type                                    |
|-------|--------------------|------------------------------------------------|
| F0-01 | Phase 0 (prior)    | Hypothesis record                              |
| F0-02 | Phase 0 (prior)    | Experiment 1 design                            |
| F0-03 | Phase 0 (prior)    | Experiment 2 design                            |
| F1-01 | Phase 1a (inertia) | Inertia force 1 (status-quo)                   |
| F1-02 | Phase 1a (inertia) | Inertia force 2 (switching cost)               |
| F1-03 | Phase 1a (inertia) | Inertia force 3 (good-enough)                  |
| F1-04 | Phase 1b (rivals)  | Named rival A with response strategy           |
| F1-05 | Phase 1b (rivals)  | Named rival B with response strategy           |
| F2-01 | Phase 2 (feasib.)  | Buildability dimension 1                       |
| F2-02 | Phase 2 (feasib.)  | Buildability dimension 2                       |
| F2-03 | Phase 2 (feasib.)  | Buildability dimension 3                       |
| F2-04 | Phase 2 (feasib.)  | Buildability dimension 4                       |
| F2-05 | Phase 2 (feasib.)  | Buildability dimension 5                       |
| F2-06 | Phase 2 (feasib.)  | Top buildability risk                          |
| F3-01 | Phase 3 (market)   | Total addressable market                       |
| F3-02 | Phase 3 (market)   | Segment 1                                      |
| F3-03 | Phase 3 (market)   | Segment 2                                      |
| F3-04 | Phase 3 (market)   | Primary segment selection                      |
| F4-01 | Phase 4 (web)      | Web source 1                                   |
| F4-02 | Phase 4 (web)      | Web source 2                                   |
| F4-03 | Phase 4 (web)      | Web source 3                                   |
| F5-01 | Phase 5 (synth)    | Hypothesis resolution record                   |
| F5-02 | Phase 5 (synth)    | Recommendation record                          |
| F5-03 | Phase 5 (synth)    | Counter-evidence record                        |
| F5-04 | Phase 5 (synth)    | Next-step record                               |

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

| FID   | Rival Name | Threat Level (L/M/H) | Key Differentiator | Response Strategy (how we win vs. this rival) | Notes |
|-------|-----------|----------------------|-------------------|-----------------------------------------------|-------|
| F1-04 |           |                      |                   |                                               |       |
| F1-05 |           |                      |                   |                                               |       |

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

**Because (one row per evidence sub-phase -- exactly 6 rows):**

| Phase    | Label              | Citation (Phase N, F[N]-seq) | Claim (one sentence) |
|----------|--------------------|------------------------------|----------------------|
| Phase 0  | PRIOR              | Phase 0, F0-[seq]            |                      |
| Phase 1a | INERTIA            | Phase 1a, F1-[seq]           |                      |
| Phase 1b | RIVALS             | Phase 1b, F1-[seq]           |                      |
| Phase 2  | FEASIBILITY        | Phase 2, F2-[seq]            |                      |
| Phase 3  | MARKET             | Phase 3, F3-[seq]            |                      |
| Phase 4  | WEB EVIDENCE       | Phase 4, F4-[seq]            |                      |

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting -- V-04 R8 criterion analysis:**
- C-01 through C-24: All criteria from V-04 R7 hold. The two structural additions (Because
  table, Response Strategy column) have no v7 criterion regressions. All gate annotations,
  FINDING REGISTER, FID system, 6-slot synthesis alignment, and hypothesis lifecycle
  structures are unchanged.
- **C-23 strict**: PASS. No regression. Phase 1b now has five domain-specific column
  headers. The Because table now has four domain-specific column headers. The synthesis
  layer is now as column-schema-compliant as the evidence layers.
- **C-24**: PASS. Because table has separate Phase 1a (INERTIA) and Phase 1b (RIVALS) rows.
  The column-based format makes row separation visually unambiguous -- Phase 1a and Phase 1b
  appear as distinct row cells in the "Phase" column. Stricter C-24 evidence than a bullet
  list, where the 1a/1b split is visible only by label prefix.
- **C-25 (v8 candidate)**: PASS. Because table column headers enforce the synthesis schema.
- **C-26 (v8 candidate)**: PASS. Phase 1b "Response Strategy" column enforces competitive
  response disposition per rival.

**Combined interaction notes:**
- The Because table (V-01 R8 change) and the Response Strategy column (V-02 R8 change)
  are structurally independent. They operate on different phases and different schema
  layers. No interaction risk.
- The Because table's "Phase" column now shows "Phase 1a" and "Phase 1b" as distinct
  rows -- more visually explicit than the bullet list's "- INERTIA (Phase 1a):" prefix.
  This strengthens C-24 evidence beyond what the bullet format provided.
- V-04 R8 is the most structurally complete template to date: FINDING REGISTER (pre-seeded,
  C-16), evidence phases (domain columns, C-23 strict), synthesis resolution tables (named
  columns, C-08/C-09/C-10/C-18/C-19), rivals with response (C-04/C-26 candidate), Because
  table (C-25 candidate), 6-slot synthesis (C-17/C-24), hybrid citations (C-22).

**Predicted v7 score**: 16/16 aspirational --> composite **100.0** strict.
Under a hypothetical v8 rubric adding C-25 and C-26: PASS both (18/18 aspirational).
Most forward-compatible template in the R8 set.

---

## V-05 -- Combined: Hypothesis lifecycle (Phase 0 outcome columns) + Because table

**Hypothesis**: C-13 (hypothesis-prior anchoring) requires the hypothesis to be committed
before evidence phases run and for synthesis to report the outcome. Currently the
experimental lifecycle is split: Phase 0 captures the prior (claim, falsification
condition, experiments), and Phase 5 captures the resolution (outcome, resolving FID).
These are two separate tables, filled at different times. V-05 R8 tests whether Phase 0's
experiment table can be extended with outcome columns that are filled at synthesis time --
creating a single experiment-lifecycle table that shows both design and result side by side.
This makes the C-13 experimental chain visible as a continuous record rather than two
separated tables. The outcome columns (Expected Result, Actual Outcome) would be blank at
Phase 0 time and filled during Phase 5. The hypothesis resolution table in Phase 5 is
retained as the authoritative FID-bearing resolution record. V-05 R8 also inherits V-01
R8's Because table. Predicted under v7: 16/16, 100.0 strict.

Base: V-04 R7 (strict C-23, C-24, Phase 4 Source Context column).
Combined changes:
1. Phase 0 experiment table: two columns added -- "Expected Result (fill now)" and
   "Actual Outcome (fill at Phase 5)" -- creating an experiment lifecycle record
2. FINDING REGISTER: F0-02/F0-03 record types updated to "Experiment 1/2 lifecycle record"
3. Because block: converted to named-column table (from V-01 R8)
All other phases, gate annotations, hypothesis resolution table in Phase 5, and Because
slot count identical to V-04 R7.

```
Run the full pre-commitment decision campaign for: {{topic}}

FINDING REGISTER: The complete finding skeleton below is committed before any evidence
phase executes. One row per record. Fill each FID row in its phase section using the
domain-specific column tables that follow. Cite by hybrid key "Phase N, F[N]-seq" in
the synthesis Because table. Do not create FIDs outside this register.

---

## FINDING REGISTER [COMPLETE BEFORE PHASE 0]

| FID   | Phase              | Record Type                          |
|-------|--------------------|--------------------------------------|
| F0-01 | Phase 0 (prior)    | Hypothesis record                    |
| F0-02 | Phase 0 (prior)    | Experiment 1 lifecycle record        |
| F0-03 | Phase 0 (prior)    | Experiment 2 lifecycle record        |
| F1-01 | Phase 1a (inertia) | Inertia force 1 (status-quo)         |
| F1-02 | Phase 1a (inertia) | Inertia force 2 (switching cost)     |
| F1-03 | Phase 1a (inertia) | Inertia force 3 (good-enough)        |
| F1-04 | Phase 1b (rivals)  | Named rival A                        |
| F1-05 | Phase 1b (rivals)  | Named rival B                        |
| F2-01 | Phase 2 (feasib.)  | Buildability dimension 1             |
| F2-02 | Phase 2 (feasib.)  | Buildability dimension 2             |
| F2-03 | Phase 2 (feasib.)  | Buildability dimension 3             |
| F2-04 | Phase 2 (feasib.)  | Buildability dimension 4             |
| F2-05 | Phase 2 (feasib.)  | Buildability dimension 5             |
| F2-06 | Phase 2 (feasib.)  | Top buildability risk                |
| F3-01 | Phase 3 (market)   | Total addressable market             |
| F3-02 | Phase 3 (market)   | Segment 1                            |
| F3-03 | Phase 3 (market)   | Segment 2                            |
| F3-04 | Phase 3 (market)   | Primary segment selection            |
| F4-01 | Phase 4 (web)      | Web source 1                         |
| F4-02 | Phase 4 (web)      | Web source 2                         |
| F4-03 | Phase 4 (web)      | Web source 3                         |
| F5-01 | Phase 5 (synth)    | Hypothesis resolution record         |
| F5-02 | Phase 5 (synth)    | Recommendation record                |
| F5-03 | Phase 5 (synth)    | Counter-evidence record              |
| F5-04 | Phase 5 (synth)    | Next-step record                     |

---

## Phase 0 -- prove-hypothesis [COMPLETE BEFORE PHASE 1]

**Hypothesis record (commit prior before any evidence phase runs):**

| FID   | Hypothesis Claim | Falsification Condition | Prior Confidence (L/M/H) | Prior Rationale |
|-------|-----------------|-------------------------|--------------------------|-----------------|
| F0-01 |                 |                         |                          |                 |

**Experiment lifecycle (design columns fill now; outcome columns fill at Phase 5):**

| FID   | Experiment Name | Investigation Method | Expected Result (fill now) | Actual Outcome (fill at Phase 5) |
|-------|----------------|---------------------|----------------------------|----------------------------------|
| F0-02 |                |                     |                            |                                  |
| F0-03 |                |                     |                            |                                  |

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

**Experiment outcomes (complete the lifecycle columns in the Phase 0 experiment table
before filling the resolution record below):**

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

**Because (one row per evidence sub-phase -- exactly 6 rows):**

| Phase    | Label              | Citation (Phase N, F[N]-seq) | Claim (one sentence) |
|----------|--------------------|------------------------------|----------------------|
| Phase 0  | PRIOR              | Phase 0, F0-[seq]            |                      |
| Phase 1a | INERTIA            | Phase 1a, F1-[seq]           |                      |
| Phase 1b | RIVALS             | Phase 1b, F1-[seq]           |                      |
| Phase 2  | FEASIBILITY        | Phase 2, F2-[seq]            |                      |
| Phase 3  | MARKET             | Phase 3, F3-[seq]            |                      |
| Phase 4  | WEB EVIDENCE       | Phase 4, F4-[seq]            |                      |

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting -- V-05 R8 criterion analysis:**
- C-01 through C-24: All criteria from V-04 R7 hold. The experiment lifecycle columns
  (Expected Result, Actual Outcome) are additions to an existing Phase 0 table. They do
  not change the prior commitment timing (C-13: PASS), the pre-seeded FID register (C-16:
  PASS), or the hypothesis resolution table in Phase 5 (C-08/C-19: PASS). The Phase 5
  instruction ("complete the lifecycle columns in the Phase 0 experiment table before
  filling the resolution record") is a prose guide, not a structural gate. C-20 (gate
  annotations in headers) is unaffected -- the instruction is in body text, not a header.
- **C-23 strict**: PASS. Phase 0's experiment lifecycle table now has five domain-specific
  column headers: FID, Experiment Name, Investigation Method, Expected Result (fill now),
  Actual Outcome (fill at Phase 5). The column header instructions "(fill now)" and
  "(fill at Phase 5)" are embedded in the column name, making the temporal protocol
  visible at the schema level rather than in prose.
- **C-13 (hypothesis-prior)**: PASS. The Phase 0 table structure is unchanged in its
  prior-commitment role. The lifecycle columns are additive -- they extend the record
  forward in time without displacing the prior commitment. F0-01 (hypothesis record)
  still precedes Phase 1. The "Expected Result" column captures a pre-evidence prediction,
  strengthening the C-13 prior-commitment evidence: the analyst writes down what they
  expect to find before any evidence phase runs.
- **C-27 (v8 candidate -- experiment lifecycle continuity)**: PASS candidate. A v8
  rubric could add a criterion requiring experiment records to capture both design (at
  Phase 0) and outcome (at Phase 5) in a continuous record, making the experimental
  chain visible without cross-referencing two separate tables. V-05 R8 satisfies this
  via the lifecycle columns: F0-02 and F0-03 hold both the investigation method and
  the actual outcome in the same row.

**C-23 interaction with lifecycle column names**: The column header "(fill now)" and
"(fill at Phase 5)" are phase-timing instructions embedded in column names. A strict
C-23 scorer who reads "column headers must enumerate required fields" might note that
timing instructions in column names are procedural, not schema-definitional. However,
the field names ("Expected Result" and "Actual Outcome") are domain-specific and schema-
meaningful on their own; the timing parentheticals are additive. C-23 PASS is not
threatened -- the schema is carried by the field names.

**FID stability**: F0-02 and F0-03 retain their FID keys. The FINDING REGISTER now
calls them "Experiment 1/2 lifecycle record" rather than "Experiment 1/2 design" --
a description change only. C-15 and C-16 are unaffected.

**Dual-table hypothesis concern**: Phase 0 experiment table (lifecycle) and Phase 5
hypothesis resolution table (F5-01) both relate to the hypothesis. A scorer might ask
whether two tables tracking the same experimental object creates FID ambiguity. Answer:
no -- the lifecycle table tracks the experiment design and outcome (F0-02, F0-03); the
resolution table tracks the hypothesis claim's ultimate disposition (F5-01 citing F0-01).
These are distinct record types with distinct FIDs. C-08 (hypothesis disposition) scores
Phase 5's F5-01 table; the lifecycle columns in Phase 0 are additional evidence, not
competitors for F5-01's disposition role.

**Predicted v7 score**: 16/16 aspirational --> composite **100.0** strict.
Under a hypothetical v8 rubric adding C-25, C-27: PASS both (18/18 aspirational).

---

## R8 Predicted Score Summary

| Variant | C-23 | C-24 | C-17 (v7) | Because format | v7 Composite | v8 candidate |
|---------|------|------|-----------|----------------|--------------|--------------|
| V-01 R8 (Because table, V-04 R7 base) | PASS strict | PASS | PASS | Table (C-25 candidate) | **100.0** | C-25 PASS |
| V-02 R8 (Phase 1b response strategy) | PASS strict | PASS | PASS | Bullet list | **100.0** | C-26 PASS |
| V-03 R8 (minimal prompt, no prose) | PASS strict | PASS | PASS | Bullet list | **100.0** | -- |
| V-04 R8 (Because table + Phase 1b strategy) | PASS strict | PASS | PASS | Table (C-25 candidate) | **100.0** | C-25 + C-26 PASS |
| V-05 R8 (lifecycle Phase 0 + Because table) | PASS strict | PASS | PASS | Table (C-25 candidate) | **100.0** | C-25 + C-27 PASS |

All five R8 variants predict 100.0 under v7. V-03 R8 confirms that no criterion depends
on instructional prose. V-01 R8 and V-04 R8 surface C-25 as the most likely v8 candidate
(synthesis-layer schema enforcement, paralleling C-23 for evidence phases). V-02 R8 and
V-04 R8 surface C-26 (competitive response disposition per rival). V-05 R8 surfaces C-27
(experiment lifecycle continuity). The three v8 candidates are structurally independent
and could be added to the rubric in any combination.

**V8 rubric candidate definitions:**

| ID | Criterion | Category | Prerequisite |
|----|-----------|----------|--------------|
| C-25 | **Synthesis-layer schema enforcement** | format | C-23 -- Because block uses named-column table; schema visible without reading slot content | C-23 |
| C-26 | **Competitive response disposition per rival** | behavior | Phase 1b table carries a response strategy or differentiator-response column per named rival; competitor analysis is actionable, not only diagnostic | C-04, C-21 |
| C-27 | **Experiment lifecycle continuity** | behavior | Experiment records capture both design (at Phase 0) and outcome (at Phase 5) in a single continuous record; prior-commitment and experimental outcome are co-located and traceable | C-13, C-16 |

**Production recommendation:** V-04 R8 is the recommended base for teams wanting to pass
any plausible v8 rubric extension. It combines strict C-23 throughout, C-24 synthesis
alignment, Because table (C-25), and Response Strategy column (C-26). V-03 R8 is the
production base for automated/API contexts where token economy matters.
