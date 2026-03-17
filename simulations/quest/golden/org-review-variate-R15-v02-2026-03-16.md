## V-02 — Descriptive Register: Narrative Instructions

**Variation axis**: Phrasing register — all reviewer section instructions are written in
descriptive/narrative form. Bracketed placeholders like "[What the team does today -- one
sentence]" become prose guidance like "State in one sentence what the team currently does
instead of building this artifact." The DISPOSITION_CONTRACT §1-§17 is unchanged (immutable).
Table field guidance describes intent and gives examples rather than listing option values.

**Hypothesis**: AI models produce more artifact-specific, less generic outputs when section
instructions describe what the field is for and why it matters, rather than commanding a fill.
The hypothesis is that "State the null hypothesis — the specific workaround or process the
team uses today" produces richer outputs than "[What the team does today]" because it
explains the purpose of the field and models the desired specificity. Criteria satisfaction
is unchanged; the structure is identical to V-01 baseline; only the instruction register differs.

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

You will produce a structured review by playing four roles in sequence. The inertia-advocate
challenger opens the review by establishing the null hypothesis — arguing from the position
that the artifact should not be built unless evidence is strong enough to overcome inertia.
The domain-expert reviewer evaluates the artifact's technical surface independently. The
lifecycle/program reviewer assesses commitment readiness. The challenger closes by integrating
all testimony and reaching a final verdict on whether the null hypothesis has been defeated.

Each reviewer derives findings from the artifact. Do not invent findings. When a field is not
applicable, write the field name followed by "N/A -- " and the specific reason. Do not alter,
reorder, or omit any pre-printed heading, label, formula, or structural element below.

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

Read `.craft/roles/signal/`. For each slot, choose the role that best fits the archetype.
The challenger slot is fixed — it must be an inertia-advocate whose lens emphasizes switching
costs, workaround viability, and the value of not changing. The domain slot should be the
role whose lens.verify entries most directly apply to the artifact's technical surfaces. The
lifecycle slot should be a PM or program role whose lens focuses on commitment readiness,
milestones, and decision quality.

| Slot | Archetype | Role | Selection Rationale |
|------|-----------|------|---------------------|
| CHALLENGER (bracket open + close -- fixed) | inertia-advocate | Write the role name selected from .craft/roles/signal/. | Write one sentence explaining why this role is the right inertia-advocate for this artifact type. |
| DOMAIN | technical/architecture | Write the domain role name. | Write one sentence explaining the technical expertise this role brings to this artifact. |
| LIFECYCLE | PM/program | Write the lifecycle role name. | Write one sentence explaining this role's commitment-readiness perspective. |

*(For `--depth deep`: add DOMAIN-2, DOMAIN-3 with separate rationale rows.)*

### APPLICABILITY MATRIX

Complete this matrix before BRACKET OPENING begins. It is locked once you proceed past this
point — no downstream section may change any applicability tier or basis. For each assigned
role, enumerate every entry from that role's lens.verify. Assign HIGH if the lens dimension
directly applies to this artifact type and a finding is expected (OPEN -> register entry
required). Assign MEDIUM if tangentially relevant and a finding is expected (OPEN -> advisory
register entry). Assign LOW if not applicable (state the basis; OPEN is acceptable at LOW).
The Artifact Domain column identifies which domain this lens entry covers, used by §10a.

| Row ID | Role | lens.verify Entry | Artifact Domain Covered | Artifact Applicability | Basis for Rating |
|--------|------|------------------|------------------------|----------------------|------------------|
| AM-01 | Write the domain role name. | Write the complete text of the first lens.verify entry for this role — do not paraphrase. | Name the artifact domain this entry addresses (e.g., "API Contract", "Data Model", "Security"). | HIGH, MEDIUM, or LOW. | One sentence grounding the rating in the artifact's actual content. |
| AM-02 | Domain role. | Full text of the second lens.verify entry. | Domain name. | Tier. | Basis sentence. |
| AM-03 | Domain role. | Full text of the third entry if present; otherwise write "N/A -- role has only two lens.verify entries". | Domain. | Tier. | Basis. |
| AM-04 | Write the lifecycle role name. | Full text of the first lens.verify entry for the lifecycle role. | Domain. | Tier. | Basis. |
| AM-05 | Lifecycle role. | Full text of the second lens.verify entry. | Domain. | Tier. | Basis. |

