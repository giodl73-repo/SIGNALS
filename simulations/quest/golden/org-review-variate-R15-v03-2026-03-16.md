## V-03 — Lifecycle Emphasis: Commitment-Readiness Matrix

**Variation axis**: Lifecycle emphasis — the LIFECYCLE section adds a mandatory
COMMITMENT-READINESS MATRIX covering four program dimensions (timeline, resources, rollback,
stakeholder alignment). The matrix produces a structured COMMITMENT-READINESS SIGNAL that
the reviewer must reference when stating G_lifecycle. Everything else is identical to V-01
baseline (three-column §17, §1 domain annotations, imperative instructions).

**Hypothesis**: The current LIFECYCLE section asks for a free-form "decision-readiness
assessment" paragraph. Without a structured scaffold, the AI tends to produce vague program
commentary that doesn't surface concrete blockers. A four-cell matrix forces explicit
gap-identification on each commitment dimension before the reviewer reaches a verdict.
G_lifecycle verdicts produced from a matrix are more traceable and harder to generate
generically.

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

**Instructions**: Fill every `[BRACKETED_FIELD]`. Do not alter, reorder, or omit any pre-printed
heading, label, field, formula, or structural element. Do not add sections between pre-printed
headers. If a field cannot be filled, write `[N/A -- reason]`.

---

