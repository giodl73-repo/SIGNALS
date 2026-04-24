Now I have all the data needed. Let me score all five variations.

---

# roles-create R6 — Scorecard

**Rubric version:** v5 | **Scoring:** `Essential (5 @ 12pt each) + Recommended (2 @ 15pt each) + Aspirational (12 @ 0.833pt each)`

---

## Per-Criterion Evaluation

### Essential Criteria (C-01 to C-05) — all variations

All five R6 variations are designed on the R5 V-05 baseline, which was confirmed to pass all essential and recommended criteria. The R6 axis of variation is confined to C-17/C-18/C-19 only. No essential criterion changes across variations.

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-01 Role file at correct path | PASS | PASS | PASS | PASS | PASS |
| C-02 All 12 frontmatter fields | PASS | PASS | PASS | PASS | PASS |
| C-03 Mode detection routes correctly | PASS | PASS | PASS | PASS | PASS |
| C-04 Frontmatter content is domain-specific | PASS | PASS | PASS | PASS | PASS |
| C-05 Inertia-advocate surfaced when absent | PASS | PASS | PASS | PASS | PASS |

All essential criteria: 5/5 across all variations.

---

### Recommended Criteria (C-06, C-07)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-06 lens.verify items are sharp and actionable | PASS | PASS | PASS | PASS | PASS |
| C-07 Body includes domain specializations table | PASS | PASS | PASS | PASS | PASS |

All recommended criteria: 2/2 across all variations.

---

### Aspirational Criteria (C-08 to C-19)

#### C-08 through C-17 — unchanged from R5 V-05 baseline

All five R6 variations carry forward the R5 V-05 structure. C-08 through C-16 are structurally identical across all five. The only axis of variation in C-17 is V-04 (no CONTRACT blocks):

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-08 Archetype calibrated to area tier | PASS | PASS | PASS | PASS | PASS |
| C-09 Orientation register matches audience | PASS | PASS | PASS | PASS | PASS |
| C-10 Body table uses domain-named headers | PASS | PASS | PASS | PASS | PASS |
| C-11 Inertia-advocate companion generated | PASS | PASS | PASS | PASS | PASS |
| C-12 Interactive mode holds for all inputs | PASS | PASS | PASS | PASS | PASS |
| C-13 Pre-write self-certification executed | PASS | PASS | PASS | PASS | PASS |
| C-14 Malformed inputs routed pre-detection | PASS | PASS | PASS | PASS | PASS |
| C-15 Audit checks distributed as in-phase gates | PASS | PASS | PASS | PASS | PASS |
| C-16 Audit obligations pre-declared | PASS | PASS | PASS | PASS | PASS |
| C-17 Hard constraints in named CONTRACT sections | PASS | PASS | PASS | **FAIL** | PASS |

**C-17 evidence for V-04:** No CONTRACT: blocks anywhere. The "SKILL ENTRY" section uses inline prose with "verified at Gate X" annotations. Rules are embedded within each phase step rather than extracted to named CONTRACT: blocks. C-17 criterion requires "Key invariants (field register rules, audit checklist, column header rules) are extracted into explicitly named CONTRACT: blocks." V-04 fails; all others pass.

---

#### C-18: Declaration-to-gate traceability is bidirectional

Pass condition: "Gated At" column in declaration (forward) AND [letter] citation suffixes on gates (backward). Both ends required.

| Variation | "Gated At" column | [letter] gate suffixes | Verdict |
|-----------|------------------|----------------------|---------|
| V-01 | YES (AUDIT-CHECKLIST, lines 175-184) | YES (Gate 0 [G], Gate 3a [B], Gate 3b [C], Gate 3d [E], Gate 4b [F]) | **PASS** |
| V-02 | YES (AUDIT-CHECKLIST, lines 431-440) | NO (Gate 0, Gate 3a, Gate 4b — no [letter] suffix on any gate) | **FAIL** |
| V-03 | NO (AUDIT-CHECKLIST has ID+Criterion only, no "Gated At" column, lines 662-671) | YES (Gate 0 [G], Gate 2a [H], Gate 3a [B], Gate 4b [F]) | **FAIL** |
| V-04 | YES (SKILL ENTRY prose lists "verified at Phase 3 Gate 3a" etc.) | YES (Gate 0 [G], Gate 2a [H], Gate 3a [B], Gate 4b [F]) | **PASS** |
| V-05 | YES (AUDIT-CHECKLIST, lines 1124-1133) | YES (Gate 0 [G], Gate 2a [H], Gate 3a [B], Gate 3b [C], Gate 3d [E], Gate 4b [F]) | **PASS** |

