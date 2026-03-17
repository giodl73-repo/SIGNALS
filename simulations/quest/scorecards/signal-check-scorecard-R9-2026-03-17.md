## Signal-Check R9 — Score Complete

**Top scores: V-04 and V-05 at 100/Gold. V-01 and V-02 at 99.44. V-03 at 98.89.**

| V | Score | C-24 | C-25 | C-26 | Gold? |
|---|-------|------|------|------|-------|
| V-01 | 99.44 | baseline (B,D) | PASS | **FAIL** | NO |
| V-02 | 99.44 | baseline (B,D) | **FAIL** | PASS | NO |
| V-03 | 98.89 | extended (B,C,D) | **FAIL** | **FAIL** | NO |
| V-04 | **100** | extended (B,C,D) | PASS | PASS | YES |
| V-05 | **100** | extended (B,C,D) | PASS | PASS | YES |

---

**Key findings from the single-axis isolations:**

**RQ1 (C-25 ARCHITECTURE table):** YES — table form satisfies C-25 with lower overhead than schema form. Three-column table (Named Output | Produced by | Consumed by) is independently scannable and sufficient for pre-execution auditability. C-25 and C-26 are complementary, not substitutable: table makes the contract visible upfront; prohibition enforces it at execution time. V-01 confirms you can have one without the other and still fail.

**RQ2 (C-26 per-site prohibition):** YES — per-site prohibition closes silent re-derivation that structural label consumption alone doesn't catch. A model can "mention" a label while re-inferring from prose; the marker makes that a locally visible violation. V-05's per-input form (separate annotation per named input) is stronger than per-step grouped — partial compliance per input becomes impossible.

**RQ3 (C-24 extended to STEP C):** YES — closes a structural gap STEP B/D cannot address. STEP C dimension coaching can characterize cross-dimension relationships without naming the Root pattern label; the per-dimension contribution note makes divergence from STEP 3 synthesis visible at the dimension level. Low overhead: one line per dimension.

**Three excellence signals:**
1. Table-form ARCHITECTURE is the minimal C-25 implementation for advisory register
2. Per-input prohibition is the strongest C-26 form (V-05 over V-04/V-02)
3. All three R9 axes are register-agnostic — V-04 (advisory) and V-05 (imperative) both reach 100

