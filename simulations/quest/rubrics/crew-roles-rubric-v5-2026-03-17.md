Written. Here is the complete v5 rubric:

---

**crew-roles rubric v5**

**3 new criteria added (C-21 through C-23):**

| ID | Name | Source Pattern | What it closes |
|----|------|----------------|----------------|
| C-21 | Bucketed vocabulary extraction | V-01 three-bucket Phase 1 (Current-System / Migration-Cost / User-Habit) | C-20 enforces alignment per-Q at answer time; this enforces it at extraction time via bucket assignment -- prevents cross-domain selection before Q&A begins |
| C-22 | Domain-alignment audit table at Phase 2 exit | V-02 post-answer Q x Domain table with YES/NO per row | C-20 enforces domain alignment through per-Q constraints; this makes mismatches visible as explicit NO artifacts that gate Phase 2 completion |
| C-23 | Frame-fill as dedicated named phase | V-03 standalone Phase 3 between Q&A and role writing | C-19 defines the frame as a Q-slot template; this elevates slot population to a phase-level artifact -- unfilled slots are detectable at a phase boundary before any file is written |

**Formula updated:** `aspirational_pass / 15 * 10` (was `/12`). Each full pass = 0.667 pts. Maximum score still 100.

---

**Changes from v4:**

- Added **C-21 Bucketed-Vocabulary-Extraction** (aspirational): Phase 1 organizes extracted vocabulary into three pre-labeled Q-domain buckets -- Current-System Terms, Migration-Cost Terms, User-Habit Terms -- rather than a flat list. Each term is assigned to its bucket during extraction; bucket membership makes cross-domain selection in Phase 2 a structural failure rather than a semantic check after answers are written. C-20 enforces Q-domain alignment by per-Q constraints at answer time; this enforces it earlier, at extraction time, so no misaligned term is available to select for the wrong Q. V-01 demonstrates: Phase 2 exit gate condition is "Q1 term drawn from Current-System Terms; Q2 from Migration-Cost Terms; Q3 from User-Habit Terms; no cross-bucket reuse."

- Added **C-22 Domain-Alignment-Audit-Table** (aspirational): After Q1/Q2/Q3 answers are written, a structured audit table (Q-number | Term Used | Expected Domain | Match YES/NO) gates Phase 2 exit. Any NO triggers term replacement; gate condition is all three rows YES. The table is a structural artifact in the output, not an inline comment. C-20 enforces alignment by constraining selection per Q; this enforces it by post-answer visibility -- mismatches appear as explicit NO entries that must be resolved. V-02 demonstrates: gate blocks on any NO row; rewrite replaces the offending term and the table re-evaluates.

- Added **C-23 Frame-Fill-As-Dedicated-Phase** (aspirational): The inertia frame fill is a standalone named phase between Phase 2 and any role-writing phase. The completed frame string (all slots filled, no unfilled placeholders) is produced as the phase output before file writing begins; no slot-filling occurs during role writing. C-19 defines the frame as a fill-in template with named Q-slots; this elevates the fill from an inline step in the inertia-advocate writing instruction to a phase-level artifact. Unfilled slots are detectable at the phase boundary. V-03 demonstrates: Phase 3 is named "Frame Fill" and must output a completed frame string before Phase 4 (role writing) may begin.

- **Formula updated**: `aspirational_pass / 15 * 10` (was `/12`). Fifteen aspirational criteria; each full pass contributes 0.667 points. Partial credit rule unchanged.

---

**crew-roles rubric -- v5**

---

**Criteria**

**Essential** -- all 5 must PASS for full essential score:

| ID | Criterion | Description |
|----|-----------|-------------|
| C-01 | All 5 fields | Every role file contains all 5 required fields: `name`, `orientation`, `expertise`, `collaborates_with`, `scope` |
| C-02 | Inertia-advocate present | At least one role has `orientation.frame` explicitly challenging the status quo; verify questions reference why the current approach is insufficient |
| C-03 | Correct output path | Roles written to `.craft/roles/{area}/` |
| C-04 | Domain specificity | `expertise.relevance` is anchored to the specific domain of the input; no generic engineering language |
| C-05 | Minimum 3 roles | Output contains at least 3 roles, including the inertia-advocate |

**Recommended** -- partial credit (0.5 per PARTIAL):

| ID | Criterion | Description |
|----|-----------|-------------|
| C-06 | Lens actionability | `orientation.verify` fields are questions (`?`); `orientation.simplify` fields are imperatives; examples reinforce the constraint |
| C-07 | Collaborates_with resolves | Every `collaborates_with` value matches the name of another file in the registry; no placeholder text or unresolved references at delivery |
| C-08 | Perspective diversity | Roles span at least 3 distinct perspective categories (e.g., product, technical, inertia, domain-specialist); no category monopoly |

**Aspirational** -- partial credit (0.5 per PARTIAL); denominator 15:

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

