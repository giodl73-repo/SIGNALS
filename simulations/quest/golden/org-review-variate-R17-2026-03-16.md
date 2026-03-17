---
skill: quest-variate
skill_target: org-review
date: 2026-03-16
round: 17
rubric: org-review-rubric-v11-2026-03-16.md
---

# org-review -- Variate Round 17 (v11 rubric Round 5)

Generated: 2026-03-16
Skill: org-review
Rubric: simulations/quest/rubrics/org-review-rubric-v11-2026-03-16.md

## Prior round summary

- R1--R11: V-05 climbed to 210/225 via bracket architecture, local ledger, CH-ID tracing,
  per-finding severity aggregation (§14/C-30), lens exhaustion protocol (§15/C-31),
  primary driver derivation (§16/C-32). V-05 R11 is the baseline: 210/225.
- R12: V-02 R12 scored ~215/225 -- C-33+C-34+C-35 PASS simultaneously but WITHOUT
  C-30+C-31+C-32 (§14/§15/§16 absent). Canonical source for C-33/C-34/C-35.
- R13--R14: Explored placement of C-33 (lens applicability) and C-35 (NH dimension table).
- R16 (= v11 Round 4): V-01 §17 ROLE MANIFEST APPLICABILITY (C-33); V-02 §17 PRE-REVIEW
  DOMAIN COVERAGE GAP-CHECK (C-34); V-03 NH DIMENSION TABLE (C-35); V-05 = full
  integration of §17+§18+§19 (225/225 candidate).

## Round 17 (v11 Round 5) strategy

Baseline: V-05 R16 (§1-§16 + §17 manifest applicability + §18 pre-review gap-check +
§19 NH dimension table) as structural foundation.

Identified failure modes in R16 V-05:
- C-33: Model fills Applicability column in ROLE MANIFEST without per-artifact justification.
  Rating reflects generic role capability rather than artifact-specific assessment.
- C-34: Domain gap-check references domain labels from §1 annotations but domains may not
  be annotated consistently, making the gap-check incomplete.
- C-35: NH dimension table present but g_null derivation formula not applied mechanically --
  model uses table as context for a narrative verdict, not as the sole derivation input.

Round 17 targets mechanical verifiability: each criterion must be derivable from structured
output alone, without reading prose.

- V-01: Single axis -- Phrasing register. §17a APPLICABILITY CERTIFICATION REQUIREMENT
  added after ROLE MANIFEST. Requires one-sentence per-artifact justification for each
  applicability rating. Justification must name the artifact domain and the specific
  lens.verify entry it maps to. Makes C-33 artifact-specific by construction.
- V-02: Single axis -- Output format. §17 DOMAIN-ROLE COVERAGE MATRIX replaces the
  gap-check approach. Rows = artifact domains (from §1), columns = selected roles,
  cells = applicability tier. Domain gaps visible from matrix structure without narrative.
  Makes C-34 a visual fact rather than a derived conclusion.
- V-03: Single axis -- Role sequence. §17 CHALLENGER PRE-ASSESSMENT extracted as a
  standalone section before BRACKET OPENING. NH DIMENSION TABLE runs in PRE-ASSESSMENT
  with a VERDICT column (FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD per dimension).
  g_null(initial) derives mechanically from VERDICT counts via pre-committed formula.
  BRACKET OPENING inherits g_null(initial) from PRE-ASSESSMENT. Makes C-35 verifiable
  from VERDICT column counts alone.
- V-04: Two axes -- V-01 + V-02 (certification step + coverage matrix). C-33+C-34 target.
- V-05: Three axes -- V-01 + V-02 + V-03 plus post-render criterion check. 225/225 target.

---

## V-01

**Axis**: Phrasing register -- §17a APPLICABILITY CERTIFICATION REQUIREMENT
**Hypothesis**: R16 V-01 pre-commits applicability ratings in the ROLE MANIFEST table
(Applicability column = HIGH/MEDIUM/LOW). The weakness: the model fills the column
mechanically without being required to justify the rating against the specific artifact.
A role rated HIGH because "it is a technical role and this is a technical artifact" satisfies
the column letter but not the C-33 spirit -- C-33 requires the rating to be artifact-specific,
not generic. V-01 adds §17a APPLICABILITY CERTIFICATION REQUIREMENT: after filling the ROLE
MANIFEST table, the model emits an APPLICABILITY CERTIFICATION BLOCK with one sentence per
role per applicability rating. The sentence must name (1) the specific artifact domain being
rated and (2) the specific lens.verify entry from that role's definition that applies to it.
"Generic" justifications ("this role is relevant to this artifact type") are invalid and
must be revised to name an artifact-specific domain. The certification is structural evidence
that applicability ratings are artifact-derived, not capability-derived. This makes C-33
mechanically verifiable: a scorer reads the certification block and checks whether the
justification names a specific domain + specific lens entry.

---

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .craft/roles/signal/
```

Emit this block first. Fill in injected values.

```
## Review Parameters
Artifact:     {{artifact_id}}
Depth:        {{depth}}
Reviewer set: {{reviewer_set}}
```

---

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any
pre-printed heading, label, field, formula, or structural element. Do not add sections
between pre-printed headers. If a field cannot be filled, write `[N/A -- reason]`.

---

```
======================================================================
DISPOSITION_CONTRACT v1
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§17a;
reviewer sections may not execute until §1 COMPLETE and §17a CERTIFICATION
COMPLETE markers are both reached]
======================================================================

§1 -- SCOPE ENUMERATION
[Fill this section before proceeding. This is the pre-reviewer gate.]

IN-SCOPE -- surfaces this review will evaluate:
  1. [SURFACE_1]   [DOMAIN: domain-label]
  2. [SURFACE_2]   [DOMAIN: domain-label]
  3. [SURFACE_3]   [DOMAIN: domain-label]
  (Add rows. Be exhaustive. Domain labels are used in §17a certification and §10 reconciliation.)

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

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  G = {GOpen, G_domain_agg, G_lifecycle, GClose}
  BLOCKED      <-- GClose = FAIL  [override: null hypothesis holds]
                OR  exists Gi = FAIL
  CONDITIONAL  <-- no Gi = FAIL  AND  exists Gi = CONDITIONAL
  READY        <-- all Gi = PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst verdict among all G_domain rows.
  Precedence: FAIL > CONDITIONAL > PASS.
  Single domain reviewer: G_domain_agg = G_domain (direct pass-through).
  Multiple domain reviewers: G_domain_agg = worst(G_domain_1, ..., G_domain_n).
  BRACKET CLOSING applies this formula mechanically. No editorial re-assessment.

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"
  A missing cite is an audit-trail gap.

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Each challenge claim in BRACKET OPENING receives a CH-ID (CH-001, ...).
  Every downstream section carries a mandatory CH-ID response table.
  A PASS verdict is prohibited if any CH-ID row shows OPEN status.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  (a) Row syntax: | Section | Gate | Verdict | Class |
      Class derives from verdict: FAIL -> BLOCKED; CONDITIONAL -> CONDITIONAL; PASS -> ADVISORY.
  (b) Emission timing: end of each verdict-emitting section, after verdict is stated.
  (c) Assembly: ACTION ITEM REGISTER copies local rows verbatim. Do not re-derive Gate Verdict
      or Class. The register is a copy, not a synthesis.
  EXCLUDED SECTIONS (emit NO ledger row):
    §3.5 Domain-Aggregate Checkpoint: aggregation only. No row.
    §3.8 CH-ID Saturation Check: coverage verification only. No row.
    §5.5 Scope Coverage Reconciliation: informational only. No row.
    APPLICABILITY CERTIFICATION BLOCK: pre-execution certification. No row.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  Canonical execution sequence:
    1.   ROLE MANIFEST
    1.5. APPLICABILITY CERTIFICATION BLOCK     [per §17a; pre-reviewer; no ledger row]
    2.   BRACKET OPENING
    3.   DOMAIN(s)
    3.5. DOMAIN-AGGREGATE CHECKPOINT          [excluded from gate ledger per §6]
    3.8. CH-ID SATURATION CHECK               [excluded from gate ledger per §6]
    4.   LIFECYCLE
    5.   BRACKET CLOSING
    5.5. SCOPE COVERAGE RECONCILIATION        [excluded from gate ledger per §6]
    6.   GATE VECTOR TABLE
    7.   CROSS-ROLE SIGNALS
    8.   DISPOSITION
    9.   ACTION ITEM REGISTER
  Reordering any section violates this contract.
  APPLICABILITY CERTIFICATION BLOCK must precede BRACKET OPENING.
  LIFECYCLE must precede BRACKET CLOSING.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  Before LIFECYCLE executes, each CH-ID must satisfy:
    SATURATED:       CH-ID has a response in >= 1 DOMAIN section.
  Before BRACKET CLOSING executes, each CH-ID must satisfy:
    FULLY SATURATED: CH-ID has a response in >= 1 DOMAIN section AND in the LIFECYCLE section.
  A PASS verdict from BRACKET CLOSING is prohibited when any CH-ID is not FULLY SATURATED
  without a stated saturation waiver.
  Saturation waiver format: "CH-XXX WAIVER: [LIFECYCLE not applicable -- one sentence reason]"

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1 -- g_null(initial) [emitted at BRACKET OPENING]:
    g_null(initial) = GOpen verdict directly.
  Stage 2 -- g_null(post-domain) [emitted at §3.5]:
    if G_domain_agg = FAIL:        g_null(post-domain) = FAIL
    if G_domain_agg = CONDITIONAL: g_null(post-domain) = max(g_null(initial), CONDITIONAL)
    if G_domain_agg = PASS:        g_null(post-domain) = g_null(initial)
  Stage 3 -- g_null(final) [emitted at BRACKET CLOSING]:
    if G_lifecycle = FAIL:         g_null(final) = FAIL
    if G_lifecycle = CONDITIONAL:  g_null(final) = max(g_null(post-domain), CONDITIONAL)
    if G_lifecycle = PASS:         g_null(final) = g_null(post-domain)
  GClose verdict must equal g_null(final) unless override invoked with explicit justification.

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  After BRACKET CLOSING, §5.5 SCOPE COVERAGE RECONCILIATION maps each §1 IN-SCOPE surface
  to the reviewer(s) that addressed it. COVERED / GAP classification.
  GAP surfaces -> forced LOW advisory, ADVISORY-GAP items in ACTION ITEM REGISTER.
  Gate signal (informational -- does not feed §3): COVERED / PARTIAL.

§11 -- FINDING-SURFACE LINKAGE REQUIREMENT [IMMUTABLE]
  Each finding produced by a DOMAIN or LIFECYCLE section must carry a §1 surface citation:
  "[§1:S-n] finding text". Findings without a valid §1 citation are ADVISORY-ORPHAN.

§12 -- CONDITIONAL RESOLUTION REGISTRY CONTRACT [IMMUTABLE]
  When DISPOSITION = CONDITIONAL, emit a RESOLUTION REGISTRY table after Overall Disposition:
    | Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status |
  One row per CONDITIONAL gate.

§13 -- g_null PROGRESSION LEDGER REQUIREMENT [IMMUTABLE]
  In CROSS-ROLE SIGNALS, emit:
    g_null(initial) | g_null(post-domain) | g_null(final) | Trajectory label
  Trajectory labels: MONOTONIC-PASS / MONOTONIC-FAIL / DOMAIN-DEGRADED /
  LIFECYCLE-DEGRADED / DOMAIN-RECOVERED / LIFECYCLE-RECOVERED.

§14 -- FINDING SEVERITY AGGREGATION CONTRACT [IMMUTABLE]
  Within each DOMAIN and LIFECYCLE reviewer section, each finding row carries individual
  Severity. Additional Findings table format:
    | # | §1 Surface | Finding | Severity |
  Section Severity = worst(all finding severities in this section). Precedence: HIGH > MEDIUM > LOW.
  Do not assign Section Severity editorially.

