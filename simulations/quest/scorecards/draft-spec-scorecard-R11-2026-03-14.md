Now I have all the data needed. Let me produce the full evaluation.

---

# /quest:score — `draft-spec` — Round 11 (Rubric v11)

## Source Files

- Variate: `simulations/quest/rubrics/draft-spec-rubric-v11-variate-R11-2026-03-15.md` (1,644 lines)
- Rubric: v11, 35 criteria (5 essential / 3 recommended / 27 aspirational), threshold 175

---

## Per-Variation Criterion Evaluation

### Essential Criteria (5) — All Variations

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|:----:|:----:|:----:|:----:|:----:|-------|
| C-01 guided section structure | PASS | PASS | PASS | PASS | PASS | All 5 phases present in all variations |
| C-02 scout status table | PASS | PASS | PASS | PASS | PASS | [SCOUT-STATUS-TABLE] with 7-row template in all |
| C-03 P0 coverage | PASS | PASS | PASS | PASS | PASS | [PM-CONTRACT-SEAL] present with P0 rows or C-03 WAIVER |
| C-04 self-review findings | PASS | PASS | PASS | PASS | PASS | Phase 4 findings table present in all |
| C-05 artifact frontmatter | PASS | PASS | PASS | PASS | PASS | `skill/topic/item/date/skill_version/input` in all |

**Essential: 5/5 PASS for all variations.** Golden threshold condition 1 met universally.

---

### Recommended Criteria (3) — All Variations

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|:----:|:----:|:----:|:----:|:----:|-------|
| C-06 secondary role validation | PASS | PASS | PASS | PASS | PASS | Validation rows present in guided sections |
| C-07 contradiction detection | PASS | PASS | PASS | PASS | PASS | Contradiction scan with R-ID pair instruction in Phase 1 |
| C-08 actionable amendment list | PASS | PASS | PASS | PASS | PASS | Phase 4/5 numbered amendment list minimum 2 items |

**Recommended: 3/3 PASS for all variations.** Golden threshold condition 2 met universally.

---

### Aspirational Criteria (27) — Variable Results

**Criteria passing in ALL 5 variations (13 stable aspirational):**

| Criterion | All | Notes |
|-----------|:---:|-------|
| C-09 no-scout fallback documented | PASS | Branch A / Branch B present |
| C-10 cross-namespace coherence | PASS | Cross-namespace signal field in Purpose table |
| C-11 pre-printed cross-namespace column | PASS | Row pre-printed in Purpose table template |
| C-13 per-row P0 status column | PASS | Status / ASSIGNED column in Requirements table |
| C-14 active inspection guard | PASS | Active "PM: inspect..." phrasing in scan instructions |
| C-16 PM-first coverage pre-assignment | PASS | [PM-COVERAGE-TABLE] structurally precedes inertia |
| C-17 named progression gate token | PASS | [PM-CONTRACT-SEAL], [INERTIA-ANALYZED], [SPEC-DRAFT-COMPLETE] |
| C-18 scripted verbatim fallback | PASS | `VERBATIM RESPONSE:` blocks with `HALT` instruction |
| C-21 gate token proof-of-work validity rule | PASS | `INVALID IF` conditions on each token |
| C-25 two-branch fallback with VERBATIM blocks | PASS | Branch A and Branch B each have VERBATIM blocks |
| C-28 PM pre-assignment structurally ordered | PASS | Phase 1 produces [PM-COVERAGE-TABLE] before Phase 2 |
| C-29 Elimination Paths reference pre-assigned R-IDs | PASS | "R-ID: [R-XX from [PM-COVERAGE-TABLE]]" in template |
| C-30 gate token validates column-level R-ID | PASS | [INERTIA-ANALYZED] Condition 2 checks R-ID per cell |

---

**Variable aspirational criteria — detailed per variation:**

#### C-12 — Role annotations inline
- **V-01**: FAIL — [PM-COVERAGE-TABLE] lacks Responsible Role column; no inline role annotations
- **V-02**: FAIL — same minimal base; no role annotations
- **V-03**: PASS — split registers; [IG-REGISTER] carries Responsible Role column per row (C-23 base includes role inline)
- **V-04**: FAIL — merged [INERTIA-TABLE] base; no role annotations
- **V-05**: PASS — [IG-REGISTER] with Responsible Role column; inline imperative phrasing identifies role at each instruction

