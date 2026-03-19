## rhythm-behavior — Round 2 Scoring

### Criterion Evaluation Matrix

| Criterion | Weight | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|--------|------|------|------|------|------|
| **C-01** Sequence declaration | essential | PASS | PASS | PASS | PASS | PASS |
| **C-02** Single unified report | essential | PASS | PASS | PASS | PASS | PASS |
| **C-03** Blast radius ranking explicit | essential | PASS | PASS | PASS | PASS | PASS |
| **C-04** Spec-gap + contract violation | essential | PASS | PASS | PASS | PASS | PASS |
| **C-05** Per-finding sub-skill attribution | recommended | PASS | PASS | PASS | PASS | PASS |
| **C-06** Actionable next step | recommended | PASS | PASS | PASS | PASS | PASS |
| **C-07** Section completeness / null result | recommended | PASS | PASS | PASS | PASS | PASS |
| **C-08** Blast radius justification | aspirational | PASS | PARTIAL | FAIL | PASS | PASS |
| **C-09** Cross-sub-skill synthesis | aspirational | FAIL | FAIL | PASS | PASS | PASS |
| **C-10** Self-documenting ranking label | aspirational | PASS | PASS | PASS | PASS | PASS |
| **C-11** Active coverage confirmation | aspirational | PASS | PASS | PASS | PASS | PASS |
| **C-12** At-discovery attribution | aspirational | PASS | PASS | PASS | PASS | PASS |

### Composite Scores

| Variation | Aspirational | Composite | Golden? |
|-----------|-------------|-----------|---------|
| V-01 | 4/5 → 8 | **98** | YES |
| V-02 | ~3.5/5 → 7 | **~96** | YES |
| V-03 | 4/5 → 8 | **98** | YES |
| V-04 | 5/5 → 10 | **100** | YES |
| V-05 | 5/5 → 10 | **100** | YES |

### Key Findings

**C-08**: Column > annotation. V-01/V-04/V-05 all PASS via structural column. V-02 PARTIAL — inline annotation can be silently dropped; no empty-cell pressure. C-08 is a pure structural mechanism question.

**C-09**: SYNTHESIS step alone is sufficient. V-03 PASS without any C-08 context — confirming C-09 was purely an instruction gap in R1, not a rationale-dependency issue.

**C-09 decoupled from C-08**: V-03 proves the two failing criteria are structurally independent. V-04's combo targets both with minimal additions.

**Primary golden candidate**: V-04 — two minimal structural additions (Rationale column + SYNTHESIS), 100/100, no verbosity penalty. V-05 is identical score with stronger at-discovery enforcement; preferred only if rationale completeness is the active concern.

