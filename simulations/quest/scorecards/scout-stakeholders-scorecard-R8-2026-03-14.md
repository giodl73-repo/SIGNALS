## /quest:score — scout-stakeholders — Round 8 — v8 Rubric (max 175)

---

### Criterion-by-Criterion Evaluation

#### Essential Criteria (C-01 through C-05 — 12 pts each)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|:----:|:----:|:----:|:----:|:----:|
| C-01 CODEOWNERS fallback | PASS | PASS | PASS | PASS | PASS |
| C-02 Power/Interest grid | PASS | PASS | PASS | PASS | PASS |
| C-03 Veto risks ranked | PASS | PASS | PASS | PASS | PASS |
| C-04 Champion + concrete action | PASS | PASS | PASS | PASS | PASS |
| C-05 Comms strategy per quadrant | PASS | PASS | PASS | PASS | PASS |

**Evidence notes:**
- C-01: All variations check CODEOWNERS, extract from invocation string if absent, ask one question, and carry FAIL_SILENT_INFERENCE or equivalent prohibition. V-03 uses coaching register ("Don't try to guess") but the gate is structurally present.
- C-03: All variations carry the `| Rank | Stakeholder | Probability | Impact | Mitigation |` table with probability-order instruction. V-03's coaching voice says "most likely first" with the same column structure.

**Essential subtotal: 60/60 for all five variations.**

---

#### Recommended Criteria (C-06 through C-08 — 10 pts each)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|:----:|:----:|:----:|:----:|:----:|
| C-06 Conflict identification | PASS | PASS | PASS | PASS | PASS |
| C-07 Role framing (3 roles separated) | PASS | PASS | PASS | PASS | PASS |
| C-08 Critical-path gatekeepers | PASS | PASS | PASS | PASS | PASS |

**Evidence notes:**
- C-06: All carry "at least two structural conflicts, each with both named parties and nature of tension."
- C-07: All separate Strategy / UX / PM into distinct phases — including V-03 (Phase 1: Strategy lens, Phase 2: UX lens, Phase 3: PM lens).
- C-08: All carry `[CRITICAL PATH -- lead time: X]` tagging with timing-requirement enforcement.

**Recommended subtotal: 30/30 for all five variations.**

---

#### Aspirational Criteria (C-09 through C-25 — 5 pts each)

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|:----:|:----:|:----:|:----:|:----:|
| C-09 | Amendment phase | PASS | PASS | PASS | PASS | PASS |
| C-10 | NOT-doing framing | PASS | PASS | PASS | PASS | PASS |
| C-11 | Source-tracking column | PASS | PASS | PASS | PASS | PASS |
| C-12 | Amendment loop + update mandate | PASS | PASS | PASS | PASS | PASS |
| C-13 | Prefilled Frame Types in comms | PASS | PASS | PASS | PASS | PASS |
| C-14 | Named failure modes inline | PASS | PASS | **FAIL** | PASS | PASS |
| C-15 | Reversed sequence (Strategy→UX→PM) | PASS | **FAIL** | PASS | **FAIL** | PASS |
| C-16 | Amendment before/after pair | PASS | PASS | **FAIL** | PASS | PASS |
| C-17 | FAIL saturation at every gate | PASS | PASS | **FAIL** | PASS | PASS |
| C-18 | Inertia structural elevation (3 positions) | PASS | PASS | **FAIL** | PASS | PASS |
| C-19 | Frame Type prefill as distinct step | PASS | PASS | PASS | **FAIL** | PASS |
| C-20 | Inertia chain prefill-stage binding | PASS | PASS | **FAIL** | **FAIL** | PASS |
| C-21 | Amendment example prefill round-trip | PASS | PASS | **FAIL** | **FAIL** | PASS |
| C-22 | Amendment mandate structural enumeration | PASS | PASS | **FAIL** | **FAIL** | PASS |
| C-23 | Role label heading binding | PASS | PASS | **FAIL** | PASS | PASS |
| C-24 | Amendment mandate inline prohibition | PASS | PASS | **FAIL** | PASS | PASS |
| C-25 | Veto risk mitigation per entry | PASS | PASS | **FAIL** | PASS | PASS |

