Here is the complete v9 rubric:

---

# crew-roles rubric — v9

## Changes from v8

Three new aspirational criteria extracted from R14 variations V-01, V-02, V-03. Each closes a gap identified in the R14 baseline assessment.

**C-30 — Inertia-first write order gate** (from V-01):
C-10 requires domain-grounded inertia framing. A skill that writes roles in open order satisfies C-10 only if the output happens to be correct — back-pressure scope drift from later-planned roles can silently contaminate framing written after the fact. The sufficient condition is a structural write-ordering gate: an `INERTIA-ADVOCATE WRITTEN` gate fires before any other role is planned or written, confirming (1) the file is written and (2) the domain framing contains at least one named system, cost, or habit from Phase 2. Writing any other role before the gate passes is a blocking error. C-30 requires the mechanism; C-10 requires the output. V-01 (R14): gate fires before Step 3; C-10 moves from PARTIAL to PASS.

**C-31 — Vocab plan-to-write binding** (from V-02):
C-11 / CHECK 4A is a post-write set-level coverage check: if any `expertise.relevance` contains a vocab term, the check passes — even if one role silently dropped its planned term during authoring. The sufficient condition is a row-by-row binding check: Phase 5 planning table adds a `Planned-Vocab-Term` column; CHECK 4B compares planned term vs. written field per role and emits `[{role}: planned {term}, written expertise.relevance lacks it — VOCAB BINDING MISMATCH]`. Structurally analogous to C-29 (scope) and C-26 (annotation row-ID). V-02 (R14): Phase 5 column + CHECK 4B closes Gap-2; C-11 moves from PARTIAL to PASS.

**C-32 — Inline per-role LENS AUDIT gate** (from V-03):
C-06 (recommended) requires `orientation.verify` to be `?`-terminated and `orientation.simplify` to start with an imperative verb. A post-write scan can fix violations after the fact, satisfying C-06. The aspirational condition is an inline gate: a `LENS AUDIT` block executes immediately after each role is written, before advancing to the next, emitting `[LENS AUDIT FAIL: {role} — {dimension}: {issue}]` on any violation. C-06 requires correct output; C-32 requires the per-role gate ran during authoring. A post-write fix satisfies C-06 but not C-32. V-03 (R14): inline LENS AUDIT per role in Phase 6; C-06 moves from PARTIAL to PASS.

**Formula updated**: `aspirational_pass / 24 * 10` (was `/21`). Each full pass = 0.417 pts.

---

## Criteria (full table)

### Essential (5)
C-01 All 5 fields | C-02 Inertia-advocate present | C-03 Correct output path | C-04 Domain specificity | C-05 Minimum 3 roles

### Recommended (3)
C-06 Lens actionability | C-07 Collaborates_with resolves | C-08 Perspective diversity

### Aspirational (24)

| ID | Criterion | Introduced |
|----|-----------|-----------|
| C-09 | Scope gradient | v1 |
| C-10 | Inertia domain-grounded | v1 |
| C-11 | Vocabulary-forced-field | v2 / R1 |
| C-12 | Inertia pre-characterization | v2 / R1 |
| C-13 | Registry summary table | v3 / R2 |
| C-14 | Scope-gradient-enforcement | v3 / R2 |
| C-15 | Verification-gate-phase | v3 / R2 |
| C-16 | Vocabulary-linked inertia Q&A | v4 / R3 |
| C-17 | Pre-write scope audit | v4 / R3 |
| C-18 | Vocabulary check in verification gate | v4 / R3 |
| C-19 | Inertia frame Q-slot template | v5 / R4 |
| C-20 | Q-domain-aligned vocabulary distribution | v5 / R4 |
| C-21 | Bucketed vocabulary extraction | v5 / R4 |
| C-22 | Domain-alignment audit table at Phase 2 exit | v5 / R4 |
| C-23 | Frame Fill as phase-boundary artifact | v5 / R4 |
| C-24 | Audit-table full re-evaluation after replacement | v6 / R5 |
| C-25 | Frame-slot source citation in Frame Fill output | v6 / R5 |
| C-26 | Four-failure-mode annotation gate | v7 / R12 |
| C-27 | Source-phrase forensic citation | v7 / R12 |
| C-28 | Five-failure-mode annotation gate | v8 / R13 |
| C-29 | Scope plan-to-write binding | v8 / R13 |
| **C-30** | **Inertia-first write order gate** | **v9 / R14 V-01** |
| **C-31** | **Vocab plan-to-write binding** | **v9 / R14 V-02** |
| **C-32** | **Inline per-role LENS AUDIT gate** | **v9 / R14 V-03** |

