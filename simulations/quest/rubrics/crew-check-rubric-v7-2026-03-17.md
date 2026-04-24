Done. Here is the complete updated rubric:

---

## crew-check — Quest Rubric v7

### v6 → v7 — New criteria

**Four patterns extracted from R7 scorecard evidence:**

| ID | Name | Source |
|----|------|--------|
| C-24 | Dual-axis calibration contract | V-02 |
| C-25 | Named convergence tier register | V-02 |
| C-26 | Artifact maturity stage pre-condition | V-03 |
| C-27 | Stage-scoped matrix and readiness filter | V-03 |

---

### What each new criterion covers

**C-24 — Dual-axis calibration contract (2 pts)**
V-02 extends the PRE-EXECUTION calibration section (C-12 covers severity) to also pre-commit a confidence scale. The confidence tier is load-bearing: secondary sort key after severity, readiness modifier (CONFIRMED treated as HIGH-effective), and prerequisite for C-25.

*PASS*: PRE-EXECUTION section emits both a severity table and a confidence table with named tiers and criteria; confidence appears in matrix schema and sort specification.
*FAIL*: Confidence in matrix but no pre-committed scale; freeform annotation without operational definition.

---

**C-25 — Named convergence tier register (2 pts)**
V-02 Gate 9 names convergence levels as a formal register: CORROBORATED (same finding across roles) and CONFIRMED (same finding + matching confidence tier). Confidence=LOW findings enumerated separately for verification. C-09 covers synthesis existence; C-25 covers whether levels are operationally defined. Presupposes C-24.

*PASS*: Synthesis gate emits a convergence register with >=2 named tier labels; distinguishing criteria for each; Confidence=LOW findings flagged separately.
*FAIL*: Freeform agreement narrative with no tier labels; confidence not used to distinguish convergence strength.

---

**C-26 — Artifact maturity stage pre-condition (2 pts)**
V-03 introduces G0.5, a pre-registry gate that fires BLOCKING before G1 if the artifact's maturity stage is absent or unrecognized. Stage is a structural pre-condition to pool construction, not a G4 content check. C-16 covers hard-halt gates within the run; C-26 covers whether stage is gated before G1 with its own HALT REGISTRY entry.

*PASS*: Pre-registry stage gate defined with named identifier; halts BLOCKING on absent/unrecognized stage; appears in HALT REGISTRY; executes before G1.
*FAIL*: Missing stage produces a warning or default; gate positioned within G4 rather than before G1.

---

**C-27 — Stage-scoped matrix and readiness filter (2 pts)**
V-03 adds a STAGE-APPROPRIATE column (YES / ADVISORY / NO / DEPRECATED) per matrix row. Matrix groups by scope tier before severity sort. Gate 7 reads only YES-scope rows; DEPRECATED always READY. AMEND supports `--amend stage:{value}`. C-14 covers readiness gate existence; C-26 covers the pre-condition; C-27 covers per-row scope, grouped matrix, and verdict filtering.

*PASS*: STAGE-APPROPRIATE column with four defined values; scope-grouped matrix; Gate 7 excludes non-YES rows; DEPRECATED yields automatic READY; `--amend stage:{value}` in AMEND block.
*FAIL*: Stage information in preamble only, not per-row; readiness computed across all findings; no stage-change AMEND.

---

### Scoring mechanics

| | v6 | v7 |
|--|-----|-----|
| Aspirational criteria | 15 | 19 |
| Aspirational pts | 30 | 38 |
| Total max | 120 | 128 |
| Golden threshold | unchanged | all 5 essential PASS + composite >= 80 |

---

### Structural relationships

**C-24 → C-25 dependency:** Naming convergence tiers requires confidence as a first-class dimension. A variation earns C-09 with freeform synthesis; it needs C-24 before C-25 is scoreable.

**C-26 → C-27 dependency:** Stage-scoped matrix is only coherent if stage was validated at run entry. C-26 (pre-condition gate) and C-27 (per-row propagation) are separable in the rubric but not in practice: a variation that earns C-27 without C-26 has a stage contract with no enforcement.

