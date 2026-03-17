## Corps-PR R12 — Five Variations

---

## V-01 — Lifecycle Emphasis Axis

**Hypothesis**: Making the Phase C exit condition checklist the structural anchor for C-36 and C-37 — rather than burying the ordering rule in prose — produces reliable compliance because reviewers must verify both conditions as named items before advancing.

---

```markdown
## /corps-pr — Full-Org PR Review

Read the PR diff and `org.yaml`. Execute the four-phase pipeline below in order.
Do not produce output for a later phase until all exit conditions for the prior phase are met.

---

### Phase A — Reviewer Selection

Scan all changed files. For each file or file group, identify the org.yaml role whose
scope covers it. Output:

```
REVIEWER SELECTION
─────────────────────────────────────────────
Changed files:
  [list every changed file]

Role mapping:
  [file or file group] → [role] — [scope match reason]
  ...
─────────────────────────────────────────────
```

Rules:
- Every selected role must trace to at least one specific changed file.
- A role that cannot be traced is not selected.
- If an AMEND directive names an additional reviewer, add them with reason: "AMEND-specified."

Phase A exit: every selected role has a file mapping with a stated reason.

---

### Phase B — Per-Role Review

Run each selected role through sub-phases B1 → B2 → B3 → B4 in sequence.
Do not begin B2 until B1 is complete. Do not begin B3 until B2 is complete.

**B1 — PRE-COMMITMENT**

Before accessing any IA document, the reviewer commits an initial position:

```
PRE-COMMITMENT — [Role Name]
Position: ACCEPT | CHALLENGE | NEUTRAL
Basis: [one sentence — what in this role's domain informs this position]
```

**B2 — IA READ RECEIPT**

Access the IA document. Record receipt evidence for all five fields:

```
READ RECEIPT — [Role Name]
(a) IA reference:         [document ID or section heading]
(b) Cost framing:         [verbatim or close paraphrase of IA's cost claim]
(c) Evidence basis:       [what the IA cites as supporting evidence]
(d) Recommended action:   [what the IA recommends]
(e) Confidence qualifier: [how the IA qualifies its own confidence]
```

The READ RECEIPT block must appear in the output before the C2 RESULT block.
This is the Phase C ordering compliance requirement (C-35). It must be enforced here
so the Phase C exit condition can verify it.

**B3 — C2 RESULT**

After the READ RECEIPT, produce the C2 RESULT. Enumerate every receipt field
by its label with a present/absent verdict:

```
C2 RESULT — [Role Name]
(a) IA reference:         PRESENT | ABSENT
(b) Cost framing:         PRESENT | ABSENT
(c) Evidence basis:       PRESENT | ABSENT
(d) Recommended action:   PRESENT | ABSENT
(e) Confidence qualifier: PRESENT | ABSENT
─────────────────────────
VERDICT: SATISFIED [all five PRESENT] | UNSATISFIED [any ABSENT]
```

A C2 RESULT that states only a summary verdict without enumerating (a)–(e) is invalid.

**B4 — Findings**

Produce one findings section per role. Each finding carries a severity label:
P1 (blocking) | P2 (major) | P3 (minor).

For findings of type IA-RESPONSE, use the F-01 template. The Description field must
name both components as separately-labeled slots:

```
[F-01] IA-RESPONSE — [Role Name]
Severity: P1 | P2 | P3
Description: [IA-VERDICT: {reviewer's verdict on the IA's cost claim}]
           | [ROLE-MECHANISM: {specific mechanism owned by this role's domain}]
Evidence: [what in the diff or IA supports this finding]
```

Apply the domain-lens gate to every finding before including it:
1. Binary test: Would ONLY this role raise this finding given their domain scope?
2. If NO: Revise to name a specific mechanism owned by this role's domain.
3. If still NO after revision: Drop the finding.

A finding that names a mechanism any generic reviewer could raise fails the gate.

Phase B exit: all selected roles have completed B1–B4.

---

### Phase C — Consensus Analysis

Synthesize across all role findings. Produce a dedicated CONSENSUS ANALYSIS section.

The section must include:
- Agreement: findings where two or more roles converge — name the finding and the roles.
- Disagreement: findings where roles conflict — name the finding and characterize the tension.
- Most critical: the single highest-severity finding across all roles — name it, name its
  severity, name the role that raised it.

**Phase C Exit Conditions** — verify all before proceeding to Phase D:

☐ Every selected role has a findings section in the output.
☐ PRE-COMMITMENT appears before READ RECEIPT for every role.
☐ READ RECEIPT appears before C2 RESULT for every role.
    [C-35 ORDERING — this is a Phase C compliance item: the output sequence
     PRE-COMMITMENT → READ RECEIPT → C2 RESULT must be verifiable by inspection.]
☐ C2 RESULT for every role enumerates fields (a)–(e) with a present/absent verdict per field.
☐ Every F-01 IA-RESPONSE Description uses named slots [IA-VERDICT] and [ROLE-MECHANISM].
☐ Consensus analysis contains agreement, disagreement, and most-critical sections.

Do not produce Phase D output until all six exit conditions are checked.

---

### Phase D — Go/No-Go Recommendation

State exactly one: **GO** | **NO-GO** | **GO WITH CONDITIONS**

Justify by citing:
- The primary reason (name the specific finding)
- The role that raised it
- Its severity (P1 / P2 / P3)

A recommendation without justification is not acceptable.
An ambiguous recommendation ("the team should decide") is not acceptable.
```

---

## V-02 — Output Format Axis

**Hypothesis**: Providing a mandatory table template for the C2 RESULT block — with rows pre-labeled (a)–(e) and a PRESENT/ABSENT column — eliminates the ambiguity that allows a compliant-in-prose C2 block to omit per-field evidence. The table makes C-37 structurally impossible to accidentally satisfy with a summary verdict.

---

```markdown
## /corps-pr — Full-Org PR Review

Read the PR diff and `org.yaml`. Produce output in the template structure below.
Every block that shows a template must be filled exactly — no substitutions, no collapses.

---

### Block 1: REVIEWER SELECTION

| Changed File / File Group | Org.yaml Role | Selection Reason |
|---------------------------|--------------|-----------------|
| [file]                    | [role]       | [scope match]   |
| ...                       | ...          | ...             |

Rules: Every row must have a non-empty selection reason. A role without a mapped file is
not selected. AMEND-specified reviewers get reason: "AMEND-specified."

---

### Block 2: PER-ROLE REVIEW

Repeat the following sub-block template for every selected role.

#### [Role Name]

**PRE-COMMITMENT**

| Field   | Value |
|---------|-------|
| Role    | [role name] |
| Position| ACCEPT \| CHALLENGE \| NEUTRAL |
| Basis   | [one sentence — domain basis for this position] |

*Produce PRE-COMMITMENT before accessing the IA document.*

---

**IA READ RECEIPT**

| Field | Receipt Value |
|-------|--------------|
| (a) IA reference | [document ID or section heading] |
| (b) Cost framing | [verbatim or close paraphrase of IA's cost claim] |
| (c) Evidence basis | [what the IA cites as supporting evidence] |
| (d) Recommended action | [what the IA recommends] |
| (e) Confidence qualifier | [how the IA qualifies its own confidence] |

*The READ RECEIPT table must appear before the C2 RESULT table in the output.*

---

**C2 RESULT**

| Receipt Field | Verdict |
|--------------|---------|
| (a) IA reference | PRESENT \| ABSENT |
| (b) Cost framing | PRESENT \| ABSENT |
| (c) Evidence basis | PRESENT \| ABSENT |
| (d) Recommended action | PRESENT \| ABSENT |
| (e) Confidence qualifier | PRESENT \| ABSENT |
| **Overall** | **SATISFIED** (all PRESENT) \| **UNSATISFIED** (any ABSENT) |

*Do not collapse the five rows into a summary verdict. All five rows are required.*

---

**FINDINGS**

| ID | Type | Severity | Description | Evidence |
|----|------|----------|-------------|---------|
| F-NN | [type] | P1 \| P2 \| P3 | [description] | [evidence] |

For findings of type IA-RESPONSE (F-01), the Description cell must use the slot template:

```
[IA-VERDICT: {verdict on IA's cost claim}] | [ROLE-MECHANISM: {mechanism in this role's domain}]
```

Both slots are required. A Description that contains both components but does not label
them as [IA-VERDICT: ...] and [ROLE-MECHANISM: ...] is non-compliant.

Domain-lens gate (apply before adding any row):
1. Binary test: Would ONLY this role raise this finding given their domain?
2. If NO → revise Description to name a mechanism owned by this role's domain.
3. If still NO after revision → remove the row.

---

### Block 3: CONSENSUS ANALYSIS

| Category | Finding | Roles |
|----------|---------|-------|
| Agreement | [finding description] | [role A, role B] |
| Disagreement | [finding description] | [role A disagrees with role B because: ...] |
| Most Critical | [finding description] | [role], Severity: P1 \| P2 \| P3 |

At least one row per category is required. A consensus section that only restates
per-role findings without cross-role analysis fails.

**Pre-output compliance check** (verify before Block 4):
- READ RECEIPT table precedes C2 RESULT table for every role (C-35 ordering).
- C2 RESULT table has all five (a)–(e) rows filled with PRESENT/ABSENT (not a summary).
- Every F-01 Description cell uses [IA-VERDICT: ...] | [ROLE-MECHANISM: ...] slot syntax.

---

### Block 4: GO/NO-GO RECOMMENDATION

| Decision | Primary Finding | Role | Severity |
|----------|----------------|------|----------|
| GO \| NO-GO \| GO WITH CONDITIONS | [finding] | [role] | P1 \| P2 \| P3 |

Conditions (if GO WITH CONDITIONS): list each condition as a bullet with a resolution owner.
```

---

## V-03 — Phrasing Register Axis

**Hypothesis**: Expressing C-36, C-37, and C-38 compliance requirements in strict imperative register — using MUST, INVALID, and FAIL as hard-stop keywords rather than guidance — converts structural requirements into self-auditing rules. A reviewer executing the prompt treats a MUST as a blocker, not a suggestion.

---

```markdown
## /corps-pr — Full-Org PR Review

**Input**: PR diff + `org.yaml`. Execute the pipeline below.
**Register**: Every rule marked MUST is a hard requirement. Output that violates a MUST
is INVALID. Do not proceed to the next section if a MUST is unmet.

---

### SECTION 1 — REVIEWER SELECTION

MUST: Map every changed file to an org.yaml role with an explicit scope-match reason.
MUST: A role appears in the output ONLY IF it traces to at least one specific changed file.
MUST: If an AMEND directive names a reviewer, include them with reason "AMEND-specified."
FAIL condition: A role appears in the output with no file mapping → INVALID, remove the role.

Output format:
```
REVIEWER SELECTION
  [file or file group] → [role] — [reason]
  ...
```

---

### SECTION 2 — PER-ROLE REVIEW

For every selected role, produce sub-sections 2a through 2d in order.
MUST: Do not begin 2b until 2a is complete. Do not begin 2c until 2b is complete.

**2a — PRE-COMMITMENT**

MUST: Produce PRE-COMMITMENT before the reviewer accesses any IA document.
MUST: State a position (ACCEPT / CHALLENGE / NEUTRAL) and a one-sentence domain basis.

```
PRE-COMMITMENT — [Role]
Position: ACCEPT | CHALLENGE | NEUTRAL
Basis: [domain basis]
```

FAIL condition: PRE-COMMITMENT is missing or appears after READ RECEIPT → INVALID.

---

**2b — READ RECEIPT**

MUST: Produce READ RECEIPT immediately after accessing the IA document.
MUST: Include all five fields by label. A READ RECEIPT with fewer than five labeled
fields is INVALID — it does not satisfy the receipt requirement.

```
READ RECEIPT — [Role]
(a) IA reference:         [document ID or section heading]
(b) Cost framing:         [verbatim or close paraphrase of IA's cost claim]
(c) Evidence basis:       [what the IA cites as supporting evidence]
(d) Recommended action:   [what the IA recommends]
(e) Confidence qualifier: [how the IA qualifies its own confidence]
```

MUST: READ RECEIPT MUST appear before C2 RESULT in the output.
This ordering is not a style preference — it is a structural compliance requirement.
FAIL condition: C2 RESULT appears before READ RECEIPT in the output → INVALID for this role.

---

**2c — C2 RESULT**

MUST: C2 RESULT appears after READ RECEIPT in the output.
MUST: C2 RESULT enumerates all five receipt fields by their (a)–(e) labels with a
PRESENT or ABSENT verdict per field. A C2 RESULT that states only a summary verdict
without per-field verdicts is INVALID — it does not satisfy the C2 requirement.
MUST: Add an overall VERDICT: SATISFIED (all PRESENT) or UNSATISFIED (any ABSENT).

```
C2 RESULT — [Role]
(a) IA reference:         PRESENT | ABSENT
(b) Cost framing:         PRESENT | ABSENT
(c) Evidence basis:       PRESENT | ABSENT
(d) Recommended action:   PRESENT | ABSENT
(e) Confidence qualifier: PRESENT | ABSENT
VERDICT: SATISFIED | UNSATISFIED
```

FAIL condition: Any of (a)–(e) is missing → INVALID.
FAIL condition: Only a summary verdict appears (e.g., "C2 RESULT: SATISFIED") → INVALID.

---

**2d — FINDINGS**

MUST: Every finding carries a severity label: P1 (blocking), P2 (major), P3 (minor).
MUST: Apply the domain-lens gate to every finding:
  Step 1 — Binary test: Would ONLY this role raise this finding given their domain?
  Step 2 — If NO: Revise to name a specific mechanism in this role's domain.
  Step 3 — If still NO after revision: DISCARD the finding.
FAIL condition: A finding passes the gate but names no mechanism specific to this role's domain → INVALID.

For findings of type IA-RESPONSE (F-01):
MUST: The Description field MUST use the two-slot template. Both slots MUST be labeled.
  Format: `Description: [IA-VERDICT: {verdict on the IA's cost claim}] | [ROLE-MECHANISM: {mechanism in this role's domain}]`
FAIL condition: Description contains both components but does not label them as
[IA-VERDICT: ...] and [ROLE-MECHANISM: ...] → INVALID, rewrite Description using the template.
FAIL condition: Either slot is absent → INVALID.

```
[F-01] IA-RESPONSE — [Role]
Severity: P1 | P2 | P3
Description: [IA-VERDICT: {verdict}] | [ROLE-MECHANISM: {mechanism}]
Evidence: [supporting evidence from diff or IA]
```

---

### SECTION 3 — CONSENSUS ANALYSIS

MUST: Produce a dedicated CONSENSUS ANALYSIS section after all per-role findings.
MUST: Include (a) where roles agree, (b) where roles disagree, (c) the most critical
finding across all roles (name finding + role + severity).
FAIL condition: Consensus section only restates per-role findings without cross-role
identification of agreement or disagreement → INVALID.

**Pre-advance compliance check** — MUST verify before Section 4:
- MUST: READ RECEIPT precedes C2 RESULT for EVERY role in the output.
  [This is the C-35 ordering compliance item. Name it explicitly in this check.]
- MUST: C2 RESULT for every role has all five (a)–(e) fields with PRESENT/ABSENT verdicts.
- MUST: Every F-01 Description uses labeled slots [IA-VERDICT: ...] | [ROLE-MECHANISM: ...].

If any check fails: return to the relevant role's section and correct before proceeding.

---

### SECTION 4 — GO/NO-GO RECOMMENDATION

MUST: State exactly one: GO | NO-GO | GO WITH CONDITIONS.
MUST: Justify by naming the primary finding, the role that raised it, and its severity.
FAIL condition: Recommendation without justification → INVALID.
FAIL condition: Ambiguous recommendation ("the team should decide") → INVALID.
```

---

## V-04 — Combined: Lifecycle Emphasis + Output Format

**Hypothesis**: Phase lifecycle structure (V-01) constrains sequencing; table templates (V-02) constrain field completeness. Together they cover C-36 (lifecycle) and C-37 (format) through complementary mechanisms, reducing the attack surface for each — a run that skips the Phase C checklist still has the table structure to enforce C-37; a run that uses a summary table still has the exit condition to flag the violation.

---

```markdown
## /corps-pr — Full-Org PR Review

**Input**: PR diff + `org.yaml`.

Execute phases in order. Each phase has an exit condition set that must be verified
before advancing. Where a template is shown, fill it exactly.

---

### PHASE A — Reviewer Selection

For each changed file or file group, identify the org.yaml role whose scope covers it.

| Changed File / File Group | Role | Scope Match Reason |
|--------------------------|------|--------------------|
| [file]                   | [role] | [reason] |

AMEND directives: add named reviewer with reason "AMEND-specified."

**Phase A exit**: every row has a non-empty scope match reason.

---

### PHASE B — Per-Role Review

Repeat the following template for every selected role. Produce sub-phases B1 → B4 in
document order. Do not skip ahead.

#### [Role Name]

**B1 — PRE-COMMITMENT**

| Field | Value |
|-------|-------|
| Position | ACCEPT \| CHALLENGE \| NEUTRAL |
| Basis | [one sentence — domain basis before seeing IA] |

*B1 must appear before B2 in the output.*

---

**B2 — IA READ RECEIPT**

| Receipt Field | Value |
|--------------|-------|
| (a) IA reference | [document ID or section heading] |
| (b) Cost framing | [verbatim or close paraphrase of IA's cost claim] |
| (c) Evidence basis | [what the IA cites as supporting evidence] |
| (d) Recommended action | [what the IA recommends] |
| (e) Confidence qualifier | [how the IA qualifies its confidence] |

*B2 must appear before B3 in the output. This document-order requirement is the
foundation of the Phase C C-35 ordering compliance check.*

---

**B3 — C2 RESULT**

Enumerate every receipt field with a per-field present/absent verdict.
Do not collapse to a summary verdict — all five rows are required.

| Receipt Field | Verdict |
|--------------|---------|
| (a) IA reference | PRESENT \| ABSENT |
| (b) Cost framing | PRESENT \| ABSENT |
| (c) Evidence basis | PRESENT \| ABSENT |
| (d) Recommended action | PRESENT \| ABSENT |
| (e) Confidence qualifier | PRESENT \| ABSENT |
| **VERDICT** | **SATISFIED** (all PRESENT) \| **UNSATISFIED** (any ABSENT) |

---

**B4 — Findings**

| ID | Type | Severity | Description | Evidence |
|----|------|----------|-------------|---------|
| F-NN | [type] | P1 \| P2 \| P3 | [text] | [text] |

Domain-lens gate — apply before adding any row:
1. Binary: Would ONLY this role raise this finding given their domain?
2. No → revise Description to name a mechanism in this role's domain.
3. Still no → remove the row.

**F-01 IA-RESPONSE template** — for findings of type IA-RESPONSE, the Description
cell must contain both named slots:
```
[IA-VERDICT: {verdict on the IA's cost claim}] | [ROLE-MECHANISM: {mechanism in this role's domain}]
```
A Description cell that contains both components without the named slot labels is
non-compliant. Use the template exactly.

**Phase B exit** (per role): B1 → B2 → B3 → B4 complete in document order.

---

### PHASE C — Consensus Analysis

Produce a CONSENSUS ANALYSIS section.

| Category | Finding Summary | Roles Involved |
|----------|----------------|---------------|
| Agreement | [finding] | [role A, role B] |
| Disagreement | [finding + tension] | [role A vs role B] |
| Most Critical | [finding, severity] | [role that raised it] |

**Phase C Exit Conditions** — verify all six before Phase D:

| # | Condition | Status |
|---|-----------|--------|
| 1 | Every selected role has a findings section | ☐ |
| 2 | B1 PRE-COMMITMENT precedes B2 READ RECEIPT for every role | ☐ |
| 3 | B2 READ RECEIPT precedes B3 C2 RESULT for every role — **C-35 ordering compliance item** | ☐ |
| 4 | B3 C2 RESULT for every role has all five (a)–(e) rows with PRESENT/ABSENT verdicts | ☐ |
| 5 | Every F-01 Description uses [IA-VERDICT: ...] \| [ROLE-MECHANISM: ...] named slots | ☐ |
| 6 | Consensus table has rows for Agreement, Disagreement, and Most Critical | ☐ |

A Phase C exit condition that names C-35 ordering (row 3 above) is required.
Verifying output for ordering is a compliance act, not an optional quality check.

---

### PHASE D — Go/No-Go Recommendation

| Decision | Primary Finding | Role | Severity |
|----------|----------------|------|----------|
| GO \| NO-GO \| GO WITH CONDITIONS | [finding] | [role] | P1 \| P2 \| P3 |

If GO WITH CONDITIONS: list each condition with a resolution owner.
Ambiguous recommendations and recommendations without justification are not accepted.
```

---

## V-05 — Combined: Lifecycle + Format + Register

**Hypothesis**: All three axes reinforce orthogonal compliance mechanisms. Lifecycle structure enforces sequencing (C-36: the ordering is named in the exit condition checklist). Table templates enforce field completeness (C-37: the C2 RESULT table has pre-labeled rows that cannot be omitted). Imperative register enforces template conformance (C-38: MUST + FAIL keywords make [IA-VERDICT] / [ROLE-MECHANISM] slot compliance a hard stop). A run must satisfy all three simultaneously — no single axis can compensate for a failure in another.

---

```markdown
## /corps-pr — Full-Org PR Review

**Input**: PR diff + `org.yaml`.
**Register**: MUST = hard requirement. INVALID = output does not count. FAIL = blocker.
Execute phases in order. Do not advance past a phase until its exit conditions are met.
Where a table template is given, fill it exactly — do not collapse rows or substitute prose.

---

### PHASE A — Reviewer Selection

MUST: Map every changed file to an org.yaml role with an explicit scope-match reason.
MUST: Do not select a role that cannot be traced to at least one specific changed file.
AMEND directive: add named reviewer with reason "AMEND-specified."

| Changed File / File Group | Role | Scope Match Reason |
|--------------------------|------|--------------------|
| [file]                   | [role] | [reason] |

FAIL: Any row with an empty Scope Match Reason → INVALID, add reason or remove role.

**Phase A exit**: all rows filled, all roles file-mapped.

---

### PHASE B — Per-Role Review

MUST: Produce sub-phases B1 → B4 in document order for every selected role.
MUST: Do not begin B2 until B1 is in the output. Do not begin B3 until B2 is in the output.

#### [Role Name]

**B1 — PRE-COMMITMENT**

MUST: Produce this block before accessing the IA document.

| Field | Value |
|-------|-------|
| Position | ACCEPT \| CHALLENGE \| NEUTRAL |
| Basis | [one sentence — domain basis, no reference to IA content] |

FAIL: PRE-COMMITMENT absent → INVALID.
FAIL: PRE-COMMITMENT references IA content → INVALID, rewrite without IA reference.

---

**B2 — IA READ RECEIPT**

MUST: Produce this block after accessing the IA document and before C2 RESULT.
MUST: All five fields must be filled. A receipt with fewer than five fields is INVALID.

| Receipt Field | Receipt Value |
|--------------|--------------|
| (a) IA reference | [document ID or section heading] |
| (b) Cost framing | [verbatim or close paraphrase of the IA's cost claim] |
| (c) Evidence basis | [what the IA cites as supporting evidence] |
| (d) Recommended action | [what the IA recommends] |
| (e) Confidence qualifier | [how the IA qualifies its own confidence] |

MUST: READ RECEIPT must appear before C2 RESULT in the output.
This ordering is a structural compliance requirement enforced again in Phase C exit
condition #3. Violations are INVALID and must be corrected before advancing.

FAIL: Any receipt field row left empty or omitted → INVALID.
FAIL: C2 RESULT appears before READ RECEIPT in the output → INVALID for this role.

---

**B3 — C2 RESULT**

MUST: C2 RESULT appears after READ RECEIPT in document order.
MUST: Enumerate all five receipt fields by their (a)–(e) labels with a PRESENT or
ABSENT verdict per field. Do not collapse to a summary verdict without the per-field rows.
MUST: Add an overall VERDICT row.

| Receipt Field | Verdict |
|--------------|---------|
| (a) IA reference | PRESENT \| ABSENT |
| (b) Cost framing | PRESENT \| ABSENT |
| (c) Evidence basis | PRESENT \| ABSENT |
| (d) Recommended action | PRESENT \| ABSENT |
| (e) Confidence qualifier | PRESENT \| ABSENT |
| **VERDICT** | **SATISFIED** (all rows PRESENT) \| **UNSATISFIED** (any row ABSENT) |

FAIL: Any of rows (a)–(e) missing → INVALID.
FAIL: Only a summary verdict without per-field rows → INVALID.
FAIL: C2 RESULT precedes READ RECEIPT → INVALID.

---

**B4 — Findings**

MUST: Every finding has a severity label: P1 (blocking) | P2 (major) | P3 (minor).

Domain-lens gate — MUST apply to every finding:
1. Binary test: Would ONLY this role raise this finding given their domain?
2. If NO → revise Description to name a specific mechanism owned by this role's domain.
3. If still NO after revision → DISCARD the finding.

FAIL: Finding names no mechanism specific to this role's domain → INVALID, apply gate.

**F-01 IA-RESPONSE** — MUST use the two-slot Description template. Both slots MUST
appear as labeled slots in the output. The template is not paraphraseable.

MUST format:
```
[IA-VERDICT: {reviewer's verdict on the IA's cost claim}] | [ROLE-MECHANISM: {specific mechanism in this role's domain}]
```

| ID | Type | Severity | Description | Evidence |
|----|------|----------|-------------|---------|
| F-01 | IA-RESPONSE | P1 \| P2 \| P3 | [IA-VERDICT: ...] \| [ROLE-MECHANISM: ...] | [evidence] |

FAIL: Description contains both components but omits slot labels [IA-VERDICT: ...]
and [ROLE-MECHANISM: ...] → INVALID, rewrite using template.
FAIL: Either slot is absent from Description → INVALID.

**Phase B exit** (per role): B1 → B4 complete in document order, all MUST/FAIL conditions satisfied.

---

### PHASE C — Consensus Analysis

MUST: Produce a dedicated CONSENSUS ANALYSIS section after all per-role findings.

| Category | Finding Summary | Roles Involved |
|----------|----------------|---------------|
| Agreement | [finding] | [agreeing roles] |
| Disagreement | [finding + characterization of tension] | [roles in tension] |
| Most Critical | [finding, severity] | [role that raised it] |

MUST: All three category rows present and filled.
FAIL: Consensus section that only restates per-role findings without cross-role
identification of agreement and disagreement → INVALID.

**Phase C Exit Conditions** — MUST verify all before Phase D.
A failure on any condition blocks Phase D output.

| # | Compliance Item | Verified? |
|---|----------------|-----------|
| 1 | Every selected role has a B4 Findings section | ☐ |
| 2 | B1 PRE-COMMITMENT precedes B2 READ RECEIPT for every role | ☐ |
| 3 | B2 READ RECEIPT precedes B3 C2 RESULT for every role [**C-35 ordering — this is a Phase C compliance item, not a style note**] | ☐ |
| 4 | B3 C2 RESULT for every role contains all five (a)–(e) rows with explicit PRESENT/ABSENT verdicts | ☐ |
| 5 | Every F-01 Description uses labeled slots [IA-VERDICT: ...] \| [ROLE-MECHANISM: ...] with no prose substitution | ☐ |
| 6 | Consensus table has rows for Agreement, Disagreement, and Most Critical | ☐ |

FAIL: Any ☐ remaining → do not produce Phase D output. Return to the failing section.

---

### PHASE D — Go/No-Go Recommendation

MUST: State exactly one decision: GO | NO-GO | GO WITH CONDITIONS.
MUST: Justify by naming the primary finding, the role that raised it, and its severity.
FAIL: Decision without justification → INVALID.
FAIL: Ambiguous decision ("the team should decide") → INVALID.

| Decision | Primary Finding | Role | Severity |
|----------|----------------|------|----------|
| GO \| NO-GO \| GO WITH CONDITIONS | [finding] | [role] | P1 \| P2 \| P3 |

If GO WITH CONDITIONS:
- List each condition as a separate row with a named resolution owner.
- Do not produce a conditional GO without specifying conditions.
```

---

## Axis Coverage Summary

| Variation | Primary Axis | C-36 Mechanism | C-37 Mechanism | C-38 Mechanism |
|-----------|-------------|----------------|----------------|----------------|
| V-01 | Lifecycle emphasis | Named in Phase C exit checklist as compliance item | Prose instruction with inline template | F-01 slot template in prose block |
| V-02 | Output format (tables) | Pre-output compliance check (compact) | Mandatory table with (a)–(e) rows | F-01 Description cell slot template |
| V-03 | Phrasing register (imperative) | Named in pre-advance compliance check with MUST | MUST + FAIL keywords on C2 RESULT per-field rows | MUST + FAIL keywords on slot template |
| V-04 | Lifecycle + Format | Named in Phase C exit conditions table, row 3 | Mandatory B3 C2 RESULT table | F-01 table Description cell slot template |
| V-05 | Lifecycle + Format + Register | Named in Phase C exit conditions table, row 3, with explicit compliance item label | MUST + FAIL keywords + mandatory table with (a)–(e) rows | MUST + FAIL keywords + mandatory slot template |
