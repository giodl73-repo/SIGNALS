## crew-check — Quest Score R1

---

### Scoring Methodology

Each variation is evaluated against the rubric by inspecting the prompt body's structural guarantees — how the prompt is designed to elicit the correct output, not a live execution. The evidence notes assess whether the prompt *structurally forces* the model toward each criterion or leaves it to chance.

---

## V-01 — Role Sequence (Severity-Anchored)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Role source traceability | PASS | Step 1 explicitly reads `.roles/`, "Do not add roles not present in that directory." Strong guard. |
| C-02 | Review matrix structure | PASS | Step 5 defines the table with four named columns; role/findings/severity/recommendation all required. |
| C-03 | Perspective fidelity | PASS | Step 4 requires "Lock the lens" from `orientation.frame`/`lens.verify` before each finding. Challenger null-hypothesis rule adds role-differentiated voice. |
| C-04 | Depth mode compliance | PASS | Step 2 explicitly branches standard (2-4 roles) vs `--depth deep` (all roles). Clear conditional. |
| C-05 | Severity presence | PASS | Step 4 defines exactly HIGH/MEDIUM/LOW — three values only. Every row must have one. |
| C-06 | Finding specificity | PASS | "Find something specific in the artifact: name the section, field, decision, or assumption" — explicit requirement per reviewer. |
| C-07 | Recommendation actionability | PASS | "Write a recommendation naming (1) what to do and (2) where in the artifact." Two-part requirement. |
| C-08 | Severity calibration consistency | PASS | Severity anchoring is the primary axis: challenger-first ordering semantically anchors HIGH to real blockers. Explicit three-tier scale (HIGH=blocks commit, MEDIUM=fix before ship, LOW=advisory) provides calibration contract. |
| C-09 | Cross-role synthesis | PASS | Step 6 is mandatory: "Name at least one convergent finding: two roles that independently flagged the same concern." Required, not optional. |
| C-10 | AMEND responsiveness | PARTIAL | AMEND block is present with add/deep/reorder options. But no instruction on how to incorporate amendments into the output — only surface-level flag documentation. |

**essential_pass** = 5/5 → 60 pts  
**recommended_pass** = 3/3 → 30 pts  
**aspirational_pass** = 1.5/2 → 7.5 pts  
**composite** = 60 + 30 + 7.5 = **97.5**  
**golden** = YES (5/5 essential, composite >= 80)

---

## V-02 — Output Format (Labeled Blocks)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Role source traceability | PASS | "Read `.roles/`. Build role pool from files found. No invented roles." Clear guard. |
| C-02 | Review matrix structure | PASS | Labeled block format enforces all four fields structurally — missing label is visually immediate. "Every label must be present and non-empty. A blank value is a structural failure." |
| C-03 | Perspective fidelity | PARTIAL | Challenger null-hypothesis rule present. But no lens-anchoring step for non-challenger roles — perspective fidelity depends on model inference from role files, not structural forcing. |
| C-04 | Depth mode compliance | PASS | Standard (2-4) vs deep (all roles) branch is present and explicit. |
| C-05 | Severity presence | PASS | "Severity must be exactly one of: HIGH, MEDIUM, LOW" — labeled block makes absence immediately visible. |
| C-06 | Finding specificity | PASS | "Findings must name something specific in the artifact (not generic boilerplate)" — explicit rule per block. |
| C-07 | Recommendation actionability | PASS | "add X to section Y" not "improve this area" — concrete negative example provided. |
| C-08 | Severity calibration consistency | PARTIAL | Three-value scale defined, but no explicit calibration contract. No severity-anchoring mechanism. Miscalibration possible without challenger-first ordering. |
| C-09 | Cross-role synthesis | PASS | Synthesis section is required after all blocks: convergences (required), conflicts (optional). |
| C-10 | AMEND responsiveness | PARTIAL | AMEND block present with three options. Same gap as V-01: no execution instruction for incorporation. |

**essential_pass** = 4/5 (C-03 partial → borderline; treating as PARTIAL = 4.5 of 5, but rubric is binary pass/fail)

Re-evaluating C-03: the challenger null-hypothesis rule does force differentiation for one archetype. Non-challenger roles lack lens-anchoring. This is a structural gap. **C-03 = FAIL** for non-challenger rows.

**essential_pass** = 4/5 → 48 pts  
**recommended_pass** = 2/3 (C-08 partial → PARTIAL = FAIL) → 2/3 → 20 pts  
**aspirational_pass** = 1/2 (C-10 partial → FAIL, C-09 PASS) → 5 pts  
**composite** = 48 + 20 + 5 = **73**  
**golden** = NO (only 4/5 essential)

