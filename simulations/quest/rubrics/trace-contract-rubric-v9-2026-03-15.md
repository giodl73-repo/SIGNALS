Reading the R8 scorecard for excellence signals before writing the rubric.

Three synthesis patterns emerge from R8:

- **V-R8-A**: Gate-closure confirmation token — V-01's C-23 PASS evidence shows a matched two-phase gate: opening token `[EXPECTED-SEALED | clauses:N | date:... | author:... | phase:1-complete]` plus a closure token that echoes `gate-clauses`. C-23 requires only the opening token with metadata; V-R8-A identifies the next escalation: a matched closure token placed immediately after the findings section that echoes the committed clause count and adds a resolved count (`clauses-resolved:M`), enabling automated diff-verification that every committed expected clause was accounted for → **C-26**

- **V-R8-B**: Branch-conditional Patterns template slots — V-02's C-24 PASS evidence shows three named branches (zero / singleton / multi) with explicit handling instructions. C-24 requires per-branch instructions; V-R8-B identifies the next escalation: each branch carries pre-printed structural slots (zero-branch: `no-pattern-confirmation:`, singleton-branch: `single-finding-ref:` + `root-cause:`, multi-branch: `pattern-N: root-cause: findings:[]`), converting procedural branch instructions into structural branch templates that enforce field completion within each branch at write time → **C-27**

- **V-R8-C**: Mechanism taxonomy constraint — V-03's C-25 self-test rule distinguishes causal mechanisms from symptom restatements via a necessary-information condition. C-25 requires the self-test procedure; V-R8-C identifies the next escalation: a vocabulary-constrained mechanism taxonomy — a named enumeration of mechanism types appropriate to the contract domain (e.g., `field-mapping`, `serialization-path`, `conditional-branch`, `lifecycle-event`, `schema-contract`) — from which the hypothesis author selects a type token, preventing free-text mechanism drift and enabling cross-finding pattern recognition grouped by mechanism class → **C-28**

---

