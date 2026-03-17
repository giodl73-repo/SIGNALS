Scanning the R3 scorecard for patterns present in 2+ variations not already captured in C-01 through C-16.

**New patterns found:**

| Pattern | Variations | Evidence |
|---------|-----------|----------|
| Named halt identifier system | V-02, V-04 | V-02 C-16: named registry "G1, G4-lens, G4-severity, G4-location, G5-empty"; V-04 C-01/C-03/C-05/C-07: "HALT [G1]", "HALT [G4-{role}] lens", "HALT [G4-{role}] severity", "HALT [G4-{role}] location" — halt conditions carry stable identifiers that appear verbatim in error output |
| AMEND gate-audit sub-command | V-02, V-04 | V-02 C-10: "`--amend halts` (lists every gate that fired) — strongest C-10 in R3"; V-04 C-10: AMEND block enumerates "halts" as a named sub-command — post-run introspection of fired gates without rerunning the skill |

**Scoring mechanics for v4:** Add 2 new criteria at 2 pts each. Aspirational tier grows from 16 to 20 pts; total max from 106 to 110. Golden threshold (all 5 essential PASS + composite >= 80) unchanged.

Note: C-17 and C-18 are structurally coupled — named identifiers (C-17) are what make gate-audit enumeration (C-18) meaningful. A variation can pass C-17 without C-18 (names halt IDs but no audit sub-command), but C-18 without C-17 is degenerate (audit sub-command listing unnamed gates).

---

## crew-check — Quest Rubric v4

### Changelog: v3 → v4

Two new aspirational criteria added from R3 excellence signals:

| ID | Name | Source signal |
|----|------|---------------|
| C-17 | Named halt identifier system | V-02 and V-04 both assign stable names to halt conditions (G1, G4-lens, G4-{role}, G5-empty, etc.) that appear verbatim in error output. V-01 has hard halts but produces generic stop messages with no stable ID. The naming pattern is load-bearing: it enables audit trails, targeted AMEND re-entry, and human-readable error messages. Variations that halt but don't name the condition correctly score C-16 but miss C-17. |
| C-18 | AMEND gate-audit sub-command | V-02 and V-04 both include `--amend halts` in the AMEND block, listing every gate identifier that fired in the most recent run. V-02's commentary explicitly marks this as "strongest C-10 in R3." V-01 and V-03 have general AMEND operations but no post-run gate introspection. C-10 covers whether AMEND handles standard operations; C-18 covers whether AMEND exposes the halt audit trail. The two criteria are independent: a variation can score full C-10 without C-18. |

Aspirational tier total: 16 pts (v3) → 20 pts (v4), 2 pts × 10 criteria. Golden threshold unchanged: all 5 essential PASS + composite >= 80.

---

### Rubric v4 — Criteria Reference

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

**Total: 110 pts · Golden threshold: all 5 essential PASS + composite >= 80**

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

*PASS*: Lens-anchor step present; finding language differs meaningfully across roles.
*FAIL*: Reviewers produce interchangeable findings; lens-anchor absent or nominal.

---

**C-04 · Depth mode compliance (12 pts)**
The skill distinguishes standard mode (2–4 selected roles) from `--depth deep` (all roles in pool). The challenger archetype is included in both modes. Mode selection is explicit, not inferred.

*PASS*: Mode branch present; challenger always included regardless of mode; role count differs between modes.
*FAIL*: No mode distinction; challenger omitted in standard mode; role count identical across modes.

---

**C-05 · Severity presence (12 pts)**
Every row in the review matrix carries a severity label drawn from the locked three-value scale: HIGH, MEDIUM, LOW. No other values are permitted. The scale is established before any reviewer runs.

*PASS*: Severity column populated for every row; values from locked scale only; scale defined before reviewer step.
*FAIL*: Severity absent or blank for any row; unlocked scale; values outside HIGH/MEDIUM/LOW.

---

#### Recommended tier

**C-06 · Finding specificity (10 pts)**
Each finding names a specific artifact surface: a section heading, field name, stated assumption, or diagram element. Generic observations without a named surface are not acceptable.

*PASS*: Every finding references a named artifact surface.
*FAIL*: Any finding states a concern without naming the specific surface it points at.

---

**C-07 · Recommendation actionability (10 pts)**
Each recommendation specifies one concrete action and the location in the artifact where it applies. Directives without a location ("address this concern") do not qualify.

*PASS*: Every recommendation contains a concrete action and an artifact location.
*FAIL*: Any recommendation is directional without specifying what to do and where.

---

**C-08 · Severity calibration consistency (10 pts)**
Severity labels are applied consistently across the matrix. The locked scale and any calibration contract established before reviewing act as the enforcement standard; rows inconsistent with the contract are not staged.

