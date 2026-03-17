Scanning the R4 scorecard for patterns present in 2+ variations not already captured in C-01 through C-18.

**New patterns found:**

| Pattern | Variations | Evidence |
|---------|-----------|----------|
| Self-routing halt messages | V-03, V-05 | V-03 C-18 note: halt messages embed recovery commands directly (`→ To continue: /crew-check [artifact] --amend rerun:pm`); V-05 C-17: "IDs appear in halt messages with embedded recovery commands" — the halt output tells the user exactly what to run next without consulting documentation |
| Executable audit output | V-02, V-05 | V-02 C-18: adds `--amend halts:{id}` for focused single-gate lookup — audit becomes a command menu, not just a report; V-05 C-18: "each entry includes a ready-to-paste re-entry command (audit-as-AMEND-menu). Extends C-18 beyond introspection to execution: user holds an action list, not a diagnostic report" |

**Structural note:** C-19 and C-20 are coupled in the same way as C-17/C-18. C-19 (self-routing halt) operates at point-of-failure; C-20 (executable audit) operates at post-run review. A variation can earn C-19 without C-20 (V-03), and C-20 without C-19 (V-02). V-05 earns both. The four criteria C-17→C-18→C-19→C-20 form a progression: *name the halt → enumerate what fired → route from the failure message → make the audit actionable*.

**Scoring mechanics for v5:** Add 2 new criteria at 2 pts each. Aspirational tier grows from 20 to 24 pts; total max from 110 to 114. Golden threshold (all 5 essential PASS + composite >= 80) unchanged.

---

## crew-check — Quest Rubric v5

### Changelog

#### v4 → v5

Two new aspirational criteria added from R4 excellence signals:

| ID | Name | Source signal |
|----|------|---------------|
| C-19 | Self-routing halt messages | V-03 and V-05 both embed recovery commands directly inside halt messages. V-03 pioneered the pattern (`→ To continue: /crew-check [artifact] --amend rerun:pm`); V-05 combined it with the stable ID system so the embedded command references the named gate. Prior variations halt with a named ID (C-17) but leave the user to consult the AMEND block separately. C-19 collapses that gap: the failure output is also the remediation prompt. |
| C-20 | Executable audit output | V-02 and V-05 both make the audit block actionable rather than diagnostic. V-02 adds `--amend halts:{id}` for focused single-gate re-entry; V-05 frames each audit entry as a ready-to-paste command (audit-as-AMEND-menu). C-18 covers whether the audit sub-command exists and enumerates fired gates; C-20 covers whether each audit entry includes a runnable re-entry command. A variation can earn C-18 with a read-only report and miss C-20. |

Aspirational tier total: 20 pts (v4) → 24 pts (v5), 2 pts × 12 criteria. Golden threshold unchanged: all 5 essential PASS + composite >= 80.

#### v3 → v4

Two aspirational criteria added from R3 excellence signals:

| ID | Name | Source signal |
|----|------|---------------|
| C-17 | Named halt identifier system | V-02 and V-04 both assign stable names to halt conditions (G1, G4-lens, G4-{role}, G5-empty, etc.) that appear verbatim in error output. The naming pattern is load-bearing: it enables audit trails, targeted AMEND re-entry, and human-readable error messages. |
| C-18 | AMEND gate-audit sub-command | V-02 and V-04 both include `--amend halts` in the AMEND block, listing every gate identifier that fired in the most recent run. C-10 covers whether AMEND handles standard operations; C-18 covers whether AMEND exposes the halt audit trail. |

---

### Rubric v5 — Criteria Reference

| Tier | ID | Criterion | Pts |
|------|----|-----------|-----|
| Essential | C-01 | Role source traceability | 12 |
| Essential | C-02 | Review matrix structure | 12 |
| Essential | C-03 | Perspective fidelity | 12 |
| Essential | C-04 | Depth mode compliance | 12 |
| Essential | C-05 | Severity presence | 12 |
| Recommended | C-06 | Finding specificity | 10 |
| Recommended | C-07 | Recommendation actionability | 10 |
| Recommended | C-08 | Severity calibration consistency | 10 |
| Aspirational | C-09 | Cross-role synthesis | 2 |
| Aspirational | C-10 | AMEND responsiveness | 2 |
| Aspirational | C-11 | Lens-anchoring step | 2 |
| Aspirational | C-12 | Severity calibration contract | 2 |
| Aspirational | C-13 | Challenger-first sequencing | 2 |
| Aspirational | C-14 | Readiness-gate framing | 2 |
| Aspirational | C-15 | Severity-sorted matrix output | 2 |
| Aspirational | C-16 | Hard-halt execution gate | 2 |
| Aspirational | C-17 | Named halt identifier system | 2 |
| Aspirational | C-18 | AMEND gate-audit sub-command | 2 |
| Aspirational | C-19 | Self-routing halt messages | 2 |
| Aspirational | C-20 | Executable audit output | 2 |