#### C-15 — Cross-namespace signal at two locations
- **V-01**: FAIL — Phase 1 cross-namespace table has no `Location 1 of 2` marker; no cascade to Purpose
- **V-02**: FAIL — same
- **V-03**: PASS — `Location 1 of 2` in Phase 1 table, `Location 2 of 2` in Purpose section; CASCADE TO annotation present
- **V-04**: FAIL — no ordinal location markers; single occurrence only
- **V-05**: PASS — both locations marked, CASCADE TO annotation, completeness check on Purpose row

#### C-19 — Ordinal location markers
- **V-01**: FAIL — no `1 of 2 / 2 of 2` markers anywhere
- **V-02**: FAIL — same
- **V-03**: FAIL — **acknowledged gap**: combined base (R10 V-04) did not include location-count markers; V-05 adds them. *This is the one criterion V-03 does not satisfy.*
- **V-04**: FAIL — same
- **V-05**: PASS — `location 1 of 2 / location 2 of 2` appear on cross-namespace signal table AND Fallback Branch A/B headers

#### C-20 — Unified role-and-source declaration
- **V-01**: FAIL — no unified role declaration in Phase 1
- **V-02**: FAIL — same
- **V-03**: PASS — `**PM: scan scout-requirements -> assign...** CASCADE TO:` present as unified role+source declaration
- **V-04**: FAIL — Phase 1 lacks unified declaration
- **V-05**: PASS — `**PM: scan scout-requirements -> assign each P0 requirement... CASCADE TO:**` unified declaration with role, action, and cascade target in one block

#### C-22 — Split inertia registers [IG-REGISTER] / [ID-REGISTER]
- **V-01**: FAIL — single merged [INERTIA-TABLE]
- **V-02**: FAIL — single merged [INERTIA-TABLE]
- **V-03**: PASS — Phase 2 produces [IG-REGISTER] (hypothesis + elimination) and [ID-REGISTER] (risk + verdict) as separate named registers
- **V-04**: FAIL — single merged [INERTIA-TABLE]
- **V-05**: PASS — split registers with separate section headers

#### C-23 — Responsible Role column in [IG-REGISTER]
- **V-01/V-02/V-04**: FAIL — merged table has no Responsible Role column
- **V-03/V-05**: PASS — `| IG-ID | Responsible Role | Inertia Hypothesis | Elimination Path |` template in [IG-REGISTER]

#### C-24 — CASCADE TO annotations
- **V-01/V-02/V-04**: FAIL — no CASCADE TO annotations
- **V-03/V-05**: PASS — `CASCADE TO: [IG-REGISTER] Phase 2 (pre-assigned R-IDs) AND Purpose section cross-namespace signal row (location 2 of 2)` present in Phase 1

#### C-26 — Per-artifact Branch B sub-conditionals
- **V-01/V-02/V-04**: FAIL — single monolithic Branch B with one VERBATIM block
- **V-03/V-05**: PASS — Branch B subdivided: B-1 (feasibility only), B-2 (compliance only), B-3 (both), B-catch; each with distinct VERBATIM copy; anti-blend instruction present

#### C-27 — Imperative phrasing register
- **V-01/V-02/V-04**: FAIL — instructions use descriptive "If X" phrasing
- **V-03/V-05**: PASS — instructions use `**PM: scan ... -> assign ... -> fill ... -> emit ...**` imperative register throughout

#### C-31 — Waiver propagation structural rule
- **V-01**: FAIL — waiver handling is prose note; no structural propagation obligation declared in Phase 1
- **V-02**: FAIL — same; no structural rule (only the AMPLIFIED format note)
- **V-03**: PASS — `**Waiver propagation rule (structural)**: Requirements carrying C-03 WAIVER ... must generate "R-ID WAIVED" markers ... A behavioral note ... does not satisfy — the propagation is a named structural obligation declared here in Phase 1 and verified in [INERTIA-ANALYZED].`
- **V-04**: PASS — same structural rule present (C-31 base for V-04)
- **V-05**: PASS — full structural rule with named obligation and verification pointer

#### C-32 — AMPLIFIED dual sub-slot structural format
- **V-01**: FAIL — AMPLIFIED format instruction is prose ("must also name the specific risk dimension...") without pre-printed `Risk:` / `R-ID:` sub-slot labels
- **V-02**: PASS — pre-printed sub-slots present with labeled template:
  ```
  Risk: [feasibility constraint or compliance gap ...]
  R-ID: [R-XX from [PM-COVERAGE-TABLE] ...]
  ```
