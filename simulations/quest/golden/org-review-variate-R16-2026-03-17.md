---
skill: quest-variate
skill_target: org-review
date: 2026-03-17
round: 16
rubric: org-review-rubric-v11-2026-03-16.md
variants: V-01 V-02 V-03 V-04 V-05
---

# org-review -- Variate R16 (2026-03-17)

**Base**: V-05 R15 (225/225 under v11 -- all C-01 through C-35 passing).
**Goal**: Explore post-225 candidate criteria for future rubric versions.

**Variation axes selected:**
- V-01: Inertia framing -- §0 NULL HYPOTHESIS CHARTER as pre-contract immutable block
- V-02: Output format -- Global F-ID namespace (cross-section finding IDs)
- V-03: Lifecycle emphasis -- LIFECYCLE emits NH Dimension Score sub-table (candidate C-41)
- V-04: Inertia framing + Output format (V-01 + V-02)
- V-05: All three axes (V-01 + V-02 + V-03)

---

## V-01

**Axis**: Inertia framing -- §0 NULL HYPOTHESIS CHARTER as a pre-DISPOSITION_CONTRACT
immutable block.

**Hypothesis**: The DISPOSITION_CONTRACT currently pre-commits disposition algebra, class
derivation, severity semantics, and NH progression. But the challenger's *specific case* --
the named status-quo state and the evidence threshold required to defeat it -- is not
pre-committed. §0 closes this gap: before the contract executes, the challenger names their
best null argument (three arguments, §0:Arg-1 through §0:Arg-3) and states the minimum
evidence bar each requires. Downstream: each challenge claim carries a §0:Arg-n citation;
BRACKET CLOSING emits a Charter Coverage Audit showing COVERED vs. CHARTER-GAP per argument.
CHARTER-GAP arguments enter the ACTION ITEM REGISTER as ADVISORY-CHARTER-GAP items.
Candidate C-41: NH Charter Reference Completeness.

---

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .roles/signal/
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

You will play four roles in sequence: an inertia-advocate challenger who opens the review by
defending the status quo, a domain-expert reviewer who evaluates the artifact's technical
surface, a lifecycle/program reviewer who assesses commitment readiness, and the challenger
again at closing who integrates all testimony to reach a final verdict on the null hypothesis.

The challenger's default is that the artifact should NOT be built. This review is the evidence
process that can overcome that prior. The domain reviewer provides technical evidence. The
lifecycle reviewer provides program and commitment evidence. Only after all evidence is in does
the challenger determine whether the inertia bar has been cleared.

Fill in all required fields by deriving findings from the artifact. Do not invent findings.
If a field is not applicable, write "N/A -- " followed by the reason. Do not alter, reorder,
or omit any pre-printed heading, label, formula, or structural element in the contract below.

---

```
======================================================================
§0 -- NULL HYPOTHESIS CHARTER [IMMUTABLE -- complete before DISPOSITION_CONTRACT]
======================================================================

The challenger commits their best null case here, before any contract executes.
Every challenge claim in BRACKET OPENING must cite one §0 argument via [§0:Arg-n].
A claim that cannot cite an §0 argument is CHARTER-ORPHAN and must be flagged.
BRACKET CLOSING emits a Charter Coverage Audit over these arguments.

Null statement (one sentence): What does the team currently do instead of building this?
  [NULL_STATEMENT]

Charter arguments (minimum two, maximum five):
  §0:Arg-1 -- [Name the first null argument. State the concrete advantage of the status quo
              on this dimension. State the minimum evidence that would defeat this argument.]
  §0:Arg-2 -- [Second argument. Same format.]
  §0:Arg-3 -- [Third argument, or omit if fewer than three are meaningful.]

Defeat threshold (pre-committed):
  This null hypothesis is defeated only when: ALL of the following hold --
    (a) §17 g_null = DEFEATED (table formula applied mechanically)
    (b) BRACKET CLOSING emits Charter Coverage Audit with zero CHARTER-GAP arguments
    (c) CH-ID saturation is FULLY SATURATED per §8
  Failure of any condition forces CHARTER-GAP items into ACTION ITEM REGISTER.

§0 COMPLETE -- DISPOSITION_CONTRACT proceeds below.
======================================================================
```

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
  Each claim must also carry a [§0:Arg-n] citation from the NULL HYPOTHESIS CHARTER.
  A claim without §0 citation is CHARTER-ORPHAN; flag inline and add to ACTION ITEM REGISTER.
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
  comparison table before stating challenge claims.

  Table format (three comparison columns):
    | Dimension | Status-Quo Score (A,0-10) | Proposed-Build Score (B,0-10) | Best-Non-Build-Alt Score (C,0-10) | D1=(B-A) | D2=(B-C) | NH Verdict |
  MUST-CLEAR dimensions marked (*). Minimum 3 dimensions.

  NULL HYPOTHESIS DERIVATION RULE (pre-committed; apply mechanically):
    Per-row NH Verdict:
      FAVORS-BUILD    <-- D1 > 0 AND D2 > 0
      CONDITIONAL     <-- D1 > 0 AND D2 <= 0
      OPPOSES-BUILD   <-- D1 <= 0
    g_null verdict:
      HOLDS           <-- any MUST-CLEAR row NH Verdict = OPPOSES-BUILD
      CONDITIONAL     <-- no MUST-CLEAR OPPOSES-BUILD AND
                          count(FAVORS-BUILD) <= count(OPPOSES-BUILD) + count(CONDITIONAL)
      DEFEATED        <-- no MUST-CLEAR OPPOSES-BUILD AND
                          count(FAVORS-BUILD) > count(OPPOSES-BUILD) + count(CONDITIONAL)
    DEFEATED requires BOTH D1 AND D2 positive majority.

  NH TABLE AGGREGATION RULE (governs bracket closing re-population):
    Column A: challenger's opening score carried forward (status-quo is control arm).
    Column B: arithmetic average of all domain reviewer B scores per dimension.
    Column C: arithmetic average of all domain reviewer C scores per dimension.
    All three derivations are pre-committed. No editorial selection at bracket closing.

  BRACKET CLOSING re-applies §17 rule to REVISED NH DIMENSION TABLE.
  §9 Stage 1 g_null(initial) = §17 formula output at BRACKET OPENING.

§17a -- NULL HYPOTHESIS CHARTER COVERAGE AUDIT [IMMUTABLE]
  BRACKET CLOSING emits a Charter Coverage Audit table before GClose verdict:
    | §0 Arg | Argument Text (summary) | Addressed By | Coverage |
  Coverage: COVERED (at least one CH-ID claim cited this arg AND domain/lifecycle responded
            ADDRESSED or PARTIAL), or CHARTER-GAP (no CH-ID cited this arg, or all citees
            remain OPEN at closing).
  CHARTER-GAP arguments -> ACTION ITEM REGISTER as ADVISORY-CHARTER-GAP:
    Attribution: "CHARTER COVERAGE AUDIT / §0:Arg-n / [reason: no claim cited / all open]"
    Class: ADVISORY

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================
```

---

## ROLE MANIFEST

Read `.roles/signal/`. Choose the inertia-advocate as the challenger. Choose a domain
role whose lens.verify entries best match this artifact's technical surface. Choose a
lifecycle/program role focused on commitment readiness.

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (bracket open + close) | inertia-advocate | [ROLE_NAME] | One sentence on fit. |
| DOMAIN | technical/architecture | [ROLE_NAME] | One sentence on domain expertise. |
| LIFECYCLE | PM/program | [ROLE_NAME] | One sentence on commitment-readiness perspective. |

*(For `--depth deep`: add DOMAIN-2, DOMAIN-3.)*

### APPLICABILITY MATRIX

Complete this matrix now, before BRACKET OPENING. It is locked at this point. For each role,
list every lens.verify entry. Rate applicability HIGH (finding expected; OPEN -> register
entry REQUIRED), MEDIUM (finding expected; OPEN -> register entry), or LOW (not applicable;
state why; OPEN is acceptable). The Artifact Domain column groups entries by the domain they
cover, feeding the §10a gap-check.

| Row ID | Role | lens.verify Entry | Artifact Domain Covered | Artifact Applicability | Basis for Rating |
|--------|------|------------------|------------------------|----------------------|------------------|
| AM-01 | [DOMAIN ROLE] | Full text of first lens.verify entry. | Domain name. | HIGH / MEDIUM / LOW. | One sentence explaining the rating for this artifact. |
| AM-02 | [DOMAIN ROLE] | Full text of second entry. | Domain. | Tier. | Basis. |
| AM-03 | [DOMAIN ROLE] | Full text of third entry if present. | Domain. | Tier. | Basis. |
| AM-04 | [LIFECYCLE ROLE] | Full text of first lifecycle lens.verify entry. | Domain. | Tier. | Basis. |
| AM-05 | [LIFECYCLE ROLE] | Full text of second entry. | Domain. | Tier. | Basis. |

*(Add a row for every lens.verify entry from every assigned role. Matrix is now locked.)*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**STATUS QUO VIABILITY ASSESSMENT** *(complete before challenge claims)*

Before any challenge is issued, establish why the current state is a viable default.

| SQ-DIM | Current State Description | Why Current State Is Acceptable | Viability |
|--------|--------------------------|--------------------------------|-----------|
| [Dimension 1] | [What team does today.] | [Concrete advantage that would be lost.] | HIGH / MEDIUM / LOW |
| [Dimension 2] | [Current practice.] | [Advantage.] | [Viability.] |
| [Dimension 3] | [Current practice.] | [Advantage.] | [Viability.] |

**Overall SQ Viability**: VIABLE / MARGINAL / STRETCHED.

---

**Null hypothesis**: [One sentence: what the team currently does instead of building this.]

**Alternatives comparison table** *(score 0-10; at least 3 dimensions; distinct from §17)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|---------------|-----------|----------------------|-------|
| [Dim-1] | [Score] | [Score] | [Score] | |
| [Dim-2] | [Score] | [Score] | [Score] | |
| [Dim-3] | [Score] | [Score] | [Score] | |

**NULL HYPOTHESIS DIMENSION TABLE** *(per §17; DEFEATED requires BOTH D1 AND D2 positive majority)*:

| Dimension | Status-Quo Score (A) | Proposed-Build Score (B) | Best-Non-Build-Alt Score (C) | D1=(B-A) | D2=(B-C) | NH Verdict |
|-----------|---------------------|--------------------------|------------------------------|----------|----------|------------|
| [Dim-1*] | [Score] | [Score] | [Score] | [B-A] | [B-C] | [FAVORS-BUILD / CONDITIONAL / OPPOSES-BUILD] |
| [Dim-2*] | [Score] | [Score] | [Score] | [B-A] | [B-C] | [Verdict] |
| [Dim-3] | [Score] | [Score] | [Score] | [B-A] | [B-C] | [Verdict] |

**Applying §17 g_null derivation rule**:
```
MUST-CLEAR rows with OPPOSES-BUILD: [list or "none"]
count(FAVORS-BUILD)  = [N]
count(CONDITIONAL)   = [N]
count(OPPOSES-BUILD) = [N]
DEFEATED: count(FAVORS-BUILD) > count(OPPOSES-BUILD) + count(CONDITIONAL) AND no MUST-CLEAR OPPOSES? [Y/N]
Result: [HOLDS / CONDITIONAL / DEFEATED]
```
**g_null(initial)** *(§9 Stage 1)*: [HOLDS / CONDITIONAL / DEFEATED]

---

**Challenge claims** *(each claim cites SQ-DIM and §0:Arg-n; CHARTER-ORPHAN if §0 citation absent)*:

| CH-ID | Challenge Claim | SQ-DIM Referenced | §0 Arg | Severity |
|-------|----------------|-------------------|--------|---------|
| CH-001 | [Claim grounded in a SQ advantage.] | [SQ-DIM-n] | [§0:Arg-n] | HIGH / MEDIUM / LOW |
| CH-002 | [Second claim.] | [SQ-DIM-n] | [§0:Arg-n] | [Severity] |
| CH-003 | [Third claim or omit.] | [SQ-DIM-n] | [§0:Arg-n] | [Severity] |

**Verify Question**: [Most critical lens.verify question for this artifact.]
**Simplify**: [One lens.simplify suggestion.]

**GOpen Verdict**: PASS if g_null=DEFEATED. CONDITIONAL if CONDITIONAL. FAIL if HOLDS.
**GOpen Reason**: [One sentence citing which g_null result drove this verdict.]
**g_null(initial)** *(§9 Stage 1)*: Copy from §17 derivation above.

*GOpen, g_null(initial), and all CH-IDs carry forward to every downstream section.*

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [Verdict] | [Class per §6] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [Copy GOpen from BRACKET OPENING.]

**CH-ID Response Table**:

| CH-ID | Challenge Claim (copy verbatim) | Your Technical Assessment | Status |
|-------|----------------------|-------------------------------|--------|
| CH-001 | [Copy claim.] | [Technical assessment. Does artifact design address this?] | ADDRESSED / PARTIAL / OPEN |
| CH-002 | [Copy.] | [Assessment.] | [Status] |
| CH-003 | [Copy if active.] | [Assessment.] | [Status] |

**Domain re-score**:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Rationale |
|-----------|---------------|-----------|----------------------|-----------|
| [Copy from BRACKET OPENING.] | [Score] | [Score] | [Score] | [Where view differs from challenger.] |
| [Dim-2] | [Score] | [Score] | [Score] | |
| [Dim-3] | [Score] | [Score] | [Score] | |

**NH Dimension Scores** *(BRACKET CLOSING averages per NH TABLE AGGREGATION RULE)*:

| Dimension | Your Proposed-Build Score (B) | Your Best-Non-Build-Alt Score (C) |
|-----------|-------------------------------|-----------------------------------|
| [Copy §17 dimension.] | [0-10] | [0-10] |
| [Dim-2] | [Score] | [Score] |
| [Dim-3] | [Score] | [Score] |

**Additional Findings** *(each must cite §1 surface; severity per §14)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [Finding in 1-2 sentences.] | HIGH / MEDIUM / LOW |
| F-2 | [§1:S-n] | [Second finding.] | [Severity] |
| F-3 | [§1:S-n] -- optional | [Third finding.] | [Severity] |

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_], ...) = [SECTION_SEVERITY]
```
**Section Severity**: [Mechanical result.]

**Lens Coverage Table** *(cite AM row and tier exactly as assigned in ROLE MANIFEST)*:

| # | lens.verify Entry | Applicability (from ROLE MANIFEST) | Status | Finding Reference |
|---|------------------|-----------------------------------|--------|-------------------|
| Q-1 | [Full text of lens.verify entry 1.] | AM-01: [HIGH/MEDIUM/LOW] | ADDRESSED / OPEN | [F-n or AM cite] |
| Q-2 | [Entry 2.] | AM-02: [tier] | [Status] | [Reference] |
| Q-3 | [Entry 3 if present.] | AM-03: [tier] | [Status] | [Reference] |

**Recommendation**: [One specific, actionable change.]
**Simplify**: [One lens.simplify suggestion.]

