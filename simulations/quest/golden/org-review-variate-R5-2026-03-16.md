# org-review Variations — Round 5 (v4 rubric, 2026-03-16)
Generated: 2026-03-16
Skill: org-review
Rubric: simulations/quest/rubrics/org-review-rubric-v4-2026-03-16.md

Prior round summary:
- R1 (v1 rubric): V-05=95 (C-09+C-10+C-11+C-12), V-04=90 (C-13).
- R2 (v2 rubric / v3 retroactive): V-04=110 (C-12+C-13+C-14+C-15). First Gold.
- R3 (v3 rubric): V-04=110, V-05=125 (full stack). Aspirational frontier closed.
- R4 (v3 → v4 rubric): V-05=135 (C-16+C-17 PASS, C-18 FAIL), V-03=100 (C-18 PASS, no bracket).
  V-05 R4 at 135/140 is the high-water mark. Perfect (140) requires all three R4 patterns
  simultaneously: C-16 (Alternatives Table bracket), C-17 (three-contract preamble), C-18
  (inline gate ledger). No R4 variant achieved all three.

Round 5 strategy:
- Three unexplored single-axis axes: role sequence, lifecycle emphasis format, finding ID anchoring.
- Two 140-attempt combinations: one starting from V-05 R4 (C-16+C-17 proven) and adding C-18;
  one starting from V-03 R4 (C-18 proven) and adding C-16+C-17.
- V-01: single axis -- role sequence (lifecycle commitment gate before domain testimony)
- V-02: single axis -- lifecycle emphasis (structured 5-item commitment checklist replaces open findings)
- V-03: single axis -- output format (named Finding IDs F-XX as positional anchors throughout)
- V-04: combination -- V-05 R4 full stack + inline gate ledger added to every section (high-end path to 140)
- V-05: combination -- V-03 R4 inline ledger base + Alternatives Table bracket + three-contract preamble (low-end path to 140)

Expected score ladder (v4 rubric, 140 pts max):
  V-01: 60+30+5(C-10)+5(C-12)+5(C-13)+5(C-14)+5(C-15)+5(C-17)=120  -- Gold (lifecycle-first;
        no bracket so C-09/C-11/C-16 inactive; C-17 adds three-contract preamble including g_null rule)
  V-02: 60+30+5(C-10)+5(C-12)+5(C-13)+5(C-14)+5(C-15)=110           -- Gold floor (checklist
        lifecycle; structured verdict derivation; same stack as R3-V04)
  V-03: 60+30+5(C-10)+5(C-12)+5(C-13)+5(C-14)+5(C-15)=110           -- Gold (F-ID anchoring;
        finding-graph traceability; same stack but tests whether ID anchoring degrades any criterion)
  V-04: 60+30+50=140                                                   -- Perfect attempt (V-05 R4
        base + C-18 added; first variant to combine C-16+C-17+C-18 from high-end construction)
  V-05: 60+30+50=140                                                   -- Perfect attempt (V-03 R4
        base + C-16+C-17 added; alternative construction path from C-18 foundation)

---

## V-01 -- Role Sequence: Lifecycle Gate Before Domain Testimony

**Variation axis**: Role sequence -- the lifecycle/program reviewer runs as a second gate
immediately after the null hypothesis gate and before any domain reviewer sections; domain
reviewers are given the lifecycle gate verdict as declared context and must address it explicitly;
the role ordering is: inertia-advocate (null hypothesis) → lifecycle (commitment readiness) →
domain reviewers → synthesis