*(Add a row for every lens.verify entry from every assigned role. The matrix is now locked.)*

---

## BRACKET OPENING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1

State the null hypothesis first — in one sentence, describe what the team currently does
instead of building this artifact. Be concrete and specific: name the actual workaround,
tool, or process in use, not just the absence of the feature. For example: "Teams export
metrics to CSV and analyze in spreadsheets when cross-service dashboards are needed."

**Null hypothesis**: State in one sentence the concrete workaround or process the team uses today instead of this artifact.

Then evaluate the artifact across at least three dimensions by scoring the status quo, the
proposed build, and the best non-build alternative on each. Present these scores in the
alternatives comparison table below, then separately in the NH dimension table.

**Alternatives comparison table** *(score each option 0-10 per dimension; present at least three dimensions; this table is distinct from the §17 NH dimension table)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Notes |
|-----------|---------------|-----------|----------------------|-------|
| Name the first dimension — something that matters to a decision-maker evaluating this artifact. | Score 0-10 representing how well the status quo performs on this dimension. | Score 0-10 for the proposed build. | Score 0-10 for the best non-build alternative. | Any qualifying note. |
| Name the second dimension. | Score. | Score. | Score. | |
| Name the third dimension. | Score. | Score. | Score. | |

**NULL HYPOTHESIS DIMENSION TABLE** *(per §17; three columns required when three or more
alternatives are evaluated; DEFEATED requires BOTH D1 AND D2 positive majority — the build
must outperform both the status quo AND the best alternative on most dimensions)*:

| Dimension | Status-Quo Score (A) | Proposed-Build Score (B) | Best-Non-Build-Alt Score (C) | D1=(B-A) | D2=(B-C) | NH Verdict |
|-----------|---------------------|--------------------------|------------------------------|----------|----------|------------|
| Name a must-clear dimension — one where improvement is required — and mark it with *. | Score the status quo 0-10. | Score the proposed build 0-10. | Score the best non-build alternative 0-10. | Compute B minus A. | Compute B minus C. | FAVORS-BUILD if both D1 and D2 are positive. CONDITIONAL if D1 is positive but D2 is not. OPPOSES-BUILD if D1 is zero or negative. |
| Name a second must-clear dimension. * | Score. | Score. | Score. | D1. | D2. | Verdict. |
| Name a third dimension (not must-clear). | Score. | Score. | Score. | D1. | D2. | Verdict. |
| Add more dimensions as needed. | | | | | | |

**Applying §17 g_null derivation rule**:
```
List any must-clear rows where NH Verdict = OPPOSES-BUILD, or write "none":
count of FAVORS-BUILD rows (D1>0 AND D2>0):
count of CONDITIONAL rows (D1>0 AND D2<=0):
count of OPPOSES-BUILD rows (D1<=0):
DEFEATED condition: count(FAVORS-BUILD) > count(OPPOSES-BUILD) + count(CONDITIONAL)
  AND no must-clear row = OPPOSES-BUILD: write YES or NO
Result: HOLDS if any must-clear = OPPOSES-BUILD.
        CONDITIONAL if DEFEATED condition = NO and no must-clear OPPOSES-BUILD.
        DEFEATED if DEFEATED condition = YES and no must-clear OPPOSES-BUILD.
```
**g_null(initial)** *(§9 Stage 1 -- output of §17 formula above)*: Write HOLDS, CONDITIONAL, or DEFEATED.

**NULL HYPOTHESIS DERIVATION RULE** *(this rule is re-applied by BRACKET CLOSING to the revised table)*:
  DEFEATED requires a majority of rows to have FAVORS-BUILD verdict, no must-clear row with
  OPPOSES-BUILD, and importantly, BOTH D1 AND D2 positive in the majority — the build must
  beat both the status quo AND the best non-build alternative. A positive D1 alone (beating
  only the status quo) is insufficient for DEFEATED.

**Challenge claims** *(assign sequential CH-IDs; each claim should be a specific, falsifiable
concern about whether building is the right decision — focus on switching costs, the viability
of current workarounds, or adoption friction)*:

| CH-ID | Challenge Claim | Severity |
|-------|----------------|---------|
| CH-001 | Write the first challenge claim in one sentence. Focus on a specific switching cost (what the team loses by moving away from the status quo), a workaround viability concern (whether the existing approach is actually adequate), or adoption friction (resistance or integration risk). | Rate HIGH if this claim would block commitment, MEDIUM if it conditions commitment but doesn't block it, LOW if it is advisory. |
| CH-002 | Write the second challenge claim, similarly specific. | Severity. |
| CH-003 | Write an optional third claim, or omit this row entirely. | Severity if present. |

**Verify Question**: Write the one question from this role's lens.verify that you consider most critical for evaluating this artifact.
**Simplify**: Write one suggestion from this role's lens.simplify for how the artifact could be made simpler.

**GOpen Verdict**: Write PASS if g_null = DEFEATED, CONDITIONAL if CONDITIONAL, FAIL if HOLDS.
**GOpen Reason**: Write one sentence explaining this verdict, naming the g_null result that drove it.
**g_null(initial)** *(§9 Stage 1)*: Copy the value from the §17 derivation above.

*GOpen, g_null(initial), and all CH-IDs carry forward to every downstream section.*

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET OPENING | GOpen | Write PASS, CONDITIONAL, or FAIL. | Write ADVISORY if PASS, CONDITIONAL if CONDITIONAL, BLOCKED if FAIL. |

---

## DOMAIN -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: Copy the GOpen verdict from BRACKET OPENING.

Begin by responding to each challenge claim from your technical perspective. Assess whether
the concern is valid given the artifact's actual design — reference specific sections or
elements of the artifact in your response. Then re-score the alternatives table with your own
analysis of the same dimensions. Report your NH dimension scores separately (the challenger
will average these at bracket closing per the NH TABLE AGGREGATION RULE in §17). Then produce
findings from your lens.verify entries and expertise, citing §1 surfaces for each.

**CH-ID Response Table** *(respond to every active CH-ID; copy claim text verbatim)*:

| CH-ID | Challenge Claim (copy verbatim from BRACKET OPENING) | Your Technical Assessment | Status |
|-------|----------------------|-------------------------------|--------|
| CH-001 | Copy the exact claim text. | Assess this claim from your technical perspective. Does the artifact's design address or mitigate this concern? Name the specific design element or artifact section that addresses it, or explain why the concern remains valid. | Write ADDRESSED if fully resolved from your technical frame. PARTIAL if partially addressed — describe in one sentence what remains unresolved. OPEN if this claim is outside your technical scope. |
| CH-002 | Copy claim. | Technical assessment. | Status. |
| CH-003 | Copy if this CH-ID is active. | Assessment. | Status. |

**Domain re-score** *(re-score the same dimensions from BRACKET OPENING alternatives table with your own analysis)*:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Rationale |
|-----------|---------------|-----------|----------------------|-----------|
| Copy the dimension name from BRACKET OPENING. | Your score for the status quo. | Your score for the proposed build. | Your score for the best non-build alternative. | One sentence explaining how your assessment differs from the challenger's opener, or confirming agreement. |
| Second dimension. | Score. | Score. | Score. | Rationale. |
| Third dimension. | Score. | Score. | Score. | Rationale. |

**NH Dimension Scores** *(these scores will be averaged by the challenger at bracket closing
per the NH TABLE AGGREGATION RULE pre-committed in §17 — one row per §17 NH dimension)*:

| Dimension | Your Proposed-Build Score (B) | Your Best-Non-Build-Alt Score (C) |
|-----------|-------------------------------|-----------------------------------|
| Copy the §17 NH dimension name. | Your score 0-10 for the proposed build on this dimension. | Your score 0-10 for the best non-build alternative on this dimension. |
| Second §17 NH dimension. | Score. | Score. |
| Third §17 NH dimension. | Score. | Score. |

*(For --depth deep: each domain reviewer produces their own NH Dimension Scores table.)*

**Additional Findings** *(derive from lens.verify entries and expertise.depth; each finding
must cite the §1 surface it addresses; severity per §2 definitions)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | Write [§1:S-n] citing the relevant §1 surface by number (e.g., [§1:S-1]). | Describe the finding in one to two sentences, grounded in a specific lens.verify entry or area of expertise.depth. | HIGH if it blocks commitment, MEDIUM if it conditions commitment, LOW if advisory. |
| F-2 | [§1:S-n]. | Second finding. | Severity. |
| F-3 | [§1:S-n] — include a third finding if present; otherwise omit this row. | Third finding. | Severity. |