**Total: 114 pts · Golden threshold: all 5 essential PASS + composite >= 80**

---

### Criterion Definitions

#### Essential tier

**C-01 · Role source traceability (12 pts)**
The reviewer pool is built exclusively from `.craft/roles/`. No roles are invented or inferred from context. The skill names the source explicitly and does not proceed if the directory is absent.

*PASS*: Pool construction step references `.craft/roles/` by path; no invented roles permitted.
*FAIL*: Any role sourced from memory, context, or inference; source path omitted.

---

**C-02 · Review matrix structure (12 pts)**
The output contains a review matrix with exactly four columns: Role, Finding, Severity, Recommendation. No column may be blank. Rows map one-to-one with selected reviewer roles.

*PASS*: Matrix present; all four columns populated for every row.
*FAIL*: Missing column; blank cell; findings listed outside matrix structure.

---

**C-03 · Perspective fidelity (12 pts)**
Each reviewer row reflects that role's lens, not a generic or averaged voice. The skill enforces a lens-anchor step before writing the finding — the role's orientation frame is quoted or stated before the finding is written.

*PASS*: Each row demonstrably anchored to its role's lens; no generic findings applicable to any role.
*FAIL*: Findings interchangeable across roles; lens-anchor step absent or decorative.

---

**C-04 · Depth mode compliance (12 pts)**
The skill accepts a depth parameter (e.g., `--depth brief|standard|deep`) and adjusts finding detail accordingly. The depth mode in effect is stated at output header.

*PASS*: Depth parameter accepted; output calibrated to depth; mode declared.
*FAIL*: Depth parameter ignored; uniform output regardless of depth; mode undeclared.

---

**C-05 · Severity presence (12 pts)**
Every finding in the matrix carries an explicit severity label. The severity vocabulary is defined before use and applied consistently.

*PASS*: Severity column populated for every row; vocabulary declared.
*FAIL*: Any row missing severity; severity vocabulary undefined or inconsistently applied.

---

#### Recommended tier

**C-06 · Finding specificity (10 pts)**
Findings cite specific evidence from the reviewed artifact — named sections, quoted text, or identified line-level issues. Generic observations not anchored to artifact content do not qualify.

*PASS*: Each finding references specific artifact content.
*FAIL*: Findings could apply to any artifact of the same type; no artifact-specific anchoring.

---

**C-07 · Recommendation actionability (10 pts)**
Each recommendation names a concrete next action the author can take. Vague directives ("improve clarity," "consider revising") do not qualify.

*PASS*: Each recommendation specifies what to do, not just that something needs doing.
*FAIL*: Any recommendation is a direction without an action.

---

**C-08 · Severity calibration consistency (10 pts)**
Severity labels are applied at a consistent threshold across roles and findings. A CRITICAL from the PM lens and a CRITICAL from the engineering lens represent the same level of blocking risk.

*PASS*: Severity threshold consistent across all rows; no label inflation or deflation by role.
*FAIL*: Same class of issue labeled differently across roles without explicit rationale.

---

#### Aspirational tier

**C-09 · Cross-role synthesis (2 pts)**
The output includes a synthesis section that identifies patterns appearing across multiple reviewer roles — shared concerns, converging recommendations, or aggregate readiness signal. The synthesis is additive beyond the matrix rows.

*PASS*: Explicit synthesis section; pattern identified across ≥2 roles; not a summary of individual rows.
*FAIL*: No synthesis section; synthesis is a restatement of matrix content.

---

**C-10 · AMEND responsiveness (2 pts)**
The skill defines an AMEND block specifying how to re-enter after a failed run or partial execution. The AMEND block names the supported sub-operations and their preconditions.

*PASS*: AMEND block present; sub-operations named; preconditions stated.
*FAIL*: No AMEND block; AMEND block present but sub-operations unnamed.

---

**C-11 · Lens-anchoring step (2 pts)**
The skill includes an explicit lens-anchor step as a named execution phase before findings are written. The step quotes or paraphrases the role's orientation frame from its `.craft/roles/` definition.

*PASS*: Lens-anchor named as a step; orientation frame quoted or paraphrased per role.
*FAIL*: Lens-anchoring implicit or absent as a named step.

---

**C-12 · Severity calibration contract (2 pts)**
The skill defines a severity calibration contract — a named phase where reviewers align on severity thresholds before scoring. The contract prevents label drift across roles.

