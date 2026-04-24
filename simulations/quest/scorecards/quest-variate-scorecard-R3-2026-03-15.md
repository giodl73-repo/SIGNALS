## quest-variate R3 — Scorecard

**Rubric:** v3 (C-01 through C-18) | **Set:** V-01 through V-05 | **Round:** 3

---

### Per-Variation Criterion Assessment

#### C-01 — Runnable Completeness

| V | Status | Evidence |
|---|--------|----------|
| V-01 | PASS | Full three-step prompt: SELECT AXES → envelope format → GENERATE BODIES → FINDINGS with tables. All sections written out. |
| V-02 | PASS | Full three-step prompt: SELECT AXES → GENERATOR role + LOOP-GATE VERIFIER per-body → FINDINGS with loop-gate verdict column. All sections present. |
| V-03 | PASS | Full prompt: DECLARE THE CHAMPION → GENERATE CHALLENGERS → FINDINGS with challenger map, combination candidates, evaluation order. |
| V-04 | PASS | Full three-phase prompt: PHASE 1 (envelope commitment + review) → PHASE 2 (generator + loop gate) → PHASE 3 (findings with three tables). No placeholders. |
| V-05 | PASS | Full three-phase prompt: PHASE 1 (champion inventory + variation map with score predictions) → PHASE 2 (challenger generation) → PHASE 3 (findings with calibration table). No placeholders. |

---

#### C-02 — Count and Labeling

| V | Status | Evidence |
|---|--------|----------|
| All | PASS | Exactly 5 variations, labeled V-01 through V-05 with no gaps. Combination passes are additive, not substitutions. |

---

#### C-03 — Axis Declaration

| V | Status | Evidence |
|---|--------|----------|
| V-01 | PASS | `axis: output-format`; `hypothesis:` field fully populated with criterion ID, direction, mechanism, and failure condition. |
| V-02 | PASS | `axis: role-sequence`; `hypothesis:` field fully populated including two distinct failure conditions. |
| V-03 | PASS | `axis: inertia-framing`; `hypothesis:` field names C-07 and C-09 with competitive mechanism. |
| V-04 | PASS | `axis: output-format × role-sequence`; `pass-type: combination` labeled explicitly. `hypothesis:` field names C-01, C-03, C-14 with mechanisms. |
| V-05 | PASS | `axis: inertia-framing × scoring-granularity`; `pass-type: combination` labeled explicitly. `hypothesis:` names C-07, C-14. |

---

#### C-04 — Single-Axis Isolation

| V | Status | Evidence |
|---|--------|----------|
| V-01 | PASS | Structural change: adds structured variation envelope. No role, lifecycle, or framing changes. |
| V-02 | PASS | Structural change: adds Loop-Gate Verifier role. No format, lifecycle, or framing changes. |
| V-03 | PASS | Structural change: replaces neutral baseline reference with champion-challenger competitive framing. No format or role changes. |
| V-04 | PASS | Labeled combination: `output-format × role-sequence`. C-04 exception explicitly invoked. |
| V-05 | PASS | Labeled combination: `inertia-framing × scoring-granularity`. C-04 exception explicitly invoked. |

---

#### C-05 — Genuine Distinctness

| V | Status | Evidence |
|---|--------|----------|
| All | PASS | Three non-overlapping single-axis changes (structured envelope, loop-gate role, champion-challenger framing) + two distinct combination compositions. No synonym-swap degeneracy. Reading any two variation bodies side-by-side, the structural difference maps to its named axis and produces observably different generation behavior. |

---

#### C-06 — Axis Spread

| V | Status | Evidence |
|---|--------|----------|
| All | PASS | Single-axis coverage: output-format (V-01), role-sequence (V-02), inertia-framing (V-03). Combination coverage adds scoring-granularity (V-05). Four distinct axes from the canonical six. Exceeds ≥3 threshold. |

---

#### C-07 — Falsifiable Hypotheses

