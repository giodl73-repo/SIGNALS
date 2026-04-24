## V-04 — V-01 + V-02: Challenger-Dominant + Descriptive Register

**Variation axis**: Combination of V-01 (inertia framing -- STATUS QUO VIABILITY ASSESSMENT
anchors challenge claims) and V-02 (descriptive instruction register -- narrative guidance
replaces imperative bracketed placeholders). The DISPOSITION_CONTRACT §1-§17 is unchanged.

**Hypothesis**: V-01 produces better-anchored challenge claims by requiring SQ viability
articulation first. V-02 produces richer per-field outputs by describing intent rather than
commanding format. Combined, the hypothesis is that explicit inertia scaffolding plus
narrative instruction register produces the highest-quality adversarial bracket sections
while still satisfying all rubric criteria mechanically.

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
The challenger's job is to argue against building — to establish why the status quo is
acceptable and what it would take to overcome that prior. The domain reviewer evaluates the
artifact's technical surface from their expertise. The lifecycle reviewer assesses commitment
readiness from a program perspective. The review is governed by DISPOSITION_CONTRACT v1 below.

Fill in all required fields. Derive findings from the artifact — do not invent them. If a
field is not applicable, write the field name followed by "N/A -- " and the reason. Do not
alter, reorder, or omit any pre-printed heading, label, formula, or structural element.

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

Read `.roles/signal/`. Choose the inertia-advocate as challenger — the role that most
forcefully argues for not building, surfaces switching costs, and owns both bracket sections.
Choose a domain role whose lens.verify entries best match the artifact's technical surface.
Choose a lifecycle/program role focused on commitment readiness.

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (bracket open + close -- fixed) | inertia-advocate | [ROLE_NAME] | Write one sentence explaining why this role is the right inertia-advocate for this artifact. |
| DOMAIN | technical/architecture | [ROLE_NAME] | Write one sentence explaining the domain expertise this role brings. |
| LIFECYCLE | PM/program | [ROLE_NAME] | Write one sentence explaining this role's commitment-readiness perspective. |

*(For `--depth deep`: add DOMAIN-2, DOMAIN-3.)*

### APPLICABILITY MATRIX

Complete this matrix before BRACKET OPENING begins. It is locked at this point. For each
assigned role, list every lens.verify entry and rate its applicability to this artifact type.
HIGH means a finding is expected; MEDIUM means a finding is expected but may be brief; LOW
means the lens dimension does not apply (state why). The Artifact Domain column groups entries
for the §10a gap-check.

| Row ID | Role | lens.verify Entry | Artifact Domain Covered | Artifact Applicability | Basis for Rating |
|--------|------|------------------|------------------------|----------------------|------------------|
| AM-01 | [DOMAIN ROLE] | Write the full text of the first lens.verify entry for this role. | Name the artifact domain this entry addresses. | HIGH, MEDIUM, or LOW. | One sentence explaining the rating. |
| AM-02 | [DOMAIN ROLE] | Full text of the second entry. | Domain. | Tier. | Basis. |
| AM-03 | [DOMAIN ROLE] | Full text of the third entry if present. | Domain. | Tier. | Basis. |
| AM-04 | [LIFECYCLE ROLE] | Full text of the first lifecycle lens.verify entry. | Domain. | Tier. | Basis. |
| AM-05 | [LIFECYCLE ROLE] | Full text of the second entry. | Domain. | Tier. | Basis. |

*(Add a row for every lens.verify entry from every assigned role. Matrix is now locked.)*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

**V-01 AXIS: STATUS QUO VIABILITY ASSESSMENT** *(complete before challenge claims)*

Before issuing any challenge, establish why the current state is a viable default. For each
status quo dimension, describe what the team currently does and articulate the concrete
advantage that makes the current state acceptable. This is not a concession — it is the
evidence base for your claims. Each challenge claim below should reference at least one
dimension from this table.

| SQ-DIM | Current State Description | Why Current State Is Acceptable | Viability |
|--------|--------------------------|--------------------------------|-----------|
| Name the first status quo dimension. | Describe what the team actually does today on this dimension. | State the concrete advantage the current approach provides. | HIGH if the SQ is robust on this dimension. MEDIUM if adequate. LOW if strained. |
| Name a second dimension. | Current state. | Advantage. | Viability. |
| Name a third dimension. | Current state. | Advantage. | Viability. |