- **V-03**: PASS — same pre-printed sub-slot template in [IG-REGISTER]
- **V-04**: FAIL — AMPLIFIED instruction is prose without pre-printed sub-slots (C-32 isolated out to test C-34 alone)
- **V-05**: PASS — pre-printed sub-slots in [IG-REGISTER] with code block format

---

### New R11 Criteria — C-33, C-34, C-35

#### C-33 — PM-COVERAGE-TABLE Waiver Status column

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | **PASS** | Table definition includes `Waiver Status` column with `COVERED / C-03 WAIVER` enumeration; structural note: "This column is a named structural element of [PM-COVERAGE-TABLE]; a prose note ... does not substitute" |
| V-02 | FAIL | [PM-COVERAGE-TABLE] has only 5 columns (Req ID / Priority / Requirement Text / Assigned Section / Spec Entry Name); no Waiver Status column |
| V-03 | **PASS** | Full `| Req ID | Priority | Requirement Text | Responsible Role | Assigned Section | Spec Entry Name | Waiver Status |` template with enumeration note |
| V-04 | FAIL | [PM-COVERAGE-TABLE] has standard 5 columns; waiver handling via prose C-03 note only |
| V-05 | **PASS** | Waiver Status column present with `COVERED / C-03 WAIVER` enumeration; note about prose note non-substitution; [PM-CONTRACT-SEAL] invalidity rule updated to require Waiver Status column |

**Isolation confirmed**: V-01 passes C-33 and fails all other new criteria — clean isolation.

#### C-34 — Named chain closure declaration in [INERTIA-ANALYZED]

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | FAIL | [INERTIA-ANALYZED] has Condition 1 + Condition 2 + proof-of-work statement; no named chain closure declaration |
| V-02 | FAIL | Same; no chain declaration |
| V-03 | **PASS** | `**Chain closed**: [PM-COVERAGE-TABLE] C-03 WAIVER entry in Waiver Status column (Phase 1) → "R-ID WAIVED" cell marker in [IG-REGISTER] Elimination Path (propagated per Phase 1 structural rule) → Condition 2 exemption declared above. This declaration names all three nodes of the waiver traceability path in sequence.` — single co-located statement naming nodes 1→2→3 |
| V-04 | **PASS** | `**Chain closed**: [PM-COVERAGE-TABLE] waiver entry (C-03 WAIVER declared in Phase 1) → "R-ID WAIVED" cell marker in [INERTIA-TABLE] Elimination Path (propagated per Phase 1 structural rule) → Condition 2 exemption declared above.` — same three-node named declaration |
| V-05 | **PASS** | Full chain closure declaration co-located in [INERTIA-ANALYZED]; names Waiver Status column as upstream source (C-33 base) |

**Isolation confirmed**: V-04 passes C-34 (and C-31) but fails all other new criteria. Three-note-vs-one-statement test: V-04's single `**Chain closed**:` block names all three nodes in sequence — satisfies C-34.

#### C-35 — Pre-printed sub-slot partial-population structural fail rule

| Variation | Result | Evidence |
|-----------|--------|---------|
| V-01 | FAIL | No AMPLIFIED sub-slot format (C-32 absent); C-35 vacuously absent |
| V-02 | **PASS** | `**Partial-population structural fail rule**: Each sub-slot is structurally required. A cell with "Risk:" populated and "R-ID:" blank is a structural fail, not a content gap. A cell with "R-ID:" populated and "Risk:" blank is also a structural fail.` — named enforcement rule, co-located with AMPLIFIED sub-slot definition, names both fail directions explicitly |
| V-03 | **PASS** | Same named enforcement rule in [IG-REGISTER] AMPLIFIED format block |
| V-04 | FAIL | C-32 absent; no pre-printed sub-slots; C-35 vacuously absent |
| V-05 | **PASS** | Full rule in [IG-REGISTER]; [INERTIA-ANALYZED] certifies "all AMPLIFIED rows carry both sub-slots populated"; Phase 4 SELF-REVIEW scan list explicitly includes "partial-population structural fail rule co-located with AMPLIFIED sub-slot definition" |

**Isolation confirmed**: V-02 passes C-35 (and C-32) but fails all other new criteria.

---

## Composite Scores

Using the formula: `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/27 × 85)`