| V | Status | Evidence |
|---|--------|----------|
| V-01 | PASS | Predicts "increases C-03 pass rates because the required-field structure cannot be silently omitted." Failure condition: does not exceed R2 inline-header baseline on C-03. |
| V-02 | PASS | Predicts "increases C-01 pass rates because incomplete bodies are caught while the generation context is still active." Failure condition: two modes named — no C-01 improvement vs. R2, or gate implemented as post-generation review (which would independently fail C-15). |
| V-03 | PASS | Predicts "increases C-07 specificity because competitive arguments are criterion-grounded by construction." Failure condition: two modes — C-07 rate doesn't exceed R2 baselines, or hypotheses describe only what challenger does without naming champion failure. |
| V-04 | PASS | Predicts "increases C-01 and C-03 jointly" with front-and-back coverage mechanism. Failure condition: names V-01 as denominator specifically. |
| V-05 | PASS | Predicts "increases C-07 jointly" with combined competitive + criterion-keyed mechanism. Failure condition: names V-03 as denominator specifically. |

---

#### C-08 — Baseline Explicit or Inferable

| V | Status | Evidence |
|---|--------|----------|
| All | PASS | Pre-Generation Per-Axis Pole Declaration table covers all 6 canonical axes with "Baseline Pole (What the Champion Currently Does)" column. Baseline is stated, not inferable — exceeds C-08 minimum requirement. |

---

#### C-09 — Combination Roadmap

| V | Status | Evidence |
|---|--------|----------|
| All | PASS | "Combination Roadmap for Round 4 (C-09)" table after the single-axis variations: Priority 1 (role-sequence × inertia-framing, basis V-02 × V-03, criteria C-01, C-04, C-07) and Priority 2 (output-format × scoring-granularity, basis V-01 × uncovered, criteria C-03, C-07, C-14). Mechanism sentence per row. |

---

#### C-10 — Hypothesis Tension Surfaced

| V | Status | Evidence |
|---|--------|----------|
| All | PASS | "Axis Tension Note" section names two tensions: (1) output-format × role-sequence — "these axes operate at opposite lifecycle positions: pre-body and post-body"; (2) inertia-framing × scoring-granularity — "they may be redundant: a competitive hypothesis that names the champion failure is already criterion-targeted." |

---

#### C-11 — Explicit Failure Condition on Every Hypothesis

| V | Status | Evidence |
|---|--------|----------|
| V-01 | PASS | "Failure condition: if C-03 pass rates do not exceed those from inline-header variations in R2…" |
| V-02 | PASS | Two failure conditions: (1) C-01 no improvement vs. R2 gate-absent baseline; (2) "Additionally fails if the gate is implemented as a final-step review of all bodies rather than a per-body check." |
| V-03 | PASS | Two failure conditions: (1) C-07 rate doesn't exceed R2 baselines; (2) "Also fails if any variation hypothesis describes only what the challenger does, without naming a specific champion failure." |
| V-04 | PASS | "Failure condition: if C-01 and C-03 pass rates do not jointly exceed those achieved by V-01 alone (R3 V-01 structured-envelope single-axis baseline)…" |
| V-05 | PASS | "Failure condition: if C-07 pass rates do not jointly exceed those achieved by V-03 alone (R3 V-03 inertia-framing single-axis baseline)…" |

---

#### C-12 — Evaluation Order Guidance

| V | Status | Evidence |
|---|--------|----------|
| All | PASS | "Evaluation Order Guidance" table at end: 5 rows, columns for Priority / Variation / Axis / Evaluation Cost / Independence / Dependency Note. V-01 listed first (establishes C-03 and C-14 baseline for V-04), V-03 second (comparison denominator for V-05), V-02 third, V-04 fourth, V-05 last. Dependency chain is explicit. |

---

#### C-13 — Hypothesis Tension Pre-Combination

| V | Status | Evidence |
|---|--------|----------|
| All | PASS | "Axis Tension Note" section appears before "Combination Roadmap for Round 4" in document order. Dominant axis predictions stated: output-format dominates role-sequence (pre-commitment beats post-correction); inertia-framing dominates scoring-granularity (competitive argument already criterion-targeted). |

