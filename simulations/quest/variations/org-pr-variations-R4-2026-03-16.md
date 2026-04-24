**R4 variations written** to `simulations/quest/variations/org-pr-variations-R4-2026-03-16.md`.

**Round 4 strategy summary:**

| Variation | Axis | New Criteria Targeted |
|-----------|------|-----------------------|
| V-01 | Role authority sequence declaration (isolated) | C-17 |
| V-02 | Axis conflict resolution rule (two-axis composition: phrasing register + inertia framing) | C-18 |
| V-03 | C-17 + C-18 combined | C-17, C-18 |
| V-04 | C-17 + C-18 + inertia framing (three-axis) | C-17, C-18, C-13, C-15 |
| V-05 | Full integration — R3 V-05 + C-17 authority chain + C-18 seven-axis priority table | All 14 criteria |

**Key design decisions:**

- **C-17** (authority ordering): V-01 adds an explicit "Authority Chain" block that names not just the order but *why* each position carries the weight it does — Security sets the threat boundary that all other roles work within, Compliance overrides all tradeoffs, etc. This is what R3 V-04/V-05 had implicitly but never stated.

- **C-18** (conflict resolution): V-02 introduces the explicit rule that inertia framing governs *content* and property declarations govern *validation* — so the `Root Surface` column name comes from inertia framing, but `LOCATION PROPERTY` defines what values are valid for it. V-05 formalizes this as a seven-axis priority table covering all axes.

- **V-05** adds both C-17 and C-18 to R3 V-05's body without removing any existing machinery — the authority chain block slots before Phase 2, and the axis composition priority table slots after it. The C-18 rule itself is the structural mitigation for overcrowding risk.
les must
work within — should produce PASS on C-17. Single-axis test: no inertia framing, no property
declarations, no self-correction gate. Just authority ordering made explicit.

---

```
You are running /org-pr.

PURPOSE: Pre-merge org audit. Each role that owns a surface touched by this PR reviews the
diff and produces findings. Output: per-role findings with P1/P2/P3 severity, consensus
analysis, go/no-go verdict.

---

## ROLE AUTHORITY CHAIN

Roles run in authority sequence order. This sequence is not arbitrary — it reflects the
constraint propagation direction across role surfaces:

1. **Security** — runs first because security findings define the threat boundary that all
   other roles must reason within. A Security P1 cannot be rationalized away by a later
   role's judgment.

2. **Compliance** — runs second because regulatory constraints are non-negotiable overrides.
   A finding that Compliance raises as non-compliant is not subject to architectural
   compromise or performance tradeoff.

3. **Architect** — runs third because architectural boundary violations discovered after
   Security and Compliance have set their constraints are the correct scope for design
   discussion. Architect findings inform what is structurally fixable within the compliance
   and security envelope.

4. **Testing** — runs fourth because test coverage gaps are assessed against the behavioral
   contracts that Security, Compliance, and Architect have now defined. Testing evaluates
   whether the intended behavior is verifiable.

5. **Performance** — runs fifth because performance characteristics are evaluated on the
   implementation as bounded by the preceding three roles. A regression that Security
   requires for correctness is not a Performance veto.

6. **UX** — runs last because user-facing surface is assessed after the structural concerns
   are known. UX can identify usability issues without the authority to override P1 findings
   from earlier roles.

**Authority rule**: Earlier roles in this chain establish constraints that later roles work
within. A later role cannot override a finding from an earlier role. A later role CAN flag
that an earlier role's finding creates a secondary impact on their surface — this is noted
as a downstream effect, not a counter-finding.

---

## STEP 1: INPUT

Required before proceeding:
- PR diff or description of what changed and which files
- File manifest (all changed paths)

---

## STEP 2: ROLE ACTIVATION

For each role in authority sequence order, identify whether any changed file falls within
their owned surface.

| Order | Role | Owned Surface | Activating File(s) | Active? |
|-------|------|--------------|-------------------|---------|
| 1 | Security | auth, input validation, secrets, RBAC, session handling | [named path(s)] | YES / NO |
| 2 | Compliance | PII, audit logging, regulatory data handling, consent | [named path(s)] | YES / NO |
| 3 | Architect | design boundaries, API contracts, component coupling | [named path(s)] | YES / NO |
| 4 | Testing | coverage gaps, test contracts, mock fidelity, regression | [named path(s)] | YES / NO |
| 5 | Performance | hot paths, N+1 queries, memory allocation, latency | [named path(s)] | YES / NO |
| 6 | UX | user-facing strings, navigation flows, error messages | [named path(s)] | YES / NO |

Rule: "Activating File(s)" must name specific changed paths from the manifest. "General
concerns" and "overall scope" are invalid activation values. Minimum 2 YES rows required.

---

## STEP 3: PER-ROLE FINDINGS

Run active roles in authority sequence order. Complete each role's section fully before
advancing.

### [ROLE NAME] (authority position: [N])

**Activated by**: [specific changed file(s)]

**Authority scope**: [one sentence — what this role's positional authority covers in this
PR, and what constraint it establishes for roles that follow]

**Findings**:

| Severity | File : Location | Concern | Downstream Risk |
|----------|----------------|---------|-----------------|
| P1/P2/P3 | [file.ts : function()] | [specific concern] | [downstream effect if merged] |

Rules:
- Severity: P1, P2, or P3. No other values.
- File : Location: must name a specific file, function, line range, or named code pattern.
  "The codebase," "throughout," "general concern" are not valid locations.
- Downstream Risk: what breaks or degrades downstream if this finding merges without fix.
  "N/A" is not a valid downstream risk.
- If no findings: "No findings for this role in this PR."

[Repeat for each Active role, in authority sequence order]

---

## STEP 4: CONSENSUS ANALYSIS

### CONSENSUS ANALYSIS

**Convergence** — surfaces raised independently by 2+ roles:

| Shared Surface | Roles | What They Agreed On |
|---------------|-------|---------------------|
| [surface] | [Role A, Role B] | [shared concern] |
| None detected | — | — |

**Authority chain effects** — cases where a later role's finding was directly constrained
by, or is a downstream consequence of, an earlier role's finding:

| Later Role Finding | Earlier Role Finding That Scoped It | Relationship |
|-------------------|-------------------------------------|--------------|
| None detected | — | — |

**Conflicts** — incompatible assessments of the same surface:

| Surface | Role A Position | Role B Position |
|---------|----------------|----------------|
| None detected | — | — |

---

## STEP 5: VERDICT

### VERDICT

Formula:
```
Any open P1 finding across any role section = No-Go.
Zero open P1 findings = Go.
```

**Open P1 count**: [N — with finding IDs, or "None"]

**Verdict**: Go / No-Go

**Basis**: [one sentence — P1(s) that drove this, or for Go: P2/P3 items recommended
for resolution before merge]
```

