Now I have all the information needed. Let me perform the full scoring.

---

# mock-ns — Round 18 Scoring (rubric v18)

**Rubric max: 158 pts** | 5 essential (50) + 3 recommended (30) + 39 aspirational (78)
**New criteria in scope: C-46 (trailing-group form), C-47 (scope boundary + cascade)**

---

## Uniform Criteria (all five variations identical)

All variations share the same structure outside the CONSTRAINT line. Evaluated once; applies to V-01 through V-05.

### Essential C-01–C-05: **All PASS (50/50)**

| Criterion | Evidence | Verdict |
|-----------|----------|---------|
| C-01 | Header block present with skill, topic, tier, category, flag, date — 6 fields | PASS |
| C-02 | S-2 lookup table present and complete; skill-id maps to CATEGORY correctly | PASS |
| C-03 | 5-row FLAG table with compliance path; verbatim copy instruction explicit | PASS |
| C-04 | Category-matched fidelity warning section (HIGH-STRUCTURE / EVIDENCE-HEAVY / MIXED) | PASS |
| C-05 | S-4 body instruction: correct section headings, skill-specific tables, gate/verdict position | PASS |

### Recommended C-06–C-08: **All PASS (30/30)**

| Criterion | Evidence | Verdict |
|-----------|----------|---------|
| C-06 | S-0 emit (TOPICS.md status line) + S-1 emit (Generating mock...) both present, S-0 before S-1 | PASS |
| C-07 | `> Artifact written: simulations/mock/{topic}-{namespace}-mock-{date}.md` emit present | PASS |
| C-08 | `Next: /mock:review {topic} simulations/mock/...` written as last line of artifact | PASS |

### Aspirational C-09–C-43: **All PASS (70/70 in golden form)**

All five variations use the same S-0–S-5 structure. Per V-04/V-05 scoring 158/158 (zero failures outside CONSTRAINT axis), these criteria pass uniformly.

| Range | Notable checks | Verdict |
|-------|----------------|---------|
| C-09 | S-1 table includes `NEVER topic-status` exclusion note | PASS |
| C-10 | No compliance tags present in scenario → passes by default | PASS |
| C-11 | 5-case FLAG table present; critical namespaces enumerated | PASS |
| C-12 | S-0 is a discrete labeled step before S-1 | PASS |
| C-13 | S-2 lookup table present with halt-on-unrecognized logic | PASS |
| C-14 | S-4 HEADER BLOCK / FIDELITY WARNING / MOCK BODY + S-5.4 WRITE / next-step = 5 discrete labeled output responsibilities | PASS |
| C-15–C-24 | Variable — scored per variation below | — |
| C-16 | `trace-*`, `listen-*`, `scout-feasibility` in Critical skills line adjacent to FLAG table | PASS |
| C-17 | "Before any other step begins, this step emits the TOPICS.md status line" + CONSTRAINT names S-1 | PASS |
| C-18 | Resolution table Downstream-Action column names S-3.1, S-3.2, S-3.3 consumers | PASS |
| C-19 | Preamble gate ("Before any other step begins...") + terminal gate ("Only this step emits...") both present | PASS |
| C-20 | Table downstream-use column + "Only this step emits..." terminal sentence | PASS |
| C-22 | FLAG table separates HIGH-STRUCTURE critical tier=1 row from non-critical row | PASS |
| C-23 | "Before any other step begins, this step emits..." appears before resolution table; CONSTRAINT is post-preamble defense layer in this prompt form | PASS |
| C-25 | S-0 opens with declarative identity via preamble gate sentence before resolution bullets | PASS |
| C-26 | Identity sentence names emit (TOPICS.md status line) as the step output | PASS |
| C-27 | S-1 receives tier from S-0 before skill selection | PASS |
| C-28 | "This step emits the TOPICS.md status line" — step = nominative subject, emit = main predicate | PASS |
| C-29–C-43 | No prohibited grammatical forms present in S-0 (no possessive-nominal, no artifact-as-subject, no modal, no lifecycle replacement) | PASS |

---

## Variable Criteria: CONSTRAINT Axis (C-15, C-21, C-24, C-44, C-45, C-46, C-47)

---

### V-01 — Step-IDs-only CONSTRAINT

```
CONSTRAINT: Do not perform S-1, S-2, S-3.1, S-3.2, or S-3.3 until this step's emit is written.
```

