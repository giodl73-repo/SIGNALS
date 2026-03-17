**Note:** Only V-01 was provided in the invocation — Phase 4 Task Steps/Constraints are absent, and V-02 through V-05 are missing. Scoring V-01 on available content; Phase 4 incompleteness is noted per criterion.

---

# Quest Score — org-build Round 20

**Rubric version:** 14 | **Variations evaluated:** V-01 only (V-02–V-05 not provided)

---

## V-01 — Lifecycle Emphasis

### Essential Criteria (weight: 60)

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | **PASS** | Preamble specifies "org-chart.md — ASCII hierarchy, headcount-by-area table…"; Phase 4 Input Contract establishes production context. |
| C-02 | **PASS** | Preamble explicitly lists all five fields: "orientation, lens, expertise, scope, collaborates_with for every enumerated role." Phase 3 IA-ANCHOR enforces scope field. |
| C-03 | **PASS** | Phase 3 Constraints: "MUST include inertia-advocate as a named role file under .craft/roles/." Unconditional. |
| C-04 | **PASS** | Phase 3 Sub-step COUNT: "T1-DEPTH-FLAG = standard → enumerate 20–30 roles; T1-DEPTH-FLAG = deep → enumerate 50+ roles." Flag-conditional floor in role enumeration phase instruction. |
| C-05 | **FAIL** | Preamble says "headcount-by-area table" — columns not specified. Decides/Escalates are required per rubric; Phase 4 Task Steps absent, no column enforcement. |

**Essential pass: 4/5**

---

### Recommended Criteria (weight: 30)

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | **PASS** | Phase 3 Constraints: "MUST create minimum 2 area subdirectories under .craft/roles/." Sub-step AREA-GROUPING: "Each area becomes a subdirectory." |
| C-07 | **FAIL** | Preamble lists "operating rhythm, committee charters" but Phase 4 Task Steps absent. No enforcement of 3+ distinct rhythm rows or Quorum field in charters. |
| C-08 | **PASS** | Phase 2 record block materializes `T2-IA-GATE: FLAT-CASE-PRESSURE: {{T2-PRESSURE}}. VERDICT: {{T2-VERDICT}}.` Constraints enforce exactly one of two closed-set values. Verdict guard is bidirectional. |

**Recommended pass: 2/3**

---

