## trace-migration Rubric v18 — Round 20 Scoring

---

### Scoring Approach

Each variation is evaluated against all 53 criteria. For brevity, criteria where all five variations score identically are grouped; per-variation breakdowns focus on differentiating criteria.

---

### Essential Criteria — All Variations

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | Before/After State | PASS | PASS | PASS | PASS | PASS |
| C-02 | Data Loss Path | PASS | PASS | PASS | PASS | PASS |
| C-03 | Constraint Violation Analysis | PASS | PASS | PASS | PASS | PASS |
| C-04 | Missing Default Detection | PASS | PASS | PASS | PASS | PASS |
| C-05 | Chronological Step Ordering | PASS | PASS | PASS | PASS | PASS |

All five: **60/60 essential pts**.

---

### Aspirational Criteria — Shared PASS Block (C-06 through C-32, excl. C-33)

All five variations pass the following on identical evidence:

| Criteria | Shared Evidence |
|----------|----------------|
| C-06–C-20 (structure/gate basics) | All variations carry complete two-phase architecture with parse phase, Q1/Q2/Q3 roles, EXIT BLOCK/ENTRY REFERENCE, PROTOCOL COUNT MANIFEST |
| C-21 | Binary gate at every phase transition — PARSE GATE (BINARY FIELD) present at Phase A-to-B |
| C-22–C-26 | Gating completeness, rollback path, per-entity analysis checklist |
| C-27 | Three-part inertia-contrast example present in all variations |
| C-28 | Per-constraint-type dedicated fields: NOT NULL, FK, UNIQUE, CHECK in separate slots across all Q sections |
| C-29 | Cross-role checklist coverage: Q2/Q3 explicitly mandated to apply same checklist as Q1 |
| C-30 | Distinct Phase A and B inertia examples: all explicitly require distinctness |
| C-31 | CONSTRAINT TYPE REGISTRY present in parse phase before Phase A in all |
| C-32 | B3 canonical table includes all four constraint types |

All five: **PASS** on C-06 through C-32 (excluding C-33).

---

### C-33 — Pre-Role Enforcement Block

**Pass condition**: A named enforcement block BEFORE the first role section, listing all required items with explicit scoping-prohibition language ("DO NOT SCOPE OR SHORTEN," "apply to ALL roles," "do not limit to financial columns").

| Variation | Rating | Evidence |
|-----------|--------|----------|
| V-01 | **FAIL** | Analytical checklist is inside Q1's body, not in a pre-positioned named block before Q1. Q2/Q3 instruction is inline: "Apply the same analytical checklist…" — no prohibition language, no dedicated named block. |
| V-02 | **FAIL** | No pre-Q1 enforcement block. Per-role tables appear within each role section; no scoping-prohibition language preceding the first role. |
| V-03 | **FAIL** | DIRECTIVE A-0 and B-1a/B-2 cover frame placement and ENTRY REFERENCE, but no named pre-role enforcement block with scoping-prohibition language before Q1. |
| V-04 | **PARTIAL** | "PHASE ARCHITECTURE AND COVERAGE FLOORS" appears before all role sections and lists "All four constraint-type analysis fields in each role section" as a floor requirement — closest to C-33. Missing explicit prohibition formulation ("DO NOT SCOPE OR SHORTEN") prevents full PASS. |
| V-05 | **FAIL** | Q1 contains its own checklist internally; Q2/Q3 are abbreviated. No pre-Q1 named enforcement block. |

---

### C-34 through C-50 — All Variations

