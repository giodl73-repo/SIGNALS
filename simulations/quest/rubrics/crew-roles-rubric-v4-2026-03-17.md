**crew-roles rubric v4** written to `simulations/quest/rubrics/crew-roles-rubric-v4-2026-03-17.md`.

**4 new criteria added (C-17 through C-20):**

| ID | Name | Source Pattern | What it closes |
|----|------|----------------|----------------|
| C-17 | Pre-write scope audit | V-03/V-04/V-05 SCOPE AUDIT before authoring | C-14 corrects post-write; this prevents pre-write — stronger than correction |
| C-18 | Vocabulary check in verification gate | V-04 PARTIAL on C-11 — gate missing CHECK 4 | C-15 gate defined without vocabulary; V-01/V-05 both add it explicitly |
| C-19 | Inertia frame Q-slot template | V-05 fill-in frame with `[Q1]`/`[Q2]` slots | C-16 wires vocabulary to Q&A answers; this wires Phase 2 into the frame itself |
| C-20 | Q-domain-aligned vocabulary distribution | V-05 per-question vocab distribution by Q-number | C-16 allows same term in all three answers; this requires Q1/Q2/Q3 domain alignment |

**Formula updated:** `aspirational_pass / 12 * 10` (was `/8`). Each full pass = 0.833 pts. Maximum score still 100.
abulary must be added to that definition.

3. **Inertia frame as fill-in template with Q-slots** — V-05's inertia-advocate frame is a structural template: "Challenge every proposal with evidence that [Q1 current system] remains sufficient given [Q2 migration cost]." Q1 and Q2 Phase 2 answers fill named slots. C-12 gates the pre-characterization; this closes the gap between pre-characterization and delivery by wiring answers into the frame template itself.

4. **Q-domain-aligned vocabulary distribution** — C-16 requires each Q1/Q2/Q3 answer to reference at least one Phase 1 vocabulary term. V-05 goes further: Q1 answer references a Q1-domain term, Q2 answer references a Q2-domain term, Q3 answer references a Q3-domain term. Prevents concentration (all three answers reusing a single term) and cross-domain mismatch.

**Formula recheck:** Aspirational criteria C-09–C-16 = 8. Adding C-17/C-18/C-19/C-20 brings aspirational to 12. Denominator updates to 12; each full pass contributes 10/12 ≈ 0.833 points.

---

**crew-roles rubric — v4**

---

**Changes from v3:**

- Added **C-17 Pre-Write-Scope-Audit** (aspirational): Before any roles are written, the skill runs a SCOPE AUDIT that surveys the planned role set and assigns scope values in advance. Writing is blocked until ≥ 2 distinct scope values appear in the plan. Closes the gap between C-14's post-write correction and C-09's scope-gradient check — prevention before the problem is written is structurally stronger than revision after. V-03 (SCOPE AUDIT gate in Step 2), V-04 (Phase 3 pre-write + Phase 5 post-write dual enforcement), and V-05 (Phase 3 exit-gated audit) all demonstrate this pattern.

- Added **C-18 Vocabulary-Check-In-Gate** (aspirational): The verification gate (C-15) must include an explicit vocabulary coverage check: every `expertise.relevance` in the output references a Phase 1 vocabulary term. Without this, the gate blocks on orphan references, scope homogeneity, and registry table, but leaves vocabulary enforcement to inline instructions that drift under model compression. V-04's PARTIAL on C-11 traces directly to this gap — vocabulary instruction exists but is not gated. V-01 and V-05 both include CHECK 4 in the gate and PASS.

- Added **C-19 Inertia-Frame-Q-Slot-Template** (aspirational): The inertia-advocate's `orientation.frame` is a fill-in template with explicit Q1 and Q2 slots populated from Phase 2 answers (e.g., "Challenge every proposal with evidence that [Q1 current system] remains sufficient given [Q2 migration cost]"). Structural wiring of Phase 2 into the frame; not an instruction to reference. Distinct from C-16, which wires vocabulary to Q&A answers — this wires pre-characterization answers into the advocate's primary framing stance. V-05 demonstrates.

- Added **C-20 Q-Domain-Aligned-Vocabulary-Distribution** (aspirational): In the inertia pre-characterization, each Q1/Q2/Q3 answer references a vocabulary term whose domain aligns with that Q's dimension — Q1 answer uses a Q1-domain term (current system vocabulary), Q2 answer uses a Q2-domain term (migration cost vocabulary), Q3 answer uses a Q3-domain term (user habit vocabulary). Closes the gap in C-16: a skill can satisfy C-16 by using the same vocabulary term in all three answers or cross-domain terms; Q-domain alignment enforces per-dimension grounding. V-05 demonstrates (per-question vocabulary term distribution mapped by Q-number).