---

**Formula**

```
score = (essential_pass / 5 * 60)
      + (recommended_pass / 3 * 30)
      + (aspirational_pass / 15 * 10)
```

- PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0
- Essential: 5 criteria x 12 pts each = 60 pts max
- Recommended: 3 criteria x 10 pts each = 30 pts max
- Aspirational: 15 criteria x 0.667 pts each = 10 pts max
- Maximum score: 100

---

**Failure Mode Table** (C-21 through C-23 appended):

| Criterion | Common Failure Mode | Structural Fix |
|-----------|--------------------|-----------------|
| ... | (C-01 through C-20 unchanged) | ... |
| C-21 | Vocabulary is a flat list -- Q-domain alignment must be asserted per-answer rather than structurally enforced | Phase 1 extraction partitions output into three named buckets; each term domain is declared at extraction time; cross-bucket selection is structurally blocked rather than caught after writing |
| C-22 | Domain alignment is checked mentally or by instruction -- mismatches not surfaced as output artifacts | Post-Q&A audit table produces explicit YES/NO rows; any NO is a visible, gated blocking condition rather than a soft prompt to reconsider |
| C-23 | Frame fill is embedded in inertia-advocate writing step -- slot population can be skipped or deferred during role construction | Dedicated frame-fill phase produces completed frame string before writing begins; unfilled slots at phase boundary are blocking errors detectable without reading subsequent role files |

---

**Design note on C-21 vs C-20 vs C-22:**

These three criteria form a layered enforcement chain for Q-domain vocabulary alignment:

- **C-20** (v4): per-Q constraint at answer time -- the weakest gate, relies on instruction following
- **C-21** (v5): pre-Q bucket assignment at extraction time -- structurally blocks wrong-domain terms from being available
- **C-22** (v5): post-Q audit table -- makes any slip visible as an explicit NO artifact before the phase closes

A skill can satisfy C-20 through instruction; C-21 closes the gap by making misalignment impossible at source; C-22 closes the residual gap by making it auditable at Phase 2 exit. All three can coexist and are independently valuable.
verification gate; homogeneous set triggers forced revision |
| C-10 | Inertia framing is generic ("change is hard") | Pre-characterization block gates writing; current system must be named |
| C-11 | Domain specificity relies on instruction only -- regresses under drift | Phase 1 extraction produces a vocabulary list; every expertise.relevance must cite a term from it |
| C-12 | Inertia-advocate written without naming system/costs/habits | 3-question pre-characterization block appears before inertia-advocate; verify questions constrained to reference at least 2 of 3 answers |
| C-13 | No self-verification of orphan references or scope homogeneity | Post-write registry table forces both checks at execution time |
| C-14 | Scope gradient exists in template but is not enforced -- all roles collapse to same scope | Structural revision step: if homogeneous, name 1-2 roles to revise and revise before proceeding |
| C-15 | Orphan check, scope check, and table run as separate optional steps -- any can be skipped | Single named verification gate bundles all three; gate outcome (PASS/FAIL) is stated explicitly; delivery blocked on FAIL |
| C-16 | C-11 and C-12 both present but never linked -- vocabulary unused in inertia answers | Q1/Q2/Q3 template includes `(must reference a term from Phase 1 vocabulary)` constraint inline |
| C-17 | Scope is planned homogeneously then corrected post-write -- C-14 correction required | Pre-write SCOPE AUDIT assigns scope values to planned roles before authoring; writing blocked until plan shows diversity |
| C-18 | Vocabulary instruction present but not gated -- drops under compression | Vocabulary coverage check added as CHECK 4 (or equivalent) in the verification gate; gate does not complete without it |
| C-19 | Q1/Q2 referenced in frame by soft instruction -- omitted under model drift | Frame is a named template with `[Q1 current system]` and `[Q2 migration cost]` slot syntax; unfilled slots are detectable errors |
| C-20 | All three Q answers reference the same vocabulary term; cross-domain terms used for convenience | Q-number-to-term-domain mapping enforced: Q1 answer must reference a current-system term, Q2 a migration-cost term, Q3 a user-habit term |
| C-21 | Vocabulary is a flat list -- Q-domain alignment must be asserted per-answer rather than structurally enforced | Phase 1 extraction partitions output into three named buckets; each term domain is declared at extraction time; cross-bucket selection is structurally blocked rather than caught after writing |
| C-22 | Domain alignment is checked mentally or by instruction -- mismatches not surfaced as output artifacts | Post-Q&A audit table produces explicit YES/NO rows; any NO is a visible, gated blocking condition rather than a soft prompt to reconsider |
| C-23 | Frame fill is embedded in inertia-advocate writing step -- slot population can be skipped or deferred during role construction | Dedicated frame-fill phase produces completed frame string before writing begins; unfilled slots at phase boundary are blocking errors detectable without reading subsequent role files |