**Overall SQ Viability**: VIABLE if the team can continue without this artifact indefinitely.
MARGINAL if the status quo is bearable short-term. STRETCHED if it is showing strain.

---

**Null hypothesis**: State in one sentence what the team currently does instead of building
this artifact. Name the specific workaround or existing process — not just "nothing".

**Alternatives comparison table** *(score each option 0-10 per dimension; at least three dimensions; this table is distinct from the NH dimension table below)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|---------------|-----------|----------------------|-------|
| Name a dimension. | Score 0-10. | Score 0-10. | Score 0-10. | Optional note. |
| Second dimension. | Score. | Score. | Score. | |
| Third dimension. | Score. | Score. | Score. | |

**NULL HYPOTHESIS DIMENSION TABLE** *(per §17; three columns required; DEFEATED requires BOTH D1 AND D2 positive majority)*:

| Dimension | Status-Quo Score (A) | Proposed-Build Score (B) | Best-Non-Build-Alt Score (C) | D1=(B-A) | D2=(B-C) | NH Verdict |
|-----------|---------------------|--------------------------|------------------------------|----------|----------|------------|
| Name a must-clear dimension and mark *. | Score the status quo. | Score the proposed build. | Score the best non-build alt. | Compute B-A. | Compute B-C. | FAVORS-BUILD if D1>0 and D2>0. CONDITIONAL if D1>0 and D2<=0. OPPOSES-BUILD if D1<=0. |
| Second must-clear dimension. * | Score. | Score. | Score. | D1. | D2. | Verdict. |
| Third dimension (not must-clear). | Score. | Score. | Score. | D1. | D2. | Verdict. |

**Applying §17 g_null derivation rule**:
```
MUST-CLEAR rows with OPPOSES-BUILD: list them, or write "none".
count(FAVORS-BUILD)  = count rows where D1>0 AND D2>0
count(CONDITIONAL)   = count rows where D1>0 AND D2<=0
count(OPPOSES-BUILD) = count rows where D1<=0
DEFEATED: count(FAVORS-BUILD) > count(OPPOSES-BUILD) + count(CONDITIONAL) AND no MUST-CLEAR OPPOSES? [Y/N]
Result: HOLDS if any MUST-CLEAR=OPPOSES. CONDITIONAL if DEFEATED=NO. DEFEATED if DEFEATED=YES.
Note: DEFEATED requires both D1 and D2 positive majority.
```
**g_null(initial)** *(§9 Stage 1)*: Write HOLDS, CONDITIONAL, or DEFEATED.

**NULL HYPOTHESIS DERIVATION RULE** *(re-applied by BRACKET CLOSING to revised table)*:
  DEFEATED requires count(FAVORS-BUILD) majority with no MUST-CLEAR OPPOSES-BUILD.
  BOTH D1 and D2 must be positive majority.

**Challenge claims** *(each claim should reference a named SQ-DIM from the STATUS QUO VIABILITY
ASSESSMENT above; focus on switching costs, workaround viability, or adoption friction)*:

| CH-ID | Challenge Claim | SQ-DIM Referenced | Severity |
|-------|----------------|-------------------|---------|
| CH-001 | Write the first challenge claim in one sentence. Ground it in a specific SQ advantage from the viability table above. | Name the SQ-DIM this claim is grounded in. | HIGH, MEDIUM, or LOW per §2. |
| CH-002 | Second claim. | SQ-DIM. | Severity. |
| CH-003 | Optional third claim, or omit. | SQ-DIM or N/A. | Severity. |

**Verify Question**: Write one question from this role's lens.verify that you consider most critical for this artifact.
**Simplify**: Write one simplification suggestion from this role's lens.simplify.

**GOpen Verdict**: PASS if g_null=DEFEATED. CONDITIONAL if CONDITIONAL. FAIL if HOLDS.
**GOpen Reason**: One sentence explaining the verdict.
**g_null(initial)** *(§9 Stage 1)*: Copy from §17 derivation.