**Detailed evidence by variation:**

---

**V-01 — Phase-Transition Confirmation Gates**

All 17 aspirational criteria pass. Key evidence:

- **C-15**: Phase 1 = Strategy (Step 1a/1b/1c), Phase 2 = UX, Phase 3 = PM. Explicit "Run Phase 1 first" mandate present.
- **C-17**: New transition gates carry FAIL_INCOMPLETE_PHASE1 and FAIL_INCOMPLETE_PHASE2, extending saturation without displacing any existing label. Every step and gate has a named failure mode.
- **C-23**: Both new gate headings carry role labels ("Phase 1 -> Phase 2 Transition Gate -- PM role", "Phase 2 -> Phase 3 Transition Gate -- PM role"). All prior headings carry roles unchanged from V-01 R7.
- **C-24**: Amendment mandate contains "-- no observation without revision" inline after the target list.
- **C-25**: Step 4 table has Mitigation column; FAIL_NO_MITIGATION is present at the veto risk step.

Aspirational: **85/85**

---

**V-02 — Role Sequence: UX-First**

- **C-15 FAIL**: Phase 1 = UX (segment analysis), Phase 2 = Strategy (conflict + inertia + critical-path). This is UX → Strategy → PM, which inverts the required Strategy-first ordering. Grid-first is not the issue; analysis-role-first is. The variation correctly isolates this single failure.
- **C-17 PASS**: All steps carry FAIL labels — the gate positions for FAIL labels are within numbered steps, not between phases, so UX-first ordering doesn't disrupt label coverage.
- **C-23 PASS**: Phase 1 heading carries "-- UX role", Phase 2 "-- Strategy role", all sub-steps carry role labels. V-02's heading format is identical to V-01's aside from phase ordering.
- **C-24 PASS**: Amendment mandate in Step 8 carries "-- no observation without revision" inline. V-02 confirms C-24 is independently satisfiable with PM-first (not Strategy-first) mandate position.
- **C-25 PASS**: FAIL_NO_MITIGATION at Step 4 with Mitigation column intact.

Aspirational: **80/85** (−C-15)

---

**V-03 — Coaching Voice**

This variation tests whether advisory/coaching register disrupts formal structural criteria. Ten aspirational criteria fail.

- **C-14 FAIL**: Coaching register replaces every FAIL label with "Watch out for" / "If you can only name one party..." / "A risk without a mitigation is an observation, not a plan" — none are formally named inline failure labels. Two named labels required; zero present.
- **C-15 PASS** *(finding — design predicted failure)*: Phase 1 is "Finding the structural conflicts (Strategy lens)", Phase 2 is "User segment analysis (UX lens)", Phase 3 is "Building the Power/Interest grid (PM lens)". The sequence is correctly Strategy → UX → PM, and "Start here, before you build any grid or table" (Phase 1 opening) explicitly mandates the order. C-15's pass condition is structural ordering — advisory framing does not invalidate it. **C-15 survives coaching voice when phase sequence is correct.**
- **C-16 FAIL**: Step 8 shows only a single coaching-form amendment example ("Here's what a good amendment looks like:"). No adjacent "Bad form / Correct form" labeled pair is present.
- **C-17 FAIL**: No formal FAIL labels exist anywhere in the variation. C-17 requires every execution step to carry at least one named failure mode; coaching register replaces all of them.
- **C-18 FAIL**: The inertia sub-section exists as an informal heading ("The stakeholders who benefit from the current approach") within Phase 1, not as a formally numbered sub-step. C-18's first requirement is "a dedicated sub-step in the strategy phase." An informal sub-heading within a phase does not constitute a formal sub-step. The other two positions (grid [INERTIA] tag, displacement-acknowledgment prefill assignment) are present, but all three must be present. Three-position elevation fails.
- **C-19 PASS**: Step 6a ("Assigning Frame Types before writing messages") is a distinct labeled section before Step 6b. The prefill table is present as a required constraint block before row population. Advisory language does not disqualify it as a distinct step.
- **C-20 FAIL**: Step 6a contains "Make that assignment here, before you write the row content" for inertia stakeholders but no FAIL_MISSING_DISPLACEMENT_PREFILL label. C-20 requires the inline failure label at the prefill gate.
- **C-21 FAIL**: C-21 depends on C-16, which fails. The coaching amendment example shows a prefill round-trip structurally, but the criterion is not satisfiable without C-16.
- **C-22 FAIL**: The amendment mandate says "update the relevant table or list" — generic, does not enumerate "Step 6a prefill" as a structural target. C-22 requires explicit enumeration.
- **C-23 FAIL**: Phase headings carry "(Strategy lens)" / "(UX lens)" / "(PM lens)" — acceptable as role identifiers — but Steps 6a, 6b, and 8 have headings without role labels. "Step 6a -- Assigning Frame Types before writing messages" and "Step 8 -- Amendment pass" omit role labels. Any heading missing a role label = FAIL.
- **C-24 FAIL**: The amendment execution instruction reads "The goal is a revision, not an observation" — separated from the mandate sentence ("update the relevant table or list -- don't just note it"). C-24 requires the prohibition clause embedded directly in the mandate sentence. The prohibition exists but is in a separate sentence, not inline in the mandate.
- **C-25 FAIL**: The veto risk table has a Mitigation column and the text says "include... a mitigation approach," but FAIL_NO_MITIGATION as a formal gate label is absent. C-25 requires the FAIL label at the step.