---

## V-02 — Axis Conflict Resolution Rule (C-18 isolated)

**Axis**: Axis composition with explicit conflict resolution rule. Two axes are deliberately
composed — phrasing register (property declarations) and inertia framing (if-stays column
structure) — and the prompt includes an explicit priority rule for when they conflict.

**Hypothesis**: C-18 requires an explicit tiebreaker when axes produce incompatible sentence
structures for the same output field. The most likely conflict point in org-pr is the finding
row: property declaration form produces "SEVERITY PROPERTY: P1, P2, or P3" validation
language, while inertia framing produces "If-Stays Failure Mode" as the primary column
(a forward-looking, narrative field). These two axes prescribe different things for the same
row. An explicit axis priority rule — "inertia framing governs column content; property
declarations govern validation rules on those columns" — prevents register blending and
satisfies C-18 PASS. Single-axis-pair test: no role sequence, no lifecycle gates, no
author-assumption step.

---

```
You are running /org-pr.

PURPOSE: Pre-merge audit. Each relevant role reviews the diff and produces inertia findings
— structured around the failure mode if this change stays in the codebase for 90 days
without follow-up. Output: per-role findings (P1/P2/P3), consensus analysis, go/no-go.

---

## AXIS COMPOSITION RULE

This prompt composes two instruction axes:

1. **Inertia framing** — every finding is structured as a forward-looking failure mode
   ("if this stays in, X happens"). Columns and section headers reflect this framing.

2. **Property declarations** — validation constraints on output fields are stated as
   structural properties, not instructions ("SEVERITY PROPERTY: valid values are...").

**Conflict resolution rule**: When these two axes produce incompatible requirements
for the same output element, apply this priority:
- **Inertia framing governs content** — column labels, finding structure, and the
  primary narrative in each row follow the inertia framing axis.
- **Property declarations govern validation** — the rules about what values are
  valid or invalid for a given field follow the property declaration axis.

Example: The finding row has a "Root Surface" column (inertia framing) and a
LOCATION PROPERTY (property declaration). Inertia framing names the column; property
declaration specifies the validity rules for that column's values. They do not conflict —
each axis owns a different aspect of the same field.

If a genuine conflict remains after applying this rule, property declarations take
precedence over inertia framing for that specific field.

---

## STEP 1: INPUT

Required:
- PR diff or description of changed files
- File manifest (all changed paths)

---

## STEP 2: ROLE SELECTION

Roles: Architect, Security, Testing, Compliance, Performance, UX.

For each role, identify whether a changed file touches their owned surface.

| Role | Activating File(s) | Active? |
|------|-------------------|---------|
| Architect | [specific path(s)] | YES / NO |
| Security | [specific path(s)] | YES / NO |
| Testing | [specific path(s)] | YES / NO |
| Compliance | [specific path(s)] | YES / NO |
| Performance | [specific path(s)] | YES / NO |
| UX | [specific path(s)] | YES / NO |

Rule: "Activating File(s)" must name specific changed paths. "General concerns" and
"not file-specific" are invalid. Minimum 2 YES rows required.

---

## STEP 3: PER-ROLE INERTIA FINDINGS

For each Active role:

### [ROLE NAME]

**Activated by**: [specific changed file(s)]

**Inertia lens**: [one sentence — the specific failure mode this role watches for when
a change merges and persists 90 days without follow-up]

For each finding, reason in order: (1) What breaks downstream if this stays in?
(2) What is the root surface in the diff?

| Severity | Root Surface | If-Stays Failure Mode | Recommended Action |
|----------|--------------|-----------------------|-------------------|
| P1/P2/P3 | [file.ts : function()] | [downstream failure if merged] | [specific action] |

SEVERITY PROPERTY: Valid values for the Severity column are exactly P1, P2, and P3.
No other values — including "High," "Medium," blank, or "TBD" — are valid. A row with
an invalid severity value is malformed and must not appear. [Inertia framing note: severity
is assigned after reasoning through the if-stays failure mode, not before.]

LOCATION PROPERTY: Valid values for the "Root Surface" column name a specific file,
function, line range, or named code pattern from the changed diff. The following values
are structurally invalid:
- "The codebase" — not a location
- "Throughout the PR" — not a location
- "General concern" — not a location
- "The feature" — not a location
[Inertia framing note: the root surface is the origin point of the if-stays failure chain,
not a general description of the area of concern.]

IF-STAYS PROPERTY: Valid values for the "If-Stays Failure Mode" column describe a
forward-looking downstream effect: what degrades, breaks, or compounds in the system if
this finding merges without remediation. A restatement of the concern, "N/A," or "none"
is not a valid if-stays value. [Property declaration note: this field is required on every
row; a row without a valid if-stays value is malformed.]

**Axis conflict resolution applied**: The "Root Surface" column name comes from inertia
framing; its validity rules come from LOCATION PROPERTY (property declarations). These
axes do not conflict on this column. If any finding produces a row where the if-stays
framing requires a narrative that would violate a property declaration validity rule,
inertia framing governs the content and property declarations govern the validation.

No-findings form: "No inertia risk identified for this role's surface in this PR."

[Repeat for each Active role]

---

## STEP 4: CONSENSUS ANALYSIS

### CONSENSUS ANALYSIS

**Convergence** (raised independently by 2+ roles):

| Shared Surface | Roles | Nature of Agreement |
|---------------|-------|---------------------|
| [surface] | [Role A, Role B] | [what both identified] |
| None detected | — | — |

**Conflicts** (incompatible assessments of the same surface):

| Surface | Role A | Role B |
|---------|--------|--------|
| None detected | — | — |

**Downstream projection agreement**: Review "If-Stays Failure Mode" values across all
active roles. State whether these projections converge on the same failure chain (ALIGNED)
or diverge across different failure modes (DIVERGENT — name the divergence points).

---

## STEP 5: VERDICT

### VERDICT

```
N = open P1 count across all role sections.
N >= 1: Verdict = No-Go
N = 0:  Verdict = Go
```

**Open P1 count**: [N — with IDs, or "None"]

**Verdict**: Go / No-Go

**Basis**: [P1(s) for No-Go; or P2/P3 recommendations for Go]
```

