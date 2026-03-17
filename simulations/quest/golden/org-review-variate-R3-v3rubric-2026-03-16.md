# org-review Variations — Round 3 (v3 rubric, 2026-03-16)
Generated: 2026-03-16
Skill: org-review
Rubric: simulations/quest/rubrics/org-review-rubric-v3-2026-03-16.md

Prior round summary:
- R1 (v1 rubric): V-05=95, V-04=90. Differentiators: C-09/C-10/C-11/C-12/C-13.
- R2 (v2 rubric): V-04=100 (C-12+C-13), V-03=97 (bracket). No variant passed C-14 or C-15.
- R2 retroactive (v3 rubric): V-04=110 (C-12+C-13+C-14+C-15), V-03=97. C-14/C-15 are the frontier.

Round 3 strategy:
- V-01: single axis -- C-14 (Gate Verdict column in action register); base is V-03 R2 formula-first structure
- V-02: single axis -- C-15 ({{reviewer_set}} injectable); base is V-01 R2 template variable structure
- V-03: single axis -- C-09 + C-11 (adversarial bracket + labeled override field); minimal clean bracket
- V-04: combination -- C-12 + C-13 + C-14 + C-15 (Gold path, no bracket overhead); deliberate rebuild
- V-05: full stack -- C-09 + C-10 + C-11 + C-12 + C-13 + C-14 + C-15; targeting 125/125

Expected score ladder (v3 rubric, 125 pts max):
  V-01: 60+30+5(C-14)=95                           -- Strong hi (all recommended assumed pass)
  V-02: 60+30+5(C-13)+5(C-15)=100                  -- Gold floor
  V-03: 60+20+5(C-09)+5(C-11)=90                   -- Gold floor (2/3 recommended assumed)
  V-04: 60+30+5(C-12)+5(C-13)+5(C-14)+5(C-15)=110  -- Gold
  V-05: 60+30+35=125                                -- Perfect

---

## V-01 -- Single Axis: Gate Verdict Column in Action Register (C-14)

**Variation axis**: Output format -- the action register table carries a dedicated `Gate Verdict`
column preserving the intermediate verdict from the producing gate alongside each action item,
making the derivation chain machine-auditable without re-reading reviewer narrative

**Hypothesis**: C-14 failed in all R2 variants except V-02 (positional slot in finding reference)
and V-04 (dedicated column). V-03 R2 scored 97 on a clean formula-first structure but used
`[section] / [role] / [5-word summary]` with no gate verdict slot -- a single structural absence.
This variation takes V-03 R2's formula-first architecture and makes exactly one change: the action
register table gains a `Gate Verdict` column between `#` and `Class`. The pre-stated disposition
formula already handles C-10. Adding C-14's column should push from 97 to ~102 without touching
any other mechanism.

---

You are running `org-review` on the artifact provided below.

**Disposition formula** (read before the review begins; the final disposition is derived by
evaluating this formula against gate verdicts -- do not assert the disposition, evaluate it):

```
Let G = {g_null, g_domain, g_lifecycle}
Each gi in {PASS, CONDITIONAL, FAIL}

BLOCKED      <-- exists gi = FAIL
CONDITIONAL  <-- (all gi != FAIL) AND (exists gi = CONDITIONAL)
READY        <-- all gi = PASS

Tiebreaker: g_null = FAIL always yields BLOCKED regardless of other verdicts.
A domain or lifecycle PASS does not override a challenger FAIL.
```

The review produces verdicts. The formula produces the disposition.

**Severity Legend** (applies throughout):

| Severity | Commit-gate meaning |
|----------|---------------------|
| HIGH | Blocks commitment to proceed |
| MEDIUM | Conditions commitment; proceed only after remediation |
| LOW | Advisory; proceed regardless |

---

**Step 1 -- Role Selection**

Read `.craft/roles/signal/` to enumerate available reviewers.

- **Standard** (default): Select one role per archetype slot -- CHALLENGER (inertia-advocate),
  DOMAIN (technical/architecture), LIFECYCLE (PM/program). Map each to a role in
  `.craft/roles/signal/` whose `expertise.relevance` matches this artifact type. State each
  assignment and one-sentence rationale.
- **`--depth deep`**: Fill each slot with all matching roles. State total count and slot
  distribution.

All reviewers must come from `.craft/roles/signal/`. Do not invent roles.

---

**Step 2 -- Null Hypothesis Gate**

Run the CHALLENGER role first, in isolation. Domain and lifecycle reviewers do not have access
to this section.

```
## Null Hypothesis Gate -- [CHALLENGER role name]
**Null hypothesis**: [what the team does today instead of building this -- one sentence]
**Artifact's response**: [yes / partial / no]
**Findings**: [2-3 findings from challenger's lens.verify: switching costs, workaround
  viability, adoption friction]
**Severity**: HIGH | MEDIUM | LOW
**Verify Question**: [one from challenger's lens.verify]
**Gate Verdict (g_null)**: PASS | CONDITIONAL | FAIL
```

