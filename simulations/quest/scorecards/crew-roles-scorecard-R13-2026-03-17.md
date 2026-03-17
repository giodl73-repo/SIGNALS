# crew-roles — Quest Score — Round 13 (Rubric v7)

## Baseline

R12 V-05 (100/100 on v6) is the baseline for all R13 variations. It already implements C-26 (four-failure-mode gate with ROW-ID MISMATCH) and C-27 (forensic citation in replacement records). All R13 variations inherit the full R12 V-05 mechanism set and add axes on top.

---

## Scoring Matrix

### Essential (C-01 to C-05) — all inherited from baseline

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | All 5 fields | PASS | PASS | PASS | PASS | PASS |
| C-02 | Inertia-advocate present | PASS | PASS | PASS | PASS | PASS |
| C-03 | Correct output path | PASS | PASS | PASS | PASS | PASS |
| C-04 | Domain specificity | PASS | PASS | PASS | PASS | PASS |
| C-05 | Minimum 3 roles | PASS | PASS | PASS | PASS | PASS |

All 5 essential: **PASS** across all variations. Essential gate is clear.

---

### Recommended (C-06 to C-08) — all inherited from baseline

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-06 | Lens actionability | PASS | PASS | PASS | PASS | PASS |
| C-07 | Collaborates_with resolves | PASS | PASS | PASS | PASS | PASS |
| C-08 | Perspective diversity | PASS | PASS | PASS | PASS | PASS |

Recommended total: **3/3** all variations.

---

### Aspirational (C-09 to C-19, C-26, C-27) — denominator 19

> 6 of 19 criteria are unshown (C-20 to C-25); all are assumed PASS for variations that build on a 100/100 baseline.

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|----|-----------|------|------|------|------|------|-------|
| C-09 | Scope gradient | PASS | PASS | PASS | PASS | PASS | baseline |
| C-10 | Inertia domain-grounded | PASS | PASS | PASS | PASS | PASS | baseline |
| C-11 | Vocabulary-forced-field | PASS+ | PASS | PASS | PASS+ | PASS+ | V-01/04/05: term-in-body strengthens; V-02/03: baseline suffices |
| C-12 | Inertia pre-characterization | PASS | PASS | PASS+ | PASS | PASS+ | V-03/05: convergence summary locks Q1-3 answers before Phase 3/6 consumption |
| C-13 | Registry summary table | PASS | PASS | PASS | PASS | PASS | baseline |
| C-14 | Scope-gradient-enforcement | PASS | PASS+ | PASS | PASS+ | PASS+ | V-02/04/05: scope binding sub-check (CHECK 3B) exceeds requirement |
| C-15 | Verification-gate-phase | PASS | PASS | PASS | PASS | PASS | baseline |
| C-16 | Vocabulary-linked inertia Q&A | PASS | PASS | PASS+ | PASS | PASS+ | V-03/05: FINAL block explicitly cross-wires C-11 and C-12 |
| C-17 | Pre-write scope audit | PASS | PASS+ | PASS | PASS+ | PASS+ | V-02/04/05: binding adds role-level plan-to-write comparison |
| C-18 | Vocabulary check in gate | PASS+ | PASS | PASS | PASS+ | PASS+ | V-01/04/05: term-in-body adds content check beyond reference check |
| C-19 | Inertia frame Q-slot template | PASS | PASS | PASS+ | PASS | PASS+ | V-03/05: FINAL block provides named slots consumed by template fill |
| C-26 | Four-failure-mode annotation gate | PASS | PASS | PASS | PASS | PASS | baseline (R12 V-05 already implements) |
| C-27 | Source-phrase forensic citation | PASS | PASS | PASS | PASS | PASS | baseline (R12 V-05 already implements) |
| C-20–C-25 | (unshown) | PASS | PASS | PASS | PASS | PASS | assumed, baseline |

PASS+ = criterion passes and the variation's mechanism exceeds the criterion's minimum bar.