### Aspirational Criteria (weight: 10)

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | **FAIL** | Evolution roadmap in preamble; Phase 4 Task Steps absent. No typed trigger enforcement (headcount threshold vs. different category rows). |
| C-10 | **FAIL** | TABLE-B uses cat-N notation; Phase 4 absent. No MUST requiring `[element name] (cat-N) —` syntax in Anti-Pattern Watch cells. |
| C-11 | **PASS** | Phase 3 Input Contract consumes T2-PRESSURE from Phase 2. Sub-step IA-ANCHOR: "Look up T2-PRESSURE in TABLE-A." Scope template selection is verdict-gated by construction. |
| C-12 | **PASS** | TABLE-B header: "Category selection independent of this table fails C-12 and C-18." Explicit structural derivation, verdict-keyed. |
| C-13 | **PASS** | Phase 2 Sub-step VERDICT: "Only one verdict. Both is an error." Record block T2-IA-GATE repeats the framing. Explicit error form present. |
| C-14 | **PASS** | Three record blocks declare typed outputs. Phase 3 and Phase 4 Input Contracts name upstream variables by gate origin. At least one named typed pair (T2-VERDICT → Phase 3 Input Contract). |
| C-15 | **PASS** | Phase 2 Constraints: "FORBIDDEN: writing both… Both is an error." AND "FORBIDDEN: writing neither… Neither is an error." Both directions explicitly covered. |
| C-16 | **FAIL** | Phase 4 Task Steps absent. No enforcement of remediation-action content in Anti-Pattern Watch mitigation cells. |
| C-17 | **PASS** | Phase 3 Constraints: "MUST copy TABLE-A scope text verbatim. Paraphrase fails C-17." GLOBAL CONSTANTS: "FORBIDDEN: paraphrase, adaptation, or deviation of any kind." Verbatim requirement stated twice. |
| C-18 | **PASS** | TABLE-B populates both Required and FORBIDDEN columns per verdict row. CAN-OPERATE-FLAT → FORBIDDEN cat-1/cat-4; STRUCTURE-WARRANTED → FORBIDDEN cat-2/cat-3. |
| C-19 | **FAIL** | Phase 2 Sub-step PRESSURE: "Consider each pressure tier against the signals observed in sub-step SCAN." "Consider" is advisory language in an execution instruction. C-19 requires MUST/FORBIDDEN in all constraint-equivalent statements. |
| C-20 | **PASS** | All three intermediate phases emit record blocks with named typed variables. All consuming phases (2, 3, 4) declare Input Contracts naming source phase and valid-value set. Systematic coverage. |
| C-21 | **PASS** | Phase 3 Input Contract: MUST binding with closed-set for each of T1-DEPTH-FLAG, T2-PRESSURE, T2-VERDICT. Phase 4 Input Contract: same for all 7 consumed variables. No variable consumed without MUST. |
| C-22 | **FAIL** | T2-IA-GATE uses `{{T2-PRESSURE}}/{{T2-VERDICT}}` slots inside a record block field — not a pre-print artifact skeleton. No skeleton for org-chart.md or .craft/roles/ files with named {{}} slots. |
| C-23 | **PASS** | Each phase boundary: Constraints FORBIDDEN + PHASE-ORDERING-GUARD in record block + standalone Boundary Guard section. Every phase transition covered. |
| C-24 | **PASS** | `=== RECORD: PHASE-1 ===`, `=== RECORD: PHASE-2 ===`, `=== RECORD: PHASE-3 ===` all present. Phase 4 is terminal; no downstream gate required. |
| C-25 | **PASS** | Each boundary carries 4 guards: (1) Constraints FORBIDDEN outbound, (2) PHASE-ORDERING-GUARD in record block, (3) standalone "Boundary Guard — Phase N+1 Inbound" section, (4) Input Contract FORBIDDEN inbound. Surpasses bidirectionality requirement. |
| C-26 | **PASS** | PHASE-ORDERING-GUARD is first field inside record block. Gate schema (typed fields), ordering anchor, and materialization artifact are one construct. A reader seeing only the record block can derive all three. |
| C-27 | **PASS** | Phase 3 Sub-step COUNT contains per-value conditional: "T1-DEPTH-FLAG = standard → enumerate 20–30 roles; T1-DEPTH-FLAG = deep → enumerate 50+ roles." Binding is inside the role-enumeration phase instruction. |
| C-28 | **PASS** | All three record blocks: PHASE-ORDERING-GUARD is structurally the first field, carrying "FORBIDDEN: Phase N+1 begins before this block is emitted." Not in surrounding preamble. |
| C-29 | **PASS** | All prohibitions use FORBIDDEN: keyword. "Paraphrase fails C-17" in Phase 3 Constraints is a cross-reference to the GLOBAL CONSTANTS FORBIDDEN declaration, not a standalone prohibition. No "do not" / "never" / "avoid" found in constraint contexts. |
| C-30 | **PASS** | Each phase has `### Task Steps` and `### Constraints` as distinct labeled subsections. Structural boundary is explicit. |
| C-31 | **FAIL** | `PHASE-ORDERING-GUARD` field carries a FORBIDDEN directive, not a closed-set annotation. `T2-IA-GATE` carries template prose (`FLAT-CASE-PRESSURE: {{T2-PRESSURE}}…`) — descriptive, not a closed enumeration. Both fail C-31's self-documentation requirement. |
| C-32 | **PASS** | Phases 2, 3, 4 all have `### Input Contract` as a section distinct from `### Constraints`. Gate-consumption audit is independently readable. |
| C-33 | **PASS** | Input Contract sections name every consumed variable with source phase and MUST binding. Phase 4 Input Contract: 7 variables, all sourced, all MUST-bound. A reader scanning only Input Contract sections can reconstruct the full chain. |
| C-34 | **PASS** | TABLE-B: three columns — T2-VERDICT / Required Categories / FORBIDDEN Categories — side-by-side. Both verdict paths are simultaneously visible in one scan. |
| C-35 | **PASS** | Phase 2 (Inertia Assessment) precedes Phase 3 (Role Enumeration). Phase 3 Input Contract requires T2-VERDICT as a named typed gate output. Inertia is structurally locked before role count begins. |
| C-36 | **PASS** | `## GLOBAL CONSTANTS` section declared before Phase 1. TABLE-A and TABLE-B defined once. Phase 3 references "TABLE-A" and "TABLE-B" by name only; no inline table embedding. |
| C-37 | **PASS** | Phase 2 Constraints: 2 sub-step FORBIDDENs (SCAN→PRESSURE, PRESSURE→VERDICT), both naming blocked and prerequisite. Phase 3 Constraints: 3 sub-step FORBIDDENs (COUNT→AREA, AREA→IA-ANCHOR, IA-ANCHOR→CATEGORY-READ). |
| C-38 | **PASS** | `T3-ROLE-OUTCOME: [STANDARD-FLOOR-MET \| DEEP-FLOOR-MET \| FLOOR-MISS]` encodes mode × compliance in one composite token. No separate mode field + compliance field cross-reference needed. |
| C-39 | **PASS** | Task step bodies contain only task prose and declarative error-framing ("Both is an error. Neither is an error.") — no FORBIDDEN: keyword. All FORBIDDEN: directives reside in Constraints sections. Sub-step ordering guards in Phase 2/3 are in Constraints, not task step bodies. Structurally clean. |