File written to `simulations/quest/rubrics/crew-roles-rubric-v9-2026-03-17.md`.
 Phase 5 (or equivalent)
  must include a `Planned-Vocab-Term` column in the role planning table before authoring
  begins. CHECK 4B (or equivalent) must emit the mismatch flag before the verification gate
  (C-15) closes. C-11 / CHECK 4A confirms overall vocabulary coverage; C-31 / CHECK 4B
  confirms per-role binding. V-02 (R14) demonstrates: Phase 5 `Planned-Vocab-Term` column
  added; CHECK 4B row-by-row binding closes Gap-2; C-11 moves from PARTIAL to PASS.

- Added **C-32 Inline per-role LENS AUDIT gate** (aspirational): C-06 (recommended)
  requires `orientation.verify` fields to be `?`-terminated and `orientation.simplify`
  fields to start with an imperative verb. A post-write scan can satisfy C-06 by correcting
  violations after all roles are written, but it cannot prevent lens violations from
  propagating into inter-role cross-references or `collaborates_with` framings written while
  the violation existed. The sufficient condition is an inline per-role gate: a `LENS AUDIT`
  block executes immediately after each role is written, before advancing to the next role.
  The audit checks: (1) `orientation.verify` is `?`-terminated; (2) `orientation.simplify`
  starts with an imperative verb. On any violation the gate emits `[LENS AUDIT FAIL:
  {role} — {dimension}: {issue}]` and blocks advancement to the next role until the
  violation is resolved. C-06 requires the output to satisfy lens constraints; C-32 requires
  that the per-role gate was executed during authoring. A role set that passes C-06 via
  post-write fix satisfies the recommended criterion; only a skill that ran the inline gate
  for every role satisfies C-32. V-03 (R14) demonstrates: inline `LENS AUDIT` block per
  role in Phase 6; C-06 moves from PARTIAL to PASS; C-32 gate present and independently
  verifiable.

- **Formula updated**: `aspirational_pass / 24 * 10` (was `/21`). Twenty-four aspirational
  criteria; each full pass contributes 0.417 points. Partial credit rule unchanged.

---

## Criteria

### Essential — all 5 must PASS for full essential score

| ID   | Criterion                | Description |
|------|--------------------------|-------------|
| C-01 | All 5 fields             | Every role file contains all 5 required fields: `name`, `orientation`, `expertise`, `collaborates_with`, `scope` |
| C-02 | Inertia-advocate present | At least one role has `orientation.frame` explicitly challenging the status quo; verify questions reference why the current approach is insufficient |
| C-03 | Correct output path      | Roles written to `.craft/roles/{area}/` |
| C-04 | Domain specificity       | `expertise.relevance` is anchored to the specific domain of the input; no generic engineering language |
| C-05 | Minimum 3 roles          | Output contains at least 3 roles, including the inertia-advocate |

### Recommended — partial credit (0.5 per PARTIAL)

