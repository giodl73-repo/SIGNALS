---
skill: quest-variate
skill_target: campaign-decide
round: 6
date: 2026-03-16
rubric: simulations/quest/rubrics/campaign-decide-rubric-v6-2026-03-16.md
---

# Variations -- campaign-decide / Round 6

Five complete, runnable skill body variations targeting the v6 rubric.
Single-axis first (V-01, V-02, V-03), then combined (V-04, V-05).

**R5 -> R6 diagnosis:**

The v6 rubric added two new aspirational criteria (C-21 and C-22) and expanded the
denominator from /12 to /14. The rubric's tracking table logged three single-axis
R5 variants:

| R5 variation | v6 C-21 | v6 C-22 | v6 composite |
|--------------|---------|---------|--------------|
| V-01 R5 (hybrid citation, field-order inertia) | FAIL -- single-section, field order only | PASS -- "Phase N, F[N]-seq" dual-axis | 99.3 |
| V-02 R5 (Phase 1a/1b split, FID-only citation) | PASS -- Phase 1a gated before Phase 1b | FAIL -- FID-only, no phase prefix | 99.3 (liberal) / 98.6 (strict) |
| V-03 R5 (C-20 graft, no FID) | FAIL | FAIL | ~95.7 |

The tracking table did not score V-04 R5 or V-05 R5. V-04 R5 was the combined
variant (Phase 1a/1b split + hybrid citation) and already held both C-21 and C-22
structural elements. Under v6 scoring, V-04 R5 would score 22/22 = 100.0. V-05 R5
(conversational) dropped bracket annotations from Phase 0 and Phase 1a headers and
retained FID-only citation -- it fails C-20, C-21, and C-22, scoring ~97.1.

**R6 task:** Confirm the convergence path, characterize two boundary interactions not
yet tested (C-17/C-21 slot tension; C-20 gate density minimum), and extend the
conversational variant to full 22-criterion coverage.

**R6 axes:**

| Axis | Criterion targeted | Single/Combined |
|------|--------------------|-----------------|
| Canonical 22/22 convergence | C-21 + C-22 simultaneous | V-01 (single) |
| Table format | C-21+C-22 in all-table layout | V-02 (single) |
| Phase 1 Because slot split | C-17/C-21 interaction test | V-03 (single) |
| Convergence + gate density | C-20 at every phase boundary | V-04 (combined) |
| Convergence + conversational register | C-21+C-22 in narrative style | V-05 (combined) |

---

## V-01 -- Axis: Canonical 22/22 convergence

**Hypothesis**: V-04 R5 already combined Phase 1a/1b (C-21) with hybrid citation (C-22)
and should achieve 22/22 under v6. V-01 R6 makes this the canonical template by (a)
confirming the structure from first principles against all 22 criteria, (b) adding
`[COMPLETE BEFORE PHASE N+1]` gates to all phase headers (strengthening C-20 beyond
the minimum), and (c) labeling it as the R6 reference for all downstream variants.
This is not a new structural discovery -- it is the stabilization of R5's highest-
scoring template into a documented standard.

Base: V-04 R5 (Phase 1a/1b split + hybrid citation).
Single-axis refinement: add `[COMPLETE BEFORE PHASE N+1]` to Phase 2, 3, and 4
headers (V-04 R5 had no gate annotations on those headers). Structural content
is otherwise identical to V-04 R5.

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

F5-01  Hypothesis outcome: [Confirmed/Refuted/Inconclusive -- resolves F0-01]
F5-02  Recommendation: [COMMIT/PAUSE/PIVOT/ABANDON]
F5-03  Confidence: [High/Medium/Low]
F5-04  Confidence rationale: [cite the specific FIDs that drove this rating -- not just the label]
F5-05  Counter-evidence: [one risk or caveat -- cite the FID it qualifies]
F5-06  Next step: [COMMIT: concrete action | no-build: exit condition or revisit trigger]