*(Findings without a valid §1:S-n citation are ADVISORY-ORPHAN per §11 and must be listed in the ACTION ITEM REGISTER.)*

**Finding Severity Aggregation (per §14)** — compute mechanically, not editorially:
```
worst(F-1=[severity], F-2=[severity], ...) = [SECTION_SEVERITY]
```
**Section Severity**: Write the mechanical result — the worst severity across all findings.

**Lens Coverage Table** *(cite the APPLICABILITY MATRIX row ID and tier exactly as assigned
in the ROLE MANIFEST; do not reassign applicability tiers here)*:

| # | lens.verify Entry | Applicability (from ROLE MANIFEST) | Status | Finding Reference |
|---|------------------|-----------------------------------|--------|-------------------|
| Q-1 | Write the complete text of lens.verify entry 1 for this role. | Write "AM-01: HIGH" or "AM-01: MEDIUM" or "AM-01: LOW" — copy the tier directly from the ROLE MANIFEST APPLICABILITY MATRIX, do not reassign. | Write ADDRESSED if a finding in this section addresses this entry; OPEN if not. | If ADDRESSED: cite the finding number (e.g., F-1). If LOW and OPEN: write "AM-01: LOW -- [copy basis from matrix]". If HIGH or MEDIUM and OPEN: this generates an ACTION ITEM REGISTER entry. |
| Q-2 | Complete text of entry 2. | AM-02: tier from matrix. | ADDRESSED or OPEN. | F-n or AM cite. |
| Q-3 | Complete text of entry 3 if present. | AM-03: tier. | Status. | Reference. |

*(Add a row for every lens.verify entry from this role.)*

**Recommendation**: Write one specific, actionable change to the artifact.
**Simplify**: Write one suggestion from this role's lens.simplify.

**G_domain Verdict**: Write PASS, CONDITIONAL, or FAIL.
**G_domain Reason**: Write one sentence. If CONDITIONAL, name the condition. If FAIL, name the gap.

*(For `--depth deep`: repeat this entire DOMAIN section as DOMAIN-2, DOMAIN-3, each with their
own NH Dimension Scores, local ledger row, domain re-score, and lens coverage table.)*

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| DOMAIN -- [ROLE_NAME] | G_domain | Write PASS, CONDITIONAL, or FAIL. | Write ADVISORY, CONDITIONAL, or BLOCKED accordingly. |

---

## §3.5 DOMAIN-AGGREGATE CHECKPOINT

*(EXCLUDED from gate ledger per §6 -- no ledger row emitted here.)*

Apply the §3a formula mechanically to compute G_domain_agg, then apply §9 Stage 2 to advance
the null hypothesis trajectory:
```
G_domain rows collected:
  DOMAIN -- [ROLE_NAME]: copy verdict
  (add rows for each domain reviewer if --depth deep)
G_domain_agg = worst(all listed verdicts) = write result

g_null(initial) = copy from BRACKET OPENING | G_domain_agg = copy
  If G_domain_agg = FAIL: g_null(post-domain) = FAIL
  If G_domain_agg = CONDITIONAL: g_null(post-domain) = max(g_null(initial), CONDITIONAL)
  If G_domain_agg = PASS: g_null(post-domain) = g_null(initial)
g_null(post-domain) = write result
```
**G_domain Aggregate**: Write the result.
**g_null(post-domain)**: Write the result.

*Both values carry forward to §3.8, LIFECYCLE, and BRACKET CLOSING.*

---

## §3.8 CH-ID SATURATION CHECK

*(EXCLUDED from gate ledger -- no ledger row emitted here.)*

| CH-ID | DOMAIN Response Status | Pre-LIFECYCLE Saturation |
|-------|------------------------|--------------------------|
| CH-001 | Copy the status from DOMAIN's CH-ID table. | SATURATED if status is ADDRESSED. UNSATURATED if PARTIAL or OPEN. |
| CH-002 | Copy. | Saturation status. |
| CH-003 | Copy if active, otherwise N/A. | Status or N/A. |

**Pre-LIFECYCLE unsaturated CH-IDs**: List any UNSATURATED IDs, or write "None".
*LIFECYCLE may proceed. Full saturation verification executes at BRACKET CLOSING.*