| Variation | Essential | Recommended | Aspirational | Composite | All Essential |
|-----------|:---------:|:-----------:|:------------:|:---------:|:-------------:|
| V-01 | 5/5 | 3/3 | 13/27 | **107/175** | YES |
| V-02 | 5/5 | 3/3 | 14/27 | **110/175** | YES |
| V-03 | 5/5 | 3/3 | 26/27* | **~172/175*** | YES |
| V-04 | 5/5 | 3/3 | 14/27 | **110/175** | YES |
| V-05 | 5/5 | 3/3 | 27/27 | **175/175** | YES |

**Note on V-03**: The variate scoring table states 175/175 for V-03, but the per-criterion table and the file's own note (line 1644) confirm C-19 (ordinal location markers) FAILS in V-03. V-03 achieves 26/27 aspirational, not 27. Corrected composite ≈ 172/175. This is an acknowledged design choice: V-03 targets the combined base without the C-19 location-count overhead. V-05 is the definitive 175/175.

---

## Rankings

| Rank | Variation | Score | Notes |
|------|-----------|-------|-------|
| 1 | **V-05** | 175/175 | All 35 criteria — clean top score, no gaps |
| 2 | **V-03** | ~172/175 | All new R11 criteria + C-31 base; C-19 gap acknowledged |
| 3 | **V-02** | 110/175 | C-35 + C-32 pass; C-33/C-34 absent by design |
| 3 | **V-04** | 110/175 | C-34 + C-31 pass; C-33/C-35 absent by design |
| 5 | **V-01** | 107/175 | C-33 pass only; isolated base |

---

## Excellence Signals — V-05 (Top Scorer)

What made V-05 score above all others:

**1. Tri-register coherence (C-33 + C-34 + C-35 composing with C-31/C-32)**
The three new criteria don't just add features — they close a traceability ring. C-33 creates a typed upstream source; C-31 propagates it structurally; C-34 names the closure explicitly; C-35 makes partial population a detectable structural error rather than a runtime content gap. V-05 is the only variation where all four link explicitly in [INERTIA-ANALYZED]'s proof-of-work statement.

**2. Self-review scan completeness**
V-05 Phase 4 explicitly lists six scan targets including "Waiver Status column in [PM-COVERAGE-TABLE]" and "partial-population structural fail rule co-located with AMPLIFIED sub-slot definition." Self-review detects what was added in this round — future-proof against new criteria.

**3. Ordinal location markers (C-19) closing the last gap over V-03**
V-05 adds `location 1 of 2 / location 2 of 2` markers on every multi-occurrence element. This makes omission immediately visible — the pre-printed row at location 2 of 2 is blank if the population was skipped at location 1 of 2.

**4. [SPEC-DRAFT-COMPLETE] expanded invalidity rule**
V-05's [SPEC-DRAFT-COMPLETE] certifies cross-namespace signal at both locations: `"cross-namespace signal present at both locations (Phase 1 table location 1 of 2 AND Purpose row location 2 of 2)"` — the gate token itself enforces C-15.

**5. C-35 verified at gate token level**
[INERTIA-ANALYZED] in V-05: `"Its presence certifies: ... all AMPLIFIED rows carry both sub-slots populated"` — C-35 enforcement surfaced into the gate token's validity contract, not just the format instruction.

---

## New Patterns

Scanning V-05 for patterns beyond the 35 v11 criteria:

**Candidate — Gate token expanding its certification scope to include new structural criteria**: [INERTIA-ANALYZED] and [SPEC-DRAFT-COMPLETE] in V-05 explicitly name C-33, C-35 compliance in their proof-of-work statements. The pattern: *each new aspirational criterion added in a round should update the downstream gate token's validity declaration to certify it*. This is visible in V-05 but not a named criterion — it's an implementation quality the variate achieves rather than a rubric-enforced rule.

However, this pattern is already partially captured by C-21 (gate token proof-of-work validity rule). The V-05 behavior is C-21 implemented correctly with up-to-date criterion coverage — not a new structural element requiring its own criterion.

**Conclusion**: No patterns emerge in R11 beyond C-33, C-34, C-35 (already incorporated into v11). The variate is structurally complete for this round.

---

## Summary

| Metric | Value |
|--------|-------|
| Top score | 175/175 (V-05) |
| All essential pass | YES — all 5 variations |
| Golden threshold met | V-05 only (clean); V-03 close (~172) |
| New R11 criteria isolated | C-33 in V-01, C-35 in V-02, C-34 in V-04 |
| V-03/C-19 discrepancy | Acknowledged in file; V-03 composite ~172 not 175 |
| New patterns for v12 | None |

---

```json
{"top_score": 175, "all_essential_pass": true, "new_patterns": []}
```