**G_domain Verdict**: PASS / CONDITIONAL / FAIL
**G_domain Reason**: [One sentence. Name condition if CONDITIONAL; name gap if FAIL.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | [Verdict] | [Class] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT

*(EXCLUDED from gate ledger per §6.)*

```
G_domain rows: DOMAIN -- [ROLE_NAME]: [verdict]
G_domain_agg = worst([list]) = [result]

g_null(initial) = [copy] | G_domain_agg = [copy]
  FAIL->FAIL | CONDITIONAL->max(initial,CONDITIONAL) | PASS->g_null(initial)
g_null(post-domain) = [result]
```
**G_domain Aggregate**: [Result.]
**g_null(post-domain)**: [Result.]

---

## §3.8 CH-ID SATURATION CHECK

*(EXCLUDED from gate ledger.)*

| CH-ID | DOMAIN Response Status | Pre-LIFECYCLE Saturation |
|-------|------------------------|--------------------------|
| CH-001 | [Copy from DOMAIN.] | SATURATED / UNSATURATED |
| CH-002 | [Copy.] | [Status] |
| CH-003 | [Copy if active.] | [Status or N/A] |

**Pre-LIFECYCLE unsaturated CH-IDs**: [List UNSATURATED, or "None".]

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [Copy from BRACKET OPENING.]
Received G_domain Aggregate: [Copy from §3.5.]
Received g_null(post-domain): [Copy from §3.5.]

**CH-ID Response Table**:

| CH-ID | Challenge Claim (copy) | Your Commitment-Frame Response | Status |
|-------|----------------------|--------------------------------------|--------|
| CH-001 | [Copy claim.] | [Program and commitment perspective.] | ADDRESSED / PARTIAL / OPEN |
| CH-002 | [Copy.] | [Response.] | [Status] |
| CH-003 | [Copy if active.] | [Response.] | [Status] |

**COMMITMENT-READINESS MATRIX** *(complete before verdict)*:

| CRM Dimension | Current State | Required State for Commitment | Gap | Severity |
|---------------|--------------|-------------------------------|-----|---------|
| Timeline | [Current delivery state.] | [Required milestone certainty.] | [Gap or "None".] | HIGH / MEDIUM / LOW |
| Resources | [Current allocation.] | [Required resource commitment.] | [Gap or "None".] | [Severity] |
| Rollback | [Current rollback state.] | [Required rollback capability.] | [Gap or "None".] | [Severity] |
| Stakeholder Alignment | [Current alignment state.] | [Required alignment level.] | [Gap or "None".] | [Severity] |

**CRM Severity Aggregation**:
```
worst(Timeline=[_], Resources=[_], Rollback=[_], Stakeholder=[_]) = [CRM_SEVERITY]
```
**CRM Signal**: HIGH / MEDIUM / LOW

**Decision-readiness assessment**: [One paragraph referencing GOpen, G_domain Aggregate,
g_null(post-domain), and CRM Signal by name.]

**Null hypothesis status**: [One sentence on whether g_null(post-domain) has been defeated,
remains conditional, or holds -- citing the value explicitly.]

**Additional Findings** *(HIGH/MEDIUM CRM gaps should appear as findings; cite §1 surfaces)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [Commitment or program concern.] | HIGH / MEDIUM / LOW |
| F-2 | [§1:S-n] | [Second finding.] | [Severity] |

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_]) = [SECTION_SEVERITY]
```
**Section Severity**: [Mechanical result.]

**Lens Coverage Table**:

| # | lens.verify Entry | Applicability (from ROLE MANIFEST) | Status | Finding Reference |
|---|------------------|-----------------------------------|--------|-------------------|
| Q-1 | [Full text of lifecycle lens.verify entry 1.] | AM-04: [tier] | ADDRESSED / OPEN | [F-n or AM cite] |
| Q-2 | [Entry 2.] | AM-05: [tier] | [Status] | [Reference] |

**Recommendation**: [One concrete program or commitment action.]
**Simplify**: [One lens.simplify suggestion.]

**G_lifecycle Verdict**: PASS / CONDITIONAL / FAIL
**G_lifecycle Reason**: [One sentence. If CRM drove the verdict, cite the specific dimension.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| LIFECYCLE -- [ROLE_NAME] | G_lifecycle | [Verdict] | [Class] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1
*Full record received: scope declaration, APPLICABILITY MATRIX, all CH-ID tables, all verdicts.*

**STATUS QUO VERDICT** *(revisit STATUS QUO VIABILITY ASSESSMENT from opening)*

| SQ-DIM | Opening Viability | Evidence That Changed This | Revised Viability |
|--------|------------------|---------------------------|-------------------|
| [SQ-DIM-1] | [Opening rating.] | [Specific finding that changed view, or "none".] | VIABLE / MARGINAL / STRETCHED |
| [SQ-DIM-2] | [Opening.] | [Finding ref or "none".] | [Revised.] |
| [SQ-DIM-3] | [Opening.] | [Finding ref or "none".] | [Revised.] |

**SQ Viability Trajectory**: REINFORCED / UNCHANGED / WEAKENED

---

Apply §9 Stage 3 and re-populate the NH table mechanically per NH TABLE AGGREGATION RULE.

**Applying §9 Stage 3 formula**:
```
g_null(post-domain) = [copy] | G_lifecycle = [copy]
  FAIL->FAIL | CONDITIONAL->max(post-domain,CONDITIONAL) | PASS->g_null(post-domain)
g_null(final) = [result]
```
**g_null(final)**: [Result.] *GClose must equal g_null(final) per §9.*

**Revised NULL HYPOTHESIS DIMENSION TABLE**:

| Dimension | Status-Quo Score (A) | Proposed-Build Score (B) | Best-Non-Build-Alt Score (C) | D1=(B-A) | D2=(B-C) | NH Verdict |
|-----------|---------------------|--------------------------|------------------------------|----------|----------|------------|
| [DIM-1*] | A: carry from opening. | B: avg domain B scores. | C: avg domain C scores. | [D1] | [D2] | [Verdict] |
| [DIM-2*] | A unchanged. | avg domain B. | avg domain C. | [D1] | [D2] | [Verdict] |
| [DIM-3] | A unchanged. | avg domain B. | avg domain C. | [D1] | [D2] | [Verdict] |

**NH AGGREGATION RULE APPLIED**:
```
Column A: challenger opening values carried forward unchanged
Column B averages: [DIM-1]: avg([domain B scores]) = [result]; [DIM-2]: avg([...]) = [result]
Column C averages: [DIM-1]: avg([domain C scores]) = [result]; [DIM-2]: avg([...]) = [result]
```

**Applying §17 g_null derivation rule to revised table**:
```
MUST-CLEAR rows with OPPOSES-BUILD: [list or "none"]
count(FAVORS-BUILD)=[N] count(CONDITIONAL)=[N] count(OPPOSES-BUILD)=[N]
DEFEATED: [Y/N]
Result: [HOLDS / CONDITIONAL / DEFEATED]
```

**Full CH-ID Saturation Check** *(per §8)*:

| CH-ID | DOMAIN Status | LIFECYCLE Status | Full Saturation | Waiver (if needed) |
|-------|--------------|-----------------|-----------------|---------------------|
| CH-001 | [Copy.] | [Copy.] | FULLY SATURATED / UNSATURATED | [WAIVER or N/A] |
| CH-002 | [Copy.] | [Copy.] | [Status] | N/A |
| CH-003 | [Copy if active.] | [Copy.] | [Status] | N/A |

**§17a CHARTER COVERAGE AUDIT** *(per §17a [IMMUTABLE])*:

| §0 Arg | Argument Text (summary) | Addressed By CH-IDs | Coverage |
|--------|------------------------|---------------------|----------|
| §0:Arg-1 | [Summary of Arg-1.] | [CH-IDs that cited this arg.] | COVERED / CHARTER-GAP |
| §0:Arg-2 | [Summary.] | [CH-IDs.] | [Coverage] |
| §0:Arg-3 | [Summary or N/A.] | [CH-IDs.] | [Coverage] |

**CHARTER-GAP items** *(if any)*: [List CHARTER-GAP args or "None".]

**GClose Verdict**: PASS if g_null=DEFEATED, CH-IDs fully saturated, and zero CHARTER-GAP.
CONDITIONAL or FAIL otherwise.
**Override invoked**: YES / NO
**g_null Override**: N/A -- formula applied, or [justification].
**GClose Rationale**: [2-3 sentences referencing g_null(final), CH-ID saturation,
SQ Viability Trajectory, Charter Coverage Audit result, and CRM Signal.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [Verdict] | [Class] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION

*(EXCLUDED from gate ledger per §6.)*

### Surface Coverage *(per §10)*

| IN-SCOPE Surface | Reviewer(s) | Finding Reference(s) | Coverage |
|-----------------|-------------|---------------------|----------|
| [Surface 1.] | [Reviewer or "none".] | [Finding refs.] | COVERED / GAP |
| [Surface 2.] | [Reviewer.] | [Refs.] | [Coverage] |

**Surface coverage gate signal**: COVERED / PARTIAL -- [N surface(s) not addressed.]

### Domain Coverage Gap-Check *(per §10a)*

| Artifact Domain | HIGH-Applicability MATRIX Rows | Coverage |
|----------------|-------------------------------|----------|
| [Domain from §1 annotations.] | [AM rows with HIGH, or "none".] | COVERED / ADVISORY-GAP |
| [Second domain.] | [AM rows or "none".] | [Coverage] |

**§11 ADVISORY-ORPHAN check**: [List findings lacking §1:S-n citations, or "None detected."]

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract Cite |
|------|----------|---------|---------------|
| GOpen -- bracket opening | [CHALLENGER_ROLE] | [Copy verdict.] | DISPOSITION_CONTRACT v1 |
| G_domain_agg -- domain aggregate | [DOMAIN_ROLE] | [Copy verdict.] | DISPOSITION_CONTRACT v1 |
| G_lifecycle -- lifecycle | [LIFECYCLE_ROLE] | [Copy verdict.] | DISPOSITION_CONTRACT v1 |
| GClose -- bracket closing | [CHALLENGER_ROLE] | [Copy verdict.] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [Identify incompatible assessments across roles, or "None detected."]

**Convergence**: [Identify concern raised independently by 2+ reviewers. Explain why convergence
makes it the highest-confidence signal.]

**Scope coverage**: [List §1 surfaces no reviewer addressed, or "None."]

**§13 PROGRESSION LEDGER**:
```
g_null(initial)     = [copy from BRACKET OPENING §17]
g_null(post-domain) = [copy from §3.5]
g_null(final)       = [copy from BRACKET CLOSING §9 Stage 3]
Trajectory:         [MONOTONIC-PASS / MONOTONIC-FAIL / DOMAIN-DEGRADED / LIFECYCLE-DEGRADED /
                    DOMAIN-RECOVERED / LIFECYCLE-RECOVERED]
```

---

## DISPOSITION

**Gate vector**: GOpen=[copy] | G_domain_agg=[copy] | G_lifecycle=[copy] | GClose=[copy]

Apply §3 formula mechanically:
```
GClose=FAIL? -> BLOCKED
Any other Gi=FAIL? -> BLOCKED
No FAIL and any CONDITIONAL? -> CONDITIONAL
All PASS? -> READY
```

**Overall Disposition**: READY / CONDITIONAL / BLOCKED

**Applying §16 rule**: [Rule number and reason it fired.]
**Primary Driver**: [BRACKET CLOSING / DOMAIN / LIFECYCLE / BRACKET OPENING / N/A]

**Conditions** *(only if CONDITIONAL)*: [State condition(s) from CONDITIONAL gate(s).]

**Blocker** *(only if BLOCKED)*: [Specific finding from FAIL gate. If GClose=FAIL: "Challenger
final verdict HOLDS -- [GClose Rationale summary]."]

**RESOLUTION REGISTRY** *(only if CONDITIONAL)*:
| Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status |
|------|------------------|-----------------|---------------------|--------|
| [Gate.] | [Condition.] | [Role.] | [Falsifiable test.] | OPEN |

*If not CONDITIONAL: "RESOLUTION REGISTRY: N/A -- disposition is [value]"*

---

## ACTION ITEM REGISTER

Copy all local gate ledger rows verbatim. Do not re-derive Gate Verdict or Class.
Then add all advisory items.

| Source | CH-ID / Finding | Item Description | Disposition Class | Owner Role | Resolution Criterion |
|--------|----------------|-----------------|------------------|------------|---------------------|
| Gate ledger copy. | -- | [Section / Gate / Verdict / Class verbatim.] | [Class] | [Role] | [Criterion] |
| CH-ID item. | CH-00n | [What must be resolved for PARTIAL or HOLDS status.] | [Class] | [Role] | [Criterion] |
| Lens HIGH. | AM-0n / Q-n | ADVISORY-OPEN-LENS-REQUIRED: [lens entry] not addressed; HIGH applicability. | ADVISORY | [Role] | Produce finding for this lens entry. |
| Lens MEDIUM. | AM-0n / Q-n | ADVISORY-OPEN-LENS: [lens entry] not addressed; MEDIUM applicability. | ADVISORY | [Role] | Address or justify non-applicability. |
| Scope gap. | -- | ADVISORY-GAP: §1 surface [name] not covered by any reviewer. | ADVISORY | [Role] | Assign reviewer with relevant lens. |
| Domain gap. | -- | ADVISORY-GAP (DOMAIN COVERAGE): [domain] has no HIGH-applicability reviewer. | ADVISORY | [Role] | Add HIGH-applicability reviewer or justify waiver. |
| Orphan. | -- | ADVISORY-ORPHAN: finding [F-n] from [SECTION] lacks §1:S-n citation. | ADVISORY | [Role] | Re-assign to valid §1 surface. |
| Charter gap. | §0:Arg-n | ADVISORY-CHARTER-GAP: §0:Arg-n "[summary]" not addressed by any CH-ID claim. | ADVISORY | [CHALLENGER] | Issue a challenge claim citing this argument, or declare waiver with justification. |

---

**Artifact to review:**

{{artifact}}
```

---

## V-02

**Axis**: Output format -- Global F-ID namespace. All findings across all reviewer sections
receive globally unique identifiers (e.g., F-DOMAIN-01, F-LIFECYCLE-01) declared in a §18
GLOBAL F-ID REGISTRY contract. The ACTION ITEM REGISTER and SCOPE COVERAGE RECONCILIATION
reference findings by global ID, enabling cross-section finding traceability.

**Hypothesis**: Currently each reviewer section uses a local F-1, F-2, ... numbering scheme.
Cross-section references (e.g., "see F-2 from DOMAIN") require the reader to track section
context. A global F-ID namespace (F-{SECTION_PREFIX}-{nn}) makes every finding uniquely
addressable without section context. The ACTION ITEM REGISTER can cite F-DOMAIN-01 directly.
SCOPE COVERAGE RECONCILIATION can list "F-DOMAIN-01, F-LIFECYCLE-01" per surface. Candidate
C-41: Global Finding Addressability -- all findings carry globally unique IDs declared in a
pre-committed registry contract; all downstream references use global IDs; cross-section
tracing is available without reader-side section-name disambiguation.

---

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .roles/signal/
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

You will play four roles in sequence: an inertia-advocate challenger who opens the review,
a domain-expert reviewer, a lifecycle/program reviewer, and the challenger again at closing.

The challenger's default is that the artifact should NOT be built. This review is the evidence
process that can overcome that prior.

Fill in all required fields. Do not alter, reorder, or omit any pre-printed heading, label,
formula, or structural element. If a field is not applicable, write "N/A -- " followed by
the reason.

---