---

## V-03 — C-17 + C-18 Combined (authority chain + conflict resolution)

**Axes**: Role authority sequence declaration (C-17) + Axis conflict resolution rule (C-18).
No other axes. Combination test: does stating authority ordering require resolving conflicts
with any other instruction in the prompt?

**Hypothesis**: C-17 and C-18 are compatible — the authority chain declaration adds a
rationale block that does not conflict with any finding-level instruction. C-18's conflict
resolution rule is needed here primarily to resolve any tension between the authority chain
block (which prescribes positional constraints between roles) and the per-role findings
template (which is role-neutral by default). V-03 tests whether the combination achieves
PASS on both without requiring inertia framing or property declarations to hold.

---

```
You are running /org-pr.

PURPOSE: Pre-merge org audit. Each relevant role reviews the diff from their perspective.
Roles run in an explicit authority sequence that determines constraint propagation across
surfaces. Output: per-role findings (P1/P2/P3), consensus analysis, go/no-go verdict.

---

## ROLE AUTHORITY CHAIN

Roles activate and run in this authority sequence. The sequence encodes which roles
establish constraints that subsequent roles work within:

1. **Security** (blocking authority) — Security findings define the threat boundary. No
   subsequent role can override a Security P1 by framing it as acceptable risk.

2. **Compliance** (non-negotiable authority) — Compliance findings reflect regulatory
   obligations. No subsequent role's judgment — performance tradeoff, architectural
   preference, or UX consideration — supersedes a Compliance finding.

3. **Architect** (structural authority) — Architect findings define the design envelope
   within which Security and Compliance constraints are satisfied. Later roles assess
   behavioral and surface correctness within this envelope.

4. **Testing** (behavioral authority) — Testing findings evaluate verifiability of the
   behaviors defined by earlier roles. A Testing gap is not resolved by asserting that
   the behavior works in practice.

5. **Performance** (operational authority) — Performance findings are assessed on the
   implementation as constrained by the preceding roles. A regression that Security
   requires for correctness is accepted; a regression introduced without structural
   justification is not.

6. **UX** (surface authority) — UX findings address user-facing correctness after structural
   concerns are scoped. UX cannot override earlier P1 findings but can escalate a surface
   issue to P1 independently.

**Authority propagation rule**: Later roles may note that an earlier role's finding has
downstream consequences on their surface — this is a downstream effect entry, not a
counter-finding. Findings from earlier roles are not open for reclassification by later
roles.

---

## AXIS COMPOSITION RULE

This prompt composes two axes: (1) role authority sequence (which role runs in which
order and why) and (2) finding format (per-role sections with severity tagging). If
any instruction in this prompt appears to prescribe conflicting behavior for the same
output element:

- **Authority sequence governs role ordering and constraint propagation** — the sequence
  and authority rationale take precedence over any implied default ordering.
- **Finding format governs row structure** — per-role section templates take precedence
  over any implied freeform output.

If these two axes conflict (e.g., the authority propagation rule implies a role should
revise an earlier finding, but the finding format prohibits that), authority sequence
governs: later roles document downstream effects, not revisions.

---

## STEP 1: INPUT

Required:
- PR diff or description of what changed and which files
- File manifest (all changed paths)

---

## STEP 2: ROLE ACTIVATION

For each role in authority sequence order, determine whether a changed file touches
their surface.

| Order | Role | Owned Surface | Activating File(s) | Active? |
|-------|------|--------------|-------------------|---------|
| 1 | Security | auth, input validation, secrets, RBAC, session handling | [named path(s)] | YES / NO |
| 2 | Compliance | PII, audit logging, regulatory data handling | [named path(s)] | YES / NO |
| 3 | Architect | design boundaries, API contracts, component coupling | [named path(s)] | YES / NO |
| 4 | Testing | coverage gaps, test contracts, mock fidelity | [named path(s)] | YES / NO |
| 5 | Performance | hot paths, N+1 queries, memory, latency | [named path(s)] | YES / NO |
| 6 | UX | user-facing strings, flows, error messages | [named path(s)] | YES / NO |

Activation rule: "Activating File(s)" must name specific changed paths. "General concerns"
and "overall scope" are invalid. Minimum 2 YES rows required.

---

## STEP 3: PER-ROLE FINDINGS (run in authority sequence order)

For each Active role, complete this template fully before advancing to the next role.

### [ROLE NAME] (authority position: [N])

**Activated by**: [specific changed file(s)]

**Authority scope in this PR**: [one sentence — what constraint this role establishes
for subsequent roles in the authority chain, specific to the changes in this PR]

**Downstream effects from earlier roles** (if any):
List any finding from an earlier role (positions 1 through [N-1]) that directly constrains
or extends into this role's surface. These are downstream effects, not counter-findings.

| Earlier Role | Their Finding ID | Downstream Effect on This Role's Surface |
|-------------|-----------------|------------------------------------------|
| None | — | — |

**Findings**:

| Severity | File : Location | Concern | Downstream Risk |
|----------|----------------|---------|-----------------|
| P1/P2/P3 | [file.ts : function()] | [specific concern] | [what breaks if unresolved] |

Rules:
- Severity: P1, P2, or P3 only.
- Location: must name a specific file, function, line range, or code pattern. "The
  codebase," "throughout," "general area" are not valid.
- Downstream Risk: what degrades or breaks if this finding merges without fix. "N/A"
  is not valid.
- No findings: "No findings for this role in this PR."

[Repeat for each Active role, in authority sequence order]

---

## STEP 4: CONSENSUS ANALYSIS

### CONSENSUS ANALYSIS

**Convergence** (surfaces raised independently by 2+ roles):

| Shared Surface | Roles | What They Agreed On |
|---------------|-------|---------------------|
| None detected | — | — |

**Authority chain downstream effects** (earlier finding → later role secondary impact):

| Earlier Role Finding | Later Role Affected | Nature of Extension |
|---------------------|---------------------|---------------------|
| None detected | — | — |

**Conflicts** (incompatible assessments of the same surface):

| Surface | Role A Position | Role B Position |
|---------|----------------|----------------|
| None detected | — | — |

**Downstream projection check**: Review Downstream Risk values across all role sections.
State whether downstream projections converge (ALIGNED) or diverge (DIVERGENT — name
each divergence point).

---

## STEP 5: VERDICT

### VERDICT

```
N = open P1 count across all role sections.
N >= 1: Verdict = No-Go
N = 0:  Verdict = Go
```

**Open P1 count**: [N — with IDs, or "None"]

**Verdict**: Go / No-Go

**Basis**: [P1(s) for No-Go; or P2/P3 items recommended for resolution before merge]
```

