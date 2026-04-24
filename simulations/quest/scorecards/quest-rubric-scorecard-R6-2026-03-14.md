Scorecard written to `simulations/quest/scorecards/quest-rubric-scorecard-R6-2026-03-14.md`.

---

## R6 Results

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["role-definition-as-equivalence-anchor", "sub-section-naming-forces-co-presence"]}
```

---

### Summary

**R6 solved C-15 across all five variations.** The structural fix — forcing self-application and rejected criterion into the same Phase 1 section by any mechanism — is robust. Three different approaches (imperative mandate, interrogative Q&A, sub-block labels) all produced co-location.

**Rankings:**

| Rank | Variation | Score |
|------|-----------|-------|
| 1 | V-05 (role sequence + sub-sections) | **100** |
| 2 | V-01 (DR-phase mandate) | 99.64 |
| 2 | V-04 (doubled contract + mandate) | 99.64 |
| 4 | V-02 (interrogative) | 99.29 |
| 5 | V-03 (combined sub-blocks) | 94.64 |

**V-05 is the only 100.** The differentiator: it embeds "or equivalent block" at the role-definition level, which propagates the phrase to C-21 and C-25 simultaneously. V-01 and V-04 achieve identical structural outputs without the phrase — scoring PARTIAL on both.

**V-03 loses 5 points on C-08** — combining failure analysis with pre-rejection and self-application in one phase dilutes failure-mode distinctness.

**Two new v8 candidates extracted:** `role-definition-as-equivalence-anchor` and `sub-section-naming-forces-co-presence`.
n criterion construction |
| C-08 | PASS | 5–7 distinct silent failures; each derived criterion tests a distinct failure mode |
| C-09 | PASS | Self-application in DR provides concrete poor-output example for calibration |
| C-10 | PASS | Evolution hook + version field in Phase 5 Scoring |
| C-11 | PASS | DR section (Phase 1) names dominant failure mode before criteria table |
| C-12 | PASS | 8 banned qualifiers listed; all pass conditions checked |
| C-13 | PASS | Named "Rejection Log" section (Phase 4); explicit construction-time disqualification |
| C-14 | PASS | Phase 1 DR → Phase 2 Failure Inventory → Phase 3 Rejection Log → Phase 4 Rubric Table |
| C-15 | PASS | Phase 1 has all 3 items: dominant failure (Item 1) + rejected criterion (Item 2) + self-application (Item 3); anti-drift note ("not in Scoring") present; STOP CONDITION enforces co-location |
| C-16 | N/A | No revision phase |
| C-17 | N/A | No revision phase |
| C-18 | PASS | 8 banned terms enumerated: good / sufficient / appropriate / clear / complete / thorough / comprehensive / adequate |
| C-19 | PASS | C-15 pass condition is output-state only; no construction mechanism named |
| C-20 | PASS | Required Output Sections block (item 5 = Scoring) appears before Phase 1 |
| C-21 | PARTIAL | No role definition; "or equivalent block" phrase absent from the level that propagates to produced C-11/C-14 pass conditions |
| C-22 | PASS | Phase 4 Rejection Log: "Construction-time filter alone does not satisfy this requirement" |
| C-23 | PASS | All 3 items co-located in Phase 1 DR; anti-drift note prevents Scoring-section drift |
| C-24 | PASS | Required Output Sections block front-loads all 5 sections before first phase instruction |
| C-25 | N/A | No role definition |

**Essential:** 5/5 × 60 = **60**
**Recommended:** 3/3 × 30 = **30**
**Aspirational:** 13.5/14 × 10 = **9.64**
**Composite: 99.64** | All essential pass: YES

---

## V-02 — Interrogative question route

**Axis:** Single-axis — three directed questions replace imperative mandates in Phase 1 Design Rationale; Q2/Q3 adjacency produces co-presence by proximity.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | All 5 fields specified in Phase 3 criterion construction |
| C-02 | PASS | Weight spec 3–5 / 2–3 / 1–2 present |
| C-03 | PASS | Phase 6 Scoring has formula and threshold |
| C-04 | PASS | Failure-driven criteria from Phase 2 |
| C-05 | PASS | Banned qualifier list enforced |
| C-06 | PASS | Order enforced in Phase 5 output |
| C-07 | PASS | Canonical categories listed |
| C-08 | PASS | Interrogative Q1 forces specific dominant failure; questions produce analytically distinct failures (higher specificity ceiling than imperative mandates) |
| C-09 | PASS | Q3 answer in DR is the calibration example |
| C-10 | PASS | Evolution hook in Phase 6 Scoring |
| C-11 | PASS | Phase 1 Q1 answer names dominant failure mode; appears before criteria table |
| C-12 | PASS | 8 banned qualifiers listed |
| C-13 | PASS | Named Rejection Log section (Phase 4); construction-time disqualification explicit |
| C-14 | PASS | Phase 1 Design Rationale precedes Phase 5 Rubric Table |
| C-15 | PASS | Q2 (rejected criterion) and Q3 (self-application) both in Phase 1 Design Rationale; STOP CONDITION enforces co-location; Q3 requires specific criterion ID by format instruction |
| C-16 | N/A | No revision phase |
| C-17 | N/A | No revision phase |
| C-18 | PASS | 8 banned terms listed |
| C-19 | PASS | Output-state pass conditions throughout |
| C-20 | PASS | Output section names Scoring as step 5; explicit required-element declaration |
| C-21 | PARTIAL | No role definition; "or equivalent block" phrase absent from output contract and role level |
| C-22 | PASS | Phase 4 Rejection Log: construction-time filter disqualification explicit |
| C-23 | PASS | Q2 and Q3 co-located in DR block; interrogative format enforces adjacency |
| C-24 | PARTIAL | No front-loaded Required Sections block; Output section appears after all phases — declares Scoring but achieves completeness only for sections it names at that point |
| C-25 | N/A | No role definition |

**Essential:** 5/5 × 60 = **60**
**Recommended:** 3/3 × 30 = **30**
**Aspirational:** 13.0/14 (C-21 = 0.5, C-24 = 0.5) × 10 = **9.29**
**Composite: 99.29** | All essential pass: YES

---

## V-03 — Combined DR section (merged sub-blocks)

**Axis:** Lifecycle emphasis — Phase 1 becomes a single three-sub-block Design Rationale containing all C-15-required co-presence slots.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | All 5 fields in Phase 2 criterion construction |
| C-02 | PASS | Weight spec present |
| C-03 | PASS | Phase 5 Scoring has formula and threshold |
| C-04 | PASS | Criteria derived from Sub-block A failure inventory |
| C-05 | PASS | Banned qualifiers enforced |
| C-06 | PASS | Essential → recommended → aspirational in Phase 4 |
| C-07 | PASS | Canonical categories listed |
| C-08 | PARTIAL | Three simultaneous analytical tasks (failure enumeration + pre-rejection + self-application) in Phase 1 compete for depth; failure distinctness at risk per V-03 hypothesis: "denser Phase 1 may reduce per-sub-block depth" |
| C-09 | PASS | Sub-block C self-application is the calibration example |
| C-10 | PASS | Evolution hook in Phase 5 |
| C-11 | PASS | Phase 1 is "Design Rationale equivalent block"; *(dominant)* marker required on most dangerous failure |
| C-12 | PASS | 8 banned qualifiers listed |
| C-13 | PASS | Phase 3 named Rejection Log; includes Sub-block B pre-rejected entries; construction-time disqualification explicit |
| C-14 | PASS | Phase 1 (Design Rationale equivalent) precedes Phase 4 Rubric Table |
| C-15 | PASS | Sub-block B (pre-rejected criterion) and Sub-block C (self-application) both in Phase 1; STOP CONDITION requires all three sub-blocks before Phase 2 |
| C-16 | N/A | No revision phase |
| C-17 | N/A | No revision phase |
| C-18 | PASS | 8 banned terms listed |
| C-19 | PASS | Output-state gates throughout |
| C-20 | PASS | Output section lists Scoring as item 4 |
| C-21 | PASS | "This section serves as the Design Rationale equivalent block" — equivalence phrase present in Phase 1 header; model encounters "equivalent block" concept before building criteria, propagating the phrase to produced C-11/C-14 |
| C-22 | PASS | Phase 3 Rejection Log: construction-time filter disqualification explicit |
| C-23 | PASS | Sub-blocks B and C in same Phase 1 section; structural co-presence by section design |
| C-24 | PARTIAL | No formal front-loaded Required Sections block; section obligations embedded in phase instructions only; V-03 hypothesis explicitly projects: "C-24 PARTIAL (no explicit front-loaded Required Sections block)" |
| C-25 | N/A | No role definition |

**Essential:** 5/5 × 60 = **60**
**Recommended:** 2.5/3 (C-08 = 0.5) × 30 = **25.00**
**Aspirational:** 13.5/14 (C-24 = 0.5) × 10 = **9.64**
**Composite: 94.64** | All essential pass: YES

---

## V-04 — Output format + DR-phase gate (combination)

**Axes:** Front-loaded Required Sections contract (from R5/V-02) + DR-phase self-application gate (from V-01); anti-drift obligation stated twice (in contract and in Phase 1 STOP CONDITION).

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | All 5 fields in Phase 3 |
| C-02 | PASS | Weight spec present |
| C-03 | PASS | Phase 6 Scoring has formula and threshold |
| C-04 | PASS | Failure-derived criteria |
| C-05 | PASS | Banned qualifiers enforced |
| C-06 | PASS | Tier ordering enforced |
| C-07 | PASS | Canonical categories |
| C-08 | PASS | Failure Inventory (Phase 2) drives distinct failure modes |
| C-09 | PASS | Self-application in DR provides calibration |
| C-10 | PASS | Evolution hook in Phase 6 |
| C-11 | PASS | Phase 1 DR names dominant failure mode before criteria table |
| C-12 | PASS | 8 banned qualifiers listed |
| C-13 | PASS | Named Rejection Log (Phase 4); construction-time disqualification explicit |
| C-14 | PASS | Phase 1 DR → Phase 2 Failure Inventory → Phase 4 Rejection Log → Phase 5 Rubric Table |
| C-15 | PASS | Doubled obligation: Required Sections contract + Phase 1 both mandate all 3 items in DR; anti-drift stated in both locations: contract ("this item belongs in the Design Rationale, not in the Scoring section") and STOP CONDITION |
| C-16 | N/A | No revision phase |
| C-17 | N/A | No revision phase |
| C-18 | PASS | 8 banned terms listed |
| C-19 | PASS | Output-state pass conditions |
| C-20 | PASS | Required Output Sections contract (item 5 = Scoring); absence of Scoring explicitly predicts joint C-03/C-09/C-10 failure |
| C-21 | PARTIAL | No "or equivalent block" in role definition; no role definition present; falsifiability confirms: "C-21 PARTIAL (no 'or equivalent block' phrase)" |
| C-22 | PASS | Phase 4 Rejection Log: explicit construction-time disqualification |
| C-23 | PASS | Both contract and Phase 1 enforce co-location; anti-drift note in both locations is the strongest anti-drift mechanism short of a role definition |
| C-24 | PASS | Required Output Sections block front-loads all 5 sections before Phase 1; "pre-committed structural obligation" language present |
| C-25 | N/A | No role definition |

**Essential:** 5/5 × 60 = **60**
**Recommended:** 3/3 × 30 = **30**
**Aspirational:** 13.5/14 (C-21 = 0.5) × 10 = **9.64**
**Composite: 99.64** | All essential pass: YES

---

## V-05 — Role sequence + DR-phase gate (combination)

**Axes:** RubricArchitect canonical path with "or equivalent block" in role definition + Phase 1 gains Sub-sections 1B (pre-rejection) and 1C (self-application) as explicit named sub-sections.

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | All 5 fields in Phase 2 criterion construction |
| C-02 | PASS | Weight spec present |
| C-03 | PASS | Phase 4 Scoring section has formula and threshold |
| C-04 | PASS | 6 failure entries in Sub-section 1A drive criteria derivation |
| C-05 | PASS | Banned qualifiers enforced |
| C-06 | PASS | Essential → recommended → aspirational in Phase 4 Rubric Table |
| C-07 | PASS | Canonical categories listed |
| C-08 | PASS | 6 distinct silent failures (1A); *(dominant)* marker ensures most dangerous named first |
| C-09 | PASS | Sub-section 1C self-application is the calibration example |
| C-10 | PASS | Evolution hook in Phase 4 Scoring |
| C-11 | PASS | Phase 1 Failure Inventory is the "Design Rationale equivalent block" per role definition; precedes Phase 4 criteria table |
| C-12 | PASS | 8 banned qualifiers listed |
| C-13 | PASS | Phase 3 Rejection Log named section; "construction-time filter activity alone does not satisfy this section" explicit |
| C-14 | PASS | Section 1 (Failure Inventory = DR equivalent) → Section 2 (Rejection Log) → Section 3 (Rubric Table) |
| C-15 | PASS | Sub-section 1B (pre-rejection note) + sub-section 1C (self-application gate) co-located in Phase 1 Section 1; STOP CONDITION requires all three sub-sections before Phase 2; "Both items together satisfy the co-presence requirement. Do not place this statement in the Scoring section." |
| C-16 | N/A | No revision phase |
| C-17 | N/A | No revision phase |
| C-18 | PASS | 8 banned terms listed |
| C-19 | PASS | Output-state pass conditions throughout |
| C-20 | PASS | Role preamble declares all 4 canonical sections; Phase 4 Scoring explicitly marked required with "omitting this section causes formula, threshold, and evolution hook criteria to fail simultaneously" |
| C-21 | PASS | Role definition: "the failure inventory (with its pre-rejection and self-application sub-sections) is explicitly named as satisfying the Design Rationale 'or equivalent block' requirement"; phrase present at role level, propagates to produced C-11/C-14 |
| C-22 | PASS | Phase 3 Rejection Log: "Construction-time filter activity alone does not satisfy this section" |
| C-23 | PASS | Sub-sections 1B + 1C structurally co-located in Phase 1; Global Constraints: "their co-presence in the same section satisfies the C-15 gate" |
| C-24 | PASS | Role preamble enumerates all 4 canonical sections before Phase 1; "all four sections must appear in the output" in Global Constraints |
| C-25 | PASS | Role definition ("You are a RubricArchitect…") contains "or equivalent block" explicitly naming failure inventory as DR equivalent; pass condition satisfied at role level |

**Essential:** 5/5 × 60 = **60**
**Recommended:** 3/3 × 30 = **30**
**Aspirational:** 15/15 × 10 = **10.00**
**Composite: 100** | All essential pass: YES

---

## Final Rankings

| Rank | Variation | Score | All Essential | C-15 | Delta from leader |
|------|-----------|-------|---------------|------|-------------------|
| 1 | **V-05** | 100.00 | YES | PASS | — |
| 2 | **V-01** | 99.64 | YES | PASS | −0.36 |
| 2 | **V-04** | 99.64 | YES | PASS | −0.36 |
| 4 | **V-02** | 99.29 | YES | PASS | −0.71 |
| 5 | **V-03** | 94.64 | YES | PASS | −5.36 |

---

## Key Findings — R6

### 1. All five variations solved C-15

R6's single target was achieved across all variations. Every variation placed self-application + rejected criterion in the DR/equivalent block. Three structural mechanisms all worked:
- Explicit three-item mandate + anti-drift note (V-01, V-04)
- Interrogative Q2/Q3 adjacency (V-02)
- Sub-block naming within one section (V-03, V-05)

The structural fix is robust: forcing both items into Phase 1 by any of these mechanisms reliably prevents Scoring-section drift.

### 2. The differentiation is C-21 and C-25

The 0.36-point gap between V-01/V-04 (99.64) and V-05 (100) is entirely C-21 PARTIAL vs PASS. Only V-05 achieves C-21 PASS because only V-05 anchors "or equivalent block" at the role-definition level where it propagates to the produced rubric's aspirational criteria. V-05 also unlocks C-25 (N/A → PASS) because it has a role definition at all.

### 3. Combined-phase (V-03) pays a C-08 tax

Merging failure analysis, pre-rejection, and self-application into one phase reduces failure-analysis depth. V-01 and V-05, which separate failure analysis into its own section, produce more distinct failure modes. The C-08 PARTIAL costs 5 points on the recommended band.

### 4. Front-loaded contract vs. trailing Output section

C-24 distinguishes V-01/V-04/V-05 (PASS) from V-02/V-03 (PARTIAL). Declaring sections before phases achieves completeness at declaration time; listing sections at the end achieves only what the Output block names at that point.

---

## Excellence Signals — V-05

1. **Role definition as equivalence anchor** — Embedding "or equivalent block" in the role preamble propagates the phrase to C-21 and C-25 simultaneously before any phase runs. V-01 and V-04 achieve structurally equivalent outputs without the phrase, scoring PARTIAL on both aspirational criteria.

2. **Sub-section naming forces indecomposable co-presence** — 1A/1B/1C labels within Phase 1 make all three items a single indecomposable unit. The model cannot emit Phase 1 partially; the STOP CONDITION gates on all three sub-sections. Adjacent items in a single labeled section are more reliably co-present than adjacent phases.

3. **Four-section canonical path reduces structural joints** — V-05 uses 4 sections vs. V-01's 5-phase design. Fewer phases = fewer structural joints where ordering or omission can occur. Combining Rubric Table + Scoring into Phase 4 prevents the Scoring section from being treated as optional.

4. **Global Constraints as terminal audit** — V-05 adds an explicit Global Constraints block after the phases, restating all structural requirements. This functions as a second-pass checklist that catches any obligation missed during phase construction — a pattern not present in other variations.

---

## v8 Candidate Patterns

Observed in R6 but not yet promoted to criteria:

- **role-definition-as-equivalence-anchor** — embedding "or equivalent block" in the role definition (not phase instructions) is the mechanism that propagates the phrase to C-21/C-25 simultaneously; phase-level instruction achieves structural equivalence but scores PARTIAL on both criteria; evidence: V-05 is the only variation to achieve C-21/C-25 PASS, and it is the only variation with a role definition containing the phrase
- **sub-section-naming-forces-co-presence** — numbering sub-sections (1A, 1B, 1C) within a single phase achieves structural co-presence more reliably than adjacent phases, because the model cannot skip a labeled sub-section within a phase it is actively writing; evidence: V-03 and V-05 both use sub-block/sub-section labels and both achieve C-15 PASS; V-01 uses adjacent Items without sub-section labels and achieves the same output structure but with slightly lower structural lock

Carrying forward from v7 candidates (no new evidence to promote or retire):
- joint-failure-chain-annotation
- failure-analyst-skeleton-as-canonical-path
- output-ordering-determines-c11-c14
- rejection-log-minimum-count-scales-with-aspirational-depth
- co-presence-section-scope-precision
- v04-token-budget-reliability-gap
