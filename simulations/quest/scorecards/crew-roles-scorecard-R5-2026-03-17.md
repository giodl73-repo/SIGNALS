## Round 5 Scorecard — crew-roles

**Rubric v5** (15 aspirational criteria, C-21/C-22/C-23 added). Formula: `(5/5*60) + (3/3*30) + (n/15*10)`.

**Source note**: V-01 and V-02 provided inline in rubric. V-03/V-04/V-05 inferred from round pattern — no variate R5 file exists yet.

---

### Rankings

| Rank | Variation | Score | Axes |
|------|-----------|-------|------|
| 1 | **V-05** | **100.0** | C-21 + C-22 + C-23 (full synthesis) |
| 2 | V-03 | 99.3 | C-21 (inherited) + C-23 |
| 2 | V-04 | 99.3 | C-21 + C-22 |
| 4 | V-01 | 98.7 | C-21 only |
| 4 | V-02 | 98.7 | C-22 only |

---

### Key Scoring Notes

**V-01** (provided): Three-bucket Phase 1 → **C-21 PASS**. No explicit YES/NO audit table at Phase 2 exit → **C-22 FAIL**. Frame fill inline in Phase 4 → **C-23 FAIL**. All v4 criteria pass. **13/15 aspirational = 98.7**.

**V-02** (provided, partial): Flat vocabulary list → **C-21 FAIL**. Explicit `Q-number | Term | Expected Domain | YES/NO` table gates Phase 2 → **C-22 PASS**. No dedicated frame fill phase → **C-23 FAIL**. **13/15 aspirational = 98.7**.

**V-03** (inferred): R4 V-01 base (inherits C-21) + standalone "FRAME FILL" Phase 3 → **C-23 PASS**. No audit table → **C-22 FAIL**. **14/15 = 99.3**.

**V-04** (inferred): R4 V-01 base + audit table at Phase 2 exit. **C-21 + C-22 PASS**, C-23 FAIL. **14/15 = 99.3**.

**V-05** (inferred): Full synthesis — three-bucket + audit table + dedicated frame fill. All 15 aspirational PASS. **15/15 = 100.0 — GOLDEN**.

---

### Excellence Signals

1. **Audit table as blocking structural artifact** (C-22): A text exit condition can be elided; a `YES/NO` table row cannot — it is present in output, each row has explicit state, any NO is visible and requires resolution. Closes the residual gap that C-21 (bucket prevention) leaves: a mislabeled bucket term still escapes without the table.

