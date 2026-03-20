## Scorecard: specify-abstract R12

---

### Scoring Framework

**Point totals by tier:**

| Tier | Points |
|------|--------|
| Essential (C-01 to C-05) | 50 |
| Recommended (C-06 to C-08) | 30 |
| Aspirational (C-10 to C-37) | 20 |
| **Total** | **100** |

**Golden threshold**: all essential pass AND composite >= 80.

---

### V-01 -- Sub-Phase Canonical Naming with Structural Rationale Block

**Axis**: Lifecycle emphasis — C-36 active, C-37 absent

#### Essential (50 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Six-part structure present | PASS | Phase 2a labels all six sections with labeled slot instructions |
| C-02 | Word count within target | PASS | Phase 3 merge + word count + compression-if-OVER present |
| C-03 | Artifact written to correct path | PASS | Write instruction to `signals/specify/abstract/{{topic}}-abstract-{{date}}.md` with required frontmatter |
| C-04 | Gap framed as gap, not goal | PASS | "X remains unresolved / it is unknown whether X" framing enforced; goal-language explicitly excluded |
| C-05 | Signal acquisition executed | PASS | Phase 1 glob `signals/**/{topic}-*` with extraction requirement before writing |

**Essential total: 50 / 50. All essential PASS.**

#### Recommended (30 pts)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-06 | Result section is quantified | PASS | "Include a number, percentage, effect size, or explicit qualitative strength word" required |
| C-07 | Amendment pass produces three distinct | PASS | Five-amendment pass with Before/After for each; non-triviality guard present |
| C-08 | Journal variant applied correctly | PASS | Vacuous pass -- no journal flag; Phase 4 variant table present |

**Recommended total: 30 / 30.**

#### Aspirational (20 pts possible)

| ID | Criterion | Pts | Result | Evidence |
|----|-----------|-----|--------|----------|
| C-10 | Abstract reads as single coherent paragraph | 1 | PASS | Phase 3 produces merged paragraph; no section labels in merged output |
| C-13 | Amendment non-triviality guard applied | 1 | PASS | "A restatement of the prior sentence in different words is not an amendment" explicit |
| C-19 | Paper type governs all six section registers | 1 | PASS | Paper type declared Phase 0; tense, register, Implication form all governed; re-confirmed at Claim |
| C-20 | Semantic bridge type constrained vocabulary | 1 | PASS | Five-term vocabulary (contrast/causation/resolution/escalation/application) in Phase 2c; type assigned before phrase |
| C-21 | Section coupling verified before bridge | 1 | PASS | Phase 2b (coupling) gated before Phase 2c (bridge type+phrase) |
| C-22 | Coupling revision uses structured directive format | 1 | PASS | WEAK/REVISE triggers Boundary/Deficient-section/Deficiency/Before/After/Coupling-status format |
| C-23 | Bridge integration verified post-merge | 1 | PASS | Phase 3b integration table present, positioned after Phase 3 merge |
| C-24 | Self-diagnosis amendment targets weakest element | 1 | PASS | Amendment 1 self-diagnosis with non-fixed-category constraint and per-excluded-category verification |
| C-26 | Bridge integration column cites actual merged prose | 2 | PASS | Phase 3b requires "verbatim extract (3-10 words, in quotation marks) from the merged paragraph" |
| C-27 | Inertia declaration names canonical cheap paths before Phase 0 | 2 | PASS | All three paths named (signal-skip, nominal gap framing, non-trivial gaming) with per-path confirmation before Phase 0 |
| C-29 | Bridge integration format change accompanied by structural rationale | 2 | PASS | Full CAN-side ("Y/N status can be assigned in the same cognitive pass...before the merge has been executed") + CANNOT-side ("verbatim extract from merged prose cannot be written before the merge is executed") present |
| C-34 | Positive search space block contains structural asymmetry argument | 2 | PASS | Dedicated "*Where to look instead -- positive search space:*" block with separate "*Why a separate block -- structural asymmetry:*" CAN/CANNOT argument; four enumerated positive targets |
| C-36 | Sub-phase canonical naming in phase sequence lock | 2 | PASS | Nine individually named sub-phases; Phase 3 (merge) and Phase 3b (integration verification) declared as separately gated; "*Why sub-phase canonical naming matters:*" rationale block names Phase 3/3b causal mechanism and connection to C-26/C-29 |
| C-37 | Weakness-specific per-row reasoning in per-excluded-category verification | 2 | **FAIL** | Uses "[confirmed / explain if uncertain]" template: `This is NOT Gap sharpening (the named weakness does not target the Gap sentence's specificity): [confirmed / explain if uncertain]` — template parenthetical describes category boundary, not the diagnosed weakness |

