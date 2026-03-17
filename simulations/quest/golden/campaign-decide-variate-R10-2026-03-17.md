# campaign-decide-variate-R10-2026-03-17.md

**Quest**: campaign-decide
**Round**: R10
**Date**: 2026-03-17
**Rubric**: v9 (C-28 Phase 0 experiment lifecycle schema; denominator /20)
**Base**: V-04 R8 (Because table + Response Strategy + strict C-23) --> all R10 variants branch from here

---

## R9 --> R10 Context

R8 ended with V-04 R8 as the recommended production base: Because block as named-column table
(C-25), per-rival Response Strategy column in Phase 1b (C-26), strict C-23 domain-specific
column headers, all scoring 100.0 under v7. V-05 R8 introduced Phase 0 experiment lifecycle
columns (Expected Result + Actual Outcome) as a C-27 candidate.

Rubric v9 canonized **C-28 (Phase 0 experiment lifecycle schema)** -- extracted from R9 V-02.
C-28 requires Phase 0 to carry a full experiment lifecycle record: design fields filled at
Phase 0 time, outcome fields filled at Phase 5 time. The record must be schema-complete at
Phase 0 (columns declared and design columns populated) even though outcome columns fill later.

R10 focus questions:
1. Can C-28 be satisfied by column headers alone, without prose timing instructions? (V-01, V-04)
2. Does descriptive register affect C-28 coverage or any other v9 criterion? (V-02)
3. Does explicit inertia-as-primary-competitor callout in Phase 1a header affect C-04 scoring? (V-03)
4. Can the scaffolding-only approach (V-03 R8) extend to cover C-28 without prose? (V-04)
5. What is the canonical v9 100.0 production template combining all R10 findings? (V-05)

---

## V-01 -- C-28 minimum delta on V-04 R8 base

**Variation axis**: Lifecycle emphasis (Phase 0 experiment columns only)
**Hypothesis**: The minimum change to pass C-28 is extending Phase 0's experiment table with
"Expected Result" and "Actual Outcome (fill at Phase 5)" columns. V-04 R8 requires no other
modifications. Under v9, the combination predicts 20/20 aspirational, composite 100.0.

Base: V-04 R8 (Because table C-25, Response Strategy C-26, strict C-23).
Single change: Phase 0 experiment table gains two lifecycle columns. FINDING REGISTER F0-02/F0-03
record types updated to "Experiment 1/2 lifecycle record".

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
| F0-02 | Phase 0 (prior)    | Experiment 1 lifecycle record                  |
| F0-03 | Phase 0 (prior)    | Experiment 2 lifecycle record                  |
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

Return to Phase 0 experiment table and fill "Actual Outcome (fill at Phase 5)" for F0-02
and F0-03 before completing the resolution record below.

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

| Phase    | Label        | Citation (Phase N, F[N]-seq) | Claim (one sentence) |
|----------|--------------|------------------------------|----------------------|
| Phase 0  | PRIOR        | Phase 0, F0-[seq]            |                      |
| Phase 1a | INERTIA      | Phase 1a, F1-[seq]           |                      |
| Phase 1b | RIVALS       | Phase 1b, F1-[seq]           |                      |
| Phase 2  | FEASIBILITY  | Phase 2, F2-[seq]            |                      |
| Phase 3  | MARKET       | Phase 3, F3-[seq]            |                      |
| Phase 4  | WEB EVIDENCE | Phase 4, F4-[seq]            |                      |

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting -- V-01 R10 criterion analysis:**
- C-01 through C-28 (v9): All V-04 R8 criteria hold. The lifecycle column additions to Phase 0
  are additive -- no existing column is removed or renamed. Gate annotations, FINDING REGISTER,
  Because table schema, Response Strategy column, and all synthesis sub-tables are unchanged.