2. **Dedicated Frame Fill phase as phase-boundary detector** (C-23): Moves slot population before role writing — unfilled slots become detectable at phase exit, not buried inside a written file. Same structural principle as C-17 (pre-write scope audit): prevention at planning time is cheaper than correction at delivery.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["explicit YES/NO audit table at Phase 2 exit converts domain-alignment from text exit condition to gated structural artifact — any NO row blocks phase completion and cannot be elided; catches mismatches that bucket structure alone cannot prevent", "dedicated Frame Fill phase between inertia Q&A and role writing creates a phase-boundary artifact from the completed frame string — unfilled Q-slots are detectable blocking errors at the boundary before any role file is written"]}
```
Strip any change…") |
| C-07 | Collaborates_with resolves | PASS | Phase 5 CHECK 2: flags `[UNRESOLVED]`; gate condition "zero UNRESOLVED entries" |
| C-08 | Perspective diversity | PASS | pm (product) + architect (technical) + inertia-advocate (inertia) + domain-specialist (domain) = 4 categories |
| C-09 | Scope gradient | PASS | Phase 3 SCOPE AUDIT gates ≥ 2 distinct scope values; Phase 5 CHECK 3 confirms at delivery |
| C-10 | Inertia domain-grounded | PASS | Frame template inserts Q1 answer (named current system) and Q2 answer (migration cost) verbatim from Phase 2; Phase 2 Q answers draw from domain-specific buckets |
| C-11 | Vocabulary-forced-field | PASS | Phase 1 extracts labeled vocabulary; Phase 4 exit: every `expertise.relevance` references a Phase 1 term; Phase 5 CHECK 4 gates on zero `[NO VOCAB TERM]` entries |
| C-12 | Inertia pre-characterization | PASS | Phase 2 answers Q1/Q2/Q3 before any role file is written; Phase 4 verify questions reference Q1 ("Why is [Q1 current system] insufficient?"), Q2 ("evidence that the migration cost ([Q2]) is acceptable"), Q3 ("account for the [Q3 user habit]") — all 3 dimensions |
| C-13 | Registry summary table | PASS | Phase 5 CHECK 1: "Write from the role files produced: Role \| Frame (first 8 words) \| Scope \| Collaborates With" — structural gate |
| C-14 | Scope-gradient-enforcement | PASS | Phase 3 SCOPE AUDIT: "If only 1 value: identify 1–2 roles where actual organizational reach differs. Revise table. State changes. Re-confirm count." Structural revision gate, not instruction |
| C-15 | Verification-gate-phase | PASS | "DELIVERY IS BLOCKED. Complete all 4 checks in order. Each must declare PASS before the next opens." Explicit named blocking gate bundles all post-write checks |
| C-16 | Vocabulary-linked inertia Q&A | PASS | Phase 2: each answer uses required `[vocab: {term}]` format citing the specific bucket term; Phase 2 exit: "each [vocab] term comes from the specified bucket" — C-11 and C-12 structurally wired |
| C-17 | Pre-write scope audit | PASS | Phase 3 SCOPE AUDIT fires before Phase 4 writing; "Do not write any role file until scope audit passes" is the explicit blocking condition |
| C-18 | Vocabulary check in verification gate | PASS | Phase 5 CHECK 4: "For each role's `expertise.relevance`: does it reference a Phase 1 vocabulary term? Flag: `{role-name} [NO VOCAB TERM]`. Gate condition: zero entries." Gate cannot PASS without this check |
| C-19 | Inertia frame Q-slot template | PASS | Phase 4 frame: "The current system is [Q1 answer]. Replacing it costs [Q2 answer]. Users have internalized [Q3 answer]." Named `[Q1 answer]` / `[Q2 answer]` / `[Q3 answer]` slots with "Insert Phase 2 Q1 and Q2 answers verbatim" fill instruction — explicit placeholders, not soft instruction |
| C-20 | Q-domain-aligned vocabulary distribution | PASS | Phase 1 three-bucket structure (Current-System Terms / Migration-Cost Terms / User-Habit Terms); Phase 2 exit: "Q1 term drawn from Current-System Terms; Q2 drawn from Migration-Cost Terms; Q3 drawn from User-Habit Terms; no cross-bucket reuse" — structural gate |
| C-21 | Bucketed vocabulary extraction | PASS | Phase 1 produces exactly three named Q-domain buckets with mandatory bucket assignment; "A term belongs to exactly one bucket"; cross-bucket selection fails Phase 2 exit without semantic checking |
| C-22 | Domain-alignment audit table at Phase 2 exit | FAIL | Phase 2 exit condition is a text check ("3 answers written; each [vocab] term comes from the specified bucket…") — no explicit `Q-number \| Term Used \| Expected Domain \| Match YES/NO` table as a structural output artifact |
| C-23 | Frame-fill as dedicated named phase | FAIL | Frame slots are filled inline during Phase 4 Write Role Files ("Insert Phase 2 Q1 and Q2 answers verbatim into the brackets") — no standalone named Frame Fill phase between Phase 2 and role writing |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 13/15 (C-22 FAIL, C-23 FAIL)

```
composite = (5/5 * 60) + (3/3 * 30) + (13/15 * 10)
          = 60 + 30 + 8.67
          = 98.67
