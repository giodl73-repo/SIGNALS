Written to `simulations/quest/rubrics/trace-migration-rubric-v3-2026-03-15.md`.

---

**Rubric: trace-migration v3** — 15 criteria across 3 tiers:

**Essential (5, 60 pts)** — unchanged from v2

**Recommended (3, 30 pts)** — unchanged from v2

**Aspirational (7, 35 pts)** — three new criteria added:

- **C-13 Structural compliance enforcement** — Compliance obligations are embedded in the output *structure* so violations are visible as malformed or missing structural elements, not absent prose. A reader can verify compliance by column scan or field scan. Pass requires: at least one structural compliance mechanism (e.g., COMPLIANCE STATUS column, GAP INDICATOR column adjacent to registry entries). Prose-only enforcement does not pass.

  *Source: V-02 distinctive strength — "A TABLE 2 violation is a malformed cell, not missing prose — visible by column scan."*

- **C-14 Phase-gate closing conditions** — Every major section boundary has a named closing gate that must be explicitly cleared before the output advances. An output that advances past a gate without a clearing statement is structurally incomplete — the missing close condition is observable. Pass requires: at least two named closing gates at section boundaries, each with an explicit clearing condition.

  *Source: V-03 distinctive strength — "Skipping a gate is visible as a missing close condition, not missing prose."*

- **C-15 Cross-register coverage audit** — Coverage between per-entity analysis and the risk register is provable in both directions: forward (entity analysis -> register) and backward (register -> source section). An issue present in analysis but absent from the register triggers the halt protocol. Pass requires: source-section citation on every register entry; explicit coverage-audit statement; unidirectional registers do not pass.

  *Source: V-02 TABLE 9 source-table column + V-04 DIRECTIVE E — "An issue present in role analysis but absent from the register is a coverage gap."*

**Scoring changes:**
- Aspirational: 20 pts (4 criteria) → 35 pts (7 criteria), 5 pts each
- Total: 110 → 125
- Golden threshold: >= 85 → >= 95

The three new criteria share a single underlying insight surfaced across V-02, V-03, and V-04: **structural verifiability is an architectural property, not a review practice**. The format enforces the contract. That principle now has three named expressions in the rubric.
C-05 | **Constraint violation identification** — The output identifies nullable violations (adding NOT NULL to a column with existing NULLs), unique constraint violations (deduplication not handled), and check constraint failures that could cause the migration to fail or silently corrupt rows. | correctness | essential | Every new or tightened constraint is analyzed against the pre-migration data state. Missing constraint analysis does not pass. |

---

## Recommended Criteria (30 pts total — output is meaningfully better with these)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Default value gap analysis** — For every new NOT NULL column or column with a changed default, the output identifies whether a safe default exists, what value will be written to existing rows during backfill, and whether that value is semantically correct for the domain (Commerce / Finance / Operations context). | depth | recommended | Each new NOT NULL column has an explicit default-value analysis entry. Missing or assumed defaults are flagged. |
| C-07 | **Performance cliff identification** — The output identifies operations that could cause table scans, lock escalations, or index rebuilds on large tables: full-table UPDATE backfills, DROP INDEX / CREATE INDEX pairs, ALTER COLUMN type changes requiring rewrites, and foreign key constraint additions without concurrent index. | depth | recommended | At least one performance section exists. Each high-risk operation (backfill, reindex, lock) is annotated with a risk level (low / medium / high) and a recommended mitigation (batching, online DDL flag, maintenance window). |
| C-08 | **Reversibility and rollback assessment** — For each entity change, the output states whether the operation is reversible (e.g., ADD COLUMN is reversible by DROP COLUMN; column rename may require data copy; type narrowing may be irreversible if data was truncated). | behavior | recommended | Each entity entry includes a reversibility verdict (reversible / conditional / irreversible) with a brief rationale. |

---