*GOpen, g_null(initial), and all CH-IDs carry forward to every downstream section.*

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | Write verdict. | Write class. |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: Copy GOpen from BRACKET OPENING.

Begin by responding to each challenge claim from your technical perspective. Then re-score the
alternatives table with your own assessments. Report your NH dimension scores for each §17
dimension — the challenger will average these at bracket closing per the NH TABLE AGGREGATION
RULE. Then produce findings from your lens.verify entries and expertise, citing §1 surfaces.

**CH-ID Response Table**:

| CH-ID | Challenge Claim (copy verbatim) | Your Technical Assessment | Status |
|-------|----------------------|-------------------------------|--------|
| CH-001 | Copy the claim from BRACKET OPENING. | Assess this claim from your technical perspective. Is the concern valid? Does the artifact design mitigate it? | ADDRESSED if resolved from your frame. PARTIAL if partially addressed — name the gap. OPEN if outside your technical scope. |
| CH-002 | Copy. | Assessment. | Status. |
| CH-003 | Copy if active. | Assessment. | Status. |

**Domain re-score**:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Rationale |
|-----------|---------------|-----------|----------------------|-----------|
| Copy dimension from BRACKET OPENING. | Your score. | Your score. | Your score. | One sentence on how your view differs from the challenger's, if at all. |
| Second dimension. | | | | |
| Third dimension. | | | | |

**NH Dimension Scores** *(BRACKET CLOSING will average these per NH TABLE AGGREGATION RULE)*:

| Dimension | Your Proposed-Build Score (B) | Your Best-Non-Build-Alt Score (C) |
|-----------|-------------------------------|-----------------------------------|
| Copy §17 dimension name. | Your score 0-10 for the proposed build on this dimension. | Your score 0-10 for the best non-build alternative. |
| Second §17 dimension. | Score. | Score. |
| Third §17 dimension. | Score. | Score. |

**Additional Findings** *(cite §1 surface for each; severity per §14)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | Write [§1:S-n]. | Describe the finding. Ground it in your lens.verify or expertise.depth. | HIGH, MEDIUM, or LOW. |
| F-2 | [§1:S-n]. | Second finding. | Severity. |
| F-3 | [§1:S-n] — optional. | Third finding. | Severity. |

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_], ...) = [SECTION_SEVERITY]
```
**Section Severity**: Mechanical result — do not assign editorially.

**Lens Coverage Table** *(cite AM row and tier; do not reassign)*:

| # | lens.verify Entry | Applicability (from ROLE MANIFEST) | Status | Finding Reference |
|---|------------------|-----------------------------------|--------|-------------------|
| Q-1 | Copy full text of lens.verify entry 1. | Write "AM-01: HIGH" (or MEDIUM/LOW). Do not change this value. | ADDRESSED or OPEN. | F-n if addressed. If LOW+OPEN: "AM-01: LOW -- [basis from matrix]". |
| Q-2 | Copy entry 2. | AM-02: tier. | Status. | F-n or AM cite. |
| Q-3 | Copy entry 3 if present. | AM-03: tier. | Status. | Reference. |

**Recommendation**: One specific, actionable change to the artifact.
**Simplify**: One suggestion from this role's lens.simplify.

**G_domain Verdict**: PASS, CONDITIONAL, or FAIL.
**G_domain Reason**: One sentence. Name the condition if CONDITIONAL; name the gap if FAIL.

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | Verdict. | Class. |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT

*(EXCLUDED from gate ledger per §6.)*

Apply §3a and §9 Stage 2 mechanically:
```
G_domain rows: DOMAIN -- [ROLE_NAME]: [verdict]
G_domain_agg = worst([list]) = [result]

g_null(initial) = [copy] | G_domain_agg = [copy]
  FAIL->FAIL | CONDITIONAL->max(initial,CONDITIONAL) | PASS->g_null(initial)