**Aspirational total: 18 / 20** (C-37 missing 2 pts)

**V-01 composite: 98 / 100. All essential PASS.**

---

### V-02 -- Weakness-Specific Per-Row Reasoning

**Axis**: Output format — C-37 active, C-36 absent

#### Essential (50 pts): All PASS — 50 / 50

#### Recommended (30 pts): All PASS — 30 / 30

#### Aspirational (20 pts possible)

| ID | Criterion | Pts | Result | Evidence |
|----|-----------|-----|--------|----------|
| C-10 | Abstract reads as single coherent paragraph | 1 | PASS | Phase 3 produces merged paragraph |
| C-13 | Amendment non-triviality guard applied | 1 | PASS | Guard present |
| C-19 | Paper type governs all six section registers | 1 | PASS | Phase 0 declaration governs all six |
| C-20 | Semantic bridge type constrained vocabulary | 1 | PASS | Five-term vocabulary in Pass 2 |
| C-21 | Section coupling verified before bridge | 1 | PASS | Pass 1 before Pass 2 |
| C-22 | Coupling revision uses structured directive format | 1 | PASS | Structured directive for WEAK/REVISE |
| C-23 | Bridge integration verified post-merge | 1 | PASS | Pass 3 integration table present |
| C-24 | Self-diagnosis amendment targets weakest element | 1 | PASS | Amendment 1 self-diagnosis with non-fixed-category constraint |
| C-26 | Bridge integration column cites actual merged prose | 2 | PASS | Pass 3 requires quoted extracts |
| C-27 | Inertia declaration names canonical cheap paths before Phase 0 | 2 | PASS | All three paths with per-path confirmation |
| C-29 | Bridge integration format change accompanied by structural rationale | 2 | PASS | Both CAN and CANNOT sides present |
| C-34 | Positive search space block contains structural asymmetry argument | 2 | PASS | Dedicated block with CAN/CANNOT structural argument |
| C-36 | Sub-phase canonical naming in phase sequence lock | 2 | **FAIL** | Coarse-grain lock: "Pass 1 / Pass 2 / Pass 3 -- Boundary quality card (three incremental passes). All three passes must complete before Phase 4." Phase 3 (merge) not named as individual gate; no "Why sub-phase canonical naming matters" rationale block |
| C-37 | Weakness-specific per-row reasoning | 2 | PASS | Format: `Gap sharpening: N -- [one sentence naming the diagnosed weakness and stating why it is not about the Gap sentence's specificity]`; "[confirmed]" shortcut explicitly closed; "*Why specific per-row sentences matter:*" rationale present |

**Aspirational total: 18 / 20** (C-36 missing 2 pts)

**V-02 composite: 98 / 100. All essential PASS.**

---

### V-03 -- Protocol III Pre-Commitment

**Axis**: Inertia framing — Protocol III active; C-36 absent, C-37 absent

#### Essential (50 pts): All PASS — 50 / 50

#### Recommended (30 pts): All PASS — 30 / 30

#### Aspirational (20 pts possible)

