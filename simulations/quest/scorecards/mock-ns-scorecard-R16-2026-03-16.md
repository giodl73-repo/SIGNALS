Now I have everything. Writing the full scorecard.

---

# Round 16 Scorecard — mock-ns (rubric v16)

## Evaluation basis

- Golden ground truth: R15 V-02 = 150/150 under v16 (all 43 criteria pass). R16 variations are modifications of that baseline structure.
- Scoring method: identify deviations from the golden structure that clearly violate stated rubric rules; accept golden-structure criterion behavior for all unchanged elements.

---

## Critical finding: V-01 CONSTRAINT deviation

The single structural difference that determines V-01's score:

| Variation | CONSTRAINT text |
|-----------|----------------|
| V-01 | `Do not perform S-1, S-2, S-3.1, S-3.2, or S-3.3 until this step's emit is written.` |
| V-02–V-05 | `Do not perform S-1 (skill selection), S-2 (category lookup), S-3.1 (carry), S-3.2 (compliance detection), or S-3.3 (flag computation) until this step's emit is written.` |

C-15 rubric: *"must name operation types, not just restate ordering rule; Naming steps ('Do not begin S-1...') rather than operation types loses C-15 even if C-17 gained."*

V-01 names step IDs only (S-1, S-2, S-3.1, S-3.2, S-3.3) with no operation-type annotations. V-02–V-05 annotate with types in parentheses: skill selection, category lookup, carry, compliance detection, flag computation — five types named, satisfying the 3+ minimum.

---

## V-01 Full Criteria Evaluation

**Axis: Phrasing register (declarative "The step emits:" replacing "Emit:")**

| Criterion | Tier | Result | Evidence |
|-----------|------|--------|---------|
| C-01 Header fields | essential | PASS | All 6 fields present in MOCK ARTIFACT header block |
| C-02 CATEGORY correctness | essential | PASS | Complete 3-category membership table in S-2 |
| C-03 FLAG correctness | essential | PASS | 5-row FLAG table + critical skills list in S-3.3 |
| C-04 Fidelity warning | essential | PASS | All 3 category-matched warnings in S-4 |
| C-05 Skill-specific body | essential | PASS | Golden structural pattern instruction present |
| C-06 Emit lines present | recommended | PASS | TOPICS.md status line + skill selection emit both present |
| C-07 Correct path + write confirmation | recommended | PASS | S-5.4 emit present |
| C-08 Next-step line final | recommended | PASS | S-5.4 writes next-step as last artifact line |
| C-09 topic-status exclusion | aspirational | PASS | "NEVER topic-status (excluded: meta-structural)" in S-1 table |
| C-10 Compliance override | aspirational | PASS | COMPLIANCE-OVERRIDE path in S-3.3 |
| C-11 5-case FLAG coverage | aspirational | PASS | All 5 rows present in FLAG table |
| C-12 Tier before skill selection | aspirational | PASS | S-0 resolves tier before S-1 begins |
| C-13 Halt on unrecognized skill-id | aspirational | PASS | Table lookup with no else path = implicit halt (same as golden) |
| C-14 Discrete named assembly steps | aspirational | PASS | HEADER BLOCK / FIDELITY WARNING / MOCK BODY named; S-5.4 WRITE + next-step = 5 labeled units |
| **C-15 CONSTRAINT names 3+ op types** | **aspirational** | **FAIL** | **"Do not perform S-1, S-2, S-3.1, S-3.2, or S-3.3" — step IDs only, no operation types; rubric: "Naming steps rather than operation types loses C-15"** |
| C-16 Wildcards in FLAG table condition | aspirational | PASS | Critical skills note directly follows FLAG table (same as golden) |
| C-17 S-0 explicit advancement gate naming S-1 | aspirational | PASS | CONSTRAINT names S-1 explicitly |
| C-18 Tier-carry handoff names downstream steps | aspirational | PASS | Downstream-Action column names S-3.1, S-3.2, S-3.3 (same as golden) |
| C-19 Preamble gate + terminal gate | aspirational | PASS | CONSTRAINT (pre-resolution gate) + "Only this step emits..." (post-resolution exclusivity) |
| C-20 Tier-carry in table + standalone sentence | aspirational | PASS | Table Downstream-Action column + "Only this step emits..." closing (same as golden) |
| C-21 CONSTRAINT names 4+ op types incl. body gen | aspirational | FAIL | Step IDs only — same as C-15 failure; body generation not named |
| C-22 FLAG table row separation HIGH-STRUCT critical t1 | aspirational | PASS | Separate rows for "any not critical" / "1 critical" / "2+ critical" |
| C-23 Preamble gate as opening sentence | aspirational | PASS | CONSTRAINT is opening labeled block of S-0; first prose sentence after CONSTRAINT = declarative (same as golden) |
| C-24 CONSTRAINT names 5+ op types incl. write | aspirational | FAIL | Step IDs only — write operations not named |
| C-25 S-0 declarative identity sentence | aspirational | PASS | "This step emits the TOPICS.md status line before any other step produces output." — declarative identity after CONSTRAINT |
| C-26 Identity sentence names step output | aspirational | PASS | "TOPICS.md status line" named as output artifact |
| C-27 S-1 acknowledges S-0 output | aspirational | PASS | S-0 completes before S-1 via CONSTRAINT gate |
| C-28 Step as nominative subject of emission | aspirational | PASS | "This step emits..." (C-28 ✓) + "Only this step emits..." (focus-particle OK per C-28) — both in S-0 |
| C-29 No possessive-nominal subject | aspirational | PASS | No "This step's action is..." form |
| C-30 No artifact-as-subject active voice | aspirational | PASS | TOPICS.md not used as active-voice subject |
| C-31 No modal-obligation in role declaration | aspirational | PASS | Declarative sentences only; no "must/shall/should" |
| C-32 Tier-carry terminal sentence in closing position | aspirational | PASS | "Only this step emits the TOPICS.md status line." closes S-0 (same as golden) |
| C-33 Passive artifact-as-subject prohibited | aspirational | PASS | No passive artifact-subject form |
| C-34 Gerundive-as-subject prohibited | aspirational | PASS | No gerundive subject form |
| C-35 Artifact main-clause subject + step as relative-clause agent | aspirational | PASS | None present |
| C-36 Ordering predicate as main clause verb | aspirational | PASS | Emission verbs used, not ordering predicates |
| C-37 Possessive-NP action-abstraction + gerundive | aspirational | PASS | Not present |
| C-38 Expletive it-cleft | aspirational | PASS | Not present |
| C-39 Wh-pseudo-cleft | aspirational | PASS | Not present |
| C-40 Existential-there negation | aspirational | PASS | Not present |
| C-41 C-35 scope: by-PP does not trigger C-35 | aspirational | PASS | No by-PP constructions present |
| **C-42 Step-scope displacement** | **aspirational** | **PASS** | S-0 exists as discrete step; nominative-subject emission sentence within S-0 |
| **C-43 Lifecycle annotation replacement** | **aspirational** | **PASS** | No lifecycle annotation; C-43 trivially passes |