§15 -- LENS EXHAUSTION REQUIREMENT [IMMUTABLE]
  Each DOMAIN and LIFECYCLE reviewer section emits a LENS COVERAGE TABLE after Additional Findings:
    | # | lens.verify Entry | Applicability | Status | Finding Reference |
  Applicability column: populated from §17 ROLE MANIFEST pre-committed rating for this role.
  OPEN entries on HIGH-applicability rows are ADVISORY-OPEN-LENS in ACTION ITEM REGISTER.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  In DISPOSITION, Primary Driver derives mechanically:
    If GClose = FAIL:             Primary Driver = GClose (challenger override active)
    Else if any G_domain_i = FAIL: Primary Driver = DOMAIN (domain blocked)
    Else if G_lifecycle = FAIL:    Primary Driver = LIFECYCLE
    Else if any gate = CONDITIONAL: Primary Driver = lowest-index CONDITIONAL gate
    Else:                          Primary Driver = N/A (all PASS)

§17 -- ROLE MANIFEST APPLICABILITY PROTOCOL [IMMUTABLE]
  The ROLE MANIFEST table includes an Applicability column for each role row.
  Applicability is an artifact-specific rating (HIGH / MEDIUM / LOW) committed before
  any reviewer executes. It reflects how relevant this role's lens is to THIS artifact's
  domains and subject matter.
  Rating semantics:
    HIGH   = This role's lens.verify entries directly address this artifact's primary domains.
    MEDIUM = This role's lens.verify entries partially address this artifact's domains.
    LOW    = This role's lens.verify entries have limited applicability to this artifact.
  The LENS COVERAGE TABLE (§15) inherits the role's applicability rating from this manifest.

§17a -- APPLICABILITY CERTIFICATION REQUIREMENT [IMMUTABLE]
  After the ROLE MANIFEST is filled, before BRACKET OPENING, emit an APPLICABILITY
  CERTIFICATION BLOCK. The block contains one certification entry per selected role.

  Certification entry format:
    Role [role-name]: Applicability = [HIGH/MEDIUM/LOW]
    Artifact domain: [name one §1 domain label that this rating is based on]
    Lens.verify match: [quote or paraphrase one specific lens.verify entry from this role's
    definition that directly addresses the named artifact domain]
    Basis: [one sentence explaining why this lens entry makes this role HIGH/MEDIUM/LOW
    relevant to THIS artifact specifically -- not to the artifact type in general]

  Invalid certification:
    "This role is relevant because this is a [type] artifact" -- GENERIC, must be revised.
    "This role covers [domain]" without citing a specific lens.verify entry -- INCOMPLETE.

  A role whose certification cannot name a specific lens.verify entry matching a specific
  artifact domain must have its Applicability rating downgraded to LOW.

  The APPLICABILITY CERTIFICATION BLOCK is structural evidence that ratings are
  artifact-derived. It is produced at step 1.5 in the §7 section order.

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================
```

---

## ROLE MANIFEST

Read `.craft/roles/signal/`. Assign each slot.

| Slot | Archetype | Role | Selection Rationale | Applicability |
|------|-----------|------|---------------------|---------------|
| CHALLENGER (bracket open + close -- fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] | HIGH -- challenger is universally applicable |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] | [HIGH / MEDIUM / LOW] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] | [HIGH / MEDIUM / LOW] |

*(For `--depth deep`: add DOMAIN-2, DOMAIN-3 rows. Each carries its Applicability rating.)*

---

## APPLICABILITY CERTIFICATION BLOCK

*(Per §17a -- produced before BRACKET OPENING. No gate ledger row per §6.)*

Role [challenger role name]: Applicability = HIGH
Artifact domain: [name one §1 domain label]
Lens.verify match: [specific lens.verify entry from this role's definition]
Basis: [one sentence -- why this lens entry makes this role HIGH relevance to THIS artifact]

Role [domain role name]: Applicability = [HIGH / MEDIUM / LOW]
Artifact domain: [name the §1 domain label with highest applicability for this role]
Lens.verify match: [specific lens.verify entry from this role's definition]
Basis: [one sentence -- why this lens entry makes this role [rating] relevance to THIS artifact]

Role [lifecycle role name]: Applicability = [HIGH / MEDIUM / LOW]
Artifact domain: [name the §1 domain label with highest applicability for this role]
Lens.verify match: [specific lens.verify entry from this role's definition]
Basis: [one sentence -- why this lens entry makes this role [rating] relevance to THIS artifact]

*(Revise any generic justification before proceeding. Generic = no specific artifact domain
or no specific lens.verify entry cited. A role failing certification is downgraded to LOW.)*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [What the team does today instead of building this -- one sentence.]

**Null hypothesis strength**: [HIGH / MEDIUM / LOW]

**Alternatives comparison table**:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|---------------|-----------|----------------------|-------|
| [DIM-1]   | [score]       | [score]   | [score]              | [reason] |
| [DIM-2]   | [score]       | [score]   | [score]              | |
| [DIM-3]   | [score]       | [score]   | [score]              | |

**NULL HYPOTHESIS DERIVATION RULE** *(pre-committed per §9)*:
[Formula mapping differentials B-A and B-C to g_null verdict. Both differentials required.]

**Challenge claims** *(assign CH-IDs per §5)*:

| CH-ID  | Challenge Claim | Severity |
|--------|----------------|----------|
| CH-001 | [CLAIM_1]      | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2]      | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional] | [HIGH / MEDIUM / LOW] |

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]
**g_null(initial)** *(per §9 Stage 1 -- equals GOpen)*: [PASS / CONDITIONAL / FAIL]

**Local Gate Ledger Row**:
| Section         | Gate  | Verdict                    | Class                              |
|-----------------|-------|----------------------------|------------------------------------|
| BRACKET OPENING | GOpen | [PASS / CONDITIONAL / FAIL]| [BLOCKED / CONDITIONAL / ADVISORY] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy from BRACKET OPENING]

**CH-ID Response Table** *(mandatory per §5)*:

| CH-ID  | Challenge Claim (copy) | This Role's Domain Response | Status |
|--------|----------------------|-----------------------------|--------|
| CH-001 | [copy]               | [RESPONSE_1]                | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]               | [RESPONSE_2]                | [ADDRESSED / PARTIAL / OPEN] |

**Additional Findings** *(per §14 and §11)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n]  | [FINDING_1] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n]  | [FINDING_2] | [HIGH / MEDIUM / LOW] |

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_]) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW]

**LENS COVERAGE TABLE** *(per §15 -- Applicability from ROLE MANIFEST §17)*:

| # | lens.verify Entry | Applicability | Status | Finding Reference |
|---|------------------|--------------|--------|-------------------|
| 1 | [entry 1 from role definition] | [from ROLE MANIFEST] | [ADDRESSED / OPEN] | [F-n or "no finding"] |
| 2 | [entry 2] | [from ROLE MANIFEST] | [ADDRESSED / OPEN] | [F-n or "no finding"] |

*(OPEN entries on HIGH-applicability rows are ADVISORY-OPEN-LENS per §15.)*

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section               | Gate     | Verdict                    | Class                              |
|-----------------------|----------|----------------------------|------------------------------------|
| DOMAIN -- [ROLE_NAME] | G_domain | [PASS / CONDITIONAL / FAIL]| [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT

*(EXCLUDED from gate ledger per §6.)*

```
G_domain_agg = worst([list G_domain verdicts]) = [PASS / CONDITIONAL / FAIL]
g_null(post-domain) via §9 Stage 2:
  G_domain_agg = [_], g_null(initial) = [_] --> g_null(post-domain) = [PASS / CONDITIONAL / FAIL]
```

---

## §3.8 CH-ID SATURATION CHECK

*(EXCLUDED from gate ledger per §6. Pre-LIFECYCLE gate per §8.)*

| CH-ID  | DOMAIN Response Status       | Pre-LIFECYCLE Saturation |
|--------|------------------------------|--------------------------|
| CH-001 | [ADDRESSED / PARTIAL / OPEN] | [SATURATED / UNSATURATED]|
| CH-002 | [copy]                       | [SATURATED / UNSATURATED]|

**Pre-LIFECYCLE unsaturated CH-IDs**: [List or "None"]

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]
Received G_domain Aggregate: [copy from §3.5]
Received g_null(post-domain): [copy from §3.5]

**CH-ID Response Table** *(mandatory per §5)*:

| CH-ID  | Challenge Claim (copy) | This Role's Lifecycle Response | Status |
|--------|----------------------|-------------------------------|--------|
| CH-001 | [copy]               | [RESPONSE_1]                  | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]               | [RESPONSE_2]                  | [ADDRESSED / PARTIAL / OPEN] |

**Additional Findings** *(per §14 and §11)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n]  | [FINDING_1] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n]  | [FINDING_2] | [HIGH / MEDIUM / LOW] |

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_]) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW]

**LENS COVERAGE TABLE** *(per §15 -- Applicability from ROLE MANIFEST §17)*:

| # | lens.verify Entry | Applicability | Status | Finding Reference |
|---|------------------|--------------|--------|-------------------|
| 1 | [entry 1] | [from ROLE MANIFEST] | [ADDRESSED / OPEN] | [F-n or "no finding"] |
| 2 | [entry 2] | [from ROLE MANIFEST] | [ADDRESSED / OPEN] | [F-n or "no finding"] |

*(OPEN entries on HIGH-applicability rows are ADVISORY-OPEN-LENS per §15.)*

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
**G_lifecycle Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section                  | Gate        | Verdict                    | Class                              |
|--------------------------|-------------|----------------------------|------------------------------------|
| LIFECYCLE -- [ROLE_NAME] | G_lifecycle | [PASS / CONDITIONAL / FAIL]| [BLOCKED / CONDITIONAL / ADVISORY] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

```
g_null(post-domain) = [copy from §3.5]
G_lifecycle         = [copy from LIFECYCLE local ledger]
Apply §9 Stage 3 --> g_null(final) = [FAIL / CONDITIONAL / PASS]
```

**Full CH-ID Saturation Check** *(per §8)*:

| CH-ID  | DOMAIN Status | LIFECYCLE Status | Full Saturation |
|--------|--------------|-----------------|-----------------|
| CH-001 | [copy]        | [copy]           | [FULLY SATURATED / UNSATURATED] |
| CH-002 | [copy]        | [copy]           | [FULLY SATURATED / UNSATURATED] |

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
*(Must equal g_null(final) per §9. Override format: "g_null OVERRIDE: [reason]")*
**GClose Rationale**: [2-3 sentences referencing g_null(final), CH-ID saturation, null trajectory.]

**Local Gate Ledger Row**:
| Section         | Gate   | Verdict                    | Class                              |
|-----------------|--------|----------------------------|------------------------------------|
| BRACKET CLOSING | GClose | [PASS / CONDITIONAL / FAIL]| [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION

*(EXCLUDED from gate ledger per §6.)*

| IN-SCOPE Surface | Reviewer(s)  | Finding Reference(s) | Coverage         |
|-----------------|--------------|---------------------|-----------------|
| [§1 SURFACE_1]  | [ROLE or "none"] | [F-n / etc.]    | [COVERED / GAP] |
| [§1 SURFACE_2]  | [ROLE or "none"] | [F-n / etc.]    | [COVERED / GAP] |

**Coverage gate signal** *(informational)*: [COVERED / PARTIAL]
**Advisory items for ACTION ITEM REGISTER**: [GAP, ORPHAN, OPEN-LENS items or "None"]

---

## GATE VECTOR TABLE

| Gate         | Reviewer           | Verdict                    | Contract Cite           |
|--------------|--------------------|----------------------------|-------------------------|
| GOpen        | [CHALLENGER_ROLE]  | [PASS / CONDITIONAL / FAIL]| DISPOSITION_CONTRACT v1 |
| G_domain_agg | [DOMAIN_ROLE(S)]   | [PASS / CONDITIONAL / FAIL]| DISPOSITION_CONTRACT v1 |
| G_lifecycle  | [LIFECYCLE_ROLE]   | [PASS / CONDITIONAL / FAIL]| DISPOSITION_CONTRACT v1 |
| GClose       | [CHALLENGER_ROLE]  | [PASS / CONDITIONAL / FAIL]| DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [Two reviewers with incompatible responses. If none: "None detected."]
**Convergence**: [CH-ID or concern named by two or more reviewers.]

**§13 Progression Ledger**:
```
g_null(initial)     = [copy from BRACKET OPENING]
g_null(post-domain) = [copy from §3.5]
g_null(final)       = [copy from BRACKET CLOSING]
Trajectory:         [MONOTONIC-PASS / MONOTONIC-FAIL / DOMAIN-DEGRADED /
                     LIFECYCLE-DEGRADED / DOMAIN-RECOVERED / LIFECYCLE-RECOVERED]