```
======================================================================
DISPOSITION_CONTRACT v1
[IMMUTABLE BLOCK -- complete §1 scope fields; do not alter §2-§18;
reviewer sections may not execute until §1 COMPLETE marker is reached]
======================================================================

§1 -- SCOPE ENUMERATION
IN-SCOPE (cited in §5.5 SCOPE COVERAGE RECONCILIATION and §11 FINDING-SURFACE LINKAGE):
  Each surface must carry a [DOMAIN: label] annotation.
  1. [SURFACE_1] [DOMAIN: label]
  2. [SURFACE_2] [DOMAIN: label]
  3. [SURFACE_3] [DOMAIN: label]
  (Add rows. Be exhaustive.)

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
  PASS from BRACKET CLOSING prohibited without full saturation or stated waiver.
  Waiver: "CH-XXX WAIVER: [reason]" -> ACTION ITEM REGISTER as ADVISORY.

§9 -- NULL HYPOTHESIS PROGRESSION CONTRACT [IMMUTABLE]
  Stage 1: g_null(initial) = output of §17 formula [emitted at BRACKET OPENING]
  Stage 2: g_null(post-domain) [emitted at §3.5]:
    G_domain_agg=FAIL        -> g_null(post-domain)=FAIL
    G_domain_agg=CONDITIONAL -> g_null(post-domain)=max(g_null(initial), CONDITIONAL)
    G_domain_agg=PASS        -> g_null(post-domain)=g_null(initial)
  Stage 3: g_null(final) [emitted at BRACKET CLOSING]:
    G_lifecycle=FAIL         -> g_null(final)=FAIL
    G_lifecycle=CONDITIONAL  -> g_null(final)=max(g_null(post-domain), CONDITIONAL)
    G_lifecycle=PASS         -> g_null(final)=g_null(post-domain)
  GClose must equal g_null(final). Override: "g_null OVERRIDE: [justification]"

§10 -- SCOPE COVERAGE GATE PROTOCOL [IMMUTABLE]
  After BRACKET CLOSING, §5.5 maps each §1 IN-SCOPE surface to reviewer findings.
  Classification: COVERED (>=1 finding) or GAP (no finding).
  GAP surfaces -> ADVISORY-GAP in ACTION ITEM REGISTER.
  §5.5 ALSO runs DOMAIN COVERAGE GAP-CHECK per §10a.

§10a -- DOMAIN COVERAGE GAP-CHECK PROTOCOL [IMMUTABLE]
  Embedded in §5.5, after the surface coverage table.
  Step 1: Group §1 surfaces into ARTIFACT DOMAINS via [DOMAIN: label] annotations.
  Step 2: For each domain, look up APPLICABILITY MATRIX rows with HIGH rating.
  Step 3: COVERED = at least one HIGH row. ADVISORY-GAP = no HIGH row.
  Step 4: ADVISORY-GAP domains -> ACTION ITEM REGISTER as ADVISORY.

§11 -- FINDING-SURFACE LINKAGE REQUIREMENT [IMMUTABLE]
  Each finding carries a "[§1:S-n]" citation.
  Missing citation = ADVISORY-ORPHAN -> ACTION ITEM REGISTER.

§12 -- CONDITIONAL RESOLUTION REGISTRY CONTRACT [IMMUTABLE]
  DISPOSITION=CONDITIONAL -> emit RESOLUTION REGISTRY table.
  Else: "RESOLUTION REGISTRY: N/A -- disposition is [value]"

§13 -- g_null PROGRESSION LEDGER REQUIREMENT [IMMUTABLE]
  CROSS-ROLE SIGNALS: §13 PROGRESSION LEDGER:
    g_null(initial) | g_null(post-domain) | g_null(final) | Trajectory

§14 -- FINDING SEVERITY AGGREGATION CONTRACT [IMMUTABLE]
  Findings table: | # | §1 Surface | Finding | Severity |
  Section Severity = worst(all severities in section). HIGH>MEDIUM>LOW.
  No findings: Section Severity = LOW.

§15 -- LENS EXHAUSTION REQUIREMENT [IMMUTABLE]
  Each section emits LENS COVERAGE TABLE after findings:
    | # | lens.verify Entry | Applicability (from ROLE MANIFEST) | Status | Finding Reference |
  Applicability: cite APPLICABILITY MATRIX row ID and tier. Do NOT reassign.
  HIGH + OPEN -> ADVISORY-OPEN-LENS-REQUIRED.
  MEDIUM + OPEN -> ADVISORY-OPEN-LENS.
  LOW + OPEN -> no register entry; cite AM row.

§16 -- PRIMARY DRIVER DERIVATION CONTRACT [IMMUTABLE]
  Precedence rule at DISPOSITION:
    1. GClose=FAIL        -> BRACKET CLOSING
    2. G_domain_agg=FAIL  -> DOMAIN
    3. G_lifecycle=FAIL   -> LIFECYCLE
    4. GOpen=FAIL         -> BRACKET OPENING
    5. GClose=CONDITIONAL -> BRACKET CLOSING
    6. G_domain_agg=CONDITIONAL -> DOMAIN
    7. G_lifecycle=CONDITIONAL  -> LIFECYCLE
    8. GOpen=CONDITIONAL        -> BRACKET OPENING
    9. all PASS           -> N/A

§17 -- NULL HYPOTHESIS DIMENSION TABLE CONTRACT [IMMUTABLE]
  BRACKET OPENING challenger uses a three-column per-dimension comparison table.
  Table format:
    | Dimension | Status-Quo (A,0-10) | Proposed-Build (B,0-10) | Best-Non-Build-Alt (C,0-10) | D1=(B-A) | D2=(B-C) | NH Verdict |
  MUST-CLEAR dimensions marked (*). Minimum 3 dimensions.
  Per-row verdict: FAVORS-BUILD (D1>0 AND D2>0) / CONDITIONAL (D1>0, D2<=0) / OPPOSES-BUILD (D1<=0).
  g_null: HOLDS (any MUST-CLEAR OPPOSES-BUILD) / CONDITIONAL / DEFEATED (FAVORS-BUILD majority,
          no MUST-CLEAR OPPOSES, BOTH D1 AND D2 positive majority).
  NH TABLE AGGREGATION RULE: Column A = opener's original. Column B = avg(domain B scores).
    Column C = avg(domain C scores). BRACKET CLOSING re-applies §17 rule to revised table.

§18 -- GLOBAL F-ID REGISTRY [IMMUTABLE]
  Every finding in every reviewer section receives a globally unique identifier.
  Format: F-{PREFIX}-{nn} where PREFIX is:
    OPEN = BRACKET OPENING  (F-OPEN-01, F-OPEN-02, ...)
    DOM  = DOMAIN reviewer(s) (F-DOM-01, F-DOM-02, ...; multi-reviewer: F-DOM1-01, F-DOM2-01)
    LIFE = LIFECYCLE reviewer (F-LIFE-01, F-LIFE-02, ...)
  Counter is per-prefix, sequential within each section.
  All downstream references (ACTION ITEM REGISTER, SCOPE COVERAGE RECONCILIATION,
  LENS COVERAGE TABLE Finding Reference, CH-ID response tables) MUST use the global F-ID.
  Per-section F-1/F-2 local aliases are NOT used. Global IDs are the sole reference.
  The GATE VECTOR TABLE records the highest-severity global F-ID per gate as a named field.

======================================================================
END DISPOSITION_CONTRACT v1
======================================================================
```

---

## ROLE MANIFEST

Read `.roles/signal/`. Choose challenger (inertia-advocate), domain role, lifecycle role.

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER | inertia-advocate | [ROLE_NAME] | [One sentence.] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [One sentence.] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [One sentence.] |

### APPLICABILITY MATRIX

Complete before BRACKET OPENING. Locked at this point.

| Row ID | Role | lens.verify Entry | Artifact Domain Covered | Artifact Applicability | Basis for Rating |
|--------|------|------------------|------------------------|----------------------|------------------|
| AM-01 | [DOMAIN] | [Full lens.verify text.] | [Domain.] | HIGH / MEDIUM / LOW | [Basis.] |
| AM-02 | [DOMAIN] | [Second entry.] | [Domain.] | [Tier.] | [Basis.] |
| AM-03 | [DOMAIN] | [Third entry.] | [Domain.] | [Tier.] | [Basis.] |
| AM-04 | [LIFECYCLE] | [First lifecycle entry.] | [Domain.] | [Tier.] | [Basis.] |
| AM-05 | [LIFECYCLE] | [Second entry.] | [Domain.] | [Tier.] | [Basis.] |

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**STATUS QUO VIABILITY ASSESSMENT**:

| SQ-DIM | Current State | Why Acceptable | Viability |
|--------|--------------|----------------|-----------|
| [Dim-1] | [Current practice.] | [Concrete advantage.] | HIGH/MEDIUM/LOW |
| [Dim-2] | [Current practice.] | [Advantage.] | [Viability] |
| [Dim-3] | [Current practice.] | [Advantage.] | [Viability] |

**Overall SQ Viability**: VIABLE / MARGINAL / STRETCHED

**Null hypothesis**: [One sentence: what team does today.]

**Alternatives comparison table**:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|---------------|-----------|----------------------|-------|
| [Dim-1] | [Score] | [Score] | [Score] | |
| [Dim-2] | [Score] | [Score] | [Score] | |
| [Dim-3] | [Score] | [Score] | [Score] | |

**NULL HYPOTHESIS DIMENSION TABLE** *(per §17)*:

| Dimension | Status-Quo (A) | Proposed-Build (B) | Best-Non-Build-Alt (C) | D1=(B-A) | D2=(B-C) | NH Verdict |
|-----------|---------------|-------------------|----------------------|----------|----------|------------|
| [Dim-1*] | [Score] | [Score] | [Score] | [D1] | [D2] | [Verdict] |
| [Dim-2*] | [Score] | [Score] | [Score] | [D1] | [D2] | [Verdict] |
| [Dim-3] | [Score] | [Score] | [Score] | [D1] | [D2] | [Verdict] |

**Applying §17 g_null derivation**:
```
MUST-CLEAR OPPOSES-BUILD: [list or "none"]
count(FAVORS-BUILD)=[N] count(CONDITIONAL)=[N] count(OPPOSES-BUILD)=[N]
DEFEATED: [Y/N]
Result: [HOLDS / CONDITIONAL / DEFEATED]
```
**g_null(initial)**: [HOLDS / CONDITIONAL / DEFEATED]

*(BRACKET OPENING findings use global F-IDs per §18: F-OPEN-01, F-OPEN-02, ...)*

**Challenge claims** *(cite SQ-DIM; assign CH-IDs)*:

| CH-ID | Challenge Claim | SQ-DIM Referenced | Severity |
|-------|----------------|-------------------|---------|
| CH-001 | [Claim.] | [SQ-DIM-n] | HIGH/MEDIUM/LOW |
| CH-002 | [Claim.] | [SQ-DIM-n] | [Severity] |
| CH-003 | [Claim or omit.] | [SQ-DIM-n] | [Severity] |

**GOpen Verdict**: PASS / CONDITIONAL / FAIL
**GOpen Reason**: [One sentence.]
**Leading F-ID**: F-OPEN-[nn] (highest-severity finding from this section, or "N/A -- no findings")

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [Verdict] | [Class] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [Copy from BRACKET OPENING.]

*(All findings in this section use global F-IDs per §18: F-DOM-01, F-DOM-02, ...)*

**CH-ID Response Table**:

| CH-ID | Challenge Claim (verbatim) | Technical Assessment | Status |
|-------|---------------------------|---------------------|--------|
| CH-001 | [Copy.] | [Assessment.] | ADDRESSED/PARTIAL/OPEN |
| CH-002 | [Copy.] | [Assessment.] | [Status] |
| CH-003 | [Copy if active.] | [Assessment.] | [Status] |

**Domain re-score**:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Rationale |
|-----------|---------------|-----------|----------------------|-----------|
| [Dim-1] | [Score] | [Score] | [Score] | [Difference from challenger view.] |
| [Dim-2] | [Score] | [Score] | [Score] | |
| [Dim-3] | [Score] | [Score] | [Score] | |

**NH Dimension Scores** *(for §17 aggregation at BRACKET CLOSING)*:

| Dimension | Your Build Score (B) | Your Best-Alt Score (C) |
|-----------|---------------------|------------------------|
| [Dim-1] | [Score] | [Score] |
| [Dim-2] | [Score] | [Score] |
| [Dim-3] | [Score] | [Score] |

**Findings** *(global F-IDs; each cites §1 surface; severity per §14)*:

| # | Global F-ID | §1 Surface | Finding | Severity |
|---|-------------|-----------|---------|---------|
| 1 | F-DOM-01 | [§1:S-n] | [Finding.] | HIGH/MEDIUM/LOW |
| 2 | F-DOM-02 | [§1:S-n] | [Finding.] | [Severity] |
| 3 | F-DOM-03 | [§1:S-n] | [Finding.] | [Severity] |

**Finding Severity Aggregation (per §14)**:
```
worst(F-DOM-01=[_], F-DOM-02=[_], ...) = [SECTION_SEVERITY]
```
**Section Severity**: [Mechanical result.]

**Lens Coverage Table**:

| # | lens.verify Entry | Applicability (from ROLE MANIFEST) | Status | Finding Reference |
|---|------------------|-----------------------------------|--------|-------------------|
| Q-1 | [Entry 1.] | AM-01: [tier] | ADDRESSED/OPEN | F-DOM-[nn] or AM cite |
| Q-2 | [Entry 2.] | AM-02: [tier] | [Status] | [Reference] |
| Q-3 | [Entry 3.] | AM-03: [tier] | [Status] | [Reference] |

**Recommendation**: [One actionable change.]
**Leading F-ID**: F-DOM-[nn] (highest-severity finding from this section)

**G_domain Verdict**: PASS / CONDITIONAL / FAIL
**G_domain Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | [Verdict] | [Class] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT

*(EXCLUDED from gate ledger per §6.)*

```
G_domain_agg = worst([list]) = [result]
g_null(post-domain) = [derivation per §9 Stage 2]
```
**G_domain Aggregate**: [Result.]
**g_null(post-domain)**: [Result.]

---

## §3.8 CH-ID SATURATION CHECK

*(EXCLUDED from gate ledger.)*

| CH-ID | DOMAIN Response Status | Pre-LIFECYCLE Saturation |
|-------|------------------------|--------------------------|
| CH-001 | [Copy.] | SATURATED / UNSATURATED |
| CH-002 | [Copy.] | [Status] |

**Pre-LIFECYCLE unsaturated CH-IDs**: [List or "None".]

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [Copy.] | G_domain Aggregate: [Copy.] | g_null(post-domain): [Copy.]

*(All findings in this section use global F-IDs per §18: F-LIFE-01, F-LIFE-02, ...)*

**CH-ID Response Table**:

| CH-ID | Challenge Claim (copy) | Commitment-Frame Response | Status |
|-------|----------------------|--------------------------|--------|
| CH-001 | [Copy.] | [Program perspective.] | ADDRESSED/PARTIAL/OPEN |
| CH-002 | [Copy.] | [Response.] | [Status] |

**COMMITMENT-READINESS MATRIX**:

| CRM Dimension | Current State | Required State | Gap | Severity |
|---------------|--------------|----------------|-----|---------|
| Timeline | [Current.] | [Required.] | [Gap or "None".] | HIGH/MEDIUM/LOW |
| Resources | [Current.] | [Required.] | [Gap.] | [Severity] |
| Rollback | [Current.] | [Required.] | [Gap.] | [Severity] |
| Stakeholder Alignment | [Current.] | [Required.] | [Gap.] | [Severity] |

**CRM Severity**: worst([list]) = [CRM_SEVERITY]

**Decision-readiness assessment**: [One paragraph referencing GOpen, G_domain_agg,
g_null(post-domain), and CRM Signal.]

**Findings** *(global F-IDs; cite §1 surfaces)*:

| # | Global F-ID | §1 Surface | Finding | Severity |
|---|-------------|-----------|---------|---------|
| 1 | F-LIFE-01 | [§1:S-n] | [Finding.] | HIGH/MEDIUM/LOW |
| 2 | F-LIFE-02 | [§1:S-n] | [Finding.] | [Severity] |

**Finding Severity Aggregation**: worst(F-LIFE-01=[_], ...) = [SECTION_SEVERITY]
**Section Severity**: [Mechanical result.]

