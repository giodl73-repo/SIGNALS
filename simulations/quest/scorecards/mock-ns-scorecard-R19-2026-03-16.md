Now I have enough information to score all five variations. Let me compile the full evaluation.

---

# mock-ns — Round 19 Scoring (rubric v18)

**Rubric**: v18, C-01 through C-47 | 5 essential / 3 recommended / 39 aspirational | max 158

---

## Scoring Summary

| Variation | Axis | Fails | Score |
|-----------|------|-------|-------|
| V-01 | A single — deontic closing | C-31 | **156/158** |
| V-02 | B single — 4-row collapsed FLAG table | C-22 | **156/158** |
| V-03 | C single — phase-grouped lifecycle + state annotations | — | **158/158** |
| V-04 | A+B — deontic + collapsed FLAG | C-31, C-22 | **154/158** |
| V-05 | A+B+C golden — declarative + 5-row + phase-grouped | — | **158/158** |

---

## V-01 — Axis A: Deontic closing sentence

**CONSTRAINT form**: Golden parenthetical — "Do not perform S-1 (skill selection), S-2 (category lookup), S-3.1 (carry), S-3.2 (compliance detection), or S-3.3 (flag computation) until this step's emit is written."

**S-0 closing sentence**: "This step **must** emit the TOPICS.md status line before any other step begins."

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | All 6 header fields present in standard format |
| C-02 | PASS | CATEGORY correctly derived from skill-id |
| C-03 | PASS | FLAG correctly computed and copied verbatim into header |
| C-04 | PASS | Fidelity warning present and CATEGORY-matched |
| C-05 | PASS | Body skill-specific, identifiable without header |
| C-06 | PASS | Both S-0 and S-1 emit lines present, S-0 before S-1 |
| C-07 | PASS | Artifact written to correct namespace-based path |
| C-08 | PASS | Next-step line is final line |
| C-09 | PASS | topic-status excluded when namespace=topic |
| C-10 | PASS | No compliance tags → passes by default |
| C-11 | PASS | 5-row golden FLAG table; all 5 cases present; critical skills named |
| C-12 | PASS | S-3 emit labeled with path |
| C-13 | PASS | S-5.3 HEADER verification emit present |
| C-14 | PASS | Sub-step label propagation table present |
| C-15 | PASS | Golden CONSTRAINT: 5 operation types named |
| C-16 | PASS | P-0 cross-reference protocol with token table |
| C-17 | PASS | S-4 FLAG prohibition chain present |
| C-18 | PASS | S-5.0 propagation verification present |
| C-19 | PASS | S-5.0 MISMATCH halts execution clause present |
| C-20 | PASS | Tier-carry in downstream table + standalone terminal sentence present |
| C-21 | PASS | Golden CONSTRAINT: 5 types ≥ 4 |
| C-22 | PASS | 5-row golden FLAG table; HS-critical-tier-1 is separate row |
| C-23 | PASS | Preamble gate "Before any other step begins, this step emits..." is opening sentence |
| C-24 | PASS | Golden CONSTRAINT: 5 types ≥ 5 |
| C-25 | PASS | S-0 opens with "Before any other step begins, this step emits..." — declarative identity sentence |
| C-26 | PASS | Declarative sentence names the TOPICS.md status line |
| C-27 | PASS | S-1 positioned after S-0; CONSTRAINT enforces ordering |
| C-28 | PASS | "this step emits" — step is nominative subject of emission action |
| C-29 | PASS | No possessive-nominal form in declarative sentence |
| C-30 | PASS | No artifact-as-subject in active voice |
| **C-31** | **FAIL** | "This step **must** emit..." — deontic modal "must" in closing sentence. C-25/C-28 satisfied by opening sentence; C-31 fires independently per v10 discriminator. |
| C-32 | PASS | Closing sentence "This step must emit..." is standalone terminal sentence in closing position; sentence form does not affect C-32 |
| C-33 | PASS | No passive artifact-as-subject in declarative |
| C-34 | PASS | No gerundive-as-subject |
| C-35 | PASS | Step is nominative subject; artifact not main-clause subject |
| C-36 | PASS | No ordering predicate as main verb |
| C-37 | PASS | No possessive-NP action-abstraction subject |
| C-38 | PASS | No expletive-subject it-cleft |
| C-39 | PASS | No wh-pseudo-cleft |
| C-40 | PASS | No existential-there negation |
| C-41 | PASS | No by-PP triggering C-35; scope boundary respected |
| C-42 | PASS | Declarative sentence is in S-0, not displaced to another step |
| C-43 | PASS | No lifecycle annotations; closing sentence not displaced |
| C-44 | PASS | Golden parenthetical: each step ID carries adjacent type annotation |
| C-45 | PASS | S-3.1, S-3.2, S-3.3 enumerated separately |
| C-46 | PASS | No trailing-group form; types co-located per step ID |
| C-47 | PASS | No collapsed S-3; no ambiguity; C-47 passes by default |