```
======================================================================
DISPOSITION_CONTRACT v1
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§17;
reviewer sections may not execute until §1 COMPLETE marker is reached]
======================================================================

§1 -- SCOPE ENUMERATION
IN-SCOPE (cited in §5.5 SCOPE COVERAGE RECONCILIATION and §11 FINDING-SURFACE LINKAGE):
  Each surface must carry a [DOMAIN: label] annotation. Domain label consumed by §10a gap-check.
  1. [SURFACE_1] [DOMAIN: label]
  2. [SURFACE_2] [DOMAIN: label]
  3. [SURFACE_3] [DOMAIN: label]
  (Add rows. Be exhaustive. Every surface requires a domain annotation.)

OUT-OF-SCOPE:
  1. [SURFACE -- REASON_EXCLUDED]

Scope Amendment Protocol:
  SCOPE AMENDMENT: [surface] added to IN-SCOPE -- [reason]
  Silent scope expansion violates this contract.

§1 COMPLETE -- role selection, APPLICABILITY MATRIX, and reviewer gates proceed below.

§2 -- SEVERITY SEMANTICS [IMMUTABLE]
  HIGH   = Blocks commitment.
  MEDIUM = Conditions commitment. Proceeds only after named resolution.
  LOW    = Advisory. Commitment may proceed.
  These definitions apply universally.

§3 -- DISPOSITION ALGEBRA [IMMUTABLE]
  G = {GOpen, G_domain_agg, G_lifecycle, GClose}
  BLOCKED      <-- GClose=FAIL OR exists Gi=FAIL
  CONDITIONAL  <-- no Gi=FAIL AND exists Gi=CONDITIONAL
  READY        <-- all Gi=PASS

§3a -- DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(all G_domain rows). FAIL>CONDITIONAL>PASS.
  Single domain: G_domain_agg = G_domain (direct pass-through).

§4 -- CONTRACT CITE REQUIREMENT [IMMUTABLE]
  Each reviewer section opens with: "Contract: DISPOSITION_CONTRACT v1"
  A missing cite is an audit-trail gap.

§5 -- CH-ID TRACING REQUIREMENT [IMMUTABLE]
  Each challenge claim in BRACKET OPENING receives a CH-ID (CH-001, ...).
  Every downstream section carries a mandatory CH-ID response table.
  A PASS verdict is prohibited if any CH-ID row shows OPEN status.

§6 -- LOCAL GATE LEDGER PROTOCOL [IMMUTABLE]
  Row syntax: | Section | Gate | Verdict | Class |
  Class: FAIL->BLOCKED; CONDITIONAL->CONDITIONAL; PASS->ADVISORY.
  EXCLUDED (no row emitted): §3.5, §3.8, §5.5.

§7 -- SECTION ORDER CONTRACT [IMMUTABLE]
  1. ROLE MANIFEST (APPLICABILITY MATRIX required before BRACKET OPENING)
  2. BRACKET OPENING
  3. DOMAIN(s)
  3.5. DOMAIN-AGGREGATE CHECKPOINT
  3.8. CH-ID SATURATION CHECK
  4. LIFECYCLE
  5. BRACKET CLOSING
  5.5. SCOPE COVERAGE RECONCILIATION (surface table + DOMAIN COVERAGE GAP-CHECK)
  6. GATE VECTOR TABLE
  7. CROSS-ROLE SIGNALS
  8. DISPOSITION
  9. ACTION ITEM REGISTER
  Reordering any section violates this contract.

§8 -- CH-ID SATURATION REQUIREMENT [IMMUTABLE]
  FULLY SATURATED: CH-ID has received DOMAIN + LIFECYCLE responses before BRACKET CLOSING.
  PASS from BRACKET CLOSING is prohibited without full saturation or a stated waiver.
  Waiver: "CH-XXX WAIVER: [reason]"
  Waivers -> ACTION ITEM REGISTER as ADVISORY.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial) = output of §17 formula [emitted at BRACKET OPENING]
           [If §17 inactive: g_null(initial) = GOpen verdict directly]
  Stage 2: g_null(post-domain) [emitted at §3.5]:
    G_domain_agg=FAIL        -> g_null(post-domain)=FAIL
    G_domain_agg=CONDITIONAL -> g_null(post-domain)=max(g_null(initial), CONDITIONAL)
    G_domain_agg=PASS        -> g_null(post-domain)=g_null(initial)
  Stage 3: g_null(final) [emitted at BRACKET CLOSING]:
    G_lifecycle=FAIL         -> g_null(final)=FAIL
    G_lifecycle=CONDITIONAL  -> g_null(final)=max(g_null(post-domain), CONDITIONAL)
    G_lifecycle=PASS         -> g_null(final)=g_null(post-domain)
  GClose must equal g_null(final). Override: "g_null OVERRIDE: [justification]"
  Scale: FAIL < CONDITIONAL < PASS.

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  After BRACKET CLOSING, §5.5 maps each §1 IN-SCOPE surface to reviewer findings.
  Classification: COVERED (>=1 finding) or GAP (no finding).
  GAP surfaces -> ADVISORY-GAP in ACTION ITEM REGISTER.
  Gate signal COVERED/PARTIAL is informational; §5.5 emits no ledger row.
  §5.5 ALSO runs DOMAIN COVERAGE GAP-CHECK per §10a.

§10a -- DOMAIN COVERAGE GAP-CHECK PROTOCOL [IMMUTABLE]
  Embedded in §5.5, after the surface coverage table.
  Step 1: Group §1 IN-SCOPE surfaces into ARTIFACT DOMAINS using [DOMAIN: label] annotations.
  Step 2: For each artifact domain, look up ROLE MANIFEST APPLICABILITY MATRIX rows where
          Artifact Domain Covered matches AND Artifact Applicability = HIGH.
  Step 3: Classify each artifact domain:
    COVERED    = at least one APPLICABILITY MATRIX row with HIGH rating covers this domain.
    ADVISORY-GAP = no APPLICABILITY MATRIX row with HIGH rating covers this domain.
  Step 4: ADVISORY-GAP domains -> ACTION ITEM REGISTER:
    Attribution: "DOMAIN COVERAGE GAP-CHECK / [domain] / no HIGH-applicability reviewer"
    Class: ADVISORY
  Table format:
    | Artifact Domain | HIGH-Applicability MATRIX Rows | Coverage |
  This check is informational. It does not feed the §3 formula or produce gate verdicts.

§11 -- FINDING-SURFACE LINKAGE REQUIREMENT [IMMUTABLE]
  Each finding in DOMAIN and LIFECYCLE sections carries a "[§1:S-n]" citation.
  Missing citation = ADVISORY-ORPHAN. ADVISORY-ORPHAN -> ACTION ITEM REGISTER.

§12 -- CONDITIONAL RESOLUTION REGISTRY CONTRACT [IMMUTABLE]
  DISPOSITION=CONDITIONAL -> emit RESOLUTION REGISTRY table (Gate/Condition/Owner/Criterion/OPEN).
  One row per CONDITIONAL gate. Resolution Criterion = falsifiable test.
  Else: "RESOLUTION REGISTRY: N/A -- disposition is [value]"

§13 -- g_null PROGRESSION LEDGER REQUIREMENT [IMMUTABLE]
  CROSS-ROLE SIGNALS: §13 PROGRESSION LEDGER sub-section:
    g_null(initial) | g_null(post-domain) | g_null(final) | Trajectory
  Labels: MONOTONIC-PASS / MONOTONIC-FAIL / DOMAIN-DEGRADED / LIFECYCLE-DEGRADED /
          DOMAIN-RECOVERED / LIFECYCLE-RECOVERED. Informational only.

§14 -- FINDING SEVERITY AGGREGATION CONTRACT [IMMUTABLE]
  Findings table: | # | §1 Surface | Finding | Severity |
  Section Severity = worst(all severities in section). HIGH>MEDIUM>LOW.
  No findings: Section Severity = LOW. Apply mechanically; do not assign editorially.

§15 -- LENS EXHAUSTION REQUIREMENT [IMMUTABLE]
  Each DOMAIN and LIFECYCLE section must address ALL entries from the role's lens.verify.
  After findings, emit LENS COVERAGE TABLE:
    | # | lens.verify Entry | Applicability (from ROLE MANIFEST) | Status | Finding Reference |
  Applicability column: cite the APPLICABILITY MATRIX row ID and tier from the ROLE MANIFEST.
  Do NOT assign applicability inline. The value must match the pre-committed APPLICABILITY MATRIX.
  Status: ADDRESSED / OPEN.
  HIGH applicability + OPEN -> ADVISORY-OPEN-LENS-REQUIRED in ACTION ITEM REGISTER.
  MEDIUM applicability + OPEN -> ADVISORY-OPEN-LENS in ACTION ITEM REGISTER.
  LOW applicability + OPEN -> no register entry; cite AM row in Finding Reference.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  Mechanical precedence rule at DISPOSITION:
    1. GClose=FAIL        -> Primary Driver = BRACKET CLOSING  [override]
    2. G_domain_agg=FAIL  -> Primary Driver = DOMAIN
    3. G_lifecycle=FAIL   -> Primary Driver = LIFECYCLE
    4. GOpen=FAIL         -> Primary Driver = BRACKET OPENING
    5. GClose=CONDITIONAL -> Primary Driver = BRACKET CLOSING  [partial defeat]
    6. G_domain_agg=CONDITIONAL -> DOMAIN
    7. G_lifecycle=CONDITIONAL  -> LIFECYCLE
    8. GOpen=CONDITIONAL        -> BRACKET OPENING
    9. all PASS           -> N/A
  Emit: **Applying §16 rule**: [n + reason]  **Primary Driver**: [result]

§17 -- NULL HYPOTHESIS DIMENSION TABLE CONTRACT [IMMUTABLE]
  BRACKET OPENING challenger evaluates the null hypothesis via a three-column per-dimension
  comparison table before stating challenge claims. Table is SEPARATE from the §16 alternatives
  table. When the alternatives table has three or more options, the NH dimension table includes
  three comparison columns.

  Table format (three comparison columns):
    | Dimension | Status-Quo Score (A,0-10) | Proposed-Build Score (B,0-10) | Best-Non-Build-Alt Score (C,0-10) | D1=(B-A) | D2=(B-C) | NH Verdict |
  MUST-CLEAR dimensions marked (*). Minimum 3 dimensions.

  NULL HYPOTHESIS DERIVATION RULE (pre-committed; apply mechanically):
    Per-row NH Verdict:
      FAVORS-BUILD    <-- D1 > 0 AND D2 > 0
      CONDITIONAL     <-- D1 > 0 AND D2 <= 0  (improves over status-quo; not over best alt)
      OPPOSES-BUILD   <-- D1 <= 0              (fails to improve over status quo)
    g_null verdict:
      HOLDS           <-- any MUST-CLEAR row NH Verdict = OPPOSES-BUILD
      CONDITIONAL     <-- no MUST-CLEAR OPPOSES-BUILD AND
                          count(FAVORS-BUILD) <= count(OPPOSES-BUILD) + count(CONDITIONAL)
      DEFEATED        <-- no MUST-CLEAR OPPOSES-BUILD AND
                          count(FAVORS-BUILD) > count(OPPOSES-BUILD) + count(CONDITIONAL)
    DEFEATED requires BOTH D1 AND D2 positive majority. Positive D1 alone is insufficient.

  NH TABLE AGGREGATION RULE (governs bracket closing re-population; apply mechanically):
    Column A (Status-Quo): challenger's original opening score per dimension, carried forward.
      Rationale: status-quo baseline is control arm; no reviewer testimony revises current state.
    Column B (Proposed-Build): arithmetic average of all domain reviewer B scores per dimension.
      Formula: avg(domain_reviewer_B_scores_for_this_dimension)
    Column C (Best-Non-Build-Alt): arithmetic average of all domain reviewer C scores per dimension.
      Formula: avg(domain_reviewer_C_scores_for_this_dimension)
    All three column derivations are pre-committed. No editorial selection at bracket closing.

  BRACKET CLOSING re-applies §17 rule to REVISED NH DIMENSION TABLE (values per AGGREGATION RULE).
  The revised table's NH Verdict column is the sole input to g_null(final) derivation.
  §9 Stage 1 g_null(initial) = §17 formula output at BRACKET OPENING.

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================
```