Because (one citation per evidence phase -- exactly 5 slots):
- PRIOR (Phase 0): [claim] because Phase 0, F0-[seq]
- COMPETITORS (Phase 1): [claim] because Phase 1, F1-[seq]
- FEASIBILITY (Phase 2): [claim] because Phase 2, F2-[seq]
- MARKET (Phase 3): [claim] because Phase 3, F3-[seq]
- WEB EVIDENCE (Phase 4): [claim] because Phase 4, F4-[seq]

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting -- all 22 criteria:**
- C-01: F5-02 labeled COMMIT/PAUSE/PIVOT/ABANDON
- C-02: F5-03 labeled confidence field
- C-03: All six domains -- Phase 0 (prove-hypothesis), Phase 1a+1b (competitors), Phase 2 (feasibility), Phase 3 (market), Phase 4 (websearch), Phase 5 (synthesize)
- C-04: Phase 1a (Inertia) is a named, gated sub-section preceding Phase 1b (Rivals)
- C-05: Because block -- five labeled slots, each carrying a phase+FID citation
- C-06: Section headers per phase + labeled FID rows
- C-07: F5-05 counter-evidence field with explicit FID citation requirement
- C-08: F5-01 hypothesis outcome field -- resolves F0-01
- C-09: F5-04 confidence rationale cites FIDs -- not the label alone
- C-10: F5-06 conditioned next step (concrete action vs exit trigger)
- C-11: FID-labeled required rows per phase = per-phase required-field schema
- C-12: "because Phase N, F[N]-seq" -- Phase prefix matches rubric example format; FID key provides unique auditable reference. PASS strict and liberal.
- C-13: Phase 0 section appears before Phase 1 by document position; FINDING REGISTER precedes Phase 0
- C-14: Five labeled phase slots in Because block -- 5 distinct phases by label
- C-15: FINDING REGISTER pre-assigns all FIDs with unique keys
- C-16: Standalone FINDING REGISTER before Phase 0 with "--" skeleton rows -- PASS strict and liberal
- C-17: Exactly 5 labeled Because slots for 5 evidence phases (scout-competitors is ONE skill = ONE slot regardless of 1a/1b internal split)
- C-18: F5-05 cites the FID it qualifies
- C-19: F5-01 resolves F0-01 by FID reference
- C-20: Gate annotations present in FINDING REGISTER, Phase 0, Phase 1, Phase 1a, Phase 2, Phase 3, Phase 4 headers -- 7 gate points
- **C-21: Phase 1a (Inertia) is a gated ### sub-section before Phase 1b (Rivals) -- structurally unbreakable at section boundary, not field ordering or prose instruction. PASS.**
- **C-22: "because Phase N, F[N]-seq" carries both phase prefix (campaign position) and FID key (finding identity) -- dual-axis closes strict/liberal C-12 ambiguity. PASS.**

**C-17 / C-21 interaction note**: Phase 1a and Phase 1b are sub-sections of Phase 1 (scout-competitors). The synthesis Because block has ONE slot labeled "COMPETITORS (Phase 1)" covering all Phase 1 findings (F1-01..F1-05). The FID cited in that slot may be from either Phase 1a or 1b. C-17 counts evidence skill-phases (5), not structural sub-phases -- so the single Phase 1 slot is correct. C-21 passes on the structural split; C-17 passes on the slot count.

**Predicted v6 score**: 14/14 aspirational --> composite **100.0**. Confirms V-04 R5 path.

---

## V-02 -- Axis: Output format (all-table content with C-21+C-22)

**Hypothesis**: V-01 R6 uses inline FID row notation (`F2-01  Technical complexity: ...`).
Replacing phase content with full markdown tables strengthens C-11 (the table column
header defines the required-field schema explicitly) and may improve mechanical
fillability. The question is whether all-table content affects any other criterion when
the structural headers and gate annotations are held constant. Predicted: no criterion
is harmed by the format change; C-11 evidence is strengthened.