**V-02 evidence:** The declaration names which gate executes each item (forward direction present), but in-phase gates use bare labels — `-> **Gate 3a:**`, `-> **Gate 4b:**` — with no bracketed letter suffix. The audit is traversable forward (declaration → gate) but not backward (gate → declaration). One-way forward only = C-18 fail.

**V-03 evidence:** The AUDIT-CHECKLIST table at lines 662-671 has only two columns: `ID | Criterion` — the "Gated At" column is structurally absent. Gates do cite [letter] suffixes (`Gate 0 [G]`, `Gate 3a [B]`, etc.), so the backward direction is present. One-way backward only = C-18 fail. Symmetric failure mode to V-02.

**V-04 note:** C-18 prerequisite set is C-15 + C-16. V-04 passes both (in-phase gates exist; SKILL ENTRY pre-declares the full checklist). C-17 is not in the prerequisite set for C-18. Full bidirectional annotation is structurally present despite no CONTRACT blocks. **C-18 = PASS** — confirms the prerequisite graph.

---

#### C-19: Content-producing phases are thin CONTRACT citations

Pass condition: every content-producing phase references a CONTRACT block by name and contains no restatement of rules within that block.

| Variation | Phase 3 structure | Phase 4 structure | Verdict |
|-----------|------------------|------------------|---------|
| V-01 | "Apply CONTRACT: FIELD-REGISTER." THEN "Field-by-field guidance (from CONTRACT: FIELD-REGISTER, **restated here for execution clarity**):" + full inline rules | "Apply CONTRACT: COLUMN-HEADER for table column headers." THEN full inline FAIL/PASS examples + rule prose | **FAIL** |
| V-02 | "Apply CONTRACT: FIELD-REGISTER." only, then gates. No inline rules. | "Apply CONTRACT: COLUMN-HEADER for table column headers. Minimum 3 rows." only, then gates. | **PASS** |
| V-03 | "Apply CONTRACT: FIELD-REGISTER." THEN full field-by-field inline guidance with GOOD/BAD examples | "Apply CONTRACT: COLUMN-HEADER for table column headers." THEN full inline FAIL/PASS examples + rule prose | **FAIL** |
| V-04 | N/A — no CONTRACT blocks to cite. Inline field rules embedded in Phase 3. | N/A — inline column header rules embedded in Phase 4. | **FAIL** (auto from C-17=F) |
| V-05 | "Apply CONTRACT: FIELD-REGISTER." only, then gates. No inline rules. | "Apply CONTRACT: COLUMN-HEADER for table column headers. Minimum 3 rows." only, then gates. | **PASS** |

**V-01 evidence (fat phases):** Phase 3 explicitly announces: "Field-by-field guidance (from CONTRACT: FIELD-REGISTER, restated here for execution clarity):" followed by archetype, orientation.frame, orientation.serves, lens.verify rules with GOOD/BAD examples — identical to the CONTRACT content. Phase 4 similarly restates all FAIL/PASS column header examples inline. C-19 requires the phase step to be a single-line citation with no restatement. V-01 fails despite full bidirectional traceability (C-18 = P, C-19 = F — the two criteria are independently additive).

**V-02 evidence (thin phases):** Phase 3 body: `Generate YAML frontmatter for .roles/{area}/{subrole}.md. All 12 fields required. Apply CONTRACT: FIELD-REGISTER.` — exactly one CONTRACT citation, no rule restatement. Phase 4 adds "Minimum 3 rows" which is a row-count spec absent from CONTRACT: COLUMN-HEADER (not a restatement of any CONTRACT rule). C-19 = P.

**V-04 auto-fail:** C-19 implies C-17. Since C-17 = F (no CONTRACT blocks exist to reference), C-19 = F by the prerequisite chain. Not a content judgment — structural impossibility.

---