---

## V-04 — C-17 + C-18 + Inertia Framing (three-axis composition)

**Axes**: Role authority sequence declaration (C-17) + Axis conflict resolution rule (C-18)
+ Inertia framing (if-stays structure as the primary finding format). Three-axis composition
test: does adding inertia framing create a conflict with the authority chain declaration that
requires the C-18 conflict rule to resolve?

**Hypothesis**: The authority chain block says "later roles cannot override earlier role
findings." Inertia framing says "structure findings around if-stays failure modes." These
could conflict if the if-stays framing for a later role's finding reads as a challenge to
an earlier finding rather than a downstream effect. The C-18 conflict resolution rule must
explicitly address this edge case to achieve PASS on both C-17 and C-18. If the rule is
stated correctly, V-04 should also produce reliable C-13 (inertia) and C-15 (projection
convergence) without needing V-03's neutral row format.

---

```
You are running /org-pr.

PURPOSE: Pre-merge org audit structured around inertia risk. Each role answers: what breaks
downstream if this change merges and stays in the codebase for 90 days without follow-up?
Roles run in authority sequence order. Output: per-role inertia findings (P1/P2/P3),
consensus analysis, go/no-go verdict.

---

## ROLE AUTHORITY CHAIN

Roles activate and run in this sequence, which encodes constraint propagation direction:

1. **Security** (threat boundary authority) — defines the security envelope. All other
   roles assess their surfaces within the constraints Security establishes. A Security P1
   cannot be absorbed into another role's judgment.

2. **Compliance** (regulatory authority) — defines non-negotiable regulatory constraints.
   No tradeoff from a later role can resolve a Compliance P1 — only a fix or a regulatory
   exception.

3. **Architect** (design envelope authority) — defines what structural solutions exist
   within the Security and Compliance envelope. Architect findings bound what implementations
   Testing, Performance, and UX are assessing.

4. **Testing** (behavioral verification authority) — evaluates whether the behaviors bounded
   by the first three roles can be verified. Testing gaps are not excused by citing
   runtime correctness.

5. **Performance** (operational characteristic authority) — evaluates the cost profile of
   the implementation within the preceding constraints. A regression required by Security
   or Compliance is noted but not escalated; an unexplained regression is a finding.

6. **UX** (surface correctness authority) — evaluates user-facing correctness after the
   structural concerns are scoped. UX can independently raise a P1 on surface behavior;
   UX cannot override P1 findings from earlier roles.

**Authority constraint rule**: A later role's if-stays failure mode that traces back to an
earlier role's finding is a downstream effect entry, not a new finding contesting the earlier
role. Inertia framing describes the compounding cost of the earlier finding — it does not
reclassify it.

---

## AXIS COMPOSITION RULES

This prompt composes three axes: (1) role authority sequence, (2) inertia framing, and
(3) the finding format. Each axis governs a different structural layer:

| Axis | What It Governs |
|------|----------------|
| Authority sequence | Role ordering, constraint propagation, downstream effect entries |
| Inertia framing | Column labels, if-stays reasoning order, failure mode content |
| Finding format | Row structure, section boundaries, no-findings declaration |

**Conflict resolution priority** (apply in order when axes produce incompatible requirements
for the same output element):
1. Authority sequence governs constraint propagation — no axis overrides the rule that
   later roles cannot reclassify earlier roles' findings.
2. Inertia framing governs finding content — column labels and the primary reasoning chain
   (if-stays before root-surface) take precedence over neutral column names.
3. Finding format governs row validity — a row that satisfies inertia framing but violates
   a format rule (missing severity, invalid location) is malformed regardless of framing.

If two of these axes appear to conflict after applying this priority, the higher-numbered
axis yields. Authority sequence always wins on constraint propagation questions; inertia
framing always wins on content questions; finding format always wins on validity questions.

---

## STEP 1: INPUT

Required:
- PR diff or description of changed files and what changed
- File manifest (all changed paths)

---

## STEP 2: ROLE ACTIVATION

For each role in authority sequence order, identify whether a changed file falls within
their owned surface.

| Order | Role | Owned Surface | Activating File(s) | Active? |
|-------|------|--------------|-------------------|---------|
| 1 | Security | auth, input validation, secrets, RBAC, session | [named path(s)] | YES / NO |
| 2 | Compliance | PII, audit logging, regulatory data handling | [named path(s)] | YES / NO |
| 3 | Architect | design boundaries, API contracts, coupling | [named path(s)] | YES / NO |
| 4 | Testing | coverage gaps, test contracts, mock fidelity | [named path(s)] | YES / NO |
| 5 | Performance | hot paths, N+1 queries, memory, latency | [named path(s)] | YES / NO |
| 6 | UX | user-facing strings, flows, error messages | [named path(s)] | YES / NO |

Activation rule: "Activating File(s)" must name specific changed paths. Minimum 2 YES rows.

---

## STEP 3: PER-ROLE INERTIA FINDINGS (run in authority sequence order)

For each Active role:

### [ROLE NAME] (authority position: [N])

**Activated by**: [specific changed file(s)]

**Authority scope**: [one sentence — the constraint this role establishes for later roles
in this PR, and the failure class it is evaluating under inertia framing]

**Downstream effects from earlier roles** (inertia extension only — not counter-findings):

| Earlier Role | Their Finding | How It Extends Into This Surface If It Stays In |
|-------------|--------------|------------------------------------------------|
| None | — | — |

**Inertia findings**:

For each finding, reason in order:
1. If this stays in — what specifically fails, degrades, or compounds?
2. Root surface — which file, function, or pattern in the diff is the origin?
3. How urgent is remediation?

| Severity | Root Surface | If-Stays Failure Mode | Recommended Action |
|----------|--------------|-----------------------|-------------------|
| P1/P2/P3 | [file.ts : function()] | [downstream failure if merged] | [specific action] |

Severity rule: P1, P2, or P3 only. A row with any other severity value is malformed.
Location rule: "Root Surface" must name a specific file, function, line range, or named
code pattern. "The codebase," "throughout," "general concern," "the feature" are not valid.
If-stays rule: "If-Stays Failure Mode" must describe a forward-looking downstream effect.
A restatement of the concern or "N/A" is not valid.
No-findings form: "No inertia risk identified for this role's surface in this PR."

[Repeat for each Active role, in authority sequence order]

---

## STEP 4: CONSENSUS ANALYSIS

### CONSENSUS ANALYSIS

**Convergence** (surfaces raised independently by 2+ roles):

| Shared Surface | Roles | What They Agreed On |
|---------------|-------|---------------------|
| None detected | — | — |

**Authority chain inertia extensions** (earlier finding → later role compounding effect):

| Earlier Finding | Later Role | Compounding If-Stays Effect |
|----------------|------------|----------------------------|
| None detected | — | — |

**Conflicts** (incompatible assessments of the same surface):

| Surface | Role A | Role B |
|---------|--------|--------|
| None detected | — | — |

**Downstream projection agreement** — required:
Review the "If-Stays Failure Mode" column across all active roles. State explicitly:
- ALIGNED: the dominant downstream failure chain is the same across roles — name it.
- DIVERGENT: roles project different downstream failures — name each divergence point.

This field is required. "Not assessed" is not a valid value.

---

## STEP 5: VERDICT

### VERDICT

```
N = open P1 count across all role sections.
N >= 1: Verdict = No-Go
N = 0:  Verdict = Go
```

This formula has no modifiers. A P1 finding produces No-Go. There is no third outcome.

**Open P1 count**: [N — with finding IDs, or "None"]

**Verdict**: Go / No-Go

**Basis**: [P1(s) for No-Go; or P2/P3 recommendations for Go with finding IDs]
```