g_null(post-domain) = [result]
```
**G_domain Aggregate**: Result.
**g_null(post-domain)**: Result.

---

## §3.8 CH-ID SATURATION CHECK

*(EXCLUDED from gate ledger.)*

| CH-ID | DOMAIN Response Status | Pre-LIFECYCLE Saturation |
|-------|------------------------|--------------------------|
| CH-001 | Copy from DOMAIN. | SATURATED if ADDRESSED; UNSATURATED if PARTIAL or OPEN. |
| CH-002 | Copy. | Status. |
| CH-003 | Copy if active. | Status or N/A. |

**Pre-LIFECYCLE unsaturated CH-IDs**: List UNSATURATED IDs, or "None".

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: Copy from BRACKET OPENING.
Received G_domain Aggregate: Copy from §3.5.
Received g_null(post-domain): Copy from §3.5.

You are the program/PM reviewer. Assess whether this artifact is ready for commitment from a
decision, resource, and program perspective. Begin with CH-ID responses, then write a
decision-readiness paragraph that explicitly references GOpen, G_domain Aggregate, and
g_null(post-domain). Then produce findings from your lens.verify entries.

**CH-ID Response Table**:

| CH-ID | Challenge Claim (copy) | Your Commitment-Frame Response | Status |
|-------|----------------------|--------------------------------------|--------|
| CH-001 | Copy. | Assess this claim from a program and commitment perspective. | ADDRESSED / PARTIAL / OPEN. |
| CH-002 | Copy. | Response. | Status. |
| CH-003 | Copy if active. | Response. | Status. |

**Decision-readiness assessment**: Write one paragraph. Reference GOpen, G_domain Aggregate,
and g_null(post-domain) by name. Assess whether the decision to build is ready, noting what
program or commitment factors are clear and what remains uncertain.

**Null hypothesis status**: One sentence. State whether g_null(post-domain) has been defeated,
remains conditional, or holds.

**Additional Findings**:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n] | Commitment, program, or decision-readiness concern grounded in the artifact. | HIGH / MEDIUM / LOW. |
| F-2 | [§1:S-n] | Second finding. | Severity. |

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_]) = [SECTION_SEVERITY]
```
**Section Severity**: Mechanical result.

**Lens Coverage Table**:

| # | lens.verify Entry | Applicability (from ROLE MANIFEST) | Status | Finding Reference |
|---|------------------|-----------------------------------|--------|-------------------|
| Q-1 | Copy full text of entry 1. | AM-04: tier from ROLE MANIFEST. | ADDRESSED / OPEN. | F-n or AM cite. |
| Q-2 | Copy entry 2. | AM-05: tier. | Status. | Reference. |

**Recommendation**: One concrete program or commitment action.
**Simplify**: One suggestion from this role's lens.simplify.

**G_lifecycle Verdict**: PASS, CONDITIONAL, or FAIL.
**G_lifecycle Reason**: One sentence.

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| LIFECYCLE -- [ROLE_NAME] | G_lifecycle | Verdict. | Class. |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1
*Full record received: scope declaration, APPLICABILITY MATRIX, all CH-ID tables, all verdicts.*

**V-01 AXIS: STATUS QUO VERDICT** *(revisit the STATUS QUO VIABILITY ASSESSMENT from opening)*

Having seen domain and lifecycle testimony, re-evaluate each SQ dimension. For each, note
whether evidence received changed your view of the status quo's viability. Then assess the
overall trajectory — did testimony strengthen or weaken the inertia case?

| SQ-DIM | Opening Viability | Evidence That Changed This | Revised Viability |
|--------|------------------|---------------------------|-------------------|
| Copy SQ-DIM-1 from opening. | Copy the opening viability rating. | Name the domain or lifecycle finding that changed your view, or write "none". | VIABLE, MARGINAL, or STRETCHED after evidence. |
| SQ-DIM-2. | Opening rating. | Finding ref or "none". | Revised rating. |
| SQ-DIM-3. | Opening rating. | Finding ref or "none". | Revised rating. |

**SQ Viability Trajectory**: REINFORCED if evidence made the status quo case stronger.
UNCHANGED if no finding altered the viability assessment. WEAKENED if domain/lifecycle evidence
undermined one or more SQ advantages.

---

Apply §9 Stage 3 and re-populate the NH table per the NH TABLE AGGREGATION RULE.