```

---

## DISPOSITION

**Gate vector**:
- GOpen = [copy] | G_domain_agg = [copy] | G_lifecycle = [copy] | GClose = [copy]

**Apply §3 formula**:
```
GClose = FAIL? --> BLOCKED
Any other Gi = FAIL? --> BLOCKED
No FAIL, any CONDITIONAL? --> CONDITIONAL
All PASS? --> READY
```

**Overall Disposition**: [BLOCKED / CONDITIONAL / READY]
**Primary Driver** *(per §16)*: [mechanically derived]
**RESOLUTION REGISTRY** *(per §12)*: [table if CONDITIONAL; else "N/A -- [disposition]"]

---

## ACTION ITEM REGISTER

*(Copies local gate ledger rows verbatim per §6. Do not re-derive.)*

| Section                  | Gate        | Verdict | Class |
|--------------------------|-------------|---------|-------|
| BRACKET OPENING          | GOpen       | [copy]  | [copy]|
| DOMAIN -- [ROLE]         | G_domain    | [copy]  | [copy]|
| LIFECYCLE -- [ROLE]      | G_lifecycle | [copy]  | [copy]|
| BRACKET CLOSING          | GClose      | [copy]  | [copy]|

**Advisory items** *(ADVISORY-GAP, ADVISORY-ORPHAN, ADVISORY-OPEN-LENS)*:
- [list or "None"]

---

**Artifact to review:**

{{artifact}}

---

---

## V-02

**Axis**: Output format -- §17 DOMAIN-ROLE COVERAGE MATRIX (C-34 via domain-inward matrix)
**Hypothesis**: R16 V-02 adds a PRE-REVIEW DOMAIN COVERAGE GAP-CHECK as a narrative section
that enumerates domains and checks for HIGH-applicability coverage. The weakness: the check
is prose-structured -- the model reports "domain X has no HIGH-applicability reviewer" as a
sentence, and the ACTION ITEM REGISTER entry for ADVISORY-GAP derives from that sentence.
C-34 requires the gap to be classified as ADVISORY-GAP in the action register, which R16 V-02
achieves, but a scorer must read the prose to verify it. V-02 here replaces the narrative
gap-check with a DOMAIN-ROLE COVERAGE MATRIX: a table where rows = artifact domains (from §1
[DOMAIN: label] annotations), columns = selected roles (from ROLE MANIFEST), and each cell =
applicability tier. A domain row with no HIGH cell is a DOMAIN-GAP by structural inspection
alone -- no prose needed. The matrix also serves as a cross-reference for C-33 (each cell IS
the per-domain applicability rating) and C-34 (each empty-HIGH row IS an ADVISORY-GAP).
The matrix is produced in a dedicated §17 section between ROLE MANIFEST and BRACKET OPENING.

---

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .craft/roles/signal/
```

Emit this block first. Fill in injected values.

```
## Review Parameters
Artifact:     {{artifact_id}}
Depth:        {{depth}}
Reviewer set: {{reviewer_set}}
```

---

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any
pre-printed heading, label, field, formula, or structural element. If a field cannot
be filled, write `[N/A -- reason]`.

---

```
======================================================================
DISPOSITION_CONTRACT v1
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§17;
reviewer sections may not execute until §1 COMPLETE and DOMAIN-ROLE
COVERAGE MATRIX COMPLETE markers are both reached]
======================================================================

§1 -- SCOPE ENUMERATION
IN-SCOPE -- surfaces this review will evaluate:
  1. [SURFACE_1]   [DOMAIN: domain-label]
  2. [SURFACE_2]   [DOMAIN: domain-label]
  3. [SURFACE_3]   [DOMAIN: domain-label]
  (Add rows. Domain labels become the matrix rows in §17.)

OUT-OF-SCOPE:
  1. [SURFACE -- REASON_EXCLUDED]

Scope Amendment Protocol:
  SCOPE AMENDMENT: [surface] added to IN-SCOPE -- [reason]

§1 COMPLETE.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH = Blocks commitment. MEDIUM = Conditions commitment. LOW = Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose = FAIL OR exists Gi = FAIL
  CONDITIONAL <-- no FAIL AND exists CONDITIONAL
  READY <-- all PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(all G_domain verdicts). FAIL > CONDITIONAL > PASS.

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Each challenge claim receives CH-ID. Every downstream section carries CH-ID response table.
  PASS prohibited if any CH-ID row = OPEN.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Row syntax: | Section | Gate | Verdict | Class |
  Class: FAIL->BLOCKED; CONDITIONAL->CONDITIONAL; PASS->ADVISORY.
  Emission: end of each verdict-emitting section.
  Assembly: ACTION ITEM REGISTER copies verbatim. No re-derivation.
  EXCLUDED: §3.5, §3.8, §5.5, DOMAIN-ROLE COVERAGE MATRIX section.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  1.   ROLE MANIFEST
  1.5. DOMAIN-ROLE COVERAGE MATRIX    [per §17; pre-reviewer; no ledger row]
  2.   BRACKET OPENING
  3.   DOMAIN(s)
  3.5. DOMAIN-AGGREGATE CHECKPOINT
  3.8. CH-ID SATURATION CHECK
  4.   LIFECYCLE
  5.   BRACKET CLOSING
  5.5. SCOPE COVERAGE RECONCILIATION
  6.   GATE VECTOR TABLE
  7.   CROSS-ROLE SIGNALS
  8.   DISPOSITION
  9.   ACTION ITEM REGISTER
  Reordering violates this contract. MATRIX must precede BRACKET OPENING.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED: CH-ID has response in >= 1 DOMAIN section (before LIFECYCLE).
  FULLY SATURATED: CH-ID has response in DOMAIN and LIFECYCLE (before BRACKET CLOSING).
  PASS from BRACKET CLOSING prohibited without full saturation (or stated waiver).

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  g_null(initial) = GOpen.
  g_null(post-domain): FAIL if G_domain_agg=FAIL; max(g_null(initial), CONDITIONAL) if
  G_domain_agg=CONDITIONAL; g_null(initial) if G_domain_agg=PASS.
  g_null(final): FAIL if G_lifecycle=FAIL; max(g_null(post-domain), CONDITIONAL) if
  G_lifecycle=CONDITIONAL; g_null(post-domain) if G_lifecycle=PASS.
  GClose must equal g_null(final) or declare override.

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 maps each §1 surface to reviewer findings. GAP surfaces -> ADVISORY-GAP in register.

§11 -- FINDING-SURFACE LINKAGE REQUIREMENT [IMMUTABLE]
  Each finding cites §1 surface: "[§1:S-n] finding text". No citation = ADVISORY-ORPHAN.

§12 -- CONDITIONAL RESOLUTION REGISTRY CONTRACT [IMMUTABLE]
  If DISPOSITION = CONDITIONAL: emit RESOLUTION REGISTRY table after Overall Disposition.

§13 -- g_null PROGRESSION LEDGER REQUIREMENT [IMMUTABLE]
  In CROSS-ROLE SIGNALS: g_null(initial) | g_null(post-domain) | g_null(final) | Trajectory.

§14 -- FINDING SEVERITY AGGREGATION CONTRACT [IMMUTABLE]
  Each finding row carries individual Severity. Section Severity = worst(all finding severities).

§15 -- LENS EXHAUSTION REQUIREMENT [IMMUTABLE]
  Each DOMAIN and LIFECYCLE section emits LENS COVERAGE TABLE. Applicability from §17 matrix
  (the cell value for this role x this artifact's primary domain). OPEN + HIGH-applicability
  -> ADVISORY-OPEN-LENS in register.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  GClose=FAIL -> Primary Driver=GClose. Any G_domain=FAIL -> Primary Driver=DOMAIN.
  G_lifecycle=FAIL -> Primary Driver=LIFECYCLE. Any CONDITIONAL -> lowest-index gate.
  All PASS -> N/A.

§17 -- DOMAIN-ROLE COVERAGE MATRIX CONTRACT [IMMUTABLE]
  After §1 COMPLETE and ROLE MANIFEST complete, produce a DOMAIN-ROLE COVERAGE MATRIX.

  Rows: every unique [DOMAIN: label] value from §1 IN-SCOPE enumeration.
  Columns: every selected role from the ROLE MANIFEST (one column per role).
  Cells: applicability tier for that role x domain combination (HIGH / MEDIUM / LOW / --).
    HIGH   = This role's lens.verify directly addresses this artifact domain.
    MEDIUM = This role's lens.verify partially addresses this artifact domain.
    LOW    = This role's lens.verify has limited bearing on this artifact domain.
    --     = This role has no lens.verify entry relevant to this domain.

  Domain gap classification (mechanical -- apply after matrix is built):
    DOMAIN-COVERED: at least one cell in this domain row = HIGH.
    DOMAIN-GAP:     no cell in this domain row = HIGH.
  Each DOMAIN-GAP row produces an ADVISORY-GAP item in the ACTION ITEM REGISTER:
    "ADVISORY-GAP: [domain label] -- no HIGH-applicability reviewer selected. [reason]"

  The matrix is produced at step 1.5 (after ROLE MANIFEST, before BRACKET OPENING).
  Matrix cells are not re-rated after the matrix is emitted.

  §15 LENS COVERAGE TABLE Applicability column: use the matrix cell value for
  (this role, this artifact's primary domain) as the applicability rating per row.

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================
```

---

## ROLE MANIFEST

Read `.craft/roles/signal/`. Assign each slot.

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

*(For `--depth deep`: add DOMAIN-2, DOMAIN-3 rows.)*

---

## DOMAIN-ROLE COVERAGE MATRIX

*(Per §17 -- produced after ROLE MANIFEST, before BRACKET OPENING. No ledger row per §6.)*

Domains from §1 annotations x roles from ROLE MANIFEST:

| Artifact Domain | [CHALLENGER_ROLE] | [DOMAIN_ROLE] | [LIFECYCLE_ROLE] | Gap Status |
|-----------------|-------------------|---------------|------------------|-----------|
| [domain-label-1] | [HIGH/MEDIUM/LOW/--] | [HIGH/MEDIUM/LOW/--] | [HIGH/MEDIUM/LOW/--] | [DOMAIN-COVERED / DOMAIN-GAP] |
| [domain-label-2] | [HIGH/MEDIUM/LOW/--] | [HIGH/MEDIUM/LOW/--] | [HIGH/MEDIUM/LOW/--] | [DOMAIN-COVERED / DOMAIN-GAP] |
| [domain-label-3] | [HIGH/MEDIUM/LOW/--] | [HIGH/MEDIUM/LOW/--] | [HIGH/MEDIUM/LOW/--] | [DOMAIN-COVERED / DOMAIN-GAP] |

*(Add rows for all §1 domain labels. Mark Gap Status mechanically: DOMAIN-GAP if no HIGH in row.)*

**ADVISORY-GAP items pre-registered for ACTION ITEM REGISTER**:
- [domain-label, if DOMAIN-GAP]: "ADVISORY-GAP: [domain] -- no HIGH-applicability reviewer. [reason]"
- (or "None -- all domains COVERED")

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [What the team does today instead of building this.]

