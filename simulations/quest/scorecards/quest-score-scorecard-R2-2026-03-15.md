## quest-score Round 2 — Scorecard

### Rubric Derivation

```
Active rubric: quest-score-rubric-v2-2026-03-15.md
Essential criteria:    C-01, C-02, C-03, C-04, C-05   → E_count = 5
Recommended criteria:  C-06, C-07, C-08               → R_count = 3
Aspirational criteria: C-09, C-10, C-11, C-12         → A_count = 4

Composite formula (symbolic):
composite = (essential_pass / E_count * 60)
          + (recommended_pass / R_count * 30)
          + (aspirational_pass / A_count * 10)

Scoring: PASS = 1.0, PARTIAL = 0.5 (Essential and Recommended tiers only)
         Aspirational PARTIAL counts as 0.0 (binary)
Golden threshold: all 5 essentials PASS AND composite >= 80
```

---

## V-01 — Rubric-derivation-first (Axis A)

#### Verdict Matrix

| ID | Criterion | Tier | Verdict | Evidence |
|----|-----------|------|---------|----------|
| C-01 | Complete verdict matrix | Essential | PASS | Phase 3: "one row per criterion from the active rubric; No criterion row may be blank or absent; a table that omits criteria added in the current rubric version is FAIL on C-01" — explicit completeness gate tied to current rubric |
| C-02 | Evidence per verdict | Essential | PASS | Phase 3 evidence rules: "must name a specific structural element, section title, field label, template pattern, or direct quote"; criterion restatements explicitly excluded by name |
| C-03 | Formula-correct composite | Essential | PASS | Phase 4 Composite Scores block uses `[essential_pass] / E_count × 60` — symbolic, not literal; Phase 1 derivation provides the variable values |
| C-04 | Ranked leaderboard | Essential | PASS | Phase 4 "Ranked Leaderboard" section: standalone required section, descending by composite, tie-breaking by essential_pass count then output ID alphabetically |
| C-05 | Failure patterns identified | Essential | PASS | Phase 4 "Failure Patterns" required section; Pattern/Diagnosis/Rationale template; explicit fallback: "No universal failures detected" |
| C-06 | Excellence signals | Recommended | PASS | Phase 4 "Excellence Signals" required section; explicit fallback: "No excellence signals detected in this scoring run" |
| C-07 | Regression signals | Recommended | PASS | Phase 4 "Regression Signals" required section; explicit no-prior-data fallback stated verbatim |
| C-08 | Per-output summary note | Recommended | PASS | Phase 3: "After the table: 1-3 sentence summary note naming this output's primary differentiator or primary miss... Name the structural feature — not just the score" — explicitly prohibits score restatement |
| C-09 | Golden threshold declaration | Aspirational | PASS | Phase 4 Composite Scores: `Golden: YES` / `Golden: NO — [specific failing condition]` per-output required field; field is labeled and explicit, not inferred from the score table |
| C-10 | Failure-pattern root-cause diagnosis | Aspirational | PASS | Failure Patterns template includes `Diagnosis: [rubric gap \| skill design issue]` + `Rationale: [one sentence]`; if no failures, vacuously PASS |
| C-11 | Rubric-adaptive formula derivation | Aspirational | PASS | Phase 1 DERIVE gate forces E_count/R_count/A_count before any output is opened; explicit instruction: "Do not substitute E_count, R_count, A_count with their resolved numeric values in the Composite formula line"; Phase 4 reinforces: "use E_count, R_count, A_count as named variables — do not re-embed their resolved values" |
| C-12 | Structured diagnosis template | Aspirational | PASS | Phase 4: "Apply this template to every universal failure. Do not write prose in place of the template." Template enforces Pattern/Diagnosis/Rationale in consistent order; if no failures, vacuously PASS |

