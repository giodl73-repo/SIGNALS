# Quest Score — org-build R16 (Rubric v12)

---

## Per-Variation Scoring

### V-01 — Phase Sequencing: Ordering Lock as Primary Structure

**Essential (5/5)**

| ID | Result | Evidence |
|----|--------|----------|
| C-01 | PASS | Phase 3 Task Step 1: ASCII hierarchy min 2 levels required |
| C-02 | PASS | Phase 3 requires all five fields per role file |
| C-03 | PASS | Phase 2 Task Step 3: MUST include inertia-advocate role |
| C-04 | PASS | Phase 2 Task Step 1: T0-DEPTH-FLAG=standard → 20-30; deep → 50+ |
| C-05 | PASS | Phase 3: headcount table with Area, Headcount, Key Roles, Decides, Escalates |

**Recommended (3/3)**

| ID | Result | Evidence |
|----|--------|----------|
| C-06 | PASS | MUST create min 2 area subdirs under `.roles/` |
| C-07 | PASS | Operating Rhythm 3+ rows; governance charter with quorum as N of M |
| C-08 | PASS | FLAT-CASE-PRESSURE + CAN-OPERATE-FLAT/STRUCTURE-WARRANTED verdict block |

**Aspirational (25/28)**

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Row 1 = headcount threshold; Row 2 = different trigger category |
| C-10 | **FAIL** | `[element name] (cat-N) --` format mentioned in Task Step 4 as description only; no MUST in Constraints section. "Descriptive format guidance without imperative MUST fails." |
| C-11 | PASS | SCOPE-TEMPLATE[T1-PRESSURE] verbatim |
| C-12 | PASS | CATEGORY-DERIVATION table keyed to T1-VERDICT |
| C-13 | PASS | Task Step 3: "Only one verdict. Both is an error." |
| C-14 | PASS | T1-VERDICT declared at Phase 1 gate; Phase 2 IC consumes by name |
| C-15 | PASS | "FORBIDDEN: writing neither. Neither is an error." |
| C-16 | PASS | Phase 3 FORBIDDEN: Mitigation cells containing format guidance |
| C-17 | PASS | FORBIDDEN: paraphrasing or adapting template text |
| C-18 | PASS | CATEGORY-DERIVATION has Required + FORBIDDEN columns |
| C-19 | PASS | All constraint sections use MUST/FORBIDDEN; no advisory language |
| C-20 | PASS | Phases 0/1/2 declare typed gate outputs; Phases 1/2/3 declare Input Contracts naming upstream variables |
| C-21 | PASS | Every typed gate variable in Phase 2/3 ICs bound by MUST or FORBIDDEN |
| C-22 | **FAIL** | Partial skeleton (FLAT-CASE-PRESSURE block with `<T1-PRESSURE>` / `<T1-VERDICT>`) but no complete org-chart.md skeleton covering all gate variables |
| C-23 | PASS | Each phase boundary carries FORBIDDEN guard on proceeding before record block emitted |
| C-24 | PASS | `=== RECORD: PHASE-N ===` blocks after Phase 0, 1, 2 |
| C-25 | PASS | Bidirectional: outbound FORBIDDEN in Constraints + record block; inbound FORBIDDEN in consuming IC — all three boundaries |
| C-26 | PASS | PHASE-ORDERING-GUARD as first field unifies gate declaration, ordering anchor, materialization |
| C-27 | PASS | Phase 2 Task Step 1: explicit per-flag count floor conditional inside phase instruction |
| C-28 | PASS | `PHASE-ORDERING-GUARD:` is structurally first field in all three record blocks |
| C-29 | PASS | No "do not" / "never" / "avoid" in constraint contexts; all prohibitions use FORBIDDEN: |
| C-30 | PASS | Every phase has distinct **Task Steps** and **Constraints** sections |
| C-31 | **FAIL** | T2-ROLE-COUNT: [integer >= 20] and T2-AREA-COUNT: [integer >= 2] are range annotations, not closed enumerations. C-31 requires complete valid-value sets in bracket notation. |
| C-32 | PASS | **Input Contract** and **Constraints** are labeled separately in every consuming phase |
| C-33 | PASS | Each IC names all upstream variables with source phase and MUST/FORBIDDEN binding; self-sufficient for audit |
| C-34 | PASS | CATEGORY-DERIVATION: T1-VERDICT | Required Categories | FORBIDDEN Categories — three columns, both verdict rows populated |
| C-35 | PASS | SEQUENCE-LOCK on Phase 1; ROLE-ENUM Input Contract requires T1-VERDICT from Phase 1 record block |
| C-36 | PASS | PRE-PHASE CONSTANTS block precedes Phase 0; SCOPE-TEMPLATE and CATEGORY-DERIVATION defined once; phase instructions reference by name with FORBIDDEN: embedding inline |

