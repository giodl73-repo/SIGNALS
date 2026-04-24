## /quest:score — quest-golden Round 3 (rubric v2)

---

### Phase 0: Criterion Counts

```
Loaded rubric: v2 (quest-golden-rubric-2026-03-15.md)
Essential criteria:    N_e = 5  (C-01 through C-05)
Recommended criteria:  N_r = 3  (C-06 through C-08)
Aspirational criteria: N_a = 4  (C-09 through C-12)
```

C-12 interpretation note: The rubric text says "trial gate and quest gate" but QG-09 says "GATE 1 and GATE 2." The R3 variations uniformly target the SCORING gates (essential/composite) as the dual-gate anti-conflation concern. QG-09's formulation is treated as authoritative — C-12 pass condition evaluated against the scoring step gate labels, not convergence gates.

---

### Scorecard: V-01 — Output Format: Inline Resolved Formula

| Criterion | Tier | Weight | Verdict | Evidence |
|-----------|------|--------|---------|----------|
| C-01 | essential | 12 | PASS | Step 1 produces V-NN format; Step 5 convergence check with "Name the axis or combination to target next" enforces multi-round loop |
| C-02 | essential | 12 | PASS | Step 5: "Trial convergence" and "Quest plateau" explicitly named; "Dual convergence = trial converged AND quest plateau" |
| C-03 | essential | 12 | PASS | Step 5: "the golden prompt body is the body of the highest-scoring GOLDEN variation. Write it as the canonical skill body" |
| C-04 | essential | 12 | PASS | Step 5: "Write the final rubric." QU4 in Step 4 gates criterion addition with approval decision |
| C-05 | essential | 12 | PASS | Step 2 formula block requires numeric total: `= [numeric total]`. Example: `(5/5 * 60) + (2/3 * 30) + (1/4 * 10) = 82.5` |
| C-06 | recommended | 10 | PASS | Step 3: `Mechanism: [the specific structural element in V-NN that produced the higher score]` + `Pattern: [the generalized principle]` |
| C-07 | recommended | 10 | PASS | Step 4: QU3 table with ID/Category/Pass Condition + QU4: "Proposed: add C-[NN] to rubric... Apply? [Y/N]" with version/date/denominator note |
| C-08 | recommended | 10 | PARTIAL | Step 5 tracks "Signals this round: [count]" and "Signals prior round: [count from round N-1]" and "Consecutive rounds with no signals: [count]" — count tracked but no instruction to name specific rounds by label |
| C-09 | aspirational | 2.5 | FAIL | No element-mapping requirement present at golden prompt write step. QG outcome: gratuitous inclusion check absent |
| C-10 | aspirational | 2.5 | FAIL | Outcome criterion; no structural enforcement of ≤5 rounds in prompt body |
| C-11 | aspirational | 2.5 | PASS | Phase 0 Step 0a declares `N_e = [count]`, `N_r = [count]`, `N_a = [count]`. Step 2: "Write the formula with these concrete values substituted. Do not retain symbolic N_essential… Resolve to arithmetic." Example with concrete numbers. QG-08 failure mode directly closed |
| C-12 | aspirational | 2.5 | FAIL | Step 5 has labeled "Trial convergence" and "Quest plateau" sections and "Dual convergence = trial converged AND quest plateau" — but no prohibition sentence per QG-09: "contains no explicit prohibition against collapsing them into a single compound check" |

**Formula resolution (N_e=5, N_r=3, N_a=4; PARTIAL=0 in count):**
```
essential_pass = 5, recommended_pass = 2 (C-08 PARTIAL excluded), aspirational_pass = 1

composite = (5/5 * 60) + (2/3 * 30) + (1/4 * 10)
          = 60 + 20 + 2.5
          = 82.5
```

**GATE 1 — Essential pass:** C-01 PASS, C-02 PASS, C-03 PASS, C-04 PASS, C-05 PASS → SATISFIED  
**GATE 2 — Composite >= 80:** 82.5 >= 80 → SATISFIED  
**Verdict: GOLDEN**

---

### Scorecard: V-02 — Phrasing Register: Explicit Dual-Gate Anti-Conflation