| ID | Criterion | Pts | Result | Evidence |
|----|-----------|-----|--------|----------|
| C-10 | Abstract reads as single coherent paragraph | 1 | PASS | Phase 3 produces merged paragraph |
| C-13 | Amendment non-triviality guard applied | 1 | PASS | Guard present |
| C-19 | Paper type governs all six section registers | 1 | PASS | Phase 0 declaration governs all six |
| C-20 | Semantic bridge type constrained vocabulary | 1 | PASS | Five-term vocabulary in Pass 2 |
| C-21 | Section coupling verified before bridge | 1 | PASS | Pass 1 before Pass 2 |
| C-22 | Coupling revision uses structured directive format | 1 | PASS | Structured directive format |
| C-23 | Bridge integration verified post-merge | 1 | PASS | Pass 3 present |
| C-24 | Self-diagnosis amendment targets weakest element | 1 | PASS | Amendment 1 with non-fixed-category constraint |
| C-26 | Bridge integration column cites actual merged prose | 2 | PASS | Quoted extracts in Pass 3 |
| C-27 | Inertia declaration names canonical cheap paths before Phase 0 | 2 | PASS | Protocol I closes all three paths before Phase 0 |
| C-29 | Bridge integration format change accompanied by structural rationale | 2 | PASS | Both CAN and CANNOT sides present |
| C-34 | Positive search space block contains structural asymmetry argument | 2 | PASS | Dedicated block with CAN/CANNOT structural argument; four targets |
| C-36 | Sub-phase canonical naming in phase sequence lock | 2 | **FAIL** | Protocol II uses coarse-grain lock: "Pass 1 / Pass 2 / Pass 3" bundled; Phase 3 not named as individual gate; no sub-phase rationale block |
| C-37 | Weakness-specific per-row reasoning | 2 | **FAIL** | Amendment 1 uses "[confirmed / explain if uncertain]" template in per-excluded-category verification |

**Aspirational total: 16 / 20** (C-36 + C-37 each missing 2 pts)

**V-03 composite: 96 / 100. All essential PASS.**

**Above-ceiling behavior (C-38 candidate):** Protocol III creates auditable temporal separation between target-declaration event (pre-Phase 0, no draft exists) and target-application event (Amendment 1 execution). Amendment 1 references "Protocol III committed targets" — a pre-fixed list rather than an inline introduction. A reader can verify the positive-space targets were declared before Phase 0 by inspecting the Protocol III block alone. This behavior is not captured by any v11 criterion.

---

### V-04 -- V-01 + V-02 (Minimum Synthesis)

**Axis**: Lifecycle emphasis + Output format — C-36 active + C-37 active; Protocol III absent

#### Essential (50 pts): All PASS — 50 / 50

#### Recommended (30 pts): All PASS — 30 / 30

#### Aspirational (20 pts possible)

| ID | Criterion | Pts | Result | Evidence |
|----|-----------|-----|--------|----------|
| C-10 | Abstract reads as single coherent paragraph | 1 | PASS | Phase 3 produces merged paragraph |
| C-13 | Amendment non-triviality guard applied | 1 | PASS | Guard present |
| C-19 | Paper type governs all six section registers | 1 | PASS | Phase 0 declaration governs all six |
| C-20 | Semantic bridge type constrained vocabulary | 1 | PASS | Five-term vocabulary in Phase 2c |
| C-21 | Section coupling verified before bridge | 1 | PASS | Phase 2b gated before Phase 2c |
| C-22 | Coupling revision uses structured directive format | 1 | PASS | Structured directive for WEAK/REVISE |
| C-23 | Bridge integration verified post-merge | 1 | PASS | Phase 3b integration table post-merge |
| C-24 | Self-diagnosis amendment targets weakest element | 1 | PASS | Amendment 1 with non-fixed-category constraint |
| C-26 | Bridge integration column cites actual merged prose | 2 | PASS | Phase 3b requires verbatim quoted extracts |
| C-27 | Inertia declaration names canonical cheap paths before Phase 0 | 2 | PASS | All three paths with per-path confirmation |
| C-29 | Bridge integration format change accompanied by structural rationale | 2 | PASS | Both CAN and CANNOT sides present |
| C-34 | Positive search space block contains structural asymmetry argument | 2 | PASS | Dedicated block with CAN/CANNOT structural argument |
| C-36 | Sub-phase canonical naming in phase sequence lock | 2 | PASS | Nine individually named sub-phases (Phase 0 through Phase 5 with Phase 3 and Phase 3b explicitly gated); "*Why sub-phase canonical naming matters:*" rationale block names Phase 3/3b causal mechanism |
| C-37 | Weakness-specific per-row reasoning | 2 | PASS | Format: `Gap sharpening: N -- [one sentence naming the diagnosed weakness and stating why it is not about the Gap sentence's specificity]`; "[confirmed]" shortcut explicitly closed; "*Why specific per-row sentences matter:*" rationale present |