**C-24/C-25 vs. C-12/C-09:** The prior criteria remain in place at their original point values. C-24 and C-25 are additive extensions, not replacements.
-------|
| C-24 | Dual-axis calibration contract | V-02 extends the pre-execution calibration contract (C-12) to include a confidence scale alongside the severity scale. Both scales are locked in the PRE-EXECUTION section before Gate 1. The confidence tier feeds into sort order (secondary DESC key after severity), readiness verdict (CONFIRMED surfaces treated as HIGH-effective for Gate 7 purposes), and convergence synthesis (C-25). C-12 covers the severity-only contract; C-24 covers whether confidence is also pre-committed with named tiers and operational meanings. A variation earns C-12 for severity-only calibration and C-24 only when confidence is formalized with equal rigor. |
| C-25 | Named convergence tier register | V-02 Gate 9 names two convergence levels: CORROBORATED (same finding surface and direction across roles) and CONFIRMED (same finding + matching confidence tier). Confidence=LOW findings are separately enumerated for cross-role verification. The synthesis section emits a convergence register with named tier labels rather than a freeform summary. C-09 covers whether a synthesis gate exists and identifies >=1 cross-role signal; C-25 covers whether convergence levels are operationally defined and the register distinguishes agreement strength by label. A variation can earn C-09 without C-25; earning C-25 presupposes confidence data (C-24). |
| C-26 | Artifact maturity stage pre-condition | V-03 introduces G0.5, a pre-registry gate that fires BLOCKING before the role-load gate (G1) if the artifact's maturity stage is absent or unrecognized. Stage declaration is a structural pre-condition: all downstream gates assume stage is known. C-16 covers whether hard-halt execution gates exist within the run; C-26 covers whether artifact maturity stage is formalized as a named pre-condition gate that executes before G1 with its own halt identifier in the HALT REGISTRY. |
| C-27 | Stage-scoped matrix and readiness filter | V-03 adds a STAGE-APPROPRIATE column to the review matrix classifying each finding's relevance as YES (in-scope for this stage), ADVISORY (relevant to a future stage), NO (explicitly out of scope), or DEPRECATED (artifact retired). The matrix is grouped by scope tier before severity sort within tier. Gate 7 reads only YES-scope rows when computing the readiness verdict; DEPRECATED artifacts automatically receive READY because no in-scope findings exist. AMEND supports `--amend stage:{value}` for stage change without full re-execution. C-14 covers whether a readiness gate exists; C-26 covers the stage pre-condition; C-27 covers whether finding scope is declared per row, the matrix is grouped by scope, and the readiness verdict filters to YES-scope findings only. |

Aspirational tier total: 30 pts (v6) -> 38 pts (v7), 2 pts x 19 criteria. Golden threshold unchanged: all 5 essential PASS + composite >= 80.

#### v5 -> v6

Three new aspirational criteria added from R6 excellence signals:

| ID | Name | Source signal |
|----|------|---------------|
| C-21 | Run health certificate (always-emit) | V-02 introduces Gate 10 as an always-present RUN HEALTH section. Clean runs emit `RUN HEALTH: PASS` with gate enumeration and zero-halt confirmation; failed runs emit `RUN HEALTH: [N] HALT(S) FIRED`. No absence semantics: the section appears regardless of outcome. The heading encodes run state as a first-class signal without requiring the reader to scan for halts. Prior variations only produce halt output on failure; C-21 covers whether the run state is affirmatively reported on every run. |
| C-22 | Three-tier halt scope | V-03 classifies halts into three tiers: BLOCKING (run-level full stop, no further output), SCOPED (role skipped, matrix continues without that role, EXCLUDED ROWS appendix appended), and DEFERRED (finding included in matrix with tier tag, forces CONDITIONAL readiness verdict regardless of finding severity). The HALT REGISTRY includes a tier column. C-16 covers whether a hard-halt execution gate exists; C-22 covers whether halt conditions carry a resolution tier that governs how much of the run continues and how the readiness verdict is modified. |
| C-23 | Pre-committed skip-map | V-01 publishes a skip-map in the pre-execution preamble declaring which sub-gates are bypassed on re-entry for each named halt condition. Halt messages embed skip-map annotations alongside recovery commands. C-19 covers embedding the recovery command at point-of-failure; C-23 covers pre-declaring the sub-gate bypass plan before any gate executes, so re-entry is surgical (skipping already-completed sub-gates) rather than full replay. A variation can earn C-19 without C-23 (recovery command present, no pre-committed map) and C-23 without C-19 (map published in preamble, halt messages do not embed annotations). |

