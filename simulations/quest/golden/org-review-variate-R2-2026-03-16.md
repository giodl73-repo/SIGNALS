# org-review Variations — Round 2 (v2 rubric)
Generated: 2026-03-16
Skill: org-review
Rubric: simulations/quest/rubrics/org-review-rubric-v2-2026-03-16.md

Prior rounds:
- R1 (new v2 rubric, 2026-03-16): single-axis and combination variations; V-04=95, V-05=105 lead.
  Three new v2 criteria (C-11/C-12/C-13) were the differentiators. V-04 passed C-13 only.
  V-05 passed C-09+C-10+C-11+C-12 but failed C-13. No variant passed all five aspirational.

Round 2 strategy:
- V-01: single axis — C-13 (template variables), output format axis
- V-02: single axis — C-12 (mechanical class derivation), lifecycle emphasis axis
- V-03: single axis — C-11 via C-09 (adversarial bracket + override labeled field), inertia framing axis
- V-04: combination — C-12 + C-13 without bracket; targeting Gold at 90+ without aspirational overhead
- V-05: full stack — C-09 + C-10 + C-11 + C-12 + C-13; V-05-R1 base + template variables; targeting 115

Expected score ladder:
  V-01: 60+20+5(C-13)=85 (Strong hi if recommended full, else lower)
  V-02: 60+20+5(C-12)=85
  V-03: 60+20+5(C-09)+5(C-11)=90 (Gold floor if all recommended pass)
  V-04: 60+30+5(C-12)+5(C-13)=100
  V-05: 60+30+25=115

---

## V-01 — Output Format: Template Variable Injection

**Variation axis**: Output format — declare review inputs as explicit template variables with an
acknowledgment block at execution start; C-13 is the sole aspirational target
**Hypothesis**: C-13 failed everywhere in R1 except V-04, which passed only because `{{depth}}`
was present. The rubric requires >= 2 variables (depth + artifact identity) plus an acknowledgment
block confirming injected values. V-03-R1 had clean essential coverage (75 pts) but no template
variables. Adding `{{depth}}` and `{{artifact_id}}` as declared inputs at the prompt top, and
emitting an acknowledgment block before Step 1, is sufficient to PASS C-13 without touching any
other structural element. Base: V-03-R1's rigid labeled-field structure.

---

**Template inputs:**

```
{{artifact_id}}  — identifier or short name for the artifact under review
{{depth}}        — depth mode: standard | deep
```

**Acknowledgment block (emit at the start of your output, before any review section):**

```
## Review Parameters
Artifact: {{artifact_id}}
Depth mode: {{depth}}
```

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

- **`{{depth}}` = standard** (default): Select roles relevant to this artifact type. State
  selection rationale (one sentence per role). The inertia-advocate must always be included.
- **`{{depth}}` = deep**: Include all roles. State total count.

Emit role selection before any reviewer section:
```
Depth mode: {{depth}}
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

For each selected role (excluding the inertia-advocate, already executed in Step 2), produce an
entry with these exact labeled fields. No field may be omitted.

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
- Reference the Null Hypothesis Gate verdict from Step 2
- Explain the disposition — why this disposition, not just what it is

**Step 6 — Disposition**

Emit a labeled disposition field after the Integrating Summary.

```
DISPOSITION: READY | CONDITIONAL | BLOCKED
```

- READY: all HIGH findings resolved or zero
- CONDITIONAL: MEDIUM findings remain; no unresolved HIGH
- BLOCKED: one or more HIGH findings unresolved

The Disposition must not contradict the Null Hypothesis Gate verdict. A FAIL at the gate produces
at minimum CONDITIONAL.

**Artifact to review:**

{{artifact_id}} artifact content:

{{artifact}}

---

## V-02 — Lifecycle Emphasis: Gate-to-Class Derivation Pre-Committed

**Variation axis**: Lifecycle emphasis — a CLASS DERIVATION CONTRACT is stated in the preamble
before any reviewer executes; action item classes are derived from gate verdicts, not re-assessed
editorially at synthesis time; C-12 is the sole aspirational target
**Hypothesis**: C-12 failed in all R1 variants except V-05. The fix is structural, not behavioral:
a pre-committed derivation rule in the preamble that the Action Register step names explicitly when
assigning classes. If the rule is there and the Register references it, an evaluator cannot assign
CONDITIONAL to a FAIL gate or soften a BLOCKED item. The base is V-01-R1's role-sequence structure
(clean essential coverage), with no bracket added. Single-axis target: can C-12 alone be reliably
passed by adding only the derivation contract?

---

You are running `org-review` on the artifact provided below.

**Severity Legend** (applies throughout):
- HIGH: finding blocks commitment to proceed
- MEDIUM: commitment may proceed only after this finding is remediated
- LOW: advisory; commitment may proceed regardless

**CLASS DERIVATION CONTRACT** (committed before any reviewer executes):

Action item classes in the Action Register are derived mechanically from gate verdicts.
The evaluator does not re-assess class at synthesis time.

```
Gate verdict → Action Item Class:
  FAIL         → BLOCKED      (must resolve before any commitment)
  CONDITIONAL  → CONDITIONAL  (must resolve before proceeding)
  PASS + HIGH  → CONDITIONAL  (HIGH finding remains actionable even at passing gate)
  PASS + LOW   → ADVISORY     (may defer)
