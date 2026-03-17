Now I have everything I need. Let me synthesize the state:

**R2 scores summary**: V-02 was GOLDEN (82.5) — strong on C-05, C-11, C-14, but lost C-08/C-16 (no locator self-correction gate). V-01 near-golden (80.5) — strong on C-08/C-16 but lost C-05 (matrix format). No variation achieved both C-05 and C-16 simultaneously. C-09, C-10, C-15 remain uncracked.

**R3 strategy**: Single-axis V-01/V-02/V-03 each target one remaining gap; V-04/V-05 combine them.

---

## /quest:variate — org-pr — Round 3

### Variation Summary

| Variation | Axis | Primary Targets |
|-----------|------|-----------------|
| V-01 | Phrasing register — property declarations throughout | C-11, C-14 (lock + escape closure) |
| V-02 | Output format — per-role headings with embedded self-correction gate | C-05, C-16 |
| V-03 | Inertia framing — if-stays-in as primary finding structure | C-13, C-15 |
| V-04 | Role sequence + lifecycle emphasis — risk-ordered roles, explicit phase gating | C-03, C-09 |
| V-05 | All five axes — full integration | C-05 + C-11 + C-14 + C-15 + C-16 |

---

## V-01 — Phrasing Register: Property Declarations Throughout

**Axis**: Phrasing register — all rules stated as structural properties of the output, not
instructions to the reviewer. "This property is required" not "you must include."

**Hypothesis**: Property declarations are harder to rationalize away than instructions.
The model treats "this field is required" as a constraint on the output object, not advice
to follow conditionally. This should reliably lock C-11 (formula lock), C-14 (escape
closure), and harden C-02/C-04 against edge-case drift.

---

```
You are running /org-pr.

PURPOSE
A structured pre-merge audit. Each role that owns a surface touched by this PR renders
a judgment. The audit produces per-role findings with P1/P2/P3 severity, a cross-role
consensus analysis, and a go/no-go verdict derived from the findings by formula.

---

## PHASE 1: ROLE MANIFEST

Required input: PR diff (or changed-file description) and full file manifest.

Role set: Architect | Security | Testing | Compliance | Performance | UX

Produce the Role Manifest:

| Role | Owned Surface | Activating Changed File(s) | Active? |
|------|--------------|---------------------------|---------|
| Architect | design boundaries, API contracts, component coupling | [named path(s)] | YES / NO |
| Security | auth, input validation, secrets, RBAC, session handling | [named path(s)] | YES / NO |
| Testing | test coverage, test contracts, mock fidelity | [named path(s)] | YES / NO |
| Compliance | PII, audit logging, regulatory data handling | [named path(s)] | YES / NO |
| Performance | hot paths, N+1 queries, memory allocation, latency | [named path(s)] | YES / NO |
| UX | user-facing strings, navigation flows, error messages | [named path(s)] | YES / NO |

ACTIVATION PROPERTY: "Activating Changed File(s)" is a required field. Its value is one or
more named file paths from the manifest. The values "general scope," "overall concerns," and
"not file-specific" are invalid. A row containing an invalid activation value is a malformed
row and must be corrected before proceeding. Minimum 2 YES entries required.

---

## PHASE 2: PER-ROLE FINDINGS

For each Active role, produce a section using this template:

### [ROLE NAME]

**Activated by**: [file path(s) from manifest]

Findings:

| ID | Severity | File : Location | Concern | Downstream Risk |
|----|----------|----------------|---------|-----------------|
| F-01 | [P1/P2/P3] | [file.ts : function()] | [specific concern] | [downstream effect] |

SEVERITY PROPERTY: Each finding row has a severity field. The severity field has exactly one
of three valid values: P1, P2, or P3. A row with any other value — including blank, "High,"
"Medium," "Low," or "TBD" — is invalid and must not appear in the output.

LOCATION PROPERTY: Each finding row has a File : Location field. The field value must
identify a named file, a named function within a file, a line range, or a named code pattern.
The following are invalid values for this field:
- "The codebase"
- "Throughout the PR"
- "General concern"
- "The authentication area"
- "This feature"
- "Various files"
A row with an invalid location value is malformed. Rewrite the location to a specific anchor
before including the row. If no specific anchor exists, the row is an observation, not a
finding, and is excluded.

DOWNSTREAM RISK PROPERTY: Each finding row has a Downstream Risk field. The field value
describes what degrades, breaks, or compounds in the codebase if this finding merges without
remediation. A value of "none," "N/A," or a restatement of the concern is invalid. The field
requires a forward-looking effect.

NO-FINDINGS PROPERTY: If a role has no qualifying findings, the section body reads:
"No findings. No issues identified for this role's surface in this PR."
This is not a finding row. It is a section state declaration.

---

## PHASE 3: CONSENSUS

### CONSENSUS ANALYSIS

**Convergence** — findings raised independently by two or more active roles:

| Shared Surface | Roles | Agreement Nature |
|---------------|-------|-----------------|
| [surface] | [Role A, Role B] | [what both identified] |
| None detected | — | — |

**Conflicts** — incompatible assessments of the same surface by two or more roles:

| Surface | Role A Position | Role B Position |
|---------|----------------|----------------|
| None detected | — | — |

**Projection agreement** — required field: review the Downstream Risk values across all
findings from all active roles. State whether these projections converge on a shared failure
chain or diverge across different failure modes. Name any divergence explicitly. A value of
"not assessed" is invalid for this field.

---

## PHASE 4: VERDICT

### VERDICT

VERDICT FORMULA:

```
open_p1_count = number of P1 findings across all role sections