| ID | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|----|------|------|------|------|------|-------|
| C-34 | PASS | PASS | PASS | PASS | PASS | EXIT BLOCK at Phase A close + ENTRY REFERENCE at Phase B open — both present in all |
| C-35 | PASS | PASS | PASS | PASS | PASS | BOUNDARY PROTOCOL as named section header: "BOUNDARY PROTOCOL: PHASE A TO PHASE B" in all |
| C-36 | PASS | PASS | PASS | PASS | PASS | Named STATUS QUO COST FRAME section before Q1 in all |
| C-37 | PASS | PASS | PASS | PASS | PASS | PROTOCOL COUNT MANIFEST table before B1 in all |
| C-38 | PASS | PASS | PASS | PASS | PASS | COST LEDGER table with 3 named rows (a)/(b)/(c) in all |
| C-39 | PASS | PASS | PASS | PASS | PASS | B2 has shared substrate + Commerce consequence + Finance consequence + causal link in all |
| C-40 | PASS | PASS | PASS | PASS | PASS | Q1 = OPERATIONS / INFRASTRUCTURE ROLE runs first in all |
| C-41 | PASS | PASS | PASS | PASS | PASS | Row (a): "Infrastructure or schema condition only — not a business process outcome" in all |
| C-42 | PASS | PASS | PASS | PASS | PASS | ALIGNMENT STATE binding statement present in all: names three artifacts to same condition class |
| C-43 | PASS | PASS | PASS | PASS | PASS | COST LEDGER SUBSTRATE GATE present in all: wrong-category row (a) = stop, return, re-identify |
| C-44 | PASS | PASS | PASS | PASS | PASS | ALIGNMENT STATE as listed condition in Phase A-to-B EXIT BLOCK in all |
| C-45 | PASS | PASS | PASS | PASS | PASS | MANIFEST includes PARSE GATE (EXIT), PARSE GATE (ENTRY REF), ALIGNMENT STATE, COST LEDGER SUBSTRATE GATE in all |
| C-46 | PASS | PASS | PASS | PASS | PASS | "(BINARY FIELD)" annotation on PARSE GATE at ENTRY REFERENCE position in all |
| C-47 | PASS | PASS | PASS | PASS | PASS | Manifest completeness rule present in all: "A gate named in any… but absent from this manifest = incomplete registry" |
| C-48 | PASS | PASS | PASS | PASS | PASS | Inline rationale note at ENTRY REFERENCE position in all — naming self-documenting property |
| C-49 | PASS | PASS | PASS | PASS | PASS | Completeness rule accompanied by action directive in all: "Apply this rule to detect omissions — do not rely on cross-document search" |
| C-50 | PASS | PASS | PASS | PASS | PASS | Completeness rule names three block types: "BOUNDARY PROTOCOL block, EXIT BLOCK, or ENTRY REFERENCE position" in all |

---

### C-51 — STATUS QUO COST FRAME Pre-Parse Positioning

| Variation | Rating | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | STATUS QUO COST FRAME section with "OPEN" header is first structural section; PARSE PHASE — CONSTRAINT TYPE REGISTRY follows it; PHASE A / Q1 follow the registry. Structural annotation: "*The STATUS QUO COST FRAME is open. Enumerate constraint types within that frame.*" placed inside PARSE PHASE confirms the registry operates within the opened frame. |
| V-02 | **PASS** | Explicit section-ordering rule at section header: "*Section order requirement: this section precedes the PARSE PHASE section. The inertia-cost commitment established here is the architectural premise for constraint enumeration and all subsequent analysis.*" Section ordering makes C-51 a format compliance requirement. |
| V-03 | **PASS** | DIRECTIVE A-0: "*WRITE the STATUS QUO COST FRAME section as the first section of this output, before the PARSE PHASE and before any constraint enumeration… A STATUS QUO COST FRAME that first appears after constraint type enumeration has begun violates this directive.*" Violation condition named explicitly — the direction is a DIRECTIVE infraction, not an aspirational miss. |
| V-04 | **PASS** | Coverage floor declares STATUS QUO COST FRAME floor requires terms "architectural premise" or "before the parse phase"; floor check is stated before Phase A begins. Section header: "*Architectural premise: the STATUS QUO COST FRAME is established here, before the parse phase and before any constraint enumeration.*" Vocabulary-based audit trail. |
| V-05 | **PASS** | Sub-heading "*Structural position: before the parse phase, before constraint enumeration, before any analytical content*" makes position explicit at three levels of specificity. Body: "*This section is the architectural premise for the entire trace… Everything that follows operates within this frame.*" Most comprehensive placement statement. |

---

### C-52 — B2 as Explicit STATUS QUO COST FRAME Closure