**Summary Note:** V-01's primary differentiator is the DERIVE phase gate (Phase 1) — the only way to write `[DERIVE COMPLETE]` is to first produce the derivation block with explicit E_count/R_count/A_count and symbolic formula. The phase gate creates a structural checkpoint that makes literal formula embedding visible as a skip, not just an instruction violation. The Golden field appears in Phase 4 synthesis rather than Phase 3 output blocks, which is the primary structural gap relative to V-02/V-04/V-05.

#### Composite
Formula: (essential_pass / E_count * 60) + (recommended_pass / R_count * 30) + (aspirational_pass / A_count * 10)
  [E_count=5, R_count=3, A_count=4 from derivation above]
Essential:    5 PASS = 5.0 / E_count × 60 = 60.0
Recommended:  3 PASS = 3.0 / R_count × 30 = 30.0
Aspirational: 4 PASS = 4.0 / A_count × 10 = 10.0
Composite: **100**

Golden: YES

---

## V-02 — Labeled-field slots (Axis B)

#### Verdict Matrix

| ID | Criterion | Tier | Verdict | Evidence |
|----|-----------|------|---------|----------|
| C-01 | Complete verdict matrix | Essential | PASS | Step 2: "one row per criterion from the active rubric; no row may be blank or absent" — completeness gate on the active rubric's full list |
| C-02 | Evidence per verdict | Essential | PASS | Step 2 evidence rule in the verdict matrix block: "evidence must name a specific structural element, section title, field label, or direct quote from this output. Criterion restatements are not evidence" |
| C-03 | Formula-correct composite | Essential | PASS | Step 2 `#### Composite` block shows formula as `(essential_pass / E_count * 60) + (recommended_pass / R_count * 30) + (aspirational_pass / A_count * 10)` with `where E_count, R_count, A_count as derived in Step 1` — symbolic calculation formula |
| C-04 | Ranked leaderboard | Essential | PASS | Step 3 "Ranked Leaderboard": standalone required section, table format, tie-breaking by essential_pass then output ID |
| C-05 | Failure patterns identified | Essential | PASS | Step 3 "Failure Patterns" required section; template prescribed; fallback "No universal failures detected" |
| C-06 | Excellence signals | Recommended | PASS | Step 3 "Excellence Signals" required section; fallback stated verbatim |
| C-07 | Regression signals | Recommended | PASS | Step 3 "Regression Signals" required section; explicit no-prior-data fallback |
| C-08 | Per-output summary note | Recommended | PASS | Step 2 `#### Summary Note` labeled required field: "1-3 sentences: primary differentiator or primary miss... name the structural feature, not just the score" |
| C-09 | Golden threshold declaration | Aspirational | PASS | Step 2 `#### Golden` labeled required field with instruction "complete exactly one of the following lines — do not leave this field blank or inferred" — strongest placement in the primary output block; unfilled slot is structurally visible |
| C-10 | Failure-pattern root-cause diagnosis | Aspirational | PASS | Step 3 Failure Patterns template includes `Diagnosis: [rubric gap \| skill design issue]` and `Rationale: [one sentence: why...]`; if no failures, vacuously PASS |
| C-11 | Rubric-adaptive formula derivation | Aspirational | **FAIL** | Step 1 derives E_count/R_count/A_count correctly, but the load block template prescribes `Formula: [state composite formula from the rubric]`. The rubric file states its formula with numeric literals (`/5`, `/3`, `/4`). A scorer following this instruction would copy those literals into the Step 1 output, producing a hardcoded formula in the load block. C-11 is binary — even though the Step 2 calculation formula is symbolic, the Step 1 formula section embeds literals, and C-11 requires the mechanism to be correct at all formula sites |
| C-12 | Structured diagnosis template | Aspirational | PASS | Step 3: "Apply the template to every universal failure. Do not write prose for any entry, even if only one failure exists." Pattern/Diagnosis/Rationale in consistent order enforced; vacuously PASS if no failures |

