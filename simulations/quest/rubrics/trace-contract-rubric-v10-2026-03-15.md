```markdown
# Rubric: trace-contract v10

Reading the scorecard, two synthesis patterns emerge from R9:

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
A **golden** output scores ≥ 80 and passes all essential criteria.

---

## Scoring Summary

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01 – C-05 | 12 pts each = 60 pts |
| Recommended | C-06 – C-12 | 30 pts |
| Aspirational | C-13 – C-30 | 22 pts max |
| **Total** | | **112 pts max** |

---

## Criteria

### Essential — 12 pts each

| ID | Criterion |
|----|-----------|
| C-01 | Role assignment and boundary statement present |
| C-02 | Coverage obligation explicitly stated |
| C-03 | One-finding-per-deviation rule enforced with three severity-tier templates (BREAKING / DEGRADED / COSMETIC) |
| C-04 | Spec-anchored expected output; "invalid without citation" constraint declared |
| C-05 | Causal mechanism requirement stated with self-test: "if your hypothesis could be written without knowing anything about the system under test — only from reading the deviation line — it is a symptom restatement, not a mechanism" |

### Recommended — 30 pts

| ID | Criterion |
|----|-----------|
| C-06 | `connector-impact:` field on BREAKING and DEGRADED tier finding templates |
| C-07 | Summary section with severity count table, verdict, and coverage line |
| C-08 | Zero-finding affirmation: "If no deviations: write `## Diff -- Contract satisfied. No findings.` and skip to Step 6." |
| C-09 | `recommendation:` labeled slot present on BREAKING tier template |
| C-10 | §7 Patterns section present; groups findings by recurrence category |
| C-11 | Per-finding block uses consistently labeled fields throughout |
| C-12 | Phase-lock instruction: "Do not run or simulate the operation before writing this token." |

### Aspirational — 1–2 pts each; 22 pts max

| ID | Criterion |
|----|-----------|
| C-13 | Gate bracket token — distinct `[EXPECTED-SEALED]` or equivalent opening token placed before analysis begins, preventing post-hoc hypothesis insertion |
| C-14 | `connector-impact:` field present on COSMETIC tier template (completing tier stratification across all three severity tiers) |
| C-15 | `recommendation:` slot present as explicitly labeled field on BREAKING (not inlined or implied) |
| C-16 | COSMETIC tier includes integration-impact field — all three tiers carry consistent structural slots |
| C-17 | `rationale:` one-sentence field alongside `recommendation:` on BREAKING tier |
| C-18 | `spec:` field references specific clause from Expected Output — rule number, named constraint, or sub-clause path; not a paraphrase |
| C-19 | Behavioral protocol block present: explicit phase-ordered instructions governing execution sequence |
| C-20 | Patterns section is a standalone top-level section positioned outside Phase 5 (not embedded as sub-block within the findings phase) |
| C-21 | Named phase-role headings in skeleton structure (each phase identified by role, not just sequence number) |
| C-22 | Full skeleton pre-declared with all section headers before analysis begins |
| C-23 | Gate structured-metadata manifest: `[EXPECTED-SEALED | clauses:N | date:... | author:... | phase:1-complete]` — clause count plus at least one identity field |
| C-24 | Three named branch templates in Patterns section (Zero / Singleton / Multi-pattern) with per-branch handling instructions; "This section may not be silently omitted." |
| C-25 | Hypothesis self-test decision rule embedded in finding template as an in-line procedure the model can invoke at write time without external judgment |
| C-26 | Gate-closure confirmation token: `[FINDINGS-RESOLVED | gate-clauses:{N} | clauses-resolved:{M} | phase:5-complete]` placed immediately after last finding block, before Summary; echoes opening clause count and adds resolved count; includes `CLAUSE-GAP` divergence path for mismatches |
| C-27 | Branch-conditional Patterns template slots — structural pre-printed fields per branch: zero-branch (`no-pattern-confirmation:`), singleton-branch (`single-finding-ref:`, `root-cause:`, `attribution:`, `single-fix:`), multi-branch (`pattern-N: root-cause: findings:[] single-fix:`, `patterns-summary:`) |
| C-28 | Mechanism taxonomy type token — `mechanism-type:` field in finding template with vocabulary-constrained enumeration (e.g., `field-mapping`, `serialization-path`, `conditional-branch`, `lifecycle-event`, `schema-contract`) |
| C-29 | `mechanism-type-shared:` field in Singleton and Multi-pattern Patterns branch templates — propagates mechanism taxonomy into synthesis layer; same-class value (e.g., `mechanism-type-shared: field-mapping`) signals systemic root cause requiring one fix; `mixed` signals coincident symptoms requiring independent fixes |
| C-30 | Taxonomy distribution line in Summary: `mechanism-distribution: <type>:<count> ...` aggregates per-finding `mechanism-type:` tokens into a document-level class distribution, enabling cross-session failure-class trending by mechanism type |
```