---

## ROLE MANIFEST

Read `.craft/roles/signal/`. Assign each slot.

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (bracket open + close -- fixed) | inertia-advocate | [ROLE_NAME] | [ONE_SENTENCE] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [ONE_SENTENCE] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [ONE_SENTENCE] |

*(For `--depth deep`: add DOMAIN-2, DOMAIN-3. Each adds rows to APPLICABILITY MATRIX.)*

### APPLICABILITY MATRIX

*(REQUIRED before BRACKET OPENING executes. Locked after this point. Referenced by §15 and §10a.)*

| Row ID | Role | lens.verify Entry | Artifact Domain Covered | Artifact Applicability | Basis for Rating |
|--------|------|------------------|------------------------|----------------------|------------------|
| AM-01 | [DOMAIN ROLE] | [Full text lens.verify entry 1] | [domain name] | [HIGH / MEDIUM / LOW] | [One sentence] |
| AM-02 | [DOMAIN ROLE] | [Full text lens.verify entry 2] | [domain name] | [HIGH / MEDIUM / LOW] | [One sentence] |
| AM-03 | [DOMAIN ROLE] | [Full text lens.verify entry 3 if present] | [domain name] | [HIGH / MEDIUM / LOW] | [One sentence] |
| AM-04 | [LIFECYCLE ROLE] | [Full text lens.verify entry 1] | [domain name] | [HIGH / MEDIUM / LOW] | [One sentence] |
| AM-05 | [LIFECYCLE ROLE] | [Full text lens.verify entry 2] | [domain name] | [HIGH / MEDIUM / LOW] | [One sentence] |