Aspirational tier total: 24 pts (v5) -> 30 pts (v6).

#### v4 -> v5

Two aspirational criteria added from R4 excellence signals:

| ID | Name | Source signal |
|----|------|---------------|
| C-19 | Self-routing halt messages | V-03 and V-05 both embed recovery commands directly inside halt messages. V-03 pioneered the pattern (`-> To continue: /crew-check [artifact] --amend rerun:pm`); V-05 combined it with the stable ID system so the embedded command references the named gate. Prior variations halt with a named ID (C-17) but leave the user to consult the AMEND block separately. C-19 collapses that gap: the failure output is also the remediation prompt. |
| C-20 | Executable audit output | V-02 and V-05 both make the audit block actionable rather than diagnostic. V-02 adds `--amend halts:{id}` for focused single-gate re-entry; V-05 frames each audit entry as a ready-to-paste command (audit-as-AMEND-menu). C-18 covers whether the audit sub-command exists and enumerates fired gates; C-20 covers whether each audit entry includes a runnable re-entry command. A variation can earn C-18 with a read-only report and miss C-20. |

Aspirational tier total: 20 pts (v4) -> 24 pts (v5).

#### v3 -> v4

Two aspirational criteria added from R3 excellence signals:

| ID | Name | Source signal |
|----|------|---------------|
| C-17 | Named halt identifier system | V-02 and V-04 both assign stable names to halt conditions (G1, G4-lens, G4-{role}, G5-empty, etc.) that appear verbatim in error output. The naming pattern is load-bearing: it enables audit trails, targeted AMEND re-entry, and human-readable error messages. |
| C-18 | AMEND gate-audit sub-command | V-02 and V-04 both include `--amend halts` in the AMEND block, listing every gate identifier that fired in the most recent run. C-10 covers whether AMEND handles standard operations; C-18 covers whether AMEND exposes the halt audit trail. |

---

### Rubric v7 -- Criteria Reference

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
| Aspirational | C-21 | Run health certificate (always-emit) | 2 |
| Aspirational | C-22 | Three-tier halt scope | 2 |
| Aspirational | C-23 | Pre-committed skip-map | 2 |
| Aspirational | C-24 | Dual-axis calibration contract | 2 |
| Aspirational | C-25 | Named convergence tier register | 2 |
| Aspirational | C-26 | Artifact maturity stage pre-condition | 2 |
| Aspirational | C-27 | Stage-scoped matrix and readiness filter | 2 |

**Total: 128 pts - Golden threshold: all 5 essential PASS + composite >= 80**

---

### Criterion Definitions

#### Essential tier

**C-01 - Role source traceability (12 pts)**
The reviewer pool is built exclusively from `.roles/`. No roles are invented or inferred from context. The skill names the source explicitly and does not proceed if the directory is absent.

*PASS*: Pool construction step references `.roles/` by path; no invented roles permitted.
*FAIL*: Any role sourced from memory, context, or inference; source path omitted.

**C-02 - Review matrix structure (12 pts)**
Gate 4 produces a structured matrix with columns for Role, Finding, Artifact Surface, Severity, and Recommendation. The matrix is the primary output artifact.

*PASS*: All five columns present; matrix format specified before execution.
*FAIL*: Any column absent; unstructured narrative substituted for matrix.

**C-03 - Perspective fidelity (12 pts)**
Each reviewer applies their assigned lens before producing findings. The lens anchor is not optional: it is a required sub-gate that precedes finding generation.

*PASS*: Lens anchor step enforced per role; findings traceable to lens perspective.
*FAIL*: Lens application implicit, skippable, or absent; generic findings not anchored to role perspective.

**C-04 - Depth mode compliance (12 pts)**
The skill accepts a `{{depth}}` parameter with at least `standard` and `deep` values. `deep` includes all roles; `standard` restricts to relevant roles with documented rationale.

*PASS*: Both modes defined; `standard` mode includes rationale for exclusions.
*FAIL*: Depth parameter absent; all roles always run without mode distinction.