| Variation | Rating | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | B2 carries dual closure statements: (1) "*This section closes the STATUS QUO COST FRAME opened before the parse phase.*" in the B2 header area; (2) "*STATUS QUO COST FRAME CLOSE: B2 demonstrates the accumulated cross-role cost that the STATUS QUO COST FRAME established before parsing. The inertia-cost frame opened before constraint enumeration began is now closed at this cross-role synthesis.*" at the section close. Named open/close pair. |
| V-02 | **PASS** | B2 table schema contains mandatory "FRAME CLOSURE STATEMENT" row pre-filled with "*This section closes the STATUS QUO COST FRAME established before the parse phase. B2 demonstrates the accumulated cross-role cost that the STATUS QUO COST FRAME was opened to establish. The inertia-cost frame is now closed.*" Below the table: "*The FRAME CLOSURE STATEMENT row is required. An absent or placeholder FRAME CLOSURE STATEMENT row means B2 is not explicitly positioned as the STATUS QUO COST FRAME close.*" |
| V-03 | **PASS** | DIRECTIVE B-2: "*WRITE the B2 section as the explicit close of the STATUS QUO COST FRAME established before the parse phase… A B2 section that provides a cross-role causal chain without an explicit STATUS QUO COST FRAME closure statement fails this directive.*" Directive violation condition named. |
| V-04 | **PASS** | B2 opens with "*STATUS QUO COST FRAME CLOSE: this section closes the STATUS QUO COST FRAME opened before the parse phase.*" Phase B coverage floor requires vocabulary "closes the STATUS QUO COST FRAME" as an auditable floor item, creating two enforcement layers. |
| V-05 | **PASS** | B2 table schema pre-fills STATUS QUO COST FRAME CLOSE row with full closure statement + self-referential enforcement: "*(Reproduce this statement or equivalent; a B2 section that provides a cross-role causal chain without an explicit STATUS QUO COST FRAME closure statement does not close the frame — the frame remains structurally open.)*" Below table: "*The STATUS QUO COST FRAME CLOSE row is required. A B2 table that omits or leaves blank the STATUS QUO COST FRAME CLOSE row means the STATUS QUO COST FRAME opened before the parse phase has no named close — the frame boundary pair is incomplete.*" Most structurally weighted implementation. |

---

### C-53 — ENTRY REFERENCE Structural Incompleteness Verdict

| Variation | Rating | Evidence |
|-----------|--------|----------|
| V-01 | **PASS** | Inline verdict at ENTRY REFERENCE position: "*An ENTRY REFERENCE block that carries the `(BINARY FIELD)` annotation but contains no inline rationale explaining the self-documenting property is structurally incomplete.*" Verdict present; no self-enforcement around the verdict itself. |
| V-02 | **PASS** | ENTRY REFERENCE STRUCTURAL COMPLETENESS TABLE has two required rows: Self-documenting rationale (fill field) and Structural completeness verdict (pre-filled): "*An ENTRY REFERENCE block that carries the `(BINARY FIELD)` annotation but contains no inline rationale explaining the self-documenting property is structurally incomplete.*" Enforcement: "*Both rows are required. An ENTRY REFERENCE table with a blank or placeholder Self-documenting rationale row fails the structural completeness check stated in the row immediately below it.*" |
| V-03 | **PASS** | DIRECTIVE B-1a verbatim: "*An ENTRY REFERENCE block that carries the annotation but contains no inline rationale is structurally incomplete.*" Then echoed inside the ENTRY REFERENCE body: "*Per DIRECTIVE B-1a: an ENTRY REFERENCE block that carries the `(BINARY FIELD)` annotation but contains no inline rationale explaining the self-documenting property is structurally incomplete.*" Dual-location presence. |
| V-04 | **PASS** | Inline verdict at ENTRY REFERENCE: "*An ENTRY REFERENCE block that carries the `(BINARY FIELD)` annotation but contains no inline rationale explaining the self-documenting property is structurally incomplete.*" Phase B coverage floor requires term "structurally incomplete" in inline rationale, making absence a vocabulary-level floor failure. |
| V-05 | **PASS** | ENTRY REFERENCE STRUCTURAL COMPLETENESS TABLE pre-fills Structural completeness verdict row with verbatim text. Table footer: "*The structural completeness verdict row is pre-filled and must be reproduced verbatim. An ENTRY REFERENCE table that carries the gate annotation rows but omits the structural completeness verdict row is itself structurally incomplete — the verdict is not optional content but a block-level completeness requirement.*" Two-level recursion: the verdict names absence as structural incompleteness, and the table schema names the verdict row's own absence as structural incompleteness — each level enforces the level below it. |

---

### Composite Scores

Scoring method: 12 pts × 5 essential + 5.3 pts × 48 aspirational = 315 pts max.

| Criterion range | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------------|------|------|------|------|------|
| C-01–C-05 (essential, 60 pts) | 60 | 60 | 60 | 60 | 60 |
| C-06–C-20 (carried structure, ~80 pts) | 80 | 80 | 80 | 80 | 80 |
| C-21–C-32 (gate + structure v8-v9, ~63 pts) | 63 | 63 | 63 | 63 | 63 |
| C-33 (pre-role enforcement, 5.3 pts) | 0 | 0 | 0 | 2.7 | 0 |
| C-34–C-50 (gate architecture v10-v17, ~90 pts) | 90 | 90 | 90 | 90 | 90 |
| C-51 (pre-parse positioning, 5.3 pts) | 5.3 | 5.3 | 5.3 | 5.3 | 5.3 |
| C-52 (B2 FRAME CLOSE, 5.3 pts) | 5.3 | 5.3 | 5.3 | 5.3 | 5.3 |
| C-53 (structural incompleteness verdict, 5.3 pts) | 5.3 | 5.3 | 5.3 | 5.3 | 5.3 |
| **Total** | **309** | **309** | **309** | **311** | **309** |
| **% of max** | 98.1% | 98.1% | 98.1% | 98.7% | 98.1% |