| ID   | Criterion                    | Description |
|------|------------------------------|-------------|
| C-06 | Lens actionability           | `orientation.verify` fields are questions (`?`); `orientation.simplify` fields are imperatives; examples reinforce the constraint |
| C-07 | Collaborates_with resolves   | Every `collaborates_with` value matches the name of another file in the registry; no placeholder text or unresolved references at delivery |
| C-08 | Perspective diversity        | Roles span at least 3 distinct perspective categories (e.g., product, technical, inertia, domain-specialist); no category monopoly |

### Aspirational — partial credit (0.5 per PARTIAL); denominator 24

| ID   | Criterion                                       | Description |
|------|-------------------------------------------------|-------------|
| C-09 | Scope gradient                                  | Roles span at least 2 distinct scope values (e.g., `team`, `cross-team`, `org`); no homogeneous scope set |
| C-10 | Inertia domain-grounded                         | The inertia-advocate framing names the specific current system, migration cost, or user habit — not generic resistance language |
| C-11 | Vocabulary-forced-field                         | Phase 1 produces a named vocabulary list extracted from input; every `expertise.relevance` field must reference at least one vocabulary term |
| C-12 | Inertia pre-characterization                    | Before writing the inertia-advocate, the skill answers 3 explicit questions: (1) current system name, (2) migration costs, (3) user habits; verify questions must reference at least 2 of these 3 dimensions |
| C-13 | Registry summary table                          | A `Role \| Orientation \| Scope \| Collaborates With` table appears in output after all roles are written; forces orphan-reference and scope-homogeneity checks at execution time |
| C-14 | Scope-gradient-enforcement                      | A structural step after writing checks scope diversity; if all roles share the same scope value, the skill identifies and revises 1-2 roles before delivery — structural gate, not soft instruction |
| C-15 | Verification-gate-phase                         | All post-write structural checks (registry summary table, orphan-reference check, scope-gradient check) are bundled into a single named gate that explicitly blocks delivery until all pass; checks are not scattered across instructions |
| C-16 | Vocabulary-linked inertia Q&A                   | Each Q1/Q2/Q3 answer in the inertia pre-characterization references at least one term from the Phase 1 vocabulary; C-11 and C-12 are structurally wired, not independently satisfied |
| C-17 | Pre-write scope audit                           | Before any roles are written, a SCOPE AUDIT surveys the planned role set and assigns scope values; writing is blocked until >= 2 distinct scope values appear in the plan — prevention, not correction; structural gate before authoring |
| C-18 | Vocabulary check in verification gate           | The verification gate includes an explicit vocabulary coverage check confirming every `expertise.relevance` references a Phase 1 vocabulary term; the gate does not PASS without this check, regardless of orphan and scope checks passing |
| C-19 | Inertia frame Q-slot template                   | The inertia-advocate `orientation.frame` is a fill-in template with explicit Q1 and Q2 slots populated from Phase 2 answers; the frame text contains named placeholders (e.g., `[Q1 current system]`, `[Q2 migration cost]`) that must be filled, not a soft instruction to reference them |
| C-20 | Q-domain-aligned vocabulary distribution        | Each Q1/Q2/Q3 answer references a vocabulary term whose domain aligns with that Q dimension: Q1 uses a current-system term, Q2 a migration-cost term, Q3 a user-habit term; same-term reuse across all three answers fails this criterion |
| C-21 | Bucketed vocabulary extraction                  | Phase 1 produces three named Q-domain buckets — Current-System Terms, Migration-Cost Terms, User-Habit Terms — rather than a flat vocabulary list; each extracted term is assigned to its bucket during Phase 1; Q1/Q2/Q3 answers in Phase 2 must draw from their respective buckets; cross-bucket selection fails Phase 2 exit without requiring semantic checking at answer time |
| C-22 | Domain-alignment audit table at Phase 2 exit    | After Q1/Q2/Q3 answers are written, a structured audit table (Q-number \| Term Used \| Expected Domain \| Match YES/NO) gates Phase 2 exit; any NO entry triggers term replacement and re-evaluation; all three rows must show YES before Phase 2 is complete; the table is a structural artifact in the output, not an inline comment |
| C-23 | Frame Fill as phase-boundary artifact           | Frame Fill is a dedicated named phase that produces the completed frame string before any role file is written; unfilled Q-slots are detectable blocking errors at the phase boundary; the phase exit condition requires a complete frame string, not an inline reference to Phase 2 answers |
| C-24 | Audit-table full re-evaluation after replacement | After any NO row in the Phase 2 audit table triggers term replacement, re-evaluation restarts from row 1 rather than re-scoring only the replaced row; the gate condition is "all three rows YES after full re-evaluation with no cross-row reuse" — evaluated as a unit, not per-row; incremental replacement satisfies the replaced row but can introduce a cross-row conflict invisible from the replacement row alone; V-05 demonstrates: audit table re-runs from Q1 after any replacement; gate condition evaluated against all three rows simultaneously before Phase 2 closes |
| C-25 | Frame-slot source citation in Frame Fill output  | The Frame Fill phase output annotates each slot with its verbatim source from Phase 2 — "Q1 slot <- Phase 2 Q1: [verbatim answer]" and "Q2 slot <- Phase 2 Q2: [verbatim answer]" — alongside the completed frame string; the completed frame string without source citations does not satisfy the Frame Fill phase exit condition; the verification gate CHECK includes a slot-source binding check; a mismatch (Q2 answer used in Q1 slot, or vice versa) is a blocking error |
| C-26 | Four-failure-mode annotation gate               | The three-handle annotation `[Q: Q{N} — vocab: {bucket-row-id} — {term}]` binds Q-number, row-ID, and term as three independently flaggable dimensions; the verification gate CHECK must expose ROW-ID MISMATCH as a fourth distinct failure mode separate from TERM MISMATCH — a question can carry the correct term while citing the wrong row; CHECK must emit `[ROW-ID MISMATCH: annotation says {row-A}, Phase 2 Q{N} used {row-B}]` as a structurally distinct flag before term verification runs |
| C-27 | Source-phrase forensic citation                 | After any term replacement triggered by a NO row in the Phase 2 audit table, the replacement record cites the verbatim Phase 1 source phrase alongside the new row identifier: `Phase 1 citation: {new-row-id} = "{new-term}" in Phase 1 {bucket-name}: "{source phrase}"`; a bucket-name re-assertion is non-verifiable; the forensic format requires the quoted source phrase to exist verbatim in Phase 1 output; CHECK 7 (or equivalent) validates the phrase before the replacement is accepted |
| C-28 | Five-failure-mode annotation gate               | The annotation verification gate adds a fifth failure mode `[TERM NOT IN QUESTION TEXT: annotation declares {term}, question body does not contain it]` beyond the four required by C-26; the declared term must appear verbatim or stem-matched in the question body before the annotation is accepted; structural validity of the annotation (correct Q-number, row-ID, and term match against Phase 2) is necessary but not sufficient; CHECK 6 (or equivalent) emits the fifth flag independently |
| C-29 | Scope plan-to-write binding                     | A row-by-row binding check compares each role's planned scope (from the pre-write scope audit, C-17) to its written scope and emits `[{role}: planned {scope-A}, written {scope-B} — SCOPE BINDING MISMATCH]` for any per-role divergence; this check runs before the verification gate (C-15) closes and blocks delivery on any mismatch; post-write diversity confirmation (C-14) is necessary but not sufficient; per-role binding (C-29) is the sufficient condition; CHECK 3B (or equivalent) emits the binding mismatch flag independently of whether the post-write diversity count still satisfies >= 2 distinct values |
| C-30 | Inertia-first write order gate                  | The inertia-advocate is the first role written; an explicit `INERTIA-ADVOCATE WRITTEN` gate fires before any other role is planned or written and confirms: (1) the inertia-advocate file is written, (2) the domain framing contains at least one named system, cost, or habit from Phase 2 answers; writing any other role before this gate passes is a blocking error; C-10 requires domain-grounded output; C-30 requires the write-ordering mechanism that enforces it structurally; a skill that writes roles in open order satisfies C-10 only if the output happens to be domain-grounded; back-pressure scope drift from other roles cannot contaminate the inertia framing when it is locked first; V-01 (R14) demonstrates: gate fires before Step 3; C-10 moves from PARTIAL to PASS |
| C-31 | Vocab plan-to-write binding                     | Phase 5 (or equivalent) planning table includes a `Planned-Vocab-Term` column assigning each role its required vocabulary term before authoring begins; CHECK 4B (or equivalent) performs a row-by-row binding comparison and emits `[{role}: planned {term}, written expertise.relevance lacks it — VOCAB BINDING MISMATCH]` for any per-role divergence; CHECK 4B runs before the verification gate (C-15) closes and blocks delivery on any mismatch; C-11 / CHECK 4A confirms set-level vocabulary coverage; C-31 / CHECK 4B is the sufficient per-role condition; structurally analogous to C-29 (scope binding) and C-26 (annotation row-ID binding); V-02 (R14) demonstrates: Phase 5 `Planned-Vocab-Term` column added; CHECK 4B row-by-row binding closes Gap-2; C-11 moves from PARTIAL to PASS |
| C-32 | Inline per-role LENS AUDIT gate                 | A `LENS AUDIT` block executes inline for each role immediately after it is written in Phase 6, before advancing to the next role; the audit checks: (1) `orientation.verify` is `?`-terminated, (2) `orientation.simplify` starts with an imperative verb; on any violation the gate emits `[LENS AUDIT FAIL: {role} — {dimension}: {issue}]` and blocks advancement until the violation is resolved; C-06 (recommended) requires the output to satisfy these lens constraints; C-32 (aspirational) requires that the per-role gate was executed during authoring — a post-write fix satisfies C-06 but not C-32; only a skill that ran the inline gate for every role satisfies C-32; V-03 (R14) demonstrates: inline `LENS AUDIT` block per role in Phase 6; C-06 moves from PARTIAL to PASS; C-32 gate present and independently verifiable |