---

#### C-14 — Criterion-Targeted Axis Selection

| V | Status | Evidence |
|---|--------|----------|
| V-01 | PASS | Formal `targets-criterion: C-03` field with mechanism: "a structured variation envelope with required named fields forces field completeness before the body is written." Strongest C-14 implementation in the set — dedicated header field, not prose. |
| V-02 | PASS | Formal `targets-criterion: C-01` field with mechanism: "a Loop-Gate Verifier role fires after each variation body… errors caught while the body's generation context is active are correctable." |
| V-03 | PASS | No formal `targets-criterion:` field. However, hypothesis names C-07 by ID and states mechanism: "replaces directional predictions… with competitive arguments that are criterion-grounded by construction" — mechanism explicit in hypothesis prose. PASS for C-14 set-level test; slightly weaker per-variation implementation than V-01/V-02. |
| V-04 | PASS | Hypothesis states: "The `criterion-targeted:` field also compounds C-14 (criterion-targeted axis selection) by making the axis-to-criterion connection a required declaration per variation." Combination amplifies C-14 by elevating it to envelope infrastructure. |
| V-05 | PASS | Hypothesis states: "The `criterion-targeted:` field produced by the score prediction block also advances C-14 (criterion-targeted axis selection) for each generated variation." |

---

#### C-15 — Inline Generation Loop Gate

| V | Status | Evidence |
|---|--------|----------|
| V-01 | FAIL | Output-format variation only. No loop gate present. The criterion applies: "at least one variation" must have it — V-02 and V-04 carry this for the set. Per-variation gap. |
| V-02 | PASS | "--- ROLE: LOOP-GATE VERIFIER ---… fires once per variation, in sequence: After V-01 is written, before V-02 begins. After V-02 is written, before V-03 begins." Checks C-01 and C-04 by name. Explicit "fix before advancing" in both check blocks. |
| V-03 | FAIL | Inertia-framing variation. No loop gate. FINDINGS section is post-generation only. |
| V-04 | PASS | "--- ROLE: LOOP-GATE VERIFIER (fires after EACH body, before Generator advances) ---" with three checks: C-01 COMPLETENESS, C-04 ISOLATION, ENVELOPE FIDELITY. Fires inside Phase 2 loop. |
| V-05 | FAIL | Combination variation but loop gate not included. PHASE 3 FINDINGS is post-generation only. Champion inventory + score prediction table provide pre-generation rigor but no in-loop gate. |

---

#### C-16 — Per-Axis Pole Declaration Before Generation

| V | Status | Evidence |
|---|--------|----------|
| All | PASS | "Pre-Generation: Per-Axis Pole Declaration (C-16)" table covers all 6 canonical axes: role-sequence, output-format, lifecycle-emphasis, phrasing-register, inertia-framing, scoring-granularity — each with its "Baseline Pole" and "R3 Variation Pole Committed" columns. Appears before any variation body. |

---

#### C-17 — Pre-Generation Axis Lock (combination passes only)

| V | Status | Evidence |
|---|--------|----------|
| V-01 | N/A (pass) | Single-axis — vacuously true. |
| V-02 | N/A (pass) | Single-axis — vacuously true. |
| V-03 | N/A (pass) | Single-axis — vacuously true. |
| V-04 | PASS | "Do not revise axis assignments after Phase 2 begins. The axis committed in each envelope is immutable once Phase 2 starts." Appears in PHASE 1 before any body is written. |
| V-05 | PASS | "Do not revise axis assignments after Phase 2 begins." appears at top of PHASE 1, before the champion inventory even begins. |

---

#### C-18 — Single-Axis Comparison Denominator (combination passes only)