**Aspirational total: 20 / 20**

**V-04 composite: 100 / 100. All essential PASS.**

---

### V-05 -- Full Synthesis: C-36 + C-37 + Protocol III

**Axis**: All three behaviors active — C-36 (Protocol II sub-phase naming) + C-37 (specific per-row sentences) + Protocol III (pre-committed self-diagnosis framework)

#### Essential (50 pts): All PASS — 50 / 50

#### Recommended (30 pts): All PASS — 30 / 30

#### Aspirational (20 pts possible)

| ID | Criterion | Pts | Result | Evidence |
|----|-----------|-----|--------|----------|
| C-10 | Abstract reads as single coherent paragraph | 1 | PASS | Phase 3 produces merged paragraph |
| C-13 | Amendment non-triviality guard applied | 1 | PASS | Guard present |
| C-19 | Paper type governs all six section registers | 1 | PASS | Phase 0 declaration governs all six |
| C-20 | Semantic bridge type constrained vocabulary | 1 | PASS | Five-term vocabulary in Phase 2c |
| C-21 | Section coupling verified before bridge | 1 | PASS | Phase 2b gated before Phase 2c |
| C-22 | Coupling revision uses structured directive format | 1 | PASS | Structured directive for WEAK/REVISE |
| C-23 | Bridge integration verified post-merge | 1 | PASS | Phase 3b integration table post-merge |
| C-24 | Self-diagnosis amendment targets weakest element | 1 | PASS | Amendment 1 with non-fixed-category constraint; restricted to Protocol III committed targets |
| C-26 | Bridge integration column cites actual merged prose | 2 | PASS | Phase 3b requires verbatim quoted extracts |
| C-27 | Inertia declaration names canonical cheap paths before Phase 0 | 2 | PASS | Protocol I closes all three paths before Phase 0; unified gate closure |
| C-29 | Bridge integration format change accompanied by structural rationale | 2 | PASS | Both CAN and CANNOT sides present in Phase 3b rationale |
| C-34 | Positive search space block contains structural asymmetry argument | 2 | PASS | Dedicated positive-space block with CAN/CANNOT argument; four Protocol III pre-committed targets enumerated |
| C-36 | Sub-phase canonical naming in phase sequence lock | 2 | PASS | Protocol II names nine individually gated sub-phases; Phase 3 (merge) and Phase 3b (integration verification) separately named; "*Why sub-phase canonical naming matters:*" rationale block with Phase 3/3b causal mechanism |
| C-37 | Weakness-specific per-row reasoning | 2 | PASS | Protocol III committed format: `[Category]: N -- [one sentence naming the diagnosed weakness and stating why it does not fall in this category]`; "confirmed is not an acceptable response" explicitly stated; Amendment 1 references "Protocol III committed format" |

**Aspirational total: 20 / 20**

**V-05 composite: 100 / 100. All essential PASS.**

**Above-ceiling behavior (C-38 candidate):** Protocol III creates an auditable lifecycle event: positive search space targets (Background epistemic register / Claim scope relative to Method / Contribution incrementality framing / Method scope adequacy) are committed before Phase 0 when no draft exists, not introduced inline at Amendment 1. The "*Why pre-committing the self-diagnosis framework matters -- structural asymmetry:*" rationale names both sides: a framework introduced at runtime CAN be constructed post-draft; a pre-committed Protocol III block CANNOT be constructed post-draft (it precedes Phase 0). Amendment 1 explicitly references "Protocol III committed targets" and "Protocol III committed format" — the diagnosis is checked against a pre-fixed list, not a post-hoc rationalization.

