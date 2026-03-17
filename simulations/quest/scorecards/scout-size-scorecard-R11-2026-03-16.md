## Scout-Size R11 — Scoring Scorecard

---

### Scoring Methodology

**Scoring formula:**
- Essential (C-01–C-05): 60 pts total — must all pass
- Recommended (C-06–C-08): 30 pts total
- Aspirational (C-09–C-31, 23 criteria): 10 pts total; PASS=1, PARTIAL=0.5, FAIL=0; per-criterion value = ~0.435 pts

---

### Per-Variation Evaluation

---

#### V-01 — Axis: Output format (Pre-slot example placement throughout)

**Core change**: WRONG/CORRECT examples moved before every output field they govern (was post-slot for Steps 2, 3, 6, 7 in R10 V-01; now pre-slot throughout).

**Essential (C-01–C-05):**

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Named integration points + total count required in table column header |
| C-02 | PASS | "LOW / MEDIUM / HIGH / XL — nothing else" vocabulary enforced |
| C-03 | PASS | Step 1 has inertia table with Cost Direction and Key Driver fields |
| C-04 | PASS | Step 6 separates confidence level from basis; WRONG example shows bare-level failure |
| C-05 | PASS | Explicit boundary check at Output Compilation |

**Recommended (C-06–C-08):**

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | PASS | "name the role — 'engineer' alone fails" in column header |
| C-07 | PASS | "N–M format — not a calendar date, not a single number" |
| C-08 | PASS | "'it's complex' fails" constraint with causal-factor examples |

**Aspirational (C-09–C-31):**

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Step 9 has tier-up and tier-down with "tier-specific" framing |
| C-10 | PASS | Step 8 Confidence Calibration section present |
| C-11 | PASS | Step 7 dedicated gap section |
| C-12 | PASS | "one scenario — not a list, not a hedge" in column header |
| C-13 | PASS | "fill with LOW / MEDIUM / HIGH / XL" in Destination Tier column header |
| C-14 | PASS | CORRECT examples show named, investigable conditions |
| C-15 | PASS | Pre-field self-test: "Could a reader derive this gap by negating something confirmed?" |
| C-16 | PASS | "[a tier that maps to itself is vacuous]" in column header |
| C-17 | PASS | C-11, C-15, C-16 scoped fields all have inline WRONG examples making violations recognizable |
| C-18 | PASS | Destination Tier and Complexity Tier column headers encode constraints structurally |
| C-19 | PASS | V-01's defining change — WRONG/CORRECT now precede every output table slot; Step 7 order: examples → self-test → table |
| C-20 | FAIL | Single-phase design; no role separation |
| C-21 | PASS | All steps have both named WRONG and CORRECT instances in same block |
| C-22 | PASS | Gap column header: "[must address a dimension NOT covered by the Confidence Basis above — not a negation or restatement]"; Destination Tier: "[must differ from current tier]" |
| C-23 | FAIL | No role charters |
| C-24 | FAIL | No Phase 2 |
| C-25 | FAIL | No Phase 2 (C-28 is the applicable single-phase criterion) |
| C-26 | FAIL | No role tags in output structure field labels |
| C-27 | FAIL | Output Compilation table gap field: "[specific named unknown — why it matters]" — no C-15 encoding in compilation table |
| C-28 | PASS | "Before writing your gap, ask: Could a reader derive this gap by negating something confirmed in the basis above — reversing 'X is confirmed' to 'X has not been confirmed'?" — concrete self-test before the table slot |
| C-29 | FAIL | No phase structure |
| C-30 | PASS | All three mechanisms converge in Step 7: (1) C-22 label in column header; (2) C-28 self-test before table; (3) C-21 WRONG+CORRECT before table |
| C-31 | PASS (vacuous) | C-19 achieved throughout; no in-table gap field without pre-slot examples |

**Aspirational score:** 16/23 = 6.957 pts

**Composite: 60 + 30 + 6.957 = 96.96**

---

#### V-02 — Axis: Lifecycle emphasis (Gap as standalone checkpoint)

**Core change**: Confidence gap extracted from table cell into a dedicated `── CONFIDENCE GAP CHECKPOINT ──` prose section between Section 6 and Section 7. Gap is no longer a table row.