**Composite V-01**: (5/5 × 60) + (3/3 × 30) + (25/28 × 10) = 60 + 30 + 8.9 = **98.9**

---

### V-02 — Output Format: Table-Dominant Instructions

**Essential (5/5)** — identical to V-01. PASS all.

**Recommended (3/3)** — identical to V-01. PASS all.

**Aspirational (25/28)**

| ID | Result | Evidence |
|----|--------|----------|
| C-10 | **FAIL** | Format requirement appears in Task Steps table (step 3: "Write FLAT-CASE-PRESSURE block") without dedicated MUST constraint for `[element name] (cat-N) --` syntax |
| C-22 | **FAIL** | No full artifact skeleton; Phase 3 produces a task-step table, not a template with named gate-variable slots |
| C-31 | **FAIL** | T2-ROLE-COUNT: [integer >= 20], T2-AREA-COUNT: [integer >= 2] — not closed enumerations |
| all others | PASS | Table-based IC, MUST/FORBIDDEN columns, PHASE-ORDERING-GUARD first in all record blocks — clean structure throughout |

**Composite V-02**: 60 + 30 + 8.9 = **98.9**

---

### V-03 — Lifecycle Emphasis: Maximum Gate Density with Sub-Step Checkpoints

**Essential (5/5)** — PASS all.

**Recommended (3/3)** — PASS all.

**Aspirational (25/28)**

| ID | Result | Evidence |
|----|--------|----------|
| C-10 | **FAIL** | Phase 3 Task Step 1: "`Why It Applies Here` opens with `[element name] (cat-N) --`" — descriptive in Task Steps; Constraints section has no MUST for citation format |
| C-22 | **FAIL** | Sub-step checkpoints (SCAN, SCORE, VERDICT) add checkpoints but no full skeleton with gate-variable placeholder slots |
| C-31 | **FAIL** | Same T2-ROLE-COUNT / T2-AREA-COUNT range annotation issue |
| C-30 | PASS | Phase-level Task Steps / Constraints segmentation is maintained; sub-step FORBIDDENs (proceeding guards) are completion conditions for each sub-step, not free-floating constraint prose |
| all others | PASS | Sub-step checkpoints strengthen C-35 by making T1-PRESSURE independently auditable before T1-VERDICT derivation |

**Composite V-03**: 60 + 30 + 8.9 = **98.9**

---

### V-04 — Phrasing Register: Terse Imperative

**Essential (5/5)** — PASS all.

**Recommended (3/3)** — PASS all.

**Aspirational (25/28)**

| ID | Result | Evidence |
|----|--------|----------|
| C-10 | **FAIL** | Phase 3 Task Step 1: `` `[element] (cat-N) --` citations `` mentioned inline in a task step; no MUST in Phase 3 Constraints for the citation format |
| C-22 | **FAIL** | No artifact skeleton |
| C-31 | **FAIL** | Same count-field range annotation issue |
| C-29 | PASS | Terse register produces the cleanest FORBIDDEN: saturation of any variation; "FORBIDDEN: enumerating any role in this phase" and register is uniform throughout |
| all others | PASS | Zero advisory language anywhere; every prohibition uses FORBIDDEN: |

**Composite V-04**: 60 + 30 + 8.9 = **98.9**

---

### V-05 — Combined: Inertia-First Framing + Unified Record Block as Narrative Backbone

**Essential (5/5)** — PASS all.

**Recommended (3/3)** — PASS all.

**Aspirational (27/28)**