| Criterion | Tier | Weight | Verdict | Evidence |
|-----------|------|--------|---------|----------|
| C-01 | essential | 12 | PASS | Same loop structure; Step 5 convergence check guides additional rounds |
| C-02 | essential | 12 | PASS | Step 5: "Trial converged: Y / N" and "Quest plateau: Y (0 signals for 2 consecutive rounds) / N" and "Convergence verdict: dual convergence / not yet" |
| C-03 | essential | 12 | PASS | Step 5: "If dual convergence: write the golden prompt body." |
| C-04 | essential | 12 | PASS | Step 5: "Write the final rubric." QU4 present with apply/defer decision |
| C-05 | essential | 12 | PASS | Step 2: formula block with `= [computed score]` |
| C-06 | recommended | 10 | PASS | Step 3: `Mechanism: [the structural element producing the higher score]` + `Pattern: [the generalized principle]` |
| C-07 | recommended | 10 | PASS | Step 4: QU3 table + QU4 "State whether to apply or defer. If applied, note the version, date, and formula update." |
| C-08 | recommended | 10 | PARTIAL | "Quest plateau: Y (0 signals for 2 consecutive rounds) / N" — binary flag, no round-label naming instruction |
| C-09 | aspirational | 2.5 | FAIL | No element-mapping requirement at convergence step |
| C-10 | aspirational | 2.5 | FAIL | No structural enforcement of ≤5 round bound |
| C-11 | aspirational | 2.5 | FAIL | Step 2 formula retains symbolic denominators: `(essential_pass / N_essential * 60) + (recommended_pass / N_recommended * 30) + (aspirational_pass / N_aspirational * 10)`. No Phase 0 count block. QG-08 failure mode open |
| C-12 | aspirational | 2.5 | PASS | GATE 1: "Do not consider the composite score in GATE 1. A composite of 95 does not satisfy GATE 1 if any essential criterion is PARTIAL or FAIL. Do not conflate." GATE 2: "Do not apply GATE 2 to a variation where GATE 1 is NOT SATISFIED. Do not conflate. A variation with an essential FAIL is FAIL regardless of its composite score." Two explicit prohibition sentences, one per gate. QG-09 directly closed |

**Formula resolution:**
```
essential_pass = 5, recommended_pass = 2, aspirational_pass = 1

composite = (5/5 * 60) + (2/3 * 30) + (1/4 * 10)
          = 60 + 20 + 2.5
          = 82.5
```

**GATE 1:** All essential PASS → SATISFIED  
**GATE 2:** 82.5 >= 80 → SATISFIED  
**Verdict: GOLDEN**

---

### Scorecard: V-03 — Inertia Framing: Status-Quo Conflation Competitor

| Criterion | Tier | Weight | Verdict | Evidence |
|-----------|------|--------|---------|----------|
| C-01 | essential | 12 | PASS | Same loop structure with per-round Status-Quo Scorer comparison adding naming pressure |
| C-02 | essential | 12 | PASS | Step 5: "Trial converged: Y / N" and "Quest plateau: Y / N" and "Convergence verdict: dual convergence / not yet" |
| C-03 | essential | 12 | PASS | Step 5: "If dual convergence: write the golden prompt body." |
| C-04 | essential | 12 | PASS | Step 4 QU4 + Step 5 final rubric instruction |
| C-05 | essential | 12 | PASS | Step 2: `composite = (essential_pass / N_essential * 60) + ... = [computed score]` — numeric score computed |
| C-06 | recommended | 10 | PASS | Step 3 with `Mechanism:` and `Pattern:` fields + SQS comparison: "beats the Status-Quo Scorer by: [one sentence per criterion where anti-conflation evaluation prevented a verdict]" |
| C-07 | recommended | 10 | PASS | Step 4: QU3 table + QU4 apply/defer |
| C-08 | recommended | 10 | PARTIAL | Step 5 counts signals but no round-label naming requirement |
| C-09 | aspirational | 2.5 | FAIL | No element mapping at convergence step |
| C-10 | aspirational | 2.5 | FAIL | No structural ≤5 round enforcement |
| C-11 | aspirational | 2.5 | FAIL | Step 2 formula is symbolic: `essential_pass / N_essential`. No count block in Phase 0. QG-08 open |
| C-12 | aspirational | 2.5 | PASS | Preamble defines SQS as conflater. Anti-conflation test: "Does this scorecard evaluate the essential gate independently from the composite gate? YES/NO." Scoring threshold block: "1. Essential gate: [all PASS / ...] -- independent of composite score. 2. Composite gate: [score] -- evaluated only because essential gate passed." Anti-conflation record required: "This scorecard beats the Status-Quo Scorer because: [one sentence]." Structural independence is argued and recorded per scorecard |