Aspirational passes: C-09, C-10, C-11, C-12, C-13, C-15, C-19 = **35/85**

---

**V-04 — UX-First + Steps 6a/6b Merged**

This variation tests two axes simultaneously: UX-first (−C-15) and merged Step 6 with labeled sub-parts (±C-19 and cascade).

- **C-15 FAIL**: UX-first ordering (Phase 1 = UX, Phase 2 = Strategy). Same as V-02.
- **C-19 FAIL** *(C-19 determination confirmed)*: "Step 6 -- Frame Type assignment and communication table -- PM role" is a single numbered step with "Part A: prefill" and "Part B: populate" within it. C-19 requires "a standalone prefill table... as a *distinct step*." Part A shares a step number with Part B. A sub-part within a step does not satisfy "distinct step." FAIL.
- **C-20 FAIL** (cascade from C-19): C-20 is not satisfiable if C-19 is absent.
- **C-21 FAIL** (cascade from C-19): C-21 is not satisfiable if C-16 or C-19 is absent. C-16 is present; C-19 is absent.
- **C-22 FAIL** (cascade from C-19): C-22 is not satisfiable if C-19 is absent.
- **C-23 PASS**: All step headings in V-04 carry role labels — including "Step 6 -- Frame Type assignment and communication table -- PM role". The merged step retains the role binding.
- **C-24 PASS** *(key finding)*: Step 8 amendment mandate reads "For every amendment, update the affected structural target (grid, veto list, comms rows, or Step 6 Part A prefill assignments) -- no observation without revision." The phrase "no observation without revision" is embedded inline in the mandate sentence. C-24 passes independently of C-19: the mandate-level prohibition survives the 6a/6b merge because it references "Step 6 Part A" directly and the prohibition clause is present.
- **C-25 PASS**: FAIL_NO_MITIGATION present at Step 4.

Aspirational passes: C-09, C-10, C-11, C-12, C-13, C-14, C-16, C-17, C-18, C-23, C-24, C-25 = **60/85**

---

**V-05 — All 25 + Champion Depth Scoring + Champion Durability**

All 17 aspirational criteria pass. Three additions.

- **C-17 PASS** (extended): FAIL_NO_DURABILITY fires at Step 5 Part C when a champion plan has a single named person with no succession or deterioration signal. This is a new gate covering the new durability sub-step. C-17 coverage is complete across all steps including the new champion sub-steps.
- **C-21 PASS**: Correct-form amendment example in Step 8 includes "Step 6a prefill updated -- Keep Satisfied Frame Type reassigned from `value-capture` to `compliance-alignment`; Step 6b row revised accordingly" — prefill round-trip is present.
- **C-24 PASS**: Amendment mandate reads "-- no observation without revision" inline, and update targets list now includes "champion depth scores and durability assessments" — the mandate expands to cover the new amendment-eligible targets without losing the prohibition clause.