```

This rule is applied at the Action Register step. Any item whose class contradicts the gate
verdict that sourced it is a structural defect.

---

**Step 1 — Depth Mode and Role Selection**

Read `.craft/roles/signal/` to enumerate available reviewers.

- **Standard** (default): Select the roles most relevant to this artifact type based on each
  role's `expertise.relevance` field. Minimum 2 domain roles. State your selection and
  one-sentence rationale per role. The inertia-advocate is always included.
- **`--depth deep`**: Include every role found in `.craft/roles/signal/`. State the total role
  count before proceeding.

All roles must come from `.craft/roles/signal/`. Do not invent roles.

**Step 2 — Null Hypothesis Gate (runs first)**

Before any other reviewer speaks, run the `inertia-advocate` review. This step is not optional
and not reorderable.

```
### Null Hypothesis Gate — inertia-advocate
**Null hypothesis**: [state what the team does today instead of this]
**Challenge**: [does the artifact defeat this hypothesis? what evidence is present or absent?]
**Findings**: [2–3 sentences from the inertia-advocate's lens]
**Severity**: HIGH | MEDIUM | LOW
**Recommendation**: [one concrete action the artifact must add or change]
**Verify Question**: [one question from the inertia-advocate's lens.verify]
**Gate Verdict**: FAIL | CONDITIONAL | PASS
```

FAIL: artifact does not address the null hypothesis.
CONDITIONAL: artifact partially addresses it.
PASS: artifact addresses it sufficiently.

**Step 3 — Domain Reviewer Sections**

After the Null Hypothesis Gate, run each remaining selected role. Domain reviewers have access
to the artifact only — they do not have access to the inertia-advocate's findings.

For each domain reviewer:
1. Read the role's `lens.verify`, `lens.simplify`, and `expertise.depth` from its role file.
2. Produce findings from this role's specific frame. Findings must not echo the inertia-advocate's
   framing or repeat findings from other reviewers.
3. Output:

```
### [Role name] — [archetype]
**Findings**: [2–4 sentences, role-frame-specific]
**Severity**: HIGH | MEDIUM | LOW
**Recommendation**: [one concrete scoped action]
**Verify Question**: [one question from this role's lens.verify]
**Simplify**: [one element from lens.simplify this reviewer would cut or collapse]
**Gate Verdict**: FAIL | CONDITIONAL | PASS
```

Severity is calibrated independently per reviewer. If all domain reviewers share the same
severity level, re-examine.

**Step 4 — Action Register**

Using the CLASS DERIVATION CONTRACT from the preamble, produce a consolidated action list.

```
## Action Register
(Class derives mechanically from gate verdict per CLASS DERIVATION CONTRACT above)

| # | Gate Verdict | Class | Finding Reference | Action Required |
|---|--------------|-------|-------------------|-----------------|
```

- Finding Reference: `[role] / [gate verdict] / [finding in 5 words or fewer]`
- Class: applied from the derivation contract, not re-assessed here
- Action: synthesis — not a verbatim recommendation copy

Minimum: one row per FAIL or CONDITIONAL gate verdict.

**Step 5 — Cross-Role Summary and Disposition**

Write a synthesis section (5–8 sentences) that:
- Names the highest-severity finding across all reviewers
- Identifies any cross-role conflict (two reviewers with incompatible recommendations)
- References the Null Hypothesis Gate Verdict from Step 2
- Explains (not just states) the overall disposition

Close with:
```
DISPOSITION: READY | CONDITIONAL | BLOCKED
```

DISPOSITION is computed from gate verdicts:
- BLOCKED: any gate verdict = FAIL
- CONDITIONAL: no FAIL; at least one gate verdict = CONDITIONAL
- READY: all gate verdicts = PASS

**Artifact to review:**

{{artifact}}

---

## V-03 — Inertia Framing: Override Authority with Labeled Decision Field

**Variation axis**: Inertia framing — the challenger role runs twice (bracket architecture, C-09)
and emits an explicit `Override invoked: YES | NO` labeled field in the Bracket Closing (C-11);
single-axis focus is the override decision field as a structural output contract
**Hypothesis**: C-11 is vacuous without C-09. To isolate C-11, this variation must implement C-09
first. The bracket architecture is taken from V-05-R1 verbatim. The single-axis addition is
precisely: the Bracket Closing section now has a mandatory `Override invoked: YES | NO` field
that appears regardless of whether override is exercised. The hypothesis: making the field
mandatory (not conditional on whether override is invoked) is what makes C-11 pass reliably.
V-05-R1 already had this field — this variation verifies the pattern survives without the full
disposition algebra (C-10 is not added here). Expected score: 60+20+5(C-09)+5(C-11)=90 if
recommended criteria hold, scoring in the Gold tier without C-10.

---

You are running `org-review` on the artifact provided below.

**Severity Semantics** (fixed; applies throughout):
- HIGH: blocks commitment to proceed
- MEDIUM: conditions commitment; proceed only after remediation
- LOW: advisory; proceed regardless

---

**§0 — Scope Declaration**

Before any reviewer section, declare:

```
IN SCOPE:
- Artifact: [name / type]
- Surfaces: [spec text, design constraints, prior decisions named in the artifact]

OUT OF SCOPE:
- [surfaces not being reviewed in this pass]
```

Any surface discovered during review not listed above is flagged as a scope gap in that
reviewer's findings — not silently incorporated into scope.

---

**§1 — Depth Mode and Role Selection**

Read `.craft/roles/signal/`. Enumerate all roles.

- **Standard** (default): Select roles relevant to this artifact type. Minimum 2 domain roles.
  State selection and one-sentence rationale per role.
- **`--depth deep`**: Include all roles. State total count.

The `inertia-advocate` is reserved for §1.5 and §3 (Bracket Opening and Bracket Closing).
It does not appear in the domain reviewer list for §2.

---

**§1.5 — Bracket Opening: Challenger Pre-Domain Testimony**

This section runs before any domain reviewer. Domain reviewers do not have access to this section.

From the inertia-advocate role file, apply `lens.verify` and `expertise` to produce:

```
## Bracket Opening — inertia-advocate
**Null hypothesis**: [what the team does today instead of this]
**Challenge**: [does the artifact name and address the status quo case?]
**Specific gap (if any)**: [what must be true for this artifact to defeat the null hypothesis]
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
2. Apply `orientation.frame` to the artifact. Generate findings from this frame.
3. Findings must not echo the Bracket Opening framing or other domain reviewers.
4. Emit:

```
## Domain Reviewer: [role] ([archetype])
**Findings**: [2–4 sentences, frame-specific, non-echoing]
**Severity**: HIGH | MEDIUM | LOW
**Recommendation**: [one concrete action]
**Verify Question**: [from lens.verify]
**Simplify**: [one observation from lens.simplify]
**Gate Verdict**: FAIL | CONDITIONAL | PASS
```

---

**§3 — Bracket Closing: Challenger Post-Domain Reassessment**

After all domain reviewer sections are complete, the inertia-advocate reassesses whether domain
evidence collectively defeats the null hypothesis from §1.5. The Bracket Closing does not
re-review the artifact from scratch. It answers one question: *Do the domain findings together
constitute sufficient evidence to defeat the null hypothesis stated in §1.5?*

The inertia-advocate carries override authority: if domain reviewers collectively PASS but the
null hypothesis is still not addressed, the Bracket Closing may override with BLOCKED.

```
## Bracket Closing — inertia-advocate (post-domain reassessment)
**Null hypothesis restated**: [from §1.5]
**Domain evidence reviewed**: [name which domain reviewers' findings speak to the null hypothesis]
**Assessment**: [does domain testimony defeat the null hypothesis? what is still missing?]
**Override authority**: if domain reviewers collectively PASS but the null hypothesis remains
  unaddressed, the Bracket Closing may override. State override explicitly if invoked.
**Closing Verdict**: DEFEATED | PARTIAL | NOT DEFEATED
**Override invoked**: YES | NO
```

This field is mandatory. If YES: append "Bracket Closing overrides domain PASS — see Disposition."
If NO: no action; the domain verdicts stand.

Closing Verdict and Override invoked feed directly into the Disposition section.

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
- BLOCKED class: sourced from FAIL gate verdicts or Override invoked: YES
- CONDITIONAL class: sourced from CONDITIONAL gate verdicts
- ADVISORY class: sourced from LOW-only findings at PASS gates
- Actions are syntheses, not verbatim recommendation copies

Minimum: one row per FAIL or CONDITIONAL gate verdict.

---

**§5 — Integrating Summary and Disposition**

Write a synthesis section (5–8 sentences):
- Name the highest-severity finding
- Name any cross-role conflict
- Name areas of cross-role convergence
- Reference the Opening Verdict (§1.5) and the Closing Verdict (§3) explicitly
- Note whether Override invoked = YES or NO and explain the consequence

Close with:
```
DISPOSITION: READY | CONDITIONAL | BLOCKED
```

Disposition logic:
- BLOCKED: any gate verdict = FAIL, OR Override invoked = YES in §3
- CONDITIONAL: no FAIL, no override; at least one CONDITIONAL gate verdict remains
- READY: all gate verdicts = PASS and Override invoked = NO

**Artifact to review:**

{{artifact}}

---

## V-04 — Combination: Template Variables + Mechanical Class Derivation (Gold path, no bracket)

**Variation axes**: Output format (template variables, C-13) + lifecycle emphasis (class derivation
contract, C-12); Gold-tier target without bracket overhead
**Hypothesis**: V-04-R1 passed C-13 (template vars) but failed C-12 (class derivation). V-05-R1
passed C-12 but failed C-13. This combination takes the clean Phase-structured format from V-04-R1,
adds a CLASS DERIVATION CONTRACT to the preamble, and makes both template variables explicit.
With all 5 essential, all 3 recommended, C-12, and C-13 in scope — and no bracket (C-09/C-10/C-11
are out) — the expected score is 60+30+5+5=100. This is the highest achievable score without
bracket architecture, and it avoids the structural complexity that makes bracket variants harder
to execute correctly.

---

**Template inputs:**

```
{{artifact_id}}   — identifier or short name for the artifact under review
{{depth}}         — depth mode: standard | deep
{{reviewer_set}}  — (optional) comma-separated list of roles to run; "auto" to select by relevance
```

**Acknowledgment block (emit at the start of your output):**

```
## Review Parameters
Artifact: {{artifact_id}}
Depth mode: {{depth}}
Reviewer set: {{reviewer_set}}
```

---

You are executing the `org-review` skill. This skill distributes an artifact to a set of
organizational reviewers drawn from the role registry at `.craft/roles/signal/`. Each reviewer
applies their designated lens and returns a structured finding. The output is a review matrix
and disposition suitable for decision-making.

**Severity Semantics** (applies throughout this review):
- HIGH: finding blocks commitment to proceed
- MEDIUM: commitment may proceed only after remediation
- LOW: advisory; proceed regardless

**CLASS DERIVATION CONTRACT** (committed before any reviewer executes):

Action item classes in the Action Register derive mechanically from gate verdicts.
The evaluator does not re-assess class at synthesis time.

```
Gate verdict → Action Item Class:
  FAIL         → BLOCKED      (must resolve before any commitment)
  CONDITIONAL  → CONDITIONAL  (must resolve before proceeding)
  PASS + HIGH  → CONDITIONAL  (HIGH finding retained as conditional even at PASS gate)
  PASS + LOW   → ADVISORY     (may defer; not blocking)
```

Any item in the Action Register whose class contradicts the gate verdict that sourced it is a
structural defect.

---

**Phase 0: Scope Declaration**

Enumerate what is under review before any reviewer section executes:

```
IN SCOPE:
- Artifact: {{artifact_id}}
- Surfaces: [e.g., spec text, design constraints, prior decisions named in the artifact]

OUT OF SCOPE:
- [surfaces not being reviewed in this pass]
```

Scope is fixed here. If a reviewer discovers an artifact or dependency not listed, it is flagged
as a scope gap in that reviewer's findings — not silently incorporated.

---

**Phase 1: Reviewer Selection**

Input: `.craft/roles/signal/` directory
Depth parameter: {{depth}}
Reviewer set override: {{reviewer_set}} (if not "auto", use the named roles)

Procedure:
1. Enumerate all role files in `.craft/roles/signal/`.
2. If `{{depth}}` = `standard` and `{{reviewer_set}}` = `auto`: apply relevance filter —
   select roles whose `expertise.relevance` matches this artifact type. Minimum 2 domain roles.
   The inertia-advocate is always included. Document selection rationale (one sentence per role).
3. If `{{depth}}` = `deep`: include all enumerated roles. Document total count.
4. If `{{reviewer_set}}` is not "auto": use the named roles exactly.

Output:

```
Depth mode: {{depth}}
Reviewer manifest:
  - [role]: [archetype] — [selection rationale or "deep run — all roles" or "explicit set"]
  ...
```

No role may be invented. Every reviewer must have a corresponding file in `.craft/roles/signal/`.

---

**Phase 2: Null Hypothesis Gate**

Run the inertia-advocate's lens before domain reviewer sections execute.

```
## Phase 2 — Null Hypothesis Gate
Reviewer: inertia-advocate
Status quo: [what the team does today in place of this artifact]
Challenge: [does the artifact name and address the status quo case?]
Severity: HIGH | MEDIUM | LOW
Gate Verdict: FAIL | CONDITIONAL | PASS
```

Domain sections (Phase 3) begin only after this verdict is emitted.

---

**Phase 3: Review Execution**

For each reviewer in the Phase 1 manifest (excluding the inertia-advocate, executed in Phase 2):

3a. Load role file from `.craft/roles/signal/{role}.md`.
3b. Extract: `orientation.frame`, `lens.verify`, `lens.simplify`, `expertise.depth`.
3c. Apply the orientation frame to the artifact. This frame determines which properties are salient.
3d. Generate findings from this frame. Findings must not duplicate the framing of another reviewer.
    Cross-role finding homogeneity is a structural defect.
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
**Gate Verdict**: FAIL | CONDITIONAL | PASS
```

---

**Phase 4: Action Register**

Using the CLASS DERIVATION CONTRACT from the preamble, consolidate all gate verdicts into a
traceable action list.

```
## Phase 4 — Action Register
(Classes derived per CLASS DERIVATION CONTRACT — no editorial re-assessment)

| # | Gate Verdict | Class | Finding Reference | Action |
|---|--------------|-------|-------------------|--------|
```

- Finding Reference: [phase] / [role] / [5-word summary]
- Class: applied from the derivation contract, not re-assessed here
- Action: synthesis — not verbatim recommendation copy

Minimum: one row per FAIL or CONDITIONAL gate verdict.

---

**Phase 5: Synthesis and Disposition**

5a. Identify the highest-severity finding across all phases.
5b. Identify cross-role conflicts: two reviewers whose recommendations are incompatible.
5c. Identify convergence areas where multiple reviewers flag the same risk.
5d. Reference the Phase 2 null hypothesis verdict explicitly.
5e. Explain the disposition — the reasoning, not only the label.

```
## Phase 5 — Synthesis
[5–8 sentence synthesis addressing 5a–5e above]

DISPOSITION: READY | CONDITIONAL | BLOCKED
```

Disposition computation:
- BLOCKED: any gate verdict = FAIL
- CONDITIONAL: no FAIL; at least one gate verdict = CONDITIONAL
- READY: all gate verdicts = PASS

Disposition may not contradict a FAIL null hypothesis verdict without explicit override explanation.

---

**Artifact to review:**

{{artifact_id}} artifact content:

{{artifact}}

---

## V-05 — Full Stack: All Five Aspirational Criteria

**Variation axes**: Adversarial bracket architecture (C-09) + disposition algebra pre-committed
(C-10) + override decision labeled field (C-11) + class derivation contract (C-12) + template
variable injection (C-13); targeting 115/115
**Hypothesis**: V-05-R1 scored 105/115 — it passed C-09/C-10/C-11/C-12 but failed C-13. V-04-R1
scored 95/115 — it passed C-13 but not C-09/C-10/C-11/C-12. The only missing piece is
combining them. This variation takes V-05-R1 verbatim and adds: (1) explicit template variable
declarations at the top, (2) an acknowledgment block before §0, (3) `{{depth}}` and
`{{artifact_id}}` woven into Phase 1 exactly as in V-04 above. If C-13 requires >= 2 variables
plus an acknowledgment block, adding those two elements to the V-05-R1 structure — which
already passes everything else — should be sufficient for a perfect score.

---

**Template inputs:**

```
{{artifact_id}}  — identifier or short name for the artifact under review
{{depth}}        — depth mode: standard | deep
```

**Acknowledgment block (emit at the start of your output, before §0):**

```
## Review Parameters
Artifact: {{artifact_id}}
Depth mode: {{depth}}
```

---

You are running `org-review` on the artifact provided below.

**Severity Semantics** (fixed; applies throughout):

| Label | Commit-gate meaning |
|-------|---------------------|
| HIGH | Blocks commitment. Unresolved HIGH finding → BLOCKED disposition. |
| MEDIUM | Conditions commitment. No unresolved HIGH + MEDIUM present → CONDITIONAL. |
| LOW | Advisory. No MEDIUM or HIGH → READY. |

**DISPOSITION CONTRACT** (committed before any reviewer executes):

The following formula maps gate verdicts to overall disposition. This formula is applied
mechanically at synthesis time. The synthesis section applies this formula — it does not produce
a new one.

```
DISPOSITION FORMULA:
  if   any gate verdict = FAIL                → DISPOSITION = BLOCKED
  elif Override invoked = YES  (see §3)       → DISPOSITION = BLOCKED
  elif any gate verdict = CONDITIONAL         → DISPOSITION = CONDITIONAL
  elif all gate verdicts = PASS               → DISPOSITION = READY
  else                                        → DISPOSITION = CONDITIONAL  (ambiguous gates)
```

Gate verdicts are emitted by: Bracket Opening (§1.5), domain reviewers (§2), Bracket Closing (§3).
The formula is the evaluator. Editorial judgment at summary time does not override it.

**CLASS DERIVATION CONTRACT** (committed before any reviewer executes):

Action item classes in the Action Register derive mechanically from gate verdicts:

```
Gate verdict → Action Item Class:
  FAIL         → BLOCKED
  CONDITIONAL  → CONDITIONAL
  PASS + HIGH  → CONDITIONAL
  PASS + LOW   → ADVISORY
```

No item's class may be assigned editorially at synthesis time.

---

**§0 — Scope Declaration**

Before any reviewer section, declare:

```
IN SCOPE:
- Artifact: {{artifact_id}}
- Surfaces: [spec text, constraints, named prior decisions]

OUT OF SCOPE:
- [surfaces not reviewed in this pass]
```

Any surface discovered during review not listed above is flagged as a scope gap — not silently
incorporated into scope.

---

**§1 — Depth Mode and Role Selection**

Read `.craft/roles/signal/`. Enumerate all roles.
Depth parameter: {{depth}}

- **`{{depth}}` = standard**: Select roles relevant to this artifact type. Minimum 2 domain roles.
  State selection and one-sentence rationale per role.
- **`{{depth}}` = deep**: Include all roles. State total count.

Output:

```
Depth mode: {{depth}}
Reviewer manifest:
  - [role]: [archetype] — [rationale or "deep run — all roles"]
  ...
```

The `inertia-advocate` is reserved for §1.5 and §3 (Bracket Opening and Closing). It does not
appear in the domain reviewer list for §2.

No role may be invented. Every reviewer must have a corresponding file in `.craft/roles/signal/`.

---

**§1.5 — Bracket Opening: Challenger Pre-Domain Testimony**

This section runs before any domain reviewer. Domain reviewers do not have access to this section.

From the inertia-advocate role file, apply `lens.verify` and `expertise.depth`:

```
## Bracket Opening — inertia-advocate
**Null hypothesis**: [what the team does today]
**Challenge to artifact**: [does the artifact name this? address it? is the evidence real?]
**Specific gap (if any)**: [what must be true for this artifact to defeat the null hypothesis]
**Severity**: HIGH | MEDIUM | LOW
**Verify Question**: [from inertia-advocate's lens.verify]
**Opening Verdict**: FAIL | CONDITIONAL | PASS
```

Domain reviewer sections begin only after the Opening Verdict is emitted.

---

**§2 — Domain Reviewer Sections**

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
**Findings**: [2–4 sentences, frame-specific, non-echoing]
**Severity**: HIGH | MEDIUM | LOW
**Recommendation**: [one concrete action]
**Verify Question**: [from lens.verify]
**Simplify**: [one observation from lens.simplify]
**Gate Verdict**: FAIL | CONDITIONAL | PASS
```

---

**§3 — Bracket Closing: Challenger Post-Domain Reassessment**

This section runs after all domain reviewer sections are complete. The inertia-advocate now has
access to all domain findings and reassesses whether domain evidence collectively defeats the
null hypothesis from §1.5.

The Bracket Closing answers one question: *Do the domain findings together constitute sufficient
evidence to defeat the null hypothesis stated in §1.5?*

The inertia-advocate carries override authority: if domain reviewers collectively PASS but the
null hypothesis is still not addressed, the Bracket Closing may override with BLOCKED.

```
## Bracket Closing — inertia-advocate (post-domain reassessment)
**Null hypothesis restated**: [from §1.5]
**Domain evidence reviewed**: [name which domain reviewers' findings are relevant to null hypothesis]
**Assessment**: [does domain testimony defeat the null hypothesis? what is still missing?]
**Override authority**: if domain reviewers collectively PASS but null hypothesis remains
  unaddressed, the Bracket Closing may override. State explicitly if invoked.
**Closing Verdict**: DEFEATED | PARTIAL | NOT DEFEATED
**Override invoked**: YES | NO
```

This field is mandatory. Emit YES or NO.
- If YES: append "Bracket Closing overrides domain PASS — DISPOSITION = BLOCKED per DISPOSITION CONTRACT."
- If NO: domain verdicts stand; Closing Verdict feeds DISPOSITION CONTRACT normally.

---

**§4 — Action Register**

Using the CLASS DERIVATION CONTRACT from the preamble, consolidate all FAIL/CONDITIONAL gate
verdicts from §1.5, §2, and §3 into a traceable action list.

```
## Action Register
(Classes derived per CLASS DERIVATION CONTRACT — no editorial re-assessment)

| # | Gate Verdict | Class | Finding Reference | Action |
|---|--------------|-------|-------------------|--------|
```

- Finding Reference: [§] / [role] / [5-word summary]
- Class: applied from the derivation contract, not re-assessed here
- Actions are syntheses, not verbatim recommendation copies

Minimum: one row per FAIL or CONDITIONAL gate verdict.

---

**§5 — Integrating Summary and Disposition**

Write a synthesis section (5–8 sentences):
- Name the highest-severity finding across all phases
- Name any cross-role conflict (two domain reviewers with incompatible recommendations)
- Name areas of cross-role convergence
- Reference the Opening Verdict (§1.5) and Closing Verdict (§3) explicitly
- State whether Override invoked = YES or NO, and the consequence for disposition
- Explain why the disposition follows from the gate verdicts

Apply the DISPOSITION CONTRACT from the preamble to the gate verdicts. State which formula
branch applies.

```
## Phase 5 — Synthesis
[5–8 sentence synthesis]

FORMULA APPLIED: [state which branch of the DISPOSITION CONTRACT applies and why]

DISPOSITION: READY | CONDITIONAL | BLOCKED
```

The Integrating Summary explains the disposition. It does not produce a new formula.

---

**Artifact to review:**

{{artifact_id}} artifact content:

{{artifact}}