**Failed criteria: C-15, C-21, C-24 (-6 pts)**

Wait — I need to re-examine C-21 and C-24 for the golden structure. If R15 V-02 = 150/150, these must also pass in the golden. Let me revisit.

C-21 requires "4+ op types including body generation." C-24 requires "5+ op types including artifact-write." The golden CONSTRAINT (V-02–V-05) names: skill selection, category lookup, carry, compliance detection, flag computation. That is five operation types. Body generation and write are not explicitly named — they are downstream of what the CONSTRAINT covers.

Two competing interpretations:
1. **Strict**: body gen and write must be literally named → C-21 fails in all golden variants → contradicts 150/150
2. **Count-based**: 5 operation types ≥ 4 (C-21) and ≥ 5 (C-24), count satisfied even without the named examples → golden passes

Since R15 V-02 = 150/150 is the ground truth, the count-based interpretation applies. V-02–V-05 name 5 operation types → C-21 PASS (5 ≥ 4), C-24 PASS (5 ≥ 5). V-01 names 0 operation types (step IDs only) → C-15/C-21/C-24 all FAIL (0 < 3/4/5).

**Revised V-01 failures: C-15, C-21, C-24 = -6 points**

**V-01 score: 144/150**

---

## V-02 Full Criteria Evaluation

**Axis: Lifecycle emphasis — explicit CONSTRAINT gate + supplementation annotation**

All criteria inherit golden-structure behavior. Key criteria:

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-15 | PASS | CONSTRAINT names 5 op types: "skill selection, category lookup, carry, compliance detection, flag computation" |
| C-21 | PASS | 5 op types ≥ 4 |
| C-24 | PASS | 5 op types ≥ 5 |
| C-28 | PASS | "Before any other step begins, this step emits the TOPICS.md status line." — step as nominative subject, in S-0 |
| C-32 | PASS | "Only this step emits the TOPICS.md status line." present as discrete prose; annotation FOLLOWS (supplementation) |
| **C-42** | **PASS** | S-0 is discrete; emission sentence scoped to S-0 |
| **C-43** | **PASS** | Supplementation path: `[S-0 lifecycle exit: all four field values resolved; downstream steps may proceed]` follows terminal sentence; terminal sentence remains as discrete prose |

All 43 criteria pass.