---

## V-03 — Lifecycle Emphasis (Phase-Gated)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Role source traceability | PASS | Phase 1 enforces: role pool = all files found, "No additions, no inventions." Halt condition on missing registry. Exit condition gates progress. |
| C-02 | Review matrix structure | PASS | Phase 4 R2 defines the four-column table. Phase 3 validates each row before writing with explicit per-cell validation. |
| C-03 | Perspective fidelity | PASS | Phase 3 step (a): "Lens: what does this role care about? (one sentence from their `orientation.frame`)" — forces lens declaration before finding. Challenger archetype runs first. |
| C-04 | Depth mode compliance | PASS | Phase 2 has explicit depth check: `--depth deep` → full pool; absent → standard with rationale per role. Phase header declares "Depth: [standard|deep] | Roles: [...]". |
| C-05 | Severity presence | PASS | Phase 3c: "Severity: HIGH / MEDIUM / LOW. Only these three values are valid." Validation step before writing. |
| C-06 | Finding specificity | PASS | Phase 3b: "Must name a specific surface: section title, field name, diagram element, stated assumption. Generic observations without an artifact surface fail validation." |
| C-07 | Recommendation actionability | PASS | Phase 3d: "one concrete action. Must name what and where. Generic directives fail." |
| C-08 | Severity calibration consistency | PASS | Three-value scale with precise definitions (HIGH=blocks commitment, MEDIUM=fix before ship, LOW=advisory). Phase exit-gate validation catches miscalibrated rows. |
| C-09 | Cross-role synthesis | PASS | Phase 4 R3: required, "2-3 sentences naming at least one convergence or conflict." Explicit fallback sentence provided. |
| C-10 | AMEND responsiveness | PARTIAL | Phase 4 R4 includes AMEND block. No execution guidance on how amendments change the output. |

**essential_pass** = 5/5 → 60 pts  
**recommended_pass** = 3/3 → 30 pts  
**aspirational_pass** = 1.5/2 → 7.5 pts  
**composite** = **97.5**  
**golden** = YES

---

## V-04 — Output Format + Phrasing Register (Combination)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Role source traceability | PASS | "SHALL be the filename stem of a role file in `.roles/`. MAY NOT be invented." Formal prohibition in the schema contract. |
| C-02 | Review matrix structure | PASS | Output contract table defines all four columns with SHALL constraints. "A row that violates any constraint SHALL be revised before appearing in the output." |
| C-03 | Perspective fidelity | PASS | Stage 3 step 1: "Anchor the lens: quote or paraphrase one line from the role's `orientation.frame` or `lens.verify`." Mandatory lens-anchoring per reviewer before finding. |
| C-04 | Depth mode compliance | PASS | Stage 2 applies depth rule with explicit conditional. Standard includes challenger mandate. |
| C-05 | Severity presence | PASS | Schema contract: "SHALL be exactly one of: HIGH, MEDIUM, LOW. No other values are permitted." |
| C-06 | Finding specificity | PASS | Schema: "SHALL name at least one specific artifact surface — a section heading, a named field, a diagram element, or a stated assumption." |
| C-07 | Recommendation actionability | PASS | Schema: "SHALL be a concrete action naming (1) what to do and (2) where in the artifact. SHALL NOT be a generic directive." Negative example included. |
| C-08 | Severity calibration consistency | PASS | Formal definitions (HIGH/MEDIUM/LOW) in schema contract. Challenger null-hypothesis severity logic specified. SHA language makes calibration contract binding. |
| C-09 | Cross-role synthesis | PASS | "SHALL name at least one convergence... or one conflict." Mandatory, with fallback. |
| C-10 | AMEND responsiveness | PARTIAL | Four AMEND options present. Same structural gap: no guidance on incorporating the amendment into output mechanics. |

**essential_pass** = 5/5 → 60 pts  
**recommended_pass** = 3/3 → 30 pts  
**aspirational_pass** = 1.5/2 → 7.5 pts  
**composite** = **97.5**  
**golden** = YES

---