Domain reviewer sections begin only after g_null is emitted.

---

**Step 3 -- Domain Reviewer**

For each DOMAIN role:

```
## Domain Reviewer: [role name] -- [archetype]
**Findings**: [2-4 findings from this role's lens.verify and expertise.depth; must not echo
  the null hypothesis gate framing]
**Severity**: HIGH | MEDIUM | LOW
**Recommendation**: [one concrete action from this role's expertise frame]
**Verify Question**: [one from this role's lens.verify]
**Simplify**: [one observation from this role's lens.simplify]
**Gate Verdict (g_domain)**: PASS | CONDITIONAL | FAIL
```

If depth = deep and multiple domain roles run, state `Gate Verdict (g_domain aggregate) =` the
worst verdict among all domain rows (FAIL > CONDITIONAL > PASS).

---

**Step 4 -- Lifecycle Reviewer**

For each LIFECYCLE role:

```
## Lifecycle Reviewer: [role name] -- [archetype]
**Findings**: [2-3 findings from this role's lens.verify and expertise.depth; commitment
  readiness, decision sufficiency, program concerns]
**Severity**: HIGH | MEDIUM | LOW
**Recommendation**: [one concrete action]
**Verify Question**: [one from this role's lens.verify]
**Simplify**: [one from this role's lens.simplify]
**Gate Verdict (g_lifecycle)**: PASS | CONDITIONAL | FAIL
```

---

**Step 5 -- Action Register**

Produce a consolidated action register. Every FAIL or CONDITIONAL gate verdict produces at
least one row. The `Gate Verdict` column records the intermediate verdict from the producing
gate -- do not omit it.

```
## Action Register

| # | Gate Verdict | Class | Finding Reference | Action Required |
|---|--------------|-------|-------------------|-----------------|
```

Column definitions:
- **Gate Verdict**: the verdict emitted by the gate that sourced this item (FAIL / CONDITIONAL /
  PASS). Copy from the gate section above -- do not reassign.
- **Class**: BLOCKED (from FAIL gate) | CONDITIONAL (from CONDITIONAL gate) | ADVISORY (from
  PASS gate with HIGH or LOW finding)
- **Finding Reference**: `[role] / [5-word summary]`
- **Action Required**: synthesis of the required action -- not verbatim recommendation copy

The Gate Verdict column is the machine-readable link between the derivation formula and each
action item. An auditor must be able to verify the Class assignment from Gate Verdict alone,
without re-reading reviewer narrative.

---

**Step 6 -- Formula Evaluation and Disposition**

Collect all gate verdicts:

| Gate | Role | Verdict |
|------|------|---------|
| Null Hypothesis (g_null) | [challenger role] | [verdict] |
| Domain (g_domain) | [domain role] | [verdict] |
| Lifecycle (g_lifecycle) | [lifecycle role] | [verdict] |

**Gate verdict set G** = { g_null=[_], g_domain=[_], g_lifecycle=[_] }

Evaluate the preamble formula:
- Any gi = FAIL? --> BLOCKED. Name the gate.
- No FAIL, any gi = CONDITIONAL? --> CONDITIONAL. List conditions in priority order.
- All PASS? --> READY.

Write a synthesis section (5-8 sentences): name the highest-severity finding, name any
cross-role conflict, name areas of convergence, reference the null hypothesis gate verdict
explicitly, explain the disposition.

```
FORMULA APPLIED: [state which branch and why]
DISPOSITION: READY | CONDITIONAL | BLOCKED
```

**Artifact to review:**

{{artifact}}

---

## V-02 -- Single Axis: {{reviewer_set}} as Injectable Template Variable (C-15)

**Variation axis**: Output format (template variables) -- extends C-13 by adding `{{reviewer_set}}`
as a third declared template variable alongside `{{artifact_id}}` and `{{depth}}`; the role
selection step branches on this variable; the acknowledgment block emits all three values

**Hypothesis**: C-15 requires three things: (1) `{{reviewer_set}}` declared as a template
variable, (2) the output acknowledgment block emits its value, (3) reviewers invoked are
consistent with the declared variable. V-01 R2 passed C-13 with `{{artifact_id}}` and `{{depth}}`
but did not declare `{{reviewer_set}}`. Adding exactly one new variable declaration, one
acknowledgment line, and one conditional branch in role selection should pass C-15 without any
other structural change. Base: V-01 R2's step-by-step structure. Single-axis question: does
`{{reviewer_set}}` alone push to 100?

---

**Template inputs:**

```
{{artifact_id}}   -- identifier or short name for the artifact under review
{{depth}}         -- depth mode: standard | deep
{{reviewer_set}}  -- reviewer configuration; "auto" to select by relevance, or a comma-separated
                     list of role names from .craft/roles/signal/ to run exactly
```

**Acknowledgment block (emit at the start of your output, before any review section):**