**New amendment-eligible target**: Champion depth scores and durability assessments are explicitly listed as update targets in the Step 8 mandate. The correct-form amendment example demonstrates a champion score revision ("Champion depth scoring updated -- [Primary Champion] Proximity score revised from 4 to 3...") as an amendment-eligible finding. This extends C-21 structurally without replacing the prefill round-trip.

Aspirational: **85/85**

---

### Composite Scores

| Variation | Essential | Recommended | Aspirational | **Total** | vs Expected | Golden? |
|-----------|:---------:|:-----------:|:------------:|:---------:|:-----------:|:-------:|
| V-01 — Phase-transition gates | 60 | 30 | 85 | **175/175** | 175 ✓ | YES |
| V-02 — UX-first | 60 | 30 | 80 | **170/175** | ~170 ✓ | YES |
| V-03 — Coaching voice | 60 | 30 | 35 | **125/175** | ~120 (+5) | YES |
| V-04 — UX-first + merged step 6 | 60 | 30 | 60 | **150/175** | ~155-160 (−10) | YES |
| V-05 — All 25 + champion depth/durability | 60 | 30 | 85 | **175/175** | 175+ ✓ | YES |

**Ranking**: V-01 = V-05 (175) > V-02 (170) > V-04 (150) > V-03 (125)

All five variations clear the golden threshold (≥ 80). All pass every essential criterion.

---

### Score vs Expected — Discrepancies

**V-03 scores 125, not ~120** (+5 gap): C-15 passes with coaching voice. Phase ordering is structurally Strategy → UX → PM with explicit advisory mandates ("Start here, before you build any grid or table"). C-15 measures structural sequence, not imperative register. Coaching voice does not cause C-15 to fail when the phase order is correct. This is a confirmed new finding.

**V-04 scores 150, not ~155-160** (−5 to −10 gap): C-19 fails, cascading to C-20, C-21, and C-22 (−20 pts). The design expected C-19 as uncertain (??); it resolves to FAIL. Part A within a shared step number is not a "distinct step." The cascade is clean — C-24 and C-23 both survive the merge, confirming mandate-level criteria are not coupled to step-number structure.

---

### Structural Properties Confirmed by Round 8

1. **C-26 confirmed as independently satisfiable** (V-01): Phase-gate prerequisite confirmation is an additive axis — two between-phase gates, each with a prerequisite checklist and FAIL label, extend C-17 coverage without displacing any prior criterion. V-01 is V-01 R7 verbatim plus the two gates. Perfect score unchanged.

2. **C-19 "distinct step" boundary resolved** (V-04): A labeled sub-part within a shared step number does not satisfy "distinct step." The step number is the boundary — Step 6a and Step 6b are distinct steps; Part A and Part B within Step 6 are not. This resolves the v5 candidate's ?? definitively.

3. **C-24 is decoupled from C-19** (V-04): The amendment mandate inline prohibition survives the 6a/6b merge. V-04 passes C-24 while failing C-19 — the mandate sentence contains "no observation without revision" regardless of prefill step structure.

4. **C-15 survives coaching voice** (V-03): Advisory ordering language satisfies C-15's explicit-ordering requirement when the structural phase sequence is Strategy → UX → PM. "Start here, before you build any grid or table" is sufficient.

5. **C-18 requires a formal sub-step, not an informal sub-heading** (V-03): V-03's "The stakeholders who benefit from the current approach" is a sub-heading within Phase 1, not a formally numbered sub-step. C-18's first requirement (dedicated sub-step) fails with informal headings.

6. **Champion depth scoring and durability are additive without interference** (V-05): Three new champion additions (Part B scoring table, Part C durability fields, extended amendment example) carry all 25 existing criteria unaffected. FAIL_NO_DURABILITY extends C-17 saturation. The amendment mandate expands to include champion targets without losing the prohibition clause.

