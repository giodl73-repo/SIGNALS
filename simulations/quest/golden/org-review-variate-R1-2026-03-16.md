# org-review Variations — Round 1 (New Rubric)
Generated: 2026-03-16
Skill: org-review
Rubric: simulations/quest/rubrics/org-review-rubric-2026-03-16.md

Prior rounds (old rubric, archived):
- R1–R6 (2026-03-15): explored bracket architecture, disposition algebra, CH-ID registers, scope gates
  under a 23-criterion multi-round rubric. Those findings inform the aspirational criteria C-09/C-10
  in this rubric, but the rubric has been simplified to 10 criteria with new essential/recommended splits.

Round 1 strategy (new rubric):
- Single-axis variations: V-01 (role sequence), V-02 (inertia framing), V-03 (output format)
- Combination variations: V-04 (phrasing register + lifecycle emphasis), V-05 (bracket architecture + disposition algebra)
- Golden path target: all 5 essential (C-01–C-05) + C-06 + C-07 + C-09 = 85 pts

---

## V-01 — Role Sequence: Null Hypothesis Gate Runs First

**Variation axis**: Role sequence — inertia-advocate always runs before any domain reviewer
**Hypothesis**: C-03 requires a null hypothesis verdict before domain testimony. Operationalizing this
as a hard role-sequence constraint (challenger step is structurally first, not optional, not embedded in
a later synthesis) is the cleanest way to guarantee C-03 never degrades to prose absorption. Domain
reviewers see an artifact that has already been challenged; they cannot reframe the null hypothesis
evaluation by going first.

---

You are running `org-review` on the artifact provided below.

**Severity legend** (applies to all reviewers):
- HIGH: finding blocks commitment to proceed
- MEDIUM: commitment may proceed only after this finding is remediated
- LOW: advisory; commitment may proceed regardless

**Step 1 — Depth Mode and Role Selection**

Read `.craft/roles/signal/` to enumerate available reviewers.

- **Standard** (default): Select the roles most relevant to this artifact type based on each role's
  `expertise.relevance` field. Minimum 2 roles beyond the inertia-advocate. State your selection and
  one-sentence rationale per role.
- **`--depth deep`**: Include every role found in `.craft/roles/signal/`. State the total role count
  before proceeding.

All roles must come from `.craft/roles/signal/`. Do not invent roles.

**Step 2 — Null Hypothesis Gate (always runs first)**

Before any other reviewer speaks, run the `inertia-advocate` review. This step is not optional and
not reorderable. The inertia-advocate argues the case for doing nothing — for the team keeping its
current workflow and not adopting this feature.

From the inertia-advocate's role file, apply:
- `lens.verify`: What is the team doing today instead of this? Is the existing workaround genuinely
  worse? Has anyone spoken with non-adopters?
- `lens.simplify`: The inertia case is the default. Name what the team does today before naming
  anything else.
- `expertise`: switching cost quantification, null hypothesis construction, adoption friction.

Produce the inertia-advocate entry:
```
### Null Hypothesis Gate — inertia-advocate
**Null hypothesis**: [state what the team does today instead of this]
**Challenge**: [does the artifact defeat this hypothesis? state specifically what evidence is present
or absent]
**Findings**: [2–3 sentences from the inertia-advocate's lens]
**Severity**: HIGH | MEDIUM | LOW
**Recommendation**: [one concrete action the artifact must add or change to survive the inertia test]
**Verify Question**: [one question from the inertia-advocate's lens.verify]
**Null Hypothesis Verdict**: FAIL | CONDITIONAL | PASS
```

The verdict is a labeled field. FAIL means the artifact does not address the null hypothesis.
CONDITIONAL means it partially addresses it. PASS means it addresses it sufficiently.

**Step 3 — Domain Reviewer Sections**

After the Null Hypothesis Gate, run each remaining selected role. The domain reviewers have access
to the artifact only — they do not have access to the inertia-advocate's findings. Their sections
address domain concerns (decision sufficiency, technical feasibility, quality) independent of the
inertia framing.

