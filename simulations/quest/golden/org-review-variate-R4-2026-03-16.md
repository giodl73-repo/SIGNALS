# org-review Variations — Round 4 (v3 rubric, 2026-03-16)
Generated: 2026-03-16
Skill: org-review
Rubric: simulations/quest/rubrics/org-review-rubric-v3-2026-03-16.md

Prior round summary:
- R1 (v1 rubric): V-05=95 (C-09+C-10+C-11+C-12), V-04=90 (C-13). C-11/C-12 differentiators.
- R2 (v2 rubric / v3 retroactive): V-04=110 (C-12+C-13+C-14+C-15), V-03=97 (bracket). First Gold.
- R3 (v3 rubric): Five deliberate designs — single-axis C-14, C-15, C-09+C-11, then two
  combinations. R3-V04 = C-12+C-13+C-14+C-15 rebuild (target 110). R3-V05 = all 7 aspirational
  (target 125). Axes covered: phase-labeled structure, pre-printed template, formula-first algebra,
  adversarial bracket, stepped propagation.

Round 4 strategy:
- Axes NOT yet explored: phrasing register (all prior variants formal/technical), inertia framing
  via quantified Alternatives Table, output format via inline ledger (gate verdict recorded at
  origin, not deferred to register), lifecycle-emphasis via decision schema preamble.
- Three single-axis variants (V-01, V-02, V-03), then two combinations (V-04, V-05).
- V-01: single axis -- phrasing register (conversational direct imperative); base = R3-V04 Gold
  path mechanisms, different register
- V-02: single axis -- inertia framing (Alternatives Table with dimension scoring); base = Gold
  path structure; null hypothesis gate verdict derived from score differential rule in preamble
- V-03: single axis -- output format (inline Gate Ledger per reviewer; deferred consolidation);
  base = minimal Gold path; C-14 enforcement moves to point of origin
- V-04: combination -- phrasing register + C-12 + C-13 + C-14 + C-15 (conversational Gold path)
- V-05: combination -- Alternatives Table + full stack (C-09 + C-10 + C-11 + C-12 + C-13 +
  C-14 + C-15); table feeds bracket; domain reviewers re-score dimensions; closer reassesses
  aggregate table; targeting 125/125

Expected score ladder (v3 rubric, 125 pts max):
  V-01: 60+30+5(C-12)+5(C-13)+5(C-14)+5(C-15)=110  -- Gold (conversational register; same structure as R3-V04)
  V-02: 60+30+5(C-10)+5(C-14)=100                   -- Gold floor (table rule = C-10 analog; table column = C-14)
  V-03: 60+30+5(C-12)+5(C-14)=100                   -- Gold floor (inline ledger enforces C-12+C-14 structurally)
  V-04: 60+30+5(C-12)+5(C-13)+5(C-14)+5(C-15)=110  -- Gold (combination confirms register indifference)
  V-05: 60+30+35=125                                 -- Perfect (table + bracket path)

---

## V-01 -- Phrasing Register: Conversational Direct Imperative

**Variation axis**: Phrasing register -- all structural mechanisms of R3-V04 (CLASS DERIVATION
CONTRACT, three template variables, Gate Verdict column) are preserved unchanged; the register
is rewritten from formal phase-labeled instructional to second-person conversational imperative
with short sentences and no Phase/Step headers