**C-05 - Severity presence (12 pts)**
Every finding carries a severity rating. The severity scale is defined before any reviewer executes.

*PASS*: Scale defined pre-execution; every matrix row has a severity value.
*FAIL*: Severity absent from any row; scale undefined or post-hoc.

---

#### Recommended tier

**C-06 - Finding specificity (10 pts)**
Each finding names the specific artifact surface it addresses. Vague or artifact-free findings halt execution.

*PASS*: Surface named per finding; HALT fires on missing surface.
*FAIL*: Findings reference artifacts in aggregate or by type rather than specific surface; no halt on missing surface.

**C-07 - Recommendation actionability (10 pts)**
Each recommendation includes a location reference enabling direct action. Location-free recommendations halt execution.

*PASS*: Location reference required per recommendation; HALT fires on missing reference.
*FAIL*: Recommendations are directional without location; no halt on missing reference.

**C-08 - Severity calibration consistency (10 pts)**
A calibration contract is locked before any reviewer executes and validated against throughout the run. Severity assignments are checked against the contract, not assigned ad hoc.

*PASS*: Contract defined pre-execution; each severity assignment validated against it.
*FAIL*: Severity assigned without contract; calibration inconsistencies possible across reviewers.

---

#### Aspirational tier

**C-09 - Cross-role synthesis (2 pts)**
A synthesis gate produces 2-4 sentences identifying convergence or conflict across reviewer findings. At least one cross-role signal (agreement or tension) is named explicitly.

*PASS*: Synthesis gate present; >=1 cross-role convergence or conflict identified by name.
*FAIL*: No synthesis gate; per-role findings not integrated.

**C-10 - AMEND responsiveness (2 pts)**
An AMEND block specifies operations for modifying the run after initial execution. Supported operations include at minimum: adding roles, changing depth, and rerunning specific gate sequences.

*PASS*: AMEND block present with >=3 named operations.
*FAIL*: No AMEND block; post-run modification requires re-running from scratch.

**C-11 - Lens-anchoring step (2 pts)**
The lens anchor is an explicit, named sub-gate with a specified output format. Execution halts if the lens anchor output is missing or malformed.

*PASS*: G4a named explicitly with format; HALT on missing or malformed anchor.
*FAIL*: Lens application mentioned but not gated; no halt on missing anchor.

**C-12 - Severity calibration contract (2 pts)**
A PRE-EXECUTION table locks the severity scale with named levels and distinguishing criteria before any gate executes. The table is visible output, not internal state.

*PASS*: PRE-EXECUTION table emitted with named levels and criteria before Gate 1.
*FAIL*: Severity scale defined inline during execution or implicit in examples.

**C-13 - Challenger-first sequencing (2 pts)**
A challenger role occupies fixed slots at the opening and closing of the review sequence. The challenger runs before domain reviewers (opening bracket) and again after all domain findings (closing bracket).

*PASS*: Challenger in Gate 3 (opening) and Gate 8 (closing); positions fixed regardless of `{{depth}}` value.
*FAIL*: Challenger position variable or absent; no bracket structure.

**C-14 - Readiness-gate framing (2 pts)**
A readiness gate translates severity aggregation into a named verdict: HIGH findings produce BLOCKED, MEDIUM findings produce CONDITIONAL, LOW-only findings produce READY. The gate emits a `READINESS:` token.

*PASS*: Gate 7 defined with all three verdict mappings; `READINESS:` token emitted.
*FAIL*: Readiness verdict absent, implicit, or not mapped from severity levels.

**C-15 - Severity-sorted matrix output (2 pts)**
The final matrix is sorted by severity score descending. Within a severity tier, the challenger role appears before domain roles.

*PASS*: Sort specified as score 3->1; challenger precedes domain within tier.
*FAIL*: Matrix unsorted or sorted by role order rather than severity.

**C-16 - Hard-halt execution gate (2 pts)**
Pre-condition failures produce a hard halt with explicit "You are not ready to..." or equivalent language that terminates the run without producing partial output. A gate that finds zero findings across all roles also halts.

*PASS*: G1 and G2 pre-condition halts terminate run; G5 halts on zero findings; halt language is unambiguous.
*FAIL*: Pre-condition failures produce warnings rather than halts; partial output emitted before failure confirmed.