**Summary Note:** V-02's primary strength is C-09 and C-12 structural enforcement — `#### Golden` as a required in-block labeled field (unfilled slot is visible as a gap) and the strongest Failure Patterns prose prohibition ("even if only one failure exists"). Its primary miss is the C-11 mechanism failure in Step 1: `Formula: [state composite formula from the rubric]` copies the rubric's literal formula (`/5, /3, /4`), hardcoding the current rubric's counts into the load block even while the Step 2 calculation correctly uses named variables. The two formula contexts are inconsistent, and C-11 is binary.

#### Composite
Formula: (essential_pass / E_count * 60) + (recommended_pass / R_count * 30) + (aspirational_pass / A_count * 10)
Essential:    5 PASS = 5.0 / E_count × 60 = 60.0
Recommended:  3 PASS = 3.0 / R_count × 30 = 30.0
Aspirational: 3 PASS (C-11 FAIL) = 3.0 / A_count × 10 = 7.5
Composite: **97.5**

Golden: YES — all essentials PASS, composite 97.5 >= 80

---

## V-03 — Formula-hardcoding anti-pattern (Axis C)

#### Verdict Matrix

| ID | Criterion | Tier | Verdict | Evidence |
|----|-----------|------|---------|----------|
| C-01 | Complete verdict matrix | Essential | PASS | Step 2: "one row per criterion from the active rubric. No criterion row may be blank or absent." |
| C-02 | Evidence per verdict | Essential | PASS | Step 2 evidence rules: "must name a specific structural element, section title, field label, template pattern, or direct quote from this output. Do not restate the criterion name as evidence. Do not write evidence that could apply to any well-designed output." Three exclusion rules, not one |
| C-03 | Formula-correct composite | Essential | PASS | Step 3 Composite Scores: `[Output ID]: E=[n]/E_count, R=[n]/R_count, A=[n]/A_count` — symbolic notation in synthesis |
| C-04 | Ranked leaderboard | Essential | PASS | Step 3 "Ranked Leaderboard": standalone required section, table format, explicit tie instruction |
| C-05 | Failure patterns identified | Essential | PASS | Step 3 "Failure Patterns" required section; Pattern/Diagnosis/Rationale template; fallback stated |
| C-06 | Excellence signals | Recommended | PASS | Step 3 "Excellence Signals" required section; fallback stated |
| C-07 | Regression signals | Recommended | PASS | Step 3 "Regression Signals" required section; no-prior-data fallback |
| C-08 | Per-output summary note | Recommended | PASS | Step 2: "After the table: 1-3 sentence summary note identifying this output's primary differentiator or primary miss relative to the other scored outputs" — structural content required by phrasing (differentiator/miss implies mechanism, not score) |
| C-09 | Golden threshold declaration | Aspirational | PASS | Step 3 Composite Scores section: `Golden: YES` / `Golden: NO — [failing condition]` per-output required lines; field is explicit and labeled per output in synthesis, not inferred from a table |
| C-10 | Failure-pattern root-cause diagnosis | Aspirational | PASS | Step 3 Failure Patterns template: `Diagnosis: [rubric gap \| skill design issue]` + `Rationale: [one sentence]`; vacuously PASS if no failures |
| C-11 | Rubric-adaptive formula derivation | Aspirational | PASS | Anti-pattern block fires before any file is opened — shows HARDCODED (`/5, /2, /1` literals) vs CORRECT (`E_count, R_count, A_count` variables); Step 1 derives counts and writes formula symbolically; per-line check: "Before writing any formula line in this run: check whether a numeric literal appears in a denominator position. If it does — replace it." The per-line check is the key enforcement mechanism |
| C-12 | Structured diagnosis template | Aspirational | PASS | Step 3: "Apply the template to every entry. Do not substitute prose." Pattern/Diagnosis/Rationale in consistent order; vacuously PASS if no failures |