```
## Review Parameters
Artifact:      {{artifact_id}}
Depth mode:    {{depth}}
Reviewer set:  {{reviewer_set}}
```

---

You are running `org-review` on the artifact provided below.

**Severity Legend** (applies throughout):

| Severity | Commit-gate meaning |
|----------|---------------------|
| HIGH | Blocks commitment to proceed |
| MEDIUM | Conditions commitment; proceed only after remediation |
| LOW | Advisory; proceed regardless |

---

**Step 1 -- Depth Mode and Role Selection**

Read `.craft/roles/signal/`. Enumerate available roles.

Reviewer set input: `{{reviewer_set}}`
Depth input: `{{depth}}`

Procedure:
1. If `{{reviewer_set}}` is not "auto": use the named roles exactly. The inertia-advocate must
   still be included; if not named in `{{reviewer_set}}`, add it and note the addition.
2. If `{{reviewer_set}}` = "auto" and `{{depth}}` = "standard": select roles relevant to this
   artifact type based on each role's `expertise.relevance`. Minimum 2 domain roles. State
   one-sentence rationale per role.
3. If `{{reviewer_set}}` = "auto" and `{{depth}}` = "deep": include all roles in
   `.craft/roles/signal/`. State total count.

Emit before any reviewer section:

```
Depth mode: {{depth}}
Reviewer set: {{reviewer_set}}
Reviewer manifest:
  - [role]: [archetype] -- [rationale | "explicit set" | "deep run -- all roles"]
  ...
```

No role may be invented. Every reviewer must have a corresponding file in `.craft/roles/signal/`.

---

**Step 2 -- Null Hypothesis Gate**

Before any domain reviewer speaks, run the `inertia-advocate` review. This step is not optional.

```
## Null Hypothesis Gate -- inertia-advocate
**Null hypothesis**: [what the team does today instead of this artifact]
**Challenge**: [does the artifact name and address the status quo case?]
**Findings**: [2-3 findings from inertia-advocate's lens.verify]
**Severity**: HIGH | MEDIUM | LOW
**Verify Question**: [one from inertia-advocate's lens.verify]
**Gate Verdict**: FAIL | CONDITIONAL | PASS
```

FAIL: artifact does not address the null hypothesis.
CONDITIONAL: artifact partially addresses it.
PASS: artifact sufficiently addresses it.

Domain reviewer sections begin only after the Gate Verdict is emitted.

---

**Step 3 -- Review Matrix**

For each selected role (excluding the inertia-advocate, which ran in Step 2):

```
## Reviewer: [role name] ([archetype])
**Findings**: [2-4 findings from this role's lens.verify and expertise.depth; must not echo
  the inertia-advocate's framing or repeat findings from other reviewers]
**Severity**: HIGH | MEDIUM | LOW
**Recommendation**: [one concrete action]
**Verify Question**: [one from this role's lens.verify]
**Simplify**: [one observation from this role's lens.simplify]
**Gate Verdict**: FAIL | CONDITIONAL | PASS
```

Cross-check: if all reviewers share identical severity levels, re-examine.

---

**Step 4 -- Action Register**

Every HIGH or MEDIUM finding, and every FAIL or CONDITIONAL gate verdict, produces at least one
row. The finding reference includes role and finding summary.

```
## Action Register

| # | Disposition Class | Finding Reference | Required Action |
|---|-------------------|-------------------|-----------------|
```

Disposition Classes:
- BLOCKED: must resolve before any commitment
- CONDITIONAL: must resolve before proceeding
- ADVISORY: may defer

Finding Reference format: `[role] / [finding in 5 words or fewer]`

The Action Register is a synthesis -- do not copy recommendation text verbatim.

---

**Step 5 -- Integrating Summary**

Write a synthesis section (5-8 sentences):
- Name the highest-severity finding across all reviewers
- Name any cross-role conflict (incompatible recommendations from two roles)
- Name areas of cross-role convergence
- Reference the Null Hypothesis Gate verdict from Step 2
- Explain the disposition

---

**Step 6 -- Disposition**

Emit a labeled disposition field after the Integrating Summary:

```
DISPOSITION: READY | CONDITIONAL | BLOCKED
```

- READY: all gate verdicts = PASS and no HIGH finding remains
- CONDITIONAL: no FAIL gate; at least one CONDITIONAL gate or MEDIUM finding remains
- BLOCKED: one or more gate verdicts = FAIL

The Disposition must not contradict a FAIL null hypothesis verdict without explicit explanation.

**Artifact to review:**

{{artifact_id}} artifact content:

{{artifact}}

---

## V-03 -- Single Axis: Adversarial Bracket + Labeled Override Field (C-09 + C-11)

**Variation axis**: Inertia framing -- the challenger role runs twice (Bracket Opening before all
domain testimony, Bracket Closing after all domain sections), and the Bracket Closing contains a
mandatory `Override invoked: YES | NO` labeled boolean field emitted regardless of whether override
is exercised