**Essential (C-01–C-05):**

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Named points + "Total [N] integration points" in table |
| C-02 | PASS | "exactly one: LOW / MEDIUM / HIGH / XL" in column header |
| C-03 | PASS | Section 1 Inertia Check with WRONG/CORRECT examples and three-column table |
| C-04 | PASS | Section 6 separates level from basis; "State only what IS known here" directive |
| C-05 | PASS | "No task breakdowns, sprint assignments, owner names, or milestone dates" |

**Recommended (C-06–C-08):** All PASS — same structure as V-01.

**Aspirational:**

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Section 7 has tier-up and tier-down |
| C-10 | PASS | Section 8 calibration present |
| C-11 | PASS | Dedicated CONFIDENCE GAP CHECKPOINT with explicit "different dimension" requirement |
| C-12 | PASS | "one scenario — name what settles it" in column header |
| C-13 | PASS | "must differ from current: LOW / MEDIUM / HIGH / XL" in Destination Tier header |
| C-14 | PASS | CORRECT examples show named falsifiable conditions |
| C-15 | PASS | Self-check: "Ask — if I reversed something from my Section 6 basis... would I get my gap? If yes, I have written a basis-negation." |
| C-16 | PASS | "[must differ from current: LOW / MEDIUM / HIGH / XL]" in column header |
| C-17 | PASS | Gap checkpoint has inline WRONG/CORRECT; sensitivity has WRONG/CORRECT; violations recognizable |
| C-18 | PASS | Structural column headers for tier vocabulary and sensitivity destination |
| C-19 | PASS | Gap field is a prose line (`Gap: ___`) appearing AFTER examples and self-check in the checkpoint section — trivially pre-slot |
| C-20 | FAIL | Single-phase |
| C-21 | PASS | WRONG and CORRECT both present in checkpoint and sensitivity sections |
| C-22 | PASS | Gap field label: "[must address a dimension not covered by the Section 6 basis — not a negation of it]"; Destination Tier: "[must differ from current: LOW / MEDIUM / HIGH / XL]" |
| C-23 | FAIL | No role charters |
| C-24 | FAIL | No Phase 2 |
| C-25 | FAIL | No Phase 2 |
| C-26 | FAIL | No role tags |
| C-27 | FAIL | Output Compilation table gap field has no C-15 encoding |
| C-28 | PASS | "Self-check before writing: Ask — if I reversed something from my Section 6 basis..." — concrete executable test before the gap prose line |
| C-29 | FAIL | No phase structure |
| C-30 | PASS | All three mechanisms in CONFIDENCE GAP CHECKPOINT: (1) field label with "[must address... not a negation]" (C-22); (2) self-check query (C-28); (3) WRONG+CORRECT examples (C-21) — all before the prose gap field |
| C-31 | PASS (vacuous) | Gap is not in a table at all; C-19 trivially satisfied |

**Aspirational score:** 16/23 = 6.957 pts

**Composite: 60 + 30 + 6.957 = 96.96**

---

#### V-03 — Axis: Phrasing register (Imperative, active self-interrogation)

**Core change**: Gate label shifts from "Before finalizing your Confidence Gap:" to "**Stop. Read this before you write anything.**" Self-test shifts from passive ("ask: could a reader derive...") to imperative ("Now check your draft: Ask yourself — if I took something from my Step 6 basis and negated it...").

**Essential (C-01–C-05):** All PASS — same structural features as V-01.

**Recommended (C-06–C-08):** All PASS.