*(Add rows for every lens.verify entry from every assigned role. Matrix is now locked.)*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**Null hypothesis**: [What the team does today instead of building this -- one sentence.]

**Alternatives comparison table** *(>= 3 dimensions; distinct from §17 below)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|---------------|-----------|----------------------|-------|
| [DIM-1] | [score] | [score] | [score] | |
| [DIM-2] | [score] | [score] | [score] | |
| [DIM-3] | [score] | [score] | [score] | |

**NULL HYPOTHESIS DIMENSION TABLE** *(per §17 -- three columns; DEFEATED requires D1 AND D2 positive majority)*:

| Dimension | Status-Quo Score (A) | Proposed-Build Score (B) | Best-Non-Build-Alt Score (C) | D1=(B-A) | D2=(B-C) | NH Verdict |
|-----------|---------------------|--------------------------|------------------------------|----------|----------|------------|
| [DIM-A*]  | [N] | [M] | [P] | [M-N] | [M-P] | [FAVORS-BUILD / CONDITIONAL / OPPOSES-BUILD] |
| [DIM-B*]  | [N] | [M] | [P] | [M-N] | [M-P] | [FAVORS-BUILD / CONDITIONAL / OPPOSES-BUILD] |
| [DIM-C]   | [N] | [M] | [P] | [M-N] | [M-P] | [FAVORS-BUILD / CONDITIONAL / OPPOSES-BUILD] |