*PASS*: Severity labels consistent with contract; no rows staged with unlocked or miscalibrated values.
*FAIL*: Severity labels vary arbitrarily; calibration contract absent or unenforced.

---

#### Aspirational tier

**C-09 · Cross-role synthesis (2 pts)**
After the per-role matrix, the skill produces a synthesis step that identifies convergence across roles (findings shared or reinforced by multiple reviewers) and conflict (findings that contradict across roles). A fallback is present for runs with no cross-role signal.

*PASS*: Synthesis step present; convergence and conflict both addressed; fallback for null signal.
*FAIL*: No synthesis step; convergence or conflict omitted; no fallback.

---

**C-10 · AMEND responsiveness (2 pts)**
The skill's AMEND block supports at minimum: adding roles to the pool, running `--depth deep`, rerunning the review, and reloading the role registry. Each AMEND operation produces a distinct behavior.

*PASS*: AMEND block covers add, deep, rerun, and reload operations.
*FAIL*: AMEND block missing or covers fewer than four standard operations.

---

**C-11 · Lens-anchoring step (2 pts)**
Before writing each finding, the skill quotes or paraphrases the role's orientation frame or lens. The anchor is not nominal — it must reflect the specific documented perspective of that role.

*PASS*: Lens anchor step present and enforced before each finding; anchor text is role-specific.
*FAIL*: Lens anchor absent, nominal, or identical across roles.

---

**C-12 · Severity calibration contract (2 pts)**
The three-value severity scale is locked as a contract before any reviewer runs. The contract is written, not implicit, and its terms govern the entire matrix.

*PASS*: Severity contract written and locked before first reviewer step.
*FAIL*: Scale established mid-run, post-hoc, or by convention only.

---

**C-13 · Challenger-first sequencing (2 pts)**
The skill processes challenger archetype roles before domain roles. The matrix reflects this ordering: challenger rows precede domain rows within each severity tier.

*PASS*: Challenger roles processed first; challenger rows appear before domain rows in matrix.
*FAIL*: Processing order not specified or challengers interleaved with domain roles.

---

**C-14 · Readiness-gate framing (2 pts)**
Prerequisites are framed as gates, not guidelines. Gate language uses the "you are not ready to advance until X" idiom or equivalent, applied universally across stage transitions — not only at selected checkpoints.

*PASS*: Readiness-gate idiom present at all major stage transitions; prerequisite language is conditional, not instructional.
*FAIL*: Prerequisite language is instructional ("you should do X") at any stage transition; gate framing limited to one or two checkpoints.

---

**C-15 · Severity-sorted matrix output (2 pts)**
The review matrix is rendered sorted by severity descending (HIGH first, then MEDIUM, then LOW). Within each severity tier, challenger rows precede domain rows. The sort order is declared, not inferred.

*PASS*: Matrix sorted severity-descending; challenger-before-domain within each tier; sort order stated in output.
*FAIL*: Matrix in execution order only; no severity sort; sort order not declared.

---

**C-16 · Hard-halt execution gate (2 pts)**
Missing or invalid preconditions trigger a formal halt, not an advisory. At minimum the role-registry absence (G1) produces an error-and-halt. Per-reviewer gate failures (invalid severity, missing lens anchor, missing location) also halt row staging rather than proceeding with a warning.

*PASS*: G1 halt present; per-reviewer gate failures halt row staging; no advisory-only enforcement path for any named gate.
*FAIL*: Halt limited to G1 only; per-reviewer gates produce warnings or "revisit" language without a formal stop.

---

**C-17 · Named halt identifier system (2 pts)**
Halt conditions carry unique stable identifiers (e.g., G1, G4-lens, G4-{role}, G5-empty) that appear verbatim in error output. The identifier namespace covers at least the role-registry gate and the per-reviewer row-staging gates. Named identifiers enable referencing from AMEND operations and from user-facing error messages.

*PASS*: At least three distinct gate conditions carry unique named identifiers appearing in halt output; identifiers are stable and referenceable.
*FAIL*: Halt conditions produce generic stop text with no stable ID; halt messages are not addressable by name.

---

**C-18 · AMEND gate-audit sub-command (2 pts)**
The AMEND block includes a gate-audit sub-command (e.g., `--amend halts`) that lists every gate identifier that fired in the most recent run. This sub-command enables post-run introspection without rerunning the skill. The output names gate identifiers, not generic messages.

*PASS*: AMEND block contains a gate-audit sub-command; output enumerates the named gate identifiers that triggered; sub-command is distinct from standard rerun.
*FAIL*: No gate-audit sub-command; fired gates not enumerable post-run; AMEND block restricted to add/deep/rerun/reload only.