**V-02 score: 150/150**

---

## V-03 Full Criteria Evaluation

**Axis: Output format — prose S-1/S-2 replacing lookup tables**

Changes: S-1 namespace default expressed as prose mapping; S-2 category membership as inline prose lists. S-0, S-3, S-4, S-5 unchanged vs V-02 (same expanded CONSTRAINT, same S-0 structure).

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-09 topic-status exclusion | PASS | "topic-status is permanently excluded (meta-structural; never default for any namespace)" retained in prose form |
| C-13 Halt on unrecognized skill-id | PASS | Prose enumeration has no else path = implicit halt (same mechanism as table) |
| C-15 / C-21 / C-24 | PASS | Expanded CONSTRAINT unchanged from V-02 |
| C-28 | PASS | S-0 structure unchanged; emission sentence in S-0 |
| C-42 | PASS | S-0 discrete; emission sentence not displaced |
| C-43 | PASS | No lifecycle annotation; trivially passes |

All 43 criteria pass.

**V-03 score: 150/150**

---

## V-04 Full Criteria Evaluation

**Axis: Role sequence — S-3 sub-steps as explicit numbered sequence with in-order constraint**

Changes: S-3 restructured as numbered list (1. S-3.1, 2. S-3.2, 3. S-3.3) with explicit "do not proceed until emit written" between each. S-3.2 adds explicit compliance-detection logic (scout-compliance/trace-permissions skill check). S-0 and all other steps unchanged.

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-10 Compliance override | PASS | S-3.2 now explicitly states: "If both [compliance-sensitive skill + compliance tags] present: FLAG = 'REAL-REQUIRED (compliance-sensitive)'" — stronger than golden |
| C-15 / C-21 / C-24 | PASS | Expanded CONSTRAINT unchanged |
| C-33 Passive artifact-as-subject | PASS | Declarative emit forms used |
| C-42 | PASS | S-0 discrete and unchanged |
| C-43 | PASS | No lifecycle annotation; trivially passes |

Numbered sequence with "do not proceed" constraints strengthens C-33 (carry-emit ordering) expression without creating new failure surfaces.

All 43 criteria pass.

**V-04 score: 150/150**

---

## V-05 Full Criteria Evaluation

**Axis: Combined — declarative phrasing (V-01) + explicit S-0 CONSTRAINT gate (V-02) + prose S-1/S-2 (V-03)**