Base: V-01 R6 (all 22 criteria pass).
Single-axis change: all phase content converted to markdown tables. Section headers,
FINDING REGISTER, gate annotations, and Because block are identical to V-01.

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

Because (one citation per evidence phase -- exactly 5 slots):
- PRIOR (Phase 0): [claim] because Phase 0, F0-[seq]
- COMPETITORS (Phase 1): [claim] because Phase 1, F1-[seq]
- FEASIBILITY (Phase 2): [claim] because Phase 2, F2-[seq]
- MARKET (Phase 3): [claim] because Phase 3, F3-[seq]
- WEB EVIDENCE (Phase 4): [claim] because Phase 4, F4-[seq]

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting -- format axis notes:**
- C-11: Table column headers ARE the required-field schema. `| Dimension | Rating (R/Y/G) | Reason |` makes the schema explicit at the table level rather than inferrable from field labels. Stronger C-11 evidence than V-01.
- C-12/C-22: Because block identical to V-01 -- hybrid citation format unchanged.
- C-21: ### Phase 1a and ### Phase 1b headers with gate annotation unchanged from V-01. Format of content inside the sub-sections (table vs inline) does not affect C-21 -- the criterion scores the section boundary structure, not the content format.
- C-16: FINDING REGISTER table identical to V-01 -- skeleton "--" rows in place before Phase 0. PASS strict and liberal.
- C-18/C-19: Phase 5 table rows require FID citations in F5-05 and F5-01. Table cell constraint is equivalent to inline field instruction.

**Format interaction notes:**
- Phase 4 table compresses the multi-line source/quote/strength/verdict block into a single row per source. Quote fidelity may suffer from cell-width pressure. If a scorer requires "not paraphrase" evidence, a truncated table cell introduces risk.
- Phase 4 is the one phase where inline format (V-01) may be more reliable for quote capture than table format (V-02). A hybrid -- table for Phases 0-3 and inline for Phase 4 -- is a future candidate.

**Predicted v6 score**: 14/14 aspirational --> composite **100.0**. Same score as V-01.
The format change does not affect criterion outcomes; it changes the evidence quality for
C-11 (stronger) and Phase 4 quote fidelity (minor risk, non-criterion).

---

## V-03 -- Axis: Phase 1 Because slot split (C-17/C-21 tension test)

**Hypothesis**: When Phase 1 is structurally split into Phase 1a (Inertia) and Phase 1b
(Rivals), an analyst may argue that synthesis should cover each sub-phase separately --
producing 6 Because slots instead of 5. If the synthesis template provides 6 slots, C-17
fails: the rubric counts evidence skill-phases (5 skills in the campaign spec), not
structural sub-phases. C-14 is unaffected (citations from at least 3 distinct phases --
6 slots trivially satisfies this). C-22 can still pass if each slot uses hybrid citation
syntax ("because Phase 1a, F1-seq"). This variant tests whether splitting the synthesis
slot introduces a C-17 failure and what compensating effects, if any, arise.

Base: V-01 R6 (all 22 pass).
Single-axis change: Phase 1 Because slot split into two ("INERTIA (Phase 1a)" +
"RIVALS (Phase 1b)"), giving 6 total slots. All other structure identical to V-01.

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

F5-01  Hypothesis outcome: [Confirmed/Refuted/Inconclusive -- resolves F0-01]
F5-02  Recommendation: [COMMIT/PAUSE/PIVOT/ABANDON]
F5-03  Confidence: [High/Medium/Low]
F5-04  Confidence rationale: [cite the specific FIDs that drove this rating -- not just the label]
F5-05  Counter-evidence: [one risk or caveat -- cite the FID it qualifies]
F5-06  Next step: [COMMIT: concrete action | no-build: exit condition or revisit trigger]

