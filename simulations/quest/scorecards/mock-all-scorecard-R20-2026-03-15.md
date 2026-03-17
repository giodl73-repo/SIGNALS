## mock-all — Round 20 Scorecard (Rubric v20)

**Rubric:** v20 | **Denominator:** 32 (C-09 through C-40) | **Formula:** `(E/5×60) + (R/3×30) + (A/32×10)`

---

### Criterion-by-Criterion Evaluation

#### Essential Criteria (all variations — same result for all five)

| Criterion | Evidence | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|----------|------|------|------|------|------|
| **E-01** TOPICS.md lookup + tier state before any role | Lines before ROLE 1: "Read TOPICS.md... State: `Tier: {N}`" | PASS | PASS | PASS | PASS | PASS |
| **E-02** Classification table, correct column headers | 8-column header present: Namespace, Category, MUST use, DO NOT use, Tier 2/3 Critical, Compliance-Tagged, REAL-REQUIRED, Inertia gap skeleton | PASS | PASS | PASS | PASS | PASS |
| **E-03** Nine namespace rows | scout, draft, review, flow, trace, prove, listen, program, topic | PASS | PASS | PASS | PASS | PASS |
| **E-04** Sequential gated phases that cannot be skipped | ROLE 1 STOP → ROLE 2 STOP → ROLE 3 STOP → ROLE 4 gates present; ontological identity framing reinforces no-skip | PASS | PASS | PASS | PASS | PASS |
| **E-05** REAL-REQUIRED block with at least one entry | REAL-REQUIRED Rationale section present with prove, listen, compliance-tagged entries | PASS | PASS | PASS | PASS | PASS |

**Essential: 5/5 all variations → 60.0 pts each**

---

#### Recommended Criteria (all variations — same result for all five)

| Criterion | Evidence | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|----------|------|------|------|------|------|
| **R-01** Per-namespace MUST/DO NOT vocabulary | Each of 9 namespace rows has distinct MUST use and DO NOT use vocabulary | PASS | PASS | PASS | PASS | PASS |
| **R-02** Explicit body vocabulary compliance instruction | Each stage body instruction names vocabulary register (specification language / study-data framing / discovery-signal language) and DO NOT terms | PASS | PASS | PASS | PASS | PASS |
| **R-03** Stage STOP gates reference classification-derived conditions | STAGE 1 STOP: "compliance-tagged namespace has a REAL-REQUIRED block"; STAGE 2 STOP: "each has a REAL-REQUIRED block"; ROLE 2 STOP: "every REAL-REQUIRED = YES namespace" — all derived from classification table | PASS | PASS | PASS | PASS | PASS |

**Recommended: 3/3 all variations → 30.0 pts each**

---

#### Aspirational Criteria — C-09 through C-38 (30 criteria, same for all variations)

The variate design confirms all C-09 through C-38 pass across all five variations. Key spot-checks:

| Criterion | Evidence |
|-----------|----------|
| **C-17** Inertia extension instruction present | Each stage header carries the inertia extension format `-- specifically, {instance}` |
| **C-18** Named phases with ontological violation mechanism | "You ARE the CLASSIFIER... Producing artifact output while in the CLASSIFIER role means you have ceased to be the CLASSIFIER... That is a category error" |
| **C-19** Depth-anchored seed phrases | 9 seed phrases in authoritative list before ROLE 1 table |
| **C-20** Body-grounding instruction | Per-stage body vocabulary instructions present |
| **C-21** Inertia gap skeleton column pre-seeded | Classification table column 8 pre-seeded with verbatim seed phrases |

**C-09 through C-38: 30/30 all variations**

---

#### New Aspirational Criteria: C-39 and C-40

**C-39 — Declarations architecturally separate (one dimension each)**

**Diagnostic:** Read Declaration A alone — does it contain per-stage firing language? Read Declaration B alone — does it contain REAL-REQUIRED identifier language? Either contamination = FAIL.

| Variation | Declaration A text | Declaration B text | C-39 |
|-----------|-------------------|-------------------|------|
| **V-01** | "This declaration also governs the per-stage inertia extension requirement... Both the REAL-REQUIRED block presence and the per-stage inertia extension are Declaration A requirements" — contains both dimensions | "The inertia extension... The REAL-REQUIRED rationale block must also appear... Declaration B governs both per-artifact inertia extension and rationale section copying" — contains both dimensions | **FAIL** |
| **V-02** | "REAL-REQUIRED is the canonical identifier... The GENERATOR copies from the REAL-REQUIRED Rationale section by canonical name" — REAL-REQUIRED only, no per-stage firing language | "The inertia extension fires independently within Stage 1, Stage 2, and Stage 3... Completing a stage without per-artifact inertia extension is a Declaration B violation" — inertia only, no REAL-REQUIRED language | **PASS** |
| **V-03** | Same cross-contaminating text as V-01: "This declaration also governs the per-stage inertia extension... Both the REAL-REQUIRED block presence and the per-stage inertia extension are Declaration A requirements" | Same cross-contaminating text as V-01: "Declaration B governs both per-artifact inertia extension and rationale section copying" | **FAIL** |
| **V-04** | Same clean text as V-02: "REAL-REQUIRED is the canonical identifier... by canonical name, not by location heuristic" — no inertia language | Same clean text as V-02: "fires independently within Stage 1, Stage 2, and Stage 3" — no REAL-REQUIRED language | **PASS** |
| **V-05** | Same clean text as V-02/V-04 | Same clean text as V-02/V-04 | **PASS** |

**C-40 — Stage body inertia instance phrase is stage-specific (not cross-stage boilerplate)**