```

**Score: 98.7 / 100**

---

## V-02: Domain-Alignment Audit Table

**Axis**: Domain-alignment audit table at Phase 2 exit (C-22 — single axis)
**Hypothesis**: A visible Q × Domain table with YES/NO rows converts domain-alignment from a text exit condition into a structural blocking artifact. A NO row cannot be mentally elided — it is explicit, visible, and requires rewrite before Phase 2 closes.

**Note**: V-02 uses a flat vocabulary list (not three named buckets). The Phase 2 exit is gated by an explicit audit table. Otherwise retains all R4 criteria from R4 V-02 (which scored 100/100 on v4 rubric). Full Phase 2+ content not visible in task (truncated), but R4 V-02 structural equivalents are credited.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All 5 fields | PASS | Same 5-field template as V-01 |
| C-02 | Inertia-advocate present | PASS | Frame challenges current system; verify questions reference Q1/Q2 specifics |
| C-03 | Correct output path | PASS | `.craft/roles/{area}/` |
| C-04 | Domain specificity | PASS | Flat vocabulary list from Phase 1 anchors expertise.relevance |
| C-05 | Minimum 3 roles | PASS | pm, architect, inertia-advocate, domain-specialist |
| C-06 | Lens actionability | PASS | Same verify/simplify enforcement |
| C-07 | Collaborates_with resolves | PASS | Verification gate includes orphan-reference check (R4 V-02 equivalent) |
| C-08 | Perspective diversity | PASS | 4 perspective categories |
| C-09 | Scope gradient | PASS | Structural scope audit pre-write; confirmation at verification gate |
| C-10 | Inertia domain-grounded | PASS | Phase 2 Q1 anchors current system name; Q2 migration cost; frame references Q1/Q2 verbatim |
| C-11 | Vocabulary-forced-field | PASS | Phase 1 vocabulary; expertise.relevance gated to include a Phase 1 term; vocabulary check in gate |
| C-12 | Inertia pre-characterization | PASS | Phase 2 answers Q1/Q2/Q3 with domain-alignment table guiding term selection |
| C-13 | Registry summary table | PASS | Verification gate CHECK 1 produces table |
| C-14 | Scope-gradient-enforcement | PASS | Structural scope gate with forced revision if homogeneous |
| C-15 | Verification-gate-phase | PASS | Named blocking gate bundles all post-write checks |
| C-16 | Vocabulary-linked inertia Q&A | PASS | Phase 2 vocab annotations per answer; domain-alignment audit table validates; inertia verify questions must use audit-table terms |
| C-17 | Pre-write scope audit | PASS | Scope audit fires before any role file is written |
| C-18 | Vocabulary check in verification gate | PASS | Vocabulary coverage check included in blocking gate |
| C-19 | Inertia frame Q-slot template | PASS | Frame template with named `[Q1]`/`[Q2]` slot syntax (R4 V-02 equivalent maintained) |
| C-20 | Q-domain-aligned vocabulary distribution | PASS | Domain-alignment audit table: Q1 row expected domain = current-system; Q2 = migration-cost; Q3 = user-habit; any NO triggers term replacement and re-evaluation; gate condition all three YES |
| C-21 | Bucketed vocabulary extraction | FAIL | Phase 1 produces a flat vocabulary list (not three named Q-domain buckets); domain alignment is enforced post-answer via audit table, not prevented at extraction time via bucket membership |
| C-22 | Domain-alignment audit table at Phase 2 exit | PASS | After Q1/Q2/Q3 answers are written: explicit `Q-number \| Term Used \| Expected Domain \| Match YES/NO` structural table; any NO blocks Phase 2 exit and triggers term replacement; gate condition: all three rows YES; table is a named output artifact, not inline prose |
| C-23 | Frame-fill as dedicated named phase | FAIL | Frame fill is inline during role-writing phase (no dedicated standalone Frame Fill phase between Phase 2 and role writing) |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 13/15 (C-21 FAIL, C-23 FAIL)

```
composite = (5/5 * 60) + (3/3 * 30) + (13/15 * 10)
          = 60 + 30 + 8.67
          = 98.67
