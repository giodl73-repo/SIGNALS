# org-review Variations -- Round 3 (v3 rubric, 2026-03-16)

Generated: 2026-03-16
Skill: org-review
Rubric: simulations/quest/rubrics/org-review-rubric-v3-2026-03-16.md

## Prior Round Summary

- R1 (v1 rubric): V-05 best. C-11 (verdict-preview tables, E-1) and C-12 (count constraint, E-2) identified.
- R2 (v2 rubric): V-05=110 under v2. E-3 (LIFECYCLE-before-DOMAIN, C-14) and E-4 (NULL HYPOTHESIS REGISTER, C-13) confirmed. v3 rubric adds both as aspirational criteria; max composite raised to 120.
- R2 retroactive (v3 rubric): V-05 R2 carries C-11 + C-12 + C-13 + C-14. Scores 120/120 under v3 ceiling from base inheritance.

## Round 3 Strategy

All R3 variants inherit V-05 R2 as non-negotiable base. Round 3 is a frontier-extension round.

V-05 R2 satisfies all 14 criteria (max 120 under v3). Round 3 explores axes that could surface C-15+ patterns for a future v4 rubric.

Three new single-axis hypotheses, then two combinations:

| Variation | Axis | New Hypothesis |
|-----------|------|----------------|
| V-01 | SCOPE SURFACE REGISTER | Same register+prohibition+downstream-reference pattern as C-13 applied to §1 scope surfaces; converts C-06 (scope specificity) from execution-dependent to template-determined |
| V-02 | FINDING SURFACE LINKAGE TABLE | Structured findings table (Finding / Surface / Role Lens / Severity) converts C-10 (role-grounded findings) from execution-dependent to template-determined |
| V-03 | PER-FINDING SEVERITY AGGREGATION | Per-finding severity tag + mechanical worst-case formula for section severity eliminates editorial section-level severity; creates auditable chain: finding -> severity -> formula -> gate verdict |
| V-04 | V-01 + V-02 | SCOPE REGISTER + FINDING TABLE combined |
| V-05 | Full integration | V-01 + V-02 + V-03 |

Single-axis: V-01, V-02, V-03. Combinations: V-04, V-05.

---

## V-01 -- Single Axis: SCOPE SURFACE REGISTER

**Variation axis**: Pre-section register for §1 scope surfaces.

**Hypothesis**: §1 IN-SCOPE currently uses generic placeholders ([SURFACE_1], [SURFACE_2]) that accept any description including "all sections" or "the full document". A SCOPE SURFACE REGISTER -- requiring named, concrete surfaces with explicit prohibition of generic substitutes -- applies the same C-13 register+prohibition+downstream-reference pattern to scope surfaces. §1 IN-SCOPE field references the register by S-ID copy rather than free-form text. C-06 (scope enumeration artifact-specific) becomes template-determined: if the register contains generic values, the violation is visible at register-fill time, not at finding-evaluation time. Expected excellence pattern: E-1 (new, v4 candidate C-15) -- generalizes C-13 register mechanism from one-criterion (null hypothesis) to a second criterion (scope surfaces).

**Changes from V-05 R2**:
- Add SCOPE SURFACE REGISTER section before DISPOSITION_CONTRACT (the consuming section is §1 IN-SCOPE)
- §1 IN-SCOPE template updated to reference register by S-ID copy with explicit instruction prohibiting generic substitutes
- Additional Findings in DOMAIN and LIFECYCLE add surface S-ID citation guidance

---

```
depth: standard
confidence: standard
for: {value}
iterations: 1

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any pre-printed
heading, label, field, formula, or structural element. Do not add sections between pre-printed
headers. If a field cannot be filled, write `[N/A -- reason]`.

---

## SCOPE SURFACE REGISTER

*Complete this register before §1 IN-SCOPE. Name each concrete surface the artifact exposes for
review. Generic descriptions ("all sections", "the full document", "all fields", "entire spec",
"all content") are not acceptable -- they prevent surface-specific finding linkage and violate the
audit trail. Each surface must be nameable as a specific section heading, interface contract,
behavioral claim, schema component, or named protocol.*

| S-ID  | Surface Name                                                              | Why In Scope                                                      | Primary Lens          |
|-------|---------------------------------------------------------------------------|-------------------------------------------------------------------|-----------------------|
| S-001 | [Specific section, interface, behavioral claim -- not "all sections"]     | [One sentence: what reviewer question does this surface answer?]  | [DOMAIN / LIFECYCLE / either] |
| S-002 | [Another specific surface -- not "all fields" or "the document"]          | [One sentence]                                                    | [DOMAIN / LIFECYCLE / either] |
| S-003 | [Optional -- add rows to be exhaustive; each must name a discrete surface]| [One sentence]                                                    | [DOMAIN / LIFECYCLE / either] |

*S-IDs (S-001, S-002, ...) carry to §1 IN-SCOPE below and to finding citations in every
reviewer section. A finding that cannot cite a registered S-ID is out-of-scope and must not
appear in Additional Findings.*

---

======================================================================
DISPOSITION_CONTRACT v1
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§5;
reviewer sections may not execute until §1 COMPLETE marker is reached]
======================================================================

§1 -- SCOPE ENUMERATION
[Fill this section before proceeding. Copy from SCOPE SURFACE REGISTER above by S-ID and name.
Do not add surfaces not in the register. Do not substitute generic descriptions for S-ID values.]

IN-SCOPE -- surfaces this review will evaluate (from SCOPE SURFACE REGISTER -- copy S-ID and name
exactly; do not add unlisted surfaces; do not substitute "all sections" or similar generic text):
  1. [S-001: copy name from register]
  2. [S-002: copy name from register]
  3. [S-003: copy if active]
  (Total row count must equal non-empty rows in SCOPE SURFACE REGISTER.)

OUT-OF-SCOPE -- surfaces this review will not evaluate:
  1. [SURFACE -- REASON_EXCLUDED]
  (Write "None" if nothing is excluded.)

Scope Amendment Protocol:
  SCOPE AMENDMENT: [surface] added to IN-SCOPE -- [reason]
  Silent scope expansion violates this contract.

§1 COMPLETE -- role selection and reviewer gates proceed below.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH   = Blocks commitment. No commitment proceeds with open HIGH findings.
  MEDIUM = Conditions commitment. Proceeds only after named resolution.
  LOW    = Advisory. Commitment may proceed.
  These definitions apply universally. They may not be restated at any gate.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE -- evaluated at DISPOSITION section]
  G = {GOpen, G_domain_agg, G_lifecycle, GClose}
  BLOCKED      <-- GClose = FAIL  [override: null hypothesis holds]
                OR  exists Gi = FAIL
  CONDITIONAL  <-- no Gi = FAIL  AND  exists Gi = CONDITIONAL
  READY        <-- all Gi = PASS

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"
  A missing cite is an audit-trail gap.

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Each challenge claim in BRACKET OPENING receives a CH-ID (CH-001, CH-002, ...).
  CH-ID COUNT: N = the number of CH-IDs declared in BRACKET OPENING. Record N
    in the "CH-ID Count declared" field immediately after the Challenge Claims table.
  Every downstream CH-ID table must contain exactly N rows -- one row per declared CH-ID.
    A table with fewer than N rows is a §5 count violation regardless of other completeness.
    A table with more than N rows invents claims not in evidence -- also a §5 violation.
  A PASS verdict is prohibited if any CH-ID row shows OPEN status.

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================

---

## ROLE MANIFEST

Read `.roles/signal/`. Assign each slot.

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (bracket open + close -- fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |

*Execution order: BRACKET OPENING -> LIFECYCLE -> DOMAIN -> BRACKET CLOSING.*
*LIFECYCLE runs first to surface commitment-readiness blockers before technical depth.*
*(For `--depth deep`: add DOMAIN-2, DOMAIN-3, etc. CHALLENGER positions remain fixed.
State total count.)*

---

## NULL HYPOTHESIS REGISTER

*Complete before BRACKET OPENING. Name the concrete alternative the team uses today.
Generic phrases ("do nothing", "status quo", "the current approach") are not acceptable --
name the specific tool, process, or workaround.*

| Field | Value |
|-------|-------|
| What teams use today | [Specific tool, process, or workaround the team relies on instead of building this] |
| Why it works well enough | [One sentence -- the genuine case for continuing with the status quo] |
| Where it breaks down | [One sentence -- the gap or friction that motivates this artifact] |
| Switching cost | [HIGH / MEDIUM / LOW] |
| Null hypothesis strength | [HIGH / MEDIUM / LOW -- how viable is the current approach overall?] |

*This register is the source of truth for all null hypothesis fields in this review.*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis** *(from NULL HYPOTHESIS REGISTER -- name the specific tool or process)*:
[The team continues to use [TOOL/PROCESS from Register] because [WHY IT WORKS from Register].
One sentence. Do not substitute generic language.]

**Null hypothesis strength**: [Copy from NULL HYPOTHESIS REGISTER -- HIGH / MEDIUM / LOW]

**Challenge claims** *(assign CH-IDs; carry to every downstream section per contract §5)*:

| CH-ID  | Challenge Claim                                                                            | Severity              |
|--------|--------------------------------------------------------------------------------------------|-----------------------|
| CH-001 | [CLAIM_1 -- switching cost, workaround viability, or adoption friction. One sentence.]     | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2]                                                                                  | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional]                                                                      | [HIGH / MEDIUM / LOW] |

**CH-ID Count declared**: N = [fill -- count the rows above. Every downstream CH-ID table
  must contain exactly N rows per contract §5.]

**Verify Question**: [One from challenger's `lens.verify`.]

**Simplify**: [One from challenger's `lens.simplify`.]

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]

*GOpen and all N CH-IDs above carry forward. Execution continues: LIFECYCLE -> DOMAIN -> BRACKET CLOSING.*

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [PASS / CONDITIONAL / FAIL -- copy from BRACKET OPENING]
*(DOMAIN has not yet run. LIFECYCLE assesses commitment readiness from GOpen alone.)*

**CH-ID Verdict Preview** *(fill the Status column now -- before writing the full response table)*:

| CH-ID  | Status                         |
|--------|--------------------------------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN]   |
| CH-002 | [ADDRESSED / PARTIAL / OPEN]   |
| CH-003 | [ADDRESSED / PARTIAL / OPEN -- omit if not active] |

**CH-ID Response Table** *(exactly N rows -- N from BRACKET OPENING "CH-ID Count declared" --
a row count other than N is a §5 contract violation)*:

| CH-ID  | Challenge Claim (copy) | This Role's Commitment-Frame Response | Status                       |
|--------|------------------------|---------------------------------------|------------------------------|
| CH-001 | [copy]                 | [RESPONSE_1]                          | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]                 | [RESPONSE_2]                          | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active]       | [RESPONSE_3]                          | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [Is evidence sufficient to proceed to technical review?
One paragraph referencing GOpen explicitly. Note: G_domain is not yet available -- assess
commitment readiness from challenger framing alone.]

**Null hypothesis status** *(reference NULL HYPOTHESIS REGISTER)*:
Given GOpen, the null hypothesis -- [restate: specific tool/process from Register] -- is:
[STILL VIABLE / CHALLENGED / OPEN]. Justification: [one sentence. Note: full defeat requires
DOMAIN review; this is a preliminary commitment-readiness assessment.]

**Additional Findings** *(each finding cites an S-ID from the SCOPE SURFACE REGISTER)*:
1. [FINDING_1 -- surface: S-00X. From this role's `lens.verify`. Commitment, program, or decision concerns.]
2. [FINDING_2 -- surface: S-00X.]

**Severity**: [HIGH / MEDIUM / LOW]
*Per contract §2.*

**Recommendation**: [One concrete action.]

**Verify Question**: [One from this role's `lens.verify`.]

**Simplify**: [One from this role's `lens.simplify`.]

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
**G_lifecycle Reason**: [One sentence. If FAIL: execution should pause -- DOMAIN review may
be deferred until this gate is resolved.]

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [PASS / CONDITIONAL / FAIL -- copy from BRACKET OPENING]
Received G_lifecycle: [PASS / CONDITIONAL / FAIL -- copy from LIFECYCLE]

**CH-ID Verdict Preview** *(fill the Status column now -- before writing the full response table.
This table is the convergence anchor vs LIFECYCLE Verdict Preview above.)*:

| CH-ID  | Status                         |
|--------|--------------------------------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN]   |
| CH-002 | [ADDRESSED / PARTIAL / OPEN]   |
| CH-003 | [ADDRESSED / PARTIAL / OPEN -- omit if not active] |

**CH-ID Response Table** *(exactly N rows -- N from BRACKET OPENING "CH-ID Count declared" --
a row count other than N is a §5 contract violation -- PASS verdict prohibited if any row = OPEN)*:

| CH-ID  | Challenge Claim (copy)             | This Role's Technical Response | Status                       |
|--------|------------------------------------|-------------------------------|------------------------------|
| CH-001 | [copy full claim from BRACKET OPENING] | [RESPONSE_1]              | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]                             | [RESPONSE_2]                  | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active]                   | [RESPONSE_3]                  | [ADDRESSED / PARTIAL / OPEN] |

*(PARTIAL requires a named resolution path. OPEN = claim not addressable from this role's frame.)*

**Additional Findings** *(each finding cites an S-ID from the SCOPE SURFACE REGISTER; a finding
that cannot cite a registered S-ID is out-of-scope and must not appear here)*:
1. [FINDING_1 -- surface: S-00X. From this role's `lens.verify` and `expertise.depth`.]
2. [FINDING_2 -- surface: S-00X.]
3. [FINDING_3 -- optional -- surface: S-00X.]
4. [FINDING_4 -- optional -- surface: S-00X.]

**Severity**: [HIGH / MEDIUM / LOW]
*Per contract §2. Do not copy GOpen or G_lifecycle severity.*

**Recommendation**: [One concrete action.]

**Verify Question**: [One from this role's `lens.verify`.]

**Simplify**: [One from this role's `lens.simplify`.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence. If CONDITIONAL: name condition. If FAIL: name gap.]

*(For `--depth deep`: repeat labeled DOMAIN-2, DOMAIN-3. G_domain Aggregate = worst verdict
among all DOMAIN rows. State aggregate explicitly below.)*

**G_domain Aggregate**: [PASS / CONDITIONAL / FAIL -- worst among all DOMAIN rows]

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1
*Full record received: scope declaration, all CH-ID tables, all gate verdicts.*

**CH-ID Cross-Gate Tally** *(copy from LIFECYCLE and DOMAIN Verdict Preview tables above --
scan for convergence: same non-ADDRESSED status in both columns = high-confidence signal)*:

| CH-ID  | LIFECYCLE Status                  | DOMAIN Status                    | Converged? |
|--------|-----------------------------------|----------------------------------|------------|
| CH-001 | [copy from LIFECYCLE preview]     | [copy from DOMAIN preview]       | [yes / no] |
| CH-002 | [copy]                            | [copy]                           | [yes / no] |
| CH-003 | [copy if active]                  | [copy if active]                 | [yes / no] |

**CH-ID Final Assessment** *(exactly N rows -- N from BRACKET OPENING "CH-ID Count declared" --
a row count other than N is a §5 contract violation)*:

| CH-ID  | G_lifecycle Status | G_domain Status | Final Status                    | Notes              |
|--------|-------------------|-----------------|---------------------------------|--------------------|
| CH-001 | [copy from LIFECYCLE] | [copy from DOMAIN] | [DEFEATED / PARTIAL / HOLDS] | [ONE_SENTENCE_NOTE] |
| CH-002 | [copy]            | [copy]          | [DEFEATED / PARTIAL / HOLDS]    | [note]             |
| CH-003 | [copy if active]  | [copy]          | [DEFEATED / PARTIAL / HOLDS]    | [note]             |

**Remaining gaps**: [What was not fully addressed. If none: "None -- all CH-IDs DEFEATED."]

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
- PASS (= DEFEATED): All CH-IDs DEFEATED -- accumulated record defeats the null hypothesis.
- CONDITIONAL (= PARTIAL): Some CH-IDs PARTIAL -- material gaps remain; name them.
- FAIL (= HOLDS): At least one CH-ID HOLDS -- null hypothesis survives.

**GClose override authority**: GClose = FAIL overrides all prior gate verdicts. A HOLDS verdict
from the challenger is not overturned by G_lifecycle or G_domain PASses. This override is
pre-stated in the contract §3 and is not subject to editorial revision at the Disposition step.

**GClose Rationale**: [2-3 sentences. Reference the specific tool/process from NULL HYPOTHESIS
REGISTER when stating whether it has been defeated.]

---

## GATE VECTOR TABLE

*(Execution order: GOpen -> G_lifecycle -> G_domain -> GClose. §3 algebra operates on the set --
order does not affect the disposition formula.)*

| Gate                        | Reviewer          | Verdict                    | Contract Cite            |
|-----------------------------|-------------------|----------------------------|--------------------------|
| GOpen -- bracket opening    | [CHALLENGER_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1  |
| G_lifecycle -- lifecycle    | [LIFECYCLE_ROLE]  | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1  |
| G_domain -- domain aggregate| [DOMAIN_ROLE(S)]  | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1  |
| GClose -- bracket closing   | [CHALLENGER_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1  |

---

## CROSS-ROLE SIGNALS

**Convergence** *(scan CH-ID Cross-Gate Tally in BRACKET CLOSING -- rows where Converged = yes
are the highest-confidence signals; name each by CH-ID. If no converged rows: "None detected.")*:

**Conflicts**: [Two reviewers with incompatible CH-ID responses or incompatible findings --
name roles and tension. If none: "None detected."]

**Scope coverage** *(scan SCOPE SURFACE REGISTER S-IDs against findings in all reviewer sections --
any S-ID not cited by any finding is a coverage gap; list it with the S-ID and name)*:
[S-00X: [surface name] -- no reviewer cited this surface. OR "None -- all registered surfaces cited."]

---

## DISPOSITION

**Gate vector** *(fill from GATE VECTOR TABLE above)*:
- GOpen = [copy]
- G_domain_agg = [copy]
- G_lifecycle = [copy]
- GClose = [copy]

**Apply contract §3 formula** *(do not alter the formula; do not reason editorially -- evaluate
the gate vector against the pre-stated formula)*:

```
G = {GOpen=[_], G_domain_agg=[_], G_lifecycle=[_], GClose=[_]}
GClose = FAIL? --> BLOCKED  (challenger override: null hypothesis holds)
Any other Gi = FAIL? --> BLOCKED
No FAIL, any CONDITIONAL? --> CONDITIONAL
All PASS? --> READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED -- result of evaluating the formula above]

