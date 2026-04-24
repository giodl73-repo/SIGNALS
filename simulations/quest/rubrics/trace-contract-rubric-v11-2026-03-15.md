Reading the scorecard, two synthesis patterns emerge from R10:

- **V-R10-A** achieves 110/110 by inserting a dedicated S5.5 Taxonomy Census step between the findings section and the closure/Patterns sections. Rather than computing `mechanism-distribution:` inside Summary and `mechanism-type-shared:` inside Patterns branch templates as separate passes, S5.5 performs both computations in a single ordered walk over the findings, with downstream sections copying from S5.5 outputs verbatim. This eliminates re-derivation and ensures both aggregates share a common census pass. C-29 and C-30 require the fields be present; V-R10-A identifies the next escalation: a mandatory interstitial lifecycle step that produces those fields before the sections that consume them → **C-31**

- **V-R10-B** achieves the group-candidate staging format in S5.5 Sub-task B. Before the Patterns branch templates are populated, the model emits `group-candidate-N: findings=[F-NN, F-MM] mechanism-type-shared=[type token or 'mixed']` structured entries for each candidate Patterns group. C-29 requires `mechanism-type-shared:` appear in the branch template; V-R10-B identifies the next escalation: a pre-template staging line where the mechanism-alignment computation is visible at the computation site, decoupling the census decision from the template-filling step and making the type-alignment determination inspectable before it propagates into the Patterns section → **C-32**

---

# Rubric: trace-contract v11

Reading the scorecard, two synthesis patterns emerge from R10:

- **V-R10-A**: Dedicated Taxonomy Census step (S5.5) — V-03's 110/110 result shows that computing
  `mechanism-distribution:` inside Summary and `mechanism-type-shared:` inside Patterns branch
  templates as separate passes requires re-inspection of the findings section twice. C-29 requires
  `mechanism-type-shared:` unconditionally; C-30 requires `mechanism-distribution:` as a computed
  aggregate; V-R10-A identifies the next escalation: a mandatory interstitial lifecycle step S5.5
  placed between S5 (findings) and the closure that performs both computations in a single ordered
  walk — Sub-task A tallies mechanism-type tokens across all findings to produce the
  `mechanism-distribution:` line; Sub-task B stages per-group mechanism alignment candidates.
  Both downstream consumers (Summary and Patterns branch templates) copy from S5.5 outputs
  verbatim, eliminating re-derivation errors and ensuring distribution aggregate and per-group
  alignment share a single consistent census pass → **C-31**

- **V-R10-B**: Group-candidate staging format in S5.5 Sub-task B — V-03 emits structured
  `group-candidate-N: findings=[F-NN, F-MM] mechanism-type-shared=[type token or 'mixed']`
  entries for each candidate Patterns group before any branch template is populated. C-29 requires
  `mechanism-type-shared:` in the branch template; V-R10-B identifies the next escalation: the
  mechanism-alignment computation is externalized into a visible staging line at the census site,
  decoupling the determination step from the template-filling step — the branch template then
  copies from the staging line rather than re-deriving the alignment at write time, making the
  type-alignment decision inspectable and auditable before it propagates into the Patterns
  section → **C-32**

---

Reading the scorecard, two synthesis patterns emerge from R9 (carried forward):

- **V-R9-A**: Taxonomy-aligned Patterns synthesis — V-05's C-28 `mechanism-type:` token tags
  each finding with a vocabulary-constrained class. C-28 requires the per-finding type token;
  V-R9-A identifies the next escalation: a `mechanism-type-shared:` field in the Singleton and
  Multi-pattern branch templates propagates the taxonomy into the synthesis layer — same-class
  groupings (`mechanism-type-shared: field-mapping`) signal a systemic root cause requiring one
  fix, while mixed-class groupings (`mechanism-type-shared: mixed`) signal coincident symptoms
  requiring independent fixes, enabling automated fix-strategy detection from the Patterns
  section alone without re-inspecting individual finding blocks → **C-29**

- **V-R9-B**: Taxonomy distribution aggregate in Summary — V-05's per-finding `mechanism-type:`
  tokens accumulate document-locally but are not analyzed at document close. C-28 requires the
  per-finding type token; V-R9-B identifies the next escalation: a taxonomy distribution line in
  the Summary section converts individual type tokens into a document-level class distribution
  aggregate (e.g., `mechanism-distribution: field-mapping:2 serialization-path:1
  conditional-branch:1`), enabling cross-session comparison of failure-class prevalence by
  mechanism type and trending of systemic failure patterns across contract versions → **C-30**