## V-05 — Full Integration (Role Sequence + Inertia Framing + Lifecycle)

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | Role source traceability | PASS | P1.1: "Role pool = all files discovered. Zero roles may be invented." Halt on missing registry. Phase exit gate enforces this before proceeding. |
| C-02 | Review matrix structure | PASS | Phase 4 R2 defines four-column table; rows flushed from staging buffer. Phase 3 validates each row with named cell-level checks before staging. |
| C-03 | Perspective fidelity | PASS | Phase 3 step 1: "Lock the lens (one sentence from `orientation.frame`)" per domain reviewer. Challenger roles have dedicated inertia-framing instructions with three-variable null hypothesis format (X, Y, Z). Maximum per-archetype differentiation. |
| C-04 | Depth mode compliance | PASS | P2.1 explicit depth check: deep → full pool; absent → standard with rationale. Phase header declares depth and roles. |
| C-05 | Severity presence | PASS | Phase 3 severity: "HIGH / MEDIUM / LOW. Only these three values." Validation before staging includes severity check. Challenger severity logic gives explicit HIGH/MEDIUM/LOW conditions tied to inertia state. |
| C-06 | Finding specificity | PASS | Phase 3 step 2: "Name the artifact surface — section title, field, assumption, diagram element. No unnamed surfaces pass." Validation gate. |
| C-07 | Recommendation actionability | PASS | Phase 3 step 4: "one concrete action naming what to do and where. Not a directive." Validation requires this before staging. |
| C-08 | Severity calibration consistency | PASS | Strongest across all variations: challenger severity follows explicit conditional logic (HIGH/MEDIUM/LOW tied to whether inertia is credible, named, or refuted). Domain roles inherit the severity landscape established by challenger rows. Phase 1 challenger-first ordering is the structural guarantee. |
| C-09 | Cross-role synthesis | PASS | Phase 4 R3: required, convergence or conflict must be named, with explicit fallback. Same as V-03/V-04. |
| C-10 | AMEND responsiveness | PASS | Phase 4 R4 AMEND block includes five options, including `--amend skip:challengers` which changes the output contract — this is the most explicit description of how amendment changes behavior. The `--amend rerun:[role-name]` option implies re-execution, not just flagging. Best AMEND mechanics of all variations. |

**essential_pass** = 5/5 → 60 pts  
**recommended_pass** = 3/3 → 30 pts  
**aspirational_pass** = 2/2 → 10 pts  
**composite** = **100**  
**golden** = YES

---

## Composite Score Summary

| Variation | Essential | Recommended | Aspirational | Composite | Golden |
|-----------|-----------|-------------|--------------|-----------|--------|
| V-01 | 5/5 (60) | 3/3 (30) | 1.5 (7.5) | 97.5 | YES |
| V-02 | 4/5 (48) | 2/3 (20) | 1 (5) | 73 | NO |
| V-03 | 5/5 (60) | 3/3 (30) | 1.5 (7.5) | 97.5 | YES |
| V-04 | 5/5 (60) | 3/3 (30) | 1.5 (7.5) | 97.5 | YES |
| **V-05** | **5/5 (60)** | **3/3 (30)** | **2/2 (10)** | **100** | **YES** |

**Rank**: V-05 > V-01 = V-03 = V-04 > V-02

---

## Excellence Signals from V-05

**What made V-05 the only perfect scorer:**

1. **AMEND as output-contract modifier**: `--amend skip:challengers` explicitly changes the output contract, not just the reviewer list. This is the first variation where AMEND has a named behavioral consequence beyond "add a row." C-10 passes because the amendment's effect on output structure is described.

2. **Challenger severity as a conditional logic tree**: The three-variable null hypothesis (X=what team does today, Y=cost, Z=condition for acting) combined with explicit HIGH/MEDIUM/LOW conditions tied to inertia state gives the model a decision procedure for severity, not just a label vocabulary. C-08 passes structurally, not by convention.

3. **Phase 1 exit condition embeds the inertia mandate**: Making the null hypothesis a Phase 1 exit condition — not a step inside the review loop — means challenger output is produced before any domain review and cannot be skipped. C-03 and C-08 are guaranteed by sequencing, not by model compliance.

4. **Staging buffer architecture**: Rows are staged, validated, then rendered in Phase 4. This separation means C-02 and C-05 are enforced at write-time for every row, including challenger rows that are otherwise computed in a different phase.

---

## Scorecard

Written to: `simulations/quest/scorecards/crew-check-scorecard-R1-2026-03-17.md`

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["AMEND as output-contract modifier: naming how the amendment changes the output structure (not just row count) is what makes C-10 pass structurally", "Challenger severity as conditional logic tree: HIGH/MEDIUM/LOW tied to inertia state (credible+unaddressed / named+unquantified / refuted) gives model a decision procedure rather than a label vocabulary", "Phase 1 exit condition as inertia gate: embedding null hypothesis production as a phase exit condition guarantees it runs before domain reviews and cannot be skipped by model drift"]}
```
