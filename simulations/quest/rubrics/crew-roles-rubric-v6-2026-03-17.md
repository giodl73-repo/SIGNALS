Reading the R5 scorecard excellence signals and JSON `new_patterns`, then writing v6.

The two R5 patterns are:
1. **Audit table cannot be elided** — a YES/NO row is present in output; any NO is visible and requires resolution; closes the residual gap C-21 leaves (mislabeled bucket term escapes without the table)
2. **Frame Fill phase as phase-boundary artifact** — unfilled slots are detectable blocking errors at the phase boundary before any role file is written

C-22 and C-23 in v5 capture these at first-order. The R5 excellence signals also articulate a **second-order gap** in each:

- C-22 gap: incremental replacement after a NO row (only the replaced row re-scored) can introduce a cross-row conflict that a full re-evaluation would catch
- C-23 gap: the completed frame string is produced as phase output but its slot-source binding is implicit — a slot could be populated from the wrong Phase 2 answer with no structural detection

Those gaps become C-24 and C-25 in v6.

---

**crew-roles rubric v6**

**2 new criteria added (C-24 through C-25):**

| ID | Name | Source Pattern | What it closes |
|----|------|----------------|----------------|
| C-24 | Audit-table full re-evaluation after replacement | R5 ES-1: "any NO row blocks phase completion and cannot be elided; catches mismatches that bucket structure alone cannot prevent" | C-22 gates Phase 2 exit on all-YES; this enforces that re-evaluation after any term replacement restarts from row 1 -- incremental re-scoring satisfies an individual row but can introduce cross-row conflicts or cross-bucket reuse that a full pass detects |
| C-25 | Frame-slot source citation in Frame Fill output | R5 ES-2: "phase-boundary artifact from the completed frame string -- unfilled Q-slots are detectable blocking errors at the boundary" | C-23 requires Frame Fill to be a dedicated named phase; this enforces that each slot carry an explicit source citation (Q1 slot ← Phase 2 Q1 answer verbatim; Q2 slot ← Phase 2 Q2 answer verbatim) -- a completed frame string without citations cannot confirm correct slot-answer binding before role writing begins |

**Formula updated:** `aspirational_pass / 17 * 10` (was `/15`). Each full pass = 0.588 pts. Maximum score still 100.

---

**Changes from v5:**

- Added **C-24 Audit-table-full-re-evaluation** (aspirational): After any NO row in the Phase 2 audit table triggers term replacement, re-evaluation restarts from row 1 rather than re-scoring only the replaced row. The gate condition is "all three rows YES after full re-evaluation with no cross-row reuse" -- evaluated as a unit, not per-row. C-22 establishes the table as a blocking structural artifact; this closes the residual gap where incremental replacement satisfies the replaced row but introduces a cross-row conflict (e.g., replacement term is a synonym already used in another answer, or is drawn from the adjacent bucket, passing its own row but creating a reuse violation not visible from the replacement row alone). V-05 demonstrates: audit table re-runs from Q1 after any replacement; gate condition is evaluated against all three rows simultaneously before Phase 2 closes.

- Added **C-25 Frame-slot-source-citation** (aspirational): The Frame Fill phase output annotates each slot with its verbatim source from Phase 2 -- "Q1 slot ← Phase 2 Q1: [verbatim answer]" and "Q2 slot ← Phase 2 Q2: [verbatim answer]" -- alongside the completed frame string. The completed frame string without source citations does not satisfy the Frame Fill phase exit condition. The verification gate includes a slot-source binding check: Q1 slot drawn from Q1 answer and Q2 slot drawn from Q2 answer; a mismatch (Q2 answer used in Q1 slot, or vice versa) is a blocking error. C-23 requires Frame Fill to be a standalone named phase that produces the frame string before role writing; this closes the gap where a slot is populated from the wrong Phase 2 answer -- the error is structurally undetectable in C-23 alone because the frame string is complete and superficially correct. V-05 demonstrates: Frame Fill phase output includes citations; verification gate CHECK includes slot-binding verification before PASS.

- **Formula updated**: `aspirational_pass / 17 * 10` (was `/15`). Seventeen aspirational criteria; each full pass contributes 0.588 points. Partial credit rule unchanged.

---

**crew-roles rubric -- v6**

---

**Criteria**

**Essential** -- all 5 must PASS for full essential score:

| ID | Criterion | Description |
|----|-----------|-------------|
| C-01 | All 5 fields | Every role file contains all 5 required fields: `name`, `orientation`, `expertise`, `collaborates_with`, `scope` |
| C-02 | Inertia-advocate present | At least one role has `orientation.frame` explicitly challenging the status quo; verify questions reference why the current approach is insufficient |
| C-03 | Correct output path | Roles written to `.roles/{area}/` |
| C-04 | Domain specificity | `expertise.relevance` is anchored to the specific domain of the input; no generic engineering language |
| C-05 | Minimum 3 roles | Output contains at least 3 roles, including the inertia-advocate |

**Recommended** -- partial credit (0.5 per PARTIAL):

| ID | Criterion | Description |
|----|-----------|-------------|
| C-06 | Lens actionability | `orientation.verify` fields are questions (`?`); `orientation.simplify` fields are imperatives; examples reinforce the constraint |
| C-07 | Collaborates_with resolves | Every `collaborates_with` value matches the name of another file in the registry; no placeholder text or unresolved references at delivery |
| C-08 | Perspective diversity | Roles span at least 3 distinct perspective categories (e.g., product, technical, inertia, domain-specialist); no category monopoly |

**Aspirational** -- partial credit (0.5 per PARTIAL); denominator 17:

