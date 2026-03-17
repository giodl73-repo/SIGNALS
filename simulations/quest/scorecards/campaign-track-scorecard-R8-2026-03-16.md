## Quest Score — campaign-track / Round 8

**Rubric version**: v8 | **Max points**: 110 | **Variations**: V-01 through V-05

---

### Scoring Model

| Tier | Points each | Criteria |
|------|-------------|----------|
| Essential | 10 | C-01..C-05 (5 criteria) |
| Recommended | 5 | C-06..C-08 (3 criteria) |
| Aspirational | 3 | C-09..C-16, C-22..C-28 (15 criteria) |

**Baseline** (C-01..C-24, all five variations): `5×10 + 3×5 + 11×3 = 98`

New differential criteria: C-25, C-26, C-27, C-28 — 3 pts each, max +12.

---

### Criterion-by-Criterion Evaluation

#### Essential Criteria — all five PASS all five (50 pts each)

| Criterion | Evidence | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|----------|------|------|------|------|------|
| **C-01** Four-phase structure | Register→Plan→Status→Narrative labeled in all | PASS | PASS | PASS | PASS | PASS |
| **C-02** Artifact-per-phase discipline | strategy/roadmap/status/story each with write path; delta is Phase 3 sub-artifact, not a merged artifact | PASS | PASS | PASS | PASS | PASS |
| **C-03** Nine-namespace coverage table | Phase 3 Contract specifies all 9 rows with planned/collected/missing/zero_flag in all five | PASS | PASS | PASS | PASS | PASS |
| **C-04** Readiness verdict from enumerated set | 3-token set `READY\|NOT READY\|CONDITIONALLY READY` declared and constrained in all | PASS | PASS | PASS | PASS | PASS |
| **C-05** Narrative verdict with evidence | Phase 4 story.md contract: verdict_verb + hypothesis_mutation + echoes + 3 recommendations in all | PASS | PASS | PASS | PASS | PASS |

#### Recommended Criteria — all five PASS all three (15 pts each)

| Criterion | Evidence | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|----------|------|------|------|------|------|
| **C-06** Artifact write paths | All four phases + delta have `simulations/topic/{{topic}}-{artifact}-{{date}}.md` pattern | PASS | PASS | PASS | PASS | PASS |
| **C-07** Coverage ratio and readiness statement | `coverage_ratio: "X/N"` + `readiness_verdict` from 3-token set in Phase 3 Contract | PASS | PASS | PASS | PASS | PASS |
| **C-08** Cross-namespace signal balance | 9-row table with `zero_flag = "NO SIGNALS"` for uncovered namespaces in all | PASS | PASS | PASS | PASS | PASS |

#### Aspirational Criteria — C-09 through C-24 — all five PASS (33 pts each)

| Criterion | Evidence | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|----------|------|------|------|------|------|
| **C-09** Echo integration | `echoes: list; if none, ["NONE"]` fallback in Phase 4 Contract; Empty-State sets `echoes = ["NONE"]` | PASS | PASS | PASS | PASS | PASS |
| **C-10** Dual-session delta | Session Delta Contract with session_number, signals_added, verdict_before/after, verdict_changed in all | PASS | PASS | PASS | PASS | PASS |
| **C-11** Role-gated phases | Registrar/Planner/Analyst/Narrator each assigned to distinct phase with active-role header | PASS | PASS | PASS | PASS | PASS |
| **C-12** Explicit progression gates | GATE statements between all adjacent phases in all variations | PASS | PASS | PASS | PASS | PASS |
| **C-13** Empty-state as named section | `## Empty-State Handling / First Invocation (0 signals collected)` with per-phase per-role behavior | PASS | PASS | PASS | PASS | PASS |
| **C-14** Per-role prohibition lists | All four roles carry exactly 5 enumerated forbidden actions with named prohibited behaviors | PASS | PASS | PASS | PASS | PASS |
| **C-15** Typed output contracts per phase | Full-Phase Type Coverage Rule declared; all four phase contracts typed with integer/enumerated-string specs | PASS | PASS | PASS | PASS | PASS |
| **C-16** Terminal completion checklist | TERMINAL section with per-field PASS conditions; "re-run Phase X only" targeted re-run language; dashboard gated on all items | PASS | PASS | PASS | PASS | PASS |
| **C-22** Prohibition-count parity | Parity rule declared: "exactly 5 forbidden actions — no more, no fewer"; all four roles conform; count verifiable by inspection | PASS | PASS | PASS | PASS | PASS |
| **C-23** Full-phase type coverage | Rule: "All four phases have typed output contracts. No phase is exempt. Partial coverage fails." + all four contracts present | PASS | PASS | PASS | PASS | PASS |
| **C-24** Field-level terminal checklist | Terminal checklist uses per-field items (not per-phase): each checking a specific named field with its constraint and fail action | PASS | PASS | PASS | PASS | PASS |