**Applying §9 Stage 3 formula**:
```
g_null(post-domain) = [copy] | G_lifecycle = [copy]
  FAIL->FAIL | CONDITIONAL->max(post-domain,CONDITIONAL) | PASS->g_null(post-domain)
g_null(final) = [result]
```
**g_null(final)**: Result. *GClose must equal g_null(final) per §9.*

**Revised NULL HYPOTHESIS DIMENSION TABLE** *(per §17 + NH TABLE AGGREGATION RULE)*:

| Dimension | Status-Quo Score (A) | Proposed-Build Score (B) | Best-Non-Build-Alt Score (C) | D1=(B-A) | D2=(B-C) | NH Verdict |
|-----------|---------------------|--------------------------|------------------------------|----------|----------|------------|
| DIM-A*. | A: carry from opening (unchanged). | B: average of all domain reviewers' B scores for this dimension. | C: average of all domain reviewers' C scores. | Compute D1. | Compute D2. | Recompute verdict. |
| DIM-B*. | A unchanged. | avg domain B. | avg domain C. | D1. | D2. | Verdict. |
| DIM-C. | A unchanged. | avg domain B. | avg domain C. | D1. | D2. | Verdict. |

**NH AGGREGATION RULE APPLIED**:
```
Column A: challenger opening values carried forward (control arm -- unchanged per §17)
Column B averages: [DIM-A]=avg([domain B scores]) | [DIM-B]=avg([scores]) | [DIM-C]=avg([scores])
Column C averages: [DIM-A]=avg([domain C scores]) | [DIM-B]=avg([scores]) | [DIM-C]=avg([scores])
```

**Applying §17 g_null derivation rule to revised table**:
```
MUST-CLEAR rows with OPPOSES-BUILD: [list or "none"]
count(FAVORS-BUILD)=[N]  count(CONDITIONAL)=[N]  count(OPPOSES-BUILD)=[N]
DEFEATED condition met? [Y/N]
Result: [HOLDS / CONDITIONAL / DEFEATED]
```

**Revised alternatives table**:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Domain Agg Rationale |
|-----------|---------------|-----------|----------------------|---------------------|
| DIM-1. | Agg score. | Agg score. | Agg score. | One sentence. |
| DIM-2. | | | | |

**Full CH-ID Saturation Check** *(per §8)*:

| CH-ID | DOMAIN Status | LIFECYCLE Status | Full Saturation | Waiver (if needed) |
|-------|--------------|-----------------|-----------------|---------------------|
| CH-001 | Copy. | Copy. | FULLY SATURATED or UNSATURATED. | WAIVER or N/A. |
| CH-002 | Copy. | Copy. | Status. | N/A. |
| CH-003 | Copy if active. | Copy. | Status. | N/A. |

**CH-ID Final Assessment**:

| CH-ID | G_domain Status | G_lifecycle Status | Final Status | Notes |
|-------|----------------|-------------------|--------------|-------|
| CH-001 | Copy. | Copy. | DEFEATED / PARTIAL / HOLDS. | Note. |
| CH-002 | Copy. | Copy. | Status. | |
| CH-003 | Copy if active. | Copy. | Status. | |

**Remaining gaps**: All defeated, or list unresolved items.
**GClose Verdict**: PASS if g_null=DEFEATED and CH-IDs satisfied. CONDITIONAL or FAIL otherwise.
**Override invoked**: YES or NO.
**g_null Override**: N/A -- formula applied, or write justification.
**GClose Rationale**: Two to three sentences. Reference g_null(final), CH-ID saturation, SQ Viability Trajectory, and overall trajectory.

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | Verdict. | Class. |

---

## §5.5 SCOPE COVERAGE RECONCILIATION

*(EXCLUDED from gate ledger per §6.)*

### Surface Coverage *(per §10)*

| IN-SCOPE Surface | Reviewer(s) | Finding Reference(s) | Coverage |
|-----------------|-------------|---------------------|----------|
| Copy §1 surface 1. | Reviewer or "none". | Finding refs. | COVERED or GAP. |
| Surface 2. | Reviewer. | Refs. | Coverage. |
| Surface 3. | Reviewer. | Refs. | Coverage. |

**Surface coverage gate signal**: COVERED or PARTIAL -- [N] surface(s) not addressed.