**Hypothesis**: All prior variants treat lifecycle as a closing check -- the PM/program reviewer
assesses implementation readiness after domain reviewers have established technical quality.
This treats lifecycle as posterior to technical judgment. Sequencing lifecycle as a pre-domain
gate inverts the dependency: commitment readiness is established before technical review begins,
and domain reviewers respond to a declared commitment context ("the program has flagged X as a
commitment-readiness concern -- does your domain frame corroborate or contradict this?"). If
lifecycle-first produces more coherent synthesis (C-07) by giving domain reviewers an explicit
commitment frame to respond to, this axis has quality value independent of aspirational criteria.
If it does not change scores, lifecycle sequencing is confirmed as a free variable.

---

**Template inputs:**

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .craft/roles/signal/
```

Emit this acknowledgment block before §0. Fill in the injected values.

```
## Review Parameters
Artifact:     {{artifact_id}}
Depth:        {{depth}}
Reviewer set: {{reviewer_set}}
```

---

You are running `org-review` on the artifact provided below.

Read all three contracts before any reviewer section executes. They do not change.

**DISPOSITION CONTRACT** (the synthesis applies this formula -- it does not produce a new one):

```
DISPOSITION FORMULA:
  if   any gate verdict = FAIL                -->  DISPOSITION = BLOCKED
  elif any gate verdict = CONDITIONAL         -->  DISPOSITION = CONDITIONAL
  elif all gate verdicts = PASS               -->  DISPOSITION = READY
  else                                        -->  DISPOSITION = CONDITIONAL  (ambiguous -- treat as conditional)
```

g_null = FAIL always yields BLOCKED. Domain or lifecycle PASS does not override g_null FAIL.

**CLASS DERIVATION CONTRACT** (action item classes derive mechanically from gate verdicts;
do not re-assign class at synthesis time):

```
FAIL gate        -->  BLOCKED      (must resolve before any commitment)
CONDITIONAL gate -->  CONDITIONAL  (must resolve before proceeding)
PASS + HIGH      -->  CONDITIONAL  (HIGH finding retained even at PASS gate)
PASS + LOW       -->  ADVISORY     (may defer)
```

**NULL HYPOTHESIS DERIVATION RULE** (g_null derives from the inertia-advocate's gate verdict;
the inertia-advocate reaches that verdict by structured evaluation of switching cost, coverage,
and adoption friction -- they do not assert g_null, they derive it from findings):

```
Any finding rated HIGH in switching cost, coverage gap, or adoption friction  -->  g_null = FAIL
All findings rated MEDIUM, no HIGH  -->  g_null = CONDITIONAL
All findings rated LOW  -->  g_null = PASS
```

The inertia-advocate applies this rule. The composite verdict governs §0 gate output.

**Severity Semantics** (applies throughout):

| Severity | Commit-gate meaning |
|----------|---------------------|
| HIGH | Blocks commitment to proceed |
| MEDIUM | Conditions commitment; proceed only after remediation |
| LOW | Advisory; proceed regardless |

---

**§0 -- Scope Declaration**

Before any reviewer section:

```
IN SCOPE:
- Artifact: {{artifact_id}}
- Surfaces: [spec text, design constraints, named prior decisions]
OUT OF SCOPE:
- [surfaces not reviewed in this pass]
```

Any surface discovered mid-review not listed above is a scope gap. Flag it; do not absorb it.

---

**§1 -- Role Selection**

Read `.craft/roles/signal/`. No invented roles.

Branch on `{{reviewer_set}}`:
- Not "auto": use those roles exactly. If inertia-advocate or lifecycle role is missing, add it
  and note the addition.
- "auto" + "standard": select the CHALLENGER slot (inertia-advocate archetype), LIFECYCLE slot
  (PM/program archetype), and >= 2 DOMAIN slots (technical/architecture archetype) relevant to
  this artifact type. State role assignment and one-sentence rationale per role.
- "auto" + "deep": all roles in the directory. State total count.

Emit the manifest before any reviewer section runs:

```
Depth mode: {{depth}}
Reviewer set: {{reviewer_set}}
Reviewer manifest:
  - [role]: [archetype] -- [rationale | "explicit" | "all roles"]
    SLOT: CHALLENGER | LIFECYCLE | DOMAIN
```

---

**§2 -- Null Hypothesis Gate (Inertia-Advocate)**

This section runs before lifecycle and domain reviewers. Neither lifecycle nor domain reviewers
have seen this section.

Apply the NULL HYPOTHESIS DERIVATION RULE. Do not assert g_null -- derive it.

```
## §2 -- Null Hypothesis Gate -- [challenger role]

**Status quo statement**: [what the team does today instead of building this -- one sentence]
**Challenge**: [does the artifact address the status quo case?]
**Findings**:
  F-NH-1: [finding: switching cost] | Severity: HIGH | MEDIUM | LOW
  F-NH-2: [finding: workaround viability] | Severity: HIGH | MEDIUM | LOW
  F-NH-3: [finding: adoption friction] | Severity: HIGH | MEDIUM | LOW
**Verify Question**: [one from challenger's lens.verify]
**NULL HYPOTHESIS DERIVATION RULE applied**: [which branch; cite highest-severity finding]
**Gate Verdict (g_null)**: FAIL | CONDITIONAL | PASS
```

---

**§3 -- Lifecycle Commitment Gate**

This section runs after §2 and before any domain reviewer. Domain reviewers have not seen §2
or §3 -- they receive only the artifact.

The lifecycle reviewer assesses whether the team is ready to make a commitment decision at this
point. They do not evaluate technical quality (that is domain's scope). They evaluate decision
readiness: Is the artifact sufficiently specified? Are dependencies declared? Are risks stated
and owned?

The lifecycle gate produces a verdict (g_lifecycle) that domain reviewers are given as context.
Domain reviewers must acknowledge this verdict in their sections.

```
## §3 -- Lifecycle Commitment Gate -- [lifecycle role] ([archetype])

**Commitment readiness assessment**: [2-3 sentences: is this artifact ready for a commitment
  decision? Is scope complete, risks stated, dependencies declared? Reference the artifact
  directly -- not the null hypothesis verdict, which domain reviewers haven't seen.]
**Findings**:
  F-LC-1: [finding: scope completeness] | Severity: HIGH | MEDIUM | LOW
  F-LC-2: [finding: risk declaration] | Severity: HIGH | MEDIUM | LOW
  F-LC-3: [finding: dependency readiness] | Severity: HIGH | MEDIUM | LOW
**Verify Question**: [one from this role's lens.verify]
**Simplify**: [one from this role's lens.simplify]
**Gate Verdict (g_lifecycle)**: FAIL | CONDITIONAL | PASS
```

---

**§4 -- Domain Reviewer Sections**

Domain reviewers have access to the artifact and the g_lifecycle verdict from §3 only. They
have not seen §2 (null hypothesis gate) or §3 findings.

For each selected domain reviewer, state at the opening: "Lifecycle gate verdict: [g_lifecycle]."
Each domain reviewer must explicitly address whether their findings affect or corroborate the
lifecycle gate verdict in at least one sentence.

Keep findings distinct per reviewer. Cross-role homogeneity in findings is a structural defect.

```
## §4 -- Domain Reviewer: [role] ([archetype])

Lifecycle gate verdict declared: [g_lifecycle]

**Findings**: [2-4 findings from this role's lens.verify and expertise.depth; must not echo
  other domain reviewer framing; at least one finding must relate to whether the lifecycle
  gate verdict is supported or contradicted by this domain frame]
**Severity**: HIGH | MEDIUM | LOW
**Recommendation**: [one concrete action from this role's frame]
**Verify Question**: [one from this role's lens.verify]
**Simplify**: [one from this role's lens.simplify]
**Gate Verdict (g_domain_[role])**: FAIL | CONDITIONAL | PASS
```

---

**§5 -- Action Register**

Apply CLASS DERIVATION CONTRACT. Gate Verdict column is mandatory.

```
## §5 -- Action Register
(Classes per CLASS DERIVATION CONTRACT -- no editorial re-assessment)

| # | Gate Verdict | Class | Finding Reference | Action |
|---|--------------|-------|-------------------|--------|
```

Columns:
- **Gate Verdict**: copy from the producing section (§2, §3, §4) -- FAIL / CONDITIONAL / PASS
- **Class**: applied from the derivation contract, not re-assessed here
- **Finding Reference**: `[§] / [role] / [finding label or 5-word summary]`
- **Action**: synthesis -- not verbatim recommendation copy

Minimum: one row per FAIL or CONDITIONAL gate verdict.

---

**§6 -- Synthesis and Disposition**

Write 5-8 sentences:
- Name the highest-severity finding across all sections
- Name cross-role conflicts: instances where a domain reviewer contradicted or corroborated
  the lifecycle gate verdict from §3
- Name convergence areas (multiple reviewers flagging the same gap)
- Reference g_null (§2) and g_lifecycle (§3) by name
- State which branch of the DISPOSITION CONTRACT applies and why

Apply the DISPOSITION CONTRACT from the preamble. State the branch.

```
## §6 -- Synthesis

[5-8 sentences]

FORMULA APPLIED: [which DISPOSITION CONTRACT branch]

DISPOSITION: READY | CONDITIONAL | BLOCKED
```

---

**Artifact to review:**

{{artifact_id}} content:

{{artifact}}

---

## V-02 -- Lifecycle Emphasis: Structured Commitment Readiness Checklist

**Variation axis**: Lifecycle emphasis -- the lifecycle reviewer section is replaced by a
5-item Commitment Readiness Checklist; each item produces its own PASS / CONDITIONAL / FAIL
verdict; the overall lifecycle gate verdict is derived mechanically from checklist item
verdicts via a stated rule; the lifecycle reviewer does not produce open-ended findings but
instead evaluates each checklist item against the artifact

**Hypothesis**: Prior variants treat the lifecycle reviewer as a findings-first role -- the PM
or program manager generates narrative observations that produce a single gate verdict. This
creates the same editorial-at-execution failure mode that C-10 and C-12 address for the
overall disposition: the reviewer generates findings then decides the verdict, rather than
evaluating structured criteria. A Commitment Readiness Checklist is the lifecycle analog of
the Disposition Formula: it states the evaluation criteria before any review happens, then
maps item verdicts to an overall lifecycle verdict mechanically. If this produces more reliable
C-08 compliance (depth parameter honored) and C-07 synthesis coherence, it validates that
formula-first is the correct pattern at the reviewer level, not just the disposition level.

---

**Template inputs:**

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .craft/roles/signal/
```

Emit this acknowledgment block before §0.

```
## Review Parameters
Artifact:     {{artifact_id}}
Depth:        {{depth}}
Reviewer set: {{reviewer_set}}
```

---

You are running `org-review` on the artifact provided below.

Read all pre-commitment contracts before any reviewer section executes.

**DISPOSITION CONTRACT** (the synthesis evaluates this formula -- it does not produce a new one):

```
DISPOSITION FORMULA:
  if   any gate verdict = FAIL                -->  DISPOSITION = BLOCKED
  elif any gate verdict = CONDITIONAL         -->  DISPOSITION = CONDITIONAL
  elif all gate verdicts = PASS               -->  DISPOSITION = READY
  else                                        -->  DISPOSITION = CONDITIONAL
```

**CLASS DERIVATION CONTRACT**:

```
FAIL gate        -->  BLOCKED
CONDITIONAL gate -->  CONDITIONAL
PASS + HIGH      -->  CONDITIONAL
PASS + LOW       -->  ADVISORY
```

**COMMITMENT READINESS DERIVATION RULE** (lifecycle gate verdict g_lifecycle derived
mechanically from checklist item verdicts; do not editorially assess):

```
Checklist items: CR-1 through CR-5 (defined in §3)
Each item verdict: PASS | CONDITIONAL | FAIL

g_lifecycle derivation:
  if   any item = FAIL                -->  g_lifecycle = FAIL
  elif any item = CONDITIONAL         -->  g_lifecycle = CONDITIONAL
  elif all items = PASS               -->  g_lifecycle = PASS
```

The lifecycle reviewer evaluates each checklist item. The rule produces g_lifecycle.

**Severity Semantics**:

| Severity | Commit-gate meaning |
|----------|---------------------|
| HIGH | Blocks commitment to proceed |
| MEDIUM | Conditions commitment; proceed only after remediation |
| LOW | Advisory; proceed regardless |

---

**§0 -- Scope Declaration**

```
IN SCOPE:
- Artifact: {{artifact_id}}
- Surfaces: [spec text, design constraints, named prior decisions]
OUT OF SCOPE:
- [surfaces not reviewed in this pass]
```

Flag any surface discovered mid-review not listed above. Do not absorb it into scope.

---

**§1 -- Role Selection**

Read `.craft/roles/signal/`. No invented roles.

Branch on `{{reviewer_set}}`:
- Not "auto": use those roles exactly. If inertia-advocate or lifecycle role is missing, add it.
- "auto" + "standard": select CHALLENGER (inertia-advocate), LIFECYCLE (PM/program archetype),
  >= 2 DOMAIN (technical/architecture). One-sentence rationale per role.
- "auto" + "deep": all roles. State total count.

```
Depth mode: {{depth}}
Reviewer set: {{reviewer_set}}
Reviewer manifest:
  - [role]: [archetype] -- [rationale | "explicit" | "all roles"]
```

---

**§2 -- Null Hypothesis Gate (Inertia-Advocate)**

Domain reviewers have not seen this section.

```
## §2 -- Null Hypothesis Gate -- [challenger role]

**Status quo**: [what the team does today instead of building this]
**Challenge**: [does the artifact address the status quo case?]
**Findings**: [2-3 findings: switching costs, workaround viability, adoption friction]
**Severity**: HIGH | MEDIUM | LOW
**Verify Question**: [one from challenger's lens.verify]
**Gate Verdict (g_null)**: FAIL | CONDITIONAL | PASS
```

Domain sections begin only after g_null is emitted.

---

**§3 -- Lifecycle Commitment Readiness Gate**

The lifecycle reviewer does not produce free-form findings. They evaluate five structured
checklist items and derive g_lifecycle from item verdicts per the COMMITMENT READINESS
DERIVATION RULE.

Checklist items are defined below. Evaluate each against the artifact.

```
## §3 -- Lifecycle Commitment Readiness Gate -- [lifecycle role] ([archetype])

**CR-1 -- Scope Completeness**
  Evaluation: [Does the artifact define what is in scope, out of scope, and explicitly name
    surfaces under review? Is the boundary unambiguous?]
  Item Verdict: PASS | CONDITIONAL | FAIL
  Severity if non-PASS: HIGH | MEDIUM | LOW

**CR-2 -- Risk Declaration**
  Evaluation: [Does the artifact state known risks, failure modes, and their severity? Are
    risks owned (named owner or mitigation path) or merely listed?]
  Item Verdict: PASS | CONDITIONAL | FAIL
  Severity if non-PASS: HIGH | MEDIUM | LOW

**CR-3 -- Dependency Readiness**
  Evaluation: [Are dependencies on other components, services, or decisions declared? For
    each named dependency, is the dependency status known (resolved / pending / blocked)?]
  Item Verdict: PASS | CONDITIONAL | FAIL
  Severity if non-PASS: HIGH | MEDIUM | LOW

**CR-4 -- Decision Sufficiency**
  Evaluation: [Does the artifact provide enough information to make a commitment decision?
    Are alternatives and tradeoffs stated? Are open questions that would block commitment
    surfaced rather than deferred?]
  Item Verdict: PASS | CONDITIONAL | FAIL
  Severity if non-PASS: HIGH | MEDIUM | LOW

**CR-5 -- Signal Quality**
  Evaluation: [Is the artifact's quality sufficient for a structured org review? Are sections
    complete, recommendations actionable, and findings grounded in the artifact rather than
    general concerns?]
  Item Verdict: PASS | CONDITIONAL | FAIL
  Severity if non-PASS: HIGH | MEDIUM | LOW

**COMMITMENT READINESS DERIVATION RULE applied**:
  [State which branch. List item verdicts: CR-1=[v], CR-2=[v], CR-3=[v], CR-4=[v], CR-5=[v]]

**Gate Verdict (g_lifecycle)**: FAIL | CONDITIONAL | PASS
```

---

**§4 -- Domain Reviewer Sections**

For each selected domain reviewer:

```
## §4 -- Domain Reviewer: [role] ([archetype])

**Findings**: [2-4 findings from this role's lens.verify and expertise.depth; must not echo
  challenger framing or other domain reviewer framing]
**Severity**: HIGH | MEDIUM | LOW
**Recommendation**: [one concrete action from this role's frame]
**Verify Question**: [one from this role's lens.verify]
**Simplify**: [one from this role's lens.simplify]
**Gate Verdict (g_domain)**: FAIL | CONDITIONAL | PASS
```

Cross-role homogeneity in findings is a structural defect.

---

**§5 -- Action Register**

Apply CLASS DERIVATION CONTRACT. Gate Verdict column is mandatory.

```
## §5 -- Action Register
(Classes per CLASS DERIVATION CONTRACT -- no editorial re-assessment)

| # | Gate Verdict | Class | Finding Reference | Action |
|---|--------------|-------|-------------------|--------|
```

- **Gate Verdict**: copy from the producing section (§2, §3, §4)
- **Class**: from the derivation contract, not editorial judgment
- **Finding Reference**: `[§] / [role] / [5-word summary or CR item]`
- **Action**: synthesis, not verbatim recommendation copy

Minimum: one row per FAIL or CONDITIONAL verdict.

---

**§6 -- Synthesis and Disposition**

Write 5-8 sentences:
- Name the highest-severity finding across all sections
- Name cross-role conflicts or convergence
- Reference g_null (§2) and g_lifecycle (§3) by name; cite which CR items drove g_lifecycle
- Explain the disposition

Apply the DISPOSITION CONTRACT. State which branch.

```
## §6 -- Synthesis

[5-8 sentences]

FORMULA APPLIED: [which DISPOSITION CONTRACT branch]

DISPOSITION: READY | CONDITIONAL | BLOCKED
```

---

**Artifact to review:**

{{artifact_id}} content:

{{artifact}}

---

## V-03 -- Output Format: Named Finding IDs as Positional Anchors

**Variation axis**: Output format -- each finding across all reviewer sections receives a
sequential Finding ID (F-01, F-02, F-03...) at the moment it is emitted; all subsequent
cross-references (action register, synthesis, gate verdicts) use Finding IDs as stable
positional anchors; the action register maps F-ID → Gate Verdict → Class → Action; the
synthesis references findings by F-ID

**Hypothesis**: Prior variants reference findings as `[role] / [5-word summary]`, which
creates brittle references -- two similar findings share ambiguous summaries, and the model
re-describes findings rather than pointing to them. A sequential F-ID emitted at the moment of
finding production creates a stable reference graph: any action item, synthesis statement, or
gate verdict can be traced to the exact finding by ID without re-reading reviewer sections.
This tests whether formal ID anchoring improves C-05 (action item traceability) and C-14
(gate verdict preserved in register) without introducing the full inline ledger mechanism.
If F-ID anchoring achieves the same traceability as inline ledger at lower structural cost,
it is a simpler path to the same auditability goal.

---

**Template inputs:**

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .craft/roles/signal/
```

Emit this acknowledgment block before §0.

```
## Review Parameters
Artifact:     {{artifact_id}}
Depth:        {{depth}}
Reviewer set: {{reviewer_set}}
```

---

You are running `org-review` on the artifact provided below.

Read these contracts before any reviewer section executes.

**DISPOSITION CONTRACT**:

```
DISPOSITION FORMULA:
  if   any gate verdict = FAIL                -->  DISPOSITION = BLOCKED
  elif any gate verdict = CONDITIONAL         -->  DISPOSITION = CONDITIONAL
  elif all gate verdicts = PASS               -->  DISPOSITION = READY
  else                                        -->  DISPOSITION = CONDITIONAL
```

**CLASS DERIVATION CONTRACT**:

```
FAIL gate        -->  BLOCKED
CONDITIONAL gate -->  CONDITIONAL
PASS + HIGH      -->  CONDITIONAL
PASS + LOW       -->  ADVISORY
```

**Finding ID Protocol**: Findings are numbered sequentially F-01, F-02, F-03... across all
reviewer sections in the order they are emitted. The ID is assigned at the moment the finding
is written. All references to findings -- in gate verdicts, the action register, and synthesis
-- use the F-ID, not role/summary strings. The master finding index is assembled at §5.

**Severity Semantics**:

| Severity | Commit-gate meaning |
|----------|---------------------|
| HIGH | Blocks commitment to proceed |
| MEDIUM | Conditions commitment; proceed only after remediation |
| LOW | Advisory; proceed regardless |

---

**§0 -- Scope Declaration**

```
IN SCOPE:
- Artifact: {{artifact_id}}
- Surfaces: [spec text, design constraints, named prior decisions]
OUT OF SCOPE:
- [surfaces not reviewed in this pass]
```

Flag any surface discovered mid-review not listed above.

---

**§1 -- Role Selection**

Read `.craft/roles/signal/`. No invented roles.

Branch on `{{reviewer_set}}`:
- Not "auto": use those roles exactly. Add inertia-advocate if absent and note the addition.
- "auto" + "standard": CHALLENGER, LIFECYCLE, >= 2 DOMAIN. One-sentence rationale per role.
- "auto" + "deep": all roles. State total count.

```
Depth mode: {{depth}}
Reviewer set: {{reviewer_set}}
Reviewer manifest:
  - [role]: [archetype] -- [rationale | "explicit" | "all roles"]
```

---

**§2 -- Null Hypothesis Gate (Inertia-Advocate)**

Domain reviewers have not seen this section. Assign Finding IDs starting at F-01.

```
## §2 -- Null Hypothesis Gate -- [challenger role]

**Status quo**: [what the team does today instead of building this]
**Challenge**: [does the artifact address the status quo case?]
**Findings**:
  F-01: [finding text] | Severity: HIGH | MEDIUM | LOW
  F-02: [finding text] | Severity: HIGH | MEDIUM | LOW
  F-03: [finding text, if any] | Severity: HIGH | MEDIUM | LOW
**Verify Question**: [one from challenger's lens.verify]
**Gate Verdict (g_null)**: FAIL | CONDITIONAL | PASS
  [Gate verdict grounds on: F-xx, F-xx]
```

Findings are numbered F-01 upward. Resume sequential numbering in each subsequent section.

---

**§3 -- Domain Reviewer Sections**

For each selected domain reviewer. Continue F-ID sequence from §2.

```
## §3 -- Domain Reviewer: [role] ([archetype])

**Findings**:
  F-[n]: [finding text] | Severity: HIGH | MEDIUM | LOW
  F-[n+1]: [finding text] | Severity: HIGH | MEDIUM | LOW
  [additional findings as needed]
**Recommendation**: [one concrete action from this role's frame]
**Verify Question**: [one from this role's lens.verify]
**Simplify**: [one from this role's lens.simplify]
**Gate Verdict (g_domain)**: FAIL | CONDITIONAL | PASS
  [Gate verdict grounds on: F-xx, F-xx]
```

Cross-role homogeneity in findings is a structural defect. Each reviewer's F-IDs must be
substantively distinct from other reviewers' F-IDs.

---

**§4 -- Lifecycle Reviewer**

Continue F-ID sequence.

```
## §4 -- Lifecycle Reviewer: [role] ([archetype])

**Findings**:
  F-[n]: [finding text] | Severity: HIGH | MEDIUM | LOW
  F-[n+1]: [finding text] | Severity: HIGH | MEDIUM | LOW
  [additional findings as needed]
**Recommendation**: [one concrete action]
**Verify Question**: [one from this role's lens.verify]
**Simplify**: [one from this role's lens.simplify]
**Gate Verdict (g_lifecycle)**: FAIL | CONDITIONAL | PASS
  [Gate verdict grounds on: F-xx, F-xx]
```

---

**§5 -- Finding Index**

Before the action register, emit a consolidated index of all findings:

```
## §5 -- Finding Index

| F-ID | Role | Severity | Summary |
|------|------|----------|---------|
| F-01 | [role] | HIGH/MEDIUM/LOW | [10-word summary] |
| ...  | ...  | ...      | ...     |
```

This index is the source of truth for Finding Reference entries in the action register.

---

**§6 -- Action Register**

Apply CLASS DERIVATION CONTRACT. Gate Verdict column is mandatory.

```
## §6 -- Action Register
(Classes per CLASS DERIVATION CONTRACT -- no editorial re-assessment)

| # | Gate Verdict | Class | Finding Reference | Action |
|---|--------------|-------|-------------------|--------|
```

- **Gate Verdict**: copy from the producing section gate verdict
- **Class**: from the derivation contract
- **Finding Reference**: `F-[ID]` -- use the Finding ID, not a prose summary
- **Action**: synthesis from the finding; not verbatim recommendation copy

Minimum: one row per F-ID that grounded a FAIL or CONDITIONAL gate verdict.

---

**§7 -- Synthesis and Disposition**

Write 5-8 sentences. Reference findings by F-ID throughout (not role/summary strings):
- Highest-severity finding: "F-xx ([role]) is the highest severity finding..."
- Cross-role conflicts: "F-xx and F-yy represent incompatible recommendations..."
- Convergence: "F-xx (role-A), F-yy (role-B), and F-zz (role-C) converge on..."
- g_null gate verdict explicitly: "Null hypothesis gate (§2) returned g_null = [verdict]..."
- Disposition derivation from DISPOSITION CONTRACT

```
## §7 -- Synthesis

[5-8 sentences, findings referenced by F-ID]

FORMULA APPLIED: [which DISPOSITION CONTRACT branch]

DISPOSITION: READY | CONDITIONAL | BLOCKED
```

---

**Artifact to review:**

{{artifact_id}} content:

{{artifact}}

---

## V-04 -- Combination: V-05 R4 Full Stack + Inline Gate Ledger in Every Section (C-16 + C-17 + C-18 Path A)

**Variation axes**: V-05 R4 structure preserved in full (Alternatives Table bracket, three-contract
preamble, all 7 prior aspirational criteria) + inline Local Gate Ledger rows added to EVERY
reviewer section including Bracket Opening (§1.5), each domain section (§2), and Bracket
Closing (§3); master action register assembled by copy from local rows (not re-synthesis)

**Hypothesis**: V-05 R4 scored 135/140 under v4, missing only C-18 (Inline Gate Ledger at
Origin). C-18 requires gate verdict + class to be captured at the moment of verdict emission,
not deferred to the master register. V-05 R4's action register satisfies C-14 (gate verdict
in register) but all verdicts are captured post-hoc at §4 -- there is no local ledger row
within each reviewer section. This variant adds exactly one structural element to V-05 R4:
a Local Gate Ledger row at the end of §1.5, each §2 domain section, and §3. The master
register at §4 explicitly copies from these local rows verbatim rather than synthesizing.
This is Path A to Perfect (140): start from C-16+C-17 proven, add C-18. Path B (V-05) starts
from C-18 proven and adds C-16+C-17.

---

**Template inputs:**

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .craft/roles/signal/
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

Read all pre-commitment contracts before any reviewer section executes. They do not change.

**DISPOSITION CONTRACT** (the synthesis evaluates this formula -- it does not produce a new one):

```
DISPOSITION FORMULA:
  if   any gate verdict = FAIL                    -->  DISPOSITION = BLOCKED
  elif Override invoked = YES  (see §3)           -->  DISPOSITION = BLOCKED
  elif any gate verdict = CONDITIONAL             -->  DISPOSITION = CONDITIONAL
  elif all gate verdicts = PASS                   -->  DISPOSITION = READY
  else                                            -->  DISPOSITION = CONDITIONAL
```

Gates that produce verdicts: Opening Verdict (§1.5), domain gate verdicts (§2), Closing
Verdict (§3). The formula is the evaluator. Editorial judgment at summary time does not
override it.

**CLASS DERIVATION CONTRACT** (committed before any reviewer runs; action classes derive
mechanically from gate verdicts -- do not re-assign at synthesis time):

```
FAIL gate        -->  BLOCKED      (must resolve before any commitment)
CONDITIONAL gate -->  CONDITIONAL  (must resolve before proceeding)
PASS + HIGH      -->  CONDITIONAL  (HIGH finding retained even at PASS gate)
PASS + LOW       -->  ADVISORY     (may defer)
```

**NULL HYPOTHESIS DERIVATION RULE** (committed before any reviewer runs; Opening Verdict
derives from the score differential -- do not assert it, derive it):

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

Bracket Closing (§3) may re-derive Opening Verdict using domain-adjusted scores. If the
re-derived verdict changes the category, Bracket Closing emits the revised verdict and may
invoke override.

**LOCAL GATE LEDGER PROTOCOL** (committed before any reviewer runs; applies in §1.5, §2,
and §3):

Every reviewer section ends with a Local Gate Ledger row. The row captures Gate Verdict +
Class at the moment of verdict emission -- before the master register is assembled. The Class
is assigned by applying the CLASS DERIVATION CONTRACT at the point of origin. The master
register (§4) copies these rows verbatim. It does not re-derive Gate Verdict or Class.

Local Gate Ledger row syntax:

```
**Local Gate Ledger:**
| Gate Verdict | Class | Finding Reference | Action |
|-------------|-------|-------------------|--------|
| [verdict]   | [class per CONTRACT] | [§] / [role] / [5-word summary] | [synthesis action] |
```

Add one row per FAIL or CONDITIONAL verdict. ADVISORY rows are optional.

**Severity Semantics:**

| Label | Commit-gate meaning |
|-------|---------------------|
| HIGH | Blocks commitment. |
| MEDIUM | Conditions commitment; proceed only after remediation. |
| LOW | Advisory; proceed regardless. |

---

**§0 -- Scope Declaration**

```
IN SCOPE:
- Artifact: {{artifact_id}}
- Surfaces: [spec text, design constraints, named prior decisions]
OUT OF SCOPE:
- [surfaces not reviewed in this pass]
```

Any surface discovered mid-review not listed above is a scope gap. Flag it; do not absorb it.

---

**§1 -- Role Selection**

Read `.craft/roles/signal/`. No invented roles.
Depth: `{{depth}}`; Reviewer set: `{{reviewer_set}}`

Procedure:
1. If `{{reviewer_set}}` is not "auto": use those roles exactly. Inertia-advocate must be
   included for bracket positions; if absent, add it and note the addition.
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

---

**§1.5 -- Bracket Opening: Challenger Pre-Domain Testimony**

This section runs before all domain reviewers. Domain reviewers have not seen it.

```
## §1.5 -- Bracket Opening -- inertia-advocate

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
**NULL HYPOTHESIS DERIVATION RULE applied**: [which branch; state the derivation explicitly]

**Challenge to domain reviewers**: [one specific question that domain reviewers must address
  to change any of these dimension scores]

**Findings**: [2-3 narrative findings from challenger's lens.verify supporting the table scores]
**Severity**: HIGH | MEDIUM | LOW
**Verify Question**: [one from inertia-advocate's lens.verify]
**Opening Verdict**: FAIL | CONDITIONAL | PASS
```

Emit Local Gate Ledger row here, immediately after Opening Verdict:

```
**Local Gate Ledger:**
| Gate Verdict | Class | Finding Reference | Action |
|-------------|-------|-------------------|--------|
| [Opening Verdict] | [CLASS DERIVATION CONTRACT applied] | §1.5 / inertia-advocate / [5-word summary] | [synthesis action] |
```

Domain sections begin only after this Local Gate Ledger row is complete.

---

**§2 -- Domain Reviewer Sections**

Domain reviewers have access to the artifact only. They have not seen §1.5.

For each selected domain reviewer:

1. Load role file from `.craft/roles/signal/{role}.md`.
2. Apply `orientation.frame` to the artifact.
3. Re-score each dimension from this role's technical frame. Mark unchanged dimensions explicitly.
4. Emit the section, ending with a Local Gate Ledger row.

```
## §2 -- Domain Reviewer: [role] ([archetype])

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

Emit Local Gate Ledger row here, immediately after Gate Verdict:

```
**Local Gate Ledger:**
| Gate Verdict | Class | Finding Reference | Action |
|-------------|-------|-------------------|--------|
| [verdict] | [CLASS DERIVATION CONTRACT applied] | §2 / [role] / [5-word summary] | [synthesis action] |
```

One row minimum per FAIL or CONDITIONAL verdict.

---

**§3 -- Bracket Closing: Challenger Post-Domain Reassessment**

After all domain sections complete. The inertia-advocate now has access to all domain re-reads.

The Bracket Closing answers: *Do the domain-adjusted dimension scores, taken in aggregate,
constitute sufficient evidence to defeat the null hypothesis stated in §1.5?*

The inertia-advocate carries override authority: if domain reviewers collectively PASS but
revised table scores are unjustified or still fail to defeat the status quo, the Bracket
Closing may override.

```
## §3 -- Bracket Closing -- inertia-advocate (post-domain reassessment)

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

**Override authority**: If domain re-reads inflate artifact scores without technical
  justification, or if the adjusted verdict still indicates CONDITIONAL or FAIL, invoke override.
  State explicitly if invoked.

**Closing Verdict**: FAIL | CONDITIONAL | PASS
**Override invoked**: YES | NO
```

Emit Local Gate Ledger row here, immediately after "Override invoked":

```
**Local Gate Ledger:**
| Gate Verdict | Class | Finding Reference | Action |
|-------------|-------|-------------------|--------|
| [Closing Verdict] | [CLASS DERIVATION CONTRACT applied] | §3 / inertia-advocate / [5-word summary] | [synthesis action] |
```

If Override invoked = YES, add a second row:

```
| FAIL (override) | BLOCKED | §3 / inertia-advocate / override invoked | Override: DISPOSITION = BLOCKED |
```

This field is mandatory. Emit YES or NO regardless of whether override is exercised.

---

**§4 -- Master Action Register (Assembled from Local Gate Ledger Rows)**

Copy all Local Gate Ledger rows from §1.5, §2, and §3 into the master table verbatim. Do not
re-derive Gate Verdict or Class. Any row whose Class contradicts the Gate Verdict per the CLASS
DERIVATION CONTRACT is a structural defect traceable to its originating section.

```
## §4 -- Master Action Register
(Consolidated from Local Gate Ledger rows -- copy only, no re-derivation)

| # | Gate Verdict | Class | Finding Reference | Action |
|---|--------------|-------|-------------------|--------|
| [row from §1.5 local ledger] |
| [rows from §2 local ledgers] |
| [rows from §3 local ledger]  |
```

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

---

**Artifact to review:**

{{artifact_id}} artifact content:

{{artifact}}

---

## V-05 -- Combination: V-03 R4 Inline Ledger Base + Alternatives Table Bracket + Three-Contract Preamble (C-16 + C-17 + C-18 Path B)

**Variation axes**: V-03 R4's inline Local Gate Ledger mechanism (which passed C-18) is
preserved as the structural foundation; Alternatives Table adversarial bracket (C-09 + C-16)
is added, integrating the local ledger into the Bracket Opening and Bracket Closing sections;
all three pre-commitment contracts (DISPOSITION + CLASS DERIVATION + NULL HYPOTHESIS DERIVATION
RULE) are moved into the preamble (C-17); this is Path B to Perfect (140): start from C-18
proven and add C-16 + C-17

**Hypothesis**: V-05 R4 (Path A) starts from the full bracket stack and adds inline ledger.
This variant (Path B) starts from the inline ledger foundation and adds the bracket and
three-contract preamble. If both reach 140, the two construction paths are structurally
equivalent -- the three R4 criteria can be combined in either direction. If one path scores
differently, the ordering reveals which criteria are harder to retrofit onto an existing base.
The structural difference: V-03 R4's local ledger was designed for a non-bracket architecture
(each reviewer ends with a local row, master register copies). V-05 must integrate the local
ledger into bracket sections -- §1.5 (Bracket Opening) and §3 (Bracket Closing) must both
emit local rows, and the master register must copy them. The LOCAL GATE LEDGER PROTOCOL
from V-04 applies here identically; what changes is the construction order that led to it.

---

**Template inputs:**

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .craft/roles/signal/
```

Emit this acknowledgment block before §0.

```
## Review Parameters
Artifact:     {{artifact_id}}
Depth:        {{depth}}
Reviewer set: {{reviewer_set}}
```

---

You are running `org-review` on the artifact provided below.

Read all three contracts and the Local Gate Ledger Protocol before any reviewer section runs.

**DISPOSITION CONTRACT** (the synthesis evaluates this formula -- it does not produce a new one):

```
DISPOSITION FORMULA:
  if   any gate verdict = FAIL                    -->  DISPOSITION = BLOCKED
  elif Override invoked = YES  (see §3)           -->  DISPOSITION = BLOCKED
  elif any gate verdict = CONDITIONAL             -->  DISPOSITION = CONDITIONAL
  elif all gate verdicts = PASS                   -->  DISPOSITION = READY
  else                                            -->  DISPOSITION = CONDITIONAL
```

**CLASS DERIVATION CONTRACT** (action classes derive mechanically from gate verdicts;
do not re-assign at synthesis time):

```
FAIL gate        -->  BLOCKED
CONDITIONAL gate -->  CONDITIONAL
PASS + HIGH      -->  CONDITIONAL
PASS + LOW       -->  ADVISORY
```

**NULL HYPOTHESIS DERIVATION RULE** (Opening Verdict derives from the score differential;
do not assert it, derive it):

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

**LOCAL GATE LEDGER PROTOCOL** (applies in §2, §3, and §4):

Every reviewer section -- including Bracket Opening (§2), each domain reviewer (§3), and
Bracket Closing (§4) -- ends with a Local Gate Ledger row. The row captures Gate Verdict
+ Class at the moment of verdict emission. Class is assigned by applying the CLASS
DERIVATION CONTRACT at the point of origin. The master register (§5) copies these rows
verbatim. Do not re-derive Gate Verdict or Class at §5.

Local Gate Ledger row syntax:

```
**Local Gate Ledger:**
| Gate Verdict | Class | Finding Reference | Action |
|-------------|-------|-------------------|--------|
| [verdict]   | [class per CONTRACT] | [§] / [role] / [5-word summary] | [synthesis action] |
```

Add one row per FAIL or CONDITIONAL verdict. ADVISORY rows optional.

**Severity Semantics:**

| Severity | Commit-gate meaning |
|----------|---------------------|
| HIGH | Blocks commitment to proceed |
| MEDIUM | Conditions commitment; proceed only after remediation |
| LOW | Advisory; proceed regardless |

---

**§0 -- Scope Declaration**

```
IN SCOPE:
- Artifact: {{artifact_id}}
- Surfaces: [spec text, design constraints, named prior decisions]
OUT OF SCOPE:
- [surfaces not reviewed in this pass]
```

Any surface discovered mid-review not listed above is a scope gap. Flag it; do not absorb it.

---

**§1 -- Role Selection**

Read `.craft/roles/signal/`. No invented roles.
Depth: `{{depth}}`; Reviewer set: `{{reviewer_set}}`

1. If `{{reviewer_set}}` is not "auto": use those roles exactly. Inertia-advocate must be
   included for bracket positions (§2 and §4); if absent, add it and note the addition.
2. "auto" + "standard": min 2 domain roles + lifecycle role + inertia-advocate.
   One-sentence rationale per role.
3. "auto" + "deep": all roles in directory. State total count.

Inertia-advocate is reserved for §2 (Bracket Opening) and §4 (Bracket Closing).

```
Depth mode: {{depth}}
Reviewer set: {{reviewer_set}}
Reviewer manifest:
  - [role]: [archetype] -- [rationale | "explicit" | "deep run"]
    ...
  (inertia-advocate: reserved for bracket positions -- §2 and §4)
```

---

**§2 -- Bracket Opening: Challenger Pre-Domain Testimony**

This section runs before all domain reviewers. Domain reviewers have not seen it.

```
## §2 -- Bracket Opening -- inertia-advocate

**Status quo statement**: [what the team does today instead of building this -- one sentence]

**Alternatives Table (challenger frame):**

| Dimension            | Status Quo | This Artifact | Rationale                       |
|----------------------|-----------|---------------|---------------------------------|
| D1 Switching cost    | [1-5]     | [1-5]         | [one sentence per cell]         |
| D2 Coverage          | [1-5]     | [1-5]         | [one sentence]                  |
| D3 Adoption friction | [1-5]     | [1-5]         | [one sentence]                  |
| D4 Time-to-value     | [1-5]     | [1-5]         | [one sentence]                  |
| **TOTAL**            | [sum]     | [sum]         |                                 |

**Score differential**: [artifact total] - [status quo total] = [+/- n]
**NULL HYPOTHESIS DERIVATION RULE applied**: [which branch; state the derivation explicitly]

**Challenge to domain reviewers**: [one specific question that domain reviewers must answer
  to change any of these dimension scores -- this is the anchor for §3 re-reads]

**Findings**: [2-3 findings from challenger's lens.verify supporting the table scores]
**Severity**: HIGH | MEDIUM | LOW
**Verify Question**: [one from inertia-advocate's lens.verify]
**Opening Verdict**: FAIL | CONDITIONAL | PASS
```

Emit Local Gate Ledger row immediately after Opening Verdict:

```
**Local Gate Ledger:**
| Gate Verdict | Class | Finding Reference | Action |
|-------------|-------|-------------------|--------|
| [Opening Verdict] | [CLASS DERIVATION CONTRACT applied] | §2 / inertia-advocate / [5-word summary] | [synthesis action] |
```

Domain sections begin only after this Local Gate Ledger row is complete.

---

**§3 -- Domain Reviewer Sections**

Domain reviewers have access to the artifact only. They have not seen §2.

For each selected domain reviewer:

1. Load role file from `.craft/roles/signal/{role}.md`.
2. Apply `orientation.frame` to the artifact.
3. Re-score each dimension from this role's technical frame. Mark unchanged dimensions explicitly.
4. Emit the section, ending with a Local Gate Ledger row.

```
## §3 -- Domain Reviewer: [role] ([archetype])

**Domain re-read of alternatives table**
(Challenger's challenge: "[copy challenge text from §2]")

| Dimension            | Challenger Score | Revised Score | Justification or "unchanged" |
|----------------------|-----------------|---------------|-------------------------------|
| D1 Switching cost    | [challenger]    | [1-5]         | [sentence]                    |
| D2 Coverage          | [challenger]    | [1-5]         | [sentence]                    |
| D3 Adoption friction | [challenger]    | [1-5]         | [sentence]                    |
| D4 Time-to-value     | [challenger]    | [1-5]         | [sentence]                    |

**[This role's null hypothesis address]**: [does the technical approach make the status quo
  obsolete? One sentence. Must differ from challenger's framing.]

**Findings**: [2-4 findings from this role's lens.verify and expertise.depth; must not echo
  §2 framing or other domain reviewers]
**Severity**: HIGH | MEDIUM | LOW
**Recommendation**: [one concrete action]
**Verify Question**: [one from this role's lens.verify]
**Simplify**: [one from this role's lens.simplify]
**Gate Verdict**: FAIL | CONDITIONAL | PASS
```

Emit Local Gate Ledger row immediately after Gate Verdict:

```
**Local Gate Ledger:**
| Gate Verdict | Class | Finding Reference | Action |
|-------------|-------|-------------------|--------|
| [verdict] | [CLASS DERIVATION CONTRACT applied] | §3 / [role] / [5-word summary] | [synthesis action] |
```

One row minimum per FAIL or CONDITIONAL verdict.

---

**§4 -- Bracket Closing: Challenger Post-Domain Reassessment**

After all domain sections complete. The inertia-advocate now has access to all domain re-reads.

Answers: *Do the domain-adjusted dimension scores, taken in aggregate, constitute sufficient
evidence to defeat the null hypothesis stated in §2?*

Override authority: if domain re-reads inflate artifact scores without technical justification,
or if the adjusted verdict still indicates CONDITIONAL or FAIL, the Bracket Closing may
override. Override invoked = YES forces DISPOSITION = BLOCKED per DISPOSITION CONTRACT.

```
## §4 -- Bracket Closing -- inertia-advocate (post-domain reassessment)

**Domain re-read aggregation:**

| Reviewer | D1 | D2 | D3 | D4 | Null Hypothesis Address | Challenge Answered? |
|----------|----|----|----|----|-----------------------|---------------------|
| [role]   | [rev] | [rev] | [rev] | [rev] | [one sentence] | yes / partial / no |

**Revised Alternatives Table (challenger vs domain-aggregate):**

| Dimension            | Status Quo | Artifact (challenger) | Artifact (domain avg) | Accepted Score |
|----------------------|-----------|----------------------|----------------------|----------------|
| D1 Switching cost    | [SQ]      | [challenger]         | [domain avg]         | [final]        |
| D2 Coverage          | [SQ]      | [challenger]         | [domain avg]         | [final]        |
| D3 Adoption friction | [SQ]      | [challenger]         | [domain avg]         | [final]        |
| D4 Time-to-value     | [SQ]      | [challenger]         | [domain avg]         | [final]        |
| **TOTAL**            | [SQ sum]  |                      |                      | [final sum]    |

**Revised score differential**: [final artifact sum] - [SQ sum] = [+/- n]
**NULL HYPOTHESIS DERIVATION RULE re-applied**: [which branch; state if verdict changes from §2]

**Assessment**: [Does the domain-adjusted table change the verdict? What remains unaddressed?]

**Override authority**: [State explicitly if invoked and why, or state "not invoked".]

**Closing Verdict**: FAIL | CONDITIONAL | PASS
**Override invoked**: YES | NO
```

Emit Local Gate Ledger row immediately after "Override invoked":

```
**Local Gate Ledger:**
| Gate Verdict | Class | Finding Reference | Action |
|-------------|-------|-------------------|--------|
| [Closing Verdict] | [CLASS DERIVATION CONTRACT applied] | §4 / inertia-advocate / [5-word summary] | [synthesis action] |
```

If Override invoked = YES, also emit:

```
| FAIL (override) | BLOCKED | §4 / inertia-advocate / override invoked | Override: DISPOSITION = BLOCKED |
```

Both fields are mandatory. Emit YES or NO regardless of whether override is exercised.

---

**§5 -- Lifecycle Reviewer**

```
## §5 -- Lifecycle Reviewer: [role] ([archetype])

**Findings**: [2-3 findings: commitment readiness, decision sufficiency, program concerns]
**Severity**: HIGH | MEDIUM | LOW
**Recommendation**: [one concrete action]
**Verify Question**: [one from this role's lens.verify]
**Simplify**: [one from this role's lens.simplify]
**Gate Verdict (g_lifecycle)**: FAIL | CONDITIONAL | PASS
```

Emit Local Gate Ledger row:

```
**Local Gate Ledger:**
| Gate Verdict | Class | Finding Reference | Action |
|-------------|-------|-------------------|--------|
| [g_lifecycle] | [CLASS DERIVATION CONTRACT applied] | §5 / [role] / [5-word summary] | [synthesis action] |
```

---

**§6 -- Master Action Register (Assembled from Local Gate Ledger Rows)**

Copy all Local Gate Ledger rows from §2, §3, §4, and §5 into the master table verbatim. Do
not re-derive Gate Verdict or Class. Any row whose Class contradicts the Gate Verdict per the
CLASS DERIVATION CONTRACT is a structural defect traceable to its originating section.

```
## §6 -- Master Action Register
(Consolidated from Local Gate Ledger rows -- copy only, no re-derivation)

| # | Gate Verdict | Class | Finding Reference | Action |
|---|--------------|-------|-------------------|--------|
| [rows from §2 local ledger] |
| [rows from §3 local ledgers] |
| [rows from §4 local ledger]  |
| [rows from §5 local ledger]  |
```

---

**§7 -- Integrating Summary and Disposition**

Write 5-8 sentences:
- Name the highest-severity finding across all sections
- Name cross-role conflicts (incompatible recommendations from two domain reviewers)
- Name convergence areas
- Reference Opening Verdict (§2) and Closing Verdict (§4) explicitly -- include score differentials
- State whether Override invoked = YES or NO and the consequence
- Name which DISPOSITION CONTRACT branch applies

Apply the DISPOSITION CONTRACT from the preamble. State which branch.

```
## §7 -- Synthesis

[5-8 sentence synthesis]

FORMULA APPLIED: [state which branch of DISPOSITION CONTRACT applies and why]

DISPOSITION: READY | CONDITIONAL | BLOCKED
```

---

**Artifact to review:**

{{artifact_id}} artifact content:

{{artifact}}