Because (one citation per structural evidence phase -- 6 slots, covering inertia and
rivals as separate synthesis targets):
- PRIOR (Phase 0): [claim] because Phase 0, F0-[seq]
- INERTIA (Phase 1a): [claim] because Phase 1a, F1-[seq]
- RIVALS (Phase 1b): [claim] because Phase 1b, F1-[seq]
- FEASIBILITY (Phase 2): [claim] because Phase 2, F2-[seq]
- MARKET (Phase 3): [claim] because Phase 3, F3-[seq]
- WEB EVIDENCE (Phase 4): [claim] because Phase 4, F4-[seq]

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting -- C-17 / C-21 tension analysis:**
- C-17: FAIL. The rubric scores slot count against "evidence phase count in the campaign spec." Campaign spec has 5 evidence skills (competitors, feasibility, market, hypothesis, websearch). Phase 1a and 1b are sub-phases of ONE evidence skill. 6 slots != 5. Template fails C-17 regardless of analyst intent.
- C-21: PASS. Phase 1a/1b sub-section split with gate annotation in Phase 1a header is unchanged from V-01. C-21 does not care about synthesis slot count.
- C-22: PASS. "because Phase 1a, F1-[seq]" carries a phase prefix token ("Phase 1a") and a FID key (F1-[seq]). Both dimensions present. A strict scorer who disputes whether "Phase 1a" satisfies "Phase N" syntax would be unreasonable -- the format is structurally equivalent.
- C-14: PASS. 6 slots from 6 labeled phases easily clears the "at least 3 distinct phases" threshold.
- All other criteria: identical to V-01 -- PASS.

**Boundary finding**: C-17 and C-21 are structurally in tension when Phase 1 has a 1a/1b split. C-21 rewards structural isolation of inertia from rivals at the section level; C-17 penalizes any Because block whose slot count exceeds the number of evidence skills in the campaign spec. The correct resolution -- confirmed by V-01 -- is to maintain ONE Phase 1 synthesis slot while internally splitting the evidence section. V-03 exists to document that the 6-slot synthesis is the wrong path.

**Predicted v6 score**: 13/14 aspirational (C-17 fails) --> composite **99.3**.
Confirms that Phase 1a/1b structural split must NOT propagate into the synthesis slot count.

---

## V-04 -- Combined: Convergence + gate density (C-20 maximally reinforced)

**Hypothesis**: V-01 R6 has 7 gate annotations (FINDING REGISTER, Phase 0, Phase 1,
Phase 1a, Phase 2, Phase 3, Phase 4). This is the maximum for a 5-phase + 1a/1b
campaign. V-04 tests whether adding explicit phase purpose annotations to each section
header -- as inline labels, not as separate prose blocks -- improves mechanical
compliance without creating C-17 or C-14 risks. The axis is "lifecycle emphasis":
each phase header carries a one-phrase goal statement alongside the gate annotation,
making the phase's purpose visible without adding body prose.

Changes from V-01 R6:
1. Each phase header adds a brief purpose label: `-- prove-hypothesis: commit prior`
2. Phase 1 section header adds a purpose note: `-- scout-competitors: inertia then rivals`
3. FINDING REGISTER header adds a purpose note: `-- seed all FIDs before entering Phase 0`
4. Phase 5 synthesis header adds: `-- cross-phase Because, one slot per evidence phase`

These are cosmetic additions to headers -- the gate annotations, section structure,
FINDING REGISTER, and Because format are identical to V-01. No criterion is changed.
The test: does this improve fillability without introducing any C-17/C-14/C-22 risk?