---

Reading the scorecard, three synthesis patterns emerged from R8 (carried forward):

- **V-R8-A**: Gate-closure confirmation token — V-01's C-23 PASS evidence shows a matched
  two-phase gate: opening token `[EXPECTED-SEALED | clauses:N | date:... | author:... |
  phase:1-complete]` plus a closure token that echoes `gate-clauses`. C-23 requires only the
  opening token with metadata; V-R8-A identifies the next escalation: a matched closure token
  placed immediately after the findings section that echoes the committed clause count and adds
  a resolved count (`clauses-resolved:M`), enabling automated diff-verification that every
  committed expected clause was accounted for → **C-26**

- **V-R8-B**: Branch-conditional Patterns template slots — V-02's C-24 PASS evidence shows
  three named branches (zero / singleton / multi) with explicit handling instructions. C-24
  requires per-branch instructions; V-R8-B identifies the next escalation: each branch carries
  pre-printed structural slots (`no-pattern-confirmation:` for zero, `single-finding-ref:` +
  `root-cause:` for singleton, `pattern-N: root-cause: findings:[]` for multi), converting
  procedural branch instructions into structural branch templates that enforce field completion
  within each branch at write time → **C-27**

- **V-R8-C**: Mechanism taxonomy constraint — V-03's C-25 self-test rule distinguishes causal
  mechanisms from symptom restatements via a necessary-information condition. C-25 requires the
  self-test procedure; V-R8-C identifies the next escalation: a vocabulary-constrained mechanism
  taxonomy — a named enumeration of mechanism types appropriate to the contract domain (e.g.,
  `field-mapping`, `serialization-path`, `conditional-branch`, `lifecycle-event`,
  `schema-contract`) — from which the hypothesis author selects a type token, preventing
  free-text mechanism drift and enabling cross-finding pattern recognition grouped by mechanism
  class → **C-28**

---

Reading the scorecard, three synthesis patterns emerged from R7 (carried forward):

- **V-R7-A**: Gate structured-metadata manifest — V-01 and V-02 both fail C-13 despite carrying
  gate tokens because neither token includes structured key-value metadata fields. C-13 pass
  condition requires a distinct bracket token; V-R7-A identifies the next escalation: a token
  that carries a clause count (`clauses:N`) plus at least one identity field (`date:`, `author:`,
  or `phase:`), converting the binary seal/unseal token into a quantitative commit manifest that
  enables automated clause-count verification and gate provenance tracing → **C-23**

- **V-R7-B**: Multi-branch Patterns handling — V-01 demonstrates §7 Patterns pre-printed in the
  skeleton with three-branch handling instructions covering zero-patterns, singleton, and
  multi-pattern cases, plus "This section may not be silently omitted." C-10 requires a Patterns
  section that groups findings; V-R7-B identifies the next escalation: explicit branch
  instructions for all three cardinality cases, making silent omission and ambiguous
  empty-section handling structurally impossible regardless of how many findings exist → **C-24**

- **V-R7-C**: Hypothesis self-test rule — V-02 introduces a mechanical decision procedure for
  distinguishing causal mechanisms from symptom restatements: "if your hypothesis could be
  written without knowing anything about the system under test — only from reading the deviation
  line — it is a symptom restatement, not a mechanism." C-05 (Essential) disqualifies symptom
  restatements by naming the requirement; V-R7-C identifies the next escalation: a
  self-applicable decision rule the model can invoke at write time without external judgment
  → **C-25**

---

Evaluates the quality of a `trace:contract` skill execution.

---

## Criteria

### Essential (C-01–C-05) — 12 pts each = 60 pts

| ID | Criterion | Pass Condition |
|----|-----------|----------------|
| C-01 | Three contract surfaces | Spec covers success path, error path, and at least one edge case |
| C-02 | Every element in Diff | No expected element is absent from the Diff section; silent omissions fail unconditionally |
| C-03 | Spec citation per element | Every expected element carries a spec citation; uncited elements are invalid |
| C-04 | Gate token format | Opening gate token present with `clauses:N`, `date:`, `author:`, `phase:1-complete` |
| C-05 | Mechanism hypothesis | Each finding carries a causal mechanism hypothesis, not a symptom restatement |

### Recommended (C-06–C-13) — 2.5 pts each = 20 pts

