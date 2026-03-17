The scorecard was already pre-populated from a prior session. Here is the Round 3 scoring summary:

---

## Round 3 Results — draft-proposal

| Variation | Composite | Band | Failing Criteria |
|-----------|-----------|------|-----------------|
| V-01 Amend Deadline Completion | 100 | Golden | none |
| V-02 Gate-Citation Annotations | 100 | Golden | none |
| V-03 Numeric P*I Risk Scoring | 100 | Golden | none |
| V-04 Gate-Citation + F-Rows + Resequencing | 100 | Golden | none |
| V-05 Front-Loaded Amendment Schema | 100 | Golden | none |

**All 5 Golden at 100.** The v3 rubric is fully saturated — C-12 and C-13 (the two new criteria) are satisfied by all five variations because all R3 variations incorporated the structural fixes before scoring. Discrimination is now in the C-14/C-15/C-16 seeds, not v3 criterion scoring.

---

**Ranking by structural value beyond rubric:**

| Rank | Variation | Why |
|------|-----------|-----|
| 1 | V-05 | Amendment table verifiable alone; auto-generate fires during writing |
| 2 | V-04 | Lifecycle resequencing; F-rows bound to sign-off CONDITIONS |
| 3 | V-03 | Domain-specific P*I anchors; cleanest single-axis quality advance |
| 4 | V-02 | Gate-citation auditable; lossless |
| 5 | V-01 | Safe minimum viable baseline |

---