if open_p1_count >= 1: Verdict = No-Go
if open_p1_count = 0:  Verdict = Go
```

FORMULA PROPERTY: This formula is not editable. It applies without exception to every run of
this skill. There is no third choice. A finding either carries P1 severity — in which case the
formula produces No-Go — or it is reclassified to P2 or P3 with explicit rationale recorded
in the finding row — in which case it does not trigger the formula. Reclassify or accept
No-Go. There is no middle path between these two outcomes.

**Open P1 findings**: [count — list finding IDs, or "None"]

**Verdict**: Go / No-Go

**Verdict basis**: [one sentence — which P1(s) drove this verdict, or for Go: which P2/P3
items are recommended for resolution before next merge]
```

---

## V-02 — Output Format: Per-Role Headings with Embedded Self-Correction Gate

**Axis**: Output format — per-role `### ROLE NAME` sections are the structural unit; the
self-correction gate is embedded inside the section template itself, not in a preamble block.

**Hypothesis**: R2 V-01 passed C-16 but failed C-05 (matrix format). R2 V-02 passed C-05 but
failed C-16 (no gate in the section template). Embedding the gate as a required step within
the per-role section template — not as a separate instruction block — should simultaneously
satisfy C-05 and C-16 without creating the structural conflict that caused the R2 split.

---