**Hypothesis**: C-11 is vacuous without C-09, so both must be present. The critical lesson from
prior rounds: (a) the override field must be mandatory, not conditional on whether the challenger
decides to override; (b) the field must be a labeled boolean field, not prose embedded in the
closing narrative. R2-V03 R2 implemented this pattern and scored at Gold floor. This variation
re-implements it cleanly as a single-axis test without C-10 (disposition algebra), C-12, C-13,
C-14, or C-15. If C-09+C-11 alone reliably score 90+, the mechanism is validated for combination.

---

You are running `org-review` on the artifact provided below.

**Severity Semantics** (fixed; applies throughout):
- HIGH: blocks commitment to proceed
- MEDIUM: conditions commitment; proceed only after remediation
- LOW: advisory; proceed regardless

---

**§0 -- Scope Declaration**

Before any reviewer section, emit:

```
IN SCOPE:
- Artifact: [name / type]
- Surfaces: [spec text, design constraints, prior decisions named in the artifact]

OUT OF SCOPE:
- [surfaces not being reviewed in this pass]
```

Any surface discovered during review not listed here is flagged as a scope gap in that
reviewer's findings -- not silently incorporated into scope.

---

**§1 -- Role Selection**

Read `.craft/roles/signal/`. Enumerate all roles.

- **Standard** (default): Select roles relevant to this artifact type. Minimum 2 domain roles.
  State selection and one-sentence rationale per role. The inertia-advocate is reserved for
  §1.5 and §3 (Bracket Opening and Bracket Closing) -- it does not appear in the domain list.
- **`--depth deep`**: Include all roles. State total count.

---

**§1.5 -- Bracket Opening: Challenger Pre-Domain Testimony**

This section runs before any domain reviewer. Domain reviewers do not have access to this section.

```
## Bracket Opening -- inertia-advocate
**Null hypothesis**: [what the team does today instead of this]
**Challenge**: [does the artifact name and address the status quo case?]
**Specific gap (if any)**: [what must be true for this artifact to defeat the null hypothesis]
**Severity**: HIGH | MEDIUM | LOW
**Verify Question**: [from inertia-advocate's lens.verify]
**Opening Verdict**: FAIL | CONDITIONAL | PASS
```

Domain reviewer sections begin only after the Opening Verdict is emitted.

---

**§2 -- Domain Reviewer Sections**

Domain reviewers have access to the artifact only. They have not seen §1.5.

For each selected domain reviewer:

1. Read the role file from `.craft/roles/signal/{role}.md`.
2. Apply `orientation.frame` to the artifact. Generate findings from this frame.
3. Findings must not echo the Bracket Opening framing or other domain reviewers.
4. Emit:

```
## Domain Reviewer: [role] ([archetype])
**Findings**: [2-4 findings, frame-specific, non-echoing]
**Severity**: HIGH | MEDIUM | LOW
**Recommendation**: [one concrete action]
**Verify Question**: [from this role's lens.verify]
**Simplify**: [one observation from this role's lens.simplify]
**Gate Verdict**: FAIL | CONDITIONAL | PASS
```

---

**§3 -- Bracket Closing: Challenger Post-Domain Reassessment**

After all domain reviewer sections are complete, the inertia-advocate reassesses whether domain
evidence collectively defeats the null hypothesis from §1.5.

The Bracket Closing answers exactly one question: *Do the domain findings together constitute
sufficient evidence to defeat the null hypothesis stated in §1.5?*

The inertia-advocate carries override authority: if domain reviewers collectively PASS but the
null hypothesis remains unaddressed, the Bracket Closing may override with BLOCKED.

```
## Bracket Closing -- inertia-advocate (post-domain reassessment)
**Null hypothesis restated**: [from §1.5]
**Domain evidence reviewed**: [name which domain reviewers' findings speak to the null hypothesis]
**Assessment**: [does domain testimony defeat the null hypothesis? what is still missing?]
**Override authority**: The inertia-advocate may override a collective domain PASS if the null
  hypothesis remains unaddressed. State override explicitly if invoked.
**Closing Verdict**: DEFEATED | PARTIAL | NOT DEFEATED
**Override invoked**: YES | NO
```

This field is mandatory. Emit YES or NO regardless of whether override is exercised.
- If YES: append "Bracket Closing overrides domain PASS -- DISPOSITION = BLOCKED."
- If NO: domain verdicts stand.

Closing Verdict and Override invoked feed directly into the Disposition section.

---

**§4 -- Action Register**

Consolidate all FAIL and CONDITIONAL gate verdicts from §1.5, §2, and §3 into a traceable
action list.

```
## Action Register
| # | Class | Finding Reference | Action |
|---|-------|-------------------|--------|
```

- Class: BLOCKED | CONDITIONAL | ADVISORY
- Finding Reference: `[§] / [role] / [5-word summary]`
- BLOCKED class: sourced from FAIL gate verdicts or Override invoked: YES
- CONDITIONAL class: sourced from CONDITIONAL gate verdicts
- ADVISORY class: sourced from LOW-only findings at PASS gates
- Actions are syntheses, not verbatim recommendation copies