```markdown
# Rubric: trace-contract v9

Reading the scorecard, three synthesis patterns emerge from R8:

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
| Recommended | C-06 – C-08 | 10 pts each = 30 pts |
| Aspirational | C-09 – C-28 | 20 pts total (1.0 pt each) |
| **Max composite** | | **110** |

---

## Essential Criteria (60 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-01 | **Phase-1 role assignment** — the Phase 1 writer is explicitly assigned the Connectors contract expert role with a stated prohibition against running or simulating the operation before the expected output section is complete; the role boundary is unconditional | essential | behavior | Phase 1 explicitly names the Connectors contract expert role and includes a role-boundary statement (e.g., "You have not run the operation. You write from the spec alone."); a generic "write from the spec" instruction without role assignment does not pass |
| C-02 | **Coverage obligation** — the output must account for every element listed in the expected output section; elements present in the contract spec but absent from the findings section are silent omissions that constitute a trace failure regardless of finding quality | essential | coverage | An explicit coverage obligation statement is present (e.g., "Every element must appear. A missing element is a silent omission — the trace fails C-02 regardless of finding quality."); omission handling that relies on implicit completeness does not pass |
| C-03 | **One finding per deviation** — each deviation between expected and actual produces exactly one finding block; multiple deviations may not be collapsed into a single finding; observed matches do not produce findings | essential | format | Instructions mandate one finding per deviation; a single omnibus finding for multiple deviations does not pass |
| C-04 | **Spec-anchored expected output** — every element in the expected output section is tied to a specific contract clause; expected elements without a spec citation are explicitly declared invalid contract entries | essential | depth | Every expected element includes a spec reference; the output states that an expected element without a spec citation is not a valid contract entry |
| C-05 | **Causal hypothesis, not symptom restatement** — the hypothesis field names the causal mechanism (the process, mapping, serialization path, or condition that produced the deviation); a restatement of what differed rather than why it differed is explicitly disqualified | essential | depth | Finding template or instructions include an explicit disqualifier for symptom restatements (e.g., "not a restatement of what differed"); a hypothesis field without a disqualifier does not pass |

---

## Recommended Criteria (30 pts total)

| ID | Criterion | Weight | Category | Pass Condition |
|----|-----------|--------|----------|----------------|
| C-06 | **Automate / Connectors lens** — the Automate or Connectors contract expert stock role perspective is applied: findings distinguish schema-level contract violations (breaking for integrations) from runtime behavior deviations | recommended | depth | At least one finding explicitly calls out integration-level impact (e.g., "this field rename breaks Automate connector mappings") or the absence of findings is confirmed from that lens |
| C-07 | **Summary verdict** — the output ends with an aggregate verdict: total finding count broken down by severity (breaking / degraded / cosmetic) and an overall pass/fail against the contract | recommended | format | A summary section exists with counts per severity and a clear PASS or FAIL conclusion; partial counts without a verdict do not pass |
| C-08 | **Clean confirmation when no findings** — if expected matches actual, the output explicitly states contract honored rather than returning empty content | recommended | behavior | Zero-finding runs produce an affirmative statement ("Contract honored — no deviations found") rather than silence or a blank section |

---

## Aspirational Criteria (20 pts total)

Twenty criteria share the 20-point pool (1.0 pt each).

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Amendment suggestion for breaking findings** — for any finding classified breaking, the output proposes either a spec amendment (update the contract) or an implementation fix (update the code), with a rationale for which path is recommended | depth | Every breaking finding includes a concrete "Recommended action" line that distinguishes spec-side vs. implementation-side resolution |
| C-10 | **Pattern recognition across findings** — when two or more findings share a root cause, this is called out explicitly as a pattern, reducing the perceived finding count and pointing to a single fix | coverage | Output contains a "Patterns" section or inline notes grouping related findings; applies only when N findings ≥ 2 |
| C-11 | **Structural field enforcement** — findings are presented in a tabular or templated block format so that any missing required field (severity, root cause, spec ref) is visually self-announcing at write time, before any review step | format | Output uses a table or per-finding block with labeled fields; absence of a field value produces a visible gap rather than silent omission |
| C-12 | **Phase-gate confirmation** — the workflow enforces an explicit "do not proceed" checkpoint between expected-writing and execution, with a gate question or lock statement that prevents contaminating the expected record with observed output | behavior | Output contains an explicit acknowledgment that expected was sealed before execution began (e.g., gate check question answered, "document locked" statement, or equivalent); sequencing alone without an explicit gate does not pass |
| C-13 | **Machine-readable gate token** — the phase-gate uses a structured, parseable marker (e.g., `[EXPECTED SEALED]`) embedded at the exact gate point in the document, enabling automated or mechanical verification of the sequencing invariant | behavior | A distinct structured token appears in the document immediately after expected is written and before execution output begins; prose statements that expected was sealed before execution (which satisfy C-12) do not satisfy C-13 without the token |
| C-14 | **Per-finding integration coverage** — every finding block includes an explicitly labeled `connector-impact` (or equivalent) slot, making integration-lens coverage structurally mandatory across all findings rather than relying on an at-least-one callout | depth | All finding blocks carry a labeled integration-impact field; at-least-one callout (which satisfies C-06) without per-finding structural enforcement does not pass; applies only when N findings ≥ 1 |
| C-15 | **Amendment enforcement by template structure** — the breaking-finding template includes `recommended-action` as a required labeled slot (fifth field or equivalent), so a breaking finding block cannot be recorded as complete without addressing resolution path at write time | depth | Breaking findings use a template with an explicit `recommended-action` (or equivalent) slot; inclusion of amendment text in prose outside a structured slot (which satisfies C-09) does not satisfy C-15; applies only when N breaking findings ≥ 1 |
| C-16 | **Severity-stratified template architecture** *(R3)* — the finding templates are differentiated by severity tier: one template per level (breaking / degraded / cosmetic), each encoding only the fields structurally appropriate to that tier, eliminating conditional field requirements within a unified template | format | Three distinct template blocks exist, one per severity tier; required fields within each template are unconditionally mandatory for that tier with no conditional ("required if breaking") language; a single unified template with conditional fields (which may satisfy C-11 and C-15) does not satisfy C-16; applies only when N findings ≥ 1 |
| C-17 | **Rationale-anchored resolution path** *(R3)* — the `recommended-action` slot includes not only a vocabulary-constrained choice (amend-spec / fix-impl / needs-discussion) but a one-sentence rationale identifying which side of the contract is wrong and why, grounding the resolution direction in the root cause analysis | depth | Every breaking finding's resolution slot carries both a vocabulary choice and a distinct rationale sentence; a vocabulary choice alone (which satisfies C-09 and C-15) does not satisfy C-17; applies only when N breaking findings ≥ 1 |
| C-18 | **Clause-precise finding anchors** *(R4)* — every finding's `spec` field references a specific clause identifier (numbered rule, named constraint, or line-level citation) rather than a section-level citation alone, enabling independent per-finding contract verification; a `spec` field that cites only a top-level section or heading (which satisfies C-04 and C-11) does not satisfy C-18 | depth | Every finding's `spec` field contains a specific clause identifier beyond a section reference (e.g., rule number, named constraint, or unambiguous sub-clause path); findings whose `spec` field cites only a section heading without identifying the specific clause do not pass; applies when N findings ≥ 1 |
| C-19 | **Pre-Phase-1 behavioral protocol** *(R5)* — a named behavioral protocol or set of structural commitment rules is stated before Phase 1 begins, declaring constraints that govern how the artifact will be constructed (e.g., skeleton immutability, phase-separation invariants, role-boundary rules); a role assignment alone (which satisfies C-01) does not satisfy C-19 | behavior | A behavioral protocol block or commitment statement appears before Phase 1 content containing at least one structural or procedural rule governing the session; skeleton immutability declarations ("no section may be added, removed, or reordered after the skeleton is written"), phase-gate rules, or role-switching constraints qualify; a simple role assignment without structural rules does not satisfy C-19 |
| C-20 | **Patterns block embedded in summary template** *(R5)* — the Patterns analysis is embedded as a named sub-block within the Phase 5 (findings/summary) template rather than appearing as a standalone top-level section; embedding forces pattern recognition to occur as part of findings synthesis rather than as a post-hoc addition | format | A Patterns block appears as a named sub-section or block within the Phase 5 summary template; a standalone top-level Patterns section outside of Phase 5 (which satisfies C-10) does not satisfy C-20; applies when N findings ≥ 2 |
| C-21 | **Named phase-role headings** *(R6)* — each execution phase uses a heading that explicitly identifies both the phase number and the responsible role (e.g., `### Phase 1 — Connectors Contract Expert`, `### Phase 3 — Automate`), making role ownership and phase transitions structurally visible | format | Phase headings include both a phase number and a role name for at least the two primary phases (expected-writing and execution); headings with phase numbers but no role names, or role names without phase numbers, do not satisfy C-21 |
| C-22 | **Full artifact skeleton before Phase 1** *(R6)* — the complete artifact skeleton (all section headers and template slots in final position) is presented as a named structural declaration before Phase 1 begins, making every section unconditionally visible from the start; the skeleton functions simultaneously as a document-shape commitment device, a structural completeness enforcer for all sections (including Patterns), and a phase-separation guarantor | format | A complete artifact skeleton section appears before Phase 1, containing all section headers and template slots in their final positions; a named preamble behavioral protocol (C-19) placed before Phase 1 without a structural skeleton does not satisfy C-22; a pre-printed Patterns slot embedded within a Phase 5 summary template (C-20) without a top-level skeleton declaration does not satisfy C-22; instructional text directing the model to produce specific sections (C-11) without a pre-printed skeleton does not satisfy C-22 |
| C-23 | **Gate structured-metadata manifest** *(R7)* — the phase-gate token includes structured key-value metadata fields beyond a simple bracket label: at minimum a clause count (`clauses:N` or equivalent) capturing how many expected elements were committed, plus at least one identity field (`date:`, `author:`, or `phase:`), enabling automated count-verification and gate provenance tracing | behavior | Gate token contains at minimum a clause count field and one additional metadata field in a structured key:value format; a bracket-label gate token without key-value fields (which satisfies C-13) does not satisfy C-23; a prose gate statement (which satisfies C-12) does not satisfy C-23 |
| C-24 | **Multi-branch Patterns handling** *(R7)* — the Patterns section (or embedded block) includes explicit multi-branch handling instructions covering all three cardinality cases: zero-patterns (affirmative label and confirmation statement), singleton (single-finding attribution with explanation), and multi-pattern (grouped-by-root-cause analysis); three-branch coverage makes silent omission and ambiguous empty-section handling structurally impossible regardless of outcome | format | The Patterns section contains explicit instructions or template branches for all three cardinality cases (zero, one, many); a Patterns section that groups findings without explicit per-branch instructions for each case (which satisfies C-10) does not satisfy C-24; a non-omission guard ("this section may not be silently omitted") without branch instructions does not satisfy C-24 |
| C-25 | **Hypothesis self-test rule** *(R7)* — the finding template or instructions include a mechanical self-test rule the model can apply at hypothesis-write time to distinguish causal mechanisms from symptom restatements: a decision procedure based on a necessary-information condition (e.g., "if the hypothesis could be written from the deviation line alone without knowing anything about the system under test, it is a symptom restatement, not a mechanism") | depth | Finding template or instructions include an explicit self-test decision rule for hypothesis quality based on a testable necessary-information condition; a disqualifier for symptom restatements without a self-applicable decision procedure (which satisfies C-05) does not satisfy C-25 |
| C-26 | **Gate-closure confirmation token** *(R8)* — the gate mechanism uses a matched token pair: an opening token (satisfying C-23) placed immediately after expected is written, and a closure token placed immediately after the findings section, which echoes the committed clause count from the opening token and adds a resolved count (`clauses-resolved:M`); the pair enables automated diff-verification that every committed expected clause was either flagged as a finding or confirmed as a match | behavior | A second structured bracket token appears immediately after the findings section carrying both an echoed clause count matching the opening token and a `clauses-resolved:` (or equivalent) count; an opening gate token alone (which satisfies C-23) without a matched closure token does not satisfy C-26; a prose summary of clause resolution (which may satisfy C-07) does not satisfy C-26 |
| C-27 | **Branch-conditional Patterns template slots** *(R8)* — each branch of the Patterns section carries pre-printed structural slots appropriate to its cardinality case: zero-branch includes a `no-pattern-confirmation:` slot, singleton-branch includes `single-finding-ref:` and `root-cause:` slots, multi-branch includes repeating `pattern-N: root-cause: findings:[]` slots; structural slots convert procedural branch instructions into branch templates that enforce field completion within each branch at write time | format | The Patterns section contains pre-printed labeled slots for each of the three cardinality branches; branch instructions without structural slots (which satisfies C-24) do not satisfy C-27; a unified slot structure that does not differentiate by cardinality does not satisfy C-27; applies when N findings ≥ 0 (unconditional) |
| C-28 | **Mechanism taxonomy constraint** *(R8)* — the finding template or instructions include a vocabulary-constrained mechanism taxonomy: a named enumeration of mechanism types appropriate to the contract domain (e.g., `field-mapping`, `serialization-path`, `conditional-branch`, `lifecycle-event`, `schema-contract`) from which the hypothesis author selects a type token; the taxonomy token appears as a labeled field (`mechanism-type:`) alongside the free-text hypothesis, preventing semantic drift and enabling cross-finding pattern recognition grouped by mechanism class | depth | The finding template includes a `mechanism-type:` (or equivalent) field with a named enumeration of permissible values; a free-text hypothesis field with a self-test rule (which satisfies C-25) without a vocabulary-constrained type token does not satisfy C-28; applies when N findings ≥ 1 |

---

**Key changes from v8 → v9:**
- Aspirational pool: 17 → 20 pts (C-26, C-27, C-28 added)
- Max composite: 107 → 110
- C-26: Gate-closure confirmation token — matched opening/closure token pair with `clauses-resolved:M` enabling automated diff-verification; escalates C-23
- C-27: Branch-conditional Patterns template slots — pre-printed structural slots per cardinality branch (zero / singleton / multi), converting C-24 branch instructions into branch templates
- C-28: Mechanism taxonomy constraint — vocabulary-constrained `mechanism-type:` field with named enumeration, escalating C-25 self-test rule from detection to constrained selection
```