**Summary Note:** V-03's differentiator is the pre-load anti-pattern anchor — it fires before Phase 1, making the failure mechanism viscerally visible before any output is opened. The risk the hypothesis identified (scorer reads "wrong v1 counts" not "wrong mechanism") is mitigated by the explicit per-line check ("replace any numeric literal in a denominator position with the named variable") which targets mechanism, not values. V-03 lacks phase gates and EXIT TOKENs, which is the main structural risk for synthesis completeness under context pressure vs V-01/V-04/V-05.

#### Composite
Formula: (essential_pass / E_count * 60) + (recommended_pass / R_count * 30) + (aspirational_pass / A_count * 10)
Essential:    5 PASS = 5.0 / E_count × 60 = 60.0
Recommended:  3 PASS = 3.0 / R_count × 30 = 30.0
Aspirational: 4 PASS = 4.0 / A_count × 10 = 10.0
Composite: **100**

Golden: YES

---

## V-04 — Rubric-derivation-first + labeled-field slots (A+B)

#### Verdict Matrix

| ID | Criterion | Tier | Verdict | Evidence |
|----|-----------|------|---------|----------|
| C-01 | Complete verdict matrix | Essential | PASS | Phase 3: "one row per criterion from the active rubric — no row may be blank or absent" — same gate as V-01; phase gate structure additionally makes omission visible as incomplete phase |
| C-02 | Evidence per verdict | Essential | PASS | Phase 3: "every cell must name a specific structural element, field label, or direct quote from this output. Criterion restatements are not evidence. Generic descriptions that apply to any well-designed output are not evidence." Two distinct exclusion rules |
| C-03 | Formula-correct composite | Essential | PASS | Phase 3 `#### Composite` block: formula stated with E_count/R_count/A_count variables; explicit instruction: "use E_count, R_count, A_count from Phase 1 — do not substitute literals here" |
| C-04 | Ranked leaderboard | Essential | PASS | Phase 4 "Ranked Leaderboard": standalone required section, descending, tie-breaking stated; "Standalone, descending. Ties: state explicitly, break by essential_pass count then output ID" |
| C-05 | Failure patterns identified | Essential | PASS | Phase 4 "Failure Patterns" required section; Pattern/Diagnosis/Rationale template mandated for every entry; fallback stated; "Every entry must have all three fields in this order" |
| C-06 | Excellence signals | Recommended | PASS | Phase 4 "Excellence Signals" required section; fallback stated |
| C-07 | Regression signals | Recommended | PASS | Phase 4 "Regression Signals" required section; no-prior-data fallback stated |
| C-08 | Per-output summary note | Recommended | PASS | Phase 3 `#### Summary Note` labeled required field: "1-3 sentences: primary differentiator or primary miss... name the structural feature that explains this output's relative rank or its most significant gap" |
| C-09 | Golden threshold declaration | Aspirational | PASS | Phase 3 `#### Golden` labeled required field per output block: "complete exactly one of the following — this field is required, not optional" — same in-block enforcement as V-02; unfilled slot structurally visible |
| C-10 | Failure-pattern root-cause diagnosis | Aspirational | PASS | Phase 4 Failure Patterns: `Diagnosis: [rubric gap \| skill design issue]` + `Rationale:` in template; vacuously PASS if no failures |
| C-11 | Rubric-adaptive formula derivation | Aspirational | PASS | Phase 1 DERIVE gate: E_count/R_count/A_count derived explicitly; formula is symbolic; instruction: "E_count, R_count, A_count are resolved above the formula; they must not be substituted into the formula line itself." Phase 3 reinforces: "do not substitute literals here" — two enforcement points vs V-01's one |
| C-12 | Structured diagnosis template | Aspirational | PASS | Phase 4: "Every entry must have all three fields in this order. Prose without these labels is FAIL regardless of content quality." — strongest C-12 enforcement language of any variation |

**Summary Note:** V-04 is the strongest combination variation short of V-05 — it contributes DERIVE gate enforcement from V-01 (C-11) and labeled-slot enforcement from V-02 (C-09, C-12), while avoiding V-02's C-11 failure because the DERIVE phase gate forces symbolic formula before the load phase. The explicit Phase 3 instruction "do not substitute literals here" provides a second enforcement point for C-11 absent from V-01. C-12 enforcement language ("Prose without these labels is FAIL") is the most explicit of any variation.