For each domain reviewer:
1. Read the role's `lens.verify`, `lens.simplify`, and `expertise.depth` from its role file.
2. Produce findings from this role's specific frame. PM findings address decision and commitment
   questions. Architect findings address boundaries, feasibility, and complexity. Findings must not
   echo or rephrase the inertia-advocate's framing.
3. Output:

```
### [Role name] — [archetype]
**Findings**: [2–4 sentences, role-frame-specific]
**Severity**: HIGH | MEDIUM | LOW
**Recommendation**: [one concrete scoped action]
**Verify Question**: [one question from this role's lens.verify]
**Simplify**: [one thing from this role's lens.simplify this reviewer would cut or collapse]
```

Severity is calibrated independently per reviewer. If all domain reviewers share the same severity
level, re-examine — roles with different expertise routinely see different risk magnitudes.

**Step 4 — Consolidated Action Register**

After all reviewer sections, produce a consolidated action list. This is a synthesis artifact, not
a copy of recommendations. Each item:
- References the finding that generated it: `[role] / [finding summary]`
- Carries a disposition class: BLOCKED (resolve before any commitment), CONDITIONAL (resolve before
  proceeding), ADVISORY (may defer)
- Is a distinct action, not a restatement of the recommendation

Format:
```
## Action Register
| # | Disposition Class | Finding Reference | Action Required |
|---|-------------------|-------------------|-----------------|
| 1 | BLOCKED | inertia-advocate / null hypothesis not addressed | ... |
| 2 | CONDITIONAL | architect / boundary undefined | ... |
```

At minimum: one item per HIGH or MEDIUM finding across all reviewer sections.

**Step 5 — Cross-Role Summary and Disposition**

Write a synthesis section (5–8 sentences) that:
- Names the highest-severity finding across all reviewers
- Identifies any cross-role conflict (two reviewers whose recommendations are incompatible) — name
  the roles and the tension explicitly
- References the Null Hypothesis Verdict from Step 2
- Explains (not just states) the overall disposition

Close with:
```
DISPOSITION: READY | CONDITIONAL | BLOCKED
```

DISPOSITION must be consistent with finding severities — it cannot be READY if any HIGH finding is
unresolved, unless an explicit override reason is stated.

**Artifact to review:**

{{artifact}}

---

## V-02 — Inertia Framing: Universal Null Hypothesis Anchor

**Variation axis**: Inertia framing — every reviewer (not only the inertia-advocate) must answer
the null hypothesis question from their own frame before giving domain findings
**Hypothesis**: C-03 requires a null hypothesis verdict before domain testimony, and C-01 requires
each role section to be substantively distinct. Requiring every reviewer to answer "what is the
inertia case from my frame, and does this artifact defeat it?" before giving domain findings forces
genuine role differentiation. The PM's answer to that question looks structurally different from the
architect's answer. This prevents the most common C-01 failure: role sections that say the same
thing in different vocabulary.

---

You are running `org-review` on the artifact provided below.

The shared premise for every reviewer: the team does nothing. They keep the current workflow.
They do not adopt this feature, proposal, or spec. The artifact's job is to defeat this premise.
Every reviewer's job is to evaluate how well it does — from their own frame, not from a shared frame.

**Severity semantics** (stated once, applies throughout):
- HIGH: this finding blocks commitment to proceed
- MEDIUM: commitment may proceed only after remediation
- LOW: advisory; proceed regardless

**Step 1 — Role Selection**

Read `.craft/roles/signal/` to enumerate available reviewers.
- **Standard** (default): Select 2–4 roles whose `expertise.relevance` matches this artifact type.
  State your selection with one-sentence rationale per role. The inertia-advocate must always be
  included.
- **`--depth deep`**: Include all roles in `.craft/roles/signal/`. State the count.

**Step 2 — Per-Reviewer Sections**

For each selected reviewer, produce a three-part entry. The three parts must appear in this order.

**Part A — Null Hypothesis Stance**

This reviewer answers one question from their own frame:
*Does this artifact defeat the null hypothesis — the case for doing nothing?*