**Null hypothesis defeat** *(from GClose verdict and NULL HYPOTHESIS REGISTER)*:
[DEFEATED / PARTIALLY DEFEATED / HOLDS -- one sentence. If GClose = FAIL: "HOLDS -- [specific
tool/process from Register] remains the team's viable alternative: [GClose Rationale summary]."]

**Primary driver**: [The gate verdict most responsible for this disposition -- one sentence.
Do not reason from findings -- the formula completed the derivation.]

**Conditions** *(complete only if CONDITIONAL)*:
1. [Condition from first CONDITIONAL gate. Gate order for resolution: GOpen -> G_lifecycle -> G_domain -> GClose.]
2. [Additional conditions if present.]

**Blocker** *(complete only if BLOCKED)*: [Specific finding from the FAIL gate.]

---

## ACTION ITEM REGISTER

*One row per PARTIAL or HOLDS CH-ID from BRACKET CLOSING. Items not sourced from a CH-ID are
marked ADVISORY-OBS. This register is the CH-ID-indexed synthesis artifact per contract §5.*

| CH-ID  | Item Description  | Disposition Class                       | Owner Role   | Resolution Criterion                                     |
|--------|-------------------|-----------------------------------------|--------------|----------------------------------------------------------|
| CH-001 | [What must be done] | [BLOCKED / CONDITIONAL / ADVISORY]    | [ROLE_NAME]  | [One sentence: what must be true to close this item]     |
| CH-002 | [Item 2]          | [BLOCKED / CONDITIONAL / ADVISORY]      | [ROLE_NAME]  | [Resolution criterion]                                   |
| --     | [Advisory observation not sourced from a CH-ID, if any] | ADVISORY-OBS | [ROLE_NAME] | [Criterion]             |

*Every row traces: BRACKET OPENING CH-ID -> reviewer CH-ID tables -> BRACKET CLOSING final status.*

---

**Artifact to review:**

{{artifact}}
```

---

## V-02 -- Single Axis: FINDING SURFACE LINKAGE TABLE

**Variation axis**: Structured findings table replacing prose Additional Findings.

**Hypothesis**: "Additional Findings" as numbered prose allows findings that reference no specific in-scope surface and invoke no named role lens -- a reviewer can write a generic observation without the template preventing it. Replacing prose with a structured table (Finding / In-Scope Surface / Role Lens / Severity) makes each finding structurally accountable to a specific §1 surface and a named lens.verify entry. C-10 (domain findings role-grounded and in-scope) becomes template-determined: if the Surface column contains "the document" or the Role Lens column contains "general expertise", the violation is visible at the table cell, not at the scoring inference step. Expected excellence pattern: E-2 (new, v4 candidate C-16) -- generalizes C-13 register mechanism from pre-section registers to in-section structured columns.

**Changes from V-05 R2**:
- DOMAIN Additional Findings: replace prose list with a structured table (Finding / In-Scope Surface / Role Lens / Severity)
- LIFECYCLE Additional Findings: same structured table
- Both tables include instruction: "In-Scope Surface must match a §1 surface name exactly. Role Lens must name a specific lens.verify entry, not 'general expertise'. A finding citing no §1 surface is out of scope and must not appear."

---

```
depth: standard
confidence: standard
for: {value}
iterations: 1

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any pre-printed
heading, label, field, formula, or structural element. Do not add sections between pre-printed
headers. If a field cannot be filled, write `[N/A -- reason]`.

---

======================================================================
DISPOSITION_CONTRACT v1
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§5;
reviewer sections may not execute until §1 COMPLETE marker is reached]
======================================================================

§1 -- SCOPE ENUMERATION
[Fill this section before proceeding. This is the pre-reviewer gate.]

