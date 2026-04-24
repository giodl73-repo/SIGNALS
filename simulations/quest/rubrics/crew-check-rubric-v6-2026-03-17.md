Scanning R6 scorecards for patterns present in the variations that are not already captured in C-01 through C-20.

**New patterns found:**

| Pattern | Variations | Evidence |
|---------|-----------|----------|
| Run health certificate (always-emit) | V-02 | Gate 10 emits `RUN HEALTH: PASS` or `RUN HEALTH: [N] HALT(S) FIRED` on every run — no absence semantics. Clean runs get the same section as failed runs; the heading encodes run state as a first-class signal. V-02 critical test: "Does the RUN HEALTH section appear on clean runs? YES." |
| Three-tier halt scope | V-03 | Halts classified into BLOCKING (run-level full stop), SCOPED (role skipped, EXCLUDED ROWS appendix, matrix continues), and DEFERRED (row tagged, forces CONDITIONAL readiness). V-03 critical test: "A run with only LOW findings but one DEFERRED row is CONDITIONAL, not READY." HALT REGISTRY carries a tier column. |
| Pre-committed skip-map | V-01 | Preamble pre-declares which sub-gates are bypassed on re-entry for each named halt condition. Halt messages embed skip-map annotations alongside recovery commands; C-19 covers embedding the command, C-23 covers pre-declaring the bypass map before any gate executes. V-01 C-19 evidence: "with skip-map annotation." V-01 C-20 evidence: "equivalent to consulting the skip-map manually." |

**Structural note:** C-21, C-22, and C-23 extend the halt/audit progression in independent directions. C-21 (always-emit health certificate) closes the observability gap on clean runs — prior criteria only address failure output. C-22 (three-tier scope) adds resolution granularity: a SCOPED halt continues the run for other roles; a DEFERRED halt lets the row survive into the matrix with a modified readiness verdict. C-23 (pre-committed skip-map) completes the C-19 pattern: C-19 embeds the recovery command at point-of-failure; C-23 publishes the sub-gate bypass plan in the preamble so re-entry is surgical rather than full replay.

**Scoring mechanics for v6:** 3 new criteria at 2 pts each. Aspirational tier grows from 24 to 30 pts; total max from 114 to 120. Golden threshold unchanged.

---

## crew-check — Quest Rubric v6

### Changelog

#### v5 → v6

Three new aspirational criteria added from R6 excellence signals:

| ID | Name | Source signal |
|----|------|---------------|
| C-21 | Run health certificate (always-emit) | V-02 introduces Gate 10 as an always-present RUN HEALTH section. Clean runs emit `RUN HEALTH: PASS` with gate enumeration and zero-halt confirmation; failed runs emit `RUN HEALTH: [N] HALT(S) FIRED`. No absence semantics: the section appears regardless of outcome. The heading encodes run state as a first-class signal without requiring the reader to scan for halts. Prior variations only produce halt output on failure; C-21 covers whether the run state is affirmatively reported on every run. |
| C-22 | Three-tier halt scope | V-03 classifies halts into three tiers: BLOCKING (run-level full stop, no further output), SCOPED (role skipped, matrix continues without that role, EXCLUDED ROWS appendix appended), and DEFERRED (finding included in matrix with tier tag, forces CONDITIONAL readiness verdict regardless of finding severity). The HALT REGISTRY includes a tier column. C-16 covers whether a hard-halt execution gate exists; C-22 covers whether halt conditions carry a resolution tier that governs how much of the run continues and how the readiness verdict is modified. |
| C-23 | Pre-committed skip-map | V-01 publishes a skip-map in the pre-execution preamble declaring which sub-gates are bypassed on re-entry for each named halt condition. Halt messages embed skip-map annotations alongside recovery commands. C-19 covers embedding the recovery command at point-of-failure; C-23 covers pre-declaring the sub-gate bypass plan before any gate executes, so re-entry is surgical (skipping already-completed sub-gates) rather than full replay. A variation can earn C-19 without C-23 (recovery command present, no pre-committed map) and C-23 without C-19 (map published in preamble, halt messages do not embed annotations). |