**Formula resolution:**
```
essential_pass = 5, recommended_pass = 2, aspirational_pass = 1

composite = (5/5 * 60) + (2/3 * 30) + (1/4 * 10)
          = 60 + 20 + 2.5
          = 82.5
```

**GATE 1:** All essential PASS → SATISFIED  
**GATE 2:** 82.5 >= 80 → SATISFIED  
**Verdict: GOLDEN**

---

### Scorecard: V-04 — Combination: Output Format × Phrasing Register (Priority 1)

| Criterion | Tier | Weight | Verdict | Evidence |
|-----------|------|--------|---------|----------|
| C-01 | essential | 12 | PASS | Same loop structure with spread table and convergence check |
| C-02 | essential | 12 | PASS | Step 5: "Trial converged: Y / N" and "Quest plateau: Y / N" and "Convergence verdict: dual convergence / not yet" |
| C-03 | essential | 12 | PASS | Step 5: "If dual convergence: write the golden prompt body." |
| C-04 | essential | 12 | PASS | QU4 + final rubric instruction |
| C-05 | essential | 12 | PASS | Step 2: `= ([ep] / [N_e] * 60) + ([rp] / [N_r] * 30) + ([ap] / [N_a] * 10) = [numeric total]` |
| C-06 | recommended | 10 | PASS | Step 3: `Mechanism:` and `Pattern:` fields present |
| C-07 | recommended | 10 | PASS | Step 4: QU3 table + QU4 apply/defer with version/date/denominator update |
| C-08 | recommended | 10 | PARTIAL | Step 5: "Quest plateau: Y / N" without round-naming instruction |
| C-09 | aspirational | 2.5 | FAIL | No element-mapping requirement at convergence step |
| C-10 | aspirational | 2.5 | FAIL | No structural ≤5 round enforcement |
| C-11 | aspirational | 2.5 | PASS | Phase 0 Step 0a: `N_e = [count]`, `N_r = [count]`, `N_a = [count]`. Step 2: "Write the formula with actual counts substituted. Do not use symbolic N_essential." Example: `(4/5 * 60) + (2/3 * 30) + (1/4 * 10) = 48 + 20 + 2.5 = 70.5`. QG-08 closed |
| C-12 | aspirational | 2.5 | PASS | GATE 1: "Do not consider composite score in GATE 1. A high composite does not override an essential FAIL. Do not conflate." GATE 2: "If GATE 1 is NOT SATISFIED, do not evaluate GATE 2. A variation with an essential failure is FAIL regardless of its composite score. Do not conflate." QG-09 closed |

**Formula resolution:**
```
essential_pass = 5, recommended_pass = 2, aspirational_pass = 2 (C-11 PASS, C-12 PASS)

composite = (5/5 * 60) + (2/3 * 30) + (2/4 * 10)
          = 60 + 20 + 5
          = 85
```

**GATE 1:** All essential PASS → SATISFIED  
**GATE 2:** 85 >= 80 → SATISFIED  
**Verdict: GOLDEN**

---

### Scorecard: V-05 — Combination: Lifecycle Emphasis × Output Format (Priority 2)