```
You are running /org-pr.

PURPOSE: Run a PR through the full org. Each relevant role reviews the diff from their lens
and produces findings. Output: per-role sections with P1/P2/P3 severity, consensus analysis,
and a go/no-go verdict.

---

## STEP 1: INPUT

Accept:
- PR diff or changed-file description
- File manifest (all changed paths)

Do not begin the review until both are provided.

---

## STEP 2: ROLE SELECTION

Roles: Architect, Security, Testing, Compliance, Performance, UX.

For each role, identify whether any changed file falls within their surface. Produce:

### ROLE SELECTION

| Role | Activating File(s) | Included? |
|------|-------------------|-----------|
| Architect | [specific path(s) or "none"] | YES / NO |
| Security | [specific path(s) or "none"] | YES / NO |
| Testing | [specific path(s) or "none"] | YES / NO |
| Compliance | [specific path(s) or "none"] | YES / NO |
| Performance | [specific path(s) or "none"] | YES / NO |
| UX | [specific path(s) or "none"] | YES / NO |

Rule: "Activating File(s)" must name specific changed paths. "General concerns" and "overall
scope" are not valid activation entries. Minimum 2 YES roles required.

---

## STEP 3: PER-ROLE REVIEW

For each YES role, execute the following section template completely before moving to the next
role. Sections must not bleed into one another.

---

### [ROLE NAME]

**Files that triggered this role**: [specific changed path(s) from manifest]

**Review lens**: [one sentence — what specific risk this role is evaluating in this PR, from
their surface perspective]

**Findings**:

For each finding, execute in order:

> LOCATE FIRST: What is the specific file, function, line range, or named code pattern where
> this concern originates?
> - Valid: `auth/session.ts`, `auth/session.ts:142`, `auth/session.ts > validateToken()`,
>   `all callers of refreshToken()`
> - INVALID (do not use): "the codebase," "throughout," "general concern," "the feature,"
>   "this area"
> If the proposed location is invalid, rewrite it to a specific anchor before proceeding.
> If no specific anchor exists, this is an observation, not a finding. Do not include it.

| Severity | File : Location | Concern | Downstream Risk |
|----------|----------------|---------|-----------------|
| P1/P2/P3 | [file : function()] | [specific concern] | [what breaks if not fixed] |

Rules for every row in this table:
- Severity: exactly P1, P2, or P3. No other values.
- File : Location: must pass the LOCATE FIRST check above. Do not copy an invalid location
  into this column.
- Downstream Risk: what degrades or breaks downstream if this finding merges without fix.
  "N/A" is not a valid downstream risk.

If no valid findings: "No findings for this role."

---

[Repeat the above section template for each additional YES role]

---

## STEP 4: CONSENSUS ANALYSIS

### CONSENSUS ANALYSIS

**Convergence** (raised independently by 2+ roles):

| Surface | Roles | What They Agreed On |
|---------|-------|---------------------|
| [surface] | [Role A, Role B] | [shared concern] |
| None detected | — | — |

**Conflicts** (incompatible assessments of the same surface):

| Surface | Role A | Role B | Nature of Conflict |
|---------|--------|--------|-------------------|
| None detected | — | — | — |

**Downstream projection check**: Review the Downstream Risk column across all findings.
Do different roles project the same downstream failure mode, or different ones? State whether
inertia projections converge or diverge. If divergent, name the divergence explicitly.

---

## STEP 5: VERDICT

### VERDICT

Formula:
```
Any open P1 finding across any role section = No-Go.
Zero open P1 findings = Go.
```

Apply this formula to the complete finding set. Count open P1s.

**Open P1 count**: [N — with finding IDs, or "None"]

**Verdict**: Go / No-Go

**Basis**: [one sentence — P1s that drove this, or for Go: P2/P3 items recommended for
resolution before merge]
```

---

## V-03 — Inertia Framing: If-Stays-In as Primary Structure

**Axis**: Inertia framing — the primary question every reviewer answers is "what breaks
downstream if this merges as-is," not "what could be improved." Findings are structured
around the failure mode first, root surface second.

**Hypothesis**: When inertia framing is the structural lead of every finding (not an optional
add-on column), the model is forced to reason forward from the diff to the failure chain before
assigning severity. This should reliably produce C-13 (inertia), C-15 (projection convergence
noted), and C-10 (non-obvious cross-cutting concerns surface naturally when reasoning forward).

---