> **Note:** Scores reflect structural completeness of the *prompt design*. The tight spread (309–311) reflects that all five variations achieve high criterion coverage, with C-33 as the primary differentiator. Implementation-quality gradations within PASS (strength of C-51/C-52/C-53 enforcement) affect future rubric evolution (new criteria derived from excellence signals) but do not affect the current PASS/FAIL count.

---

### Ranking

| Rank | Variation | Score | C-33 | Primary strength |
|------|-----------|-------|------|-----------------|
| 1 | **V-04** | **311** | PARTIAL | Coverage floors pre-position enforcement before role sections |
| 2 | V-01 | 309 | FAIL | Dual closure statements at B2 create open/close pair most legibly in narrative prose |
| 2 | V-02 | 309 | FAIL | Table-format enforcement makes all three criteria mechanically auditable by row count |
| 2 | V-03 | 309 | FAIL | DIRECTIVE imperatives with explicit violation conditions create the most actionable rule set |
| 2 | V-05 | 309 | FAIL | Recursive self-referential enforcement at C-52/C-53 is strongest structural implementation |

---

### Excellence Signals — Top Variation (V-04) and High Runners (V-05/V-03)

**From V-04 (top score):**
- **Coverage floor as pre-role enforcement proxy**: Placing a PHASE ARCHITECTURE AND COVERAGE FLOORS section at the document top — before all phases — creates a pre-positioned enforcement mandate that partially satisfies C-33. The floor lists per-phase required items in a scan-level inventory that precedes all analytical content. This is the closest any variation has come to C-33 compliance without using explicit prohibition language.

**From V-05 (strongest C-52/C-53 implementation):**
- **Pre-filled verdict cell as table schema element**: The structural incompleteness verdict is embedded as a pre-filled required row in the ENTRY REFERENCE STRUCTURAL COMPLETENESS TABLE — not as an instruction to include the verdict, but as the verdict itself already present in the schema. A model cannot omit the verdict without visibly leaving a required row blank.
- **Self-referential frame-close row**: The B2 table's STATUS QUO COST FRAME CLOSE row is pre-filled with the closure statement AND the row itself declares that its absence leaves the frame structurally open. Enforcement is embedded in the row being enforced.
- **Two-level recursive completeness chain**: For C-53, the verdict cell names the incompleteness condition, and the table footer names the verdict row's own omission as structural incompleteness. Each level recursively enforces the level below: a model cannot satisfy the schema without reproducing both the rationale (level 1) and the verdict (level 2), and the schema names what happens if either is missing.

**From V-03 (strongest DIRECTIVE implementation):**
- **Violation-condition directives**: DIRECTIVE A-0, DIRECTIVE B-1a, and DIRECTIVE B-2 each pair the requirement with an explicit failure sentence ("A STATUS QUO COST FRAME that first appears after constraint type enumeration has begun violates this directive"). This is more enforcement-dense than an instruction: the model sees not just what to do but exactly what constitutes a violation.

---

### v19 Rubric Candidates (from R20 excellence signals)

| Proposed | Chain position | Tests |
|----------|----------------|-------|
| **C-54** | Pre-role enforcement block with scoping-prohibition language | V-04's PARTIAL on C-33 reveals that coverage floors are necessary but insufficient — a criterion testing explicit prohibition vocabulary ("DO NOT SCOPE," "apply to ALL roles") in the pre-role block would capture this gap |
| **C-55** | Recursive verdict-row self-enforcement | V-05's B2 and ENTRY REFERENCE STRUCTURAL COMPLETENESS TABLE pattern: a required table row that names its own absence as the same structural failure it documents. C-53 passes if the verdict is present; C-55 would pass only if the table schema declares the verdict row itself mandatory by name |

---

```json
{"top_score": 311, "all_essential_pass": true, "new_patterns": ["coverage floor as pre-role enforcement proxy — pre-positioned phase-architecture section partially satisfies C-33 by listing per-phase required items before all role sections", "pre-filled verdict cell as table schema element — verdict text is the cell content in a required row, not an instruction to write the verdict", "self-referential frame-close row — B2 table row pre-fills the closure statement and declares its own absence leaves the frame structurally open", "two-level recursive completeness chain — verdict cell names incompleteness condition and table footer names verdict-row omission as the same failure, each level enforcing the level below"]}
```