**Baseline subtotal (C-01..C-24): 98 pts — all five**

---

#### New v8 Criteria — the differentiators

**C-25 — Two-pass delta update** | aspirational | behavior

Pass requires: Phase 3 Step B writes `verdict_after = "NOT YET REACHED"` as declared placeholder; named Post-Phase-4 update step overwrites with actual verdict_verb; terminal verdict_after item is order-dependent with "placeholder fails" language.

| Variation | Evidence | Result |
|-----------|----------|--------|
| **V-01** | Explicit `## Two-Pass Delta Rule` section; Phase 3 Step B "IMPORTANT — Two-pass protocol applies: Write verdict_after = 'NOT YET REACHED'" as declared placeholder; `## Post-Phase-4 Delta Update (Pass 2)` section; terminal item: "must reflect Phase 4 verdict_verb; placeholder 'NOT YET REACHED' fails after Phase 4 completes (unless Phase 4 verdict_verb is also 'NOT YET REACHED') / FAIL: re-run Phase 3 Step B after Phase 4 completes" | **PASS** |
| **V-02** | No two-pass protocol. Phase 3 Step B writes verdict_after in one pass using readiness_verdict or "NOT YET REACHED" as proxy. No Post-Phase-4 update section. Terminal item: bare enum check only, no order-dependent language | **FAIL** |
| **V-03** | No two-pass protocol. Step B says "verdict_after reflects Phase 4 narrative verdict; if Phase 4 has not yet run, use readiness_verdict from Step A or 'NOT YET REACHED'" — one-pass judgment call. No Post-Phase-4 update section. Terminal item: bare enum check only | **FAIL** |
| **V-04** | `## Two-Pass Delta Rule` section present; Phase 3 Step B "(Pass 1)" with "Set verdict_after = 'NOT YET REACHED' (placeholder — Phase 4 not yet run)"; `## Post-Phase-4 Delta Update (Pass 2)` section; terminal item with "placeholder fails after Phase 4" and "re-run Phase 3 Step B after Phase 4 completes (Pass 2)" | **PASS** |
| **V-05** | All V-04 elements plus terminal closing note: "The verdict_after item is the only order-dependent item: verify it last, after Phase 4 and the Post-Phase-4 Delta Update have both completed" | **PASS** |

---

**C-26 — Dual-contract active-role annotation** | aspirational | format

Pass requires: Phase 3 header names both Phase 3 Contract AND Session Delta Contract; normative rule that single-contract header is a structural defect.

| Variation | Evidence | Result |
|-----------|----------|--------|
| **V-01** | Phase 3 header: `*Analyst active. Exactly 5 forbidden actions apply. Phase 3 Contract governs output.*` — single-contract only. No Dual-Contract Annotation Rule section | **FAIL** |
| **V-02** | `## Dual-Contract Annotation Rule` section with normative language: "Naming one contract and omitting others is a structural defect." Phase 3 header: `*Phase 3 Contract governs status.md. Session Delta Contract governs delta.md.*` — both contracts named | **PASS** |
| **V-03** | Phase 3 header: `*Analyst active. Exactly 5 forbidden actions apply. Phase 3 Contract governs output.*` — single-contract only. No Dual-Contract Annotation Rule section | **FAIL** |
| **V-04** | `## Dual-Contract Annotation Rule` section with normative language; Phase 3 header names both contracts explicitly | **PASS** |
| **V-05** | `## Dual-Contract Annotation Rule` section + Phase 3 header names both; "Both contracts are active at this phase. Both artifacts are required to satisfy the Phase 3 postcondition." | **PASS** |