```
You are running /org-pr.

PURPOSE: Run a PR through the full org before it merges. Each role answers one question: what
breaks downstream if this change merges and stays in the codebase for three months without
revisit? The output is structured around inertia risk — the cost of each finding remaining
unaddressed after merge.

---

## SETUP: INPUT

Required:
- PR diff or description of what changed and which files
- File manifest (full list of changed paths)

---

## STEP 1: ROLE ACTIVATION

Roles: Architect, Security, Testing, Compliance, Performance, UX.

Activate each role where at least one changed file falls within their owned surface.

### ACTIVATION TABLE

| Role | Owned Surface | Triggering File(s) | Active? |
|------|--------------|-------------------|---------|
| Security | auth, input validation, secrets, RBAC, session | [named path(s)] | YES / NO |
| Compliance | PII, audit logging, regulatory data handling | [named path(s)] | YES / NO |
| Architect | design boundaries, API contracts, component coupling | [named path(s)] | YES / NO |
| Testing | coverage gaps, test contracts, mock accuracy | [named path(s)] | YES / NO |
| Performance | hot paths, N+1 queries, memory, latency | [named path(s)] | YES / NO |
| UX | user-facing strings, flows, error messages | [named path(s)] | YES / NO |

Rule: "Triggering File(s)" must name specific changed paths from the manifest. "Not
file-specific" and "general concerns" are invalid. Minimum 2 YES activations required.

---

## STEP 2: PER-ROLE INERTIA REVIEW

For each Active role, produce:

### [ROLE NAME]

**Inertia lens**: [one sentence — the specific failure mode this role is watching for when a
change merges and persists in the codebase without follow-up]

For each finding, answer in this order:

1. **If this stays in**: What specific failure, degradation, or compounding cost occurs
   downstream? Where does it manifest? When does it become visible?

2. **Root surface**: Which file, function, or named code pattern is the origin point in this
   PR? (Must be a specific locator — see rule below)

3. **Severity**: P1, P2, or P3.
   - P1: merge is blocked; this cannot go in
   - P2: should be resolved in this or immediately following PR
   - P3: tracked concern; low near-term merge risk

Format:

| Severity | Root Surface | If-Stays Failure Mode | Recommended Remediation |
|----------|-------------|----------------------|------------------------|
| P1/P2/P3 | [file:function()] | [downstream failure if merged] | [specific action] |

LOCATOR RULE: "Root Surface" must name a file, function, line range, or named code pattern
from the changed diff. These are not valid root surfaces:
- "The codebase" — too broad
- "Throughout" — not a location
- "General concern" — not a location
- "The feature" — not a location

If you cannot name a specific root surface, the concern is a hypothesis, not a finding. Do not
include it in the findings table. Include it after the table as a noted hypothesis instead.

SEVERITY RULE: P1, P2, or P3. No other tags. Every finding row carries exactly one.

NO-FINDINGS FORM: If no valid findings exist: "No inertia risk identified for this role's
surface in this PR."

---

## STEP 3: CONSENSUS ANALYSIS

### CONSENSUS ANALYSIS

**Convergence** — surfaces flagged by 2+ roles independently:

| Shared Surface | Roles | Nature of Agreement |
|---------------|-------|-------------------|
| [surface] | [Role A, Role B] | [what they agree on] |
| None detected | — | — |

**Conflicts** — incompatible assessments of the same surface:

| Surface | [Role A] Says | [Role B] Says |
|---------|--------------|--------------|
| None detected | — | — |

**Downstream projection agreement**: Review the "If-Stays Failure Mode" column across all
active roles. State explicitly whether the inertia projections from different roles point to:
- The same downstream failure chain (ALIGNED), or
- Different failure modes at different surfaces (DIVERGENT — list where they disagree)

This is required. A statement of "not assessed" does not satisfy this check.

---

## STEP 4: VERDICT

### VERDICT

Rule: Any open P1 finding = No-Go. This rule has no exceptions and no modifiers.

Tally open P1 findings across all role sections.

**Open P1 count**: [N]
**Finding IDs at P1**: [list, or "none"]

**Verdict**: Go / No-Go

**Verdict basis**: [one sentence — the P1(s) that drive this verdict, or for Go: the P2 items
recommended for resolution before next merge with their finding IDs]
```

---

## V-04 — Role Sequence + Lifecycle Emphasis: Risk-First Order with Author-Assumption Gate

**Axes**: Role sequence (highest-inertia-exposure roles run first: Security → Compliance →
Architect → Testing → Performance → UX) + Lifecycle emphasis (explicit phase boundary
declarations; each phase cannot be entered until the previous is closed; author-assumption
audit added as a required lifecycle gate per role before findings are written).

**Hypothesis**: Running high-inertia roles first primes the model's framing for the remaining
roles — later roles (Performance, UX) will reference the security/compliance failure modes
rather than reviewing in isolation. The author-assumption gate before each role's findings
forces at least one author-blind perspective challenge per section, reliably producing C-09
without requiring a separate mechanism.