**Aspirational:**

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Step 9 has tier-up and tier-down |
| C-10 | PASS | Step 8 calibration present |
| C-11 | PASS | Step 7 dedicated gap section with "Stop. Read this before you write anything." |
| C-12 | PASS | "Name it — name what settles it" instruction |
| C-13 | PASS | "[must differ from current: LOW / MEDIUM / HIGH / XL]" in column header |
| C-14 | PASS | CORRECT examples show falsifiable conditions |
| C-15 | PASS | Imperative self-test: "Now check your draft: Ask yourself — if I took something from my Step 6 basis and negated it, would I get this gap?" |
| C-16 | PASS | "[must differ from current: LOW / MEDIUM / HIGH / XL]" in column header |
| C-17 | PASS | WRONG/CORRECT inline for all high-risk fields |
| C-18 | PASS | Column headers encode structural constraints |
| C-19 | PASS | Step 7 order: "Stop" instruction → WRONG example → CORRECT example → self-test → table (output slot). All before slot. |
| C-20 | FAIL | Single-phase |
| C-21 | PASS | Both WRONG and CORRECT present in Step 7 and Step 9 |
| C-22 | PASS | Gap column header: "[must name a dimension Step 6 did NOT establish — negating the basis fails this field]"; Destination Tier: "[must differ from current: LOW / MEDIUM / HIGH / XL]" |
| C-23 | FAIL | No role charters |
| C-24 | FAIL | No Phase 2 |
| C-25 | FAIL | No Phase 2 |
| C-26 | FAIL | No role tags |
| C-27 | FAIL | Compilation table gap field: "[specific named unknown — why it matters]" — no C-15 encoding |
| C-28 | PASS | "Now check your draft: Ask yourself — if I took something from my Step 6 basis and negated it, would I get this gap? If yes, throw it out..." — imperative active procedure, pre-slot |
| C-29 | FAIL | No phase structure |
| C-30 | PASS | All three mechanisms in Step 7: (1) "[must name a dimension Step 6 did NOT establish — negating the basis fails this field]" in column header; (2) "Now check your draft: Ask yourself..." self-test; (3) WRONG+CORRECT before table |
| C-31 | PASS (vacuous) | C-19 achieved; no in-table gap without pre-slot examples |

**Aspirational score:** 16/23 = 6.957 pts

**Composite: 60 + 30 + 6.957 = 96.96**

> **Note**: V-03's imperative register change is structurally identical to V-01 and V-02 — the rubric measures mechanism presence, not activation-language phrasing. V-03 neither gains nor loses criteria relative to V-01. The phrasing hypothesis is untestable by the current rubric.

---

#### V-04 — Combined: Role sequence + Lifecycle (Two-phase + C-30 in Phase 2)

**Core change**: Two-phase design. Phase 1 (Sizing Analyst) owns 11 fields; Phase 2 (Risk Assessor) owns Confidence Gap exclusively. Phase 2 has explicit prohibited-category non-access clause and executable self-test. C-30 cluster in Phase 2: WRONG/CORRECT before the gap table, C-25 self-test in charter body, C-22 in gap column header.

**Essential (C-01–C-05):** All PASS — all output fields present across phases; boundary check at Output Compilation.

**Recommended (C-06–C-08):** All PASS.