The frame is role-specific:
- **inertia-advocate frame**: What is the team doing today? Is the current workaround genuinely
  worse? Is the switching cost acknowledged?
- **PM / product frame**: Is the evidence strong enough to justify building over doing nothing?
  Are the named customers real? Is the inertia case named anywhere in the artifact?
- **Architect / technical frame**: Is the technical complexity actually justified by the stated
  problem? Could the current workaround be extended more cheaply?
- **Other roles**: state the null hypothesis question this role cares about, then answer it.

Part A must produce one of: DEFEATS NULL / PARTIAL / DOES NOT DEFEAT — as a labeled verdict.
Part A answers must be substantively different across reviewers. They may not all open from the same
concern.

**Part B — Domain Findings**

2–3 findings from this role's `lens.verify` and `expertise.depth`. Do not repeat Part A. Do not
reference other reviewers' findings — this reviewer has not seen them.

**Part C — Severity, Recommendation, Verify Question**
```
**Severity**: HIGH | MEDIUM | LOW (one sentence of justification)
**Recommendation**: [one concrete action, in this role's voice]
**Verify Question**: [one question from this role's lens.verify]
```

**Step 3 — Null Hypothesis Verdict**

After all reviewer entries, produce a Null Hypothesis Verdict section before the final disposition:

```
## Null Hypothesis Verdict
**Aggregate null threat**: HIGH | MEDIUM | LOW
**Evidence that defeats it**: [what the artifact provides]
**Gap that keeps it alive**: [what is missing]
**Verdict**: DEFEATS NULL | PARTIAL | DOES NOT DEFEAT NULL
```

This section synthesizes Part A verdicts across all reviewers. It is not a copy of any single
reviewer's answer.

**Step 4 — Consolidated Action Register**

Produce a consolidated list. Each item:
- Traces to a specific reviewer + finding
- Carries disposition class: BLOCKED / CONDITIONAL / ADVISORY
- Is an action, not a restatement

```
## Action Register
| # | Class | Source | Action |
|---|-------|--------|--------|
```

At minimum one BLOCKED or CONDITIONAL item per HIGH or MEDIUM finding.

**Step 5 — Integrating Summary and Disposition**

Write a synthesis section (5–8 sentences):
- Name the highest-severity finding
- Name any cross-role conflict — where two reviewers' recommendations are incompatible
- Reference the Null Hypothesis Verdict explicitly
- Explain why the disposition is what it is, not merely what it is

```
DISPOSITION: READY | CONDITIONAL | BLOCKED
```

DISPOSITION may not contradict any unresolved HIGH finding.

**Artifact to review:**

{{artifact}}

---

## V-03 — Output Format: Severity Legend + Labeled Fields + Traceable Action Register

**Variation axis**: Output format — the output structure enforces C-02, C-04, and C-05 through
rigid labeled fields that cannot be omitted without a visible structural gap
**Hypothesis**: C-02 (severity semantics defined), C-04 (labeled disposition field), and C-05
(traceable action items) all fail the same way — the required element is present in prose but
not emittable as a discrete, scannable artifact. Enforcing labeled fields for severity legend,
disposition, and action register makes these failures structurally impossible: missing a field
leaves a visible blank in a table or header, forcing the evaluator to fill it.

---

You are running `org-review` on the artifact provided below.

**Preamble — Severity Legend**

The following severity semantics apply throughout this review. Every severity label in every
reviewer section is interpretable against this legend.

| Severity | Commit-gate meaning |
|----------|---------------------|
| HIGH | Blocks commitment to proceed. Work cannot advance until this finding is resolved. |
| MEDIUM | Conditions commitment. Work may proceed only after this finding is remediated. |
| LOW | Advisory. Work may proceed; resolution is recommended but not required before commitment. |

**Step 1 — Depth Mode and Role Selection**

Read `.craft/roles/signal/`. Enumerate available roles.

- **Standard** (default): Select roles relevant to this artifact type. State selection rationale
  (one sentence per role). The inertia-advocate must always be included.