---

**C-27 — Conjunction progression gate** | aspirational | behavior

Pass requires: Phase 3 postcondition is `status.md AND delta.md BOTH present`; explicit statement that writing status.md alone does not satisfy the postcondition.

| Variation | Evidence | Result |
|-----------|----------|--------|
| **V-01** | Phase 3 postcondition: "status.md present with 9 rows, integer fields, readiness_verdict assigned from enumerated set." GATE on status.md only — no conjunction | **FAIL** |
| **V-02** | Phase 3 postcondition: "status.md present with 9 rows..." — status.md only gate. No conjunction | **FAIL** |
| **V-03** | Phase 3 postcondition: "status.md AND delta.md are BOTH present and satisfy their respective contracts. Writing status.md alone does not satisfy this postcondition. delta.md must be present with all Session Delta Contract fields populated." GATE: "BOTH status.md AND delta.md satisfy their contracts" | **PASS** |
| **V-04** | Phase 3 postcondition: "status.md AND delta.md are BOTH present, each satisfying their respective contracts. Status.md alone does not satisfy this postcondition." GATE uses "BOTH" | **PASS** |
| **V-05** | Phase 3 postcondition: "status.md AND delta.md are BOTH present, each satisfying their respective contracts. Writing status.md alone does not satisfy this postcondition." GATE: "BOTH status.md AND delta.md satisfy their contracts" | **PASS** |

---

**C-28 — Empty-list sentinel type-tightening** | aspirational | correctness

Pass requires: terminal checklist item for signals_added explicitly rejects string "NONE" sentinel and requires empty list []; empty-state section contrasts list-typed vs string-typed "NONE" fields.

| Variation | Evidence | Result |
|-----------|----------|--------|
| **V-01** | Terminal item: `signals_added: list present ([] permitted if no signals added this session)` — permits [] but does not explicitly reject string "NONE" | **FAIL** |
| **V-02** | Terminal item: `signals_added: list present` — no type guidance, no "NONE" rejection | **FAIL** |
| **V-03** | Terminal item: `signals_added: list present` — no "NONE" rejection | **FAIL** |
| **V-04** | Terminal item: `signals_added: list present ([] permitted)` — does not explicitly reject string "NONE" sentinel (per rubric notes for V-04: "Misses: C-28 (signals_added terminal item says '[] permitted' but does not explicitly reject string 'NONE' sentinel)") | **FAIL** |
| **V-05** | Session Delta Contract: "empty list [] if no signals added -- string 'NONE' is not a valid value"; Terminal: `signals_added: list present ([] permitted; absent field or string 'NONE' fails -- the empty-list type [] is required, not the string sentinel)`; Empty-State: `signals_added = [] (empty list -- NOT the string "NONE")`; contrast note: `verdict_before = "NONE" (string sentinel for first session -- this field is string-typed, unlike signals_added which is list-typed)` | **PASS** |

---

### Composite Scores

| Criterion | Pts | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-----|------|------|------|------|------|
| C-01..C-05 (essential) | 10×5=50 | 50 | 50 | 50 | 50 | 50 |
| C-06..C-08 (recommended) | 5×3=15 | 15 | 15 | 15 | 15 | 15 |
| C-09..C-16, C-22..C-24 (aspirational) | 3×11=33 | 33 | 33 | 33 | 33 | 33 |
| **Baseline subtotal** | **98** | **98** | **98** | **98** | **98** | **98** |
| C-25 Two-pass delta | 3 | +3 | — | — | +3 | +3 |
| C-26 Dual-contract annotation | 3 | — | +3 | — | +3 | +3 |
| C-27 Conjunction gate | 3 | — | — | +3 | +3 | +3 |
| C-28 Empty-list type-tightening | 3 | — | — | — | — | +3 |
| **TOTAL** | **/110** | **101** | **101** | **101** | **107** | **110** |
| **%** | | 91.8% | 91.8% | 91.8% | 97.3% | 100% |