**Diagnostic:** Stage 1 instance placeholder must name HIGH-STRUCTURE domain (state transition / boundary contract / trigger condition / configuration key). Stage 2: EVIDENCE-HEAVY (study finding / empirical result / adoption measurement / hypothesis outcome). Stage 3: MIXED (market signal / design judgment / delivery milestone / coverage gap). Generic placeholder valid across all stages = FAIL.

| Variation | Stage 1 instance | Stage 2 instance | Stage 3 instance | C-40 |
|-----------|-----------------|-----------------|-----------------|------|
| **V-01** | `{one phrase naming the topic-specific instance of that gap}` — generic, no domain constraint | Same generic placeholder | Same generic placeholder | **FAIL** |
| **V-02** | `{one phrase naming the topic-specific instance of that gap}` — identical generic placeholder | Same generic placeholder | Same generic placeholder | **FAIL** |
| **V-03** | `{one phrase naming a state transition, boundary contract, trigger condition, or configuration key that defines this namespace's HIGH-STRUCTURE contribution to {topic}}` — stage-specific domain vocabulary | `{one phrase naming a study finding, empirical result, adoption measurement, or hypothesis outcome...}` — EVIDENCE-HEAVY specific | `{one phrase naming a market signal, design judgment, delivery milestone, or coverage gap...}` — MIXED specific | **PASS** |
| **V-04** | Instruction constraint: "must name a HIGH-STRUCTURE artifact domain... state transition, boundary contract, trigger condition, or configuration key" + placeholder `{HIGH-STRUCTURE instance for {topic}}` | "must name an EVIDENCE-HEAVY artifact domain... study finding, empirical result, adoption measurement, or hypothesis outcome" + `{EVIDENCE-HEAVY instance for {topic}}` | "must name a MIXED artifact domain... market signal, design judgment, delivery milestone, or coverage gap" + `{MIXED instance for {topic}}` | **PASS** |
| **V-05** | Pre-seeded example: "the trigger condition that determines when {topic}'s state machine transitions from PENDING to ACTIVE under nominal load" + e.g. pattern in placeholder | Pre-seeded example: "the prototype result showing whether {topic}'s core hypothesis held under the N=20 test run against realistic input data" + e.g. pattern | Pre-seeded example: "the open question about whether {topic}'s positioning holds against the closest competitor's announced roadmap" + e.g. pattern | **PASS (strongest)** |

---

### Composite Score Computation

| Variation | Essential (5/5) | Recommended (3/3) | C-39 | C-40 | Aspirational | Composite |
|-----------|----------------|------------------|------|------|-------------|-----------|
| **V-01** | 5/5 → 60 | 3/3 → 30 | FAIL | FAIL | 30/32 → 9.375 | **99.375** |
| **V-02** | 5/5 → 60 | 3/3 → 30 | PASS | FAIL | 31/32 → 9.688 | **99.688** |
| **V-03** | 5/5 → 60 | 3/3 → 30 | FAIL | PASS | 31/32 → 9.688 | **99.688** |
| **V-04** | 5/5 → 60 | 3/3 → 30 | PASS | PASS | 32/32 → 10.0 | **100.0** |
| **V-05** | 5/5 → 60 | 3/3 → 30 | PASS | PASS | 32/32 → 10.0 | **100.0** |

---

### Ranking

| Rank | Variation | Score | Differentiator |
|------|-----------|-------|---------------|
| **1** | V-04, V-05 | **100.0** | C-39 PASS + C-40 PASS |
| **3** | V-02, V-03 | **99.688** | Single-axis fix only |
| **5** | V-01 | **99.375** | Regression baseline — both new criteria fail |

**V-04 vs V-05 at equal score:** V-05 carries stronger structural guarantee for C-40. V-04 depends on model compliance with the artifact-domain instruction; V-05 pre-seeds an example phrase per stage that the model copies rather than generates. Same rubric score, V-05 eliminates the model-inference risk. This mirrors the V-02/V-03 structural-guarantee distinction identified in the scout-feasibility R3 series.

---

### Excellence Signals (from V-05, top-scoring strongest variation)

**Signal 1 — Declaration isolation as architectural property:** Separate each compliance dimension into its own named declaration with a scope boundary verifiable by inspection: read Declaration A alone, it must be complete for REAL-REQUIRED identifier authority; read Declaration B alone, it must be complete for per-stage inertia firing authority. Cross-contamination is invisible at the structural label level but detectable by body-text scan — making the isolation verifiable is what makes it durable.

**Signal 2 — Pre-seeded stage-specific examples as structural guarantee:** Rather than instructing the model to generate a domain-appropriate phrase (instruction-based), print an example phrase in the correct domain vocabulary directly in the stage template body. The model copies or adapts a phrase already on the page rather than inferring what "HIGH-STRUCTURE" or "EVIDENCE-HEAVY" means at generation time. This is the same structural class as verbatim seed-phrase transcription in the ROLE 1 skeleton column — the compliance guarantee moves from behavioral (model follows instruction) to transcriptive (model copies content).

**Signal 3 — Cross-stage invalidity as explicit gate condition:** V-05's STOP gates add the clause "the instance phrase valid only for its stage category, not cross-stage" as an explicit verification condition. This turns C-40 from an aspirational property into an enforced gate check, making the criterion self-auditing at each stage boundary.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Pre-seeded stage-specific example phrases in instance placeholders eliminate model-inference risk for domain-appropriate generation — model transcribes rather than generates, same structural class as verbatim skeleton seed phrases", "Architecturally separate declarations verifiable by body-text scan: Declaration A complete for REAL-REQUIRED identifier authority with no inertia language; Declaration B complete for per-stage firing authority with no REAL-REQUIRED language — isolation durable because it is inspectable", "Cross-stage invalidity made explicit in STOP gate condition: instance phrase must not be valid for any other stage category — converts aspirational C-40 property into enforced per-stage gate check"]}
```
