## Round 17 — topic-plan Scoring (v17 rubric, C-52 + C-53 new)

---

### Scoring Framework Recap

| Tier | Count | Weight | Max pts |
|------|-------|--------|---------|
| Essential | 5 | 60/5 = 12 pts each | 60 |
| Recommended | 3 | 30/3 = 10 pts each | 30 |
| Aspirational | 45 | 10/45 = 0.222 pts each | 10 |
| **Total** | **53** | | **100** |

---

### V-01 — Output Format Axis

**Gate-0 form:** `GATE-0 PASS THRESHOLD: 8 declared schemas + 3 structural checks = 11 items total; passes when all 11 items confirmed; blocked by any single STOP result.`

**C-52 axis:** PASS — arithmetic formula (`M + K = N`) appears inside the threshold annotation field; reading the THRESHOLD line alone reveals the derivation.

**C-53 axis:** FAIL — §5b remains an inline Phase 5 instruction; no Gate-0 check item; cannot be detected absent by Gate-0.

| Criterion | Result | Note |
|-----------|--------|------|
| C-01 | PASS | Strategy.md cited |
| C-02 | PASS | All 9 namespaces assessed |
| C-03 | PASS | NEW/PRIOR split, strategy date named |
| C-04 | PASS | ADD/REMOVE/REPRIORITIZE typed |
| C-05 | PASS | YES/NO/REVISED gate present |
| C-06 | PASS | Artifact filenames in proposal rows |
| C-07 | PASS | Before/After diff present |
| C-08 | PASS | Per-row inertia justification |
| C-09–C-42 | PASS | Inherits R16 V-05 structure |
| C-43 | PASS | Cell-exhaustive gate enumeration |
| C-44 | PASS | "Gate-0" label in block header |
| C-45 | PASS | Schema-gate checklist atomic per schema |
| C-46 | PASS | "passes when all 11 confirmed" present |
| C-47 | PASS | Condition line enumerates all items by label |
| C-48 | PASS | "blocked by any single STOP result" |
| C-49 | PASS | Attestation clause present |
| C-50 | PASS | Semantic category grouping on condition line |
| C-51 | PASS | Pass+halt co-located in single GATE-0 PASS THRESHOLD field |
| C-52 | **PASS** | Arithmetic (`8 + 3 = 11`) embedded in threshold field |
| C-53 | **FAIL** | §5b not a schema block; no [A6] check item |

**Essential:** 5/5 | **Recommended:** 3/3 | **Aspirational:** 44/45 (C-53 fails)

**Score:** `(5/5 × 60) + (3/3 × 30) + (44/45 × 10)` = 60 + 30 + **9.78** = **99.78**

---

### V-02 — Lifecycle Emphasis Axis

**Gate-0 form:** §5b promoted to Check [A6]; threshold bare-count: `passes when all 12 items confirmed` — arithmetic in a separate decomposition block.

**C-52 axis:** FAIL — reading the THRESHOLD annotation alone gives "passes when all 12 items confirmed" with no arithmetic; M + K = N lives in a sibling field.

**C-53 axis:** PASS — §5b is [A6] in Phase −1 schema inventory; participates in Gate-0 count and checklist.

| Criterion | Result | Note |
|-----------|--------|------|
| C-01–C-05 | PASS | Core behavior unaffected by lifecycle axis |
| C-06–C-08 | PASS | Evidence/diff/inertia present |
| C-09–C-42 | PASS | Inherits R16 structure |
| C-43 | PASS | §5b now named cell in gate |
| C-44 | PASS | Gate-0 header label present |
| C-45 | PASS | 12-item checklist atomic per schema (including [A6]) |
| C-46 | PASS | "passes when all 12 items confirmed" |
| C-47 | PASS | All 12 item labels in condition line |
| C-48 | PASS | Halt declaration present |
| C-49 | PASS | Attestation clause present |
| C-50 | PASS | Semantic grouping maintained |
| C-51 | PASS | Pass+halt co-located; arithmetic separation doesn't break co-location of pass+halt |
| C-52 | **FAIL** | Threshold annotation is bare count; derivation arithmetic is in a separate field |
| C-53 | **PASS** | §5b is [A6] schema block; Gate-0 item present |

**Essential:** 5/5 | **Recommended:** 3/3 | **Aspirational:** 44/45 (C-52 fails)

**Score:** `60 + 30 + (44/45 × 10)` = **99.78**

---

### V-03 — Phrasing Register Axis

**Gate-0 form:** Arithmetic in threshold annotation (C-52 satisfied); hypothesis-test opening style; C-49 explicitly absent.

**C-52 axis:** PASS — arithmetic embedded in threshold annotation.

**C-53 axis:** FAIL — §5b inline only.

**C-49 axis:** FAIL — attestation clause absent (phrasing-register axis strips the self-containment declaration).

| Criterion | Result | Note |
|-----------|--------|------|
| C-01–C-05 | PASS | Core behavior unaffected |
| C-06–C-08 | PASS | Present |
| C-09–C-42 | PASS | Inherited |
| C-43–C-48 | PASS | Gate structure sound |
| C-49 | **FAIL** | No attestation clause; explicitly absent per variation description |
| C-50 | PASS | Semantic grouping present |
| C-51 | PASS | Co-location present |
| C-52 | **PASS** | Arithmetic in threshold annotation |
| C-53 | **FAIL** | §5b inline instruction only |