- **`--depth deep`**: Include all roles. State total count.

State depth mode before proceeding:
```
Depth mode: standard | deep
Selected roles: [list]
Selection rationale: [one sentence per role, standard mode only]
```

**Step 2 — Null Hypothesis Gate**

Before domain reviewer sections, run the null hypothesis gate. This is a standalone section.

```
## Null Hypothesis Gate
**Status quo**: [what the team does today instead of this artifact]
**Challenge**: [does the artifact address the status quo case?]
**Challenger role**: inertia-advocate
**Verdict**: FAIL | CONDITIONAL | PASS
```

FAIL: artifact does not address the null hypothesis.
CONDITIONAL: artifact partially addresses it.
PASS: artifact sufficiently addresses it.

Domain reviewer sections begin only after this section is complete.

**Step 3 — Review Matrix**

For each selected role, produce an entry with these exact labeled fields. No field may be omitted.

```
## Reviewer: [role name]
**Archetype**: [from role file]
**Findings**: [2–4 sentences from this role's lens.verify and expertise.depth. Must not echo
  the inertia-advocate's framing or repeat findings from other roles.]
**Severity**: HIGH | MEDIUM | LOW
**Recommendation**: [one concrete scoped action]
**Verify Question**: [one question from this role's lens.verify]
**Simplify**: [one thing from lens.simplify this reviewer would remove or collapse]
```

Cross-check: if all reviewers carry identical severity levels, re-examine — roles with different
expertise routinely see different risk magnitudes.

**Step 4 — Action Register**

Produce the following table. Every HIGH or MEDIUM finding must produce at least one row.

```
## Action Register
| # | Disposition Class | Finding Reference | Required Action |
|---|-------------------|-------------------|-----------------|
```

Disposition classes:
- BLOCKED: must resolve before any commitment
- CONDITIONAL: must resolve before proceeding
- ADVISORY: may defer

Finding Reference format: `[role] / [finding in 5 words or fewer]`

The Action Register is a synthesis — do not copy recommendation text verbatim.

**Step 5 — Integrating Summary**

Write a synthesis section (5–8 sentences):
- Name the most important cross-role finding
- Name any cross-role conflict (incompatible recommendations from two roles)
- Reference the Null Hypothesis Gate verdict
- Explain the disposition — why this disposition, not just what it is

**Step 6 — Disposition**

Emit a labeled disposition field. This field appears on its own line, after the Integrating Summary.

```
DISPOSITION: READY | CONDITIONAL | BLOCKED
```

- READY: all HIGH findings resolved or zero
- CONDITIONAL: MEDIUM findings remain; no unresolved HIGH
- BLOCKED: one or more HIGH findings unresolved

The Disposition must not contradict the Null Hypothesis Gate verdict. A FAIL at the gate produces
at minimum CONDITIONAL.

**Artifact to review:**

{{artifact}}

---

## V-04 — Combination: Formal Register + Lifecycle Emphasis

**Variation axes**: Phrasing register (formal/technical) + lifecycle emphasis (explicit numbered
phases with scope as Phase 0 structural gate)
**Hypothesis**: Formal technical register — treating the skill as a bounded operation with
observable phases — closes two recommended criteria simultaneously: C-06 (scope declared before
review begins) and C-08 (depth parameter honored and acknowledged). Numbered phases with input/
output contracts make structural omissions visible as incomplete state transitions rather than
prose gaps. This is the lowest-overhead path to all 5 essential + C-06 + C-08 without reaching
for the aspirational bracket architecture.

---

You are executing the `org-review` skill. This skill distributes an artifact to a set of
organizational reviewers drawn from the role registry at `.craft/roles/signal/`. Each reviewer
applies their designated lens and returns a structured finding. The output is a review matrix
and disposition suitable for decision-making.

**Severity semantics** (applies throughout this review):
- HIGH: finding blocks commitment to proceed
- MEDIUM: commitment may proceed only after remediation
- LOW: advisory; proceed regardless

---

**Phase 0: Scope Declaration**

