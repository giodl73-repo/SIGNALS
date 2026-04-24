Looking at the Round 2 scorecard, I need to identify recurring partial patterns and the structural mechanisms that resolved them in specific variants before writing v3.

**Patterns to extract:**

1. **Scope-gradient enforcement** — C-09 is PARTIAL in V-01, V-02, V-04 because scope diversity is instructed but not enforced. V-03's Step 4 "if all same, revise" is a structural fix.

2. **Verification-gate bundling** — V-03 passes C-07, C-09, and C-13 via a single Step 4 gate. When checks are scattered, each can be dropped independently under model drift. Bundling creates a forcing function.

3. **Vocabulary-linked inertia Q&A** — V-04's Phase 2 requires each Q1/Q2/Q3 answer to reference a Phase 1 vocabulary term. C-11 and C-12 can both pass independently without ever being wired together; V-04 closes that integration gap.

**Formula recheck first:** Verifying the tier breakdown from scorecard arithmetic — Essential: C-01–C-05, Recommended: C-06, C-07, C-08, Aspirational: C-09–C-13. Adding C-14/C-15/C-16 brings aspirational to 8, so denominator updates to 8.

---

**crew-roles rubric — v3**

---

**Changes from v2:**

- Added **C-14 Scope-Gradient-Enforcement** (aspirational): A structural verification step checks scope diversity after all roles are written. If all roles share the same scope value, the skill must identify and revise 1–2 roles before delivery. Closes the C-09 PARTIAL pattern in V-01, V-02, and V-04 — scope diversity was instructed but never enforced; instruction alone regresses under model drift.

- Added **C-15 Verification-Gate-Phase** (aspirational): All post-write structural checks — registry summary table, orphan-reference check, and scope-gradient check — must be bundled into a single named verification gate. The gate must explicitly block delivery until all checks pass. Closes the scatter pattern where C-07, C-09, and C-13 each pass or fail independently; V-03's Step 4 demonstrates that bundling creates a forcing function that individual instructions cannot.

- Added **C-16 Vocabulary-Linked-Inertia-Q&A** (aspirational): Each Q1/Q2/Q3 answer in the inertia pre-characterization must reference at least one term from the Phase 1 vocabulary. Closes the C-11/C-12 integration gap — both criteria can pass independently without structural linkage. V-04's Phase 2 demonstrates the pattern; a skill can have vocabulary extraction and inertia pre-characterization as separate phases that never cross-reference each other.

- **Formula updated**: `aspirational_pass / 8 * 10` (was `/5`). Eight aspirational criteria now in denominator; each full pass contributes 1.25 points. Partial credit rule unchanged.

---

**Criteria**

**Essential** — all 5 must PASS for full essential score:

| ID | Criterion | Description |
|----|-----------|-------------|
| C-01 | All 5 fields | Every role file contains all 5 required fields: `name`, `orientation`, `expertise`, `collaborates_with`, `scope` |
| C-02 | Inertia-advocate present | At least one role has `orientation.frame` explicitly challenging the status quo; verify questions reference why the current approach is insufficient |
| C-03 | Correct output path | Roles written to `.roles/{area}/` |
| C-04 | Domain specificity | `expertise.relevance` is anchored to the specific domain of the input; no generic engineering language |
| C-05 | Minimum 3 roles | Output contains at least 3 roles, including the inertia-advocate |

**Recommended** — partial credit (0.5 per PARTIAL):

| ID | Criterion | Description |
|----|-----------|-------------|
| C-06 | Lens actionability | `orientation.verify` fields are questions (`?`); `orientation.simplify` fields are imperatives; examples reinforce the constraint |
| C-07 | Collaborates_with resolves | Every `collaborates_with` value matches the name of another file in the registry; no placeholder text or unresolved references at delivery |
| C-08 | Perspective diversity | Roles span at least 3 distinct perspective categories (e.g., product, technical, inertia, domain-specialist); no category monopoly |

**Aspirational** — partial credit (0.5 per PARTIAL); denominator 8:

| ID | Criterion | Description |
|----|-----------|-------------|
| C-09 | Scope gradient | Roles span at least 2 distinct scope values (e.g., `team`, `cross-team`, `org`); no homogeneous scope set |
| C-10 | Inertia domain-grounded | The inertia-advocate's framing names the specific current system, migration cost, or user habit — not generic resistance language |
| C-11 | Vocabulary-forced-field | Phase 1 produces a named vocabulary list extracted from input; every `expertise.relevance` field must reference at least one vocabulary term |
| C-12 | Inertia pre-characterization | Before writing the inertia-advocate, the skill answers 3 explicit questions: (1) current system name, (2) migration costs, (3) user habits; verify questions must reference at least 2 of these 3 dimensions |
| C-13 | Registry summary table | A `Role \| Orientation \| Scope \| Collaborates With` table appears in output after all roles are written; forces orphan-reference and scope-homogeneity checks at execution time |
| C-14 | Scope-gradient-enforcement | A structural step after writing checks scope diversity; if all roles share the same scope value, the skill identifies and revises 1–2 roles before delivery — structural gate, not soft instruction |
| C-15 | Verification-gate-phase | All post-write structural checks (registry summary table, orphan-reference check, scope-gradient check) are bundled into a single named gate that explicitly blocks delivery until all pass; checks are not scattered across instructions |
| C-16 | Vocabulary-linked inertia Q&A | Each Q1/Q2/Q3 answer in the inertia pre-characterization references at least one term from the Phase 1 vocabulary; C-11 and C-12 are structurally wired, not independently satisfied |

---

**Formula**

```
score = (essential_pass / 5 * 60)
      + (recommended_pass / 3 * 30)
      + (aspirational_pass / 8 * 10)
```

- PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0
- Essential: 5 criteria × 12 pts each = 60 pts max
- Recommended: 3 criteria × 10 pts each = 30 pts max
- Aspirational: 8 criteria × 1.25 pts each = 10 pts max
- Maximum score: 100

---

**Failure Mode Table**

| Criterion | Common Failure Mode | Structural Fix |
|-----------|--------------------|-----------------|
| C-01 | Missing field under model compression | Template enforces all 5 fields as required slots |
| C-02 | Inertia-advocate written with generic resistance framing | orientation.frame must name the specific incumbent; verify must ask "why is [current approach] insufficient?" |
| C-03 | Files written to working directory or wrong path | Path stated at skill top; Phase 1 sets path variable |
| C-04 | `expertise.relevance` uses generic language ("engineering best practices") | Vocabulary extraction phase anchors every relevance field to a domain term |
| C-05 | Inertia-advocate omitted or fewer than 3 roles | Minimum explicitly stated; inertia-advocate listed as required member |
| C-06 | Verify statements are declarative; simplify is vague | Examples in constraint text; `?` and imperative form enforced |
| C-07 | Placeholder `{role-name}` left unresolved | Template constraint names expected format; Step 4 orphan check marks `[UNRESOLVED]` and blocks delivery |
| C-08 | All roles are technical architects | Explicit category list; PM + technical + inertia + domain required |
| C-09 | All roles assigned `team` scope | Scope-gradient check in verification gate; homogeneous set triggers forced revision |
| C-10 | Inertia framing is generic ("change is hard") | Pre-characterization block gates writing; current system must be named |
| C-11 | Domain specificity relies on instruction only — regresses under drift | Phase 1 extraction produces a vocabulary list; every expertise.relevance must cite a term from it |
| C-12 | Inertia-advocate written without naming system/costs/habits | 3-question pre-characterization block appears before inertia-advocate; verify questions constrained to reference at least 2 of 3 answers |
| C-13 | No self-verification of orphan references or scope homogeneity | Post-write registry table forces both checks at execution time |
| C-14 | Scope gradient exists in template but is not enforced — all roles collapse to same scope | Structural revision step: if homogeneous, name 1–2 roles to revise and revise before proceeding |
| C-15 | Orphan check, scope check, and table run as separate optional steps — any can be skipped | Single named verification gate bundles all three; gate outcome (PASS/FAIL) is stated explicitly; delivery blocked on FAIL |
| C-16 | C-11 and C-12 both present but never linked — vocabulary unused in inertia answers | Q1/Q2/Q3 template includes `(must reference a term from Phase 1 vocabulary)` constraint inline |