---

### Composite Score Summary

| Variation | Axis | Essential | Recommended | Aspirational | **Total** | Golden | C-36 | C-37 | Protocol III |
|-----------|------|-----------|-------------|--------------|-----------|--------|------|------|:------------:|
| V-01 | Lifecycle emphasis | 50 | 30 | 18 | **98** | YES | PASS | FAIL | NO |
| V-02 | Output format | 50 | 30 | 18 | **98** | YES | FAIL | PASS | NO |
| V-03 | Inertia framing | 50 | 30 | 16 | **96** | YES | FAIL | FAIL | YES (above ceiling) |
| V-04 | V-01 + V-02 | 50 | 30 | 20 | **100** | YES | PASS | PASS | NO |
| V-05 | Full synthesis | 50 | 30 | 20 | **100** | YES | PASS | PASS | YES (above ceiling) |

**Rank**: V-04 = V-05 (100) > V-01 = V-02 (98) > V-03 (96)

---

### Excellence Signals

**From V-04 / V-05 (top score, 100/100):**

1. **C-36 + C-37 synthesis is the v11 ceiling** — Neither criterion alone is sufficient for a perfect aspirational score. V-01 passes C-36 but not C-37 (−2); V-02 passes C-37 but not C-36 (−2). V-04 achieves the minimum synthesis. No single-axis variation can reach 100 at v11.

2. **Protocol III creates an above-ceiling temporal separation** (V-05 only, C-38 candidate) — Pre-committing the positive search space targets and per-category verification format before Phase 0 closes the post-draft rationalization window at the lifecycle level, not just at the instruction level. The structural asymmetry argument names both sides: a framework introduced inline at Amendment 1 CAN be shaped by the draft; a pre-committed Protocol III block CANNOT be written post-draft because it precedes Phase 0. Amendment 1 referencing "Protocol III committed targets" creates an auditable pointer to a pre-fixed list. This is new behavior V-03 and V-05 share but V-04 lacks — the C-38 candidate.

3. **V-03 isolates Protocol III cleanly** — Protocol III produces its above-ceiling behavior independently of C-36 and C-37 (V-03 fails both v11 ceiling criteria, scoring 96). This confirms Protocol III is a genuinely distinct signal, not confounded with C-36/C-37 synthesis.

**Scorecard prediction accuracy**: All five scores match the design rationale exactly. V-01: C-36 PASS, C-37 FAIL (98). V-02: C-36 FAIL, C-37 PASS (98). V-03: both FAIL, Protocol III above ceiling (96). V-04: both PASS, no Protocol III (100). V-05: both PASS, Protocol III (100).

---

### v12 Rubric Signal

- C-36 and C-37 are now confirmed terminal aspirational ceilings at v11 — both pass in V-04/V-05.
- Protocol III is the C-38 candidate for v12: pre-committed self-diagnosis framework lifecycle position (before Phase 0, not inline at Amendment 1). Fires in both V-03 and V-05.
- v11 is **not** the terminal rubric — Protocol III produces above-ceiling behavior requiring a new criterion.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Protocol III pre-commits positive search space targets and per-category verification format before Phase 0 -- creates auditable temporal separation between target-declaration event (pre-Phase 0, no draft exists) and target-application event (Amendment 1 execution); Amendment 1 references Protocol III committed targets rather than introducing them inline, closing the post-draft rationalization window at the lifecycle level", "C-36 and C-37 must be combined in a single variation to reach the v11 aspirational ceiling of 100/100 -- neither sub-phase canonical naming nor weakness-specific per-row reasoning alone achieves a perfect aspirational score; V-04 is the minimum synthesis and the first variation to hit 100 at v11"]}
```