Aspirational tier total: 24 pts (v5) → 30 pts (v6), 2 pts × 15 criteria. Golden threshold unchanged: all 5 essential PASS + composite >= 80.

#### v4 → v5

Two aspirational criteria added from R4 excellence signals:

| ID | Name | Source signal |
|----|------|---------------|
| C-19 | Self-routing halt messages | V-03 and V-05 both embed recovery commands directly inside halt messages. V-03 pioneered the pattern (`→ To continue: /crew-check [artifact] --amend rerun:pm`); V-05 combined it with the stable ID system so the embedded command references the named gate. Prior variations halt with a named ID (C-17) but leave the user to consult the AMEND block separately. C-19 collapses that gap: the failure output is also the remediation prompt. |
| C-20 | Executable audit output | V-02 and V-05 both make the audit block actionable rather than diagnostic. V-02 adds `--amend halts:{id}` for focused single-gate re-entry; V-05 frames each audit entry as a ready-to-paste command (audit-as-AMEND-menu). C-18 covers whether the audit sub-command exists and enumerates fired gates; C-20 covers whether each audit entry includes a runnable re-entry command. A variation can earn C-18 with a read-only report and miss C-20. |

Aspirational tier total: 20 pts (v4) → 24 pts (v5).

#### v3 → v4

Two aspirational criteria added from R3 excellence signals:

| ID | Name | Source signal |
|----|------|---------------|
| C-17 | Named halt identifier system | V-02 and V-04 both assign stable names to halt conditions (G1, G4-lens, G4-{role}, G5-empty, etc.) that appear verbatim in error output. The naming pattern is load-bearing: it enables audit trails, targeted AMEND re-entry, and human-readable error messages. |
| C-18 | AMEND gate-audit sub-command | V-02 and V-04 both include `--amend halts` in the AMEND block, listing every gate identifier that fired in the most recent run. C-10 covers whether AMEND handles standard operations; C-18 covers whether AMEND exposes the halt audit trail. |

---

### Rubric v6 — Criteria Reference

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

**Total: 120 pts · Golden threshold: all 5 essential PASS + composite >= 80**

---

### Criterion Definitions

#### Essential tier

**C-01 · Role source traceability (12 pts)**
The reviewer pool is built exclusively from `.roles/`. No roles are invented or inferred from context. The skill names the source explicitly and does not proceed if the directory is absent.

*PASS*: Pool construction step references `.roles/` by path; no invented roles permitted.
*FAIL*: Any role sourced from memory, context, or inference; source path omitted.

**C-02 · Review matrix structure (12 pts)**
Gate 4 produces a structured matrix with columns for Role, Finding, Artifact Surface, Severity, and Recommendation. The matrix is the primary output artifact.

*PASS*: All five columns present; matrix format specified before execution.
*FAIL*: Any column absent; unstructured narrative substituted for matrix.

**C-03 · Perspective fidelity (12 pts)**
Each reviewer applies their assigned lens before producing findings. The lens anchor is not optional: it is a required sub-gate that precedes finding generation.

*PASS*: Lens anchor step enforced per role; findings traceable to lens perspective.
*FAIL*: Lens application implicit, skippable, or absent; generic findings not anchored to role perspective.

**C-04 · Depth mode compliance (12 pts)**
The skill accepts a `{{depth}}` parameter with at least `standard` and `deep` values. `deep` includes all roles; `standard` restricts to relevant roles with documented rationale.

*PASS*: Both modes defined; `standard` mode includes rationale for exclusions.
*FAIL*: Depth parameter absent; all roles always run without mode distinction.

**C-05 · Severity presence (12 pts)**
Every finding carries a severity rating. The severity scale is defined before any reviewer executes.

*PASS*: Scale defined pre-execution; every matrix row has a severity value.
*FAIL*: Severity absent from any row; scale undefined or post-hoc.

---

#### Recommended tier

**C-06 · Finding specificity (10 pts)**
Each finding names the specific artifact surface it addresses. Vague or artifact-free findings halt execution.

*PASS*: Surface named per finding; HALT fires on missing surface.
*FAIL*: Findings reference artifacts in aggregate or by type rather than specific surface; no halt on missing surface.