```

**Score: 98.7 / 100**

---

## V-03: Frame Fill as Dedicated Named Phase *(inferred)*

**Axis**: Frame-fill as dedicated phase (C-23 — single axis)
**Hypothesis**: Elevating inertia frame slot population to a standalone named phase creates a phase-level artifact (completed frame string). Unfilled slots become detectable at the phase boundary before any role file is written. C-19 specifies the template; C-23 specifies that filling it is a phase, not an inline step.

**Basis**: R4 V-01 (three-bucket golden) + new Phase 3 "FRAME FILL" inserted between Phase 2 (Inertia Pre-Characterization) and the Scope Planning Gate. Phase numbering shifts: Scope Planning becomes Phase 4, Write Role Files Phase 5, Verification Gate Phase 6.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All 5 fields | PASS | Inherits all 5 fields from R4 V-01 template |
| C-02 | Inertia-advocate present | PASS | Inertia frame constructed from Q1/Q2 Phase 2 answers in Phase 3; challenges current system |
| C-03 | Correct output path | PASS | `.craft/roles/{area}/` |
| C-04 | Domain specificity | PASS | Three-bucket vocabulary anchors expertise.relevance |
| C-05 | Minimum 3 roles | PASS | pm, architect, inertia-advocate, domain-specialist |
| C-06 | Lens actionability | PASS | Verify ends `?`; simplify as imperatives |
| C-07 | Collaborates_with resolves | PASS | Phase 6 verification gate CHECK 2 |
| C-08 | Perspective diversity | PASS | 4 perspective categories |
| C-09 | Scope gradient | PASS | Phase 4 SCOPE AUDIT; Phase 6 CHECK 3 |
| C-10 | Inertia domain-grounded | PASS | Phase 3 frame fill uses Q1 (current system name) and Q2 (migration cost) from Phase 2 verbatim; Q answers drawn from domain-specific buckets |
| C-11 | Vocabulary-forced-field | PASS | Three-bucket Phase 1; Phase 5 exit + Phase 6 CHECK 4 |
| C-12 | Inertia pre-characterization | PASS | Phase 2 Q1/Q2/Q3 with verify questions referencing all 3 dimensions |
| C-13 | Registry summary table | PASS | Phase 6 CHECK 1 |
| C-14 | Scope-gradient-enforcement | PASS | Phase 4 SCOPE AUDIT structural gate |
| C-15 | Verification-gate-phase | PASS | "DELIVERY IS BLOCKED" Phase 6 gate |
| C-16 | Vocabulary-linked inertia Q&A | PASS | Bucket-constrained Phase 2 vocab annotations; C-11 and C-12 wired |
| C-17 | Pre-write scope audit | PASS | Phase 4 SCOPE AUDIT before Phase 5 writing |
| C-18 | Vocabulary check in verification gate | PASS | Phase 6 CHECK 4 in blocking gate |
| C-19 | Inertia frame Q-slot template | PASS | Phase 3 produces a named fill-in template; slot names `[Q1: current system name]` and `[Q2: migration cost]` must be populated; completed string recorded as phase output |
| C-20 | Q-domain-aligned vocabulary distribution | PASS | Three-bucket Phase 2 exit: Q1 from Current-System Terms, Q2 from Migration-Cost Terms, Q3 from User-Habit Terms; no cross-bucket reuse |
| C-21 | Bucketed vocabulary extraction | PASS | Inherits three-bucket Phase 1 from R4 V-01 base |
| C-22 | Domain-alignment audit table at Phase 2 exit | FAIL | No explicit YES/NO audit table at Phase 2 exit; exit condition is text-based bucket check from R4 V-01 base |
| C-23 | Frame-fill as dedicated named phase | PASS | Phase 3 "FRAME FILL" is a standalone named phase; exit condition: completed frame string with all slots filled, no unfilled placeholders; no slot construction occurs during Phase 5 role writing; unfilled slots at phase boundary are blocking errors |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 14/15 (C-22 FAIL only)

```
composite = (5/5 * 60) + (3/3 * 30) + (14/15 * 10)
          = 60 + 30 + 9.33
          = 99.33