- **Formula updated**: `aspirational_pass / 12 * 10` (was `/8`). Twelve aspirational criteria now in denominator; each full pass contributes 0.833 points. Partial credit rule unchanged.

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

**Aspirational** — partial credit (0.5 per PARTIAL); denominator 12:

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
| C-17 | Pre-write scope audit | Before any roles are written, a SCOPE AUDIT surveys the planned role set and assigns scope values; writing is blocked until ≥ 2 distinct scope values appear in the plan — prevention, not correction; structural gate before authoring |
| C-18 | Vocabulary check in verification gate | The verification gate includes an explicit vocabulary coverage check confirming every `expertise.relevance` references a Phase 1 vocabulary term; the gate does not PASS without this check, regardless of orphan and scope checks passing |
| C-19 | Inertia frame Q-slot template | The inertia-advocate's `orientation.frame` is a fill-in template with explicit Q1 and Q2 slots populated from Phase 2 answers; the frame text contains named placeholders (e.g., `[Q1 current system]`, `[Q2 migration cost]`) that must be filled, not a soft instruction to reference them |
| C-20 | Q-domain-aligned vocabulary distribution | Each Q1/Q2/Q3 answer in the inertia pre-characterization references a vocabulary term whose domain aligns with that Q's dimension: Q1 answer uses a current-system vocabulary term, Q2 answer uses a migration-cost vocabulary term, Q3 answer uses a user-habit vocabulary term; same-term reuse across all three answers fails this criterion |

---

**Formula**

```
score = (essential_pass / 5 * 60)
      + (recommended_pass / 3 * 30)
      + (aspirational_pass / 12 * 10)
```

- PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0
- Essential: 5 criteria x 12 pts each = 60 pts max
- Recommended: 3 criteria x 10 pts each = 30 pts max
- Aspirational: 12 criteria x 0.833 pts each = 10 pts max
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
| C-07 | Placeholder `{role-name}` left unresolved | Template constraint names expected format; gate orphan check marks `[UNRESOLVED]` and blocks delivery |
| C-08 | All roles are technical architects | Explicit category list; PM + technical + inertia + domain required |
| C-09 | All roles assigned `team` scope | Scope-gradient check in verification gate; homogeneous set triggers forced revision |
| C-10 | Inertia framing is generic ("change is hard") | Pre-characterization block gates writing; current system must be named |
| C-11 | Domain specificity relies on instruction only — regresses under drift | Phase 1 extraction produces a vocabulary list; every expertise.relevance must cite a term from it |
| C-12 | Inertia-advocate written without naming system/costs/habits | 3-question pre-characterization block appears before inertia-advocate; verify questions constrained to reference at least 2 of 3 answers |
| C-13 | No self-verification of orphan references or scope homogeneity | Post-write registry table forces both checks at execution time |
| C-14 | Scope gradient exists in template but is not enforced — all roles collapse to same scope | Structural revision step: if homogeneous, name 1-2 roles to revise and revise before proceeding |
| C-15 | Orphan check, scope check, and table run as separate optional steps — any can be skipped | Single named verification gate bundles all three; gate outcome (PASS/FAIL) is stated explicitly; delivery blocked on FAIL |
| C-16 | C-11 and C-12 both present but never linked — vocabulary unused in inertia answers | Q1/Q2/Q3 template includes `(must reference a term from Phase 1 vocabulary)` constraint inline |
| C-17 | Scope is planned homogeneously then corrected post-write — C-14 correction required | Pre-write SCOPE AUDIT assigns scope values to planned roles before authoring; writing blocked until plan shows diversity |
| C-18 | Vocabulary instruction present but not gated — drops under compression | Vocabulary coverage check added as CHECK 4 (or equivalent) in the verification gate; gate does not complete without it |
| C-19 | Q1/Q2 referenced in frame by soft instruction — omitted under model drift | Frame is a named template with `[Q1 current system]` and `[Q2 migration cost]` slot syntax; unfilled slots are detectable errors |
| C-20 | All three Q answers reference the same vocabulary term; cross-domain terms used for convenience | Q-number-to-term-domain mapping enforced: Q1 answer must reference a current-system term, Q2 a migration-cost term, Q3 a user-habit term |