**Aspirational:**

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Sections 1.7 and 1.8 (Tier-Up, Tier-Down sensitivity) |
| C-10 | PASS | Section 1.9 Confidence Calibration |
| C-11 | PASS | Phase 2 produces Confidence Gap with full defense cluster |
| C-12 | PASS | "one scenario — name what settles it" in column headers |
| C-13 | PASS | "[must be HIGHER than current tier: HIGH or XL]" / "[must be LOWER than current tier: LOW or MEDIUM]" — more explicit than "differs" |
| C-14 | PASS | CORRECT examples in 1.7 and 1.8 show falsifiable, investigable conditions |
| C-15 | PASS | Phase 2 self-test + prohibited category list enforces non-overlap structurally |
| C-16 | PASS | "[must be HIGHER/LOWER than current tier]" in Phase 1 sensitivity column headers |
| C-17 | PASS | All high-risk fields (C-11, C-15, C-16) have inline WRONG/CORRECT examples at point of production |
| C-18 | PASS | Column headers encode tier vocabulary, sensitivity direction, confidence level constraints |
| C-19 | PASS | Phase 2: WRONG/CORRECT examples appear before the gap table row; Phase 1: all examples pre-slot |
| C-20 | PASS | Phase 1 / Phase 2 role separation; Phase 2 charter explicitly prohibits re-using Phase 1 confirmed content |
| C-21 | PASS | Both WRONG and CORRECT present in Phase 2 gap section and Phase 1 sensitivity sections |
| C-22 | PASS | Gap column header: "[Phase 2: Risk Assessor — PROHIBITED: ... — must name a dimension Phase 1 did not reach — not derivable from Phase 1 by negation]"; Destination Tier: "[must be HIGHER/LOWER than current tier]" |
| C-23 | PASS | Phase 1 lists all 11 owned fields; Phase 2 owns exactly 1; both have explicit "you do NOT produce" exclusion statements |
| C-24 | PASS | Phase 2 non-access clause names four specific prohibited content categories: integration points, API contract status, complexity drivers, team/timeline signals |
| C-25 | PASS | "Ask: 'Could a reader look only at Phase 1 output and derive my gap by negating something the Sizing Analyst confirmed — reversing "X is established" to "X has not been confirmed"?' If yes, it is a restatement and a charter violation." — concrete procedure |
| C-26 | PARTIAL | Phase 2's gap column header has "[Phase 2: Risk Assessor — ...]" — role name present. Phase 1's within-phase production tables lack "[Phase 1: Sizing Analyst]" role tags in their field labels (e.g., "Confidence Level [HIGH / MEDIUM / LOW]" without role tag). Compilation table has a "Phase" column (numbers, not role names). Phase number encoding requires one lookup to resolve role name — partially satisfies C-26's cross-reference elimination goal. |
| C-27 | PASS | Compilation table gap field: "[must address a different dimension than Phase 1 Confidence Basis — not a negation of what Phase 1 confirmed]" — C-15 non-overlap rule encoded in gap column header within the aggregation table |
| C-28 | FAIL | N/A in two-phase design; C-25 is the applicable criterion |
| C-29 | PASS | Phase 1 charter: "Charter — you do NOT produce: Confidence Gap. That field belongs to Phase 2." Explicit exclusion list matching Phase 2's owned field |
| C-30 | PASS | All three mechanisms in Phase 2 gap section: (1) C-22 label in column header with prohibited categories; (2) C-25 self-test before the gap table; (3) C-21 WRONG+CORRECT before the gap table |
| C-31 | PASS (vacuous) | C-19 achieved (examples before table in Phase 2); post-table "Before finalizing" reminder is belt-and-suspenders |

**Aspirational score:** 21 PASS + 0.5 (C-26 PARTIAL) + 1 FAIL (C-28) = **21.5/23 = 9.348 pts**

**Composite: 60 + 30 + 9.348 = 99.35**

---

#### V-05 — Combined: Inertia framing + Role sequence + Output format (Three-phase, max structural encoding)

**Core change**: Three-phase design: Phase 0 (Inertia Analyst) owns Inertia Check as a gate phase; Phase 1 (Sizing Analyst) owns the nine sizing fields; Phase 2 (Risk Assessor) owns Confidence Gap. Every within-phase production table field label carries `[Phase N: Role Name]`. All phases have comprehensive exclusion lists.

**Essential (C-01–C-05):** All PASS — complete coverage across three phases; boundary check at Output Compilation.

**Recommended (C-06–C-08):** All PASS.