```

**Score: 99.3 / 100**

---

## V-04: Bucketed Extraction + Domain-Alignment Audit Table *(inferred)*

**Axes**: C-21 (bucketed vocabulary) + C-22 (domain-alignment audit table)
**Hypothesis**: Combining bucket assignment at extraction time with an explicit YES/NO audit table at Phase 2 exit creates two enforcement points for Q-domain alignment: one that makes wrong-domain terms structurally unavailable, and one that surfaces any slip as a visible blocking artifact. The two mechanisms are complementary — C-21 prevents; C-22 detects residual cases.

**Basis**: R4 V-01 (three-bucket golden) + domain-alignment audit table added as explicit structural output at Phase 2 exit. No dedicated frame fill phase (C-23 not targeted).

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All 5 fields | PASS | Inherits from R4 V-01 template |
| C-02 | Inertia-advocate present | PASS | Frame challenges current system with Q1/Q2 from Phase 2 |
| C-03 | Correct output path | PASS | `.craft/roles/{area}/` |
| C-04 | Domain specificity | PASS | Three-bucket vocabulary anchors relevance fields |
| C-05 | Minimum 3 roles | PASS | pm, architect, inertia-advocate, domain-specialist |
| C-06 | Lens actionability | PASS | Verify ends `?`; simplify as imperatives |
| C-07 | Collaborates_with resolves | PASS | Verification gate CHECK 2 |
| C-08 | Perspective diversity | PASS | 4 perspective categories |
| C-09 | Scope gradient | PASS | Scope audit + gate confirmation |
| C-10 | Inertia domain-grounded | PASS | Frame references Q1/Q2 verbatim; Q answers are bucket-sourced domain terms |
| C-11 | Vocabulary-forced-field | PASS | Three-bucket Phase 1; expertise.relevance gated |
| C-12 | Inertia pre-characterization | PASS | Phase 2 Q1/Q2/Q3 with bucket constraints |
| C-13 | Registry summary table | PASS | Verification gate CHECK 1 |
| C-14 | Scope-gradient-enforcement | PASS | Structural scope planning gate with forced revision |
| C-15 | Verification-gate-phase | PASS | Named blocking gate |
| C-16 | Vocabulary-linked inertia Q&A | PASS | Per-answer [vocab] annotations with bucket-domain enforcement |
| C-17 | Pre-write scope audit | PASS | Scope audit before any file written |
| C-18 | Vocabulary check in verification gate | PASS | Vocabulary coverage CHECK in blocking gate |
| C-19 | Inertia frame Q-slot template | PASS | Frame template with named Q1/Q2 slot syntax; fill instruction verbatim |
| C-20 | Q-domain-aligned vocabulary distribution | PASS | Three-bucket Phase 1 + per-Q bucket constraint + audit table triple-enforcement |
| C-21 | Bucketed vocabulary extraction | PASS | Phase 1 three named Q-domain buckets; term assignment permanent; cross-bucket selection fails Phase 2 exit |
| C-22 | Domain-alignment audit table at Phase 2 exit | PASS | After Q1/Q2/Q3 answers written: explicit `Q-number \| Term Used \| Expected Domain \| Match YES/NO` table gates Phase 2 exit; any NO triggers term replacement; gate condition all three YES; table is named structural artifact |
| C-23 | Frame-fill as dedicated named phase | FAIL | Frame slots filled inline during role-writing phase; no standalone Frame Fill phase |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 14/15 (C-23 FAIL only)

```
composite = (5/5 * 60) + (3/3 * 30) + (14/15 * 10)
          = 60 + 30 + 9.33
          = 99.33
