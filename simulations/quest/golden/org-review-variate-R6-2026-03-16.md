# org-review Variations — Round 6
Generated: 2026-03-16
Skill: org-review
Rubric: simulations/quest/rubrics/org-review-rubric-v6-2026-03-16.md

Prior rounds explored:
- R1: inertia-first sequence, strict table, null-hypothesis-universal, formal register, parallel blind
- R2: multi-dimension scorecard, four-gate, challenger-last rebuttal, inertia bracket + per-role NH, verdict cards
- R3: gate verdict propagation, pre-printed template, formula-first algebra, bracket + propagation, pre-printed + algebra + bracket
- R4: (ref in rubric changelog) bracket architecture with gate propagation, scored 96/109 under v5
- R5: (ref in rubric changelog) scope declared but not as pre-reviewer gate; scored 79/109 under v5

Round 6 strategy: two new v6 criteria dominate — C-22 (scope as structural pre-reviewer gate)
and C-23 (CH-ID action register). V-01 isolates C-22. V-02 isolates C-23. V-03 isolates the
DISPOSITION_CONTRACT preamble as the anchor for both scope and severity (C-19 + C-22 via contract
surface, phrasing-register axis). V-04 combines scope gate + adversarial bracket + CH-ID tracing
(C-22 + C-15 + C-18 + C-20 + C-17). V-05 is the maximum structural combination: pre-printed
template + DISPOSITION_CONTRACT + scope gate + bracket + CH-ID register, targeting all 23 criteria.

Rubric projects: R4-V05 bracket architecture scores ~96-99/115 under v6. V-04 here adds C-22 and
partial C-23 for ~103-108. V-05 adds full C-23 + pre-printed template for ~109-114.

---

## V-01 — Lifecycle Emphasis: Scope Declaration as Pre-Reviewer Gate

**Variation axis**: Lifecycle emphasis — a mandatory numbered Step 1 enumerates IN-SCOPE and
OUT-OF-SCOPE surfaces as a structural gate; role selection (Step 2) may not begin until Step 1
is complete; reviewer execution begins at Step 3 or later; any surface discovered after Step 1
requires a formal scope amendment

**Hypothesis**: C-22 requires scope to be a *structural precondition*, not a recommendation. R5
scored C-22 PARTIAL because scope was declared within the review body without a gating rule. Step 1
with an explicit gate condition — "role selection may not proceed until this step is complete" — is
the first mechanism that satisfies C-22 fully. The scope amendment protocol closes the mid-review
expansion gap: a reviewer discovering an unlisted surface mid-execution cannot silently treat it as
in-scope.

---

You are running `org-review` on the artifact provided below.

---

**STEP 1 — SCOPE DECLARATION**
*[GATE — role selection (Step 2) may not begin until this step is complete]*

Read the artifact and enumerate its scope explicitly before any reviewer is selected or any gate runs.

**IN-SCOPE** — surfaces this review will evaluate:

| # | Surface | Description |
|---|---------|-------------|
| 1 | [SURFACE_1] | [Brief description of what this surface covers] |
| 2 | [SURFACE_2] | [Brief description] |
| 3 | [SURFACE_3] | [Brief description] |
(Add rows as needed. Be exhaustive — nothing material may fall outside this list.)

**OUT-OF-SCOPE** — surfaces this review will not evaluate:

| # | Surface | Reason excluded |
|---|---------|-----------------|
| 1 | [SURFACE] | [REASON] |
(Write "None — full artifact surface in scope" if nothing is excluded.)

**Scope Amendment Protocol**: Any artifact surface discovered mid-review that is not listed
in IN-SCOPE above requires a formal amendment before that surface may be reviewed:
> `SCOPE AMENDMENT: [surface name] added to IN-SCOPE — [reason]`
A reviewer may not issue a finding on an unlisted surface without this amendment. Silent scope
expansion is a structural violation.

**Step 1 Complete** — role selection and reviewer gates proceed below.

---

**STEP 2 — ROLE MANIFEST**
*(Role selection proceeds because Step 1 is complete.)*

Read `.roles/signal/` to enumerate available reviewers.

- **Standard** (default): Assign one role per archetype slot. Select based on `expertise.relevance`
  to the IN-SCOPE surfaces declared in Step 1. State each assignment and one-sentence rationale.
  - CHALLENGER: inertia-advocate archetype — runs first; default stance is "don't build"
  - DOMAIN: technical/architecture archetype — evaluates implementation soundness
  - LIFECYCLE: PM/program archetype — evaluates commitment readiness
- **`--depth deep`**: Fill each slot with all matching roles. State total count and slot
  distribution.

All reviewers must come from `.roles/signal/`. Do not invent roles.

---

**STEP 3 — REVIEWER GATES**

Run each archetype slot in sequence: CHALLENGER → DOMAIN → LIFECYCLE. Each gate produces a
typed verdict (PASS / CONDITIONAL / FAIL) that propagates as a named input to the next gate. A
gate's verdict changes the task of downstream gates — it is not merely background context.

---

**Gate 1 — Null Hypothesis Gate (CHALLENGER)**

The challenger reviews in isolation. All findings must cite an in-scope surface from Step 1.

- **Null Hypothesis**: What the team does today instead of building this. One sentence.
- **Artifact's Response**: Does the artifact name and address the null hypothesis?
  yes / partial / no
- **Findings**: 2–3 findings from the challenger's `lens.verify`. Switching costs, workaround
  viability, adoption friction. Each finding names the in-scope surface it addresses.
- **Severity**: HIGH / MEDIUM / LOW.
  *Anchor: HIGH = artifact does not address null hypothesis; LOW = null hypothesis convincingly
  defeated.*
- **Verify Question**: One from the challenger's `lens.verify`.

**Gate 1 Verdict**: PASS / CONDITIONAL / FAIL

**Propagation rules — read before Gate 2 begins**:
- Gate 1 **PASS**: Domain reviewers evaluate technical merits. Null hypothesis treated as
  addressed. No additional null hypothesis response required.
- Gate 1 **CONDITIONAL**: Domain reviewers must each identify whether their findings address
  the specific null hypothesis gap named above. A domain PASS verdict is not valid unless that
  gap is addressed.
- Gate 1 **FAIL**: Domain reviewers evaluate the artifact but must each state whether their
  technical analysis would change the Gate 1 verdict. The Gate 1 FAIL persists unless all domain
  reviewers explicitly argue for upgrade to CONDITIONAL.

*State Gate 1 verdict at the top of Gate 2 as:* `Received Gate 1 Verdict: [value]`

---

**Gate 2 — Domain Gate (DOMAIN)**

For each domain reviewer:

---
**[Role name] — DOMAIN**