| ID | Criterion | Description |
|----|-----------|-------------|
| C-09 | Scope gradient | Roles span at least 2 distinct scope values (e.g., `team`, `cross-team`, `org`); no homogeneous scope set |
| C-10 | Inertia domain-grounded | The inertia-advocate framing names the specific current system, migration cost, or user habit -- not generic resistance language |
| C-11 | Vocabulary-forced-field | Phase 1 produces a named vocabulary list extracted from input; every `expertise.relevance` field must reference at least one vocabulary term |
| C-12 | Inertia pre-characterization | Before writing the inertia-advocate, the skill answers 3 explicit questions: (1) current system name, (2) migration costs, (3) user habits; verify questions must reference at least 2 of these 3 dimensions |
| C-13 | Registry summary table | A `Role \| Orientation \| Scope \| Collaborates With` table appears in output after all roles are written; forces orphan-reference and scope-homogeneity checks at execution time |
| C-14 | Scope-gradient-enforcement | A structural step after writing checks scope diversity; if all roles share the same scope value, the skill identifies and revises 1-2 roles before delivery -- structural gate, not soft instruction |
| C-15 | Verification-gate-phase | All post-write structural checks (registry summary table, orphan-reference check, scope-gradient check) are bundled into a single named gate that explicitly blocks delivery until all pass; checks are not scattered across instructions |
| C-16 | Vocabulary-linked inertia Q&A | Each Q1/Q2/Q3 answer in the inertia pre-characterization references at least one term from the Phase 1 vocabulary; C-11 and C-12 are structurally wired, not independently satisfied |
| C-17 | Pre-write scope audit | Before any roles are written, a SCOPE AUDIT surveys the planned role set and assigns scope values; writing is blocked until >= 2 distinct scope values appear in the plan -- prevention, not correction; structural gate before authoring |
| C-18 | Vocabulary check in verification gate | The verification gate includes an explicit vocabulary coverage check confirming every `expertise.relevance` references a Phase 1 vocabulary term; the gate does not PASS without this check, regardless of orphan and scope checks passing |
| C-19 | Inertia frame Q-slot template | The inertia-advocate `orientation.frame` is a fill-in template with explicit Q1 and Q2 slots populated from Phase 2 answers; the frame text contains named placeholders (e.g., `[Q1 current system]`, `[Q2 migration cost]`) that must be filled, not a soft instruction to reference them |
| C-20 | Q-domain-aligned vocabulary distribution | Each Q1/Q2/Q3 answer references a vocabulary term whose domain aligns with that Q dimension: Q1 uses a current-system term, Q2 a migration-cost term, Q3 a user-habit term; same-term reuse across all three answers fails this criterion |
| C-21 | Bucketed vocabulary extraction | Phase 1 produces three named Q-domain buckets -- Current-System Terms, Migration-Cost Terms, User-Habit Terms -- rather than a flat vocabulary list; each extracted term is assigned to its bucket during Phase 1; Q1/Q2/Q3 answers in Phase 2 must draw from their respective buckets; cross-bucket selection fails Phase 2 exit without requiring semantic checking at answer time |
| C-22 | Domain-alignment audit table at Phase 2 exit | After Q1/Q2/Q3 answers are written, a structured audit table (Q-number \| Term Used \| Expected Domain \| Match YES/NO) gates Phase 2 exit; any NO entry triggers term replacement and re-evaluation; all three rows must show YES before Phase 2 is complete; the table is a structural artifact in the output, not an inline comment |
| C-23 | Frame-fill as dedicated named phase | The inertia frame fill -- populating the Q1 and Q2 named slots from Phase 2 answers -- is a standalone named phase between Phase 2 and the role-writing phase(s); the completed frame string (all slots filled, no unfilled placeholders) is the phase output and is treated as an input to role writing; no slot construction occurs during role writing; unfilled slots at the phase boundary are a blocking error |
| C-24 | Audit-table full re-evaluation after replacement | After any NO row in the Phase 2 audit table triggers term replacement, re-evaluation restarts from row 1; the gate condition -- all three rows YES with no cross-row reuse -- is evaluated against all rows simultaneously; partial re-evaluation (re-scoring only the replaced row) fails the gate; this catches cross-row conflicts introduced by replacement (e.g., replacement term reused from another answer, or drawn from the adjacent bucket) that per-row re-scoring cannot detect |
| C-25 | Frame-slot source citation in Frame Fill output | The Frame Fill phase output annotates each slot with its verbatim source from Phase 2: "Q1 slot ← Phase 2 Q1: [verbatim answer]" and "Q2 slot ← Phase 2 Q2: [verbatim answer]", alongside the completed frame string; a frame string without source citations does not satisfy the Frame Fill phase exit condition; the verification gate includes a slot-source binding check confirming Q1 slot was drawn from Q1 answer and Q2 slot from Q2 answer; a mismatch (Q2 answer in Q1 slot, or vice versa) is a blocking error regardless of the frame string appearing complete |

---

**Formula**

```
score = (essential_pass / 5 * 60)
      + (recommended_pass / 3 * 30)   [PARTIAL = 0.5]
      + (aspirational_pass / 17 * 10) [PARTIAL = 0.5]

max = 60 + 30 + 10 = 100
aspirational full pass = 0.588 pts each
```

---

**Scoring Notes**

- **Essential**: binary per criterion; any FAIL caps essential score at 0 for that criterion
- **Recommended**: PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0; denominator is always 3
- **Aspirational**: PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0; denominator is always 17
- Aspirational criteria are additive; a FAIL on C-24 does not affect scoring of C-22

**Golden threshold**: all essential PASS + all recommended PASS + all 17 aspirational PASS = 100.0