**Null hypothesis strength**: [HIGH / MEDIUM / LOW]

**Alternatives comparison table**:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|---------------|-----------|----------------------|-------|
| [DIM-1]   | [score]       | [score]   | [score]              | [reason] |
| [DIM-2]   | [score]       | [score]   | [score]              | |
| [DIM-3]   | [score]       | [score]   | [score]              | |

**NULL HYPOTHESIS DERIVATION RULE**: [Formula mapping B-A and B-C differentials to verdict.]

**Challenge claims**:

| CH-ID  | Challenge Claim | Severity |
|--------|----------------|----------|
| CH-001 | [CLAIM_1]      | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2]      | [HIGH / MEDIUM / LOW] |

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]
**g_null(initial)** *(= GOpen per §9)*: [PASS / CONDITIONAL / FAIL]

**Local Gate Ledger Row**:
| Section         | Gate  | Verdict                    | Class                              |
|-----------------|-------|----------------------------|------------------------------------|
| BRACKET OPENING | GOpen | [PASS / CONDITIONAL / FAIL]| [BLOCKED / CONDITIONAL / ADVISORY] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]

**CH-ID Response Table**:

| CH-ID  | Challenge Claim (copy) | Domain Response | Status |
|--------|----------------------|-----------------|--------|
| CH-001 | [copy]               | [RESPONSE_1]    | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]               | [RESPONSE_2]    | [ADDRESSED / PARTIAL / OPEN] |

**Additional Findings**:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n]  | [FINDING_1] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n]  | [FINDING_2] | [HIGH / MEDIUM / LOW] |

**Section Severity** *(worst per §14)*: [HIGH / MEDIUM / LOW]

**LENS COVERAGE TABLE** *(Applicability from §17 matrix -- use cell value for this role x primary domain)*:

| # | lens.verify Entry | Applicability | Status | Finding Reference |
|---|------------------|--------------|--------|-------------------|
| 1 | [entry 1] | [from §17 matrix] | [ADDRESSED / OPEN] | [F-n or "no finding"] |
| 2 | [entry 2] | [from §17 matrix] | [ADDRESSED / OPEN] | [F-n or "no finding"] |

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section               | Gate     | Verdict                    | Class                              |
|-----------------------|----------|----------------------------|------------------------------------|
| DOMAIN -- [ROLE_NAME] | G_domain | [PASS / CONDITIONAL / FAIL]| [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT

*(EXCLUDED from gate ledger.)*

```
G_domain_agg = worst([verdicts]) = [PASS / CONDITIONAL / FAIL]
g_null(post-domain) via §9: [PASS / CONDITIONAL / FAIL]
```

---

## §3.8 CH-ID SATURATION CHECK

*(EXCLUDED from gate ledger.)*

| CH-ID  | DOMAIN Status | Pre-LIFECYCLE Saturation |
|--------|--------------|--------------------------|
| CH-001 | [status]     | [SATURATED / UNSATURATED]|
| CH-002 | [status]     | [SATURATED / UNSATURATED]|

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy] | G_domain Aggregate: [copy] | g_null(post-domain): [copy]

**CH-ID Response Table**:

| CH-ID  | Challenge Claim (copy) | Lifecycle Response | Status |
|--------|----------------------|-------------------|--------|
| CH-001 | [copy]               | [RESPONSE_1]      | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]               | [RESPONSE_2]      | [ADDRESSED / PARTIAL / OPEN] |

**Additional Findings**:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n]  | [FINDING_1] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n]  | [FINDING_2] | [HIGH / MEDIUM / LOW] |

**Section Severity** *(worst per §14)*: [HIGH / MEDIUM / LOW]

**LENS COVERAGE TABLE** *(Applicability from §17 matrix)*:

| # | lens.verify Entry | Applicability | Status | Finding Reference |
|---|------------------|--------------|--------|-------------------|
| 1 | [entry 1] | [from §17 matrix] | [ADDRESSED / OPEN] | [F-n or "no finding"] |
| 2 | [entry 2] | [from §17 matrix] | [ADDRESSED / OPEN] | [F-n or "no finding"] |

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
**G_lifecycle Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section                  | Gate        | Verdict                    | Class                              |
|--------------------------|-------------|----------------------------|------------------------------------|
| LIFECYCLE -- [ROLE_NAME] | G_lifecycle | [PASS / CONDITIONAL / FAIL]| [BLOCKED / CONDITIONAL / ADVISORY] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

```
g_null(post-domain) = [copy] | G_lifecycle = [copy]
Apply §9 Stage 3 --> g_null(final) = [FAIL / CONDITIONAL / PASS]
```

**Full CH-ID Saturation Check**:

| CH-ID  | DOMAIN | LIFECYCLE | Full Saturation |
|--------|--------|-----------|-----------------|
| CH-001 | [copy] | [copy]    | [FULLY SATURATED / UNSATURATED] |
| CH-002 | [copy] | [copy]    | [FULLY SATURATED / UNSATURATED] |

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**GClose Rationale**: [2-3 sentences.]

**Local Gate Ledger Row**:
| Section         | Gate   | Verdict                    | Class                              |
|-----------------|--------|----------------------------|------------------------------------|
| BRACKET CLOSING | GClose | [PASS / CONDITIONAL / FAIL]| [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION

*(EXCLUDED from gate ledger.)*

| IN-SCOPE Surface | Reviewer(s) | Finding Reference(s) | Coverage |
|-----------------|-------------|---------------------|----------|
| [SURFACE_1]     | [ROLE]      | [F-n]               | [COVERED / GAP] |

**Advisory items**: [GAP, ORPHAN, OPEN-LENS items or "None"]

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract Cite |
|------|----------|---------|---------------|
| GOpen | [CHALLENGER] | [verdict] | DISPOSITION_CONTRACT v1 |
| G_domain_agg | [DOMAIN] | [verdict] | DISPOSITION_CONTRACT v1 |
| G_lifecycle | [LIFECYCLE] | [verdict] | DISPOSITION_CONTRACT v1 |
| GClose | [CHALLENGER] | [verdict] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [or "None detected."]
**Convergence**: [or "None detected."]
**§13 Progression Ledger**: g_null(initial)=[_] | g_null(post-domain)=[_] | g_null(final)=[_] | Trajectory=[_]

---

## DISPOSITION

Gate vector: GOpen=[_] | G_domain_agg=[_] | G_lifecycle=[_] | GClose=[_]

**Apply §3**: [BLOCKED / CONDITIONAL / READY]
**Overall Disposition**: [result]
**Primary Driver** *(per §16)*: [derived]
**RESOLUTION REGISTRY** *(per §12)*: [table or "N/A"]

---

## ACTION ITEM REGISTER

*(Verbatim copy per §6.)*

| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [copy] | [copy] |
| DOMAIN -- [ROLE] | G_domain | [copy] | [copy] |
| LIFECYCLE -- [ROLE] | G_lifecycle | [copy] | [copy] |
| BRACKET CLOSING | GClose | [copy] | [copy] |

**Advisory items** *(including ADVISORY-GAP items from §17 matrix gap-check)*:
- [list from DOMAIN-ROLE COVERAGE MATRIX + §5.5 + §11 + §15 or "None"]

---

**Artifact to review:**

{{artifact}}

---

---

## V-03

**Axis**: Role sequence -- §17 CHALLENGER PRE-ASSESSMENT (C-35 via extracted standalone section)
**Hypothesis**: R16 V-03 adds an NH DIMENSION TABLE inside BRACKET OPENING. The table has
columns: Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes. g_null
is derived from a NULL HYPOTHESIS DERIVATION RULE applied to differentials B-A and B-C.
The weakness: the dimension table and the derivation rule are inside BRACKET OPENING alongside
the challenge claims, the GOpen verdict, and the g_null(initial) assignment. A model executing
this section attends to many fields at once; the mechanical derivation of g_null from table
values may be overridden by the narrative "Null hypothesis strength: HIGH/MEDIUM/LOW" field
that precedes it, or by the GOpen Verdict field that follows it. C-35 requires g_null
derivable from the table values ALONE -- without reading prose. V-03 extracts the NH dimension
table into a standalone CHALLENGER PRE-ASSESSMENT section that runs before BRACKET OPENING.
The PRE-ASSESSMENT has one output: g_null(initial) derived mechanically from a VERDICT column
per dimension. BRACKET OPENING inherits that value and does NOT re-derive it. Structural
separation makes C-35 verifiable from PRE-ASSESSMENT output alone.

---

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .craft/roles/signal/
```

Emit this block first. Fill in injected values.

```
## Review Parameters
Artifact:     {{artifact_id}}
Depth:        {{depth}}
Reviewer set: {{reviewer_set}}
```

---

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any
pre-printed heading, label, field, formula, or structural element. If a field cannot
be filled, write `[N/A -- reason]`.

---

```
======================================================================
DISPOSITION_CONTRACT v1
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§17;
reviewer sections may not execute until §1 COMPLETE marker is reached]
======================================================================

§1 -- SCOPE ENUMERATION
IN-SCOPE:
  1. [SURFACE_1]   [DOMAIN: domain-label]
  2. [SURFACE_2]   [DOMAIN: domain-label]
  3. [SURFACE_3]   [DOMAIN: domain-label]

OUT-OF-SCOPE:
  1. [SURFACE -- REASON_EXCLUDED]

§1 COMPLETE.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH = Blocks. MEDIUM = Conditions. LOW = Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose=FAIL OR any Gi=FAIL
  CONDITIONAL <-- no FAIL AND any CONDITIONAL
  READY <-- all PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(all G_domain verdicts).

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Challenge claims receive CH-IDs. All downstream sections carry CH-ID response tables.
  PASS prohibited if any CH-ID = OPEN.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Row syntax: | Section | Gate | Verdict | Class |
  Class: FAIL->BLOCKED; CONDITIONAL->CONDITIONAL; PASS->ADVISORY.
  Emission: end of each verdict-emitting section.
  Assembly: verbatim copy to ACTION ITEM REGISTER. No re-derivation.
  EXCLUDED: §3.5, §3.8, §5.5, CHALLENGER PRE-ASSESSMENT.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  1.   ROLE MANIFEST
  1.5. CHALLENGER PRE-ASSESSMENT     [per §17; standalone; no ledger row]
  2.   BRACKET OPENING               [inherits g_null(initial) from PRE-ASSESSMENT]
  3.   DOMAIN(s)
  3.5. DOMAIN-AGGREGATE CHECKPOINT
  3.8. CH-ID SATURATION CHECK
  4.   LIFECYCLE
  5.   BRACKET CLOSING
  5.5. SCOPE COVERAGE RECONCILIATION
  6.   GATE VECTOR TABLE
  7.   CROSS-ROLE SIGNALS
  8.   DISPOSITION
  9.   ACTION ITEM REGISTER
  CHALLENGER PRE-ASSESSMENT must precede BRACKET OPENING.
  BRACKET OPENING inherits g_null(initial) from CHALLENGER PRE-ASSESSMENT;
  it does not re-derive g_null(initial) from narrative fields.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED: domain response before LIFECYCLE. FULLY SATURATED: domain + lifecycle before
  BRACKET CLOSING. PASS from BRACKET CLOSING prohibited without full saturation.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial) is produced by CHALLENGER PRE-ASSESSMENT via §17 formula.
    GOpen in BRACKET OPENING must equal g_null(initial). If GOpen != g_null(initial):
    emit "g_null CONFLICT: GOpen=[_] vs g_null(initial)=[_] -- [resolution]".
  Stage 2: g_null(post-domain):
    G_domain_agg=FAIL -> FAIL; G_domain_agg=CONDITIONAL -> max(g_null(initial),CONDITIONAL);
    G_domain_agg=PASS -> g_null(initial).
  Stage 3: g_null(final):
    G_lifecycle=FAIL -> FAIL; G_lifecycle=CONDITIONAL -> max(g_null(post-domain),CONDITIONAL);
    G_lifecycle=PASS -> g_null(post-domain).
  GClose must equal g_null(final) or declare override.

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 maps §1 surfaces to findings. GAP -> ADVISORY-GAP in register.