| Criterion | Tier | Weight | Verdict | Evidence |
|-----------|------|--------|---------|----------|
| C-01 | essential | 12 | PASS | Loop structure with Phase A/B scoring and convergence check |
| C-02 | essential | 12 | PASS | Step 5: "Quest plateau: Y (0 signals for 2 consecutive rounds) / N" + "Convergence verdict: dual convergence / not yet" |
| C-03 | essential | 12 | PASS | Step 5: "If dual convergence: write the golden prompt body." |
| C-04 | essential | 12 | PASS | QU4 + "If applied, note version, date, and update N_a in Phase 0 for the next round." Final rubric instruction |
| C-05 | essential | 12 | PASS | Step 2A: `composite = ([essential_pass_count] / [N_e] * 60) + ... = [numeric total]` |
| C-06 | recommended | 10 | PASS | Step 3: `Mechanism:` and `Pattern:` fields present |
| C-07 | recommended | 10 | PASS | Step 4: QU3 table + QU4 apply/defer with N_a denominator update note |
| C-08 | recommended | 10 | PARTIAL | Step 5: "Quest plateau: Y (0 signals for 2 consecutive rounds) / N" — binary, no round-label naming instruction |
| C-09 | aspirational | 2.5 | FAIL | No element-mapping requirement |
| C-10 | aspirational | 2.5 | FAIL | No structural ≤5 round enforcement |
| C-11 | aspirational | 2.5 | PASS | Phase 0 Step 0a: explicit count block. Step 2A: "Substitute concrete denominators from Phase 0 Step 0a. Resolve to arithmetic. Do not retain symbolic N_essential, N_recommended, N_aspirational." Step 2A completion gate: "Proceed to Step 2B only after the formula has been resolved with concrete counts and a numeric total is present." QG-08 closed with temporal enforcement |
| C-12 | aspirational | 2.5 | PASS | Step 2B GATE 1: "Do not use the composite score to determine GATE 1. Evaluate GATE 1 independently. Do not conflate." GATE 2: "If GATE 1 is NOT SATISFIED: do not evaluate GATE 2. A FAIL verdict from GATE 1 is final. Do not conflate with composite score." Phase A/B boundary structurally prevents gate conflation by temporal ordering |

**Formula resolution:**
```
essential_pass = 5, recommended_pass = 2, aspirational_pass = 2 (C-11 PASS, C-12 PASS)

composite = (5/5 * 60) + (2/3 * 30) + (2/4 * 10)
          = 60 + 20 + 5
          = 85
```

**GATE 1:** All essential PASS → SATISFIED  
**GATE 2:** 85 >= 80 → SATISFIED  
**Verdict: GOLDEN**

---

### Step 5: Dual Convergence Check

| Variation | GATE 1 (essential) | GATE 2 (composite) | Composite | Verdict |
|-----------|-------------------|-------------------|-----------|---------|
| V-01 | SATISFIED | SATISFIED | 82.5 | GOLDEN |
| V-02 | SATISFIED | SATISFIED | 82.5 | GOLDEN |
| V-03 | SATISFIED | SATISFIED | 82.5 | GOLDEN |
| V-04 | SATISFIED | SATISFIED | 85.0 | GOLDEN |
| V-05 | SATISFIED | SATISFIED | 85.0 | GOLDEN |

Trial converged: **Y** — 5/5 GOLDEN  
Quest plateau: **N** — 2 excellence signals this round (C-11, C-12 first appeared in R1; V-04/V-05 combination is new this round)

Convergence verdict: **not yet** — quest plateau unmet. R3 produced new combination patterns. Next round: target C-09 (element-mapping) and C-08 (round-label naming) to push toward 90+.

---

### Ranking

| Rank | Variation | Composite | Verdict | Differentiator |
|------|-----------|-----------|---------|----------------|
| 1 (tie) | V-04 | 85.0 | GOLDEN | C-11 + C-12 both PASS; non-overlapping combination |
| 1 (tie) | V-05 | 85.0 | GOLDEN | C-11 + C-12 both PASS; temporal enforcement via phase split |
| 3 (tie) | V-01 | 82.5 | GOLDEN | C-11 PASS, C-12 FAIL |
| 3 (tie) | V-02 | 82.5 | GOLDEN | C-12 PASS, C-11 FAIL |
| 3 (tie) | V-03 | 82.5 | GOLDEN | C-12 PASS via competitive framing, C-11 FAIL |

---

### Excellence Signals

```
Signal: C-11 -- Composite formula embedded inline with concrete denominators
Source variation: V-01 (axis: output-format)
Baseline verdict: FAIL (V-02, V-03 — symbolic N_essential retained)
Signal verdict: PASS
Mechanism: Two-step substitution. Phase 0 Step 0a declares N_e/N_r/N_a as named outputs.
  Step 2 explicitly references those outputs ("concrete denominators from Phase 0")
  and prohibits retaining symbolic form. The count block in Phase 0 creates a visible
  structural dependency: if the formula in Step 2 still shows N_essential, the Phase 0
  output is present-but-unused — a mechanically detectable inconsistency.
Pattern: Formula correctness enforced by grounding: when denominators are declared as
  phase outputs before the step that uses them, skipping the substitution produces a
  visible structural inconsistency rather than an invisible omission.
```