#### Composite
Formula: (essential_pass / E_count * 60) + (recommended_pass / R_count * 30) + (aspirational_pass / A_count * 10)
Essential:    5 PASS = 5.0 / E_count × 60 = 60.0
Recommended:  3 PASS = 3.0 / R_count × 30 = 30.0
Aspirational: 4 PASS = 4.0 / A_count × 10 = 10.0
Composite: **100**

Golden: YES

---

## V-05 — Rubric-derivation-first + labeled-field slots + formula anti-pattern (A+B+C)

#### Verdict Matrix

| ID | Criterion | Tier | Verdict | Evidence |
|----|-----------|------|---------|----------|
| C-01 | Complete verdict matrix | Essential | PASS | Phase 3: "one row per criterion from the active rubric — no row may be blank or absent"; phase manifest with EXIT TOKEN makes omission visible as incomplete phase |
| C-02 | Evidence per verdict | Essential | PASS | Phase 3: "evidence must name a specific structural element, section title, field label, template pattern, or direct quote from this output. Criterion restatements are not evidence. Generic observations that apply to any output are not evidence." — three exclusion rules |
| C-03 | Formula-correct composite | Essential | PASS | Phase 3 `#### Composite` block: "E_count, R_count, A_count from Phase 1; do not substitute their numeric values here"; per-block check: "scan the formula line for numeric literals in denominator positions. If present — replace with E_count, R_count, A_count" |
| C-04 | Ranked leaderboard | Essential | PASS | Phase 4 "Ranked Leaderboard": standalone table, descending, explicit tie instruction, pre-synthesis check references "leaderboard is a standalone explicit list (not a pointer to score blocks)" |
| C-05 | Failure patterns identified | Essential | PASS | Phase 4 "Failure Patterns" required section; Pattern/Diagnosis/Rationale template; pre-synthesis check: "Every universal failure has Pattern:, Diagnosis:, and Rationale: fields in that order. No entry is prose-only." |
| C-06 | Excellence signals | Recommended | PASS | Phase 4 "Excellence Signals" required section; fallback stated |
| C-07 | Regression signals | Recommended | PASS | Phase 4 "Regression Signals" required section; no-prior-data fallback stated |
| C-08 | Per-output summary note | Recommended | PASS | Phase 3 `#### Summary Note` labeled required field: "1-3 sentences: primary differentiator or primary miss; name the structural feature that explains this output's relative rank or its most significant structural gap" |
| C-09 | Golden threshold declaration | Aspirational | PASS | Phase 3 `#### Golden` labeled required field per output block: "complete exactly one of the following lines — this field is required, not optional"; same in-block placement as V-02/V-04 |
| C-10 | Failure-pattern root-cause diagnosis | Aspirational | PASS | Phase 4 Failure Patterns template: `Diagnosis: [rubric gap \| skill design issue]`; pre-synthesis check requires `Diagnosis:` field in every entry; vacuously PASS if no failures |
| C-11 | Rubric-adaptive formula derivation | Aspirational | PASS | Three checkpoints at distinct lifecycle stages: (1) anti-pattern anchor fires before Phase 1 — shows HARDCODED vs CORRECT with explicit "C-11 fails even when literals happen to match"; (2) DERIVE phase gate with formula scan before writing `[DERIVE COMPLETE]`; (3) Phase 3 per-block scan "before writing each `#### Composite` block" — most comprehensive C-11 enforcement of any variation |
| C-12 | Structured diagnosis template | Aspirational | PASS | Phase 4 pre-synthesis check: "Every universal failure has Pattern:, Diagnosis:, and Rationale: fields in that order. No entry is prose-only. Even a single failure entry must use the template." — both the template and a pre-synthesis verification gate |