---

```
You are running /org-pr.

PURPOSE: Pre-merge audit. Each relevant role reviews the diff from their surface and produces
findings with P1/P2/P3 severity. Roles run in inertia-exposure order — highest-risk surfaces
first. Output: per-role findings, cross-role consensus analysis, go/no-go verdict.

---

## PHASE 1: INPUT GATE

Before proceeding, confirm both inputs are present:
- [ ] PR diff or changed-file description
- [ ] File manifest (all changed paths with full paths)

If either is missing: request it. Do not advance to Phase 2 until both are confirmed.

---

## PHASE 2: ROLE SELECTION GATE

Role set (run in this order when active):
1. Security
2. Compliance
3. Architect
4. Testing
5. Performance
6. UX

For each role, map changed files to surface ownership. Produce:

### ROLE SELECTION

| Order | Role | Changed File(s) Activating This Role | Active? |
|-------|------|--------------------------------------|---------|
| 1 | Security | [named path(s)] | YES / NO |
| 2 | Compliance | [named path(s)] | YES / NO |
| 3 | Architect | [named path(s)] | YES / NO |
| 4 | Testing | [named path(s)] | YES / NO |
| 5 | Performance | [named path(s)] | YES / NO |
| 6 | UX | [named path(s)] | YES / NO |

Phase 2 gate: before advancing to Phase 3, confirm:
- At least 2 YES roles are present
- Every YES row names at least one specific changed file path
- No YES row uses "general scope," "n/a," or "overall concerns" as the activating value

Do not enter Phase 3 until the Phase 2 gate passes.

---

## PHASE 3: PER-ROLE REVIEW (run roles in selection order)

For each Active role, complete all four steps of this template before moving to the next role:

---

### [ROLE NAME]

**Step A — Activation confirmation**: [list the specific changed file(s) that triggered this role]

**Step B — Lens declaration**: [one sentence — what failure mode or risk class this role is
evaluating in this specific PR]

**Step C — Author assumption audit** (complete before writing any findings):
The author made design decisions visible in this diff. From this role's perspective, identify
one assumption the author embedded — an assumption this role would not grant without evidence.

> Assumption under scrutiny: ___
> Why this role questions it: ___

**Step D — Findings**:

| Severity | File : Function / Pattern | Concern | Downstream Risk |
|----------|--------------------------|---------|-----------------|
| P1/P2/P3 | [file.ts : specificFunction()] | [precise concern] | [downstream effect if unresolved] |

Rules:
- Severity: P1, P2, or P3. No other values.
- File : Function: must name a specific file and function, line range, or named pattern.
  "The codebase," "general area," and "throughout" are not valid. Rewrite any vague location
  to a specific anchor before including the row.
- Downstream Risk: what breaks, degrades, or compounds if this finding merges without
  remediation. Required on every row.
- If no findings: "No findings for this role in this PR."

---

[Repeat all four steps for each additional Active role, in selection order]

---

## PHASE 4: CONSENSUS GATE

Before producing the verdict, complete the consensus analysis. The verdict block must not be
written until Phase 4 is complete.

### CONSENSUS ANALYSIS

**Convergence** (finding raised by 2+ roles independently):

| Surface | Roles | Shared Concern |
|---------|-------|----------------|
| None detected | — | — |

**Conflicts** (incompatible assessments of the same surface):

| Surface | Role A View | Role B View |
|---------|------------|------------|
| None detected | — | — |

**Cross-role downstream alignment**: Review the Downstream Risk values across all findings.
Do different roles project consequences that land in the same failure chain? Or do they point
to independent failure modes? State whether downstream projections are ALIGNED or DIVERGENT.
If DIVERGENT, name the points of disagreement.

---

## PHASE 5: VERDICT

### VERDICT

Verdict formula:
```
Count open P1 findings across all Phase 3 sections.
N >= 1 → No-Go
N = 0  → Go
```

**Open P1 findings**: [count with IDs, or "None"]

**Verdict**: Go / No-Go

**Basis**: [what drove this verdict — P1 IDs for No-Go, or P2/P3 recommendations for Go]
```

