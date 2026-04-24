Reading the scorecard and JSON `new_patterns`, extracting two new criteria.

**ES-1** maps to **C-26**: the three-handle annotation already binds Q-number + row-ID + term, but row-ID binding is not independently flaggable in V-01's three-failure-mode gate — a question can carry the correct term while citing the wrong row. A fourth distinct flag `ROW-ID MISMATCH` is required.

**ES-2** maps to **C-27**: replacement records that re-assert a bucket name without quoting the verbatim Phase 1 source phrase cannot be cross-checked; a forensic citation format (`Phase 1 citation: {new-row-id} = "{new-term}" in Phase 1 {bucket-name}: "{source phrase}"`) closes the fabricated-row-ID path.

Formula bumps to `/19` (was `/17`). Each full pass = 0.526 pts.

---

```markdown
# crew-roles rubric — v7

---

## Changes from v6

- Added **C-26 Four-failure-mode annotation gate** (aspirational): The three-handle
  annotation `[Q: Q{N} — vocab: {bucket-row-id} — {term}]` carries three independently
  verifiable dimensions: Q-number, row-ID, and term. The verification gate CHECK must
  expose ROW-ID MISMATCH as a **fourth distinct failure mode**, separate from TERM
  MISMATCH. A question can carry the correct term while citing the wrong row (e.g., CS-2
  instead of CS-1 for the same term appearing in two row positions); three-failure-mode
  gates cannot detect this because term and Q-number both pass. CHECK 6 (or equivalent)
  must produce a flag `[ROW-ID MISMATCH: annotation says {row-A}, Phase 2 Q{N} used
  {row-B}]` that is structurally distinct from `[TERM MISMATCH]`. V-05 demonstrates:
  four-flag gate; ROW-ID MISMATCH is independently emitted before term verification runs.

- Added **C-27 Source-phrase forensic citation in replacement records** (aspirational):
  After any term replacement triggered by a NO row in the Phase 2 audit table, the
  replacement record quotes the verbatim Phase 1 source phrase alongside the new row
  identifier: `Phase 1 citation: {new-row-id} = "{new-term}" in Phase 1 {bucket-name}:
  "{source phrase}"`. A bucket-name re-assertion (`{new-row-id} confirmed in Phase 1
  {bucket-name} bucket`) is a non-verifiable re-assertion: a fabricated row identifier
  can produce a well-formed re-assertion that passes structural inspection. The forensic
  format requires the quoted source phrase to exist verbatim in Phase 1 output; CHECK 7
  (or equivalent) validates the match. V-05 demonstrates: replacement records include the
  quoted source phrase; CHECK 7 verifies the phrase against Phase 1 output before the
  replacement is accepted.

- **Formula updated**: `aspirational_pass / 19 * 10` (was `/17`). Nineteen aspirational
  criteria; each full pass contributes 0.526 points. Partial credit rule unchanged.

---

## Criteria

### Essential — all 5 must PASS for full essential score

| ID   | Criterion                | Description |
|------|--------------------------|-------------|
| C-01 | All 5 fields             | Every role file contains all 5 required fields: `name`, `orientation`, `expertise`, `collaborates_with`, `scope` |
| C-02 | Inertia-advocate present | At least one role has `orientation.frame` explicitly challenging the status quo; verify questions reference why the current approach is insufficient |
| C-03 | Correct output path      | Roles written to `.roles/{area}/` |
| C-04 | Domain specificity       | `expertise.relevance` is anchored to the specific domain of the input; no generic engineering language |
| C-05 | Minimum 3 roles          | Output contains at least 3 roles, including the inertia-advocate |

### Recommended — partial credit (0.5 per PARTIAL)

| ID   | Criterion                    | Description |
|------|------------------------------|-------------|
| C-06 | Lens actionability           | `orientation.verify` fields are questions (`?`); `orientation.simplify` fields are imperatives; examples reinforce the constraint |
| C-07 | Collaborates_with resolves   | Every `collaborates_with` value matches the name of another file in the registry; no placeholder text or unresolved references at delivery |
| C-08 | Perspective diversity        | Roles span at least 3 distinct perspective categories (e.g., product, technical, inertia, domain-specialist); no category monopoly |

### Aspirational — partial credit (0.5 per PARTIAL); denominator 19

| ID   | Criterion                              | Description |
|------|----------------------------------------|-------------|
| C-09 | Scope gradient                         | Roles span at least 2 distinct scope values (e.g., `team`, `cross-team`, `org`); no homogeneous scope set |
| C-10 | Inertia domain-grounded                | The inertia-advocate framing names the specific current system, migration cost, or user habit -- not generic resistance language |
| C-11 | Vocabulary-forced-field                | Phase 1 produces a named vocabulary list extracted from input; every `expertise.relevance` field must reference at least one vocabulary term |
| C-12 | Inertia pre-characterization           | Before writing the inertia-advocate, the skill answers 3 explicit questions: (1) current system name, (2) migration costs, (3) user habits; verify questions must reference at least 2 of these 3 dimensions |
| C-13 | Registry summary table                 | A `Role \| Orientation \| Scope \| Collaborates With` table appears in output after all roles are written; forces orphan-reference and scope-homogeneity checks at execution time |
| C-14 | Scope-gradient-enforcement             | A structural step after writing checks scope diversity; if all roles share the same scope value, the skill identifies and revises 1-2 roles before delivery -- structural gate, not soft instruction |
| C-15 | Verification-gate-phase                | All post-write structural checks (registry summary table, orphan-reference check, scope-gradient check) are bundled into a single named gate that explicitly blocks delivery until all pass; checks are not scattered across instructions |
| C-16 | Vocabulary-linked inertia Q&A          | Each Q1/Q2/Q3 answer in the inertia pre-characterization references at least one term from the Phase 1 vocabulary; C-11 and C-12 are structurally wired, not independently satisfied |
| C-17 | Pre-write scope audit                  | Before any roles are written, a SCOPE AUDIT surveys the planned role set and assigns scope values; writing is blocked until >= 2 distinct scope values appear in the plan -- prevention, not correction; structural gate before authoring |
| C-18 | Vocabulary check in verification gate  | The verification gate includes an explicit vocabulary coverage check confirming every `expertise.relevance` references a Phase 1 vocabulary term; the gate does not PASS without this check, regardless of orphan and scope checks passing |
| C-19 | Inertia frame Q-slot template          | The inertia-advocate `orientation.frame` is a fill-in template with explicit Q1 and Q2 slots populated from Phase 2 answers; the frame text contains named placeholders (e.g., `[Q1 current system]`, `[Q2 migration cost]`) that must be filled, not a soft instruction to reference them |
| C-20 | Q-domain-aligned vocabulary distribution | Each Q1/Q2/Q3 answer references a vocabulary term whose domain aligns with that Q dimension: Q1 uses a current-system term, Q2 a migration-cost term, Q3 a user-habit term; same-term reuse across all three answers fails this criterion |
| C-21 | Bucketed vocabulary extraction         | Phase 1 produces three named Q-domain buckets -- Current-System Terms, Migration-Cost Terms, User-Habit Terms -- rather than a flat vocabulary list; each extracted term is assigned to its bucket during Phase 1; Q1/Q2/Q3 answers in Phase 2 must draw from their respective buckets; cross-bucket selection fails Phase 2 exit without requiring semantic checking at answer time |
| C-22 | Domain-alignment audit table at Phase 2 exit | After Q1/Q2/Q3 answers are written, a structured audit table (Q-number \| Term Used \| Expected Domain \| Match YES/NO) gates Phase 2 exit; any NO entry triggers term replacement and re-evaluation; all three rows must show YES before Phase 2 is complete; the table is a structural artifact in the output, not an inline comment |
| C-23 | Frame Fill as phase-boundary artifact  | Frame Fill is a dedicated named phase that produces the completed frame string before any role file is written; unfilled Q-slots are detectable blocking errors at the phase boundary; the phase exit condition requires a complete frame string, not an inline reference to Phase 2 answers |
| C-24 | Audit-table full re-evaluation after replacement | After any NO row in the Phase 2 audit table triggers term replacement, re-evaluation restarts from row 1 rather than re-scoring only the replaced row; the gate condition is "all three rows YES after full re-evaluation with no cross-row reuse" -- evaluated as a unit, not per-row; incremental replacement satisfies the replaced row but can introduce a cross-row conflict (e.g., replacement term is a synonym already used in another answer, or is drawn from the adjacent bucket, passing its own row while creating a reuse violation invisible from the replacement row alone); V-05 demonstrates: audit table re-runs from Q1 after any replacement; gate condition is evaluated against all three rows simultaneously before Phase 2 closes |
| C-25 | Frame-slot source citation in Frame Fill output | The Frame Fill phase output annotates each slot with its verbatim source from Phase 2 -- "Q1 slot <- Phase 2 Q1: [verbatim answer]" and "Q2 slot <- Phase 2 Q2: [verbatim answer]" -- alongside the completed frame string; the completed frame string without source citations does not satisfy the Frame Fill phase exit condition; the verification gate CHECK includes a slot-source binding check: Q1 slot drawn from Q1 answer and Q2 slot drawn from Q2 answer; a mismatch (Q2 answer used in Q1 slot, or vice versa) is a blocking error; V-05 demonstrates: Frame Fill phase output includes citations; verification gate CHECK includes slot-binding verification before PASS |
| C-26 | Four-failure-mode annotation gate      | The three-handle annotation `[Q: Q{N} — vocab: {bucket-row-id} — {term}]` binds Q-number, row-ID, and term as three independently flaggable dimensions; the verification gate CHECK must expose ROW-ID MISMATCH as a **fourth distinct failure mode** separate from TERM MISMATCH -- a question can carry the correct term while citing the wrong row (e.g., annotation says CS-2, but Phase 2 Q1 selected CS-1), which three-failure-mode gates cannot detect because term and Q-number both pass; CHECK must emit `[ROW-ID MISMATCH: annotation says {row-A}, Phase 2 Q{N} used {row-B}]` as a structurally distinct flag before term verification runs; V-05 demonstrates: four-flag gate; ROW-ID MISMATCH is independently emitted |
| C-27 | Source-phrase forensic citation in replacement records | After any term replacement triggered by a NO row in the Phase 2 audit table, the replacement record cites the verbatim Phase 1 source phrase alongside the new row identifier: `Phase 1 citation: {new-row-id} = "{new-term}" in Phase 1 {bucket-name}: "{source phrase}"`; a bucket-name re-assertion (`{new-row-id} confirmed in Phase 1 {bucket-name} bucket`) is non-verifiable and permits fabricated row identifiers to pass structural inspection unchallenged; the forensic format requires the quoted source phrase to exist verbatim in Phase 1 output; CHECK 7 (or equivalent) validates the phrase against Phase 1 output before the replacement is accepted; V-05 demonstrates: replacement records include the quoted source phrase; CHECK 7 verifies the phrase against Phase 1 output before replacement is accepted |

---

## Scoring

### Formula

```
score = (essential_pass / 5 * 50)
      + (recommended_pass / 3 * 33.75 + recommended_partial / 3 * 16.875)
      + (aspirational_pass / 19 * 10 + aspirational_partial / 19 * 5)