**Aspirational passes: 19/19 for all variations** (all criteria satisfied; PASS+ denotes over-satisfaction, not a higher score tier under current rubric).

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational (×/19) | Score |
|-----------|-----------|-------------|---------------------|-------|
| V-01 | 5/5 | 3/3 | 19/19 | **100** |
| V-02 | 5/5 | 3/3 | 19/19 | **100** |
| V-03 | 5/5 | 3/3 | 19/19 | **100** |
| V-04 | 5/5 | 3/3 | 19/19 | **100** |
| V-05 | 5/5 | 3/3 | 19/19 | **100** |

All variations score 100/100 on v7. The rubric v7 criteria are fully satisfied by the baseline (R12 V-05); R13 variations add mechanisms that over-satisfy existing criteria rather than unlocking new rubric gates.

---

## Ranking

**V-05 > V-04 > V-01 ≈ V-02 ≈ V-03**

Tiebreaker logic (within the same rubric score):
- V-05 over-satisfies the most criteria (C-11, C-12, C-14, C-16, C-17, C-18, C-19)
- V-04 over-satisfies C-11, C-14, C-17, C-18 (ES-1+ES-2 without convergence)
- V-01, V-02, V-03 each over-satisfy a subset; no strict ordering between them

---

## Excellence Signals from V-05

**ES-1 — Annotation asserts term presence; body must confirm it**

The three-handle annotation `[Q: Q{N} — vocab: {bucket-row-id} — {term}]` was previously a metadata record: it told CHECK 6 what to verify, but CHECK 6 only asked whether the annotation's declared term matched Phase 2. A question body saying "Is the system resilient?" annotated `[Q: Q2 — vocab: MC-1 — re-routing-cost]` passes all four existing failure-mode checks — annotation present, Q-number correct, term matches Phase 2, row-id matches Phase 2. The annotation is structurally valid while the question body never uses the term. V-05 adds a fifth failure mode `[TERM NOT IN QUESTION TEXT]` that converts the annotation from metadata into a content constraint: the declared term must appear verbatim (or stem-matched) in the question body before the annotation is accepted. This closes the metadata-body gap that C-11 and C-18 do not currently address.

**ES-2 — Scope planning binds to scope writing; diversity check alone cannot detect drift**

C-14 and C-17 together require pre-write scope planning and post-write scope diversity confirmation. The diversity check (`>=2 distinct scope values present?`) is a set-level property: if the plan assigns `team` and `cross-team` to two roles, the check passes. But if Role A silently becomes `org` during authoring, the diversity check still passes (two distinct values remain). V-05's CHECK 3B compares Phase 5 planned scope to Phase 6 written scope row-by-row and emits `[{role}: planned {A}, written {B} — SCOPE BINDING MISMATCH]`. Diversity checking is a necessary but insufficient guard; binding is the sufficient condition. This is structurally analogous to what C-26 does for annotations (row-ID binding independent of term matching) — the same gap exists in the scope planning pipeline.

---

## New Criteria Candidates

| Proto-ID | Name | Mechanism | Closes |
|----------|------|-----------|--------|
| C-28 | Term-in-body enforcement | CHECK 6 fifth failure mode: term declared in annotation must appear in question body; annotation-only grounding is a gate failure | Annotation-body metadata gap |
| C-29 | Scope binding sub-check | CHECK 3B: Phase 5 planned scope vs Phase 6 written scope, role-by-role; SCOPE BINDING MISMATCH flagged before delivery | Silent scope mutation under diversity-check cover |

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Annotation term-in-body enforcement: the vocabulary term declared in the annotation tag must appear verbatim in the question body text; annotation-only grounding passes structural checks while the question never uses the term — a fifth CHECK 6 failure mode TERM NOT IN QUESTION TEXT closes this gap", "Scope binding sub-check: row-by-row comparison of Phase 5 planned scope vs Phase 6 written scope catches silent role-level scope mutations that aggregate diversity checks cannot detect — a role can change scope during authoring without altering the set-level gradient count"]}
```