**Applying §17 g_null derivation rule**:
```
MUST-CLEAR rows with OPPOSES-BUILD: [list or "none"]
count(FAVORS-BUILD) = [N]  count(CONDITIONAL) = [N]  count(OPPOSES-BUILD) = [N]
DEFEATED: count(FAVORS-BUILD) > count(OPPOSES-BUILD) + count(CONDITIONAL) AND no MUST-CLEAR OPPOSES? [Y/N]
Result: [HOLDS / CONDITIONAL / DEFEATED]
```
**g_null(initial)** *(§9 Stage 1)*: [HOLDS / CONDITIONAL / DEFEATED]

**Challenge claims**:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | [CLAIM_1] | [HIGH / MEDIUM / LOW] |
| CH-002 | [CLAIM_2] | [HIGH / MEDIUM / LOW] |
| CH-003 | [CLAIM_3 -- optional] | [HIGH / MEDIUM / LOW] |

**Verify Question**: [One from challenger's `lens.verify`.]
**Simplify**: [One from challenger's `lens.simplify`.]

**GOpen Verdict**: [PASS / CONDITIONAL / FAIL]
**GOpen Reason**: [One sentence.]
**g_null(initial)**: [copy from §17 derivation]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy from BRACKET OPENING]

**CH-ID Response Table**:

| CH-ID | Challenge Claim (copy) | This Role's Technical Response | Status |
|-------|----------------------|-------------------------------|--------|
| CH-001 | [copy] | [RESPONSE_1] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

**Domain re-score**:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Rationale |
|-----------|---------------|-----------|----------------------|-----------|
| [DIM-1] | [revised] | [revised] | [revised] | [reason] |
| [DIM-2] | [revised] | [revised] | [revised] | |
| [DIM-3] | [revised] | [revised] | [revised] | |

**NH Dimension Scores** *(per §17 NH TABLE AGGREGATION RULE -- consumed by BRACKET CLOSING)*:

| Dimension | This Reviewer's Proposed-Build Score (B) | This Reviewer's Best-Non-Build-Alt Score (C) |
|-----------|------------------------------------------|----------------------------------------------|
| [DIM-A] | [score 0-10] | [score 0-10] |
| [DIM-B] | [score 0-10] | [score 0-10] |
| [DIM-C] | [score 0-10] | [score 0-10] |

**Additional Findings**:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |
| F-3 | [§1:S-n -- optional] | [FINDING_3] | [HIGH / MEDIUM / LOW] |

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_], ...) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW]

**Lens Coverage Table**:

| # | lens.verify Entry | Applicability (from ROLE MANIFEST) | Status | Finding Reference |
|---|------------------|-----------------------------------|--------|-------------------|
| Q-1 | [Full text entry 1] | AM-01: [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or AM-01 basis] |
| Q-2 | [Full text entry 2] | AM-02: [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or cite AM-02] |
| Q-3 | [Full text entry 3] | AM-03: [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or cite AM-03] |

