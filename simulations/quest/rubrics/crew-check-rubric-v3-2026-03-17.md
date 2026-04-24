Scanning the R2 scorecard for patterns present in 2+ variations that aren't already captured in C-01 through C-13.

**New patterns found:**

| Pattern | Variations | Evidence |
|---------|-----------|----------|
| Readiness-gate framing | V-02, V-03 | V-02 C-11: "strongest compliance framing across all variations"; V-03 C-03/C-11: "Do not proceed to the finding without it" — both frame prerequisites as execution gates, not guidelines |
| Severity-sorted matrix output | V-03, V-04 | V-03 C-02: "sorted by severity score descending"; V-04 C-02: "Stage 6 severity-sorted matrix" — structural output property that reinforces calibration pressure |
| Hard-halt execution gate | V-01, V-04 | V-01 C-01: "error+halt if absent"; V-04 C-01: "ERROR+halt if missing" — transforms role-pool rule into an enforcement stop, distinct from C-01 traceability |

**Scoring mechanics for v3:** Add 3 new criteria at 2 pts each. Aspirational tier grows from 10 to 16 pts; total max from 100 to 106. Golden threshold (composite >= 80) unchanged. All current goldens score 106/106.

---

## crew-check — Quest Rubric v3

### Changelog: v2 → v3

Three new aspirational criteria added from R2 excellence signals:

| ID | Name | Source signal |
|----|------|---------------|
| C-14 | Readiness-gate framing | V-02 scored 100 and the commentary on C-11 explicitly marks it as "strongest compliance framing across all variations." V-03 uses identical "Do not proceed" gate language. The pattern: prerequisites framed as "you are not ready until X" rather than "you should do X." Future variations that use instructional framing instead of gate framing will correctly score lower. |
| C-15 | Severity-sorted matrix output | V-03 and V-04 both render the review matrix sorted by severity descending. V-03 further reinforces this with a numeric score per row. The sort is a structural forcing function: it surfaces calibration inconsistencies at render time and makes the synthesis step (C-09) faster and more reliable. |
| C-16 | Hard-halt execution gate | V-01 and V-04 both treat a missing role pool as ERROR+halt, not an advisory. C-01 covers where roles come from; C-16 covers what happens when the precondition fails. Advisory-only variations pass C-01 but miss the enforcement property that makes the gate load-bearing in automated or semi-automated runs. |

Aspirational tier total: 10 pts (v2) → 16 pts (v3), 2 pts × 8 criteria. Golden threshold unchanged: all 5 essential + composite >= 80.

---

### Rubric v3 — Criteria Reference

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

**Total: 106 pts · Golden threshold: all 5 essential PASS + composite >= 80**

---

### Criterion Definitions

#### Essential tier

**C-01 · Role source traceability (12 pts)**
The reviewer pool is built exclusively from `.roles/`. No roles are invented or inferred from context. The skill names the source explicitly and does not proceed if the directory is absent.

*PASS*: Pool construction step references `.roles/` by path; no invented roles permitted.
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
Standard mode selects 2–4 relevant roles plus at least one challenger archetype. `--depth deep` selects all available roles. The challenger is always included regardless of mode.

*PASS*: Role count and selection logic match the active depth mode; challenger present in all modes.
*FAIL*: Wrong role count; challenger omitted; depth flag ignored.

---

**C-05 · Severity presence (12 pts)**
Every finding row carries a severity label (HIGH / MEDIUM / LOW or equivalent defined scale). The severity is assigned during review, not post-hoc. A severity contract is applied before the matrix is rendered.

*PASS*: Every row has a severity label; contract applied before render.
*FAIL*: Any row missing severity; severity assigned after matrix is written.

---

#### Recommended tier

**C-06 · Finding specificity (10 pts)**
Every finding names a specific surface in the artifact: a section, field, diagram, or assumption. A finding without a named surface is not ready to be written.

*PASS*: Every finding names a surface; vague findings ("the overall structure") not permitted.
*PARTIAL*: Most findings name a surface; one or two are insufficiently specific.
*FAIL*: Findings state concerns without naming where in the artifact they live.

---

**C-07 · Recommendation actionability (10 pts)**
Every recommendation names both what to do and where in the artifact to do it. A recommendation that names only an action without a location is not ready.

*PASS*: Every recommendation has a location; "add X to section Y" form or equivalent.
*PARTIAL*: Most recommendations are location-specific; one or two omit the location.
*FAIL*: Recommendations describe changes without naming artifact location.

---

**C-08 · Severity calibration consistency (10 pts)**
Severity labels are applied consistently within the review. The scale has operational definitions — HIGH, MEDIUM, and LOW are defined in terms of commitment gates or ship decisions, not just relative urgency. When calibration is ambiguous, the skill resolves toward the higher severity rather than leaving it indeterminate.