IN-SCOPE -- surfaces this review will evaluate:
  1. [SURFACE_1 -- name a specific section, interface, behavioral claim, or schema component]
  2. [SURFACE_2 -- not "all sections" or "the full document"]
  3. [SURFACE_3 -- optional]
  (Add rows. Be exhaustive. Each row is cited by findings in reviewer sections.)

OUT-OF-SCOPE -- surfaces this review will not evaluate:
  1. [SURFACE -- REASON_EXCLUDED]
  (Write "None" if nothing is excluded.)

Scope Amendment Protocol:
  SCOPE AMENDMENT: [surface] added to IN-SCOPE -- [reason]
  Silent scope expansion violates this contract.

§1 COMPLETE -- role selection and reviewer gates proceed below.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH   = Blocks commitment. No commitment proceeds with open HIGH findings.
  MEDIUM = Conditions commitment. Proceeds only after named resolution.
  LOW    = Advisory. Commitment may proceed.
  These definitions apply universally. They may not be restated at any gate.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE -- evaluated at DISPOSITION section]
  G = {GOpen, G_domain_agg, G_lifecycle, GClose}
  BLOCKED      <-- GClose = FAIL  [override: null hypothesis holds]
                OR  exists Gi = FAIL
  CONDITIONAL  <-- no Gi = FAIL  AND  exists Gi = CONDITIONAL
  READY        <-- all Gi = PASS

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"
  A missing cite is an audit-trail gap.

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Each challenge claim in BRACKET OPENING receives a CH-ID (CH-001, CH-002, ...).
  CH-ID COUNT: N = the number of CH-IDs declared in BRACKET OPENING. Record N
    in the "CH-ID Count declared" field immediately after the Challenge Claims table.
  Every downstream CH-ID table must contain exactly N rows -- one row per declared CH-ID.
    A table with fewer than N rows is a §5 count violation regardless of other completeness.
    A table with more than N rows invents claims not in evidence -- also a §5 violation.
  A PASS verdict is prohibited if any CH-ID row shows OPEN status.

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================

---

## ROLE MANIFEST

Read `.roles/signal/`. Assign each slot.

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (bracket open + close -- fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |

*Execution order: BRACKET OPENING -> LIFECYCLE -> DOMAIN -> BRACKET CLOSING.*
*LIFECYCLE runs first to surface commitment-readiness blockers before technical depth.*
*(For `--depth deep`: add DOMAIN-2, DOMAIN-3, etc. CHALLENGER positions remain fixed.
State total count.)*

---

## NULL HYPOTHESIS REGISTER

*Complete before BRACKET OPENING. Name the concrete alternative the team uses today.
Generic phrases ("do nothing", "status quo", "the current approach") are not acceptable --
name the specific tool, process, or workaround.*

| Field | Value |
|-------|-------|
| What teams use today | [Specific tool, process, or workaround the team relies on instead of building this] |
| Why it works well enough | [One sentence -- the genuine case for continuing with the status quo] |
| Where it breaks down | [One sentence -- the gap or friction that motivates this artifact] |
| Switching cost | [HIGH / MEDIUM / LOW] |
| Null hypothesis strength | [HIGH / MEDIUM / LOW -- how viable is the current approach overall?] |

*This register is the source of truth for all null hypothesis fields in this review.*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis** *(from NULL HYPOTHESIS REGISTER -- name the specific tool or process)*:
[The team continues to use [TOOL/PROCESS from Register] because [WHY IT WORKS from Register].
One sentence. Do not substitute generic language.]

**Null hypothesis strength**: [Copy from NULL HYPOTHESIS REGISTER -- HIGH / MEDIUM / LOW]

**Challenge claims** *(assign CH-IDs; carry to every downstream section per contract §5)*:

| CH-ID  | Challenge Claim                                                                            | Severity              |
|--------|--------------------------------------------------------------------------------------------|-----------------------|
| CH-001 | [CLAIM_1 -- switching cost, workaround viability, or adoption friction. One sentence.]     | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2]                                                                                  | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional]                                                                      | [HIGH / MEDIUM / LOW] |

**CH-ID Count declared**: N = [fill -- count the rows above. Every downstream CH-ID table
  must contain exactly N rows per contract §5.]

**Verify Question**: [One from challenger's `lens.verify`.]

**Simplify**: [One from challenger's `lens.simplify`.]

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]

*GOpen and all N CH-IDs above carry forward. Execution continues: LIFECYCLE -> DOMAIN -> BRACKET CLOSING.*

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [PASS / CONDITIONAL / FAIL -- copy from BRACKET OPENING]
*(DOMAIN has not yet run. LIFECYCLE assesses commitment readiness from GOpen alone.)*

**CH-ID Verdict Preview** *(fill the Status column now -- before writing the full response table)*:

| CH-ID  | Status                         |
|--------|--------------------------------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN]   |
| CH-002 | [ADDRESSED / PARTIAL / OPEN]   |
| CH-003 | [ADDRESSED / PARTIAL / OPEN -- omit if not active] |

**CH-ID Response Table** *(exactly N rows -- N from BRACKET OPENING "CH-ID Count declared" --
a row count other than N is a §5 contract violation)*:

| CH-ID  | Challenge Claim (copy) | This Role's Commitment-Frame Response | Status                       |
|--------|------------------------|---------------------------------------|------------------------------|
| CH-001 | [copy]                 | [RESPONSE_1]                          | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]                 | [RESPONSE_2]                          | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active]       | [RESPONSE_3]                          | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [Is evidence sufficient to proceed to technical review?
One paragraph referencing GOpen explicitly. Note: G_domain is not yet available -- assess
commitment readiness from challenger framing alone.]

**Null hypothesis status** *(reference NULL HYPOTHESIS REGISTER)*:
Given GOpen, the null hypothesis -- [restate: specific tool/process from Register] -- is:
[STILL VIABLE / CHALLENGED / OPEN]. Justification: [one sentence.]

**Additional Findings** *(structured table -- In-Scope Surface must match a §1 surface name exactly;
Role Lens must name a specific lens.verify entry from this role's definition, not "general expertise";
a finding that cites no §1 surface is out-of-scope and must not appear)*:

| # | Finding | In-Scope Surface (from §1 -- exact name) | Role Lens (from this role's lens.verify) | Severity              |
|---|---------|------------------------------------------|------------------------------------------|-----------------------|
| 1 | [FINDING_1 -- commitment, program, or decision concern] | [copy §1 surface name] | [Named lens.verify entry] | [HIGH / MEDIUM / LOW] |
| 2 | [FINDING_2] | [copy §1 surface name] | [Named lens.verify entry] | [HIGH / MEDIUM / LOW] |

**Severity**: [HIGH / MEDIUM / LOW]
*Per contract §2.*

**Recommendation**: [One concrete action.]

**Verify Question**: [One from this role's `lens.verify`.]

**Simplify**: [One from this role's `lens.simplify`.]

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
**G_lifecycle Reason**: [One sentence. If FAIL: execution should pause -- DOMAIN review may
be deferred until this gate is resolved.]

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [PASS / CONDITIONAL / FAIL -- copy from BRACKET OPENING]
Received G_lifecycle: [PASS / CONDITIONAL / FAIL -- copy from LIFECYCLE]

**CH-ID Verdict Preview** *(fill the Status column now -- before writing the full response table.
This table is the convergence anchor vs LIFECYCLE Verdict Preview above.)*:

| CH-ID  | Status                         |
|--------|--------------------------------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN]   |
| CH-002 | [ADDRESSED / PARTIAL / OPEN]   |
| CH-003 | [ADDRESSED / PARTIAL / OPEN -- omit if not active] |

**CH-ID Response Table** *(exactly N rows -- N from BRACKET OPENING "CH-ID Count declared" --
a row count other than N is a §5 contract violation -- PASS verdict prohibited if any row = OPEN)*:

| CH-ID  | Challenge Claim (copy)                 | This Role's Technical Response | Status                       |
|--------|----------------------------------------|-------------------------------|------------------------------|
| CH-001 | [copy full claim from BRACKET OPENING] | [RESPONSE_1]                  | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]                                 | [RESPONSE_2]                  | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active]                       | [RESPONSE_3]                  | [ADDRESSED / PARTIAL / OPEN] |