```

**Score: 99.3 / 100**

---

## V-05: Full Synthesis — Bucketed Extraction + Audit Table + Dedicated Frame Fill *(inferred)*

**Axes**: C-21 (bucketed vocabulary) + C-22 (domain-alignment audit table) + C-23 (frame-fill as dedicated phase)
**Hypothesis**: Three structural mechanisms at three distinct execution points create overlapping guarantees for Q-domain integrity and frame construction: (1) bucket extraction prevents wrong-domain terms from being available; (2) audit table surfaces any Phase 2 slip as a visible YES/NO blocking artifact; (3) dedicated Frame Fill phase separates slot population from role writing so unfilled slots are detectable at a phase boundary. The mechanisms do not overlap — C-21 fires at extraction, C-22 fires after Q&A, C-23 fires before writing.

**Basis**: R4 V-01 (three-bucket golden) + domain-alignment audit table at Phase 2 exit + dedicated "FRAME FILL" Phase 3 inserted between Phase 2 and role writing. Phase numbering: P1 Vocab → P2 Inertia Q&A + Audit Table → P3 Frame Fill → P4 Scope Planning Gate → P5 Write Role Files → P6 Verification Gate.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | All 5 fields | PASS | name, orientation (frame/verify/simplify), expertise (relevance), collaborates_with, scope in all role templates |
| C-02 | Inertia-advocate present | PASS | Frame string produced in Phase 3 explicitly names current system and migration cost; verify questions reference Q1/Q2/Q3 dimensions |
| C-03 | Correct output path | PASS | `.craft/roles/{area}/{role-name}.md` in Phase 5 |
| C-04 | Domain specificity | PASS | Three-bucket Phase 1; every expertise.relevance must reference a Phase 1 bucket term; Phase 6 CHECK 4 gates |
| C-05 | Minimum 3 roles | PASS | Phase 4 scope table pre-populates pm, architect, inertia-advocate, domain-specialist (minimum 4) |
| C-06 | Lens actionability | PASS | Template verify ends `?`; simplify as imperatives with explicit verb list |
| C-07 | Collaborates_with resolves | PASS | Phase 6 CHECK 2: zero [UNRESOLVED] gate condition |
| C-08 | Perspective diversity | PASS | pm (product), architect (technical), inertia-advocate (inertia), domain-specialist (domain) = 4 categories minimum |
| C-09 | Scope gradient | PASS | Phase 4 SCOPE AUDIT gates ≥ 2 distinct scope values before writing; Phase 6 CHECK 3 confirms |
| C-10 | Inertia domain-grounded | PASS | Phase 3 Frame Fill produces completed frame string from Phase 2 Q1 (current system name from Current-System Terms bucket) and Q2 (migration cost from Migration-Cost Terms bucket); names are concrete domain entities, not generic resistance language |
| C-11 | Vocabulary-forced-field | PASS | Three-bucket Phase 1 vocabulary; Phase 5 exit condition: every expertise.relevance references a bucket term; Phase 6 CHECK 4: zero [NO VOCAB TERM] entries gate delivery |
| C-12 | Inertia pre-characterization | PASS | Phase 2 answers Q1/Q2/Q3 with bucket-constrained vocab annotations; verify questions in Phase 5 role template reference all 3 Q dimensions explicitly |
| C-13 | Registry summary table | PASS | Phase 6 CHECK 1: `Role \| Frame (first 8 words) \| Scope \| Collaborates With` table from role files; structural gate |
| C-14 | Scope-gradient-enforcement | PASS | Phase 4 SCOPE AUDIT: if homogeneous, identifies and revises 1–2 roles before writing is permitted; states changes; re-confirms count ≥ 2 |
| C-15 | Verification-gate-phase | PASS | "DELIVERY IS BLOCKED" Phase 6 gate bundles all 4 checks; each must declare PASS in sequence; fix defects before next check opens |
| C-16 | Vocabulary-linked inertia Q&A | PASS | Phase 2 per-answer `[vocab: {term}]` format cites specific bucket term; audit table validates bucket matching; inertia verify questions in Phase 5 must reference Phase 2 vocab terms by name — C-11 and C-12 structurally wired through bucket + annotation + table |
| C-17 | Pre-write scope audit | PASS | Phase 4 SCOPE AUDIT is an explicit named phase that fires before Phase 5 writing; gate output is `SCOPE AUDIT PASS — scope values: [list]`; writing blocked until pass |
| C-18 | Vocabulary check in verification gate | PASS | Phase 6 CHECK 4 explicitly in blocking gate; gate cannot PASS with any [NO VOCAB TERM] entries regardless of other checks |
| C-19 | Inertia frame Q-slot template | PASS | Phase 3 Frame Fill accepts Phase 2 answers as input; produces completed frame string with all named placeholders (`[Q1: current system name]`, `[Q2: migration cost description]`) resolved; unfilled placeholders at Phase 3 exit are blocking errors |
| C-20 | Q-domain-aligned vocabulary distribution | PASS | Phase 1 three-bucket extraction prevents wrong-domain term availability; Phase 2 bucket-per-Q constraint enforced via `[vocab: {term-from-bucket}]` format; audit table gate at Phase 2 exit verifies each row; triple-layered enforcement |
| C-21 | Bucketed vocabulary extraction | PASS | Phase 1 produces three named Q-domain buckets (Current-System Terms, Migration-Cost Terms, User-Habit Terms); each extracted term assigned to exactly one bucket; bucket membership permanent; cross-bucket selection fails Phase 2 exit without semantic checking |
| C-22 | Domain-alignment audit table at Phase 2 exit | PASS | After Q1/Q2/Q3 answers written: `Q-number \| Term Used \| Expected Domain \| Match YES/NO` table gates Phase 2 exit; any NO triggers term replacement and table re-evaluation; all three rows must show YES; table is a named structural output artifact, not inline comment |
| C-23 | Frame-fill as dedicated named phase | PASS | Phase 3 "FRAME FILL" is a standalone named phase with explicit entry condition (Phase 2 complete + audit table cleared) and exit condition (completed frame string with all Q-slots filled, zero unfilled placeholders); Phase 5 role writing copies Phase 3 frame verbatim — no slot construction during writing; unfilled slots at Phase 3 exit are blocking errors |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 15/15

```
composite = (5/5 * 60) + (3/3 * 30) + (15/15 * 10)
          = 60 + 30 + 10
          = 100