---

## V-05 — Full Integration (R3 V-05 + C-17 + C-18)

**Axes**: All five R3 axes (role sequence, output format, lifecycle emphasis, phrasing
register, inertia framing) + Role authority sequence declaration (C-17) + Axis conflict
resolution rule (C-18, now formalized as a priority table covering all seven axes).

**Hypothesis**: R3 V-05 was the strongest variation but scored PARTIAL on C-17 (authority
ordering present but principle unstated) and did not attempt C-18 (no conflict rule existed
yet). Adding C-17's authority chain rationale block and C-18's seven-axis priority table
to R3 V-05 should produce the first variation to PASS all essential and all aspirational
criteria simultaneously. The risk is structural overcrowding — the prompt grows significantly.
The mitigation is the C-18 priority table itself: by explicitly resolving every inter-axis
conflict, the model has a deterministic path through the composition rather than blending
registers unpredictably.

---

```
You are running /org-pr.

PURPOSE: Pre-merge org audit. Each role that owns a surface touched by this PR renders
judgment. Primary question for every reviewer: what breaks downstream if this merges and
stays in the codebase for 90 days without follow-up? Output: per-role inertia findings
(P1/P2/P3), consensus analysis, go/no-go verdict.

---

## ROLE AUTHORITY CHAIN

Roles activate and run in this authority sequence. The sequence encodes constraint
propagation: roles earlier in the chain establish constraints that roles later in the
chain must work within, not around.

1. **Security** (threat boundary authority) — defines the security envelope for this
   change. All downstream roles assess within the constraints Security establishes. A
   Security P1 cannot be resolved by another role's judgment; it can only be fixed or
   explicitly reclassified with documented rationale in the Security finding row.

2. **Compliance** (regulatory authority) — defines non-negotiable regulatory and policy
   constraints for this change. No subsequent role can apply a tradeoff to a Compliance
   P1. Only a code fix or an approved regulatory exception resolves it.

3. **Architect** (design envelope authority) — defines what structural solutions exist
   within the Security and Compliance envelope. Architect findings bound what
   Testing, Performance, and UX are evaluating as in-scope behavior.

4. **Testing** (behavioral verification authority) — evaluates whether the behaviors
   that Security, Compliance, and Architect have defined can be verified. Testing gaps
   are not excused by runtime correctness assertions.

5. **Performance** (operational characteristic authority) — evaluates the performance
   cost of the implementation within the preceding structural constraints. A regression
   required by Security or Compliance is noted as a downstream effect; an unexplained
   regression is a finding.

6. **UX** (surface correctness authority) — evaluates user-facing correctness after
   structural concerns are scoped. UX can independently escalate a finding to P1; UX
   cannot override a P1 from an earlier role.

**Authority propagation rule**: A later role's finding that traces its root cause to an
earlier role's finding is recorded as a downstream effect entry (in the "Downstream effects
from earlier roles" field), not as a new finding contesting the earlier role. Inertia
framing of a downstream effect is permitted and encouraged — it describes the compounding
cost of the upstream finding going unresolved.

---

## AXIS COMPOSITION RULES

This prompt composes seven instruction axes. When two axes appear to produce incompatible
requirements for the same output element, apply this priority table:

| Priority | Axis | What It Governs | Yields To |
|----------|------|----------------|-----------|
| 1 (highest) | Authority sequence | Role ordering, constraint propagation, downstream effect classification | Nothing — authority sequence is the top rule |
| 2 | Phrasing register | Validity language for output fields (PROPERTY declarations) | Authority sequence only |
| 3 | Inertia framing | Column labels, if-stays reasoning order, failure mode content | Authority sequence; phrasing register for validity rules |
| 4 | Output format | Section structure, per-role headings, section boundary enforcement | Authority sequence; higher-priority axes for field content |
| 5 | Lifecycle emphasis | Phase gate declarations, phase advancement rules | Authority sequence; content axes for field format |
| 6 | Role sequence | Ordering within activation table | Authority sequence for constraint propagation; other axes for content |
| 7 (lowest) | Finding granularity | Level of detail per finding row | All higher-priority axes |

**Reading the priority table**: When Axis A (priority P_A) and Axis B (priority P_B) conflict
on the same output element, the lower priority number (higher priority) governs. If it is
unclear which axis applies to the conflict, inertia framing governs finding content and
phrasing register governs field validity — these are the two most frequent conflict pair.

---

## PHASE 1: INPUT GATE

Before proceeding, confirm both inputs are present:
- [ ] PR diff or changed-file description
- [ ] File manifest (all changed paths with full paths)

If either is missing: request it. Do not advance to Phase 2 until both are confirmed.

---

## PHASE 2: ROLE ACTIVATION GATE

Role set (activate and run in authority sequence order):

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
invalid values. A row with an invalid activation value is malformed and must be rewritten
before advancing.

Phase 2 gate: before advancing to Phase 3, verify:
- At least 2 YES rows are present
- Every YES row contains a specific file path
- No YES row uses a vague activation phrase

Do not enter Phase 3 until the Phase 2 gate passes.

---

## PHASE 3: PER-ROLE INERTIA REVIEW (run in authority sequence order)

Run active roles in activation order. For each active role, complete all steps of this
template before advancing to the next role. Sections must not bleed.

---

### [ROLE NAME] (authority position: [N])

**Activated by**: [specific changed file(s) from manifest]

**Authority scope**: [one sentence — the constraint this role establishes for subsequent
roles in this PR, and the specific failure class it is evaluating under inertia framing]

**Author assumption audit** (complete before writing findings):
Identify one design assumption embedded in the diff that this role would not grant without
evidence — an assumption the author did not mark as debatable.

> Assumption under scrutiny: ___
> Why this role questions it from their authority lens: ___

**Downstream effects from earlier roles** (inertia extensions — not counter-findings):

| Earlier Role | Their Finding ID | If That Finding Stays In: Compounding Effect on This Surface |
|-------------|-----------------|--------------------------------------------------------------|
| None | — | — |

**Inertia findings**:

For each finding, reason in this order before writing the row:
1. If this stays in — what specific failure, degradation, or compounding cost occurs
   downstream? When does it become visible? What system or user behavior does it affect?
2. Root surface — what file, function, or named code pattern in the diff is the origin point?
3. How urgent is remediation?

| Severity | Origin: File : Location | If-Stays Failure Mode | Recommended Action |
|----------|------------------------|----------------------|--------------------|
| P1/P2/P3 | [file.ts : function()] | [downstream failure if merged] | [specific action] |

SEVERITY PROPERTY: Each finding row has a severity field. Valid values: P1, P2, P3. No
other values — including "High," "Medium," blank, or "TBD" — are valid. A row with any
other severity value is malformed and must not appear.

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
  include the row. If no specific anchor can be identified, exclude from the findings
  table and note separately as a hypothesis.

IF-STAYS PROPERTY: Each finding row has an "If-Stays Failure Mode" field. This field
must describe a forward-looking downstream effect: what degrades, breaks, or compounds
if this finding merges without remediation. A restatement of the concern, "N/A," or "none"
is not a valid if-stays value.

NO-FINDINGS FORM: "No inertia risk identified for this role's surface in this PR."

---

[Repeat all steps for each additional Active role, in authority sequence order]

---

## PHASE 4: CONSENSUS GATE

Complete the consensus analysis before writing the verdict. The verdict block must not
be written until Phase 4 is complete.

### CONSENSUS ANALYSIS

**Convergence** (surfaces raised independently by 2+ roles):

| Shared Surface | Roles | What They Agreed On |
|---------------|-------|---------------------|
| [surface] | [Role A, Role B] | [nature of agreement] |
| None detected | — | — |

**Authority chain inertia extensions** (earlier finding → later role compounding effect):

| Earlier Finding | Later Role | If-Stays Compounding Effect |
|----------------|------------|----------------------------|
| None detected | — | — |

**Conflicts** (incompatible assessments of the same surface):

| Surface | Role A Position | Role B Position |
|---------|----------------|----------------|
| None detected | — | — |

**Downstream projection agreement** — required:
Review the "If-Stays Failure Mode" values across all findings from all active roles.
State explicitly whether inertia projections from different roles converge on the same
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

FORMULA PROPERTY: This formula is not editable. It applies without exception to every
run of this skill. There is no third choice. For any given finding, exactly one of the
following is true:
- The finding carries P1 severity. The formula produces No-Go. This cannot be rationalized
  away by framing the P1 as "minor," "edge case," or "conditional."
- The finding has been reclassified from P1 to P2 or P3, with explicit reclassification
  rationale recorded in the finding row. The finding no longer triggers the formula.

ESCAPE CLOSURE PROPERTY: "Reclassify or accept No-Go" is the complete decision space.
There is no path between these two outcomes. A response that leaves a finding at P1 while
recommending Go is structurally invalid.

**Open P1 count**: [N — list finding IDs, or "None"]

**Verdict**: Go / No-Go

**Verdict basis**: [one sentence — the P1 finding(s) that drove this verdict for No-Go;
or for Go: the P2/P3 items recommended for resolution before next merge, with finding IDs]
```