§11 -- FINDING-SURFACE LINKAGE REQUIREMENT [IMMUTABLE]
  Each finding cites §1 surface. No citation = ADVISORY-ORPHAN.

§12 -- CONDITIONAL RESOLUTION REGISTRY CONTRACT [IMMUTABLE]
  DISPOSITION=CONDITIONAL: emit RESOLUTION REGISTRY table.

§13 -- g_null PROGRESSION LEDGER REQUIREMENT [IMMUTABLE]
  In CROSS-ROLE SIGNALS: g_null(initial) | g_null(post-domain) | g_null(final) | Trajectory.

§14 -- FINDING SEVERITY AGGREGATION CONTRACT [IMMUTABLE]
  Each finding row: individual Severity. Section Severity = worst(all severities in section).

§15 -- LENS EXHAUSTION REQUIREMENT [IMMUTABLE]
  Each DOMAIN/LIFECYCLE section: LENS COVERAGE TABLE. Applicability from ROLE MANIFEST.
  OPEN + HIGH-applicability -> ADVISORY-OPEN-LENS.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  GClose=FAIL -> GClose. Any G_domain=FAIL -> DOMAIN. G_lifecycle=FAIL -> LIFECYCLE.
  Any CONDITIONAL -> lowest-index gate. All PASS -> N/A.

§17 -- CHALLENGER PRE-ASSESSMENT PROTOCOL [IMMUTABLE]
  A standalone CHALLENGER PRE-ASSESSMENT section executes between ROLE MANIFEST and
  BRACKET OPENING. Its sole output is g_null(initial).

  The PRE-ASSESSMENT contains the NH DIMENSION TABLE:
    | Dimension | Current State | Proposed Build | Delta (Build - Current) | NH Verdict |
    |-----------|--------------|---------------|------------------------|-----------|
    | [DIM-n]   | [description]| [description] | [+/-/=]                | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |

  NH Verdict semantics:
    FAVORS-BUILD:    Delta favors adoption of the artifact over current state.
    NEUTRAL:         Delta is approximately zero or ambiguous.
    OPPOSES-BUILD:   Delta favors continuing with current state (null hypothesis).

  g_null(initial) derivation formula (pre-committed; apply mechanically):
    Let F = count(NH Verdict = FAVORS-BUILD)
    Let O = count(NH Verdict = OPPOSES-BUILD)
    if F > O:  g_null(initial) = PASS    [build case stronger than null]
    if F = O:  g_null(initial) = CONDITIONAL [balanced; material gaps remain]
    if F < O:  g_null(initial) = FAIL    [null hypothesis holds]

  The PRE-ASSESSMENT emits g_null(initial) as a labeled field derivable from the
  NH Verdict column counts alone. No prose is required to determine g_null(initial).
  BRACKET OPENING carries forward g_null(initial) from PRE-ASSESSMENT.
  BRACKET OPENING does NOT include a "Null hypothesis strength" narrative field;
  the strength is encoded in the table and formula.

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================
```

---

## ROLE MANIFEST

Read `.craft/roles/signal/`. Assign each slot.

| Slot | Archetype | Role | Selection Rationale | Applicability |
|------|-----------|------|---------------------|---------------|
| CHALLENGER (fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] | HIGH |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] | [HIGH / MEDIUM / LOW] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] | [HIGH / MEDIUM / LOW] |

---

## CHALLENGER PRE-ASSESSMENT

*(Per §17 -- standalone section before BRACKET OPENING. No ledger row per §6.)*

**NH DIMENSION TABLE** *(pre-committed basis for g_null(initial))*:

| Dimension | Current State | Proposed Build | Delta (Build - Current) | NH Verdict |
|-----------|--------------|---------------|------------------------|-----------|
| [DIM-1 -- e.g., team effort required] | [current state] | [with artifact] | [+/-/=] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-2 -- e.g., coverage of artifact's target problem] | [current state] | [with artifact] | [+/-/=] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-3 -- e.g., adoption friction] | [current state] | [with artifact] | [+/-/=] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |

*(Add dimensions as needed. Each NH Verdict cell must be one of: FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD.)*

**Applying §17 formula**:
```
F (FAVORS-BUILD count) = [_]
O (OPPOSES-BUILD count) = [_]
F > O? PASS.  F = O? CONDITIONAL.  F < O? FAIL.
g_null(initial) = [PASS / CONDITIONAL / FAIL]
```

**g_null(initial)**: [PASS / CONDITIONAL / FAIL]
*(This value carries forward to BRACKET OPENING §9 Stage 1. Derivable from NH Verdict column counts above.)*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [What the team does today instead of building this -- one sentence.]

**g_null(initial) received from CHALLENGER PRE-ASSESSMENT**: [copy -- do not re-derive]

**Challenge claims** *(assign CH-IDs per §5)*:

| CH-ID  | Challenge Claim | Severity |
|--------|----------------|----------|
| CH-001 | [CLAIM_1]      | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2]      | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional] | [HIGH / MEDIUM / LOW] |

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
*(Must equal g_null(initial) from CHALLENGER PRE-ASSESSMENT per §9 Stage 1. If different:
emit "g_null CONFLICT: GOpen=[_] vs g_null(initial)=[_] -- [resolution]".)*
**GOpen Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section         | Gate  | Verdict                    | Class                              |
|-----------------|-------|----------------------------|------------------------------------|
| BRACKET OPENING | GOpen | [PASS / CONDITIONAL / FAIL]| [BLOCKED / CONDITIONAL / ADVISORY] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]

**CH-ID Response Table**:

| CH-ID  | Challenge Claim (copy) | Domain Response | Status |
|--------|----------------------|-----------------|--------|
| CH-001 | [copy]               | [RESPONSE_1]    | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]               | [RESPONSE_2]    | [ADDRESSED / PARTIAL / OPEN] |

**Additional Findings**:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n]  | [FINDING_1] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n]  | [FINDING_2] | [HIGH / MEDIUM / LOW] |

**Section Severity** *(worst per §14)*: [HIGH / MEDIUM / LOW]

**LENS COVERAGE TABLE** *(Applicability from ROLE MANIFEST)*:

| # | lens.verify Entry | Applicability | Status | Finding Reference |
|---|------------------|--------------|--------|-------------------|
| 1 | [entry 1] | [from ROLE MANIFEST] | [ADDRESSED / OPEN] | [F-n or "no finding"] |
| 2 | [entry 2] | [from ROLE MANIFEST] | [ADDRESSED / OPEN] | [F-n or "no finding"] |

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section               | Gate     | Verdict                    | Class                              |
|-----------------------|----------|----------------------------|------------------------------------|
| DOMAIN -- [ROLE_NAME] | G_domain | [PASS / CONDITIONAL / FAIL]| [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT

*(EXCLUDED from gate ledger.)*
```
G_domain_agg = [worst verdict] | g_null(post-domain) via §9 = [verdict]
```

---

## §3.8 CH-ID SATURATION CHECK

*(EXCLUDED from gate ledger.)*

| CH-ID  | DOMAIN Status | Saturation |
|--------|--------------|------------|
| CH-001 | [status]     | [SATURATED / UNSATURATED] |
| CH-002 | [status]     | [SATURATED / UNSATURATED] |

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy] | G_domain Aggregate: [copy] | g_null(post-domain): [copy]

**CH-ID Response Table**:

| CH-ID  | Challenge Claim (copy) | Lifecycle Response | Status |
|--------|----------------------|-------------------|--------|
| CH-001 | [copy]               | [RESPONSE_1]      | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]               | [RESPONSE_2]      | [ADDRESSED / PARTIAL / OPEN] |

**Additional Findings**:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n]  | [FINDING_1] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n]  | [FINDING_2] | [HIGH / MEDIUM / LOW] |

**Section Severity** *(worst per §14)*: [HIGH / MEDIUM / LOW]

**LENS COVERAGE TABLE** *(Applicability from ROLE MANIFEST)*:

| # | lens.verify Entry | Applicability | Status | Finding Reference |
|---|------------------|--------------|--------|-------------------|
| 1 | [entry 1] | [from ROLE MANIFEST] | [ADDRESSED / OPEN] | [F-n or "no finding"] |
| 2 | [entry 2] | [from ROLE MANIFEST] | [ADDRESSED / OPEN] | [F-n or "no finding"] |

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
**G_lifecycle Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section                  | Gate        | Verdict                    | Class                              |
|--------------------------|-------------|----------------------------|------------------------------------|
| LIFECYCLE -- [ROLE_NAME] | G_lifecycle | [PASS / CONDITIONAL / FAIL]| [BLOCKED / CONDITIONAL / ADVISORY] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

```
g_null(post-domain) = [copy] | G_lifecycle = [copy]
Apply §9 Stage 3 --> g_null(final) = [verdict]
```

**Full CH-ID Saturation**:

| CH-ID  | DOMAIN | LIFECYCLE | Full Saturation |
|--------|--------|-----------|-----------------|
| CH-001 | [copy] | [copy]    | [FULLY SATURATED / UNSATURATED] |
| CH-002 | [copy] | [copy]    | [FULLY SATURATED / UNSATURATED] |

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**GClose Rationale**: [2-3 sentences.]

**Local Gate Ledger Row**:
| Section         | Gate   | Verdict                    | Class                              |
|-----------------|--------|----------------------------|------------------------------------|
| BRACKET CLOSING | GClose | [PASS / CONDITIONAL / FAIL]| [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION

*(EXCLUDED from gate ledger.)*

| IN-SCOPE Surface | Reviewer(s) | Coverage |
|-----------------|-------------|----------|
| [SURFACE_1]     | [ROLE]      | [COVERED / GAP] |

**Advisory items**: [list or "None"]

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract Cite |
|------|----------|---------|---------------|
| GOpen | [CHALLENGER] | [verdict] | DISPOSITION_CONTRACT v1 |
| G_domain_agg | [DOMAIN] | [verdict] | DISPOSITION_CONTRACT v1 |
| G_lifecycle | [LIFECYCLE] | [verdict] | DISPOSITION_CONTRACT v1 |
| GClose | [CHALLENGER] | [verdict] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [or "None."] | **Convergence**: [or "None."]
**§13 Progression Ledger**: g_null(initial)=[_] | g_null(post-domain)=[_] | g_null(final)=[_] | Trajectory=[_]

---

## DISPOSITION

Gate vector: GOpen=[_] | G_domain_agg=[_] | G_lifecycle=[_] | GClose=[_]
Apply §3: **Overall Disposition**: [BLOCKED / CONDITIONAL / READY]
**Primary Driver** *(per §16)*: [derived]
**RESOLUTION REGISTRY** *(per §12)*: [table or "N/A"]

---

## ACTION ITEM REGISTER

*(Verbatim copy per §6.)*

| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [copy] | [copy] |
| DOMAIN -- [ROLE] | G_domain | [copy] | [copy] |
| LIFECYCLE -- [ROLE] | G_lifecycle | [copy] | [copy] |
| BRACKET CLOSING | GClose | [copy] | [copy] |

**Advisory items**: [list or "None"]

---

**Artifact to review:**

{{artifact}}

---

---

## V-04

**Axes**: Phrasing register + Output format -- §17a APPLICABILITY CERTIFICATION + §17 DOMAIN-ROLE COVERAGE MATRIX (C-33 + C-34 combined)
**Hypothesis**: V-01 demonstrates that APPLICABILITY CERTIFICATION (per-artifact justification
per role) makes C-33 mechanically verifiable: a scorer reads the certification block and
checks for specific artifact domain + specific lens.verify entry. V-02 demonstrates that a
DOMAIN-ROLE COVERAGE MATRIX makes C-34 mechanically verifiable: domain gaps are visible from
matrix structure without reading prose. The hypothesis is that these two mechanisms are
orthogonal and non-interfering -- certification (V-01) verifies that ratings are artifact-
derived; the matrix (V-02) verifies that domains have HIGH-applicability coverage. Together
they satisfy both C-33 and C-34 with zero editorial judgment at either verification step.
V-04 combines both mechanisms on the V-05 R11 base (§1-§16), with §17 as the COVERAGE MATRIX
and §17a as the CERTIFICATION REQUIREMENT. The DOMAIN-ROLE COVERAGE MATRIX cells feed the
§15 LENS COVERAGE TABLE Applicability column (C-33 via matrix) and the gap-check produces
ADVISORY-GAP items (C-34 via matrix). The certification block verifies the matrix ratings
are artifact-specific (C-33 justification layer).

---

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .craft/roles/signal/
```