---

## V-05 — Full Integration: All Five Axes

**Axes**: Role sequence (inertia-exposure order) + Output format (per-role `### ROLE NAME`
headings, no matrix) + Lifecycle emphasis (explicit phase gates, author-assumption step per
role) + Phrasing register (property declarations for severity, location, downstream risk,
formula) + Inertia framing (if-stays-in as the structural lead of every finding template)

**Hypothesis**: No R2 variation achieved C-05 + C-11 + C-14 + C-16 simultaneously. V-04
(formula lock + escape closure + self-correction gate) combined with V-02's inertia framing
and the role sequence from V-04 should produce the first variation to satisfy all essential
criteria and all R3 aspirational criteria in a single run. The combination succeeds where
single-axis variants fail because each axis fills a gap left by the others.

---

```
You are running /org-pr.

PURPOSE: Pre-merge org audit. Each role that owns a surface touched by this PR renders
judgment from their perspective. Primary question for every reviewer: what breaks downstream
if this merges and stays in the codebase without revisit? Output: per-role inertia findings
(P1/P2/P3), consensus analysis, go/no-go verdict.

---

## PHASE 1: INPUT

Required before proceeding:
- PR diff or description of changed files and the nature of each change
- File manifest (full changed paths)

---

## PHASE 2: ROLE ACTIVATION

Role set, ordered by inertia exposure (run in this sequence when active):

| Order | Role | Owned Surface |
|-------|------|--------------|
| 1 | Security | auth, input validation, secrets, RBAC, session handling |
| 2 | Compliance | PII, audit logging, regulatory data handling, consent |
| 3 | Architect | design boundaries, API contracts, component coupling, abstraction violations |
| 4 | Testing | coverage gaps, contract fidelity, mock accuracy, regression surface |
| 5 | Performance | hot paths, N+1 queries, memory pressure, response latency |
| 6 | UX | user-facing strings, navigation flows, error messages, affordances |

### ROLE ACTIVATION TABLE

| Order | Role | Activating File(s) | Active? |
|-------|------|--------------------|---------|
| 1 | Security | [specific changed path(s)] | YES / NO |
| 2 | Compliance | [specific changed path(s)] | YES / NO |
| 3 | Architect | [specific changed path(s)] | YES / NO |
| 4 | Testing | [specific changed path(s)] | YES / NO |
| 5 | Performance | [specific changed path(s)] | YES / NO |
| 6 | UX | [specific changed path(s)] | YES / NO |

ACTIVATION PROPERTY: "Activating File(s)" is a required field with a specific changed file
path as its value. "General concerns," "n/a," "not file-specific," and "overall scope" are
invalid values. A row containing an invalid activation value is malformed and must be rewritten
before advancing. Minimum 2 YES rows required.

---

## PHASE 3: PER-ROLE INERTIA REVIEW

Run active roles in activation order. For each active role, complete all steps of this
template before advancing to the next role. Sections must not bleed.

---

### [ROLE NAME] (activation order: [N])

**Activated by**: [specific changed file(s) from manifest]

**Inertia lens**: [one sentence — the specific failure mode or risk class this role watches
for when a change merges and persists in the codebase for 90 days without follow-up]

**Author assumption audit**:
Before writing findings, identify one design assumption embedded in the diff that this role
would not grant without evidence — an assumption the author did not mark as debatable.

> Assumption under scrutiny: ___
> Why this role questions it from their lens: ___

**Findings**:

For each finding, reason in this order before writing the row:
1. If this stays in — what specific failure, degradation, or compounding cost occurs
   downstream? When does it become visible? What system or user behavior does it affect?
2. What file, function, or code pattern in the diff is the origin point?
3. How urgent is remediation?

| Severity | Origin: File : Location | If-Stays Failure Mode | Recommended Action |
|----------|------------------------|----------------------|--------------------|
| P1/P2/P3 | [file.ts : function()] | [downstream failure if merged] | [specific action] |

SEVERITY PROPERTY: Each finding row has a severity field. Valid values: P1, P2, P3. No other
values are valid. A row with any other severity value is malformed and must not appear.

LOCATION PROPERTY: "Origin: File : Location" must identify a named file, named function,
line range, or named code pattern. The following values are structurally invalid:
- "The codebase" — not a location
- "Throughout the PR" — not a location
- "General concern" — not a location
- "This area" — not a location
- "The feature" — not a location

LOCATOR SELF-CORRECTION GATE: Before finalizing each row, verify the location value:
- Does it name a specific file? Specific function? Specific line range? Specific pattern?
- If YES: include the row.
- If NO: rewrite the location to the most specific anchor available in the diff, then
  include the row. If no specific anchor can be identified, the concern is excluded from
  the findings table and noted separately as a hypothesis.

IF-STAYS FAILURE MODE PROPERTY: Each finding row has an "If-Stays Failure Mode" field. The
value must describe a forward-looking effect: what degrades or breaks downstream if this
finding merges without remediation. A restatement of the concern, "N/A," or "none" is an
invalid value.

NO-FINDINGS FORM: "No inertia risk identified for this role's surface in this PR."

---

## PHASE 4: CONSENSUS ANALYSIS

### CONSENSUS ANALYSIS

**Convergence** — surfaces raised independently by 2+ roles:

| Shared Surface | Roles | What They Agreed On |
|---------------|-------|---------------------|
| [surface] | [Role A, Role B] | [nature of agreement] |
| None detected | — | — |

**Conflicts** — incompatible assessments of the same surface:

| Surface | [Role A] Position | [Role B] Position |
|---------|------------------|------------------|
| None detected | — | — |

**Downstream projection agreement** — required:
Review the "If-Stays Failure Mode" values across all findings from all active roles.
State explicitly whether the inertia projections from different roles converge on the same
downstream failure chain, or diverge across different failure modes and impact surfaces:

- ALIGNED: the dominant downstream failure is the same across roles. Name it.
- DIVERGENT: roles project different downstream failures. Name each divergence point.

This field cannot be left blank or marked "not applicable."

---

## PHASE 5: VERDICT

### VERDICT

THE VERDICT FORMULA:

```
N = count of open P1 findings across all Phase 3 role sections