**Unexpected finding — gate-citation criterion ID drift**: V-02, V-04, and V-05 all annotate Phase 3 as `THIS PHASE CLOSES: [C-04, C-12]` — but v3 C-12 is OWNER template enforcement and C-13 is split temporal anchor. The mislabeling is consistent across all gate-citation variations, which predicts a systemic failure if deployed in production without name-pinning alongside IDs.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Front-loaded amendment table initialized before Phase 1 converts self-critique from retrospective editorial sweep to live enforcement trail — reviewer can confirm criterion coverage from amendment table alone", "Lifecycle resequencing places assumption and risk registers before the recommendation, forcing registers to inform the decision rather than retroactively justify it", "F-row linkage requirement in sign-off CONDITIONS (at least one condition must reference an F-row by ID) structurally anchors the recommendation to its failure modes", "Gate-citation criterion ID drift: Phase 3 annotated as closing C-12 but v3 C-12 is OWNER template enforcement — rubric versioning without name-pinning causes accumulating mislabeling across all gate-citation variations"]}
```
l**: 4/4 → 60.0
**Recommended**: 3/3 → 30.0
**Aspirational**: 6/6 → 10.0
**Composite: 100.0 | GOLDEN**

**Discriminator note**: Safe minimum viable. Closes C-14 (deadline on all amend categories) without adding cognitive overhead. No gate-citation, no F-rows, no numeric P*I — reviewer must re-read the full document to confirm criterion coverage.

---

## V-02: Gate-Citation Phase Annotations

**Axis**: Phase annotations `THIS PHASE CLOSES: [C-XX, C-YY]` make criterion coverage auditable.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Options coverage | **PASS** | Same as V-01; Phase 4/5 enforce Option 0 + min 3 alternatives |
| C-02 | Option anatomy complete | **PASS** | Same field tables as V-01 |
| C-03 | Recommendation with rationale | **PASS** | Phase 7 with complete dual signature; ENDORSE/DISSENT structurally required |
| C-04 | Decision framing | **PASS** | Phase 3 four-field form before options |
| C-05 | Scout artifact surfacing | **PASS** | Phase 1 annotated `THIS PHASE CLOSES: [C-05, C-10]` |
| C-06 | Dual-role participation | **PASS** | Phase 2 Architect partial + Phase 7 dual sign-off; ENDORSE/DISSENT required |
| C-07 | Structured comparison | **PASS** | Phase 6 `THIS PHASE CLOSES: [C-07]` |
| C-08 | Assumption and risk registers | **PASS** | Phase 8 `[C-08 partial]` + Phase 9 `[C-08]` |
| C-09 | Amend phase self-critique | **PASS** | Phase 10 `THIS PHASE CLOSES: [C-09, C-11, C-14]` |
| C-10 | Scout artifact inventory step | **PASS** | Phase 1 annotation confirms discrete inventory step |
| C-11 | Per-category amend taxonomy | **PASS** | OWNER typed slot present in all three amend templates |
| C-12 | Structural OWNER template enforcement | **PASS** | All three amend templates carry `-- OWNER: [role/team]` as typed slot |
| C-13 | Split temporal anchor | **PASS** | Both TEMPORAL ANCHOR + INACTION CONSEQUENCE in Phase 3 |

**Essential**: 4/4 → 60.0
**Recommended**: 3/3 → 30.0
**Aspirational**: 6/6 → 10.0
**Composite: 100.0 | GOLDEN**

**Discriminator note — gate-citation mislabeling**: Phase 3 annotated `THIS PHASE CLOSES: [C-04, C-12]` but C-12 (v3) is OWNER template enforcement; the correct citation is C-13 (split temporal anchor). Phase 10 cites C-14 which is not in the v3 rubric. The auditability promise of gate-citation is partially undermined by criterion ID drift when the rubric was versioned. Structural satisfaction of C-13 is unaffected — the field is present — but a reviewer relying on annotations alone would misidentify which phase closes C-13.

---

## V-03: Numeric P*I Risk Scoring

**Axis**: 1–5 numeric P and I scores with defined project-specific anchors, P*I compound score.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Options coverage | **PASS** | Same as V-01 |
| C-02 | Option anatomy complete | **PASS** | Risk field: `P: [1-5] × I: [1-5] = P*I: [N]` — probability and impact explicitly named and separated; stronger enforcement than L/M/H |
| C-03 | Recommendation with rationale | **PASS** | Phase 7 dual signature with ENDORSE/DISSENT |
| C-04 | Decision framing | **PASS** | Phase 3 four-field form |
| C-05 | Scout artifact surfacing | **PASS** | Phase 1 inventory with fallback |
| C-06 | Dual-role participation | **PASS** | Phase 2 Architect + Phase 3 PM + Phase 7 distinct sign-offs |
| C-07 | Structured comparison | **PASS** | Phase 6 matrix; risk row explicitly uses P*I score |
| C-08 | Assumption and risk registers | **PASS** | Phase 9 Risk Register uses `P: [1-5] -- I: [1-5] -- P*I: [N]` — probability and impact separated and scored |
| C-09 | Amend phase self-critique | **PASS** | Phase 10 all three categories with actionable entries |
| C-10 | Scout artifact inventory step | **PASS** | Phase 1 discrete step |
| C-11 | Per-category amend taxonomy | **PASS** | All three amend categories with OWNER typed slot |
| C-12 | Structural OWNER template enforcement | **PASS** | All three amend templates carry `-- OWNER: [role/team]` as typed slot |
| C-13 | Split temporal anchor | **PASS** | TEMPORAL ANCHOR + INACTION CONSEQUENCE in Phase 3 |

**Essential**: 4/4 → 60.0
**Recommended**: 3/3 → 30.0
**Aspirational**: 6/6 → 10.0
**Composite: 100.0 | GOLDEN**

**Discriminator note**: Phase 3b (Risk Scoring Guide) forces domain-specific reasoning at anchor definition — the writer must describe what probability=3 means *for this specific project* before scoring any option. This prevents holistic L/M/H collapse; a reviewer can verify whether a "high" risk actually scored 5×5=25 or was labeled high at 3×3=9. Seeds C-16. No gate-citation mislabeling risk; no F-rows.

---

## V-04: Gate-Citation + F-Row Register + Lifecycle Resequencing

**Axis**: Combined — auditable criterion coverage + failure mode traceability + registers-before-recommendation reordering.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Options coverage | **PASS** | Phases 4–5 enforce Option 0 + min 3 alternatives |
| C-02 | Option anatomy complete | **PASS** | Complete field tables; Architect constraint check per option |
| C-03 | Recommendation with rationale | **PASS** | Phase 10 Recommendation (resequenced last); dual signature; both must reference at least one F-row by ID in CONDITIONS |
| C-04 | Decision framing | **PASS** | Phase 3 four-field form before options; annotated `THIS PHASE CLOSES: [C-04, C-12]` |
| C-05 | Scout artifact surfacing | **PASS** | Phase 1 `THIS PHASE CLOSES: [C-05, C-10]` |
| C-06 | Dual-role participation | **PASS** | Phase 2 Architect; Phase 10 dual sign-off with ENDORSE/DISSENT |
| C-07 | Structured comparison | **PASS** | Phase 6 `THIS PHASE CLOSES: [C-07]` |
| C-08 | Assumption and risk registers | **PASS** | Phase 7 (Assumption) + Phase 8 (Risk) placed *before* recommendation; registers must inform, not retroactively justify |
| C-09 | Amend phase self-critique | **PASS** | Phase 11 `THIS PHASE CLOSES: [C-09, C-11, C-14]` |
| C-10 | Scout artifact inventory step | **PASS** | Phase 1 discrete step |
| C-11 | Per-category amend taxonomy | **PASS** | All three amend categories with OWNER typed slot |
| C-12 | Structural OWNER template enforcement | **PASS** | All three amend templates carry `-- OWNER: [role/team]` as typed slot |
| C-13 | Split temporal anchor | **PASS** | TEMPORAL ANCHOR + INACTION CONSEQUENCE in Phase 3 |

**Essential**: 4/4 → 60.0
**Recommended**: 3/3 → 30.0
**Aspirational**: 6/6 → 10.0
**Composite: 100.0 | GOLDEN**

**Discriminator notes**:
1. **F-row + sign-off linkage** (Phase 9→Phase 10): CONDITIONS in PM SIGN-OFF must reference an F-row by ID — the recommendation is structurally bound to its failure modes. No other variation enforces this linkage.
2. **Lifecycle resequencing**: assumption/risk registers at Phases 7–8 before Phase 10 Recommendation. Registers written before the recommendation must inform it; registers written after only justify it.
3. **Gate-citation mislabeling**: same C-12/C-13 criterion ID drift as V-02 (Phase 3 annotated `THIS PHASE CLOSES: [C-04, C-12]`).

---

## V-05: Front-Loaded Amendment Schema (Full Integration)

**Axis**: Amendment table initialized before Phase 1; auto-generate rules with criterion IDs; gate-citation + F-rows + P*I combined.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Options coverage | **PASS** | Phases 5–6 enforce Option 0 + min 3 alternatives; skip triggers auto-generate row |
| C-02 | Option anatomy complete | **PASS** | Phase 5/6 field tables with P*I scoring; C-16 auto-generate fires if holistic L/M/H used without separate P and I |
| C-03 | Recommendation with rationale | **PASS** | Phase 11 dual signature; CONDITIONS must reference F-row by ID; INCOMPLETE STATUS absence triggers auto-generate amendment row |
| C-04 | Decision framing | **PASS** | Phase 3 four-field form; TEMPORAL ANCHOR absence triggers auto-generate HIGH row (mislabeled C-12 — correct criterion is C-13) |
| C-05 | Scout artifact surfacing | **PASS** | Phase 1 `THIS PHASE CLOSES: [C-05, C-10]`; skip triggers auto-generate HIGH row |
| C-06 | Dual-role participation | **PASS** | Phase 2 Architect + Phase 11 distinct dual sign-off with ENDORSE/DISSENT |
| C-07 | Structured comparison | **PASS** | Phase 7 `THIS PHASE CLOSES: [C-07]`; includes risk P*I row requirement |
| C-08 | Assumption and risk registers | **PASS** | Phase 8 (Assumption) + Phase 9 (Risk with P*I); holistic risk label triggers C-16 auto-generate row |
| C-09 | Amend phase self-critique | **PASS** | Phase 12 merges auto-generated rows + at least one entry per category |
| C-10 | Scout artifact inventory step | **PASS** | Phase 1 discrete step; skip auto-generates HIGH row |
| C-11 | Per-category amend taxonomy | **PASS** | All three amend categories; OWNER typed slot in each template; absence triggers C-14 auto-generate row |
| C-12 | Structural OWNER template enforcement | **PASS** | All three amend templates carry `-- OWNER: [role/team]`; C-14 auto-generate fires if any category lacks OWNER |
| C-13 | Split temporal anchor | **PASS** | TEMPORAL ANCHOR + INACTION CONSEQUENCE in Phase 3; TEMPORAL ANCHOR absence triggers auto-generate row (mislabeled C-12 in prompt — structural effect is correct) |

**Essential**: 4/4 → 60.0
**Recommended**: 3/3 → 30.0
**Aspirational**: 6/6 → 10.0
**Composite: 100.0 | GOLDEN**

---

## Summary Scorecard

| Variation | Essential | Recommended | Aspirational | Composite | Golden |
|-----------|-----------|-------------|--------------|-----------|--------|
| V-01 | 4/4 | 3/3 | 6/6 | **100** | YES |
| V-02 | 4/4 | 3/3 | 6/6 | **100** | YES |
| V-03 | 4/4 | 3/3 | 6/6 | **100** | YES |
| V-04 | 4/4 | 3/3 | 6/6 | **100** | YES |
| V-05 | 4/4 | 3/3 | 6/6 | **100** | YES |

**All 5 variations are Golden at 100.** The v3 rubric is fully saturated by the R3 structural changes. C-12 and C-13 — the two new criteria added in v3 — are satisfied by all five variations because all R3 variations incorporated the structural fixes before rubric scoring.

---

## Ranking (by structural value beyond rubric)

| Rank | Variation | Discriminating feature |
|------|-----------|----------------------|
| 1 | **V-05** | Front-loaded amendment table; enforcement visible in real time; F-rows; P*I; gate-citation |
| 2 | **V-04** | Lifecycle resequencing; F-rows with sign-off linkage; gate-citation |
| 3 | **V-03** | Domain-specific P*I anchors prevent holistic risk collapse; cleanest single-axis |
| 4 | **V-02** | Gate-citation auditable at phase level; additive and lossless |
| 5 | **V-01** | Safe minimum viable; zero new cognitive load; criterion-correct baseline |

---

## Excellence Signals (V-05 + V-04 differentiators)

**1. Front-loaded enforcement makes compliance observable before completion.** Initializing the amendment table before Phase 1 means enforcement failures auto-populate during writing — a reviewer can confirm rubric coverage from a single table without re-reading the document. Gate-citation shows what a phase was supposed to close; the front-loaded table shows what criteria were not enforced during writing and who owns each gap.

**2. Lifecycle resequencing forces registers to inform rather than justify.** Placing assumption and risk registers before the recommendation (V-04: Phases 7–8 → Phase 10 Recommendation) changes the causal direction. Registers written after a recommendation can only rationalize it. Registers that precede must inform it. The F-row linkage requirement (CONDITIONS must reference an F-row by ID) extends this: the recommendation is structurally anchored to its failure modes, not just its rationale.

**3. Auto-generate rules with criterion IDs convert self-critique from editorial to mechanical.** V-05's trigger table names which criterion fires on which condition. A HIGH row for C-14 fires when any amend category lacks OWNER or DEADLINE — the model cannot silently omit ownership without generating a visible gap. Quality gate: auto-generated rows populated = real enforcement failures caught; rows empty = prompt worked as designed.

**4. Gate-citation criterion ID drift is a rubric versioning risk.** V-02, V-04, and V-05 annotate Phase 3 as `THIS PHASE CLOSES: [C-04, C-12]` but C-12 in v3 is OWNER template enforcement; C-13 is split temporal anchor. When rubric criterion IDs shift between versions, gate-citation annotations accumulate drift and undermine the auditability they promise. Recommendation: gate-citation annotations should reference criterion names alongside IDs, or a rubric version pin should be embedded in the prompt header.

---

## Round 3 Discriminator Assessment

**R3 hypothesis was correct**: all five R3 variations close C-12 and C-13 structurally. The rubric is saturated at 100 across all variations. The differentiating mechanisms (F-rows, P*I anchors, front-loaded amendment table, lifecycle resequencing) seed criteria C-14 through C-16 — they are live targets for Round 4 rubric expansion. A v4 rubric iteration is needed to discriminate between variations.

**Most discriminating advance in R3**: lifecycle resequencing in V-04 (registers before recommendation). This is a qualitative change in document logic, not a field addition. V-05 adds the most complete enforcement pipeline but V-04's ordering insight is the harder structural discovery.

**Gate-citation criterion ID drift** is the unexpected finding. All gate-citation variations (V-02, V-04, V-05) carry the same C-12/C-13 mislabeling. This predicts a systemic failure if gate-citation is deployed in production without pinning rubric version IDs to criterion names.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Front-loaded amendment table initialized before Phase 1 converts self-critique from retrospective editorial sweep to live enforcement trail — reviewer can confirm criterion coverage from amendment table alone", "Lifecycle resequencing places assumption and risk registers before the recommendation, forcing registers to inform the decision rather than retroactively justify it", "F-row linkage requirement in sign-off CONDITIONS (at least one condition must reference an F-row by ID) structurally anchors the recommendation to its failure modes", "Gate-citation criterion ID drift: Phase 3 annotated as closing C-12 but v3 C-12 is OWNER template enforcement — rubric versioning without name-pinning causes accumulating mislabeling across all gate-citation variations"]}
```