```
Run the full pre-commitment decision campaign for: {{topic}}

FINDING REGISTER: The complete finding skeleton below is committed before any evidence
phase executes. Fill each registered row in its phase section. Cite by hybrid key
"Phase N, F[N]-seq" in the synthesis Because block. Do not create FIDs outside this
register.

---

## FINDING REGISTER -- seed all FIDs before entering Phase 0 [COMPLETE BEFORE PHASE 0]

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

## Phase 0 -- prove-hypothesis: commit prior belief [COMPLETE BEFORE PHASE 1]

F0-01  Claim: [one falsifiable sentence -- what must be true for this to be worth building]
F0-02  Falsification condition: [what single piece of evidence would disprove this claim]
F0-03  Confidence prior: [Low/Medium/High]
F0-04  Prior rationale: [reason for your prior before any external data is gathered]
F0-05  Experiment 1: [name and method]
F0-06  Experiment 2: [name and method]

---

## Phase 1 -- scout-competitors: inertia then rivals [COMPLETE BEFORE PHASE 2]

### Phase 1a -- Inertia Analysis: why people don't change [COMPLETE BEFORE PHASE 1b]

F1-01  Status-quo inertia: [why people pay the hidden cost of not changing]
F1-02  Switching cost: [what users lose by moving to any alternative]
F1-03  Good-enough threshold: [when the current approach feels acceptable]

### Phase 1b -- Named Rivals: named alternatives

F1-04  Rival A -- name: [name] | threat: [Low/Medium/High] | notes: [one sentence]
F1-05  Rival B -- name: [name] | threat: [Low/Medium/High] | notes: [one sentence]

---

## Phase 2 -- scout-feasibility: buildability rating [COMPLETE BEFORE PHASE 3]

F2-01  Technical complexity: [R/Y/G] -- [reason]
F2-02  Team capability: [R/Y/G] -- [reason]
F2-03  Timeline: [R/Y/G] -- [reason]
F2-04  Cost: [R/Y/G] -- [reason]
F2-05  Overall feasibility: [R/Y/G]
F2-06  Top risk: [single biggest buildability threat]

---

## Phase 3 -- scout-market: who wants this [COMPLETE BEFORE PHASE 4]

F3-01  Addressable market: [size estimate with stated basis]
F3-02  Segment 1 -- name: [name] | fit: [1-10] | reason: [one sentence]
F3-03  Segment 2 -- name: [name] | fit: [1-10] | reason: [one sentence]
F3-04  Primary segment: [name] | justification: [one sentence]

---

## Phase 4 -- prove-websearch: external evidence [COMPLETE BEFORE PHASE 5]

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

## Phase 5 -- prove-synthesize: cross-phase Because, one slot per evidence phase

F5-01  Hypothesis outcome: [Confirmed/Refuted/Inconclusive -- resolves F0-01]
F5-02  Recommendation: [COMMIT/PAUSE/PIVOT/ABANDON]
F5-03  Confidence: [High/Medium/Low]
F5-04  Confidence rationale: [cite the specific FIDs that drove this rating -- not just the label]
F5-05  Counter-evidence: [one risk or caveat -- cite the FID it qualifies]
F5-06  Next step: [COMMIT: concrete action | no-build: exit condition or revisit trigger]

Because (one citation per evidence phase -- exactly 5 slots):
- PRIOR (Phase 0): [claim] because Phase 0, F0-[seq]
- COMPETITORS (Phase 1): [claim] because Phase 1, F1-[seq]
- FEASIBILITY (Phase 2): [claim] because Phase 2, F2-[seq]
- MARKET (Phase 3): [claim] because Phase 3, F3-[seq]
- WEB EVIDENCE (Phase 4): [claim] because Phase 4, F4-[seq]

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting -- lifecycle emphasis axis notes:**
- C-20: Phase purpose labels are appended to gate annotations in the header text. A gate like `[COMPLETE BEFORE PHASE 1]` is the gate; `: commit prior belief` is the label. Both are part of the heading. C-20 requires the gate itself to be in the header -- the label does not dilute it. PASS, same as V-01. Gate density is now 7 explicit gate-annotated headers.
- C-21: Phase 1a header reads `### Phase 1a -- Inertia Analysis: why people don't change [COMPLETE BEFORE PHASE 1b]`. Gate annotation is present. PASS.
- C-22: Because block unchanged from V-01. PASS.
- C-17: 5 slots. PASS.
- All other criteria: identical to V-01.

**Lifecycle label interaction note**: Adding `: commit prior belief` to Phase 0's header creates a self-describing template -- a filler reading only headers can reconstruct the campaign's purpose per phase without opening the body. This is a usability improvement, not a scoring improvement. No criterion is affected.