```

- Essential full pass: 50 pts (10 pts each)
- Recommended full pass: 33.75 pts; partial: 16.875 pts
- Aspirational full pass: 10 pts at 0.526 per criterion; partial: 5 pts at 0.263 per criterion
- Maximum score: 100

### Partial credit rule

PARTIAL applies when a criterion is structurally present but incompletely satisfied (e.g.,
the audit table exists but lacks one required column; the replacement record cites the
bucket name but omits the source phrase). FAIL applies when the structural artifact is
absent. PASS requires all conditions stated in the criterion description to be met.

---

## Criterion source map

| ID   | Introduced | Source |
|------|------------|--------|
| C-01 to C-05  | v1 | Base spec |
| C-06 to C-08  | v1 | Base spec |
| C-09 to C-10  | v1 | Base spec |
| C-11 to C-12  | v2 | R1 excellence signals |
| C-13 to C-15  | v3 | R2 excellence signals |
| C-16 to C-18  | v4 | R3 excellence signals |
| C-19 to C-21  | v5 | R4 excellence signals |
| C-22 to C-23  | v5 | R4 second-order patterns |
| C-24 to C-25  | v6 | R5 second-order patterns |
| C-26 to C-27  | v7 | R12 excellence signals ES-1, ES-2 |
```

---

Two criteria added, denominator bumped to 19. The key structural distinction in v7:

- **C-26** separates row-ID binding from term binding in the annotation gate — a well-formed term with a wrong row ID is now a detectable failure mode, not a pass.
- **C-27** replaces re-assertion with forensic citation in replacement records — the quoted source phrase must exist verbatim in Phase 1 output, closing the path where a fabricated row ID produces a syntactically valid but unverifiable replacement record.