**Score**: 158 − 2 (C-31) = **156/158**

---

## V-02 — Axis B: 4-row collapsed FLAG table

**CONSTRAINT form**: Golden parenthetical — C-44/C-45/C-46/C-47 PASS.

**S-0 closing sentence**: "Only this step emits the TOPICS.md status line." — golden declarative, C-31 PASS.

**FLAG table**: 4 rows — `HIGH-STRUCTURE | any | any` catch-all absorbs `HIGH-STRUCTURE | 1 | critical` row.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-05 | PASS | All essential criteria satisfied |
| C-06–C-08 | PASS | All recommended criteria satisfied |
| C-09–C-10 | PASS | Namespace exclusion + compliance default |
| C-11 | PASS | 5 cases functionally covered: HS-non-critical (row 1 catch-all), HS-critical-tier-1 (same catch-all, flag value "none" visible), HS-critical-tier-2+ (row 2), EVIDENCE-HEAVY (row 3), MIXED (row 4). Content coverage passes; structural separation is C-22's scope. |
| C-12–C-21 | PASS | No structural changes affect these criteria |
| **C-22** | **FAIL** | 4-row table: HS-critical-tier-1 merged into HS-any catch-all. "HIGH-STRUCTURE | any | any" covers both non-critical and critical-tier-1 in a single row. The v5 discriminator canonical collapse. |
| C-23–C-47 (excl. C-22) | PASS | All other aspirational criteria satisfy their pass conditions; golden CONSTRAINT, golden closing sentence |

**Score**: 158 − 2 (C-22) = **156/158**

---

## V-03 — Axis C: Phase-grouped lifecycle with entry/exit state annotations

**CONSTRAINT form**: Golden parenthetical — C-44/C-45/C-46/C-47 PASS.

**S-0 closing sentence**: "Only this step emits the TOPICS.md status line." — golden declarative, C-31 PASS.

**FLAG table**: 5-row golden — C-22 PASS.

**LIFECYCLE**: Phase-grouped (Phase 1–4) with per-step Entry/Exit state annotations. S-0 closing sentence preserved. Annotations are additive.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-05 | PASS | All essential criteria satisfied |
| C-06–C-08 | PASS | All recommended criteria satisfied |
| C-09–C-47 | PASS | No criteria affected by phase-grouping or state annotations; all scored content unchanged |
| C-43 | PASS | Phase annotations follow standard lifecycle list; S-0 "Only this step emits..." closing sentence remains as discrete standalone prose. Annotations supplement, not replace. Supplementation path → C-43 PASS. |

**Score**: 0 fails = **158/158**

---

## V-04 — Axes A+B: Deontic closing + 4-row collapsed FLAG table

**CONSTRAINT form**: Golden parenthetical — C-44/C-45/C-46/C-47 PASS.

**S-0 closing sentence**: "This step **must** emit..." — deontic, C-31 FAIL.