Input: the artifact provided below.

Enumerate what is under review:
```
IN SCOPE:
- Artifact: [name / version / type]
- Surfaces: [e.g., spec text, design constraints, prior decisions named in the artifact]

OUT OF SCOPE:
- [surfaces not being reviewed in this pass]
```

Scope is fixed before any reviewer section executes. If a reviewer discovers an artifact or
dependency not listed in scope, it is flagged as a scope gap in that reviewer's findings —
it is not silently incorporated into scope.

---

**Phase 1: Reviewer Selection**

Input: `.craft/roles/signal/` directory
Depth parameter: {{depth}} (`standard` | `deep`)

Procedure:
1. Enumerate all role files in `.craft/roles/signal/`.
2. If `standard`: apply relevance filter — read each role's `expertise.relevance` and select roles
   matching this artifact type. Minimum selection: 2 roles. The inertia-advocate is always included.
   Document selection rationale (one sentence per role).
3. If `deep`: include all enumerated roles without filtering. Document total count.

Output:
```
Depth mode: [standard | deep]
Reviewer manifest:
  - [role]: [archetype] — [selection rationale or "deep run — all roles"]
  ...
```

No role may be invented. Every reviewer must have a corresponding file in `.craft/roles/signal/`.

---

**Phase 2: Null Hypothesis Gate**

Procedure: run the inertia-advocate's lens before domain reviewer sections execute.

Input: inertia-advocate role file, artifact.
Output:
```
## Phase 2 — Null Hypothesis Gate
Reviewer: inertia-advocate
Status quo: [what the team does today in place of this artifact]
Challenge: [does the artifact name and address the status quo case?]
Severity: HIGH | MEDIUM | LOW
Verdict: FAIL | CONDITIONAL | PASS
```

FAIL: artifact does not address the null hypothesis.
CONDITIONAL: artifact partially addresses it; named gaps exist.
PASS: artifact sufficiently addresses the status quo case.

Domain sections (Phase 3) begin only after this verdict is emitted.

---

**Phase 3: Review Execution**

For each reviewer in the Phase 1 manifest (excluding the inertia-advocate, already executed in
Phase 2), execute this procedure:

3a. Load role file from `.craft/roles/signal/{role}.md`.
3b. Extract: `orientation.frame`, `lens.verify`, `lens.simplify`, `expertise.depth`.
3c. Apply the orientation frame to the artifact. The frame determines which artifact properties
    are salient to this reviewer.
3d. Generate findings from this frame. Findings must not duplicate the framing of another reviewer
    in this phase. Cross-role finding homogeneity is a structural defect.
3e. Classify findings by severity per the legend above.
3f. Formulate one recommendation: concrete, scoped, from this role's expertise.
3g. Formulate one verify question from `lens.verify`.
3h. Apply `lens.simplify`: name one element the artifact should remove or collapse.

Output per reviewer:
```
## Phase 3 — Reviewer: [role] ([archetype])
**Findings**: [2–4 sentences, frame-specific, non-echoing]
**Severity**: HIGH | MEDIUM | LOW
**Recommendation**: [action]
**Verify Question**: [question]
**Simplify**: [observation]
```

---

**Phase 4: Action Register**

Consolidate all HIGH and MEDIUM findings into a traceable action list.

```
## Phase 4 — Action Register
| # | Class | Finding Reference | Action |
|---|-------|-------------------|--------|
```

- Class: BLOCKED | CONDITIONAL | ADVISORY
- Finding Reference: [phase] / [role] / [5-word summary]
- Action: synthesis — not verbatim recommendation copy

Minimum: one row per HIGH or MEDIUM finding.

---

**Phase 5: Synthesis and Disposition**

5a. Identify the highest-severity finding across all phases.
5b. Identify cross-role conflicts: two reviewers whose recommendations are incompatible. Name the
    roles and the decision required to resolve the tension.
5c. Identify areas of convergence: where multiple reviewers flag the same risk.
5d. Reference the Phase 2 null hypothesis verdict.
5e. Explain the disposition — the reasoning, not only the label.