**C-17 - Named halt identifier system (2 pts)**
Every halt condition has a stable, human-readable identifier (e.g., `G1`, `G4a-{role}`, `G5-empty`) that appears verbatim in error output, audit trails, and AMEND commands. The identifier set is declared in a HALT REGISTRY before execution begins.

*PASS*: HALT REGISTRY present pre-execution; every halt message uses a declared identifier.
*FAIL*: Halt messages use positional or ad hoc descriptions; no registry; identifiers not reusable in AMEND commands.

**C-18 - AMEND gate-audit sub-command (2 pts)**
The AMEND block includes a `halts` operation that produces a HALT AUDIT table listing every gate identifier that fired in the most recent run. A `halts:{id}` variant supports targeted lookup of a single gate.

*PASS*: `halts` and `halts:{id}` in AMEND block; HALT AUDIT table format specified.
*FAIL*: AMEND block lacks halt audit operation; fired gates not enumerable post-run.

**C-19 - Self-routing halt messages (2 pts)**
Each halt message embeds a ready-to-run recovery command directing the user to the exact AMEND operation needed to continue. The user does not need to consult the AMEND block separately; the failure output is also the remediation prompt.

*PASS*: Every halt message includes `-> To continue: /crew-check {{artifact}} --amend rerun:{id}` or equivalent; recovery command references the named halt identifier.
*FAIL*: Halt messages name the condition (C-17) but leave recovery command lookup to the user.

**C-20 - Executable audit output (2 pts)**
Each entry in the HALT AUDIT table includes a paste-ready re-entry command, transforming the audit from a diagnostic report into an action menu. C-18 covers whether the audit exists and enumerates fired gates; C-20 covers whether each entry is directly executable.

*PASS*: HALT AUDIT table includes a Re-entry command column; each row contains a complete, paste-ready command.
*FAIL*: HALT AUDIT table is read-only; re-entry commands require manual construction from audit data.

**C-21 - Run health certificate (always-emit) (2 pts)**
A RUN HEALTH section is emitted on every run regardless of halt state. Clean runs emit `RUN HEALTH: PASS` with gate enumeration and zero-halt confirmation; failed runs emit `RUN HEALTH: [N] HALT(S) FIRED`. The section heading encodes run state as a first-class signal; no absence semantics are used. Prior criteria address what halt output contains; C-21 addresses whether run state is affirmatively reported when no halts fire.

*PASS*: Gate 10 (or equivalent) always emits a RUN HEALTH section; heading varies by outcome; clean-run version includes gate enumeration and zero-halt confirmation.
*FAIL*: RUN HEALTH section absent on clean runs; run health inferrable only by absence of halt messages.

**C-22 - Three-tier halt scope (2 pts)**
Halt conditions are classified into three tiers, each with a distinct resolution behavior. BLOCKING halts terminate the entire run with no further output. SCOPED halts skip the affected role, continue the run for remaining roles, and append an EXCLUDED ROWS section to the matrix. DEFERRED halts include the affected finding in the matrix with a tier tag and force a CONDITIONAL readiness verdict regardless of finding severity. The HALT REGISTRY includes a tier column. C-16 covers whether a hard-halt gate exists; C-22 covers whether halt conditions carry a resolution tier governing run continuation and readiness modification.

*PASS*: All three tiers defined with distinct behaviors; HALT REGISTRY has tier column; DEFERRED-forces-CONDITIONAL constraint stated explicitly; EXCLUDED ROWS appendix produced on SCOPED halt.
*FAIL*: All halts terminate the run identically (effectively all BLOCKING); no tier distinction; no EXCLUDED ROWS.

**C-23 - Pre-committed skip-map (2 pts)**
The pre-execution preamble declares a skip-map: for each named halt condition, which sub-gates are bypassed on re-entry. This pre-commitment is published before any gate executes so re-entry is surgical (skipping already-completed sub-gates) rather than full replay. Halt messages may embed skip-map annotations alongside recovery commands (C-19), but C-23 specifically covers whether the bypass plan is declared in the preamble as a contract with the user. A variation can earn C-19 (recovery command embedded) without C-23 (no pre-committed map), and C-23 without C-19 (map in preamble, no annotations in halt messages).