**Essential:** 5/5 | **Recommended:** 3/3 | **Aspirational:** 43/45 (C-49, C-53 fail)

**Score:** `60 + 30 + (43/45 × 10)` = 60 + 30 + **9.56** = **99.56**

---

### V-04 — Combined Output + Lifecycle Axis

**Gate-0 form:** `GATE-0 PASS THRESHOLD: 9 declared schemas + 3 structural checks = 12 items total; passes when all 12 items confirmed; blocked by any single STOP result.` + §5b as [A6] in Phase −1 schema inventory.

**C-52 axis:** PASS — arithmetic (`9 + 3 = 12`) inside the threshold annotation field.

**C-53 axis:** PASS — §5b is a named schema block [A6]; participates in Gate-0, item count arithmetic, and condition-line conjunction.

| Criterion | Result | Note |
|-----------|--------|------|
| C-01–C-05 | PASS | Full behavioral compliance |
| C-06–C-08 | PASS | Evidence/diff/inertia present |
| C-09–C-42 | PASS | Structural requirements all met |
| C-43 | PASS | Cell-exhaustive; all mandatory columns named |
| C-44 | PASS | "Gate-0" in block header |
| C-45 | PASS | 12-item atomic checklist ([A1]–[A9] + [B] + [C] + [D]) |
| C-46 | PASS | "passes when all 12 items confirmed" |
| C-47 | PASS | All 12 item labels in condition line |
| C-48 | PASS | "blocked by any single STOP result" |
| C-49 | PASS | Attestation clause present |
| C-50 | PASS | Semantic category grouping on condition line |
| C-51 | PASS | Pass+halt in single GATE-0 PASS THRESHOLD field |
| C-52 | **PASS** | `9 declared schemas + 3 structural checks = 12 items total` inside threshold field |
| C-53 | **PASS** | §5b is [A6]; Gate-0 check item; N updated correctly |

**Essential:** 5/5 | **Recommended:** 3/3 | **Aspirational:** 45/45

**Score:** `60 + 30 + (45/45 × 10)` = **100.00**

---

### V-05 — Full Ceiling (C-43–C-53) + Role Sequence

**Gate-0 form:** V-04 structure + §5b phase-authorization note declares it runs **before §5 scope filtering**: phase authorization reads `§5b §5 §6 §7`. §5b evaluates against the full new-evidence set, not the scope-filtered subset.

**C-52 axis:** PASS — arithmetic inside threshold annotation (inherited from V-04).

**C-53 axis:** PASS — §5b is [A6]; participates in all gate structures (inherited from V-04).

**Role sequence addition:** §5b schema block's phase-authorization note explicitly declares positional precedence: runs before §5 (scope filter). This is structurally visible in [A6]'s block annotation.

| Criterion | Result | Note |
|-----------|--------|------|
| C-01–C-05 | PASS | Full behavioral compliance |
| C-06–C-08 | PASS | Evidence/diff/inertia present |
| C-09–C-42 | PASS | All met |
| C-43–C-51 | PASS | V-04 gate structure preserved |
| C-52 | **PASS** | Arithmetic in threshold annotation |
| C-53 | **PASS** | §5b as [A6] schema block |
| *Role sequence* | *Excellence signal beyond rubric* | §5b phase-authorization declares pre-scope execution order — not captured by any existing criterion |

**Essential:** 5/5 | **Recommended:** 3/3 | **Aspirational:** 45/45

**Score:** `60 + 30 + (45/45 × 10)` = **100.00**

---

### Rankings

| Rank | Variation | Score | Gaps |
|------|-----------|-------|------|
| 1 | **V-05** | **100.00** | None (+ excellence signal beyond rubric) |
| 1 | **V-04** | **100.00** | None |
| 3 | V-01 | 99.78 | C-53 |
| 3 | V-02 | 99.78 | C-52 |
| 5 | V-03 | 99.56 | C-49, C-53 |

---

### Excellence Signals from V-05

**Signal 1 — Phase-sequence position of procedural schema block declared in phase-authorization note**

V-05 adds an explicit authorization sequence `§5b §5 §6 §7` inside [A6]'s schema block, declaring that §5b executes *before* scope filtering. C-53 requires §5b to be a named schema block; it does not require the block to declare its relative execution position within the phase. V-05 surfaces that a procedural schema block can be mis-positioned without Gate-0 detecting it — adding §5b as [A6] prevents silent omission, but does not prevent §5b being placed *after* §5 (scope filter), which changes the evaluation semantics from full-evidence to scope-filtered-evidence. The phase-authorization sequence annotation makes that positional commitment auditable.

Candidate C-54: *Procedural schema block phase-sequence position declared in authorization note* — the schema block for a pre-proposal evaluation step explicitly declares whether it executes before or after scope filtering in its phase-authorization annotation, making a positional reordering detectable by annotation inspection without running the phase.

---

### JSON Summary

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Phase-sequence position of procedural schema block declared in phase-authorization note — §5b schema block explicitly annotates pre-scope execution order (§5b §5 §6 §7), making positional reordering detectable by annotation inspection; C-53 gates omission but not mis-sequencing"]}
```