---

## LIFECYCLE -- [ROLE_NAME]

Contract: DISPOSITION_CONTRACT v1
Received GOpen: Copy GOpen from BRACKET OPENING.
Received G_domain Aggregate: Copy G_domain_agg from §3.5.
Received g_null(post-domain): Copy g_null(post-domain) from §3.5.

You are the program/PM reviewer. Your responsibility is to assess whether this artifact is
ready for commitment from a decision, resource, and program perspective — not to re-evaluate
whether the technical design is correct. Begin by responding to each challenge claim from your
program frame. Then write a decision-readiness paragraph that explicitly names GOpen,
G_domain Aggregate, and g_null(post-domain) as evidence inputs. Produce findings from your
lens.verify entries, each grounded in the artifact's actual content.

**CH-ID Response Table** *(respond from your commitment and program perspective)*:

| CH-ID | Challenge Claim (copy verbatim) | Your Commitment-Frame Response | Status |
|-------|----------------------|--------------------------------------|--------|
| CH-001 | Copy claim. | From a program and commitment perspective, assess whether this concern is valid. Does your program knowledge support or challenge this claim? Reference the artifact's specifics. | ADDRESSED if fully resolved from your frame. PARTIAL if partially addressed — state the gap. OPEN if outside your program scope. |
| CH-002 | Copy. | Response. | Status. |
| CH-003 | Copy if active. | Response. | Status. |

**Decision-readiness assessment**: Write one paragraph. Reference GOpen, G_domain Aggregate,
and g_null(post-domain) by name, explaining what each tells you about commitment readiness.
Assess what program, resource, or commitment factors are clear and what remains uncertain
before a commitment decision can safely be made.

**Null hypothesis status**: Write one sentence stating whether g_null(post-domain) has been
defeated, remains conditional, or holds, and what that means for the current decision state.

**Additional Findings** *(commitment, program, and decision-readiness concerns; each cites §1 surface)*:

| # | §1 Surface | Finding | Severity |
|---|-----------|---------|---------|
| F-1 | [§1:S-n]. | Describe a commitment, program, or decision concern grounded in the artifact. | HIGH / MEDIUM / LOW. |
| F-2 | [§1:S-n]. | Second finding. | Severity. |

**Finding Severity Aggregation (per §14)**:
```
worst(F-1=[_], F-2=[_]) = [SECTION_SEVERITY]
```
**Section Severity**: Mechanical result.

**Lens Coverage Table** *(cite AM row and tier from ROLE MANIFEST)*:

| # | lens.verify Entry | Applicability (from ROLE MANIFEST) | Status | Finding Reference |
|---|------------------|-----------------------------------|--------|-------------------|
| Q-1 | Complete text of lifecycle lens.verify entry 1. | AM-04: copy tier from ROLE MANIFEST. | ADDRESSED or OPEN. | F-n if addressed; AM cite if LOW+OPEN. |
| Q-2 | Complete text of entry 2. | AM-05: tier. | Status. | Reference. |

**Recommendation**: Write one concrete, actionable program or commitment recommendation.
**Simplify**: Write one suggestion from this role's lens.simplify.

**G_lifecycle Verdict**: Write PASS, CONDITIONAL, or FAIL.
**G_lifecycle Reason**: Write one sentence explaining the verdict.

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| LIFECYCLE -- [ROLE_NAME] | G_lifecycle | Write verdict. | Write class. |

---

## BRACKET CLOSING -- CHALLENGER

Contract: DISPOSITION_CONTRACT v1
*Full record received: scope declaration, APPLICABILITY MATRIX, all CH-ID tables, all verdicts.*

You have now received domain and lifecycle testimony. Apply §9 Stage 3 to advance g_null to its
final value, then re-populate the NH dimension table mechanically using the NH TABLE AGGREGATION
RULE pre-committed in §17 — Column A carries forward unchanged, Column B is the average of all
domain reviewer B scores per dimension, Column C is the average of all domain reviewer C scores.
Then assess CH-ID saturation and reach a final verdict.