**Summary Note:** V-05's primary differentiator is defense-in-depth on C-11 — the anti-pattern anchor fires before Phase 1 (preventing first-write literal embedding), the DERIVE gate fires in Phase 1 (forcing derivation before any output is opened), and the per-block scan fires in Phase 3 (catching any literal that survived earlier checkpoints). No single point of failure can allow hardcoded literals through. V-05 also carries the pre-synthesis check for both C-11 and C-12, making verification explicit before `[SYNTHESIS COMPLETE]` is written.

#### Composite
Formula: (essential_pass / E_count * 60) + (recommended_pass / R_count * 30) + (aspirational_pass / A_count * 10)
Essential:    5 PASS = 5.0 / E_count × 60 = 60.0
Recommended:  3 PASS = 3.0 / R_count × 30 = 30.0
Aspirational: 4 PASS = 4.0 / A_count × 10 = 10.0
Composite: **100**

Golden: YES

---

## Synthesis

### Ranked Leaderboard

| Rank | Output | Composite | Golden |
|------|--------|-----------|--------|
| 1 (tie) | V-01 | 100 | YES |
| 1 (tie) | V-03 | 100 | YES |
| 1 (tie) | V-04 | 100 | YES |
| 1 (tie) | V-05 | 100 | YES |
| 5 | V-02 | 97.5 | YES |

_Tie at rank 1: V-01/V-03/V-04/V-05 all achieve essential_pass=5, composite=100. Tiebreaker: output ID alphabetically._

---

### Excellence Signals

**V-05 on C-11:** V-05 is the only variation with three independent C-11 checkpoints at distinct lifecycle stages — pre-load anti-pattern (fires before Phase 1), DERIVE gate with formula scan (Phase 1), and per-block scan (Phase 3). The structural mechanism: each checkpoint targets a different failure mode (first-write hardcoding, derivation skip, and re-substitution of resolved values), so no single contextual slip allows literals through. V-01/V-04 have one DERIVE gate; V-03 has one per-line check; V-05 has both plus the anti-pattern anchor.

**V-02/V-04/V-05 on C-09:** `#### Golden` as a required labeled field inside Phase 3/Step 2 output blocks — unfilled slot is structurally visible as a gap at output-block level. V-01 and V-03 produce the Golden field only in synthesis sections; a model under context pressure could complete Phase 3 output blocks, run out of tokens during Phase 4, and produce incomplete Golden coverage. In-block placement removes this timing dependency.

**V-04/V-05 on C-12:** The Failure Patterns enforcement language "Prose without these labels is FAIL regardless of content quality" is explicitly stated as a consequence, not just a mandate. This framing closes the failure mode where a scorer produces high-quality diagnosis in prose format and considers it sufficient — it names the quality dimension that doesn't rescue a structural violation.

---

### Regression Signals

No prior round data — regression analysis cannot be performed. (R1 scored against rubric v1; rubric v2 added C-09 through C-12, making direct criterion-level comparison structurally incompatible.)

---

### Failure Patterns

No universal failures detected. C-11 failed in V-02 only (4/5 variations PASS). No criterion received zero PASS across all 5 scored variations.

_Note: V-02's C-11 failure is a near-miss pattern worth tracking. The `Formula: [state composite formula from the rubric]` instruction in Step 1 produces a literal formula (copied from the rubric's own formula line which contains `/5, /3, /4`) while the Step 2 calculation correctly uses named variables. The two formula contexts are inconsistent — derivation fires in Step 1 for the counts, but not for the formula expression itself._

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Formula extraction placeholder 'state composite formula from the rubric' copies rubric literals into the load block even when counts are derived separately — formula statement and symbolic derivation must be colocated in the same instruction context", "Multi-checkpoint C-11 enforcement (anti-pattern pre-load + derivation gate Phase 1 + per-block scan Phase 3) provides defense-in-depth: each checkpoint targets a distinct failure mode so no single contextual slip allows literal denominators through to any formula site"]}
```