**Aspirational:**

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Phase 1 has Tier Sensitivity section with up and down directions |
| C-10 | PASS | Phase 1 has Confidence Calibration section |
| C-11 | PASS | Phase 2 produces Confidence Gap with full defense cluster |
| C-12 | PASS | "one scenario — name what settles it" in sensitivity column header |
| C-13 | PASS | "[Phase 1: Sizing Analyst — must differ from current: LOW / MEDIUM / HIGH / XL]" in Destination Tier column header |
| C-14 | PASS | CORRECT examples show falsifiable conditions confirming specific named investigations |
| C-15 | PASS | Phase 2 self-test + prohibited category non-access clause structurally enforces non-overlap |
| C-16 | PASS | "[must differ from current: LOW / MEDIUM / HIGH / XL]" in sensitivity destination column header |
| C-17 | PASS | C-11, C-15, C-16 scoped fields all have inline WRONG examples making the violation recognizable at production time |
| C-18 | PASS | Structural column headers for tier vocabulary, destination tier, sensitivity conditions |
| C-19 | PASS | Phase 0: WRONG/CORRECT before table. Phase 1: all section WRONG/CORRECT before tables. Phase 2: WRONG/CORRECT before gap table. Pre-slot throughout. |
| C-20 | PASS | Three-phase role separation — Phase 0, Phase 1, Phase 2 each have named charters; Phase 2 prohibited from Phase 1 confirmed content |
| C-21 | PASS | Both WRONG and CORRECT present in all sections (Phase 0, Phase 1 steps, Phase 2 gap section) |
| C-22 | PASS | Phase 2 gap column header: "[Phase 2: Risk Assessor — PROHIBITED: ... — must name a dimension Phase 1 did not reach — verify it is NOT derivable from Phase 1 by negation before writing]"; Destination Tier: "[Phase 1: Sizing Analyst — must differ from current: LOW / MEDIUM / HIGH / XL]" |
| C-23 | PASS | Phase 0 lists 1 owned field + full exclusion list. Phase 1 lists 9 owned fields + "you do NOT produce: Inertia Check (Phase 0). Confidence Gap (Phase 2)." Phase 2 lists 1 owned field + exhaustive exclusion list of all Phase 0 and Phase 1 fields. Every field in exactly one charter. |
| C-24 | PASS | Phase 2 names four prohibited content categories: integration points Analyst enumerated, API contracts Analyst confirmed, complexity drivers Analyst identified, team/timeline signals Analyst produced |
| C-25 | PASS | "Could a reader look only at Phase 1 output and derive my gap by negating something the Sizing Analyst confirmed — turning 'X is established' into 'X has not been confirmed'?" — concrete, executable test |
| C-26 | PASS | Every within-phase production table field label carries `[Phase N: Role Name]`: Phase 0 gap label "[Phase 0: Inertia Analyst — ...]"; Phase 1 field labels "[Phase 1: Sizing Analyst — ...]" throughout; Phase 2 gap label "[Phase 2: Risk Assessor — ...]". Ownership visible at production site without charter cross-reference. |
| C-27 | PASS | Compilation table gap field: "[must address a different dimension than Phase 1 Confidence Basis — not a negation of what Phase 1 confirmed]" encodes C-15 in the aggregation table's dependent field column |
| C-28 | FAIL | N/A in three-phase design; C-25 is the applicable single-phase analog; C-25 PASSES |
| C-29 | PASS | Phase 1 charter: "you do NOT produce: Inertia Check (owned by Phase 0). Confidence Gap (owned by Phase 2)." Explicit bidirectional exclusion list matching Phase 2's owned field. Phase 0 has full exclusion list of all Phase 1 + Phase 2 fields. |
| C-30 | PASS | All three mechanisms converge in Phase 2 gap section: (1) C-22 relational constraint in gap column header "[... must name a dimension Phase 1 did not reach — verify it is NOT derivable from Phase 1 by negation before writing]"; (2) C-25 self-test in Phase 2 charter body before the gap table; (3) C-21 WRONG+CORRECT before the gap table |
| C-31 | PASS (vacuous + belt) | C-19 achieved (pre-slot examples in Phase 2); post-table "Before finalizing your Confidence Gap: Run the self-test one more time" provides belt-and-suspenders gate even though C-31 is vacuously satisfied |

**Aspirational score:** 22/23 = 9.565 pts

**Composite: 60 + 30 + 9.565 = 99.57**

---

### Composite Score Summary

| Rank | Variation | Aspir (of 23) | Composite |
|------|-----------|---------------|-----------|
| 1 | **V-05** | 22.0 | **99.57** |
| 2 | V-04 | 21.5 | 99.35 |
| 3 | V-01 | 16.0 | 96.96 |
| 3 | V-02 | 16.0 | 96.96 |
| 3 | V-03 | 16.0 | 96.96 |

**New champion: V-05 at 99.57**

---