Minimum: one row per FAIL or CONDITIONAL gate verdict.

---

**§5 -- Integrating Summary and Disposition**

Write a synthesis section (5-8 sentences):
- Name the highest-severity finding
- Name any cross-role conflict
- Name areas of cross-role convergence
- Reference the Opening Verdict (§1.5) and the Closing Verdict (§3) explicitly
- State whether Override invoked = YES or NO and explain the consequence

Close with:

```
DISPOSITION: READY | CONDITIONAL | BLOCKED
```

Disposition logic:
- BLOCKED: any gate verdict = FAIL, OR Override invoked = YES in §3
- CONDITIONAL: no FAIL, no override; at least one CONDITIONAL gate verdict
- READY: all gate verdicts = PASS and Override invoked = NO

**Artifact to review:**

{{artifact}}

---

## V-04 -- Combination: CLASS DERIVATION CONTRACT + Three Template Variables + Gate Verdict Column (C-12 + C-13 + C-14 + C-15)

**Variation axes**: Lifecycle emphasis (class derivation contract pre-committed, C-12) + Output
format (three template variables declared: {{artifact_id}}, {{depth}}, {{reviewer_set}}, C-13
and C-15) + Action register format (Gate Verdict as dedicated column, C-14); Gold path without
bracket overhead

**Hypothesis**: V-04 R2 scored 110/125 by passing C-12, C-13, C-14, C-15 without bracket. That
prompt was discovered through iteration rather than deliberate design. This variation re-implements
the same combination from first principles: the CLASS DERIVATION CONTRACT is stated in the
preamble (C-12); all three template variables are explicitly declared and acknowledged (C-13 + C-15
simultaneously); the action register table has a dedicated Gate Verdict column (C-14); all 5
essential and all 3 recommended criteria are structurally enforced through Phase labels. With no
bracket, C-09/C-10/C-11 are out of scope. Target: 60+30+20=110.

---

**Template inputs:**

```
{{artifact_id}}   -- identifier or short name for the artifact under review
{{depth}}         -- depth mode: standard | deep
{{reviewer_set}}  -- reviewer configuration; "auto" to select by relevance, or a comma-separated
                     list of role names from .craft/roles/signal/ to run exactly
```

**Acknowledgment block (emit at the start of your output, before Phase 0):**

```
## Review Parameters
Artifact:      {{artifact_id}}
Depth mode:    {{depth}}
Reviewer set:  {{reviewer_set}}
```

---

You are executing the `org-review` skill. This skill distributes an artifact to a set of
organizational reviewers drawn from `.craft/roles/signal/`. Each reviewer applies their
designated lens and returns a structured finding. The output is a review matrix and disposition
suitable for commitment decisions.

**Severity Semantics** (applies throughout this review):

| Severity | Commit-gate meaning |
|----------|---------------------|
| HIGH | Blocks commitment to proceed |
| MEDIUM | Conditions commitment; proceed only after remediation |
| LOW | Advisory; proceed regardless |

**CLASS DERIVATION CONTRACT** (committed before any reviewer executes):

Action item classes in the Action Register derive mechanically from gate verdicts.
The evaluator does not re-assess class at synthesis time.

```
Gate verdict  -->  Action Item Class:
  FAIL         -->  BLOCKED      (must resolve before any commitment)
  CONDITIONAL  -->  CONDITIONAL  (must resolve before proceeding)
  PASS + HIGH  -->  CONDITIONAL  (HIGH finding retained as conditional even at PASS gate)
  PASS + LOW   -->  ADVISORY     (may defer; not blocking)
```

Any item in the Action Register whose class contradicts the gate verdict that sourced it is a
structural defect.

---

**Phase 0: Scope Declaration**

Enumerate what is under review before any reviewer section executes:

```
IN SCOPE:
- Artifact: {{artifact_id}}
- Surfaces: [spec text, design constraints, prior decisions named in the artifact]

OUT OF SCOPE:
- [surfaces not being reviewed in this pass]
```

Scope is fixed here. If a reviewer discovers an artifact or dependency not listed, flag it as a
scope gap in that reviewer's section -- do not silently incorporate it into scope.

---

**Phase 1: Reviewer Selection**

Input: `.craft/roles/signal/` directory
Depth parameter: `{{depth}}`
Reviewer set override: `{{reviewer_set}}`

Procedure:
1. Enumerate all role files in `.craft/roles/signal/`.
2. If `{{reviewer_set}}` is not "auto": use the named roles exactly. The inertia-advocate must
   still be included; if not named, add it and note the addition.
3. If `{{reviewer_set}}` = "auto" and `{{depth}}` = "standard": apply relevance filter --
   select roles whose `expertise.relevance` matches this artifact type. Minimum 2 domain roles.
   Inertia-advocate always included. Document selection rationale (one sentence per role).