*(PARTIAL requires a named resolution path. OPEN = claim not addressable from this role's frame.)*

**Additional Findings** *(structured table -- In-Scope Surface must match a §1 surface name exactly;
Role Lens must name a specific lens.verify entry from this role's definition, not "general expertise";
a finding that cites no §1 surface is out-of-scope and must not appear)*:

| # | Finding | In-Scope Surface (from §1 -- exact name) | Role Lens (from this role's lens.verify) | Severity              |
|---|---------|------------------------------------------|------------------------------------------|-----------------------|
| 1 | [FINDING_1 -- technical concern grounded in this role's expertise] | [copy §1 surface name] | [Named lens.verify entry] | [HIGH / MEDIUM / LOW] |
| 2 | [FINDING_2] | [copy §1 surface name] | [Named lens.verify entry] | [HIGH / MEDIUM / LOW] |
| 3 | [FINDING_3 -- optional] | [copy §1 surface name] | [Named lens.verify entry] | [HIGH / MEDIUM / LOW] |
| 4 | [FINDING_4 -- optional] | [copy §1 surface name] | [Named lens.verify entry] | [HIGH / MEDIUM / LOW] |

*(C-10 check: at least 2 of 3 findings must name a different §1 surface and a different lens.verify
entry. A finding using "the document" or "general expertise" fails the role-grounding test.)*

**Severity**: [HIGH / MEDIUM / LOW]
*Per contract §2. Do not copy GOpen or G_lifecycle severity.*

**Recommendation**: [One concrete action.]

**Verify Question**: [One from this role's `lens.verify`.]

**Simplify**: [One from this role's `lens.simplify`.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence. If CONDITIONAL: name condition. If FAIL: name gap.]

*(For `--depth deep`: repeat labeled DOMAIN-2, DOMAIN-3. G_domain Aggregate = worst verdict
among all DOMAIN rows. State aggregate explicitly below.)*

**G_domain Aggregate**: [PASS / CONDITIONAL / FAIL -- worst among all DOMAIN rows]

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1
*Full record received: scope declaration, all CH-ID tables, all gate verdicts.*

**CH-ID Cross-Gate Tally** *(copy from LIFECYCLE and DOMAIN Verdict Preview tables above --
scan for convergence: same non-ADDRESSED status in both columns = high-confidence signal)*:

| CH-ID  | LIFECYCLE Status              | DOMAIN Status                | Converged? |
|--------|-------------------------------|------------------------------|------------|
| CH-001 | [copy from LIFECYCLE preview] | [copy from DOMAIN preview]   | [yes / no] |
| CH-002 | [copy]                        | [copy]                       | [yes / no] |
| CH-003 | [copy if active]              | [copy if active]             | [yes / no] |

**CH-ID Final Assessment** *(exactly N rows -- N from BRACKET OPENING "CH-ID Count declared" --
a row count other than N is a §5 contract violation)*:

| CH-ID  | G_lifecycle Status      | G_domain Status  | Final Status                 | Notes               |
|--------|------------------------|------------------|------------------------------|---------------------|
| CH-001 | [copy from LIFECYCLE]  | [copy from DOMAIN] | [DEFEATED / PARTIAL / HOLDS] | [ONE_SENTENCE_NOTE] |
| CH-002 | [copy]                 | [copy]           | [DEFEATED / PARTIAL / HOLDS] | [note]              |
| CH-003 | [copy if active]       | [copy]           | [DEFEATED / PARTIAL / HOLDS] | [note]              |

**Remaining gaps**: [What was not fully addressed. If none: "None -- all CH-IDs DEFEATED."]

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
- PASS (= DEFEATED): All CH-IDs DEFEATED -- accumulated record defeats the null hypothesis.
- CONDITIONAL (= PARTIAL): Some CH-IDs PARTIAL -- material gaps remain; name them.
- FAIL (= HOLDS): At least one CH-ID HOLDS -- null hypothesis survives.

**GClose override authority**: GClose = FAIL overrides all prior gate verdicts. This override
is pre-stated in the contract §3 and is not subject to editorial revision at the Disposition step.

**GClose Rationale**: [2-3 sentences. Reference the specific tool/process from NULL HYPOTHESIS
REGISTER when stating whether it has been defeated.]

---

## GATE VECTOR TABLE

*(Execution order: GOpen -> G_lifecycle -> G_domain -> GClose. §3 algebra operates on the set.)*

| Gate                         | Reviewer          | Verdict                     | Contract Cite           |
|------------------------------|-------------------|-----------------------------|-------------------------|
| GOpen -- bracket opening     | [CHALLENGER_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_lifecycle -- lifecycle     | [LIFECYCLE_ROLE]  | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_domain -- domain aggregate | [DOMAIN_ROLE(S)]  | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| GClose -- bracket closing    | [CHALLENGER_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Convergence** *(scan CH-ID Cross-Gate Tally in BRACKET CLOSING -- rows where Converged = yes
are the highest-confidence signals; name each by CH-ID. If no converged rows: "None detected.")*:

**Conflicts**: [Two reviewers with incompatible CH-ID responses or findings --
name roles and tension. If none: "None detected."]

**Scope coverage**: [Any in-scope surface from contract §1 not cited by any finding in any
reviewer section -- list it. If all cited: "None -- all §1 surfaces referenced."]

---

## DISPOSITION

**Gate vector** *(fill from GATE VECTOR TABLE above)*:
- GOpen = [copy]
- G_domain_agg = [copy]
- G_lifecycle = [copy]
- GClose = [copy]

**Apply contract §3 formula** *(do not alter the formula; do not reason editorially)*:

```
G = {GOpen=[_], G_domain_agg=[_], G_lifecycle=[_], GClose=[_]}
GClose = FAIL? --> BLOCKED  (challenger override: null hypothesis holds)
Any other Gi = FAIL? --> BLOCKED
No FAIL, any CONDITIONAL? --> CONDITIONAL
All PASS? --> READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**Null hypothesis defeat** *(from GClose verdict and NULL HYPOTHESIS REGISTER)*:
[DEFEATED / PARTIALLY DEFEATED / HOLDS -- one sentence. If GClose = FAIL: "HOLDS -- [specific
tool/process from Register] remains the team's viable alternative: [GClose Rationale summary]."]

**Primary driver**: [The gate verdict most responsible for this disposition -- one sentence.
Do not reason from findings -- the formula completed the derivation.]

**Conditions** *(complete only if CONDITIONAL)*:
1. [Condition from first CONDITIONAL gate.]
2. [Additional conditions if present.]

**Blocker** *(complete only if BLOCKED)*: [Specific finding from the FAIL gate.]

---

## ACTION ITEM REGISTER

*One row per PARTIAL or HOLDS CH-ID from BRACKET CLOSING. Items not sourced from a CH-ID are
marked ADVISORY-OBS. This register is the CH-ID-indexed synthesis artifact per contract §5.*

| CH-ID  | Item Description    | Disposition Class                    | Owner Role  | Resolution Criterion                               |
|--------|---------------------|--------------------------------------|-------------|---------------------------------------------------|
| CH-001 | [What must be done] | [BLOCKED / CONDITIONAL / ADVISORY]   | [ROLE_NAME] | [One sentence: what must be true to close this]   |
| CH-002 | [Item 2]            | [BLOCKED / CONDITIONAL / ADVISORY]   | [ROLE_NAME] | [Resolution criterion]                            |
| --     | [Advisory observation, if any] | ADVISORY-OBS              | [ROLE_NAME] | [Criterion]                                       |

*Every row traces: BRACKET OPENING CH-ID -> reviewer CH-ID tables -> BRACKET CLOSING final status.*

---

**Artifact to review:**

{{artifact}}
```

---

## V-03 -- Single Axis: Per-Finding Severity Aggregation

**Variation axis**: Per-finding severity tag with mechanical worst-case section severity formula.

**Hypothesis**: Each reviewer section currently emits ONE severity label covering all findings collectively, assigned editorially. This allows a HIGH-severity finding to be masked by a reviewer who assigns LOW to the section overall. Adding an individual severity tag to each finding and a mechanical aggregation formula (Section Severity = worst(all finding severities)) creates an auditable chain: individual finding -> individual severity -> formula -> section severity -> gate verdict. A HIGH finding cannot produce a LOW section severity without a visible formula-deviation. This is structurally similar to §3a (G_domain_agg = worst of domain verdicts) applied one level deeper: finding severity -> section severity. Expected excellence pattern: E-3 (new, v4 candidate C-17) -- pre-committed worst-case formula eliminates editorial severity assignment at section level.

**Changes from V-05 R2**:
- DOMAIN findings: each item gets inline `Severity: [HIGH / MEDIUM / LOW]` tag
- LIFECYCLE findings: same inline severity tag
- After findings list in each reviewer section: add "Section Severity Formula" block showing worst-case derivation
- The existing **Severity** field becomes: "Section Severity: [result from formula -- do not assign independently]"

---

```
depth: standard
confidence: standard
for: {value}
iterations: 1

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any pre-printed
heading, label, field, formula, or structural element. Do not add sections between pre-printed
headers. If a field cannot be filled, write `[N/A -- reason]`.

---

======================================================================
DISPOSITION_CONTRACT v1
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§5;
reviewer sections may not execute until §1 COMPLETE marker is reached]
======================================================================

§1 -- SCOPE ENUMERATION
[Fill this section before proceeding. This is the pre-reviewer gate.]

IN-SCOPE -- surfaces this review will evaluate:
  1. [SURFACE_1]
  2. [SURFACE_2]
  3. [SURFACE_3]
  (Add rows. Be exhaustive.)

OUT-OF-SCOPE -- surfaces this review will not evaluate:
  1. [SURFACE -- REASON_EXCLUDED]
  (Write "None" if nothing is excluded.)

Scope Amendment Protocol:
  SCOPE AMENDMENT: [surface] added to IN-SCOPE -- [reason]
  Silent scope expansion violates this contract.

§1 COMPLETE -- role selection and reviewer gates proceed below.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH   = Blocks commitment. No commitment proceeds with open HIGH findings.
  MEDIUM = Conditions commitment. Proceeds only after named resolution.
  LOW    = Advisory. Commitment may proceed.
  These definitions apply universally. They may not be restated at any gate.

§2a -- SECTION SEVERITY FORMULA [IMMUTABLE -- applied in each reviewer section]
  Section Severity = worst(all individual finding severities in this section).
  Precedence: HIGH > MEDIUM > LOW.
  A section with at least one HIGH finding must emit Section Severity = HIGH.
  No editorial override. The formula result is the Section Severity -- do not assign independently.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE -- evaluated at DISPOSITION section]
  G = {GOpen, G_domain_agg, G_lifecycle, GClose}
  BLOCKED      <-- GClose = FAIL  [override: null hypothesis holds]
                OR  exists Gi = FAIL
  CONDITIONAL  <-- no Gi = FAIL  AND  exists Gi = CONDITIONAL
  READY        <-- all Gi = PASS

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"
  A missing cite is an audit-trail gap.

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Each challenge claim in BRACKET OPENING receives a CH-ID (CH-001, CH-002, ...).
  CH-ID COUNT: N = the number of CH-IDs declared in BRACKET OPENING. Record N
    in the "CH-ID Count declared" field immediately after the Challenge Claims table.
  Every downstream CH-ID table must contain exactly N rows -- one row per declared CH-ID.
    A table with fewer than N rows is a §5 count violation regardless of other completeness.
    A table with more than N rows invents claims not in evidence -- also a §5 violation.
  A PASS verdict is prohibited if any CH-ID row shows OPEN status.

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================

---

## ROLE MANIFEST

Read `.roles/signal/`. Assign each slot.

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (bracket open + close -- fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |

*Execution order: BRACKET OPENING -> LIFECYCLE -> DOMAIN -> BRACKET CLOSING.*
*LIFECYCLE runs first to surface commitment-readiness blockers before technical depth.*
*(For `--depth deep`: add DOMAIN-2, DOMAIN-3, etc. CHALLENGER positions remain fixed.
State total count.)*

---

## NULL HYPOTHESIS REGISTER

*Complete before BRACKET OPENING. Name the concrete alternative the team uses today.
Generic phrases ("do nothing", "status quo", "the current approach") are not acceptable --
name the specific tool, process, or workaround.*

| Field | Value |
|-------|-------|
| What teams use today | [Specific tool, process, or workaround the team relies on instead of building this] |
| Why it works well enough | [One sentence -- the genuine case for continuing with the status quo] |
| Where it breaks down | [One sentence -- the gap or friction that motivates this artifact] |
| Switching cost | [HIGH / MEDIUM / LOW] |
| Null hypothesis strength | [HIGH / MEDIUM / LOW -- how viable is the current approach overall?] |

*This register is the source of truth for all null hypothesis fields in this review.*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis** *(from NULL HYPOTHESIS REGISTER -- name the specific tool or process)*:
[The team continues to use [TOOL/PROCESS from Register] because [WHY IT WORKS from Register].
One sentence. Do not substitute generic language.]

**Null hypothesis strength**: [Copy from NULL HYPOTHESIS REGISTER -- HIGH / MEDIUM / LOW]

**Challenge claims** *(assign CH-IDs; carry to every downstream section per contract §5)*:

| CH-ID  | Challenge Claim                                                                        | Severity              |
|--------|----------------------------------------------------------------------------------------|-----------------------|
| CH-001 | [CLAIM_1 -- switching cost, workaround viability, or adoption friction. One sentence.] | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2]                                                                              | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional]                                                                  | [HIGH / MEDIUM / LOW] |

**CH-ID Count declared**: N = [fill -- count the rows above. Every downstream CH-ID table
  must contain exactly N rows per contract §5.]

**Verify Question**: [One from challenger's `lens.verify`.]

**Simplify**: [One from challenger's `lens.simplify`.]

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]

*GOpen and all N CH-IDs above carry forward. Execution continues: LIFECYCLE -> DOMAIN -> BRACKET CLOSING.*

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [PASS / CONDITIONAL / FAIL -- copy from BRACKET OPENING]
*(DOMAIN has not yet run. LIFECYCLE assesses commitment readiness from GOpen alone.)*

**CH-ID Verdict Preview** *(fill the Status column now -- before writing the full response table)*:

| CH-ID  | Status                         |
|--------|--------------------------------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN]   |
| CH-002 | [ADDRESSED / PARTIAL / OPEN]   |
| CH-003 | [ADDRESSED / PARTIAL / OPEN -- omit if not active] |

**CH-ID Response Table** *(exactly N rows -- N from BRACKET OPENING "CH-ID Count declared" --
a row count other than N is a §5 contract violation)*:

| CH-ID  | Challenge Claim (copy) | This Role's Commitment-Frame Response | Status                       |
|--------|------------------------|---------------------------------------|------------------------------|
| CH-001 | [copy]                 | [RESPONSE_1]                          | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]                 | [RESPONSE_2]                          | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active]       | [RESPONSE_3]                          | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [Is evidence sufficient to proceed to technical review?
One paragraph referencing GOpen explicitly. Note: G_domain is not yet available.]

**Null hypothesis status** *(reference NULL HYPOTHESIS REGISTER)*:
Given GOpen, the null hypothesis -- [restate: specific tool/process from Register] -- is:
[STILL VIABLE / CHALLENGED / OPEN]. Justification: [one sentence.]

**Additional Findings** *(each finding carries an individual severity tag; do not assign
Section Severity below until all individual tags are filled)*:
1. [FINDING_1 -- from this role's `lens.verify`. Commitment, program, or decision concern. Names an in-scope surface.] | **Severity**: [HIGH / MEDIUM / LOW]
2. [FINDING_2 -- names an in-scope surface.] | **Severity**: [HIGH / MEDIUM / LOW]

**Section Severity Formula** *(apply §2a -- do not assign Section Severity independently)*:
  Finding severities: [list from above, e.g., HIGH, MEDIUM]
  Section Severity = worst([...]) = [HIGH / MEDIUM / LOW]

**Section Severity**: [Copy result from formula above -- do not assign editorially.]
*Per contract §2 and §2a.*

**Recommendation**: [One concrete action.]

**Verify Question**: [One from this role's `lens.verify`.]

**Simplify**: [One from this role's `lens.simplify`.]

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
**G_lifecycle Reason**: [One sentence. If FAIL: execution should pause.]

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [PASS / CONDITIONAL / FAIL -- copy from BRACKET OPENING]
Received G_lifecycle: [PASS / CONDITIONAL / FAIL -- copy from LIFECYCLE]

**CH-ID Verdict Preview** *(fill the Status column now -- convergence anchor vs LIFECYCLE preview)*:

| CH-ID  | Status                         |
|--------|--------------------------------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN]   |
| CH-002 | [ADDRESSED / PARTIAL / OPEN]   |
| CH-003 | [ADDRESSED / PARTIAL / OPEN -- omit if not active] |

**CH-ID Response Table** *(exactly N rows -- §5 contract violation if row count differs from N --
PASS verdict prohibited if any row = OPEN)*:

| CH-ID  | Challenge Claim (copy)                 | This Role's Technical Response | Status                       |
|--------|----------------------------------------|-------------------------------|------------------------------|
| CH-001 | [copy full claim from BRACKET OPENING] | [RESPONSE_1]                  | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]                                 | [RESPONSE_2]                  | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active]                       | [RESPONSE_3]                  | [ADDRESSED / PARTIAL / OPEN] |

*(PARTIAL requires a named resolution path. OPEN = claim not addressable from this role's frame.)*

**Additional Findings** *(each finding carries an individual severity tag; do not assign
Section Severity below until all individual tags are filled)*:
1. [FINDING_1 -- from this role's `lens.verify` and `expertise.depth`. Names an in-scope surface.] | **Severity**: [HIGH / MEDIUM / LOW]
2. [FINDING_2 -- names an in-scope surface.] | **Severity**: [HIGH / MEDIUM / LOW]
3. [FINDING_3 -- optional -- names an in-scope surface.] | **Severity**: [HIGH / MEDIUM / LOW]
4. [FINDING_4 -- optional -- names an in-scope surface.] | **Severity**: [HIGH / MEDIUM / LOW]

**Section Severity Formula** *(apply §2a -- do not assign Section Severity independently)*:
  Finding severities: [list from above, e.g., HIGH, MEDIUM, LOW]
  Section Severity = worst([...]) = [HIGH / MEDIUM / LOW]

**Section Severity**: [Copy result from formula above -- do not assign editorially.]
*Per contract §2 and §2a. Do not copy GOpen or G_lifecycle severity.*

**Recommendation**: [One concrete action.]

**Verify Question**: [One from this role's `lens.verify`.]

**Simplify**: [One from this role's `lens.simplify`.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence. Section Severity = HIGH -> strong signal for FAIL or CONDITIONAL.]

*(For `--depth deep`: repeat labeled DOMAIN-2, DOMAIN-3. G_domain Aggregate = worst verdict
among all DOMAIN rows. State aggregate explicitly below.)*

**G_domain Aggregate**: [PASS / CONDITIONAL / FAIL -- worst among all DOMAIN rows]

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1
*Full record received: scope declaration, all CH-ID tables, all gate verdicts.*

**CH-ID Cross-Gate Tally** *(copy from LIFECYCLE and DOMAIN Verdict Preview tables above)*:

| CH-ID  | LIFECYCLE Status              | DOMAIN Status              | Converged? |
|--------|-------------------------------|----------------------------|------------|
| CH-001 | [copy from LIFECYCLE preview] | [copy from DOMAIN preview] | [yes / no] |
| CH-002 | [copy]                        | [copy]                     | [yes / no] |
| CH-003 | [copy if active]              | [copy if active]           | [yes / no] |

**CH-ID Final Assessment** *(exactly N rows -- §5 contract violation if row count differs from N)*:

| CH-ID  | G_lifecycle Status      | G_domain Status    | Final Status                 | Notes               |
|--------|------------------------|--------------------|------------------------------|---------------------|
| CH-001 | [copy from LIFECYCLE]  | [copy from DOMAIN] | [DEFEATED / PARTIAL / HOLDS] | [ONE_SENTENCE_NOTE] |
| CH-002 | [copy]                 | [copy]             | [DEFEATED / PARTIAL / HOLDS] | [note]              |
| CH-003 | [copy if active]       | [copy]             | [DEFEATED / PARTIAL / HOLDS] | [note]              |

**Remaining gaps**: [What was not fully addressed. If none: "None -- all CH-IDs DEFEATED."]

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
- PASS (= DEFEATED): All CH-IDs DEFEATED.
- CONDITIONAL (= PARTIAL): Some CH-IDs PARTIAL -- name them.
- FAIL (= HOLDS): At least one CH-ID HOLDS.

**GClose override authority**: GClose = FAIL overrides all prior gate verdicts per §3.

**GClose Rationale**: [2-3 sentences. Reference the specific tool/process from NULL HYPOTHESIS
REGISTER when stating whether it has been defeated.]

---

## GATE VECTOR TABLE

*(Execution order: GOpen -> G_lifecycle -> G_domain -> GClose. §3 algebra operates on the set.)*

| Gate                         | Reviewer          | Verdict                     | Contract Cite           |
|------------------------------|-------------------|-----------------------------|-------------------------|
| GOpen -- bracket opening     | [CHALLENGER_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_lifecycle -- lifecycle     | [LIFECYCLE_ROLE]  | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_domain -- domain aggregate | [DOMAIN_ROLE(S)]  | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| GClose -- bracket closing    | [CHALLENGER_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Convergence** *(scan CH-ID Cross-Gate Tally -- rows where Converged = yes; name each by CH-ID)*:

**Conflicts**: [Incompatible responses or findings between reviewers -- name roles and tension.
If none: "None detected."]

**Scope coverage**: [Any §1 surface not addressed by any finding. If all covered: "None."]

---

## DISPOSITION

**Gate vector** *(fill from GATE VECTOR TABLE above)*:
- GOpen = [copy]
- G_domain_agg = [copy]
- G_lifecycle = [copy]
- GClose = [copy]

**Apply contract §3 formula**:

```
G = {GOpen=[_], G_domain_agg=[_], G_lifecycle=[_], GClose=[_]}
GClose = FAIL? --> BLOCKED  (challenger override: null hypothesis holds)
Any other Gi = FAIL? --> BLOCKED
No FAIL, any CONDITIONAL? --> CONDITIONAL
All PASS? --> READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**Null hypothesis defeat** *(from GClose and NULL HYPOTHESIS REGISTER)*:
[DEFEATED / PARTIALLY DEFEATED / HOLDS -- one sentence.]

**Primary driver**: [One sentence. Formula completed the derivation.]

**Conditions** *(only if CONDITIONAL)*:
1. [Condition from first CONDITIONAL gate.]

**Blocker** *(only if BLOCKED)*: [Finding from FAIL gate.]

---

## ACTION ITEM REGISTER

*One row per PARTIAL or HOLDS CH-ID from BRACKET CLOSING.*

| CH-ID  | Item Description    | Disposition Class                  | Owner Role  | Resolution Criterion                             |
|--------|---------------------|------------------------------------|-------------|--------------------------------------------------|
| CH-001 | [What must be done] | [BLOCKED / CONDITIONAL / ADVISORY] | [ROLE_NAME] | [What must be true to close this]                |
| CH-002 | [Item 2]            | [BLOCKED / CONDITIONAL / ADVISORY] | [ROLE_NAME] | [Resolution criterion]                           |
| --     | [Advisory OBS]      | ADVISORY-OBS                       | [ROLE_NAME] | [Criterion]                                      |

---

**Artifact to review:**

{{artifact}}
```

---

## V-04 -- Combination: SCOPE SURFACE REGISTER + FINDING SURFACE LINKAGE TABLE

**Variation axis**: V-01 + V-02 combined.

**Hypothesis**: SCOPE SURFACE REGISTER (V-01) and FINDING SURFACE LINKAGE TABLE (V-02) address two adjacent gaps in the same traceability chain: what surfaces are in scope (§1) and whether findings cite those specific surfaces. Combined, they close the bidirectional trace: register -> §1 IN-SCOPE (top-down) and finding table surface column -> §1 surface name (bottom-up). V-05 R2 has neither; V-04 adds both without the per-finding severity formula, keeping the single strongest combination. Expected score under v3: 120 (V-05 R2 base is already 120). Expected excellence pattern activation: E-1 + E-2 simultaneously, confirming their independence.

**Changes from V-05 R2**:
- All V-01 changes: SCOPE SURFACE REGISTER before contract block; §1 IN-SCOPE references by S-ID; findings cite S-IDs
- All V-02 changes: findings tables in DOMAIN and LIFECYCLE with Surface / Role Lens columns

---

```
depth: standard
confidence: standard
for: {value}
iterations: 1

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any pre-printed
heading, label, field, formula, or structural element. Do not add sections between pre-printed
headers. If a field cannot be filled, write `[N/A -- reason]`.

---

## SCOPE SURFACE REGISTER

*Complete this register before §1 IN-SCOPE. Name each concrete surface the artifact exposes for
review. Generic descriptions ("all sections", "the full document", "all fields", "entire spec",
"all content") are not acceptable -- they prevent surface-specific finding linkage.
Each surface must be nameable as a specific section heading, interface contract, behavioral
claim, schema component, or named protocol.*

| S-ID  | Surface Name                                                               | Why In Scope                                                     | Primary Lens                  |
|-------|----------------------------------------------------------------------------|------------------------------------------------------------------|-------------------------------|
| S-001 | [Specific section, interface, or behavioral claim -- not "all sections"]   | [One sentence]                                                   | [DOMAIN / LIFECYCLE / either] |
| S-002 | [Another specific surface -- not "all fields" or "the document"]           | [One sentence]                                                   | [DOMAIN / LIFECYCLE / either] |
| S-003 | [Optional -- each row must name a discrete, reviewable surface]            | [One sentence]                                                   | [DOMAIN / LIFECYCLE / either] |

*S-IDs carry to §1 IN-SCOPE and to the In-Scope Surface column of every findings table.
A finding that cannot cite a registered S-ID is out-of-scope and must not appear.*

---

======================================================================
DISPOSITION_CONTRACT v1
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§5;
reviewer sections may not execute until §1 COMPLETE marker is reached]
======================================================================

§1 -- SCOPE ENUMERATION
[Copy from SCOPE SURFACE REGISTER above by S-ID and name. Do not add surfaces not in the
register. Do not substitute generic descriptions for S-ID values.]

IN-SCOPE -- surfaces this review will evaluate (from SCOPE SURFACE REGISTER -- S-ID and name
by copy; generic substitutes violate this contract):
  1. [S-001: copy name from register]
  2. [S-002: copy name from register]
  3. [S-003: copy if active]

OUT-OF-SCOPE -- surfaces this review will not evaluate:
  1. [SURFACE -- REASON_EXCLUDED]
  (Write "None" if nothing is excluded.)

Scope Amendment Protocol:
  SCOPE AMENDMENT: [surface] added to IN-SCOPE -- [reason]
  Silent scope expansion violates this contract.

§1 COMPLETE -- role selection and reviewer gates proceed below.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH   = Blocks commitment. No commitment proceeds with open HIGH findings.
  MEDIUM = Conditions commitment. Proceeds only after named resolution.
  LOW    = Advisory. Commitment may proceed.
  These definitions apply universally. They may not be restated at any gate.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE -- evaluated at DISPOSITION section]
  G = {GOpen, G_domain_agg, G_lifecycle, GClose}
  BLOCKED      <-- GClose = FAIL  [override: null hypothesis holds]
                OR  exists Gi = FAIL
  CONDITIONAL  <-- no Gi = FAIL  AND  exists Gi = CONDITIONAL
  READY        <-- all Gi = PASS

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"
  A missing cite is an audit-trail gap.

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Each challenge claim in BRACKET OPENING receives a CH-ID (CH-001, CH-002, ...).
  CH-ID COUNT: N = the number of CH-IDs declared in BRACKET OPENING. Record N
    in the "CH-ID Count declared" field immediately after the Challenge Claims table.
  Every downstream CH-ID table must contain exactly N rows -- one row per declared CH-ID.
    A table with fewer than N rows is a §5 count violation regardless of other completeness.
    A table with more than N rows invents claims not in evidence -- also a §5 violation.
  A PASS verdict is prohibited if any CH-ID row shows OPEN status.

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================

---

## ROLE MANIFEST

Read `.roles/signal/`. Assign each slot.

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (bracket open + close -- fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |

*Execution order: BRACKET OPENING -> LIFECYCLE -> DOMAIN -> BRACKET CLOSING.*
*(For `--depth deep`: add DOMAIN-2, DOMAIN-3, etc.)*

---

## NULL HYPOTHESIS REGISTER

*Complete before BRACKET OPENING. Name the concrete alternative the team uses today.
Generic phrases ("do nothing", "status quo") are not acceptable.*

| Field | Value |
|-------|-------|
| What teams use today | [Specific tool, process, or workaround] |
| Why it works well enough | [One sentence] |
| Where it breaks down | [One sentence] |
| Switching cost | [HIGH / MEDIUM / LOW] |
| Null hypothesis strength | [HIGH / MEDIUM / LOW] |

*This register is the source of truth for all null hypothesis fields in this review.*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis** *(from NULL HYPOTHESIS REGISTER -- name the specific tool or process)*:
[One sentence. Do not substitute generic language.]

**Null hypothesis strength**: [Copy from NULL HYPOTHESIS REGISTER]

**Challenge claims** *(assign CH-IDs; carry to every downstream section per contract §5)*:

| CH-ID  | Challenge Claim                                                                        | Severity              |
|--------|----------------------------------------------------------------------------------------|-----------------------|
| CH-001 | [CLAIM_1 -- switching cost, workaround viability, or adoption friction. One sentence.] | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2]                                                                              | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional]                                                                  | [HIGH / MEDIUM / LOW] |

**CH-ID Count declared**: N = [count rows above -- every downstream CH-ID table must have exactly N rows]

**Verify Question**: [One from challenger's `lens.verify`.]
**Simplify**: [One from challenger's `lens.simplify`.]
**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]

*GOpen and all N CH-IDs carry forward. Execution: LIFECYCLE -> DOMAIN -> BRACKET CLOSING.*

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]
*(DOMAIN has not yet run. Assess commitment readiness from GOpen alone.)*

**CH-ID Verdict Preview**:

| CH-ID  | Status                         |
|--------|--------------------------------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN]   |
| CH-002 | [ADDRESSED / PARTIAL / OPEN]   |
| CH-003 | [omit if not active]           |

**CH-ID Response Table** *(exactly N rows)*:

| CH-ID  | Challenge Claim (copy) | Commitment-Frame Response | Status                       |
|--------|------------------------|--------------------------|------------------------------|
| CH-001 | [copy]                 | [RESPONSE_1]             | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]                 | [RESPONSE_2]             | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active]       | [RESPONSE_3]             | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [One paragraph referencing GOpen explicitly.]