**Recommendation**: [One concrete action.]
**Simplify**: [One from this role's `lens.simplify`.]

**G_domain Verdict**: [PASS / CONDITIONAL / FAIL]
**G_domain Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT

*(EXCLUDED from gate ledger per §6.)*

**Applying §3a formula**:
```
G_domain rows collected:
  DOMAIN -- [ROLE_NAME]: [verdict]
G_domain_agg = worst([list]) = [PASS / CONDITIONAL / FAIL]
```
**G_domain Aggregate**: [PASS / CONDITIONAL / FAIL]

**Applying §9 Stage 2 formula**:
```
g_null(initial) = [copy] | G_domain_agg = [copy]
  FAIL->FAIL | CONDITIONAL->max(initial,CONDITIONAL) | PASS->g_null(initial)
g_null(post-domain) = [result]
```
**g_null(post-domain)**: [FAIL / CONDITIONAL / PASS]

---

## §3.8 CH-ID SATURATION CHECK

*(EXCLUDED from gate ledger.)*

| CH-ID | DOMAIN Response Status | Pre-LIFECYCLE Saturation |
|-------|------------------------|--------------------------|
| CH-001 | [copy from DOMAIN] | [SATURATED / UNSATURATED] |
| CH-002 | [copy] | [SATURATED / UNSATURATED] |
| CH-003 | [copy if active] | [SATURATED / UNSATURATED or N/A] |

**Pre-LIFECYCLE unsaturated CH-IDs**: [List or "None"]

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [copy from BRACKET OPENING]
Received G_domain Aggregate: [copy from §3.5]
Received g_null(post-domain): [copy from §3.5]

**CH-ID Response Table**:

| CH-ID | Challenge Claim (copy) | This Role's Commitment-Frame Response | Status |
|-------|----------------------|--------------------------------------|--------|
| CH-001 | [copy] | [RESPONSE_1] | [ADDRESSED / PARTIAL / OPEN] |
| CH-002 | [copy] | [RESPONSE_2] | [ADDRESSED / PARTIAL / OPEN] |
| CH-003 | [copy if active] | [RESPONSE_3] | [ADDRESSED / PARTIAL / OPEN] |

**V-03 AXIS: COMMITMENT-READINESS MATRIX** *(complete before verdict; each row feeds G_lifecycle)*:

| CRM Dimension | Current State | Required State for Commitment | Gap | Severity |
|---------------|--------------|-------------------------------|-----|---------|
| Timeline | [current milestone state or estimated delivery] | [what timeline is needed for commitment to proceed safely] | [description of gap or "None"] | [HIGH / MEDIUM / LOW] |
| Resources | [current team allocation / budget state] | [what resource allocation is required] | [gap or "None"] | [HIGH / MEDIUM / LOW] |
| Rollback | [current rollback plan status] | [what rollback plan is required for commitment] | [gap or "None"] | [HIGH / MEDIUM / LOW] |
| Stakeholder Alignment | [current stakeholder buy-in state] | [alignment required before commitment] | [gap or "None"] | [HIGH / MEDIUM / LOW] |

**CRM Severity Aggregation**:
```
worst(Timeline=[_], Resources=[_], Rollback=[_], Stakeholder=[_]) = [CRM_SEVERITY]
```
**CRM Signal**: [CRM_SEVERITY -- HIGH / MEDIUM / LOW]
*(HIGH -> G_lifecycle cannot be PASS unless addressed. MEDIUM -> G_lifecycle cannot be PASS without
named condition. LOW -> advisory; G_lifecycle may be PASS with noted caveats.)*

**Decision-readiness assessment**: [One paragraph. Reference GOpen, G_domain Aggregate,
g_null(post-domain), and CRM Signal explicitly.]

**Null hypothesis status**: [yes / partial / no -- reference g_null(post-domain). One sentence.]

**Additional Findings** *(per §14 and §11 -- CRM gaps that rise to HIGH/MEDIUM should appear as findings)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [FINDING_1 -- commitment, program, or CRM concern.] | [HIGH / MEDIUM / LOW] |
| F-2 | [§1:S-n] | [FINDING_2] | [HIGH / MEDIUM / LOW] |

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_]) = [SECTION_SEVERITY]
```
**Section Severity**: [HIGH / MEDIUM / LOW]

**Lens Coverage Table**:

| # | lens.verify Entry | Applicability (from ROLE MANIFEST) | Status | Finding Reference |
|---|------------------|-----------------------------------|--------|-------------------|
| Q-1 | [Full text entry 1] | AM-04: [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or cite AM-04] |
| Q-2 | [Full text entry 2] | AM-05: [HIGH / MEDIUM / LOW] | [ADDRESSED / OPEN] | [F-n or cite AM-05] |

**Recommendation**: [One concrete action.]
**Simplify**: [One from this role's `lens.simplify`.]

**G_lifecycle Verdict**: [PASS / CONDITIONAL / FAIL]
*(CRM Signal=HIGH -> FAIL unless waived. CRM Signal=MEDIUM -> CONDITIONAL unless resolved.)*
**G_lifecycle Reason**: [One sentence. If CRM drove the verdict, cite the specific CRM dimension.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| LIFECYCLE -- [ROLE_NAME] | G_lifecycle | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1
*Full record received: scope declaration, APPLICABILITY MATRIX, all CH-ID tables, all verdicts.*

**Applying §9 Stage 3 formula**:
```
g_null(post-domain) = [copy from §3.5]
G_lifecycle         = [copy from LIFECYCLE ledger]
  FAIL->FAIL | CONDITIONAL->max(post-domain,CONDITIONAL) | PASS->g_null(post-domain)