4. If `{{reviewer_set}}` = "auto" and `{{depth}}` = "deep": include all enumerated roles.
   Document total count.

Output:

```
Depth mode: {{depth}}
Reviewer set: {{reviewer_set}}
Reviewer manifest:
  - [role]: [archetype] -- [selection rationale | "explicit set" | "deep run"]
  ...
```

No role may be invented. Every reviewer must have a corresponding file in `.craft/roles/signal/`.

---

**Phase 2: Null Hypothesis Gate**

Run the inertia-advocate lens before all domain reviewer sections.

```
## Phase 2 -- Null Hypothesis Gate
Reviewer: inertia-advocate
Status quo: [what the team does today in place of this artifact]
Challenge: [does the artifact name and address the status quo case?]
Findings: [2-3 sentences from inertia-advocate's lens.verify and expertise.depth]
Severity: HIGH | MEDIUM | LOW
Verify Question: [one from inertia-advocate's lens.verify]
Gate Verdict: FAIL | CONDITIONAL | PASS
```

Domain sections (Phase 3) begin only after this verdict is emitted.

---

**Phase 3: Review Execution**

For each reviewer in the Phase 1 manifest (excluding the inertia-advocate, already executed in
Phase 2):

3a. Load role file from `.craft/roles/signal/{role}.md`.
3b. Extract `orientation.frame`, `lens.verify`, `lens.simplify`, `expertise.depth`.
3c. Apply the orientation frame to the artifact. This frame determines which properties are salient.
3d. Generate findings from this frame. Findings must not duplicate the framing of another reviewer.
    Cross-role finding homogeneity is a structural defect.
3e. Classify findings by severity per the legend above.
3f. Formulate one recommendation: concrete, scoped, from this role's expertise.
3g. Formulate one verify question from `lens.verify`.
3h. Apply `lens.simplify`: name one element the artifact should remove or collapse.

Output per reviewer:

```
## Phase 3 -- Reviewer: [role] ([archetype])
**Findings**: [2-4 sentences, frame-specific, non-echoing]
**Severity**: HIGH | MEDIUM | LOW
**Recommendation**: [action]
**Verify Question**: [question]
**Simplify**: [observation]
**Gate Verdict**: FAIL | CONDITIONAL | PASS
```

---

**Phase 4: Action Register**

Using the CLASS DERIVATION CONTRACT from the preamble, consolidate all gate verdicts into a
traceable action list. The `Gate Verdict` column preserves the intermediate verdict so that the
class assignment can be verified row by row against the derivation contract without re-reading
reviewer narrative.

```
## Phase 4 -- Action Register
(Classes derived per CLASS DERIVATION CONTRACT -- no editorial re-assessment)

| # | Gate Verdict | Class | Finding Reference | Action |
|---|--------------|-------|-------------------|--------|
```

Column definitions:
- **Gate Verdict**: copy from the gate section that produced this item (FAIL / CONDITIONAL / PASS)
- **Class**: applied from the derivation contract, not re-assessed here
- **Finding Reference**: `[phase] / [role] / [5-word summary]`
- **Action**: synthesis -- not verbatim recommendation copy

Minimum: one row per FAIL or CONDITIONAL gate verdict.

---

**Phase 5: Synthesis and Disposition**

5a. Identify the highest-severity finding across all phases.
5b. Identify cross-role conflicts (two reviewers whose recommendations are incompatible).
5c. Identify convergence areas where multiple reviewers flag the same risk independently.
5d. Reference the Phase 2 null hypothesis gate verdict explicitly.
5e. Explain the disposition -- the reasoning, not only the label.

```
## Phase 5 -- Synthesis
[5-8 sentence synthesis addressing 5a-5e above]

DISPOSITION: READY | CONDITIONAL | BLOCKED
```

Disposition computation:
- BLOCKED: any gate verdict = FAIL
- CONDITIONAL: no FAIL; at least one gate verdict = CONDITIONAL
- READY: all gate verdicts = PASS

Disposition may not contradict a FAIL null hypothesis verdict without explicit override
explanation.

---

**Artifact to review:**

{{artifact_id}} artifact content:

{{artifact}}

---

## V-05 -- Full Stack: All Seven Aspirational Criteria (C-09 through C-15)

**Variation axes**: Adversarial bracket (C-09) + disposition algebra pre-committed (C-10) +
override field labeled (C-11) + class derivation contract (C-12) + three template variables
(C-13 + C-15) + Gate Verdict column (C-14); targeting 125/125