**Null hypothesis status** *(reference NULL HYPOTHESIS REGISTER)*:
Given GOpen, the null hypothesis -- [specific tool/process] -- is: [STILL VIABLE / CHALLENGED / OPEN].
Justification: [one sentence.]

**Additional Findings** *(structured table -- In-Scope Surface must match a §1 surface exactly,
or cite S-ID from SCOPE SURFACE REGISTER; Role Lens must name a specific lens.verify entry;
generic surface "the document" or "all sections" is not a §1 surface)*:

| # | Finding | In-Scope Surface (S-ID: name from §1) | Role Lens (lens.verify entry) | Severity              |
|---|---------|---------------------------------------|-------------------------------|-----------------------|
| 1 | [FINDING_1 -- commitment/program concern] | [S-00X: surface name] | [Named entry] | [HIGH / MEDIUM / LOW] |
| 2 | [FINDING_2] | [S-00X: surface name] | [Named entry] | [HIGH / MEDIUM / LOW] |

**Severity**: [HIGH / MEDIUM / LOW per contract §2]
**Recommendation**: [One concrete action.]
**Verify Question**: [One from this role's `lens.verify`.]
**Simplify**: [One from this role's `lens.simplify`.]

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
**G_lifecycle Reason**: [One sentence.]

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]
Received G_lifecycle: [copy]

**CH-ID Verdict Preview** *(convergence anchor vs LIFECYCLE preview)*:

| CH-ID  | Status                         |
|--------|--------------------------------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN]   |
| CH-002 | [ADDRESSED / PARTIAL / OPEN]   |
| CH-003 | [omit if not active]           |