### Criteria Coverage by Design Tier

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 Sensitivity tier-specific | P | P | P | P | P |
| C-10 Confidence calibration | P | P | P | P | P |
| C-11 Gap named | P | P | P | P | P |
| C-12 Single named conditions | P | P | P | P | P |
| C-13 Explicit tier destination | P | P | P | P | P |
| C-14 Falsifiable conditions | P | P | P | P | P |
| C-15 Basis/gap non-overlapping | P | P | P | P | P |
| C-16 Destination differs from current | P | P | P | P | P |
| C-17 Inline failure examples | P | P | P | P | P |
| C-18 Structural encoding | P | P | P | P | P |
| C-19 Examples precede output field | **P** | **P** | **P** | P | P |
| C-20 Role-separated production | F | F | F | **P** | **P** |
| C-21 Both WRONG and CORRECT | P | P | P | P | P |
| C-22 Relational constraints in field label | P | P | P | P | P |
| C-23 Charter covers all fields | F | F | F | **P** | **P** |
| C-24 Non-access names prohibited categories | F | F | F | **P** | **P** |
| C-25 Phase 2 self-test | F | F | F | **P** | **P** |
| C-26 Role ownership in output structure | F | F | F | ½ | **P** |
| C-27 Cross-phase constraint in compilation table | F | F | F | **P** | **P** |
| C-28 Single-phase self-test in gap body | P | P | P | F(N/A) | F(N/A) |
| C-29 Phase 1 exclusion list | F | F | F | **P** | **P** |
| C-30 Defense cluster convergence | P | P | P | P | P |
| C-31 Named gate block | P(v) | P(v) | P(v) | P(v) | P(v) |

**P** = PASS · **½** = PARTIAL · **F** = FAIL · **(v)** = vacuously satisfied · **bold** = criterion newly gained relative to prior tier

---

### R11 Analysis: What Changed

**C-30 and C-31 (new in v11):** All five variations pass both — C-30 because all three defense mechanisms already converge on the gap section in every variation; C-31 vacuously because all variations achieve C-19 (examples before the table slot). The new criteria formalize what R10 V-01 demonstrated; they do not change the champion.

**C-19 (now achieved by all):** The defining R10 gap for V-01 is resolved in all R11 variations. Single-phase designs (V-01, V-02, V-03) close this gap and reach 16/23.

**C-26 separates V-04 from V-05:** V-04 achieves C-26 PARTIAL (phase numbers in compilation table + role name only in gap field label). V-05 achieves C-26 PASS by embedding `[Phase N: Role Name]` in every within-phase production table field label. This is the single criterion separating the top two.

---

### Excellence Signals from V-05 (New Patterns)

**Pattern 1 — Role-tagged field labels at all production sites:**
V-05 embeds `[Phase 0: Inertia Analyst]`, `[Phase 1: Sizing Analyst]`, `[Phase 2: Risk Assessor]` in every within-phase production table field label — not just the highest-risk gap field. This eliminates ownership ambiguity at every production decision point. V-04 applied the technique only to the gap field; V-05 extends it universally. The pattern: *wherever a model fills a field value, the role responsible for that value is visible in the field's own column header.* Charter cross-reference is not required.

**Pattern 2 — Phase-0 inertia gate:**
Promoting the inertia analysis from a numbered section to a named phase with a dedicated charter and comprehensive exclusion list converts it from a completable step into a structural gate. Phase 0's exclusion list ("you do NOT produce: Surface Area, Complexity Tier, ...") makes it impossible to conflate inertia analysis with sizing logic — the phase boundary is a charter violation, not a style violation. The pattern: *contextual prerequisites become structurally isolated phases rather than leading sections within a single phase.*

---

### Candidate for R12 Rubric

**C-32 (proposed):** Role ownership co-encoded in field labels across ALL within-phase production tables (not only the highest-risk field). A prompt passes when every phase's production tables carry `[Phase N: Role Name]` in field column headers or labels, not only the gap field's definition. This distinguishes V-05's approach from V-04's partial coverage.

---

```json
{"top_score": 99.57, "all_essential_pass": true, "new_patterns": ["Phase-0 inertia gate: dedicated pre-sizing phase with charter and exclusion list promotes cost-of-not-building from a completable section to a structural gate before sizing begins", "Role-tagged field labels at all production sites: embedding [Phase N: Role Name] in every within-phase production table field header eliminates ownership ambiguity at every decision point, not only the highest-risk gap field"]}
```