**Lens Coverage Table**:

| # | lens.verify Entry | Applicability (from ROLE MANIFEST) | Status | Finding Reference |
|---|------------------|-----------------------------------|--------|-------------------|
| Q-1 | [Entry 1.] | AM-04: [tier] | ADDRESSED/OPEN | F-LIFE-[nn] or AM cite |
| Q-2 | [Entry 2.] | AM-05: [tier] | [Status] | [Reference] |

**Recommendation**: [One concrete program action.]
**Leading F-ID**: F-LIFE-[nn] (highest-severity finding)

**G_lifecycle Verdict**: PASS / CONDITIONAL / FAIL
**G_lifecycle Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| LIFECYCLE -- [ROLE_NAME] | G_lifecycle | [Verdict] | [Class] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**STATUS QUO VERDICT**:

| SQ-DIM | Opening | Evidence Changed? | Revised |
|--------|---------|-------------------|---------|
| [Dim-1] | [Opening.] | [Finding ref or "none".] | VIABLE/MARGINAL/STRETCHED |
| [Dim-2] | [Opening.] | [Finding ref.] | [Revised.] |
| [Dim-3] | [Opening.] | [Finding ref.] | [Revised.] |

**SQ Viability Trajectory**: REINFORCED / UNCHANGED / WEAKENED

**Applying §9 Stage 3**:
```
g_null(post-domain)=[copy] | G_lifecycle=[copy]
g_null(final) = [derivation]
```
**g_null(final)**: [Result.]

**Revised NULL HYPOTHESIS DIMENSION TABLE** *(§17 aggregation)*:

| Dimension | A (carry forward) | B (avg domain) | C (avg domain) | D1 | D2 | NH Verdict |
|-----------|------------------|----------------|----------------|----|----|------------|
| [Dim-1*] | [A] | [avg] | [avg] | [D1] | [D2] | [Verdict] |
| [Dim-2*] | [A] | [avg] | [avg] | [D1] | [D2] | [Verdict] |
| [Dim-3] | [A] | [avg] | [avg] | [D1] | [D2] | [Verdict] |

```
MUST-CLEAR OPPOSES-BUILD: [list or "none"]
DEFEATED: [Y/N]  Result: [HOLDS / CONDITIONAL / DEFEATED]
```

**Full CH-ID Saturation**:

| CH-ID | DOMAIN | LIFECYCLE | Full Saturation |
|-------|--------|-----------|-----------------|
| CH-001 | [Copy.] | [Copy.] | FULLY SATURATED / UNSATURATED |
| CH-002 | [Copy.] | [Copy.] | [Status] |