**CH-ID Response Table** *(exactly N rows -- PASS prohibited if any row = OPEN)*:

| CH-ID  | Challenge Claim (copy)                 | Technical Response | Status                       |
|--------|----------------------------------------|--------------------|------------------------------|
| CH-001 | [copy full claim from BRACKET OPENING] | [RESPONSE_1]       | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]                                 | [RESPONSE_2]       | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active]                       | [RESPONSE_3]       | [ADDRESSED / PARTIAL / OPEN] |

**Additional Findings** *(structured table -- In-Scope Surface must match a §1 surface exactly,
or cite S-ID from SCOPE SURFACE REGISTER; Role Lens must name a specific lens.verify entry;
a finding citing no §1 surface is out-of-scope)*:

| # | Finding | In-Scope Surface (S-ID: name from §1) | Role Lens (lens.verify entry) | Severity              |
|---|---------|---------------------------------------|-------------------------------|-----------------------|
| 1 | [FINDING_1 -- technical concern, role-grounded] | [S-00X: surface name] | [Named entry] | [HIGH / MEDIUM / LOW] |
| 2 | [FINDING_2] | [S-00X: surface name] | [Named entry] | [HIGH / MEDIUM / LOW] |
| 3 | [FINDING_3 -- optional] | [S-00X: surface name] | [Named entry] | [HIGH / MEDIUM / LOW] |
| 4 | [FINDING_4 -- optional] | [S-00X: surface name] | [Named entry] | [HIGH / MEDIUM / LOW] |

*(C-10 check: >= 2 of 3 findings must name different S-IDs and different lens.verify entries.)*