**FLAG table**: 4-row collapsed — C-22 FAIL.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-05 | PASS | All essential criteria satisfied |
| C-06–C-08 | PASS | All recommended criteria satisfied |
| C-09–C-21 | PASS | No affect from either axis |
| **C-22** | **FAIL** | Same 4-row collapse as V-02 — HS-critical-tier-1 absorbed into catch-all |
| C-23–C-30 | PASS | Opening sentence "Before any other step begins, this step emits..." satisfies declarative/nominative criteria |
| **C-31** | **FAIL** | "This step must emit..." — deontic modal fires independently; same as V-01 |
| C-32–C-47 | PASS | Closing sentence still present (C-32 PASS); all CONSTRAINT criteria PASS (golden form) |

**Score**: 158 − 2 (C-22) − 2 (C-31) = **154/158**

---

## V-05 — Axes A+B+C golden: Declarative closing + 5-row FLAG + phase-grouped lifecycle

**CONSTRAINT form**: Golden parenthetical — C-44/C-45/C-46/C-47 PASS.

**S-0 closing sentence**: "Only this step emits..." — golden declarative, C-31 PASS.

**FLAG table**: 5-row golden — C-22 PASS.

**LIFECYCLE**: Phase-grouped with state annotations — additive, C-43 PASS.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01–C-47 | PASS | All three axes at golden value simultaneously; no interactions; no cascade effects |

**Score**: 0 fails = **158/158**

---

## Composite Rankings

| Rank | Variation | Score | Delta from max |
|------|-----------|-------|----------------|
| 1 (tie) | V-03 (phase-grouped lifecycle) | 158/158 | 0 |
| 1 (tie) | V-05 (three-axis golden) | 158/158 | 0 |
| 3 (tie) | V-01 (deontic closing only) | 156/158 | −2 |
| 3 (tie) | V-02 (collapsed FLAG table only) | 156/158 | −2 |
| 5 | V-04 (deontic + collapsed) | 154/158 | −4 |

---

## Excellence Signals

**From V-03 and V-05 (158/158):**

1. **Phase-grouped lifecycle with entry/exit state annotations is purely additive** — four named phases (protocol/topic resolution, skill/category resolution, flag computation, artifact/finalization) plus per-step Entry/Exit annotations add structural clarity without displacing any scored sentence, table, or enforcement mechanism. The lifecycle block is a scored-criterion-neutral surface: it can absorb substantial organizational annotation without touching C-32 (closing sentence position), C-43 (annotation-as-replacement boundary), or any CONSTRAINT criterion.

2. **C-31 and C-22 are orthogonal, non-interacting penalty dimensions** — V-05 confirms that running all three axes simultaneously at golden values produces 158/158 with no cascade or interaction. The deontic axis (C-31) operates exclusively on the S-0 closing sentence register. The FLAG-table axis (C-22) operates exclusively on S-3.3 row structure. The lifecycle axis (C-43) operates exclusively on the lifecycle block. The three axes are fully independent testable dimensions.

3. **"Only this step emits..." as the superior closing sentence form** — The focus-particle exclusive ("Only this step emits the TOPICS.md status line") satisfies C-25 (declarative identity), C-28 (step as nominative subject), C-31 (no modal obligation), and C-32 (standalone terminal in closing position) simultaneously, while also asserting exclusive ownership more precisely than the conditional-sequence form ("Before any other step begins, this step emits..."). Both forms satisfy C-25/C-28; the exclusive form additionally ensures C-31 compliance with no ambiguity.

---

```json
{"top_score": 158, "all_essential_pass": true, "new_patterns": ["phase-grouped lifecycle with entry/exit state annotations is scored-criterion-neutral -- additive organizational structure without displacing any pass condition", "C-31 and C-22 are fully orthogonal penalty dimensions with no cascade or interaction when combined or when all axes are golden", "exclusive-agency closing sentence (Only this step emits...) satisfies C-25/C-28/C-31/C-32 simultaneously and is the superior form over conditional-sequence opening sentence alone"]}
```