*PASS*: Preamble includes a skip-map table or equivalent structure mapping each named halt condition to its re-entry bypass set; published before Gate 1 executes.
*FAIL*: Re-entry skips sub-gates implicitly or by convention; no pre-committed bypass plan visible in preamble.

**C-24 - Dual-axis calibration contract (2 pts)**
The PRE-EXECUTION section locks a confidence scale alongside the severity scale (C-12). Both scales are published before Gate 1 with named tiers and operational meanings. The confidence tier is load-bearing: it feeds into sort order (secondary DESC key after severity), readiness verdict (CONFIRMED surfaces treated as HIGH-effective for Gate 7), and convergence synthesis (C-25). C-12 covers the severity-only contract; C-24 covers whether confidence is formalized with equal rigor as a pre-committed scale. A variation earns C-12 for severity-only calibration and C-24 only when confidence is also named, tiered, and operationally defined in the preamble.

*PASS*: PRE-EXECUTION section includes a confidence scale table with named tiers and criteria; confidence tier appears in matrix schema; sort order references confidence as secondary key.
*FAIL*: Confidence appears in matrix but with no pre-committed scale; scale defined inline during execution; or confidence treated as freeform annotation without operational meaning.

**C-25 - Named convergence tier register (2 pts)**
The synthesis gate (C-09) distinguishes convergence levels by name rather than reporting agreement in aggregate. At minimum: CORROBORATED (same finding surface and direction across >=2 roles) and CONFIRMED (same finding + matching confidence tier). Confidence=LOW findings are separately enumerated for cross-role verification even when not converged. The synthesis section emits a labeled convergence register. C-09 covers whether synthesis exists and names >=1 signal; C-25 covers whether convergence strength is graded by tier label. Earning C-25 presupposes confidence data from C-24.

*PASS*: Synthesis gate emits a convergence register with >=2 named tier labels; CORROBORATED and CONFIRMED (or equivalent) defined with distinguishing criteria; Confidence=LOW findings flagged separately.
*FAIL*: Synthesis names convergence in aggregate without tier labels; no register structure; or confidence not used to distinguish convergence strength.

**C-26 - Artifact maturity stage pre-condition (2 pts)**
A named pre-registry gate (e.g., G0.5) fires BLOCKING before the role-load gate (G1) if the artifact's maturity stage is absent or unrecognized. Stage declaration is a structural pre-condition: all downstream gates assume stage is known. The gate has its own halt identifier in the HALT REGISTRY. C-16 covers whether hard-halt execution gates exist within the run; C-26 covers whether artifact maturity stage is formalized as a named gate that executes before G1 -- a pre-condition to pool construction, not a content validation within G4.

*PASS*: Pre-registry stage gate defined with named identifier; halts BLOCKING on absent or unrecognized stage; gate appears in HALT REGISTRY; gate executes before G1.
*FAIL*: Stage accepted as optional parameter without a pre-condition gate; missing stage produces a warning or default behavior rather than a BLOCKING halt before G1.

**C-27 - Stage-scoped matrix and readiness filter (2 pts)**
The review matrix includes a STAGE-APPROPRIATE column classifying each finding's relevance to the declared artifact maturity stage: YES (in-scope), ADVISORY (future-stage relevance), NO (explicitly out of scope), or DEPRECATED (artifact retired). The matrix is grouped by scope tier before severity sort within tier. Gate 7 reads only YES-scope rows when computing the readiness verdict; DEPRECATED artifacts automatically receive READY. AMEND supports `--amend stage:{value}` for stage change without full re-execution. C-14 covers whether a readiness gate exists; C-26 covers the stage pre-condition; C-27 covers whether finding scope is declared per row, the matrix groups by scope, and the readiness verdict filters to YES-scope findings only.

*PASS*: STAGE-APPROPRIATE column in matrix schema with YES/ADVISORY/NO/DEPRECATED values defined; matrix grouped by scope before severity sort; Gate 7 excludes non-YES rows from verdict computation; DEPRECATED produces automatic READY; `--amend stage:{value}` in AMEND block.
*FAIL*: Stage information appears in preamble but does not produce a per-row scope column; readiness verdict computed across all findings regardless of stage relevance; no stage-change AMEND operation.