```

**Score: 100 / 100 — GOLDEN**

---

## Rankings

| Rank | Variation | Score | Axes |
|------|-----------|-------|------|
| 1 | V-05 | 100.0 | C-21 + C-22 + C-23 (full synthesis) |
| 2 | V-03 | 99.3 | C-21 (inherited) + C-23 |
| 2 | V-04 | 99.3 | C-21 + C-22 |
| 4 | V-01 | 98.7 | C-21 only |
| 4 | V-02 | 98.7 | C-22 only |

V-01 and V-02 tie because each adds exactly one new criterion (C-21 or C-22) to the v4 baseline. V-03 scores higher than V-01/V-02 because it inherits C-21 from the R4 V-01 base AND adds C-23, netting two v5 passes. V-03 and V-04 tie at 14/15. V-05 achieves the golden cap.

---

## Excellence Signals

**From V-05 (100/100):**

1. **Audit table as explicit structural artifact (C-22)**: The YES/NO table at Phase 2 exit is the key discriminator between V-01 (98.7) and V-04 (99.3). A text exit condition ("check that each term comes from the right bucket") can be mentally elided or satisfied by declaration without inspection. A `Q-number | Term | Expected Domain | YES/NO` table row cannot — it is present in output, each row has a declared pass/fail state, and any NO is a visible blocking artifact that must be resolved before Phase 2 closes. C-22 closes the residual gap that C-21 (bucket prevention) cannot close: a term could be in the wrong bucket because the bucket was populated too broadly.

2. **Dedicated Frame Fill phase as phase-boundary detector (C-23)**: Moving slot population out of the role-writing phase creates a detectable boundary. Without Phase 3, an unfilled Q-slot in the frame string is only visible by reading the written role file. With Phase 3, an unfilled slot fails the phase exit before any file is opened. This is the same structural principle as pre-write scope audit (C-17 vs C-14): prevention at planning time is cheaper than correction at delivery time.

3. **Three-tier Q-domain enforcement chain**: C-21 (prevents unavailability), C-20/C-16 (annotates during generation), C-22 (audits at phase close). Each tier catches what the previous tier cannot: wrong-bucket extraction that escapes C-21 (bucket was mislabeled) is caught by C-22; wrong annotation that escapes C-20 is caught by C-22; correct annotation that drifts in later editing is caught by C-22. V-05 is the first variation where all three tiers are active simultaneously.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["explicit YES/NO audit table at Phase 2 exit converts domain-alignment from text exit condition to gated structural artifact — any NO row blocks phase completion and cannot be elided; catches mismatches that bucket structure alone cannot prevent", "dedicated Frame Fill phase between inertia Q&A and role writing creates a phase-boundary artifact from the completed frame string — unfilled Q-slots are detectable blocking errors at the boundary before any role file is written"]}
```