*PASS*: Calibration contract defined as a named phase; thresholds specified.
*FAIL*: No calibration contract; thresholds assumed or undefined.

---

**C-13 · Challenger-first sequencing (2 pts)**
The matrix rows are ordered with the highest-severity challenger roles first, ensuring the most blocking findings appear at the top of the output before supportive or lower-severity roles.

*PASS*: Matrix rows ordered by severity, challenger roles first.
*FAIL*: Matrix rows in arbitrary order; challenger roles not surfaced first.

---

**C-14 · Readiness-gate framing (2 pts)**
The output concludes with an explicit readiness gate: a binary or tiered signal (PROCEED / HOLD / CONDITIONAL) with the conditions that must be resolved before the artifact advances.

*PASS*: Readiness gate present; signal is binary or tiered; unresolved conditions named.
*FAIL*: No readiness gate; gate present but conditions not named.

---

**C-15 · Severity-sorted matrix output (2 pts)**
Within the matrix, rows are sorted by severity descending so that CRITICAL findings appear before MAJOR, MAJOR before MINOR, and MINOR before INFO.

*PASS*: Rows sorted by severity descending within the matrix.
*FAIL*: Rows unsorted or sorted by role rather than severity.

---

**C-16 · Hard-halt execution gate (2 pts)**
The skill defines hard-halt conditions — named gates that abort execution entirely when triggered. Hard halts produce an explicit HALT signal with the gate that fired; the run does not produce partial output.

*PASS*: Hard-halt conditions named; HALT signal emitted on trigger; no partial output produced.
*FAIL*: No hard-halt conditions defined; skill degrades silently on triggering conditions; HALT signal absent.

---

**C-17 · Named halt identifier system (2 pts)**
Each halt condition carries a stable identifier (e.g., G1, G4-{role}, G5-empty) that appears verbatim in three independent locations: the gate definition, the HALT signal emitted at runtime, and the AMEND routing key. The identifier system is load-bearing: it enables audit trails, targeted re-entry, and human-readable error messages that remain parseable across runs.

*PASS*: Stable IDs defined; IDs appear verbatim in gate definitions, runtime HALT output, and AMEND routing keys.
*FAIL*: Halt conditions unnamed; IDs appear in only one location; IDs vary between definition and output.

---

**C-18 · AMEND gate-audit sub-command (2 pts)**
The AMEND block includes a `--amend halts` sub-command that, when invoked after a failed run, enumerates every gate identifier that fired — producing a structured list of Gate ID, gate name, message triggered, and resolution step. The audit sub-command is for post-run introspection without rerunning the skill.

*PASS*: `--amend halts` sub-command defined; output includes Gate ID, gate name, message, and resolution step for each fired gate.
*FAIL*: No `--amend halts` sub-command; AMEND block covers re-entry operations only; fired gates not enumerable without rerunning.

*Note: C-18 without C-17 is degenerate — an audit listing unnamed gate conditions has no stable referents. A variation may earn C-17 without C-18.*

---

**C-19 · Self-routing halt messages (2 pts)**
Halt messages embed the exact recovery command inline, so the user receives both the failure signal and the remediation prompt in the same output. The embedded command is ready to run without consulting the AMEND block or documentation. When combined with C-17, the embedded command references the stable gate ID.

*PASS*: Each HALT message includes a verbatim re-entry command; command is executable without modification or cross-reference.
*FAIL*: HALT messages name the condition (C-17) but require separate AMEND block consultation to determine next action; recovery commands absent from halt output.

*Note: C-19 operates at point-of-failure; C-18 operates at post-run review. The two criteria are independent: V-03 earns C-19 without C-18; V-02 earns C-18 without C-19.*

---

**C-20 · Executable audit output (2 pts)**
Each entry in the gate-audit output (`--amend halts`) includes a ready-to-paste re-entry command, making the audit block an action menu rather than a diagnostic report. The user can resolve failures by executing commands directly from the audit output without constructing commands manually.

*PASS*: Each audit entry includes a ready-to-paste re-entry command; audit block functions as an executable action list.
*FAIL*: Audit block is read-only diagnostic output; entries identify fired gates but do not include runnable commands; user must construct re-entry commands from AMEND documentation.

*Note: C-20 extends C-18 — a variation must earn C-18 to be eligible for C-20. C-19 and C-20 are independent: a variation can embed self-routing in halt messages (C-19) without making the audit block executable (C-20), and vice versa. V-05 earns both by combining the V-03 self-routing pattern with the V-02 executable-audit pattern.*