g_null(final) = [result]
```
**g_null(final)**: [FAIL / CONDITIONAL / PASS]
*GClose must equal g_null(final) per §9.*

**Revised NULL HYPOTHESIS DIMENSION TABLE** *(per §17 + NH TABLE AGGREGATION RULE)*:

| Dimension | Status-Quo Score (A) | Proposed-Build Score (B) | Best-Non-Build-Alt Score (C) | D1=(B-A) | D2=(B-C) | NH Verdict |
|-----------|---------------------|--------------------------|------------------------------|----------|----------|------------|
| [DIM-A*]  | [A: carry from opening] | [B: avg domain B] | [C: avg domain C] | [D1] | [D2] | [FAVORS-BUILD / CONDITIONAL / OPPOSES-BUILD] |
| [DIM-B*]  | [A: carry from opening] | [B: avg domain B] | [C: avg domain C] | [D1] | [D2] | [FAVORS-BUILD / CONDITIONAL / OPPOSES-BUILD] |
| [DIM-C]   | [A: carry from opening] | [B: avg domain B] | [C: avg domain C] | [D1] | [D2] | [FAVORS-BUILD / CONDITIONAL / OPPOSES-BUILD] |

**NH AGGREGATION RULE APPLIED**:
```
Column A: challenger opening values carried forward (control arm -- unchanged)
Column B: avg domain B scores -- [DIM-A]: avg([scores])=[result] | [DIM-B]: avg=[result] | [DIM-C]: avg=[result]
Column C: avg domain C scores -- [DIM-A]: avg([scores])=[result] | [DIM-B]: avg=[result] | [DIM-C]: avg=[result]
```

**Applying §17 g_null derivation rule to revised table**:
```
MUST-CLEAR rows with OPPOSES-BUILD: [list or "none"]
count(FAVORS-BUILD)=[N]  count(CONDITIONAL)=[N]  count(OPPOSES-BUILD)=[N]
DEFEATED: count(FAVORS-BUILD) > count(OPPOSES-BUILD) + count(CONDITIONAL) AND no MUST-CLEAR OPPOSES? [Y/N]
Result: [HOLDS / CONDITIONAL / DEFEATED]
```

**Revised alternatives table**:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Domain Agg Rationale |
|-----------|---------------|-----------|----------------------|---------------------|
| [DIM-1] | [agg] | [agg] | [agg] | [reason] |
| [DIM-2] | [agg] | [agg] | [agg] | |

**Full CH-ID Saturation Check** *(per §8)*:

| CH-ID | DOMAIN Status | LIFECYCLE Status | Full Saturation | Waiver (if needed) |
|-------|--------------|-----------------|-----------------|---------------------|
| CH-001 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [WAIVER or N/A] |
| CH-002 | [copy] | [copy] | [FULLY SATURATED / UNSATURATED] | [WAIVER or N/A] |
| CH-003 | [copy if active] | [copy] | [FULLY SATURATED / UNSATURATED] | [WAIVER or N/A] |

**CH-ID Final Assessment**:

| CH-ID | G_domain Status | G_lifecycle Status | Final Status | Notes |
|-------|----------------|-------------------|--------------|-------|
| CH-001 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | |
| CH-002 | [copy] | [copy] | [DEFEATED / PARTIAL / HOLDS] | |
| CH-003 | [copy if active] | [copy] | [DEFEATED / PARTIAL / HOLDS] | |

**Remaining gaps**: [All defeated, or list.]
**GClose Verdict**: [PASS / CONDITIONAL / FAIL]
**Override invoked**: [YES / NO]
**g_null Override**: [N/A -- formula applied | or justification]
**GClose Rationale**: [2-3 sentences. Reference g_null(final), CH-ID saturation, CRM Signal from LIFECYCLE, trajectory.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [PASS / CONDITIONAL / FAIL] | [BLOCKED / CONDITIONAL / ADVISORY] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION

*(EXCLUDED from gate ledger per §6.)*

### Surface Coverage *(per §10)*

| IN-SCOPE Surface | Reviewer(s) | Finding Reference(s) | Coverage |
|-----------------|-------------|---------------------|----------|
| [§1 SURFACE_1] | [ROLE or "none"] | [F-n or N/A] | [COVERED / GAP] |
| [§1 SURFACE_2] | [ROLE or "none"] | [ref] | [COVERED / GAP] |
| [§1 SURFACE_3] | [ROLE or "none"] | [ref] | [COVERED / GAP] |

**Surface coverage gate signal**: [COVERED / PARTIAL -- [N] surface(s) not addressed]

### Domain Coverage Gap-Check *(per §10a)*

| Artifact Domain | HIGH-Applicability MATRIX Rows | Coverage |
|----------------|-------------------------------|----------|
| [DOMAIN-1 per §1 annotation] | [AM-0n: [ROLE] -- "[entry summary]" / "none"] | [COVERED / ADVISORY-GAP] |
| [DOMAIN-2] | [AM-0n / "none"] | [COVERED / ADVISORY-GAP] |

**§11 ADVISORY-ORPHAN check**: [List orphaned findings, or "None detected."]

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract Cite |
|------|----------|---------|---------------|
| GOpen -- bracket opening | [CHALLENGER_ROLE] | [copy] | DISPOSITION_CONTRACT v1 |
| G_domain_agg -- domain aggregate | [DOMAIN_ROLE(S)] | [copy] | DISPOSITION_CONTRACT v1 |
| G_lifecycle -- lifecycle | [LIFECYCLE_ROLE] | [copy] | DISPOSITION_CONTRACT v1 |
| GClose -- bracket closing | [CHALLENGER_ROLE] | [copy] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [Incompatible assessments across roles, or "None detected."]

**Convergence**: [Concern raised by 2+ reviewers independently. Name it and state confidence level.]

**Scope coverage**: [Uncovered §1 surfaces, or "None."]

**§13 PROGRESSION LEDGER**:
```
g_null(initial)     = [copy]
g_null(post-domain) = [copy]
g_null(final)       = [copy]
Trajectory:         [MONOTONIC-PASS / MONOTONIC-FAIL / DOMAIN-DEGRADED / LIFECYCLE-DEGRADED /
                     DOMAIN-RECOVERED / LIFECYCLE-RECOVERED]