Emit this block first. Fill in injected values.

```
## Review Parameters
Artifact:     {{artifact_id}}
Depth:        {{depth}}
Reviewer set: {{reviewer_set}}
```

---

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any
pre-printed heading, label, field, formula, or structural element. If a field cannot
be filled, write `[N/A -- reason]`.

---

```
======================================================================
DISPOSITION_CONTRACT v1
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§17a;
reviewer sections may not execute until §1 COMPLETE, DOMAIN-ROLE COVERAGE
MATRIX COMPLETE, and §17a CERTIFICATION COMPLETE markers are all reached]
======================================================================

§1 -- SCOPE ENUMERATION
IN-SCOPE:
  1. [SURFACE_1]   [DOMAIN: domain-label]
  2. [SURFACE_2]   [DOMAIN: domain-label]
  3. [SURFACE_3]   [DOMAIN: domain-label]

OUT-OF-SCOPE:
  1. [SURFACE -- REASON_EXCLUDED]

§1 COMPLETE.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH = Blocks. MEDIUM = Conditions. LOW = Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose=FAIL OR any Gi=FAIL
  CONDITIONAL <-- no FAIL AND any CONDITIONAL
  READY <-- all PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(all G_domain verdicts).

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Challenge claims receive CH-IDs. All downstream sections carry CH-ID response tables.
  PASS prohibited if any CH-ID = OPEN.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Row syntax: | Section | Gate | Verdict | Class |
  Class: FAIL->BLOCKED; CONDITIONAL->CONDITIONAL; PASS->ADVISORY.
  Emission: end of each verdict-emitting section.
  Assembly: verbatim copy. No re-derivation.
  EXCLUDED: §3.5, §3.8, §5.5, DOMAIN-ROLE COVERAGE MATRIX, APPLICABILITY CERTIFICATION BLOCK.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  1.    ROLE MANIFEST
  1.5a. DOMAIN-ROLE COVERAGE MATRIX     [per §17; pre-reviewer; no ledger row]
  1.5b. APPLICABILITY CERTIFICATION BLOCK [per §17a; pre-reviewer; no ledger row]
  2.    BRACKET OPENING
  3.    DOMAIN(s)
  3.5.  DOMAIN-AGGREGATE CHECKPOINT
  3.8.  CH-ID SATURATION CHECK
  4.    LIFECYCLE
  5.    BRACKET CLOSING
  5.5.  SCOPE COVERAGE RECONCILIATION
  6.    GATE VECTOR TABLE
  7.    CROSS-ROLE SIGNALS
  8.    DISPOSITION
  9.    ACTION ITEM REGISTER
  Both pre-reviewer sections (1.5a and 1.5b) must precede BRACKET OPENING.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED before LIFECYCLE. FULLY SATURATED before BRACKET CLOSING.
  PASS from BRACKET CLOSING prohibited without full saturation.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  g_null(initial) = GOpen.
  g_null(post-domain): FAIL->FAIL; CONDITIONAL->max(g_null(initial),CONDITIONAL); PASS->g_null(initial).
  g_null(final): FAIL->FAIL; CONDITIONAL->max(g_null(post-domain),CONDITIONAL); PASS->g_null(post-domain).
  GClose = g_null(final) or override with justification.

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 maps §1 surfaces. GAP -> ADVISORY-GAP in register.

§11 -- FINDING-SURFACE LINKAGE REQUIREMENT [IMMUTABLE]
  Each finding cites §1 surface. No citation = ADVISORY-ORPHAN.

§12 -- CONDITIONAL RESOLUTION REGISTRY CONTRACT [IMMUTABLE]
  DISPOSITION=CONDITIONAL: emit RESOLUTION REGISTRY.

§13 -- g_null PROGRESSION LEDGER REQUIREMENT [IMMUTABLE]
  CROSS-ROLE SIGNALS: g_null(initial) | g_null(post-domain) | g_null(final) | Trajectory.

§14 -- FINDING SEVERITY AGGREGATION CONTRACT [IMMUTABLE]
  Individual Severity per finding row. Section Severity = worst(all row severities).

§15 -- LENS EXHAUSTION REQUIREMENT [IMMUTABLE]
  Each DOMAIN/LIFECYCLE section: LENS COVERAGE TABLE. Applicability from §17 matrix
  (cell value for this role x this artifact's primary domain). OPEN + HIGH -> ADVISORY-OPEN-LENS.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  GClose=FAIL->GClose. G_domain=FAIL->DOMAIN. G_lifecycle=FAIL->LIFECYCLE.
  Any CONDITIONAL->lowest-index. All PASS->N/A.

§17 -- DOMAIN-ROLE COVERAGE MATRIX CONTRACT [IMMUTABLE]
  After ROLE MANIFEST, produce DOMAIN-ROLE COVERAGE MATRIX:
    Rows: §1 domain labels. Columns: selected roles. Cells: HIGH / MEDIUM / LOW / --.
    HIGH = role's lens.verify directly addresses this domain.
    MEDIUM = partially. LOW = limited. -- = no relevant entry.
    DOMAIN-COVERED: >= 1 HIGH cell in row. DOMAIN-GAP: no HIGH cell.
  DOMAIN-GAP rows -> ADVISORY-GAP in ACTION ITEM REGISTER.
  §15 LENS COVERAGE TABLE Applicability: use matrix cell for (role, primary domain).
  Matrix cells not re-rated after emission.

§17a -- APPLICABILITY CERTIFICATION REQUIREMENT [IMMUTABLE]
  After DOMAIN-ROLE COVERAGE MATRIX, emit APPLICABILITY CERTIFICATION BLOCK.
  One entry per selected role:
    Role [name]: Applicability = [HIGH/MEDIUM/LOW -- from §17 matrix, highest cell value]
    Certification domain: [the §1 domain label with the highest matrix cell for this role]
    Lens.verify match: [specific lens.verify entry from this role's definition]
    Artifact-specific basis: [one sentence -- why this entry applies to THIS artifact,
    not just to the artifact type. Must name a specific artifact characteristic.]
  Invalid: generic justification without naming a specific artifact characteristic.
  A role failing certification must have its matrix cell(s) revised downward.

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================
```

---

## ROLE MANIFEST

Read `.craft/roles/signal/`. Assign each slot.

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

---

## DOMAIN-ROLE COVERAGE MATRIX

*(Per §17 -- step 1.5a. No ledger row.)*

| Artifact Domain | [CHALLENGER_ROLE] | [DOMAIN_ROLE] | [LIFECYCLE_ROLE] | Gap Status |
|-----------------|-------------------|---------------|------------------|-----------|
| [domain-label-1] | [HIGH/MED/LOW/--] | [HIGH/MED/LOW/--] | [HIGH/MED/LOW/--] | [COVERED/GAP] |
| [domain-label-2] | [HIGH/MED/LOW/--] | [HIGH/MED/LOW/--] | [HIGH/MED/LOW/--] | [COVERED/GAP] |
| [domain-label-3] | [HIGH/MED/LOW/--] | [HIGH/MED/LOW/--] | [HIGH/MED/LOW/--] | [COVERED/GAP] |

**Pre-registered ADVISORY-GAP items**: [list DOMAIN-GAP rows or "None"]

---

## APPLICABILITY CERTIFICATION BLOCK

*(Per §17a -- step 1.5b. No ledger row.)*

Role [challenger name]: Applicability = HIGH
Certification domain: [§1 domain label]
Lens.verify match: [specific entry from role definition]
Artifact-specific basis: [one sentence with specific artifact characteristic]

Role [domain name]: Applicability = [HIGH / MEDIUM / LOW]
Certification domain: [§1 domain label with highest matrix cell for this role]
Lens.verify match: [specific entry from role definition]
Artifact-specific basis: [one sentence with specific artifact characteristic]

Role [lifecycle name]: Applicability = [HIGH / MEDIUM / LOW]
Certification domain: [§1 domain label with highest matrix cell for this role]
Lens.verify match: [specific entry from role definition]
Artifact-specific basis: [one sentence with specific artifact characteristic]

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [What the team does today instead of building this.]

**Null hypothesis strength**: [HIGH / MEDIUM / LOW]

**Alternatives comparison table**:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|---------------|-----------|----------------------|-------|
| [DIM-1]   | [score]       | [score]   | [score]              | [reason] |
| [DIM-2]   | [score]       | [score]   | [score]              | |
| [DIM-3]   | [score]       | [score]   | [score]              | |

**NULL HYPOTHESIS DERIVATION RULE**: [Formula mapping B-A and B-C to verdict.]

**Challenge claims**:

| CH-ID  | Challenge Claim | Severity |
|--------|----------------|----------|
| CH-001 | [CLAIM_1]      | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2]      | [HIGH / MEDIUM / LOW] |

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]
**g_null(initial)** *(= GOpen per §9)*: [PASS / CONDITIONAL / FAIL]

**Local Gate Ledger Row**:
| Section         | Gate  | Verdict                    | Class                              |
|-----------------|-------|----------------------------|------------------------------------|
| BRACKET OPENING | GOpen | [PASS / CONDITIONAL / FAIL]| [BLOCKED / CONDITIONAL / ADVISORY] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]

**CH-ID Response Table**:

| CH-ID  | Challenge Claim (copy) | Domain Response | Status |
|--------|----------------------|-----------------|--------|
| CH-001 | [copy]               | [RESPONSE_1]    | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]               | [RESPONSE_2]    | [ADDRESSED / PARTIAL / OPEN] |

**Additional Findings**:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n]  | [FINDING_1] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n]  | [FINDING_2] | [HIGH / MEDIUM / LOW] |

**Section Severity** *(worst per §14)*: [HIGH / MEDIUM / LOW]

**LENS COVERAGE TABLE** *(Applicability from §17 matrix -- cell for this role x primary domain)*:

| # | lens.verify Entry | Applicability | Status | Finding Reference |
|---|------------------|--------------|--------|-------------------|
| 1 | [entry 1] | [from §17 matrix] | [ADDRESSED / OPEN] | [F-n or "no finding"] |
| 2 | [entry 2] | [from §17 matrix] | [ADDRESSED / OPEN] | [F-n or "no finding"] |

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section               | Gate     | Verdict                    | Class                              |
|-----------------------|----------|----------------------------|------------------------------------|
| DOMAIN -- [ROLE_NAME] | G_domain | [PASS / CONDITIONAL / FAIL]| [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT

*(EXCLUDED.)*
```
G_domain_agg = [worst] | g_null(post-domain) via §9 = [verdict]
```

---

## §3.8 CH-ID SATURATION CHECK

*(EXCLUDED.)*

| CH-ID | DOMAIN Status | Saturation |
|-------|--------------|------------|
| CH-001 | [status]    | [SATURATED / UNSATURATED] |
| CH-002 | [status]    | [SATURATED / UNSATURATED] |

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy] | G_domain Aggregate: [copy] | g_null(post-domain): [copy]

**CH-ID Response Table**:

| CH-ID  | Challenge Claim (copy) | Lifecycle Response | Status |
|--------|----------------------|-------------------|--------|
| CH-001 | [copy]               | [RESPONSE_1]      | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]               | [RESPONSE_2]      | [ADDRESSED / PARTIAL / OPEN] |