**R10 direction:** All three axes now locked (denominator stays 18). Candidate: should per-dimension Root pattern contribution notes in STEP C emit a named binary (`STEP C drift: CLOSED/OPEN`) consumable by STEP D, completing the structural chain from dimension coaching back to confirmed readiness?

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Table-form ARCHITECTURE (Named Output | Produced by | Consumed by) satisfies C-25 with lower overhead than schema form on the advisory register — three-column table delivers pre-execution auditability and independent scannability without per-step enumeration of consuming relationships", "Per-input C-26 prohibition (separate annotation per named input at consuming step) is stronger than per-step grouped notation — makes partial compliance impossible by requiring each specific named input reference to carry the prohibition independently", "Three R9 axes (C-24 extended, C-25, C-26) are structurally complementary and register-agnostic: C-25 delivers pre-execution auditability, C-26 delivers execution-time enforcement, C-24 extended closes STEP C dimension-coaching drift; combination reaches 100 on both advisory and imperative registers"]}
```
SS | PASS | PASS | PASS |
| C-23 | Named binary outputs consumed by label in STEP 3 and PART 2 | PASS | PASS | PASS | PASS | PASS |
| C-24 | STEP 3 named root-pattern label consumed by PART 2 | PASS | PASS | PASS | PASS | PASS |
| C-25 | Upfront ARCHITECTURE block declares all outputs + consuming steps | PASS | **FAIL** | **FAIL** | PASS | PASS |
| C-26 | Consuming steps carry "do not re-derive" prohibition per named input | **FAIL** | PASS | **FAIL** | PASS | PASS |

**Aspirational pass counts**: V-01: 17/18 · V-02: 17/18 · V-03: 16/18 · V-04: 18/18 · V-05: 18/18

---

## Composite Scores

Formula: `(essential/5 × 60) + (recommended/3 × 30) + (aspirational/18 × 10)`

| V | Essential | Recommended | Aspirational | Composite | Gold? |
|---|-----------|-------------|--------------|-----------|-------|
| V-01 | 60 | 30 | 9.44 (17/18) | **99.44** | NO |
| V-02 | 60 | 30 | 9.44 (17/18) | **99.44** | NO |
| V-03 | 60 | 30 | 8.89 (16/18) | **98.89** | NO |
| V-04 | 60 | 30 | 10.00 (18/18) | **100** | YES |
| V-05 | 60 | 30 | 10.00 (18/18) | **100** | YES |

---

## Criterion Evidence Notes

### C-24 — STEP 3 named root-pattern label consumed by PART 2

All five variations have the C-24 baseline: STEP 3 emits `Root pattern: [SHORT NAME]`; STEP B and STEP D consume by label.

V-03/V-04/V-05 extend into STEP C per-dimension: each dimension coaching observation includes a "Root pattern contribution:" note that references the label by name and states whether the dimension contributed to the named root or is an isolated flag. This closes a structural gap: STEP B and STEP D consumption prevents PART 2 summary drift from STEP 3, but STEP C dimension coaching could still independently characterize cross-dimension relationships without consuming the label. The per-dimension contribution note closes that gap.

### C-25 — Upfront ARCHITECTURE block

**V-01 (PASS)**: Table-form ARCHITECTURE block placed before PART 1. Three columns: Named Output | Produced by | Consumed by. Lists all five named outputs with correct consuming steps for V-01's scope (Root pattern: STEP B and STEP D only — baseline C-24). Table accurately reflects the actual pipeline, is independently scannable, and appears before analysis runs. Satisfies C-25 with lower overhead than schema form.

**V-02 (FAIL)**: No ARCHITECTURE block. Per-site prohibition markers are present at each consumption site but there is no upfront declaration of the pipeline. A reader must trace through the full prompt to verify compliance — the dataflow contract is distributed, not front-loaded.

**V-03 (FAIL)**: No ARCHITECTURE block. C-24 extension is noted in the "Locked structural features" instruction block (items 8 and 9), not in a named ARCHITECTURE declaration with consuming-step enumeration. Instruction does not substitute for upfront contract.

**V-04 (PASS)**: Table-form ARCHITECTURE with extended Root pattern row: `| Root pattern: [label] | STEP 3 | PART 2 STEP B (by name); STEP C per-dimension (by name); STEP D (by name) |` — accurately reflects extended C-24 scope.

**V-05 (PASS)**: Schema-form ARCHITECTURE. "step C: Root pattern (all four per-dimension contribution notes)" makes per-dimension consumption explicit. More detailed than V-04's table; highest overhead but most precisely specified.

### C-26 — "Required input — do not re-derive" prohibition per named input

**V-01 (FAIL)**: Arrow notation at production sites (`<- SEQUENCE quotes this line verbatim below`) but no "do not re-derive" prohibition at consuming sites. The ARCHITECTURE table carries "Consuming steps reference named outputs by the exact label in the table above" — a table-level instruction, not a per-site inline prohibition. C-26 requires the annotation on the consuming step itself.

**V-02 (PASS)**: "Required input — do not re-derive:" at every consuming step. STEP 3: "Required inputs — consume by label, do not re-derive from prose." PART 2 steps each carry the marker. All consuming relationships have per-site prohibition.

**V-03 (FAIL)**: No prohibition markers. STEP 3 says "Consume named outputs by label — do not re-derive" as a single instructional clause, not per-input annotations. STEP C uses label-reference instructions but no "do not re-derive" marker at each consumption site.

**V-04 (PASS)**: Per-site prohibition at every consuming step. Production site arrows carry "Required input — do not re-derive. Quote verbatim." STEP 3, PART 2 STEP B, STEP C per-dimension all carry per-site annotations. Full per-site coverage on advisory register.

**V-05 (PASS, strengthened)**: Per-input prohibition — separate annotation for each named input at every consuming step. ARCHITECTURE pre-declares the requirement. STEP C carries individual "Required input — do not re-derive: Pre-specification gap" and "Required input — do not re-derive: Root pattern" as independent annotations rather than a grouped list. Strongest C-26 implementation: partial compliance per input is impossible.

---

## Research Question Findings

### RQ1: Does the ARCHITECTURE table improve named-output consumption consistency over per-step label arrows?

**YES — table satisfies C-25 with significantly lower overhead than schema form.**

V-01 and V-04 demonstrate that a three-column table delivers C-25 compliance on the advisory register: pipeline is front-loaded, independently scannable, and accurate to the variation's scope. The table does more than help auditors — it makes the contract explicit before analysis runs so that missing consumption sites are visible without reading the full prompt.

V-05's schema form is more detailed (consuming steps listed per input rather than per output row) and is more precisely aligned with the consuming-step perspective. Both satisfy C-25. For advisory-register prompts, table form is preferred — comparable auditability, lower overhead.

V-02 and V-03 (no ARCHITECTURE block) fail C-25: the dataflow contract exists implicitly in per-step instructions but cannot be verified without tracing the full analytical chain.

### RQ2: Does per-site prohibition close silent re-derivation that structural label consumption does not catch?

**YES — prohibition makes re-derivation a locally visible violation, which structural consumption alone does not.**

V-02 demonstrates that per-site prohibition without an ARCHITECTURE block still produces C-26 compliance. The critical difference: a model can "mention" a label while re-inferring the conclusion from prose; the prohibition marker makes that a local inspectable violation rather than an undetectable judgment call.

V-01 shows the complementary gap: ARCHITECTURE without per-site prohibition (C-25 PASS, C-26 FAIL). The table makes consumption relationships visible upfront but does not prevent re-derivation at execution time. C-25 and C-26 address different failure modes: C-25 ensures pre-execution auditability; C-26 ensures execution-time enforcement. They are complementary, not substitutable.

V-05's per-input prohibition (vs. V-04/V-02's per-step grouped notation) is the strongest form: each individual input reference carries the annotation independently, so a step cannot appear C-26-compliant at the step level while re-deriving one of its named inputs.

### RQ3: Does Root pattern consumption extended into STEP C per-dimension close drift between PART 1 synthesis and individual dimension coaching?

**YES — and it closes a structural gap that STEP B/D consumption cannot address.**

STEP B and STEP D (C-24 baseline) prevent PART 2 summary and confirmation from re-inferring the cross-dimension pattern. But STEP C dimension coaching is structurally unconnected to the root pattern: each dimension observation can characterize cross-dimension relationships in advisory prose without naming the STEP 3 Root pattern label.

The per-dimension "Root pattern contribution:" note in V-03/V-04/V-05 closes this: each dimension coaching observation explicitly states — by the Root pattern label — whether the dimension contributed to the named root or is an isolated flag. STEP C cannot produce a cross-dimension characterization that diverges from STEP 3 synthesis without the divergence being visible in the label reference.

Design note: the extension adds roughly one line per dimension in STEP C — low overhead for a genuine drift-closing gain. V-04 implements it with per-site prohibition; V-05 with per-input prohibition; V-03 without either.

---

## Variation Analysis

### V-01 — Single Axis: C-25 ARCHITECTURE Table

**Finding**: Table-form ARCHITECTURE satisfies C-25 on the advisory register. The table is independently scannable, accurately reflects the V-01 pipeline, and appears before analysis runs. C-25 PASS. No per-site prohibition (C-26 FAIL) — confirming the two criteria are complementary.

**Score**: 99.44

---

### V-02 — Single Axis: C-26 Per-Site Prohibition

**Finding**: C-26 PASS — per-site markers at every consuming step are sufficient for the criterion. C-25 FAIL — without the upfront contract, a reader cannot verify the full pipeline without tracing the prompt. Confirms C-25 and C-26 address different failure modes.

**Score**: 99.44

---

### V-03 — Single Axis: C-24 Extended to STEP C Per-Dimension

**Finding**: Structural STEP C drift gap confirmed closed — each dimension observation carries a Root pattern contribution note. But without C-25 (no ARCHITECTURE block) and C-26 (no prohibition markers), two of three new R9 criteria fail. C-24 extension adds genuine value but is insufficient alone for 100.

**Score**: 98.89

---

### V-04 — All Three Combined, Advisory Register

**Finding**: All 18 aspirational criteria PASS. Table-form ARCHITECTURE makes pipeline scannable; per-site prohibition enforces consumption at execution; per-dimension Root pattern contribution closes STEP C drift. Full structural lock achieved on advisory register with lower overhead than V-05.

**Score**: 100/Gold

---

### V-05 — All Three Combined, Imperative Register

**Finding**: All 18 aspirational criteria PASS. Strongest individual-criterion implementations: per-input C-26 makes each named input reference independently prohibited; ARCHITECTURE schema lists consuming steps per input rather than per output row. Highest overhead variation but maximum structural precision.

**Score**: 100/Gold

---

## Excellence Signals

### EX-01: Table-Form ARCHITECTURE as Minimal C-25 Implementation

V-01/V-04 demonstrate that a three-column table (Named Output | Produced by | Consumed by) is sufficient to satisfy C-25 on the advisory register. Lower overhead than schema form with equivalent pre-execution auditability. Recommended for advisory-register prompt designs.

### EX-02: Per-Input Prohibition as Strongest C-26 Form

V-05's per-input annotation (separate "Required input — do not re-derive: [label]" for each named input at a consuming step) is stronger than V-02/V-04's per-step grouped notation. Per-input makes partial compliance impossible: a step cannot appear compliant at the step level while one of its inputs lacks the prohibition. Preferred for imperative-register prompts.

### EX-03: Three R9 Axes are Complementary, Not Redundant

Single-axis failures (V-01, V-02, V-03) confirm each axis addresses a distinct structural gap:
- C-25 (ARCHITECTURE): pre-execution auditability — contract visible before analysis runs
- C-26 (prohibition): execution-time enforcement — re-derivation is a local visible violation
- C-24 extended (per-dimension): STEP C drift closure — dimension coaching cannot diverge from synthesis without a visible label mismatch

The combination is register-agnostic: V-04 (advisory) and V-05 (imperative) both reach 100.

---

## Round Result

- **Top score**: 100 (V-04 and V-05)
- **All essential pass**: YES (all five)
- **Ranking**:
  1. V-05 — per-input C-26 + schema C-25 + extended C-24 (imperative, highest precision)
  2. V-04 — per-site C-26 + table C-25 + extended C-24 (advisory, best overhead/coverage ratio)
  3. V-01 — table C-25 alone; C-26 absent; confirms table is necessary but not sufficient
  4. V-02 — per-site C-26 alone; C-25 absent; confirms prohibition is necessary but not sufficient
  5. V-03 — extended C-24 alone; both C-25 and C-26 absent; closes STEP C drift but leaves pipeline non-auditable and non-enforced
- **Recommended for golden**: V-04 (complete coverage, advisory register, lower overhead)
- **R10 direction**: All three R9 axes now locked as C-24, C-25, C-26 (denominator 18). Single-axis variations scored below 100 for the first time since R7 — rubric is discriminating at the new criteria. R10 candidate: whether per-dimension Root pattern contribution notes in STEP C should emit a named binary (e.g., `STEP C drift: CLOSED/OPEN`) consumable by STEP D, completing the structural chain from dimension coaching back to confirmed readiness.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Table-form ARCHITECTURE (Named Output | Produced by | Consumed by) satisfies C-25 with lower overhead than schema form on the advisory register — three-column table delivers pre-execution auditability and independent scannability without per-step enumeration of consuming relationships", "Per-input C-26 prohibition (separate annotation per named input at consuming step) is stronger than per-step grouped notation — makes partial compliance impossible by requiring each specific named input reference to carry the prohibition independently", "Three R9 axes (C-24 extended, C-25, C-26) are structurally complementary and register-agnostic: C-25 delivers pre-execution auditability, C-26 delivers execution-time enforcement, C-24 extended closes STEP C dimension-coaching drift; combination reaches 100 on both advisory and imperative registers"]}
```