```

---

## DISPOSITION

**Gate vector**:
- GOpen = [copy]  |  G_domain_agg = [copy]  |  G_lifecycle = [copy]  |  GClose = [copy]

**Apply contract §3 formula**:
```
GClose=FAIL? -> BLOCKED | any Gi=FAIL? -> BLOCKED | any CONDITIONAL? -> CONDITIONAL | all PASS? -> READY
```

**Overall Disposition**: [READY / CONDITIONAL / BLOCKED]

**Applying §16 rule**: [rule n + reason]
**Primary Driver**: [BRACKET CLOSING / DOMAIN / LIFECYCLE / BRACKET OPENING / N/A]

**Conditions** *(only if CONDITIONAL)*: [List per-gate conditions.]

**Blocker** *(only if BLOCKED)*: [Specific finding from FAIL gate.]

**RESOLUTION REGISTRY** *(only if CONDITIONAL)*:
| Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status |
|------|------------------|-----------------|---------------------|--------|
| [gate] | [one sentence] | [role] | [falsifiable test] | OPEN |

*If not CONDITIONAL: "RESOLUTION REGISTRY: N/A -- disposition is [value]"*

---

## ACTION ITEM REGISTER

| Source | CH-ID / Finding | Item Description | Disposition Class | Owner Role | Resolution Criterion |
|--------|----------------|-----------------|------------------|------------|---------------------|
| [gate ledger copy] | -- | [Section / Gate / Verdict / Class verbatim] | [class] | [ROLE] | [criterion] |
| [CH-ID] | CH-00n | [PARTIAL/HOLDS resolution required] | [class] | [ROLE] | [criterion] |
| [lens HIGH] | AM-0n / Q-n | ADVISORY-OPEN-LENS-REQUIRED: [entry] not addressed | ADVISORY | [ROLE] | Produce finding. |
| [lens MED] | AM-0n / Q-n | ADVISORY-OPEN-LENS: [entry] not addressed | ADVISORY | [ROLE] | Address or justify. |
| [scope gap] | -- | ADVISORY-GAP: §1 surface [name] not covered | ADVISORY | [ROLE] | Assign reviewer. |
| [domain gap] | -- | ADVISORY-GAP (DOMAIN): [domain] no HIGH-applicability reviewer | ADVISORY | [ROLE] | Add reviewer or justify. |
| [orphan] | -- | ADVISORY-ORPHAN: [F-n] from [SECTION] lacks §1:S-n citation | ADVISORY | [ROLE] | Re-assign or remove. |

---

**Artifact to review:**

{{artifact}}