**GClose Verdict**: PASS / CONDITIONAL / FAIL
**Override invoked**: YES / NO
**g_null Override**: N/A or [justification.]
**GClose Rationale**: [2-3 sentences referencing g_null(final), CH-ID saturation,
SQ Viability Trajectory, and CRM Signal.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [Verdict] | [Class] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION

*(EXCLUDED from gate ledger.)*

**Surface Coverage** *(references use global F-IDs per §18)*:

| IN-SCOPE Surface | Reviewer(s) | Global F-IDs | Coverage |
|-----------------|-------------|--------------|----------|
| [Surface 1.] | [Reviewer.] | [F-DOM-01, F-LIFE-01, ...] | COVERED / GAP |
| [Surface 2.] | [Reviewer.] | [F-IDs or "none".] | [Coverage] |

**Surface coverage signal**: COVERED / PARTIAL

**Domain Coverage Gap-Check** *(per §10a)*:

| Artifact Domain | HIGH-Applicability MATRIX Rows | Coverage |
|----------------|-------------------------------|----------|
| [Domain.] | [AM rows or "none".] | COVERED / ADVISORY-GAP |

**§11 ADVISORY-ORPHAN check**: [Findings lacking §1:S-n, or "None".]

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Leading F-ID | Contract Cite |
|------|----------|---------|-------------|---------------|
| GOpen | [CHALLENGER] | [Verdict] | F-OPEN-[nn] or N/A | DISPOSITION_CONTRACT v1 |
| G_domain_agg | [DOMAIN] | [Verdict] | F-DOM-[nn] | DISPOSITION_CONTRACT v1 |
| G_lifecycle | [LIFECYCLE] | [Verdict] | F-LIFE-[nn] | DISPOSITION_CONTRACT v1 |
| GClose | [CHALLENGER] | [Verdict] | N/A | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [Incompatible cross-role assessments, or "None".]

**Convergence**: [Concern raised by 2+ reviewers, with global F-IDs named.]

**Scope coverage**: [§1 surfaces with no finding, or "None".]

**§13 PROGRESSION LEDGER**:
```
g_null(initial)=[copy] | g_null(post-domain)=[copy] | g_null(final)=[copy]
Trajectory: [label]
```

---

## DISPOSITION

**Gate vector**: GOpen=[copy] | G_domain_agg=[copy] | G_lifecycle=[copy] | GClose=[copy]

Apply §3 mechanically:
```
GClose=FAIL? -> BLOCKED | Any Gi=FAIL? -> BLOCKED | Any CONDITIONAL? -> CONDITIONAL | READY
```

**Overall Disposition**: READY / CONDITIONAL / BLOCKED
**Applying §16 rule**: [Rule n + reason.] **Primary Driver**: [result]

**Conditions** *(CONDITIONAL only)*: [State conditions.]
**Blocker** *(BLOCKED only)*: [Specific finding (global F-ID) from FAIL gate.]

**RESOLUTION REGISTRY** *(CONDITIONAL only)*:
| Gate | Condition | Owner | Resolution Criterion | Status |
|------|-----------|-------|---------------------|--------|
| [Gate.] | [Condition.] | [Role.] | [Falsifiable test.] | OPEN |

*If not CONDITIONAL: "RESOLUTION REGISTRY: N/A -- disposition is [value]"*

---

## ACTION ITEM REGISTER

*(Copy all local gate ledger rows verbatim. Do not re-derive. Use global F-IDs throughout.)*

| Source | Global F-ID / CH-ID | Item Description | Class | Owner | Resolution Criterion |
|--------|--------------------|-----------------|----|-------|---------------------|
| Gate ledger copy. | -- | [Verbatim: Section/Gate/Verdict/Class.] | [Class] | [Role] | [Criterion] |
| CH-ID item. | CH-00n | [What to resolve.] | [Class] | [Role] | [Criterion] |
| Lens HIGH. | AM-0n / Q-n | ADVISORY-OPEN-LENS-REQUIRED: [lens entry]. | ADVISORY | [Role] | Produce finding. |
| Lens MEDIUM. | AM-0n / Q-n | ADVISORY-OPEN-LENS: [lens entry]. | ADVISORY | [Role] | Address or justify. |
| Scope gap. | -- | ADVISORY-GAP: §1 surface [name] not covered. | ADVISORY | [Role] | Assign reviewer. |
| Domain gap. | -- | ADVISORY-GAP (DOMAIN): [domain] no HIGH reviewer. | ADVISORY | [Role] | Add reviewer or waive. |
| Orphan. | F-{PREFIX}-[nn] | ADVISORY-ORPHAN: [F-ID] from [SECTION] lacks §1:S-n. | ADVISORY | [Role] | Re-assign to §1 surface. |

---

**Artifact to review:**

{{artifact}}
```

---

## V-03

**Axis**: Lifecycle emphasis -- LIFECYCLE reviewer emits a NH Dimension Score sub-table
(B and C scores per §17 dimension), and §17 NH TABLE AGGREGATION RULE is extended to average
LIFECYCLE scores alongside DOMAIN scores when computing bracket-closing Column B and C values.

**Hypothesis**: The current §17 NH TABLE AGGREGATION RULE averages only DOMAIN reviewer B/C
scores at bracket closing. LIFECYCLE has a commitment-readiness perspective on whether Build
beats Best-Alt on program dimensions (timeline predictability, integration cost, rollback
risk). Excluding LIFECYCLE from the NH averaging chain means bracket closing integrates domain
evidence only. Extending the aggregation to include LIFECYCLE closes this arm. Candidate C-41:
Universal Reviewer NH Score Emission -- all verdict-emitting reviewer archetypes (DOMAIN and
LIFECYCLE) emit NH dimension score sub-tables; bracket closing averages all reviewer scores per
dimension without prose extraction.

---

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .roles/signal/
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

You will play four roles in sequence: an inertia-advocate challenger who opens the review,
a domain-expert reviewer, a lifecycle/program reviewer, and the challenger again at closing.
All reviewer archetypes contribute NH dimension scores that feed the bracket closing aggregation.

Fill in all required fields. Do not alter, reorder, or omit any pre-printed heading, label,
formula, or structural element. If a field is not applicable, write "N/A -- " followed by
the reason.

---

DISPOSITION_CONTRACT v1 [IMMUTABLE]

§1 SCOPE ENUMERATION
IN-SCOPE (cited in §5.5 and §11; each surface carries [DOMAIN: label]):
  1. [SURFACE_1] [DOMAIN: label]
  2. [SURFACE_2] [DOMAIN: label]
  3. [SURFACE_3] [DOMAIN: label]
OUT-OF-SCOPE: 1. [SURFACE -- REASON_EXCLUDED]
Scope Amendment Protocol: SCOPE AMENDMENT: [surface] -- [reason]; silent expansion violates.

§1 COMPLETE

§2 SEVERITY SEMANTICS [IMMUTABLE]
  HIGH=Blocks. MEDIUM=Conditions (named resolution required). LOW=Advisory.

§3 DISPOSITION ALGEBRA [IMMUTABLE]
  BLOCKED if GClose=FAIL or any Gi=FAIL; CONDITIONAL if no FAIL and some CONDITIONAL; READY if all PASS.

§3a DOMAIN-AGGREGATE FORMULA [IMMUTABLE]
  G_domain_agg = worst(all G_domain rows). Single domain: direct pass-through.

§4 CONTRACT CITE [IMMUTABLE]: Each section opens with "Contract: DISPOSITION_CONTRACT v1"

§5 CH-ID TRACING [IMMUTABLE]: Claims receive CH-IDs. All downstream sections carry CH-ID table.
  PASS prohibited if any CH-ID OPEN.

§6 LOCAL GATE LEDGER [IMMUTABLE]
  Row: | Section | Gate | Verdict | Class | (FAIL->BLOCKED; CONDITIONAL->CONDITIONAL; PASS->ADVISORY)
  EXCLUDED: §3.5, §3.8, §5.5.

§7 SECTION ORDER [IMMUTABLE]: ROLE MANIFEST -> BRACKET OPENING -> DOMAIN(s) ->
  §3.5 DOMAIN-AGGREGATE -> §3.8 CH-ID SATURATION -> LIFECYCLE -> BRACKET CLOSING ->
  §5.5 SCOPE COVERAGE -> GATE VECTOR TABLE -> CROSS-ROLE SIGNALS -> DISPOSITION ->
  ACTION ITEM REGISTER. Reordering violates.

§8 CH-ID SATURATION [IMMUTABLE]: FULLY SATURATED = DOMAIN+LIFECYCLE response before BRACKET CLOSING.
  PASS prohibited without saturation or waiver. Waiver -> ADVISORY in register.

§9 NULL HYPOTHESIS PROGRESSION [IMMUTABLE]
  Stage 1: g_null(initial) = §17 formula at BRACKET OPENING
  Stage 2 at §3.5: FAIL->FAIL; CONDITIONAL->max(initial,COND); PASS->initial
  Stage 3 at BRACKET CLOSING: FAIL->FAIL; CONDITIONAL->max(post-domain,COND); PASS->post-domain
  GClose must equal g_null(final).

§10 SCOPE COVERAGE [IMMUTABLE]: §5.5 maps §1 surfaces to findings. GAP -> ADVISORY-GAP. Also runs §10a.

§10a DOMAIN COVERAGE GAP-CHECK [IMMUTABLE]: Group §1 surfaces by [DOMAIN: label]. Find APPLICABILITY
  MATRIX rows with HIGH per domain. COVERED=at least one HIGH row. ADVISORY-GAP=no HIGH row ->
  ACTION ITEM REGISTER.

§11 FINDING-SURFACE LINKAGE [IMMUTABLE]: Each finding: [§1:S-n]. Missing -> ADVISORY-ORPHAN.

§12 CONDITIONAL RESOLUTION REGISTRY [IMMUTABLE]: DISPOSITION=CONDITIONAL -> RESOLUTION REGISTRY.

§13 g_null PROGRESSION LEDGER [IMMUTABLE]: In CROSS-ROLE SIGNALS:
  g_null(initial) | g_null(post-domain) | g_null(final) | Trajectory label

§14 FINDING SEVERITY AGGREGATION [IMMUTABLE]: Section Severity = worst(all findings). None -> LOW.

§15 LENS EXHAUSTION [IMMUTABLE]: LENS COVERAGE TABLE per section:
  | # | lens.verify Entry | Applicability (from ROLE MANIFEST) | Status | Finding Reference |
  Cite APPLICABILITY MATRIX row ID+tier. HIGH+OPEN -> ADVISORY-OPEN-LENS-REQUIRED.
  MEDIUM+OPEN -> ADVISORY-OPEN-LENS. LOW+OPEN -> cite AM row only.

§16 PRIMARY DRIVER [IMMUTABLE]: GClose=FAIL->BRACKET CLOSING; G_domain_agg=FAIL->DOMAIN;
  G_lifecycle=FAIL->LIFECYCLE; GOpen=FAIL->BRACKET OPENING; CONDITIONAL mirrors order; all PASS->N/A.

§17 NULL HYPOTHESIS DIMENSION TABLE [IMMUTABLE]
  BRACKET OPENING: | Dimension | A(0-10) | B(0-10) | C(0-10) | D1=(B-A) | D2=(B-C) | NH Verdict |
  MUST-CLEAR marked (*). Minimum 3 dimensions.
  Per-row verdict: FAVORS-BUILD(D1>0,D2>0) / CONDITIONAL(D1>0,D2<=0) / OPPOSES-BUILD(D1<=0).
  g_null: HOLDS(MUST-CLEAR OPPOSES) / DEFEATED(FAVORS majority, both D1 and D2 positive majority) /
          CONDITIONAL(otherwise).

  NH TABLE AGGREGATION RULE [EXTENDED -- universal reviewer participation; V-03 axis]:
    Column A: challenger opening score, carried forward unchanged (status-quo control arm).
    Column B (Proposed-Build): avg(ALL domain reviewer B scores + LIFECYCLE B score) per dimension.
      Formula: avg(dom_B_scores_for_dim, lifecycle_B_score_for_dim)
    Column C (Best-Non-Build-Alt): avg(ALL domain reviewer C scores + LIFECYCLE C score) per dim.
      Formula: avg(dom_C_scores_for_dim, lifecycle_C_score_for_dim)
    All three derivations pre-committed. No editorial selection at bracket closing.
    Rationale: LIFECYCLE assesses build/alt from program lens (timeline, integration cost,
    rollback risk) -- dimensions that complement domain technical evidence. Including LIFECYCLE
    B/C in the aggregation means the revised NH table reflects both technical and program
    perspectives.

  BRACKET CLOSING re-applies §17 rule to REVISED NH DIMENSION TABLE using extended aggregation.

END DISPOSITION_CONTRACT v1

---

## ROLE MANIFEST

| Slot | Archetype | Role | Rationale |
|------|-----------|------|-----------|
| CHALLENGER | inertia-advocate | [ROLE_NAME] | [One sentence.] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [One sentence.] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [One sentence.] |

### APPLICABILITY MATRIX

Complete before BRACKET OPENING. Locked.

| Row ID | Role | lens.verify Entry | Artifact Domain Covered | Artifact Applicability | Basis |
|--------|------|------------------|------------------------|----------------------|-------|
| AM-01 | [DOMAIN] | [Entry.] | [Domain.] | HIGH/MEDIUM/LOW | [Basis.] |
| AM-02 | [DOMAIN] | [Entry.] | [Domain.] | [Tier.] | [Basis.] |
| AM-03 | [DOMAIN] | [Entry.] | [Domain.] | [Tier.] | [Basis.] |
| AM-04 | [LIFECYCLE] | [Entry.] | [Domain.] | [Tier.] | [Basis.] |
| AM-05 | [LIFECYCLE] | [Entry.] | [Domain.] | [Tier.] | [Basis.] |

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**STATUS QUO VIABILITY ASSESSMENT**:

| SQ-DIM | Current State | Why Acceptable | Viability |
|--------|--------------|----------------|-----------|
| [Dim-1] | [Current practice.] | [Concrete advantage.] | HIGH/MEDIUM/LOW |
| [Dim-2] | [Current practice.] | [Advantage.] | [Viability] |
| [Dim-3] | [Current practice.] | [Advantage.] | [Viability] |

**Overall SQ Viability**: VIABLE / MARGINAL / STRETCHED

**Null hypothesis**: [One sentence: what team does today.]

**Alternatives comparison table** (score 0-10; at least 3 dimensions):

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|---------------|-----------|----------------------|-------|
| [Dim-1] | [Score] | [Score] | [Score] | |
| [Dim-2] | [Score] | [Score] | [Score] | |
| [Dim-3] | [Score] | [Score] | [Score] | |

**NULL HYPOTHESIS DIMENSION TABLE** (per §17; BRACKET CLOSING will average in LIFECYCLE scores):

| Dimension | A | B | C | D1=(B-A) | D2=(B-C) | NH Verdict |
|-----------|---|---|---|----------|----------|------------|
| [Dim-1*] | [Score] | [Score] | [Score] | [D1] | [D2] | [Verdict] |
| [Dim-2*] | [Score] | [Score] | [Score] | [D1] | [D2] | [Verdict] |
| [Dim-3] | [Score] | [Score] | [Score] | [D1] | [D2] | [Verdict] |

Applying §17 g_null derivation:
  MUST-CLEAR OPPOSES-BUILD: [list or "none"]
  count(FAVORS-BUILD)=[N] count(CONDITIONAL)=[N] count(OPPOSES-BUILD)=[N]
  DEFEATED: [Y/N]  Result: [HOLDS / CONDITIONAL / DEFEATED]

**g_null(initial)** (§9 Stage 1): [HOLDS / CONDITIONAL / DEFEATED]

**Challenge claims**:

| CH-ID | Claim | SQ-DIM | Severity |
|-------|-------|--------|---------|
| CH-001 | [Claim.] | [SQ-DIM-n] | HIGH/MEDIUM/LOW |
| CH-002 | [Claim.] | [SQ-DIM-n] | [Severity] |

**GOpen Verdict**: PASS / CONDITIONAL / FAIL
**GOpen Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [Verdict] | [Class] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [Copy.]

**CH-ID Response Table**:

| CH-ID | Claim (verbatim) | Technical Assessment | Status |
|-------|-----------------|---------------------|--------|
| CH-001 | [Copy.] | [Assessment.] | ADDRESSED/PARTIAL/OPEN |
| CH-002 | [Copy.] | [Assessment.] | [Status] |

**Domain re-score**:

| Dimension | A | B | C | Rationale |
|-----------|---|---|---|-----------|
| [Dim-1] | [Score] | [Score] | [Score] | [vs. challenger.] |
| [Dim-2] | [Score] | [Score] | [Score] | |

**NH Dimension Scores** (for §17 extended aggregation -- paired with LIFECYCLE at bracket closing):

| Dimension | Your Build Score (B) | Your Best-Alt Score (C) |
|-----------|---------------------|------------------------|
| [Dim-1] | [Score] | [Score] |
| [Dim-2] | [Score] | [Score] |
| [Dim-3] | [Score] | [Score] |

**Findings** (cite §1 surfaces; §14):

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [Finding.] | HIGH/MEDIUM/LOW |
| F-2 | [§1:S-n] | [Finding.] | [Severity] |

**Severity Aggregation**: worst(F-1=[_], ...) = [SECTION_SEVERITY]

**Lens Coverage Table**:

| # | lens.verify Entry | Applicability (ROLE MANIFEST) | Status | Finding Ref |
|---|------------------|------------------------------|--------|------------|
| Q-1 | [Entry.] | AM-01: [tier] | ADDRESSED/OPEN | [F-n or AM cite] |
| Q-2 | [Entry.] | AM-02: [tier] | [Status] | [Ref] |

**G_domain Verdict**: PASS / CONDITIONAL / FAIL   **G_domain Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | [Verdict] | [Class] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT (EXCLUDED from ledger)

G_domain_agg = worst([list]) = [result]
g_null(post-domain) per §9 Stage 2: [derivation] = [result]

**G_domain Aggregate**: [Result.] | **g_null(post-domain)**: [Result.]

---

## §3.8 CH-ID SATURATION CHECK (EXCLUDED from ledger)

| CH-ID | DOMAIN Status | Pre-LIFECYCLE Saturation |
|-------|--------------|--------------------------|
| CH-001 | [Copy.] | SATURATED / UNSATURATED |
| CH-002 | [Copy.] | [Status] |

Unsaturated: [list or "None"]

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received: GOpen=[copy] | G_domain_agg=[copy] | g_null(post-domain)=[copy]

**CH-ID Response Table**:

| CH-ID | Claim | Commitment-Frame Response | Status |
|-------|-------|--------------------------|--------|
| CH-001 | [Copy.] | [Program perspective.] | ADDRESSED/PARTIAL/OPEN |
| CH-002 | [Copy.] | [Response.] | [Status] |

**COMMITMENT-READINESS MATRIX**:

| CRM Dimension | Current State | Required State | Gap | Severity |
|---------------|--------------|----------------|-----|---------|
| Timeline | [Current.] | [Required.] | [Gap.] | HIGH/MEDIUM/LOW |
| Resources | [Current.] | [Required.] | [Gap.] | [Severity] |
| Rollback | [Current.] | [Required.] | [Gap.] | [Severity] |
| Stakeholder Alignment | [Current.] | [Required.] | [Gap.] | [Severity] |

**CRM Severity**: worst([list]) = [CRM_SEVERITY]

**NH Dimension Scores** (V-03 AXIS: LIFECYCLE participates in §17 EXTENDED aggregation)

Assess the build/alt comparison from your program lens. For each §17 dimension, score how
well Build (vs. Best-Alt) performs from a commitment-readiness perspective: schedule
predictability, integration overhead, rollback reversibility, stakeholder confidence.
BRACKET CLOSING averages your scores with DOMAIN scores per the §17 EXTENDED NH AGGREGATION.

| Dimension | Your Build Score (B) | Your Best-Alt Score (C) | Program Rationale |
|-----------|---------------------|------------------------|--------------------|
| [§17 Dim-1] | [0-10] | [0-10] | [One sentence program perspective.] |
| [§17 Dim-2] | [0-10] | [0-10] | [Rationale.] |
| [§17 Dim-3] | [0-10] | [0-10] | [Rationale.] |

**Decision-readiness assessment**: [One paragraph: GOpen, G_domain_agg, g_null(post-domain), CRM Signal.]

**Null hypothesis status**: [One sentence citing g_null(post-domain) explicitly.]

**Findings** (cite §1 surfaces):

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | [Commitment concern.] | HIGH/MEDIUM/LOW |
| F-2 | [§1:S-n] | [Finding.] | [Severity] |

**Severity Aggregation**: worst([list]) = [SECTION_SEVERITY]

**Lens Coverage Table**:

| # | lens.verify Entry | Applicability (ROLE MANIFEST) | Status | Finding Ref |
|---|------------------|------------------------------|--------|------------|
| Q-1 | [Entry.] | AM-04: [tier] | ADDRESSED/OPEN | [F-n or AM cite] |
| Q-2 | [Entry.] | AM-05: [tier] | [Status] | [Ref] |

**G_lifecycle Verdict**: PASS / CONDITIONAL / FAIL   **G_lifecycle Reason**: [One sentence.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| LIFECYCLE -- [ROLE_NAME] | G_lifecycle | [Verdict] | [Class] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**STATUS QUO VERDICT**:

| SQ-DIM | Opening | Changed By | Revised |
|--------|---------|------------|---------|
| [Dim-1] | [Opening.] | [Finding or "none".] | VIABLE/MARGINAL/STRETCHED |
| [Dim-2] | [Opening.] | [Finding.] | [Revised.] |

**SQ Viability Trajectory**: REINFORCED / UNCHANGED / WEAKENED

Applying §9 Stage 3:
  g_null(post-domain)=[copy] | G_lifecycle=[copy] -> g_null(final)=[derivation]
**g_null(final)**: [Result.]

**Revised NULL HYPOTHESIS DIMENSION TABLE** (§17 EXTENDED aggregation -- all reviewers):

| Dimension | A (carry forward) | B (avg DOM+LIFE) | C (avg DOM+LIFE) | D1 | D2 | NH Verdict |
|-----------|------------------|-----------------|-----------------|----|----|------------|
| [Dim-1*] | [A] | [avg] | [avg] | [D1] | [D2] | [Verdict] |
| [Dim-2*] | [A] | [avg] | [avg] | [D1] | [D2] | [Verdict] |
| [Dim-3] | [A] | [avg] | [avg] | [D1] | [D2] | [Verdict] |

NH AGGREGATION (extended -- domain + lifecycle):
  Col A: opener values unchanged
  Col B per dim: Dim-1: avg(DOM=[_], LIFE=[_])=[result]; Dim-2: avg(...)=[result]
  Col C per dim: Dim-1: avg(DOM=[_], LIFE=[_])=[result]; Dim-2: avg(...)=[result]

Applying §17 to revised table:
  MUST-CLEAR OPPOSES-BUILD: [list or "none"]
  DEFEATED: [Y/N]  Result: [HOLDS / CONDITIONAL / DEFEATED]

**Full CH-ID Saturation**:

| CH-ID | DOMAIN | LIFECYCLE | Full Saturation |
|-------|--------|-----------|-----------------|
| CH-001 | [Copy.] | [Copy.] | FULLY SATURATED / UNSATURATED |
| CH-002 | [Copy.] | [Copy.] | [Status] |

**GClose Verdict**: PASS / CONDITIONAL / FAIL
**Override invoked**: YES / NO
**GClose Rationale**: [2-3 sentences: g_null(final), CH-ID saturation, SQ Viability,
CRM Signal. Note whether LIFECYCLE NH scores shifted revised table: LIFECYCLE-AMPLIFIED,
LIFECYCLE-NEUTRAL, or LIFECYCLE-ATTENUATED.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [Verdict] | [Class] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION (EXCLUDED from ledger)

Surface Coverage:
| IN-SCOPE Surface | Reviewer(s) | Finding Refs | Coverage |
|-----------------|-------------|--------------|----------|
| [Surface 1.] | [Reviewer.] | [F-n.] | COVERED/GAP |

Signal: COVERED / PARTIAL

Domain Coverage Gap-Check (per §10a):
| Artifact Domain | HIGH-Applicability MATRIX Rows | Coverage |
|----------------|-------------------------------|----------|
| [Domain.] | [AM rows or "none".] | COVERED/ADVISORY-GAP |

§11 ADVISORY-ORPHAN check: [Orphans or "None".]

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract Cite |
|------|----------|---------|---------------|
| GOpen | [CHALLENGER] | [Verdict] | DISPOSITION_CONTRACT v1 |
| G_domain_agg | [DOMAIN] | [Verdict] | DISPOSITION_CONTRACT v1 |
| G_lifecycle | [LIFECYCLE] | [Verdict] | DISPOSITION_CONTRACT v1 |
| GClose | [CHALLENGER] | [Verdict] | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [Or "None".]
**Convergence**: [2+ reviewer agreement.]
**Scope coverage**: [Uncovered surfaces or "None".]

**§13 PROGRESSION LEDGER**:
  g_null(initial)=[copy] | g_null(post-domain)=[copy] | g_null(final)=[copy] | Trajectory=[label]

**NH chain note**: State whether LIFECYCLE NH scores shifted the revised table compared to
domain-only averaging: LIFECYCLE-AMPLIFIED (LIFE scores higher than DOM), LIFECYCLE-NEUTRAL
(within 1 pt per dimension), or LIFECYCLE-ATTENUATED (LIFE scores lower). Note if direction
change was material to g_null(final) verdict.

---

## DISPOSITION

Gate vector: GOpen=[copy] | G_domain_agg=[copy] | G_lifecycle=[copy] | GClose=[copy]

Apply §3 mechanically: GClose=FAIL->BLOCKED; any Gi=FAIL->BLOCKED; any COND->CONDITIONAL; all PASS->READY.

**Overall Disposition**: READY / CONDITIONAL / BLOCKED
**Applying §16 rule**: [n + reason.]  **Primary Driver**: [result]

**Conditions** (CONDITIONAL only): [State conditions.]
**Blocker** (BLOCKED only): [Finding from FAIL gate.]

**RESOLUTION REGISTRY**: [Table if CONDITIONAL, else "N/A -- disposition is [value]".]

---

## ACTION ITEM REGISTER (copy gate ledger rows verbatim; do not re-derive)

| Source | CH-ID / Finding | Item Description | Class | Owner | Criterion |
|--------|----------------|-----------------|-------|-------|-----------|
| Gate ledger copy | -- | [Verbatim.] | [Class] | [Role] | [Criterion] |
| CH-ID | CH-00n | [What to resolve.] | [Class] | [Role] | [Criterion] |
| Lens HIGH | AM-0n/Q-n | ADVISORY-OPEN-LENS-REQUIRED: [entry]. | ADVISORY | [Role] | Produce finding. |
| Lens MEDIUM | AM-0n/Q-n | ADVISORY-OPEN-LENS: [entry]. | ADVISORY | [Role] | Address or justify. |
| Scope gap | -- | ADVISORY-GAP: §1 surface [name]. | ADVISORY | [Role] | Assign reviewer. |
| Domain gap | -- | ADVISORY-GAP (DOMAIN): [domain]. | ADVISORY | [Role] | Add HIGH reviewer. |
| Orphan | -- | ADVISORY-ORPHAN: [F-n] lacks §1:S-n. | ADVISORY | [Role] | Re-assign. |

---

**Artifact to review:**

{{artifact}}

---

## V-04

**Axes**: Inertia framing + Output format (V-01 + V-02 combined).

**Hypothesis**: V-01 (§0 NULL HYPOTHESIS CHARTER) pre-commits the challenger's specific null
arguments and requires downstream §0:Arg-n citations in every CH-ID claim; BRACKET CLOSING
audits Charter coverage. V-02 (§18 GLOBAL F-ID REGISTRY) gives every finding a globally unique
cross-section ID, making all downstream references (ACTION ITEM REGISTER, SCOPE COVERAGE
RECONCILIATION, LENS COVERAGE TABLE) use globally addressable finding identifiers. Combined:
the review has both a pre-committed argument traceability layer (V-01) and a pre-committed
finding addressability layer (V-02). The two axes are orthogonal: V-01 operates on challenge
argument coverage; V-02 operates on finding identification. Together they close the two
remaining editorial gaps at the top (null argument pre-commitment) and bottom (finding
cross-reference) of the review structure.

---

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .roles/signal/
```

Emit this block first.

```
## Review Parameters
Artifact:     {{artifact_id}}
Depth:        {{depth}}
Reviewer set: {{reviewer_set}}
```

---

You are running `org-review` on the artifact provided below.

You will play four roles in sequence: inertia-advocate challenger (opening), domain-expert
reviewer, lifecycle/program reviewer, and challenger again (closing).

Fill in all required fields. Do not alter, reorder, or omit any pre-printed heading, label,
formula, or structural element. If a field is not applicable, write "N/A -- " followed by
the reason.

---

NULL HYPOTHESIS CHARTER §0 [IMMUTABLE -- complete before DISPOSITION_CONTRACT]

The challenger commits their best null case here before any contract executes.
Every CH-ID claim in BRACKET OPENING must cite one §0 argument: [§0:Arg-n].
A claim without §0 citation is CHARTER-ORPHAN -- flag inline and add to ACTION ITEM REGISTER.
BRACKET CLOSING emits a Charter Coverage Audit (§17a) over these arguments.

Null statement (one sentence): [What does the team currently do instead of building this?]

Charter arguments:
  §0:Arg-1 -- [First null argument. Name the concrete status-quo advantage. State the minimum
               evidence that would defeat this argument.]
  §0:Arg-2 -- [Second argument. Same format.]
  §0:Arg-3 -- [Third argument or omit if fewer than three are meaningful.]

Defeat threshold (pre-committed): This null hypothesis is defeated only when ALL hold:
  (a) §17 g_null = DEFEATED (table formula applied mechanically)
  (b) BRACKET CLOSING Charter Coverage Audit shows zero CHARTER-GAP arguments
  (c) CH-ID saturation FULLY SATURATED per §8

§0 COMPLETE

---

DISPOSITION_CONTRACT v1 [IMMUTABLE]

§1 SCOPE ENUMERATION
IN-SCOPE (§5.5 + §11; each surface: [DOMAIN: label]):
  1. [SURFACE_1] [DOMAIN: label]
  2. [SURFACE_2] [DOMAIN: label]
  3. [SURFACE_3] [DOMAIN: label]
OUT-OF-SCOPE: 1. [SURFACE -- REASON]
Scope Amendment: SCOPE AMENDMENT: [surface] -- [reason]; silent expansion violates.
§1 COMPLETE

§2 SEVERITY [IMMUTABLE]: HIGH=Blocks. MEDIUM=Conditions. LOW=Advisory.

§3 DISPOSITION ALGEBRA [IMMUTABLE]:
  BLOCKED if GClose=FAIL or any Gi=FAIL. CONDITIONAL if no FAIL, some CONDITIONAL. READY if all PASS.

§3a DOMAIN-AGGREGATE [IMMUTABLE]: G_domain_agg = worst(all G_domain rows).

§4 CONTRACT CITE [IMMUTABLE]: Each section: "Contract: DISPOSITION_CONTRACT v1"

§5 CH-ID TRACING [IMMUTABLE]: Claims receive CH-IDs. Each claim also carries [§0:Arg-n].
  CHARTER-ORPHAN if §0 citation absent. Downstream sections carry CH-ID table.
  PASS prohibited if any CH-ID OPEN.

§6 LOCAL GATE LEDGER [IMMUTABLE]:
  Row: | Section | Gate | Verdict | Class | EXCLUDED: §3.5, §3.8, §5.5.

§7 SECTION ORDER [IMMUTABLE]: ROLE MANIFEST -> BRACKET OPENING -> DOMAIN(s) ->
  §3.5 -> §3.8 -> LIFECYCLE -> BRACKET CLOSING -> §5.5 -> GATE VECTOR TABLE ->
  CROSS-ROLE SIGNALS -> DISPOSITION -> ACTION ITEM REGISTER.

§8 CH-ID SATURATION [IMMUTABLE]: FULLY SATURATED = DOMAIN+LIFECYCLE responses. PASS prohibited
  without saturation or waiver.

§9 NULL HYPOTHESIS PROGRESSION [IMMUTABLE]:
  Stage 1: g_null(initial)=§17 formula at BRACKET OPENING.
  Stage 2 at §3.5: FAIL->FAIL; CONDITIONAL->max(initial,COND); PASS->initial.
  Stage 3 at BRACKET CLOSING: FAIL->FAIL; CONDITIONAL->max(post-domain,COND); PASS->post-domain.
  GClose must equal g_null(final).

§10 SCOPE COVERAGE [IMMUTABLE]: §5.5 maps §1 surfaces. GAP -> ADVISORY-GAP. Also runs §10a.

§10a DOMAIN GAP-CHECK [IMMUTABLE]: Group by [DOMAIN: label]. ADVISORY-GAP where no HIGH row.

§11 FINDING-SURFACE LINKAGE [IMMUTABLE]: [§1:S-n] on each finding. Missing -> ADVISORY-ORPHAN.

§12 CONDITIONAL RESOLUTION REGISTRY [IMMUTABLE]: CONDITIONAL -> RESOLUTION REGISTRY table.

§13 g_null PROGRESSION LEDGER [IMMUTABLE]: In CROSS-ROLE SIGNALS.

§14 FINDING SEVERITY AGGREGATION [IMMUTABLE]: Section Severity = worst(all findings). None -> LOW.

§15 LENS EXHAUSTION [IMMUTABLE]: LENS COVERAGE TABLE per section. HIGH+OPEN -> REQUIRED.

§16 PRIMARY DRIVER [IMMUTABLE]: GClose=FAIL->BRACKET CLOSING; G_domain_agg=FAIL->DOMAIN; etc.

§17 NULL HYPOTHESIS DIMENSION TABLE [IMMUTABLE]
  BRACKET OPENING: three-column table (A=Status-Quo, B=Build, C=Best-Alt; D1=B-A, D2=B-C).
  MUST-CLEAR marked (*). Min 3 dimensions.
  Per-row: FAVORS-BUILD(D1>0,D2>0) / CONDITIONAL(D1>0,D2<=0) / OPPOSES-BUILD(D1<=0).
  g_null: HOLDS(MUST-CLEAR OPPOSES) / DEFEATED(FAVORS majority + both D1,D2 positive) / CONDITIONAL.
  NH TABLE AGGREGATION RULE: A=opener (unchanged). B=avg(domain B scores). C=avg(domain C scores).
  BRACKET CLOSING re-applies §17 rule to revised table.

§17a NULL HYPOTHESIS CHARTER COVERAGE AUDIT [IMMUTABLE]
  BRACKET CLOSING emits before GClose verdict:
    | §0 Arg | Summary | Addressed By CH-IDs | Coverage |
  COVERED = at least one CH-ID cited this arg AND domain/lifecycle responded ADDRESSED or PARTIAL.
  CHARTER-GAP = no CH-ID cited this arg, or all citees remain OPEN at closing.
  CHARTER-GAP args -> ACTION ITEM REGISTER as ADVISORY-CHARTER-GAP.

§18 GLOBAL F-ID REGISTRY [IMMUTABLE]
  Every finding receives a globally unique identifier:
    F-OPEN-{nn} (BRACKET OPENING), F-DOM-{nn} (DOMAIN), F-LIFE-{nn} (LIFECYCLE)
    Multi-domain: F-DOM1-{nn}, F-DOM2-{nn}, ...
  Counters are per-prefix, sequential within each section.
  All downstream references (ACTION ITEM REGISTER, §5.5, LENS COVERAGE TABLE Finding Reference,
  CH-ID response tables) MUST use global F-IDs. Per-section F-1/F-2 local aliases NOT used.
  GATE VECTOR TABLE records leading F-ID (highest severity) per gate.

END DISPOSITION_CONTRACT v1

---

## ROLE MANIFEST

| Slot | Archetype | Role | Rationale |
|------|-----------|------|-----------|
| CHALLENGER | inertia-advocate | [ROLE_NAME] | [One sentence.] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [One sentence.] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [One sentence.] |

### APPLICABILITY MATRIX (locked before BRACKET OPENING)

| Row ID | Role | lens.verify Entry | Artifact Domain Covered | Artifact Applicability | Basis |
|--------|------|------------------|------------------------|----------------------|-------|
| AM-01 | [DOMAIN] | [Entry.] | [Domain.] | HIGH/MEDIUM/LOW | [Basis.] |
| AM-02 | [DOMAIN] | [Entry.] | [Domain.] | [Tier.] | [Basis.] |
| AM-03 | [DOMAIN] | [Entry.] | [Domain.] | [Tier.] | [Basis.] |
| AM-04 | [LIFECYCLE] | [Entry.] | [Domain.] | [Tier.] | [Basis.] |
| AM-05 | [LIFECYCLE] | [Entry.] | [Domain.] | [Tier.] | [Basis.] |

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**STATUS QUO VIABILITY ASSESSMENT**:

| SQ-DIM | Current State | Why Acceptable | Viability |
|--------|--------------|----------------|-----------|
| [Dim-1] | [Current practice.] | [Concrete advantage.] | HIGH/MEDIUM/LOW |
| [Dim-2] | [Current practice.] | [Advantage.] | [Viability] |
| [Dim-3] | [Current practice.] | [Advantage.] | [Viability] |

**Overall SQ Viability**: VIABLE / MARGINAL / STRETCHED

**Null hypothesis**: [One sentence: current practice named.]

**Alternatives comparison table** (0-10; 3+ dimensions):

| Dimension | A | B | C | Notes |
|-----------|---|---|---|-------|
| [Dim-1] | [Score] | [Score] | [Score] | |
| [Dim-2] | [Score] | [Score] | [Score] | |
| [Dim-3] | [Score] | [Score] | [Score] | |

**NULL HYPOTHESIS DIMENSION TABLE** (per §17):

| Dimension | A | B | C | D1=(B-A) | D2=(B-C) | NH Verdict |
|-----------|---|---|---|----------|----------|------------|
| [Dim-1*] | [Score] | [Score] | [Score] | [D1] | [D2] | [Verdict] |
| [Dim-2*] | [Score] | [Score] | [Score] | [D1] | [D2] | [Verdict] |
| [Dim-3] | [Score] | [Score] | [Score] | [D1] | [D2] | [Verdict] |

Applying §17: MUST-CLEAR OPPOSES=[list or "none"]; count(FAV)=[N] count(COND)=[N] count(OPP)=[N];
  DEFEATED=[Y/N]; Result=[HOLDS/CONDITIONAL/DEFEATED]
**g_null(initial)**: [Result] (§9 Stage 1)

*(Findings in BRACKET OPENING use global F-IDs per §18: F-OPEN-01, F-OPEN-02, ...)*

**Challenge claims** (each cites SQ-DIM and §0:Arg-n; CHARTER-ORPHAN if §0 citation absent):

| CH-ID | Claim | SQ-DIM | §0 Arg | Severity |
|-------|-------|--------|--------|---------|
| CH-001 | [Claim.] | [SQ-DIM-n] | §0:Arg-[n] | HIGH/MEDIUM/LOW |
| CH-002 | [Claim.] | [SQ-DIM-n] | §0:Arg-[n] | [Severity] |
| CH-003 | [Claim or omit.] | [SQ-DIM-n] | §0:Arg-[n] | [Severity] |

**GOpen Verdict**: PASS / CONDITIONAL / FAIL
**GOpen Reason**: [One sentence.]
**Leading F-ID**: F-OPEN-[nn] or "N/A -- no findings"

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [Verdict] | [Class] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: [Copy.]
*(All findings: F-DOM-{nn} per §18)*

**CH-ID Response Table**:

| CH-ID | Claim (verbatim) | Technical Assessment | Status |
|-------|-----------------|---------------------|--------|
| CH-001 | [Copy.] | [Assessment.] | ADDRESSED/PARTIAL/OPEN |
| CH-002 | [Copy.] | [Assessment.] | [Status] |

**Domain re-score**:

| Dimension | A | B | C | Rationale |
|-----------|---|---|---|-----------|
| [Dim-1] | [Score] | [Score] | [Score] | [vs. challenger.] |
| [Dim-2] | [Score] | [Score] | [Score] | |

**NH Dimension Scores** (for §17 aggregation):

| Dimension | Your B | Your C |
|-----------|--------|--------|
| [Dim-1] | [Score] | [Score] |
| [Dim-2] | [Score] | [Score] |
| [Dim-3] | [Score] | [Score] |

**Findings** (global F-IDs; §1 citations; §14):

| # | Global F-ID | §1 Surface | Finding | Severity |
|---|-------------|-----------|---------|---------|
| 1 | F-DOM-01 | [§1:S-n] | [Finding.] | HIGH/MEDIUM/LOW |
| 2 | F-DOM-02 | [§1:S-n] | [Finding.] | [Severity] |

**Severity Aggregation**: worst(F-DOM-01=[_], ...) = [SECTION_SEVERITY]

**Lens Coverage Table**:

| # | lens.verify Entry | Applicability (ROLE MANIFEST) | Status | Finding Ref |
|---|------------------|------------------------------|--------|------------|
| Q-1 | [Entry.] | AM-01: [tier] | ADDRESSED/OPEN | F-DOM-[nn] or AM cite |
| Q-2 | [Entry.] | AM-02: [tier] | [Status] | [Ref] |

**G_domain Verdict**: PASS / CONDITIONAL / FAIL
**G_domain Reason**: [One sentence.]
**Leading F-ID**: F-DOM-[nn]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | [Verdict] | [Class] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT (EXCLUDED from ledger)

G_domain_agg=worst([list])=[result]; g_null(post-domain)=[§9 Stage 2 derivation]=[result]

---

## §3.8 CH-ID SATURATION CHECK (EXCLUDED from ledger)

| CH-ID | DOMAIN | Pre-LIFECYCLE Saturation |
|-------|--------|--------------------------|
| CH-001 | [Copy.] | SATURATED/UNSATURATED |
| CH-002 | [Copy.] | [Status] |

Unsaturated: [list or "None"]

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received: GOpen=[copy] | G_domain_agg=[copy] | g_null(post-domain)=[copy]
*(All findings: F-LIFE-{nn} per §18)*

**CH-ID Response Table**:

| CH-ID | Claim | Response | Status |
|-------|-------|----------|--------|
| CH-001 | [Copy.] | [Program perspective.] | ADDRESSED/PARTIAL/OPEN |
| CH-002 | [Copy.] | [Response.] | [Status] |

**COMMITMENT-READINESS MATRIX**:

| CRM Dimension | Current State | Required State | Gap | Severity |
|---------------|--------------|----------------|-----|---------|
| Timeline | [Current.] | [Required.] | [Gap.] | HIGH/MEDIUM/LOW |
| Resources | [Current.] | [Required.] | [Gap.] | [Severity] |
| Rollback | [Current.] | [Required.] | [Gap.] | [Severity] |
| Stakeholder Alignment | [Current.] | [Required.] | [Gap.] | [Severity] |

**CRM Severity**: worst([list]) = [CRM_SEVERITY]

**Decision-readiness assessment**: [One paragraph: GOpen, G_domain_agg, g_null(post-domain), CRM Signal.]
**Null hypothesis status**: [One sentence with g_null(post-domain) value.]

**Findings** (global F-IDs; §1 citations):

| # | Global F-ID | §1 Surface | Finding | Severity |
|---|-------------|-----------|---------|---------|
| 1 | F-LIFE-01 | [§1:S-n] | [Concern.] | HIGH/MEDIUM/LOW |
| 2 | F-LIFE-02 | [§1:S-n] | [Finding.] | [Severity] |

**Severity Aggregation**: worst([list]) = [SECTION_SEVERITY]

**Lens Coverage Table**:

| # | lens.verify Entry | Applicability (ROLE MANIFEST) | Status | Finding Ref |
|---|------------------|------------------------------|--------|------------|
| Q-1 | [Entry.] | AM-04: [tier] | ADDRESSED/OPEN | F-LIFE-[nn] or AM cite |
| Q-2 | [Entry.] | AM-05: [tier] | [Status] | [Ref] |

**G_lifecycle Verdict**: PASS / CONDITIONAL / FAIL
**G_lifecycle Reason**: [One sentence.]
**Leading F-ID**: F-LIFE-[nn]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| LIFECYCLE -- [ROLE_NAME] | G_lifecycle | [Verdict] | [Class] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**STATUS QUO VERDICT**:

| SQ-DIM | Opening | Changed By | Revised |
|--------|---------|------------|---------|
| [Dim-1] | [Opening.] | [Global F-ID or "none".] | VIABLE/MARGINAL/STRETCHED |
| [Dim-2] | [Opening.] | [F-ID.] | [Revised.] |

**SQ Viability Trajectory**: REINFORCED / UNCHANGED / WEAKENED

Applying §9 Stage 3: g_null(final)=[derivation]=[result]

**Revised NULL HYPOTHESIS DIMENSION TABLE** (§17 aggregation):

| Dimension | A | B (avg domain) | C (avg domain) | D1 | D2 | NH Verdict |
|-----------|---|---------------|---------------|----|----|------------|
| [Dim-1*] | [A] | [avg] | [avg] | [D1] | [D2] | [Verdict] |
| [Dim-2*] | [A] | [avg] | [avg] | [D1] | [D2] | [Verdict] |
| [Dim-3] | [A] | [avg] | [avg] | [D1] | [D2] | [Verdict] |

Col B averages: [derivations]; Col C averages: [derivations]
Applying §17: DEFEATED=[Y/N]; Result=[HOLDS/CONDITIONAL/DEFEATED]

**§17a CHARTER COVERAGE AUDIT** (per §17a):

| §0 Arg | Summary | Addressed By | Coverage |
|--------|---------|--------------|----------|
| §0:Arg-1 | [Summary.] | [CH-IDs that cited this.] | COVERED/CHARTER-GAP |
| §0:Arg-2 | [Summary.] | [CH-IDs.] | [Coverage] |
| §0:Arg-3 | [Summary or N/A.] | [CH-IDs.] | [Coverage] |

CHARTER-GAP items: [List or "None".]

**Full CH-ID Saturation**:

| CH-ID | DOMAIN | LIFECYCLE | Full Saturation |
|-------|--------|-----------|-----------------|
| CH-001 | [Copy.] | [Copy.] | FULLY SATURATED/UNSATURATED |
| CH-002 | [Copy.] | [Copy.] | [Status] |

**GClose Verdict**: PASS if g_null=DEFEATED, CH-IDs fully saturated, zero CHARTER-GAP. Otherwise CONDITIONAL/FAIL.
**Override invoked**: YES / NO
**GClose Rationale**: [2-3 sentences: g_null(final), CH-ID saturation, SQ Trajectory,
Charter Coverage Audit result, CRM Signal.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [Verdict] | [Class] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION (EXCLUDED from ledger)

Surface Coverage (references use global F-IDs):

| IN-SCOPE Surface | Reviewer(s) | Global F-IDs | Coverage |
|-----------------|-------------|--------------|----------|
| [Surface 1.] | [Reviewer.] | [F-DOM-01, ...] | COVERED/GAP |

Coverage signal: COVERED / PARTIAL

Domain Coverage Gap-Check (§10a):
| Artifact Domain | HIGH-Applicability MATRIX Rows | Coverage |
|----------------|-------------------------------|----------|
| [Domain.] | [AM rows or "none".] | COVERED/ADVISORY-GAP |

§11 ADVISORY-ORPHAN check: [Orphans or "None".]

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Leading F-ID | Contract Cite |
|------|----------|---------|-------------|---------------|
| GOpen | [CHALLENGER] | [Verdict] | F-OPEN-[nn] or N/A | DISPOSITION_CONTRACT v1 |
| G_domain_agg | [DOMAIN] | [Verdict] | F-DOM-[nn] | DISPOSITION_CONTRACT v1 |
| G_lifecycle | [LIFECYCLE] | [Verdict] | F-LIFE-[nn] | DISPOSITION_CONTRACT v1 |
| GClose | [CHALLENGER] | [Verdict] | N/A | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [Or "None".]
**Convergence**: [2+ reviewer agreement; cite global F-IDs.]
**Scope coverage**: [Uncovered or "None".]

§13 PROGRESSION LEDGER:
  g_null(initial)=[copy] | g_null(post-domain)=[copy] | g_null(final)=[copy] | Trajectory=[label]

---

## DISPOSITION

Gate vector: GOpen=[copy] | G_domain_agg=[copy] | G_lifecycle=[copy] | GClose=[copy]
Apply §3. **Overall Disposition**: READY / CONDITIONAL / BLOCKED
**§16 Primary Driver**: [rule n + reason + result]
**Conditions** (CONDITIONAL): [conditions] | **Blocker** (BLOCKED): [global F-ID from FAIL gate]
**RESOLUTION REGISTRY**: [Table or "N/A -- disposition is [value]".]

---

## ACTION ITEM REGISTER (verbatim gate ledger copy; global F-IDs throughout)

| Source | Global F-ID / CH-ID | Item | Class | Owner | Criterion |
|--------|--------------------|----|-------|-------|-----------|
| Gate ledger | -- | [Verbatim: Section/Gate/Verdict/Class.] | [Class] | [Role] | [Criterion] |
| CH-ID | CH-00n | [Resolve.] | [Class] | [Role] | [Criterion] |
| Lens HIGH | AM-0n/Q-n | ADVISORY-OPEN-LENS-REQUIRED: [entry]. | ADVISORY | [Role] | Produce finding. |
| Lens MEDIUM | AM-0n/Q-n | ADVISORY-OPEN-LENS: [entry]. | ADVISORY | [Role] | Address or justify. |
| Scope gap | -- | ADVISORY-GAP: [surface]. | ADVISORY | [Role] | Assign reviewer. |
| Domain gap | -- | ADVISORY-GAP (DOMAIN): [domain]. | ADVISORY | [Role] | Add HIGH reviewer. |
| Orphan | F-{PRE}-[nn] | ADVISORY-ORPHAN: [F-ID] lacks §1:S-n. | ADVISORY | [Role] | Re-assign. |
| Charter gap | §0:Arg-n | ADVISORY-CHARTER-GAP: §0:Arg-n not addressed by any CH-ID claim. | ADVISORY | [CHALLENGER] | Issue claim citing arg or declare waiver. |

---

**Artifact to review:**

{{artifact}}

---

## V-05

**Axes**: All three -- Inertia framing (V-01) + Output format (V-02) + Lifecycle emphasis (V-03).

**Hypothesis**: V-01 closes the null argument pre-commitment gap (§0 CHARTER + §17a AUDIT).
V-02 closes the finding addressability gap (§18 GLOBAL F-ID). V-03 closes the NH aggregation
completeness gap (LIFECYCLE contributes B/C scores to §17 extended aggregation). Each axis
addresses a distinct structural gap at a different layer: V-01 at the inertia argument layer,
V-02 at the finding identification layer, V-03 at the NH evidence aggregation layer. The
three are mutually reinforcing: V-01 makes the challenger's argument pre-committed;
V-02 makes findings globally addressable; V-03 makes the NH revised table reflect all
reviewer perspectives. The combined prompt is the most complete chain from pre-commitment
(§0 Charter) through evidence aggregation (§17 extended) through finding traceability
(§18 global F-IDs) to audit (§17a Charter Coverage Audit referencing global F-IDs).

---

```
{{artifact_id}}   -- identifier or short name of the artifact under review
{{depth}}         -- standard | deep
{{reviewer_set}}  -- "auto" or comma-separated role names from .roles/signal/
```

Emit this block first.

```
## Review Parameters
Artifact:     {{artifact_id}}
Depth:        {{depth}}
Reviewer set: {{reviewer_set}}
```

---

You are running `org-review` on the artifact provided below.

You will play four roles in sequence: an inertia-advocate challenger (opening and closing),
a domain-expert reviewer, and a lifecycle/program reviewer. All reviewer archetypes contribute
NH dimension scores to the bracket closing aggregation. The challenger commits their null
arguments before any contract runs.

Fill in all required fields. Do not alter, reorder, or omit any pre-printed heading, label,
formula, or structural element. If inapplicable, write "N/A -- " followed by the reason.

---

NULL HYPOTHESIS CHARTER §0 [IMMUTABLE -- complete before DISPOSITION_CONTRACT]

Null statement: [What the team currently does instead of building this.]

Charter arguments:
  §0:Arg-1 -- [Name the first status-quo advantage. State minimum evidence to defeat it.]
  §0:Arg-2 -- [Second argument. Same format.]
  §0:Arg-3 -- [Third argument or omit.]

Defeat threshold: This null hypothesis is defeated only when ALL hold:
  (a) §17 g_null = DEFEATED (extended aggregation: domain + lifecycle scores)
  (b) §17a Charter Coverage Audit: zero CHARTER-GAP arguments
  (c) §8 CH-ID saturation: FULLY SATURATED

§0 COMPLETE

---

DISPOSITION_CONTRACT v1 [IMMUTABLE]

§1 SCOPE (§5.5 + §11; [DOMAIN: label] on each surface):
  1. [SURFACE_1] [DOMAIN: label]  2. [SURFACE_2] [DOMAIN: label]  3. [SURFACE_3] [DOMAIN: label]
OUT-OF-SCOPE: 1. [SURFACE -- REASON]
Scope Amendment: declare with SCOPE AMENDMENT tag; silent expansion violates.
§1 COMPLETE

§2 SEVERITY [IMMUTABLE]: HIGH=Blocks. MEDIUM=Conditions. LOW=Advisory.

§3 DISPOSITION ALGEBRA [IMMUTABLE]:
  BLOCKED(GClose=FAIL or any Gi=FAIL) / CONDITIONAL(no FAIL, some COND) / READY(all PASS).

§3a DOMAIN-AGGREGATE [IMMUTABLE]: G_domain_agg=worst(all G_domain rows).

§4 CONTRACT CITE [IMMUTABLE]: "Contract: DISPOSITION_CONTRACT v1" opens each reviewer section.

§5 CH-ID TRACING [IMMUTABLE]: CH-IDs on all claims. Each claim carries [§0:Arg-n].
  CHARTER-ORPHAN if §0 absent. CH-ID response table in all downstream sections.
  PASS prohibited if any CH-ID OPEN.

§6 LOCAL GATE LEDGER [IMMUTABLE]: | Section | Gate | Verdict | Class |
  EXCLUDED: §3.5, §3.8, §5.5.

§7 SECTION ORDER [IMMUTABLE]: ROLE MANIFEST -> BRACKET OPENING -> DOMAIN(s) ->
  §3.5 -> §3.8 -> LIFECYCLE -> BRACKET CLOSING -> §5.5 -> GATE VECTOR TABLE ->
  CROSS-ROLE SIGNALS -> DISPOSITION -> ACTION ITEM REGISTER.

§8 CH-ID SATURATION [IMMUTABLE]: FULLY SATURATED=DOMAIN+LIFECYCLE before BRACKET CLOSING.
  PASS prohibited without saturation or waiver.

§9 NULL HYPOTHESIS PROGRESSION [IMMUTABLE]:
  Stage 1: g_null(initial)=§17 formula output at BRACKET OPENING.
  Stage 2 at §3.5: FAIL->FAIL; COND->max(initial,COND); PASS->initial.
  Stage 3 at BRACKET CLOSING: FAIL->FAIL; COND->max(post-domain,COND); PASS->post-domain.
  GClose must equal g_null(final).

§10 SCOPE COVERAGE [IMMUTABLE]: §5.5 maps §1 surfaces. GAP->ADVISORY-GAP. Also runs §10a.

§10a DOMAIN GAP-CHECK [IMMUTABLE]: Group by [DOMAIN:]. HIGH-applicability check per domain.
  ADVISORY-GAP where no HIGH row -> ACTION ITEM REGISTER.

§11 FINDING-SURFACE LINKAGE [IMMUTABLE]: [§1:S-n] per finding. Missing -> ADVISORY-ORPHAN.

§12 CONDITIONAL RESOLUTION REGISTRY [IMMUTABLE]: CONDITIONAL -> RESOLUTION REGISTRY table.

§13 g_null PROGRESSION LEDGER [IMMUTABLE]: In CROSS-ROLE SIGNALS.

§14 FINDING SEVERITY AGGREGATION [IMMUTABLE]: Section Severity=worst(all findings). None->LOW.

§15 LENS EXHAUSTION [IMMUTABLE]: LENS COVERAGE TABLE per section. Cite AM row ID+tier.
  HIGH+OPEN->ADVISORY-OPEN-LENS-REQUIRED. MEDIUM+OPEN->ADVISORY-OPEN-LENS.

§16 PRIMARY DRIVER [IMMUTABLE]: GClose=FAIL->BRACKET CLOSING; G_domain_agg=FAIL->DOMAIN;
  G_lifecycle=FAIL->LIFECYCLE; GOpen=FAIL->BRACKET OPENING; CONDITIONAL mirrors order.

§17 NULL HYPOTHESIS DIMENSION TABLE [IMMUTABLE]
  BRACKET OPENING: | Dim | A(0-10) | B(0-10) | C(0-10) | D1=(B-A) | D2=(B-C) | NH Verdict |
  MUST-CLEAR(*). Min 3 dims.
  Per-row: FAVORS-BUILD(D1>0,D2>0)/CONDITIONAL(D1>0,D2<=0)/OPPOSES-BUILD(D1<=0).
  g_null: HOLDS(MUST-CLEAR OPPOSES)/DEFEATED(FAVORS majority+both D1,D2 positive)/CONDITIONAL.

  NH TABLE AGGREGATION RULE [EXTENDED -- all reviewer archetypes; V-03 axis]:
    Column A: challenger opening, unchanged.
    Column B: avg(ALL domain B scores + LIFECYCLE B score) per dimension.
    Column C: avg(ALL domain C scores + LIFECYCLE C score) per dimension.
    Pre-committed. No editorial selection.

  BRACKET CLOSING re-applies §17 to revised table.

§17a CHARTER COVERAGE AUDIT [IMMUTABLE]:
  BRACKET CLOSING emits before GClose:
    | §0 Arg | Summary | Addressed By CH-IDs | Coverage |
  COVERED=at least one CH-ID cited arg AND response ADDRESSED/PARTIAL.
  CHARTER-GAP=no CH-ID cited arg or all citees OPEN.
  CHARTER-GAP->ADVISORY-CHARTER-GAP in ACTION ITEM REGISTER.

§18 GLOBAL F-ID REGISTRY [IMMUTABLE]:
  F-OPEN-{nn}, F-DOM-{nn}, F-LIFE-{nn} (multi-domain: F-DOM1-{nn}, F-DOM2-{nn}).
  Per-prefix sequential counters.
  All downstream refs use global F-IDs: ACTION ITEM REGISTER, §5.5, LENS COVERAGE TABLE,
  CH-ID response tables. Local F-1/F-2 aliases NOT used.
  GATE VECTOR TABLE records leading F-ID (highest severity) per gate.

END DISPOSITION_CONTRACT v1

---

## ROLE MANIFEST

| Slot | Archetype | Role | Rationale |
|------|-----------|------|-----------|
| CHALLENGER | inertia-advocate | [ROLE_NAME] | [One sentence.] |
| DOMAIN | technical/architecture | [ROLE_NAME] | [One sentence.] |
| LIFECYCLE | PM/program | [ROLE_NAME] | [One sentence.] |

### APPLICABILITY MATRIX (locked before BRACKET OPENING)

| Row ID | Role | lens.verify Entry | Artifact Domain | Artifact Applicability | Basis |
|--------|------|------------------|-----------------|----------------------|-------|
| AM-01 | [DOMAIN] | [Entry.] | [Domain.] | HIGH/MEDIUM/LOW | [Basis.] |
| AM-02 | [DOMAIN] | [Entry.] | [Domain.] | [Tier.] | [Basis.] |
| AM-03 | [DOMAIN] | [Entry.] | [Domain.] | [Tier.] | [Basis.] |
| AM-04 | [LIFECYCLE] | [Entry.] | [Domain.] | [Tier.] | [Basis.] |
| AM-05 | [LIFECYCLE] | [Entry.] | [Domain.] | [Tier.] | [Basis.] |

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**STATUS QUO VIABILITY ASSESSMENT**:

| SQ-DIM | Current State | Why Acceptable | Viability |
|--------|--------------|----------------|-----------|
| [Dim-1] | [Current.] | [Advantage.] | HIGH/MEDIUM/LOW |
| [Dim-2] | [Current.] | [Advantage.] | [Viability] |
| [Dim-3] | [Current.] | [Advantage.] | [Viability] |

**Overall SQ Viability**: VIABLE / MARGINAL / STRETCHED

**Null hypothesis**: [One sentence.]

**Alternatives comparison table** (0-10; 3+ dims):

| Dimension | A | B | C | Notes |
|-----------|---|---|---|-------|
| [Dim-1] | [Score] | [Score] | [Score] | |
| [Dim-2] | [Score] | [Score] | [Score] | |
| [Dim-3] | [Score] | [Score] | [Score] | |

**NULL HYPOTHESIS DIMENSION TABLE** (per §17; BRACKET CLOSING uses extended aggregation with LIFECYCLE):

| Dim | A | B | C | D1=(B-A) | D2=(B-C) | NH Verdict |
|-----|---|---|---|----------|----------|------------|
| [Dim-1*] | [Score] | [Score] | [Score] | [D1] | [D2] | [Verdict] |
| [Dim-2*] | [Score] | [Score] | [Score] | [D1] | [D2] | [Verdict] |
| [Dim-3] | [Score] | [Score] | [Score] | [D1] | [D2] | [Verdict] |

Applying §17: MUST-CLEAR OPPOSES=[list or "none"]; FAV=[N] COND=[N] OPP=[N];
  DEFEATED=[Y/N]; g_null(initial)=[HOLDS/CONDITIONAL/DEFEATED] (§9 Stage 1)

*(Findings use F-OPEN-{nn} per §18)*

**Challenge claims** (cite SQ-DIM and §0:Arg-n; CHARTER-ORPHAN if §0 absent):

| CH-ID | Claim | SQ-DIM | §0 Arg | Severity |
|-------|-------|--------|--------|---------|
| CH-001 | [Claim.] | [SQ-DIM-n] | §0:Arg-[n] | HIGH/MEDIUM/LOW |
| CH-002 | [Claim.] | [SQ-DIM-n] | §0:Arg-[n] | [Severity] |
| CH-003 | [Claim or omit.] | [SQ-DIM-n] | §0:Arg-[n] | [Severity] |

**GOpen Verdict**: PASS/CONDITIONAL/FAIL  **GOpen Reason**: [One sentence.]
**Leading F-ID**: F-OPEN-[nn] or N/A

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | [Verdict] | [Class] |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1  |  Received GOpen: [Copy.]
*(Findings: F-DOM-{nn} per §18)*

**CH-ID Response Table**:

| CH-ID | Claim | Assessment | Status |
|-------|-------|------------|--------|
| CH-001 | [Copy.] | [Technical.] | ADDRESSED/PARTIAL/OPEN |
| CH-002 | [Copy.] | [Assessment.] | [Status] |

**Domain re-score**:

| Dim | A | B | C | Rationale |
|-----|---|---|---|-----------|
| [Dim-1] | [Score] | [Score] | [Score] | [vs. challenger.] |
| [Dim-2] | [Score] | [Score] | [Score] | |

**NH Dimension Scores** (for §17 extended aggregation -- averaged with LIFECYCLE at bracket closing):

| Dim | Your B | Your C |
|-----|--------|--------|
| [Dim-1] | [Score] | [Score] |
| [Dim-2] | [Score] | [Score] |
| [Dim-3] | [Score] | [Score] |

**Findings** (global F-IDs; §1 cites; §14):

| # | F-ID | §1 Surface | Finding | Severity |
|---|------|-----------|---------|---------|
| 1 | F-DOM-01 | [§1:S-n] | [Finding.] | HIGH/MEDIUM/LOW |
| 2 | F-DOM-02 | [§1:S-n] | [Finding.] | [Severity] |

**Severity Aggregation**: worst([list]) = [SECTION_SEVERITY]

**Lens Coverage Table**:

| # | lens.verify Entry | Applicability | Status | Finding Ref |
|---|------------------|--------------|--------|------------|
| Q-1 | [Entry.] | AM-01: [tier] | ADDRESSED/OPEN | F-DOM-[nn] or AM cite |
| Q-2 | [Entry.] | AM-02: [tier] | [Status] | [Ref] |

**G_domain Verdict**: PASS/CONDITIONAL/FAIL  **Reason**: [One sentence.]  **Leading F-ID**: F-DOM-[nn]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | [Verdict] | [Class] |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT (EXCLUDED from ledger)

G_domain_agg=worst([list])=[result]; g_null(post-domain)=[§9 Stage 2]=[result]

---

## §3.8 CH-ID SATURATION CHECK (EXCLUDED from ledger)

| CH-ID | DOMAIN | Pre-LIFECYCLE Saturation |
|-------|--------|--------------------------|
| CH-001 | [Copy.] | SATURATED/UNSATURATED |
| CH-002 | [Copy.] | [Status] |

Unsaturated: [list or "None"]

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received: GOpen=[copy] | G_domain_agg=[copy] | g_null(post-domain)=[copy]
*(Findings: F-LIFE-{nn} per §18)*

**CH-ID Response Table**:

| CH-ID | Claim | Response | Status |
|-------|-------|----------|--------|
| CH-001 | [Copy.] | [Program.] | ADDRESSED/PARTIAL/OPEN |
| CH-002 | [Copy.] | [Response.] | [Status] |

**COMMITMENT-READINESS MATRIX**:

| CRM Dim | Current | Required | Gap | Severity |
|---------|---------|----------|-----|---------|
| Timeline | [Current.] | [Required.] | [Gap.] | HIGH/MEDIUM/LOW |
| Resources | [Current.] | [Required.] | [Gap.] | [Severity] |
| Rollback | [Current.] | [Required.] | [Gap.] | [Severity] |
| Stakeholder | [Current.] | [Required.] | [Gap.] | [Severity] |

**CRM Severity**: worst([list]) = [CRM_SEVERITY]

**NH Dimension Scores** (V-03 AXIS: LIFECYCLE participates in §17 extended aggregation)

Assess each §17 dimension from your program lens. BRACKET CLOSING averages your scores
with DOMAIN scores per the §17 EXTENDED NH TABLE AGGREGATION RULE.

| Dim | Your Build Score (B) | Your Best-Alt Score (C) | Program Rationale |
|-----|---------------------|------------------------|--------------------|
| [§17 Dim-1] | [0-10] | [0-10] | [One sentence program perspective.] |
| [§17 Dim-2] | [0-10] | [0-10] | [Rationale.] |
| [§17 Dim-3] | [0-10] | [0-10] | [Rationale.] |

**Decision-readiness assessment**: [One paragraph: GOpen, G_domain_agg, g_null(post-domain), CRM.]
**Null hypothesis status**: [One sentence with g_null(post-domain) value.]

**Findings**:

| # | F-ID | §1 Surface | Finding | Severity |
|---|------|-----------|---------|---------|
| 1 | F-LIFE-01 | [§1:S-n] | [Concern.] | HIGH/MEDIUM/LOW |
| 2 | F-LIFE-02 | [§1:S-n] | [Finding.] | [Severity] |

**Severity Aggregation**: worst([list]) = [SECTION_SEVERITY]

**Lens Coverage Table**:

| # | lens.verify Entry | Applicability | Status | Finding Ref |
|---|------------------|--------------|--------|------------|
| Q-1 | [Entry.] | AM-04: [tier] | ADDRESSED/OPEN | F-LIFE-[nn] or AM cite |
| Q-2 | [Entry.] | AM-05: [tier] | [Status] | [Ref] |

**G_lifecycle Verdict**: PASS/CONDITIONAL/FAIL  **Reason**: [One sentence.]  **Leading F-ID**: F-LIFE-[nn]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| LIFECYCLE -- [ROLE_NAME] | G_lifecycle | [Verdict] | [Class] |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**STATUS QUO VERDICT**:

| SQ-DIM | Opening | Changed By (global F-ID) | Revised |
|--------|---------|--------------------------|---------|
| [Dim-1] | [Opening.] | [F-ID or "none".] | VIABLE/MARGINAL/STRETCHED |
| [Dim-2] | [Opening.] | [F-ID.] | [Revised.] |

**SQ Viability Trajectory**: REINFORCED / UNCHANGED / WEAKENED

Applying §9 Stage 3: g_null(final)=[derivation]=[result]

**Revised NULL HYPOTHESIS DIMENSION TABLE** (§17 EXTENDED -- domain + lifecycle):

| Dim | A | B (avg DOM+LIFE) | C (avg DOM+LIFE) | D1 | D2 | NH Verdict |
|-----|---|-----------------|-----------------|----|----|------------|
| [Dim-1*] | [A] | [avg] | [avg] | [D1] | [D2] | [Verdict] |
| [Dim-2*] | [A] | [avg] | [avg] | [D1] | [D2] | [Verdict] |
| [Dim-3] | [A] | [avg] | [avg] | [D1] | [D2] | [Verdict] |

NH AGGREGATION (domain + lifecycle):
  Col A: opener values unchanged.
  Col B: Dim-1: avg(DOM=[_], LIFE=[_])=[result]; Dim-2: avg(...)=[result]
  Col C: Dim-1: avg(DOM=[_], LIFE=[_])=[result]; Dim-2: avg(...)=[result]

Applying §17: MUST-CLEAR OPPOSES=[list or "none"]; DEFEATED=[Y/N]; Result=[HOLDS/COND/DEFEATED]

**§17a CHARTER COVERAGE AUDIT** (per §17a):

| §0 Arg | Summary | Addressed By | Coverage |
|--------|---------|--------------|----------|
| §0:Arg-1 | [Summary.] | [CH-IDs.] | COVERED/CHARTER-GAP |
| §0:Arg-2 | [Summary.] | [CH-IDs.] | [Coverage] |
| §0:Arg-3 | [Summary or N/A.] | [CH-IDs.] | [Coverage] |

CHARTER-GAP items: [List or "None".]

NH chain note: LIFECYCLE-AMPLIFIED / LIFECYCLE-NEUTRAL / LIFECYCLE-ATTENUATED -- [one sentence
on whether LIFECYCLE NH scores shifted revised table materially.]

**Full CH-ID Saturation**:

| CH-ID | DOMAIN | LIFECYCLE | Full Saturation |
|-------|--------|-----------|-----------------|
| CH-001 | [Copy.] | [Copy.] | FULLY SATURATED/UNSATURATED |
| CH-002 | [Copy.] | [Copy.] | [Status] |

**GClose Verdict**: PASS if g_null=DEFEATED, fully saturated, zero CHARTER-GAP. Otherwise CONDITIONAL/FAIL.
**Override invoked**: YES / NO
**GClose Rationale**: [2-3 sentences: g_null(final), CH-ID saturation, SQ Trajectory,
Charter Coverage Audit, CRM Signal, LIFECYCLE NH contribution.]

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | [Verdict] | [Class] |

---

## §5.5 SCOPE COVERAGE RECONCILIATION (EXCLUDED from ledger)

Surface Coverage (global F-IDs):

| IN-SCOPE Surface | Reviewer(s) | Global F-IDs | Coverage |
|-----------------|-------------|--------------|----------|
| [Surface 1.] | [Reviewer.] | [F-DOM-01, F-LIFE-01, ...] | COVERED/GAP |

Coverage signal: COVERED / PARTIAL

Domain Coverage Gap-Check (§10a):
| Artifact Domain | HIGH-Applicability MATRIX Rows | Coverage |
|----------------|-------------------------------|----------|
| [Domain.] | [AM rows or "none".] | COVERED/ADVISORY-GAP |

§11 ADVISORY-ORPHAN check: [Orphans or "None".]

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Leading F-ID | Contract |
|------|----------|---------|-------------|---------|
| GOpen | [CHALLENGER] | [Verdict] | F-OPEN-[nn] or N/A | DISPOSITION_CONTRACT v1 |
| G_domain_agg | [DOMAIN] | [Verdict] | F-DOM-[nn] | DISPOSITION_CONTRACT v1 |
| G_lifecycle | [LIFECYCLE] | [Verdict] | F-LIFE-[nn] | DISPOSITION_CONTRACT v1 |
| GClose | [CHALLENGER] | [Verdict] | N/A | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Conflicts**: [Or "None".]
**Convergence**: [2+ reviewers; cite global F-IDs.]
**Scope coverage**: [Uncovered or "None".]

§13 PROGRESSION LEDGER:
  g_null(initial)=[copy] | g_null(post-domain)=[copy] | g_null(final)=[copy] | Trajectory=[label]

NH chain note: [LIFECYCLE-AMPLIFIED / LIFECYCLE-NEUTRAL / LIFECYCLE-ATTENUATED. One sentence
on whether LIFECYCLE B/C scores materially shifted g_null(final) vs. domain-only aggregation.]

---

## DISPOSITION

Gate vector: GOpen=[copy] | G_domain_agg=[copy] | G_lifecycle=[copy] | GClose=[copy]
Apply §3. **Overall Disposition**: READY / CONDITIONAL / BLOCKED
**§16 Primary Driver**: [rule n + reason + result]
**Conditions** (CONDITIONAL): [Conditions.] | **Blocker** (BLOCKED): [Global F-ID from FAIL gate.]
**RESOLUTION REGISTRY**: [Table or "N/A -- disposition is [value]".]

---

## ACTION ITEM REGISTER (verbatim gate ledger copy; global F-IDs throughout; no re-derivation)

| Source | Global F-ID / CH-ID | Item | Class | Owner | Criterion |
|--------|--------------------|----|-------|-------|-----------|
| Gate ledger | -- | [Verbatim: Section/Gate/Verdict/Class.] | [Class] | [Role] | [Criterion] |
| CH-ID | CH-00n | [Resolve.] | [Class] | [Role] | [Criterion] |
| Lens HIGH | AM-0n/Q-n | ADVISORY-OPEN-LENS-REQUIRED: [entry]. | ADVISORY | [Role] | Produce finding. |
| Lens MEDIUM | AM-0n/Q-n | ADVISORY-OPEN-LENS: [entry]. | ADVISORY | [Role] | Address or justify. |
| Scope gap | -- | ADVISORY-GAP: [surface]. | ADVISORY | [Role] | Assign reviewer. |
| Domain gap | -- | ADVISORY-GAP (DOMAIN): [domain]. | ADVISORY | [Role] | Add HIGH reviewer. |
| Orphan | F-{PRE}-[nn] | ADVISORY-ORPHAN: [F-ID] lacks §1:S-n. | ADVISORY | [Role] | Re-assign. |
| Charter gap | §0:Arg-n | ADVISORY-CHARTER-GAP: §0:Arg-n not covered. | ADVISORY | [CHALLENGER] | Issue claim or declare waiver. |

---

**Artifact to review:**

{{artifact}}