**Predicted v6 score**: 14/14 aspirational --> composite **100.0**. Identical to V-01.
The lifecycle emphasis axis is scoring-neutral.

---

## V-05 -- Combined: Convergence + conversational phrasing register

**Hypothesis**: V-05 R5 (conversational) scored below 100.0 because it dropped bracket
gate annotations from Phase 0 and Phase 1a headers, replacing them with prose instructions.
That broke C-20 (annotations in headers) and C-21 (C-20 is a prerequisite). It also
retained FID-only citation, breaking C-22. V-05 R6 repairs all three gaps: bracket
annotations are preserved in all 7 gate positions (as in V-01), and the Because block
uses hybrid citation. The remaining change is phrasing register: instruction text is
rewritten from imperative-concise to explanatory-narrative. The test is whether
conversational prose wrapping structurally intact mechanisms produces a 22/22 template.

Changes from V-01 R6:
1. Preamble: narrative explanation of the campaign's purpose and registration requirement
2. Phase 0 body: explanatory note on WHY the prior must be committed first
3. Phase 1a body: narrative on WHY inertia precedes rival analysis
4. Phase 1b body: brief connector note
5. Phase 5 body: explanatory note on the Because block's function
6. All headers, gate annotations, FINDING REGISTER, FID fields, and Because format:
   IDENTICAL to V-01.

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

F0-01  Claim: [one falsifiable sentence -- what must be true for this to be worth building]
F0-02  Falsification condition: [what single piece of evidence would disprove this claim]
F0-03  Confidence prior: [Low/Medium/High]
F0-04  Prior rationale: [reason for your prior before any external data is gathered]
F0-05  Experiment 1: [name and method]
F0-06  Experiment 2: [name and method]

---

## Phase 1 -- scout-competitors [COMPLETE BEFORE PHASE 2]

### Phase 1a -- Inertia Analysis [COMPLETE BEFORE PHASE 1b]

The most important competitor in most markets is not a named product -- it is the
status quo. People have a cost of doing nothing and a threshold at which "good enough"
wins over "better." Understand why people stay put before naming any alternative. A
competitor analysis that opens with product names anchors on the wrong question.

F1-01  Status-quo inertia: [why people pay the hidden cost of not changing]
F1-02  Switching cost: [what users lose by moving to any alternative]
F1-03  Good-enough threshold: [when the current approach feels acceptable]

### Phase 1b -- Named Rivals

With inertia established, name the products or approaches that actively compete.

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

The Because block below is the audit trail. Each slot carries one citation from one
evidence phase using the format "because Phase N, F[N]-seq" -- the phase prefix proves
which phase the claim comes from; the FID key pins the specific finding in the register.
Five evidence phases = exactly five slots. A missing slot means that phase's evidence
didn't reach the recommendation.

F5-01  Hypothesis outcome: [Confirmed/Refuted/Inconclusive -- resolves F0-01]
F5-02  Recommendation: [COMMIT/PAUSE/PIVOT/ABANDON]
F5-03  Confidence: [High/Medium/Low]
F5-04  Confidence rationale: [cite the specific FIDs that drove this rating -- not just the label]
F5-05  Counter-evidence: [one risk or caveat -- cite the FID it qualifies]
F5-06  Next step: [COMMIT: concrete action | no-build: exit condition or revisit trigger]

Because (one citation per evidence phase -- exactly 5 slots):
- PRIOR (Phase 0): [claim] because Phase 0, F0-[seq]
- COMPETITORS (Phase 1): [claim] because Phase 1, F1-[seq]
- FEASIBILITY (Phase 2): [claim] because Phase 2, F2-[seq]
- MARKET (Phase 3): [claim] because Phase 3, F3-[seq]
- WEB EVIDENCE (Phase 4): [claim] because Phase 4, F4-[seq]

---