---

## Scoring

### Formula

```
score = (essential_pass / 5 * 50)
      + (recommended_pass / 3 * 33.75 + recommended_partial / 3 * 16.875)
      + (aspirational_pass / 24 * 10 + aspirational_partial / 24 * 5)
```

- Essential full pass: 50 pts (10 pts each)
- Recommended full pass: 33.75 pts; partial: 16.875 pts
- Aspirational full pass: 10 pts at 0.417 per criterion; partial: 5 pts at 0.208 per criterion
- Maximum score: 100

### Partial credit rule

PARTIAL applies when a criterion is structurally present but incompletely satisfied (e.g.,
the audit table exists but lacks one required column; the replacement record cites the
bucket name but omits the source phrase). FAIL applies when the structural artifact is
absent. PASS requires all conditions stated in the criterion description to be met.

---

## Criterion source map

| ID            | Introduced | Source |
|---------------|------------|--------|
| C-01 to C-05  | v1         | Base spec |
| C-06 to C-08  | v1         | Base spec |
| C-09 to C-10  | v1         | Base spec |
| C-11 to C-12  | v2         | R1 excellence signals |
| C-13 to C-15  | v3         | R2 excellence signals |
| C-16 to C-18  | v4         | R3 excellence signals |
| C-19 to C-21  | v5         | R4 excellence signals |
| C-22 to C-23  | v5         | R4 second-order patterns |
| C-24 to C-25  | v6         | R5 second-order patterns |
| C-26 to C-27  | v7         | R12 excellence signals ES-1, ES-2 |
| C-28 to C-29  | v8         | R13 excellence signals ES-1, ES-2 |
| C-30 to C-32  | v9         | R14 variations V-01, V-02, V-03 |
```