### Full Aspirational Summary

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-08 | P | P | P | P | P |
| C-09 | P | P | P | P | P |
| C-10 | P | P | P | P | P |
| C-11 | P | P | P | P | P |
| C-12 | P | P | P | P | P |
| C-13 | P | P | P | P | P |
| C-14 | P | P | P | P | P |
| C-15 | P | P | P | P | P |
| C-16 | P | P | P | P | P |
| C-17 | P | P | P | **F** | P |
| C-18 | **P** | **F** | **F** | **P** | P |
| C-19 | **F** | **P** | **F** | F(auto) | P |
| **Passed** | **11/12** | **11/12** | **10/12** | **10/12** | **12/12** |

---

## Composite Scores

| Variation | Essential (max 60) | Recommended (max 30) | Aspirational (max 10) | Composite |
|-----------|-------------------|---------------------|----------------------|-----------|
| V-01 Bidirectional + Fat | 5/5 × 60 = **60** | 2/2 × 30 = **30** | 11/12 × 10 = **9.17** | **99.17** |
| V-02 Decl-to-Gate + Thin | 5/5 × 60 = **60** | 2/2 × 30 = **30** | 11/12 × 10 = **9.17** | **99.17** |
| V-03 Gate-Back + Fat | 5/5 × 60 = **60** | 2/2 × 30 = **30** | 10/12 × 10 = **8.33** | **98.33** |
| V-04 Bidirectional without CONTRACTs | 5/5 × 60 = **60** | 2/2 × 30 = **30** | 10/12 × 10 = **8.33** | **98.33** |
| V-05 Full Six-Criteria | 5/5 × 60 = **60** | 2/2 × 30 = **30** | 12/12 × 10 = **10** | **100** |

---

## Rankings

| Rank | Variation | Score | Delta from Ceiling |
|------|-----------|-------|--------------------|
| 1 | V-05 Full Six-Criteria | **100** | — |
| 2 | V-01 Bidirectional + Fat | **99.17** | −0.83 (C-19 fail) |
| 2 | V-02 Decl-to-Gate + Thin | **99.17** | −0.83 (C-18 fail) |
| 4 | V-03 Gate-Back + Fat | **98.33** | −1.67 (C-18 + C-19 fail) |
| 4 | V-04 Bidirectional without CONTRACTs | **98.33** | −1.67 (C-17 + C-19-auto fail) |

**Rubric separation check passed:** V-01 and V-02 tie at 99.17 — confirms C-18 and C-19 are equally weighted and independently additive. V-03 and V-04 tie at 98.33 — confirms the C-17/C-19-auto prerequisite chain costs exactly one criterion, same as independent C-18+C-19 failure in V-03.

---

## Excellence Signals from V-05

**Three patterns that make V-05 the sole ceiling:**

1. **Named CONTRACT blocks as single source of truth.** Every invariant lives in exactly one place — the CONTRACT: block. Phases execute by reference, never by restatement. Eliminates the drift risk where an inline restatement diverges from the canonical definition over iteration.

2. **Bidirectional audit annotation.** The AUDIT-CHECKLIST "Gated At" column maps each declared obligation to its execution gate (declaration → gate). Each gate's `[letter]` suffix maps back to the declaration item it validates (gate → declaration). The audit is fully traversable in both directions: from any checklist item, find the gate; from any gate, find the item. No dead ends.

3. **Thin-phase referencing.** Every content-producing phase is a single-line CONTRACT citation: `Apply CONTRACT: FIELD-REGISTER.` / `Apply CONTRACT: COLUMN-HEADER for table column headers. Minimum 3 rows.` Verbosity lives in the CONTRACT, not in the execution site. Each phase step is a pointer, not a copy.

**Key adversarial finding (V-01):** A skill can pass C-18 (full bidirectional traceability) and still fail C-19 (thin phases). The fat-phase restatement is a separate failure mode from annotation incompleteness. The two new criteria detect orthogonal defects in the audit architecture.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["bidirectional audit annotation — Gated At column maps declaration to gates; [letter] gate suffixes map gates back to declaration; audit traversable in both directions", "thin-phase referencing — every content-producing phase is a single-line CONTRACT citation with no rule restatement; verbosity lives in the CONTRACT not at the execution site", "C-18 and C-19 are independently additive — passing bidirectional annotation does not require thin phases and vice versa; each detects an orthogonal defect in audit architecture", "C-18 prerequisite set is C-15+C-16 only — bidirectional annotation is achievable with inline prose when in-phase gates and pre-declaration are both present; C-17 is not a prerequisite for C-18"]}
```