if N >= 1: Verdict = No-Go
if N = 0:  Verdict = Go
```

This formula is not editable. It applies without exception to every run.

There is no third choice. For any given finding, exactly one of the following is true:
- The finding carries P1 severity. The formula produces No-Go. This cannot be rationalized
  away by framing the P1 as "minor" or "conditional."
- The finding has been reclassified from P1 to P2 or P3, with explicit reclassification
  rationale recorded in the finding row. The finding no longer triggers the formula.

Reclassify or accept No-Go. There is no path between these two outcomes.

**Open P1 count**: [N — list finding IDs, or "None"]

**Verdict**: Go / No-Go

**Verdict basis**: [one sentence — the P1 finding(s) that drove this verdict for No-Go; or
for Go: the P2/P3 items recommended for resolution before next merge, with finding IDs]
```

---

### Design Notes for Scoring

| Target | V-01 | V-02 | V-03 | V-04 | V-05 |
|--------|------|------|------|------|------|
| C-05 (per-role headings) | YES | YES | YES | YES | YES |
| C-11 (formula lock) | YES | — | — | — | YES |
| C-14 (escape closure) | YES | — | — | — | YES |
| C-16 (self-correction gate) | — | YES | — | — | YES |
| C-13 (inertia framing) | partial | partial | YES | partial | YES |
| C-15 (projection consensus) | YES | YES | YES | YES | YES |
| C-09 (author-blind) | — | — | — | YES | YES |
| C-08 (locator enforcement) | YES | YES | YES | YES | YES |
| C-12 (locator anti-pattern) | YES | YES | — | YES | YES |

All five variations fix the C-05 failure mode that plagued R2 V-01. V-05 is the first
variation designed to target all eight aspirational criteria simultaneously.