| Criterion | Evidence | Verdict | Pts |
|-----------|----------|---------|-----|
| C-15 | "S-1, S-2, S-3.1, S-3.2, S-3.3" are step IDs, not operation type names; 0 types present | FAIL | −2 |
| C-21 | 0 types < 4 threshold | FAIL | −2 |
| C-24 | 0 types < 5 threshold | FAIL | −2 |
| C-44 | Step IDs present; zero per-ID annotations anywhere | FAIL | −2 |
| C-45 | S-3.1, S-3.2, S-3.3 are separately enumerated entries | PASS | 0 |
| C-46 | No trailing clause present (zero types, no "Operations blocked:" sentence) — step-IDs-only form → C-46 passes by default | PASS | 0 |
| C-47 | C-45 passes; no cascade to adjudicate. C-44 scope: all named IDs (S-1, S-2, S-3.1, S-3.2, S-3.3) unannotated → C-44 correctly fails | PASS | 0 |

**Failures: C-15, C-21, C-24, C-44 → −8 pts**
**Computed score: 158 − 8 = 150/158**
**Hypothesis: 148/158**

> **Discrepancy note (+2):** Four aspirational criteria × 2 pts = 8 pts lost → 150/158 by rubric arithmetic. The stated hypothesis of 148/158 implies a 5th failing criterion (−2 additional). No fifth criterion is identifiable from rubric analysis; V-01 passes C-45, C-46, and C-47 cleanly. Scoring: **150/158** (hypothesis may carry a 2-pt arithmetic error from earlier round accumulation).

---

### V-02 — Trailing-Group CONSTRAINT

```
CONSTRAINT: Do not perform S-1, S-2, S-3.1, S-3.2, or S-3.3 until this step's emit is written.
Operations blocked: skill selection, category lookup, carry, compliance detection, flag computation.
```

| Criterion | Evidence | Verdict | Pts |
|-----------|----------|---------|-----|
| C-15 | Five operation types named in block: skill selection, category lookup, carry, compliance detection, flag computation ≥ 3 | PASS | 0 |
| C-21 | 5 types ≥ 4 | PASS | 0 |
| C-24 | 5 types ≥ 5 | PASS | 0 |
| C-44 | Types present but isolated in trailing "Operations blocked:" sentence — not co-located per step ID | FAIL | −2 |
| C-45 | S-3.1, S-3.2, S-3.3 separately enumerated in step-ID clause | PASS | 0 |
| C-46 | "Operations blocked: skill selection, category lookup, carry, compliance detection, flag computation." is the canonical trailing-group form — type names in distinct trailing clause | FAIL | −2 |
| C-47 | C-45 passes; no cascade. C-44 fires correctly for trailing-group (types not per-ID); C-46 co-fires correctly | PASS | 0 |

**Failures: C-44, C-46 → −4 pts**
**Computed score: 158 − 4 = 154/158** ✓ matches hypothesis

---

### V-03 — Collapsed S-3 with Per-ID Annotations

```
CONSTRAINT: Do not perform S-1 (skill selection), S-2 (category lookup), or S-3 (flag computation) until this step's emit is written.
```

| Criterion | Evidence | Verdict | Pts |
|-----------|----------|---------|-----|
| C-15 | 3 types named (skill selection, category lookup, flag computation) ≥ 3 floor | PASS | 0 |
| C-21 | C-45 cascade: S-3 collapse removes carry (S-3.1) and compliance detection (S-3.2) → 3 types < 4 | FAIL | −2 |
| C-24 | Cascade: 3 types < 5 | FAIL | −2 |
| C-44 | S-1 (skill selection), S-2 (category lookup), S-3 (flag computation): each named ID has adjacent parenthetical annotation. C-47 scope rule: evaluates named IDs only — S-3.1/S-3.2 absence is C-45 scope, not C-44 scope | PASS | 0 |
| C-45 | S-3 collapsed to single entry; S-3.1 (carry) and S-3.2 (compliance detection) are not separately enumerated | FAIL | −2 |
| C-46 | Per-ID annotation form; no trailing group clause present | PASS | 0 |
| C-47 | Rule 1 (scope boundary): C-44 correctly passes — named IDs annotated, absent sub-steps not penalized. Rule 2 (cascade): C-45 FAIL reduces count 5→3; C-21 FAIL + C-24 FAIL predicted; C-15 survives at floor 3. Propagation table explicitly annotates collapsed sub-steps as "S-3 (collapsed -- S-3.X sub-step not named)" making cascade unambiguous | PASS | 0 |

**Failures: C-45, C-21 (cascade), C-24 (cascade) → −6 pts**
**Computed score: 158 − 6 = 152/158** ✓ matches hypothesis

---

### V-04 — Em-Dash Per-ID CONSTRAINT

```
CONSTRAINT: Do not perform S-1 -- skill selection, S-2 -- category lookup, S-3.1 -- carry, S-3.2 -- compliance detection, or S-3.3 -- flag computation until this step's emit is written.
```