Output artifact: simulations/{{topic}}/decide-{{date}}.md
```

**Rubric targeting -- conversational register axis notes:**
- C-20: Gate annotations `[COMPLETE BEFORE PHASE N]` are preserved in all 7 header positions. The explanatory body prose that follows each section header is body text, not header text -- it does not interfere with the gate. PASS. (This is the fix relative to V-05 R5, which dropped bracket annotations from Phase 0 and Phase 1a.)
- C-21: `### Phase 1a -- Inertia Analysis [COMPLETE BEFORE PHASE 1b]` -- gate annotation in header. The explanatory paragraph that follows is body text. C-21 requires the gate "appear at the structural boundary it governs, as part of the heading label itself" -- the bracket annotation satisfies this; the prose explanation does not undermine it. PASS.
- C-22: Because block uses "because Phase N, F[N]-seq" -- hybrid citation format. PASS. (Fix relative to V-05 R5's FID-only citations.)
- C-13: Phase 0 explanatory note ("State what you believe before you look at anything") makes the prior-commitment intent explicit. Does not change criterion outcome -- Phase 0 header position before Phase 1 is what passes C-13. The prose is explanatory.
- All other criteria: identical to V-01.

**Phrasing register vs structural enforcement**: The explanatory prose in Phase 1a
("The most important competitor is not a named product...") does not replace the
gate annotation `[COMPLETE BEFORE PHASE 1b]`. It co-exists with it. A filler may
find the explanation helpful; the structural constraint is the gate. V-05 R5 made
the mistake of thinking prose could substitute for the bracket annotation. V-05 R6
uses both: prose explains the reason; the gate enforces the boundary.

**V-05 R5 repair summary:**
- V-05 R5 dropped `[COMPLETE BEFORE PHASE 1]` from Phase 0 header --> C-20 borderline, C-13 not affected
- V-05 R5 dropped `[COMPLETE BEFORE PHASE 1b]` from Phase 1a header --> C-20 fail, C-21 fail
- V-05 R5 used `because F[N]-[seq]` in Because block --> C-22 fail
- V-05 R6 restores all bracket annotations + hybrid citation --> C-20 PASS, C-21 PASS, C-22 PASS

**Predicted v6 score**: 14/14 aspirational --> composite **100.0**.
Confirms that conversational register is compatible with full 22-criterion coverage when
structural annotations are preserved intact.

---

## Cross-variant summary

| Variant | C-21 | C-22 | C-17 | C-20 | v6 Composite | Notes |
|---------|------|------|------|------|--------------|-------|
| V-01 R6 (canonical convergence) | PASS | PASS | PASS | PASS | **100.0** | Reference template |
| V-02 R6 (all-table content) | PASS | PASS | PASS | PASS | **100.0** | Format-neutral |
| V-03 R6 (6-slot Because split) | PASS | PASS | FAIL | PASS | **99.3** | C-17 trap -- do not split Phase 1 slots |
| V-04 R6 (lifecycle emphasis) | PASS | PASS | PASS | PASS | **100.0** | Purpose labels add usability, not score |
| V-05 R6 (conversational register) | PASS | PASS | PASS | PASS | **100.0** | V-05 R5 repaired |

**Key learnings from R6:**
1. V-04 R5 already achieved 22/22 -- the single-axis tracking table had a blind spot for combined variants. R6 V-01 makes this explicit.
2. Table format is structurally equivalent to inline FID rows for all 22 criteria. Format is a usability choice, not a scoring lever.
3. The 6-slot Phase 1 Because split is a C-17 trap: C-21 and the synthesis slot count operate on different definitions of "phase" (structural sub-phase vs evidence skill-phase). The canonical resolution is one slot per skill.
4. Lifecycle emphasis (purpose labels on headers) is scoring-neutral. It improves readability.
5. Conversational register achieves 22/22 when bracket gate annotations are preserved. The error in V-05 R5 was substituting prose for structural annotations. Prose can co-exist with annotations; it cannot replace them.