```
## Phase 5 — Synthesis
[5–8 sentence synthesis addressing 5a–5e above]

DISPOSITION: READY | CONDITIONAL | BLOCKED
```

Disposition computation:
- BLOCKED if any unresolved HIGH finding exists
- CONDITIONAL if MEDIUM findings exist and no unresolved HIGH
- READY if all HIGH findings resolved and no MEDIUM findings remain

Disposition may not contradict a FAIL null hypothesis verdict without explicit override explanation.

---

**Artifact to review:**

{{artifact}}

---

## V-05 — Combination: Adversarial Bracket Architecture + Disposition Algebra Pre-Committed

**Variation axes**: Inertia framing (adversarial bracket — challenger runs before AND after domain
testimony) + lifecycle emphasis (disposition formula committed in preamble before any reviewer executes)
**Hypothesis**: C-09 (adversarial bracket) and C-10 (disposition algebra pre-committed) are the two
aspirational criteria. Together they represent the structural integrity mechanisms that prevent
post-hoc rationalization: C-10 forces the formula before evidence is visible, and C-09 gives the
challenger a second pass to reassess whether domain evidence actually answered the challenge —
with override authority. This is the maximum structural combination and should score all 5 essential
+ C-06 + C-07 + C-09 + C-10 = 95 pts if executed correctly.

---

You are running `org-review` on the artifact provided below.

**Severity Semantics** (fixed; applies throughout):
| Label | Commit-gate meaning |
|-------|---------------------|
| HIGH | Blocks commitment. Unresolved HIGH finding → BLOCKED disposition. |
| MEDIUM | Conditions commitment. No unresolved HIGH + MEDIUM present → CONDITIONAL. |
| LOW | Advisory. No MEDIUM or HIGH → READY. |

**DISPOSITION CONTRACT** (committed before any reviewer executes):

The following formula maps gate verdicts to overall disposition. This formula is applied mechanically
at synthesis time. The synthesis section does not produce a new formula — it applies this one.

```
DISPOSITION FORMULA:
  if   any gate verdict = FAIL              → DISPOSITION = BLOCKED
  elif any gate verdict = CONDITIONAL       → DISPOSITION = CONDITIONAL
  elif Bracket Closing = OVERRIDES (see §3) → DISPOSITION = BLOCKED
  elif all gate verdicts = PASS             → DISPOSITION = READY
  else                                      → DISPOSITION = CONDITIONAL (ambiguous gates)
```

Gate verdicts are emitted by: Bracket Opening (§1), domain reviewers (§2), Bracket Closing (§3).
The formula is the evaluator. Editorial judgment at summary time does not override it.

---

**§0 — Scope Declaration**

Before any reviewer section, declare:
```
IN SCOPE:
- Artifact: [name / type]
- Surfaces: [spec text, constraints, named prior decisions]
OUT OF SCOPE:
- [surfaces not reviewed in this pass]
```

Any surface discovered during review that is not listed above is flagged as a scope gap — not
silently incorporated.

---

**§1 — Depth Mode and Role Selection**

Read `.craft/roles/signal/`. Enumerate all roles.

- **Standard** (default): Select roles relevant to this artifact type. Minimum 2 domain roles.
  State selection and one-sentence rationale per role.
- **`--depth deep`**: Include all roles. State total count.

The `inertia-advocate` is reserved for §1.5 and §3 (Bracket Opening and Closing). It does not
appear in the domain reviewer list in §2.

---

**§1.5 — Bracket Opening: Challenger Pre-Domain Testimony**

This section runs before any domain reviewer. Domain reviewers do not have access to this section.

From the inertia-advocate role file, apply:
- `lens.verify`: status quo case, adoption friction, switching cost
- `expertise`: null hypothesis construction

```
## Bracket Opening — inertia-advocate
**Null hypothesis**: [what the team does today]
**Challenge to artifact**: [does the artifact name this? does it address it? is the evidence real?]
**Specific gap (if any)**: [what would need to be true for this artifact to defeat the null hypothesis]
**Severity**: HIGH | MEDIUM | LOW
**Verify Question**: [from inertia-advocate's lens.verify]
**Opening Verdict**: FAIL | CONDITIONAL | PASS
```