| Criterion | Evidence | Verdict | Pts |
|-----------|----------|---------|-----|
| C-15 | 5 types named (skill selection, category lookup, carry, compliance detection, flag computation) ≥ 3 | PASS | 0 |
| C-21 | 5 ≥ 4 | PASS | 0 |
| C-24 | 5 ≥ 5 | PASS | 0 |
| C-44 | "S-1 -- skill selection": em-dash separator places annotation immediately adjacent to step ID in same clause segment. Punctuation-flexibility rule (R17 V-04): adjacency satisfied, form accepted | PASS | 0 |
| C-45 | S-3.1 -- carry, S-3.2 -- compliance detection, S-3.3 -- flag computation: all three sub-steps separately enumerated with individual annotations | PASS | 0 |
| C-46 | No trailing group clause; all type names are inline per-ID | PASS | 0 |
| C-47 | C-45 passes (no cascade); golden 5-type per-ID form (no ambiguity) | PASS | 0 |

**Failures: none → 0 pts lost**
**Computed score: 158/158** ✓ matches hypothesis

---

### V-05 — Golden Parenthetical CONSTRAINT

```
CONSTRAINT: Do not perform S-1 (skill selection), S-2 (category lookup), S-3.1 (carry), S-3.2 (compliance detection), or S-3.3 (flag computation) until this step's emit is written.
```

| Criterion | Evidence | Verdict | Pts |
|-----------|----------|---------|-----|
| C-15 | 5 types ≥ 3 | PASS | 0 |
| C-21 | 5 ≥ 4 | PASS | 0 |
| C-24 | 5 ≥ 5 | PASS | 0 |
| C-44 | "S-3.1 (carry)": canonical per-ID parenthetical form; each of the five step IDs immediately followed by inline annotation | PASS | 0 |
| C-45 | S-3.1, S-3.2, S-3.3 listed as distinct entries with distinct annotations | PASS | 0 |
| C-46 | No trailing group; per-ID form throughout | PASS | 0 |
| C-47 | C-45 passes; golden form; no ambiguity | PASS | 0 |

**Failures: none → 0 pts lost**
**Computed score: 158/158** ✓ matches hypothesis

---

## Composite Scores and Ranking

| Rank | Variation | Fails | Score | vs Hypothesis |
|------|-----------|-------|-------|---------------|
| 1 (tie) | **V-04** (em-dash per-ID) | — | **158/158** | ✓ |
| 1 (tie) | **V-05** (golden parenthetical) | — | **158/158** | ✓ |
| 3 | V-02 (trailing-group) | C-44, C-46 | **154/158** | ✓ |
| 4 | V-03 (collapsed S-3 + per-ID) | C-45, C-21↓, C-24↓ | **152/158** | ✓ |
| 5 | V-01 (step-IDs-only) | C-15, C-21, C-24, C-44 | **150/158** | ≠ (hypothesis: 148) |

**V-01 discrepancy:** Rubric arithmetic yields 150/158 (4 criteria × 2 pts = −8). Hypothesis states 148/158 (−10). No 5th failing criterion is identifiable from rubric analysis. The 2-pt offset likely traces to prior round accumulation in the confirmation table. Scoring 150/158.

---

## Excellence Signals (V-04 / V-05 — 158/158)

Three patterns differentiate the top-scoring variations from all intermediate forms:

**1. Per-ID inline annotation for every step ID**
Each step ID in the CONSTRAINT prohibition clause is immediately followed by its operation type name — no aggregation, no separation. The annotation is adjacent to the step ID it describes. This satisfies C-44 regardless of punctuation form.

**2. Sub-step granularity preserved**
S-3 sub-steps are individually enumerated as S-3.1 (carry), S-3.2 (compliance detection), S-3.3 (flag computation). This satisfies C-45 and prevents the type-count cascade. Without this, C-21 and C-24 fail via deterministic 5→3 reduction.

**3. Punctuation-flexible adjacency (V-04 distinguishing signal)**
V-04 confirms that em-dash (`--`) is structurally equivalent to parenthetical (`()`) for C-44: the requirement is adjacency and co-location, not punctuation form. This opens a family of CONSTRAINT forms: any separator that places the annotation in the same clause segment as the step ID satisfies the criterion.

**What trailing-group (V-02) almost got right:** All five operation types named, all sub-steps enumerated — type-count criteria pass. But aggregating types into a trailing sentence instead of distributing them per-ID costs both C-44 and C-46. The defect is structural co-location, not completeness.

---

```json
{"top_score": 158, "all_essential_pass": true, "new_patterns": []}
```