**Hypothesis**: V-04 R2 scored 110/125 (missing C-09, C-10, C-11 = 15 pts). V-05 R2 scored
~115 against the v2 rubric (missing C-14, C-15 = 10 pts in v3). No single variant has captured
all 7 aspirational criteria. This variation combines the clean Gold structure of V-04 R2 with
the bracket + algebra + override field from V-05 R2, plus three template variables (adding
`{{reviewer_set}}` for C-15) and a Gate Verdict column in the action register (C-14). The four
mechanisms are structurally independent: bracket handles null hypothesis architecture (C-09);
algebra handles disposition derivation (C-10); override field handles auditable override
decision (C-11); class derivation handles action item classification (C-12); template variables
handle automation (C-13 + C-15); Gate Verdict column handles derivation chain auditability
(C-14). Adding them to a sound essential+recommended base should reach 125.

---

**Template inputs:**

```
{{artifact_id}}   -- identifier or short name for the artifact under review
{{depth}}         -- depth mode: standard | deep
{{reviewer_set}}  -- reviewer configuration; "auto" to select by relevance, or a comma-separated
                     list of role names from .craft/roles/signal/ to run exactly
```

**Acknowledgment block (emit at the start of your output, before §0):**

```
## Review Parameters
Artifact:      {{artifact_id}}
Depth mode:    {{depth}}
Reviewer set:  {{reviewer_set}}
```

---

You are running `org-review` on the artifact provided below.

**Severity Semantics** (fixed; applies throughout):

| Label | Commit-gate meaning |
|-------|---------------------|
| HIGH | Blocks commitment. Unresolved HIGH finding -> BLOCKED disposition. |
| MEDIUM | Conditions commitment. No unresolved HIGH + at least one MEDIUM -> CONDITIONAL. |
| LOW | Advisory. No MEDIUM or HIGH -> READY. |

**DISPOSITION CONTRACT** (committed before any reviewer executes):

The following formula maps gate verdicts to overall disposition. The synthesis section evaluates
this formula -- it does not produce a new one.

```
DISPOSITION FORMULA:
  if   any gate verdict = FAIL                           --> DISPOSITION = BLOCKED
  elif Override invoked = YES  (see §3)                  --> DISPOSITION = BLOCKED
  elif any gate verdict = CONDITIONAL                    --> DISPOSITION = CONDITIONAL
  elif all gate verdicts = PASS                          --> DISPOSITION = READY
  else                                                   --> DISPOSITION = CONDITIONAL  (ambiguous)
```

Gate verdicts are emitted by: Bracket Opening (§1.5), domain reviewers (§2), Bracket Closing (§3).
The formula is the evaluator. Editorial judgment at summary time does not override it.

**CLASS DERIVATION CONTRACT** (committed before any reviewer executes):

Action item classes in the Action Register derive mechanically from gate verdicts:

```
Gate verdict  -->  Action Item Class:
  FAIL         -->  BLOCKED
  CONDITIONAL  -->  CONDITIONAL
  PASS + HIGH  -->  CONDITIONAL
  PASS + LOW   -->  ADVISORY
```

No item's class may be assigned editorially at synthesis time.

---

**§0 -- Scope Declaration**

Before any reviewer section, emit:

```
IN SCOPE:
- Artifact: {{artifact_id}}
- Surfaces: [spec text, design constraints, named prior decisions]

OUT OF SCOPE:
- [surfaces not reviewed in this pass]
```

Any surface discovered during review not listed above is flagged as a scope gap -- not silently
incorporated into scope.

---

**§1 -- Role Selection**

Read `.craft/roles/signal/`. Enumerate all roles.
Depth parameter: `{{depth}}`
Reviewer set override: `{{reviewer_set}}`

Procedure:
1. If `{{reviewer_set}}` is not "auto": use the named roles exactly. The inertia-advocate must
   still be included; if not named, add it and note the addition.
2. If `{{reviewer_set}}` = "auto" and `{{depth}}` = "standard": select roles relevant to this
   artifact type. Minimum 2 domain roles. State selection and one-sentence rationale per role.
3. If `{{reviewer_set}}` = "auto" and `{{depth}}` = "deep": include all roles. State total count.

The `inertia-advocate` is reserved for §1.5 and §3 (Bracket Opening and Closing). It does not
appear in the domain reviewer list for §2.

Output:

```
Depth mode: {{depth}}
Reviewer set: {{reviewer_set}}
Reviewer manifest:
  - [role]: [archetype] -- [rationale | "explicit set" | "deep run -- all roles"]
  ...
  (inertia-advocate: reserved for bracket positions)
```

No role may be invented. Every reviewer must have a corresponding file in `.craft/roles/signal/`.

---

**§1.5 -- Bracket Opening: Challenger Pre-Domain Testimony**

This section runs before any domain reviewer. Domain reviewers do not have access to this section.

From the inertia-advocate role file, apply `lens.verify` and `expertise.depth`:

```
## Bracket Opening -- inertia-advocate
**Null hypothesis**: [what the team does today]
**Challenge to artifact**: [does the artifact name this? address it? is the evidence real?]
**Specific gap (if any)**: [what must be true for this artifact to defeat the null hypothesis]
**Challenge to domain reviewers**: [one specific question domain reviewers must address to defeat
  this null hypothesis -- this is the anchor all downstream reviewers respond to]
**Severity**: HIGH | MEDIUM | LOW
**Verify Question**: [from inertia-advocate's lens.verify]
**Opening Verdict**: FAIL | CONDITIONAL | PASS
```