**Applying §9 Stage 3 formula**:
```
g_null(post-domain) = copy from §3.5 | G_lifecycle = copy from LIFECYCLE ledger
  If G_lifecycle=FAIL: g_null(final) = FAIL
  If G_lifecycle=CONDITIONAL: g_null(final) = max(g_null(post-domain), CONDITIONAL)
  If G_lifecycle=PASS: g_null(final) = g_null(post-domain)
g_null(final) = write result
```
**g_null(final)**: Write result. *GClose must equal g_null(final) per §9.*

**Revised NULL HYPOTHESIS DIMENSION TABLE** *(per §17 + NH TABLE AGGREGATION RULE -- values
are derived mechanically; no editorial column selection permitted)*:

| Dimension | Status-Quo Score (A) | Proposed-Build Score (B) | Best-Non-Build-Alt Score (C) | D1=(B-A) | D2=(B-C) | NH Verdict |
|-----------|---------------------|--------------------------|------------------------------|----------|----------|------------|
| Copy DIM-A from opening. | Copy the challenger's opening A value — this is the control arm and is carried forward unchanged. | Compute the average of all domain reviewers' B scores for this dimension. | Compute the average of all domain reviewers' C scores for this dimension. | Compute revised D1. | Compute revised D2. | Recompute NH Verdict using §17 rule. |
| DIM-B. | A unchanged. | avg domain B. | avg domain C. | D1. | D2. | Verdict. |
| DIM-C. | A unchanged. | avg domain B. | avg domain C. | D1. | D2. | Verdict. |

**NH AGGREGATION RULE APPLIED**:
```
Column A: challenger opening values carried forward unchanged (status quo is the control arm)
Column B: average of domain reviewer B scores per dimension:
  [DIM-A]: avg([list each reviewer's B score]) = [result]
  [DIM-B]: avg([scores]) = [result]
  [DIM-C]: avg([scores]) = [result]
Column C: average of domain reviewer C scores per dimension:
  [DIM-A]: avg([list each reviewer's C score]) = [result]
  [DIM-B]: avg([scores]) = [result]
  [DIM-C]: avg([scores]) = [result]
```

**Applying §17 g_null derivation rule to revised table**:
```
Must-clear rows with OPPOSES-BUILD: list them or write "none".
count(FAVORS-BUILD): count rows where revised D1>0 AND revised D2>0
count(CONDITIONAL): count rows where revised D1>0 AND revised D2<=0
count(OPPOSES-BUILD): count rows where revised D1<=0
DEFEATED condition met (count(FAVORS-BUILD) > count(OPPOSES-BUILD)+count(CONDITIONAL) AND no must-clear OPPOSES)? write YES or NO
Result: HOLDS, CONDITIONAL, or DEFEATED
```

**Revised alternatives table**:

| Dimension | Status Quo (A) | Build (B) | Best Non-Build Alt (C) | Domain Agg Rationale |
|-----------|---------------|-----------|----------------------|---------------------|
| DIM-1. | Aggregated score. | Aggregated score. | Aggregated score. | One sentence on what domain testimony changed. |
| DIM-2. | | | | |

**Full CH-ID Saturation Check** *(per §8 -- PASS is prohibited without full saturation or a waiver)*:

| CH-ID | DOMAIN Status | LIFECYCLE Status | Full Saturation | Waiver (if needed) |
|-------|--------------|-----------------|-----------------|---------------------|
| CH-001 | Copy status from DOMAIN. | Copy status from LIFECYCLE. | FULLY SATURATED if both are ADDRESSED. UNSATURATED if either is PARTIAL or OPEN. | Write waiver text if needed, otherwise N/A. |
| CH-002 | Copy. | Copy. | Status. | N/A. |
| CH-003 | Copy if active. | Copy. | Status. | N/A. |

**CH-ID Final Assessment**:

| CH-ID | G_domain Status | G_lifecycle Status | Final Status | Notes |
|-------|----------------|-------------------|--------------|-------|
| CH-001 | Copy from DOMAIN verdict row. | Copy from LIFECYCLE verdict row. | DEFEATED if both reviewers ADDRESSED the claim. PARTIAL if one reviewer returned PARTIAL. HOLDS if either returned OPEN. | Any additional note. |
| CH-002 | Copy. | Copy. | Status. | |
| CH-003 | Copy if active. | Copy. | Status. | |