| ID | Result | Evidence |
|----|--------|----------|
| C-09 | PASS | Skeleton shows Row 1 = headcount trigger, Row 2 = `{{DIFFERENT-TYPE}}` trigger; roadmap structure explicit |
| C-10 | **PASS** | Phase 3 Constraints: "MUST write Anti-Pattern Watch rows with `[element name] (cat-N) --` citation format." Explicit MUST — only variation to promote the format requirement from task step to constraint |
| C-11 | PASS | SCOPE-TEMPLATE[T1-PRESSURE] verbatim; reference by name from PRE-PHASE CONSTANTS |
| C-12 | PASS | CATEGORY-DERIVATION[T1-VERDICT] drives category derivation |
| C-13 | PASS | "FORBIDDEN: writing both. Both is an error." |
| C-14 | PASS | T1-VERDICT gate output consumed by ROLE-ENUM IC |
| C-15 | PASS | "FORBIDDEN: writing neither. Neither is an error." |
| C-16 | PASS | "MUST write Mitigation cells as specific remediation actions -- FORBIDDEN: format guidance." |
| C-17 | PASS | FORBIDDEN: paraphrasing or adapting SCOPE-TEMPLATE text |
| C-18 | PASS | CATEGORY-DERIVATION columns |
| C-19 | PASS | Uniform MUST/FORBIDDEN register throughout all phase instructions |
| C-20 | PASS | All gates typed; all consuming phases have named ICs |
| C-21 | PASS | All typed gate variable bindings in ICs use MUST or FORBIDDEN |
| C-22 | **PASS** | Complete org-chart.md skeleton: `{{T1-PRESSURE}}`, `{{T1-VERDICT}}`, `{{T2-CATEGORY-A}}`, `{{T2-CATEGORY-B}}`, `{{HEADCOUNT-TABLE-ROWS}}` etc. — all gate variables have corresponding artifact slots. Only variation to satisfy C-22. |
| C-23 | PASS | Per-boundary FORBIDDEN at each phase transition |
| C-24 | PASS | Named record blocks after Phase 0, 1, 2 |
| C-25 | PASS | Bidirectional FORBIDDENs at all three boundaries |
| C-26 | PASS | PHASE-ORDERING-GUARD as first field; record block is single construct for gate declaration + ordering anchor + materialization |
| C-27 | PASS | Phase 2 Task Step 1: explicit T0-DEPTH-FLAG → count floor conditional |
| C-28 | PASS | PHASE-ORDERING-GUARD is first field in all record blocks |
| C-29 | PASS | No imperative negation forms; all prohibitions use FORBIDDEN: |
| C-30 | PASS | **Task Steps** / **Constraints** structural boundary in every phase |
| C-31 | **FAIL** | T2-ROLE-COUNT: [integer >= 20], T2-AREA-COUNT: [integer >= 2] — range annotations, not closed enumerations. Shared issue across all variations. |
| C-32 | PASS | **Input Contract** distinct labeled section from **Constraints** in all consuming phases |
| C-33 | PASS | ICs name every upstream variable with source phase and MUST/FORBIDDEN binding; independently auditable |
| C-34 | PASS | CATEGORY-DERIVATION: Required + FORBIDDEN columns side-by-side |
| C-35 | PASS | "Before enumerating a single role, answer the central question: can this org operate flat?" Phase 1 = INERTIA-VERDICT; Phase 2 ROLE-ENUM IC requires T1-VERDICT from Phase 1 record block |
| C-36 | PASS | PRE-PHASE CONSTANTS framed as "the tools you will need to answer the central question"; FORBIDDEN: embedding definitions inside phase instructions |

**Composite V-05**: 60 + 30 + (27/28 × 10) = 60 + 30 + 9.6 = **99.6**

---

## Rankings

| Rank | Variation | Aspirational | Composite | Gap-closers |
|------|-----------|-------------|-----------|-------------|
| 1 | **V-05** | 27/28 | **99.6** | C-10 PASS, C-22 PASS |
| 2 | V-01 | 25/28 | 98.9 | C-35 + C-36 structural baseline |
| 2 | V-02 | 25/28 | 98.9 | Same |
| 2 | V-03 | 25/28 | 98.9 | Sub-step checkpoints (quality, not criterion-moving) |
| 2 | V-04 | 25/28 | 98.9 | Cleanest C-29 register |

---

## Excellence Signals from V-05

**Signal 1 — Format requirements promoted from Task Steps to MUST in Constraints (C-10)**
V-01–V-04 described the `[element name] (cat-N) --` citation format in Task Step prose ("each 'Why It Applies Here' cell opens with..."). V-05 moved it to an explicit `MUST` in the Constraints section: "MUST write Anti-Pattern Watch rows with `[element name] (cat-N) --` citation format." The principle generalizes: any format requirement that determines artifact correctness belongs in the Constraints section as a MUST, not embedded in task-step description. Task steps describe what to do; Constraints dictate how the output must be structured.

**Signal 2 — Complete artifact skeleton as gate-coverage proof (C-22)**
V-05 provides a full `org-chart.md` skeleton with every gate output appearing as a named slot: `{{T1-PRESSURE}}`, `{{T1-VERDICT}}`, `{{T2-CATEGORY-A}}`, `{{T2-CATEGORY-B}}`, etc. This does more than satisfy C-22 — the skeleton serves as a visual proof that every declared gate variable has exactly one destination slot in the final artifact. Any gate output declared in a record block but absent from the skeleton would be immediately visible as a dangling variable. The skeleton is simultaneously a format template (C-22), a coupling validator, and a completeness argument for the gate chain.

**Open gap — C-31 (shared across all variations)**
All five variations use `T2-ROLE-COUNT: [integer >= 20]` and `T2-AREA-COUNT: [integer >= 2]` as range annotations rather than closed enumerations. C-31 requires complete valid-value sets in bracket notation. For count fields, a finite closed set is structurally impossible; a rubric amendment recognizing range-constrained integer annotations as passing for cardinality fields would unblock C-31 for R17.

---

```json
{"top_score": 99.6, "all_essential_pass": true, "new_patterns": []}
```