---

### Ranking

| Rank | Variation | Score | New Criteria |
|------|-----------|-------|-------------|
| 1 | **V-05** | **110/110** | C-25, C-26, C-27, C-28 all pass |
| 2 | **V-04** | **107/110** | C-25, C-26, C-27 pass; C-28 missing |
| 3 (tie) | **V-01** | **101/110** | C-25 only; strongest lifecycle enforcement |
| 3 (tie) | **V-02** | **101/110** | C-26 only; weakest single-axis (format, no behavior) |
| 3 (tie) | **V-03** | **101/110** | C-27 only; strongest behavioral enforcement among single-axis |

**Note on the three-way tie (V-01/V-02/V-03)**: Rubric scoring gives equal points for any single new criterion. The qualitative ordering V-03 > V-01 ≥ V-02 from the variation summary reflects behavioral enforcement strength but does not resolve through rubric arithmetic alone. A future rubric revision could differentiate by weighting behavioral criteria over format criteria.

**Open question resolved**: C-25 requires both the named Post-Phase-4 update section AND the order-dependent terminal item. V-01 has both. This means a minimal variation with only the terminal item would score C-25 as PARTIAL (borderline) — the named section is what makes it unambiguous. V-04 and V-05 both confirm this interpretation.

---

### Predicted vs Actual Leaderboard

| Predicted | Actual |
|-----------|--------|
| V-05 > V-04 > V-03 > V-01 ≥ V-02 | V-05 > V-04 > V-01 = V-02 = V-03 (3-way tie) |

The predicted ordering was qualitatively correct at the top (V-05, V-04) but the single-axis trio ties under rubric arithmetic. The predicted V-03 > V-01 > V-02 ordering is a behavioral quality judgment not captured by binary PASS/FAIL per criterion.

---

### Excellence Signals from V-05

Three patterns in V-05 are structurally distinct from C-25 through C-28 and could discriminate future variations:

**E-01 — Type-field contrast annotation**
V-05's Empty-State section explicitly contrasts list-typed fields (`signals_added = [] (empty list -- NOT the string "NONE")`) with string-typed sentinel fields (`verdict_before = "NONE" (string sentinel for first session -- this field is string-typed, unlike signals_added which is list-typed)`) in the same section, with inline comments explaining the type distinction. C-28 covers rejecting "NONE" in signals_added, but the explicit contrast preventing over-application of the rejection rule to verdict_before is new. A variation that adds the rejection without the contrast creates a new failure mode.

**E-02 — Terminal order-dependency declaration**
V-05 closes the terminal checklist with: "The verdict_after item is the only order-dependent item: verify it last, after Phase 4 and the Post-Phase-4 Delta Update have both completed." This makes the checklist execution order explicit as a closing normative statement — distinct from C-25's two-pass protocol (which governs write order) and C-16's per-item gating. It addresses the checklist verification order, not just the artifact write order.

**E-03 — Execution-site constraint injection**
V-05's Phase 3 Step B injects type constraints directly at the execution site: `signals_added: list ([] if none -- string "NONE" is invalid)` appears in the Step B instructions, not only in the Session Delta Contract definition. This pattern — repeating key type constraints from the contract section at the execution instructions — prevents a model from executing Step B without having the constraint visible, even if it didn't read back to the contract section. This is distinct from the contract definition (C-28) and from the terminal item (also C-28).

---

```json
{"top_score": 110, "all_essential_pass": true, "new_patterns": ["Type-field contrast annotation: Empty-State section explicitly contrasts list-typed fields requiring [] with string-typed sentinel fields where string 'NONE' is valid, preventing over-application of the type-rejection rule across fields with structurally different types", "Terminal order-dependency declaration: a closing note in the terminal checklist names the single order-dependent verification item and instructs verify-last ordering, making temporal dependencies explicit at the checklist level itself rather than only at the artifact write level", "Execution-site constraint injection: key type constraints from contract definitions are repeated inline at the Phase 3 Step B execution instructions, bringing constraint visibility to the execution site without requiring the model to navigate back to the contract section"]}
```