**C-07 · Recommendation actionability (10 pts)**
Each recommendation includes a location reference enabling direct action. Location-free recommendations halt execution.

*PASS*: Location reference required per recommendation; HALT fires on missing reference.
*FAIL*: Recommendations are directional without location; no halt on missing reference.

**C-08 · Severity calibration consistency (10 pts)**
A calibration contract is locked before any reviewer executes and validated against throughout the run. Severity assignments are checked against the contract, not assigned ad hoc.

*PASS*: Contract defined pre-execution; each severity assignment validated against it.
*FAIL*: Severity assigned without contract; calibration inconsistencies possible across reviewers.

---

#### Aspirational tier

**C-09 · Cross-role synthesis (2 pts)**
A synthesis gate produces 2–4 sentences identifying convergence or conflict across reviewer findings. At least one cross-role signal (agreement or tension) is named explicitly.

*PASS*: Synthesis gate present; ≥1 cross-role convergence or conflict identified by name.
*FAIL*: No synthesis gate; per-role findings not integrated.

**C-10 · AMEND responsiveness (2 pts)**
An AMEND block specifies operations for modifying the run after initial execution. Supported operations include at minimum: adding roles, changing depth, and rerunning specific gate sequences.

*PASS*: AMEND block present with ≥3 named operations.
*FAIL*: No AMEND block; post-run modification requires re-running from scratch.

**C-11 · Lens-anchoring step (2 pts)**
The lens anchor is an explicit, named sub-gate with a specified output format. Execution halts if the lens anchor output is missing or malformed.

*PASS*: G4a named explicitly with format; HALT on missing or malformed anchor.
*FAIL*: Lens application mentioned but not gated; no halt on missing anchor.

**C-12 · Severity calibration contract (2 pts)**
A PRE-EXECUTION table locks the severity scale with named levels and distinguishing criteria before any gate executes. The table is visible output, not internal state.

*PASS*: PRE-EXECUTION table emitted with named levels and criteria before Gate 1.
*FAIL*: Severity scale defined inline during execution or implicit in examples.

**C-13 · Challenger-first sequencing (2 pts)**
A challenger role occupies fixed slots at the opening and closing of the review sequence. The challenger runs before domain reviewers (opening bracket) and again after all domain findings (closing bracket).

*PASS*: Challenger in Gate 3 (opening) and Gate 8 (closing); positions fixed regardless of `{{depth}}` value.
*FAIL*: Challenger position variable or absent; no bracket structure.

**C-14 · Readiness-gate framing (2 pts)**
A readiness gate translates severity aggregation into a named verdict: HIGH findings produce BLOCKED, MEDIUM findings produce CONDITIONAL, LOW-only findings produce READY. The gate emits a `READINESS:` token.

*PASS*: Gate 7 defined with all three verdict mappings; `READINESS:` token emitted.
*FAIL*: Readiness verdict absent, implicit, or not mapped from severity levels.

**C-15 · Severity-sorted matrix output (2 pts)**
The final matrix is sorted by severity score descending. Within a severity tier, the challenger role appears before domain roles.

*PASS*: Sort specified as score 3→1; challenger precedes domain within tier.
*FAIL*: Matrix unsorted or sorted by role order rather than severity.

**C-16 · Hard-halt execution gate (2 pts)**
Pre-condition failures produce a hard halt with explicit "You are not ready to…" or equivalent language that terminates the run without producing partial output. A gate that finds zero findings across all roles also halts.

*PASS*: G1 and G2 pre-condition halts terminate run; G5 halts on zero findings; halt language is unambiguous.
*FAIL*: Pre-condition failures produce warnings rather than halts; partial output emitted before failure confirmed.

**C-17 · Named halt identifier system (2 pts)**
Every halt condition has a stable, human-readable identifier (e.g., `G1`, `G4a-{role}`, `G5-empty`) that appears verbatim in error output, audit trails, and AMEND commands. The identifier set is declared in a HALT REGISTRY before execution begins.