Domain reviewer sections begin only after the Opening Verdict is emitted.

---

**§2 -- Domain Reviewer Sections**

Domain reviewers have access to the artifact only. They have not seen §1.5.

For each selected domain reviewer:

1. Load role file from `.craft/roles/signal/{role}.md`.
2. Apply `orientation.frame` to the artifact. This frame determines which properties are salient.
3. Generate findings from this frame. A PM reviewer attends to decision sufficiency. An architect
   attends to boundary correctness and feasibility. Findings must not echo §1.5 framing or other
   domain reviewers. Cross-role finding homogeneity is a structural defect.
4. Emit:

```
## Domain Reviewer: [role] ([archetype])
**Null hypothesis address**: [from this role's frame, does the artifact defeat the null hypothesis?
  One sentence. Must differ from §1.5's framing.]
**Findings**: [2-4 sentences, frame-specific, non-echoing]
**Severity**: HIGH | MEDIUM | LOW
**Recommendation**: [one concrete action]
**Verify Question**: [from this role's lens.verify]
**Simplify**: [one observation from this role's lens.simplify]
**Gate Verdict**: FAIL | CONDITIONAL | PASS
```

---

**§3 -- Bracket Closing: Challenger Post-Domain Reassessment**

This section runs after all domain reviewer sections are complete. The inertia-advocate now has
access to all domain findings and reassesses whether domain evidence collectively defeats the
null hypothesis from §1.5.

The Bracket Closing answers one question: *Do the domain findings together constitute sufficient
evidence to defeat the null hypothesis stated in §1.5?*

The inertia-advocate carries override authority: if domain reviewers collectively PASS but the
null hypothesis remains unaddressed, the Bracket Closing may override with BLOCKED.

```
## Bracket Closing -- inertia-advocate (post-domain reassessment)
**Null hypothesis restated**: [from §1.5]
**Domain evidence reviewed**: [name which domain reviewers' findings are relevant to null
  hypothesis; summarize each reviewer's null hypothesis address in one sentence]
**Assessment**: [does domain testimony defeat the null hypothesis? what is still missing?]
**Override authority**: If domain reviewers collectively PASS but null hypothesis remains
  unaddressed, the Bracket Closing may override. State explicitly if invoked.
**Closing Verdict**: DEFEATED | PARTIAL | NOT DEFEATED
**Override invoked**: YES | NO
```

This field is mandatory. Emit YES or NO regardless of whether override is exercised.
- If YES: append "Bracket Closing overrides domain PASS -- DISPOSITION = BLOCKED per DISPOSITION
  CONTRACT."
- If NO: domain verdicts stand; Closing Verdict feeds DISPOSITION CONTRACT normally.

---

**§4 -- Action Register**

Using the CLASS DERIVATION CONTRACT from the preamble, consolidate all FAIL and CONDITIONAL gate
verdicts from §1.5, §2, and §3 into a traceable action list. The `Gate Verdict` column preserves
the intermediate verdict so the class assignment can be verified row by row without re-reading
reviewer narrative.

```
## Action Register
(Classes derived per CLASS DERIVATION CONTRACT -- no editorial re-assessment)

| # | Gate Verdict | Class | Finding Reference | Action |
|---|--------------|-------|-------------------|--------|
```

Column definitions:
- **Gate Verdict**: copy from the gate section that produced this item (FAIL / CONDITIONAL / PASS)
- **Class**: applied from the derivation contract, not re-assessed here
- **Finding Reference**: `[§] / [role] / [5-word summary]`
- **Action**: synthesis -- not verbatim recommendation copy

Additional rows:
- If Override invoked = YES in §3: add a BLOCKED row with Finding Reference `§3 / inertia-advocate
  / override invoked` regardless of domain gate verdicts.

Minimum: one row per FAIL or CONDITIONAL gate verdict.

---

**§5 -- Integrating Summary and Disposition**

Write a synthesis section (5-8 sentences):
- Name the highest-severity finding across all sections
- Name any cross-role conflict (two domain reviewers with incompatible recommendations)
- Name areas of cross-role convergence
- Reference the Opening Verdict (§1.5) and Closing Verdict (§3) explicitly
- State whether Override invoked = YES or NO and the consequence
- Explain why the disposition follows from the gate verdicts

Apply the DISPOSITION CONTRACT from the preamble. State which formula branch applies.

```
## §5 -- Synthesis
[5-8 sentence synthesis]

FORMULA APPLIED: [state which branch of the DISPOSITION CONTRACT applies and why]

DISPOSITION: READY | CONDITIONAL | BLOCKED
```

The Integrating Summary explains the disposition. It does not produce a new formula.

---

**Artifact to review:**

{{artifact_id}} artifact content:

{{artifact}}