**Remaining gaps**: Write "All defeated" if no CH-ID holds. Otherwise list what remains unresolved.
**GClose Verdict**: Write PASS if g_null=DEFEATED and CH-IDs are all DEFEATED. Write CONDITIONAL or FAIL otherwise.
**Override invoked**: Write YES or NO.
**g_null Override**: Write "N/A -- formula applied" if no override. If overriding, write the justification in one sentence.
**GClose override authority**: GClose=FAIL overrides all prior verdicts per §3.
**GClose Rationale**: Write two to three sentences referencing g_null(final), CH-ID saturation state, and overall trajectory.

**Local Gate Ledger Row**:
| Section | Gate | Verdict | Class |
|---------|------|---------|-------|
| BRACKET CLOSING | GClose | Write verdict. | Write class. |

---

## §5.5 SCOPE COVERAGE RECONCILIATION

*(EXCLUDED from gate ledger per §6.)*

### Surface Coverage *(per §10)*

Map each §1 IN-SCOPE surface to the reviewer who addressed it. If no reviewer produced a
finding for a surface, classify it as GAP and add an ADVISORY-GAP item to the ACTION ITEM
REGISTER.

| IN-SCOPE Surface | Reviewer(s) | Finding Reference(s) | Coverage |
|-----------------|-------------|---------------------|----------|
| Copy §1 surface 1 with its domain annotation. | Name the reviewer role that produced a finding for this surface, or write "none". | List the finding references (e.g., DOMAIN F-1, LIFECYCLE F-1). Write N/A if no findings. | COVERED if at least one finding references this surface. GAP if none. |
| Surface 2. | Reviewer or "none". | References. | Coverage. |
| Surface 3. | Reviewer or "none". | References. | Coverage. |

**Surface coverage gate signal**: Write COVERED if all surfaces have findings. Write PARTIAL
followed by the count if any surfaces have no findings.

### Domain Coverage Gap-Check *(per §10a)*

Group §1 surfaces by their [DOMAIN: label] annotations. For each domain, identify whether
any APPLICABILITY MATRIX row with HIGH applicability covers that domain. If not, it is an
ADVISORY-GAP that must appear in the ACTION ITEM REGISTER.

| Artifact Domain | HIGH-Applicability MATRIX Rows | Coverage |
|----------------|-------------------------------|----------|
| Name the first artifact domain, drawn from §1 [DOMAIN: label] annotations. | List all APPLICABILITY MATRIX rows (by row ID, role, and lens entry summary) with HIGH applicability covering this domain. Write "none" if no row qualifies. | COVERED if at least one HIGH-applicability row covers this domain. ADVISORY-GAP if none. |
| Second domain. | AM rows or "none". | Coverage. |
| Third domain if applicable. | AM rows or "none". | Coverage. |

**§11 ADVISORY-ORPHAN check**: List any findings that lack a §1:S-n citation along with
their section, or write "None detected."

---

## GATE VECTOR TABLE

| Gate | Reviewer | Verdict | Contract Cite |
|------|----------|---------|---------------|
| GOpen -- bracket opening | Write the challenger role name. | Copy verdict. | DISPOSITION_CONTRACT v1 |
| G_domain_agg -- domain aggregate | Write the domain role name(s). | Copy verdict. | DISPOSITION_CONTRACT v1 |
| G_lifecycle -- lifecycle | Write the lifecycle role name. | Copy verdict. | DISPOSITION_CONTRACT v1 |
| GClose -- bracket closing | Write the challenger role name. | Copy verdict. | DISPOSITION_CONTRACT v1 |

---

## CROSS-ROLE SIGNALS

**Conflicts**: Identify any two reviewers who reached incompatible conclusions on the same
CH-ID or the same §1 surface. Name the conflict and explain why the conclusions are
incompatible. If no conflicts exist, write "None detected."

**Convergence**: Identify any concern raised independently by two or more reviewers without
coordination — a convergence point across roles. Name it and explain why independent
convergence makes it the highest-confidence finding in this review.

**Scope coverage**: List any §1 surfaces that no reviewer addressed at all, or write "None."