```
Signal: C-12 -- Anti-conflation guard present in the dual-gate section
Source variation: V-02 (axis: phrasing-register)
Baseline verdict: FAIL (V-01 — labeled sections, no prohibition text)
Signal verdict: PASS
Mechanism: Per-gate prohibition sentence. Each gate block contains one sentence
  explicitly prohibiting use of the other gate's output: "Do not consider the composite
  score in GATE 1" and "Do not apply GATE 2 to a variation where GATE 1 is NOT SATISFIED."
  The prohibition fires at the moment of gate evaluation, not at the moment of reading
  a general instruction.
Pattern: Point-of-use prohibition: when a prohibition against conflation is placed
  inside the section it protects (rather than as a preamble or structural label),
  the operator encounters it at the moment the conflation temptation arises.
```

```
Signal: C-11 + C-12 joint coverage
Source variation: V-04 (axis: output-format x phrasing-register) and V-05 (lifecycle-emphasis x output-format)
Baseline verdict: V-01 passes C-11, fails C-12. V-02 passes C-12, fails C-11. Neither achieves joint coverage.
Signal verdict: Both C-11 and C-12 PASS — 85.0 vs 82.5 for single-axis variations.
Mechanism (V-04): The two criteria occupy non-overlapping sections of the scoring block.
  V-01's formula resolution instruction lives in Phase 0 and Step 2. V-02's anti-conflation
  prohibition lives in Gate 1 and Gate 2 blocks. Combining them adds no redundancy and
  produces additive aspirational coverage.
Mechanism (V-05): Phase A / Phase B split creates temporal ordering. Phase A (formula
  resolution) must complete before Phase B (threshold evaluation) begins. This structural
  sequencing enforces concrete denominators (you need them to finish Phase A) and prevents
  gate conflation (the gates inhabit separate labeled phases rather than a single scoring block).
  One lifecycle change addresses both criteria simultaneously.
Pattern (V-04): Non-overlapping mechanism combination — when two criteria each have
  independent structural addresses in adjacent non-overlapping sections, combining their
  single-axis fixes produces additive criterion coverage without structural redundancy.
Pattern (V-05): Single architectural change addressing multiple criteria — a lifecycle
  phase boundary that creates temporal ordering can simultaneously enforce formula resolution
  (must be done in Phase A before Phase B starts) and gate independence (each gate is
  structurally located in its own phase).
```

---

### QU2 / QU3 / QU4

**QU2 — Top signal:**  
"When a Phase A / Phase B split separates per-criterion verdict and formula resolution from threshold evaluation, C-11 and C-12 scores both improve from FAIL to PASS because the phase boundary creates a structural temporal dependency: the formula must be resolved with concrete denominators (Phase A output) before the gates can be evaluated (Phase B input), and the two gates already inhabit separate structural sections, making conflation architecturally awkward rather than merely discouraged."

**QU3 — Proposed criterion (V-05 pattern):**

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-13 | **Single-change multi-criterion coverage** — The prompt body contains at least one structural element that simultaneously satisfies two or more aspirational criteria through a shared mechanism | efficiency | aspirational | Identify one structural element in the prompt body; name the two criteria it satisfies; confirm that removing the element would degrade BOTH criteria. A structural element that addresses only one criterion does not qualify. |

**QU4 — Defer.**  
C-13 requires at least one more round to validate that the V-05 phase-split pattern holds across different skill types. The current evidence is from a single combination variation (V-05). Defer to Round 4.

---

### Summary

All 5 variations GOLDEN. Top score: **85** (V-04, V-05 tied). Single-axis variations plateau at 82.5. The combination slot is the scoring frontier: both C-11 and C-12 are independently achievable but only jointly covered by V-04/V-05.

V-05 is the more structurally interesting winner: its Phase A/Phase B split achieves C-11+C-12 joint coverage through a single architectural change rather than two parallel additions. This makes V-05 the preferred base for Round 4 work, since it leaves adjacent sections open for C-08 (round-naming) and C-09 (element-mapping) improvements without crowding the scoring block.

---

```json
{"top_score": 85, "all_essential_pass": true, "new_patterns": ["Phase A / Phase B lifecycle split simultaneously enforces concrete formula resolution (C-11) and gate independence (C-12) through a single temporal-ordering change — one architectural decision addresses both criteria", "Non-overlapping adjacent mechanism combination: when two aspirational criteria have independent structural addresses in non-overlapping sections, combining their single-axis fixes produces additive scoring gains without redundancy"]}
```