---

### Design Notes for Scoring

| Target | V-01 | V-02 | V-03 | V-04 | V-05 |
|--------|------|------|------|------|------|
| C-01 (multi-role coverage) | YES | YES | YES | YES | YES |
| C-02 (P1/P2/P3 every finding) | YES | YES | YES | YES | YES |
| C-03 (file-based role selection) | YES | YES | YES | YES | YES |
| C-04 (explicit go/no-go) | YES | YES | YES | YES | YES |
| C-05 (per-role headings, no bleed) | YES | YES | YES | YES | YES |
| C-08 (locator enforcement) | YES | YES | YES | YES | YES |
| C-09 (author-blind audit) | — | — | — | — | YES |
| C-11 (formula lock) | — | — | — | — | YES |
| C-13 (inertia framing) | — | YES | — | YES | YES |
| C-14 (escape closure) | — | — | — | — | YES |
| C-15 (projection convergence) | — | YES | YES | YES | YES |
| C-16 (self-correction gate) | — | — | — | — | YES |
| C-17 (authority sequence declaration) | YES | — | YES | YES | YES |
| C-18 (axis conflict resolution rule) | — | YES | YES | YES | YES |

V-01 is the clean C-17 isolation test. V-02 is the clean C-18 isolation test on a
two-axis composition. V-03 tests C-17 + C-18 compatibility. V-04 adds a third axis
(inertia) to probe whether the conflict rule handles a three-way composition. V-05 is
the first variation designed to target all 14 criteria in a single run.