Critical test: V-05 inherits the **expanded CONSTRAINT from V-02** (not V-01's shortened form), so C-15/C-21/C-24 pass. The V-01 declarative phrasing ("The step emits:") is applied to S-3 and S-5 emit instructions. Lifecycle supplementation annotation from V-02 present. Prose S-1/S-2 from V-03 present.

| Criterion | Result | Evidence |
|-----------|--------|---------|
| C-15 | PASS | V-05 uses V-02's expanded CONSTRAINT: "S-1 (skill selection), S-2 (category lookup), S-3.1 (carry), S-3.2 (compliance detection), or S-3.3 (flag computation)" |
| C-25 / C-26 | PASS | "This step emits the TOPICS.md status line before any other step produces output." is declarative identity naming the artifact |
| C-28 | PASS | "This step emits the TOPICS.md status line before any other step produces output." + "Only this step emits the TOPICS.md status line." — both nominative-subject in S-0 |
| C-32 | PASS | "Only this step emits the TOPICS.md status line." present as discrete prose; annotation FOLLOWS |
| **C-42** | **PASS** | S-0 is discrete; both emission sentences within S-0 scope |
| **C-43** | **PASS** | Supplementation path: `[S-0 lifecycle exit: all four field values resolved; S-1 through S-3.3 may proceed]` follows terminal sentence; sentence not displaced |

No cross-axis interference. V-01 declarative phrasing composites cleanly with V-02 CONSTRAINT expansion and V-03 prose format.

All 43 criteria pass.

**V-05 score: 150/150**

---

## Score Summary

| Variation | Score | Failures | Delta from top |
|-----------|-------|----------|---------------|
| V-02 | **150/150** | none | — |
| V-03 | **150/150** | none | — |
| V-04 | **150/150** | none | — |
| V-05 | **150/150** | none | — |
| V-01 | **144/150** | C-15 (-2), C-21 (-2), C-24 (-2) | -6 |

---

## Detailed V-01 Failure Chain

**Root cause**: CONSTRAINT uses step IDs only: `"Do not perform S-1, S-2, S-3.1, S-3.2, or S-3.3 until this step's emit is written."`

This triggers a **three-criterion cascade**:
- **C-15** (3+ op types): 0 operation types named < 3 → FAIL
- **C-21** (4+ op types including body gen): 0 < 4 → FAIL
- **C-24** (5+ op types including write): 0 < 5 → FAIL

**Repair**: Add operation-type annotations in parentheses — exactly as V-02–V-05 do: `"S-1 (skill selection), S-2 (category lookup), S-3.1 (carry), S-3.2 (compliance detection), or S-3.3 (flag computation)"` — five types, satisfying all three criteria simultaneously.

**Key discriminator confirmed by R16**: The V-01 declarative phrasing change ("The step emits:" vs "Emit:") is itself criteria-neutral (C-28 scores the structural emission sentence, not the procedural emit instructions). The loss is entirely attributable to the CONSTRAINT shortening, not to the declared phrasing axis. V-05 isolates this: it applies V-01's declarative phrasing but restores V-02's expanded CONSTRAINT, achieving 150/150.

---

## Excellence Signals

Top-scoring variations: **V-02, V-03, V-04, V-05** (all 150/150).

**Signal 1 — Parenthetical operation-type annotation in CONSTRAINT (V-02, V-03, V-04, V-05)**
The pattern `"S-N (operation-type)"` e.g., `"S-1 (skill selection), S-2 (category lookup)"` satisfies C-15, C-21, and C-24 simultaneously from a single CONSTRAINT sentence. This is the single highest-leverage sentence in the skill: zero words wasted, three criteria satisfied.

**Signal 2 — Supplementation path explicitly exercised (V-02, V-05)**
`[S-0 lifecycle exit: all four field values resolved; downstream steps may proceed]` following (not replacing) the terminal sentence constitutes a live probe of the C-43 supplementation boundary. The annotation declares exit state in terms of the resolved fields rather than abstract lifecycle vocabulary — making it semantically tied to S-0's actual work.

**Signal 3 — Numbered sub-step ordering with in-sequence gate (V-04)**
`"1. S-3.1 -- CARRY ... Do not proceed to S-3.2 until this emit is written. 2. S-3.2 -- COMPLIANCE ... Do not proceed to S-3.3 until this emit is written. 3. S-3.3 -- FLAG"` expresses C-33 (carry-emit ordering) at the instruction level, not just the lifecycle note level. This makes the ordering contract unambiguous to an executor who reads only S-3.

**Signal 4 — Format-orthogonality of S-1/S-2 confirmed (V-03, V-05)**
Replacing namespace default tables and category membership tables with prose lists has zero criteria impact. Format and structure are independent for these steps.

**Signal 5 — Composition without interference (V-05)**
Three independent axis changes (declarative phrasing + expanded CONSTRAINT gate + prose format) compose without criterion interaction. None of the three changes affects the other's criteria. V-05 reaches 150/150 with a substantially more readable surface form than the table-heavy golden.

---

## C-42 / C-43 Round Summary

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-42 (step-scope boundary) | PASS | PASS | PASS | PASS | PASS |
| C-43 (annotation placement) | PASS (no annotation) | PASS (supplementation) | PASS (no annotation) | PASS (no annotation) | PASS (supplementation) |

C-42 passes across all five because S-0 exists as a discrete step in every variation and the nominative-subject emission sentence is scoped within S-0 in every case. C-43 passes via supplementation in V-02/V-05; trivially passes in V-01/V-03/V-04 (no annotation present). The R15 displacement failure modes are fully repaired.

---

## Ranking

| Rank | Variation | Score | Best-in-class signal |
|------|-----------|-------|---------------------|
| 1 (tie) | V-02 | 150/150 | Supplementation lifecycle annotation proof |
| 1 (tie) | V-03 | 150/150 | Format-orthogonality proof |
| 1 (tie) | V-04 | 150/150 | In-sequence gate reinforcement of C-33 |
| 1 (tie) | V-05 | 150/150 | Full composition — most readable surface form at max score |
| 5 | V-01 | 144/150 | Declarative phrasing neutral; CONSTRAINT shortening exposes C-15/C-21/C-24 cascade |

V-05 is the standout for practical use: it is the most readable (prose S-1/S-2 + declarative "The step emits:" throughout) while hitting 150/150, establishing that readability and structural score are not in tension.

---

```json
{"top_score": 150, "all_essential_pass": true, "new_patterns": ["parenthetical operation-type annotation in CONSTRAINT (e.g., 'S-1 (skill selection)') satisfies C-15/C-21/C-24 cascade from single sentence", "numbered S-3 sub-steps with in-order 'do not proceed until emit written' gate strengthens C-33 with zero criteria risk", "prose S-1/S-2 format is criteria-neutral — table vs prose has no structural criterion impact", "declarative phrasing composites cleanly with expanded CONSTRAINT and lifecycle annotations — no cross-axis interference at 150/150"]}
```