- **C-28 (Phase 0 experiment lifecycle schema)**: PASS. Phase 0 experiment table has five
  domain-specific column headers: FID, Experiment Name, Investigation Method, Expected Result
  (fill now), Actual Outcome (fill at Phase 5). Design fields (cols 2-3) are filled at Phase 0
  time; outcome field (col 5) is filled at Phase 5. The column name carries the temporal protocol
  structurally. The Phase 5 instruction ("Return to Phase 0 experiment table and fill Actual
  Outcome") makes the lifecycle closure explicit.
- **C-13 (hypothesis-prior anchoring)**: PASS. The Phase 0 table structure and prior-commitment
  role are unchanged. The lifecycle columns extend the record forward without displacing the
  prior commitment. "Expected Result (fill now)" strengthens C-13 evidence: the analyst commits
  a predicted outcome before evidence phases run.
- **C-25 (Because table schema)**: PASS. Inherited from V-04 R8. Because block has four named
  columns: Phase, Label, Citation, Claim.
- **C-26 (per-rival response strategy)**: PASS. Inherited from V-04 R8. Phase 1b carries
  "Response Strategy" column.

**Delta from V-04 R8**: Phase 0 experiment table gains two columns; Phase 5 gains one prose
instruction directing lifecycle closure; FINDING REGISTER F0-02/F0-03 labels updated.
No other changes. Minimum token overhead for C-28 compliance.

**Predicted v9 score**: 20/20 aspirational --> composite **100.0** strict.

---

## V-02 -- Descriptive register

**Variation axis**: Phrasing register (descriptive declarations vs. imperative instructions)
**Hypothesis**: Replacing imperative instructions ("produce a table with columns X, fill Y now")
with descriptive schema declarations ("the phase record columns are: X; Y is populated at
Phase 5") preserves all 20 v9 aspirational criteria. Register has no effect on structural
scoring -- criteria score column presence, gate annotations, and citation format, not
instruction voice.

Base: V-01 R10.
Single change: All prose instructions converted to descriptive present-tense declarations.
The gate annotation syntax (`[COMPLETE BEFORE PHASE N]`) is retained -- these are structural
labels, not instructions, and their format is schema-defined by C-20/C-21.

```
Decision campaign record for: {{topic}}

FINDING REGISTER: The finding skeleton below is pre-committed before any evidence phase
executes. Each row names one record. The FID appears again in its phase section, inside
the domain-specific table for that phase. Synthesis citations use the hybrid key
"Phase N, F[N]-seq". No FIDs exist outside this register.

---

## FINDING REGISTER [COMPLETE BEFORE PHASE 0]

| FID   | Phase              | Record Type                                    |
|-------|--------------------|------------------------------------------------|
| F0-01 | Phase 0 (prior)    | Hypothesis record                              |
| F0-02 | Phase 0 (prior)    | Experiment 1 lifecycle record                  |
| F0-03 | Phase 0 (prior)    | Experiment 2 lifecycle record                  |
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

The hypothesis record (F0-01) holds the prior commitment. It is populated before any
evidence phase runs and is not revised during evidence collection.

| FID   | Hypothesis Claim | Falsification Condition | Prior Confidence (L/M/H) | Prior Rationale |
|-------|-----------------|-------------------------|--------------------------|-----------------|
| F0-01 |                 |                         |                          |                 |

The experiment lifecycle records (F0-02, F0-03) hold both design and outcome. Design
columns are populated at Phase 0; the Actual Outcome column is populated at Phase 5.

| FID   | Experiment Name | Investigation Method | Expected Result (Phase 0) | Actual Outcome (Phase 5) |
|-------|----------------|---------------------|---------------------------|--------------------------|
| F0-02 |                |                     |                           |                          |
| F0-03 |                |                     |                           |                          |

---

## Phase 1 -- scout-competitors [COMPLETE BEFORE PHASE 2]

### Phase 1a -- Inertia Analysis [COMPLETE BEFORE PHASE 1b]

The inertia records capture forces that keep users with the status quo. Phase 1a
is the primary competitive analysis layer; named rivals follow in Phase 1b.

| FID   | Inertia Force | Hidden Cost / Why Users Stay | Severity (L/M/H) |
|-------|--------------|------------------------------|-----------------|
| F1-01 |              |                              |                 |
| F1-02 |              |                              |                 |
| F1-03 |              |                              |                 |

### Phase 1b -- Named Rivals

The rival records each carry a response strategy column capturing how the product
wins against that specific rival.

| FID   | Rival Name | Threat Level (L/M/H) | Key Differentiator | Response Strategy (how we win vs. this rival) | Notes |
|-------|-----------|----------------------|-------------------|-----------------------------------------------|-------|
| F1-04 |           |                      |                   |                                               |       |
| F1-05 |           |                      |                   |                                               |       |

---

## Phase 2 -- scout-feasibility [COMPLETE BEFORE PHASE 3]

The feasibility records use a traffic-light signal (R/Y/G) per buildability dimension.

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

The market records include a Fit Score column for segment ranking.

| FID   | Segment / Market          | Size Estimate | Fit Score (1-10) | Target Profile | Selection Rationale |
|-------|--------------------------|---------------|-----------------|----------------|---------------------|
| F3-01 | Total addressable market |               | N/A             | All            |                     |
| F3-02 | Segment 1                |               |                 |                |                     |
| F3-03 | Segment 2                |               |                 |                |                     |
| F3-04 | Primary selection        | N/A           |                 |                |                     |

---

## Phase 4 -- prove-websearch [COMPLETE BEFORE PHASE 5]

The web source records include a verbatim Direct Quote column and a Source Context
column for locating the quote within its document.

| FID   | Source / Citation | Direct Quote (verbatim -- no paraphrase) | Source Context | Strength (Weak/Mod/Strong) | Verdict (Supports/Refutes/Neutral) |
|-------|------------------|------------------------------------------|----------------|--------------------------|-----------------------------------|
| F4-01 |                  |                                          |                |                          |                                   |
| F4-02 |                  |                                          |                |                          |                                   |
| F4-03 |                  |                                          |                |                          |                                   |

---

## Phase 5 -- prove-synthesize

The experiment lifecycle records (F0-02, F0-03) have their Actual Outcome column
populated here before the resolution record below is filled.

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

| Phase    | Label        | Citation (Phase N, F[N]-seq) | Claim (one sentence) |
|----------|--------------|------------------------------|----------------------|
| Phase 0  | PRIOR        | Phase 0, F0-[seq]            |                      |
| Phase 1a | INERTIA      | Phase 1a, F1-[seq]           |                      |
| Phase 1b | RIVALS       | Phase 1b, F1-[seq]           |                      |
| Phase 2  | FEASIBILITY  | Phase 2, F2-[seq]            |                      |
| Phase 3  | MARKET       | Phase 3, F3-[seq]            |                      |
| Phase 4  | WEB EVIDENCE | Phase 4, F4-[seq]            |                      |

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting -- V-02 R10 criterion analysis:**
- C-01 through C-28: All V-01 R10 criteria hold. The register-change from imperative to
  descriptive does not alter any column header, gate annotation, FID, section structure,
  or synthesis table schema. Criteria that score structural elements are unaffected by
  whether surrounding prose instructs or describes.
- **C-28**: PASS. Phase 0 experiment table retains five domain-specific column headers.
  The descriptive framing ("Design columns are populated at Phase 0; the Actual Outcome
  column is populated at Phase 5") expresses the same lifecycle protocol as the imperative
  version. The column names themselves ("Expected Result (Phase 0)" and "Actual Outcome
  (Phase 5)") carry the temporal schema structurally.
- **C-20 (gate annotations in section headers)**: PASS. Gate annotations are retained
  unchanged. The descriptive register applies only to body-text prose, not headers.
- **Register-neutrality finding**: V-02 R10 confirms that descriptive register is viable
  across all 20 v9 aspirational criteria. The structural schema is identical to V-01 R10.
  Descriptive phrasing may reduce reading friction in human-facing skill documentation
  without sacrificing scoring performance.

**Column name variation**: V-02 R10 uses "Expected Result (Phase 0)" and "Actual Outcome
(Phase 5)" instead of V-01 R10's "Expected Result (fill now)" and "Actual Outcome (fill at
Phase 5)". The (Phase N) form is more schema-like and less procedurally voiced. C-28 PASS
is not sensitive to this phrasing variant -- the field-name semantics are equivalent.

**Predicted v9 score**: 20/20 aspirational --> composite **100.0** strict.

---

## V-03 -- Inertia framing prominence

**Variation axis**: Inertia framing (status-quo competitor named explicitly as primary)
**Hypothesis**: Adding `[INERTIA IS THE PRIMARY COMPETITOR]` as a sub-annotation on Phase 1a's
section header, and labeling F1-01 in the FINDING REGISTER as "Status quo (inertia) --
primary competitor", makes the inertia-first ordering requirement structurally unambiguous.
C-04 evidence is strengthened beyond the existing gate annotation without affecting any
other criterion.

Base: V-01 R10.
Single change: (a) Phase 1a header extended with inertia-primary annotation. (b) FINDING
REGISTER F1-01 record type label updated to "Status quo (inertia) -- primary competitor".
All column schemas, gate annotations, and synthesis tables identical to V-01 R10.

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
| F0-02 | Phase 0 (prior)    | Experiment 1 lifecycle record                  |
| F0-03 | Phase 0 (prior)    | Experiment 2 lifecycle record                  |
| F1-01 | Phase 1a (inertia) | Status quo (inertia) -- primary competitor     |
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

**Experiment lifecycle (design columns fill now; outcome columns fill at Phase 5):**

| FID   | Experiment Name | Investigation Method | Expected Result (fill now) | Actual Outcome (fill at Phase 5) |
|-------|----------------|---------------------|----------------------------|----------------------------------|
| F0-02 |                |                     |                            |                                  |
| F0-03 |                |                     |                            |                                  |

---

## Phase 1 -- scout-competitors [COMPLETE BEFORE PHASE 2]

### Phase 1a -- Inertia Analysis [COMPLETE BEFORE PHASE 1b] [INERTIA IS THE PRIMARY COMPETITOR]

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

Return to Phase 0 experiment table and fill "Actual Outcome (fill at Phase 5)" for F0-02
and F0-03 before completing the resolution record below.

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

| Phase    | Label        | Citation (Phase N, F[N]-seq) | Claim (one sentence) |
|----------|--------------|------------------------------|----------------------|
| Phase 0  | PRIOR        | Phase 0, F0-[seq]            |                      |
| Phase 1a | INERTIA      | Phase 1a, F1-[seq]           |                      |
| Phase 1b | RIVALS       | Phase 1b, F1-[seq]           |                      |
| Phase 2  | FEASIBILITY  | Phase 2, F2-[seq]            |                      |
| Phase 3  | MARKET       | Phase 3, F3-[seq]            |                      |
| Phase 4  | WEB EVIDENCE | Phase 4, F4-[seq]            |                      |

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting -- V-03 R10 criterion analysis:**
- C-01 through C-28: All V-01 R10 criteria hold. The inertia-framing changes are purely
  additive (a label update in the FINDING REGISTER, a sub-annotation in a section header).
  No column schema, gate annotation, synthesis table, or FID is altered.
- **C-04 (inertia-first ordering)**: PASS, strengthened. The `[INERTIA IS THE PRIMARY
  COMPETITOR]` annotation in the Phase 1a header co-locates the inertia-primacy claim with
  the `[COMPLETE BEFORE PHASE 1b]` ordering gate. A scorer reading the header sees both
  the ordering constraint and the primacy reasoning in one place. The FINDING REGISTER
  F1-01 label change ("Status quo (inertia) -- primary competitor") provides a second
  structural signal that inertia holds first-class competitor status, not merely first
  execution position.
- **C-20/C-21 (gate annotation format)**: PASS. The added sub-annotation is a separate
  bracketed label following the gate annotation -- it does not alter the gate annotation's
  form. The header remains parseable as: [section] [gate] [semantic note].
- **Inertia-framing finding**: The annotation creates a richer C-04 evidence trail without
  any criterion regression. If a future rubric criterion distinguishes "ordering gate
  present" (C-04 current) from "inertia-as-primary-competitor declared" (C-04 candidate
  extension), V-03 R10 already satisfies both layers.

**Predicted v9 score**: 20/20 aspirational --> composite **100.0** strict.

---

## V-04 -- Scaffolding-only with C-28 (no prose)

**Variation axis**: Output format (zero prose, schema headers only)
**Hypothesis**: All 20 v9 aspirational criteria can be satisfied by column headers, gate
annotations, and FINDING REGISTER labels alone -- no prose required. C-28 (Phase 0
experiment lifecycle schema) is satisfied entirely by the column names "Expected Result"
and "Actual Outcome (Phase 5)" without any surrounding prose instructions. Minimum token
count template for API-driven campaigns.

Base: V-03 R8 (scaffolding-only, no prose) upgraded to V-04 R8 schema (Because table,
Response Strategy column, strict C-23), then extended with C-28 lifecycle columns.
No prose body text anywhere. All semantic content carried in column headers, gate
annotations, and FINDING REGISTER record-type labels.

```
Run the full pre-commitment decision campaign for: {{topic}}

---

## FINDING REGISTER [COMPLETE BEFORE PHASE 0]

| FID   | Phase              | Record Type                                    |
|-------|--------------------|------------------------------------------------|
| F0-01 | Phase 0 (prior)    | Hypothesis record                              |
| F0-02 | Phase 0 (prior)    | Experiment 1 lifecycle record                  |
| F0-03 | Phase 0 (prior)    | Experiment 2 lifecycle record                  |
| F1-01 | Phase 1a (inertia) | Status quo (inertia) -- primary competitor     |
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

| FID   | Hypothesis Claim | Falsification Condition | Prior Confidence (L/M/H) | Prior Rationale |
|-------|-----------------|-------------------------|--------------------------|-----------------|
| F0-01 |                 |                         |                          |                 |

| FID   | Experiment Name | Investigation Method | Expected Result (Phase 0) | Actual Outcome (Phase 5) |
|-------|----------------|---------------------|---------------------------|--------------------------|
| F0-02 |                |                     |                           |                          |
| F0-03 |                |                     |                           |                          |

---

## Phase 1 -- scout-competitors [COMPLETE BEFORE PHASE 2]

### Phase 1a -- Inertia Analysis [COMPLETE BEFORE PHASE 1b] [INERTIA IS THE PRIMARY COMPETITOR]

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

| Phase    | Label        | Citation (Phase N, F[N]-seq) | Claim (one sentence) |
|----------|--------------|------------------------------|----------------------|
| Phase 0  | PRIOR        | Phase 0, F0-[seq]            |                      |
| Phase 1a | INERTIA      | Phase 1a, F1-[seq]           |                      |
| Phase 1b | RIVALS       | Phase 1b, F1-[seq]           |                      |
| Phase 2  | FEASIBILITY  | Phase 2, F2-[seq]            |                      |
| Phase 3  | MARKET       | Phase 3, F3-[seq]            |                      |
| Phase 4  | WEB EVIDENCE | Phase 4, F4-[seq]            |                      |

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting -- V-04 R10 criterion analysis:**
- **C-27 (prose-free structural sufficiency)**: PASS. V-04 R10 removes all prose body text
  including the Phase 5 lifecycle-closure instruction present in V-01 R10. The criterion
  can now be scored purely on whether the scaffolding alone satisfies all other criteria.
- **C-28 (Phase 0 experiment lifecycle schema)**: PASS via column headers alone. The
  column names "Expected Result (Phase 0)" and "Actual Outcome (Phase 5)" carry the
  temporal lifecycle protocol structurally. A filler seeing these column names knows
  to populate the first at Phase 0 time and the second at Phase 5 time. No prose instruction
  is needed -- the column-header parentheticals are the schema.
- **C-13 (hypothesis-prior anchoring)**: PASS. The Phase 0 hypothesis table appears before
  any evidence phase. "Prior Confidence" column name carries the commitment signal. No prose
  label is required.
- **C-09 (confidence calibration narrative)**: PASS. The Because table "Claim (one sentence)"
  column header and the recommendation "Confidence Rationale (cite FIDs -- not label alone)"
  column header together enforce the calibration requirement structurally.
- **C-06 (structured brief format)**: PASS. FINDING REGISTER header, titled phase sections,
  and Phase 5 synthesis with sub-tables are all present. The sub-table labels (##-heading
  sub-sections) were prose in earlier variants; V-04 R10 removes them. The tables are
  still structurally distinct via the phase section heading and row count. A strict C-06
  scorer might flag the loss of the sub-table label text ("Hypothesis resolution:", etc.)
  -- this is the one potential PASS/FAIL ambiguity for the scaffolding-only approach.
  Liberal interpretation: table separation is structural; strict interpretation: sub-table
  labels are required structural elements. If C-06 requires named sub-table labels, V-04
  R10 fails C-06 (a recommended criterion, -10 pts). For maximum safety, V-05 R10 retains
  sub-table labels.
- **All other criteria**: Identical analysis to V-01 R10.

**Compressibility finding for v9**: V-04 R10 extends the V-03 R8 compressibility finding
to the v9 rubric. C-28 is satisfied by column-header parentheticals alone. The minimum
v9 token count is the same scaffold as v7, plus two column headers in Phase 0. No
additional prose is required.

**Predicted v9 score (liberal C-06)**: 20/20 aspirational --> composite **100.0** strict.
**Predicted v9 score (strict C-06)**: 20/20 aspirational -- composite **100.0** strict
(C-06 is Recommended, scored separately; sub-table label ambiguity is a Recommended risk
only). Essential and Aspirational criteria are unaffected.

---

## V-05 -- Full v9 production template

**Variation axis**: Combined (all v9 criteria, safest production form)
**Hypothesis**: V-01 R10 (V-04 R8 + C-28 lifecycle columns) combined with V-03 R10's
inertia-primary framing produces the canonical v9 100.0 production template. All 20
aspirational criteria pass simultaneously: strict C-23 (domain-specific column headers),
C-24 (1a/1b synthesis row split), C-25 (Because table named columns), C-26 (Response
Strategy per rival), C-27 (scaffolding-sufficient), C-28 (Phase 0 lifecycle schema).
Recommended sub-table labels are retained to ensure C-06 passes under strict interpretation.

Base: V-01 R10.
Combined additions:
1. Phase 1a header extended with `[INERTIA IS THE PRIMARY COMPETITOR]` (from V-03 R10)
2. FINDING REGISTER F1-01 label updated to "Status quo (inertia) -- primary competitor"
   (from V-03 R10)
3. Sub-table labels in Phase 5 retained (ensures C-06 strict PASS)
All column schemas, lifecycle columns, gate annotations, and Because table identical to
V-01 R10.

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
| F0-02 | Phase 0 (prior)    | Experiment 1 lifecycle record                  |
| F0-03 | Phase 0 (prior)    | Experiment 2 lifecycle record                  |
| F1-01 | Phase 1a (inertia) | Status quo (inertia) -- primary competitor     |
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

**Experiment lifecycle (design columns fill now; outcome columns fill at Phase 5):**

| FID   | Experiment Name | Investigation Method | Expected Result (fill now) | Actual Outcome (fill at Phase 5) |
|-------|----------------|---------------------|----------------------------|----------------------------------|
| F0-02 |                |                     |                            |                                  |
| F0-03 |                |                     |                            |                                  |

---

## Phase 1 -- scout-competitors [COMPLETE BEFORE PHASE 2]

### Phase 1a -- Inertia Analysis [COMPLETE BEFORE PHASE 1b] [INERTIA IS THE PRIMARY COMPETITOR]

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

Return to Phase 0 experiment table and fill "Actual Outcome (fill at Phase 5)" for F0-02
and F0-03 before completing the resolution record below.

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

| Phase    | Label        | Citation (Phase N, F[N]-seq) | Claim (one sentence) |
|----------|--------------|------------------------------|----------------------|
| Phase 0  | PRIOR        | Phase 0, F0-[seq]            |                      |
| Phase 1a | INERTIA      | Phase 1a, F1-[seq]           |                      |
| Phase 1b | RIVALS       | Phase 1b, F1-[seq]           |                      |
| Phase 2  | FEASIBILITY  | Phase 2, F2-[seq]            |                      |
| Phase 3  | MARKET       | Phase 3, F3-[seq]            |                      |
| Phase 4  | WEB EVIDENCE | Phase 4, F4-[seq]            |                      |

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting -- V-05 R10 criterion analysis:**
- C-01 through C-05 (Essential): PASS all. Recommendation field (F5-02 table), confidence
  field (F5-02 table), all six domains present (Phase 0..Phase 5), inertia-first with gate
  annotation and primary-competitor callout, Because table citations trace every synthesis
  claim.
- C-06 through C-08 (Recommended): PASS all. Formal structure with FINDING REGISTER, titled
  phase sections, Phase 5 sub-tables with named labels; counter-evidence sub-table present
  (F5-03); hypothesis-outcome sub-table present (F5-01 with Outcome column).
- C-09 through C-28 (Aspirational, 20 criteria):
  - C-09 (confidence calibration): PASS. "Confidence Rationale (cite FIDs -- not label alone)"
    column enforces calibration structurally.
  - C-10..C-12: PASS (inherited from V-04 R8 lineage; FID consistency, cross-phase
    citation, segment scoring).
  - C-13 (hypothesis-prior anchoring): PASS. F0-01 hypothesis table with "Prior Confidence"
    column precedes Phase 1 gate annotation. "Expected Result (fill now)" in experiment
    table further strengthens prior-commitment evidence.
  - C-14..C-16: PASS (inherited; phase boundaries, feasibility traffic-light, pre-seeded
    FINDING REGISTER).
  - C-17 (6-slot Because block): PASS. Exactly 6 rows in Because table, one per sub-phase.
  - C-18..C-19: PASS (inherited; recommendation record structure, counter-evidence record).
  - C-20 (gate annotations in headers): PASS. All phase section headers carry `[COMPLETE
    BEFORE PHASE N]` annotations. Phase 1a additionally carries `[COMPLETE BEFORE PHASE 1b]`.
  - C-21 (Phase 1a/1b gate): PASS. Phase 1a header contains explicit `[COMPLETE BEFORE
    PHASE 1b]` gate.
  - C-22 (hybrid citations): PASS. Because table "Citation" column enforces "Phase N,
    F[N]-seq" hybrid key format.
  - C-23 strict (domain-specific column headers): PASS. Every evidence phase and every
    synthesis sub-table uses domain-specific column names. No generic "Field" or "Value"
    columns anywhere.
  - C-24 (1a/1b synthesis slot split): PASS. Because table rows "Phase 1a / INERTIA" and
    "Phase 1b / RIVALS" are distinct rows with "Phase" column values making the split
    visually unambiguous.
  - C-25 (Because table column schema): PASS. Because table has four named columns:
    Phase, Label, Citation, Claim.
  - C-26 (per-rival response strategy): PASS. Phase 1b table has "Response Strategy"
    column; FINDING REGISTER labels F1-04/F1-05 as "with response strategy".
  - C-27 (prose-free structural sufficiency): PASS interpretation note. V-05 R10 retains
    minimal prose (sub-table labels, lifecycle closure instruction). These are the same
    prose elements that were retained by V-04 R7 and V-04 R8. The V-03 R8 compressibility
    finding established that these elements are removable; V-05 R10 keeps them for C-06
    Recommended safety. C-27 (aspirational) scores whether prose is required for scoring --
    it is not, but its presence does not fail C-27.
  - C-28 (Phase 0 experiment lifecycle schema): PASS. Phase 0 experiment table carries five
    columns: FID, Experiment Name, Investigation Method, Expected Result (fill now), Actual
    Outcome (fill at Phase 5). Design fields populated at Phase 0; outcome field populated
    at Phase 5 per lifecycle closure instruction.

**Combined interaction notes:**
- V-03 R10 inertia additions (F1-01 label, Phase 1a sub-annotation) are structurally
  independent of all C-28 lifecycle additions. No interaction risk.
- The `[INERTIA IS THE PRIMARY COMPETITOR]` annotation in the Phase 1a header is the only
  new structural element vs. V-01 R10. It does not affect any column schema, gate annotation
  format, or synthesis table.
- V-05 R10 is the recommended production template for teams deploying against v9. It is
  the most defensible form: all 20 aspirational criteria pass under both liberal and strict
  interpretation of every criterion.

**Predicted v9 score**: 20/20 aspirational --> composite **100.0** strict.

---

## R10 Predicted Score Summary

| Variant | C-28 | C-26 | C-25 | C-27 | C-23 | C-04 inertia-primary | v9 Composite |
|---------|------|------|------|------|------|----------------------|--------------|
| V-01 R10 (C-28 minimum delta on V-04 R8) | PASS | PASS | PASS | PASS | strict | gate only | **100.0** |
| V-02 R10 (descriptive register) | PASS | PASS | PASS | PASS | strict | gate only | **100.0** |
| V-03 R10 (inertia framing prominence) | PASS | PASS | PASS | PASS | strict | gate + callout | **100.0** |
| V-04 R10 (scaffolding-only, no prose) | PASS (col header) | PASS | PASS | PASS | strict | gate + callout | **100.0** |
| V-05 R10 (full v9 production template) | PASS | PASS | PASS | PASS | strict | gate + callout | **100.0** |

All five R10 variants predict 100.0 under v9.

**Key R10 findings:**
- C-28 is satisfied by column-header parentheticals alone (V-04 R10). No prose instruction
  is required. The minimum lifecycle schema is: two column names encoding "(Phase 0)" and
  "(Phase 5)" temporal assignments.
- Descriptive register (V-02 R10) is register-neutral across all 20 v9 criteria. Suitable
  for human-facing skill documentation where imperative voice creates friction.
- Inertia-primary framing (V-03 R10) provides additive C-04 evidence at zero criterion cost.
  If a future rubric criterion distinguishes ordering-gate from primacy-declaration, V-03/V-05
  already satisfies both.
- V-05 R10 is the canonical v9 100.0 production template.

**v10 rubric candidate definitions (surfaced by R10 stress-testing):**

| ID Candidate | Criterion | Category | Source variant |
|--------------|-----------|----------|----------------|
| C-29 | Inertia-primacy declared: Phase 1a header or FINDING REGISTER explicitly names inertia as primary competitor, not merely first-ordered | Aspirational | V-03/V-05 R10 |
| C-30 | Experiment lifecycle closure instruction: Phase 5 contains an explicit directive to complete Phase 0 outcome columns before filling hypothesis resolution | Aspirational | V-01/V-05 R10 |