**Hypothesis**: All prior variants use formal, third-person, phase-labeled instruction ("The
review produces verdicts. The formula produces the disposition."). The model may interpret
descriptive phrasing as lower-commitment than directive phrasing. Conversational imperative
("Run the inertia-advocate first. Do not skip this.") reduces syntactic distance between
instruction and required action. If register affects compliance, this is the cleanest test:
identical structure and targeted criteria, different sentence-level style. A register-invariant
score validates that formal/conversational register is not a meaningful variable for this skill.

---

**Template inputs:**

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .roles/signal/
```

Start your output with this block. Fill in the injected values.

```
## Review Parameters
Artifact:     {{artifact_id}}
Depth:        {{depth}}
Reviewers:    {{reviewer_set}}
```

---

You're running org-review on {{artifact_id}}. Your job: distribute the artifact to reviewers
from `.roles/signal/`, collect structured findings per role, and emit a commitment
disposition.

Keep this derivation rule in scope for the whole review. It doesn't change.

**CLASS DERIVATION RULE** -- derive action item class from gate verdict, not from editorial
re-read of finding text:

```
FAIL gate        -->  BLOCKED      (must resolve before any commitment)
CONDITIONAL gate -->  CONDITIONAL  (must resolve before proceeding)
PASS + HIGH      -->  CONDITIONAL  (HIGH finding retained even at PASS gate)
PASS + LOW       -->  ADVISORY     (may defer)
```

Don't re-assess class at synthesis time. Apply the rule to the verdict. That's all.

**Severity:**
- HIGH: blocks commitment to proceed
- MEDIUM: conditions commitment; proceed only after fix
- LOW: advisory; doesn't block

---

**First: Declare scope.** Before any reviewer runs, write:

```
In scope:
  - Artifact: {{artifact_id}}
  - Surfaces: [spec text, design constraints, named prior decisions]
Out of scope:
  - [what isn't being reviewed in this pass]
```

If a reviewer discovers something not in this list, flag it as a scope gap. Don't silently
add it to scope.

---

**Second: Pick your reviewers.** Read `.roles/signal/`. Don't invent roles.

Check `{{reviewer_set}}`:
- Not "auto": use those roles exactly. If inertia-advocate is missing, add it and say so.
- "auto" + "standard": pick roles relevant to this artifact type. At least 2 domain roles.
  One sentence of rationale per role.
- "auto" + "deep": all roles in the directory. State the total count.

Emit this manifest before any reviewer section:

```
Depth mode: {{depth}}
Reviewer set: {{reviewer_set}}
Reviewers:
  - [role]: [archetype] -- [rationale | "explicit" | "all roles"]
```

---

**Third: Run the inertia-advocate.** Domain reviewers don't see this section.

```
Null Hypothesis Gate -- inertia-advocate
Status quo:      [what the team does today instead of building this -- one sentence]
Challenge:       [does the artifact address the status quo case?]
Findings:        [2-3 findings: switching costs, workaround viability, adoption friction]
Severity:        HIGH | MEDIUM | LOW
Verify Question: [one from inertia-advocate's lens.verify]
Gate Verdict:    FAIL | CONDITIONAL | PASS
```

Domain reviewer sections start only after Gate Verdict is emitted.

---

**Fourth: Run each domain reviewer.** Keep findings distinct per reviewer. Don't echo the
challenger's framing. Cross-role homogeneity in findings is a defect.

```
Reviewer: [role] ([archetype])
Findings:    [2-4 from this role's lens.verify and expertise.depth]
Severity:    HIGH | MEDIUM | LOW
Recommend:   [one concrete action from this role's frame]
Verify:      [one from this role's lens.verify]
Simplify:    [one from this role's lens.simplify]
Gate Verdict: FAIL | CONDITIONAL | PASS
```

---

**Fifth: Build the action register.** Apply CLASS DERIVATION RULE. The Gate Verdict column is
mandatory -- don't omit it, don't rename it.

```
Action Register
(Classes from CLASS DERIVATION RULE -- no editorial re-assessment)

| # | Gate Verdict | Class | Finding Reference | Action |
|---|--------------|-------|-------------------|--------|
```

Columns:
- Gate Verdict: copy the verdict from the reviewer section that produced this item
- Class: from the derivation rule, not from editorial judgment
- Finding Reference: `[role] / [5-word summary]`
- Action: your synthesis -- not verbatim recommendation copy

One row minimum per FAIL or CONDITIONAL verdict.

---

**Sixth: Write the synthesis.** 5-8 sentences. Cover:
- highest-severity finding across all reviewers
- any cross-role conflict (incompatible recommendations from two roles)
- areas where multiple reviewers converge
- null hypothesis gate verdict -- name it explicitly
- why the disposition follows from the gate verdicts

Then emit:

```
DISPOSITION: READY | CONDITIONAL | BLOCKED
```

Rules:
- BLOCKED: any gate = FAIL
- CONDITIONAL: no FAIL, at least one CONDITIONAL
- READY: all PASS

Disposition may not contradict a FAIL null hypothesis verdict without explanation.

---

**Artifact to review:**

{{artifact_id}} content:

{{artifact}}

---

## V-02 -- Inertia Framing: Alternatives Table with Dimension Scoring

**Variation axis**: Inertia framing -- the null hypothesis is quantified via an Alternatives
Table (4 named dimensions, 1-5 scale per alternative); the challenger gate verdict derives from
a score differential rule stated in the preamble, not from narrative prose; domain reviewers
provide a domain-frame re-read of the same dimension scores; the null hypothesis evaluation is
machine-auditable from the table alone

**Hypothesis**: Prior variants frame the null hypothesis as prose that the challenger evaluates
narratively. This makes C-03 a narration criterion: the model can "address" the null hypothesis
without any structured comparison. An Alternatives Table forces a named, scored comparison on
fixed dimensions. The derivation rule in the preamble maps score differential to gate verdict --
making the null hypothesis gate structurally analogous to C-10 (disposition algebra committed
before execution) but for the null hypothesis specifically. If the table is more reliable, it
creates a novel machine-auditable path for C-03 and C-14 (gate verdict traceable through the
score differential, not just a label).

---

You are running `org-review` on the artifact provided below.

**Severity Semantics** (applies throughout):

| Severity | Commit-gate meaning |
|----------|---------------------|
| HIGH | Blocks commitment |
| MEDIUM | Conditions commitment; proceed only after remediation |
| LOW | Advisory; proceed regardless |

**NULL HYPOTHESIS DERIVATION RULE** (committed before the review begins; g_null is derived from
the score differential -- do not assert the verdict, derive it):

The Alternatives Table compares the status quo (what the team does today) against this artifact
on four dimensions. Each dimension scored 1-5 per alternative.

```
Dimensions:
  D1 -- Switching cost       (1 = prohibitive to adopt artifact, 5 = negligible)
  D2 -- Coverage             (1 = artifact covers far less than status quo, 5 = complete coverage)
  D3 -- Adoption friction    (1 = high friction to adopt, 5 = frictionless)
  D4 -- Time-to-value        (1 = months before value, 5 = immediate value on adoption)

Score differential = Artifact total - Status Quo total   (range: -16 to +16)

Derivation rule:
  differential >= +6   -->  g_null = PASS        (artifact clearly superior)
  differential +1..+5  -->  g_null = CONDITIONAL  (marginal case; named gaps must be addressed)
  differential <= 0    -->  g_null = FAIL         (no case for building over the status quo)
```

The review produces table scores. The rule produces g_null. The evaluator does not assert it.

---

**Step 1 -- Role Selection**

Read `.roles/signal/`. Select reviewers.

- **Standard** (default): CHALLENGER slot (inertia-advocate archetype), DOMAIN slot
  (technical/architecture archetype, minimum 1), LIFECYCLE slot (PM/program archetype).
  One role per slot. State assignment and one-sentence rationale.
- **`--depth deep`**: All roles in directory. State count.

No invented roles.

---

**Step 2 -- Null Hypothesis Gate (Challenger)**

Run the inertia-advocate first. Domain reviewers have not seen this section.

```
## Null Hypothesis Gate -- [challenger role]

**Status quo statement**: [what the team does today instead of building this -- one sentence]

**Alternatives Table (challenger frame):**

| Dimension | Status Quo | This Artifact | Rationale |
|-----------|-----------|---------------|-----------|
| D1 Switching cost    | [1-5] | [1-5] | [one sentence per cell explaining the score] |
| D2 Coverage          | [1-5] | [1-5] | [one sentence] |
| D3 Adoption friction | [1-5] | [1-5] | [one sentence] |
| D4 Time-to-value     | [1-5] | [1-5] | [one sentence] |
| **TOTAL**            | [sum] | [sum] | |

**Score differential**: [artifact total] - [status quo total] = [+/- n]

**NULL HYPOTHESIS DERIVATION RULE applied**: [state which branch and why]

**Gate Verdict (g_null)**: PASS | CONDITIONAL | FAIL

**Findings**: [2-3 narrative findings from challenger's lens.verify supporting the table scores]
**Severity**: HIGH | MEDIUM | LOW
**Verify Question**: [one from challenger's lens.verify]
```

Domain sections begin only after g_null is emitted.

---

**Step 3 -- Domain Reviewer**

Each domain reviewer provides a domain-frame re-read of the alternatives table and their own
technical findings.

```
## Domain Reviewer: [role] ([archetype])

**Domain re-read of alternatives table** (challenger's score differential was [+/-n]):
  D1 revised: [1-5] | [unchanged | justification for revision]
  D2 revised: [1-5] | [unchanged | justification for revision]
  D3 revised: [1-5] | [unchanged | justification for revision]
  D4 revised: [1-5] | [unchanged | justification for revision]
  [Domain-frame null hypothesis address]: [from this role's technical frame, does the artifact
    defeat the status quo? One sentence. Must differ from challenger's framing.]

**Findings**: [2-4 findings from this role's lens.verify and expertise.depth; must not
  duplicate challenger framing or other domain reviewers]
**Severity**: HIGH | MEDIUM | LOW
**Recommendation**: [one concrete action]
**Verify Question**: [one from this role's lens.verify]
**Simplify**: [one from this role's lens.simplify]
**Gate Verdict (g_domain)**: PASS | CONDITIONAL | FAIL
```

---

**Step 4 -- Lifecycle Reviewer**

```
## Lifecycle Reviewer: [role] ([archetype])

**Commitment-readiness assessment**: [Is the alternatives table evidence sufficient to support
  a commitment decision? Reference the g_null verdict and domain re-reads explicitly. One
  paragraph.]
**Findings**: [2-3 findings: commitment readiness, decision sufficiency, program concerns]
**Severity**: HIGH | MEDIUM | LOW
**Recommendation**: [one concrete action]
**Verify Question**: [one from this role's lens.verify]
**Simplify**: [one from this role's lens.simplify]
**Gate Verdict (g_lifecycle)**: PASS | CONDITIONAL | FAIL
```

---

**Step 5 -- Action Register**

```
## Action Register

| # | Class | Finding Reference | Action Required |
|---|-------|-------------------|-----------------|
```

Classes:
- BLOCKED: from FAIL gate verdicts -- must resolve before any commitment
- CONDITIONAL: from CONDITIONAL gate verdicts -- must resolve before proceeding
- ADVISORY: from PASS + LOW findings

Finding Reference: `[role] / [5-word summary]`

Minimum: one row per FAIL or CONDITIONAL gate verdict.

---

**Step 6 -- Synthesis and Disposition**

Write 5-8 sentences:
- Name the dimension gap most responsible for any FAIL or CONDITIONAL g_null verdict
- Name cross-role conflicts (incompatible recommendations)
- Name convergence (multiple reviewers flagging the same gap independently)
- Reference g_null explicitly (score differential + derived verdict)
- Explain the disposition

```
DISPOSITION: READY | CONDITIONAL | BLOCKED
```

- BLOCKED: any gate = FAIL
- CONDITIONAL: no FAIL, at least one CONDITIONAL
- READY: all PASS

**Artifact to review:**

{{artifact}}

---

## V-03 -- Output Format: Inline Gate Ledger with Deferred Consolidation

**Variation axis**: Output format -- each reviewer section ends with a mandatory Local Gate
Ledger row (a one-row table containing Gate Verdict, Class, Finding Reference, Action); the
final action register is assembled by consolidating all local ledger rows into a master table;
the Gate Verdict is recorded at the point of origin, not retroactively assigned during synthesis

**Hypothesis**: In prior variants, the Gate Verdict column appears only in the final action
register, requiring the model to copy each verdict from a reviewer section into a separate table
written later. This creates a copy-distance failure mode: the model states the verdict in the
reviewer section, then re-assigns the class editorially during synthesis. Moving Gate Verdict +
Class + Action into a local ledger row at the reviewer section makes derivation local and
immediate -- the class is assigned at the same moment the verdict is emitted. C-14 compliance
becomes structural rather than a deferred task. The consolidation step is then a copy operation,
not a synthesis -- making structural defects (class contradicts verdict) visible immediately.

---

You are running `org-review` on the artifact provided below.

**Severity Semantics:**

| Severity | Commit-gate meaning |
|----------|---------------------|
| HIGH | Blocks commitment |
| MEDIUM | Conditions commitment; proceed only after remediation |
| LOW | Advisory; proceed regardless |

**CLASS DERIVATION RULE** -- applies to every Local Gate Ledger row. Stated once here.
Do not re-derive class at consolidation time.

```
FAIL gate        -->  BLOCKED
CONDITIONAL gate -->  CONDITIONAL
PASS + HIGH      -->  CONDITIONAL
PASS + LOW       -->  ADVISORY
```

Every reviewer section ends with a Local Gate Ledger row. That row is the source of truth
for the final master action register. Class must follow the derivation rule -- no exceptions.

---

**Step 0 -- Scope**

Before any reviewer section:

```
In scope:
  - Artifact: [name / type]
  - Surfaces: [spec text, design constraints, named prior decisions]
Out of scope:
  - [what is not being reviewed in this pass]
```

Any surface discovered mid-review not in this list is flagged as a scope gap, not absorbed.

---

**Step 1 -- Role Selection**

Read `.roles/signal/`. Select:
- CHALLENGER: inertia-advocate archetype
- DOMAIN: technical/architecture archetype (minimum 1; more if `--depth deep`)
- LIFECYCLE: PM/program archetype

State role assignments and one-sentence rationale per role. No invented roles.

---

**Step 2 -- Null Hypothesis Gate**

Run the inertia-advocate first. Domain reviewers do not see this section.

```
## Null Hypothesis Gate -- [challenger role]
**Null hypothesis**: [what the team does today instead of building this]
**Challenge**: [does the artifact address the status quo case?]
**Findings**: [2-3 findings: switching costs, workaround viability, adoption friction]
**Severity**: HIGH | MEDIUM | LOW
**Verify Question**: [one from challenger's lens.verify]
**Gate Verdict (g_null)**: FAIL | CONDITIONAL | PASS

**Local Gate Ledger:**
| Gate Verdict | Class | Finding Reference | Action |
|-------------|-------|-------------------|--------|
| [g_null] | [from CLASS DERIVATION RULE] | inertia-advocate / [5-word summary] | [synthesis action] |
```

Add one row per FAIL or CONDITIONAL verdict. Advisory rows optional.
Domain sections begin only after this Local Gate Ledger is complete.

---

**Step 3 -- Domain Reviewer**

For each selected domain reviewer:

```
## Domain Reviewer: [role] ([archetype])
**Findings**: [2-4 findings from this role's lens.verify and expertise.depth; must not echo
  null hypothesis gate framing or other domain reviewer framing]
**Severity**: HIGH | MEDIUM | LOW
**Recommendation**: [one concrete action]
**Verify Question**: [one from this role's lens.verify]
**Simplify**: [one from this role's lens.simplify]
**Gate Verdict (g_domain)**: FAIL | CONDITIONAL | PASS

**Local Gate Ledger:**
| Gate Verdict | Class | Finding Reference | Action |
|-------------|-------|-------------------|--------|
| [g_domain] | [from CLASS DERIVATION RULE] | [role] / [5-word summary] | [synthesis action] |
```

One row minimum per FAIL or CONDITIONAL verdict.

---

**Step 4 -- Lifecycle Reviewer**

```
## Lifecycle Reviewer: [role] ([archetype])
**Findings**: [2-3 findings: commitment readiness, decision sufficiency, program concerns]
**Severity**: HIGH | MEDIUM | LOW
**Recommendation**: [one concrete action]
**Verify Question**: [one from this role's lens.verify]
**Simplify**: [one from this role's lens.simplify]
**Gate Verdict (g_lifecycle)**: FAIL | CONDITIONAL | PASS

**Local Gate Ledger:**
| Gate Verdict | Class | Finding Reference | Action |
|-------------|-------|-------------------|--------|
| [g_lifecycle] | [from CLASS DERIVATION RULE] | [role] / [5-word summary] | [synthesis action] |
```

---

**Step 5 -- Master Action Register (Consolidation)**

Copy all Local Gate Ledger rows from Steps 2-4 into the master table. Do not re-derive Gate
Verdict or Class -- copy them exactly from each local row. Any row whose Class contradicts the
Gate Verdict per the CLASS DERIVATION RULE is a structural defect.

```
## Master Action Register
(Consolidated from local Gate Ledger rows -- no re-derivation)

| # | Gate Verdict | Class | Finding Reference | Action |
|---|--------------|-------|-------------------|--------|
```

---

**Step 6 -- Synthesis and Disposition**

Write 5-8 sentences:
- highest-severity finding across all reviewers
- cross-role conflicts (two reviewers with incompatible recommendations)
- convergence areas (multiple reviewers flagging the same gap)
- null hypothesis gate verdict (g_null) explicitly
- why the disposition follows

```
DISPOSITION: READY | CONDITIONAL | BLOCKED
```

- BLOCKED: any gate = FAIL
- CONDITIONAL: no FAIL, at least one CONDITIONAL
- READY: all PASS

**Artifact to review:**

{{artifact}}

---

## V-04 -- Combination: Conversational Register + C-12 + C-13 + C-14 + C-15

**Variation axes**: Phrasing register (conversational imperative, V-01 base) + CLASS DERIVATION
CONTRACT (C-12) + three template variables `{{artifact_id}}`, `{{depth}}`, `{{reviewer_set}}`
(C-13 + C-15) + Gate Verdict column in action register (C-14); Gold path targeting 110/125

**Hypothesis**: V-01 tests register as a single axis; this combination layers all four
automation/auditability criteria onto the conversational base to confirm that the conversational
register does not degrade compliance with the derivation contract or the template variable
acknowledgment requirement. If V-04 scores equal to R3-V04 formal version (110/125), register
is confirmed as a free variable. If it scores lower, the formal register provides a compliance
advantage for automation criteria. If it scores higher, conversational imperative is the
preferred style for structured compliance.

---

**Template inputs:**

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .roles/signal/
```

Emit this block before anything else. Fill in the injected values.

```
## Review Parameters
Artifact:     {{artifact_id}}
Depth:        {{depth}}
Reviewer set: {{reviewer_set}}
```

---

You're running org-review on {{artifact_id}}. Distribute it to reviewers from
`.roles/signal/`, collect structured findings, and emit a commitment disposition.

Before any reviewer runs, read this contract. It does not change.

**CLASS DERIVATION CONTRACT** -- action item classes derive mechanically from gate verdicts.
Do not re-assign class at synthesis time.

```
FAIL gate        -->  BLOCKED      (must resolve before any commitment)
CONDITIONAL gate -->  CONDITIONAL  (must resolve before proceeding)
PASS + HIGH      -->  CONDITIONAL  (HIGH finding retained even at PASS gate)
PASS + LOW       -->  ADVISORY     (may defer)
```

Any action item whose class contradicts the gate verdict that sourced it is a structural defect.

**Severity:**
- HIGH: blocks commitment
- MEDIUM: conditions commitment; proceed only after fix
- LOW: advisory; doesn't block

---

**1. Scope declaration.** Write this before any reviewer section.

```
In scope:
  - Artifact: {{artifact_id}}
  - Surfaces: [spec text, design constraints, named prior decisions]
Out of scope:
  - [surfaces not being reviewed]
```

Flag anything found mid-review that isn't listed here. Don't silently add it to scope.

---

**2. Reviewer selection.** Read `.roles/signal/`. No invented roles.

Branch on `{{reviewer_set}}`:
- Not "auto": use those roles exactly. If inertia-advocate is missing, add it and note the addition.
- "auto" + "standard": pick roles relevant to this artifact type. Min 2 domain roles.
  One reason per role.
- "auto" + "deep": all roles. State total count.

Emit the manifest before any reviewer runs:

```
Depth mode: {{depth}}
Reviewer set: {{reviewer_set}}
Reviewer manifest:
  - [role]: [archetype] -- [rationale | "explicit" | "all roles"]
```

---

**3. Run the inertia-advocate first.** Domain reviewers don't see this section.

```
## Null Hypothesis Gate -- inertia-advocate
Status quo:      [what the team does today instead of building this]
Challenge:       [does the artifact address it?]
Findings:        [2-3: switching costs, workaround viability, adoption friction]
Severity:        HIGH | MEDIUM | LOW
Verify Question: [one from inertia-advocate's lens.verify]
Gate Verdict:    FAIL | CONDITIONAL | PASS
```

Domain sections start only after Gate Verdict is emitted.

---

**4. Run each domain reviewer.** Keep findings distinct per reviewer. Don't echo the
challenger. Cross-role homogeneity in findings is a structural defect.

```
## Reviewer: [role] ([archetype])
Findings:     [2-4 from this role's lens.verify and expertise.depth]
Severity:     HIGH | MEDIUM | LOW
Recommend:    [one concrete action from this role's frame]
Verify:       [one from this role's lens.verify]
Simplify:     [one from this role's lens.simplify]
Gate Verdict: FAIL | CONDITIONAL | PASS
```

---

**5. Build the action register.** Apply CLASS DERIVATION CONTRACT. The Gate Verdict column
is mandatory -- don't omit it, rename it, or defer it.

```
## Action Register
(Classes per CLASS DERIVATION CONTRACT -- no editorial re-assessment)

| # | Gate Verdict | Class | Finding Reference | Action |
|---|--------------|-------|-------------------|--------|
```

Columns:
- Gate Verdict: copy from the reviewer section that produced this item (FAIL / CONDITIONAL / PASS)
- Class: from the contract, not editorial judgment
- Finding Reference: `[role] / [5-word summary]`
- Action: synthesis -- not verbatim recommendation copy

One row minimum per FAIL or CONDITIONAL verdict.

---

**6. Write the synthesis.** 5-8 sentences:
- highest-severity finding across all reviewers
- any cross-role conflict
- convergence areas
- null hypothesis gate verdict -- name it explicitly
- why the disposition follows

Then emit:

```
DISPOSITION: READY | CONDITIONAL | BLOCKED
```

- BLOCKED: any gate = FAIL
- CONDITIONAL: no FAIL, any CONDITIONAL
- READY: all PASS

Disposition cannot contradict a FAIL null hypothesis verdict without explanation.

---

**Artifact to review:**

{{artifact_id}} content:

{{artifact}}

---

## V-05 -- Combination: Alternatives Table + Full Stack (C-09 + C-10 + C-11 + C-12 + C-13 + C-14 + C-15)

**Variation axes**: Inertia framing (Alternatives Table with dimension scoring, V-02 base) +
adversarial bracket (C-09) + disposition formula pre-committed (C-10) + labeled override field
(C-11) + CLASS DERIVATION CONTRACT (C-12) + three template variables (C-13 + C-15) + Gate
Verdict column (C-14); targeting 125/125

**Hypothesis**: R3-V05 combines bracket + disposition formula + class derivation + template
variables + Gate Verdict column via a formal phase-labeled structure. This variation introduces
a genuinely different mechanism for C-09/C-10: the Alternatives Table is the structural anchor
for the bracket. The Bracket Opening populates the table; domain reviewers each re-score the
dimensions from their frame; the Bracket Closing reassesses the aggregate table (challenger vs
domain-adjusted) and emits a revised g_null with override if domain re-reads unjustifiably
inflated artifact scores. The table makes the override decision auditable without re-reading
reviewer narrative -- matching the auditability goal of C-14. A domain PASS that doesn't address
the challenger's dimension gaps is now visibly non-compliant in the table itself, not just in
prose. Target: 125/125 via the alternatives-table bracket path.

---

**Template inputs:**

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .roles/signal/
```

**Acknowledgment block (emit first, before §0):**

```
## Review Parameters
Artifact:     {{artifact_id}}
Depth:        {{depth}}
Reviewer set: {{reviewer_set}}
```

---

You are running `org-review` on the artifact provided below.

**Severity Semantics:**

| Label | Commit-gate meaning |
|-------|---------------------|
| HIGH | Blocks commitment. |
| MEDIUM | Conditions commitment; proceed only after remediation. |
| LOW | Advisory; proceed regardless. |

**DISPOSITION CONTRACT** (committed before any reviewer runs; the synthesis evaluates this
formula -- it does not produce a new one):

```
DISPOSITION FORMULA:
  if   any gate verdict = FAIL                    -->  DISPOSITION = BLOCKED
  elif Override invoked = YES  (see §3)            -->  DISPOSITION = BLOCKED
  elif any gate verdict = CONDITIONAL              -->  DISPOSITION = CONDITIONAL
  elif all gate verdicts = PASS                    -->  DISPOSITION = READY
  else                                             -->  DISPOSITION = CONDITIONAL  (ambiguous)
```

Gates that produce verdicts: Bracket Opening (§1.5), domain reviewers (§2), Bracket Closing (§3).
The formula is the evaluator. Editorial judgment at summary time does not override it.

**CLASS DERIVATION CONTRACT** (committed before any reviewer runs):

```
FAIL gate        -->  BLOCKED
CONDITIONAL gate -->  CONDITIONAL
PASS + HIGH      -->  CONDITIONAL
PASS + LOW       -->  ADVISORY
```

No item's class is assigned editorially at synthesis time.

**NULL HYPOTHESIS DERIVATION RULE** (committed before any reviewer runs; Opening Verdict
is derived from the score differential -- do not assert it, derive it):

```
Dimensions (scored 1-5 per alternative):
  D1 -- Switching cost       (1 = prohibitive, 5 = negligible)
  D2 -- Coverage             (1 = partial, 5 = complete)
  D3 -- Adoption friction    (1 = high, 5 = frictionless)
  D4 -- Time-to-value        (1 = months, 5 = immediate)

Score differential = Artifact total - Status Quo total

Opening Verdict derivation:
  differential >= +6   -->  Opening Verdict = PASS
  differential +1..+5  -->  Opening Verdict = CONDITIONAL
  differential <= 0    -->  Opening Verdict = FAIL
```

The Bracket Closing may re-derive this verdict using domain-adjusted scores. If the
re-derived verdict changes the category, Bracket Closing emits the revised verdict and may
invoke override if domain re-reads are unjustified.

---

**§0 -- Scope Declaration**

```
IN SCOPE:
- Artifact: {{artifact_id}}
- Surfaces: [spec text, design constraints, named prior decisions]
OUT OF SCOPE:
- [surfaces not reviewed in this pass]
```

Any surface discovered mid-review not listed above is a scope gap -- flag it, don't absorb it.

---

**§1 -- Role Selection**

Read `.roles/signal/`. Enumerate all roles.
Depth: `{{depth}}`
Reviewer set: `{{reviewer_set}}`

Procedure:
1. If `{{reviewer_set}}` is not "auto": use those roles exactly. Inertia-advocate must still be
   included for bracket positions; if not named, add it and note the addition.
2. "auto" + "standard": select roles relevant to this artifact type. Min 2 domain roles.
   One-sentence rationale per role.
3. "auto" + "deep": all roles. State total count.

Inertia-advocate is reserved for §1.5 and §3 (bracket positions only).

```
Depth mode: {{depth}}
Reviewer set: {{reviewer_set}}
Reviewer manifest:
  - [role]: [archetype] -- [rationale | "explicit" | "deep run"]
  ...
  (inertia-advocate: reserved for bracket positions -- §1.5 and §3)
```

No invented roles.

---

**§1.5 -- Bracket Opening: Challenger Pre-Domain Testimony**

This section runs before all domain reviewers. Domain reviewers have not seen it.

```
## Bracket Opening -- inertia-advocate

**Status quo statement**: [what the team does today instead of building this -- one sentence]

**Alternatives Table (challenger frame):**

| Dimension            | Status Quo | This Artifact | Rationale                    |
|----------------------|-----------|---------------|------------------------------|
| D1 Switching cost    | [1-5]     | [1-5]         | [one sentence per cell]      |
| D2 Coverage          | [1-5]     | [1-5]         | [one sentence]               |
| D3 Adoption friction | [1-5]     | [1-5]         | [one sentence]               |
| D4 Time-to-value     | [1-5]     | [1-5]         | [one sentence]               |
| **TOTAL**            | [sum]     | [sum]         |                              |

**Score differential**: [artifact total] - [status quo total] = [+/- n]
**NULL HYPOTHESIS DERIVATION RULE applied**: [which branch]

**Challenge to domain reviewers**: [one specific question that domain reviewers must address
  to change any of these dimension scores; this is the anchor all downstream reviewers
  respond to]

**Findings**: [2-3 narrative findings from challenger's lens.verify supporting the table scores]
**Severity**: HIGH | MEDIUM | LOW
**Verify Question**: [one from inertia-advocate's lens.verify]
**Opening Verdict**: FAIL | CONDITIONAL | PASS
```

Domain sections begin only after Opening Verdict is emitted.

---

**§2 -- Domain Reviewer Sections**

Domain reviewers have access to the artifact only. They have not seen §1.5.

For each selected domain reviewer:

1. Load role file from `.roles/signal/{role}.md`.
2. Apply `orientation.frame` to the artifact.
3. Re-score each dimension from this role's technical frame. Mark unchanged dimensions explicitly.
4. Emit:

```
## Domain Reviewer: [role] ([archetype])

**Domain re-read of alternatives table**
(Challenger's challenge: "[copy challenge text from §1.5]")

| Dimension            | Challenger Score | Revised Score | Justification or "unchanged" |
|----------------------|-----------------|---------------|-------------------------------|
| D1 Switching cost    | [challenger]    | [1-5]         | [sentence]                    |
| D2 Coverage          | [challenger]    | [1-5]         | [sentence]                    |
| D3 Adoption friction | [challenger]    | [1-5]         | [sentence]                    |
| D4 Time-to-value     | [challenger]    | [1-5]         | [sentence]                    |

**[This role's null hypothesis address]**: [does the technical approach make the status quo
  obsolete? One sentence. Must differ from challenger's framing.]

**Findings**: [2-4 findings from this role's lens.verify and expertise.depth; must not echo
  §1.5 framing or other domain reviewers]
**Severity**: HIGH | MEDIUM | LOW
**Recommendation**: [one concrete action]
**Verify Question**: [one from this role's lens.verify]
**Simplify**: [one from this role's lens.simplify]
**Gate Verdict**: FAIL | CONDITIONAL | PASS
```

---

**§3 -- Bracket Closing: Challenger Post-Domain Reassessment**

After all domain sections complete. The inertia-advocate now has access to all domain re-reads.

The Bracket Closing answers one question: *Do the domain-adjusted dimension scores, taken in
aggregate, constitute sufficient evidence to defeat the null hypothesis stated in §1.5?*

The inertia-advocate carries override authority: if domain reviewers collectively PASS but
revised table scores are unjustified or still fail to defeat the status quo, the Bracket
Closing may override.

```
## Bracket Closing -- inertia-advocate (post-domain reassessment)

**Domain re-read aggregation:**

| Reviewer | D1 | D2 | D3 | D4 | Null Hypothesis Address | Challenge Answered? |
|----------|----|----|----|----|-----------------------|---------------------|
| [role]   | [revised] | [revised] | [revised] | [revised] | [one sentence] | yes / partial / no |

**Revised Alternatives Table (challenger vs domain-aggregate):**

| Dimension            | Status Quo | Artifact (challenger) | Artifact (domain avg) | Accepted Score |
|----------------------|-----------|----------------------|----------------------|----------------|
| D1 Switching cost    | [SQ]      | [challenger]         | [domain avg]         | [final]        |
| D2 Coverage          | [SQ]      | [challenger]         | [domain avg]         | [final]        |
| D3 Adoption friction | [SQ]      | [challenger]         | [domain avg]         | [final]        |
| D4 Time-to-value     | [SQ]      | [challenger]         | [domain avg]         | [final]        |
| **TOTAL**            | [SQ sum]  |                      |                      | [final sum]    |

**Revised score differential**: [final artifact sum] - [SQ sum] = [+/- n]
**NULL HYPOTHESIS DERIVATION RULE re-applied**: [which branch; state if verdict changes from §1.5]

**Assessment**: [Does the domain-adjusted table change the verdict? What remains unaddressed?]

**Override authority**: If domain re-reads inflate artifact scores without technical justification,
  or if the adjusted verdict still indicates CONDITIONAL or FAIL, the Bracket Closing may override.
  State explicitly if invoked.

**Closing Verdict**: FAIL | CONDITIONAL | PASS
**Override invoked**: YES | NO
```

This field is mandatory. Emit YES or NO regardless of whether override is exercised.
- If YES: "Bracket Closing overrides per DISPOSITION CONTRACT -- DISPOSITION = BLOCKED."
- If NO: domain verdicts stand; Closing Verdict feeds DISPOSITION CONTRACT normally.

---

**§4 -- Action Register**

Using the CLASS DERIVATION CONTRACT. The Gate Verdict column is mandatory.

```
## Action Register
(Classes derived per CLASS DERIVATION CONTRACT -- no editorial re-assessment)

| # | Gate Verdict | Class | Finding Reference | Action |
|---|--------------|-------|-------------------|--------|
```

Columns:
- **Gate Verdict**: copy from the producing section (§1.5, §2, or §3) -- FAIL / CONDITIONAL / PASS
- **Class**: applied from the derivation contract, not re-assessed here
- **Finding Reference**: `[§] / [role] / [5-word summary]`
- **Action**: synthesis -- not verbatim recommendation copy

If Override invoked = YES in §3: add a BLOCKED row:
`§3 / inertia-advocate / override invoked → BLOCKED`

Minimum: one row per FAIL or CONDITIONAL gate verdict.

---

**§5 -- Integrating Summary and Disposition**

Write 5-8 sentences:
- Name the highest-severity finding across all sections
- Name cross-role conflicts (two domain reviewers with incompatible recommendations)
- Name convergence areas
- Reference Opening Verdict (§1.5) and Closing Verdict (§3) explicitly -- include score
  differentials
- State whether Override invoked = YES or NO and the consequence
- Name which DISPOSITION CONTRACT branch applies

Apply the DISPOSITION CONTRACT from the preamble. State which branch.

```
## §5 -- Synthesis
[5-8 sentence synthesis]

FORMULA APPLIED: [state which branch of DISPOSITION CONTRACT applies and why]

DISPOSITION: READY | CONDITIONAL | BLOCKED
```

The synthesis explains the disposition. It does not produce a new formula.

---

**Artifact to review:**

{{artifact_id}} artifact content:

{{artifact}}
