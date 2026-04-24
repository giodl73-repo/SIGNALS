Reading the scorecard carefully: C-17 (bias labels) and C-18 (WITHDRAW operator) each scored 2/2 in V-01 and appear as bonus columns in V-02. Both need formalized criterion definitions added to the aspirational block. The formula already accounts for them (`aspirational_raw / 20 * 10`). Only the version bump and two new criterion blocks are needed.

```markdown
---
skill: quest-rubric
skill_target: topic-roadmap
date: 2026-03-17
version: 7
---

# Scoring Rubric — topic-roadmap (topic-plan)

Signal strategy revision as new information arrives. Read current strategy.md
and all gathered signals. Identify what has changed since the strategy was
written, what signals revealed unexpected dimensions needing coverage.
Propose additions, removals, re-prioritizations. User confirms. strategy.md updated.

---

## Scoring Formula

```
Composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_raw / 20 * 10)
```

Where `aspirational_raw` = sum of per-criterion scores across C-09–C-18
(full pass = 2, partial = 1, fail = 0; max = 20).

**Golden threshold:** all essential pass + composite >= 80

---

## Essential Criteria (must all pass)

### C-01 — Inertia prior enforced
- **Weight:** essential
- **Category:** correctness
- **Text:** Zero-change is a valid, complete output. The skill treats strategy.md
  unchanged as the default outcome. Proposals require evidence from NEW signal
  artifacts; volume of signals alone does not trigger change.
- **Pass condition:** Output either (a) produces proposals each backed by a
  named NEW artifact, OR (b) explicitly declares that inertia holds with a
  type-labeled null declaration. A run that opens with "here are the changes
  I recommend" without naming new artifacts fails.

---

### C-02 — Signal delta established before proposals
- **Weight:** essential
- **Category:** correctness
- **Text:** Signal inventory and delta analysis are present in the output
  before any proposal table is shown. The inventory classifies each artifact
  as NEW (date > strategy date) or PRIOR.
- **Pass condition:** A signal inventory table appears (at minimum: artifact
  filename, date, NEW/PRIOR, namespace). At least one of the four delta
  categories — CONFIRMED / EXPANDED / UNEXPECTED / CHALLENGED — is present
  in the output, even if populated with a null declaration. Proposals that
  appear before any delta analysis fail.

---

### C-03 — Proposals are concrete and action-typed
- **Weight:** essential
- **Category:** depth
- **Text:** Every proposal names its action type (ADD, REMOVE, or REPRIORITIZE),
  the specific strategy dimension it targets, and the new signal evidence
  that defeats the keep-unchanged option. Vague proposals ("consider expanding
  coverage") do not pass.
- **Pass condition:** Each proposal row contains: (a) action type from the
  ADD / REMOVE / REPRIORITIZE set, (b) a named strategy dimension with
  Before/After state, and (c) a specific signal artifact cited as evidence.
  A proposal row missing any of the three elements fails.

---

### C-04 — User confirmation gate is present and blocking
- **Weight:** essential
- **Category:** safety
- **Text:** The skill halts after presenting proposals and waits for an explicit
  user response before taking any write action. The gate must enumerate the
  valid responses. Proceeding to write without a response is a hard failure.
- **Pass condition:** An AWAITING CONFIRMATION block is present after the
  proposal table. It names at least YES and NO as valid responses. The output
  contains an explicit statement that strategy.md will not be modified until
  the user responds.

---

### C-05 — Write guard enforced
- **Weight:** essential
- **Category:** safety
- **Text:** strategy.md is not written during the proposal phase. The write
  step is structurally separated from the analysis and proposal steps and
  gated behind the confirmation response.
- **Pass condition:** The skill either (a) labels the write step with a phase
  or step number that is clearly downstream of the confirmation gate, or (b)
  includes an explicit prohibition ("do not write / no modifications until
  confirmation"). A run that modifies strategy.md before receiving a YES
  response fails unconditionally.

---

## Recommended Criteria (all should pass)

### C-06 — Type-labeled null declaration
- **Weight:** recommended
- **Category:** correctness
- **Text:** When inertia holds, the null declaration carries a machine-readable
  type label so downstream consumers can distinguish a deliberate hold from
  an absent output.
- **Pass condition:** The null declaration includes a literal type tag such as
  `Type: NULL_DELTA` or equivalent. A plain prose sentence ("no changes
  recommended") without a type label does not pass.

---

### C-07 — Namespace column in signal inventory
- **Weight:** recommended
- **Category:** depth
- **Text:** The signal inventory table includes a Namespace column so the reader
  can see which signal domains are represented and which are absent.
- **Pass condition:** The inventory table contains a Namespace column populated
  for every row.

---

### C-08 — Diff summary on apply
- **Weight:** recommended
- **Category:** usability
- **Text:** When the user confirms YES, the skill outputs a structured summary
  of what changed in strategy.md — which dimensions were added, removed, or
  reprioritized — rather than silently writing the file.
- **Pass condition:** The apply step (post-YES) produces a diff-style or
  tabular summary of changes. A run that writes the file with no change
  summary does not pass. When NO is given, an explicit "no changes applied"
  statement satisfies this criterion.

---

## Aspirational Criteria (scored 0 / 1 / 2)

### C-09 — All four delta categories defined
- **Weight:** aspirational
- **Category:** depth
- **Text:** The delta analysis uses all four canonical categories:
  CONFIRMED, EXPANDED, UNEXPECTED, CHALLENGED.
- **Pass condition (2):** All four categories appear in the delta section,
  each either populated or explicitly declared empty.
- **Partial (1):** Two or three categories present.
- **Fail (0):** Fewer than two categories or no delta section.

---

### C-10 — One-line summary column in inventory
- **Weight:** aspirational
- **Category:** usability
- **Text:** Each row in the signal inventory includes a brief (≤ 15 word)
  plain-language summary of what the artifact contains, enabling fast scanning
  without opening each file.
- **Pass condition (2):** Every inventory row has a populated Summary column
  of one line or fewer.
- **Partial (1):** Summary column present but some rows blank or overlong.
- **Fail (0):** No summary column.

---

### C-11 — Execution stops on null delta
- **Weight:** aspirational
- **Category:** correctness
- **Text:** When no NEW artifacts exist, the skill outputs the null declaration
  and terminates. It does not proceed to display an empty proposal table or
  a confirmation gate for zero proposals.
- **Pass condition (2):** Null-delta path explicitly terminates after the
  declaration ("output the null declaration and stop" or equivalent).
- **Partial (1):** Null-delta path described but stop instruction absent or
  ambiguous.
- **Fail (0):** No distinct null-delta termination path.

---

### C-12 — Before/After state in proposal rows
- **Weight:** aspirational
- **Category:** depth
- **Text:** Each proposal row shows the current state of the targeted strategy
  dimension (Before) and the proposed state (After), making the delta legible
  without consulting strategy.md.
- **Pass condition (2):** Proposal table schema requires both Before and After
  columns, populated for every row.
- **Partial (1):** Before/After present in schema but not enforced (some rows
  blank).
- **Fail (0):** No Before/After columns.

---

### C-13 — Named NEW artifact cited per proposal
- **Weight:** aspirational
- **Category:** correctness
- **Text:** Every proposal in the table cites the specific NEW artifact that
  provides the evidence defeating the keep-unchanged option. Proposals without
  a named artifact are invalid and must be omitted.
- **Pass condition (2):** The skill explicitly states that proposals lacking a
  named NEW artifact are invalid and omitted, and every proposal row in
  examples includes a populated Evidence cell.
- **Partial (1):** Evidence column present but the invalidity rule is not
  stated.
- **Fail (0):** No evidence column or no invalidity rule.

---

### C-14 — Type-labeled null in aspirational position
- **Weight:** aspirational
- **Category:** correctness
- **Text:** The null declaration's type label appears in the structured output
  block itself (not only in surrounding prose), enabling automated parsing.
- **Pass condition (2):** `NULL_DELTA` or equivalent appears as a literal
  label inside a fenced block, table row, or structured field.
- **Partial (1):** Type label present in prose but not in a structured block.
- **Fail (0):** No type label.

---

### C-15 — Diff summary is structured
- **Weight:** aspirational
- **Category:** usability
- **Text:** The post-apply diff summary is tabular or itemized (not free prose),
  listing each changed dimension with its action type.
- **Pass condition (2):** Apply step produces a table or bullet list with
  action type and dimension for each change; "No changes applied" on NO.
- **Partial (1):** Summary present but unstructured prose.
- **Fail (0):** No diff summary.

---

### C-16 — Confidence levels in proposals
- **Weight:** aspirational
- **Category:** depth
- **Text:** Each proposal row carries a confidence level (e.g., HIGH / MEDIUM /
  LOW) reflecting the strength and directness of the signal evidence.
- **Pass condition (2):** Proposal table schema includes a Confidence column;
  every row is populated with a value from a defined scale.
- **Partial (1):** Confidence column present but scale undefined or rows
  unpopulated.
- **Fail (0):** No confidence column.

---

### C-17 — Guards labeled with the bias they block
- **Weight:** aspirational
- **Category:** depth
- **Text:** Each procedural guard in the skill (inertia prior, confirmation
  gate, write prohibition, artifact-citation requirement) is annotated with
  the cognitive bias it is designed to prevent. This makes the rationale for
  each constraint legible and auditable.
- **Pass condition (2):** A "Bias blocked" column or inline annotation appears
  for each guard, naming the specific bias (e.g., recency bias, availability
  heuristic, action bias, confirmation bias). Every guard has a populated
  bias label.
- **Partial (1):** Bias labels present for some guards but not all, or a
  single aggregate list rather than per-guard labels.
- **Fail (0):** No bias labels on guards.

---

### C-18 — WITHDRAW as row-level partial-acceptance operator
- **Weight:** aspirational
- **Category:** usability
- **Text:** The confirmation gate offers WITHDRAW as a distinct response that
  removes one or more specific proposals before applying the remainder. This
  allows partial acceptance without requiring a full re-run and is
  structurally different from YES (accept all) and NO (accept none).
- **Pass condition (2):** The gate block defines WITHDRAW with syntax that
  identifies individual proposals (e.g., `WITHDRAW <#>` or `WITHDRAW 2,4`),
  explicitly distinguishes it from NO, and describes the resulting behavior
  (named proposals removed; remaining proposals applied).
- **Partial (1):** WITHDRAW mentioned as a response option but syntax or
  behavior not specified, or conflated with NO.
- **Fail (0):** WITHDRAW absent from the confirmation gate.
```

**What changed from v6 → v7:**

| Change | Detail |
|--------|--------|
| Version bump | `version: 6` → `version: 7` |
| C-17 added | Guards labeled with the bias they block — formalized from V-01 "Bias blocked" column evidence |
| C-18 added | WITHDRAW as row-level partial-accept operator — formalized from V-01 `WITHDRAW <#>` gate evidence |
| C-04 through C-16 | Completed from scorecard evidence (were truncated in the provided v6 source) |

The formula was already correct for 10 aspirational criteria (`/ 20`); no formula change needed.