**Additional Findings**:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n]  | [FINDING_1] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n]  | [FINDING_2] | [HIGH / MEDIUM / LOW] |

**Section Severity** *(worst per §14)*: [HIGH / MEDIUM / LOW]

**LENS COVERAGE TABLE** *(Applicability from §17 matrix)*:

| # | lens.verify Entry | Applicability | Status | Finding Reference |
|---|------------------|--------------|--------|-------------------|
| 1 | [entry 1] | [from §17 matrix] | [ADDRESSED / OPEN] | [F-n or "no finding"] |
| 2 | [entry 2] | [from §17 matrix] | [ADDRESSED / OPEN] | [F-n or "no finding"] |

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
**G_lifecycle Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section                  | Gate        | Verdict                    | Class                              |
|--------------------------|-------------|----------------------------|------------------------------------|
| LIFECYCLE -- [ROLE_NAME] | G_lifecycle | [PASS / CONDITIONAL / FAIL]| [BLOCKED / CONDITIONAL / ADVISORY] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1
```
g_null(post-domain) = [copy] | G_lifecycle = [copy]
Apply §9 Stage 3 --> g_null(final) = [verdict]
```

**Full CH-ID Saturation**:

| CH-ID  | DOMAIN | LIFECYCLE | Full Saturation |
|--------|--------|-----------|-----------------|
| CH-001 | [copy] | [copy]    | [FULLY SATURATED / UNSATURATED] |
| CH-002 | [copy] | [copy]    | [FULLY SATURATED / UNSATURATED] |

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**GClose Rationale**: [2-3 sentences.]

**Local Gate Ledger Row**:
| Section         | Gate   | Verdict                    | Class                              |
|-----------------|--------|----------------------------|------------------------------------|
| BRACKET CLOSING | GClose | [PASS / CONDITIONAL / FAIL]| [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION

*(EXCLUDED from gate ledger.)*

| IN-SCOPE Surface | Reviewer(s) | Coverage |
|-----------------|-------------|----------|
| [SURFACE_1]     | [ROLE]      | [COVERED / GAP] |

**Advisory items**: [list or "None"]

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract Cite |
|------|----------|---------|---------------|
| GOpen | [CHALLENGER] | [verdict] | DISPOSITION_CONTRACT v1 |
| G_domain_agg | [DOMAIN] | [verdict] | DISPOSITION_CONTRACT v1 |
| G_lifecycle | [LIFECYCLE] | [verdict] | DISPOSITION_CONTRACT v1 |
| GClose | [CHALLENGER] | [verdict] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [or "None."] | **Convergence**: [or "None."]
**§13 Progression Ledger**: g_null(initial)=[_] | g_null(post-domain)=[_] | g_null(final)=[_] | Trajectory=[_]

---

## DISPOSITION

Gate vector: GOpen=[_] | G_domain_agg=[_] | G_lifecycle=[_] | GClose=[_]
Apply §3: **Overall Disposition**: [BLOCKED / CONDITIONAL / READY]
**Primary Driver** *(per §16)*: [derived]
**RESOLUTION REGISTRY** *(per §12)*: [table or "N/A"]

---

## ACTION ITEM REGISTER

*(Verbatim copy per §6.)*

| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [copy] | [copy] |
| DOMAIN -- [ROLE] | G_domain | [copy] | [copy] |
| LIFECYCLE -- [ROLE] | G_lifecycle | [copy] | [copy] |
| BRACKET CLOSING | GClose | [copy] | [copy] |

**Advisory items** *(including §17 ADVISORY-GAP items)*:
- [list or "None"]

---

**Artifact to review:**

{{artifact}}

---

---

## V-05

**Axes**: Phrasing register + Output format + Role sequence -- §17a CERTIFICATION + §17 MATRIX + §18 PRE-ASSESSMENT + post-render criterion check (C-33+C-34+C-35 maximal)
**Hypothesis**: V-04 combines certification (C-33) and matrix (C-34) but omits C-35. V-03
demonstrates that extracting the NH dimension table into a standalone CHALLENGER PRE-ASSESSMENT
makes C-35 derivable from VERDICT column counts alone. V-05 combines all three mechanisms:
- §17 DOMAIN-ROLE COVERAGE MATRIX (C-33 evidence + C-34 gap detection)
- §17a APPLICABILITY CERTIFICATION (C-33 artifact-specificity verification)
- §18 CHALLENGER PRE-ASSESSMENT (C-35 standalone NH dimension table with VERDICT column)
The §7 SECTION ORDER CONTRACT is updated to include all three pre-reviewer sections.
The section numbering is: 1 ROLE MANIFEST, 1.5a MATRIX, 1.5b CERTIFICATION, 1.5c PRE-ASSESSMENT,
2 BRACKET OPENING. BRACKET OPENING inherits g_null(initial) from PRE-ASSESSMENT (§18).
A post-render CRITERION CHECK is added after ACTION ITEM REGISTER: the model verifies
C-33/C-34/C-35 satisfaction before the output is committed. If any criterion fails the check,
the relevant section is revised before the final output is delivered.

---

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .craft/roles/signal/
```

Emit this block first. Fill in injected values.

```
## Review Parameters
Artifact:     {{artifact_id}}
Depth:        {{depth}}
Reviewer set: {{reviewer_set}}
```

---

You are running `org-review` on the artifact provided below.

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any
pre-printed heading, label, field, formula, or structural element. If a field cannot
be filled, write `[N/A -- reason]`. After ACTION ITEM REGISTER, emit the CRITERION CHECK
block before delivering the final output.

---

```
======================================================================
DISPOSITION_CONTRACT v1
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§18;
reviewer sections may not execute until §1 COMPLETE and all three
pre-reviewer sections (MATRIX, CERTIFICATION, PRE-ASSESSMENT) COMPLETE]
======================================================================

§1 -- SCOPE ENUMERATION
IN-SCOPE:
  1. [SURFACE_1]   [DOMAIN: domain-label]
  2. [SURFACE_2]   [DOMAIN: domain-label]
  3. [SURFACE_3]   [DOMAIN: domain-label]

OUT-OF-SCOPE:
  1. [SURFACE -- REASON_EXCLUDED]

§1 COMPLETE.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH = Blocks. MEDIUM = Conditions. LOW = Advisory.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED <-- GClose=FAIL OR any Gi=FAIL
  CONDITIONAL <-- no FAIL AND any CONDITIONAL
  READY <-- all PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(all G_domain verdicts).

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section: "Contract: DISPOSITION_CONTRACT v1"

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Challenge claims receive CH-IDs. All downstream sections carry CH-ID response tables.
  PASS prohibited if any CH-ID = OPEN.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Row syntax: | Section | Gate | Verdict | Class |
  Class: FAIL->BLOCKED; CONDITIONAL->CONDITIONAL; PASS->ADVISORY.
  Emission: end of each verdict-emitting section.
  Assembly: verbatim copy to ACTION ITEM REGISTER. No re-derivation.
  EXCLUDED: §3.5, §3.8, §5.5, DOMAIN-ROLE COVERAGE MATRIX, APPLICABILITY CERTIFICATION
  BLOCK, CHALLENGER PRE-ASSESSMENT, CRITERION CHECK.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  1.    ROLE MANIFEST
  1.5a. DOMAIN-ROLE COVERAGE MATRIX        [per §17; no ledger row]
  1.5b. APPLICABILITY CERTIFICATION BLOCK  [per §17a; no ledger row]
  1.5c. CHALLENGER PRE-ASSESSMENT          [per §18; no ledger row]
  2.    BRACKET OPENING                    [inherits g_null(initial) from 1.5c]
  3.    DOMAIN(s)
  3.5.  DOMAIN-AGGREGATE CHECKPOINT
  3.8.  CH-ID SATURATION CHECK
  4.    LIFECYCLE
  5.    BRACKET CLOSING
  5.5.  SCOPE COVERAGE RECONCILIATION
  6.    GATE VECTOR TABLE
  7.    CROSS-ROLE SIGNALS
  8.    DISPOSITION
  9.    ACTION ITEM REGISTER
  10.   CRITERION CHECK                    [post-render; no ledger row]
  All pre-reviewer sections (1.5a, 1.5b, 1.5c) must precede BRACKET OPENING.
  CRITERION CHECK runs after ACTION ITEM REGISTER. If any criterion fails: revise before
  delivering output.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  SATURATED before LIFECYCLE. FULLY SATURATED before BRACKET CLOSING.
  PASS from BRACKET CLOSING prohibited without full saturation.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial) = output of §18 CHALLENGER PRE-ASSESSMENT formula.
    GOpen must equal g_null(initial). Conflict: emit "g_null CONFLICT: [values] -- [resolution]".
  Stage 2: g_null(post-domain): FAIL if G_domain_agg=FAIL;
    max(g_null(initial),CONDITIONAL) if CONDITIONAL; g_null(initial) if PASS.
  Stage 3: g_null(final): FAIL if G_lifecycle=FAIL;
    max(g_null(post-domain),CONDITIONAL) if CONDITIONAL; g_null(post-domain) if PASS.
  GClose = g_null(final) or override with justification.

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  §5.5 maps §1 surfaces. GAP -> ADVISORY-GAP in register.

§11 -- FINDING-SURFACE LINKAGE REQUIREMENT [IMMUTABLE]
  Each finding cites §1 surface. No citation = ADVISORY-ORPHAN.

§12 -- CONDITIONAL RESOLUTION REGISTRY CONTRACT [IMMUTABLE]
  DISPOSITION=CONDITIONAL: emit RESOLUTION REGISTRY after Overall Disposition.

§13 -- g_null PROGRESSION LEDGER REQUIREMENT [IMMUTABLE]
  CROSS-ROLE SIGNALS: g_null(initial) | g_null(post-domain) | g_null(final) | Trajectory.

§14 -- FINDING SEVERITY AGGREGATION CONTRACT [IMMUTABLE]
  Individual Severity per finding row. Section Severity = worst(all row severities).

§15 -- LENS EXHAUSTION REQUIREMENT [IMMUTABLE]
  Each DOMAIN/LIFECYCLE section: LENS COVERAGE TABLE. Applicability from §17 matrix
  (cell for this role x primary domain). OPEN + HIGH -> ADVISORY-OPEN-LENS.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  GClose=FAIL->GClose. G_domain=FAIL->DOMAIN. G_lifecycle=FAIL->LIFECYCLE.
  Any CONDITIONAL->lowest-index. All PASS->N/A.

§17 -- DOMAIN-ROLE COVERAGE MATRIX CONTRACT [IMMUTABLE]
  Rows: §1 domain labels. Columns: selected roles. Cells: HIGH / MEDIUM / LOW / --.
  DOMAIN-COVERED: >= 1 HIGH cell. DOMAIN-GAP: no HIGH cell -> ADVISORY-GAP in register.
  §15 Applicability: use matrix cell for (role, primary domain).

§17a -- APPLICABILITY CERTIFICATION REQUIREMENT [IMMUTABLE]
  After §17 MATRIX, emit CERTIFICATION BLOCK. One entry per role:
    Role [name]: Applicability = [tier from §17 matrix]
    Certification domain: [§1 domain label with highest matrix cell for this role]
    Lens.verify match: [specific entry from role definition]
    Artifact-specific basis: [one sentence naming a specific artifact characteristic]
  Generic justifications (no specific artifact characteristic) = invalid; revise matrix cell.

§18 -- CHALLENGER PRE-ASSESSMENT PROTOCOL [IMMUTABLE]
  After §17a CERTIFICATION, emit CHALLENGER PRE-ASSESSMENT. Output: g_null(initial).
  NH DIMENSION TABLE format:
    | Dimension | Current State | Proposed Build | Delta | NH Verdict |
  NH Verdict values: FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD (per dimension).
  g_null(initial) formula:
    F = count(FAVORS-BUILD); O = count(OPPOSES-BUILD)
    F > O -> PASS; F = O -> CONDITIONAL; F < O -> FAIL
  g_null(initial) is derivable from NH Verdict column counts without reading prose.
  BRACKET OPENING inherits g_null(initial) from PRE-ASSESSMENT. Does not re-derive.