**Severity**: [HIGH / MEDIUM / LOW per contract §2]
**Recommendation**: [One concrete action.]
**Verify Question**: [One from this role's `lens.verify`.]
**Simplify**: [One from this role's `lens.simplify`.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]
**G_domain Aggregate**: [PASS / CONDITIONAL / FAIL -- worst among all DOMAIN rows]

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**CH-ID Cross-Gate Tally** *(from LIFECYCLE and DOMAIN Verdict Preview)*:

| CH-ID  | LIFECYCLE Status              | DOMAIN Status              | Converged? |
|--------|-------------------------------|----------------------------|------------|
| CH-001 | [copy from LIFECYCLE preview] | [copy from DOMAIN preview] | [yes / no] |
| CH-002 | [copy]                        | [copy]                     | [yes / no] |
| CH-003 | [copy if active]              | [copy if active]           | [yes / no] |

**CH-ID Final Assessment** *(exactly N rows)*:

| CH-ID  | G_lifecycle Status      | G_domain Status    | Final Status                 | Notes               |
|--------|------------------------|--------------------|------------------------------|---------------------|
| CH-001 | [copy from LIFECYCLE]  | [copy from DOMAIN] | [DEFEATED / PARTIAL / HOLDS] | [ONE_SENTENCE_NOTE] |
| CH-002 | [copy]                 | [copy]             | [DEFEATED / PARTIAL / HOLDS] | [note]              |
| CH-003 | [copy if active]       | [copy]             | [DEFEATED / PARTIAL / HOLDS] | [note]              |

**Remaining gaps**: [If none: "None -- all CH-IDs DEFEATED."]
**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**GClose override authority**: GClose = FAIL overrides all prior gates per §3.
**GClose Rationale**: [2-3 sentences referencing NULL HYPOTHESIS REGISTER tool/process.]

---

## GATE VECTOR TABLE

| Gate                         | Reviewer          | Verdict                     | Contract Cite           |
|------------------------------|-------------------|-----------------------------|-------------------------|
| GOpen -- bracket opening     | [CHALLENGER_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_lifecycle -- lifecycle     | [LIFECYCLE_ROLE]  | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_domain -- domain aggregate | [DOMAIN_ROLE(S)]  | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| GClose -- bracket closing    | [CHALLENGER_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Convergence** *(scan CH-ID Cross-Gate Tally -- rows where Converged = yes)*:

**Conflicts**: [Incompatible responses or findings. If none: "None detected."]

**Scope coverage** *(scan SCOPE SURFACE REGISTER S-IDs against all findings tables -- any S-ID
not cited in any finding is a coverage gap; list by S-ID and name)*:
[S-00X: [name] -- no reviewer cited. OR "None -- all registered surfaces cited."]

---

## DISPOSITION

**Gate vector**:
- GOpen = [copy]
- G_domain_agg = [copy]
- G_lifecycle = [copy]
- GClose = [copy]

**Apply contract §3 formula**:

```
G = {GOpen=[_], G_domain_agg=[_], G_lifecycle=[_], GClose=[_]}
GClose = FAIL? --> BLOCKED
Any other Gi = FAIL? --> BLOCKED
No FAIL, any CONDITIONAL? --> CONDITIONAL
All PASS? --> READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**Null hypothesis defeat**: [DEFEATED / PARTIALLY DEFEATED / HOLDS -- one sentence.]

**Primary driver**: [One sentence -- formula derivation, not finding reasoning.]

**Conditions** *(only if CONDITIONAL)*: 1. [condition]

**Blocker** *(only if BLOCKED)*: [finding from FAIL gate]

---

## ACTION ITEM REGISTER

| CH-ID  | Item Description    | Disposition Class                  | Owner Role  | Resolution Criterion                      |
|--------|---------------------|------------------------------------|-------------|-------------------------------------------|
| CH-001 | [What must be done] | [BLOCKED / CONDITIONAL / ADVISORY] | [ROLE_NAME] | [What must be true to close]              |
| CH-002 | [Item 2]            | [BLOCKED / CONDITIONAL / ADVISORY] | [ROLE_NAME] | [Resolution criterion]                    |
| --     | [Advisory OBS]      | ADVISORY-OBS                       | [ROLE_NAME] | [Criterion]                               |

---

**Artifact to review:**

{{artifact}}
```

---

## V-05 -- Full Integration: SCOPE REGISTER + FINDING TABLE + PER-FINDING SEVERITY

**Variation axis**: All three Round 3 axes applied simultaneously.

**Hypothesis**: V-01 (SCOPE SURFACE REGISTER), V-02 (FINDING SURFACE LINKAGE TABLE), and V-03 (PER-FINDING SEVERITY AGGREGATION) are structurally orthogonal and non-interfering: the register governs §1 surface population, the findings table governs finding-to-surface traceability, and the severity formula governs section severity derivation. Combining all three closes three previously execution-dependent criteria simultaneously: C-06 (scope specificity), C-10 (role-grounded findings), and the severity auditability chain. V-05 also inherits all V-05 R2 patterns (C-11, C-12, C-13, C-14). Under v3 rubric this is still 120 (ceiling); expected to activate E-1 + E-2 + E-3 (candidates C-15/C-16/C-17 in v4 rubric). V-04 vs V-05 delta isolates the per-finding severity effect.

**Changes from V-05 R2**: All V-01 + V-02 + V-03 changes combined.

---

```
depth: standard
confidence: standard
for: {value}
iterations: 1

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any pre-printed
heading, label, field, formula, or structural element. Do not add sections between pre-printed
headers. If a field cannot be filled, write `[N/A -- reason]`.

---

## SCOPE SURFACE REGISTER

*Complete this register before §1 IN-SCOPE. Name each concrete surface the artifact exposes for
review. Generic descriptions ("all sections", "the full document", "all fields", "entire spec")
are not acceptable -- name specific, reviewable surfaces.
Each surface must be nameable as a specific section heading, interface contract, behavioral
claim, schema component, or named protocol.*

| S-ID  | Surface Name                                                               | Why In Scope                                                     | Primary Lens                  |
|-------|----------------------------------------------------------------------------|------------------------------------------------------------------|-------------------------------|
| S-001 | [Specific section, interface, or behavioral claim -- not "all sections"]   | [One sentence]                                                   | [DOMAIN / LIFECYCLE / either] |
| S-002 | [Another specific surface -- not "all fields" or "the document"]           | [One sentence]                                                   | [DOMAIN / LIFECYCLE / either] |
| S-003 | [Optional -- each row must name a discrete, reviewable surface]            | [One sentence]                                                   | [DOMAIN / LIFECYCLE / either] |

*S-IDs carry to §1 IN-SCOPE and to the In-Scope Surface column of every findings table.
A finding that cannot cite a registered S-ID is out-of-scope and must not appear.*

---

======================================================================
DISPOSITION_CONTRACT v1
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§5;
reviewer sections may not execute until §1 COMPLETE marker is reached]
======================================================================

§1 -- SCOPE ENUMERATION
[Copy from SCOPE SURFACE REGISTER above by S-ID and name. Do not add surfaces not in the
register. Do not substitute generic descriptions.]

IN-SCOPE -- surfaces this review will evaluate (from SCOPE SURFACE REGISTER -- S-ID and name
by copy; generic substitutes violate this contract):
  1. [S-001: copy name from register]
  2. [S-002: copy name from register]
  3. [S-003: copy if active]

OUT-OF-SCOPE -- surfaces this review will not evaluate:
  1. [SURFACE -- REASON_EXCLUDED]
  (Write "None" if nothing is excluded.)

Scope Amendment Protocol:
  SCOPE AMENDMENT: [surface] added to IN-SCOPE -- [reason]
  Silent scope expansion violates this contract.

§1 COMPLETE -- role selection and reviewer gates proceed below.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH   = Blocks commitment. No commitment proceeds with open HIGH findings.
  MEDIUM = Conditions commitment. Proceeds only after named resolution.
  LOW    = Advisory. Commitment may proceed.
  These definitions apply universally. They may not be restated at any gate.

§2a -- SECTION SEVERITY FORMULA [IMMUTABLE -- applied in each reviewer section]
  Section Severity = worst(all individual finding severities in this section).
  Precedence: HIGH > MEDIUM > LOW.
  A section with at least one HIGH finding must emit Section Severity = HIGH.
  No editorial override. Show the formula result -- do not assign independently.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE -- evaluated at DISPOSITION section]
  G = {GOpen, G_domain_agg, G_lifecycle, GClose}
  BLOCKED      <-- GClose = FAIL  [override: null hypothesis holds]
                OR  exists Gi = FAIL
  CONDITIONAL  <-- no Gi = FAIL  AND  exists Gi = CONDITIONAL
  READY        <-- all Gi = PASS

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"
  A missing cite is an audit-trail gap.

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Each challenge claim in BRACKET OPENING receives a CH-ID (CH-001, CH-002, ...).
  CH-ID COUNT: N = the number of CH-IDs declared in BRACKET OPENING. Record N
    in the "CH-ID Count declared" field immediately after the Challenge Claims table.
  Every downstream CH-ID table must contain exactly N rows -- one row per declared CH-ID.
    A table with fewer than N rows is a §5 count violation regardless of other completeness.
    A table with more than N rows invents claims not in evidence -- also a §5 violation.
  A PASS verdict is prohibited if any CH-ID row shows OPEN status.

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================

---

## ROLE MANIFEST

Read `.roles/signal/`. Assign each slot.

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (bracket open + close -- fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |

*Execution order: BRACKET OPENING -> LIFECYCLE -> DOMAIN -> BRACKET CLOSING.*
*LIFECYCLE runs first to surface commitment-readiness blockers before technical depth.*
*(For `--depth deep`: add DOMAIN-2, DOMAIN-3, etc. CHALLENGER positions remain fixed.)*

---

## NULL HYPOTHESIS REGISTER

*Complete before BRACKET OPENING. Name the concrete alternative the team uses today.
Generic phrases ("do nothing", "status quo", "the current approach") are not acceptable --
name the specific tool, process, or workaround.*

| Field | Value |
|-------|-------|
| What teams use today | [Specific tool, process, or workaround the team relies on instead of building this] |
| Why it works well enough | [One sentence -- the genuine case for continuing with the status quo] |
| Where it breaks down | [One sentence -- the gap or friction that motivates this artifact] |
| Switching cost | [HIGH / MEDIUM / LOW] |
| Null hypothesis strength | [HIGH / MEDIUM / LOW -- how viable is the current approach overall?] |

*This register is the source of truth for all null hypothesis fields in this review.*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis** *(from NULL HYPOTHESIS REGISTER -- name the specific tool or process)*:
[The team continues to use [TOOL/PROCESS from Register] because [WHY IT WORKS from Register].
One sentence. Do not substitute generic language.]

**Null hypothesis strength**: [Copy from NULL HYPOTHESIS REGISTER -- HIGH / MEDIUM / LOW]

**Challenge claims** *(assign CH-IDs; carry to every downstream section per contract §5)*:

| CH-ID  | Challenge Claim                                                                        | Severity              |
|--------|----------------------------------------------------------------------------------------|-----------------------|
| CH-001 | [CLAIM_1 -- switching cost, workaround viability, or adoption friction. One sentence.] | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2]                                                                              | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional]                                                                  | [HIGH / MEDIUM / LOW] |

**CH-ID Count declared**: N = [count rows above -- every downstream CH-ID table must have exactly N rows]

**Verify Question**: [One from challenger's `lens.verify`.]
**Simplify**: [One from challenger's `lens.simplify`.]
**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]

*GOpen and all N CH-IDs carry forward. Execution: LIFECYCLE -> DOMAIN -> BRACKET CLOSING.*

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [PASS / CONDITIONAL / FAIL -- copy from BRACKET OPENING]
*(DOMAIN has not yet run. LIFECYCLE assesses commitment readiness from GOpen alone.)*

**CH-ID Verdict Preview** *(fill Status column before writing response table)*:

| CH-ID  | Status                         |
|--------|--------------------------------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN]   |
| CH-002 | [ADDRESSED / PARTIAL / OPEN]   |
| CH-003 | [ADDRESSED / PARTIAL / OPEN -- omit if not active] |

**CH-ID Response Table** *(exactly N rows -- §5 violation if count differs)*:

| CH-ID  | Challenge Claim (copy) | Commitment-Frame Response | Status                       |
|--------|------------------------|--------------------------|------------------------------|
| CH-001 | [copy]                 | [RESPONSE_1]             | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]                 | [RESPONSE_2]             | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active]       | [RESPONSE_3]             | [ADDRESSED / PARTIAL / OPEN] |

**Decision-readiness assessment**: [One paragraph referencing GOpen explicitly. G_domain not
yet available -- assess commitment readiness from challenger framing alone.]

**Null hypothesis status** *(reference NULL HYPOTHESIS REGISTER)*:
Given GOpen, the null hypothesis -- [specific tool/process from Register] -- is:
[STILL VIABLE / CHALLENGED / OPEN]. Justification: [one sentence.]

**Additional Findings** *(structured table -- In-Scope Surface must match a §1 S-ID surface
exactly; Role Lens must name a specific lens.verify entry; generic surfaces are not §1 surfaces;
each finding carries individual severity for §2a formula below)*:

| # | Finding | In-Scope Surface (S-ID: name from §1) | Role Lens (lens.verify entry) | Severity              |
|---|---------|---------------------------------------|-------------------------------|-----------------------|
| 1 | [FINDING_1 -- commitment, program, or decision concern] | [S-00X: surface name] | [Named entry] | [HIGH / MEDIUM / LOW] |
| 2 | [FINDING_2] | [S-00X: surface name] | [Named entry] | [HIGH / MEDIUM / LOW] |

**Section Severity Formula** *(apply §2a -- enumerate finding severities; derive result)*:
  Finding severities: [list from table: e.g., HIGH, MEDIUM]
  Section Severity = worst([...]) = [HIGH / MEDIUM / LOW]

**Section Severity**: [Copy formula result -- do not assign editorially. Per contract §2 + §2a.]

**Recommendation**: [One concrete action.]
**Verify Question**: [One from this role's `lens.verify`.]
**Simplify**: [One from this role's `lens.simplify`.]

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
**G_lifecycle Reason**: [One sentence. Section Severity = HIGH is a strong signal for FAIL or CONDITIONAL.]

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [PASS / CONDITIONAL / FAIL -- copy from BRACKET OPENING]
Received G_lifecycle: [PASS / CONDITIONAL / FAIL -- copy from LIFECYCLE]

**CH-ID Verdict Preview** *(fill Status column before writing response table.
Convergence anchor vs LIFECYCLE Verdict Preview above.)*:

| CH-ID  | Status                         |
|--------|--------------------------------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN]   |
| CH-002 | [ADDRESSED / PARTIAL / OPEN]   |
| CH-003 | [ADDRESSED / PARTIAL / OPEN -- omit if not active] |

**CH-ID Response Table** *(exactly N rows -- PASS prohibited if any row = OPEN)*:

| CH-ID  | Challenge Claim (copy)                 | Technical Response | Status                       |
|--------|----------------------------------------|--------------------|------------------------------|
| CH-001 | [copy full claim from BRACKET OPENING] | [RESPONSE_1]       | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]                                 | [RESPONSE_2]       | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active]                       | [RESPONSE_3]       | [ADDRESSED / PARTIAL / OPEN] |

*(PARTIAL requires a named resolution path. OPEN = claim not addressable from this role's frame.)*

**Additional Findings** *(structured table -- In-Scope Surface must match a §1 S-ID surface
exactly; Role Lens must name a specific lens.verify entry; a finding citing no §1 surface is
out-of-scope; each finding carries individual severity for §2a formula below)*:

| # | Finding | In-Scope Surface (S-ID: name from §1) | Role Lens (lens.verify entry) | Severity              |
|---|---------|---------------------------------------|-------------------------------|-----------------------|
| 1 | [FINDING_1 -- technical concern grounded in role expertise] | [S-00X: surface name] | [Named entry] | [HIGH / MEDIUM / LOW] |
| 2 | [FINDING_2] | [S-00X: surface name] | [Named entry] | [HIGH / MEDIUM / LOW] |
| 3 | [FINDING_3 -- optional] | [S-00X: surface name] | [Named entry] | [HIGH / MEDIUM / LOW] |
| 4 | [FINDING_4 -- optional] | [S-00X: surface name] | [Named entry] | [HIGH / MEDIUM / LOW] |

*(C-10 check: >= 2 of 3 findings must name different S-IDs and different lens.verify entries.)*

**Section Severity Formula** *(apply §2a -- enumerate finding severities; derive result)*:
  Finding severities: [list from table: e.g., HIGH, MEDIUM, LOW, LOW]
  Section Severity = worst([...]) = [HIGH / MEDIUM / LOW]

**Section Severity**: [Copy formula result -- do not assign editorially. Per contract §2 + §2a.]
*Do not copy GOpen or G_lifecycle severity.*

**Recommendation**: [One concrete action.]
**Verify Question**: [One from this role's `lens.verify`.]
**Simplify**: [One from this role's `lens.simplify`.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence. Section Severity = HIGH is a strong signal for FAIL or CONDITIONAL.]

*(For `--depth deep`: repeat labeled DOMAIN-2, DOMAIN-3. G_domain Aggregate = worst verdict.)*

**G_domain Aggregate**: [PASS / CONDITIONAL / FAIL -- worst among all DOMAIN rows]

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1
*Full record received: scope declaration, all CH-ID tables, all gate verdicts.*

**CH-ID Cross-Gate Tally** *(copy from LIFECYCLE and DOMAIN Verdict Preview tables)*:

| CH-ID  | LIFECYCLE Status              | DOMAIN Status              | Converged? |
|--------|-------------------------------|----------------------------|------------|
| CH-001 | [copy from LIFECYCLE preview] | [copy from DOMAIN preview] | [yes / no] |
| CH-002 | [copy]                        | [copy]                     | [yes / no] |
| CH-003 | [copy if active]              | [copy if active]           | [yes / no] |

**CH-ID Final Assessment** *(exactly N rows)*:

| CH-ID  | G_lifecycle Status      | G_domain Status    | Final Status                 | Notes               |
|--------|------------------------|--------------------|------------------------------|---------------------|
| CH-001 | [copy from LIFECYCLE]  | [copy from DOMAIN] | [DEFEATED / PARTIAL / HOLDS] | [ONE_SENTENCE_NOTE] |
| CH-002 | [copy]                 | [copy]             | [DEFEATED / PARTIAL / HOLDS] | [note]              |
| CH-003 | [copy if active]       | [copy]             | [DEFEATED / PARTIAL / HOLDS] | [note]              |

**Remaining gaps**: [If none: "None -- all CH-IDs DEFEATED."]

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
- PASS (= DEFEATED): All CH-IDs DEFEATED.
- CONDITIONAL (= PARTIAL): Some CH-IDs PARTIAL -- name them.
- FAIL (= HOLDS): At least one CH-ID HOLDS.

**GClose override authority**: GClose = FAIL overrides all prior gates per §3.

**GClose Rationale**: [2-3 sentences. Reference the specific tool/process from NULL HYPOTHESIS
REGISTER when stating whether it has been defeated.]

---

## GATE VECTOR TABLE

*(Execution order: GOpen -> G_lifecycle -> G_domain -> GClose. §3 operates on the set.)*

| Gate                         | Reviewer          | Verdict                     | Contract Cite           |
|------------------------------|-------------------|-----------------------------|-------------------------|
| GOpen -- bracket opening     | [CHALLENGER_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_lifecycle -- lifecycle     | [LIFECYCLE_ROLE]  | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| G_domain -- domain aggregate | [DOMAIN_ROLE(S)]  | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |
| GClose -- bracket closing    | [CHALLENGER_ROLE] | [PASS / CONDITIONAL / FAIL] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Convergence** *(scan CH-ID Cross-Gate Tally -- rows where Converged = yes; name each by CH-ID)*:

**Conflicts**: [Incompatible responses or findings. If none: "None detected."]

**Scope coverage** *(scan SCOPE SURFACE REGISTER S-IDs against all findings tables -- any S-ID
not cited in any finding is a coverage gap; list by S-ID and name)*:
[S-00X: [name] -- not cited by any reviewer. OR "None -- all registered surfaces cited."]

---

## DISPOSITION

**Gate vector**:
- GOpen = [copy]
- G_domain_agg = [copy]
- G_lifecycle = [copy]
- GClose = [copy]

**Apply contract §3 formula**:

```
G = {GOpen=[_], G_domain_agg=[_], G_lifecycle=[_], GClose=[_]}
GClose = FAIL? --> BLOCKED  (challenger override: null hypothesis holds)
Any other Gi = FAIL? --> BLOCKED
No FAIL, any CONDITIONAL? --> CONDITIONAL
All PASS? --> READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**Null hypothesis defeat** *(from GClose verdict and NULL HYPOTHESIS REGISTER)*:
[DEFEATED / PARTIALLY DEFEATED / HOLDS -- one sentence. If GClose = FAIL: "HOLDS -- [specific
tool/process from Register] remains the team's viable alternative: [GClose Rationale summary]."]

**Primary driver**: [One sentence. Formula completed the derivation -- do not re-reason from findings.]

**Conditions** *(only if CONDITIONAL)*:
1. [Condition from first CONDITIONAL gate. Resolution order: GOpen -> G_lifecycle -> G_domain -> GClose.]
2. [Additional conditions.]

**Blocker** *(only if BLOCKED)*: [Finding from FAIL gate.]

---

## ACTION ITEM REGISTER

*One row per PARTIAL or HOLDS CH-ID from BRACKET CLOSING. Items not sourced from a CH-ID:
mark ADVISORY-OBS. This register is the CH-ID-indexed synthesis artifact per contract §5.*

| CH-ID  | Item Description    | Disposition Class                  | Owner Role  | Resolution Criterion                             |
|--------|---------------------|------------------------------------|-------------|--------------------------------------------------|
| CH-001 | [What must be done] | [BLOCKED / CONDITIONAL / ADVISORY] | [ROLE_NAME] | [What must be true to close this]                |
| CH-002 | [Item 2]            | [BLOCKED / CONDITIONAL / ADVISORY] | [ROLE_NAME] | [Resolution criterion]                           |
| --     | [Advisory OBS]      | ADVISORY-OBS                       | [ROLE_NAME] | [Criterion]                                      |

*Every row traces: BRACKET OPENING CH-ID -> reviewer CH-ID tables -> BRACKET CLOSING final status.*

---

**Artifact to review:**

{{artifact}}
```

---

## Variation Summary

| Variation | SCOPE REGISTER (E-1) | FINDING TABLE (E-2) | SEVERITY FORMULA (E-3) | Inherited from V-05 R2 |
|-----------|---------------------|--------------------|-----------------------|------------------------|
| V-01 | YES | -- | -- | C-11, C-12, C-13, C-14 |
| V-02 | -- | YES | -- | C-11, C-12, C-13, C-14 |
| V-03 | -- | -- | YES (§2a + formula block) | C-11, C-12, C-13, C-14 |
| V-04 | YES | YES | -- | C-11, C-12, C-13, C-14 |
| V-05 | YES | YES | YES | C-11, C-12, C-13, C-14 |

**All variants score 120/120 under v3 rubric from base inheritance.**

**New excellence patterns targeted (v4 rubric candidates)**:

| ID | Source | What it tests | Detectable at template level? |
|----|--------|---------------|-------------------------------|
| E-1 | V-01 SCOPE SURFACE REGISTER | C-06 scope specificity elevated to template-determined via register+prohibition+S-ID downstream reference | YES -- §1 IN-SCOPE field references S-IDs; generic descriptions visible at fill time |
| E-2 | V-02 FINDING SURFACE LINKAGE TABLE | C-10 role-grounded findings elevated to template-determined via structured table with Surface and Role Lens columns | YES -- finding without §1 surface S-ID is a table cell violation, not a scoring inference |
| E-3 | V-03 PER-FINDING SEVERITY FORMULA | New auditability chain: finding -> individual severity -> §2a formula -> section severity -> gate influence | YES -- formula result is required cell; editorial assignment produces formula mismatch |

**Hypotheses to isolate via execution comparison**:
- E-1 isolated: V-01 vs baseline (V-05 R2 without scope register)
- E-2 isolated: V-02 vs baseline
- E-3 isolated: V-03 vs baseline
- E-1 + E-2 combined: V-04 vs V-01 and V-02 individually
- E-1 + E-2 + E-3 combined: V-05 vs V-04 (isolates E-3 in the full stack)

**Predicted v4 rubric score order**:
1. V-05 -- all three excellence patterns active; highest composite if v4 adds C-15/C-16/C-17
2. V-04 -- E-1 + E-2; C-17 (severity formula) absent
3. V-02 -- E-2 alone; scope and severity gaps present
4. V-01 -- E-1 alone; finding table and severity gaps present
5. V-03 -- E-3 alone; scope register and finding table gaps present