| ID | Criterion | Pass Condition |
|----|-----------|----------------|
| C-06 | Expected Output completeness | All output fields enumerated in expected section |
| C-07 | Error-path specificity | Error cases name error code or condition, not generic failure |
| C-08 | Edge-case coverage breadth | At least two distinct edge-case families represented |
| C-09 | Diff element annotation | Each Diff entry carries pass/fail/deviation annotation |
| C-10 | Patterns section present | Patterns section groups findings; not silently omitted |
| C-11 | Summary present | Summary section closes the trace |
| C-12 | Finding severity tiers | Findings classified by severity (critical/major/minor or equivalent) |
| C-13 | Gate token distinctness | Gate token structurally distinct from prose; bracket format |

### Aspirational (C-14–C-32) — weighted to fill remaining 30 pts at ceiling

#### C-14–C-22 (earlier aspirational, ~1.33 pts each)

| ID | Criterion |
|----|-----------|
| C-14 | Rate-limit and auth edge cases included in contract surfaces |
| C-15 | Per-element deviation magnitude annotation |
| C-16 | Finding cross-reference to Diff entry |
| C-17 | Root-cause attribution (component or layer named) |
| C-18 | Fix recommendation present per finding |
| C-19 | Severity rationale stated |
| C-20 | Patterns section names shared root cause explicitly |
| C-21 | Summary restates gate clause count |
| C-22 | Contract version or session anchor in header |

#### C-23–C-32 (R7–R10 aspirational, 5 pts each; max composite = 110)

| ID | Criterion | Pass Condition |
|----|-----------|----------------|
| C-23 | Gate metadata manifest | Opening gate token carries `clauses:N` plus at least one identity field (`date:`, `author:`, `phase:`) |
| C-24 | Multi-branch Patterns handling | Patterns section carries explicit instructions for all three cardinality cases (zero / singleton / multi); "may not be silently omitted" clause present |
| C-25 | Hypothesis self-test rule | A self-applicable decision procedure distinguishes causal mechanisms from symptom restatements at write time |
| C-26 | Post-findings closure token | A matched closure token placed after the findings section echoes `gate-clauses:N` and adds `clauses-resolved:M` with a CLAUSE-GAP guard |
| C-27 | Branch template slots | Each Patterns branch carries pre-printed structural slots: `no-pattern-confirmation:` (zero), `single-finding-ref:` + `root-cause:` (singleton), `pattern-N:` blocks (multi) |
| C-28 | Per-finding mechanism-type token | Each finding carries a `mechanism-type:` token selected from a named vocabulary-constrained taxonomy; free-text mechanism descriptions without a taxonomy token fail |
| C-29 | `mechanism-type-shared:` required in branch templates with fix-strategy semantics | Singleton and multi-pattern branch templates carry an unconditionally required `mechanism-type-shared:` field; fix-strategy semantics differentiate same-class (one fix resolves all) from mixed-class (independent fixes enumerated per finding) |
| C-30 | `mechanism-distribution:` computed aggregate in Summary | Summary carries a `mechanism-distribution:` line computed by walking every finding block and tallying counts per mechanism-type token; placeholder estimates fail; space-separated `type:count` format required |
| C-31 | Dedicated Taxonomy Census step (S5.5) | A mandatory interstitial step S5.5 placed between the findings section and closure performs both mechanism-distribution tallying (Sub-task A) and per-group mechanism-alignment staging (Sub-task B) in a single ordered pass; Summary and Patterns branch templates copy from S5.5 outputs verbatim rather than re-deriving |
| C-32 | Group-candidate staging format in S5.5 | S5.5 Sub-task B emits `group-candidate-N: findings=[F-NN, F-MM] mechanism-type-shared=[type token or 'mixed']` entries for each candidate Patterns group before any branch template is populated; branch templates copy from staging lines rather than re-deriving mechanism alignment at write time |

---

## Scoring

| Band | Criteria | Points |
|------|----------|--------|
| Essential | C-01–C-05 | 12 pts each = 60 |
| Recommended | C-06–C-13 | 2.5 pts each = 20 |
| Aspirational (earlier) | C-14–C-22 | ~1.33 pts each = 20 |
| Aspirational (R7–R10) | C-23–C-32 | 5 pts each = 50 |
| **Max composite** | | **150** |

**Golden threshold**: All essential pass + composite >= 80

**Note on ceiling**: Rounds R7–R10 have added 50 aspirational points above the prior 100-point ceiling. The golden threshold remains composite >= 80 to preserve backward compatibility with earlier golden variants; the extended ceiling rewards accumulation of structural innovations without penalizing correct prior-round work.