### Excellence signals

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["SYNTHESIS section inserted after all five sub-skill sections and before consolidation unlocks C-09 by giving the model an explicit named moment to compare findings across sub-skills -- without this step C-09 fails because consolidation cannot perform ranking and cross-skill synthesis simultaneously", "Blast Radius Rationale table column unlocks C-08 by making omission structurally visible as an empty cell -- column pressure is categorically more reliable than inline annotation because a model cannot complete a table row without filling the column", "CROSS-SKILL Sub-Skill label makes synthesis findings first-class table citizens structurally consistent with per-sub-skill findings and verifiable in the coverage summary and closing confirmation check"]}
```
Skill column in the findings table. Per-section instructions name the sub-skill to assign (e.g., "Sub-Skill = flow-lifecycle"). Attribution is structural (column), not prose-only.

**C-06 — all PASS.** All variations: "The first finding in the sorted list (highest blast radius) gets one concrete, specific next step that a developer can execute before writing the first line of implementation code. Name the exact spec section, boundary, or component to address -- not a generic directive." Inherited from R1 V-05.

**C-07 — all PASS.** All five sub-skill sections carry null-result instructions: "If you find nothing in a phase, say so briefly (e.g., 'INIT: no findings')" and "If you find no issues, say so explicitly." Identical to R1 V-05 baseline.

**C-08 — V-01 PASS, V-02 PARTIAL, V-03 FAIL, V-04 PASS, V-05 PASS.**

- **V-01 PASS**: `Blast Radius Rationale` column added to table. "Blast Radius Rationale is required for every row. Do not leave it blank." Per-section: "write one sentence in Blast Radius Rationale naming the affected scope." Closing confirmation: "Every finding has a Sub-Skill attribution, a Blast Radius, and a Blast Radius Rationale." Three-layer enforcement: column structure, per-section mandate, closing check. Empty cell is visible as omission.

- **V-02 PARTIAL**: Inline "Why [LEVEL]:" annotation mandated at point of blast radius assignment. Closing confirmation checks for it. However: no table column -- omission is invisible in dense prose output. Annotation can be silently skipped between findings in a long section. The structural column of V-01 is absent. A model that populates blast radius labels without annotations will still produce a syntactically complete table. Risk of partial omission is real. Scored PARTIAL (structural enforcement gap; higher variance than V-01).

- **V-03 FAIL**: No rationale column, no inline annotation, no "why" instruction anywhere. Blast radius assignment is bare label only. No mechanism unlocks C-08.

- **V-04 PASS**: Rationale column + "required for every row" + per-section instruction to populate + closing confirmation. SYNTHESIS section also requires Blast Radius Rationale for cross-skill findings: "Write a Blast Radius Rationale sentence naming the full affected scope across both sub-skills." C-08 enforced in all finding paths.

- **V-05 PASS**: Same as V-04 plus "Attribution rule" preamble: "Apply Sub-Skill, Finding Type, Blast Radius, and Blast Radius Rationale at the moment of discovery." Per-section: "immediately apply Sub-Skill, classify, assign Blast Radius, and write Blast Radius Rationale before moving to the next finding." Enhanced closing confirmation: "Every Blast Radius Rationale names a specific flow, contract, or permission boundary." Strongest C-08 enforcement of the five.

**C-09 — V-01 FAIL, V-02 FAIL, V-03 PASS, V-04 PASS, V-05 PASS.**

- **V-01 FAIL, V-02 FAIL**: No SYNTHESIS section. No instruction to look for patterns spanning multiple sub-skills. C-09 is not targeted.

- **V-03 PASS**: Dedicated SYNTHESIS section after all five sub-skill sections. Explicit instruction: "Look for patterns or compounding risks that only become visible when results from multiple sub-skills are read together." Requirements: name contributing sub-skills (at least two), describe relationship or compounding effect, assign blast radius, label "CROSS-SKILL: [sub-skill-A + sub-skill-B]", add to findings table with Sub-Skill = CROSS-SKILL. Null result path: "Synthesis: no cross-sub-skill patterns found." All C-09 pass conditions satisfied structurally.

- **V-04 PASS**: Same SYNTHESIS as V-03, plus SYNTHESIS findings also require Blast Radius Rationale, making cross-skill findings table-consistent with all other findings.

- **V-05 PASS**: Same SYNTHESIS as V-04. "Attribution rule" preamble applies at synthesis: "Sub-Skill = CROSS-SKILL, Finding Type, Blast Radius, and Blast Radius Rationale at point of synthesis."

**C-10 — all PASS.** All variations inherit the sort label from R1 V-05: "Label the sort: 'Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW'" in the Consolidated Findings section, adjacent to the sorted table.

**C-11 — all PASS.** All variations inherit the active coverage confirmation from R1 V-05: explicit "confirm" list after findings + "If either category is missing, go back and find at least one before closing the report." Active correction loop, not a static label. V-05 adds a fourth confirmation item: "Every Blast Radius Rationale names a specific flow, contract, or permission boundary."

**C-12 — all PASS.** All variations inherit pre-opened table + append-throughout instruction from R1 V-05. Table is opened before flow-lifecycle; rows are added at discovery. Table columns include Sub-Skill, Finding Type, and Blast Radius -- satisfying at-discovery attribution in all five sub-skill sections. V-05 reinforces with explicit "Attribution rule" preamble and per-section "immediately apply" mandate, but the base mechanism is sufficient for a PASS in all variations.

---

### Composite Scores

| Variation | Essential (4→60) | Recommended (3→30) | Aspirational (5→10) | Composite | Golden? |
|-----------|------------------|--------------------|---------------------|-----------|---------|
| V-01 | 4/4 → 60 | 3/3 → 30 | 4/5 → 8 | **98** | YES |
| V-02 | 4/4 → 60 | 3/3 → 30 | ~3.5/5 → 7* | **~96** | YES |
| V-03 | 4/4 → 60 | 3/3 → 30 | 4/5 → 8 | **98** | YES |
| V-04 | 4/4 → 60 | 3/3 → 30 | 5/5 → 10 | **100** | YES |
| V-05 | 4/4 → 60 | 3/3 → 30 | 5/5 → 10 | **100** | YES |

*V-02 C-08 PARTIAL: scored 0.5/1 aspirational -- structural enforcement gap vs column mechanism. Upper bound 98 (annotation reliably present); lower bound 96 (annotation silently omitted). Reported ~96 (conservative).

All five variations are golden. R2 closes C-08 and C-09 for V-01, V-03, V-04, V-05.

---

### Variation Ranking

1. **V-04** (100) — Minimal combo: Rationale column + SYNTHESIS. Two structural additions targeting the two R1 failing aspirationals. No verbosity over V-03. Best signal-to-noise ratio. Primary golden candidate for deployment.
2. **V-05** (100) — Same score as V-04. Higher structural rigor via "Attribution rule" preamble and per-section "immediately apply" mandate. Marginal improvement over V-04 for C-12 quality (not pass/fail). Preferred when rationale completeness is the active concern.
3. **V-01** (98) — C-08 column without SYNTHESIS. Strongest single-axis C-08 mechanism. Confirms structural column (not annotation) is the right mechanism for blast radius justification.
4. **V-03** (98) — C-09 SYNTHESIS without rationale column. Confirms SYNTHESIS step alone is sufficient for C-09. C-09 is a pure instruction gap -- not dependent on C-08 rationale context.
5. **V-02** (~96) — Inline annotation for C-08. Annotation is weaker than column: no structural empty-cell pressure, silent omission risk in dense output. Not recommended as production prompt.

---

### Open Question Resolutions

| Question | V | Resolution |
|----------|---|-----------|
| Does `Blast Radius Rationale` column reliably unlock C-08? | V-01, V-04, V-05 | YES -- column + "required for every row" + closing confirmation is three-layer enforcement. Empty cell is visible as omission. |
| Does inline "Why WIDE/MEDIUM/NARROW:" annotation unlock C-08? | V-02 | PARTIAL -- annotation passes rubric letter but structural pressure is weaker; silent omission risk in dense output. Column is preferred. |
| Does a standalone SYNTHESIS section unlock C-09? | V-03 | YES -- named step after all five sub-skills makes cross-sub-skill pattern search explicit. C-09 was a pure instruction gap in R1. |
| Does C-09 require C-08 rationale context to fire? | V-03 | NO -- V-03 passes C-09 without Blast Radius Rationale column. The two criteria are structurally independent. |
| Does reinforced C-12 wording in V-05 improve score over V-04? | V-05 vs V-04 | NO -- both score 100. C-12 already passes via inherited pre-opened table. Attribution rule improves rationale quality but does not change pass/fail. |
| Is V-04 sufficient as golden candidate for deployment? | V-04 | YES -- 100/100, two minimal additions, no noise. Preferred over V-05 unless rationale quality (not just presence) is the active deployment concern. |

---

### Excellence Signals from V-04 and V-05

1. **SYNTHESIS step decouples C-09 from consolidation.** Placing a named SYNTHESIS section after all five sub-skill sections gives the model a dedicated moment to compare findings across sub-skills before consolidation. Without this step, the consolidation section performs two jobs (rank + synthesize) and synthesis loses. The step makes cross-sub-skill pattern search an explicit task with a named output (CROSS-SKILL label), not an implicit expectation embedded in the consolidation instruction.

2. **Table column structurally enforces C-08; prose mandate does not.** The Blast Radius Rationale column makes omission visible as an empty cell. A model that leaves the cell blank fails in a way auditable by anyone reading the table. A "Why [LEVEL]:" prose annotation can be silently dropped and the table row still appears complete. Column pressure is categorically more reliable than annotation pressure for per-finding requirements.

3. **CROSS-SKILL Sub-Skill label makes synthesis findings first-class table citizens.** Using "Sub-Skill = CROSS-SKILL" in the findings table keeps cross-skill observations structurally consistent with per-sub-skill findings. The table is the authoritative record; findings outside the table are invisible to the coverage summary and closing confirmation. The CROSS-SKILL label means synthesis findings are ranked, attributed, and confirmed the same way as all other findings.

---

### Round 3 Design Targets

V-04 reaches 100/100 under the v2 rubric. All twelve criteria are saturated. Round 3 options:

- **Rubric v3**: Extract new aspirational criteria from V-04/V-05 output quality analysis. Candidates: rationale specificity (names boundary vs names component vs names component + caller), cross-skill pattern blast radius accuracy (CROSS-SKILL findings may inherit incorrect blast radius from contributing sub-skills), actionable next step quality beyond top finding.
- **Robustness test**: Run V-04 against adversarial inputs (underspecified topics, absent spec) to verify structural invariants hold outside nominal conditions.
- **Simplification test**: V-04 variant that omits SYNTHESIS from the C-01 declaration -- confirm C-01 still passes if SYNTHESIS appears between sub-skills and consolidation but is not named in the opening sequence.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["SYNTHESIS section inserted after all five sub-skill sections and before consolidation unlocks C-09 by giving the model an explicit named moment to compare findings across sub-skills -- without this step C-09 fails because consolidation cannot perform ranking and cross-skill synthesis simultaneously", "Blast Radius Rationale table column unlocks C-08 by making omission structurally visible as an empty cell -- column pressure is categorically more reliable than inline annotation because a model cannot complete a table row without filling the column", "CROSS-SKILL Sub-Skill label makes synthesis findings first-class table citizens structurally consistent with per-sub-skill findings and verifiable in the coverage summary and closing confirmation check"]}
```