## Aspirational Criteria (35 pts total — raises the bar)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Cross-entity dependency cascade** — The output traces second-order effects: foreign key cascades triggered by the migration, views or stored procedures invalidated by column changes, application-layer code assumptions broken by type or nullability changes, downstream ETL or reporting queries affected by renamed or dropped columns. | depth | aspirational | At least two cross-entity or cross-layer dependency paths are traced end-to-end with source -> impact -> mitigation. Single-entry cascade sections do not pass. |
| C-10 | **Quantified risk scoring** — Each identified issue (data loss path, constraint violation, performance cliff, irreversible operation) is assigned a structured risk entry with: severity (critical / high / medium / low), likelihood (certain / probable / possible), and a recommended remediation action before the migration runs. | format | aspirational | A risk register section exists with at least one entry per identified issue. Each entry has all three fields populated. |
| C-11 | **Admission-gate vocabulary enforcement** — The output defines an explicit approved-verb list for migration operations AND names at least three disallowed generic phrases (e.g., "changes," "modified," "updated"). Any entity entry using a disallowed phrase is flagged as non-compliant at admission — rejection is stated, not implied. The disallowed list makes compliance spot-checkable without re-reading the full output. | correctness | aspirational | An approved-verb list exists with at least five named DDL/DML verbs. A disallowed-phrase list exists with at least three named forbidden terms. At least one enforcement example is shown (e.g., "MODIFIED is not an approved verb — use ALTER TYPE or ALTER COLUMN"). |
| C-12 | **Halt-on-gap escalation protocol** — When any coverage gap is detected during entity enumeration, constraint analysis, or cascade tracing, the output includes a named halt protocol: gap identified -> named responsible role -> explicit acknowledgment required before analysis continues. The protocol prevents silent omission at the structural level; the analysis does not advance past an unresolved gap. | behavior | aspirational | At least one halt-protocol block is defined (even if no gaps are triggered in the current migration). The block names the gap condition, the responsible role, and the acknowledgment gate. An output that only flags gaps without halting does not pass. |
| C-13 | **Structural compliance enforcement** — Compliance obligations (vocabulary, gap detection, halt triggers) are embedded in the output structure itself so that a violation is visible as a malformed or missing structural element — not as missing prose. A reader can verify compliance by column scan or field scan without re-reading narrative sections. The structural embedding makes non-compliance self-evident at the formatting layer. | format | aspirational | At least one compliance mechanism is embedded structurally: e.g., a COMPLIANCE STATUS column in the operations table where a violation produces a flagged cell rather than an omitted sentence; a GAP INDICATOR column adjacent to entity registry entries where a gap-without-halt produces a visibly empty form field. Structural embedding must be explicit — prose-only enforcement does not pass. |
| C-14 | **Phase-gate closing conditions** — Every major analysis section or phase boundary has a named closing gate that must be explicitly cleared before the output advances. Closing gates name their clearing condition; an output that advances past a gate without clearing it is structurally incomplete — the missing close condition is visible without re-reading the preceding section. | behavior | aspirational | At least two named closing gates exist at section boundaries (e.g., VOCABULARY GATE, GAP HALT GATE, COVERAGE GATE). Each gate names its clearing condition explicitly. An output that defines phases but omits closing gates does not pass. An output that advances past a gate with a missing clearing statement does not pass. |
| C-15 | **Cross-register coverage audit** — Every issue identified in per-entity analysis (data loss, constraint violation, performance cliff, cascade effect) appears in the risk register, and every risk register entry traces back to its source analysis section. Coverage is provable in both directions: forward (entity analysis -> register) and backward (register -> source section). An issue present in entity analysis but absent from the register is treated as a coverage gap and triggers the halt protocol. | correctness | aspirational | The risk register includes a source-section or source-table citation for each entry. At least one explicit coverage-audit statement links the register to the per-entity analysis (e.g., "issues present in entity analysis but absent from this register constitute a coverage gap"). Unidirectional registers (issues listed but no source tracing) do not pass. |

---

## Scoring Summary

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01, C-02, C-03, C-04, C-05 | 60 |
| Recommended | C-06, C-07, C-08 | 30 |
| Aspirational | C-09, C-10, C-11, C-12, C-13, C-14, C-15 | 35 |
| **Total** | | **125** |

**Points per criterion:** Essential = 12 each | Recommended = 10 each | Aspirational = 5 each

**Golden**: all of C-01 through C-05 pass + composite >= 95.

---

## v3 Change Log

| Signal Source | Pattern Observed | New Criterion |
|---------------|-----------------|---------------|
| V-02 distinctive strength -- "A TABLE 2 violation is a malformed cell, not missing prose -- visible by column scan. TABLE 1-HALT adjacent to GAP-DETECTED makes gap-without-halt a visibly empty form cell." | Compliance enforcement embedded in data structure: violation = malformed structural element, not absent narrative. Verifiable by column/field scan without re-reading. | C-13 |
| V-03 distinctive strength -- "Every phase boundary has both a VOCABULARY GATE and a GAP HALT GATE -- skipping a gate is visible as a missing close condition, not missing prose. Phases cannot advance structurally without clearing both." | Phase closing conditions as first-class structural requirements: non-clearance is an observable structural omission, not a prose gap. | C-14 |
| V-02 TABLE 9 source-table column + V-04 DIRECTIVE E -- "An issue present in role analysis but absent from the register is a coverage gap -- issue DIRECTIVE 1 HALT BLOCK." | Bidirectional coverage audit: every issue traces to source section; every register entry cites its origin. Coverage provable in both directions; gap triggers halt protocol. | C-15 |
| V-02/V-03/V-04 general -- phase-structure and table-structure outputs consistently outperformed prose-structure outputs on spot-checkability and gap visibility | Underlying pattern behind C-13 and C-14: structural verifiability is an architectural property, not a review practice. The format enforces the contract. | Informs C-13 and C-14 |

**Inherited from v2 (unchanged):**
- C-11: Admission-gate vocabulary enforcement (approved-verb list + disallowed phrases)
- C-12: Halt-on-gap escalation protocol
- C-09 pass condition: single-entry cascade sections do not pass (explicit since v2)

**Scoring changes from v2:**
- Aspirational: 20 pts (4 criteria) -> 35 pts (7 criteria), 5 pts each
- Total: 110 -> 125
- Golden threshold: >= 85 -> >= 95