---

### Excellence Signals from Top-Scoring Variations

**V-01 — Phase-gate prerequisite confirmation pattern**

The transition gate structure creates an explicit pre-flight checklist between phases. Each gate enumerates required prior-phase outputs as bullet points, attaches a FAIL label naming the blocked transition, and explains *why* the gate matters (e.g., "Phase 2's NOT-doing statements depend on the displacement vocabulary established in Step 1b"). This is not just a gate — it's a forward-dependency explanation. The gate teaches the user why sequence matters, not just that it matters.

**V-05 — Champion scoring cascade into amendment loop**

Champion depth scoring becomes a first-class amendment-eligible target. When new stakeholders surface in the amendment pass, champion proximity scores must be updated if the new stakeholder is in a required audience the champion cannot reach. The correct-form amendment example demonstrates this: "Champion depth scoring updated -- [Primary Champion] Proximity score revised from 4 to 3 (Platform Security is a required audience and [Primary Champion] has no direct relationship there; secondary champion candidate identified...)." This creates a closed loop: Phase 1 conflict discovery → amendment pass → champion score revision → secondary champion identification. The champion durability fields (SPOF risk, succession, deterioration signal) turn champion identification from a point-in-time action into an ongoing risk posture.

---

### New Patterns Surfaced — v9 Candidates

**C-26 candidate A — Phase-gate prerequisite confirmation** (from V-01)  
A gate that lists required prior-phase outputs as an explicit prerequisite checklist with a FAIL label at the transition. Pass condition: each between-phase gate names the required prior outputs as enumerated items, names the FAIL label, and states why the dependent phase cannot be completed without the prior-phase vocabulary. A gate with a FAIL label but no prerequisite enumeration = FAIL. V-01 demonstrates with FAIL_INCOMPLETE_PHASE1 and FAIL_INCOMPLETE_PHASE2. Independently satisfiable — V-01 confirms it adds to a perfect base without changing any existing criterion.

**C-26 candidate B — Champion quantification depth** (from V-05)  
A scoring table per champion covering authority / proximity / commitment (each 1–5), a composite score (max 15), and an explicit threshold below which a champion is reclassified as supporting evidence (composite < 9). FAIL_NO_DURABILITY fires when a champion plan has a single named person with no succession or deterioration signal. Independently satisfiable — V-05 adds Part B and Part C without affecting any prior criterion.

**C-27 candidate — Champion durability** (from V-05)  
Per-champion fields for single-point-of-failure risk, succession candidate (who and what activation would require), and deterioration signal (what early sign indicates declining commitment). Independently satisfiable and orthogonal to champion scoring — a variation could carry one without the other.

---

### Golden Variation

**V-05 is the Round 8 golden variation.** It scores 175/175 (tied with V-01) but extends two new v9 candidate axes (champion quantification and durability) and demonstrates the champion-to-amendment-loop cascade pattern. V-01 is the additive-axis proof of C-26A and should be retained as the v9 C-26A reference.

---

```json
{"top_score": 175, "all_essential_pass": true, "new_patterns": ["Phase-gate prerequisite confirmation: between-phase gates enumerate required prior-phase outputs as a checklist with FAIL label at transition (C-26A candidate, confirmed independently satisfiable by V-01)", "Champion quantification depth: authority/proximity/commitment scoring (1-5 each), composite max 15, threshold classification below 9 as supporting evidence, FAIL_NO_DURABILITY at durability gate (C-26B candidate from V-05)", "Champion durability: per-champion SPOF risk, succession candidate, and deterioration signal fields, amendment-eligible target in Step 8 mandate (C-27 candidate from V-05)", "C-15 survives coaching voice: advisory ordering language ('Start here, before you build any grid or table') satisfies explicit-ordering requirement when structural phase sequence is Strategy→UX→PM", "C-19 distinct-step boundary resolved: Part A within a shared step number fails 'distinct step' requirement; step number is the structural boundary", "C-24 decoupled from C-19: mandate inline prohibition survives 6a/6b merge — mandate sentence carries 'no observation without revision' independently of prefill step structure"]}
```