### Domain Coverage Gap-Check *(per §10a)*

| Artifact Domain | HIGH-Applicability MATRIX Rows | Coverage |
|----------------|-------------------------------|----------|
| Domain from §1 annotations. | AM rows with HIGH for this domain, or "none". | COVERED or ADVISORY-GAP. |
| Second domain. | AM rows or "none". | Coverage. |

**§11 ADVISORY-ORPHAN check**: List findings lacking §1:S-n citations, or "None detected."

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract Cite |
|------|----------|---------|---------------|
| GOpen -- bracket opening | [CHALLENGER_ROLE] | Copy verdict. | DISPOSITION_CONTRACT v1 |
| G_domain_agg -- domain aggregate | [DOMAIN_ROLE(S)] | Copy verdict. | DISPOSITION_CONTRACT v1 |
| G_lifecycle -- lifecycle | [LIFECYCLE_ROLE] | Copy verdict. | DISPOSITION_CONTRACT v1 |
| GClose -- bracket closing | [CHALLENGER_ROLE] | Copy verdict. | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Conflicts**: Identify incompatible assessments across roles, or "None detected."

**Convergence**: Identify any concern raised independently by two or more reviewers. Name it
and explain why convergence makes it the highest-confidence signal.

**Scope coverage**: List any §1 surfaces no reviewer addressed, or "None."

**§13 PROGRESSION LEDGER**:
```
g_null(initial)     = copy from BRACKET OPENING
g_null(post-domain) = copy from §3.5
g_null(final)       = copy from BRACKET CLOSING
Trajectory:         MONOTONIC-PASS / MONOTONIC-FAIL / DOMAIN-DEGRADED / LIFECYCLE-DEGRADED /
                    DOMAIN-RECOVERED / LIFECYCLE-RECOVERED
```

---

## DISPOSITION

**Gate vector**: GOpen=[copy] | G_domain_agg=[copy] | G_lifecycle=[copy] | GClose=[copy]

Apply §3 mechanically:
```
GClose=FAIL? -> BLOCKED | any Gi=FAIL? -> BLOCKED | any CONDITIONAL? -> CONDITIONAL | all PASS? -> READY
```

**Overall Disposition**: READY, CONDITIONAL, or BLOCKED.

**Applying §16 rule**: State the rule number and reason.
**Primary Driver**: Result.

**Conditions** *(only if CONDITIONAL)*: List per-gate conditions.
**Blocker** *(only if BLOCKED)*: Specific finding from FAIL gate.

**RESOLUTION REGISTRY** *(only if CONDITIONAL)*:
| Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status |
|------|------------------|-----------------|---------------------|--------|
| Gate. | One sentence. | Role. | Falsifiable test. | OPEN |

*If not CONDITIONAL: "RESOLUTION REGISTRY: N/A -- disposition is [value]"*

---

## ACTION ITEM REGISTER

| Source | CH-ID / Finding | Item Description | Disposition Class | Owner Role | Resolution Criterion |
|--------|----------------|-----------------|------------------|------------|---------------------|
| Gate ledger copy. | -- | Verbatim: Section / Gate / Verdict / Class. | Class. | Role. | Criterion. |
| CH-ID item. | CH-00n | What must be resolved for PARTIAL or HOLDS. | Class. | Role. | Criterion. |
| Lens HIGH. | AM-0n / Q-n | ADVISORY-OPEN-LENS-REQUIRED: [entry] not addressed. | ADVISORY. | Role. | Produce finding. |
| Lens MED. | AM-0n / Q-n | ADVISORY-OPEN-LENS: [entry] not addressed. | ADVISORY. | Role. | Address or justify. |
| Scope gap. | -- | ADVISORY-GAP: §1 surface [name] not covered. | ADVISORY. | Role. | Assign reviewer. |
| Domain gap. | -- | ADVISORY-GAP (DOMAIN): [domain] no HIGH-applicability reviewer. | ADVISORY. | Role. | Add reviewer or justify. |
| Orphan. | -- | ADVISORY-ORPHAN: [F-n] from [SECTION] lacks §1:S-n. | ADVISORY. | Role. | Re-assign or remove. |

---

**Artifact to review:**

{{artifact}}