**Aspirational pass: 25/31**
*(Failures: C-09, C-10, C-16, C-19, C-22, C-31)*

---

### Score Computation

```
composite = (4/5 × 60) + (2/3 × 30) + (25/31 × 10)
          = 48.0 + 20.0 + 8.1
          = 76.1 → 76
```

---

### Ranking

| Variation | Essential | Recommended | Aspirational | Score |
|-----------|-----------|-------------|--------------|-------|
| V-01 | 4/5 | 2/3 | 25/31 | **76** |
| V-02–V-05 | — | — | — | not provided |

---

### Excellence Signals (V-01)

**What made V-01 strong:**

1. **Quadruple phase-boundary guarding** — The "Lifecycle Emphasis" axis generates 4 independently stated ordering guards per boundary: Constraints FORBIDDEN (outbound), PHASE-ORDERING-GUARD inside record block, standalone "Boundary Guard" section, and Input Contract FORBIDDEN (inbound). Resilient to selective attention; any one guard alone would suffice, all four together make the boundary unopenable.

2. **C-39 satisfied via task/constraint register split** — Task step bodies use declarative error-framing prose ("Only one verdict. Both is an error. Neither is an error.") without FORBIDDEN: keyword. The same prohibition appears as FORBIDDEN: in Constraints. Result: descriptive reasoning in task steps helps the model reason; FORBIDDEN: in Constraints provides the machine-auditable constraint. The split is structurally clean and satisfies C-39.

3. **GLOBAL CONSTANTS as single source of truth** — TABLE-A and TABLE-B declared before Phase 1; all phases reference by name. No table content duplicated inline. Satisfies C-36 and also prevents drift between constant definition and phase use.

4. **Composite token design lands cleanly** — T3-ROLE-OUTCOME encodes mode × compliance in one field; no cross-referencing T1-DEPTH-FLAG + a separate compliance field. Record block is self-auditing.

**Remaining gaps:**

- C-05: Headcount table columns (Decides/Escalates) not specified — can be added to preamble or Phase 4 Task Steps.
- C-31: PHASE-ORDERING-GUARD and T2-IA-GATE fields need closed-set annotations to be self-documenting. PHASE-ORDERING-GUARD is a structural field with a fixed directive; its annotation could be `[FORBIDDEN: Phase N+1 begins before this block is emitted]` as a closed singleton.
- C-19: "Consider each pressure tier" in Phase 2 Sub-step PRESSURE — replace with "Evaluate each pressure tier" or add a MUST framing.
- C-22: Pre-print skeleton absent — a minimal `org-chart.md` skeleton with `{{T2-PRESSURE}}`, `{{T2-VERDICT}}` slots would unlock this.
- Phase 4 completeness: C-07, C-09, C-10, C-16 all depend on Phase 4 Task Steps that were not provided.

---

```json
{"top_score": 76, "all_essential_pass": false, "new_patterns": ["quadruple-boundary redundancy: four independently stated ordering guards per phase transition (Constraints FORBIDDEN, record block PHASE-ORDERING-GUARD, standalone Boundary Guard section, Input Contract FORBIDDEN) making phase boundaries resilient to selective attention", "task/constraint register split for C-39: task step bodies carry declarative error-framing prose (Both is an error) without FORBIDDEN: keyword while Constraints carry the same prohibition as FORBIDDEN: directives — descriptive reasoning in task steps, machine-auditable constraints in Constraints"]}
```