*PASS*: Definitions present; consistent application across rows; ambiguous cases round up.
*PARTIAL*: Definitions present but inconsistently applied; or definitions absent but application appears consistent.
*FAIL*: No calibration definitions; severity labels appear arbitrary or contradictory across rows.

---

#### Aspirational tier

**C-09 · Cross-role synthesis (2 pts)**
After the matrix, the skill identifies findings that two or more reviewers converged on and findings where reviewers disagreed. The synthesis names the roles involved, not just the themes. If no convergence or conflict is detectable, the skill states this explicitly rather than omitting the step.

*PASS*: Convergence and conflict sections present; roles named; explicit fallback if none detected.
*FAIL*: No synthesis step; or synthesis present but roles not named.

---

**C-10 · AMEND responsiveness (2 pts)**
The skill includes an AMEND block with at minimum: add a role, switch to deep mode, rerun a specific role. Extensions (scope filtering, unsorted variant, inertia rerun) are additive.

*PASS*: AMEND block covers add, deep, and rerun:[role] at minimum.
*FAIL*: No AMEND block; or AMEND block covers fewer than three operations.

---

**C-11 · Lens-anchoring step (2 pts)**
The lens-anchor step (reading the role's orientation frame before writing the finding) is presented as a mandatory gate with explicit non-skip language. Framing like "Do not skip this step" or "Do not proceed without it" is required — not a suggestion, not a reminder.

*PASS*: Non-skip language present on the lens-anchor step; violation described as invalid, not suboptimal.
*FAIL*: Lens anchor present but framed as a suggestion; or non-skip language absent.

---

**C-12 · Severity calibration contract (2 pts)**
The severity scale includes operational definitions for each level using commit-gate or ship-decision semantics: HIGH means cannot defer / blocks commitment; MEDIUM means fix before ship; LOW means advisory / will not hold up the decision. Labels alone without operational definitions do not satisfy this criterion.

*PASS*: All three levels defined with commit-gate or ship-decision language.
*FAIL*: Labels present without operational definitions; or fewer than three levels defined.

---

**C-13 · Challenger-first sequencing (2 pts)**
The skill mandates that challenger archetype roles run before domain roles during the review pass. The ordering is stated as an explicit requirement in the execution steps, not implied by role selection.

*PASS*: Execution steps state challenger roles run first; explicit ordering mandate present.
*FAIL*: Challenger role included but ordering not mandated; or ordering described as a suggestion.

---

**C-14 · Readiness-gate framing (2 pts)**
Prerequisite steps — lens-anchor, severity contract, role pool validation — are framed as readiness gates using language like "you are not ready to write the finding" or "do not proceed to X without Y." This framing converts guidelines into execution stops. At least two distinct steps must use gate framing; advisory or reminder language does not satisfy this criterion.

*PASS*: At least two prerequisite steps use explicit readiness-gate or "do not proceed" language.
*FAIL*: Prerequisites framed as instructions or suggestions; gate framing absent or isolated to a single step.

---

**C-15 · Severity-sorted matrix output (2 pts)**
The review matrix is rendered with rows sorted by severity descending (HIGH rows first, then MEDIUM, then LOW). Ties within a severity tier preserve challenger-first order. An unsorted variant may be offered via AMEND but the default output is sorted.

*PASS*: Matrix sort order is severity descending by default; challenger-first tiebreaker within tier.
*FAIL*: Matrix rendered in role-selection order or arbitrary order; no sort applied.

---

**C-16 · Hard-halt execution gate (2 pts)**
The skill treats a missing or empty role pool as an execution error that halts the run with an explicit ERROR signal, not an advisory warning. The halt is described in the step definition, not implied. This applies at minimum to the role-pool precondition; extensions to other preconditions (missing spec, missing topic) are additive.

*PASS*: ERROR+halt explicitly described for missing role pool; language is "halt" or "stop," not "warn" or "note."
*FAIL*: Missing role pool produces a warning or fallback; no halt described; or halt implied but not stated.

---

### Scoring

```
Essential tier:     5 criteria × 12 pts = 60 pts  (all must PASS)
Recommended tier:   3 criteria × 10 pts = 30 pts
Aspirational tier:  8 criteria ×  2 pts = 16 pts
─────────────────────────────────────────────────
Maximum composite:                        106 pts

PARTIAL on a Recommended criterion = 5 pts (half credit).
Aspirational criteria are binary: PASS = 2 pts, FAIL = 0 pts.

Golden threshold: all 5 Essential criteria PASS  AND  composite >= 80
```