Domain reviewer sections begin only after the Opening Verdict is emitted.

---

**§2 — Domain Reviewer Sections**

Domain reviewers have access to the artifact only. They have not seen §1.5.

For each selected domain reviewer:

1. Read the role file from `.craft/roles/signal/{role}.md`.
2. Apply `orientation.frame` to the artifact. This frame determines which properties are salient.
3. Generate findings from this frame. A PM reviewer attends to decision sufficiency. An architect
   reviewer attends to boundary correctness. Findings must not echo the Bracket Opening framing
   or other domain reviewers.
4. Emit:

```
## Domain Reviewer: [role] ([archetype])
**Findings**: [2–4 sentences, frame-specific]
**Severity**: HIGH | MEDIUM | LOW
**Recommendation**: [one concrete action]
**Verify Question**: [from lens.verify]
**Simplify**: [one observation from lens.simplify]
**Gate Verdict**: FAIL | CONDITIONAL | PASS
```

Gate Verdict: does this reviewer pass the artifact for their domain concern?
- FAIL: the artifact fails a gate this reviewer owns
- CONDITIONAL: passes with named conditions
- PASS: passes cleanly

---

**§3 — Bracket Closing: Challenger Post-Domain Reassessment**

This section runs after all domain reviewer sections are complete. The inertia-advocate now
has access to all domain findings and reassesses whether domain evidence actually defeated
the null hypothesis from §1.5.

The Bracket Closing does not re-review the artifact from scratch. It answers one question:
*Do the domain findings together constitute sufficient evidence to defeat the null hypothesis
stated in §1.5?*

```
## Bracket Closing — inertia-advocate (post-domain reassessment)
**Null hypothesis restated**: [from §1.5]
**Domain evidence reviewed**: [name which domain reviewers' findings are relevant to the null hypothesis]
**Assessment**: [does the domain testimony defeat the null hypothesis? what is still missing?]
**Override authority**: if domain reviewers collectively PASS but the null hypothesis is still not
  addressed, the Bracket Closing may override with BLOCKED. State override explicitly if invoked.
**Closing Verdict**: DEFEATED | PARTIAL | NOT DEFEATED
**Override invoked**: YES | NO (if YES, state: "Bracket Closing overrides domain PASS — DISPOSITION = BLOCKED")
```

Closing Verdict feeds directly into the DISPOSITION FORMULA in the preamble.

---

**§4 — Action Register**

Consolidate all FAIL/CONDITIONAL gate verdicts from §1.5, §2, and §3 into a traceable action list.

```
## Action Register
| # | Class | Finding Reference | Action |
|---|-------|-------------------|--------|
```

- Class: BLOCKED | CONDITIONAL | ADVISORY
- Finding Reference: [§] / [role] / [5-word summary]
- Class derives from gate verdict: FAIL → BLOCKED, CONDITIONAL → CONDITIONAL, LOW finding → ADVISORY
- Actions are syntheses, not verbatim recommendation copies

Minimum: one row per FAIL or CONDITIONAL gate verdict.

---

**§5 — Integrating Summary and Disposition**

Write a synthesis section (5–8 sentences):
- Name the highest-severity finding
- Name any cross-role conflict (two domain reviewers whose recommendations are incompatible)
- Name areas of cross-role convergence
- Reference the Opening Verdict (§1.5) and the Closing Verdict (§3) explicitly
- Explain why the disposition follows from the gate verdicts

Apply the DISPOSITION FORMULA from the preamble to the gate verdicts. State which formula branch
applies.

```
FORMULA APPLIED: [state which branch of the DISPOSITION FORMULA applies and why]

DISPOSITION: READY | CONDITIONAL | BLOCKED
```

The Integrating Summary explains the disposition. It does not produce a new formula.

---

**Artifact to review:**

{{artifact}}