| V | Status | Evidence |
|---|--------|----------|
| V-01 | N/A (pass) | Single-axis. |
| V-02 | N/A (pass) | Single-axis. |
| V-03 | N/A (pass) | Single-axis. |
| V-04 | PASS | Failure condition: "if C-01 and C-03 pass rates do not jointly exceed those achieved by V-01 alone (R3 V-01 structured-envelope single-axis baseline, where C-03 was the primary targeted criterion)…" — V-01 is the dominant-axis denominator. |
| V-05 | PASS | Failure condition: "if C-07 pass rates do not jointly exceed those achieved by V-03 alone (R3 V-03 inertia-framing single-axis baseline, where champion-challenger framing increased C-07 pass rates…)" — V-03 is the dominant-axis denominator. |

---

### Composite Score

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 10 * 10)

Essential  (C-01–C-05): 5/5 → 60
Recommended (C-06–C-08): 3/3 → 30
Aspirational (C-09–C-18): 10/10 → 10
────────────────────────────────
Composite: 100
Band: GOLD (>= 80, all essential pass)
```

**Golden threshold:** Met — all 5 essential pass AND composite = 100.

---

### Per-Variation Ranking

Ranking uses applicable per-variation criteria (C-01, C-03, C-04, C-07, C-11, C-14, C-15, C-17, C-18; N/A = full credit for single-axis on C-17/C-18):

| Rank | V | Applicable | Pass | Score | Distinguishing Factor |
|------|---|-----------|------|-------|----------------------|
| 1 | V-04 | 9 | 9 | 100% | Only variation covering C-01, C-03, C-04, C-07, C-11, C-14, C-15, C-17, C-18 simultaneously — combination amplifies every per-variation criterion |
| 2 | V-02 | 7 | 7 | 100% | Only single-axis variation to pass C-15; strongest anchor-quality isolation (single role addition, binary failure condition) |
| 3 | V-05 | 9 | 8 | 89% | Passes C-17 and C-18; misses C-15 (no in-loop gate despite being a combination pass) |
| 4 | V-01 | 7 | 6 | 86% | Strongest per-variation C-14 implementation (dedicated `targets-criterion:` field); misses C-15 |
| 5 | V-03 | 7 | 6 | 86% | Strong C-07 and C-11 (two failure conditions); C-14 passes at prose level but no formal field; no C-15 |

*V-01 ranked above V-03 on the same raw score: V-01's `targets-criterion:` field is the most formally explicit C-14 implementation in the set (a structural slot, not hypothesis prose).*

---

### Excellence Signals

**From V-04 (top-scoring variation):**

1. **Combination passes inherit and extend the loop gate.** V-04 is the only combination variation that carries V-02's Loop-Gate Verifier forward and adds a third check (ENVELOPE FIDELITY — verifying `baseline-delta:` against what actually changed and `completeness-risk:` section presence). Combinations that add a second axis without preserving the existing gate degrade correctness coverage; carrying the gate forward with an additional check is the correct pattern.

2. **Phase separation + immutability enforces isolation as protocol.** V-04's PHASE 1 / PHASE 2 split means all axis commitments are made before any body is written, and the immutability instruction fires within that commitment phase. This converts "change only one axis" from a guideline to a structural constraint: by the time Phase 2 begins, the variation map is locked and the loop gate verifies against it.

**From V-02 (co-top, single-axis):**

3. **The gate must name the criteria it is checking by ID.** V-02's gate checks "C-01 COMPLETENESS" and "C-04 SINGLE-AXIS ISOLATION" by criterion label, not by description. This makes gate verdicts reproducible: a reviewer reading the transcript can verify the gate fired against the correct rubric item without inferring which criterion the description maps to. Per-criterion labeling inside the gate is what distinguishes a scoring instrument from a prose reminder.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["combination passes should inherit and extend the loop gate from the role-sequence single-axis variation, adding a third envelope-fidelity check that verifies baseline-delta consistency after each body", "phase separation with explicit immutability instruction converts single-axis isolation from design intention to structural protocol constraint: axis assignments locked before Phase 2 begins, loop gate verifies against the committed map", "loop gate criteria named by rubric ID inside the gate body (not by description) makes gate verdicts reproducible without inference"]}
```