*PASS*: HALT REGISTRY present pre-execution; every halt message uses a declared identifier.
*FAIL*: Halt messages use positional or ad hoc descriptions; no registry; identifiers not reusable in AMEND commands.

**C-18 · AMEND gate-audit sub-command (2 pts)**
The AMEND block includes a `halts` operation that produces a HALT AUDIT table listing every gate identifier that fired in the most recent run. A `halts:{id}` variant supports targeted lookup of a single gate.

*PASS*: `halts` and `halts:{id}` in AMEND block; HALT AUDIT table format specified.
*FAIL*: AMEND block lacks halt audit operation; fired gates not enumerable post-run.

**C-19 · Self-routing halt messages (2 pts)**
Each halt message embeds a ready-to-run recovery command directing the user to the exact AMEND operation needed to continue. The user does not need to consult the AMEND block separately; the failure output is also the remediation prompt.

*PASS*: Every halt message includes `→ To continue: /crew-check {{artifact}} --amend rerun:{id}` or equivalent; recovery command references the named halt identifier.
*FAIL*: Halt messages name the condition (C-17) but leave recovery command lookup to the user.

**C-20 · Executable audit output (2 pts)**
Each entry in the HALT AUDIT table includes a paste-ready re-entry command, transforming the audit from a diagnostic report into an action menu. C-18 covers whether the audit exists and enumerates fired gates; C-20 covers whether each entry is directly executable.

*PASS*: HALT AUDIT table includes a Re-entry command column; each row contains a complete, paste-ready command.
*FAIL*: HALT AUDIT table is read-only; re-entry commands require manual construction from audit data.

**C-21 · Run health certificate (always-emit) (2 pts)**
A RUN HEALTH section is emitted on every run regardless of halt state. Clean runs emit `RUN HEALTH: PASS` with gate enumeration and zero-halt confirmation; failed runs emit `RUN HEALTH: [N] HALT(S) FIRED`. The section heading encodes run state as a first-class signal; no absence semantics are used. Prior criteria address what halt output contains; C-21 addresses whether run state is affirmatively reported when no halts fire.

*PASS*: Gate 10 (or equivalent) always emits a RUN HEALTH section; heading varies by outcome; clean-run version includes gate enumeration and zero-halt confirmation.
*FAIL*: RUN HEALTH section absent on clean runs; run health inferrable only by absence of halt messages.

**C-22 · Three-tier halt scope (2 pts)**
Halt conditions are classified into three tiers, each with a distinct resolution behavior. BLOCKING halts terminate the entire run with no further output. SCOPED halts skip the affected role, continue the run for remaining roles, and append an EXCLUDED ROWS section to the matrix. DEFERRED halts include the affected finding in the matrix with a tier tag and force a CONDITIONAL readiness verdict regardless of finding severity. The HALT REGISTRY includes a tier column. C-16 covers whether a hard-halt gate exists; C-22 covers whether halt conditions carry a resolution tier governing run continuation and readiness modification.

*PASS*: All three tiers defined with distinct behaviors; HALT REGISTRY has tier column; DEFERRED-forces-CONDITIONAL constraint stated explicitly; EXCLUDED ROWS appendix produced on SCOPED halt.
*FAIL*: All halts terminate the run identically (effectively all BLOCKING); no tier distinction; no EXCLUDED ROWS.

**C-23 · Pre-committed skip-map (2 pts)**
The pre-execution preamble declares a skip-map: for each named halt condition, which sub-gates are bypassed on re-entry. This pre-commitment is published before any gate executes so re-entry is surgical (skipping already-completed sub-gates) rather than full replay. Halt messages may embed skip-map annotations alongside recovery commands (C-19), but C-23 specifically covers whether the bypass plan is declared in the preamble as a contract with the user. A variation can earn C-19 (recovery command embedded) without C-23 (no pre-committed map), and C-23 without C-19 (map in preamble, no annotations in halt messages).

*PASS*: Preamble includes a skip-map table or equivalent structure mapping each named halt condition to its re-entry bypass set; published before Gate 1 executes.
*FAIL*: Re-entry skips sub-gates implicitly or by convention; no pre-committed bypass plan visible in preamble.