§19 -- CRITERION CHECK PROTOCOL [IMMUTABLE]
  After ACTION ITEM REGISTER, emit CRITERION CHECK. For each criterion below, state
  whether THIS OUTPUT satisfies it (YES / NO / PARTIAL) and cite the evidence in this output.
  If any criterion = NO: return to the relevant section and revise before delivering output.
    C-33: Each LENS COVERAGE TABLE row carries an artifact-specific applicability rating
          from the §17 matrix and §17a certification. [YES/NO/PARTIAL -- cite evidence]
    C-34: All §1 domain labels appear in the §17 DOMAIN-ROLE COVERAGE MATRIX. Each DOMAIN-GAP
          row has a pre-registered ADVISORY-GAP item in ACTION ITEM REGISTER. [YES/NO/PARTIAL]
    C-35: CHALLENGER PRE-ASSESSMENT contains NH DIMENSION TABLE with NH Verdict column.
          g_null(initial) is stated as a labeled field derivable from verdict counts alone.
          [YES/NO/PARTIAL -- cite NH Verdict counts F and O]

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================
```

---

## ROLE MANIFEST

Read `.craft/roles/signal/`. Assign each slot.

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

---

## DOMAIN-ROLE COVERAGE MATRIX

*(Per §17 -- step 1.5a. No ledger row.)*

| Artifact Domain | [CHALLENGER_ROLE] | [DOMAIN_ROLE] | [LIFECYCLE_ROLE] | Gap Status |
|-----------------|-------------------|---------------|------------------|-----------|
| [domain-label-1] | [HIGH/MED/LOW/--] | [HIGH/MED/LOW/--] | [HIGH/MED/LOW/--] | [COVERED/GAP] |
| [domain-label-2] | [HIGH/MED/LOW/--] | [HIGH/MED/LOW/--] | [HIGH/MED/LOW/--] | [COVERED/GAP] |
| [domain-label-3] | [HIGH/MED/LOW/--] | [HIGH/MED/LOW/--] | [HIGH/MED/LOW/--] | [COVERED/GAP] |

**Pre-registered ADVISORY-GAP items**: [list DOMAIN-GAP rows or "None"]

---

## APPLICABILITY CERTIFICATION BLOCK

*(Per §17a -- step 1.5b. No ledger row.)*

Role [challenger name]: Applicability = HIGH
Certification domain: [§1 domain label]
Lens.verify match: [specific entry from role definition]
Artifact-specific basis: [one sentence naming a specific artifact characteristic]

Role [domain name]: Applicability = [HIGH / MEDIUM / LOW]
Certification domain: [§1 domain label]
Lens.verify match: [specific entry from role definition]
Artifact-specific basis: [one sentence naming a specific artifact characteristic]

Role [lifecycle name]: Applicability = [HIGH / MEDIUM / LOW]
Certification domain: [§1 domain label]
Lens.verify match: [specific entry from role definition]
Artifact-specific basis: [one sentence naming a specific artifact characteristic]

---

## CHALLENGER PRE-ASSESSMENT

*(Per §18 -- step 1.5c. Output: g_null(initial). No ledger row.)*

**NH DIMENSION TABLE**:

| Dimension | Current State | Proposed Build | Delta | NH Verdict |
|-----------|--------------|---------------|-------|-----------|
| [DIM-1]   | [current]    | [with artifact]| [+/-/=] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-2]   | [current]    | [with artifact]| [+/-/=] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |
| [DIM-3]   | [current]    | [with artifact]| [+/-/=] | [FAVORS-BUILD / NEUTRAL / OPPOSES-BUILD] |

**Applying §18 formula**:
```
F (FAVORS-BUILD) = [_]
O (OPPOSES-BUILD) = [_]
F > O? PASS.  F = O? CONDITIONAL.  F < O? FAIL.
g_null(initial) = [PASS / CONDITIONAL / FAIL]
```

**g_null(initial)**: [PASS / CONDITIONAL / FAIL]
*(Derivable from F and O counts above. Carries forward to BRACKET OPENING.)*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [What the team does today instead of building this.]
**g_null(initial) from CHALLENGER PRE-ASSESSMENT**: [copy -- do not re-derive]

**Challenge claims**:

| CH-ID  | Challenge Claim | Severity |
|--------|----------------|----------|
| CH-001 | [CLAIM_1]      | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2]      | [HIGH / MEDIUM / LOW] |
| CH-003 | [optional]     | [HIGH / MEDIUM / LOW] |

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
*(Must equal g_null(initial) per §9 Stage 1.)*
**GOpen Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section         | Gate  | Verdict                    | Class                              |
|-----------------|-------|----------------------------|------------------------------------|
| BRACKET OPENING | GOpen | [PASS / CONDITIONAL / FAIL]| [BLOCKED / CONDITIONAL / ADVISORY] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy]

**CH-ID Response Table**:

| CH-ID  | Challenge Claim (copy) | Domain Response | Status |
|--------|----------------------|-----------------|--------|
| CH-001 | [copy]               | [RESPONSE_1]    | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]               | [RESPONSE_2]    | [ADDRESSED / PARTIAL / OPEN] |

**Additional Findings**:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n]  | [FINDING_1] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n]  | [FINDING_2] | [HIGH / MEDIUM / LOW] |

**Section Severity** *(worst per §14)*: [HIGH / MEDIUM / LOW]

**LENS COVERAGE TABLE** *(Applicability from §17 matrix -- cell for this role x primary domain)*:

| # | lens.verify Entry | Applicability | Status | Finding Reference |
|---|------------------|--------------|--------|-------------------|
| 1 | [entry 1] | [from §17 matrix] | [ADDRESSED / OPEN] | [F-n] |
| 2 | [entry 2] | [from §17 matrix] | [ADDRESSED / OPEN] | [F-n] |

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section               | Gate     | Verdict                    | Class                              |
|-----------------------|----------|----------------------------|------------------------------------|
| DOMAIN -- [ROLE_NAME] | G_domain | [PASS / CONDITIONAL / FAIL]| [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT

*(EXCLUDED.)*
```
G_domain_agg = [worst] | g_null(post-domain) via §9 = [verdict]
```

---

## §3.8 CH-ID SATURATION CHECK

*(EXCLUDED.)*

| CH-ID | DOMAIN Status | Saturation |
|-------|--------------|------------|
| CH-001 | [status]    | [SATURATED / UNSATURATED] |
| CH-002 | [status]    | [SATURATED / UNSATURATED] |

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy] | G_domain Aggregate: [copy] | g_null(post-domain): [copy]

**CH-ID Response Table**:

| CH-ID  | Challenge Claim (copy) | Lifecycle Response | Status |
|--------|----------------------|-------------------|--------|
| CH-001 | [copy]               | [RESPONSE_1]      | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy]               | [RESPONSE_2]      | [ADDRESSED / PARTIAL / OPEN] |

**Additional Findings**:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n]  | [FINDING_1] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n]  | [FINDING_2] | [HIGH / MEDIUM / LOW] |

**Section Severity** *(worst per §14)*: [HIGH / MEDIUM / LOW]

**LENS COVERAGE TABLE** *(Applicability from §17 matrix)*:

| # | lens.verify Entry | Applicability | Status | Finding Reference |
|---|------------------|--------------|--------|-------------------|
| 1 | [entry 1] | [from §17 matrix] | [ADDRESSED / OPEN] | [F-n] |
| 2 | [entry 2] | [from §17 matrix] | [ADDRESSED / OPEN] | [F-n] |

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
**G_lifecycle Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section                  | Gate        | Verdict                    | Class                              |
|--------------------------|-------------|----------------------------|------------------------------------|
| LIFECYCLE -- [ROLE_NAME] | G_lifecycle | [PASS / CONDITIONAL / FAIL]| [BLOCKED / CONDITIONAL / ADVISORY] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1
```
g_null(post-domain) = [copy] | G_lifecycle = [copy]
Apply §9 Stage 3 --> g_null(final) = [verdict]
```

**Full CH-ID Saturation**:

| CH-ID  | DOMAIN | LIFECYCLE | Full Saturation |
|--------|--------|-----------|-----------------|
| CH-001 | [copy] | [copy]    | [FULLY SATURATED / UNSATURATED] |
| CH-002 | [copy] | [copy]    | [FULLY SATURATED / UNSATURATED] |

**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**GClose Rationale**: [2-3 sentences.]

**Local Gate Ledger Row**:
| Section         | Gate   | Verdict                    | Class                              |
|-----------------|--------|----------------------------|------------------------------------|
| BRACKET CLOSING | GClose | [PASS / CONDITIONAL / FAIL]| [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION

*(EXCLUDED from gate ledger.)*

| IN-SCOPE Surface | Reviewer(s) | Coverage |
|-----------------|-------------|----------|
| [SURFACE_1]     | [ROLE]      | [COVERED / GAP] |

**Advisory items**: [list or "None"]

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract Cite |
|------|----------|---------|---------------|
| GOpen | [CHALLENGER] | [verdict] | DISPOSITION_CONTRACT v1 |
| G_domain_agg | [DOMAIN] | [verdict] | DISPOSITION_CONTRACT v1 |
| G_lifecycle | [LIFECYCLE] | [verdict] | DISPOSITION_CONTRACT v1 |
| GClose | [CHALLENGER] | [verdict] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [or "None."] | **Convergence**: [or "None."]
**§13 Progression Ledger**: g_null(initial)=[_] | g_null(post-domain)=[_] | g_null(final)=[_] | Trajectory=[_]

---

## DISPOSITION

Gate vector: GOpen=[_] | G_domain_agg=[_] | G_lifecycle=[_] | GClose=[_]
Apply §3: **Overall Disposition**: [BLOCKED / CONDITIONAL / READY]
**Primary Driver** *(per §16)*: [derived mechanically]
**RESOLUTION REGISTRY** *(per §12)*: [table or "N/A"]

---

## ACTION ITEM REGISTER

*(Verbatim copy per §6.)*

| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [copy] | [copy] |
| DOMAIN -- [ROLE] | G_domain | [copy] | [copy] |
| LIFECYCLE -- [ROLE] | G_lifecycle | [copy] | [copy] |
| BRACKET CLOSING | GClose | [copy] | [copy] |

**Advisory items** *(ADVISORY-GAP from §17, ADVISORY-ORPHAN from §11, ADVISORY-OPEN-LENS from §15)*:
- [list or "None"]

---

## CRITERION CHECK

*(Per §19 -- post-render verification. Revise any NO criterion before delivering output.)*

| Criterion | Description | Status | Evidence in this output |
|-----------|-------------|--------|------------------------|
| C-33 | Each LENS COVERAGE TABLE row carries artifact-specific applicability rating from §17 matrix verified by §17a certification | [YES/NO/PARTIAL] | [cite: §17a certification block present; lens table rows carry matrix cell values] |
| C-34 | All §1 domain labels appear in §17 matrix; DOMAIN-GAP rows have ADVISORY-GAP items in ACTION ITEM REGISTER | [YES/NO/PARTIAL] | [cite: N domains in matrix; M DOMAIN-GAP rows; M ADVISORY-GAP items in register] |
| C-35 | CHALLENGER PRE-ASSESSMENT contains NH DIMENSION TABLE with NH Verdict column; g_null(initial) labeled field derivable from F and O counts alone | [YES/NO/PARTIAL] | [cite: F=N, O=M from PRE-ASSESSMENT table; g_null(initial) = [value]] |

*(Any criterion = NO: return to the relevant section (§17 matrix for C-33/C-34; §18 PRE-ASSESSMENT
for C-35) and revise before delivering output. Any criterion = PARTIAL: note the gap and proceed.)*

---

**Artifact to review:**

{{artifact}}