**§13 PROGRESSION LEDGER**:
```
g_null(initial)     = copy from BRACKET OPENING §17 derivation
g_null(post-domain) = copy from §3.5
g_null(final)       = copy from BRACKET CLOSING §9 Stage 3
Trajectory: write one of the following labels:
  MONOTONIC-PASS if each stage is >= the prior (on the PASS scale: DEFEATED > CONDITIONAL > HOLDS)
  MONOTONIC-FAIL if each stage is <= the prior
  DOMAIN-DEGRADED if g_null(post-domain) regressed from g_null(initial)
  LIFECYCLE-DEGRADED if g_null(final) regressed from g_null(post-domain)
  DOMAIN-RECOVERED if g_null(post-domain) improved from g_null(initial)
  LIFECYCLE-RECOVERED if g_null(final) improved from g_null(post-domain)
```
*This trajectory is informational. No gate ledger row is emitted.*

---

## DISPOSITION

**Gate vector**:
- GOpen = copy from GATE VECTOR TABLE
- G_domain_agg = copy
- G_lifecycle = copy
- GClose = copy

Apply §3 formula mechanically — evaluate the gates without editorial reasoning:
```
If GClose = FAIL: BLOCKED (challenger holds; null hypothesis not defeated)
If any other Gi = FAIL: BLOCKED
If no FAIL and at least one CONDITIONAL: CONDITIONAL
If all PASS: READY
```

**Overall Disposition**: Write READY, CONDITIONAL, or BLOCKED.

**Applying §16 rule**: State which rule number fired and exactly why.
**Primary Driver**: Write BRACKET CLOSING, DOMAIN, LIFECYCLE, BRACKET OPENING, or N/A.

**Conditions** *(write only if disposition is CONDITIONAL)*:
1. State the condition from the first CONDITIONAL gate in one sentence.
2. State additional conditions if more than one gate is CONDITIONAL.

**Blocker** *(write only if disposition is BLOCKED)*: Name the specific finding or verdict from
the FAIL gate. If GClose=FAIL, write "Challenger final verdict HOLDS -- " followed by the
GClose Rationale summary.

**RESOLUTION REGISTRY** *(write only if disposition is CONDITIONAL)*:
| Gate | Condition Summary | Resolution Owner | Resolution Criterion | Status |
|------|------------------|-----------------|---------------------|--------|
| Name the gate. | Summarize the condition in one sentence. | Name the role responsible for resolution. | Write a falsifiable test that is observable from outside the review. | OPEN |

*If disposition is not CONDITIONAL: "RESOLUTION REGISTRY: N/A -- disposition is [value]"*

---

## ACTION ITEM REGISTER

Copy all local gate ledger rows verbatim into this register first. Then add all advisory items
as described in §6. Every row traces to a source.

| Source | CH-ID / Finding | Item Description | Disposition Class | Owner Role | Resolution Criterion |
|--------|----------------|-----------------|------------------|------------|---------------------|
| Gate ledger copy. | -- | Write the exact text of the ledger row: Section / Gate / Verdict / Class. | Copy the class from the ledger. | Copy the reviewer role. | State the resolution criterion. |
| CH-ID item. | Write the CH-ID (e.g., CH-001). | Describe what must be done for any CH-ID with PARTIAL or HOLDS final status in BRACKET CLOSING. | Class. | Role. | Criterion. |
| Lens HIGH gap. | Write AM-0n / Q-n. | Write "ADVISORY-OPEN-LENS-REQUIRED: [full lens entry text] not addressed; HIGH applicability". | ADVISORY. | Role. | "Produce a finding addressing this lens entry for the artifact." |
| Lens MEDIUM gap. | AM-0n / Q-n. | Write "ADVISORY-OPEN-LENS: [full lens entry text] not addressed; MEDIUM applicability". | ADVISORY. | Role. | "Address this lens entry or provide justification for non-applicability." |
| Scope gap. | --. | Write "ADVISORY-GAP: §1 surface [surface name] not covered by any reviewer". | ADVISORY. | Role. | "Assign a reviewer with relevant lens coverage to this surface." |
| Domain gap. | --. | Write "ADVISORY-GAP (DOMAIN COVERAGE): [domain name] has no HIGH-applicability reviewer in APPLICABILITY MATRIX". | ADVISORY. | Role. | "Add a reviewer with HIGH applicability for [domain], or provide written justification for waiver." |
| Orphan finding. | --. | Write "ADVISORY-ORPHAN: finding [F-n] from [SECTION NAME] lacks a §1:S-n citation". | ADVISORY. | Role. | "Re-assign this finding to a valid §1 surface, or remove it and document the reason." |

---

**Artifact to review:**

{{artifact}}