*Received Gate 1 Verdict: [copy from Gate 1]*
*(If Gate 1 = CONDITIONAL or FAIL: at least one finding must address the null hypothesis gap
stated in Gate 1. A PASS verdict without addressing that gap is non-compliant.)*

- **Scope coverage**: Which in-scope surfaces from Step 1 does this role examine?
  [List the 1–3 Step 1 surface labels this reviewer addresses.]
- **Findings**: 2–4 findings from this role's `lens.verify` and `expertise.depth`. Each finding
  names its source surface. At least one finding must engage Gate 1's null hypothesis gap if Gate 1
  is not PASS.
- **Severity**: HIGH / MEDIUM / LOW. Calibrate independently — do not copy Gate 1's level.
- **Recommendation**: One concrete action from this role's expertise frame.
- **Verify Question**: One from this role's `lens.verify`.
- **Simplify**: One from this role's `lens.simplify`.
- **Gate 2 Verdict**: PASS / CONDITIONAL / FAIL
  - CONDITIONAL: name the specific technical condition that must be met.
  - FAIL: name the specific gap that blocks commitment.

*(If Gate 1 = FAIL and this reviewer argues for upgrade: state "Gate 2 argues Gate 1 FAIL
upgrades to CONDITIONAL if [condition]. Gate 1 FAIL stands until all domain reviewers agree.")*

---

*(For `--depth deep`: repeat for each additional domain reviewer.)*

**Gate 2 Aggregate Verdict** = worst verdict among all domain reviewers
(FAIL > CONDITIONAL > PASS). State explicitly.

*State at the top of Gate 3 as:* `Received Gate 2 Aggregate Verdict: [value]`

---

**Gate 3 — Lifecycle Gate (LIFECYCLE)**

*Received Gate 1 Verdict: [value]*
*Received Gate 2 Aggregate Verdict: [value]*
*My task: assess whether accumulated evidence, given these specific gate verdicts, supports
a commitment decision.*

- **Scope coverage**: Which in-scope surfaces from Step 1 does this role examine?
- **Decision-Readiness Assessment**: Is evidence sufficient for commitment? Reference both received
  gate verdicts explicitly. Do not re-evaluate the null hypothesis independently — Gate 1 determined
  that.
- **Null Hypothesis Status**: Given Gate 1 and Gate 2, has the null hypothesis been addressed to
  commitment-readiness? yes / partial / no.
- **Findings**: 2–3 findings from this role's `lens.verify`. Commitment readiness, program
  concerns, decision sufficiency.
- **Severity**: HIGH / MEDIUM / LOW.
- **Recommendation**: One concrete action.
- **Verify Question**: One from this role's `lens.verify`.
- **Simplify**: One from this role's `lens.simplify`.
- **Gate 3 Verdict**: PASS / CONDITIONAL / FAIL

---

**STEP 4 — SYNTHESIS**

**Gate Summary Table**:

| Gate | Reviewer | Verdict | Scope Surfaces Covered | Primary Finding |
|------|----------|---------|------------------------|-----------------|
| Gate 1 — null hypothesis | [role] | [verdict] | [surfaces] | [one sentence] |
| Gate 2 — domain | [role] | [verdict] | [surfaces] | [one sentence] |
| Gate 3 — lifecycle | [role] | [verdict] | [surfaces] | [one sentence] |

**Scope Coverage Check**: Are all IN-SCOPE surfaces from Step 1 covered by at least one reviewer?
List any uncovered surfaces. If all covered: "None — full in-scope surface reviewed."

**Conflicts**: Two reviewers whose findings or recommendations are incompatible — name the roles
and the tension. If none: "None detected."

**Convergence**: Two or more reviewers naming the same concern independently. Name it and state
why it is the highest-confidence signal.

---

**STEP 5 — DISPOSITION**

Gate Vector: G1=[_] G2=[_] G3=[_]

Algebra:
- **BLOCKED** if any gate verdict = FAIL
- **CONDITIONAL** if no gate = FAIL and at least one gate = CONDITIONAL. State conditions in
  gate order: Gate 1 gap before Gate 2 gap before Gate 3 gap.
- **READY** if all gate verdicts = PASS

**Overall Disposition**: READY / CONDITIONAL / BLOCKED

**Primary driver**: One sentence naming the gate verdict and finding most responsible for this
disposition. Do not reason editorially — the disposition derives from the verdict vector.

**Conditions** *(complete only if CONDITIONAL)*: In gate order, what must be true before each
CONDITIONAL gate upgrades to PASS.

**Blocker** *(complete only if BLOCKED)*: The specific finding from the FAIL gate.

---

**Artifact to review:**

{{artifact}}

---

## V-02 — Output Format: CH-ID Action Item Register

**Variation axis**: Output format — the challenger assigns a unique CH-ID (CH-001, CH-002, ...)
to each challenge claim; every downstream reviewer section carries a mandatory pre-printed CH-ID
response table; the review closes with an action register keyed to CH-IDs with disposition class
(BLOCKED / CONDITIONAL / ADVISORY), owner role, and resolution criterion

**Hypothesis**: C-23 requires the action register to be the CH-ID-indexed synthesis artifact —
not just a conditions list derived from gate verdicts. Prior variations close with conditions
traced to findings by description, which can be paraphrased away. Assigning CH-IDs to challenge
claims and mandating response tables in every downstream section makes non-compliance
machine-detectable: a missing CH-ID field or an unmatched register row is a structural gap.
C-06 (action items) and C-20 (CH-IDs through sections) are satisfied as structural byproducts
of the format, not as separate instructions.

---

You are running `org-review` on the artifact provided below.

This review uses CH-IDs to trace challenge claims from the challenger gate through all downstream
reviewer sections into a final action register. Each challenge claim receives a unique identifier.
Every downstream reviewer carries a mandatory CH-ID response table. A PASS verdict is prohibited
without all active CH-IDs showing ADDRESSED or PARTIAL status with a named resolution path.

---

**Step 1 — Role Manifest**

Read `.roles/signal/` to enumerate available reviewers.

- **Standard** (default): Assign one role per slot: CHALLENGER, DOMAIN, LIFECYCLE.
  Select based on `expertise.relevance`. State each assignment and one-sentence rationale.
- **`--depth deep`**: Fill each slot with all matching roles. State total count.

All reviewers must come from `.roles/signal/`. Do not invent roles.

---

**Gate 1 — Challenger: Null Hypothesis + Challenge Claims**

- **Null Hypothesis**: What the team does today instead of building this. One sentence.
- **Artifact's Response**: Does the artifact address the null hypothesis? yes / partial / no.

**Challenge Claims** — assign a CH-ID to each claim:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [Specific claim from challenger's `lens.verify` — switching cost, workaround viability, or adoption friction. One sentence.] | HIGH / MEDIUM / LOW |
| CH-002 | [Second claim.] | HIGH / MEDIUM / LOW |
| CH-003 | [Optional third claim.] | HIGH / MEDIUM / LOW |

*Severity anchor per claim: HIGH = this claim, if unaddressed, blocks commitment. MEDIUM =
conditions commitment. LOW = advisory.*

- **Verify Question**: One from the challenger's `lens.verify`.

**Gate 1 Verdict**: PASS / CONDITIONAL / FAIL
*A CONDITIONAL verdict means at least one CH-ID claim was partially addressed. A FAIL means
at least one was not addressed at all.*

**Active Claims** *(carries forward to all downstream sections)*:
- CH-001: [one-phrase summary of claim]
- CH-002: [one-phrase summary]
- CH-003: [if present — one-phrase summary]

---

**Gate 2 — Domain: [Role Name]**

*Received Gate 1 Verdict: [copy from Gate 1]*

**CH-ID Response Table** *(mandatory — fill before any additional findings)*:

| CH-ID | Challenge Claim (copy) | This Role's Technical Response | Status |
|-------|----------------------|-------------------------------|--------|
| CH-001 | [copy full claim from Gate 1] | [This role's technical response to the claim — one to two sentences from this role's domain frame.] | ADDRESSED / PARTIAL / OPEN |
| CH-002 | [copy] | [response] | ADDRESSED / PARTIAL / OPEN |
| CH-003 | [copy if active] | [response] | ADDRESSED / PARTIAL / OPEN |

*Status guide: ADDRESSED = claim answered from this role's frame. PARTIAL = partially answered;
name the resolution path. OPEN = this reviewer cannot address this claim from their frame.*
*A PASS verdict requires no OPEN entries and no PARTIAL entries without resolution paths.*

**Additional Findings**: 2–4 findings from this role's `lens.verify` and `expertise.depth`
beyond the CH-ID responses above.

1. [Finding 1]
2. [Finding 2]
3. [Optional: Finding 3]
4. [Optional: Finding 4]

**Severity**: HIGH / MEDIUM / LOW.
*Anchor: HIGH = blocks commitment; MEDIUM = conditions commitment; LOW = advisory.*

**Recommendation**: One concrete action.

**Verify Question**: One from this role's `lens.verify`.

**Simplify**: One from this role's `lens.simplify`.

**Gate 2 Verdict**: PASS / CONDITIONAL / FAIL
*CONDITIONAL: name the specific technical condition. FAIL: name the specific gap.*

*(For `--depth deep`: repeat this section labeled DOMAIN-2, DOMAIN-3, etc. Each produces its
own CH-ID response table and Gate 2 Verdict. Gate 2 Aggregate = worst verdict among all rows.
State aggregate explicitly.)*

---

**Gate 3 — Lifecycle: [Role Name]**

*Received Gate 1 Verdict: [copy from Gate 1]*
*Received Gate 2 Verdict: [copy from Domain; aggregate if multiple]*

**CH-ID Response Table** *(mandatory)*:

| CH-ID | Challenge Claim (copy) | This Role's Commitment-Frame Response | Status |
|-------|----------------------|--------------------------------------|--------|
| CH-001 | [copy] | [Commitment-readiness response — does the artifact's decision case address this claim?] | ADDRESSED / PARTIAL / OPEN |
| CH-002 | [copy] | [response] | ADDRESSED / PARTIAL / OPEN |
| CH-003 | [copy if active] | [response] | ADDRESSED / PARTIAL / OPEN |

**Decision-Readiness Assessment**: Is evidence sufficient for commitment? Reference both received
verdicts explicitly. One paragraph.

**Null Hypothesis Status**: Given Gates 1 and 2, has the null hypothesis been defeated?
yes / partial / no — one sentence of justification.

**Additional Findings**: 2–3 findings from this role's `lens.verify`.

1. [Finding 1]
2. [Finding 2]

**Severity**: HIGH / MEDIUM / LOW.

**Recommendation**: One concrete action.

**Verify Question**: One from this role's `lens.verify`.

**Simplify**: One from this role's `lens.simplify`.

**Gate 3 Verdict**: PASS / CONDITIONAL / FAIL

---

**Synthesis**

**Gate Summary**:

| Gate | Reviewer | Verdict | Primary Finding |
|------|----------|---------|-----------------|
| Gate 1 — null hypothesis | [role] | [verdict] | [one sentence] |
| Gate 2 — domain | [role] | [verdict] | [one sentence] |
| Gate 3 — lifecycle | [role] | [verdict] | [one sentence] |

**CH-ID Resolution Status** *(pre-register summary)*:

| CH-ID | Gate 2 Status | Gate 3 Status | Overall Status |
|-------|--------------|--------------|----------------|
| CH-001 | ADDRESSED / PARTIAL / OPEN | ADDRESSED / PARTIAL / OPEN | CLOSED / OPEN |
| CH-002 | ... | ... | CLOSED / OPEN |
| CH-003 | ... | ... | CLOSED / OPEN |

*A CH-ID is CLOSED only if both Gate 2 and Gate 3 show ADDRESSED. Any PARTIAL or OPEN entry
means the CH-ID remains open and generates an action register row.*

**Conflicts**: Two reviewers with incompatible findings or CH-ID responses — name roles and
tension. If none: "None detected."

**Convergence**: Any CH-ID or concern named independently by two or more reviewers.

---

**Disposition**

Gate Vector: G1=[_] G2=[_] G3=[_]

- **BLOCKED** if any gate = FAIL
- **CONDITIONAL** if no gate = FAIL and at least one gate = CONDITIONAL
- **READY** if all gates = PASS

**Overall Disposition**: READY / CONDITIONAL / BLOCKED

**Primary driver**: One sentence.

---

**ACTION ITEM REGISTER**

*One row per open or partial CH-ID. Each row is keyed to a CH-ID from Gate 1 — if no CH-ID
source, mark as ADVISORY-OBS (advisory observation, not a challenge-sourced action).*

| CH-ID | Item Description | Disposition Class | Owner Role | Resolution Criterion |
|-------|-----------------|------------------|------------|---------------------|
| CH-001 | [What must be done — derived from the unaddressed or partially addressed claim] | BLOCKED / CONDITIONAL / ADVISORY | [Role name] | [Specific statement of what must be true before this item can be closed — one sentence] |
| CH-002 | [Item 2] | BLOCKED / CONDITIONAL / ADVISORY | [Role] | [Resolution criterion] |
| — | [Advisory observation not sourced from a CH-ID, if any] | ADVISORY-OBS | [Role] | [Criterion] |

*Disposition class semantics:*
- **BLOCKED**: Must be resolved before any commitment. An unresolved BLOCKED item = BLOCKED
  overall disposition.
- **CONDITIONAL**: Must be resolved before proceeding to next lifecycle phase. An unresolved
  CONDITIONAL item = CONDITIONAL overall disposition.
- **ADVISORY**: May be deferred. Commitment may proceed.

---

**Artifact to review:**

{{artifact}}

---

## V-03 — Phrasing Register: DISPOSITION_CONTRACT with Scope Enumeration

**Variation axis**: Phrasing register (formal/structural) — the review opens with a named,
immutable DISPOSITION_CONTRACT block that contains four locked sections: (1) scope enumeration
(IN-SCOPE / OUT-OF-SCOPE with amendment protocol), (2) severity semantics, (3) disposition
algebra, (4) contract cite requirement; the contract is filled once and is the structural
authority for all downstream reviewer sections

**Hypothesis**: C-19 requires severity semantics inside a named, locked contract — not free-form
preamble prose. C-22 requires scope as a pre-reviewer structural gate. A single
DISPOSITION_CONTRACT that contains both is more efficient than separate step-gating: the
contract becomes the immutable anchor for scope, severity, and algebra simultaneously. Any
reviewer section that contradicts a contract definition is a detectable deviation, not an
ambiguous instruction-following failure. The contract cite requirement (§4) extends C-21 by
making omission structurally visible rather than instructionally prohibited.

---

You are running `org-review` on the artifact provided below.

---

```
======================================================================
DISPOSITION_CONTRACT v1
[IMMUTABLE BLOCK — complete §1 scope fields below; do not alter §2-§4
definitions; reviewer sections may not execute until §1 is complete]
======================================================================

§1 — SCOPE ENUMERATION
[Fill this section. Reviewer execution is gated on completion of §1.]

IN-SCOPE — surfaces this review will evaluate:
  1. [SURFACE_1]
  2. [SURFACE_2]
  3. [SURFACE_3]
  (Add rows. Be exhaustive.)

OUT-OF-SCOPE — surfaces this review will not evaluate:
  1. [SURFACE — REASON_EXCLUDED]
  (Write "None" if nothing is excluded.)

Scope Amendment Protocol:
  A surface not listed in IN-SCOPE may not be reviewed without a formal
  amendment entry:
    SCOPE AMENDMENT: [surface] added to IN-SCOPE — [reason]
  Silent scope expansion is a contract violation. A reviewer section that
  produces findings on an unlisted surface without amendment is a
  structural gap detectable by audit.

§1 COMPLETE — role selection and reviewer gates proceed below.

§2 — SEVERITY SEMANTICS [IMMUTABLE]

  HIGH   = This finding blocks commitment. No commitment proceeds while
           HIGH findings are open.
  MEDIUM = This finding conditions commitment. Commitment proceeds only
           after named resolution.
  LOW    = This finding is advisory. Commitment may proceed without
           resolving it.

  These definitions apply universally to all reviewer sections. They
  may not be restated differently at any gate.

§3 — DISPOSITION ALGEBRA [IMMUTABLE]

  Let G = {g_null, g_domain, g_lifecycle}, each gi in {PASS, CONDITIONAL, FAIL}

  BLOCKED      <-- exists gi = FAIL
  CONDITIONAL  <-- (all gi != FAIL) AND (exists gi = CONDITIONAL)
  READY        <-- all gi = PASS

  Tiebreaker: g_null = FAIL yields BLOCKED regardless of other verdicts.
  The synthesis section evaluates this formula. It does not reason
  editorially from findings.

§4 — CONTRACT CITE REQUIREMENT [IMMUTABLE]

  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"
  A reviewer section that omits this line is an audit-trail gap. Verdicts
  from sections without a contract cite are not authoritative.
======================================================================
END DISPOSITION_CONTRACT v1
======================================================================
```

---

**Step 1 — Role Manifest**
*(§1 scope is complete. Role selection proceeds.)*

Read `.roles/signal/` to enumerate available reviewers.

- **Standard** (default): Assign one role per slot: CHALLENGER, DOMAIN, LIFECYCLE.
  Select based on `expertise.relevance` to the IN-SCOPE surfaces in §1. State assignment and
  one-sentence rationale.
- **`--depth deep`**: Fill each slot with all matching roles. State counts per slot.

All reviewers must come from `.roles/signal/`. Do not invent roles.

---

**Gate 1 — Null Hypothesis Gate (CHALLENGER)**

Contract: DISPOSITION_CONTRACT v1

- **Null Hypothesis**: What the team does today instead of building this. One sentence.
- **Artifact's Response**: yes / partial / no.
- **Findings**: 2–3 findings from the challenger's `lens.verify`. Switching costs, workaround
  viability, adoption friction. Each finding names an in-scope surface from the contract §1.
- **Severity**: HIGH / MEDIUM / LOW. *Per contract §2.*
- **Verify Question**: One from the challenger's `lens.verify`.
- **Null Hypothesis Stance**: Is the workaround actually worse than the proposed feature?
  yes / conditional / no — one sentence from the challenger's frame.
- **Gate 1 Verdict**: PASS / CONDITIONAL / FAIL
  *CONDITIONAL: name the specific gap. FAIL: name what the artifact failed to address.*

*Carry forward: state Gate 1 verdict at top of Gate 2.*

---

**Gate 2 — Domain Gate (DOMAIN)**

Contract: DISPOSITION_CONTRACT v1
Received Gate 1 Verdict: [copy from Gate 1]

*(If Gate 1 = CONDITIONAL or FAIL: at least one finding below must address the null hypothesis
gap stated in Gate 1. A PASS verdict without addressing that gap violates the contract.)*

- **Findings**: 2–4 findings from this role's `lens.verify` and `expertise.depth`. Each names
  an in-scope surface from the contract §1.
- **Severity**: HIGH / MEDIUM / LOW. *Per contract §2. Do not copy Gate 1 level.*
- **Recommendation**: One concrete action.
- **Verify Question**: One from this role's `lens.verify`.
- **Simplify**: One from this role's `lens.simplify`.
- **Null Hypothesis Stance**: From this role's technical frame, does the artifact make the
  workaround obsolete? yes / conditional / no — one sentence.
- **Gate 2 Verdict**: PASS / CONDITIONAL / FAIL
  *CONDITIONAL: name the specific technical condition. FAIL: name the gap.*

*(For `--depth deep`: repeat for each additional domain reviewer. Gate 2 Aggregate = worst
verdict. State aggregate explicitly.)*

*Carry forward: state Gate 2 Aggregate at top of Gate 3.*

---

**Gate 3 — Lifecycle Gate (LIFECYCLE)**

Contract: DISPOSITION_CONTRACT v1
Received Gate 1 Verdict: [copy from Gate 1]
Received Gate 2 Aggregate Verdict: [copy from Gate 2]

- **Decision-Readiness Assessment**: Is evidence sufficient for commitment? Reference both
  received verdicts explicitly.
- **Null Hypothesis Status**: Given Gates 1 and 2, has the null hypothesis been addressed?
  yes / partial / no.
- **Null Hypothesis Stance**: From this role's commitment frame, is the decision case strong
  enough to commit? yes / conditional / no — one sentence.
- **Findings**: 2–3 findings from this role's `lens.verify`.
- **Severity**: HIGH / MEDIUM / LOW. *Per contract §2.*
- **Recommendation**: One concrete action.
- **Verify Question**: One from this role's `lens.verify`.
- **Simplify**: One from this role's `lens.simplify`.
- **Gate 3 Verdict**: PASS / CONDITIONAL / FAIL

---

**Synthesis**

**Gate Summary**:

| Gate | Reviewer | Verdict | Contract Cite | Primary Finding |
|------|----------|---------|---------------|-----------------|
| Gate 1 | [role] | [verdict] | DISPOSITION_CONTRACT v1 | [one sentence] |
| Gate 2 | [role] | [verdict] | DISPOSITION_CONTRACT v1 | [one sentence] |
| Gate 3 | [role] | [verdict] | DISPOSITION_CONTRACT v1 | [one sentence] |

**Scope Coverage Check**: Are all IN-SCOPE surfaces from the contract §1 covered by at least
one reviewer? List any uncovered surfaces.

**Conflicts**: Two reviewers with incompatible findings or verdicts. Name roles and tension.
"None detected" if none.

**Convergence**: Two or more reviewers naming the same concern independently.

---

**Disposition**

*Evaluate the contract §3 formula against the gate vector. Do not reason editorially.*

Gate vector: g_null=[_] g_domain=[_] g_lifecycle=[_]

Apply formula from DISPOSITION_CONTRACT v1 §3:

```
BLOCKED      <-- exists gi = FAIL
CONDITIONAL  <-- (all gi != FAIL) AND (exists gi = CONDITIONAL)
READY        <-- all gi = PASS
```

**Overall Disposition**: READY / CONDITIONAL / BLOCKED

**Primary driver**: One sentence stating the gate and formula result. Do not reason editorially.

**Conditions** *(if CONDITIONAL)*: In gate order, what must be resolved before each CONDITIONAL
gate upgrades to PASS.

**Blocker** *(if BLOCKED)*: The specific finding from the FAIL gate, cited against the in-scope
surface that generated it.

---

**Artifact to review:**

{{artifact}}

---

## V-04 — Combination: Scope Gate + Adversarial Bracket + CH-ID Tracing

**Variation axes**: Lifecycle emphasis (scope gate — Step 1 pre-reviewer structural gate, C-22)
+ Role sequence (adversarial bracket — challenger runs first to open and last to close, C-15 +
C-18) + Output format (CH-ID assignment on challenge claims + mandatory per-reviewer CH-ID
response tables, C-20 + C-17)

**Hypothesis**: The three mechanisms close three different failure modes independently but
reinforce each other. The scope gate prevents mid-review surface expansion before any CH-ID is
assigned — reviewers cannot respond to challenge claims about out-of-scope surfaces. The bracket
ensures null hypothesis is structurally first and last — the closing challenger evaluates whether
domain and lifecycle CH-ID responses actually answered the claims, not just acknowledged them.
CH-ID tracing makes the carry-forward machine-detectable: a downstream reviewer missing a CH-ID
row is a structural gap, not a paraphrase. The bracket closing override (GClose = FAIL overrides
all prior verdicts) is explicitly stated, preventing domain PASses from washing out a HOLDS
verdict. Projected to satisfy C-13, C-15, C-16 (algebra pre-stated), C-17, C-18, C-20, C-22,
and partial C-23 (register keyed to CH-IDs but without full resolution-criterion column — V-05
completes that).

---

You are running `org-review` on the artifact provided below.

This review uses three interlocking mechanisms: (1) a structural scope gate before any reviewer
runs; (2) an adversarial bracket — the challenger runs first to declare challenge claims and last
to assess whether the accumulated record defeated them; (3) CH-ID tracing — each challenge claim
carries a stable identifier through every downstream reviewer section.

**Disposition formula** *(pre-stated; evaluated at DISPOSITION section — do not alter)*:

```
G = {GOpen, G_domain, G_lifecycle, GClose}
BLOCKED      <-- GClose = FAIL   [challenger override: null hypothesis holds]
              OR  exists Gi = FAIL (any gate)
CONDITIONAL  <-- no Gi = FAIL AND exists Gi = CONDITIONAL
READY        <-- all Gi = PASS
```

---

**STEP 1 — SCOPE DECLARATION**
*[GATE — reviewer execution may not begin until this step is complete]*

**IN-SCOPE**:

| # | Surface |
|---|---------|
| 1 | [SURFACE_1] |
| 2 | [SURFACE_2] |
| 3 | [SURFACE_3] |

**OUT-OF-SCOPE** (and reason excluded):

| # | Surface | Reason |
|---|---------|--------|
| 1 | [SURFACE] | [REASON] |

**Scope Amendment Protocol**: Any surface discovered mid-review that is not listed above
requires `SCOPE AMENDMENT: [surface] — [reason]` before that surface may be reviewed.

**Step 1 Complete** — role selection and reviewer gates proceed.

---

**STEP 2 — ROLE MANIFEST**

Read `.roles/signal/` to enumerate available reviewers.

- **Standard**: Assign one role per slot: CHALLENGER (bracket open + close — fixed positions),
  DOMAIN (technical), LIFECYCLE (PM/program). State assignments and rationale.
- **`--depth deep`**: Multiple domain reviewers allowed. Challenger bracket positions remain
  fixed at opening and closing regardless of depth. State total count per slot.

All reviewers must come from `.roles/signal/`. Do not invent roles.

---

**STEP 3 — BRACKET OPENING (CHALLENGER)**

The challenger runs first. This is a declaration pass.

- **Null Hypothesis**: What the team does today instead of building this. One sentence.
- **Null Hypothesis Strength**: HIGH / MEDIUM / LOW — how strong is the case for doing nothing?

**Challenge Claims** *(assign CH-IDs; these carry forward to every downstream section)*:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [Specific claim from challenger's `lens.verify` — switching cost, workaround viability, or adoption friction. One sentence.] | HIGH / MEDIUM / LOW |
| CH-002 | [Second claim.] | HIGH / MEDIUM / LOW |
| CH-003 | [Optional third claim.] | HIGH / MEDIUM / LOW |

*Every domain and lifecycle reviewer carries a mandatory CH-ID response table for these IDs.
A PASS verdict at any gate is prohibited without all active CH-IDs showing ADDRESSED or PARTIAL
with a named resolution path.*

- **Verify Question**: One from the challenger's `lens.verify`.
- **Simplify**: One from the challenger's `lens.simplify`.

**GOpen Verdict**: PASS / CONDITIONAL / FAIL
*PASS = artifact addresses the null hypothesis. CONDITIONAL = partially. FAIL = not addressed.*

**GOpen carry-forward**: All downstream sections open with:
`Received GOpen: [value] | Active CH-IDs: CH-001, CH-002, [CH-003]`

---

**STEP 4 — DOMAIN GATE (DOMAIN)**

For each domain reviewer:

---
**[Role name] — DOMAIN**

*Received GOpen: [copy from Bracket Opening]*
*Active CH-IDs: CH-001, CH-002, [CH-003]*

**CH-ID Response Table** *(mandatory — fill before proceeding to additional findings)*:

| CH-ID | Challenge Claim (copy) | This Role's Technical Response | Status |
|-------|----------------------|-------------------------------|--------|
| CH-001 | [copy full claim from BRACKET OPENING] | [Technical response from this role's domain frame — does the artifact's approach address this claim?] | ADDRESSED / PARTIAL / OPEN |
| CH-002 | [copy] | [response] | ADDRESSED / PARTIAL / OPEN |
| CH-003 | [copy if active] | [response] | ADDRESSED / PARTIAL / OPEN |

*PARTIAL requires a named resolution path. OPEN = this role cannot address this claim from their
frame (not a FAIL, but noted for the bracket closing to assess).*

**Additional Findings**: 2–3 findings from this role's `lens.verify` and `expertise.depth` beyond
the CH-ID responses.

**Severity**: HIGH / MEDIUM / LOW. Calibrate independently.

**Recommendation**: One concrete action.

**Verify Question**: One from this role's `lens.verify`.

**Simplify**: One from this role's `lens.simplify`.

**G_domain Verdict**: PASS / CONDITIONAL / FAIL
*(CONDITIONAL: name condition. FAIL: name gap.)*

---

*(For `--depth deep`: repeat for each additional domain reviewer. G_domain Aggregate = worst
verdict among all domain rows. State aggregate explicitly.)*

**G_domain Aggregate**: [worst verdict]. *Carries to LIFECYCLE.*

---

**STEP 5 — LIFECYCLE GATE (LIFECYCLE)**

*Received GOpen: [copy from Bracket Opening]*
*Received G_domain Aggregate: [copy G_domain aggregate]*

**CH-ID Response Table** *(mandatory)*:

| CH-ID | Challenge Claim (copy) | This Role's Commitment-Frame Response | Status |
|-------|----------------------|--------------------------------------|--------|
| CH-001 | [copy] | [Commitment-readiness response — does the accumulated decision case address this claim?] | ADDRESSED / PARTIAL / OPEN |
| CH-002 | [copy] | [response] | ADDRESSED / PARTIAL / OPEN |
| CH-003 | [copy if active] | [response] | ADDRESSED / PARTIAL / OPEN |

**Decision-Readiness Assessment**: Is evidence sufficient for commitment? Reference both received
verdicts explicitly. One paragraph.

**Null Hypothesis Status**: Given GOpen and G_domain, has the null hypothesis been defeated?
yes / partial / no.

**Additional Findings**: 2–3 findings from this role's `lens.verify`.

**Severity**: HIGH / MEDIUM / LOW.

**Recommendation**: One concrete action.

**Verify Question**: One from this role's `lens.verify`.

**Simplify**: One from this role's `lens.simplify`.

**G_lifecycle Verdict**: PASS / CONDITIONAL / FAIL
*Carries to BRACKET CLOSING.*

---

**STEP 6 — BRACKET CLOSING (CHALLENGER)**

*Full record received: scope declaration, all CH-ID response tables, all gate verdicts.*

**CH-ID Final Assessment**:

| CH-ID | G_domain Status | G_lifecycle Status | Final Status | Notes |
|-------|----------------|-------------------|--------------|-------|
| CH-001 | [copy from DOMAIN] | [copy from LIFECYCLE] | DEFEATED / PARTIAL / HOLDS | [One sentence: what gap remains, if any] |
| CH-002 | [copy] | [copy] | DEFEATED / PARTIAL / HOLDS | [note] |
| CH-003 | [copy if active] | [copy] | DEFEATED / PARTIAL / HOLDS | [note] |

*DEFEATED = claim fully answered across both gates. PARTIAL = partially answered; gap named.
HOLDS = claim survived domain and lifecycle review unanswered.*

**Remaining Gaps**: Any CH-ID showing PARTIAL or HOLDS. If none: "None — all CH-IDs defeated."

**GClose Verdict**: PASS / CONDITIONAL / FAIL
- PASS (= DEFEATED): All CH-IDs DEFEATED — accumulated record defeats the null hypothesis.
- CONDITIONAL (= PARTIAL): Some CH-IDs PARTIAL — material gaps remain; name them.
- FAIL (= HOLDS): At least one CH-ID HOLDS — null hypothesis survives the review.

**GClose Override Authority**: GClose = FAIL overrides all prior gate verdicts. A HOLDS verdict
from the challenger is not overturned by G_domain or G_lifecycle PASses. This override authority
is explicit and structural — it is not subject to editorial revision at the Disposition step.

**GClose Rationale**: 2–3 sentences.

---

**STEP 7 — SYNTHESIS AND DISPOSITION**

**Gate Vector Table**:

| Gate | Reviewer | Verdict | Primary Signal |
|------|----------|---------|----------------|
| GOpen — bracket opening | [CHALLENGER_ROLE] | [verdict] | [one sentence] |
| G_domain — domain | [DOMAIN_ROLE] | [verdict] | [one sentence] |
| G_lifecycle — lifecycle | [LIFECYCLE_ROLE] | [verdict] | [one sentence] |
| GClose — bracket closing | [CHALLENGER_ROLE] | [verdict] | [one sentence] |

**Scope Coverage Check**: Any in-scope surface from Step 1 not reviewed by any gate.

**Conflicts**: Two reviewers with incompatible CH-ID responses or incompatible verdicts.
Name roles and tension.

**Convergence**: Any CH-ID that multiple reviewers flagged independently.

---

**Evaluate the pre-stated formula** *(do not reason editorially — apply the formula)*:

Gate vector: GOpen=[_] G_domain=[_] G_lifecycle=[_] GClose=[_]

```
GClose = FAIL? --> BLOCKED (challenger override: null hypothesis holds)
Any other Gi = FAIL? --> BLOCKED
No FAIL, any CONDITIONAL? --> CONDITIONAL
All PASS? --> READY
```

**Overall Disposition**: READY / CONDITIONAL / BLOCKED

**Primary driver**: One sentence naming the gate verdict most responsible. Do not reason
from findings — the formula completed the derivation.

**Conditions** *(if CONDITIONAL)*: In gate order (GOpen before G_domain before G_lifecycle
before GClose), what must be resolved before each CONDITIONAL gate upgrades to PASS.

**Blocker** *(if BLOCKED)*: The specific gap from the FAIL gate. If GClose = FAIL, lead with:
"Challenger final verdict HOLDS — [GClose Rationale summary]."

---

**ACTION ITEM REGISTER**

*Keyed to CH-IDs from the Bracket Opening. One row per PARTIAL or HOLDS CH-ID. Items not
sourced from a CH-ID are marked ADVISORY-OBS.*

| CH-ID | Item Description | Disposition Class | Owner Role | Resolution Criterion |
|-------|-----------------|------------------|------------|---------------------|
| CH-001 | [What must be done — derived from the PARTIAL or HOLDS status] | BLOCKED / CONDITIONAL / ADVISORY | [Role name] | [What must be true before this item can be closed — one sentence] |
| CH-002 | [Item] | BLOCKED / CONDITIONAL / ADVISORY | [Role] | [Criterion] |
| — | [Advisory observation not sourced from a CH-ID, if any] | ADVISORY-OBS | [Role] | [Criterion] |

---

**Artifact to review:**

{{artifact}}

---

## V-05 — Full Combination: Pre-printed Template + DISPOSITION_CONTRACT + Scope Gate + Bracket + CH-ID Register

**Variation axes**: Output format (pre-printed fill-the-brackets template, C-01/C-03/C-04
structural guarantee) + Phrasing register (DISPOSITION_CONTRACT with scope, severity, and algebra
locked, C-19 + C-22) + Role sequence (adversarial bracket, C-15 + C-18) + Output format (CH-ID
response tables + full action register, C-20 + C-17 + C-23) + Pre-run algebra commitment (C-16)
+ Contract cite per section (C-21)

**Hypothesis**: Each mechanism targets a different failure class.
- Pre-printed template: model cannot drop or reformat sections it did not generate (structural
  guarantee for C-01, C-03, C-04).
- DISPOSITION_CONTRACT: scope and severity definitions are contract-bound before any reviewer
  runs — any deviation is auditable at the section level, not only at synthesis (C-19, C-22).
- Adversarial bracket with override authority: null hypothesis is structurally first and last;
  a HOLDS verdict overrides all domain PASses without requiring editorial judgment (C-15, C-18).
- CH-ID tables + action register: challenge claims are traceable by stable identifier through
  sections and into the synthesis artifact; non-compliance is machine-detectable (C-20, C-17, C-23).
- Pre-run algebra: formula committed before Gate 1 runs; synthesis evaluates the formula, does
  not generate one after reading verdicts (C-16).
- Contract cite per section: each section's deviation from the contract is visible at that gate,
  not only at summary time (C-21).

Combined, these mechanisms project V-05 at ~109–114/115 under v6, targeting full credit on all
23 criteria.

---

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any pre-printed
heading, label, field, formula, or structural element. Do not add sections between pre-printed
headers. If a field cannot be filled, write `[N/A — reason]`.

---

```
======================================================================
DISPOSITION_CONTRACT v1
[IMMUTABLE BLOCK — complete §1 scope fields; do not alter §2-§5;
reviewer sections may not execute until §1 COMPLETE marker is reached]
======================================================================

§1 — SCOPE ENUMERATION
[Fill this section before proceeding. This is the pre-reviewer gate.]

IN-SCOPE — surfaces this review will evaluate:
  1. [SURFACE_1]
  2. [SURFACE_2]
  3. [SURFACE_3]
  (Add rows. Be exhaustive.)

OUT-OF-SCOPE — surfaces this review will not evaluate:
  1. [SURFACE — REASON_EXCLUDED]
  (Write "None" if nothing is excluded.)

Scope Amendment Protocol:
  SCOPE AMENDMENT: [surface] added to IN-SCOPE — [reason]
  Silent scope expansion violates this contract.

§1 COMPLETE — role selection and reviewer gates proceed below.

§2 — SEVERITY SEMANTICS [IMMUTABLE]
  HIGH   = Blocks commitment. No commitment proceeds with open HIGH findings.
  MEDIUM = Conditions commitment. Proceeds only after named resolution.
  LOW    = Advisory. Commitment may proceed.
  These definitions apply universally. They may not be restated at any gate.

§3 — DISPOSITION ALGEBRA [IMMUTABLE — evaluated at DISPOSITION section]
  G = {GOpen, G_domain_agg, G_lifecycle, GClose}
  BLOCKED      <-- GClose = FAIL  [override: null hypothesis holds]
                OR  exists Gi = FAIL
  CONDITIONAL  <-- no Gi = FAIL  AND  exists Gi = CONDITIONAL
  READY        <-- all Gi = PASS

§4 — CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"
  A missing cite is an audit-trail gap.

§5 — CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Each challenge claim in BRACKET OPENING receives a CH-ID (CH-001, ...).
  Every downstream section carries a mandatory CH-ID response table.
  A PASS verdict is prohibited if any CH-ID row shows OPEN status.
======================================================================
END DISPOSITION_CONTRACT v1
======================================================================
```

---

## ROLE MANIFEST

Read `.roles/signal/`. Assign each slot.

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (bracket open + close — fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

*(For `--depth deep`: add DOMAIN-2, DOMAIN-3, etc. CHALLENGER positions remain fixed.
State total count.)*

---

## BRACKET OPENING — CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [What the team does today instead of building this — one sentence.]

**Null hypothesis strength**: [HIGH / MEDIUM / LOW — how strong is the case for doing nothing?]

**Challenge claims** *(assign CH-IDs; carry to every downstream section per contract §5)*:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1 — switching cost, workaround viability, or adoption friction. One sentence.] | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2] | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 — optional] | [HIGH / MEDIUM / LOW] |

**Verify Question**: [One from challenger's `lens.verify`.]

**Simplify**: [One from challenger's `lens.simplify`.]

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]

*GOpen and all CH-IDs above carry forward to every downstream section.*

---

## DOMAIN — [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [PASS / CONDITIONAL / FAIL — copy from BRACKET OPENING]

**CH-ID Response Table** *(mandatory per contract §5 — PASS verdict prohibited if any row = OPEN)*:

| CH-ID | Challenge Claim (copy) | This Role's Technical Response | Status |
|-------|----------------------|-------------------------------|--------|
| CH-001 | [copy full claim from BRACKET OPENING] | [RESPONSE_1] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

*(PARTIAL requires a named resolution path. OPEN = claim not addressable from this role's frame.)*

**Additional Findings**:
1. [FINDING_1 — from this role's `lens.verify` and `expertise.depth`. Names an in-scope surface.]
2. [FINDING_2]
3. [FINDING_3 — optional]
4. [FINDING_4 — optional]

**Severity**: [HIGH / MEDIUM / LOW]
*Per contract §2. Do not copy GOpen severity.*

**Recommendation**: [One concrete action.]

**Verify Question**: [One from this role's `lens.verify`.]

**Simplify**: [One from this role's `lens.simplify`.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence. If CONDITIONAL: name condition. If FAIL: name gap.]

*(For `--depth deep`: repeat labeled DOMAIN-2, DOMAIN-3. G_domain Aggregate = worst verdict
among all DOMAIN rows. State aggregate explicitly below.)*

**G_domain Aggregate**: [PASS / CONDITIONAL / FAIL — worst among all DOMAIN rows]

---

## LIFECYCLE — [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [PASS / CONDITIONAL / FAIL — copy from BRACKET OPENING]
Received G_domain Aggregate: [PASS / CONDITIONAL / FAIL — copy from DOMAIN aggregate]

**CH-ID Response Table** *(mandatory per contract §5)*:

| CH-ID | Challenge Claim (copy) | This Role's Commitment-Frame Response | Status |
|-------|----------------------|--------------------------------------|--------|
| CH-001 | [copy] | [RESPONSE_1] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [Is evidence sufficient for commitment given both received
verdicts? One paragraph referencing GOpen and G_domain Aggregate explicitly.]

**Null hypothesis status**: [Given GOpen and G_domain, has the null hypothesis been defeated?
yes / partial / no — one sentence of justification.]

**Additional Findings**:
1. [FINDING_1 — from this role's `lens.verify`. Commitment, program, or decision concerns.]
2. [FINDING_2]

**Severity**: [HIGH / MEDIUM / LOW]
*Per contract §2.*

**Recommendation**: [One concrete action.]

**Verify Question**: [One from this role's `lens.verify`.]

**Simplify**: [One from this role's `lens.simplify`.]

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
**G_lifecycle Reason**: [One sentence.]

---

## BRACKET CLOSING — CHALLENGER

Contract: DISPOSITION_CONTRACT v1
*Full record received: scope declaration, all CH-ID tables, all gate verdicts.*

**CH-ID Final Assessment**:

| CH-ID | G_domain Status | G_lifecycle Status | Final Status | Notes |
|-------|----------------|-------------------|--------------|-------|
| CH-001 | [copy from DOMAIN] | [copy from LIFECYCLE] | [DEFEATED / PARTIAL / HOLDS] | [ONE_SENTENCE_NOTE] |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |
| CH-003 | [copy if active] | [copy] | [DEFEATED / PARTIAL / HOLDS] | [note] |

**Remaining gaps**: [What was not fully addressed. If none: "None — all CH-IDs DEFEATED."]

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
- PASS (= DEFEATED): All CH-IDs DEFEATED — accumulated record defeats the null hypothesis.
- CONDITIONAL (= PARTIAL): Some CH-IDs PARTIAL — material gaps remain; name them.
- FAIL (= HOLDS): At least one CH-ID HOLDS — null hypothesis survives.

**GClose override authority**: GClose = FAIL overrides all prior gate verdicts. A HOLDS verdict
from the challenger is not overturned by G_domain or G_lifecycle PASses. This override is
pre-stated in the contract §3 and is not subject to editorial revision at the Disposition step.

**GClose Rationale**: [2–3 sentences explaining the verdict.]

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract Cite |
|------|----------|---------|---------------|
| GOpen — bracket opening | [CHALLENGER_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_domain — domain aggregate | [DOMAIN_ROLE(S)] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_lifecycle — lifecycle | [LIFECYCLE_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| GClose — bracket closing | [CHALLENGER_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [Two reviewers with incompatible CH-ID responses or incompatible findings —
name roles and tension. If none: "None detected."]

**Convergence**: [Any CH-ID or concern named independently by two or more reviewers — name it
and state why it is the highest-confidence signal in this review.]

**Scope coverage**: [Any in-scope surface from contract §1 not covered by any reviewer — list
it. If all covered: "None — full in-scope surface reviewed."]

---

## DISPOSITION

**Gate vector** *(fill from GATE VECTOR TABLE above)*:
- GOpen = [copy]
- G_domain_agg = [copy]
- G_lifecycle = [copy]
- GClose = [copy]

**Apply contract §3 formula** *(do not alter the formula; do not reason editorially — evaluate
the gate vector against the pre-stated formula)*:

```
G = {GOpen=[_], G_domain_agg=[_], G_lifecycle=[_], GClose=[_]}
GClose = FAIL? --> BLOCKED  (challenger override: null hypothesis holds)
Any other Gi = FAIL? --> BLOCKED
No FAIL, any CONDITIONAL? --> CONDITIONAL
All PASS? --> READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED — result of evaluating the formula above]

**Primary driver**: [The gate verdict most responsible for this disposition — one sentence.
Do not reason from findings — the formula completed the derivation.]

**Conditions** *(complete only if CONDITIONAL)*:
1. [Condition from first CONDITIONAL gate — what must be resolved to upgrade to PASS. Gate order:
   GOpen before G_domain before G_lifecycle before GClose.]
2. [Additional conditions if present.]

**Blocker** *(complete only if BLOCKED)*: [Specific finding from the FAIL gate. If GClose = FAIL,
lead with: "Challenger final verdict HOLDS — [GClose Rationale summary]."]

---

## ACTION ITEM REGISTER

*One row per PARTIAL or HOLDS CH-ID from BRACKET CLOSING. Items not sourced from a CH-ID are
marked ADVISORY-OBS. This register is the CH-ID-indexed synthesis artifact per contract §5.*

| CH-ID | Item Description | Disposition Class | Owner Role | Resolution Criterion |
|-------|-----------------|------------------|------------|---------------------|
| CH-001 | [What must be done — derived from the PARTIAL or HOLDS status of this claim] | [BLOCKED / CONDITIONAL / ADVISORY] | [ROLE_NAME] | [Specific statement of what must be true before this item can be closed — one sentence] |
| CH-002 | [Item 2] | [BLOCKED / CONDITIONAL / ADVISORY] | [ROLE_NAME] | [Resolution criterion] |
| — | [Advisory observation not sourced from a CH-ID, if any] | ADVISORY-OBS | [ROLE_NAME] | [Criterion] |

*Disposition class per contract §2:*
- **BLOCKED**: Must be resolved before any commitment. An open BLOCKED item = BLOCKED disposition.
- **CONDITIONAL**: Must be resolved before proceeding to next lifecycle phase.
- **ADVISORY**: May be deferred. Commitment may proceed.

*Every row in this register traces to a CH-ID from BRACKET OPENING → reviewer CH-ID tables →
BRACKET CLOSING final status. The full chain is navigable in either direction without
cross-referencing reviewer sections separately.*

---

**Artifact to review:**

{{artifact}}
